# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/c4321cb1-84b0-4cbf-9932-aa6cf3807d7b.jsonl`
- **Structured JSON:** [`847f1e3d025bd50597a9.json`](../../sessions/84/847f1e3d025bd50597a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T22:11:56.055Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T22:11:56.055Z",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心 framing 失效。Reviewer 共识：(1) base-model-only + temperature [0.5,0.9] 的 scope 在 2026 年没有实际意义——instruct/chat models 主导生成内容，方法对 instruct models 信号反转 (ρ 从负变正)；(2) 0.694 binary F1 被认为不足以支撑 classification claim ——random baseline 0.5，margin 仅 0.194，per-gen 最差 Mistral-7B 只有 0.633；(3) DDR decoding-agnostic 被视为 incremental robustness check 而非 contribution upgrade——\"验证了方法在另一种 decoding 下也能产生同样 modest 的结果\"； (4) Negative finding 被 weaponize 为 \"so the method has no practical use?\"——depth-aware curation ≡ random subsampling 直接 质疑 task motivation；(5) 多位 reviewer 指出所有 drifting features 都在测量同一个 vocabulary impoverishment 现象，DDR 不是新发现 而是 repackaging；(6) 写作修复不充分，presentation issues 加剧负面印象。 Reframe 方向：从 'depth classification tool' 转向 'understanding distributional dynamics of recursive autoregressive generation' ——DDR 本身作为 analytical framework 是贡献，classifier 降级为 validation probe。Paper 重心从 Claim 1 转移到 Claim 2 (DDR characterization) + decoding-agnostic 作为主线。Claim 3 negative finding 重新包装为 'distributional shift ≠ quality degradation, challenging implicit assumptions in model collapse literature'。 这个 reframe 放弃 practical utility 叙事，转向 understanding/characterization 贡献。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T22:11:56.058Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T22:11:56.058Z",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-21T22:11:56.074Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心 framing 失效。Reviewer 共识：(1) base-model-only + temperature [0.5,0.9] 的 scope 在 2026 年没有实际意义——instruct/chat models 主导生成内容，方法对 instruct models 信号反转 (ρ 从负变正)；(2) 0.694 binary F1 被认为不足以支撑 classification claim ——random baseline 0.5，margin 仅 0.194，per-gen 最差 Mistral-7B 只有 0.633；(3) DDR decoding-agnostic 被视为 incremental robustness check 而非 contribution upgrade——"验证了方法在另一种 decoding 下也能产生同样 modest 的结果"； (4) Negative finding 被 weaponize 为 "so the method has no practical use?"——depth-aware curation ≡ random subsampling 直接 质疑 task motivation；(5) 多位 reviewer 指出所有 drifting features 都在测量同一个 vocabulary impoverishment 现象，DDR 不是新发现 而是 repackaging；(6) 写作修复不充分，presentation issues 加剧负面印象。 Reframe 方向：从 'depth classification tool' 转向 'understanding distributional dynamics of recursive autoregressive generation' ——DDR 本身作为 analytical framework 是贡献，classifier 降级为 validation probe。Paper 重心从 Claim 1 转移到 Claim 2 (DDR characterization) + decoding-agnostic 作为主线。Claim 3 negative finding 重新包装为 'distributional shift ≠ quality degradation, challenging implicit assumptions in model collapse literature'。 这个 reframe 放弃 practical utility 叙事，转向 understanding/characterization 贡献。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "12d921e8-341f-44ac-a576-e06495ed1bc0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T22:11:56.073Z_

```json
{
  "parentUuid": "12d921e8-341f-44ac-a576-e06495ed1bc0",
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
  "uuid": "5c6d8a51-0147-450a-bdfd-8cabb24ce62e",
  "timestamp": "2026-05-21T22:11:56.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T22:11:56.073Z_

```json
{
  "parentUuid": "5c6d8a51-0147-450a-bdfd-8cabb24ce62e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6f3495a4-3c27-4200-96f2-c74b48556ae4",
  "timestamp": "2026-05-21T22:11:56.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
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
  "aiTitle": "Generate reframed paper on depth decoding dynamics",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Assistant

_source line 7 · 2026-05-21T22:11:58.431Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f3495a4-3c27-4200-96f2-c74b48556ae4",
  "isSidechain": false,
  "requestId": "req_011CbGUsJqdjgLqBRbNCMUpy",
  "type": "assistant",
  "uuid": "5873a142-f14b-4918-af45-1ff66270d868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gobSQbYYUCiiUK9SZHLwp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13784,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13784
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

_source line 8 · 2026-05-21T22:11:59.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GBwcG7BT6muTWgCQy5FSn6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5873a142-f14b-4918-af45-1ff66270d868",
  "isSidechain": false,
  "requestId": "req_011CbGUsJqdjgLqBRbNCMUpy",
  "type": "assistant",
  "uuid": "3c8d78a1-eeb3-496f-ac5f-bfd40524b20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gobSQbYYUCiiUK9SZHLwp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13784,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13784
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

_source line 9 · 2026-05-21T22:11:59.683Z_

<details><summary>↩ Tool result · `toolu_01GBwcG7BT6muTWgCQy5FSn6`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "MVP 数据上三部分分析：(A) Feature ablation: reference-only vs surface-only vs full 7-feature, XGBoost 5-fold CV； (B) 每个 feature 的 depth trend (slope, R², Spearman ρ)；(C) Pythia-410M perplexity pre-validation for Claim 3。\n",
5	    "results": {
6	      "full_macro_f1": 0.82,
7	      "surface_only_f1": 0.763,
8	      "reference_only_f1": 0.719,
9	      "surface_vs_full_gap_pp": 5.7,
10	      "ref_vs_surf_bootstrap_ci": "[0.706,0.733] vs [0.747,0.774]",
11	      "mcnemar_full_vs_surface_p": 0.0,
12	      "mcnemar_full_vs_ref_p": 0.0,
13	      "h2_features": "entropy_mean, ttr, hapax_ratio",
14	      "h1_features": "tail_decay, entropy_std, entropy_max, entropy_min",
15	      "hapax_ratio_slope": -0.063,
16	      "hapax_ratio_r2": 0.88,
17	      "hapax_ratio_rho": -0.63,
18	      "ttr_slope": -0.041,
19	      "ttr_r2": 0.82,
20	      "ttr_rho": -0.61,
21	      "entropy_mean_slope": -0.089,
22	      "entropy_mean_r2": 0.79,
23	      "entropy_mean_rho": -0.6,
24	      "entropy_std_slope": -0.031,
25	      "entropy_std_r2": 0.41,
26	      "entropy_std_rho": -0.2,
27	      "tail_decay_slope": 0.003,
28	      "tail_decay_r2": 0.04,
29	      "tail_decay_rho": 0.04,
30	      "entropy_max_slope": 0.008,
31	      "entropy_max_r2": 0.07,
32	      "entropy_max_rho": 0.05,
33	      "median_ppl_by_depth": [
34	        13.5,
35	        4.96,
36	        3.0,
37	        2.07,
38	        1.72
39	      ]
40	    },
41	    "tables": [
42	      {
43	        "caption": "Feature ablation: 5-fold CV macro F1 on MVP data (Pythia-2.8B, ~4600 records)",
44	        "rows": [
45	          [
46	            "Feature Set",
47	            "Macro F1",
48	            "95% CI",
49	            "Δ vs Full"
50	          ],
51	          [
52	            "Full (7 features)",
53	            "0.820",
54	            "[0.807, 0.833]",
55	            "—"
56	          ],
57	          [
58	            "Surface-only (TTR + hapax)",
59	            "0.763",
60	            "[0.747, 0.774]",
61	            "−5.7 pp"
62	          ],
63	          [
64	            "Reference-only (5 entropy)",
65	            "0.719",
66	            "[0.706, 0.733]",
67	            "−10.1 pp"
68	          ]
69	        ]
70	      },
71	      {
72	        "caption": "Per-feature depth trend (linear regression on depth 0–4)",
73	        "rows": [
74	          [
75	            "Feature",
76	            "Category",
77	            "Slope",
78	            "R²",
79	            "Spearman ρ"
80	          ],
81	          [
82	            "hapax_ratio",
83	            "Drifting",
84	            "−0.063",
85	            "0.88",
86	            "−0.63"
87	          ],
88	          [
89	            "TTR",
90	            "Drifting",
91	            "−0.041",
92	            "0.82",
93	            "−0.61"
94	          ],
95	          [
96	            "entropy_mean",
97	            "Drifting",
98	            "−0.089",
99	            "0.79",
100	            "−0.60"
101	          ],
102	          [
103	            "entropy_std",
104	            "Ambiguous",
105	            "−0.031",
106	            "0.41",
107	            "−0.20"
108	          ],
109	          [
110	            "entropy_min",
111	            "Stationary",
112	            "−0.018",
113	            "0.22",
114	            "−0.15"
115	          ],
116	          [
117	            "tail_decay",
118	            "Stationary",
119	            "+0.003",
120	            "0.04",
121	            "+0.04"
122	          ],
123	          [
124	            "entropy_max",
125	            "Stationary",
126	            "+0.008",
127	            "0.07",
128	            "+0.05"
129	          ]
130	        ]
131	      }
132	    ],
133	    "figures": [],
134	    "analysis": "在 worst 档下，ablation 的核心问题是 surface features 太强：93% signal retention 意味着 reference features 的  independent contribution minimal。Reviewer 会写：\"The proposed DDR framework adds substantial complexity (reference  model inference, 5 entropy features) for a 5.7 pp improvement over two simple vocabulary diversity metrics. The claim  of 'complementary signal' is technically supported but practically marginal.\" entropy_std 的 ambiguous status  (R²=0.41, ρ=-0.20) 破坏 DDR clean binary split 的叙事核心，reviewer 会 argue 这是 continuous degradation  而非 bimodal response。\n\n\nSurface-only (0.763) 达到 full (0.820) 的 93%——审稿人会 argue reference features 只是 marginal add-on，不构成独立 contribution。虽然 McNemar p=0 确认显著性，但 worst-tier reviewer 会指出 5.7 pp 差距中 hapax_ratio 单个 surface  feature 就占据了 0.289 importance（plan-002-eval 实测），说明 reference features 被 surface features 的 vocabulary  impoverishment 信号 dominate。entropy_std 的 R²=0.41 处于 drifting/stationary 灰色地带，reviewer 会 argue DDR  不是 bimodal dichotomy 而是 continuous gradient——\"the clean split between drifting and stationary is an artifact of  thresholding a continuous degradation spectrum.\" 所有 drifting features (hapax, TTR, entropy_mean) 沿同一方向单调递减， reviewer 会 argue 这就是 well-known vocabulary impoverishment 的多种测量维度，不是新现象。Perplexity 单调递减  (13.50→1.72) 只是说明 recursive generation 使 text 对 reference model 更 predictable——这是 trivial observation。\n"
135	  },
136	  {
137	    "name": "cross_generator_evaluation",
138	    "description": "扩展到 8 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Llama-3.2-3B, Qwen3-8B,  Mistral-7B-v0.3) 的 LOGO 评估。~37K records。\n",
139	    "results": {
140	      "total_records": 37500,
141	      "generators": 8,
142	      "families": 5,
143	      "logo_avg_3class_f1": 0.762,
144	      "logo_avg_3class_ci": [
145	        0.758,
146	        0.766
147	      ],
148	      "logo_avg_binary_f1": 0.694,
149	      "logo_binary_ci": [
150	        0.688,
151	        0.7
152	      ],
153	      "lofo_binary_f1": 0.686,
154	      "per_gen_binary_f1": {
155	        "pythia-1b": 0.724,
156	        "pythia-2.8b": 0.711,
157	        "qwen3-0.6b": 0.702,
158	        "qwen3-1.7b": 0.698,
159	        "olmo-2-1b": 0.679,
160	        "llama-3.2-3b": 0.688,
161	        "qwen3-8b": 0.647,
162	        "mistral-7b": 0.633
163	      },
164	      "per_gen_range_pp": 9.1,
165	      "fn_rate_of_binary_errors": 0.86,
166	      "worst_gen": "mistral-7b-v0.3",
167	      "best_gen": "pythia-1b"
168	    },
169	    "tables": [
170	      {
171	        "caption": "Leave-one-generator-out (LOGO) binary F1 (gen-1 vs gen-2+, 8 generators)",
172	        "rows": [
173	          [
174	            "Held-out Generator",
175	            "Family",
176	            "Size",
177	            "Binary F1",
178	            "95% CI"
179	          ],
180	          [
181	            "Pythia-1B",
182	            "Pythia",
183	            "1.0B",
184	            "0.724",
185	            "[0.707, 0.741]"
186	          ],
187	          [
188	            "Pythia-2.8B",
189	            "Pythia",
190	            "2.8B",
191	            "0.711",
192	            "[0.693, 0.729]"
193	          ],
194	          [
195	            "Qwen3-0.6B",
196	            "Qwen",
197	            "0.6B",
198	            "0.702",
199	            "[0.682, 0.722]"
200	          ],
201	          [
202	            "Qwen3-1.7B",
203	            "Qwen",
204	            "1.7B",
205	            "0.698",
206	            "[0.678, 0.718]"
207	          ],
208	          [
209	            "Llama-3.2-3B",
210	            "Llama",
211	            "3.0B",
212	            "0.688",
213	            "[0.668, 0.708]"
214	          ],
215	          [
216	            "OLMo-2-1B",
217	            "OLMo",
218	            "1.5B",
219	            "0.679",
220	            "[0.658, 0.700]"
221	          ],
222	          [
223	            "Qwen3-8B",
224	            "Qwen",
225	            "8.0B",
226	            "0.647",
227	            "[0.624, 0.670]"
228	          ],
229	          [
230	            "Mistral-7B-v0.3",
231	            "Mistral",
232	            "7.0B",
233	            "0.633",
234	            "[0.609, 0.657]"
235	          ],
236	          [
237	            "**Average**",
238	            "—",
239	            "—",
240	            "**0.694**",
241	            "[0.688, 0.700]"
242	          ]
243	        ]
244	      },
245	      {
246	        "caption": "Leave-one-family-out (LOFO) binary F1",
247	        "rows": [
248	          [
249	            "Held-out Family",
250	            "Binary F1",
251	            "Δ vs LOGO"
252	          ],
253	          [
254	            "Pythia",
255	            "0.668",
256	            "−2.6 pp"
257	          ],
258	          [
259	            "Qwen",
260	            "0.672",
261	            "−2.2 pp"
262	          ],
263	          [
264	            "OLMo",
265	            "0.714",
266	            "+2.0 pp"
267	          ],
268	          [
269	            "Llama",
270	            "0.701",
271	            "+0.7 pp"
272	          ],
273	          [
274	            "Mistral",
275	            "0.673",
276	            "−2.1 pp"
277	          ],
278	          [
279	            "**Average**",
280	            "**0.686**",
281	            "**−0.8 pp**"
282	          ]
283	        ]
284	      }
285	    ],
286	    "figures": [],
287	    "analysis": "0.694 是论文 headline number，也是 worst 档审稿人的 primary attack target。两个结构性问题：(1) margin over  chance (0.194) 太薄——在 noisy real-world setting 下可能进一步缩小到 near-chance；(2) per-gen range 9.1 pp  说明 performance 高度 generator-dependent，最差的大模型们恰好是最重要的模型。审稿人会 write：\"At the models  that actually generate content at scale (7B+), the method achieves binary F1 of 0.633–0.647, which is  not meaningfully above random guessing for a balanced binary task.\"\n\n\nLOGO binary F1 = 0.694，margin over random baseline (0.50) 仅 0.194。在 balanced binary 任务中，这意味着  每 10 个 gen-2+ 样本中约 3 个被误判为 gen-1。Per-gen range 达 9.1 pp (Pythia-1B 0.724 vs Mistral-7B 0.633)， 审稿人会 argue 方法 performance 高度依赖 generator identity，且最差的恰好是两个较大模型 (Mistral-7B 0.633,  Qwen3-8B 0.647)——暗示 scale 上升时方法失效。LOFO binary F1 = 0.686 比 LOGO 低 0.8 pp，说明跨 family 泛化 存在但 margin 更薄。86% 的 binary errors 集中在 FN (gen-2+ 被判为 gen-1)——方法系统性地 under-detect deeper  generation，恰好是实际应用中最需要检出的样本。Reviewer 会写：\"The primary metric of 0.694 offers a margin of  less than 0.20 over random guessing. While statistically significant, this margin is far too thin for any  practical deployment, particularly given the 9 pp variance across generators and the systematic FN bias  toward deeper generations.\"\n"
288	  },
289	  {
290	    "name": "cross_family_reference_model",
291	    "description": "测试 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model (替代 Pythia-410M)。验证 DDR drift 是否在  非 Pythia reference 下持续存在。Claim 2 的关键 falsification test。\n",
292	    "results": {
293	      "logo_f1_pythia_ref": 0.803,
294	      "logo_f1_olmo_ref": 0.807,
295	      "logo_f1_qwen_ref": 0.816,
296	      "entropy_mean_drift_pythia_range": [
297	        -1.19,
298	        -1.4
299	      ],
300	      "entropy_mean_drift_olmo_range": [
301	        -0.61,
302	        -0.91
303	      ],
304	      "entropy_mean_drift_qwen_range": [
305	        -0.96,
306	        -1.35
307	      ],
308	      "drift_direction_consistent": true,
309	      "shape_stationary_all_refs": true,
310	      "drift_magnitude_ratio_olmo_vs_pythia": 0.55,
311	      "qwen_ref_gives_best_logo": true
312	    },
313	    "tables": [
314	      {
315	        "caption": "Cross-reference-model DDR comparison",
316	        "rows": [
317	          [
318	            "Reference Model",
319	            "Size",
320	            "LOGO F1",
321	            "entropy_mean avg ρ",
322	            "hapax avg ρ",
323	            "tail_decay avg ρ",
324	            "Drift magnitude range"
325	          ],
326	          [
327	            "Pythia-410M",
328	            "410M",
329	            "0.803",
330	            "−0.60",
331	            "−0.63",
332	            "+0.04",
333	            "[−1.19, −1.40]"
334	          ],
335	          [
336	            "OLMo-2-1B",
337	            "1.5B",
338	            "0.807",
339	            "−0.50",
340	            "−0.58",
341	            "+0.07",
342	            "[−0.61, −0.91]"
343	          ],
344	          [
345	            "Qwen3-0.6B",
346	            "0.6B",
347	            "0.816",
348	            "−0.56",
349	            "−0.61",
350	            "+0.05",
351	            "[−0.96, −1.35]"
352	          ]
353	        ]
354	      }
355	    ],
356	    "figures": [],
357	    "analysis": "这是 worst 档中最 subtle 的攻击向量。实验技术上通过了 falsification (drift direction consistent, shape  stationary)，但 magnitude dependence on reference model 给了审稿人一个 elegant reframe：\"DDR is not a  pure property of recursive generation but a joint function of generation and reference model. The authors'  claim of an 'intrinsic differential response' is overstated—it's a measurement-relative phenomenon.\"  这不会导致 reject 但会让 Claim 2 的 contribution 评估降半档。\n\n\nFalsification test 技术上通过了——drift direction 在所有 reference models 下一致 (所有 entropy_mean ρ < 0， 所有 shape features |ρ| < 0.10)。但 drift magnitude 高度依赖 reference model：OLMo reference 的 entropy_mean  drift 仅为 Pythia 的 ~55% (-0.61 vs -1.19 on weakest generator)。LOGO F1 across references 差异小  (0.803–0.816)——但 worst-tier reviewer 会 reframe 这为：\"The classification performance is similar regardless  of reference model, but the underlying DDR characterization changes substantially. This means DDR magnitude  is as much a function of reference-generator mismatch as of recursive depth. The phenomenon the authors claim  to study is partially an artifact of their measurement instrument.\" 技术上不 kill Claim 2，但 interpretive  precision 被严重削弱。Qwen reference 给出最高 LOGO 说明 reference choice matters——在 worst 档下这被视为  \"the method's performance depends on an engineering choice (reference model) that has no principled selection  criterion.\"\n"
358	  },
359	  {
360	    "name": "downstream_utility",
361	    "description": "Fine-tune OLMo-1B on depth-stratified data subsets。3 random seeds, bootstrap CIs。Compare depth-aware  filtering vs binary baselines vs random subsampling。Sample-count-matched comparison。\n",
362	    "results": {
363	      "all_data_ppl_mean": 2.335,
364	      "all_data_ppl_std": 0.0003,
365	      "size_matched_ppl_mean": 2.367,
366	      "size_matched_ppl_std": 0.0003,
367	      "depth01_ppl_mean": 2.387,
368	      "depth01_ppl_std": 0.0004,
369	      "binary_filtered_ppl_mean": 2.389,
370	      "binary_filtered_ppl_std": 0.0006,
371	      "depth0_only_ppl_mean": 2.681,
372	      "depth0_only_ppl_std": 0.0006,
373	      "tost_p_2pct": 0.00011,
374	      "tost_p_1pct": 0.087,
375	      "ranking": "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)",
376	      "seed_variance": "极小 (<0.002 within variant)",
377	      "cohens_d_sizematched_vs_depth01": 0.42
378	    },
379	    "tables": [
380	      {
381	        "caption": "Downstream CLM perplexity by training data depth composition (3 seeds, OLMo-1B)",
382	        "rows": [
383	          [
384	            "Variant",
385	            "Train Size",
386	            "PPL (mean ± std)",
387	            "Δ vs Size-matched",
388	            "TOST ±2% p"
389	          ],
390	          [
391	            "All depths",
392	            "12,299",
393	            "2.335 ± 0.0003",
394	            "—",
395	            "—"
396	          ],
397	          [
398	            "Size-matched random",
399	            "3,951",
400	            "2.367 ± 0.0003",
401	            "ref",
402	            "ref"
403	          ],
404	          [
405	            "Depth 0+1 only",
406	            "3,951",
407	            "2.387 ± 0.0004",
408	            "+0.020",
409	            "1.1×10⁻⁴"
410	          ],
411	          [
412	            "Binary filtered",
413	            "3,951",
414	            "2.389 ± 0.0006",
415	            "+0.022",
416	            "8.7×10⁻⁵"
417	          ],
418	          [
419	            "Depth 0 only",
420	            "797",
421	            "2.681 ± 0.0006",
422	            "+0.314",
423	            "—"
424	          ]
425	        ]
426	      }
427	    ],
428	    "figures": [],
429	    "analysis": "Negative finding 是 worst 档的 strategic vulnerability。论文 framing 为 \"diagnostic not curative\"  是诚实的，但 worst-tier reviewers 会 argue diagnostic value 未被证明——\"where is the use case where  knowing depth matters?\" 这与 Claim 1 的 practical motivation 形成 circular problem：如果 depth 没有 downstream impact，为什么要分类 depth？论文需要 reframe 为 understanding contribution (DDR characterization)  而非 any form of utility，但这 reframe 在 worst 档下被视为 post-hoc rationalization。\n\n\nNegative finding 极其 clean 且 robust：depth-aware filtering 与 random subsampling 在 ±2% margin 内  equivalence 被 TOST 确认 (p=1.1×10⁻⁴)。Cross-seed variance < 0.002 意味着这个 negative finding 是  highly reliable——不是 noisy null 而是 genuine equivalence。Ranking 显示更多数据 always better (all <  size_matched)，depth filtering 反而 slightly worse than random (2.387 vs 2.367)——意味着 depth-aware  curation 不仅没有帮助，还可能因为丢弃了 useful training signal 而 slightly hurt。\n审稿人在 worst 档下会 weaponize 这个结果：\"The authors' own Claim 3 establishes that generation depth  is informationally vacuous for the most obvious downstream application. If depth information provides  zero utility for data curation — indeed, depth-filtered data is slightly WORSE than random — then the  practical motivation for depth classification collapses entirely. The paper's pivot to 'diagnostic tool'  is an ad hoc rescue, not a designed contribution.\" TOST 在 ±1% margin 不显著 (p=0.087) 会被注意到但 不 weaponize (论文已选 ±2%)。depth0_only 的高 perplexity (2.681) 只证明 human vs machine 有区别—— 这是 binary detection 已解决的问题，不支持 depth classification 的 incremental value。\n"
430	  },
431	  {
432	    "name": "prompt_type_comparison",
433	    "description": "Compare continuation vs elaboration vs inspired_rewriting chains。1000 seeds × Pythia-2.8B × 3 prompt types。\n",
434	    "results": {
435	      "cv_f1_continuation": 0.781,
436	      "cv_f1_elaboration": 0.73,
437	      "cv_f1_rewriting": 0.737,
438	      "lopto_avg_f1": 0.753,
439	      "lopto_held_out_cont": 0.762,
440	      "lopto_held_out_elab": 0.762,
441	      "lopto_held_out_rewrite": 0.734,
442	      "depth_retention_cont": 0.831,
443	      "depth_retention_elab": 0.986,
444	      "depth_retention_rewrite": 0.939,
445	      "drift_hapax_cont": -0.74,
446	      "drift_hapax_elab": -0.828,
447	      "drift_hapax_rewrite": -0.8,
448	      "drift_entropy_mean_cont": -0.557,
449	      "drift_entropy_mean_elab": -0.471,
450	      "drift_entropy_mean_rewrite": -0.477,
451	      "spearman_ttr_cont": -0.629,
452	      "spearman_ttr_elab": -0.666,
453	      "spearman_ttr_rewrite": -0.659,
454	      "cross_prompt_type_range_pp": 5.1
455	    },
456	    "tables": [
457	      {
458	        "caption": "Per-prompt-type classification and drift statistics (Pythia-2.8B)",
459	        "rows": [
460	          [
461	            "Prompt Type",
462	            "CV F1",
463	            "LOPTO F1",
464	            "Depth Retention",
465	            "entropy_mean ρ",
466	            "hapax ρ",
467	            "TTR ρ"
468	          ],
469	          [
470	            "Continuation",
471	            "0.781",
472	            "0.762",
473	            "0.831",
474	            "−0.557",
475	            "−0.740",
476	            "−0.629"
477	          ],
478	          [
479	            "Elaboration",
480	            "0.730",
481	            "0.762",
482	            "0.986",
483	            "−0.471",
484	            "−0.828",
485	            "−0.666"
486	          ],
487	          [
488	            "Inspired Rewriting",
489	            "0.737",
490	            "0.734",
491	            "0.939",
492	            "−0.477",
493	            "−0.800",
494	            "−0.659"
495	          ]
496	        ]
497	      }
498	    ],
499	    "figures": [],
500	    "analysis": "Prompt-type dependence 在 worst 档下被叠加到 scope limitations 上。Reviewer list: \"base models only,  temperature ∈ [0.5, 0.9], continuation chains preferred, Wikipedia seeds.\" 每增加一个条件性 qualifier， 方法的 practical scope 进一步收窄。Feature-drift inconsistency (不同 feature 在不同 prompt type 下  rank 不同) 是对 DDR unified framework 的直接挑战。\n\n\nContinuation chains 优于 elaboration 5.1 pp (0.781 vs 0.730)，但 elaboration/rewriting 有更高 depth  retention (0.986/0.939 vs 0.831)。这是一个 paradox：elaboration 保留更多 chain completeness 但 depth  signal 更弱——说明 signal strength 与 chain fidelity inversely correlated。Worst-tier reviewer 会 argue  \"the method works best on continuation chains — the simplest, least realistic generation paradigm. In more  naturalistic scenarios (elaboration, rewriting), where generators receive richer prompts and produce more  diverse output, the depth signal degrades by 5 pp.\" Feature drift inconsistency across prompt types  (entropy_mean 在 continuation 最强 -0.557 但 hapax 在 elaboration 最强 -0.828) 进一步 undermines DDR  作为 universal phenomenon 的叙事。LOPTO 显示 cross-prompt-type transfer 存在但不完美 (avg 0.753 vs  best within-type 0.781)——在实际应用中 prompt type 未知，reviewer 会 argue 应取 worst-case performance。\n"
501	  },
502	  {
503	    "name": "paraphrastic_comparison",
504	    "description": "构建 parallel paraphrasing chains 与 continuation chains 直接比较。测试 attractor convergence theory。 1000 seeds × Pythia-2.8B × 2 chain types。\n",
505	    "results": {
506	      "paraphrastic_cv_f1": 0.718,
507	      "continuation_cv_f1": 0.781,
508	      "paraphrastic_binary_f1": 0.661,
509	      "continuation_binary_f1": 0.694,
510	      "paraphrastic_drift_entropy_mean": -0.39,
511	      "paraphrastic_drift_hapax": -0.52,
512	      "paraphrastic_depth_retention": 0.992,
513	      "attractor_convergence_observed": true,
514	      "effective_classes_paraphrastic": 2,
515	      "delta_para_vs_cont_binary_pp": 3.3,
516	      "paraphrastic_gen2_vs_gen3_confusion": 0.62
517	    },
518	    "tables": [
519	      {
520	        "caption": "Paraphrastic vs non-paraphrastic chain comparison (Pythia-2.8B)",
521	        "rows": [
522	          [
523	            "Chain Type",
524	            "CV F1",
525	            "Binary F1",
526	            "Depth Retention",
527	            "entropy_mean ρ",
528	            "Effective Classes"
529	          ],
530	          [
531	            "Continuation (non-para)",
532	            "0.781",
533	            "0.694",
534	            "0.831",
535	            "−0.557",
536	            "3"
537	          ],
538	          [
539	            "Paraphrastic",
540	            "0.718",
541	            "0.661",
542	            "0.992",
543	            "−0.390",
544	            "~2"
545	          ],
546	          [
547	            "Δ",
548	            "+6.3 pp",
549	            "+3.3 pp",
550	            "−0.161",
551	            "−0.167",
552	            "+1"
553	          ]
554	        ]
555	      }
556	    ],
557	    "figures": [],
558	    "analysis": "Paraphrastic comparison 在 worst 档下 backfires。预期 non-paraphrastic chains 会显示 dramatically  different behavior，但 3.3 pp binary delta 不够 dramatic。反而证明 depth signal 是 generic generation  phenomenon 而非 non-paraphrastic chains 的 unique property。论文需要 reframe 为 \"depth signal exists  across chain types with moderate variation\" 而非 \"non-paraphrastic chains are special\"。\n\n\nParaphrastic chains 显示 attractor convergence (depth retention 0.992 ≈ 1.0)，但 depth signal 弱于  non-paraphrastic (binary F1 0.661 vs 0.694, −3.3 pp)。差距只有 3.3 pp——worst-tier reviewer 会 argue  这太小了不足以证明 non-paraphrastic chains 有 qualitatively different depth dynamics。\"Both chain types  show comparable (and modest) depth signal, suggesting the phenomenon is generic generation drift rather  than the differential depth response the authors claim.\" Paraphrastic chains 的 gen-2 vs gen-3 confusion  rate (0.62) 比 continuation (0.51) 更高，但 gen-0 vs gen-1 distinction 在两者中都 robust——说明 depth  signal 本质上是 binary (near-source vs deeper)，不是 true ordinal。Attractor convergence 被确认但  反而成为 negative evidence：\"if paraphrasting chains converge within ~3 iterations, and non-paraphrastic  chains show only 3.3 pp more depth signal, the 'novel' non-paraphrastic depth estimation adds negligible  value over studying convergence itself.\"\n"
559	  },
560	  {
561	    "name": "cross_model_chains",
562	    "description": "Cross-model chains (每个 depth step 使用不同 generator) vs single-model chains。5-gen subset,  generator-level LOGO。\n",
563	    "results": {
564	      "cross_model_binary_f1": 0.764,
565	      "cross_model_3class_f1": 0.789,
566	      "single_model_binary_f1": 0.694,
567	      "single_model_3class_f1": 0.762,
568	      "cross_model_logo_binary_f1": 0.83,
569	      "delta_binary_pp": 7.0,
570	      "delta_logo_pp": 13.6
571	    },
572	    "tables": [
573	      {
574	        "caption": "Cross-model vs single-model chain classification",
575	        "rows": [
576	          [
577	            "Setting",
578	            "Binary F1",
579	            "3-class F1",
580	            "LOGO Binary F1"
581	          ],
582	          [
583	            "Single-model chains",
584	            "0.694",
585	            "0.762",
586	            "0.694"
587	          ],
588	          [
589	            "Cross-model chains",
590	            "0.764",
591	            "0.789",
592	            "0.830"
593	          ],
594	          [
595	            "Δ",
596	            "+7.0 pp",
597	            "+2.7 pp",
598	            "+13.6 pp"
599	          ]
600	        ]
601	      }
602	    ],
603	    "figures": [],
604	    "analysis": "Cross-model improvement 是 double-edged sword。在 worst 档下，0.830 是 \"cheating number\" (conflates  depth with generator identity)，0.694 是 \"honest number\" (single-model, pure depth signal)。Paper 如果 同时 report 两者，reviewer 会 focus on 差距作为方法不是真正测量 depth 的 evidence。如果只 report 0.694， reviewer 会问 \"where are the cross-model results?\" 无法赢。\n\n\nCross-model chains binary F1 大幅高于 single-model (0.764 vs 0.694, +7 pp; LOGO 0.830 vs 0.694, +13.6 pp)。 Worst-tier reviewer 会 reframe 这为 devastating counter-evidence：\"The +13.6 pp LOGO improvement on  cross-model chains reveals that the method is primarily detecting generator switching (different model  fingerprints at each depth step) rather than generation depth. In the single-model case — which is the  harder, more interesting, and more realistic scenario for same-generator iterative contamination — F1 drops  back to the modest 0.694.\" Cross-model improvement 被解释为 trivially explained by OOD detection of  different model fingerprints。\"The authors' best result (0.830) is achieved on the easiest setting that  conflates depth with generator identity. The honest number for depth classification is 0.694, achieved  on single-model chains where the confound is absent.\" 这直接 undercuts the paper's strongest metric。\n"
605	  },
606	  {
607	    "name": "multi_domain_seeds",
608	    "description": "扩展到 4 domains: Wikipedia, news (CNN/DailyMail), academic (S2ORC), code。500 seeds × 5 depths per domain。 Cross-domain LOGO evaluation。\n",
609	    "results": {
610	      "wikipedia_binary_f1": 0.815,
611	      "news_binary_f1": 0.712,
612	      "news_binary_ci": [
613	        0.69,
614	        0.733
615	      ],
616	      "academic_binary_f1": 0.628,
617	      "academic_binary_ci": [
618	        0.603,
619	        0.652
620	      ],
621	      "code_binary_f1": 0.687,
622	      "code_binary_ci": [
623	        0.664,
624	        0.71
625	      ],
626	      "cross_domain_logo_binary_f1": 0.668,
627	      "max_gap_vs_wiki_pp": 18.7,
628	      "worst_domain": "academic",
629	      "best_domain": "wikipedia"
630	    },
631	    "tables": [
632	      {
633	        "caption": "Per-domain binary F1 (LOGO across generators)",
634	        "rows": [
635	          [
636	            "Domain",
637	            "Seeds",
638	            "Binary F1",
639	            "95% CI",
640	            "Δ vs Wiki"
641	          ],
642	          [
643	            "Wikipedia",
644	            "500",
645	            "0.815",
646	            "[0.796, 0.834]",
647	            "—"
648	          ],
649	          [
650	            "News",
651	            "500",
652	            "0.712",
653	            "[0.690, 0.733]",
654	            "−10.3 pp"
655	          ],
656	          [
657	            "Code",
658	            "500",
659	            "0.687",
660	            "[0.664, 0.710]",
661	            "−12.8 pp"
662	          ],
663	          [
664	            "Academic",
665	            "500",
666	            "0.628",
667	            "[0.603, 0.652]",
668	            "−18.7 pp"
669	          ],
670	          [
671	            "**Cross-domain LOGO**",
672	            "2000",
673	            "**0.668**",
674	            "[0.654, 0.682]",
675	            "—"
676	          ]
677	        ]
678	      }
679	    ],
680	    "figures": [],
681	    "analysis": "Domain dependence 在 worst 档下与 generator/temperature/instruct/edit 依赖 叠加。Reviewer 列出  cumulative conditions：\"base models only, temperature ∈ [0.5, 0.9], continuation preferred,  Wikipedia domain, no human editing, single reference model.\" 这是 increasingly narrow niche。 Academic domain failure 尤其 damaging 因为 paper motivation 中引用了 \"7–17% of recent scientific  papers contain LLM text\"——方法恰好在这个最相关 domain 上最弱。\n\n\nWikipedia (训练数据主 domain) 表现最好 (0.815)，academic 最差 (0.628)——gap 达 18.7 pp。在 t=0.7 下 academic binary F1 进一步降到 ~0.628，接近 chance + 0.128 margin。Cross-domain LOGO (train on 3, test  on 1) 降到 0.668。Worst-tier reviewer 会 argue：\"The method's performance is catastrophically  domain-dependent. Scientific text — precisely the domain where AI contamination is a pressing concern  per the authors' own motivation — yields near-chance binary F1 of 0.628. This domain sensitivity,  combined with the base-model and temperature restrictions, makes the method's scope so narrow as to  be practically meaningless.\" Academic domain 的 weak signal 可能因为 scientific text 的 formulaic  structure 本身就限制了 vocabulary diversity variation，使 surface features 失效。Cross-domain LOGO  0.668 加上 cross-generator LOGO 0.694 = cumulative degradation when both unknowns (generator + domain)  are combined，reviewer 会 estimate real-world F1 < 0.65。\n"
682	  },
683	  {
684	    "name": "finer_grained_ordinal",
685	    "description": "5-class ordinal classification (gen-0 through gen-4)。测试 depth resolution 是否超过 3-class。 Ordinal methods (CORAL, Frank-Hall) 比较。\n",
686	    "results": {
687	      "five_class_macro_f1": 0.498,
688	      "five_class_ci": [
689	        0.48,
690	        0.516
691	      ],
692	      "three_class_macro_f1": 0.762,
693	      "ordinal_coral_f1": 0.502,
694	      "ordinal_frank_hall_f1": 0.491,
695	      "gen0_recall": 0.92,
696	      "gen1_recall": 0.63,
697	      "gen2_recall": 0.41,
698	      "gen3_recall": 0.33,
699	      "gen4_recall": 0.29,
700	      "gen2_gen3_confusion_rate": 0.51,
701	      "gen3_gen4_confusion_rate": 0.48,
702	      "mean_absolute_depth_error": 0.89
703	    },
704	    "tables": [
705	      {
706	        "caption": "Ordinal depth classification resolution",
707	        "rows": [
708	          [
709	            "Granularity",
710	            "Method",
711	            "Macro F1",
712	            "Ordinal vs XGBoost"
713	          ],
714	          [
715	            "3-class",
716	            "XGBoost",
717	            "0.762",
718	            "—"
719	          ],
720	          [
721	            "5-class",
722	            "XGBoost",
723	            "0.498",
724	            "—"
725	          ],
726	          [
727	            "5-class",
728	            "CORAL",
729	            "0.502",
730	            "+0.4 pp"
731	          ],
732	          [
733	            "5-class",
734	            "Frank-Hall",
735	            "0.491",
736	            "−0.7 pp"
737	          ]
738	        ]
739	      },
740	      {
741	        "caption": "5-class per-depth recall",
742	        "rows": [
743	          [
744	            "Depth",
745	            "Recall",
746	            "Primary Confusion"
747	          ],
748	          [
749	            "gen-0",
750	            "0.92",
751	            "gen-1 (6%)"
752	          ],
753	          [
754	            "gen-1",
755	            "0.63",
756	            "gen-2 (24%)"
757	          ],
758	          [
759	            "gen-2",
760	            "0.41",
761	            "gen-1/gen-3 (26%/18%)"
762	          ],
763	          [
764	            "gen-3",
765	            "0.33",
766	            "gen-2/gen-4 (31%/21%)"
767	          ],
768	          [
769	            "gen-4",
770	            "0.29",
771	            "gen-3 (38%)"
772	          ]
773	        ]
774	      }
775	    ],
776	    "figures": [],
777	    "analysis": "5-class collapse 是 worst 档对 task formulation novelty 最有力的 attack。如果 depth signal 本质上 是 binary (+gen-1 略有区分)，那 \"generation depth classification\" 这个 task formulation 的 novelty  = 在 binary detection 上加了一个勉强可用的 third class。Ordinal methods 无改善进一步说明 depth  不是 ordinal quantity (continuous gradient)——而是 discrete jump from near-source to deep,  与 model collapse theory 的 gradual degradation 预测不一致。\n\n\n5-class F1 = 0.498 (random baseline ~0.20, so margin = 0.298)。Ordinal methods 无改善 (CORAL 0.502,  Frank-Hall 0.491)——depth signal 不具备 ordinal structure beyond coarse binning。Gen-0 recall 高  (0.92) 但 gen-2/3/4 几乎无法区分 (recall 0.29–0.41, confusion 48–51%)。Gen-0 的高 recall 来自  seed-sharing (原始人类文本与训练 features 有 distributional gap)——这不是 depth classification 而是  human-vs-machine detection。\nWorst-tier reviewer 会 argue：\"5-class F1 of 0.498 confirms depth signal is essentially binary: the  method distinguishes 'source-adjacent' (gen-0/1) from 'deep' (gen-2+) but cannot resolve within either  group. The 3-class formulation is not a principled task definition but an artifact of signal weakness —  it happens to be the granularity at which the method achieves non-trivial performance. The gen-2/3/4  confusion block (48–51% confusion rate) shows the 'generation depth' framing overclaims — this is  at most a binary-plus-one classifier.\"\n"
778	  },
779	  {
780	    "name": "human_edit_robustness",
781	    "description": "Robustness to simulated human edits: (A) random word replacement 5/10/20%,  (B) LLM-simulated light rephrasing (Qwen3-1.7B)。\n",
782	    "results": {
783	      "baseline_binary_f1": 0.695,
784	      "random_5pct_f1": 0.65,
785	      "random_10pct_f1": 0.614,
786	      "random_20pct_f1": 0.591,
787	      "llm_rephrase_binary_f1": 0.647,
788	      "llm_rephrase_multiclass_f1": 0.667,
789	      "llm_rephrase_edit_distance": 0.507,
790	      "degradation_5pct_pp": -4.5,
791	      "degradation_10pct_pp": -8.1,
792	      "degradation_20pct_pp": -10.4,
793	      "degradation_llm_pp": -4.5
794	    },
795	    "tables": [
796	      {
797	        "caption": "Robustness to simulated human edits",
798	        "rows": [
799	          [
800	            "Perturbation",
801	            "Binary F1",
802	            "Δ vs Baseline",
803	            "Edit Distance"
804	          ],
805	          [
806	            "None (baseline)",
807	            "0.695",
808	            "—",
809	            "0.0"
810	          ],
811	          [
812	            "Random 5%",
813	            "0.650",
814	            "−4.5 pp",
815	            "~0.05"
816	          ],
817	          [
818	            "Random 10%",
819	            "0.614",
820	            "−8.1 pp",
821	            "~0.10"
822	          ],
823	          [
824	            "Random 20%",
825	            "0.591",
826	            "−10.4 pp",
827	            "~0.20"
828	          ],
829	          [
830	            "LLM rephrase",
831	            "0.647",
832	            "−4.5 pp",
833	            "0.507"
834	          ]
835	        ]
836	      }
837	    ],
838	    "figures": [],
839	    "analysis": "Robustness 实验在 worst 档下是 lose-lose。Fragile result confirms depth signal 是 surface-level  且 easily disrupted。Combined with instruct degradation、temperature sensitivity、domain dependence， the cumulative fragility makes a devastating picture for any practical deployment argument。\n\n\n5% random replacement 造成 4.5 pp drop (0.695 → 0.650)。LLM rephrasing (edit distance 0.507,  avg 1.69 sentences replaced) 造成相同量级 drop (−4.5 pp → 0.647)。20% replacement 降到 0.591。\nWorst-tier reviewer 会 argue：\"In practice, AI-generated text is almost always edited before  publication — students edit LLM essays, writers revise LLM drafts, automated pipelines post-process  outputs. The method loses 4.5 pp F1 from light editing (50% edit distance ratio, ~1.7 sentences  changed), pushing the already-modest 0.695 baseline to 0.647. At this level, the method correctly  classifies depth for barely 65% of edited text — not actionable for any real-world application.\"\nDegradation is near-linear with perturbation intensity, suggesting the depth signal resides in  surface-level distributional properties easily disrupted by any text modification. This confirms  the \"vocabulary impoverishment repackaging\" critique—if the signal were capturing deeper structural  properties of recursive generation, it would be more robust to superficial edits.\n"
840	  },
841	  {
842	    "name": "ld_score_feature",
843	    "description": "添加 LD-Score (character-distribution signature) 作为第 8 个 feature。测试 character-level 信号 是否与 word/entropy features 互补。\n",
844	    "results": {
845	      "seven_feature_logo_f1": 0.798,
846	      "eight_feature_with_ld_f1": 0.802,
847	      "ld_score_alone_logo_f1": 0.721,
848	      "ld_score_alone_spearman": 0.794,
849	      "marginal_improvement_pp": 0.4,
850	      "feature_importance_ld": 0.022,
851	      "ld_score_cv_corrected_f1": 0.793
852	    },
853	    "tables": [
854	      {
855	        "caption": "LD-Score feature addition (3-class LOGO)",
856	        "rows": [
857	          [
858	            "Feature Set",
859	            "LOGO F1",
860	            "Δ"
861	          ],
862	          [
863	            "7 features (baseline)",
864	            "0.798",
865	            "—"
866	          ],
867	          [
868	            "7 + LD-Score",
869	            "0.802",
870	            "+0.4 pp"
871	          ],
872	          [
873	            "LD-Score only",
874	            "0.721",
875	            "—"
876	          ]
877	        ]
878	      }
879	    ],
880	    "figures": [],
881	    "analysis": "Minor experiment, minor result。在 worst 档下主要作为 \"all signals converge\" narrative 的  supporting evidence。不是 primary attack vector。\n\n\nLD-Score 单独 LOGO F1 = 0.721 (高于 FastDetectGPT 0.627 和 Binoculars 0.579，但低于 Avg-LogProb  0.765 和 7-feature 0.798)。加入后 marginal improvement 仅 0.4 pp (0.798 → 0.802)，feature  importance 排最后 (0.022)。LD-Score 的 high Spearman (0.794) 说明它有 ordinal depth signal， 但被 existing features 高度 subsume。\nWorst-tier reviewer 不会直接 attack 这个实验 (minor addition)，但会用它 reinforce vocabulary  impoverishment narrative：\"Adding a character-level feature provides negligible improvement (0.4 pp),  confirming that character, word, and NLL features all measure the same underlying phenomenon —  text simplification under recursive generation. The claimed 'differential depth response' across  feature types is an artifact of measuring the same signal at different linguistic levels.\"\n"
882	  },
883	  {
884	    "name": "end_to_end_classifier",
885	    "description": "QLoRA fine-tuned end-to-end depth classifier (OLMo-1B-Instruct, Qwen3-1.7B-Instruct,  及其 base model variants)。Within-distribution CV 和 cross-generator transfer。\n",
886	    "results": {
887	      "qlora_olmo_instruct_3class": 0.888,
888	      "qlora_olmo_instruct_3class_std": 0.007,
889	      "qlora_olmo_instruct_binary": 0.836,
890	      "qlora_olmo_instruct_binary_std": 0.01,
891	      "qlora_qwen_instruct_3class": 0.907,
892	      "qlora_qwen_instruct_binary": 0.867,
893	      "qlora_olmo_base_3class": 0.859,
894	      "qlora_olmo_base_binary": 0.793,
895	      "qlora_qwen_base_3class": 0.904,
896	      "qlora_qwen_base_binary": 0.86,
897	      "seven_feature_3class": 0.762,
898	      "seven_feature_binary": 0.694,
899	      "delta_3class_pp_olmo": 12.6,
900	      "delta_binary_pp_olmo": 14.2,
901	      "qlora_5class_f1": 0.575,
902	      "qlora_inference_cost_ratio": 47.0
903	    },
904	    "tables": [
905	      {
906	        "caption": "End-to-end (QLoRA) vs 7-feature ensemble",
907	        "rows": [
908	          [
909	            "Method",
910	            "Model",
911	            "3-class F1 (±std)",
912	            "Binary F1 (±std)",
913	            "Cost Ratio"
914	          ],
915	          [
916	            "7-feature XGBoost",
917	            "—",
918	            "0.762",
919	            "0.694",
920	            "1×"
921	          ],
922	          [
923	            "QLoRA",
924	            "OLMo-Instruct",
925	            "0.888 ± 0.007",
926	            "0.836 ± 0.010",
927	            "47×"
928	          ],
929	          [
930	            "QLoRA",
931	            "Qwen-Instruct",
932	            "0.907 ± 0.008",
933	            "0.867 ± 0.014",
934	            "47×"
935	          ],
936	          [
937	            "QLoRA",
938	            "OLMo-Base",
939	            "0.859 ± 0.004",
940	            "0.793 ± 0.010",
941	            "47×"
942	          ],
943	          [
944	            "QLoRA",
945	            "Qwen-Base",
946	            "0.904 ± 0.009",
947	            "0.860 ± 0.012",
948	            "47×"
949	          ]
950	        ]
951	      }
952	    ],
953	    "figures": [],
954	    "analysis": "End-to-end comparison 在 worst 档下 devastating。14-17 pp gap 说明 7-feature ensemble 遗漏了  substantial depth signal。论文的 positioning 是 efficiency vs absolute performance tradeoff，但  worst-tier reviewer 不买账：\"if the features miss this much signal, the contribution is not a  competitive method but an incomplete characterization.\" QLoRA instruct > base 也 undermine  \"instruct kills depth signal\" narrative——within-distribution instruct QLoRA actually works fine,  说明 instruct 限制的是 the specific features chosen, not the depth signal itself。\n\n\nQLoRA within-distribution 大幅碾压 7-feature：OLMo-Instruct 3-class 0.888 vs 0.762 (+12.6 pp)， binary 0.836 vs 0.694 (+14.2 pp)。Qwen-Instruct 更高 (3-class 0.907, binary 0.867)。Even base  models QLoRA (3-class 0.859/0.904) 远超 7-feature。5-class F1 = 0.575 也远超 7-feature 的 ~0.50。\nWorst-tier reviewer 会 cherry-pick within-distribution numbers：\"A straightforward QLoRA classifier  achieves 0.867 binary F1 (Qwen-Instruct), dwarfing the proposed method's 0.694 by 17.3 pp. Even  with the base model alone, QLoRA achieves 0.860 binary — a 16.6 pp advantage. The 7-feature  ensemble captures less than half the depth signal available in the text. The authors' efficiency  argument (47× cost ratio) is unconvincing: the QLoRA classifier runs on the same-sized model  already needed as a reference, and the 17 pp gap is too large to justify on cost grounds.\"\n论文的 rebuttal point 是 LOGO cross-generator transfer——QLoRA within-distribution 的 advantage  partly comes from overfitting to generator-specific patterns。但 worst-tier reviewer 已经 scored  low before considering this nuance。\n"
955	  },
956	  {
957	    "name": "text_length_control",
958	    "description": "Address text length confound: (A) length-depth correlation analysis, (B) length-normalized features,  (C) length-matched subsampling re-evaluation。\n",
959	    "results": {
960	      "spearman_length_depth": 0.12,
961	      "spearman_p": 0.001,
962	      "length_depth_correlation": "weak (|ρ|<0.14)",
963	      "length_matched_binary_f1": 0.724,
964	      "unmatched_binary_f1": 0.77,
965	      "delta_pp": -4.6,
966	      "normalized_ttr_trend_preserved": true,
967	      "normalized_hapax_trend_preserved": true,
968	      "normalized_rho_stronger": true,
969	      "length_is_primary_confound": false,
970	      "short_text_dropout_bias": true,
971	      "length_matched_f1_vs_logo_headline": "+3.0 pp above 0.694 LOGO"
972	    },
973	    "tables": [
974	      {
975	        "caption": "Length control analysis",
976	        "rows": [
977	          [
978	            "Condition",
979	            "Binary F1",
980	            "Δ vs Unmatched"
981	          ],
982	          [
983	            "Unmatched (original)",
984	            "0.770",
985	            "—"
986	          ],
987	          [
988	            "Length-normalized features",
989	            "0.748",
990	            "−2.2 pp"
991	          ],
992	          [
993	            "Length-matched subsample",
994	            "0.724",
995	            "−4.6 pp"
996	          ]
997	        ]
998	      }
999	    ],
1000	    "figures": [],
1001	    "analysis": "Length confound 不 kill paper 但 erode credibility。4.6 pp 降幅在 worst 档下被 generalize 为  \"confound-sensitive method\"——reviewer 会 question every reported number 是否被 uncontrolled  confounds inflate。这使 0.694 headline number 的 credibility 进一步下降。\n\n\nLength-depth correlation weak (ρ=0.12) 但 statistically significant (p=0.001)。Length-matched  binary F1 降 4.6 pp (0.770 → 0.724)——意味着 ~6% of signal 来自 text length。Normalized  features 的 depth trend 保持说明 depth signal 不完全是 length artifact，但 worst-tier reviewer  会 magnify 4.6 pp drop：\"After controlling for the most basic confound — text length — the method  loses 4.6 pp. How many other confounds (topic, style, vocabulary register) remain uncontrolled?  The 0.694 LOGO F1 may be further inflated by confounds the authors haven't tested.\"\nShort-text dropout bias 增加了 confound complexity：deeper depths 有更多 short text 被 pipeline  过滤掉，导致 surviving deeper text 是 systematically longer/more complete——这是 selection bias， 方法可能部分检测的是 \"which texts survived the pipeline filter\" 而非 true depth signal。\n"
1002	  },
1003	  {
1004	    "name": "large_scale_generator",
1005	    "description": "添加 Qwen3-8B-Base 测试 7B+ scale 的 depth signal。1000 seeds × 5 depths。与现有 6-gen  LOGO 集成。\n",
1006	    "results": {
1007	      "qwen3_8b_records": 4497,
1008	      "qwen3_8b_unique_seeds": 995,
1009	      "qwen3_8b_depth_dist": {
1010	        "0": 995,
1011	        "1": 979,
1012	        "2": 937,
1013	        "3": 831,
1014	        "4": 755
1015	      },
1016	      "logo_6gen_avg_f1": 0.789,
1017	      "qwen3_8b_logo_binary_f1": 0.647,
1018	      "qwen3_8b_logo_3class_f1": 0.683,
1019	      "qwen3_8b_within_cv_f1": 0.711,
1020	      "delta_vs_avg_pp": -10.6,
1021	      "hapax_rho_8b": -0.558,
1022	      "ttr_rho_8b": -0.542,
1023	      "entropy_mean_rho_8b": -0.475,
1024	      "feature_margin_compression_vs_avg": 0.72,
1025	      "ddr_pattern_preserved": true
1026	    },
1027	    "tables": [
1028	      {
1029	        "caption": "Scale effect: Qwen3-8B vs smaller generators",
1030	        "rows": [
1031	          [
1032	            "Generator",
1033	            "Size",
1034	            "LOGO Binary F1",
1035	            "hapax ρ",
1036	            "entropy_mean ρ",
1037	            "Feature compression"
1038	          ],
1039	          [
1040	            "Pythia-1B",
1041	            "1.0B",
1042	            "0.724",
1043	            "−0.65",
1044	            "−0.60",
1045	            "—"
1046	          ],
1047	          [
1048	            "Qwen3-1.7B",
1049	            "1.7B",
1050	            "0.698",
1051	            "−0.63",
1052	            "−0.60",
1053	            "—"
1054	          ],
1055	          [
1056	            "Pythia-2.8B",
1057	            "2.8B",
1058	            "0.711",
1059	            "−0.63",
1060	            "−0.60",
1061	            "—"
1062	          ],
1063	          [
1064	            "Qwen3-8B",
1065	            "8.0B",
1066	            "0.647",
1067	            "−0.56",
1068	            "−0.48",
1069	            "0.72×"
1070	          ],
1071	          [
1072	            "**Trend**",
1073	            "—",
1074	            "**Declining**",
1075	            "**Compressing**",
1076	            "**Compressing**",
1077	            "—"
1078	          ]
1079	        ]
1080	      }
1081	    ],
1082	    "figures": [],
1083	    "analysis": "Scale degradation 是 worst 档的 structural problem。论文诚实 report 这是 scope boundary，但  reviewer reframe：\"the scope boundary excludes all models that generate text at scale.\" 加上  instruct degradation (OLMo-Instruct LOGO 0.338)，方法的 applicable scope = base models ≤ 8B  at moderate temperature in Wikipedia-like domains without human editing。这个 niche 在 2026 年 没有 practical relevance。\n\n\nQwen3-8B LOGO binary F1 = 0.647——比 6-gen average 低 ~10.6 pp。Feature drift magnitudes 全面压缩  (hapax ρ −0.558 vs avg −0.647, compression ~0.72)。DDR pattern 仍然 preserved (drifting > stationary  分离 maintained)，但 magnitudes 显著 weakened。Within-CV F1 = 0.711 说明 8B 自身 depth signal 存在， 但 cross-generator transfer 弱 (LOGO 0.647)——smaller models 的 feature distribution 不 transfer well。\nWorst-tier reviewer 会 extrapolate：\"At 8B, the method shows substantial degradation (−10.6 pp vs  average, LOGO binary 0.647). This model is still far from frontier: GPT-4 (>100B), Claude 3 (unknown),  Llama-3-70B — the models generating the vast majority of AI text in practice — are 10–100× larger.  The observed linear degradation in log-scale model size (from 0.6B to 8B) projects to near-chance  performance at frontier scales, rendering the method irrelevant for the contamination problem it claims  to address.\" 这是 worst 档中 most damaging extrapolation——审稿人不需要实验数据就可以 argue。\nDepth distribution (gen-4 only 755/995 = 75.9% retention) 也说明 8B models 更容易产生 degenerate  output at depth (higher skip rate)——selection bias adds to confound concerns。\n"
1084	  },
1085	  {
1086	    "name": "ordinal_baseline_comparison",
1087	    "description": "Compare existing detector continuous scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb)  作为 ordinal depth predictors vs 7-feature ensemble。Multi-detector ensemble 比较。\n",
1088	    "results": {
1089	      "seven_feature_logo_f1": 0.798,
1090	      "seven_feature_ci": [
1091	        0.786,
1092	        0.799
1093	      ],
1094	      "avg_logprob_logo_f1": 0.765,
1095	      "avg_logprob_ci": [
1096	        0.616,
1097	        0.82
1098	      ],
1099	      "ld_score_logo_f1": 0.721,
1100	      "ld_score_ci": [
1101	        0.588,
1102	        0.77
1103	      ],
1104	      "fastdetectgpt_logo_f1": 0.627,
1105	      "fastdetectgpt_ci": [
1106	        0.511,
1107	        0.762
1108	      ],
1109	      "binoculars_logo_f1": 0.579,
1110	      "binoculars_ci": [
1111	        0.405,
1112	        0.664
1113	      ],
1114	      "bootstrap_7feat_vs_avglogprob_delta": 0.033,
1115	      "bootstrap_7feat_vs_avglogprob_p": 0.0,
1116	      "multi_detector_ensemble_f1": 0.708,
1117	      "multi_det_4det_plus_surface_3class": 0.795,
1118	      "multi_det_binary": 0.708,
1119	      "seven_feature_binary": 0.705,
1120	      "multi_det_vs_7feat_binary_pp": 0.3,
1121	      "multi_det_inference_cost": "2.4×"
1122	    },
1123	    "tables": [
1124	      {
1125	        "caption": "Ordinal depth classification: 7-feature vs existing detector baselines (LOGO)",
1126	        "rows": [
1127	          [
1128	            "Method",
1129	            "3-class F1",
1130	            "95% CI",
1131	            "Binary F1",
1132	            "Δ vs 7-feat 3-class",
1133	            "Bootstrap p"
1134	          ],
1135	          [
1136	            "**7-feature ensemble**",
1137	            "**0.798**",
1138	            "[0.786, 0.799]",
1139	            "**0.705**",
1140	            "—",
1141	            "—"
1142	          ],
1143	          [
1144	            "Avg-LogProb",
1145	            "0.765",
1146	            "[0.616, 0.820]",
1147	            "0.695",
1148	            "−3.3 pp",
1149	            "<0.001"
1150	          ],
1151	          [
1152	            "LD-Score",
1153	            "0.721",
1154	            "[0.588, 0.770]",
1155	            "0.672",
1156	            "−7.7 pp",
1157	            "<0.001"
1158	          ],
1159	          [
1160	            "FastDetectGPT",
1161	            "0.627",
1162	            "[0.511, 0.762]",
1163	            "0.601",
1164	            "−17.1 pp",
1165	            "<0.001"
1166	          ],
1167	          [
1168	            "Binoculars",
1169	            "0.579",
1170	            "[0.405, 0.664]",
1171	            "0.558",
1172	            "−21.9 pp",
1173	            "<0.001"
1174	          ],
1175	          [
1176	            "4-det + surface",
1177	            "0.795",
1178	            "[0.781, 0.808]",
1179	            "0.708",
1180	            "−0.3 pp",
1181	            "0.72"
1182	          ]
1183	        ]
1184	      }
1185	    ],
1186	    "figures": [],
1187	    "analysis": "Baseline comparison 在 worst 档下是 most dangerous experiment。在 binary metric (primary) 下， 7-feature (0.705) 和 multi-det (0.708) 几乎无差——reviewer 会 conclude 7-feature 的 contribution  不足以 justify publication。3-class 下 7-feature 略优 (0.798 vs 0.795)，但差距 near-zero。 论文 contribution 被 reduce 为：\"a modestly different feature set that performs comparably to  existing detector ensembles, with an interpretive framework (DDR) that may or may not correspond  to a real phenomenon.\" 这是 worst 档下 paper's reason to exist 被直接 challenged 的实验。\n\n7-feature LOGO F1 = 0.798 (3-class) 显著优于最佳 single detector Avg-LogProb (0.765, δ=3.3 pp,  p < 0.001)。但 single detector CIs 极宽 (Avg-LogProb CI [0.616, 0.820] 跨越 7-feature point  estimate)——说明 per-generator variance 极高。Multi-detector ensemble (4-det + surface) 达到  3-class 0.795 和 binary 0.708 vs 7-feature binary 0.705——仅 0.3 pp 差距。\nWorst-tier reviewer 会 argue：\"The 7-feature ensemble achieves 3.3 pp over Avg-LogProb, but this  single number (average log probability) requires only basic LM inference — no feature engineering,  no reference model selection, no DDR framework. The tiny margin and overlapping confidence intervals  suggest the elaborate DDR characterization provides minimal practical benefit over a trivial baseline.  Moreover, a multi-detector ensemble matches the 7-feature binary F1 within 0.3 pp. The contribution  reduces to: 'a slightly different way to achieve what existing tools already achieve, with a novel  but unvalidated interpretive framework (DDR).'\"\nBootstrap p < 0.001 for 7-feat vs Avg-LogProb 在 3-class setting 是 significant。但 binary  setting 差距 near-zero (0.705 vs 0.708)——primary metric 下 7-feature 反而略低于 multi-detector。\n"
1188	  }
1189	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8d78a1-eeb3-496f-ac5f-bfd40524b20d",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "84ee7a20-2348-4c95-8b8f-53a9ce7fa576",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"MVP 数据上三部分分析：(A) Feature ablation: reference-only vs surface-only vs full 7-feature, XGBoost 5-fold CV； (B) 每个 feature 的 depth trend (slope, R², Spearman ρ)；(C) Pythia-410M perplexity pre-validation for Claim 3。\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.82,\n      \"surface_only_f1\": 0.763,\n      \"reference_only_f1\": 0.719,\n      \"surface_vs_full_gap_pp\": 5.7,\n      \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\",\n      \"mcnemar_full_vs_surface_p\": 0.0,\n      \"mcnemar_full_vs_ref_p\": 0.0,\n      \"h2_features\": \"entropy_mean, ttr, hapax_ratio\",\n      \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\",\n      \"hapax_ratio_slope\": -0.063,\n      \"hapax_ratio_r2\": 0.88,\n      \"hapax_ratio_rho\": -0.63,\n      \"ttr_slope\": -0.041,\n      \"ttr_r2\": 0.82,\n      \"ttr_rho\": -0.61,\n      \"entropy_mean_slope\": -0.089,\n      \"entropy_mean_r2\": 0.79,\n      \"entropy_mean_rho\": -0.6,\n      \"entropy_std_slope\": -0.031,\n      \"entropy_std_r2\": 0.41,\n      \"entropy_std_rho\": -0.2,\n      \"tail_decay_slope\": 0.003,\n      \"tail_decay_r2\": 0.04,\n      \"tail_decay_rho\": 0.04,\n      \"entropy_max_slope\": 0.008,\n      \"entropy_max_r2\": 0.07,\n      \"entropy_max_rho\": 0.05,\n      \"median_ppl_by_depth\": [\n        13.5,\n        4.96,\n        3.0,\n        2.07,\n        1.72\n      ]\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Feature ablation: 5-fold CV macro F1 on MVP data (Pythia-2.8B, ~4600 records)\",\n        \"rows\": [\n          [\n            \"Feature Set\",\n            \"Macro F1\",\n            \"95% CI\",\n            \"Δ vs Full\"\n          ],\n          [\n            \"Full (7 features)\",\n            \"0.820\",\n            \"[0.807, 0.833]\",\n            \"—\"\n          ],\n          [\n            \"Surface-only (TTR + hapax)\",\n            \"0.763\",\n            \"[0.747, 0.774]\",\n            \"−5.7 pp\"\n          ],\n          [\n            \"Reference-only (5 entropy)\",\n            \"0.719\",\n            \"[0.706, 0.733]\",\n            \"−10.1 pp\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Per-feature depth trend (linear regression on depth 0–4)\",\n        \"rows\": [\n          [\n            \"Feature\",\n            \"Category\",\n            \"Slope\",\n            \"R²\",\n            \"Spearman ρ\"\n          ],\n          [\n            \"hapax_ratio\",\n            \"Drifting\",\n            \"−0.063\",\n            \"0.88\",\n            \"−0.63\"\n          ],\n          [\n            \"TTR\",\n            \"Drifting\",\n            \"−0.041\",\n            \"0.82\",\n            \"−0.61\"\n          ],\n          [\n            \"entropy_mean\",\n            \"Drifting\",\n            \"−0.089\",\n            \"0.79\",\n            \"−0.60\"\n          ],\n          [\n            \"entropy_std\",\n            \"Ambiguous\",\n            \"−0.031\",\n            \"0.41\",\n            \"−0.20\"\n          ],\n          [\n            \"entropy_min\",\n            \"Stationary\",\n            \"−0.018\",\n            \"0.22\",\n            \"−0.15\"\n          ],\n          [\n            \"tail_decay\",\n            \"Stationary\",\n            \"+0.003\",\n            \"0.04\",\n            \"+0.04\"\n          ],\n          [\n            \"entropy_max\",\n            \"Stationary\",\n            \"+0.008\",\n            \"0.07\",\n            \"+0.05\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 worst 档下，ablation 的核心问题是 surface features 太强：93% signal retention 意味着 reference features 的  independent contribution minimal。Reviewer 会写：\\\"The proposed DDR framework adds substantial complexity (reference  model inference, 5 entropy features) for a 5.7 pp improvement over two simple vocabulary diversity metrics. The claim  of 'complementary signal' is technically supported but practically marginal.\\\" entropy_std 的 ambiguous status  (R²=0.41, ρ=-0.20) 破坏 DDR clean binary split 的叙事核心，reviewer 会 argue 这是 continuous degradation  而非 bimodal response。\\n\\n\\nSurface-only (0.763) 达到 full (0.820) 的 93%——审稿人会 argue reference features 只是 marginal add-on，不构成独立 contribution。虽然 McNemar p=0 确认显著性，但 worst-tier reviewer 会指出 5.7 pp 差距中 hapax_ratio 单个 surface  feature 就占据了 0.289 importance（plan-002-eval 实测），说明 reference features 被 surface features 的 vocabulary  impoverishment 信号 dominate。entropy_std 的 R²=0.41 处于 drifting/stationary 灰色地带，reviewer 会 argue DDR  不是 bimodal dichotomy 而是 continuous gradient——\\\"the clean split between drifting and stationary is an artifact of  thresholding a continuous degradation spectrum.\\\" 所有 drifting features (hapax, TTR, entropy_mean) 沿同一方向单调递减， reviewer 会 argue 这就是 well-known vocabulary impoverishment 的多种测量维度，不是新现象。Perplexity 单调递减  (13.50→1.72) 只是说明 recursive generation 使 text 对 reference model 更 predictable——这是 trivial observation。\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"扩展到 8 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Llama-3.2-3B, Qwen3-8B,  Mistral-7B-v0.3) 的 LOGO 评估。~37K records。\\n\",\n    \"results\": {\n      \"total_records\": 37500,\n      \"generators\": 8,\n      \"families\": 5,\n      \"logo_avg_3class_f1\": 0.762,\n      \"logo_avg_3class_ci\": [\n        0.758,\n        0.766\n      ],\n      \"logo_avg_binary_f1\": 0.694,\n      \"logo_binary_ci\": [\n        0.688,\n        0.7\n      ],\n      \"lofo_binary_f1\": 0.686,\n      \"per_gen_binary_f1\": {\n        \"pythia-1b\": 0.724,\n        \"pythia-2.8b\": 0.711,\n        \"qwen3-0.6b\": 0.702,\n        \"qwen3-1.7b\": 0.698,\n        \"olmo-2-1b\": 0.679,\n        \"llama-3.2-3b\": 0.688,\n        \"qwen3-8b\": 0.647,\n        \"mistral-7b\": 0.633\n      },\n      \"per_gen_range_pp\": 9.1,\n      \"fn_rate_of_binary_errors\": 0.86,\n      \"worst_gen\": \"mistral-7b-v0.3\",\n      \"best_gen\": \"pythia-1b\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Leave-one-generator-out (LOGO) binary F1 (gen-1 vs gen-2+, 8 generators)\",\n        \"rows\": [\n          [\n            \"Held-out Generator\",\n            \"Family\",\n            \"Size\",\n            \"Binary F1\",\n            \"95% CI\"\n          ],\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            \"1.0B\",\n            \"0.724\",\n            \"[0.707, 0.741]\"\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            \"2.8B\",\n            \"0.711\",\n            \"[0.693, 0.729]\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"Qwen\",\n            \"0.6B\",\n            \"0.702\",\n            \"[0.682, 0.722]\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Qwen\",\n            \"1.7B\",\n            \"0.698\",\n            \"[0.678, 0.718]\"\n          ],\n          [\n            \"Llama-3.2-3B\",\n            \"Llama\",\n            \"3.0B\",\n            \"0.688\",\n            \"[0.668, 0.708]\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1.5B\",\n            \"0.679\",\n            \"[0.658, 0.700]\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"Qwen\",\n            \"8.0B\",\n            \"0.647\",\n            \"[0.624, 0.670]\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"Mistral\",\n            \"7.0B\",\n            \"0.633\",\n            \"[0.609, 0.657]\"\n          ],\n          [\n            \"**Average**\",\n            \"—\",\n            \"—\",\n            \"**0.694**\",\n            \"[0.688, 0.700]\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Leave-one-family-out (LOFO) binary F1\",\n        \"rows\": [\n          [\n            \"Held-out Family\",\n            \"Binary F1\",\n            \"Δ vs LOGO\"\n          ],\n          [\n            \"Pythia\",\n            \"0.668\",\n            \"−2.6 pp\"\n          ],\n          [\n            \"Qwen\",\n            \"0.672\",\n            \"−2.2 pp\"\n          ],\n          [\n            \"OLMo\",\n            \"0.714\",\n            \"+2.0 pp\"\n          ],\n          [\n            \"Llama\",\n            \"0.701\",\n            \"+0.7 pp\"\n          ],\n          [\n            \"Mistral\",\n            \"0.673\",\n            \"−2.1 pp\"\n          ],\n          [\n            \"**Average**\",\n            \"**0.686**\",\n            \"**−0.8 pp**\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"0.694 是论文 headline number，也是 worst 档审稿人的 primary attack target。两个结构性问题：(1) margin over  chance (0.194) 太薄——在 noisy real-world setting 下可能进一步缩小到 near-chance；(2) per-gen range 9.1 pp  说明 performance 高度 generator-dependent，最差的大模型们恰好是最重要的模型。审稿人会 write：\\\"At the models  that actually generate content at scale (7B+), the method achieves binary F1 of 0.633–0.647, which is  not meaningfully above random guessing for a balanced binary task.\\\"\\n\\n\\nLOGO binary F1 = 0.694，margin over random baseline (0.50) 仅 0.194。在 balanced binary 任务中，这意味着  每 10 个 gen-2+ 样本中约 3 个被误判为 gen-1。Per-gen range 达 9.1 pp (Pythia-1B 0.724 vs Mistral-7B 0.633)， 审稿人会 argue 方法 performance 高度依赖 generator identity，且最差的恰好是两个较大模型 (Mistral-7B 0.633,  Qwen3-8B 0.647)——暗示 scale 上升时方法失效。LOFO binary F1 = 0.686 比 LOGO 低 0.8 pp，说明跨 family 泛化 存在但 margin 更薄。86% 的 binary errors 集中在 FN (gen-2+ 被判为 gen-1)——方法系统性地 under-detect deeper  generation，恰好是实际应用中最需要检出的样本。Reviewer 会写：\\\"The primary metric of 0.694 offers a margin of  less than 0.20 over random guessing. While statistically significant, this margin is far too thin for any  practical deployment, particularly given the 9 pp variance across generators and the systematic FN bias  toward deeper generations.\\\"\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"测试 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model (替代 Pythia-410M)。验证 DDR drift 是否在  非 Pythia reference 下持续存在。Claim 2 的关键 falsification test。\\n\",\n    \"results\": {\n      \"logo_f1_pythia_ref\": 0.803,\n      \"logo_f1_olmo_ref\": 0.807,\n      \"logo_f1_qwen_ref\": 0.816,\n      \"entropy_mean_drift_pythia_range\": [\n        -1.19,\n        -1.4\n      ],\n      \"entropy_mean_drift_olmo_range\": [\n        -0.61,\n        -0.91\n      ],\n      \"entropy_mean_drift_qwen_range\": [\n        -0.96,\n        -1.35\n      ],\n      \"drift_direction_consistent\": true,\n      \"shape_stationary_all_refs\": true,\n      \"drift_magnitude_ratio_olmo_vs_pythia\": 0.55,\n      \"qwen_ref_gives_best_logo\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-reference-model DDR comparison\",\n        \"rows\": [\n          [\n            \"Reference Model\",\n            \"Size\",\n            \"LOGO F1\",\n            \"entropy_mean avg ρ\",\n            \"hapax avg ρ\",\n            \"tail_decay avg ρ\",\n            \"Drift magnitude range\"\n          ],\n          [\n            \"Pythia-410M\",\n            \"410M\",\n            \"0.803\",\n            \"−0.60\",\n            \"−0.63\",\n            \"+0.04\",\n            \"[−1.19, −1.40]\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            \"0.807\",\n            \"−0.50\",\n            \"−0.58\",\n            \"+0.07\",\n            \"[−0.61, −0.91]\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            \"0.816\",\n            \"−0.56\",\n            \"−0.61\",\n            \"+0.05\",\n            \"[−0.96, −1.35]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 worst 档中最 subtle 的攻击向量。实验技术上通过了 falsification (drift direction consistent, shape  stationary)，但 magnitude dependence on reference model 给了审稿人一个 elegant reframe：\\\"DDR is not a  pure property of recursive generation but a joint function of generation and reference model. The authors'  claim of an 'intrinsic differential response' is overstated—it's a measurement-relative phenomenon.\\\"  这不会导致 reject 但会让 Claim 2 的 contribution 评估降半档。\\n\\n\\nFalsification test 技术上通过了——drift direction 在所有 reference models 下一致 (所有 entropy_mean ρ < 0， 所有 shape features |ρ| < 0.10)。但 drift magnitude 高度依赖 reference model：OLMo reference 的 entropy_mean  drift 仅为 Pythia 的 ~55% (-0.61 vs -1.19 on weakest generator)。LOGO F1 across references 差异小  (0.803–0.816)——但 worst-tier reviewer 会 reframe 这为：\\\"The classification performance is similar regardless  of reference model, but the underlying DDR characterization changes substantially. This means DDR magnitude  is as much a function of reference-generator mismatch as of recursive depth. The phenomenon the authors claim  to study is partially an artifact of their measurement instrument.\\\" 技术上不 kill Claim 2，但 interpretive  precision 被严重削弱。Qwen reference 给出最高 LOGO 说明 reference choice matters——在 worst 档下这被视为  \\\"the method's performance depends on an engineering choice (reference model) that has no principled selection  criterion.\\\"\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune OLMo-1B on depth-stratified data subsets。3 random seeds, bootstrap CIs。Compare depth-aware  filtering vs binary baselines vs random subsampling。Sample-count-matched comparison。\\n\",\n    \"results\": {\n      \"all_data_ppl_mean\": 2.335,\n      \"all_data_ppl_std\": 0.0003,\n      \"size_matched_ppl_mean\": 2.367,\n      \"size_matched_ppl_std\": 0.0003,\n      \"depth01_ppl_mean\": 2.387,\n      \"depth01_ppl_std\": 0.0004,\n      \"binary_filtered_ppl_mean\": 2.389,\n      \"binary_filtered_ppl_std\": 0.0006,\n      \"depth0_only_ppl_mean\": 2.681,\n      \"depth0_only_ppl_std\": 0.0006,\n      \"tost_p_2pct\": 0.00011,\n      \"tost_p_1pct\": 0.087,\n      \"ranking\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\",\n      \"seed_variance\": \"极小 (<0.002 within variant)\",\n      \"cohens_d_sizematched_vs_depth01\": 0.42\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Downstream CLM perplexity by training data depth composition (3 seeds, OLMo-1B)\",\n        \"rows\": [\n          [\n            \"Variant\",\n            \"Train Size\",\n            \"PPL (mean ± std)\",\n            \"Δ vs Size-matched\",\n            \"TOST ±2% p\"\n          ],\n          [\n            \"All depths\",\n            \"12,299\",\n            \"2.335 ± 0.0003\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Size-matched random\",\n            \"3,951\",\n            \"2.367 ± 0.0003\",\n            \"ref\",\n            \"ref\"\n          ],\n          [\n            \"Depth 0+1 only\",\n            \"3,951\",\n            \"2.387 ± 0.0004\",\n            \"+0.020\",\n            \"1.1×10⁻⁴\"\n          ],\n          [\n            \"Binary filtered\",\n            \"3,951\",\n            \"2.389 ± 0.0006\",\n            \"+0.022\",\n            \"8.7×10⁻⁵\"\n          ],\n          [\n            \"Depth 0 only\",\n            \"797\",\n            \"2.681 ± 0.0006\",\n            \"+0.314\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative finding 是 worst 档的 strategic vulnerability。论文 framing 为 \\\"diagnostic not curative\\\"  是诚实的，但 worst-tier reviewers 会 argue diagnostic value 未被证明——\\\"where is the use case where  knowing depth matters?\\\" 这与 Claim 1 的 practical motivation 形成 circular problem：如果 depth 没有 downstream impact，为什么要分类 depth？论文需要 reframe 为 understanding contribution (DDR characterization)  而非 any form of utility，但这 reframe 在 worst 档下被视为 post-hoc rationalization。\\n\\n\\nNegative finding 极其 clean 且 robust：depth-aware filtering 与 random subsampling 在 ±2% margin 内  equivalence 被 TOST 确认 (p=1.1×10⁻⁴)。Cross-seed variance < 0.002 意味着这个 negative finding 是  highly reliable——不是 noisy null 而是 genuine equivalence。Ranking 显示更多数据 always better (all <  size_matched)，depth filtering 反而 slightly worse than random (2.387 vs 2.367)——意味着 depth-aware  curation 不仅没有帮助，还可能因为丢弃了 useful training signal 而 slightly hurt。\\n审稿人在 worst 档下会 weaponize 这个结果：\\\"The authors' own Claim 3 establishes that generation depth  is informationally vacuous for the most obvious downstream application. If depth information provides  zero utility for data curation — indeed, depth-filtered data is slightly WORSE than random — then the  practical motivation for depth classification collapses entirely. The paper's pivot to 'diagnostic tool'  is an ad hoc rescue, not a designed contribution.\\\" TOST 在 ±1% margin 不显著 (p=0.087) 会被注意到但 不 weaponize (论文已选 ±2%)。depth0_only 的高 perplexity (2.681) 只证明 human vs machine 有区别—— 这是 binary detection 已解决的问题，不支持 depth classification 的 incremental value。\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Compare continuation vs elaboration vs inspired_rewriting chains。1000 seeds × Pythia-2.8B × 3 prompt types。\\n\",\n    \"results\": {\n      \"cv_f1_continuation\": 0.781,\n      \"cv_f1_elaboration\": 0.73,\n      \"cv_f1_rewriting\": 0.737,\n      \"lopto_avg_f1\": 0.753,\n      \"lopto_held_out_cont\": 0.762,\n      \"lopto_held_out_elab\": 0.762,\n      \"lopto_held_out_rewrite\": 0.734,\n      \"depth_retention_cont\": 0.831,\n      \"depth_retention_elab\": 0.986,\n      \"depth_retention_rewrite\": 0.939,\n      \"drift_hapax_cont\": -0.74,\n      \"drift_hapax_elab\": -0.828,\n      \"drift_hapax_rewrite\": -0.8,\n      \"drift_entropy_mean_cont\": -0.557,\n      \"drift_entropy_mean_elab\": -0.471,\n      \"drift_entropy_mean_rewrite\": -0.477,\n      \"spearman_ttr_cont\": -0.629,\n      \"spearman_ttr_elab\": -0.666,\n      \"spearman_ttr_rewrite\": -0.659,\n      \"cross_prompt_type_range_pp\": 5.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Per-prompt-type classification and drift statistics (Pythia-2.8B)\",\n        \"rows\": [\n          [\n            \"Prompt Type\",\n            \"CV F1\",\n            \"LOPTO F1\",\n            \"Depth Retention\",\n            \"entropy_mean ρ\",\n            \"hapax ρ\",\n            \"TTR ρ\"\n          ],\n          [\n            \"Continuation\",\n            \"0.781\",\n            \"0.762\",\n            \"0.831\",\n            \"−0.557\",\n            \"−0.740\",\n            \"−0.629\"\n          ],\n          [\n            \"Elaboration\",\n            \"0.730\",\n            \"0.762\",\n            \"0.986\",\n            \"−0.471\",\n            \"−0.828\",\n            \"−0.666\"\n          ],\n          [\n            \"Inspired Rewriting\",\n            \"0.737\",\n            \"0.734\",\n            \"0.939\",\n            \"−0.477\",\n            \"−0.800\",\n            \"−0.659\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt-type dependence 在 worst 档下被叠加到 scope limitations 上。Reviewer list: \\\"base models only,  temperature ∈ [0.5, 0.9], continuation chains preferred, Wikipedia seeds.\\\" 每增加一个条件性 qualifier， 方法的 practical scope 进一步收窄。Feature-drift inconsistency (不同 feature 在不同 prompt type 下  rank 不同) 是对 DDR unified framework 的直接挑战。\\n\\n\\nContinuation chains 优于 elaboration 5.1 pp (0.781 vs 0.730)，但 elaboration/rewriting 有更高 depth  retention (0.986/0.939 vs 0.831)。这是一个 paradox：elaboration 保留更多 chain completeness 但 depth  signal 更弱——说明 signal strength 与 chain fidelity inversely correlated。Worst-tier reviewer 会 argue  \\\"the method works best on continuation chains — the simplest, least realistic generation paradigm. In more  naturalistic scenarios (elaboration, rewriting), where generators receive richer prompts and produce more  diverse output, the depth signal degrades by 5 pp.\\\" Feature drift inconsistency across prompt types  (entropy_mean 在 continuation 最强 -0.557 但 hapax 在 elaboration 最强 -0.828) 进一步 undermines DDR  作为 universal phenomenon 的叙事。LOPTO 显示 cross-prompt-type transfer 存在但不完美 (avg 0.753 vs  best within-type 0.781)——在实际应用中 prompt type 未知，reviewer 会 argue 应取 worst-case performance。\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"构建 parallel paraphrasing chains 与 continuation chains 直接比较。测试 attractor convergence theory。 1000 seeds × Pythia-2.8B × 2 chain types。\\n\",\n    \"results\": {\n      \"paraphrastic_cv_f1\": 0.718,\n      \"continuation_cv_f1\": 0.781,\n      \"paraphrastic_binary_f1\": 0.661,\n      \"continuation_binary_f1\": 0.694,\n      \"paraphrastic_drift_entropy_mean\": -0.39,\n      \"paraphrastic_drift_hapax\": -0.52,\n      \"paraphrastic_depth_retention\": 0.992,\n      \"attractor_convergence_observed\": true,\n      \"effective_classes_paraphrastic\": 2,\n      \"delta_para_vs_cont_binary_pp\": 3.3,\n      \"paraphrastic_gen2_vs_gen3_confusion\": 0.62\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Paraphrastic vs non-paraphrastic chain comparison (Pythia-2.8B)\",\n        \"rows\": [\n          [\n            \"Chain Type\",\n            \"CV F1\",\n            \"Binary F1\",\n            \"Depth Retention\",\n            \"entropy_mean ρ\",\n            \"Effective Classes\"\n          ],\n          [\n            \"Continuation (non-para)\",\n            \"0.781\",\n            \"0.694\",\n            \"0.831\",\n            \"−0.557\",\n            \"3\"\n          ],\n          [\n            \"Paraphrastic\",\n            \"0.718\",\n            \"0.661\",\n            \"0.992\",\n            \"−0.390\",\n            \"~2\"\n          ],\n          [\n            \"Δ\",\n            \"+6.3 pp\",\n            \"+3.3 pp\",\n            \"−0.161\",\n            \"−0.167\",\n            \"+1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Paraphrastic comparison 在 worst 档下 backfires。预期 non-paraphrastic chains 会显示 dramatically  different behavior，但 3.3 pp binary delta 不够 dramatic。反而证明 depth signal 是 generic generation  phenomenon 而非 non-paraphrastic chains 的 unique property。论文需要 reframe 为 \\\"depth signal exists  across chain types with moderate variation\\\" 而非 \\\"non-paraphrastic chains are special\\\"。\\n\\n\\nParaphrastic chains 显示 attractor convergence (depth retention 0.992 ≈ 1.0)，但 depth signal 弱于  non-paraphrastic (binary F1 0.661 vs 0.694, −3.3 pp)。差距只有 3.3 pp——worst-tier reviewer 会 argue  这太小了不足以证明 non-paraphrastic chains 有 qualitatively different depth dynamics。\\\"Both chain types  show comparable (and modest) depth signal, suggesting the phenomenon is generic generation drift rather  than the differential depth response the authors claim.\\\" Paraphrastic chains 的 gen-2 vs gen-3 confusion  rate (0.62) 比 continuation (0.51) 更高，但 gen-0 vs gen-1 distinction 在两者中都 robust——说明 depth  signal 本质上是 binary (near-source vs deeper)，不是 true ordinal。Attractor convergence 被确认但  反而成为 negative evidence：\\\"if paraphrasting chains converge within ~3 iterations, and non-paraphrastic  chains show only 3.3 pp more depth signal, the 'novel' non-paraphrastic depth estimation adds negligible  value over studying convergence itself.\\\"\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains (每个 depth step 使用不同 generator) vs single-model chains。5-gen subset,  generator-level LOGO。\\n\",\n    \"results\": {\n      \"cross_model_binary_f1\": 0.764,\n      \"cross_model_3class_f1\": 0.789,\n      \"single_model_binary_f1\": 0.694,\n      \"single_model_3class_f1\": 0.762,\n      \"cross_model_logo_binary_f1\": 0.83,\n      \"delta_binary_pp\": 7.0,\n      \"delta_logo_pp\": 13.6\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-model vs single-model chain classification\",\n        \"rows\": [\n          [\n            \"Setting\",\n            \"Binary F1\",\n            \"3-class F1\",\n            \"LOGO Binary F1\"\n          ],\n          [\n            \"Single-model chains\",\n            \"0.694\",\n            \"0.762\",\n            \"0.694\"\n          ],\n          [\n            \"Cross-model chains\",\n            \"0.764\",\n            \"0.789\",\n            \"0.830\"\n          ],\n          [\n            \"Δ\",\n            \"+7.0 pp\",\n            \"+2.7 pp\",\n            \"+13.6 pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model improvement 是 double-edged sword。在 worst 档下，0.830 是 \\\"cheating number\\\" (conflates  depth with generator identity)，0.694 是 \\\"honest number\\\" (single-model, pure depth signal)。Paper 如果 同时 report 两者，reviewer 会 focus on 差距作为方法不是真正测量 depth 的 evidence。如果只 report 0.694， reviewer 会问 \\\"where are the cross-model results?\\\" 无法赢。\\n\\n\\nCross-model chains binary F1 大幅高于 single-model (0.764 vs 0.694, +7 pp; LOGO 0.830 vs 0.694, +13.6 pp)。 Worst-tier reviewer 会 reframe 这为 devastating counter-evidence：\\\"The +13.6 pp LOGO improvement on  cross-model chains reveals that the method is primarily detecting generator switching (different model  fingerprints at each depth step) rather than generation depth. In the single-model case — which is the  harder, more interesting, and more realistic scenario for same-generator iterative contamination — F1 drops  back to the modest 0.694.\\\" Cross-model improvement 被解释为 trivially explained by OOD detection of  different model fingerprints。\\\"The authors' best result (0.830) is achieved on the easiest setting that  conflates depth with generator identity. The honest number for depth classification is 0.694, achieved  on single-model chains where the confound is absent.\\\" 这直接 undercuts the paper's strongest metric。\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"扩展到 4 domains: Wikipedia, news (CNN/DailyMail), academic (S2ORC), code。500 seeds × 5 depths per domain。 Cross-domain LOGO evaluation。\\n\",\n    \"results\": {\n      \"wikipedia_binary_f1\": 0.815,\n      \"news_binary_f1\": 0.712,\n      \"news_binary_ci\": [\n        0.69,\n        0.733\n      ],\n      \"academic_binary_f1\": 0.628,\n      \"academic_binary_ci\": [\n        0.603,\n        0.652\n      ],\n      \"code_binary_f1\": 0.687,\n      \"code_binary_ci\": [\n        0.664,\n        0.71\n      ],\n      \"cross_domain_logo_binary_f1\": 0.668,\n      \"max_gap_vs_wiki_pp\": 18.7,\n      \"worst_domain\": \"academic\",\n      \"best_domain\": \"wikipedia\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Per-domain binary F1 (LOGO across generators)\",\n        \"rows\": [\n          [\n            \"Domain\",\n            \"Seeds\",\n            \"Binary F1\",\n            \"95% CI\",\n            \"Δ vs Wiki\"\n          ],\n          [\n            \"Wikipedia\",\n            \"500\",\n            \"0.815\",\n            \"[0.796, 0.834]\",\n            \"—\"\n          ],\n          [\n            \"News\",\n            \"500\",\n            \"0.712\",\n            \"[0.690, 0.733]\",\n            \"−10.3 pp\"\n          ],\n          [\n            \"Code\",\n            \"500\",\n            \"0.687\",\n            \"[0.664, 0.710]\",\n            \"−12.8 pp\"\n          ],\n          [\n            \"Academic\",\n            \"500\",\n            \"0.628\",\n            \"[0.603, 0.652]\",\n            \"−18.7 pp\"\n          ],\n          [\n            \"**Cross-domain LOGO**\",\n            \"2000\",\n            \"**0.668**\",\n            \"[0.654, 0.682]\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain dependence 在 worst 档下与 generator/temperature/instruct/edit 依赖 叠加。Reviewer 列出  cumulative conditions：\\\"base models only, temperature ∈ [0.5, 0.9], continuation preferred,  Wikipedia domain, no human editing, single reference model.\\\" 这是 increasingly narrow niche。 Academic domain failure 尤其 damaging 因为 paper motivation 中引用了 \\\"7–17% of recent scientific  papers contain LLM text\\\"——方法恰好在这个最相关 domain 上最弱。\\n\\n\\nWikipedia (训练数据主 domain) 表现最好 (0.815)，academic 最差 (0.628)——gap 达 18.7 pp。在 t=0.7 下 academic binary F1 进一步降到 ~0.628，接近 chance + 0.128 margin。Cross-domain LOGO (train on 3, test  on 1) 降到 0.668。Worst-tier reviewer 会 argue：\\\"The method's performance is catastrophically  domain-dependent. Scientific text — precisely the domain where AI contamination is a pressing concern  per the authors' own motivation — yields near-chance binary F1 of 0.628. This domain sensitivity,  combined with the base-model and temperature restrictions, makes the method's scope so narrow as to  be practically meaningless.\\\" Academic domain 的 weak signal 可能因为 scientific text 的 formulaic  structure 本身就限制了 vocabulary diversity variation，使 surface features 失效。Cross-domain LOGO  0.668 加上 cross-generator LOGO 0.694 = cumulative degradation when both unknowns (generator + domain)  are combined，reviewer 会 estimate real-world F1 < 0.65。\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4)。测试 depth resolution 是否超过 3-class。 Ordinal methods (CORAL, Frank-Hall) 比较。\\n\",\n    \"results\": {\n      \"five_class_macro_f1\": 0.498,\n      \"five_class_ci\": [\n        0.48,\n        0.516\n      ],\n      \"three_class_macro_f1\": 0.762,\n      \"ordinal_coral_f1\": 0.502,\n      \"ordinal_frank_hall_f1\": 0.491,\n      \"gen0_recall\": 0.92,\n      \"gen1_recall\": 0.63,\n      \"gen2_recall\": 0.41,\n      \"gen3_recall\": 0.33,\n      \"gen4_recall\": 0.29,\n      \"gen2_gen3_confusion_rate\": 0.51,\n      \"gen3_gen4_confusion_rate\": 0.48,\n      \"mean_absolute_depth_error\": 0.89\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Ordinal depth classification resolution\",\n        \"rows\": [\n          [\n            \"Granularity\",\n            \"Method\",\n            \"Macro F1\",\n            \"Ordinal vs XGBoost\"\n          ],\n          [\n            \"3-class\",\n            \"XGBoost\",\n            \"0.762\",\n            \"—\"\n          ],\n          [\n            \"5-class\",\n            \"XGBoost\",\n            \"0.498\",\n            \"—\"\n          ],\n          [\n            \"5-class\",\n            \"CORAL\",\n            \"0.502\",\n            \"+0.4 pp\"\n          ],\n          [\n            \"5-class\",\n            \"Frank-Hall\",\n            \"0.491\",\n            \"−0.7 pp\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"5-class per-depth recall\",\n        \"rows\": [\n          [\n            \"Depth\",\n            \"Recall\",\n            \"Primary Confusion\"\n          ],\n          [\n            \"gen-0\",\n            \"0.92\",\n            \"gen-1 (6%)\"\n          ],\n          [\n            \"gen-1\",\n            \"0.63\",\n            \"gen-2 (24%)\"\n          ],\n          [\n            \"gen-2\",\n            \"0.41\",\n            \"gen-1/gen-3 (26%/18%)\"\n          ],\n          [\n            \"gen-3\",\n            \"0.33\",\n            \"gen-2/gen-4 (31%/21%)\"\n          ],\n          [\n            \"gen-4\",\n            \"0.29\",\n            \"gen-3 (38%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-class collapse 是 worst 档对 task formulation novelty 最有力的 attack。如果 depth signal 本质上 是 binary (+gen-1 略有区分)，那 \\\"generation depth classification\\\" 这个 task formulation 的 novelty  = 在 binary detection 上加了一个勉强可用的 third class。Ordinal methods 无改善进一步说明 depth  不是 ordinal quantity (continuous gradient)——而是 discrete jump from near-source to deep,  与 model collapse theory 的 gradual degradation 预测不一致。\\n\\n\\n5-class F1 = 0.498 (random baseline ~0.20, so margin = 0.298)。Ordinal methods 无改善 (CORAL 0.502,  Frank-Hall 0.491)——depth signal 不具备 ordinal structure beyond coarse binning。Gen-0 recall 高  (0.92) 但 gen-2/3/4 几乎无法区分 (recall 0.29–0.41, confusion 48–51%)。Gen-0 的高 recall 来自  seed-sharing (原始人类文本与训练 features 有 distributional gap)——这不是 depth classification 而是  human-vs-machine detection。\\nWorst-tier reviewer 会 argue：\\\"5-class F1 of 0.498 confirms depth signal is essentially binary: the  method distinguishes 'source-adjacent' (gen-0/1) from 'deep' (gen-2+) but cannot resolve within either  group. The 3-class formulation is not a principled task definition but an artifact of signal weakness —  it happens to be the granularity at which the method achieves non-trivial performance. The gen-2/3/4  confusion block (48–51% confusion rate) shows the 'generation depth' framing overclaims — this is  at most a binary-plus-one classifier.\\\"\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated human edits: (A) random word replacement 5/10/20%,  (B) LLM-simulated light rephrasing (Qwen3-1.7B)。\\n\",\n    \"results\": {\n      \"baseline_binary_f1\": 0.695,\n      \"random_5pct_f1\": 0.65,\n      \"random_10pct_f1\": 0.614,\n      \"random_20pct_f1\": 0.591,\n      \"llm_rephrase_binary_f1\": 0.647,\n      \"llm_rephrase_multiclass_f1\": 0.667,\n      \"llm_rephrase_edit_distance\": 0.507,\n      \"degradation_5pct_pp\": -4.5,\n      \"degradation_10pct_pp\": -8.1,\n      \"degradation_20pct_pp\": -10.4,\n      \"degradation_llm_pp\": -4.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Robustness to simulated human edits\",\n        \"rows\": [\n          [\n            \"Perturbation\",\n            \"Binary F1\",\n            \"Δ vs Baseline\",\n            \"Edit Distance\"\n          ],\n          [\n            \"None (baseline)\",\n            \"0.695\",\n            \"—\",\n            \"0.0\"\n          ],\n          [\n            \"Random 5%\",\n            \"0.650\",\n            \"−4.5 pp\",\n            \"~0.05\"\n          ],\n          [\n            \"Random 10%\",\n            \"0.614\",\n            \"−8.1 pp\",\n            \"~0.10\"\n          ],\n          [\n            \"Random 20%\",\n            \"0.591\",\n            \"−10.4 pp\",\n            \"~0.20\"\n          ],\n          [\n            \"LLM rephrase\",\n            \"0.647\",\n            \"−4.5 pp\",\n            \"0.507\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Robustness 实验在 worst 档下是 lose-lose。Fragile result confirms depth signal 是 surface-level  且 easily disrupted。Combined with instruct degradation、temperature sensitivity、domain dependence， the cumulative fragility makes a devastating picture for any practical deployment argument。\\n\\n\\n5% random replacement 造成 4.5 pp drop (0.695 → 0.650)。LLM rephrasing (edit distance 0.507,  avg 1.69 sentences replaced) 造成相同量级 drop (−4.5 pp → 0.647)。20% replacement 降到 0.591。\\nWorst-tier reviewer 会 argue：\\\"In practice, AI-generated text is almost always edited before  publication — students edit LLM essays, writers revise LLM drafts, automated pipelines post-process  outputs. The method loses 4.5 pp F1 from light editing (50% edit distance ratio, ~1.7 sentences  changed), pushing the already-modest 0.695 baseline to 0.647. At this level, the method correctly  classifies depth for barely 65% of edited text — not actionable for any real-world application.\\\"\\nDegradation is near-linear with perturbation intensity, suggesting the depth signal resides in  surface-level distributional properties easily disrupted by any text modification. This confirms  the \\\"vocabulary impoverishment repackaging\\\" critique—if the signal were capturing deeper structural  properties of recursive generation, it would be more robust to superficial edits.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"添加 LD-Score (character-distribution signature) 作为第 8 个 feature。测试 character-level 信号 是否与 word/entropy features 互补。\\n\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"eight_feature_with_ld_f1\": 0.802,\n      \"ld_score_alone_logo_f1\": 0.721,\n      \"ld_score_alone_spearman\": 0.794,\n      \"marginal_improvement_pp\": 0.4,\n      \"feature_importance_ld\": 0.022,\n      \"ld_score_cv_corrected_f1\": 0.793\n    },\n    \"tables\": [\n      {\n        \"caption\": \"LD-Score feature addition (3-class LOGO)\",\n        \"rows\": [\n          [\n            \"Feature Set\",\n            \"LOGO F1\",\n            \"Δ\"\n          ],\n          [\n            \"7 features (baseline)\",\n            \"0.798\",\n            \"—\"\n          ],\n          [\n            \"7 + LD-Score\",\n            \"0.802\",\n            \"+0.4 pp\"\n          ],\n          [\n            \"LD-Score only\",\n            \"0.721\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Minor experiment, minor result。在 worst 档下主要作为 \\\"all signals converge\\\" narrative 的  supporting evidence。不是 primary attack vector。\\n\\n\\nLD-Score 单独 LOGO F1 = 0.721 (高于 FastDetectGPT 0.627 和 Binoculars 0.579，但低于 Avg-LogProb  0.765 和 7-feature 0.798)。加入后 marginal improvement 仅 0.4 pp (0.798 → 0.802)，feature  importance 排最后 (0.022)。LD-Score 的 high Spearman (0.794) 说明它有 ordinal depth signal， 但被 existing features 高度 subsume。\\nWorst-tier reviewer 不会直接 attack 这个实验 (minor addition)，但会用它 reinforce vocabulary  impoverishment narrative：\\\"Adding a character-level feature provides negligible improvement (0.4 pp),  confirming that character, word, and NLL features all measure the same underlying phenomenon —  text simplification under recursive generation. The claimed 'differential depth response' across  feature types is an artifact of measuring the same signal at different linguistic levels.\\\"\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned end-to-end depth classifier (OLMo-1B-Instruct, Qwen3-1.7B-Instruct,  及其 base model variants)。Within-distribution CV 和 cross-generator transfer。\\n\",\n    \"results\": {\n      \"qlora_olmo_instruct_3class\": 0.888,\n      \"qlora_olmo_instruct_3class_std\": 0.007,\n      \"qlora_olmo_instruct_binary\": 0.836,\n      \"qlora_olmo_instruct_binary_std\": 0.01,\n      \"qlora_qwen_instruct_3class\": 0.907,\n      \"qlora_qwen_instruct_binary\": 0.867,\n      \"qlora_olmo_base_3class\": 0.859,\n      \"qlora_olmo_base_binary\": 0.793,\n      \"qlora_qwen_base_3class\": 0.904,\n      \"qlora_qwen_base_binary\": 0.86,\n      \"seven_feature_3class\": 0.762,\n      \"seven_feature_binary\": 0.694,\n      \"delta_3class_pp_olmo\": 12.6,\n      \"delta_binary_pp_olmo\": 14.2,\n      \"qlora_5class_f1\": 0.575,\n      \"qlora_inference_cost_ratio\": 47.0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"End-to-end (QLoRA) vs 7-feature ensemble\",\n        \"rows\": [\n          [\n            \"Method\",\n            \"Model\",\n            \"3-class F1 (±std)\",\n            \"Binary F1 (±std)\",\n            \"Cost Ratio\"\n          ],\n          [\n            \"7-feature XGBoost\",\n            \"—\",\n            \"0.762\",\n            \"0.694\",\n            \"1×\"\n          ],\n          [\n            \"QLoRA\",\n            \"OLMo-Instruct\",\n            \"0.888 ± 0.007\",\n            \"0.836 ± 0.010\",\n            \"47×\"\n          ],\n          [\n            \"QLoRA\",\n            \"Qwen-Instruct\",\n            \"0.907 ± 0.008\",\n            \"0.867 ± 0.014\",\n            \"47×\"\n          ],\n          [\n            \"QLoRA\",\n            \"OLMo-Base\",\n            \"0.859 ± 0.004\",\n            \"0.793 ± 0.010\",\n            \"47×\"\n          ],\n          [\n            \"QLoRA\",\n            \"Qwen-Base\",\n            \"0.904 ± 0.009\",\n            \"0.860 ± 0.012\",\n            \"47×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"End-to-end comparison 在 worst 档下 devastating。14-17 pp gap 说明 7-feature ensemble 遗漏了  substantial depth signal。论文的 positioning 是 efficiency vs absolute performance tradeoff，但  worst-tier reviewer 不买账：\\\"if the features miss this much signal, the contribution is not a  competitive method but an incomplete characterization.\\\" QLoRA instruct > base 也 undermine  \\\"instruct kills depth signal\\\" narrative——within-distribution instruct QLoRA actually works fine,  说明 instruct 限制的是 the specific features chosen, not the depth signal itself。\\n\\n\\nQLoRA within-distribution 大幅碾压 7-feature：OLMo-Instruct 3-class 0.888 vs 0.762 (+12.6 pp)， binary 0.836 vs 0.694 (+14.2 pp)。Qwen-Instruct 更高 (3-class 0.907, binary 0.867)。Even base  models QLoRA (3-class 0.859/0.904) 远超 7-feature。5-class F1 = 0.575 也远超 7-feature 的 ~0.50。\\nWorst-tier reviewer 会 cherry-pick within-distribution numbers：\\\"A straightforward QLoRA classifier  achieves 0.867 binary F1 (Qwen-Instruct), dwarfing the proposed method's 0.694 by 17.3 pp. Even  with the base model alone, QLoRA achieves 0.860 binary — a 16.6 pp advantage. The 7-feature  ensemble captures less than half the depth signal available in the text. The authors' efficiency  argument (47× cost ratio) is unconvincing: the QLoRA classifier runs on the same-sized model  already needed as a reference, and the 17 pp gap is too large to justify on cost grounds.\\\"\\n论文的 rebuttal point 是 LOGO cross-generator transfer——QLoRA within-distribution 的 advantage  partly comes from overfitting to generator-specific patterns。但 worst-tier reviewer 已经 scored  low before considering this nuance。\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Address text length confound: (A) length-depth correlation analysis, (B) length-normalized features,  (C) length-matched subsampling re-evaluation。\\n\",\n    \"results\": {\n      \"spearman_length_depth\": 0.12,\n      \"spearman_p\": 0.001,\n      \"length_depth_correlation\": \"weak (|ρ|<0.14)\",\n      \"length_matched_binary_f1\": 0.724,\n      \"unmatched_binary_f1\": 0.77,\n      \"delta_pp\": -4.6,\n      \"normalized_ttr_trend_preserved\": true,\n      \"normalized_hapax_trend_preserved\": true,\n      \"normalized_rho_stronger\": true,\n      \"length_is_primary_confound\": false,\n      \"short_text_dropout_bias\": true,\n      \"length_matched_f1_vs_logo_headline\": \"+3.0 pp above 0.694 LOGO\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Length control analysis\",\n        \"rows\": [\n          [\n            \"Condition\",\n            \"Binary F1\",\n            \"Δ vs Unmatched\"\n          ],\n          [\n            \"Unmatched (original)\",\n            \"0.770\",\n            \"—\"\n          ],\n          [\n            \"Length-normalized features\",\n            \"0.748\",\n            \"−2.2 pp\"\n          ],\n          [\n            \"Length-matched subsample\",\n            \"0.724\",\n            \"−4.6 pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound 不 kill paper 但 erode credibility。4.6 pp 降幅在 worst 档下被 generalize 为  \\\"confound-sensitive method\\\"——reviewer 会 question every reported number 是否被 uncontrolled  confounds inflate。这使 0.694 headline number 的 credibility 进一步下降。\\n\\n\\nLength-depth correlation weak (ρ=0.12) 但 statistically significant (p=0.001)。Length-matched  binary F1 降 4.6 pp (0.770 → 0.724)——意味着 ~6% of signal 来自 text length。Normalized  features 的 depth trend 保持说明 depth signal 不完全是 length artifact，但 worst-tier reviewer  会 magnify 4.6 pp drop：\\\"After controlling for the most basic confound — text length — the method  loses 4.6 pp. How many other confounds (topic, style, vocabulary register) remain uncontrolled?  The 0.694 LOGO F1 may be further inflated by confounds the authors haven't tested.\\\"\\nShort-text dropout bias 增加了 confound complexity：deeper depths 有更多 short text 被 pipeline  过滤掉，导致 surviving deeper text 是 systematically longer/more complete——这是 selection bias， 方法可能部分检测的是 \\\"which texts survived the pipeline filter\\\" 而非 true depth signal。\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"添加 Qwen3-8B-Base 测试 7B+ scale 的 depth signal。1000 seeds × 5 depths。与现有 6-gen  LOGO 集成。\\n\",\n    \"results\": {\n      \"qwen3_8b_records\": 4497,\n      \"qwen3_8b_unique_seeds\": 995,\n      \"qwen3_8b_depth_dist\": {\n        \"0\": 995,\n        \"1\": 979,\n        \"2\": 937,\n        \"3\": 831,\n        \"4\": 755\n      },\n      \"logo_6gen_avg_f1\": 0.789,\n      \"qwen3_8b_logo_binary_f1\": 0.647,\n      \"qwen3_8b_logo_3class_f1\": 0.683,\n      \"qwen3_8b_within_cv_f1\": 0.711,\n      \"delta_vs_avg_pp\": -10.6,\n      \"hapax_rho_8b\": -0.558,\n      \"ttr_rho_8b\": -0.542,\n      \"entropy_mean_rho_8b\": -0.475,\n      \"feature_margin_compression_vs_avg\": 0.72,\n      \"ddr_pattern_preserved\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Scale effect: Qwen3-8B vs smaller generators\",\n        \"rows\": [\n          [\n            \"Generator\",\n            \"Size\",\n            \"LOGO Binary F1\",\n            \"hapax ρ\",\n            \"entropy_mean ρ\",\n            \"Feature compression\"\n          ],\n          [\n            \"Pythia-1B\",\n            \"1.0B\",\n            \"0.724\",\n            \"−0.65\",\n            \"−0.60\",\n            \"—\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"1.7B\",\n            \"0.698\",\n            \"−0.63\",\n            \"−0.60\",\n            \"—\"\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"2.8B\",\n            \"0.711\",\n            \"−0.63\",\n            \"−0.60\",\n            \"—\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"8.0B\",\n            \"0.647\",\n            \"−0.56\",\n            \"−0.48\",\n            \"0.72×\"\n          ],\n          [\n            \"**Trend**\",\n            \"—\",\n            \"**Declining**\",\n            \"**Compressing**\",\n            \"**Compressing**\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale degradation 是 worst 档的 structural problem。论文诚实 report 这是 scope boundary，但  reviewer reframe：\\\"the scope boundary excludes all models that generate text at scale.\\\" 加上  instruct degradation (OLMo-Instruct LOGO 0.338)，方法的 applicable scope = base models ≤ 8B  at moderate temperature in Wikipedia-like domains without human editing。这个 niche 在 2026 年 没有 practical relevance。\\n\\n\\nQwen3-8B LOGO binary F1 = 0.647——比 6-gen average 低 ~10.6 pp。Feature drift magnitudes 全面压缩  (hapax ρ −0.558 vs avg −0.647, compression ~0.72)。DDR pattern 仍然 preserved (drifting > stationary  分离 maintained)，但 magnitudes 显著 weakened。Within-CV F1 = 0.711 说明 8B 自身 depth signal 存在， 但 cross-generator transfer 弱 (LOGO 0.647)——smaller models 的 feature distribution 不 transfer well。\\nWorst-tier reviewer 会 extrapolate：\\\"At 8B, the method shows substantial degradation (−10.6 pp vs  average, LOGO binary 0.647). This model is still far from frontier: GPT-4 (>100B), Claude 3 (unknown),  Llama-3-70B — the models generating the vast majority of AI text in practice — are 10–100× larger.  The observed linear degradation in log-scale model size (from 0.6B to 8B) projects to near-chance  performance at frontier scales, rendering the method irrelevant for the contamination problem it claims  to address.\\\" 这是 worst 档中 most damaging extrapolation——审稿人不需要实验数据就可以 argue。\\nDepth distribution (gen-4 only 755/995 = 75.9% retention) 也说明 8B models 更容易产生 degenerate  output at depth (higher skip rate)——selection bias adds to confound concerns。\\n\"\n  },\n  {\n    \"name\": \"ordinal_baseline_comparison\",\n    \"description\": \"Compare existing detector continuous scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb)  作为 ordinal depth predictors vs 7-feature ensemble。Multi-detector ensemble 比较。\\n\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"seven_feature_ci\": [\n        0.786,\n        0.799\n      ],\n      \"avg_logprob_logo_f1\": 0.765,\n      \"avg_logprob_ci\": [\n        0.616,\n        0.82\n      ],\n      \"ld_score_logo_f1\": 0.721,\n      \"ld_score_ci\": [\n        0.588,\n        0.77\n      ],\n      \"fastdetectgpt_logo_f1\": 0.627,\n      \"fastdetectgpt_ci\": [\n        0.511,\n        0.762\n      ],\n      \"binoculars_logo_f1\": 0.579,\n      \"binoculars_ci\": [\n        0.405,\n        0.664\n      ],\n      \"bootstrap_7feat_vs_avglogprob_delta\": 0.033,\n      \"bootstrap_7feat_vs_avglogprob_p\": 0.0,\n      \"multi_detector_ensemble_f1\": 0.708,\n      \"multi_det_4det_plus_surface_3class\": 0.795,\n      \"multi_det_binary\": 0.708,\n      \"seven_feature_binary\": 0.705,\n      \"multi_det_vs_7feat_binary_pp\": 0.3,\n      \"multi_det_inference_cost\": \"2.4×\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Ordinal depth classification: 7-feature vs existing detector baselines (LOGO)\",\n        \"rows\": [\n          [\n            \"Method\",\n            \"3-class F1\",\n            \"95% CI\",\n            \"Binary F1\",\n            \"Δ vs 7-feat 3-class\",\n            \"Bootstrap p\"\n          ],\n          [\n            \"**7-feature ensemble**\",\n            \"**0.798**\",\n            \"[0.786, 0.799]\",\n            \"**0.705**\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Avg-LogProb\",\n            \"0.765\",\n            \"[0.616, 0.820]\",\n            \"0.695\",\n            \"−3.3 pp\",\n            \"<0.001\"\n          ],\n          [\n            \"LD-Score\",\n            \"0.721\",\n            \"[0.588, 0.770]\",\n            \"0.672\",\n            \"−7.7 pp\",\n            \"<0.001\"\n          ],\n          [\n            \"FastDetectGPT\",\n            \"0.627\",\n            \"[0.511, 0.762]\",\n            \"0.601\",\n            \"−17.1 pp\",\n            \"<0.001\"\n          ],\n          [\n            \"Binoculars\",\n            \"0.579\",\n            \"[0.405, 0.664]\",\n            \"0.558\",\n            \"−21.9 pp\",\n            \"<0.001\"\n          ],\n          [\n            \"4-det + surface\",\n            \"0.795\",\n            \"[0.781, 0.808]\",\n            \"0.708\",\n            \"−0.3 pp\",\n            \"0.72\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Baseline comparison 在 worst 档下是 most dangerous experiment。在 binary metric (primary) 下， 7-feature (0.705) 和 multi-det (0.708) 几乎无差——reviewer 会 conclude 7-feature 的 contribution  不足以 justify publication。3-class 下 7-feature 略优 (0.798 vs 0.795)，但差距 near-zero。 论文 contribution 被 reduce 为：\\\"a modestly different feature set that performs comparably to  existing detector ensembles, with an interpretive framework (DDR) that may or may not correspond  to a real phenomenon.\\\" 这是 worst 档下 paper's reason to exist 被直接 challenged 的实验。\\n\\n7-feature LOGO F1 = 0.798 (3-class) 显著优于最佳 single detector Avg-LogProb (0.765, δ=3.3 pp,  p < 0.001)。但 single detector CIs 极宽 (Avg-LogProb CI [0.616, 0.820] 跨越 7-feature point  estimate)——说明 per-generator variance 极高。Multi-detector ensemble (4-det + surface) 达到  3-class 0.795 和 binary 0.708 vs 7-feature binary 0.705——仅 0.3 pp 差距。\\nWorst-tier reviewer 会 argue：\\\"The 7-feature ensemble achieves 3.3 pp over Avg-LogProb, but this  single number (average log probability) requires only basic LM inference — no feature engineering,  no reference model selection, no DDR framework. The tiny margin and overlapping confidence intervals  suggest the elaborate DDR characterization provides minimal practical benefit over a trivial baseline.  Moreover, a multi-detector ensemble matches the 7-feature binary F1 within 0.3 pp. The contribution  reduces to: 'a slightly different way to achieve what existing tools already achieve, with a novel  but unvalidated interpretive framework (DDR).'\\\"\\nBootstrap p < 0.001 for 7-feat vs Avg-LogProb 在 3-class setting 是 significant。但 binary  setting 差距 near-zero (0.705 vs 0.708)——primary metric 下 7-feature 反而略低于 multi-detector。\\n\"\n  }\n]",
      "numLines": 1189,
      "startLine": 1,
      "totalLines": 1189
    }
  },
  "sourceToolAssistantUUID": "3c8d78a1-eeb3-496f-ac5f-bfd40524b20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T22:11:59.691Z_

<details><summary>↩ Tool result · `toolu_01Su3kReged87LKsQyBYThL3`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
5	- Positioning: **Findings paper**（非 main conference long paper）
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.
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
31	| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |
32	| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |
33	| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
34	| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |
35	
36	## Scope & Limitations (必须在论文中突出)
37	
38	1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
39	2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
40	3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
41	4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
42	5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
43	6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).
44	
45	## Story Spine
46	
47	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.
48	
49	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.
50	
51	**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.
52	
53	**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."
54	
55	## Anticipated Reviewer Concerns
56	
57	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.
58	
59	**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.
60	
61	**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.
62	
63	**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.
64	
65	**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.
66	
67	**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).
68	
69	**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.
70	
71	**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.
72	
73	**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.
74	
75	**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.
76	
77	## Contribution Positioning (Findings Level)
78	The contribution is **empirical and conceptual**, appropriate for Findings:
79	1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
80	2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
81	3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.
82	
83	**Framing discipline:**
84	- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
85	- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
86	- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
87	- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
88	- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
89	- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.
90	
91	Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.
92	
93	## Venue Fit
94	- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c48573fc-4ce8-40b4-a43d-4a3dfb75d772",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "9311298e-c784-4c83-9ad0-1658a0630449",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |\n| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  },
  "sourceToolAssistantUUID": "c48573fc-4ce8-40b4-a43d-4a3dfb75d772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T22:11:59.688Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Su3kReged87LKsQyBYThL3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ee7a20-2348-4c95-8b8f-53a9ce7fa576",
  "isSidechain": false,
  "requestId": "req_011CbGUsJqdjgLqBRbNCMUpy",
  "type": "assistant",
  "uuid": "c48573fc-4ce8-40b4-a43d-4a3dfb75d772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gobSQbYYUCiiUK9SZHLwp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13784,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13784
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "9311298e-c784-4c83-9ad0-1658a0630449",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate reframed paper on depth decoding dynamics",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Assistant

_source line 14 · 2026-05-21T22:12:37.663Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the full LaTeX paper for the "worst" tier dream simulation. This paper should be "够审" (reviewable) quality — covering Abstract, Introduction, Method, Experiments, and Conclusion — with all experiment data from the JSON represented in appropriate sections/tables.

Let me organize the paper structure based on the narrative guidance (worst tier):

The narrative guidance says:
- Core framing fails
- Reframe from 'depth classification tool' to 'understanding distributional dynamics of recursive autoregressive generation'
- DDR as analytical framework is the contribution, classifier degraded to validation probe


- Repackage the negative finding about distributional shift not correlating with quality degradation as a key insight into generation dynamics
- Shift away from practical applications and focus instead on characterizing and understanding the phenomenon

I have thirteen experiments to work with, spanning feature ablations, cross-generator comparisons, downstream utility tests, prompt variations, and robustness checks. I'll weave these into the paper to support the reframed narrative about distributional dynamics rather than practical classification performance. I'm organizing the paper structure with the main sections: Introduction, Related Work, Method covering the DDR framework and classifier design, then Experimental Setup followed by Results broken into key findings like feature ablation trends, cross-generator performance, baseline comparisons, and downstream utility analysis. The Analysis section will dive deeper into ordinal granularity, scaling effects, and reference model sensitivity.

For the Discussion and Conclusion, I need to wrap up the findings and implications. Given the 8-page EMNLP constraint, I should strategically place the core experiments in the main text—feature ablation, cross-generator generalization, and baseline comparisons are essential—while moving supporting experiments like multi-domain analysis, prompt type variations, paraphrastic comparisons, and robustness checks to the appendix. This keeps the narrative focused on the primary contributions while still documenting the full experimental scope. Continuing with the rest of the paper structure — I need to map out the remaining analysis sections covering scale effects with larger generators, how the approach performs across different reference model families, then wrap up with conclusions and limitations. The appendix will cover various robustness checks and extensions like prompt sensitivity, paraphrastic variations, multi-domain evaluation, human edit robustness, and alternative scoring approaches. Now I'm ready to write out the full LaTeX document.

Wait, I'm realizing the framing guidance matters here — this should be written as a worst-case paper where the core framing is vulnerable. The task wants reviewers to see the idea and experimental design clearly, but the paper should expose the weaknesses that would draw criticism. So I need to attempt the reframe from a classification tool toward understanding distributional dynamics, but leave that reframing incomplete or unconvincing, letting the original problematic framing show through. That way the paper is complete and evaluable, but structured to highlight its own vulnerabilities.

Now I'll write this as a LaTeX document with basic article formatting since the goal is reviewability rather than submission polish.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9311298e-c784-4c83-9ad0-1658a0630449",
  "isSidechain": false,
  "requestId": "req_011CbGUsaetyacMhxRzasAYL",
  "type": "assistant",
  "uuid": "7c6ed929-5aa5-481e-9005-40b17c82ab6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAfEsJANsPFsrnDzypQkht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24524,
      "cache_read_input_tokens": 25625,
      "output_tokens": 1892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1892,
          "cache_read_input_tokens": 25625,
          "cache_creation_input_tokens": 24524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24524
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

_source line 15 · 2026-05-21T22:12:37.832Z_

Let me check what LaTeX packages are available and ensure the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c6ed929-5aa5-481e-9005-40b17c82ab6b",
  "isSidechain": false,
  "requestId": "req_011CbGUsaetyacMhxRzasAYL",
  "type": "assistant",
  "uuid": "5c3cb702-3bcc-4c61-941b-8fca94aa5664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAfEsJANsPFsrnDzypQkht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24524,
      "cache_read_input_tokens": 25625,
      "output_tokens": 1892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1892,
          "cache_read_input_tokens": 25625,
          "cache_creation_input_tokens": 24524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24524
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

_source line 16 · 2026-05-21T22:12:41.283Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UAXcLYuu4mvB2a5xFfJJkB`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/ && which pdflatex && kpsewhich acl.sty 2>/dev/null; kpsewhich geometry.sty 2>/dev/null",
  "description": "Check directory and LaTeX availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c3cb702-3bcc-4c61-941b-8fca94aa5664",
  "isSidechain": false,
  "requestId": "req_011CbGUsaetyacMhxRzasAYL",
  "type": "assistant",
  "uuid": "b452c6c1-a497-49bb-a388-735391ceeccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAfEsJANsPFsrnDzypQkht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24524,
      "cache_read_input_tokens": 25625,
      "output_tokens": 1892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1892,
          "cache_read_input_tokens": 25625,
          "cache_creation_input_tokens": 24524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24524
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

_source line 17 · 2026-05-21T22:12:41.462Z_

<details><summary>↩ Tool result · `toolu_01UAXcLYuu4mvB2a5xFfJJkB`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
/usr/bin/pdflatex
/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b452c6c1-a497-49bb-a388-735391ceeccb",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "9ec8fedd-6240-4dd0-ae8a-925251afdea1",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex\n/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b452c6c1-a497-49bb-a388-735391ceeccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T22:12:44.284Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GYj2zff9h65uSEZoKQUvhZ`</summary>

```json
{
  "command": "kpsewhich booktabs.sty multirow.sty hyperref.sty natbib.sty xcolor.sty 2>/dev/null",
  "description": "Check additional LaTeX packages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ec8fedd-6240-4dd0-ae8a-925251afdea1",
  "isSidechain": false,
  "requestId": "req_011CbGUvf58uPhGq3j5Du4NQ",
  "type": "assistant",
  "uuid": "50a6f9d6-b22e-4fd8-804e-a00c822a28eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwRM9t8gUYffTViN1pLrbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 50149,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 50149,
          "cache_creation_input_tokens": 1954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1954
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

_source line 19 · 2026-05-21T22:12:44.338Z_

<details><summary>↩ Tool result · `toolu_01GYj2zff9h65uSEZoKQUvhZ`</summary>

```text
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty
/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50a6f9d6-b22e-4fd8-804e-a00c822a28eb",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "56017d9b-64f3-4fcc-8a28-84ae868df1ca",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\n/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty\n/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty\n/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "50a6f9d6-b22e-4fd8-804e-a00c822a28eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T22:12:48.702Z_

<details><summary>Logged reasoning block</summary>

```text
Good, all packages available. Now let me write the full paper. This is for the "worst" tier dream, so I need to write it reflecting the worst-case framing while still being complete and reviewable.

Let me write the paper now. I need to cover all 15 experiments from the JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56017d9b-64f3-4fcc-8a28-84ae868df1ca",
  "isSidechain": false,
  "requestId": "req_011CbGUvs5SrG4G95zYzydff",
  "type": "assistant",
  "uuid": "f8c9af9c-ed61-4200-a040-9489d6b6bde1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqZjeQgzQSxz4a2zALATCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 52103,
      "output_tokens": 10936,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10936,
          "cache_read_input_tokens": 52103,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 264
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

_source line 21 · 2026-05-21T22:12:49.192Z_

Now writing the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8c9af9c-ed61-4200-a040-9489d6b6bde1",
  "isSidechain": false,
  "requestId": "req_011CbGUvs5SrG4G95zYzydff",
  "type": "assistant",
  "uuid": "d41e8f17-6625-4aa6-b50c-c7217ec08ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqZjeQgzQSxz4a2zALATCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 52103,
      "output_tokens": 10936,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10936,
          "cache_read_input_tokens": 52103,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 264
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

_source line 22 · 2026-05-21T22:16:07.291Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ste7TkKNcXjkcRJnk9q1Tx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{xcolor}\n\\usepackage{amsmath}\n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\title{Differential Depth Response in Recursive Autoregressive Generation:\\\\Understanding Distributional Dynamics Beyond Binary Detection}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text that has been recursively generated through multiple autoregressive passes. Current detection methods provide only binary real-versus-synthetic classification, conflating qualitatively different material along the generation chain. We formulate \\emph{generation depth classification} (gen-0/gen-1/gen-2+) and characterize \\textbf{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while distributional-shape features (tail decay, entropy max) remain near-stationary ($|\\rho| < 0.10$). Across 8 base-model generators from 5 families (0.6B--8B parameters), a lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under leave-one-generator-out (LOGO) evaluation, outperforming existing detector baselines repurposed as ordinal predictors (best single: Avg-LogProb 0.765 3-class, $\\Delta = -3.3$ pp). We further show that depth-aware data curation is statistically equivalent to random subsampling for downstream causal language model quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm$2\\% margin), establishing that distributional shift under recursive generation does not entail quality degradation---challenging implicit assumptions in the model collapse literature. The depth signal degrades substantially under instruction tuning and at high temperature, restricting the current scope to base models at moderate temperatures.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models increasingly generate text that re-enters training pipelines through web scraping, creating recursive feedback loops. Estimates suggest 7--17\\% of recent scientific publications contain LLM-generated content, and this proportion is growing. Understanding the provenance of such text---specifically, \\emph{how many autoregressive passes} separate it from human-authored source material---is important for characterizing the distributional dynamics of these feedback loops.\n\nBinary detection methods (FastDetectGPT, Binoculars, LD-Score) classify text as human or machine-generated but cannot distinguish first-generation output (gen-1), which retains much of the source distribution's lexical properties, from deeper generations (gen-2+), which exhibit measurably reduced vocabulary diversity and compressed perplexity. This conflation obscures important distributional structure: gen-1 text may be nearly indistinguishable from human writing on surface metrics, while gen-4+ text shows substantial vocabulary impoverishment.\n\nWe formulate \\emph{generation depth classification} as a new task and introduce the \\textbf{differential depth response} (DDR) framework for characterizing how distributional features evolve across recursive generation steps. Our central finding is that features split into two behavioral categories: \\emph{drifting} features (hapax ratio, TTR, entropy mean) that exhibit strong monotonic trends with depth, and \\emph{stationary} features (tail decay, entropy max) whose distributions remain approximately invariant. This split is consistent with recursive autoregressive generation inducing a location shift in the next-token log-likelihood (NLL) distribution while approximately preserving its shape.\n\nWe make three contributions:\n\\begin{enumerate}[nosep]\n\\item \\textbf{Task formulation \\& DDR characterization}: Generation depth classification beyond binary detection, with empirical validation of the drifting/stationary dichotomy across 8 generators from 5 model families (0.6B--8B).\n\\item \\textbf{Lightweight depth classifier}: A 7-feature XGBoost ensemble achieving leak-free binary F1 = 0.694 under 8-generator LOGO, using a single 410M reference model.\n\\item \\textbf{Negative finding}: Depth-aware data curation provides no benefit over random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{AI text detection.} Perplexity-based detectors leverage statistical properties of model-generated text. DetectGPT~\\citep{mitchell2023detectgpt} uses log-probability curvature; Fast-DetectGPT~\\citep{bao2024fast} replaces perturbation with conditional sampling; Binoculars~\\citep{hans2024binoculars} contrasts two models' cross-entropy; GLTR~\\citep{gehrmann2019gltr} visualizes token-level statistics. All operate in a binary detection paradigm and do not address generation depth.\n\n\\paragraph{Model collapse \\& iterative generation.} Shumailov et al. (2024) show that training on model-generated data leads to distributional collapse. Dohmatob et al. (2024) provide theoretical analysis of iterative retraining dynamics. Briesch et al.\\ (2025) study paraphrasing chains as ``LLM as Broken Telephone,'' finding attractor convergence within 3--5 iterations. These works characterize population-level collapse but do not address sample-level depth estimation.\n\n\\paragraph{Data quality \\& provenance.} Recent work on data curation (Penedo et al., 2024; Wettig et al., 2024) focuses on filtering low-quality text but does not distinguish generation depth. Our downstream utility experiment directly tests whether depth information improves curation, finding no benefit.\n\n\\paragraph{Vocabulary diversity \\& stylometry.} Type-token ratio (TTR), hapax legomena ratio, and lexical diversity metrics have long been used in authorship attribution. We show these surface features capture substantial depth signal (F1 = 0.763 surface-only) but reference model features provide complementary information.\n\n%% ============================================================\n%% 3. METHODOLOGY\n%% ============================================================\n\\section{Methodology}\n\n\\subsection{Problem Formulation}\n\nGiven a text passage $x$, we seek to classify its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d=0$ denotes human-authored seed text, $d=1$ denotes first-pass LLM generation from the seed, and $d \\geq 2$ denotes recursively generated text. The primary evaluation metric is \\emph{leak-free binary F1}: F1 for the gen-1 vs.\\ gen-2+ distinction, excluding gen-0 to avoid seed-sharing leakage artifacts.\n\n\\subsection{Generation Pipeline}\n\nWe construct non-paraphrastic continuation chains: starting from human-authored seed texts (Wikipedia), each depth step feeds the previous output as a continuation prompt to the generator. We generate chains of depth 0--4 using 8 base-model generators from 5 families: Pythia (1B, 2.8B), OLMo-2 (1B), Qwen3 (0.6B, 1.7B, 8B), Llama-3.2 (3B), and Mistral-7B-v0.3.\n\n\\subsection{Differential Depth Response (DDR) Features}\n\nWe extract 7 features per text, computed relative to a reference model (Pythia-410M):\n\n\\paragraph{Surface features (2).} \\emph{Type-token ratio} (TTR): ratio of unique tokens to total tokens. \\emph{Hapax ratio}: fraction of tokens occurring exactly once.\n\n\\paragraph{Reference features (5).} Given the reference model's next-token NLL distribution over the text: \\emph{entropy mean}, \\emph{entropy std}, \\emph{entropy min}, \\emph{entropy max}, and \\emph{tail decay} (rate parameter of exponential fit to the upper tail of the NLL distribution).\n\n\\paragraph{DDR dichotomy.} We characterize each feature's depth trend via Spearman $\\rho$ against depth. Features with $|\\rho| > 0.50$ are classified as \\emph{drifting}; those with $|\\rho| < 0.10$ as \\emph{stationary}. This split reflects a location shift in the NLL distribution under recursive generation: central-tendency statistics (mean, diversity) shift monotonically, while shape statistics (tail behavior, extrema) are approximately preserved.\n\n\\subsection{Classifier}\n\nWe use XGBoost with 5-fold cross-validation for within-distribution evaluation and leave-one-generator-out (LOGO) for cross-generator generalization. LOGO trains on 7 generators and evaluates on the held-out 8th, averaging across all 8 folds.\n\n%% ============================================================\n%% 4. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Data.} We generate chains from 1,000 Wikipedia seed passages per generator, with 5 depth levels (0--4) and default temperature $t = 0.7$ (nucleus sampling, $p = 0.95$). Total dataset: ${\\sim}37{,}500$ records across 8 generators. Texts shorter than 50 tokens after generation are discarded.\n\n\\paragraph{Evaluation protocol.} Primary metric: leak-free binary F1 (gen-1 vs.\\ gen-2+) under LOGO. Secondary: 3-class macro F1 (gen-0/gen-1/gen-2+) and leave-one-family-out (LOFO) binary F1. All confidence intervals are bootstrap 95\\% CIs (10,000 resamples).\n\n\\paragraph{Baselines.} We repurpose four existing detection methods as ordinal depth predictors: FastDetectGPT, Binoculars, LD-Score, and Avg-LogProb (average log-probability under the reference model). Each detector's continuous score is used as a single feature in the same XGBoost LOGO pipeline.\n\n%% ============================================================\n%% 5. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{DDR Characterization and Feature Ablation}\n\nTable~\\ref{tab:feature_trend} reports per-feature depth trends computed via linear regression across depths 0--4 on the Pythia-2.8B subset (${\\sim}4{,}600$ records).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-feature depth trend (linear regression, depths 0--4, Pythia-2.8B).}\n\\label{tab:feature_trend}\n\\begin{tabular}{llccc}\n\\toprule\nFeature & Category & Slope & $R^2$ & Spearman $\\rho$ \\\\\n\\midrule\nhapax\\_ratio & Drifting & $-0.063$ & 0.88 & $-0.63$ \\\\\nTTR & Drifting & $-0.041$ & 0.82 & $-0.61$ \\\\\nentropy\\_mean & Drifting & $-0.089$ & 0.79 & $-0.60$ \\\\\nentropy\\_std & Ambiguous & $-0.031$ & 0.41 & $-0.20$ \\\\\nentropy\\_min & Stationary & $-0.018$ & 0.22 & $-0.15$ \\\\\ntail\\_decay & Stationary & $+0.003$ & 0.04 & $+0.04$ \\\\\nentropy\\_max & Stationary & $+0.008$ & 0.07 & $+0.05$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree features exhibit strong monotonic drift with depth ($|\\rho| \\geq 0.60$, $R^2 \\geq 0.79$): hapax ratio, TTR, and entropy mean. Two shape features show near-zero correlation ($|\\rho| < 0.10$): tail decay and entropy max. Entropy std falls in an ambiguous zone ($\\rho = -0.20$, $R^2 = 0.41$), suggesting a continuous rather than strictly bimodal response spectrum.\n\nTable~\\ref{tab:ablation} reports feature ablation results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature ablation: 5-fold CV macro F1 (Pythia-2.8B, ${\\sim}4{,}600$ records).}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\nFeature Set & Macro F1 & 95\\% CI & $\\Delta$ vs Full \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.833] & --- \\\\\nSurface-only (TTR + hapax) & 0.763 & [0.747, 0.774] & $-5.7$ pp \\\\\nReference-only (5 entropy) & 0.719 & [0.706, 0.733] & $-10.1$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full 7-feature set outperforms both subsets (McNemar $p \\approx 0$ for both comparisons), confirming complementarity. Surface features alone retain 93\\% of the full signal (0.763/0.820), indicating that vocabulary diversity metrics capture the majority of depth information. Reference features contribute an additional 5.7 pp, primarily improving gen-1/gen-2+ discrimination.\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:logo} reports LOGO binary F1 across all 8 generators (${\\sim}37{,}500$ records total).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-generator-out (LOGO) binary F1 (gen-1 vs.\\ gen-2+).}\n\\label{tab:logo}\n\\begin{tabular}{llccc}\n\\toprule\nHeld-out Generator & Family & Size & Binary F1 & 95\\% CI \\\\\n\\midrule\nPythia-1B & Pythia & 1.0B & 0.724 & [0.707, 0.741] \\\\\nPythia-2.8B & Pythia & 2.8B & 0.711 & [0.693, 0.729] \\\\\nQwen3-0.6B & Qwen & 0.6B & 0.702 & [0.682, 0.722] \\\\\nQwen3-1.7B & Qwen & 1.7B & 0.698 & [0.678, 0.718] \\\\\nLlama-3.2-3B & Llama & 3.0B & 0.688 & [0.668, 0.708] \\\\\nOLMo-2-1B & OLMo & 1.5B & 0.679 & [0.658, 0.700] \\\\\nQwen3-8B & Qwen & 8.0B & 0.647 & [0.624, 0.670] \\\\\nMistral-7B-v0.3 & Mistral & 7.0B & 0.633 & [0.609, 0.657] \\\\\n\\midrule\n\\textbf{Average} & --- & --- & \\textbf{0.694} & [0.688, 0.700] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe average LOGO binary F1 is 0.694, with a per-generator range of 9.1 pp (Pythia-1B 0.724 to Mistral-7B 0.633). Performance degrades with model scale: the two largest generators (Mistral-7B at 0.633, Qwen3-8B at 0.647) yield the lowest F1, consistent with larger models compressing inter-depth feature margins. 86\\% of binary classification errors are false negatives (gen-2+ misclassified as gen-1), indicating systematic under-detection of deeper generations.\n\nTable~\\ref{tab:lofo} shows leave-one-family-out (LOFO) results, confirming cross-family transfer with a modest 0.8 pp average degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-family-out (LOFO) binary F1.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-out Family & Binary F1 & $\\Delta$ vs LOGO \\\\\n\\midrule\nPythia & 0.668 & $-2.6$ pp \\\\\nQwen & 0.672 & $-2.2$ pp \\\\\nOLMo & 0.714 & $+2.0$ pp \\\\\nLlama & 0.701 & $+0.7$ pp \\\\\nMistral & 0.673 & $-2.1$ pp \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.686} & $\\mathbf{-0.8}$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Existing Detectors}\n\nTable~\\ref{tab:baseline} compares the 7-feature ensemble against existing detectors repurposed as ordinal depth predictors under the same LOGO protocol.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ordinal depth classification: 7-feature vs.\\ existing detectors (LOGO). Bootstrap $p$ tests 7-feature vs.\\ each baseline.}\n\\label{tab:baseline}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & 3-class F1 & 95\\% CI & Binary F1 & $p$ \\\\\n\\midrule\n\\textbf{7-feature} & \\textbf{0.798} & [0.786, 0.799] & \\textbf{0.705} & --- \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 0.695 & $<$0.001 \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0.672 & $<$0.001 \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 0.601 & $<$0.001 \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 0.558 & $<$0.001 \\\\\n4-det + surface & 0.795 & [0.781, 0.808] & 0.708 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7-feature ensemble significantly outperforms all single detectors in 3-class F1 ($p < 0.001$). However, the margin over Avg-LogProb is modest (3.3 pp), and a multi-detector ensemble (4 detectors + surface features) achieves near-identical performance (3-class 0.795 vs.\\ 0.798; binary 0.708 vs.\\ 0.705, $p = 0.72$). The wide confidence intervals for single detectors (e.g., Avg-LogProb CI spanning 0.616--0.820) reflect high cross-generator variance.\n\n\\subsection{Cross-Model Chains}\n\nTable~\\ref{tab:cross_model} compares single-model chains (same generator at every depth step) with cross-model chains (different generator per step).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model vs.\\ single-model chain classification.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccc}\n\\toprule\nSetting & Binary F1 & 3-class F1 & LOGO Binary F1 \\\\\n\\midrule\nSingle-model & 0.694 & 0.762 & 0.694 \\\\\nCross-model & 0.764 & 0.789 & 0.830 \\\\\n\\midrule\n$\\Delta$ & $+7.0$ pp & $+2.7$ pp & $+13.6$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains yield substantially higher F1 (+7.0 pp binary, +13.6 pp LOGO), as generator switching across depth steps introduces additional distributional shifts beyond the depth signal alone. The single-model setting isolates the pure depth signal and is the more conservative evaluation.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\nTable~\\ref{tab:downstream} reports downstream causal language model perplexity when fine-tuning OLMo-1B on depth-stratified data subsets (3 random seeds, sample-count-matched).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream CLM perplexity by training data depth composition (3 seeds, OLMo-1B).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nVariant & Train Size & PPL (mean $\\pm$ std) & $\\Delta$ vs Size-matched \\\\\n\\midrule\nAll depths & 12,299 & 2.335 $\\pm$ 0.0003 & --- \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.0003 & ref \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.0004 & $+0.020$ \\\\\nBinary filtered & 3,951 & 2.389 $\\pm$ 0.0006 & $+0.022$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.0006 & $+0.314$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth-aware filtering provides no advantage over random subsampling at equal sample count: depth 0+1 (ppl = 2.387) and binary-filtered (2.389) are statistically equivalent to size-matched random (2.367) under TOST at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$). The ranking \\emph{all} $<$ \\emph{size-matched} $<$ \\emph{depth 0+1} $\\approx$ \\emph{binary filtered} $\\ll$ \\emph{depth 0 only} indicates that more data is always better, and depth-based selection slightly hurts by discarding useful training signal.\n\nThis negative finding challenges an implicit assumption in the model collapse literature: that distributional shift under recursive generation necessarily entails quality degradation. The DDR-characterized drift (vocabulary impoverishment, entropy compression) does not translate to worse downstream training outcomes at these depth levels.\n\n%% ============================================================\n%% 6. ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\subsection{Depth Resolution Limits}\n\nTable~\\ref{tab:ordinal} evaluates finer-grained 5-class ordinal classification (gen-0 through gen-4).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ordinal depth classification resolution.}\n\\label{tab:ordinal}\n\\begin{tabular}{llcc}\n\\toprule\nGranularity & Method & Macro F1 \\\\\n\\midrule\n3-class & XGBoost & 0.762 \\\\\n5-class & XGBoost & 0.498 \\\\\n5-class & CORAL & 0.502 \\\\\n5-class & Frank-Hall & 0.491 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class F1 drops to 0.498, and ordinal methods (CORAL, Frank-Hall) provide no improvement, indicating that depth signal does not possess ordinal structure beyond coarse binning. Per-depth recall analysis reveals the structure: gen-0 recall is high (0.92) but gen-2/3/4 are poorly separable (recall 0.29--0.41, inter-class confusion 48--51\\%). The depth signal is effectively binary-plus-one: source-adjacent (gen-0/1) versus deep (gen-2+), with limited resolution within either group.\n\n\\subsection{Scale Effects}\n\nTable~\\ref{tab:scale} examines how model scale affects depth signal strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale effect: depth signal degradation with generator size.}\n\\label{tab:scale}\n\\begin{tabular}{llcccc}\n\\toprule\nGenerator & Size & LOGO Binary F1 & hapax $\\rho$ & entropy\\_mean $\\rho$ \\\\\n\\midrule\nPythia-1B & 1.0B & 0.724 & $-0.65$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.698 & $-0.63$ & $-0.60$ \\\\\nPythia-2.8B & 2.8B & 0.711 & $-0.63$ & $-0.60$ \\\\\nQwen3-8B & 8.0B & 0.647 & $-0.56$ & $-0.48$ \\\\\n\\midrule\n\\textbf{Trend} & --- & \\textbf{Declining} & \\multicolumn{2}{c}{\\textbf{Compressing}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3-8B shows a 10.6 pp degradation in LOGO binary F1 relative to the 6-generator average, with feature drift magnitudes compressed to ${\\sim}72\\%$ of smaller models. The DDR pattern (drifting $>$ stationary separation) is preserved, but weakened. This suggests that higher-capacity models produce more uniform output across depth levels, compressing the inter-depth distributional margins that DDR exploits.\n\n\\subsection{Reference Model Independence}\n\nTable~\\ref{tab:ref_model} tests whether DDR patterns persist across different reference models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-reference-model DDR comparison.}\n\\label{tab:ref_model}\n\\begin{tabular}{lcccc}\n\\toprule\nReference Model & Size & LOGO F1 & entropy\\_mean $\\rho$ & Drift range \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & $-0.60$ & [$-1.19$, $-1.40$] \\\\\nOLMo-2-1B & 1.5B & 0.807 & $-0.50$ & [$-0.61$, $-0.91$] \\\\\nQwen3-0.6B & 0.6B & 0.816 & $-0.56$ & [$-0.96$, $-1.35$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDrift direction is consistent across all reference models (all entropy\\_mean $\\rho < 0$, all shape features $|\\rho| < 0.10$), confirming that DDR is not an artifact of the specific reference model. However, drift \\emph{magnitude} varies substantially: OLMo reference produces only ${\\sim}55\\%$ of Pythia's drift magnitude. LOGO F1 remains comparable (0.803--0.816), indicating that classification performance is robust to reference model choice even as the underlying DDR characterization changes in scale.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe introduced generation depth classification and characterized differential depth response (DDR) across 8 base-model generators from 5 families. Central-tendency features drift monotonically with depth while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO (per-generator range: 0.633--0.724), modestly outperforming single detector baselines but matching multi-detector ensembles. The depth signal is effectively limited to 3-class resolution and degrades with model scale.\n\nOur negative downstream finding---depth-aware curation is equivalent to random subsampling for CLM quality---suggests that the distributional shifts characterized by DDR do not entail quality degradation at the depth levels studied. This challenges the assumption that recursive generation necessarily produces inferior training data and positions DDR as a diagnostic framework for understanding distributional dynamics rather than a tool for data curation.\n\n\\paragraph{Limitations.} Three key limitations bound the scope of this work. (1) \\emph{Base models only}: instruction-tuned models show substantially degraded depth signal (LOGO F1 drops to 0.338 for OLMo-Instruct vs.\\ 0.763 for OLMo-Base), restricting applicability to base model outputs---a shrinking fraction of deployed LLM-generated text. (2) \\emph{Temperature sensitivity}: reliable performance is restricted to $t \\in [0.5, 0.9]$; at $t = 1.0$, entropy mean $\\rho$ drops to near-zero and cross-temperature transfer degrades severely. (3) \\emph{Scale degradation}: larger generators (7B+) compress depth signal, and the observed trend suggests further degradation at frontier model scales.\n\n%% ============================================================\n%% APPENDICES\n%% ============================================================\n\\appendix\n\n\\section{Prompt Type Sensitivity}\n\\label{app:prompt}\n\nTable~\\ref{tab:prompt_type} compares three prompt types: continuation, elaboration, and inspired rewriting (Pythia-2.8B, 1000 seeds).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-prompt-type classification and drift statistics (Pythia-2.8B).}\n\\label{tab:prompt_type}\n\\begin{tabular}{lcccccc}\n\\toprule\nPrompt Type & CV F1 & LOPTO F1 & Depth Ret. & ent\\_mean $\\rho$ & hapax $\\rho$ & TTR $\\rho$ \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.557$ & $-0.740$ & $-0.629$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.471$ & $-0.828$ & $-0.666$ \\\\\nRewriting & 0.737 & 0.734 & 0.939 & $-0.477$ & $-0.800$ & $-0.659$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContinuation chains yield the strongest within-type signal (CV F1 = 0.781), while elaboration and rewriting show higher depth retention but weaker depth discrimination ($\\Delta = 5.1$ pp). Cross-prompt-type transfer (LOPTO) averages 0.753, indicating partial but imperfect generalization.\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{app:para}\n\nTable~\\ref{tab:para} compares paraphrastic and non-paraphrastic (continuation) chains.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paraphrastic vs.\\ non-paraphrastic chain comparison (Pythia-2.8B).}\n\\label{tab:para}\n\\begin{tabular}{lccccc}\n\\toprule\nChain Type & CV F1 & Binary F1 & Depth Ret. & ent\\_mean $\\rho$ & Eff.\\ Classes \\\\\n\\midrule\nContinuation & 0.781 & 0.694 & 0.831 & $-0.557$ & 3 \\\\\nParaphrastic & 0.718 & 0.661 & 0.992 & $-0.390$ & ${\\sim}2$ \\\\\n\\midrule\n$\\Delta$ & $+6.3$ pp & $+3.3$ pp & --- & --- & $+1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nParaphrastic chains exhibit attractor convergence (depth retention 0.992), reducing effective depth classes to ${\\sim}2$. The binary F1 gap ($\\Delta = 3.3$ pp) is moderate, suggesting the depth signal is a generic property of recursive generation rather than unique to non-paraphrastic chains, though non-paraphrastic chains sustain an additional class of depth resolution.\n\n\\section{Multi-Domain Evaluation}\n\\label{app:domain}\n\nTable~\\ref{tab:domain} reports per-domain binary F1 under LOGO evaluation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-domain binary F1 (LOGO across generators).}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & Seeds & Binary F1 & 95\\% CI & $\\Delta$ vs Wiki \\\\\n\\midrule\nWikipedia & 500 & 0.815 & [0.796, 0.834] & --- \\\\\nNews & 500 & 0.712 & [0.690, 0.733] & $-10.3$ pp \\\\\nCode & 500 & 0.687 & [0.664, 0.710] & $-12.8$ pp \\\\\nAcademic & 500 & 0.628 & [0.603, 0.652] & $-18.7$ pp \\\\\n\\midrule\nCross-domain LOGO & 2000 & 0.668 & [0.654, 0.682] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerformance is strongly domain-dependent: Wikipedia (primary training domain) achieves 0.815, while academic text---the domain where LLM contamination is most frequently cited---yields only 0.628 ($\\Delta = -18.7$ pp). Cross-domain LOGO drops to 0.668.\n\n\\section{Robustness to Human Edits}\n\\label{app:edits}\n\nTable~\\ref{tab:edits} evaluates robustness under simulated human editing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Robustness to simulated human edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nPerturbation & Binary F1 & $\\Delta$ vs Baseline & Edit Distance \\\\\n\\midrule\nNone (baseline) & 0.695 & --- & 0.0 \\\\\nRandom 5\\% & 0.650 & $-4.5$ pp & ${\\sim}0.05$ \\\\\nRandom 10\\% & 0.614 & $-8.1$ pp & ${\\sim}0.10$ \\\\\nRandom 20\\% & 0.591 & $-10.4$ pp & ${\\sim}0.20$ \\\\\nLLM rephrase & 0.647 & $-4.5$ pp & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLight editing (5\\% random replacement or LLM rephrasing) reduces binary F1 by 4.5 pp. Degradation is approximately linear with perturbation intensity, suggesting the depth signal resides in surface-level distributional properties susceptible to text modification.\n\n\\section{LD-Score Feature Extension}\n\\label{app:ld}\n\nTable~\\ref{tab:ld} evaluates the addition of LD-Score (character-distribution signature) as an 8th feature.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LD-Score feature addition (3-class LOGO).}\n\\label{tab:ld}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & LOGO F1 & $\\Delta$ \\\\\n\\midrule\n7 features (baseline) & 0.798 & --- \\\\\n7 + LD-Score & 0.802 & $+0.4$ pp \\\\\nLD-Score only & 0.721 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLD-Score alone achieves 3-class F1 = 0.721, but its marginal contribution when added to the 7-feature set is negligible (0.4 pp), indicating substantial information overlap with existing features.\n\n\\section{End-to-End QLoRA Classifier}\n\\label{app:qlora}\n\nTable~\\ref{tab:qlora} compares the 7-feature ensemble with end-to-end QLoRA fine-tuned classifiers.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{End-to-end (QLoRA) vs.\\ 7-feature ensemble.}\n\\label{tab:qlora}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Model & 3-class F1 & Binary F1 & Cost \\\\\n\\midrule\n7-feature XGBoost & --- & 0.762 & 0.694 & $1\\times$ \\\\\nQLoRA & OLMo-Instruct & 0.888 $\\pm$ 0.007 & 0.836 $\\pm$ 0.010 & $47\\times$ \\\\\nQLoRA & Qwen-Instruct & 0.907 $\\pm$ 0.008 & 0.867 $\\pm$ 0.014 & $47\\times$ \\\\\nQLoRA & OLMo-Base & 0.859 $\\pm$ 0.004 & 0.793 $\\pm$ 0.010 & $47\\times$ \\\\\nQLoRA & Qwen-Base & 0.904 $\\pm$ 0.009 & 0.860 $\\pm$ 0.012 & $47\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQLoRA classifiers substantially outperform the 7-feature ensemble ($+12.6$ to $+17.3$ pp binary F1), indicating the text contains substantially more depth signal than the 7-feature set captures. The 7-feature ensemble trades absolute performance for $47\\times$ lower inference cost. Notably, instruct-model QLoRA classifiers achieve the highest F1, suggesting that instruction tuning degrades the specific features selected rather than the depth signal itself.\n\n\\section{Text Length Control}\n\\label{app:length}\n\nTable~\\ref{tab:length} controls for text length as a potential confound.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Length control analysis.}\n\\label{tab:length}\n\\begin{tabular}{lcc}\n\\toprule\nCondition & Binary F1 & $\\Delta$ vs Unmatched \\\\\n\\midrule\nUnmatched (original) & 0.770 & --- \\\\\nLength-normalized features & 0.748 & $-2.2$ pp \\\\\nLength-matched subsample & 0.724 & $-4.6$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLength-depth correlation is weak ($\\rho = 0.12$, $p = 0.001$). Length-matched subsampling reduces binary F1 by 4.6 pp (0.770 $\\to$ 0.724), indicating that approximately 6\\% of the signal is attributable to text length. Feature depth trends (TTR, hapax ratio) are preserved after length normalization, confirming that the core DDR pattern is not a length artifact.\n\n%% ============================================================\n%% REFERENCES (placeholder)\n%% ============================================================\n\\begin{thebibliography}{20}\n\\bibitem[1]{mitchell2023detectgpt} E.~Mitchell et al. DetectGPT: Zero-shot machine-generated text detection using probability curvature. In \\emph{ICML}, 2023.\n\\bibitem[2]{bao2024fast} G.~Bao et al. Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature. In \\emph{ICLR}, 2024.\n\\bibitem[3]{hans2024binoculars} A.~Hans et al. Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text. In \\emph{ICML}, 2024.\n\\bibitem[4]{gehrmann2019gltr} S.~Gehrmann et al. GLTR: Statistical detection and visualization of generated text. In \\emph{ACL}, 2019.\n\\bibitem[5]{shumailov2024curse} I.~Shumailov et al. AI models collapse when trained on recursively generated data. \\emph{Nature}, 2024.\n\\bibitem[6]{dohmatob2024tale} E.~Dohmatob et al. A tale of tails: Model collapse as a change of scaling laws. In \\emph{ICML}, 2024.\n\\bibitem[7]{briesch2025broken} M.~Briesch et al. LLM as broken telephone: Iterative paraphrasing converges to attractor cycles. In \\emph{ACL}, 2025.\n\\bibitem[8]{penedo2024fineweb} G.~Penedo et al. The FineWeb datasets: Decanting the web for the finest text data at scale. \\emph{NeurIPS Datasets and Benchmarks}, 2024.\n\\bibitem[9]{wettig2024qurating} A.~Wettig et al. QuRating: Selecting high-quality data for training language models. In \\emph{ICML}, 2024.\n\\bibitem[10]{tulchinskii2024ld} E.~Tulchinskii et al. Intrinsic dimension estimation for robust detection of AI-generated texts. In \\emph{NeurIPS}, 2024.\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d41e8f17-6625-4aa6-b50c-c7217ec08ace",
  "isSidechain": false,
  "requestId": "req_011CbGUvs5SrG4G95zYzydff",
  "type": "assistant",
  "uuid": "d2f0c22c-5a99-4f7b-8eb2-2280ab1751ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqZjeQgzQSxz4a2zALATCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 52103,
      "output_tokens": 10936,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10936,
          "cache_read_input_tokens": 52103,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 264
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

_source line 23 · 2026-05-21T22:16:07.308Z_

<details><summary>↩ Tool result · `toolu_01Ste7TkKNcXjkcRJnk9q1Tx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2f0c22c-5a99-4f7b-8eb2-2280ab1751ec",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "110381ec-1cda-4f63-ace8-d25dd4c03978",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{xcolor}\n\\usepackage{amsmath}\n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\n\\title{Differential Depth Response in Recursive Autoregressive Generation:\\\\Understanding Distributional Dynamics Beyond Binary Detection}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text that has been recursively generated through multiple autoregressive passes. Current detection methods provide only binary real-versus-synthetic classification, conflating qualitatively different material along the generation chain. We formulate \\emph{generation depth classification} (gen-0/gen-1/gen-2+) and characterize \\textbf{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while distributional-shape features (tail decay, entropy max) remain near-stationary ($|\\rho| < 0.10$). Across 8 base-model generators from 5 families (0.6B--8B parameters), a lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under leave-one-generator-out (LOGO) evaluation, outperforming existing detector baselines repurposed as ordinal predictors (best single: Avg-LogProb 0.765 3-class, $\\Delta = -3.3$ pp). We further show that depth-aware data curation is statistically equivalent to random subsampling for downstream causal language model quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm$2\\% margin), establishing that distributional shift under recursive generation does not entail quality degradation---challenging implicit assumptions in the model collapse literature. The depth signal degrades substantially under instruction tuning and at high temperature, restricting the current scope to base models at moderate temperatures.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models increasingly generate text that re-enters training pipelines through web scraping, creating recursive feedback loops. Estimates suggest 7--17\\% of recent scientific publications contain LLM-generated content, and this proportion is growing. Understanding the provenance of such text---specifically, \\emph{how many autoregressive passes} separate it from human-authored source material---is important for characterizing the distributional dynamics of these feedback loops.\n\nBinary detection methods (FastDetectGPT, Binoculars, LD-Score) classify text as human or machine-generated but cannot distinguish first-generation output (gen-1), which retains much of the source distribution's lexical properties, from deeper generations (gen-2+), which exhibit measurably reduced vocabulary diversity and compressed perplexity. This conflation obscures important distributional structure: gen-1 text may be nearly indistinguishable from human writing on surface metrics, while gen-4+ text shows substantial vocabulary impoverishment.\n\nWe formulate \\emph{generation depth classification} as a new task and introduce the \\textbf{differential depth response} (DDR) framework for characterizing how distributional features evolve across recursive generation steps. Our central finding is that features split into two behavioral categories: \\emph{drifting} features (hapax ratio, TTR, entropy mean) that exhibit strong monotonic trends with depth, and \\emph{stationary} features (tail decay, entropy max) whose distributions remain approximately invariant. This split is consistent with recursive autoregressive generation inducing a location shift in the next-token log-likelihood (NLL) distribution while approximately preserving its shape.\n\nWe make three contributions:\n\\begin{enumerate}[nosep]\n\\item \\textbf{Task formulation \\& DDR characterization}: Generation depth classification beyond binary detection, with empirical validation of the drifting/stationary dichotomy across 8 generators from 5 model families (0.6B--8B).\n\\item \\textbf{Lightweight depth classifier}: A 7-feature XGBoost ensemble achieving leak-free binary F1 = 0.694 under 8-generator LOGO, using a single 410M reference model.\n\\item \\textbf{Negative finding}: Depth-aware data curation provides no benefit over random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{AI text detection.} Perplexity-based detectors leverage statistical properties of model-generated text. DetectGPT~\\citep{mitchell2023detectgpt} uses log-probability curvature; Fast-DetectGPT~\\citep{bao2024fast} replaces perturbation with conditional sampling; Binoculars~\\citep{hans2024binoculars} contrasts two models' cross-entropy; GLTR~\\citep{gehrmann2019gltr} visualizes token-level statistics. All operate in a binary detection paradigm and do not address generation depth.\n\n\\paragraph{Model collapse \\& iterative generation.} Shumailov et al. (2024) show that training on model-generated data leads to distributional collapse. Dohmatob et al. (2024) provide theoretical analysis of iterative retraining dynamics. Briesch et al.\\ (2025) study paraphrasing chains as ``LLM as Broken Telephone,'' finding attractor convergence within 3--5 iterations. These works characterize population-level collapse but do not address sample-level depth estimation.\n\n\\paragraph{Data quality \\& provenance.} Recent work on data curation (Penedo et al., 2024; Wettig et al., 2024) focuses on filtering low-quality text but does not distinguish generation depth. Our downstream utility experiment directly tests whether depth information improves curation, finding no benefit.\n\n\\paragraph{Vocabulary diversity \\& stylometry.} Type-token ratio (TTR), hapax legomena ratio, and lexical diversity metrics have long been used in authorship attribution. We show these surface features capture substantial depth signal (F1 = 0.763 surface-only) but reference model features provide complementary information.\n\n%% ============================================================\n%% 3. METHODOLOGY\n%% ============================================================\n\\section{Methodology}\n\n\\subsection{Problem Formulation}\n\nGiven a text passage $x$, we seek to classify its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d=0$ denotes human-authored seed text, $d=1$ denotes first-pass LLM generation from the seed, and $d \\geq 2$ denotes recursively generated text. The primary evaluation metric is \\emph{leak-free binary F1}: F1 for the gen-1 vs.\\ gen-2+ distinction, excluding gen-0 to avoid seed-sharing leakage artifacts.\n\n\\subsection{Generation Pipeline}\n\nWe construct non-paraphrastic continuation chains: starting from human-authored seed texts (Wikipedia), each depth step feeds the previous output as a continuation prompt to the generator. We generate chains of depth 0--4 using 8 base-model generators from 5 families: Pythia (1B, 2.8B), OLMo-2 (1B), Qwen3 (0.6B, 1.7B, 8B), Llama-3.2 (3B), and Mistral-7B-v0.3.\n\n\\subsection{Differential Depth Response (DDR) Features}\n\nWe extract 7 features per text, computed relative to a reference model (Pythia-410M):\n\n\\paragraph{Surface features (2).} \\emph{Type-token ratio} (TTR): ratio of unique tokens to total tokens. \\emph{Hapax ratio}: fraction of tokens occurring exactly once.\n\n\\paragraph{Reference features (5).} Given the reference model's next-token NLL distribution over the text: \\emph{entropy mean}, \\emph{entropy std}, \\emph{entropy min}, \\emph{entropy max}, and \\emph{tail decay} (rate parameter of exponential fit to the upper tail of the NLL distribution).\n\n\\paragraph{DDR dichotomy.} We characterize each feature's depth trend via Spearman $\\rho$ against depth. Features with $|\\rho| > 0.50$ are classified as \\emph{drifting}; those with $|\\rho| < 0.10$ as \\emph{stationary}. This split reflects a location shift in the NLL distribution under recursive generation: central-tendency statistics (mean, diversity) shift monotonically, while shape statistics (tail behavior, extrema) are approximately preserved.\n\n\\subsection{Classifier}\n\nWe use XGBoost with 5-fold cross-validation for within-distribution evaluation and leave-one-generator-out (LOGO) for cross-generator generalization. LOGO trains on 7 generators and evaluates on the held-out 8th, averaging across all 8 folds.\n\n%% ============================================================\n%% 4. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Data.} We generate chains from 1,000 Wikipedia seed passages per generator, with 5 depth levels (0--4) and default temperature $t = 0.7$ (nucleus sampling, $p = 0.95$). Total dataset: ${\\sim}37{,}500$ records across 8 generators. Texts shorter than 50 tokens after generation are discarded.\n\n\\paragraph{Evaluation protocol.} Primary metric: leak-free binary F1 (gen-1 vs.\\ gen-2+) under LOGO. Secondary: 3-class macro F1 (gen-0/gen-1/gen-2+) and leave-one-family-out (LOFO) binary F1. All confidence intervals are bootstrap 95\\% CIs (10,000 resamples).\n\n\\paragraph{Baselines.} We repurpose four existing detection methods as ordinal depth predictors: FastDetectGPT, Binoculars, LD-Score, and Avg-LogProb (average log-probability under the reference model). Each detector's continuous score is used as a single feature in the same XGBoost LOGO pipeline.\n\n%% ============================================================\n%% 5. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{DDR Characterization and Feature Ablation}\n\nTable~\\ref{tab:feature_trend} reports per-feature depth trends computed via linear regression across depths 0--4 on the Pythia-2.8B subset (${\\sim}4{,}600$ records).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-feature depth trend (linear regression, depths 0--4, Pythia-2.8B).}\n\\label{tab:feature_trend}\n\\begin{tabular}{llccc}\n\\toprule\nFeature & Category & Slope & $R^2$ & Spearman $\\rho$ \\\\\n\\midrule\nhapax\\_ratio & Drifting & $-0.063$ & 0.88 & $-0.63$ \\\\\nTTR & Drifting & $-0.041$ & 0.82 & $-0.61$ \\\\\nentropy\\_mean & Drifting & $-0.089$ & 0.79 & $-0.60$ \\\\\nentropy\\_std & Ambiguous & $-0.031$ & 0.41 & $-0.20$ \\\\\nentropy\\_min & Stationary & $-0.018$ & 0.22 & $-0.15$ \\\\\ntail\\_decay & Stationary & $+0.003$ & 0.04 & $+0.04$ \\\\\nentropy\\_max & Stationary & $+0.008$ & 0.07 & $+0.05$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree features exhibit strong monotonic drift with depth ($|\\rho| \\geq 0.60$, $R^2 \\geq 0.79$): hapax ratio, TTR, and entropy mean. Two shape features show near-zero correlation ($|\\rho| < 0.10$): tail decay and entropy max. Entropy std falls in an ambiguous zone ($\\rho = -0.20$, $R^2 = 0.41$), suggesting a continuous rather than strictly bimodal response spectrum.\n\nTable~\\ref{tab:ablation} reports feature ablation results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature ablation: 5-fold CV macro F1 (Pythia-2.8B, ${\\sim}4{,}600$ records).}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\nFeature Set & Macro F1 & 95\\% CI & $\\Delta$ vs Full \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.833] & --- \\\\\nSurface-only (TTR + hapax) & 0.763 & [0.747, 0.774] & $-5.7$ pp \\\\\nReference-only (5 entropy) & 0.719 & [0.706, 0.733] & $-10.1$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full 7-feature set outperforms both subsets (McNemar $p \\approx 0$ for both comparisons), confirming complementarity. Surface features alone retain 93\\% of the full signal (0.763/0.820), indicating that vocabulary diversity metrics capture the majority of depth information. Reference features contribute an additional 5.7 pp, primarily improving gen-1/gen-2+ discrimination.\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:logo} reports LOGO binary F1 across all 8 generators (${\\sim}37{,}500$ records total).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-generator-out (LOGO) binary F1 (gen-1 vs.\\ gen-2+).}\n\\label{tab:logo}\n\\begin{tabular}{llccc}\n\\toprule\nHeld-out Generator & Family & Size & Binary F1 & 95\\% CI \\\\\n\\midrule\nPythia-1B & Pythia & 1.0B & 0.724 & [0.707, 0.741] \\\\\nPythia-2.8B & Pythia & 2.8B & 0.711 & [0.693, 0.729] \\\\\nQwen3-0.6B & Qwen & 0.6B & 0.702 & [0.682, 0.722] \\\\\nQwen3-1.7B & Qwen & 1.7B & 0.698 & [0.678, 0.718] \\\\\nLlama-3.2-3B & Llama & 3.0B & 0.688 & [0.668, 0.708] \\\\\nOLMo-2-1B & OLMo & 1.5B & 0.679 & [0.658, 0.700] \\\\\nQwen3-8B & Qwen & 8.0B & 0.647 & [0.624, 0.670] \\\\\nMistral-7B-v0.3 & Mistral & 7.0B & 0.633 & [0.609, 0.657] \\\\\n\\midrule\n\\textbf{Average} & --- & --- & \\textbf{0.694} & [0.688, 0.700] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe average LOGO binary F1 is 0.694, with a per-generator range of 9.1 pp (Pythia-1B 0.724 to Mistral-7B 0.633). Performance degrades with model scale: the two largest generators (Mistral-7B at 0.633, Qwen3-8B at 0.647) yield the lowest F1, consistent with larger models compressing inter-depth feature margins. 86\\% of binary classification errors are false negatives (gen-2+ misclassified as gen-1), indicating systematic under-detection of deeper generations.\n\nTable~\\ref{tab:lofo} shows leave-one-family-out (LOFO) results, confirming cross-family transfer with a modest 0.8 pp average degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leave-one-family-out (LOFO) binary F1.}\n\\label{tab:lofo}\n\\begin{tabular}{lcc}\n\\toprule\nHeld-out Family & Binary F1 & $\\Delta$ vs LOGO \\\\\n\\midrule\nPythia & 0.668 & $-2.6$ pp \\\\\nQwen & 0.672 & $-2.2$ pp \\\\\nOLMo & 0.714 & $+2.0$ pp \\\\\nLlama & 0.701 & $+0.7$ pp \\\\\nMistral & 0.673 & $-2.1$ pp \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.686} & $\\mathbf{-0.8}$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Comparison with Existing Detectors}\n\nTable~\\ref{tab:baseline} compares the 7-feature ensemble against existing detectors repurposed as ordinal depth predictors under the same LOGO protocol.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ordinal depth classification: 7-feature vs.\\ existing detectors (LOGO). Bootstrap $p$ tests 7-feature vs.\\ each baseline.}\n\\label{tab:baseline}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & 3-class F1 & 95\\% CI & Binary F1 & $p$ \\\\\n\\midrule\n\\textbf{7-feature} & \\textbf{0.798} & [0.786, 0.799] & \\textbf{0.705} & --- \\\\\nAvg-LogProb & 0.765 & [0.616, 0.820] & 0.695 & $<$0.001 \\\\\nLD-Score & 0.721 & [0.588, 0.770] & 0.672 & $<$0.001 \\\\\nFastDetectGPT & 0.627 & [0.511, 0.762] & 0.601 & $<$0.001 \\\\\nBinoculars & 0.579 & [0.405, 0.664] & 0.558 & $<$0.001 \\\\\n4-det + surface & 0.795 & [0.781, 0.808] & 0.708 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7-feature ensemble significantly outperforms all single detectors in 3-class F1 ($p < 0.001$). However, the margin over Avg-LogProb is modest (3.3 pp), and a multi-detector ensemble (4 detectors + surface features) achieves near-identical performance (3-class 0.795 vs.\\ 0.798; binary 0.708 vs.\\ 0.705, $p = 0.72$). The wide confidence intervals for single detectors (e.g., Avg-LogProb CI spanning 0.616--0.820) reflect high cross-generator variance.\n\n\\subsection{Cross-Model Chains}\n\nTable~\\ref{tab:cross_model} compares single-model chains (same generator at every depth step) with cross-model chains (different generator per step).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model vs.\\ single-model chain classification.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccc}\n\\toprule\nSetting & Binary F1 & 3-class F1 & LOGO Binary F1 \\\\\n\\midrule\nSingle-model & 0.694 & 0.762 & 0.694 \\\\\nCross-model & 0.764 & 0.789 & 0.830 \\\\\n\\midrule\n$\\Delta$ & $+7.0$ pp & $+2.7$ pp & $+13.6$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains yield substantially higher F1 (+7.0 pp binary, +13.6 pp LOGO), as generator switching across depth steps introduces additional distributional shifts beyond the depth signal alone. The single-model setting isolates the pure depth signal and is the more conservative evaluation.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\nTable~\\ref{tab:downstream} reports downstream causal language model perplexity when fine-tuning OLMo-1B on depth-stratified data subsets (3 random seeds, sample-count-matched).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream CLM perplexity by training data depth composition (3 seeds, OLMo-1B).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nVariant & Train Size & PPL (mean $\\pm$ std) & $\\Delta$ vs Size-matched \\\\\n\\midrule\nAll depths & 12,299 & 2.335 $\\pm$ 0.0003 & --- \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.0003 & ref \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.0004 & $+0.020$ \\\\\nBinary filtered & 3,951 & 2.389 $\\pm$ 0.0006 & $+0.022$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.0006 & $+0.314$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth-aware filtering provides no advantage over random subsampling at equal sample count: depth 0+1 (ppl = 2.387) and binary-filtered (2.389) are statistically equivalent to size-matched random (2.367) under TOST at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$). The ranking \\emph{all} $<$ \\emph{size-matched} $<$ \\emph{depth 0+1} $\\approx$ \\emph{binary filtered} $\\ll$ \\emph{depth 0 only} indicates that more data is always better, and depth-based selection slightly hurts by discarding useful training signal.\n\nThis negative finding challenges an implicit assumption in the model collapse literature: that distributional shift under recursive generation necessarily entails quality degradation. The DDR-characterized drift (vocabulary impoverishment, entropy compression) does not translate to worse downstream training outcomes at these depth levels.\n\n%% ============================================================\n%% 6. ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\subsection{Depth Resolution Limits}\n\nTable~\\ref{tab:ordinal} evaluates finer-grained 5-class ordinal classification (gen-0 through gen-4).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Ordinal depth classification resolution.}\n\\label{tab:ordinal}\n\\begin{tabular}{llcc}\n\\toprule\nGranularity & Method & Macro F1 \\\\\n\\midrule\n3-class & XGBoost & 0.762 \\\\\n5-class & XGBoost & 0.498 \\\\\n5-class & CORAL & 0.502 \\\\\n5-class & Frank-Hall & 0.491 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class F1 drops to 0.498, and ordinal methods (CORAL, Frank-Hall) provide no improvement, indicating that depth signal does not possess ordinal structure beyond coarse binning. Per-depth recall analysis reveals the structure: gen-0 recall is high (0.92) but gen-2/3/4 are poorly separable (recall 0.29--0.41, inter-class confusion 48--51\\%). The depth signal is effectively binary-plus-one: source-adjacent (gen-0/1) versus deep (gen-2+), with limited resolution within either group.\n\n\\subsection{Scale Effects}\n\nTable~\\ref{tab:scale} examines how model scale affects depth signal strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale effect: depth signal degradation with generator size.}\n\\label{tab:scale}\n\\begin{tabular}{llcccc}\n\\toprule\nGenerator & Size & LOGO Binary F1 & hapax $\\rho$ & entropy\\_mean $\\rho$ \\\\\n\\midrule\nPythia-1B & 1.0B & 0.724 & $-0.65$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.698 & $-0.63$ & $-0.60$ \\\\\nPythia-2.8B & 2.8B & 0.711 & $-0.63$ & $-0.60$ \\\\\nQwen3-8B & 8.0B & 0.647 & $-0.56$ & $-0.48$ \\\\\n\\midrule\n\\textbf{Trend} & --- & \\textbf{Declining} & \\multicolumn{2}{c}{\\textbf{Compressing}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3-8B shows a 10.6 pp degradation in LOGO binary F1 relative to the 6-generator average, with feature drift magnitudes compressed to ${\\sim}72\\%$ of smaller models. The DDR pattern (drifting $>$ stationary separation) is preserved, but weakened. This suggests that higher-capacity models produce more uniform output across depth levels, compressing the inter-depth distributional margins that DDR exploits.\n\n\\subsection{Reference Model Independence}\n\nTable~\\ref{tab:ref_model} tests whether DDR patterns persist across different reference models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-reference-model DDR comparison.}\n\\label{tab:ref_model}\n\\begin{tabular}{lcccc}\n\\toprule\nReference Model & Size & LOGO F1 & entropy\\_mean $\\rho$ & Drift range \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & $-0.60$ & [$-1.19$, $-1.40$] \\\\\nOLMo-2-1B & 1.5B & 0.807 & $-0.50$ & [$-0.61$, $-0.91$] \\\\\nQwen3-0.6B & 0.6B & 0.816 & $-0.56$ & [$-0.96$, $-1.35$] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDrift direction is consistent across all reference models (all entropy\\_mean $\\rho < 0$, all shape features $|\\rho| < 0.10$), confirming that DDR is not an artifact of the specific reference model. However, drift \\emph{magnitude} varies substantially: OLMo reference produces only ${\\sim}55\\%$ of Pythia's drift magnitude. LOGO F1 remains comparable (0.803--0.816), indicating that classification performance is robust to reference model choice even as the underlying DDR characterization changes in scale.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe introduced generation depth classification and characterized differential depth response (DDR) across 8 base-model generators from 5 families. Central-tendency features drift monotonically with depth while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO (per-generator range: 0.633--0.724), modestly outperforming single detector baselines but matching multi-detector ensembles. The depth signal is effectively limited to 3-class resolution and degrades with model scale.\n\nOur negative downstream finding---depth-aware curation is equivalent to random subsampling for CLM quality---suggests that the distributional shifts characterized by DDR do not entail quality degradation at the depth levels studied. This challenges the assumption that recursive generation necessarily produces inferior training data and positions DDR as a diagnostic framework for understanding distributional dynamics rather than a tool for data curation.\n\n\\paragraph{Limitations.} Three key limitations bound the scope of this work. (1) \\emph{Base models only}: instruction-tuned models show substantially degraded depth signal (LOGO F1 drops to 0.338 for OLMo-Instruct vs.\\ 0.763 for OLMo-Base), restricting applicability to base model outputs---a shrinking fraction of deployed LLM-generated text. (2) \\emph{Temperature sensitivity}: reliable performance is restricted to $t \\in [0.5, 0.9]$; at $t = 1.0$, entropy mean $\\rho$ drops to near-zero and cross-temperature transfer degrades severely. (3) \\emph{Scale degradation}: larger generators (7B+) compress depth signal, and the observed trend suggests further degradation at frontier model scales.\n\n%% ============================================================\n%% APPENDICES\n%% ============================================================\n\\appendix\n\n\\section{Prompt Type Sensitivity}\n\\label{app:prompt}\n\nTable~\\ref{tab:prompt_type} compares three prompt types: continuation, elaboration, and inspired rewriting (Pythia-2.8B, 1000 seeds).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-prompt-type classification and drift statistics (Pythia-2.8B).}\n\\label{tab:prompt_type}\n\\begin{tabular}{lcccccc}\n\\toprule\nPrompt Type & CV F1 & LOPTO F1 & Depth Ret. & ent\\_mean $\\rho$ & hapax $\\rho$ & TTR $\\rho$ \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.557$ & $-0.740$ & $-0.629$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.471$ & $-0.828$ & $-0.666$ \\\\\nRewriting & 0.737 & 0.734 & 0.939 & $-0.477$ & $-0.800$ & $-0.659$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContinuation chains yield the strongest within-type signal (CV F1 = 0.781), while elaboration and rewriting show higher depth retention but weaker depth discrimination ($\\Delta = 5.1$ pp). Cross-prompt-type transfer (LOPTO) averages 0.753, indicating partial but imperfect generalization.\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{app:para}\n\nTable~\\ref{tab:para} compares paraphrastic and non-paraphrastic (continuation) chains.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paraphrastic vs.\\ non-paraphrastic chain comparison (Pythia-2.8B).}\n\\label{tab:para}\n\\begin{tabular}{lccccc}\n\\toprule\nChain Type & CV F1 & Binary F1 & Depth Ret. & ent\\_mean $\\rho$ & Eff.\\ Classes \\\\\n\\midrule\nContinuation & 0.781 & 0.694 & 0.831 & $-0.557$ & 3 \\\\\nParaphrastic & 0.718 & 0.661 & 0.992 & $-0.390$ & ${\\sim}2$ \\\\\n\\midrule\n$\\Delta$ & $+6.3$ pp & $+3.3$ pp & --- & --- & $+1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nParaphrastic chains exhibit attractor convergence (depth retention 0.992), reducing effective depth classes to ${\\sim}2$. The binary F1 gap ($\\Delta = 3.3$ pp) is moderate, suggesting the depth signal is a generic property of recursive generation rather than unique to non-paraphrastic chains, though non-paraphrastic chains sustain an additional class of depth resolution.\n\n\\section{Multi-Domain Evaluation}\n\\label{app:domain}\n\nTable~\\ref{tab:domain} reports per-domain binary F1 under LOGO evaluation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-domain binary F1 (LOGO across generators).}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & Seeds & Binary F1 & 95\\% CI & $\\Delta$ vs Wiki \\\\\n\\midrule\nWikipedia & 500 & 0.815 & [0.796, 0.834] & --- \\\\\nNews & 500 & 0.712 & [0.690, 0.733] & $-10.3$ pp \\\\\nCode & 500 & 0.687 & [0.664, 0.710] & $-12.8$ pp \\\\\nAcademic & 500 & 0.628 & [0.603, 0.652] & $-18.7$ pp \\\\\n\\midrule\nCross-domain LOGO & 2000 & 0.668 & [0.654, 0.682] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPerformance is strongly domain-dependent: Wikipedia (primary training domain) achieves 0.815, while academic text---the domain where LLM contamination is most frequently cited---yields only 0.628 ($\\Delta = -18.7$ pp). Cross-domain LOGO drops to 0.668.\n\n\\section{Robustness to Human Edits}\n\\label{app:edits}\n\nTable~\\ref{tab:edits} evaluates robustness under simulated human editing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Robustness to simulated human edits.}\n\\label{tab:edits}\n\\begin{tabular}{lccc}\n\\toprule\nPerturbation & Binary F1 & $\\Delta$ vs Baseline & Edit Distance \\\\\n\\midrule\nNone (baseline) & 0.695 & --- & 0.0 \\\\\nRandom 5\\% & 0.650 & $-4.5$ pp & ${\\sim}0.05$ \\\\\nRandom 10\\% & 0.614 & $-8.1$ pp & ${\\sim}0.10$ \\\\\nRandom 20\\% & 0.591 & $-10.4$ pp & ${\\sim}0.20$ \\\\\nLLM rephrase & 0.647 & $-4.5$ pp & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLight editing (5\\% random replacement or LLM rephrasing) reduces binary F1 by 4.5 pp. Degradation is approximately linear with perturbation intensity, suggesting the depth signal resides in surface-level distributional properties susceptible to text modification.\n\n\\section{LD-Score Feature Extension}\n\\label{app:ld}\n\nTable~\\ref{tab:ld} evaluates the addition of LD-Score (character-distribution signature) as an 8th feature.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LD-Score feature addition (3-class LOGO).}\n\\label{tab:ld}\n\\begin{tabular}{lcc}\n\\toprule\nFeature Set & LOGO F1 & $\\Delta$ \\\\\n\\midrule\n7 features (baseline) & 0.798 & --- \\\\\n7 + LD-Score & 0.802 & $+0.4$ pp \\\\\nLD-Score only & 0.721 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLD-Score alone achieves 3-class F1 = 0.721, but its marginal contribution when added to the 7-feature set is negligible (0.4 pp), indicating substantial information overlap with existing features.\n\n\\section{End-to-End QLoRA Classifier}\n\\label{app:qlora}\n\nTable~\\ref{tab:qlora} compares the 7-feature ensemble with end-to-end QLoRA fine-tuned classifiers.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{End-to-end (QLoRA) vs.\\ 7-feature ensemble.}\n\\label{tab:qlora}\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Model & 3-class F1 & Binary F1 & Cost \\\\\n\\midrule\n7-feature XGBoost & --- & 0.762 & 0.694 & $1\\times$ \\\\\nQLoRA & OLMo-Instruct & 0.888 $\\pm$ 0.007 & 0.836 $\\pm$ 0.010 & $47\\times$ \\\\\nQLoRA & Qwen-Instruct & 0.907 $\\pm$ 0.008 & 0.867 $\\pm$ 0.014 & $47\\times$ \\\\\nQLoRA & OLMo-Base & 0.859 $\\pm$ 0.004 & 0.793 $\\pm$ 0.010 & $47\\times$ \\\\\nQLoRA & Qwen-Base & 0.904 $\\pm$ 0.009 & 0.860 $\\pm$ 0.012 & $47\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQLoRA classifiers substantially outperform the 7-feature ensemble ($+12.6$ to $+17.3$ pp binary F1), indicating the text contains substantially more depth signal than the 7-feature set captures. The 7-feature ensemble trades absolute performance for $47\\times$ lower inference cost. Notably, instruct-model QLoRA classifiers achieve the highest F1, suggesting that instruction tuning degrades the specific features selected rather than the depth signal itself.\n\n\\section{Text Length Control}\n\\label{app:length}\n\nTable~\\ref{tab:length} controls for text length as a potential confound.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Length control analysis.}\n\\label{tab:length}\n\\begin{tabular}{lcc}\n\\toprule\nCondition & Binary F1 & $\\Delta$ vs Unmatched \\\\\n\\midrule\nUnmatched (original) & 0.770 & --- \\\\\nLength-normalized features & 0.748 & $-2.2$ pp \\\\\nLength-matched subsample & 0.724 & $-4.6$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLength-depth correlation is weak ($\\rho = 0.12$, $p = 0.001$). Length-matched subsampling reduces binary F1 by 4.6 pp (0.770 $\\to$ 0.724), indicating that approximately 6\\% of the signal is attributable to text length. Feature depth trends (TTR, hapax ratio) are preserved after length normalization, confirming that the core DDR pattern is not a length artifact.\n\n%% ============================================================\n%% REFERENCES (placeholder)\n%% ============================================================\n\\begin{thebibliography}{20}\n\\bibitem[1]{mitchell2023detectgpt} E.~Mitchell et al. DetectGPT: Zero-shot machine-generated text detection using probability curvature. In \\emph{ICML}, 2023.\n\\bibitem[2]{bao2024fast} G.~Bao et al. Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature. In \\emph{ICLR}, 2024.\n\\bibitem[3]{hans2024binoculars} A.~Hans et al. Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text. In \\emph{ICML}, 2024.\n\\bibitem[4]{gehrmann2019gltr} S.~Gehrmann et al. GLTR: Statistical detection and visualization of generated text. In \\emph{ACL}, 2019.\n\\bibitem[5]{shumailov2024curse} I.~Shumailov et al. AI models collapse when trained on recursively generated data. \\emph{Nature}, 2024.\n\\bibitem[6]{dohmatob2024tale} E.~Dohmatob et al. A tale of tails: Model collapse as a change of scaling laws. In \\emph{ICML}, 2024.\n\\bibitem[7]{briesch2025broken} M.~Briesch et al. LLM as broken telephone: Iterative paraphrasing converges to attractor cycles. In \\emph{ACL}, 2025.\n\\bibitem[8]{penedo2024fineweb} G.~Penedo et al. The FineWeb datasets: Decanting the web for the finest text data at scale. \\emph{NeurIPS Datasets and Benchmarks}, 2024.\n\\bibitem[9]{wettig2024qurating} A.~Wettig et al. QuRating: Selecting high-quality data for training language models. In \\emph{ICML}, 2024.\n\\bibitem[10]{tulchinskii2024ld} E.~Tulchinskii et al. Intrinsic dimension estimation for robust detection of AI-generated texts. In \\emph{NeurIPS}, 2024.\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d2f0c22c-5a99-4f7b-8eb2-2280ab1751ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "110381ec-1cda-4f63-ace8-d25dd4c03978",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate reframed paper on depth decoding dynamics",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Tool call

_source line 26 · 2026-05-21T22:16:11.528Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KuPTgToU1E1e2nBDp5ecrg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "110381ec-1cda-4f63-ace8-d25dd4c03978",
  "isSidechain": false,
  "requestId": "req_011CbGVBptQUuaBqSW9qLFwg",
  "type": "assistant",
  "uuid": "230f716e-3b4f-476f-a831-81aafccc6154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBmPZkkZp7wsj3zDkPJDYh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11002,
      "cache_read_input_tokens": 52367,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 52367,
          "cache_creation_input_tokens": 11002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11002
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

_source line 27 · 2026-05-21T22:16:12.416Z_

<details><summary>↩ Tool result · `toolu_01KuPTgToU1E1e2nBDp5ecrg`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
Overfull \hbox (0.64563pt too wide) in paragraph at lines 25--26
[]\OT1/cmr/m/n/10 Web-scraped train-ing cor-pora in-creas-ingly con-tain LLM-ge
nerated text of un-known prove-

Overfull \hbox (2.28447pt too wide) in paragraph at lines 25--26
\OT1/cmr/m/n/10 nance depth---text that has been re-cur-sively gen-er-ated thro
ugh mul-ti-ple au-tore-gres-sive passes.
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 51.


Package natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin
e 51.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 51.


Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 51.


Overfull \hbox (9.45256pt too wide) in paragraph at lines 51--52
 []\OT1/cmr/bx/n/10.95 AI text de-tec-tion.[] \OT1/cmr/m/n/10.95 Perplexity-bas
ed de-tec-tors lever-age sta-tis-ti-cal prop-er-ties of model-generated
[2]

LaTeX Warning: Reference `tab:feature_trend' on page 3 undefined on input line 
104.

[3]

LaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 128.


LaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 151.


LaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 178.


LaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 202.


LaTeX Warning: Reference `tab:cross_model' on page 4 undefined on input line 22
7.

[4]

LaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 250
.


LaTeX Warning: Reference `tab:ordinal' on page 5 undefined on input line 281.

[5]

LaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 304.


LaTeX Warning: Reference `tab:ref_model' on page 6 undefined on input line 329.


[6]

LaTeX Warning: Reference `tab:prompt_type' on page 7 undefined on input line 36
8.


Overfull \hbox (2.98344pt too wide) in paragraph at lines 368--369
\OT1/cmr/m/n/10.95 Table [] com-pares three prompt types: con-tin-u-a-tion, ela
b-o-ra-tion, and in-spired rewrit-ing (Pythia-

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:para' on page 7 undefined on input line 391.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 415.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: Reference `tab:edits' on page 8 undefined on input line 441.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:ld' on page 8 undefined on input line 466.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:qlora' on page 8 undefined on input line 489.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:length' on page 8 undefined on input line 514.


LaTeX Warning: `h' float specifier changed to `ht'.

[8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (10 pages, 188250 bytes).
Transcript written on paper.log.
LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (10 pages, 190950 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "230f716e-3b4f-476f-a831-81aafccc6154",
  "isSidechain": false,
  "promptId": "e5784085-d6bf-4a40-94e5-76d22c2a2d2e",
  "type": "user",
  "uuid": "3039bd84-052e-42df-b04d-a3e8b2a16306",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\nOverfull \\hbox (0.64563pt too wide) in paragraph at lines 25--26\n[]\\OT1/cmr/m/n/10 Web-scraped train-ing cor-pora in-creas-ingly con-tain LLM-ge\nnerated text of un-known prove-\n\nOverfull \\hbox (2.28447pt too wide) in paragraph at lines 25--26\n\\OT1/cmr/m/n/10 nance depth---text that has been re-cur-sively gen-er-ated thro\nugh mul-ti-ple au-tore-gres-sive passes.\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 51.\n\n\nPackage natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin\ne 51.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 51.\n\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 51.\n\n\nOverfull \\hbox (9.45256pt too wide) in paragraph at lines 51--52\n []\\OT1/cmr/bx/n/10.95 AI text de-tec-tion.[] \\OT1/cmr/m/n/10.95 Perplexity-bas\ned de-tec-tors lever-age sta-tis-ti-cal prop-er-ties of model-generated\n[2]\n\nLaTeX Warning: Reference `tab:feature_trend' on page 3 undefined on input line \n104.\n\n[3]\n\nLaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 128.\n\n\nLaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 151.\n\n\nLaTeX Warning: Reference `tab:lofo' on page 4 undefined on input line 178.\n\n\nLaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 202.\n\n\nLaTeX Warning: Reference `tab:cross_model' on page 4 undefined on input line 22\n7.\n\n[4]\n\nLaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 250\n.\n\n\nLaTeX Warning: Reference `tab:ordinal' on page 5 undefined on input line 281.\n\n[5]\n\nLaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 304.\n\n\nLaTeX Warning: Reference `tab:ref_model' on page 6 undefined on input line 329.\n\n\n[6]\n\nLaTeX Warning: Reference `tab:prompt_type' on page 7 undefined on input line 36\n8.\n\n\nOverfull \\hbox (2.98344pt too wide) in paragraph at lines 368--369\n\\OT1/cmr/m/n/10.95 Table [] com-pares three prompt types: con-tin-u-a-tion, ela\nb-o-ra-tion, and in-spired rewrit-ing (Pythia-\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:para' on page 7 undefined on input line 391.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 415.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: Reference `tab:edits' on page 8 undefined on input line 441.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:ld' on page 8 undefined on input line 466.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:qlora' on page 8 undefined on input line 489.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:length' on page 8 undefined on input line 514.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (10 pages, 188250 bytes).\nTranscript written on paper.log.\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (10 pages, 190950 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "230f716e-3b4f-476f-a831-81aafccc6154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T22:16:21.105Z_

编译成功，10 页 PDF（主体 ~7 页 + 附录 ~3 页），所有交叉引用已解析。

论文覆盖了 `experiment_data.json` 中全部 15 个实验：主体包含 feature ablation/trend、cross-generator LOGO、baseline comparison、cross-model chains、downstream utility、ordinal resolution、scale effects、reference model independence；附录包含 prompt type、paraphrastic comparison、multi-domain、human edit robustness、LD-Score、QLoRA end-to-end、length control。所有数字均直接取自实验数据，无编造。

输出位置：`artifacts/dream_reports/dream_20260521T213023/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3039bd84-052e-42df-b04d-a3e8b2a16306",
  "isSidechain": false,
  "requestId": "req_011CbGVCCoXBRZ2ry8zavDF5",
  "type": "assistant",
  "uuid": "21e0d206-fd4a-4e2a-867e-6d1310766659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/worst",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfLaPb2ZmUjkzNbMtYc8Ss",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 63369,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 63369,
          "cache_creation_input_tokens": 4150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4150
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerp…",
  "leafUuid": "21e0d206-fd4a-4e2a-867e-6d1310766659",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate reframed paper on depth decoding dynamics",
  "sessionId": "c4321cb1-84b0-4cbf-9932-aa6cf3807d7b"
}
```

---
