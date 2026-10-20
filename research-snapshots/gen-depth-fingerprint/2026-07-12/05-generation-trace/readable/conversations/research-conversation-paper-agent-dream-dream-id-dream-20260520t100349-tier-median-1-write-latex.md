# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/bf76e3fd-e630-4bd3-9134-5a44eba8a7bc.jsonl`
- **Structured JSON:** [`91bcdc72ae7bece20144.json`](../../sessions/91/91bcdc72ae7bece20144.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:33:06.976Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:33:06.976Z",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：3.0 Solid Findings 档位下，核心贡献（DDR + 深度分类 task formulation）被审稿人认可， 但在 scope（base-model only）、novelty（是否只是 vocabulary impoverishment 的衍生）、 practical utility（0.694 F1 + per-gen 0.633-0.724 的方差）上受到中等强度质疑。 Claim 2 的 entropy_std 归类问题被追问；Gemma-2-2B anomaly 被要求显式讨论。 Rebuttal 需回应 2-3 个 medium-severity concerns，但无 fatal flaw。 整体定位：有价值的 empirical contribution，Findings 可接收，但不够 main conference。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T10:33:06.979Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:33:06.979Z",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-20T10:33:06.996Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：3.0 Solid Findings 档位下，核心贡献（DDR + 深度分类 task formulation）被审稿人认可， 但在 scope（base-model only）、novelty（是否只是 vocabulary impoverishment 的衍生）、 practical utility（0.694 F1 + per-gen 0.633-0.724 的方差）上受到中等强度质疑。 Claim 2 的 entropy_std 归类问题被追问；Gemma-2-2B anomaly 被要求显式讨论。 Rebuttal 需回应 2-3 个 medium-severity concerns，但无 fatal flaw。 整体定位：有价值的 empirical contribution，Findings 可接收，但不够 main conference。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "467c464e-1e13-48a4-8d50-0578a2c4b80f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:33:06.996Z_

```json
{
  "parentUuid": "467c464e-1e13-48a4-8d50-0578a2c4b80f",
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
  "uuid": "6feac3c3-7dfa-4fa6-870c-f887d8f8c9a1",
  "timestamp": "2026-05-20T10:33:06.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:33:06.996Z_

```json
{
  "parentUuid": "6feac3c3-7dfa-4fa6-870c-f887d8f8c9a1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d71d3086-d472-466a-88e3-2360c9f717a3",
  "timestamp": "2026-05-20T10:33:06.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
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
  "aiTitle": "Generate median-tier research paper for dream_20260520T100349",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Assistant

_source line 7 · 2026-05-20T10:33:12.579Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d71d3086-d472-466a-88e3-2360c9f717a3",
  "isSidechain": false,
  "requestId": "req_011CbDfmdBoRV86KTfEwGNfm",
  "type": "assistant",
  "uuid": "0f6edb24-5506-4a81-bb62-5367f6cc03ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141g7HRgwts9Zut97XQxFxd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12821,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12821
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

_source line 8 · 2026-05-20T10:33:13.656Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UySXAS6JzT5snw9DRNNeXj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f6edb24-5506-4a81-bb62-5367f6cc03ab",
  "isSidechain": false,
  "requestId": "req_011CbDfmdBoRV86KTfEwGNfm",
  "type": "assistant",
  "uuid": "712d0dee-0e66-4a19-9a75-2f079125a475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141g7HRgwts9Zut97XQxFxd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12821,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12821
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

_source line 9 · 2026-05-20T10:33:13.931Z_

<details><summary>↩ Tool result · `toolu_01UySXAS6JzT5snw9DRNNeXj`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "在 MVP 数据上做三部分分析：(A) 特征消融（full vs reference-only vs surface-only）， (B) H1/H2 趋势分析（每个特征跨 depth 的 Spearman ρ + KS）， (C) perplexity 预验证（Pythia-410M forward pass on depth-stratified subsets）。\n",
5	    "results": {
6	      "full_macro_f1": 0.82,
7	      "full_macro_f1_ci": [
8	        0.805,
9	        0.835
10	      ],
11	      "reference_only_f1": 0.719,
12	      "reference_only_ci": [
13	        0.706,
14	        0.733
15	      ],
16	      "surface_only_f1": 0.763,
17	      "surface_only_ci": [
18	        0.747,
19	        0.774
20	      ],
21	      "mcnemar_full_vs_surface_p": 0.0,
22	      "mcnemar_full_vs_ref_p": 0.0,
23	      "h2_features": [
24	        "entropy_mean",
25	        "ttr",
26	        "hapax_ratio"
27	      ],
28	      "h2_spearman_entropy_mean": -0.6,
29	      "h2_spearman_ttr": -0.61,
30	      "h2_spearman_hapax_ratio": -0.63,
31	      "h1_features": [
32	        "tail_decay",
33	        "entropy_max",
34	        "entropy_min"
35	      ],
36	      "h1_spearman_tail_decay": 0.04,
37	      "h1_spearman_entropy_max": 0.05,
38	      "h1_spearman_entropy_min": -0.3,
39	      "contested_feature": "entropy_std",
40	      "entropy_std_spearman": -0.2,
41	      "entropy_std_ks": 0.15,
42	      "median_ppl_by_depth": [
43	        13.5,
44	        4.96,
45	        3.0,
46	        2.07,
47	        1.72
48	      ],
49	      "ppl_depth_trend": "monotonic_decrease"
50	    },
51	    "tables": [
52	      {
53	        "name": "Table: Feature Ablation (5-fold CV on MVP data)",
54	        "columns": [
55	          "Feature_Set",
56	          "Macro_F1",
57	          "95%_CI",
58	          "N_Features"
59	        ],
60	        "rows": [
61	          [
62	            "Full (7-feature)",
63	            0.82,
64	            "[0.805, 0.835]",
65	            7
66	          ],
67	          [
68	            "Surface-only (TTR + hapax)",
69	            0.763,
70	            "[0.747, 0.774]",
71	            2
72	          ],
73	          [
74	            "Reference-only (entropy + tail)",
75	            0.719,
76	            "[0.706, 0.733]",
77	            5
78	          ]
79	        ]
80	      },
81	      {
82	        "name": "Table: Feature Trend Classification",
83	        "columns": [
84	          "Feature",
85	          "Spearman_ρ",
86	          "KS_stat",
87	          "Trend_Class"
88	        ],
89	        "rows": [
90	          [
91	            "hapax_ratio",
92	            -0.63,
93	            0.537,
94	            "Drifting"
95	          ],
96	          [
97	            "ttr",
98	            -0.61,
99	            0.521,
100	            "Drifting"
101	          ],
102	          [
103	            "entropy_mean",
104	            -0.6,
105	            0.516,
106	            "Drifting"
107	          ],
108	          [
109	            "entropy_min",
110	            -0.3,
111	            0.28,
112	            "Intermediate"
113	          ],
114	          [
115	            "entropy_std",
116	            -0.2,
117	            0.15,
118	            "Contested (d=0.458)"
119	          ],
120	          [
121	            "entropy_max",
122	            0.05,
123	            0.052,
124	            "Stationary"
125	          ],
126	          [
127	            "tail_decay",
128	            0.04,
129	            0.043,
130	            "Stationary"
131	          ]
132	        ]
133	      }
134	    ],
135	    "figures": [],
136	    "analysis": "核心发现成立但有裂缝。Surface-only 0.763 vs full 0.820 的 gap 只有 5.7pp， 审稿人可能认为 \"complementary signal\" 的 framing 对 reference features 的 marginal contribution 过度包装。entropy_std 的 contested 状态是最大叙事风险—— 原始 H1/H2 二分法需要调整为 spectrum（drifting → intermediate → stationary）， 在 paper abstract 中不能回避。\n\n\nMedian 档下，消融结果清晰显示 reference 和 surface 特征互补（McNemar p≈0）， 但 surface-only (0.763) 已接近 full (0.820)，给审稿人留下 \"reference 特征 边际贡献有限\" 的印象。H2 趋势在 entropy_mean/ttr/hapax 上非常强（|ρ|>0.60）， 但 entropy_std (ρ=-0.20) 处于 drifting 和 stationary 之间的灰色地带—— 它的 KS 值 (0.15) 远高于 tail_decay (0.05) 但远低于 hapax (0.54)， 导致二分法（drifting vs stationary）在这个特征上站不住脚。 审稿人会追问为何把 entropy_std 归入 stationary 组（后续 TOST 的 d=0.458  进一步加剧此问题）。Perplexity 随 depth 单调下降（13.50→1.72）证实  depth signal 存在，但也暴露 gen-0 ppl 异常高（seed text 质量差异）， 需要在 paper 中解释。\n"
137	  },
138	  {
139	    "name": "cross_generator_evaluation",
140	    "description": "扩展至 5 个生成器 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)， LOGO CV 评估跨生成器泛化能力。\n",
141	    "results": {
142	      "total_records": 23032,
143	      "generators": [
144	        "pythia-2.8b",
145	        "pythia-1b",
146	        "olmo-2-1b",
147	        "qwen3-1.7b",
148	        "qwen3-0.6b"
149	      ],
150	      "logo_avg_macro_f1": 0.804,
151	      "logo_avg_macro_f1_ci": [
152	        0.786,
153	        0.799
154	      ],
155	      "logo_binary_f1": 0.694,
156	      "logo_binary_f1_ci": [
157	        0.688,
158	        0.7
159	      ],
160	      "per_gen_binary_f1": {
161	        "pythia-2.8b": 0.724,
162	        "pythia-1b": 0.718,
163	        "olmo-2-1b": 0.668,
164	        "qwen3-1.7b": 0.702,
165	        "qwen3-0.6b": 0.659
166	      },
167	      "per_gen_macro_f1": {
168	        "pythia-2.8b": 0.851,
169	        "pythia-1b": 0.831,
170	        "olmo-2-1b": 0.752,
171	        "qwen3-1.7b": 0.805,
172	        "qwen3-0.6b": 0.78
173	      },
174	      "lofo_binary_f1": 0.686,
175	      "lofo_macro_f1": 0.791,
176	      "worst_case_generator": "qwen3-0.6b",
177	      "best_case_generator": "pythia-2.8b",
178	      "per_gen_binary_range": [
179	        0.659,
180	        0.724
181	      ],
182	      "binary_f1_std_across_gens": 0.028,
183	      "top_features_importance": [
184	        "hapax_ratio_0.289",
185	        "ttr_0.168",
186	        "entropy_mean_0.160"
187	      ]
188	    },
189	    "tables": [
190	      {
191	        "name": "Table: LOGO Per-Generator Results",
192	        "columns": [
193	          "Generator",
194	          "Family",
195	          "Params",
196	          "Binary_F1",
197	          "Macro_F1",
198	          "95%_CI_Binary"
199	        ],
200	        "rows": [
201	          [
202	            "Pythia-2.8B",
203	            "Pythia",
204	            "2.8B",
205	            0.724,
206	            0.851,
207	            "[0.710, 0.738]"
208	          ],
209	          [
210	            "Pythia-1B",
211	            "Pythia",
212	            "1B",
213	            0.718,
214	            0.831,
215	            "[0.703, 0.733]"
216	          ],
217	          [
218	            "Qwen3-1.7B",
219	            "Qwen",
220	            "1.7B",
221	            0.702,
222	            0.805,
223	            "[0.687, 0.717]"
224	          ],
225	          [
226	            "OLMo-2-1B",
227	            "OLMo",
228	            "1.5B",
229	            0.668,
230	            0.752,
231	            "[0.652, 0.684]"
232	          ],
233	          [
234	            "Qwen3-0.6B",
235	            "Qwen",
236	            "0.6B",
237	            0.659,
238	            0.78,
239	            "[0.643, 0.675]"
240	          ],
241	          [
242	            "**Average**",
243	            "—",
244	            "—",
245	            "**0.694**",
246	            "**0.804**",
247	            "[0.688, 0.700]"
248	          ]
249	        ]
250	      },
251	      {
252	        "name": "Table: LOFO vs LOGO Comparison",
253	        "columns": [
254	          "Eval_Protocol",
255	          "Binary_F1",
256	          "Macro_F1"
257	        ],
258	        "rows": [
259	          [
260	            "LOGO (leave-one-generator-out)",
261	            0.694,
262	            0.804
263	          ],
264	          [
265	            "LOFO (leave-one-family-out)",
266	            0.686,
267	            0.791
268	          ],
269	          [
270	            "Δ",
271	            -0.008,
272	            -0.013
273	          ]
274	        ]
275	      }
276	    ],
277	    "figures": [],
278	    "analysis": "LOGO binary F1=0.694 是 paper 的 headline metric，在 median 档下被审稿人 标注为 \"modest\"。Per-gen range 0.659-0.724 的 variance 是一个 moderate concern： worst-case (Qwen3-0.6B at 0.659) 的实用性被质疑。Pythia 家族两个模型都偏高 增加了 family leakage 的可信度问题，但 LOFO (0.686) 与 LOGO (0.694)  差距仅 0.8pp，可在 rebuttal 中论证 leakage 影响有限。\n\n\nMedian 档下，LOGO 跨生成器平均 macro F1 达到 0.804（solid），但 binary F1  只有 0.694——这个数字成为审稿人 \"modest performance\" 评价的核心锚点。 Per-gen binary F1 从 0.659 (Qwen3-0.6B) 到 0.724 (Pythia-2.8B) 的 6.5pp  spread 说明方法对生成器敏感。两个 Pythia 模型 (2.8B: 0.724, 1B: 0.718)  都偏高，暗示 Pythia 家族内部信息泄露可能膨胀了 LOGO 的平均值—— LOFO (0.686) 比 LOGO (0.694) 低 0.8pp 证实了这一点但差距不大。 OLMo-2-1B 和 Qwen3-0.6B 作为 held-out 时 F1 较低，表明跨架构泛化  存在 gap。审稿人不会认为这是 failure，但会标注为 \"moderate generalization\"。\n"
279	  },
280	  {
281	    "name": "cross_family_reference_model",
282	    "description": "用 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model（取代 Pythia-410M）， 验证 DDR 趋势是否为 generation-intrinsic 而非 reference-model artifact。\n",
283	    "results": {
284	      "logo_f1_pythia_ref": 0.803,
285	      "logo_f1_olmo_ref": 0.807,
286	      "logo_f1_qwen_ref": 0.816,
287	      "entropy_drift_all_refs_negative": true,
288	      "pythia_ref_drift_range": [
289	        -1.19,
290	        -1.4
291	      ],
292	      "olmo_ref_drift_range": [
293	        -0.61,
294	        -0.91
295	      ],
296	      "qwen_ref_drift_range": [
297	        -0.96,
298	        -1.35
299	      ],
300	      "dual_dynamics_is_pythia_artifact": false,
301	      "shape_features_stationary_all_refs": true,
302	      "tail_decay_cross_ref_ks_max": 0.06,
303	      "entropy_std_cross_ref_inconsistency": true,
304	      "entropy_std_d_pythia": 0.458,
305	      "entropy_std_d_olmo": 0.31,
306	      "entropy_std_d_qwen": 0.52
307	    },
308	    "tables": [
309	      {
310	        "name": "Table: Cross-Reference-Model LOGO F1",
311	        "columns": [
312	          "Reference_Model",
313	          "Params",
314	          "LOGO_Macro_F1",
315	          "entropy_mean_ρ",
316	          "tail_decay_ρ"
317	        ],
318	        "rows": [
319	          [
320	            "Pythia-410M",
321	            "410M",
322	            0.803,
323	            -0.6,
324	            0.04
325	          ],
326	          [
327	            "OLMo-2-1B",
328	            "1.5B",
329	            0.807,
330	            -0.52,
331	            0.06
332	          ],
333	          [
334	            "Qwen3-0.6B",
335	            "0.6B",
336	            0.816,
337	            -0.58,
338	            0.03
339	          ]
340	        ]
341	      },
342	      {
343	        "name": "Table: entropy_std Cohen's d Across Reference Models",
344	        "columns": [
345	          "Reference_Model",
346	          "entropy_std_d",
347	          "TOST_rejection",
348	          "Classification"
349	        ],
350	        "rows": [
351	          [
352	            "Pythia-410M",
353	            0.458,
354	            "0/1000",
355	            "Contested"
356	          ],
357	          [
358	            "OLMo-2-1B",
359	            0.31,
360	            "partial",
361	            "Borderline stationary"
362	          ],
363	          [
364	            "Qwen3-0.6B",
365	            0.52,
366	            "0/1000",
367	            "Contested"
368	          ]
369	        ]
370	      }
371	    ],
372	    "figures": [],
373	    "analysis": "DDR 的 generation-intrinsic 属性得到验证，这是 median 档下最强的子结果。 但 reference model 选择对 drift magnitude 的影响（最大 2× 差异）是审稿人 可能追问的 nuance——需要在 paper 中透明报告。entropy_std 跨 reference  不一致性为将其重新归类为 \"intermediate\" 提供了额外证据。\n\n\nMedian 档的关键 falsification test 通过：DDR 趋势在三个不同 reference model  下均成立（drift 方向一致为负），排除了 Pythia-specific artifact 假说。 这是 Claim 2 的核心支撑，审稿人会认可。但细节上，drift 幅度差异大 （OLMo ref drift 仅 -0.61 到 -0.91，约为 Pythia ref 的一半）， 说明 reference model 选择影响 signal 强度——审稿人会要求讨论。 entropy_std 的跨 reference 不一致性（d 从 0.31 到 0.52）进一步 削弱了它的 \"stationary\" 归类，支持将其移入 \"intermediate\" 类别。 Qwen ref 略微优于 Pythia ref（0.816 vs 0.803），暗示小模型 reference  不一定最优，但差异在 CI 重叠范围内。\n"
374	  },
375	  {
376	    "name": "downstream_utility",
377	    "description": "Fine-tune OLMo-1B on depth-stratified subsets (all / depth0-1 / size-matched /  binary-filtered / depth0-only)，3 seeds with bootstrap CIs，测量 perplexity 差异。\n",
378	    "results": {
379	      "total_runs": 15,
380	      "variants": {
381	        "all": {
382	          "train_n": 12299,
383	          "ppl_mean": 2.335,
384	          "ppl_std": 0.0003
385	        },
386	        "size_matched": {
387	          "train_n": 3951,
388	          "ppl_mean": 2.367,
389	          "ppl_std": 0.0002
390	        },
391	        "depth01": {
392	          "train_n": 3951,
393	          "ppl_mean": 2.387,
394	          "ppl_std": 0.001
395	        },
396	        "binary_filtered": {
397	          "train_n": 3951,
398	          "ppl_mean": 2.389,
399	          "ppl_std": 0.001
400	        },
401	        "depth0_only": {
402	          "train_n": 797,
403	          "ppl_mean": 2.681,
404	          "ppl_std": 0.001
405	        }
406	      },
407	      "ranking": "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)",
408	      "tost_equal_count_p": 0.00011,
409	      "tost_equal_count_margin": "±2%",
410	      "tost_all_vs_filtered_p": 0.15,
411	      "tost_all_vs_filtered_margin": "±2%",
412	      "tost_all_vs_filtered_margin_3pct_p": 0.003,
413	      "cohens_d_size_matched_vs_depth01": 0.85,
414	      "seed_variance": "<0.002 ppl across seeds",
415	      "negative_finding_confirmed": true
416	    },
417	    "tables": [
418	      {
419	        "name": "Table: Downstream CLM Perplexity by Training Data Composition",
420	        "columns": [
421	          "Variant",
422	          "Train_N",
423	          "Ppl_Mean",
424	          "Ppl_Std",
425	          "Δ_vs_SizeMatched"
426	        ],
427	        "rows": [
428	          [
429	            "All depths",
430	            12299,
431	            2.335,
432	            0.0003,
433	            "-0.032 (more data)"
434	          ],
435	          [
436	            "Size-matched random",
437	            3951,
438	            2.367,
439	            0.0002,
440	            "—(baseline)"
441	          ],
442	          [
443	            "Depth 0+1 only",
444	            3951,
445	            2.387,
446	            0.001,
447	            "+0.020"
448	          ],
449	          [
450	            "Binary-filtered",
451	            3951,
452	            2.389,
453	            0.001,
454	            "+0.022"
455	          ],
456	          [
457	            "Depth 0 only",
458	            797,
459	            2.681,
460	            0.001,
461	            "+0.314"
462	          ]
463	        ]
464	      },
465	      {
466	        "name": "Table: TOST Equivalence Tests",
467	        "columns": [
468	          "Comparison",
469	          "Margin",
470	          "p_value",
471	          "Equivalent"
472	        ],
473	        "rows": [
474	          [
475	            "size_matched vs depth01",
476	            "±2%",
477	            0.00011,
478	            true
479	          ],
480	          [
481	            "size_matched vs binary_filtered",
482	            "±2%",
483	            8.3e-05,
484	            true
485	          ],
486	          [
487	            "all vs size_matched",
488	            "±2%",
489	            0.15,
490	            false
491	          ],
492	          [
493	            "all vs size_matched",
494	            "±3%",
495	            0.003,
496	            true
497	          ]
498	        ]
499	      }
500	    ],
501	    "figures": [],
502	    "analysis": "Negative finding 成立且叙事清晰：depth fingerprinting 是 diagnostic 工具， 不是 curative 工具。但 3 seeds + single metric 是审稿人的合理质疑点—— 在 median 档下不会导致 reject 但会在 review 中被标记为 \"limited evidence\"， 需要在 rebuttal 中承认并论证 seed variance 极小说明更多 seeds 不会改变结论。\n\n\nMedian 档下 Claim 3 的 negative finding 成立但 evidence 被认为 limited。 核心结果：等样本量下 size_matched (2.367) vs depth01 (2.387) 差异仅 0.020 ppl， TOST 在 ±2% margin 下确认 equivalence (p=1.1e-4)。但审稿人会质疑： (1) 只有 3 seeds——seed variance 极小 (<0.002) 说明 variance 来源不在 seed  而在 data composition，但 3 seeds 仍显 underpowered。 (2) 单一 metric (perplexity)——不涵盖 downstream task performance、 toxicity、factuality 等维度。 (3) all (12299) vs filtered (3951) 的 TOST 需要放宽到 ±3% 才 reject， 说明 data quantity 效应存在但被标注为 \"modest\"。 depth0_only (2.681) 显著差于其他——符合预期（只有 797 samples + 只有 seed text）， 反而支持 \"更多 synthetic data 不 hurt\" 的叙事。\n"
503	  },
504	  {
505	    "name": "prompt_type_comparison",
506	    "description": "对比 continuation / elaboration / inspired_rewriting 三种 prompt 类型的 depth signal 保留度和分类性能。Pythia-2.8B, 1000 seeds。\n",
507	    "results": {
508	      "cv_f1": {
509	        "continuation": 0.781,
510	        "elaboration": 0.73,
511	        "inspired_rewriting": 0.737
512	      },
513	      "lopto_f1": {
514	        "held_out_continuation": 0.762,
515	        "held_out_elaboration": 0.762,
516	        "held_out_rewriting": 0.733,
517	        "avg": 0.753
518	      },
519	      "depth_retention_d4_d0": {
520	        "continuation": 0.831,
521	        "elaboration": 0.986,
522	        "inspired_rewriting": 0.939
523	      },
524	      "drift_hapax_ratio": {
525	        "continuation": -0.74,
526	        "elaboration": -0.83,
527	        "rewriting": -0.8
528	      },
529	      "drift_entropy_mean": {
530	        "continuation": -0.56,
531	        "elaboration": -0.47,
532	        "rewriting": -0.48
533	      },
534	      "semantic_divergence_ranking": "continuation > rewriting > elaboration",
535	      "f1_ranking": "continuation > rewriting > elaboration"
536	    },
537	    "tables": [
538	      {
539	        "name": "Table: Prompt Type Comparison",
540	        "columns": [
541	          "Prompt_Type",
542	          "CV_F1",
543	          "LOPTO_F1",
544	          "Depth_Retention",
545	          "hapax_ρ",
546	          "entropy_mean_ρ"
547	        ],
548	        "rows": [
549	          [
550	            "Continuation",
551	            0.781,
552	            0.762,
553	            0.831,
554	            -0.74,
555	            -0.56
556	          ],
557	          [
558	            "Inspired rewriting",
559	            0.737,
560	            0.733,
561	            0.939,
562	            -0.8,
563	            -0.48
564	          ],
565	          [
566	            "Elaboration",
567	            0.73,
568	            0.762,
569	            0.986,
570	            -0.83,
571	            -0.47
572	          ]
573	        ]
574	      }
575	    ],
576	    "figures": [],
577	    "analysis": "Prompt type 对 depth signal 有系统性影响（continuation > rewriting > elaboration）， 且影响方向与语义发散度一致。这支持 DDR 的 mechanistic interpretation： 更大的语义偏移→更强的 distributional shift→更易分类。但 elaboration 的 hapax drift (-0.83) 反而比 continuation (-0.74) 更强，说明 lexical  impoverishment 和 distributional shift 不完全共线——这是一个 subtle finding， 在 median 档下审稿人可能注意到但不会深究。\n\n\nMedian 档下，三种 prompt 类型均表现出 DDR 趋势，但强度和模式不同。 Continuation (F1=0.781) 最高，因为语义发散最大（每一步生成新内容而非 紧扣原文），distributional shift 更剧烈。Elaboration (F1=0.730) 最低， 因为 elaboration 保持话题一致性（retention 0.986），distributional features  变化较缓。这个排序符合直觉但也暴露问题：审稿人会问 \"如果 continuation  vs elaboration 差 5pp，那 real-world 混合 prompt 场景下性能如何？\" Paper 需要报告 cross-prompt-type transfer（lopto），avg 0.753 表明 prompt-type 泛化合理但非完美。审稿人不会在这个实验上深入追问—— 它是 supporting evidence，不是 core claim。\n"
578	  },
579	  {
580	    "name": "paraphrastic_comparison",
581	    "description": "构建 paraphrastic chains 与 continuation chains 做直接对比， 测试 attractor convergence theory（paraphrasing 是否更快收敛）。\n",
582	    "results": {
583	      "paraphrastic_cv_f1": 0.62,
584	      "paraphrastic_ci": [
585	        0.6,
586	        0.64
587	      ],
588	      "continuation_cv_f1": 0.781,
589	      "continuation_ci": [
590	        0.765,
591	        0.797
592	      ],
593	      "delta_pp": -16.1,
594	      "paraphrastic_depth_retention_d4_d0": 0.97,
595	      "paraphrastic_hapax_drift": -0.35,
596	      "paraphrastic_entropy_mean_drift": -0.22,
597	      "attractor_effect_observed": true,
598	      "binary_f1_paraphrastic": 0.55,
599	      "binary_f1_continuation": 0.694
600	    },
601	    "tables": [
602	      {
603	        "name": "Table: Paraphrastic vs Non-Paraphrastic Chains",
604	        "columns": [
605	          "Chain_Type",
606	          "CV_F1",
607	          "Binary_F1",
608	          "hapax_ρ",
609	          "entropy_mean_ρ",
610	          "Retention_d4"
611	        ],
612	        "rows": [
613	          [
614	            "Continuation",
615	            0.781,
616	            0.694,
617	            -0.74,
618	            -0.56,
619	            0.831
620	          ],
621	          [
622	            "Paraphrastic",
623	            0.62,
624	            0.55,
625	            -0.35,
626	            -0.22,
627	            0.97
628	          ],
629	          [
630	            "Δ",
631	            -0.161,
632	            -0.144,
633	            "+0.39 (weaker)",
634	            "+0.34 (weaker)",
635	            "+0.139"
636	          ]
637	        ]
638	      }
639	    ],
640	    "figures": [],
641	    "analysis": "结果清晰支持 scope boundary：本方法不适用于 paraphrastic chains。 这对论文定位有利（honest scoping），但也意味着方法的实用场景被进一步缩窄—— 在 median 档下，审稿人会在 \"practical relevance\" 维度扣 0.25-0.5pp。\n\n\nMedian 档下，paraphrastic chains 的 depth signal 显著弱于 continuation chains （F1 0.62 vs 0.781, -16pp），符合 attractor convergence theory 预测： paraphrasing 保持语义不变，distributional features 快速收敛到 attractor， 深度间差异被压缩。hapax drift 仅 -0.35（vs continuation -0.74）， entropy_mean drift 仅 -0.22（vs -0.56）。这验证了 paper 的核心 scope claim： 方法针对 non-paraphrastic chains，paraphrastic 场景需要不同方法。 审稿人会认为这是 expected result（不加分也不扣分），但写入 paper  有助于 position scope boundary。Binary F1 只有 0.55 进一步说明 gen-1/gen-2+ 在 paraphrastic 链中几乎不可区分。\n"
642	  },
643	  {
644	    "name": "cross_model_chains",
645	    "description": "Cross-model chains：每个 depth step 用不同生成器，模拟 real-world  web contamination（多源 LLM 混合）。\n",
646	    "results": {
647	      "cross_model_binary_f1": 0.83,
648	      "cross_model_binary_ci": [
649	        0.815,
650	        0.845
651	      ],
652	      "cross_model_3class_f1": 0.789,
653	      "cross_model_3class_ci": [
654	        0.775,
655	        0.803
656	      ],
657	      "single_model_binary_f1_ref": 0.694,
658	      "delta_vs_single_model": "+0.136",
659	      "n_generators_in_pool": 5,
660	      "generator_level_logo_f1": 0.83,
661	      "heterogeneity_amplifies_signal": true,
662	      "per_depth_f1": {
663	        "gen0": 0.95,
664	        "gen1": 0.82,
665	        "gen2plus": 0.78
666	      }
667	    },
668	    "tables": [
669	      {
670	        "name": "Table: Single-Model vs Cross-Model Chains",
671	        "columns": [
672	          "Setup",
673	          "Binary_F1",
674	          "3-Class_F1",
675	          "N_Generators",
676	          "Eval_Protocol"
677	        ],
678	        "rows": [
679	          [
680	            "Single-model (LOGO)",
681	            0.694,
682	            0.762,
683	            "5 (1 per chain)",
684	            "LOGO"
685	          ],
686	          [
687	            "Cross-model (LOGO)",
688	            0.83,
689	            0.789,
690	            "5 (mixed per chain)",
691	            "Generator-LOGO"
692	          ],
693	          [
694	            "Δ",
695	            "+0.136",
696	            "+0.027",
697	            "—",
698	            "—"
699	          ]
700	        ]
701	      }
702	    ],
703	    "figures": [],
704	    "analysis": "Cross-model 的高 F1 是 paper 的 second headline result，在 median 档下 被审稿人接受为有趣且 practically relevant。但 \"是否在学 generator identity\"  的质疑需要用 feature importance 分析回应——如果 cross-model 下 shape features  importance 上升，说明分类器确实在用 depth-related signal。\n\n\nMedian 档下最 surprising 的正面结果：cross-model chains binary F1=0.830  远高于 single-model 0.694（+13.6pp）。原因：不同生成器在每个 depth step  引入不同的 distributional signature，generator heterogeneity 放大了  depth-to-depth 的 feature variance，使分类更容易。这对 practical relevance  有利——real-world 的多源 LLM 混合场景恰好是 DDR 最强的条件。 但审稿人会质疑：(1) cross-model setup 中分类器是否在学习 \"generator identity\"  而非 \"depth\"？(2) 5-gen pool 是否过小？在 median 档下这被标为 minor concern， 不影响 acceptance。LOGO evaluation 确保没有 generator leakage。\n"
705	  },
706	  {
707	    "name": "multi_domain_seeds",
708	    "description": "扩展到 4 个 domain (Wikipedia, news, scientific, creative/code)， 500 seeds × 5 depths per domain，测试 domain independence。\n",
709	    "results": {
710	      "wikipedia_binary_f1": 0.695,
711	      "news_binary_f1": 0.712,
712	      "academic_binary_f1": 0.628,
713	      "code_binary_f1": 0.687,
714	      "overall_binary_f1": 0.676,
715	      "overall_binary_ci": [
716	        0.664,
717	        0.688
718	      ],
719	      "max_gap_vs_wiki_pp": 6.7,
720	      "worst_domain": "academic",
721	      "best_new_domain": "news",
722	      "domain_independent_label": "moderate",
723	      "cross_domain_transfer_f1": 0.65,
724	      "ddr_trend_preserved_all_domains": true
725	    },
726	    "tables": [
727	      {
728	        "name": "Table: Multi-Domain Binary F1",
729	        "columns": [
730	          "Domain",
731	          "Binary_F1",
732	          "95%_CI",
733	          "hapax_ρ",
734	          "entropy_mean_ρ"
735	        ],
736	        "rows": [
737	          [
738	            "News",
739	            0.712,
740	            "[0.690, 0.733]",
741	            -0.65,
742	            -0.58
743	          ],
744	          [
745	            "Wikipedia",
746	            0.695,
747	            "[0.675, 0.715]",
748	            -0.63,
749	            -0.6
750	          ],
751	          [
752	            "Code",
753	            0.687,
754	            "[0.664, 0.710]",
755	            -0.58,
756	            -0.55
757	          ],
758	          [
759	            "Academic",
760	            0.628,
761	            "[0.603, 0.652]",
762	            -0.52,
763	            -0.48
764	          ]
765	        ]
766	      }
767	    ],
768	    "figures": [],
769	    "analysis": "Domain independence 部分成立（趋势保留），但性能 gap 存在。Academic domain  的弱表现可以在 paper 中用 \"低 baseline vocabulary diversity\" 解释， 但需要显式讨论。这个实验在 median 档下为 Claim 1 增加了 moderate support， 但也暴露了 method 在 specialized text domains 的局限。\n\n\nMedian 档下，DDR 趋势在所有 domain 中保留，但分类性能有 domain 依赖性。 Academic domain 最弱 (0.628)——scientific text 的 vocabulary 本身就 specialized  且 low-diversity（术语重复率高），压缩了 surface features 的 discriminative range。 News (0.712) 最强——新闻文体的 vocabulary diversity 高，depth-driven  impoverishment 更易检测。Wikipedia (0.695) 接近 LOGO average  （训练数据的主要来源就是 Wiki seeds）。Code domain (0.687) 意外接近 Wiki， 因为代码的 token distribution 有独特结构。 审稿人会关注 academic domain 的 gap (−6.7pp vs Wiki)，但作为 Findings paper  这个 cross-domain analysis 是 bonus evidence，不是 core claim。\n"
770	  },
771	  {
772	    "name": "finer_grained_ordinal",
773	    "description": "5-class ordinal classification (gen-0 through gen-4)，测试 3-class  之外是否有更多 depth signal。附带 ordinal methods (CORAL, Frank-Hall)。\n",
774	    "results": {
775	      "five_class_macro_f1": 0.5,
776	      "five_class_ci": [
777	        0.48,
778	        0.52
779	      ],
780	      "three_class_macro_f1_ref": 0.762,
781	      "delta_5class_vs_3class": -0.262,
782	      "coral_f1": 0.5,
783	      "frank_hall_f1": 0.49,
784	      "standard_xgboost_f1": 0.5,
785	      "ordinal_methods_improve": false,
786	      "per_class_5class_f1": {
787	        "gen0": 0.92,
788	        "gen1": 0.55,
789	        "gen2": 0.35,
790	        "gen3": 0.3,
791	        "gen4": 0.38
792	      },
793	      "bottleneck": "gen-2/gen-3 boundary (practically indistinguishable)",
794	      "confusion_concentration": "gen-2 and gen-3 mutually confused (65% of errors)"
795	    },
796	    "tables": [
797	      {
798	        "name": "Table: 5-Class vs 3-Class Ordinal Classification",
799	        "columns": [
800	          "N_Classes",
801	          "Method",
802	          "Macro_F1",
803	          "Gen-0_F1",
804	          "Gen-1_F1",
805	          "Gen-2(+)_F1"
806	        ],
807	        "rows": [
808	          [
809	            3,
810	            "XGBoost",
811	            0.762,
812	            0.95,
813	            0.68,
814	            0.66
815	          ],
816	          [
817	            5,
818	            "XGBoost",
819	            0.5,
820	            0.92,
821	            0.55,
822	            "0.35/0.30/0.38"
823	          ],
824	          [
825	            5,
826	            "CORAL",
827	            0.5,
828	            0.91,
829	            0.56,
830	            "0.34/0.31/0.38"
831	          ],
832	          [
833	            5,
834	            "Frank-Hall",
835	            0.49,
836	            0.9,
837	            0.54,
838	            "0.33/0.30/0.37"
839	          ]
840	        ]
841	      }
842	    ],
843	    "figures": [],
844	    "analysis": "5-class 结果清晰支持 paper 的 \"3-class ceiling\" claim。无需调整叙事。 Gen-1/gen-2+ boundary 是分辨率瓶颈（86% binary errors as FN）， 更细分只会引入更多 noise。这个实验是 clean negative result，审稿人不会追问。\n\n\nMedian 档下，5-class F1 约 0.50——比 3-class (0.762) 下降 26pp， 证实 3-class 是 practical resolution ceiling。Gen-2/gen-3/gen-4 之间 几乎不可区分（F1 分别为 0.35/0.30/0.38），因为 features 在 depth ≥2 后 趋于饱和（DDR 的 drift 是减速的，不是线性的）。Ordinal methods (CORAL,  Frank-Hall) 未改善性能——说明瓶颈不在 model structure 而在 feature signal。 审稿人会接受 \"3-class resolution ceiling\" 的结论，这是 honest limitation。 Gen-4 的 F1 (0.38) 反而略高于 gen-3 (0.30)，可能是因为 gen-4  features 已极度偏离 gen-0 baseline，形成了另一个 discriminative boundary。\n"
845	  },
846	  {
847	    "name": "human_edit_robustness",
848	    "description": "Robustness to simulated human edits: (A) random word replacement (5/10/20%),  (B) LLM-simulated rephrasing。\n",
849	    "results": {
850	      "baseline_binary_f1": 0.695,
851	      "random_5pct_f1": 0.65,
852	      "random_10pct_f1": 0.614,
853	      "random_20pct_f1": 0.591,
854	      "llm_rephrase_binary_f1": 0.647,
855	      "llm_rephrase_ci": [
856	        0.631,
857	        0.662
858	      ],
859	      "llm_rephrase_multiclass_f1": 0.667,
860	      "edit_distance_ratio": 0.507,
861	      "avg_sentences_replaced": 1.69,
862	      "graceful_degradation": true,
863	      "catastrophic_threshold": ">20% random replacement",
864	      "delta_5pct": -0.046,
865	      "delta_10pct": -0.081,
866	      "delta_20pct": -0.104,
867	      "delta_llm_rephrase": -0.045
868	    },
869	    "tables": [
870	      {
871	        "name": "Table: Robustness to Human Editing",
872	        "columns": [
873	          "Edit_Type",
874	          "Edit_Rate",
875	          "Binary_F1",
876	          "Δ_vs_Baseline"
877	        ],
878	        "rows": [
879	          [
880	            "None (baseline)",
881	            "0%",
882	            0.695,
883	            "—"
884	          ],
885	          [
886	            "Random replacement",
887	            "5%",
888	            0.65,
889	            -0.046
890	          ],
891	          [
892	            "Random replacement",
893	            "10%",
894	            0.614,
895	            -0.081
896	          ],
897	          [
898	            "Random replacement",
899	            "20%",
900	            0.591,
901	            -0.104
902	          ],
903	          [
904	            "LLM rephrasing",
905	            "~50% edit dist",
906	            0.647,
907	            -0.045
908	          ]
909	        ]
910	      }
911	    ],
912	    "figures": [],
913	    "analysis": "Graceful degradation 成立。审稿人在 median 档下对此满意， 但会在 limitations 中注明 \"real-world editing patterns may differ from  random replacement and LLM rephrasing\"。\n\n\nMedian 档下，method 在 light editing 下展现 graceful degradation： 5% random replacement 仅降 4.6pp (0.695→0.650)，LLM rephrasing 降 4.5pp  (0.695→0.647)。审稿人会认为这个 robustness 是 \"acceptable but not impressive\"—— real-world human editing 通常比 5% random replacement 更 targeted 也更 destructive。 20% replacement 下降至 0.591（-10.4pp），说明 heavy editing 破坏 depth signal。 LLM rephrasing（avg 1.69 sentences replaced, edit distance 0.507）接近 5%  random 的效果，说明 LLM-style editing 是一种 moderate perturbation。 审稿人不会在这个实验上深入追问——它作为 appendix material 回应 RC5 即可。\n"
914	  },
915	  {
916	    "name": "ld_score_feature",
917	    "description": "加入 LD-Score (character-level distribution signature) 作为第 8 个特征， 测试 character-level signal 是否与 token-level features 互补。\n",
918	    "results": {
919	      "seven_feature_f1": 0.804,
920	      "eight_feature_with_ld_f1": 0.811,
921	      "delta": "+0.007",
922	      "ld_score_importance_rank": "6/8 (below entropy_mean, above entropy_min)",
923	      "ld_score_spearman_depth": -0.42,
924	      "ld_score_solo_f1": 0.721,
925	      "ld_score_is_drifting": true,
926	      "ld_score_corr_with_hapax": 0.68,
927	      "marginal_contribution_significant": false,
928	      "mcnemar_p_7_vs_8": 0.12
929	    },
930	    "tables": [
931	      {
932	        "name": "Table: LD-Score Feature Addition",
933	        "columns": [
934	          "Feature_Set",
935	          "N_Features",
936	          "Macro_F1",
937	          "Binary_F1",
938	          "McNemar_p"
939	        ],
940	        "rows": [
941	          [
942	            "7-feature baseline",
943	            7,
944	            0.804,
945	            0.694,
946	            "—"
947	          ],
948	          [
949	            "+ LD-Score",
950	            8,
951	            0.811,
952	            0.699,
953	            0.12
954	          ],
955	          [
956	            "LD-Score only",
957	            1,
958	            0.721,
959	            0.64,
960	            "—"
961	          ]
962	        ]
963	      }
964	    ],
965	    "figures": [],
966	    "analysis": "LD-Score 不改变 headline numbers。作为 appendix 中 \"character-level  features provide redundant signal\" 的 evidence 有价值，支持论文选择  token-level features 的 design decision。\n\n\nMedian 档下，LD-Score 作为单独特征表现不错（solo F1=0.721），但加入 7-feature  ensemble 后边际贡献仅 +0.7pp (0.804→0.811)，McNemar p=0.12 不显著。 原因：LD-Score 与 hapax_ratio 相关性高（r=0.68），character-level  和 token-level vocabulary diversity 高度共线。LD-Score 属于 drifting 类别 （ρ=-0.42），进一步支持 DDR 中 central-tendency features drift 的结论， 但不提供独立信息。审稿人不会对这个结果有强烈反应——它是 nice-to-have  analysis，写入 appendix 即可。不建议将 LD-Score 加入 main feature set  以保持 7-feature 的简洁叙事。\n"
967	  },
968	  {
969	    "name": "end_to_end_classifier",
970	    "description": "QLoRA fine-tuned small LM (OLMo-1B-Instruct or Qwen3-1.7B) for end-to-end  depth classification，对比 handcrafted features。\n",
971	    "results": {
972	      "qlora_3class_f1_instruct": 0.89,
973	      "qlora_3class_ci": [
974	        0.88,
975	        0.91
976	      ],
977	      "qlora_binary_f1_instruct": 0.84,
978	      "qlora_binary_ci": [
979	        0.82,
980	        0.85
981	      ],
982	      "qlora_5class_f1": 0.6,
983	      "seven_feature_3class_f1_ref": 0.762,
984	      "seven_feature_binary_f1_ref": 0.694,
985	      "delta_3class": "+0.128",
986	      "delta_binary": "+0.146",
987	      "qlora_base_3class_f1": 0.86,
988	      "qlora_base_binary_f1": 0.79,
989	      "inference_cost_ratio": "~150× (1B model vs 410M ref + XGBoost)",
990	      "gpu_memory_gb": 4.2,
991	      "training_time_minutes": 28
992	    },
993	    "tables": [
994	      {
995	        "name": "Table: Handcrafted vs End-to-End Classification",
996	        "columns": [
997	          "Method",
998	          "3-Class_F1",
999	          "Binary_F1",
1000	          "5-Class_F1",
1001	          "Inference_Cost"
1002	        ],
1003	        "rows": [
1004	          [
1005	            "7-feature XGBoost",
1006	            0.762,
1007	            0.694,
1008	            0.5,
1009	            "1× (410M ref)"
1010	          ],
1011	          [
1012	            "QLoRA OLMo-1B-Instruct",
1013	            0.889,
1014	            0.836,
1015	            0.598,
1016	            "~150×"
1017	          ],
1018	          [
1019	            "QLoRA Qwen3-1.7B-Instruct",
1020	            0.907,
1021	            0.867,
1022	            0.551,
1023	            "~250×"
1024	          ],
1025	          [
1026	            "QLoRA OLMo-1B-Base",
1027	            0.859,
1028	            0.793,
1029	            0.54,
1030	            "~150×"
1031	          ],
1032	          [
1033	            "QLoRA Qwen3-1.7B-Base",
1034	            0.904,
1035	            0.86,
1036	            0.554,
1037	            "~250×"
1038	          ]
1039	        ]
1040	      }
1041	    ],
1042	    "figures": [],
1043	    "analysis": "QLoRA 结果是 median 档下的 strategic risk：它验证了 depth signal 的真实性 （fine-tuned model 能学到），但也暴露了 handcrafted features 的 performance gap。 Paper 必须在 discussion 中坦诚报告，positioning 7-feature 为  \"interpretable + efficient diagnostic\" 而非 \"best classifier\"。 审稿人会要求这段讨论的存在——缺失会被标为 major issue。\n\n\nMedian 档下，QLoRA end-to-end 分类器大幅超越 7-feature ensemble  （3-class +12.8pp, binary +14.6pp）。这是一个 double-edged result： 它证明 depth signal 存在且比 7 features 捕获的更丰富，但也意味着  审稿人会问 \"既然 fine-tuned LM 远优于 handcrafted features， 为什么不直接用 LM？\" Paper 的回应是 efficiency argument： 7-feature ensemble 只需 410M ref model + XGBoost（推理速度 ~150× faster）， 且 features 可解释（DDR analysis 的基础）。QLoRA 是 black-box。 在 median 档下，审稿人接受 efficiency argument 但会标注： \"the main methodological contribution (handcrafted features) is substantially  outperformed by standard fine-tuning\"——这削弱了 method 维度的 novelty claim。 Instruct model (0.89) 略优于 base (0.86)，因为 instruct 的 classification  head 更容易学习 task-specific patterns。5-class F1 (0.60) 仍远低于理想， 确认 5-class resolution ceiling。\n"
1044	  },
1045	  {
1046	    "name": "text_length_control",
1047	    "description": "排除 text length confound：(A) length-depth correlation,  (B) length-normalized features, (C) length-matched classifier evaluation。\n",
1048	    "results": {
1049	      "spearman_length_depth_range": [
1050	        -0.066,
1051	        0.134
1052	      ],
1053	      "length_depth_correlation": "weak (|ρ|<0.14)",
1054	      "normalized_ttr_trend_preserved": true,
1055	      "normalized_hapax_trend_preserved": true,
1056	      "normalized_rho_stronger": true,
1057	      "length_matched_binary_f1": 0.724,
1058	      "unmatched_binary_f1": 0.77,
1059	      "delta_length_matched": -0.046,
1060	      "random_subsample_control_f1": 0.74,
1061	      "length_is_confound": false,
1062	      "dropout_short_text_bias": true
1063	    },
1064	    "tables": [
1065	      {
1066	        "name": "Table: Length Control Analysis",
1067	        "columns": [
1068	          "Condition",
1069	          "Binary_F1",
1070	          "Δ_vs_Full",
1071	          "Note"
1072	        ],
1073	        "rows": [
1074	          [
1075	            "Full (unmatched)",
1076	            0.77,
1077	            "—",
1078	            "N=full dataset"
1079	          ],
1080	          [
1081	            "Length-matched",
1082	            0.724,
1083	            -0.046,
1084	            "Length distributions equalized"
1085	          ],
1086	          [
1087	            "Random subsample (same N)",
1088	            0.74,
1089	            -0.03,
1090	            "Size control"
1091	          ],
1092	          [
1093	            "Δ attributable to length",
1094	            "—",
1095	            -0.016,
1096	            "0.046 - 0.030"
1097	          ]
1098	        ]
1099	      }
1100	    ],
1101	    "figures": [],
1102	    "analysis": "Clean confound control。Attributable length effect 仅 1.6pp（4.6pp total drop  中 3pp 来自 sample reduction）。审稿人在 median 档下对此满意—— 这是 paper credibility 的必要 check，不是 exciting finding。\n\n\nMedian 档下，length confound 被有效排除但有 nuance。Length-depth 相关性弱 (|ρ|<0.14)，说明 deeper text 不是系统性地更短或更长。Length-normalized  surface features (TTR, hapax on fixed windows) 保留 drifting trend 且  ρ 值更强（normalization 消除了短文本 noise）。Length-matched subsampling  后 binary F1 从 0.770 降至 0.724（-4.6pp），但 random subsample control  (0.740) 也降了 3pp，说明 drop 主要来自 sample size reduction（短文本 dropout  减少了 training data），而非 length 本身是 confound。 审稿人会接受 \"length is not a confound\" 结论，但可能追问 4.6pp drop 的  composition。Paper 需要同时报告 random-subsample control 以 deconfound  the deconfounding。\n"
1103	  },
1104	  {
1105	    "name": "large_scale_generator",
1106	    "description": "加入 7B+ generator (Qwen3-8B-Base) 测试 scale effect。 1000 seeds × 5 depths。\n",
1107	    "results": {
1108	      "total_records": 4497,
1109	      "unique_seeds": 995,
1110	      "depth_dist": {
1111	        "0": 995,
1112	        "1": 979,
1113	        "2": 937,
1114	        "3": 831,
1115	        "4": 755
1116	      },
1117	      "logo_6gen_avg_f1": 0.789,
1118	      "logo_qwen3_8b_held_out_f1": 0.683,
1119	      "logo_5gen_baseline_f1": 0.8,
1120	      "delta_6gen_vs_5gen": -0.011,
1121	      "spearman_hapax": -0.558,
1122	      "spearman_ttr": -0.542,
1123	      "spearman_entropy_mean": -0.475,
1124	      "spearman_tail_decay": -0.089,
1125	      "scale_degradation_confirmed": true,
1126	      "degradation_magnitude": "moderate (-0.011 avg, Qwen3-8B at 0.683 vs 0.694 avg)",
1127	      "per_gen_ranking": "pythia-1b > qwen3-0.6b > pythia-2.8b > qwen3-1.7b > olmo-2-1b > qwen3-8b"
1128	    },
1129	    "tables": [
1130	      {
1131	        "name": "Table: Scale Effect (6-Generator LOGO)",
1132	        "columns": [
1133	          "Generator",
1134	          "Params",
1135	          "LOGO_Binary_F1",
1136	          "hapax_ρ",
1137	          "entropy_mean_ρ"
1138	        ],
1139	        "rows": [
1140	          [
1141	            "Pythia-1B",
1142	            "1B",
1143	            0.718,
1144	            -0.65,
1145	            -0.64
1146	          ],
1147	          [
1148	            "Qwen3-0.6B",
1149	            "0.6B",
1150	            0.659,
1151	            -0.6,
1152	            -0.58
1153	          ],
1154	          [
1155	            "Pythia-2.8B",
1156	            "2.8B",
1157	            0.724,
1158	            -0.63,
1159	            -0.6
1160	          ],
1161	          [
1162	            "Qwen3-1.7B",
1163	            "1.7B",
1164	            0.702,
1165	            -0.61,
1166	            -0.57
1167	          ],
1168	          [
1169	            "OLMo-2-1B",
1170	            "1.5B",
1171	            0.668,
1172	            -0.57,
1173	            -0.52
1174	          ],
1175	          [
1176	            "Qwen3-8B",
1177	            "8B",
1178	            0.683,
1179	            -0.56,
1180	            -0.48
1181	          ],
1182	          [
1183	            "**6-gen avg**",
1184	            "—",
1185	            "**0.692**",
1186	            "-0.60",
1187	            "-0.57"
1188	          ]
1189	        ]
1190	      },
1191	      {
1192	        "name": "Table: Depth Retention at Scale",
1193	        "columns": [
1194	          "Generator",
1195	          "gen4_retention",
1196	          "gen3_retention"
1197	        ],
1198	        "rows": [
1199	          [
1200	            "Pythia-2.8B",
1201	            "83.1%",
1202	            "87.8%"
1203	          ],
1204	          [
1205	            "Qwen3-8B",
1206	            "75.9%",
1207	            "83.5%"
1208	          ]
1209	        ]
1210	      }
1211	    ],
1212	    "figures": [],
1213	    "analysis": "Scale effect 是 honest limitation（-1.1pp avg degradation）。8B 是当前最大  generator，DDR 仍然 work（F1=0.683, above chance）。但 trend suggests  更大模型可能 further degrade。审稿人会标注但不会因此 reject。 加入 Mistral-7B 后（plan 外但 registry 显示已完成）worst-case 降至 0.633， 进一步说明 large-model challenge。\n\n\nMedian 档下，Qwen3-8B-Base 的 LOGO F1 (0.683) 低于 5-gen average (0.694)， 确认 scale degradation 存在但 moderate。Higher-capacity models 压缩 feature  margins：hapax ρ=-0.558（vs avg -0.63），entropy_mean ρ=-0.475（vs avg -0.60）。 DDR 趋势保留但幅度缩小。6-gen LOGO avg (0.789 macro) 比 5-gen (0.800)  降 1.1pp——可接受。审稿人在 median 档下不会将此视为 major weakness  但会要求在 limitations 中讨论 scale trend。Depth retention 更低 (gen-4 仅 755/995=75.9% vs 5-gen avg ~85%)——大模型 generation  truncation 更频繁（EOS token 更 aggressive），需要在 paper 中提及。 审稿人可能追问 \"如果 70B 模型呢？\"——这是 base-model scope 的内在局限， 只能诚实标注为 future work。\n"
1214	  },
1215	  {
1216	    "name": "ordinal_baseline_comparison",
1217	    "description": "CRITICAL baseline: 测试 FastDetectGPT / Binoculars / LD-Score / Avg-LogProb  的 continuous scores 是否已提供 ordinal depth signal，与 7-feature 对比。\n",
1218	    "results": {
1219	      "seven_feature_logo_f1": 0.798,
1220	      "seven_feature_ci": [
1221	        0.786,
1222	        0.799
1223	      ],
1224	      "avg_logprob_logo_f1": 0.765,
1225	      "avg_logprob_ci": [
1226	        0.616,
1227	        0.82
1228	      ],
1229	      "ld_score_logo_f1": 0.721,
1230	      "ld_score_ci": [
1231	        0.588,
1232	        0.77
1233	      ],
1234	      "fast_detect_gpt_logo_f1": 0.627,
1235	      "fast_detect_gpt_ci": [
1236	        0.511,
1237	        0.762
1238	      ],
1239	      "binoculars_logo_f1": 0.579,
1240	      "binoculars_ci": [
1241	        0.405,
1242	        0.664
1243	      ],
1244	      "best_single_detector": "Avg-LogProb (0.765)",
1245	      "seven_feature_advantage_pp": 3.3,
1246	      "bootstrap_7feat_vs_avglogprob_p": 0.0,
1247	      "bootstrap_7feat_vs_avglogprob_delta": 0.039,
1248	      "bootstrap_7feat_vs_fdgpt_p": 0.0,
1249	      "multi_detector_ensemble_f1": 0.795,
1250	      "multi_detector_ci": [
1251	        0.78,
1252	        0.81
1253	      ],
1254	      "four_det_plus_surface_f1": 0.795,
1255	      "delta_7feat_vs_4det": "+0.003"
1256	    },
1257	    "tables": [
1258	      {
1259	        "name": "Table: 7-Feature vs Existing Detector Baselines (LOGO)",
1260	        "columns": [
1261	          "Method",
1262	          "LOGO_Macro_F1",
1263	          "95%_CI",
1264	          "Spearman_ρ_depth",
1265	          "N_Models_Required"
1266	        ],
1267	        "rows": [
1268	          [
1269	            "7-feature XGBoost",
1270	            0.798,
1271	            "[0.786, 0.799]",
1272	            "—",
1273	            "1 (410M ref)"
1274	          ],
1275	          [
1276	            "Avg-LogProb",
1277	            0.765,
1278	            "[0.616, 0.820]",
1279	            0.788,
1280	            "1 (410M ref)"
1281	          ],
1282	          [
1283	            "LD-Score",
1284	            0.721,
1285	            "[0.588, 0.770]",
1286	            0.794,
1287	            0
1288	          ],
1289	          [
1290	            "FastDetectGPT",
1291	            0.627,
1292	            "[0.511, 0.762]",
1293	            0.433,
1294	            "2 (source + scoring)"
1295	          ],
1296	          [
1297	            "Binoculars",
1298	            0.579,
1299	            "[0.405, 0.664]",
1300	            0.199,
1301	            "2 (observer + performer)"
1302	          ],
1303	          [
1304	            "4-det + surface ensemble",
1305	            0.795,
1306	            "[0.780, 0.810]",
1307	            "—",
1308	            "4+ models"
1309	          ]
1310	        ]
1311	      },
1312	      {
1313	        "name": "Table: Bootstrap Pairwise Comparisons",
1314	        "columns": [
1315	          "Comparison",
1316	          "Delta",
1317	          "p_value",
1318	          "Significant"
1319	        ],
1320	        "rows": [
1321	          [
1322	            "7-feat vs Avg-LogProb",
1323	            "+0.033",
1324	            0.0,
1325	            true
1326	          ],
1327	          [
1328	            "7-feat vs LD-Score",
1329	            "+0.077",
1330	            0.0,
1331	            true
1332	          ],
1333	          [
1334	            "7-feat vs FastDetectGPT",
1335	            "+0.171",
1336	            0.0,
1337	            true
1338	          ],
1339	          [
1340	            "7-feat vs 4-det ensemble",
1341	            "+0.003",
1342	            0.38,
1343	            false
1344	          ]
1345	        ]
1346	      }
1347	    ],
1348	    "figures": [],
1349	    "analysis": "Baseline comparison 是 paper 能否被接收的 gatekeeping experiment。 7-feature 优势统计显著但 practical margin 不大（+3.3pp vs Avg-LogProb）。 在 median 档下，审稿人接受 \"custom features add value\" 但会标注  \"the advantage is modest\"。关键防线是 CI width argument 和 DDR  conceptual contribution——如果 paper 只 claim classification performance， 这个 margin 不够；但如果 position 为 \"empirical characterization of DDR,  with classification as validation\"，审稿人更容易接受。\n\n\nMedian 档的 critical baseline test 通过但 margin 不大。7-feature (0.798)  显著优于所有 single detectors（bootstrap p=0），但 Avg-LogProb (0.765)  的 gap 仅 3.3pp。审稿人会说 \"7-feature set 的优势 modest，而且 Avg-LogProb  作为 single feature 已经不错了——custom features 的边际贡献在 practical  意义上有多大？\" 在 median 档下这个质疑被 offset by 两个论点： (1) 7-feature 的 CI 远窄于单检测器（cross-generator variance 更低）， 说明 robustness 更好；(2) DDR analysis 需要多个 features 才能做（ 这是 conceptual contribution，不只是 classification performance）。 Multi-detector ensemble (4-det + surface, 0.795) 与 7-feature (0.798)  几乎等效但需要 2.4× inference cost + 3.2× GPU memory， 支持 efficiency positioning。Binoculars CI 极宽 [0.405, 0.664]  说明它对 generator 极度敏感。\n"
1350	  },
1351	  {
1352	    "name": "9-gen scale evaluation (with Gemma-2-2B)",
1353	    "description": "扩展至 9 个 generator (原 8 + Gemma-2-2B) 的 LOGO 评估， 测试 broader generalization 和 edge cases。\n",
1354	    "results": {
1355	      "nine_gen_logo_3class_f1": 0.751,
1356	      "nine_gen_logo_binary_f1": 0.666,
1357	      "eight_gen_baseline_3class_f1": 0.77,
1358	      "delta_9gen_vs_8gen": -0.019,
1359	      "gemma_2_2b_3class_f1": 0.628,
1360	      "gemma_2_2b_binary_f1": 0.44,
1361	      "gemma_2_2b_gen1_f1": 0.036,
1362	      "mistral_7b_3class_f1": 0.605,
1363	      "mistral_7b_binary_f1": 0.633,
1364	      "per_gen_3class_range": [
1365	        0.605,
1366	        0.857
1367	      ]
1368	    },
1369	    "tables": [
1370	      {
1371	        "name": "Table: 9-Generator LOGO Results",
1372	        "columns": [
1373	          "Generator",
1374	          "Family",
1375	          "Params",
1376	          "3-Class_F1",
1377	          "Binary_F1",
1378	          "Gen-1_F1"
1379	        ],
1380	        "rows": [
1381	          [
1382	            "Pythia-1B",
1383	            "Pythia",
1384	            "1B",
1385	            0.857,
1386	            0.718,
1387	            0.65
1388	          ],
1389	          [
1390	            "Qwen3-0.6B",
1391	            "Qwen",
1392	            "0.6B",
1393	            0.819,
1394	            0.659,
1395	            0.61
1396	          ],
1397	          [
1398	            "Pythia-2.8B",
1399	            "Pythia",
1400	            "2.8B",
1401	            0.812,
1402	            0.724,
1403	            0.68
1404	          ],
1405	          [
1406	            "Qwen3-1.7B",
1407	            "Qwen",
1408	            "1.7B",
1409	            0.811,
1410	            0.702,
1411	            0.66
1412	          ],
1413	          [
1414	            "OLMo-2-1B",
1415	            "OLMo",
1416	            "1.5B",
1417	            0.773,
1418	            0.668,
1419	            0.58
1420	          ],
1421	          [
1422	            "Llama-3.2-3B",
1423	            "Llama",
1424	            "3B",
1425	            0.759,
1426	            0.69,
1427	            0.6
1428	          ],
1429	          [
1430	            "Qwen3-8B",
1431	            "Qwen",
1432	            "8B",
1433	            0.696,
1434	            0.647,
1435	            0.52
1436	          ],
1437	          [
1438	            "**Gemma-2-2B**",
1439	            "Gemma",
1440	            "2B",
1441	            "**0.628**",
1442	            "**0.440**",
1443	            "**0.036**"
1444	          ],
1445	          [
1446	            "Mistral-7B-v0.3",
1447	            "Mistral",
1448	            "7B",
1449	            0.605,
1450	            0.633,
1451	            0.44
1452	          ]
1453	        ]
1454	      }
1455	    ],
1456	    "figures": [],
1457	    "analysis": "Gemma anomaly 是 median 档审稿人重点追问对象。-0.25pp reviewer penalty  的来源。Paper 处理策略：承认 failure case，分析 Gemma gen-1 的 feature  distribution（是否与 gen-0 truly indistinguishable），讨论可能的  architectural 原因（GQA, training data composition）。\n\n\nMedian 档下 Gemma-2-2B 是 paper 中最显著的 anomaly：gen-1 F1=0.036  意味着分类器完全无法识别 Gemma 的 gen-1 output。原因：Gemma-2 的  architecture (grouped-query attention + RMSNorm) 和 training recipe  使其 gen-1 的 distributional features 异常接近 gen-0——depth signal  在第一步就极度微弱。这是 method failure 而非 Gemma 特殊性， 因为其他大模型 (Qwen3-8B, Mistral-7B) 虽然 F1 较低但仍在 0.63+ 水平。 审稿人会追问：\"gen-1 F1=0.036 是否意味着方法对某些 architecture  完全失败？如果是，如何判断哪些 generator 会失败？\" 这是 rebuttal 中需要回应的 medium-severity concern。 Paper 必须在 9-gen appendix 中显式讨论 Gemma anomaly， 并承认 \"方法不保证对所有 generator architectures 均有效\"。\n"
1458	  },
1459	  {
1460	    "name": "DDR causality analysis",
1461	    "description": "通过 permutation importance, Granger causality, feature intervention  三种方法验证 DDR 的 causal structure。\n",
1462	    "results": {
1463	      "permutation_baseline_f1": 0.771,
1464	      "drifting_avg_importance": 0.158,
1465	      "stationary_avg_importance": 0.03,
1466	      "drifting_stationary_ratio": 5.3,
1467	      "granger_significant": "6/7 features",
1468	      "granger_nonsig": "entropy_min",
1469	      "granger_max_delta_r2": 0.031,
1470	      "intervention_max_f1_drop": 0.02,
1471	      "intervention_max_feature": "entropy_max"
1472	    },
1473	    "tables": [
1474	      {
1475	        "name": "Table: DDR Causality Evidence",
1476	        "columns": [
1477	          "Method",
1478	          "Drifting_Signal",
1479	          "Stationary_Signal",
1480	          "Gap_Ratio"
1481	        ],
1482	        "rows": [
1483	          [
1484	            "Permutation importance",
1485	            0.158,
1486	            0.03,
1487	            "5.3×"
1488	          ],
1489	          [
1490	            "Granger causality",
1491	            "6/7 sig (p<0.05)",
1492	            "—",
1493	            "—"
1494	          ],
1495	          [
1496	            "Feature intervention (max F1 drop)",
1497	            0.02,
1498	            0.006,
1499	            "3.3×"
1500	          ]
1501	        ]
1502	      }
1503	    ],
1504	    "figures": [],
1505	    "analysis": "Causality analysis 为 DDR 提供了超越 correlation 的 evidence， 但 effect sizes 偏小。在 median 档下这是 \"nice methodological rigor\"  而非 game-changer。\n\n\nMedian 档下，causality analysis 是 DDR claim 的强化 evidence。 5.3× permutation importance gap（drifting 0.158 vs stationary 0.030） 清晰支持 DDR 的 feature-role 划分。6/7 features Granger significant  说明 temporal ordering matters（depth 预测 feature 值）。 但 Granger max delta R² 仅 0.031——effect size 小，审稿人可能认为  \"statistically significant but practically negligible\"。 Entropy_min 的 non-significance 与其 intermediate status 一致。 Feature intervention max drop 仅 0.020（entropy_max），说明  no single feature is critical——系统鲁棒但个体 feature 贡献分散。 审稿人会认可方法论的 rigor（三种独立 causality tests）， 但不会被 effect sizes 打动。\n"
1506	  },
1507	  {
1508	    "name": "TOST bootstrap stability validation",
1509	    "description": "Bootstrap TOST 验证 shape features 的 stationarity classification  在重采样下是否稳定。\n",
1510	    "results": {
1511	      "n_bootstrap": 1000,
1512	      "margin_d": 0.2,
1513	      "entropy_max": {
1514	        "rejection_rate": 1.0,
1515	        "median_d": 0.062,
1516	        "classification": "Stationary (robust)"
1517	      },
1518	      "entropy_min": {
1519	        "rejection_rate": 1.0,
1520	        "median_d": -0.016,
1521	        "classification": "Stationary (robust)"
1522	      },
1523	      "tail_decay": {
1524	        "rejection_rate": 1.0,
1525	        "median_d": 0.088,
1526	        "classification": "Stationary (robust)"
1527	      },
1528	      "entropy_std": {
1529	        "rejection_rate": 0.0,
1530	        "median_d": 0.458,
1531	        "classification": "NOT stationary (TOST never rejects)",
1532	        "d_ci": [
1533	          0.435,
1534	          0.479
1535	        ]
1536	      }
1537	    },
1538	    "tables": [
1539	      {
1540	        "name": "Table: TOST Bootstrap Stability (margin d=0.2)",
1541	        "columns": [
1542	          "Feature",
1543	          "Median_d",
1544	          "d_95%_CI",
1545	          "Rejection_Rate",
1546	          "Classification"
1547	        ],
1548	        "rows": [
1549	          [
1550	            "entropy_max",
1551	            0.062,
1552	            "[0.037, 0.088]",
1553	            "1000/1000",
1554	            "Stationary"
1555	          ],
1556	          [
1557	            "entropy_min",
1558	            -0.016,
1559	            "[-0.042, 0.011]",
1560	            "1000/1000",
1561	            "Stationary"
1562	          ],
1563	          [
1564	            "tail_decay",
1565	            0.088,
1566	            "[0.065, 0.111]",
1567	            "1000/1000",
1568	            "Stationary"
1569	          ],
1570	          [
1571	            "**entropy_std**",
1572	            "**0.458**",
1573	            "**[0.435, 0.479]**",
1574	            "**0/1000**",
1575	            "**NOT stationary**"
1576	          ]
1577	        ]
1578	      }
1579	    ],
1580	    "figures": [],
1581	    "analysis": "entropy_std 的 TOST 结果是 median 档下审稿人最可能追问的 technical point。 Paper 必须从二分法转向 spectrum 模型，否则 internal inconsistency  会被标为 moderate issue。这个调整实际上使论文更 nuanced 也更 honest， 审稿人倾向于正面看待。\n\n\nMedian 档下的 key tension point：三个 shape features (entropy_max,  entropy_min, tail_decay) 通过 TOST 所有 1000 次 bootstrap  (rejection rate=1.0)，d 值远低于 0.2 threshold。但 entropy_std  的 rejection rate=0.0，d=0.458 [0.435, 0.479] 远超 equivalence margin。 这直接否定了将 entropy_std 归入 \"stationary\" 组的原始分类。 审稿人会追问：\"为什么原文将 entropy_std 归为 H1/stationary？ TOST 明确拒绝了 equivalence。这是否意味着 DDR 的二分法本身有问题？\" Paper 需要调整：将 entropy_std 移出 stationary 组，要么归入 drifting  (但 ρ=-0.20 比 drifting group 弱很多)，要么引入 \"intermediate\" 类别。 Median 档的叙事方向选择 spectrum model：drifting → intermediate → stationary， entropy_std 和 entropy_min 居于 intermediate。\n"
1582	  },
1583	  {
1584	    "name": "Instruct model evaluation (3 models)",
1585	    "description": "在 Qwen3-1.7B-Instruct, OLMo-2-1B-Instruct, Llama-3.2-3B-Instruct 上 测试 depth signal 在 instruct tuning 下的 degradation。\n",
1586	    "results": {
1587	      "qwen_instruct_logo_binary": 0.658,
1588	      "qwen_instruct_logo_3class": 0.543,
1589	      "olmo_instruct_logo_binary": 0.338,
1590	      "olmo_instruct_logo_3class": 0.42,
1591	      "llama_instruct_binary": 0.838,
1592	      "llama_instruct_3class": 0.544,
1593	      "qwen_base_logo_binary": 0.821,
1594	      "olmo_base_logo_binary": 0.763,
1595	      "llama_base_binary": 0.849,
1596	      "delta_qwen": -0.163,
1597	      "delta_olmo": -0.425,
1598	      "delta_llama": -0.011,
1599	      "feature_reversal_count": {
1600	        "olmo": "6/7",
1601	        "qwen": "partial (direction flip in entropy_mean)",
1602	        "llama": "3/7"
1603	      },
1604	      "spearman_direction_instruct": "多数特征 ρ>0 (reversed from base ρ<0)"
1605	    },
1606	    "tables": [
1607	      {
1608	        "name": "Table: Instruct vs Base Model Comparison",
1609	        "columns": [
1610	          "Model",
1611	          "Base_Binary_F1",
1612	          "Instruct_Binary_F1",
1613	          "Δ",
1614	          "Features_Reversed"
1615	        ],
1616	        "rows": [
1617	          [
1618	            "OLMo-2-1B",
1619	            0.763,
1620	            0.338,
1621	            -0.425,
1622	            "6/7"
1623	          ],
1624	          [
1625	            "Qwen3-1.7B",
1626	            0.821,
1627	            0.658,
1628	            -0.163,
1629	            "partial"
1630	          ],
1631	          [
1632	            "Llama-3.2-3B",
1633	            0.849,
1634	            0.838,
1635	            -0.011,
1636	            "3/7"
1637	          ]
1638	        ]
1639	      }
1640	    ],
1641	    "figures": [],
1642	    "analysis": "Instruct degradation 的异质性（OLMo 极严重，Llama 几乎不受影响） 是一个 interesting finding，但也使 scope boundary 变得模糊—— 审稿人会问 \"哪些 instruct model 会 degrade？能否 predict？\" 在 median 档下只能回答 \"we cannot predict a priori\" 并标注为 limitation。\n\n\nMedian 档下 instruct degradation 是 paper 的 primary scope limitation。 OLMo-Instruct 的 LOGO binary F1 仅 0.338（vs base 0.763, -42.5pp）， 6/7 features Spearman ρ 方向反转（base 为负/instruct 为正）。 这说明 instruction tuning 的 format regulation 和 length normalization  破坏甚至反转了 DDR pattern。Qwen-Instruct degradation 中等 (-16.3pp)， Llama-Instruct 最小 (-1.1pp)——instruct 影响的 magnitude 是 model-specific。 审稿人中 1-2 个会标注 \"base-model-only scope\" 为 major limitation  并扣 -0.5pp。Rebuttal 需要论证：(1) base model 在 data contamination  分析场景下仍然 relevant（web-scraped data 主要由 base/API 模型生成）， (2) instruct 场景是 explicit future work with clear direction。 Feature reversal 的发现本身有一定 novelty——instruct tuning 不只是削弱  depth signal，而是反转了 distributional dynamics，这值得在 discussion 中提及。\n"
1643	  },
1644	  {
1645	    "name": "Temperature sensitivity curve",
1646	    "description": "温度敏感性分析：t=0.5, 0.7, 0.9, 1.0 的 depth signal 强度和跨温度 transfer。\n",
1647	    "results": {
1648	      "within_t05_binary": 0.813,
1649	      "within_t07_binary": 0.694,
1650	      "within_t09_binary": 0.48,
1651	      "cross_t07_to_t10_binary_qwen": 0.418,
1652	      "cross_t10_to_t07_binary_qwen": 0.944,
1653	      "delta_t05_vs_t07": "+0.119",
1654	      "delta_t09_vs_t07": "-0.214",
1655	      "entropy_mean_rho_t05": -0.58,
1656	      "entropy_mean_rho_t07": -0.6,
1657	      "entropy_mean_rho_t09": -0.3,
1658	      "reliable_range": "[0.5, 0.9) — ≤1pp degradation within [0.5, 0.7]",
1659	      "cross_temp_transfer_asymmetric": true
1660	    },
1661	    "tables": [
1662	      {
1663	        "name": "Table: Temperature Sensitivity",
1664	        "columns": [
1665	          "Temperature",
1666	          "Within-CV_Binary_F1",
1667	          "entropy_mean_ρ",
1668	          "Reliable"
1669	        ],
1670	        "rows": [
1671	          [
1672	            0.5,
1673	            0.813,
1674	            -0.58,
1675	            "Yes (stronger signal)"
1676	          ],
1677	          [
1678	            0.7,
1679	            0.694,
1680	            -0.6,
1681	            "Yes (default)"
1682	          ],
1683	          [
1684	            0.9,
1685	            0.48,
1686	            -0.3,
1687	            "No (severe degradation)"
1688	          ]
1689	        ]
1690	      },
1691	      {
1692	        "name": "Table: Cross-Temperature Transfer (Qwen3-1.7B)",
1693	        "columns": [
1694	          "Train_Temp",
1695	          "Test_Temp",
1696	          "Binary_F1",
1697	          "Δ_vs_Within"
1698	        ],
1699	        "rows": [
1700	          [
1701	            0.7,
1702	            0.7,
1703	            0.789,
1704	            "—"
1705	          ],
1706	          [
1707	            0.7,
1708	            1.0,
1709	            0.418,
1710	            -0.371
1711	          ],
1712	          [
1713	            1.0,
1714	            0.7,
1715	            0.944,
1716	            "+0.155"
1717	          ],
1718	          [
1719	            1.0,
1720	            1.0,
1721	            0.825,
1722	            "—"
1723	          ]
1724	        ]
1725	      }
1726	    ],
1727	    "figures": [],
1728	    "analysis": "温度限制在 median 档下被标为 known scope boundary。 t≥0.9 的 degradation 源于 high-temperature sampling 的 entropy inflation—— 所有 depth 的 entropy features 都被推高，压缩了 depth-to-depth 差异。\n\n\nMedian 档下，温度敏感性是第二个 scope limitation。t∈[0.5, 0.7]  内 depth signal 稳定（0.694-0.813），但 t=0.9 时急剧下降至 0.480  (below chance for binary)，entropy_mean ρ 从 -0.60 降至 -0.30。 t=1.0 下跨温度 transfer 极差（Qwen t=0.7→t=1.0: 0.789→0.418, -37pp）， 但反方向 (t=1.0→t=0.7) 反而好 (0.944)——不对称 transfer 说明  high-temp features 是 low-temp features 的 superset（noise 更大但信号保留）。 Paper 将 \"t∈[0.5, 0.9)\" 标为 reliable range，t≥0.9 为 degraded。 审稿人在 median 档下会问 \"most API models default to t=1.0,  does this limit real-world applicability?\"——需要在 limitations 中回应。\n"
1729	  },
1730	  {
1731	    "name": "Independent seed validation",
1732	    "description": "用完全独立的 seed sets 验证 shared-seed LOGO 是否存在 seed leakage。\n",
1733	    "results": {
1734	      "pythia_to_olmo_binary": 0.695,
1735	      "olmo_to_pythia_binary": 0.666,
1736	      "avg_independent": 0.68,
1737	      "shared_seed_logo_ref": 0.694,
1738	      "delta_vs_shared": -0.014
1739	    },
1740	    "tables": [
1741	      {
1742	        "name": "Table: Seed Leakage Validation",
1743	        "columns": [
1744	          "Setup",
1745	          "Binary_F1",
1746	          "Seeds_Shared"
1747	        ],
1748	        "rows": [
1749	          [
1750	            "Shared-seed LOGO",
1751	            0.694,
1752	            "Yes (same 995 seeds)"
1753	          ],
1754	          [
1755	            {
1756	              "Independent": "Pythia→OLMo"
1757	            },
1758	            0.695,
1759	            false
1760	          ],
1761	          [
1762	            {
1763	              "Independent": "OLMo→Pythia"
1764	            },
1765	            0.666,
1766	            false
1767	          ],
1768	          [
1769	            "Independent avg",
1770	            0.68,
1771	            false
1772	          ]
1773	        ]
1774	      }
1775	    ],
1776	    "figures": [],
1777	    "analysis": "Seed leakage 不是问题。-1.4pp delta 在 noise range 内。 作为 supplementary validation 写入 appendix。\n\n\nMedian 档下，independent seed validation 确认 shared-seed LOGO 的  seed leakage 极小（delta 仅 -1.4pp）。Pythia→OLMo (0.695) 几乎等同于  LOGO average (0.694)，说明 seed content 不是主要信号源。 OLMo→Pythia 略低 (0.666) 可能反映 OLMo 作为训练集的 feature space  不完全覆盖 Pythia 的分布。审稿人不会在此处追问——这是一个 clean validation。\n"
1778	  },
1779	  {
1780	    "name": "Seed complexity stratification",
1781	    "description": "按 seed text complexity (low/medium/high) 分层分析 depth signal 是否依赖 seed 质量。\n",
1782	    "results": {
1783	      "low_complexity_binary": 0.685,
1784	      "medium_binary": 0.695,
1785	      "high_complexity_binary": 0.695,
1786	      "max_diff_binary_pp": 1.06,
1787	      "seed_independent_label": true
1788	    },
1789	    "tables": [
1790	      {
1791	        "name": "Table: Seed Complexity Stratification",
1792	        "columns": [
1793	          "Complexity_Bin",
1794	          "Binary_F1",
1795	          "Multiclass_F1",
1796	          "N_Seeds"
1797	        ],
1798	        "rows": [
1799	          [
1800	            "Low",
1801	            0.685,
1802	            0.772,
1803	            "~332"
1804	          ],
1805	          [
1806	            "Medium",
1807	            0.695,
1808	            0.778,
1809	            "~332"
1810	          ],
1811	          [
1812	            "High",
1813	            0.695,
1814	            0.779,
1815	            "~331"
1816	          ]
1817	        ]
1818	      }
1819	    ],
1820	    "figures": [],
1821	    "analysis": "Clean result. Seed independence confirmed. Appendix material.\n\n\nMedian 档下 seed complexity 对 depth signal 影响极小（max diff 1.06pp）， 确认方法对 seed 质量不敏感。Low complexity seeds 的微弱 drop (1pp)  可能源于低复杂度 text 的 feature range 本身更窄。审稿人不会在此处追问。\n"
1822	  },
1823	  {
1824	    "name": "Topic drift correlation",
1825	    "description": "分析 semantic similarity (cosine) 与 depth 和 feature drift 的关系。\n",
1826	    "results": {
1827	      "sim_0to1_mean": 0.622,
1828	      "sim_1to2_mean": 0.683,
1829	      "sim_2to3_mean": 0.801,
1830	      "sim_3to4_mean": 0.859,
1831	      "shape_entropy_std_rho": -0.164,
1832	      "shape_tail_decay_rho": 0.068,
1833	      "drifting_hapax_rho": -0.124,
1834	      "drifting_entropy_mean_rho": -0.286,
1835	      "semantic_convergence_with_depth": true
1836	    },
1837	    "tables": [
1838	      {
1839	        "name": "Table: Semantic Similarity by Depth Transition",
1840	        "columns": [
1841	          "Transition",
1842	          "Mean_Cosine_Sim",
1843	          "Std"
1844	        ],
1845	        "rows": [
1846	          [
1847	            "gen-0 → gen-1",
1848	            0.622,
1849	            0.165
1850	          ],
1851	          [
1852	            "gen-1 → gen-2",
1853	            0.683,
1854	            0.184
1855	          ],
1856	          [
1857	            "gen-2 → gen-3",
1858	            0.801,
1859	            0.201
1860	          ],
1861	          [
1862	            "gen-3 → gen-4",
1863	            0.859,
1864	            0.19
1865	          ]
1866	        ]
1867	      }
1868	    ],
1869	    "figures": [],
1870	    "analysis": "Semantic convergence + distributional divergence 的 decoupling 是  intellectually interesting 的 supporting evidence。审稿人在 median 档下 会认可但不会因此提高分数。\n\nMedian 档下，topic drift analysis 揭示 counter-intuitive pattern： deeper generations 在 semantic space 中 converge（sim 从 0.622 增至 0.859）， 即使 distributional features 在 diverge。这说明 DDR 不是 topic drift  的结果——topic 趋同但 distribution 趋异，方向相反。 Drifting features 与 semantic sim 的弱负相关（entropy_mean ρ=-0.286） 说明两者部分共变但独立性主要成立。Shape features 几乎无关（|ρ|<0.17）。 审稿人可能对 \"semantic convergence\" finding 感兴趣但这不是 paper 的  core claim。作为 appendix evidence 支持 \"DDR is distributional, not semantic\"。\n"
1871	  }
1872	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "712d0dee-0e66-4a19-9a75-2f079125a475",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "230af998-bf53-42f7-b166-ab371993e83c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"在 MVP 数据上做三部分分析：(A) 特征消融（full vs reference-only vs surface-only）， (B) H1/H2 趋势分析（每个特征跨 depth 的 Spearman ρ + KS）， (C) perplexity 预验证（Pythia-410M forward pass on depth-stratified subsets）。\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.82,\n      \"full_macro_f1_ci\": [\n        0.805,\n        0.835\n      ],\n      \"reference_only_f1\": 0.719,\n      \"reference_only_ci\": [\n        0.706,\n        0.733\n      ],\n      \"surface_only_f1\": 0.763,\n      \"surface_only_ci\": [\n        0.747,\n        0.774\n      ],\n      \"mcnemar_full_vs_surface_p\": 0.0,\n      \"mcnemar_full_vs_ref_p\": 0.0,\n      \"h2_features\": [\n        \"entropy_mean\",\n        \"ttr\",\n        \"hapax_ratio\"\n      ],\n      \"h2_spearman_entropy_mean\": -0.6,\n      \"h2_spearman_ttr\": -0.61,\n      \"h2_spearman_hapax_ratio\": -0.63,\n      \"h1_features\": [\n        \"tail_decay\",\n        \"entropy_max\",\n        \"entropy_min\"\n      ],\n      \"h1_spearman_tail_decay\": 0.04,\n      \"h1_spearman_entropy_max\": 0.05,\n      \"h1_spearman_entropy_min\": -0.3,\n      \"contested_feature\": \"entropy_std\",\n      \"entropy_std_spearman\": -0.2,\n      \"entropy_std_ks\": 0.15,\n      \"median_ppl_by_depth\": [\n        13.5,\n        4.96,\n        3.0,\n        2.07,\n        1.72\n      ],\n      \"ppl_depth_trend\": \"monotonic_decrease\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Feature Ablation (5-fold CV on MVP data)\",\n        \"columns\": [\n          \"Feature_Set\",\n          \"Macro_F1\",\n          \"95%_CI\",\n          \"N_Features\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7-feature)\",\n            0.82,\n            \"[0.805, 0.835]\",\n            7\n          ],\n          [\n            \"Surface-only (TTR + hapax)\",\n            0.763,\n            \"[0.747, 0.774]\",\n            2\n          ],\n          [\n            \"Reference-only (entropy + tail)\",\n            0.719,\n            \"[0.706, 0.733]\",\n            5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Feature Trend Classification\",\n        \"columns\": [\n          \"Feature\",\n          \"Spearman_ρ\",\n          \"KS_stat\",\n          \"Trend_Class\"\n        ],\n        \"rows\": [\n          [\n            \"hapax_ratio\",\n            -0.63,\n            0.537,\n            \"Drifting\"\n          ],\n          [\n            \"ttr\",\n            -0.61,\n            0.521,\n            \"Drifting\"\n          ],\n          [\n            \"entropy_mean\",\n            -0.6,\n            0.516,\n            \"Drifting\"\n          ],\n          [\n            \"entropy_min\",\n            -0.3,\n            0.28,\n            \"Intermediate\"\n          ],\n          [\n            \"entropy_std\",\n            -0.2,\n            0.15,\n            \"Contested (d=0.458)\"\n          ],\n          [\n            \"entropy_max\",\n            0.05,\n            0.052,\n            \"Stationary\"\n          ],\n          [\n            \"tail_decay\",\n            0.04,\n            0.043,\n            \"Stationary\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现成立但有裂缝。Surface-only 0.763 vs full 0.820 的 gap 只有 5.7pp， 审稿人可能认为 \\\"complementary signal\\\" 的 framing 对 reference features 的 marginal contribution 过度包装。entropy_std 的 contested 状态是最大叙事风险—— 原始 H1/H2 二分法需要调整为 spectrum（drifting → intermediate → stationary）， 在 paper abstract 中不能回避。\\n\\n\\nMedian 档下，消融结果清晰显示 reference 和 surface 特征互补（McNemar p≈0）， 但 surface-only (0.763) 已接近 full (0.820)，给审稿人留下 \\\"reference 特征 边际贡献有限\\\" 的印象。H2 趋势在 entropy_mean/ttr/hapax 上非常强（|ρ|>0.60）， 但 entropy_std (ρ=-0.20) 处于 drifting 和 stationary 之间的灰色地带—— 它的 KS 值 (0.15) 远高于 tail_decay (0.05) 但远低于 hapax (0.54)， 导致二分法（drifting vs stationary）在这个特征上站不住脚。 审稿人会追问为何把 entropy_std 归入 stationary 组（后续 TOST 的 d=0.458  进一步加剧此问题）。Perplexity 随 depth 单调下降（13.50→1.72）证实  depth signal 存在，但也暴露 gen-0 ppl 异常高（seed text 质量差异）， 需要在 paper 中解释。\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"扩展至 5 个生成器 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)， LOGO CV 评估跨生成器泛化能力。\\n\",\n    \"results\": {\n      \"total_records\": 23032,\n      \"generators\": [\n        \"pythia-2.8b\",\n        \"pythia-1b\",\n        \"olmo-2-1b\",\n        \"qwen3-1.7b\",\n        \"qwen3-0.6b\"\n      ],\n      \"logo_avg_macro_f1\": 0.804,\n      \"logo_avg_macro_f1_ci\": [\n        0.786,\n        0.799\n      ],\n      \"logo_binary_f1\": 0.694,\n      \"logo_binary_f1_ci\": [\n        0.688,\n        0.7\n      ],\n      \"per_gen_binary_f1\": {\n        \"pythia-2.8b\": 0.724,\n        \"pythia-1b\": 0.718,\n        \"olmo-2-1b\": 0.668,\n        \"qwen3-1.7b\": 0.702,\n        \"qwen3-0.6b\": 0.659\n      },\n      \"per_gen_macro_f1\": {\n        \"pythia-2.8b\": 0.851,\n        \"pythia-1b\": 0.831,\n        \"olmo-2-1b\": 0.752,\n        \"qwen3-1.7b\": 0.805,\n        \"qwen3-0.6b\": 0.78\n      },\n      \"lofo_binary_f1\": 0.686,\n      \"lofo_macro_f1\": 0.791,\n      \"worst_case_generator\": \"qwen3-0.6b\",\n      \"best_case_generator\": \"pythia-2.8b\",\n      \"per_gen_binary_range\": [\n        0.659,\n        0.724\n      ],\n      \"binary_f1_std_across_gens\": 0.028,\n      \"top_features_importance\": [\n        \"hapax_ratio_0.289\",\n        \"ttr_0.168\",\n        \"entropy_mean_0.160\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LOGO Per-Generator Results\",\n        \"columns\": [\n          \"Generator\",\n          \"Family\",\n          \"Params\",\n          \"Binary_F1\",\n          \"Macro_F1\",\n          \"95%_CI_Binary\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            \"2.8B\",\n            0.724,\n            0.851,\n            \"[0.710, 0.738]\"\n          ],\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            \"1B\",\n            0.718,\n            0.831,\n            \"[0.703, 0.733]\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Qwen\",\n            \"1.7B\",\n            0.702,\n            0.805,\n            \"[0.687, 0.717]\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1.5B\",\n            0.668,\n            0.752,\n            \"[0.652, 0.684]\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"Qwen\",\n            \"0.6B\",\n            0.659,\n            0.78,\n            \"[0.643, 0.675]\"\n          ],\n          [\n            \"**Average**\",\n            \"—\",\n            \"—\",\n            \"**0.694**\",\n            \"**0.804**\",\n            \"[0.688, 0.700]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: LOFO vs LOGO Comparison\",\n        \"columns\": [\n          \"Eval_Protocol\",\n          \"Binary_F1\",\n          \"Macro_F1\"\n        ],\n        \"rows\": [\n          [\n            \"LOGO (leave-one-generator-out)\",\n            0.694,\n            0.804\n          ],\n          [\n            \"LOFO (leave-one-family-out)\",\n            0.686,\n            0.791\n          ],\n          [\n            \"Δ\",\n            -0.008,\n            -0.013\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LOGO binary F1=0.694 是 paper 的 headline metric，在 median 档下被审稿人 标注为 \\\"modest\\\"。Per-gen range 0.659-0.724 的 variance 是一个 moderate concern： worst-case (Qwen3-0.6B at 0.659) 的实用性被质疑。Pythia 家族两个模型都偏高 增加了 family leakage 的可信度问题，但 LOFO (0.686) 与 LOGO (0.694)  差距仅 0.8pp，可在 rebuttal 中论证 leakage 影响有限。\\n\\n\\nMedian 档下，LOGO 跨生成器平均 macro F1 达到 0.804（solid），但 binary F1  只有 0.694——这个数字成为审稿人 \\\"modest performance\\\" 评价的核心锚点。 Per-gen binary F1 从 0.659 (Qwen3-0.6B) 到 0.724 (Pythia-2.8B) 的 6.5pp  spread 说明方法对生成器敏感。两个 Pythia 模型 (2.8B: 0.724, 1B: 0.718)  都偏高，暗示 Pythia 家族内部信息泄露可能膨胀了 LOGO 的平均值—— LOFO (0.686) 比 LOGO (0.694) 低 0.8pp 证实了这一点但差距不大。 OLMo-2-1B 和 Qwen3-0.6B 作为 held-out 时 F1 较低，表明跨架构泛化  存在 gap。审稿人不会认为这是 failure，但会标注为 \\\"moderate generalization\\\"。\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"用 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model（取代 Pythia-410M）， 验证 DDR 趋势是否为 generation-intrinsic 而非 reference-model artifact。\\n\",\n    \"results\": {\n      \"logo_f1_pythia_ref\": 0.803,\n      \"logo_f1_olmo_ref\": 0.807,\n      \"logo_f1_qwen_ref\": 0.816,\n      \"entropy_drift_all_refs_negative\": true,\n      \"pythia_ref_drift_range\": [\n        -1.19,\n        -1.4\n      ],\n      \"olmo_ref_drift_range\": [\n        -0.61,\n        -0.91\n      ],\n      \"qwen_ref_drift_range\": [\n        -0.96,\n        -1.35\n      ],\n      \"dual_dynamics_is_pythia_artifact\": false,\n      \"shape_features_stationary_all_refs\": true,\n      \"tail_decay_cross_ref_ks_max\": 0.06,\n      \"entropy_std_cross_ref_inconsistency\": true,\n      \"entropy_std_d_pythia\": 0.458,\n      \"entropy_std_d_olmo\": 0.31,\n      \"entropy_std_d_qwen\": 0.52\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Reference-Model LOGO F1\",\n        \"columns\": [\n          \"Reference_Model\",\n          \"Params\",\n          \"LOGO_Macro_F1\",\n          \"entropy_mean_ρ\",\n          \"tail_decay_ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"410M\",\n            0.803,\n            -0.6,\n            0.04\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            0.807,\n            -0.52,\n            0.06\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            0.816,\n            -0.58,\n            0.03\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: entropy_std Cohen's d Across Reference Models\",\n        \"columns\": [\n          \"Reference_Model\",\n          \"entropy_std_d\",\n          \"TOST_rejection\",\n          \"Classification\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            0.458,\n            \"0/1000\",\n            \"Contested\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.31,\n            \"partial\",\n            \"Borderline stationary\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.52,\n            \"0/1000\",\n            \"Contested\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DDR 的 generation-intrinsic 属性得到验证，这是 median 档下最强的子结果。 但 reference model 选择对 drift magnitude 的影响（最大 2× 差异）是审稿人 可能追问的 nuance——需要在 paper 中透明报告。entropy_std 跨 reference  不一致性为将其重新归类为 \\\"intermediate\\\" 提供了额外证据。\\n\\n\\nMedian 档的关键 falsification test 通过：DDR 趋势在三个不同 reference model  下均成立（drift 方向一致为负），排除了 Pythia-specific artifact 假说。 这是 Claim 2 的核心支撑，审稿人会认可。但细节上，drift 幅度差异大 （OLMo ref drift 仅 -0.61 到 -0.91，约为 Pythia ref 的一半）， 说明 reference model 选择影响 signal 强度——审稿人会要求讨论。 entropy_std 的跨 reference 不一致性（d 从 0.31 到 0.52）进一步 削弱了它的 \\\"stationary\\\" 归类，支持将其移入 \\\"intermediate\\\" 类别。 Qwen ref 略微优于 Pythia ref（0.816 vs 0.803），暗示小模型 reference  不一定最优，但差异在 CI 重叠范围内。\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune OLMo-1B on depth-stratified subsets (all / depth0-1 / size-matched /  binary-filtered / depth0-only)，3 seeds with bootstrap CIs，测量 perplexity 差异。\\n\",\n    \"results\": {\n      \"total_runs\": 15,\n      \"variants\": {\n        \"all\": {\n          \"train_n\": 12299,\n          \"ppl_mean\": 2.335,\n          \"ppl_std\": 0.0003\n        },\n        \"size_matched\": {\n          \"train_n\": 3951,\n          \"ppl_mean\": 2.367,\n          \"ppl_std\": 0.0002\n        },\n        \"depth01\": {\n          \"train_n\": 3951,\n          \"ppl_mean\": 2.387,\n          \"ppl_std\": 0.001\n        },\n        \"binary_filtered\": {\n          \"train_n\": 3951,\n          \"ppl_mean\": 2.389,\n          \"ppl_std\": 0.001\n        },\n        \"depth0_only\": {\n          \"train_n\": 797,\n          \"ppl_mean\": 2.681,\n          \"ppl_std\": 0.001\n        }\n      },\n      \"ranking\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\",\n      \"tost_equal_count_p\": 0.00011,\n      \"tost_equal_count_margin\": \"±2%\",\n      \"tost_all_vs_filtered_p\": 0.15,\n      \"tost_all_vs_filtered_margin\": \"±2%\",\n      \"tost_all_vs_filtered_margin_3pct_p\": 0.003,\n      \"cohens_d_size_matched_vs_depth01\": 0.85,\n      \"seed_variance\": \"<0.002 ppl across seeds\",\n      \"negative_finding_confirmed\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Downstream CLM Perplexity by Training Data Composition\",\n        \"columns\": [\n          \"Variant\",\n          \"Train_N\",\n          \"Ppl_Mean\",\n          \"Ppl_Std\",\n          \"Δ_vs_SizeMatched\"\n        ],\n        \"rows\": [\n          [\n            \"All depths\",\n            12299,\n            2.335,\n            0.0003,\n            \"-0.032 (more data)\"\n          ],\n          [\n            \"Size-matched random\",\n            3951,\n            2.367,\n            0.0002,\n            \"—(baseline)\"\n          ],\n          [\n            \"Depth 0+1 only\",\n            3951,\n            2.387,\n            0.001,\n            \"+0.020\"\n          ],\n          [\n            \"Binary-filtered\",\n            3951,\n            2.389,\n            0.001,\n            \"+0.022\"\n          ],\n          [\n            \"Depth 0 only\",\n            797,\n            2.681,\n            0.001,\n            \"+0.314\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: TOST Equivalence Tests\",\n        \"columns\": [\n          \"Comparison\",\n          \"Margin\",\n          \"p_value\",\n          \"Equivalent\"\n        ],\n        \"rows\": [\n          [\n            \"size_matched vs depth01\",\n            \"±2%\",\n            0.00011,\n            true\n          ],\n          [\n            \"size_matched vs binary_filtered\",\n            \"±2%\",\n            8.3e-05,\n            true\n          ],\n          [\n            \"all vs size_matched\",\n            \"±2%\",\n            0.15,\n            false\n          ],\n          [\n            \"all vs size_matched\",\n            \"±3%\",\n            0.003,\n            true\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative finding 成立且叙事清晰：depth fingerprinting 是 diagnostic 工具， 不是 curative 工具。但 3 seeds + single metric 是审稿人的合理质疑点—— 在 median 档下不会导致 reject 但会在 review 中被标记为 \\\"limited evidence\\\"， 需要在 rebuttal 中承认并论证 seed variance 极小说明更多 seeds 不会改变结论。\\n\\n\\nMedian 档下 Claim 3 的 negative finding 成立但 evidence 被认为 limited。 核心结果：等样本量下 size_matched (2.367) vs depth01 (2.387) 差异仅 0.020 ppl， TOST 在 ±2% margin 下确认 equivalence (p=1.1e-4)。但审稿人会质疑： (1) 只有 3 seeds——seed variance 极小 (<0.002) 说明 variance 来源不在 seed  而在 data composition，但 3 seeds 仍显 underpowered。 (2) 单一 metric (perplexity)——不涵盖 downstream task performance、 toxicity、factuality 等维度。 (3) all (12299) vs filtered (3951) 的 TOST 需要放宽到 ±3% 才 reject， 说明 data quantity 效应存在但被标注为 \\\"modest\\\"。 depth0_only (2.681) 显著差于其他——符合预期（只有 797 samples + 只有 seed text）， 反而支持 \\\"更多 synthetic data 不 hurt\\\" 的叙事。\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"对比 continuation / elaboration / inspired_rewriting 三种 prompt 类型的 depth signal 保留度和分类性能。Pythia-2.8B, 1000 seeds。\\n\",\n    \"results\": {\n      \"cv_f1\": {\n        \"continuation\": 0.781,\n        \"elaboration\": 0.73,\n        \"inspired_rewriting\": 0.737\n      },\n      \"lopto_f1\": {\n        \"held_out_continuation\": 0.762,\n        \"held_out_elaboration\": 0.762,\n        \"held_out_rewriting\": 0.733,\n        \"avg\": 0.753\n      },\n      \"depth_retention_d4_d0\": {\n        \"continuation\": 0.831,\n        \"elaboration\": 0.986,\n        \"inspired_rewriting\": 0.939\n      },\n      \"drift_hapax_ratio\": {\n        \"continuation\": -0.74,\n        \"elaboration\": -0.83,\n        \"rewriting\": -0.8\n      },\n      \"drift_entropy_mean\": {\n        \"continuation\": -0.56,\n        \"elaboration\": -0.47,\n        \"rewriting\": -0.48\n      },\n      \"semantic_divergence_ranking\": \"continuation > rewriting > elaboration\",\n      \"f1_ranking\": \"continuation > rewriting > elaboration\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Prompt Type Comparison\",\n        \"columns\": [\n          \"Prompt_Type\",\n          \"CV_F1\",\n          \"LOPTO_F1\",\n          \"Depth_Retention\",\n          \"hapax_ρ\",\n          \"entropy_mean_ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.781,\n            0.762,\n            0.831,\n            -0.74,\n            -0.56\n          ],\n          [\n            \"Inspired rewriting\",\n            0.737,\n            0.733,\n            0.939,\n            -0.8,\n            -0.48\n          ],\n          [\n            \"Elaboration\",\n            0.73,\n            0.762,\n            0.986,\n            -0.83,\n            -0.47\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt type 对 depth signal 有系统性影响（continuation > rewriting > elaboration）， 且影响方向与语义发散度一致。这支持 DDR 的 mechanistic interpretation： 更大的语义偏移→更强的 distributional shift→更易分类。但 elaboration 的 hapax drift (-0.83) 反而比 continuation (-0.74) 更强，说明 lexical  impoverishment 和 distributional shift 不完全共线——这是一个 subtle finding， 在 median 档下审稿人可能注意到但不会深究。\\n\\n\\nMedian 档下，三种 prompt 类型均表现出 DDR 趋势，但强度和模式不同。 Continuation (F1=0.781) 最高，因为语义发散最大（每一步生成新内容而非 紧扣原文），distributional shift 更剧烈。Elaboration (F1=0.730) 最低， 因为 elaboration 保持话题一致性（retention 0.986），distributional features  变化较缓。这个排序符合直觉但也暴露问题：审稿人会问 \\\"如果 continuation  vs elaboration 差 5pp，那 real-world 混合 prompt 场景下性能如何？\\\" Paper 需要报告 cross-prompt-type transfer（lopto），avg 0.753 表明 prompt-type 泛化合理但非完美。审稿人不会在这个实验上深入追问—— 它是 supporting evidence，不是 core claim。\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"构建 paraphrastic chains 与 continuation chains 做直接对比， 测试 attractor convergence theory（paraphrasing 是否更快收敛）。\\n\",\n    \"results\": {\n      \"paraphrastic_cv_f1\": 0.62,\n      \"paraphrastic_ci\": [\n        0.6,\n        0.64\n      ],\n      \"continuation_cv_f1\": 0.781,\n      \"continuation_ci\": [\n        0.765,\n        0.797\n      ],\n      \"delta_pp\": -16.1,\n      \"paraphrastic_depth_retention_d4_d0\": 0.97,\n      \"paraphrastic_hapax_drift\": -0.35,\n      \"paraphrastic_entropy_mean_drift\": -0.22,\n      \"attractor_effect_observed\": true,\n      \"binary_f1_paraphrastic\": 0.55,\n      \"binary_f1_continuation\": 0.694\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Paraphrastic vs Non-Paraphrastic Chains\",\n        \"columns\": [\n          \"Chain_Type\",\n          \"CV_F1\",\n          \"Binary_F1\",\n          \"hapax_ρ\",\n          \"entropy_mean_ρ\",\n          \"Retention_d4\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.781,\n            0.694,\n            -0.74,\n            -0.56,\n            0.831\n          ],\n          [\n            \"Paraphrastic\",\n            0.62,\n            0.55,\n            -0.35,\n            -0.22,\n            0.97\n          ],\n          [\n            \"Δ\",\n            -0.161,\n            -0.144,\n            \"+0.39 (weaker)\",\n            \"+0.34 (weaker)\",\n            \"+0.139\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"结果清晰支持 scope boundary：本方法不适用于 paraphrastic chains。 这对论文定位有利（honest scoping），但也意味着方法的实用场景被进一步缩窄—— 在 median 档下，审稿人会在 \\\"practical relevance\\\" 维度扣 0.25-0.5pp。\\n\\n\\nMedian 档下，paraphrastic chains 的 depth signal 显著弱于 continuation chains （F1 0.62 vs 0.781, -16pp），符合 attractor convergence theory 预测： paraphrasing 保持语义不变，distributional features 快速收敛到 attractor， 深度间差异被压缩。hapax drift 仅 -0.35（vs continuation -0.74）， entropy_mean drift 仅 -0.22（vs -0.56）。这验证了 paper 的核心 scope claim： 方法针对 non-paraphrastic chains，paraphrastic 场景需要不同方法。 审稿人会认为这是 expected result（不加分也不扣分），但写入 paper  有助于 position scope boundary。Binary F1 只有 0.55 进一步说明 gen-1/gen-2+ 在 paraphrastic 链中几乎不可区分。\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains：每个 depth step 用不同生成器，模拟 real-world  web contamination（多源 LLM 混合）。\\n\",\n    \"results\": {\n      \"cross_model_binary_f1\": 0.83,\n      \"cross_model_binary_ci\": [\n        0.815,\n        0.845\n      ],\n      \"cross_model_3class_f1\": 0.789,\n      \"cross_model_3class_ci\": [\n        0.775,\n        0.803\n      ],\n      \"single_model_binary_f1_ref\": 0.694,\n      \"delta_vs_single_model\": \"+0.136\",\n      \"n_generators_in_pool\": 5,\n      \"generator_level_logo_f1\": 0.83,\n      \"heterogeneity_amplifies_signal\": true,\n      \"per_depth_f1\": {\n        \"gen0\": 0.95,\n        \"gen1\": 0.82,\n        \"gen2plus\": 0.78\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Single-Model vs Cross-Model Chains\",\n        \"columns\": [\n          \"Setup\",\n          \"Binary_F1\",\n          \"3-Class_F1\",\n          \"N_Generators\",\n          \"Eval_Protocol\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model (LOGO)\",\n            0.694,\n            0.762,\n            \"5 (1 per chain)\",\n            \"LOGO\"\n          ],\n          [\n            \"Cross-model (LOGO)\",\n            0.83,\n            0.789,\n            \"5 (mixed per chain)\",\n            \"Generator-LOGO\"\n          ],\n          [\n            \"Δ\",\n            \"+0.136\",\n            \"+0.027\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model 的高 F1 是 paper 的 second headline result，在 median 档下 被审稿人接受为有趣且 practically relevant。但 \\\"是否在学 generator identity\\\"  的质疑需要用 feature importance 分析回应——如果 cross-model 下 shape features  importance 上升，说明分类器确实在用 depth-related signal。\\n\\n\\nMedian 档下最 surprising 的正面结果：cross-model chains binary F1=0.830  远高于 single-model 0.694（+13.6pp）。原因：不同生成器在每个 depth step  引入不同的 distributional signature，generator heterogeneity 放大了  depth-to-depth 的 feature variance，使分类更容易。这对 practical relevance  有利——real-world 的多源 LLM 混合场景恰好是 DDR 最强的条件。 但审稿人会质疑：(1) cross-model setup 中分类器是否在学习 \\\"generator identity\\\"  而非 \\\"depth\\\"？(2) 5-gen pool 是否过小？在 median 档下这被标为 minor concern， 不影响 acceptance。LOGO evaluation 确保没有 generator leakage。\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"扩展到 4 个 domain (Wikipedia, news, scientific, creative/code)， 500 seeds × 5 depths per domain，测试 domain independence。\\n\",\n    \"results\": {\n      \"wikipedia_binary_f1\": 0.695,\n      \"news_binary_f1\": 0.712,\n      \"academic_binary_f1\": 0.628,\n      \"code_binary_f1\": 0.687,\n      \"overall_binary_f1\": 0.676,\n      \"overall_binary_ci\": [\n        0.664,\n        0.688\n      ],\n      \"max_gap_vs_wiki_pp\": 6.7,\n      \"worst_domain\": \"academic\",\n      \"best_new_domain\": \"news\",\n      \"domain_independent_label\": \"moderate\",\n      \"cross_domain_transfer_f1\": 0.65,\n      \"ddr_trend_preserved_all_domains\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Multi-Domain Binary F1\",\n        \"columns\": [\n          \"Domain\",\n          \"Binary_F1\",\n          \"95%_CI\",\n          \"hapax_ρ\",\n          \"entropy_mean_ρ\"\n        ],\n        \"rows\": [\n          [\n            \"News\",\n            0.712,\n            \"[0.690, 0.733]\",\n            -0.65,\n            -0.58\n          ],\n          [\n            \"Wikipedia\",\n            0.695,\n            \"[0.675, 0.715]\",\n            -0.63,\n            -0.6\n          ],\n          [\n            \"Code\",\n            0.687,\n            \"[0.664, 0.710]\",\n            -0.58,\n            -0.55\n          ],\n          [\n            \"Academic\",\n            0.628,\n            \"[0.603, 0.652]\",\n            -0.52,\n            -0.48\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain independence 部分成立（趋势保留），但性能 gap 存在。Academic domain  的弱表现可以在 paper 中用 \\\"低 baseline vocabulary diversity\\\" 解释， 但需要显式讨论。这个实验在 median 档下为 Claim 1 增加了 moderate support， 但也暴露了 method 在 specialized text domains 的局限。\\n\\n\\nMedian 档下，DDR 趋势在所有 domain 中保留，但分类性能有 domain 依赖性。 Academic domain 最弱 (0.628)——scientific text 的 vocabulary 本身就 specialized  且 low-diversity（术语重复率高），压缩了 surface features 的 discriminative range。 News (0.712) 最强——新闻文体的 vocabulary diversity 高，depth-driven  impoverishment 更易检测。Wikipedia (0.695) 接近 LOGO average  （训练数据的主要来源就是 Wiki seeds）。Code domain (0.687) 意外接近 Wiki， 因为代码的 token distribution 有独特结构。 审稿人会关注 academic domain 的 gap (−6.7pp vs Wiki)，但作为 Findings paper  这个 cross-domain analysis 是 bonus evidence，不是 core claim。\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4)，测试 3-class  之外是否有更多 depth signal。附带 ordinal methods (CORAL, Frank-Hall)。\\n\",\n    \"results\": {\n      \"five_class_macro_f1\": 0.5,\n      \"five_class_ci\": [\n        0.48,\n        0.52\n      ],\n      \"three_class_macro_f1_ref\": 0.762,\n      \"delta_5class_vs_3class\": -0.262,\n      \"coral_f1\": 0.5,\n      \"frank_hall_f1\": 0.49,\n      \"standard_xgboost_f1\": 0.5,\n      \"ordinal_methods_improve\": false,\n      \"per_class_5class_f1\": {\n        \"gen0\": 0.92,\n        \"gen1\": 0.55,\n        \"gen2\": 0.35,\n        \"gen3\": 0.3,\n        \"gen4\": 0.38\n      },\n      \"bottleneck\": \"gen-2/gen-3 boundary (practically indistinguishable)\",\n      \"confusion_concentration\": \"gen-2 and gen-3 mutually confused (65% of errors)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 5-Class vs 3-Class Ordinal Classification\",\n        \"columns\": [\n          \"N_Classes\",\n          \"Method\",\n          \"Macro_F1\",\n          \"Gen-0_F1\",\n          \"Gen-1_F1\",\n          \"Gen-2(+)_F1\"\n        ],\n        \"rows\": [\n          [\n            3,\n            \"XGBoost\",\n            0.762,\n            0.95,\n            0.68,\n            0.66\n          ],\n          [\n            5,\n            \"XGBoost\",\n            0.5,\n            0.92,\n            0.55,\n            \"0.35/0.30/0.38\"\n          ],\n          [\n            5,\n            \"CORAL\",\n            0.5,\n            0.91,\n            0.56,\n            \"0.34/0.31/0.38\"\n          ],\n          [\n            5,\n            \"Frank-Hall\",\n            0.49,\n            0.9,\n            0.54,\n            \"0.33/0.30/0.37\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-class 结果清晰支持 paper 的 \\\"3-class ceiling\\\" claim。无需调整叙事。 Gen-1/gen-2+ boundary 是分辨率瓶颈（86% binary errors as FN）， 更细分只会引入更多 noise。这个实验是 clean negative result，审稿人不会追问。\\n\\n\\nMedian 档下，5-class F1 约 0.50——比 3-class (0.762) 下降 26pp， 证实 3-class 是 practical resolution ceiling。Gen-2/gen-3/gen-4 之间 几乎不可区分（F1 分别为 0.35/0.30/0.38），因为 features 在 depth ≥2 后 趋于饱和（DDR 的 drift 是减速的，不是线性的）。Ordinal methods (CORAL,  Frank-Hall) 未改善性能——说明瓶颈不在 model structure 而在 feature signal。 审稿人会接受 \\\"3-class resolution ceiling\\\" 的结论，这是 honest limitation。 Gen-4 的 F1 (0.38) 反而略高于 gen-3 (0.30)，可能是因为 gen-4  features 已极度偏离 gen-0 baseline，形成了另一个 discriminative boundary。\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated human edits: (A) random word replacement (5/10/20%),  (B) LLM-simulated rephrasing。\\n\",\n    \"results\": {\n      \"baseline_binary_f1\": 0.695,\n      \"random_5pct_f1\": 0.65,\n      \"random_10pct_f1\": 0.614,\n      \"random_20pct_f1\": 0.591,\n      \"llm_rephrase_binary_f1\": 0.647,\n      \"llm_rephrase_ci\": [\n        0.631,\n        0.662\n      ],\n      \"llm_rephrase_multiclass_f1\": 0.667,\n      \"edit_distance_ratio\": 0.507,\n      \"avg_sentences_replaced\": 1.69,\n      \"graceful_degradation\": true,\n      \"catastrophic_threshold\": \">20% random replacement\",\n      \"delta_5pct\": -0.046,\n      \"delta_10pct\": -0.081,\n      \"delta_20pct\": -0.104,\n      \"delta_llm_rephrase\": -0.045\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Robustness to Human Editing\",\n        \"columns\": [\n          \"Edit_Type\",\n          \"Edit_Rate\",\n          \"Binary_F1\",\n          \"Δ_vs_Baseline\"\n        ],\n        \"rows\": [\n          [\n            \"None (baseline)\",\n            \"0%\",\n            0.695,\n            \"—\"\n          ],\n          [\n            \"Random replacement\",\n            \"5%\",\n            0.65,\n            -0.046\n          ],\n          [\n            \"Random replacement\",\n            \"10%\",\n            0.614,\n            -0.081\n          ],\n          [\n            \"Random replacement\",\n            \"20%\",\n            0.591,\n            -0.104\n          ],\n          [\n            \"LLM rephrasing\",\n            \"~50% edit dist\",\n            0.647,\n            -0.045\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation 成立。审稿人在 median 档下对此满意， 但会在 limitations 中注明 \\\"real-world editing patterns may differ from  random replacement and LLM rephrasing\\\"。\\n\\n\\nMedian 档下，method 在 light editing 下展现 graceful degradation： 5% random replacement 仅降 4.6pp (0.695→0.650)，LLM rephrasing 降 4.5pp  (0.695→0.647)。审稿人会认为这个 robustness 是 \\\"acceptable but not impressive\\\"—— real-world human editing 通常比 5% random replacement 更 targeted 也更 destructive。 20% replacement 下降至 0.591（-10.4pp），说明 heavy editing 破坏 depth signal。 LLM rephrasing（avg 1.69 sentences replaced, edit distance 0.507）接近 5%  random 的效果，说明 LLM-style editing 是一种 moderate perturbation。 审稿人不会在这个实验上深入追问——它作为 appendix material 回应 RC5 即可。\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"加入 LD-Score (character-level distribution signature) 作为第 8 个特征， 测试 character-level signal 是否与 token-level features 互补。\\n\",\n    \"results\": {\n      \"seven_feature_f1\": 0.804,\n      \"eight_feature_with_ld_f1\": 0.811,\n      \"delta\": \"+0.007\",\n      \"ld_score_importance_rank\": \"6/8 (below entropy_mean, above entropy_min)\",\n      \"ld_score_spearman_depth\": -0.42,\n      \"ld_score_solo_f1\": 0.721,\n      \"ld_score_is_drifting\": true,\n      \"ld_score_corr_with_hapax\": 0.68,\n      \"marginal_contribution_significant\": false,\n      \"mcnemar_p_7_vs_8\": 0.12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LD-Score Feature Addition\",\n        \"columns\": [\n          \"Feature_Set\",\n          \"N_Features\",\n          \"Macro_F1\",\n          \"Binary_F1\",\n          \"McNemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature baseline\",\n            7,\n            0.804,\n            0.694,\n            \"—\"\n          ],\n          [\n            \"+ LD-Score\",\n            8,\n            0.811,\n            0.699,\n            0.12\n          ],\n          [\n            \"LD-Score only\",\n            1,\n            0.721,\n            0.64,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score 不改变 headline numbers。作为 appendix 中 \\\"character-level  features provide redundant signal\\\" 的 evidence 有价值，支持论文选择  token-level features 的 design decision。\\n\\n\\nMedian 档下，LD-Score 作为单独特征表现不错（solo F1=0.721），但加入 7-feature  ensemble 后边际贡献仅 +0.7pp (0.804→0.811)，McNemar p=0.12 不显著。 原因：LD-Score 与 hapax_ratio 相关性高（r=0.68），character-level  和 token-level vocabulary diversity 高度共线。LD-Score 属于 drifting 类别 （ρ=-0.42），进一步支持 DDR 中 central-tendency features drift 的结论， 但不提供独立信息。审稿人不会对这个结果有强烈反应——它是 nice-to-have  analysis，写入 appendix 即可。不建议将 LD-Score 加入 main feature set  以保持 7-feature 的简洁叙事。\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned small LM (OLMo-1B-Instruct or Qwen3-1.7B) for end-to-end  depth classification，对比 handcrafted features。\\n\",\n    \"results\": {\n      \"qlora_3class_f1_instruct\": 0.89,\n      \"qlora_3class_ci\": [\n        0.88,\n        0.91\n      ],\n      \"qlora_binary_f1_instruct\": 0.84,\n      \"qlora_binary_ci\": [\n        0.82,\n        0.85\n      ],\n      \"qlora_5class_f1\": 0.6,\n      \"seven_feature_3class_f1_ref\": 0.762,\n      \"seven_feature_binary_f1_ref\": 0.694,\n      \"delta_3class\": \"+0.128\",\n      \"delta_binary\": \"+0.146\",\n      \"qlora_base_3class_f1\": 0.86,\n      \"qlora_base_binary_f1\": 0.79,\n      \"inference_cost_ratio\": \"~150× (1B model vs 410M ref + XGBoost)\",\n      \"gpu_memory_gb\": 4.2,\n      \"training_time_minutes\": 28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Handcrafted vs End-to-End Classification\",\n        \"columns\": [\n          \"Method\",\n          \"3-Class_F1\",\n          \"Binary_F1\",\n          \"5-Class_F1\",\n          \"Inference_Cost\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature XGBoost\",\n            0.762,\n            0.694,\n            0.5,\n            \"1× (410M ref)\"\n          ],\n          [\n            \"QLoRA OLMo-1B-Instruct\",\n            0.889,\n            0.836,\n            0.598,\n            \"~150×\"\n          ],\n          [\n            \"QLoRA Qwen3-1.7B-Instruct\",\n            0.907,\n            0.867,\n            0.551,\n            \"~250×\"\n          ],\n          [\n            \"QLoRA OLMo-1B-Base\",\n            0.859,\n            0.793,\n            0.54,\n            \"~150×\"\n          ],\n          [\n            \"QLoRA Qwen3-1.7B-Base\",\n            0.904,\n            0.86,\n            0.554,\n            \"~250×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"QLoRA 结果是 median 档下的 strategic risk：它验证了 depth signal 的真实性 （fine-tuned model 能学到），但也暴露了 handcrafted features 的 performance gap。 Paper 必须在 discussion 中坦诚报告，positioning 7-feature 为  \\\"interpretable + efficient diagnostic\\\" 而非 \\\"best classifier\\\"。 审稿人会要求这段讨论的存在——缺失会被标为 major issue。\\n\\n\\nMedian 档下，QLoRA end-to-end 分类器大幅超越 7-feature ensemble  （3-class +12.8pp, binary +14.6pp）。这是一个 double-edged result： 它证明 depth signal 存在且比 7 features 捕获的更丰富，但也意味着  审稿人会问 \\\"既然 fine-tuned LM 远优于 handcrafted features， 为什么不直接用 LM？\\\" Paper 的回应是 efficiency argument： 7-feature ensemble 只需 410M ref model + XGBoost（推理速度 ~150× faster）， 且 features 可解释（DDR analysis 的基础）。QLoRA 是 black-box。 在 median 档下，审稿人接受 efficiency argument 但会标注： \\\"the main methodological contribution (handcrafted features) is substantially  outperformed by standard fine-tuning\\\"——这削弱了 method 维度的 novelty claim。 Instruct model (0.89) 略优于 base (0.86)，因为 instruct 的 classification  head 更容易学习 task-specific patterns。5-class F1 (0.60) 仍远低于理想， 确认 5-class resolution ceiling。\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"排除 text length confound：(A) length-depth correlation,  (B) length-normalized features, (C) length-matched classifier evaluation。\\n\",\n    \"results\": {\n      \"spearman_length_depth_range\": [\n        -0.066,\n        0.134\n      ],\n      \"length_depth_correlation\": \"weak (|ρ|<0.14)\",\n      \"normalized_ttr_trend_preserved\": true,\n      \"normalized_hapax_trend_preserved\": true,\n      \"normalized_rho_stronger\": true,\n      \"length_matched_binary_f1\": 0.724,\n      \"unmatched_binary_f1\": 0.77,\n      \"delta_length_matched\": -0.046,\n      \"random_subsample_control_f1\": 0.74,\n      \"length_is_confound\": false,\n      \"dropout_short_text_bias\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Length Control Analysis\",\n        \"columns\": [\n          \"Condition\",\n          \"Binary_F1\",\n          \"Δ_vs_Full\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Full (unmatched)\",\n            0.77,\n            \"—\",\n            \"N=full dataset\"\n          ],\n          [\n            \"Length-matched\",\n            0.724,\n            -0.046,\n            \"Length distributions equalized\"\n          ],\n          [\n            \"Random subsample (same N)\",\n            0.74,\n            -0.03,\n            \"Size control\"\n          ],\n          [\n            \"Δ attributable to length\",\n            \"—\",\n            -0.016,\n            \"0.046 - 0.030\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clean confound control。Attributable length effect 仅 1.6pp（4.6pp total drop  中 3pp 来自 sample reduction）。审稿人在 median 档下对此满意—— 这是 paper credibility 的必要 check，不是 exciting finding。\\n\\n\\nMedian 档下，length confound 被有效排除但有 nuance。Length-depth 相关性弱 (|ρ|<0.14)，说明 deeper text 不是系统性地更短或更长。Length-normalized  surface features (TTR, hapax on fixed windows) 保留 drifting trend 且  ρ 值更强（normalization 消除了短文本 noise）。Length-matched subsampling  后 binary F1 从 0.770 降至 0.724（-4.6pp），但 random subsample control  (0.740) 也降了 3pp，说明 drop 主要来自 sample size reduction（短文本 dropout  减少了 training data），而非 length 本身是 confound。 审稿人会接受 \\\"length is not a confound\\\" 结论，但可能追问 4.6pp drop 的  composition。Paper 需要同时报告 random-subsample control 以 deconfound  the deconfounding。\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"加入 7B+ generator (Qwen3-8B-Base) 测试 scale effect。 1000 seeds × 5 depths。\\n\",\n    \"results\": {\n      \"total_records\": 4497,\n      \"unique_seeds\": 995,\n      \"depth_dist\": {\n        \"0\": 995,\n        \"1\": 979,\n        \"2\": 937,\n        \"3\": 831,\n        \"4\": 755\n      },\n      \"logo_6gen_avg_f1\": 0.789,\n      \"logo_qwen3_8b_held_out_f1\": 0.683,\n      \"logo_5gen_baseline_f1\": 0.8,\n      \"delta_6gen_vs_5gen\": -0.011,\n      \"spearman_hapax\": -0.558,\n      \"spearman_ttr\": -0.542,\n      \"spearman_entropy_mean\": -0.475,\n      \"spearman_tail_decay\": -0.089,\n      \"scale_degradation_confirmed\": true,\n      \"degradation_magnitude\": \"moderate (-0.011 avg, Qwen3-8B at 0.683 vs 0.694 avg)\",\n      \"per_gen_ranking\": \"pythia-1b > qwen3-0.6b > pythia-2.8b > qwen3-1.7b > olmo-2-1b > qwen3-8b\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Scale Effect (6-Generator LOGO)\",\n        \"columns\": [\n          \"Generator\",\n          \"Params\",\n          \"LOGO_Binary_F1\",\n          \"hapax_ρ\",\n          \"entropy_mean_ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            \"1B\",\n            0.718,\n            -0.65,\n            -0.64\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            0.659,\n            -0.6,\n            -0.58\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"2.8B\",\n            0.724,\n            -0.63,\n            -0.6\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"1.7B\",\n            0.702,\n            -0.61,\n            -0.57\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            0.668,\n            -0.57,\n            -0.52\n          ],\n          [\n            \"Qwen3-8B\",\n            \"8B\",\n            0.683,\n            -0.56,\n            -0.48\n          ],\n          [\n            \"**6-gen avg**\",\n            \"—\",\n            \"**0.692**\",\n            \"-0.60\",\n            \"-0.57\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Depth Retention at Scale\",\n        \"columns\": [\n          \"Generator\",\n          \"gen4_retention\",\n          \"gen3_retention\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"83.1%\",\n            \"87.8%\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"75.9%\",\n            \"83.5%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale effect 是 honest limitation（-1.1pp avg degradation）。8B 是当前最大  generator，DDR 仍然 work（F1=0.683, above chance）。但 trend suggests  更大模型可能 further degrade。审稿人会标注但不会因此 reject。 加入 Mistral-7B 后（plan 外但 registry 显示已完成）worst-case 降至 0.633， 进一步说明 large-model challenge。\\n\\n\\nMedian 档下，Qwen3-8B-Base 的 LOGO F1 (0.683) 低于 5-gen average (0.694)， 确认 scale degradation 存在但 moderate。Higher-capacity models 压缩 feature  margins：hapax ρ=-0.558（vs avg -0.63），entropy_mean ρ=-0.475（vs avg -0.60）。 DDR 趋势保留但幅度缩小。6-gen LOGO avg (0.789 macro) 比 5-gen (0.800)  降 1.1pp——可接受。审稿人在 median 档下不会将此视为 major weakness  但会要求在 limitations 中讨论 scale trend。Depth retention 更低 (gen-4 仅 755/995=75.9% vs 5-gen avg ~85%)——大模型 generation  truncation 更频繁（EOS token 更 aggressive），需要在 paper 中提及。 审稿人可能追问 \\\"如果 70B 模型呢？\\\"——这是 base-model scope 的内在局限， 只能诚实标注为 future work。\\n\"\n  },\n  {\n    \"name\": \"ordinal_baseline_comparison\",\n    \"description\": \"CRITICAL baseline: 测试 FastDetectGPT / Binoculars / LD-Score / Avg-LogProb  的 continuous scores 是否已提供 ordinal depth signal，与 7-feature 对比。\\n\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"seven_feature_ci\": [\n        0.786,\n        0.799\n      ],\n      \"avg_logprob_logo_f1\": 0.765,\n      \"avg_logprob_ci\": [\n        0.616,\n        0.82\n      ],\n      \"ld_score_logo_f1\": 0.721,\n      \"ld_score_ci\": [\n        0.588,\n        0.77\n      ],\n      \"fast_detect_gpt_logo_f1\": 0.627,\n      \"fast_detect_gpt_ci\": [\n        0.511,\n        0.762\n      ],\n      \"binoculars_logo_f1\": 0.579,\n      \"binoculars_ci\": [\n        0.405,\n        0.664\n      ],\n      \"best_single_detector\": \"Avg-LogProb (0.765)\",\n      \"seven_feature_advantage_pp\": 3.3,\n      \"bootstrap_7feat_vs_avglogprob_p\": 0.0,\n      \"bootstrap_7feat_vs_avglogprob_delta\": 0.039,\n      \"bootstrap_7feat_vs_fdgpt_p\": 0.0,\n      \"multi_detector_ensemble_f1\": 0.795,\n      \"multi_detector_ci\": [\n        0.78,\n        0.81\n      ],\n      \"four_det_plus_surface_f1\": 0.795,\n      \"delta_7feat_vs_4det\": \"+0.003\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 7-Feature vs Existing Detector Baselines (LOGO)\",\n        \"columns\": [\n          \"Method\",\n          \"LOGO_Macro_F1\",\n          \"95%_CI\",\n          \"Spearman_ρ_depth\",\n          \"N_Models_Required\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature XGBoost\",\n            0.798,\n            \"[0.786, 0.799]\",\n            \"—\",\n            \"1 (410M ref)\"\n          ],\n          [\n            \"Avg-LogProb\",\n            0.765,\n            \"[0.616, 0.820]\",\n            0.788,\n            \"1 (410M ref)\"\n          ],\n          [\n            \"LD-Score\",\n            0.721,\n            \"[0.588, 0.770]\",\n            0.794,\n            0\n          ],\n          [\n            \"FastDetectGPT\",\n            0.627,\n            \"[0.511, 0.762]\",\n            0.433,\n            \"2 (source + scoring)\"\n          ],\n          [\n            \"Binoculars\",\n            0.579,\n            \"[0.405, 0.664]\",\n            0.199,\n            \"2 (observer + performer)\"\n          ],\n          [\n            \"4-det + surface ensemble\",\n            0.795,\n            \"[0.780, 0.810]\",\n            \"—\",\n            \"4+ models\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Bootstrap Pairwise Comparisons\",\n        \"columns\": [\n          \"Comparison\",\n          \"Delta\",\n          \"p_value\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"7-feat vs Avg-LogProb\",\n            \"+0.033\",\n            0.0,\n            true\n          ],\n          [\n            \"7-feat vs LD-Score\",\n            \"+0.077\",\n            0.0,\n            true\n          ],\n          [\n            \"7-feat vs FastDetectGPT\",\n            \"+0.171\",\n            0.0,\n            true\n          ],\n          [\n            \"7-feat vs 4-det ensemble\",\n            \"+0.003\",\n            0.38,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Baseline comparison 是 paper 能否被接收的 gatekeeping experiment。 7-feature 优势统计显著但 practical margin 不大（+3.3pp vs Avg-LogProb）。 在 median 档下，审稿人接受 \\\"custom features add value\\\" 但会标注  \\\"the advantage is modest\\\"。关键防线是 CI width argument 和 DDR  conceptual contribution——如果 paper 只 claim classification performance， 这个 margin 不够；但如果 position 为 \\\"empirical characterization of DDR,  with classification as validation\\\"，审稿人更容易接受。\\n\\n\\nMedian 档的 critical baseline test 通过但 margin 不大。7-feature (0.798)  显著优于所有 single detectors（bootstrap p=0），但 Avg-LogProb (0.765)  的 gap 仅 3.3pp。审稿人会说 \\\"7-feature set 的优势 modest，而且 Avg-LogProb  作为 single feature 已经不错了——custom features 的边际贡献在 practical  意义上有多大？\\\" 在 median 档下这个质疑被 offset by 两个论点： (1) 7-feature 的 CI 远窄于单检测器（cross-generator variance 更低）， 说明 robustness 更好；(2) DDR analysis 需要多个 features 才能做（ 这是 conceptual contribution，不只是 classification performance）。 Multi-detector ensemble (4-det + surface, 0.795) 与 7-feature (0.798)  几乎等效但需要 2.4× inference cost + 3.2× GPU memory， 支持 efficiency positioning。Binoculars CI 极宽 [0.405, 0.664]  说明它对 generator 极度敏感。\\n\"\n  },\n  {\n    \"name\": \"9-gen scale evaluation (with Gemma-2-2B)\",\n    \"description\": \"扩展至 9 个 generator (原 8 + Gemma-2-2B) 的 LOGO 评估， 测试 broader generalization 和 edge cases。\\n\",\n    \"results\": {\n      \"nine_gen_logo_3class_f1\": 0.751,\n      \"nine_gen_logo_binary_f1\": 0.666,\n      \"eight_gen_baseline_3class_f1\": 0.77,\n      \"delta_9gen_vs_8gen\": -0.019,\n      \"gemma_2_2b_3class_f1\": 0.628,\n      \"gemma_2_2b_binary_f1\": 0.44,\n      \"gemma_2_2b_gen1_f1\": 0.036,\n      \"mistral_7b_3class_f1\": 0.605,\n      \"mistral_7b_binary_f1\": 0.633,\n      \"per_gen_3class_range\": [\n        0.605,\n        0.857\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 9-Generator LOGO Results\",\n        \"columns\": [\n          \"Generator\",\n          \"Family\",\n          \"Params\",\n          \"3-Class_F1\",\n          \"Binary_F1\",\n          \"Gen-1_F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            \"1B\",\n            0.857,\n            0.718,\n            0.65\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"Qwen\",\n            \"0.6B\",\n            0.819,\n            0.659,\n            0.61\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            \"2.8B\",\n            0.812,\n            0.724,\n            0.68\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Qwen\",\n            \"1.7B\",\n            0.811,\n            0.702,\n            0.66\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1.5B\",\n            0.773,\n            0.668,\n            0.58\n          ],\n          [\n            \"Llama-3.2-3B\",\n            \"Llama\",\n            \"3B\",\n            0.759,\n            0.69,\n            0.6\n          ],\n          [\n            \"Qwen3-8B\",\n            \"Qwen\",\n            \"8B\",\n            0.696,\n            0.647,\n            0.52\n          ],\n          [\n            \"**Gemma-2-2B**\",\n            \"Gemma\",\n            \"2B\",\n            \"**0.628**\",\n            \"**0.440**\",\n            \"**0.036**\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"Mistral\",\n            \"7B\",\n            0.605,\n            0.633,\n            0.44\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma anomaly 是 median 档审稿人重点追问对象。-0.25pp reviewer penalty  的来源。Paper 处理策略：承认 failure case，分析 Gemma gen-1 的 feature  distribution（是否与 gen-0 truly indistinguishable），讨论可能的  architectural 原因（GQA, training data composition）。\\n\\n\\nMedian 档下 Gemma-2-2B 是 paper 中最显著的 anomaly：gen-1 F1=0.036  意味着分类器完全无法识别 Gemma 的 gen-1 output。原因：Gemma-2 的  architecture (grouped-query attention + RMSNorm) 和 training recipe  使其 gen-1 的 distributional features 异常接近 gen-0——depth signal  在第一步就极度微弱。这是 method failure 而非 Gemma 特殊性， 因为其他大模型 (Qwen3-8B, Mistral-7B) 虽然 F1 较低但仍在 0.63+ 水平。 审稿人会追问：\\\"gen-1 F1=0.036 是否意味着方法对某些 architecture  完全失败？如果是，如何判断哪些 generator 会失败？\\\" 这是 rebuttal 中需要回应的 medium-severity concern。 Paper 必须在 9-gen appendix 中显式讨论 Gemma anomaly， 并承认 \\\"方法不保证对所有 generator architectures 均有效\\\"。\\n\"\n  },\n  {\n    \"name\": \"DDR causality analysis\",\n    \"description\": \"通过 permutation importance, Granger causality, feature intervention  三种方法验证 DDR 的 causal structure。\\n\",\n    \"results\": {\n      \"permutation_baseline_f1\": 0.771,\n      \"drifting_avg_importance\": 0.158,\n      \"stationary_avg_importance\": 0.03,\n      \"drifting_stationary_ratio\": 5.3,\n      \"granger_significant\": \"6/7 features\",\n      \"granger_nonsig\": \"entropy_min\",\n      \"granger_max_delta_r2\": 0.031,\n      \"intervention_max_f1_drop\": 0.02,\n      \"intervention_max_feature\": \"entropy_max\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DDR Causality Evidence\",\n        \"columns\": [\n          \"Method\",\n          \"Drifting_Signal\",\n          \"Stationary_Signal\",\n          \"Gap_Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"Permutation importance\",\n            0.158,\n            0.03,\n            \"5.3×\"\n          ],\n          [\n            \"Granger causality\",\n            \"6/7 sig (p<0.05)\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Feature intervention (max F1 drop)\",\n            0.02,\n            0.006,\n            \"3.3×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Causality analysis 为 DDR 提供了超越 correlation 的 evidence， 但 effect sizes 偏小。在 median 档下这是 \\\"nice methodological rigor\\\"  而非 game-changer。\\n\\n\\nMedian 档下，causality analysis 是 DDR claim 的强化 evidence。 5.3× permutation importance gap（drifting 0.158 vs stationary 0.030） 清晰支持 DDR 的 feature-role 划分。6/7 features Granger significant  说明 temporal ordering matters（depth 预测 feature 值）。 但 Granger max delta R² 仅 0.031——effect size 小，审稿人可能认为  \\\"statistically significant but practically negligible\\\"。 Entropy_min 的 non-significance 与其 intermediate status 一致。 Feature intervention max drop 仅 0.020（entropy_max），说明  no single feature is critical——系统鲁棒但个体 feature 贡献分散。 审稿人会认可方法论的 rigor（三种独立 causality tests）， 但不会被 effect sizes 打动。\\n\"\n  },\n  {\n    \"name\": \"TOST bootstrap stability validation\",\n    \"description\": \"Bootstrap TOST 验证 shape features 的 stationarity classification  在重采样下是否稳定。\\n\",\n    \"results\": {\n      \"n_bootstrap\": 1000,\n      \"margin_d\": 0.2,\n      \"entropy_max\": {\n        \"rejection_rate\": 1.0,\n        \"median_d\": 0.062,\n        \"classification\": \"Stationary (robust)\"\n      },\n      \"entropy_min\": {\n        \"rejection_rate\": 1.0,\n        \"median_d\": -0.016,\n        \"classification\": \"Stationary (robust)\"\n      },\n      \"tail_decay\": {\n        \"rejection_rate\": 1.0,\n        \"median_d\": 0.088,\n        \"classification\": \"Stationary (robust)\"\n      },\n      \"entropy_std\": {\n        \"rejection_rate\": 0.0,\n        \"median_d\": 0.458,\n        \"classification\": \"NOT stationary (TOST never rejects)\",\n        \"d_ci\": [\n          0.435,\n          0.479\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: TOST Bootstrap Stability (margin d=0.2)\",\n        \"columns\": [\n          \"Feature\",\n          \"Median_d\",\n          \"d_95%_CI\",\n          \"Rejection_Rate\",\n          \"Classification\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_max\",\n            0.062,\n            \"[0.037, 0.088]\",\n            \"1000/1000\",\n            \"Stationary\"\n          ],\n          [\n            \"entropy_min\",\n            -0.016,\n            \"[-0.042, 0.011]\",\n            \"1000/1000\",\n            \"Stationary\"\n          ],\n          [\n            \"tail_decay\",\n            0.088,\n            \"[0.065, 0.111]\",\n            \"1000/1000\",\n            \"Stationary\"\n          ],\n          [\n            \"**entropy_std**\",\n            \"**0.458**\",\n            \"**[0.435, 0.479]**\",\n            \"**0/1000**\",\n            \"**NOT stationary**\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"entropy_std 的 TOST 结果是 median 档下审稿人最可能追问的 technical point。 Paper 必须从二分法转向 spectrum 模型，否则 internal inconsistency  会被标为 moderate issue。这个调整实际上使论文更 nuanced 也更 honest， 审稿人倾向于正面看待。\\n\\n\\nMedian 档下的 key tension point：三个 shape features (entropy_max,  entropy_min, tail_decay) 通过 TOST 所有 1000 次 bootstrap  (rejection rate=1.0)，d 值远低于 0.2 threshold。但 entropy_std  的 rejection rate=0.0，d=0.458 [0.435, 0.479] 远超 equivalence margin。 这直接否定了将 entropy_std 归入 \\\"stationary\\\" 组的原始分类。 审稿人会追问：\\\"为什么原文将 entropy_std 归为 H1/stationary？ TOST 明确拒绝了 equivalence。这是否意味着 DDR 的二分法本身有问题？\\\" Paper 需要调整：将 entropy_std 移出 stationary 组，要么归入 drifting  (但 ρ=-0.20 比 drifting group 弱很多)，要么引入 \\\"intermediate\\\" 类别。 Median 档的叙事方向选择 spectrum model：drifting → intermediate → stationary， entropy_std 和 entropy_min 居于 intermediate。\\n\"\n  },\n  {\n    \"name\": \"Instruct model evaluation (3 models)\",\n    \"description\": \"在 Qwen3-1.7B-Instruct, OLMo-2-1B-Instruct, Llama-3.2-3B-Instruct 上 测试 depth signal 在 instruct tuning 下的 degradation。\\n\",\n    \"results\": {\n      \"qwen_instruct_logo_binary\": 0.658,\n      \"qwen_instruct_logo_3class\": 0.543,\n      \"olmo_instruct_logo_binary\": 0.338,\n      \"olmo_instruct_logo_3class\": 0.42,\n      \"llama_instruct_binary\": 0.838,\n      \"llama_instruct_3class\": 0.544,\n      \"qwen_base_logo_binary\": 0.821,\n      \"olmo_base_logo_binary\": 0.763,\n      \"llama_base_binary\": 0.849,\n      \"delta_qwen\": -0.163,\n      \"delta_olmo\": -0.425,\n      \"delta_llama\": -0.011,\n      \"feature_reversal_count\": {\n        \"olmo\": \"6/7\",\n        \"qwen\": \"partial (direction flip in entropy_mean)\",\n        \"llama\": \"3/7\"\n      },\n      \"spearman_direction_instruct\": \"多数特征 ρ>0 (reversed from base ρ<0)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Instruct vs Base Model Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"Base_Binary_F1\",\n          \"Instruct_Binary_F1\",\n          \"Δ\",\n          \"Features_Reversed\"\n        ],\n        \"rows\": [\n          [\n            \"OLMo-2-1B\",\n            0.763,\n            0.338,\n            -0.425,\n            \"6/7\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            0.821,\n            0.658,\n            -0.163,\n            \"partial\"\n          ],\n          [\n            \"Llama-3.2-3B\",\n            0.849,\n            0.838,\n            -0.011,\n            \"3/7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Instruct degradation 的异质性（OLMo 极严重，Llama 几乎不受影响） 是一个 interesting finding，但也使 scope boundary 变得模糊—— 审稿人会问 \\\"哪些 instruct model 会 degrade？能否 predict？\\\" 在 median 档下只能回答 \\\"we cannot predict a priori\\\" 并标注为 limitation。\\n\\n\\nMedian 档下 instruct degradation 是 paper 的 primary scope limitation。 OLMo-Instruct 的 LOGO binary F1 仅 0.338（vs base 0.763, -42.5pp）， 6/7 features Spearman ρ 方向反转（base 为负/instruct 为正）。 这说明 instruction tuning 的 format regulation 和 length normalization  破坏甚至反转了 DDR pattern。Qwen-Instruct degradation 中等 (-16.3pp)， Llama-Instruct 最小 (-1.1pp)——instruct 影响的 magnitude 是 model-specific。 审稿人中 1-2 个会标注 \\\"base-model-only scope\\\" 为 major limitation  并扣 -0.5pp。Rebuttal 需要论证：(1) base model 在 data contamination  分析场景下仍然 relevant（web-scraped data 主要由 base/API 模型生成）， (2) instruct 场景是 explicit future work with clear direction。 Feature reversal 的发现本身有一定 novelty——instruct tuning 不只是削弱  depth signal，而是反转了 distributional dynamics，这值得在 discussion 中提及。\\n\"\n  },\n  {\n    \"name\": \"Temperature sensitivity curve\",\n    \"description\": \"温度敏感性分析：t=0.5, 0.7, 0.9, 1.0 的 depth signal 强度和跨温度 transfer。\\n\",\n    \"results\": {\n      \"within_t05_binary\": 0.813,\n      \"within_t07_binary\": 0.694,\n      \"within_t09_binary\": 0.48,\n      \"cross_t07_to_t10_binary_qwen\": 0.418,\n      \"cross_t10_to_t07_binary_qwen\": 0.944,\n      \"delta_t05_vs_t07\": \"+0.119\",\n      \"delta_t09_vs_t07\": \"-0.214\",\n      \"entropy_mean_rho_t05\": -0.58,\n      \"entropy_mean_rho_t07\": -0.6,\n      \"entropy_mean_rho_t09\": -0.3,\n      \"reliable_range\": \"[0.5, 0.9) — ≤1pp degradation within [0.5, 0.7]\",\n      \"cross_temp_transfer_asymmetric\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Temperature Sensitivity\",\n        \"columns\": [\n          \"Temperature\",\n          \"Within-CV_Binary_F1\",\n          \"entropy_mean_ρ\",\n          \"Reliable\"\n        ],\n        \"rows\": [\n          [\n            0.5,\n            0.813,\n            -0.58,\n            \"Yes (stronger signal)\"\n          ],\n          [\n            0.7,\n            0.694,\n            -0.6,\n            \"Yes (default)\"\n          ],\n          [\n            0.9,\n            0.48,\n            -0.3,\n            \"No (severe degradation)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Cross-Temperature Transfer (Qwen3-1.7B)\",\n        \"columns\": [\n          \"Train_Temp\",\n          \"Test_Temp\",\n          \"Binary_F1\",\n          \"Δ_vs_Within\"\n        ],\n        \"rows\": [\n          [\n            0.7,\n            0.7,\n            0.789,\n            \"—\"\n          ],\n          [\n            0.7,\n            1.0,\n            0.418,\n            -0.371\n          ],\n          [\n            1.0,\n            0.7,\n            0.944,\n            \"+0.155\"\n          ],\n          [\n            1.0,\n            1.0,\n            0.825,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"温度限制在 median 档下被标为 known scope boundary。 t≥0.9 的 degradation 源于 high-temperature sampling 的 entropy inflation—— 所有 depth 的 entropy features 都被推高，压缩了 depth-to-depth 差异。\\n\\n\\nMedian 档下，温度敏感性是第二个 scope limitation。t∈[0.5, 0.7]  内 depth signal 稳定（0.694-0.813），但 t=0.9 时急剧下降至 0.480  (below chance for binary)，entropy_mean ρ 从 -0.60 降至 -0.30。 t=1.0 下跨温度 transfer 极差（Qwen t=0.7→t=1.0: 0.789→0.418, -37pp）， 但反方向 (t=1.0→t=0.7) 反而好 (0.944)——不对称 transfer 说明  high-temp features 是 low-temp features 的 superset（noise 更大但信号保留）。 Paper 将 \\\"t∈[0.5, 0.9)\\\" 标为 reliable range，t≥0.9 为 degraded。 审稿人在 median 档下会问 \\\"most API models default to t=1.0,  does this limit real-world applicability?\\\"——需要在 limitations 中回应。\\n\"\n  },\n  {\n    \"name\": \"Independent seed validation\",\n    \"description\": \"用完全独立的 seed sets 验证 shared-seed LOGO 是否存在 seed leakage。\\n\",\n    \"results\": {\n      \"pythia_to_olmo_binary\": 0.695,\n      \"olmo_to_pythia_binary\": 0.666,\n      \"avg_independent\": 0.68,\n      \"shared_seed_logo_ref\": 0.694,\n      \"delta_vs_shared\": -0.014\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Seed Leakage Validation\",\n        \"columns\": [\n          \"Setup\",\n          \"Binary_F1\",\n          \"Seeds_Shared\"\n        ],\n        \"rows\": [\n          [\n            \"Shared-seed LOGO\",\n            0.694,\n            \"Yes (same 995 seeds)\"\n          ],\n          [\n            {\n              \"Independent\": \"Pythia→OLMo\"\n            },\n            0.695,\n            false\n          ],\n          [\n            {\n              \"Independent\": \"OLMo→Pythia\"\n            },\n            0.666,\n            false\n          ],\n          [\n            \"Independent avg\",\n            0.68,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Seed leakage 不是问题。-1.4pp delta 在 noise range 内。 作为 supplementary validation 写入 appendix。\\n\\n\\nMedian 档下，independent seed validation 确认 shared-seed LOGO 的  seed leakage 极小（delta 仅 -1.4pp）。Pythia→OLMo (0.695) 几乎等同于  LOGO average (0.694)，说明 seed content 不是主要信号源。 OLMo→Pythia 略低 (0.666) 可能反映 OLMo 作为训练集的 feature space  不完全覆盖 Pythia 的分布。审稿人不会在此处追问——这是一个 clean validation。\\n\"\n  },\n  {\n    \"name\": \"Seed complexity stratification\",\n    \"description\": \"按 seed text complexity (low/medium/high) 分层分析 depth signal 是否依赖 seed 质量。\\n\",\n    \"results\": {\n      \"low_complexity_binary\": 0.685,\n      \"medium_binary\": 0.695,\n      \"high_complexity_binary\": 0.695,\n      \"max_diff_binary_pp\": 1.06,\n      \"seed_independent_label\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Seed Complexity Stratification\",\n        \"columns\": [\n          \"Complexity_Bin\",\n          \"Binary_F1\",\n          \"Multiclass_F1\",\n          \"N_Seeds\"\n        ],\n        \"rows\": [\n          [\n            \"Low\",\n            0.685,\n            0.772,\n            \"~332\"\n          ],\n          [\n            \"Medium\",\n            0.695,\n            0.778,\n            \"~332\"\n          ],\n          [\n            \"High\",\n            0.695,\n            0.779,\n            \"~331\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Clean result. Seed independence confirmed. Appendix material.\\n\\n\\nMedian 档下 seed complexity 对 depth signal 影响极小（max diff 1.06pp）， 确认方法对 seed 质量不敏感。Low complexity seeds 的微弱 drop (1pp)  可能源于低复杂度 text 的 feature range 本身更窄。审稿人不会在此处追问。\\n\"\n  },\n  {\n    \"name\": \"Topic drift correlation\",\n    \"description\": \"分析 semantic similarity (cosine) 与 depth 和 feature drift 的关系。\\n\",\n    \"results\": {\n      \"sim_0to1_mean\": 0.622,\n      \"sim_1to2_mean\": 0.683,\n      \"sim_2to3_mean\": 0.801,\n      \"sim_3to4_mean\": 0.859,\n      \"shape_entropy_std_rho\": -0.164,\n      \"shape_tail_decay_rho\": 0.068,\n      \"drifting_hapax_rho\": -0.124,\n      \"drifting_entropy_mean_rho\": -0.286,\n      \"semantic_convergence_with_depth\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Semantic Similarity by Depth Transition\",\n        \"columns\": [\n          \"Transition\",\n          \"Mean_Cosine_Sim\",\n          \"Std\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0 → gen-1\",\n            0.622,\n            0.165\n          ],\n          [\n            \"gen-1 → gen-2\",\n            0.683,\n            0.184\n          ],\n          [\n            \"gen-2 → gen-3\",\n            0.801,\n            0.201\n          ],\n          [\n            \"gen-3 → gen-4\",\n            0.859,\n            0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semantic convergence + distributional divergence 的 decoupling 是  intellectually interesting 的 supporting evidence。审稿人在 median 档下 会认可但不会因此提高分数。\\n\\nMedian 档下，topic drift analysis 揭示 counter-intuitive pattern： deeper generations 在 semantic space 中 converge（sim 从 0.622 增至 0.859）， 即使 distributional features 在 diverge。这说明 DDR 不是 topic drift  的结果——topic 趋同但 distribution 趋异，方向相反。 Drifting features 与 semantic sim 的弱负相关（entropy_mean ρ=-0.286） 说明两者部分共变但独立性主要成立。Shape features 几乎无关（|ρ|<0.17）。 审稿人可能对 \\\"semantic convergence\\\" finding 感兴趣但这不是 paper 的  core claim。作为 appendix evidence 支持 \\\"DDR is distributional, not semantic\\\"。\\n\"\n  }\n]",
      "numLines": 1872,
      "startLine": 1,
      "totalLines": 1872
    }
  },
  "sourceToolAssistantUUID": "712d0dee-0e66-4a19-9a75-2f079125a475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T10:33:14.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XeijfzGaByMcczT2cRz3ap`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "230af998-bf53-42f7-b166-ab371993e83c",
  "isSidechain": false,
  "requestId": "req_011CbDfmdBoRV86KTfEwGNfm",
  "type": "assistant",
  "uuid": "286ba039-6cbf-4ffd-a7ed-a0611d683931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141g7HRgwts9Zut97XQxFxd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12821,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12821
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

_source line 11 · 2026-05-20T10:33:14.029Z_

<details><summary>↩ Tool result · `toolu_01XeijfzGaByMcczT2cRz3ap`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
5	- Positioning: **Findings paper**（非 main conference long paper）
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.
14	
15	**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.
16	
17	**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.
18	
19	## Headline Metrics Summary
20	
21	| Metric | Value | Context |
22	|--------|-------|---------|
23	| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |
24	| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |
25	| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |
26	| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |
27	| LOFO binary F1 | 0.686 | Leave-one-family-out |
28	| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |
29	| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |
30	| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |
31	| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
32	| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |
33	
34	## Scope & Limitations (必须在论文中突出)
35	
36	1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
37	2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
38	3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
39	4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
40	5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
41	6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).
42	
43	## Story Spine
44	
45	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.
46	
47	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.
48	
49	**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.
50	
51	**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."
52	
53	## Anticipated Reviewer Concerns
54	
55	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.
56	
57	**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.
58	
59	**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.
60	
61	**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.
62	
63	**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.
64	
65	**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).
66	
67	**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.
68	
69	**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.
70	
71	**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.
72	
73	**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.
74	
75	## Contribution Positioning (Findings Level)
76	The contribution is **empirical and conceptual**, appropriate for Findings:
77	1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
78	2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
79	3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.
80	
81	**Framing discipline:**
82	- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
83	- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
84	- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
85	- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
86	- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
87	- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.
88	
89	Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.
90	
91	## Venue Fit
92	- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "286ba039-6cbf-4ffd-a7ed-a0611d683931",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "e032fb2b-60fd-470f-aea8-04a3cd3c44b3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  },
  "sourceToolAssistantUUID": "286ba039-6cbf-4ffd-a7ed-a0611d683931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "e032fb2b-60fd-470f-aea8-04a3cd3c44b3",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260520T100349",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Assistant

_source line 14 · 2026-05-20T10:33:32.797Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write a complete LaTeX paper. I need to ensure the output directory exists first, then write the paper.

Let me organize the paper structure:

1. Abstract
2. Introduction
3. Related Work
4. Method (DDR framework, feature design, evaluation protocol)
5. Experiments (covering all experiments from the JSON)
6. Discussion
7. Conclusion
8. Appendix (for supplementary experiments)

Key data points to include:
- Feature ablation: full 0.82, surface-only 0.763, ref-only 0.719


- Cross-generator performance with LOGO showing binary F1 of 0.694 and macro F1 of 0.804
- Cross-family reference model demonstrating DDR preservation
- Downstream utility findings, prompt type and paraphrastic comparisons
- Cross-model chains achieving binary F1 of 0.83
- Multi-domain seeds and finer-grained ordinal classification at 5-class F1 of 0.50
- Human edit robustness, LD-Score feature analysis
- End-to-end classifier, text length control, and large-scale generator results
- Ordinal baseline comparisons

Writing the LaTeX paper... I see the constraint now—I need to ensure every experiment from the data file has a corresponding section or table in the paper. With twenty experiments total, I'll distribute the core ones across the main text and relegate the more specialized validations to the appendices. Let me start drafting the paper structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e032fb2b-60fd-470f-aea8-04a3cd3c44b3",
  "isSidechain": false,
  "requestId": "req_011CbDfn8vTdNtZ5oYSumaui",
  "type": "assistant",
  "uuid": "385ce50c-6e91-4f2f-8646-0b7b7435eb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9ZE2Y2KakwACFhDULWoMZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32953,
      "cache_read_input_tokens": 24662,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 24662,
          "cache_creation_input_tokens": 32953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32953
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

_source line 15 · 2026-05-20T10:33:34.747Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X85ZETkodEz1bvTMyLjaeJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/",
  "description": "Check output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "385ce50c-6e91-4f2f-8646-0b7b7435eb4d",
  "isSidechain": false,
  "requestId": "req_011CbDfn8vTdNtZ5oYSumaui",
  "type": "assistant",
  "uuid": "e0dc14d6-047d-4077-aebe-085d07e17353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9ZE2Y2KakwACFhDULWoMZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32953,
      "cache_read_input_tokens": 24662,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 24662,
          "cache_creation_input_tokens": 32953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32953
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

_source line 16 · 2026-05-20T10:33:34.869Z_

<details><summary>↩ Tool result · `toolu_01X85ZETkodEz1bvTMyLjaeJ`</summary>

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
  "parentUuid": "e0dc14d6-047d-4077-aebe-085d07e17353",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "400452b0-8977-49b1-bc90-a3d6844586ce",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e0dc14d6-047d-4077-aebe-085d07e17353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T10:33:37.045Z_

Directory exists. Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "400452b0-8977-49b1-bc90-a3d6844586ce",
  "isSidechain": false,
  "requestId": "req_011CbDfog3W4PXnHTGoHXjqQ",
  "type": "assistant",
  "uuid": "e1603476-8fb8-4144-9a8f-aac3f8e077ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4Dg7vvjAZ3YMjrKavcLnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 57615,
      "output_tokens": 15322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15322,
          "cache_read_input_tokens": 57615,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 900
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

_source line 18 · 2026-05-20T10:37:58.304Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RLjRjYa96Z2SP8qxq37VVo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\title{Differential Depth Response in Non-Paraphrastic LLM Generation Chains: \\\\\nAn Empirical Characterization Across Model Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n% ABSTRACT\n%==============================================================================\n\\begin{abstract}\nWeb-scraped corpora increasingly contain LLM-generated text of unknown provenance depth---the number of recursive generation steps from the original human-written source.\nCurrent detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material.\nWe formulate \\emph{generation depth classification} (gen-0/gen-1/gen-2+) for non-paraphrastic continuation chains and characterize a phenomenon we term \\emph{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while shape features (entropy max, tail decay) remain near-stationary ($|\\rho| < 0.10$).\nAcross 8 base-model generators from 5 families (0.6B--8B), a lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under leave-one-generator-out (LOGO) evaluation, and 0.830 on cross-model chains using a single 410M reference model.\nPer-generator binary F1 ranges from 0.633 to 0.724.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language modeling quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm$2\\% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization rather than a curative tool for data selection.\nThe signal degrades substantially under instruction tuning and high temperature ($t \\geq 0.9$), restricting current scope to base models.\nWe also identify \\texttt{entropy\\_std} as an intermediate feature whose classification is inconsistent across reference models, motivating a spectrum model (drifting $\\to$ intermediate $\\to$ stationary) over the original binary partition.\n\\end{abstract}\n\n%==============================================================================\n% 1. INTRODUCTION\n%==============================================================================\n\\section{Introduction}\n\nWeb-scraped training data increasingly contains LLM-generated text of unknown provenance: recent estimates suggest 7--17\\% of scientific papers may contain AI-generated content.\nThis recursive contamination creates \\emph{generation chains} where output from one model becomes input to another, potentially degrading data quality across training iterations.\nCurrent detection methods treat text classification as a binary problem---human-written vs.\\ machine-generated---conflating gen-1 text (which retains much of the source distribution's lexical properties) with deeper generations that exhibit measurably reduced vocabulary diversity and compressed perplexity.\n\nThis binary framing is insufficient for data governance.\nA dataset curator deciding whether to include questionable text needs to know not just \\emph{whether} it was machine-generated, but \\emph{how far removed} it is from the original human source.\nWe formulate \\textbf{generation depth classification} as an ordinal prediction task: given a text passage, determine whether it is gen-0 (human-written), gen-1 (first-generation synthetic), or gen-2+ (recursively generated).\n\nOur central empirical finding is \\textbf{differential depth response (DDR)}: distributional features computed from a reference model's token-level negative log-likelihood (NLL) distribution exhibit systematically different behavior across generation depths.\nCentral-tendency and diversity features---entropy mean, type-token ratio (TTR), and hapax ratio---drift monotonically with depth, consistent with recursive generation inducing a location shift in the NLL distribution.\nShape features---entropy max and tail decay---remain approximately stationary, preserving distributional shape even as the center shifts.\nThis differential response is not an artifact of any particular reference model: it holds across three independent reference models from different families.\n\nWe validate DDR across 8 base-model generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B) and present three core contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{Task formulation and empirical validation}: Generation depth classification beyond binary detection, with a 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-generator LOGO evaluation.\n    \\item \\textbf{DDR characterization}: Drifting features show $|\\rho| > 0.60$ while shape features show $|\\rho| < 0.10$, with a $\\sim$10$\\times$ gap in KS statistics. We identify \\texttt{entropy\\_std} as an intermediate feature (Cohen's $d = 0.458$, TOST rejection rate 0/1000) that challenges a strict binary partition.\n    \\item \\textbf{Negative finding on downstream utility}: Depth-aware data curation is equivalent to random subsampling for downstream CLM quality (TOST confirmed at $\\pm$2\\% margin), establishing depth fingerprinting as diagnostic, not curative.\n\\end{enumerate}\n\nThe signal degrades substantially under instruction tuning (OLMo-Instruct F1 = 0.338 vs.\\ 0.763 base) and high sampling temperature ($t \\geq 0.9$), restricting current scope to base models at moderate temperatures.\nWe report these boundaries transparently as defining constraints rather than limitations to be worked around.\n\n%==============================================================================\n% 2. RELATED WORK\n%==============================================================================\n\\section{Related Work}\n\n\\paragraph{Perplexity-based detection.}\nStatistical detection methods leverage the observation that machine-generated text tends to occupy high-probability regions of the source model's distribution.\nDetectGPT \\cite{mitchell2023detectgpt} uses perturbation-based curvature estimation; Fast-DetectGPT \\cite{bao2024fast} replaces perturbations with conditional probability curvature.\nGLTR \\cite{gehrmann2019gltr} visualizes token-level log-probabilities.\nBinoculars \\cite{hans2024binoculars} compares cross-entropy ratios between two models.\nDNA-GPT \\cite{yang2024dnagpt} uses divergent n-gram analysis.\nThese methods provide binary classification and do not address ordinal depth estimation.\nWhen repurposed as depth predictors, their continuous scores show moderate signal but high cross-generator variance.\n\n\\paragraph{Model collapse and iterative generation.}\nShumailov et al.\\ study model collapse under recursive training on synthetic data, showing progressive loss of distributional tails.\nThe ``LLM as Broken Telephone'' framework (ACL 2025) examines iterative generation chains and bounds paraphrasing chains to $\\sim$3 distinguishable classes under semantic-preservation constraints.\nOur work differs by addressing non-paraphrastic continuation chains where semantic drift is unconstrained.\n\n\\paragraph{Data quality and vocabulary diversity.}\nVocabulary diversity metrics (TTR, hapax legomena ratio) have long been used in stylometry and authorship attribution.\nRecent work connects these metrics to LLM-generated text detection, observing that machine-generated text exhibits reduced lexical diversity.\nOur contribution situates these observations within an ordinal depth framework, showing that diversity reduction is progressive and measurable across generation steps.\n\n\\paragraph{OOD detection and membership inference.}\nOur feature set overlaps with out-of-distribution detection approaches that use reference model statistics.\nWe explicitly acknowledge this connection: the contribution is not the features themselves but (a) the ordinal depth estimation formulation, (b) the empirical DDR characterization showing systematic drifting-vs-stationary behavior, and (c) the downstream utility analysis.\n\n%==============================================================================\n% 3. METHOD\n%==============================================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\nGiven a text passage $x$, we aim to classify its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d=0$ denotes human-written text, $d=1$ denotes first-generation LLM output, and $d=2+$ denotes text produced by two or more recursive generation steps.\nWe construct \\emph{generation chains} by iteratively feeding each generation's output as the prompt for the next, using non-paraphrastic continuation prompts.\n\n\\subsection{Feature Design}\nWe compute 7 features from the token-level NLL distribution obtained by a reference model $M_\\text{ref}$ (Pythia-410M by default).\nFor each text $x = (x_1, \\ldots, x_T)$, we compute $\\ell_t = -\\log p_{M_\\text{ref}}(x_t | x_{&lt;t})$ and derive:\n\n\\paragraph{Drifting features} (central-tendency/diversity):\n\\begin{itemize}\n    \\item \\textbf{entropy\\_mean}: $\\bar{\\ell} = \\frac{1}{T}\\sum_t \\ell_t$\n    \\item \\textbf{TTR}: type-token ratio $|\\text{types}(x)| / T$\n    \\item \\textbf{hapax\\_ratio}: fraction of tokens appearing exactly once\n\\end{itemize}\n\n\\paragraph{Shape features} (near-stationary):\n\\begin{itemize}\n    \\item \\textbf{entropy\\_max}: $\\max_t \\ell_t$\n    \\item \\textbf{tail\\_decay}: exponential decay rate of the upper tail of $\\{\\ell_t\\}$\n\\end{itemize}\n\n\\paragraph{Intermediate features}:\n\\begin{itemize}\n    \\item \\textbf{entropy\\_min}: $\\min_t \\ell_t$ (Spearman $\\rho = -0.30$)\n    \\item \\textbf{entropy\\_std}: $\\text{std}(\\{\\ell_t\\})$ (contested; $\\rho = -0.20$, Cohen's $d = 0.458$)\n\\end{itemize}\n\nWe classify features into a spectrum---drifting ($|\\rho| > 0.50$), intermediate ($0.15 \\leq |\\rho| \\leq 0.50$), and stationary ($|\\rho| < 0.15$)---rather than a binary partition, based on TOST bootstrap validation (\\S\\ref{sec:tost}).\n\n\\subsection{Classifier and Evaluation Protocol}\nWe train an XGBoost classifier on the 7-feature representation.\nTo ensure leak-free evaluation, we use two protocols:\n\n\\paragraph{LOGO (Leave-One-Generator-Out):} Train on chains from all generators except one; test on the held-out generator. Repeat for each generator and average.\n\n\\paragraph{LOFO (Leave-One-Family-Out):} Same as LOGO but holding out an entire model family (e.g., all Pythia models), testing cross-family transfer.\n\nOur \\textbf{primary metric} is \\emph{leak-free binary F1}: the F1 score for distinguishing gen-1 from gen-2+, excluding gen-0 samples to avoid seed-sharing leakage between generators that share the same human-written seeds.\n\n%==============================================================================\n% 4. EXPERIMENTS\n%==============================================================================\n\\section{Experiments}\n\n\\subsection{Feature Ablation and DDR Trend Analysis}\n\\label{sec:ablation}\n\nWe first validate the feature design on MVP data using 5-fold cross-validation.\nTable~\\ref{tab:ablation} shows that the full 7-feature set (macro F1 = 0.820) significantly outperforms both surface-only (TTR + hapax; F1 = 0.763) and reference-only (entropy + tail; F1 = 0.719) subsets (McNemar $p \\approx 0$ for both comparisons).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} & \\textbf{95\\% CI} & \\textbf{$N$} \\\\\n\\midrule\nFull (7-feature) & 0.820 & [0.805, 0.835] & 7 \\\\\nSurface-only & 0.763 & [0.747, 0.774] & 2 \\\\\nReference-only & 0.719 & [0.706, 0.733] & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation under 5-fold CV on MVP data. Surface features (TTR, hapax) and reference features (entropy, tail) provide complementary signal (McNemar $p \\approx 0$).}\n\\label{tab:ablation}\n\\end{table}\n\nTable~\\ref{tab:trend} shows the DDR trend classification.\nDrifting features exhibit strong monotonic relationships with depth ($|\\rho| > 0.60$, KS $> 0.50$), while shape features are near-stationary ($|\\rho| < 0.10$, KS $< 0.06$).\nNotably, \\texttt{entropy\\_std} ($\\rho = -0.20$, KS $= 0.15$, Cohen's $d = 0.458$) falls between groups, motivating the intermediate category.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Feature} & \\textbf{Spearman $\\rho$} & \\textbf{KS} & \\textbf{Class} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & 0.537 & Drifting \\\\\nTTR & $-0.61$ & 0.521 & Drifting \\\\\nentropy\\_mean & $-0.60$ & 0.516 & Drifting \\\\\nentropy\\_min & $-0.30$ & 0.280 & Intermediate \\\\\nentropy\\_std & $-0.20$ & 0.150 & Intermediate \\\\\nentropy\\_max & $+0.05$ & 0.052 & Stationary \\\\\ntail\\_decay & $+0.04$ & 0.043 & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature trend classification across depth. Drifting features show $\\sim$10$\\times$ larger KS statistics than stationary features. \\texttt{entropy\\_std} is classified as intermediate (TOST $d = 0.458$, rejection 0/1000).}\n\\label{tab:trend}\n\\end{table}\n\nPerplexity validation with Pythia-410M confirms monotonic decrease across depth: median perplexity drops from 13.50 (gen-0) through 4.96, 3.00, 2.07, to 1.72 (gen-4).\n\n\\subsection{Cross-Generator Evaluation}\n\\label{sec:cross_gen}\n\nWe expand to 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; $N = 23{,}032$ records) and evaluate under LOGO and LOFO protocols.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{Bin. F1} & \\textbf{Mac. F1} & \\textbf{CI (Bin.)} \\\\\n\\midrule\nPythia-2.8B & 2.8B & 0.724 & 0.851 & [0.710, 0.738] \\\\\nPythia-1B & 1B & 0.718 & 0.831 & [0.703, 0.733] \\\\\nQwen3-1.7B & 1.7B & 0.702 & 0.805 & [0.687, 0.717] \\\\\nOLMo-2-1B & 1.5B & 0.668 & 0.752 & [0.652, 0.684] \\\\\nQwen3-0.6B & 0.6B & 0.659 & 0.780 & [0.643, 0.675] \\\\\n\\midrule\n\\textbf{Average} & — & \\textbf{0.694} & \\textbf{0.804} & [0.688, 0.700] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO per-generator results (5-gen). Binary F1 ranges 0.659--0.724 across generators.}\n\\label{tab:logo}\n\\end{table}\n\nLOFO evaluation yields binary F1 = 0.686 and macro F1 = 0.791, only 0.8 pp below LOGO (Table~\\ref{tab:lofo}), indicating that within-family information leakage is minimal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Protocol} & \\textbf{Binary F1} & \\textbf{Macro F1} \\\\\n\\midrule\nLOGO & 0.694 & 0.804 \\\\\nLOFO & 0.686 & 0.791 \\\\\n$\\Delta$ & $-0.008$ & $-0.013$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO vs.\\ LOFO comparison. The small gap confirms limited family leakage.}\n\\label{tab:lofo}\n\\end{table}\n\n\\subsection{Cross-Reference-Model Validation}\n\nTo confirm that DDR is generation-intrinsic rather than a Pythia-specific artifact, we repeat the analysis with OLMo-2-1B and Qwen3-0.6B as alternative reference models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Ref.\\ Model} & \\textbf{Params} & \\textbf{LOGO F1} & \\textbf{$\\rho_\\text{ent.mean}$} & \\textbf{$\\rho_\\text{tail}$} \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & $-0.60$ & $+0.04$ \\\\\nOLMo-2-1B & 1.5B & 0.807 & $-0.52$ & $+0.06$ \\\\\nQwen3-0.6B & 0.6B & 0.816 & $-0.58$ & $+0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-reference-model validation. DDR trends hold across all reference models, confirming generation-intrinsic origin. Drift magnitude varies (OLMo range [$-0.61$, $-0.91$] vs.\\ Pythia [$-1.19$, $-1.40$]).}\n\\label{tab:cross_ref}\n\\end{table}\n\nAll three reference models produce consistent DDR: entropy drift is universally negative, and tail\\_decay remains near-stationary (Table~\\ref{tab:cross_ref}).\nHowever, \\texttt{entropy\\_std} shows inconsistent classification across references (Cohen's $d$: 0.458 Pythia, 0.310 OLMo, 0.520 Qwen), further supporting its intermediate status.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baseline}\n\nWe compare the 7-feature ensemble against existing detection methods repurposed as ordinal depth predictors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} & \\textbf{Cost} \\\\\n\\midrule\n7-feature XGBoost & 0.798 & [0.786, 0.799] & 1$\\times$ \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 1$\\times$ \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0$\\times$ \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 2$\\times$ \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 2$\\times$ \\\\\n4-det + surface & 0.795 & [0.780, 0.810] & 4$\\times$+ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Baseline comparison (LOGO macro F1). The 7-feature ensemble significantly outperforms all individual detectors (bootstrap $p < 0.001$). The multi-detector ensemble matches performance at $>$2.4$\\times$ inference cost.}\n\\label{tab:baseline}\n\\end{table}\n\nThe 7-feature ensemble significantly outperforms all individual baselines (bootstrap $p < 0.001$; Table~\\ref{tab:baseline}).\nAvg-LogProb is the strongest single detector (0.765) but with much wider confidence intervals, indicating higher cross-generator variance.\nA multi-detector ensemble (4-det + surface features; 0.795) matches the 7-feature set but requires $>$2.4$\\times$ inference cost and 3.2$\\times$ GPU memory.\nThe 7-feature ensemble's advantage lies in efficiency and interpretability rather than absolute performance superiority.\n\n\\subsection{Cross-Model Chains}\n\nReal-world web contamination involves multiple LLM sources.\nWe construct cross-model chains where each depth step uses a different generator from a 5-model pool, evaluating under generator-level LOGO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setup} & \\textbf{Bin. F1} & \\textbf{3-Class F1} & \\textbf{Protocol} \\\\\n\\midrule\nSingle-model (LOGO) & 0.694 & 0.762 & LOGO \\\\\nCross-model (LOGO) & 0.830 & 0.789 & Gen-LOGO \\\\\n$\\Delta$ & $+$0.136 & $+$0.027 & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Single-model vs.\\ cross-model chains. Generator heterogeneity amplifies depth signal by $+$13.6 pp binary F1.}\n\\label{tab:cross_model}\n\\end{table}\n\nCross-model chains yield substantially higher binary F1 (0.830 vs.\\ 0.694; Table~\\ref{tab:cross_model}).\nGenerator heterogeneity amplifies depth-to-depth feature variance, making classification easier.\nThis is practically relevant: real-world multi-source contamination is the condition under which DDR is strongest.\nPer-depth F1 shows gen-0 at 0.95, gen-1 at 0.82, and gen-2+ at 0.78.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\nWe fine-tune OLMo-1B on depth-stratified subsets (3 seeds, bootstrap CIs) to test whether depth-aware curation improves downstream causal language modeling.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{$N$} & \\textbf{PPL} & \\textbf{$\\Delta$ vs.\\ SM} \\\\\n\\midrule\nAll depths & 12,299 & 2.335 & $-$0.032 \\\\\nSize-matched random & 3,951 & 2.367 & — \\\\\nDepth 0+1 only & 3,951 & 2.387 & $+$0.020 \\\\\nBinary-filtered & 3,951 & 2.389 & $+$0.022 \\\\\nDepth 0 only & 797 & 2.681 & $+$0.314 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM perplexity by training data composition. At equal sample count, depth-aware curation does not improve over random subsampling.}\n\\label{tab:downstream}\n\\end{table}\n\nAt equal sample count ($n = 3{,}951$), size-matched random subsampling (PPL = 2.367) outperforms depth 0+1 filtering (2.387) and binary filtering (2.389; Table~\\ref{tab:downstream}).\nTOST equivalence is confirmed at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$).\nSeed variance is extremely small ($< 0.002$ PPL across seeds), indicating the result is robust.\nThis establishes depth fingerprinting as a \\textbf{diagnostic} tool for provenance characterization, not a curative tool for data selection.\n\n\\subsection{9-Generator Scale Evaluation}\n\\label{sec:9gen}\n\nExpanding to 9 generators (adding Gemma-2-2B, Llama-3.2-3B, Qwen3-8B, and Mistral-7B) tests broader generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{3-Cl F1} & \\textbf{Bin F1} & \\textbf{G1 F1} \\\\\n\\midrule\nPythia-1B & 1B & 0.857 & 0.718 & 0.65 \\\\\nQwen3-0.6B & 0.6B & 0.819 & 0.659 & 0.61 \\\\\nPythia-2.8B & 2.8B & 0.812 & 0.724 & 0.68 \\\\\nQwen3-1.7B & 1.7B & 0.811 & 0.702 & 0.66 \\\\\nOLMo-2-1B & 1.5B & 0.773 & 0.668 & 0.58 \\\\\nLlama-3.2-3B & 3B & 0.759 & 0.690 & 0.60 \\\\\nQwen3-8B & 8B & 0.696 & 0.647 & 0.52 \\\\\n\\textbf{Gemma-2-2B} & 2B & \\textbf{0.628} & \\textbf{0.440} & \\textbf{0.036} \\\\\nMistral-7B & 7B & 0.605 & 0.633 & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{9-generator LOGO results. Gemma-2-2B exhibits anomalous gen-1 F1 = 0.036; Mistral-7B and Qwen3-8B show moderate scale-related degradation.}\n\\label{tab:9gen}\n\\end{table}\n\nThe 9-generator LOGO yields 3-class F1 = 0.751 and binary F1 = 0.666 (Table~\\ref{tab:9gen}).\nGemma-2-2B is a notable anomaly: gen-1 F1 = 0.036 indicates the classifier cannot distinguish Gemma's gen-1 output from gen-0.\nThis may reflect Gemma-2's architecture (grouped-query attention, RMSNorm) producing gen-1 distributional features unusually close to the seed text.\nThe method does not guarantee effectiveness across all generator architectures.\nLarger models (Qwen3-8B at 0.647, Mistral-7B at 0.633) show moderate degradation, compressing feature margins as model capacity increases.\n\n%==============================================================================\n% 5. DISCUSSION\n%==============================================================================\n\\section{Discussion}\n\n\\paragraph{Scope: base models only.}\nInstruction-tuned models show substantially degraded depth signal (Table~\\ref{tab:instruct_app}).\nOLMo-2-1B-Instruct drops to LOGO binary F1 = 0.338 (vs.\\ 0.763 base), with 6/7 features exhibiting Spearman $\\rho$ direction reversal.\nLlama-3.2-3B-Instruct is minimally affected ($-$1.1 pp), while Qwen3-1.7B-Instruct shows intermediate degradation ($-$16.3 pp).\nThis heterogeneity means we cannot predict \\textit{a priori} which instruct models will degrade.\nBase models remain relevant for data contamination analysis, as web-scraped synthetic text is predominantly generated by base or API models.\n\n\\paragraph{Temperature sensitivity.}\nDepth signal is reliable within $t \\in [0.5, 0.9)$ but degrades severely at $t = 0.9$ (binary F1 drops to 0.480; see Table~\\ref{tab:temp_app}).\nHigh-temperature sampling inflates entropy uniformly across depths, compressing inter-depth differences.\nCross-temperature transfer is asymmetric: training at $t = 1.0$ and testing at $t = 0.7$ yields F1 = 0.944, but the reverse yields only 0.418.\n\n\\paragraph{The \\texttt{entropy\\_std} question.}\nBootstrap TOST validation (1000 resamples, margin $d = 0.2$) rejects stationarity for three shape features (rejection rate 1000/1000) but \\emph{never} rejects for \\texttt{entropy\\_std} (rate 0/1000, median $d = 0.458$; Table~\\ref{tab:tost_app}).\nCross-reference analysis shows $d$ ranging from 0.310 (OLMo) to 0.520 (Qwen), further demonstrating inconsistency.\nWe adopt a spectrum model: drifting ($|\\rho| > 0.50$) $\\to$ intermediate (0.15--0.50) $\\to$ stationary ($< 0.15$), with \\texttt{entropy\\_std} and \\texttt{entropy\\_min} in the intermediate category.\n\n\\paragraph{Handcrafted vs.\\ end-to-end.}\nQLoRA fine-tuned classifiers substantially outperform the 7-feature ensemble (Table~\\ref{tab:qlora_app}): Qwen3-1.7B-Instruct achieves 3-class F1 = 0.907 and binary F1 = 0.867, a $+$14.5 pp improvement.\nThis confirms that depth signal is richer than what 7 features capture.\nWe position the 7-feature ensemble on \\emph{interpretability and efficiency}: it requires only a 410M reference model and XGBoost ($\\sim$150$\\times$ less inference cost), and its features enable the DDR analysis that constitutes our primary conceptual contribution.\n\n\\paragraph{Semantic convergence vs.\\ distributional divergence.}\nTopic drift analysis reveals a counter-intuitive pattern: deeper generations converge in semantic space (cosine similarity increases from 0.622 at gen-0$\\to$gen-1 to 0.859 at gen-3$\\to$gen-4) while distributional features diverge.\nDDR is a distributional phenomenon, not a semantic one.\n\n%==============================================================================\n% 6. CONCLUSION\n%==============================================================================\n\\section{Conclusion}\n\nWe formulate generation depth classification for non-paraphrastic LLM generation chains and characterize differential depth response across 8 base-model generators from 5 families.\nA lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (per-generator range 0.633--0.724) under LOGO evaluation, and 0.830 on cross-model chains, using a single 410M reference model.\nDDR is generation-intrinsic: it persists across reference models and is driven by drifting central-tendency features ($|\\rho| > 0.60$) while shape features remain stationary ($|\\rho| < 0.10$).\nDepth-aware data curation does not improve downstream CLM quality over random subsampling, establishing depth fingerprinting as diagnostic rather than curative.\n\nCurrent limitations include restriction to base models (instruct tuning degrades or reverses DDR), temperature sensitivity ($t \\geq 0.9$), a 3-class resolution ceiling, and architecture-specific failures (Gemma-2-2B gen-1 F1 = 0.036).\nExtending to instruct models and larger generators ($>$8B) remains future work.\n\n%==============================================================================\n% LIMITATIONS\n%==============================================================================\n\\section*{Limitations}\n\n\\begin{enumerate}\n    \\item \\textbf{Base models only.} The method does not reliably apply to instruction-tuned models, which represent a large fraction of deployed LLMs.\n    \\item \\textbf{Temperature range.} Reliable only for $t \\in [0.5, 0.9)$; most API defaults use $t = 1.0$.\n    \\item \\textbf{Scale.} Larger generators ($>$3B) show moderate signal degradation; 70B+ models are untested.\n    \\item \\textbf{Architecture sensitivity.} Gemma-2-2B represents a failure case; we cannot predict which architectures will fail.\n    \\item \\textbf{Downstream evidence.} The negative finding is based on 3 seeds and a single perplexity metric, though seed variance is extremely small ($<$0.002).\n    \\item \\textbf{Prompt-type dependence.} Performance varies across continuation, elaboration, and rewriting prompts (5 pp range).\n    \\item \\textbf{Paraphrastic chains.} The method does not apply to paraphrastic chains (binary F1 = 0.55 vs.\\ 0.694 for continuation).\n\\end{enumerate}\n\n%==============================================================================\n% REFERENCES\n%==============================================================================\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{20}\n\n\\bibitem[Mitchell et al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D.\\ Manning, and Chelsea Finn. 2023.\n\\newblock {DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Bao et al.(2024)]{bao2024fast}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang. 2024.\n\\newblock Fast-{DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Gehrmann et al.(2019)]{gehrmann2019gltr}\nSebastian Gehrmann, Hendrik Strobelt, and Alexander Rush. 2019.\n\\newblock {GLTR}: Statistical Detection and Visualization of Generated Text.\n\\newblock In \\emph{Proceedings of ACL: System Demonstrations}.\n\n\\bibitem[Hans et al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein. 2024.\n\\newblock Spotting {LLMs} With Binoculars: Zero-Shot Detection of Machine-Generated Text.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Yang et al.(2024)]{yang2024dnagpt}\nXianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen. 2024.\n\\newblock {DNA-GPT}: Divergent N-Gram Analysis for Training-Free Detection of {GPT}-Generated Text.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\end{thebibliography}\n\n%==============================================================================\n% APPENDIX\n%==============================================================================\n\\clearpage\n\\appendix\n\n\\section{Prompt Type Comparison}\n\\label{app:prompt}\n\nThree prompt types---continuation, elaboration, and inspired rewriting---exhibit different DDR strengths (Table~\\ref{tab:prompt}).\nContinuation shows the strongest depth signal (CV F1 = 0.781), consistent with its largest semantic divergence per step.\nCross-prompt-type transfer (LOPTO) averages F1 = 0.753.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt} & \\textbf{CV F1} & \\textbf{LOPTO F1} & \\textbf{Ret.} & \\textbf{$\\rho_\\text{hapax}$} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.74$ \\\\\nRewriting & 0.737 & 0.733 & 0.939 & $-0.80$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.83$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt type comparison. Higher semantic divergence (lower retention) correlates with stronger depth signal. LOPTO: leave-one-prompt-type-out.}\n\\label{tab:prompt}\n\\end{table}\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{app:para}\n\nParaphrastic chains show severely weakened depth signal (Table~\\ref{tab:para}), confirming the method's scope boundary.\nParaphrasing preserves semantics (retention = 0.97), compressing distributional variation across depths.\nBinary F1 drops to 0.55, near chance.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{CV F1} & \\textbf{Bin. F1} & \\textbf{$\\rho_\\text{hapax}$} & \\textbf{Ret.} \\\\\n\\midrule\nContinuation & 0.781 & 0.694 & $-0.74$ & 0.831 \\\\\nParaphrastic & 0.620 & 0.550 & $-0.35$ & 0.970 \\\\\n$\\Delta$ & $-0.161$ & $-0.144$ & $+0.39$ & $+0.139$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs.\\ continuation chains. Semantic preservation compresses depth signal.}\n\\label{tab:para}\n\\end{table}\n\n\\section{Multi-Domain Analysis}\n\\label{app:domain}\n\nDDR trends are preserved across four domains (Table~\\ref{tab:domain}), though classification performance is domain-dependent.\nAcademic text shows the weakest signal (0.628), likely due to inherently low vocabulary diversity in specialized scientific writing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{95\\% CI} & \\textbf{$\\rho_\\text{hapax}$} \\\\\n\\midrule\nNews & 0.712 & [0.690, 0.733] & $-0.65$ \\\\\nWikipedia & 0.695 & [0.675, 0.715] & $-0.63$ \\\\\nCode & 0.687 & [0.664, 0.710] & $-0.58$ \\\\\nAcademic & 0.628 & [0.603, 0.652] & $-0.52$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-domain binary F1. Cross-domain transfer F1 = 0.650.}\n\\label{tab:domain}\n\\end{table}\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{app:ordinal}\n\n5-class ordinal classification drops to F1 = 0.50 (Table~\\ref{tab:ordinal}).\nOrdinal methods (CORAL, Frank-Hall) provide no improvement, confirming the bottleneck is in feature signal, not model structure.\nGen-2 and gen-3 concentrate 65\\% of confusion errors.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccl}\n\\toprule\n\\textbf{$K$} & \\textbf{Method} & \\textbf{F1} & \\textbf{G0 F1} & \\textbf{G2+ F1} \\\\\n\\midrule\n3 & XGBoost & 0.762 & 0.95 & 0.66 \\\\\n5 & XGBoost & 0.500 & 0.92 & .35/.30/.38 \\\\\n5 & CORAL & 0.500 & 0.91 & .34/.31/.38 \\\\\n5 & Frank-Hall & 0.490 & 0.90 & .33/.30/.37 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{3-class vs.\\ 5-class classification. 3-class is the practical resolution ceiling.}\n\\label{tab:ordinal}\n\\end{table}\n\n\\section{Robustness to Human Editing}\n\\label{app:edit}\n\nThe method shows graceful degradation under simulated human editing (Table~\\ref{tab:edit}).\nAt 5\\% random word replacement, binary F1 drops 4.6 pp; LLM rephrasing ($\\sim$50\\% edit distance) causes a comparable 4.5 pp drop.\nHeavy editing ($>$20\\%) substantially degrades signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Edit Type} & \\textbf{Rate} & \\textbf{Bin. F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nNone & 0\\% & 0.695 & — \\\\\nRandom & 5\\% & 0.650 & $-0.046$ \\\\\nRandom & 10\\% & 0.614 & $-0.081$ \\\\\nRandom & 20\\% & 0.591 & $-0.104$ \\\\\nLLM rephrase & $\\sim$50\\% ed. & 0.647 & $-0.045$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Robustness to simulated human editing.}\n\\label{tab:edit}\n\\end{table}\n\n\\section{LD-Score Feature Addition}\n\\label{app:ld}\n\nAdding LD-Score (character-level distribution signature) as an 8th feature yields marginal improvement ($+$0.7 pp macro F1, McNemar $p = 0.12$; Table~\\ref{tab:ld}).\nLD-Score correlates highly with hapax\\_ratio ($r = 0.68$), confirming character-level and token-level vocabulary diversity are largely redundant.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{$N$} & \\textbf{Macro F1} & \\textbf{McNemar $p$} \\\\\n\\midrule\n7-feature & 7 & 0.804 & — \\\\\n+ LD-Score & 8 & 0.811 & 0.12 \\\\\nLD-Score only & 1 & 0.721 & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LD-Score feature addition. Marginal contribution is not significant.}\n\\label{tab:ld}\n\\end{table}\n\n\\section{End-to-End QLoRA Classification}\n\\label{app:qlora}\n\nQLoRA fine-tuned classifiers substantially outperform the 7-feature ensemble (Table~\\ref{tab:qlora_app}), confirming depth signal is richer than captured by 7 features.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-Cl F1} & \\textbf{Bin F1} & \\textbf{5-Cl F1} & \\textbf{Cost} \\\\\n\\midrule\n7-feat XGBoost & 0.762 & 0.694 & 0.500 & 1$\\times$ \\\\\nQLoRA OLMo-1B-Inst & 0.889 & 0.836 & 0.598 & $\\sim$150$\\times$ \\\\\nQLoRA Qwen3-1.7B-Inst & 0.907 & 0.867 & 0.551 & $\\sim$250$\\times$ \\\\\nQLoRA OLMo-1B-Base & 0.859 & 0.793 & 0.540 & $\\sim$150$\\times$ \\\\\nQLoRA Qwen3-1.7B-Base & 0.904 & 0.860 & 0.554 & $\\sim$250$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Handcrafted vs.\\ end-to-end classification. QLoRA achieves $+$12--15 pp improvement at $\\sim$150--250$\\times$ inference cost.}\n\\label{tab:qlora_app}\n\\end{table}\n\n\\section{Text Length Control}\n\\label{app:length}\n\nLength-depth correlation is weak ($|\\rho| < 0.14$; Table~\\ref{tab:length}).\nLength-matched subsampling reduces binary F1 by 4.6 pp, but a random-subsample control (same $N$) also drops 3.0 pp, attributing only 1.6 pp to the length confound.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Bin. F1} & \\textbf{$\\Delta$} & \\textbf{Note} \\\\\n\\midrule\nFull (unmatched) & 0.770 & — & Full dataset \\\\\nLength-matched & 0.724 & $-0.046$ & Equalized \\\\\nRandom subsample & 0.740 & $-0.030$ & Size control \\\\\n$\\Delta$ (length) & — & $-0.016$ & Attributable \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Only 1.6 pp of the 4.6 pp drop is attributable to length.}\n\\label{tab:length}\n\\end{table}\n\n\\section{Large-Scale Generator}\n\\label{app:scale}\n\nAdding Qwen3-8B-Base (8B parameters) confirms moderate scale degradation (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{LOGO Bin F1} & \\textbf{$\\rho_\\text{hapax}$} & \\textbf{$\\rho_\\text{ent.m}$} \\\\\n\\midrule\nPythia-1B & 1B & 0.718 & $-0.65$ & $-0.64$ \\\\\nQwen3-0.6B & 0.6B & 0.659 & $-0.60$ & $-0.58$ \\\\\nPythia-2.8B & 2.8B & 0.724 & $-0.63$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.702 & $-0.61$ & $-0.57$ \\\\\nOLMo-2-1B & 1.5B & 0.668 & $-0.57$ & $-0.52$ \\\\\nQwen3-8B & 8B & 0.683 & $-0.56$ & $-0.48$ \\\\\n\\midrule\n\\textbf{6-gen avg} & — & \\textbf{0.692} & $-0.60$ & $-0.57$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{6-generator LOGO including Qwen3-8B. Scale degradation is moderate ($-$1.1 pp average).}\n\\label{tab:scale}\n\\end{table}\n\n\\section{DDR Causality Analysis}\n\\label{app:causality}\n\nThree independent methods confirm drifting features carry $\\sim$5$\\times$ more predictive signal than stationary features (Table~\\ref{tab:causality}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Drifting} & \\textbf{Stationary} & \\textbf{Ratio} \\\\\n\\midrule\nPerm.\\ importance & 0.158 & 0.030 & 5.3$\\times$ \\\\\nGranger causality & 6/7 sig & — & — \\\\\nFeature intervention & 0.020 & 0.006 & 3.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DDR causality evidence. Drifting features dominate across all methods.}\n\\label{tab:causality}\n\\end{table}\n\n\\section{TOST Bootstrap Stability}\n\\label{sec:tost}\n\nBootstrap TOST (1000 resamples, $d = 0.2$ margin) validates stationarity for entropy\\_max, entropy\\_min, and tail\\_decay (Table~\\ref{tab:tost_app}) but rejects it for \\texttt{entropy\\_std} (rate 0/1000, median $d = 0.458$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Med.\\ $d$} & \\textbf{95\\% CI} & \\textbf{Rej.\\ Rate} & \\textbf{Class} \\\\\n\\midrule\nentropy\\_max & 0.062 & [0.037, 0.088] & 1000/1000 & Stationary \\\\\nentropy\\_min & $-0.016$ & [$-0.042$, 0.011] & 1000/1000 & Stationary \\\\\ntail\\_decay & 0.088 & [0.065, 0.111] & 1000/1000 & Stationary \\\\\n\\textbf{entropy\\_std} & \\textbf{0.458} & \\textbf{[0.435, 0.479]} & \\textbf{0/1000} & \\textbf{Intermediate} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST bootstrap stability. \\texttt{entropy\\_std} fails stationarity at $d = 0.2$ margin.}\n\\label{tab:tost_app}\n\\end{table}\n\n\\section{Instruct Model Evaluation}\n\\label{app:instruct}\n\nInstruction tuning substantially degrades depth signal, with heterogeneous effects across models (Table~\\ref{tab:instruct_app}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Base F1} & \\textbf{Inst F1} & \\textbf{$\\Delta$} & \\textbf{Feat Rev.} \\\\\n\\midrule\nOLMo-2-1B & 0.763 & 0.338 & $-0.425$ & 6/7 \\\\\nQwen3-1.7B & 0.821 & 0.658 & $-0.163$ & partial \\\\\nLlama-3.2-3B & 0.849 & 0.838 & $-0.011$ & 3/7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instruct vs.\\ base model depth signal. OLMo-Instruct shows near-complete degradation with feature direction reversal.}\n\\label{tab:instruct_app}\n\\end{table}\n\n\\section{Temperature Sensitivity}\n\\label{app:temp}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$t$} & \\textbf{Within-CV Bin F1} & \\textbf{$\\rho_\\text{ent.m}$} & \\textbf{Reliable} \\\\\n\\midrule\n0.5 & 0.813 & $-0.58$ & Yes \\\\\n0.7 & 0.694 & $-0.60$ & Yes \\\\\n0.9 & 0.480 & $-0.30$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temperature sensitivity. Signal degrades severely at $t \\geq 0.9$.}\n\\label{tab:temp_app}\n\\end{table}\n\nCross-temperature transfer (Qwen3-1.7B): training at $t = 0.7$, testing at $t = 1.0$ yields binary F1 = 0.418 ($-$37.1 pp vs.\\ within-temperature). The reverse direction ($t = 1.0 \\to 0.7$) yields 0.944 ($+$15.5 pp), demonstrating asymmetric transfer.\n\n\\section{Independent Seed Validation}\n\\label{app:seed_val}\n\nIndependent seed sets confirm shared-seed LOGO does not suffer seed leakage (Table~\\ref{tab:seed_val}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Setup} & \\textbf{Binary F1} & \\textbf{Seeds Shared} \\\\\n\\midrule\nShared-seed LOGO & 0.694 & Yes \\\\\nIndependent: Pythia$\\to$OLMo & 0.695 & No \\\\\nIndependent: OLMo$\\to$Pythia & 0.666 & No \\\\\nIndependent avg & 0.680 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed leakage validation. $\\Delta = -0.014$, within noise.}\n\\label{tab:seed_val}\n\\end{table}\n\n\\section{Seed Complexity Stratification}\n\\label{app:seed_complex}\n\nDepth signal is independent of seed text complexity (Table~\\ref{tab:seed_complex}; max difference 1.06 pp).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Complexity} & \\textbf{Bin F1} & \\textbf{Multi F1} & \\textbf{$N$} \\\\\n\\midrule\nLow & 0.685 & 0.772 & $\\sim$332 \\\\\nMedium & 0.695 & 0.778 & $\\sim$332 \\\\\nHigh & 0.695 & 0.779 & $\\sim$331 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed complexity stratification. Depth signal is seed-independent.}\n\\label{tab:seed_complex}\n\\end{table}\n\n\\section{Topic Drift Correlation}\n\\label{app:topic}\n\nSemantic similarity increases with depth (Table~\\ref{tab:topic}), while distributional features diverge---confirming DDR is distributional, not semantic.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Transition} & \\textbf{Mean Cosine Sim} & \\textbf{Std} \\\\\n\\midrule\ngen-0 $\\to$ gen-1 & 0.622 & 0.165 \\\\\ngen-1 $\\to$ gen-2 & 0.683 & 0.184 \\\\\ngen-2 $\\to$ gen-3 & 0.801 & 0.201 \\\\\ngen-3 $\\to$ gen-4 & 0.859 & 0.190 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Semantic similarity by depth transition. Deeper generations converge semantically while diverging distributionally.}\n\\label{tab:topic}\n\\end{table}\n\n\\section{TOST Equivalence Tests (Downstream)}\n\\label{app:tost_downstream}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Margin} & \\textbf{$p$} & \\textbf{Equiv.} \\\\\n\\midrule\nSM vs.\\ depth01 & $\\pm$2\\% & $1.1 \\times 10^{-4}$ & Yes \\\\\nSM vs.\\ binary-filt. & $\\pm$2\\% & $8.3 \\times 10^{-5}$ & Yes \\\\\nAll vs.\\ SM & $\\pm$2\\% & 0.15 & No \\\\\nAll vs.\\ SM & $\\pm$3\\% & 0.003 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST equivalence tests for downstream CLM quality. SM = size-matched random.}\n\\label{tab:tost_downstream}\n\\end{table}\n\n\\section{\\texttt{entropy\\_std} Cross-Reference Inconsistency}\n\\label{app:entropy_std}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Ref.\\ Model} & \\textbf{$d$} & \\textbf{TOST Rej.} & \\textbf{Class} \\\\\n\\midrule\nPythia-410M & 0.458 & 0/1000 & Contested \\\\\nOLMo-2-1B & 0.310 & partial & Borderline \\\\\nQwen3-0.6B & 0.520 & 0/1000 & Contested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\texttt{entropy\\_std} Cohen's $d$ across reference models.}\n\\label{tab:entropy_std_cross}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1603476-8fb8-4144-9a8f-aac3f8e077ab",
  "isSidechain": false,
  "requestId": "req_011CbDfog3W4PXnHTGoHXjqQ",
  "type": "assistant",
  "uuid": "9606e5d9-d67a-459b-a92c-741c6da0ee94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4Dg7vvjAZ3YMjrKavcLnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 57615,
      "output_tokens": 15322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15322,
          "cache_read_input_tokens": 57615,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 900
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

_source line 19 · 2026-05-20T10:37:58.350Z_

<details><summary>↩ Tool result · `toolu_01RLjRjYa96Z2SP8qxq37VVo`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9606e5d9-d67a-459b-a92c-741c6da0ee94",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "df3a5f74-be58-4746-b991-480cbcc06793",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\title{Differential Depth Response in Non-Paraphrastic LLM Generation Chains: \\\\\nAn Empirical Characterization Across Model Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n% ABSTRACT\n%==============================================================================\n\\begin{abstract}\nWeb-scraped corpora increasingly contain LLM-generated text of unknown provenance depth---the number of recursive generation steps from the original human-written source.\nCurrent detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material.\nWe formulate \\emph{generation depth classification} (gen-0/gen-1/gen-2+) for non-paraphrastic continuation chains and characterize a phenomenon we term \\emph{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while shape features (entropy max, tail decay) remain near-stationary ($|\\rho| < 0.10$).\nAcross 8 base-model generators from 5 families (0.6B--8B), a lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under leave-one-generator-out (LOGO) evaluation, and 0.830 on cross-model chains using a single 410M reference model.\nPer-generator binary F1 ranges from 0.633 to 0.724.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language modeling quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm$2\\% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization rather than a curative tool for data selection.\nThe signal degrades substantially under instruction tuning and high temperature ($t \\geq 0.9$), restricting current scope to base models.\nWe also identify \\texttt{entropy\\_std} as an intermediate feature whose classification is inconsistent across reference models, motivating a spectrum model (drifting $\\to$ intermediate $\\to$ stationary) over the original binary partition.\n\\end{abstract}\n\n%==============================================================================\n% 1. INTRODUCTION\n%==============================================================================\n\\section{Introduction}\n\nWeb-scraped training data increasingly contains LLM-generated text of unknown provenance: recent estimates suggest 7--17\\% of scientific papers may contain AI-generated content.\nThis recursive contamination creates \\emph{generation chains} where output from one model becomes input to another, potentially degrading data quality across training iterations.\nCurrent detection methods treat text classification as a binary problem---human-written vs.\\ machine-generated---conflating gen-1 text (which retains much of the source distribution's lexical properties) with deeper generations that exhibit measurably reduced vocabulary diversity and compressed perplexity.\n\nThis binary framing is insufficient for data governance.\nA dataset curator deciding whether to include questionable text needs to know not just \\emph{whether} it was machine-generated, but \\emph{how far removed} it is from the original human source.\nWe formulate \\textbf{generation depth classification} as an ordinal prediction task: given a text passage, determine whether it is gen-0 (human-written), gen-1 (first-generation synthetic), or gen-2+ (recursively generated).\n\nOur central empirical finding is \\textbf{differential depth response (DDR)}: distributional features computed from a reference model's token-level negative log-likelihood (NLL) distribution exhibit systematically different behavior across generation depths.\nCentral-tendency and diversity features---entropy mean, type-token ratio (TTR), and hapax ratio---drift monotonically with depth, consistent with recursive generation inducing a location shift in the NLL distribution.\nShape features---entropy max and tail decay---remain approximately stationary, preserving distributional shape even as the center shifts.\nThis differential response is not an artifact of any particular reference model: it holds across three independent reference models from different families.\n\nWe validate DDR across 8 base-model generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B) and present three core contributions:\n\n\\begin{enumerate}\n    \\item \\textbf{Task formulation and empirical validation}: Generation depth classification beyond binary detection, with a 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-generator LOGO evaluation.\n    \\item \\textbf{DDR characterization}: Drifting features show $|\\rho| > 0.60$ while shape features show $|\\rho| < 0.10$, with a $\\sim$10$\\times$ gap in KS statistics. We identify \\texttt{entropy\\_std} as an intermediate feature (Cohen's $d = 0.458$, TOST rejection rate 0/1000) that challenges a strict binary partition.\n    \\item \\textbf{Negative finding on downstream utility}: Depth-aware data curation is equivalent to random subsampling for downstream CLM quality (TOST confirmed at $\\pm$2\\% margin), establishing depth fingerprinting as diagnostic, not curative.\n\\end{enumerate}\n\nThe signal degrades substantially under instruction tuning (OLMo-Instruct F1 = 0.338 vs.\\ 0.763 base) and high sampling temperature ($t \\geq 0.9$), restricting current scope to base models at moderate temperatures.\nWe report these boundaries transparently as defining constraints rather than limitations to be worked around.\n\n%==============================================================================\n% 2. RELATED WORK\n%==============================================================================\n\\section{Related Work}\n\n\\paragraph{Perplexity-based detection.}\nStatistical detection methods leverage the observation that machine-generated text tends to occupy high-probability regions of the source model's distribution.\nDetectGPT \\cite{mitchell2023detectgpt} uses perturbation-based curvature estimation; Fast-DetectGPT \\cite{bao2024fast} replaces perturbations with conditional probability curvature.\nGLTR \\cite{gehrmann2019gltr} visualizes token-level log-probabilities.\nBinoculars \\cite{hans2024binoculars} compares cross-entropy ratios between two models.\nDNA-GPT \\cite{yang2024dnagpt} uses divergent n-gram analysis.\nThese methods provide binary classification and do not address ordinal depth estimation.\nWhen repurposed as depth predictors, their continuous scores show moderate signal but high cross-generator variance.\n\n\\paragraph{Model collapse and iterative generation.}\nShumailov et al.\\ study model collapse under recursive training on synthetic data, showing progressive loss of distributional tails.\nThe ``LLM as Broken Telephone'' framework (ACL 2025) examines iterative generation chains and bounds paraphrasing chains to $\\sim$3 distinguishable classes under semantic-preservation constraints.\nOur work differs by addressing non-paraphrastic continuation chains where semantic drift is unconstrained.\n\n\\paragraph{Data quality and vocabulary diversity.}\nVocabulary diversity metrics (TTR, hapax legomena ratio) have long been used in stylometry and authorship attribution.\nRecent work connects these metrics to LLM-generated text detection, observing that machine-generated text exhibits reduced lexical diversity.\nOur contribution situates these observations within an ordinal depth framework, showing that diversity reduction is progressive and measurable across generation steps.\n\n\\paragraph{OOD detection and membership inference.}\nOur feature set overlaps with out-of-distribution detection approaches that use reference model statistics.\nWe explicitly acknowledge this connection: the contribution is not the features themselves but (a) the ordinal depth estimation formulation, (b) the empirical DDR characterization showing systematic drifting-vs-stationary behavior, and (c) the downstream utility analysis.\n\n%==============================================================================\n% 3. METHOD\n%==============================================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\nGiven a text passage $x$, we aim to classify its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d=0$ denotes human-written text, $d=1$ denotes first-generation LLM output, and $d=2+$ denotes text produced by two or more recursive generation steps.\nWe construct \\emph{generation chains} by iteratively feeding each generation's output as the prompt for the next, using non-paraphrastic continuation prompts.\n\n\\subsection{Feature Design}\nWe compute 7 features from the token-level NLL distribution obtained by a reference model $M_\\text{ref}$ (Pythia-410M by default).\nFor each text $x = (x_1, \\ldots, x_T)$, we compute $\\ell_t = -\\log p_{M_\\text{ref}}(x_t | x_{&lt;t})$ and derive:\n\n\\paragraph{Drifting features} (central-tendency/diversity):\n\\begin{itemize}\n    \\item \\textbf{entropy\\_mean}: $\\bar{\\ell} = \\frac{1}{T}\\sum_t \\ell_t$\n    \\item \\textbf{TTR}: type-token ratio $|\\text{types}(x)| / T$\n    \\item \\textbf{hapax\\_ratio}: fraction of tokens appearing exactly once\n\\end{itemize}\n\n\\paragraph{Shape features} (near-stationary):\n\\begin{itemize}\n    \\item \\textbf{entropy\\_max}: $\\max_t \\ell_t$\n    \\item \\textbf{tail\\_decay}: exponential decay rate of the upper tail of $\\{\\ell_t\\}$\n\\end{itemize}\n\n\\paragraph{Intermediate features}:\n\\begin{itemize}\n    \\item \\textbf{entropy\\_min}: $\\min_t \\ell_t$ (Spearman $\\rho = -0.30$)\n    \\item \\textbf{entropy\\_std}: $\\text{std}(\\{\\ell_t\\})$ (contested; $\\rho = -0.20$, Cohen's $d = 0.458$)\n\\end{itemize}\n\nWe classify features into a spectrum---drifting ($|\\rho| > 0.50$), intermediate ($0.15 \\leq |\\rho| \\leq 0.50$), and stationary ($|\\rho| < 0.15$)---rather than a binary partition, based on TOST bootstrap validation (\\S\\ref{sec:tost}).\n\n\\subsection{Classifier and Evaluation Protocol}\nWe train an XGBoost classifier on the 7-feature representation.\nTo ensure leak-free evaluation, we use two protocols:\n\n\\paragraph{LOGO (Leave-One-Generator-Out):} Train on chains from all generators except one; test on the held-out generator. Repeat for each generator and average.\n\n\\paragraph{LOFO (Leave-One-Family-Out):} Same as LOGO but holding out an entire model family (e.g., all Pythia models), testing cross-family transfer.\n\nOur \\textbf{primary metric} is \\emph{leak-free binary F1}: the F1 score for distinguishing gen-1 from gen-2+, excluding gen-0 samples to avoid seed-sharing leakage between generators that share the same human-written seeds.\n\n%==============================================================================\n% 4. EXPERIMENTS\n%==============================================================================\n\\section{Experiments}\n\n\\subsection{Feature Ablation and DDR Trend Analysis}\n\\label{sec:ablation}\n\nWe first validate the feature design on MVP data using 5-fold cross-validation.\nTable~\\ref{tab:ablation} shows that the full 7-feature set (macro F1 = 0.820) significantly outperforms both surface-only (TTR + hapax; F1 = 0.763) and reference-only (entropy + tail; F1 = 0.719) subsets (McNemar $p \\approx 0$ for both comparisons).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} & \\textbf{95\\% CI} & \\textbf{$N$} \\\\\n\\midrule\nFull (7-feature) & 0.820 & [0.805, 0.835] & 7 \\\\\nSurface-only & 0.763 & [0.747, 0.774] & 2 \\\\\nReference-only & 0.719 & [0.706, 0.733] & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation under 5-fold CV on MVP data. Surface features (TTR, hapax) and reference features (entropy, tail) provide complementary signal (McNemar $p \\approx 0$).}\n\\label{tab:ablation}\n\\end{table}\n\nTable~\\ref{tab:trend} shows the DDR trend classification.\nDrifting features exhibit strong monotonic relationships with depth ($|\\rho| > 0.60$, KS $> 0.50$), while shape features are near-stationary ($|\\rho| < 0.10$, KS $< 0.06$).\nNotably, \\texttt{entropy\\_std} ($\\rho = -0.20$, KS $= 0.15$, Cohen's $d = 0.458$) falls between groups, motivating the intermediate category.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Feature} & \\textbf{Spearman $\\rho$} & \\textbf{KS} & \\textbf{Class} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & 0.537 & Drifting \\\\\nTTR & $-0.61$ & 0.521 & Drifting \\\\\nentropy\\_mean & $-0.60$ & 0.516 & Drifting \\\\\nentropy\\_min & $-0.30$ & 0.280 & Intermediate \\\\\nentropy\\_std & $-0.20$ & 0.150 & Intermediate \\\\\nentropy\\_max & $+0.05$ & 0.052 & Stationary \\\\\ntail\\_decay & $+0.04$ & 0.043 & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature trend classification across depth. Drifting features show $\\sim$10$\\times$ larger KS statistics than stationary features. \\texttt{entropy\\_std} is classified as intermediate (TOST $d = 0.458$, rejection 0/1000).}\n\\label{tab:trend}\n\\end{table}\n\nPerplexity validation with Pythia-410M confirms monotonic decrease across depth: median perplexity drops from 13.50 (gen-0) through 4.96, 3.00, 2.07, to 1.72 (gen-4).\n\n\\subsection{Cross-Generator Evaluation}\n\\label{sec:cross_gen}\n\nWe expand to 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; $N = 23{,}032$ records) and evaluate under LOGO and LOFO protocols.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{Bin. F1} & \\textbf{Mac. F1} & \\textbf{CI (Bin.)} \\\\\n\\midrule\nPythia-2.8B & 2.8B & 0.724 & 0.851 & [0.710, 0.738] \\\\\nPythia-1B & 1B & 0.718 & 0.831 & [0.703, 0.733] \\\\\nQwen3-1.7B & 1.7B & 0.702 & 0.805 & [0.687, 0.717] \\\\\nOLMo-2-1B & 1.5B & 0.668 & 0.752 & [0.652, 0.684] \\\\\nQwen3-0.6B & 0.6B & 0.659 & 0.780 & [0.643, 0.675] \\\\\n\\midrule\n\\textbf{Average} & — & \\textbf{0.694} & \\textbf{0.804} & [0.688, 0.700] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO per-generator results (5-gen). Binary F1 ranges 0.659--0.724 across generators.}\n\\label{tab:logo}\n\\end{table}\n\nLOFO evaluation yields binary F1 = 0.686 and macro F1 = 0.791, only 0.8 pp below LOGO (Table~\\ref{tab:lofo}), indicating that within-family information leakage is minimal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Protocol} & \\textbf{Binary F1} & \\textbf{Macro F1} \\\\\n\\midrule\nLOGO & 0.694 & 0.804 \\\\\nLOFO & 0.686 & 0.791 \\\\\n$\\Delta$ & $-0.008$ & $-0.013$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO vs.\\ LOFO comparison. The small gap confirms limited family leakage.}\n\\label{tab:lofo}\n\\end{table}\n\n\\subsection{Cross-Reference-Model Validation}\n\nTo confirm that DDR is generation-intrinsic rather than a Pythia-specific artifact, we repeat the analysis with OLMo-2-1B and Qwen3-0.6B as alternative reference models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Ref.\\ Model} & \\textbf{Params} & \\textbf{LOGO F1} & \\textbf{$\\rho_\\text{ent.mean}$} & \\textbf{$\\rho_\\text{tail}$} \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & $-0.60$ & $+0.04$ \\\\\nOLMo-2-1B & 1.5B & 0.807 & $-0.52$ & $+0.06$ \\\\\nQwen3-0.6B & 0.6B & 0.816 & $-0.58$ & $+0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-reference-model validation. DDR trends hold across all reference models, confirming generation-intrinsic origin. Drift magnitude varies (OLMo range [$-0.61$, $-0.91$] vs.\\ Pythia [$-1.19$, $-1.40$]).}\n\\label{tab:cross_ref}\n\\end{table}\n\nAll three reference models produce consistent DDR: entropy drift is universally negative, and tail\\_decay remains near-stationary (Table~\\ref{tab:cross_ref}).\nHowever, \\texttt{entropy\\_std} shows inconsistent classification across references (Cohen's $d$: 0.458 Pythia, 0.310 OLMo, 0.520 Qwen), further supporting its intermediate status.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baseline}\n\nWe compare the 7-feature ensemble against existing detection methods repurposed as ordinal depth predictors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} & \\textbf{Cost} \\\\\n\\midrule\n7-feature XGBoost & 0.798 & [0.786, 0.799] & 1$\\times$ \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 1$\\times$ \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0$\\times$ \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 2$\\times$ \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 2$\\times$ \\\\\n4-det + surface & 0.795 & [0.780, 0.810] & 4$\\times$+ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Baseline comparison (LOGO macro F1). The 7-feature ensemble significantly outperforms all individual detectors (bootstrap $p < 0.001$). The multi-detector ensemble matches performance at $>$2.4$\\times$ inference cost.}\n\\label{tab:baseline}\n\\end{table}\n\nThe 7-feature ensemble significantly outperforms all individual baselines (bootstrap $p < 0.001$; Table~\\ref{tab:baseline}).\nAvg-LogProb is the strongest single detector (0.765) but with much wider confidence intervals, indicating higher cross-generator variance.\nA multi-detector ensemble (4-det + surface features; 0.795) matches the 7-feature set but requires $>$2.4$\\times$ inference cost and 3.2$\\times$ GPU memory.\nThe 7-feature ensemble's advantage lies in efficiency and interpretability rather than absolute performance superiority.\n\n\\subsection{Cross-Model Chains}\n\nReal-world web contamination involves multiple LLM sources.\nWe construct cross-model chains where each depth step uses a different generator from a 5-model pool, evaluating under generator-level LOGO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setup} & \\textbf{Bin. F1} & \\textbf{3-Class F1} & \\textbf{Protocol} \\\\\n\\midrule\nSingle-model (LOGO) & 0.694 & 0.762 & LOGO \\\\\nCross-model (LOGO) & 0.830 & 0.789 & Gen-LOGO \\\\\n$\\Delta$ & $+$0.136 & $+$0.027 & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Single-model vs.\\ cross-model chains. Generator heterogeneity amplifies depth signal by $+$13.6 pp binary F1.}\n\\label{tab:cross_model}\n\\end{table}\n\nCross-model chains yield substantially higher binary F1 (0.830 vs.\\ 0.694; Table~\\ref{tab:cross_model}).\nGenerator heterogeneity amplifies depth-to-depth feature variance, making classification easier.\nThis is practically relevant: real-world multi-source contamination is the condition under which DDR is strongest.\nPer-depth F1 shows gen-0 at 0.95, gen-1 at 0.82, and gen-2+ at 0.78.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\nWe fine-tune OLMo-1B on depth-stratified subsets (3 seeds, bootstrap CIs) to test whether depth-aware curation improves downstream causal language modeling.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{$N$} & \\textbf{PPL} & \\textbf{$\\Delta$ vs.\\ SM} \\\\\n\\midrule\nAll depths & 12,299 & 2.335 & $-$0.032 \\\\\nSize-matched random & 3,951 & 2.367 & — \\\\\nDepth 0+1 only & 3,951 & 2.387 & $+$0.020 \\\\\nBinary-filtered & 3,951 & 2.389 & $+$0.022 \\\\\nDepth 0 only & 797 & 2.681 & $+$0.314 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM perplexity by training data composition. At equal sample count, depth-aware curation does not improve over random subsampling.}\n\\label{tab:downstream}\n\\end{table}\n\nAt equal sample count ($n = 3{,}951$), size-matched random subsampling (PPL = 2.367) outperforms depth 0+1 filtering (2.387) and binary filtering (2.389; Table~\\ref{tab:downstream}).\nTOST equivalence is confirmed at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$).\nSeed variance is extremely small ($< 0.002$ PPL across seeds), indicating the result is robust.\nThis establishes depth fingerprinting as a \\textbf{diagnostic} tool for provenance characterization, not a curative tool for data selection.\n\n\\subsection{9-Generator Scale Evaluation}\n\\label{sec:9gen}\n\nExpanding to 9 generators (adding Gemma-2-2B, Llama-3.2-3B, Qwen3-8B, and Mistral-7B) tests broader generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{3-Cl F1} & \\textbf{Bin F1} & \\textbf{G1 F1} \\\\\n\\midrule\nPythia-1B & 1B & 0.857 & 0.718 & 0.65 \\\\\nQwen3-0.6B & 0.6B & 0.819 & 0.659 & 0.61 \\\\\nPythia-2.8B & 2.8B & 0.812 & 0.724 & 0.68 \\\\\nQwen3-1.7B & 1.7B & 0.811 & 0.702 & 0.66 \\\\\nOLMo-2-1B & 1.5B & 0.773 & 0.668 & 0.58 \\\\\nLlama-3.2-3B & 3B & 0.759 & 0.690 & 0.60 \\\\\nQwen3-8B & 8B & 0.696 & 0.647 & 0.52 \\\\\n\\textbf{Gemma-2-2B} & 2B & \\textbf{0.628} & \\textbf{0.440} & \\textbf{0.036} \\\\\nMistral-7B & 7B & 0.605 & 0.633 & 0.44 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{9-generator LOGO results. Gemma-2-2B exhibits anomalous gen-1 F1 = 0.036; Mistral-7B and Qwen3-8B show moderate scale-related degradation.}\n\\label{tab:9gen}\n\\end{table}\n\nThe 9-generator LOGO yields 3-class F1 = 0.751 and binary F1 = 0.666 (Table~\\ref{tab:9gen}).\nGemma-2-2B is a notable anomaly: gen-1 F1 = 0.036 indicates the classifier cannot distinguish Gemma's gen-1 output from gen-0.\nThis may reflect Gemma-2's architecture (grouped-query attention, RMSNorm) producing gen-1 distributional features unusually close to the seed text.\nThe method does not guarantee effectiveness across all generator architectures.\nLarger models (Qwen3-8B at 0.647, Mistral-7B at 0.633) show moderate degradation, compressing feature margins as model capacity increases.\n\n%==============================================================================\n% 5. DISCUSSION\n%==============================================================================\n\\section{Discussion}\n\n\\paragraph{Scope: base models only.}\nInstruction-tuned models show substantially degraded depth signal (Table~\\ref{tab:instruct_app}).\nOLMo-2-1B-Instruct drops to LOGO binary F1 = 0.338 (vs.\\ 0.763 base), with 6/7 features exhibiting Spearman $\\rho$ direction reversal.\nLlama-3.2-3B-Instruct is minimally affected ($-$1.1 pp), while Qwen3-1.7B-Instruct shows intermediate degradation ($-$16.3 pp).\nThis heterogeneity means we cannot predict \\textit{a priori} which instruct models will degrade.\nBase models remain relevant for data contamination analysis, as web-scraped synthetic text is predominantly generated by base or API models.\n\n\\paragraph{Temperature sensitivity.}\nDepth signal is reliable within $t \\in [0.5, 0.9)$ but degrades severely at $t = 0.9$ (binary F1 drops to 0.480; see Table~\\ref{tab:temp_app}).\nHigh-temperature sampling inflates entropy uniformly across depths, compressing inter-depth differences.\nCross-temperature transfer is asymmetric: training at $t = 1.0$ and testing at $t = 0.7$ yields F1 = 0.944, but the reverse yields only 0.418.\n\n\\paragraph{The \\texttt{entropy\\_std} question.}\nBootstrap TOST validation (1000 resamples, margin $d = 0.2$) rejects stationarity for three shape features (rejection rate 1000/1000) but \\emph{never} rejects for \\texttt{entropy\\_std} (rate 0/1000, median $d = 0.458$; Table~\\ref{tab:tost_app}).\nCross-reference analysis shows $d$ ranging from 0.310 (OLMo) to 0.520 (Qwen), further demonstrating inconsistency.\nWe adopt a spectrum model: drifting ($|\\rho| > 0.50$) $\\to$ intermediate (0.15--0.50) $\\to$ stationary ($< 0.15$), with \\texttt{entropy\\_std} and \\texttt{entropy\\_min} in the intermediate category.\n\n\\paragraph{Handcrafted vs.\\ end-to-end.}\nQLoRA fine-tuned classifiers substantially outperform the 7-feature ensemble (Table~\\ref{tab:qlora_app}): Qwen3-1.7B-Instruct achieves 3-class F1 = 0.907 and binary F1 = 0.867, a $+$14.5 pp improvement.\nThis confirms that depth signal is richer than what 7 features capture.\nWe position the 7-feature ensemble on \\emph{interpretability and efficiency}: it requires only a 410M reference model and XGBoost ($\\sim$150$\\times$ less inference cost), and its features enable the DDR analysis that constitutes our primary conceptual contribution.\n\n\\paragraph{Semantic convergence vs.\\ distributional divergence.}\nTopic drift analysis reveals a counter-intuitive pattern: deeper generations converge in semantic space (cosine similarity increases from 0.622 at gen-0$\\to$gen-1 to 0.859 at gen-3$\\to$gen-4) while distributional features diverge.\nDDR is a distributional phenomenon, not a semantic one.\n\n%==============================================================================\n% 6. CONCLUSION\n%==============================================================================\n\\section{Conclusion}\n\nWe formulate generation depth classification for non-paraphrastic LLM generation chains and characterize differential depth response across 8 base-model generators from 5 families.\nA lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (per-generator range 0.633--0.724) under LOGO evaluation, and 0.830 on cross-model chains, using a single 410M reference model.\nDDR is generation-intrinsic: it persists across reference models and is driven by drifting central-tendency features ($|\\rho| > 0.60$) while shape features remain stationary ($|\\rho| < 0.10$).\nDepth-aware data curation does not improve downstream CLM quality over random subsampling, establishing depth fingerprinting as diagnostic rather than curative.\n\nCurrent limitations include restriction to base models (instruct tuning degrades or reverses DDR), temperature sensitivity ($t \\geq 0.9$), a 3-class resolution ceiling, and architecture-specific failures (Gemma-2-2B gen-1 F1 = 0.036).\nExtending to instruct models and larger generators ($>$8B) remains future work.\n\n%==============================================================================\n% LIMITATIONS\n%==============================================================================\n\\section*{Limitations}\n\n\\begin{enumerate}\n    \\item \\textbf{Base models only.} The method does not reliably apply to instruction-tuned models, which represent a large fraction of deployed LLMs.\n    \\item \\textbf{Temperature range.} Reliable only for $t \\in [0.5, 0.9)$; most API defaults use $t = 1.0$.\n    \\item \\textbf{Scale.} Larger generators ($>$3B) show moderate signal degradation; 70B+ models are untested.\n    \\item \\textbf{Architecture sensitivity.} Gemma-2-2B represents a failure case; we cannot predict which architectures will fail.\n    \\item \\textbf{Downstream evidence.} The negative finding is based on 3 seeds and a single perplexity metric, though seed variance is extremely small ($<$0.002).\n    \\item \\textbf{Prompt-type dependence.} Performance varies across continuation, elaboration, and rewriting prompts (5 pp range).\n    \\item \\textbf{Paraphrastic chains.} The method does not apply to paraphrastic chains (binary F1 = 0.55 vs.\\ 0.694 for continuation).\n\\end{enumerate}\n\n%==============================================================================\n% REFERENCES\n%==============================================================================\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{20}\n\n\\bibitem[Mitchell et al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D.\\ Manning, and Chelsea Finn. 2023.\n\\newblock {DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Bao et al.(2024)]{bao2024fast}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang. 2024.\n\\newblock Fast-{DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Gehrmann et al.(2019)]{gehrmann2019gltr}\nSebastian Gehrmann, Hendrik Strobelt, and Alexander Rush. 2019.\n\\newblock {GLTR}: Statistical Detection and Visualization of Generated Text.\n\\newblock In \\emph{Proceedings of ACL: System Demonstrations}.\n\n\\bibitem[Hans et al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein. 2024.\n\\newblock Spotting {LLMs} With Binoculars: Zero-Shot Detection of Machine-Generated Text.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Yang et al.(2024)]{yang2024dnagpt}\nXianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen. 2024.\n\\newblock {DNA-GPT}: Divergent N-Gram Analysis for Training-Free Detection of {GPT}-Generated Text.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\end{thebibliography}\n\n%==============================================================================\n% APPENDIX\n%==============================================================================\n\\clearpage\n\\appendix\n\n\\section{Prompt Type Comparison}\n\\label{app:prompt}\n\nThree prompt types---continuation, elaboration, and inspired rewriting---exhibit different DDR strengths (Table~\\ref{tab:prompt}).\nContinuation shows the strongest depth signal (CV F1 = 0.781), consistent with its largest semantic divergence per step.\nCross-prompt-type transfer (LOPTO) averages F1 = 0.753.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt} & \\textbf{CV F1} & \\textbf{LOPTO F1} & \\textbf{Ret.} & \\textbf{$\\rho_\\text{hapax}$} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.74$ \\\\\nRewriting & 0.737 & 0.733 & 0.939 & $-0.80$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.83$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt type comparison. Higher semantic divergence (lower retention) correlates with stronger depth signal. LOPTO: leave-one-prompt-type-out.}\n\\label{tab:prompt}\n\\end{table}\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{app:para}\n\nParaphrastic chains show severely weakened depth signal (Table~\\ref{tab:para}), confirming the method's scope boundary.\nParaphrasing preserves semantics (retention = 0.97), compressing distributional variation across depths.\nBinary F1 drops to 0.55, near chance.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{CV F1} & \\textbf{Bin. F1} & \\textbf{$\\rho_\\text{hapax}$} & \\textbf{Ret.} \\\\\n\\midrule\nContinuation & 0.781 & 0.694 & $-0.74$ & 0.831 \\\\\nParaphrastic & 0.620 & 0.550 & $-0.35$ & 0.970 \\\\\n$\\Delta$ & $-0.161$ & $-0.144$ & $+0.39$ & $+0.139$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs.\\ continuation chains. Semantic preservation compresses depth signal.}\n\\label{tab:para}\n\\end{table}\n\n\\section{Multi-Domain Analysis}\n\\label{app:domain}\n\nDDR trends are preserved across four domains (Table~\\ref{tab:domain}), though classification performance is domain-dependent.\nAcademic text shows the weakest signal (0.628), likely due to inherently low vocabulary diversity in specialized scientific writing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{95\\% CI} & \\textbf{$\\rho_\\text{hapax}$} \\\\\n\\midrule\nNews & 0.712 & [0.690, 0.733] & $-0.65$ \\\\\nWikipedia & 0.695 & [0.675, 0.715] & $-0.63$ \\\\\nCode & 0.687 & [0.664, 0.710] & $-0.58$ \\\\\nAcademic & 0.628 & [0.603, 0.652] & $-0.52$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-domain binary F1. Cross-domain transfer F1 = 0.650.}\n\\label{tab:domain}\n\\end{table}\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{app:ordinal}\n\n5-class ordinal classification drops to F1 = 0.50 (Table~\\ref{tab:ordinal}).\nOrdinal methods (CORAL, Frank-Hall) provide no improvement, confirming the bottleneck is in feature signal, not model structure.\nGen-2 and gen-3 concentrate 65\\% of confusion errors.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llccl}\n\\toprule\n\\textbf{$K$} & \\textbf{Method} & \\textbf{F1} & \\textbf{G0 F1} & \\textbf{G2+ F1} \\\\\n\\midrule\n3 & XGBoost & 0.762 & 0.95 & 0.66 \\\\\n5 & XGBoost & 0.500 & 0.92 & .35/.30/.38 \\\\\n5 & CORAL & 0.500 & 0.91 & .34/.31/.38 \\\\\n5 & Frank-Hall & 0.490 & 0.90 & .33/.30/.37 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{3-class vs.\\ 5-class classification. 3-class is the practical resolution ceiling.}\n\\label{tab:ordinal}\n\\end{table}\n\n\\section{Robustness to Human Editing}\n\\label{app:edit}\n\nThe method shows graceful degradation under simulated human editing (Table~\\ref{tab:edit}).\nAt 5\\% random word replacement, binary F1 drops 4.6 pp; LLM rephrasing ($\\sim$50\\% edit distance) causes a comparable 4.5 pp drop.\nHeavy editing ($>$20\\%) substantially degrades signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Edit Type} & \\textbf{Rate} & \\textbf{Bin. F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nNone & 0\\% & 0.695 & — \\\\\nRandom & 5\\% & 0.650 & $-0.046$ \\\\\nRandom & 10\\% & 0.614 & $-0.081$ \\\\\nRandom & 20\\% & 0.591 & $-0.104$ \\\\\nLLM rephrase & $\\sim$50\\% ed. & 0.647 & $-0.045$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Robustness to simulated human editing.}\n\\label{tab:edit}\n\\end{table}\n\n\\section{LD-Score Feature Addition}\n\\label{app:ld}\n\nAdding LD-Score (character-level distribution signature) as an 8th feature yields marginal improvement ($+$0.7 pp macro F1, McNemar $p = 0.12$; Table~\\ref{tab:ld}).\nLD-Score correlates highly with hapax\\_ratio ($r = 0.68$), confirming character-level and token-level vocabulary diversity are largely redundant.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{$N$} & \\textbf{Macro F1} & \\textbf{McNemar $p$} \\\\\n\\midrule\n7-feature & 7 & 0.804 & — \\\\\n+ LD-Score & 8 & 0.811 & 0.12 \\\\\nLD-Score only & 1 & 0.721 & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LD-Score feature addition. Marginal contribution is not significant.}\n\\label{tab:ld}\n\\end{table}\n\n\\section{End-to-End QLoRA Classification}\n\\label{app:qlora}\n\nQLoRA fine-tuned classifiers substantially outperform the 7-feature ensemble (Table~\\ref{tab:qlora_app}), confirming depth signal is richer than captured by 7 features.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-Cl F1} & \\textbf{Bin F1} & \\textbf{5-Cl F1} & \\textbf{Cost} \\\\\n\\midrule\n7-feat XGBoost & 0.762 & 0.694 & 0.500 & 1$\\times$ \\\\\nQLoRA OLMo-1B-Inst & 0.889 & 0.836 & 0.598 & $\\sim$150$\\times$ \\\\\nQLoRA Qwen3-1.7B-Inst & 0.907 & 0.867 & 0.551 & $\\sim$250$\\times$ \\\\\nQLoRA OLMo-1B-Base & 0.859 & 0.793 & 0.540 & $\\sim$150$\\times$ \\\\\nQLoRA Qwen3-1.7B-Base & 0.904 & 0.860 & 0.554 & $\\sim$250$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Handcrafted vs.\\ end-to-end classification. QLoRA achieves $+$12--15 pp improvement at $\\sim$150--250$\\times$ inference cost.}\n\\label{tab:qlora_app}\n\\end{table}\n\n\\section{Text Length Control}\n\\label{app:length}\n\nLength-depth correlation is weak ($|\\rho| < 0.14$; Table~\\ref{tab:length}).\nLength-matched subsampling reduces binary F1 by 4.6 pp, but a random-subsample control (same $N$) also drops 3.0 pp, attributing only 1.6 pp to the length confound.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Bin. F1} & \\textbf{$\\Delta$} & \\textbf{Note} \\\\\n\\midrule\nFull (unmatched) & 0.770 & — & Full dataset \\\\\nLength-matched & 0.724 & $-0.046$ & Equalized \\\\\nRandom subsample & 0.740 & $-0.030$ & Size control \\\\\n$\\Delta$ (length) & — & $-0.016$ & Attributable \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Only 1.6 pp of the 4.6 pp drop is attributable to length.}\n\\label{tab:length}\n\\end{table}\n\n\\section{Large-Scale Generator}\n\\label{app:scale}\n\nAdding Qwen3-8B-Base (8B parameters) confirms moderate scale degradation (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Params} & \\textbf{LOGO Bin F1} & \\textbf{$\\rho_\\text{hapax}$} & \\textbf{$\\rho_\\text{ent.m}$} \\\\\n\\midrule\nPythia-1B & 1B & 0.718 & $-0.65$ & $-0.64$ \\\\\nQwen3-0.6B & 0.6B & 0.659 & $-0.60$ & $-0.58$ \\\\\nPythia-2.8B & 2.8B & 0.724 & $-0.63$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.702 & $-0.61$ & $-0.57$ \\\\\nOLMo-2-1B & 1.5B & 0.668 & $-0.57$ & $-0.52$ \\\\\nQwen3-8B & 8B & 0.683 & $-0.56$ & $-0.48$ \\\\\n\\midrule\n\\textbf{6-gen avg} & — & \\textbf{0.692} & $-0.60$ & $-0.57$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{6-generator LOGO including Qwen3-8B. Scale degradation is moderate ($-$1.1 pp average).}\n\\label{tab:scale}\n\\end{table}\n\n\\section{DDR Causality Analysis}\n\\label{app:causality}\n\nThree independent methods confirm drifting features carry $\\sim$5$\\times$ more predictive signal than stationary features (Table~\\ref{tab:causality}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Drifting} & \\textbf{Stationary} & \\textbf{Ratio} \\\\\n\\midrule\nPerm.\\ importance & 0.158 & 0.030 & 5.3$\\times$ \\\\\nGranger causality & 6/7 sig & — & — \\\\\nFeature intervention & 0.020 & 0.006 & 3.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DDR causality evidence. Drifting features dominate across all methods.}\n\\label{tab:causality}\n\\end{table}\n\n\\section{TOST Bootstrap Stability}\n\\label{sec:tost}\n\nBootstrap TOST (1000 resamples, $d = 0.2$ margin) validates stationarity for entropy\\_max, entropy\\_min, and tail\\_decay (Table~\\ref{tab:tost_app}) but rejects it for \\texttt{entropy\\_std} (rate 0/1000, median $d = 0.458$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Med.\\ $d$} & \\textbf{95\\% CI} & \\textbf{Rej.\\ Rate} & \\textbf{Class} \\\\\n\\midrule\nentropy\\_max & 0.062 & [0.037, 0.088] & 1000/1000 & Stationary \\\\\nentropy\\_min & $-0.016$ & [$-0.042$, 0.011] & 1000/1000 & Stationary \\\\\ntail\\_decay & 0.088 & [0.065, 0.111] & 1000/1000 & Stationary \\\\\n\\textbf{entropy\\_std} & \\textbf{0.458} & \\textbf{[0.435, 0.479]} & \\textbf{0/1000} & \\textbf{Intermediate} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST bootstrap stability. \\texttt{entropy\\_std} fails stationarity at $d = 0.2$ margin.}\n\\label{tab:tost_app}\n\\end{table}\n\n\\section{Instruct Model Evaluation}\n\\label{app:instruct}\n\nInstruction tuning substantially degrades depth signal, with heterogeneous effects across models (Table~\\ref{tab:instruct_app}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Base F1} & \\textbf{Inst F1} & \\textbf{$\\Delta$} & \\textbf{Feat Rev.} \\\\\n\\midrule\nOLMo-2-1B & 0.763 & 0.338 & $-0.425$ & 6/7 \\\\\nQwen3-1.7B & 0.821 & 0.658 & $-0.163$ & partial \\\\\nLlama-3.2-3B & 0.849 & 0.838 & $-0.011$ & 3/7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instruct vs.\\ base model depth signal. OLMo-Instruct shows near-complete degradation with feature direction reversal.}\n\\label{tab:instruct_app}\n\\end{table}\n\n\\section{Temperature Sensitivity}\n\\label{app:temp}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$t$} & \\textbf{Within-CV Bin F1} & \\textbf{$\\rho_\\text{ent.m}$} & \\textbf{Reliable} \\\\\n\\midrule\n0.5 & 0.813 & $-0.58$ & Yes \\\\\n0.7 & 0.694 & $-0.60$ & Yes \\\\\n0.9 & 0.480 & $-0.30$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temperature sensitivity. Signal degrades severely at $t \\geq 0.9$.}\n\\label{tab:temp_app}\n\\end{table}\n\nCross-temperature transfer (Qwen3-1.7B): training at $t = 0.7$, testing at $t = 1.0$ yields binary F1 = 0.418 ($-$37.1 pp vs.\\ within-temperature). The reverse direction ($t = 1.0 \\to 0.7$) yields 0.944 ($+$15.5 pp), demonstrating asymmetric transfer.\n\n\\section{Independent Seed Validation}\n\\label{app:seed_val}\n\nIndependent seed sets confirm shared-seed LOGO does not suffer seed leakage (Table~\\ref{tab:seed_val}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Setup} & \\textbf{Binary F1} & \\textbf{Seeds Shared} \\\\\n\\midrule\nShared-seed LOGO & 0.694 & Yes \\\\\nIndependent: Pythia$\\to$OLMo & 0.695 & No \\\\\nIndependent: OLMo$\\to$Pythia & 0.666 & No \\\\\nIndependent avg & 0.680 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed leakage validation. $\\Delta = -0.014$, within noise.}\n\\label{tab:seed_val}\n\\end{table}\n\n\\section{Seed Complexity Stratification}\n\\label{app:seed_complex}\n\nDepth signal is independent of seed text complexity (Table~\\ref{tab:seed_complex}; max difference 1.06 pp).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Complexity} & \\textbf{Bin F1} & \\textbf{Multi F1} & \\textbf{$N$} \\\\\n\\midrule\nLow & 0.685 & 0.772 & $\\sim$332 \\\\\nMedium & 0.695 & 0.778 & $\\sim$332 \\\\\nHigh & 0.695 & 0.779 & $\\sim$331 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed complexity stratification. Depth signal is seed-independent.}\n\\label{tab:seed_complex}\n\\end{table}\n\n\\section{Topic Drift Correlation}\n\\label{app:topic}\n\nSemantic similarity increases with depth (Table~\\ref{tab:topic}), while distributional features diverge---confirming DDR is distributional, not semantic.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Transition} & \\textbf{Mean Cosine Sim} & \\textbf{Std} \\\\\n\\midrule\ngen-0 $\\to$ gen-1 & 0.622 & 0.165 \\\\\ngen-1 $\\to$ gen-2 & 0.683 & 0.184 \\\\\ngen-2 $\\to$ gen-3 & 0.801 & 0.201 \\\\\ngen-3 $\\to$ gen-4 & 0.859 & 0.190 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Semantic similarity by depth transition. Deeper generations converge semantically while diverging distributionally.}\n\\label{tab:topic}\n\\end{table}\n\n\\section{TOST Equivalence Tests (Downstream)}\n\\label{app:tost_downstream}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Margin} & \\textbf{$p$} & \\textbf{Equiv.} \\\\\n\\midrule\nSM vs.\\ depth01 & $\\pm$2\\% & $1.1 \\times 10^{-4}$ & Yes \\\\\nSM vs.\\ binary-filt. & $\\pm$2\\% & $8.3 \\times 10^{-5}$ & Yes \\\\\nAll vs.\\ SM & $\\pm$2\\% & 0.15 & No \\\\\nAll vs.\\ SM & $\\pm$3\\% & 0.003 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST equivalence tests for downstream CLM quality. SM = size-matched random.}\n\\label{tab:tost_downstream}\n\\end{table}\n\n\\section{\\texttt{entropy\\_std} Cross-Reference Inconsistency}\n\\label{app:entropy_std}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Ref.\\ Model} & \\textbf{$d$} & \\textbf{TOST Rej.} & \\textbf{Class} \\\\\n\\midrule\nPythia-410M & 0.458 & 0/1000 & Contested \\\\\nOLMo-2-1B & 0.310 & partial & Borderline \\\\\nQwen3-0.6B & 0.520 & 0/1000 & Contested \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\texttt{entropy\\_std} Cohen's $d$ across reference models.}\n\\label{tab:entropy_std_cross}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "9606e5d9-d67a-459b-a92c-741c6da0ee94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "df3a5f74-be58-4746-b991-480cbcc06793",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260520T100349",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Tool call

_source line 22 · 2026-05-20T10:38:01.580Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BKpFtWBGEmEsaY7zMdKxV4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3a5f74-be58-4746-b991-480cbcc06793",
  "isSidechain": false,
  "requestId": "req_011CbDg96WwDMmLdNvTrZJSN",
  "type": "assistant",
  "uuid": "d8ca938f-10f6-4a58-a2ad-21e1a0f30ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cb5Gta1jU6ATNt72rrn3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15388,
      "cache_read_input_tokens": 58515,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 58515,
          "cache_creation_input_tokens": 15388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15388
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

_source line 23 · 2026-05-20T10:38:01.709Z_

<details><summary>↩ Tool result · reported error · `toolu_01BKpFtWBGEmEsaY7zMdKxV4`</summary>

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
  "parentUuid": "d8ca938f-10f6-4a58-a2ad-21e1a0f30ed0",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "80c106dd-cb48-4be3-baf0-730fc19e709b",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "d8ca938f-10f6-4a58-a2ad-21e1a0f30ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T10:38:04.282Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file isn't available. Let me switch to a simpler document class that doesn't require external style files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c106dd-cb48-4be3-baf0-730fc19e709b",
  "isSidechain": false,
  "requestId": "req_011CbDg9LrtxfeiR3uxdMU5Y",
  "type": "assistant",
  "uuid": "d2cee4e2-d0c7-4701-8a4b-32a0ce6e4a30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8J9mXwTj8KeXYbr7acP3D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 73903,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 73903,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 25 · 2026-05-20T10:38:04.841Z_

ACL style not available. Switching to a standalone class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2cee4e2-d0c7-4701-8a4b-32a0ce6e4a30",
  "isSidechain": false,
  "requestId": "req_011CbDg9LrtxfeiR3uxdMU5Y",
  "type": "assistant",
  "uuid": "7f1a6c69-eede-4fda-b6e1-4ebc449f2ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8J9mXwTj8KeXYbr7acP3D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 73903,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 73903,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 26 · 2026-05-20T10:38:10.629Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01UNDzGh6EtzSCw5FaY7JDix`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1a6c69-eede-4fda-b6e1-4ebc449f2ccb",
  "isSidechain": false,
  "requestId": "req_011CbDg9LrtxfeiR3uxdMU5Y",
  "type": "assistant",
  "uuid": "e9b2113f-7988-4ea5-8f44-f4b398e7b47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8J9mXwTj8KeXYbr7acP3D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 73903,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 73903,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 465
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

_source line 27 · 2026-05-20T10:38:10.656Z_

<details><summary>↩ Tool result · `toolu_01UNDzGh6EtzSCw5FaY7JDix`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b2113f-7988-4ea5-8f44-f4b398e7b47a",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "00752314-2a9b-4efd-b920-ae1150b89103",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}",
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
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}",
          " ",
          " \\title{Differential Depth Response in Non-Paraphrastic LLM Generation Chains: \\\\",
          " An Empirical Characterization Across Model Families}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e9b2113f-7988-4ea5-8f44-f4b398e7b47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T10:38:14.693Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XNtiWmeTUp3TzvP1xVytp1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
  "old_string": "\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00752314-2a9b-4efd-b920-ae1150b89103",
  "isSidechain": false,
  "requestId": "req_011CbDgA1HCXbZz2UPbufpRV",
  "type": "assistant",
  "uuid": "4354d3eb-d126-4eed-a30d-0dad045a74fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9N9hM3ntnUdDig9hBwtgF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 74368,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 74368,
          "cache_creation_input_tokens": 550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 550
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

_source line 29 · 2026-05-20T10:38:14.705Z_

<details><summary>↩ Tool result · `toolu_01XNtiWmeTUp3TzvP1xVytp1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4354d3eb-d126-4eed-a30d-0dad045a74fe",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "308bb53e-6bea-437e-94d5-91f1b54bb229",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/paper.tex",
    "oldString": "\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 431,
        "oldLines": 7,
        "newStart": 431,
        "newLines": 7,
        "lines": [
          " %==============================================================================",
          " % REFERENCES",
          " %==============================================================================",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          " \\begin{thebibliography}{20}",
          " ",
          " \\bibitem[Mitchell et al.(2023)]{mitchell2023detectgpt}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "4354d3eb-d126-4eed-a30d-0dad045a74fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T10:38:14.751Z_

```json
{
  "parentUuid": "308bb53e-6bea-437e-94d5-91f1b54bb229",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0da6bf10-a347-41da-99ca-775bd4b00a58",
  "timestamp": "2026-05-20T10:38:14.751Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 31 · 2026-05-20T10:38:17.739Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01J27z9DpkrQXwtvzmNzoYpb`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0da6bf10-a347-41da-99ca-775bd4b00a58",
  "isSidechain": false,
  "requestId": "req_011CbDgAJaFp9Bc8wyjRcQwW",
  "type": "assistant",
  "uuid": "f8d272f4-2e91-4845-a5a4-995e71309da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGAP9tHcBFFRoikYjxtX5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 74918,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 74918,
          "cache_creation_input_tokens": 347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 347
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

_source line 32 · 2026-05-20T10:38:18.700Z_

<details><summary>↩ Tool result · `toolu_01J27z9DpkrQXwtvzmNzoYpb`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 73.


Package natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin
e 73.


Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 74.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 75.


Package natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input 
line 76.


Overfull \hbox (19.10239pt too wide) in paragraph at lines 72--79
 []\OT1/ptm/b/n/10.95 Perplexity-based de-tec-tion.[] \OT1/ptm/m/n/10.95 Sta-ti
s-ti-cal de-tec-tion meth-ods lever-age the ob-ser-va-tion that machine-generat
ed

Overfull \hbox (0.41052pt too wide) in paragraph at lines 72--79
\OT1/ptm/m/n/10.95 perturbation-based cur-va-ture es-ti-ma-tion; Fast-DetectGPT
 \OT1/ptm/b/n/10.95 ? \OT1/ptm/m/n/10.95 re-places per-tur-ba-tions with con-di
-tional prob-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `sec:tost' on page 3 undefined on input line 126.


LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 147.

[3]

LaTeX Warning: Reference `tab:trend' on page 4 undefined on input line 165.


LaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 216.


LaTeX Warning: Reference `tab:cross_ref' on page 4 undefined on input line 254.



Overfull \hbox (10.86362pt too wide) in paragraph at lines 254--256
[]\OT1/ptm/m/n/10.95 All three ref-er-ence mod-els pro-duce con-sis-tent DDR: e
n-tropy drift is uni-ver-sally neg-a-tive, and tail[]decay
[4]

LaTeX Warning: Reference `tab:baseline' on page 5 undefined on input line 281.


LaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 30
7.


LaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 334
.


LaTeX Warning: Reference `tab:9gen' on page 5 undefined on input line 366.

[5]

LaTeX Warning: Reference `tab:instruct_app' on page 6 undefined on input line 3
78.


LaTeX Warning: Reference `tab:temp_app' on page 6 undefined on input line 385.


LaTeX Warning: Reference `tab:tost_app' on page 6 undefined on input line 390.


LaTeX Warning: Reference `tab:qlora_app' on page 6 undefined on input line 395.


[6] [7] [8]

LaTeX Warning: Reference `tab:prompt' on page 9 undefined on input line 473.


LaTeX Warning: Reference `tab:para' on page 9 undefined on input line 496.


LaTeX Warning: Reference `tab:domain' on page 9 undefined on input line 519.


LaTeX Warning: Reference `tab:ordinal' on page 9 undefined on input line 542.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:edit' on page 9 undefined on input line 566.

[9]

LaTeX Warning: Reference `tab:ld' on page 10 undefined on input line 591.


LaTeX Warning: Reference `tab:qlora_app' on page 10 undefined on input line 613
.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:length' on page 10 undefined on input line 636.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:scale' on page 10 undefined on input line 659.

[10]

LaTeX Warning: Reference `tab:causality' on page 11 undefined on input line 685
.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:tost_app' on page 11 undefined on input line 706.



LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:instruct_app' on page 11 undefined on input line 
728.


LaTeX Warning: `h' float specifier changed to `ht'.

[11]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:seed_val' on page 12 undefined on input line 770.



LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:seed_complex' on page 12 undefined on input line 
792.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:topic' on page 12 undefined on input line 813.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[12] [13] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time
s/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 192275 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (19.10239pt too wide) in paragraph at lines 72--79
 []\OT1/ptm/b/n/10.95 Perplexity-based de-tec-tion.[] \OT1/ptm/m/n/10.95 Sta-ti
s-ti-cal de-tec-tion meth-ods lever-age the ob-ser-va-tion that machine-generat
ed
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]
Overfull \hbox (10.86362pt too wide) in paragraph at lines 254--256
[]\OT1/ptm/m/n/10.95 All three ref-er-ence mod-els pro-duce con-sis-tent DDR: e
n-tropy drift is uni-ver-sally neg-a-tive, and tail[]decay
[4] [5] [6] [7] [8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[10]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[11]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[12] [13] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time
s/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 196210 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d272f4-2e91-4845-a5a4-995e71309da8",
  "isSidechain": false,
  "promptId": "195bd691-97f3-4a51-8285-2117347de551",
  "type": "user",
  "uuid": "74cf064f-cdce-42d0-9081-fe72e3a46d02",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 73.\n\n\nPackage natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin\ne 73.\n\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 74.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 75.\n\n\nPackage natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input \nline 76.\n\n\nOverfull \\hbox (19.10239pt too wide) in paragraph at lines 72--79\n []\\OT1/ptm/b/n/10.95 Perplexity-based de-tec-tion.[] \\OT1/ptm/m/n/10.95 Sta-ti\ns-ti-cal de-tec-tion meth-ods lever-age the ob-ser-va-tion that machine-generat\ned\n\nOverfull \\hbox (0.41052pt too wide) in paragraph at lines 72--79\n\\OT1/ptm/m/n/10.95 perturbation-based cur-va-ture es-ti-ma-tion; Fast-DetectGPT\n \\OT1/ptm/b/n/10.95 ? \\OT1/ptm/m/n/10.95 re-places per-tur-ba-tions with con-di\n-tional prob-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `sec:tost' on page 3 undefined on input line 126.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 147.\n\n[3]\n\nLaTeX Warning: Reference `tab:trend' on page 4 undefined on input line 165.\n\n\nLaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 216.\n\n\nLaTeX Warning: Reference `tab:cross_ref' on page 4 undefined on input line 254.\n\n\n\nOverfull \\hbox (10.86362pt too wide) in paragraph at lines 254--256\n[]\\OT1/ptm/m/n/10.95 All three ref-er-ence mod-els pro-duce con-sis-tent DDR: e\nn-tropy drift is uni-ver-sally neg-a-tive, and tail[]decay\n[4]\n\nLaTeX Warning: Reference `tab:baseline' on page 5 undefined on input line 281.\n\n\nLaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 30\n7.\n\n\nLaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 334\n.\n\n\nLaTeX Warning: Reference `tab:9gen' on page 5 undefined on input line 366.\n\n[5]\n\nLaTeX Warning: Reference `tab:instruct_app' on page 6 undefined on input line 3\n78.\n\n\nLaTeX Warning: Reference `tab:temp_app' on page 6 undefined on input line 385.\n\n\nLaTeX Warning: Reference `tab:tost_app' on page 6 undefined on input line 390.\n\n\nLaTeX Warning: Reference `tab:qlora_app' on page 6 undefined on input line 395.\n\n\n[6] [7] [8]\n\nLaTeX Warning: Reference `tab:prompt' on page 9 undefined on input line 473.\n\n\nLaTeX Warning: Reference `tab:para' on page 9 undefined on input line 496.\n\n\nLaTeX Warning: Reference `tab:domain' on page 9 undefined on input line 519.\n\n\nLaTeX Warning: Reference `tab:ordinal' on page 9 undefined on input line 542.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:edit' on page 9 undefined on input line 566.\n\n[9]\n\nLaTeX Warning: Reference `tab:ld' on page 10 undefined on input line 591.\n\n\nLaTeX Warning: Reference `tab:qlora_app' on page 10 undefined on input line 613\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:length' on page 10 undefined on input line 636.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:scale' on page 10 undefined on input line 659.\n\n[10]\n\nLaTeX Warning: Reference `tab:causality' on page 11 undefined on input line 685\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:tost_app' on page 11 undefined on input line 706.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:instruct_app' on page 11 undefined on input line \n728.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:seed_val' on page 12 undefined on input line 770.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:seed_complex' on page 12 undefined on input line \n792.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:topic' on page 12 undefined on input line 813.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[12] [13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\ns/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 192275 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (19.10239pt too wide) in paragraph at lines 72--79\n []\\OT1/ptm/b/n/10.95 Perplexity-based de-tec-tion.[] \\OT1/ptm/m/n/10.95 Sta-ti\ns-ti-cal de-tec-tion meth-ods lever-age the ob-ser-va-tion that machine-generat\ned\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [3]\nOverfull \\hbox (10.86362pt too wide) in paragraph at lines 254--256\n[]\\OT1/ptm/m/n/10.95 All three ref-er-ence mod-els pro-duce con-sis-tent DDR: e\nn-tropy drift is uni-ver-sally neg-a-tive, and tail[]decay\n[4] [5] [6] [7] [8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[12] [13] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\ns/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 196210 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f8d272f4-2e91-4845-a5a4-995e71309da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "74cf064f-cdce-42d0-9081-fe72e3a46d02",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260520T100349",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Assistant

_source line 35 · 2026-05-20T10:38:25.388Z_

编译成功，生成 13 页 PDF。

论文覆盖了 `experiment_data.json` 中全部 20 个实验，每个实验对应至少一个 table 和对应 section。主文 8 页（Abstract/Introduction/Related Work/Method/Experiments 6 subsections/Discussion/Conclusion/Limitations），附录 5 页覆盖其余 14 个实验。所有数字直接取自实验数据，无编造。

输出文件：`artifacts/dream_reports/dream_20260520T100349/median/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74cf064f-cdce-42d0-9081-fe72e3a46d02",
  "isSidechain": false,
  "requestId": "req_011CbDgAbUVsAxGprDAkpRJ4",
  "type": "assistant",
  "uuid": "bf7ca666-5589-4331-9f2a-bc75363be9ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6MP7rt9RKuLToyfCZyAoZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7510,
      "cache_read_input_tokens": 75265,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 75265,
          "cache_creation_input_tokens": 7510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7510
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "bf7ca666-5589-4331-9f2a-bc75363be9ef",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for dream_20260520T100349",
  "sessionId": "bf76e3fd-e630-4bd3-9134-5a44eba8a7bc"
}
```

---
