# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/aff8659a-12a1-49c5-abd3-438f536cf446.jsonl`
- **Structured JSON:** [`3463783d3f93f5f2fbe2.json`](../../sessions/34/3463783d3f93f5f2fbe2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T06:03:39.082Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T06:03:39.082Z",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 主证据锚定在 pairwise 层面（Few-NERD r=0.156 p<1e-11 已有，MAVEN 复现 r=0.09 p=0.003）， per-type partial r 作为 supporting evidence 方向正确但仅 marginal (p≈0.065)。 第二模型方向一致但效应量弱 (pairwise r=0.09)。Claim 1 措辞从 \"independently predicts\" 软化为 \"contributes to prediction beyond count, with strongest evidence at type-pair mechanistic level\"。 Claim 2 双通道基本 additive，2x2 interaction 不显著 (p=0.135)；error taxonomy 方向正确但不完全干净 (high-BCS type_substitution 47% vs low-BCS 18%，但 boundary_error 未完全分离)。 Claim 3 限定适用范围：SDGD 在 MAVEN (168 types) 增益 +4.0 F1 显著，Few-NERD (66 types) 仅 +2.3。 SDGD-cal 校准可弥补 SCS 噪声 (MAVEN +1.7 over zero)。方法学贡献 (frequency confound 发现、 batch→pairwise→per-type 分析演进) 作为独立 contribution。仍冲 EMNLP main，Findings 是现实 fallback。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T06:03:39.085Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T06:03:39.085Z",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-15T06:03:39.105Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 主证据锚定在 pairwise 层面（Few-NERD r=0.156 p<1e-11 已有，MAVEN 复现 r=0.09 p=0.003）， per-type partial r 作为 supporting evidence 方向正确但仅 marginal (p≈0.065)。 第二模型方向一致但效应量弱 (pairwise r=0.09)。Claim 1 措辞从 "independently predicts" 软化为 "contributes to prediction beyond count, with strongest evidence at type-pair mechanistic level"。 Claim 2 双通道基本 additive，2x2 interaction 不显著 (p=0.135)；error taxonomy 方向正确但不完全干净 (high-BCS type_substitution 47% vs low-BCS 18%，但 boundary_error 未完全分离)。 Claim 3 限定适用范围：SDGD 在 MAVEN (168 types) 增益 +4.0 F1 显著，Few-NERD (66 types) 仅 +2.3。 SDGD-cal 校准可弥补 SCS 噪声 (MAVEN +1.7 over zero)。方法学贡献 (frequency confound 发现、 batch→pairwise→per-type 分析演进) 作为独立 contribution。仍冲 EMNLP main，Findings 是现实 fallback。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "3dfd510b-06d4-4f29-9199-21e57daad274",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T06:03:39.104Z_

```json
{
  "parentUuid": "3dfd510b-06d4-4f29-9199-21e57daad274",
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
  "uuid": "00c4027d-923a-41d0-b7ea-f8ed608cbbe1",
  "timestamp": "2026-05-15T06:03:39.104Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T06:03:39.104Z_

```json
{
  "parentUuid": "00c4027d-923a-41d0-b7ea-f8ed608cbbe1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "120064cb-45bb-4ab6-b404-882bae682456",
  "timestamp": "2026-05-15T06:03:39.104Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
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
  "aiTitle": "Generate median-tier simulation paper for dream_20260515T053106",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Assistant

_source line 7 · 2026-05-15T06:03:41.603Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "120064cb-45bb-4ab6-b404-882bae682456",
  "isSidechain": false,
  "requestId": "req_011Cb3rBEg1NvNWtjCm3iHLm",
  "type": "assistant",
  "uuid": "f41d6f7d-56b5-4246-ab6f-cd359c9cede6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhryKQn6ysARp89Ubj363o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11427,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11427
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

_source line 8 · 2026-05-15T06:03:42.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dwf6cuBkrL9jP8YDd8H6yG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41d6f7d-56b5-4246-ab6f-cd359c9cede6",
  "isSidechain": false,
  "requestId": "req_011Cb3rBEg1NvNWtjCm3iHLm",
  "type": "assistant",
  "uuid": "ec270b38-3863-4c58-9f3b-bac6b17a0b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhryKQn6ysARp89Ubj363o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11427,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11427
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

_source line 9 · 2026-05-15T06:03:42.399Z_

<details><summary>↩ Tool result · `toolu_01Dwf6cuBkrL9jP8YDd8H6yG`</summary>

```text
1	[
2	  {
3	    "name": "MAVEN Confusability Study",
4	    "description": "在 MAVEN (168 FrameNet event types) 上复现 Few-NERD 核心发现：count curve + within-count BCS 相关 + pairwise BCS-confusion 分析。跨任务 (NER→ED) 验证 confusability independence。\n",
5	    "results": {
6	      "count_1_f1": 0.252,
7	      "count_1_precision": 0.17,
8	      "count_1_recall": 0.485,
9	      "count_1_pred_gold_ratio": 2.85,
10	      "count_6_f1": 0.218,
11	      "count_6_recall": 0.29,
12	      "count_14_f1": 0.198,
13	      "count_14_recall": 0.202,
14	      "count_28_f1": 0.21,
15	      "count_28_recall": 0.182,
16	      "count_56_f1": 0.192,
17	      "count_56_recall": 0.146,
18	      "count_84_f1": 0.168,
19	      "count_84_recall": 0.115,
20	      "count_168_f1": 0.135,
21	      "count_168_recall": 0.082,
22	      "pairwise_n_pairs": 14028,
23	      "pairwise_pearson_r": 0.09,
24	      "pairwise_pearson_p": 0.003,
25	      "pairwise_nonzero_spearman_rho": 0.15,
26	      "pairwise_nonzero_spearman_p": 0.025,
27	      "pairwise_count14_r": 0.06,
28	      "pairwise_count14_p": 0.042,
29	      "pairwise_count28_r": 0.1,
30	      "pairwise_count28_p": 0.009,
31	      "batch_f1_bcs_count14_r": 0.12,
32	      "batch_f1_bcs_count14_p": 0.42,
33	      "batch_f1_bcs_count28_r": 0.28,
34	      "batch_f1_bcs_count28_p": 0.14,
35	      "batch_f1_bcs_partial_r": 0.19,
36	      "batch_f1_bcs_partial_p": 0.24,
37	      "confusion_ratio_extreme_count14": 3.2,
38	      "confusion_ratio_extreme_count28": 2.8,
39	      "confusion_ratio_random_count14": 1.5,
40	      "confusion_ratio_random_count28": 1.9,
41	      "per_type_partial_r": 0.14,
42	      "per_type_partial_p": 0.11,
43	      "wrong_type_count_1": 0,
44	      "wrong_type_count_28": 3800,
45	      "wrong_type_count_168": 11500,
46	      "top_pair_1": "Giving <-> Sending (BCS=0.784, confusion=89)",
47	      "top_pair_2": "Attack <-> Hostile_encounter (BCS=0.761, confusion=72)",
48	      "top_pair_3": "Statement <-> Communication (BCS=0.738, confusion=65)"
49	    },
50	    "tables": [
51	      {
52	        "name": "MAVEN Count Curve (Qwen3-32B, V2 prompt)",
53	        "columns": [
54	          "count",
55	          "F1",
56	          "Precision",
57	          "Recall",
58	          "Pred/Gold",
59	          "WrongType_count"
60	        ],
61	        "rows": [
62	          [
63	            1,
64	            0.252,
65	            0.17,
66	            0.485,
67	            2.85,
68	            0
69	          ],
70	          [
71	            6,
72	            0.218,
73	            0.175,
74	            0.29,
75	            1.66,
76	            620
77	          ],
78	          [
79	            14,
80	            0.198,
81	            0.195,
82	            0.202,
83	            1.04,
84	            1850
85	          ],
86	          [
87	            28,
88	            0.21,
89	            0.248,
90	            0.182,
91	            0.73,
92	            3800
93	          ],
94	          [
95	            56,
96	            0.192,
97	            0.28,
98	            0.146,
99	            0.52,
100	            6200
101	          ],
102	          [
103	            84,
104	            0.168,
105	            0.305,
106	            0.115,
107	            0.38,
108	            8400
109	          ],
110	          [
111	            168,
112	            0.135,
113	            0.34,
114	            0.082,
115	            0.24,
116	            11500
117	          ]
118	        ]
119	      },
120	      {
121	        "name": "MAVEN Pairwise BCS-Confusion Analysis",
122	        "columns": [
123	          "subset",
124	          "n_pairs",
125	          "statistic",
126	          "value",
127	          "p"
128	        ],
129	        "rows": [
130	          [
131	            "all",
132	            14028,
133	            "Pearson r",
134	            0.09,
135	            0.003
136	          ],
137	          [
138	            "all",
139	            14028,
140	            "Spearman ρ",
141	            0.1,
142	            0.001
143	          ],
144	          [
145	            "count_14",
146	            12880,
147	            "Pearson r",
148	            0.06,
149	            0.042
150	          ],
151	          [
152	            "count_28",
153	            14028,
154	            "Pearson r",
155	            0.1,
156	            0.009
157	          ],
158	          [
159	            "nonzero_only",
160	            580,
161	            "Spearman ρ",
162	            0.15,
163	            0.025
164	          ]
165	        ]
166	      },
167	      {
168	        "name": "MAVEN Extreme Batch Confusion Ratio",
169	        "columns": [
170	          "count",
171	          "high_BCS_confusion_rate",
172	          "low_BCS_confusion_rate",
173	          "ratio"
174	        ],
175	        "rows": [
176	          [
177	            14,
178	            0.028,
179	            0.0088,
180	            3.2
181	          ],
182	          [
183	            28,
184	            0.038,
185	            0.0136,
186	            2.8
187	          ]
188	        ]
189	      }
190	    ],
191	    "figures": [],
192	    "analysis": "MAVEN 跨任务复现方向正确但效应量弱化。Pairwise 分析 (r=0.09, p=0.003) 仍 significant， 可作为 Claim 1 的 cross-task supporting evidence，但需承认效应量从 NER 的 r=0.156 降至 ED 的 0.09。 Per-type partial r 不显著 (p=0.11)，与 Few-NERD 的 marginal result 一致——两个数据集都显示 per-type 层面证据弱于 pairwise。论文叙事应强调：pairwise 分析是免疫 frequency confound 的 mechanistic 证据，cross-task 复现确认了现象的 task-agnostic 本质，但效应量的差异需 transparent 报告。 MAVEN 特有的 FrameNet 层级结构提供了额外的 qualitative 验证——top confused pairs 全部是 同层级 sibling events，与 FrameNet 文献的 14.6-19.8% sibling confusion rate 吻合。 Count curve 的更陡下降 (recall 从 0.485 到 0.082) 为 SDGD 在大 schema 上的增益提供了动机。\n\n\nMAVEN pairwise r=0.09 弱于 Few-NERD 的 0.156，原因：(1) 168 types 使 confusion 更分散， 每对 type 的 base confusion rate 更低，稀释了 SCS-confusion 相关；(2) event triggers 通常是 单 token (动词/名词)，surface form 变异小于 entity mention，boundary 信号不足以区分 type confusion； (3) FrameNet 事件类型的细粒度语义区分 (如 Giving vs Sending) 在 embedding space 中的 SCS 是不完美的 proxy——实际 confusion 受 context 影响更大。但因 n=14028 远大于 Few-NERD 的 1953， 即使 r=0.09 也 significant (p=0.003)。Batch-level 相关不显著 (p=0.24) 复现了 Few-NERD 的 frequency confound 问题——在 168 types 上此 confound 更严重因为 type frequency 分布更 skewed (MAVEN 长尾分布，少数高频 event type 主导)。Confusion ratio 在 extreme batches 仅 2.8-3.2x (vs Few-NERD 10-28x)，因 168 types 中极端 BCS batch 的 confusability contrast 被稀释。 Count curve 显示 recall 从 0.485 降至 0.082——比 Few-NERD (0.641→0.304) 更陡峭，因 168 types 远超模型 attention capacity。\n"
193	  },
194	  {
195	    "name": "DocRED Confusability Study",
196	    "description": "在 DocRED (96 relation types) 上测试 confusability independence。 Document-level RE 的 scaling stress test。\n",
197	    "results": {
198	      "count_1_f1": 0.095,
199	      "count_1_recall": 0.21,
200	      "count_6_f1": 0.082,
201	      "count_12_f1": 0.075,
202	      "count_24_f1": 0.068,
203	      "count_48_f1": 0.058,
204	      "count_96_f1": 0.042,
205	      "pairwise_n_pairs": 4560,
206	      "pairwise_pearson_r": 0.055,
207	      "pairwise_pearson_p": 0.065,
208	      "pairwise_nonzero_spearman_rho": 0.1,
209	      "pairwise_nonzero_spearman_p": 0.12,
210	      "per_type_partial_r": 0.08,
211	      "per_type_partial_p": 0.32
212	    },
213	    "tables": [
214	      {
215	        "name": "DocRED Count Curve (Qwen3-32B, V2 prompt)",
216	        "columns": [
217	          "count",
218	          "F1",
219	          "Precision",
220	          "Recall"
221	        ],
222	        "rows": [
223	          [
224	            1,
225	            0.095,
226	            0.058,
227	            0.21
228	          ],
229	          [
230	            6,
231	            0.082,
232	            0.055,
233	            0.175
234	          ],
235	          [
236	            12,
237	            0.075,
238	            0.062,
239	            0.095
240	          ],
241	          [
242	            24,
243	            0.068,
244	            0.07,
245	            0.066
246	          ],
247	          [
248	            48,
249	            0.058,
250	            0.078,
251	            0.046
252	          ],
253	          [
254	            96,
255	            0.042,
256	            0.085,
257	            0.028
258	          ]
259	        ]
260	      }
261	    ],
262	    "figures": [],
263	    "analysis": "DocRED 结果弱于预期，建议降级为 appendix 材料。主要价值：(1) 确认 count-recall 降解在 RE 任务上也存在 (Channel 1 task-agnostic)；(2) 暴露了 confusability 分析在 RE 上的局限—— type confusion 被更大的 task-specific confound 掩盖。论文不应将 DocRED 列为 Claim 1 的 核心证据，而是作为 \"boundary condition\" 讨论：confusability analysis 在 extraction 性能 极低 (<0.10 F1) 时信号被噪声淹没。如时间紧张 (P1 优先级)，可完全省略而不损害核心论点。\n\n\nDocRED 的 pairwise r 仅 0.055 (p=0.065，marginal)，原因：(1) document-level RE 的核心难度在于 entity pair identification 和 multi-hop reasoning，这些 confound 远大于 type confusability 的效应； (2) relation types 的 confusability 不仅来自语义相似 (如 headquarters_location vs place_of_birth)， 还来自 entity type 重叠——两者难以通过 SCS 单一维度捕获；(3) 96 types 但 document-level 评估的 样本量和信号都比 sentence-level NER/ED 更稀疏。训练-free LLM RE 的整体 F1 极低 (0.04-0.10)， 在此性能区间，噪声掩盖了 confusability 信号。此结果建议：论文报告 DocRED 作为 \"scaling stress test\" 但承认 RE 任务的额外 confound 限制了 confusability 信号的可检测性。可在 appendix 报告， 不作为主 claim 的核心证据。\n"
264	  },
265	  {
266	    "name": "Interaction Effect 2x2",
267	    "description": "Few-NERD 上 {count_6, count_22} × {low_BCS, high_BCS} 的 2×2 factorial design。 检验 count 和 confusability 的交互效应——additive vs multiplicative。\n",
268	    "results": {
269	      "count6_lowBCS_f1": 0.338,
270	      "count6_highBCS_f1": 0.28,
271	      "count22_lowBCS_f1": 0.318,
272	      "count22_highBCS_f1": 0.245,
273	      "count6_lowBCS_recall": 0.45,
274	      "count6_highBCS_recall": 0.412,
275	      "count22_lowBCS_recall": 0.295,
276	      "count22_highBCS_recall": 0.248,
277	      "count6_lowBCS_precision": 0.268,
278	      "count6_highBCS_precision": 0.215,
279	      "count22_lowBCS_precision": 0.352,
280	      "count22_highBCS_precision": 0.243,
281	      "count_main_effect_F": 8.2,
282	      "count_main_effect_p": 0.006,
283	      "count_main_effect_eta2": 0.12,
284	      "bcs_main_effect_F": 5.1,
285	      "bcs_main_effect_p": 0.028,
286	      "bcs_main_effect_eta2": 0.08,
287	      "interaction_F": 2.3,
288	      "interaction_p": 0.135,
289	      "interaction_eta2": 0.04,
290	      "additive_prediction_HH": 0.25,
291	      "actual_HH": 0.245,
292	      "super_additive_residual": -0.005,
293	      "count_effect_on_recall": -0.16,
294	      "count_effect_on_precision": 0.052,
295	      "bcs_effect_on_recall": -0.043,
296	      "bcs_effect_on_precision": -0.081,
297	      "n_per_cell": 12
298	    },
299	    "tables": [
300	      {
301	        "name": "2×2 Factorial Cell Means (F1 / Recall / Precision)",
302	        "columns": [
303	          "",
304	          "Low BCS",
305	          "High BCS",
306	          "BCS Effect"
307	        ],
308	        "rows": [
309	          [
310	            "Count=6",
311	            "0.338 / 0.450 / 0.268",
312	            "0.280 / 0.412 / 0.215",
313	            "-0.058 / -0.038 / -0.053"
314	          ],
315	          [
316	            "Count=22",
317	            "0.318 / 0.295 / 0.352",
318	            "0.245 / 0.248 / 0.243",
319	            "-0.073 / -0.047 / -0.109"
320	          ],
321	          [
322	            "Count Effect",
323	            "-0.020 / -0.155 / +0.084",
324	            "-0.035 / -0.164 / +0.028",
325	            ""
326	          ]
327	        ]
328	      },
329	      {
330	        "name": "Two-Way ANOVA Results",
331	        "columns": [
332	          "Source",
333	          "F",
334	          "p",
335	          "η²",
336	          "Verdict"
337	        ],
338	        "rows": [
339	          [
340	            "Count (main)",
341	            8.2,
342	            0.006,
343	            0.12,
344	            "Significant"
345	          ],
346	          [
347	            "BCS (main)",
348	            5.1,
349	            0.028,
350	            0.08,
351	            "Significant"
352	          ],
353	          [
354	            "Count × BCS",
355	            2.3,
356	            0.135,
357	            0.04,
358	            "Not significant"
359	          ]
360	        ]
361	      }
362	    ],
363	    "figures": [],
364	    "analysis": "两个 main effects 均显著 (p<0.05)，interaction 不显著 (p=0.135) → 支持 multi-channel model 的 基本 additive 假设。但 η²(interaction)=0.04 虽不显著，方向是 super-additive (实际 HH 比预测 差 0.5 点)，须在论文中 transparent 报告。Channel decomposition 清晰：count 主要影响 recall (Δ=-0.160)，BCS 主要影响 precision (Δ=-0.081)。但 BCS 也影响 recall (Δ=-0.043)，说明 confusability 不仅导致 type confusion (precision hit) 还导致部分 entity 被完全遗漏 (model 在 confusable types 间犹豫不决时选择不输出)。这为 Claim 2 提供细化： 两通道非完全正交，confusability 有 secondary recall 效应。\n\n\nCount 主效应显著 (F=8.2, p=0.006)：count_6 vs count_22 的 F1 差异 (~2.7 points) 主要由 recall 驱动 (0.431→0.272, Δ=-0.160)，确认 Channel 1 (count→recall) 机制。 BCS 主效应显著 (F=5.1, p=0.028)：low vs high BCS 的 F1 差异 (~6.5 points) 同时影响 recall 和 precision，但 precision 效应更大 (Δ=-0.081)，因为 type confusion 直接导致 precision 下降。 Interaction 不显著 (F=2.3, p=0.135)：additive 预测 (0.250) 与实际 (0.245) 仅差 0.5 point， slight super-additivity 因统计功效不足 (n=12/cell) 未达显著。机制解释：count 和 BCS 共享 下游 working memory 资源——当 count 已高时，BCS 的额外负担略微放大，但两个通道的主要机制 (attention allocation vs type discrimination) 仍大致独立。此结果支持 \"approximately orthogonal\" 但须将 \"orthogonal channels\" 措辞软化为 \"largely additive with marginal interaction\"。\n"
365	  },
366	  {
367	    "name": "Error Taxonomy by BCS Bin",
368	    "description": "系统 FP/FN 分类 (type_substitution / boundary_error / false_negative / hallucination)， 按 BCS bin 分层。Claim 2 的 mechanistic evidence。\n",
369	    "results": {
370	      "high_bcs_type_substitution_pct": 0.47,
371	      "high_bcs_boundary_error_pct": 0.12,
372	      "high_bcs_false_negative_pct": 0.33,
373	      "high_bcs_hallucination_pct": 0.08,
374	      "low_bcs_type_substitution_pct": 0.18,
375	      "low_bcs_boundary_error_pct": 0.15,
376	      "low_bcs_false_negative_pct": 0.55,
377	      "low_bcs_hallucination_pct": 0.12,
378	      "mid_bcs_type_substitution_pct": 0.3,
379	      "mid_bcs_false_negative_pct": 0.45,
380	      "type_sub_monotonic_increase_with_bcs": true,
381	      "false_neg_monotonic_decrease_with_bcs": true,
382	      "boundary_err_monotonic": false,
383	      "hallucination_monotonic": false,
384	      "type_sub_ratio_high_vs_low": 2.6,
385	      "chi2_type_sub_vs_bcs_bin": 18.4,
386	      "chi2_p": 0.001
387	    },
388	    "tables": [
389	      {
390	        "name": "Error Distribution by BCS Bin",
391	        "columns": [
392	          "BCS Bin",
393	          "type_substitution",
394	          "boundary_error",
395	          "false_negative",
396	          "hallucination",
397	          "n_errors"
398	        ],
399	        "rows": [
400	          [
401	            "[0, 0.3)",
402	            "18%",
403	            "15%",
404	            "55%",
405	            "12%",
406	            820
407	          ],
408	          [
409	            "[0.3, 0.5)",
410	            "30%",
411	            "14%",
412	            "45%",
413	            "11%",
414	            540
415	          ],
416	          [
417	            "[0.5, 0.7)",
418	            "42%",
419	            "11%",
420	            "38%",
421	            "9%",
422	            380
423	          ],
424	          [
425	            "[0.7, 1.0]",
426	            "52%",
427	            "13%",
428	            "28%",
429	            "7%",
430	            260
431	          ]
432	        ]
433	      },
434	      {
435	        "name": "Monotonicity Summary",
436	        "columns": [
437	          "Error Type",
438	          "Trend with BCS↑",
439	          "Monotonic?",
440	          "Chi² p"
441	        ],
442	        "rows": [
443	          [
444	            "type_substitution",
445	            "↑ (18→52%)",
446	            "Yes",
447	            "0.001"
448	          ],
449	          [
450	            "boundary_error",
451	            "≈flat (11-15%)",
452	            "No",
453	            "0.62"
454	          ],
455	          [
456	            "false_negative",
457	            "↓ (55→28%)",
458	            "Yes",
459	            "0.003"
460	          ],
461	          [
462	            "hallucination",
463	            "↓ slight (12→7%)",
464	            "No (non-monotonic at mid)",
465	            "0.18"
466	          ]
467	        ]
468	      }
469	    ],
470	    "figures": [],
471	    "analysis": "Error taxonomy 提供了 multi-channel model 最直接的 mechanistic 支持：type_substitution 从 18% (low BCS) 上升到 52% (high BCS)，false_negative 从 55% 下降到 28%。这确认了 confusability 驱动 type confusion (Channel 2) 而 count/attention dilution 驱动 entity omission (Channel 1)。 但趋势的不完全干净 (boundary_error 无 BCS 趋势、hallucination 非单调) 要求在论文中用 \"dominant error modes shift\" 而非 \"exclusive channels\" 的措辞。Chi-square 显著 (p=0.001) 确保 type_substitution-BCS 关系有统计支撑。此分析与 exp-002 的 confusion ratio (10-28x) 互补——后者量化了 confusability 对混淆频率的影响，前者量化了 confusability 对 error 类型分布的影响。\n\n\nHigh-BCS batch 中 type_substitution 占 47%：当 batch 内包含语义相近的 types (如 person-athlete vs person-artist)，模型正确识别 entity span 但选错 type——这正是 confusability 的直接机械效应。 Low-BCS batch 中 false_negative 占 55%：当 types 不 confusable 时，主要错误模式变为 entity 遗漏 (模型在 prompt 中看到多个不相关 types，attention 分散导致某些 types 的 entities 被忽略)。 趋势不完全干净的原因：(1) boundary_error 不随 BCS 单调变化——它受 entity mention 的 surface form 模糊性影响 (如 \"New York City\" vs \"New York\")，与 type confusability 部分独立； (2) hallucination 在各 bin 间波动 (8-12%)，因为 hallucination 主要由模型的 parametric knowledge 驱动，与 batch confusability 无关。Chi-square 检验确认 type_substitution 比例与 BCS bin 显著 相关 (p=0.001)，但整体 error taxonomy 不是完美的 four-way separation。\n"
472	  },
473	  {
474	    "name": "Multi-Model Validation (LLaMA-3.3-70B)",
475	    "description": "用 LLaMA-3.3-70B-Instruct 复现 exp-002 protocol on Few-NERD。 验证 confusability independence 非 model-specific artifact。\n",
476	    "results": {
477	      "model2_full_schema_f1": 0.385,
478	      "model2_full_schema_precision": 0.59,
479	      "model2_full_schema_recall": 0.285,
480	      "model2_count1_f1": 0.295,
481	      "model2_count1_recall": 0.595,
482	      "model2_count6_f1": 0.278,
483	      "model2_count6_recall": 0.43,
484	      "model2_count12_f1": 0.31,
485	      "model2_count12_recall": 0.305,
486	      "model2_count64_f1": 0.385,
487	      "model2_count64_recall": 0.285,
488	      "model2_pairwise_all_r": 0.09,
489	      "model2_pairwise_all_p": 0.012,
490	      "model2_pairwise_count6_r": 0.04,
491	      "model2_pairwise_count6_p": 0.12,
492	      "model2_pairwise_count12_r": 0.11,
493	      "model2_pairwise_count12_p": 0.008,
494	      "model2_pairwise_nonzero_spearman": 0.17,
495	      "model2_pairwise_nonzero_p": 0.032,
496	      "model2_f1_bcs_partial_r": 0.22,
497	      "model2_f1_bcs_partial_p": 0.11,
498	      "model2_f1_bcs_count12_r": 0.38,
499	      "model2_f1_bcs_count12_p": 0.048,
500	      "model2_per_type_partial_r": 0.15,
501	      "model2_per_type_partial_p": 0.082,
502	      "model2_confusion_ratio_extreme_count12": 7.5,
503	      "model2_confusion_ratio_extreme_count6": 15.2,
504	      "model2_top_pair": "person-other <-> person-politician (BCS=0.934, confusion=118)"
505	    },
506	    "tables": [
507	      {
508	        "name": "Cross-Model Pairwise Comparison",
509	        "columns": [
510	          "Metric",
511	          "Qwen3-32B",
512	          "LLaMA-3.3-70B",
513	          "Direction Consistent?"
514	        ],
515	        "rows": [
516	          [
517	            "Pairwise r (all)",
518	            0.156,
519	            0.09,
520	            "Yes (positive)"
521	          ],
522	          [
523	            "Pairwise p (all)",
524	            "4.6e-12",
525	            0.012,
526	            "Both significant"
527	          ],
528	          [
529	            "Pairwise r (count_6)",
530	            0.078,
531	            0.04,
532	            "Yes but LLaMA n.s."
533	          ],
534	          [
535	            "Pairwise r (count_12)",
536	            0.147,
537	            0.11,
538	            "Yes"
539	          ],
540	          [
541	            "Nonzero Spearman ρ",
542	            0.254,
543	            0.17,
544	            "Yes"
545	          ],
546	          [
547	            "Confusion ratio (extreme, c12)",
548	            "9.9x",
549	            "7.5x",
550	            "Yes"
551	          ],
552	          [
553	            "Top confused pair",
554	            "person-other↔politician",
555	            "person-other↔politician",
556	            "Same pair"
557	          ]
558	        ]
559	      },
560	      {
561	        "name": "LLaMA-3.3-70B Count Curve",
562	        "columns": [
563	          "count",
564	          "F1",
565	          "Precision",
566	          "Recall"
567	        ],
568	        "rows": [
569	          [
570	            1,
571	            0.295,
572	            0.195,
573	            0.595
574	          ],
575	          [
576	            6,
577	            0.278,
578	            0.208,
579	            0.43
580	          ],
581	          [
582	            12,
583	            0.31,
584	            0.33,
585	            0.305
586	          ],
587	          [
588	            22,
589	            0.275,
590	            0.315,
591	            0.245
592	          ],
593	          [
594	            44,
595	            0.398,
596	            0.465,
597	            0.348
598	          ],
599	          [
600	            64,
601	            0.385,
602	            0.59,
603	            0.285
604	          ]
605	        ]
606	      }
607	    ],
608	    "figures": [],
609	    "analysis": "Multi-model validation 确认 confusability-confusion 关系非 model-specific：方向一致、top confused pair 相同、confusion ratio 均为正。但效应量差异 (0.156 vs 0.09) 要求论文承认 \"effect size varies across model families\"。count_6 在 LLaMA 上不显著是功效问题 (小样本 + 弱效应)， 不影响 main claim。论文应报告 cross-model comparison table，强调方向一致性而非效应量匹配。 满足 reviewer \">=2 models\" 要求，但 reviewer 可能追问为什么效应量减半——准备好解释： 不同模型的 internal representation 与 static embedding SCS 的对齐程度不同。\n\n\nLLaMA-3.3-70B 的 pairwise r=0.09 弱于 Qwen3-32B 的 0.156，原因：(1) 不同模型家族对 type confusability 有不同的 sensitivity——LLaMA 的 instruction following 和 NER 能力与 Qwen 不同， 某些 confusable pairs (如 location subtypes) LLaMA 处理更好，其他 (如 person subtypes) 更差， 导致总体 BCS-confusion 相关被 partial cancellation 削弱；(2) LLaMA-3.3 在 70B scale 上的 in-context learning 能力可能使其对 type description 的 discrimination 更好，降低了 embedding SCS 的预测力 (模型实际 confusion pattern 与 static embedding SCS 的偏差更大)。 count_6 pairwise r 不显著 (p=0.12) 因为 6 types 下 confusion event 很少——每个 batch 只有 C(6,2)=15 个 type pair，大多数 confusion count 为 0，统计检验功效不足。count_12 仍显著 (r=0.11, p=0.008)。Top confused pair 仍是 person-other ↔ person-politician (确认 confusion 结构 model-agnostic)。整体全 schema F1=0.385 略低于 Qwen3 的 0.414，可能因 70B < 32B (FP8 quantization 使 Qwen3-32B 的有效参数更多) 或 model architecture 差异。\n"
610	  },
611	  {
612	    "name": "SDGD-zero on Few-NERD",
613	    "description": "Confusability-minimizing batch composition via embedding SCS + graph coloring on Few-NERD (66 types)。 与 single-pass full-schema baseline 对比。\n",
614	    "results": {
615	      "scs_threshold": 0.5,
616	      "n_edges_above_threshold": 85,
617	      "chromatic_number": 10,
618	      "avg_batch_size": 6.6,
619	      "max_batch_size": 9,
620	      "min_batch_size": 4,
621	      "max_within_batch_scs": 0.42,
622	      "sdgd_zero_f1": 0.437,
623	      "sdgd_zero_precision": 0.405,
624	      "sdgd_zero_recall": 0.474,
625	      "single_pass_f1": 0.414,
626	      "single_pass_precision": 0.648,
627	      "single_pass_recall": 0.304,
628	      "f1_gain_over_single": 2.3,
629	      "n_merge_conflicts": 145,
630	      "merge_conflict_resolution": "confidence-based (max logprob)",
631	      "pct_docs_with_conflicts": 0.18,
632	      "sdgd_wrong_type_count": 1280,
633	      "single_pass_wrong_type_count": 2050,
634	      "wrong_type_reduction_pct": 0.375,
635	      "api_calls_per_doc": 10,
636	      "wall_clock_ratio_vs_single": 8.5
637	    },
638	    "tables": [
639	      {
640	        "name": "SDGD-zero vs Single-Pass on Few-NERD",
641	        "columns": [
642	          "Method",
643	          "Batches",
644	          "F1",
645	          "Precision",
646	          "Recall",
647	          "WrongType",
648	          "API Calls"
649	        ],
650	        "rows": [
651	          [
652	            "Single-pass",
653	            1,
654	            0.414,
655	            0.648,
656	            0.304,
657	            2050,
658	            1
659	          ],
660	          [
661	            "SDGD-zero",
662	            10,
663	            0.437,
664	            0.405,
665	            0.474,
666	            1280,
667	            10
668	          ],
669	          [
670	            "Δ",
671	            "",
672	            "+2.3",
673	            "-24.3",
674	            "+17.0",
675	            "-37.5%",
676	            "+9"
677	          ]
678	        ]
679	      },
680	      {
681	        "name": "SDGD Batch Composition Summary",
682	        "columns": [
683	          "Batch",
684	          "Size",
685	          "Max Intra-Batch SCS",
686	          "Example Types"
687	        ],
688	        "rows": [
689	          [
690	            1,
691	            7,
692	            0.38,
693	            "person-athlete, event-protest, product-car, ..."
694	          ],
695	          [
696	            2,
697	            6,
698	            0.35,
699	            "location-city, art-music, organization-company, ..."
700	          ],
701	          [
702	            3,
703	            8,
704	            0.42,
705	            "person-politician, building-library, event-election, ..."
706	          ],
707	          [
708	            "...",
709	            "...",
710	            "...",
711	            "..."
712	          ],
713	          [
714	            10,
715	            5,
716	            0.28,
717	            "other-disease, other-currency, other-language, ..."
718	          ]
719	        ]
720	      }
721	    ],
722	    "figures": [],
723	    "analysis": "Few-NERD 上 SDGD-zero 的 +2.3 F1 增益在统计上 marginal (需报 confidence interval)。 主要价值在于方向验证——wrong type reduction (37.5%) 确认 confusability-aware grouping 的 mechanistic 效果。但在 66-type schema 上，SDGD 的 practical significance 有限—— single-pass 已 decent，decomposition 的额外 API cost (10x) 可能不值得。 论文应将 Few-NERD 结果定位为 \"proof of concept\"，MAVEN 结果才是 \"practical demonstration\"。 Precision-recall tradeoff (precision 下降 24 points but recall 上升 17 points) 需要在论文中 讨论：SDGD 的 batch size reduction 解决了 under-prediction 问题，但引入了 over-prediction。 future work 可结合 SDGD + per-type precision calibration。\n\n\nSDGD-zero 在 66-type Few-NERD 上增益有限 (+2.3 F1) 的原因：(1) 66 types 的 confusability 负担中等——只有 ~85 个 type pair SCS>0.5 (out of C(66,2)=2145)，graph coloring 的优化空间 有限；(2) single-pass baseline 在 V2 prompt 下已达 F1=0.414，under-prediction (pred/gold=0.47) 是主要瓶颈——SDGD 通过降低 batch size 提升了 recall (+0.170) 但同时降低了 precision (-0.243)， 因为小 batch 促使模型 over-predict；(3) merge step 引入 ~145 个 span conflict (18% docs 受影响)， confidence-based resolution 不完美——部分 conflict 解决错误抵消了 confusability reduction 的收益。 Wrong type count 从 2050 降至 1280 (减少 37.5%) 是 SDGD 的直接 mechanistic 效果—— confusable types 被分到不同 batch 后 type confusion 减少。但 F1 gain 仅 2.3 是因为 wrong type reduction 只是 overall error 的一部分——false negative 和 boundary error 未被 SDGD 直接解决。 结论：66 types 属于 \"中等 schema\"，SDGD 增益 marginal，consistent with median tier 定义。\n"
724	  },
725	  {
726	    "name": "SDGD-zero on MAVEN",
727	    "description": "SDGD-zero on MAVEN (168 event types)。与 single-pass + random batching 对比。 Cross-task validation of SDGD framework (NER→ED)。\n",
728	    "results": {
729	      "scs_threshold": 0.45,
730	      "n_edges_above_threshold": 230,
731	      "chromatic_number": 22,
732	      "avg_batch_size": 7.6,
733	      "max_batch_size": 11,
734	      "min_batch_size": 5,
735	      "max_within_batch_scs": 0.4,
736	      "sdgd_zero_f1": 0.175,
737	      "sdgd_zero_precision": 0.19,
738	      "sdgd_zero_recall": 0.162,
739	      "single_pass_f1": 0.135,
740	      "single_pass_recall": 0.082,
741	      "random_k22_f1": 0.155,
742	      "random_k22_recall": 0.138,
743	      "f1_gain_over_single": 4.0,
744	      "f1_gain_over_random": 2.0,
745	      "sdgd_vs_single_p": 0.002,
746	      "sdgd_vs_random_p": 0.038,
747	      "sdgd_wrong_type_count": 4200,
748	      "single_pass_wrong_type_count": 11500,
749	      "random_wrong_type_count": 6800,
750	      "api_calls_per_doc": 22,
751	      "wall_clock_ratio_vs_single": 18.5,
752	      "wall_clock_ratio_vs_pertype": 0.2
753	    },
754	    "tables": [
755	      {
756	        "name": "SDGD-zero Comparison on MAVEN (168 types)",
757	        "columns": [
758	          "Method",
759	          "Batches",
760	          "F1",
761	          "Precision",
762	          "Recall",
763	          "WrongType",
764	          "p vs SDGD"
765	        ],
766	        "rows": [
767	          [
768	            "Single-pass",
769	            1,
770	            0.135,
771	            0.34,
772	            0.082,
773	            11500,
774	            0.002
775	          ],
776	          [
777	            "Random (k=22)",
778	            22,
779	            0.155,
780	            0.175,
781	            0.138,
782	            6800,
783	            0.038
784	          ],
785	          [
786	            "SDGD-zero (k=22)",
787	            22,
788	            0.175,
789	            0.19,
790	            0.162,
791	            4200,
792	            "—"
793	          ]
794	        ]
795	      },
796	      {
797	        "name": "Cross-Task SDGD Gain Summary",
798	        "columns": [
799	          "Dataset",
800	          "Types",
801	          "SDGD-zero F1",
802	          "Single F1",
803	          "Δ F1",
804	          "Δ WrongType%"
805	        ],
806	        "rows": [
807	          [
808	            "Few-NERD",
809	            66,
810	            0.437,
811	            0.414,
812	            "+2.3",
813	            "-37.5%"
814	          ],
815	          [
816	            "MAVEN",
817	            168,
818	            0.175,
819	            0.135,
820	            "+4.0",
821	            "-63.5%"
822	          ]
823	        ]
824	      }
825	    ],
826	    "figures": [],
827	    "analysis": "MAVEN 结果确认 SDGD 在大 schema (168 types) 上有 substantial 增益——F1 gain +4.0 显著 (p=0.002)。与 Few-NERD 的 +2.3 对比形成清晰趋势：SDGD 的价值随 schema complexity (type count × confusability density) 递增。Cross-task 成功 (NER → ED) 支持 SDGD 的 task-agnostic 性质。Random ablation (Δ=+2.0) 确认 confusability-aware grouping 的独立 贡献超越 mere batch count reduction。Wrong type 63.5% 减少是 SDGD 的 headline mechanistic result。论文应将此作为 Claim 3 的 primary evidence，Few-NERD 作为 secondary。 局限性：absolute F1=0.175 仍很低——SDGD 改善了 relative performance 但 training-free ED 在 168 types 上仍远落后 supervised method。须在论文中 frame 为 \"SDGD narrows the gap but does not close it\" 并指出 remaining error 来自 non-confusability sources (count capacity, event trigger ambiguity)。\n\n\nMAVEN 上 SDGD-zero 增益更大 (+4.0 F1 over single-pass, +2.0 over random) 的原因： (1) 168 types 的 single-pass baseline 极差 (F1=0.135)——模型在一个 prompt 中处理 168 个 event type definition 时严重过载，recall 仅 0.082；SDGD 将 batch size 降至 ~7.6 types， recall 从 0.082 提升至 0.162 (几乎翻倍)；(2) FrameNet 层级中 sibling types 的 BCS 很高 (119 pairs > 0.5)，random batching 让这些 sibling 有 ~1/22 概率共现——SDGD 将此概率降至零， 减少了 FrameNet-specific type confusion；(3) wrong type 从 11500 降至 4200 (63% reduction)， 远高于 Few-NERD 的 37.5%，说明 confusability-aware grouping 在大 schema 上价值递增。 SDGD vs random delta (+2.0 F1) 隔离了 confusability-aware grouping 的 contribution—— random 也帮助 (by reducing count per batch) 但 SDGD 额外分离了 confusable types。 p=0.002 (vs single-pass) 和 p=0.038 (vs random) 确认显著性。 此结果是论文 Claim 3 的核心证据——在 ≥100 types 的大 schema 上 SDGD 有 practical significance。\n"
828	  },
829	  {
830	    "name": "SDGD-cal on Few-NERD",
831	    "description": "用 5-10 calibration examples 构建 empirical confusion matrix，替换 embedding SCS 做 graph coloring。对比 SDGD-zero。\n",
832	    "results": {
833	      "n_calibration_examples": 8,
834	      "calibration_api_calls": 528,
835	      "empirical_confusion_pairs_discovered": 42,
836	      "overlap_with_scs_top50": 0.62,
837	      "sdgd_cal_f1": 0.449,
838	      "sdgd_cal_precision": 0.415,
839	      "sdgd_cal_recall": 0.488,
840	      "sdgd_zero_f1": 0.437,
841	      "f1_gain_over_zero": 1.2,
842	      "n_batches_changed": 4,
843	      "types_reassigned": 8,
844	      "new_chromatic_number": 11,
845	      "sdgd_cal_vs_zero_p": 0.15
846	    },
847	    "tables": [
848	      {
849	        "name": "SDGD-cal vs SDGD-zero on Few-NERD",
850	        "columns": [
851	          "Method",
852	          "F1",
853	          "P",
854	          "R",
855	          "Calibration Cost"
856	        ],
857	        "rows": [
858	          [
859	            "SDGD-zero",
860	            0.437,
861	            0.405,
862	            0.474,
863	            "0 examples"
864	          ],
865	          [
866	            "SDGD-cal",
867	            0.449,
868	            0.415,
869	            0.488,
870	            "8 examples (528 API calls)"
871	          ],
872	          [
873	            "Δ",
874	            "+1.2",
875	            "+1.0",
876	            "+1.4",
877	            ""
878	          ]
879	        ]
880	      },
881	      {
882	        "name": "SCS vs Empirical Confusion Discrepancies (Top 5)",
883	        "columns": [
884	          "Type Pair",
885	          "SCS",
886	          "Empirical Confusion",
887	          "Direction"
888	        ],
889	        "rows": [
890	          [
891	            "art-film ↔ art-broadcastprogram",
892	            0.38,
893	            12,
894	            "SCS underestimates"
895	          ],
896	          [
897	            "person-director ↔ person-actor",
898	            0.41,
899	            9,
900	            "SCS underestimates"
901	          ],
902	          [
903	            "organization-religion ↔ organization-political",
904	            0.72,
905	            0,
906	            "SCS overestimates"
907	          ],
908	          [
909	            "location-park ↔ location-island",
910	            0.65,
911	            1,
912	            "SCS overestimates"
913	          ],
914	          [
915	            "person-other ↔ person-scholar",
916	            0.88,
917	            45,
918	            "SCS accurate"
919	          ]
920	        ]
921	      }
922	    ],
923	    "figures": [],
924	    "analysis": "Few-NERD 上 SDGD-cal 增益不显著 (p=0.15)，但 mechanistic insight 有价值：SCS 与 empirical confusion 的 overlap 为 62% 意味着 embedding proxy 的 precision 约为 0.62——足以用于 zero-shot SDGD 但有改进空间。SCS 的主要失败模式：(1) 低估跨 subtree 的 confusion (如 art-film ↔ art-broadcastprogram 在 Few-NERD hierarchy 中不是 direct sibling 但实际 highly confused)；(2) 高估有明确区分特征的 pairs (如 religion ↔ political 虽语义相近但 entity mention 有明确 lexical 区分)。这些 insight 为 exp-015 (SCS validation) 提供预期框架。 对论文的贡献：SDGD-cal 作为 \"how much room for improvement exists over zero-shot\" 的 upper bound indicator，即使在 66-type schema 上增量有限。\n\n\nSDGD-cal 比 SDGD-zero 仅 +1.2 F1 的原因：(1) 8 个 calibration example 对 66×66 confusion matrix 的估计很稀疏——C(66,2)=2145 个 pair 中只有 ~42 个被经验观察到 confused，其余是零， matrix 极度 sparse；(2) SCS top-50 confusable pairs 中 62% 与 empirical confusion 重合—— embedding proxy 已捕获主要 confusion 结构，calibration 只修正了 38% 的 \"surprise\" pairs； (3) 修正的 8 个 type 重新分配只影响了 4 个 batch，global batch structure 变化有限。 Calibration 的主要价值在于发现 SCS 低估的 confusable pairs (如 art-film ↔ art-broadcastprogram， SCS=0.38 但 empirical confusion=12) 和 SCS 高估的 pairs (如 organization-religion ↔ organization-political，SCS=0.72 但 confusion=0)。p=0.15 不显著——在 66-type schema 上 calibration 的增量太小。此结果建议 SDGD-cal 的价值在大 schema 上更大 (where SCS noise affects more pairs)。\n"
925	  },
926	  {
927	    "name": "SDGD-cal on MAVEN",
928	    "description": "SDGD-cal on MAVEN (168 event types)。Empirical calibration on 168 types with 5-10 examples。 Full comparison table。\n",
929	    "results": {
930	      "n_calibration_examples": 8,
931	      "calibration_api_calls": 1344,
932	      "empirical_confusion_pairs_discovered": 128,
933	      "overlap_with_scs_top100": 0.48,
934	      "sdgd_cal_f1": 0.192,
935	      "sdgd_cal_precision": 0.205,
936	      "sdgd_cal_recall": 0.18,
937	      "sdgd_zero_f1": 0.175,
938	      "f1_gain_over_zero": 1.7,
939	      "sdgd_cal_vs_zero_p": 0.045,
940	      "types_reassigned": 24,
941	      "new_chromatic_number": 24,
942	      "sdgd_cal_wrong_type": 3500,
943	      "sdgd_zero_wrong_type": 4200,
944	      "wrong_type_reduction_vs_zero": 0.167
945	    },
946	    "tables": [
947	      {
948	        "name": "Full Comparison Table — MAVEN",
949	        "columns": [
950	          "Method",
951	          "k",
952	          "F1",
953	          "P",
954	          "R",
955	          "WrongType",
956	          "Total API Calls",
957	          "p vs best"
958	        ],
959	        "rows": [
960	          [
961	            "Single-pass",
962	            1,
963	            0.135,
964	            0.34,
965	            0.082,
966	            11500,
967	            710,
968	            "<0.001"
969	          ],
970	          [
971	            "Random (k=22)",
972	            22,
973	            0.155,
974	            0.175,
975	            0.138,
976	            6800,
977	            15620,
978	            0.005
979	          ],
980	          [
981	            "SDGD-zero",
982	            22,
983	            0.175,
984	            0.19,
985	            0.162,
986	            4200,
987	            15620,
988	            0.045
989	          ],
990	          [
991	            "SDGD-cal",
992	            24,
993	            0.192,
994	            0.205,
995	            0.18,
996	            3500,
997	            "15620+1344",
998	            "—"
999	          ],
1000	          [
1001	            "Per-type",
1002	            168,
1003	            0.195,
1004	            0.15,
1005	            0.28,
1006	            1800,
1007	            119280,
1008	            0.82
1009	          ]
1010	        ]
1011	      },
1012	      {
1013	        "name": "Full Comparison Table — Few-NERD",
1014	        "columns": [
1015	          "Method",
1016	          "k",
1017	          "F1",
1018	          "P",
1019	          "R",
1020	          "WrongType",
1021	          "Total API Calls",
1022	          "p vs best"
1023	        ],
1024	        "rows": [
1025	          [
1026	            "Single-pass",
1027	            1,
1028	            0.414,
1029	            0.648,
1030	            0.304,
1031	            2050,
1032	            500,
1033	            0.003
1034	          ],
1035	          [
1036	            "Random (k=10)",
1037	            10,
1038	            0.423,
1039	            0.395,
1040	            0.455,
1041	            1650,
1042	            5000,
1043	            0.08
1044	          ],
1045	          [
1046	            "SDGD-zero",
1047	            10,
1048	            0.437,
1049	            0.405,
1050	            0.474,
1051	            1280,
1052	            5000,
1053	            0.15
1054	          ],
1055	          [
1056	            "SDGD-cal",
1057	            11,
1058	            0.449,
1059	            0.415,
1060	            0.488,
1061	            1100,
1062	            "5000+528",
1063	            "—"
1064	          ],
1065	          [
1066	            "Per-type",
1067	            66,
1068	            0.47,
1069	            0.385,
1070	            0.602,
1071	            650,
1072	            33000,
1073	            0.18
1074	          ]
1075	        ]
1076	      }
1077	    ],
1078	    "figures": [],
1079	    "analysis": "MAVEN 上 SDGD-cal 是最佳方法 (F1=0.192)，但与 per-type splitting (F1=0.195) 几乎持平 (p=0.82 no significant difference)——这出乎意料地好，因为 SDGD-cal 只用 24 batches vs per-type 的 168。Cost-effectiveness 是 SDGD 的核心卖点：相近质量，~15% latency。 Cross-dataset 对比揭示 SDGD 的适用范围：(1) ≥100 types: SDGD-zero already significant, SDGD-cal further improves; (2) 30-66 types: gains marginal, calibration not cost-effective; (3) <30 types: SDGD unnecessary (single-pass sufficient)。这为论文的 Claim 3 限定了清晰的 适用条件。Full comparison table (两个 dataset × 五种方法) 是论文 Table 1 的核心。\n\n\nSDGD-cal 在 MAVEN 上增益更大 (+1.7 F1, p=0.045 marginal significant)，原因： (1) 168 types 使 SCS 的累积误差更大——SCS top-100 confusable pairs 中只有 48% 与 empirical confusion 重合 (vs Few-NERD 的 62%)，因为 FrameNet 事件类型的细粒度语义区分在 embedding space 中表示不够准确 (如 Giving vs Commerce_sell, SCS=0.35 但 empirical confusion 高)； (2) calibration 发现了 24 个需要重新分配的 types (vs Few-NERD 的 8)，batch 结构变化更大； (3) wrong type 进一步减少 16.7% (4200→3500) 确认 calibration 修正了 SCS 的 false negatives。 Marginal significance (p=0.045) 勉强过线，robustness 需额外 validation——如换 random seed 重复 calibration sampling，p 值可能波动到 0.05 以上。此结果支持 \"calibration 对大 schema 有价值\"，但收益的 cost-effectiveness (1344 额外 API 调用换 +1.7 F1) 需在论文中讨论。\n"
1080	  },
1081	  {
1082	    "name": "Random Batching Ablation",
1083	    "description": "Same batch count k as SDGD, random composition。隔离 confusability-aware grouping 的增量贡献。\n",
1084	    "results": {
1085	      "random_k10_fewnerd_f1": 0.423,
1086	      "random_k10_fewnerd_precision": 0.395,
1087	      "random_k10_fewnerd_recall": 0.455,
1088	      "sdgd_zero_fewnerd_f1": 0.437,
1089	      "delta_fewnerd": 1.4,
1090	      "delta_fewnerd_p": 0.08,
1091	      "random_k22_maven_f1": 0.155,
1092	      "sdgd_zero_maven_f1": 0.175,
1093	      "delta_maven": 2.0,
1094	      "delta_maven_p": 0.018,
1095	      "random_mean_within_batch_bcs_fewnerd": 0.285,
1096	      "sdgd_mean_within_batch_bcs_fewnerd": 0.168,
1097	      "random_mean_within_batch_bcs_maven": 0.235,
1098	      "sdgd_mean_within_batch_bcs_maven": 0.145,
1099	      "random_f1_std_fewnerd": 0.008,
1100	      "random_f1_std_maven": 0.006,
1101	      "n_random_seeds": 5
1102	    },
1103	    "tables": [
1104	      {
1105	        "name": "Random vs SDGD Ablation",
1106	        "columns": [
1107	          "Dataset",
1108	          "Single-pass F1",
1109	          "Random F1 (mean±σ)",
1110	          "SDGD-zero F1",
1111	          "Δ Random",
1112	          "Δ SDGD-Random",
1113	          "p (SDGD vs Rand)"
1114	        ],
1115	        "rows": [
1116	          [
1117	            "Few-NERD (66)",
1118	            0.414,
1119	            "0.423±0.008",
1120	            0.437,
1121	            "+0.9",
1122	            "+1.4",
1123	            0.08
1124	          ],
1125	          [
1126	            "MAVEN (168)",
1127	            0.135,
1128	            "0.155±0.006",
1129	            0.175,
1130	            "+2.0",
1131	            "+2.0",
1132	            0.018
1133	          ]
1134	        ]
1135	      },
1136	      {
1137	        "name": "Within-Batch BCS Analysis",
1138	        "columns": [
1139	          "Method",
1140	          "Mean Within-Batch BCS (Few-NERD)",
1141	          "Mean Within-Batch BCS (MAVEN)"
1142	        ],
1143	        "rows": [
1144	          [
1145	            "Random",
1146	            0.285,
1147	            0.235
1148	          ],
1149	          [
1150	            "SDGD-zero",
1151	            0.168,
1152	            0.145
1153	          ],
1154	          [
1155	            "Reduction",
1156	            "-41%",
1157	            "-38%"
1158	          ]
1159	        ]
1160	      }
1161	    ],
1162	    "figures": [],
1163	    "analysis": "Ablation 成功隔离了两个 contribution：batch size reduction (Channel 1) 和 confusability-aware grouping (Channel 2)。在 MAVEN 上两者贡献相当 (各 +2.0 F1)；在 Few-NERD 上 Channel 1 贡献较小 (+0.9) 因为 66 types 的 single-pass recall (0.304) 虽不高但不 catastrophic。 SDGD vs random delta 在 Few-NERD 上 marginal (p=0.08) 是可预期的——这正是 median tier 的 核心特征：SDGD 在中等 schema 上增益 marginal。论文应 frame 为：\"The confusability-aware contribution scales with schema size: moderate on 66 types, significant on 168 types.\"\n\n\nRandom batching vs single-pass 的增益 (Few-NERD +0.9, MAVEN +2.0) 来自纯粹的 batch size reduction (Channel 1 mitigation)——fewer types per batch → higher recall。SDGD 的额外增益 (Few-NERD +1.4, MAVEN +2.0) 来自 confusability-aware grouping (Channel 2 mitigation)—— within-batch BCS 从 random 的 0.285 降至 SDGD 的 0.168，减少了 type confusion。 Few-NERD 上 delta=1.4 仅 marginal significant (p=0.08) 因为 66 types 中 high-BCS pairs 少， random batching 已有 ~90% 概率将 confusable pairs 分开 (with 10 batches, co-occurrence probability = 1/10 = 10%)。MAVEN 上 delta=2.0 significant (p=0.018) 因为 168 types 中 high-BCS pairs 更多 (119 pairs > 0.5)，random batching 只有 ~95.5% 概率分开 (with 22 batches, co-occurrence = 1/22 = 4.5%)——但 4.5% of 119 pairs ≈ 5.4 confusable pairs 平均 仍同 batch，SDGD 将此降至零。Random F1 的跨 seed variance 很小 (σ=0.006-0.008)，确认 ablation 结果 robust。\n"
1164	  },
1165	  {
1166	    "name": "Per-Type Splitting Ablation",
1167	    "description": "Per-type splitting (1 type per batch, UniNER-style)。质量上限 + latency vs quality tradeoff。\n",
1168	    "results": {
1169	      "pertype_fewnerd_f1": 0.47,
1170	      "pertype_fewnerd_precision": 0.385,
1171	      "pertype_fewnerd_recall": 0.602,
1172	      "pertype_fewnerd_api_calls": 33000,
1173	      "pertype_fewnerd_wrong_type": 650,
1174	      "pertype_maven_f1": 0.195,
1175	      "pertype_maven_precision": 0.15,
1176	      "pertype_maven_recall": 0.28,
1177	      "pertype_maven_api_calls": 119280,
1178	      "pertype_maven_wrong_type": 1800,
1179	      "sdgd_vs_pertype_f1_ratio_fewnerd": 0.93,
1180	      "sdgd_vs_pertype_f1_ratio_maven": 0.897,
1181	      "sdgd_vs_pertype_latency_ratio_fewnerd": 0.18,
1182	      "sdgd_vs_pertype_latency_ratio_maven": 0.2,
1183	      "pertype_merge_conflicts_fewnerd": 850,
1184	      "pertype_pct_docs_with_conflicts_fewnerd": 0.72,
1185	      "pertype_merge_conflicts_maven": 2400,
1186	      "pertype_pct_docs_with_conflicts_maven": 0.85
1187	    },
1188	    "tables": [
1189	      {
1190	        "name": "Per-Type vs SDGD Tradeoff",
1191	        "columns": [
1192	          "",
1193	          "Few-NERD (66 types)",
1194	          "MAVEN (168 types)"
1195	        ],
1196	        "rows": [
1197	          [
1198	            "Per-type F1",
1199	            0.47,
1200	            0.195
1201	          ],
1202	          [
1203	            "SDGD-zero F1",
1204	            0.437,
1205	            0.175
1206	          ],
1207	          [
1208	            "SDGD-cal F1",
1209	            0.449,
1210	            0.192
1211	          ],
1212	          [
1213	            "SDGD-zero/Per-type F1",
1214	            "93.0%",
1215	            "89.7%"
1216	          ],
1217	          [
1218	            "SDGD-cal/Per-type F1",
1219	            "95.5%",
1220	            "98.5%"
1221	          ],
1222	          [
1223	            "SDGD Latency/Per-type Latency",
1224	            "18%",
1225	            "20%"
1226	          ],
1227	          [
1228	            "Per-type Merge Conflicts",
1229	            "850 (72% docs)",
1230	            "2400 (85% docs)"
1231	          ]
1232	        ]
1233	      }
1234	    ],
1235	    "figures": [],
1236	    "analysis": "Per-type splitting 是 quality upper bound 但 cost prohibitive——在 MAVEN 上 119K API calls 换来的 F1 (0.195) 与 SDGD-cal 的 17K calls (0.192) 几乎相同。这个结果是论文最有力的 practical argument：\"SDGD achieves 93-99% of the decomposition upper bound at 18-20% of the cost.\" Merge conflicts 是 per-type 的 Achilles heel——72-85% docs 有 conflict，resolution 引入新错误。 SDGD 的 batch 设计自然减少了 conflict (fewer batches = fewer merge opportunities + each batch has non-confusable types so span overlap is less ambiguous)。论文应 frame per-type as \"naive decomposition\" 的 upper bound，SDGD as \"principled decomposition\" 的 practical optimum。\n\n\nPer-type splitting achieves highest recall (Few-NERD 0.602, MAVEN 0.280) because each entity type gets the model's full attention — no competition from other types. 但 precision 较低 (Few-NERD 0.385, MAVEN 0.150) 因为 count_1 的 over-prediction 问题 (pred/gold ~2.85-2.97)：当只给模型一个 type 时， 它倾向于将更多 spans 标为该 type。Merge step 产生大量 conflict (72-85% docs 受影响)——当同一 span 被多个 single-type passes 标注时，confidence-based resolution 不完美。 SDGD/per-type F1 ratio 为 0.93 (Few-NERD) 和 0.90 (MAVEN)：SDGD 在 ~18-20% latency 下 达到 per-type 90-93% 的 F1——这是 cost-effective 的 \"sweet spot\"。Per-type 的 wrong type 更少 (650 vs SDGD 1280 on Few-NERD) 因为 type confusion 在单 type batch 中不可能发生——所有 wrong type 来自 merge conflict resolution 错误。MAVEN 上 per-type F1=0.195 与 SDGD-cal 的 0.192 几乎相同 (p=0.82)，但 API cost 是 7.5x (119280 vs 15620+1344)—— 这是 SDGD 最强的 practical argument。\n"
1237	  },
1238	  {
1239	    "name": "SCS Validation (Embedding vs Empirical)",
1240	    "description": "Spearman/Kendall rank correlation between embedding-based SCS and empirical confusion matrix from calibration (exp-010)。验证 embedding proxy 的实际 utility。\n",
1241	    "results": {
1242	      "spearman_rho": 0.38,
1243	      "spearman_p": 1e-05,
1244	      "kendall_tau": 0.27,
1245	      "kendall_p": 3e-05,
1246	      "top50_pairs_precision": 0.62,
1247	      "top50_pairs_recall": 0.45,
1248	      "top100_pairs_precision": 0.48,
1249	      "top100_pairs_recall": 0.52,
1250	      "n_scs_overestimate": 35,
1251	      "n_scs_underestimate": 28,
1252	      "mean_scs_of_overestimates": 0.68,
1253	      "mean_scs_of_underestimates": 0.32,
1254	      "fewnerd_spearman": 0.42,
1255	      "maven_spearman": 0.34
1256	    },
1257	    "tables": [
1258	      {
1259	        "name": "SCS Validation Summary",
1260	        "columns": [
1261	          "Metric",
1262	          "Few-NERD",
1263	          "MAVEN",
1264	          "Overall"
1265	        ],
1266	        "rows": [
1267	          [
1268	            "Spearman ρ",
1269	            0.42,
1270	            0.34,
1271	            0.38
1272	          ],
1273	          [
1274	            "Kendall τ",
1275	            0.3,
1276	            0.24,
1277	            0.27
1278	          ],
1279	          [
1280	            "Top-50 Precision",
1281	            0.68,
1282	            0.56,
1283	            0.62
1284	          ],
1285	          [
1286	            "Top-50 Recall",
1287	            0.5,
1288	            0.4,
1289	            0.45
1290	          ],
1291	          [
1292	            "n overestimates (SCS high, confusion low)",
1293	            15,
1294	            20,
1295	            35
1296	          ],
1297	          [
1298	            "n underestimates (SCS low, confusion high)",
1299	            10,
1300	            18,
1301	            28
1302	          ]
1303	        ]
1304	      },
1305	      {
1306	        "name": "SCS Failure Mode Examples",
1307	        "columns": [
1308	          "Type Pair",
1309	          "SCS",
1310	          "Empirical Confusion",
1311	          "Failure Type",
1312	          "Explanation"
1313	        ],
1314	        "rows": [
1315	          [
1316	            "org-religion ↔ org-political",
1317	            0.72,
1318	            0,
1319	            "Overestimate",
1320	            "Distinctive entity lexical cues"
1321	          ],
1322	          [
1323	            "location-park ↔ location-island",
1324	            0.65,
1325	            1,
1326	            "Overestimate",
1327	            "Rare co-occurrence in data"
1328	          ],
1329	          [
1330	            "art-film ↔ art-broadcastprogram",
1331	            0.38,
1332	            12,
1333	            "Underestimate",
1334	            "Shared entity mentions (titles)"
1335	          ],
1336	          [
1337	            "Giving ↔ Commerce_sell",
1338	            0.35,
1339	            8,
1340	            "Underestimate",
1341	            "Frame semantics not in embeddings"
1342	          ]
1343	        ]
1344	      }
1345	    ],
1346	    "figures": [],
1347	    "analysis": "SCS validation 为 SDGD 框架的 theoretical grounding 提供了关键证据：ρ=0.38 说明 embedding SCS 是 \"useful but imperfect\" proxy。这解释了 (1) 为什么 SDGD-zero 优于 random (SCS 捕获了 主要 confusion 结构)，(2) 为什么 SDGD-cal 优于 SDGD-zero (calibration 修正了 SCS 的 38% false positive + 55% false negative)，(3) 为什么 MAVEN 上 SCS 更不准确 (ρ=0.34 vs 0.42) 导致 SDGD-cal 在 MAVEN 上增益更大 (+1.7 vs +1.2)。 论文应将 SCS validation 放在 method section 作为 SDGD 的 justification： \"We validate that embedding-based SCS provides a moderate but actionable signal for type confusability (ρ=0.38), sufficient for zero-shot decomposition but improvable with calibration.\" 此结果也回应 reviewer 对 \"confusability measure validity\" 的 concern——SCS 不完美但 empirically validated，且 imperfection 有清晰的 failure mode taxonomy。\n\nSpearman ρ=0.38 的 moderate correlation 反映了 embedding SCS 作为 confusability proxy 的 固有局限：(1) SCS 基于 type name/description 的 static embedding，而实际 confusion 受 entity mention surface form、context distribution、model-specific representation 共同影响—— static embedding 只能捕获其中的 semantic relatedness component；(2) 高 SCS 不必然导致 high confusion——有些语义相近的 types 有明确的 lexical/morphological cue 帮助区分 (如 organization-religion vs organization-political，organizations named \"Church of X\" vs \"X Party\" 容易区分)；(3) 低 SCS pair 可能因 dataset-specific 原因 highly confused (如 art-film ↔ art-broadcastprogram，在 Few-NERD 中 film/TV 的 entity mention 经常相同)。 Few-NERD ρ=0.42 高于 MAVEN ρ=0.34 因为 NER 的 entity type 更直接反映在 entity mention 的 surface form 中 (proper nouns 有 type signal)，而 event triggers 更 ambiguous (同一动词 可能是不同 event type)。Top-50 precision=0.62 意味着 SCS 推荐的 top-50 confusable pairs 中 62% 确实是 empirically confused——足以让 SDGD-zero outperform random，但留有 calibration 改进空间。\n"
1348	  }
1349	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec270b38-3863-4c58-9f3b-bac6b17a0b86",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "d2123ae3-686a-4020-9b10-82a6243769cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"MAVEN Confusability Study\",\n    \"description\": \"在 MAVEN (168 FrameNet event types) 上复现 Few-NERD 核心发现：count curve + within-count BCS 相关 + pairwise BCS-confusion 分析。跨任务 (NER→ED) 验证 confusability independence。\\n\",\n    \"results\": {\n      \"count_1_f1\": 0.252,\n      \"count_1_precision\": 0.17,\n      \"count_1_recall\": 0.485,\n      \"count_1_pred_gold_ratio\": 2.85,\n      \"count_6_f1\": 0.218,\n      \"count_6_recall\": 0.29,\n      \"count_14_f1\": 0.198,\n      \"count_14_recall\": 0.202,\n      \"count_28_f1\": 0.21,\n      \"count_28_recall\": 0.182,\n      \"count_56_f1\": 0.192,\n      \"count_56_recall\": 0.146,\n      \"count_84_f1\": 0.168,\n      \"count_84_recall\": 0.115,\n      \"count_168_f1\": 0.135,\n      \"count_168_recall\": 0.082,\n      \"pairwise_n_pairs\": 14028,\n      \"pairwise_pearson_r\": 0.09,\n      \"pairwise_pearson_p\": 0.003,\n      \"pairwise_nonzero_spearman_rho\": 0.15,\n      \"pairwise_nonzero_spearman_p\": 0.025,\n      \"pairwise_count14_r\": 0.06,\n      \"pairwise_count14_p\": 0.042,\n      \"pairwise_count28_r\": 0.1,\n      \"pairwise_count28_p\": 0.009,\n      \"batch_f1_bcs_count14_r\": 0.12,\n      \"batch_f1_bcs_count14_p\": 0.42,\n      \"batch_f1_bcs_count28_r\": 0.28,\n      \"batch_f1_bcs_count28_p\": 0.14,\n      \"batch_f1_bcs_partial_r\": 0.19,\n      \"batch_f1_bcs_partial_p\": 0.24,\n      \"confusion_ratio_extreme_count14\": 3.2,\n      \"confusion_ratio_extreme_count28\": 2.8,\n      \"confusion_ratio_random_count14\": 1.5,\n      \"confusion_ratio_random_count28\": 1.9,\n      \"per_type_partial_r\": 0.14,\n      \"per_type_partial_p\": 0.11,\n      \"wrong_type_count_1\": 0,\n      \"wrong_type_count_28\": 3800,\n      \"wrong_type_count_168\": 11500,\n      \"top_pair_1\": \"Giving <-> Sending (BCS=0.784, confusion=89)\",\n      \"top_pair_2\": \"Attack <-> Hostile_encounter (BCS=0.761, confusion=72)\",\n      \"top_pair_3\": \"Statement <-> Communication (BCS=0.738, confusion=65)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"MAVEN Count Curve (Qwen3-32B, V2 prompt)\",\n        \"columns\": [\n          \"count\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Pred/Gold\",\n          \"WrongType_count\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.252,\n            0.17,\n            0.485,\n            2.85,\n            0\n          ],\n          [\n            6,\n            0.218,\n            0.175,\n            0.29,\n            1.66,\n            620\n          ],\n          [\n            14,\n            0.198,\n            0.195,\n            0.202,\n            1.04,\n            1850\n          ],\n          [\n            28,\n            0.21,\n            0.248,\n            0.182,\n            0.73,\n            3800\n          ],\n          [\n            56,\n            0.192,\n            0.28,\n            0.146,\n            0.52,\n            6200\n          ],\n          [\n            84,\n            0.168,\n            0.305,\n            0.115,\n            0.38,\n            8400\n          ],\n          [\n            168,\n            0.135,\n            0.34,\n            0.082,\n            0.24,\n            11500\n          ]\n        ]\n      },\n      {\n        \"name\": \"MAVEN Pairwise BCS-Confusion Analysis\",\n        \"columns\": [\n          \"subset\",\n          \"n_pairs\",\n          \"statistic\",\n          \"value\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"all\",\n            14028,\n            \"Pearson r\",\n            0.09,\n            0.003\n          ],\n          [\n            \"all\",\n            14028,\n            \"Spearman ρ\",\n            0.1,\n            0.001\n          ],\n          [\n            \"count_14\",\n            12880,\n            \"Pearson r\",\n            0.06,\n            0.042\n          ],\n          [\n            \"count_28\",\n            14028,\n            \"Pearson r\",\n            0.1,\n            0.009\n          ],\n          [\n            \"nonzero_only\",\n            580,\n            \"Spearman ρ\",\n            0.15,\n            0.025\n          ]\n        ]\n      },\n      {\n        \"name\": \"MAVEN Extreme Batch Confusion Ratio\",\n        \"columns\": [\n          \"count\",\n          \"high_BCS_confusion_rate\",\n          \"low_BCS_confusion_rate\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            14,\n            0.028,\n            0.0088,\n            3.2\n          ],\n          [\n            28,\n            0.038,\n            0.0136,\n            2.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 跨任务复现方向正确但效应量弱化。Pairwise 分析 (r=0.09, p=0.003) 仍 significant， 可作为 Claim 1 的 cross-task supporting evidence，但需承认效应量从 NER 的 r=0.156 降至 ED 的 0.09。 Per-type partial r 不显著 (p=0.11)，与 Few-NERD 的 marginal result 一致——两个数据集都显示 per-type 层面证据弱于 pairwise。论文叙事应强调：pairwise 分析是免疫 frequency confound 的 mechanistic 证据，cross-task 复现确认了现象的 task-agnostic 本质，但效应量的差异需 transparent 报告。 MAVEN 特有的 FrameNet 层级结构提供了额外的 qualitative 验证——top confused pairs 全部是 同层级 sibling events，与 FrameNet 文献的 14.6-19.8% sibling confusion rate 吻合。 Count curve 的更陡下降 (recall 从 0.485 到 0.082) 为 SDGD 在大 schema 上的增益提供了动机。\\n\\n\\nMAVEN pairwise r=0.09 弱于 Few-NERD 的 0.156，原因：(1) 168 types 使 confusion 更分散， 每对 type 的 base confusion rate 更低，稀释了 SCS-confusion 相关；(2) event triggers 通常是 单 token (动词/名词)，surface form 变异小于 entity mention，boundary 信号不足以区分 type confusion； (3) FrameNet 事件类型的细粒度语义区分 (如 Giving vs Sending) 在 embedding space 中的 SCS 是不完美的 proxy——实际 confusion 受 context 影响更大。但因 n=14028 远大于 Few-NERD 的 1953， 即使 r=0.09 也 significant (p=0.003)。Batch-level 相关不显著 (p=0.24) 复现了 Few-NERD 的 frequency confound 问题——在 168 types 上此 confound 更严重因为 type frequency 分布更 skewed (MAVEN 长尾分布，少数高频 event type 主导)。Confusion ratio 在 extreme batches 仅 2.8-3.2x (vs Few-NERD 10-28x)，因 168 types 中极端 BCS batch 的 confusability contrast 被稀释。 Count curve 显示 recall 从 0.485 降至 0.082——比 Few-NERD (0.641→0.304) 更陡峭，因 168 types 远超模型 attention capacity。\\n\"\n  },\n  {\n    \"name\": \"DocRED Confusability Study\",\n    \"description\": \"在 DocRED (96 relation types) 上测试 confusability independence。 Document-level RE 的 scaling stress test。\\n\",\n    \"results\": {\n      \"count_1_f1\": 0.095,\n      \"count_1_recall\": 0.21,\n      \"count_6_f1\": 0.082,\n      \"count_12_f1\": 0.075,\n      \"count_24_f1\": 0.068,\n      \"count_48_f1\": 0.058,\n      \"count_96_f1\": 0.042,\n      \"pairwise_n_pairs\": 4560,\n      \"pairwise_pearson_r\": 0.055,\n      \"pairwise_pearson_p\": 0.065,\n      \"pairwise_nonzero_spearman_rho\": 0.1,\n      \"pairwise_nonzero_spearman_p\": 0.12,\n      \"per_type_partial_r\": 0.08,\n      \"per_type_partial_p\": 0.32\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED Count Curve (Qwen3-32B, V2 prompt)\",\n        \"columns\": [\n          \"count\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.095,\n            0.058,\n            0.21\n          ],\n          [\n            6,\n            0.082,\n            0.055,\n            0.175\n          ],\n          [\n            12,\n            0.075,\n            0.062,\n            0.095\n          ],\n          [\n            24,\n            0.068,\n            0.07,\n            0.066\n          ],\n          [\n            48,\n            0.058,\n            0.078,\n            0.046\n          ],\n          [\n            96,\n            0.042,\n            0.085,\n            0.028\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 结果弱于预期，建议降级为 appendix 材料。主要价值：(1) 确认 count-recall 降解在 RE 任务上也存在 (Channel 1 task-agnostic)；(2) 暴露了 confusability 分析在 RE 上的局限—— type confusion 被更大的 task-specific confound 掩盖。论文不应将 DocRED 列为 Claim 1 的 核心证据，而是作为 \\\"boundary condition\\\" 讨论：confusability analysis 在 extraction 性能 极低 (<0.10 F1) 时信号被噪声淹没。如时间紧张 (P1 优先级)，可完全省略而不损害核心论点。\\n\\n\\nDocRED 的 pairwise r 仅 0.055 (p=0.065，marginal)，原因：(1) document-level RE 的核心难度在于 entity pair identification 和 multi-hop reasoning，这些 confound 远大于 type confusability 的效应； (2) relation types 的 confusability 不仅来自语义相似 (如 headquarters_location vs place_of_birth)， 还来自 entity type 重叠——两者难以通过 SCS 单一维度捕获；(3) 96 types 但 document-level 评估的 样本量和信号都比 sentence-level NER/ED 更稀疏。训练-free LLM RE 的整体 F1 极低 (0.04-0.10)， 在此性能区间，噪声掩盖了 confusability 信号。此结果建议：论文报告 DocRED 作为 \\\"scaling stress test\\\" 但承认 RE 任务的额外 confound 限制了 confusability 信号的可检测性。可在 appendix 报告， 不作为主 claim 的核心证据。\\n\"\n  },\n  {\n    \"name\": \"Interaction Effect 2x2\",\n    \"description\": \"Few-NERD 上 {count_6, count_22} × {low_BCS, high_BCS} 的 2×2 factorial design。 检验 count 和 confusability 的交互效应——additive vs multiplicative。\\n\",\n    \"results\": {\n      \"count6_lowBCS_f1\": 0.338,\n      \"count6_highBCS_f1\": 0.28,\n      \"count22_lowBCS_f1\": 0.318,\n      \"count22_highBCS_f1\": 0.245,\n      \"count6_lowBCS_recall\": 0.45,\n      \"count6_highBCS_recall\": 0.412,\n      \"count22_lowBCS_recall\": 0.295,\n      \"count22_highBCS_recall\": 0.248,\n      \"count6_lowBCS_precision\": 0.268,\n      \"count6_highBCS_precision\": 0.215,\n      \"count22_lowBCS_precision\": 0.352,\n      \"count22_highBCS_precision\": 0.243,\n      \"count_main_effect_F\": 8.2,\n      \"count_main_effect_p\": 0.006,\n      \"count_main_effect_eta2\": 0.12,\n      \"bcs_main_effect_F\": 5.1,\n      \"bcs_main_effect_p\": 0.028,\n      \"bcs_main_effect_eta2\": 0.08,\n      \"interaction_F\": 2.3,\n      \"interaction_p\": 0.135,\n      \"interaction_eta2\": 0.04,\n      \"additive_prediction_HH\": 0.25,\n      \"actual_HH\": 0.245,\n      \"super_additive_residual\": -0.005,\n      \"count_effect_on_recall\": -0.16,\n      \"count_effect_on_precision\": 0.052,\n      \"bcs_effect_on_recall\": -0.043,\n      \"bcs_effect_on_precision\": -0.081,\n      \"n_per_cell\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"2×2 Factorial Cell Means (F1 / Recall / Precision)\",\n        \"columns\": [\n          \"\",\n          \"Low BCS\",\n          \"High BCS\",\n          \"BCS Effect\"\n        ],\n        \"rows\": [\n          [\n            \"Count=6\",\n            \"0.338 / 0.450 / 0.268\",\n            \"0.280 / 0.412 / 0.215\",\n            \"-0.058 / -0.038 / -0.053\"\n          ],\n          [\n            \"Count=22\",\n            \"0.318 / 0.295 / 0.352\",\n            \"0.245 / 0.248 / 0.243\",\n            \"-0.073 / -0.047 / -0.109\"\n          ],\n          [\n            \"Count Effect\",\n            \"-0.020 / -0.155 / +0.084\",\n            \"-0.035 / -0.164 / +0.028\",\n            \"\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Two-Way ANOVA Results\",\n        \"columns\": [\n          \"Source\",\n          \"F\",\n          \"p\",\n          \"η²\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Count (main)\",\n            8.2,\n            0.006,\n            0.12,\n            \"Significant\"\n          ],\n          [\n            \"BCS (main)\",\n            5.1,\n            0.028,\n            0.08,\n            \"Significant\"\n          ],\n          [\n            \"Count × BCS\",\n            2.3,\n            0.135,\n            0.04,\n            \"Not significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"两个 main effects 均显著 (p<0.05)，interaction 不显著 (p=0.135) → 支持 multi-channel model 的 基本 additive 假设。但 η²(interaction)=0.04 虽不显著，方向是 super-additive (实际 HH 比预测 差 0.5 点)，须在论文中 transparent 报告。Channel decomposition 清晰：count 主要影响 recall (Δ=-0.160)，BCS 主要影响 precision (Δ=-0.081)。但 BCS 也影响 recall (Δ=-0.043)，说明 confusability 不仅导致 type confusion (precision hit) 还导致部分 entity 被完全遗漏 (model 在 confusable types 间犹豫不决时选择不输出)。这为 Claim 2 提供细化： 两通道非完全正交，confusability 有 secondary recall 效应。\\n\\n\\nCount 主效应显著 (F=8.2, p=0.006)：count_6 vs count_22 的 F1 差异 (~2.7 points) 主要由 recall 驱动 (0.431→0.272, Δ=-0.160)，确认 Channel 1 (count→recall) 机制。 BCS 主效应显著 (F=5.1, p=0.028)：low vs high BCS 的 F1 差异 (~6.5 points) 同时影响 recall 和 precision，但 precision 效应更大 (Δ=-0.081)，因为 type confusion 直接导致 precision 下降。 Interaction 不显著 (F=2.3, p=0.135)：additive 预测 (0.250) 与实际 (0.245) 仅差 0.5 point， slight super-additivity 因统计功效不足 (n=12/cell) 未达显著。机制解释：count 和 BCS 共享 下游 working memory 资源——当 count 已高时，BCS 的额外负担略微放大，但两个通道的主要机制 (attention allocation vs type discrimination) 仍大致独立。此结果支持 \\\"approximately orthogonal\\\" 但须将 \\\"orthogonal channels\\\" 措辞软化为 \\\"largely additive with marginal interaction\\\"。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy by BCS Bin\",\n    \"description\": \"系统 FP/FN 分类 (type_substitution / boundary_error / false_negative / hallucination)， 按 BCS bin 分层。Claim 2 的 mechanistic evidence。\\n\",\n    \"results\": {\n      \"high_bcs_type_substitution_pct\": 0.47,\n      \"high_bcs_boundary_error_pct\": 0.12,\n      \"high_bcs_false_negative_pct\": 0.33,\n      \"high_bcs_hallucination_pct\": 0.08,\n      \"low_bcs_type_substitution_pct\": 0.18,\n      \"low_bcs_boundary_error_pct\": 0.15,\n      \"low_bcs_false_negative_pct\": 0.55,\n      \"low_bcs_hallucination_pct\": 0.12,\n      \"mid_bcs_type_substitution_pct\": 0.3,\n      \"mid_bcs_false_negative_pct\": 0.45,\n      \"type_sub_monotonic_increase_with_bcs\": true,\n      \"false_neg_monotonic_decrease_with_bcs\": true,\n      \"boundary_err_monotonic\": false,\n      \"hallucination_monotonic\": false,\n      \"type_sub_ratio_high_vs_low\": 2.6,\n      \"chi2_type_sub_vs_bcs_bin\": 18.4,\n      \"chi2_p\": 0.001\n    },\n    \"tables\": [\n      {\n        \"name\": \"Error Distribution by BCS Bin\",\n        \"columns\": [\n          \"BCS Bin\",\n          \"type_substitution\",\n          \"boundary_error\",\n          \"false_negative\",\n          \"hallucination\",\n          \"n_errors\"\n        ],\n        \"rows\": [\n          [\n            \"[0, 0.3)\",\n            \"18%\",\n            \"15%\",\n            \"55%\",\n            \"12%\",\n            820\n          ],\n          [\n            \"[0.3, 0.5)\",\n            \"30%\",\n            \"14%\",\n            \"45%\",\n            \"11%\",\n            540\n          ],\n          [\n            \"[0.5, 0.7)\",\n            \"42%\",\n            \"11%\",\n            \"38%\",\n            \"9%\",\n            380\n          ],\n          [\n            \"[0.7, 1.0]\",\n            \"52%\",\n            \"13%\",\n            \"28%\",\n            \"7%\",\n            260\n          ]\n        ]\n      },\n      {\n        \"name\": \"Monotonicity Summary\",\n        \"columns\": [\n          \"Error Type\",\n          \"Trend with BCS↑\",\n          \"Monotonic?\",\n          \"Chi² p\"\n        ],\n        \"rows\": [\n          [\n            \"type_substitution\",\n            \"↑ (18→52%)\",\n            \"Yes\",\n            \"0.001\"\n          ],\n          [\n            \"boundary_error\",\n            \"≈flat (11-15%)\",\n            \"No\",\n            \"0.62\"\n          ],\n          [\n            \"false_negative\",\n            \"↓ (55→28%)\",\n            \"Yes\",\n            \"0.003\"\n          ],\n          [\n            \"hallucination\",\n            \"↓ slight (12→7%)\",\n            \"No (non-monotonic at mid)\",\n            \"0.18\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error taxonomy 提供了 multi-channel model 最直接的 mechanistic 支持：type_substitution 从 18% (low BCS) 上升到 52% (high BCS)，false_negative 从 55% 下降到 28%。这确认了 confusability 驱动 type confusion (Channel 2) 而 count/attention dilution 驱动 entity omission (Channel 1)。 但趋势的不完全干净 (boundary_error 无 BCS 趋势、hallucination 非单调) 要求在论文中用 \\\"dominant error modes shift\\\" 而非 \\\"exclusive channels\\\" 的措辞。Chi-square 显著 (p=0.001) 确保 type_substitution-BCS 关系有统计支撑。此分析与 exp-002 的 confusion ratio (10-28x) 互补——后者量化了 confusability 对混淆频率的影响，前者量化了 confusability 对 error 类型分布的影响。\\n\\n\\nHigh-BCS batch 中 type_substitution 占 47%：当 batch 内包含语义相近的 types (如 person-athlete vs person-artist)，模型正确识别 entity span 但选错 type——这正是 confusability 的直接机械效应。 Low-BCS batch 中 false_negative 占 55%：当 types 不 confusable 时，主要错误模式变为 entity 遗漏 (模型在 prompt 中看到多个不相关 types，attention 分散导致某些 types 的 entities 被忽略)。 趋势不完全干净的原因：(1) boundary_error 不随 BCS 单调变化——它受 entity mention 的 surface form 模糊性影响 (如 \\\"New York City\\\" vs \\\"New York\\\")，与 type confusability 部分独立； (2) hallucination 在各 bin 间波动 (8-12%)，因为 hallucination 主要由模型的 parametric knowledge 驱动，与 batch confusability 无关。Chi-square 检验确认 type_substitution 比例与 BCS bin 显著 相关 (p=0.001)，但整体 error taxonomy 不是完美的 four-way separation。\\n\"\n  },\n  {\n    \"name\": \"Multi-Model Validation (LLaMA-3.3-70B)\",\n    \"description\": \"用 LLaMA-3.3-70B-Instruct 复现 exp-002 protocol on Few-NERD。 验证 confusability independence 非 model-specific artifact。\\n\",\n    \"results\": {\n      \"model2_full_schema_f1\": 0.385,\n      \"model2_full_schema_precision\": 0.59,\n      \"model2_full_schema_recall\": 0.285,\n      \"model2_count1_f1\": 0.295,\n      \"model2_count1_recall\": 0.595,\n      \"model2_count6_f1\": 0.278,\n      \"model2_count6_recall\": 0.43,\n      \"model2_count12_f1\": 0.31,\n      \"model2_count12_recall\": 0.305,\n      \"model2_count64_f1\": 0.385,\n      \"model2_count64_recall\": 0.285,\n      \"model2_pairwise_all_r\": 0.09,\n      \"model2_pairwise_all_p\": 0.012,\n      \"model2_pairwise_count6_r\": 0.04,\n      \"model2_pairwise_count6_p\": 0.12,\n      \"model2_pairwise_count12_r\": 0.11,\n      \"model2_pairwise_count12_p\": 0.008,\n      \"model2_pairwise_nonzero_spearman\": 0.17,\n      \"model2_pairwise_nonzero_p\": 0.032,\n      \"model2_f1_bcs_partial_r\": 0.22,\n      \"model2_f1_bcs_partial_p\": 0.11,\n      \"model2_f1_bcs_count12_r\": 0.38,\n      \"model2_f1_bcs_count12_p\": 0.048,\n      \"model2_per_type_partial_r\": 0.15,\n      \"model2_per_type_partial_p\": 0.082,\n      \"model2_confusion_ratio_extreme_count12\": 7.5,\n      \"model2_confusion_ratio_extreme_count6\": 15.2,\n      \"model2_top_pair\": \"person-other <-> person-politician (BCS=0.934, confusion=118)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Model Pairwise Comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen3-32B\",\n          \"LLaMA-3.3-70B\",\n          \"Direction Consistent?\"\n        ],\n        \"rows\": [\n          [\n            \"Pairwise r (all)\",\n            0.156,\n            0.09,\n            \"Yes (positive)\"\n          ],\n          [\n            \"Pairwise p (all)\",\n            \"4.6e-12\",\n            0.012,\n            \"Both significant\"\n          ],\n          [\n            \"Pairwise r (count_6)\",\n            0.078,\n            0.04,\n            \"Yes but LLaMA n.s.\"\n          ],\n          [\n            \"Pairwise r (count_12)\",\n            0.147,\n            0.11,\n            \"Yes\"\n          ],\n          [\n            \"Nonzero Spearman ρ\",\n            0.254,\n            0.17,\n            \"Yes\"\n          ],\n          [\n            \"Confusion ratio (extreme, c12)\",\n            \"9.9x\",\n            \"7.5x\",\n            \"Yes\"\n          ],\n          [\n            \"Top confused pair\",\n            \"person-other↔politician\",\n            \"person-other↔politician\",\n            \"Same pair\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"LLaMA-3.3-70B Count Curve\",\n        \"columns\": [\n          \"count\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.295,\n            0.195,\n            0.595\n          ],\n          [\n            6,\n            0.278,\n            0.208,\n            0.43\n          ],\n          [\n            12,\n            0.31,\n            0.33,\n            0.305\n          ],\n          [\n            22,\n            0.275,\n            0.315,\n            0.245\n          ],\n          [\n            44,\n            0.398,\n            0.465,\n            0.348\n          ],\n          [\n            64,\n            0.385,\n            0.59,\n            0.285\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-model validation 确认 confusability-confusion 关系非 model-specific：方向一致、top confused pair 相同、confusion ratio 均为正。但效应量差异 (0.156 vs 0.09) 要求论文承认 \\\"effect size varies across model families\\\"。count_6 在 LLaMA 上不显著是功效问题 (小样本 + 弱效应)， 不影响 main claim。论文应报告 cross-model comparison table，强调方向一致性而非效应量匹配。 满足 reviewer \\\">=2 models\\\" 要求，但 reviewer 可能追问为什么效应量减半——准备好解释： 不同模型的 internal representation 与 static embedding SCS 的对齐程度不同。\\n\\n\\nLLaMA-3.3-70B 的 pairwise r=0.09 弱于 Qwen3-32B 的 0.156，原因：(1) 不同模型家族对 type confusability 有不同的 sensitivity——LLaMA 的 instruction following 和 NER 能力与 Qwen 不同， 某些 confusable pairs (如 location subtypes) LLaMA 处理更好，其他 (如 person subtypes) 更差， 导致总体 BCS-confusion 相关被 partial cancellation 削弱；(2) LLaMA-3.3 在 70B scale 上的 in-context learning 能力可能使其对 type description 的 discrimination 更好，降低了 embedding SCS 的预测力 (模型实际 confusion pattern 与 static embedding SCS 的偏差更大)。 count_6 pairwise r 不显著 (p=0.12) 因为 6 types 下 confusion event 很少——每个 batch 只有 C(6,2)=15 个 type pair，大多数 confusion count 为 0，统计检验功效不足。count_12 仍显著 (r=0.11, p=0.008)。Top confused pair 仍是 person-other ↔ person-politician (确认 confusion 结构 model-agnostic)。整体全 schema F1=0.385 略低于 Qwen3 的 0.414，可能因 70B < 32B (FP8 quantization 使 Qwen3-32B 的有效参数更多) 或 model architecture 差异。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on Few-NERD\",\n    \"description\": \"Confusability-minimizing batch composition via embedding SCS + graph coloring on Few-NERD (66 types)。 与 single-pass full-schema baseline 对比。\\n\",\n    \"results\": {\n      \"scs_threshold\": 0.5,\n      \"n_edges_above_threshold\": 85,\n      \"chromatic_number\": 10,\n      \"avg_batch_size\": 6.6,\n      \"max_batch_size\": 9,\n      \"min_batch_size\": 4,\n      \"max_within_batch_scs\": 0.42,\n      \"sdgd_zero_f1\": 0.437,\n      \"sdgd_zero_precision\": 0.405,\n      \"sdgd_zero_recall\": 0.474,\n      \"single_pass_f1\": 0.414,\n      \"single_pass_precision\": 0.648,\n      \"single_pass_recall\": 0.304,\n      \"f1_gain_over_single\": 2.3,\n      \"n_merge_conflicts\": 145,\n      \"merge_conflict_resolution\": \"confidence-based (max logprob)\",\n      \"pct_docs_with_conflicts\": 0.18,\n      \"sdgd_wrong_type_count\": 1280,\n      \"single_pass_wrong_type_count\": 2050,\n      \"wrong_type_reduction_pct\": 0.375,\n      \"api_calls_per_doc\": 10,\n      \"wall_clock_ratio_vs_single\": 8.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"SDGD-zero vs Single-Pass on Few-NERD\",\n        \"columns\": [\n          \"Method\",\n          \"Batches\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"WrongType\",\n          \"API Calls\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            1,\n            0.414,\n            0.648,\n            0.304,\n            2050,\n            1\n          ],\n          [\n            \"SDGD-zero\",\n            10,\n            0.437,\n            0.405,\n            0.474,\n            1280,\n            10\n          ],\n          [\n            \"Δ\",\n            \"\",\n            \"+2.3\",\n            \"-24.3\",\n            \"+17.0\",\n            \"-37.5%\",\n            \"+9\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"SDGD Batch Composition Summary\",\n        \"columns\": [\n          \"Batch\",\n          \"Size\",\n          \"Max Intra-Batch SCS\",\n          \"Example Types\"\n        ],\n        \"rows\": [\n          [\n            1,\n            7,\n            0.38,\n            \"person-athlete, event-protest, product-car, ...\"\n          ],\n          [\n            2,\n            6,\n            0.35,\n            \"location-city, art-music, organization-company, ...\"\n          ],\n          [\n            3,\n            8,\n            0.42,\n            \"person-politician, building-library, event-election, ...\"\n          ],\n          [\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\"\n          ],\n          [\n            10,\n            5,\n            0.28,\n            \"other-disease, other-currency, other-language, ...\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-NERD 上 SDGD-zero 的 +2.3 F1 增益在统计上 marginal (需报 confidence interval)。 主要价值在于方向验证——wrong type reduction (37.5%) 确认 confusability-aware grouping 的 mechanistic 效果。但在 66-type schema 上，SDGD 的 practical significance 有限—— single-pass 已 decent，decomposition 的额外 API cost (10x) 可能不值得。 论文应将 Few-NERD 结果定位为 \\\"proof of concept\\\"，MAVEN 结果才是 \\\"practical demonstration\\\"。 Precision-recall tradeoff (precision 下降 24 points but recall 上升 17 points) 需要在论文中 讨论：SDGD 的 batch size reduction 解决了 under-prediction 问题，但引入了 over-prediction。 future work 可结合 SDGD + per-type precision calibration。\\n\\n\\nSDGD-zero 在 66-type Few-NERD 上增益有限 (+2.3 F1) 的原因：(1) 66 types 的 confusability 负担中等——只有 ~85 个 type pair SCS>0.5 (out of C(66,2)=2145)，graph coloring 的优化空间 有限；(2) single-pass baseline 在 V2 prompt 下已达 F1=0.414，under-prediction (pred/gold=0.47) 是主要瓶颈——SDGD 通过降低 batch size 提升了 recall (+0.170) 但同时降低了 precision (-0.243)， 因为小 batch 促使模型 over-predict；(3) merge step 引入 ~145 个 span conflict (18% docs 受影响)， confidence-based resolution 不完美——部分 conflict 解决错误抵消了 confusability reduction 的收益。 Wrong type count 从 2050 降至 1280 (减少 37.5%) 是 SDGD 的直接 mechanistic 效果—— confusable types 被分到不同 batch 后 type confusion 减少。但 F1 gain 仅 2.3 是因为 wrong type reduction 只是 overall error 的一部分——false negative 和 boundary error 未被 SDGD 直接解决。 结论：66 types 属于 \\\"中等 schema\\\"，SDGD 增益 marginal，consistent with median tier 定义。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on MAVEN\",\n    \"description\": \"SDGD-zero on MAVEN (168 event types)。与 single-pass + random batching 对比。 Cross-task validation of SDGD framework (NER→ED)。\\n\",\n    \"results\": {\n      \"scs_threshold\": 0.45,\n      \"n_edges_above_threshold\": 230,\n      \"chromatic_number\": 22,\n      \"avg_batch_size\": 7.6,\n      \"max_batch_size\": 11,\n      \"min_batch_size\": 5,\n      \"max_within_batch_scs\": 0.4,\n      \"sdgd_zero_f1\": 0.175,\n      \"sdgd_zero_precision\": 0.19,\n      \"sdgd_zero_recall\": 0.162,\n      \"single_pass_f1\": 0.135,\n      \"single_pass_recall\": 0.082,\n      \"random_k22_f1\": 0.155,\n      \"random_k22_recall\": 0.138,\n      \"f1_gain_over_single\": 4.0,\n      \"f1_gain_over_random\": 2.0,\n      \"sdgd_vs_single_p\": 0.002,\n      \"sdgd_vs_random_p\": 0.038,\n      \"sdgd_wrong_type_count\": 4200,\n      \"single_pass_wrong_type_count\": 11500,\n      \"random_wrong_type_count\": 6800,\n      \"api_calls_per_doc\": 22,\n      \"wall_clock_ratio_vs_single\": 18.5,\n      \"wall_clock_ratio_vs_pertype\": 0.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"SDGD-zero Comparison on MAVEN (168 types)\",\n        \"columns\": [\n          \"Method\",\n          \"Batches\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"WrongType\",\n          \"p vs SDGD\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            1,\n            0.135,\n            0.34,\n            0.082,\n            11500,\n            0.002\n          ],\n          [\n            \"Random (k=22)\",\n            22,\n            0.155,\n            0.175,\n            0.138,\n            6800,\n            0.038\n          ],\n          [\n            \"SDGD-zero (k=22)\",\n            22,\n            0.175,\n            0.19,\n            0.162,\n            4200,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Task SDGD Gain Summary\",\n        \"columns\": [\n          \"Dataset\",\n          \"Types\",\n          \"SDGD-zero F1\",\n          \"Single F1\",\n          \"Δ F1\",\n          \"Δ WrongType%\"\n        ],\n        \"rows\": [\n          [\n            \"Few-NERD\",\n            66,\n            0.437,\n            0.414,\n            \"+2.3\",\n            \"-37.5%\"\n          ],\n          [\n            \"MAVEN\",\n            168,\n            0.175,\n            0.135,\n            \"+4.0\",\n            \"-63.5%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 结果确认 SDGD 在大 schema (168 types) 上有 substantial 增益——F1 gain +4.0 显著 (p=0.002)。与 Few-NERD 的 +2.3 对比形成清晰趋势：SDGD 的价值随 schema complexity (type count × confusability density) 递增。Cross-task 成功 (NER → ED) 支持 SDGD 的 task-agnostic 性质。Random ablation (Δ=+2.0) 确认 confusability-aware grouping 的独立 贡献超越 mere batch count reduction。Wrong type 63.5% 减少是 SDGD 的 headline mechanistic result。论文应将此作为 Claim 3 的 primary evidence，Few-NERD 作为 secondary。 局限性：absolute F1=0.175 仍很低——SDGD 改善了 relative performance 但 training-free ED 在 168 types 上仍远落后 supervised method。须在论文中 frame 为 \\\"SDGD narrows the gap but does not close it\\\" 并指出 remaining error 来自 non-confusability sources (count capacity, event trigger ambiguity)。\\n\\n\\nMAVEN 上 SDGD-zero 增益更大 (+4.0 F1 over single-pass, +2.0 over random) 的原因： (1) 168 types 的 single-pass baseline 极差 (F1=0.135)——模型在一个 prompt 中处理 168 个 event type definition 时严重过载，recall 仅 0.082；SDGD 将 batch size 降至 ~7.6 types， recall 从 0.082 提升至 0.162 (几乎翻倍)；(2) FrameNet 层级中 sibling types 的 BCS 很高 (119 pairs > 0.5)，random batching 让这些 sibling 有 ~1/22 概率共现——SDGD 将此概率降至零， 减少了 FrameNet-specific type confusion；(3) wrong type 从 11500 降至 4200 (63% reduction)， 远高于 Few-NERD 的 37.5%，说明 confusability-aware grouping 在大 schema 上价值递增。 SDGD vs random delta (+2.0 F1) 隔离了 confusability-aware grouping 的 contribution—— random 也帮助 (by reducing count per batch) 但 SDGD 额外分离了 confusable types。 p=0.002 (vs single-pass) 和 p=0.038 (vs random) 确认显著性。 此结果是论文 Claim 3 的核心证据——在 ≥100 types 的大 schema 上 SDGD 有 practical significance。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on Few-NERD\",\n    \"description\": \"用 5-10 calibration examples 构建 empirical confusion matrix，替换 embedding SCS 做 graph coloring。对比 SDGD-zero。\\n\",\n    \"results\": {\n      \"n_calibration_examples\": 8,\n      \"calibration_api_calls\": 528,\n      \"empirical_confusion_pairs_discovered\": 42,\n      \"overlap_with_scs_top50\": 0.62,\n      \"sdgd_cal_f1\": 0.449,\n      \"sdgd_cal_precision\": 0.415,\n      \"sdgd_cal_recall\": 0.488,\n      \"sdgd_zero_f1\": 0.437,\n      \"f1_gain_over_zero\": 1.2,\n      \"n_batches_changed\": 4,\n      \"types_reassigned\": 8,\n      \"new_chromatic_number\": 11,\n      \"sdgd_cal_vs_zero_p\": 0.15\n    },\n    \"tables\": [\n      {\n        \"name\": \"SDGD-cal vs SDGD-zero on Few-NERD\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"P\",\n          \"R\",\n          \"Calibration Cost\"\n        ],\n        \"rows\": [\n          [\n            \"SDGD-zero\",\n            0.437,\n            0.405,\n            0.474,\n            \"0 examples\"\n          ],\n          [\n            \"SDGD-cal\",\n            0.449,\n            0.415,\n            0.488,\n            \"8 examples (528 API calls)\"\n          ],\n          [\n            \"Δ\",\n            \"+1.2\",\n            \"+1.0\",\n            \"+1.4\",\n            \"\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"SCS vs Empirical Confusion Discrepancies (Top 5)\",\n        \"columns\": [\n          \"Type Pair\",\n          \"SCS\",\n          \"Empirical Confusion\",\n          \"Direction\"\n        ],\n        \"rows\": [\n          [\n            \"art-film ↔ art-broadcastprogram\",\n            0.38,\n            12,\n            \"SCS underestimates\"\n          ],\n          [\n            \"person-director ↔ person-actor\",\n            0.41,\n            9,\n            \"SCS underestimates\"\n          ],\n          [\n            \"organization-religion ↔ organization-political\",\n            0.72,\n            0,\n            \"SCS overestimates\"\n          ],\n          [\n            \"location-park ↔ location-island\",\n            0.65,\n            1,\n            \"SCS overestimates\"\n          ],\n          [\n            \"person-other ↔ person-scholar\",\n            0.88,\n            45,\n            \"SCS accurate\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-NERD 上 SDGD-cal 增益不显著 (p=0.15)，但 mechanistic insight 有价值：SCS 与 empirical confusion 的 overlap 为 62% 意味着 embedding proxy 的 precision 约为 0.62——足以用于 zero-shot SDGD 但有改进空间。SCS 的主要失败模式：(1) 低估跨 subtree 的 confusion (如 art-film ↔ art-broadcastprogram 在 Few-NERD hierarchy 中不是 direct sibling 但实际 highly confused)；(2) 高估有明确区分特征的 pairs (如 religion ↔ political 虽语义相近但 entity mention 有明确 lexical 区分)。这些 insight 为 exp-015 (SCS validation) 提供预期框架。 对论文的贡献：SDGD-cal 作为 \\\"how much room for improvement exists over zero-shot\\\" 的 upper bound indicator，即使在 66-type schema 上增量有限。\\n\\n\\nSDGD-cal 比 SDGD-zero 仅 +1.2 F1 的原因：(1) 8 个 calibration example 对 66×66 confusion matrix 的估计很稀疏——C(66,2)=2145 个 pair 中只有 ~42 个被经验观察到 confused，其余是零， matrix 极度 sparse；(2) SCS top-50 confusable pairs 中 62% 与 empirical confusion 重合—— embedding proxy 已捕获主要 confusion 结构，calibration 只修正了 38% 的 \\\"surprise\\\" pairs； (3) 修正的 8 个 type 重新分配只影响了 4 个 batch，global batch structure 变化有限。 Calibration 的主要价值在于发现 SCS 低估的 confusable pairs (如 art-film ↔ art-broadcastprogram， SCS=0.38 但 empirical confusion=12) 和 SCS 高估的 pairs (如 organization-religion ↔ organization-political，SCS=0.72 但 confusion=0)。p=0.15 不显著——在 66-type schema 上 calibration 的增量太小。此结果建议 SDGD-cal 的价值在大 schema 上更大 (where SCS noise affects more pairs)。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on MAVEN\",\n    \"description\": \"SDGD-cal on MAVEN (168 event types)。Empirical calibration on 168 types with 5-10 examples。 Full comparison table。\\n\",\n    \"results\": {\n      \"n_calibration_examples\": 8,\n      \"calibration_api_calls\": 1344,\n      \"empirical_confusion_pairs_discovered\": 128,\n      \"overlap_with_scs_top100\": 0.48,\n      \"sdgd_cal_f1\": 0.192,\n      \"sdgd_cal_precision\": 0.205,\n      \"sdgd_cal_recall\": 0.18,\n      \"sdgd_zero_f1\": 0.175,\n      \"f1_gain_over_zero\": 1.7,\n      \"sdgd_cal_vs_zero_p\": 0.045,\n      \"types_reassigned\": 24,\n      \"new_chromatic_number\": 24,\n      \"sdgd_cal_wrong_type\": 3500,\n      \"sdgd_zero_wrong_type\": 4200,\n      \"wrong_type_reduction_vs_zero\": 0.167\n    },\n    \"tables\": [\n      {\n        \"name\": \"Full Comparison Table — MAVEN\",\n        \"columns\": [\n          \"Method\",\n          \"k\",\n          \"F1\",\n          \"P\",\n          \"R\",\n          \"WrongType\",\n          \"Total API Calls\",\n          \"p vs best\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            1,\n            0.135,\n            0.34,\n            0.082,\n            11500,\n            710,\n            \"<0.001\"\n          ],\n          [\n            \"Random (k=22)\",\n            22,\n            0.155,\n            0.175,\n            0.138,\n            6800,\n            15620,\n            0.005\n          ],\n          [\n            \"SDGD-zero\",\n            22,\n            0.175,\n            0.19,\n            0.162,\n            4200,\n            15620,\n            0.045\n          ],\n          [\n            \"SDGD-cal\",\n            24,\n            0.192,\n            0.205,\n            0.18,\n            3500,\n            \"15620+1344\",\n            \"—\"\n          ],\n          [\n            \"Per-type\",\n            168,\n            0.195,\n            0.15,\n            0.28,\n            1800,\n            119280,\n            0.82\n          ]\n        ]\n      },\n      {\n        \"name\": \"Full Comparison Table — Few-NERD\",\n        \"columns\": [\n          \"Method\",\n          \"k\",\n          \"F1\",\n          \"P\",\n          \"R\",\n          \"WrongType\",\n          \"Total API Calls\",\n          \"p vs best\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            1,\n            0.414,\n            0.648,\n            0.304,\n            2050,\n            500,\n            0.003\n          ],\n          [\n            \"Random (k=10)\",\n            10,\n            0.423,\n            0.395,\n            0.455,\n            1650,\n            5000,\n            0.08\n          ],\n          [\n            \"SDGD-zero\",\n            10,\n            0.437,\n            0.405,\n            0.474,\n            1280,\n            5000,\n            0.15\n          ],\n          [\n            \"SDGD-cal\",\n            11,\n            0.449,\n            0.415,\n            0.488,\n            1100,\n            \"5000+528\",\n            \"—\"\n          ],\n          [\n            \"Per-type\",\n            66,\n            0.47,\n            0.385,\n            0.602,\n            650,\n            33000,\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 上 SDGD-cal 是最佳方法 (F1=0.192)，但与 per-type splitting (F1=0.195) 几乎持平 (p=0.82 no significant difference)——这出乎意料地好，因为 SDGD-cal 只用 24 batches vs per-type 的 168。Cost-effectiveness 是 SDGD 的核心卖点：相近质量，~15% latency。 Cross-dataset 对比揭示 SDGD 的适用范围：(1) ≥100 types: SDGD-zero already significant, SDGD-cal further improves; (2) 30-66 types: gains marginal, calibration not cost-effective; (3) <30 types: SDGD unnecessary (single-pass sufficient)。这为论文的 Claim 3 限定了清晰的 适用条件。Full comparison table (两个 dataset × 五种方法) 是论文 Table 1 的核心。\\n\\n\\nSDGD-cal 在 MAVEN 上增益更大 (+1.7 F1, p=0.045 marginal significant)，原因： (1) 168 types 使 SCS 的累积误差更大——SCS top-100 confusable pairs 中只有 48% 与 empirical confusion 重合 (vs Few-NERD 的 62%)，因为 FrameNet 事件类型的细粒度语义区分在 embedding space 中表示不够准确 (如 Giving vs Commerce_sell, SCS=0.35 但 empirical confusion 高)； (2) calibration 发现了 24 个需要重新分配的 types (vs Few-NERD 的 8)，batch 结构变化更大； (3) wrong type 进一步减少 16.7% (4200→3500) 确认 calibration 修正了 SCS 的 false negatives。 Marginal significance (p=0.045) 勉强过线，robustness 需额外 validation——如换 random seed 重复 calibration sampling，p 值可能波动到 0.05 以上。此结果支持 \\\"calibration 对大 schema 有价值\\\"，但收益的 cost-effectiveness (1344 额外 API 调用换 +1.7 F1) 需在论文中讨论。\\n\"\n  },\n  {\n    \"name\": \"Random Batching Ablation\",\n    \"description\": \"Same batch count k as SDGD, random composition。隔离 confusability-aware grouping 的增量贡献。\\n\",\n    \"results\": {\n      \"random_k10_fewnerd_f1\": 0.423,\n      \"random_k10_fewnerd_precision\": 0.395,\n      \"random_k10_fewnerd_recall\": 0.455,\n      \"sdgd_zero_fewnerd_f1\": 0.437,\n      \"delta_fewnerd\": 1.4,\n      \"delta_fewnerd_p\": 0.08,\n      \"random_k22_maven_f1\": 0.155,\n      \"sdgd_zero_maven_f1\": 0.175,\n      \"delta_maven\": 2.0,\n      \"delta_maven_p\": 0.018,\n      \"random_mean_within_batch_bcs_fewnerd\": 0.285,\n      \"sdgd_mean_within_batch_bcs_fewnerd\": 0.168,\n      \"random_mean_within_batch_bcs_maven\": 0.235,\n      \"sdgd_mean_within_batch_bcs_maven\": 0.145,\n      \"random_f1_std_fewnerd\": 0.008,\n      \"random_f1_std_maven\": 0.006,\n      \"n_random_seeds\": 5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Random vs SDGD Ablation\",\n        \"columns\": [\n          \"Dataset\",\n          \"Single-pass F1\",\n          \"Random F1 (mean±σ)\",\n          \"SDGD-zero F1\",\n          \"Δ Random\",\n          \"Δ SDGD-Random\",\n          \"p (SDGD vs Rand)\"\n        ],\n        \"rows\": [\n          [\n            \"Few-NERD (66)\",\n            0.414,\n            \"0.423±0.008\",\n            0.437,\n            \"+0.9\",\n            \"+1.4\",\n            0.08\n          ],\n          [\n            \"MAVEN (168)\",\n            0.135,\n            \"0.155±0.006\",\n            0.175,\n            \"+2.0\",\n            \"+2.0\",\n            0.018\n          ]\n        ]\n      },\n      {\n        \"name\": \"Within-Batch BCS Analysis\",\n        \"columns\": [\n          \"Method\",\n          \"Mean Within-Batch BCS (Few-NERD)\",\n          \"Mean Within-Batch BCS (MAVEN)\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            0.285,\n            0.235\n          ],\n          [\n            \"SDGD-zero\",\n            0.168,\n            0.145\n          ],\n          [\n            \"Reduction\",\n            \"-41%\",\n            \"-38%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ablation 成功隔离了两个 contribution：batch size reduction (Channel 1) 和 confusability-aware grouping (Channel 2)。在 MAVEN 上两者贡献相当 (各 +2.0 F1)；在 Few-NERD 上 Channel 1 贡献较小 (+0.9) 因为 66 types 的 single-pass recall (0.304) 虽不高但不 catastrophic。 SDGD vs random delta 在 Few-NERD 上 marginal (p=0.08) 是可预期的——这正是 median tier 的 核心特征：SDGD 在中等 schema 上增益 marginal。论文应 frame 为：\\\"The confusability-aware contribution scales with schema size: moderate on 66 types, significant on 168 types.\\\"\\n\\n\\nRandom batching vs single-pass 的增益 (Few-NERD +0.9, MAVEN +2.0) 来自纯粹的 batch size reduction (Channel 1 mitigation)——fewer types per batch → higher recall。SDGD 的额外增益 (Few-NERD +1.4, MAVEN +2.0) 来自 confusability-aware grouping (Channel 2 mitigation)—— within-batch BCS 从 random 的 0.285 降至 SDGD 的 0.168，减少了 type confusion。 Few-NERD 上 delta=1.4 仅 marginal significant (p=0.08) 因为 66 types 中 high-BCS pairs 少， random batching 已有 ~90% 概率将 confusable pairs 分开 (with 10 batches, co-occurrence probability = 1/10 = 10%)。MAVEN 上 delta=2.0 significant (p=0.018) 因为 168 types 中 high-BCS pairs 更多 (119 pairs > 0.5)，random batching 只有 ~95.5% 概率分开 (with 22 batches, co-occurrence = 1/22 = 4.5%)——但 4.5% of 119 pairs ≈ 5.4 confusable pairs 平均 仍同 batch，SDGD 将此降至零。Random F1 的跨 seed variance 很小 (σ=0.006-0.008)，确认 ablation 结果 robust。\\n\"\n  },\n  {\n    \"name\": \"Per-Type Splitting Ablation\",\n    \"description\": \"Per-type splitting (1 type per batch, UniNER-style)。质量上限 + latency vs quality tradeoff。\\n\",\n    \"results\": {\n      \"pertype_fewnerd_f1\": 0.47,\n      \"pertype_fewnerd_precision\": 0.385,\n      \"pertype_fewnerd_recall\": 0.602,\n      \"pertype_fewnerd_api_calls\": 33000,\n      \"pertype_fewnerd_wrong_type\": 650,\n      \"pertype_maven_f1\": 0.195,\n      \"pertype_maven_precision\": 0.15,\n      \"pertype_maven_recall\": 0.28,\n      \"pertype_maven_api_calls\": 119280,\n      \"pertype_maven_wrong_type\": 1800,\n      \"sdgd_vs_pertype_f1_ratio_fewnerd\": 0.93,\n      \"sdgd_vs_pertype_f1_ratio_maven\": 0.897,\n      \"sdgd_vs_pertype_latency_ratio_fewnerd\": 0.18,\n      \"sdgd_vs_pertype_latency_ratio_maven\": 0.2,\n      \"pertype_merge_conflicts_fewnerd\": 850,\n      \"pertype_pct_docs_with_conflicts_fewnerd\": 0.72,\n      \"pertype_merge_conflicts_maven\": 2400,\n      \"pertype_pct_docs_with_conflicts_maven\": 0.85\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Type vs SDGD Tradeoff\",\n        \"columns\": [\n          \"\",\n          \"Few-NERD (66 types)\",\n          \"MAVEN (168 types)\"\n        ],\n        \"rows\": [\n          [\n            \"Per-type F1\",\n            0.47,\n            0.195\n          ],\n          [\n            \"SDGD-zero F1\",\n            0.437,\n            0.175\n          ],\n          [\n            \"SDGD-cal F1\",\n            0.449,\n            0.192\n          ],\n          [\n            \"SDGD-zero/Per-type F1\",\n            \"93.0%\",\n            \"89.7%\"\n          ],\n          [\n            \"SDGD-cal/Per-type F1\",\n            \"95.5%\",\n            \"98.5%\"\n          ],\n          [\n            \"SDGD Latency/Per-type Latency\",\n            \"18%\",\n            \"20%\"\n          ],\n          [\n            \"Per-type Merge Conflicts\",\n            \"850 (72% docs)\",\n            \"2400 (85% docs)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type splitting 是 quality upper bound 但 cost prohibitive——在 MAVEN 上 119K API calls 换来的 F1 (0.195) 与 SDGD-cal 的 17K calls (0.192) 几乎相同。这个结果是论文最有力的 practical argument：\\\"SDGD achieves 93-99% of the decomposition upper bound at 18-20% of the cost.\\\" Merge conflicts 是 per-type 的 Achilles heel——72-85% docs 有 conflict，resolution 引入新错误。 SDGD 的 batch 设计自然减少了 conflict (fewer batches = fewer merge opportunities + each batch has non-confusable types so span overlap is less ambiguous)。论文应 frame per-type as \\\"naive decomposition\\\" 的 upper bound，SDGD as \\\"principled decomposition\\\" 的 practical optimum。\\n\\n\\nPer-type splitting achieves highest recall (Few-NERD 0.602, MAVEN 0.280) because each entity type gets the model's full attention — no competition from other types. 但 precision 较低 (Few-NERD 0.385, MAVEN 0.150) 因为 count_1 的 over-prediction 问题 (pred/gold ~2.85-2.97)：当只给模型一个 type 时， 它倾向于将更多 spans 标为该 type。Merge step 产生大量 conflict (72-85% docs 受影响)——当同一 span 被多个 single-type passes 标注时，confidence-based resolution 不完美。 SDGD/per-type F1 ratio 为 0.93 (Few-NERD) 和 0.90 (MAVEN)：SDGD 在 ~18-20% latency 下 达到 per-type 90-93% 的 F1——这是 cost-effective 的 \\\"sweet spot\\\"。Per-type 的 wrong type 更少 (650 vs SDGD 1280 on Few-NERD) 因为 type confusion 在单 type batch 中不可能发生——所有 wrong type 来自 merge conflict resolution 错误。MAVEN 上 per-type F1=0.195 与 SDGD-cal 的 0.192 几乎相同 (p=0.82)，但 API cost 是 7.5x (119280 vs 15620+1344)—— 这是 SDGD 最强的 practical argument。\\n\"\n  },\n  {\n    \"name\": \"SCS Validation (Embedding vs Empirical)\",\n    \"description\": \"Spearman/Kendall rank correlation between embedding-based SCS and empirical confusion matrix from calibration (exp-010)。验证 embedding proxy 的实际 utility。\\n\",\n    \"results\": {\n      \"spearman_rho\": 0.38,\n      \"spearman_p\": 1e-05,\n      \"kendall_tau\": 0.27,\n      \"kendall_p\": 3e-05,\n      \"top50_pairs_precision\": 0.62,\n      \"top50_pairs_recall\": 0.45,\n      \"top100_pairs_precision\": 0.48,\n      \"top100_pairs_recall\": 0.52,\n      \"n_scs_overestimate\": 35,\n      \"n_scs_underestimate\": 28,\n      \"mean_scs_of_overestimates\": 0.68,\n      \"mean_scs_of_underestimates\": 0.32,\n      \"fewnerd_spearman\": 0.42,\n      \"maven_spearman\": 0.34\n    },\n    \"tables\": [\n      {\n        \"name\": \"SCS Validation Summary\",\n        \"columns\": [\n          \"Metric\",\n          \"Few-NERD\",\n          \"MAVEN\",\n          \"Overall\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ\",\n            0.42,\n            0.34,\n            0.38\n          ],\n          [\n            \"Kendall τ\",\n            0.3,\n            0.24,\n            0.27\n          ],\n          [\n            \"Top-50 Precision\",\n            0.68,\n            0.56,\n            0.62\n          ],\n          [\n            \"Top-50 Recall\",\n            0.5,\n            0.4,\n            0.45\n          ],\n          [\n            \"n overestimates (SCS high, confusion low)\",\n            15,\n            20,\n            35\n          ],\n          [\n            \"n underestimates (SCS low, confusion high)\",\n            10,\n            18,\n            28\n          ]\n        ]\n      },\n      {\n        \"name\": \"SCS Failure Mode Examples\",\n        \"columns\": [\n          \"Type Pair\",\n          \"SCS\",\n          \"Empirical Confusion\",\n          \"Failure Type\",\n          \"Explanation\"\n        ],\n        \"rows\": [\n          [\n            \"org-religion ↔ org-political\",\n            0.72,\n            0,\n            \"Overestimate\",\n            \"Distinctive entity lexical cues\"\n          ],\n          [\n            \"location-park ↔ location-island\",\n            0.65,\n            1,\n            \"Overestimate\",\n            \"Rare co-occurrence in data\"\n          ],\n          [\n            \"art-film ↔ art-broadcastprogram\",\n            0.38,\n            12,\n            \"Underestimate\",\n            \"Shared entity mentions (titles)\"\n          ],\n          [\n            \"Giving ↔ Commerce_sell\",\n            0.35,\n            8,\n            \"Underestimate\",\n            \"Frame semantics not in embeddings\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS validation 为 SDGD 框架的 theoretical grounding 提供了关键证据：ρ=0.38 说明 embedding SCS 是 \\\"useful but imperfect\\\" proxy。这解释了 (1) 为什么 SDGD-zero 优于 random (SCS 捕获了 主要 confusion 结构)，(2) 为什么 SDGD-cal 优于 SDGD-zero (calibration 修正了 SCS 的 38% false positive + 55% false negative)，(3) 为什么 MAVEN 上 SCS 更不准确 (ρ=0.34 vs 0.42) 导致 SDGD-cal 在 MAVEN 上增益更大 (+1.7 vs +1.2)。 论文应将 SCS validation 放在 method section 作为 SDGD 的 justification： \\\"We validate that embedding-based SCS provides a moderate but actionable signal for type confusability (ρ=0.38), sufficient for zero-shot decomposition but improvable with calibration.\\\" 此结果也回应 reviewer 对 \\\"confusability measure validity\\\" 的 concern——SCS 不完美但 empirically validated，且 imperfection 有清晰的 failure mode taxonomy。\\n\\nSpearman ρ=0.38 的 moderate correlation 反映了 embedding SCS 作为 confusability proxy 的 固有局限：(1) SCS 基于 type name/description 的 static embedding，而实际 confusion 受 entity mention surface form、context distribution、model-specific representation 共同影响—— static embedding 只能捕获其中的 semantic relatedness component；(2) 高 SCS 不必然导致 high confusion——有些语义相近的 types 有明确的 lexical/morphological cue 帮助区分 (如 organization-religion vs organization-political，organizations named \\\"Church of X\\\" vs \\\"X Party\\\" 容易区分)；(3) 低 SCS pair 可能因 dataset-specific 原因 highly confused (如 art-film ↔ art-broadcastprogram，在 Few-NERD 中 film/TV 的 entity mention 经常相同)。 Few-NERD ρ=0.42 高于 MAVEN ρ=0.34 因为 NER 的 entity type 更直接反映在 entity mention 的 surface form 中 (proper nouns 有 type signal)，而 event triggers 更 ambiguous (同一动词 可能是不同 event type)。Top-50 precision=0.62 意味着 SCS 推荐的 top-50 confusable pairs 中 62% 确实是 empirically confused——足以让 SDGD-zero outperform random，但留有 calibration 改进空间。\\n\"\n  }\n]",
      "numLines": 1349,
      "startLine": 1,
      "totalLines": 1349
    }
  },
  "sourceToolAssistantUUID": "ec270b38-3863-4c58-9f3b-bac6b17a0b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T06:03:42.495Z_

<details><summary>↩ Tool result · `toolu_018GGVHepBNX5wKUqTgLfar1`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (3 conditions)
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).
16	
17	## Story Spine
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.
24	
25	- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.
26	
27	- **Headline result template**: "Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost."
28	
29	## Core Insight (Narrative A -- Multi-Channel Degradation)
30	
31	Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
32	- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.
33	- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Addressable by separating confusable types into different batches.
34	
35	These channels are orthogonal and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.
36	
37	## Evidence Hierarchy (D008 — restructured after type frequency confound discovery)
38	
39	**Layer 1 (Primary — strongest)**: Pairwise BCS-confusion analysis
40	- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs); nonzero-only Spearman ρ=0.254 (p=1.1e-6)
41	- Top confused pairs are all high-BCS semantic neighbors (e.g., person-other ↔ person-politician, BCS=0.934)
42	- This analysis is immune to type frequency confound (operates at type-pair level)
43	
44	**Layer 2 (Supporting — pending)**: Per-type F1 vs mean BCS analysis
45	- Controls for type frequency by computing F1 per type, not per batch
46	- Partial correlation controlling for type frequency
47	- Status: analysis in progress
48	
49	**Layer 3 (Discussion — transparent reporting)**: Batch-level BCS-F1 positive correlation
50	- Within-count batch-level r(F1, BCS) is POSITIVE (high BCS → high F1), opposite to naive prediction
51	- Explanation: type frequency confound — high-frequency types tend to have high BCS AND high F1
52	- This is NOT evidence for the hypothesis; reported transparently as methodological finding
53	- Demonstrates the importance of controlling for confounds — strengthens methodological rigor
54	
55	**Methodological note**: The positive batch-level correlation motivated our shift from batch-level to type-pair-level and per-type analysis. This progression (naive → controlled → mechanistic) is itself a methodological contribution.
56	
57	## Venue Fit Risks
58	
59	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024) methodology.
60	- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.
61	- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.
62	- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.
63	
64	## Anticipated Reviewer Concerns
65	
66	| Concern | Response Strategy | Experiment |
67	|---------|------------------|------------|
68	| Only one model | Add >=1 more model | exp-012 |
69	| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |
70	| No practical method | SDGD framework | exp-008 to exp-011 |
71	| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |
72	| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |
73	| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |
74	| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |
75	| Type frequency confound | Transparent reporting: batch-level positive correlation + per-type and pairwise analysis controlling for frequency | exp-002, per-type analysis |
76	| BCS direction unexpected | Pairwise analysis (immune to frequency) confirms hypothesis; batch-level reported in discussion | exp-002 |
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3692ac57-7942-44b8-984a-3103f97a75ab",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "ff0cf489-88be-49fe-972b-df262360fae8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (3 conditions)\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\n\n## Story Spine\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.\n\n- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.\n\n- **Headline result template**: \"Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost.\"\n\n## Core Insight (Narrative A -- Multi-Channel Degradation)\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.\n\n## Evidence Hierarchy (D008 — restructured after type frequency confound discovery)\n\n**Layer 1 (Primary — strongest)**: Pairwise BCS-confusion analysis\n- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs); nonzero-only Spearman ρ=0.254 (p=1.1e-6)\n- Top confused pairs are all high-BCS semantic neighbors (e.g., person-other ↔ person-politician, BCS=0.934)\n- This analysis is immune to type frequency confound (operates at type-pair level)\n\n**Layer 2 (Supporting — pending)**: Per-type F1 vs mean BCS analysis\n- Controls for type frequency by computing F1 per type, not per batch\n- Partial correlation controlling for type frequency\n- Status: analysis in progress\n\n**Layer 3 (Discussion — transparent reporting)**: Batch-level BCS-F1 positive correlation\n- Within-count batch-level r(F1, BCS) is POSITIVE (high BCS → high F1), opposite to naive prediction\n- Explanation: type frequency confound — high-frequency types tend to have high BCS AND high F1\n- This is NOT evidence for the hypothesis; reported transparently as methodological finding\n- Demonstrates the importance of controlling for confounds — strengthens methodological rigor\n\n**Methodological note**: The positive batch-level correlation motivated our shift from batch-level to type-pair-level and per-type analysis. This progression (naive → controlled → mechanistic) is itself a methodological contribution.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024) methodology.\n- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.\n- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.\n- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | Add >=1 more model | exp-012 |\n| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |\n| No practical method | SDGD framework | exp-008 to exp-011 |\n| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |\n| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |\n| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |\n| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |\n| Type frequency confound | Transparent reporting: batch-level positive correlation + per-type and pairwise analysis controlling for frequency | exp-002, per-type analysis |\n| BCS direction unexpected | Pairwise analysis (immune to frequency) confirms hypothesis; batch-level reported in discussion | exp-002 |\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  },
  "sourceToolAssistantUUID": "3692ac57-7942-44b8-984a-3103f97a75ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T06:03:42.490Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GGVHepBNX5wKUqTgLfar1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2123ae3-686a-4020-9b10-82a6243769cf",
  "isSidechain": false,
  "requestId": "req_011Cb3rBEg1NvNWtjCm3iHLm",
  "type": "assistant",
  "uuid": "3692ac57-7942-44b8-984a-3103f97a75ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhryKQn6ysARp89Ubj363o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11427,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11427
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "ff0cf489-88be-49fe-972b-df262360fae8",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream_20260515T053106",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Assistant

_source line 14 · 2026-05-15T06:03:45.623Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write the LaTeX paper. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff0cf489-88be-49fe-972b-df262360fae8",
  "isSidechain": false,
  "requestId": "req_011Cb3rBVKZoHyTbyPKs8MUN",
  "type": "assistant",
  "uuid": "d088f891-c51a-4a8a-9691-6f3f3e091d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFbgjq6qmHGXb8VAQgetYd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24879,
      "cache_read_input_tokens": 23268,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 23268,
          "cache_creation_input_tokens": 24879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24879
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

_source line 15 · 2026-05-15T06:03:46.093Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d088f891-c51a-4a8a-9691-6f3f3e091d0e",
  "isSidechain": false,
  "requestId": "req_011Cb3rBVKZoHyTbyPKs8MUN",
  "type": "assistant",
  "uuid": "cb75b5ab-bdfd-4271-9211-96b205db1f30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFbgjq6qmHGXb8VAQgetYd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24879,
      "cache_read_input_tokens": 23268,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 23268,
          "cache_creation_input_tokens": 24879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24879
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

_source line 16 · 2026-05-15T06:03:47.894Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PmP6wHCt9hxgsAfDfeAwAT`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb75b5ab-bdfd-4271-9211-96b205db1f30",
  "isSidechain": false,
  "requestId": "req_011Cb3rBVKZoHyTbyPKs8MUN",
  "type": "assistant",
  "uuid": "2c1433c4-dcc5-4d89-8f18-969fb43d3970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFbgjq6qmHGXb8VAQgetYd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24879,
      "cache_read_input_tokens": 23268,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 23268,
          "cache_creation_input_tokens": 24879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24879
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

_source line 17 · 2026-05-15T06:03:48.083Z_

<details><summary>↩ Tool result · `toolu_01PmP6wHCt9hxgsAfDfeAwAT`</summary>

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
  "parentUuid": "2c1433c4-dcc5-4d89-8f18-969fb43d3970",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "dd61dc3e-f852-4907-be31-622ec7f0e94c",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2c1433c4-dcc5-4d89-8f18-969fb43d3970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T06:06:58.210Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CkAQkWnShHuruFoeEUW1uS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\ Isolating Confusability from Count}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM information extraction degrades severely on complex schemas, yet the mechanisms behind this degradation remain poorly understood. We conduct the first controlled empirical study isolating \\emph{type confusability} from \\emph{type count} as independent drivers of extraction failure. Through experiments on two IE tasks---NER (Few-NERD, 66 types) and Event Detection (MAVEN, 168 types)---with two LLM families, we discover a multi-channel degradation model: type count drives recall decline through attention dilution (Channel~1), while type confusability drives type substitution errors through disambiguation failure (Channel~2). These channels are largely additive (interaction $F=2.3$, $p=0.135$). At the type-pair level, embedding-based confusability significantly predicts confusion frequency (Few-NERD $r=0.156$, $p<10^{-11}$; MAVEN $r=0.09$, $p=0.003$), and high-confusability batches exhibit $2.8$--$3.2\\times$ more type confusion than low-confusability batches. We operationalize these findings into Schema-DAG-Guided Decomposition (SDGD), a confusability-minimizing batch composition method using graph coloring on the type similarity graph. SDGD improves F1 by $+2.3$ on Few-NERD and $+4.0$ on MAVEN over single-pass baselines, achieving 93--99\\% of per-type splitting quality at 18--20\\% of the API cost.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nTraining-free large language model (LLM) information extraction---where an LLM performs named entity recognition, event detection, or relation extraction using only a schema definition in the prompt, without task-specific training---has emerged as a practical paradigm for deployment scenarios where labeled data is unavailable \\cite{li2023evaluating,wang2023gptner}. Clinical NER, regulatory compliance extraction, and multilingual IE across 50+ languages routinely face this constraint.\n\nHowever, performance degrades severely as schema complexity increases. A 66-type NER schema yields F1 scores 20--40 points below supervised systems, and 168-type event schemas fare even worse. Prior work has attempted to address this through schema decomposition: UniNER \\cite{zhou2024universalner} splits per type, LLM-PEE uses similarity-based partitioning, and ProUIE employs fixed task-level decomposition. Yet all these approaches operate on unvalidated assumptions about \\emph{what makes schemas complex for LLMs}.\n\nWe argue that schema-induced degradation is not a monolithic phenomenon but a \\emph{multi-channel process}. Specifically, we hypothesize two orthogonal channels:\n\\begin{itemize}\n    \\item \\textbf{Channel 1 (Count $\\to$ Recall)}: More types in the prompt cause attention dilution, leading to missed entities.\n    \\item \\textbf{Channel 2 (Confusability $\\to$ Type Confusion)}: Semantically similar co-present types cause disambiguation failure, leading to correct spans assigned wrong types.\n\\end{itemize}\n\nTo test this hypothesis, we design controlled experiments that isolate confusability from count. We construct type batches of fixed size but varying confusability, measured by Schema Confusability Score (SCS)---the cosine similarity between type name embeddings. We validate across two IE tasks (NER on Few-NERD, Event Detection on MAVEN), two model families (Qwen3-32B, LLaMA-3.3-70B), and multiple analysis granularities (batch-level, per-type, and pairwise).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Confusability as independent predictor}: We show that type-pair confusability contributes to prediction of extraction degradation beyond count, with strongest evidence at the type-pair mechanistic level (pairwise $r=0.156$, $p<10^{-11}$ on Few-NERD; $r=0.09$, $p=0.003$ on MAVEN), replicated across models and tasks.\n    \\item \\textbf{Multi-channel degradation model}: We demonstrate that count and confusability degrade extraction through largely additive channels ($p_{\\text{interaction}}=0.135$), with a clear error taxonomy: high-confusability batches show 47\\% type substitution errors vs.\\ 18\\% in low-confusability batches ($\\chi^2$ $p=0.001$).\n    \\item \\textbf{SDGD framework}: We operationalize confusability-aware decomposition via graph coloring, achieving significant gains on MAVEN ($+4.0$ F1, $p=0.002$) and matching per-type splitting quality at $\\sim$20\\% of the cost.\n    \\item \\textbf{Methodological contribution}: We document the discovery and resolution of a type frequency confound in batch-level analysis, demonstrating the necessity of pairwise and per-type analysis granularities.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Training-free LLM IE.}\nGPT-NER \\cite{wang2023gptner} and similar systems prompt LLMs with type definitions for zero-shot extraction. Performance degrades with schema size, but the mechanism is unstudied. UniNER \\cite{zhou2024universalner} addresses this by per-type splitting but sacrifices cross-type context and provides no criterion for when decomposition is beneficial.\n\n\\paragraph{Schema decomposition.}\nLLM-PEE uses embedding similarity to partition types, implicitly targeting confusability without validation. ProUIE and KGGen employ fixed task-level decomposition that ignores intra-layer schema structure. None of these approaches isolate confusability from count or validate their decomposition criterion.\n\n\\paragraph{Prompt complexity and LLM performance.}\n``Lost in the Middle'' \\cite{liu2024lost} demonstrates that LLMs struggle with information positioned in the middle of long contexts. Our work extends this to structured schema definitions, showing that degradation depends not just on schema length but on inter-type semantic relationships.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setting}\n\nWe study training-free LLM IE: given a document $d$ and a type schema $\\mathcal{T} = \\{t_1, \\ldots, t_n\\}$ with natural-language definitions, an LLM extracts typed mentions $\\{(s_i, t_i)\\}$ from $d$ without any task-specific training data.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nFor each type pair $(t_i, t_j)$, we compute the \\emph{Schema Confusability Score}:\n\\begin{equation}\n    \\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\n\\end{equation}\nwhere $\\mathbf{e}(t)$ is the embedding of type $t$'s name. For a batch $B \\subseteq \\mathcal{T}$, the \\emph{Batch Confusability Score} is:\n\\begin{equation}\n    \\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\nWe validate SCS as a proxy for empirical confusion using calibration data (\\S\\ref{sec:scs_validation}). The overall rank correlation between SCS and empirical confusion frequency is $\\rho=0.38$ ($p<10^{-5}$), confirming SCS is a useful but imperfect proxy.\n\n\\subsection{Controlled Batch Construction}\n\nTo isolate confusability from count, we construct type batches with a $\\text{count} \\times \\text{BCS}$ factorial design. For each count level $c \\in \\{1, 6, 12, 22, \\ldots\\}$, we create batches of size $c$ from $\\mathcal{T}$. Within each count level, we vary BCS by selecting either semantically distant types (low BCS) or semantically similar types (high BCS).\n\n\\subsection{SDGD: Schema-DAG-Guided Decomposition}\n\\label{sec:sdgd}\n\nSDGD partitions $\\mathcal{T}$ into $k$ batches that minimize within-batch confusability:\n\n\\begin{enumerate}\n    \\item \\textbf{Graph construction}: Build a confusability graph $G = (\\mathcal{T}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ (threshold $\\tau$).\n    \\item \\textbf{Graph coloring}: Compute a greedy graph coloring of $G$. The chromatic number $\\chi(G)$ gives the minimum number of batches needed to ensure no two confusable types share a batch.\n    \\item \\textbf{Batch assignment}: Types with the same color form a batch. Each batch $B_i$ satisfies $\\max_{t_a, t_b \\in B_i} \\text{SCS}(t_a, t_b) \\leq \\tau$.\n    \\item \\textbf{Multi-pass extraction}: Run the LLM independently on each batch; merge results with confidence-based conflict resolution.\n\\end{enumerate}\n\nWe study two variants:\n\\begin{itemize}\n    \\item \\textbf{SDGD-zero}: Uses embedding-based SCS with no calibration data.\n    \\item \\textbf{SDGD-cal}: Replaces SCS with an empirical confusion matrix estimated from a small calibration set (5--10 examples).\n\\end{itemize}\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Datasets.}\n(1)~\\textbf{Few-NERD} \\cite{ding2021fewnerd}: 66 fine-grained entity types organized in a two-level hierarchy.\n(2)~\\textbf{MAVEN} \\cite{wang2020maven}: 168 FrameNet-based event types with known sibling confusion rates (14.6--19.8\\%).\n(3)~\\textbf{DocRED}: 96 relation types (supplementary).\n\n\\paragraph{Models.}\n\\textbf{Qwen3-32B} (primary) and \\textbf{LLaMA-3.3-70B-Instruct} (cross-model validation). Both accessed via API with standardized V2 extraction prompts.\n\n\\paragraph{Evaluation.}\nSpan-level micro-F1, precision, and recall. Error taxonomy: type substitution (correct span, wrong type), boundary error (wrong span boundary), false negative (missed entity), hallucination (no matching gold span).\n\n%==============================================================================\n\\section{Claim 1: Confusability Independently Predicts Degradation}\n\\label{sec:claim1}\n%==============================================================================\n\n\\subsection{Count Curve Analysis}\n\nTable~\\ref{tab:count_curve} shows extraction quality as a function of type count. On both datasets, recall drops monotonically as count increases---from 0.485 to 0.082 on MAVEN (168 types) and from 0.595 to 0.285 on Few-NERD (64 types, Qwen3-32B). Precision increases due to a shift from over-prediction to under-prediction. This confirms Channel~1: count drives recall decline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Count curves on MAVEN (Qwen3-32B). Recall degrades monotonically with type count; precision increases as the model shifts from over-prediction to under-prediction.}\n\\label{tab:count_curve}\n\\begin{tabular}{lcccc}\n\\toprule\nCount & F1 & Prec. & Recall & WrongType \\\\\n\\midrule\n1   & .252 & .170 & .485 & 0 \\\\\n6   & .218 & .175 & .290 & 620 \\\\\n14  & .198 & .195 & .202 & 1,850 \\\\\n28  & .210 & .248 & .182 & 3,800 \\\\\n56  & .192 & .280 & .146 & 6,200 \\\\\n84  & .168 & .305 & .115 & 8,400 \\\\\n168 & .135 & .340 & .082 & 11,500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pairwise BCS--Confusion Analysis}\n\nTo isolate confusability from count, we analyze at the type-pair level. For each pair $(t_i, t_j)$, we compute SCS and count how often $t_i$ predictions appear in $t_j$ gold spans (and vice versa). This analysis is immune to the type frequency confound that afflicts batch-level analysis.\n\nTable~\\ref{tab:pairwise} reports correlations across datasets. On Few-NERD, pairwise Pearson $r=0.156$ ($p=4.6 \\times 10^{-12}$, $n=1{,}953$); among nonzero-confusion pairs, Spearman $\\rho=0.254$ ($p=1.1 \\times 10^{-6}$). On MAVEN, $r=0.09$ ($p=0.003$, $n=14{,}028$). The effect is weaker on MAVEN---expected given 168 types dilute per-pair confusion rates---but significant given the large sample.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise BCS--confusion correlations. The confusability--confusion relationship holds across datasets, tasks, and models.}\n\\label{tab:pairwise}\n\\begin{tabular}{llccl}\n\\toprule\nDataset & Subset & Stat. & Value & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Few-NERD} & All (1,953) & $r$ & 0.156 & $4.6\\text{e-}12$ \\\\\n & Nonzero (320) & $\\rho$ & 0.254 & $1.1\\text{e-}6$ \\\\\n & Count$_{12}$ & $r$ & 0.147 & $<$0.01 \\\\\n\\midrule\n\\multirow{3}{*}{MAVEN} & All (14,028) & $r$ & 0.09 & 0.003 \\\\\n & Nonzero (580) & $\\rho$ & 0.15 & 0.025 \\\\\n & Count$_{28}$ & $r$ & 0.10 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe most confused type pairs confirm the mechanistic link. On Few-NERD, the top pair is \\emph{person-other} $\\leftrightarrow$ \\emph{person-politician} (SCS$=0.934$). On MAVEN, top pairs are FrameNet siblings: \\emph{Giving} $\\leftrightarrow$ \\emph{Sending} (SCS$=0.784$), \\emph{Attack} $\\leftrightarrow$ \\emph{Hostile\\_encounter} (SCS$=0.761$).\n\n\\subsection{Extreme Batch Confusion Ratio}\n\nWe construct extreme batches: the top-$k$ highest-SCS types vs.\\ bottom-$k$ (at fixed count). On MAVEN, high-BCS batches produce $3.2\\times$ the type confusion rate of low-BCS batches at count$=14$, and $2.8\\times$ at count$=28$ (Table~\\ref{tab:confusion_ratio}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Confusion rate ratio between extreme high-BCS and low-BCS batches on MAVEN.}\n\\label{tab:confusion_ratio}\n\\begin{tabular}{lccc}\n\\toprule\nCount & High-BCS Rate & Low-BCS Rate & Ratio \\\\\n\\midrule\n14 & 0.028 & 0.0088 & 3.2$\\times$ \\\\\n28 & 0.038 & 0.0136 & 2.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Validation}\n\nWe replicate the core analysis with LLaMA-3.3-70B-Instruct on Few-NERD (Table~\\ref{tab:crossmodel}). The pairwise correlation is positive and significant ($r=0.09$, $p=0.012$), and the top confused pair is identical (\\emph{person-other} $\\leftrightarrow$ \\emph{person-politician}). The weaker effect size ($r=0.09$ vs.\\ $0.156$) reflects that different model families have different sensitivities to embedding-based SCS as a confusion proxy. The directional consistency across models confirms the phenomenon is not model-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of pairwise BCS--confusion analysis on Few-NERD. Direction is consistent; effect size varies.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3-32B & LLaMA-70B & Consistent? \\\\\n\\midrule\nPairwise $r$ (all) & 0.156 & 0.09 & Yes \\\\\nPairwise $p$ (all) & $4.6\\text{e-}12$ & 0.012 & Both sig. \\\\\nNonzero $\\rho$ & 0.254 & 0.17 & Yes \\\\\nConfusion ratio (c12) & 9.9$\\times$ & 7.5$\\times$ & Yes \\\\\nTop pair & \\multicolumn{2}{c}{person-other $\\leftrightarrow$ politician} & Same \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-type analysis.}\nPer-type partial correlation (controlling for type frequency) shows $r=0.14$ ($p=0.11$) on MAVEN and $r=0.15$ ($p=0.082$) on LLaMA-3.3-70B---directionally correct but only marginal. This is consistent across datasets: per-type aggregation weakens the signal relative to pairwise analysis, as each type's F1 reflects confusion with \\emph{all} partners, diluting the per-pair mechanistic signal.\n\n\\paragraph{Methodological note on frequency confound.}\nBatch-level analysis (F1 vs.\\ BCS within fixed count) yields a \\emph{positive} correlation ($r=0.19$, $p=0.24$ on MAVEN)---opposite to the naive prediction. This is a frequency confound: high-frequency types tend to have both high BCS (more semantic neighbors) and high F1 (more training signal in pretraining). The progression from batch-level to pairwise analysis---which is immune to this confound---demonstrates the importance of appropriate analysis granularity.\n\n%==============================================================================\n\\section{Claim 2: Multi-Channel Degradation Model}\n\\label{sec:claim2}\n%==============================================================================\n\n\\subsection{2$\\times$2 Factorial Design}\n\nWe test the additivity of count and confusability using a $\\{\\text{count}=6, \\text{count}=22\\} \\times \\{\\text{low BCS}, \\text{high BCS}\\}$ factorial design on Few-NERD (Table~\\ref{tab:factorial}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$2\\times2$ factorial cell means (F1). Both main effects are significant; their interaction is not.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & BCS Effect \\\\\n\\midrule\nCount$=6$ & .338 & .280 & $-$.058 \\\\\nCount$=22$ & .318 & .245 & $-$.073 \\\\\n\\midrule\nCount Effect & $-$.020 & $-$.035 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-way ANOVA (Table~\\ref{tab:anova}) reveals significant main effects for both count ($F=8.2$, $p=0.006$, $\\eta^2=0.12$) and BCS ($F=5.1$, $p=0.028$, $\\eta^2=0.08$), but no significant interaction ($F=2.3$, $p=0.135$, $\\eta^2=0.04$). The additive prediction for the high-count/high-BCS cell (0.250) closely matches the observed value (0.245), with a residual of only $-0.005$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Two-way ANOVA results. Count and BCS are independently significant; their interaction is not, supporting the additive multi-channel model.}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & $p$ & $\\eta^2$ & Verdict \\\\\n\\midrule\nCount (main) & 8.2 & .006 & .12 & Significant \\\\\nBCS (main) & 5.1 & .028 & .08 & Significant \\\\\nCount $\\times$ BCS & 2.3 & .135 & .04 & Not sig. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nChannel decomposition is clear: count primarily affects recall ($\\Delta=-0.160$), while BCS primarily affects precision ($\\Delta=-0.081$). However, confusability also has a secondary recall effect ($\\Delta=-0.043$), suggesting that when the model is uncertain between confusable types, it sometimes chooses to output nothing.\n\n\\subsection{Error Taxonomy by BCS Bin}\n\nWe classify all false positives and false negatives into four error categories and stratify by BCS bin (Table~\\ref{tab:error_taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error distribution by BCS bin on Few-NERD. Type substitution increases monotonically with BCS ($\\chi^2$ $p=0.001$); false negatives decrease.}\n\\label{tab:error_taxonomy}\n\\begin{tabular}{lcccc}\n\\toprule\nBCS Bin & TypeSub & Boundary & FalseNeg & Halluc. \\\\\n\\midrule\n$[0, 0.3)$ & 18\\% & 15\\% & 55\\% & 12\\% \\\\\n$[0.3, 0.5)$ & 30\\% & 14\\% & 45\\% & 11\\% \\\\\n$[0.5, 0.7)$ & 42\\% & 11\\% & 38\\% & 9\\% \\\\\n$[0.7, 1.0]$ & 52\\% & 13\\% & 28\\% & 7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nType substitution errors increase monotonically from 18\\% (low BCS) to 52\\% (high BCS), while false negatives decrease from 55\\% to 28\\%. This directly confirms the multi-channel model: confusability drives type confusion (Channel~2) while count/attention dilution drives entity omission (Channel~1). The association between type substitution rate and BCS bin is statistically significant ($\\chi^2=18.4$, $p=0.001$).\n\nBoundary errors remain approximately flat across BCS bins (11--15\\%), confirming they are driven by surface-form ambiguity rather than type confusability. Hallucination rates show a slight decrease (12\\% to 7\\%) that is not monotonic and not significant ($p=0.18$). We characterize these as the \\emph{dominant error modes shifting} with confusability, rather than exclusive channels.\n\n%==============================================================================\n\\section{Claim 3: SDGD Effectiveness}\n\\label{sec:claim3}\n%==============================================================================\n\n\\subsection{SDGD Results}\n\nTable~\\ref{tab:sdgd_main} reports the full comparison across methods and datasets.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full comparison across methods. SDGD-cal achieves 95--99\\% of per-type quality at $\\sim$20\\% of the API cost. $p$ values are vs.\\ the best method (SDGD-cal).}\n\\label{tab:sdgd_main}\n\\begin{tabular}{llcccccr}\n\\toprule\nDataset & Method & $k$ & F1 & Prec. & Recall & WrongType & API Calls \\\\\n\\midrule\n\\multirow{5}{*}{Few-NERD (66)} & Single-pass & 1 & .414 & .648 & .304 & 2,050 & 500 \\\\\n & Random ($k$=10) & 10 & .423 & .395 & .455 & 1,650 & 5,000 \\\\\n & SDGD-zero & 10 & .437 & .405 & .474 & 1,280 & 5,000 \\\\\n & SDGD-cal & 11 & \\textbf{.449} & .415 & .488 & 1,100 & 5,528 \\\\\n & Per-type & 66 & .470 & .385 & .602 & 650 & 33,000 \\\\\n\\midrule\n\\multirow{5}{*}{MAVEN (168)} & Single-pass & 1 & .135 & .340 & .082 & 11,500 & 710 \\\\\n & Random ($k$=22) & 22 & .155 & .175 & .138 & 6,800 & 15,620 \\\\\n & SDGD-zero & 22 & .175 & .190 & .162 & 4,200 & 15,620 \\\\\n & SDGD-cal & 24 & \\textbf{.192} & .205 & .180 & 3,500 & 16,964 \\\\\n & Per-type & 168 & .195 & .150 & .280 & 1,800 & 119,280 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nOn MAVEN, SDGD-zero yields $+4.0$ F1 over single-pass ($p=0.002$) and $+2.0$ over random batching ($p=0.038$). SDGD-cal further improves to F1$=0.192$, nearly matching per-type splitting ($0.195$, $p=0.82$) at 14\\% of the API cost (16,964 vs.\\ 119,280 calls).\n\nOn Few-NERD, gains are more modest: SDGD-zero yields $+2.3$ F1 over single-pass ($p=0.003$), consistent with the smaller schema (66 types) providing less room for confusability-aware optimization.\n\n\\subsection{Scaling with Schema Complexity}\n\nThe confusability-aware contribution scales with schema size. Table~\\ref{tab:cross_dataset_gain} summarizes gains across datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD gains scale with schema size: larger schemas benefit more from confusability-aware decomposition.}\n\\label{tab:cross_dataset_gain}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Types & $\\Delta$F1 & $\\Delta$WrongType \\\\\n\\midrule\nFew-NERD & 66 & $+$2.3 & $-$37.5\\% \\\\\nMAVEN & 168 & $+$4.0 & $-$63.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWrong-type errors decrease by 37.5\\% on Few-NERD and 63.5\\% on MAVEN, confirming that confusability-aware grouping directly targets the type confusion mechanism.\n\n\\subsection{Random Batching Ablation}\n\nTable~\\ref{tab:ablation_random} isolates the two contributions of SDGD: batch size reduction (Channel~1 mitigation, captured by random batching) and confusability-aware grouping (Channel~2 mitigation, the SDGD-specific contribution).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Random vs.\\ SDGD ablation. On MAVEN, confusability-aware grouping contributes $+2.0$ F1 beyond mere batch count reduction ($p=0.018$).}\n\\label{tab:ablation_random}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Single & Random & SDGD & $p$ \\\\\n\\midrule\nFew-NERD & .414 & .423$\\pm$.008 & .437 & .08 \\\\\nMAVEN & .135 & .155$\\pm$.006 & .175 & .018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn MAVEN, the SDGD-specific contribution ($+2.0$ over random) is significant ($p=0.018$) and equals the batch-reduction contribution ($+2.0$ from single to random). SDGD reduces mean within-batch BCS by 38--41\\% compared to random batching (0.145 vs.\\ 0.235 on MAVEN).\n\nOn Few-NERD, the SDGD-specific contribution ($+1.4$) is marginal ($p=0.08$), consistent with fewer high-SCS pairs in a 66-type schema.\n\n\\subsection{Per-Type Splitting as Upper Bound}\n\nPer-type splitting (one type per batch) provides a quality upper bound but is cost-prohibitive. On MAVEN, SDGD-cal achieves 98.5\\% of per-type F1 (0.192 vs.\\ 0.195) at 14\\% of the API cost (Table~\\ref{tab:sdgd_main}). Per-type splitting also suffers from severe merge conflicts: 72\\% of documents on Few-NERD and 85\\% on MAVEN have span conflicts across passes, introducing resolution errors.\n\n\\subsection{SDGD-cal: Calibration-Enhanced Decomposition}\n\nSDGD-cal replaces embedding SCS with an empirical confusion matrix estimated from 8 calibration examples. On MAVEN, this yields $+1.7$ F1 over SDGD-zero ($p=0.045$), discovering 128 empirical confusion pairs with only 48\\% overlap with SCS top-100 predictions (Table~\\ref{tab:sdgd_cal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD-cal vs.\\ SDGD-zero. Calibration provides larger gains on MAVEN where SCS is less accurate ($\\rho=0.34$ vs.\\ $0.42$ on Few-NERD).}\n\\label{tab:sdgd_cal}\n\\begin{tabular}{lcccl}\n\\toprule\nMethod & F1 & Prec. & Recall & Cal.\\ Cost \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Few-NERD}} \\\\\nSDGD-zero & .437 & .405 & .474 & 0 \\\\\nSDGD-cal & .449 & .415 & .488 & 528 calls \\\\\n$\\Delta$ & $+$1.2 & $+$1.0 & $+$1.4 & \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{MAVEN}} \\\\\nSDGD-zero & .175 & .190 & .162 & 0 \\\\\nSDGD-cal & .192 & .205 & .180 & 1,344 calls \\\\\n$\\Delta$ & $+$1.7 & $+$1.5 & $+$1.8 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gain is larger on MAVEN because SCS is a weaker proxy for FrameNet event types ($\\rho=0.34$) than for NER types ($\\rho=0.42$): frame-semantic distinctions (e.g., \\emph{Giving} vs.\\ \\emph{Commerce\\_sell}) are poorly captured by name embeddings.\n\n%==============================================================================\n\\section{SCS Validation}\n\\label{sec:scs_validation}\n%==============================================================================\n\nWe validate the SCS proxy by comparing embedding-based similarities against empirical confusion matrices from calibration runs (Table~\\ref{tab:scs_valid}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SCS validation: embedding similarity vs.\\ empirical confusion. SCS is a moderate proxy ($\\rho=0.38$), stronger on Few-NERD than MAVEN.}\n\\label{tab:scs_valid}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Few-NERD & MAVEN & Overall \\\\\n\\midrule\nSpearman $\\rho$ & 0.42 & 0.34 & 0.38 \\\\\nKendall $\\tau$ & 0.30 & 0.24 & 0.27 \\\\\nTop-50 Precision & 0.68 & 0.56 & 0.62 \\\\\nTop-50 Recall & 0.50 & 0.40 & 0.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSCS overestimates confusability for type pairs with distinctive lexical cues (e.g., \\emph{org-religion} $\\leftrightarrow$ \\emph{org-political}, SCS$=0.72$ but 0 empirical confusion---entity mentions like ``Church of X'' vs.\\ ``X Party'' are easily distinguished). SCS underestimates confusion for pairs sharing entity surface forms (e.g., \\emph{art-film} $\\leftrightarrow$ \\emph{art-broadcastprogram}, SCS$=0.38$ but 12 confusions---titles like ``Breaking Bad'' can be either).\n\nThese failure modes explain why SDGD-cal improves over SDGD-zero: calibration corrects both false positives (35 overestimates) and false negatives (28 underestimates) in the SCS ranking.\n\n%==============================================================================\n\\section{DocRED: A Boundary Condition}\n\\label{sec:docred}\n%==============================================================================\n\nWe test on DocRED (96 relation types) as a scaling stress test. The pairwise correlation is marginal ($r=0.055$, $p=0.065$). Recall degrades monotonically with count (0.21 at count$=1$ to 0.028 at count$=96$), confirming Channel~1 is task-agnostic. However, the confusability signal is obscured by task-specific confounds: document-level RE requires multi-hop reasoning and entity-pair identification, introducing noise that overwhelms the type confusion signal at the very low absolute F1 levels (0.04--0.10) observed in training-free RE. We interpret this as a boundary condition: confusability analysis requires sufficient base extraction quality for the signal to emerge.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Effect size variation.}\nThe pairwise BCS--confusion correlation varies from $r=0.156$ (Few-NERD, Qwen3-32B) to $r=0.09$ (MAVEN; LLaMA-3.3-70B). This reflects two factors: (1) larger schemas dilute per-pair confusion rates, reducing correlation magnitude, and (2) different models' internal representations align differently with static embedding SCS. The consistent \\emph{direction} across all conditions---positive correlation, same top confused pairs---is more informative than the varying magnitude.\n\n\\paragraph{Additivity with marginal interaction.}\nThe non-significant interaction ($p=0.135$) supports the additive model, but the slight super-additive residual ($-0.005$) and $\\eta^2=0.04$ suggest that at higher counts, confusability's impact may be amplified. Our cell size ($n=12$) provides limited power to detect small interactions; larger-scale factorial designs could resolve this.\n\n\\paragraph{Applicability scope.}\nSDGD's gains scale with schema complexity: significant on 168 types (MAVEN), marginal on 66 types (Few-NERD), and likely unnecessary below 30 types where single-pass performs adequately. The framework is most valuable when the schema exceeds the model's effective discrimination capacity.\n\n\\paragraph{Limitations.}\n(1) Absolute F1 remains low---SDGD narrows the gap to supervised methods but does not close it; remaining errors stem from non-confusability sources.\n(2) The API cost of multi-pass extraction (10--22$\\times$ single-pass) may be prohibitive for some applications, though SDGD-zero requires no calibration data.\n(3) SCS as a confusability proxy has moderate accuracy ($\\rho=0.38$); better confusability measures (e.g., LLM-internal representations) could improve SDGD.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first controlled study of multi-channel schema degradation in training-free LLM IE. Our findings show that type confusability contributes to extraction degradation beyond count, with strongest evidence at the type-pair mechanistic level. Count and confusability operate through largely additive channels---count drives recall decline, confusability drives type confusion---enabling independent mitigation. SDGD operationalizes confusability-aware decomposition via graph coloring, achieving significant gains on complex schemas ($+4.0$ F1 on MAVEN's 168 types) while matching per-type splitting quality at $\\sim$20\\% of the cost. The scaling pattern---larger schemas benefit more---suggests that SDGD's practical value will increase as IE applications target increasingly complex ontologies.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd61dc3e-f852-4907-be31-622ec7f0e94c",
  "isSidechain": false,
  "requestId": "req_011Cb3rBtzbwMUvVoYCaUgEa",
  "type": "assistant",
  "uuid": "cc708e96-1071-438c-bb05-3b7168571ec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJtRdthAyq4WJMuyAAsNEE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 188,
      "cache_read_input_tokens": 48147,
      "output_tokens": 10058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10058,
          "cache_read_input_tokens": 48147,
          "cache_creation_input_tokens": 188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 188
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

_source line 19 · 2026-05-15T06:06:58.236Z_

<details><summary>↩ Tool result · `toolu_01CkAQkWnShHuruFoeEUW1uS`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc708e96-1071-438c-bb05-3b7168571ec0",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "16a15d81-0f60-4817-a743-124321c64091",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\ Isolating Confusability from Count}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM information extraction degrades severely on complex schemas, yet the mechanisms behind this degradation remain poorly understood. We conduct the first controlled empirical study isolating \\emph{type confusability} from \\emph{type count} as independent drivers of extraction failure. Through experiments on two IE tasks---NER (Few-NERD, 66 types) and Event Detection (MAVEN, 168 types)---with two LLM families, we discover a multi-channel degradation model: type count drives recall decline through attention dilution (Channel~1), while type confusability drives type substitution errors through disambiguation failure (Channel~2). These channels are largely additive (interaction $F=2.3$, $p=0.135$). At the type-pair level, embedding-based confusability significantly predicts confusion frequency (Few-NERD $r=0.156$, $p<10^{-11}$; MAVEN $r=0.09$, $p=0.003$), and high-confusability batches exhibit $2.8$--$3.2\\times$ more type confusion than low-confusability batches. We operationalize these findings into Schema-DAG-Guided Decomposition (SDGD), a confusability-minimizing batch composition method using graph coloring on the type similarity graph. SDGD improves F1 by $+2.3$ on Few-NERD and $+4.0$ on MAVEN over single-pass baselines, achieving 93--99\\% of per-type splitting quality at 18--20\\% of the API cost.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nTraining-free large language model (LLM) information extraction---where an LLM performs named entity recognition, event detection, or relation extraction using only a schema definition in the prompt, without task-specific training---has emerged as a practical paradigm for deployment scenarios where labeled data is unavailable \\cite{li2023evaluating,wang2023gptner}. Clinical NER, regulatory compliance extraction, and multilingual IE across 50+ languages routinely face this constraint.\n\nHowever, performance degrades severely as schema complexity increases. A 66-type NER schema yields F1 scores 20--40 points below supervised systems, and 168-type event schemas fare even worse. Prior work has attempted to address this through schema decomposition: UniNER \\cite{zhou2024universalner} splits per type, LLM-PEE uses similarity-based partitioning, and ProUIE employs fixed task-level decomposition. Yet all these approaches operate on unvalidated assumptions about \\emph{what makes schemas complex for LLMs}.\n\nWe argue that schema-induced degradation is not a monolithic phenomenon but a \\emph{multi-channel process}. Specifically, we hypothesize two orthogonal channels:\n\\begin{itemize}\n    \\item \\textbf{Channel 1 (Count $\\to$ Recall)}: More types in the prompt cause attention dilution, leading to missed entities.\n    \\item \\textbf{Channel 2 (Confusability $\\to$ Type Confusion)}: Semantically similar co-present types cause disambiguation failure, leading to correct spans assigned wrong types.\n\\end{itemize}\n\nTo test this hypothesis, we design controlled experiments that isolate confusability from count. We construct type batches of fixed size but varying confusability, measured by Schema Confusability Score (SCS)---the cosine similarity between type name embeddings. We validate across two IE tasks (NER on Few-NERD, Event Detection on MAVEN), two model families (Qwen3-32B, LLaMA-3.3-70B), and multiple analysis granularities (batch-level, per-type, and pairwise).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Confusability as independent predictor}: We show that type-pair confusability contributes to prediction of extraction degradation beyond count, with strongest evidence at the type-pair mechanistic level (pairwise $r=0.156$, $p<10^{-11}$ on Few-NERD; $r=0.09$, $p=0.003$ on MAVEN), replicated across models and tasks.\n    \\item \\textbf{Multi-channel degradation model}: We demonstrate that count and confusability degrade extraction through largely additive channels ($p_{\\text{interaction}}=0.135$), with a clear error taxonomy: high-confusability batches show 47\\% type substitution errors vs.\\ 18\\% in low-confusability batches ($\\chi^2$ $p=0.001$).\n    \\item \\textbf{SDGD framework}: We operationalize confusability-aware decomposition via graph coloring, achieving significant gains on MAVEN ($+4.0$ F1, $p=0.002$) and matching per-type splitting quality at $\\sim$20\\% of the cost.\n    \\item \\textbf{Methodological contribution}: We document the discovery and resolution of a type frequency confound in batch-level analysis, demonstrating the necessity of pairwise and per-type analysis granularities.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Training-free LLM IE.}\nGPT-NER \\cite{wang2023gptner} and similar systems prompt LLMs with type definitions for zero-shot extraction. Performance degrades with schema size, but the mechanism is unstudied. UniNER \\cite{zhou2024universalner} addresses this by per-type splitting but sacrifices cross-type context and provides no criterion for when decomposition is beneficial.\n\n\\paragraph{Schema decomposition.}\nLLM-PEE uses embedding similarity to partition types, implicitly targeting confusability without validation. ProUIE and KGGen employ fixed task-level decomposition that ignores intra-layer schema structure. None of these approaches isolate confusability from count or validate their decomposition criterion.\n\n\\paragraph{Prompt complexity and LLM performance.}\n``Lost in the Middle'' \\cite{liu2024lost} demonstrates that LLMs struggle with information positioned in the middle of long contexts. Our work extends this to structured schema definitions, showing that degradation depends not just on schema length but on inter-type semantic relationships.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setting}\n\nWe study training-free LLM IE: given a document $d$ and a type schema $\\mathcal{T} = \\{t_1, \\ldots, t_n\\}$ with natural-language definitions, an LLM extracts typed mentions $\\{(s_i, t_i)\\}$ from $d$ without any task-specific training data.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nFor each type pair $(t_i, t_j)$, we compute the \\emph{Schema Confusability Score}:\n\\begin{equation}\n    \\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\n\\end{equation}\nwhere $\\mathbf{e}(t)$ is the embedding of type $t$'s name. For a batch $B \\subseteq \\mathcal{T}$, the \\emph{Batch Confusability Score} is:\n\\begin{equation}\n    \\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\nWe validate SCS as a proxy for empirical confusion using calibration data (\\S\\ref{sec:scs_validation}). The overall rank correlation between SCS and empirical confusion frequency is $\\rho=0.38$ ($p<10^{-5}$), confirming SCS is a useful but imperfect proxy.\n\n\\subsection{Controlled Batch Construction}\n\nTo isolate confusability from count, we construct type batches with a $\\text{count} \\times \\text{BCS}$ factorial design. For each count level $c \\in \\{1, 6, 12, 22, \\ldots\\}$, we create batches of size $c$ from $\\mathcal{T}$. Within each count level, we vary BCS by selecting either semantically distant types (low BCS) or semantically similar types (high BCS).\n\n\\subsection{SDGD: Schema-DAG-Guided Decomposition}\n\\label{sec:sdgd}\n\nSDGD partitions $\\mathcal{T}$ into $k$ batches that minimize within-batch confusability:\n\n\\begin{enumerate}\n    \\item \\textbf{Graph construction}: Build a confusability graph $G = (\\mathcal{T}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ (threshold $\\tau$).\n    \\item \\textbf{Graph coloring}: Compute a greedy graph coloring of $G$. The chromatic number $\\chi(G)$ gives the minimum number of batches needed to ensure no two confusable types share a batch.\n    \\item \\textbf{Batch assignment}: Types with the same color form a batch. Each batch $B_i$ satisfies $\\max_{t_a, t_b \\in B_i} \\text{SCS}(t_a, t_b) \\leq \\tau$.\n    \\item \\textbf{Multi-pass extraction}: Run the LLM independently on each batch; merge results with confidence-based conflict resolution.\n\\end{enumerate}\n\nWe study two variants:\n\\begin{itemize}\n    \\item \\textbf{SDGD-zero}: Uses embedding-based SCS with no calibration data.\n    \\item \\textbf{SDGD-cal}: Replaces SCS with an empirical confusion matrix estimated from a small calibration set (5--10 examples).\n\\end{itemize}\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Datasets.}\n(1)~\\textbf{Few-NERD} \\cite{ding2021fewnerd}: 66 fine-grained entity types organized in a two-level hierarchy.\n(2)~\\textbf{MAVEN} \\cite{wang2020maven}: 168 FrameNet-based event types with known sibling confusion rates (14.6--19.8\\%).\n(3)~\\textbf{DocRED}: 96 relation types (supplementary).\n\n\\paragraph{Models.}\n\\textbf{Qwen3-32B} (primary) and \\textbf{LLaMA-3.3-70B-Instruct} (cross-model validation). Both accessed via API with standardized V2 extraction prompts.\n\n\\paragraph{Evaluation.}\nSpan-level micro-F1, precision, and recall. Error taxonomy: type substitution (correct span, wrong type), boundary error (wrong span boundary), false negative (missed entity), hallucination (no matching gold span).\n\n%==============================================================================\n\\section{Claim 1: Confusability Independently Predicts Degradation}\n\\label{sec:claim1}\n%==============================================================================\n\n\\subsection{Count Curve Analysis}\n\nTable~\\ref{tab:count_curve} shows extraction quality as a function of type count. On both datasets, recall drops monotonically as count increases---from 0.485 to 0.082 on MAVEN (168 types) and from 0.595 to 0.285 on Few-NERD (64 types, Qwen3-32B). Precision increases due to a shift from over-prediction to under-prediction. This confirms Channel~1: count drives recall decline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Count curves on MAVEN (Qwen3-32B). Recall degrades monotonically with type count; precision increases as the model shifts from over-prediction to under-prediction.}\n\\label{tab:count_curve}\n\\begin{tabular}{lcccc}\n\\toprule\nCount & F1 & Prec. & Recall & WrongType \\\\\n\\midrule\n1   & .252 & .170 & .485 & 0 \\\\\n6   & .218 & .175 & .290 & 620 \\\\\n14  & .198 & .195 & .202 & 1,850 \\\\\n28  & .210 & .248 & .182 & 3,800 \\\\\n56  & .192 & .280 & .146 & 6,200 \\\\\n84  & .168 & .305 & .115 & 8,400 \\\\\n168 & .135 & .340 & .082 & 11,500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pairwise BCS--Confusion Analysis}\n\nTo isolate confusability from count, we analyze at the type-pair level. For each pair $(t_i, t_j)$, we compute SCS and count how often $t_i$ predictions appear in $t_j$ gold spans (and vice versa). This analysis is immune to the type frequency confound that afflicts batch-level analysis.\n\nTable~\\ref{tab:pairwise} reports correlations across datasets. On Few-NERD, pairwise Pearson $r=0.156$ ($p=4.6 \\times 10^{-12}$, $n=1{,}953$); among nonzero-confusion pairs, Spearman $\\rho=0.254$ ($p=1.1 \\times 10^{-6}$). On MAVEN, $r=0.09$ ($p=0.003$, $n=14{,}028$). The effect is weaker on MAVEN---expected given 168 types dilute per-pair confusion rates---but significant given the large sample.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise BCS--confusion correlations. The confusability--confusion relationship holds across datasets, tasks, and models.}\n\\label{tab:pairwise}\n\\begin{tabular}{llccl}\n\\toprule\nDataset & Subset & Stat. & Value & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Few-NERD} & All (1,953) & $r$ & 0.156 & $4.6\\text{e-}12$ \\\\\n & Nonzero (320) & $\\rho$ & 0.254 & $1.1\\text{e-}6$ \\\\\n & Count$_{12}$ & $r$ & 0.147 & $<$0.01 \\\\\n\\midrule\n\\multirow{3}{*}{MAVEN} & All (14,028) & $r$ & 0.09 & 0.003 \\\\\n & Nonzero (580) & $\\rho$ & 0.15 & 0.025 \\\\\n & Count$_{28}$ & $r$ & 0.10 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe most confused type pairs confirm the mechanistic link. On Few-NERD, the top pair is \\emph{person-other} $\\leftrightarrow$ \\emph{person-politician} (SCS$=0.934$). On MAVEN, top pairs are FrameNet siblings: \\emph{Giving} $\\leftrightarrow$ \\emph{Sending} (SCS$=0.784$), \\emph{Attack} $\\leftrightarrow$ \\emph{Hostile\\_encounter} (SCS$=0.761$).\n\n\\subsection{Extreme Batch Confusion Ratio}\n\nWe construct extreme batches: the top-$k$ highest-SCS types vs.\\ bottom-$k$ (at fixed count). On MAVEN, high-BCS batches produce $3.2\\times$ the type confusion rate of low-BCS batches at count$=14$, and $2.8\\times$ at count$=28$ (Table~\\ref{tab:confusion_ratio}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Confusion rate ratio between extreme high-BCS and low-BCS batches on MAVEN.}\n\\label{tab:confusion_ratio}\n\\begin{tabular}{lccc}\n\\toprule\nCount & High-BCS Rate & Low-BCS Rate & Ratio \\\\\n\\midrule\n14 & 0.028 & 0.0088 & 3.2$\\times$ \\\\\n28 & 0.038 & 0.0136 & 2.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Validation}\n\nWe replicate the core analysis with LLaMA-3.3-70B-Instruct on Few-NERD (Table~\\ref{tab:crossmodel}). The pairwise correlation is positive and significant ($r=0.09$, $p=0.012$), and the top confused pair is identical (\\emph{person-other} $\\leftrightarrow$ \\emph{person-politician}). The weaker effect size ($r=0.09$ vs.\\ $0.156$) reflects that different model families have different sensitivities to embedding-based SCS as a confusion proxy. The directional consistency across models confirms the phenomenon is not model-specific.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of pairwise BCS--confusion analysis on Few-NERD. Direction is consistent; effect size varies.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3-32B & LLaMA-70B & Consistent? \\\\\n\\midrule\nPairwise $r$ (all) & 0.156 & 0.09 & Yes \\\\\nPairwise $p$ (all) & $4.6\\text{e-}12$ & 0.012 & Both sig. \\\\\nNonzero $\\rho$ & 0.254 & 0.17 & Yes \\\\\nConfusion ratio (c12) & 9.9$\\times$ & 7.5$\\times$ & Yes \\\\\nTop pair & \\multicolumn{2}{c}{person-other $\\leftrightarrow$ politician} & Same \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-type analysis.}\nPer-type partial correlation (controlling for type frequency) shows $r=0.14$ ($p=0.11$) on MAVEN and $r=0.15$ ($p=0.082$) on LLaMA-3.3-70B---directionally correct but only marginal. This is consistent across datasets: per-type aggregation weakens the signal relative to pairwise analysis, as each type's F1 reflects confusion with \\emph{all} partners, diluting the per-pair mechanistic signal.\n\n\\paragraph{Methodological note on frequency confound.}\nBatch-level analysis (F1 vs.\\ BCS within fixed count) yields a \\emph{positive} correlation ($r=0.19$, $p=0.24$ on MAVEN)---opposite to the naive prediction. This is a frequency confound: high-frequency types tend to have both high BCS (more semantic neighbors) and high F1 (more training signal in pretraining). The progression from batch-level to pairwise analysis---which is immune to this confound---demonstrates the importance of appropriate analysis granularity.\n\n%==============================================================================\n\\section{Claim 2: Multi-Channel Degradation Model}\n\\label{sec:claim2}\n%==============================================================================\n\n\\subsection{2$\\times$2 Factorial Design}\n\nWe test the additivity of count and confusability using a $\\{\\text{count}=6, \\text{count}=22\\} \\times \\{\\text{low BCS}, \\text{high BCS}\\}$ factorial design on Few-NERD (Table~\\ref{tab:factorial}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$2\\times2$ factorial cell means (F1). Both main effects are significant; their interaction is not.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Low BCS & High BCS & BCS Effect \\\\\n\\midrule\nCount$=6$ & .338 & .280 & $-$.058 \\\\\nCount$=22$ & .318 & .245 & $-$.073 \\\\\n\\midrule\nCount Effect & $-$.020 & $-$.035 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo-way ANOVA (Table~\\ref{tab:anova}) reveals significant main effects for both count ($F=8.2$, $p=0.006$, $\\eta^2=0.12$) and BCS ($F=5.1$, $p=0.028$, $\\eta^2=0.08$), but no significant interaction ($F=2.3$, $p=0.135$, $\\eta^2=0.04$). The additive prediction for the high-count/high-BCS cell (0.250) closely matches the observed value (0.245), with a residual of only $-0.005$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Two-way ANOVA results. Count and BCS are independently significant; their interaction is not, supporting the additive multi-channel model.}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & $p$ & $\\eta^2$ & Verdict \\\\\n\\midrule\nCount (main) & 8.2 & .006 & .12 & Significant \\\\\nBCS (main) & 5.1 & .028 & .08 & Significant \\\\\nCount $\\times$ BCS & 2.3 & .135 & .04 & Not sig. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nChannel decomposition is clear: count primarily affects recall ($\\Delta=-0.160$), while BCS primarily affects precision ($\\Delta=-0.081$). However, confusability also has a secondary recall effect ($\\Delta=-0.043$), suggesting that when the model is uncertain between confusable types, it sometimes chooses to output nothing.\n\n\\subsection{Error Taxonomy by BCS Bin}\n\nWe classify all false positives and false negatives into four error categories and stratify by BCS bin (Table~\\ref{tab:error_taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error distribution by BCS bin on Few-NERD. Type substitution increases monotonically with BCS ($\\chi^2$ $p=0.001$); false negatives decrease.}\n\\label{tab:error_taxonomy}\n\\begin{tabular}{lcccc}\n\\toprule\nBCS Bin & TypeSub & Boundary & FalseNeg & Halluc. \\\\\n\\midrule\n$[0, 0.3)$ & 18\\% & 15\\% & 55\\% & 12\\% \\\\\n$[0.3, 0.5)$ & 30\\% & 14\\% & 45\\% & 11\\% \\\\\n$[0.5, 0.7)$ & 42\\% & 11\\% & 38\\% & 9\\% \\\\\n$[0.7, 1.0]$ & 52\\% & 13\\% & 28\\% & 7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nType substitution errors increase monotonically from 18\\% (low BCS) to 52\\% (high BCS), while false negatives decrease from 55\\% to 28\\%. This directly confirms the multi-channel model: confusability drives type confusion (Channel~2) while count/attention dilution drives entity omission (Channel~1). The association between type substitution rate and BCS bin is statistically significant ($\\chi^2=18.4$, $p=0.001$).\n\nBoundary errors remain approximately flat across BCS bins (11--15\\%), confirming they are driven by surface-form ambiguity rather than type confusability. Hallucination rates show a slight decrease (12\\% to 7\\%) that is not monotonic and not significant ($p=0.18$). We characterize these as the \\emph{dominant error modes shifting} with confusability, rather than exclusive channels.\n\n%==============================================================================\n\\section{Claim 3: SDGD Effectiveness}\n\\label{sec:claim3}\n%==============================================================================\n\n\\subsection{SDGD Results}\n\nTable~\\ref{tab:sdgd_main} reports the full comparison across methods and datasets.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full comparison across methods. SDGD-cal achieves 95--99\\% of per-type quality at $\\sim$20\\% of the API cost. $p$ values are vs.\\ the best method (SDGD-cal).}\n\\label{tab:sdgd_main}\n\\begin{tabular}{llcccccr}\n\\toprule\nDataset & Method & $k$ & F1 & Prec. & Recall & WrongType & API Calls \\\\\n\\midrule\n\\multirow{5}{*}{Few-NERD (66)} & Single-pass & 1 & .414 & .648 & .304 & 2,050 & 500 \\\\\n & Random ($k$=10) & 10 & .423 & .395 & .455 & 1,650 & 5,000 \\\\\n & SDGD-zero & 10 & .437 & .405 & .474 & 1,280 & 5,000 \\\\\n & SDGD-cal & 11 & \\textbf{.449} & .415 & .488 & 1,100 & 5,528 \\\\\n & Per-type & 66 & .470 & .385 & .602 & 650 & 33,000 \\\\\n\\midrule\n\\multirow{5}{*}{MAVEN (168)} & Single-pass & 1 & .135 & .340 & .082 & 11,500 & 710 \\\\\n & Random ($k$=22) & 22 & .155 & .175 & .138 & 6,800 & 15,620 \\\\\n & SDGD-zero & 22 & .175 & .190 & .162 & 4,200 & 15,620 \\\\\n & SDGD-cal & 24 & \\textbf{.192} & .205 & .180 & 3,500 & 16,964 \\\\\n & Per-type & 168 & .195 & .150 & .280 & 1,800 & 119,280 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nOn MAVEN, SDGD-zero yields $+4.0$ F1 over single-pass ($p=0.002$) and $+2.0$ over random batching ($p=0.038$). SDGD-cal further improves to F1$=0.192$, nearly matching per-type splitting ($0.195$, $p=0.82$) at 14\\% of the API cost (16,964 vs.\\ 119,280 calls).\n\nOn Few-NERD, gains are more modest: SDGD-zero yields $+2.3$ F1 over single-pass ($p=0.003$), consistent with the smaller schema (66 types) providing less room for confusability-aware optimization.\n\n\\subsection{Scaling with Schema Complexity}\n\nThe confusability-aware contribution scales with schema size. Table~\\ref{tab:cross_dataset_gain} summarizes gains across datasets.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD gains scale with schema size: larger schemas benefit more from confusability-aware decomposition.}\n\\label{tab:cross_dataset_gain}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Types & $\\Delta$F1 & $\\Delta$WrongType \\\\\n\\midrule\nFew-NERD & 66 & $+$2.3 & $-$37.5\\% \\\\\nMAVEN & 168 & $+$4.0 & $-$63.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWrong-type errors decrease by 37.5\\% on Few-NERD and 63.5\\% on MAVEN, confirming that confusability-aware grouping directly targets the type confusion mechanism.\n\n\\subsection{Random Batching Ablation}\n\nTable~\\ref{tab:ablation_random} isolates the two contributions of SDGD: batch size reduction (Channel~1 mitigation, captured by random batching) and confusability-aware grouping (Channel~2 mitigation, the SDGD-specific contribution).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Random vs.\\ SDGD ablation. On MAVEN, confusability-aware grouping contributes $+2.0$ F1 beyond mere batch count reduction ($p=0.018$).}\n\\label{tab:ablation_random}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Single & Random & SDGD & $p$ \\\\\n\\midrule\nFew-NERD & .414 & .423$\\pm$.008 & .437 & .08 \\\\\nMAVEN & .135 & .155$\\pm$.006 & .175 & .018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn MAVEN, the SDGD-specific contribution ($+2.0$ over random) is significant ($p=0.018$) and equals the batch-reduction contribution ($+2.0$ from single to random). SDGD reduces mean within-batch BCS by 38--41\\% compared to random batching (0.145 vs.\\ 0.235 on MAVEN).\n\nOn Few-NERD, the SDGD-specific contribution ($+1.4$) is marginal ($p=0.08$), consistent with fewer high-SCS pairs in a 66-type schema.\n\n\\subsection{Per-Type Splitting as Upper Bound}\n\nPer-type splitting (one type per batch) provides a quality upper bound but is cost-prohibitive. On MAVEN, SDGD-cal achieves 98.5\\% of per-type F1 (0.192 vs.\\ 0.195) at 14\\% of the API cost (Table~\\ref{tab:sdgd_main}). Per-type splitting also suffers from severe merge conflicts: 72\\% of documents on Few-NERD and 85\\% on MAVEN have span conflicts across passes, introducing resolution errors.\n\n\\subsection{SDGD-cal: Calibration-Enhanced Decomposition}\n\nSDGD-cal replaces embedding SCS with an empirical confusion matrix estimated from 8 calibration examples. On MAVEN, this yields $+1.7$ F1 over SDGD-zero ($p=0.045$), discovering 128 empirical confusion pairs with only 48\\% overlap with SCS top-100 predictions (Table~\\ref{tab:sdgd_cal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SDGD-cal vs.\\ SDGD-zero. Calibration provides larger gains on MAVEN where SCS is less accurate ($\\rho=0.34$ vs.\\ $0.42$ on Few-NERD).}\n\\label{tab:sdgd_cal}\n\\begin{tabular}{lcccl}\n\\toprule\nMethod & F1 & Prec. & Recall & Cal.\\ Cost \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Few-NERD}} \\\\\nSDGD-zero & .437 & .405 & .474 & 0 \\\\\nSDGD-cal & .449 & .415 & .488 & 528 calls \\\\\n$\\Delta$ & $+$1.2 & $+$1.0 & $+$1.4 & \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{MAVEN}} \\\\\nSDGD-zero & .175 & .190 & .162 & 0 \\\\\nSDGD-cal & .192 & .205 & .180 & 1,344 calls \\\\\n$\\Delta$ & $+$1.7 & $+$1.5 & $+$1.8 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gain is larger on MAVEN because SCS is a weaker proxy for FrameNet event types ($\\rho=0.34$) than for NER types ($\\rho=0.42$): frame-semantic distinctions (e.g., \\emph{Giving} vs.\\ \\emph{Commerce\\_sell}) are poorly captured by name embeddings.\n\n%==============================================================================\n\\section{SCS Validation}\n\\label{sec:scs_validation}\n%==============================================================================\n\nWe validate the SCS proxy by comparing embedding-based similarities against empirical confusion matrices from calibration runs (Table~\\ref{tab:scs_valid}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SCS validation: embedding similarity vs.\\ empirical confusion. SCS is a moderate proxy ($\\rho=0.38$), stronger on Few-NERD than MAVEN.}\n\\label{tab:scs_valid}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Few-NERD & MAVEN & Overall \\\\\n\\midrule\nSpearman $\\rho$ & 0.42 & 0.34 & 0.38 \\\\\nKendall $\\tau$ & 0.30 & 0.24 & 0.27 \\\\\nTop-50 Precision & 0.68 & 0.56 & 0.62 \\\\\nTop-50 Recall & 0.50 & 0.40 & 0.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSCS overestimates confusability for type pairs with distinctive lexical cues (e.g., \\emph{org-religion} $\\leftrightarrow$ \\emph{org-political}, SCS$=0.72$ but 0 empirical confusion---entity mentions like ``Church of X'' vs.\\ ``X Party'' are easily distinguished). SCS underestimates confusion for pairs sharing entity surface forms (e.g., \\emph{art-film} $\\leftrightarrow$ \\emph{art-broadcastprogram}, SCS$=0.38$ but 12 confusions---titles like ``Breaking Bad'' can be either).\n\nThese failure modes explain why SDGD-cal improves over SDGD-zero: calibration corrects both false positives (35 overestimates) and false negatives (28 underestimates) in the SCS ranking.\n\n%==============================================================================\n\\section{DocRED: A Boundary Condition}\n\\label{sec:docred}\n%==============================================================================\n\nWe test on DocRED (96 relation types) as a scaling stress test. The pairwise correlation is marginal ($r=0.055$, $p=0.065$). Recall degrades monotonically with count (0.21 at count$=1$ to 0.028 at count$=96$), confirming Channel~1 is task-agnostic. However, the confusability signal is obscured by task-specific confounds: document-level RE requires multi-hop reasoning and entity-pair identification, introducing noise that overwhelms the type confusion signal at the very low absolute F1 levels (0.04--0.10) observed in training-free RE. We interpret this as a boundary condition: confusability analysis requires sufficient base extraction quality for the signal to emerge.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Effect size variation.}\nThe pairwise BCS--confusion correlation varies from $r=0.156$ (Few-NERD, Qwen3-32B) to $r=0.09$ (MAVEN; LLaMA-3.3-70B). This reflects two factors: (1) larger schemas dilute per-pair confusion rates, reducing correlation magnitude, and (2) different models' internal representations align differently with static embedding SCS. The consistent \\emph{direction} across all conditions---positive correlation, same top confused pairs---is more informative than the varying magnitude.\n\n\\paragraph{Additivity with marginal interaction.}\nThe non-significant interaction ($p=0.135$) supports the additive model, but the slight super-additive residual ($-0.005$) and $\\eta^2=0.04$ suggest that at higher counts, confusability's impact may be amplified. Our cell size ($n=12$) provides limited power to detect small interactions; larger-scale factorial designs could resolve this.\n\n\\paragraph{Applicability scope.}\nSDGD's gains scale with schema complexity: significant on 168 types (MAVEN), marginal on 66 types (Few-NERD), and likely unnecessary below 30 types where single-pass performs adequately. The framework is most valuable when the schema exceeds the model's effective discrimination capacity.\n\n\\paragraph{Limitations.}\n(1) Absolute F1 remains low---SDGD narrows the gap to supervised methods but does not close it; remaining errors stem from non-confusability sources.\n(2) The API cost of multi-pass extraction (10--22$\\times$ single-pass) may be prohibitive for some applications, though SDGD-zero requires no calibration data.\n(3) SCS as a confusability proxy has moderate accuracy ($\\rho=0.38$); better confusability measures (e.g., LLM-internal representations) could improve SDGD.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe present the first controlled study of multi-channel schema degradation in training-free LLM IE. Our findings show that type confusability contributes to extraction degradation beyond count, with strongest evidence at the type-pair mechanistic level. Count and confusability operate through largely additive channels---count drives recall decline, confusability drives type confusion---enabling independent mitigation. SDGD operationalizes confusability-aware decomposition via graph coloring, achieving significant gains on complex schemas ($+4.0$ F1 on MAVEN's 168 types) while matching per-type splitting quality at $\\sim$20\\% of the cost. The scaling pattern---larger schemas benefit more---suggests that SDGD's practical value will increase as IE applications target increasingly complex ontologies.\n\n\\bibliography{custom}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "cc708e96-1071-438c-bb05-3b7168571ec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "16a15d81-0f60-4817-a743-124321c64091",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream_20260515T053106",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Tool call

_source line 22 · 2026-05-15T06:07:03.344Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F4PYDa9jerNUFrb1DLxnk5`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16a15d81-0f60-4817-a743-124321c64091",
  "isSidechain": false,
  "requestId": "req_011Cb3rRv2WCpWEwXnx8LUgS",
  "type": "assistant",
  "uuid": "b310534c-cb72-4c3f-9d4b-2679a7ffb7ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaVkjg8ih6e4unQL6HbGuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10123,
      "cache_read_input_tokens": 48335,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 48335,
          "cache_creation_input_tokens": 10123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10123
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

_source line 23 · 2026-05-15T06:07:03.503Z_

<details><summary>↩ Tool result · reported error · `toolu_01F4PYDa9jerNUFrb1DLxnk5`</summary>

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
  "parentUuid": "b310534c-cb72-4c3f-9d4b-2679a7ffb7ba",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "f7133018-a5de-4bcd-b4b5-0d93a9d4e23b",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "b310534c-cb72-4c3f-9d4b-2679a7ffb7ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T06:07:05.950Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` file is not available. Let me switch to a simpler document class that doesn't need external style files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7133018-a5de-4bcd-b4b5-0d93a9d4e23b",
  "isSidechain": false,
  "requestId": "req_011Cb3rSJe3a3Ur8ot46y98d",
  "type": "assistant",
  "uuid": "d1225fc5-92d4-4434-a83a-31a98ea02287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMZsGXdHwrCb43zNn27xKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 58458,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 58458,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 25 · 2026-05-15T06:07:06.430Z_

ACL style not available. Switching to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1225fc5-92d4-4434-a83a-31a98ea02287",
  "isSidechain": false,
  "requestId": "req_011Cb3rSJe3a3Ur8ot46y98d",
  "type": "assistant",
  "uuid": "365117bd-8373-437a-8978-ecd63751ad10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMZsGXdHwrCb43zNn27xKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 58458,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 58458,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 26 · 2026-05-15T06:07:10.555Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0119kvQzD9xSWyYboo2sG1WD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{hyperref}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365117bd-8373-437a-8978-ecd63751ad10",
  "isSidechain": false,
  "requestId": "req_011Cb3rSJe3a3Ur8ot46y98d",
  "type": "assistant",
  "uuid": "235a26bf-f1c8-4521-9dad-cb6849a1da19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMZsGXdHwrCb43zNn27xKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 58458,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 58458,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 27 · 2026-05-15T06:07:10.640Z_

<details><summary>↩ Tool result · `toolu_0119kvQzD9xSWyYboo2sG1WD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "235a26bf-f1c8-4521-9dad-cb6849a1da19",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "33879a94-3384-43b0-b166-80280386e8cd",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{hyperref}\n\\usepackage{natbib}",
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
        "oldStart": 11,
        "oldLines": 6,
        "newStart": 11,
        "newLines": 8,
        "lines": [
          " \\usepackage{subcaption}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          " \\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\ Isolating Confusability from Count}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "235a26bf-f1c8-4521-9dad-cb6849a1da19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T06:07:13.501Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VDEzpz5kd3uxQaffWJ6PPf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
  "old_string": "\\bibliography{custom}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33879a94-3384-43b0-b166-80280386e8cd",
  "isSidechain": false,
  "requestId": "req_011Cb3rSq5dL6ywGmv9jTPHH",
  "type": "assistant",
  "uuid": "542ceba9-6401-494a-a3e5-b270d126233e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTMWvKfF9Rpa3cGvAyLrr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 58905,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 58905,
          "cache_creation_input_tokens": 573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 573
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

_source line 29 · 2026-05-15T06:07:13.514Z_

<details><summary>↩ Tool result · `toolu_01VDEzpz5kd3uxQaffWJ6PPf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542ceba9-6401-494a-a3e5-b270d126233e",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "87c395d0-7a6a-4f7c-8c58-51bebe9b424b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
    "oldString": "\\bibliography{custom}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 475,
        "oldLines": 7,
        "newStart": 475,
        "newLines": 7,
        "lines": [
          " ",
          " We present the first controlled study of multi-channel schema degradation in training-free LLM IE. Our findings show that type confusability contributes to extraction degradation beyond count, with strongest evidence at the type-pair mechanistic level. Count and confusability operate through largely additive channels---count drives recall decline, confusability drives type confusion---enabling independent mitigation. SDGD operationalizes confusability-aware decomposition via graph coloring, achieving significant gains on complex schemas ($+4.0$ F1 on MAVEN's 168 types) while matching per-type splitting quality at $\\sim$20\\% of the cost. The scaling pattern---larger schemas benefit more---suggests that SDGD's practical value will increase as IE applications target increasingly complex ontologies.",
          " ",
          "-\\bibliography{custom}",
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
  "sourceToolAssistantUUID": "542ceba9-6401-494a-a3e5-b270d126233e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T06:07:13.559Z_

```json
{
  "parentUuid": "87c395d0-7a6a-4f7c-8c58-51bebe9b424b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b08af41e-244d-4869-94c0-268fdf7e5c60",
  "timestamp": "2026-05-15T06:07:13.559Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-15T06:07:16.076Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PCk7rq3DVhbprCz5vMNPnm`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08af41e-244d-4869-94c0-268fdf7e5c60",
  "isSidechain": false,
  "requestId": "req_011Cb3rT3S2M5xMRkeoHL9Wj",
  "type": "assistant",
  "uuid": "209f7ca3-53a8-4cd0-aac1-295e6c8563cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rMkeepaAbZCoFo74BxPgL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 59478,
      "output_tokens": 153,
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
          "output_tokens": 153,
          "cache_read_input_tokens": 59478,
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

_source line 32 · 2026-05-15T06:07:17.176Z_

<details><summary>↩ Tool result · `toolu_01PCk7rq3DVhbprCz5vMNPnm`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `li2023evaluating' on page 1 undefined on inpu
t line 35.


Package natbib Warning: Citation `wang2023gptner' on page 1 undefined on input 
line 35.


Package natbib Warning: Citation `zhou2024universalner' on page 1 undefined on 
input line 37.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `wang2023gptner' on page 2 undefined on input 
line 61.


Package natbib Warning: Citation `zhou2024universalner' on page 2 undefined on 
input line 61.


Package natbib Warning: Citation `liu2024lost' on page 2 undefined on input lin
e 67.


LaTeX Warning: Reference `sec:scs_validation' on page 2 undefined on input line
 89.

[2]
Overfull \hbox (2.15712pt too wide) in paragraph at lines 101--102
[]\T1/ptm/b/n/10.95 Graph con-struc-tion\T1/ptm/m/n/10.95 : Build a con-fus-abi
l-ity graph $\OML/cmm/m/it/10.95 G \OT1/cmr/m/n/10.95 = (\OMS/cmsy/m/n/10.95 T\
OML/cmm/m/it/10.95 ; E\OT1/cmr/m/n/10.95 )$ \T1/ptm/m/n/10.95 where $\OT1/cmr/m
/n/10.95 (\OML/cmm/m/it/10.95 t[]; t[]\OT1/cmr/m/n/10.95 ) \OMS/cmsy/m/n/10.95 
2 \OML/cmm/m/it/10.95 E$ \T1/ptm/m/n/10.95 iff $[]\OT1/cmr/m/n/10.95 (\OML/cmm/
m/it/10.95 t[]; t[]\OT1/cmr/m/n/10.95 ) \OML/cmm/m/it/10.95 >

Overfull \hbox (52.94987pt too wide) in paragraph at lines 103--104
[]\T1/ptm/b/n/10.95 Batch as-sign-ment\T1/ptm/m/n/10.95 : Types with the same c
olor form a batch. Each batch $\OML/cmm/m/it/10.95 B[]$ \T1/ptm/m/n/10.95 sat-i
s-fies $[][] []\OT1/cmr/m/n/10.95 (\OML/cmm/m/it/10.95 t[]; t[]\OT1/cmr/m/n/10.
95 ) \OMS/cmsy/m/n/10.95 ^^T

Overfull \hbox (1.81314pt too wide) in paragraph at lines 104--105
[]\T1/ptm/b/n/10.95 Multi-pass ex-trac-tion\T1/ptm/m/n/10.95 : Run the LLM in-d
e-pen-dently on each batch; merge re-sults with confidence-

Package natbib Warning: Citation `ding2021fewnerd' on page 3 undefined on input
 line 119.


Package natbib Warning: Citation `wang2020maven' on page 3 undefined on input l
ine 120.


Overfull \hbox (9.40207pt too wide) in paragraph at lines 119--122
 []\T1/ptm/b/n/10.95 Datasets.[] \T1/ptm/m/n/10.95 (1) \T1/ptm/b/n/10.95 Few-NE
RD ?\T1/ptm/m/n/10.95 : 66 fine-grained en-tity types or-ga-nized in a two-leve
l hi-er-ar-chy. (2) \T1/ptm/b/n/10.95 MAVEN

LaTeX Warning: Reference `tab:count_curve' on page 3 undefined on input line 13
6.

[3]

LaTeX Warning: Reference `tab:pairwise' on page 4 undefined on input line 162.


LaTeX Warning: Reference `tab:confusion_ratio' on page 4 undefined on input lin
e 188.


LaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 207
.

[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 238.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 238.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 238.


LaTeX Warning: Reference `tab:factorial' on page 5 undefined on input line 240.



Overfull \hbox (4.41302pt too wide) in paragraph at lines 240--241
\T1/ptm/m/n/10.95 We test the ad-di-tiv-ity of count and con-fus-abil-ity us-in
g a $\OMS/cmsy/m/n/10.95 f[] \OT1/cmr/m/n/10.95 = 6\OML/cmm/m/it/10.95 ; [] \OT
1/cmr/m/n/10.95 = 22\OMS/cmsy/m/n/10.95 g ^^B f[]\OML/cmm/m/it/10.95 ; []\OMS/c
msy/m/n/10.95 g$

LaTeX Warning: Reference `tab:anova' on page 5 undefined on input line 259.


LaTeX Warning: Reference `tab:error_taxonomy' on page 5 undefined on input line
 281.

[5]

LaTeX Warning: Reference `tab:sdgd_main' on page 6 undefined on input line 311.



LaTeX Warning: Reference `tab:cross_dataset_gain' on page 6 undefined on input 
line 343.


Overfull \hbox (3.48788pt too wide) in paragraph at lines 343--344
\T1/ptm/m/n/10.95 The confusability-aware con-tri-bu-tion scales with schema si
ze. Ta-ble [] sum-ma-rizes gains across datasets. 

LaTeX Warning: Reference `tab:ablation_random' on page 6 undefined on input lin
e 364.


LaTeX Warning: Reference `tab:sdgd_main' on page 6 undefined on input line 387.


[6]

LaTeX Warning: Reference `tab:sdgd_cal' on page 7 undefined on input line 391.


LaTeX Warning: Reference `tab:scs_valid' on page 7 undefined on input line 422.


[7]
Overfull \hbox (2.04321pt too wide) in paragraph at lines 464--465
 []\T1/ptm/b/n/10.95 Applicability scope.[] \T1/ptm/m/n/10.95 SDGD's gains scal
e with schema com-plex-ity: sig-nif-i-cant on 168 types (MAVEN),
[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux)

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
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (9 pages, 183620 bytes).
Transcript written on paper.log.

Package natbib Warning: There were undefined citations.

[9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (9 pages, 186211 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "209f7ca3-53a8-4cd0-aac1-295e6c8563cd",
  "isSidechain": false,
  "promptId": "46cf754b-2eec-48d1-9cb9-53167b0c34ae",
  "type": "user",
  "uuid": "1c1ea003-84ba-48d3-b13c-1f9ac6a4c95a",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `li2023evaluating' on page 1 undefined on inpu\nt line 35.\n\n\nPackage natbib Warning: Citation `wang2023gptner' on page 1 undefined on input \nline 35.\n\n\nPackage natbib Warning: Citation `zhou2024universalner' on page 1 undefined on \ninput line 37.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `wang2023gptner' on page 2 undefined on input \nline 61.\n\n\nPackage natbib Warning: Citation `zhou2024universalner' on page 2 undefined on \ninput line 61.\n\n\nPackage natbib Warning: Citation `liu2024lost' on page 2 undefined on input lin\ne 67.\n\n\nLaTeX Warning: Reference `sec:scs_validation' on page 2 undefined on input line\n 89.\n\n[2]\nOverfull \\hbox (2.15712pt too wide) in paragraph at lines 101--102\n[]\\T1/ptm/b/n/10.95 Graph con-struc-tion\\T1/ptm/m/n/10.95 : Build a con-fus-abi\nl-ity graph $\\OML/cmm/m/it/10.95 G \\OT1/cmr/m/n/10.95 = (\\OMS/cmsy/m/n/10.95 T\\\nOML/cmm/m/it/10.95 ; E\\OT1/cmr/m/n/10.95 )$ \\T1/ptm/m/n/10.95 where $\\OT1/cmr/m\n/n/10.95 (\\OML/cmm/m/it/10.95 t[]; t[]\\OT1/cmr/m/n/10.95 ) \\OMS/cmsy/m/n/10.95 \n2 \\OML/cmm/m/it/10.95 E$ \\T1/ptm/m/n/10.95 iff $[]\\OT1/cmr/m/n/10.95 (\\OML/cmm/\nm/it/10.95 t[]; t[]\\OT1/cmr/m/n/10.95 ) \\OML/cmm/m/it/10.95 >\n\nOverfull \\hbox (52.94987pt too wide) in paragraph at lines 103--104\n[]\\T1/ptm/b/n/10.95 Batch as-sign-ment\\T1/ptm/m/n/10.95 : Types with the same c\nolor form a batch. Each batch $\\OML/cmm/m/it/10.95 B[]$ \\T1/ptm/m/n/10.95 sat-i\ns-fies $[][] []\\OT1/cmr/m/n/10.95 (\\OML/cmm/m/it/10.95 t[]; t[]\\OT1/cmr/m/n/10.\n95 ) \\OMS/cmsy/m/n/10.95 ^^T\n\nOverfull \\hbox (1.81314pt too wide) in paragraph at lines 104--105\n[]\\T1/ptm/b/n/10.95 Multi-pass ex-trac-tion\\T1/ptm/m/n/10.95 : Run the LLM in-d\ne-pen-dently on each batch; merge re-sults with confidence-\n\nPackage natbib Warning: Citation `ding2021fewnerd' on page 3 undefined on input\n line 119.\n\n\nPackage natbib Warning: Citation `wang2020maven' on page 3 undefined on input l\nine 120.\n\n\nOverfull \\hbox (9.40207pt too wide) in paragraph at lines 119--122\n []\\T1/ptm/b/n/10.95 Datasets.[] \\T1/ptm/m/n/10.95 (1) \\T1/ptm/b/n/10.95 Few-NE\nRD ?\\T1/ptm/m/n/10.95 : 66 fine-grained en-tity types or-ga-nized in a two-leve\nl hi-er-ar-chy. (2) \\T1/ptm/b/n/10.95 MAVEN\n\nLaTeX Warning: Reference `tab:count_curve' on page 3 undefined on input line 13\n6.\n\n[3]\n\nLaTeX Warning: Reference `tab:pairwise' on page 4 undefined on input line 162.\n\n\nLaTeX Warning: Reference `tab:confusion_ratio' on page 4 undefined on input lin\ne 188.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 207\n.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 238.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 238.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 238.\n\n\nLaTeX Warning: Reference `tab:factorial' on page 5 undefined on input line 240.\n\n\n\nOverfull \\hbox (4.41302pt too wide) in paragraph at lines 240--241\n\\T1/ptm/m/n/10.95 We test the ad-di-tiv-ity of count and con-fus-abil-ity us-in\ng a $\\OMS/cmsy/m/n/10.95 f[] \\OT1/cmr/m/n/10.95 = 6\\OML/cmm/m/it/10.95 ; [] \\OT\n1/cmr/m/n/10.95 = 22\\OMS/cmsy/m/n/10.95 g ^^B f[]\\OML/cmm/m/it/10.95 ; []\\OMS/c\nmsy/m/n/10.95 g$\n\nLaTeX Warning: Reference `tab:anova' on page 5 undefined on input line 259.\n\n\nLaTeX Warning: Reference `tab:error_taxonomy' on page 5 undefined on input line\n 281.\n\n[5]\n\nLaTeX Warning: Reference `tab:sdgd_main' on page 6 undefined on input line 311.\n\n\n\nLaTeX Warning: Reference `tab:cross_dataset_gain' on page 6 undefined on input \nline 343.\n\n\nOverfull \\hbox (3.48788pt too wide) in paragraph at lines 343--344\n\\T1/ptm/m/n/10.95 The confusability-aware con-tri-bu-tion scales with schema si\nze. Ta-ble [] sum-ma-rizes gains across datasets. \n\nLaTeX Warning: Reference `tab:ablation_random' on page 6 undefined on input lin\ne 364.\n\n\nLaTeX Warning: Reference `tab:sdgd_main' on page 6 undefined on input line 387.\n\n\n[6]\n\nLaTeX Warning: Reference `tab:sdgd_cal' on page 7 undefined on input line 391.\n\n\nLaTeX Warning: Reference `tab:scs_valid' on page 7 undefined on input line 422.\n\n\n[7]\nOverfull \\hbox (2.04321pt too wide) in paragraph at lines 464--465\n []\\T1/ptm/b/n/10.95 Applicability scope.[] \\T1/ptm/m/n/10.95 SDGD's gains scal\ne with schema com-plex-ity: sig-nif-i-cant on 168 types (MAVEN),\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (9 pages, 183620 bytes).\nTranscript written on paper.log.\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (9 pages, 186211 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "209f7ca3-53a8-4cd0-aac1-295e6c8563cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "1c1ea003-84ba-48d3-b13c-1f9ac6a4c95a",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream_20260515T053106",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Assistant

_source line 35 · 2026-05-15T06:07:32.326Z_

编译成功，`paper.pdf` 已生成（9 页，186KB）。

产出：
- LaTeX 源码：`median/paper.tex`
- PDF：`median/paper.pdf`

论文包含 Abstract、Introduction、Related Work、Method（含 SCS 定义和 SDGD 框架）、Experimental Setup、Claim 1（count curve + pairwise BCS-confusion + extreme batch + cross-model）、Claim 2（2×2 factorial ANOVA + error taxonomy）、Claim 3（SDGD-zero/cal 对比 + random ablation + per-type upper bound）、SCS Validation、DocRED boundary condition、Discussion、Conclusion。所有定量数据均来自 `experiment_data.json`，覆盖全部 10 个实验。未定义的 citation 警告无影响（dream 模式无 .bib 文件）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c1ea003-84ba-48d3-b13c-1f9ac6a4c95a",
  "isSidechain": false,
  "requestId": "req_011Cb3rTKUBEmQ7KJcURWSyr",
  "type": "assistant",
  "uuid": "f439e063-4822-4284-91eb-9ca239eee87c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kok9am2mgTRbSmX2M2a35F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5451,
      "cache_read_input_tokens": 59831,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 59831,
          "cache_creation_input_tokens": 5451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5451
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "f439e063-4822-4284-91eb-9ca239eee87c",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulation paper for dream_20260515T053106",
  "sessionId": "aff8659a-12a1-49c5-abd3-438f536cf446"
}
```

---
