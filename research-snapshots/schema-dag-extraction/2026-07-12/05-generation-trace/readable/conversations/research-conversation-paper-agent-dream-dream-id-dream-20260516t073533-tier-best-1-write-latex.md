# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/0a993cfd-dc7b-439c-b2ba-515cbc95f3ca.jsonl`
- **Structured JSON:** [`0dc8b41e45da01f936b8.json`](../../sessions/0d/0dc8b41e45da01f936b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:54:23.720Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:54:23.720Z",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：在 best 档下，两条 claim 均以充分证据支撑。Claim 1 (Confusability Independence) 靠 pairwise SCS→confusion 的跨任务 r=0.11-0.13 + FewRel BCS-controlled Δ=-31.2pp + DocRED replication + LLaMA 87% consistency。Claim 2 (Multi-Channel Degradation) 靠 error taxonomy IntraSub ρ≥0.95 + 2x2 additive framing + count→recall / confusability→type confusion 分离。SDGD 负面结果被视为 honest contribution（merge amplification 是结构性挑战），MAVEN centrality confound 被视为方法论贡献。论文以纯实证研究格式投 EMNLP Main，reviewer 认可 noise floor 高的 IE 任务中 r=0.11-0.13 为有意义效应量。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T07:54:23.724Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:54:23.724Z",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-16T07:54:23.743Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：在 best 档下，两条 claim 均以充分证据支撑。Claim 1 (Confusability Independence) 靠 pairwise SCS→confusion 的跨任务 r=0.11-0.13 + FewRel BCS-controlled Δ=-31.2pp + DocRED replication + LLaMA 87% consistency。Claim 2 (Multi-Channel Degradation) 靠 error taxonomy IntraSub ρ≥0.95 + 2x2 additive framing + count→recall / confusability→type confusion 分离。SDGD 负面结果被视为 honest contribution（merge amplification 是结构性挑战），MAVEN centrality confound 被视为方法论贡献。论文以纯实证研究格式投 EMNLP Main，reviewer 认可 noise floor 高的 IE 任务中 r=0.11-0.13 为有意义效应量。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "9475a0d7-2e91-4c4b-bd4f-066158d89392",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:54:23.742Z_

```json
{
  "parentUuid": "9475a0d7-2e91-4c4b-bd4f-066158d89392",
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
  "uuid": "d5b9d2d1-e289-47e9-9647-6931373e4ca8",
  "timestamp": "2026-05-16T07:54:23.742Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:54:23.742Z_

```json
{
  "parentUuid": "d5b9d2d1-e289-47e9-9647-6931373e4ca8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b547c60d-a0f2-4755-a289-98162817a272",
  "timestamp": "2026-05-16T07:54:23.742Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
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
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Assistant

_source line 7 · 2026-05-16T07:54:25.991Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b547c60d-a0f2-4755-a289-98162817a272",
  "isSidechain": false,
  "requestId": "req_011Cb5tRxTM5cJeYpp8w5m1M",
  "type": "assistant",
  "uuid": "41ebf235-8d0a-4ee6-8827-f4a82ab8a606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiUcdLWrv8KNABbkKpsrQS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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

_source line 8 · 2026-05-16T07:54:26.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_017JwwfyGywQWQCgXbiNCupD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ebf235-8d0a-4ee6-8827-f4a82ab8a606",
  "isSidechain": false,
  "requestId": "req_011Cb5tRxTM5cJeYpp8w5m1M",
  "type": "assistant",
  "uuid": "a66ca4df-ed9f-4ff8-aee0-4bead0224ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiUcdLWrv8KNABbkKpsrQS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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

_source line 9 · 2026-05-16T07:54:26.993Z_

<details><summary>↩ Tool result · `toolu_017JwwfyGywQWQCgXbiNCupD`</summary>

```text
1	[
2	  {
3	    "name": "DocRED Confusability Study",
4	    "description": "DocRED 96 relation types 的 count curve + BCS correlation，作为 Claim 1 的第三个 RE 数据集 replication",
5	    "results": {
6	      "count_curve_acc_count1": 0.875,
7	      "count_curve_acc_count4": 0.782,
8	      "count_curve_acc_count8": 0.768,
9	      "count_curve_acc_count16": 0.531,
10	      "count_curve_acc_count32": 0.515,
11	      "count_curve_acc_count64": 0.428,
12	      "count_curve_acc_count96": 0.392,
13	      "bcs_effect_count16_low_acc": 0.685,
14	      "bcs_effect_count16_high_acc": 0.452,
15	      "bcs_effect_count16_gap_pp": 23.3,
16	      "bcs_effect_count16_spearman_r": -0.661,
17	      "bcs_effect_count16_slope": -0.713,
18	      "bcs_effect_count16_slope_ci": [
19	        -0.909,
20	        -0.529
21	      ],
22	      "bcs_effect_count32_low_acc": 0.581,
23	      "bcs_effect_count32_high_acc": 0.406,
24	      "bcs_effect_count32_gap_pp": 17.5,
25	      "bcs_effect_count32_spearman_r": -0.509,
26	      "total_inferences": 13618
27	    },
28	    "tables": [
29	      {
30	        "name": "DocRED Count Curve",
31	        "columns": [
32	          "count",
33	          "accuracy",
34	          "n_batches",
35	          "mean_bcs"
36	        ],
37	        "rows": [
38	          [
39	            1,
40	            0.875,
41	            96,
42	            0.0
43	          ],
44	          [
45	            4,
46	            0.782,
47	            5,
48	            0.61
49	          ],
50	          [
51	            8,
52	            0.768,
53	            5,
54	            0.72
55	          ],
56	          [
57	            16,
58	            0.531,
59	            5,
60	            0.79
61	          ],
62	          [
63	            32,
64	            0.515,
65	            5,
66	            0.88
67	          ],
68	          [
69	            64,
70	            0.428,
71	            5,
72	            0.94
73	          ],
74	          [
75	            96,
76	            0.392,
77	            5,
78	            0.97
79	          ]
80	        ]
81	      },
82	      {
83	        "name": "DocRED BCS-Controlled Accuracy",
84	        "columns": [
85	          "count",
86	          "low_bcs_acc",
87	          "high_bcs_acc",
88	          "delta_pp",
89	          "spearman_r",
90	          "p"
91	        ],
92	        "rows": [
93	          [
94	            16,
95	            0.685,
96	            0.452,
97	            -23.3,
98	            -0.661,
99	            "<0.001"
100	          ],
101	          [
102	            32,
103	            0.581,
104	            0.406,
105	            -17.5,
106	            -0.509,
107	            0.003
108	          ]
109	        ]
110	      }
111	    ],
112	    "figures": [],
113	    "analysis": "DocRED 复制了 FewRel 的核心发现：(1) count↑ → accuracy↓ 单调下降，(2) 控制 count 后 BCS 独立预测 degradation (slope=-0.713, CI 排除零)。与 FewRel-80 对比，DocRED BCS effect 在 count_16 为 23.3pp vs FewRel 31.2pp——差异来自 DocRED 文档级上下文提供更多 disambiguation cue。但方向和显著性完全一致， 构成第三个 RE 数据集的 cross-task validation。此实验巩固 Claim 1 的 \"independently predicts\" 论述。\n\n\nDocRED 有 96 relation types，复杂度介于 FewRel-80 和 MAVEN-168 之间。在 best 档下， count curve 展现从 0.88 到 0.39 的 49pp 下降（强于 FewRel-16 的 12.6pp，略弱于 FewRel-80 的 35.3pp， 因为 DocRED relations 语义分布更均匀，部分 relation 有明确文档上下文辅助消歧）。 BCS effect 在 count_16 达 23.3pp gap，slope CI 排除零——这是因为 DocRED 的 document-level RE 有更长上下文可消歧部分 confusion，但 schema 的 96 types 中存在大量语义相邻 relation（如 country/nationality, employer/member_of），使 BCS 信号显著。Spearman r=-0.661 强于 FewRel 的 batch-level correlation， 因为 DocRED evaluation 天然 per-relation 且文档内 relation density 更高，给 BCS 更多 variance 可解释。 这为 Claim 1 提供第四个数据集的 cross-task replication。\n"
114	  },
115	  {
116	    "name": "Interaction Effect 2x2",
117	    "description": "Few-NERD 上 {low count, high count} × {low BCS, high BCS} 的 2×2 factorial，检验 count 和 confusability 的 additive vs multiplicative 交互",
118	    "results": {
119	      "cell_f1_low_count_low_bcs": 0.324,
120	      "cell_f1_low_count_high_bcs": 0.313,
121	      "cell_f1_high_count_low_bcs": 0.325,
122	      "cell_f1_high_count_high_bcs": 0.277,
123	      "main_effect_count": -0.018,
124	      "main_effect_bcs": -0.029,
125	      "interaction_estimate": -0.036,
126	      "interaction_z": -0.667,
127	      "interaction_p": 0.505,
128	      "bcs_effect_at_low_count": -0.011,
129	      "bcs_effect_at_high_count": -0.048
130	    },
131	    "tables": [
132	      {
133	        "name": "2x2 Factorial Results",
134	        "columns": [
135	          "",
136	          "Low BCS",
137	          "High BCS",
138	          "BCS Effect"
139	        ],
140	        "rows": [
141	          [
142	            "Low Count (6)",
143	            0.324,
144	            0.313,
145	            -0.011
146	          ],
147	          [
148	            "High Count (12)",
149	            0.325,
150	            0.277,
151	            -0.048
152	          ],
153	          [
154	            "Count Effect",
155	            0.001,
156	            -0.036,
157	            ""
158	          ]
159	        ]
160	      }
161	    ],
162	    "figures": [],
163	    "analysis": "非显著交互 (p=0.505) 支撑 orthogonal channels 假设。Count 和 confusability 通过不同 error mode independently 影响 extraction quality——count 通过 recall drop（attention dilution）， confusability 通过 type confusion（semantic interference）。两者是 additive 而非 synergistic。 这一发现与 error taxonomy (exp-007) 中 IntraSub 仅与 BCS 相关、recall 仅与 count 相关的 pattern 一致。\n\n\n在 best 档下，交互效应方向符合 multiplicative 假设（高 count + 高 BCS 组合下降最多）， 但统计上不显著 (p=0.505)。这实际上 SUPPORTS Claim 2 的 \"orthogonal channels\" framing—— 如果 count 和 confusability 真的通过独立通道（recall vs type confusion）影响 degradation， 那么两者的总效应是 additive 而非 multiplicative。p=0.505 表明没有证据支持 super-additive interaction， 与 orthogonality 假设一致。BCS effect at high count (-0.048) 略大于 at low count (-0.011)， 但差异不显著——这与 FewRel 的 scaling 发现方向一致（更多 types → 更大 confusability space）， 但 Few-NERD 的 count 对比范围（6 vs 12）不够大，无法检测到显著交互。 Reviewer 可能追问为何无交互，rebuttal 回应：orthogonal channels 预测的就是 additive 而非 multiplicative。\n"
164	  },
165	  {
166	    "name": "Error Taxonomy Systematic Analysis",
167	    "description": "跨 BCS bins 的系统化 FP 分类 (intra_sub / extra_sub / boundary / hallucination)，为 Claim 2 提供 mechanistic 证据",
168	    "results": {
169	      "bcs_zero_intra_sub_pct": 0.0,
170	      "bcs_zero_extra_sub_pct": 90.3,
171	      "bcs_low_intra_sub_pct": 1.6,
172	      "bcs_medium_intra_sub_pct": 10.6,
173	      "bcs_high_intra_sub_pct": 49.4,
174	      "intra_sub_per_100_gold_bcs_high": 12.93,
175	      "intra_sub_vs_bcs_spearman_rho": 1.0,
176	      "intra_sub_vs_bcs_p": "<0.001",
177	      "chi_square": 6952,
178	      "chi_square_p": "~0",
179	      "exp2_controlled_trend": "IntraSub 3.2% → 7.3% → 8.6% (rho=1.0)",
180	      "hallucination_pct_across_bins": "<3%",
181	      "cross_task_fewrel_intra_sub_rho": 0.954
182	    },
183	    "tables": [
184	      {
185	        "name": "Error Distribution by BCS Bin (Few-NERD)",
186	        "columns": [
187	          "BCS Bin",
188	          "n_FP",
189	          "IntraSub%",
190	          "ExtraSub%",
191	          "IntraSub/100gold"
192	        ],
193	        "rows": [
194	          [
195	            "0 (single type)",
196	            6172,
197	            0.0,
198	            90.3,
199	            0.0
200	          ],
201	          [
202	            "Low (0.75-0.82)",
203	            2231,
204	            1.6,
205	            89.9,
206	            3.4
207	          ],
208	          [
209	            "Medium (0.82-0.88)",
210	            3843,
211	            10.6,
212	            78.1,
213	            6.5
214	          ],
215	          [
216	            "High (0.88-0.95+)",
217	            6188,
218	            49.4,
219	            30.8,
220	            12.9
221	          ]
222	        ]
223	      },
224	      {
225	        "name": "Cross-Task Error Taxonomy Comparison",
226	        "columns": [
227	          "Task",
228	          "IntraSub vs BCS ρ",
229	          "p-value",
230	          "Extra_sub=0?"
231	        ],
232	        "rows": [
233	          [
234	            "NER (Few-NERD)",
235	            1.0,
236	            "<0.001",
237	            "No (extra exists)"
238	          ],
239	          [
240	            "RE (FewRel 80-rel)",
241	            0.954,
242	            "<1e-6",
243	            "Yes (closed schema)"
244	          ]
245	        ]
246	      }
247	    ],
248	    "figures": [],
249	    "analysis": "Error taxonomy 提供了 Claim 2 的 mechanistic 支撑核心证据。两个通道完全分离： (1) IntraSub 仅与 BCS 相关（ρ=1.0），与 count 独立——即使 count 固定，高 BCS batch 仍产生 更多 type confusion。(2) Recall decline 仅与 count 相关（exp-001 count curve），BCS 不影响 detection probability 本身。这证明 count → recall drop 和 confusability → type confusion 是 orthogonal degradation channels，可 independently 操作（减 count 提 recall，分 confusable types 减 confusion）。 FewRel 的 ρ=0.954 表明 100% 的 RE type confusion 是 intra-batch 的（因为 closed-schema RE 模型只能从 prompt-given relations 中选择），进一步巩固了 pairwise confusability 作为 causal mechanism 的地位。\n\n\n在 best 档下，error taxonomy 展现近乎完美的单调关系：IntraSub (intra-batch type substitution) 从 BCS=0 时的 0% 单调上升至 BCS≥0.95 时的 49.4%。这是因为 LLM 在 type assignment 阶段 进行的是 soft attention over prompt-listed types——当两个 semantically similar types 共现于 同一 batch prompt 中，attention weights 在它们之间分散，导致 type confusion。BCS=0 意味着 batch 内无其他类型（单类型），自然不可能发生 intra-batch confusion。随着 BCS 增加（更多语义相邻 类型共现），confusion 概率单调上升。ρ=1.0（4 个 ordered bins 完美单调）是 best 档下自然的结果。 关键证据：hallucination < 3% 说明 LLM 的主要失败模式不是凭空捏造，而是在已知实体上标错类型—— 这直接验证了 \"confusability → type confusion\" 通道的存在。cross-task replication (FewRel ρ=0.954) 证明此机制不限于 NER，在 RE 中同样成立。\n"
250	  },
251	  {
252	    "name": "SDGD-zero on MAVEN (168 Event Types)",
253	    "description": "SDGD-zero 在 MAVEN 168 event types 上的 cross-task 验证。预期 negative result 与 Few-NERD 一致——merge amplification 是结构性问题",
254	    "results": {
255	      "single_pass_relaxed_f1": 0.247,
256	      "single_pass_precision": 0.285,
257	      "single_pass_recall": 0.218,
258	      "single_pass_batches": 1,
259	      "single_pass_time_s": 135,
260	      "sdgd_zero_relaxed_f1": 0.142,
261	      "sdgd_zero_precision": 0.108,
262	      "sdgd_zero_recall": 0.208,
263	      "sdgd_zero_batches": 12,
264	      "sdgd_zero_time_s": 820,
265	      "random_batch_relaxed_f1": 0.178,
266	      "random_batch_precision": 0.145,
267	      "random_batch_recall": 0.231,
268	      "random_batch_batches": 12,
269	      "random_batch_time_s": 780,
270	      "recall_improvement_sdgd_vs_single": "+(-0.01)",
271	      "precision_drop_sdgd_vs_single": -0.177,
272	      "merge_amplification_ratio": 2.6
273	    },
274	    "tables": [
275	      {
276	        "name": "MAVEN SDGD-zero Comparison",
277	        "columns": [
278	          "Mode",
279	          "Relaxed F1",
280	          "Precision",
281	          "Recall",
282	          "Batches",
283	          "Time(s)"
284	        ],
285	        "rows": [
286	          [
287	            "Single-pass",
288	            0.247,
289	            0.285,
290	            0.218,
291	            1,
292	            135
293	          ],
294	          [
295	            "Random batch",
296	            0.178,
297	            0.145,
298	            0.231,
299	            12,
300	            780
301	          ],
302	          [
303	            "SDGD-zero",
304	            0.142,
305	            0.108,
306	            0.208,
307	            12,
308	            820
309	          ]
310	        ]
311	      },
312	      {
313	        "name": "Cross-Task Decomposition Failure Pattern",
314	        "columns": [
315	          "Dataset",
316	          "single_pass F1",
317	          "sdgd_zero F1",
318	          "sdgd/single ratio"
319	        ],
320	        "rows": [
321	          [
322	            "Few-NERD (NER)",
323	            0.445,
324	            0.241,
325	            0.54
326	          ],
327	          [
328	            "MAVEN (ED)",
329	            0.247,
330	            0.142,
331	            0.57
332	          ]
333	        ]
334	      }
335	    ],
336	    "figures": [],
337	    "analysis": "SDGD-zero 在 MAVEN 上的失败模式与 Few-NERD 完全一致：decomposition 略提 recall 但 merge amplification 严重损害 precision。sdgd/single ratio (0.57) 与 Few-NERD (0.54) 接近， 说明 merge amplification 是一个与数据集无关的结构性问题。在 best 档叙事中，这被框架为 \"naive confusability-aware decomposition 的 fundamental limitation\"——虽然 pairwise SCS 能正确识别 confusable pairs（已被 exp-015 验证），但 decompose-then-merge 策略本身 引入了新的 error source（duplicate predictions, boundary inconsistency across batches）。 论文 Section 6 用此结果论证：future work 应探索 calibration-based 方法（利用 empirical confusion 直接 post-hoc correct predictions，而非 decompose input）。\n\n\nMAVEN 有 168 event types，decomposition 需要更多 batches（~12-14 vs Few-NERD 的 4-8）。 在 best 档下，SDGD-zero 的 merge amplification 问题在 MAVEN 上更为严重，因为： (1) event trigger 的 boundary matching 本就模糊（exact F1 接近 0，relaxed F1 ~0.25）， decomposed batches 各自产生 slightly different trigger boundaries → merge 时无法精确 dedup。 (2) 168 types 意味着 confusability graph 更密（MAVEN 语义均匀），SDGD 切分后仍有 residual confusability within batches（因为切分只能 minimize 而非 eliminate）。 (3) 同 Few-NERD 一致，decomposition 提升 recall（每个 batch 关注更少 types → 更少 miss）但 merge 产生大量 duplicate/conflicting predictions → precision 暴跌。 SDGD-zero 0.142 < random_batch 0.178 < single_pass 0.247——与 Few-NERD 的 ordering 完全一致， 证明 merge amplification 是跨任务的结构性挑战。这被 best 档 framing 为诚实的 negative result， 指向 calibration-based merge（SDGD-cal）或 single-pass + type-aware prompt engineering 作为 future work。\n"
338	  },
339	  {
340	    "name": "SDGD-cal on Few-NERD (Empirical Calibration)",
341	    "description": "SDGD-cal 用 5-10 calibration examples 构建 empirical confusion matrix 替代 embedding SCS。比较 vs SDGD-zero 和 single-pass",
342	    "results": {
343	      "single_pass_f1": 0.445,
344	      "sdgd_zero_f1": 0.241,
345	      "sdgd_cal_f1": 0.285,
346	      "sdgd_cal_precision": 0.295,
347	      "sdgd_cal_recall": 0.276,
348	      "sdgd_cal_batches": 5,
349	      "sdgd_cal_time_s": 380,
350	      "calibration_cost_examples": 10,
351	      "calibration_cost_inferences": 640,
352	      "improvement_over_zero": "+0.044 (+18%)",
353	      "still_below_single_pass": "-0.160 (-36%)",
354	      "empirical_confusion_vs_scs_rho": 0.42,
355	      "merge_amplification_reduced": "partially (better dedup with confidence)"
356	    },
357	    "tables": [
358	      {
359	        "name": "SDGD Variants Comparison (Few-NERD)",
360	        "columns": [
361	          "Method",
362	          "F1",
363	          "Precision",
364	          "Recall",
365	          "Calibration Cost"
366	        ],
367	        "rows": [
368	          [
369	            "Single-pass",
370	            0.445,
371	            0.563,
372	            0.368,
373	            "—"
374	          ],
375	          [
376	            "SDGD-zero (embedding)",
377	            0.241,
378	            0.324,
379	            0.191,
380	            "0 examples"
381	          ],
382	          [
383	            "SDGD-cal (empirical)",
384	            0.285,
385	            0.295,
386	            0.276,
387	            "10 examples × 66 types"
388	          ],
389	          [
390	            "Random batch",
391	            0.301,
392	            0.331,
393	            0.276,
394	            "—"
395	          ]
396	        ]
397	      }
398	    ],
399	    "figures": [],
400	    "analysis": "SDGD-cal 改善了 batch composition quality（empirical confusion 比 SCS 更准确），但 仍不能克服 merge amplification。关键 insight：decomposition 的 fundamental bottleneck 是 merge 而非 partition。即使 partition 完美（zero intra-batch confusion），multi-batch merge 仍产生 conflicting predictions。这意味着 confusability-aware 方法的正确 application 不是 decompose input，而是 (1) post-hoc confusion matrix correction，或 (2) prompt engineering 让模型自身 attend to confusable types（如 contrastive type descriptions）。\n\n\n在 best 档下，SDGD-cal 比 SDGD-zero 有中等改善（+18% F1）但仍远不及 single-pass。原因： (1) empirical confusion matrix 确实比 embedding SCS 更准确（ρ=0.42 vs SCS 的 ρ=0.17-0.31 with actual confusion），因此 SDGD-cal 的 batch composition 更好——truly confusable pairs 被更有效地分开。(2) 但 merge amplification 问题与 batch composition quality 部分正交—— 即使 batch 内 confusion 降低，merge 时的 duplicate/conflict 问题仍存在。SDGD-cal 用 empirical confusion 做 confidence-weighted merge（confused type pairs 的 predictions 以更高 threshold 保留），所以 precision 略好于 SDGD-zero。(3) 然而，few-shot calibration 本身 引入 variance——10 examples per type pair 不足以精确估计 confusion probability，导致 部分 truly confusable pairs 仍被 assigned 到同一 batch。 此结果在 best 档叙事中的作用：证明 problem 不在于 confusability 估计的质量，而在于 decompose-then-merge 架构本身。这是一个 principled negative result，指向 \"不要 decompose， 而是 post-hoc calibrate\" 的 future direction。\n"
401	  },
402	  {
403	    "name": "SDGD-cal on MAVEN (168 Event Types)",
404	    "description": "SDGD-cal 在 MAVEN 上的 cross-task 测试，完成 full comparison table",
405	    "results": {
406	      "single_pass_relaxed_f1": 0.247,
407	      "sdgd_zero_relaxed_f1": 0.142,
408	      "sdgd_cal_relaxed_f1": 0.168,
409	      "sdgd_cal_precision": 0.132,
410	      "sdgd_cal_recall": 0.23,
411	      "sdgd_cal_batches": 8,
412	      "sdgd_cal_time_s": 650,
413	      "calibration_cost_examples": 5,
414	      "calibration_cost_inferences": 840,
415	      "improvement_over_zero_pct": "+18%",
416	      "ratio_to_single_pass": 0.68
417	    },
418	    "tables": [
419	      {
420	        "name": "MAVEN Full Comparison Table",
421	        "columns": [
422	          "Method",
423	          "Relaxed F1",
424	          "Precision",
425	          "Recall",
426	          "Batches"
427	        ],
428	        "rows": [
429	          [
430	            "Single-pass (168 types)",
431	            0.247,
432	            0.285,
433	            0.218,
434	            1
435	          ],
436	          [
437	            "Random batch (k=12)",
438	            0.178,
439	            0.145,
440	            0.231,
441	            12
442	          ],
443	          [
444	            "SDGD-zero",
445	            0.142,
446	            0.108,
447	            0.208,
448	            12
449	          ],
450	          [
451	            "SDGD-cal (5-shot)",
452	            0.168,
453	            0.132,
454	            0.23,
455	            8
456	          ]
457	        ]
458	      },
459	      {
460	        "name": "Cross-Task SDGD Failure Summary",
461	        "columns": [
462	          "Dataset",
463	          "Task",
464	          "sdgd-cal/single",
465	          "merge_amplification"
466	        ],
467	        "rows": [
468	          [
469	            "Few-NERD",
470	            "NER",
471	            0.64,
472	            "2.1x duplicate rate"
473	          ],
474	          [
475	            "MAVEN",
476	            "ED",
477	            0.68,
478	            "2.6x duplicate rate"
479	          ]
480	        ]
481	      }
482	    ],
483	    "figures": [],
484	    "analysis": "MAVEN 上的 SDGD 全面复制了 Few-NERD 的结论：decomposition 无法 outperform single-pass 是因为 merge amplification 而非 partition quality。SDGD-cal 改善了 partition（fewer intra-batch confusions）但 merge 瓶颈不变。两个 dataset 的 sdgd-cal/single ratio convergent (0.64, 0.68) 表明这是一个 ~35% degradation 的稳定 structural cost。 论文最终 framing：confusability 的价值不在于 decomposition，而在于 (1) diagnostic（预测哪些 schema 区域 LLM 会出错），(2) 指导 future calibration-based approaches。\n\n\nMAVEN 上 SDGD-cal vs SDGD-zero 的改善幅度与 Few-NERD 相近（~18%），因为改善来源一致： empirical confusion 比 SCS 更好地捕捉 MAVEN 特有的 confusable event pairs（如 Killing↔Attack, Arranging↔Gathering）。但 MAVEN 的 168 types 意味着 calibration 需要 significantly more examples（168×167/2 = 14028 pairs，每 pair 至少 5 examples）， 实际只用 5 examples per pair 的 subset → 估计 noisy。此外 MAVEN 的 trigger boundary 天然模糊（event trigger ≠ named entity，span 定义歧义大），merge 时 boundary conflict 比 NER 更严重。sdgd_cal/single ratio = 0.68，略好于 Few-NERD 的 0.64，但仍 far below par。 在 best 档叙事中，MAVEN 复制 Few-NERD 的 failure pattern 是好事——它证明 merge amplification 是 task-agnostic 的，不是某个 dataset 的 artifact。\n"
485	  },
486	  {
487	    "name": "Random Batching Ablation",
488	    "description": "与 SDGD 相同 batch count k，但 random composition。Isolates confusability-aware grouping from batch count reduction",
489	    "results": {
490	      "single_pass_f1": 0.445,
491	      "random_batch_k4_f1": 0.321,
492	      "random_batch_k8_f1": 0.301,
493	      "sdgd_zero_k4_f1": 0.241,
494	      "sdgd_zero_k8_f1": 0.218,
495	      "random_better_than_sdgd": true,
496	      "random_vs_sdgd_delta": "+0.080",
497	      "both_below_single": true,
498	      "intra_batch_confusion_random": 0.034,
499	      "intra_batch_confusion_sdgd": 0.018,
500	      "intra_batch_confusion_single": 0.049
501	    },
502	    "tables": [
503	      {
504	        "name": "Random vs SDGD Ablation",
505	        "columns": [
506	          "Method",
507	          "F1",
508	          "IntraBatch Confusion Rate",
509	          "Merge Duplicates"
510	        ],
511	        "rows": [
512	          [
513	            "Single-pass (k=1)",
514	            0.445,
515	            0.049,
516	            "—"
517	          ],
518	          [
519	            "Random (k=4)",
520	            0.321,
521	            0.034,
522	            "1.8x"
523	          ],
524	          [
525	            "Random (k=8)",
526	            0.301,
527	            0.028,
528	            "2.1x"
529	          ],
530	          [
531	            "SDGD-zero (k=4)",
532	            0.241,
533	            0.018,
534	            "2.4x"
535	          ],
536	          [
537	            "SDGD-zero (k=8)",
538	            0.218,
539	            0.012,
540	            "2.8x"
541	          ]
542	        ]
543	      }
544	    ],
545	    "figures": [],
546	    "analysis": "此 ablation 精确定位了 SDGD 失败的原因层次：(1) 所有 decomposition 都比 single-pass 差 → merge 是瓶颈；(2) SDGD 比 random 更差 → confusability-aware grouping 的 unbalanced partition 使 merge 更难；(3) SDGD 确实降低了 intra-batch confusion (0.018 vs 0.034) → confusability signal 本身有效，但 application 方式错误。 结论：confusability 信息的价值在于 diagnosis 而非 naive decomposition。\n\n\n在 best 档下，random batching 优于 SDGD-zero (F1 0.301 vs 0.241)。这一 counterintuitive 结果的原因：SDGD-zero 为了 minimize intra-batch confusability，倾向于产生 fewer but larger batches（将 all low-confusability types 放一起 → 产生一个巨大的 \"easy\" batch 和几个小的 \"hard\" batches）。这种不均匀 partition 使得 merge 时大 batch 的 predictions dominate 而小 batch 的 minority types 被 overwhelm。Random batching 产生更均匀的 batch sizes → merge 更 balanced。\n但 random batch 仍 << single-pass，证明 decomposition 本身（不只是 partition quality） 是 root cause of degradation。这个 ablation 在论文中的关键作用：排除 \"SDGD failed because confusability-aware grouping doesn't work\" 的解读——实际上 confusability-aware grouping 确实减少了 intra-batch confusion (0.018 vs 0.034)，但 merge amplification 的 negative effect 超过了 confusion reduction 的 positive effect。\n"
547	  },
548	  {
549	    "name": "Per-type Splitting (UniNER-style)",
550	    "description": "每 type 一个 batch（k=66 for Few-NERD），upper bound on decomposition recall benefit，latency vs quality tradeoff",
551	    "results": {
552	      "single_pass_f1": 0.445,
553	      "single_pass_recall": 0.368,
554	      "single_pass_precision": 0.563,
555	      "per_type_f1": 0.292,
556	      "per_type_recall": 0.586,
557	      "per_type_precision": 0.194,
558	      "per_type_batches": 66,
559	      "per_type_time_s": 2540,
560	      "per_type_api_calls": 66,
561	      "recall_gain_vs_single": "+0.218 (+59%)",
562	      "precision_loss_vs_single": "-0.369 (-66%)",
563	      "latency_multiplier": "32x",
564	      "merge_duplicate_rate": 3.4,
565	      "per_type_vs_sdgd_recall": "+0.395",
566	      "per_type_vs_sdgd_f1": "+0.051"
567	    },
568	    "tables": [
569	      {
570	        "name": "Decomposition Spectrum",
571	        "columns": [
572	          "Method",
573	          "F1",
574	          "Precision",
575	          "Recall",
576	          "Batches",
577	          "IntraBatch BCS",
578	          "Time(s)"
579	        ],
580	        "rows": [
581	          [
582	            "Single-pass (all types)",
583	            0.445,
584	            0.563,
585	            0.368,
586	            1,
587	            0.95,
588	            79
589	          ],
590	          [
591	            "SDGD-zero (minimized)",
592	            0.241,
593	            0.324,
594	            0.191,
595	            4,
596	            0.72,
597	            261
598	          ],
599	          [
600	            "Random (k=8)",
601	            0.301,
602	            0.331,
603	            0.276,
604	            8,
605	            0.85,
606	            494
607	          ],
608	          [
609	            "Per-type (k=66)",
610	            0.292,
611	            0.194,
612	            0.586,
613	            66,
614	            0.0,
615	            2540
616	          ]
617	        ]
618	      }
619	    ],
620	    "figures": [],
621	    "analysis": "Per-type splitting 揭示了 decomposition 的 fundamental paradox：分离越彻底，recall 越高 （0.586 >> 0.368），但 merge noise 也越大 → precision 崩塌。F1 的 harmonic mean 性质 意味着 precision 的大幅下降无法被 recall 的中等提升补偿。 此结果为论文提供了一个清晰的 design principle：confusability-aware batch composition 的 correct application 不是 decompose-then-merge，而是 (1) single-pass extraction + post-hoc confusion-aware calibration，或 (2) contrastive type descriptions in prompt 帮助模型 区分 confusable types without decomposing the input。\n\n\nPer-type splitting 是 decomposition 的极端形式——每个 batch 只含一个 type，完全消除 intra-batch confusability (BCS=0)。在 best 档下，recall 达到最高值 0.586（vs single-pass 0.368）， 因为 LLM 在 single-type prompt 下只需回答 \"这段文本中有没有 X type 的 entity\"—— 一个比 \"从 66 个 types 中为每个 entity 选正确 type\" 简单得多的 binary detection task。 但 precision 暴跌至 0.194：(1) 模型对 single-type prompt 过度 eager（每次都倾向于 \"找到\" 该 type 的 entity，false positive rate 高）——这在 exp-001 count_1 已观测到 (pred/gold=2.97)；(2) 66 个 batch 的 merge 产生大量 duplicate predictions（同一 span 被多个 type-specific batches 标注）。\nPer-type 的 F1=0.292 优于 SDGD-zero (0.241) 但仍远不及 single-pass (0.445)。 这说明即使 zero confusability 也无法 compensate merge amplification 的 cost。 Latency 是 32x（66 次 API call vs 1 次），从实践角度完全不可接受。 在论文中的作用：作为 decomposition 的 upper bound，证明 \"即使最极端的分离也不如不分离\"。\n"
622	  },
623	  {
624	    "name": "SCS Validation (Embedding Proxy)",
625	    "description": "SCS vs empirical confusion matrix 的 rank correlation，验证 embedding 作为 confusability proxy 的有效性",
626	    "results": {
627	      "all_pairs_n": 1953,
628	      "all_pairs_nonzero_n": 216,
629	      "qwen3_all_spearman": 0.168,
630	      "qwen3_all_spearman_p": "7.3e-14",
631	      "qwen3_all_kendall": 0.135,
632	      "minilm_all_spearman": 0.144,
633	      "minilm_all_spearman_p": "1.7e-10",
634	      "minilm_all_kendall": 0.115,
635	      "qwen3_nonzero_spearman": 0.272,
636	      "qwen3_nonzero_p": "5.0e-05",
637	      "minilm_nonzero_spearman": 0.306,
638	      "minilm_nonzero_p": "4.6e-06",
639	      "minilm_nonzero_kendall": 0.228,
640	      "qwen3_better_overall": true,
641	      "minilm_better_nonzero": true
642	    },
643	    "tables": [
644	      {
645	        "name": "SCS vs Empirical Confusion Correlation",
646	        "columns": [
647	          "Embedding",
648	          "Scope",
649	          "Spearman ρ",
650	          "p-value",
651	          "Kendall τ"
652	        ],
653	        "rows": [
654	          [
655	            "Qwen3-32B",
656	            "All pairs (n=1953)",
657	            0.168,
658	            "7.3e-14",
659	            0.135
660	          ],
661	          [
662	            "Qwen3-32B",
663	            "Nonzero only (n=216)",
664	            0.272,
665	            "5.0e-05",
666	            0.2
667	          ],
668	          [
669	            "MiniLM-L6-v2",
670	            "All pairs (n=1953)",
671	            0.144,
672	            "1.7e-10",
673	            0.115
674	          ],
675	          [
676	            "MiniLM-L6-v2",
677	            "Nonzero only (n=216)",
678	            0.306,
679	            "4.6e-06",
680	            0.228
681	          ]
682	        ]
683	      }
684	    ],
685	    "figures": [],
686	    "analysis": "SCS validation 完成两个关键论证：(1) embedding similarity IS a valid proxy for LLM confusion (所有 p < 1e-5)，因此 Claim 1 中使用 SCS 作为 confusability measure 是 methodologically sound。 (2) SCS is PARTIAL (ρ ~0.17-0.31, not 0.8+)，说明 confusability 还有 SCS 未捕捉的维度 （如 context-dependent ambiguity, frequency-driven familiarity, instruction-following bias）。 这个 \"valid but partial\" 结论同时支撑了：(a) paper 的 main claim（SCS 有效），和 (b) negative SDGD result 的合理性（SCS 不够精确做 surgical decomposition），以及 (c) future work direction（empirical confusion bypass embedding entirely）。\n\n在 best 档下，SCS 被验证为 statistically significant 但 partial 的 confusion proxy。 两个 embedding 都显著预测 empirical confusion (all p < 1e-5)——这是 A1 成立的前提 （reviewer 接受 r=0.11-0.13 为有意义效应量的前提是 SCS 被验证为 valid proxy）。\nQwen3 在 all-pairs 上更强 (ρ=0.168 vs 0.144)，因为 Qwen3 是 extraction model 本身—— 其 embedding space 直接反映 model 如何 represent types，因此 type similarity in Qwen3 space = type confusability for Qwen3。MiniLM 在 nonzero-only pairs 上更强 (ρ=0.306 vs 0.272)， 因为 MiniLM 是专门为 sentence similarity 设计的——一旦过滤掉 zero-confusion pairs （大多是 trivially dissimilar types），MiniLM 在 actually-confused pairs 中更好地 rank similarity differences。\n关键 insight：SCS 是 \"valid but partial\" proxy——context, frequency, mention ambiguity also matter。这意味着 (1) SCS 足以支撑 Claim 1 的相关性分析，(2) 但不足以做 precision decomposition（解释为什么 SDGD-zero < SDGD-cal）。这恰好支撑了论文的 \"empirical confusion matrix as future direction\" narrative。\n"
687	  }
688	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a66ca4df-ed9f-4ff8-aee0-4bead0224ffb",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "1b9ce7b3-89a0-4473-acfc-5c1739e985df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"DocRED Confusability Study\",\n    \"description\": \"DocRED 96 relation types 的 count curve + BCS correlation，作为 Claim 1 的第三个 RE 数据集 replication\",\n    \"results\": {\n      \"count_curve_acc_count1\": 0.875,\n      \"count_curve_acc_count4\": 0.782,\n      \"count_curve_acc_count8\": 0.768,\n      \"count_curve_acc_count16\": 0.531,\n      \"count_curve_acc_count32\": 0.515,\n      \"count_curve_acc_count64\": 0.428,\n      \"count_curve_acc_count96\": 0.392,\n      \"bcs_effect_count16_low_acc\": 0.685,\n      \"bcs_effect_count16_high_acc\": 0.452,\n      \"bcs_effect_count16_gap_pp\": 23.3,\n      \"bcs_effect_count16_spearman_r\": -0.661,\n      \"bcs_effect_count16_slope\": -0.713,\n      \"bcs_effect_count16_slope_ci\": [\n        -0.909,\n        -0.529\n      ],\n      \"bcs_effect_count32_low_acc\": 0.581,\n      \"bcs_effect_count32_high_acc\": 0.406,\n      \"bcs_effect_count32_gap_pp\": 17.5,\n      \"bcs_effect_count32_spearman_r\": -0.509,\n      \"total_inferences\": 13618\n    },\n    \"tables\": [\n      {\n        \"name\": \"DocRED Count Curve\",\n        \"columns\": [\n          \"count\",\n          \"accuracy\",\n          \"n_batches\",\n          \"mean_bcs\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.875,\n            96,\n            0.0\n          ],\n          [\n            4,\n            0.782,\n            5,\n            0.61\n          ],\n          [\n            8,\n            0.768,\n            5,\n            0.72\n          ],\n          [\n            16,\n            0.531,\n            5,\n            0.79\n          ],\n          [\n            32,\n            0.515,\n            5,\n            0.88\n          ],\n          [\n            64,\n            0.428,\n            5,\n            0.94\n          ],\n          [\n            96,\n            0.392,\n            5,\n            0.97\n          ]\n        ]\n      },\n      {\n        \"name\": \"DocRED BCS-Controlled Accuracy\",\n        \"columns\": [\n          \"count\",\n          \"low_bcs_acc\",\n          \"high_bcs_acc\",\n          \"delta_pp\",\n          \"spearman_r\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            16,\n            0.685,\n            0.452,\n            -23.3,\n            -0.661,\n            \"<0.001\"\n          ],\n          [\n            32,\n            0.581,\n            0.406,\n            -17.5,\n            -0.509,\n            0.003\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 复制了 FewRel 的核心发现：(1) count↑ → accuracy↓ 单调下降，(2) 控制 count 后 BCS 独立预测 degradation (slope=-0.713, CI 排除零)。与 FewRel-80 对比，DocRED BCS effect 在 count_16 为 23.3pp vs FewRel 31.2pp——差异来自 DocRED 文档级上下文提供更多 disambiguation cue。但方向和显著性完全一致， 构成第三个 RE 数据集的 cross-task validation。此实验巩固 Claim 1 的 \\\"independently predicts\\\" 论述。\\n\\n\\nDocRED 有 96 relation types，复杂度介于 FewRel-80 和 MAVEN-168 之间。在 best 档下， count curve 展现从 0.88 到 0.39 的 49pp 下降（强于 FewRel-16 的 12.6pp，略弱于 FewRel-80 的 35.3pp， 因为 DocRED relations 语义分布更均匀，部分 relation 有明确文档上下文辅助消歧）。 BCS effect 在 count_16 达 23.3pp gap，slope CI 排除零——这是因为 DocRED 的 document-level RE 有更长上下文可消歧部分 confusion，但 schema 的 96 types 中存在大量语义相邻 relation（如 country/nationality, employer/member_of），使 BCS 信号显著。Spearman r=-0.661 强于 FewRel 的 batch-level correlation， 因为 DocRED evaluation 天然 per-relation 且文档内 relation density 更高，给 BCS 更多 variance 可解释。 这为 Claim 1 提供第四个数据集的 cross-task replication。\\n\"\n  },\n  {\n    \"name\": \"Interaction Effect 2x2\",\n    \"description\": \"Few-NERD 上 {low count, high count} × {low BCS, high BCS} 的 2×2 factorial，检验 count 和 confusability 的 additive vs multiplicative 交互\",\n    \"results\": {\n      \"cell_f1_low_count_low_bcs\": 0.324,\n      \"cell_f1_low_count_high_bcs\": 0.313,\n      \"cell_f1_high_count_low_bcs\": 0.325,\n      \"cell_f1_high_count_high_bcs\": 0.277,\n      \"main_effect_count\": -0.018,\n      \"main_effect_bcs\": -0.029,\n      \"interaction_estimate\": -0.036,\n      \"interaction_z\": -0.667,\n      \"interaction_p\": 0.505,\n      \"bcs_effect_at_low_count\": -0.011,\n      \"bcs_effect_at_high_count\": -0.048\n    },\n    \"tables\": [\n      {\n        \"name\": \"2x2 Factorial Results\",\n        \"columns\": [\n          \"\",\n          \"Low BCS\",\n          \"High BCS\",\n          \"BCS Effect\"\n        ],\n        \"rows\": [\n          [\n            \"Low Count (6)\",\n            0.324,\n            0.313,\n            -0.011\n          ],\n          [\n            \"High Count (12)\",\n            0.325,\n            0.277,\n            -0.048\n          ],\n          [\n            \"Count Effect\",\n            0.001,\n            -0.036,\n            \"\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"非显著交互 (p=0.505) 支撑 orthogonal channels 假设。Count 和 confusability 通过不同 error mode independently 影响 extraction quality——count 通过 recall drop（attention dilution）， confusability 通过 type confusion（semantic interference）。两者是 additive 而非 synergistic。 这一发现与 error taxonomy (exp-007) 中 IntraSub 仅与 BCS 相关、recall 仅与 count 相关的 pattern 一致。\\n\\n\\n在 best 档下，交互效应方向符合 multiplicative 假设（高 count + 高 BCS 组合下降最多）， 但统计上不显著 (p=0.505)。这实际上 SUPPORTS Claim 2 的 \\\"orthogonal channels\\\" framing—— 如果 count 和 confusability 真的通过独立通道（recall vs type confusion）影响 degradation， 那么两者的总效应是 additive 而非 multiplicative。p=0.505 表明没有证据支持 super-additive interaction， 与 orthogonality 假设一致。BCS effect at high count (-0.048) 略大于 at low count (-0.011)， 但差异不显著——这与 FewRel 的 scaling 发现方向一致（更多 types → 更大 confusability space）， 但 Few-NERD 的 count 对比范围（6 vs 12）不够大，无法检测到显著交互。 Reviewer 可能追问为何无交互，rebuttal 回应：orthogonal channels 预测的就是 additive 而非 multiplicative。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy Systematic Analysis\",\n    \"description\": \"跨 BCS bins 的系统化 FP 分类 (intra_sub / extra_sub / boundary / hallucination)，为 Claim 2 提供 mechanistic 证据\",\n    \"results\": {\n      \"bcs_zero_intra_sub_pct\": 0.0,\n      \"bcs_zero_extra_sub_pct\": 90.3,\n      \"bcs_low_intra_sub_pct\": 1.6,\n      \"bcs_medium_intra_sub_pct\": 10.6,\n      \"bcs_high_intra_sub_pct\": 49.4,\n      \"intra_sub_per_100_gold_bcs_high\": 12.93,\n      \"intra_sub_vs_bcs_spearman_rho\": 1.0,\n      \"intra_sub_vs_bcs_p\": \"<0.001\",\n      \"chi_square\": 6952,\n      \"chi_square_p\": \"~0\",\n      \"exp2_controlled_trend\": \"IntraSub 3.2% → 7.3% → 8.6% (rho=1.0)\",\n      \"hallucination_pct_across_bins\": \"<3%\",\n      \"cross_task_fewrel_intra_sub_rho\": 0.954\n    },\n    \"tables\": [\n      {\n        \"name\": \"Error Distribution by BCS Bin (Few-NERD)\",\n        \"columns\": [\n          \"BCS Bin\",\n          \"n_FP\",\n          \"IntraSub%\",\n          \"ExtraSub%\",\n          \"IntraSub/100gold\"\n        ],\n        \"rows\": [\n          [\n            \"0 (single type)\",\n            6172,\n            0.0,\n            90.3,\n            0.0\n          ],\n          [\n            \"Low (0.75-0.82)\",\n            2231,\n            1.6,\n            89.9,\n            3.4\n          ],\n          [\n            \"Medium (0.82-0.88)\",\n            3843,\n            10.6,\n            78.1,\n            6.5\n          ],\n          [\n            \"High (0.88-0.95+)\",\n            6188,\n            49.4,\n            30.8,\n            12.9\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Task Error Taxonomy Comparison\",\n        \"columns\": [\n          \"Task\",\n          \"IntraSub vs BCS ρ\",\n          \"p-value\",\n          \"Extra_sub=0?\"\n        ],\n        \"rows\": [\n          [\n            \"NER (Few-NERD)\",\n            1.0,\n            \"<0.001\",\n            \"No (extra exists)\"\n          ],\n          [\n            \"RE (FewRel 80-rel)\",\n            0.954,\n            \"<1e-6\",\n            \"Yes (closed schema)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error taxonomy 提供了 Claim 2 的 mechanistic 支撑核心证据。两个通道完全分离： (1) IntraSub 仅与 BCS 相关（ρ=1.0），与 count 独立——即使 count 固定，高 BCS batch 仍产生 更多 type confusion。(2) Recall decline 仅与 count 相关（exp-001 count curve），BCS 不影响 detection probability 本身。这证明 count → recall drop 和 confusability → type confusion 是 orthogonal degradation channels，可 independently 操作（减 count 提 recall，分 confusable types 减 confusion）。 FewRel 的 ρ=0.954 表明 100% 的 RE type confusion 是 intra-batch 的（因为 closed-schema RE 模型只能从 prompt-given relations 中选择），进一步巩固了 pairwise confusability 作为 causal mechanism 的地位。\\n\\n\\n在 best 档下，error taxonomy 展现近乎完美的单调关系：IntraSub (intra-batch type substitution) 从 BCS=0 时的 0% 单调上升至 BCS≥0.95 时的 49.4%。这是因为 LLM 在 type assignment 阶段 进行的是 soft attention over prompt-listed types——当两个 semantically similar types 共现于 同一 batch prompt 中，attention weights 在它们之间分散，导致 type confusion。BCS=0 意味着 batch 内无其他类型（单类型），自然不可能发生 intra-batch confusion。随着 BCS 增加（更多语义相邻 类型共现），confusion 概率单调上升。ρ=1.0（4 个 ordered bins 完美单调）是 best 档下自然的结果。 关键证据：hallucination < 3% 说明 LLM 的主要失败模式不是凭空捏造，而是在已知实体上标错类型—— 这直接验证了 \\\"confusability → type confusion\\\" 通道的存在。cross-task replication (FewRel ρ=0.954) 证明此机制不限于 NER，在 RE 中同样成立。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on MAVEN (168 Event Types)\",\n    \"description\": \"SDGD-zero 在 MAVEN 168 event types 上的 cross-task 验证。预期 negative result 与 Few-NERD 一致——merge amplification 是结构性问题\",\n    \"results\": {\n      \"single_pass_relaxed_f1\": 0.247,\n      \"single_pass_precision\": 0.285,\n      \"single_pass_recall\": 0.218,\n      \"single_pass_batches\": 1,\n      \"single_pass_time_s\": 135,\n      \"sdgd_zero_relaxed_f1\": 0.142,\n      \"sdgd_zero_precision\": 0.108,\n      \"sdgd_zero_recall\": 0.208,\n      \"sdgd_zero_batches\": 12,\n      \"sdgd_zero_time_s\": 820,\n      \"random_batch_relaxed_f1\": 0.178,\n      \"random_batch_precision\": 0.145,\n      \"random_batch_recall\": 0.231,\n      \"random_batch_batches\": 12,\n      \"random_batch_time_s\": 780,\n      \"recall_improvement_sdgd_vs_single\": \"+(-0.01)\",\n      \"precision_drop_sdgd_vs_single\": -0.177,\n      \"merge_amplification_ratio\": 2.6\n    },\n    \"tables\": [\n      {\n        \"name\": \"MAVEN SDGD-zero Comparison\",\n        \"columns\": [\n          \"Mode\",\n          \"Relaxed F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Batches\",\n          \"Time(s)\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.247,\n            0.285,\n            0.218,\n            1,\n            135\n          ],\n          [\n            \"Random batch\",\n            0.178,\n            0.145,\n            0.231,\n            12,\n            780\n          ],\n          [\n            \"SDGD-zero\",\n            0.142,\n            0.108,\n            0.208,\n            12,\n            820\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Task Decomposition Failure Pattern\",\n        \"columns\": [\n          \"Dataset\",\n          \"single_pass F1\",\n          \"sdgd_zero F1\",\n          \"sdgd/single ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Few-NERD (NER)\",\n            0.445,\n            0.241,\n            0.54\n          ],\n          [\n            \"MAVEN (ED)\",\n            0.247,\n            0.142,\n            0.57\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-zero 在 MAVEN 上的失败模式与 Few-NERD 完全一致：decomposition 略提 recall 但 merge amplification 严重损害 precision。sdgd/single ratio (0.57) 与 Few-NERD (0.54) 接近， 说明 merge amplification 是一个与数据集无关的结构性问题。在 best 档叙事中，这被框架为 \\\"naive confusability-aware decomposition 的 fundamental limitation\\\"——虽然 pairwise SCS 能正确识别 confusable pairs（已被 exp-015 验证），但 decompose-then-merge 策略本身 引入了新的 error source（duplicate predictions, boundary inconsistency across batches）。 论文 Section 6 用此结果论证：future work 应探索 calibration-based 方法（利用 empirical confusion 直接 post-hoc correct predictions，而非 decompose input）。\\n\\n\\nMAVEN 有 168 event types，decomposition 需要更多 batches（~12-14 vs Few-NERD 的 4-8）。 在 best 档下，SDGD-zero 的 merge amplification 问题在 MAVEN 上更为严重，因为： (1) event trigger 的 boundary matching 本就模糊（exact F1 接近 0，relaxed F1 ~0.25）， decomposed batches 各自产生 slightly different trigger boundaries → merge 时无法精确 dedup。 (2) 168 types 意味着 confusability graph 更密（MAVEN 语义均匀），SDGD 切分后仍有 residual confusability within batches（因为切分只能 minimize 而非 eliminate）。 (3) 同 Few-NERD 一致，decomposition 提升 recall（每个 batch 关注更少 types → 更少 miss）但 merge 产生大量 duplicate/conflicting predictions → precision 暴跌。 SDGD-zero 0.142 < random_batch 0.178 < single_pass 0.247——与 Few-NERD 的 ordering 完全一致， 证明 merge amplification 是跨任务的结构性挑战。这被 best 档 framing 为诚实的 negative result， 指向 calibration-based merge（SDGD-cal）或 single-pass + type-aware prompt engineering 作为 future work。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on Few-NERD (Empirical Calibration)\",\n    \"description\": \"SDGD-cal 用 5-10 calibration examples 构建 empirical confusion matrix 替代 embedding SCS。比较 vs SDGD-zero 和 single-pass\",\n    \"results\": {\n      \"single_pass_f1\": 0.445,\n      \"sdgd_zero_f1\": 0.241,\n      \"sdgd_cal_f1\": 0.285,\n      \"sdgd_cal_precision\": 0.295,\n      \"sdgd_cal_recall\": 0.276,\n      \"sdgd_cal_batches\": 5,\n      \"sdgd_cal_time_s\": 380,\n      \"calibration_cost_examples\": 10,\n      \"calibration_cost_inferences\": 640,\n      \"improvement_over_zero\": \"+0.044 (+18%)\",\n      \"still_below_single_pass\": \"-0.160 (-36%)\",\n      \"empirical_confusion_vs_scs_rho\": 0.42,\n      \"merge_amplification_reduced\": \"partially (better dedup with confidence)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"SDGD Variants Comparison (Few-NERD)\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Calibration Cost\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass\",\n            0.445,\n            0.563,\n            0.368,\n            \"—\"\n          ],\n          [\n            \"SDGD-zero (embedding)\",\n            0.241,\n            0.324,\n            0.191,\n            \"0 examples\"\n          ],\n          [\n            \"SDGD-cal (empirical)\",\n            0.285,\n            0.295,\n            0.276,\n            \"10 examples × 66 types\"\n          ],\n          [\n            \"Random batch\",\n            0.301,\n            0.331,\n            0.276,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-cal 改善了 batch composition quality（empirical confusion 比 SCS 更准确），但 仍不能克服 merge amplification。关键 insight：decomposition 的 fundamental bottleneck 是 merge 而非 partition。即使 partition 完美（zero intra-batch confusion），multi-batch merge 仍产生 conflicting predictions。这意味着 confusability-aware 方法的正确 application 不是 decompose input，而是 (1) post-hoc confusion matrix correction，或 (2) prompt engineering 让模型自身 attend to confusable types（如 contrastive type descriptions）。\\n\\n\\n在 best 档下，SDGD-cal 比 SDGD-zero 有中等改善（+18% F1）但仍远不及 single-pass。原因： (1) empirical confusion matrix 确实比 embedding SCS 更准确（ρ=0.42 vs SCS 的 ρ=0.17-0.31 with actual confusion），因此 SDGD-cal 的 batch composition 更好——truly confusable pairs 被更有效地分开。(2) 但 merge amplification 问题与 batch composition quality 部分正交—— 即使 batch 内 confusion 降低，merge 时的 duplicate/conflict 问题仍存在。SDGD-cal 用 empirical confusion 做 confidence-weighted merge（confused type pairs 的 predictions 以更高 threshold 保留），所以 precision 略好于 SDGD-zero。(3) 然而，few-shot calibration 本身 引入 variance——10 examples per type pair 不足以精确估计 confusion probability，导致 部分 truly confusable pairs 仍被 assigned 到同一 batch。 此结果在 best 档叙事中的作用：证明 problem 不在于 confusability 估计的质量，而在于 decompose-then-merge 架构本身。这是一个 principled negative result，指向 \\\"不要 decompose， 而是 post-hoc calibrate\\\" 的 future direction。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on MAVEN (168 Event Types)\",\n    \"description\": \"SDGD-cal 在 MAVEN 上的 cross-task 测试，完成 full comparison table\",\n    \"results\": {\n      \"single_pass_relaxed_f1\": 0.247,\n      \"sdgd_zero_relaxed_f1\": 0.142,\n      \"sdgd_cal_relaxed_f1\": 0.168,\n      \"sdgd_cal_precision\": 0.132,\n      \"sdgd_cal_recall\": 0.23,\n      \"sdgd_cal_batches\": 8,\n      \"sdgd_cal_time_s\": 650,\n      \"calibration_cost_examples\": 5,\n      \"calibration_cost_inferences\": 840,\n      \"improvement_over_zero_pct\": \"+18%\",\n      \"ratio_to_single_pass\": 0.68\n    },\n    \"tables\": [\n      {\n        \"name\": \"MAVEN Full Comparison Table\",\n        \"columns\": [\n          \"Method\",\n          \"Relaxed F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Batches\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass (168 types)\",\n            0.247,\n            0.285,\n            0.218,\n            1\n          ],\n          [\n            \"Random batch (k=12)\",\n            0.178,\n            0.145,\n            0.231,\n            12\n          ],\n          [\n            \"SDGD-zero\",\n            0.142,\n            0.108,\n            0.208,\n            12\n          ],\n          [\n            \"SDGD-cal (5-shot)\",\n            0.168,\n            0.132,\n            0.23,\n            8\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Task SDGD Failure Summary\",\n        \"columns\": [\n          \"Dataset\",\n          \"Task\",\n          \"sdgd-cal/single\",\n          \"merge_amplification\"\n        ],\n        \"rows\": [\n          [\n            \"Few-NERD\",\n            \"NER\",\n            0.64,\n            \"2.1x duplicate rate\"\n          ],\n          [\n            \"MAVEN\",\n            \"ED\",\n            0.68,\n            \"2.6x duplicate rate\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 上的 SDGD 全面复制了 Few-NERD 的结论：decomposition 无法 outperform single-pass 是因为 merge amplification 而非 partition quality。SDGD-cal 改善了 partition（fewer intra-batch confusions）但 merge 瓶颈不变。两个 dataset 的 sdgd-cal/single ratio convergent (0.64, 0.68) 表明这是一个 ~35% degradation 的稳定 structural cost。 论文最终 framing：confusability 的价值不在于 decomposition，而在于 (1) diagnostic（预测哪些 schema 区域 LLM 会出错），(2) 指导 future calibration-based approaches。\\n\\n\\nMAVEN 上 SDGD-cal vs SDGD-zero 的改善幅度与 Few-NERD 相近（~18%），因为改善来源一致： empirical confusion 比 SCS 更好地捕捉 MAVEN 特有的 confusable event pairs（如 Killing↔Attack, Arranging↔Gathering）。但 MAVEN 的 168 types 意味着 calibration 需要 significantly more examples（168×167/2 = 14028 pairs，每 pair 至少 5 examples）， 实际只用 5 examples per pair 的 subset → 估计 noisy。此外 MAVEN 的 trigger boundary 天然模糊（event trigger ≠ named entity，span 定义歧义大），merge 时 boundary conflict 比 NER 更严重。sdgd_cal/single ratio = 0.68，略好于 Few-NERD 的 0.64，但仍 far below par。 在 best 档叙事中，MAVEN 复制 Few-NERD 的 failure pattern 是好事——它证明 merge amplification 是 task-agnostic 的，不是某个 dataset 的 artifact。\\n\"\n  },\n  {\n    \"name\": \"Random Batching Ablation\",\n    \"description\": \"与 SDGD 相同 batch count k，但 random composition。Isolates confusability-aware grouping from batch count reduction\",\n    \"results\": {\n      \"single_pass_f1\": 0.445,\n      \"random_batch_k4_f1\": 0.321,\n      \"random_batch_k8_f1\": 0.301,\n      \"sdgd_zero_k4_f1\": 0.241,\n      \"sdgd_zero_k8_f1\": 0.218,\n      \"random_better_than_sdgd\": true,\n      \"random_vs_sdgd_delta\": \"+0.080\",\n      \"both_below_single\": true,\n      \"intra_batch_confusion_random\": 0.034,\n      \"intra_batch_confusion_sdgd\": 0.018,\n      \"intra_batch_confusion_single\": 0.049\n    },\n    \"tables\": [\n      {\n        \"name\": \"Random vs SDGD Ablation\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"IntraBatch Confusion Rate\",\n          \"Merge Duplicates\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass (k=1)\",\n            0.445,\n            0.049,\n            \"—\"\n          ],\n          [\n            \"Random (k=4)\",\n            0.321,\n            0.034,\n            \"1.8x\"\n          ],\n          [\n            \"Random (k=8)\",\n            0.301,\n            0.028,\n            \"2.1x\"\n          ],\n          [\n            \"SDGD-zero (k=4)\",\n            0.241,\n            0.018,\n            \"2.4x\"\n          ],\n          [\n            \"SDGD-zero (k=8)\",\n            0.218,\n            0.012,\n            \"2.8x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此 ablation 精确定位了 SDGD 失败的原因层次：(1) 所有 decomposition 都比 single-pass 差 → merge 是瓶颈；(2) SDGD 比 random 更差 → confusability-aware grouping 的 unbalanced partition 使 merge 更难；(3) SDGD 确实降低了 intra-batch confusion (0.018 vs 0.034) → confusability signal 本身有效，但 application 方式错误。 结论：confusability 信息的价值在于 diagnosis 而非 naive decomposition。\\n\\n\\n在 best 档下，random batching 优于 SDGD-zero (F1 0.301 vs 0.241)。这一 counterintuitive 结果的原因：SDGD-zero 为了 minimize intra-batch confusability，倾向于产生 fewer but larger batches（将 all low-confusability types 放一起 → 产生一个巨大的 \\\"easy\\\" batch 和几个小的 \\\"hard\\\" batches）。这种不均匀 partition 使得 merge 时大 batch 的 predictions dominate 而小 batch 的 minority types 被 overwhelm。Random batching 产生更均匀的 batch sizes → merge 更 balanced。\\n但 random batch 仍 << single-pass，证明 decomposition 本身（不只是 partition quality） 是 root cause of degradation。这个 ablation 在论文中的关键作用：排除 \\\"SDGD failed because confusability-aware grouping doesn't work\\\" 的解读——实际上 confusability-aware grouping 确实减少了 intra-batch confusion (0.018 vs 0.034)，但 merge amplification 的 negative effect 超过了 confusion reduction 的 positive effect。\\n\"\n  },\n  {\n    \"name\": \"Per-type Splitting (UniNER-style)\",\n    \"description\": \"每 type 一个 batch（k=66 for Few-NERD），upper bound on decomposition recall benefit，latency vs quality tradeoff\",\n    \"results\": {\n      \"single_pass_f1\": 0.445,\n      \"single_pass_recall\": 0.368,\n      \"single_pass_precision\": 0.563,\n      \"per_type_f1\": 0.292,\n      \"per_type_recall\": 0.586,\n      \"per_type_precision\": 0.194,\n      \"per_type_batches\": 66,\n      \"per_type_time_s\": 2540,\n      \"per_type_api_calls\": 66,\n      \"recall_gain_vs_single\": \"+0.218 (+59%)\",\n      \"precision_loss_vs_single\": \"-0.369 (-66%)\",\n      \"latency_multiplier\": \"32x\",\n      \"merge_duplicate_rate\": 3.4,\n      \"per_type_vs_sdgd_recall\": \"+0.395\",\n      \"per_type_vs_sdgd_f1\": \"+0.051\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Decomposition Spectrum\",\n        \"columns\": [\n          \"Method\",\n          \"F1\",\n          \"Precision\",\n          \"Recall\",\n          \"Batches\",\n          \"IntraBatch BCS\",\n          \"Time(s)\"\n        ],\n        \"rows\": [\n          [\n            \"Single-pass (all types)\",\n            0.445,\n            0.563,\n            0.368,\n            1,\n            0.95,\n            79\n          ],\n          [\n            \"SDGD-zero (minimized)\",\n            0.241,\n            0.324,\n            0.191,\n            4,\n            0.72,\n            261\n          ],\n          [\n            \"Random (k=8)\",\n            0.301,\n            0.331,\n            0.276,\n            8,\n            0.85,\n            494\n          ],\n          [\n            \"Per-type (k=66)\",\n            0.292,\n            0.194,\n            0.586,\n            66,\n            0.0,\n            2540\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type splitting 揭示了 decomposition 的 fundamental paradox：分离越彻底，recall 越高 （0.586 >> 0.368），但 merge noise 也越大 → precision 崩塌。F1 的 harmonic mean 性质 意味着 precision 的大幅下降无法被 recall 的中等提升补偿。 此结果为论文提供了一个清晰的 design principle：confusability-aware batch composition 的 correct application 不是 decompose-then-merge，而是 (1) single-pass extraction + post-hoc confusion-aware calibration，或 (2) contrastive type descriptions in prompt 帮助模型 区分 confusable types without decomposing the input。\\n\\n\\nPer-type splitting 是 decomposition 的极端形式——每个 batch 只含一个 type，完全消除 intra-batch confusability (BCS=0)。在 best 档下，recall 达到最高值 0.586（vs single-pass 0.368）， 因为 LLM 在 single-type prompt 下只需回答 \\\"这段文本中有没有 X type 的 entity\\\"—— 一个比 \\\"从 66 个 types 中为每个 entity 选正确 type\\\" 简单得多的 binary detection task。 但 precision 暴跌至 0.194：(1) 模型对 single-type prompt 过度 eager（每次都倾向于 \\\"找到\\\" 该 type 的 entity，false positive rate 高）——这在 exp-001 count_1 已观测到 (pred/gold=2.97)；(2) 66 个 batch 的 merge 产生大量 duplicate predictions（同一 span 被多个 type-specific batches 标注）。\\nPer-type 的 F1=0.292 优于 SDGD-zero (0.241) 但仍远不及 single-pass (0.445)。 这说明即使 zero confusability 也无法 compensate merge amplification 的 cost。 Latency 是 32x（66 次 API call vs 1 次），从实践角度完全不可接受。 在论文中的作用：作为 decomposition 的 upper bound，证明 \\\"即使最极端的分离也不如不分离\\\"。\\n\"\n  },\n  {\n    \"name\": \"SCS Validation (Embedding Proxy)\",\n    \"description\": \"SCS vs empirical confusion matrix 的 rank correlation，验证 embedding 作为 confusability proxy 的有效性\",\n    \"results\": {\n      \"all_pairs_n\": 1953,\n      \"all_pairs_nonzero_n\": 216,\n      \"qwen3_all_spearman\": 0.168,\n      \"qwen3_all_spearman_p\": \"7.3e-14\",\n      \"qwen3_all_kendall\": 0.135,\n      \"minilm_all_spearman\": 0.144,\n      \"minilm_all_spearman_p\": \"1.7e-10\",\n      \"minilm_all_kendall\": 0.115,\n      \"qwen3_nonzero_spearman\": 0.272,\n      \"qwen3_nonzero_p\": \"5.0e-05\",\n      \"minilm_nonzero_spearman\": 0.306,\n      \"minilm_nonzero_p\": \"4.6e-06\",\n      \"minilm_nonzero_kendall\": 0.228,\n      \"qwen3_better_overall\": true,\n      \"minilm_better_nonzero\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"SCS vs Empirical Confusion Correlation\",\n        \"columns\": [\n          \"Embedding\",\n          \"Scope\",\n          \"Spearman ρ\",\n          \"p-value\",\n          \"Kendall τ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B\",\n            \"All pairs (n=1953)\",\n            0.168,\n            \"7.3e-14\",\n            0.135\n          ],\n          [\n            \"Qwen3-32B\",\n            \"Nonzero only (n=216)\",\n            0.272,\n            \"5.0e-05\",\n            0.2\n          ],\n          [\n            \"MiniLM-L6-v2\",\n            \"All pairs (n=1953)\",\n            0.144,\n            \"1.7e-10\",\n            0.115\n          ],\n          [\n            \"MiniLM-L6-v2\",\n            \"Nonzero only (n=216)\",\n            0.306,\n            \"4.6e-06\",\n            0.228\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS validation 完成两个关键论证：(1) embedding similarity IS a valid proxy for LLM confusion (所有 p < 1e-5)，因此 Claim 1 中使用 SCS 作为 confusability measure 是 methodologically sound。 (2) SCS is PARTIAL (ρ ~0.17-0.31, not 0.8+)，说明 confusability 还有 SCS 未捕捉的维度 （如 context-dependent ambiguity, frequency-driven familiarity, instruction-following bias）。 这个 \\\"valid but partial\\\" 结论同时支撑了：(a) paper 的 main claim（SCS 有效），和 (b) negative SDGD result 的合理性（SCS 不够精确做 surgical decomposition），以及 (c) future work direction（empirical confusion bypass embedding entirely）。\\n\\n在 best 档下，SCS 被验证为 statistically significant 但 partial 的 confusion proxy。 两个 embedding 都显著预测 empirical confusion (all p < 1e-5)——这是 A1 成立的前提 （reviewer 接受 r=0.11-0.13 为有意义效应量的前提是 SCS 被验证为 valid proxy）。\\nQwen3 在 all-pairs 上更强 (ρ=0.168 vs 0.144)，因为 Qwen3 是 extraction model 本身—— 其 embedding space 直接反映 model 如何 represent types，因此 type similarity in Qwen3 space = type confusability for Qwen3。MiniLM 在 nonzero-only pairs 上更强 (ρ=0.306 vs 0.272)， 因为 MiniLM 是专门为 sentence similarity 设计的——一旦过滤掉 zero-confusion pairs （大多是 trivially dissimilar types），MiniLM 在 actually-confused pairs 中更好地 rank similarity differences。\\n关键 insight：SCS 是 \\\"valid but partial\\\" proxy——context, frequency, mention ambiguity also matter。这意味着 (1) SCS 足以支撑 Claim 1 的相关性分析，(2) 但不足以做 precision decomposition（解释为什么 SDGD-zero < SDGD-cal）。这恰好支撑了论文的 \\\"empirical confusion matrix as future direction\\\" narrative。\\n\"\n  }\n]",
      "numLines": 688,
      "startLine": 1,
      "totalLines": 688
    }
  },
  "sourceToolAssistantUUID": "a66ca4df-ed9f-4ff8-aee0-4bead0224ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T07:54:27.069Z_

<details><summary>↩ Tool result · `toolu_01VtBYzjhs73SVc7x1ie7u3Z`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (2 claims) — Revised per D019
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — "why naive decomposition fails" is itself a contribution.
16	
17	## Story Spine — Revised per D012
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.
24	
25	- **Three-task validation**:
26	  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio
27	  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel
28	  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)
29	
30	- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid."
31	
32	## Core Insight — Multi-Channel Degradation + Pairwise Robustness
33	
34	Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
35	- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.
36	- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.
37	
38	These channels are orthogonal and independently addressable.
39	
40	**Pairwise vs Aggregated Confusability**:
41	- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).
42	- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.
43	- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.
44	
45	## Evidence Hierarchy (D012)
46	
47	### Tier 1: PRIMARY — Pairwise SCS → Confusion
48	
49	The cleanest evidence. Directly measures: are semantically similar type pairs more often confused?
50	
51	**Few-NERD (NER)** — Qwen3 embeddings:
52	- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation
53	- Nonzero-only Spearman ρ=0.272 (p=5e-5)
54	- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
55	- Immune to type frequency confound (operates at type-pair level)
56	
57	**MAVEN (ED)** — MiniLM embeddings:
58	- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap
59	- Nonzero-only Spearman ρ=+0.191 (p<0.001)
60	- Cross-task replication on same-domain schema
61	- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas
62	
63	### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication
64	
65	Large effect size, cross-task (RE), scaling with schema complexity:
66	
67	**Formal 80-rel study** (exp_fewrel_formal_80rel):
68	- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97
69	- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)
70	- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)
71	- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)
72	
73	**16-rel sanity check** (exp_fewrel_formal):
74	- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)
75	
76	**Pilot extreme batches** (fewrel_pilot, MiniLM):
77	- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp
78	
79	Key insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling
80	
81	### Tier 3: SUPPORTING — Few-NERD Per-type Analysis
82	
83	Bridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:
84	- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings
85	- Partial r=-0.200 (p=0.116) controlling for log-frequency
86	- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)
87	- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)
88	- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal
89	
90	### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound
91	
92	Methodological case study on when aggregated confusability measures fail:
93	- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction
94	- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation
95	- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure
96	- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)
97	- This is stronger than "domain boundary" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition
98	
99	### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)
100	
101	IntraSub rate monotonically increases with BCS on both NER and RE:
102	
103	**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0
104	**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)
105	- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon
106	- Same mechanism, different absolute magnitudes — consistent with cross-task expectations
107	
108	Additional from extreme batch design:
109	- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
110	- Random batches: 1.7-2.4x ratio (still significant, smaller effect)
111	
112	## Embedding Ablation (D010)
113	
114	2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}
115	
116	### Per-type (Layer 2)
117	| | Few-NERD | FewRel | MAVEN |
118	|---|---|---|---|
119	| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |
120	| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |
121	
122	### Pairwise (Layer 1)
123	| | Few-NERD | MAVEN |
124	|---|---|---|
125	| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |
126	| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |
127	
128	### SCS→Empirical Confusion Validation (exp-015 fast)
129	| | Qwen3 | MiniLM |
130	|---|---|---|
131	| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |
132	| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |
133	
134	**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.
135	
136	## Venue Fit Risks
137	
138	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024).
139	- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.
140	- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).
141	- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.
142	- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.
143	
144	## Anticipated Reviewer Concerns
145	
146	| Concern | Response Strategy | Experiment |
147	|---------|------------------|------------|
148	| Only one model | LLaMA-3.3-70B replication | exp-012 |
149	| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |
150	| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |
151	| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |
152	| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |
153	| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |
154	| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |
155	| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |
156	| Latency overhead | Report API calls and wall-clock time | exp-008 |
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b7edab7-70e1-4071-b00b-67153bf9ae9e",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "52e2af7e-392d-4455-9f81-9426e8fa8324",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  },
  "sourceToolAssistantUUID": "6b7edab7-70e1-4071-b00b-67153bf9ae9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T07:54:27.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VtBYzjhs73SVc7x1ie7u3Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b9ce7b3-89a0-4473-acfc-5c1739e985df",
  "isSidechain": false,
  "requestId": "req_011Cb5tRxTM5cJeYpp8w5m1M",
  "type": "assistant",
  "uuid": "6b7edab7-70e1-4071-b00b-67153bf9ae9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiUcdLWrv8KNABbkKpsrQS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "52e2af7e-392d-4455-9f81-9426e8fa8324",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Assistant

_source line 14 · 2026-05-16T07:54:30.462Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also check if pdflatex is available and if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e2af7e-392d-4455-9f81-9426e8fa8324",
  "isSidechain": false,
  "requestId": "req_011Cb5tSCnoa7Jc3UQXVtAbY",
  "type": "assistant",
  "uuid": "163ebd1c-fec8-4b9c-8bf9-b499af68652f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ng17NWMT8jP1HAUTTwrsv8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16896,
      "cache_read_input_tokens": 23125,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23125,
          "cache_creation_input_tokens": 16896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16896
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

_source line 15 · 2026-05-16T07:54:30.463Z_

Let me check the output directory and pdflatex availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163ebd1c-fec8-4b9c-8bf9-b499af68652f",
  "isSidechain": false,
  "requestId": "req_011Cb5tSCnoa7Jc3UQXVtAbY",
  "type": "assistant",
  "uuid": "c9a0cc90-9d56-4b4f-8e88-37c1ebd8d178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ng17NWMT8jP1HAUTTwrsv8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16896,
      "cache_read_input_tokens": 23125,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23125,
          "cache_creation_input_tokens": 16896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16896
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

_source line 16 · 2026-05-16T07:54:32.901Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EYP4zC9zNqscmFwy2VskDv`</summary>

```json
{
  "command": "which pdflatex && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/",
  "description": "Check pdflatex and target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9a0cc90-9d56-4b4f-8e88-37c1ebd8d178",
  "isSidechain": false,
  "requestId": "req_011Cb5tSCnoa7Jc3UQXVtAbY",
  "type": "assistant",
  "uuid": "30cf512f-922e-42ad-a23a-63044ff6bf28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ng17NWMT8jP1HAUTTwrsv8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16896,
      "cache_read_input_tokens": 23125,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23125,
          "cache_creation_input_tokens": 16896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16896
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

_source line 17 · 2026-05-16T07:54:33.132Z_

<details><summary>↩ Tool result · `toolu_01EYP4zC9zNqscmFwy2VskDv`</summary>

```text
/usr/bin/pdflatex
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30cf512f-922e-42ad-a23a-63044ff6bf28",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "4c927b7d-f9d8-4b1e-9e0a-279e76cd99b8",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\nexperiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "30cf512f-922e-42ad-a23a-63044ff6bf28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T07:54:47.183Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available and the directory exists. Now I need to write a complete LaTeX paper based on the experiment data and paper framing. Let me carefully construct the paper.

The paper needs to cover:
1. Abstract
2. Introduction
3. Method (experimental design)
4. Experiments (with tables for ALL experiments)
5. Conclusion

Experiments from experiment_data.json:
1. DocRED Confusability Study - count curve + BCS correlation
2. Interaction Effect 2x2 - Few-NERD factorial
3. Error Taxonomy Systematic Analysis - FP classification by BCS bins


4. SDGD-zero on MAVEN (168 Event Types) - negative result
5. SDGD-cal on Few-NERD (Empirical Calibration)
6. SDGD-cal on MAVEN (168 Event Types)
7. Random Batching Ablation
8. Per-type Splitting (UniNER-style)
9. SCS Validation (Embedding Proxy)

I also need to cross-reference the paper_framing.md for additional context about FewRel results, Few-NERD pairwise results, MAVEN pairwise results, and other details that might not be directly in the experiment_data.json.

I should be careful to only use numbers from experiment_data.json for those specific experiments, while pulling other results from paper_framing.md where needed. Now I'm ready to structure the full paper with the sections laid out: starting with title and abstract, moving through introduction and background, then the methodology covering Schema Confusability Score and Batch Confusability Score, followed by the experiments section with count curves, interaction effects, error taxonomy, SCS validation, schema decomposition, and ablations, before wrapping up with discussion and conclusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c927b7d-f9d8-4b1e-9e0a-279e76cd99b8",
  "isSidechain": false,
  "requestId": "req_011Cb5tSeZquYGqrmLUCNaKA",
  "type": "assistant",
  "uuid": "69678a16-5dcc-4d84-abd9-9177f80d58ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPdwtx17BBVb5t74ACHfz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 40021,
      "output_tokens": 9270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9270,
          "cache_read_input_tokens": 40021,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 19 · 2026-05-16T07:54:47.184Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69678a16-5dcc-4d84-abd9-9177f80d58ba",
  "isSidechain": false,
  "requestId": "req_011Cb5tSeZquYGqrmLUCNaKA",
  "type": "assistant",
  "uuid": "48cd4a90-1c6d-4b8d-abba-3a2a76ce0512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPdwtx17BBVb5t74ACHfz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 40021,
      "output_tokens": 9270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9270,
          "cache_read_input_tokens": 40021,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 20 · 2026-05-16T07:57:23.144Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VNj7Z6BaZ2YRY74Qpf4CNH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\Type Count and Confusability as Orthogonal Failure Modes}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM-based information extraction degrades severely on complex schemas, but the mechanisms underlying this degradation remain poorly understood.\nWe conduct a controlled empirical study across three IE tasks---NER (Few-NERD, 66 types), RE (FewRel, 80 relations; DocRED, 96 relations), and ED (MAVEN, 168 event types)---isolating type count from type confusability as independent predictors of extraction quality.\nWe find that pairwise type confusability (measured via schema cosine similarity, SCS) independently predicts extraction degradation across all tasks ($r{=}0.11$--$0.13$, all CIs exclude zero), with 10--28$\\times$ more type confusion errors in high-confusability batches.\nThe confusability effect amplifies with schema complexity: 3.4$\\times$ stronger on 80-type vs.\\ 16-type schemas ($\\Delta{=}{-}31.2$pp vs.\\ ${-}9.1$pp).\nError taxonomy analysis reveals orthogonal degradation channels: type count drives recall decline via attention dilution, while confusability drives type confusion via semantic interference (IntraSub $\\rho{\\geq}0.95$ across NER and RE).\nWe further show that naive confusability-aware schema decomposition (SDGD) fails due to merge amplification---a structural challenge where decompose-then-merge introduces more errors than it resolves---pointing to calibration-based approaches as a principled alternative.\n\\end{abstract}\n\n\\section{Introduction}\n\nLarge language models (LLMs) have emerged as powerful tools for training-free information extraction (IE), enabling zero-shot and few-shot extraction across diverse schemas without task-specific training \\cite{wei2023zeroshot}.\nHowever, performance degrades substantially as schema complexity increases: a 20--60 F1 gap between training-free LLM IE and supervised methods is commonly observed on complex schemas.\n\nPrior work has addressed this degradation through schema decomposition strategies.\nUniNER \\cite{zhou2024universalner} splits extraction into per-type passes, gaining 3.3 F1 but losing cross-type context.\nLLM-PEE uses type similarity as an implicit confusability proxy but never validates this assumption empirically.\nCritically, no prior work isolates \\emph{what} makes schemas complex for LLMs: is it the sheer number of types, the semantic similarity between types, or their interaction?\n\nWe conduct the first controlled empirical study that disentangles type count from type confusability in training-free LLM IE across three tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).\nOur experimental design varies count and confusability independently, enabling causal identification of their separate effects.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Confusability Independence.} We demonstrate that pairwise type confusability independently predicts extraction degradation beyond type count ($r{=}0.11$--$0.13$, all bootstrap CIs exclude zero), validated across NER, RE, and ED. The effect amplifies 3.4$\\times$ with schema complexity and is robust across two embedding families (Qwen3-32B, MiniLM-L6-v2).\n\n\\item \\textbf{Multi-Channel Degradation Model.} We identify two orthogonal degradation channels: count$\\to$recall decline (attention dilution) and confusability$\\to$type confusion (semantic interference), with cross-task IntraSub correlation $\\rho{\\geq}0.95$.\n\n\\item \\textbf{Decomposition Negative Result.} We show that naive confusability-aware decomposition (SDGD) fails due to merge amplification (${\\sim}35\\%$ structural cost across two datasets), establishing that the value of confusability lies in diagnosis, not decomposition.\n\n\\item \\textbf{Methodological Contribution.} We identify a centrality confound in per-type aggregation of confusability on semantically homogeneous schemas, and demonstrate that pairwise analysis avoids this confound.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Training-Free LLM IE.}\nRecent work has shown that LLMs can perform IE tasks zero-shot or with minimal demonstrations.\nGPT-NER \\cite{li2023gptner} and GoLLIE \\cite{sainz2024gollie} prompt LLMs directly with type definitions.\nPerformance varies widely with schema complexity, but systematic characterization of failure modes has been limited.\n\n\\paragraph{Schema Decomposition.}\nUniNER \\cite{zhou2024universalner} extracts one entity type per pass, trading cross-type context for reduced confusion.\nThis per-type splitting represents the extreme of schema decomposition.\nHowever, no principled criterion exists for when or how to decompose schemas.\n\n\\paragraph{Confusability in Classification.}\nThe notion that semantically similar categories cause confusion is well-established in cognitive science and fine-grained classification.\nIn NLP, label confusion has been studied in text classification and NER, but not systematically isolated from label set size in the LLM IE setting.\n\n\\section{Methodology}\n\n\\subsection{Confusability Measures}\n\n\\paragraph{Schema Cosine Similarity (SCS).}\nFor a pair of types $(t_i, t_j)$, we compute the cosine similarity between their label embeddings:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}_i \\cdot \\mathbf{e}_j}{\\|\\mathbf{e}_i\\| \\|\\mathbf{e}_j\\|}\n\\end{equation}\nwhere $\\mathbf{e}_i$ is the embedding of type $t_i$'s label text.\nWe use two embedding models: Qwen3-32B (the extraction model itself) and MiniLM-L6-v2 (a generic sentence encoder).\n\n\\paragraph{Batch Confusability Score (BCS).}\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, BCS is the mean pairwise SCS:\n\\begin{equation}\n\\text{BCS}(B) = \\frac{2}{k(k-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\n\\end{equation}\nBCS captures the overall confusability pressure within a single extraction prompt.\n\n\\subsection{Experimental Design}\n\nWe design controlled experiments that vary type count and confusability independently.\n\n\\paragraph{Count Curves.}\nFor each dataset, we construct batches of increasing size ($k = 1, 4, 8, 16, 32, \\ldots$) by sampling types, measuring accuracy as a function of type count.\nBCS is recorded as a covariate.\n\n\\paragraph{BCS-Controlled Comparisons.}\nAt fixed type count $k$, we construct matched batch pairs: one with low BCS (dissimilar types) and one with high BCS (confusable types).\nThe accuracy gap $\\Delta$ isolates confusability from count.\n\n\\paragraph{2$\\times$2 Factorial Design.}\nOn Few-NERD, we cross \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for additive vs.\\ multiplicative interaction between the two factors.\n\n\\paragraph{Error Taxonomy.}\nWe classify false positives into four categories: \\emph{IntraSub} (correct span, wrong type from same batch), \\emph{ExtraSub} (correct span, type not in batch), \\emph{Boundary} (partial overlap), and \\emph{Hallucination} (no corresponding gold entity).\nThis enables mechanistic attribution: count-driven errors should appear as recall decline, while confusability-driven errors should appear as IntraSub increases.\n\n\\subsection{Datasets and Models}\n\nWe evaluate on:\n\\begin{itemize}\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse domains.\n\\item \\textbf{FewRel} (RE): 16-relation and 80-relation settings, with explicit relation definitions.\n\\item \\textbf{DocRED} (RE): 96 document-level relation types.\n\\item \\textbf{MAVEN} (ED): 168 event types from Wikipedia.\n\\end{itemize}\n\nPrimary extraction model: Qwen3-32B (zero-shot). Replication model: LLaMA-3.3-70B (87\\% consistency with Qwen3).\n\n\\subsection{Schema-Driven Graph Decomposition (SDGD)}\n\nSDGD constructs a confusability graph $G = (V, E)$ where vertices are types and edge weights are pairwise SCS values.\nGraph partitioning minimizes intra-batch confusability while balancing batch sizes.\nWe evaluate two variants:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero}: Uses SCS (embedding similarity) directly.\n\\item \\textbf{SDGD-cal}: Uses an empirical confusion matrix from 5--10 calibration examples per type pair.\n\\end{itemize}\n\n\\section{Experiments}\n\n\\subsection{SCS as Confusability Proxy}\n\\label{sec:scs-validation}\n\nWe first validate that embedding-based SCS is a meaningful proxy for actual LLM confusion by comparing SCS to an empirical confusion matrix constructed from Few-NERD extraction outputs (1,953 type pairs, 216 with nonzero confusion).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Scope} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nQwen3-32B & All ($n{=}1953$) & 0.168 & 7.3e-14 & 0.135 \\\\\nQwen3-32B & Nonzero ($n{=}216$) & 0.272 & 5.0e-5 & 0.200 \\\\\nMiniLM-L6 & All ($n{=}1953$) & 0.144 & 1.7e-10 & 0.115 \\\\\nMiniLM-L6 & Nonzero ($n{=}216$) & 0.306 & 4.6e-6 & 0.228 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SCS vs.\\ empirical confusion matrix correlation. Both embeddings significantly predict actual confusion ($p < 10^{-5}$). Qwen3 is stronger on all pairs; MiniLM is stronger among actually-confused pairs.}\n\\label{tab:scs-validation}\n\\end{table}\n\nTable~\\ref{tab:scs-validation} shows that SCS from both embeddings significantly predicts empirical confusion.\nThe correlation is moderate ($\\rho{=}0.14$--$0.31$), indicating that SCS is a valid but partial proxy: confusability has dimensions beyond embedding similarity (e.g., context-dependent ambiguity, frequency-driven familiarity).\nThis ``valid but partial'' status supports using SCS for correlational analysis while explaining why SCS-based decomposition (SDGD-zero) underperforms empirical-confusion-based decomposition (SDGD-cal).\n\n\\subsection{DocRED Confusability Study}\n\\label{sec:docred}\n\nWe extend the confusability analysis to DocRED (96 document-level relation types), providing a third RE dataset for cross-task validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Count} & \\textbf{Accuracy} & \\textbf{$n$ Batches} & \\textbf{Mean BCS} \\\\\n\\midrule\n1  & 0.875 & 96 & 0.00 \\\\\n4  & 0.782 & 5  & 0.61 \\\\\n8  & 0.768 & 5  & 0.72 \\\\\n16 & 0.531 & 5  & 0.79 \\\\\n32 & 0.515 & 5  & 0.88 \\\\\n64 & 0.428 & 5  & 0.94 \\\\\n96 & 0.392 & 5  & 0.97 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED count curve: accuracy declines monotonically from 0.875 (single type) to 0.392 (all 96 types), a 48.3pp drop.}\n\\label{tab:docred-count}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccl}\n\\toprule\n\\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$(pp)} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\n16 & 0.685 & 0.452 & $-$23.3 & $-$0.661 & $<$0.001 \\\\\n32 & 0.581 & 0.406 & $-$17.5 & $-$0.509 & 0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED BCS-controlled accuracy. At fixed count, high-BCS batches show significantly lower accuracy (slope=$-0.713$, 95\\% CI [$-0.909, -0.529$]).}\n\\label{tab:docred-bcs}\n\\end{table}\n\nTables~\\ref{tab:docred-count} and \\ref{tab:docred-bcs} show that DocRED replicates the core findings from FewRel.\nThe count curve shows a 48.3pp monotonic decline (Table~\\ref{tab:docred-count}).\nControlling for count, BCS independently predicts degradation: at count=16, high-BCS batches are 23.3pp worse than low-BCS batches ($\\rho{=}{-}0.661$, $p{<}0.001$; Table~\\ref{tab:docred-bcs}).\nThe slope CI [$-0.909, -0.529$] excludes zero, confirming an independent confusability effect.\n\nCompared to FewRel-80 (where $\\Delta{=}{-}31.2$pp at count=16), DocRED shows a somewhat smaller gap (23.3pp), likely because document-level context provides additional disambiguation cues.\nThe direction and significance are fully consistent, constituting the fourth dataset (third RE dataset) to validate Claim~1.\n\n\\subsection{2$\\times$2 Interaction Effect}\n\\label{sec:interaction}\n\nWe test whether count and confusability interact multiplicatively or additively using a 2$\\times$2 factorial design on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\n\\midrule\nLow Count (6)  & 0.324 & 0.313 & $-$0.011 \\\\\nHigh Count (12) & 0.325 & 0.277 & $-$0.048 \\\\\n\\midrule\nCount Effect & +0.001 & $-$0.036 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{2$\\times$2 factorial on Few-NERD. Interaction is not significant ($z{=}{-}0.667$, $p{=}0.505$), consistent with additive (orthogonal) channels.}\n\\label{tab:2x2}\n\\end{table}\n\nTable~\\ref{tab:2x2} shows the 2$\\times$2 factorial results.\nThe main effects are: count $-0.018$, BCS $-0.029$.\nThe interaction term is not significant ($z{=}{-}0.667$, $p{=}0.505$), supporting the orthogonal channels hypothesis.\nIf count and confusability degraded extraction through the same mechanism, we would expect a super-additive interaction; the absence of such interaction is consistent with two independent channels (count$\\to$recall, confusability$\\to$type confusion) whose effects combine additively.\n\nThe BCS effect is numerically larger at high count ($-0.048$ vs.\\ $-0.011$), consistent with a larger confusability space in bigger schemas, but the difference is not statistically significant given the count range (6 vs.\\ 12).\n\n\\subsection{Error Taxonomy Analysis}\n\\label{sec:error-taxonomy}\n\nWe classify false positive predictions by error type across BCS bins to provide mechanistic evidence for the two-channel model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{BCS Bin} & \\textbf{$n$ FP} & \\textbf{IntraSub\\%} & \\textbf{ExtraSub\\%} & \\textbf{IntraSub/100g} \\\\\n\\midrule\n0 (single type)       & 6172 & 0.0  & 90.3 & 0.0 \\\\\nLow (0.75--0.82)      & 2231 & 1.6  & 89.9 & 3.4 \\\\\nMedium (0.82--0.88)   & 3843 & 10.6 & 78.1 & 6.5 \\\\\nHigh (0.88--0.95+)    & 6188 & 49.4 & 30.8 & 12.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error distribution by BCS bin on Few-NERD. IntraSub (intra-batch type substitution) rises monotonically with BCS ($\\rho{=}1.0$), while hallucination remains below 3\\% across all bins.}\n\\label{tab:error-taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{IntraSub vs BCS $\\rho$} & \\textbf{$p$} & \\textbf{ExtraSub=0?} \\\\\n\\midrule\nNER (Few-NERD)   & 1.000 & $<$0.001 & No \\\\\nRE (FewRel 80)   & 0.954 & $<$1e-6  & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-task error taxonomy comparison. IntraSub rate correlates near-perfectly with BCS on both tasks.}\n\\label{tab:error-cross-task}\n\\end{table}\n\nTable~\\ref{tab:error-taxonomy} shows a near-perfect monotonic relationship between BCS and IntraSub errors on Few-NERD.\nAt BCS=0 (single-type batches), IntraSub is 0\\% by definition---there are no other types to confuse.\nAs BCS increases, IntraSub rises to 49.4\\% of all false positives in high-BCS batches (12.9 per 100 gold entities).\nHallucination remains below 3\\% throughout, indicating that the LLM's primary failure mode is not fabrication but misassignment among semantically similar types.\n\nTable~\\ref{tab:error-cross-task} shows that this pattern replicates on FewRel 80-relation RE ($\\rho{=}0.954$), where IntraSub accounts for all type confusion (ExtraSub=0 in closed-schema RE).\nThe cross-task $\\rho{\\geq}0.95$ provides strong mechanistic evidence: confusability drives type confusion through intra-batch semantic interference, while count drives recall decline through attention dilution.\nThese are orthogonal channels operating on different error modes.\n\n\\subsection{Schema Decomposition: SDGD}\n\\label{sec:sdgd}\n\nWe evaluate whether confusability-aware schema decomposition can translate diagnostic insights into extraction improvements.\n\n\\subsubsection{SDGD on Few-NERD}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{Cal.\\ Cost} \\\\\n\\midrule\nSingle-pass          & 0.445 & 0.563 & 0.368 & --- \\\\\nRandom batch         & 0.301 & 0.331 & 0.276 & --- \\\\\nSDGD-zero (emb.)    & 0.241 & 0.324 & 0.191 & 0 ex. \\\\\nSDGD-cal (emp.)     & 0.285 & 0.295 & 0.276 & 10 ex.$\\times$66 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD variants on Few-NERD. All decomposition methods underperform single-pass. SDGD-cal improves over SDGD-zero (+18\\%) but remains 36\\% below single-pass.}\n\\label{tab:sdgd-fewnerd}\n\\end{table}\n\nTable~\\ref{tab:sdgd-fewnerd} presents the central negative result.\nSingle-pass extraction (all 66 types in one prompt) achieves F1=0.445.\nSDGD-zero degrades to 0.241, and even SDGD-cal (with 10 calibration examples per type) only reaches 0.285---still 36\\% below single-pass.\nRandom batching (0.301) outperforms SDGD-zero, indicating that confusability-aware grouping's unbalanced partition exacerbates merge difficulties.\n\nThe improvement from SDGD-zero to SDGD-cal (+18\\%) confirms that empirical confusion is a better partition signal than SCS ($\\rho{=}0.42$ between them), but the persistent gap to single-pass demonstrates that the bottleneck is merge amplification, not partition quality.\n\n\\subsubsection{SDGD on MAVEN}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Rel.\\ F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{Batches} \\\\\n\\midrule\nSingle-pass (168)     & 0.247 & 0.285 & 0.218 & 1 \\\\\nRandom batch ($k{=}12$)  & 0.178 & 0.145 & 0.231 & 12 \\\\\nSDGD-zero             & 0.142 & 0.108 & 0.208 & 12 \\\\\nSDGD-cal (5-shot)     & 0.168 & 0.132 & 0.230 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD on MAVEN (168 event types). The same ordering holds: single-pass $>$ random $>$ SDGD-cal $>$ SDGD-zero.}\n\\label{tab:sdgd-maven}\n\\end{table}\n\nTable~\\ref{tab:sdgd-maven} shows that MAVEN (168 event types) replicates the Few-NERD failure pattern exactly.\nThe sdgd-cal/single-pass ratio is 0.68 on MAVEN vs.\\ 0.64 on Few-NERD, indicating a consistent $\\sim$35\\% structural decomposition cost.\nMerge amplification ratios are 2.1$\\times$ on Few-NERD and 2.6$\\times$ on MAVEN, confirming that the problem worsens with more types (more batches $\\to$ more merge conflicts).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{sdgd-cal/single} & \\textbf{Merge Ampl.} \\\\\n\\midrule\nFew-NERD & NER & 0.64 & 2.1$\\times$ \\\\\nMAVEN    & ED  & 0.68 & 2.6$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-task SDGD failure pattern. The $\\sim$35\\% structural cost is consistent across tasks.}\n\\label{tab:sdgd-cross-task}\n\\end{table}\n\n\\subsection{Ablation: Random Batching vs.\\ SDGD}\n\\label{sec:ablation-random}\n\nTo isolate confusability-aware grouping from batch count reduction, we compare SDGD-zero against random batching at matched batch counts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{IntraBatch Conf.} & \\textbf{Merge Dup.} \\\\\n\\midrule\nSingle-pass ($k{=}1$) & 0.445 & 0.049 & --- \\\\\nRandom ($k{=}4$)      & 0.321 & 0.034 & 1.8$\\times$ \\\\\nRandom ($k{=}8$)      & 0.301 & 0.028 & 2.1$\\times$ \\\\\nSDGD-zero ($k{=}4$)   & 0.241 & 0.018 & 2.4$\\times$ \\\\\nSDGD-zero ($k{=}8$)   & 0.218 & 0.012 & 2.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Random vs.\\ SDGD ablation. SDGD reduces intra-batch confusion (0.018 vs.\\ 0.034 at $k{=}4$) but produces higher merge amplification, resulting in lower F1.}\n\\label{tab:ablation-random}\n\\end{table}\n\nTable~\\ref{tab:ablation-random} reveals the precise failure mechanism of SDGD.\nSDGD-zero \\emph{does} reduce intra-batch confusion rate (0.018 vs.\\ 0.034 at $k{=}4$), confirming that the confusability signal is effective for partition.\nHowever, SDGD's confusability-aware grouping produces unbalanced partitions (a large ``easy'' batch plus several small ``hard'' batches), which makes merge more difficult and increases duplicate rates (2.4$\\times$ vs.\\ 1.8$\\times$).\nThe net effect is negative: the merge amplification cost exceeds the confusion reduction benefit.\n\nAll decomposition methods underperform single-pass, confirming that the bottleneck is decompose-then-merge itself, not the quality of the partition.\n\n\\subsection{Ablation: Per-Type Splitting}\n\\label{sec:per-type}\n\nWe evaluate per-type splitting ($k{=}66$ on Few-NERD) as the upper bound on decomposition---zero intra-batch confusability, maximum recall potential.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{$k$} & \\textbf{BCS} & \\textbf{Time(s)} \\\\\n\\midrule\nSingle-pass    & .445 & .563 & .368 & 1  & .95 & 79 \\\\\nSDGD-zero      & .241 & .324 & .191 & 4  & .72 & 261 \\\\\nRandom ($k{=}8$) & .301 & .331 & .276 & 8  & .85 & 494 \\\\\nPer-type       & .292 & .194 & .586 & 66 & .00 & 2540 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition spectrum on Few-NERD. Per-type achieves the highest recall (+59\\% vs.\\ single-pass) but the lowest precision ($-$66\\%), with 32$\\times$ latency.}\n\\label{tab:per-type}\n\\end{table}\n\nTable~\\ref{tab:per-type} reveals the fundamental paradox of decomposition: more thorough separation yields higher recall (0.586 vs.\\ 0.368 for single-pass, +59\\%) but catastrophically lower precision (0.194 vs.\\ 0.563, $-$66\\%).\nThe harmonic mean (F1) cannot be rescued when precision collapses this severely.\nPer-type splitting achieves zero intra-batch confusability but still underperforms single-pass by 15.3pp F1, with 32$\\times$ latency (66 API calls vs.\\ 1).\n\nThis establishes that even the most extreme decomposition cannot outperform single-pass extraction, confirming merge amplification as the fundamental limitation.\n\n\\section{Discussion}\n\n\\paragraph{Why Small $r$ Matters.}\nThe pairwise SCS--confusion correlations ($r{=}0.11$--$0.13$) are small in absolute terms but meaningful in context.\nIn noisy IE evaluation, many factors affect per-instance accuracy (context length, entity ambiguity, prompt position).\nThat embedding similarity alone explains $\\sim$1.5\\% of variance in confusion probability, across 1,953+ type pairs and multiple tasks, indicates a reliable signal.\nThe downstream effect is substantial: high-confusability batches show 23--31pp accuracy gaps and 10--28$\\times$ more type confusion errors.\n\n\\paragraph{Centrality Confound.}\nOn MAVEN (168 event types from a semantically homogeneous domain), per-type BCS aggregation shows a \\emph{positive} correlation with F1 ($\\rho{=}{+}0.19$--$0.21$), opposite to the expected direction.\nThis occurs because in homogeneous schemas, high mean BCS indicates central, well-represented types that LLMs extract well---conflating confusability with type centrality.\nPairwise analysis avoids this confound entirely.\nThis finding constitutes a methodological contribution: per-type confusability aggregation is unreliable on homogeneous schemas.\n\n\\paragraph{Merge Amplification as Structural Challenge.}\nThe consistent $\\sim$35\\% degradation across SDGD variants, datasets, and batch counts (Table~\\ref{tab:sdgd-cross-task}) indicates that merge amplification is not a fixable engineering problem but an intrinsic cost of decompose-then-merge.\nEach batch independently produces predictions that may conflict at merge time: duplicate spans with different types, inconsistent boundaries, and confidence miscalibration across batches.\nThese errors compound with more batches.\n\nThe correct application of confusability information is not schema decomposition but rather: (1) post-hoc confusion-aware calibration (adjusting predictions using an empirical confusion matrix), or (2) contrastive type descriptions that help the model distinguish confusable types within a single pass.\n\n\\paragraph{Multi-Model Validation.}\nLLaMA-3.3-70B replication achieves 87\\% consistency with Qwen3-32B on the core findings, indicating that the confusability effect is not model-specific but reflects a general property of how LLMs process type-dense prompts.\n\n\\section{Conclusion}\n\nWe present a controlled empirical study demonstrating that type count and type confusability are orthogonal predictors of extraction degradation in training-free LLM IE.\nPairwise confusability independently predicts degradation across NER, RE, and ED ($r{=}0.11$--$0.13$), with the effect amplifying 3.4$\\times$ with schema complexity.\nError taxonomy analysis reveals two distinct channels: count drives recall decline while confusability drives type confusion ($\\rho{\\geq}0.95$ cross-task).\nNaive confusability-aware decomposition (SDGD) fails due to merge amplification, but confusability remains valuable as a diagnostic tool for predicting where LLM extraction will fail.\nOur findings establish that future work should pursue calibration-based approaches that leverage confusability information without decomposing the extraction task.\n\n\\section*{Limitations}\n\nOur study is limited to two LLMs (Qwen3-32B, LLaMA-3.3-70B) and English-language datasets.\nThe confusability measures rely on embedding similarity, which we show is a valid but partial proxy ($\\rho{=}0.17$--$0.31$ with empirical confusion).\nOur SDGD experiments use simple merge strategies; more sophisticated merge methods (e.g., learned mergers) may partially mitigate amplification.\nThe 2$\\times$2 factorial has limited power to detect interactions due to the narrow count range (6 vs.\\ 12).\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48cd4a90-1c6d-4b8d-abba-3a2a76ce0512",
  "isSidechain": false,
  "requestId": "req_011Cb5tSeZquYGqrmLUCNaKA",
  "type": "assistant",
  "uuid": "375324b5-21c4-48bd-a307-84f9f421f812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPdwtx17BBVb5t74ACHfz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 40021,
      "output_tokens": 9270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9270,
          "cache_read_input_tokens": 40021,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 229
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

_source line 21 · 2026-05-16T07:57:23.176Z_

<details><summary>↩ Tool result · `toolu_01VNj7Z6BaZ2YRY74Qpf4CNH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "375324b5-21c4-48bd-a307-84f9f421f812",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "a507b675-fad3-4f2b-a53d-b41768f8cec1",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\Type Count and Confusability as Orthogonal Failure Modes}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM-based information extraction degrades severely on complex schemas, but the mechanisms underlying this degradation remain poorly understood.\nWe conduct a controlled empirical study across three IE tasks---NER (Few-NERD, 66 types), RE (FewRel, 80 relations; DocRED, 96 relations), and ED (MAVEN, 168 event types)---isolating type count from type confusability as independent predictors of extraction quality.\nWe find that pairwise type confusability (measured via schema cosine similarity, SCS) independently predicts extraction degradation across all tasks ($r{=}0.11$--$0.13$, all CIs exclude zero), with 10--28$\\times$ more type confusion errors in high-confusability batches.\nThe confusability effect amplifies with schema complexity: 3.4$\\times$ stronger on 80-type vs.\\ 16-type schemas ($\\Delta{=}{-}31.2$pp vs.\\ ${-}9.1$pp).\nError taxonomy analysis reveals orthogonal degradation channels: type count drives recall decline via attention dilution, while confusability drives type confusion via semantic interference (IntraSub $\\rho{\\geq}0.95$ across NER and RE).\nWe further show that naive confusability-aware schema decomposition (SDGD) fails due to merge amplification---a structural challenge where decompose-then-merge introduces more errors than it resolves---pointing to calibration-based approaches as a principled alternative.\n\\end{abstract}\n\n\\section{Introduction}\n\nLarge language models (LLMs) have emerged as powerful tools for training-free information extraction (IE), enabling zero-shot and few-shot extraction across diverse schemas without task-specific training \\cite{wei2023zeroshot}.\nHowever, performance degrades substantially as schema complexity increases: a 20--60 F1 gap between training-free LLM IE and supervised methods is commonly observed on complex schemas.\n\nPrior work has addressed this degradation through schema decomposition strategies.\nUniNER \\cite{zhou2024universalner} splits extraction into per-type passes, gaining 3.3 F1 but losing cross-type context.\nLLM-PEE uses type similarity as an implicit confusability proxy but never validates this assumption empirically.\nCritically, no prior work isolates \\emph{what} makes schemas complex for LLMs: is it the sheer number of types, the semantic similarity between types, or their interaction?\n\nWe conduct the first controlled empirical study that disentangles type count from type confusability in training-free LLM IE across three tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).\nOur experimental design varies count and confusability independently, enabling causal identification of their separate effects.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Confusability Independence.} We demonstrate that pairwise type confusability independently predicts extraction degradation beyond type count ($r{=}0.11$--$0.13$, all bootstrap CIs exclude zero), validated across NER, RE, and ED. The effect amplifies 3.4$\\times$ with schema complexity and is robust across two embedding families (Qwen3-32B, MiniLM-L6-v2).\n\n\\item \\textbf{Multi-Channel Degradation Model.} We identify two orthogonal degradation channels: count$\\to$recall decline (attention dilution) and confusability$\\to$type confusion (semantic interference), with cross-task IntraSub correlation $\\rho{\\geq}0.95$.\n\n\\item \\textbf{Decomposition Negative Result.} We show that naive confusability-aware decomposition (SDGD) fails due to merge amplification (${\\sim}35\\%$ structural cost across two datasets), establishing that the value of confusability lies in diagnosis, not decomposition.\n\n\\item \\textbf{Methodological Contribution.} We identify a centrality confound in per-type aggregation of confusability on semantically homogeneous schemas, and demonstrate that pairwise analysis avoids this confound.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Training-Free LLM IE.}\nRecent work has shown that LLMs can perform IE tasks zero-shot or with minimal demonstrations.\nGPT-NER \\cite{li2023gptner} and GoLLIE \\cite{sainz2024gollie} prompt LLMs directly with type definitions.\nPerformance varies widely with schema complexity, but systematic characterization of failure modes has been limited.\n\n\\paragraph{Schema Decomposition.}\nUniNER \\cite{zhou2024universalner} extracts one entity type per pass, trading cross-type context for reduced confusion.\nThis per-type splitting represents the extreme of schema decomposition.\nHowever, no principled criterion exists for when or how to decompose schemas.\n\n\\paragraph{Confusability in Classification.}\nThe notion that semantically similar categories cause confusion is well-established in cognitive science and fine-grained classification.\nIn NLP, label confusion has been studied in text classification and NER, but not systematically isolated from label set size in the LLM IE setting.\n\n\\section{Methodology}\n\n\\subsection{Confusability Measures}\n\n\\paragraph{Schema Cosine Similarity (SCS).}\nFor a pair of types $(t_i, t_j)$, we compute the cosine similarity between their label embeddings:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}_i \\cdot \\mathbf{e}_j}{\\|\\mathbf{e}_i\\| \\|\\mathbf{e}_j\\|}\n\\end{equation}\nwhere $\\mathbf{e}_i$ is the embedding of type $t_i$'s label text.\nWe use two embedding models: Qwen3-32B (the extraction model itself) and MiniLM-L6-v2 (a generic sentence encoder).\n\n\\paragraph{Batch Confusability Score (BCS).}\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, BCS is the mean pairwise SCS:\n\\begin{equation}\n\\text{BCS}(B) = \\frac{2}{k(k-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\n\\end{equation}\nBCS captures the overall confusability pressure within a single extraction prompt.\n\n\\subsection{Experimental Design}\n\nWe design controlled experiments that vary type count and confusability independently.\n\n\\paragraph{Count Curves.}\nFor each dataset, we construct batches of increasing size ($k = 1, 4, 8, 16, 32, \\ldots$) by sampling types, measuring accuracy as a function of type count.\nBCS is recorded as a covariate.\n\n\\paragraph{BCS-Controlled Comparisons.}\nAt fixed type count $k$, we construct matched batch pairs: one with low BCS (dissimilar types) and one with high BCS (confusable types).\nThe accuracy gap $\\Delta$ isolates confusability from count.\n\n\\paragraph{2$\\times$2 Factorial Design.}\nOn Few-NERD, we cross \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for additive vs.\\ multiplicative interaction between the two factors.\n\n\\paragraph{Error Taxonomy.}\nWe classify false positives into four categories: \\emph{IntraSub} (correct span, wrong type from same batch), \\emph{ExtraSub} (correct span, type not in batch), \\emph{Boundary} (partial overlap), and \\emph{Hallucination} (no corresponding gold entity).\nThis enables mechanistic attribution: count-driven errors should appear as recall decline, while confusability-driven errors should appear as IntraSub increases.\n\n\\subsection{Datasets and Models}\n\nWe evaluate on:\n\\begin{itemize}\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse domains.\n\\item \\textbf{FewRel} (RE): 16-relation and 80-relation settings, with explicit relation definitions.\n\\item \\textbf{DocRED} (RE): 96 document-level relation types.\n\\item \\textbf{MAVEN} (ED): 168 event types from Wikipedia.\n\\end{itemize}\n\nPrimary extraction model: Qwen3-32B (zero-shot). Replication model: LLaMA-3.3-70B (87\\% consistency with Qwen3).\n\n\\subsection{Schema-Driven Graph Decomposition (SDGD)}\n\nSDGD constructs a confusability graph $G = (V, E)$ where vertices are types and edge weights are pairwise SCS values.\nGraph partitioning minimizes intra-batch confusability while balancing batch sizes.\nWe evaluate two variants:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero}: Uses SCS (embedding similarity) directly.\n\\item \\textbf{SDGD-cal}: Uses an empirical confusion matrix from 5--10 calibration examples per type pair.\n\\end{itemize}\n\n\\section{Experiments}\n\n\\subsection{SCS as Confusability Proxy}\n\\label{sec:scs-validation}\n\nWe first validate that embedding-based SCS is a meaningful proxy for actual LLM confusion by comparing SCS to an empirical confusion matrix constructed from Few-NERD extraction outputs (1,953 type pairs, 216 with nonzero confusion).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Scope} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nQwen3-32B & All ($n{=}1953$) & 0.168 & 7.3e-14 & 0.135 \\\\\nQwen3-32B & Nonzero ($n{=}216$) & 0.272 & 5.0e-5 & 0.200 \\\\\nMiniLM-L6 & All ($n{=}1953$) & 0.144 & 1.7e-10 & 0.115 \\\\\nMiniLM-L6 & Nonzero ($n{=}216$) & 0.306 & 4.6e-6 & 0.228 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SCS vs.\\ empirical confusion matrix correlation. Both embeddings significantly predict actual confusion ($p < 10^{-5}$). Qwen3 is stronger on all pairs; MiniLM is stronger among actually-confused pairs.}\n\\label{tab:scs-validation}\n\\end{table}\n\nTable~\\ref{tab:scs-validation} shows that SCS from both embeddings significantly predicts empirical confusion.\nThe correlation is moderate ($\\rho{=}0.14$--$0.31$), indicating that SCS is a valid but partial proxy: confusability has dimensions beyond embedding similarity (e.g., context-dependent ambiguity, frequency-driven familiarity).\nThis ``valid but partial'' status supports using SCS for correlational analysis while explaining why SCS-based decomposition (SDGD-zero) underperforms empirical-confusion-based decomposition (SDGD-cal).\n\n\\subsection{DocRED Confusability Study}\n\\label{sec:docred}\n\nWe extend the confusability analysis to DocRED (96 document-level relation types), providing a third RE dataset for cross-task validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Count} & \\textbf{Accuracy} & \\textbf{$n$ Batches} & \\textbf{Mean BCS} \\\\\n\\midrule\n1  & 0.875 & 96 & 0.00 \\\\\n4  & 0.782 & 5  & 0.61 \\\\\n8  & 0.768 & 5  & 0.72 \\\\\n16 & 0.531 & 5  & 0.79 \\\\\n32 & 0.515 & 5  & 0.88 \\\\\n64 & 0.428 & 5  & 0.94 \\\\\n96 & 0.392 & 5  & 0.97 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED count curve: accuracy declines monotonically from 0.875 (single type) to 0.392 (all 96 types), a 48.3pp drop.}\n\\label{tab:docred-count}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{cccccl}\n\\toprule\n\\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$(pp)} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\n16 & 0.685 & 0.452 & $-$23.3 & $-$0.661 & $<$0.001 \\\\\n32 & 0.581 & 0.406 & $-$17.5 & $-$0.509 & 0.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED BCS-controlled accuracy. At fixed count, high-BCS batches show significantly lower accuracy (slope=$-0.713$, 95\\% CI [$-0.909, -0.529$]).}\n\\label{tab:docred-bcs}\n\\end{table}\n\nTables~\\ref{tab:docred-count} and \\ref{tab:docred-bcs} show that DocRED replicates the core findings from FewRel.\nThe count curve shows a 48.3pp monotonic decline (Table~\\ref{tab:docred-count}).\nControlling for count, BCS independently predicts degradation: at count=16, high-BCS batches are 23.3pp worse than low-BCS batches ($\\rho{=}{-}0.661$, $p{<}0.001$; Table~\\ref{tab:docred-bcs}).\nThe slope CI [$-0.909, -0.529$] excludes zero, confirming an independent confusability effect.\n\nCompared to FewRel-80 (where $\\Delta{=}{-}31.2$pp at count=16), DocRED shows a somewhat smaller gap (23.3pp), likely because document-level context provides additional disambiguation cues.\nThe direction and significance are fully consistent, constituting the fourth dataset (third RE dataset) to validate Claim~1.\n\n\\subsection{2$\\times$2 Interaction Effect}\n\\label{sec:interaction}\n\nWe test whether count and confusability interact multiplicatively or additively using a 2$\\times$2 factorial design on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\n\\midrule\nLow Count (6)  & 0.324 & 0.313 & $-$0.011 \\\\\nHigh Count (12) & 0.325 & 0.277 & $-$0.048 \\\\\n\\midrule\nCount Effect & +0.001 & $-$0.036 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{2$\\times$2 factorial on Few-NERD. Interaction is not significant ($z{=}{-}0.667$, $p{=}0.505$), consistent with additive (orthogonal) channels.}\n\\label{tab:2x2}\n\\end{table}\n\nTable~\\ref{tab:2x2} shows the 2$\\times$2 factorial results.\nThe main effects are: count $-0.018$, BCS $-0.029$.\nThe interaction term is not significant ($z{=}{-}0.667$, $p{=}0.505$), supporting the orthogonal channels hypothesis.\nIf count and confusability degraded extraction through the same mechanism, we would expect a super-additive interaction; the absence of such interaction is consistent with two independent channels (count$\\to$recall, confusability$\\to$type confusion) whose effects combine additively.\n\nThe BCS effect is numerically larger at high count ($-0.048$ vs.\\ $-0.011$), consistent with a larger confusability space in bigger schemas, but the difference is not statistically significant given the count range (6 vs.\\ 12).\n\n\\subsection{Error Taxonomy Analysis}\n\\label{sec:error-taxonomy}\n\nWe classify false positive predictions by error type across BCS bins to provide mechanistic evidence for the two-channel model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{BCS Bin} & \\textbf{$n$ FP} & \\textbf{IntraSub\\%} & \\textbf{ExtraSub\\%} & \\textbf{IntraSub/100g} \\\\\n\\midrule\n0 (single type)       & 6172 & 0.0  & 90.3 & 0.0 \\\\\nLow (0.75--0.82)      & 2231 & 1.6  & 89.9 & 3.4 \\\\\nMedium (0.82--0.88)   & 3843 & 10.6 & 78.1 & 6.5 \\\\\nHigh (0.88--0.95+)    & 6188 & 49.4 & 30.8 & 12.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error distribution by BCS bin on Few-NERD. IntraSub (intra-batch type substitution) rises monotonically with BCS ($\\rho{=}1.0$), while hallucination remains below 3\\% across all bins.}\n\\label{tab:error-taxonomy}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Task} & \\textbf{IntraSub vs BCS $\\rho$} & \\textbf{$p$} & \\textbf{ExtraSub=0?} \\\\\n\\midrule\nNER (Few-NERD)   & 1.000 & $<$0.001 & No \\\\\nRE (FewRel 80)   & 0.954 & $<$1e-6  & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-task error taxonomy comparison. IntraSub rate correlates near-perfectly with BCS on both tasks.}\n\\label{tab:error-cross-task}\n\\end{table}\n\nTable~\\ref{tab:error-taxonomy} shows a near-perfect monotonic relationship between BCS and IntraSub errors on Few-NERD.\nAt BCS=0 (single-type batches), IntraSub is 0\\% by definition---there are no other types to confuse.\nAs BCS increases, IntraSub rises to 49.4\\% of all false positives in high-BCS batches (12.9 per 100 gold entities).\nHallucination remains below 3\\% throughout, indicating that the LLM's primary failure mode is not fabrication but misassignment among semantically similar types.\n\nTable~\\ref{tab:error-cross-task} shows that this pattern replicates on FewRel 80-relation RE ($\\rho{=}0.954$), where IntraSub accounts for all type confusion (ExtraSub=0 in closed-schema RE).\nThe cross-task $\\rho{\\geq}0.95$ provides strong mechanistic evidence: confusability drives type confusion through intra-batch semantic interference, while count drives recall decline through attention dilution.\nThese are orthogonal channels operating on different error modes.\n\n\\subsection{Schema Decomposition: SDGD}\n\\label{sec:sdgd}\n\nWe evaluate whether confusability-aware schema decomposition can translate diagnostic insights into extraction improvements.\n\n\\subsubsection{SDGD on Few-NERD}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{Cal.\\ Cost} \\\\\n\\midrule\nSingle-pass          & 0.445 & 0.563 & 0.368 & --- \\\\\nRandom batch         & 0.301 & 0.331 & 0.276 & --- \\\\\nSDGD-zero (emb.)    & 0.241 & 0.324 & 0.191 & 0 ex. \\\\\nSDGD-cal (emp.)     & 0.285 & 0.295 & 0.276 & 10 ex.$\\times$66 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD variants on Few-NERD. All decomposition methods underperform single-pass. SDGD-cal improves over SDGD-zero (+18\\%) but remains 36\\% below single-pass.}\n\\label{tab:sdgd-fewnerd}\n\\end{table}\n\nTable~\\ref{tab:sdgd-fewnerd} presents the central negative result.\nSingle-pass extraction (all 66 types in one prompt) achieves F1=0.445.\nSDGD-zero degrades to 0.241, and even SDGD-cal (with 10 calibration examples per type) only reaches 0.285---still 36\\% below single-pass.\nRandom batching (0.301) outperforms SDGD-zero, indicating that confusability-aware grouping's unbalanced partition exacerbates merge difficulties.\n\nThe improvement from SDGD-zero to SDGD-cal (+18\\%) confirms that empirical confusion is a better partition signal than SCS ($\\rho{=}0.42$ between them), but the persistent gap to single-pass demonstrates that the bottleneck is merge amplification, not partition quality.\n\n\\subsubsection{SDGD on MAVEN}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Rel.\\ F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{Batches} \\\\\n\\midrule\nSingle-pass (168)     & 0.247 & 0.285 & 0.218 & 1 \\\\\nRandom batch ($k{=}12$)  & 0.178 & 0.145 & 0.231 & 12 \\\\\nSDGD-zero             & 0.142 & 0.108 & 0.208 & 12 \\\\\nSDGD-cal (5-shot)     & 0.168 & 0.132 & 0.230 & 8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD on MAVEN (168 event types). The same ordering holds: single-pass $>$ random $>$ SDGD-cal $>$ SDGD-zero.}\n\\label{tab:sdgd-maven}\n\\end{table}\n\nTable~\\ref{tab:sdgd-maven} shows that MAVEN (168 event types) replicates the Few-NERD failure pattern exactly.\nThe sdgd-cal/single-pass ratio is 0.68 on MAVEN vs.\\ 0.64 on Few-NERD, indicating a consistent $\\sim$35\\% structural decomposition cost.\nMerge amplification ratios are 2.1$\\times$ on Few-NERD and 2.6$\\times$ on MAVEN, confirming that the problem worsens with more types (more batches $\\to$ more merge conflicts).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{sdgd-cal/single} & \\textbf{Merge Ampl.} \\\\\n\\midrule\nFew-NERD & NER & 0.64 & 2.1$\\times$ \\\\\nMAVEN    & ED  & 0.68 & 2.6$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-task SDGD failure pattern. The $\\sim$35\\% structural cost is consistent across tasks.}\n\\label{tab:sdgd-cross-task}\n\\end{table}\n\n\\subsection{Ablation: Random Batching vs.\\ SDGD}\n\\label{sec:ablation-random}\n\nTo isolate confusability-aware grouping from batch count reduction, we compare SDGD-zero against random batching at matched batch counts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{IntraBatch Conf.} & \\textbf{Merge Dup.} \\\\\n\\midrule\nSingle-pass ($k{=}1$) & 0.445 & 0.049 & --- \\\\\nRandom ($k{=}4$)      & 0.321 & 0.034 & 1.8$\\times$ \\\\\nRandom ($k{=}8$)      & 0.301 & 0.028 & 2.1$\\times$ \\\\\nSDGD-zero ($k{=}4$)   & 0.241 & 0.018 & 2.4$\\times$ \\\\\nSDGD-zero ($k{=}8$)   & 0.218 & 0.012 & 2.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Random vs.\\ SDGD ablation. SDGD reduces intra-batch confusion (0.018 vs.\\ 0.034 at $k{=}4$) but produces higher merge amplification, resulting in lower F1.}\n\\label{tab:ablation-random}\n\\end{table}\n\nTable~\\ref{tab:ablation-random} reveals the precise failure mechanism of SDGD.\nSDGD-zero \\emph{does} reduce intra-batch confusion rate (0.018 vs.\\ 0.034 at $k{=}4$), confirming that the confusability signal is effective for partition.\nHowever, SDGD's confusability-aware grouping produces unbalanced partitions (a large ``easy'' batch plus several small ``hard'' batches), which makes merge more difficult and increases duplicate rates (2.4$\\times$ vs.\\ 1.8$\\times$).\nThe net effect is negative: the merge amplification cost exceeds the confusion reduction benefit.\n\nAll decomposition methods underperform single-pass, confirming that the bottleneck is decompose-then-merge itself, not the quality of the partition.\n\n\\subsection{Ablation: Per-Type Splitting}\n\\label{sec:per-type}\n\nWe evaluate per-type splitting ($k{=}66$ on Few-NERD) as the upper bound on decomposition---zero intra-batch confusability, maximum recall potential.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{$k$} & \\textbf{BCS} & \\textbf{Time(s)} \\\\\n\\midrule\nSingle-pass    & .445 & .563 & .368 & 1  & .95 & 79 \\\\\nSDGD-zero      & .241 & .324 & .191 & 4  & .72 & 261 \\\\\nRandom ($k{=}8$) & .301 & .331 & .276 & 8  & .85 & 494 \\\\\nPer-type       & .292 & .194 & .586 & 66 & .00 & 2540 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition spectrum on Few-NERD. Per-type achieves the highest recall (+59\\% vs.\\ single-pass) but the lowest precision ($-$66\\%), with 32$\\times$ latency.}\n\\label{tab:per-type}\n\\end{table}\n\nTable~\\ref{tab:per-type} reveals the fundamental paradox of decomposition: more thorough separation yields higher recall (0.586 vs.\\ 0.368 for single-pass, +59\\%) but catastrophically lower precision (0.194 vs.\\ 0.563, $-$66\\%).\nThe harmonic mean (F1) cannot be rescued when precision collapses this severely.\nPer-type splitting achieves zero intra-batch confusability but still underperforms single-pass by 15.3pp F1, with 32$\\times$ latency (66 API calls vs.\\ 1).\n\nThis establishes that even the most extreme decomposition cannot outperform single-pass extraction, confirming merge amplification as the fundamental limitation.\n\n\\section{Discussion}\n\n\\paragraph{Why Small $r$ Matters.}\nThe pairwise SCS--confusion correlations ($r{=}0.11$--$0.13$) are small in absolute terms but meaningful in context.\nIn noisy IE evaluation, many factors affect per-instance accuracy (context length, entity ambiguity, prompt position).\nThat embedding similarity alone explains $\\sim$1.5\\% of variance in confusion probability, across 1,953+ type pairs and multiple tasks, indicates a reliable signal.\nThe downstream effect is substantial: high-confusability batches show 23--31pp accuracy gaps and 10--28$\\times$ more type confusion errors.\n\n\\paragraph{Centrality Confound.}\nOn MAVEN (168 event types from a semantically homogeneous domain), per-type BCS aggregation shows a \\emph{positive} correlation with F1 ($\\rho{=}{+}0.19$--$0.21$), opposite to the expected direction.\nThis occurs because in homogeneous schemas, high mean BCS indicates central, well-represented types that LLMs extract well---conflating confusability with type centrality.\nPairwise analysis avoids this confound entirely.\nThis finding constitutes a methodological contribution: per-type confusability aggregation is unreliable on homogeneous schemas.\n\n\\paragraph{Merge Amplification as Structural Challenge.}\nThe consistent $\\sim$35\\% degradation across SDGD variants, datasets, and batch counts (Table~\\ref{tab:sdgd-cross-task}) indicates that merge amplification is not a fixable engineering problem but an intrinsic cost of decompose-then-merge.\nEach batch independently produces predictions that may conflict at merge time: duplicate spans with different types, inconsistent boundaries, and confidence miscalibration across batches.\nThese errors compound with more batches.\n\nThe correct application of confusability information is not schema decomposition but rather: (1) post-hoc confusion-aware calibration (adjusting predictions using an empirical confusion matrix), or (2) contrastive type descriptions that help the model distinguish confusable types within a single pass.\n\n\\paragraph{Multi-Model Validation.}\nLLaMA-3.3-70B replication achieves 87\\% consistency with Qwen3-32B on the core findings, indicating that the confusability effect is not model-specific but reflects a general property of how LLMs process type-dense prompts.\n\n\\section{Conclusion}\n\nWe present a controlled empirical study demonstrating that type count and type confusability are orthogonal predictors of extraction degradation in training-free LLM IE.\nPairwise confusability independently predicts degradation across NER, RE, and ED ($r{=}0.11$--$0.13$), with the effect amplifying 3.4$\\times$ with schema complexity.\nError taxonomy analysis reveals two distinct channels: count drives recall decline while confusability drives type confusion ($\\rho{\\geq}0.95$ cross-task).\nNaive confusability-aware decomposition (SDGD) fails due to merge amplification, but confusability remains valuable as a diagnostic tool for predicting where LLM extraction will fail.\nOur findings establish that future work should pursue calibration-based approaches that leverage confusability information without decomposing the extraction task.\n\n\\section*{Limitations}\n\nOur study is limited to two LLMs (Qwen3-32B, LLaMA-3.3-70B) and English-language datasets.\nThe confusability measures rely on embedding similarity, which we show is a valid but partial proxy ($\\rho{=}0.17$--$0.31$ with empirical confusion).\nOur SDGD experiments use simple merge strategies; more sophisticated merge methods (e.g., learned mergers) may partially mitigate amplification.\nThe 2$\\times$2 factorial has limited power to detect interactions due to the narrow count range (6 vs.\\ 12).\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "375324b5-21c4-48bd-a307-84f9f421f812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "a507b675-fad3-4f2b-a53d-b41768f8cec1",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Tool call

_source line 24 · 2026-05-16T07:57:27.024Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017eUi67jAz5RUd2ZMkFqc2V`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a507b675-fad3-4f2b-a53d-b41768f8cec1",
  "isSidechain": false,
  "requestId": "req_011Cb5tfBmecfDrsGTjkhezg",
  "type": "assistant",
  "uuid": "a0f629fe-c641-4310-a59a-c79f142f4467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCMwJHY9jeNKB38CwJVUgj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9334,
      "cache_read_input_tokens": 40250,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 40250,
          "cache_creation_input_tokens": 9334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9334
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

_source line 25 · 2026-05-16T07:57:27.181Z_

<details><summary>↩ Tool result · `toolu_017eUi67jAz5RUd2ZMkFqc2V`</summary>

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

! LaTeX Error: File `emnlp2023.sty' not found.

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
  "parentUuid": "a0f629fe-c641-4310-a59a-c79f142f4467",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "fea5ae32-9205-4932-98fd-d9209f2c01d5",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a0f629fe-c641-4310-a59a-c79f142f4467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T07:57:29.974Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023 style file isn't available. Let me switch to a standard article class instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea5ae32-9205-4932-98fd-d9209f2c01d5",
  "isSidechain": false,
  "requestId": "req_011Cb5tfUeuGJQEiRQEyDzmy",
  "type": "assistant",
  "uuid": "8373012a-685e-4395-80f5-572cd3fbe857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPVXA13htTkXpoZyoaG9Cf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 49584,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 49584,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 427
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

_source line 27 · 2026-05-16T07:57:30.449Z_

EMNLP style not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8373012a-685e-4395-80f5-572cd3fbe857",
  "isSidechain": false,
  "requestId": "req_011Cb5tfUeuGJQEiRQEyDzmy",
  "type": "assistant",
  "uuid": "344d6700-6a9d-4d33-827e-c9a791f534e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPVXA13htTkXpoZyoaG9Cf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 49584,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 49584,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 427
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

_source line 28 · 2026-05-16T07:57:33.514Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BBk7sUZSXw4BCFvLLP8bzK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{enumitem}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "344d6700-6a9d-4d33-827e-c9a791f534e8",
  "isSidechain": false,
  "requestId": "req_011Cb5tfUeuGJQEiRQEyDzmy",
  "type": "assistant",
  "uuid": "d8910ff4-96ae-4d38-9b24-035d3971fd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPVXA13htTkXpoZyoaG9Cf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 49584,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 49584,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 427
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

_source line 29 · 2026-05-16T07:57:33.532Z_

<details><summary>↩ Tool result · `toolu_01BBk7sUZSXw4BCFvLLP8bzK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8910ff4-96ae-4d38-9b24-035d3971fd49",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "432a5b66-8919-42d0-bb5b-98695ad82f39",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{url}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{enumitem}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 14,
        "newStart": 1,
        "newLines": 16,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{latexsym}",
          " \\usepackage{amsmath}",
          " \\usepackage{amssymb}",
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          "-\\usepackage{url}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{enumitem}",
          "+\\usepackage{natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\Type Count and Confusability as Orthogonal Failure Modes}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d8910ff4-96ae-4d38-9b24-035d3971fd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-16T07:57:33.556Z_

```json
{
  "parentUuid": "432a5b66-8919-42d0-bb5b-98695ad82f39",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "167dc02e-5edc-4dd4-94cd-257b7ab7dfe1",
  "timestamp": "2026-05-16T07:57:33.556Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-16T07:57:36.706Z_

Also need to fix the bibliography reference at the end since we don't have a .bib file. I'll replace it with inline references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "167dc02e-5edc-4dd4-94cd-257b7ab7dfe1",
  "isSidechain": false,
  "requestId": "req_011Cb5tfwwjEAmkxjyjo1QQ9",
  "type": "assistant",
  "uuid": "b7ffc194-fbb6-4ff5-8731-657cf98f4213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbFrH9H3P3arFHvdvK7faG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 50011,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 440,
          "cache_read_input_tokens": 50011,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 32 · 2026-05-16T07:57:42.077Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LupPGaeMyxX9Xf6A5imuWU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{9}\n\n\\bibitem{wei2023zeroshot}\nWei, X., et al. (2023).\nZero-Shot Information Extraction via Chatting with ChatGPT.\n\\emph{arXiv preprint arXiv:2302.10205}.\n\n\\bibitem{zhou2024universalner}\nZhou, W., et al. (2024).\nUniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition.\n\\emph{ICLR 2024}.\n\n\\bibitem{li2023gptner}\nLi, J., et al. (2023).\nGPT-NER: Named Entity Recognition via Large Language Models.\n\\emph{arXiv preprint arXiv:2304.10428}.\n\n\\bibitem{sainz2024gollie}\nSainz, O., et al. (2024).\nGoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.\n\\emph{ICLR 2024}.\n\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ffc194-fbb6-4ff5-8731-657cf98f4213",
  "isSidechain": false,
  "requestId": "req_011Cb5tfwwjEAmkxjyjo1QQ9",
  "type": "assistant",
  "uuid": "e1431dbe-1238-4882-88d7-0da8612d13e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbFrH9H3P3arFHvdvK7faG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 50011,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 440,
          "cache_read_input_tokens": 50011,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 33 · 2026-05-16T07:57:42.096Z_

<details><summary>↩ Tool result · `toolu_01LupPGaeMyxX9Xf6A5imuWU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1431dbe-1238-4882-88d7-0da8612d13e2",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "b57ee5e0-bd28-4f16-8a18-e76f08e105a5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{9}\n\n\\bibitem{wei2023zeroshot}\nWei, X., et al. (2023).\nZero-Shot Information Extraction via Chatting with ChatGPT.\n\\emph{arXiv preprint arXiv:2302.10205}.\n\n\\bibitem{zhou2024universalner}\nZhou, W., et al. (2024).\nUniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition.\n\\emph{ICLR 2024}.\n\n\\bibitem{li2023gptner}\nLi, J., et al. (2023).\nGPT-NER: Named Entity Recognition via Large Language Models.\n\\emph{arXiv preprint arXiv:2304.10428}.\n\n\\bibitem{sainz2024gollie}\nSainz, O., et al. (2024).\nGoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.\n\\emph{ICLR 2024}.\n\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 445,
        "oldLines": 6,
        "newStart": 445,
        "newLines": 28,
        "lines": [
          " Our SDGD experiments use simple merge strategies; more sophisticated merge methods (e.g., learned mergers) may partially mitigate amplification.",
          " The 2$\\times$2 factorial has limited power to detect interactions due to the narrow count range (6 vs.\\ 12).",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{9}",
          " ",
          "+\\bibitem{wei2023zeroshot}",
          "+Wei, X., et al. (2023).",
          "+Zero-Shot Information Extraction via Chatting with ChatGPT.",
          "+\\emph{arXiv preprint arXiv:2302.10205}.",
          "+",
          "+\\bibitem{zhou2024universalner}",
          "+Zhou, W., et al. (2024).",
          "+UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition.",
          "+\\emph{ICLR 2024}.",
          "+",
          "+\\bibitem{li2023gptner}",
          "+Li, J., et al. (2023).",
          "+GPT-NER: Named Entity Recognition via Large Language Models.",
          "+\\emph{arXiv preprint arXiv:2304.10428}.",
          "+",
          "+\\bibitem{sainz2024gollie}",
          "+Sainz, O., et al. (2024).",
          "+GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.",
          "+\\emph{ICLR 2024}.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e1431dbe-1238-4882-88d7-0da8612d13e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T07:57:50.367Z_

Also need to remove the `\cite` commands and replace with inline refs, and remove the natbib import since we're using thebibliography directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b57ee5e0-bd28-4f16-8a18-e76f08e105a5",
  "isSidechain": false,
  "requestId": "req_011Cb5tgaSSUH25C8jYUgf5u",
  "type": "assistant",
  "uuid": "f422c35b-4698-4ffb-852f-04e221c917f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwkE7WDpRkMAV8VMa29EZE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 50636,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 50636,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 525
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

_source line 35 · 2026-05-16T07:57:52.662Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PnKCFvEfVoo15CXwFr6h3v`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "old_string": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f422c35b-4698-4ffb-852f-04e221c917f1",
  "isSidechain": false,
  "requestId": "req_011Cb5tgaSSUH25C8jYUgf5u",
  "type": "assistant",
  "uuid": "5ea19d12-d819-4308-8a92-4042742f0985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwkE7WDpRkMAV8VMa29EZE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 50636,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 50636,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 525
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

_source line 36 · 2026-05-16T07:57:52.674Z_

<details><summary>↩ Tool result · `toolu_01PnKCFvEfVoo15CXwFr6h3v`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ea19d12-d819-4308-8a92-4042742f0985",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "4a4dfb8a-9a9c-47f0-af3d-c005173c7d98",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
    "oldString": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
    "newString": "",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 8,
        "newStart": 9,
        "newLines": 6,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{hyperref}",
          " \\usepackage{enumitem}",
          "-\\usepackage{natbib}",
          "-\\bibliographystyle{plainnat}",
          " ",
          " \\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\Type Count and Confusability as Orthogonal Failure Modes}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5ea19d12-d819-4308-8a92-4042742f0985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T07:57:55.897Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015sboyjzeEY3RAZ3Vbb9FAx`</summary>

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
  "parentUuid": "4a4dfb8a-9a9c-47f0-af3d-c005173c7d98",
  "isSidechain": false,
  "requestId": "req_011Cb5thNTQ87PoRNaUxrgmT",
  "type": "assistant",
  "uuid": "b292b8b7-531d-4bf9-b071-5115c0e3a5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpaqfnjKqB3boUoWbkwgXh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 51161,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 51161,
          "cache_creation_input_tokens": 273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 273
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

_source line 38 · 2026-05-16T07:57:56.442Z_

<details><summary>↩ Tool result · `toolu_015sboyjzeEY3RAZ3Vbb9FAx`</summary>

```text
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
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 150261 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b292b8b7-531d-4bf9-b071-5115c0e3a5e2",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "bded39b3-543b-4ccb-ba90-f0275536225a",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 150261 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b292b8b7-531d-4bf9-b071-5115c0e3a5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T07:57:59.164Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FJxqV9Xrp619S3hNcNCcQr`</summary>

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
  "parentUuid": "bded39b3-543b-4ccb-ba90-f0275536225a",
  "isSidechain": false,
  "requestId": "req_011Cb5thdjfDwcJyRnXYmwFg",
  "type": "assistant",
  "uuid": "60433b7e-28f9-4fa0-ba16-9d41491555fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkkeyHRy6gfFEuPFzCoHpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 51434,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 51434,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
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

_source line 40 · 2026-05-16T07:57:59.730Z_

<details><summary>↩ Tool result · `toolu_01FJxqV9Xrp619S3hNcNCcQr`</summary>

```text
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 152317 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60433b7e-28f9-4fa0-ba16-9d41491555fb",
  "isSidechain": false,
  "promptId": "2448ad5f-61b9-445f-8eda-d75fcfbced8d",
  "type": "user",
  "uuid": "78fd5d2d-a61b-4277-975d-038c1c40db39",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 152317 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "60433b7e-28f9-4fa0-ba16-9d41491555fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T07:58:11.781Z_

编译成功，8 页 PDF 已生成。

论文 `paper.pdf` 写入 `best/` 目录，包含：
- **Abstract + Introduction**: 两条 core claim + 贡献列表
- **Section 4.1**: SCS validation（Table 1, Qwen3/MiniLM 两组 embedding 的 ρ）
- **Section 4.2**: DocRED count curve + BCS-controlled（Tables 2--3, 48.3pp 下降 + 23.3pp gap）
- **Section 4.3**: 2×2 factorial（Table 4, 交互不显著 p=0.505 支撑 orthogonal channels）
- **Section 4.4**: Error taxonomy（Tables 5--6, IntraSub 0%→49.4% ρ=1.0, 跨任务 ρ≥0.954）
- **Section 4.5**: SDGD 负面结果（Tables 7--9, Few-NERD + MAVEN, ~35% structural cost）
- **Section 4.6**: Random batching ablation（Table 10, confusion ↓ 但 merge amplification ↑）
- **Section 4.7**: Per-type splitting（Table 11, recall +59% 但 precision −66%, 32× latency）
- **Discussion**: 小 r 的意义、centrality confound、merge amplification 结构性挑战
- 所有数字均来自 `experiment_data.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78fd5d2d-a61b-4277-975d-038c1c40db39",
  "isSidechain": false,
  "requestId": "req_011Cb5thsnkQuwbo2nkZZtas",
  "type": "assistant",
  "uuid": "56fcf29d-6bcf-4ce2-b588-3c3bc8279307",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kGwH4wNew7AogPCCtsndW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 52027,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 52027,
          "cache_creation_input_tokens": 238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 238
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "56fcf29d-6bcf-4ce2-b588-3c3bc8279307",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extrac…",
  "leafUuid": "56fcf29d-6bcf-4ce2-b588-3c3bc8279307",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "0a993cfd-dc7b-439c-b2ba-515cbc95f3ca"
}
```

---
