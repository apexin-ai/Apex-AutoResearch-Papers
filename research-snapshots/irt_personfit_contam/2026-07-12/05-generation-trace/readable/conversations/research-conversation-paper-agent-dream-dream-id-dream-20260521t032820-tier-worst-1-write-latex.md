# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/f36dd737-9d19-4972-ba6a-9a0d91a2e1e2.jsonl`
- **Structured JSON:** [`b1d326001fa36d0fac3e.json`](../../sessions/b1/b1d326001fa36d0fac3e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:59:58.488Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:59:58.488Z",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心 detection claim 不成立。ctrl-contam 仅在 Qwen+Llama（已验证家族）上有效， Gemma/Mistral 泛化失败（SFT generalization 过强或 4PL 参数不适配）。 非 MMLU benchmark 检测能力严重不足。Post-RL 检测完全失败。 lz* 作为 binary-only method 在 baseline 对比中显著落后于 privileged methods。 论文必须 reframe 为 characterization/impossibility paper，放弃 general detection claim。 已有 simulation + universal misfit + θ-shift + 4PL ablation + seen/unseen split 仍为 solid contributions。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T03:59:58.493Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:59:58.493Z",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-21T03:59:58.517Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心 detection claim 不成立。ctrl-contam 仅在 Qwen+Llama（已验证家族）上有效， Gemma/Mistral 泛化失败（SFT generalization 过强或 4PL 参数不适配）。 非 MMLU benchmark 检测能力严重不足。Post-RL 检测完全失败。 lz* 作为 binary-only method 在 baseline 对比中显著落后于 privileged methods。 论文必须 reframe 为 characterization/impossibility paper，放弃 general detection claim。 已有 simulation + universal misfit + θ-shift + 4PL ablation + seen/unseen split 仍为 solid contributions。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "7f7cb1c7-6b64-437e-a020-6a54addc9482",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:59:58.516Z_

```json
{
  "parentUuid": "7f7cb1c7-6b64-437e-a020-6a54addc9482",
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
  "uuid": "4bdeb62a-7c9b-4593-b56f-6946af73f3d2",
  "timestamp": "2026-05-21T03:59:58.516Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:59:58.516Z_

```json
{
  "parentUuid": "4bdeb62a-7c9b-4593-b56f-6946af73f3d2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3437c8f2-23a4-41e4-934d-9f37909e2b2b",
  "timestamp": "2026-05-21T03:59:58.516Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
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
  "aiTitle": "Generate worst-case paper on IRT contamination detection",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Assistant

_source line 7 · 2026-05-21T04:00:03.319Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3437c8f2-23a4-41e4-934d-9f37909e2b2b",
  "isSidechain": false,
  "requestId": "req_011CbF3bjGxBwJycQxQL14jy",
  "type": "assistant",
  "uuid": "4322f328-b0e7-46d2-bd7e-cb6afaed444d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k37oJmPHLugqaybnYtKJA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11743,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11743
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

_source line 8 · 2026-05-21T04:00:03.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XSEGCwnLRBNFYBAHrQheCB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4322f328-b0e7-46d2-bd7e-cb6afaed444d",
  "isSidechain": false,
  "requestId": "req_011CbF3bjGxBwJycQxQL14jy",
  "type": "assistant",
  "uuid": "3a82be2e-1dec-4630-a106-32ebe57d41bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k37oJmPHLugqaybnYtKJA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11743,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11743
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

_source line 9 · 2026-05-21T04:00:04.031Z_

<details><summary>↩ Tool result · `toolu_01XSEGCwnLRBNFYBAHrQheCB`</summary>

```text
1	[
2	  {
3	    "name": "exp-ctrl-contam-pilot",
4	    "description": "Qwen3.5-9B × 4 conditions (0%×2/15%/50%) × MMLU only，go/no-go 信号",
5	    "results": {
6	      "clean_s1_lz_star": 6.2,
7	      "clean_s2_lz_star": 5.8,
8	      "clean_mean_lz_star": 6.0,
9	      "clean_std_lz_star": 0.28,
10	      "contam_15_lz_star": 4.1,
11	      "contam_50_lz_star": 5.5,
12	      "contam_15_delta_lz_star": -1.9,
13	      "contam_50_delta_lz_star": -0.5,
14	      "cohens_d_contam_15_ddof1": -1.8,
15	      "cohens_d_contam_50_ddof1": -0.5,
16	      "memorization_fraction_15pct": 0.22,
17	      "memorization_fraction_50pct": 0.18,
18	      "theta_shift_15pct": 0.21,
19	      "theta_shift_50pct": 0.39,
20	      "theta_fixed_restores_monotonicity": true,
21	      "theta_fixed_ratio": 2.1
22	    },
23	    "tables": [
24	      {
25	        "caption": "Pilot: Qwen3.5-9B × MMLU Δlz* summary",
26	        "columns": [
27	          "condition",
28	          "lz_star",
29	          "delta_lz_star",
30	          "cohens_d",
31	          "acc",
32	          "theta",
33	          "memo_frac"
34	        ],
35	        "rows": [
36	          [
37	            "clean_s1",
38	            6.2,
39	            0,
40	            "-",
41	            0.672,
42	            -0.12,
43	            "-"
44	          ],
45	          [
46	            "clean_s2",
47	            5.8,
48	            0,
49	            "-",
50	            0.668,
51	            -0.14,
52	            "-"
53	          ],
54	          [
55	            "contam_15",
56	            4.1,
57	            -1.9,
58	            -1.8,
59	            0.718,
60	            0.09,
61	            0.22
62	          ],
63	          [
64	            "contam_50",
65	            5.5,
66	            -0.5,
67	            -0.5,
68	            0.751,
69	            0.27,
70	            0.18
71	          ]
72	        ]
73	      }
74	    ],
75	    "figures": [],
76	    "analysis": "Go 信号成立但弱于 best/expected。Qwen 在 15% 可检测，50% 因 θ-shift 信号衰减。 memorization fraction 低意味着 power function 的 upper bound 与 adjusted power 差距大。 需要 cross-family 验证，但预期 Gemma/Mistral 会失败。\n\n\nWorst 档下 Qwen 仍检测成功（已验证家族），但效应量比实际偏弱。 contam_15 |d|≈1.8 仍然 significant（Qwen 是最强信号家族之一）， 但 contam_50 出现非单调（free-θ 下 |d|=0.5），θ-shift 吃掉大部分信号。 memorization fraction 偏低（22%），说明 SFT generalization 比预期更强—— 模型不是死记硬背而是\"学会了\"，导致 seen/unseen accuracy gap 缩小。 这是 worst 档的核心机制：SFT generalization 过强，lz* 检测的 memorization 信号被稀释。 θ-fixed 仍能恢复单调性，因为 θ-shift 是可修正的 confound，但绝对效应量仍低。 Go/no-go 判定：go（但仅限 Qwen），需要 cross-family 验证。\n"
77	  },
78	  {
79	    "name": "exp-ctrl-contam (full)",
80	    "description": "4 模型 × 6 levels × 3 benchmarks 完整控制实验",
81	    "results": {
82	      "qwen_mmlu_d_15pct": -2.8,
83	      "llama_mmlu_d_15pct": -2.2,
84	      "gemma_mmlu_d_15pct": -0.7,
85	      "mistral_mmlu_d_15pct": -0.4,
86	      "d_15pct_min_across_families": 0.4,
87	      "d_15pct_mean_across_families": 1.5,
88	      "n_families_d_gt_2": 2,
89	      "hellaswag_d_15pct_mean": 0.5,
90	      "gsm8k_d_15pct_mean": 0.3,
91	      "gemma_memorization_fraction_15pct": 0.15,
92	      "mistral_memorization_fraction_15pct": 0.17,
93	      "qwen_memorization_fraction_15pct": 0.35,
94	      "llama_memorization_fraction_15pct": 0.32,
95	      "theta_fixed_monotonic_families": 2,
96	      "theta_fixed_fails_gemma": true,
97	      "theta_fixed_fails_mistral": true,
98	      "dose_response_monotonic_free_theta": 1,
99	      "dose_response_monotonic_fixed_theta": 2,
100	      "hellaswag_any_family_d_gt_2": false,
101	      "gsm8k_any_family_d_gt_2": false,
102	      "gsm8k_best_family_d": 0.8,
103	      "hellaswag_best_family_d": 1.2
104	    },
105	    "tables": [
106	      {
107	        "caption": "Table 1: Cohen's d at 15% contamination by family × benchmark",
108	        "columns": [
109	          "family",
110	          "mmlu_d",
111	          "hellaswag_d",
112	          "gsm8k_d",
113	          "mean_d"
114	        ],
115	        "rows": [
116	          [
117	            "Qwen2.5-7B",
118	            -2.8,
119	            -1.0,
120	            -0.6,
121	            -1.47
122	          ],
123	          [
124	            "Llama-3.1-8B",
125	            -2.2,
126	            -0.8,
127	            -0.5,
128	            -1.17
129	          ],
130	          [
131	            "Gemma-4-12B",
132	            -0.7,
133	            -0.3,
134	            -0.1,
135	            -0.37
136	          ],
137	          [
138	            "Mistral-7B-v0.3",
139	            -0.4,
140	            -0.2,
141	            -0.1,
142	            -0.23
143	          ]
144	        ]
145	      },
146	      {
147	        "caption": "Table 2: Memorization fraction by family (15% contamination)",
148	        "columns": [
149	          "family",
150	          "mmlu",
151	          "hellaswag",
152	          "gsm8k",
153	          "mean"
154	        ],
155	        "rows": [
156	          [
157	            "Qwen2.5-7B",
158	            0.35,
159	            0.28,
160	            0.2,
161	            0.28
162	          ],
163	          [
164	            "Llama-3.1-8B",
165	            0.32,
166	            0.25,
167	            0.18,
168	            0.25
169	          ],
170	          [
171	            "Gemma-4-12B",
172	            0.15,
173	            0.12,
174	            0.08,
175	            0.12
176	          ],
177	          [
178	            "Mistral-7B-v0.3",
179	            0.17,
180	            0.13,
181	            0.09,
182	            0.13
183	          ]
184	        ]
185	      },
186	      {
187	        "caption": "Table 3: θ-fixed vs free-θ dose-response monotonicity",
188	        "columns": [
189	          "family",
190	          "free_theta_monotonic",
191	          "fixed_theta_monotonic",
192	          "theta_shift_at_50pct"
193	        ],
194	        "rows": [
195	          [
196	            "Qwen2.5-7B",
197	            false,
198	            true,
199	            0.45
200	          ],
201	          [
202	            "Llama-3.1-8B",
203	            true,
204	            true,
205	            0.48
206	          ],
207	          [
208	            "Gemma-4-12B",
209	            false,
210	            false,
211	            0.52
212	          ],
213	          [
214	            "Mistral-7B-v0.3",
215	            false,
216	            false,
217	            0.38
218	          ]
219	        ]
220	      }
221	    ],
222	    "figures": [],
223	    "analysis": "核心结论：detection 不 generalize。2/4 家族 |d|>2（Qwen+Llama），2/4 家族 |d|<1。 非 MMLU benchmark 全面弱化。不能 claim \"IRT person-fit detects contamination\"， 只能 claim \"IRT person-fit detects contamination under specific conditions (sufficient n_items, sufficient memorization fraction, specific model architectures)\"。 必须 reframe。memorization fraction 的极端分化（15-38%）是关键发现—— 这说明 SFT generalization 是 model-specific 的，binary-only detection 的天花板由此决定。\n\n\nWorst 档核心假设：ctrl-contam 仅在已验证的 Qwen+Llama 有效。\nQwen/Llama 成功原因：这两个家族在 SFT 时 memorization fraction 较高（32-38%）， 产生足够的 aberrant pattern 让 lz* 捕捉。Qwen baseline misfit 高（lz*≈8.7）， Llama baseline 低（lz*≈-0.14），但两者都在 MMLU 上产生 |d|>2。\nGemma 失败原因：Gemma 家族的 SFT generalization 特别强。SFT 后模型不仅记住 seen items， 还大幅提升 unseen items 的正确率，memorization fraction 降至 15%。 这意味着 contaminated response pattern 与 \"genuinely improved\" pattern 几乎不可区分。 另外 Gemma 的 4PL 参数适配可能不佳——PSN-IRT 的参数是在不同模型群体上估计的， Gemma 架构的 response pattern 可能需要不同的 item parameters。 |d|=0.7 在统计上可能 barely significant（p≈0.05 with n=3），但不足以支撑 detection claim。\nMistral 失败原因：Mistral-7B-v0.3 是相对较弱的模型，baseline accuracy 低。 SFT 后 θ 提升幅度大但 pattern 变化方式更像 \"legitimate learning\"。 4PL 参数对低能力模型的 discrimination 不足（a 参数区域覆盖差）， 导致 lz* 对 contamination-induced pattern change 不敏感。|d|=0.4，不显著。\n非 MMLU benchmark 失败原因：n_items 不足。HellaSwag (10K) 勉强可用但 4PL 参数估计质量下降， GSM8K (1.3K) 太小导致 lz* 方差大、信噪比低。power function 预测 GSM8K@15% 理论 power≈59%， 但 SFT generalization 折扣后 adjusted power≈20-30%。\nθ-fixed 仅在 Qwen+Llama 恢复信号：因为这两个家族的 θ-shift 是主要 confound， fix θ 后信号恢复。Gemma/Mistral 的问题不是 θ-shift 而是 memorization fraction 本身太低， θ-fixed 无法修复根本问题。\n"
224	  },
225	  {
226	    "name": "exp-leaderboard-audit",
227	    "description": "Open LLM Leaderboard v1 大规模扫描（已 ABANDONED）",
228	    "results": {
229	      "status": "ABANDONED — not executed",
230	      "reason": "D011 v1-irt-refit a_r=0.111, item alignment 54.56%",
231	      "hypothetical_if_forced": {
232	        "n_models_scanned": 500,
233	        "flagged_rate_mmlu": 0.92,
234	        "flagged_rate_overall": 0.88,
235	        "false_positive_rate_estimated": ">80%",
236	        "meaningful_contamination_signal": false
237	      }
238	    },
239	    "tables": [],
240	    "figures": [],
241	    "analysis": "Abandon 决策正确。v1 数据可用性写入 Discussion/Future Work， 强调 \"13K+ per-item data publicly available, awaiting better IRT estimation methods\"。\n\n\n已 abandoned 因 a_r=0.111（discrimination 完全失败）和 item alignment 仅 54.56%。 即使强行执行，v1 refit 的 IRT 参数质量太差，lz* 退化为 accuracy-like statistic， flagging 率与 accuracy z-score 高度相关，无法区分 contamination 与 ability。 在 worst 档下这个实验根本不应该做，正确的决定是 abandon。\n"
242	  },
243	  {
244	    "name": "exp-natural-experiment",
245	    "description": "v1 leaderboard base→chat model pairs 自然实验",
246	    "results": {
247	      "n_pairs": 4,
248	      "n_complete_pairs": 3,
249	      "significant_benchmarks": 0,
250	      "mmlu_p": 0.45,
251	      "hellaswag_p": 0.28,
252	      "gsm8k_p": 0.31,
253	      "arc_c_p": 0.62,
254	      "individual_outliers": 0,
255	      "effect_interpretable": false
256	    },
257	    "tables": [
258	      {
259	        "caption": "Base→Chat Δlz* paired t-tests (v1 IRT parameters)",
260	        "columns": [
261	          "benchmark",
262	          "mean_delta_lz",
263	          "t_stat",
264	          "p_value",
265	          "n_pairs"
266	        ],
267	        "rows": [
268	          [
269	            "MMLU",
270	            1.2,
271	            0.85,
272	            0.45,
273	            4
274	          ],
275	          [
276	            "HellaSwag",
277	            -2.1,
278	            -1.3,
279	            0.28,
280	            4
281	          ],
282	          [
283	            "GSM8K",
284	            1.8,
285	            1.15,
286	            0.31,
287	            4
288	          ],
289	          [
290	            "ARC-C",
291	            -0.5,
292	            -0.52,
293	            0.62,
294	            4
295	          ]
296	        ]
297	      }
298	    ],
299	    "figures": [],
300	    "analysis": "统计检验能力不足 + IRT 参数质量差 = 无法得出任何结论。 P2-optional 优先级正确。在 worst 档叙事中仅作为 \"attempted but inconclusive\" 提及。\n\n\nWorst 档下 a_r=0.111 导致 lz* 退化。仅 4-5 pairs 没有统计检验能力（power<0.2 for d=0.5）。 Base→chat 的 SFT 效应被 IRT 参数质量低掩盖。即使有 systematic shift， n_pairs 太少无法达到 significance。此外，base→chat 的 SFT 是 general instruction tuning， 不是 benchmark-specific contamination，所以即使检测到 Δlz*，也无法归因为 contamination。 Worst 档下这个实验提供 zero additional evidence。\n"
301	  },
302	  {
303	    "name": "exp-v1-irt-refit-expanded",
304	    "description": "扩大 v1 IRT 重拟合样本量至 N≥500，最终关闭 Path D",
305	    "results": {
306	      "n_models_downloaded": 520,
307	      "n_models_usable": 410,
308	      "a_pearson_r_3pl": 0.13,
309	      "a_pearson_r_2pl": -0.02,
310	      "b_pearson_r_3pl": 0.68,
311	      "b_spearman_r_3pl": 0.7,
312	      "path_d_verdict": "DEAD",
313	      "discrimination_above_threshold": false
314	    },
315	    "tables": [
316	      {
317	        "caption": "IRT refit: parameter recovery by sample size",
318	        "columns": [
319	          "N",
320	          "a_r_3pl",
321	          "a_r_2pl",
322	          "b_r_3pl",
323	          "verdict"
324	        ],
325	        "rows": [
326	          [
327	            63,
328	            0.111,
329	            -0.084,
330	            0.626,
331	            "dead"
332	          ],
333	          [
334	            178,
335	            0.127,
336	            -0.029,
337	            0.663,
338	            "dead"
339	          ],
340	          [
341	            520,
342	            0.13,
343	            -0.02,
344	            0.68,
345	            "dead"
346	          ]
347	        ]
348	      }
349	    ],
350	    "figures": [],
351	    "analysis": "Path D 最终关闭。Classical IRT estimation 无法恢复 PSN-IRT 的 neural-estimated discrimination。 这本身是 methodological contribution（Claim 3c）：quantify classical vs neural IRT gap。 在 worst 档叙事中作为 \"impossibility result\" 贡献。\n\n\nN=63→178 时 a_r 仅从 0.111 提升到 0.127。Worst 档下 N=500+ 带来的边际改善极小（a_r≈0.13）， 远低于 0.2 threshold，更不可能达到 0.4 可行线。\n根本原因不是样本量而是 classical IRT (MML-EM) 与 neural IRT 的 estimation paradigm gap： (1) classical IRT 假设 unidimensional latent trait，但 LLM 能力是高维的； (2) LLM response patterns violate local independence（同 domain items 高度相关）； (3) v1 leaderboard 模型异质性太高（从 1B 到 70B，架构各异）， 单一 θ dimension 无法 capture 这种异质性。 b 参数（difficulty）较好恢复是因为 item difficulty 是 population-level statistic， 对 latent structure 假设不敏感；a 参数（discrimination）需要精确的 latent structure。\n"
352	  },
353	  {
354	    "name": "exp-4pl-ablation",
355	    "description": "4PL vs 3PL(d=1) ablation in simulation",
356	    "results": {
357	      "far_4pl": 0.05,
358	      "far_3pl": 0.12,
359	      "far_2pl": 0.65,
360	      "mean_power_gain_4pl_vs_3pl_mmlu": 0.18,
361	      "mean_power_gain_4pl_vs_3pl_hellaswag": 0.15,
362	      "mean_power_gain_4pl_vs_3pl_gsm8k": 0.12,
363	      "ctrl_contam_4pl_vs_3pl_delta_d": 0.8,
364	      "ctrl_contam_3pl_d_15pct_qwen": -1.5,
365	      "ctrl_contam_4pl_d_15pct_qwen": -2.8
366	    },
367	    "tables": [
368	      {
369	        "caption": "4PL vs 3PL detection power comparison",
370	        "columns": [
371	          "benchmark",
372	          "power_4pl_15pct",
373	          "power_3pl_15pct",
374	          "gain_pp"
375	        ],
376	        "rows": [
377	          [
378	            "MMLU",
379	            0.98,
380	            0.8,
381	            18
382	          ],
383	          [
384	            "HellaSwag",
385	            0.75,
386	            0.6,
387	            15
388	          ],
389	          [
390	            "GSM8K",
391	            0.59,
392	            0.47,
393	            12
394	          ],
395	          [
396	            "ARC-C",
397	            0.13,
398	            0.09,
399	            4
400	          ],
401	          [
402	            "HumanEval",
403	            0.24,
404	            0.18,
405	            6
406	          ]
407	        ]
408	      }
409	    ],
410	    "figures": [],
411	    "analysis": "Simulation-level ablation 仍成立。4PL 是必要的 model specification。 但这仅是 necessary condition，不是 sufficient condition for detection。 在 worst 档叙事中，4PL ablation 作为 methodological contribution 保留， 但不能作为 \"detection works\" 的证据。\n\n\n4PL ablation 在 simulation 层面是 robust 的（这是 model specification 问题，不受 generalization 影响）。 即使在 worst 档，4PL 仍优于 3PL/2PL，因为 LLM high-ability models 确实需要 d parameter。 但 worst 档的差异在于：ctrl-contam 验证时 4PL 优势在 failing families（Gemma/Mistral） 上体现不出来——因为两者都失败了。优势仅在 Qwen/Llama 上体现， 使得 \"4PL essential\" 的 claim 变成 \"4PL essential for the families where detection works at all\"。 Power gain 数值低于 best 档因为 worst 档假设部分 4PL 参数（特别是 d 值接近 1 的 items） 对 detection 贡献有限。\n"
412	  },
413	  {
414	    "name": "exp-baseline-comparison",
415	    "description": "与 ≥5 baselines 对比 AUROC/Type-I error",
416	    "results": {
417	      "auroc_lz_star_15pct": 0.62,
418	      "auroc_mink_pp_15pct": 0.82,
419	      "auroc_ppl_15pct": 0.78,
420	      "auroc_constat_15pct": 0.85,
421	      "auroc_acc_zscore_15pct": 0.55,
422	      "auroc_random_15pct": 0.5,
423	      "auroc_lz_star_5pct": 0.58,
424	      "auroc_mink_pp_5pct": 0.72,
425	      "auroc_ppl_5pct": 0.68,
426	      "auroc_constat_5pct": 0.75,
427	      "auroc_acc_zscore_5pct": 0.52,
428	      "auroc_gap_15pct_vs_best": -0.23,
429	      "auroc_gap_5pct_vs_best": -0.17,
430	      "type_i_lz_star": 0.06,
431	      "type_i_mink_pp": 0.04,
432	      "type_i_constat": 0.05,
433	      "ci_lz_star_15pct": [
434	        0.54,
435	        0.7
436	      ],
437	      "ci_mink_pp_15pct": [
438	        0.76,
439	        0.88
440	      ],
441	      "auroc_lz_star_post_rl": 0.53,
442	      "auroc_mink_pp_post_rl": 0.51,
443	      "auroc_ppl_post_rl": 0.52
444	    },
445	    "tables": [
446	      {
447	        "caption": "Table: AUROC comparison at 15% contamination (bootstrap 95% CI)",
448	        "columns": [
449	          "method",
450	          "info_level",
451	          "auroc_mean",
452	          "ci_lower",
453	          "ci_upper",
454	          "type_i"
455	        ],
456	        "rows": [
457	          [
458	            "ConStat",
459	            "rephrased-retest",
460	            0.85,
461	            0.79,
462	            0.91,
463	            0.05
464	          ],
465	          [
466	            "MinK%++",
467	            "token-probs",
468	            0.82,
469	            0.76,
470	            0.88,
471	            0.04
472	          ],
473	          [
474	            "PPL-based",
475	            "log-probs",
476	            0.78,
477	            0.71,
478	            0.85,
479	            0.06
480	          ],
481	          [
482	            "lz* (ours)",
483	            "binary-only",
484	            0.62,
485	            0.54,
486	            0.7,
487	            0.06
488	          ],
489	          [
490	            "Acc z-score",
491	            "binary-only",
492	            0.55,
493	            0.48,
494	            0.62,
495	            0.08
496	          ],
497	          [
498	            "Random",
499	            "none",
500	            0.5,
501	            0.5,
502	            0.5,
503	            0.05
504	          ]
505	        ]
506	      },
507	      {
508	        "caption": "Table: AUROC by contamination level (lz* vs best privileged)",
509	        "columns": [
510	          "contam_pct",
511	          "auroc_lz_star",
512	          "auroc_best_privileged",
513	          "gap"
514	        ],
515	        "rows": [
516	          [
517	            3,
518	            0.54,
519	            0.62,
520	            -0.08
521	          ],
522	          [
523	            5,
524	            0.58,
525	            0.72,
526	            -0.14
527	          ],
528	          [
529	            10,
530	            0.6,
531	            0.78,
532	            -0.18
533	          ],
534	          [
535	            15,
536	            0.62,
537	            0.85,
538	            -0.23
539	          ],
540	          [
541	            25,
542	            0.68,
543	            0.91,
544	            -0.23
545	          ],
546	          [
547	            50,
548	            0.74,
549	            0.95,
550	            -0.21
551	          ]
552	        ]
553	      }
554	    ],
555	    "figures": [],
556	    "analysis": "lz* 显著弱于 privileged methods，但仍优于 random 和 accuracy z-score。 这证实了 \"minimal-information operating point\" 的代价。 在 worst 档叙事中，这个 gap 本身是 contribution： \"we precisely quantify the detection power lost by operating at the binary-only level\"。 Figure showing the detection frontier (info access vs AUROC) 是论文的 key figure。\n\n\nWorst 档核心假设：lz* 在所有区间显著落后于 MinK%++（>15% AUROC gap）。\nlz* AUROC 低的原因： (1) binary-only 信息瓶颈——lz* 只看对/错，而 MinK%++ 用 token-level probability， 信息量差异是本质性的（每个 item MinK%++ 有数百个 token prob vs lz* 有 1 bit）； (2) SFT generalization 将 memorization fraction 降至 15-38%， 真正产生 aberrant signal 的 items 比例低； (3) Gemma/Mistral 失败拖低 cross-family average AUROC。\nlz* 仅在两个极端条件下有 competitive advantage： (a) post-RL：所有 log-prob methods 失效（AUROC≈0.50-0.52），lz* 也失效但程度类似（0.53）， 差距消失但这不是 \"优势\" 而是 \"everyone fails\"； (b) 极低 contamination (3-5%)：lz* 的 IRT inductive bias 在 n=3 seeds 下 可能比需要更多 training data 的 supervised methods 稍好，但优势仅 +0.05 AUROC， 不足以 claim superiority。\nConStat 是最强 baseline（需要 re-test），因为 re-phrased questions 直接测 memorization vs understanding， 信息量远超 binary-only。\n-23% AUROC gap 在论文中必须 honestly 报告。Reframe 方向： \"we quantify the cost of operating at the minimal-information point\"。\n"
557	  },
558	  {
559	    "name": "exp-multiscale-lzm",
560	    "description": "跨 benchmark 聚合 lzm 统计量",
561	    "results": {
562	      "lzm_improves_over_per_benchmark_lz": false,
563	      "lzm_auroc_15pct": 0.6,
564	      "lzm_vs_lz_star_auroc_delta": -0.02,
565	      "cross_benchmark_correlation_low": true,
566	      "aggregation_benefit": "negligible",
567	      "psn_12_model_lzm_flagged": 10
568	    },
569	    "tables": [
570	      {
571	        "caption": "lzm vs per-benchmark lz* AUROC",
572	        "columns": [
573	          "method",
574	          "auroc_15pct",
575	          "auroc_50pct"
576	        ],
577	        "rows": [
578	          [
579	            "lz*_MMLU_only",
580	            0.62,
581	            0.74
582	          ],
583	          [
584	            "lz*_HellaSwag_only",
585	            0.55,
586	            0.62
587	          ],
588	          [
589	            "lzm_aggregated",
590	            0.6,
591	            0.7
592	          ]
593	        ]
594	      }
595	    ],
596	    "figures": [],
597	    "analysis": "lzm 不作为主要 contribution。在论文中可以用一句话提及 \"cross-benchmark aggregation did not improve detection, consistent with the low cross-benchmark correlation of lz*\"。\n\n\nWorst 档下 lzm 无法改善检测。原因： (1) 非 MMLU benchmark 的 lz* 信号太弱（|d|<0.8），聚合时引入更多 noise 而非 signal； (2) cross-benchmark lz* 相关性很低（Phase B 仅 1/10 对显著）， 说明 contamination signal 在不同 benchmark 上不 coherent，聚合不增加信息量； (3) lzm 统计量假设各 benchmark 的 lz* 独立同分布， 但实际上 benchmark-specific 的 4PL 参数质量差异大（MMLU 好，HumanEval 差）。 在 worst 档下，lzm 甚至可能因为纳入低质量 benchmark 而降低 MMLU-only 的检测力。\n"
598	  },
599	  {
600	    "name": "exp-post-rl",
601	    "description": "Post-RL 检测：SFT 污染 → GRPO 训练 → person-fit 测试",
602	    "results": {
603	      "cohens_d_pre_rl_15pct": -2.5,
604	      "cohens_d_post_rl_15pct": -0.3,
605	      "cohens_d_post_rl_50pct": -0.4,
606	      "lz_star_post_rl_contam_15": 7.8,
607	      "lz_star_post_rl_clean": 8.1,
608	      "delta_lz_post_rl": -0.3,
609	      "post_rl_detection_power": 0.08,
610	      "rl_training_steps": 2000,
611	      "rl_reward_type": "rule-based (MMLU accuracy)",
612	      "memorization_fraction_post_rl": 0.05,
613	      "theta_shift_post_rl": 0.62,
614	      "experiment_completion": true
615	    },
616	    "tables": [
617	      {
618	        "caption": "Pre-RL vs Post-RL detection",
619	        "columns": [
620	          "condition",
621	          "lz_star",
622	          "delta_lz",
623	          "cohens_d",
624	          "memo_frac",
625	          "theta"
626	        ],
627	        "rows": [
628	          [
629	            "clean",
630	            8.1,
631	            0,
632	            "-",
633	            "-",
634	            -0.1
635	          ],
636	          [
637	            "contam_15_pre_rl",
638	            4.2,
639	            -3.9,
640	            -2.5,
641	            0.35,
642	            0.12
643	          ],
644	          [
645	            "contam_15_post_rl",
646	            7.8,
647	            -0.3,
648	            -0.3,
649	            0.05,
650	            0.52
651	          ],
652	          [
653	            "contam_50_pre_rl",
654	            6.8,
655	            -1.3,
656	            -0.8,
657	            0.28,
658	            0.28
659	          ],
660	          [
661	            "contam_50_post_rl",
662	            7.5,
663	            -0.6,
664	            -0.4,
665	            0.06,
666	            0.68
667	          ]
668	        ]
669	      }
670	    ],
671	    "figures": [],
672	    "analysis": "Post-RL 检测完全失败。但这不是新发现（Wang et al. 2025 已 established）， 而是 confirms that binary-only methods share the same limitation。 在 worst 档叙事中的用法：\"post-RL failure is expected and consistent with the theoretical framework — RL converts memorization to generalization, eliminating the aberrant pattern that lz* detects。\" 这支持 \"characterization paper\" angle：我们 precisely 量化了检测的 boundary conditions。\n\n\nWorst 档核心假设：post-RL 检测完全失败（|d|<0.5）。\nGRPO 训练对 contamination signal 的破坏机制： (1) RL 优化 reward（整体 accuracy），不区分 seen/unseen items， 将 memorization-specific pattern 平滑化为 general improvement pattern； (2) RL 的 policy gradient update 改变了 response distribution 的结构， 消除了 SFT 阶段产生的 item-level aberrance pattern； (3) θ-shift 在 RL 后更严重（Δθ=0.62），因为 RL 同时提升 seen+unseen performance； (4) memorization fraction 从 pre-RL 的 ~35% 降至 post-RL 的 ~5%， 因为 RL 让模型\"真正学会了\"而非记住答案。\n这与 Wang et al. (2025) 的发现一致：RL 不仅破坏 log-prob methods， 也破坏 binary-pattern methods。差异在于 log-prob methods 因 distributional shift 失效， 而 binary-pattern methods 因 memorization-to-generalization conversion 失效。 机制不同但结果相同：post-RL detection ≈ random。\n唯一的正面叙事：lz* 的失败模式（memorization→generalization） 与 MinK%++ 的失败模式（distributional shift）不同， 这意味着两者可能 complementary——但在 worst 档下无法验证此假设。\n"
673	  },
674	  {
675	    "name": "exp-extra-benchmarks",
676	    "description": "BBH (6,511) + MATH (5,000) 扩展 benchmark",
677	    "results": {
678	      "bbh_4pl_params_available": false,
679	      "math_4pl_params_available": false,
680	      "need_own_calibration": true,
681	      "bbh_sim_power_15pct": 0.42,
682	      "math_sim_power_15pct": 0.35,
683	      "bbh_ctrl_contam_d_15pct": 0.5,
684	      "math_ctrl_contam_d_15pct": 0.3,
685	      "calibration_quality": {
686	        "bbh_a_r": 0.15,
687	        "math_a_r": 0.12
688	      },
689	      "items_in_power_gap": true
690	    },
691	    "tables": [
692	      {
693	        "caption": "Extended benchmarks: predicted vs observed power",
694	        "columns": [
695	          "benchmark",
696	          "n_items",
697	          "theory_power_15pct",
698	          "adjusted_power_15pct",
699	          "observed_d"
700	        ],
701	        "rows": [
702	          [
703	            "MMLU",
704	            14042,
705	            0.98,
706	            0.65,
707	            2.8
708	          ],
709	          [
710	            "HellaSwag",
711	            10042,
712	            0.75,
713	            0.45,
714	            1.0
715	          ],
716	          [
717	            "BBH",
718	            6511,
719	            0.42,
720	            0.18,
721	            0.5
722	          ],
723	          [
724	            "MATH",
725	            5000,
726	            0.35,
727	            0.12,
728	            0.3
729	          ],
730	          [
731	            "GSM8K",
732	            1319,
733	            0.59,
734	            0.15,
735	            0.3
736	          ]
737	        ]
738	      }
739	    ],
740	    "figures": [],
741	    "analysis": "BBH/MATH 证实了 power function 的定性预测（smaller benchmark = lower power）， 但定量拟合不佳（R²=0.65）。在 worst 档叙事中作为 \"partial validation of power theory\" 使用。 不增加 detection evidence，但增加 characterization evidence。\n\n\nWorst 档下 non-MMLU benchmarks 全面弱化。\nBBH/MATH 失败原因： (1) PSN-IRT 很可能不包含这些 benchmark 的 4PL 参数，需要自行校准； (2) 自行校准面临与 v1-refit 相同的问题——sample size 不足 + classical IRT estimation gap， a_r 预期在 0.12-0.15，discrimination 参数不可靠； (3) n_items 在 5K-6.5K 范围，理论 power@15% 仅 42%/35%（power function: min_items_15pct_80power=7958）， SFT generalization 折扣后 adjusted power 降至 15-20%； (4) MATH 的 binary response 定义可能有歧义（partial credit? exact match?）， 增加 measurement noise。\n这些 benchmark 的主要价值不是检测而是验证 power function： 如果 BBH (6.5K) 和 MATH (5K) 的 observed power 落在 power function 预测的 CI 内， 则 power function 作为 theoretical contribution 得到更强验证。 但在 worst 档下 R²<0.7，理论与实测脱节明显。\n"
742	  },
743	  {
744	    "name": "exp-domain-analysis",
745	    "description": "MMLU domain-level person-fit 分析",
746	    "results": {
747	      "gemini_domain_concentrated": false,
748	      "gemini_all_domains_flagged": true,
749	      "gemini_domain_lz_range": [
750	        12,
751	        25
752	      ],
753	      "gemini_stem_lz": 21,
754	      "gemini_humanities_lz": 18,
755	      "gemini_social_sciences_lz": 16,
756	      "gemini_other_lz": 15,
757	      "ctrl_contam_domain_uniform": true,
758	      "ctrl_contam_domain_lz_std": 2.1,
759	      "domain_level_detection_improvement": false
760	    },
761	    "tables": [
762	      {
763	        "caption": "Domain-level lz* for Gemini-1.5 and ctrl-contam models",
764	        "columns": [
765	          "model",
766	          "stem",
767	          "humanities",
768	          "social_sci",
769	          "other",
770	          "uniform_test_p"
771	        ],
772	        "rows": [
773	          [
774	            "Gemini-1.5",
775	            21,
776	            18,
777	            16,
778	            15,
779	            0.42
780	          ],
781	          [
782	            "Qwen-contam-15",
783	            4.5,
784	            3.8,
785	            3.2,
786	            3.0,
787	            0.68
788	          ],
789	          [
790	            "Qwen-contam-50",
791	            5.8,
792	            5.2,
793	            4.8,
794	            4.5,
795	            0.71
796	          ]
797	        ]
798	      }
799	    ],
800	    "figures": [],
801	    "analysis": "Domain analysis 不增加 detection power 但增加 interpretability。 在 worst 档叙事中作为 \"diagnostic tool\" angle 的 supporting evidence： 即使绝对检测力不足，domain-level profiles 提供 interpretability that other methods lack。\n\nWorst 档下 domain-level 分析不增加检测力。\nGemini-1.5 的 100% accuracy 意味着所有 domain 均被 \"完美回答\"， 无法区分哪些 domain 是 contaminated vs genuinely mastered。 ctrl-contam 的 QLoRA SFT 是在整个 MMLU 上训练的，contamination 是 uniform across domains， 所以 domain-level split 不提供额外信号。\n在 worst 档下，domain analysis 的价值是 interpretability 而非 detection： \"contamination fingerprint 是 domain-level uniform 而非 concentrated， 这与 benchmark-level SFT contamination 的预期一致\"。 但这不是 novel finding——是 experimental design 的 artifact（我们选择了 uniform contamination）。\n唯一的潜在价值：Phase B 12-model case study 中某些模型（Doubao） 显示 domain-selective misfit pattern，这可以作为 \"non-contamination misfit patterns exist\" 的证据， 但不能作为 detection 的证据。\n"
802	  }
803	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a82be2e-1dec-4630-a106-32ebe57d41bb",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "4c66dbf0-8afc-4a69-8d35-dca8f7c33679",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"exp-ctrl-contam-pilot\",\n    \"description\": \"Qwen3.5-9B × 4 conditions (0%×2/15%/50%) × MMLU only，go/no-go 信号\",\n    \"results\": {\n      \"clean_s1_lz_star\": 6.2,\n      \"clean_s2_lz_star\": 5.8,\n      \"clean_mean_lz_star\": 6.0,\n      \"clean_std_lz_star\": 0.28,\n      \"contam_15_lz_star\": 4.1,\n      \"contam_50_lz_star\": 5.5,\n      \"contam_15_delta_lz_star\": -1.9,\n      \"contam_50_delta_lz_star\": -0.5,\n      \"cohens_d_contam_15_ddof1\": -1.8,\n      \"cohens_d_contam_50_ddof1\": -0.5,\n      \"memorization_fraction_15pct\": 0.22,\n      \"memorization_fraction_50pct\": 0.18,\n      \"theta_shift_15pct\": 0.21,\n      \"theta_shift_50pct\": 0.39,\n      \"theta_fixed_restores_monotonicity\": true,\n      \"theta_fixed_ratio\": 2.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Pilot: Qwen3.5-9B × MMLU Δlz* summary\",\n        \"columns\": [\n          \"condition\",\n          \"lz_star\",\n          \"delta_lz_star\",\n          \"cohens_d\",\n          \"acc\",\n          \"theta\",\n          \"memo_frac\"\n        ],\n        \"rows\": [\n          [\n            \"clean_s1\",\n            6.2,\n            0,\n            \"-\",\n            0.672,\n            -0.12,\n            \"-\"\n          ],\n          [\n            \"clean_s2\",\n            5.8,\n            0,\n            \"-\",\n            0.668,\n            -0.14,\n            \"-\"\n          ],\n          [\n            \"contam_15\",\n            4.1,\n            -1.9,\n            -1.8,\n            0.718,\n            0.09,\n            0.22\n          ],\n          [\n            \"contam_50\",\n            5.5,\n            -0.5,\n            -0.5,\n            0.751,\n            0.27,\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Go 信号成立但弱于 best/expected。Qwen 在 15% 可检测，50% 因 θ-shift 信号衰减。 memorization fraction 低意味着 power function 的 upper bound 与 adjusted power 差距大。 需要 cross-family 验证，但预期 Gemma/Mistral 会失败。\\n\\n\\nWorst 档下 Qwen 仍检测成功（已验证家族），但效应量比实际偏弱。 contam_15 |d|≈1.8 仍然 significant（Qwen 是最强信号家族之一）， 但 contam_50 出现非单调（free-θ 下 |d|=0.5），θ-shift 吃掉大部分信号。 memorization fraction 偏低（22%），说明 SFT generalization 比预期更强—— 模型不是死记硬背而是\\\"学会了\\\"，导致 seen/unseen accuracy gap 缩小。 这是 worst 档的核心机制：SFT generalization 过强，lz* 检测的 memorization 信号被稀释。 θ-fixed 仍能恢复单调性，因为 θ-shift 是可修正的 confound，但绝对效应量仍低。 Go/no-go 判定：go（但仅限 Qwen），需要 cross-family 验证。\\n\"\n  },\n  {\n    \"name\": \"exp-ctrl-contam (full)\",\n    \"description\": \"4 模型 × 6 levels × 3 benchmarks 完整控制实验\",\n    \"results\": {\n      \"qwen_mmlu_d_15pct\": -2.8,\n      \"llama_mmlu_d_15pct\": -2.2,\n      \"gemma_mmlu_d_15pct\": -0.7,\n      \"mistral_mmlu_d_15pct\": -0.4,\n      \"d_15pct_min_across_families\": 0.4,\n      \"d_15pct_mean_across_families\": 1.5,\n      \"n_families_d_gt_2\": 2,\n      \"hellaswag_d_15pct_mean\": 0.5,\n      \"gsm8k_d_15pct_mean\": 0.3,\n      \"gemma_memorization_fraction_15pct\": 0.15,\n      \"mistral_memorization_fraction_15pct\": 0.17,\n      \"qwen_memorization_fraction_15pct\": 0.35,\n      \"llama_memorization_fraction_15pct\": 0.32,\n      \"theta_fixed_monotonic_families\": 2,\n      \"theta_fixed_fails_gemma\": true,\n      \"theta_fixed_fails_mistral\": true,\n      \"dose_response_monotonic_free_theta\": 1,\n      \"dose_response_monotonic_fixed_theta\": 2,\n      \"hellaswag_any_family_d_gt_2\": false,\n      \"gsm8k_any_family_d_gt_2\": false,\n      \"gsm8k_best_family_d\": 0.8,\n      \"hellaswag_best_family_d\": 1.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 1: Cohen's d at 15% contamination by family × benchmark\",\n        \"columns\": [\n          \"family\",\n          \"mmlu_d\",\n          \"hellaswag_d\",\n          \"gsm8k_d\",\n          \"mean_d\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            -2.8,\n            -1.0,\n            -0.6,\n            -1.47\n          ],\n          [\n            \"Llama-3.1-8B\",\n            -2.2,\n            -0.8,\n            -0.5,\n            -1.17\n          ],\n          [\n            \"Gemma-4-12B\",\n            -0.7,\n            -0.3,\n            -0.1,\n            -0.37\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            -0.4,\n            -0.2,\n            -0.1,\n            -0.23\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 2: Memorization fraction by family (15% contamination)\",\n        \"columns\": [\n          \"family\",\n          \"mmlu\",\n          \"hellaswag\",\n          \"gsm8k\",\n          \"mean\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            0.35,\n            0.28,\n            0.2,\n            0.28\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.32,\n            0.25,\n            0.18,\n            0.25\n          ],\n          [\n            \"Gemma-4-12B\",\n            0.15,\n            0.12,\n            0.08,\n            0.12\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.17,\n            0.13,\n            0.09,\n            0.13\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 3: θ-fixed vs free-θ dose-response monotonicity\",\n        \"columns\": [\n          \"family\",\n          \"free_theta_monotonic\",\n          \"fixed_theta_monotonic\",\n          \"theta_shift_at_50pct\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            false,\n            true,\n            0.45\n          ],\n          [\n            \"Llama-3.1-8B\",\n            true,\n            true,\n            0.48\n          ],\n          [\n            \"Gemma-4-12B\",\n            false,\n            false,\n            0.52\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            false,\n            false,\n            0.38\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心结论：detection 不 generalize。2/4 家族 |d|>2（Qwen+Llama），2/4 家族 |d|<1。 非 MMLU benchmark 全面弱化。不能 claim \\\"IRT person-fit detects contamination\\\"， 只能 claim \\\"IRT person-fit detects contamination under specific conditions (sufficient n_items, sufficient memorization fraction, specific model architectures)\\\"。 必须 reframe。memorization fraction 的极端分化（15-38%）是关键发现—— 这说明 SFT generalization 是 model-specific 的，binary-only detection 的天花板由此决定。\\n\\n\\nWorst 档核心假设：ctrl-contam 仅在已验证的 Qwen+Llama 有效。\\nQwen/Llama 成功原因：这两个家族在 SFT 时 memorization fraction 较高（32-38%）， 产生足够的 aberrant pattern 让 lz* 捕捉。Qwen baseline misfit 高（lz*≈8.7）， Llama baseline 低（lz*≈-0.14），但两者都在 MMLU 上产生 |d|>2。\\nGemma 失败原因：Gemma 家族的 SFT generalization 特别强。SFT 后模型不仅记住 seen items， 还大幅提升 unseen items 的正确率，memorization fraction 降至 15%。 这意味着 contaminated response pattern 与 \\\"genuinely improved\\\" pattern 几乎不可区分。 另外 Gemma 的 4PL 参数适配可能不佳——PSN-IRT 的参数是在不同模型群体上估计的， Gemma 架构的 response pattern 可能需要不同的 item parameters。 |d|=0.7 在统计上可能 barely significant（p≈0.05 with n=3），但不足以支撑 detection claim。\\nMistral 失败原因：Mistral-7B-v0.3 是相对较弱的模型，baseline accuracy 低。 SFT 后 θ 提升幅度大但 pattern 变化方式更像 \\\"legitimate learning\\\"。 4PL 参数对低能力模型的 discrimination 不足（a 参数区域覆盖差）， 导致 lz* 对 contamination-induced pattern change 不敏感。|d|=0.4，不显著。\\n非 MMLU benchmark 失败原因：n_items 不足。HellaSwag (10K) 勉强可用但 4PL 参数估计质量下降， GSM8K (1.3K) 太小导致 lz* 方差大、信噪比低。power function 预测 GSM8K@15% 理论 power≈59%， 但 SFT generalization 折扣后 adjusted power≈20-30%。\\nθ-fixed 仅在 Qwen+Llama 恢复信号：因为这两个家族的 θ-shift 是主要 confound， fix θ 后信号恢复。Gemma/Mistral 的问题不是 θ-shift 而是 memorization fraction 本身太低， θ-fixed 无法修复根本问题。\\n\"\n  },\n  {\n    \"name\": \"exp-leaderboard-audit\",\n    \"description\": \"Open LLM Leaderboard v1 大规模扫描（已 ABANDONED）\",\n    \"results\": {\n      \"status\": \"ABANDONED — not executed\",\n      \"reason\": \"D011 v1-irt-refit a_r=0.111, item alignment 54.56%\",\n      \"hypothetical_if_forced\": {\n        \"n_models_scanned\": 500,\n        \"flagged_rate_mmlu\": 0.92,\n        \"flagged_rate_overall\": 0.88,\n        \"false_positive_rate_estimated\": \">80%\",\n        \"meaningful_contamination_signal\": false\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Abandon 决策正确。v1 数据可用性写入 Discussion/Future Work， 强调 \\\"13K+ per-item data publicly available, awaiting better IRT estimation methods\\\"。\\n\\n\\n已 abandoned 因 a_r=0.111（discrimination 完全失败）和 item alignment 仅 54.56%。 即使强行执行，v1 refit 的 IRT 参数质量太差，lz* 退化为 accuracy-like statistic， flagging 率与 accuracy z-score 高度相关，无法区分 contamination 与 ability。 在 worst 档下这个实验根本不应该做，正确的决定是 abandon。\\n\"\n  },\n  {\n    \"name\": \"exp-natural-experiment\",\n    \"description\": \"v1 leaderboard base→chat model pairs 自然实验\",\n    \"results\": {\n      \"n_pairs\": 4,\n      \"n_complete_pairs\": 3,\n      \"significant_benchmarks\": 0,\n      \"mmlu_p\": 0.45,\n      \"hellaswag_p\": 0.28,\n      \"gsm8k_p\": 0.31,\n      \"arc_c_p\": 0.62,\n      \"individual_outliers\": 0,\n      \"effect_interpretable\": false\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Base→Chat Δlz* paired t-tests (v1 IRT parameters)\",\n        \"columns\": [\n          \"benchmark\",\n          \"mean_delta_lz\",\n          \"t_stat\",\n          \"p_value\",\n          \"n_pairs\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            1.2,\n            0.85,\n            0.45,\n            4\n          ],\n          [\n            \"HellaSwag\",\n            -2.1,\n            -1.3,\n            0.28,\n            4\n          ],\n          [\n            \"GSM8K\",\n            1.8,\n            1.15,\n            0.31,\n            4\n          ],\n          [\n            \"ARC-C\",\n            -0.5,\n            -0.52,\n            0.62,\n            4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计检验能力不足 + IRT 参数质量差 = 无法得出任何结论。 P2-optional 优先级正确。在 worst 档叙事中仅作为 \\\"attempted but inconclusive\\\" 提及。\\n\\n\\nWorst 档下 a_r=0.111 导致 lz* 退化。仅 4-5 pairs 没有统计检验能力（power<0.2 for d=0.5）。 Base→chat 的 SFT 效应被 IRT 参数质量低掩盖。即使有 systematic shift， n_pairs 太少无法达到 significance。此外，base→chat 的 SFT 是 general instruction tuning， 不是 benchmark-specific contamination，所以即使检测到 Δlz*，也无法归因为 contamination。 Worst 档下这个实验提供 zero additional evidence。\\n\"\n  },\n  {\n    \"name\": \"exp-v1-irt-refit-expanded\",\n    \"description\": \"扩大 v1 IRT 重拟合样本量至 N≥500，最终关闭 Path D\",\n    \"results\": {\n      \"n_models_downloaded\": 520,\n      \"n_models_usable\": 410,\n      \"a_pearson_r_3pl\": 0.13,\n      \"a_pearson_r_2pl\": -0.02,\n      \"b_pearson_r_3pl\": 0.68,\n      \"b_spearman_r_3pl\": 0.7,\n      \"path_d_verdict\": \"DEAD\",\n      \"discrimination_above_threshold\": false\n    },\n    \"tables\": [\n      {\n        \"caption\": \"IRT refit: parameter recovery by sample size\",\n        \"columns\": [\n          \"N\",\n          \"a_r_3pl\",\n          \"a_r_2pl\",\n          \"b_r_3pl\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            63,\n            0.111,\n            -0.084,\n            0.626,\n            \"dead\"\n          ],\n          [\n            178,\n            0.127,\n            -0.029,\n            0.663,\n            \"dead\"\n          ],\n          [\n            520,\n            0.13,\n            -0.02,\n            0.68,\n            \"dead\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Path D 最终关闭。Classical IRT estimation 无法恢复 PSN-IRT 的 neural-estimated discrimination。 这本身是 methodological contribution（Claim 3c）：quantify classical vs neural IRT gap。 在 worst 档叙事中作为 \\\"impossibility result\\\" 贡献。\\n\\n\\nN=63→178 时 a_r 仅从 0.111 提升到 0.127。Worst 档下 N=500+ 带来的边际改善极小（a_r≈0.13）， 远低于 0.2 threshold，更不可能达到 0.4 可行线。\\n根本原因不是样本量而是 classical IRT (MML-EM) 与 neural IRT 的 estimation paradigm gap： (1) classical IRT 假设 unidimensional latent trait，但 LLM 能力是高维的； (2) LLM response patterns violate local independence（同 domain items 高度相关）； (3) v1 leaderboard 模型异质性太高（从 1B 到 70B，架构各异）， 单一 θ dimension 无法 capture 这种异质性。 b 参数（difficulty）较好恢复是因为 item difficulty 是 population-level statistic， 对 latent structure 假设不敏感；a 参数（discrimination）需要精确的 latent structure。\\n\"\n  },\n  {\n    \"name\": \"exp-4pl-ablation\",\n    \"description\": \"4PL vs 3PL(d=1) ablation in simulation\",\n    \"results\": {\n      \"far_4pl\": 0.05,\n      \"far_3pl\": 0.12,\n      \"far_2pl\": 0.65,\n      \"mean_power_gain_4pl_vs_3pl_mmlu\": 0.18,\n      \"mean_power_gain_4pl_vs_3pl_hellaswag\": 0.15,\n      \"mean_power_gain_4pl_vs_3pl_gsm8k\": 0.12,\n      \"ctrl_contam_4pl_vs_3pl_delta_d\": 0.8,\n      \"ctrl_contam_3pl_d_15pct_qwen\": -1.5,\n      \"ctrl_contam_4pl_d_15pct_qwen\": -2.8\n    },\n    \"tables\": [\n      {\n        \"caption\": \"4PL vs 3PL detection power comparison\",\n        \"columns\": [\n          \"benchmark\",\n          \"power_4pl_15pct\",\n          \"power_3pl_15pct\",\n          \"gain_pp\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.98,\n            0.8,\n            18\n          ],\n          [\n            \"HellaSwag\",\n            0.75,\n            0.6,\n            15\n          ],\n          [\n            \"GSM8K\",\n            0.59,\n            0.47,\n            12\n          ],\n          [\n            \"ARC-C\",\n            0.13,\n            0.09,\n            4\n          ],\n          [\n            \"HumanEval\",\n            0.24,\n            0.18,\n            6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simulation-level ablation 仍成立。4PL 是必要的 model specification。 但这仅是 necessary condition，不是 sufficient condition for detection。 在 worst 档叙事中，4PL ablation 作为 methodological contribution 保留， 但不能作为 \\\"detection works\\\" 的证据。\\n\\n\\n4PL ablation 在 simulation 层面是 robust 的（这是 model specification 问题，不受 generalization 影响）。 即使在 worst 档，4PL 仍优于 3PL/2PL，因为 LLM high-ability models 确实需要 d parameter。 但 worst 档的差异在于：ctrl-contam 验证时 4PL 优势在 failing families（Gemma/Mistral） 上体现不出来——因为两者都失败了。优势仅在 Qwen/Llama 上体现， 使得 \\\"4PL essential\\\" 的 claim 变成 \\\"4PL essential for the families where detection works at all\\\"。 Power gain 数值低于 best 档因为 worst 档假设部分 4PL 参数（特别是 d 值接近 1 的 items） 对 detection 贡献有限。\\n\"\n  },\n  {\n    \"name\": \"exp-baseline-comparison\",\n    \"description\": \"与 ≥5 baselines 对比 AUROC/Type-I error\",\n    \"results\": {\n      \"auroc_lz_star_15pct\": 0.62,\n      \"auroc_mink_pp_15pct\": 0.82,\n      \"auroc_ppl_15pct\": 0.78,\n      \"auroc_constat_15pct\": 0.85,\n      \"auroc_acc_zscore_15pct\": 0.55,\n      \"auroc_random_15pct\": 0.5,\n      \"auroc_lz_star_5pct\": 0.58,\n      \"auroc_mink_pp_5pct\": 0.72,\n      \"auroc_ppl_5pct\": 0.68,\n      \"auroc_constat_5pct\": 0.75,\n      \"auroc_acc_zscore_5pct\": 0.52,\n      \"auroc_gap_15pct_vs_best\": -0.23,\n      \"auroc_gap_5pct_vs_best\": -0.17,\n      \"type_i_lz_star\": 0.06,\n      \"type_i_mink_pp\": 0.04,\n      \"type_i_constat\": 0.05,\n      \"ci_lz_star_15pct\": [\n        0.54,\n        0.7\n      ],\n      \"ci_mink_pp_15pct\": [\n        0.76,\n        0.88\n      ],\n      \"auroc_lz_star_post_rl\": 0.53,\n      \"auroc_mink_pp_post_rl\": 0.51,\n      \"auroc_ppl_post_rl\": 0.52\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: AUROC comparison at 15% contamination (bootstrap 95% CI)\",\n        \"columns\": [\n          \"method\",\n          \"info_level\",\n          \"auroc_mean\",\n          \"ci_lower\",\n          \"ci_upper\",\n          \"type_i\"\n        ],\n        \"rows\": [\n          [\n            \"ConStat\",\n            \"rephrased-retest\",\n            0.85,\n            0.79,\n            0.91,\n            0.05\n          ],\n          [\n            \"MinK%++\",\n            \"token-probs\",\n            0.82,\n            0.76,\n            0.88,\n            0.04\n          ],\n          [\n            \"PPL-based\",\n            \"log-probs\",\n            0.78,\n            0.71,\n            0.85,\n            0.06\n          ],\n          [\n            \"lz* (ours)\",\n            \"binary-only\",\n            0.62,\n            0.54,\n            0.7,\n            0.06\n          ],\n          [\n            \"Acc z-score\",\n            \"binary-only\",\n            0.55,\n            0.48,\n            0.62,\n            0.08\n          ],\n          [\n            \"Random\",\n            \"none\",\n            0.5,\n            0.5,\n            0.5,\n            0.05\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: AUROC by contamination level (lz* vs best privileged)\",\n        \"columns\": [\n          \"contam_pct\",\n          \"auroc_lz_star\",\n          \"auroc_best_privileged\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            3,\n            0.54,\n            0.62,\n            -0.08\n          ],\n          [\n            5,\n            0.58,\n            0.72,\n            -0.14\n          ],\n          [\n            10,\n            0.6,\n            0.78,\n            -0.18\n          ],\n          [\n            15,\n            0.62,\n            0.85,\n            -0.23\n          ],\n          [\n            25,\n            0.68,\n            0.91,\n            -0.23\n          ],\n          [\n            50,\n            0.74,\n            0.95,\n            -0.21\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lz* 显著弱于 privileged methods，但仍优于 random 和 accuracy z-score。 这证实了 \\\"minimal-information operating point\\\" 的代价。 在 worst 档叙事中，这个 gap 本身是 contribution： \\\"we precisely quantify the detection power lost by operating at the binary-only level\\\"。 Figure showing the detection frontier (info access vs AUROC) 是论文的 key figure。\\n\\n\\nWorst 档核心假设：lz* 在所有区间显著落后于 MinK%++（>15% AUROC gap）。\\nlz* AUROC 低的原因： (1) binary-only 信息瓶颈——lz* 只看对/错，而 MinK%++ 用 token-level probability， 信息量差异是本质性的（每个 item MinK%++ 有数百个 token prob vs lz* 有 1 bit）； (2) SFT generalization 将 memorization fraction 降至 15-38%， 真正产生 aberrant signal 的 items 比例低； (3) Gemma/Mistral 失败拖低 cross-family average AUROC。\\nlz* 仅在两个极端条件下有 competitive advantage： (a) post-RL：所有 log-prob methods 失效（AUROC≈0.50-0.52），lz* 也失效但程度类似（0.53）， 差距消失但这不是 \\\"优势\\\" 而是 \\\"everyone fails\\\"； (b) 极低 contamination (3-5%)：lz* 的 IRT inductive bias 在 n=3 seeds 下 可能比需要更多 training data 的 supervised methods 稍好，但优势仅 +0.05 AUROC， 不足以 claim superiority。\\nConStat 是最强 baseline（需要 re-test），因为 re-phrased questions 直接测 memorization vs understanding， 信息量远超 binary-only。\\n-23% AUROC gap 在论文中必须 honestly 报告。Reframe 方向： \\\"we quantify the cost of operating at the minimal-information point\\\"。\\n\"\n  },\n  {\n    \"name\": \"exp-multiscale-lzm\",\n    \"description\": \"跨 benchmark 聚合 lzm 统计量\",\n    \"results\": {\n      \"lzm_improves_over_per_benchmark_lz\": false,\n      \"lzm_auroc_15pct\": 0.6,\n      \"lzm_vs_lz_star_auroc_delta\": -0.02,\n      \"cross_benchmark_correlation_low\": true,\n      \"aggregation_benefit\": \"negligible\",\n      \"psn_12_model_lzm_flagged\": 10\n    },\n    \"tables\": [\n      {\n        \"caption\": \"lzm vs per-benchmark lz* AUROC\",\n        \"columns\": [\n          \"method\",\n          \"auroc_15pct\",\n          \"auroc_50pct\"\n        ],\n        \"rows\": [\n          [\n            \"lz*_MMLU_only\",\n            0.62,\n            0.74\n          ],\n          [\n            \"lz*_HellaSwag_only\",\n            0.55,\n            0.62\n          ],\n          [\n            \"lzm_aggregated\",\n            0.6,\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 不作为主要 contribution。在论文中可以用一句话提及 \\\"cross-benchmark aggregation did not improve detection, consistent with the low cross-benchmark correlation of lz*\\\"。\\n\\n\\nWorst 档下 lzm 无法改善检测。原因： (1) 非 MMLU benchmark 的 lz* 信号太弱（|d|<0.8），聚合时引入更多 noise 而非 signal； (2) cross-benchmark lz* 相关性很低（Phase B 仅 1/10 对显著）， 说明 contamination signal 在不同 benchmark 上不 coherent，聚合不增加信息量； (3) lzm 统计量假设各 benchmark 的 lz* 独立同分布， 但实际上 benchmark-specific 的 4PL 参数质量差异大（MMLU 好，HumanEval 差）。 在 worst 档下，lzm 甚至可能因为纳入低质量 benchmark 而降低 MMLU-only 的检测力。\\n\"\n  },\n  {\n    \"name\": \"exp-post-rl\",\n    \"description\": \"Post-RL 检测：SFT 污染 → GRPO 训练 → person-fit 测试\",\n    \"results\": {\n      \"cohens_d_pre_rl_15pct\": -2.5,\n      \"cohens_d_post_rl_15pct\": -0.3,\n      \"cohens_d_post_rl_50pct\": -0.4,\n      \"lz_star_post_rl_contam_15\": 7.8,\n      \"lz_star_post_rl_clean\": 8.1,\n      \"delta_lz_post_rl\": -0.3,\n      \"post_rl_detection_power\": 0.08,\n      \"rl_training_steps\": 2000,\n      \"rl_reward_type\": \"rule-based (MMLU accuracy)\",\n      \"memorization_fraction_post_rl\": 0.05,\n      \"theta_shift_post_rl\": 0.62,\n      \"experiment_completion\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Pre-RL vs Post-RL detection\",\n        \"columns\": [\n          \"condition\",\n          \"lz_star\",\n          \"delta_lz\",\n          \"cohens_d\",\n          \"memo_frac\",\n          \"theta\"\n        ],\n        \"rows\": [\n          [\n            \"clean\",\n            8.1,\n            0,\n            \"-\",\n            \"-\",\n            -0.1\n          ],\n          [\n            \"contam_15_pre_rl\",\n            4.2,\n            -3.9,\n            -2.5,\n            0.35,\n            0.12\n          ],\n          [\n            \"contam_15_post_rl\",\n            7.8,\n            -0.3,\n            -0.3,\n            0.05,\n            0.52\n          ],\n          [\n            \"contam_50_pre_rl\",\n            6.8,\n            -1.3,\n            -0.8,\n            0.28,\n            0.28\n          ],\n          [\n            \"contam_50_post_rl\",\n            7.5,\n            -0.6,\n            -0.4,\n            0.06,\n            0.68\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-RL 检测完全失败。但这不是新发现（Wang et al. 2025 已 established）， 而是 confirms that binary-only methods share the same limitation。 在 worst 档叙事中的用法：\\\"post-RL failure is expected and consistent with the theoretical framework — RL converts memorization to generalization, eliminating the aberrant pattern that lz* detects。\\\" 这支持 \\\"characterization paper\\\" angle：我们 precisely 量化了检测的 boundary conditions。\\n\\n\\nWorst 档核心假设：post-RL 检测完全失败（|d|<0.5）。\\nGRPO 训练对 contamination signal 的破坏机制： (1) RL 优化 reward（整体 accuracy），不区分 seen/unseen items， 将 memorization-specific pattern 平滑化为 general improvement pattern； (2) RL 的 policy gradient update 改变了 response distribution 的结构， 消除了 SFT 阶段产生的 item-level aberrance pattern； (3) θ-shift 在 RL 后更严重（Δθ=0.62），因为 RL 同时提升 seen+unseen performance； (4) memorization fraction 从 pre-RL 的 ~35% 降至 post-RL 的 ~5%， 因为 RL 让模型\\\"真正学会了\\\"而非记住答案。\\n这与 Wang et al. (2025) 的发现一致：RL 不仅破坏 log-prob methods， 也破坏 binary-pattern methods。差异在于 log-prob methods 因 distributional shift 失效， 而 binary-pattern methods 因 memorization-to-generalization conversion 失效。 机制不同但结果相同：post-RL detection ≈ random。\\n唯一的正面叙事：lz* 的失败模式（memorization→generalization） 与 MinK%++ 的失败模式（distributional shift）不同， 这意味着两者可能 complementary——但在 worst 档下无法验证此假设。\\n\"\n  },\n  {\n    \"name\": \"exp-extra-benchmarks\",\n    \"description\": \"BBH (6,511) + MATH (5,000) 扩展 benchmark\",\n    \"results\": {\n      \"bbh_4pl_params_available\": false,\n      \"math_4pl_params_available\": false,\n      \"need_own_calibration\": true,\n      \"bbh_sim_power_15pct\": 0.42,\n      \"math_sim_power_15pct\": 0.35,\n      \"bbh_ctrl_contam_d_15pct\": 0.5,\n      \"math_ctrl_contam_d_15pct\": 0.3,\n      \"calibration_quality\": {\n        \"bbh_a_r\": 0.15,\n        \"math_a_r\": 0.12\n      },\n      \"items_in_power_gap\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Extended benchmarks: predicted vs observed power\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"theory_power_15pct\",\n          \"adjusted_power_15pct\",\n          \"observed_d\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            14042,\n            0.98,\n            0.65,\n            2.8\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.75,\n            0.45,\n            1.0\n          ],\n          [\n            \"BBH\",\n            6511,\n            0.42,\n            0.18,\n            0.5\n          ],\n          [\n            \"MATH\",\n            5000,\n            0.35,\n            0.12,\n            0.3\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.59,\n            0.15,\n            0.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH/MATH 证实了 power function 的定性预测（smaller benchmark = lower power）， 但定量拟合不佳（R²=0.65）。在 worst 档叙事中作为 \\\"partial validation of power theory\\\" 使用。 不增加 detection evidence，但增加 characterization evidence。\\n\\n\\nWorst 档下 non-MMLU benchmarks 全面弱化。\\nBBH/MATH 失败原因： (1) PSN-IRT 很可能不包含这些 benchmark 的 4PL 参数，需要自行校准； (2) 自行校准面临与 v1-refit 相同的问题——sample size 不足 + classical IRT estimation gap， a_r 预期在 0.12-0.15，discrimination 参数不可靠； (3) n_items 在 5K-6.5K 范围，理论 power@15% 仅 42%/35%（power function: min_items_15pct_80power=7958）， SFT generalization 折扣后 adjusted power 降至 15-20%； (4) MATH 的 binary response 定义可能有歧义（partial credit? exact match?）， 增加 measurement noise。\\n这些 benchmark 的主要价值不是检测而是验证 power function： 如果 BBH (6.5K) 和 MATH (5K) 的 observed power 落在 power function 预测的 CI 内， 则 power function 作为 theoretical contribution 得到更强验证。 但在 worst 档下 R²<0.7，理论与实测脱节明显。\\n\"\n  },\n  {\n    \"name\": \"exp-domain-analysis\",\n    \"description\": \"MMLU domain-level person-fit 分析\",\n    \"results\": {\n      \"gemini_domain_concentrated\": false,\n      \"gemini_all_domains_flagged\": true,\n      \"gemini_domain_lz_range\": [\n        12,\n        25\n      ],\n      \"gemini_stem_lz\": 21,\n      \"gemini_humanities_lz\": 18,\n      \"gemini_social_sciences_lz\": 16,\n      \"gemini_other_lz\": 15,\n      \"ctrl_contam_domain_uniform\": true,\n      \"ctrl_contam_domain_lz_std\": 2.1,\n      \"domain_level_detection_improvement\": false\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Domain-level lz* for Gemini-1.5 and ctrl-contam models\",\n        \"columns\": [\n          \"model\",\n          \"stem\",\n          \"humanities\",\n          \"social_sci\",\n          \"other\",\n          \"uniform_test_p\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            21,\n            18,\n            16,\n            15,\n            0.42\n          ],\n          [\n            \"Qwen-contam-15\",\n            4.5,\n            3.8,\n            3.2,\n            3.0,\n            0.68\n          ],\n          [\n            \"Qwen-contam-50\",\n            5.8,\n            5.2,\n            4.8,\n            4.5,\n            0.71\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 不增加 detection power 但增加 interpretability。 在 worst 档叙事中作为 \\\"diagnostic tool\\\" angle 的 supporting evidence： 即使绝对检测力不足，domain-level profiles 提供 interpretability that other methods lack。\\n\\nWorst 档下 domain-level 分析不增加检测力。\\nGemini-1.5 的 100% accuracy 意味着所有 domain 均被 \\\"完美回答\\\"， 无法区分哪些 domain 是 contaminated vs genuinely mastered。 ctrl-contam 的 QLoRA SFT 是在整个 MMLU 上训练的，contamination 是 uniform across domains， 所以 domain-level split 不提供额外信号。\\n在 worst 档下，domain analysis 的价值是 interpretability 而非 detection： \\\"contamination fingerprint 是 domain-level uniform 而非 concentrated， 这与 benchmark-level SFT contamination 的预期一致\\\"。 但这不是 novel finding——是 experimental design 的 artifact（我们选择了 uniform contamination）。\\n唯一的潜在价值：Phase B 12-model case study 中某些模型（Doubao） 显示 domain-selective misfit pattern，这可以作为 \\\"non-contamination misfit patterns exist\\\" 的证据， 但不能作为 detection 的证据。\\n\"\n  }\n]",
      "numLines": 803,
      "startLine": 1,
      "totalLines": 803
    }
  },
  "sourceToolAssistantUUID": "3a82be2e-1dec-4630-a106-32ebe57d41bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:00:04.063Z_

<details><summary>↩ Tool result · `toolu_012kRfFMcr5wcTPvZrapwbwa`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.
15	
16	**Claim 3 (Empirical Findings from Real LLM Data)**:
17	Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
48	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
49	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
50	
51	## Key Narrative Elements (from External Review + Distillation)
52	
53	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
54	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
55	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
56	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
57	5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
58	6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
59	7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
60	8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
61	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
62	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
63	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
64	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
65	13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
66	
67	## Writing Strategy (from Distillation)
68	
69	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
70	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
71	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
72	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
73	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
74	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
75	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
76	
77	## Evidence Summary
78	
79	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
80	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
81	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).
82	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
83	- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.
84	- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = "θ_fixed repairs non-monotonicity"; Llama story = "θ_fixed enhances existing monotonicity". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.
85	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21544d4c-5247-4b78-9f62-05478d615eee",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "5e969fc2-cb34-420c-862f-7e1f6576cd46",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  },
  "sourceToolAssistantUUID": "21544d4c-5247-4b78-9f62-05478d615eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:00:04.051Z_

<details open><summary>🔧 Tool call — Read · `toolu_012kRfFMcr5wcTPvZrapwbwa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c66dbf0-8afc-4a69-8d35-dca8f7c33679",
  "isSidechain": false,
  "requestId": "req_011CbF3bjGxBwJycQxQL14jy",
  "type": "assistant",
  "uuid": "21544d4c-5247-4b78-9f62-05478d615eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k37oJmPHLugqaybnYtKJA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11743,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11743
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "5e969fc2-cb34-420c-862f-7e1f6576cd46",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case paper on IRT contamination detection",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Assistant

_source line 14 · 2026-05-21T04:00:30.870Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me also load the paper-writing-norms skill to ensure I follow the right conventions, and check if there's a ROADMAP or other context files.

Actually, the instructions say "不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完". Let me just write the paper directly.

Let me analyze what I have:

**Tier: worst** - This means the paper should present the most pessimistic interpretation of results.

**Key narrative from guidance:**
- Core detection claim doesn't hold
- ctrl-contam only works on Qwen+Llama (verified families), Gemma/Mistral generalization fails


- Non-MMLU benchmarks show severely limited detection capability
- Post-RL detection completely breaks down
- lz* methods fall significantly short compared to privileged approaches in baseline comparisons
- I need to reframe this as a characterization and impossibility paper rather than claiming general detection works
- But simulation, universal misfit, θ-shift, 4PL ablation, and the seen/unseen split analysis remain solid contributions

For experiments, I'm covering the Qwen pilot, the full ctrl-contam study across 4 models with 6 contamination levels and 3 benchmarks, while abandoning the leaderboard audit.

Looking at the remaining experiments: the natural experiment with base-to-chat model pairs didn't yield clear results, the IRT refit approach failed to work, the 4PL versus 3PL simulation comparison shows the value of the fuller model, baseline comparisons reveal the gap between binary-only and privileged methods, cross-benchmark aggregation provides minimal gains, post-RL detection fails entirely, extra benchmarks like BBH and MATH show weak performance, and domain-level MMLU analysis rounds out the characterization.

I'm framing this as a paper about the limits and impossibility of binary-only contamination detection, being honest about what works and what doesn't. Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e969fc2-cb34-420c-862f-7e1f6576cd46",
  "isSidechain": false,
  "requestId": "req_011CbF3c99eJ2Vf2hKQ9DzSu",
  "type": "assistant",
  "uuid": "30f93c7d-2db6-4d3c-adf4-fe59d2fd56f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj5T6n7UeEVq6K7fdpTp6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18888,
      "cache_read_input_tokens": 23584,
      "output_tokens": 981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 981,
          "cache_read_input_tokens": 23584,
          "cache_creation_input_tokens": 18888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18888
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

_source line 15 · 2026-05-21T04:00:30.930Z_

Now let me read the paper-writing-norms skill for reference, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30f93c7d-2db6-4d3c-adf4-fe59d2fd56f4",
  "isSidechain": false,
  "requestId": "req_011CbF3c99eJ2Vf2hKQ9DzSu",
  "type": "assistant",
  "uuid": "c40dd83c-ed11-4a07-8c0d-73328a002eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj5T6n7UeEVq6K7fdpTp6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18888,
      "cache_read_input_tokens": 23584,
      "output_tokens": 981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 981,
          "cache_read_input_tokens": 23584,
          "cache_creation_input_tokens": 18888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18888
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

_source line 16 · 2026-05-21T04:00:31.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hhsu4A3oH2xcz3y2j4jio2`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c40dd83c-ed11-4a07-8c0d-73328a002eb5",
  "isSidechain": false,
  "requestId": "req_011CbF3c99eJ2Vf2hKQ9DzSu",
  "type": "assistant",
  "uuid": "730c0736-7ae1-4f88-b679-5d2c65e2810e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj5T6n7UeEVq6K7fdpTp6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18888,
      "cache_read_input_tokens": 23584,
      "output_tokens": 981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 981,
          "cache_read_input_tokens": 23584,
          "cache_creation_input_tokens": 18888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18888
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

_source line 17 · 2026-05-21T04:00:35.125Z_

<details><summary>↩ Tool result · `toolu_01QDHvvCxXi8jcECYbeuz2Sh`</summary>

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
  "parentUuid": "8c6e7d38-0fa3-4ca3-af10-c1d1d1ef961d",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "60f92895-14c9-4f82-9e62-6bcd274ff507",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8c6e7d38-0fa3-4ca3-af10-c1d1d1ef961d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:00:31.315Z_

<details><summary>↩ Tool result · `toolu_01Hhsu4A3oH2xcz3y2j4jio2`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "730c0736-7ae1-4f88-b679-5d2c65e2810e",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "37920cd5-76f1-47b0-98ba-142c51ff22ff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "730c0736-7ae1-4f88-b679-5d2c65e2810e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:00:34.974Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QDHvvCxXi8jcECYbeuz2Sh`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37920cd5-76f1-47b0-98ba-142c51ff22ff",
  "isSidechain": false,
  "requestId": "req_011CbF3c99eJ2Vf2hKQ9DzSu",
  "type": "assistant",
  "uuid": "8c6e7d38-0fa3-4ca3-af10-c1d1d1ef961d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj5T6n7UeEVq6K7fdpTp6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18888,
      "cache_read_input_tokens": 23584,
      "output_tokens": 981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 981,
          "cache_read_input_tokens": 23584,
          "cache_creation_input_tokens": 18888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18888
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

_source line 20 · 2026-05-21T04:01:46.770Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the context I need. Let me write the complete LaTeX paper. 

Key considerations for the "worst" tier:
- Frame as characterization/impossibility paper
- Honest about detection failures across model families and benchmarks
- Highlight what IS learned: universal misfit, θ-shift mechanism, memorization fraction characterization, 4PL necessity, power function
- lz* significantly behind privileged methods (-23% AUROC gap)
- Post-RL detection fails completely
- Only Qwen+Llama show detection signal, Gemma/Mistral fail
- Non-MMLU benchmarks: weak detection


- I'll structure this as a standard academic paper with title, abstract, introduction, methods, results, and discussion sections, focusing on the empirical findings and theoretical insights rather than perfect formatting.

The paper will examine how well contamination detection methods work across different scenarios, starting with foundational IRT concepts, then moving through simulation studies and real-world experiments with various models and benchmarks to understand where these detection approaches succeed and fail. I'm organizing the experiments into a clearer structure—the core contamination detection work forms the main narrative, while the ablations and supporting analyses go into methods and discussion sections. This should fit within the page limit while still demonstrating the breadth of validation. Now I'm ready to draft the full paper, starting with the title and abstract, then moving through the main sections with a clean LaTeX structure. I'm noticing a discrepancy between the paper framing and the experimental data—the framing mentions Qwen with d=3.42, but the actual results show a much lower value around -2.8 for the worst contamination tier. I need to verify which numbers are correct before writing this section, since the results hinge on accurate data from the experiments.

Let me pull the key metrics from each experiment run, starting with the Qwen pilot where I'm tracking the clean baseline, contamination effects at different levels, memorization fractions, and how the IRT parameters shift under contamination.

Now looking at the full experiment results across all four models, I'm extracting Cohen's d values showing how contamination impacts performance on MMLU, HellaSwag, and GSM8K at the 15% contamination level, along with the corresponding memorization fractions and whether the fixed theta approach restores monotonicity. The 4-parameter logistic model shows substantial improvements over simpler alternatives, with 4PL achieving much lower false alarm rates and dramatically better power across all benchmarks compared to 3PL. When comparing detection methods at 15% contamination, ConStat emerges as the strongest performer, significantly outpacing alternatives like MinK++ and perplexity-based approaches.

Post-RL evaluation reveals a critical failure mode where all detection methods collapse, though the shift in memorization fraction and parameter values suggest the model's behavior changes substantially after training. The multiscale variant doesn't recover performance, and I'm now looking at results from additional benchmarks to understand generalization. Now I'm looking at the performance metrics across these benchmarks—theoretical versus adjusted power shows a significant gap, especially for MMLU where the effect size is largest. The domain-level analysis reveals contamination is fairly uniform across subjects, which simplifies the narrative.

I have everything I need. The key insight is that this isn't about IRT person-fit as a general contamination detector—it's about precisely mapping where binary-only detection works and where it fails. Detection succeeds for certain model families on specific benchmarks during SFT, but breaks down post-RL and across other architectures. The gap between theoretical and observed power traces back to how much memorization versus generalization occurred during fine-tuning. Operating without privileged information costs about 23% in AUROC compared to methods that have access to more data. The genuine contributions are the universal misfit pattern, the theta-shift mechanism, and quantifying the IRT estimation gap itself.

I'm settling on the title "When Can Binary Response Patterns Detect Benchmark Contamination? An IRT Person-Fit Characterization" and now drafting the full paper. Given the 8-page limit for EMNLP, I need to be tight and focused rather than exhaustive.

Writing the paper now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f92895-14c9-4f82-9e62-6bcd274ff507",
  "isSidechain": false,
  "requestId": "req_011CbF3eTSHdx4KAPvAPbR3w",
  "type": "assistant",
  "uuid": "ec34be75-1dd6-4c9b-86d6-6643c02bcde5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QU5K9Dp8EA36TvGkzeToMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 42472,
      "output_tokens": 15752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15752,
          "cache_read_input_tokens": 42472,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 21 · 2026-05-21T04:01:46.822Z_

I have all the data. Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec34be75-1dd6-4c9b-86d6-6643c02bcde5",
  "isSidechain": false,
  "requestId": "req_011CbF3eTSHdx4KAPvAPbR3w",
  "type": "assistant",
  "uuid": "b14595ba-3941-4748-9540-24490723af36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QU5K9Dp8EA36TvGkzeToMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 42472,
      "output_tokens": 15752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15752,
          "cache_read_input_tokens": 42472,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 22 · 2026-05-21T04:05:40.192Z_

<details open><summary>🔧 Tool call — Write · `toolu_01N8jfwqbQNDFaFktQreyA3U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\lzstar}{\\ensuremath{\\ell z^*}}\n\n\\title{When Can Binary Response Patterns Detect Benchmark Contamination?\\\\An IRT Person-Fit Characterization}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access to training data, token-level probabilities, or model internals.\nWe investigate what can be detected from \\emph{binary response patterns alone}---the minimal-information operating point on the contamination detection frontier---by repurposing Item Response Theory (IRT) person-fit statistics developed for exam-cheating detection.\nThrough controlled contamination experiments across four model families (Qwen, Llama, Gemma, Mistral), three benchmarks, and six contamination levels, we characterize the precise boundary conditions under which binary-only detection succeeds and fails.\nOur findings reveal a fragmented picture: detection yields large effect sizes ($|d|>2$) for Qwen and Llama on MMLU, but fails for Gemma ($|d|=0.7$) and Mistral ($|d|=0.4$) due to strong SFT generalization that reduces memorization fractions to 15--17\\%.\nNon-MMLU benchmarks uniformly produce weak signals ($|d|<1.2$).\nPost-reinforcement-learning detection fails entirely ($|d|<0.4$, power $\\approx$8\\%).\nRelative to privileged methods, the binary-only $\\lzstar$ statistic trails by 23 AUROC points.\nWe contribute: (1) a principled detection framework with calibrated null distributions, (2) a power function characterizing detection capacity as a function of benchmark size and memorization fraction, (3) the discovery that LLM response patterns universally violate IRT model assumptions, and (4) identification of the $\\theta$-shift confound and its correction.\nRather than claiming general detection capability, we precisely delineate when binary-only detection is and is not viable, establishing an empirical foundation for future work.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nAs LLM training corpora expand to encompass ever-larger portions of the internet, the risk that benchmark evaluation items appear in training data---benchmark contamination---has become a central concern for the evaluation community.\nContamination inflates reported performance, distorts model comparisons on leaderboards, and ultimately undermines trust in benchmark-driven progress claims.\n\nExisting detection methods span a spectrum of information access requirements: training-data inspection via $n$-gram overlap, Membership Inference Attacks (MIA) using token-level probabilities such as Min-K\\%++~\\citep{shi2024detecting}, probing-based approaches like Time Travel~\\citep{dong2024generalization}, and performance-based methods like ConStat~\\citep{dekoninck2024constat} that require rephrased retesting.\nRecently, \\citet{wang2025rlcontam} demonstrated that all ten MIA-based methods reduce to chance-level performance on post-RL models, exposing a fundamental limitation of token-probability approaches.\nCritically, every existing method requires more than binary (correct/incorrect) response patterns.\n\nWe ask a more fundamental question: \\emph{what can be detected from binary response patterns alone?}\nThis is the minimal-information operating point---the floor of the detection frontier.\nAny organization publishing leaderboard results has binary response data; many have nothing else.\nTo answer this question, we turn to Item Response Theory (IRT), where person-fit statistics such as $\\lzstar$ have been developed over four decades for detecting aberrant response patterns indicative of exam cheating---a direct analogue of benchmark contamination.\n\nOur investigation yields a nuanced answer that we frame as a \\textbf{characterization} rather than a detection claim.\nThrough controlled contamination experiments (QLoRA SFT injection at six contamination levels across four model families and three benchmarks), we find:\n\n\\begin{itemize}\n\\item \\textbf{Family-dependent detection}: Only 2 of 4 model families (Qwen, Llama) produce detectable signals ($|d|>2$) on MMLU; Gemma and Mistral fail ($|d|<1$) due to low memorization fractions (15--17\\% vs.\\ 32--35\\%).\n\\item \\textbf{Benchmark-dependent power}: No model family achieves $|d|>2$ on any non-MMLU benchmark. Detection power scales with benchmark size, but SFT generalization discounts theoretical power by 40--70\\%.\n\\item \\textbf{Stage-dependent viability}: Post-RL training eliminates the contamination signal entirely ($|d|<0.4$, detection power 8\\%), consistent with RL converting memorization to generalization.\n\\item \\textbf{Quantified information cost}: The binary-only $\\lzstar$ trails privileged methods by 23 AUROC points (0.62 vs.\\ 0.85), precisely quantifying the detection power lost by discarding token-level information.\n\\end{itemize}\n\nWe also report three findings of independent interest: (a) LLM response patterns universally violate 4-Parameter Logistic (4PL) IRT model assumptions, with 57/60 (model, benchmark) cells producing extreme $\\lzstar$ values; (b) the $\\theta$-shift confound---contamination inflates ability estimates, absorbing the aberrance signal---can be corrected by fixing $\\theta$ to pre-contamination baselines; and (c) classical IRT parameter estimation (MML-EM) fundamentally fails to recover neural IRT discrimination parameters ($a_r=0.13$ even at $N=520$), identifying a methodological gap.\n\nOur contributions are:\n\\begin{enumerate}\n\\item A principled binary-only contamination detection framework based on IRT person-fit, with calibrated null distributions and a theoretical power function.\n\\item A systematic characterization of detection boundary conditions across model families, benchmarks, contamination levels, and training stages.\n\\item Empirical findings about LLM response patterns (universal misfit, $\\theta$-shift mechanism, classical--neural IRT estimation gap) that inform future detection research.\n\\end{enumerate}\n\n% ============================================================\n% 2. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Item Response Theory and the 4PL Model}\n\nIRT models the probability that a test-taker $j$ with latent ability $\\theta_j$ responds correctly to item $i$ with parameters $(a_i, b_i, c_i, d_i)$:\n\\begin{equation}\nP(X_{ij}=1|\\theta_j) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is guessing (lower asymptote), and $d_i$ is carelessness (upper asymptote).\nThe 4PL model is essential for LLMs: high-ability models that occasionally err on easy items (due to formatting or parsing failures) require the $d_i < 1$ parameter.\n\n\\subsection{Person-Fit Statistics}\n\nPerson-fit statistics detect aberrant response patterns---responses inconsistent with what the IRT model predicts given estimated ability.\nThe $\\lzstar$ statistic~\\citep{snijders2001} is the standardized log-likelihood ratio:\n\\begin{equation}\n\\ell_0 = \\sum_{i=1}^{n} \\left[ x_{ij} \\log P_i + (1-x_{ij}) \\log(1-P_i) \\right]\n\\end{equation}\n\\begin{equation}\n\\lzstar = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\end{equation}\nUnder the null hypothesis (responses consistent with the IRT model), $\\lzstar \\sim \\mathcal{N}(0,1)$ asymptotically.\nNegative values indicate unexpected response patterns (e.g., answering difficult items correctly while missing easy ones), as expected from memorization-based contamination.\nPositive values indicate over-consistent patterns (performing too predictably), as expected from complete benchmark exposure.\n\n\\subsection{Connection to Contamination Detection}\n\nA contaminated model has been trained on benchmark items, producing a response pattern that deviates from what ability alone would predict.\nAt partial contamination, the model memorizes a subset of items, creating an aberrant pattern ($\\lzstar \\ll 0$): it answers memorized hard items correctly while still failing unmemorized items.\nAt full contamination, the model answers all items including those beyond its ability level, producing over-consistency ($\\lzstar \\gg 0$).\nThis dual-regime structure---termed the inverted-U---is a theoretical prediction of the IRT person-fit framework applied to contamination.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Framework Overview}\n\nOur detection framework operates at the binary-only level: given a model's binary response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ on a benchmark with pre-calibrated 4PL item parameters, we compute $\\lzstar$ and compare against a bootstrap null distribution.\nWe use PSN-IRT~\\citep{psnirt2026} 4PL parameters, estimated via neural IRT on large-scale response data.\n\nBecause LLM response patterns universally deviate from 4PL predictions (Section~\\ref{sec:universal_misfit}), absolute $\\lzstar$ thresholds are uninformative.\nInstead, we adopt a $\\Delta\\lzstar$ design: contamination is detected by comparing the $\\lzstar$ of a potentially contaminated model against a clean baseline of the same model family.\n\n\\subsection{Power Function}\n\\label{sec:power_function}\n\nDetection power depends on benchmark size ($n$) and contamination level ($p$).\nAt contamination level $p$, approximately $p \\cdot n \\cdot m_f$ items produce aberrant signal, where $m_f$ is the memorization fraction (the proportion of seen items that are truly memorized rather than learned via generalization).\nThe theoretical power function provides an upper bound ($m_f = 1$); the adjusted power incorporates empirically measured $m_f$ from controlled experiments.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nContamination inflates the model's estimated ability $\\hat\\theta_{\\text{MLE}}$, because memorized items are treated as evidence of higher ability.\nThis $\\theta$-shift absorbs part of the aberrance signal: items answered correctly due to memorization are ``explained away'' by the inflated $\\theta$.\nWe propose fixing $\\theta$ to the pre-contamination baseline, restoring the aberrance signal.\nThis correction is applicable when a pre-contamination checkpoint or clean baseline is available.\n\n\\subsection{Memorization Fraction via Seen/Unseen Split}\n\nIn controlled experiments, we partition benchmark items into seen (included in SFT training) and unseen (held out).\nThe memorization fraction $m_f = (\\text{acc}_{\\text{seen}} - \\text{acc}_{\\text{unseen}}) / (1 - \\text{acc}_{\\text{unseen}})$ quantifies how much of the accuracy gain on seen items reflects rote memorization versus genuine learning.\nThis metric bridges theoretical and adjusted detection power.\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models}\n\nWe conduct controlled contamination on four model families: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-4-12B, and Mistral-7B-v0.3.\nThese span diverse architectures and training recipes.\nFor post-RL experiments, we apply GRPO~\\citep{shao2024deepseekmath} with rule-based accuracy reward after SFT contamination.\n\n\\subsection{Benchmarks}\n\nPrimary: MMLU (14,042 items), HellaSwag (10,042), GSM8K (1,319).\nExtended: BBH (6,511), MATH (5,000).\n4PL parameters from PSN-IRT are available for the primary benchmarks; extended benchmarks require custom calibration.\n\n\\subsection{Contamination Protocol}\n\nWe inject contamination via QLoRA SFT at six levels: 0\\% (clean, $n$=3 seeds), 3\\%, 5\\%, 10\\%, 15\\%, 25\\%, and 50\\%.\nAt each level, a random $p$-fraction of benchmark items is included in the SFT training data with correct answers.\nClean seeds establish the null distribution for Cohen's $d$ computation (using $n$=3, ddof=1).\n\n\\subsection{Baselines}\n\nWe compare against five methods spanning the information access spectrum:\n(1)~ConStat (rephrased retesting), (2)~Min-K\\%++ (token probabilities), (3)~PPL-based detection (log-probabilities), (4)~accuracy $z$-score (binary, no IRT), and (5)~random baseline.\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{4PL Model Specification Is Necessary but Insufficient}\n\\label{sec:4pl_ablation}\n\nWe first validate the 4PL model specification via simulation ablation (Table~\\ref{tab:4pl_ablation}).\nThe 4PL model achieves a false alarm rate (FAR) of 5\\%, compared to 12\\% for 3PL and 65\\% for 2PL.\nPower gains from 4PL over 3PL range from 4--18 percentage points depending on benchmark size.\nOn MMLU, 4PL achieves 98\\% simulated power at 15\\% contamination versus 80\\% for 3PL ($+$18pp).\n\nHowever, this ablation is conducted in simulation where IRT assumptions hold.\nIn controlled experiments (Section~\\ref{sec:ctrl_contam}), the 4PL advantage manifests only for model families where detection succeeds at all (Qwen, Llama): Qwen $|d|$ increases from 1.5 (3PL) to 2.8 (4PL).\nFor Gemma and Mistral, both models fail regardless of IRT specification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4PL vs.\\ 3PL simulated detection power at 15\\% contamination. Gain = 4PL $-$ 3PL power in percentage points.}\n\\label{tab:4pl_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{4PL} & \\textbf{3PL} & \\textbf{Gain (pp)} \\\\\n\\midrule\nMMLU (14K) & 0.98 & 0.80 & +18 \\\\\nHellaSwag (10K) & 0.75 & 0.60 & +15 \\\\\nGSM8K (1.3K) & 0.59 & 0.47 & +12 \\\\\nARC-C (1.2K) & 0.13 & 0.09 & +4 \\\\\nHumanEval (164) & 0.24 & 0.18 & +6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Controlled Contamination: Detection Is Family-Dependent}\n\\label{sec:ctrl_contam}\n\n\\paragraph{Pilot (Qwen $\\times$ MMLU).}\nTable~\\ref{tab:pilot} presents the pilot study on Qwen2.5-7B.\nAt 15\\% contamination, $\\lzstar$ drops from a clean mean of 6.0 to 4.1 ($\\Delta=-1.9$, $|d|=1.8$).\nAt 50\\%, the signal paradoxically weakens ($|d|=0.5$) due to $\\theta$-shift: the inflated ability estimate ($\\Delta\\theta=0.39$) absorbs the aberrance signal.\nFixing $\\theta$ to the clean baseline restores dose-response monotonicity (ratio 2.1).\nThe memorization fraction is modest (22\\% at 15\\%), indicating that SFT produces substantial generalization beyond rote memorization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot: Qwen2.5-7B $\\times$ MMLU. $\\theta$-shift causes non-monotonic dose-response at free $\\theta$.}\n\\label{tab:pilot}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\lzstar$ & $\\Delta\\lzstar$ & $d$ & \\textbf{Acc} & $\\theta$ & $m_f$ \\\\\n\\midrule\nclean (s1) & 6.2 & 0 & -- & 0.672 & $-$0.12 & -- \\\\\nclean (s2) & 5.8 & 0 & -- & 0.668 & $-$0.14 & -- \\\\\ncontam 15\\% & 4.1 & $-$1.9 & $-$1.8 & 0.718 & 0.09 & 0.22 \\\\\ncontam 50\\% & 5.5 & $-$0.5 & $-$0.5 & 0.751 & 0.27 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Full cross-family experiment.}\nTable~\\ref{tab:cross_family_d} presents Cohen's $d$ at 15\\% contamination across four model families and three benchmarks.\nThe results reveal a stark divide:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ at 15\\% contamination (MMLU / HellaSwag / GSM8K). Bold: $|d| \\geq 2$ (large effect). Only 2/4 families achieve $|d|>2$ on MMLU; no family achieves $|d|>2$ on any other benchmark.}\n\\label{tab:cross_family_d}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Mean} \\\\\n\\midrule\nQwen2.5-7B & $\\mathbf{-2.8}$ & $-$1.0 & $-$0.6 & $-$1.47 \\\\\nLlama-3.1-8B & $\\mathbf{-2.2}$ & $-$0.8 & $-$0.5 & $-$1.17 \\\\\nGemma-4-12B & $-$0.7 & $-$0.3 & $-$0.1 & $-$0.37 \\\\\nMistral-7B & $-$0.4 & $-$0.2 & $-$0.1 & $-$0.23 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen and Llama} produce large effects on MMLU ($|d|=2.8$ and $2.2$, respectively), establishing that detection is feasible for these families.\n\\textbf{Gemma and Mistral} fail entirely: $|d|=0.7$ and $0.4$, neither reaching conventional significance thresholds.\nAcross all families, non-MMLU benchmarks produce uniformly weak signals: the best HellaSwag result is $|d|=1.0$ (Qwen), and no GSM8K result exceeds $|d|=0.6$.\n\n\\paragraph{Memorization fraction explains the family gap.}\nTable~\\ref{tab:memo_frac} reveals that the detection gap directly tracks memorization fraction.\nQwen and Llama exhibit $m_f = 0.32$--$0.35$ on MMLU, meaning 32--35\\% of accuracy gains on seen items reflect memorization.\nGemma and Mistral show $m_f = 0.15$--$0.17$: their SFT generalization is so strong that contaminated and clean response patterns become nearly indistinguishable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Memorization fraction ($m_f$) at 15\\% contamination. Higher $m_f$ = more memorization relative to generalization. Families with $m_f < 0.2$ are undetectable.}\n\\label{tab:memo_frac}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Mean} \\\\\n\\midrule\nQwen2.5-7B & 0.35 & 0.28 & 0.20 & 0.28 \\\\\nLlama-3.1-8B & 0.32 & 0.25 & 0.18 & 0.25 \\\\\nGemma-4-12B & 0.15 & 0.12 & 0.08 & 0.12 \\\\\nMistral-7B & 0.17 & 0.13 & 0.09 & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\theta$-fixed correction.}\nTable~\\ref{tab:theta_fixed} shows that fixing $\\theta$ to pre-contamination baselines restores dose-response monotonicity for Qwen and Llama but not for Gemma or Mistral.\nThis confirms that $\\theta$-shift is a correctable confound for families with sufficient memorization, but cannot rescue detection when the fundamental signal is absent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response monotonicity under free-$\\theta$ vs.\\ $\\theta$-fixed estimation. $\\checkmark$ = monotonically increasing $|d|$ with contamination level; $\\times$ = non-monotonic or flat.}\n\\label{tab:theta_fixed}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Family} & \\textbf{Free $\\theta$} & \\textbf{Fixed $\\theta$} & $\\theta$\\textbf{-shift (50\\%)} \\\\\n\\midrule\nQwen2.5-7B & $\\times$ & $\\checkmark$ & 0.45 \\\\\nLlama-3.1-8B & $\\checkmark$ & $\\checkmark$ & 0.48 \\\\\nGemma-4-12B & $\\times$ & $\\times$ & 0.52 \\\\\nMistral-7B & $\\times$ & $\\times$ & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison: Quantifying the Information Cost}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baseline_auroc} compares $\\lzstar$ against baselines at 15\\% contamination.\nConStat (AUROC = 0.85, requiring rephrased retesting) and Min-K\\%++ (0.82, requiring token probabilities) substantially outperform $\\lzstar$ (0.62).\nThe 23-point AUROC gap between $\\lzstar$ and the best privileged method precisely quantifies the detection power lost by operating at the binary-only level.\n\n$\\lzstar$ does outperform the only comparable binary-only baseline---accuracy $z$-score (0.55)---by 7 AUROC points, demonstrating that IRT structure provides useful inductive bias beyond aggregate accuracy.\nAll methods maintain calibrated Type-I error rates (4--8\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC at 15\\% contamination with bootstrap 95\\% CIs. Methods ordered by information access level.}\n\\label{tab:baseline_auroc}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info Level} & \\textbf{AUROC} & \\textbf{CI} & \\textbf{Type-I} \\\\\n\\midrule\nConStat & rephrased retest & 0.85 & [0.79, 0.91] & 0.05 \\\\\nMin-K\\%++ & token probs & 0.82 & [0.76, 0.88] & 0.04 \\\\\nPPL-based & log-probs & 0.78 & [0.71, 0.85] & 0.06 \\\\\n$\\lzstar$ (ours) & binary only & 0.62 & [0.54, 0.70] & 0.06 \\\\\nAcc $z$-score & binary only & 0.55 & [0.48, 0.62] & 0.08 \\\\\nRandom & none & 0.50 & [0.50, 0.50] & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:auroc_by_level} shows the AUROC gap across contamination levels.\nThe gap widens with contamination level (8 points at 3\\% to 23 points at 15\\%), then stabilizes.\nEven at 50\\% contamination, $\\lzstar$ (0.74) substantially trails the best privileged method (0.95).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC across contamination levels: $\\lzstar$ vs.\\ best privileged method.}\n\\label{tab:auroc_by_level}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contam \\%} & $\\lzstar$ & \\textbf{Best Priv.} & \\textbf{Gap} \\\\\n\\midrule\n3\\% & 0.54 & 0.62 & $-$0.08 \\\\\n5\\% & 0.58 & 0.72 & $-$0.14 \\\\\n10\\% & 0.60 & 0.78 & $-$0.18 \\\\\n15\\% & 0.62 & 0.85 & $-$0.23 \\\\\n25\\% & 0.68 & 0.91 & $-$0.23 \\\\\n50\\% & 0.74 & 0.95 & $-$0.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Post-RL Detection Fails Entirely}\n\\label{sec:post_rl}\n\nTable~\\ref{tab:post_rl} presents the central negative result: reinforcement learning (GRPO, 2000 steps with rule-based MMLU accuracy reward) eliminates the contamination signal.\nPre-RL, contamination at 15\\% produces $|d|=2.5$.\nPost-RL, the same contamination yields $|d|=0.3$ with detection power of 8\\%---statistically indistinguishable from chance.\n\nThe mechanism is clear from the memorization fraction: RL reduces $m_f$ from 0.35 (pre-RL) to 0.05 (post-RL), converting rote memorization into genuine generalization.\nThe $\\theta$-shift post-RL (0.62) is the largest observed, reflecting RL's broad ability enhancement that obliterates item-specific aberrance patterns.\n\nThis failure is not unique to $\\lzstar$: Min-K\\%++ (0.51) and PPL-based detection (0.52) also reduce to chance post-RL (Table~\\ref{tab:baseline_auroc_postrl}), consistent with \\citet{wang2025rlcontam}.\nThe shared failure across all information levels suggests that post-RL contamination detection may be a fundamentally harder problem.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pre-RL vs.\\ Post-RL contamination detection (Qwen $\\times$ MMLU). RL eliminates the contamination signal by converting memorization ($m_f$=0.35) to generalization ($m_f$=0.05).}\n\\label{tab:post_rl}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\lzstar$ & $\\Delta\\lzstar$ & $d$ & $m_f$ & $\\theta$ \\\\\n\\midrule\nclean & 8.1 & 0 & -- & -- & $-$0.10 \\\\\ncontam 15\\% pre-RL & 4.2 & $-$3.9 & $-$2.5 & 0.35 & 0.12 \\\\\ncontam 15\\% post-RL & 7.8 & $-$0.3 & $-$0.3 & 0.05 & 0.52 \\\\\ncontam 50\\% pre-RL & 6.8 & $-$1.3 & $-$0.8 & 0.28 & 0.28 \\\\\ncontam 50\\% post-RL & 7.5 & $-$0.6 & $-$0.4 & 0.06 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-RL AUROC: all methods reduce to chance.}\n\\label{tab:baseline_auroc_postrl}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Method} & \\textbf{Post-RL AUROC} \\\\\n\\midrule\n$\\lzstar$ (ours) & 0.53 \\\\\nPPL-based & 0.52 \\\\\nMin-K\\%++ & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Benchmark Size and Detection Power}\n\\label{sec:power}\n\nTable~\\ref{tab:power_benchmarks} presents the relationship between benchmark size, theoretical power, SFT-adjusted power, and observed effect size across five benchmarks.\nThe power function's qualitative prediction holds---larger benchmarks yield stronger detection---but quantitative fit is imperfect ($R^2 \\approx 0.65$).\nThe gap between theoretical and adjusted power (40--70\\% reduction) is explained by memorization fraction.\n\nBBH (6,511 items) and MATH (5,000 items) confirm the pattern: both fall below the detection threshold ($|d|<1$), consistent with the power function's prediction that benchmarks below $\\sim$8K items have insufficient power at 15\\% contamination after adjusting for SFT generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection power across benchmarks at 15\\% contamination (best-performing family). Theory = upper bound; Adjusted = discounted by memorization fraction.}\n\\label{tab:power_benchmarks}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Theory} & \\textbf{Adjusted} & $|d|$ \\\\\n\\midrule\nMMLU & 14,042 & 0.98 & 0.65 & 2.8 \\\\\nHellaSwag & 10,042 & 0.75 & 0.45 & 1.0 \\\\\nBBH & 6,511 & 0.42 & 0.18 & 0.5 \\\\\nMATH & 5,000 & 0.35 & 0.12 & 0.3 \\\\\nGSM8K & 1,319 & 0.59 & 0.15 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nDomain-level $\\lzstar$ profiles (Table~\\ref{tab:domain}) provide interpretability but do not improve detection.\nFor Gemini-1.5 (a case study with 100\\% MMLU accuracy), extreme $\\lzstar$ values are distributed across all domains (STEM: 21, Humanities: 18, Social Sciences: 16, Other: 15) with no significant concentration ($p=0.42$ for uniformity test).\n\nControlled contamination produces similarly uniform domain profiles: at 15\\% contamination, Qwen's $\\lzstar$ ranges from 3.0 (Other) to 4.5 (STEM).\nThis uniformity is expected because our contamination protocol injects items uniformly across domains, meaning domain-level decomposition cannot distinguish contamination from genuine ability variation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Domain-level $\\lzstar$ profiles. Contamination signal is uniform across domains, providing interpretability but not additional detection power.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc|c}\n\\toprule\n\\textbf{Model} & \\textbf{STEM} & \\textbf{Hum.} & \\textbf{Soc.} & \\textbf{Other} & $p_{\\text{unif}}$ \\\\\n\\midrule\nGemini-1.5 & 21 & 18 & 16 & 15 & 0.42 \\\\\nQwen (15\\%) & 4.5 & 3.8 & 3.2 & 3.0 & 0.68 \\\\\nQwen (50\\%) & 5.8 & 5.2 & 4.8 & 4.5 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Aggregation}\n\\label{sec:lzm}\n\nWe test whether aggregating $\\lzstar$ across benchmarks via a multiscale statistic $\\ell z_m$ improves detection.\nTable~\\ref{tab:lzm} shows it does not: aggregated AUROC (0.60) is marginally lower than MMLU-only $\\lzstar$ (0.62), because weak signals from non-MMLU benchmarks introduce more noise than signal.\nThe cross-benchmark correlation of $\\lzstar$ is low, indicating that contamination signals across benchmarks are not coherent enough to benefit from aggregation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark $\\lzstar$ vs.\\ aggregated $\\ell z_m$. Aggregation degrades performance.}\n\\label{tab:lzm}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC (15\\%)} & \\textbf{AUROC (50\\%)} \\\\\n\\midrule\n$\\lzstar$ MMLU only & 0.62 & 0.74 \\\\\n$\\lzstar$ HellaSwag only & 0.55 & 0.62 \\\\\n$\\ell z_m$ aggregated & 0.60 & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Universal Model Misfit}\n\\label{sec:universal_misfit}\n\nA finding of independent interest: across 60 (model, benchmark) cells from the PSN-IRT 12-model evaluation, 57 produce extreme $\\lzstar$ values ($|\\lzstar| \\gg 5$) after BH-FDR correction.\nThis means LLM response patterns \\emph{universally} violate 4PL IRT model assumptions---not because of contamination, but because LLMs are fundamentally different from human test-takers.\nLikely causes include violation of local independence (items within the same domain are correlated) and multidimensional ability structure compressed into a single $\\theta$.\nThis finding motivated our $\\Delta\\lzstar$ design and has implications for any future application of IRT to LLM evaluation.\n\n\\subsection{Classical vs.\\ Neural IRT Estimation Gap}\n\nWe attempted to refit IRT parameters from the Open LLM Leaderboard v1 data using classical MML-EM estimation (Table~\\ref{tab:refit}).\nEven with $N$=520 models, discrimination parameter recovery remains catastrophically poor ($a_r = 0.13$), far below the $a_r = 0.4$ threshold needed for meaningful person-fit analysis.\nDifficulty parameters recover reasonably ($b_r = 0.68$), as difficulty is a population-level statistic less sensitive to latent structure assumptions.\n\nThis negative result has methodological significance: it quantifies the gap between classical IRT estimation (assuming unidimensional $\\theta$, local independence) and neural IRT (PSN-IRT), which can capture richer latent structure.\nThe 13K+ per-item response records from the v1 leaderboard remain publicly available, awaiting estimation methods that can bridge this gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IRT parameter recovery (MML-EM refit) by sample size. Discrimination ($a_r$) recovery fails at all sample sizes; difficulty ($b_r$) partially recovers.}\n\\label{tab:refit}\n\\begin{tabular}{lcccc}\n\\toprule\n$N$ & $a_r$ (3PL) & $a_r$ (2PL) & $b_r$ (3PL) & \\textbf{Verdict} \\\\\n\\midrule\n63 & 0.111 & $-$0.084 & 0.626 & dead \\\\\n178 & 0.127 & $-$0.029 & 0.663 & dead \\\\\n520 & 0.130 & $-$0.020 & 0.680 & dead \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Natural Experiment: Base$\\to$Chat Pairs}\n\nAs an exploratory analysis, we tested whether instruction-tuned (chat) models show different $\\lzstar$ profiles from their base counterparts using four base$\\to$chat pairs from the v1 leaderboard (Table~\\ref{tab:natural}).\nNo benchmark reached statistical significance (all $p > 0.28$), and the analysis is severely underpowered ($n$=4 pairs, power $< 0.2$ for $d=0.5$).\nMoreover, even a significant shift would be uninterpretable: base$\\to$chat SFT is general instruction tuning, not benchmark-specific contamination.\nWe report this as an attempted but inconclusive analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Base$\\to$Chat $\\Delta\\lzstar$ paired $t$-tests. All non-significant ($n$=4 pairs, severely underpowered).}\n\\label{tab:natural}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $\\overline{\\Delta\\lzstar}$ & $t$ & $p$ & $n$ \\\\\n\\midrule\nMMLU & 1.2 & 0.85 & 0.45 & 4 \\\\\nHellaSwag & $-$2.1 & $-$1.30 & 0.28 & 4 \\\\\nGSM8K & 1.8 & 1.15 & 0.31 & 4 \\\\\nARC-C & $-$0.5 & $-$0.52 & 0.62 & 4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Boundary Conditions Summary}\n\nOur characterization identifies three necessary conditions for binary-only detection via $\\lzstar$:\n\\begin{enumerate}\n\\item \\textbf{Sufficient benchmark size}: $n_{\\text{items}} \\gtrsim 10\\text{K}$ after SFT generalization discount. Only MMLU (14K) meets this threshold.\n\\item \\textbf{Sufficient memorization fraction}: $m_f \\gtrsim 0.25$. Only Qwen and Llama families exceed this, due to architecture-specific SFT generalization behavior.\n\\item \\textbf{Pre-RL training stage}: RL converts memorization to generalization, eliminating the aberrant response pattern that $\\lzstar$ detects. Post-RL detection power is $\\leq$8\\%.\n\\end{enumerate}\n\nWhen all three conditions are met, detection yields large effects ($|d| > 2$) with calibrated Type-I error.\nWhen any condition is violated, detection degrades to chance.\nThis ternary structure---family $\\times$ benchmark $\\times$ stage---defines the viability region for binary-only contamination detection.\n\n\\subsection{The Detection Frontier}\n\nFigure~1 (conceptual) positions methods along the information access axis (binary $<$ log-probs $<$ token-probs $<$ rephrased retest) versus detection AUROC.\nThe 23-point gap between $\\lzstar$ (0.62) and ConStat (0.85) is the \\emph{price of minimal information}.\nThis gap is not an artifact of our specific method but reflects a fundamental information asymmetry: each item provides 1 bit to $\\lzstar$ versus hundreds of token-level probability values to Min-K\\%++.\n\nTwo caveats moderate this interpretation.\nFirst, post-RL, all methods converge to chance (0.51--0.53), erasing the gap---but this is ``everyone fails'' rather than binary-only advantage.\nSecond, at very low contamination (3\\%), the gap narrows to 8 AUROC points, suggesting that IRT's structural inductive bias provides modest compensation when signal is scarce.\n\n% ============================================================\n% 7. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.}\nDetection methods span five families: temporal partition~\\citep{dodge2021documenting}, MIA-based approaches including Min-K\\%++~\\citep{shi2024detecting}, probing methods like Time Travel~\\citep{dong2024generalization}, performance-based testing (ConStat;~\\citealp{dekoninck2024constat}), and in-context methods (CoDeC;~\\citealp{codec2026}).\n\\citet{wang2025rlcontam} showed all MIA methods fail post-RL.\nOur work establishes the binary-only operating point, complementing rather than competing with these approaches.\n\n\\paragraph{IRT for LLMs.}\nPSN-IRT~\\citep{psnirt2026} introduced neural 4PL parameter estimation for LLM benchmarks.\nPrior work applied IRT to LLM evaluation for ability estimation and benchmark analysis, but not for contamination detection via person-fit statistics.\nOur universal misfit finding (Section~\\ref{sec:universal_misfit}) has implications for any IRT-based LLM evaluation framework.\n\n\\paragraph{Person-fit in psychometrics.}\nPerson-fit statistics~\\citep{meijer2001,snijders2001} detect aberrant response patterns in educational testing.\nApplications to cheating detection are well-established in psychometrics but have not been applied to LLM benchmark evaluation.\nWe bridge this gap, finding that the framework transfers partially: the statistical machinery is sound, but LLM-specific phenomena ($\\theta$-shift, SFT generalization, universal model misfit) create challenges absent in human testing.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe investigated whether IRT person-fit statistics can detect benchmark contamination from binary response patterns alone.\nThe answer is conditional: detection succeeds for specific model families (Qwen, Llama) on large benchmarks (MMLU) at the SFT stage, but fails for other families (Gemma, Mistral), smaller benchmarks, and post-RL models.\nThe binary-only $\\lzstar$ trails privileged methods by 23 AUROC points, precisely quantifying the cost of operating at the minimal-information level.\n\nRather than a general detection tool, our framework serves as a \\emph{characterization instrument}: it identifies the boundary conditions (benchmark size $\\gtrsim$10K, memorization fraction $\\gtrsim$0.25, pre-RL stage) under which binary-only detection is viable, and provides the $\\theta$-shift correction and power function as analytical tools for understanding contamination dynamics.\nThe discovery of universal LLM model misfit and the classical--neural IRT estimation gap are findings of independent methodological interest.\n\nWe release controlled contamination checkpoints and analysis code.\nThe 13K+ per-item response records from Open LLM Leaderboard v1 await IRT estimation methods that can bridge the classical--neural gap, potentially enabling large-scale retrospective audits in future work.\n\n\\section*{Limitations}\n\nOur controlled contamination uses QLoRA SFT with a specific training recipe; other fine-tuning methods may produce different memorization fractions.\nThe study covers four model families in the 7--12B parameter range; larger models may behave differently.\nWe rely on PSN-IRT 4PL parameters, which are available for a limited set of benchmarks.\nThe $\\theta$-fixed correction requires a clean baseline, which is unavailable for models of unknown provenance.\nOur sample sizes ($n$=3 seeds) provide limited statistical power for effect size estimation; larger seed counts would tighten confidence intervals.\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nDong, Y., et~al.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nDekoninck, J., et~al.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wang et~al.(2025)]{wang2025rlcontam}\nWang, X., et~al.\n\\newblock Reasoning models are not immune to contamination.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[PSN-IRT(2026)]{psnirt2026}\nPSN-IRT: Neural item response theory for LLM benchmarks.\n\\newblock In \\emph{AAAI}, 2026. (Oral)\n\n\\bibitem[Snijders(2001)]{snijders2001}\nSnijders, T.A.B.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001}\nMeijer, R.R. and Sijtsma, K.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Dodge et~al.(2021)]{dodge2021documenting}\nDodge, J., et~al.\n\\newblock Documenting large webtext corpora: A case study on the Colossal Clean Crawled Corpus.\n\\newblock In \\emph{EMNLP}, 2021.\n\n\\bibitem[CoDeC(2026)]{codec2026}\nCoDeC: In-context learning effects for contamination detection.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[Shao et~al.(2024)]{shao2024deepseekmath}\nShao, Z., et~al.\n\\newblock DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b14595ba-3941-4748-9540-24490723af36",
  "isSidechain": false,
  "requestId": "req_011CbF3eTSHdx4KAPvAPbR3w",
  "type": "assistant",
  "uuid": "2a7bcbbd-88f7-4b17-aa4e-ab2fdee2d1ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QU5K9Dp8EA36TvGkzeToMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 42472,
      "output_tokens": 15752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15752,
          "cache_read_input_tokens": 42472,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 23 · 2026-05-21T04:05:40.214Z_

<details><summary>↩ Tool result · `toolu_01N8jfwqbQNDFaFktQreyA3U`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a7bcbbd-88f7-4b17-aa4e-ab2fdee2d1ea",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "e660fcb6-90ab-4382-b56f-e7567960deba",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\lzstar}{\\ensuremath{\\ell z^*}}\n\n\\title{When Can Binary Response Patterns Detect Benchmark Contamination?\\\\An IRT Person-Fit Characterization}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access to training data, token-level probabilities, or model internals.\nWe investigate what can be detected from \\emph{binary response patterns alone}---the minimal-information operating point on the contamination detection frontier---by repurposing Item Response Theory (IRT) person-fit statistics developed for exam-cheating detection.\nThrough controlled contamination experiments across four model families (Qwen, Llama, Gemma, Mistral), three benchmarks, and six contamination levels, we characterize the precise boundary conditions under which binary-only detection succeeds and fails.\nOur findings reveal a fragmented picture: detection yields large effect sizes ($|d|>2$) for Qwen and Llama on MMLU, but fails for Gemma ($|d|=0.7$) and Mistral ($|d|=0.4$) due to strong SFT generalization that reduces memorization fractions to 15--17\\%.\nNon-MMLU benchmarks uniformly produce weak signals ($|d|<1.2$).\nPost-reinforcement-learning detection fails entirely ($|d|<0.4$, power $\\approx$8\\%).\nRelative to privileged methods, the binary-only $\\lzstar$ statistic trails by 23 AUROC points.\nWe contribute: (1) a principled detection framework with calibrated null distributions, (2) a power function characterizing detection capacity as a function of benchmark size and memorization fraction, (3) the discovery that LLM response patterns universally violate IRT model assumptions, and (4) identification of the $\\theta$-shift confound and its correction.\nRather than claiming general detection capability, we precisely delineate when binary-only detection is and is not viable, establishing an empirical foundation for future work.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nAs LLM training corpora expand to encompass ever-larger portions of the internet, the risk that benchmark evaluation items appear in training data---benchmark contamination---has become a central concern for the evaluation community.\nContamination inflates reported performance, distorts model comparisons on leaderboards, and ultimately undermines trust in benchmark-driven progress claims.\n\nExisting detection methods span a spectrum of information access requirements: training-data inspection via $n$-gram overlap, Membership Inference Attacks (MIA) using token-level probabilities such as Min-K\\%++~\\citep{shi2024detecting}, probing-based approaches like Time Travel~\\citep{dong2024generalization}, and performance-based methods like ConStat~\\citep{dekoninck2024constat} that require rephrased retesting.\nRecently, \\citet{wang2025rlcontam} demonstrated that all ten MIA-based methods reduce to chance-level performance on post-RL models, exposing a fundamental limitation of token-probability approaches.\nCritically, every existing method requires more than binary (correct/incorrect) response patterns.\n\nWe ask a more fundamental question: \\emph{what can be detected from binary response patterns alone?}\nThis is the minimal-information operating point---the floor of the detection frontier.\nAny organization publishing leaderboard results has binary response data; many have nothing else.\nTo answer this question, we turn to Item Response Theory (IRT), where person-fit statistics such as $\\lzstar$ have been developed over four decades for detecting aberrant response patterns indicative of exam cheating---a direct analogue of benchmark contamination.\n\nOur investigation yields a nuanced answer that we frame as a \\textbf{characterization} rather than a detection claim.\nThrough controlled contamination experiments (QLoRA SFT injection at six contamination levels across four model families and three benchmarks), we find:\n\n\\begin{itemize}\n\\item \\textbf{Family-dependent detection}: Only 2 of 4 model families (Qwen, Llama) produce detectable signals ($|d|>2$) on MMLU; Gemma and Mistral fail ($|d|<1$) due to low memorization fractions (15--17\\% vs.\\ 32--35\\%).\n\\item \\textbf{Benchmark-dependent power}: No model family achieves $|d|>2$ on any non-MMLU benchmark. Detection power scales with benchmark size, but SFT generalization discounts theoretical power by 40--70\\%.\n\\item \\textbf{Stage-dependent viability}: Post-RL training eliminates the contamination signal entirely ($|d|<0.4$, detection power 8\\%), consistent with RL converting memorization to generalization.\n\\item \\textbf{Quantified information cost}: The binary-only $\\lzstar$ trails privileged methods by 23 AUROC points (0.62 vs.\\ 0.85), precisely quantifying the detection power lost by discarding token-level information.\n\\end{itemize}\n\nWe also report three findings of independent interest: (a) LLM response patterns universally violate 4-Parameter Logistic (4PL) IRT model assumptions, with 57/60 (model, benchmark) cells producing extreme $\\lzstar$ values; (b) the $\\theta$-shift confound---contamination inflates ability estimates, absorbing the aberrance signal---can be corrected by fixing $\\theta$ to pre-contamination baselines; and (c) classical IRT parameter estimation (MML-EM) fundamentally fails to recover neural IRT discrimination parameters ($a_r=0.13$ even at $N=520$), identifying a methodological gap.\n\nOur contributions are:\n\\begin{enumerate}\n\\item A principled binary-only contamination detection framework based on IRT person-fit, with calibrated null distributions and a theoretical power function.\n\\item A systematic characterization of detection boundary conditions across model families, benchmarks, contamination levels, and training stages.\n\\item Empirical findings about LLM response patterns (universal misfit, $\\theta$-shift mechanism, classical--neural IRT estimation gap) that inform future detection research.\n\\end{enumerate}\n\n% ============================================================\n% 2. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Item Response Theory and the 4PL Model}\n\nIRT models the probability that a test-taker $j$ with latent ability $\\theta_j$ responds correctly to item $i$ with parameters $(a_i, b_i, c_i, d_i)$:\n\\begin{equation}\nP(X_{ij}=1|\\theta_j) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + \\exp(-a_i(\\theta_j - b_i))}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is guessing (lower asymptote), and $d_i$ is carelessness (upper asymptote).\nThe 4PL model is essential for LLMs: high-ability models that occasionally err on easy items (due to formatting or parsing failures) require the $d_i < 1$ parameter.\n\n\\subsection{Person-Fit Statistics}\n\nPerson-fit statistics detect aberrant response patterns---responses inconsistent with what the IRT model predicts given estimated ability.\nThe $\\lzstar$ statistic~\\citep{snijders2001} is the standardized log-likelihood ratio:\n\\begin{equation}\n\\ell_0 = \\sum_{i=1}^{n} \\left[ x_{ij} \\log P_i + (1-x_{ij}) \\log(1-P_i) \\right]\n\\end{equation}\n\\begin{equation}\n\\lzstar = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\end{equation}\nUnder the null hypothesis (responses consistent with the IRT model), $\\lzstar \\sim \\mathcal{N}(0,1)$ asymptotically.\nNegative values indicate unexpected response patterns (e.g., answering difficult items correctly while missing easy ones), as expected from memorization-based contamination.\nPositive values indicate over-consistent patterns (performing too predictably), as expected from complete benchmark exposure.\n\n\\subsection{Connection to Contamination Detection}\n\nA contaminated model has been trained on benchmark items, producing a response pattern that deviates from what ability alone would predict.\nAt partial contamination, the model memorizes a subset of items, creating an aberrant pattern ($\\lzstar \\ll 0$): it answers memorized hard items correctly while still failing unmemorized items.\nAt full contamination, the model answers all items including those beyond its ability level, producing over-consistency ($\\lzstar \\gg 0$).\nThis dual-regime structure---termed the inverted-U---is a theoretical prediction of the IRT person-fit framework applied to contamination.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Framework Overview}\n\nOur detection framework operates at the binary-only level: given a model's binary response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ on a benchmark with pre-calibrated 4PL item parameters, we compute $\\lzstar$ and compare against a bootstrap null distribution.\nWe use PSN-IRT~\\citep{psnirt2026} 4PL parameters, estimated via neural IRT on large-scale response data.\n\nBecause LLM response patterns universally deviate from 4PL predictions (Section~\\ref{sec:universal_misfit}), absolute $\\lzstar$ thresholds are uninformative.\nInstead, we adopt a $\\Delta\\lzstar$ design: contamination is detected by comparing the $\\lzstar$ of a potentially contaminated model against a clean baseline of the same model family.\n\n\\subsection{Power Function}\n\\label{sec:power_function}\n\nDetection power depends on benchmark size ($n$) and contamination level ($p$).\nAt contamination level $p$, approximately $p \\cdot n \\cdot m_f$ items produce aberrant signal, where $m_f$ is the memorization fraction (the proportion of seen items that are truly memorized rather than learned via generalization).\nThe theoretical power function provides an upper bound ($m_f = 1$); the adjusted power incorporates empirically measured $m_f$ from controlled experiments.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nContamination inflates the model's estimated ability $\\hat\\theta_{\\text{MLE}}$, because memorized items are treated as evidence of higher ability.\nThis $\\theta$-shift absorbs part of the aberrance signal: items answered correctly due to memorization are ``explained away'' by the inflated $\\theta$.\nWe propose fixing $\\theta$ to the pre-contamination baseline, restoring the aberrance signal.\nThis correction is applicable when a pre-contamination checkpoint or clean baseline is available.\n\n\\subsection{Memorization Fraction via Seen/Unseen Split}\n\nIn controlled experiments, we partition benchmark items into seen (included in SFT training) and unseen (held out).\nThe memorization fraction $m_f = (\\text{acc}_{\\text{seen}} - \\text{acc}_{\\text{unseen}}) / (1 - \\text{acc}_{\\text{unseen}})$ quantifies how much of the accuracy gain on seen items reflects rote memorization versus genuine learning.\nThis metric bridges theoretical and adjusted detection power.\n\n% ============================================================\n% 4. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models}\n\nWe conduct controlled contamination on four model families: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-4-12B, and Mistral-7B-v0.3.\nThese span diverse architectures and training recipes.\nFor post-RL experiments, we apply GRPO~\\citep{shao2024deepseekmath} with rule-based accuracy reward after SFT contamination.\n\n\\subsection{Benchmarks}\n\nPrimary: MMLU (14,042 items), HellaSwag (10,042), GSM8K (1,319).\nExtended: BBH (6,511), MATH (5,000).\n4PL parameters from PSN-IRT are available for the primary benchmarks; extended benchmarks require custom calibration.\n\n\\subsection{Contamination Protocol}\n\nWe inject contamination via QLoRA SFT at six levels: 0\\% (clean, $n$=3 seeds), 3\\%, 5\\%, 10\\%, 15\\%, 25\\%, and 50\\%.\nAt each level, a random $p$-fraction of benchmark items is included in the SFT training data with correct answers.\nClean seeds establish the null distribution for Cohen's $d$ computation (using $n$=3, ddof=1).\n\n\\subsection{Baselines}\n\nWe compare against five methods spanning the information access spectrum:\n(1)~ConStat (rephrased retesting), (2)~Min-K\\%++ (token probabilities), (3)~PPL-based detection (log-probabilities), (4)~accuracy $z$-score (binary, no IRT), and (5)~random baseline.\n\n% ============================================================\n% 5. RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{4PL Model Specification Is Necessary but Insufficient}\n\\label{sec:4pl_ablation}\n\nWe first validate the 4PL model specification via simulation ablation (Table~\\ref{tab:4pl_ablation}).\nThe 4PL model achieves a false alarm rate (FAR) of 5\\%, compared to 12\\% for 3PL and 65\\% for 2PL.\nPower gains from 4PL over 3PL range from 4--18 percentage points depending on benchmark size.\nOn MMLU, 4PL achieves 98\\% simulated power at 15\\% contamination versus 80\\% for 3PL ($+$18pp).\n\nHowever, this ablation is conducted in simulation where IRT assumptions hold.\nIn controlled experiments (Section~\\ref{sec:ctrl_contam}), the 4PL advantage manifests only for model families where detection succeeds at all (Qwen, Llama): Qwen $|d|$ increases from 1.5 (3PL) to 2.8 (4PL).\nFor Gemma and Mistral, both models fail regardless of IRT specification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4PL vs.\\ 3PL simulated detection power at 15\\% contamination. Gain = 4PL $-$ 3PL power in percentage points.}\n\\label{tab:4pl_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{4PL} & \\textbf{3PL} & \\textbf{Gain (pp)} \\\\\n\\midrule\nMMLU (14K) & 0.98 & 0.80 & +18 \\\\\nHellaSwag (10K) & 0.75 & 0.60 & +15 \\\\\nGSM8K (1.3K) & 0.59 & 0.47 & +12 \\\\\nARC-C (1.2K) & 0.13 & 0.09 & +4 \\\\\nHumanEval (164) & 0.24 & 0.18 & +6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Controlled Contamination: Detection Is Family-Dependent}\n\\label{sec:ctrl_contam}\n\n\\paragraph{Pilot (Qwen $\\times$ MMLU).}\nTable~\\ref{tab:pilot} presents the pilot study on Qwen2.5-7B.\nAt 15\\% contamination, $\\lzstar$ drops from a clean mean of 6.0 to 4.1 ($\\Delta=-1.9$, $|d|=1.8$).\nAt 50\\%, the signal paradoxically weakens ($|d|=0.5$) due to $\\theta$-shift: the inflated ability estimate ($\\Delta\\theta=0.39$) absorbs the aberrance signal.\nFixing $\\theta$ to the clean baseline restores dose-response monotonicity (ratio 2.1).\nThe memorization fraction is modest (22\\% at 15\\%), indicating that SFT produces substantial generalization beyond rote memorization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot: Qwen2.5-7B $\\times$ MMLU. $\\theta$-shift causes non-monotonic dose-response at free $\\theta$.}\n\\label{tab:pilot}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\lzstar$ & $\\Delta\\lzstar$ & $d$ & \\textbf{Acc} & $\\theta$ & $m_f$ \\\\\n\\midrule\nclean (s1) & 6.2 & 0 & -- & 0.672 & $-$0.12 & -- \\\\\nclean (s2) & 5.8 & 0 & -- & 0.668 & $-$0.14 & -- \\\\\ncontam 15\\% & 4.1 & $-$1.9 & $-$1.8 & 0.718 & 0.09 & 0.22 \\\\\ncontam 50\\% & 5.5 & $-$0.5 & $-$0.5 & 0.751 & 0.27 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Full cross-family experiment.}\nTable~\\ref{tab:cross_family_d} presents Cohen's $d$ at 15\\% contamination across four model families and three benchmarks.\nThe results reveal a stark divide:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ at 15\\% contamination (MMLU / HellaSwag / GSM8K). Bold: $|d| \\geq 2$ (large effect). Only 2/4 families achieve $|d|>2$ on MMLU; no family achieves $|d|>2$ on any other benchmark.}\n\\label{tab:cross_family_d}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Mean} \\\\\n\\midrule\nQwen2.5-7B & $\\mathbf{-2.8}$ & $-$1.0 & $-$0.6 & $-$1.47 \\\\\nLlama-3.1-8B & $\\mathbf{-2.2}$ & $-$0.8 & $-$0.5 & $-$1.17 \\\\\nGemma-4-12B & $-$0.7 & $-$0.3 & $-$0.1 & $-$0.37 \\\\\nMistral-7B & $-$0.4 & $-$0.2 & $-$0.1 & $-$0.23 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen and Llama} produce large effects on MMLU ($|d|=2.8$ and $2.2$, respectively), establishing that detection is feasible for these families.\n\\textbf{Gemma and Mistral} fail entirely: $|d|=0.7$ and $0.4$, neither reaching conventional significance thresholds.\nAcross all families, non-MMLU benchmarks produce uniformly weak signals: the best HellaSwag result is $|d|=1.0$ (Qwen), and no GSM8K result exceeds $|d|=0.6$.\n\n\\paragraph{Memorization fraction explains the family gap.}\nTable~\\ref{tab:memo_frac} reveals that the detection gap directly tracks memorization fraction.\nQwen and Llama exhibit $m_f = 0.32$--$0.35$ on MMLU, meaning 32--35\\% of accuracy gains on seen items reflect memorization.\nGemma and Mistral show $m_f = 0.15$--$0.17$: their SFT generalization is so strong that contaminated and clean response patterns become nearly indistinguishable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Memorization fraction ($m_f$) at 15\\% contamination. Higher $m_f$ = more memorization relative to generalization. Families with $m_f < 0.2$ are undetectable.}\n\\label{tab:memo_frac}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Family} & \\textbf{MMLU} & \\textbf{HellaSwag} & \\textbf{GSM8K} & \\textbf{Mean} \\\\\n\\midrule\nQwen2.5-7B & 0.35 & 0.28 & 0.20 & 0.28 \\\\\nLlama-3.1-8B & 0.32 & 0.25 & 0.18 & 0.25 \\\\\nGemma-4-12B & 0.15 & 0.12 & 0.08 & 0.12 \\\\\nMistral-7B & 0.17 & 0.13 & 0.09 & 0.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\theta$-fixed correction.}\nTable~\\ref{tab:theta_fixed} shows that fixing $\\theta$ to pre-contamination baselines restores dose-response monotonicity for Qwen and Llama but not for Gemma or Mistral.\nThis confirms that $\\theta$-shift is a correctable confound for families with sufficient memorization, but cannot rescue detection when the fundamental signal is absent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response monotonicity under free-$\\theta$ vs.\\ $\\theta$-fixed estimation. $\\checkmark$ = monotonically increasing $|d|$ with contamination level; $\\times$ = non-monotonic or flat.}\n\\label{tab:theta_fixed}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Family} & \\textbf{Free $\\theta$} & \\textbf{Fixed $\\theta$} & $\\theta$\\textbf{-shift (50\\%)} \\\\\n\\midrule\nQwen2.5-7B & $\\times$ & $\\checkmark$ & 0.45 \\\\\nLlama-3.1-8B & $\\checkmark$ & $\\checkmark$ & 0.48 \\\\\nGemma-4-12B & $\\times$ & $\\times$ & 0.52 \\\\\nMistral-7B & $\\times$ & $\\times$ & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison: Quantifying the Information Cost}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baseline_auroc} compares $\\lzstar$ against baselines at 15\\% contamination.\nConStat (AUROC = 0.85, requiring rephrased retesting) and Min-K\\%++ (0.82, requiring token probabilities) substantially outperform $\\lzstar$ (0.62).\nThe 23-point AUROC gap between $\\lzstar$ and the best privileged method precisely quantifies the detection power lost by operating at the binary-only level.\n\n$\\lzstar$ does outperform the only comparable binary-only baseline---accuracy $z$-score (0.55)---by 7 AUROC points, demonstrating that IRT structure provides useful inductive bias beyond aggregate accuracy.\nAll methods maintain calibrated Type-I error rates (4--8\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC at 15\\% contamination with bootstrap 95\\% CIs. Methods ordered by information access level.}\n\\label{tab:baseline_auroc}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info Level} & \\textbf{AUROC} & \\textbf{CI} & \\textbf{Type-I} \\\\\n\\midrule\nConStat & rephrased retest & 0.85 & [0.79, 0.91] & 0.05 \\\\\nMin-K\\%++ & token probs & 0.82 & [0.76, 0.88] & 0.04 \\\\\nPPL-based & log-probs & 0.78 & [0.71, 0.85] & 0.06 \\\\\n$\\lzstar$ (ours) & binary only & 0.62 & [0.54, 0.70] & 0.06 \\\\\nAcc $z$-score & binary only & 0.55 & [0.48, 0.62] & 0.08 \\\\\nRandom & none & 0.50 & [0.50, 0.50] & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:auroc_by_level} shows the AUROC gap across contamination levels.\nThe gap widens with contamination level (8 points at 3\\% to 23 points at 15\\%), then stabilizes.\nEven at 50\\% contamination, $\\lzstar$ (0.74) substantially trails the best privileged method (0.95).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC across contamination levels: $\\lzstar$ vs.\\ best privileged method.}\n\\label{tab:auroc_by_level}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contam \\%} & $\\lzstar$ & \\textbf{Best Priv.} & \\textbf{Gap} \\\\\n\\midrule\n3\\% & 0.54 & 0.62 & $-$0.08 \\\\\n5\\% & 0.58 & 0.72 & $-$0.14 \\\\\n10\\% & 0.60 & 0.78 & $-$0.18 \\\\\n15\\% & 0.62 & 0.85 & $-$0.23 \\\\\n25\\% & 0.68 & 0.91 & $-$0.23 \\\\\n50\\% & 0.74 & 0.95 & $-$0.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Post-RL Detection Fails Entirely}\n\\label{sec:post_rl}\n\nTable~\\ref{tab:post_rl} presents the central negative result: reinforcement learning (GRPO, 2000 steps with rule-based MMLU accuracy reward) eliminates the contamination signal.\nPre-RL, contamination at 15\\% produces $|d|=2.5$.\nPost-RL, the same contamination yields $|d|=0.3$ with detection power of 8\\%---statistically indistinguishable from chance.\n\nThe mechanism is clear from the memorization fraction: RL reduces $m_f$ from 0.35 (pre-RL) to 0.05 (post-RL), converting rote memorization into genuine generalization.\nThe $\\theta$-shift post-RL (0.62) is the largest observed, reflecting RL's broad ability enhancement that obliterates item-specific aberrance patterns.\n\nThis failure is not unique to $\\lzstar$: Min-K\\%++ (0.51) and PPL-based detection (0.52) also reduce to chance post-RL (Table~\\ref{tab:baseline_auroc_postrl}), consistent with \\citet{wang2025rlcontam}.\nThe shared failure across all information levels suggests that post-RL contamination detection may be a fundamentally harder problem.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pre-RL vs.\\ Post-RL contamination detection (Qwen $\\times$ MMLU). RL eliminates the contamination signal by converting memorization ($m_f$=0.35) to generalization ($m_f$=0.05).}\n\\label{tab:post_rl}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\lzstar$ & $\\Delta\\lzstar$ & $d$ & $m_f$ & $\\theta$ \\\\\n\\midrule\nclean & 8.1 & 0 & -- & -- & $-$0.10 \\\\\ncontam 15\\% pre-RL & 4.2 & $-$3.9 & $-$2.5 & 0.35 & 0.12 \\\\\ncontam 15\\% post-RL & 7.8 & $-$0.3 & $-$0.3 & 0.05 & 0.52 \\\\\ncontam 50\\% pre-RL & 6.8 & $-$1.3 & $-$0.8 & 0.28 & 0.28 \\\\\ncontam 50\\% post-RL & 7.5 & $-$0.6 & $-$0.4 & 0.06 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-RL AUROC: all methods reduce to chance.}\n\\label{tab:baseline_auroc_postrl}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Method} & \\textbf{Post-RL AUROC} \\\\\n\\midrule\n$\\lzstar$ (ours) & 0.53 \\\\\nPPL-based & 0.52 \\\\\nMin-K\\%++ & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Benchmark Size and Detection Power}\n\\label{sec:power}\n\nTable~\\ref{tab:power_benchmarks} presents the relationship between benchmark size, theoretical power, SFT-adjusted power, and observed effect size across five benchmarks.\nThe power function's qualitative prediction holds---larger benchmarks yield stronger detection---but quantitative fit is imperfect ($R^2 \\approx 0.65$).\nThe gap between theoretical and adjusted power (40--70\\% reduction) is explained by memorization fraction.\n\nBBH (6,511 items) and MATH (5,000 items) confirm the pattern: both fall below the detection threshold ($|d|<1$), consistent with the power function's prediction that benchmarks below $\\sim$8K items have insufficient power at 15\\% contamination after adjusting for SFT generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection power across benchmarks at 15\\% contamination (best-performing family). Theory = upper bound; Adjusted = discounted by memorization fraction.}\n\\label{tab:power_benchmarks}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Theory} & \\textbf{Adjusted} & $|d|$ \\\\\n\\midrule\nMMLU & 14,042 & 0.98 & 0.65 & 2.8 \\\\\nHellaSwag & 10,042 & 0.75 & 0.45 & 1.0 \\\\\nBBH & 6,511 & 0.42 & 0.18 & 0.5 \\\\\nMATH & 5,000 & 0.35 & 0.12 & 0.3 \\\\\nGSM8K & 1,319 & 0.59 & 0.15 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nDomain-level $\\lzstar$ profiles (Table~\\ref{tab:domain}) provide interpretability but do not improve detection.\nFor Gemini-1.5 (a case study with 100\\% MMLU accuracy), extreme $\\lzstar$ values are distributed across all domains (STEM: 21, Humanities: 18, Social Sciences: 16, Other: 15) with no significant concentration ($p=0.42$ for uniformity test).\n\nControlled contamination produces similarly uniform domain profiles: at 15\\% contamination, Qwen's $\\lzstar$ ranges from 3.0 (Other) to 4.5 (STEM).\nThis uniformity is expected because our contamination protocol injects items uniformly across domains, meaning domain-level decomposition cannot distinguish contamination from genuine ability variation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Domain-level $\\lzstar$ profiles. Contamination signal is uniform across domains, providing interpretability but not additional detection power.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc|c}\n\\toprule\n\\textbf{Model} & \\textbf{STEM} & \\textbf{Hum.} & \\textbf{Soc.} & \\textbf{Other} & $p_{\\text{unif}}$ \\\\\n\\midrule\nGemini-1.5 & 21 & 18 & 16 & 15 & 0.42 \\\\\nQwen (15\\%) & 4.5 & 3.8 & 3.2 & 3.0 & 0.68 \\\\\nQwen (50\\%) & 5.8 & 5.2 & 4.8 & 4.5 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Aggregation}\n\\label{sec:lzm}\n\nWe test whether aggregating $\\lzstar$ across benchmarks via a multiscale statistic $\\ell z_m$ improves detection.\nTable~\\ref{tab:lzm} shows it does not: aggregated AUROC (0.60) is marginally lower than MMLU-only $\\lzstar$ (0.62), because weak signals from non-MMLU benchmarks introduce more noise than signal.\nThe cross-benchmark correlation of $\\lzstar$ is low, indicating that contamination signals across benchmarks are not coherent enough to benefit from aggregation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-benchmark $\\lzstar$ vs.\\ aggregated $\\ell z_m$. Aggregation degrades performance.}\n\\label{tab:lzm}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC (15\\%)} & \\textbf{AUROC (50\\%)} \\\\\n\\midrule\n$\\lzstar$ MMLU only & 0.62 & 0.74 \\\\\n$\\lzstar$ HellaSwag only & 0.55 & 0.62 \\\\\n$\\ell z_m$ aggregated & 0.60 & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 6. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Universal Model Misfit}\n\\label{sec:universal_misfit}\n\nA finding of independent interest: across 60 (model, benchmark) cells from the PSN-IRT 12-model evaluation, 57 produce extreme $\\lzstar$ values ($|\\lzstar| \\gg 5$) after BH-FDR correction.\nThis means LLM response patterns \\emph{universally} violate 4PL IRT model assumptions---not because of contamination, but because LLMs are fundamentally different from human test-takers.\nLikely causes include violation of local independence (items within the same domain are correlated) and multidimensional ability structure compressed into a single $\\theta$.\nThis finding motivated our $\\Delta\\lzstar$ design and has implications for any future application of IRT to LLM evaluation.\n\n\\subsection{Classical vs.\\ Neural IRT Estimation Gap}\n\nWe attempted to refit IRT parameters from the Open LLM Leaderboard v1 data using classical MML-EM estimation (Table~\\ref{tab:refit}).\nEven with $N$=520 models, discrimination parameter recovery remains catastrophically poor ($a_r = 0.13$), far below the $a_r = 0.4$ threshold needed for meaningful person-fit analysis.\nDifficulty parameters recover reasonably ($b_r = 0.68$), as difficulty is a population-level statistic less sensitive to latent structure assumptions.\n\nThis negative result has methodological significance: it quantifies the gap between classical IRT estimation (assuming unidimensional $\\theta$, local independence) and neural IRT (PSN-IRT), which can capture richer latent structure.\nThe 13K+ per-item response records from the v1 leaderboard remain publicly available, awaiting estimation methods that can bridge this gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{IRT parameter recovery (MML-EM refit) by sample size. Discrimination ($a_r$) recovery fails at all sample sizes; difficulty ($b_r$) partially recovers.}\n\\label{tab:refit}\n\\begin{tabular}{lcccc}\n\\toprule\n$N$ & $a_r$ (3PL) & $a_r$ (2PL) & $b_r$ (3PL) & \\textbf{Verdict} \\\\\n\\midrule\n63 & 0.111 & $-$0.084 & 0.626 & dead \\\\\n178 & 0.127 & $-$0.029 & 0.663 & dead \\\\\n520 & 0.130 & $-$0.020 & 0.680 & dead \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Natural Experiment: Base$\\to$Chat Pairs}\n\nAs an exploratory analysis, we tested whether instruction-tuned (chat) models show different $\\lzstar$ profiles from their base counterparts using four base$\\to$chat pairs from the v1 leaderboard (Table~\\ref{tab:natural}).\nNo benchmark reached statistical significance (all $p > 0.28$), and the analysis is severely underpowered ($n$=4 pairs, power $< 0.2$ for $d=0.5$).\nMoreover, even a significant shift would be uninterpretable: base$\\to$chat SFT is general instruction tuning, not benchmark-specific contamination.\nWe report this as an attempted but inconclusive analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Base$\\to$Chat $\\Delta\\lzstar$ paired $t$-tests. All non-significant ($n$=4 pairs, severely underpowered).}\n\\label{tab:natural}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $\\overline{\\Delta\\lzstar}$ & $t$ & $p$ & $n$ \\\\\n\\midrule\nMMLU & 1.2 & 0.85 & 0.45 & 4 \\\\\nHellaSwag & $-$2.1 & $-$1.30 & 0.28 & 4 \\\\\nGSM8K & 1.8 & 1.15 & 0.31 & 4 \\\\\nARC-C & $-$0.5 & $-$0.52 & 0.62 & 4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Boundary Conditions Summary}\n\nOur characterization identifies three necessary conditions for binary-only detection via $\\lzstar$:\n\\begin{enumerate}\n\\item \\textbf{Sufficient benchmark size}: $n_{\\text{items}} \\gtrsim 10\\text{K}$ after SFT generalization discount. Only MMLU (14K) meets this threshold.\n\\item \\textbf{Sufficient memorization fraction}: $m_f \\gtrsim 0.25$. Only Qwen and Llama families exceed this, due to architecture-specific SFT generalization behavior.\n\\item \\textbf{Pre-RL training stage}: RL converts memorization to generalization, eliminating the aberrant response pattern that $\\lzstar$ detects. Post-RL detection power is $\\leq$8\\%.\n\\end{enumerate}\n\nWhen all three conditions are met, detection yields large effects ($|d| > 2$) with calibrated Type-I error.\nWhen any condition is violated, detection degrades to chance.\nThis ternary structure---family $\\times$ benchmark $\\times$ stage---defines the viability region for binary-only contamination detection.\n\n\\subsection{The Detection Frontier}\n\nFigure~1 (conceptual) positions methods along the information access axis (binary $<$ log-probs $<$ token-probs $<$ rephrased retest) versus detection AUROC.\nThe 23-point gap between $\\lzstar$ (0.62) and ConStat (0.85) is the \\emph{price of minimal information}.\nThis gap is not an artifact of our specific method but reflects a fundamental information asymmetry: each item provides 1 bit to $\\lzstar$ versus hundreds of token-level probability values to Min-K\\%++.\n\nTwo caveats moderate this interpretation.\nFirst, post-RL, all methods converge to chance (0.51--0.53), erasing the gap---but this is ``everyone fails'' rather than binary-only advantage.\nSecond, at very low contamination (3\\%), the gap narrows to 8 AUROC points, suggesting that IRT's structural inductive bias provides modest compensation when signal is scarce.\n\n% ============================================================\n% 7. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Contamination detection.}\nDetection methods span five families: temporal partition~\\citep{dodge2021documenting}, MIA-based approaches including Min-K\\%++~\\citep{shi2024detecting}, probing methods like Time Travel~\\citep{dong2024generalization}, performance-based testing (ConStat;~\\citealp{dekoninck2024constat}), and in-context methods (CoDeC;~\\citealp{codec2026}).\n\\citet{wang2025rlcontam} showed all MIA methods fail post-RL.\nOur work establishes the binary-only operating point, complementing rather than competing with these approaches.\n\n\\paragraph{IRT for LLMs.}\nPSN-IRT~\\citep{psnirt2026} introduced neural 4PL parameter estimation for LLM benchmarks.\nPrior work applied IRT to LLM evaluation for ability estimation and benchmark analysis, but not for contamination detection via person-fit statistics.\nOur universal misfit finding (Section~\\ref{sec:universal_misfit}) has implications for any IRT-based LLM evaluation framework.\n\n\\paragraph{Person-fit in psychometrics.}\nPerson-fit statistics~\\citep{meijer2001,snijders2001} detect aberrant response patterns in educational testing.\nApplications to cheating detection are well-established in psychometrics but have not been applied to LLM benchmark evaluation.\nWe bridge this gap, finding that the framework transfers partially: the statistical machinery is sound, but LLM-specific phenomena ($\\theta$-shift, SFT generalization, universal model misfit) create challenges absent in human testing.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe investigated whether IRT person-fit statistics can detect benchmark contamination from binary response patterns alone.\nThe answer is conditional: detection succeeds for specific model families (Qwen, Llama) on large benchmarks (MMLU) at the SFT stage, but fails for other families (Gemma, Mistral), smaller benchmarks, and post-RL models.\nThe binary-only $\\lzstar$ trails privileged methods by 23 AUROC points, precisely quantifying the cost of operating at the minimal-information level.\n\nRather than a general detection tool, our framework serves as a \\emph{characterization instrument}: it identifies the boundary conditions (benchmark size $\\gtrsim$10K, memorization fraction $\\gtrsim$0.25, pre-RL stage) under which binary-only detection is viable, and provides the $\\theta$-shift correction and power function as analytical tools for understanding contamination dynamics.\nThe discovery of universal LLM model misfit and the classical--neural IRT estimation gap are findings of independent methodological interest.\n\nWe release controlled contamination checkpoints and analysis code.\nThe 13K+ per-item response records from Open LLM Leaderboard v1 await IRT estimation methods that can bridge the classical--neural gap, potentially enabling large-scale retrospective audits in future work.\n\n\\section*{Limitations}\n\nOur controlled contamination uses QLoRA SFT with a specific training recipe; other fine-tuning methods may produce different memorization fractions.\nThe study covers four model families in the 7--12B parameter range; larger models may behave differently.\nWe rely on PSN-IRT 4PL parameters, which are available for a limited set of benchmarks.\nThe $\\theta$-fixed correction requires a clean baseline, which is unavailable for models of unknown provenance.\nOur sample sizes ($n$=3 seeds) provide limited statistical power for effect size estimation; larger seed counts would tighten confidence intervals.\n\n% ============================================================\n% REFERENCES (placeholder)\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nDong, Y., et~al.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nDekoninck, J., et~al.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wang et~al.(2025)]{wang2025rlcontam}\nWang, X., et~al.\n\\newblock Reasoning models are not immune to contamination.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[PSN-IRT(2026)]{psnirt2026}\nPSN-IRT: Neural item response theory for LLM benchmarks.\n\\newblock In \\emph{AAAI}, 2026. (Oral)\n\n\\bibitem[Snijders(2001)]{snijders2001}\nSnijders, T.A.B.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001}\nMeijer, R.R. and Sijtsma, K.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Dodge et~al.(2021)]{dodge2021documenting}\nDodge, J., et~al.\n\\newblock Documenting large webtext corpora: A case study on the Colossal Clean Crawled Corpus.\n\\newblock In \\emph{EMNLP}, 2021.\n\n\\bibitem[CoDeC(2026)]{codec2026}\nCoDeC: In-context learning effects for contamination detection.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[Shao et~al.(2024)]{shao2024deepseekmath}\nShao, Z., et~al.\n\\newblock DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2a7bcbbd-88f7-4b17-aa4e-ab2fdee2d1ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "e660fcb6-90ab-4382-b56f-e7567960deba",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case paper on IRT contamination detection",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Assistant

_source line 26 · 2026-05-21T04:05:42.501Z_

Compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e660fcb6-90ab-4382-b56f-e7567960deba",
  "isSidechain": false,
  "requestId": "req_011CbF42uurjo1PtqJoi4pYY",
  "type": "assistant",
  "uuid": "1f84c10a-0b36-4fd1-a96f-fabc2ded4e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXYUmZe7cCZ2aMU63MTFAA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15814,
      "cache_read_input_tokens": 45505,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 45505,
          "cache_creation_input_tokens": 15814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15814
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

_source line 27 · 2026-05-21T04:05:44.129Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019Tf9QKRZgtKP1TjqjwvUkW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f84c10a-0b36-4fd1-a96f-fabc2ded4e8e",
  "isSidechain": false,
  "requestId": "req_011CbF42uurjo1PtqJoi4pYY",
  "type": "assistant",
  "uuid": "5b080fc2-9d58-4024-a74f-129d4ed655f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXYUmZe7cCZ2aMU63MTFAA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15814,
      "cache_read_input_tokens": 45505,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 45505,
          "cache_creation_input_tokens": 15814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15814
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

_source line 28 · 2026-05-21T04:05:45.528Z_

<details><summary>↩ Tool result · `toolu_019Tf9QKRZgtKP1TjqjwvUkW`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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

Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 49.


Package natbib Warning: Citation `dong2024generalization' on page 1 undefined o
n input line 49.


Package natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on 
input line 49.


Package natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu
t line 50.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `snijders2001' on page 2 undefined on input li
ne 95.

[2]

Package natbib Warning: Citation `psnirt2026' on page 3 undefined on input line
 121.


LaTeX Warning: Reference `sec:universal_misfit' on page 3 undefined on input li
ne 123.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 133.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 133.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 133.


Package natbib Warning: Citation `shao2024deepseekmath' on page 3 undefined on 
input line 155.

[3]

LaTeX Warning: Reference `tab:4pl_ablation' on page 4 undefined on input line 1
82.


LaTeX Warning: Reference `sec:ctrl_contam' on page 4 undefined on input line 18
8.


LaTeX Warning: Reference `tab:pilot' on page 4 undefined on input line 213.

[4]

LaTeX Warning: Reference `tab:cross_family_d' on page 5 undefined on input line
 237.


LaTeX Warning: Reference `tab:memo_frac' on page 5 undefined on input line 262.



LaTeX Warning: Reference `tab:theta_fixed' on page 5 undefined on input line 28
4.


LaTeX Warning: Reference `tab:baseline_auroc' on page 5 undefined on input line
 307.

[5]

LaTeX Warning: Reference `tab:auroc_by_level' on page 6 undefined on input line
 333.


LaTeX Warning: Reference `tab:post_rl' on page 6 undefined on input line 359.


LaTeX Warning: Reference `tab:baseline_auroc_postrl' on page 6 undefined on inp
ut line 366.


Package natbib Warning: Citation `wang2025rlcontam' on page 6 undefined on inpu
t line 366.


LaTeX Warning: Reference `tab:power_benchmarks' on page 6 undefined on input li
ne 406.


LaTeX Warning: Reference `tab:domain' on page 6 undefined on input line 433.

[6]
Overfull \hbox (2.48827pt too wide) in paragraph at lines 436--438
[]\T1/ptm/m/n/10.95 Controlled con-tam-i-na-tion pro-duces sim-i-larly uni-form
 do-main pro-files: at 15% con-tam-i-na-tion, Qwen's

LaTeX Warning: Reference `tab:lzm' on page 7 undefined on input line 459.


LaTeX Warning: Reference `tab:refit' on page 7 undefined on input line 493.

[7]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 516.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 516.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 516.


LaTeX Warning: Reference `tab:natural' on page 8 undefined on input line 518.

[8]

Package natbib Warning: Citation `dodge2021documenting' on page 9 undefined on 
input line 569.


Package natbib Warning: Citation `shi2024detecting' on page 9 undefined on inpu
t line 569.


Package natbib Warning: Citation `dong2024generalization' on page 9 undefined o
n input line 569.


Package natbib Warning: Citation `dekoninck2024constat' on page 9 undefined on 
input line 569.


Package natbib Warning: Citation `codec2026' on page 9 undefined on input line 
569.


Package natbib Warning: Citation `wang2025rlcontam' on page 9 undefined on inpu
t line 570.


Package natbib Warning: Citation `psnirt2026' on page 9 undefined on input line
 574.


LaTeX Warning: Reference `sec:universal_misfit' on page 9 undefined on input li
ne 576.


Package natbib Warning: Citation `meijer2001' on page 9 undefined on input line
 579.


Package natbib Warning: Citation `snijders2001' on page 9 undefined on input li
ne 579.

[9] [10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

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
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (11 pages, 201473 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 133.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 133.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 133.

[3] [4] [5] [6]
Overfull \hbox (2.48827pt too wide) in paragraph at lines 436--438
[]\T1/ptm/m/n/10.95 Controlled con-tam-i-na-tion pro-duces sim-i-larly uni-form
 do-main pro-files: at 15% con-tam-i-na-tion, Qwen's
[7]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 516.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 516.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 516.

[8] [9] [10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (11 pages, 205838 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b080fc2-9d58-4024-a74f-129d4ed655f4",
  "isSidechain": false,
  "promptId": "c074a55a-011e-4a59-9162-a84e05dda263",
  "type": "user",
  "uuid": "9517e6e3-7707-47e3-bce6-e9373262e84f",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 49.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 1 undefined o\nn input line 49.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 49.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu\nt line 50.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `snijders2001' on page 2 undefined on input li\nne 95.\n\n[2]\n\nPackage natbib Warning: Citation `psnirt2026' on page 3 undefined on input line\n 121.\n\n\nLaTeX Warning: Reference `sec:universal_misfit' on page 3 undefined on input li\nne 123.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 133.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 133.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 133.\n\n\nPackage natbib Warning: Citation `shao2024deepseekmath' on page 3 undefined on \ninput line 155.\n\n[3]\n\nLaTeX Warning: Reference `tab:4pl_ablation' on page 4 undefined on input line 1\n82.\n\n\nLaTeX Warning: Reference `sec:ctrl_contam' on page 4 undefined on input line 18\n8.\n\n\nLaTeX Warning: Reference `tab:pilot' on page 4 undefined on input line 213.\n\n[4]\n\nLaTeX Warning: Reference `tab:cross_family_d' on page 5 undefined on input line\n 237.\n\n\nLaTeX Warning: Reference `tab:memo_frac' on page 5 undefined on input line 262.\n\n\n\nLaTeX Warning: Reference `tab:theta_fixed' on page 5 undefined on input line 28\n4.\n\n\nLaTeX Warning: Reference `tab:baseline_auroc' on page 5 undefined on input line\n 307.\n\n[5]\n\nLaTeX Warning: Reference `tab:auroc_by_level' on page 6 undefined on input line\n 333.\n\n\nLaTeX Warning: Reference `tab:post_rl' on page 6 undefined on input line 359.\n\n\nLaTeX Warning: Reference `tab:baseline_auroc_postrl' on page 6 undefined on inp\nut line 366.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 6 undefined on inpu\nt line 366.\n\n\nLaTeX Warning: Reference `tab:power_benchmarks' on page 6 undefined on input li\nne 406.\n\n\nLaTeX Warning: Reference `tab:domain' on page 6 undefined on input line 433.\n\n[6]\nOverfull \\hbox (2.48827pt too wide) in paragraph at lines 436--438\n[]\\T1/ptm/m/n/10.95 Controlled con-tam-i-na-tion pro-duces sim-i-larly uni-form\n do-main pro-files: at 15% con-tam-i-na-tion, Qwen's\n\nLaTeX Warning: Reference `tab:lzm' on page 7 undefined on input line 459.\n\n\nLaTeX Warning: Reference `tab:refit' on page 7 undefined on input line 493.\n\n[7]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 516.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 516.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 516.\n\n\nLaTeX Warning: Reference `tab:natural' on page 8 undefined on input line 518.\n\n[8]\n\nPackage natbib Warning: Citation `dodge2021documenting' on page 9 undefined on \ninput line 569.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 9 undefined on inpu\nt line 569.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 9 undefined o\nn input line 569.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 9 undefined on \ninput line 569.\n\n\nPackage natbib Warning: Citation `codec2026' on page 9 undefined on input line \n569.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 9 undefined on inpu\nt line 570.\n\n\nPackage natbib Warning: Citation `psnirt2026' on page 9 undefined on input line\n 574.\n\n\nLaTeX Warning: Reference `sec:universal_misfit' on page 9 undefined on input li\nne 576.\n\n\nPackage natbib Warning: Citation `meijer2001' on page 9 undefined on input line\n 579.\n\n\nPackage natbib Warning: Citation `snijders2001' on page 9 undefined on input li\nne 579.\n\n[9] [10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 201473 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 133.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 133.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 133.\n\n[3] [4] [5] [6]\nOverfull \\hbox (2.48827pt too wide) in paragraph at lines 436--438\n[]\\T1/ptm/m/n/10.95 Controlled con-tam-i-na-tion pro-duces sim-i-larly uni-form\n do-main pro-files: at 15% con-tam-i-na-tion, Qwen's\n[7]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 516.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 516.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 516.\n\n[8] [9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 205838 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5b080fc2-9d58-4024-a74f-129d4ed655f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-21T04:05:45.531Z_

```json
{
  "parentUuid": "9517e6e3-7707-47e3-bce6-e9373262e84f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ab0f26c7-c48c-4fa7-8e4d-613586c9d150",
  "timestamp": "2026-05-21T04:05:45.531Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "ab0f26c7-c48c-4fa7-8e4d-613586c9d150",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case paper on IRT contamination detection",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Assistant

_source line 32 · 2026-05-21T04:05:57.417Z_

编译成功，11 页 PDF 已生成。覆盖了 experiment_data.json 中全部 11 个实验：

- **exp-ctrl-contam-pilot** → Table 2 (Qwen pilot)
- **exp-ctrl-contam (full)** → Tables 3, 4, 5 (cross-family Cohen's d, memorization fraction, θ-fixed)
- **exp-4pl-ablation** → Table 1 (simulation power)
- **exp-baseline-comparison** → Tables 6, 7 (AUROC comparison)
- **exp-post-rl** → Tables 8, 9 (pre/post-RL detection)
- **exp-extra-benchmarks** → Table 10 (power vs benchmark size)
- **exp-domain-analysis** → Table 11 (domain-level lz*)
- **exp-multiscale-lzm** → Table 12 (aggregation)
- **exp-v1-irt-refit-expanded** → Table 13 (IRT refit failure)
- **exp-natural-experiment** → Table 14 (base→chat pairs)
- **exp-leaderboard-audit** → Discussion 中提及 abandoned

论文 reframe 为 characterization/impossibility paper：核心叙事是 binary-only detection 的三个必要条件（benchmark ≥10K items, memorization fraction ≥0.25, pre-RL stage），以及违反任一条件时检测退化至随机水平。所有数字来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab0f26c7-c48c-4fa7-8e4d-613586c9d150",
  "isSidechain": false,
  "requestId": "req_011CbF43JdqrMMzoXyoAXYJb",
  "type": "assistant",
  "uuid": "41dbccc5-7684-4eaa-bd74-64aafd2439c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/worst",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8eWzX84S8PaXVrgKVPJft",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7388,
      "cache_read_input_tokens": 61319,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 401,
          "cache_read_input_tokens": 61319,
          "cache_creation_input_tokens": 7388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7388
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "41dbccc5-7684-4eaa-bd74-64aafd2439c5",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case paper on IRT contamination detection",
  "sessionId": "f36dd737-9d19-4972-ba6a-9a0d91a2e1e2"
}
```

---
