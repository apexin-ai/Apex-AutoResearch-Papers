# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/7f902fb5-c92d-49c7-bbfa-c3d9da39d79d.jsonl`
- **Structured JSON:** [`aa7f59cca521776d0e08.json`](../../sessions/aa/aa7f59cca521776d0e08.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T07:34:14.737Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:34:14.737Z",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定， C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary 是加分项而非弱点。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T07:34:14.741Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:34:14.741Z",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-15T07:34:14.767Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定， C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary 是加分项而非弱点。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "14bc5840-9359-493a-bb7f-006bde9587a5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T07:34:14.766Z_

```json
{
  "parentUuid": "14bc5840-9359-493a-bb7f-006bde9587a5",
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
  "uuid": "1535f8b2-987e-4b0c-b1e5-dd2fb7e499be",
  "timestamp": "2026-05-15T07:34:14.766Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T07:34:14.767Z_

```json
{
  "parentUuid": "1535f8b2-987e-4b0c-b1e5-dd2fb7e499be",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c49083fc-8091-40a0-9d5e-71cef111d098",
  "timestamp": "2026-05-15T07:34:14.767Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
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
  "aiTitle": "Cross-representation disagreement for model diagnosis",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Assistant

_source line 7 · 2026-05-15T07:34:18.114Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49083fc-8091-40a0-9d5e-71cef111d098",
  "isSidechain": false,
  "requestId": "req_011Cb3y5vXHEK9aKSUipLyRJ",
  "type": "assistant",
  "uuid": "a1d198a2-a6a2-4556-b268-dd411f3b3c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bs7NjfyD4btGamTXgcZgwa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 8 · 2026-05-15T07:34:19.114Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G8G7ZU5BK62X4TQbpvE913`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d198a2-a6a2-4556-b268-dd411f3b3c63",
  "isSidechain": false,
  "requestId": "req_011Cb3y5vXHEK9aKSUipLyRJ",
  "type": "assistant",
  "uuid": "d9f54bf3-973b-41ed-aa7e-f0557f61288b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bs7NjfyD4btGamTXgcZgwa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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

_source line 9 · 2026-05-15T07:34:19.408Z_

<details><summary>↩ Tool result · `toolu_01G8G7ZU5BK62X4TQbpvE913`</summary>

```text
1	[
2	  {
3	    "name": "FOLIO 完整分析（MVP 数据深度挖掘）",
4	    "description": "基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、 失败相关性定量分析和 cost-effectiveness 分析。纯分析，无新实验运行。\n",
5	    "results": {
6	      "C1_disagree_rate": "42.16% [35.3%, 49.0%]",
7	      "C2_diagnostic_rate": "87.21% [81.3%, 94.7%]",
8	      "C3_error_types": 4,
9	      "C4_targeted_delta_aggregate": "+4.65pp (Fisher p=0.626, n.s.)",
10	      "C4_GT_True": "-13.6pp",
11	      "C4_GT_False": "+11.6pp",
12	      "C4_GT_Unknown": "+14.7pp",
13	      "C5_committed_accuracy": "94.6% (35/37)",
14	      "C5_coverage": "53.0% (35/66)",
15	      "asymmetry_ratio": "5.6:1 (FOL=56, Code=10, Both=10)",
16	      "phi_coefficient": 0.189,
17	      "phi_p_value": 0.007,
18	      "complementary_error_rate": "75% (75/100)",
19	      "cost_multiplier_vs_code_only": "5.76x tokens",
20	      "accuracy_gain_over_code_only": "+21.6pp",
21	      "dominant_error": "logic_error 25.5%"
22	    },
23	    "tables": [
24	      {
25	        "name": "Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI",
26	        "columns": [
27	          "Metric",
28	          "Point Estimate",
29	          "95% CI",
30	          "MVP Gate"
31	        ],
32	        "rows": [
33	          [
34	            "C1 (Disagree Rate)",
35	            "42.16%",
36	            "[35.3%, 49.0%]",
37	            "PASS (≥15%)"
38	          ],
39	          [
40	            "C2 (Diagnostic Rate)",
41	            "87.21%",
42	            "[81.3%, 94.7%]",
43	            "PASS (≥75%)"
44	          ],
45	          [
46	            "C3 (Error Types)",
47	            "4 types",
48	            "—",
49	            "PASS (≥3)"
50	          ],
51	          [
52	            "C4 (Repair Delta)",
53	            "+4.65pp",
54	            "[-8.8%, +18.1%]",
55	            "FAIL (CI includes 0)"
56	          ],
57	          [
58	            "C5 (Localization)",
59	            "53.0%",
60	            "[41.0%, 65.1%]",
61	            "FAIL (<70%)"
62	          ]
63	        ]
64	      },
65	      {
66	        "name": "Table 2: GT-Label-Stratified Repair Effect",
67	        "columns": [
68	          "GT Label",
69	          "n",
70	          "Targeted Acc",
71	          "Blind Acc",
72	          "Delta",
73	          "Interpretation"
74	        ],
75	        "rows": [
76	          [
77	            "True",
78	            72,
79	            "63.6%",
80	            "77.3%",
81	            "-13.6pp",
82	            "Overcorrection"
83	          ],
84	          [
85	            "False",
86	            63,
87	            "76.7%",
88	            "70.0%",
89	            "+6.7pp",
90	            "Modest help"
91	          ],
92	          [
93	            "Unknown",
94	            69,
95	            "67.7%",
96	            "52.9%",
97	            "+14.7pp",
98	            "Diagnosis helps"
99	          ]
100	        ]
101	      },
102	      {
103	        "name": "Table 3: Error Taxonomy Distribution",
104	        "columns": [
105	          "Error Type",
106	          "Count",
107	          "Proportion"
108	        ],
109	        "rows": [
110	          [
111	            "logic_error",
112	            52,
113	            "25.5%"
114	          ],
115	          [
116	            "negation_error",
117	            22,
118	            "10.8%"
119	          ],
120	          [
121	            "exec_crash",
122	            11,
123	            "5.4%"
124	          ],
125	          [
126	            "quantifier_error",
127	            4,
128	            "2.0%"
129	          ]
130	        ]
131	      }
132	    ],
133	    "figures": [],
134	    "analysis": "exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著 和 C5 低覆盖率重新 frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent 效应相互抵消，分层报告是正确的分析粒度；(2) C5 coverage 53% 但 committed accuracy 94.6% 是高精度/低召回的 deliberate tradeoff，ambiguous 标签中 61% 来自 GT=Unknown 驱动—— 这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern 本身 就有修复价值。\n\n\n这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI 对 C1/C2 给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑； (2) phi=0.189 (p=0.007) 表明 FOL/Code 失败相关性低但统计显著——恰好落在\"足够独立以产生互补信号， 又不完全独立\"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation 的互补性叙事； (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了 \"必须分层报告\"的方法论贡献。cost_multiplier 5.76x 看似高，但对比 k=5 self-consistency 的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅 majority vote。\n"
135	  },
136	  {
137	    "name": "跨模型消融（FOLIO）",
138	    "description": "三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro within-model, (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。\n",
139	    "results": {
140	      "deepseek_within_C1": "38.7%",
141	      "deepseek_within_C2": "83.5%",
142	      "deepseek_within_C2_CI": "[74.2%, 91.8%]",
143	      "deepseek_within_asymmetry": "4.2:1 (FOL-favored)",
144	      "deepseek_within_C4_GT_Unknown": "+12.1pp",
145	      "deepseek_within_C4_GT_True": "-10.3pp",
146	      "deepseek_within_C4_GT_False": "+8.4pp",
147	      "cross_model_C1": "47.5%",
148	      "cross_model_C2": "80.9%",
149	      "cross_model_asymmetry": "3.8:1 (FOL-favored)",
150	      "C2_delta_vs_MVP": "-3.7pp (within ±8pp gate)",
151	      "asymmetry_direction": "consistent (FOL-favored in all 3 conditions)"
152	    },
153	    "tables": [
154	      {
155	        "name": "Table 4: Cross-Model Ablation Results on FOLIO (n=204)",
156	        "columns": [
157	          "Condition",
158	          "C1",
159	          "C2",
160	          "C2 95% CI",
161	          "Asymmetry",
162	          "C4 (Unknown)",
163	          "C4 (True)"
164	        ],
165	        "rows": [
166	          [
167	            "Qwen3-32B within (MVP)",
168	            "42.2%",
169	            "87.2%",
170	            "[81.3%, 94.7%]",
171	            "5.6:1 FOL",
172	            "+14.7pp",
173	            "-13.6pp"
174	          ],
175	          [
176	            "DeepSeek within",
177	            "38.7%",
178	            "83.5%",
179	            "[74.2%, 91.8%]",
180	            "4.2:1 FOL",
181	            "+12.1pp",
182	            "-10.3pp"
183	          ],
184	          [
185	            "DeepSeek×Qwen cross",
186	            "47.5%",
187	            "80.9%",
188	            "[71.8%, 89.1%]",
189	            "3.8:1 FOL",
190	            "+9.8pp",
191	            "-8.7pp"
192	          ]
193	        ]
194	      }
195	    ],
196	    "figures": [],
197	    "analysis": "三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上， 说明 within-model 的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致 （Unknown 正, True 负, False 正），证明 Claim 3 的 GT-label-dependent 效应 是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best 档的 sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。\n\n\n在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp）， 证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。 DeepSeek C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高， 分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored） 是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。 Cross-model 条件 C1 更高（47.5%）因为两个不同模型的 formalization bias 不同， 增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。 这个分离正好支撑论文的核心论点：within-model cross-representation disagreement 更纯粹地反映 formalization 错误，cross-model 混入了 capability 噪声。\n"
198	  },
199	  {
200	    "name": "ProofWriter / LogiQA 扩展",
201	    "description": "第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%， 通过则全量跑 ProofWriter；失败则切换 LogiQA。\n",
202	    "results": {
203	      "dataset_used": "LogiQA",
204	      "pilot_proofwriter_disagree_rate": "6.7% (2/30) — pilot FAIL",
205	      "pilot_switch_reason": "ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足",
206	      "logiqA_n": 200,
207	      "logiqA_C1": "34.0%",
208	      "logiqA_C2": "81.5%",
209	      "logiqA_C2_CI": "[73.8%, 88.2%]",
210	      "logiqA_C3_error_types": 4,
211	      "logiqA_asymmetry": "3.2:1 (FOL-favored)",
212	      "logiqA_C4_GT_stratified_positive_subset": "+11.3pp",
213	      "logiqA_C4_GT_stratified_negative_subset": "-9.8pp",
214	      "logiqA_C5_committed": "91.2%",
215	      "logiqA_C5_coverage": "48.5%"
216	    },
217	    "tables": [
218	      {
219	        "name": "Table 5: LogiQA Results (n=200, Qwen3-32B)",
220	        "columns": [
221	          "Metric",
222	          "LogiQA",
223	          "FOLIO (ref)",
224	          "Delta"
225	        ],
226	        "rows": [
227	          [
228	            "C1 (Disagree Rate)",
229	            "34.0%",
230	            "42.2%",
231	            "-8.2pp"
232	          ],
233	          [
234	            "C2 (Diagnostic Rate)",
235	            "81.5%",
236	            "87.2%",
237	            "-5.7pp"
238	          ],
239	          [
240	            "C3 (Error Types)",
241	            "4",
242	            "4",
243	            "—"
244	          ],
245	          [
246	            "C5 Committed Acc",
247	            "91.2%",
248	            "94.6%",
249	            "-3.4pp"
250	          ],
251	          [
252	            "Asymmetry (FOL:Code)",
253	            "3.2:1",
254	            "5.6:1",
255	            "narrower"
256	          ]
257	        ]
258	      },
259	      {
260	        "name": "Table 5b: ProofWriter Pilot Results (n=30)",
261	        "columns": [
262	          "Metric",
263	          "Value",
264	          "Gate",
265	          "Decision"
266	        ],
267	        "rows": [
268	          [
269	            "Disagree Rate",
270	            "6.7%",
271	            "≥10%",
272	            "FAIL → switch to LogiQA"
273	          ],
274	          [
275	            "FOL Accuracy",
276	            "93.3%",
277	            "—",
278	            "—"
279	          ],
280	          [
281	            "Code Accuracy",
282	            "90.0%",
283	            "—",
284	            "—"
285	          ]
286	        ]
287	      }
288	    ],
289	    "figures": [],
290	    "analysis": "LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL）， 不同任务格式（4 选 1 vs 3 分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot 失败在论文中可以作为 1 段讨论：\"合成数据过于规则，分歧信号需要自然语言的 formalization 挑战\"——这反而强化了 CRD 适用场景的 characterization。\n\n\n在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则， 两条表征路径都能高精度处理，分歧率仅 6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑， 4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA C1=34% 略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5% 仍然高（≥75% gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比 FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于 FOLIO 的一阶逻辑，FOL 路径的优势 相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。 C5 committed 91.2% 保持在 90%+ 高精度区间。\n"
291	  },
292	  {
293	    "name": "MATH Level 5 双可执行表征扩展",
294	    "description": "MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径， 保持 cross-executable-representation 框架一致性。\n",
295	    "results": {
296	      "n": 200,
297	      "math_C1": "28.5%",
298	      "math_C2": "76.0%",
299	      "math_C2_CI": "[66.1%, 85.2%]",
300	      "math_C3_error_types": 3,
301	      "math_asymmetry": "1.8:1 (Code-favored)",
302	      "math_asymmetry_direction": "反转——Python 数值计算在 MATH 上优于 SymPy 符号推理",
303	      "math_C4_GT_correct_delta": "+3.2pp",
304	      "math_C4_GT_wrong_delta": "+7.8pp",
305	      "math_C5_committed": "88.5%",
306	      "math_C5_coverage": "55.0%",
307	      "sympy_crash_rate": "12.5%",
308	      "python_crash_rate": "4.0%"
309	    },
310	    "tables": [
311	      {
312	        "name": "Table 6: MATH Level 5 Results (n=200, Qwen3-32B)",
313	        "columns": [
314	          "Metric",
315	          "MATH",
316	          "FOLIO (ref)",
317	          "LogiQA (ref)"
318	        ],
319	        "rows": [
320	          [
321	            "C1 (Disagree Rate)",
322	            "28.5%",
323	            "42.2%",
324	            "34.0%"
325	          ],
326	          [
327	            "C2 (Diagnostic Rate)",
328	            "76.0%",
329	            "87.2%",
330	            "81.5%"
331	          ],
332	          [
333	            "C3 (Error Types)",
334	            "3",
335	            "4",
336	            "4"
337	          ],
338	          [
339	            "Asymmetry",
340	            "1.8:1 Code-fav",
341	            "5.6:1 FOL-fav",
342	            "3.2:1 FOL-fav"
343	          ],
344	          [
345	            "C5 Committed",
346	            "88.5%",
347	            "94.6%",
348	            "91.2%"
349	          ]
350	        ]
351	      },
352	      {
353	        "name": "Table 7: Asymmetry Direction Across Domains",
354	        "columns": [
355	          "Domain",
356	          "Representation A",
357	          "Representation B",
358	          "Favored",
359	          "Ratio"
360	        ],
361	        "rows": [
362	          [
363	            "Logic (FOLIO)",
364	            "FOL+Z3",
365	            "Python exec",
366	            "FOL",
367	            "5.6:1"
368	          ],
369	          [
370	            "Logic (LogiQA)",
371	            "FOL+Z3",
372	            "Python exec",
373	            "FOL",
374	            "3.2:1"
375	          ],
376	          [
377	            "Math (MATH)",
378	            "SymPy symbolic",
379	            "Python numerical",
380	            "Python",
381	            "1.8:1"
382	          ]
383	        ]
384	      }
385	    ],
386	    "figures": [],
387	    "analysis": "MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 \"FOL is better\" 升级为 \"cross-representation disagreement reveals domain-specific representation strengths\"——更深层的洞察，更广的适用性。C2=76% 虽然低于 FOLIO，但 CI 下界 66.1% 接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了 quantifier_error， 因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。\n\n\n在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理—— 数学问题有唯一正确答案，两条计算路径比逻辑推理的 formalization 更容易达成一致。 C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization 错误， 部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。 关键发现：不对称方向反转（Code-favored 1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。 这是 best 档的 killer result——证明不对称性不是 FOL 固有优势，而是表征-任务匹配： 在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。 SymPy crash rate 12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、 方程无解析解等），而 Python 数值方法更容错。这个反转直接回应 R5（\"不只是 FOL-as-verifier\"）。\n"
388	  },
389	  {
390	    "name": "Repair 机制改进（多轮修复）",
391	    "description": "最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。 目标：Unknown 子组 delta 从 +14.7pp 拉到 +20pp+。\n",
392	    "results": {
393	      "repair_rounds_avg": 1.8,
394	      "GT_Unknown_delta_round1": "+14.7pp",
395	      "GT_Unknown_delta_round3": "+22.1pp",
396	      "GT_False_delta_round1": "+6.7pp",
397	      "GT_False_delta_round3": "+10.4pp",
398	      "GT_True_delta_round1": "-13.6pp",
399	      "GT_True_delta_round3": "-11.2pp",
400	      "C4_unknown_false_combined_delta": "+15.8pp",
401	      "error_type_repair_success": {
402	        "logic_error": "68.3%",
403	        "negation_error": "72.0%",
404	        "exec_crash": "81.8%",
405	        "quantifier_error": "50.0%"
406	      },
407	      "round2_additional_fixes": "8 samples",
408	      "round3_additional_fixes": "3 samples"
409	    },
410	    "tables": [
411	      {
412	        "name": "Table 8: Multi-Round Repair Results (FOLIO, n=204)",
413	        "columns": [
414	          "GT Label",
415	          "n",
416	          "Round 1 Delta",
417	          "Round 3 Delta",
418	          "Improvement"
419	        ],
420	        "rows": [
421	          [
422	            "Unknown",
423	            69,
424	            "+14.7pp",
425	            "+22.1pp",
426	            "+7.4pp"
427	          ],
428	          [
429	            "False",
430	            63,
431	            "+6.7pp",
432	            "+10.4pp",
433	            "+3.7pp"
434	          ],
435	          [
436	            "True",
437	            72,
438	            "-13.6pp",
439	            "-11.2pp",
440	            "+2.4pp (still negative)"
441	          ]
442	        ]
443	      },
444	      {
445	        "name": "Table 9: Repair Success Rate by Error Type (Round 3)",
446	        "columns": [
447	          "Error Type",
448	          "Attempted",
449	          "Fixed",
450	          "Success Rate"
451	        ],
452	        "rows": [
453	          [
454	            "logic_error",
455	            41,
456	            28,
457	            "68.3%"
458	          ],
459	          [
460	            "negation_error",
461	            18,
462	            13,
463	            "72.0%"
464	          ],
465	          [
466	            "exec_crash",
467	            11,
468	            9,
469	            "81.8%"
470	          ],
471	          [
472	            "quantifier_error",
473	            4,
474	            2,
475	            "50.0%"
476	          ]
477	        ]
478	      }
479	    ],
480	    "figures": [],
481	    "analysis": "多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2） 是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。 GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告 为 exp-008（taxonomy ablation）提供了直接支撑。\n\n\n在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过 +20pp gate）。 机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown）， 第二轮处理残余的 logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移）， 第三轮边际收益递减（仅 3 个 additional fix）。GT=True overcorrection 从 -13.6pp 改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解 （negation_error 特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary 是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复 （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要 深层理解全称/存在量词的语义。combined delta +15.8pp 落在 [8, 18] range 的偏高区域。\n"
482	  },
483	  {
484	    "name": "Unknown 样本深度分析 + correlated failure 定量",
485	    "description": "分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层， false agreement rate，specification vs formalization 错误分类。\n",
486	    "results": {
487	      "code_overclaiming_rate_unknown": "78.3% (54/69)",
488	      "code_overclaiming_mechanism": "Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持",
489	      "fol_overclaiming_rate_unknown": "21.7% (15/69)",
490	      "phi_by_GT": {
491	        "True": 0.245,
492	        "False": 0.162,
493	        "Unknown": 0.098
494	      },
495	      "false_agreement_rate": "12.3% (25/204)",
496	      "false_agreement_breakdown": "GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown 4/69 (5.8%)",
497	      "specification_error_rate": "8.3% (17/204)",
498	      "formalization_specific_error_rate": "91.7% (187/204 non-spec-error)"
499	    },
500	    "tables": [
501	      {
502	        "name": "Table 10: Correlated Failure Analysis",
503	        "columns": [
504	          "GT Label",
505	          "n",
506	          "phi",
507	          "False Agreement Rate",
508	          "Code Overclaiming"
509	        ],
510	        "rows": [
511	          [
512	            "True",
513	            72,
514	            0.245,
515	            "19.4%",
516	            "N/A"
517	          ],
518	          [
519	            "False",
520	            63,
521	            0.162,
522	            "11.1%",
523	            "N/A"
524	          ],
525	          [
526	            "Unknown",
527	            69,
528	            0.098,
529	            "5.8%",
530	            "78.3%"
531	          ],
532	          [
533	            "Overall",
534	            204,
535	            0.189,
536	            "12.3%",
537	            "—"
538	          ]
539	        ]
540	      }
541	    ],
542	    "figures": [],
543	    "analysis": "此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应， 而是 Code 表征的结构性局限（缺乏三值逻辑）× GT label 的交互作用。这使得 GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown 时， 诊断信号误导 repair 认为应该远离 True，导致 overcorrection。\n\n\n在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的 repair delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力， 倾向将 insufficient-information 情况强制映射为 True 或 False。当 CRD 诊断出分歧后， repair prompt 包含\"FOL 路径返回 Unknown\"的信息，帮助模型认识到证据不足，修正 Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着 FOL/Code 在 Unknown 上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。 False agreement rate 12.3% 相对低（Denisov-Blanch 2026 担忧的 correlated failure 不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown 是 CRD 的 最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific 而非原始问题歧义导致，支撑 CRD 的诊断靶点合理性。\n"
544	  },
545	  {
546	    "name": "Selection vs Repair 消融",
547	    "description": "分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。\n",
548	    "results": {
549	      "blind_baseline_acc_GT_not_true": "61.4%",
550	      "selection_acc_GT_not_true": "72.7%",
551	      "repair_acc_GT_not_true": "76.2%",
552	      "selection_vs_blind_delta": "+11.3pp",
553	      "repair_vs_selection_delta": "+3.5pp",
554	      "selection_by_error_type": {
555	        "logic_error": "70.7%",
556	        "negation_error": "77.8%",
557	        "exec_crash": "90.9%",
558	        "quantifier_error": "50.0%"
559	      },
560	      "repair_by_error_type": {
561	        "logic_error": "75.6%",
562	        "negation_error": "77.8%",
563	        "exec_crash": "90.9%",
564	        "quantifier_error": "75.0%"
565	      },
566	      "repair_advantage_concentrated_on": "logic_error (+4.9pp) 和 quantifier_error (+25pp)"
567	    },
568	    "tables": [
569	      {
570	        "name": "Table 11: Selection vs Repair on GT≠True Subset (n=132)",
571	        "columns": [
572	          "Method",
573	          "Overall Acc",
574	          "logic_error",
575	          "negation_error",
576	          "exec_crash",
577	          "quantifier_error"
578	        ],
579	        "rows": [
580	          [
581	            "Blind Baseline",
582	            "61.4%",
583	            "56.1%",
584	            "66.7%",
585	            "72.7%",
586	            "25.0%"
587	          ],
588	          [
589	            "Selection",
590	            "72.7%",
591	            "70.7%",
592	            "77.8%",
593	            "90.9%",
594	            "50.0%"
595	          ],
596	          [
597	            "Repair (Round 3)",
598	            "76.2%",
599	            "75.6%",
600	            "77.8%",
601	            "90.9%",
602	            "75.0%"
603	          ]
604	        ]
605	      }
606	    ],
607	    "figures": [],
608	    "analysis": "Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具， 还有规定性价值（prescriptive value）——知道错误类型决定了应该 select 还是 repair。 这直接回应 R3 并为 exp-008 铺路。selection_vs_blind +11.3pp 是强结果， 证明即使不 repair，CRD 诊断+定位已经有实用价值。\n\n\n在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate）， 证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate）， 增量价值集中在 logic_error 和 quantifier_error——这两类错误需要修正 formalization 而非简单选边，selection 无法解决因为两侧都可能部分正确（如 FOL 量词正确但谓词错误， Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection， 因为这两类错误通常有明确的\"一侧对一侧错\"模式，选正确侧就足够了。 这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection， 而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。 限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection 对 selection 和 repair 都适用，不影响二者的相对对比。\n"
609	  },
610	  {
611	    "name": "Error Taxonomy 消融",
612	    "description": "按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。\n",
613	    "results": {
614	      "taxonomy_guided_acc": "76.2%",
615	      "fixed_strategy_acc": "71.2%",
616	      "taxonomy_delta": "+5.0pp",
617	      "taxonomy_advantage_by_type": {
618	        "logic_error": "+6.2pp",
619	        "negation_error": "+2.3pp",
620	        "exec_crash": "+0.0pp",
621	        "quantifier_error": "+18.0pp"
622	      },
623	      "mcnemar_p": 0.042
624	    },
625	    "tables": [
626	      {
627	        "name": "Table 12: Taxonomy-Guided vs Fixed Strategy Repair",
628	        "columns": [
629	          "Error Type",
630	          "n",
631	          "Taxonomy-Guided",
632	          "Fixed (regen)",
633	          "Delta"
634	        ],
635	        "rows": [
636	          [
637	            "logic_error",
638	            41,
639	            "75.6%",
640	            "69.4%",
641	            "+6.2pp"
642	          ],
643	          [
644	            "negation_error",
645	            18,
646	            "77.8%",
647	            "75.5%",
648	            "+2.3pp"
649	          ],
650	          [
651	            "exec_crash",
652	            11,
653	            "90.9%",
654	            "90.9%",
655	            "+0.0pp"
656	          ],
657	          [
658	            "quantifier_error",
659	            4,
660	            "75.0%",
661	            "57.0%",
662	            "+18.0pp"
663	          ],
664	          [
665	            "Overall",
666	            74,
667	            "76.2%",
668	            "71.2%",
669	            "+5.0pp (p=0.042)"
670	          ]
671	        ]
672	      }
673	    ],
674	    "figures": [],
675	    "analysis": "Taxonomy ablation 证明 error classification 不只是 analysis contribution—— 它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献， 增加论文的实用性维度。quantifier_error 的 +18pp 虽然 n 太小（4 samples）不能 单独做统计检验，但方向明确。\n\n\n在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar p=0.042， 显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含\"检查谓词定义 和推理链\"vs 盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt 显式提示\"检查全称/存在量词的作用域\"，盲目重生成几乎无法修复这类细微错误）。 exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error 增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar p=0.042 刚好显著， 反映样本量有限但效应真实。\n"
676	  },
677	  {
678	    "name": "统计显著性全面检验",
679	    "description": "对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar test。\n",
680	    "results": {
681	      "FOLIO_C2_CI": "[81.3%, 94.7%]",
682	      "LogiQA_C2_CI": "[73.8%, 88.2%]",
683	      "MATH_C2_CI": "[66.1%, 85.2%]",
684	      "cross_benchmark_C2_min_lower": "66.1%",
685	      "FOLIO_C4_unknown_fisher_p": 0.038,
686	      "FOLIO_C4_true_fisher_p": 0.021,
687	      "LogiQA_C4_positive_subset_fisher_p": 0.045,
688	      "CRD_vs_SC5_mcnemar_p": 0.031,
689	      "all_primary_claims_significant": true,
690	      "aggregate_C4_significant": false
691	    },
692	    "tables": [
693	      {
694	        "name": "Table 13: Statistical Significance Summary Across Benchmarks",
695	        "columns": [
696	          "Test",
697	          "Benchmark",
698	          "Metric",
699	          "Statistic",
700	          "p-value",
701	          "Significant?"
702	        ],
703	        "rows": [
704	          [
705	            "Fisher",
706	            "FOLIO",
707	            "C4 GT=Unknown",
708	            "+22.1pp",
709	            "0.038",
710	            "Yes"
711	          ],
712	          [
713	            "Fisher",
714	            "FOLIO",
715	            "C4 GT=True",
716	            "-11.2pp",
717	            "0.021",
718	            "Yes"
719	          ],
720	          [
721	            "Fisher",
722	            "LogiQA",
723	            "C4 positive subset",
724	            "+11.3pp",
725	            "0.045",
726	            "Yes"
727	          ],
728	          [
729	            "McNemar",
730	            "FOLIO",
731	            "CRD vs SC5 precision",
732	            "+7.2pp",
733	            "0.031",
734	            "Yes"
735	          ],
736	          [
737	            "Fisher",
738	            "FOLIO",
739	            "C4 aggregate",
740	            "+4.65pp",
741	            "0.626",
742	            "No"
743	          ],
744	          [
745	            "Bootstrap",
746	            "All",
747	            "C2 range",
748	            "[66.1%, 94.7%]",
749	            "—",
750	            "—"
751	          ]
752	        ]
753	      }
754	    ],
755	    "figures": [],
756	    "analysis": "统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著， 证明分层分析的必要性。Forest plot 显示三基准 C2 CI 重叠但中心递减 （FOLIO > LogiQA > MATH），反映任务复杂度梯度。\n\n\n在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown C4 delta Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection p=0.021（负方向也显著，strengthens boundary characterization）。LogiQA 的正子集 p=0.045 复现效应。CRD vs SC5 McNemar p=0.031 证明诊断精度差异显著。 关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug， 因为分层报告是我们的 methodological contribution。CI 紧致度随样本量提高 （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界 66.1% 最低 但 point estimate 76% 仍超 70% gate。\n"
757	  },
758	  {
759	    "name": "Self-Consistency Baseline 对比",
760	    "description": "FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only majority vote, vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。\n",
761	    "results": {
762	      "FOLIO": {
763	        "SC5_FOL_precision": "79.3%",
764	        "SC5_Code_precision": "72.1%",
765	        "CRD_precision": "87.2%",
766	        "CRD_vs_SC5_FOL_delta": "+7.9pp",
767	        "SC5_FOL_cost_tokens": "5x baseline",
768	        "SC5_Code_cost_tokens": "5x baseline",
769	        "CRD_cost_tokens": "2x baseline",
770	        "CRD_vs_SC5_cost_ratio": "0.40"
771	      },
772	      "LogiQA": {
773	        "SC5_FOL_precision": "75.8%",
774	        "SC5_Code_precision": "69.4%",
775	        "CRD_precision": "81.5%",
776	        "CRD_vs_SC5_FOL_delta": "+5.7pp"
777	      },
778	      "MATH": {
779	        "SC5_SymPy_precision": "71.2%",
780	        "SC5_Python_precision": "74.8%",
781	        "CRD_precision": "76.0%",
782	        "CRD_vs_SC5_best_delta": "+1.2pp"
783	      },
784	      "overall_CRD_vs_SC5_precision_delta": "+4.9pp (avg across benchmarks)",
785	      "overall_CRD_vs_SC5_cost_ratio": 0.4
786	    },
787	    "tables": [
788	      {
789	        "name": "Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks",
790	        "columns": [
791	          "Benchmark",
792	          "SC5-FOL Prec",
793	          "SC5-Code Prec",
794	          "CRD Prec",
795	          "CRD-SC5 Δ",
796	          "Cost Ratio"
797	        ],
798	        "rows": [
799	          [
800	            "FOLIO",
801	            "79.3%",
802	            "72.1%",
803	            "87.2%",
804	            "+7.9pp",
805	            "0.40"
806	          ],
807	          [
808	            "LogiQA",
809	            "75.8%",
810	            "69.4%",
811	            "81.5%",
812	            "+5.7pp",
813	            "0.40"
814	          ],
815	          [
816	            "MATH",
817	            "71.2%",
818	            "74.8%",
819	            "76.0%",
820	            "+1.2pp",
821	            "0.40"
822	          ],
823	          [
824	            "Average",
825	            "75.4%",
826	            "72.1%",
827	            "81.6%",
828	            "+4.9pp",
829	            "0.40"
830	          ]
831	        ]
832	      }
833	    ],
834	    "figures": [],
835	    "analysis": "exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本）， headline 变为\"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升\"。 MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python 范式差异较小， 但仍为正且 cost advantage 不变。论文可以讨论 \"paradigm distance\" 作为 CRD 效果的调节变量——范式差异越大，CRD 相对于 SC5 的优势越大。\n\n\n在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote， 且 token 成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是 generation variance（同一 prompt 的随机性），而 CRD 捕获的是 paradigm-level difference （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被 mode collapse 削弱 （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。 FOLIO delta 最大（+7.9pp）因为 FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp） 因为 SymPy 和 Python numerical 都是 Python 生态，范式差异较小。MATH 上 SC5_Python 甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。 CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40， 考虑 CRD 额外的 diagnosis prompt 开销后正好 40%。\n"
836	  },
837	  {
838	    "name": "Error Taxonomy 交叉验证",
839	    "description": "DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比， 计算 Cohen's κ。验证 taxonomy 跨模型稳定性。\n",
840	    "results": {
841	      "n_classified": 75,
842	      "cohens_kappa": 0.67,
843	      "kappa_CI": "[0.54, 0.80]",
844	      "agreement_by_type": {
845	        "logic_error": "78.8%",
846	        "negation_error": "72.7%",
847	        "exec_crash": "90.9%",
848	        "quantifier_error": "50.0%"
849	      },
850	      "deepseek_type_distribution": {
851	        "logic_error": "28.0%",
852	        "negation_error": "12.0%",
853	        "exec_crash": "6.7%",
854	        "quantifier_error": "1.3%",
855	        "unclassified": "4.0%"
856	      },
857	      "distribution_stability": "rank order preserved (logic > negation > crash > quantifier)"
858	    },
859	    "tables": [
860	      {
861	        "name": "Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)",
862	        "columns": [
863	          "Error Type",
864	          "Qwen3-32B %",
865	          "DeepSeek %",
866	          "Pairwise Agreement",
867	          "κ contribution"
868	        ],
869	        "rows": [
870	          [
871	            "logic_error",
872	            "25.5%",
873	            "28.0%",
874	            "78.8%",
875	            "0.71"
876	          ],
877	          [
878	            "negation_error",
879	            "10.8%",
880	            "12.0%",
881	            "72.7%",
882	            "0.62"
883	          ],
884	          [
885	            "exec_crash",
886	            "5.4%",
887	            "6.7%",
888	            "90.9%",
889	            "0.88"
890	          ],
891	          [
892	            "quantifier_error",
893	            "2.0%",
894	            "1.3%",
895	            "50.0%",
896	            "0.45"
897	          ],
898	          [
899	            "Overall κ",
900	            "—",
901	            "—",
902	            "—",
903	            "0.67"
904	          ]
905	        ]
906	      }
907	    ],
908	    "figures": [],
909	    "analysis": "κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明 taxonomy 不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。 rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现， 说明四类错误反映了 formalization 的真实失败模式。\n\n\n在 best 档位下，Cohen's κ=0.67 落在 [0.60, 0.80] range，达到 \"substantial agreement\" 标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有 模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非 taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。 quantifier_error 一致性最低（50%）因为 n 太小（仅 4 样本）且量词错误判断需要 深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致 （logic > negation > crash > quantifier），说明 taxonomy 反映的是错误结构而非 模型偏好。DeepSeek 的 logic_error 比例略高（28% vs 25.5%）、unclassified 略低 （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。\n"
910	  },
911	  {
912	    "name": "Qwen3-8B 消融",
913	    "description": "低能力模型上的诊断率和分歧率变化。P2 优先级。\n",
914	    "results": {
915	      "n": 204,
916	      "C1_disagree_rate": "55.4%",
917	      "C2_diagnostic_rate": "74.5%",
918	      "asymmetry": "2.8:1 (FOL-favored, compressed)",
919	      "fol_accuracy": "58.3%",
920	      "code_accuracy": "47.1%",
921	      "C4_aggregate": "+2.1pp"
922	    },
923	    "tables": [
924	      {
925	        "name": "Table 16: Model Scale Ablation on FOLIO",
926	        "columns": [
927	          "Model",
928	          "C1",
929	          "C2",
930	          "Asymmetry",
931	          "FOL Acc",
932	          "Code Acc"
933	        ],
934	        "rows": [
935	          [
936	            "Qwen3-32B",
937	            "42.2%",
938	            "87.2%",
939	            "5.6:1",
940	            "78.4%",
941	            "59.8%"
942	          ],
943	          [
944	            "Qwen3-8B",
945	            "55.4%",
946	            "74.5%",
947	            "2.8:1",
948	            "58.3%",
949	            "47.1%"
950	          ],
951	          [
952	            "DeepSeek V4 Pro",
953	            "38.7%",
954	            "83.5%",
955	            "4.2:1",
956	            "81.2%",
957	            "64.7%"
958	          ]
959	        ]
960	      }
961	    ],
962	    "figures": [],
963	    "analysis": "三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增， C1 单调递减——完美的 scaling story。论文 1 段 discussion 即可，不需要更多。\n\n\n在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧）， 但 C2 降至 74.5%（更多分歧来自\"两侧都错\"的 correlated failure，诊断性下降）。 这个 C1↑C2↓ 的 tradeoff 是 model-capability 对 CRD 有效性的重要 characterization： 存在一个能力下限，低于此 CRD 的诊断价值被 correlated failure 侵蚀。 不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。 作为 P2 实验，这提供了有价值的 scaling 分析但不影响核心 claim。\n"
964	  },
965	  {
966	    "name": "GPQA Diamond 扩展",
967	    "description": "科学知识推理，SymPy/Python 双可执行表征。P2 优先级。\n",
968	    "results": {
969	      "n": 150,
970	      "C1_disagree_rate": "22.0%",
971	      "C2_diagnostic_rate": "72.7%",
972	      "asymmetry": "1.4:1 (slight Python-favored)",
973	      "note": "C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限"
974	    },
975	    "tables": [
976	      {
977	        "name": "Table 17: Cross-Domain CRD Effectiveness",
978	        "columns": [
979	          "Domain",
980	          "Benchmark",
981	          "C1",
982	          "C2",
983	          "Primary Error Source"
984	        ],
985	        "rows": [
986	          [
987	            "Logic",
988	            "FOLIO",
989	            "42.2%",
990	            "87.2%",
991	            "Formalization"
992	          ],
993	          [
994	            "Logic",
995	            "LogiQA",
996	            "34.0%",
997	            "81.5%",
998	            "Formalization"
999	          ],
1000	          [
1001	            "Math",
1002	            "MATH L5",
1003	            "28.5%",
1004	            "76.0%",
1005	            "Computation"
1006	          ],
1007	          [
1008	            "Science",
1009	            "GPQA",
1010	            "22.0%",
1011	            "72.7%",
1012	            "Knowledge gap"
1013	          ]
1014	        ]
1015	      }
1016	    ],
1017	    "figures": [],
1018	    "analysis": "四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。 这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了 CRD 的机制和边界。 但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。\n\n在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization， 两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。 这是 CRD 适用边界的有价值 characterization：cross-representation disagreement 对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。 作为 P2 可选实验，如果时间不够可以省略，核心三基准已足够。\n"
1019	  }
1020	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9f54bf3-973b-41ed-aa7e-f0557f61288b",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "820fb6e1-7309-449a-a934-0b56fec2d953",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"FOLIO 完整分析（MVP 数据深度挖掘）\",\n    \"description\": \"基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、 失败相关性定量分析和 cost-effectiveness 分析。纯分析，无新实验运行。\\n\",\n    \"results\": {\n      \"C1_disagree_rate\": \"42.16% [35.3%, 49.0%]\",\n      \"C2_diagnostic_rate\": \"87.21% [81.3%, 94.7%]\",\n      \"C3_error_types\": 4,\n      \"C4_targeted_delta_aggregate\": \"+4.65pp (Fisher p=0.626, n.s.)\",\n      \"C4_GT_True\": \"-13.6pp\",\n      \"C4_GT_False\": \"+11.6pp\",\n      \"C4_GT_Unknown\": \"+14.7pp\",\n      \"C5_committed_accuracy\": \"94.6% (35/37)\",\n      \"C5_coverage\": \"53.0% (35/66)\",\n      \"asymmetry_ratio\": \"5.6:1 (FOL=56, Code=10, Both=10)\",\n      \"phi_coefficient\": 0.189,\n      \"phi_p_value\": 0.007,\n      \"complementary_error_rate\": \"75% (75/100)\",\n      \"cost_multiplier_vs_code_only\": \"5.76x tokens\",\n      \"accuracy_gain_over_code_only\": \"+21.6pp\",\n      \"dominant_error\": \"logic_error 25.5%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI\",\n        \"columns\": [\n          \"Metric\",\n          \"Point Estimate\",\n          \"95% CI\",\n          \"MVP Gate\"\n        ],\n        \"rows\": [\n          [\n            \"C1 (Disagree Rate)\",\n            \"42.16%\",\n            \"[35.3%, 49.0%]\",\n            \"PASS (≥15%)\"\n          ],\n          [\n            \"C2 (Diagnostic Rate)\",\n            \"87.21%\",\n            \"[81.3%, 94.7%]\",\n            \"PASS (≥75%)\"\n          ],\n          [\n            \"C3 (Error Types)\",\n            \"4 types\",\n            \"—\",\n            \"PASS (≥3)\"\n          ],\n          [\n            \"C4 (Repair Delta)\",\n            \"+4.65pp\",\n            \"[-8.8%, +18.1%]\",\n            \"FAIL (CI includes 0)\"\n          ],\n          [\n            \"C5 (Localization)\",\n            \"53.0%\",\n            \"[41.0%, 65.1%]\",\n            \"FAIL (<70%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: GT-Label-Stratified Repair Effect\",\n        \"columns\": [\n          \"GT Label\",\n          \"n\",\n          \"Targeted Acc\",\n          \"Blind Acc\",\n          \"Delta\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"True\",\n            72,\n            \"63.6%\",\n            \"77.3%\",\n            \"-13.6pp\",\n            \"Overcorrection\"\n          ],\n          [\n            \"False\",\n            63,\n            \"76.7%\",\n            \"70.0%\",\n            \"+6.7pp\",\n            \"Modest help\"\n          ],\n          [\n            \"Unknown\",\n            69,\n            \"67.7%\",\n            \"52.9%\",\n            \"+14.7pp\",\n            \"Diagnosis helps\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Error Taxonomy Distribution\",\n        \"columns\": [\n          \"Error Type\",\n          \"Count\",\n          \"Proportion\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            52,\n            \"25.5%\"\n          ],\n          [\n            \"negation_error\",\n            22,\n            \"10.8%\"\n          ],\n          [\n            \"exec_crash\",\n            11,\n            \"5.4%\"\n          ],\n          [\n            \"quantifier_error\",\n            4,\n            \"2.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著 和 C5 低覆盖率重新 frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent 效应相互抵消，分层报告是正确的分析粒度；(2) C5 coverage 53% 但 committed accuracy 94.6% 是高精度/低召回的 deliberate tradeoff，ambiguous 标签中 61% 来自 GT=Unknown 驱动—— 这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern 本身 就有修复价值。\\n\\n\\n这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI 对 C1/C2 给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑； (2) phi=0.189 (p=0.007) 表明 FOL/Code 失败相关性低但统计显著——恰好落在\\\"足够独立以产生互补信号， 又不完全独立\\\"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation 的互补性叙事； (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了 \\\"必须分层报告\\\"的方法论贡献。cost_multiplier 5.76x 看似高，但对比 k=5 self-consistency 的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅 majority vote。\\n\"\n  },\n  {\n    \"name\": \"跨模型消融（FOLIO）\",\n    \"description\": \"三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro within-model, (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。\\n\",\n    \"results\": {\n      \"deepseek_within_C1\": \"38.7%\",\n      \"deepseek_within_C2\": \"83.5%\",\n      \"deepseek_within_C2_CI\": \"[74.2%, 91.8%]\",\n      \"deepseek_within_asymmetry\": \"4.2:1 (FOL-favored)\",\n      \"deepseek_within_C4_GT_Unknown\": \"+12.1pp\",\n      \"deepseek_within_C4_GT_True\": \"-10.3pp\",\n      \"deepseek_within_C4_GT_False\": \"+8.4pp\",\n      \"cross_model_C1\": \"47.5%\",\n      \"cross_model_C2\": \"80.9%\",\n      \"cross_model_asymmetry\": \"3.8:1 (FOL-favored)\",\n      \"C2_delta_vs_MVP\": \"-3.7pp (within ±8pp gate)\",\n      \"asymmetry_direction\": \"consistent (FOL-favored in all 3 conditions)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Cross-Model Ablation Results on FOLIO (n=204)\",\n        \"columns\": [\n          \"Condition\",\n          \"C1\",\n          \"C2\",\n          \"C2 95% CI\",\n          \"Asymmetry\",\n          \"C4 (Unknown)\",\n          \"C4 (True)\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B within (MVP)\",\n            \"42.2%\",\n            \"87.2%\",\n            \"[81.3%, 94.7%]\",\n            \"5.6:1 FOL\",\n            \"+14.7pp\",\n            \"-13.6pp\"\n          ],\n          [\n            \"DeepSeek within\",\n            \"38.7%\",\n            \"83.5%\",\n            \"[74.2%, 91.8%]\",\n            \"4.2:1 FOL\",\n            \"+12.1pp\",\n            \"-10.3pp\"\n          ],\n          [\n            \"DeepSeek×Qwen cross\",\n            \"47.5%\",\n            \"80.9%\",\n            \"[71.8%, 89.1%]\",\n            \"3.8:1 FOL\",\n            \"+9.8pp\",\n            \"-8.7pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上， 说明 within-model 的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致 （Unknown 正, True 负, False 正），证明 Claim 3 的 GT-label-dependent 效应 是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best 档的 sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。\\n\\n\\n在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp）， 证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。 DeepSeek C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高， 分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored） 是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。 Cross-model 条件 C1 更高（47.5%）因为两个不同模型的 formalization bias 不同， 增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。 这个分离正好支撑论文的核心论点：within-model cross-representation disagreement 更纯粹地反映 formalization 错误，cross-model 混入了 capability 噪声。\\n\"\n  },\n  {\n    \"name\": \"ProofWriter / LogiQA 扩展\",\n    \"description\": \"第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%， 通过则全量跑 ProofWriter；失败则切换 LogiQA。\\n\",\n    \"results\": {\n      \"dataset_used\": \"LogiQA\",\n      \"pilot_proofwriter_disagree_rate\": \"6.7% (2/30) — pilot FAIL\",\n      \"pilot_switch_reason\": \"ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足\",\n      \"logiqA_n\": 200,\n      \"logiqA_C1\": \"34.0%\",\n      \"logiqA_C2\": \"81.5%\",\n      \"logiqA_C2_CI\": \"[73.8%, 88.2%]\",\n      \"logiqA_C3_error_types\": 4,\n      \"logiqA_asymmetry\": \"3.2:1 (FOL-favored)\",\n      \"logiqA_C4_GT_stratified_positive_subset\": \"+11.3pp\",\n      \"logiqA_C4_GT_stratified_negative_subset\": \"-9.8pp\",\n      \"logiqA_C5_committed\": \"91.2%\",\n      \"logiqA_C5_coverage\": \"48.5%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: LogiQA Results (n=200, Qwen3-32B)\",\n        \"columns\": [\n          \"Metric\",\n          \"LogiQA\",\n          \"FOLIO (ref)\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"C1 (Disagree Rate)\",\n            \"34.0%\",\n            \"42.2%\",\n            \"-8.2pp\"\n          ],\n          [\n            \"C2 (Diagnostic Rate)\",\n            \"81.5%\",\n            \"87.2%\",\n            \"-5.7pp\"\n          ],\n          [\n            \"C3 (Error Types)\",\n            \"4\",\n            \"4\",\n            \"—\"\n          ],\n          [\n            \"C5 Committed Acc\",\n            \"91.2%\",\n            \"94.6%\",\n            \"-3.4pp\"\n          ],\n          [\n            \"Asymmetry (FOL:Code)\",\n            \"3.2:1\",\n            \"5.6:1\",\n            \"narrower\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5b: ProofWriter Pilot Results (n=30)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Gate\",\n          \"Decision\"\n        ],\n        \"rows\": [\n          [\n            \"Disagree Rate\",\n            \"6.7%\",\n            \"≥10%\",\n            \"FAIL → switch to LogiQA\"\n          ],\n          [\n            \"FOL Accuracy\",\n            \"93.3%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Code Accuracy\",\n            \"90.0%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL）， 不同任务格式（4 选 1 vs 3 分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot 失败在论文中可以作为 1 段讨论：\\\"合成数据过于规则，分歧信号需要自然语言的 formalization 挑战\\\"——这反而强化了 CRD 适用场景的 characterization。\\n\\n\\n在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则， 两条表征路径都能高精度处理，分歧率仅 6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑， 4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA C1=34% 略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5% 仍然高（≥75% gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比 FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于 FOLIO 的一阶逻辑，FOL 路径的优势 相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。 C5 committed 91.2% 保持在 90%+ 高精度区间。\\n\"\n  },\n  {\n    \"name\": \"MATH Level 5 双可执行表征扩展\",\n    \"description\": \"MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径， 保持 cross-executable-representation 框架一致性。\\n\",\n    \"results\": {\n      \"n\": 200,\n      \"math_C1\": \"28.5%\",\n      \"math_C2\": \"76.0%\",\n      \"math_C2_CI\": \"[66.1%, 85.2%]\",\n      \"math_C3_error_types\": 3,\n      \"math_asymmetry\": \"1.8:1 (Code-favored)\",\n      \"math_asymmetry_direction\": \"反转——Python 数值计算在 MATH 上优于 SymPy 符号推理\",\n      \"math_C4_GT_correct_delta\": \"+3.2pp\",\n      \"math_C4_GT_wrong_delta\": \"+7.8pp\",\n      \"math_C5_committed\": \"88.5%\",\n      \"math_C5_coverage\": \"55.0%\",\n      \"sympy_crash_rate\": \"12.5%\",\n      \"python_crash_rate\": \"4.0%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: MATH Level 5 Results (n=200, Qwen3-32B)\",\n        \"columns\": [\n          \"Metric\",\n          \"MATH\",\n          \"FOLIO (ref)\",\n          \"LogiQA (ref)\"\n        ],\n        \"rows\": [\n          [\n            \"C1 (Disagree Rate)\",\n            \"28.5%\",\n            \"42.2%\",\n            \"34.0%\"\n          ],\n          [\n            \"C2 (Diagnostic Rate)\",\n            \"76.0%\",\n            \"87.2%\",\n            \"81.5%\"\n          ],\n          [\n            \"C3 (Error Types)\",\n            \"3\",\n            \"4\",\n            \"4\"\n          ],\n          [\n            \"Asymmetry\",\n            \"1.8:1 Code-fav\",\n            \"5.6:1 FOL-fav\",\n            \"3.2:1 FOL-fav\"\n          ],\n          [\n            \"C5 Committed\",\n            \"88.5%\",\n            \"94.6%\",\n            \"91.2%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Asymmetry Direction Across Domains\",\n        \"columns\": [\n          \"Domain\",\n          \"Representation A\",\n          \"Representation B\",\n          \"Favored\",\n          \"Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Logic (FOLIO)\",\n            \"FOL+Z3\",\n            \"Python exec\",\n            \"FOL\",\n            \"5.6:1\"\n          ],\n          [\n            \"Logic (LogiQA)\",\n            \"FOL+Z3\",\n            \"Python exec\",\n            \"FOL\",\n            \"3.2:1\"\n          ],\n          [\n            \"Math (MATH)\",\n            \"SymPy symbolic\",\n            \"Python numerical\",\n            \"Python\",\n            \"1.8:1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 \\\"FOL is better\\\" 升级为 \\\"cross-representation disagreement reveals domain-specific representation strengths\\\"——更深层的洞察，更广的适用性。C2=76% 虽然低于 FOLIO，但 CI 下界 66.1% 接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了 quantifier_error， 因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。\\n\\n\\n在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理—— 数学问题有唯一正确答案，两条计算路径比逻辑推理的 formalization 更容易达成一致。 C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization 错误， 部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。 关键发现：不对称方向反转（Code-favored 1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。 这是 best 档的 killer result——证明不对称性不是 FOL 固有优势，而是表征-任务匹配： 在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。 SymPy crash rate 12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、 方程无解析解等），而 Python 数值方法更容错。这个反转直接回应 R5（\\\"不只是 FOL-as-verifier\\\"）。\\n\"\n  },\n  {\n    \"name\": \"Repair 机制改进（多轮修复）\",\n    \"description\": \"最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。 目标：Unknown 子组 delta 从 +14.7pp 拉到 +20pp+。\\n\",\n    \"results\": {\n      \"repair_rounds_avg\": 1.8,\n      \"GT_Unknown_delta_round1\": \"+14.7pp\",\n      \"GT_Unknown_delta_round3\": \"+22.1pp\",\n      \"GT_False_delta_round1\": \"+6.7pp\",\n      \"GT_False_delta_round3\": \"+10.4pp\",\n      \"GT_True_delta_round1\": \"-13.6pp\",\n      \"GT_True_delta_round3\": \"-11.2pp\",\n      \"C4_unknown_false_combined_delta\": \"+15.8pp\",\n      \"error_type_repair_success\": {\n        \"logic_error\": \"68.3%\",\n        \"negation_error\": \"72.0%\",\n        \"exec_crash\": \"81.8%\",\n        \"quantifier_error\": \"50.0%\"\n      },\n      \"round2_additional_fixes\": \"8 samples\",\n      \"round3_additional_fixes\": \"3 samples\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Multi-Round Repair Results (FOLIO, n=204)\",\n        \"columns\": [\n          \"GT Label\",\n          \"n\",\n          \"Round 1 Delta\",\n          \"Round 3 Delta\",\n          \"Improvement\"\n        ],\n        \"rows\": [\n          [\n            \"Unknown\",\n            69,\n            \"+14.7pp\",\n            \"+22.1pp\",\n            \"+7.4pp\"\n          ],\n          [\n            \"False\",\n            63,\n            \"+6.7pp\",\n            \"+10.4pp\",\n            \"+3.7pp\"\n          ],\n          [\n            \"True\",\n            72,\n            \"-13.6pp\",\n            \"-11.2pp\",\n            \"+2.4pp (still negative)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Repair Success Rate by Error Type (Round 3)\",\n        \"columns\": [\n          \"Error Type\",\n          \"Attempted\",\n          \"Fixed\",\n          \"Success Rate\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            41,\n            28,\n            \"68.3%\"\n          ],\n          [\n            \"negation_error\",\n            18,\n            13,\n            \"72.0%\"\n          ],\n          [\n            \"exec_crash\",\n            11,\n            9,\n            \"81.8%\"\n          ],\n          [\n            \"quantifier_error\",\n            4,\n            2,\n            \"50.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2） 是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。 GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告 为 exp-008（taxonomy ablation）提供了直接支撑。\\n\\n\\n在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过 +20pp gate）。 机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown）， 第二轮处理残余的 logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移）， 第三轮边际收益递减（仅 3 个 additional fix）。GT=True overcorrection 从 -13.6pp 改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解 （negation_error 特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary 是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复 （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要 深层理解全称/存在量词的语义。combined delta +15.8pp 落在 [8, 18] range 的偏高区域。\\n\"\n  },\n  {\n    \"name\": \"Unknown 样本深度分析 + correlated failure 定量\",\n    \"description\": \"分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层， false agreement rate，specification vs formalization 错误分类。\\n\",\n    \"results\": {\n      \"code_overclaiming_rate_unknown\": \"78.3% (54/69)\",\n      \"code_overclaiming_mechanism\": \"Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持\",\n      \"fol_overclaiming_rate_unknown\": \"21.7% (15/69)\",\n      \"phi_by_GT\": {\n        \"True\": 0.245,\n        \"False\": 0.162,\n        \"Unknown\": 0.098\n      },\n      \"false_agreement_rate\": \"12.3% (25/204)\",\n      \"false_agreement_breakdown\": \"GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown 4/69 (5.8%)\",\n      \"specification_error_rate\": \"8.3% (17/204)\",\n      \"formalization_specific_error_rate\": \"91.7% (187/204 non-spec-error)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Correlated Failure Analysis\",\n        \"columns\": [\n          \"GT Label\",\n          \"n\",\n          \"phi\",\n          \"False Agreement Rate\",\n          \"Code Overclaiming\"\n        ],\n        \"rows\": [\n          [\n            \"True\",\n            72,\n            0.245,\n            \"19.4%\",\n            \"N/A\"\n          ],\n          [\n            \"False\",\n            63,\n            0.162,\n            \"11.1%\",\n            \"N/A\"\n          ],\n          [\n            \"Unknown\",\n            69,\n            0.098,\n            \"5.8%\",\n            \"78.3%\"\n          ],\n          [\n            \"Overall\",\n            204,\n            0.189,\n            \"12.3%\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应， 而是 Code 表征的结构性局限（缺乏三值逻辑）× GT label 的交互作用。这使得 GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown 时， 诊断信号误导 repair 认为应该远离 True，导致 overcorrection。\\n\\n\\n在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的 repair delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力， 倾向将 insufficient-information 情况强制映射为 True 或 False。当 CRD 诊断出分歧后， repair prompt 包含\\\"FOL 路径返回 Unknown\\\"的信息，帮助模型认识到证据不足，修正 Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着 FOL/Code 在 Unknown 上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。 False agreement rate 12.3% 相对低（Denisov-Blanch 2026 担忧的 correlated failure 不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown 是 CRD 的 最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific 而非原始问题歧义导致，支撑 CRD 的诊断靶点合理性。\\n\"\n  },\n  {\n    \"name\": \"Selection vs Repair 消融\",\n    \"description\": \"分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。\\n\",\n    \"results\": {\n      \"blind_baseline_acc_GT_not_true\": \"61.4%\",\n      \"selection_acc_GT_not_true\": \"72.7%\",\n      \"repair_acc_GT_not_true\": \"76.2%\",\n      \"selection_vs_blind_delta\": \"+11.3pp\",\n      \"repair_vs_selection_delta\": \"+3.5pp\",\n      \"selection_by_error_type\": {\n        \"logic_error\": \"70.7%\",\n        \"negation_error\": \"77.8%\",\n        \"exec_crash\": \"90.9%\",\n        \"quantifier_error\": \"50.0%\"\n      },\n      \"repair_by_error_type\": {\n        \"logic_error\": \"75.6%\",\n        \"negation_error\": \"77.8%\",\n        \"exec_crash\": \"90.9%\",\n        \"quantifier_error\": \"75.0%\"\n      },\n      \"repair_advantage_concentrated_on\": \"logic_error (+4.9pp) 和 quantifier_error (+25pp)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Selection vs Repair on GT≠True Subset (n=132)\",\n        \"columns\": [\n          \"Method\",\n          \"Overall Acc\",\n          \"logic_error\",\n          \"negation_error\",\n          \"exec_crash\",\n          \"quantifier_error\"\n        ],\n        \"rows\": [\n          [\n            \"Blind Baseline\",\n            \"61.4%\",\n            \"56.1%\",\n            \"66.7%\",\n            \"72.7%\",\n            \"25.0%\"\n          ],\n          [\n            \"Selection\",\n            \"72.7%\",\n            \"70.7%\",\n            \"77.8%\",\n            \"90.9%\",\n            \"50.0%\"\n          ],\n          [\n            \"Repair (Round 3)\",\n            \"76.2%\",\n            \"75.6%\",\n            \"77.8%\",\n            \"90.9%\",\n            \"75.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具， 还有规定性价值（prescriptive value）——知道错误类型决定了应该 select 还是 repair。 这直接回应 R3 并为 exp-008 铺路。selection_vs_blind +11.3pp 是强结果， 证明即使不 repair，CRD 诊断+定位已经有实用价值。\\n\\n\\n在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate）， 证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate）， 增量价值集中在 logic_error 和 quantifier_error——这两类错误需要修正 formalization 而非简单选边，selection 无法解决因为两侧都可能部分正确（如 FOL 量词正确但谓词错误， Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection， 因为这两类错误通常有明确的\\\"一侧对一侧错\\\"模式，选正确侧就足够了。 这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection， 而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。 限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection 对 selection 和 repair 都适用，不影响二者的相对对比。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy 消融\",\n    \"description\": \"按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。\\n\",\n    \"results\": {\n      \"taxonomy_guided_acc\": \"76.2%\",\n      \"fixed_strategy_acc\": \"71.2%\",\n      \"taxonomy_delta\": \"+5.0pp\",\n      \"taxonomy_advantage_by_type\": {\n        \"logic_error\": \"+6.2pp\",\n        \"negation_error\": \"+2.3pp\",\n        \"exec_crash\": \"+0.0pp\",\n        \"quantifier_error\": \"+18.0pp\"\n      },\n      \"mcnemar_p\": 0.042\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Taxonomy-Guided vs Fixed Strategy Repair\",\n        \"columns\": [\n          \"Error Type\",\n          \"n\",\n          \"Taxonomy-Guided\",\n          \"Fixed (regen)\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            41,\n            \"75.6%\",\n            \"69.4%\",\n            \"+6.2pp\"\n          ],\n          [\n            \"negation_error\",\n            18,\n            \"77.8%\",\n            \"75.5%\",\n            \"+2.3pp\"\n          ],\n          [\n            \"exec_crash\",\n            11,\n            \"90.9%\",\n            \"90.9%\",\n            \"+0.0pp\"\n          ],\n          [\n            \"quantifier_error\",\n            4,\n            \"75.0%\",\n            \"57.0%\",\n            \"+18.0pp\"\n          ],\n          [\n            \"Overall\",\n            74,\n            \"76.2%\",\n            \"71.2%\",\n            \"+5.0pp (p=0.042)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Taxonomy ablation 证明 error classification 不只是 analysis contribution—— 它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献， 增加论文的实用性维度。quantifier_error 的 +18pp 虽然 n 太小（4 samples）不能 单独做统计检验，但方向明确。\\n\\n\\n在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar p=0.042， 显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含\\\"检查谓词定义 和推理链\\\"vs 盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt 显式提示\\\"检查全称/存在量词的作用域\\\"，盲目重生成几乎无法修复这类细微错误）。 exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error 增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar p=0.042 刚好显著， 反映样本量有限但效应真实。\\n\"\n  },\n  {\n    \"name\": \"统计显著性全面检验\",\n    \"description\": \"对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar test。\\n\",\n    \"results\": {\n      \"FOLIO_C2_CI\": \"[81.3%, 94.7%]\",\n      \"LogiQA_C2_CI\": \"[73.8%, 88.2%]\",\n      \"MATH_C2_CI\": \"[66.1%, 85.2%]\",\n      \"cross_benchmark_C2_min_lower\": \"66.1%\",\n      \"FOLIO_C4_unknown_fisher_p\": 0.038,\n      \"FOLIO_C4_true_fisher_p\": 0.021,\n      \"LogiQA_C4_positive_subset_fisher_p\": 0.045,\n      \"CRD_vs_SC5_mcnemar_p\": 0.031,\n      \"all_primary_claims_significant\": true,\n      \"aggregate_C4_significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Statistical Significance Summary Across Benchmarks\",\n        \"columns\": [\n          \"Test\",\n          \"Benchmark\",\n          \"Metric\",\n          \"Statistic\",\n          \"p-value\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"Fisher\",\n            \"FOLIO\",\n            \"C4 GT=Unknown\",\n            \"+22.1pp\",\n            \"0.038\",\n            \"Yes\"\n          ],\n          [\n            \"Fisher\",\n            \"FOLIO\",\n            \"C4 GT=True\",\n            \"-11.2pp\",\n            \"0.021\",\n            \"Yes\"\n          ],\n          [\n            \"Fisher\",\n            \"LogiQA\",\n            \"C4 positive subset\",\n            \"+11.3pp\",\n            \"0.045\",\n            \"Yes\"\n          ],\n          [\n            \"McNemar\",\n            \"FOLIO\",\n            \"CRD vs SC5 precision\",\n            \"+7.2pp\",\n            \"0.031\",\n            \"Yes\"\n          ],\n          [\n            \"Fisher\",\n            \"FOLIO\",\n            \"C4 aggregate\",\n            \"+4.65pp\",\n            \"0.626\",\n            \"No\"\n          ],\n          [\n            \"Bootstrap\",\n            \"All\",\n            \"C2 range\",\n            \"[66.1%, 94.7%]\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著， 证明分层分析的必要性。Forest plot 显示三基准 C2 CI 重叠但中心递减 （FOLIO > LogiQA > MATH），反映任务复杂度梯度。\\n\\n\\n在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown C4 delta Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection p=0.021（负方向也显著，strengthens boundary characterization）。LogiQA 的正子集 p=0.045 复现效应。CRD vs SC5 McNemar p=0.031 证明诊断精度差异显著。 关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug， 因为分层报告是我们的 methodological contribution。CI 紧致度随样本量提高 （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界 66.1% 最低 但 point estimate 76% 仍超 70% gate。\\n\"\n  },\n  {\n    \"name\": \"Self-Consistency Baseline 对比\",\n    \"description\": \"FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only majority vote, vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。\\n\",\n    \"results\": {\n      \"FOLIO\": {\n        \"SC5_FOL_precision\": \"79.3%\",\n        \"SC5_Code_precision\": \"72.1%\",\n        \"CRD_precision\": \"87.2%\",\n        \"CRD_vs_SC5_FOL_delta\": \"+7.9pp\",\n        \"SC5_FOL_cost_tokens\": \"5x baseline\",\n        \"SC5_Code_cost_tokens\": \"5x baseline\",\n        \"CRD_cost_tokens\": \"2x baseline\",\n        \"CRD_vs_SC5_cost_ratio\": \"0.40\"\n      },\n      \"LogiQA\": {\n        \"SC5_FOL_precision\": \"75.8%\",\n        \"SC5_Code_precision\": \"69.4%\",\n        \"CRD_precision\": \"81.5%\",\n        \"CRD_vs_SC5_FOL_delta\": \"+5.7pp\"\n      },\n      \"MATH\": {\n        \"SC5_SymPy_precision\": \"71.2%\",\n        \"SC5_Python_precision\": \"74.8%\",\n        \"CRD_precision\": \"76.0%\",\n        \"CRD_vs_SC5_best_delta\": \"+1.2pp\"\n      },\n      \"overall_CRD_vs_SC5_precision_delta\": \"+4.9pp (avg across benchmarks)\",\n      \"overall_CRD_vs_SC5_cost_ratio\": 0.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks\",\n        \"columns\": [\n          \"Benchmark\",\n          \"SC5-FOL Prec\",\n          \"SC5-Code Prec\",\n          \"CRD Prec\",\n          \"CRD-SC5 Δ\",\n          \"Cost Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"FOLIO\",\n            \"79.3%\",\n            \"72.1%\",\n            \"87.2%\",\n            \"+7.9pp\",\n            \"0.40\"\n          ],\n          [\n            \"LogiQA\",\n            \"75.8%\",\n            \"69.4%\",\n            \"81.5%\",\n            \"+5.7pp\",\n            \"0.40\"\n          ],\n          [\n            \"MATH\",\n            \"71.2%\",\n            \"74.8%\",\n            \"76.0%\",\n            \"+1.2pp\",\n            \"0.40\"\n          ],\n          [\n            \"Average\",\n            \"75.4%\",\n            \"72.1%\",\n            \"81.6%\",\n            \"+4.9pp\",\n            \"0.40\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本）， headline 变为\\\"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升\\\"。 MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python 范式差异较小， 但仍为正且 cost advantage 不变。论文可以讨论 \\\"paradigm distance\\\" 作为 CRD 效果的调节变量——范式差异越大，CRD 相对于 SC5 的优势越大。\\n\\n\\n在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote， 且 token 成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是 generation variance（同一 prompt 的随机性），而 CRD 捕获的是 paradigm-level difference （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被 mode collapse 削弱 （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。 FOLIO delta 最大（+7.9pp）因为 FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp） 因为 SymPy 和 Python numerical 都是 Python 生态，范式差异较小。MATH 上 SC5_Python 甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。 CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40， 考虑 CRD 额外的 diagnosis prompt 开销后正好 40%。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy 交叉验证\",\n    \"description\": \"DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比， 计算 Cohen's κ。验证 taxonomy 跨模型稳定性。\\n\",\n    \"results\": {\n      \"n_classified\": 75,\n      \"cohens_kappa\": 0.67,\n      \"kappa_CI\": \"[0.54, 0.80]\",\n      \"agreement_by_type\": {\n        \"logic_error\": \"78.8%\",\n        \"negation_error\": \"72.7%\",\n        \"exec_crash\": \"90.9%\",\n        \"quantifier_error\": \"50.0%\"\n      },\n      \"deepseek_type_distribution\": {\n        \"logic_error\": \"28.0%\",\n        \"negation_error\": \"12.0%\",\n        \"exec_crash\": \"6.7%\",\n        \"quantifier_error\": \"1.3%\",\n        \"unclassified\": \"4.0%\"\n      },\n      \"distribution_stability\": \"rank order preserved (logic > negation > crash > quantifier)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)\",\n        \"columns\": [\n          \"Error Type\",\n          \"Qwen3-32B %\",\n          \"DeepSeek %\",\n          \"Pairwise Agreement\",\n          \"κ contribution\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            \"25.5%\",\n            \"28.0%\",\n            \"78.8%\",\n            \"0.71\"\n          ],\n          [\n            \"negation_error\",\n            \"10.8%\",\n            \"12.0%\",\n            \"72.7%\",\n            \"0.62\"\n          ],\n          [\n            \"exec_crash\",\n            \"5.4%\",\n            \"6.7%\",\n            \"90.9%\",\n            \"0.88\"\n          ],\n          [\n            \"quantifier_error\",\n            \"2.0%\",\n            \"1.3%\",\n            \"50.0%\",\n            \"0.45\"\n          ],\n          [\n            \"Overall κ\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"0.67\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明 taxonomy 不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。 rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现， 说明四类错误反映了 formalization 的真实失败模式。\\n\\n\\n在 best 档位下，Cohen's κ=0.67 落在 [0.60, 0.80] range，达到 \\\"substantial agreement\\\" 标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有 模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非 taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。 quantifier_error 一致性最低（50%）因为 n 太小（仅 4 样本）且量词错误判断需要 深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致 （logic > negation > crash > quantifier），说明 taxonomy 反映的是错误结构而非 模型偏好。DeepSeek 的 logic_error 比例略高（28% vs 25.5%）、unclassified 略低 （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。\\n\"\n  },\n  {\n    \"name\": \"Qwen3-8B 消融\",\n    \"description\": \"低能力模型上的诊断率和分歧率变化。P2 优先级。\\n\",\n    \"results\": {\n      \"n\": 204,\n      \"C1_disagree_rate\": \"55.4%\",\n      \"C2_diagnostic_rate\": \"74.5%\",\n      \"asymmetry\": \"2.8:1 (FOL-favored, compressed)\",\n      \"fol_accuracy\": \"58.3%\",\n      \"code_accuracy\": \"47.1%\",\n      \"C4_aggregate\": \"+2.1pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Model Scale Ablation on FOLIO\",\n        \"columns\": [\n          \"Model\",\n          \"C1\",\n          \"C2\",\n          \"Asymmetry\",\n          \"FOL Acc\",\n          \"Code Acc\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B\",\n            \"42.2%\",\n            \"87.2%\",\n            \"5.6:1\",\n            \"78.4%\",\n            \"59.8%\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"55.4%\",\n            \"74.5%\",\n            \"2.8:1\",\n            \"58.3%\",\n            \"47.1%\"\n          ],\n          [\n            \"DeepSeek V4 Pro\",\n            \"38.7%\",\n            \"83.5%\",\n            \"4.2:1\",\n            \"81.2%\",\n            \"64.7%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增， C1 单调递减——完美的 scaling story。论文 1 段 discussion 即可，不需要更多。\\n\\n\\n在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧）， 但 C2 降至 74.5%（更多分歧来自\\\"两侧都错\\\"的 correlated failure，诊断性下降）。 这个 C1↑C2↓ 的 tradeoff 是 model-capability 对 CRD 有效性的重要 characterization： 存在一个能力下限，低于此 CRD 的诊断价值被 correlated failure 侵蚀。 不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。 作为 P2 实验，这提供了有价值的 scaling 分析但不影响核心 claim。\\n\"\n  },\n  {\n    \"name\": \"GPQA Diamond 扩展\",\n    \"description\": \"科学知识推理，SymPy/Python 双可执行表征。P2 优先级。\\n\",\n    \"results\": {\n      \"n\": 150,\n      \"C1_disagree_rate\": \"22.0%\",\n      \"C2_diagnostic_rate\": \"72.7%\",\n      \"asymmetry\": \"1.4:1 (slight Python-favored)\",\n      \"note\": \"C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: Cross-Domain CRD Effectiveness\",\n        \"columns\": [\n          \"Domain\",\n          \"Benchmark\",\n          \"C1\",\n          \"C2\",\n          \"Primary Error Source\"\n        ],\n        \"rows\": [\n          [\n            \"Logic\",\n            \"FOLIO\",\n            \"42.2%\",\n            \"87.2%\",\n            \"Formalization\"\n          ],\n          [\n            \"Logic\",\n            \"LogiQA\",\n            \"34.0%\",\n            \"81.5%\",\n            \"Formalization\"\n          ],\n          [\n            \"Math\",\n            \"MATH L5\",\n            \"28.5%\",\n            \"76.0%\",\n            \"Computation\"\n          ],\n          [\n            \"Science\",\n            \"GPQA\",\n            \"22.0%\",\n            \"72.7%\",\n            \"Knowledge gap\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。 这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了 CRD 的机制和边界。 但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。\\n\\n在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization， 两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。 这是 CRD 适用边界的有价值 characterization：cross-representation disagreement 对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。 作为 P2 可选实验，如果时间不够可以省略，核心三基准已足够。\\n\"\n  }\n]",
      "numLines": 1020,
      "startLine": 1,
      "totalLines": 1020
    }
  },
  "sourceToolAssistantUUID": "d9f54bf3-973b-41ed-aa7e-f0557f61288b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T07:34:19.698Z_

<details><summary>↩ Tool result · `toolu_01W2AmuFTHkTHVng8RUcANPP`</summary>

```text
1	# Paper Framing — cross_representation_disagreement_diagno
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (10 days)
7	- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage
8	
9	## Core Insight
10	When the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This "disagreement as diagnostic" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.
11	
12	## Core Claims (3 条)
13	
14	### Claim 1: Disagreement as High-Precision Diagnostic Signal
15	When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.
16	
17	**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).
18	
19	### Claim 2: Error Classification and Conditional Localization
20	Disagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.
21	
22	**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return "ambiguous" (especially Unknown: 61%). C3=4 error types.
23	
24	**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.
25	
26	**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled "the error."
27	
28	### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral
29	Diagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:
30	
31	| GT Label | n | Targeted | Blind | Delta | Interpretation |
32	|----------|---|----------|-------|-------|----------------|
33	| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |
34	| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |
35	| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |
36	
37	This is NOT simply "conditional advantage" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal ("Code disagrees with FOL") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.
38	
39	**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.
40	
41	**Presentation strategy**: 
42	1. Report C4 stratified by GT label as the PRIMARY result (table above)
43	2. Aggregate C4 only as context, with explicit caveat about non-significance
44	3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness
45	4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)
46	
47	## Story Spine
48	
49	- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.
50	
51	- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.
52	
53	- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).
54	
55	- **Headline result template**: "On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation."
56	
57	## Venue Fit
58	
59	- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.
60	- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.
61	- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.
62	
63	## Anticipated Reviewer Concerns & Responses
64	
65	| # | Concern | Response Strategy | Required Experiment |
66	|---|---------|-------------------|---------------------|
67	| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |
68	| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |
69	| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |
70	| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |
71	| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |
72	| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |
73	| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |
74	| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |
75	| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |
76	| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as "cross-representation" is imprecise | Frame MATH domain as "cross-executable-paradigm" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |
77	| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea6d34c3-ff96-44af-950e-00c5ef3b6cc5",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "70b73aa5-2ad5-4f72-b1b5-64a77936925e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md",
      "content": "# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \"disagreement as diagnostic\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Error Classification and Conditional Localization\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\n\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \"ambiguous\" (especially Unknown: 61%). C3=4 error types.\n\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\n\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \"the error.\"\n\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\n\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\n|----------|---|----------|-------|-------|----------------|\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\n\nThis is NOT simply \"conditional advantage\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\"Code disagrees with FOL\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\n\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\n\n**Presentation strategy**: \n1. Report C4 stratified by GT label as the PRIMARY result (table above)\n2. Aggregate C4 only as context, with explicit caveat about non-significance\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \"cross-representation\" is imprecise | Frame MATH domain as \"cross-executable-paradigm\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  },
  "sourceToolAssistantUUID": "ea6d34c3-ff96-44af-950e-00c5ef3b6cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T07:34:19.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W2AmuFTHkTHVng8RUcANPP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820fb6e1-7309-449a-a934-0b56fec2d953",
  "isSidechain": false,
  "requestId": "req_011Cb3y5vXHEK9aKSUipLyRJ",
  "type": "assistant",
  "uuid": "ea6d34c3-ff96-44af-950e-00c5ef3b6cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bs7NjfyD4btGamTXgcZgwa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11281
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representati…",
  "leafUuid": "70b73aa5-2ad5-4f72-b1b5-64a77936925e",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement for model diagnosis",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Assistant

_source line 14 · 2026-05-15T07:34:28.667Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write the full LaTeX paper. I need to ensure the output directory exists first, then write the paper.

Let me organize the paper structure:

1. Abstract
2. Introduction
3. Related Work
4. Method (Cross-Representation Disagreement Diagnosis)
5. Experiments
   - Setup (benchmarks, models)
   - Exp 1: FOLIO core analysis (C1-C5)
   - Exp 2: Cross-model ablation
   - Exp 3: LogiQA extension (+ ProofWriter pilot)
   - Exp 4: MATH Level 5 extension
   - Exp 5: Multi-round repair
   - Exp 6: Unknown sample analysis + correlated failure
   - Exp 7: Selection vs repair ablation
   - Exp 8: Taxonomy ablation
   - Exp 9: Statistical significance
   - Exp 10: Self-consistency baseline
   - Exp 11: Cross-model taxonomy validation
   - Exp 12: Qwen3-8B scale ablation
   - Exp 13: GPQA Diamond extension
6. Discussion
7. Conclusion

Now I'll write out the complete paper with all these sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b73aa5-2ad5-4f72-b1b5-64a77936925e",
  "isSidechain": false,
  "requestId": "req_011Cb3y6HnhyncX4ywNyXXae",
  "type": "assistant",
  "uuid": "3a9e10af-c8ba-4c62-9cec-a21aa75dc715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J6pU1XsNJhgud3N6PKUsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20080,
      "cache_read_input_tokens": 23122,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 20080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20080
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

_source line 15 · 2026-05-15T07:34:28.672Z_

Now let me ensure the output directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a9e10af-c8ba-4c62-9cec-a21aa75dc715",
  "isSidechain": false,
  "requestId": "req_011Cb3y6HnhyncX4ywNyXXae",
  "type": "assistant",
  "uuid": "482a90a2-bfb7-4c1c-b667-a12352566ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J6pU1XsNJhgud3N6PKUsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20080,
      "cache_read_input_tokens": 23122,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 20080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20080
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

_source line 16 · 2026-05-15T07:34:29.968Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PGuuxm69nYBEHDTc69VsyG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "482a90a2-bfb7-4c1c-b667-a12352566ae3",
  "isSidechain": false,
  "requestId": "req_011Cb3y6HnhyncX4ywNyXXae",
  "type": "assistant",
  "uuid": "fbdae1b9-d2df-4e30-bec4-8a3e98b20896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J6pU1XsNJhgud3N6PKUsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20080,
      "cache_read_input_tokens": 23122,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 443,
          "cache_read_input_tokens": 23122,
          "cache_creation_input_tokens": 20080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20080
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

_source line 17 · 2026-05-15T07:34:30.258Z_

<details><summary>↩ Tool result · `toolu_01PGuuxm69nYBEHDTc69VsyG`</summary>

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
  "parentUuid": "fbdae1b9-d2df-4e30-bec4-8a3e98b20896",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "d9f91dce-ab38-48f7-a2ee-7681b0bee12a",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fbdae1b9-d2df-4e30-bec4-8a3e98b20896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T07:38:45.196Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AvJjhDBMX4aRB6ZddNpJyG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\newcommand{\\method}{CRD}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{Cross-Representation Disagreement as a Diagnostic Signal\\\\for LLM Reasoning Errors}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic with Z3 verification and executable Python---disagreements between the outputs serve as a high-precision diagnostic signal. On three benchmarks (FOLIO, LogiQA, MATH Level~5) and two models (Qwen3-32B, DeepSeek~V4~Pro), we show that cross-representation disagreement (CRD) detects errors with 76--87\\% diagnostic precision at 28--42\\% disagreement rates, using only 40\\% of the token cost of $k\\!=\\!5$ self-consistency. We contribute a four-type error taxonomy validated across models (Cohen's $\\kappa\\!=\\!0.67$), reveal a GT-label-dependent repair effect where diagnosis helps for uncertain cases (+22.1\\pp{} on GT=Unknown) but hurts for true cases ($-$11.2\\pp{} overcorrection), and demonstrate that asymmetry direction reverses across domains---FOL-favored in logic (5.6:1), Code-favored in math (1.8:1)---indicating that disagreement patterns reflect domain-specific representation strengths rather than fixed verifier superiority.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nNeurosymbolic reasoning pipelines increasingly rely on LLMs to translate natural language into formal executable representations~\\cite{pan2023logiclm,ye2024satlm}. The dominant failure mode is not the symbolic solver but the LLM's formalization: subtle corruptions introduced during translation from natural language to formal representation~\\cite{olausson2023linc}. Detecting these errors is difficult because the formal output is syntactically valid and the solver returns a definitive answer, masking upstream formalization errors.\n\nCurrent approaches to this problem fall into three categories: (1)~\\emph{selection} methods that choose among representations based on confidence~\\cite{li2024hybridmind,sun2024adaptive}, (2)~\\emph{within-representation verification} that checks consistency within a single paradigm~\\cite{weng2023vericot,kang2025verge,zhong2025roundtrip}, and (3)~\\emph{cross-representation filtering} that discards samples where two formalizations disagree~\\cite{liang2024cotpot,prove2024}. None of these exploit the diagnostic information \\emph{within} the disagreement pattern itself---what type of error caused the disagreement, which representation is likely wrong, and how to repair it.\n\nWe present \\textbf{Cross-Representation Disagreement Diagnosis (\\method{})}, an analysis framework and lightweight repair method that extends cross-representation disagreement from a binary filtering signal to a structured diagnostic tool. Given a reasoning problem, we generate two executable formalizations (FOL+Z3 and Python), execute both, and when they disagree, classify the error type, localize the faulty representation via stability testing, and optionally perform diagnosis-guided repair. Our three claims:\n\n\\begin{enumerate}\n\\item \\textbf{Disagreement as high-precision diagnostic signal.} Cross-representation disagreement occurs at 28--42\\% rates across benchmarks and is diagnostically informative with 76--87\\% precision---substantially higher than $k\\!=\\!5$ single-representation self-consistency (71--79\\%) at 40\\% of the token cost.\n\n\\item \\textbf{Structured error taxonomy with prescriptive value.} Disagreement patterns enable classification into four error types (logic\\_error, negation\\_error, exec\\_crash, quantifier\\_error). This taxonomy is stable across models ($\\kappa\\!=\\!0.67$) and has prescriptive value: taxonomy-guided repair outperforms fixed-strategy repair by +5.0\\pp{} ($p\\!=\\!0.042$).\n\n\\item \\textbf{GT-label-dependent repair effect.} Diagnosis-guided repair exhibits a striking asymmetry: it substantially helps for GT=Unknown (+22.1\\pp{}) and GT=False (+10.4\\pp{}) cases but \\emph{hurts} for GT=True cases ($-$11.2\\pp{}). The aggregate masks a three-way split that is the actual finding. We characterize this as a fundamental boundary of cross-representation diagnosis.\n\\end{enumerate}\n\nOur primary contribution is the systematic analysis of cross-representation disagreement as a diagnostic signal across domains and models. The repair framework demonstrates downstream utility but is secondary to the analytical findings. We release all experimental data and analysis code.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Neurosymbolic Reasoning.}\nLogic-LM~\\cite{pan2023logiclm} and LINC~\\cite{olausson2023linc} translate NL to FOL for symbolic solving. SatLM~\\cite{ye2024satlm} uses SAT solvers. These methods use a single representation and cannot detect formalization errors through cross-representation comparison.\n\n\\paragraph{Cross-Representation Filtering.}\nLiang et al.~\\cite{liang2024cotpot} showed CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements---no error categorization, no repair. PROVE~\\cite{prove2024} similarly filters but does not diagnose. Our work extends filtering to structured diagnosis.\n\n\\paragraph{Within-Representation Verification.}\nVeriCoT~\\cite{weng2023vericot} and VERGE~\\cite{kang2025verge} verify reasoning chains within a single paradigm. Roundtrip Verification~\\cite{zhong2025roundtrip} demonstrated diagnosis-guided repair within one representation on a narrow domain (150 traffic rules). We extend to cross-representation diagnosis across multiple domains.\n\n\\paragraph{Self-Consistency and Ensemble Methods.}\nSelf-consistency~\\cite{wang2023selfconsistency} uses $k$ samples from the same prompt for majority voting. Multi-agent debate~\\cite{du2023debate,liang2023debate} and LEVER~\\cite{ni2023lever} leverage multiple generation attempts. A key distinction: within-representation sampling captures generation variance, while CRD captures systematic paradigm-level differences between formal logic and imperative code.\n\n\\paragraph{Self-Debugging and Refinement.}\nSelf-Debug~\\cite{chen2023selfdebug} and Self-Refine~\\cite{madaan2023selfrefine} use execution feedback for iterative correction within a single representation. Faithful CoT~\\cite{lyu2023faithful} ensures reasoning chains are executable. These operate within one paradigm; CRD uses cross-paradigm disagreement as the diagnostic trigger.\n\n\\paragraph{Adaptive Selection.}\nHybridMind~\\cite{li2024hybridmind} and adaptive selection methods~\\cite{sun2024adaptive} choose between representations based on problem features. They select but do not diagnose or repair. CRD is complementary---it diagnoses \\emph{after} both representations are generated.\n\n\\paragraph{Correlated Failures.}\nDenisov-Blanch~\\cite{denisovblanch2026} raised concerns about correlated failures in ensemble methods. We explicitly quantify the false agreement rate (12.3\\%) and show it varies by GT label, with the lowest correlation ($\\phi\\!=\\!0.098$) on the subset where CRD is most effective (GT=Unknown).\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $x$ with ground-truth label $y \\in \\{\\text{True}, \\text{False}, \\text{Unknown}\\}$, \\method{} proceeds in four stages:\n\n\\begin{enumerate}\n\\item \\textbf{Dual formalization.} Prompt the LLM to produce two executable formalizations: $f_\\text{FOL}(x)$ (first-order logic formula verified by Z3) and $f_\\text{Code}(x)$ (Python program with execution).\n\\item \\textbf{Disagreement detection.} Execute both formalizations and compare outputs. If $f_\\text{FOL}(x) \\neq f_\\text{Code}(x)$, the sample enters the diagnostic pipeline.\n\\item \\textbf{Error classification and localization.} Classify the disagreement into one of four error types using a rule-based taxonomy. Apply a stability test (re-execution with perturbed prompts) to localize the faulty representation.\n\\item \\textbf{Diagnosis-guided repair} (optional). Generate a repair prompt incorporating the diagnosis (error type, suspected faulty side, disagreement pattern) and re-generate the faulty formalization.\n\\end{enumerate}\n\nFor mathematical reasoning, we instantiate the dual representations as SymPy symbolic computation and Python numerical computation, maintaining the cross-executable-paradigm structure.\n\n\\subsection{Error Taxonomy}\n\nWe define four error types based on analysis of disagreement patterns:\n\n\\begin{itemize}\n\\item \\textbf{logic\\_error}: Incorrect predicate definitions, flawed inference chains, or wrong logical connectives in the formalization.\n\\item \\textbf{negation\\_error}: Incorrect handling of negation---either missing negation or spurious double negation.\n\\item \\textbf{exec\\_crash}: Runtime errors in the executable path (syntax errors, undefined variables, solver timeouts).\n\\item \\textbf{quantifier\\_error}: Incorrect scope or type of quantifiers ($\\forall$ vs.\\ $\\exists$) in FOL formalization.\n\\end{itemize}\n\nThe taxonomy is deliberately rule-based for interpretability. We validate its cross-model stability in Section~\\ref{sec:taxonomy_validation}.\n\n\\subsection{Stability-Based Localization}\n\nTo determine which representation contains the error, we apply a stability test: re-run each formalization $k\\!=\\!3$ times with temperature perturbation. If one representation produces consistent outputs while the other fluctuates, the unstable side is localized as the error source. When neither side is clearly unstable, the localization returns ``ambiguous.''\n\nThis yields a high-precision / low-recall localization: when the stability test commits (53\\% of diagnostic cases on FOLIO), accuracy is 94.6\\%. The 47\\% ambiguous rate is primarily driven by GT=Unknown samples where Code overclaiming creates systematically unstable predictions.\n\n\\subsection{Multi-Round Repair}\n\nRepair proceeds for up to 3 rounds. Each round generates a repair prompt incorporating:\n(1)~the error type from the taxonomy,\n(2)~the localized faulty side (if available),\n(3)~the outputs from both representations.\nThe repair prompt is type-specific: logic errors receive prompts targeting predicate and inference chain review; negation errors receive prompts checking polarity; exec\\_crash triggers re-generation; quantifier errors receive prompts reviewing quantifier scope.\n\n\\subsection{Cost Analysis}\n\n\\method{} requires exactly 2 LLM calls for dual formalization (1 FOL + 1 Code), compared to $k\\!=\\!5$ calls for self-consistency. The repair pipeline adds 1--3 calls only for disagreeing samples. Overall token cost is approximately $2/5 = 0.40$ of SC-5, with additional diagnosis tokens for the disagreeing subset.\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Qwen3-32B (primary), DeepSeek V4 Pro (cross-model validation), Qwen3-8B (scale ablation).\n\n\\paragraph{Benchmarks.} (1)~FOLIO~\\cite{han2022folio}: expert-annotated FOL problems, 204 samples, 3-class (True/False/Unknown). (2)~LogiQA~\\cite{liu2021logiqa}: natural language logical reasoning from Chinese civil service exams, 200 samples, 4-way multiple choice. (3)~MATH Level~5~\\cite{hendrycks2021math}: competition mathematics, 200 samples, using SymPy symbolic vs.\\ Python numerical as dual representations. (4)~GPQA Diamond~\\cite{rein2024gpqa}: graduate-level science questions, 150 samples (secondary benchmark).\n\n\\paragraph{Metrics.} C1: disagreement rate. C2: diagnostic rate (fraction of disagreements where at least one side is wrong). C3: number of distinct error types observed. C4: repair delta (accuracy improvement over blind baseline). C5: localization accuracy (committed accuracy and coverage).\n\n% --------------------------------------------------------\n% 4.2 FOLIO Core Analysis\n% --------------------------------------------------------\n\\subsection{FOLIO Core Analysis}\n\\label{sec:folio_core}\n\nTable~\\ref{tab:folio_core} presents the core metrics on FOLIO with Qwen3-32B (204 samples).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Estimate} & \\textbf{95\\% CI} & \\textbf{Gate} \\\\\n\\midrule\nC1 (Disagree Rate) & 42.16\\% & [35.3, 49.0] & $\\geq$15\\% \\\\\nC2 (Diagnostic Rate) & 87.21\\% & [81.3, 94.7] & $\\geq$75\\% \\\\\nC3 (Error Types) & 4 & --- & $\\geq$3 \\\\\nC4 (Repair $\\Delta$) & +4.65\\pp{} & [$-$8.8, +18.1] & n.s. \\\\\nC5 (Committed Acc) & 94.6\\% & [86.1, 100] & --- \\\\\nC5 (Coverage) & 53.0\\% & [41.0, 65.1] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{FOLIO C1--C5 metrics with bootstrap 95\\% CI (Qwen3-32B, $n\\!=\\!204$). C2 lower bound 81.3\\% exceeds the 75\\% threshold, confirming high diagnostic precision.}\n\\label{tab:folio_core}\n\\end{table}\n\nThe disagreement rate of 42.16\\% indicates that a substantial fraction of problems elicit different answers from FOL+Z3 vs.\\ Python execution. Of these disagreements, 87.21\\% are diagnostically informative (at least one side is wrong). The error taxonomy identifies four types, dominated by logic\\_error (25.5\\%), followed by negation\\_error (10.8\\%), exec\\_crash (5.4\\%), and quantifier\\_error (2.0\\%) (Table~\\ref{tab:error_taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Count} & \\textbf{Proportion} \\\\\n\\midrule\nlogic\\_error & 52 & 25.5\\% \\\\\nnegation\\_error & 22 & 10.8\\% \\\\\nexec\\_crash & 11 & 5.4\\% \\\\\nquantifier\\_error & 4 & 2.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error taxonomy distribution on FOLIO disagreement samples.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\nThe representation asymmetry is striking: FOL is correct in 56 disagreement cases vs.\\ Code correct in 10 and both wrong in 10, yielding a 5.6:1 FOL-favored ratio. The phi coefficient between FOL and Code failures is 0.189 ($p\\!=\\!0.007$), indicating low but statistically significant correlation---the representations fail largely independently, with 75\\% of errors being single-sided.\n\n% --------------------------------------------------------\n% 4.3 GT-Label-Dependent Repair Effect\n% --------------------------------------------------------\n\\subsection{GT-Label-Dependent Repair Effect}\n\\label{sec:repair_effect}\n\nThe aggregate C4 of +4.65\\pp{} (Fisher $p\\!=\\!0.626$) is not statistically significant. However, stratification by ground-truth label reveals a three-way split (Table~\\ref{tab:gt_repair}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{GT} & $n$ & \\textbf{Targeted} & \\textbf{Blind} & $\\Delta$ & \\textbf{Interp.} \\\\\n\\midrule\nTrue & 72 & 63.6\\% & 77.3\\% & $-$13.6\\pp{} & Overcorrect \\\\\nFalse & 63 & 76.7\\% & 70.0\\% & +6.7\\pp{} & Modest help \\\\\nUnknown & 69 & 67.7\\% & 52.9\\% & +14.7\\pp{} & Diagnosis helps \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GT-label-stratified repair effect on FOLIO (Round 1). Aggregate non-significance masks a three-way split.}\n\\label{tab:gt_repair}\n\\end{table}\n\nThe GT=Unknown subset benefits most from diagnosis because Python's Code path lacks native three-valued logic and tends to overclaim True or False (78.3\\% overclaiming rate). When CRD diagnosis reveals that FOL returned Unknown, the repair prompt helps the model recognize insufficient evidence. GT=True overcorrection occurs because when Code erroneously outputs False/Unknown, the diagnostic signal triggers the model to move away from True.\n\n% --------------------------------------------------------\n% 4.4 Multi-Round Repair\n% --------------------------------------------------------\n\\subsection{Multi-Round Repair}\n\\label{sec:multiround}\n\nTable~\\ref{tab:multiround} shows how repair delta evolves across three rounds with error-type-specific prompts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GT Label} & $n$ & \\textbf{Rd.~1 $\\Delta$} & \\textbf{Rd.~3 $\\Delta$} & \\textbf{Improv.} \\\\\n\\midrule\nUnknown & 69 & +14.7\\pp{} & +22.1\\pp{} & +7.4\\pp{} \\\\\nFalse & 63 & +6.7\\pp{} & +10.4\\pp{} & +3.7\\pp{} \\\\\nTrue & 72 & $-$13.6\\pp{} & $-$11.2\\pp{} & +2.4\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-round repair results on FOLIO. GT=Unknown $\\Delta$ rises from +14.7 to +22.1\\pp{}; GT=True overcorrection partially mitigated but remains negative.}\n\\label{tab:multiround}\n\\end{table}\n\nMulti-round repair exhibits diminishing returns (Round~2: 8 additional fixes, Round~3: 3), confirming that type-specific strategies provide incremental value. Table~\\ref{tab:repair_by_type} breaks down repair success by error type.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Attempted} & \\textbf{Fixed} & \\textbf{Success} \\\\\n\\midrule\nlogic\\_error & 41 & 28 & 68.3\\% \\\\\nnegation\\_error & 18 & 13 & 72.0\\% \\\\\nexec\\_crash & 11 & 9 & 81.8\\% \\\\\nquantifier\\_error & 4 & 2 & 50.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Repair success rate by error type (Round 3, FOLIO). exec\\_crash is easiest to fix; quantifier\\_error is hardest.}\n\\label{tab:repair_by_type}\n\\end{table}\n\n% --------------------------------------------------------\n% 4.5 Cross-Model Ablation\n% --------------------------------------------------------\n\\subsection{Cross-Model Ablation}\n\\label{sec:cross_model}\n\nTo verify that CRD properties are not specific to Qwen3-32B, we test three conditions on FOLIO (Table~\\ref{tab:cross_model}): (a)~Qwen3-32B within-model (MVP), (b)~DeepSeek V4 Pro within-model, and (c)~DeepSeek~FOL + Qwen~Code cross-model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{C1} & \\textbf{C2} & \\textbf{C2 CI} & \\textbf{Asym.} \\\\\n\\midrule\nQwen within & 42.2\\% & 87.2\\% & [81.3, 94.7] & 5.6:1 FOL \\\\\nDeepSeek within & 38.7\\% & 83.5\\% & [74.2, 91.8] & 4.2:1 FOL \\\\\nDS$\\times$Qwen cross & 47.5\\% & 80.9\\% & [71.8, 89.1] & 3.8:1 FOL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model ablation on FOLIO ($n\\!=\\!204$). C2 remains above 80\\% across conditions. Asymmetry direction is consistently FOL-favored.}\n\\label{tab:cross_model}\n\\end{table}\n\nDeepSeek within-model C2 (83.5\\%) falls within $\\pm$8\\pp{} of Qwen (87.2\\%), confirming that diagnostic precision is a structural property of cross-representation disagreement rather than model-specific. The cross-model condition shows higher C1 (47.5\\%) because different models' formalization biases increase disagreement probability, but slightly lower C2 (80.9\\%) because some disagreement arises from capability differences rather than formalization errors. The GT-label-dependent repair effect replicates: DeepSeek shows +12.1\\pp{} on GT=Unknown and $-$10.3\\pp{} on GT=True.\n\n% --------------------------------------------------------\n% 4.6 Cross-Benchmark Generalization\n% --------------------------------------------------------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_benchmark}\n\n\\paragraph{LogiQA.} We first piloted ProofWriter ($n\\!=\\!30$) but found only 6.7\\% disagreement rate---synthetic data is too regular for CRD to be informative (both FOL and Code achieve $>$90\\% accuracy). We switched to LogiQA, a natural-language logic benchmark derived from Chinese civil service exams. Table~\\ref{tab:logiqa} compares LogiQA with FOLIO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LogiQA} & \\textbf{FOLIO} & $\\Delta$ \\\\\n\\midrule\nC1 (Disagree Rate) & 34.0\\% & 42.2\\% & $-$8.2\\pp{} \\\\\nC2 (Diagnostic Rate) & 81.5\\% & 87.2\\% & $-$5.7\\pp{} \\\\\nC3 (Error Types) & 4 & 4 & --- \\\\\nC5 Committed Acc & 91.2\\% & 94.6\\% & $-$3.4\\pp{} \\\\\nAsymmetry & 3.2:1 FOL & 5.6:1 FOL & narrower \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LogiQA results ($n\\!=\\!200$, Qwen3-32B) vs.\\ FOLIO reference. C2 remains above 80\\%; the GT-stratified repair effect replicates.}\n\\label{tab:logiqa}\n\\end{table}\n\nLogiQA C2 of 81.5\\% (CI: [73.8\\%, 88.2\\%]) confirms cross-benchmark stability. The narrower asymmetry (3.2:1 vs.\\ 5.6:1) reflects LogiQA's propositional logic being less demanding than FOLIO's first-order logic, reducing FOL's relative advantage.\n\n\\paragraph{ProofWriter pilot failure.} The 6.7\\% pilot disagreement rate on ProofWriter (Table~\\ref{tab:proofwriter_pilot}) is itself informative: CRD requires natural-language formalization challenges to produce a useful disagreement signal. Synthetic benchmarks with regular structure are well-handled by both representations, limiting CRD's applicability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Gate} & \\textbf{Decision} \\\\\n\\midrule\nDisagree Rate & 6.7\\% & $\\geq$10\\% & FAIL \\\\\nFOL Accuracy & 93.3\\% & --- & --- \\\\\nCode Accuracy & 90.0\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ProofWriter pilot ($n\\!=\\!30$). High accuracy on both paths yields insufficient disagreement for CRD.}\n\\label{tab:proofwriter_pilot}\n\\end{table}\n\n\\paragraph{MATH Level 5.} We extend CRD to mathematical reasoning using SymPy symbolic computation vs.\\ Python numerical computation as dual executable representations (Table~\\ref{tab:math}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{MATH} & \\textbf{FOLIO} & \\textbf{LogiQA} \\\\\n\\midrule\nC1 & 28.5\\% & 42.2\\% & 34.0\\% \\\\\nC2 & 76.0\\% & 87.2\\% & 81.5\\% \\\\\nC3 & 3 & 4 & 4 \\\\\nAsymmetry & 1.8:1 Code & 5.6:1 FOL & 3.2:1 FOL \\\\\nC5 Committed & 88.5\\% & 94.6\\% & 91.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MATH Level~5 results ($n\\!=\\!200$, Qwen3-32B). Asymmetry direction \\emph{reverses}: Python numerical outperforms SymPy symbolic, contrasting with FOL-favored logic benchmarks.}\n\\label{tab:math}\n\\end{table}\n\nThe asymmetry reversal is a key finding (Table~\\ref{tab:asymmetry_direction}). In logic, FOL+Z3's formal verification guarantee gives it a systematic advantage. In mathematics, Python's flexible numerical methods are more robust than SymPy's symbolics (SymPy crash rate 12.5\\% vs.\\ Python 4.0\\%). This proves that CRD captures \\emph{domain-specific representation strengths}, not a fixed verifier hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llllc}\n\\toprule\n\\textbf{Domain} & \\textbf{Rep.\\ A} & \\textbf{Rep.\\ B} & \\textbf{Favored} & \\textbf{Ratio} \\\\\n\\midrule\nLogic (FOLIO) & FOL+Z3 & Python & FOL & 5.6:1 \\\\\nLogic (LogiQA) & FOL+Z3 & Python & FOL & 3.2:1 \\\\\nMath (MATH) & SymPy & Python & Python & 1.8:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Asymmetry direction across domains. The reversal from FOL-favored (logic) to Code-favored (math) reflects representation-task fit.}\n\\label{tab:asymmetry_direction}\n\\end{table}\n\n% --------------------------------------------------------\n% 4.7 Correlated Failure Analysis\n% --------------------------------------------------------\n\\subsection{Correlated Failure Analysis}\n\\label{sec:correlated}\n\nA natural concern is correlated failures: if both representations fail on the same samples, disagreement underestimates the true error rate. Table~\\ref{tab:correlated} quantifies this.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GT} & $n$ & $\\phi$ & \\textbf{False Agr.} & \\textbf{Code Overcl.} \\\\\n\\midrule\nTrue & 72 & 0.245 & 19.4\\% & N/A \\\\\nFalse & 63 & 0.162 & 11.1\\% & N/A \\\\\nUnknown & 69 & 0.098 & 5.8\\% & 78.3\\% \\\\\n\\midrule\nOverall & 204 & 0.189 & 12.3\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlated failure analysis by GT label. GT=Unknown has the lowest failure correlation ($\\phi\\!=\\!0.098$) and highest Code overclaiming (78.3\\%), explaining why CRD is most effective on this subset.}\n\\label{tab:correlated}\n\\end{table}\n\nThe overall false agreement rate is 12.3\\%---relatively low, and lowest on GT=Unknown (5.8\\%) where CRD repair delta is highest. The phi coefficient is 0.189 overall ($p\\!=\\!0.007$), falling in the range where representations are independent enough to generate complementary signals but not so independent that disagreement is noise. Specification errors (ambiguity in the original problem) account for only 8.3\\% of cases, confirming that most errors are formalization-specific.\n\n% --------------------------------------------------------\n% 4.8 Selection vs Repair Ablation\n% --------------------------------------------------------\n\\subsection{Selection vs.\\ Repair Ablation}\n\\label{sec:selection_repair}\n\nAfter detecting disagreement and localizing the error side, should one simply \\emph{select} the other side, or \\emph{repair} the faulty one? Table~\\ref{tab:selection_repair} compares on the GT$\\neq$True subset ($n\\!=\\!132$), where diagnosis is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{All} & \\textbf{logic} & \\textbf{neg.} & \\textbf{crash} & \\textbf{quant.} \\\\\n\\midrule\nBlind & 61.4 & 56.1 & 66.7 & 72.7 & 25.0 \\\\\nSelection & 72.7 & 70.7 & 77.8 & 90.9 & 50.0 \\\\\nRepair (Rd.~3) & 76.2 & 75.6 & 77.8 & 90.9 & 75.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ Repair on GT$\\neq$True subset (FOLIO, $n\\!=\\!132$). All values are accuracy (\\%). Selection already yields +11.3\\pp{} over blind; repair adds +3.5\\pp{}, concentrated on logic\\_error and quantifier\\_error.}\n\\label{tab:selection_repair}\n\\end{table}\n\nSelection alone provides +11.3\\pp{} over blind baseline, demonstrating that CRD's diagnostic value is substantial even without repair. Repair adds +3.5\\pp{} on top, with the advantage concentrated on logic\\_error (+4.9\\pp{}) and quantifier\\_error (+25.0\\pp{})---error types where both sides may be partially correct, making simple selection insufficient.\n\n% --------------------------------------------------------\n% 4.9 Taxonomy Ablation\n% --------------------------------------------------------\n\\subsection{Taxonomy-Guided vs.\\ Fixed-Strategy Repair}\n\\label{sec:taxonomy_ablation}\n\nTo test the prescriptive value of the error taxonomy, we compare taxonomy-guided repair (type-specific prompts) against a fixed strategy (uniform re-generation) in Table~\\ref{tab:taxonomy_ablation}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & $n$ & \\textbf{Guided} & \\textbf{Fixed} & $\\Delta$ \\\\\n\\midrule\nlogic\\_error & 41 & 75.6\\% & 69.4\\% & +6.2\\pp{} \\\\\nnegation\\_error & 18 & 77.8\\% & 75.5\\% & +2.3\\pp{} \\\\\nexec\\_crash & 11 & 90.9\\% & 90.9\\% & +0.0\\pp{} \\\\\nquantifier\\_error & 4 & 75.0\\% & 57.0\\% & +18.0\\pp{} \\\\\n\\midrule\nOverall & 74 & 76.2\\% & 71.2\\% & +5.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy-guided vs.\\ fixed-strategy repair (FOLIO, GT$\\neq$True). Overall $\\Delta\\!=\\!$+5.0\\pp{} (McNemar $p\\!=\\!0.042$). exec\\_crash shows no difference (re-generation is already optimal); quantifier\\_error shows the largest gap.}\n\\label{tab:taxonomy_ablation}\n\\end{table}\n\nThe +5.0\\pp{} overall advantage is statistically significant (McNemar $p\\!=\\!0.042$). The taxonomy's prescriptive value is concentrated on errors requiring targeted understanding: logic\\_error (+6.2\\pp{}, prompts targeting predicate and inference chain review) and quantifier\\_error (+18.0\\pp{}, prompts reviewing quantifier scope). exec\\_crash shows zero difference because re-generation is inherently the correct strategy regardless of diagnosis.\n\n% --------------------------------------------------------\n% 4.10 Cross-Model Taxonomy Validation\n% --------------------------------------------------------\n\\subsection{Cross-Model Taxonomy Validation}\n\\label{sec:taxonomy_validation}\n\nTo validate that the error taxonomy is not an artifact of a single model's classification, we have DeepSeek V4 Pro independently classify the same 75 diagnostic FOLIO samples (Table~\\ref{tab:taxonomy_validation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Qwen} & \\textbf{DS} & \\textbf{Agree} & $\\kappa$ \\\\\n\\midrule\nlogic\\_error & 25.5\\% & 28.0\\% & 78.8\\% & 0.71 \\\\\nnegation\\_error & 10.8\\% & 12.0\\% & 72.7\\% & 0.62 \\\\\nexec\\_crash & 5.4\\% & 6.7\\% & 90.9\\% & 0.88 \\\\\nquantifier\\_error & 2.0\\% & 1.3\\% & 50.0\\% & 0.45 \\\\\n\\midrule\nOverall $\\kappa$ & --- & --- & --- & 0.67 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model taxonomy validation ($n\\!=\\!75$). Cohen's $\\kappa\\!=\\!0.67$ (CI: [0.54, 0.80]) indicates substantial agreement. Rank order of error types is preserved across models.}\n\\label{tab:taxonomy_validation}\n\\end{table}\n\nCohen's $\\kappa\\!=\\!0.67$ (CI: [0.54, 0.80]) reaches ``substantial agreement.'' The rank order of error types is identical across models (logic $>$ negation $>$ crash $>$ quantifier), suggesting the taxonomy captures genuine structural failure modes rather than model-specific artifacts. exec\\_crash achieves the highest agreement (90.9\\%) due to its objective verifiability; quantifier\\_error the lowest (50.0\\%) due to small sample size ($n\\!=\\!4$).\n\n% --------------------------------------------------------\n% 4.11 Self-Consistency Baseline\n% --------------------------------------------------------\n\\subsection{CRD vs.\\ Self-Consistency}\n\\label{sec:sc_baseline}\n\nWe compare single-pass CRD against $k\\!=\\!5$ self-consistency (majority vote) within each representation (Table~\\ref{tab:crd_vs_sc}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{SC5-FOL} & \\textbf{SC5-Code} & \\textbf{CRD} & $\\Delta$ & \\textbf{Cost} \\\\\n\\midrule\nFOLIO & 79.3 & 72.1 & 87.2 & +7.9 & 0.40 \\\\\nLogiQA & 75.8 & 69.4 & 81.5 & +5.7 & 0.40 \\\\\nMATH & 71.2 & 74.8 & 76.0 & +1.2 & 0.40 \\\\\n\\midrule\nAvg. & 75.4 & 72.1 & 81.6 & +4.9 & 0.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD vs.\\ $k\\!=\\!5$ self-consistency. All values are diagnostic precision (\\%); $\\Delta$ is CRD minus best SC5; Cost is CRD token ratio vs.\\ SC5. CRD Pareto-dominates: higher precision at 40\\% of the cost.}\n\\label{tab:crd_vs_sc}\n\\end{table}\n\nCRD Pareto-dominates $k\\!=\\!5$ self-consistency: +4.9\\pp{} average precision at 40\\% token cost. The advantage is largest on FOLIO (+7.9\\pp{}), where FOL and Python represent maximally different paradigms, and smallest on MATH (+1.2\\pp{}), where SymPy and Python numerical are both Python-ecosystem tools with smaller paradigm distance. On FOLIO, the precision gap is statistically significant (McNemar $p\\!=\\!0.031$). This result supports the thesis that cross-representation disagreement captures paradigm-level differences---fundamentally more informative than within-representation sampling variance.\n\n% --------------------------------------------------------\n% 4.12 Model Scale Ablation\n% --------------------------------------------------------\n\\subsection{Model Scale Ablation}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} compares three models on FOLIO, forming a capability gradient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{C1} & \\textbf{C2} & \\textbf{Asym.} & \\textbf{FOL} & \\textbf{Code} \\\\\n\\midrule\nQwen3-8B & 55.4 & 74.5 & 2.8:1 & 58.3 & 47.1 \\\\\nQwen3-32B & 42.2 & 87.2 & 5.6:1 & 78.4 & 59.8 \\\\\nDeepSeek Pro & 38.7 & 83.5 & 4.2:1 & 81.2 & 64.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model scale ablation on FOLIO. C1 and C2 show inverse scaling: weaker models produce more disagreements (C1$\\uparrow$) but with lower diagnostic value (C2$\\downarrow$). FOL and Code columns show individual path accuracy (\\%).}\n\\label{tab:scale}\n\\end{table}\n\nWeaker models produce more disagreements (C1: 55.4\\% for 8B vs.\\ 42.2\\% for 32B) but with lower diagnostic value (C2: 74.5\\% vs.\\ 87.2\\%). The 8B model's C2 of 74.5\\% approaches the lower bound of usefulness---below some capability threshold, correlated failures (both sides wrong) begin to dominate disagreement, eroding diagnostic precision. The asymmetry ratio compresses from 5.6:1 to 2.8:1 because FOL accuracy degrades faster with model scale (formal logic is more capability-sensitive), reducing the structural advantage.\n\n% --------------------------------------------------------\n% 4.13 Cross-Domain Boundary (GPQA)\n% --------------------------------------------------------\n\\subsection{Cross-Domain Boundary: GPQA Diamond}\n\\label{sec:gpqa}\n\nTo characterize the boundary of CRD's applicability, we test on GPQA Diamond, a graduate-level science reasoning benchmark (Table~\\ref{tab:cross_domain}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Benchmark} & \\textbf{C1} & \\textbf{C2} & \\textbf{Error Source} \\\\\n\\midrule\nLogic & FOLIO & 42.2 & 87.2 & Formalization \\\\\nLogic & LogiQA & 34.0 & 81.5 & Formalization \\\\\nMath & MATH L5 & 28.5 & 76.0 & Computation \\\\\nScience & GPQA & 22.0 & 72.7 & Knowledge gap \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD effectiveness across domains. C2 decreases monotonically as the primary error source shifts from formalization to knowledge gaps. CRD is most effective when errors arise from the translation to formal representation, not from missing domain knowledge.}\n\\label{tab:cross_domain}\n\\end{table}\n\nThe four benchmarks form a clear domain gradient: C2 decreases from 87.2\\% (pure logic) through 81.5\\% and 76.0\\% to 72.7\\% (science) as the primary error source shifts from formalization errors to domain knowledge gaps. CRD's diagnostic power derives from detecting formalization-specific errors; when the model lacks the domain knowledge to formalize correctly in \\emph{any} representation, disagreement provides weaker signal.\n\n% --------------------------------------------------------\n% 4.14 Statistical Significance\n% --------------------------------------------------------\n\\subsection{Statistical Significance}\n\\label{sec:significance}\n\nTable~\\ref{tab:significance} summarizes significance tests across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llllcl}\n\\toprule\n\\textbf{Test} & \\textbf{Bench.} & \\textbf{Metric} & \\textbf{Effect} & $p$ & \\textbf{Sig.} \\\\\n\\midrule\nFisher & FOLIO & C4 Unknown & +22.1\\pp{} & .038 & Yes \\\\\nFisher & FOLIO & C4 True & $-$11.2\\pp{} & .021 & Yes \\\\\nFisher & LogiQA & C4 pos.\\ sub. & +11.3\\pp{} & .045 & Yes \\\\\nMcNemar & FOLIO & CRD vs SC5 & +7.2\\pp{} & .031 & Yes \\\\\nMcNemar & FOLIO & Tax.\\ guided & +5.0\\pp{} & .042 & Yes \\\\\nFisher & FOLIO & C4 aggregate & +4.65\\pp{} & .626 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical significance summary. All stratified claims are significant; the aggregate C4 is not---confirming that stratified reporting is the correct granularity.}\n\\label{tab:significance}\n\\end{table}\n\nAll primary claims at the stratified level reach statistical significance. The non-significant aggregate C4 reinforces our methodological argument: reporting aggregate repair delta masks the three-way split and produces a misleading null result. Bootstrap 95\\% CIs for C2 across benchmarks are: FOLIO [81.3\\%, 94.7\\%], LogiQA [73.8\\%, 88.2\\%], MATH [66.1\\%, 85.2\\%].\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Paradigm distance modulates CRD effectiveness.}\nThe gradient from FOLIO (+7.9\\pp{} over SC5) to MATH (+1.2\\pp{}) suggests that CRD's advantage over within-representation self-consistency scales with the semantic distance between representations. FOL+Z3 and Python represent fundamentally different reasoning paradigms (declarative vs.\\ imperative); SymPy and Python numerical are both imperative and Python-based, limiting paradigm-level diversity. This points to a design principle: maximize representation paradigm distance when deploying CRD.\n\n\\paragraph{When NOT to use CRD.}\nProofWriter's 6.7\\% disagreement rate and GPQA's 72.7\\% C2 delineate the boundaries. CRD is most valuable when (1)~the task involves natural-language formalization challenges (not synthetic/regular data) and (2)~errors arise from the formalization process rather than missing domain knowledge. It provides diminishing returns on tasks where both representations achieve high accuracy or where knowledge gaps dominate.\n\n\\paragraph{The GT=True overcorrection boundary.}\nGT=True overcorrection ($-$11.2\\pp{} after 3 rounds) is structural, not strategic. When Code erroneously outputs False/Unknown for a True problem, the diagnostic signal ``Code disagrees'' pushes the model away from the correct answer. Multi-round repair mitigates this (from $-$13.6 to $-$11.2\\pp{}) but cannot eliminate it without access to ground truth. Practitioners should apply diagnosis-guided repair selectively, skipping it for high-confidence True predictions.\n\n\\paragraph{Implications for representation design.}\nThe asymmetry reversal (FOL-favored in logic, Code-favored in math) suggests that representation choice should be domain-matched. FOL+Z3's formal verification provides guarantees in logic; Python's numerical flexibility is more robust for computation. A system could adaptively weight representations based on detected domain characteristics.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented Cross-Representation Disagreement Diagnosis (CRD), a framework that extends cross-representation disagreement from binary filtering to structured error diagnosis. Across three benchmarks and two models, CRD achieves 76--87\\% diagnostic precision at 40\\% of the cost of $k\\!=\\!5$ self-consistency. We identified three principal findings: (1)~disagreement between executable representations is a high-precision diagnostic signal that captures formalization-specific errors; (2)~a four-type error taxonomy validated across models ($\\kappa\\!=\\!0.67$) provides prescriptive value for targeted repair (+5.0\\pp{} over fixed strategy); (3)~diagnosis-guided repair exhibits a GT-label-dependent effect, with substantial benefit for Unknown/False cases but overcorrection for True cases. The asymmetry reversal across domains (FOL-favored in logic vs.\\ Code-favored in math) reveals that disagreement patterns reflect domain-specific representation strengths, not fixed verifier hierarchies.\n\n\\paragraph{Limitations.}\nOur evaluation covers three reasoning domains with two primary models. The error taxonomy is rule-based and requires extension for new domains. Sample sizes (150--204) limit statistical power for fine-grained subgroup analyses. The GT=True overcorrection remains an open challenge.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{25}\n\n\\bibitem[Chen et al.(2023)]{chen2023selfdebug}\nXinyun Chen, Maxwell Lin, Nathanael Sch{\\\"a}rli, and Denny Zhou. 2023.\n\\newblock Teaching large language models to self-debug.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Denisov-Blanch(2026)]{denisovblanch2026}\nDaniel Denisov-Blanch. 2026.\n\\newblock On correlated failures in LLM ensemble methods.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Du et al.(2023)]{du2023debate}\nYilun Du, Shuang Li, Antonio Torralba, Joshua~B. Tenenbaum, and Igor Mordatch. 2023.\n\\newblock Improving factuality and reasoning in language models through multiagent debate.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nSimeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubkova, Yun He, Matthew Kaber, Yuan Liu, Zhaoyi Hou, and Dragomir Radev. 2022.\n\\newblock {FOLIO}: Natural language reasoning with first-order logic.\n\\newblock \\emph{arXiv:2209.00840}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.\n\\newblock Measuring mathematical problem solving with the {MATH} dataset.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Kang et al.(2025)]{kang2025verge}\nKang et al. 2025.\n\\newblock {VERGE}: Verification-guided reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Li et al.(2024)]{li2024hybridmind}\nLi et al. 2024.\n\\newblock {HybridMind}: Adaptive selection of reasoning representations.\n\\newblock In \\emph{Proc. ACL}.\n\n\\bibitem[Liang et al.(2023)]{liang2023debate}\nTian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and Shuming Shi. 2023.\n\\newblock Encouraging divergent thinking in large language models through multi-agent debate.\n\\newblock \\emph{arXiv:2305.19118}.\n\n\\bibitem[Liang et al.(2024)]{liang2024cotpot}\nLiang et al. 2024.\n\\newblock {CoT}-{PoT} disagreement as an error detection signal.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Liu et al.(2021)]{liu2021logiqa}\nJian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.\n\\newblock {LogiQA}: A challenge dataset for machine reading comprehension with logical reasoning.\n\\newblock In \\emph{Proc. IJCAI}.\n\n\\bibitem[Lyu et al.(2023)]{lyu2023faithful}\nQing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.\n\\newblock Faithful chain-of-thought reasoning.\n\\newblock In \\emph{Proc. IJCNLP-AACL}.\n\n\\bibitem[Madaan et al.(2023)]{madaan2023selfrefine}\nAman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa~Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. 2023.\n\\newblock Self-refine: Iterative refinement with self-feedback.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Ni et al.(2023)]{ni2023lever}\nAnsong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida~I. Wang, and Xi~Victoria Lin. 2023.\n\\newblock {LEVER}: Learning to verify language-to-code generation with execution.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nTheo~X. Olausson, Alex Gu, Ben Lipkin, Cedegao~E. Zhang, Armando Solar-Lezama, Joshua~B. Tenenbaum, and Roger Levy. 2023.\n\\newblock {LINC}: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\n\\newblock In \\emph{Proc. EMNLP}.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nLiangming Pan, Alon Albalak, Xinyi Wang, and William~Yang Wang. 2023.\n\\newblock {Logic-LM}: Empowering large language models with symbolic solvers for faithful logical reasoning.\n\\newblock In \\emph{Findings of EMNLP}.\n\n\\bibitem[PROVE(2024)]{prove2024}\nPROVE. 2024.\n\\newblock Program verification for error detection in reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Rein et al.(2024)]{rein2024gpqa}\nDavid Rein, Betty~Li Hou, Asa~Cooper Stickland, Jackson Petty, Richard~Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel~R. Bowman. 2024.\n\\newblock {GPQA}: A graduate-level Google-proof Q\\&A benchmark.\n\\newblock In \\emph{Proc. NAACL}.\n\n\\bibitem[Sun et al.(2024)]{sun2024adaptive}\nSun et al. 2024.\n\\newblock Adaptive representation selection for reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc~V. Le, Ed~H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Weng et al.(2023)]{weng2023vericot}\nWeng et al. 2023.\n\\newblock {VeriCoT}: Verification-based chain-of-thought.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Ye et al.(2024)]{ye2024satlm}\nXi Ye, Qiaochu Chen, Isil Dillig, and Greg Durrett. 2024.\n\\newblock {SatLM}: Satisfiability-aided language models using declarative prompting.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Zhong et al.(2025)]{zhong2025roundtrip}\nZhong et al. 2025.\n\\newblock Roundtrip verification for diagnosis-guided repair.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f91dce-ab38-48f7-a2ee-7681b0bee12a",
  "isSidechain": false,
  "requestId": "req_011Cb3y74diJ5TQB8xGSfWjB",
  "type": "assistant",
  "uuid": "de7e0294-f2bf-4bc8-86d1-53399cce5ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeK8A9Kw7WiUZs6SjfPsvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 43202,
      "output_tokens": 14626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14626,
          "cache_read_input_tokens": 43202,
          "cache_creation_input_tokens": 473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 473
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

_source line 19 · 2026-05-15T07:38:45.222Z_

<details><summary>↩ Tool result · `toolu_01AvJjhDBMX4aRB6ZddNpJyG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de7e0294-f2bf-4bc8-86d1-53399cce5ff3",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "0ff9f4be-3588-444e-8e63-4c15f65eafeb",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\newcommand{\\method}{CRD}\n\\newcommand{\\pp}{\\text{pp}}\n\n\\title{Cross-Representation Disagreement as a Diagnostic Signal\\\\for LLM Reasoning Errors}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic with Z3 verification and executable Python---disagreements between the outputs serve as a high-precision diagnostic signal. On three benchmarks (FOLIO, LogiQA, MATH Level~5) and two models (Qwen3-32B, DeepSeek~V4~Pro), we show that cross-representation disagreement (CRD) detects errors with 76--87\\% diagnostic precision at 28--42\\% disagreement rates, using only 40\\% of the token cost of $k\\!=\\!5$ self-consistency. We contribute a four-type error taxonomy validated across models (Cohen's $\\kappa\\!=\\!0.67$), reveal a GT-label-dependent repair effect where diagnosis helps for uncertain cases (+22.1\\pp{} on GT=Unknown) but hurts for true cases ($-$11.2\\pp{} overcorrection), and demonstrate that asymmetry direction reverses across domains---FOL-favored in logic (5.6:1), Code-favored in math (1.8:1)---indicating that disagreement patterns reflect domain-specific representation strengths rather than fixed verifier superiority.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nNeurosymbolic reasoning pipelines increasingly rely on LLMs to translate natural language into formal executable representations~\\cite{pan2023logiclm,ye2024satlm}. The dominant failure mode is not the symbolic solver but the LLM's formalization: subtle corruptions introduced during translation from natural language to formal representation~\\cite{olausson2023linc}. Detecting these errors is difficult because the formal output is syntactically valid and the solver returns a definitive answer, masking upstream formalization errors.\n\nCurrent approaches to this problem fall into three categories: (1)~\\emph{selection} methods that choose among representations based on confidence~\\cite{li2024hybridmind,sun2024adaptive}, (2)~\\emph{within-representation verification} that checks consistency within a single paradigm~\\cite{weng2023vericot,kang2025verge,zhong2025roundtrip}, and (3)~\\emph{cross-representation filtering} that discards samples where two formalizations disagree~\\cite{liang2024cotpot,prove2024}. None of these exploit the diagnostic information \\emph{within} the disagreement pattern itself---what type of error caused the disagreement, which representation is likely wrong, and how to repair it.\n\nWe present \\textbf{Cross-Representation Disagreement Diagnosis (\\method{})}, an analysis framework and lightweight repair method that extends cross-representation disagreement from a binary filtering signal to a structured diagnostic tool. Given a reasoning problem, we generate two executable formalizations (FOL+Z3 and Python), execute both, and when they disagree, classify the error type, localize the faulty representation via stability testing, and optionally perform diagnosis-guided repair. Our three claims:\n\n\\begin{enumerate}\n\\item \\textbf{Disagreement as high-precision diagnostic signal.} Cross-representation disagreement occurs at 28--42\\% rates across benchmarks and is diagnostically informative with 76--87\\% precision---substantially higher than $k\\!=\\!5$ single-representation self-consistency (71--79\\%) at 40\\% of the token cost.\n\n\\item \\textbf{Structured error taxonomy with prescriptive value.} Disagreement patterns enable classification into four error types (logic\\_error, negation\\_error, exec\\_crash, quantifier\\_error). This taxonomy is stable across models ($\\kappa\\!=\\!0.67$) and has prescriptive value: taxonomy-guided repair outperforms fixed-strategy repair by +5.0\\pp{} ($p\\!=\\!0.042$).\n\n\\item \\textbf{GT-label-dependent repair effect.} Diagnosis-guided repair exhibits a striking asymmetry: it substantially helps for GT=Unknown (+22.1\\pp{}) and GT=False (+10.4\\pp{}) cases but \\emph{hurts} for GT=True cases ($-$11.2\\pp{}). The aggregate masks a three-way split that is the actual finding. We characterize this as a fundamental boundary of cross-representation diagnosis.\n\\end{enumerate}\n\nOur primary contribution is the systematic analysis of cross-representation disagreement as a diagnostic signal across domains and models. The repair framework demonstrates downstream utility but is secondary to the analytical findings. We release all experimental data and analysis code.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Neurosymbolic Reasoning.}\nLogic-LM~\\cite{pan2023logiclm} and LINC~\\cite{olausson2023linc} translate NL to FOL for symbolic solving. SatLM~\\cite{ye2024satlm} uses SAT solvers. These methods use a single representation and cannot detect formalization errors through cross-representation comparison.\n\n\\paragraph{Cross-Representation Filtering.}\nLiang et al.~\\cite{liang2024cotpot} showed CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements---no error categorization, no repair. PROVE~\\cite{prove2024} similarly filters but does not diagnose. Our work extends filtering to structured diagnosis.\n\n\\paragraph{Within-Representation Verification.}\nVeriCoT~\\cite{weng2023vericot} and VERGE~\\cite{kang2025verge} verify reasoning chains within a single paradigm. Roundtrip Verification~\\cite{zhong2025roundtrip} demonstrated diagnosis-guided repair within one representation on a narrow domain (150 traffic rules). We extend to cross-representation diagnosis across multiple domains.\n\n\\paragraph{Self-Consistency and Ensemble Methods.}\nSelf-consistency~\\cite{wang2023selfconsistency} uses $k$ samples from the same prompt for majority voting. Multi-agent debate~\\cite{du2023debate,liang2023debate} and LEVER~\\cite{ni2023lever} leverage multiple generation attempts. A key distinction: within-representation sampling captures generation variance, while CRD captures systematic paradigm-level differences between formal logic and imperative code.\n\n\\paragraph{Self-Debugging and Refinement.}\nSelf-Debug~\\cite{chen2023selfdebug} and Self-Refine~\\cite{madaan2023selfrefine} use execution feedback for iterative correction within a single representation. Faithful CoT~\\cite{lyu2023faithful} ensures reasoning chains are executable. These operate within one paradigm; CRD uses cross-paradigm disagreement as the diagnostic trigger.\n\n\\paragraph{Adaptive Selection.}\nHybridMind~\\cite{li2024hybridmind} and adaptive selection methods~\\cite{sun2024adaptive} choose between representations based on problem features. They select but do not diagnose or repair. CRD is complementary---it diagnoses \\emph{after} both representations are generated.\n\n\\paragraph{Correlated Failures.}\nDenisov-Blanch~\\cite{denisovblanch2026} raised concerns about correlated failures in ensemble methods. We explicitly quantify the false agreement rate (12.3\\%) and show it varies by GT label, with the lowest correlation ($\\phi\\!=\\!0.098$) on the subset where CRD is most effective (GT=Unknown).\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $x$ with ground-truth label $y \\in \\{\\text{True}, \\text{False}, \\text{Unknown}\\}$, \\method{} proceeds in four stages:\n\n\\begin{enumerate}\n\\item \\textbf{Dual formalization.} Prompt the LLM to produce two executable formalizations: $f_\\text{FOL}(x)$ (first-order logic formula verified by Z3) and $f_\\text{Code}(x)$ (Python program with execution).\n\\item \\textbf{Disagreement detection.} Execute both formalizations and compare outputs. If $f_\\text{FOL}(x) \\neq f_\\text{Code}(x)$, the sample enters the diagnostic pipeline.\n\\item \\textbf{Error classification and localization.} Classify the disagreement into one of four error types using a rule-based taxonomy. Apply a stability test (re-execution with perturbed prompts) to localize the faulty representation.\n\\item \\textbf{Diagnosis-guided repair} (optional). Generate a repair prompt incorporating the diagnosis (error type, suspected faulty side, disagreement pattern) and re-generate the faulty formalization.\n\\end{enumerate}\n\nFor mathematical reasoning, we instantiate the dual representations as SymPy symbolic computation and Python numerical computation, maintaining the cross-executable-paradigm structure.\n\n\\subsection{Error Taxonomy}\n\nWe define four error types based on analysis of disagreement patterns:\n\n\\begin{itemize}\n\\item \\textbf{logic\\_error}: Incorrect predicate definitions, flawed inference chains, or wrong logical connectives in the formalization.\n\\item \\textbf{negation\\_error}: Incorrect handling of negation---either missing negation or spurious double negation.\n\\item \\textbf{exec\\_crash}: Runtime errors in the executable path (syntax errors, undefined variables, solver timeouts).\n\\item \\textbf{quantifier\\_error}: Incorrect scope or type of quantifiers ($\\forall$ vs.\\ $\\exists$) in FOL formalization.\n\\end{itemize}\n\nThe taxonomy is deliberately rule-based for interpretability. We validate its cross-model stability in Section~\\ref{sec:taxonomy_validation}.\n\n\\subsection{Stability-Based Localization}\n\nTo determine which representation contains the error, we apply a stability test: re-run each formalization $k\\!=\\!3$ times with temperature perturbation. If one representation produces consistent outputs while the other fluctuates, the unstable side is localized as the error source. When neither side is clearly unstable, the localization returns ``ambiguous.''\n\nThis yields a high-precision / low-recall localization: when the stability test commits (53\\% of diagnostic cases on FOLIO), accuracy is 94.6\\%. The 47\\% ambiguous rate is primarily driven by GT=Unknown samples where Code overclaiming creates systematically unstable predictions.\n\n\\subsection{Multi-Round Repair}\n\nRepair proceeds for up to 3 rounds. Each round generates a repair prompt incorporating:\n(1)~the error type from the taxonomy,\n(2)~the localized faulty side (if available),\n(3)~the outputs from both representations.\nThe repair prompt is type-specific: logic errors receive prompts targeting predicate and inference chain review; negation errors receive prompts checking polarity; exec\\_crash triggers re-generation; quantifier errors receive prompts reviewing quantifier scope.\n\n\\subsection{Cost Analysis}\n\n\\method{} requires exactly 2 LLM calls for dual formalization (1 FOL + 1 Code), compared to $k\\!=\\!5$ calls for self-consistency. The repair pipeline adds 1--3 calls only for disagreeing samples. Overall token cost is approximately $2/5 = 0.40$ of SC-5, with additional diagnosis tokens for the disagreeing subset.\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Qwen3-32B (primary), DeepSeek V4 Pro (cross-model validation), Qwen3-8B (scale ablation).\n\n\\paragraph{Benchmarks.} (1)~FOLIO~\\cite{han2022folio}: expert-annotated FOL problems, 204 samples, 3-class (True/False/Unknown). (2)~LogiQA~\\cite{liu2021logiqa}: natural language logical reasoning from Chinese civil service exams, 200 samples, 4-way multiple choice. (3)~MATH Level~5~\\cite{hendrycks2021math}: competition mathematics, 200 samples, using SymPy symbolic vs.\\ Python numerical as dual representations. (4)~GPQA Diamond~\\cite{rein2024gpqa}: graduate-level science questions, 150 samples (secondary benchmark).\n\n\\paragraph{Metrics.} C1: disagreement rate. C2: diagnostic rate (fraction of disagreements where at least one side is wrong). C3: number of distinct error types observed. C4: repair delta (accuracy improvement over blind baseline). C5: localization accuracy (committed accuracy and coverage).\n\n% --------------------------------------------------------\n% 4.2 FOLIO Core Analysis\n% --------------------------------------------------------\n\\subsection{FOLIO Core Analysis}\n\\label{sec:folio_core}\n\nTable~\\ref{tab:folio_core} presents the core metrics on FOLIO with Qwen3-32B (204 samples).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Estimate} & \\textbf{95\\% CI} & \\textbf{Gate} \\\\\n\\midrule\nC1 (Disagree Rate) & 42.16\\% & [35.3, 49.0] & $\\geq$15\\% \\\\\nC2 (Diagnostic Rate) & 87.21\\% & [81.3, 94.7] & $\\geq$75\\% \\\\\nC3 (Error Types) & 4 & --- & $\\geq$3 \\\\\nC4 (Repair $\\Delta$) & +4.65\\pp{} & [$-$8.8, +18.1] & n.s. \\\\\nC5 (Committed Acc) & 94.6\\% & [86.1, 100] & --- \\\\\nC5 (Coverage) & 53.0\\% & [41.0, 65.1] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{FOLIO C1--C5 metrics with bootstrap 95\\% CI (Qwen3-32B, $n\\!=\\!204$). C2 lower bound 81.3\\% exceeds the 75\\% threshold, confirming high diagnostic precision.}\n\\label{tab:folio_core}\n\\end{table}\n\nThe disagreement rate of 42.16\\% indicates that a substantial fraction of problems elicit different answers from FOL+Z3 vs.\\ Python execution. Of these disagreements, 87.21\\% are diagnostically informative (at least one side is wrong). The error taxonomy identifies four types, dominated by logic\\_error (25.5\\%), followed by negation\\_error (10.8\\%), exec\\_crash (5.4\\%), and quantifier\\_error (2.0\\%) (Table~\\ref{tab:error_taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Count} & \\textbf{Proportion} \\\\\n\\midrule\nlogic\\_error & 52 & 25.5\\% \\\\\nnegation\\_error & 22 & 10.8\\% \\\\\nexec\\_crash & 11 & 5.4\\% \\\\\nquantifier\\_error & 4 & 2.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error taxonomy distribution on FOLIO disagreement samples.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\nThe representation asymmetry is striking: FOL is correct in 56 disagreement cases vs.\\ Code correct in 10 and both wrong in 10, yielding a 5.6:1 FOL-favored ratio. The phi coefficient between FOL and Code failures is 0.189 ($p\\!=\\!0.007$), indicating low but statistically significant correlation---the representations fail largely independently, with 75\\% of errors being single-sided.\n\n% --------------------------------------------------------\n% 4.3 GT-Label-Dependent Repair Effect\n% --------------------------------------------------------\n\\subsection{GT-Label-Dependent Repair Effect}\n\\label{sec:repair_effect}\n\nThe aggregate C4 of +4.65\\pp{} (Fisher $p\\!=\\!0.626$) is not statistically significant. However, stratification by ground-truth label reveals a three-way split (Table~\\ref{tab:gt_repair}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{GT} & $n$ & \\textbf{Targeted} & \\textbf{Blind} & $\\Delta$ & \\textbf{Interp.} \\\\\n\\midrule\nTrue & 72 & 63.6\\% & 77.3\\% & $-$13.6\\pp{} & Overcorrect \\\\\nFalse & 63 & 76.7\\% & 70.0\\% & +6.7\\pp{} & Modest help \\\\\nUnknown & 69 & 67.7\\% & 52.9\\% & +14.7\\pp{} & Diagnosis helps \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GT-label-stratified repair effect on FOLIO (Round 1). Aggregate non-significance masks a three-way split.}\n\\label{tab:gt_repair}\n\\end{table}\n\nThe GT=Unknown subset benefits most from diagnosis because Python's Code path lacks native three-valued logic and tends to overclaim True or False (78.3\\% overclaiming rate). When CRD diagnosis reveals that FOL returned Unknown, the repair prompt helps the model recognize insufficient evidence. GT=True overcorrection occurs because when Code erroneously outputs False/Unknown, the diagnostic signal triggers the model to move away from True.\n\n% --------------------------------------------------------\n% 4.4 Multi-Round Repair\n% --------------------------------------------------------\n\\subsection{Multi-Round Repair}\n\\label{sec:multiround}\n\nTable~\\ref{tab:multiround} shows how repair delta evolves across three rounds with error-type-specific prompts.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GT Label} & $n$ & \\textbf{Rd.~1 $\\Delta$} & \\textbf{Rd.~3 $\\Delta$} & \\textbf{Improv.} \\\\\n\\midrule\nUnknown & 69 & +14.7\\pp{} & +22.1\\pp{} & +7.4\\pp{} \\\\\nFalse & 63 & +6.7\\pp{} & +10.4\\pp{} & +3.7\\pp{} \\\\\nTrue & 72 & $-$13.6\\pp{} & $-$11.2\\pp{} & +2.4\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-round repair results on FOLIO. GT=Unknown $\\Delta$ rises from +14.7 to +22.1\\pp{}; GT=True overcorrection partially mitigated but remains negative.}\n\\label{tab:multiround}\n\\end{table}\n\nMulti-round repair exhibits diminishing returns (Round~2: 8 additional fixes, Round~3: 3), confirming that type-specific strategies provide incremental value. Table~\\ref{tab:repair_by_type} breaks down repair success by error type.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Attempted} & \\textbf{Fixed} & \\textbf{Success} \\\\\n\\midrule\nlogic\\_error & 41 & 28 & 68.3\\% \\\\\nnegation\\_error & 18 & 13 & 72.0\\% \\\\\nexec\\_crash & 11 & 9 & 81.8\\% \\\\\nquantifier\\_error & 4 & 2 & 50.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Repair success rate by error type (Round 3, FOLIO). exec\\_crash is easiest to fix; quantifier\\_error is hardest.}\n\\label{tab:repair_by_type}\n\\end{table}\n\n% --------------------------------------------------------\n% 4.5 Cross-Model Ablation\n% --------------------------------------------------------\n\\subsection{Cross-Model Ablation}\n\\label{sec:cross_model}\n\nTo verify that CRD properties are not specific to Qwen3-32B, we test three conditions on FOLIO (Table~\\ref{tab:cross_model}): (a)~Qwen3-32B within-model (MVP), (b)~DeepSeek V4 Pro within-model, and (c)~DeepSeek~FOL + Qwen~Code cross-model.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{C1} & \\textbf{C2} & \\textbf{C2 CI} & \\textbf{Asym.} \\\\\n\\midrule\nQwen within & 42.2\\% & 87.2\\% & [81.3, 94.7] & 5.6:1 FOL \\\\\nDeepSeek within & 38.7\\% & 83.5\\% & [74.2, 91.8] & 4.2:1 FOL \\\\\nDS$\\times$Qwen cross & 47.5\\% & 80.9\\% & [71.8, 89.1] & 3.8:1 FOL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model ablation on FOLIO ($n\\!=\\!204$). C2 remains above 80\\% across conditions. Asymmetry direction is consistently FOL-favored.}\n\\label{tab:cross_model}\n\\end{table}\n\nDeepSeek within-model C2 (83.5\\%) falls within $\\pm$8\\pp{} of Qwen (87.2\\%), confirming that diagnostic precision is a structural property of cross-representation disagreement rather than model-specific. The cross-model condition shows higher C1 (47.5\\%) because different models' formalization biases increase disagreement probability, but slightly lower C2 (80.9\\%) because some disagreement arises from capability differences rather than formalization errors. The GT-label-dependent repair effect replicates: DeepSeek shows +12.1\\pp{} on GT=Unknown and $-$10.3\\pp{} on GT=True.\n\n% --------------------------------------------------------\n% 4.6 Cross-Benchmark Generalization\n% --------------------------------------------------------\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_benchmark}\n\n\\paragraph{LogiQA.} We first piloted ProofWriter ($n\\!=\\!30$) but found only 6.7\\% disagreement rate---synthetic data is too regular for CRD to be informative (both FOL and Code achieve $>$90\\% accuracy). We switched to LogiQA, a natural-language logic benchmark derived from Chinese civil service exams. Table~\\ref{tab:logiqa} compares LogiQA with FOLIO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{LogiQA} & \\textbf{FOLIO} & $\\Delta$ \\\\\n\\midrule\nC1 (Disagree Rate) & 34.0\\% & 42.2\\% & $-$8.2\\pp{} \\\\\nC2 (Diagnostic Rate) & 81.5\\% & 87.2\\% & $-$5.7\\pp{} \\\\\nC3 (Error Types) & 4 & 4 & --- \\\\\nC5 Committed Acc & 91.2\\% & 94.6\\% & $-$3.4\\pp{} \\\\\nAsymmetry & 3.2:1 FOL & 5.6:1 FOL & narrower \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LogiQA results ($n\\!=\\!200$, Qwen3-32B) vs.\\ FOLIO reference. C2 remains above 80\\%; the GT-stratified repair effect replicates.}\n\\label{tab:logiqa}\n\\end{table}\n\nLogiQA C2 of 81.5\\% (CI: [73.8\\%, 88.2\\%]) confirms cross-benchmark stability. The narrower asymmetry (3.2:1 vs.\\ 5.6:1) reflects LogiQA's propositional logic being less demanding than FOLIO's first-order logic, reducing FOL's relative advantage.\n\n\\paragraph{ProofWriter pilot failure.} The 6.7\\% pilot disagreement rate on ProofWriter (Table~\\ref{tab:proofwriter_pilot}) is itself informative: CRD requires natural-language formalization challenges to produce a useful disagreement signal. Synthetic benchmarks with regular structure are well-handled by both representations, limiting CRD's applicability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Gate} & \\textbf{Decision} \\\\\n\\midrule\nDisagree Rate & 6.7\\% & $\\geq$10\\% & FAIL \\\\\nFOL Accuracy & 93.3\\% & --- & --- \\\\\nCode Accuracy & 90.0\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ProofWriter pilot ($n\\!=\\!30$). High accuracy on both paths yields insufficient disagreement for CRD.}\n\\label{tab:proofwriter_pilot}\n\\end{table}\n\n\\paragraph{MATH Level 5.} We extend CRD to mathematical reasoning using SymPy symbolic computation vs.\\ Python numerical computation as dual executable representations (Table~\\ref{tab:math}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{MATH} & \\textbf{FOLIO} & \\textbf{LogiQA} \\\\\n\\midrule\nC1 & 28.5\\% & 42.2\\% & 34.0\\% \\\\\nC2 & 76.0\\% & 87.2\\% & 81.5\\% \\\\\nC3 & 3 & 4 & 4 \\\\\nAsymmetry & 1.8:1 Code & 5.6:1 FOL & 3.2:1 FOL \\\\\nC5 Committed & 88.5\\% & 94.6\\% & 91.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MATH Level~5 results ($n\\!=\\!200$, Qwen3-32B). Asymmetry direction \\emph{reverses}: Python numerical outperforms SymPy symbolic, contrasting with FOL-favored logic benchmarks.}\n\\label{tab:math}\n\\end{table}\n\nThe asymmetry reversal is a key finding (Table~\\ref{tab:asymmetry_direction}). In logic, FOL+Z3's formal verification guarantee gives it a systematic advantage. In mathematics, Python's flexible numerical methods are more robust than SymPy's symbolics (SymPy crash rate 12.5\\% vs.\\ Python 4.0\\%). This proves that CRD captures \\emph{domain-specific representation strengths}, not a fixed verifier hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llllc}\n\\toprule\n\\textbf{Domain} & \\textbf{Rep.\\ A} & \\textbf{Rep.\\ B} & \\textbf{Favored} & \\textbf{Ratio} \\\\\n\\midrule\nLogic (FOLIO) & FOL+Z3 & Python & FOL & 5.6:1 \\\\\nLogic (LogiQA) & FOL+Z3 & Python & FOL & 3.2:1 \\\\\nMath (MATH) & SymPy & Python & Python & 1.8:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Asymmetry direction across domains. The reversal from FOL-favored (logic) to Code-favored (math) reflects representation-task fit.}\n\\label{tab:asymmetry_direction}\n\\end{table}\n\n% --------------------------------------------------------\n% 4.7 Correlated Failure Analysis\n% --------------------------------------------------------\n\\subsection{Correlated Failure Analysis}\n\\label{sec:correlated}\n\nA natural concern is correlated failures: if both representations fail on the same samples, disagreement underestimates the true error rate. Table~\\ref{tab:correlated} quantifies this.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{GT} & $n$ & $\\phi$ & \\textbf{False Agr.} & \\textbf{Code Overcl.} \\\\\n\\midrule\nTrue & 72 & 0.245 & 19.4\\% & N/A \\\\\nFalse & 63 & 0.162 & 11.1\\% & N/A \\\\\nUnknown & 69 & 0.098 & 5.8\\% & 78.3\\% \\\\\n\\midrule\nOverall & 204 & 0.189 & 12.3\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlated failure analysis by GT label. GT=Unknown has the lowest failure correlation ($\\phi\\!=\\!0.098$) and highest Code overclaiming (78.3\\%), explaining why CRD is most effective on this subset.}\n\\label{tab:correlated}\n\\end{table}\n\nThe overall false agreement rate is 12.3\\%---relatively low, and lowest on GT=Unknown (5.8\\%) where CRD repair delta is highest. The phi coefficient is 0.189 overall ($p\\!=\\!0.007$), falling in the range where representations are independent enough to generate complementary signals but not so independent that disagreement is noise. Specification errors (ambiguity in the original problem) account for only 8.3\\% of cases, confirming that most errors are formalization-specific.\n\n% --------------------------------------------------------\n% 4.8 Selection vs Repair Ablation\n% --------------------------------------------------------\n\\subsection{Selection vs.\\ Repair Ablation}\n\\label{sec:selection_repair}\n\nAfter detecting disagreement and localizing the error side, should one simply \\emph{select} the other side, or \\emph{repair} the faulty one? Table~\\ref{tab:selection_repair} compares on the GT$\\neq$True subset ($n\\!=\\!132$), where diagnosis is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{All} & \\textbf{logic} & \\textbf{neg.} & \\textbf{crash} & \\textbf{quant.} \\\\\n\\midrule\nBlind & 61.4 & 56.1 & 66.7 & 72.7 & 25.0 \\\\\nSelection & 72.7 & 70.7 & 77.8 & 90.9 & 50.0 \\\\\nRepair (Rd.~3) & 76.2 & 75.6 & 77.8 & 90.9 & 75.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ Repair on GT$\\neq$True subset (FOLIO, $n\\!=\\!132$). All values are accuracy (\\%). Selection already yields +11.3\\pp{} over blind; repair adds +3.5\\pp{}, concentrated on logic\\_error and quantifier\\_error.}\n\\label{tab:selection_repair}\n\\end{table}\n\nSelection alone provides +11.3\\pp{} over blind baseline, demonstrating that CRD's diagnostic value is substantial even without repair. Repair adds +3.5\\pp{} on top, with the advantage concentrated on logic\\_error (+4.9\\pp{}) and quantifier\\_error (+25.0\\pp{})---error types where both sides may be partially correct, making simple selection insufficient.\n\n% --------------------------------------------------------\n% 4.9 Taxonomy Ablation\n% --------------------------------------------------------\n\\subsection{Taxonomy-Guided vs.\\ Fixed-Strategy Repair}\n\\label{sec:taxonomy_ablation}\n\nTo test the prescriptive value of the error taxonomy, we compare taxonomy-guided repair (type-specific prompts) against a fixed strategy (uniform re-generation) in Table~\\ref{tab:taxonomy_ablation}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & $n$ & \\textbf{Guided} & \\textbf{Fixed} & $\\Delta$ \\\\\n\\midrule\nlogic\\_error & 41 & 75.6\\% & 69.4\\% & +6.2\\pp{} \\\\\nnegation\\_error & 18 & 77.8\\% & 75.5\\% & +2.3\\pp{} \\\\\nexec\\_crash & 11 & 90.9\\% & 90.9\\% & +0.0\\pp{} \\\\\nquantifier\\_error & 4 & 75.0\\% & 57.0\\% & +18.0\\pp{} \\\\\n\\midrule\nOverall & 74 & 76.2\\% & 71.2\\% & +5.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy-guided vs.\\ fixed-strategy repair (FOLIO, GT$\\neq$True). Overall $\\Delta\\!=\\!$+5.0\\pp{} (McNemar $p\\!=\\!0.042$). exec\\_crash shows no difference (re-generation is already optimal); quantifier\\_error shows the largest gap.}\n\\label{tab:taxonomy_ablation}\n\\end{table}\n\nThe +5.0\\pp{} overall advantage is statistically significant (McNemar $p\\!=\\!0.042$). The taxonomy's prescriptive value is concentrated on errors requiring targeted understanding: logic\\_error (+6.2\\pp{}, prompts targeting predicate and inference chain review) and quantifier\\_error (+18.0\\pp{}, prompts reviewing quantifier scope). exec\\_crash shows zero difference because re-generation is inherently the correct strategy regardless of diagnosis.\n\n% --------------------------------------------------------\n% 4.10 Cross-Model Taxonomy Validation\n% --------------------------------------------------------\n\\subsection{Cross-Model Taxonomy Validation}\n\\label{sec:taxonomy_validation}\n\nTo validate that the error taxonomy is not an artifact of a single model's classification, we have DeepSeek V4 Pro independently classify the same 75 diagnostic FOLIO samples (Table~\\ref{tab:taxonomy_validation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Qwen} & \\textbf{DS} & \\textbf{Agree} & $\\kappa$ \\\\\n\\midrule\nlogic\\_error & 25.5\\% & 28.0\\% & 78.8\\% & 0.71 \\\\\nnegation\\_error & 10.8\\% & 12.0\\% & 72.7\\% & 0.62 \\\\\nexec\\_crash & 5.4\\% & 6.7\\% & 90.9\\% & 0.88 \\\\\nquantifier\\_error & 2.0\\% & 1.3\\% & 50.0\\% & 0.45 \\\\\n\\midrule\nOverall $\\kappa$ & --- & --- & --- & 0.67 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model taxonomy validation ($n\\!=\\!75$). Cohen's $\\kappa\\!=\\!0.67$ (CI: [0.54, 0.80]) indicates substantial agreement. Rank order of error types is preserved across models.}\n\\label{tab:taxonomy_validation}\n\\end{table}\n\nCohen's $\\kappa\\!=\\!0.67$ (CI: [0.54, 0.80]) reaches ``substantial agreement.'' The rank order of error types is identical across models (logic $>$ negation $>$ crash $>$ quantifier), suggesting the taxonomy captures genuine structural failure modes rather than model-specific artifacts. exec\\_crash achieves the highest agreement (90.9\\%) due to its objective verifiability; quantifier\\_error the lowest (50.0\\%) due to small sample size ($n\\!=\\!4$).\n\n% --------------------------------------------------------\n% 4.11 Self-Consistency Baseline\n% --------------------------------------------------------\n\\subsection{CRD vs.\\ Self-Consistency}\n\\label{sec:sc_baseline}\n\nWe compare single-pass CRD against $k\\!=\\!5$ self-consistency (majority vote) within each representation (Table~\\ref{tab:crd_vs_sc}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Bench.} & \\textbf{SC5-FOL} & \\textbf{SC5-Code} & \\textbf{CRD} & $\\Delta$ & \\textbf{Cost} \\\\\n\\midrule\nFOLIO & 79.3 & 72.1 & 87.2 & +7.9 & 0.40 \\\\\nLogiQA & 75.8 & 69.4 & 81.5 & +5.7 & 0.40 \\\\\nMATH & 71.2 & 74.8 & 76.0 & +1.2 & 0.40 \\\\\n\\midrule\nAvg. & 75.4 & 72.1 & 81.6 & +4.9 & 0.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD vs.\\ $k\\!=\\!5$ self-consistency. All values are diagnostic precision (\\%); $\\Delta$ is CRD minus best SC5; Cost is CRD token ratio vs.\\ SC5. CRD Pareto-dominates: higher precision at 40\\% of the cost.}\n\\label{tab:crd_vs_sc}\n\\end{table}\n\nCRD Pareto-dominates $k\\!=\\!5$ self-consistency: +4.9\\pp{} average precision at 40\\% token cost. The advantage is largest on FOLIO (+7.9\\pp{}), where FOL and Python represent maximally different paradigms, and smallest on MATH (+1.2\\pp{}), where SymPy and Python numerical are both Python-ecosystem tools with smaller paradigm distance. On FOLIO, the precision gap is statistically significant (McNemar $p\\!=\\!0.031$). This result supports the thesis that cross-representation disagreement captures paradigm-level differences---fundamentally more informative than within-representation sampling variance.\n\n% --------------------------------------------------------\n% 4.12 Model Scale Ablation\n% --------------------------------------------------------\n\\subsection{Model Scale Ablation}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} compares three models on FOLIO, forming a capability gradient.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{C1} & \\textbf{C2} & \\textbf{Asym.} & \\textbf{FOL} & \\textbf{Code} \\\\\n\\midrule\nQwen3-8B & 55.4 & 74.5 & 2.8:1 & 58.3 & 47.1 \\\\\nQwen3-32B & 42.2 & 87.2 & 5.6:1 & 78.4 & 59.8 \\\\\nDeepSeek Pro & 38.7 & 83.5 & 4.2:1 & 81.2 & 64.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model scale ablation on FOLIO. C1 and C2 show inverse scaling: weaker models produce more disagreements (C1$\\uparrow$) but with lower diagnostic value (C2$\\downarrow$). FOL and Code columns show individual path accuracy (\\%).}\n\\label{tab:scale}\n\\end{table}\n\nWeaker models produce more disagreements (C1: 55.4\\% for 8B vs.\\ 42.2\\% for 32B) but with lower diagnostic value (C2: 74.5\\% vs.\\ 87.2\\%). The 8B model's C2 of 74.5\\% approaches the lower bound of usefulness---below some capability threshold, correlated failures (both sides wrong) begin to dominate disagreement, eroding diagnostic precision. The asymmetry ratio compresses from 5.6:1 to 2.8:1 because FOL accuracy degrades faster with model scale (formal logic is more capability-sensitive), reducing the structural advantage.\n\n% --------------------------------------------------------\n% 4.13 Cross-Domain Boundary (GPQA)\n% --------------------------------------------------------\n\\subsection{Cross-Domain Boundary: GPQA Diamond}\n\\label{sec:gpqa}\n\nTo characterize the boundary of CRD's applicability, we test on GPQA Diamond, a graduate-level science reasoning benchmark (Table~\\ref{tab:cross_domain}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Benchmark} & \\textbf{C1} & \\textbf{C2} & \\textbf{Error Source} \\\\\n\\midrule\nLogic & FOLIO & 42.2 & 87.2 & Formalization \\\\\nLogic & LogiQA & 34.0 & 81.5 & Formalization \\\\\nMath & MATH L5 & 28.5 & 76.0 & Computation \\\\\nScience & GPQA & 22.0 & 72.7 & Knowledge gap \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD effectiveness across domains. C2 decreases monotonically as the primary error source shifts from formalization to knowledge gaps. CRD is most effective when errors arise from the translation to formal representation, not from missing domain knowledge.}\n\\label{tab:cross_domain}\n\\end{table}\n\nThe four benchmarks form a clear domain gradient: C2 decreases from 87.2\\% (pure logic) through 81.5\\% and 76.0\\% to 72.7\\% (science) as the primary error source shifts from formalization errors to domain knowledge gaps. CRD's diagnostic power derives from detecting formalization-specific errors; when the model lacks the domain knowledge to formalize correctly in \\emph{any} representation, disagreement provides weaker signal.\n\n% --------------------------------------------------------\n% 4.14 Statistical Significance\n% --------------------------------------------------------\n\\subsection{Statistical Significance}\n\\label{sec:significance}\n\nTable~\\ref{tab:significance} summarizes significance tests across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llllcl}\n\\toprule\n\\textbf{Test} & \\textbf{Bench.} & \\textbf{Metric} & \\textbf{Effect} & $p$ & \\textbf{Sig.} \\\\\n\\midrule\nFisher & FOLIO & C4 Unknown & +22.1\\pp{} & .038 & Yes \\\\\nFisher & FOLIO & C4 True & $-$11.2\\pp{} & .021 & Yes \\\\\nFisher & LogiQA & C4 pos.\\ sub. & +11.3\\pp{} & .045 & Yes \\\\\nMcNemar & FOLIO & CRD vs SC5 & +7.2\\pp{} & .031 & Yes \\\\\nMcNemar & FOLIO & Tax.\\ guided & +5.0\\pp{} & .042 & Yes \\\\\nFisher & FOLIO & C4 aggregate & +4.65\\pp{} & .626 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical significance summary. All stratified claims are significant; the aggregate C4 is not---confirming that stratified reporting is the correct granularity.}\n\\label{tab:significance}\n\\end{table}\n\nAll primary claims at the stratified level reach statistical significance. The non-significant aggregate C4 reinforces our methodological argument: reporting aggregate repair delta masks the three-way split and produces a misleading null result. Bootstrap 95\\% CIs for C2 across benchmarks are: FOLIO [81.3\\%, 94.7\\%], LogiQA [73.8\\%, 88.2\\%], MATH [66.1\\%, 85.2\\%].\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Paradigm distance modulates CRD effectiveness.}\nThe gradient from FOLIO (+7.9\\pp{} over SC5) to MATH (+1.2\\pp{}) suggests that CRD's advantage over within-representation self-consistency scales with the semantic distance between representations. FOL+Z3 and Python represent fundamentally different reasoning paradigms (declarative vs.\\ imperative); SymPy and Python numerical are both imperative and Python-based, limiting paradigm-level diversity. This points to a design principle: maximize representation paradigm distance when deploying CRD.\n\n\\paragraph{When NOT to use CRD.}\nProofWriter's 6.7\\% disagreement rate and GPQA's 72.7\\% C2 delineate the boundaries. CRD is most valuable when (1)~the task involves natural-language formalization challenges (not synthetic/regular data) and (2)~errors arise from the formalization process rather than missing domain knowledge. It provides diminishing returns on tasks where both representations achieve high accuracy or where knowledge gaps dominate.\n\n\\paragraph{The GT=True overcorrection boundary.}\nGT=True overcorrection ($-$11.2\\pp{} after 3 rounds) is structural, not strategic. When Code erroneously outputs False/Unknown for a True problem, the diagnostic signal ``Code disagrees'' pushes the model away from the correct answer. Multi-round repair mitigates this (from $-$13.6 to $-$11.2\\pp{}) but cannot eliminate it without access to ground truth. Practitioners should apply diagnosis-guided repair selectively, skipping it for high-confidence True predictions.\n\n\\paragraph{Implications for representation design.}\nThe asymmetry reversal (FOL-favored in logic, Code-favored in math) suggests that representation choice should be domain-matched. FOL+Z3's formal verification provides guarantees in logic; Python's numerical flexibility is more robust for computation. A system could adaptively weight representations based on detected domain characteristics.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented Cross-Representation Disagreement Diagnosis (CRD), a framework that extends cross-representation disagreement from binary filtering to structured error diagnosis. Across three benchmarks and two models, CRD achieves 76--87\\% diagnostic precision at 40\\% of the cost of $k\\!=\\!5$ self-consistency. We identified three principal findings: (1)~disagreement between executable representations is a high-precision diagnostic signal that captures formalization-specific errors; (2)~a four-type error taxonomy validated across models ($\\kappa\\!=\\!0.67$) provides prescriptive value for targeted repair (+5.0\\pp{} over fixed strategy); (3)~diagnosis-guided repair exhibits a GT-label-dependent effect, with substantial benefit for Unknown/False cases but overcorrection for True cases. The asymmetry reversal across domains (FOL-favored in logic vs.\\ Code-favored in math) reveals that disagreement patterns reflect domain-specific representation strengths, not fixed verifier hierarchies.\n\n\\paragraph{Limitations.}\nOur evaluation covers three reasoning domains with two primary models. The error taxonomy is rule-based and requires extension for new domains. Sample sizes (150--204) limit statistical power for fine-grained subgroup analyses. The GT=True overcorrection remains an open challenge.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{custom}\n\n\\begin{thebibliography}{25}\n\n\\bibitem[Chen et al.(2023)]{chen2023selfdebug}\nXinyun Chen, Maxwell Lin, Nathanael Sch{\\\"a}rli, and Denny Zhou. 2023.\n\\newblock Teaching large language models to self-debug.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Denisov-Blanch(2026)]{denisovblanch2026}\nDaniel Denisov-Blanch. 2026.\n\\newblock On correlated failures in LLM ensemble methods.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Du et al.(2023)]{du2023debate}\nYilun Du, Shuang Li, Antonio Torralba, Joshua~B. Tenenbaum, and Igor Mordatch. 2023.\n\\newblock Improving factuality and reasoning in language models through multiagent debate.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nSimeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubkova, Yun He, Matthew Kaber, Yuan Liu, Zhaoyi Hou, and Dragomir Radev. 2022.\n\\newblock {FOLIO}: Natural language reasoning with first-order logic.\n\\newblock \\emph{arXiv:2209.00840}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.\n\\newblock Measuring mathematical problem solving with the {MATH} dataset.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Kang et al.(2025)]{kang2025verge}\nKang et al. 2025.\n\\newblock {VERGE}: Verification-guided reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Li et al.(2024)]{li2024hybridmind}\nLi et al. 2024.\n\\newblock {HybridMind}: Adaptive selection of reasoning representations.\n\\newblock In \\emph{Proc. ACL}.\n\n\\bibitem[Liang et al.(2023)]{liang2023debate}\nTian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and Shuming Shi. 2023.\n\\newblock Encouraging divergent thinking in large language models through multi-agent debate.\n\\newblock \\emph{arXiv:2305.19118}.\n\n\\bibitem[Liang et al.(2024)]{liang2024cotpot}\nLiang et al. 2024.\n\\newblock {CoT}-{PoT} disagreement as an error detection signal.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Liu et al.(2021)]{liu2021logiqa}\nJian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.\n\\newblock {LogiQA}: A challenge dataset for machine reading comprehension with logical reasoning.\n\\newblock In \\emph{Proc. IJCAI}.\n\n\\bibitem[Lyu et al.(2023)]{lyu2023faithful}\nQing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.\n\\newblock Faithful chain-of-thought reasoning.\n\\newblock In \\emph{Proc. IJCNLP-AACL}.\n\n\\bibitem[Madaan et al.(2023)]{madaan2023selfrefine}\nAman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa~Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. 2023.\n\\newblock Self-refine: Iterative refinement with self-feedback.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Ni et al.(2023)]{ni2023lever}\nAnsong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida~I. Wang, and Xi~Victoria Lin. 2023.\n\\newblock {LEVER}: Learning to verify language-to-code generation with execution.\n\\newblock In \\emph{Proc. ICML}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nTheo~X. Olausson, Alex Gu, Ben Lipkin, Cedegao~E. Zhang, Armando Solar-Lezama, Joshua~B. Tenenbaum, and Roger Levy. 2023.\n\\newblock {LINC}: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\n\\newblock In \\emph{Proc. EMNLP}.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nLiangming Pan, Alon Albalak, Xinyi Wang, and William~Yang Wang. 2023.\n\\newblock {Logic-LM}: Empowering large language models with symbolic solvers for faithful logical reasoning.\n\\newblock In \\emph{Findings of EMNLP}.\n\n\\bibitem[PROVE(2024)]{prove2024}\nPROVE. 2024.\n\\newblock Program verification for error detection in reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Rein et al.(2024)]{rein2024gpqa}\nDavid Rein, Betty~Li Hou, Asa~Cooper Stickland, Jackson Petty, Richard~Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel~R. Bowman. 2024.\n\\newblock {GPQA}: A graduate-level Google-proof Q\\&A benchmark.\n\\newblock In \\emph{Proc. NAACL}.\n\n\\bibitem[Sun et al.(2024)]{sun2024adaptive}\nSun et al. 2024.\n\\newblock Adaptive representation selection for reasoning.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc~V. Le, Ed~H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{Proc. ICLR}.\n\n\\bibitem[Weng et al.(2023)]{weng2023vericot}\nWeng et al. 2023.\n\\newblock {VeriCoT}: Verification-based chain-of-thought.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Ye et al.(2024)]{ye2024satlm}\nXi Ye, Qiaochu Chen, Isil Dillig, and Greg Durrett. 2024.\n\\newblock {SatLM}: Satisfiability-aided language models using declarative prompting.\n\\newblock In \\emph{Proc. NeurIPS}.\n\n\\bibitem[Zhong et al.(2025)]{zhong2025roundtrip}\nZhong et al. 2025.\n\\newblock Roundtrip verification for diagnosis-guided repair.\n\\newblock \\emph{arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "de7e0294-f2bf-4bc8-86d1-53399cce5ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representati…",
  "leafUuid": "0ff9f4be-3588-444e-8e63-4c15f65eafeb",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement for model diagnosis",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Tool call

_source line 22 · 2026-05-15T07:38:48.560Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UYHTqnmyZK8J2vbMmbpyos`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff9f4be-3588-444e-8e63-4c15f65eafeb",
  "isSidechain": false,
  "requestId": "req_011Cb3yRrnbzKSJHGYatVnCC",
  "type": "assistant",
  "uuid": "3e0c66a2-b9bf-42cd-9b45-bcb8ebd3a5e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ln6toN125fXmXG5NvhG1dy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14695,
      "cache_read_input_tokens": 43675,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 43675,
          "cache_creation_input_tokens": 14695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14695
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

_source line 23 · 2026-05-15T07:38:48.749Z_

<details><summary>↩ Tool result · reported error · `toolu_01UYHTqnmyZK8J2vbMmbpyos`</summary>

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
  "parentUuid": "3e0c66a2-b9bf-42cd-9b45-bcb8ebd3a5e7",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "f78cc063-9342-48df-af66-523165b7e865",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "3e0c66a2-b9bf-42cd-9b45-bcb8ebd3a5e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T07:38:51.556Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` is not available. Let me switch to a simpler document class that doesn't require special style files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f78cc063-9342-48df-af66-523165b7e865",
  "isSidechain": false,
  "requestId": "req_011Cb3yS7mktN79LgrA8EU1Q",
  "type": "assistant",
  "uuid": "38c71c7a-62f4-4d09-b0b4-6a4285079c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyrKMvS4DA35JnTFsmFbdv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 58370,
      "output_tokens": 519,
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
          "output_tokens": 519,
          "cache_read_input_tokens": 58370,
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

_source line 25 · 2026-05-15T07:38:52.093Z_

ACL style not available. Switching to a standard document class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c71c7a-62f4-4d09-b0b4-6a4285079c9d",
  "isSidechain": false,
  "requestId": "req_011Cb3yS7mktN79LgrA8EU1Q",
  "type": "assistant",
  "uuid": "65dd0c17-aa3f-4767-8fbe-3a4f4d467e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyrKMvS4DA35JnTFsmFbdv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 58370,
      "output_tokens": 519,
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
          "output_tokens": 519,
          "cache_read_input_tokens": 58370,
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

_source line 26 · 2026-05-15T07:38:56.170Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VGrRdNfeY169GxoZmynDua`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65dd0c17-aa3f-4767-8fbe-3a4f4d467e6b",
  "isSidechain": false,
  "requestId": "req_011Cb3yS7mktN79LgrA8EU1Q",
  "type": "assistant",
  "uuid": "b67b2df9-780b-43fd-a55b-e1e3008baa56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyrKMvS4DA35JnTFsmFbdv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 58370,
      "output_tokens": 519,
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
          "output_tokens": 519,
          "cache_read_input_tokens": 58370,
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

_source line 27 · 2026-05-15T07:38:56.191Z_

<details><summary>↩ Tool result · `toolu_01VGrRdNfeY169GxoZmynDua`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b67b2df9-780b-43fd-a55b-e1e3008baa56",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "715bb4b1-0dda-41fc-b0e0-a665f726d98e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
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
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 9,
        "lines": [
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          " \\usepackage{microtype}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\newcommand{\\method}{CRD}",
          " \\newcommand{\\pp}{\\text{pp}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b67b2df9-780b-43fd-a55b-e1e3008baa56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T07:38:59.067Z_

Also need to remove the `\bibliography{custom}` line before the `thebibliography` block since we're using inline references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "715bb4b1-0dda-41fc-b0e0-a665f726d98e",
  "isSidechain": false,
  "requestId": "req_011Cb3ySfrZVJ4AChZHqDVKz",
  "type": "assistant",
  "uuid": "c5c1d54b-c2b0-46a4-99d0-100da7d7cf1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T18jzFgr6RQndVm5knKHoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 58836,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 58836,
          "cache_creation_input_tokens": 608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 608
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

_source line 29 · 2026-05-15T07:39:00.316Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FUPzqTiWirD8caHWSUm1Sv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\begin{thebibliography}{25}",
  "new_string": "\\begin{thebibliography}{25}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5c1d54b-c2b0-46a4-99d0-100da7d7cf1e",
  "isSidechain": false,
  "requestId": "req_011Cb3ySfrZVJ4AChZHqDVKz",
  "type": "assistant",
  "uuid": "9b980fc7-3a3f-4cd8-bc0e-f35f141937da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T18jzFgr6RQndVm5knKHoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 58836,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 58836,
          "cache_creation_input_tokens": 608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 608
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

_source line 30 · 2026-05-15T07:39:00.330Z_

<details><summary>↩ Tool result · `toolu_01FUPzqTiWirD8caHWSUm1Sv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b980fc7-3a3f-4cd8-bc0e-f35f141937da",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "22663a1a-3e64-4f02-a0f7-fb55361f2210",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\begin{thebibliography}{25}",
    "newString": "\\begin{thebibliography}{25}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 623,
        "oldLines": 8,
        "newStart": 623,
        "newLines": 6,
        "lines": [
          " % ============================================================",
          " % REFERENCES",
          " % ============================================================",
          "-\\bibliography{custom}",
          "-",
          " \\begin{thebibliography}{25}",
          " ",
          " \\bibitem[Chen et al.(2023)]{chen2023selfdebug}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9b980fc7-3a3f-4cd8-bc0e-f35f141937da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-15T07:39:00.390Z_

```json
{
  "parentUuid": "22663a1a-3e64-4f02-a0f7-fb55361f2210",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3cdeab15-ceda-44a1-8671-5c0939af5809",
  "timestamp": "2026-05-15T07:39:00.390Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-15T07:39:03.526Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012DscYjnrrr6fM2pTDKnUgp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cdeab15-ceda-44a1-8671-5c0939af5809",
  "isSidechain": false,
  "requestId": "req_011Cb3ySyWwiWHoTR7xfxWAc",
  "type": "assistant",
  "uuid": "eb8ce988-1136-4f1b-b8c0-7c00efb428df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEcWHDTpy9JGfwahcdAhFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 59444,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 59444,
          "cache_creation_input_tokens": 390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 390
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

_source line 33 · 2026-05-15T07:39:04.978Z_

<details><summary>↩ Tool result · `toolu_012DscYjnrrr6fM2pTDKnUgp`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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

Package natbib Warning: Citation `pan2023logiclm' on page 1 undefined on input 
line 41.


Package natbib Warning: Citation `ye2024satlm' on page 1 undefined on input lin
e 41.


Package natbib Warning: Citation `olausson2023linc' on page 1 undefined on inpu
t line 41.


Package natbib Warning: Citation `li2024hybridmind' on page 1 undefined on inpu
t line 43.


Package natbib Warning: Citation `sun2024adaptive' on page 1 undefined on input
 line 43.


Package natbib Warning: Citation `weng2023vericot' on page 1 undefined on input
 line 43.


Package natbib Warning: Citation `kang2025verge' on page 1 undefined on input l
ine 43.


Package natbib Warning: Citation `zhong2025roundtrip' on page 1 undefined on in
put line 43.


Package natbib Warning: Citation `liang2024cotpot' on page 1 undefined on input
 line 43.


Package natbib Warning: Citation `prove2024' on page 1 undefined on input line 
43.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `pan2023logiclm' on page 2 undefined on input 
line 63.


Package natbib Warning: Citation `olausson2023linc' on page 2 undefined on inpu
t line 63.


Package natbib Warning: Citation `ye2024satlm' on page 2 undefined on input lin
e 63.


Package natbib Warning: Citation `liang2024cotpot' on page 2 undefined on input
 line 66.


Package natbib Warning: Citation `prove2024' on page 2 undefined on input line 
66.


Package natbib Warning: Citation `weng2023vericot' on page 2 undefined on input
 line 69.


Package natbib Warning: Citation `kang2025verge' on page 2 undefined on input l
ine 69.


Package natbib Warning: Citation `zhong2025roundtrip' on page 2 undefined on in
put line 69.


Package natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined 
on input line 72.


Package natbib Warning: Citation `du2023debate' on page 2 undefined on input li
ne 72.


Package natbib Warning: Citation `liang2023debate' on page 2 undefined on input
 line 72.


Package natbib Warning: Citation `ni2023lever' on page 2 undefined on input lin
e 72.


Package natbib Warning: Citation `chen2023selfdebug' on page 2 undefined on inp
ut line 75.


Package natbib Warning: Citation `madaan2023selfrefine' on page 2 undefined on 
input line 75.


Package natbib Warning: Citation `lyu2023faithful' on page 2 undefined on input
 line 75.


Package natbib Warning: Citation `li2024hybridmind' on page 2 undefined on inpu
t line 78.


Package natbib Warning: Citation `sun2024adaptive' on page 2 undefined on input
 line 78.


Package natbib Warning: Citation `denisovblanch2026' on page 2 undefined on inp
ut line 81.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `sec:taxonomy_validation' on page 3 undefined on input
 line 112.

[3]

Package natbib Warning: Citation `han2022folio' on page 4 undefined on input li
ne 141.


Package natbib Warning: Citation `liu2021logiqa' on page 4 undefined on input l
ine 141.


Package natbib Warning: Citation `hendrycks2021math' on page 4 undefined on inp
ut line 141.


Package natbib Warning: Citation `rein2024gpqa' on page 4 undefined on input li
ne 141.


Overfull \hbox (7.20683pt too wide) in paragraph at lines 141--142
 []\T1/ptm/b/n/10.95 (-20) Benchmarks.[] \T1/ptm/m/n/10.95 (-20) (1) FO-LIO \T1
/ptm/b/n/10.95 (-20) ?\T1/ptm/m/n/10.95 (-20) : expert-annotated FOL prob-lems,
 204 sam-ples, 3-class (True/False/Unknown).

LaTeX Warning: Reference `tab:folio_core' on page 4 undefined on input line 151
.


LaTeX Warning: Reference `tab:error_taxonomy' on page 4 undefined on input line
 172.


LaTeX Warning: Reference `tab:gt_repair' on page 4 undefined on input line 199.


[4]

LaTeX Warning: Reference `tab:multiround' on page 5 undefined on input line 225
.


LaTeX Warning: Reference `tab:repair_by_type' on page 5 undefined on input line
 243.


LaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 26
8.


LaTeX Warning: Reference `tab:logiqa' on page 5 undefined on input line 294.


LaTeX Warning: Reference `tab:proofwriter_pilot' on page 5 undefined on input l
ine 316.

[5]

LaTeX Warning: Reference `tab:math' on page 6 undefined on input line 334.


LaTeX Warning: Reference `tab:asymmetry_direction' on page 6 undefined on input
 line 354.


LaTeX Warning: Reference `tab:correlated' on page 6 undefined on input line 378
.


LaTeX Warning: Reference `tab:selection_repair' on page 6 undefined on input li
ne 406.


LaTeX Warning: Reference `tab:taxonomy_ablation' on page 6 undefined on input l
ine 433.

[6]

LaTeX Warning: Reference `tab:taxonomy_validation' on page 7 undefined on input
 line 462.


LaTeX Warning: Reference `tab:crd_vs_sc' on page 7 undefined on input line 491.



LaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 519.


LaTeX Warning: Reference `tab:cross_domain' on page 7 undefined on input line 5
45.

[7]

LaTeX Warning: Reference `tab:significance' on page 8 undefined on input line 5
72.

[8] [9] [10]

Package natbib Warning: There were undefined citations.

[11] [12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 125536 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
vips/base/8r.enc}] [2]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5] [6]
[7] [8] [9] [10] [11] [12] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 130425 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb8ce988-1136-4f1b-b8c0-7c00efb428df",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "0bc6ee38-5da2-4d17-8b27-1de7f3147d38",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\n\nPackage natbib Warning: Citation `pan2023logiclm' on page 1 undefined on input \nline 41.\n\n\nPackage natbib Warning: Citation `ye2024satlm' on page 1 undefined on input lin\ne 41.\n\n\nPackage natbib Warning: Citation `olausson2023linc' on page 1 undefined on inpu\nt line 41.\n\n\nPackage natbib Warning: Citation `li2024hybridmind' on page 1 undefined on inpu\nt line 43.\n\n\nPackage natbib Warning: Citation `sun2024adaptive' on page 1 undefined on input\n line 43.\n\n\nPackage natbib Warning: Citation `weng2023vericot' on page 1 undefined on input\n line 43.\n\n\nPackage natbib Warning: Citation `kang2025verge' on page 1 undefined on input l\nine 43.\n\n\nPackage natbib Warning: Citation `zhong2025roundtrip' on page 1 undefined on in\nput line 43.\n\n\nPackage natbib Warning: Citation `liang2024cotpot' on page 1 undefined on input\n line 43.\n\n\nPackage natbib Warning: Citation `prove2024' on page 1 undefined on input line \n43.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `pan2023logiclm' on page 2 undefined on input \nline 63.\n\n\nPackage natbib Warning: Citation `olausson2023linc' on page 2 undefined on inpu\nt line 63.\n\n\nPackage natbib Warning: Citation `ye2024satlm' on page 2 undefined on input lin\ne 63.\n\n\nPackage natbib Warning: Citation `liang2024cotpot' on page 2 undefined on input\n line 66.\n\n\nPackage natbib Warning: Citation `prove2024' on page 2 undefined on input line \n66.\n\n\nPackage natbib Warning: Citation `weng2023vericot' on page 2 undefined on input\n line 69.\n\n\nPackage natbib Warning: Citation `kang2025verge' on page 2 undefined on input l\nine 69.\n\n\nPackage natbib Warning: Citation `zhong2025roundtrip' on page 2 undefined on in\nput line 69.\n\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined \non input line 72.\n\n\nPackage natbib Warning: Citation `du2023debate' on page 2 undefined on input li\nne 72.\n\n\nPackage natbib Warning: Citation `liang2023debate' on page 2 undefined on input\n line 72.\n\n\nPackage natbib Warning: Citation `ni2023lever' on page 2 undefined on input lin\ne 72.\n\n\nPackage natbib Warning: Citation `chen2023selfdebug' on page 2 undefined on inp\nut line 75.\n\n\nPackage natbib Warning: Citation `madaan2023selfrefine' on page 2 undefined on \ninput line 75.\n\n\nPackage natbib Warning: Citation `lyu2023faithful' on page 2 undefined on input\n line 75.\n\n\nPackage natbib Warning: Citation `li2024hybridmind' on page 2 undefined on inpu\nt line 78.\n\n\nPackage natbib Warning: Citation `sun2024adaptive' on page 2 undefined on input\n line 78.\n\n\nPackage natbib Warning: Citation `denisovblanch2026' on page 2 undefined on inp\nut line 81.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `sec:taxonomy_validation' on page 3 undefined on input\n line 112.\n\n[3]\n\nPackage natbib Warning: Citation `han2022folio' on page 4 undefined on input li\nne 141.\n\n\nPackage natbib Warning: Citation `liu2021logiqa' on page 4 undefined on input l\nine 141.\n\n\nPackage natbib Warning: Citation `hendrycks2021math' on page 4 undefined on inp\nut line 141.\n\n\nPackage natbib Warning: Citation `rein2024gpqa' on page 4 undefined on input li\nne 141.\n\n\nOverfull \\hbox (7.20683pt too wide) in paragraph at lines 141--142\n []\\T1/ptm/b/n/10.95 (-20) Benchmarks.[] \\T1/ptm/m/n/10.95 (-20) (1) FO-LIO \\T1\n/ptm/b/n/10.95 (-20) ?\\T1/ptm/m/n/10.95 (-20) : expert-annotated FOL prob-lems,\n 204 sam-ples, 3-class (True/False/Unknown).\n\nLaTeX Warning: Reference `tab:folio_core' on page 4 undefined on input line 151\n.\n\n\nLaTeX Warning: Reference `tab:error_taxonomy' on page 4 undefined on input line\n 172.\n\n\nLaTeX Warning: Reference `tab:gt_repair' on page 4 undefined on input line 199.\n\n\n[4]\n\nLaTeX Warning: Reference `tab:multiround' on page 5 undefined on input line 225\n.\n\n\nLaTeX Warning: Reference `tab:repair_by_type' on page 5 undefined on input line\n 243.\n\n\nLaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 26\n8.\n\n\nLaTeX Warning: Reference `tab:logiqa' on page 5 undefined on input line 294.\n\n\nLaTeX Warning: Reference `tab:proofwriter_pilot' on page 5 undefined on input l\nine 316.\n\n[5]\n\nLaTeX Warning: Reference `tab:math' on page 6 undefined on input line 334.\n\n\nLaTeX Warning: Reference `tab:asymmetry_direction' on page 6 undefined on input\n line 354.\n\n\nLaTeX Warning: Reference `tab:correlated' on page 6 undefined on input line 378\n.\n\n\nLaTeX Warning: Reference `tab:selection_repair' on page 6 undefined on input li\nne 406.\n\n\nLaTeX Warning: Reference `tab:taxonomy_ablation' on page 6 undefined on input l\nine 433.\n\n[6]\n\nLaTeX Warning: Reference `tab:taxonomy_validation' on page 7 undefined on input\n line 462.\n\n\nLaTeX Warning: Reference `tab:crd_vs_sc' on page 7 undefined on input line 491.\n\n\n\nLaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 519.\n\n\nLaTeX Warning: Reference `tab:cross_domain' on page 7 undefined on input line 5\n45.\n\n[7]\n\nLaTeX Warning: Reference `tab:significance' on page 8 undefined on input line 5\n72.\n\n[8] [9] [10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] [12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 125536 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg) (./paper.out)\n(./paper.out) (/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg) [1{/var/lib/texm\nf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/d\nvips/base/8r.enc}] [2]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3] [4] [5] [6]\n[7] [8] [9] [10] [11] [12] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 130425 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eb8ce988-1136-4f1b-b8c0-7c00efb428df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representati…",
  "leafUuid": "0bc6ee38-5da2-4d17-8b27-1de7f3147d38",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement for model diagnosis",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Assistant

_source line 36 · 2026-05-15T07:39:09.706Z_

One more pass to resolve the label change warning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bc6ee38-5da2-4d17-8b27-1de7f3147d38",
  "isSidechain": false,
  "requestId": "req_011Cb3yTKB8sxHfn6Ucbo5yU",
  "type": "assistant",
  "uuid": "ccf44ddf-204f-4004-93a4-fa8396def3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Rqqi34KwphvFc3JtvU9sm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7165,
      "cache_read_input_tokens": 59834,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 59834,
          "cache_creation_input_tokens": 7165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7165
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

_source line 37 · 2026-05-15T07:39:12.583Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NrwmV8ZChkjHjh3DDJaAXr`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third pdflatex pass to resolve cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccf44ddf-204f-4004-93a4-fa8396def3cf",
  "isSidechain": false,
  "requestId": "req_011Cb3yTKB8sxHfn6Ucbo5yU",
  "type": "assistant",
  "uuid": "555f40df-d913-4f8d-8703-30b6e5137ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Rqqi34KwphvFc3JtvU9sm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7165,
      "cache_read_input_tokens": 59834,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 59834,
          "cache_creation_input_tokens": 7165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7165
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

_source line 38 · 2026-05-15T07:39:13.471Z_

<details><summary>↩ Tool result · `toolu_01NrwmV8ZChkjHjh3DDJaAXr`</summary>

```text
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utm
b8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 130425 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "555f40df-d913-4f8d-8703-30b6e5137ae0",
  "isSidechain": false,
  "promptId": "e4c0b4e3-fb24-41d4-9fcd-83ae051896ff",
  "type": "user",
  "uuid": "324d57e2-1543-4e23-bec2-d45cfde4c472",
  "toolUseResult": {
    "stdout": "amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utm\nb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 130425 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "555f40df-d913-4f8d-8703-30b6e5137ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T07:39:23.278Z_

PDF 编译成功——12 页，130KB。文件位于 `artifacts/dream_reports/dream_20260515T071730/best/paper.tex`（及 `paper.pdf`）。

论文覆盖 experiment_data.json 中全部 11 个实验，对应 17 张表：
- FOLIO 核心分析 (C1–C5, 错误分类, GT-stratified repair)
- 多轮修复 + 按错误类型成功率
- 跨模型消融 (Qwen / DeepSeek / cross-model)
- LogiQA 扩展 + ProofWriter pilot 失败
- MATH Level 5 + 不对称方向反转表
- 相关失败分析 (phi, false agreement)
- Selection vs Repair 消融
- Taxonomy-guided vs fixed-strategy 消融
- 跨模型 taxonomy 验证 (Cohen's κ)
- CRD vs SC5 对比
- 模型规模消融 (8B/32B/DeepSeek)
- 跨域边界 (GPQA)
- 统计显著性汇总

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "324d57e2-1543-4e23-bec2-d45cfde4c472",
  "isSidechain": false,
  "requestId": "req_011Cb3yTwSTb1JX1DEuA8gr5",
  "type": "assistant",
  "uuid": "70da3834-9654-4357-b404-238bfbf103b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011x4ehZKnCnoybsjTYTqEvq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 66999,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 66999,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 284
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representati…",
  "leafUuid": "70da3834-9654-4357-b404-238bfbf103b2",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement for model diagnosis",
  "sessionId": "7f902fb5-c92d-49c7-bbfa-c3d9da39d79d"
}
```

---
