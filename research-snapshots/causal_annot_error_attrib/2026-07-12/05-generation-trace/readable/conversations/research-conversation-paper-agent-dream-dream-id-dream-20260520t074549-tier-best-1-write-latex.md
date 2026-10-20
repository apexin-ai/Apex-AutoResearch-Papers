# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/91a9ab6d-de69-4f3c-8c74-05f4d04786ff.jsonl`
- **Structured JSON:** [`63c2ad889a27621d7a4c.json`](../../sessions/63/63c2ad889a27621d7a4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:24:18.255Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:24:18.255Z",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Version A 完全成立。Lead finding: non-differential K≥3 误分类在 4 个 DAG 拓扑（exposure, mediation, collider, front-door）中打破经典 toward-null 保证， 而 confounding 和 instrument 保持单调性。反转模式严格拓扑依赖——同一混淆矩阵在 confounding DAG 中仅引起可预测的残差偏倚，在 mediation/collider DAG 中却产生方向反转。 Headline: \"the same confusion matrix that is benign in confounding topology produces direction-reversing bias in mediation and collider topologies.\" ASV 框架在三个优先拓扑上均有完整单调性+紧性形式化证明，经验校准良好。Correction framework 在 95% 场景推荐最优方法。 Binarization collapse 分析强化了核心论点：K→2 折叠最大额外偏倚达 Δ=0.19，证明 binarization 不是安全退路。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T08:24:18.258Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:24:18.258Z",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-20T08:24:18.292Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Version A 完全成立。Lead finding: non-differential K≥3 误分类在 4 个 DAG 拓扑（exposure, mediation, collider, front-door）中打破经典 toward-null 保证， 而 confounding 和 instrument 保持单调性。反转模式严格拓扑依赖——同一混淆矩阵在 confounding DAG 中仅引起可预测的残差偏倚，在 mediation/collider DAG 中却产生方向反转。 Headline: "the same confusion matrix that is benign in confounding topology produces direction-reversing bias in mediation and collider topologies." ASV 框架在三个优先拓扑上均有完整单调性+紧性形式化证明，经验校准良好。Correction framework 在 95% 场景推荐最优方法。 Binarization collapse 分析强化了核心论点：K→2 折叠最大额外偏倚达 Δ=0.19，证明 binarization 不是安全退路。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "8a1fb5bb-ba24-4820-a9f2-4b7ba051e73a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:24:18.291Z_

```json
{
  "parentUuid": "8a1fb5bb-ba24-4820-a9f2-4b7ba051e73a",
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
  "uuid": "3d2bdd0b-27c9-4e5d-86b1-33efb28bee58",
  "timestamp": "2026-05-20T08:24:18.291Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:24:18.291Z_

```json
{
  "parentUuid": "3d2bdd0b-27c9-4e5d-86b1-33efb28bee58",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa7a899b-e172-467c-8519-b5591ab9cc69",
  "timestamp": "2026-05-20T08:24:18.291Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
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
  "aiTitle": "Generate causal annotation error attribution paper",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Assistant

_source line 7 · 2026-05-20T08:24:23.142Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa7a899b-e172-467c-8519-b5591ab9cc69",
  "isSidechain": false,
  "requestId": "req_011CbDVwuVw4vzq4JC2vYpGT",
  "type": "assistant",
  "uuid": "8014684f-a18d-4c8b-9c0d-7f86d4941e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZBishK8fNJhTS2WZeoPBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11806,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11806
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

_source line 8 · 2026-05-20T08:24:23.696Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UT2kkWYbVGTygEYSgshvF7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8014684f-a18d-4c8b-9c0d-7f86d4941e69",
  "isSidechain": false,
  "requestId": "req_011CbDVwuVw4vzq4JC2vYpGT",
  "type": "assistant",
  "uuid": "5c67425a-926e-4f8f-865d-78a00c3e9b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZBishK8fNJhTS2WZeoPBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11806,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11806
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

_source line 9 · 2026-05-20T08:24:23.996Z_

<details><summary>↩ Tool result · `toolu_01UT2kkWYbVGTygEYSgshvF7`</summary>

```text
1	[
2	  {
3	    "name": "Multi-topology bias derivation and MC validation (K=3)",
4	    "description": "对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 闭式偏倚表达式， 每个拓扑用 6 种混淆矩阵结构 × 1000 MC reps × N=10000 验证。另对 mediation/collider/front-door/M-bias/instrument 执行 100k random C 搜索，检测方向反转违背率。\n",
5	    "results": {
6	      "theory_mc_match_rate": 0.972,
7	      "theory_mc_match_detail": "35/36 structure×topology 组合落入 95% MC CI；1 个边界 case（front-door + rank-deficient C）偏差 0.003 超 CI 上界，增加到 N=50000 后收敛",
8	      "reversal_topologies_count": 4,
9	      "reversal_topologies": [
10	        "exposure (MVP)",
11	        "mediation",
12	        "collider",
13	        "front-door"
14	      ],
15	      "non_reversal_topologies": [
16	        "confounding",
17	        "instrument"
18	      ],
19	      "mediation_violation_rate": 0.52,
20	      "mediation_sign_reversal_rate": 0.47,
21	      "mediation_amplification_rate": 0.11,
22	      "collider_violation_rate": 0.41,
23	      "collider_sign_reversal_rate": 0.36,
24	      "collider_amplification_rate": 0.09,
25	      "frontdoor_violation_rate": 0.34,
26	      "frontdoor_sign_reversal_rate": 0.28,
27	      "frontdoor_amplification_rate": 0.12,
28	      "mbias_violation_rate": 0.0,
29	      "mbias_bias_range": [
30	        0.04,
31	        0.18
32	      ],
33	      "instrument_violation_rate": 0.0,
34	      "instrument_bias_range": [
35	        0.02,
36	        0.14
37	      ],
38	      "confounding_violation_rate": 0.0,
39	      "confounding_bias_range": [
40	        0.063,
41	        0.298
42	      ],
43	      "mediation_worst_case": "β_indirect=0.5 → estimate=-0.31 (sign reversal, 1.62x amplification)",
44	      "collider_worst_case": "β_XY=0.0 (null) → estimate=0.44 (spurious effect creation + direction assignment)",
45	      "frontdoor_worst_case": "β_total=0.8 → estimate=-0.22 (sign reversal via second-stage distortion)"
46	    },
47	    "tables": [
48	      {
49	        "name": "Table 1: Topology × Reversal Summary",
50	        "columns": [
51	          "Topology",
52	          "Role of Annotated Variable",
53	          "Violation Rate (100k)",
54	          "Sign Reversal Rate",
55	          "Amplification Rate",
56	          "Worst-Case Severity",
57	          "K=2 Control"
58	        ],
59	        "rows": [
60	          [
61	            "Confounding",
62	            "Confounder",
63	            "0.000",
64	            "0.000",
65	            "0.000",
66	            "0.298 (toward OVB)",
67	            "toward OVB ✓"
68	          ],
69	          [
70	            "Exposure (MVP)",
71	            "Treatment",
72	            "0.850",
73	            "0.834",
74	            "0.141",
75	            "2.83x amplification",
76	            "toward null ✓"
77	          ],
78	          [
79	            "Mediation",
80	            "Mediator",
81	            "0.520",
82	            "0.470",
83	            "0.110",
84	            "1.62x + sign reversal",
85	            "toward null ✓"
86	          ],
87	          [
88	            "Collider",
89	            "Collider",
90	            "0.410",
91	            "0.360",
92	            "0.090",
93	            "spurious 0.44 from null",
94	            "attenuated ✓"
95	          ],
96	          [
97	            "M-bias",
98	            "M-bias variable",
99	            "0.000",
100	            "0.000",
101	            "0.000",
102	            "0.18 (attenuated)",
103	            "attenuated ✓"
104	          ],
105	          [
106	            "Instrument",
107	            "Instrument",
108	            "0.000",
109	            "0.000",
110	            "0.000",
111	            "ratio distortion 0.14",
112	            "attenuated ✓"
113	          ],
114	          [
115	            "Front-door",
116	            "Front-door variable",
117	            "0.340",
118	            "0.280",
119	            "0.120",
120	            "sign reversal",
121	            "toward null ✓"
122	          ]
123	        ]
124	      },
125	      {
126	        "name": "Table 2: Theory-MC Match per Topology × C Structure",
127	        "columns": [
128	          "Topology",
129	          "Diagonal-dominant",
130	          "Moderate off-diag",
131	          "Uniform off-diag",
132	          "Block-diagonal",
133	          "Near-permutation",
134	          "Rank-deficient",
135	          "Match Rate"
136	        ],
137	        "rows": [
138	          [
139	            "Confounding",
140	            "✓",
141	            "✓",
142	            "✓",
143	            "✓",
144	            "✓",
145	            "✓",
146	            "6/6"
147	          ],
148	          [
149	            "Mediation",
150	            "✓",
151	            "✓",
152	            "✓",
153	            "✓",
154	            "✓",
155	            "✓",
156	            "6/6"
157	          ],
158	          [
159	            "Collider",
160	            "✓",
161	            "✓",
162	            "✓",
163	            "✓",
164	            "✓",
165	            "✓",
166	            "6/6"
167	          ],
168	          [
169	            "M-bias",
170	            "✓",
171	            "✓",
172	            "✓",
173	            "✓",
174	            "✓",
175	            "✓",
176	            "6/6"
177	          ],
178	          [
179	            "Instrument",
180	            "✓",
181	            "✓",
182	            "✓",
183	            "✓",
184	            "✓",
185	            "✓",
186	            "6/6"
187	          ],
188	          [
189	            "Front-door",
190	            "✓",
191	            "✓",
192	            "✓",
193	            "✓",
194	            "✓",
195	            "△*",
196	            "5/6"
197	          ]
198	        ]
199	      }
200	    ],
201	    "figures": [],
202	    "analysis": "核心发现：非差异 K≥3 误分类的方向反转是拓扑依赖的。6 个拓扑分为两类：(1) 信息丢失型（confounding, instrument, M-bias）—— 误分类只能减少变量的信息量，偏倚方向可预测；(2) 结构扭曲型（exposure, mediation, collider, front-door）—— 误分类改变变量在 DAG 中的功能角色（如 mediator 的类别标签互换等价于改变 M→Y 的函数形式）， 导致不可预测的方向反转。这一二分法是论文的核心理论贡献。Confounding DAG 的\"良性\"行为不可推广到其他拓扑， 这直接挑战了实践者\"non-differential error is conservative\"的默认假设。\n\n\nMediation (violation rate 0.52): 间接效应 = β_XM × β_MY|X。K≥3 非差异误分类扭曲 M→Y|X 回归系数—— 近置换矩阵 C 使相邻类别标签互换，导致 β_MY|X 符号翻转，从而间接效应反转。K=2 下非差异误分类只能将 β_MY|X  向零压缩（attenuation），结构上不可能越过零点。violation rate 0.52 而非更高（对比 exposure 的 0.85）， 因为间接效应经过两步回归（X→M 和 M→Y|X），仅当 C 同时严重扰动 M 的条件分布时才出现反转， 而 exposure 误分类直接作用于处理变量，单步即可反转。\nCollider (violation rate 0.41): 对 collider C̃ 条件化打开伪路径 X←U→C←V→Y。K≥3 误分类改变条件化的 有效权重——不同类别的合并创造不同的伪关联模式。violation rate 低于 mediation 因为反转需要 C 矩阵 使 X-path 和 Y-path 的贡献权重同时满足特定比例条件，约束更强。\nFront-door (violation rate 0.34): 前门调整涉及两阶段估计（X→M 和 M→Y|do(X)）。K≥3 误分类不对称地 扭曲两个阶段——第一阶段 attenuation 与第二阶段 distortion 的交互可使整体估计翻转。violation rate  最低因为反转需要两阶段同时被 C 严重扰动且扰动方向\"配合\"，是三个反转拓扑中约束最强的。\nConfounding (violation rate 0.0): 已由 MVP 确认。残差混淆始终朝向 OVB 方向，因为误分类只能减少 confounder 的解释力（信息丢失），不能创造新的混淆结构。K≥3 增加了更多丢失信息的方式但不改变方向性。\nInstrument (violation rate 0.0): Wald estimator = Cov(Y,Z̃)/Cov(X,Z̃)。非差异误分类对 Z 的两个 协方差施加相同方向的 attenuation（均乘以 C 的特征值相关因子），比值的符号不变。 K≥3 下分子分母的 attenuation 系数不再相同（不同特征值），导致幅度偏倚但符号保持。\nM-bias (violation rate 0.0): M-bias（蝴蝶 DAG）中被误分类的变量本不应被条件化。 误分类使条件化效应减弱（信息丢失方向），偏倚幅度变化但不反转。\n"
203	  },
204	  {
205	    "name": "General K bias expressions with interpretability tools (K=5,7)",
206	    "description": "将偏倚表达式推广到矩阵形式（一般 K）。开发三种可解释性工具：(a) 特征分解摘要，(b) 最坏情况标量界， (c) 诊断可视化。在 confounding + mediation + collider DAG 上用 K=5,7 验证。\n",
207	    "results": {
208	      "eigendecomposition_variance_captured_top2": 0.87,
209	      "eigendecomposition_variance_captured_top3": 0.96,
210	      "worstcase_bound_tightness": 0.88,
211	      "worstcase_bound_tightness_detail": "最坏情况标量界在 88% 的场景中与真实最坏情况偏差 <15%",
212	      "K5_mediation_violation_rate": 0.61,
213	      "K5_collider_violation_rate": 0.49,
214	      "K7_mediation_violation_rate": 0.68,
215	      "K7_collider_violation_rate": 0.55,
216	      "K5_confounding_reversal": false,
217	      "K7_confounding_reversal": false,
218	      "theory_mc_match_K5": "17/18 within 95% CI",
219	      "theory_mc_match_K7": "16/18 within 95% CI"
220	    },
221	    "tables": [
222	      {
223	        "name": "Table 3: Violation Rate Scaling with K",
224	        "columns": [
225	          "Topology",
226	          "K=3",
227	          "K=5",
228	          "K=7",
229	          "Trend"
230	        ],
231	        "rows": [
232	          [
233	            "Confounding",
234	            "0.000",
235	            "0.000",
236	            "0.000",
237	            "Stable at 0 (monotonic toward OVB)"
238	          ],
239	          [
240	            "Mediation",
241	            "0.520",
242	            "0.610",
243	            "0.680",
244	            "Monotonically increasing"
245	          ],
246	          [
247	            "Collider",
248	            "0.410",
249	            "0.490",
250	            "0.550",
251	            "Monotonically increasing"
252	          ]
253	        ]
254	      },
255	      {
256	        "name": "Table 4: Eigendecomposition Variance Explained",
257	        "columns": [
258	          "Topology",
259	          "K",
260	          "Top-1 EV%",
261	          "Top-2 EV%",
262	          "Top-3 EV%"
263	        ],
264	        "rows": [
265	          [
266	            "Confounding",
267	            "5",
268	            "72%",
269	            "89%",
270	            "97%"
271	          ],
272	          [
273	            "Confounding",
274	            "7",
275	            "68%",
276	            "85%",
277	            "95%"
278	          ],
279	          [
280	            "Mediation",
281	            "5",
282	            "70%",
283	            "87%",
284	            "96%"
285	          ],
286	          [
287	            "Mediation",
288	            "7",
289	            "65%",
290	            "84%",
291	            "94%"
292	          ],
293	          [
294	            "Collider",
295	            "5",
296	            "71%",
297	            "88%",
298	            "96%"
299	          ],
300	          [
301	            "Collider",
302	            "7",
303	            "66%",
304	            "85%",
305	            "95%"
306	          ]
307	        ]
308	      }
309	    ],
310	    "figures": [],
311	    "analysis": "K 增大强化了核心论点：随着分类粒度增加，binary 近似的失效更严重，方向反转概率上升。 可解释性工具使 K≥5 的矩阵偏倚表达式在实践中可用：研究者无需理解完整 K×K 偏倚矩阵， 只需检查 top-2 特征模式即可判断偏倚的方向和严重程度。最坏情况标量界为风险厌恶型研究者 提供保守但可操作的单一数字。\n\n\nK 增大时 violation rate 单调上升（mediation: 0.52→0.61→0.68；collider: 0.41→0.49→0.55）， 因为混淆矩阵的自由参数从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。 更高维度的 C 矩阵有更多\"方向\"可以扭曲类别映射，使得 random search 中遇到反转配置的概率增加。\n特征分解 top-2 捕获 87% 方差：偏倚矩阵 B = f(C) 的谱结构由 C 的谱结构决定。 C 通常是行随机矩阵（行和为 1），其最大特征值为 1（对应\"保真\"模式），第二大特征值 对应主要误分类模式。因此 B 的前 2 个特征值对应\"无偏\"基线和\"主误分类方向\"， 合计解释大部分方差。top-3 达 96% 因为第三个模式捕获了次要误分类模式。\n最坏情况标量界紧度 88%：该界通过对 B 的谱范数取上界得到，对于高对角优势 C  这个界很紧（谱范数 ≈ 最大特征值），但对于结构化偏差（如 block-diagonal C） 谱范数高估约 25-30%，拉低了整体紧度。\nTheory-MC match 在 K=7 时略降（16/18 vs K=3 的 35/36）：高维 MC 模拟的方差增大， 需要更大 N 才能达到同样精度。2 个未匹配 case 均为 near-permutation extreme， 增加到 N=50000 后收敛。\n"
312	  },
313	  {
314	    "name": "Empirical confusion matrices: 3 LLMs × 3 CSS tasks",
315	    "description": "收集 3 个 LLM（Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4）在 3 个 CSS 任务 （protest event coding K=5, stance detection K=3, toxicity K=2）上的实证混淆矩阵。 ~30K annotations per model × 3 datasets × 3 prompt variants。\n",
316	    "results": {
317	      "total_annotations": "~270K (3 models × 3 tasks × ~30K)",
318	      "protest_K5_avg_diagonal_dominance": 0.62,
319	      "protest_K5_inter_model_kappa": 0.71,
320	      "stance_K3_avg_diagonal_dominance": 0.74,
321	      "stance_K3_inter_model_kappa": 0.68,
322	      "toxicity_K2_avg_accuracy": 0.89,
323	      "toxicity_K2_inter_model_kappa": 0.76,
324	      "cross_model_error_correlation": 0.58,
325	      "cross_model_error_correlation_detail": "当两个模型均出错时，58% 的 case 错向同一类别（与 Kim et al. 的 60% 一致）",
326	      "distinct_C_structures_observed": 9,
327	      "near_permutation_cases": 2,
328	      "block_diagonal_cases": 3,
329	      "prompt_variant_C_shift": "prompt 变体导致 C 结构在 Frobenius 距离上变化 0.04-0.12",
330	      "downstream_bias_vs_gold_protest": [
331	        -0.08,
332	        0.15
333	      ],
334	      "downstream_bias_vs_gold_stance": [
335	        -0.05,
336	        0.09
337	      ],
338	      "downstream_bias_vs_gold_toxicity": [
339	        -0.02,
340	        0.03
341	      ]
342	    },
343	    "tables": [
344	      {
345	        "name": "Table 5: Empirical Confusion Matrix Summary",
346	        "columns": [
347	          "Task",
348	          "K",
349	          "Model",
350	          "Accuracy",
351	          "Diagonal Dominance",
352	          "Largest Off-Diag",
353	          "C Structure Type"
354	        ],
355	        "rows": [
356	          [
357	            "Protest",
358	            "5",
359	            "Llama 4 Maverick",
360	            "0.64",
361	            "0.60",
362	            "0.18 (strat_dev→peaceful)",
363	            "Moderate off-diag"
364	          ],
365	          [
366	            "Protest",
367	            "5",
368	            "Qwen 3.5 Plus",
369	            "0.60",
370	            "0.57",
371	            "0.21 (strat_dev→peaceful)",
372	            "Near-permutation"
373	          ],
374	          [
375	            "Protest",
376	            "5",
377	            "DeepSeek V4",
378	            "0.67",
379	            "0.63",
380	            "0.15 (other→gov_resp)",
381	            "Block-diagonal"
382	          ],
383	          [
384	            "Stance",
385	            "3",
386	            "Llama 4 Maverick",
387	            "0.77",
388	            "0.76",
389	            "0.14 (neutral→against)",
390	            "Block-diagonal"
391	          ],
392	          [
393	            "Stance",
394	            "3",
395	            "Qwen 3.5 Plus",
396	            "0.73",
397	            "0.72",
398	            "0.16 (against→neutral)",
399	            "Block-diagonal"
400	          ],
401	          [
402	            "Stance",
403	            "3",
404	            "DeepSeek V4",
405	            "0.76",
406	            "0.75",
407	            "0.13 (neutral→against)",
408	            "Block-diagonal"
409	          ],
410	          [
411	            "Toxicity",
412	            "2",
413	            "Llama 4 Maverick",
414	            "0.91",
415	            "0.91",
416	            "0.09 (toxic→non-toxic)",
417	            "Diagonal-dominant"
418	          ],
419	          [
420	            "Toxicity",
421	            "2",
422	            "Qwen 3.5 Plus",
423	            "0.87",
424	            "0.87",
425	            "0.13 (non-toxic→toxic)",
426	            "Diagonal-dominant"
427	          ],
428	          [
429	            "Toxicity",
430	            "2",
431	            "DeepSeek V4",
432	            "0.90",
433	            "0.90",
434	            "0.10 (toxic→non-toxic)",
435	            "Diagonal-dominant"
436	          ]
437	        ]
438	      },
439	      {
440	        "name": "Table 6: Inter-Model Error Agreement",
441	        "columns": [
442	          "Task",
443	          "Model Pair",
444	          "Cohen's κ",
445	          "Error Agreement Rate",
446	          "Same-Direction Error %"
447	        ],
448	        "rows": [
449	          [
450	            "Protest",
451	            "Llama-Qwen",
452	            "0.69",
453	            "0.24",
454	            "0.61"
455	          ],
456	          [
457	            "Protest",
458	            "Llama-DeepSeek",
459	            "0.72",
460	            "0.21",
461	            "0.57"
462	          ],
463	          [
464	            "Protest",
465	            "Qwen-DeepSeek",
466	            "0.68",
467	            "0.25",
468	            "0.56"
469	          ],
470	          [
471	            "Stance",
472	            "Llama-Qwen",
473	            "0.67",
474	            "0.18",
475	            "0.59"
476	          ],
477	          [
478	            "Stance",
479	            "Llama-DeepSeek",
480	            "0.70",
481	            "0.16",
482	            "0.58"
483	          ],
484	          [
485	            "Stance",
486	            "Qwen-DeepSeek",
487	            "0.66",
488	            "0.19",
489	            "0.57"
490	          ],
491	          [
492	            "Toxicity",
493	            "All pairs avg",
494	            "0.76",
495	            "0.09",
496	            "0.62"
497	          ]
498	        ]
499	      }
500	    ],
501	    "figures": [],
502	    "analysis": "实证 C 矩阵覆盖了理论分析中的多种结构类型（diagonal-dominant, block-diagonal, near-permutation）， 为后续 ASV 校准和 correction framework 验证提供了现实基础。关键观察： (1) Protest coding 的 C 矩阵接近 plan_001 中产生反转的区域，预示该任务在 mediation/collider  拓扑下风险最高；(2) 跨模型错误高度相关，确认多 LLM 集成不是解决方案； (3) Prompt 变体可显著移动 C 结构（Frobenius Δ 达 0.12），暗示 prompt engineering  本身是一种（未被充分认识的）bias intervention。\n\n\nProtest event coding (K=5) 对角优势最低（0.62）：5 类任务（peaceful protest, violent protest,  strategic development, government response, other）存在固有歧义——\"strategic development\"与  \"peaceful protest\"常被混淆，LLM 倾向于对 borderline case 系统性偏向高频类别。 低对角优势意味着 C 矩阵偏离对角，更接近 random search 中产生反转的区域。\nStance detection (K=3) 对角优势较高（0.74）：3 类（favor, against, neutral）语义距离较大， 但 neutral 与 against 的边界模糊导致特定 off-diagonal 元素偏高，形成 block-diagonal 结构 （favor 与 against/neutral 分离，但 against-neutral 互相混淆）。\nToxicity (K=2) 准确率最高（0.89）：二分类任务较简单，且 toxicity 有较清晰的语言标记。 作为 binary special case / consistency check——K=2 下所有模型的偏倚均 toward null， 与理论预测一致。\n跨模型错误相关 0.58：Kim et al. (ICML 2025) 报告 60%，我们的 0.58 高度一致。 这不是巧合——LLM 共享类似的预训练数据和推理模式，对同类歧义样本倾向于犯同类错误。 这个发现强化了我们的论点：多模型集成无法消除系统性偏倚，必须分析 C 结构。\n9 种不同 C 结构（3 models × 3 tasks）为后续 ASV 校准提供了充分多样性。 2 个 near-permutation cases 出现在 protest coding 的特定 prompt 变体下（过度指令化导致 类别定义混乱），3 个 block-diagonal cases 出现在 stance detection 中（favor 孤立）。\n"
503	  },
504	  {
505	    "name": "Binarization collapse analysis across all topologies",
506	    "description": "对 6 个拓扑 + exposure（共 7 个拓扑），K=3,5,7 条件下，将 K 类变量折叠为二分类， 比较完整多类偏倚表达式 vs 二值化后偏倚表达式的差异 Δ。\n",
507	    "results": {
508	      "binarization_max_delta": 0.19,
509	      "binarization_max_delta_topology": "mediation",
510	      "binarization_max_delta_K": 7,
511	      "binarization_avg_delta_K3": 0.08,
512	      "binarization_avg_delta_K5": 0.13,
513	      "binarization_avg_delta_K7": 0.16,
514	      "binarization_direction_reversal_cases": "12% of K=5,7 scenarios show Δ that flips bias direction",
515	      "binarization_delta_by_topology": {
516	        "confounding_K3": 0.06,
517	        "confounding_K5": 0.09,
518	        "confounding_K7": 0.11,
519	        "mediation_K3": 0.1,
520	        "mediation_K5": 0.15,
521	        "mediation_K7": 0.19,
522	        "collider_K3": 0.09,
523	        "collider_K5": 0.14,
524	        "collider_K7": 0.17,
525	        "exposure_K3": 0.08,
526	        "exposure_K5": 0.12,
527	        "exposure_K7": 0.15,
528	        "mbias_K3": 0.05,
529	        "mbias_K5": 0.08,
530	        "mbias_K7": 0.1,
531	        "instrument_K3": 0.04,
532	        "instrument_K5": 0.07,
533	        "instrument_K7": 0.09,
534	        "frontdoor_K3": 0.09,
535	        "frontdoor_K5": 0.13,
536	        "frontdoor_K7": 0.16
537	      }
538	    },
539	    "tables": [
540	      {
541	        "name": "Table 7: Binarization Collapse Δ by Topology × K",
542	        "columns": [
543	          "Topology",
544	          "K=3 Δ",
545	          "K=5 Δ",
546	          "K=7 Δ",
547	          "Max Δ",
548	          "Direction Reversal by Δ?"
549	        ],
550	        "rows": [
551	          [
552	            "Confounding",
553	            "0.06",
554	            "0.09",
555	            "0.11",
556	            "0.11",
557	            "No"
558	          ],
559	          [
560	            "Exposure",
561	            "0.08",
562	            "0.12",
563	            "0.15",
564	            "0.15",
565	            "Yes (3% of K=7)"
566	          ],
567	          [
568	            "Mediation",
569	            "0.10",
570	            "0.15",
571	            "0.19",
572	            "0.19",
573	            "Yes (18% of K=7)"
574	          ],
575	          [
576	            "Collider",
577	            "0.09",
578	            "0.14",
579	            "0.17",
580	            "0.17",
581	            "Yes (14% of K=7)"
582	          ],
583	          [
584	            "M-bias",
585	            "0.05",
586	            "0.08",
587	            "0.10",
588	            "0.10",
589	            "No"
590	          ],
591	          [
592	            "Instrument",
593	            "0.04",
594	            "0.07",
595	            "0.09",
596	            "0.09",
597	            "No"
598	          ],
599	          [
600	            "Front-door",
601	            "0.09",
602	            "0.13",
603	            "0.16",
604	            "0.16",
605	            "Yes (11% of K=7)"
606	          ]
607	        ]
608	      }
609	    ],
610	    "figures": [],
611	    "analysis": "Binarization 不是安全退路。Max Δ = 0.19 在实际社会科学研究中足以改变实质性结论 （典型效应量 0.1-0.3）。这一结果与 MVP 中 confounding DAG 的 Δ=0.103 一致且推广： 更多拓扑、更高 K 值下 Δ 更大。结合 plan_001 的方向反转结果，完整论点是： (1) 保留多类可能导致方向反转，(2) 折叠为二类也不安全——研究者无处可逃，必须使用 ASV 框架 诊断其具体 {C × topology} 组合的偏倚性质。\n\n\nBinarization max Δ = 0.19（mediation, K=7）：折叠 7 类 mediator 为二分类丢弃了类别间的 细粒度偏倚结构。Mediation DAG 中间接效应依赖 M 的分布形状——当 7 个类别被折叠为 2 个时， 被合并的类别可能具有相反方向的 M→Y 效应，导致折叠后的间接效应与原始间接效应方向相反。 K=7 比 K=3 更严重因为折叠时信息丢失更多（5 个类别被合并 vs 1 个类别被合并）。\nΔ 随 K 单调增大（avg: 0.08→0.13→0.16）：这是信息论上的必然——K→2 折叠的信息丢失 量为 log(K)-log(2)，K 越大丢失越多。\n12% 的 K=5,7 场景中 Δ 本身导致方向翻转：这意味着研究者试图通过 binarization  \"逃入\"二分类安全区域的策略不仅无效（因为折叠引入新偏倚），而且在 12% 的场景中 反而比保留多类更危险。这个发现直接回应了一个预期的 reviewer concern： \"既然 binary case 有保证，为什么不直接 binarize？\"\nMediation > Collider > Front-door > Exposure > Confounding > M-bias > Instrument 的 Δ 排序： Mediation 最大因为间接效应的非线性依赖 M 的类别分布；Instrument 最小因为 IV 估计 主要依赖 Z 的第一阶段 F-statistic，对类别合并方式的敏感度较低。\n"
612	  },
613	  {
614	    "name": "ASV formal proofs for 3 priority topologies",
615	    "description": "推导 confounding, mediation, collider 三个优先拓扑的 ASV 表达式。 形式化证明单调性（ASV 随 δ 增大而增大）和紧性（bound 可被某个 C 达到）。 MC 验证：1000 scenarios × coverage at 90%, 95%, 99% levels。\n",
616	    "results": {
617	      "asv_sharpness_formal_proofs": 3,
618	      "asv_monotonicity_proofs": 3,
619	      "proof_technique_confounding": "algebraic — closed-form ASV as function of spectral gap of C and δ",
620	      "proof_technique_mediation": "algebraic + envelope theorem — indirect effect ASV via product-of-coefficients decomposition",
621	      "proof_technique_collider": "algebraic + Lagrangian optimization — ASV as constrained optimization over C perturbation space",
622	      "asv_coverage_90_nominal": 0.912,
623	      "asv_coverage_95_nominal": 0.952,
624	      "asv_coverage_99_nominal": 0.988,
625	      "asv_coverage_by_topology": {
626	        "confounding_95": 0.958,
627	        "mediation_95": 0.949,
628	        "collider_95": 0.948
629	      },
630	      "mc_scenarios": 1000,
631	      "mc_reps_per_scenario": 500,
632	      "sharpness_achieving_C_found": "100% of scenarios — constructive proof provides explicit C* achieving bound"
633	    },
634	    "tables": [
635	      {
636	        "name": "Table 8: ASV Formal Proof Summary",
637	        "columns": [
638	          "Topology",
639	          "Monotonicity",
640	          "Sharpness",
641	          "Proof Technique",
642	          "Constructive C*?"
643	        ],
644	        "rows": [
645	          [
646	            "Confounding",
647	            "✓ Proved",
648	            "✓ Proved",
649	            "Algebraic (spectral gap)",
650	            "Yes — explicit"
651	          ],
652	          [
653	            "Mediation",
654	            "✓ Proved",
655	            "✓ Proved",
656	            "Algebraic + envelope theorem",
657	            "Yes — explicit"
658	          ],
659	          [
660	            "Collider",
661	            "✓ Proved",
662	            "✓ Proved",
663	            "Lagrangian optimization + KKT",
664	            "Yes — explicit"
665	          ]
666	        ]
667	      },
668	      {
669	        "name": "Table 9: ASV Coverage Calibration (MC, 1000 scenarios)",
670	        "columns": [
671	          "Topology",
672	          "Nominal 90%",
673	          "Actual 90%",
674	          "Nominal 95%",
675	          "Actual 95%",
676	          "Nominal 99%",
677	          "Actual 99%"
678	        ],
679	        "rows": [
680	          [
681	            "Confounding",
682	            "90%",
683	            "91.8%",
684	            "95%",
685	            "95.8%",
686	            "99%",
687	            "99.2%"
688	          ],
689	          [
690	            "Mediation",
691	            "90%",
692	            "90.9%",
693	            "95%",
694	            "94.9%",
695	            "99%",
696	            "98.7%"
697	          ],
698	          [
699	            "Collider",
700	            "90%",
701	            "90.8%",
702	            "95%",
703	            "94.8%",
704	            "99%",
705	            "98.5%"
706	          ],
707	          [
708	            "Average",
709	            "90%",
710	            "91.2%",
711	            "95%",
712	            "95.2%",
713	            "99%",
714	            "98.8%"
715	          ]
716	        ]
717	      }
718	    ],
719	    "figures": [],
720	    "analysis": "三个完整形式化证明是本论文最重要的理论贡献之一。ASV 类比于因果推断中的 E-value： E-value 量化 \"多大的未测量混淆才能推翻结论\"，ASV 量化 \"多大的标注误差才能推翻结论\"。 关键区别：E-value 只需一个标量参数（RR），ASV 需要参考混淆矩阵 + δ 方向， 因此证明复杂度更高。构造性紧性证明（显式 C*）不仅有理论价值，还有实践价值—— 研究者可以检查 \"使结论翻转的最近 C* 与我的实证 C 有多远\"，获得直觉性理解。\n\n\n三个证明均成功（asv_sharpness_formal_proofs = 3）：这是 best tier 的硬性要求，但也是 数学上可行的，因为三个拓扑的偏倚表达式在 K=3 时有足够简洁的闭式形式。\nConfounding ASV：残差混淆偏倚 = OVB × (1 - f(C))，其中 f(C) 是 C 的对角优势函数。 ASV = min{δ : |OVB × (1-f(C·diag(1+δ)))| > threshold}。单调性：f 关于 δ 单调递减 （扰动增大→C 偏离对角→更多残差混淆），因此 ASV 单调。紧性：构造 C* = 在 δ 约束下 使 f(C*) 最小化的行随机矩阵（显式构造）。\nMediation ASV：间接效应 = β_XM × β_MY|X，两者均是 C 的函数。ASV 通过乘积分解为 两个单调函数的乘积——当两者符号一致时整体单调，当符号不一致时需要 envelope theorem 处理极值切换，但最终仍可证明关于 δ 的单调性。紧性通过构造性 Lagrangian 求解 使间接效应恰好等于 threshold 的 C*。\nCollider ASV：条件化打开伪路径的效应大小是 C 的非线性函数。通过 Lagrangian 优化 在 {C : ||C - I|| ≤ g(δ)} 约束集上求解伪效应的极值，证明该极值关于 δ 单调。 紧性：Lagrangian 的 KKT 条件给出显式 C*。\nCoverage at 95% nominal = 0.952（在 [0.93, 0.97] 范围内）：轻微过覆盖（0.952 > 0.950） 是因为 ASV bound 使用了保守的 worst-case C 方向，而大多数实际 C 不在最坏方向上。 这种过覆盖是良性的（保守偏倚）。Mediation (0.949) 和 collider (0.948) 的覆盖率 略低于 confounding (0.958)，因为这两个拓扑的偏倚函数非线性更强， ASV 的线性化近似在极端 δ 值附近不够精确。\n"
721	  },
722	  {
723	    "name": "ASV MC validation for remaining 3 topologies",
724	    "description": "对 M-bias, instrument, front-door 三个拓扑推导 ASV 表达式，MC 验证单调性和覆盖率。 紧性作为猜想，用数值证据支持。\n",
725	    "results": {
726	      "asv_monotonicity_mc_validated": 3,
727	      "asv_monotonicity_violations": 0,
728	      "asv_coverage_95_mbias": 0.954,
729	      "asv_coverage_95_instrument": 0.961,
730	      "asv_coverage_95_frontdoor": 0.943,
731	      "sharpness_numerical_gap": "< 0.008 across all 3 topologies (bound within 0.8% of achievable)",
732	      "sharpness_conjecture_status": "Supported by 1000 scenario numerical optimization — no counterexample found",
733	      "frontdoor_asv_note": "Front-door ASV 涉及两阶段估计的联合扰动，闭式紧性证明需要解决双线性约束优化，identified as immediate future work"
734	    },
735	    "tables": [
736	      {
737	        "name": "Table 10: ASV Validation for Remaining Topologies",
738	        "columns": [
739	          "Topology",
740	          "Monotonicity",
741	          "Coverage @95%",
742	          "Sharpness Gap",
743	          "Formal Proof Status"
744	        ],
745	        "rows": [
746	          [
747	            "M-bias",
748	            "✓ MC-validated (0 violations/1000)",
749	            "95.4%",
750	            "0.006",
751	            "Conjecture (numerical)"
752	          ],
753	          [
754	            "Instrument",
755	            "✓ MC-validated (0 violations/1000)",
756	            "96.1%",
757	            "0.005",
758	            "Conjecture (numerical)"
759	          ],
760	          [
761	            "Front-door",
762	            "✓ MC-validated (0 violations/1000)",
763	            "94.3%",
764	            "0.008",
765	            "Conjecture (numerical)"
766	          ]
767	        ]
768	      }
769	    ],
770	    "figures": [],
771	    "analysis": "诚实地将紧性限定为猜想（而非证明）是策略性选择：(1) 避免 reviewer 质疑证明严谨性， (2) 数值证据已经足够有说服力（gap < 0.008），(3) 完整证明作为 immediate future work  为后续论文提供了明确方向。六个拓扑的 ASV 框架完整性：3 个有完整证明 + 3 个有强数值支持， 覆盖了实践者可能遇到的所有主要 DAG 设计。\n\n\n单调性在所有 3 个拓扑的 MC 验证中均成立（0 violations）：单调性是一个\"自然\"性质—— 更大的标注误差（更大的 δ）只能增加偏倚的潜在范围，不能减少它。这在直觉上成立： δ 增大扩展了 C 的可行域，而偏倚 bound 是在可行域上的 supremum， 可行域扩大 → supremum 不减。形式化证明的技术难点在于处理非凸可行域， 但 MC 验证表明即使在解析证明困难的情况下，性质仍成立。\n紧性作为猜想而非证明：M-bias 的 DAG 结构（butterfly）使偏倚表达式涉及 4 个 条件概率的乘积，优化问题是四次多项式约束优化，闭式解不可行。 Instrument 的 Wald ratio 使约束优化涉及分式规划。 Front-door 的两阶段结构使约束是双线性的。 数值优化（sequential quadratic programming）在所有场景中找到的最优 C  与 ASV bound 的差距 < 0.008，强烈支持紧性但不构成证明。\nFront-door coverage 略低（0.943）：两阶段估计的非线性使 ASV 的线性化近似 在 extreme δ 附近不够精确，但仍在 [0.93, 0.97] 范围内。\n"
772	  },
773	  {
774	    "name": "ASV calibration on empirical data",
775	    "description": "将 ASV 框架应用于 plan_003 的实证混淆矩阵。在 held-out gold-standard splits 上验证覆盖率。 报告 ASV alongside downstream effect estimates。比较 ASV 可解释性与原始混淆矩阵报告。\n",
776	    "results": {
777	      "empirical_asv_concordance": 8,
778	      "empirical_asv_concordance_detail": "9 个 scenario（3 tasks × 3 topological contexts）中 8 个 ASV 排序与实际 bias 严重度一致",
779	      "discordant_case": "protest × instrument context: ASV 排序 DeepSeek > Qwen，实际 bias Qwen > DeepSeek（差异 0.02，在 noise margin 内）",
780	      "asv_interpretability_rating": "研究者 pilot（N=5）中 4/5 偏好 ASV + sensitivity curve 而非原始 C 矩阵",
781	      "held_out_coverage_95": 0.94,
782	      "asv_actionable_alerts": "3/9 scenarios ASV < 1.5（结论脆弱），6/9 ASV > 3.0（结论稳健）",
783	      "asv_correctly_flags_reversal_risk": "2/2 scenarios where empirical C falls in reversal zone are flagged by ASV < 1.5"
784	    },
785	    "tables": [
786	      {
787	        "name": "Table 11: ASV Concordance with Empirical Bias Severity",
788	        "columns": [
789	          "Task",
790	          "Topological Context",
791	          "Model Ranking by ASV",
792	          "Model Ranking by Actual Bias",
793	          "Concordant?"
794	        ],
795	        "rows": [
796	          [
797	            "Protest",
798	            "Mediation",
799	            "Qwen < Llama < DeepSeek",
800	            "Qwen < Llama < DeepSeek",
801	            "✓"
802	          ],
803	          [
804	            "Protest",
805	            "Collider",
806	            "Qwen < Llama < DeepSeek",
807	            "Qwen < Llama < DeepSeek",
808	            "✓"
809	          ],
810	          [
811	            "Protest",
812	            "Instrument",
813	            "DeepSeek < Qwen < Llama",
814	            "Qwen < DeepSeek < Llama",
815	            "✗ (margin 0.02)"
816	          ],
817	          [
818	            "Stance",
819	            "Mediation",
820	            "Qwen < Llama < DeepSeek",
821	            "Qwen < Llama < DeepSeek",
822	            "✓"
823	          ],
824	          [
825	            "Stance",
826	            "Collider",
827	            "Llama < Qwen < DeepSeek",
828	            "Llama < Qwen < DeepSeek",
829	            "✓"
830	          ],
831	          [
832	            "Stance",
833	            "Confounding",
834	            "Llama < Qwen < DeepSeek",
835	            "Llama < Qwen < DeepSeek",
836	            "✓"
837	          ],
838	          [
839	            "Toxicity",
840	            "Mediation",
841	            "Qwen < Llama < DeepSeek",
842	            "Qwen < Llama < DeepSeek",
843	            "✓"
844	          ],
845	          [
846	            "Toxicity",
847	            "Collider",
848	            "Qwen < DeepSeek < Llama",
849	            "Qwen < DeepSeek < Llama",
850	            "✓"
851	          ],
852	          [
853	            "Toxicity",
854	            "Confounding",
855	            "Qwen < Llama < DeepSeek",
856	            "Qwen < Llama < DeepSeek",
857	            "✓"
858	          ]
859	        ]
860	      },
861	      {
862	        "name": "Table 12: ASV Robustness Classification",
863	        "columns": [
864	          "Task",
865	          "Context",
866	          "Best Model ASV",
867	          "Worst Model ASV",
868	          "Classification"
869	        ],
870	        "rows": [
871	          [
872	            "Protest",
873	            "Mediation",
874	            "2.1 (DeepSeek)",
875	            "0.9 (Qwen)",
876	            "FRAGILE — reversal risk"
877	          ],
878	          [
879	            "Protest",
880	            "Collider",
881	            "1.8 (DeepSeek)",
882	            "1.1 (Qwen)",
883	            "FRAGILE — reversal risk"
884	          ],
885	          [
886	            "Protest",
887	            "Instrument",
888	            "3.2 (Llama)",
889	            "2.4 (DeepSeek)",
890	            "Moderate"
891	          ],
892	          [
893	            "Stance",
894	            "Mediation",
895	            "4.1 (DeepSeek)",
896	            "2.8 (Qwen)",
897	            "Robust"
898	          ],
899	          [
900	            "Stance",
901	            "Collider",
902	            "3.8 (DeepSeek)",
903	            "2.5 (Llama)",
904	            "Moderate"
905	          ],
906	          [
907	            "Stance",
908	            "Confounding",
909	            "5.2 (DeepSeek)",
910	            "3.9 (Llama)",
911	            "Robust"
912	          ],
913	          [
914	            "Toxicity",
915	            "Mediation",
916	            "7.3 (Llama)",
917	            "5.1 (Qwen)",
918	            "Robust"
919	          ],
920	          [
921	            "Toxicity",
922	            "Collider",
923	            "6.8 (Llama)",
924	            "4.9 (Qwen)",
925	            "Robust"
926	          ],
927	          [
928	            "Toxicity",
929	            "Confounding",
930	            "8.1 (DeepSeek)",
931	            "6.2 (Qwen)",
932	            "Robust"
933	          ]
934	        ]
935	      }
936	    ],
937	    "figures": [],
938	    "analysis": "8/9 concordance 证明 ASV 在实践中是有效的偏倚严重度指标。唯一 discordance 出现在 noise margin 内，且在 instrument context（本身就是高方差估计）。关键实用发现： protest event coding 在 mediation/collider context 下使用 Qwen 3.5 Plus 时 ASV < 1.0—— 这意味着研究者如果用 Qwen 做 protest 分类并将其作为 mediator/collider，其下游因果结论 几乎肯定不可靠。这种 actionable alert 是单纯报告混淆矩阵无法提供的。\n\n\nConcordance 8/9：ASV 是基于 worst-case perturbation 的 bound，而非 point estimate。 在大多数场景中，worst-case 方向与实际偏倚方向一致，因此排序一致。 唯一 discordant case 出现在 instrument context，因为 Wald ratio 对 C 的微小差异 极其敏感（分母接近零时），导致 ASV 排序与实际偏倚排序在 noise margin 内翻转。 差异仅 0.02，在实际意义上可忽略。\n3/9 scenarios ASV < 1.5：这些对应 protest coding（K=5, 低对角优势 C）在  mediation 和 collider 拓扑下的应用。ASV < 1.5 意味着仅需 50% 的额外标注误差 即可推翻结论——这是一个强警告信号。6/9 ASV > 3.0 对应较简单的 toxicity 任务 和 confounding 拓扑，结论稳健。\nASV 正确标记了 2 个落入反转区域的实证 C：这是 ASV 框架实用价值的最直接证据。 研究者报告原始 C 矩阵时无法判断\"这个 C 有多危险\"——ASV 提供了这个判断。\nHeld-out coverage 0.94（vs 理论 0.95）：轻微欠覆盖因为实证 C 的估计本身有 sampling variance（~30K annotations），引入了理论分析未考虑的噪声。 但 0.94 在可接受范围内。\n"
939	  },
940	  {
941	    "name": "Correction guidance framework validation",
942	    "description": "构建决策框架：{topology × error structure × ASV} → correction method（DSL / PPI / MLA / naive plug-in / \"无现有方法适用\"）。 MC 验证推荐方法在各场景中是否产生最小偏倚。在 plan_003 数据上经验验证。\n",
943	    "results": {
944	      "correction_framework_accuracy": 0.95,
945	      "correction_framework_accuracy_detail": "432 个 MC scenario 中 411 个推荐方法产生最小 bias",
946	      "scenarios_tested": 432,
947	      "scenario_breakdown": "6 topologies × 6 C structures × 3 K values × 4 effect sizes = 432",
948	      "method_recommendation_distribution": {
949	        "DSL": "18% of scenarios",
950	        "PPI": "24% of scenarios",
951	        "MLA": "31% of scenarios",
952	        "naive_plugin": "12% of scenarios",
953	        "no_adequate_method": "15% of scenarios"
954	      },
955	      "no_adequate_method_conditions": "primarily: correlated multi-LLM errors + differential K≥5 + collider/front-door topology",
956	      "failure_cases": "21/432 — 14 cases where MLA and PPI are within 0.005 of each other (recommendation arbitrary), 7 cases where extreme C + small N makes all methods unstable",
957	      "empirical_validation_plan003": "8/9 empirical scenarios — recommended method produces bias reduction ≥40% vs uncorrected",
958	      "empirical_failure": "1/9 — protest × collider × Qwen: no method adequate (flagged correctly as 'no adequate method')"
959	    },
960	    "tables": [
961	      {
962	        "name": "Table 13: Correction Method Recommendation Distribution",
963	        "columns": [
964	          "Method",
965	          "% Scenarios",
966	          "Typical Condition",
967	          "Avg Bias Reduction"
968	        ],
969	        "rows": [
970	          [
971	            "MLA",
972	            "31%",
973	            "C known, K≤5, non-differential",
974	            "72%"
975	          ],
976	          [
977	            "PPI",
978	            "24%",
979	            "C uncertain, gold-standard available",
980	            "65%"
981	          ],
982	          [
983	            "DSL",
984	            "18%",
985	            "Confounding topology, high diag. dominance",
986	            "58%"
987	          ],
988	          [
989	            "Naive plug-in",
990	            "12%",
991	            "ASV > 5.0 (robust conclusions)",
992	            "N/A (unnecessary)"
993	          ],
994	          [
995	            "No adequate method",
996	            "15%",
997	            "Correlated errors + differential + collider/front-door",
998	            "N/A"
999	          ]
1000	        ]
1001	      },
1002	      {
1003	        "name": "Table 14: Framework Accuracy by Topology",
1004	        "columns": [
1005	          "Topology",
1006	          "Scenarios",
1007	          "Correct",
1008	          "Accuracy",
1009	          "Most Common Failure Mode"
1010	        ],
1011	        "rows": [
1012	          [
1013	            "Confounding",
1014	            "72",
1015	            "71",
1016	            "98.6%",
1017	            "MLA ≈ PPI (indistinguishable)"
1018	          ],
1019	          [
1020	            "Mediation",
1021	            "72",
1022	            "69",
1023	            "95.8%",
1024	            "Extreme C + small N"
1025	          ],
1026	          [
1027	            "Collider",
1028	            "72",
1029	            "67",
1030	            "93.1%",
1031	            "MLA ≈ PPI + extreme C"
1032	          ],
1033	          [
1034	            "M-bias",
1035	            "72",
1036	            "70",
1037	            "97.2%",
1038	            "Rare edge case"
1039	          ],
1040	          [
1041	            "Instrument",
1042	            "72",
1043	            "69",
1044	            "95.8%",
1045	            "Wald ratio instability"
1046	          ],
1047	          [
1048	            "Front-door",
1049	            "72",
1050	            "65",
1051	            "90.3%",
1052	            "Two-stage estimation complexity"
1053	          ]
1054	        ]
1055	      }
1056	    ],
1057	    "figures": [],
1058	    "analysis": "95% 准确率表明基于理论的决策框架在实践中可靠。最重要的发现不是哪个方法最好， 而是 \"方法选择是拓扑依赖的\"——在 confounding DAG 中最优的方法在 collider DAG 中 可能增加偏倚。这直接回应了 Jerzak et al. (EMNLP 2025) 的 unconditional benchmarking  方法论：如果不考虑拓扑，benchmarking 本身就是误导性的。 15% \"no adequate method\" 区域是诚实的 open problem identification， 为后续方法论研究提供了明确方向。\n\n\n95% accuracy（411/432）：决策框架基于理论偏倚表达式的 closed-form 分析， 在每个 {topology × C structure} cell 中选择使残差偏倚最小化的方法。 14 个\"失败\"case 实际上是 MLA 和 PPI 表现几乎相同（差异 < 0.005）的场景—— 框架推荐了其中一个，但另一个同样好。这不是真正的失败，只是不确定性。 7 个真正失败的 case 出现在极端 C（near-permutation）+ 小样本（N=1000）下， 所有方法都不稳定——这种场景下正确答案可能是\"收集更多数据\"而非选择方法。\nMethod distribution：MLA（31%）最常被推荐因为它直接利用 C 矩阵做 deconvolution， 在 C 已知时通常最优。PPI（24%）在 C 有不确定性时被推荐（利用少量 gold-standard 数据 做 prediction-powered inference）。DSL（18%）在 confounding topology +  high diagonal dominance C 下被推荐（double sampling + likelihood correction）。 Naive plug-in（12%）仅在 ASV > 5.0（结论非常稳健）时被推荐——此时 correction  的 variance cost 大于 bias reduction benefit。\n15% \"no adequate method\"：这些场景主要涉及 correlated multi-LLM errors +  differential K≥5 + collider/front-door topology。这是论文 Claim 3 的一部分—— 识别现有方法不足的区域并标记为 open problems。其中 dependence-aware multi-LLM  correction 是最重要的 open problem（回应 Kim et al. ICML 2025）。\nEmpirical 8/9：1 个\"failure\"实际上是框架正确标记为\"no adequate method\" （protest × collider × Qwen，C 接近 near-permutation + 模型间误差高度相关）。 这是一个 success case of honest scoping，而非真正失败。\n"
1059	  },
1060	  {
1061	    "name": "Pathological confusion matrix analysis",
1062	    "description": "分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在所有拓扑中的 偏倚行为。识别预测偏倚严重度的结构性指标（spectral gap, diagonal dominance ratio）。\n",
1063	    "results": {
1064	      "spectral_gap_bias_correlation": 0.91,
1065	      "diagonal_dominance_bias_correlation": 0.87,
1066	      "best_predictor": "spectral gap (1 - λ₂/λ₁) explains 83% of bias magnitude variance",
1067	      "catastrophic_bias_threshold": "spectral gap < 0.15 → bias > 2x effect size in ≥80% of reversal-prone topologies",
1068	      "near_permutation_analysis": "all near-permutation C (spectral gap < 0.05) produce reversal in mediation/collider/front-door; severity 1.5-3x",
1069	      "rank_deficient_analysis": "rank-deficient C always produce catastrophic bias regardless of topology — information loss is complete for collapsed dimensions",
1070	      "block_diagonal_analysis": "bias depends on which classes are in same block — if classes with opposite effects are merged, reversal guaranteed",
1071	      "practitioner_diagnostic": "two-number summary: (spectral gap, diagonal dominance ratio) → risk category (low/medium/high/catastrophic)"
1072	    },
1073	    "tables": [
1074	      {
1075	        "name": "Table 15: Structural Predictors of Bias Severity",
1076	        "columns": [
1077	          "Predictor",
1078	          "Correlation with |Bias|",
1079	          "R² (univariate)",
1080	          "Threshold for Catastrophic Bias"
1081	        ],
1082	        "rows": [
1083	          [
1084	            "Spectral gap (1-λ₂/λ₁)",
1085	            "-0.91",
1086	            "0.83",
1087	            "< 0.15"
1088	          ],
1089	          [
1090	            "Diagonal dominance ratio",
1091	            "-0.87",
1092	            "0.76",
1093	            "< 0.55"
1094	          ],
1095	          [
1096	            "Condition number of C",
1097	            "0.89",
1098	            "0.79",
1099	            "> 12"
1100	          ],
1101	          [
1102	            "Min diagonal element",
1103	            "-0.84",
1104	            "0.71",
1105	            "< 0.3"
1106	          ],
1107	          [
1108	            "Spectral gap + diag. dom. (joint)",
1109	            "—",
1110	            "0.89",
1111	            "Combined threshold"
1112	          ]
1113	        ]
1114	      }
1115	    ],
1116	    "figures": [],
1117	    "analysis": "为实践者提供了两个可操作的诊断数字：spectral gap 和 diagonal dominance ratio。 研究者无需理解完整的偏倚理论，只需计算其实证 C 矩阵的这两个指标， 即可判断偏倚风险等级。这补充了 ASV 框架——ASV 告诉你\"结论多稳健\"， 而 spectral diagnostics 告诉你\"为什么不稳健\"和\"C 的哪个方面最危险\"。 Catastrophic threshold（spectral gap < 0.15）在 plan_003 的实证数据中 对应 Qwen 在 protest coding 某些 prompt 变体下的 C 矩阵——与 ASV < 1.0  的 fragile classification 完全一致。\n\n\nSpectral gap 与偏倚强相关（r=0.91）：混淆矩阵 C 的第二大特征值 λ₂ 控制了 \"主误分类模式\"的强度。当 spectral gap = 1-λ₂/λ₁ 接近 0 时，C 接近非满秩， 信息丢失严重，偏倚灾难性。这不是偶然——偏倚表达式中 C 的逆（或伪逆）出现在 correction 中，spectral gap 控制了逆的条件数。\nDiagonal dominance 相关性略低（0.87 vs 0.91）因为 diagonal dominance  是一个粗糙的指标——它只看对角元素与行和的比值，不捕获 off-diagonal 的结构 （如 block-diagonal 的特殊性）。Spectral gap 通过特征分解捕获了完整的  off-diagonal 结构信息。\nNear-permutation 全部产生反转（在反转敏感拓扑中）：near-permutation C  等价于类别标签几乎完全互换，这在 K≥3 时结构性地翻转效应方向（而 K=2 时 近置换 = 高误分类率，仍然只 attenuate toward null）。\nBlock-diagonal 的方向依赖于块结构：如果具有相反效应的类别被合并在同一块中， 块内平均化可以翻转块的净效应方向。这与 binarization collapse 的机制相同， 但发生在 C 矩阵内部而非研究者的显式折叠中。\n"
1118	  },
1119	  {
1120	    "name": "annot-sensitivity Python toolkit",
1121	    "description": "开源 Python 包：用户输入 DAG + confusion matrix + downstream estimate → 输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation + diagnostic plots。 pip-installable，含每个拓扑的 worked examples。\n",
1122	    "results": {
1123	      "package_name": "annot-sensitivity",
1124	      "pip_installable": true,
1125	      "supported_topologies": 6,
1126	      "supported_K_range": "2-20",
1127	      "api_surface": "3 main functions: bias_expression(), asv_bound(), recommend_correction()",
1128	      "documentation": "6 topology-specific tutorials (Jupyter notebooks), API reference, quickstart guide",
1129	      "test_coverage": ">90%",
1130	      "benchmark": "bias_expression() < 0.1s for K≤7; asv_bound() < 1s for K≤7; recommend_correction() < 0.5s",
1131	      "dependencies": "numpy, scipy, matplotlib (minimal)",
1132	      "worked_examples": 6
1133	    },
1134	    "tables": [],
1135	    "figures": [],
1136	    "analysis": "Toolkit 的设计哲学是\"一个函数回答一个问题\"。研究者的典型 workflow： (1) 收集 gold-standard 子集 → 估计 C；(2) 调用 bias_expression(dag, C, K) →  了解偏倚结构；(3) 调用 asv_bound(dag, C, estimate, threshold) → 了解结论稳健性； (4) 调用 recommend_correction(dag, C, asv, n_gold) → 选择校正方法。 开源发布对 AAAI/ARR 审稿均加分——artifact evaluation 是近年趋势。\n\nToolkit 是论文影响力的关键放大器。学术论文的理论贡献如果没有可用工具， 很难被实践者采纳。三个主函数对应论文三个 claims：bias_expression() → Claim 1（taxonomy）， asv_bound() → Claim 2（ASV），recommend_correction() → Claim 3（correction guidance）。\nK 支持范围 2-20：K=2 作为 consistency check（应恢复经典二分类结果）， K>7 用矩阵表达式 + 特征分解可解释性工具。K>20 实际中极罕见且计算成本高 （C 矩阵有 K(K-1) 自由参数），故限定上界。\n性能目标（< 1s for K≤7）：bias_expression 和 recommend_correction 是闭式计算， 主要耗时在矩阵运算。asv_bound 涉及优化问题（构造性紧性需要求解约束优化）， K≤7 时维度足够低，SQP 在 1s 内收敛。\n最小依赖（numpy, scipy, matplotlib）：降低安装门槛，compatible with  任何 Python 科学计算环境。不依赖 PyTorch/TensorFlow 因为所有计算是 解析数学而非机器学习。\n"
1137	  }
1138	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c67425a-926e-4f8f-865d-78a00c3e9b9e",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "46e4c38b-0899-4f45-b200-cfd8911c11b3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Multi-topology bias derivation and MC validation (K=3)\",\n    \"description\": \"对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 闭式偏倚表达式， 每个拓扑用 6 种混淆矩阵结构 × 1000 MC reps × N=10000 验证。另对 mediation/collider/front-door/M-bias/instrument 执行 100k random C 搜索，检测方向反转违背率。\\n\",\n    \"results\": {\n      \"theory_mc_match_rate\": 0.972,\n      \"theory_mc_match_detail\": \"35/36 structure×topology 组合落入 95% MC CI；1 个边界 case（front-door + rank-deficient C）偏差 0.003 超 CI 上界，增加到 N=50000 后收敛\",\n      \"reversal_topologies_count\": 4,\n      \"reversal_topologies\": [\n        \"exposure (MVP)\",\n        \"mediation\",\n        \"collider\",\n        \"front-door\"\n      ],\n      \"non_reversal_topologies\": [\n        \"confounding\",\n        \"instrument\"\n      ],\n      \"mediation_violation_rate\": 0.52,\n      \"mediation_sign_reversal_rate\": 0.47,\n      \"mediation_amplification_rate\": 0.11,\n      \"collider_violation_rate\": 0.41,\n      \"collider_sign_reversal_rate\": 0.36,\n      \"collider_amplification_rate\": 0.09,\n      \"frontdoor_violation_rate\": 0.34,\n      \"frontdoor_sign_reversal_rate\": 0.28,\n      \"frontdoor_amplification_rate\": 0.12,\n      \"mbias_violation_rate\": 0.0,\n      \"mbias_bias_range\": [\n        0.04,\n        0.18\n      ],\n      \"instrument_violation_rate\": 0.0,\n      \"instrument_bias_range\": [\n        0.02,\n        0.14\n      ],\n      \"confounding_violation_rate\": 0.0,\n      \"confounding_bias_range\": [\n        0.063,\n        0.298\n      ],\n      \"mediation_worst_case\": \"β_indirect=0.5 → estimate=-0.31 (sign reversal, 1.62x amplification)\",\n      \"collider_worst_case\": \"β_XY=0.0 (null) → estimate=0.44 (spurious effect creation + direction assignment)\",\n      \"frontdoor_worst_case\": \"β_total=0.8 → estimate=-0.22 (sign reversal via second-stage distortion)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Topology × Reversal Summary\",\n        \"columns\": [\n          \"Topology\",\n          \"Role of Annotated Variable\",\n          \"Violation Rate (100k)\",\n          \"Sign Reversal Rate\",\n          \"Amplification Rate\",\n          \"Worst-Case Severity\",\n          \"K=2 Control\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"Confounder\",\n            \"0.000\",\n            \"0.000\",\n            \"0.000\",\n            \"0.298 (toward OVB)\",\n            \"toward OVB ✓\"\n          ],\n          [\n            \"Exposure (MVP)\",\n            \"Treatment\",\n            \"0.850\",\n            \"0.834\",\n            \"0.141\",\n            \"2.83x amplification\",\n            \"toward null ✓\"\n          ],\n          [\n            \"Mediation\",\n            \"Mediator\",\n            \"0.520\",\n            \"0.470\",\n            \"0.110\",\n            \"1.62x + sign reversal\",\n            \"toward null ✓\"\n          ],\n          [\n            \"Collider\",\n            \"Collider\",\n            \"0.410\",\n            \"0.360\",\n            \"0.090\",\n            \"spurious 0.44 from null\",\n            \"attenuated ✓\"\n          ],\n          [\n            \"M-bias\",\n            \"M-bias variable\",\n            \"0.000\",\n            \"0.000\",\n            \"0.000\",\n            \"0.18 (attenuated)\",\n            \"attenuated ✓\"\n          ],\n          [\n            \"Instrument\",\n            \"Instrument\",\n            \"0.000\",\n            \"0.000\",\n            \"0.000\",\n            \"ratio distortion 0.14\",\n            \"attenuated ✓\"\n          ],\n          [\n            \"Front-door\",\n            \"Front-door variable\",\n            \"0.340\",\n            \"0.280\",\n            \"0.120\",\n            \"sign reversal\",\n            \"toward null ✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Theory-MC Match per Topology × C Structure\",\n        \"columns\": [\n          \"Topology\",\n          \"Diagonal-dominant\",\n          \"Moderate off-diag\",\n          \"Uniform off-diag\",\n          \"Block-diagonal\",\n          \"Near-permutation\",\n          \"Rank-deficient\",\n          \"Match Rate\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"6/6\"\n          ],\n          [\n            \"Mediation\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"6/6\"\n          ],\n          [\n            \"Collider\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"6/6\"\n          ],\n          [\n            \"M-bias\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"6/6\"\n          ],\n          [\n            \"Instrument\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"6/6\"\n          ],\n          [\n            \"Front-door\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"✓\",\n            \"△*\",\n            \"5/6\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：非差异 K≥3 误分类的方向反转是拓扑依赖的。6 个拓扑分为两类：(1) 信息丢失型（confounding, instrument, M-bias）—— 误分类只能减少变量的信息量，偏倚方向可预测；(2) 结构扭曲型（exposure, mediation, collider, front-door）—— 误分类改变变量在 DAG 中的功能角色（如 mediator 的类别标签互换等价于改变 M→Y 的函数形式）， 导致不可预测的方向反转。这一二分法是论文的核心理论贡献。Confounding DAG 的\\\"良性\\\"行为不可推广到其他拓扑， 这直接挑战了实践者\\\"non-differential error is conservative\\\"的默认假设。\\n\\n\\nMediation (violation rate 0.52): 间接效应 = β_XM × β_MY|X。K≥3 非差异误分类扭曲 M→Y|X 回归系数—— 近置换矩阵 C 使相邻类别标签互换，导致 β_MY|X 符号翻转，从而间接效应反转。K=2 下非差异误分类只能将 β_MY|X  向零压缩（attenuation），结构上不可能越过零点。violation rate 0.52 而非更高（对比 exposure 的 0.85）， 因为间接效应经过两步回归（X→M 和 M→Y|X），仅当 C 同时严重扰动 M 的条件分布时才出现反转， 而 exposure 误分类直接作用于处理变量，单步即可反转。\\nCollider (violation rate 0.41): 对 collider C̃ 条件化打开伪路径 X←U→C←V→Y。K≥3 误分类改变条件化的 有效权重——不同类别的合并创造不同的伪关联模式。violation rate 低于 mediation 因为反转需要 C 矩阵 使 X-path 和 Y-path 的贡献权重同时满足特定比例条件，约束更强。\\nFront-door (violation rate 0.34): 前门调整涉及两阶段估计（X→M 和 M→Y|do(X)）。K≥3 误分类不对称地 扭曲两个阶段——第一阶段 attenuation 与第二阶段 distortion 的交互可使整体估计翻转。violation rate  最低因为反转需要两阶段同时被 C 严重扰动且扰动方向\\\"配合\\\"，是三个反转拓扑中约束最强的。\\nConfounding (violation rate 0.0): 已由 MVP 确认。残差混淆始终朝向 OVB 方向，因为误分类只能减少 confounder 的解释力（信息丢失），不能创造新的混淆结构。K≥3 增加了更多丢失信息的方式但不改变方向性。\\nInstrument (violation rate 0.0): Wald estimator = Cov(Y,Z̃)/Cov(X,Z̃)。非差异误分类对 Z 的两个 协方差施加相同方向的 attenuation（均乘以 C 的特征值相关因子），比值的符号不变。 K≥3 下分子分母的 attenuation 系数不再相同（不同特征值），导致幅度偏倚但符号保持。\\nM-bias (violation rate 0.0): M-bias（蝴蝶 DAG）中被误分类的变量本不应被条件化。 误分类使条件化效应减弱（信息丢失方向），偏倚幅度变化但不反转。\\n\"\n  },\n  {\n    \"name\": \"General K bias expressions with interpretability tools (K=5,7)\",\n    \"description\": \"将偏倚表达式推广到矩阵形式（一般 K）。开发三种可解释性工具：(a) 特征分解摘要，(b) 最坏情况标量界， (c) 诊断可视化。在 confounding + mediation + collider DAG 上用 K=5,7 验证。\\n\",\n    \"results\": {\n      \"eigendecomposition_variance_captured_top2\": 0.87,\n      \"eigendecomposition_variance_captured_top3\": 0.96,\n      \"worstcase_bound_tightness\": 0.88,\n      \"worstcase_bound_tightness_detail\": \"最坏情况标量界在 88% 的场景中与真实最坏情况偏差 <15%\",\n      \"K5_mediation_violation_rate\": 0.61,\n      \"K5_collider_violation_rate\": 0.49,\n      \"K7_mediation_violation_rate\": 0.68,\n      \"K7_collider_violation_rate\": 0.55,\n      \"K5_confounding_reversal\": false,\n      \"K7_confounding_reversal\": false,\n      \"theory_mc_match_K5\": \"17/18 within 95% CI\",\n      \"theory_mc_match_K7\": \"16/18 within 95% CI\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Violation Rate Scaling with K\",\n        \"columns\": [\n          \"Topology\",\n          \"K=3\",\n          \"K=5\",\n          \"K=7\",\n          \"Trend\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"0.000\",\n            \"0.000\",\n            \"0.000\",\n            \"Stable at 0 (monotonic toward OVB)\"\n          ],\n          [\n            \"Mediation\",\n            \"0.520\",\n            \"0.610\",\n            \"0.680\",\n            \"Monotonically increasing\"\n          ],\n          [\n            \"Collider\",\n            \"0.410\",\n            \"0.490\",\n            \"0.550\",\n            \"Monotonically increasing\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Eigendecomposition Variance Explained\",\n        \"columns\": [\n          \"Topology\",\n          \"K\",\n          \"Top-1 EV%\",\n          \"Top-2 EV%\",\n          \"Top-3 EV%\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"5\",\n            \"72%\",\n            \"89%\",\n            \"97%\"\n          ],\n          [\n            \"Confounding\",\n            \"7\",\n            \"68%\",\n            \"85%\",\n            \"95%\"\n          ],\n          [\n            \"Mediation\",\n            \"5\",\n            \"70%\",\n            \"87%\",\n            \"96%\"\n          ],\n          [\n            \"Mediation\",\n            \"7\",\n            \"65%\",\n            \"84%\",\n            \"94%\"\n          ],\n          [\n            \"Collider\",\n            \"5\",\n            \"71%\",\n            \"88%\",\n            \"96%\"\n          ],\n          [\n            \"Collider\",\n            \"7\",\n            \"66%\",\n            \"85%\",\n            \"95%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"K 增大强化了核心论点：随着分类粒度增加，binary 近似的失效更严重，方向反转概率上升。 可解释性工具使 K≥5 的矩阵偏倚表达式在实践中可用：研究者无需理解完整 K×K 偏倚矩阵， 只需检查 top-2 特征模式即可判断偏倚的方向和严重程度。最坏情况标量界为风险厌恶型研究者 提供保守但可操作的单一数字。\\n\\n\\nK 增大时 violation rate 单调上升（mediation: 0.52→0.61→0.68；collider: 0.41→0.49→0.55）， 因为混淆矩阵的自由参数从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。 更高维度的 C 矩阵有更多\\\"方向\\\"可以扭曲类别映射，使得 random search 中遇到反转配置的概率增加。\\n特征分解 top-2 捕获 87% 方差：偏倚矩阵 B = f(C) 的谱结构由 C 的谱结构决定。 C 通常是行随机矩阵（行和为 1），其最大特征值为 1（对应\\\"保真\\\"模式），第二大特征值 对应主要误分类模式。因此 B 的前 2 个特征值对应\\\"无偏\\\"基线和\\\"主误分类方向\\\"， 合计解释大部分方差。top-3 达 96% 因为第三个模式捕获了次要误分类模式。\\n最坏情况标量界紧度 88%：该界通过对 B 的谱范数取上界得到，对于高对角优势 C  这个界很紧（谱范数 ≈ 最大特征值），但对于结构化偏差（如 block-diagonal C） 谱范数高估约 25-30%，拉低了整体紧度。\\nTheory-MC match 在 K=7 时略降（16/18 vs K=3 的 35/36）：高维 MC 模拟的方差增大， 需要更大 N 才能达到同样精度。2 个未匹配 case 均为 near-permutation extreme， 增加到 N=50000 后收敛。\\n\"\n  },\n  {\n    \"name\": \"Empirical confusion matrices: 3 LLMs × 3 CSS tasks\",\n    \"description\": \"收集 3 个 LLM（Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4）在 3 个 CSS 任务 （protest event coding K=5, stance detection K=3, toxicity K=2）上的实证混淆矩阵。 ~30K annotations per model × 3 datasets × 3 prompt variants。\\n\",\n    \"results\": {\n      \"total_annotations\": \"~270K (3 models × 3 tasks × ~30K)\",\n      \"protest_K5_avg_diagonal_dominance\": 0.62,\n      \"protest_K5_inter_model_kappa\": 0.71,\n      \"stance_K3_avg_diagonal_dominance\": 0.74,\n      \"stance_K3_inter_model_kappa\": 0.68,\n      \"toxicity_K2_avg_accuracy\": 0.89,\n      \"toxicity_K2_inter_model_kappa\": 0.76,\n      \"cross_model_error_correlation\": 0.58,\n      \"cross_model_error_correlation_detail\": \"当两个模型均出错时，58% 的 case 错向同一类别（与 Kim et al. 的 60% 一致）\",\n      \"distinct_C_structures_observed\": 9,\n      \"near_permutation_cases\": 2,\n      \"block_diagonal_cases\": 3,\n      \"prompt_variant_C_shift\": \"prompt 变体导致 C 结构在 Frobenius 距离上变化 0.04-0.12\",\n      \"downstream_bias_vs_gold_protest\": [\n        -0.08,\n        0.15\n      ],\n      \"downstream_bias_vs_gold_stance\": [\n        -0.05,\n        0.09\n      ],\n      \"downstream_bias_vs_gold_toxicity\": [\n        -0.02,\n        0.03\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Empirical Confusion Matrix Summary\",\n        \"columns\": [\n          \"Task\",\n          \"K\",\n          \"Model\",\n          \"Accuracy\",\n          \"Diagonal Dominance\",\n          \"Largest Off-Diag\",\n          \"C Structure Type\"\n        ],\n        \"rows\": [\n          [\n            \"Protest\",\n            \"5\",\n            \"Llama 4 Maverick\",\n            \"0.64\",\n            \"0.60\",\n            \"0.18 (strat_dev→peaceful)\",\n            \"Moderate off-diag\"\n          ],\n          [\n            \"Protest\",\n            \"5\",\n            \"Qwen 3.5 Plus\",\n            \"0.60\",\n            \"0.57\",\n            \"0.21 (strat_dev→peaceful)\",\n            \"Near-permutation\"\n          ],\n          [\n            \"Protest\",\n            \"5\",\n            \"DeepSeek V4\",\n            \"0.67\",\n            \"0.63\",\n            \"0.15 (other→gov_resp)\",\n            \"Block-diagonal\"\n          ],\n          [\n            \"Stance\",\n            \"3\",\n            \"Llama 4 Maverick\",\n            \"0.77\",\n            \"0.76\",\n            \"0.14 (neutral→against)\",\n            \"Block-diagonal\"\n          ],\n          [\n            \"Stance\",\n            \"3\",\n            \"Qwen 3.5 Plus\",\n            \"0.73\",\n            \"0.72\",\n            \"0.16 (against→neutral)\",\n            \"Block-diagonal\"\n          ],\n          [\n            \"Stance\",\n            \"3\",\n            \"DeepSeek V4\",\n            \"0.76\",\n            \"0.75\",\n            \"0.13 (neutral→against)\",\n            \"Block-diagonal\"\n          ],\n          [\n            \"Toxicity\",\n            \"2\",\n            \"Llama 4 Maverick\",\n            \"0.91\",\n            \"0.91\",\n            \"0.09 (toxic→non-toxic)\",\n            \"Diagonal-dominant\"\n          ],\n          [\n            \"Toxicity\",\n            \"2\",\n            \"Qwen 3.5 Plus\",\n            \"0.87\",\n            \"0.87\",\n            \"0.13 (non-toxic→toxic)\",\n            \"Diagonal-dominant\"\n          ],\n          [\n            \"Toxicity\",\n            \"2\",\n            \"DeepSeek V4\",\n            \"0.90\",\n            \"0.90\",\n            \"0.10 (toxic→non-toxic)\",\n            \"Diagonal-dominant\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Inter-Model Error Agreement\",\n        \"columns\": [\n          \"Task\",\n          \"Model Pair\",\n          \"Cohen's κ\",\n          \"Error Agreement Rate\",\n          \"Same-Direction Error %\"\n        ],\n        \"rows\": [\n          [\n            \"Protest\",\n            \"Llama-Qwen\",\n            \"0.69\",\n            \"0.24\",\n            \"0.61\"\n          ],\n          [\n            \"Protest\",\n            \"Llama-DeepSeek\",\n            \"0.72\",\n            \"0.21\",\n            \"0.57\"\n          ],\n          [\n            \"Protest\",\n            \"Qwen-DeepSeek\",\n            \"0.68\",\n            \"0.25\",\n            \"0.56\"\n          ],\n          [\n            \"Stance\",\n            \"Llama-Qwen\",\n            \"0.67\",\n            \"0.18\",\n            \"0.59\"\n          ],\n          [\n            \"Stance\",\n            \"Llama-DeepSeek\",\n            \"0.70\",\n            \"0.16\",\n            \"0.58\"\n          ],\n          [\n            \"Stance\",\n            \"Qwen-DeepSeek\",\n            \"0.66\",\n            \"0.19\",\n            \"0.57\"\n          ],\n          [\n            \"Toxicity\",\n            \"All pairs avg\",\n            \"0.76\",\n            \"0.09\",\n            \"0.62\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"实证 C 矩阵覆盖了理论分析中的多种结构类型（diagonal-dominant, block-diagonal, near-permutation）， 为后续 ASV 校准和 correction framework 验证提供了现实基础。关键观察： (1) Protest coding 的 C 矩阵接近 plan_001 中产生反转的区域，预示该任务在 mediation/collider  拓扑下风险最高；(2) 跨模型错误高度相关，确认多 LLM 集成不是解决方案； (3) Prompt 变体可显著移动 C 结构（Frobenius Δ 达 0.12），暗示 prompt engineering  本身是一种（未被充分认识的）bias intervention。\\n\\n\\nProtest event coding (K=5) 对角优势最低（0.62）：5 类任务（peaceful protest, violent protest,  strategic development, government response, other）存在固有歧义——\\\"strategic development\\\"与  \\\"peaceful protest\\\"常被混淆，LLM 倾向于对 borderline case 系统性偏向高频类别。 低对角优势意味着 C 矩阵偏离对角，更接近 random search 中产生反转的区域。\\nStance detection (K=3) 对角优势较高（0.74）：3 类（favor, against, neutral）语义距离较大， 但 neutral 与 against 的边界模糊导致特定 off-diagonal 元素偏高，形成 block-diagonal 结构 （favor 与 against/neutral 分离，但 against-neutral 互相混淆）。\\nToxicity (K=2) 准确率最高（0.89）：二分类任务较简单，且 toxicity 有较清晰的语言标记。 作为 binary special case / consistency check——K=2 下所有模型的偏倚均 toward null， 与理论预测一致。\\n跨模型错误相关 0.58：Kim et al. (ICML 2025) 报告 60%，我们的 0.58 高度一致。 这不是巧合——LLM 共享类似的预训练数据和推理模式，对同类歧义样本倾向于犯同类错误。 这个发现强化了我们的论点：多模型集成无法消除系统性偏倚，必须分析 C 结构。\\n9 种不同 C 结构（3 models × 3 tasks）为后续 ASV 校准提供了充分多样性。 2 个 near-permutation cases 出现在 protest coding 的特定 prompt 变体下（过度指令化导致 类别定义混乱），3 个 block-diagonal cases 出现在 stance detection 中（favor 孤立）。\\n\"\n  },\n  {\n    \"name\": \"Binarization collapse analysis across all topologies\",\n    \"description\": \"对 6 个拓扑 + exposure（共 7 个拓扑），K=3,5,7 条件下，将 K 类变量折叠为二分类， 比较完整多类偏倚表达式 vs 二值化后偏倚表达式的差异 Δ。\\n\",\n    \"results\": {\n      \"binarization_max_delta\": 0.19,\n      \"binarization_max_delta_topology\": \"mediation\",\n      \"binarization_max_delta_K\": 7,\n      \"binarization_avg_delta_K3\": 0.08,\n      \"binarization_avg_delta_K5\": 0.13,\n      \"binarization_avg_delta_K7\": 0.16,\n      \"binarization_direction_reversal_cases\": \"12% of K=5,7 scenarios show Δ that flips bias direction\",\n      \"binarization_delta_by_topology\": {\n        \"confounding_K3\": 0.06,\n        \"confounding_K5\": 0.09,\n        \"confounding_K7\": 0.11,\n        \"mediation_K3\": 0.1,\n        \"mediation_K5\": 0.15,\n        \"mediation_K7\": 0.19,\n        \"collider_K3\": 0.09,\n        \"collider_K5\": 0.14,\n        \"collider_K7\": 0.17,\n        \"exposure_K3\": 0.08,\n        \"exposure_K5\": 0.12,\n        \"exposure_K7\": 0.15,\n        \"mbias_K3\": 0.05,\n        \"mbias_K5\": 0.08,\n        \"mbias_K7\": 0.1,\n        \"instrument_K3\": 0.04,\n        \"instrument_K5\": 0.07,\n        \"instrument_K7\": 0.09,\n        \"frontdoor_K3\": 0.09,\n        \"frontdoor_K5\": 0.13,\n        \"frontdoor_K7\": 0.16\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Binarization Collapse Δ by Topology × K\",\n        \"columns\": [\n          \"Topology\",\n          \"K=3 Δ\",\n          \"K=5 Δ\",\n          \"K=7 Δ\",\n          \"Max Δ\",\n          \"Direction Reversal by Δ?\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"0.06\",\n            \"0.09\",\n            \"0.11\",\n            \"0.11\",\n            \"No\"\n          ],\n          [\n            \"Exposure\",\n            \"0.08\",\n            \"0.12\",\n            \"0.15\",\n            \"0.15\",\n            \"Yes (3% of K=7)\"\n          ],\n          [\n            \"Mediation\",\n            \"0.10\",\n            \"0.15\",\n            \"0.19\",\n            \"0.19\",\n            \"Yes (18% of K=7)\"\n          ],\n          [\n            \"Collider\",\n            \"0.09\",\n            \"0.14\",\n            \"0.17\",\n            \"0.17\",\n            \"Yes (14% of K=7)\"\n          ],\n          [\n            \"M-bias\",\n            \"0.05\",\n            \"0.08\",\n            \"0.10\",\n            \"0.10\",\n            \"No\"\n          ],\n          [\n            \"Instrument\",\n            \"0.04\",\n            \"0.07\",\n            \"0.09\",\n            \"0.09\",\n            \"No\"\n          ],\n          [\n            \"Front-door\",\n            \"0.09\",\n            \"0.13\",\n            \"0.16\",\n            \"0.16\",\n            \"Yes (11% of K=7)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binarization 不是安全退路。Max Δ = 0.19 在实际社会科学研究中足以改变实质性结论 （典型效应量 0.1-0.3）。这一结果与 MVP 中 confounding DAG 的 Δ=0.103 一致且推广： 更多拓扑、更高 K 值下 Δ 更大。结合 plan_001 的方向反转结果，完整论点是： (1) 保留多类可能导致方向反转，(2) 折叠为二类也不安全——研究者无处可逃，必须使用 ASV 框架 诊断其具体 {C × topology} 组合的偏倚性质。\\n\\n\\nBinarization max Δ = 0.19（mediation, K=7）：折叠 7 类 mediator 为二分类丢弃了类别间的 细粒度偏倚结构。Mediation DAG 中间接效应依赖 M 的分布形状——当 7 个类别被折叠为 2 个时， 被合并的类别可能具有相反方向的 M→Y 效应，导致折叠后的间接效应与原始间接效应方向相反。 K=7 比 K=3 更严重因为折叠时信息丢失更多（5 个类别被合并 vs 1 个类别被合并）。\\nΔ 随 K 单调增大（avg: 0.08→0.13→0.16）：这是信息论上的必然——K→2 折叠的信息丢失 量为 log(K)-log(2)，K 越大丢失越多。\\n12% 的 K=5,7 场景中 Δ 本身导致方向翻转：这意味着研究者试图通过 binarization  \\\"逃入\\\"二分类安全区域的策略不仅无效（因为折叠引入新偏倚），而且在 12% 的场景中 反而比保留多类更危险。这个发现直接回应了一个预期的 reviewer concern： \\\"既然 binary case 有保证，为什么不直接 binarize？\\\"\\nMediation > Collider > Front-door > Exposure > Confounding > M-bias > Instrument 的 Δ 排序： Mediation 最大因为间接效应的非线性依赖 M 的类别分布；Instrument 最小因为 IV 估计 主要依赖 Z 的第一阶段 F-statistic，对类别合并方式的敏感度较低。\\n\"\n  },\n  {\n    \"name\": \"ASV formal proofs for 3 priority topologies\",\n    \"description\": \"推导 confounding, mediation, collider 三个优先拓扑的 ASV 表达式。 形式化证明单调性（ASV 随 δ 增大而增大）和紧性（bound 可被某个 C 达到）。 MC 验证：1000 scenarios × coverage at 90%, 95%, 99% levels。\\n\",\n    \"results\": {\n      \"asv_sharpness_formal_proofs\": 3,\n      \"asv_monotonicity_proofs\": 3,\n      \"proof_technique_confounding\": \"algebraic — closed-form ASV as function of spectral gap of C and δ\",\n      \"proof_technique_mediation\": \"algebraic + envelope theorem — indirect effect ASV via product-of-coefficients decomposition\",\n      \"proof_technique_collider\": \"algebraic + Lagrangian optimization — ASV as constrained optimization over C perturbation space\",\n      \"asv_coverage_90_nominal\": 0.912,\n      \"asv_coverage_95_nominal\": 0.952,\n      \"asv_coverage_99_nominal\": 0.988,\n      \"asv_coverage_by_topology\": {\n        \"confounding_95\": 0.958,\n        \"mediation_95\": 0.949,\n        \"collider_95\": 0.948\n      },\n      \"mc_scenarios\": 1000,\n      \"mc_reps_per_scenario\": 500,\n      \"sharpness_achieving_C_found\": \"100% of scenarios — constructive proof provides explicit C* achieving bound\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: ASV Formal Proof Summary\",\n        \"columns\": [\n          \"Topology\",\n          \"Monotonicity\",\n          \"Sharpness\",\n          \"Proof Technique\",\n          \"Constructive C*?\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"✓ Proved\",\n            \"✓ Proved\",\n            \"Algebraic (spectral gap)\",\n            \"Yes — explicit\"\n          ],\n          [\n            \"Mediation\",\n            \"✓ Proved\",\n            \"✓ Proved\",\n            \"Algebraic + envelope theorem\",\n            \"Yes — explicit\"\n          ],\n          [\n            \"Collider\",\n            \"✓ Proved\",\n            \"✓ Proved\",\n            \"Lagrangian optimization + KKT\",\n            \"Yes — explicit\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: ASV Coverage Calibration (MC, 1000 scenarios)\",\n        \"columns\": [\n          \"Topology\",\n          \"Nominal 90%\",\n          \"Actual 90%\",\n          \"Nominal 95%\",\n          \"Actual 95%\",\n          \"Nominal 99%\",\n          \"Actual 99%\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"90%\",\n            \"91.8%\",\n            \"95%\",\n            \"95.8%\",\n            \"99%\",\n            \"99.2%\"\n          ],\n          [\n            \"Mediation\",\n            \"90%\",\n            \"90.9%\",\n            \"95%\",\n            \"94.9%\",\n            \"99%\",\n            \"98.7%\"\n          ],\n          [\n            \"Collider\",\n            \"90%\",\n            \"90.8%\",\n            \"95%\",\n            \"94.8%\",\n            \"99%\",\n            \"98.5%\"\n          ],\n          [\n            \"Average\",\n            \"90%\",\n            \"91.2%\",\n            \"95%\",\n            \"95.2%\",\n            \"99%\",\n            \"98.8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个完整形式化证明是本论文最重要的理论贡献之一。ASV 类比于因果推断中的 E-value： E-value 量化 \\\"多大的未测量混淆才能推翻结论\\\"，ASV 量化 \\\"多大的标注误差才能推翻结论\\\"。 关键区别：E-value 只需一个标量参数（RR），ASV 需要参考混淆矩阵 + δ 方向， 因此证明复杂度更高。构造性紧性证明（显式 C*）不仅有理论价值，还有实践价值—— 研究者可以检查 \\\"使结论翻转的最近 C* 与我的实证 C 有多远\\\"，获得直觉性理解。\\n\\n\\n三个证明均成功（asv_sharpness_formal_proofs = 3）：这是 best tier 的硬性要求，但也是 数学上可行的，因为三个拓扑的偏倚表达式在 K=3 时有足够简洁的闭式形式。\\nConfounding ASV：残差混淆偏倚 = OVB × (1 - f(C))，其中 f(C) 是 C 的对角优势函数。 ASV = min{δ : |OVB × (1-f(C·diag(1+δ)))| > threshold}。单调性：f 关于 δ 单调递减 （扰动增大→C 偏离对角→更多残差混淆），因此 ASV 单调。紧性：构造 C* = 在 δ 约束下 使 f(C*) 最小化的行随机矩阵（显式构造）。\\nMediation ASV：间接效应 = β_XM × β_MY|X，两者均是 C 的函数。ASV 通过乘积分解为 两个单调函数的乘积——当两者符号一致时整体单调，当符号不一致时需要 envelope theorem 处理极值切换，但最终仍可证明关于 δ 的单调性。紧性通过构造性 Lagrangian 求解 使间接效应恰好等于 threshold 的 C*。\\nCollider ASV：条件化打开伪路径的效应大小是 C 的非线性函数。通过 Lagrangian 优化 在 {C : ||C - I|| ≤ g(δ)} 约束集上求解伪效应的极值，证明该极值关于 δ 单调。 紧性：Lagrangian 的 KKT 条件给出显式 C*。\\nCoverage at 95% nominal = 0.952（在 [0.93, 0.97] 范围内）：轻微过覆盖（0.952 > 0.950） 是因为 ASV bound 使用了保守的 worst-case C 方向，而大多数实际 C 不在最坏方向上。 这种过覆盖是良性的（保守偏倚）。Mediation (0.949) 和 collider (0.948) 的覆盖率 略低于 confounding (0.958)，因为这两个拓扑的偏倚函数非线性更强， ASV 的线性化近似在极端 δ 值附近不够精确。\\n\"\n  },\n  {\n    \"name\": \"ASV MC validation for remaining 3 topologies\",\n    \"description\": \"对 M-bias, instrument, front-door 三个拓扑推导 ASV 表达式，MC 验证单调性和覆盖率。 紧性作为猜想，用数值证据支持。\\n\",\n    \"results\": {\n      \"asv_monotonicity_mc_validated\": 3,\n      \"asv_monotonicity_violations\": 0,\n      \"asv_coverage_95_mbias\": 0.954,\n      \"asv_coverage_95_instrument\": 0.961,\n      \"asv_coverage_95_frontdoor\": 0.943,\n      \"sharpness_numerical_gap\": \"< 0.008 across all 3 topologies (bound within 0.8% of achievable)\",\n      \"sharpness_conjecture_status\": \"Supported by 1000 scenario numerical optimization — no counterexample found\",\n      \"frontdoor_asv_note\": \"Front-door ASV 涉及两阶段估计的联合扰动，闭式紧性证明需要解决双线性约束优化，identified as immediate future work\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: ASV Validation for Remaining Topologies\",\n        \"columns\": [\n          \"Topology\",\n          \"Monotonicity\",\n          \"Coverage @95%\",\n          \"Sharpness Gap\",\n          \"Formal Proof Status\"\n        ],\n        \"rows\": [\n          [\n            \"M-bias\",\n            \"✓ MC-validated (0 violations/1000)\",\n            \"95.4%\",\n            \"0.006\",\n            \"Conjecture (numerical)\"\n          ],\n          [\n            \"Instrument\",\n            \"✓ MC-validated (0 violations/1000)\",\n            \"96.1%\",\n            \"0.005\",\n            \"Conjecture (numerical)\"\n          ],\n          [\n            \"Front-door\",\n            \"✓ MC-validated (0 violations/1000)\",\n            \"94.3%\",\n            \"0.008\",\n            \"Conjecture (numerical)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"诚实地将紧性限定为猜想（而非证明）是策略性选择：(1) 避免 reviewer 质疑证明严谨性， (2) 数值证据已经足够有说服力（gap < 0.008），(3) 完整证明作为 immediate future work  为后续论文提供了明确方向。六个拓扑的 ASV 框架完整性：3 个有完整证明 + 3 个有强数值支持， 覆盖了实践者可能遇到的所有主要 DAG 设计。\\n\\n\\n单调性在所有 3 个拓扑的 MC 验证中均成立（0 violations）：单调性是一个\\\"自然\\\"性质—— 更大的标注误差（更大的 δ）只能增加偏倚的潜在范围，不能减少它。这在直觉上成立： δ 增大扩展了 C 的可行域，而偏倚 bound 是在可行域上的 supremum， 可行域扩大 → supremum 不减。形式化证明的技术难点在于处理非凸可行域， 但 MC 验证表明即使在解析证明困难的情况下，性质仍成立。\\n紧性作为猜想而非证明：M-bias 的 DAG 结构（butterfly）使偏倚表达式涉及 4 个 条件概率的乘积，优化问题是四次多项式约束优化，闭式解不可行。 Instrument 的 Wald ratio 使约束优化涉及分式规划。 Front-door 的两阶段结构使约束是双线性的。 数值优化（sequential quadratic programming）在所有场景中找到的最优 C  与 ASV bound 的差距 < 0.008，强烈支持紧性但不构成证明。\\nFront-door coverage 略低（0.943）：两阶段估计的非线性使 ASV 的线性化近似 在 extreme δ 附近不够精确，但仍在 [0.93, 0.97] 范围内。\\n\"\n  },\n  {\n    \"name\": \"ASV calibration on empirical data\",\n    \"description\": \"将 ASV 框架应用于 plan_003 的实证混淆矩阵。在 held-out gold-standard splits 上验证覆盖率。 报告 ASV alongside downstream effect estimates。比较 ASV 可解释性与原始混淆矩阵报告。\\n\",\n    \"results\": {\n      \"empirical_asv_concordance\": 8,\n      \"empirical_asv_concordance_detail\": \"9 个 scenario（3 tasks × 3 topological contexts）中 8 个 ASV 排序与实际 bias 严重度一致\",\n      \"discordant_case\": \"protest × instrument context: ASV 排序 DeepSeek > Qwen，实际 bias Qwen > DeepSeek（差异 0.02，在 noise margin 内）\",\n      \"asv_interpretability_rating\": \"研究者 pilot（N=5）中 4/5 偏好 ASV + sensitivity curve 而非原始 C 矩阵\",\n      \"held_out_coverage_95\": 0.94,\n      \"asv_actionable_alerts\": \"3/9 scenarios ASV < 1.5（结论脆弱），6/9 ASV > 3.0（结论稳健）\",\n      \"asv_correctly_flags_reversal_risk\": \"2/2 scenarios where empirical C falls in reversal zone are flagged by ASV < 1.5\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: ASV Concordance with Empirical Bias Severity\",\n        \"columns\": [\n          \"Task\",\n          \"Topological Context\",\n          \"Model Ranking by ASV\",\n          \"Model Ranking by Actual Bias\",\n          \"Concordant?\"\n        ],\n        \"rows\": [\n          [\n            \"Protest\",\n            \"Mediation\",\n            \"Qwen < Llama < DeepSeek\",\n            \"Qwen < Llama < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Protest\",\n            \"Collider\",\n            \"Qwen < Llama < DeepSeek\",\n            \"Qwen < Llama < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Protest\",\n            \"Instrument\",\n            \"DeepSeek < Qwen < Llama\",\n            \"Qwen < DeepSeek < Llama\",\n            \"✗ (margin 0.02)\"\n          ],\n          [\n            \"Stance\",\n            \"Mediation\",\n            \"Qwen < Llama < DeepSeek\",\n            \"Qwen < Llama < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Stance\",\n            \"Collider\",\n            \"Llama < Qwen < DeepSeek\",\n            \"Llama < Qwen < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Stance\",\n            \"Confounding\",\n            \"Llama < Qwen < DeepSeek\",\n            \"Llama < Qwen < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Toxicity\",\n            \"Mediation\",\n            \"Qwen < Llama < DeepSeek\",\n            \"Qwen < Llama < DeepSeek\",\n            \"✓\"\n          ],\n          [\n            \"Toxicity\",\n            \"Collider\",\n            \"Qwen < DeepSeek < Llama\",\n            \"Qwen < DeepSeek < Llama\",\n            \"✓\"\n          ],\n          [\n            \"Toxicity\",\n            \"Confounding\",\n            \"Qwen < Llama < DeepSeek\",\n            \"Qwen < Llama < DeepSeek\",\n            \"✓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: ASV Robustness Classification\",\n        \"columns\": [\n          \"Task\",\n          \"Context\",\n          \"Best Model ASV\",\n          \"Worst Model ASV\",\n          \"Classification\"\n        ],\n        \"rows\": [\n          [\n            \"Protest\",\n            \"Mediation\",\n            \"2.1 (DeepSeek)\",\n            \"0.9 (Qwen)\",\n            \"FRAGILE — reversal risk\"\n          ],\n          [\n            \"Protest\",\n            \"Collider\",\n            \"1.8 (DeepSeek)\",\n            \"1.1 (Qwen)\",\n            \"FRAGILE — reversal risk\"\n          ],\n          [\n            \"Protest\",\n            \"Instrument\",\n            \"3.2 (Llama)\",\n            \"2.4 (DeepSeek)\",\n            \"Moderate\"\n          ],\n          [\n            \"Stance\",\n            \"Mediation\",\n            \"4.1 (DeepSeek)\",\n            \"2.8 (Qwen)\",\n            \"Robust\"\n          ],\n          [\n            \"Stance\",\n            \"Collider\",\n            \"3.8 (DeepSeek)\",\n            \"2.5 (Llama)\",\n            \"Moderate\"\n          ],\n          [\n            \"Stance\",\n            \"Confounding\",\n            \"5.2 (DeepSeek)\",\n            \"3.9 (Llama)\",\n            \"Robust\"\n          ],\n          [\n            \"Toxicity\",\n            \"Mediation\",\n            \"7.3 (Llama)\",\n            \"5.1 (Qwen)\",\n            \"Robust\"\n          ],\n          [\n            \"Toxicity\",\n            \"Collider\",\n            \"6.8 (Llama)\",\n            \"4.9 (Qwen)\",\n            \"Robust\"\n          ],\n          [\n            \"Toxicity\",\n            \"Confounding\",\n            \"8.1 (DeepSeek)\",\n            \"6.2 (Qwen)\",\n            \"Robust\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"8/9 concordance 证明 ASV 在实践中是有效的偏倚严重度指标。唯一 discordance 出现在 noise margin 内，且在 instrument context（本身就是高方差估计）。关键实用发现： protest event coding 在 mediation/collider context 下使用 Qwen 3.5 Plus 时 ASV < 1.0—— 这意味着研究者如果用 Qwen 做 protest 分类并将其作为 mediator/collider，其下游因果结论 几乎肯定不可靠。这种 actionable alert 是单纯报告混淆矩阵无法提供的。\\n\\n\\nConcordance 8/9：ASV 是基于 worst-case perturbation 的 bound，而非 point estimate。 在大多数场景中，worst-case 方向与实际偏倚方向一致，因此排序一致。 唯一 discordant case 出现在 instrument context，因为 Wald ratio 对 C 的微小差异 极其敏感（分母接近零时），导致 ASV 排序与实际偏倚排序在 noise margin 内翻转。 差异仅 0.02，在实际意义上可忽略。\\n3/9 scenarios ASV < 1.5：这些对应 protest coding（K=5, 低对角优势 C）在  mediation 和 collider 拓扑下的应用。ASV < 1.5 意味着仅需 50% 的额外标注误差 即可推翻结论——这是一个强警告信号。6/9 ASV > 3.0 对应较简单的 toxicity 任务 和 confounding 拓扑，结论稳健。\\nASV 正确标记了 2 个落入反转区域的实证 C：这是 ASV 框架实用价值的最直接证据。 研究者报告原始 C 矩阵时无法判断\\\"这个 C 有多危险\\\"——ASV 提供了这个判断。\\nHeld-out coverage 0.94（vs 理论 0.95）：轻微欠覆盖因为实证 C 的估计本身有 sampling variance（~30K annotations），引入了理论分析未考虑的噪声。 但 0.94 在可接受范围内。\\n\"\n  },\n  {\n    \"name\": \"Correction guidance framework validation\",\n    \"description\": \"构建决策框架：{topology × error structure × ASV} → correction method（DSL / PPI / MLA / naive plug-in / \\\"无现有方法适用\\\"）。 MC 验证推荐方法在各场景中是否产生最小偏倚。在 plan_003 数据上经验验证。\\n\",\n    \"results\": {\n      \"correction_framework_accuracy\": 0.95,\n      \"correction_framework_accuracy_detail\": \"432 个 MC scenario 中 411 个推荐方法产生最小 bias\",\n      \"scenarios_tested\": 432,\n      \"scenario_breakdown\": \"6 topologies × 6 C structures × 3 K values × 4 effect sizes = 432\",\n      \"method_recommendation_distribution\": {\n        \"DSL\": \"18% of scenarios\",\n        \"PPI\": \"24% of scenarios\",\n        \"MLA\": \"31% of scenarios\",\n        \"naive_plugin\": \"12% of scenarios\",\n        \"no_adequate_method\": \"15% of scenarios\"\n      },\n      \"no_adequate_method_conditions\": \"primarily: correlated multi-LLM errors + differential K≥5 + collider/front-door topology\",\n      \"failure_cases\": \"21/432 — 14 cases where MLA and PPI are within 0.005 of each other (recommendation arbitrary), 7 cases where extreme C + small N makes all methods unstable\",\n      \"empirical_validation_plan003\": \"8/9 empirical scenarios — recommended method produces bias reduction ≥40% vs uncorrected\",\n      \"empirical_failure\": \"1/9 — protest × collider × Qwen: no method adequate (flagged correctly as 'no adequate method')\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Correction Method Recommendation Distribution\",\n        \"columns\": [\n          \"Method\",\n          \"% Scenarios\",\n          \"Typical Condition\",\n          \"Avg Bias Reduction\"\n        ],\n        \"rows\": [\n          [\n            \"MLA\",\n            \"31%\",\n            \"C known, K≤5, non-differential\",\n            \"72%\"\n          ],\n          [\n            \"PPI\",\n            \"24%\",\n            \"C uncertain, gold-standard available\",\n            \"65%\"\n          ],\n          [\n            \"DSL\",\n            \"18%\",\n            \"Confounding topology, high diag. dominance\",\n            \"58%\"\n          ],\n          [\n            \"Naive plug-in\",\n            \"12%\",\n            \"ASV > 5.0 (robust conclusions)\",\n            \"N/A (unnecessary)\"\n          ],\n          [\n            \"No adequate method\",\n            \"15%\",\n            \"Correlated errors + differential + collider/front-door\",\n            \"N/A\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 14: Framework Accuracy by Topology\",\n        \"columns\": [\n          \"Topology\",\n          \"Scenarios\",\n          \"Correct\",\n          \"Accuracy\",\n          \"Most Common Failure Mode\"\n        ],\n        \"rows\": [\n          [\n            \"Confounding\",\n            \"72\",\n            \"71\",\n            \"98.6%\",\n            \"MLA ≈ PPI (indistinguishable)\"\n          ],\n          [\n            \"Mediation\",\n            \"72\",\n            \"69\",\n            \"95.8%\",\n            \"Extreme C + small N\"\n          ],\n          [\n            \"Collider\",\n            \"72\",\n            \"67\",\n            \"93.1%\",\n            \"MLA ≈ PPI + extreme C\"\n          ],\n          [\n            \"M-bias\",\n            \"72\",\n            \"70\",\n            \"97.2%\",\n            \"Rare edge case\"\n          ],\n          [\n            \"Instrument\",\n            \"72\",\n            \"69\",\n            \"95.8%\",\n            \"Wald ratio instability\"\n          ],\n          [\n            \"Front-door\",\n            \"72\",\n            \"65\",\n            \"90.3%\",\n            \"Two-stage estimation complexity\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"95% 准确率表明基于理论的决策框架在实践中可靠。最重要的发现不是哪个方法最好， 而是 \\\"方法选择是拓扑依赖的\\\"——在 confounding DAG 中最优的方法在 collider DAG 中 可能增加偏倚。这直接回应了 Jerzak et al. (EMNLP 2025) 的 unconditional benchmarking  方法论：如果不考虑拓扑，benchmarking 本身就是误导性的。 15% \\\"no adequate method\\\" 区域是诚实的 open problem identification， 为后续方法论研究提供了明确方向。\\n\\n\\n95% accuracy（411/432）：决策框架基于理论偏倚表达式的 closed-form 分析， 在每个 {topology × C structure} cell 中选择使残差偏倚最小化的方法。 14 个\\\"失败\\\"case 实际上是 MLA 和 PPI 表现几乎相同（差异 < 0.005）的场景—— 框架推荐了其中一个，但另一个同样好。这不是真正的失败，只是不确定性。 7 个真正失败的 case 出现在极端 C（near-permutation）+ 小样本（N=1000）下， 所有方法都不稳定——这种场景下正确答案可能是\\\"收集更多数据\\\"而非选择方法。\\nMethod distribution：MLA（31%）最常被推荐因为它直接利用 C 矩阵做 deconvolution， 在 C 已知时通常最优。PPI（24%）在 C 有不确定性时被推荐（利用少量 gold-standard 数据 做 prediction-powered inference）。DSL（18%）在 confounding topology +  high diagonal dominance C 下被推荐（double sampling + likelihood correction）。 Naive plug-in（12%）仅在 ASV > 5.0（结论非常稳健）时被推荐——此时 correction  的 variance cost 大于 bias reduction benefit。\\n15% \\\"no adequate method\\\"：这些场景主要涉及 correlated multi-LLM errors +  differential K≥5 + collider/front-door topology。这是论文 Claim 3 的一部分—— 识别现有方法不足的区域并标记为 open problems。其中 dependence-aware multi-LLM  correction 是最重要的 open problem（回应 Kim et al. ICML 2025）。\\nEmpirical 8/9：1 个\\\"failure\\\"实际上是框架正确标记为\\\"no adequate method\\\" （protest × collider × Qwen，C 接近 near-permutation + 模型间误差高度相关）。 这是一个 success case of honest scoping，而非真正失败。\\n\"\n  },\n  {\n    \"name\": \"Pathological confusion matrix analysis\",\n    \"description\": \"分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在所有拓扑中的 偏倚行为。识别预测偏倚严重度的结构性指标（spectral gap, diagonal dominance ratio）。\\n\",\n    \"results\": {\n      \"spectral_gap_bias_correlation\": 0.91,\n      \"diagonal_dominance_bias_correlation\": 0.87,\n      \"best_predictor\": \"spectral gap (1 - λ₂/λ₁) explains 83% of bias magnitude variance\",\n      \"catastrophic_bias_threshold\": \"spectral gap < 0.15 → bias > 2x effect size in ≥80% of reversal-prone topologies\",\n      \"near_permutation_analysis\": \"all near-permutation C (spectral gap < 0.05) produce reversal in mediation/collider/front-door; severity 1.5-3x\",\n      \"rank_deficient_analysis\": \"rank-deficient C always produce catastrophic bias regardless of topology — information loss is complete for collapsed dimensions\",\n      \"block_diagonal_analysis\": \"bias depends on which classes are in same block — if classes with opposite effects are merged, reversal guaranteed\",\n      \"practitioner_diagnostic\": \"two-number summary: (spectral gap, diagonal dominance ratio) → risk category (low/medium/high/catastrophic)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Structural Predictors of Bias Severity\",\n        \"columns\": [\n          \"Predictor\",\n          \"Correlation with |Bias|\",\n          \"R² (univariate)\",\n          \"Threshold for Catastrophic Bias\"\n        ],\n        \"rows\": [\n          [\n            \"Spectral gap (1-λ₂/λ₁)\",\n            \"-0.91\",\n            \"0.83\",\n            \"< 0.15\"\n          ],\n          [\n            \"Diagonal dominance ratio\",\n            \"-0.87\",\n            \"0.76\",\n            \"< 0.55\"\n          ],\n          [\n            \"Condition number of C\",\n            \"0.89\",\n            \"0.79\",\n            \"> 12\"\n          ],\n          [\n            \"Min diagonal element\",\n            \"-0.84\",\n            \"0.71\",\n            \"< 0.3\"\n          ],\n          [\n            \"Spectral gap + diag. dom. (joint)\",\n            \"—\",\n            \"0.89\",\n            \"Combined threshold\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"为实践者提供了两个可操作的诊断数字：spectral gap 和 diagonal dominance ratio。 研究者无需理解完整的偏倚理论，只需计算其实证 C 矩阵的这两个指标， 即可判断偏倚风险等级。这补充了 ASV 框架——ASV 告诉你\\\"结论多稳健\\\"， 而 spectral diagnostics 告诉你\\\"为什么不稳健\\\"和\\\"C 的哪个方面最危险\\\"。 Catastrophic threshold（spectral gap < 0.15）在 plan_003 的实证数据中 对应 Qwen 在 protest coding 某些 prompt 变体下的 C 矩阵——与 ASV < 1.0  的 fragile classification 完全一致。\\n\\n\\nSpectral gap 与偏倚强相关（r=0.91）：混淆矩阵 C 的第二大特征值 λ₂ 控制了 \\\"主误分类模式\\\"的强度。当 spectral gap = 1-λ₂/λ₁ 接近 0 时，C 接近非满秩， 信息丢失严重，偏倚灾难性。这不是偶然——偏倚表达式中 C 的逆（或伪逆）出现在 correction 中，spectral gap 控制了逆的条件数。\\nDiagonal dominance 相关性略低（0.87 vs 0.91）因为 diagonal dominance  是一个粗糙的指标——它只看对角元素与行和的比值，不捕获 off-diagonal 的结构 （如 block-diagonal 的特殊性）。Spectral gap 通过特征分解捕获了完整的  off-diagonal 结构信息。\\nNear-permutation 全部产生反转（在反转敏感拓扑中）：near-permutation C  等价于类别标签几乎完全互换，这在 K≥3 时结构性地翻转效应方向（而 K=2 时 近置换 = 高误分类率，仍然只 attenuate toward null）。\\nBlock-diagonal 的方向依赖于块结构：如果具有相反效应的类别被合并在同一块中， 块内平均化可以翻转块的净效应方向。这与 binarization collapse 的机制相同， 但发生在 C 矩阵内部而非研究者的显式折叠中。\\n\"\n  },\n  {\n    \"name\": \"annot-sensitivity Python toolkit\",\n    \"description\": \"开源 Python 包：用户输入 DAG + confusion matrix + downstream estimate → 输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation + diagnostic plots。 pip-installable，含每个拓扑的 worked examples。\\n\",\n    \"results\": {\n      \"package_name\": \"annot-sensitivity\",\n      \"pip_installable\": true,\n      \"supported_topologies\": 6,\n      \"supported_K_range\": \"2-20\",\n      \"api_surface\": \"3 main functions: bias_expression(), asv_bound(), recommend_correction()\",\n      \"documentation\": \"6 topology-specific tutorials (Jupyter notebooks), API reference, quickstart guide\",\n      \"test_coverage\": \">90%\",\n      \"benchmark\": \"bias_expression() < 0.1s for K≤7; asv_bound() < 1s for K≤7; recommend_correction() < 0.5s\",\n      \"dependencies\": \"numpy, scipy, matplotlib (minimal)\",\n      \"worked_examples\": 6\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Toolkit 的设计哲学是\\\"一个函数回答一个问题\\\"。研究者的典型 workflow： (1) 收集 gold-standard 子集 → 估计 C；(2) 调用 bias_expression(dag, C, K) →  了解偏倚结构；(3) 调用 asv_bound(dag, C, estimate, threshold) → 了解结论稳健性； (4) 调用 recommend_correction(dag, C, asv, n_gold) → 选择校正方法。 开源发布对 AAAI/ARR 审稿均加分——artifact evaluation 是近年趋势。\\n\\nToolkit 是论文影响力的关键放大器。学术论文的理论贡献如果没有可用工具， 很难被实践者采纳。三个主函数对应论文三个 claims：bias_expression() → Claim 1（taxonomy）， asv_bound() → Claim 2（ASV），recommend_correction() → Claim 3（correction guidance）。\\nK 支持范围 2-20：K=2 作为 consistency check（应恢复经典二分类结果）， K>7 用矩阵表达式 + 特征分解可解释性工具。K>20 实际中极罕见且计算成本高 （C 矩阵有 K(K-1) 自由参数），故限定上界。\\n性能目标（< 1s for K≤7）：bias_expression 和 recommend_correction 是闭式计算， 主要耗时在矩阵运算。asv_bound 涉及优化问题（构造性紧性需要求解约束优化）， K≤7 时维度足够低，SQP 在 1s 内收敛。\\n最小依赖（numpy, scipy, matplotlib）：降低安装门槛，compatible with  任何 Python 科学计算环境。不依赖 PyTorch/TensorFlow 因为所有计算是 解析数学而非机器学习。\\n\"\n  }\n]",
      "numLines": 1138,
      "startLine": 1,
      "totalLines": 1138
    }
  },
  "sourceToolAssistantUUID": "5c67425a-926e-4f8f-865d-78a00c3e9b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T08:24:24.277Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NwmYkkHWH7qFMCCAkv5Sjx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46e4c38b-0899-4f45-b200-cfd8911c11b3",
  "isSidechain": false,
  "requestId": "req_011CbDVwuVw4vzq4JC2vYpGT",
  "type": "assistant",
  "uuid": "2b826cad-a5df-4ddf-b759-a93f8f383cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZBishK8fNJhTS2WZeoPBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11806,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11806
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

_source line 11 · 2026-05-20T08:24:24.290Z_

<details><summary>↩ Tool result · `toolu_01NwmYkkHWH7qFMCCAkv5Sjx`</summary>

```text
1	# Paper Framing — causal_annot_error_attrib
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)
5	- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)
6	- Tertiary: ICWSM 2027 Round 2 (2026-09-15)
7	
8	## Title
9	Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies
10	
11	## Core Claims (3 条)
12	
13	1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).
14	
15	2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.
16	
17	3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.
18	
19	## Story Spine
20	
21	- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.
22	
23	- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.
24	
25	- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.
26	
27	- **Headline result template**: "Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias."
28	
29	## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001
30	
31	### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)
32	The binary guarantee that "non-differential exposure misclassification biases toward the null" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification ("bias can go in either direction"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to "escape" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).
33	
34	### Version B (no direction reversal found across topologies)
35	Multi-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.
36	
37	**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.
38	
39	## MVP Evidence
40	
41	**Confounding DAG + K=3** (confounder misclassification):
42	- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated
43	- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization
44	- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is "well-behaved" (predictable direction)
45	- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.
46	
47	**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):
48	- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification
49	- K=2 control: 6/6 toward null (binary guarantee holds)
50	- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)
51	- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)
52	- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim
53	
54	## Venue Fit Risks
55	
56	- **AAAI**: Broad AI audience — emphasize general methodology for "automated annotation measurement error," not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.
57	- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.
58	- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.
59	
60	## Anticipated Reviewer Concerns & Planned Responses
61	
62	1. **"Trivial extension of binary to multi-class"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]
63	
64	2. **"Lee & Wood-Doughty (2024) already did categorical"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]
65	
66	3. **"Why these 6 DAG topologies?"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]
67	
68	4. **"K≥5 expressions aren't actionable"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]
69	
70	5. **"ASV sharpness only proved for 3 topologies"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]
71	
72	6. **"Correlated multi-LLM errors?"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]
73	
74	7. **"Empirical validation scope"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b826cad-a5df-4ddf-b759-a93f8f383cdc",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "a23560cd-4773-43c0-aa90-7af65f0eb342",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md",
      "content": "# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "2b826cad-a5df-4ddf-b759-a93f8f383cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attri…",
  "leafUuid": "a23560cd-4773-43c0-aa90-7af65f0eb342",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate causal annotation error attribution paper",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Assistant

_source line 14 · 2026-05-20T08:24:41.480Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check if the paper-writing-norms skill exists and read it for style guidance.

Actually, I need to read the paper-writing-norms skill for LaTeX writing best practices.

Let me also check if pdflatex is available and if the output directory exists.

Let me proceed to write the full LaTeX paper. I have:

1. 9 experiments with detailed results and tables
2. Paper framing with title, claims, story spine, venue info
3. Narrative guidance about Version A being confirmed

Let me now structure the paper:

- Abstract
- Introduction (story spine + core claims)


- Related Work
- Method (bias taxonomy + ASV framework + correction guidance)
- Experiments (all 9 experiments mapped to sections/tables)
- Conclusion

The experiments map to:
1. Multi-topology bias derivation (K=3) → Tables 1-2
2. General K bias expressions (K=5,7) → Tables 3-4
3. Empirical confusion matrices → Tables 5-6
4. Binarization collapse → Table 7
5. ASV formal proofs (3 priority) → Tables 8-9
6. ASV MC validation (remaining 3) → Table 10
7. ASV calibration on empirical data → Tables 11-12
8. Correction guidance framework → Tables 13-14
9. Pathological C analysis → Table 15
10. Annotation-sensitivity toolkit → mentioned in text

Now I'm ready to write the paper, pulling all numbers directly from the experiment data and making sure every result is grounded in what I've actually computed. I need to verify the directory structure and then generate the full manuscript with proper rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a23560cd-4773-43c0-aa90-7af65f0eb342",
  "isSidechain": false,
  "requestId": "req_011CbDVxM2LoZah4CsGXdvWZ",
  "type": "assistant",
  "uuid": "ffb8d5b9-3bdf-4a33-a320-6ef4f71fdf16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LawLZTUDpaTG49K6f9B5cr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23577,
      "cache_read_input_tokens": 23647,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 23647,
          "cache_creation_input_tokens": 23577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23577
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

_source line 15 · 2026-05-20T08:24:41.482Z_

Let me check the directory exists and whether pdflatex is available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffb8d5b9-3bdf-4a33-a320-6ef4f71fdf16",
  "isSidechain": false,
  "requestId": "req_011CbDVxM2LoZah4CsGXdvWZ",
  "type": "assistant",
  "uuid": "ccbd85db-0fdb-4bbb-b819-3609bb8cc598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LawLZTUDpaTG49K6f9B5cr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23577,
      "cache_read_input_tokens": 23647,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 23647,
          "cache_creation_input_tokens": 23577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23577
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

_source line 16 · 2026-05-20T08:24:42.046Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KuvnJLBQw8QntPnnJsPpVP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/ && which pdflatex",
  "description": "Check output directory and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccbd85db-0fdb-4bbb-b819-3609bb8cc598",
  "isSidechain": false,
  "requestId": "req_011CbDVxM2LoZah4CsGXdvWZ",
  "type": "assistant",
  "uuid": "97544922-8e3a-4980-9afa-a6976b8d1fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LawLZTUDpaTG49K6f9B5cr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23577,
      "cache_read_input_tokens": 23647,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 23647,
          "cache_creation_input_tokens": 23577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23577
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

_source line 17 · 2026-05-20T08:24:42.231Z_

<details><summary>↩ Tool result · `toolu_01KuvnJLBQw8QntPnnJsPpVP`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97544922-8e3a-4980-9afa-a6976b8d1fd3",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "43476491-10d2-432b-9848-7f6dbd3fc316",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "97544922-8e3a-4980-9afa-a6976b8d1fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T08:25:10.715Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists and pdflatex is available. Now let me write the full LaTeX paper.

I need to carefully structure it with all the experiments mapped to sections and tables. Let me draft the complete LaTeX source.

Key data points to include from experiment_data.json:

**Experiment 1: Multi-topology bias derivation (K=3)**
- Theory-MC match rate: 0.972 (35/36 within 95% CI)
- 4 reversal topologies: exposure, mediation, collider, front-door
- 2 non-reversal: confounding, instrument


- Mediation shows a 0.52 violation rate with 0.47 sign reversals and 0.11 amplification, while collider has 0.41 violations with 0.36 sign reversals and 0.09 amplification. Front-door follows with 0.34 violations, 0.28 sign reversals, and 0.12 amplification. The non-reversal topologies show no violations—M-bias ranges from 0.04 to 0.18, instrument from 0.02 to 0.14, and confounding from 0.063 to 0.298.

Now looking at the results across different K values and empirical settings. With K=5 and K=7, mediation violations increase to 0.61 and 0.68 respectively, while collider violations reach 0.49 and 0.55. The eigendecomposition captures 87% of variance in the top-2 components and 96% in the top-3, with worst-case bound tightness at 88%. For the empirical confusion matrices across ~270K annotations, protest achieves 0.62 diagonal dominance at K=5, stance reaches 0.74 at K=3, and toxicity hits 0.89 at K=2, with cross-model error correlation at 0.58. The binarization collapse experiment shows a maximum difference of 0.19 for mediation at K=7.

For the ASV formal proofs covering confounding, mediation, and collider scenarios, coverage improves from 90% to 91.2% at the nominal level, 95% to 95.2% at the 95% level, and 99% to 98.8% at the 99% level. The remaining three scenarios—M-bias, instrument, and front-door—show zero monotonicity violations across 1000 Monte Carlo runs, with coverage rates of 95.4%, 96.1%, and 94.3% respectively, though there's still a sharpness gap to address.

Calibration on empirical data achieves 8 out of 9 concordance with held-out coverage at 95% reaching 0.94. The correction framework demonstrates 95% accuracy across 432 cases, with method distribution showing MLA at 31%, PPI at 24%, DSL at 18%, naive at 12%, and none at 15%. For pathological confounding analysis, spectral gap correlates strongly at 0.91 with R² of 0.83, identifying a catastrophic threshold when spectral gap drops below 0.15. Finally, the annotation-sensitivity toolkit spans 6 topologies with K values from 2 to 20 and achieves over 90% test performance.

Now I'm thinking about how to structure the paper itself. The target is AAAI 2027 format with a 7-page limit plus references, though I want to make sure the content is solid regardless of the exact formatting constraints. I'll use a standard article class that's compatible and focuses on getting the research clearly presented rather than worrying about perfect formatting compliance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43476491-10d2-432b-9848-7f6dbd3fc316",
  "isSidechain": false,
  "requestId": "req_011CbDVyfe473kDYLgRwtQ9Y",
  "type": "assistant",
  "uuid": "01a68233-55bf-44df-b3ec-07ba952592a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGCLcovBC8GPgdnw9p7MN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 47224,
      "output_tokens": 14366,
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
          "output_tokens": 14366,
          "cache_read_input_tokens": 47224,
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

### Assistant

_source line 19 · 2026-05-20T08:25:10.717Z_

Now I'll write the full paper. This is a substantial document covering all 9 experiments with 15 tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a68233-55bf-44df-b3ec-07ba952592a1",
  "isSidechain": false,
  "requestId": "req_011CbDVyfe473kDYLgRwtQ9Y",
  "type": "assistant",
  "uuid": "992f0e7a-5447-4a78-b7a1-230e9ae3238b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGCLcovBC8GPgdnw9p7MN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 47224,
      "output_tokens": 14366,
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
          "output_tokens": 14366,
          "cache_read_input_tokens": 47224,
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

_source line 20 · 2026-05-20T08:28:48.631Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Pmgki35CFeU9zcTNr1hDFW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{corollary}{Corollary}\n\\newtheorem{definition}{Definition}\n\\newtheorem{conjecture}{Conjecture}\n\n\\newcommand{\\bC}{\\mathbf{C}}\n\\newcommand{\\bI}{\\mathbf{I}}\n\\newcommand{\\bB}{\\mathbf{B}}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge language models (LLMs) are rapidly replacing human annotators in computational social science, yet recent audits show that 31\\% of downstream causal conclusions drawn from LLM-annotated data are incorrect.\nWe show that the classical guarantee---non-differential misclassification biases toward the null---breaks when annotated variables have $K\\!\\ge\\!3$ categories.\nThe bias behavior is \\emph{topology-dependent}: the same confusion matrix that produces innocuous residual bias in a confounding DAG can produce direction-reversing bias in mediation or collider DAGs.\nWe make three contributions.\n\\textbf{(1)}~A \\emph{multi-class bias taxonomy}: closed-form bias expressions for $K\\!=\\!3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$, across six canonical DAG topologies.\nFour of six topologies (exposure, mediation, collider, front-door) exhibit direction reversal under non-differential $K\\!\\ge\\!3$ error; confounding and instrument topologies preserve monotonicity.\n\\textbf{(2)}~\\emph{Annotation Sensitivity Values} (ASVs), analogous to E-values for unmeasured confounding, that quantify how much annotation error is needed to overturn a conclusion.\nWe prove monotonicity and sharpness for three priority topologies and provide MC-validated conjectures for the remaining three.\n\\textbf{(3)}~A \\emph{correction guidance framework} mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to the appropriate correction method, achieving 95\\% recommendation accuracy across 432 simulated scenarios and validated on three CSS tasks annotated by three LLMs (${\\sim}270$K annotations).\nBinarizing a $K$-class variable to retreat into the binary safe zone is itself hazardous: collapsing $K\\!=\\!7$ to binary introduces up to $\\Delta\\!=\\!0.19$ additional bias, with 12\\% of scenarios exhibiting direction reversal from binarization alone.\nWe release \\texttt{annot-sensitivity}, an open-source Python toolkit implementing the full framework.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLMs have become the default annotation engine in computational social science (CSS).\nTheir speed and cost advantages are undeniable, but measurement error in LLM annotations propagates into downstream causal estimates.\n\\citet{baumann2025} audit this pipeline and find that 31\\% of downstream conclusions are already incorrect.\n\\citet{kim2025} show that cross-model annotation errors are highly correlated---when two LLMs both err, 60\\% of the time they err toward the same category---meaning multi-model ensembles cannot eliminate systematic bias.\n\nThe classical measurement-error literature provides reassurance for the binary case: non-differential misclassification of a binary exposure biases toward the null \\citep{bross1954}.\nPractitioners routinely extend this guarantee to multi-class variables by binarizing: collapsing $K$-class annotations into two categories before analysis.\nWe show that both the original guarantee and the binarization escape route fail for $K\\!\\ge\\!3$.\n\n\\paragraph{Core finding.}\nNon-differential $K\\!\\ge\\!3$ misclassification breaks the toward-null guarantee in 4 of 6 canonical DAG topologies.\nThe reversal pattern is strictly topology-dependent: the same confusion matrix that is benign in the confounding topology produces direction-reversing bias in mediation and collider topologies.\nIn our Monte Carlo experiments, the mediation topology exhibits a 52\\% violation rate (47\\% sign reversal), the collider topology 41\\% (36\\% sign reversal), the front-door topology 34\\% (28\\% sign reversal), and the exposure topology 85\\% (83.4\\% sign reversal) under 100K random confusion matrices.\nConfounding and instrument topologies maintain zero violations.\n\n\\paragraph{Why binarization is not a safe retreat.}\nCollapsing a $K$-class variable to binary discards inter-category bias structure.\nWe show that binarization introduces additional bias up to $\\Delta\\!=\\!0.19$ (mediation, $K\\!=\\!7$), and in 12\\% of $K\\!=\\!5{,}7$ scenarios the binarization itself flips the bias direction---making the collapsed estimate \\emph{worse} than the multi-class estimate.\n\n\\paragraph{Contributions.}\n\\textbf{(1)}~A multi-class bias taxonomy with closed-form and matrix-form bias expressions across six DAG topologies (\\S\\ref{sec:taxonomy}).\n\\textbf{(2)}~Annotation Sensitivity Values (ASVs) with formal monotonicity and sharpness proofs for three topologies and MC-validated conjectures for three more (\\S\\ref{sec:asv}).\n\\textbf{(3)}~A correction guidance framework achieving 95\\% recommendation accuracy (\\S\\ref{sec:correction}).\nWe validate all results on empirical confusion matrices from three LLMs across three CSS tasks (\\S\\ref{sec:empirical}) and release the \\texttt{annot-sensitivity} Python toolkit.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error in causal inference.}\nThe epidemiological literature on exposure misclassification dates to \\citet{bross1954}, with \\citet{brenner1993} first noting that polytomous confounder misclassification can bias in either direction.\n\\citet{vanderweele2019} provide sensitivity bounds for binary risk ratios.\nNone of these works provide systematic multi-class bias expressions across multiple DAG topologies.\n\n\\paragraph{Annotation error in NLP/CSS.}\n\\citet{wooddoughty2018} apply DAG reasoning to text classifier errors but produce no formal bias theorems and are limited to binary variables.\n\\citet{teblunthuis2024} provide the most complete binary treatment with MLA correction but are limited to $K\\!=\\!2$ and a single classifier.\n\\citet{lee2024} extend to categorical variables and LLM classifiers but cover only one DAG topology (unobserved confounding) on one dataset, with no systematic taxonomy or sensitivity analysis.\n\\citet{jerzak2025} benchmark correction methods but treat annotation error as monolithic---if different confusion matrix structures produce qualitatively different bias in different topologies, unconditional benchmarking is itself misleading.\n\n\\paragraph{Sensitivity analysis.}\nE-values \\citep{vanderweele2017} quantify robustness to unmeasured confounding via a single scalar.\nOur ASVs serve an analogous role for annotation error but require a reference confusion matrix and amplification direction, reflecting the richer parameterization of $K\\!\\times\\!K$ error structures.\n\n\n%% ============================================================\n%% 3  MULTI-CLASS BIAS TAXONOMY\n%% ============================================================\n\\section{Multi-Class Bias Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Setup and Notation}\n\nLet $\\tilde{V}$ denote the observed (LLM-annotated) version of a $K$-class variable $V$.\nThe misclassification process is characterized by the $K\\!\\times\\!K$ confusion matrix $\\bC$, where $C_{jk} = P(\\tilde{V}=k \\mid V=j)$.\nNon-differential misclassification requires $P(\\tilde{V} \\mid V, \\text{other variables}) = P(\\tilde{V} \\mid V)$, i.e., the error depends only on the true value.\nWe consider six canonical DAG topologies where $V$ plays distinct structural roles: confounder, treatment (exposure), mediator, collider, instrument, and front-door criterion variable.\n\nFor $K\\!=\\!3$, we derive closed-form bias expressions as functions of $\\bC$ and the structural parameters of each DAG.\nFor general $K$, we provide matrix-form expressions and develop three interpretability tools: (a) eigendecomposition summaries, (b) worst-case scalar bounds, and (c) spectral diagnostic indicators.\n\n\\subsection{Closed-Form Bias Expressions (K=3)}\n\\label{sec:kthree}\n\nFor each topology, we derive the bias $B(\\bC) = \\hat{\\theta}(\\tilde{V}) - \\theta^*(V)$ as a function of $\\bC$ and the true structural parameters.\nThe derivation proceeds by expressing the observed conditional distributions in terms of the true distributions and $\\bC$, then computing the resulting distortion in the estimand.\n\n\\paragraph{Validation.}\nWe validate all closed-form expressions via Monte Carlo simulation: 6 confusion matrix structures $\\times$ 6 topologies $\\times$ 1000 replications at $N\\!=\\!10{,}000$.\nThe theory-MC match rate is 97.2\\% (35/36 structure$\\times$topology combinations fall within 95\\% MC confidence intervals).\nThe single boundary case---front-door with rank-deficient $\\bC$---shows a discrepancy of 0.003 above the CI upper bound, which resolves at $N\\!=\\!50{,}000$.\nTable~\\ref{tab:theory-mc} reports the full match matrix.\n\n\\subsection{Topology-Dependent Reversal}\n\\label{sec:reversal}\n\nWe execute a 100K random $\\bC$ search for each topology, testing whether the bias violates the classical toward-null guarantee.\nThe topologies separate cleanly into two classes:\n\n\\begin{itemize}\n    \\item \\textbf{Information-loss topologies} (confounding, instrument, M-bias): misclassification only reduces the variable's information content; bias direction is predictable. Violation rate = 0 across all three.\n    \\item \\textbf{Structural-distortion topologies} (exposure, mediation, collider, front-door): misclassification alters the variable's functional role in the DAG, producing unpredictable direction reversal.\n\\end{itemize}\n\nTable~\\ref{tab:topology-reversal} reports the complete reversal analysis.\nThe exposure topology exhibits the highest violation rate (85.0\\%) because misclassification acts directly on the treatment variable.\nThe mediation topology (52.0\\%) is next: a near-permutation $\\bC$ that swaps adjacent category labels effectively flips the sign of $\\beta_{MY|X}$, reversing the indirect effect.\nWorst-case severity reaches $1.62\\times$ amplification with sign reversal in mediation, and spurious effect creation of 0.44 from a null truth in the collider topology.\n\n\\begin{table}[t]\n\\centering\n\\caption{Topology $\\times$ reversal summary under 100K random confusion matrices ($K\\!=\\!3$).}\n\\label{tab:topology-reversal}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lcccccc}\n\\toprule\nTopology & Role & Violation & Sign Rev. & Amplif. & Worst-Case & $K\\!=\\!2$ \\\\\n\\midrule\nConfounding & Confounder & 0.000 & 0.000 & 0.000 & 0.298 (toward OVB) & toward OVB $\\checkmark$ \\\\\nExposure & Treatment & 0.850 & 0.834 & 0.141 & 2.83$\\times$ amplification & toward null $\\checkmark$ \\\\\nMediation & Mediator & 0.520 & 0.470 & 0.110 & 1.62$\\times$ + sign reversal & toward null $\\checkmark$ \\\\\nCollider & Collider & 0.410 & 0.360 & 0.090 & spurious 0.44 from null & attenuated $\\checkmark$ \\\\\nM-bias & M-bias var. & 0.000 & 0.000 & 0.000 & 0.18 (attenuated) & attenuated $\\checkmark$ \\\\\nInstrument & Instrument & 0.000 & 0.000 & 0.000 & ratio distortion 0.14 & attenuated $\\checkmark$ \\\\\nFront-door & Front-door var. & 0.340 & 0.280 & 0.120 & sign reversal & toward null $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Theory--MC match by topology $\\times$ confusion matrix structure ($K\\!=\\!3$, $N\\!=\\!10{,}000$, 1000 reps). $\\checkmark$: within 95\\% MC CI. $\\triangle^*$: boundary case resolved at $N\\!=\\!50{,}000$.}\n\\label{tab:theory-mc}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccccc}\n\\toprule\nTopology & Diag.-dom. & Mod.~off-diag & Unif.~off-diag & Block-diag & Near-perm. & Rank-def. & Match \\\\\n\\midrule\nConfounding & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nMediation   & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nCollider    & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nM-bias      & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nInstrument  & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nFront-door  & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\triangle^*$ & 5/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{General K: Matrix-Form Expressions and Interpretability Tools}\n\\label{sec:generalk}\n\nFor $K \\ge 5$, the bias $\\bB(\\bC)$ is a matrix-valued function whose entries are not individually interpretable.\nWe develop three tools to make these expressions actionable.\n\n\\paragraph{Eigendecomposition summary.}\nThe spectral decomposition of $\\bB$ reveals that the top-2 eigenvalues capture 87\\% of bias variance and the top-3 capture 96\\% (averaged over topologies and $K$ values; Table~\\ref{tab:eigendecomp}).\nThe first eigenvalue corresponds to the ``fidelity'' mode (baseline attenuation) and the second to the dominant misclassification direction.\n\n\\paragraph{Worst-case scalar bound.}\nThe spectral norm $\\|\\bB\\|_2$ provides a scalar upper bound on bias magnitude.\nThis bound has 88\\% tightness---in 88\\% of scenarios it is within 15\\% of the true worst-case bias.\n\n\\paragraph{Scaling with $K$.}\nAs $K$ increases, the violation rate rises monotonically: mediation goes from 0.52 ($K\\!=\\!3$) to 0.61 ($K\\!=\\!5$) to 0.68 ($K\\!=\\!7$); collider from 0.41 to 0.49 to 0.55 (Table~\\ref{tab:violation-scaling}).\nConfounding remains at zero regardless of $K$.\nTheory--MC match rates are 17/18 for $K\\!=\\!5$ and 16/18 for $K\\!=\\!7$; the 2 unmatched cases at $K\\!=\\!7$ are near-permutation extremes that converge at $N\\!=\\!50{,}000$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Violation rate scaling with $K$.}\n\\label{tab:violation-scaling}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & $K\\!=\\!3$ & $K\\!=\\!5$ & $K\\!=\\!7$ & Trend \\\\\n\\midrule\nConfounding & 0.000 & 0.000 & 0.000 & Stable at 0 \\\\\nMediation   & 0.520 & 0.610 & 0.680 & Monotonically increasing \\\\\nCollider    & 0.410 & 0.490 & 0.550 & Monotonically increasing \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Eigendecomposition variance explained by top eigenvalues of the bias matrix.}\n\\label{tab:eigendecomp}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTopology & $K$ & Top-1 & Top-2 & Top-3 \\\\\n\\midrule\nConfounding & 5 & 72\\% & 89\\% & 97\\% \\\\\nConfounding & 7 & 68\\% & 85\\% & 95\\% \\\\\nMediation   & 5 & 70\\% & 87\\% & 96\\% \\\\\nMediation   & 7 & 65\\% & 84\\% & 94\\% \\\\\nCollider    & 5 & 71\\% & 88\\% & 96\\% \\\\\nCollider    & 7 & 66\\% & 85\\% & 95\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Binarization Collapse Analysis}\n\\label{sec:binarization}\n\nA natural practitioner response to the multi-class reversal result is: ``binarize the variable to recover the binary guarantee.''\nWe show this strategy is hazardous.\nFor each of 7 topologies (6 canonical + exposure) at $K\\!=\\!3{,}5{,}7$, we compute the additional bias $\\Delta$ introduced by collapsing $K$ categories to 2.\n\nThe maximum $\\Delta$ is 0.19 (mediation, $K\\!=\\!7$), which is large enough to reverse substantive conclusions in typical CSS studies where effect sizes are 0.1--0.3.\nAverage $\\Delta$ increases monotonically with $K$: 0.08 ($K\\!=\\!3$), 0.13 ($K\\!=\\!5$), 0.16 ($K\\!=\\!7$).\nIn 12\\% of $K\\!=\\!5{,}7$ scenarios, $\\Delta$ itself flips the bias direction---making the binarized estimate worse than the multi-class estimate.\nTable~\\ref{tab:binarization} reports the full results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binarization collapse $\\Delta$ by topology $\\times$ $K$. Direction reversal indicates cases where binarization flips the bias direction.}\n\\label{tab:binarization}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nTopology & $K\\!=\\!3$ $\\Delta$ & $K\\!=\\!5$ $\\Delta$ & $K\\!=\\!7$ $\\Delta$ & Max $\\Delta$ & Direction Reversal? \\\\\n\\midrule\nConfounding & 0.06 & 0.09 & 0.11 & 0.11 & No \\\\\nExposure    & 0.08 & 0.12 & 0.15 & 0.15 & Yes (3\\% of $K\\!=\\!7$) \\\\\nMediation   & 0.10 & 0.15 & 0.19 & 0.19 & Yes (18\\% of $K\\!=\\!7$) \\\\\nCollider    & 0.09 & 0.14 & 0.17 & 0.17 & Yes (14\\% of $K\\!=\\!7$) \\\\\nM-bias      & 0.05 & 0.08 & 0.10 & 0.10 & No \\\\\nInstrument  & 0.04 & 0.07 & 0.09 & 0.09 & No \\\\\nFront-door  & 0.09 & 0.13 & 0.16 & 0.16 & Yes (11\\% of $K\\!=\\!7$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n%% ============================================================\n%% 4  ANNOTATION SENSITIVITY VALUES\n%% ============================================================\n\\section{Annotation Sensitivity Values}\n\\label{sec:asv}\n\n\\subsection{Definition}\n\n\\begin{definition}[Annotation Sensitivity Value]\nGiven a DAG topology $\\mathcal{G}$, a reference confusion matrix $\\bC_0$, and a downstream estimate $\\hat\\theta$, the ASV at threshold $\\theta_0$ is\n\\[\n\\text{ASV}(\\hat\\theta, \\theta_0, \\bC_0, \\mathcal{G}) = \\inf\\!\\big\\{\\delta > 0 : \\exists\\, \\bC \\text{ with } \\|\\bC - \\bC_0\\|_F \\le g(\\delta),\\; B(\\bC, \\mathcal{G}) \\text{ overturns } \\hat\\theta \\text{ past } \\theta_0 \\big\\},\n\\]\nwhere $g(\\delta)$ maps the amplification factor $\\delta$ to the Frobenius perturbation radius of the confusion matrix.\n\\end{definition}\n\nASVs are reported alongside effect estimates, analogous to E-values for unmeasured confounding.\nAn ASV of 1.5 means that annotation error only 50\\% larger than the estimated confusion matrix would suffice to overturn the conclusion.\nAn ASV $>\\!3$ indicates a robust conclusion.\n\n\\subsection{Formal Proofs for Priority Topologies}\n\nWe prove two properties for three priority topologies:\n\n\\begin{theorem}[Monotonicity]\nFor $\\mathcal{G} \\in \\{\\text{confounding, mediation, collider}\\}$, $\\text{ASV}(\\delta)$ is monotonically non-decreasing in $\\delta$.\n\\end{theorem}\n\n\\begin{theorem}[Sharpness]\nFor each $\\delta > 0$ and $\\mathcal{G} \\in \\{\\text{confounding, mediation, collider}\\}$, there exists an explicit $\\bC^*(\\delta)$ achieving the ASV bound.\n\\end{theorem}\n\nThe proof techniques are topology-specific.\n\\textbf{Confounding}: algebraic---ASV is a closed-form function of the spectral gap of $\\bC$ and $\\delta$.\n\\textbf{Mediation}: algebraic combined with the envelope theorem---the indirect effect ASV decomposes via the product of coefficients.\n\\textbf{Collider}: Lagrangian optimization with KKT conditions over the $\\bC$ perturbation space.\nAll three proofs are constructive: they provide explicit $\\bC^*$ matrices achieving the bound in 100\\% of tested scenarios.\n\n\\subsection{MC Validation}\n\nWe validate ASV coverage via 1000 scenarios $\\times$ 500 MC replications per scenario.\nTable~\\ref{tab:asv-coverage} reports coverage at nominal 90\\%, 95\\%, and 99\\% levels.\nAverage coverage at 95\\% nominal is 95.2\\%, indicating slight conservative over-coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV coverage calibration (1000 MC scenarios, 500 reps each).}\n\\label{tab:asv-coverage}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nTopology & Nom.~90\\% & Act.~90\\% & Nom.~95\\% & Act.~95\\% & Nom.~99\\% & Act.~99\\% \\\\\n\\midrule\nConfounding & 90\\% & 91.8\\% & 95\\% & 95.8\\% & 99\\% & 99.2\\% \\\\\nMediation   & 90\\% & 90.9\\% & 95\\% & 94.9\\% & 99\\% & 98.7\\% \\\\\nCollider    & 90\\% & 90.8\\% & 95\\% & 94.8\\% & 99\\% & 98.5\\% \\\\\nAverage     & 90\\% & 91.2\\% & 95\\% & 95.2\\% & 99\\% & 98.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Remaining Topologies: MC-Validated Conjectures}\n\nFor M-bias, instrument, and front-door topologies, we derive ASV expressions and validate them via MC simulation, but report sharpness as conjectures rather than formal proofs due to algebraic complexity.\n\n\\begin{conjecture}\nThe ASV bounds for M-bias, instrument, and front-door topologies are sharp.\n\\end{conjecture}\n\nEvidence: MC validation shows zero monotonicity violations across 1000 scenarios for all three topologies, and the numerical sharpness gap is $<\\!0.008$ (Table~\\ref{tab:asv-remaining}).\nFront-door ASV involves joint perturbation of a two-stage estimator; a closed-form sharpness proof requires solving a bilinear constrained optimization, which we identify as immediate future work.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV validation for remaining topologies (1000 MC scenarios).}\n\\label{tab:asv-remaining}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Monotonicity & Coverage @95\\% & Sharpness Gap & Status \\\\\n\\midrule\nM-bias     & $\\checkmark$ (0 violations) & 95.4\\% & 0.006 & Conjecture \\\\\nInstrument & $\\checkmark$ (0 violations) & 96.1\\% & 0.005 & Conjecture \\\\\nFront-door & $\\checkmark$ (0 violations) & 94.3\\% & 0.008 & Conjecture \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5  CORRECTION GUIDANCE FRAMEWORK\n%% ============================================================\n\\section{Correction Guidance Framework}\n\\label{sec:correction}\n\nWe construct a principled decision framework: given \\{topology $\\times$ confusion matrix structure $\\times$ ASV\\}, the framework recommends the correction method that minimizes residual bias.\nCandidate methods include: matrix-based likelihood adjustment (MLA), prediction-powered inference (PPI), double-sampling likelihood (DSL), and naive plug-in.\nThe framework also identifies regimes where no existing method suffices.\n\n\\subsection{MC Validation}\n\nWe test the framework across 432 scenarios: 6 topologies $\\times$ 6 confusion matrix structures $\\times$ 3 $K$ values $\\times$ 4 effect sizes.\nThe framework recommends the optimal method in 411/432 scenarios (95.0\\% accuracy).\nTable~\\ref{tab:correction-distribution} reports the recommendation distribution, and Table~\\ref{tab:correction-accuracy} reports accuracy by topology.\n\nAmong the 21 non-optimal recommendations, 14 are cases where MLA and PPI perform within 0.005 of each other (the recommendation is arbitrary), and 7 are extreme-$\\bC$ + small-$N$ cases where all methods are unstable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Correction method recommendation distribution across 432 MC scenarios.}\n\\label{tab:correction-distribution}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & \\% Scenarios & Typical Condition & Avg Bias Reduction \\\\\n\\midrule\nMLA & 31\\% & $\\bC$ known, $K\\!\\le\\!5$, non-differential & 72\\% \\\\\nPPI & 24\\% & $\\bC$ uncertain, gold-standard available & 65\\% \\\\\nDSL & 18\\% & Confounding, high diag.~dominance & 58\\% \\\\\nNaive plug-in & 12\\% & ASV $>\\!5.0$ (robust) & N/A (unnecessary) \\\\\nNo adequate method & 15\\% & Correlated errors + differential + collider/front-door & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Framework accuracy by topology (432 scenarios total, 72 per topology).}\n\\label{tab:correction-accuracy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Scenarios & Correct & Accuracy & Most Common Failure \\\\\n\\midrule\nConfounding & 72 & 71 & 98.6\\% & MLA $\\approx$ PPI \\\\\nMediation   & 72 & 69 & 95.8\\% & Extreme $\\bC$ + small $N$ \\\\\nCollider    & 72 & 67 & 93.1\\% & MLA $\\approx$ PPI + extreme $\\bC$ \\\\\nM-bias      & 72 & 70 & 97.2\\% & Rare edge case \\\\\nInstrument  & 72 & 69 & 95.8\\% & Wald ratio instability \\\\\nFront-door  & 72 & 65 & 90.3\\% & Two-stage complexity \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 15\\% of scenarios classified as ``no adequate method'' occur primarily under correlated multi-LLM errors combined with differential $K\\!\\ge\\!5$ misclassification in collider or front-door topologies.\nWe identify dependence-aware multi-LLM correction as the most important open problem in this space, directly motivated by the findings of \\citet{kim2025}.\n\n\n%% ============================================================\n%% 6  EMPIRICAL VALIDATION\n%% ============================================================\n\\section{Empirical Validation}\n\\label{sec:empirical}\n\n\\subsection{LLM Annotation Setup}\n\nWe collect empirical confusion matrices from three LLMs---Llama~4 Maverick, Qwen~3.5 Plus, and DeepSeek~V4---on three CSS annotation tasks:\n(1)~protest event coding ($K\\!=\\!5$: peaceful protest, violent protest, strategic development, government response, other),\n(2)~stance detection ($K\\!=\\!3$: favor, against, neutral), and\n(3)~toxicity detection ($K\\!=\\!2$: toxic, non-toxic).\nEach model annotates ${\\sim}30$K instances per task across 3 prompt variants, yielding ${\\sim}270$K total annotations.\nTable~\\ref{tab:empirical-C} summarizes the confusion matrix characteristics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrix summary (${\\sim}270$K annotations).}\n\\label{tab:empirical-C}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccccl}\n\\toprule\nTask & $K$ & Model & Accuracy & Diag.~Dom. & Largest Off-Diag & $\\bC$ Structure \\\\\n\\midrule\nProtest & 5 & Llama 4 Maverick & 0.64 & 0.60 & 0.18 (strat\\_dev$\\to$peaceful) & Moderate off-diag \\\\\nProtest & 5 & Qwen 3.5 Plus    & 0.60 & 0.57 & 0.21 (strat\\_dev$\\to$peaceful) & Near-permutation \\\\\nProtest & 5 & DeepSeek V4       & 0.67 & 0.63 & 0.15 (other$\\to$gov\\_resp)     & Block-diagonal \\\\\nStance  & 3 & Llama 4 Maverick & 0.77 & 0.76 & 0.14 (neutral$\\to$against) & Block-diagonal \\\\\nStance  & 3 & Qwen 3.5 Plus    & 0.73 & 0.72 & 0.16 (against$\\to$neutral) & Block-diagonal \\\\\nStance  & 3 & DeepSeek V4       & 0.76 & 0.75 & 0.13 (neutral$\\to$against) & Block-diagonal \\\\\nToxicity& 2 & Llama 4 Maverick & 0.91 & 0.91 & 0.09 (toxic$\\to$non-toxic) & Diagonal-dominant \\\\\nToxicity& 2 & Qwen 3.5 Plus    & 0.87 & 0.87 & 0.13 (non-toxic$\\to$toxic) & Diagonal-dominant \\\\\nToxicity& 2 & DeepSeek V4       & 0.90 & 0.90 & 0.10 (toxic$\\to$non-toxic) & Diagonal-dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{Inter-Model Error Correlation}\n\nTable~\\ref{tab:inter-model} reports inter-model agreement.\nThe average same-direction error rate is 58\\%, consistent with the 60\\% reported by \\citet{kim2025}.\nThis confirms that multi-LLM ensembles cannot eliminate systematic annotation bias---errors are correlated because LLMs share similar pre-training data and reasoning patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inter-model error agreement.}\n\\label{tab:inter-model}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTask & Model Pair & Cohen's $\\kappa$ & Error Agree. & Same-Dir. \\\\\n\\midrule\nProtest & Llama--Qwen     & 0.69 & 0.24 & 0.61 \\\\\nProtest & Llama--DeepSeek  & 0.72 & 0.21 & 0.57 \\\\\nProtest & Qwen--DeepSeek   & 0.68 & 0.25 & 0.56 \\\\\nStance  & Llama--Qwen     & 0.67 & 0.18 & 0.59 \\\\\nStance  & Llama--DeepSeek  & 0.70 & 0.16 & 0.58 \\\\\nStance  & Qwen--DeepSeek   & 0.66 & 0.19 & 0.57 \\\\\nToxicity& All pairs avg   & 0.76 & 0.09 & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{ASV Calibration on Empirical Data}\n\nWe apply the ASV framework to the empirical confusion matrices, placing each task in three topological contexts (mediation, collider, confounding or instrument as appropriate) and computing ASVs.\nTable~\\ref{tab:asv-concordance} reports concordance between ASV-based model rankings and actual bias severity rankings.\nASV ranking agrees with actual bias ranking in 8/9 scenarios.\nThe single discordant case (protest $\\times$ instrument, DeepSeek vs.\\ Qwen) involves a difference of only 0.02, within the noise margin of Wald ratio estimation.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV concordance with empirical bias severity (9 scenarios).}\n\\label{tab:asv-concordance}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llllc}\n\\toprule\nTask & Context & ASV Ranking & Actual Bias Ranking & Concordant \\\\\n\\midrule\nProtest  & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nProtest  & Collider    & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nProtest  & Instrument  & DeepSeek $<$ Qwen $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\\times$ {\\scriptsize(0.02)} \\\\\nStance   & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nStance   & Collider    & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\\checkmark$ \\\\\nStance   & Confounding & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\\checkmark$ \\\\\nToxicity & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nToxicity & Collider    & Qwen $<$ DeepSeek $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\\checkmark$ \\\\\nToxicity & Confounding & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nTable~\\ref{tab:asv-robustness} classifies each scenario by ASV-based robustness.\nProtest event coding in mediation and collider contexts is flagged as \\textsc{fragile} (ASV $<\\!1.5$), with Qwen~3.5 Plus reaching ASV $=\\!0.9$ in the mediation context---meaning even modest additional annotation error would overturn the downstream conclusion.\nBoth empirical scenarios where $\\bC$ falls in the theoretical reversal zone are correctly flagged by ASV $<\\!1.5$.\nHeld-out gold-standard coverage at the 95\\% nominal level is 94\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV robustness classification across empirical scenarios.}\n\\label{tab:asv-robustness}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccl}\n\\toprule\nTask & Context & Best ASV & Worst ASV & Classification \\\\\n\\midrule\nProtest  & Mediation   & 2.1 (DeepSeek) & 0.9 (Qwen) & \\textsc{Fragile} \\\\\nProtest  & Collider    & 1.8 (DeepSeek) & 1.1 (Qwen) & \\textsc{Fragile} \\\\\nProtest  & Instrument  & 3.2 (Llama)    & 2.4 (DeepSeek) & Moderate \\\\\nStance   & Mediation   & 4.1 (DeepSeek) & 2.8 (Qwen) & Robust \\\\\nStance   & Collider    & 3.8 (DeepSeek) & 2.5 (Llama) & Moderate \\\\\nStance   & Confounding & 5.2 (DeepSeek) & 3.9 (Llama) & Robust \\\\\nToxicity & Mediation   & 7.3 (Llama)    & 5.1 (Qwen) & Robust \\\\\nToxicity & Collider    & 6.8 (Llama)    & 4.9 (Qwen) & Robust \\\\\nToxicity & Confounding & 8.1 (DeepSeek) & 6.2 (Qwen) & Robust \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{Correction Framework on Empirical Data}\n\nOn the 9 empirical scenarios, the correction guidance framework recommends the method producing $\\ge\\!40\\%$ bias reduction in 8/9 cases.\nThe single exception (protest $\\times$ collider $\\times$ Qwen) is correctly classified as ``no adequate method''---the near-permutation confusion matrix combined with high inter-model error correlation places this scenario outside the range of current correction approaches.\n\n\n%% ============================================================\n%% 7  PATHOLOGICAL CONFUSION MATRIX ANALYSIS\n%% ============================================================\n\\section{Structural Diagnostics for Confusion Matrices}\n\\label{sec:diagnostics}\n\nTo provide practitioners with actionable early-warning indicators, we analyze which properties of $\\bC$ predict bias severity.\n\n\\paragraph{Spectral gap.}\nThe spectral gap $(1 - \\lambda_2/\\lambda_1)$ of $\\bC$ explains 83\\% of bias magnitude variance ($R^2 = 0.83$, $r = -0.91$).\nA spectral gap below 0.15 predicts catastrophic bias ($>\\!2\\times$ effect size) in $\\ge\\!80\\%$ of reversal-prone topologies.\n\n\\paragraph{Diagonal dominance ratio.}\nThe diagonal dominance ratio has $R^2 = 0.76$ ($r = -0.87$).\nA ratio below 0.55 signals high risk.\n\n\\paragraph{Two-number diagnostic.}\nWe propose a practitioner-facing two-number summary: (spectral gap, diagonal dominance ratio) $\\to$ risk category \\{low, medium, high, catastrophic\\}.\nThe joint model achieves $R^2 = 0.89$.\nTable~\\ref{tab:structural-predictors} reports all structural predictors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural predictors of bias severity.}\n\\label{tab:structural-predictors}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nPredictor & $r$ with $|$Bias$|$ & $R^2$ & Catastrophic Threshold \\\\\n\\midrule\nSpectral gap $(1-\\lambda_2/\\lambda_1)$ & $-0.91$ & 0.83 & $<\\!0.15$ \\\\\nDiagonal dominance ratio & $-0.87$ & 0.76 & $<\\!0.55$ \\\\\nCondition number of $\\bC$ & $+0.89$ & 0.79 & $>\\!12$ \\\\\nMin diagonal element     & $-0.84$ & 0.71 & $<\\!0.3$ \\\\\nSpectral gap + diag.~dom.~(joint) & --- & 0.89 & Combined \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNear-permutation confusion matrices (spectral gap $<\\!0.05$) produce reversal in all structural-distortion topologies with severity $1.5$--$3\\times$.\nRank-deficient matrices produce catastrophic bias regardless of topology.\nBlock-diagonal matrices exhibit direction-dependent behavior: reversal is guaranteed when classes with opposite effects are merged within the same block.\n\nIn the empirical data, the spectral gap diagnostic for Qwen~3.5 Plus on protest coding under certain prompt variants falls below 0.15, consistent with the ASV $<\\!1.0$ fragile classification in \\S\\ref{sec:empirical}.\n\n\n%% ============================================================\n%% 8  TOOLKIT\n%% ============================================================\n\\section{The \\texttt{annot-sensitivity} Toolkit}\n\\label{sec:toolkit}\n\nWe release \\texttt{annot-sensitivity}, a pip-installable Python package implementing the full framework.\nThe API surface consists of three functions corresponding to the three contributions:\n\\begin{itemize}\n    \\item \\texttt{bias\\_expression(dag, C, K)}: returns the closed-form or matrix-form bias expression for the specified topology.\n    \\item \\texttt{asv\\_bound(dag, C, estimate, threshold)}: computes the ASV and the constructive $\\bC^*$ achieving the bound.\n    \\item \\texttt{recommend\\_correction(dag, C, asv, n\\_gold)}: recommends the appropriate correction method.\n\\end{itemize}\n\nThe package supports $K = 2$--$20$, all 6 topologies, and runs in $<\\!1$s for $K\\!\\le\\!7$.\nDependencies are minimal (NumPy, SciPy, Matplotlib).\nSix topology-specific Jupyter notebook tutorials are included.\nTest coverage exceeds 90\\%.\n\n\n%% ============================================================\n%% 9  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe have shown that multi-class annotation errors interact with DAG topology in ways that break classical binary guarantees.\nFour of six canonical topologies exhibit direction-reversing bias under non-differential $K\\!\\ge\\!3$ misclassification, and binarization is not a safe escape.\nOur three contributions---the bias taxonomy, ASV sensitivity analysis, and correction guidance framework---provide the diagnostic layer that has been missing from the LLM annotation pipeline.\n\n\\paragraph{Limitations.}\nASV sharpness is formally proved for only three topologies; the remaining three are supported by strong numerical evidence.\nThe correction framework achieves 90.3\\% accuracy on the front-door topology, the lowest among all topologies.\nThe 15\\% of scenarios where no existing correction method is adequate---primarily involving correlated multi-LLM errors---remain an open problem.\nOur empirical validation covers three CSS tasks; broader coverage across domains (e.g., biomedical NLP) is left to future work.\n\n\\paragraph{Future directions.}\nFormal sharpness proofs for the remaining three topologies (particularly front-door, which requires solving bilinear constrained optimization).\nDependence-aware multi-LLM correction methods that account for the 58\\% cross-model error correlation we observe.\nExtension to differential misclassification, where the error process depends on other variables in the DAG.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Baumann et~al.(2025)]{baumann2025}\nBaumann, L., et~al. (2025).\n\\newblock Auditing LLM annotations in computational social science.\n\\newblock \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[Brenner(1993)]{brenner1993}\nBrenner, H. (1993).\n\\newblock Bias due to non-differential misclassification of polytomous confounders.\n\\newblock \\emph{Journal of Clinical Epidemiology}, 46(1):57--63.\n\n\\bibitem[Bross(1954)]{bross1954}\nBross, I.~D. (1954).\n\\newblock Misclassification in 2$\\times$2 tables.\n\\newblock \\emph{Biometrics}, 10(4):478--486.\n\n\\bibitem[Hern{\\'a}n and Cole(2009)]{hernan2009}\nHern{\\'a}n, M.~A. and Cole, S.~R. (2009).\n\\newblock Invited commentary: Causal diagrams and measurement bias.\n\\newblock \\emph{American Journal of Epidemiology}, 170(8):959--964.\n\n\\bibitem[Jerzak et~al.(2025)]{jerzak2025}\nJerzak, C.~T., et~al. (2025).\n\\newblock Benchmarking correction methods for LLM annotation errors.\n\\newblock \\emph{Proceedings of EMNLP 2025}.\n\n\\bibitem[Kim et~al.(2025)]{kim2025}\nKim, S., et~al. (2025).\n\\newblock Correlated errors in multi-LLM annotation pipelines.\n\\newblock \\emph{Proceedings of ICML 2025}.\n\n\\bibitem[Lee and Wood-Doughty(2024)]{lee2024}\nLee, S. and Wood-Doughty, Z. (2024).\n\\newblock Categorical annotation errors in causal inference with LLM classifiers.\n\\newblock \\emph{Proceedings of EMNLP 2024}.\n\n\\bibitem[TeBlunthuis et~al.(2024)]{teblunthuis2024}\nTeBlunthuis, N., et~al. (2024).\n\\newblock Measurement error correction for binary text classifiers in causal inference.\n\\newblock \\emph{Proceedings of NAACL 2024}.\n\n\\bibitem[VanderWeele and Ding(2017)]{vanderweele2017}\nVanderWeele, T.~J. and Ding, P. (2017).\n\\newblock Sensitivity analysis in observational research: Introducing the E-value.\n\\newblock \\emph{Annals of Internal Medicine}, 167(4):268--274.\n\n\\bibitem[VanderWeele and Li(2019)]{vanderweele2019}\nVanderWeele, T.~J. and Li, Y. (2019).\n\\newblock Simple sensitivity analysis for differential measurement error.\n\\newblock \\emph{American Journal of Epidemiology}, 188(10):1823--1829.\n\n\\bibitem[Wood-Doughty et~al.(2018)]{wooddoughty2018}\nWood-Doughty, Z., et~al. (2018).\n\\newblock Challenges of using text classifiers for causal inference.\n\\newblock \\emph{Proceedings of EMNLP 2018}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "992f0e7a-5447-4a78-b7a1-230e9ae3238b",
  "isSidechain": false,
  "requestId": "req_011CbDVyfe473kDYLgRwtQ9Y",
  "type": "assistant",
  "uuid": "16df5c5f-932f-4b2a-86b5-08c9073b8814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGCLcovBC8GPgdnw9p7MN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 608,
      "cache_read_input_tokens": 47224,
      "output_tokens": 14366,
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
          "output_tokens": 14366,
          "cache_read_input_tokens": 47224,
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

_source line 21 · 2026-05-20T08:28:48.668Z_

<details><summary>↩ Tool result · `toolu_01Pmgki35CFeU9zcTNr1hDFW`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16df5c5f-932f-4b2a-86b5-08c9073b8814",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "ef4f4626-63fd-421e-9ec1-099a1156d1c9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{adjustbox}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{corollary}{Corollary}\n\\newtheorem{definition}{Definition}\n\\newtheorem{conjecture}{Conjecture}\n\n\\newcommand{\\bC}{\\mathbf{C}}\n\\newcommand{\\bI}{\\mathbf{I}}\n\\newcommand{\\bB}{\\mathbf{B}}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge language models (LLMs) are rapidly replacing human annotators in computational social science, yet recent audits show that 31\\% of downstream causal conclusions drawn from LLM-annotated data are incorrect.\nWe show that the classical guarantee---non-differential misclassification biases toward the null---breaks when annotated variables have $K\\!\\ge\\!3$ categories.\nThe bias behavior is \\emph{topology-dependent}: the same confusion matrix that produces innocuous residual bias in a confounding DAG can produce direction-reversing bias in mediation or collider DAGs.\nWe make three contributions.\n\\textbf{(1)}~A \\emph{multi-class bias taxonomy}: closed-form bias expressions for $K\\!=\\!3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$, across six canonical DAG topologies.\nFour of six topologies (exposure, mediation, collider, front-door) exhibit direction reversal under non-differential $K\\!\\ge\\!3$ error; confounding and instrument topologies preserve monotonicity.\n\\textbf{(2)}~\\emph{Annotation Sensitivity Values} (ASVs), analogous to E-values for unmeasured confounding, that quantify how much annotation error is needed to overturn a conclusion.\nWe prove monotonicity and sharpness for three priority topologies and provide MC-validated conjectures for the remaining three.\n\\textbf{(3)}~A \\emph{correction guidance framework} mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to the appropriate correction method, achieving 95\\% recommendation accuracy across 432 simulated scenarios and validated on three CSS tasks annotated by three LLMs (${\\sim}270$K annotations).\nBinarizing a $K$-class variable to retreat into the binary safe zone is itself hazardous: collapsing $K\\!=\\!7$ to binary introduces up to $\\Delta\\!=\\!0.19$ additional bias, with 12\\% of scenarios exhibiting direction reversal from binarization alone.\nWe release \\texttt{annot-sensitivity}, an open-source Python toolkit implementing the full framework.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLMs have become the default annotation engine in computational social science (CSS).\nTheir speed and cost advantages are undeniable, but measurement error in LLM annotations propagates into downstream causal estimates.\n\\citet{baumann2025} audit this pipeline and find that 31\\% of downstream conclusions are already incorrect.\n\\citet{kim2025} show that cross-model annotation errors are highly correlated---when two LLMs both err, 60\\% of the time they err toward the same category---meaning multi-model ensembles cannot eliminate systematic bias.\n\nThe classical measurement-error literature provides reassurance for the binary case: non-differential misclassification of a binary exposure biases toward the null \\citep{bross1954}.\nPractitioners routinely extend this guarantee to multi-class variables by binarizing: collapsing $K$-class annotations into two categories before analysis.\nWe show that both the original guarantee and the binarization escape route fail for $K\\!\\ge\\!3$.\n\n\\paragraph{Core finding.}\nNon-differential $K\\!\\ge\\!3$ misclassification breaks the toward-null guarantee in 4 of 6 canonical DAG topologies.\nThe reversal pattern is strictly topology-dependent: the same confusion matrix that is benign in the confounding topology produces direction-reversing bias in mediation and collider topologies.\nIn our Monte Carlo experiments, the mediation topology exhibits a 52\\% violation rate (47\\% sign reversal), the collider topology 41\\% (36\\% sign reversal), the front-door topology 34\\% (28\\% sign reversal), and the exposure topology 85\\% (83.4\\% sign reversal) under 100K random confusion matrices.\nConfounding and instrument topologies maintain zero violations.\n\n\\paragraph{Why binarization is not a safe retreat.}\nCollapsing a $K$-class variable to binary discards inter-category bias structure.\nWe show that binarization introduces additional bias up to $\\Delta\\!=\\!0.19$ (mediation, $K\\!=\\!7$), and in 12\\% of $K\\!=\\!5{,}7$ scenarios the binarization itself flips the bias direction---making the collapsed estimate \\emph{worse} than the multi-class estimate.\n\n\\paragraph{Contributions.}\n\\textbf{(1)}~A multi-class bias taxonomy with closed-form and matrix-form bias expressions across six DAG topologies (\\S\\ref{sec:taxonomy}).\n\\textbf{(2)}~Annotation Sensitivity Values (ASVs) with formal monotonicity and sharpness proofs for three topologies and MC-validated conjectures for three more (\\S\\ref{sec:asv}).\n\\textbf{(3)}~A correction guidance framework achieving 95\\% recommendation accuracy (\\S\\ref{sec:correction}).\nWe validate all results on empirical confusion matrices from three LLMs across three CSS tasks (\\S\\ref{sec:empirical}) and release the \\texttt{annot-sensitivity} Python toolkit.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error in causal inference.}\nThe epidemiological literature on exposure misclassification dates to \\citet{bross1954}, with \\citet{brenner1993} first noting that polytomous confounder misclassification can bias in either direction.\n\\citet{vanderweele2019} provide sensitivity bounds for binary risk ratios.\nNone of these works provide systematic multi-class bias expressions across multiple DAG topologies.\n\n\\paragraph{Annotation error in NLP/CSS.}\n\\citet{wooddoughty2018} apply DAG reasoning to text classifier errors but produce no formal bias theorems and are limited to binary variables.\n\\citet{teblunthuis2024} provide the most complete binary treatment with MLA correction but are limited to $K\\!=\\!2$ and a single classifier.\n\\citet{lee2024} extend to categorical variables and LLM classifiers but cover only one DAG topology (unobserved confounding) on one dataset, with no systematic taxonomy or sensitivity analysis.\n\\citet{jerzak2025} benchmark correction methods but treat annotation error as monolithic---if different confusion matrix structures produce qualitatively different bias in different topologies, unconditional benchmarking is itself misleading.\n\n\\paragraph{Sensitivity analysis.}\nE-values \\citep{vanderweele2017} quantify robustness to unmeasured confounding via a single scalar.\nOur ASVs serve an analogous role for annotation error but require a reference confusion matrix and amplification direction, reflecting the richer parameterization of $K\\!\\times\\!K$ error structures.\n\n\n%% ============================================================\n%% 3  MULTI-CLASS BIAS TAXONOMY\n%% ============================================================\n\\section{Multi-Class Bias Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Setup and Notation}\n\nLet $\\tilde{V}$ denote the observed (LLM-annotated) version of a $K$-class variable $V$.\nThe misclassification process is characterized by the $K\\!\\times\\!K$ confusion matrix $\\bC$, where $C_{jk} = P(\\tilde{V}=k \\mid V=j)$.\nNon-differential misclassification requires $P(\\tilde{V} \\mid V, \\text{other variables}) = P(\\tilde{V} \\mid V)$, i.e., the error depends only on the true value.\nWe consider six canonical DAG topologies where $V$ plays distinct structural roles: confounder, treatment (exposure), mediator, collider, instrument, and front-door criterion variable.\n\nFor $K\\!=\\!3$, we derive closed-form bias expressions as functions of $\\bC$ and the structural parameters of each DAG.\nFor general $K$, we provide matrix-form expressions and develop three interpretability tools: (a) eigendecomposition summaries, (b) worst-case scalar bounds, and (c) spectral diagnostic indicators.\n\n\\subsection{Closed-Form Bias Expressions (K=3)}\n\\label{sec:kthree}\n\nFor each topology, we derive the bias $B(\\bC) = \\hat{\\theta}(\\tilde{V}) - \\theta^*(V)$ as a function of $\\bC$ and the true structural parameters.\nThe derivation proceeds by expressing the observed conditional distributions in terms of the true distributions and $\\bC$, then computing the resulting distortion in the estimand.\n\n\\paragraph{Validation.}\nWe validate all closed-form expressions via Monte Carlo simulation: 6 confusion matrix structures $\\times$ 6 topologies $\\times$ 1000 replications at $N\\!=\\!10{,}000$.\nThe theory-MC match rate is 97.2\\% (35/36 structure$\\times$topology combinations fall within 95\\% MC confidence intervals).\nThe single boundary case---front-door with rank-deficient $\\bC$---shows a discrepancy of 0.003 above the CI upper bound, which resolves at $N\\!=\\!50{,}000$.\nTable~\\ref{tab:theory-mc} reports the full match matrix.\n\n\\subsection{Topology-Dependent Reversal}\n\\label{sec:reversal}\n\nWe execute a 100K random $\\bC$ search for each topology, testing whether the bias violates the classical toward-null guarantee.\nThe topologies separate cleanly into two classes:\n\n\\begin{itemize}\n    \\item \\textbf{Information-loss topologies} (confounding, instrument, M-bias): misclassification only reduces the variable's information content; bias direction is predictable. Violation rate = 0 across all three.\n    \\item \\textbf{Structural-distortion topologies} (exposure, mediation, collider, front-door): misclassification alters the variable's functional role in the DAG, producing unpredictable direction reversal.\n\\end{itemize}\n\nTable~\\ref{tab:topology-reversal} reports the complete reversal analysis.\nThe exposure topology exhibits the highest violation rate (85.0\\%) because misclassification acts directly on the treatment variable.\nThe mediation topology (52.0\\%) is next: a near-permutation $\\bC$ that swaps adjacent category labels effectively flips the sign of $\\beta_{MY|X}$, reversing the indirect effect.\nWorst-case severity reaches $1.62\\times$ amplification with sign reversal in mediation, and spurious effect creation of 0.44 from a null truth in the collider topology.\n\n\\begin{table}[t]\n\\centering\n\\caption{Topology $\\times$ reversal summary under 100K random confusion matrices ($K\\!=\\!3$).}\n\\label{tab:topology-reversal}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lcccccc}\n\\toprule\nTopology & Role & Violation & Sign Rev. & Amplif. & Worst-Case & $K\\!=\\!2$ \\\\\n\\midrule\nConfounding & Confounder & 0.000 & 0.000 & 0.000 & 0.298 (toward OVB) & toward OVB $\\checkmark$ \\\\\nExposure & Treatment & 0.850 & 0.834 & 0.141 & 2.83$\\times$ amplification & toward null $\\checkmark$ \\\\\nMediation & Mediator & 0.520 & 0.470 & 0.110 & 1.62$\\times$ + sign reversal & toward null $\\checkmark$ \\\\\nCollider & Collider & 0.410 & 0.360 & 0.090 & spurious 0.44 from null & attenuated $\\checkmark$ \\\\\nM-bias & M-bias var. & 0.000 & 0.000 & 0.000 & 0.18 (attenuated) & attenuated $\\checkmark$ \\\\\nInstrument & Instrument & 0.000 & 0.000 & 0.000 & ratio distortion 0.14 & attenuated $\\checkmark$ \\\\\nFront-door & Front-door var. & 0.340 & 0.280 & 0.120 & sign reversal & toward null $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Theory--MC match by topology $\\times$ confusion matrix structure ($K\\!=\\!3$, $N\\!=\\!10{,}000$, 1000 reps). $\\checkmark$: within 95\\% MC CI. $\\triangle^*$: boundary case resolved at $N\\!=\\!50{,}000$.}\n\\label{tab:theory-mc}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccccc}\n\\toprule\nTopology & Diag.-dom. & Mod.~off-diag & Unif.~off-diag & Block-diag & Near-perm. & Rank-def. & Match \\\\\n\\midrule\nConfounding & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nMediation   & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nCollider    & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nM-bias      & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nInstrument  & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & 6/6 \\\\\nFront-door  & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\checkmark$ & $\\triangle^*$ & 5/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{General K: Matrix-Form Expressions and Interpretability Tools}\n\\label{sec:generalk}\n\nFor $K \\ge 5$, the bias $\\bB(\\bC)$ is a matrix-valued function whose entries are not individually interpretable.\nWe develop three tools to make these expressions actionable.\n\n\\paragraph{Eigendecomposition summary.}\nThe spectral decomposition of $\\bB$ reveals that the top-2 eigenvalues capture 87\\% of bias variance and the top-3 capture 96\\% (averaged over topologies and $K$ values; Table~\\ref{tab:eigendecomp}).\nThe first eigenvalue corresponds to the ``fidelity'' mode (baseline attenuation) and the second to the dominant misclassification direction.\n\n\\paragraph{Worst-case scalar bound.}\nThe spectral norm $\\|\\bB\\|_2$ provides a scalar upper bound on bias magnitude.\nThis bound has 88\\% tightness---in 88\\% of scenarios it is within 15\\% of the true worst-case bias.\n\n\\paragraph{Scaling with $K$.}\nAs $K$ increases, the violation rate rises monotonically: mediation goes from 0.52 ($K\\!=\\!3$) to 0.61 ($K\\!=\\!5$) to 0.68 ($K\\!=\\!7$); collider from 0.41 to 0.49 to 0.55 (Table~\\ref{tab:violation-scaling}).\nConfounding remains at zero regardless of $K$.\nTheory--MC match rates are 17/18 for $K\\!=\\!5$ and 16/18 for $K\\!=\\!7$; the 2 unmatched cases at $K\\!=\\!7$ are near-permutation extremes that converge at $N\\!=\\!50{,}000$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Violation rate scaling with $K$.}\n\\label{tab:violation-scaling}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & $K\\!=\\!3$ & $K\\!=\\!5$ & $K\\!=\\!7$ & Trend \\\\\n\\midrule\nConfounding & 0.000 & 0.000 & 0.000 & Stable at 0 \\\\\nMediation   & 0.520 & 0.610 & 0.680 & Monotonically increasing \\\\\nCollider    & 0.410 & 0.490 & 0.550 & Monotonically increasing \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Eigendecomposition variance explained by top eigenvalues of the bias matrix.}\n\\label{tab:eigendecomp}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTopology & $K$ & Top-1 & Top-2 & Top-3 \\\\\n\\midrule\nConfounding & 5 & 72\\% & 89\\% & 97\\% \\\\\nConfounding & 7 & 68\\% & 85\\% & 95\\% \\\\\nMediation   & 5 & 70\\% & 87\\% & 96\\% \\\\\nMediation   & 7 & 65\\% & 84\\% & 94\\% \\\\\nCollider    & 5 & 71\\% & 88\\% & 96\\% \\\\\nCollider    & 7 & 66\\% & 85\\% & 95\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Binarization Collapse Analysis}\n\\label{sec:binarization}\n\nA natural practitioner response to the multi-class reversal result is: ``binarize the variable to recover the binary guarantee.''\nWe show this strategy is hazardous.\nFor each of 7 topologies (6 canonical + exposure) at $K\\!=\\!3{,}5{,}7$, we compute the additional bias $\\Delta$ introduced by collapsing $K$ categories to 2.\n\nThe maximum $\\Delta$ is 0.19 (mediation, $K\\!=\\!7$), which is large enough to reverse substantive conclusions in typical CSS studies where effect sizes are 0.1--0.3.\nAverage $\\Delta$ increases monotonically with $K$: 0.08 ($K\\!=\\!3$), 0.13 ($K\\!=\\!5$), 0.16 ($K\\!=\\!7$).\nIn 12\\% of $K\\!=\\!5{,}7$ scenarios, $\\Delta$ itself flips the bias direction---making the binarized estimate worse than the multi-class estimate.\nTable~\\ref{tab:binarization} reports the full results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binarization collapse $\\Delta$ by topology $\\times$ $K$. Direction reversal indicates cases where binarization flips the bias direction.}\n\\label{tab:binarization}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lccccc}\n\\toprule\nTopology & $K\\!=\\!3$ $\\Delta$ & $K\\!=\\!5$ $\\Delta$ & $K\\!=\\!7$ $\\Delta$ & Max $\\Delta$ & Direction Reversal? \\\\\n\\midrule\nConfounding & 0.06 & 0.09 & 0.11 & 0.11 & No \\\\\nExposure    & 0.08 & 0.12 & 0.15 & 0.15 & Yes (3\\% of $K\\!=\\!7$) \\\\\nMediation   & 0.10 & 0.15 & 0.19 & 0.19 & Yes (18\\% of $K\\!=\\!7$) \\\\\nCollider    & 0.09 & 0.14 & 0.17 & 0.17 & Yes (14\\% of $K\\!=\\!7$) \\\\\nM-bias      & 0.05 & 0.08 & 0.10 & 0.10 & No \\\\\nInstrument  & 0.04 & 0.07 & 0.09 & 0.09 & No \\\\\nFront-door  & 0.09 & 0.13 & 0.16 & 0.16 & Yes (11\\% of $K\\!=\\!7$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n%% ============================================================\n%% 4  ANNOTATION SENSITIVITY VALUES\n%% ============================================================\n\\section{Annotation Sensitivity Values}\n\\label{sec:asv}\n\n\\subsection{Definition}\n\n\\begin{definition}[Annotation Sensitivity Value]\nGiven a DAG topology $\\mathcal{G}$, a reference confusion matrix $\\bC_0$, and a downstream estimate $\\hat\\theta$, the ASV at threshold $\\theta_0$ is\n\\[\n\\text{ASV}(\\hat\\theta, \\theta_0, \\bC_0, \\mathcal{G}) = \\inf\\!\\big\\{\\delta > 0 : \\exists\\, \\bC \\text{ with } \\|\\bC - \\bC_0\\|_F \\le g(\\delta),\\; B(\\bC, \\mathcal{G}) \\text{ overturns } \\hat\\theta \\text{ past } \\theta_0 \\big\\},\n\\]\nwhere $g(\\delta)$ maps the amplification factor $\\delta$ to the Frobenius perturbation radius of the confusion matrix.\n\\end{definition}\n\nASVs are reported alongside effect estimates, analogous to E-values for unmeasured confounding.\nAn ASV of 1.5 means that annotation error only 50\\% larger than the estimated confusion matrix would suffice to overturn the conclusion.\nAn ASV $>\\!3$ indicates a robust conclusion.\n\n\\subsection{Formal Proofs for Priority Topologies}\n\nWe prove two properties for three priority topologies:\n\n\\begin{theorem}[Monotonicity]\nFor $\\mathcal{G} \\in \\{\\text{confounding, mediation, collider}\\}$, $\\text{ASV}(\\delta)$ is monotonically non-decreasing in $\\delta$.\n\\end{theorem}\n\n\\begin{theorem}[Sharpness]\nFor each $\\delta > 0$ and $\\mathcal{G} \\in \\{\\text{confounding, mediation, collider}\\}$, there exists an explicit $\\bC^*(\\delta)$ achieving the ASV bound.\n\\end{theorem}\n\nThe proof techniques are topology-specific.\n\\textbf{Confounding}: algebraic---ASV is a closed-form function of the spectral gap of $\\bC$ and $\\delta$.\n\\textbf{Mediation}: algebraic combined with the envelope theorem---the indirect effect ASV decomposes via the product of coefficients.\n\\textbf{Collider}: Lagrangian optimization with KKT conditions over the $\\bC$ perturbation space.\nAll three proofs are constructive: they provide explicit $\\bC^*$ matrices achieving the bound in 100\\% of tested scenarios.\n\n\\subsection{MC Validation}\n\nWe validate ASV coverage via 1000 scenarios $\\times$ 500 MC replications per scenario.\nTable~\\ref{tab:asv-coverage} reports coverage at nominal 90\\%, 95\\%, and 99\\% levels.\nAverage coverage at 95\\% nominal is 95.2\\%, indicating slight conservative over-coverage.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV coverage calibration (1000 MC scenarios, 500 reps each).}\n\\label{tab:asv-coverage}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nTopology & Nom.~90\\% & Act.~90\\% & Nom.~95\\% & Act.~95\\% & Nom.~99\\% & Act.~99\\% \\\\\n\\midrule\nConfounding & 90\\% & 91.8\\% & 95\\% & 95.8\\% & 99\\% & 99.2\\% \\\\\nMediation   & 90\\% & 90.9\\% & 95\\% & 94.9\\% & 99\\% & 98.7\\% \\\\\nCollider    & 90\\% & 90.8\\% & 95\\% & 94.8\\% & 99\\% & 98.5\\% \\\\\nAverage     & 90\\% & 91.2\\% & 95\\% & 95.2\\% & 99\\% & 98.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Remaining Topologies: MC-Validated Conjectures}\n\nFor M-bias, instrument, and front-door topologies, we derive ASV expressions and validate them via MC simulation, but report sharpness as conjectures rather than formal proofs due to algebraic complexity.\n\n\\begin{conjecture}\nThe ASV bounds for M-bias, instrument, and front-door topologies are sharp.\n\\end{conjecture}\n\nEvidence: MC validation shows zero monotonicity violations across 1000 scenarios for all three topologies, and the numerical sharpness gap is $<\\!0.008$ (Table~\\ref{tab:asv-remaining}).\nFront-door ASV involves joint perturbation of a two-stage estimator; a closed-form sharpness proof requires solving a bilinear constrained optimization, which we identify as immediate future work.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV validation for remaining topologies (1000 MC scenarios).}\n\\label{tab:asv-remaining}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Monotonicity & Coverage @95\\% & Sharpness Gap & Status \\\\\n\\midrule\nM-bias     & $\\checkmark$ (0 violations) & 95.4\\% & 0.006 & Conjecture \\\\\nInstrument & $\\checkmark$ (0 violations) & 96.1\\% & 0.005 & Conjecture \\\\\nFront-door & $\\checkmark$ (0 violations) & 94.3\\% & 0.008 & Conjecture \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%% ============================================================\n%% 5  CORRECTION GUIDANCE FRAMEWORK\n%% ============================================================\n\\section{Correction Guidance Framework}\n\\label{sec:correction}\n\nWe construct a principled decision framework: given \\{topology $\\times$ confusion matrix structure $\\times$ ASV\\}, the framework recommends the correction method that minimizes residual bias.\nCandidate methods include: matrix-based likelihood adjustment (MLA), prediction-powered inference (PPI), double-sampling likelihood (DSL), and naive plug-in.\nThe framework also identifies regimes where no existing method suffices.\n\n\\subsection{MC Validation}\n\nWe test the framework across 432 scenarios: 6 topologies $\\times$ 6 confusion matrix structures $\\times$ 3 $K$ values $\\times$ 4 effect sizes.\nThe framework recommends the optimal method in 411/432 scenarios (95.0\\% accuracy).\nTable~\\ref{tab:correction-distribution} reports the recommendation distribution, and Table~\\ref{tab:correction-accuracy} reports accuracy by topology.\n\nAmong the 21 non-optimal recommendations, 14 are cases where MLA and PPI perform within 0.005 of each other (the recommendation is arbitrary), and 7 are extreme-$\\bC$ + small-$N$ cases where all methods are unstable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Correction method recommendation distribution across 432 MC scenarios.}\n\\label{tab:correction-distribution}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & \\% Scenarios & Typical Condition & Avg Bias Reduction \\\\\n\\midrule\nMLA & 31\\% & $\\bC$ known, $K\\!\\le\\!5$, non-differential & 72\\% \\\\\nPPI & 24\\% & $\\bC$ uncertain, gold-standard available & 65\\% \\\\\nDSL & 18\\% & Confounding, high diag.~dominance & 58\\% \\\\\nNaive plug-in & 12\\% & ASV $>\\!5.0$ (robust) & N/A (unnecessary) \\\\\nNo adequate method & 15\\% & Correlated errors + differential + collider/front-door & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Framework accuracy by topology (432 scenarios total, 72 per topology).}\n\\label{tab:correction-accuracy}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Scenarios & Correct & Accuracy & Most Common Failure \\\\\n\\midrule\nConfounding & 72 & 71 & 98.6\\% & MLA $\\approx$ PPI \\\\\nMediation   & 72 & 69 & 95.8\\% & Extreme $\\bC$ + small $N$ \\\\\nCollider    & 72 & 67 & 93.1\\% & MLA $\\approx$ PPI + extreme $\\bC$ \\\\\nM-bias      & 72 & 70 & 97.2\\% & Rare edge case \\\\\nInstrument  & 72 & 69 & 95.8\\% & Wald ratio instability \\\\\nFront-door  & 72 & 65 & 90.3\\% & Two-stage complexity \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 15\\% of scenarios classified as ``no adequate method'' occur primarily under correlated multi-LLM errors combined with differential $K\\!\\ge\\!5$ misclassification in collider or front-door topologies.\nWe identify dependence-aware multi-LLM correction as the most important open problem in this space, directly motivated by the findings of \\citet{kim2025}.\n\n\n%% ============================================================\n%% 6  EMPIRICAL VALIDATION\n%% ============================================================\n\\section{Empirical Validation}\n\\label{sec:empirical}\n\n\\subsection{LLM Annotation Setup}\n\nWe collect empirical confusion matrices from three LLMs---Llama~4 Maverick, Qwen~3.5 Plus, and DeepSeek~V4---on three CSS annotation tasks:\n(1)~protest event coding ($K\\!=\\!5$: peaceful protest, violent protest, strategic development, government response, other),\n(2)~stance detection ($K\\!=\\!3$: favor, against, neutral), and\n(3)~toxicity detection ($K\\!=\\!2$: toxic, non-toxic).\nEach model annotates ${\\sim}30$K instances per task across 3 prompt variants, yielding ${\\sim}270$K total annotations.\nTable~\\ref{tab:empirical-C} summarizes the confusion matrix characteristics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrix summary (${\\sim}270$K annotations).}\n\\label{tab:empirical-C}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccccl}\n\\toprule\nTask & $K$ & Model & Accuracy & Diag.~Dom. & Largest Off-Diag & $\\bC$ Structure \\\\\n\\midrule\nProtest & 5 & Llama 4 Maverick & 0.64 & 0.60 & 0.18 (strat\\_dev$\\to$peaceful) & Moderate off-diag \\\\\nProtest & 5 & Qwen 3.5 Plus    & 0.60 & 0.57 & 0.21 (strat\\_dev$\\to$peaceful) & Near-permutation \\\\\nProtest & 5 & DeepSeek V4       & 0.67 & 0.63 & 0.15 (other$\\to$gov\\_resp)     & Block-diagonal \\\\\nStance  & 3 & Llama 4 Maverick & 0.77 & 0.76 & 0.14 (neutral$\\to$against) & Block-diagonal \\\\\nStance  & 3 & Qwen 3.5 Plus    & 0.73 & 0.72 & 0.16 (against$\\to$neutral) & Block-diagonal \\\\\nStance  & 3 & DeepSeek V4       & 0.76 & 0.75 & 0.13 (neutral$\\to$against) & Block-diagonal \\\\\nToxicity& 2 & Llama 4 Maverick & 0.91 & 0.91 & 0.09 (toxic$\\to$non-toxic) & Diagonal-dominant \\\\\nToxicity& 2 & Qwen 3.5 Plus    & 0.87 & 0.87 & 0.13 (non-toxic$\\to$toxic) & Diagonal-dominant \\\\\nToxicity& 2 & DeepSeek V4       & 0.90 & 0.90 & 0.10 (toxic$\\to$non-toxic) & Diagonal-dominant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{Inter-Model Error Correlation}\n\nTable~\\ref{tab:inter-model} reports inter-model agreement.\nThe average same-direction error rate is 58\\%, consistent with the 60\\% reported by \\citet{kim2025}.\nThis confirms that multi-LLM ensembles cannot eliminate systematic annotation bias---errors are correlated because LLMs share similar pre-training data and reasoning patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inter-model error agreement.}\n\\label{tab:inter-model}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTask & Model Pair & Cohen's $\\kappa$ & Error Agree. & Same-Dir. \\\\\n\\midrule\nProtest & Llama--Qwen     & 0.69 & 0.24 & 0.61 \\\\\nProtest & Llama--DeepSeek  & 0.72 & 0.21 & 0.57 \\\\\nProtest & Qwen--DeepSeek   & 0.68 & 0.25 & 0.56 \\\\\nStance  & Llama--Qwen     & 0.67 & 0.18 & 0.59 \\\\\nStance  & Llama--DeepSeek  & 0.70 & 0.16 & 0.58 \\\\\nStance  & Qwen--DeepSeek   & 0.66 & 0.19 & 0.57 \\\\\nToxicity& All pairs avg   & 0.76 & 0.09 & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{ASV Calibration on Empirical Data}\n\nWe apply the ASV framework to the empirical confusion matrices, placing each task in three topological contexts (mediation, collider, confounding or instrument as appropriate) and computing ASVs.\nTable~\\ref{tab:asv-concordance} reports concordance between ASV-based model rankings and actual bias severity rankings.\nASV ranking agrees with actual bias ranking in 8/9 scenarios.\nThe single discordant case (protest $\\times$ instrument, DeepSeek vs.\\ Qwen) involves a difference of only 0.02, within the noise margin of Wald ratio estimation.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV concordance with empirical bias severity (9 scenarios).}\n\\label{tab:asv-concordance}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llllc}\n\\toprule\nTask & Context & ASV Ranking & Actual Bias Ranking & Concordant \\\\\n\\midrule\nProtest  & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nProtest  & Collider    & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nProtest  & Instrument  & DeepSeek $<$ Qwen $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\\times$ {\\scriptsize(0.02)} \\\\\nStance   & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nStance   & Collider    & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\\checkmark$ \\\\\nStance   & Confounding & Llama $<$ Qwen $<$ DeepSeek & Llama $<$ Qwen $<$ DeepSeek & $\\checkmark$ \\\\\nToxicity & Mediation   & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\nToxicity & Collider    & Qwen $<$ DeepSeek $<$ Llama & Qwen $<$ DeepSeek $<$ Llama & $\\checkmark$ \\\\\nToxicity & Confounding & Qwen $<$ Llama $<$ DeepSeek & Qwen $<$ Llama $<$ DeepSeek & $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\nTable~\\ref{tab:asv-robustness} classifies each scenario by ASV-based robustness.\nProtest event coding in mediation and collider contexts is flagged as \\textsc{fragile} (ASV $<\\!1.5$), with Qwen~3.5 Plus reaching ASV $=\\!0.9$ in the mediation context---meaning even modest additional annotation error would overturn the downstream conclusion.\nBoth empirical scenarios where $\\bC$ falls in the theoretical reversal zone are correctly flagged by ASV $<\\!1.5$.\nHeld-out gold-standard coverage at the 95\\% nominal level is 94\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV robustness classification across empirical scenarios.}\n\\label{tab:asv-robustness}\n\\small\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{llccl}\n\\toprule\nTask & Context & Best ASV & Worst ASV & Classification \\\\\n\\midrule\nProtest  & Mediation   & 2.1 (DeepSeek) & 0.9 (Qwen) & \\textsc{Fragile} \\\\\nProtest  & Collider    & 1.8 (DeepSeek) & 1.1 (Qwen) & \\textsc{Fragile} \\\\\nProtest  & Instrument  & 3.2 (Llama)    & 2.4 (DeepSeek) & Moderate \\\\\nStance   & Mediation   & 4.1 (DeepSeek) & 2.8 (Qwen) & Robust \\\\\nStance   & Collider    & 3.8 (DeepSeek) & 2.5 (Llama) & Moderate \\\\\nStance   & Confounding & 5.2 (DeepSeek) & 3.9 (Llama) & Robust \\\\\nToxicity & Mediation   & 7.3 (Llama)    & 5.1 (Qwen) & Robust \\\\\nToxicity & Collider    & 6.8 (Llama)    & 4.9 (Qwen) & Robust \\\\\nToxicity & Confounding & 8.1 (DeepSeek) & 6.2 (Qwen) & Robust \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table}\n\n\n\\subsection{Correction Framework on Empirical Data}\n\nOn the 9 empirical scenarios, the correction guidance framework recommends the method producing $\\ge\\!40\\%$ bias reduction in 8/9 cases.\nThe single exception (protest $\\times$ collider $\\times$ Qwen) is correctly classified as ``no adequate method''---the near-permutation confusion matrix combined with high inter-model error correlation places this scenario outside the range of current correction approaches.\n\n\n%% ============================================================\n%% 7  PATHOLOGICAL CONFUSION MATRIX ANALYSIS\n%% ============================================================\n\\section{Structural Diagnostics for Confusion Matrices}\n\\label{sec:diagnostics}\n\nTo provide practitioners with actionable early-warning indicators, we analyze which properties of $\\bC$ predict bias severity.\n\n\\paragraph{Spectral gap.}\nThe spectral gap $(1 - \\lambda_2/\\lambda_1)$ of $\\bC$ explains 83\\% of bias magnitude variance ($R^2 = 0.83$, $r = -0.91$).\nA spectral gap below 0.15 predicts catastrophic bias ($>\\!2\\times$ effect size) in $\\ge\\!80\\%$ of reversal-prone topologies.\n\n\\paragraph{Diagonal dominance ratio.}\nThe diagonal dominance ratio has $R^2 = 0.76$ ($r = -0.87$).\nA ratio below 0.55 signals high risk.\n\n\\paragraph{Two-number diagnostic.}\nWe propose a practitioner-facing two-number summary: (spectral gap, diagonal dominance ratio) $\\to$ risk category \\{low, medium, high, catastrophic\\}.\nThe joint model achieves $R^2 = 0.89$.\nTable~\\ref{tab:structural-predictors} reports all structural predictors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural predictors of bias severity.}\n\\label{tab:structural-predictors}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nPredictor & $r$ with $|$Bias$|$ & $R^2$ & Catastrophic Threshold \\\\\n\\midrule\nSpectral gap $(1-\\lambda_2/\\lambda_1)$ & $-0.91$ & 0.83 & $<\\!0.15$ \\\\\nDiagonal dominance ratio & $-0.87$ & 0.76 & $<\\!0.55$ \\\\\nCondition number of $\\bC$ & $+0.89$ & 0.79 & $>\\!12$ \\\\\nMin diagonal element     & $-0.84$ & 0.71 & $<\\!0.3$ \\\\\nSpectral gap + diag.~dom.~(joint) & --- & 0.89 & Combined \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNear-permutation confusion matrices (spectral gap $<\\!0.05$) produce reversal in all structural-distortion topologies with severity $1.5$--$3\\times$.\nRank-deficient matrices produce catastrophic bias regardless of topology.\nBlock-diagonal matrices exhibit direction-dependent behavior: reversal is guaranteed when classes with opposite effects are merged within the same block.\n\nIn the empirical data, the spectral gap diagnostic for Qwen~3.5 Plus on protest coding under certain prompt variants falls below 0.15, consistent with the ASV $<\\!1.0$ fragile classification in \\S\\ref{sec:empirical}.\n\n\n%% ============================================================\n%% 8  TOOLKIT\n%% ============================================================\n\\section{The \\texttt{annot-sensitivity} Toolkit}\n\\label{sec:toolkit}\n\nWe release \\texttt{annot-sensitivity}, a pip-installable Python package implementing the full framework.\nThe API surface consists of three functions corresponding to the three contributions:\n\\begin{itemize}\n    \\item \\texttt{bias\\_expression(dag, C, K)}: returns the closed-form or matrix-form bias expression for the specified topology.\n    \\item \\texttt{asv\\_bound(dag, C, estimate, threshold)}: computes the ASV and the constructive $\\bC^*$ achieving the bound.\n    \\item \\texttt{recommend\\_correction(dag, C, asv, n\\_gold)}: recommends the appropriate correction method.\n\\end{itemize}\n\nThe package supports $K = 2$--$20$, all 6 topologies, and runs in $<\\!1$s for $K\\!\\le\\!7$.\nDependencies are minimal (NumPy, SciPy, Matplotlib).\nSix topology-specific Jupyter notebook tutorials are included.\nTest coverage exceeds 90\\%.\n\n\n%% ============================================================\n%% 9  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe have shown that multi-class annotation errors interact with DAG topology in ways that break classical binary guarantees.\nFour of six canonical topologies exhibit direction-reversing bias under non-differential $K\\!\\ge\\!3$ misclassification, and binarization is not a safe escape.\nOur three contributions---the bias taxonomy, ASV sensitivity analysis, and correction guidance framework---provide the diagnostic layer that has been missing from the LLM annotation pipeline.\n\n\\paragraph{Limitations.}\nASV sharpness is formally proved for only three topologies; the remaining three are supported by strong numerical evidence.\nThe correction framework achieves 90.3\\% accuracy on the front-door topology, the lowest among all topologies.\nThe 15\\% of scenarios where no existing correction method is adequate---primarily involving correlated multi-LLM errors---remain an open problem.\nOur empirical validation covers three CSS tasks; broader coverage across domains (e.g., biomedical NLP) is left to future work.\n\n\\paragraph{Future directions.}\nFormal sharpness proofs for the remaining three topologies (particularly front-door, which requires solving bilinear constrained optimization).\nDependence-aware multi-LLM correction methods that account for the 58\\% cross-model error correlation we observe.\nExtension to differential misclassification, where the error process depends on other variables in the DAG.\n\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Baumann et~al.(2025)]{baumann2025}\nBaumann, L., et~al. (2025).\n\\newblock Auditing LLM annotations in computational social science.\n\\newblock \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[Brenner(1993)]{brenner1993}\nBrenner, H. (1993).\n\\newblock Bias due to non-differential misclassification of polytomous confounders.\n\\newblock \\emph{Journal of Clinical Epidemiology}, 46(1):57--63.\n\n\\bibitem[Bross(1954)]{bross1954}\nBross, I.~D. (1954).\n\\newblock Misclassification in 2$\\times$2 tables.\n\\newblock \\emph{Biometrics}, 10(4):478--486.\n\n\\bibitem[Hern{\\'a}n and Cole(2009)]{hernan2009}\nHern{\\'a}n, M.~A. and Cole, S.~R. (2009).\n\\newblock Invited commentary: Causal diagrams and measurement bias.\n\\newblock \\emph{American Journal of Epidemiology}, 170(8):959--964.\n\n\\bibitem[Jerzak et~al.(2025)]{jerzak2025}\nJerzak, C.~T., et~al. (2025).\n\\newblock Benchmarking correction methods for LLM annotation errors.\n\\newblock \\emph{Proceedings of EMNLP 2025}.\n\n\\bibitem[Kim et~al.(2025)]{kim2025}\nKim, S., et~al. (2025).\n\\newblock Correlated errors in multi-LLM annotation pipelines.\n\\newblock \\emph{Proceedings of ICML 2025}.\n\n\\bibitem[Lee and Wood-Doughty(2024)]{lee2024}\nLee, S. and Wood-Doughty, Z. (2024).\n\\newblock Categorical annotation errors in causal inference with LLM classifiers.\n\\newblock \\emph{Proceedings of EMNLP 2024}.\n\n\\bibitem[TeBlunthuis et~al.(2024)]{teblunthuis2024}\nTeBlunthuis, N., et~al. (2024).\n\\newblock Measurement error correction for binary text classifiers in causal inference.\n\\newblock \\emph{Proceedings of NAACL 2024}.\n\n\\bibitem[VanderWeele and Ding(2017)]{vanderweele2017}\nVanderWeele, T.~J. and Ding, P. (2017).\n\\newblock Sensitivity analysis in observational research: Introducing the E-value.\n\\newblock \\emph{Annals of Internal Medicine}, 167(4):268--274.\n\n\\bibitem[VanderWeele and Li(2019)]{vanderweele2019}\nVanderWeele, T.~J. and Li, Y. (2019).\n\\newblock Simple sensitivity analysis for differential measurement error.\n\\newblock \\emph{American Journal of Epidemiology}, 188(10):1823--1829.\n\n\\bibitem[Wood-Doughty et~al.(2018)]{wooddoughty2018}\nWood-Doughty, Z., et~al. (2018).\n\\newblock Challenges of using text classifiers for causal inference.\n\\newblock \\emph{Proceedings of EMNLP 2018}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "16df5c5f-932f-4b2a-86b5-08c9073b8814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attri…",
  "leafUuid": "ef4f4626-63fd-421e-9ec1-099a1156d1c9",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate causal annotation error attribution paper",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Assistant

_source line 24 · 2026-05-20T08:28:52.685Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef4f4626-63fd-421e-9ec1-099a1156d1c9",
  "isSidechain": false,
  "requestId": "req_011CbDWHqKUagwjdkjHvp6tb",
  "type": "assistant",
  "uuid": "f08bd178-d946-425a-8ba6-2888b1f07980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXLtyXzDx9ZDdjEWkLLsua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14428,
      "cache_read_input_tokens": 47832,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 47832,
          "cache_creation_input_tokens": 14428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14428
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

_source line 25 · 2026-05-20T08:28:53.774Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XNvv9Crn5styhkeeFgDxv5`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08bd178-d946-425a-8ba6-2888b1f07980",
  "isSidechain": false,
  "requestId": "req_011CbDWHqKUagwjdkjHvp6tb",
  "type": "assistant",
  "uuid": "c0cb77b0-4e1d-4b0c-a6b8-deaff7c94380",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXLtyXzDx9ZDdjEWkLLsua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14428,
      "cache_read_input_tokens": 47832,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 47832,
          "cache_creation_input_tokens": 14428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14428
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

_source line 26 · 2026-05-20T08:29:04.233Z_

<details><summary>↩ Tool result · `toolu_01XNvv9Crn5styhkeeFgDxv5`</summary>

```text
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.0972pt)
Font metrics written on ecrm1728.tfm.
Output written on ecrm1728.600gf (256 characters, 84608 bytes).
Transcript written on ecrm1728.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728
.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy
mbols/msam10.pfb>
Output written on paper.pdf (11 pages, 289787 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0cb77b0-4e1d-4b0c-a6b8-deaff7c94380",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "09b9b1d5-56a2-48c8-9718-1005d9d57893",
  "toolUseResult": {
    "stdout": "(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0972pt)\nFont metrics written on ecrm1728.tfm.\nOutput written on ecrm1728.600gf (256 characters, 84608 bytes).\nTranscript written on ecrm1728.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728\n.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy\nmbols/msam10.pfb>\nOutput written on paper.pdf (11 pages, 289787 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c0cb77b0-4e1d-4b0c-a6b8-deaff7c94380",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T08:29:08.927Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U9qCJWH6g7JbbMpZzdbYon`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b9b1d5-56a2-48c8-9718-1005d9d57893",
  "isSidechain": false,
  "requestId": "req_011CbDWJypySHNQjiEb4fAAn",
  "type": "assistant",
  "uuid": "3eff8c9b-e99d-415a-9f7a-3fdc201c93e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U78jRf3pmBSwnuJeKRNJov",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 62260,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1107,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 62260,
          "cache_creation_input_tokens": 1107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1107
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

_source line 28 · 2026-05-20T08:29:09.569Z_

<details><summary>↩ Tool result · `toolu_01U9qCJWH6g7JbbMpZzdbYon`</summary>

```text
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy
mbols/msam10.pfb>
Output written on paper.pdf (11 pages, 293442 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eff8c9b-e99d-415a-9f7a-3fdc201c93e2",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "d66538ce-fa36-4e75-a4b4-f49baeb04a1a",
  "toolUseResult": {
    "stdout": "/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy\nmbols/msam10.pfb>\nOutput written on paper.pdf (11 pages, 293442 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3eff8c9b-e99d-415a-9f7a-3fdc201c93e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T08:29:09.572Z_

```json
{
  "parentUuid": "d66538ce-fa36-4e75-a4b4-f49baeb04a1a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "18f50704-ce80-46c6-9366-560baa10fc3e",
  "timestamp": "2026-05-20T08:29:09.572Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-20T08:29:12.849Z_

Let me verify no errors in the log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f50704-ce80-46c6-9366-560baa10fc3e",
  "isSidechain": false,
  "requestId": "req_011CbDWKNdAn8UJ6uM3jV887",
  "type": "assistant",
  "uuid": "cadfd379-6861-499b-b1bf-2f90ce324dfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfwmVNZpBVEPDjPBZe9wPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 63367,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 63367,
          "cache_creation_input_tokens": 551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 551
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

_source line 31 · 2026-05-20T08:29:14.624Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WPn38wQYBqPKgHodVnzNbH`</summary>

```json
{
  "command": "grep -c \"^!\" paper.log && grep -c \"Warning.*undefined\" paper.log && ls -la paper.pdf",
  "description": "Check for LaTeX errors and warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cadfd379-6861-499b-b1bf-2f90ce324dfc",
  "isSidechain": false,
  "requestId": "req_011CbDWKNdAn8UJ6uM3jV887",
  "type": "assistant",
  "uuid": "2c28b289-7704-4275-a4be-44da598c3f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfwmVNZpBVEPDjPBZe9wPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 63367,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 63367,
          "cache_creation_input_tokens": 551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 551
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

_source line 32 · 2026-05-20T08:29:14.688Z_

<details><summary>↩ Tool result · reported error · `toolu_01WPn38wQYBqPKgHodVnzNbH`</summary>

```text
Exit code 1
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c28b289-7704-4275-a4be-44da598c3f26",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "7c9babc2-d471-4567-9521-f48d1bf2d520",
  "toolUseResult": "Error: Exit code 1\n0",
  "sourceToolAssistantUUID": "2c28b289-7704-4275-a4be-44da598c3f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T08:29:18.266Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YRNNacLWbtrMh7o5huFJZ5`</summary>

```json
{
  "command": "grep \"^!\" paper.log; grep \"Warning.*undefined\" paper.log; ls -la paper.pdf",
  "description": "Check for errors/warnings and PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9babc2-d471-4567-9521-f48d1bf2d520",
  "isSidechain": false,
  "requestId": "req_011CbDWKkoRNmWuNcC6kkJmH",
  "type": "assistant",
  "uuid": "fcceb148-702d-4868-b6a7-f93ac802170b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ER5SvyhVrvrGZt3EvnxKHy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 138,
      "cache_read_input_tokens": 63918,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 63918,
          "cache_creation_input_tokens": 138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 138
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

_source line 34 · 2026-05-20T08:29:18.329Z_

<details><summary>↩ Tool result · `toolu_01YRNNacLWbtrMh7o5huFJZ5`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 293442 May 20 08:29 paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcceb148-702d-4868-b6a7-f93ac802170b",
  "isSidechain": false,
  "promptId": "f7e2070c-a1f9-41d7-88fe-e756b557178b",
  "type": "user",
  "uuid": "03bff4fa-7d63-4708-acd8-905dc6b761ca",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 293442 May 20 08:29 paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fcceb148-702d-4868-b6a7-f93ac802170b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T08:29:35.059Z_

Zero errors, zero undefined references. PDF compiled cleanly at 293KB, 11 pages.

Paper written to `best/paper.tex` and compiled to `best/paper.pdf`. Structure:

- **Abstract** — all three claims + headline numbers
- **S1 Introduction** — problem statement, core finding (4/6 topologies reverse), binarization hazard, three contributions
- **S2 Related Work** — measurement error literature, NLP/CSS annotation error, sensitivity analysis
- **S3 Multi-Class Bias Taxonomy** — K=3 closed-form (Tables 1-2), topology-dependent reversal, general K with eigendecomposition (Tables 3-4), binarization collapse (Table 7)
- **S4 ASV** — definition, formal proofs for 3 topologies (Tables 8-9), MC-validated conjectures for 3 more (Table 10)
- **S5 Correction Guidance** — framework + 432-scenario validation (Tables 13-14)
- **S6 Empirical Validation** — 3 LLMs × 3 tasks (Tables 5-6), ASV calibration (Tables 11-12)
- **S7 Structural Diagnostics** — spectral gap/diagonal dominance predictors (Table 15)
- **S8 Toolkit** — `annot-sensitivity` package description
- **S9 Conclusion** — limitations + future work

All 15 tables from experiment_data.json are included. Every quantitative claim is sourced from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03bff4fa-7d63-4708-acd8-905dc6b761ca",
  "isSidechain": false,
  "requestId": "req_011CbDWLLcQAEKASXCTPboir",
  "type": "assistant",
  "uuid": "cd29c7f3-a09b-4256-ab66-24bed9f33621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nJWmwRf6NWyu15YwjmmJV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 139,
      "cache_read_input_tokens": 64056,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 368,
          "cache_read_input_tokens": 64056,
          "cache_creation_input_tokens": 139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 139
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attri…",
  "leafUuid": "cd29c7f3-a09b-4256-ab66-24bed9f33621",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate causal annotation error attribution paper",
  "sessionId": "91a9ab6d-de69-4f3c-8c74-05f4d04786ff"
}
```

---
