# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/5be00f43-c6bb-4c5c-8f78-8057dc303cf0.jsonl`
- **Structured JSON:** [`df71ae926fdded03de51.json`](../../sessions/df/df71ae926fdded03de51.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T16:30:22.242Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T16:30:22.242Z",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Layer hierarchy 无法作为 headline claim。5-model pooled layer gap 仅 ~4pp (p=0.14, n.s.)， 被 model×type interaction (p=0.008) 瓦解——type ranking 因模型架构而异 (GPT 系 spec>ling, Qwen3-8B 反转, Claude 混合)。Judge calibration 暴露 coreferential (F1=0.61) 和 auth_scope (F1=0.68) 的 type-specific measurement bias， 进一步削弱 type-level claims。Error analysis failure mode 跨层重叠 42%，无 clean mechanism 区分。 首选 reframe: (C) \"The Massive Binary Effect\" 为 primary——+30pp 仍是文献最大因果效应 + perturbation control PASS (Δ=4.2pp, ratio=0.13)；(B) \"Ambiguity Blindness\" 为 §6 核心—— 92% traces 中 agent 未识别歧义存在，universal across types and models。 C2 降级为 \"Model-Dependent Vulnerability Profiles\" (model×type interaction 从 nuisance 升级为 finding)； C3 layer claim 放弃。备选标题: \"Policy Ambiguity Causes Catastrophic Safety Violations in LLM Agents: A Causal Study\"。仍投 EMNLP——C1 (causal binary effect) + perturbation control + ambiguity blindness analysis = solid 3-contribution paper。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T16:30:22.245Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T16:30:22.245Z",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-20T16:30:22.265Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Layer hierarchy 无法作为 headline claim。5-model pooled layer gap 仅 ~4pp (p=0.14, n.s.)， 被 model×type interaction (p=0.008) 瓦解——type ranking 因模型架构而异 (GPT 系 spec>ling, Qwen3-8B 反转, Claude 混合)。Judge calibration 暴露 coreferential (F1=0.61) 和 auth_scope (F1=0.68) 的 type-specific measurement bias， 进一步削弱 type-level claims。Error analysis failure mode 跨层重叠 42%，无 clean mechanism 区分。 首选 reframe: (C) "The Massive Binary Effect" 为 primary——+30pp 仍是文献最大因果效应 + perturbation control PASS (Δ=4.2pp, ratio=0.13)；(B) "Ambiguity Blindness" 为 §6 核心—— 92% traces 中 agent 未识别歧义存在，universal across types and models。 C2 降级为 "Model-Dependent Vulnerability Profiles" (model×type interaction 从 nuisance 升级为 finding)； C3 layer claim 放弃。备选标题: "Policy Ambiguity Causes Catastrophic Safety Violations in LLM Agents: A Causal Study"。仍投 EMNLP——C1 (causal binary effect) + perturbation control + ambiguity blindness analysis = solid 3-contribution paper。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "4580b90b-0b30-45fe-b898-6da737f68142",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T16:30:22.264Z_

```json
{
  "parentUuid": "4580b90b-0b30-45fe-b898-6da737f68142",
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
  "uuid": "b303707c-5acd-486f-9104-b6a6e2a59a1c",
  "timestamp": "2026-05-20T16:30:22.264Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T16:30:22.264Z_

```json
{
  "parentUuid": "b303707c-5acd-486f-9104-b6a6e2a59a1c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4b105c15-85e3-4d51-ae2f-b084c5f06576",
  "timestamp": "2026-05-20T16:30:22.264Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
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
  "aiTitle": "Generate worst-tier simulation paper",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Assistant

_source line 7 · 2026-05-20T16:30:25.714Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b105c15-85e3-4d51-ae2f-b084c5f06576",
  "isSidechain": false,
  "requestId": "req_011CbE91i3XaFRN8P4ey98zj",
  "type": "assistant",
  "uuid": "ef4a6a34-fffd-494b-a126-4939d1b24e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb6JTGP3Hu4fT4ezNWEnmv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11937
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

_source line 8 · 2026-05-20T16:30:26.732Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GFyWuw7Z4vv7m3JzBUeabu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef4a6a34-fffd-494b-a126-4939d1b24e1e",
  "isSidechain": false,
  "requestId": "req_011CbE91i3XaFRN8P4ey98zj",
  "type": "assistant",
  "uuid": "cb13cd2a-2fc3-43e2-be33-3e2af4901fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb6JTGP3Hu4fT4ezNWEnmv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11937
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

_source line 9 · 2026-05-20T16:30:27.047Z_

<details><summary>↩ Tool result · `toolu_01GFyWuw7Z4vv7m3JzBUeabu`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\n",
5	    "results": {
6	      "total_pairs": 300,
7	      "pairs_per_type": 50,
8	      "cp_labeled_ratio": 0.5,
9	      "quality_pass_rate": 0.92,
10	      "avg_token_delta_amb_vs_unamb": 3.8,
11	      "coreferential_revision_rounds": 3,
12	      "auth_scope_revision_rounds": 2
13	    },
14	    "tables": [
15	      {
16	        "name": "Clause Pair Statistics by Type",
17	        "columns": [
18	          "type",
19	          "n_pairs",
20	          "avg_amb_tokens",
21	          "avg_unamb_tokens",
22	          "token_delta",
23	          "quality_pass_rate"
24	        ],
25	        "rows": [
26	          [
27	            "auth_scope",
28	            50,
29	            28.3,
30	            32.1,
31	            3.8,
32	            0.9
33	          ],
34	          [
35	            "incompleteness",
36	            50,
37	            26.7,
38	            30.5,
39	            3.8,
40	            0.94
41	          ],
42	          [
43	            "conditional_polysemy",
44	            50,
45	            24.2,
46	            25.8,
47	            1.6,
48	            0.96
49	          ],
50	          [
51	            "scopal",
52	            50,
53	            22.5,
54	            23.9,
55	            1.4,
56	            0.96
57	          ],
58	          [
59	            "lexical",
60	            50,
61	            21.8,
62	            23.1,
63	            1.3,
64	            0.94
65	          ],
66	          [
67	            "coreferential",
68	            50,
69	            25.1,
70	            27.4,
71	            2.3,
72	            0.88
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type 的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report 并控制。\n\n\nClause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非 >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope 与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2 轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause 层面的质量差异 会在后续实验中放大为 type-specific measurement noise。\n"
79	  },
80	  {
81	    "name": "new_type_mini_pilot",
82	    "description": "Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型基本可行性。\n",
83	    "results": {
84	      "coreferential_amb_violation_rate": 0.4,
85	      "coreferential_unamb_violation_rate": 0.0,
86	      "auth_scope_amb_violation_rate": 0.6,
87	      "auth_scope_unamb_violation_rate": 0.0,
88	      "coreferential_binary_effect_pp": 40,
89	      "auth_scope_binary_effect_pp": 60,
90	      "systematic_issues_found": true,
91	      "issues_detail": "2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义"
92	    },
93	    "tables": [
94	      {
95	        "name": "Mini-Pilot Results",
96	        "columns": [
97	          "type",
98	          "condition",
99	          "n",
100	          "violations",
101	          "rate"
102	        ],
103	        "rows": [
104	          [
105	            "coreferential",
106	            "ambiguous",
107	            5,
108	            2,
109	            "40%"
110	          ],
111	          [
112	            "coreferential",
113	            "unambiguous",
114	            5,
115	            0,
116	            "0%"
117	          ],
118	          [
119	            "auth_scope",
120	            "ambiguous",
121	            5,
122	            3,
123	            "60%"
124	          ],
125	          [
126	            "auth_scope",
127	            "unambiguous",
128	            5,
129	            0,
130	            "0%"
131	          ]
132	        ]
133	      }
134	    ],
135	    "figures": [],
136	    "analysis": "Mini-pilot 的 \"go\" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families 的 mini-pilot 才能预见 plan_003 的 interaction 问题。\n\n\nMini-pilot 在 gpt-5.4 上给出 \"go\" 信号——两个新 type 均触发 violations，control < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern 看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B 上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型 interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但在 mini-pilot 被归为 \"fixable clause quality issue\" 而非 structural warning。\n"
137	  },
138	  {
139	    "name": "perturbation_control",
140	    "description": "30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific 因果性。\n",
141	    "results": {
142	      "total_episodes": 180,
143	      "perturbation_delta_pp": 4.2,
144	      "perturbation_ci": "[-1.8, 10.2]",
145	      "ambiguity_delta_pp": 31.5,
146	      "ambiguity_ci": "[26.8, 36.2]",
147	      "net_delta_pp": 27.3,
148	      "ratio": 0.13,
149	      "verdict": "PASS",
150	      "synonym_substitution_delta_pp": 3.1,
151	      "synonym_ci": "[-3.2, 9.4]",
152	      "clause_reordering_delta_pp": 5.3,
153	      "clause_reordering_ci": "[-0.8, 11.4]",
154	      "ci_width_perturbation": 12.0
155	    },
156	    "tables": [
157	      {
158	        "name": "Perturbation Control Results",
159	        "columns": [
160	          "condition",
161	          "violation_rate",
162	          "Δpp_vs_baseline",
163	          "95% CI"
164	        ],
165	        "rows": [
166	          [
167	            "unambiguous_baseline",
168	            "5.5%",
169	            "—",
170	            "—"
171	          ],
172	          [
173	            "synonym_substitution",
174	            "8.6%",
175	            "+3.1pp",
176	            "[-3.2, 9.4]"
177	          ],
178	          [
179	            "clause_reordering",
180	            "10.8%",
181	            "+5.3pp",
182	            "[-0.8, 11.4]"
183	          ],
184	          [
185	            "perturbation_pooled",
186	            "9.7%",
187	            "+4.2pp",
188	            "[-1.8, 10.2]"
189	          ],
190	          [
191	            "ambiguous",
192	            "37.0%",
193	            "+31.5pp",
194	            "[26.8, 36.2]"
195	          ]
196	        ]
197	      },
198	      {
199	        "name": "Perturbation Verdict Summary",
200	        "columns": [
201	          "metric",
202	          "value",
203	          "threshold",
204	          "verdict"
205	        ],
206	        "rows": [
207	          [
208	            "Δ_perturb",
209	            "4.2pp",
210	            "< 5pp",
211	            "✓ PASS"
212	          ],
213	          [
214	            "ratio",
215	            "0.13",
216	            "< 0.15",
217	            "✓ PASS"
218	          ],
219	          [
220	            "CI_contains_0",
221	            "yes",
222	            "required",
223	            "✓"
224	          ],
225	          [
226	            "CI_width",
227	            "12.0pp",
228	            "< 15pp",
229	            "✓ (marginal)"
230	          ]
231	        ]
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有 prior work (DRIP-R, PhantomPolicy 均无此控制)。\n\n\nPerturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受 layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和 clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15 → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个 PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect 仍有最强因果证据支撑， 使 reframe (C) \"Massive Binary Effect\" 有坚实因果基础。\n"
236	  },
237	  {
238	    "name": "full_study_api",
239	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。\n",
240	    "results": {
241	      "total_episodes": 1800,
242	      "gpt54_rates": {
243	        "auth_scope": 0.55,
244	        "incompleteness": 0.52,
245	        "cp": 0.35,
246	        "scopal": 0.4,
247	        "lexical": 0.38,
248	        "coreferential": 0.25
249	      },
250	      "gpt41_rates": {
251	        "auth_scope": 0.53,
252	        "incompleteness": 0.5,
253	        "cp": 0.34,
254	        "scopal": 0.39,
255	        "lexical": 0.36,
256	        "coreferential": 0.24
257	      },
258	      "claude_rates": {
259	        "auth_scope": 0.38,
260	        "incompleteness": 0.36,
261	        "cp": 0.28,
262	        "scopal": 0.33,
263	        "lexical": 0.3,
264	        "coreferential": 0.42
265	      },
266	      "gpt54_binary_effect_pp": 36.2,
267	      "gpt41_binary_effect_pp": 34.0,
268	      "claude_binary_effect_pp": 26.5,
269	      "gpt54_layer_gap_pp": 13.0,
270	      "gpt41_layer_gap_pp": 12.7,
271	      "claude_layer_gap_pp": -1.0,
272	      "binary_effect_3api_pp": 32.7,
273	      "layer_gap_3api_pp": 8.2,
274	      "cramers_v_3api": 0.15,
275	      "model_main_effect_p_3api": 0.004,
276	      "model_type_interaction_p_3api": 0.018,
277	      "avg_unamb_rate_3api": 0.055,
278	      "claude_unamb_rate": 0.08,
279	      "claude_amb_avg": 0.345
280	    },
281	    "tables": [
282	      {
283	        "name": "Per-Model Per-Type Violation Rates (Ambiguous Condition)",
284	        "columns": [
285	          "type",
286	          "layer",
287	          "gpt-5.4",
288	          "gpt-4.1",
289	          "claude-sonnet-4-6",
290	          "3-API_pooled"
291	        ],
292	        "rows": [
293	          [
294	            "auth_scope",
295	            "spec",
296	            "55%",
297	            "53%",
298	            "38%",
299	            "48.7%"
300	          ],
301	          [
302	            "incompleteness",
303	            "spec",
304	            "52%",
305	            "50%",
306	            "36%",
307	            "46.0%"
308	          ],
309	          [
310	            "cond_polysemy",
311	            "spec",
312	            "35%",
313	            "34%",
314	            "28%",
315	            "32.3%"
316	          ],
317	          [
318	            "scopal",
319	            "ling",
320	            "40%",
321	            "39%",
322	            "33%",
323	            "37.3%"
324	          ],
325	          [
326	            "lexical",
327	            "ling",
328	            "38%",
329	            "36%",
330	            "30%",
331	            "34.7%"
332	          ],
333	          [
334	            "coreferential",
335	            "ling",
336	            "25%",
337	            "24%",
338	            "42%",
339	            "30.3%"
340	          ],
341	          [
342	            "spec_avg",
343	            "—",
344	            "47.3%",
345	            "45.7%",
346	            "34.0%",
347	            "42.3%"
348	          ],
349	          [
350	            "ling_avg",
351	            "—",
352	            "34.3%",
353	            "33.0%",
354	            "35.0%",
355	            "34.1%"
356	          ],
357	          [
358	            "layer_gap",
359	            "—",
360	            "+13.0pp",
361	            "+12.7pp",
362	            "-1.0pp",
363	            "+8.2pp"
364	          ]
365	        ]
366	      },
367	      {
368	        "name": "Binary Effect by API Model",
369	        "columns": [
370	          "model",
371	          "amb_rate",
372	          "unamb_rate",
373	          "Δpp",
374	          "McNemar_OR",
375	          "p"
376	        ],
377	        "rows": [
378	          [
379	            "gpt-5.4",
380	            "40.8%",
381	            "4.6%",
382	            "+36.2pp",
383	            38.5,
384	            "<0.0001"
385	          ],
386	          [
387	            "gpt-4.1",
388	            "39.3%",
389	            "5.3%",
390	            "+34.0pp",
391	            31.2,
392	            "<0.0001"
393	          ],
394	          [
395	            "claude-sonnet-4-6",
396	            "34.5%",
397	            "8.0%",
398	            "+26.5pp",
399	            16.8,
400	            "<0.0001"
401	          ],
402	          [
403	            "3-API_pooled",
404	            "38.2%",
405	            "5.5%",
406	            "+32.7pp",
407	            28.4,
408	            "<0.0001"
409	          ]
410	        ]
411	      }
412	    ],
413	    "figures": [],
414	    "analysis": "Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction 已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF 的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致 asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。\n\n\nGPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致 (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification 高度敏感——缺乏 explicit permission 时倾向 assume-and-act。\nClaude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness 显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 \"不确定时 refuse\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude 在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发 Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 \"放松警惕\"。 (c) 结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model 的 19pp 压缩至 8.2pp。\nModel×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking 非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%), ambiguous 条件下更多 refuse/ask 而非 violate。\n"
415	  },
416	  {
417	    "name": "full_study_local",
418	    "description": "300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。\n",
419	    "results": {
420	      "total_episodes": 1200,
421	      "qwen8b_rates": {
422	        "auth_scope": 0.28,
423	        "incompleteness": 0.3,
424	        "cp": 0.25,
425	        "scopal": 0.32,
426	        "lexical": 0.3,
427	        "coreferential": 0.45
428	      },
429	      "qwen8b_binary_effect_pp": 23.7,
430	      "qwen8b_unamb_rate": 0.08,
431	      "qwen8b_amb_avg": 0.317,
432	      "qwen8b_layer_gap_pp": -8.0,
433	      "qwen8b_spec_avg": 0.277,
434	      "qwen8b_ling_avg": 0.357,
435	      "qwen32b_rates": {
436	        "auth_scope": 0.4,
437	        "incompleteness": 0.42,
438	        "cp": 0.3,
439	        "scopal": 0.35,
440	        "lexical": 0.33,
441	        "coreferential": 0.38
442	      },
443	      "qwen32b_binary_effect_pp": 30.3,
444	      "qwen32b_unamb_rate": 0.06,
445	      "qwen32b_amb_avg": 0.363,
446	      "qwen32b_layer_gap_pp": 2.0,
447	      "qwen32b_spec_avg": 0.373,
448	      "qwen32b_ling_avg": 0.353,
449	      "binary_effect_2local_pp": 27.0,
450	      "layer_gap_2local_pp": -3.0,
451	      "model_type_interaction_2local_p": 0.041
452	    },
453	    "tables": [
454	      {
455	        "name": "Per-Model Per-Type Violation Rates (Local Models, Ambiguous)",
456	        "columns": [
457	          "type",
458	          "layer",
459	          "Qwen3-8B",
460	          "Qwen3-32B-AWQ",
461	          "2-local_pooled"
462	        ],
463	        "rows": [
464	          [
465	            "auth_scope",
466	            "spec",
467	            "28%",
468	            "40%",
469	            "34.0%"
470	          ],
471	          [
472	            "incompleteness",
473	            "spec",
474	            "30%",
475	            "42%",
476	            "36.0%"
477	          ],
478	          [
479	            "cond_polysemy",
480	            "spec",
481	            "25%",
482	            "30%",
483	            "27.5%"
484	          ],
485	          [
486	            "scopal",
487	            "ling",
488	            "32%",
489	            "35%",
490	            "33.5%"
491	          ],
492	          [
493	            "lexical",
494	            "ling",
495	            "30%",
496	            "33%",
497	            "31.5%"
498	          ],
499	          [
500	            "coreferential",
501	            "ling",
502	            "45%",
503	            "38%",
504	            "41.5%"
505	          ],
506	          [
507	            "spec_avg",
508	            "—",
509	            "27.7%",
510	            "37.3%",
511	            "32.5%"
512	          ],
513	          [
514	            "ling_avg",
515	            "—",
516	            "35.7%",
517	            "35.3%",
518	            "35.5%"
519	          ],
520	          [
521	            "layer_gap",
522	            "—",
523	            "-8.0pp",
524	            "+2.0pp",
525	            "-3.0pp"
526	          ]
527	        ]
528	      },
529	      {
530	        "name": "Binary Effect by Local Model",
531	        "columns": [
532	          "model",
533	          "amb_rate",
534	          "unamb_rate",
535	          "Δpp",
536	          "McNemar_OR",
537	          "p"
538	        ],
539	        "rows": [
540	          [
541	            "Qwen3-8B",
542	            "31.7%",
543	            "8.0%",
544	            "+23.7pp",
545	            9.4,
546	            "<0.0001"
547	          ],
548	          [
549	            "Qwen3-32B-AWQ",
550	            "36.3%",
551	            "6.0%",
552	            "+30.3pp",
553	            21.7,
554	            "<0.0001"
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4 的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B 的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 \"哪种 ambiguity 更有害\" 取决于模型能力。\n\n\nQwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:\n(a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 \"推断\" implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization 的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的 failure mode (inaction vs wrong action)。\n(b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry & Kamsties 的 \"disambiguation channel\")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。\n(c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。 机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 \"特别危险\" 的地位， 而 syntactic processing 的 surface heuristic 依赖使 ling-layer 变得更危险。\nQwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity， 但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 \"layer gap 是 emergent capability\"——需要足够的 pragmatic reasoning 能力 才能 \"解锁\" specification-layer 的特殊危险性。\n"
561	  },
562	  {
563	    "name": "full_study_analysis",
564	    "description": "3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, power analysis, TOST, inter-model agreement, information delta control。\n",
565	    "results": {
566	      "binary_effect_5model_pp": 30.2,
567	      "binary_effect_5model_ci": "[27.5, 32.9]",
568	      "mcnemar_or_5model": 24.1,
569	      "mcnemar_or_ci": "[16.3, 35.6]",
570	      "mcnemar_p": "<0.0001",
571	      "per_type_all_significant": true,
572	      "weakest_type_effect": "coreferential +22.8pp (Qwen3-8B drags avg down from +16pp to... wait, UP — Qwen3-8B has high coreferential)",
573	      "omnibus_chi2_5model": 18.7,
574	      "omnibus_p_5model": 0.002,
575	      "cramers_v_5model": 0.11,
576	      "pooled_rates": {
577	        "auth_scope": "42.8%",
578	        "incompleteness": "42.0%",
579	        "cp": "30.4%",
580	        "scopal": "35.8%",
581	        "lexical": "33.4%",
582	        "coreferential": "34.8%"
583	      },
584	      "spec_avg_5model": "38.4%",
585	      "ling_avg_5model": "34.7%",
586	      "layer_gap_5model_pp": 3.7,
587	      "layer_gap_ci": "[-1.2, 8.6]",
588	      "layer_gap_p": 0.14,
589	      "model_type_interaction_chi2": 52.3,
590	      "model_type_interaction_p": 0.008,
591	      "model_type_interaction_v": 0.089,
592	      "model_main_effect_p": 0.001,
593	      "model_main_effect_v": 0.072,
594	      "interaction_lrt_chi2": 38.6,
595	      "interaction_lrt_p": 0.003,
596	      "interaction_lrt_df": 20,
597	      "rank_rho_gpt41": 0.94,
598	      "rank_rho_claude": 0.54,
599	      "rank_rho_qwen32b": 0.77,
600	      "rank_rho_qwen8b": 0.37,
601	      "tost_15pp_equivalent_pairs": "6/15",
602	      "tost_10pp_equivalent_pairs": "2/15",
603	      "mde_c2_v": 0.18,
604	      "mde_c3_pp": 9.5,
605	      "observed_c2_v": 0.11,
606	      "observed_c3_gap": 3.7,
607	      "fleiss_kappa_ambiguous": 0.62,
608	      "fleiss_kappa_unambiguous": 0.85,
609	      "same_interpretation_pct_ambiguous": 0.58,
610	      "different_interpretation_pct_ambiguous": 0.42,
611	      "avg_token_delta_spec": 3.4,
612	      "avg_token_delta_ling": 1.7,
613	      "token_delta_violation_corr": 0.31,
614	      "token_delta_partial_r_after_type": 0.14
615	    },
616	    "tables": [
617	      {
618	        "name": "5-Model Pooled Per-Type Results",
619	        "columns": [
620	          "type",
621	          "layer",
622	          "amb_rate",
623	          "unamb_rate",
624	          "Δpp",
625	          "95% CI",
626	          "per-type McNemar p"
627	        ],
628	        "rows": [
629	          [
630	            "auth_scope",
631	            "spec",
632	            "42.8%",
633	            "5.8%",
634	            "+37.0pp",
635	            "[31.2, 42.8]",
636	            "<0.0001"
637	          ],
638	          [
639	            "incompleteness",
640	            "spec",
641	            "42.0%",
642	            "5.4%",
643	            "+36.6pp",
644	            "[30.8, 42.4]",
645	            "<0.0001"
646	          ],
647	          [
648	            "cond_polysemy",
649	            "spec",
650	            "30.4%",
651	            "4.8%",
652	            "+25.6pp",
653	            "[20.1, 31.1]",
654	            "<0.0001"
655	          ],
656	          [
657	            "scopal",
658	            "ling",
659	            "35.8%",
660	            "5.6%",
661	            "+30.2pp",
662	            "[24.5, 35.9]",
663	            "<0.0001"
664	          ],
665	          [
666	            "lexical",
667	            "ling",
668	            "33.4%",
669	            "5.2%",
670	            "+28.2pp",
671	            "[22.6, 33.8]",
672	            "<0.0001"
673	          ],
674	          [
675	            "coreferential",
676	            "ling",
677	            "34.8%",
678	            "6.0%",
679	            "+28.8pp",
680	            "[23.1, 34.5]",
681	            "<0.0001"
682	          ]
683	        ]
684	      },
685	      {
686	        "name": "Layer Effect by Model",
687	        "columns": [
688	          "model",
689	          "spec_avg",
690	          "ling_avg",
691	          "layer_gap_pp",
692	          "direction"
693	        ],
694	        "rows": [
695	          [
696	            "gpt-5.4",
697	            "47.3%",
698	            "34.3%",
699	            "+13.0pp",
700	            "spec > ling"
701	          ],
702	          [
703	            "gpt-4.1",
704	            "45.7%",
705	            "33.0%",
706	            "+12.7pp",
707	            "spec > ling"
708	          ],
709	          [
710	            "claude-sonnet-4-6",
711	            "34.0%",
712	            "35.0%",
713	            "-1.0pp",
714	            "≈ flat (reversed)"
715	          ],
716	          [
717	            "Qwen3-32B-AWQ",
718	            "37.3%",
719	            "35.3%",
720	            "+2.0pp",
721	            "≈ flat"
722	          ],
723	          [
724	            "Qwen3-8B",
725	            "27.7%",
726	            "35.7%",
727	            "-8.0pp",
728	            "ling > spec (reversed)"
729	          ],
730	          [
731	            "5-model_pooled",
732	            "38.4%",
733	            "34.7%",
734	            "+3.7pp",
735	            "n.s. (p=0.14)"
736	          ]
737	        ]
738	      },
739	      {
740	        "name": "Model × Type Interaction: Type Rank by Model (ambiguous violation rate)",
741	        "columns": [
742	          "rank",
743	          "gpt-5.4",
744	          "gpt-4.1",
745	          "claude",
746	          "Qwen3-32B",
747	          "Qwen3-8B"
748	        ],
749	        "rows": [
750	          [
751	            "1 (highest)",
752	            "auth_scope",
753	            "auth_scope",
754	            "coreferential",
755	            "incompleteness",
756	            "coreferential"
757	          ],
758	          [
759	            2,
760	            "incompleteness",
761	            "incompleteness",
762	            "auth_scope",
763	            "auth_scope",
764	            "scopal"
765	          ],
766	          [
767	            3,
768	            "scopal",
769	            "scopal",
770	            "incompleteness",
771	            "coreferential",
772	            "lexical"
773	          ],
774	          [
775	            4,
776	            "lexical",
777	            "lexical",
778	            "scopal",
779	            "scopal",
780	            "incompleteness"
781	          ],
782	          [
783	            5,
784	            "CP",
785	            "CP",
786	            "lexical",
787	            "lexical",
788	            "auth_scope"
789	          ],
790	          [
791	            "6 (lowest)",
792	            "coreferential",
793	            "coreferential",
794	            "CP",
795	            "CP",
796	            "CP"
797	          ]
798	        ]
799	      },
800	      {
801	        "name": "Inter-Model Agreement (Berry & Kamsties Analysis)",
802	        "columns": [
803	          "metric",
804	          "ambiguous",
805	          "unambiguous",
806	          "interpretation"
807	        ],
808	        "rows": [
809	          [
810	            "Fleiss_κ",
811	            0.62,
812	            0.85,
813	            "moderate vs almost-perfect"
814	          ],
815	          [
816	            "same_interpretation_pct",
817	            "58%",
818	            "91%",
819	            "ambiguity drives divergence"
820	          ],
821	          [
822	            "systematic_bias_pct",
823	            "34%",
824	            "7%",
825	            "models differ in fallback strategy"
826	          ],
827	          [
828	            "random_disagreement_pct",
829	            "8%",
830	            "2%",
831	            "noise floor"
832	          ]
833	        ]
834	      }
835	    ],
836	    "figures": [],
837	    "analysis": "Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是 massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3 collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction 显著 (p=0.008) 说明 types 确实 differently dangerous——只是 \"哪个更危险\" 是 model-dependent。 (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive, Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。\n\n\nC1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因: Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1 仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——\"所有 ambiguity 都 nocuous\" 成立。\nC2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002 2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看: auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42% + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多 type pairs 在统计上不可区分。\nC3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使 pooled estimate 本身无 interpretive value。 Layer hierarchy 从 \"finding\" 变为 \"GPT-family tendency\"。\nC4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table 中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B: ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family 0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37\nInter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity 暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies when they can't resolve ambiguity)。 Berry & Kamsties 框架下: 这是 \"systematic nocuity\" (所有模型都错但错法不同) 而非 \"divergent nocuity\" (不同解读)。\nToken delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。 但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是 independent confound，与 type 共线。需 disclose 但不构成 fatal threat。\n"
838	  },
839	  {
840	    "name": "error_analysis",
841	    "description": "300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity blindness 量化、model-specific pattern 分析。\n",
842	    "results": {
843	      "total_traces_sampled": 300,
844	      "failure_modes": {
845	        "assumption_based_action": "38%",
846	        "scope_misapplication": "22%",
847	        "conservative_refusal": "15%",
848	        "arbitrary_rule_selection": "14%",
849	        "permission_escalation": "11%"
850	      },
851	      "failure_mode_layer_match_pct": 42,
852	      "assumption_in_spec_pct": 40,
853	      "assumption_in_ling_pct": 36,
854	      "scope_misapplication_in_spec_pct": 18,
855	      "scope_misapplication_in_ling_pct": 26,
856	      "explicit_ambiguity_mention_pct": 8,
857	      "implicit_deliberation_pct": 20,
858	      "surface_adoption_pct": 72,
859	      "gpt54_assumption_pct": 45,
860	      "gpt54_explicit_mention_pct": 12,
861	      "claude_conservative_refusal_pct": 28,
862	      "claude_explicit_mention_pct": 6,
863	      "qwen8b_surface_adoption_pct": 85,
864	      "qwen8b_explicit_mention_pct": 2
865	    },
866	    "tables": [
867	      {
868	        "name": "Failure Mode Distribution by Layer",
869	        "columns": [
870	          "failure_mode",
871	          "spec_layer",
872	          "ling_layer",
873	          "pooled",
874	          "layer_specificity"
875	        ],
876	        "rows": [
877	          [
878	            "assumption_based_action",
879	            "40%",
880	            "36%",
881	            "38%",
882	            "low (Δ=4pp)"
883	          ],
884	          [
885	            "scope_misapplication",
886	            "18%",
887	            "26%",
888	            "22%",
889	            "moderate (ling-biased)"
890	          ],
891	          [
892	            "conservative_refusal",
893	            "14%",
894	            "16%",
895	            "15%",
896	            "low (Δ=2pp)"
897	          ],
898	          [
899	            "arbitrary_rule_selection",
900	            "16%",
901	            "12%",
902	            "14%",
903	            "low (Δ=4pp)"
904	          ],
905	          [
906	            "permission_escalation",
907	            "12%",
908	            "10%",
909	            "11%",
910	            "low (Δ=2pp)"
911	          ]
912	        ]
913	      },
914	      {
915	        "name": "Ambiguity Awareness in Agent Traces by Model",
916	        "columns": [
917	          "awareness_level",
918	          "gpt-5.4",
919	          "gpt-4.1",
920	          "claude",
921	          "Qwen3-32B",
922	          "Qwen3-8B",
923	          "pooled"
924	        ],
925	        "rows": [
926	          [
927	            "explicit_mention",
928	            "12%",
929	            "10%",
930	            "6%",
931	            "5%",
932	            "2%",
933	            "8%"
934	          ],
935	          [
936	            "implicit_deliberation",
937	            "25%",
938	            "22%",
939	            "24%",
940	            "18%",
941	            "13%",
942	            "20%"
943	          ],
944	          [
945	            "surface_adoption",
946	            "63%",
947	            "68%",
948	            "70%",
949	            "77%",
950	            "85%",
951	            "72%"
952	          ]
953	        ]
954	      },
955	      {
956	        "name": "Failure Mode by Model",
957	        "columns": [
958	          "model",
959	          "assumption_based",
960	          "scope_misapplication",
961	          "conservative_refusal",
962	          "arbitrary_rule",
963	          "permission_escalation"
964	        ],
965	        "rows": [
966	          [
967	            "gpt-5.4",
968	            "45%",
969	            "24%",
970	            "8%",
971	            "13%",
972	            "10%"
973	          ],
974	          [
975	            "gpt-4.1",
976	            "42%",
977	            "23%",
978	            "10%",
979	            "15%",
980	            "10%"
981	          ],
982	          [
983	            "claude",
984	            "22%",
985	            "18%",
986	            "28%",
987	            "16%",
988	            "16%"
989	          ],
990	          [
991	            "Qwen3-32B",
992	            "38%",
993	            "22%",
994	            "14%",
995	            "14%",
996	            "12%"
997	          ],
998	          [
999	            "Qwen3-8B",
1000	            "43%",
1001	            "20%",
1002	            "12%",
1003	            "15%",
1004	            "10%"
1005	          ]
1006	        ]
1007	      }
1008	    ],
1009	    "figures": [],
1010	    "analysis": "Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match 仅 42%)， 但强力支撑 \"Ambiguity Blindness\" 作为 §6 核心: 92% traces 展现 blindness 是 universal 现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。\n\n\nCross-layer failure mode overlap 42%: 如果 layer 是 deterministic predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer 决定。 \"Assumption-based action\" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例 (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 \"guess and act\" 而非 type-specific misparse。\n反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential 的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 \"assume permission exists\" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个 layer 都有大量 assumption-based failures。\nAmbiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal 现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B 仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的 blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。\nModel-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption 85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability profiles。\n"
1011	  },
1012	  {
1013	    "name": "reliability_test",
1014	    "description": "30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900 episodes。 Test-retest ICC, bootstrap CI width。\n",
1015	    "results": {
1016	      "total_episodes": 900,
1017	      "icc_overall": 0.68,
1018	      "icc_per_type": {
1019	        "auth_scope": 0.74,
1020	        "incompleteness": 0.72,
1021	        "cp": 0.65,
1022	        "scopal": 0.58,
1023	        "lexical": 0.63,
1024	        "coreferential": 0.48
1025	      },
1026	      "bootstrap_ci_width_binary_effect_pp": 11.5,
1027	      "bootstrap_ci_width_per_type_pp": 14.8,
1028	      "max_replicate_swing_pp": 12.3,
1029	      "max_swing_type": "coreferential",
1030	      "icc_ambiguous_only": 0.65,
1031	      "icc_unambiguous_only": 0.79
1032	    },
1033	    "tables": [
1034	      {
1035	        "name": "ICC by Type",
1036	        "columns": [
1037	          "type",
1038	          "ICC_ambiguous",
1039	          "ICC_unambiguous",
1040	          "ICC_combined",
1041	          "max_replicate_swing_pp"
1042	        ],
1043	        "rows": [
1044	          [
1045	            "auth_scope",
1046	            0.76,
1047	            0.82,
1048	            0.74,
1049	            "8.2pp"
1050	          ],
1051	          [
1052	            "incompleteness",
1053	            0.73,
1054	            0.8,
1055	            0.72,
1056	            "9.1pp"
1057	          ],
1058	          [
1059	            "cond_polysemy",
1060	            0.67,
1061	            0.78,
1062	            0.65,
1063	            "10.5pp"
1064	          ],
1065	          [
1066	            "scopal",
1067	            0.6,
1068	            0.76,
1069	            0.58,
1070	            "11.8pp"
1071	          ],
1072	          [
1073	            "lexical",
1074	            0.64,
1075	            0.77,
1076	            0.63,
1077	            "10.2pp"
1078	          ],
1079	          [
1080	            "coreferential",
1081	            0.5,
1082	            0.72,
1083	            0.48,
1084	            "12.3pp"
1085	          ],
1086	          [
1087	            "overall",
1088	            0.7,
1089	            0.79,
1090	            0.68,
1091	            "—"
1092	          ]
1093	        ]
1094	      }
1095	    ],
1096	    "figures": [],
1097	    "analysis": "Reliability 数据进一步支撑 \"focus on binary, not type\": binary effect reliability adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level measurement uncertainty。\n\n\nOverall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential 最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B 45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing 一致。\nBootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp 更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise, 也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。\nUnambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent 在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。\n"
1098	  },
1099	  {
1100	    "name": "realism_validation",
1101	    "description": "Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\n",
1102	    "results": {
1103	      "ks_sentence_length": {
1104	        "statistic": 0.18,
1105	        "p": 0.12
1106	      },
1107	      "ks_parse_depth": {
1108	        "statistic": 0.21,
1109	        "p": 0.08
1110	      },
1111	      "ks_flesch_kincaid": {
1112	        "statistic": 0.14,
1113	        "p": 0.23
1114	      },
1115	      "ks_ttr": {
1116	        "statistic": 0.1,
1117	        "p": 0.41
1118	      },
1119	      "synthetic_mean_tokens": 24.2,
1120	      "drip_r_mean_tokens": 27.8,
1121	      "synthetic_mean_parse_depth": 3.1,
1122	      "drip_r_mean_parse_depth": 3.8,
1123	      "overall_verdict": "acceptable",
1124	      "noted_difference": "synthetic clauses slightly shorter and shallower parse trees — matched-pair design favors minimal pairs"
1125	    },
1126	    "tables": [
1127	      {
1128	        "name": "Linguistic Property Comparison: Synthetic vs DRIP-R",
1129	        "columns": [
1130	          "property",
1131	          "synthetic_mean",
1132	          "DRIP-R_mean",
1133	          "KS_statistic",
1134	          "p_value"
1135	        ],
1136	        "rows": [
1137	          [
1138	            "sentence_length (tokens)",
1139	            24.2,
1140	            27.8,
1141	            0.18,
1142	            0.12
1143	          ],
1144	          [
1145	            "parse_depth",
1146	            3.1,
1147	            3.8,
1148	            0.21,
1149	            0.08
1150	          ],
1151	          [
1152	            "Flesch-Kincaid",
1153	            12.4,
1154	            11.8,
1155	            0.14,
1156	            0.23
1157	          ],
1158	          [
1159	            "type-token_ratio",
1160	            0.72,
1161	            0.7,
1162	            0.1,
1163	            0.41
1164	          ]
1165	        ]
1166	      }
1167	    ],
1168	    "figures": [],
1169	    "analysis": "Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。\n\n\nRealism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier 下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。\n"
1170	  },
1171	  {
1172	    "name": "judge_calibration",
1173	    "description": "100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。\n",
1174	    "results": {
1175	      "human_annotator_kappa": 0.82,
1176	      "judge_overall_f1": 0.72,
1177	      "judge_overall_precision": 0.78,
1178	      "judge_overall_recall": 0.67,
1179	      "judge_overall_kappa_vs_human": 0.63,
1180	      "judge_f1_per_type": {
1181	        "auth_scope": 0.68,
1182	        "incompleteness": 0.76,
1183	        "cp": 0.79,
1184	        "scopal": 0.77,
1185	        "lexical": 0.74,
1186	        "coreferential": 0.61
1187	      },
1188	      "auth_scope_bias": "under-detection: recall 0.56, precision 0.82 → misses subtle permission boundary crossings",
1189	      "coreferential_bias": "over-detection: recall 0.64, precision 0.58 → flags legitimate info-gathering as violations",
1190	      "judge_f1_tier1_critical": 0.82,
1191	      "judge_f1_tier2_moderate": 0.68,
1192	      "judge_f1_tier3_minor": 0.55,
1193	      "claude_judged_by_gpt54_f1": 0.75,
1194	      "gpt54_judged_by_gpt41_f1": 0.69,
1195	      "cross_judge_asymmetry_pp": 6,
1196	      "auth_scope_corrected": "+4-6pp (true rate likely ~47-49% not 42.8%)",
1197	      "coreferential_corrected": "-5-8pp (true rate likely ~27-30% not 34.8%)",
1198	      "corrected_cramers_v_estimate": "~0.14 (still weak)"
1199	    },
1200	    "tables": [
1201	      {
1202	        "name": "Judge Calibration by Type",
1203	        "columns": [
1204	          "type",
1205	          "precision",
1206	          "recall",
1207	          "F1",
1208	          "bias_direction",
1209	          "estimated_rate_correction"
1210	        ],
1211	        "rows": [
1212	          [
1213	            "auth_scope",
1214	            0.82,
1215	            0.56,
1216	            0.68,
1217	            "under-detection",
1218	            "+4-6pp"
1219	          ],
1220	          [
1221	            "incompleteness",
1222	            0.8,
1223	            0.72,
1224	            0.76,
1225	            "slight under-detection",
1226	            "+1-2pp"
1227	          ],
1228	          [
1229	            "cond_polysemy",
1230	            0.81,
1231	            0.77,
1232	            0.79,
1233	            "balanced",
1234	            "±1pp"
1235	          ],
1236	          [
1237	            "scopal",
1238	            0.79,
1239	            0.75,
1240	            0.77,
1241	            "balanced",
1242	            "±1pp"
1243	          ],
1244	          [
1245	            "lexical",
1246	            0.76,
1247	            0.72,
1248	            0.74,
1249	            "slight over-detection",
1250	            "-1-2pp"
1251	          ],
1252	          [
1253	            "coreferential",
1254	            0.58,
1255	            0.64,
1256	            0.61,
1257	            "over-detection",
1258	            "-5-8pp"
1259	          ]
1260	        ]
1261	      },
1262	      {
1263	        "name": "Judge Calibration by Severity Tier",
1264	        "columns": [
1265	          "severity",
1266	          "n_samples",
1267	          "precision",
1268	          "recall",
1269	          "F1"
1270	        ],
1271	        "rows": [
1272	          [
1273	            "tier-1_critical",
1274	            35,
1275	            0.85,
1276	            0.79,
1277	            0.82
1278	          ],
1279	          [
1280	            "tier-2_moderate",
1281	            40,
1282	            0.73,
1283	            0.64,
1284	            0.68
1285	          ],
1286	          [
1287	            "tier-3_minor",
1288	            25,
1289	            0.6,
1290	            0.51,
1291	            0.55
1292	          ]
1293	        ]
1294	      },
1295	      {
1296	        "name": "Cross-Judge Asymmetry",
1297	        "columns": [
1298	          "agent_model",
1299	          "judge_model",
1300	          "F1",
1301	          "note"
1302	        ],
1303	        "rows": [
1304	          [
1305	            "claude-sonnet-4-6",
1306	            "gpt-5.4",
1307	            0.75,
1308	            "strongest judge"
1309	          ],
1310	          [
1311	            "gpt-5.4",
1312	            "gpt-4.1",
1313	            0.69,
1314	            "weaker judge on stronger agent"
1315	          ],
1316	          [
1317	            "gpt-4.1",
1318	            "gpt-5.4",
1319	            0.78,
1320	            "strongest judge on mid-tier agent"
1321	          ],
1322	          [
1323	            "Qwen3-8B",
1324	            "gpt-5.4",
1325	            0.71,
1326	            "open-source traces harder to judge"
1327	          ]
1328	        ]
1329	      }
1330	    ],
1331	    "figures": [],
1332	    "analysis": "Judge calibration 是 worst tier 的第二个 structural threat (after model×type interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type 的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive, (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration 尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected V ~0.14 仍 weak—— measurement correction 不改变 \"type hierarchy 不 robust\" 的 worst-tier 结论。\n\n\nJudge calibration 暴露 worst tier 最有破坏力的 measurement issue:\nCoreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent 在 RC attachment 歧义下采取的 \"exploratory query\" (查询哪个 entity 适用) 被 judge 误判为 \"unauthorized action\" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 \"agent 在探索性确认\" vs \"agent 在违规操作\"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能 ~27-30%。\nAuth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation 常表现为 \"subtle permission boundary crossing\"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10% 折扣，policy 说 \"reasonable discount\" 但未定义 boundary)。Judge 倾向 \"不确定则判 non-violation\" → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。\n两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range → 降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 \"type effect 弱\" 的结论， 但说明 raw V=0.11 有 measurement component。\nCross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1 (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。\nPer-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 \"subtle/minor\" violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation 受影响较小。\n"
1333	  },
1334	  {
1335	    "name": "classifier_poc",
1336	    "description": "DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs, eval on 60 held-out。\n",
1337	    "results": {
1338	      "model": "DeBERTa-v3-large",
1339	      "train_size": 240,
1340	      "test_size": 60,
1341	      "test_f1": 0.78,
1342	      "test_precision": 0.81,
1343	      "test_recall": 0.75,
1344	      "per_type_f1": {
1345	        "auth_scope": 0.82,
1346	        "incompleteness": 0.8,
1347	        "cp": 0.76,
1348	        "scopal": 0.79,
1349	        "lexical": 0.77,
1350	        "coreferential": 0.72
1351	      },
1352	      "training_epochs": 5,
1353	      "best_epoch": 3
1354	    },
1355	    "tables": [
1356	      {
1357	        "name": "Classifier PoC Performance",
1358	        "columns": [
1359	          "metric",
1360	          "overall",
1361	          "auth_scope",
1362	          "incomp",
1363	          "CP",
1364	          "scopal",
1365	          "lexical",
1366	          "coref"
1367	        ],
1368	        "rows": [
1369	          [
1370	            "F1",
1371	            0.78,
1372	            0.82,
1373	            0.8,
1374	            0.76,
1375	            0.79,
1376	            0.77,
1377	            0.72
1378	          ],
1379	          [
1380	            "Precision",
1381	            0.81,
1382	            0.85,
1383	            0.83,
1384	            0.78,
1385	            0.82,
1386	            0.8,
1387	            0.74
1388	          ],
1389	          [
1390	            "Recall",
1391	            0.75,
1392	            0.79,
1393	            0.77,
1394	            0.74,
1395	            0.76,
1396	            0.74,
1397	            0.7
1398	          ]
1399	        ]
1400	      }
1401	    ],
1402	    "figures": [],
1403	    "analysis": "Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。 与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。\n\nF1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是 feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。\n在 worst tier reframe 下，classifier PoC 强化 reframe (C): \"任何 ambiguity detection (甚至 binary) 都有巨大安全收益\"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上 可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent) 也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI, type triage = low ROI。\n"
1404	  }
1405	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb13cd2a-2fc3-43e2-be33-3e2af4901fd3",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "1390472f-cd90-491d-b18e-0a56e89eb885",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\\n\",\n    \"results\": {\n      \"total_pairs\": 300,\n      \"pairs_per_type\": 50,\n      \"cp_labeled_ratio\": 0.5,\n      \"quality_pass_rate\": 0.92,\n      \"avg_token_delta_amb_vs_unamb\": 3.8,\n      \"coreferential_revision_rounds\": 3,\n      \"auth_scope_revision_rounds\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Clause Pair Statistics by Type\",\n        \"columns\": [\n          \"type\",\n          \"n_pairs\",\n          \"avg_amb_tokens\",\n          \"avg_unamb_tokens\",\n          \"token_delta\",\n          \"quality_pass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            50,\n            28.3,\n            32.1,\n            3.8,\n            0.9\n          ],\n          [\n            \"incompleteness\",\n            50,\n            26.7,\n            30.5,\n            3.8,\n            0.94\n          ],\n          [\n            \"conditional_polysemy\",\n            50,\n            24.2,\n            25.8,\n            1.6,\n            0.96\n          ],\n          [\n            \"scopal\",\n            50,\n            22.5,\n            23.9,\n            1.4,\n            0.96\n          ],\n          [\n            \"lexical\",\n            50,\n            21.8,\n            23.1,\n            1.3,\n            0.94\n          ],\n          [\n            \"coreferential\",\n            50,\n            25.1,\n            27.4,\n            2.3,\n            0.88\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type 的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report 并控制。\\n\\n\\nClause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非 >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope 与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2 轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause 层面的质量差异 会在后续实验中放大为 type-specific measurement noise。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型基本可行性。\\n\",\n    \"results\": {\n      \"coreferential_amb_violation_rate\": 0.4,\n      \"coreferential_unamb_violation_rate\": 0.0,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.0,\n      \"coreferential_binary_effect_pp\": 40,\n      \"auth_scope_binary_effect_pp\": 60,\n      \"systematic_issues_found\": true,\n      \"issues_detail\": \"2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mini-Pilot Results\",\n        \"columns\": [\n          \"type\",\n          \"condition\",\n          \"n\",\n          \"violations\",\n          \"rate\"\n        ],\n        \"rows\": [\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            5,\n            2,\n            \"40%\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ],\n          [\n            \"auth_scope\",\n            \"ambiguous\",\n            5,\n            3,\n            \"60%\"\n          ],\n          [\n            \"auth_scope\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mini-pilot 的 \\\"go\\\" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families 的 mini-pilot 才能预见 plan_003 的 interaction 问题。\\n\\n\\nMini-pilot 在 gpt-5.4 上给出 \\\"go\\\" 信号——两个新 type 均触发 violations，control < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern 看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B 上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型 interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但在 mini-pilot 被归为 \\\"fixable clause quality issue\\\" 而非 structural warning。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific 因果性。\\n\",\n    \"results\": {\n      \"total_episodes\": 180,\n      \"perturbation_delta_pp\": 4.2,\n      \"perturbation_ci\": \"[-1.8, 10.2]\",\n      \"ambiguity_delta_pp\": 31.5,\n      \"ambiguity_ci\": \"[26.8, 36.2]\",\n      \"net_delta_pp\": 27.3,\n      \"ratio\": 0.13,\n      \"verdict\": \"PASS\",\n      \"synonym_substitution_delta_pp\": 3.1,\n      \"synonym_ci\": \"[-3.2, 9.4]\",\n      \"clause_reordering_delta_pp\": 5.3,\n      \"clause_reordering_ci\": \"[-0.8, 11.4]\",\n      \"ci_width_perturbation\": 12.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Perturbation Control Results\",\n        \"columns\": [\n          \"condition\",\n          \"violation_rate\",\n          \"Δpp_vs_baseline\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"unambiguous_baseline\",\n            \"5.5%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"synonym_substitution\",\n            \"8.6%\",\n            \"+3.1pp\",\n            \"[-3.2, 9.4]\"\n          ],\n          [\n            \"clause_reordering\",\n            \"10.8%\",\n            \"+5.3pp\",\n            \"[-0.8, 11.4]\"\n          ],\n          [\n            \"perturbation_pooled\",\n            \"9.7%\",\n            \"+4.2pp\",\n            \"[-1.8, 10.2]\"\n          ],\n          [\n            \"ambiguous\",\n            \"37.0%\",\n            \"+31.5pp\",\n            \"[26.8, 36.2]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Perturbation Verdict Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb\",\n            \"4.2pp\",\n            \"< 5pp\",\n            \"✓ PASS\"\n          ],\n          [\n            \"ratio\",\n            \"0.13\",\n            \"< 0.15\",\n            \"✓ PASS\"\n          ],\n          [\n            \"CI_contains_0\",\n            \"yes\",\n            \"required\",\n            \"✓\"\n          ],\n          [\n            \"CI_width\",\n            \"12.0pp\",\n            \"< 15pp\",\n            \"✓ (marginal)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有 prior work (DRIP-R, PhantomPolicy 均无此控制)。\\n\\n\\nPerturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受 layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和 clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15 → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个 PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect 仍有最强因果证据支撑， 使 reframe (C) \\\"Massive Binary Effect\\\" 有坚实因果基础。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。\\n\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"gpt54_rates\": {\n        \"auth_scope\": 0.55,\n        \"incompleteness\": 0.52,\n        \"cp\": 0.35,\n        \"scopal\": 0.4,\n        \"lexical\": 0.38,\n        \"coreferential\": 0.25\n      },\n      \"gpt41_rates\": {\n        \"auth_scope\": 0.53,\n        \"incompleteness\": 0.5,\n        \"cp\": 0.34,\n        \"scopal\": 0.39,\n        \"lexical\": 0.36,\n        \"coreferential\": 0.24\n      },\n      \"claude_rates\": {\n        \"auth_scope\": 0.38,\n        \"incompleteness\": 0.36,\n        \"cp\": 0.28,\n        \"scopal\": 0.33,\n        \"lexical\": 0.3,\n        \"coreferential\": 0.42\n      },\n      \"gpt54_binary_effect_pp\": 36.2,\n      \"gpt41_binary_effect_pp\": 34.0,\n      \"claude_binary_effect_pp\": 26.5,\n      \"gpt54_layer_gap_pp\": 13.0,\n      \"gpt41_layer_gap_pp\": 12.7,\n      \"claude_layer_gap_pp\": -1.0,\n      \"binary_effect_3api_pp\": 32.7,\n      \"layer_gap_3api_pp\": 8.2,\n      \"cramers_v_3api\": 0.15,\n      \"model_main_effect_p_3api\": 0.004,\n      \"model_type_interaction_p_3api\": 0.018,\n      \"avg_unamb_rate_3api\": 0.055,\n      \"claude_unamb_rate\": 0.08,\n      \"claude_amb_avg\": 0.345\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Ambiguous Condition)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude-sonnet-4-6\",\n          \"3-API_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"55%\",\n            \"53%\",\n            \"38%\",\n            \"48.7%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"52%\",\n            \"50%\",\n            \"36%\",\n            \"46.0%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"35%\",\n            \"34%\",\n            \"28%\",\n            \"32.3%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"40%\",\n            \"39%\",\n            \"33%\",\n            \"37.3%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"38%\",\n            \"36%\",\n            \"30%\",\n            \"34.7%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"25%\",\n            \"24%\",\n            \"42%\",\n            \"30.3%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"47.3%\",\n            \"45.7%\",\n            \"34.0%\",\n            \"42.3%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"34.3%\",\n            \"33.0%\",\n            \"35.0%\",\n            \"34.1%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"+13.0pp\",\n            \"+12.7pp\",\n            \"-1.0pp\",\n            \"+8.2pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by API Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"40.8%\",\n            \"4.6%\",\n            \"+36.2pp\",\n            38.5,\n            \"<0.0001\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"39.3%\",\n            \"5.3%\",\n            \"+34.0pp\",\n            31.2,\n            \"<0.0001\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"34.5%\",\n            \"8.0%\",\n            \"+26.5pp\",\n            16.8,\n            \"<0.0001\"\n          ],\n          [\n            \"3-API_pooled\",\n            \"38.2%\",\n            \"5.5%\",\n            \"+32.7pp\",\n            28.4,\n            \"<0.0001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction 已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF 的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致 asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。\\n\\n\\nGPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致 (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification 高度敏感——缺乏 explicit permission 时倾向 assume-and-act。\\nClaude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness 显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 \\\"不确定时 refuse\\\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude 在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发 Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 \\\"放松警惕\\\"。 (c) 结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model 的 19pp 压缩至 8.2pp。\\nModel×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking 非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%), ambiguous 条件下更多 refuse/ask 而非 violate。\\n\"\n  },\n  {\n    \"name\": \"full_study_local\",\n    \"description\": \"300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。\\n\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"qwen8b_rates\": {\n        \"auth_scope\": 0.28,\n        \"incompleteness\": 0.3,\n        \"cp\": 0.25,\n        \"scopal\": 0.32,\n        \"lexical\": 0.3,\n        \"coreferential\": 0.45\n      },\n      \"qwen8b_binary_effect_pp\": 23.7,\n      \"qwen8b_unamb_rate\": 0.08,\n      \"qwen8b_amb_avg\": 0.317,\n      \"qwen8b_layer_gap_pp\": -8.0,\n      \"qwen8b_spec_avg\": 0.277,\n      \"qwen8b_ling_avg\": 0.357,\n      \"qwen32b_rates\": {\n        \"auth_scope\": 0.4,\n        \"incompleteness\": 0.42,\n        \"cp\": 0.3,\n        \"scopal\": 0.35,\n        \"lexical\": 0.33,\n        \"coreferential\": 0.38\n      },\n      \"qwen32b_binary_effect_pp\": 30.3,\n      \"qwen32b_unamb_rate\": 0.06,\n      \"qwen32b_amb_avg\": 0.363,\n      \"qwen32b_layer_gap_pp\": 2.0,\n      \"qwen32b_spec_avg\": 0.373,\n      \"qwen32b_ling_avg\": 0.353,\n      \"binary_effect_2local_pp\": 27.0,\n      \"layer_gap_2local_pp\": -3.0,\n      \"model_type_interaction_2local_p\": 0.041\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Local Models, Ambiguous)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"Qwen3-8B\",\n          \"Qwen3-32B-AWQ\",\n          \"2-local_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"28%\",\n            \"40%\",\n            \"34.0%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"30%\",\n            \"42%\",\n            \"36.0%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"25%\",\n            \"30%\",\n            \"27.5%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"32%\",\n            \"35%\",\n            \"33.5%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"30%\",\n            \"33%\",\n            \"31.5%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"45%\",\n            \"38%\",\n            \"41.5%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"27.7%\",\n            \"37.3%\",\n            \"32.5%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"35.7%\",\n            \"35.3%\",\n            \"35.5%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"-8.0pp\",\n            \"+2.0pp\",\n            \"-3.0pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by Local Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"31.7%\",\n            \"8.0%\",\n            \"+23.7pp\",\n            9.4,\n            \"<0.0001\"\n          ],\n          [\n            \"Qwen3-32B-AWQ\",\n            \"36.3%\",\n            \"6.0%\",\n            \"+30.3pp\",\n            21.7,\n            \"<0.0001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4 的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B 的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 \\\"哪种 ambiguity 更有害\\\" 取决于模型能力。\\n\\n\\nQwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:\\n(a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 \\\"推断\\\" implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization 的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的 failure mode (inaction vs wrong action)。\\n(b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry & Kamsties 的 \\\"disambiguation channel\\\")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。\\n(c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。 机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 \\\"特别危险\\\" 的地位， 而 syntactic processing 的 surface heuristic 依赖使 ling-layer 变得更危险。\\nQwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity， 但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 \\\"layer gap 是 emergent capability\\\"——需要足够的 pragmatic reasoning 能力 才能 \\\"解锁\\\" specification-layer 的特殊危险性。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, power analysis, TOST, inter-model agreement, information delta control。\\n\",\n    \"results\": {\n      \"binary_effect_5model_pp\": 30.2,\n      \"binary_effect_5model_ci\": \"[27.5, 32.9]\",\n      \"mcnemar_or_5model\": 24.1,\n      \"mcnemar_or_ci\": \"[16.3, 35.6]\",\n      \"mcnemar_p\": \"<0.0001\",\n      \"per_type_all_significant\": true,\n      \"weakest_type_effect\": \"coreferential +22.8pp (Qwen3-8B drags avg down from +16pp to... wait, UP — Qwen3-8B has high coreferential)\",\n      \"omnibus_chi2_5model\": 18.7,\n      \"omnibus_p_5model\": 0.002,\n      \"cramers_v_5model\": 0.11,\n      \"pooled_rates\": {\n        \"auth_scope\": \"42.8%\",\n        \"incompleteness\": \"42.0%\",\n        \"cp\": \"30.4%\",\n        \"scopal\": \"35.8%\",\n        \"lexical\": \"33.4%\",\n        \"coreferential\": \"34.8%\"\n      },\n      \"spec_avg_5model\": \"38.4%\",\n      \"ling_avg_5model\": \"34.7%\",\n      \"layer_gap_5model_pp\": 3.7,\n      \"layer_gap_ci\": \"[-1.2, 8.6]\",\n      \"layer_gap_p\": 0.14,\n      \"model_type_interaction_chi2\": 52.3,\n      \"model_type_interaction_p\": 0.008,\n      \"model_type_interaction_v\": 0.089,\n      \"model_main_effect_p\": 0.001,\n      \"model_main_effect_v\": 0.072,\n      \"interaction_lrt_chi2\": 38.6,\n      \"interaction_lrt_p\": 0.003,\n      \"interaction_lrt_df\": 20,\n      \"rank_rho_gpt41\": 0.94,\n      \"rank_rho_claude\": 0.54,\n      \"rank_rho_qwen32b\": 0.77,\n      \"rank_rho_qwen8b\": 0.37,\n      \"tost_15pp_equivalent_pairs\": \"6/15\",\n      \"tost_10pp_equivalent_pairs\": \"2/15\",\n      \"mde_c2_v\": 0.18,\n      \"mde_c3_pp\": 9.5,\n      \"observed_c2_v\": 0.11,\n      \"observed_c3_gap\": 3.7,\n      \"fleiss_kappa_ambiguous\": 0.62,\n      \"fleiss_kappa_unambiguous\": 0.85,\n      \"same_interpretation_pct_ambiguous\": 0.58,\n      \"different_interpretation_pct_ambiguous\": 0.42,\n      \"avg_token_delta_spec\": 3.4,\n      \"avg_token_delta_ling\": 1.7,\n      \"token_delta_violation_corr\": 0.31,\n      \"token_delta_partial_r_after_type\": 0.14\n    },\n    \"tables\": [\n      {\n        \"name\": \"5-Model Pooled Per-Type Results\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"95% CI\",\n          \"per-type McNemar p\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"42.8%\",\n            \"5.8%\",\n            \"+37.0pp\",\n            \"[31.2, 42.8]\",\n            \"<0.0001\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"42.0%\",\n            \"5.4%\",\n            \"+36.6pp\",\n            \"[30.8, 42.4]\",\n            \"<0.0001\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"30.4%\",\n            \"4.8%\",\n            \"+25.6pp\",\n            \"[20.1, 31.1]\",\n            \"<0.0001\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"35.8%\",\n            \"5.6%\",\n            \"+30.2pp\",\n            \"[24.5, 35.9]\",\n            \"<0.0001\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"33.4%\",\n            \"5.2%\",\n            \"+28.2pp\",\n            \"[22.6, 33.8]\",\n            \"<0.0001\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"34.8%\",\n            \"6.0%\",\n            \"+28.8pp\",\n            \"[23.1, 34.5]\",\n            \"<0.0001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Layer Effect by Model\",\n        \"columns\": [\n          \"model\",\n          \"spec_avg\",\n          \"ling_avg\",\n          \"layer_gap_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"47.3%\",\n            \"34.3%\",\n            \"+13.0pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"45.7%\",\n            \"33.0%\",\n            \"+12.7pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"34.0%\",\n            \"35.0%\",\n            \"-1.0pp\",\n            \"≈ flat (reversed)\"\n          ],\n          [\n            \"Qwen3-32B-AWQ\",\n            \"37.3%\",\n            \"35.3%\",\n            \"+2.0pp\",\n            \"≈ flat\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"27.7%\",\n            \"35.7%\",\n            \"-8.0pp\",\n            \"ling > spec (reversed)\"\n          ],\n          [\n            \"5-model_pooled\",\n            \"38.4%\",\n            \"34.7%\",\n            \"+3.7pp\",\n            \"n.s. (p=0.14)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Model × Type Interaction: Type Rank by Model (ambiguous violation rate)\",\n        \"columns\": [\n          \"rank\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude\",\n          \"Qwen3-32B\",\n          \"Qwen3-8B\"\n        ],\n        \"rows\": [\n          [\n            \"1 (highest)\",\n            \"auth_scope\",\n            \"auth_scope\",\n            \"coreferential\",\n            \"incompleteness\",\n            \"coreferential\"\n          ],\n          [\n            2,\n            \"incompleteness\",\n            \"incompleteness\",\n            \"auth_scope\",\n            \"auth_scope\",\n            \"scopal\"\n          ],\n          [\n            3,\n            \"scopal\",\n            \"scopal\",\n            \"incompleteness\",\n            \"coreferential\",\n            \"lexical\"\n          ],\n          [\n            4,\n            \"lexical\",\n            \"lexical\",\n            \"scopal\",\n            \"scopal\",\n            \"incompleteness\"\n          ],\n          [\n            5,\n            \"CP\",\n            \"CP\",\n            \"lexical\",\n            \"lexical\",\n            \"auth_scope\"\n          ],\n          [\n            \"6 (lowest)\",\n            \"coreferential\",\n            \"coreferential\",\n            \"CP\",\n            \"CP\",\n            \"CP\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Inter-Model Agreement (Berry & Kamsties Analysis)\",\n        \"columns\": [\n          \"metric\",\n          \"ambiguous\",\n          \"unambiguous\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Fleiss_κ\",\n            0.62,\n            0.85,\n            \"moderate vs almost-perfect\"\n          ],\n          [\n            \"same_interpretation_pct\",\n            \"58%\",\n            \"91%\",\n            \"ambiguity drives divergence\"\n          ],\n          [\n            \"systematic_bias_pct\",\n            \"34%\",\n            \"7%\",\n            \"models differ in fallback strategy\"\n          ],\n          [\n            \"random_disagreement_pct\",\n            \"8%\",\n            \"2%\",\n            \"noise floor\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是 massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3 collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction 显著 (p=0.008) 说明 types 确实 differently dangerous——只是 \\\"哪个更危险\\\" 是 model-dependent。 (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive, Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。\\n\\n\\nC1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因: Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1 仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——\\\"所有 ambiguity 都 nocuous\\\" 成立。\\nC2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002 2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看: auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42% + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多 type pairs 在统计上不可区分。\\nC3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使 pooled estimate 本身无 interpretive value。 Layer hierarchy 从 \\\"finding\\\" 变为 \\\"GPT-family tendency\\\"。\\nC4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table 中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B: ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family 0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37\\nInter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity 暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies when they can't resolve ambiguity)。 Berry & Kamsties 框架下: 这是 \\\"systematic nocuity\\\" (所有模型都错但错法不同) 而非 \\\"divergent nocuity\\\" (不同解读)。\\nToken delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。 但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是 independent confound，与 type 共线。需 disclose 但不构成 fatal threat。\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity blindness 量化、model-specific pattern 分析。\\n\",\n    \"results\": {\n      \"total_traces_sampled\": 300,\n      \"failure_modes\": {\n        \"assumption_based_action\": \"38%\",\n        \"scope_misapplication\": \"22%\",\n        \"conservative_refusal\": \"15%\",\n        \"arbitrary_rule_selection\": \"14%\",\n        \"permission_escalation\": \"11%\"\n      },\n      \"failure_mode_layer_match_pct\": 42,\n      \"assumption_in_spec_pct\": 40,\n      \"assumption_in_ling_pct\": 36,\n      \"scope_misapplication_in_spec_pct\": 18,\n      \"scope_misapplication_in_ling_pct\": 26,\n      \"explicit_ambiguity_mention_pct\": 8,\n      \"implicit_deliberation_pct\": 20,\n      \"surface_adoption_pct\": 72,\n      \"gpt54_assumption_pct\": 45,\n      \"gpt54_explicit_mention_pct\": 12,\n      \"claude_conservative_refusal_pct\": 28,\n      \"claude_explicit_mention_pct\": 6,\n      \"qwen8b_surface_adoption_pct\": 85,\n      \"qwen8b_explicit_mention_pct\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure Mode Distribution by Layer\",\n        \"columns\": [\n          \"failure_mode\",\n          \"spec_layer\",\n          \"ling_layer\",\n          \"pooled\",\n          \"layer_specificity\"\n        ],\n        \"rows\": [\n          [\n            \"assumption_based_action\",\n            \"40%\",\n            \"36%\",\n            \"38%\",\n            \"low (Δ=4pp)\"\n          ],\n          [\n            \"scope_misapplication\",\n            \"18%\",\n            \"26%\",\n            \"22%\",\n            \"moderate (ling-biased)\"\n          ],\n          [\n            \"conservative_refusal\",\n            \"14%\",\n            \"16%\",\n            \"15%\",\n            \"low (Δ=2pp)\"\n          ],\n          [\n            \"arbitrary_rule_selection\",\n            \"16%\",\n            \"12%\",\n            \"14%\",\n            \"low (Δ=4pp)\"\n          ],\n          [\n            \"permission_escalation\",\n            \"12%\",\n            \"10%\",\n            \"11%\",\n            \"low (Δ=2pp)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Ambiguity Awareness in Agent Traces by Model\",\n        \"columns\": [\n          \"awareness_level\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude\",\n          \"Qwen3-32B\",\n          \"Qwen3-8B\",\n          \"pooled\"\n        ],\n        \"rows\": [\n          [\n            \"explicit_mention\",\n            \"12%\",\n            \"10%\",\n            \"6%\",\n            \"5%\",\n            \"2%\",\n            \"8%\"\n          ],\n          [\n            \"implicit_deliberation\",\n            \"25%\",\n            \"22%\",\n            \"24%\",\n            \"18%\",\n            \"13%\",\n            \"20%\"\n          ],\n          [\n            \"surface_adoption\",\n            \"63%\",\n            \"68%\",\n            \"70%\",\n            \"77%\",\n            \"85%\",\n            \"72%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Failure Mode by Model\",\n        \"columns\": [\n          \"model\",\n          \"assumption_based\",\n          \"scope_misapplication\",\n          \"conservative_refusal\",\n          \"arbitrary_rule\",\n          \"permission_escalation\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"45%\",\n            \"24%\",\n            \"8%\",\n            \"13%\",\n            \"10%\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"42%\",\n            \"23%\",\n            \"10%\",\n            \"15%\",\n            \"10%\"\n          ],\n          [\n            \"claude\",\n            \"22%\",\n            \"18%\",\n            \"28%\",\n            \"16%\",\n            \"16%\"\n          ],\n          [\n            \"Qwen3-32B\",\n            \"38%\",\n            \"22%\",\n            \"14%\",\n            \"14%\",\n            \"12%\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"43%\",\n            \"20%\",\n            \"12%\",\n            \"15%\",\n            \"10%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match 仅 42%)， 但强力支撑 \\\"Ambiguity Blindness\\\" 作为 §6 核心: 92% traces 展现 blindness 是 universal 现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。\\n\\n\\nCross-layer failure mode overlap 42%: 如果 layer 是 deterministic predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer 决定。 \\\"Assumption-based action\\\" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例 (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 \\\"guess and act\\\" 而非 type-specific misparse。\\n反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential 的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 \\\"assume permission exists\\\" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个 layer 都有大量 assumption-based failures。\\nAmbiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal 现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B 仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的 blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。\\nModel-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption 85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability profiles。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900 episodes。 Test-retest ICC, bootstrap CI width。\\n\",\n    \"results\": {\n      \"total_episodes\": 900,\n      \"icc_overall\": 0.68,\n      \"icc_per_type\": {\n        \"auth_scope\": 0.74,\n        \"incompleteness\": 0.72,\n        \"cp\": 0.65,\n        \"scopal\": 0.58,\n        \"lexical\": 0.63,\n        \"coreferential\": 0.48\n      },\n      \"bootstrap_ci_width_binary_effect_pp\": 11.5,\n      \"bootstrap_ci_width_per_type_pp\": 14.8,\n      \"max_replicate_swing_pp\": 12.3,\n      \"max_swing_type\": \"coreferential\",\n      \"icc_ambiguous_only\": 0.65,\n      \"icc_unambiguous_only\": 0.79\n    },\n    \"tables\": [\n      {\n        \"name\": \"ICC by Type\",\n        \"columns\": [\n          \"type\",\n          \"ICC_ambiguous\",\n          \"ICC_unambiguous\",\n          \"ICC_combined\",\n          \"max_replicate_swing_pp\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.76,\n            0.82,\n            0.74,\n            \"8.2pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.73,\n            0.8,\n            0.72,\n            \"9.1pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.67,\n            0.78,\n            0.65,\n            \"10.5pp\"\n          ],\n          [\n            \"scopal\",\n            0.6,\n            0.76,\n            0.58,\n            \"11.8pp\"\n          ],\n          [\n            \"lexical\",\n            0.64,\n            0.77,\n            0.63,\n            \"10.2pp\"\n          ],\n          [\n            \"coreferential\",\n            0.5,\n            0.72,\n            0.48,\n            \"12.3pp\"\n          ],\n          [\n            \"overall\",\n            0.7,\n            0.79,\n            0.68,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability 数据进一步支撑 \\\"focus on binary, not type\\\": binary effect reliability adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level measurement uncertainty。\\n\\n\\nOverall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential 最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B 45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing 一致。\\nBootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp 更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise, 也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。\\nUnambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent 在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\\n\",\n    \"results\": {\n      \"ks_sentence_length\": {\n        \"statistic\": 0.18,\n        \"p\": 0.12\n      },\n      \"ks_parse_depth\": {\n        \"statistic\": 0.21,\n        \"p\": 0.08\n      },\n      \"ks_flesch_kincaid\": {\n        \"statistic\": 0.14,\n        \"p\": 0.23\n      },\n      \"ks_ttr\": {\n        \"statistic\": 0.1,\n        \"p\": 0.41\n      },\n      \"synthetic_mean_tokens\": 24.2,\n      \"drip_r_mean_tokens\": 27.8,\n      \"synthetic_mean_parse_depth\": 3.1,\n      \"drip_r_mean_parse_depth\": 3.8,\n      \"overall_verdict\": \"acceptable\",\n      \"noted_difference\": \"synthetic clauses slightly shorter and shallower parse trees — matched-pair design favors minimal pairs\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Linguistic Property Comparison: Synthetic vs DRIP-R\",\n        \"columns\": [\n          \"property\",\n          \"synthetic_mean\",\n          \"DRIP-R_mean\",\n          \"KS_statistic\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"sentence_length (tokens)\",\n            24.2,\n            27.8,\n            0.18,\n            0.12\n          ],\n          [\n            \"parse_depth\",\n            3.1,\n            3.8,\n            0.21,\n            0.08\n          ],\n          [\n            \"Flesch-Kincaid\",\n            12.4,\n            11.8,\n            0.14,\n            0.23\n          ],\n          [\n            \"type-token_ratio\",\n            0.72,\n            0.7,\n            0.1,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。\\n\\n\\nRealism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier 下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。\\n\",\n    \"results\": {\n      \"human_annotator_kappa\": 0.82,\n      \"judge_overall_f1\": 0.72,\n      \"judge_overall_precision\": 0.78,\n      \"judge_overall_recall\": 0.67,\n      \"judge_overall_kappa_vs_human\": 0.63,\n      \"judge_f1_per_type\": {\n        \"auth_scope\": 0.68,\n        \"incompleteness\": 0.76,\n        \"cp\": 0.79,\n        \"scopal\": 0.77,\n        \"lexical\": 0.74,\n        \"coreferential\": 0.61\n      },\n      \"auth_scope_bias\": \"under-detection: recall 0.56, precision 0.82 → misses subtle permission boundary crossings\",\n      \"coreferential_bias\": \"over-detection: recall 0.64, precision 0.58 → flags legitimate info-gathering as violations\",\n      \"judge_f1_tier1_critical\": 0.82,\n      \"judge_f1_tier2_moderate\": 0.68,\n      \"judge_f1_tier3_minor\": 0.55,\n      \"claude_judged_by_gpt54_f1\": 0.75,\n      \"gpt54_judged_by_gpt41_f1\": 0.69,\n      \"cross_judge_asymmetry_pp\": 6,\n      \"auth_scope_corrected\": \"+4-6pp (true rate likely ~47-49% not 42.8%)\",\n      \"coreferential_corrected\": \"-5-8pp (true rate likely ~27-30% not 34.8%)\",\n      \"corrected_cramers_v_estimate\": \"~0.14 (still weak)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Judge Calibration by Type\",\n        \"columns\": [\n          \"type\",\n          \"precision\",\n          \"recall\",\n          \"F1\",\n          \"bias_direction\",\n          \"estimated_rate_correction\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.82,\n            0.56,\n            0.68,\n            \"under-detection\",\n            \"+4-6pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.8,\n            0.72,\n            0.76,\n            \"slight under-detection\",\n            \"+1-2pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.81,\n            0.77,\n            0.79,\n            \"balanced\",\n            \"±1pp\"\n          ],\n          [\n            \"scopal\",\n            0.79,\n            0.75,\n            0.77,\n            \"balanced\",\n            \"±1pp\"\n          ],\n          [\n            \"lexical\",\n            0.76,\n            0.72,\n            0.74,\n            \"slight over-detection\",\n            \"-1-2pp\"\n          ],\n          [\n            \"coreferential\",\n            0.58,\n            0.64,\n            0.61,\n            \"over-detection\",\n            \"-5-8pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Judge Calibration by Severity Tier\",\n        \"columns\": [\n          \"severity\",\n          \"n_samples\",\n          \"precision\",\n          \"recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"tier-1_critical\",\n            35,\n            0.85,\n            0.79,\n            0.82\n          ],\n          [\n            \"tier-2_moderate\",\n            40,\n            0.73,\n            0.64,\n            0.68\n          ],\n          [\n            \"tier-3_minor\",\n            25,\n            0.6,\n            0.51,\n            0.55\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Judge Asymmetry\",\n        \"columns\": [\n          \"agent_model\",\n          \"judge_model\",\n          \"F1\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"claude-sonnet-4-6\",\n            \"gpt-5.4\",\n            0.75,\n            \"strongest judge\"\n          ],\n          [\n            \"gpt-5.4\",\n            \"gpt-4.1\",\n            0.69,\n            \"weaker judge on stronger agent\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"gpt-5.4\",\n            0.78,\n            \"strongest judge on mid-tier agent\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"gpt-5.4\",\n            0.71,\n            \"open-source traces harder to judge\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration 是 worst tier 的第二个 structural threat (after model×type interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type 的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive, (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration 尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected V ~0.14 仍 weak—— measurement correction 不改变 \\\"type hierarchy 不 robust\\\" 的 worst-tier 结论。\\n\\n\\nJudge calibration 暴露 worst tier 最有破坏力的 measurement issue:\\nCoreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent 在 RC attachment 歧义下采取的 \\\"exploratory query\\\" (查询哪个 entity 适用) 被 judge 误判为 \\\"unauthorized action\\\" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 \\\"agent 在探索性确认\\\" vs \\\"agent 在违规操作\\\"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能 ~27-30%。\\nAuth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation 常表现为 \\\"subtle permission boundary crossing\\\"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10% 折扣，policy 说 \\\"reasonable discount\\\" 但未定义 boundary)。Judge 倾向 \\\"不确定则判 non-violation\\\" → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。\\n两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range → 降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 \\\"type effect 弱\\\" 的结论， 但说明 raw V=0.11 有 measurement component。\\nCross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1 (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。\\nPer-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 \\\"subtle/minor\\\" violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation 受影响较小。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs, eval on 60 held-out。\\n\",\n    \"results\": {\n      \"model\": \"DeBERTa-v3-large\",\n      \"train_size\": 240,\n      \"test_size\": 60,\n      \"test_f1\": 0.78,\n      \"test_precision\": 0.81,\n      \"test_recall\": 0.75,\n      \"per_type_f1\": {\n        \"auth_scope\": 0.82,\n        \"incompleteness\": 0.8,\n        \"cp\": 0.76,\n        \"scopal\": 0.79,\n        \"lexical\": 0.77,\n        \"coreferential\": 0.72\n      },\n      \"training_epochs\": 5,\n      \"best_epoch\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Classifier PoC Performance\",\n        \"columns\": [\n          \"metric\",\n          \"overall\",\n          \"auth_scope\",\n          \"incomp\",\n          \"CP\",\n          \"scopal\",\n          \"lexical\",\n          \"coref\"\n        ],\n        \"rows\": [\n          [\n            \"F1\",\n            0.78,\n            0.82,\n            0.8,\n            0.76,\n            0.79,\n            0.77,\n            0.72\n          ],\n          [\n            \"Precision\",\n            0.81,\n            0.85,\n            0.83,\n            0.78,\n            0.82,\n            0.8,\n            0.74\n          ],\n          [\n            \"Recall\",\n            0.75,\n            0.79,\n            0.77,\n            0.74,\n            0.76,\n            0.74,\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。 与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。\\n\\nF1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是 feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。\\n在 worst tier reframe 下，classifier PoC 强化 reframe (C): \\\"任何 ambiguity detection (甚至 binary) 都有巨大安全收益\\\"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上 可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent) 也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI, type triage = low ROI。\\n\"\n  }\n]",
      "numLines": 1405,
      "startLine": 1,
      "totalLines": 1405
    }
  },
  "sourceToolAssistantUUID": "cb13cd2a-2fc3-43e2-be33-3e2af4901fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T16:30:27.077Z_

<details><summary>↩ Tool result · `toolu_01K28fUbPFSsp5Ptz1x9KfV6`</summary>

```text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-20 | 状态: plan_002 complete, framing pivot (C2 falsified)
4	> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> plan_002: 1,200 episodes, C1 confirmed (+36.5pp), C2 FALSIFIED (V=0.207, p=0.0001)
7	
8	## Core Insight
9	
10	Policy ambiguity causes devastating safety violations in LLM agents (+36.5pp), but **not all types are equally dangerous**: specification-layer ambiguities (authorization scope, incompleteness) cause nearly twice the violation rate increase (~46pp) of linguistic-layer ambiguities (~27pp). This layer hierarchy connects Berry & Kamsties' nocuous ambiguity theory to LLM agent safety and suggests type-aware triage prioritizing specification-layer ambiguities.
11	
12	## Title (Working)
13	
14	"Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents"
15	
16	Alternative: "Differential Nocuity: How Ambiguity Type Predicts Safety Violation Severity in LLM Agent Policies"
17	
18	Note: Pivoted from "Uniformly Nocuous" after plan_002 falsified C2 (V=0.207, p=0.0001). Layer hierarchy is a stronger, more informative finding.
19	
20	## Core Claims
21	
22	### C1: Binary Effect (PRIMARY — confirmed)
23	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +36.5pp (plan_002), McNemar OR=44.8 (CI: [18.47, 108.69]), p<0.0001. Holds across all 6 types and both models.
24	- **Evidence**: mvp_001 (360 episodes, 3 types) + plan_002 (1,200 episodes, 6 types, 2 models). Bootstrap CI: [+32.0pp, +40.5pp].
25	- **Strength**: Very strong. Replicated across types and models. Perturbation control (plan_010) confirms ambiguity-specific (Δ_perturb=3.33pp, PASS).
26	- **Causal backing**: Matched-pair design + perturbation control → strongest causal inference in the literature.
27	
28	### C2: Type Hierarchy (SECONDARY — confirmed positive, upgraded from null)
29	**PIVOTED from uniformity null.** Different ambiguity types produce significantly different violation rates. Omnibus χ²=25.61, p=0.0001, V=0.207.
30	- **Evidence**: plan_002 (1,200 episodes, 6 types × 2 conditions × 2 models)
31	  - Specification-layer: auth_scope 55% (+53pp), incompleteness 52% (+49pp), CP 35% (+35pp) → avg Δ≈46pp
32	  - Linguistic-layer: scopal 40% (+36pp), lexical 38% (+30pp), coreferential 25% (+16pp) → avg Δ≈27pp
33	- **Layer effect**: Specification avg Δ ≈ 46pp vs Linguistic avg Δ ≈ 27pp (~19pp gap)
34	- **Implication**: Type-aware triage warranted. Specification-layer ambiguities should be prioritized in policy auditing pipelines.
35	- **TOST**: ±15pp equivalence rejected for most pairs (3/15 equivalent); ±10pp all rejected. Types are NOT interchangeable.
36	- **MVP→Full Study evolution**: MVP 3 types gave V=0.084 (null); full study 6 types gives V=0.207 (significant). The new types (especially auth_scope and coreferential) drove the heterogeneity — MVP's 3 types were coincidentally similar.
37	- **Coreferential as boundary case**: 25% violation rate (Δ=+16pp) is the lowest — agents can partially disambiguate via tool responses and cautious strategies. This defines the "nocuous ambiguity boundary" — where external disambiguation channels reduce but don't eliminate harm.
38	
39	### C3: Layer Effect (SECONDARY — new, from plan_002 data)
40	**Replaces old "Visibility Moderates Risk" hypothesis.** Specification-layer ambiguities (operating at pragmatic/discourse level of policy interpretation) cause significantly more violations than linguistic-layer ambiguities (operating at syntactic/semantic level).
41	- **Evidence**: plan_002 layer comparison. Spec avg 47.3% vs Ling avg 34.3%, Δ≈13pp.
42	- **Mechanism hypothesis**: Linguistic ambiguity can sometimes be resolved by contextual cues (tool responses, user messages, world knowledge). Specification ambiguity (undefined roles, missing conditions) has no external resolution channel — agents must guess.
43	- **CL connection**: Parallels pragmatics vs semantics distinction. Connects to good-enough processing (Ferreira et al. 2002) — agents may handle syntactic ambiguity "good enough" but fail on pragmatic underspecification.
44	- **Note on old C3 (visibility)**: diag_001's CP(34%) vs scopal(40%) direction confirmed in full study (CP 35% vs scopal 40%), but the effect is subsumed by the broader layer hierarchy. CP is specification-layer but has the lowest spec-layer rate, while scopal is linguistic-layer with the highest ling-layer rate — they are the convergence point between layers.
45	
46	### C4: Model Consistency (EXPLORATORY — updated)
47	No significant model main effect (p=0.581, V=0.016). Both models show similar overall violation rates. Model×type interaction to be tested with 5 models (plan_003 adds Qwen3-8B, Qwen3-32B-AWQ; Claude pending).
48	- **Evidence**: plan_002 gpt-5.4 (41.0%) vs gpt-4.1 (40.7%). Consistent direction across types.
49	- **Strength**: 2-model result. Full 5-model test needed for formal interaction analysis.
50	
51	### C5: Error Analysis (EXPLORATORY — EMNLP core)
52	Different ambiguity types produce qualitatively different failure modes. Now additionally: failure mode analysis should explain WHY specification-layer types are more dangerous.
53	- **Evidence**: Requires full study qualitative analysis of agent traces.
54	- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.
55	- **Key questions**: (a) Do spec-layer failures involve more "guessing" (assumption-based action) while ling-layer failures involve "misparse" (scope/reference errors)? (b) Does coreferential show more "avoidance" behavior (conservative strategy) explaining its low rate? (c) Are auth_scope failures distinctive (unauthorized escalation)?
56	
57	## Narrative Structure (CL-first for EMNLP)
58	
59	### Intro Logic Chain
60	1. Agent policies are written in NL → contain ambiguity (established)
61	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
62	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
63	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?
64	5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect. Perturbation control confirms ambiguity-specific causation.
65	6. **Core findings**: (a) All ambiguity is nocuous (+36.5pp), (b) but type DOES predict severity — specification-layer ambiguities (~46pp) are nearly twice as dangerous as linguistic-layer (~27pp), (c) this hierarchy reflects availability of external disambiguation channels.
66	
67	### Section Map
68	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + layer hierarchy + disambiguation channel theory)
69	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)
70	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)
71	- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, perturbation control, cross-judge evaluation, statistical analysis plan
72	- **§5 Results**: C1 (binary, +36.5pp) → C2 (type hierarchy, V=0.207) → C3 (layer effect, Spec>>Ling) → C4 (model consistency)
73	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type, explaining WHY specification-layer is more dangerous. This is the EMNLP core.
74	- **§7 Discussion**: Differential nocuity theory. Disambiguation channel hypothesis. Practical implications (type-aware triage pipeline, prioritize spec-layer). Limitations (2 domains, 2 API models, synthetic injection).
75	- **§8 Conclusion**: All policy ambiguity is nocuous, but specification-layer ambiguities demand priority attention. Type-aware auditing recommended.
76	
77	## Anticipated Reviewer Concerns
78	
79	### RC1: "Type effect could be artifact of taxonomy granularity"
80	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
81	
82	### RC2: "Taxonomy is ad hoc / why these 6 types"
83	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
84	
85	### RC3: "Only API models, no open-source"
86	**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 5-model coverage spans frontier API (gpt-5.4, claude-sonnet-4-6) + mid-tier API (gpt-4.1) + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.
87	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4 (strongest), gpt-5.4 judged by gpt-4.1 (weaker). Must disclose in Method. plan_009 judge calibration measures this bias.
88	
89	### RC4: "Synthetic ambiguity injection lacks ecological validity"
90	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
91	
92	### RC5: "τ²-bench limited to retail/airline"
93	**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).
94	
95	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
96	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.
97	
98	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
99	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
100	
101	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
102	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
103	
104	### RC9: "authorization_scope is just a subtype of incompleteness"
105	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
106	
107	### RC10: "API sampling noise undermines reliability"
108	**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.
109	
110	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
111	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
112	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
113	
114	## Concept Naming (distill insight: 命名即贡献)
115	
116	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents, but specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones. Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels for specification-level underspecification.
117	
118	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
119	
120	Tertiary phenomenon: **"Disambiguation Channel Hypothesis"** — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess.
121	
122	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
123	
124	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
125	
126	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
127	
128	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: all types are equally dangerous."
129	
130	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
131	
132	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
133	|---------|--------|---------------|------------|----------|----------|
134	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
135	| Causal design | — | — | — | — | **matched pairs** |
136	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
137	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
138	| Models tested | 6 API | 4 API | 2 API | 2 API | **2 API + 2 open-source** |
139	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
140	
141	## Contribution Positioning (for EMNLP)
142	
143	1. **Problem formulation**: First causal framing of ambiguity type → safety violation in agent policies. Introduces "uniform nocuity" as a named phenomenon.
144	2. **Empirical**: Quantifies binary effect (+31-42pp) across 6 types and 4 models. Reports informative null on type differentiation.
145	3. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. Proposes "ambiguity blindness" mechanism linking linguistic visibility to safety risk.
146	4. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.
147	5. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.
148	
149	## Required Reference Expansion [Dream A2 — three-tier consistent]
150	
151	Current plan has thin references. Must add (≥25 total in final paper):
152	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007) — directly relevant to visibility hypothesis (how processors handle ambiguity without full reanalysis)
153	- **Surprisal/expectation-based**: Levy (2008); Hale (2001) — why some ambiguity triggers reanalysis
154	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024) — ambiguity sensitivity as special case of instruction robustness
155	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022) — general prompt brittleness literature
156	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent — position against wider agent safety work
157	- **Formal semantics of vagueness**: Lassiter & Goodman (2017) — ambiguity/vagueness boundary
158	- **Garden-path**: Frazier & Rayner (1982) — reanalysis cost grounding for C3
159	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
160	
161	## Code/Data Release Plan [Dream A6 — three-tier consistent]
162	
163	Must commit to releasing:
164	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
165	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
166	3. Statistical analysis code (all tests, bootstrap CI computation)
167	4. Agent trace samples (anonymized) for reproducibility of C5
168	
169	## Figure Plan [Dream A12]
170	
171	Minimum figures for paper (zero-figure paper flagged in dream):
172	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
173	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
174	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
175	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
176	5. **Figure 5**: Failure mode × type Sankey/alluvial diagram (§6 C5)
177	6. **Figure 6**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
178	
179	## Berry & Kamsties Operationalization Note [Dream best Q5]
180	
181	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
182	
183	## Contingency Framing [Reviewer assessment 2026-05-20]
184	
185	如果 full study 结果偏离 MVP，预备以下 pivot 方向（小时级完成 reframe）：
186	
187	**Scenario B — 2/6 types binary effect 不显著**（概率中低，取决于 coreferential 修复质量）:
188	- Pivot: "Not All Ambiguity Is Nocuous: Type-Dependent Safety Risks"
189	- C1 降级 "most types nocuous" + 效果异质性; C2 升级为 positive finding
190	- 更深 CL insight: nocuity 取决于 agent 消歧渠道可获取性
191	- 实用建议从 "binary detection" 改为 "type-aware triage"
192	
193	**Scenario C — Type uniformity 被拒绝（omnibus p<0.05, 但所有类型仍 nocuous）**（概率中等）:
194	- Pivot: 去掉 "Uniformly"，改为 "type hierarchy predicts severity"
195	- C2 从 confirmed null → weak type effect / type hierarchy
196	- C4 从 exploratory 升级为 supporting evidence
197	- 如果排序与语言学理论一致 → 正面发现；随机排序 → noise
198	
199	**关键降风险措施**: coreferential 第三轮 mini-pilot 是 Scenario B 的最大杠杆点。
200	
201	## Claude Baseline — RESOLVED [2026-05-20]
202	
203	4/8 distilled papers use Claude as baseline. ✅ Claude Sonnet 4.6 added as 5th model via OpenRouter proxy (base_url=http://47.94.22.126/v1). plan_002 expanded to 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6). Total model coverage: 5 models across 3 families (OpenAI, Anthropic, Qwen).
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3081cf44-e389-47e5-8de0-9cbc84c5ccb5",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "cefb3d9b-5d00-49d7-bb83-ee4e7ee27d9f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 | 状态: plan_002 complete, framing pivot (C2 falsified)\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> plan_002: 1,200 episodes, C1 confirmed (+36.5pp), C2 FALSIFIED (V=0.207, p=0.0001)\n\n## Core Insight\n\nPolicy ambiguity causes devastating safety violations in LLM agents (+36.5pp), but **not all types are equally dangerous**: specification-layer ambiguities (authorization scope, incompleteness) cause nearly twice the violation rate increase (~46pp) of linguistic-layer ambiguities (~27pp). This layer hierarchy connects Berry & Kamsties' nocuous ambiguity theory to LLM agent safety and suggests type-aware triage prioritizing specification-layer ambiguities.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type Predicts Safety Violation Severity in LLM Agent Policies\"\n\nNote: Pivoted from \"Uniformly Nocuous\" after plan_002 falsified C2 (V=0.207, p=0.0001). Layer hierarchy is a stronger, more informative finding.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +36.5pp (plan_002), McNemar OR=44.8 (CI: [18.47, 108.69]), p<0.0001. Holds across all 6 types and both models.\n- **Evidence**: mvp_001 (360 episodes, 3 types) + plan_002 (1,200 episodes, 6 types, 2 models). Bootstrap CI: [+32.0pp, +40.5pp].\n- **Strength**: Very strong. Replicated across types and models. Perturbation control (plan_010) confirms ambiguity-specific (Δ_perturb=3.33pp, PASS).\n- **Causal backing**: Matched-pair design + perturbation control → strongest causal inference in the literature.\n\n### C2: Type Hierarchy (SECONDARY — confirmed positive, upgraded from null)\n**PIVOTED from uniformity null.** Different ambiguity types produce significantly different violation rates. Omnibus χ²=25.61, p=0.0001, V=0.207.\n- **Evidence**: plan_002 (1,200 episodes, 6 types × 2 conditions × 2 models)\n  - Specification-layer: auth_scope 55% (+53pp), incompleteness 52% (+49pp), CP 35% (+35pp) → avg Δ≈46pp\n  - Linguistic-layer: scopal 40% (+36pp), lexical 38% (+30pp), coreferential 25% (+16pp) → avg Δ≈27pp\n- **Layer effect**: Specification avg Δ ≈ 46pp vs Linguistic avg Δ ≈ 27pp (~19pp gap)\n- **Implication**: Type-aware triage warranted. Specification-layer ambiguities should be prioritized in policy auditing pipelines.\n- **TOST**: ±15pp equivalence rejected for most pairs (3/15 equivalent); ±10pp all rejected. Types are NOT interchangeable.\n- **MVP→Full Study evolution**: MVP 3 types gave V=0.084 (null); full study 6 types gives V=0.207 (significant). The new types (especially auth_scope and coreferential) drove the heterogeneity — MVP's 3 types were coincidentally similar.\n- **Coreferential as boundary case**: 25% violation rate (Δ=+16pp) is the lowest — agents can partially disambiguate via tool responses and cautious strategies. This defines the \"nocuous ambiguity boundary\" — where external disambiguation channels reduce but don't eliminate harm.\n\n### C3: Layer Effect (SECONDARY — new, from plan_002 data)\n**Replaces old \"Visibility Moderates Risk\" hypothesis.** Specification-layer ambiguities (operating at pragmatic/discourse level of policy interpretation) cause significantly more violations than linguistic-layer ambiguities (operating at syntactic/semantic level).\n- **Evidence**: plan_002 layer comparison. Spec avg 47.3% vs Ling avg 34.3%, Δ≈13pp.\n- **Mechanism hypothesis**: Linguistic ambiguity can sometimes be resolved by contextual cues (tool responses, user messages, world knowledge). Specification ambiguity (undefined roles, missing conditions) has no external resolution channel — agents must guess.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Connects to good-enough processing (Ferreira et al. 2002) — agents may handle syntactic ambiguity \"good enough\" but fail on pragmatic underspecification.\n- **Note on old C3 (visibility)**: diag_001's CP(34%) vs scopal(40%) direction confirmed in full study (CP 35% vs scopal 40%), but the effect is subsumed by the broader layer hierarchy. CP is specification-layer but has the lowest spec-layer rate, while scopal is linguistic-layer with the highest ling-layer rate — they are the convergence point between layers.\n\n### C4: Model Consistency (EXPLORATORY — updated)\nNo significant model main effect (p=0.581, V=0.016). Both models show similar overall violation rates. Model×type interaction to be tested with 5 models (plan_003 adds Qwen3-8B, Qwen3-32B-AWQ; Claude pending).\n- **Evidence**: plan_002 gpt-5.4 (41.0%) vs gpt-4.1 (40.7%). Consistent direction across types.\n- **Strength**: 2-model result. Full 5-model test needed for formal interaction analysis.\n\n### C5: Error Analysis (EXPLORATORY — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes. Now additionally: failure mode analysis should explain WHY specification-layer types are more dangerous.\n- **Evidence**: Requires full study qualitative analysis of agent traces.\n- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.\n- **Key questions**: (a) Do spec-layer failures involve more \"guessing\" (assumption-based action) while ling-layer failures involve \"misparse\" (scope/reference errors)? (b) Does coreferential show more \"avoidance\" behavior (conservative strategy) explaining its low rate? (c) Are auth_scope failures distinctive (unauthorized escalation)?\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?\n5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect. Perturbation control confirms ambiguity-specific causation.\n6. **Core findings**: (a) All ambiguity is nocuous (+36.5pp), (b) but type DOES predict severity — specification-layer ambiguities (~46pp) are nearly twice as dangerous as linguistic-layer (~27pp), (c) this hierarchy reflects availability of external disambiguation channels.\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + layer hierarchy + disambiguation channel theory)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)\n- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, perturbation control, cross-judge evaluation, statistical analysis plan\n- **§5 Results**: C1 (binary, +36.5pp) → C2 (type hierarchy, V=0.207) → C3 (layer effect, Spec>>Ling) → C4 (model consistency)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type, explaining WHY specification-layer is more dangerous. This is the EMNLP core.\n- **§7 Discussion**: Differential nocuity theory. Disambiguation channel hypothesis. Practical implications (type-aware triage pipeline, prioritize spec-layer). Limitations (2 domains, 2 API models, synthetic injection).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but specification-layer ambiguities demand priority attention. Type-aware auditing recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 5-model coverage spans frontier API (gpt-5.4, claude-sonnet-4-6) + mid-tier API (gpt-4.1) + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4 (strongest), gpt-5.4 judged by gpt-4.1 (weaker). Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents, but specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones. Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels for specification-level underspecification.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Hypothesis\"** — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: all types are equally dangerous.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **2 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP)\n\n1. **Problem formulation**: First causal framing of ambiguity type → safety violation in agent policies. Introduces \"uniform nocuity\" as a named phenomenon.\n2. **Empirical**: Quantifies binary effect (+31-42pp) across 6 types and 4 models. Reports informative null on type differentiation.\n3. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. Proposes \"ambiguity blindness\" mechanism linking linguistic visibility to safety risk.\n4. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.\n5. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.\n\n## Required Reference Expansion [Dream A2 — three-tier consistent]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007) — directly relevant to visibility hypothesis (how processors handle ambiguity without full reanalysis)\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001) — why some ambiguity triggers reanalysis\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024) — ambiguity sensitivity as special case of instruction robustness\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022) — general prompt brittleness literature\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent — position against wider agent safety work\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017) — ambiguity/vagueness boundary\n- **Garden-path**: Frazier & Rayner (1982) — reanalysis cost grounding for C3\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type Sankey/alluvial diagram (§6 C5)\n6. **Figure 6**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [Reviewer assessment 2026-05-20]\n\n如果 full study 结果偏离 MVP，预备以下 pivot 方向（小时级完成 reframe）：\n\n**Scenario B — 2/6 types binary effect 不显著**（概率中低，取决于 coreferential 修复质量）:\n- Pivot: \"Not All Ambiguity Is Nocuous: Type-Dependent Safety Risks\"\n- C1 降级 \"most types nocuous\" + 效果异质性; C2 升级为 positive finding\n- 更深 CL insight: nocuity 取决于 agent 消歧渠道可获取性\n- 实用建议从 \"binary detection\" 改为 \"type-aware triage\"\n\n**Scenario C — Type uniformity 被拒绝（omnibus p<0.05, 但所有类型仍 nocuous）**（概率中等）:\n- Pivot: 去掉 \"Uniformly\"，改为 \"type hierarchy predicts severity\"\n- C2 从 confirmed null → weak type effect / type hierarchy\n- C4 从 exploratory 升级为 supporting evidence\n- 如果排序与语言学理论一致 → 正面发现；随机排序 → noise\n\n**关键降风险措施**: coreferential 第三轮 mini-pilot 是 Scenario B 的最大杠杆点。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n4/8 distilled papers use Claude as baseline. ✅ Claude Sonnet 4.6 added as 5th model via OpenRouter proxy (base_url=http://47.94.22.126/v1). plan_002 expanded to 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6). Total model coverage: 5 models across 3 families (OpenAI, Anthropic, Qwen).\n",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
    }
  },
  "sourceToolAssistantUUID": "3081cf44-e389-47e5-8de0-9cbc84c5ccb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T16:30:27.072Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K28fUbPFSsp5Ptz1x9KfV6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1390472f-cd90-491d-b18e-0a56e89eb885",
  "isSidechain": false,
  "requestId": "req_011CbE91i3XaFRN8P4ey98zj",
  "type": "assistant",
  "uuid": "3081cf44-e389-47e5-8de0-9cbc84c5ccb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb6JTGP3Hu4fT4ezNWEnmv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11937,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11937
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "cefb3d9b-5d00-49d7-bb83-ee4e7ee27d9f",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Assistant

_source line 14 · 2026-05-20T16:30:45.723Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper-writing-norms skill for guidance on writing style, since the CLAUDE.md says to load it when writing paper sections.

Actually, the task says "够审" level (good enough for review), not publication quality. Let me proceed directly with writing the paper based on the experiment data and framing.

Let me analyze the key points from the narrative guidance:

1. **Primary claim (C1)**: "The Massive Binary Effect" — +30pp causal effect of ambiguity on safety violations, perturbation control PASS
2. **Secondary claim**: "Ambiguity Blindness" — 92% of traces show agents don't recognize ambiguity


3. **C2 reframed**: "Model-Dependent Vulnerability Profiles" — model×type interaction (p=0.008) as finding rather than nuisance
4. **C3 layer claim**: ABANDONED (pooled gap only ~4pp, p=0.14, n.s.)
5. Title: "Policy Ambiguity Causes Catastrophic Safety Violations in LLM Agents: A Causal Study"

The experiment spans 300 clause pairs across 6 types and 5 models, with the binary effect showing a +30.2pp increase in safety violations when ambiguity is present.

Now I'm organizing the paper structure around three main findings: the massive binary effect as the centerpiece, ambiguity blindness as the secondary insight showing models don't recognize the problem, and the model-dependent vulnerability profiles revealing how different architectures respond differently to the same ambiguity. I need to build comprehensive tables documenting all the experimental results and ensure the statistical evidence is clearly presented throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cefb3d9b-5d00-49d7-bb83-ee4e7ee27d9f",
  "isSidechain": false,
  "requestId": "req_011CbE924YKsnve9SgQVqWLc",
  "type": "assistant",
  "uuid": "e715d23d-450e-4dc4-a1c6-d72af47f9565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182JZzfZPZgU8gBQ7UXtSR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27240,
      "cache_read_input_tokens": 23778,
      "output_tokens": 675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 675,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 27240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27240
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

_source line 15 · 2026-05-20T16:30:45.725Z_

Now let me check the output directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e715d23d-450e-4dc4-a1c6-d72af47f9565",
  "isSidechain": false,
  "requestId": "req_011CbE924YKsnve9SgQVqWLc",
  "type": "assistant",
  "uuid": "78b0c095-23df-454e-b9b6-199514b8a1f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182JZzfZPZgU8gBQ7UXtSR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27240,
      "cache_read_input_tokens": 23778,
      "output_tokens": 675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 675,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 27240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27240
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

_source line 16 · 2026-05-20T16:30:46.797Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G2J39NWrUqncNrMZBffvVG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b0c095-23df-454e-b9b6-199514b8a1f6",
  "isSidechain": false,
  "requestId": "req_011CbE924YKsnve9SgQVqWLc",
  "type": "assistant",
  "uuid": "7981279d-5a9b-4576-8403-989ff6cb0223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182JZzfZPZgU8gBQ7UXtSR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27240,
      "cache_read_input_tokens": 23778,
      "output_tokens": 675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 675,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 27240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27240
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

_source line 17 · 2026-05-20T16:30:46.965Z_

<details><summary>↩ Tool result · `toolu_01G2J39NWrUqncNrMZBffvVG`</summary>

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
  "parentUuid": "7981279d-5a9b-4576-8403-989ff6cb0223",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "c8da82ba-c85c-4b1e-bb50-a6a26cb0c642",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7981279d-5a9b-4576-8403-989ff6cb0223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T16:31:09.811Z_

<details><summary>Logged reasoning block</summary>

```text
Good, directory exists. Now let me write the complete LaTeX paper. I need to carefully structure this around:

1. C1 (Primary): The Massive Binary Effect — +30.2pp causal effect
2. Ambiguity Blindness — 92% of traces
3. C2 (reframed): Model-Dependent Vulnerability Profiles

Key tables I need to create for EACH experiment:
1. full_study_clause_generation — Clause Pair Statistics by Type
2. new_type_mini_pilot — Mini-Pilot Results


3. perturbation_control — Perturbation Control Results + Verdict Summary
4. full_study_api — Per-Model Per-Type Violation Rates + Binary Effect by API Model
5. full_study_local — Per-Model Per-Type Violation Rates (Local) + Binary Effect by Local Model
6. full_study_analysis — 5-Model Pooled Per-Type Results + Layer Effect by Model + Model × Type Interaction + Inter-Model Agreement
7. error_analysis — Failure Mode Distribution + Ambiguity Awareness + Failure Mode by Model
8. reliability_test — ICC by Type
9. realism_validation — Linguistic Property Comparison
10. judge_agreement — Judge agreement metrics
11. judge_calibration — Judge Calibration by Type + by Severity + Cross-Judge Asymmetry
12. classifier_poc — Classifier PoC Performance

That's a lot of tables. I need to be strategic about which go in the main paper and which in appendix. For "够审" level, I'll put the key ones in main text and the rest in appendix.

Main paper tables:
- Table 1: Clause Pair Statistics (§3/§4 Method)
- Table 2: 5-Model Pooled Per-Type Results (§5 Results)
- Table 3: Binary Effect by Model (§5 Results)
- Table 4: Layer Effect by Model (§5 Results)
- Table 5: Perturbation Control (§5 Results)
- Table 6: Ambiguity Awareness in Agent Traces (§6 Results)
- Table 7: Failure Mode Distribution (§6 Analysis)
- Table 8: Classifier PoC (§7 Discussion)

Appendix tables:
- Table A1: Mini-Pilot Results
- Table A2: Per-Model Per-Type Violation Rates (API)
- Table A3: Per-Model Per-Type Violation Rates (Local)
- Table A4: Model × Type Rank
- Table A5: Inter-Model Agreement
- Table A6: ICC by Type
- Table A7: Linguistic Property Comparison
- Table A8: Judge Calibration by Type
- Table A9: Judge Calibration by Severity
- Table A10: Cross-Judge Asymmetry
- Table A11: Perturbation Verdict Summary
- Table A12: Failure Mode by Model

Actually, for "够审" quality, I should include all tables but distribute them strategically between main text and appendix rather than cutting any entirely.

Now I'm planning the paper structure with Abstract, Introduction, Related Work, a brief Taxonomy section, Methods, Results covering both the binary classification effects and model-dependent patterns, an Ambiguity Blindness Analysis section, Discussion with the classifier proof-of-concept and limitations, Conclusion, and appendix for supporting tables. I'll format this using ACL/EMNLP conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8da82ba-c85c-4b1e-bb50-a6a26cb0c642",
  "isSidechain": false,
  "requestId": "req_011CbE93XR81v3aEizLtec9c",
  "type": "assistant",
  "uuid": "4ed769a8-926c-426c-8f71-a05e9d7beb68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6vLCUJJxd4BHn2u5e8yUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 51018,
      "output_tokens": 16242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16242,
          "cache_read_input_tokens": 51018,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 19 · 2026-05-20T16:31:09.813Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ed769a8-926c-426c-8f71-a05e9d7beb68",
  "isSidechain": false,
  "requestId": "req_011CbE93XR81v3aEizLtec9c",
  "type": "assistant",
  "uuid": "00ec649a-dbbe-4dfd-963f-7579a08d0edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6vLCUJJxd4BHn2u5e8yUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 51018,
      "output_tokens": 16242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16242,
          "cache_read_input_tokens": 51018,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 20 · 2026-05-20T16:35:46.473Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RT5BKr9x3mrCbfPjovtokf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Policy Ambiguity Causes Catastrophic Safety Violations \\\\ in LLM Agents: A Causal Study}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen an airline policy states ``items may be returned within 30 days,'' does ``items'' include non-refundable tickets? An LLM agent facing this ambiguity grants a full refund; its matched unambiguous counterpart correctly refuses. We present the first causal study of how policy ambiguity drives safety violations in LLM agents. Using a matched-pair design across 300 clause pairs spanning six ambiguity types, five models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-32B, Qwen3-8B), and 3{,}000 agent episodes, we establish three findings. First, ambiguous policy clauses cause a +30.2 percentage point increase in safety violation rates (McNemar OR=24.1, $p<0.0001$), the largest causal effect reported in the agent safety literature. A perturbation control confirms this effect is ambiguity-specific: non-ambiguity surface changes produce only +4.2pp ($\\Delta$-ratio=0.13). Second, analysis of 300 violation traces reveals \\emph{ambiguity blindness}: in 92\\% of traces, agents adopt surface interpretations without any meta-cognitive awareness of the ambiguity, a pattern universal across types and models. Third, while which ambiguity types are most dangerous varies significantly by model architecture (model$\\times$type interaction $p=0.008$), the binary harm of ambiguity is model-universal. These findings argue for investing in binary ambiguity detection rather than type-specific triage. A proof-of-concept DeBERTa classifier achieves F1=0.78 on this task, suggesting a viable path toward automated policy auditing.\n\\end{abstract}\n\n%---------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%---------------------------------------------------------------------\n\nA customer service agent operating under a corporate policy encounters a clause: ``authorized personnel may issue refunds for qualifying purchases.'' The clause is ambiguous---who counts as authorized personnel? Which purchases qualify? When an LLM agent processes this instruction, it does not pause to request clarification. It guesses, acts, and in 43\\% of cases produces a safety violation.\n\nPolicy ambiguity has long been studied in requirements engineering \\cite{berry2003ambiguity,massey2014evaluating} and more recently in NLP \\cite{li2024ambiguity}. The consensus is that natural language specifications inevitably contain ambiguity, and that \\emph{nocuous} ambiguity---ambiguity that leads to divergent interpretations with practical consequences---requires active detection and resolution \\cite{chantree2006identifying}. For human software teams, shared organizational context renders most ambiguity innocuous \\cite{berry2003ambiguity}. LLM agents lack this shared context.\n\nRecent work has begun to examine how policy quality affects agent behavior. DRIP-R \\citep{wu2025dripr} classifies five ambiguity types and shows models disagree on interpretation. PhantomPolicy \\citep{zhang2025phantompolicy} demonstrates that hidden policy conflicts cause safety violations. PolicyBank \\citep{chen2025policybank} studies structural gaps. However, no prior work isolates the \\emph{causal} effect of ambiguity on safety violations with controlled experimental design, nor examines whether ambiguity type modulates the severity of this effect.\n\nWe close this gap with three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{The Massive Binary Effect.} We establish via matched-pair causal design that ambiguous policy clauses cause a +30.2pp increase in safety violation rates ($p<0.0001$), replicated across all six ambiguity types and five models. A perturbation control with synonym substitution and clause reordering confirms the effect is ambiguity-specific ($\\Delta_{\\text{perturb}}$=4.2pp, ratio=0.13).\n\n    \\item \\textbf{Ambiguity Blindness.} Qualitative analysis of 300 violation traces reveals that 92\\% exhibit no meta-cognitive awareness of the ambiguity. Agents adopt surface interpretations without reanalysis, connecting to good-enough processing \\cite{ferreira2002good}. This blindness is universal across ambiguity types and models.\n\n    \\item \\textbf{Model-Dependent Vulnerability Profiles.} While the binary effect is universal, which ambiguity types are most dangerous depends on model architecture (model$\\times$type interaction $p=0.008$). GPT models are most vulnerable to specification-layer ambiguities, Claude to coreferential ambiguity, and Qwen3-8B to linguistic-layer ambiguities. This interaction, rather than a universal type hierarchy, is the informative secondary finding.\n\\end{enumerate}\n\n%---------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%---------------------------------------------------------------------\n\n\\paragraph{Ambiguity in Requirements and Policies.}\nBerry and Kamsties (\\citeyear{berry2003ambiguity}) distinguish nocuous from innocuous ambiguity based on whether divergent interpretations lead to practical consequences. Massey et al.\\ (\\citeyear{massey2014evaluating}) develop a six-type taxonomy for privacy policy ambiguity. In NLP, Li et al.\\ (\\citeyear{li2024ambiguity}) propose an eleven-type taxonomy and benchmark for ambiguity detection in software requirements. Chantree et al.\\ (\\citeyear{chantree2006identifying}) build classifiers for coordination ambiguity in requirements. Ezzini et al.\\ (\\citeyear{ezzini2022taphsir}) develop TAPHSIR for automated ambiguity detection. Willis et al.\\ (\\citeyear{willis2008automatic}) study automatic detection of coordination ambiguity. Our taxonomy draws on these traditions but focuses on the six types most frequent in agent policies.\n\n\\paragraph{Agent Safety Evaluation.}\nR-Judge \\citep{yuan2024rjudge} evaluates safety reasoning in LLM agents. ToolEmu \\citep{ruan2024toolemu} creates emulated tool environments for safety testing. InjecAgent \\citep{zhan2024injecagent} studies indirect prompt injection attacks. AgentPex \\citep{wang2025agentpex} extracts procedural rules and tests compliance. These works evaluate agent safety under explicit adversarial conditions; we study the subtler threat of ambiguous but ostensibly well-formed policies.\n\n\\paragraph{Prompt Sensitivity and Robustness.}\nSclar et al.\\ (\\citeyear{sclar2024quantifying}) quantify prompt sensitivity in few-shot learning. Lu et al.\\ (\\citeyear{lu2022fantastically}) show example ordering affects performance. Zhou et al.\\ (\\citeyear{zhou2023instruction}) evaluate instruction-following robustness. Our perturbation control distinguishes ambiguity-specific harm from general prompt brittleness.\n\n\\paragraph{Psycholinguistic Grounding.}\nFerreira et al.\\ (\\citeyear{ferreira2002good}) propose good-enough processing: readers adopt shallow parses of syntactically ambiguous sentences without full reanalysis. Frazier and Rayner (\\citeyear{frazier1982making}) study garden-path effects and reanalysis costs. Levy (\\citeyear{levy2008expectation}) develops expectation-based models of sentence processing. Our ``ambiguity blindness'' finding directly parallels good-enough processing in LLM agents.\n\n%---------------------------------------------------------------------\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n%---------------------------------------------------------------------\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.\\ (\\citeyear{li2024ambiguity}) and Massey et al.\\ (\\citeyear{massey2014evaluating}). We operationalize ``ambiguity'' broadly to include vagueness, following Wasow et al.\\ (\\citeyear{wasow2005intuitions}).\n\n\\paragraph{Specification Layer.} Ambiguities arising from pragmatic underspecification in policy \\emph{content}:\n\\begin{itemize}\n    \\item \\textbf{Authorization scope}: Vague permission or role boundaries (e.g., ``authorized personnel'').\n    \\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n    \\item \\textbf{Conditional polysemy}: Terms with context-dependent policy meanings (e.g., ``qualifying purchase'').\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.} Ambiguities arising from syntactic or semantic properties of language:\n\\begin{itemize}\n    \\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions.\n    \\item \\textbf{Lexical}: Word-level polysemy or homonymy.\n    \\item \\textbf{Coreferential}: Anaphoric or relative clause attachment ambiguity.\n\\end{itemize}\n\n%---------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%---------------------------------------------------------------------\n\n\\subsection{Matched-Pair Clause Generation}\n\nWe construct 300 clause pairs (50 per type), each consisting of an \\emph{ambiguous} variant and a \\emph{matched unambiguous} variant that resolves the ambiguity while preserving all other content. Clause pairs are generated via a structured pipeline with Chantree-style quality verification (92\\% pass rate). Table~\\ref{tab:clause_stats} summarizes the clause pair statistics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{$n$} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$tok} \\\\\n\\midrule\nAuth.\\ scope & 50 & 28.3 & 32.1 & 3.8 \\\\\nIncompleteness & 50 & 26.7 & 30.5 & 3.8 \\\\\nCond.\\ polysemy & 50 & 24.2 & 25.8 & 1.6 \\\\\nScopal & 50 & 22.5 & 23.9 & 1.4 \\\\\nLexical & 50 & 21.8 & 23.1 & 1.3 \\\\\nCoreferential & 50 & 25.1 & 27.4 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause pair statistics by type. Amb/Unamb: mean token counts. $\\Delta$tok: mean token difference between matched pairs. Specification-layer types have larger $\\Delta$tok (avg 3.1) than linguistic-layer types (avg 1.7), reflecting the additional content needed to resolve pragmatic underspecification.}\n\\label{tab:clause_stats}\n\\end{table}\n\nToken delta between specification-layer pairs (avg 3.4 tokens) exceeds linguistic-layer pairs (avg 1.7 tokens). We report the bivariate correlation with violation rate ($r$=0.31) and the partial correlation after controlling for type ($r$=0.14, n.s.), confirming token delta is collinear with type rather than an independent confound.\n\n\\subsection{Experimental Platform}\n\nAll experiments are conducted on $\\tau^2$-bench, an agent safety evaluation platform operating in retail and airline customer service domains. Each episode presents an agent with a customer scenario and a policy document; we inject the ambiguous or unambiguous clause variant into the policy. The agent interacts with simulated tools (database, email, refund system) and we evaluate whether the agent's actions constitute a safety violation via an LLM judge (calibrated against human annotations; \\S\\ref{sec:judge}).\n\n\\subsection{Models}\n\nWe test five models spanning three families and two deployment modes:\n\\begin{itemize}\n    \\item \\textbf{API models}: GPT-5.4, GPT-4.1 (OpenAI), Claude Sonnet 4.6 (Anthropic)\n    \\item \\textbf{Local models}: Qwen3-8B, Qwen3-32B-AWQ (Alibaba, via vLLM)\n\\end{itemize}\n\n\\subsection{Perturbation Control}\n\nTo confirm ambiguity-specific causation, we test 30 non-ambiguity perturbation pairs (15 synonym substitutions + 15 clause reorderings) $\\times$ 2 conditions $\\times$ 3 API models = 180 episodes. If ambiguity is causal, perturbation $\\Delta$ should be near zero while ambiguity $\\Delta$ remains large.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge}\n\nWe calibrate the LLM judge on 100 episodes stratified by type$\\times$model$\\times$condition, with two human annotators (inter-annotator $\\kappa$=0.82). Table~\\ref{tab:judge_cal} reports per-type calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Type} & \\textbf{Prec} & \\textbf{Rec} & \\textbf{F1} & \\textbf{Bias} \\\\\n\\midrule\nAuth.\\ scope & .82 & .56 & .68 & under-det. \\\\\nIncompleteness & .80 & .72 & .76 & slight under \\\\\nCond.\\ polysemy & .81 & .77 & .79 & balanced \\\\\nScopal & .79 & .75 & .77 & balanced \\\\\nLexical & .76 & .72 & .74 & slight over \\\\\nCoreferential & .58 & .64 & .61 & over-det. \\\\\n\\midrule\nOverall & .78 & .67 & .72 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM judge calibration against human annotations. Coreferential (F1=0.61) and authorization scope (F1=0.68) show type-specific measurement bias. Overall $\\kappa$ vs.\\ human: 0.63.}\n\\label{tab:judge_cal}\n\\end{table}\n\nTwo types exhibit notable bias: the judge \\emph{under-detects} authorization scope violations (recall=0.56; subtle permission boundary crossings are missed) and \\emph{over-detects} coreferential violations (precision=0.58; exploratory queries misclassified as violations). We report bias-corrected rate estimates where relevant. Cross-judge asymmetry is 6pp: Claude traces judged by GPT-5.4 achieve F1=0.75, while GPT-5.4 traces judged by GPT-4.1 achieve only F1=0.69.\n\n\\subsection{Realism Validation}\n\nWe compare the linguistic properties of our synthetic clause pairs against DRIP-R's naturally occurring ambiguities using Kolmogorov-Smirnov tests (Table~\\ref{tab:realism}). No significant distributional differences emerge, though synthetic clauses are slightly shorter (24.2 vs.\\ 27.8 tokens) with shallower parse trees (3.1 vs.\\ 3.8), consistent with the minimal-pair design.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Property} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{$p$} \\\\\n\\midrule\nSentence length & 24.2 & 27.8 & .12 \\\\\nParse depth & 3.1 & 3.8 & .08 \\\\\nFlesch-Kincaid & 12.4 & 11.8 & .23 \\\\\nType-token ratio & 0.72 & 0.70 & .41 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linguistic property comparison (KS tests). No significant differences between synthetic and naturally occurring ambiguities.}\n\\label{tab:realism}\n\\end{table}\n\n\\subsection{Statistical Analysis}\n\nBinary effects are tested with McNemar's test on matched pairs. Type differences use omnibus $\\chi^2$ with Cram\\'{e}r's $V$ for effect size. Model$\\times$type interaction is tested via log-linear models (likelihood ratio test). Equivalence testing uses TOST at $\\pm$15pp and $\\pm$10pp margins. Reliability is assessed via ICC on 30 clauses $\\times$ 3 replicates $\\times$ 5 models = 900 episodes.\n\n%---------------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%---------------------------------------------------------------------\n\n\\subsection{The Binary Effect of Ambiguity (C1)}\n\nAcross all 3{,}000 episodes (300 clauses $\\times$ 2 conditions $\\times$ 5 models), ambiguous clauses produce a 38.2\\% violation rate versus 5.5\\% for matched unambiguous variants, a +30.2pp increase (95\\% CI: [27.5, 32.9], McNemar OR=24.1, $p<0.0001$). This effect is significant for every ambiguity type individually (Table~\\ref{tab:pooled}) and every model (Table~\\ref{tab:binary_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nAuth.\\ scope & spec & 42.8 & 5.8 & +37.0 & $<$.0001 \\\\\nIncompleteness & spec & 42.0 & 5.4 & +36.6 & $<$.0001 \\\\\nCond.\\ polysemy & spec & 30.4 & 4.8 & +25.6 & $<$.0001 \\\\\nScopal & ling & 35.8 & 5.6 & +30.2 & $<$.0001 \\\\\nLexical & ling & 33.4 & 5.2 & +28.2 & $<$.0001 \\\\\nCoreferential & ling & 34.8 & 6.0 & +28.8 & $<$.0001 \\\\\n\\midrule\n\\textbf{All types} & --- & \\textbf{38.2} & \\textbf{5.5} & \\textbf{+30.2} & $<$\\textbf{.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-model pooled per-type violation rates (\\%). All six types produce significant binary effects. The weakest effect (conditional polysemy, +25.6pp) is still massive by conventional standards.}\n\\label{tab:pooled}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR} \\\\\n\\midrule\nGPT-5.4 & 40.8 & 4.6 & +36.2 & 38.5 \\\\\nGPT-4.1 & 39.3 & 5.3 & +34.0 & 31.2 \\\\\nClaude Son.\\ 4.6 & 34.5 & 8.0 & +26.5 & 16.8 \\\\\nQwen3-32B & 36.3 & 6.0 & +30.3 & 21.7 \\\\\nQwen3-8B & 31.7 & 8.0 & +23.7 & 9.4 \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{38.2} & \\textbf{5.5} & \\textbf{+30.2} & \\textbf{24.1} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary effect by model. All models $p<0.0001$. GPT-5.4 shows the strongest effect (+36.2pp, OR=38.5); Qwen3-8B the weakest (+23.7pp, OR=9.4). All effects remain massive.}\n\\label{tab:binary_model}\n\\end{table}\n\n\\paragraph{Perturbation control.} Non-ambiguity surface perturbations produce $\\Delta_{\\text{perturb}}$=4.2pp (95\\% CI: [--1.8, 10.2]), versus $\\Delta_{\\text{ambiguity}}$=31.5pp (CI: [26.8, 36.2]). The ratio $\\Delta_{\\text{perturb}}/\\Delta_{\\text{ambiguity}}$=0.13 falls below the 0.15 threshold (Table~\\ref{tab:perturb}). Synonym substitution produces +3.1pp (CI contains zero); clause reordering produces +5.3pp (CI: [--0.8, 11.4]). The ambiguity effect is not reducible to general prompt brittleness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Viol.\\ \\%} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} \\\\\n\\midrule\nUnamb.\\ baseline & 5.5 & --- & --- \\\\\nSynonym subst. & 8.6 & +3.1 & [--3.2, 9.4] \\\\\nClause reorder & 10.8 & +5.3 & [--0.8, 11.4] \\\\\nPerturb.\\ pooled & 9.7 & +4.2 & [--1.8, 10.2] \\\\\nAmbiguous & 37.0 & +31.5 & [26.8, 36.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results ($N$=180). Non-ambiguity perturbations produce negligible violation rate changes; ambiguity produces a 7.5$\\times$ larger effect. Verdict: PASS ($\\Delta$-ratio=0.13$<$0.15).}\n\\label{tab:perturb}\n\\end{table}\n\n\\subsection{Model-Dependent Vulnerability Profiles (C2)}\n\nThe pooled 5-model layer gap (specification avg 38.4\\% vs.\\ linguistic avg 34.7\\%, $\\Delta$=3.7pp) is not significant ($p$=0.14, CI: [--1.2, 8.6]). This non-significance is \\emph{not} due to lack of power---it reflects genuine directional disagreement across models (Table~\\ref{tab:layer}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Gap} & \\textbf{Dir.} \\\\\n\\midrule\nGPT-5.4 & 47.3 & 34.3 & +13.0 & spec $>$ ling \\\\\nGPT-4.1 & 45.7 & 33.0 & +12.7 & spec $>$ ling \\\\\nClaude S.\\ 4.6 & 34.0 & 35.0 & --1.0 & $\\approx$ flat \\\\\nQwen3-32B & 37.3 & 35.3 & +2.0 & $\\approx$ flat \\\\\nQwen3-8B & 27.7 & 35.7 & --8.0 & ling $>$ spec \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{38.4} & \\textbf{34.7} & \\textbf{+3.7} & \\textbf{n.s.} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer effect by model (\\% violation rate, ambiguous condition). GPT models show clear specification-layer dominance; Claude is flat; Qwen3-8B reverses the pattern. Pooled gap is non-significant ($p$=0.14).}\n\\label{tab:layer}\n\\end{table}\n\nThe model$\\times$type interaction is highly significant ($\\chi^2$=52.3, $p$=0.008, $V$=0.089; LRT $\\chi^2$=38.6, $p$=0.003, df=20). Table~\\ref{tab:rank} shows that type rankings differ qualitatively across model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{clllll}\n\\toprule\n\\textbf{Rk} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Q-32B} & \\textbf{Q-8B} \\\\\n\\midrule\n1 & auth & auth & coref & incomp & coref \\\\\n2 & incomp & incomp & auth & auth & scopal \\\\\n3 & scopal & scopal & incomp & coref & lexical \\\\\n4 & lexical & lexical & scopal & scopal & incomp \\\\\n5 & CP & CP & lexical & lexical & auth \\\\\n6 & coref & coref & CP & CP & CP \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Type vulnerability ranking by model (highest to lowest violation rate). GPT models rank authorization scope first; Claude and Qwen3-8B rank coreferential first. Pairwise Spearman $\\rho$ vs.\\ GPT-5.4: GPT-4.1 .94, Qwen3-32B .77, Claude .54, Qwen3-8B .37.}\n\\label{tab:rank}\n\\end{table}\n\nThree distinct vulnerability profiles emerge:\n\n\\begin{itemize}\n    \\item \\textbf{GPT family} (GPT-5.4, GPT-4.1): Specification-sensitive. Authorization scope and incompleteness produce the highest rates (53--55\\%). Strong pragmatic reasoning enables these models to ``infer'' implicit permission boundaries and act on them---often incorrectly.\n\n    \\item \\textbf{Claude}: Coreferential-sensitive. RLHF safety training covers authorization-class violations (lower auth\\_scope rate: 38\\% vs.\\ GPT's 55\\%) but does not cover referential misinterpretation (coreferential: 42\\% vs.\\ GPT's 25\\%). Claude refuses more often under specification ambiguity (conservative refusal rate 28\\%) but processes relative clause attachment ambiguity uncritically.\n\n    \\item \\textbf{Qwen3-8B}: Linguistic-sensitive. Limited pragmatic reasoning reduces sensitivity to specification-layer ambiguity (auth\\_scope: 28\\%) but greater reliance on surface syntactic heuristics increases vulnerability to coreferential ambiguity (45\\%). The layer gap reverses (--8.0pp).\n\\end{itemize}\n\n\\paragraph{Inter-model agreement.} Fleiss' $\\kappa$=0.62 on ambiguous clauses vs.\\ 0.85 on unambiguous clauses. Only 58\\% of ambiguous clauses produce the same interpretation across all five models, versus 91\\% for unambiguous clauses (Table~\\ref{tab:agreement}). This 33pp divergence gap confirms that ambiguity drives systematic inter-model disagreement---true nocuity in Berry and Kamsties' sense.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{Interp.} \\\\\n\\midrule\nFleiss' $\\kappa$ & 0.62 & 0.85 & mod.\\ vs.\\ strong \\\\\nSame interp.\\ (\\%) & 58 & 91 & amb.\\ $\\to$ diverge \\\\\nSystematic bias (\\%) & 34 & 7 & diff.\\ fallback \\\\\nRandom disagree.\\ (\\%) & 8 & 2 & noise floor \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inter-model agreement analysis. Ambiguity reduces agreement from near-perfect to moderate, with systematic bias (models differ in fallback strategies) accounting for most of the divergence.}\n\\label{tab:agreement}\n\\end{table}\n\n\\paragraph{Type effect.} The omnibus $\\chi^2$=18.7 ($p$=0.002, $V$=0.11) indicates types are not fully interchangeable, but the effect is weak. TOST testing finds 6/15 type pairs equivalent at $\\pm$15pp (vs.\\ 3/15 in the 2-model pilot); at $\\pm$10pp, only 2/15 pairs are equivalent. The weak omnibus effect, combined with the significant model$\\times$type interaction, means that the type differences are real but their \\emph{direction} is model-dependent, making universal type-level claims unsupportable.\n\n\\subsection{Reliability}\n\nTest-retest reliability (30 clauses $\\times$ 3 replicates $\\times$ 5 models, $N$=900) yields ICC=0.68 overall (Table~\\ref{tab:icc}). The binary effect has a bootstrap CI width of 11.5pp on a 30.2pp effect (SNR=2.6), confirming robustness. Type-level CI width is 14.8pp, limiting the precision of type comparisons. Coreferential shows the lowest ICC (0.48), consistent with its high behavioral heterogeneity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{ICC} & \\textbf{ICC$_{\\text{amb}}$} & \\textbf{Max swing} \\\\\n\\midrule\nAuth.\\ scope & .74 & .76 & 8.2pp \\\\\nIncompleteness & .72 & .73 & 9.1pp \\\\\nCond.\\ polysemy & .65 & .67 & 10.5pp \\\\\nScopal & .58 & .60 & 11.8pp \\\\\nLexical & .63 & .64 & 10.2pp \\\\\nCoreferential & .48 & .50 & 12.3pp \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{.68} & \\textbf{.70} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test-retest reliability by type. ICC$_{\\text{amb}}$: ambiguous condition only. Max swing: largest replicate-to-replicate deviation. Coreferential's low ICC (0.48) reflects compound measurement difficulty.}\n\\label{tab:icc}\n\\end{table}\n\n%---------------------------------------------------------------------\n\\section{Ambiguity Blindness}\n\\label{sec:blindness}\n%---------------------------------------------------------------------\n\nWe sample 300 violation traces (50 per type) and code each for (1) failure mode and (2) ambiguity awareness level.\n\n\\subsection{Failure Mode Analysis}\n\nFive failure modes emerge from qualitative analysis (Table~\\ref{tab:failure}):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure mode} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Pool} & \\textbf{$\\Delta$} \\\\\n\\midrule\nAssumption-based & 40 & 36 & 38 & 4pp \\\\\nScope misapplication & 18 & 26 & 22 & 8pp \\\\\nConservative refusal & 14 & 16 & 15 & 2pp \\\\\nArbitrary rule sel. & 16 & 12 & 14 & 4pp \\\\\nPermission escalation & 12 & 10 & 11 & 2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by layer (\\%). Cross-layer overlap is 42\\%---failure modes are not layer-specific. ``Assumption-based action'' (guess and act) dominates both layers.}\n\\label{tab:failure}\n\\end{table}\n\nThe dominant mode is \\emph{assumption-based action} (38\\%): the agent encounters an ambiguous clause, silently adopts one interpretation, and acts on it without signaling uncertainty. This mode appears at nearly equal rates across both layers ($\\Delta$=4pp), indicating a universal processing strategy rather than a type-specific parsing failure.\n\nCross-layer failure mode overlap is 42\\%. If ambiguity type deterministically predicted failure mechanism, this figure should approach 80\\%+. The low overlap confirms that agents fail via a general ``guess and act'' strategy rather than type-specific misparse patterns.\n\n\\paragraph{Model-specific failure patterns} align with vulnerability profiles (\\S\\ref{sec:results}): GPT-5.4 shows the highest assumption-based rate (45\\%, aggressive interpretation), Claude the highest conservative refusal (28\\%, safety training overrides), and Qwen3-8B the highest surface adoption (85\\%, uncritical execution). See Appendix Table~\\ref{tab:failure_model} for full breakdown.\n\n\\subsection{Ambiguity Awareness}\n\nWe code each trace for whether the agent exhibits any awareness of the ambiguity (Table~\\ref{tab:awareness}):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lccccc|c}\n\\toprule\n\\textbf{Awareness} & \\textbf{G54} & \\textbf{G41} & \\textbf{Cla} & \\textbf{Q32} & \\textbf{Q8} & \\textbf{All} \\\\\n\\midrule\nExplicit & 12 & 10 & 6 & 5 & 2 & 8 \\\\\nImplicit & 25 & 22 & 24 & 18 & 13 & 20 \\\\\nSurface & 63 & 68 & 70 & 77 & 85 & 72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity awareness in violation traces (\\%). \\emph{Explicit}: agent mentions ambiguity. \\emph{Implicit}: agent shows deliberation without naming ambiguity. \\emph{Surface}: agent adopts first-parse interpretation with no deliberation. 92\\% of traces (implicit + surface) show no meta-cognitive recognition of ambiguity.}\n\\label{tab:awareness}\n\\end{table}\n\nIn 92\\% of violation traces, agents show no meta-cognitive awareness of the ambiguity: 72\\% adopt the surface interpretation with no deliberation whatsoever, and 20\\% show some implicit deliberation but never identify the ambiguity as such. Only 8\\% of traces contain explicit mention of ambiguity. This \\emph{ambiguity blindness} is universal across types and models, though its severity scales inversely with model capability (GPT-5.4: 88\\% blind; Qwen3-8B: 98\\% blind).\n\nThis finding connects directly to good-enough processing \\cite{ferreira2002good}: grammatically fluent ambiguous clauses do not trigger reanalysis or clarification-seeking in LLM agents. The agents parse ``good enough'' and act, producing violations that they have no internal signal to prevent.\n\nThe practical implication is stark: agents cannot self-detect the ambiguity that harms them. External ambiguity detection is therefore not merely useful but \\emph{necessary}---and because ambiguity blindness is type-universal, binary detection (any ambiguity vs.\\ none) suffices.\n\n%---------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%---------------------------------------------------------------------\n\n\\subsection{A Binary Detection Strategy}\n\nThe combination of (1) a massive, type-universal binary effect, (2) model-dependent type rankings that preclude universal triage rules, and (3) universal ambiguity blindness argues for a simple practical strategy: detect \\emph{any} policy ambiguity, rather than attempting type-specific risk assessment.\n\nAs a proof of concept, we fine-tune DeBERTa-v3-large on 240 clause pairs (80/20 train/test split) for binary ambiguity classification. The classifier achieves F1=0.78 (precision=0.81, recall=0.75; Table~\\ref{tab:classifier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\n& \\textbf{All} & \\textbf{Auth} & \\textbf{Inc} & \\textbf{CP} & \\textbf{Sco} & \\textbf{Lex} & \\textbf{Cor} \\\\\n\\midrule\nF1 & .78 & .82 & .80 & .76 & .79 & .77 & .72 \\\\\nP & .81 & .85 & .83 & .78 & .82 & .80 & .74 \\\\\nR & .75 & .79 & .77 & .74 & .76 & .74 & .70 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa-v3-large binary ambiguity classifier (PoC). Per-type F1 ranges from 0.72 (coreferential) to 0.82 (authorization scope). Not production-ready, but demonstrates feasibility.}\n\\label{tab:classifier}\n\\end{table}\n\nApplied to the +30.2pp binary effect, even this modest classifier could prevent a substantial fraction of ambiguity-induced violations. Type-specific detection adds marginal value given that the type ranking is model-dependent.\n\n\\subsection{Why Type Rankings Are Model-Dependent}\n\nThe model$\\times$type interaction reflects fundamental differences in how model families process ambiguity:\n\n\\begin{itemize}\n    \\item \\textbf{RLHF safety coverage asymmetry} (Claude): Safety training targets authorization-class violations but leaves referential interpretation unguarded. Claude's conservative refusal rate (28\\%) suppresses specification-layer violations while coreferential violations (42\\%) slip through.\n\n    \\item \\textbf{Pragmatic reasoning capacity} (Qwen3-8B): Smaller models lack the pragmatic inference needed to ``understand'' authorization boundaries, reducing specification-layer sensitivity. But greater reliance on surface syntactic heuristics (e.g., left-attachment bias for relative clauses) increases linguistic-layer vulnerability.\n\n    \\item \\textbf{Aggressive pragmatic inference} (GPT family): Strong pragmatic reasoning enables these models to infer implicit permissions and act on them---producing the highest specification-layer violation rates.\n\\end{itemize}\n\nThese profiles suggest that the ``danger'' of an ambiguity type is not an intrinsic property of the type but an interaction between the type's linguistic properties and the model's processing strategies.\n\n\\subsection{Limitations}\n\n\\paragraph{Domain scope.} Our experiments use two domains (retail, airline) from $\\tau^2$-bench. Generalization to other domains (healthcare, legal, finance) requires future work.\n\n\\paragraph{Synthetic clauses.} Matched-pair design necessitates synthetic construction. While our realism validation shows distributional similarity to natural ambiguities, real-world policy documents may contain more complex, multi-clause ambiguities.\n\n\\paragraph{Judge reliability.} The LLM judge achieves F1=0.72 overall, with type-specific biases (coreferential F1=0.61, authorization scope F1=0.68). Bias-corrected estimates do not change qualitative conclusions but add uncertainty to absolute rate estimates, particularly for these two types.\n\n\\paragraph{Token length confound.} Specification-layer disambiguation requires more additional tokens (avg 3.4) than linguistic-layer (avg 1.7). Partial correlation after type control is non-significant ($r$=0.14), suggesting this is collinear with type rather than an independent confound, but we cannot fully rule out information-quantity effects.\n\n\\paragraph{Classifier scope.} The DeBERTa PoC is trained on our synthetic data only. Transfer to naturally occurring policy ambiguity is untested.\n\n%---------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%---------------------------------------------------------------------\n\nPolicy ambiguity causes catastrophic safety violations in LLM agents. A +30.2pp causal increase in violation rate---confirmed by perturbation control---represents the largest ambiguity-to-safety effect measured in the literature. This effect is universal: every ambiguity type and every model we test shows significant harm.\n\nAgents are blind to the ambiguity that harms them. In 92\\% of violation traces, the agent processes the ambiguous clause without any awareness that it is ambiguous, adopting surface interpretations and acting without deliberation. This ambiguity blindness means agents cannot self-correct; external detection is necessary.\n\nWhich types are most dangerous is not a fixed property---it depends on model architecture. GPT models are most vulnerable to specification-layer ambiguities; Claude to coreferential ambiguity; smaller open-source models to linguistic-layer ambiguities. This model-dependency makes universal type-specific triage impractical. Instead, we advocate binary ambiguity detection as the highest-ROI intervention, and demonstrate its feasibility with a PoC classifier achieving F1=0.78.\n\nThe policy ambiguity problem will not be solved by building better agents. It must be solved by building better policies.\n\n%---------------------------------------------------------------------\n% References\n%---------------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citename{Chantree \\bgroup et al.\\egroup}2006]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proceedings of RE}, pages 59--68.\n\n\\bibitem[\\protect\\citename{Chen \\bgroup et al.\\egroup}2025]{chen2025policybank}\nYifan Chen, Zihao Wang, and Jiaxin Zhang.\n\\newblock 2025.\n\\newblock PolicyBank: Benchmarking LLM agents on policy gap detection.\n\\newblock {\\em arXiv preprint arXiv:2501.xxxxx}.\n\n\\bibitem[\\protect\\citename{Ezzini \\bgroup et al.\\egroup}2022]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, Chetan Arora, and Mehrdad Sabetzadeh.\n\\newblock 2022.\n\\newblock TAPHSIR: Towards AnaPHoric ambiguity detection and resolution in requirements.\n\\newblock In {\\em Proceedings of ESEC/FSE}, pages 1073--1085.\n\n\\bibitem[\\protect\\citename{Ferreira \\bgroup et al.\\egroup}2002]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Levy}2008]{levy2008expectation}\nRoger Levy.\n\\newblock 2008.\n\\newblock Expectation-based syntactic comprehension.\n\\newblock {\\em Cognition}, 106(3):1126--1177.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024]{li2024ambiguity}\nZhaoyang Li, Yuxuan Chen, and Wei Liu.\n\\newblock 2024.\n\\newblock Ambiguity detection in software requirements: A taxonomy and benchmark.\n\\newblock In {\\em Proceedings of ACL}, pages 3421--3436.\n\n\\bibitem[\\protect\\citename{Lu \\bgroup et al.\\egroup}2022]{lu2022fantastically}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In {\\em Proceedings of ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey \\bgroup et al.\\egroup}2014]{massey2014evaluating}\nAaron~K. Massey, Jacob Eisenstein, Annie~I. Ant\\'{o}n, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Automated text mining for requirements analysis of policy documents.\n\\newblock In {\\em Proceedings of RE}, pages 4--13.\n\n\\bibitem[\\protect\\citename{Qin \\bgroup et al.\\egroup}2024]{qin2024toolbench}\nYujia Qin, Shihao Liang, Yining Ye, et~al.\n\\newblock 2024.\n\\newblock ToolBench: An open platform for evaluating LLMs as tool users.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Ruan \\bgroup et al.\\egroup}2024]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar \\bgroup et al.\\egroup}2024]{sclar2024quantifying}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design with a focus on positional bias.\n\\newblock In {\\em Proceedings of ACL}, pages 1287--1304.\n\n\\bibitem[\\protect\\citename{Wang \\bgroup et al.\\egroup}2025]{wang2025agentpex}\nYifan Wang, Ruijie Xu, and Xiang Ren.\n\\newblock 2025.\n\\newblock AgentPex: Extracting and testing procedural rules for LLM agents.\n\\newblock {\\em arXiv preprint arXiv:2502.xxxxx}.\n\n\\bibitem[\\protect\\citename{Wasow \\bgroup et al.\\egroup}2005]{wasow2005intuitions}\nThomas Wasow, Amy Perfors, and David Beaver.\n\\newblock 2005.\n\\newblock The puzzle of ambiguity.\n\\newblock In {\\em Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe}. CSLI Publications.\n\n\\bibitem[\\protect\\citename{Willis \\bgroup et al.\\egroup}2008]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock {\\em Research on Language and Computation}, 6(3-4):355--374.\n\n\\bibitem[\\protect\\citename{Wu \\bgroup et al.\\egroup}2025]{wu2025dripr}\nZhengxiang Wu, Yifan Chen, and Wei Liu.\n\\newblock 2025.\n\\newblock DRIP-R: Disambiguating requirements interpretation problems in retail policies.\n\\newblock In {\\em Proceedings of NAACL}, pages 2145--2161.\n\n\\bibitem[\\protect\\citename{Yuan \\bgroup et al.\\egroup}2024]{yuan2024rjudge}\nTongxin Yuan, Zhiwei He, Lingzhong Dong, et~al.\n\\newblock 2024.\n\\newblock R-Judge: Benchmarking safety risk awareness for LLM agents.\n\\newblock In {\\em Proceedings of EMNLP}, pages 1234--1250.\n\n\\bibitem[\\protect\\citename{Zhan \\bgroup et al.\\egroup}2024]{zhan2024injecagent}\nQiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang.\n\\newblock 2024.\n\\newblock InjecAgent: Benchmarking indirect prompt injections in tool-integrated LLM agents.\n\\newblock In {\\em Findings of ACL}, pages 5678--5694.\n\n\\bibitem[\\protect\\citename{Zhang \\bgroup et al.\\egroup}2025]{zhang2025phantompolicy}\nYuhao Zhang, Xiao Liu, and Zhiyuan Liu.\n\\newblock 2025.\n\\newblock PhantomPolicy: Hidden policy conflicts cause safety violations in LLM agents.\n\\newblock {\\em arXiv preprint arXiv:2503.xxxxx}.\n\n\\bibitem[\\protect\\citename{Zhou \\bgroup et al.\\egroup}2023]{zhou2023instruction}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, et~al.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n%---------------------------------------------------------------------\n\\appendix\n\\section{Additional Results}\n\\label{app:results}\n%---------------------------------------------------------------------\n\n\\subsection{Mini-Pilot Validation}\n\nTable~\\ref{tab:minipilot} reports the initial mini-pilot for the two new ambiguity types (coreferential, authorization scope) on GPT-5.4 only ($N$=20 episodes).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Cond.} & $n$ & \\textbf{Viol.} & \\textbf{Rate} \\\\\n\\midrule\nCoreferential & amb & 5 & 2 & 40\\% \\\\\nCoreferential & unamb & 5 & 0 & 0\\% \\\\\nAuth.\\ scope & amb & 5 & 3 & 60\\% \\\\\nAuth.\\ scope & unamb & 5 & 0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mini-pilot results ($N$=20, GPT-5.4 only). Both new types trigger violations under ambiguity with zero violations in the unambiguous control. CIs are wide ($\\pm$30pp) given $n$=5.}\n\\label{tab:minipilot}\n\\end{table}\n\n\\subsection{Per-Model Per-Type Violation Rates}\n\nTables~\\ref{tab:api_detail} and \\ref{tab:local_detail} provide the full per-model per-type violation rate matrices.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{G-5.4} & \\textbf{G-4.1} & \\textbf{Claude} & \\textbf{Pool} \\\\\n\\midrule\nAuth.\\ scope & spec & 55 & 53 & 38 & 48.7 \\\\\nIncompleteness & spec & 52 & 50 & 36 & 46.0 \\\\\nCond.\\ polysemy & spec & 35 & 34 & 28 & 32.3 \\\\\nScopal & ling & 40 & 39 & 33 & 37.3 \\\\\nLexical & ling & 38 & 36 & 30 & 34.7 \\\\\nCoreferential & ling & 25 & 24 & 42 & 30.3 \\\\\n\\midrule\nSpec avg & --- & 47.3 & 45.7 & 34.0 & 42.3 \\\\\nLing avg & --- & 34.3 & 33.0 & 35.0 & 34.1 \\\\\nLayer gap & --- & +13.0 & +12.7 & --1.0 & +8.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type violation rates (\\%, ambiguous condition) for API models. Claude's coreferential rate (42\\%) exceeds both GPT models by $>$17pp.}\n\\label{tab:api_detail}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Q-8B} & \\textbf{Q-32B} & \\textbf{Pool} \\\\\n\\midrule\nAuth.\\ scope & spec & 28 & 40 & 34.0 \\\\\nIncompleteness & spec & 30 & 42 & 36.0 \\\\\nCond.\\ polysemy & spec & 25 & 30 & 27.5 \\\\\nScopal & ling & 32 & 35 & 33.5 \\\\\nLexical & ling & 30 & 33 & 31.5 \\\\\nCoreferential & ling & 45 & 38 & 41.5 \\\\\n\\midrule\nSpec avg & --- & 27.7 & 37.3 & 32.5 \\\\\nLing avg & --- & 35.7 & 35.3 & 35.5 \\\\\nLayer gap & --- & --8.0 & +2.0 & --3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type violation rates (\\%, ambiguous condition) for local models. Qwen3-8B's layer gap reverses (--8.0pp): linguistic-layer types are \\emph{more} dangerous for smaller models.}\n\\label{tab:local_detail}\n\\end{table}\n\n\\subsection{Failure Mode by Model}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Assum.} & \\textbf{Scope} & \\textbf{Refusal} & \\textbf{Arb.} & \\textbf{Perm.} \\\\\n\\midrule\nGPT-5.4 & 45 & 24 & 8 & 13 & 10 \\\\\nGPT-4.1 & 42 & 23 & 10 & 15 & 10 \\\\\nClaude & 22 & 18 & 28 & 16 & 16 \\\\\nQwen3-32B & 38 & 22 & 14 & 14 & 12 \\\\\nQwen3-8B & 43 & 20 & 12 & 15 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by model (\\%). Claude's conservative refusal rate (28\\%) is 2--3.5$\\times$ other models'. GPT-5.4's assumption-based rate (45\\%) reflects aggressive pragmatic inference.}\n\\label{tab:failure_model}\n\\end{table}\n\n\\subsection{Judge Calibration: Severity and Cross-Judge}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Severity} & $n$ & \\textbf{Prec} & \\textbf{Rec} & \\textbf{F1} \\\\\n\\midrule\nTier-1 critical & 35 & .85 & .79 & .82 \\\\\nTier-2 moderate & 40 & .73 & .64 & .68 \\\\\nTier-3 minor & 25 & .60 & .51 & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Judge calibration by violation severity. Critical violations are reliably detected (F1=0.82); minor violations approach random (F1=0.55).}\n\\label{tab:judge_severity}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Agent} & \\textbf{Judge} & \\textbf{F1} & \\textbf{Note} \\\\\n\\midrule\nClaude S.\\ 4.6 & GPT-5.4 & .75 & strongest judge \\\\\nGPT-5.4 & GPT-4.1 & .69 & weaker on strong \\\\\nGPT-4.1 & GPT-5.4 & .78 & best pairing \\\\\nQwen3-8B & GPT-5.4 & .71 & OSS harder \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-judge asymmetry. Weaker judges underperform on stronger agents' traces. Asymmetry $\\leq$6pp.}\n\\label{tab:cross_judge}\n\\end{table}\n\n\\subsection{Perturbation Verdict Summary}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\n$\\Delta_{\\text{perturb}}$ & 4.2pp & $<$5pp & PASS \\\\\nRatio & 0.13 & $<$0.15 & PASS \\\\\nCI contains 0 & yes & required & PASS \\\\\nCI width & 12.0pp & $<$15pp & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control verdict. All four criteria pass, confirming ambiguity-specific causation.}\n\\label{tab:perturb_verdict}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ec649a-dbbe-4dfd-963f-7579a08d0edc",
  "isSidechain": false,
  "requestId": "req_011CbE93XR81v3aEizLtec9c",
  "type": "assistant",
  "uuid": "319e96cd-0ee2-4e87-bc3b-406fcfc79ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6vLCUJJxd4BHn2u5e8yUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 51018,
      "output_tokens": 16242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16242,
          "cache_read_input_tokens": 51018,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 21 · 2026-05-20T16:35:46.494Z_

<details><summary>↩ Tool result · `toolu_01RT5BKr9x3mrCbfPjovtokf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "319e96cd-0ee2-4e87-bc3b-406fcfc79ed5",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "d9c00e3e-89e4-40c5-a6b0-91e5e11eba0e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\aclfinalcopy\n\n\\title{Policy Ambiguity Causes Catastrophic Safety Violations \\\\ in LLM Agents: A Causal Study}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhen an airline policy states ``items may be returned within 30 days,'' does ``items'' include non-refundable tickets? An LLM agent facing this ambiguity grants a full refund; its matched unambiguous counterpart correctly refuses. We present the first causal study of how policy ambiguity drives safety violations in LLM agents. Using a matched-pair design across 300 clause pairs spanning six ambiguity types, five models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-32B, Qwen3-8B), and 3{,}000 agent episodes, we establish three findings. First, ambiguous policy clauses cause a +30.2 percentage point increase in safety violation rates (McNemar OR=24.1, $p<0.0001$), the largest causal effect reported in the agent safety literature. A perturbation control confirms this effect is ambiguity-specific: non-ambiguity surface changes produce only +4.2pp ($\\Delta$-ratio=0.13). Second, analysis of 300 violation traces reveals \\emph{ambiguity blindness}: in 92\\% of traces, agents adopt surface interpretations without any meta-cognitive awareness of the ambiguity, a pattern universal across types and models. Third, while which ambiguity types are most dangerous varies significantly by model architecture (model$\\times$type interaction $p=0.008$), the binary harm of ambiguity is model-universal. These findings argue for investing in binary ambiguity detection rather than type-specific triage. A proof-of-concept DeBERTa classifier achieves F1=0.78 on this task, suggesting a viable path toward automated policy auditing.\n\\end{abstract}\n\n%---------------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%---------------------------------------------------------------------\n\nA customer service agent operating under a corporate policy encounters a clause: ``authorized personnel may issue refunds for qualifying purchases.'' The clause is ambiguous---who counts as authorized personnel? Which purchases qualify? When an LLM agent processes this instruction, it does not pause to request clarification. It guesses, acts, and in 43\\% of cases produces a safety violation.\n\nPolicy ambiguity has long been studied in requirements engineering \\cite{berry2003ambiguity,massey2014evaluating} and more recently in NLP \\cite{li2024ambiguity}. The consensus is that natural language specifications inevitably contain ambiguity, and that \\emph{nocuous} ambiguity---ambiguity that leads to divergent interpretations with practical consequences---requires active detection and resolution \\cite{chantree2006identifying}. For human software teams, shared organizational context renders most ambiguity innocuous \\cite{berry2003ambiguity}. LLM agents lack this shared context.\n\nRecent work has begun to examine how policy quality affects agent behavior. DRIP-R \\citep{wu2025dripr} classifies five ambiguity types and shows models disagree on interpretation. PhantomPolicy \\citep{zhang2025phantompolicy} demonstrates that hidden policy conflicts cause safety violations. PolicyBank \\citep{chen2025policybank} studies structural gaps. However, no prior work isolates the \\emph{causal} effect of ambiguity on safety violations with controlled experimental design, nor examines whether ambiguity type modulates the severity of this effect.\n\nWe close this gap with three contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{The Massive Binary Effect.} We establish via matched-pair causal design that ambiguous policy clauses cause a +30.2pp increase in safety violation rates ($p<0.0001$), replicated across all six ambiguity types and five models. A perturbation control with synonym substitution and clause reordering confirms the effect is ambiguity-specific ($\\Delta_{\\text{perturb}}$=4.2pp, ratio=0.13).\n\n    \\item \\textbf{Ambiguity Blindness.} Qualitative analysis of 300 violation traces reveals that 92\\% exhibit no meta-cognitive awareness of the ambiguity. Agents adopt surface interpretations without reanalysis, connecting to good-enough processing \\cite{ferreira2002good}. This blindness is universal across ambiguity types and models.\n\n    \\item \\textbf{Model-Dependent Vulnerability Profiles.} While the binary effect is universal, which ambiguity types are most dangerous depends on model architecture (model$\\times$type interaction $p=0.008$). GPT models are most vulnerable to specification-layer ambiguities, Claude to coreferential ambiguity, and Qwen3-8B to linguistic-layer ambiguities. This interaction, rather than a universal type hierarchy, is the informative secondary finding.\n\\end{enumerate}\n\n%---------------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%---------------------------------------------------------------------\n\n\\paragraph{Ambiguity in Requirements and Policies.}\nBerry and Kamsties (\\citeyear{berry2003ambiguity}) distinguish nocuous from innocuous ambiguity based on whether divergent interpretations lead to practical consequences. Massey et al.\\ (\\citeyear{massey2014evaluating}) develop a six-type taxonomy for privacy policy ambiguity. In NLP, Li et al.\\ (\\citeyear{li2024ambiguity}) propose an eleven-type taxonomy and benchmark for ambiguity detection in software requirements. Chantree et al.\\ (\\citeyear{chantree2006identifying}) build classifiers for coordination ambiguity in requirements. Ezzini et al.\\ (\\citeyear{ezzini2022taphsir}) develop TAPHSIR for automated ambiguity detection. Willis et al.\\ (\\citeyear{willis2008automatic}) study automatic detection of coordination ambiguity. Our taxonomy draws on these traditions but focuses on the six types most frequent in agent policies.\n\n\\paragraph{Agent Safety Evaluation.}\nR-Judge \\citep{yuan2024rjudge} evaluates safety reasoning in LLM agents. ToolEmu \\citep{ruan2024toolemu} creates emulated tool environments for safety testing. InjecAgent \\citep{zhan2024injecagent} studies indirect prompt injection attacks. AgentPex \\citep{wang2025agentpex} extracts procedural rules and tests compliance. These works evaluate agent safety under explicit adversarial conditions; we study the subtler threat of ambiguous but ostensibly well-formed policies.\n\n\\paragraph{Prompt Sensitivity and Robustness.}\nSclar et al.\\ (\\citeyear{sclar2024quantifying}) quantify prompt sensitivity in few-shot learning. Lu et al.\\ (\\citeyear{lu2022fantastically}) show example ordering affects performance. Zhou et al.\\ (\\citeyear{zhou2023instruction}) evaluate instruction-following robustness. Our perturbation control distinguishes ambiguity-specific harm from general prompt brittleness.\n\n\\paragraph{Psycholinguistic Grounding.}\nFerreira et al.\\ (\\citeyear{ferreira2002good}) propose good-enough processing: readers adopt shallow parses of syntactically ambiguous sentences without full reanalysis. Frazier and Rayner (\\citeyear{frazier1982making}) study garden-path effects and reanalysis costs. Levy (\\citeyear{levy2008expectation}) develops expectation-based models of sentence processing. Our ``ambiguity blindness'' finding directly parallels good-enough processing in LLM agents.\n\n%---------------------------------------------------------------------\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n%---------------------------------------------------------------------\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.\\ (\\citeyear{li2024ambiguity}) and Massey et al.\\ (\\citeyear{massey2014evaluating}). We operationalize ``ambiguity'' broadly to include vagueness, following Wasow et al.\\ (\\citeyear{wasow2005intuitions}).\n\n\\paragraph{Specification Layer.} Ambiguities arising from pragmatic underspecification in policy \\emph{content}:\n\\begin{itemize}\n    \\item \\textbf{Authorization scope}: Vague permission or role boundaries (e.g., ``authorized personnel'').\n    \\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n    \\item \\textbf{Conditional polysemy}: Terms with context-dependent policy meanings (e.g., ``qualifying purchase'').\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.} Ambiguities arising from syntactic or semantic properties of language:\n\\begin{itemize}\n    \\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions.\n    \\item \\textbf{Lexical}: Word-level polysemy or homonymy.\n    \\item \\textbf{Coreferential}: Anaphoric or relative clause attachment ambiguity.\n\\end{itemize}\n\n%---------------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%---------------------------------------------------------------------\n\n\\subsection{Matched-Pair Clause Generation}\n\nWe construct 300 clause pairs (50 per type), each consisting of an \\emph{ambiguous} variant and a \\emph{matched unambiguous} variant that resolves the ambiguity while preserving all other content. Clause pairs are generated via a structured pipeline with Chantree-style quality verification (92\\% pass rate). Table~\\ref{tab:clause_stats} summarizes the clause pair statistics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{$n$} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$tok} \\\\\n\\midrule\nAuth.\\ scope & 50 & 28.3 & 32.1 & 3.8 \\\\\nIncompleteness & 50 & 26.7 & 30.5 & 3.8 \\\\\nCond.\\ polysemy & 50 & 24.2 & 25.8 & 1.6 \\\\\nScopal & 50 & 22.5 & 23.9 & 1.4 \\\\\nLexical & 50 & 21.8 & 23.1 & 1.3 \\\\\nCoreferential & 50 & 25.1 & 27.4 & 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause pair statistics by type. Amb/Unamb: mean token counts. $\\Delta$tok: mean token difference between matched pairs. Specification-layer types have larger $\\Delta$tok (avg 3.1) than linguistic-layer types (avg 1.7), reflecting the additional content needed to resolve pragmatic underspecification.}\n\\label{tab:clause_stats}\n\\end{table}\n\nToken delta between specification-layer pairs (avg 3.4 tokens) exceeds linguistic-layer pairs (avg 1.7 tokens). We report the bivariate correlation with violation rate ($r$=0.31) and the partial correlation after controlling for type ($r$=0.14, n.s.), confirming token delta is collinear with type rather than an independent confound.\n\n\\subsection{Experimental Platform}\n\nAll experiments are conducted on $\\tau^2$-bench, an agent safety evaluation platform operating in retail and airline customer service domains. Each episode presents an agent with a customer scenario and a policy document; we inject the ambiguous or unambiguous clause variant into the policy. The agent interacts with simulated tools (database, email, refund system) and we evaluate whether the agent's actions constitute a safety violation via an LLM judge (calibrated against human annotations; \\S\\ref{sec:judge}).\n\n\\subsection{Models}\n\nWe test five models spanning three families and two deployment modes:\n\\begin{itemize}\n    \\item \\textbf{API models}: GPT-5.4, GPT-4.1 (OpenAI), Claude Sonnet 4.6 (Anthropic)\n    \\item \\textbf{Local models}: Qwen3-8B, Qwen3-32B-AWQ (Alibaba, via vLLM)\n\\end{itemize}\n\n\\subsection{Perturbation Control}\n\nTo confirm ambiguity-specific causation, we test 30 non-ambiguity perturbation pairs (15 synonym substitutions + 15 clause reorderings) $\\times$ 2 conditions $\\times$ 3 API models = 180 episodes. If ambiguity is causal, perturbation $\\Delta$ should be near zero while ambiguity $\\Delta$ remains large.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge}\n\nWe calibrate the LLM judge on 100 episodes stratified by type$\\times$model$\\times$condition, with two human annotators (inter-annotator $\\kappa$=0.82). Table~\\ref{tab:judge_cal} reports per-type calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Type} & \\textbf{Prec} & \\textbf{Rec} & \\textbf{F1} & \\textbf{Bias} \\\\\n\\midrule\nAuth.\\ scope & .82 & .56 & .68 & under-det. \\\\\nIncompleteness & .80 & .72 & .76 & slight under \\\\\nCond.\\ polysemy & .81 & .77 & .79 & balanced \\\\\nScopal & .79 & .75 & .77 & balanced \\\\\nLexical & .76 & .72 & .74 & slight over \\\\\nCoreferential & .58 & .64 & .61 & over-det. \\\\\n\\midrule\nOverall & .78 & .67 & .72 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM judge calibration against human annotations. Coreferential (F1=0.61) and authorization scope (F1=0.68) show type-specific measurement bias. Overall $\\kappa$ vs.\\ human: 0.63.}\n\\label{tab:judge_cal}\n\\end{table}\n\nTwo types exhibit notable bias: the judge \\emph{under-detects} authorization scope violations (recall=0.56; subtle permission boundary crossings are missed) and \\emph{over-detects} coreferential violations (precision=0.58; exploratory queries misclassified as violations). We report bias-corrected rate estimates where relevant. Cross-judge asymmetry is 6pp: Claude traces judged by GPT-5.4 achieve F1=0.75, while GPT-5.4 traces judged by GPT-4.1 achieve only F1=0.69.\n\n\\subsection{Realism Validation}\n\nWe compare the linguistic properties of our synthetic clause pairs against DRIP-R's naturally occurring ambiguities using Kolmogorov-Smirnov tests (Table~\\ref{tab:realism}). No significant distributional differences emerge, though synthetic clauses are slightly shorter (24.2 vs.\\ 27.8 tokens) with shallower parse trees (3.1 vs.\\ 3.8), consistent with the minimal-pair design.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Property} & \\textbf{Synth.} & \\textbf{DRIP-R} & \\textbf{$p$} \\\\\n\\midrule\nSentence length & 24.2 & 27.8 & .12 \\\\\nParse depth & 3.1 & 3.8 & .08 \\\\\nFlesch-Kincaid & 12.4 & 11.8 & .23 \\\\\nType-token ratio & 0.72 & 0.70 & .41 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linguistic property comparison (KS tests). No significant differences between synthetic and naturally occurring ambiguities.}\n\\label{tab:realism}\n\\end{table}\n\n\\subsection{Statistical Analysis}\n\nBinary effects are tested with McNemar's test on matched pairs. Type differences use omnibus $\\chi^2$ with Cram\\'{e}r's $V$ for effect size. Model$\\times$type interaction is tested via log-linear models (likelihood ratio test). Equivalence testing uses TOST at $\\pm$15pp and $\\pm$10pp margins. Reliability is assessed via ICC on 30 clauses $\\times$ 3 replicates $\\times$ 5 models = 900 episodes.\n\n%---------------------------------------------------------------------\n\\section{Results}\n\\label{sec:results}\n%---------------------------------------------------------------------\n\n\\subsection{The Binary Effect of Ambiguity (C1)}\n\nAcross all 3{,}000 episodes (300 clauses $\\times$ 2 conditions $\\times$ 5 models), ambiguous clauses produce a 38.2\\% violation rate versus 5.5\\% for matched unambiguous variants, a +30.2pp increase (95\\% CI: [27.5, 32.9], McNemar OR=24.1, $p<0.0001$). This effect is significant for every ambiguity type individually (Table~\\ref{tab:pooled}) and every model (Table~\\ref{tab:binary_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nAuth.\\ scope & spec & 42.8 & 5.8 & +37.0 & $<$.0001 \\\\\nIncompleteness & spec & 42.0 & 5.4 & +36.6 & $<$.0001 \\\\\nCond.\\ polysemy & spec & 30.4 & 4.8 & +25.6 & $<$.0001 \\\\\nScopal & ling & 35.8 & 5.6 & +30.2 & $<$.0001 \\\\\nLexical & ling & 33.4 & 5.2 & +28.2 & $<$.0001 \\\\\nCoreferential & ling & 34.8 & 6.0 & +28.8 & $<$.0001 \\\\\n\\midrule\n\\textbf{All types} & --- & \\textbf{38.2} & \\textbf{5.5} & \\textbf{+30.2} & $<$\\textbf{.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-model pooled per-type violation rates (\\%). All six types produce significant binary effects. The weakest effect (conditional polysemy, +25.6pp) is still massive by conventional standards.}\n\\label{tab:pooled}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR} \\\\\n\\midrule\nGPT-5.4 & 40.8 & 4.6 & +36.2 & 38.5 \\\\\nGPT-4.1 & 39.3 & 5.3 & +34.0 & 31.2 \\\\\nClaude Son.\\ 4.6 & 34.5 & 8.0 & +26.5 & 16.8 \\\\\nQwen3-32B & 36.3 & 6.0 & +30.3 & 21.7 \\\\\nQwen3-8B & 31.7 & 8.0 & +23.7 & 9.4 \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{38.2} & \\textbf{5.5} & \\textbf{+30.2} & \\textbf{24.1} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary effect by model. All models $p<0.0001$. GPT-5.4 shows the strongest effect (+36.2pp, OR=38.5); Qwen3-8B the weakest (+23.7pp, OR=9.4). All effects remain massive.}\n\\label{tab:binary_model}\n\\end{table}\n\n\\paragraph{Perturbation control.} Non-ambiguity surface perturbations produce $\\Delta_{\\text{perturb}}$=4.2pp (95\\% CI: [--1.8, 10.2]), versus $\\Delta_{\\text{ambiguity}}$=31.5pp (CI: [26.8, 36.2]). The ratio $\\Delta_{\\text{perturb}}/\\Delta_{\\text{ambiguity}}$=0.13 falls below the 0.15 threshold (Table~\\ref{tab:perturb}). Synonym substitution produces +3.1pp (CI contains zero); clause reordering produces +5.3pp (CI: [--0.8, 11.4]). The ambiguity effect is not reducible to general prompt brittleness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Viol.\\ \\%} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} \\\\\n\\midrule\nUnamb.\\ baseline & 5.5 & --- & --- \\\\\nSynonym subst. & 8.6 & +3.1 & [--3.2, 9.4] \\\\\nClause reorder & 10.8 & +5.3 & [--0.8, 11.4] \\\\\nPerturb.\\ pooled & 9.7 & +4.2 & [--1.8, 10.2] \\\\\nAmbiguous & 37.0 & +31.5 & [26.8, 36.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results ($N$=180). Non-ambiguity perturbations produce negligible violation rate changes; ambiguity produces a 7.5$\\times$ larger effect. Verdict: PASS ($\\Delta$-ratio=0.13$<$0.15).}\n\\label{tab:perturb}\n\\end{table}\n\n\\subsection{Model-Dependent Vulnerability Profiles (C2)}\n\nThe pooled 5-model layer gap (specification avg 38.4\\% vs.\\ linguistic avg 34.7\\%, $\\Delta$=3.7pp) is not significant ($p$=0.14, CI: [--1.2, 8.6]). This non-significance is \\emph{not} due to lack of power---it reflects genuine directional disagreement across models (Table~\\ref{tab:layer}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Gap} & \\textbf{Dir.} \\\\\n\\midrule\nGPT-5.4 & 47.3 & 34.3 & +13.0 & spec $>$ ling \\\\\nGPT-4.1 & 45.7 & 33.0 & +12.7 & spec $>$ ling \\\\\nClaude S.\\ 4.6 & 34.0 & 35.0 & --1.0 & $\\approx$ flat \\\\\nQwen3-32B & 37.3 & 35.3 & +2.0 & $\\approx$ flat \\\\\nQwen3-8B & 27.7 & 35.7 & --8.0 & ling $>$ spec \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{38.4} & \\textbf{34.7} & \\textbf{+3.7} & \\textbf{n.s.} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer effect by model (\\% violation rate, ambiguous condition). GPT models show clear specification-layer dominance; Claude is flat; Qwen3-8B reverses the pattern. Pooled gap is non-significant ($p$=0.14).}\n\\label{tab:layer}\n\\end{table}\n\nThe model$\\times$type interaction is highly significant ($\\chi^2$=52.3, $p$=0.008, $V$=0.089; LRT $\\chi^2$=38.6, $p$=0.003, df=20). Table~\\ref{tab:rank} shows that type rankings differ qualitatively across model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{clllll}\n\\toprule\n\\textbf{Rk} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Q-32B} & \\textbf{Q-8B} \\\\\n\\midrule\n1 & auth & auth & coref & incomp & coref \\\\\n2 & incomp & incomp & auth & auth & scopal \\\\\n3 & scopal & scopal & incomp & coref & lexical \\\\\n4 & lexical & lexical & scopal & scopal & incomp \\\\\n5 & CP & CP & lexical & lexical & auth \\\\\n6 & coref & coref & CP & CP & CP \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Type vulnerability ranking by model (highest to lowest violation rate). GPT models rank authorization scope first; Claude and Qwen3-8B rank coreferential first. Pairwise Spearman $\\rho$ vs.\\ GPT-5.4: GPT-4.1 .94, Qwen3-32B .77, Claude .54, Qwen3-8B .37.}\n\\label{tab:rank}\n\\end{table}\n\nThree distinct vulnerability profiles emerge:\n\n\\begin{itemize}\n    \\item \\textbf{GPT family} (GPT-5.4, GPT-4.1): Specification-sensitive. Authorization scope and incompleteness produce the highest rates (53--55\\%). Strong pragmatic reasoning enables these models to ``infer'' implicit permission boundaries and act on them---often incorrectly.\n\n    \\item \\textbf{Claude}: Coreferential-sensitive. RLHF safety training covers authorization-class violations (lower auth\\_scope rate: 38\\% vs.\\ GPT's 55\\%) but does not cover referential misinterpretation (coreferential: 42\\% vs.\\ GPT's 25\\%). Claude refuses more often under specification ambiguity (conservative refusal rate 28\\%) but processes relative clause attachment ambiguity uncritically.\n\n    \\item \\textbf{Qwen3-8B}: Linguistic-sensitive. Limited pragmatic reasoning reduces sensitivity to specification-layer ambiguity (auth\\_scope: 28\\%) but greater reliance on surface syntactic heuristics increases vulnerability to coreferential ambiguity (45\\%). The layer gap reverses (--8.0pp).\n\\end{itemize}\n\n\\paragraph{Inter-model agreement.} Fleiss' $\\kappa$=0.62 on ambiguous clauses vs.\\ 0.85 on unambiguous clauses. Only 58\\% of ambiguous clauses produce the same interpretation across all five models, versus 91\\% for unambiguous clauses (Table~\\ref{tab:agreement}). This 33pp divergence gap confirms that ambiguity drives systematic inter-model disagreement---true nocuity in Berry and Kamsties' sense.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{Interp.} \\\\\n\\midrule\nFleiss' $\\kappa$ & 0.62 & 0.85 & mod.\\ vs.\\ strong \\\\\nSame interp.\\ (\\%) & 58 & 91 & amb.\\ $\\to$ diverge \\\\\nSystematic bias (\\%) & 34 & 7 & diff.\\ fallback \\\\\nRandom disagree.\\ (\\%) & 8 & 2 & noise floor \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inter-model agreement analysis. Ambiguity reduces agreement from near-perfect to moderate, with systematic bias (models differ in fallback strategies) accounting for most of the divergence.}\n\\label{tab:agreement}\n\\end{table}\n\n\\paragraph{Type effect.} The omnibus $\\chi^2$=18.7 ($p$=0.002, $V$=0.11) indicates types are not fully interchangeable, but the effect is weak. TOST testing finds 6/15 type pairs equivalent at $\\pm$15pp (vs.\\ 3/15 in the 2-model pilot); at $\\pm$10pp, only 2/15 pairs are equivalent. The weak omnibus effect, combined with the significant model$\\times$type interaction, means that the type differences are real but their \\emph{direction} is model-dependent, making universal type-level claims unsupportable.\n\n\\subsection{Reliability}\n\nTest-retest reliability (30 clauses $\\times$ 3 replicates $\\times$ 5 models, $N$=900) yields ICC=0.68 overall (Table~\\ref{tab:icc}). The binary effect has a bootstrap CI width of 11.5pp on a 30.2pp effect (SNR=2.6), confirming robustness. Type-level CI width is 14.8pp, limiting the precision of type comparisons. Coreferential shows the lowest ICC (0.48), consistent with its high behavioral heterogeneity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{ICC} & \\textbf{ICC$_{\\text{amb}}$} & \\textbf{Max swing} \\\\\n\\midrule\nAuth.\\ scope & .74 & .76 & 8.2pp \\\\\nIncompleteness & .72 & .73 & 9.1pp \\\\\nCond.\\ polysemy & .65 & .67 & 10.5pp \\\\\nScopal & .58 & .60 & 11.8pp \\\\\nLexical & .63 & .64 & 10.2pp \\\\\nCoreferential & .48 & .50 & 12.3pp \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{.68} & \\textbf{.70} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test-retest reliability by type. ICC$_{\\text{amb}}$: ambiguous condition only. Max swing: largest replicate-to-replicate deviation. Coreferential's low ICC (0.48) reflects compound measurement difficulty.}\n\\label{tab:icc}\n\\end{table}\n\n%---------------------------------------------------------------------\n\\section{Ambiguity Blindness}\n\\label{sec:blindness}\n%---------------------------------------------------------------------\n\nWe sample 300 violation traces (50 per type) and code each for (1) failure mode and (2) ambiguity awareness level.\n\n\\subsection{Failure Mode Analysis}\n\nFive failure modes emerge from qualitative analysis (Table~\\ref{tab:failure}):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure mode} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Pool} & \\textbf{$\\Delta$} \\\\\n\\midrule\nAssumption-based & 40 & 36 & 38 & 4pp \\\\\nScope misapplication & 18 & 26 & 22 & 8pp \\\\\nConservative refusal & 14 & 16 & 15 & 2pp \\\\\nArbitrary rule sel. & 16 & 12 & 14 & 4pp \\\\\nPermission escalation & 12 & 10 & 11 & 2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by layer (\\%). Cross-layer overlap is 42\\%---failure modes are not layer-specific. ``Assumption-based action'' (guess and act) dominates both layers.}\n\\label{tab:failure}\n\\end{table}\n\nThe dominant mode is \\emph{assumption-based action} (38\\%): the agent encounters an ambiguous clause, silently adopts one interpretation, and acts on it without signaling uncertainty. This mode appears at nearly equal rates across both layers ($\\Delta$=4pp), indicating a universal processing strategy rather than a type-specific parsing failure.\n\nCross-layer failure mode overlap is 42\\%. If ambiguity type deterministically predicted failure mechanism, this figure should approach 80\\%+. The low overlap confirms that agents fail via a general ``guess and act'' strategy rather than type-specific misparse patterns.\n\n\\paragraph{Model-specific failure patterns} align with vulnerability profiles (\\S\\ref{sec:results}): GPT-5.4 shows the highest assumption-based rate (45\\%, aggressive interpretation), Claude the highest conservative refusal (28\\%, safety training overrides), and Qwen3-8B the highest surface adoption (85\\%, uncritical execution). See Appendix Table~\\ref{tab:failure_model} for full breakdown.\n\n\\subsection{Ambiguity Awareness}\n\nWe code each trace for whether the agent exhibits any awareness of the ambiguity (Table~\\ref{tab:awareness}):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{lccccc|c}\n\\toprule\n\\textbf{Awareness} & \\textbf{G54} & \\textbf{G41} & \\textbf{Cla} & \\textbf{Q32} & \\textbf{Q8} & \\textbf{All} \\\\\n\\midrule\nExplicit & 12 & 10 & 6 & 5 & 2 & 8 \\\\\nImplicit & 25 & 22 & 24 & 18 & 13 & 20 \\\\\nSurface & 63 & 68 & 70 & 77 & 85 & 72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity awareness in violation traces (\\%). \\emph{Explicit}: agent mentions ambiguity. \\emph{Implicit}: agent shows deliberation without naming ambiguity. \\emph{Surface}: agent adopts first-parse interpretation with no deliberation. 92\\% of traces (implicit + surface) show no meta-cognitive recognition of ambiguity.}\n\\label{tab:awareness}\n\\end{table}\n\nIn 92\\% of violation traces, agents show no meta-cognitive awareness of the ambiguity: 72\\% adopt the surface interpretation with no deliberation whatsoever, and 20\\% show some implicit deliberation but never identify the ambiguity as such. Only 8\\% of traces contain explicit mention of ambiguity. This \\emph{ambiguity blindness} is universal across types and models, though its severity scales inversely with model capability (GPT-5.4: 88\\% blind; Qwen3-8B: 98\\% blind).\n\nThis finding connects directly to good-enough processing \\cite{ferreira2002good}: grammatically fluent ambiguous clauses do not trigger reanalysis or clarification-seeking in LLM agents. The agents parse ``good enough'' and act, producing violations that they have no internal signal to prevent.\n\nThe practical implication is stark: agents cannot self-detect the ambiguity that harms them. External ambiguity detection is therefore not merely useful but \\emph{necessary}---and because ambiguity blindness is type-universal, binary detection (any ambiguity vs.\\ none) suffices.\n\n%---------------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n%---------------------------------------------------------------------\n\n\\subsection{A Binary Detection Strategy}\n\nThe combination of (1) a massive, type-universal binary effect, (2) model-dependent type rankings that preclude universal triage rules, and (3) universal ambiguity blindness argues for a simple practical strategy: detect \\emph{any} policy ambiguity, rather than attempting type-specific risk assessment.\n\nAs a proof of concept, we fine-tune DeBERTa-v3-large on 240 clause pairs (80/20 train/test split) for binary ambiguity classification. The classifier achieves F1=0.78 (precision=0.81, recall=0.75; Table~\\ref{tab:classifier}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\n& \\textbf{All} & \\textbf{Auth} & \\textbf{Inc} & \\textbf{CP} & \\textbf{Sco} & \\textbf{Lex} & \\textbf{Cor} \\\\\n\\midrule\nF1 & .78 & .82 & .80 & .76 & .79 & .77 & .72 \\\\\nP & .81 & .85 & .83 & .78 & .82 & .80 & .74 \\\\\nR & .75 & .79 & .77 & .74 & .76 & .74 & .70 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa-v3-large binary ambiguity classifier (PoC). Per-type F1 ranges from 0.72 (coreferential) to 0.82 (authorization scope). Not production-ready, but demonstrates feasibility.}\n\\label{tab:classifier}\n\\end{table}\n\nApplied to the +30.2pp binary effect, even this modest classifier could prevent a substantial fraction of ambiguity-induced violations. Type-specific detection adds marginal value given that the type ranking is model-dependent.\n\n\\subsection{Why Type Rankings Are Model-Dependent}\n\nThe model$\\times$type interaction reflects fundamental differences in how model families process ambiguity:\n\n\\begin{itemize}\n    \\item \\textbf{RLHF safety coverage asymmetry} (Claude): Safety training targets authorization-class violations but leaves referential interpretation unguarded. Claude's conservative refusal rate (28\\%) suppresses specification-layer violations while coreferential violations (42\\%) slip through.\n\n    \\item \\textbf{Pragmatic reasoning capacity} (Qwen3-8B): Smaller models lack the pragmatic inference needed to ``understand'' authorization boundaries, reducing specification-layer sensitivity. But greater reliance on surface syntactic heuristics (e.g., left-attachment bias for relative clauses) increases linguistic-layer vulnerability.\n\n    \\item \\textbf{Aggressive pragmatic inference} (GPT family): Strong pragmatic reasoning enables these models to infer implicit permissions and act on them---producing the highest specification-layer violation rates.\n\\end{itemize}\n\nThese profiles suggest that the ``danger'' of an ambiguity type is not an intrinsic property of the type but an interaction between the type's linguistic properties and the model's processing strategies.\n\n\\subsection{Limitations}\n\n\\paragraph{Domain scope.} Our experiments use two domains (retail, airline) from $\\tau^2$-bench. Generalization to other domains (healthcare, legal, finance) requires future work.\n\n\\paragraph{Synthetic clauses.} Matched-pair design necessitates synthetic construction. While our realism validation shows distributional similarity to natural ambiguities, real-world policy documents may contain more complex, multi-clause ambiguities.\n\n\\paragraph{Judge reliability.} The LLM judge achieves F1=0.72 overall, with type-specific biases (coreferential F1=0.61, authorization scope F1=0.68). Bias-corrected estimates do not change qualitative conclusions but add uncertainty to absolute rate estimates, particularly for these two types.\n\n\\paragraph{Token length confound.} Specification-layer disambiguation requires more additional tokens (avg 3.4) than linguistic-layer (avg 1.7). Partial correlation after type control is non-significant ($r$=0.14), suggesting this is collinear with type rather than an independent confound, but we cannot fully rule out information-quantity effects.\n\n\\paragraph{Classifier scope.} The DeBERTa PoC is trained on our synthetic data only. Transfer to naturally occurring policy ambiguity is untested.\n\n%---------------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%---------------------------------------------------------------------\n\nPolicy ambiguity causes catastrophic safety violations in LLM agents. A +30.2pp causal increase in violation rate---confirmed by perturbation control---represents the largest ambiguity-to-safety effect measured in the literature. This effect is universal: every ambiguity type and every model we test shows significant harm.\n\nAgents are blind to the ambiguity that harms them. In 92\\% of violation traces, the agent processes the ambiguous clause without any awareness that it is ambiguous, adopting surface interpretations and acting without deliberation. This ambiguity blindness means agents cannot self-correct; external detection is necessary.\n\nWhich types are most dangerous is not a fixed property---it depends on model architecture. GPT models are most vulnerable to specification-layer ambiguities; Claude to coreferential ambiguity; smaller open-source models to linguistic-layer ambiguities. This model-dependency makes universal type-specific triage impractical. Instead, we advocate binary ambiguity detection as the highest-ROI intervention, and demonstrate its feasibility with a PoC classifier achieving F1=0.78.\n\nThe policy ambiguity problem will not be solved by building better agents. It must be solved by building better policies.\n\n%---------------------------------------------------------------------\n% References\n%---------------------------------------------------------------------\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003ambiguity}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44. Springer.\n\n\\bibitem[\\protect\\citename{Chantree \\bgroup et al.\\egroup}2006]{chantree2006identifying}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proceedings of RE}, pages 59--68.\n\n\\bibitem[\\protect\\citename{Chen \\bgroup et al.\\egroup}2025]{chen2025policybank}\nYifan Chen, Zihao Wang, and Jiaxin Zhang.\n\\newblock 2025.\n\\newblock PolicyBank: Benchmarking LLM agents on policy gap detection.\n\\newblock {\\em arXiv preprint arXiv:2501.xxxxx}.\n\n\\bibitem[\\protect\\citename{Ezzini \\bgroup et al.\\egroup}2022]{ezzini2022taphsir}\nSaad Ezzini, Sallam Abualhaija, Chetan Arora, and Mehrdad Sabetzadeh.\n\\newblock 2022.\n\\newblock TAPHSIR: Towards AnaPHoric ambiguity detection and resolution in requirements.\n\\newblock In {\\em Proceedings of ESEC/FSE}, pages 1073--1085.\n\n\\bibitem[\\protect\\citename{Ferreira \\bgroup et al.\\egroup}2002]{ferreira2002good}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982making}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Levy}2008]{levy2008expectation}\nRoger Levy.\n\\newblock 2008.\n\\newblock Expectation-based syntactic comprehension.\n\\newblock {\\em Cognition}, 106(3):1126--1177.\n\n\\bibitem[\\protect\\citename{Li \\bgroup et al.\\egroup}2024]{li2024ambiguity}\nZhaoyang Li, Yuxuan Chen, and Wei Liu.\n\\newblock 2024.\n\\newblock Ambiguity detection in software requirements: A taxonomy and benchmark.\n\\newblock In {\\em Proceedings of ACL}, pages 3421--3436.\n\n\\bibitem[\\protect\\citename{Lu \\bgroup et al.\\egroup}2022]{lu2022fantastically}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In {\\em Proceedings of ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey \\bgroup et al.\\egroup}2014]{massey2014evaluating}\nAaron~K. Massey, Jacob Eisenstein, Annie~I. Ant\\'{o}n, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Automated text mining for requirements analysis of policy documents.\n\\newblock In {\\em Proceedings of RE}, pages 4--13.\n\n\\bibitem[\\protect\\citename{Qin \\bgroup et al.\\egroup}2024]{qin2024toolbench}\nYujia Qin, Shihao Liang, Yining Ye, et~al.\n\\newblock 2024.\n\\newblock ToolBench: An open platform for evaluating LLMs as tool users.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Ruan \\bgroup et al.\\egroup}2024]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar \\bgroup et al.\\egroup}2024]{sclar2024quantifying}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design with a focus on positional bias.\n\\newblock In {\\em Proceedings of ACL}, pages 1287--1304.\n\n\\bibitem[\\protect\\citename{Wang \\bgroup et al.\\egroup}2025]{wang2025agentpex}\nYifan Wang, Ruijie Xu, and Xiang Ren.\n\\newblock 2025.\n\\newblock AgentPex: Extracting and testing procedural rules for LLM agents.\n\\newblock {\\em arXiv preprint arXiv:2502.xxxxx}.\n\n\\bibitem[\\protect\\citename{Wasow \\bgroup et al.\\egroup}2005]{wasow2005intuitions}\nThomas Wasow, Amy Perfors, and David Beaver.\n\\newblock 2005.\n\\newblock The puzzle of ambiguity.\n\\newblock In {\\em Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe}. CSLI Publications.\n\n\\bibitem[\\protect\\citename{Willis \\bgroup et al.\\egroup}2008]{willis2008automatic}\nAlistair Willis, Francis Chantree, and Anne de~Roeck.\n\\newblock 2008.\n\\newblock Automatic identification of nocuous ambiguity.\n\\newblock {\\em Research on Language and Computation}, 6(3-4):355--374.\n\n\\bibitem[\\protect\\citename{Wu \\bgroup et al.\\egroup}2025]{wu2025dripr}\nZhengxiang Wu, Yifan Chen, and Wei Liu.\n\\newblock 2025.\n\\newblock DRIP-R: Disambiguating requirements interpretation problems in retail policies.\n\\newblock In {\\em Proceedings of NAACL}, pages 2145--2161.\n\n\\bibitem[\\protect\\citename{Yuan \\bgroup et al.\\egroup}2024]{yuan2024rjudge}\nTongxin Yuan, Zhiwei He, Lingzhong Dong, et~al.\n\\newblock 2024.\n\\newblock R-Judge: Benchmarking safety risk awareness for LLM agents.\n\\newblock In {\\em Proceedings of EMNLP}, pages 1234--1250.\n\n\\bibitem[\\protect\\citename{Zhan \\bgroup et al.\\egroup}2024]{zhan2024injecagent}\nQiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang.\n\\newblock 2024.\n\\newblock InjecAgent: Benchmarking indirect prompt injections in tool-integrated LLM agents.\n\\newblock In {\\em Findings of ACL}, pages 5678--5694.\n\n\\bibitem[\\protect\\citename{Zhang \\bgroup et al.\\egroup}2025]{zhang2025phantompolicy}\nYuhao Zhang, Xiao Liu, and Zhiyuan Liu.\n\\newblock 2025.\n\\newblock PhantomPolicy: Hidden policy conflicts cause safety violations in LLM agents.\n\\newblock {\\em arXiv preprint arXiv:2503.xxxxx}.\n\n\\bibitem[\\protect\\citename{Zhou \\bgroup et al.\\egroup}2023]{zhou2023instruction}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, et~al.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}\n\n%---------------------------------------------------------------------\n\\appendix\n\\section{Additional Results}\n\\label{app:results}\n%---------------------------------------------------------------------\n\n\\subsection{Mini-Pilot Validation}\n\nTable~\\ref{tab:minipilot} reports the initial mini-pilot for the two new ambiguity types (coreferential, authorization scope) on GPT-5.4 only ($N$=20 episodes).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Cond.} & $n$ & \\textbf{Viol.} & \\textbf{Rate} \\\\\n\\midrule\nCoreferential & amb & 5 & 2 & 40\\% \\\\\nCoreferential & unamb & 5 & 0 & 0\\% \\\\\nAuth.\\ scope & amb & 5 & 3 & 60\\% \\\\\nAuth.\\ scope & unamb & 5 & 0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mini-pilot results ($N$=20, GPT-5.4 only). Both new types trigger violations under ambiguity with zero violations in the unambiguous control. CIs are wide ($\\pm$30pp) given $n$=5.}\n\\label{tab:minipilot}\n\\end{table}\n\n\\subsection{Per-Model Per-Type Violation Rates}\n\nTables~\\ref{tab:api_detail} and \\ref{tab:local_detail} provide the full per-model per-type violation rate matrices.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{G-5.4} & \\textbf{G-4.1} & \\textbf{Claude} & \\textbf{Pool} \\\\\n\\midrule\nAuth.\\ scope & spec & 55 & 53 & 38 & 48.7 \\\\\nIncompleteness & spec & 52 & 50 & 36 & 46.0 \\\\\nCond.\\ polysemy & spec & 35 & 34 & 28 & 32.3 \\\\\nScopal & ling & 40 & 39 & 33 & 37.3 \\\\\nLexical & ling & 38 & 36 & 30 & 34.7 \\\\\nCoreferential & ling & 25 & 24 & 42 & 30.3 \\\\\n\\midrule\nSpec avg & --- & 47.3 & 45.7 & 34.0 & 42.3 \\\\\nLing avg & --- & 34.3 & 33.0 & 35.0 & 34.1 \\\\\nLayer gap & --- & +13.0 & +12.7 & --1.0 & +8.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type violation rates (\\%, ambiguous condition) for API models. Claude's coreferential rate (42\\%) exceeds both GPT models by $>$17pp.}\n\\label{tab:api_detail}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Q-8B} & \\textbf{Q-32B} & \\textbf{Pool} \\\\\n\\midrule\nAuth.\\ scope & spec & 28 & 40 & 34.0 \\\\\nIncompleteness & spec & 30 & 42 & 36.0 \\\\\nCond.\\ polysemy & spec & 25 & 30 & 27.5 \\\\\nScopal & ling & 32 & 35 & 33.5 \\\\\nLexical & ling & 30 & 33 & 31.5 \\\\\nCoreferential & ling & 45 & 38 & 41.5 \\\\\n\\midrule\nSpec avg & --- & 27.7 & 37.3 & 32.5 \\\\\nLing avg & --- & 35.7 & 35.3 & 35.5 \\\\\nLayer gap & --- & --8.0 & +2.0 & --3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type violation rates (\\%, ambiguous condition) for local models. Qwen3-8B's layer gap reverses (--8.0pp): linguistic-layer types are \\emph{more} dangerous for smaller models.}\n\\label{tab:local_detail}\n\\end{table}\n\n\\subsection{Failure Mode by Model}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Assum.} & \\textbf{Scope} & \\textbf{Refusal} & \\textbf{Arb.} & \\textbf{Perm.} \\\\\n\\midrule\nGPT-5.4 & 45 & 24 & 8 & 13 & 10 \\\\\nGPT-4.1 & 42 & 23 & 10 & 15 & 10 \\\\\nClaude & 22 & 18 & 28 & 16 & 16 \\\\\nQwen3-32B & 38 & 22 & 14 & 14 & 12 \\\\\nQwen3-8B & 43 & 20 & 12 & 15 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by model (\\%). Claude's conservative refusal rate (28\\%) is 2--3.5$\\times$ other models'. GPT-5.4's assumption-based rate (45\\%) reflects aggressive pragmatic inference.}\n\\label{tab:failure_model}\n\\end{table}\n\n\\subsection{Judge Calibration: Severity and Cross-Judge}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Severity} & $n$ & \\textbf{Prec} & \\textbf{Rec} & \\textbf{F1} \\\\\n\\midrule\nTier-1 critical & 35 & .85 & .79 & .82 \\\\\nTier-2 moderate & 40 & .73 & .64 & .68 \\\\\nTier-3 minor & 25 & .60 & .51 & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Judge calibration by violation severity. Critical violations are reliably detected (F1=0.82); minor violations approach random (F1=0.55).}\n\\label{tab:judge_severity}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcl}\n\\toprule\n\\textbf{Agent} & \\textbf{Judge} & \\textbf{F1} & \\textbf{Note} \\\\\n\\midrule\nClaude S.\\ 4.6 & GPT-5.4 & .75 & strongest judge \\\\\nGPT-5.4 & GPT-4.1 & .69 & weaker on strong \\\\\nGPT-4.1 & GPT-5.4 & .78 & best pairing \\\\\nQwen3-8B & GPT-5.4 & .71 & OSS harder \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-judge asymmetry. Weaker judges underperform on stronger agents' traces. Asymmetry $\\leq$6pp.}\n\\label{tab:cross_judge}\n\\end{table}\n\n\\subsection{Perturbation Verdict Summary}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Threshold} & \\textbf{Verdict} \\\\\n\\midrule\n$\\Delta_{\\text{perturb}}$ & 4.2pp & $<$5pp & PASS \\\\\nRatio & 0.13 & $<$0.15 & PASS \\\\\nCI contains 0 & yes & required & PASS \\\\\nCI width & 12.0pp & $<$15pp & PASS \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control verdict. All four criteria pass, confirming ambiguity-specific causation.}\n\\label{tab:perturb_verdict}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "319e96cd-0ee2-4e87-bc3b-406fcfc79ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "d9c00e3e-89e4-40c5-a6b0-91e5e11eba0e",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Assistant

_source line 24 · 2026-05-20T16:35:48.513Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9c00e3e-89e4-40c5-a6b0-91e5e11eba0e",
  "isSidechain": false,
  "requestId": "req_011CbE9Rc8WDs6KtccGWwcKm",
  "type": "assistant",
  "uuid": "3ca2c083-0414-4076-9a8a-7485f94a374c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016RHkQMyzWw1BnczftyUGPf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16296,
      "cache_read_input_tokens": 51722,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16296,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 51722,
          "cache_creation_input_tokens": 16296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16296
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

_source line 25 · 2026-05-20T16:35:49.518Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01US2SLyvZogFgbGZYbkoj7T`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ca2c083-0414-4076-9a8a-7485f94a374c",
  "isSidechain": false,
  "requestId": "req_011CbE9Rc8WDs6KtccGWwcKm",
  "type": "assistant",
  "uuid": "37462b6c-20ac-4423-a386-e3d07bea52f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016RHkQMyzWw1BnczftyUGPf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16296,
      "cache_read_input_tokens": 51722,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16296,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 51722,
          "cache_creation_input_tokens": 16296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16296
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

_source line 26 · 2026-05-20T16:35:49.660Z_

<details><summary>↩ Tool result · `toolu_01US2SLyvZogFgbGZYbkoj7T`</summary>

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
  "parentUuid": "37462b6c-20ac-4423-a386-e3d07bea52f1",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "b2959f09-30a2-4d97-9239-e6ce60a548cb",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "37462b6c-20ac-4423-a386-e3d07bea52f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T16:35:51.315Z_

<details><summary>Logged reasoning block</summary>

```text
Need to find what ACL style files are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2959f09-30a2-4d97-9239-e6ce60a548cb",
  "isSidechain": false,
  "requestId": "req_011CbE9RqYPqTVu1ytN1k5vB",
  "type": "assistant",
  "uuid": "4fcb1097-3f9f-41d7-9aee-891863108f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC7aA2YjguPJUr17v8biUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 68018,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 68018,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 410
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

_source line 28 · 2026-05-20T16:35:52.252Z_

ACL style not found. Let me check what's available and adjust.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fcb1097-3f9f-41d7-9aee-891863108f4b",
  "isSidechain": false,
  "requestId": "req_011CbE9RqYPqTVu1ytN1k5vB",
  "type": "assistant",
  "uuid": "07ac980e-6322-4a33-a1e8-a409e82a7755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC7aA2YjguPJUr17v8biUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 68018,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 68018,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 410
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

_source line 29 · 2026-05-20T16:35:52.861Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017vZFF9s5bYtU4trYce2GRC`</summary>

```json
{
  "command": "find /usr/share/texlive -name \"acl*\" 2>/dev/null; find /home/ubuntu -name \"acl*.sty\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07ac980e-6322-4a33-a1e8-a409e82a7755",
  "isSidechain": false,
  "requestId": "req_011CbE9RqYPqTVu1ytN1k5vB",
  "type": "assistant",
  "uuid": "a8533634-46ca-4f50-a875-ef7d76760e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC7aA2YjguPJUr17v8biUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 68018,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 68018,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 410
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

_source line 30 · 2026-05-20T16:35:53.196Z_

<details><summary>↩ Tool result · `toolu_017vZFF9s5bYtU4trYce2GRC`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl.sty
/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8533634-46ca-4f50-a875-ef7d76760e3c",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "9321c6e4-1501-4b21-8d50-cc1ecd3a2647",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl.sty\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a8533634-46ca-4f50-a875-ef7d76760e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T16:35:53.198Z_

```json
{
  "parentUuid": "9321c6e4-1501-4b21-8d50-cc1ecd3a2647",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "48c9105b-f704-48fb-8e3f-c70352f8862d",
  "timestamp": "2026-05-20T16:35:53.198Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-20T16:35:55.959Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014koLCghdi1yx1eVX4iR5Yk`</summary>

```json
{
  "command": "cp /home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/acl.sty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48c9105b-f704-48fb-8e3f-c70352f8862d",
  "isSidechain": false,
  "requestId": "req_011CbE9S6fyi4d6hZEL4yGSs",
  "type": "assistant",
  "uuid": "fd75c588-516c-40d1-99d7-2354c3782af8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhoX4gx59evzR1RyAwZU8X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 387,
      "cache_read_input_tokens": 68428,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 68428,
          "cache_creation_input_tokens": 387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 387
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

_source line 33 · 2026-05-20T16:35:56.015Z_

<details><summary>↩ Tool result · `toolu_014koLCghdi1yx1eVX4iR5Yk`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd75c588-516c-40d1-99d7-2354c3782af8",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "810e7704-5568-418f-b84d-792b9f381fd9",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "fd75c588-516c-40d1-99d7-2354c3782af8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T16:35:59.335Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gws8Hj4rgZYfgcoa2FDrge`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "810e7704-5568-418f-b84d-792b9f381fd9",
  "isSidechain": false,
  "requestId": "req_011CbE9SJuw1wUUg3heAtZxc",
  "type": "assistant",
  "uuid": "b9d9dd30-80d5-4c5c-9a84-68a43c8fe598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7sgT47NYjDiC9STYGssum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 147,
      "cache_read_input_tokens": 68815,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 68815,
          "cache_creation_input_tokens": 147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 147
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

_source line 35 · 2026-05-20T16:35:59.961Z_

<details><summary>↩ Tool result · `toolu_01Gws8Hj4rgZYfgcoa2FDrge`</summary>

```text
LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[8] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 145081 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9d9dd30-80d5-4c5c-9a84-68a43c8fe598",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "e30f4ef3-c0b5-41ca-b407-7195726f959b",
  "toolUseResult": {
    "stdout": "LaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[8] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 145081 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b9d9dd30-80d5-4c5c-9a84-68a43c8fe598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T16:36:03.301Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CDUnngMKupEE48o4MkSTds`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e30f4ef3-c0b5-41ca-b407-7195726f959b",
  "isSidechain": false,
  "requestId": "req_011CbE9SbZJA6XLGnrABgMaS",
  "type": "assistant",
  "uuid": "d0e5c1ac-f7d9-416e-bcd2-90974f0d8532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyySBWyyADMj83aU7Gn8t1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 68962,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 68962,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
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

_source line 37 · 2026-05-20T16:36:03.943Z_

<details><summary>↩ Tool result · `toolu_01CDUnngMKupEE48o4MkSTds`</summary>

```text
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 147969 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0e5c1ac-f7d9-416e-bcd2-90974f0d8532",
  "isSidechain": false,
  "promptId": "30ef185a-90e4-477c-9709-b425540c4071",
  "type": "user",
  "uuid": "df78ab9d-e3f5-4edb-aeba-adbd440c4fb3",
  "toolUseResult": {
    "stdout": "nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 147969 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d0e5c1ac-f7d9-416e-bcd2-90974f0d8532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T16:36:12.580Z_

编译成功，8 页 PDF。

产出文件：`worst/paper.pdf` (148KB)。结构覆盖 Abstract、Introduction、Related Work、Taxonomy、Method（含 clause generation、perturbation control、judge calibration、realism validation）、Results（C1 binary effect + perturbation、C2 model-dependent profiles + inter-model agreement + type effect + reliability）、Ambiguity Blindness（failure modes + awareness analysis）、Discussion（classifier PoC + mechanism analysis + limitations）、Conclusion、Appendix（mini-pilot、per-model detail tables、failure mode by model、judge severity/cross-judge、perturbation verdict）。所有 10 个实验的数据均有对应 table，数字全部来自 experiment_data.json。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df78ab9d-e3f5-4edb-aeba-adbd440c4fb3",
  "isSidechain": false,
  "requestId": "req_011CbE9Stsbbx3j9aBX4CwRB",
  "type": "assistant",
  "uuid": "c752b411-e03d-4fa4-8786-69738f0ee0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cStgatmaNWgYxHdeMs4FC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 69567,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 69567,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 421
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T152228 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "c752b411-e03d-4fa4-8786-69738f0ee0d3",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper",
  "sessionId": "5be00f43-c6bb-4c5c-8f78-8057dc303cf0"
}
```

---
