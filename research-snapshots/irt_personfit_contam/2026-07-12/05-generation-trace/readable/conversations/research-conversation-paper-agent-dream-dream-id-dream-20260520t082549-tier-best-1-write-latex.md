# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/a3045954-1da3-47eb-9a00-6db6f9842f06.jsonl`
- **Structured JSON:** [`518c46369fada81b32e7.json`](../../sessions/51/518c46369fada81b32e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:52:16.179Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:52:16.179Z",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items 有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit 构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成\"MIA 失效但 person-fit 存活\"的对比叙事。 Headline: \"IRT-FIT 是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法\"。 EMNLP 主会议无需调整 claim 强度。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T08:52:16.182Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:52:16.182Z",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-20T08:52:16.201Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items 有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit 构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT 是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim 强度。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "5265bc90-a4c7-45e1-aec1-6c049c9bb629",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:52:16.200Z_

```json
{
  "parentUuid": "5265bc90-a4c7-45e1-aec1-6c049c9bb629",
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
  "uuid": "b9cbbd64-17e3-444e-af79-8796a622f339",
  "timestamp": "2026-05-20T08:52:16.200Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:52:16.201Z_

```json
{
  "parentUuid": "b9cbbd64-17e3-444e-af79-8796a622f339",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "539f92b5-d749-4e11-b15e-2e089d12b4f9",
  "timestamp": "2026-05-20T08:52:16.201Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
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
  "aiTitle": "Generate IRT-based contamination detection paper",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Assistant

_source line 7 · 2026-05-20T08:52:18.716Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539f92b5-d749-4e11-b15e-2e089d12b4f9",
  "isSidechain": false,
  "requestId": "req_011CbDY5bTSSU45ScFy2CCaU",
  "type": "assistant",
  "uuid": "bc703e36-40ae-4b40-9788-bd044dce3f93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuhgREacGWRJxzmRvoDbc3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11800,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11800
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

_source line 8 · 2026-05-20T08:52:19.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_013egsXAKpDMhuXRyr11iEe1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc703e36-40ae-4b40-9788-bd044dce3f93",
  "isSidechain": false,
  "requestId": "req_011CbDY5bTSSU45ScFy2CCaU",
  "type": "assistant",
  "uuid": "6bfd6c2a-d1f3-4307-bec5-de6c5343bb34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuhgREacGWRJxzmRvoDbc3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11800,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11800
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

_source line 9 · 2026-05-20T08:52:20.185Z_

<details><summary>↩ Tool result · `toolu_013egsXAKpDMhuXRyr11iEe1`</summary>

```text
1	[
2	  {
3	    "name": "Two-Sided Detection Framework",
4	    "description": "基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。\n",
5	    "results": {
6	      "gemini15_mmlu_lz_star": 34.75,
7	      "gemini15_mmlu_lz_star_bootstrap_95ci": "[32.1, 37.4]",
8	      "gemini15_gsm8k_lz_star": -15.71,
9	      "gemini15_humaneval_lz_star": -12.37,
10	      "two_sided_flagged_models_at_fdr_0.05": 4,
11	      "one_sided_flagged_models_at_fdr_0.05": 2,
12	      "incremental_detection_gain_two_vs_one_sided": "2 additional models flagged (Gemini-1.5 on MMLU, 1 other high-perf model)",
13	      "optimal_negative_threshold_alpha_0.05": -2.81,
14	      "optimal_positive_threshold_alpha_0.05": 3.24,
15	      "positive_regime_models": "Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling model",
16	      "negative_regime_models": "Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)"
17	    },
18	    "tables": [
19	      {
20	        "name": "Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)",
21	        "columns": [
22	          "model",
23	          "benchmark",
24	          "accuracy",
25	          "theta_hat",
26	          "lz_star",
27	          "side",
28	          "flagged_bh_fdr_005",
29	          "bootstrap_95ci"
30	        ],
31	        "key_rows": [
32	          [
33	            "Gemini-1.5",
34	            "MMLU",
35	            1.0,
36	            0.78,
37	            34.75,
38	            "positive",
39	            "YES",
40	            "[32.1, 37.4]"
41	          ],
42	          [
43	            "Gemini-1.5",
44	            "GSM8K",
45	            0.946,
46	            2.41,
47	            -15.71,
48	            "negative",
49	            "YES",
50	            "[-17.2, -14.3]"
51	          ],
52	          [
53	            "Gemini-1.5",
54	            "HumanEval",
55	            0.878,
56	            1.92,
57	            -12.37,
58	            "negative",
59	            "YES",
60	            "[-14.1, -10.8]"
61	          ],
62	          [
63	            "GPT-4",
64	            "MMLU",
65	            0.864,
66	            2.15,
67	            -1.23,
68	            "—",
69	            "no",
70	            "[-2.1, -0.4]"
71	          ],
72	          [
73	            "Llama-2-70B",
74	            "ARC-C",
75	            0.673,
76	            1.08,
77	            -3.87,
78	            "negative",
79	            "YES",
80	            "[-5.2, -2.6]"
81	          ]
82	        ]
83	      },
84	      {
85	        "name": "Table 2: One-Sided vs Two-Sided Detection Comparison",
86	        "columns": [
87	          "method",
88	          "total_flagged",
89	          "partial_contam_detected",
90	          "full_contam_detected",
91	          "FDR_control"
92	        ],
93	        "key_rows": [
94	          [
95	            "one-sided (lz* < threshold)",
96	            2,
97	            2,
98	            0,
99	            "0.05"
100	          ],
101	          [
102	            "two-sided (|lz*| > threshold)",
103	            4,
104	            2,
105	            2,
106	            "0.05"
107	          ]
108	        ]
109	      }
110	    ],
111	    "figures": [],
112	    "analysis": "双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination 产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination 产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。 Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。\n\n\nGemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。 这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的\"偶尔失误\"模式不符。 负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz* << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power， 因为真阳性的 lz* 绝对值远超阈值（效应量极大）。\n"
113	  },
114	  {
115	    "name": "Extended Simulation (Inverted-U Characterization)",
116	    "description": "扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination 的 MLE boundary 处理，精确刻画 inverted-U 拐点。\n",
117	    "results": {
118	      "inverted_u_inflection_point_mmlu": 0.65,
119	      "inverted_u_inflection_point_hellaswag": 0.6,
120	      "inverted_u_inflection_point_gsm8k": 0.7,
121	      "inverted_u_inflection_ci_range": "[0.55, 0.75]",
122	      "lz_star_at_inflection_mmlu": -0.12,
123	      "lz_star_at_100pct_contam_mmlu": 28.5,
124	      "lz_star_at_100pct_contam_hellaswag": 18.2,
125	      "lz_star_at_100pct_contam_gsm8k": 8.7,
126	      "negative_peak_lz_at_15pct_mmlu": -8.3,
127	      "negative_peak_lz_at_25pct_mmlu": -12.1,
128	      "zero_crossing_contam_level_mmlu": 0.63,
129	      "zero_crossing_contam_level_hellaswag": 0.58,
130	      "nan_rate_after_boundary_fix": 0.0,
131	      "power_at_5pct_contam_mmlu": 0.78,
132	      "power_at_5pct_contam_hellaswag": 0.34
133	    },
134	    "tables": [
135	      {
136	        "name": "Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)",
137	        "columns": [
138	          "contam_level",
139	          "mmlu_lz_mean",
140	          "mmlu_lz_sd",
141	          "hellaswag_lz_mean",
142	          "gsm8k_lz_mean",
143	          "arc_c_lz_mean"
144	        ],
145	        "key_rows": [
146	          [
147	            "0%",
148	            0.01,
149	            1.02,
150	            0.03,
151	            -0.02,
152	            0.01
153	          ],
154	          [
155	            "5%",
156	            -3.41,
157	            1.15,
158	            -1.82,
159	            -1.34,
160	            -0.42
161	          ],
162	          [
163	            "10%",
164	            -6.12,
165	            1.28,
166	            -3.45,
167	            -2.51,
168	            -0.78
169	          ],
170	          [
171	            "15%",
172	            -8.31,
173	            1.41,
174	            -4.72,
175	            -3.38,
176	            -1.02
177	          ],
178	          [
179	            "25%",
180	            -12.08,
181	            1.67,
182	            -6.21,
183	            -4.53,
184	            -1.31
185	          ],
186	          [
187	            "50%",
188	            -5.73,
189	            2.14,
190	            -2.89,
191	            -1.67,
192	            -0.43
193	          ],
194	          [
195	            "60%",
196	            -1.24,
197	            2.31,
198	            0.82,
199	            -0.34,
200	            0.21
201	          ],
202	          [
203	            "75%",
204	            8.42,
205	            2.53,
206	            5.67,
207	            3.21,
208	            1.12
209	          ],
210	          [
211	            "90%",
212	            19.31,
213	            2.87,
214	            12.45,
215	            6.78,
216	            2.34
217	          ],
218	          [
219	            "100%",
220	            28.5,
221	            3.12,
222	            18.2,
223	            8.7,
224	            3.01
225	          ]
226	        ]
227	      },
228	      {
229	        "name": "Table 4: Two-Sided Power at Various Contamination Levels",
230	        "columns": [
231	          "contam_level",
232	          "mmlu_power",
233	          "hellaswag_power",
234	          "gsm8k_power",
235	          "arc_c_power"
236	        ],
237	        "key_rows": [
238	          [
239	            "5%",
240	            0.78,
241	            0.34,
242	            0.22,
243	            0.06
244	          ],
245	          [
246	            "15%",
247	            0.979,
248	            0.733,
249	            0.578,
250	            0.129
251	          ],
252	          [
253	            "25%",
254	            0.998,
255	            0.891,
256	            0.743,
257	            0.201
258	          ],
259	          [
260	            "50%",
261	            0.872,
262	            0.514,
263	            0.298,
264	            0.08
265	          ],
266	          [
267	            "75%",
268	            0.991,
269	            0.934,
270	            0.712,
271	            0.187
272	          ],
273	          [
274	            "100%",
275	            1.0,
276	            0.998,
277	            0.962,
278	            0.478
279	          ]
280	        ]
281	      }
282	    ],
283	    "figures": [],
284	    "analysis": "Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty 分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分 replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*， 与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。\n\n\nInverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz* < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 \"全部答对\" 开始被 IRT 模型解释为 \"该模型能力更高\"，θ 估计上移，lz* 绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个 θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 \"合理\"，所以拐点在 0.65。GSM8K 难度更集中，拐点在 0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz* 的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz* 仍可计算（只是值更极端）。\n"
285	  },
286	  {
287	    "name": "Controlled Contamination Experiment",
288	    "description": "在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，建立 ground-truth contamination → lz* 映射。\n",
289	    "results": {
290	      "ctrl_contam_auroc_at_15pct": 0.96,
291	      "ctrl_contam_auroc_at_5pct": 0.82,
292	      "ctrl_contam_auroc_at_25pct": 0.99,
293	      "ctrl_contam_min_detectable_level": 0.05,
294	      "ctrl_contam_lz_effect_size_cohens_d_at_15pct": 2.3,
295	      "ctrl_contam_lz_effect_size_cohens_d_at_5pct": 1.1,
296	      "qwen_clean_lz_star_mmlu": 0.08,
297	      "qwen_5pct_lz_star_mmlu": -3.72,
298	      "qwen_10pct_lz_star_mmlu": -6.45,
299	      "qwen_15pct_lz_star_mmlu": -8.91,
300	      "qwen_25pct_lz_star_mmlu": -11.34,
301	      "qwen_50pct_lz_star_mmlu": -4.82,
302	      "gemma_clean_lz_star_mmlu": 0.15,
303	      "gemma_5pct_lz_star_mmlu": -3.21,
304	      "gemma_15pct_lz_star_mmlu": -7.63,
305	      "gemma_50pct_lz_star_mmlu": -5.14,
306	      "accuracy_lift_at_15pct_contam_qwen": 0.043,
307	      "accuracy_lift_at_15pct_contam_gemma": 0.038,
308	      "sft_generalization_ratio": 0.12,
309	      "contaminated_items_accuracy_lift": 0.31,
310	      "non_contaminated_items_accuracy_change": 0.014,
311	      "false_positive_rate_at_alpha_0.05": 0.038
312	    },
313	    "tables": [
314	      {
315	        "name": "Table 5: Controlled Contamination — lz* by Model and Contamination Level (MMLU)",
316	        "columns": [
317	          "model",
318	          "contam_level",
319	          "accuracy",
320	          "theta_hat",
321	          "lz_star_mean",
322	          "lz_star_sd",
323	          "flagged_rate_alpha005"
324	        ],
325	        "key_rows": [
326	          [
327	            "Qwen3.5-9B",
328	            "0%",
329	            0.721,
330	            1.42,
331	            0.08,
332	            0.97,
333	            0.047
334	          ],
335	          [
336	            "Qwen3.5-9B",
337	            "5%",
338	            0.738,
339	            1.51,
340	            -3.72,
341	            1.21,
342	            0.82
343	          ],
344	          [
345	            "Qwen3.5-9B",
346	            "10%",
347	            0.756,
348	            1.59,
349	            -6.45,
350	            1.34,
351	            0.94
352	          ],
353	          [
354	            "Qwen3.5-9B",
355	            "15%",
356	            0.764,
357	            1.63,
358	            -8.91,
359	            1.42,
360	            0.97
361	          ],
362	          [
363	            "Qwen3.5-9B",
364	            "25%",
365	            0.787,
366	            1.71,
367	            -11.34,
368	            1.58,
369	            0.99
370	          ],
371	          [
372	            "Qwen3.5-9B",
373	            "50%",
374	            0.831,
375	            1.89,
376	            -4.82,
377	            2.08,
378	            0.87
379	          ],
380	          [
381	            "Gemma-4-31B",
382	            "0%",
383	            0.793,
384	            1.81,
385	            0.15,
386	            0.94,
387	            0.041
388	          ],
389	          [
390	            "Gemma-4-31B",
391	            "5%",
392	            0.808,
393	            1.88,
394	            -3.21,
395	            1.18,
396	            0.78
397	          ],
398	          [
399	            "Gemma-4-31B",
400	            "15%",
401	            0.831,
402	            1.97,
403	            -7.63,
404	            1.38,
405	            0.95
406	          ],
407	          [
408	            "Gemma-4-31B",
409	            "50%",
410	            0.874,
411	            2.14,
412	            -5.14,
413	            2.01,
414	            0.84
415	          ]
416	        ]
417	      },
418	      {
419	        "name": "Table 6: Detection Performance (AUROC) by Contamination Level",
420	        "columns": [
421	          "contam_level",
422	          "auroc_qwen",
423	          "auroc_gemma",
424	          "auroc_pooled",
425	          "cohens_d_pooled"
426	        ],
427	        "key_rows": [
428	          [
429	            "5%",
430	            0.84,
431	            0.8,
432	            0.82,
433	            1.1
434	          ],
435	          [
436	            "10%",
437	            0.93,
438	            0.91,
439	            0.92,
440	            1.8
441	          ],
442	          [
443	            "15%",
444	            0.97,
445	            0.95,
446	            0.96,
447	            2.3
448	          ],
449	          [
450	            "25%",
451	            0.99,
452	            0.98,
453	            0.99,
454	            2.8
455	          ],
456	          [
457	            "50%",
458	            0.94,
459	            0.91,
460	            0.93,
461	            1.6
462	          ]
463	        ]
464	      },
465	      {
466	        "name": "Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs Non-Contaminated Items",
467	        "columns": [
468	          "contam_level",
469	          "contam_items_acc_before",
470	          "contam_items_acc_after",
471	          "contam_items_lift",
472	          "non_contam_items_acc_before",
473	          "non_contam_items_acc_after",
474	          "non_contam_items_lift"
475	        ],
476	        "key_rows": [
477	          [
478	            "5%",
479	            0.56,
480	            0.87,
481	            0.31,
482	            0.73,
483	            0.74,
484	            0.014
485	          ],
486	          [
487	            "15%",
488	            0.54,
489	            0.84,
490	            0.3,
491	            0.73,
492	            0.75,
493	            0.018
494	          ],
495	          [
496	            "25%",
497	            0.55,
498	            0.86,
499	            0.31,
500	            0.73,
501	            0.76,
502	            0.024
503	          ],
504	          [
505	            "50%",
506	            0.57,
507	            0.88,
508	            0.31,
509	            0.73,
510	            0.77,
511	            0.037
512	          ]
513	        ]
514	      }
515	    ],
516	    "figures": [],
517	    "analysis": "控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的 person-misfit 信号，Cohen's d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination 即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了 inverted-U，与扩展模拟定量一致。\n\n\nSFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入 items 仅有微弱泛化（+1.4%）。这种\"选择性提升\"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的 non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且 benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen's d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15% 意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为 MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。\n"
518	  },
519	  {
520	    "name": "Power Theory Derivation",
521	    "description": "推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将 inverted-U 升级为理论命题。\n",
522	    "results": {
523	      "power_theory_r_squared": 0.97,
524	      "power_formula": "power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean] per item",
525	      "inverted_u_inflection_formula": "c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i)) | contam=c] − E_θ[...| contam=0]|",
526	      "predicted_inflection_mmlu": 0.64,
527	      "predicted_inflection_hellaswag": 0.59,
528	      "predicted_inflection_gsm8k": 0.68,
529	      "observed_inflection_mmlu": 0.65,
530	      "observed_inflection_hellaswag": 0.6,
531	      "observed_inflection_gsm8k": 0.7,
532	      "inflection_prediction_error": 0.02,
533	      "power_at_n100_15pct_predicted": 0.089,
534	      "power_at_n1000_15pct_predicted": 0.491,
535	      "power_at_n5000_15pct_predicted": 0.862,
536	      "power_at_n14000_15pct_predicted": 0.981,
537	      "min_n_for_80pct_power_at_15pct": 3200,
538	      "min_n_for_80pct_power_at_5pct": 9800
539	    },
540	    "tables": [
541	      {
542	        "name": "Table 8: Theoretical vs Simulated Power (15% Contamination)",
543	        "columns": [
544	          "n_items",
545	          "predicted_power",
546	          "simulated_power",
547	          "absolute_error"
548	        ],
549	        "key_rows": [
550	          [
551	            100,
552	            0.089,
553	            0.092,
554	            0.003
555	          ],
556	          [
557	            500,
558	            0.312,
559	            0.298,
560	            0.014
561	          ],
562	          [
563	            1000,
564	            0.491,
565	            0.503,
566	            0.012
567	          ],
568	          [
569	            1319,
570	            0.578,
571	            0.578,
572	            0.0
573	          ],
574	          [
575	            5000,
576	            0.862,
577	            0.851,
578	            0.011
579	          ],
580	          [
581	            10042,
582	            0.964,
583	            0.958,
584	            0.006
585	          ],
586	          [
587	            14042,
588	            0.981,
589	            0.979,
590	            0.002
591	          ]
592	        ]
593	      },
594	      {
595	        "name": "Table 9: Inverted-U Inflection Point — Predicted vs Observed",
596	        "columns": [
597	          "benchmark",
598	          "n_items",
599	          "difficulty_sd",
600	          "predicted_inflection",
601	          "observed_inflection",
602	          "abs_error"
603	        ],
604	        "key_rows": [
605	          [
606	            "MMLU",
607	            14042,
608	            1.83,
609	            0.64,
610	            0.65,
611	            0.01
612	          ],
613	          [
614	            "HellaSwag",
615	            10042,
616	            1.52,
617	            0.59,
618	            0.6,
619	            0.01
620	          ],
621	          [
622	            "GSM8K",
623	            1319,
624	            1.21,
625	            0.68,
626	            0.7,
627	            0.02
628	          ],
629	          [
630	            "ARC-C",
631	            1172,
632	            1.45,
633	            0.62,
634	            0.64,
635	            0.02
636	          ],
637	          [
638	            "HumanEval",
639	            164,
640	            1.67,
641	            0.61,
642	            0.63,
643	            0.02
644	          ]
645	        ]
646	      },
647	      {
648	        "name": "Table 10: Minimum n_items for 80% Power at Various Contamination Levels",
649	        "columns": [
650	          "contam_level",
651	          "min_n_theoretical",
652	          "min_n_simulated"
653	        ],
654	        "key_rows": [
655	          [
656	            "5%",
657	            9800,
658	            10200
659	          ],
660	          [
661	            "10%",
662	            4700,
663	            4900
664	          ],
665	          [
666	            "15%",
667	            3200,
668	            3350
669	          ],
670	          [
671	            "25%",
672	            1800,
673	            1900
674	          ]
675	        ]
676	      }
677	    ],
678	    "figures": [],
679	    "analysis": "Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15% 污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有 12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty 分布预测拐点位置，误差仅 1-2 个百分点。\n\n\nSnijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination 时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移 ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于 c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL 模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得 response pattern 看起来 \"最合理\" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。\n"
680	  },
681	  {
682	    "name": "Leaderboard Audit (Large-Scale Scan)",
683	    "description": "Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算 person-fit，绘制 per-benchmark 污染率随时间趋势。\n",
684	    "results": {
685	      "leaderboard_models_scanned": 2847,
686	      "leaderboard_models_with_per_item_logs": 0,
687	      "leaderboard_models_rerun_inference": 2847,
688	      "total_gpu_hours_inference": 18.5,
689	      "leaderboard_flagged_rate_overall": 0.12,
690	      "leaderboard_flagged_rate_mmlu": 0.15,
691	      "leaderboard_flagged_rate_hellaswag": 0.09,
692	      "leaderboard_flagged_rate_arc_c": 0.07,
693	      "leaderboard_flagged_rate_gsm8k": 0.11,
694	      "flagged_models_total": 342,
695	      "flagged_two_sided_positive": 87,
696	      "flagged_two_sided_negative": 255,
697	      "contamination_trend_increasing": true,
698	      "contamination_rate_2023q1": 0.06,
699	      "contamination_rate_2023q3": 0.11,
700	      "contamination_rate_2024q1": 0.18,
701	      "cross_benchmark_consistent_flag_rate": 0.34,
702	      "top_flagged_model_lz_star": -22.4
703	    },
704	    "tables": [
705	      {
706	        "name": "Table 11: Leaderboard Audit Summary",
707	        "columns": [
708	          "benchmark",
709	          "models_scanned",
710	          "flagged_negative",
711	          "flagged_positive",
712	          "flagged_rate",
713	          "median_lz_star_flagged"
714	        ],
715	        "key_rows": [
716	          [
717	            "MMLU",
718	            2847,
719	            312,
720	            115,
721	            0.15,
722	            -6.73
723	          ],
724	          [
725	            "HellaSwag",
726	            2847,
727	            198,
728	            58,
729	            0.09,
730	            -4.21
731	          ],
732	          [
733	            "ARC-C",
734	            2847,
735	            142,
736	            57,
737	            0.07,
738	            -3.12
739	          ],
740	          [
741	            "GSM8K",
742	            2182,
743	            178,
744	            63,
745	            0.11,
746	            -5.42
747	          ],
748	          [
749	            "Overall (any benchmark)",
750	            2847,
751	            255,
752	            87,
753	            0.12,
754	            "—"
755	          ]
756	        ]
757	      },
758	      {
759	        "name": "Table 12: Contamination Rate by Time Period",
760	        "columns": [
761	          "period",
762	          "models_in_period",
763	          "flagged_count",
764	          "flagged_rate"
765	        ],
766	        "key_rows": [
767	          [
768	            "2023 Q1-Q2",
769	            487,
770	            29,
771	            0.06
772	          ],
773	          [
774	            "2023 Q3-Q4",
775	            891,
776	            98,
777	            0.11
778	          ],
779	          [
780	            "2024 Q1-Q2",
781	            1103,
782	            198,
783	            0.18
784	          ],
785	          [
786	            "2024 Q3+",
787	            366,
788	            51,
789	            0.14
790	          ]
791	        ]
792	      },
793	      {
794	        "name": "Table 13: Top 10 Most Anomalous Models",
795	        "columns": [
796	          "model",
797	          "benchmark",
798	          "accuracy",
799	          "theta",
800	          "lz_star",
801	          "side",
802	          "params"
803	        ],
804	        "key_rows": [
805	          [
806	            "anonymous-7b-v3",
807	            "MMLU",
808	            0.847,
809	            1.23,
810	            -22.4,
811	            "negative",
812	            "7B"
813	          ],
814	          [
815	            "llm-finetune-2b",
816	            "MMLU",
817	            0.912,
818	            1.45,
819	            18.7,
820	            "positive",
821	            "2B"
822	          ],
823	          [
824	            "benchmark-tuned-3b",
825	            "GSM8K",
826	            0.891,
827	            2.12,
828	            -17.3,
829	            "negative",
830	            "3B"
831	          ]
832	        ]
833	      }
834	    ],
835	    "figures": [],
836	    "analysis": "Leaderboard audit 是 IRT-FIT 的 \"killer app\"——唯一只需要 binary response data 的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要 logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342 个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到 7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。\n\n\nPer-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存 aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847 个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是 benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%） 因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1 升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024 等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 \"suspicious near-ceiling\" 模型， 负侧 flagged（255 个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged 模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。\n"
837	  },
838	  {
839	    "name": "4PL vs 3PL Ablation",
840	    "description": "比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对 false alarm 和 detection power 的影响。\n",
841	    "results": {
842	      "auroc_4pl_15pct": 0.96,
843	      "auroc_3pl_15pct": 0.91,
844	      "auroc_difference_15pct": 0.05,
845	      "false_alarm_rate_4pl": 0.042,
846	      "false_alarm_rate_3pl": 0.078,
847	      "power_4pl_15pct_mmlu": 0.979,
848	      "power_3pl_15pct_mmlu": 0.934,
849	      "power_difference_15pct_mmlu": 0.045,
850	      "mean_abs_lz_star_difference_clean": 0.34,
851	      "mean_abs_lz_star_difference_contam": 0.87,
852	      "d_parameter_mean_psn_irt": 0.91,
853	      "d_parameter_sd_psn_irt": 0.08,
854	      "items_where_d_matters_most": "top-difficulty items (difficulty > 2.5) where d < 0.85"
855	    },
856	    "tables": [
857	      {
858	        "name": "Table 14: 4PL vs 3PL Detection Performance Comparison",
859	        "columns": [
860	          "metric",
861	          "4PL",
862	          "3PL(d=1)",
863	          "difference"
864	        ],
865	        "key_rows": [
866	          [
867	            "AUROC @ 15%",
868	            0.96,
869	            0.91,
870	            "+0.05"
871	          ],
872	          [
873	            "False Alarm Rate (α=0.05)",
874	            0.042,
875	            0.078,
876	            "−0.036"
877	          ],
878	          [
879	            "Power @ 15% MMLU",
880	            0.979,
881	            0.934,
882	            "+0.045"
883	          ],
884	          [
885	            "Power @ 5% MMLU",
886	            0.78,
887	            0.69,
888	            "+0.09"
889	          ],
890	          [
891	            "Mean |lz*| clean models",
892	            0.83,
893	            1.17,
894	            "−0.34"
895	          ],
896	          [
897	            "Mean |lz*| contam models (15%)",
898	            8.91,
899	            8.04,
900	            "+0.87"
901	          ]
902	        ]
903	      },
904	      {
905	        "name": "Table 15: Impact of d Parameter by Item Difficulty Band",
906	        "columns": [
907	          "difficulty_band",
908	          "n_items",
909	          "mean_d",
910	          "lz_star_diff_clean",
911	          "lz_star_diff_contam"
912	        ],
913	        "key_rows": [
914	          [
915	            "< 0.5 (easy)",
916	            2814,
917	            0.97,
918	            -0.08,
919	            0.12
920	          ],
921	          [
922	            "0.5–1.5",
923	            5621,
924	            0.93,
925	            -0.21,
926	            0.43
927	          ],
928	          [
929	            "1.5–2.5",
930	            3891,
931	            0.89,
932	            -0.38,
933	            0.78
934	          ],
935	          [
936	            "> 2.5 (hard)",
937	            1716,
938	            0.82,
939	            -0.67,
940	            1.45
941	          ]
942	        ]
943	      }
944	    ],
945	    "figures": [],
946	    "analysis": "4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL 也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items 恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模 在检测任务中有非平凡的价值。\n\n\n4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生 也可能答错某些 items 的现象——在 LLM 场景中对应\"某些 items 的表述/格式导致即使知道答案的模型也可能选错\"。 当 d < 1 时，3PL(d=1) 会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 \"aberrant\" 信号（false alarm 上升）。 4PL 通过让 d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的 items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model 的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。 差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。\n"
947	  },
948	  {
949	    "name": "Baseline Comparison (ConStat, Min-K%++)",
950	    "description": "在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++ 的 AUROC 和 Type-I error。\n",
951	    "results": {
952	      "irt_fit_auroc_15pct": 0.96,
953	      "constat_auroc_15pct": 0.83,
954	      "min_k_pp_auroc_15pct": 0.88,
955	      "irt_fit_auroc_5pct": 0.82,
956	      "constat_auroc_5pct": 0.61,
957	      "min_k_pp_auroc_5pct": 0.72,
958	      "auroc_advantage_vs_constat_15pct": 0.13,
959	      "auroc_advantage_vs_minkpp_15pct": 0.08,
960	      "baseline_auroc_advantage_vs_constat": 0.1,
961	      "type_i_error_irt_fit": 0.042,
962	      "type_i_error_constat": 0.053,
963	      "type_i_error_min_k_pp": 0.048,
964	      "irt_fit_information_required": "binary responses only",
965	      "constat_information_required": "binary responses + re-test capability",
966	      "min_k_pp_information_required": "token-level log-probabilities",
967	      "irt_fit_unique_advantage": "operates without model access"
968	    },
969	    "tables": [
970	      {
971	        "name": "Table 16: Baseline Comparison — Detection Performance on Controlled Contamination",
972	        "columns": [
973	          "method",
974	          "info_required",
975	          "auroc_5pct",
976	          "auroc_15pct",
977	          "auroc_25pct",
978	          "type_i_error"
979	        ],
980	        "key_rows": [
981	          [
982	            "IRT-FIT (lz*, two-sided)",
983	            "binary responses",
984	            0.82,
985	            0.96,
986	            0.99,
987	            0.042
988	          ],
989	          [
990	            "ConStat",
991	            "binary + re-test",
992	            0.61,
993	            0.83,
994	            0.91,
995	            0.053
996	          ],
997	          [
998	            "Min-K%++",
999	            "token log-probs",
1000	            0.72,
1001	            0.88,
1002	            0.95,
1003	            0.048
1004	          ]
1005	        ]
1006	      },
1007	      {
1008	        "name": "Table 17: Detection Frontier — Information Access vs Detection Power",
1009	        "columns": [
1010	          "information_level",
1011	          "method",
1012	          "auroc_15pct",
1013	          "scalability"
1014	        ],
1015	        "key_rows": [
1016	          [
1017	            "binary responses only",
1018	            "IRT-FIT",
1019	            0.96,
1020	            "any model with public scores"
1021	          ],
1022	          [
1023	            "binary + re-test",
1024	            "ConStat",
1025	            0.83,
1026	            "requires live model access"
1027	          ],
1028	          [
1029	            "token probabilities",
1030	            "Min-K%++",
1031	            0.88,
1032	            "requires API with logprobs"
1033	          ],
1034	          [
1035	            "training data",
1036	            "n-gram overlap",
1037	            "—",
1038	            "requires training data access"
1039	          ],
1040	          [
1041	            "model weights",
1042	            "internal probing",
1043	            "—",
1044	            "requires open weights"
1045	          ]
1046	        ]
1047	      }
1048	    ],
1049	    "figures": [],
1050	    "analysis": "Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT 在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为 person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。\n\n\nIRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility 参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的 re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test 分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的 person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT 不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。\n"
1051	  },
1052	  {
1053	    "name": "Multiscale lzm Statistic",
1054	    "description": "实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*， 在 PSN-IRT 12 模型 + 控制实验模型上验证。\n",
1055	    "results": {
1056	      "lzm_auroc_15pct": 0.98,
1057	      "lzm_vs_single_benchmark_auroc_gain": 0.02,
1058	      "lzm_cross_benchmark_correlation": 0.67,
1059	      "gemini15_lzm": 18.42,
1060	      "gpt4_lzm": -0.87,
1061	      "clean_model_lzm_mean": 0.03,
1062	      "clean_model_lzm_sd": 0.91,
1063	      "contam_model_lzm_mean_15pct": -7.23,
1064	      "lzm_null_ks_p": 0.312,
1065	      "lzm_power_at_15pct_pooled": 0.99
1066	    },
1067	    "tables": [
1068	      {
1069	        "name": "Table 18: lzm Results — PSN-IRT 12 Models",
1070	        "columns": [
1071	          "model",
1072	          "lzm_value",
1073	          "flagged_alpha005",
1074	          "n_benchmarks_individual_flag"
1075	        ],
1076	        "key_rows": [
1077	          [
1078	            "Gemini-1.5",
1079	            18.42,
1080	            "YES",
1081	            3
1082	          ],
1083	          [
1084	            "GPT-4",
1085	            -0.87,
1086	            "no",
1087	            0
1088	          ],
1089	          [
1090	            "Llama-2-70B",
1091	            -3.21,
1092	            "YES",
1093	            1
1094	          ],
1095	          [
1096	            "Claude-3-Opus",
1097	            0.42,
1098	            "no",
1099	            0
1100	          ],
1101	          [
1102	            "Mistral-7B",
1103	            -2.45,
1104	            "no",
1105	            0
1106	          ]
1107	        ]
1108	      },
1109	      {
1110	        "name": "Table 19: lzm vs Single-Benchmark Detection Power",
1111	        "columns": [
1112	          "method",
1113	          "auroc_15pct",
1114	          "power_at_15pct",
1115	          "false_alarm_rate"
1116	        ],
1117	        "key_rows": [
1118	          [
1119	            "lz* (MMLU only)",
1120	            0.96,
1121	            0.979,
1122	            0.042
1123	          ],
1124	          [
1125	            "lz* (best single benchmark)",
1126	            0.96,
1127	            0.979,
1128	            0.042
1129	          ],
1130	          [
1131	            "lzm (all benchmarks)",
1132	            0.98,
1133	            0.99,
1134	            0.037
1135	          ]
1136	        ]
1137	      }
1138	    ],
1139	    "figures": [],
1140	    "analysis": "lzm 是一个稳健的 \"overall contamination index\"，特别适合 leaderboard audit 场景—— 单一指标告诉你 \"这个模型总体上是否可疑\"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision 提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark 到多 benchmark 无缝聚合。\n\n\nlzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个 benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98 是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark 一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark 上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval 上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有 benchmark 上都是 \"正常\" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models 上确实近似 N(0,1)。\n"
1141	  },
1142	  {
1143	    "name": "Post-RL Hypothesis Test",
1144	    "description": "在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在 RL 后保持检测力。\n",
1145	    "results": {
1146	      "pre_rl_lz_star": -8.91,
1147	      "post_rl_lz_star": -7.12,
1148	      "post_rl_power_retention_ratio": 0.84,
1149	      "post_rl_auroc": 0.92,
1150	      "pre_rl_auroc": 0.96,
1151	      "auroc_drop_after_rl": 0.04,
1152	      "post_rl_accuracy_change": 0.012,
1153	      "post_rl_contam_items_accuracy": 0.82,
1154	      "pre_rl_contam_items_accuracy": 0.84,
1155	      "post_rl_non_contam_items_accuracy": 0.75,
1156	      "pre_rl_non_contam_items_accuracy": 0.74,
1157	      "post_rl_theta_shift": 0.08,
1158	      "mia_post_rl_auroc": 0.54,
1159	      "mia_pre_rl_auroc": 0.71,
1160	      "person_fit_vs_mia_advantage_post_rl": 0.38
1161	    },
1162	    "tables": [
1163	      {
1164	        "name": "Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)",
1165	        "columns": [
1166	          "stage",
1167	          "accuracy",
1168	          "theta",
1169	          "lz_star",
1170	          "auroc",
1171	          "power"
1172	        ],
1173	        "key_rows": [
1174	          [
1175	            "Clean baseline",
1176	            0.721,
1177	            1.42,
1178	            0.08,
1179	            "—",
1180	            "—"
1181	          ],
1182	          [
1183	            "Post-SFT (contaminated)",
1184	            0.764,
1185	            1.63,
1186	            -8.91,
1187	            0.96,
1188	            0.97
1189	          ],
1190	          [
1191	            "Post-SFT + GRPO",
1192	            0.776,
1193	            1.71,
1194	            -7.12,
1195	            0.92,
1196	            0.91
1197	          ]
1198	        ]
1199	      },
1200	      {
1201	        "name": "Table 21: Person-Fit vs MIA — Post-RL Robustness",
1202	        "columns": [
1203	          "method",
1204	          "pre_rl_auroc",
1205	          "post_rl_auroc",
1206	          "auroc_retention",
1207	          "info_required"
1208	        ],
1209	        "key_rows": [
1210	          [
1211	            "IRT-FIT (lz*)",
1212	            0.96,
1213	            0.92,
1214	            "96%",
1215	            "binary responses"
1216	          ],
1217	          [
1218	            "Min-K%++",
1219	            0.88,
1220	            0.62,
1221	            "70%",
1222	            "token log-probs"
1223	          ],
1224	          [
1225	            "MIA (reference-based)",
1226	            0.71,
1227	            0.54,
1228	            "76%",
1229	            "token log-probs + ref model"
1230	          ]
1231	        ]
1232	      },
1233	      {
1234	        "name": "Table 22: Item-Level Analysis — Accuracy Change After GRPO",
1235	        "columns": [
1236	          "item_type",
1237	          "pre_rl_accuracy",
1238	          "post_rl_accuracy",
1239	          "change"
1240	        ],
1241	        "key_rows": [
1242	          [
1243	            "contaminated items",
1244	            0.84,
1245	            0.82,
1246	            -0.02
1247	          ],
1248	          [
1249	            "non-contaminated items",
1250	            0.74,
1251	            0.75,
1252	            0.01
1253	          ],
1254	          [
1255	            "contaminated hard items (diff>2)",
1256	            0.79,
1257	            0.76,
1258	            -0.03
1259	          ],
1260	          [
1261	            "non-contaminated hard items (diff>2)",
1262	            0.41,
1263	            0.43,
1264	            0.02
1265	          ]
1266	        ]
1267	      }
1268	    ],
1269	    "figures": [],
1270	    "analysis": "Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： \"MIA 在 post-RL 后失效（AUROC 0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but does not undo memorization of correct answers。\" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information 条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in robustness to distribution shift。\n\n\nGRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance）， 对已经答对的 contaminated items 不会产生\"遗忘\"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在 reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items 的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 \"预期外正确\" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接 memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54）， 因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit 信号就存在。这是 person-fit \"信息层级优势\" 的直接体现： binary outcome 比 token probability 更鲁棒，因为 RL 可以改变 \"how confident the model is\" 但很难改变 \"whether it gets the answer right\" on memorized items.\n"
1271	  },
1272	  {
1273	    "name": "Extra Benchmarks (BBH, MATH)",
1274	    "description": "添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\n",
1275	    "results": {
1276	      "bbh_n_items": 6511,
1277	      "math_n_items": 5000,
1278	      "bbh_power_at_15pct": 0.89,
1279	      "math_power_at_15pct": 0.84,
1280	      "bbh_power_at_5pct": 0.52,
1281	      "math_power_at_5pct": 0.44,
1282	      "bbh_predicted_power_from_theory": 0.88,
1283	      "math_predicted_power_from_theory": 0.83,
1284	      "theory_prediction_error_bbh": 0.01,
1285	      "theory_prediction_error_math": 0.01,
1286	      "bbh_inverted_u_inflection": 0.62,
1287	      "math_inverted_u_inflection": 0.66,
1288	      "power_gap_1k_10k_filled": true
1289	    },
1290	    "tables": [
1291	      {
1292	        "name": "Table 23: Power Gap Analysis — All 7 Benchmarks",
1293	        "columns": [
1294	          "benchmark",
1295	          "n_items",
1296	          "power_at_15pct_simulated",
1297	          "power_at_15pct_predicted",
1298	          "power_at_5pct"
1299	        ],
1300	        "key_rows": [
1301	          [
1302	            "HumanEval",
1303	            164,
1304	            0.243,
1305	            0.231,
1306	            0.07
1307	          ],
1308	          [
1309	            "ARC-C",
1310	            1172,
1311	            0.129,
1312	            0.142,
1313	            0.04
1314	          ],
1315	          [
1316	            "GSM8K",
1317	            1319,
1318	            0.578,
1319	            0.561,
1320	            0.22
1321	          ],
1322	          [
1323	            "MATH",
1324	            5000,
1325	            0.84,
1326	            0.83,
1327	            0.44
1328	          ],
1329	          [
1330	            "BBH",
1331	            6511,
1332	            0.89,
1333	            0.88,
1334	            0.52
1335	          ],
1336	          [
1337	            "HellaSwag",
1338	            10042,
1339	            0.733,
1340	            0.748,
1341	            0.34
1342	          ],
1343	          [
1344	            "MMLU",
1345	            14042,
1346	            0.979,
1347	            0.981,
1348	            0.78
1349	          ]
1350	        ]
1351	      }
1352	    ],
1353	    "figures": [],
1354	    "analysis": "BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval) 到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97 推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319 items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item 体现。\n\n\nBBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042 ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH 的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH 难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ 参数化吸收了这些差异。\n"
1355	  },
1356	  {
1357	    "name": "Domain-Level Analysis (MMLU)",
1358	    "description": "按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。\n",
1359	    "results": {
1360	      "n_domains_analyzed": 57,
1361	      "domains_with_extreme_lz_star": 57,
1362	      "gemini15_domain_lz_star_range": "[+0.8, +12.3]",
1363	      "gemini15_domain_lz_star_mean": 4.21,
1364	      "gemini15_domain_lz_star_sd": 2.87,
1365	      "gemini15_most_aberrant_domain": "abstract_algebra",
1366	      "gemini15_least_aberrant_domain": "high_school_mathematics",
1367	      "contamination_pattern": "uniform across all domains",
1368	      "domain_level_power_mean": 0.34,
1369	      "domain_level_power_max": 0.72,
1370	      "domain_level_n_items_range": "[100, 1534]",
1371	      "gpt4_domain_lz_star_sd": 0.82,
1372	      "gpt4_domains_flagged": 0
1373	    },
1374	    "tables": [
1375	      {
1376	        "name": "Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)",
1377	        "columns": [
1378	          "domain",
1379	          "n_items",
1380	          "gemini15_acc",
1381	          "gemini15_lz_star",
1382	          "gpt4_acc",
1383	          "gpt4_lz_star"
1384	        ],
1385	        "key_rows": [
1386	          [
1387	            "abstract_algebra",
1388	            100,
1389	            1.0,
1390	            0.83,
1391	            0.73,
1392	            -0.42
1393	          ],
1394	          [
1395	            "professional_medicine",
1396	            272,
1397	            1.0,
1398	            4.21,
1399	            0.851,
1400	            0.67
1401	          ],
1402	          [
1403	            "high_school_mathematics",
1404	            270,
1405	            1.0,
1406	            2.14,
1407	            0.412,
1408	            -1.23
1409	          ],
1410	          [
1411	            "college_chemistry",
1412	            100,
1413	            1.0,
1414	            0.91,
1415	            0.47,
1416	            0.31
1417	          ],
1418	          [
1419	            "global_facts",
1420	            100,
1421	            1.0,
1422	            0.8,
1423	            0.38,
1424	            -0.87
1425	          ],
1426	          [
1427	            "...",
1428	            "...",
1429	            "...",
1430	            "...",
1431	            "...",
1432	            "..."
1433	          ],
1434	          [
1435	            "miscellaneous",
1436	            783,
1437	            1.0,
1438	            7.89,
1439	            0.872,
1440	            0.42
1441	          ],
1442	          [
1443	            "clinical_knowledge",
1444	            265,
1445	            1.0,
1446	            3.87,
1447	            0.792,
1448	            -0.18
1449	          ]
1450	        ]
1451	      },
1452	      {
1453	        "name": "Table 25: Domain-Level Power as Function of n_items",
1454	        "columns": [
1455	          "n_items_bin",
1456	          "n_domains",
1457	          "mean_power_at_15pct",
1458	          "predicted_from_theory"
1459	        ],
1460	        "key_rows": [
1461	          [
1462	            "100-150",
1463	            22,
1464	            0.18,
1465	            0.17
1466	          ],
1467	          [
1468	            "150-300",
1469	            21,
1470	            0.31,
1471	            0.33
1472	          ],
1473	          [
1474	            "300-600",
1475	            9,
1476	            0.52,
1477	            0.5
1478	          ],
1479	          [
1480	            "600-1000",
1481	            3,
1482	            0.64,
1483	            0.67
1484	          ],
1485	          [
1486	            ">1000",
1487	            2,
1488	            0.72,
1489	            0.74
1490	          ]
1491	        ]
1492	      }
1493	    ],
1494	    "figures": [],
1495	    "analysis": "Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据：\"uniform contamination across all 57 MMLU domains\" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization 的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power theory 提供了 57 个额外的 (n_items, power) 数据点。\n\nGemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz* 都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1) 各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty 分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty 分布的偏差更大。 \"uniform across all domains\" 的发现很重要：它排除了 \"Gemini-1.5 只是在特定领域特别强\" 的 innocent explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34 是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57 个 domain 相当于 57 个不同 n_items 的 \"实验\"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差 1.0），0 个 domain flagged， 作为干净的 negative control。\n"
1496	  }
1497	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bfd6c2a-d1f3-4307-bec5-de6c5343bb34",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "0d949ccd-6b24-4260-ba5b-b779cfb87f60",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Two-Sided Detection Framework\",\n    \"description\": \"基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。\\n\",\n    \"results\": {\n      \"gemini15_mmlu_lz_star\": 34.75,\n      \"gemini15_mmlu_lz_star_bootstrap_95ci\": \"[32.1, 37.4]\",\n      \"gemini15_gsm8k_lz_star\": -15.71,\n      \"gemini15_humaneval_lz_star\": -12.37,\n      \"two_sided_flagged_models_at_fdr_0.05\": 4,\n      \"one_sided_flagged_models_at_fdr_0.05\": 2,\n      \"incremental_detection_gain_two_vs_one_sided\": \"2 additional models flagged (Gemini-1.5 on MMLU, 1 other high-perf model)\",\n      \"optimal_negative_threshold_alpha_0.05\": -2.81,\n      \"optimal_positive_threshold_alpha_0.05\": 3.24,\n      \"positive_regime_models\": \"Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling model\",\n      \"negative_regime_models\": \"Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)\",\n        \"columns\": [\n          \"model\",\n          \"benchmark\",\n          \"accuracy\",\n          \"theta_hat\",\n          \"lz_star\",\n          \"side\",\n          \"flagged_bh_fdr_005\",\n          \"bootstrap_95ci\"\n        ],\n        \"key_rows\": [\n          [\n            \"Gemini-1.5\",\n            \"MMLU\",\n            1.0,\n            0.78,\n            34.75,\n            \"positive\",\n            \"YES\",\n            \"[32.1, 37.4]\"\n          ],\n          [\n            \"Gemini-1.5\",\n            \"GSM8K\",\n            0.946,\n            2.41,\n            -15.71,\n            \"negative\",\n            \"YES\",\n            \"[-17.2, -14.3]\"\n          ],\n          [\n            \"Gemini-1.5\",\n            \"HumanEval\",\n            0.878,\n            1.92,\n            -12.37,\n            \"negative\",\n            \"YES\",\n            \"[-14.1, -10.8]\"\n          ],\n          [\n            \"GPT-4\",\n            \"MMLU\",\n            0.864,\n            2.15,\n            -1.23,\n            \"—\",\n            \"no\",\n            \"[-2.1, -0.4]\"\n          ],\n          [\n            \"Llama-2-70B\",\n            \"ARC-C\",\n            0.673,\n            1.08,\n            -3.87,\n            \"negative\",\n            \"YES\",\n            \"[-5.2, -2.6]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: One-Sided vs Two-Sided Detection Comparison\",\n        \"columns\": [\n          \"method\",\n          \"total_flagged\",\n          \"partial_contam_detected\",\n          \"full_contam_detected\",\n          \"FDR_control\"\n        ],\n        \"key_rows\": [\n          [\n            \"one-sided (lz* < threshold)\",\n            2,\n            2,\n            0,\n            \"0.05\"\n          ],\n          [\n            \"two-sided (|lz*| > threshold)\",\n            4,\n            2,\n            2,\n            \"0.05\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination 产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination 产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。 Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。\\n\\n\\nGemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。 这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的\\\"偶尔失误\\\"模式不符。 负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz* << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power， 因为真阳性的 lz* 绝对值远超阈值（效应量极大）。\\n\"\n  },\n  {\n    \"name\": \"Extended Simulation (Inverted-U Characterization)\",\n    \"description\": \"扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination 的 MLE boundary 处理，精确刻画 inverted-U 拐点。\\n\",\n    \"results\": {\n      \"inverted_u_inflection_point_mmlu\": 0.65,\n      \"inverted_u_inflection_point_hellaswag\": 0.6,\n      \"inverted_u_inflection_point_gsm8k\": 0.7,\n      \"inverted_u_inflection_ci_range\": \"[0.55, 0.75]\",\n      \"lz_star_at_inflection_mmlu\": -0.12,\n      \"lz_star_at_100pct_contam_mmlu\": 28.5,\n      \"lz_star_at_100pct_contam_hellaswag\": 18.2,\n      \"lz_star_at_100pct_contam_gsm8k\": 8.7,\n      \"negative_peak_lz_at_15pct_mmlu\": -8.3,\n      \"negative_peak_lz_at_25pct_mmlu\": -12.1,\n      \"zero_crossing_contam_level_mmlu\": 0.63,\n      \"zero_crossing_contam_level_hellaswag\": 0.58,\n      \"nan_rate_after_boundary_fix\": 0.0,\n      \"power_at_5pct_contam_mmlu\": 0.78,\n      \"power_at_5pct_contam_hellaswag\": 0.34\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)\",\n        \"columns\": [\n          \"contam_level\",\n          \"mmlu_lz_mean\",\n          \"mmlu_lz_sd\",\n          \"hellaswag_lz_mean\",\n          \"gsm8k_lz_mean\",\n          \"arc_c_lz_mean\"\n        ],\n        \"key_rows\": [\n          [\n            \"0%\",\n            0.01,\n            1.02,\n            0.03,\n            -0.02,\n            0.01\n          ],\n          [\n            \"5%\",\n            -3.41,\n            1.15,\n            -1.82,\n            -1.34,\n            -0.42\n          ],\n          [\n            \"10%\",\n            -6.12,\n            1.28,\n            -3.45,\n            -2.51,\n            -0.78\n          ],\n          [\n            \"15%\",\n            -8.31,\n            1.41,\n            -4.72,\n            -3.38,\n            -1.02\n          ],\n          [\n            \"25%\",\n            -12.08,\n            1.67,\n            -6.21,\n            -4.53,\n            -1.31\n          ],\n          [\n            \"50%\",\n            -5.73,\n            2.14,\n            -2.89,\n            -1.67,\n            -0.43\n          ],\n          [\n            \"60%\",\n            -1.24,\n            2.31,\n            0.82,\n            -0.34,\n            0.21\n          ],\n          [\n            \"75%\",\n            8.42,\n            2.53,\n            5.67,\n            3.21,\n            1.12\n          ],\n          [\n            \"90%\",\n            19.31,\n            2.87,\n            12.45,\n            6.78,\n            2.34\n          ],\n          [\n            \"100%\",\n            28.5,\n            3.12,\n            18.2,\n            8.7,\n            3.01\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Two-Sided Power at Various Contamination Levels\",\n        \"columns\": [\n          \"contam_level\",\n          \"mmlu_power\",\n          \"hellaswag_power\",\n          \"gsm8k_power\",\n          \"arc_c_power\"\n        ],\n        \"key_rows\": [\n          [\n            \"5%\",\n            0.78,\n            0.34,\n            0.22,\n            0.06\n          ],\n          [\n            \"15%\",\n            0.979,\n            0.733,\n            0.578,\n            0.129\n          ],\n          [\n            \"25%\",\n            0.998,\n            0.891,\n            0.743,\n            0.201\n          ],\n          [\n            \"50%\",\n            0.872,\n            0.514,\n            0.298,\n            0.08\n          ],\n          [\n            \"75%\",\n            0.991,\n            0.934,\n            0.712,\n            0.187\n          ],\n          [\n            \"100%\",\n            1.0,\n            0.998,\n            0.962,\n            0.478\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty 分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分 replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*， 与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。\\n\\n\\nInverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz* < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 \\\"全部答对\\\" 开始被 IRT 模型解释为 \\\"该模型能力更高\\\"，θ 估计上移，lz* 绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个 θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 \\\"合理\\\"，所以拐点在 0.65。GSM8K 难度更集中，拐点在 0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz* 的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz* 仍可计算（只是值更极端）。\\n\"\n  },\n  {\n    \"name\": \"Controlled Contamination Experiment\",\n    \"description\": \"在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，建立 ground-truth contamination → lz* 映射。\\n\",\n    \"results\": {\n      \"ctrl_contam_auroc_at_15pct\": 0.96,\n      \"ctrl_contam_auroc_at_5pct\": 0.82,\n      \"ctrl_contam_auroc_at_25pct\": 0.99,\n      \"ctrl_contam_min_detectable_level\": 0.05,\n      \"ctrl_contam_lz_effect_size_cohens_d_at_15pct\": 2.3,\n      \"ctrl_contam_lz_effect_size_cohens_d_at_5pct\": 1.1,\n      \"qwen_clean_lz_star_mmlu\": 0.08,\n      \"qwen_5pct_lz_star_mmlu\": -3.72,\n      \"qwen_10pct_lz_star_mmlu\": -6.45,\n      \"qwen_15pct_lz_star_mmlu\": -8.91,\n      \"qwen_25pct_lz_star_mmlu\": -11.34,\n      \"qwen_50pct_lz_star_mmlu\": -4.82,\n      \"gemma_clean_lz_star_mmlu\": 0.15,\n      \"gemma_5pct_lz_star_mmlu\": -3.21,\n      \"gemma_15pct_lz_star_mmlu\": -7.63,\n      \"gemma_50pct_lz_star_mmlu\": -5.14,\n      \"accuracy_lift_at_15pct_contam_qwen\": 0.043,\n      \"accuracy_lift_at_15pct_contam_gemma\": 0.038,\n      \"sft_generalization_ratio\": 0.12,\n      \"contaminated_items_accuracy_lift\": 0.31,\n      \"non_contaminated_items_accuracy_change\": 0.014,\n      \"false_positive_rate_at_alpha_0.05\": 0.038\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Controlled Contamination — lz* by Model and Contamination Level (MMLU)\",\n        \"columns\": [\n          \"model\",\n          \"contam_level\",\n          \"accuracy\",\n          \"theta_hat\",\n          \"lz_star_mean\",\n          \"lz_star_sd\",\n          \"flagged_rate_alpha005\"\n        ],\n        \"key_rows\": [\n          [\n            \"Qwen3.5-9B\",\n            \"0%\",\n            0.721,\n            1.42,\n            0.08,\n            0.97,\n            0.047\n          ],\n          [\n            \"Qwen3.5-9B\",\n            \"5%\",\n            0.738,\n            1.51,\n            -3.72,\n            1.21,\n            0.82\n          ],\n          [\n            \"Qwen3.5-9B\",\n            \"10%\",\n            0.756,\n            1.59,\n            -6.45,\n            1.34,\n            0.94\n          ],\n          [\n            \"Qwen3.5-9B\",\n            \"15%\",\n            0.764,\n            1.63,\n            -8.91,\n            1.42,\n            0.97\n          ],\n          [\n            \"Qwen3.5-9B\",\n            \"25%\",\n            0.787,\n            1.71,\n            -11.34,\n            1.58,\n            0.99\n          ],\n          [\n            \"Qwen3.5-9B\",\n            \"50%\",\n            0.831,\n            1.89,\n            -4.82,\n            2.08,\n            0.87\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"0%\",\n            0.793,\n            1.81,\n            0.15,\n            0.94,\n            0.041\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"5%\",\n            0.808,\n            1.88,\n            -3.21,\n            1.18,\n            0.78\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"15%\",\n            0.831,\n            1.97,\n            -7.63,\n            1.38,\n            0.95\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"50%\",\n            0.874,\n            2.14,\n            -5.14,\n            2.01,\n            0.84\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Detection Performance (AUROC) by Contamination Level\",\n        \"columns\": [\n          \"contam_level\",\n          \"auroc_qwen\",\n          \"auroc_gemma\",\n          \"auroc_pooled\",\n          \"cohens_d_pooled\"\n        ],\n        \"key_rows\": [\n          [\n            \"5%\",\n            0.84,\n            0.8,\n            0.82,\n            1.1\n          ],\n          [\n            \"10%\",\n            0.93,\n            0.91,\n            0.92,\n            1.8\n          ],\n          [\n            \"15%\",\n            0.97,\n            0.95,\n            0.96,\n            2.3\n          ],\n          [\n            \"25%\",\n            0.99,\n            0.98,\n            0.99,\n            2.8\n          ],\n          [\n            \"50%\",\n            0.94,\n            0.91,\n            0.93,\n            1.6\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs Non-Contaminated Items\",\n        \"columns\": [\n          \"contam_level\",\n          \"contam_items_acc_before\",\n          \"contam_items_acc_after\",\n          \"contam_items_lift\",\n          \"non_contam_items_acc_before\",\n          \"non_contam_items_acc_after\",\n          \"non_contam_items_lift\"\n        ],\n        \"key_rows\": [\n          [\n            \"5%\",\n            0.56,\n            0.87,\n            0.31,\n            0.73,\n            0.74,\n            0.014\n          ],\n          [\n            \"15%\",\n            0.54,\n            0.84,\n            0.3,\n            0.73,\n            0.75,\n            0.018\n          ],\n          [\n            \"25%\",\n            0.55,\n            0.86,\n            0.31,\n            0.73,\n            0.76,\n            0.024\n          ],\n          [\n            \"50%\",\n            0.57,\n            0.88,\n            0.31,\n            0.73,\n            0.77,\n            0.037\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的 person-misfit 信号，Cohen's d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination 即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了 inverted-U，与扩展模拟定量一致。\\n\\n\\nSFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入 items 仅有微弱泛化（+1.4%）。这种\\\"选择性提升\\\"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的 non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且 benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen's d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15% 意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为 MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。\\n\"\n  },\n  {\n    \"name\": \"Power Theory Derivation\",\n    \"description\": \"推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将 inverted-U 升级为理论命题。\\n\",\n    \"results\": {\n      \"power_theory_r_squared\": 0.97,\n      \"power_formula\": \"power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean] per item\",\n      \"inverted_u_inflection_formula\": \"c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i)) | contam=c] − E_θ[...| contam=0]|\",\n      \"predicted_inflection_mmlu\": 0.64,\n      \"predicted_inflection_hellaswag\": 0.59,\n      \"predicted_inflection_gsm8k\": 0.68,\n      \"observed_inflection_mmlu\": 0.65,\n      \"observed_inflection_hellaswag\": 0.6,\n      \"observed_inflection_gsm8k\": 0.7,\n      \"inflection_prediction_error\": 0.02,\n      \"power_at_n100_15pct_predicted\": 0.089,\n      \"power_at_n1000_15pct_predicted\": 0.491,\n      \"power_at_n5000_15pct_predicted\": 0.862,\n      \"power_at_n14000_15pct_predicted\": 0.981,\n      \"min_n_for_80pct_power_at_15pct\": 3200,\n      \"min_n_for_80pct_power_at_5pct\": 9800\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Theoretical vs Simulated Power (15% Contamination)\",\n        \"columns\": [\n          \"n_items\",\n          \"predicted_power\",\n          \"simulated_power\",\n          \"absolute_error\"\n        ],\n        \"key_rows\": [\n          [\n            100,\n            0.089,\n            0.092,\n            0.003\n          ],\n          [\n            500,\n            0.312,\n            0.298,\n            0.014\n          ],\n          [\n            1000,\n            0.491,\n            0.503,\n            0.012\n          ],\n          [\n            1319,\n            0.578,\n            0.578,\n            0.0\n          ],\n          [\n            5000,\n            0.862,\n            0.851,\n            0.011\n          ],\n          [\n            10042,\n            0.964,\n            0.958,\n            0.006\n          ],\n          [\n            14042,\n            0.981,\n            0.979,\n            0.002\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Inverted-U Inflection Point — Predicted vs Observed\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"difficulty_sd\",\n          \"predicted_inflection\",\n          \"observed_inflection\",\n          \"abs_error\"\n        ],\n        \"key_rows\": [\n          [\n            \"MMLU\",\n            14042,\n            1.83,\n            0.64,\n            0.65,\n            0.01\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            1.52,\n            0.59,\n            0.6,\n            0.01\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            1.21,\n            0.68,\n            0.7,\n            0.02\n          ],\n          [\n            \"ARC-C\",\n            1172,\n            1.45,\n            0.62,\n            0.64,\n            0.02\n          ],\n          [\n            \"HumanEval\",\n            164,\n            1.67,\n            0.61,\n            0.63,\n            0.02\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Minimum n_items for 80% Power at Various Contamination Levels\",\n        \"columns\": [\n          \"contam_level\",\n          \"min_n_theoretical\",\n          \"min_n_simulated\"\n        ],\n        \"key_rows\": [\n          [\n            \"5%\",\n            9800,\n            10200\n          ],\n          [\n            \"10%\",\n            4700,\n            4900\n          ],\n          [\n            \"15%\",\n            3200,\n            3350\n          ],\n          [\n            \"25%\",\n            1800,\n            1900\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15% 污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有 12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty 分布预测拐点位置，误差仅 1-2 个百分点。\\n\\n\\nSnijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination 时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移 ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于 c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL 模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得 response pattern 看起来 \\\"最合理\\\" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard Audit (Large-Scale Scan)\",\n    \"description\": \"Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算 person-fit，绘制 per-benchmark 污染率随时间趋势。\\n\",\n    \"results\": {\n      \"leaderboard_models_scanned\": 2847,\n      \"leaderboard_models_with_per_item_logs\": 0,\n      \"leaderboard_models_rerun_inference\": 2847,\n      \"total_gpu_hours_inference\": 18.5,\n      \"leaderboard_flagged_rate_overall\": 0.12,\n      \"leaderboard_flagged_rate_mmlu\": 0.15,\n      \"leaderboard_flagged_rate_hellaswag\": 0.09,\n      \"leaderboard_flagged_rate_arc_c\": 0.07,\n      \"leaderboard_flagged_rate_gsm8k\": 0.11,\n      \"flagged_models_total\": 342,\n      \"flagged_two_sided_positive\": 87,\n      \"flagged_two_sided_negative\": 255,\n      \"contamination_trend_increasing\": true,\n      \"contamination_rate_2023q1\": 0.06,\n      \"contamination_rate_2023q3\": 0.11,\n      \"contamination_rate_2024q1\": 0.18,\n      \"cross_benchmark_consistent_flag_rate\": 0.34,\n      \"top_flagged_model_lz_star\": -22.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Leaderboard Audit Summary\",\n        \"columns\": [\n          \"benchmark\",\n          \"models_scanned\",\n          \"flagged_negative\",\n          \"flagged_positive\",\n          \"flagged_rate\",\n          \"median_lz_star_flagged\"\n        ],\n        \"key_rows\": [\n          [\n            \"MMLU\",\n            2847,\n            312,\n            115,\n            0.15,\n            -6.73\n          ],\n          [\n            \"HellaSwag\",\n            2847,\n            198,\n            58,\n            0.09,\n            -4.21\n          ],\n          [\n            \"ARC-C\",\n            2847,\n            142,\n            57,\n            0.07,\n            -3.12\n          ],\n          [\n            \"GSM8K\",\n            2182,\n            178,\n            63,\n            0.11,\n            -5.42\n          ],\n          [\n            \"Overall (any benchmark)\",\n            2847,\n            255,\n            87,\n            0.12,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Contamination Rate by Time Period\",\n        \"columns\": [\n          \"period\",\n          \"models_in_period\",\n          \"flagged_count\",\n          \"flagged_rate\"\n        ],\n        \"key_rows\": [\n          [\n            \"2023 Q1-Q2\",\n            487,\n            29,\n            0.06\n          ],\n          [\n            \"2023 Q3-Q4\",\n            891,\n            98,\n            0.11\n          ],\n          [\n            \"2024 Q1-Q2\",\n            1103,\n            198,\n            0.18\n          ],\n          [\n            \"2024 Q3+\",\n            366,\n            51,\n            0.14\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: Top 10 Most Anomalous Models\",\n        \"columns\": [\n          \"model\",\n          \"benchmark\",\n          \"accuracy\",\n          \"theta\",\n          \"lz_star\",\n          \"side\",\n          \"params\"\n        ],\n        \"key_rows\": [\n          [\n            \"anonymous-7b-v3\",\n            \"MMLU\",\n            0.847,\n            1.23,\n            -22.4,\n            \"negative\",\n            \"7B\"\n          ],\n          [\n            \"llm-finetune-2b\",\n            \"MMLU\",\n            0.912,\n            1.45,\n            18.7,\n            \"positive\",\n            \"2B\"\n          ],\n          [\n            \"benchmark-tuned-3b\",\n            \"GSM8K\",\n            0.891,\n            2.12,\n            -17.3,\n            \"negative\",\n            \"3B\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Leaderboard audit 是 IRT-FIT 的 \\\"killer app\\\"——唯一只需要 binary response data 的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要 logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342 个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到 7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。\\n\\n\\nPer-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存 aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847 个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是 benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%） 因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1 升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024 等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 \\\"suspicious near-ceiling\\\" 模型， 负侧 flagged（255 个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged 模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL Ablation\",\n    \"description\": \"比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对 false alarm 和 detection power 的影响。\\n\",\n    \"results\": {\n      \"auroc_4pl_15pct\": 0.96,\n      \"auroc_3pl_15pct\": 0.91,\n      \"auroc_difference_15pct\": 0.05,\n      \"false_alarm_rate_4pl\": 0.042,\n      \"false_alarm_rate_3pl\": 0.078,\n      \"power_4pl_15pct_mmlu\": 0.979,\n      \"power_3pl_15pct_mmlu\": 0.934,\n      \"power_difference_15pct_mmlu\": 0.045,\n      \"mean_abs_lz_star_difference_clean\": 0.34,\n      \"mean_abs_lz_star_difference_contam\": 0.87,\n      \"d_parameter_mean_psn_irt\": 0.91,\n      \"d_parameter_sd_psn_irt\": 0.08,\n      \"items_where_d_matters_most\": \"top-difficulty items (difficulty > 2.5) where d < 0.85\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: 4PL vs 3PL Detection Performance Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"4PL\",\n          \"3PL(d=1)\",\n          \"difference\"\n        ],\n        \"key_rows\": [\n          [\n            \"AUROC @ 15%\",\n            0.96,\n            0.91,\n            \"+0.05\"\n          ],\n          [\n            \"False Alarm Rate (α=0.05)\",\n            0.042,\n            0.078,\n            \"−0.036\"\n          ],\n          [\n            \"Power @ 15% MMLU\",\n            0.979,\n            0.934,\n            \"+0.045\"\n          ],\n          [\n            \"Power @ 5% MMLU\",\n            0.78,\n            0.69,\n            \"+0.09\"\n          ],\n          [\n            \"Mean |lz*| clean models\",\n            0.83,\n            1.17,\n            \"−0.34\"\n          ],\n          [\n            \"Mean |lz*| contam models (15%)\",\n            8.91,\n            8.04,\n            \"+0.87\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 15: Impact of d Parameter by Item Difficulty Band\",\n        \"columns\": [\n          \"difficulty_band\",\n          \"n_items\",\n          \"mean_d\",\n          \"lz_star_diff_clean\",\n          \"lz_star_diff_contam\"\n        ],\n        \"key_rows\": [\n          [\n            \"< 0.5 (easy)\",\n            2814,\n            0.97,\n            -0.08,\n            0.12\n          ],\n          [\n            \"0.5–1.5\",\n            5621,\n            0.93,\n            -0.21,\n            0.43\n          ],\n          [\n            \"1.5–2.5\",\n            3891,\n            0.89,\n            -0.38,\n            0.78\n          ],\n          [\n            \"> 2.5 (hard)\",\n            1716,\n            0.82,\n            -0.67,\n            1.45\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL 也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items 恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模 在检测任务中有非平凡的价值。\\n\\n\\n4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生 也可能答错某些 items 的现象——在 LLM 场景中对应\\\"某些 items 的表述/格式导致即使知道答案的模型也可能选错\\\"。 当 d < 1 时，3PL(d=1) 会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 \\\"aberrant\\\" 信号（false alarm 上升）。 4PL 通过让 d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的 items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model 的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。 差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison (ConStat, Min-K%++)\",\n    \"description\": \"在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++ 的 AUROC 和 Type-I error。\\n\",\n    \"results\": {\n      \"irt_fit_auroc_15pct\": 0.96,\n      \"constat_auroc_15pct\": 0.83,\n      \"min_k_pp_auroc_15pct\": 0.88,\n      \"irt_fit_auroc_5pct\": 0.82,\n      \"constat_auroc_5pct\": 0.61,\n      \"min_k_pp_auroc_5pct\": 0.72,\n      \"auroc_advantage_vs_constat_15pct\": 0.13,\n      \"auroc_advantage_vs_minkpp_15pct\": 0.08,\n      \"baseline_auroc_advantage_vs_constat\": 0.1,\n      \"type_i_error_irt_fit\": 0.042,\n      \"type_i_error_constat\": 0.053,\n      \"type_i_error_min_k_pp\": 0.048,\n      \"irt_fit_information_required\": \"binary responses only\",\n      \"constat_information_required\": \"binary responses + re-test capability\",\n      \"min_k_pp_information_required\": \"token-level log-probabilities\",\n      \"irt_fit_unique_advantage\": \"operates without model access\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Baseline Comparison — Detection Performance on Controlled Contamination\",\n        \"columns\": [\n          \"method\",\n          \"info_required\",\n          \"auroc_5pct\",\n          \"auroc_15pct\",\n          \"auroc_25pct\",\n          \"type_i_error\"\n        ],\n        \"key_rows\": [\n          [\n            \"IRT-FIT (lz*, two-sided)\",\n            \"binary responses\",\n            0.82,\n            0.96,\n            0.99,\n            0.042\n          ],\n          [\n            \"ConStat\",\n            \"binary + re-test\",\n            0.61,\n            0.83,\n            0.91,\n            0.053\n          ],\n          [\n            \"Min-K%++\",\n            \"token log-probs\",\n            0.72,\n            0.88,\n            0.95,\n            0.048\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: Detection Frontier — Information Access vs Detection Power\",\n        \"columns\": [\n          \"information_level\",\n          \"method\",\n          \"auroc_15pct\",\n          \"scalability\"\n        ],\n        \"key_rows\": [\n          [\n            \"binary responses only\",\n            \"IRT-FIT\",\n            0.96,\n            \"any model with public scores\"\n          ],\n          [\n            \"binary + re-test\",\n            \"ConStat\",\n            0.83,\n            \"requires live model access\"\n          ],\n          [\n            \"token probabilities\",\n            \"Min-K%++\",\n            0.88,\n            \"requires API with logprobs\"\n          ],\n          [\n            \"training data\",\n            \"n-gram overlap\",\n            \"—\",\n            \"requires training data access\"\n          ],\n          [\n            \"model weights\",\n            \"internal probing\",\n            \"—\",\n            \"requires open weights\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT 在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为 person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。\\n\\n\\nIRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility 参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的 re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test 分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的 person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT 不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Statistic\",\n    \"description\": \"实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*， 在 PSN-IRT 12 模型 + 控制实验模型上验证。\\n\",\n    \"results\": {\n      \"lzm_auroc_15pct\": 0.98,\n      \"lzm_vs_single_benchmark_auroc_gain\": 0.02,\n      \"lzm_cross_benchmark_correlation\": 0.67,\n      \"gemini15_lzm\": 18.42,\n      \"gpt4_lzm\": -0.87,\n      \"clean_model_lzm_mean\": 0.03,\n      \"clean_model_lzm_sd\": 0.91,\n      \"contam_model_lzm_mean_15pct\": -7.23,\n      \"lzm_null_ks_p\": 0.312,\n      \"lzm_power_at_15pct_pooled\": 0.99\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: lzm Results — PSN-IRT 12 Models\",\n        \"columns\": [\n          \"model\",\n          \"lzm_value\",\n          \"flagged_alpha005\",\n          \"n_benchmarks_individual_flag\"\n        ],\n        \"key_rows\": [\n          [\n            \"Gemini-1.5\",\n            18.42,\n            \"YES\",\n            3\n          ],\n          [\n            \"GPT-4\",\n            -0.87,\n            \"no\",\n            0\n          ],\n          [\n            \"Llama-2-70B\",\n            -3.21,\n            \"YES\",\n            1\n          ],\n          [\n            \"Claude-3-Opus\",\n            0.42,\n            \"no\",\n            0\n          ],\n          [\n            \"Mistral-7B\",\n            -2.45,\n            \"no\",\n            0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 19: lzm vs Single-Benchmark Detection Power\",\n        \"columns\": [\n          \"method\",\n          \"auroc_15pct\",\n          \"power_at_15pct\",\n          \"false_alarm_rate\"\n        ],\n        \"key_rows\": [\n          [\n            \"lz* (MMLU only)\",\n            0.96,\n            0.979,\n            0.042\n          ],\n          [\n            \"lz* (best single benchmark)\",\n            0.96,\n            0.979,\n            0.042\n          ],\n          [\n            \"lzm (all benchmarks)\",\n            0.98,\n            0.99,\n            0.037\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 是一个稳健的 \\\"overall contamination index\\\"，特别适合 leaderboard audit 场景—— 单一指标告诉你 \\\"这个模型总体上是否可疑\\\"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision 提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark 到多 benchmark 无缝聚合。\\n\\n\\nlzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个 benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98 是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark 一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark 上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval 上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有 benchmark 上都是 \\\"正常\\\" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models 上确实近似 N(0,1)。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Hypothesis Test\",\n    \"description\": \"在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在 RL 后保持检测力。\\n\",\n    \"results\": {\n      \"pre_rl_lz_star\": -8.91,\n      \"post_rl_lz_star\": -7.12,\n      \"post_rl_power_retention_ratio\": 0.84,\n      \"post_rl_auroc\": 0.92,\n      \"pre_rl_auroc\": 0.96,\n      \"auroc_drop_after_rl\": 0.04,\n      \"post_rl_accuracy_change\": 0.012,\n      \"post_rl_contam_items_accuracy\": 0.82,\n      \"pre_rl_contam_items_accuracy\": 0.84,\n      \"post_rl_non_contam_items_accuracy\": 0.75,\n      \"pre_rl_non_contam_items_accuracy\": 0.74,\n      \"post_rl_theta_shift\": 0.08,\n      \"mia_post_rl_auroc\": 0.54,\n      \"mia_pre_rl_auroc\": 0.71,\n      \"person_fit_vs_mia_advantage_post_rl\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)\",\n        \"columns\": [\n          \"stage\",\n          \"accuracy\",\n          \"theta\",\n          \"lz_star\",\n          \"auroc\",\n          \"power\"\n        ],\n        \"key_rows\": [\n          [\n            \"Clean baseline\",\n            0.721,\n            1.42,\n            0.08,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Post-SFT (contaminated)\",\n            0.764,\n            1.63,\n            -8.91,\n            0.96,\n            0.97\n          ],\n          [\n            \"Post-SFT + GRPO\",\n            0.776,\n            1.71,\n            -7.12,\n            0.92,\n            0.91\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 21: Person-Fit vs MIA — Post-RL Robustness\",\n        \"columns\": [\n          \"method\",\n          \"pre_rl_auroc\",\n          \"post_rl_auroc\",\n          \"auroc_retention\",\n          \"info_required\"\n        ],\n        \"key_rows\": [\n          [\n            \"IRT-FIT (lz*)\",\n            0.96,\n            0.92,\n            \"96%\",\n            \"binary responses\"\n          ],\n          [\n            \"Min-K%++\",\n            0.88,\n            0.62,\n            \"70%\",\n            \"token log-probs\"\n          ],\n          [\n            \"MIA (reference-based)\",\n            0.71,\n            0.54,\n            \"76%\",\n            \"token log-probs + ref model\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 22: Item-Level Analysis — Accuracy Change After GRPO\",\n        \"columns\": [\n          \"item_type\",\n          \"pre_rl_accuracy\",\n          \"post_rl_accuracy\",\n          \"change\"\n        ],\n        \"key_rows\": [\n          [\n            \"contaminated items\",\n            0.84,\n            0.82,\n            -0.02\n          ],\n          [\n            \"non-contaminated items\",\n            0.74,\n            0.75,\n            0.01\n          ],\n          [\n            \"contaminated hard items (diff>2)\",\n            0.79,\n            0.76,\n            -0.03\n          ],\n          [\n            \"non-contaminated hard items (diff>2)\",\n            0.41,\n            0.43,\n            0.02\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： \\\"MIA 在 post-RL 后失效（AUROC 0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but does not undo memorization of correct answers。\\\" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information 条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in robustness to distribution shift。\\n\\n\\nGRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance）， 对已经答对的 contaminated items 不会产生\\\"遗忘\\\"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在 reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items 的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 \\\"预期外正确\\\" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接 memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54）， 因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit 信号就存在。这是 person-fit \\\"信息层级优势\\\" 的直接体现： binary outcome 比 token probability 更鲁棒，因为 RL 可以改变 \\\"how confident the model is\\\" 但很难改变 \\\"whether it gets the answer right\\\" on memorized items.\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH, MATH)\",\n    \"description\": \"添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\\n\",\n    \"results\": {\n      \"bbh_n_items\": 6511,\n      \"math_n_items\": 5000,\n      \"bbh_power_at_15pct\": 0.89,\n      \"math_power_at_15pct\": 0.84,\n      \"bbh_power_at_5pct\": 0.52,\n      \"math_power_at_5pct\": 0.44,\n      \"bbh_predicted_power_from_theory\": 0.88,\n      \"math_predicted_power_from_theory\": 0.83,\n      \"theory_prediction_error_bbh\": 0.01,\n      \"theory_prediction_error_math\": 0.01,\n      \"bbh_inverted_u_inflection\": 0.62,\n      \"math_inverted_u_inflection\": 0.66,\n      \"power_gap_1k_10k_filled\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 23: Power Gap Analysis — All 7 Benchmarks\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"power_at_15pct_simulated\",\n          \"power_at_15pct_predicted\",\n          \"power_at_5pct\"\n        ],\n        \"key_rows\": [\n          [\n            \"HumanEval\",\n            164,\n            0.243,\n            0.231,\n            0.07\n          ],\n          [\n            \"ARC-C\",\n            1172,\n            0.129,\n            0.142,\n            0.04\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.578,\n            0.561,\n            0.22\n          ],\n          [\n            \"MATH\",\n            5000,\n            0.84,\n            0.83,\n            0.44\n          ],\n          [\n            \"BBH\",\n            6511,\n            0.89,\n            0.88,\n            0.52\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.733,\n            0.748,\n            0.34\n          ],\n          [\n            \"MMLU\",\n            14042,\n            0.979,\n            0.981,\n            0.78\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval) 到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97 推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319 items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item 体现。\\n\\n\\nBBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042 ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH 的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH 难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ 参数化吸收了这些差异。\\n\"\n  },\n  {\n    \"name\": \"Domain-Level Analysis (MMLU)\",\n    \"description\": \"按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。\\n\",\n    \"results\": {\n      \"n_domains_analyzed\": 57,\n      \"domains_with_extreme_lz_star\": 57,\n      \"gemini15_domain_lz_star_range\": \"[+0.8, +12.3]\",\n      \"gemini15_domain_lz_star_mean\": 4.21,\n      \"gemini15_domain_lz_star_sd\": 2.87,\n      \"gemini15_most_aberrant_domain\": \"abstract_algebra\",\n      \"gemini15_least_aberrant_domain\": \"high_school_mathematics\",\n      \"contamination_pattern\": \"uniform across all domains\",\n      \"domain_level_power_mean\": 0.34,\n      \"domain_level_power_max\": 0.72,\n      \"domain_level_n_items_range\": \"[100, 1534]\",\n      \"gpt4_domain_lz_star_sd\": 0.82,\n      \"gpt4_domains_flagged\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)\",\n        \"columns\": [\n          \"domain\",\n          \"n_items\",\n          \"gemini15_acc\",\n          \"gemini15_lz_star\",\n          \"gpt4_acc\",\n          \"gpt4_lz_star\"\n        ],\n        \"key_rows\": [\n          [\n            \"abstract_algebra\",\n            100,\n            1.0,\n            0.83,\n            0.73,\n            -0.42\n          ],\n          [\n            \"professional_medicine\",\n            272,\n            1.0,\n            4.21,\n            0.851,\n            0.67\n          ],\n          [\n            \"high_school_mathematics\",\n            270,\n            1.0,\n            2.14,\n            0.412,\n            -1.23\n          ],\n          [\n            \"college_chemistry\",\n            100,\n            1.0,\n            0.91,\n            0.47,\n            0.31\n          ],\n          [\n            \"global_facts\",\n            100,\n            1.0,\n            0.8,\n            0.38,\n            -0.87\n          ],\n          [\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\"\n          ],\n          [\n            \"miscellaneous\",\n            783,\n            1.0,\n            7.89,\n            0.872,\n            0.42\n          ],\n          [\n            \"clinical_knowledge\",\n            265,\n            1.0,\n            3.87,\n            0.792,\n            -0.18\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 25: Domain-Level Power as Function of n_items\",\n        \"columns\": [\n          \"n_items_bin\",\n          \"n_domains\",\n          \"mean_power_at_15pct\",\n          \"predicted_from_theory\"\n        ],\n        \"key_rows\": [\n          [\n            \"100-150\",\n            22,\n            0.18,\n            0.17\n          ],\n          [\n            \"150-300\",\n            21,\n            0.31,\n            0.33\n          ],\n          [\n            \"300-600\",\n            9,\n            0.52,\n            0.5\n          ],\n          [\n            \"600-1000\",\n            3,\n            0.64,\n            0.67\n          ],\n          [\n            \">1000\",\n            2,\n            0.72,\n            0.74\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据：\\\"uniform contamination across all 57 MMLU domains\\\" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization 的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power theory 提供了 57 个额外的 (n_items, power) 数据点。\\n\\nGemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz* 都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1) 各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty 分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty 分布的偏差更大。 \\\"uniform across all domains\\\" 的发现很重要：它排除了 \\\"Gemini-1.5 只是在特定领域特别强\\\" 的 innocent explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34 是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57 个 domain 相当于 57 个不同 n_items 的 \\\"实验\\\"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差 1.0），0 个 domain flagged， 作为干净的 negative control。\\n\"\n  }\n]",
      "numLines": 1497,
      "startLine": 1,
      "totalLines": 1497
    }
  },
  "sourceToolAssistantUUID": "6bfd6c2a-d1f3-4307-bec5-de6c5343bb34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T08:52:20.253Z_

<details open><summary>🔧 Tool call — Read · `toolu_016u9ELywfEpwinPaMrPmaFh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d949ccd-6b24-4260-ba5b-b779cfb87f60",
  "isSidechain": false,
  "requestId": "req_011CbDY5bTSSU45ScFy2CCaU",
  "type": "assistant",
  "uuid": "b88721e9-f89e-44b2-9494-3d72d02ff1b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuhgREacGWRJxzmRvoDbc3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11800,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11800
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

_source line 11 · 2026-05-20T08:52:20.261Z_

<details><summary>↩ Tool result · `toolu_016u9ELywfEpwinPaMrPmaFh`</summary>

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
10	**Claim 1 (Minimal-Information Detection)**:
11	IRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: "What can be detected from binary response patterns alone?" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals."
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
42	| R4 | "Only 12 models" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Single-sided test misses full contamination" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	
48	## Key Narrative Elements (from External Review)
49	
50	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
51	2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
52	3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
53	4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
54	
55	## MVP Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.
58	- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.
59	- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b88721e9-f89e-44b2-9494-3d72d02ff1b4",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "4813f309-7767-4946-bad5-f835722d5b4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection)**:\nIRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: \"What can be detected from binary response patterns alone?\" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Single-sided test misses full contamination\" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## MVP Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.\n- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.\n- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  },
  "sourceToolAssistantUUID": "b88721e9-f89e-44b2-9494-3d72d02ff1b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "4813f309-7767-4946-bad5-f835722d5b4b",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT-based contamination detection paper",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Assistant

_source line 14 · 2026-05-20T08:52:57.762Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also read the paper-writing-norms skill and the latex-paper skill for guidance on writing style.

Actually, the task says "够审级" (good enough for review), not publication quality. Let me just write the paper directly based on the experiment data and framing.

Let me structure the paper:

1. Abstract
2. Introduction (with detection frontier framing)
3. Background (IRT basics, person-fit statistics)
4. Method (IRT-FIT framework: two-sided detection, lzm)
5. Experiments
   - Controlled Contamination (Tables 5-7)
   - Extended Simulation / Inverted-U (Tables 3-4)
   - Power Theory (Tables 8-10)
   - Two-Sided Detection Framework (Tables 1-2)
   - Baseline Comparison (Tables 16-17)
   - Post-RL Robustness (Tables 20-22)
   - 4PL vs 3PL Ablation (Tables 14-15)
   - Multiscale lzm (Tables 18-19)
   - Leaderboard Audit (Tables 11-13)
   - Extra Benchmarks (Table 23)
   - Domain-Level Analysis (Tables 24-25)
6. Results and Discussion

Now I'm organizing the full paper structure to ensure all 9 experiments and 25 tables are properly covered, mapping each experiment to its corresponding results sections. I need to fit all 11 experiments into an 8-page paper, so I'm organizing them into logical sections within the experiments part. Each experiment requires at least one table and a dedicated section, but I can group related experiments together to manage the space constraints while still covering everything comprehensively. I'm consolidating the structure into three main sections—Controlled Experiments, Theory, and Comparisons—to reduce redundancy while keeping all the key results organized by their experimental focus. I need to decide on a structure that fits the page constraints while including all experiments. I'll consolidate some tables strategically and use a compact two-column format with the ACL style to keep everything organized and readable. I'm reviewing the outline structure for this paper and need to verify the output directory exists before proceeding with writing out the sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4813f309-7767-4946-bad5-f835722d5b4b",
  "isSidechain": false,
  "requestId": "req_011CbDY5tQuXEhkrUYFo8GsQ",
  "type": "assistant",
  "uuid": "32135a77-4f34-4c9b-b1ab-9f6120f20786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154NB5StCE41NdZs99heWH8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24736,
      "cache_read_input_tokens": 23641,
      "output_tokens": 2201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2201,
          "cache_read_input_tokens": 23641,
          "cache_creation_input_tokens": 24736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24736
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

_source line 15 · 2026-05-20T08:52:57.764Z_

Let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32135a77-4f34-4c9b-b1ab-9f6120f20786",
  "isSidechain": false,
  "requestId": "req_011CbDY5tQuXEhkrUYFo8GsQ",
  "type": "assistant",
  "uuid": "8b7bd7c3-b319-4ae4-9ac7-9d11f7a6c654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154NB5StCE41NdZs99heWH8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24736,
      "cache_read_input_tokens": 23641,
      "output_tokens": 2201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2201,
          "cache_read_input_tokens": 23641,
          "cache_creation_input_tokens": 24736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24736
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

_source line 16 · 2026-05-20T08:52:58.888Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YQuC1v3v2egYkVT9H7zv8n`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b7bd7c3-b319-4ae4-9ac7-9d11f7a6c654",
  "isSidechain": false,
  "requestId": "req_011CbDY5tQuXEhkrUYFo8GsQ",
  "type": "assistant",
  "uuid": "555ef39c-c1be-4177-b1b9-243f7360f3ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154NB5StCE41NdZs99heWH8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24736,
      "cache_read_input_tokens": 23641,
      "output_tokens": 2201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2201,
          "cache_read_input_tokens": 23641,
          "cache_creation_input_tokens": 24736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24736
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

_source line 17 · 2026-05-20T08:52:59.048Z_

<details><summary>↩ Tool result · `toolu_01YQuC1v3v2egYkVT9H7zv8n`</summary>

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
  "parentUuid": "555ef39c-c1be-4177-b1b9-243f7360f3ca",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "a8ff6ce1-dd75-4d07-8144-5debc4664693",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "555ef39c-c1be-4177-b1b9-243f7360f3ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T08:53:12.847Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper. I need to cover all 11 experiments with their tables. Let me write a comprehensive paper.

Let me be strategic about which tables to include in full vs. summarize. There are 25 tables across 11 experiments. I'll include the most important tables fully and summarize others in text. But the instruction says "为每个实验设计对应的 section/table" — so each experiment needs at least one table.

Let me select the key tables for each experiment:
1. Two-Sided Detection: Table 1 (key rows), Table 2


2. Extended Simulation: Table 3 (key rows), Table 4
3. Controlled Contamination: Table 5 (key rows), Table 6, Table 7
4. Power Theory: Table 8, Table 9, Table 10
5. Leaderboard Audit: Table 11, Table 12
6. 4PL vs 3PL: Table 14
7. Baseline Comparison: Table 16, Table 17
8. Multiscale lzm: Table 18, Table 19
9. Post-RL: Table 20, Table 21
10. Extra Benchmarks: Table 23
11. Domain-Level: (need to determine which table)

I'm wrapping up the domain-level section with Tables 24 and 25, which brings the total to around 20 tables. That's reasonable for a comprehensive paper. I should consolidate where possible and move some results inline to keep things manageable, but each experiment needs its own section with supporting tables. Let me start writing the LaTeX document now with a focus on completeness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ff6ce1-dd75-4d07-8144-5debc4664693",
  "isSidechain": false,
  "requestId": "req_011CbDY8kGMCaPN9gUumDpZr",
  "type": "assistant",
  "uuid": "fea6f68e-189b-4298-bf7a-170da34ea923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo98WemA2uyk2S9wiN3ecN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 48377,
      "output_tokens": 14233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14233,
          "cache_read_input_tokens": 48377,
          "cache_creation_input_tokens": 2226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2226
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

_source line 19 · 2026-05-20T08:53:12.849Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea6f68e-189b-4298-bf7a-170da34ea923",
  "isSidechain": false,
  "requestId": "req_011CbDY8kGMCaPN9gUumDpZr",
  "type": "assistant",
  "uuid": "50d98e02-0ea6-4ccd-8d40-34f64ae61f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo98WemA2uyk2S9wiN3ecN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 48377,
      "output_tokens": 14233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14233,
          "cache_read_input_tokens": 48377,
          "cache_creation_input_tokens": 2226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2226
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

_source line 20 · 2026-05-20T08:56:46.961Z_

<details open><summary>🔧 Tool call — Write · `toolu_018LZCHxEA6b8vzXhdxbjzWZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\newcolumntype{R}{>{\\raggedleft\\arraybackslash}p{1.2cm}}\n\\newcolumntype{L}{>{\\raggedright\\arraybackslash}p{2.8cm}}\n\n\\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\\\via Item Response Theory Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \\textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \\ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \\gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\\% contamination and 0.82 at 5\\%---outperforming ConStat (0.83/0.61) and Min-K\\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nBenchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.\n\nExisting detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\\%++ \\citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \\citep{oren2024proving} requires specially crafted prompts. ConStat \\citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \\citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.\n\nA contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \\emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \\citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.\n\nWe introduce \\textbf{IRT-FIT}, a framework that establishes the \\emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\\% contamination---outperforming methods requiring token probabilities or re-testing.\n    \\item \\textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.\n    \\item \\textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\\% contamination flag rate increasing from 6\\% (2023 Q1) to 18\\% (2024 Q1). We identify Gemini-1.5's 100\\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\\hat{\\theta}=0.78$).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\\label{sec:background}\n\n\\subsection{Item Response Theory}\n\nIRT models the probability of a correct response as a function of examinee ability $\\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:\n\\begin{equation}\nP_i(\\theta) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + e^{-a_i(\\theta - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.\n\n\\subsection{Person-Fit Statistics}\n\nThe $l_z$ statistic \\citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:\n\\begin{equation}\nl_z = \\frac{\\sum_{i=1}^{n} \\left[ x_i \\log P_i(\\hat{\\theta}) + (1-x_i) \\log(1-P_i(\\hat{\\theta})) \\right] - E[l_0]}{SD[l_0]}\n\\end{equation}\nwhere $x_i \\in \\{0,1\\}$ is the response to item $i$ and $\\hat{\\theta}$ is the MLE of ability. \\citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\\hat{\\theta}$, yielding $l_z^* \\sim N(0,1)$ under the null hypothesis of model fit.\n\n% ============================================================\n\\section{Method: IRT-FIT}\n\\label{sec:method}\n\n\\subsection{Two-Sided Detection Framework}\n\nTraditional person-fit analysis tests only $l_z^* < c_{\\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:\n\n\\begin{itemize}\n    \\item \\textbf{Partial contamination} ($l_z^* \\ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.\n    \\item \\textbf{Full contamination} ($l_z^* \\gg 0$): The model memorizes all items, producing a response pattern that is \\emph{over-consistent}---all items correct, including those far beyond estimated ability.\n\\end{itemize}\n\nWe apply the two-sided test $|l_z^*| > c_{\\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.\n\n\\subsection{Multiscale Aggregation ($l_{zm}$)}\n\nFollowing \\citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:\n\\begin{equation}\nl_{zm} = \\frac{1}{\\sqrt{K}} \\sum_{k=1}^{K} |l_{z,k}^*|\n\\end{equation}\nwhere $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).\n\n\\subsection{Power Theory}\n\nBuilding on Snijders' variance formula, we derive the detection power as:\n\\begin{equation}\n\\text{power} \\approx \\Phi\\!\\left(\\frac{\\delta \\sqrt{n}}{\\sigma_{l_z^*}} - z_{\\alpha}\\right)\n\\label{eq:power}\n\\end{equation}\nwhere $\\delta = E[\\log L_{\\text{contam}} - \\log L_{\\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:\n\\begin{equation}\nc^* = \\arg\\min_{c} \\left| E_\\theta\\!\\left[\\sum_i f(x_i, P_i) \\mid \\text{contam}=c\\right] - E_\\theta\\!\\left[\\sum_i f(x_i, P_i) \\mid \\text{contam}=0\\right] \\right|\n\\end{equation}\nwhere $f(x_i, P_i) = x_i \\log P_i + (1-x_i)\\log(1-P_i)$.\n\n% ============================================================\n\\section{Controlled Contamination Experiments}\n\\label{sec:controlled}\n\n\\subsection{Ground-Truth Contamination}\n\\label{sec:ctrl-contam}\n\nWe inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\\%/5\\%/10\\%/15\\%/25\\%/50\\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.\n\n\\begin{table}[t]\n\\centering\n\\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}\n\\label{tab:ctrl-contam}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Contam.} & \\textbf{Acc.} & $\\hat{\\theta}$ & $l_z^*$ & \\textbf{Flag} \\\\\n\\midrule\nQwen3.5-9B & 0\\% & .721 & 1.42 & 0.08 & .047 \\\\\nQwen3.5-9B & 5\\% & .738 & 1.51 & $-$3.72 & .82 \\\\\nQwen3.5-9B & 10\\% & .756 & 1.59 & $-$6.45 & .94 \\\\\nQwen3.5-9B & 15\\% & .764 & 1.63 & $-$8.91 & .97 \\\\\nQwen3.5-9B & 25\\% & .787 & 1.71 & $-$11.34 & .99 \\\\\nQwen3.5-9B & 50\\% & .831 & 1.89 & $-$4.82 & .87 \\\\\n\\midrule\nGemma-4-31B & 0\\% & .793 & 1.81 & 0.15 & .041 \\\\\nGemma-4-31B & 5\\% & .808 & 1.88 & $-$3.21 & .78 \\\\\nGemma-4-31B & 15\\% & .831 & 1.97 & $-$7.63 & .95 \\\\\nGemma-4-31B & 50\\% & .874 & 2.14 & $-$5.14 & .84 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection performance (AUROC) by contamination level.}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{Qwen} & \\textbf{Gemma} & \\textbf{Pooled} & \\textbf{Cohen's $d$} \\\\\n\\midrule\n5\\% & 0.84 & 0.80 & 0.82 & 1.1 \\\\\n10\\% & 0.93 & 0.91 & 0.92 & 1.8 \\\\\n15\\% & 0.97 & 0.95 & 0.96 & 2.3 \\\\\n25\\% & 0.99 & 0.98 & 0.99 & 2.8 \\\\\n50\\% & 0.94 & 0.91 & 0.93 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\\% to 25\\% contamination, followed by a decrease at 50\\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\\%), ruling out model-specific artifacts. False positive rate at $\\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\\% (AUROC 0.82, Table~\\ref{tab:auroc}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination selectivity: accuracy change on contaminated vs.\\ non-contaminated items (Qwen3.5-9B).}\n\\label{tab:selectivity}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\multicolumn{2}{c}{\\textbf{Contam.\\ Items}} & \\multicolumn{2}{c}{\\textbf{Non-Contam.\\ Items}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Before & Lift & Before & Lift \\\\\n\\midrule\n5\\% & .56 & +.31 & .73 & +.014 \\\\\n15\\% & .54 & +.30 & .73 & +.018 \\\\\n25\\% & .55 & +.31 & .73 & +.024 \\\\\n50\\% & .57 & +.31 & .73 & +.037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.\n\n\\subsection{Inverted-U Signal Characterization}\n\\label{sec:inverted-u}\n\nWe extend simulations to 60\\%/75\\%/90\\%/100\\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_z^*$ as a function of contamination level (mean $\\pm$ SD, 100 replications).}\n\\label{tab:inverted-u}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\n0\\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\\\\n5\\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\\\\n10\\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\\\\n15\\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\\\\n25\\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\\\\n50\\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\\\\n60\\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\\\\n75\\% & 8.42 & 5.67 & 3.21 & 1.12 \\\\\n90\\% & 19.31 & 12.45 & 6.78 & 2.34 \\\\\n100\\% & 28.50 & 18.20 & 8.70 & 3.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-sided detection power at various contamination levels.}\n\\label{tab:two-sided-power}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\n5\\% & .780 & .340 & .220 & .060 \\\\\n15\\% & .979 & .733 & .578 & .129 \\\\\n25\\% & .998 & .891 & .743 & .201 \\\\\n50\\% & .872 & .514 & .298 & .080 \\\\\n75\\% & .991 & .934 & .712 & .187 \\\\\n100\\% & 1.000 & .998 & .962 & .478 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:inverted-u} and \\ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\\% contamination (MMLU: $-$12.08), crosses zero near 60--65\\%, and becomes strongly positive at high contamination (100\\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.\n\n\\subsection{Power Theory Derivation}\n\\label{sec:power-theory}\n\nEquation~\\ref{eq:power} predicts detection power as a function of $n_{\\text{items}}$. Table~\\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Theoretical vs.\\ simulated power at 15\\% contamination.}\n\\label{tab:power-theory}\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n$n_{\\text{items}}$ & \\textbf{Predicted} & \\textbf{Simulated} & \\textbf{$|\\Delta|$} \\\\\n\\midrule\n100 & .089 & .092 & .003 \\\\\n500 & .312 & .298 & .014 \\\\\n1{,}000 & .491 & .503 & .012 \\\\\n1{,}319 & .578 & .578 & .000 \\\\\n5{,}000 & .862 & .851 & .011 \\\\\n10{,}042 & .964 & .958 & .006 \\\\\n14{,}042 & .981 & .979 & .002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inverted-U inflection point: predicted vs.\\ observed.}\n\\label{tab:inflection}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Pred.} & \\textbf{Obs.} & $|\\Delta|$ \\\\\n\\midrule\nMMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\\\\nHellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\\\\nGSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\\\\nARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\\\\nHumanEval & 164 & 0.61 & 0.63 & 0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Minimum $n_{\\text{items}}$ for 80\\% power at various contamination levels.}\n\\label{tab:min-n}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{Theory} & \\textbf{Simulation} \\\\\n\\midrule\n5\\% & 9{,}800 & 10{,}200 \\\\\n10\\% & 4{,}700 & 4{,}900 \\\\\n15\\% & 3{,}200 & 3{,}350 \\\\\n25\\% & 1{,}800 & 1{,}900 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\\leq$0.02. Table~\\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\\% contamination requires $\\geq$3{,}200 items; detecting 5\\% contamination requires $\\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\\% power---not a method failure, but insufficient information.\n\n% ============================================================\n\\section{Comparisons and Robustness}\n\\label{sec:comparison}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{Baseline comparison on controlled contamination ground truth.}\n\\label{tab:baseline}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Method} & \\textbf{Info Required} & \\textbf{5\\%} & \\textbf{15\\%} & \\textbf{25\\%} & \\textbf{Type-I} \\\\\n\\midrule\nIRT-FIT & binary & .82 & .96 & .99 & .042 \\\\\nConStat & binary + retest & .61 & .83 & .91 & .053 \\\\\nMin-K\\%++ & token log-probs & .72 & .88 & .95 & .048 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection frontier: information access vs.\\ detection power (AUROC at 15\\% contam.).}\n\\label{tab:frontier}\n\\small\n\\begin{tabular}{llrl}\n\\toprule\n\\textbf{Info Level} & \\textbf{Method} & \\textbf{AUROC} & \\textbf{Scalability} \\\\\n\\midrule\nBinary only & IRT-FIT & .96 & Any model w/ scores \\\\\nBinary + retest & ConStat & .83 & Requires live access \\\\\nToken probs & Min-K\\%++ & .88 & Requires API logprobs \\\\\nTraining data & N-gram & --- & Requires training data \\\\\nWeights & Probing & --- & Requires open weights \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIRT-FIT achieves the highest AUROC while requiring the least information (Table~\\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\\%++ (+0.08) is notable given that Min-K\\%++ has access to richer token-level information. Table~\\ref{tab:frontier} positions these results on the detection frontier.\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\n\\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\\% MMLU SFT contamination).\n\n\\begin{table}[t]\n\\centering\n\\caption{Pre- vs.\\ post-RL person-fit (Qwen3.5-9B, 15\\% MMLU contamination).}\n\\label{tab:post-rl}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Stage} & \\textbf{Acc.} & $\\hat{\\theta}$ & $l_z^*$ & \\textbf{AUROC} & \\textbf{Power} \\\\\n\\midrule\nClean & .721 & 1.42 & 0.08 & --- & --- \\\\\nPost-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\\\\nPost-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Person-fit vs.\\ MIA: post-RL robustness comparison.}\n\\label{tab:post-rl-comparison}\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Method} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Retain.} & \\textbf{Info} \\\\\n\\midrule\nIRT-FIT & .96 & .92 & 96\\% & binary \\\\\nMin-K\\%++ & .88 & .62 & 70\\% & token probs \\\\\nMIA (ref.) & .71 & .54 & 76\\% & token probs + ref \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGRPO reduces the $l_z^*$ signal by only 20\\% ($-$8.91 $\\to$ $-$7.12), retaining 96\\% of AUROC (Table~\\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\\% of their accuracy after GRPO (0.84 $\\to$ 0.82), while non-contaminated items gain +1\\%. RL changes \\emph{how confident} the model is, but not \\emph{whether it answers correctly} on memorized items.\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\\label{sec:ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{4PL vs.\\ 3PL detection performance.}\n\\label{tab:4pl-3pl}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Metric} & \\textbf{4PL} & \\textbf{3PL} & $\\Delta$ \\\\\n\\midrule\nAUROC @ 15\\% & .960 & .910 & +.050 \\\\\nFalse alarm ($\\alpha$=.05) & .042 & .078 & $-$.036 \\\\\nPower @ 15\\% MMLU & .979 & .934 & +.045 \\\\\nPower @ 5\\% MMLU & .780 & .690 & +.090 \\\\\nMean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\\\\nMean $|l_z^*|$ contam.\\ 15\\% & 8.91 & 8.04 & +0.87 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Impact of $d$ parameter by item difficulty band.}\n\\label{tab:d-param}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Difficulty} & $n$ & Mean $d$ & $\\Delta l_z^*$ clean & $\\Delta l_z^*$ contam. \\\\\n\\midrule\n$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\\\\n0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\\\\n1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\\\\n$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\\% to 4.2\\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.\n\n\\subsection{Multiscale $l_{zm}$ Statistic}\n\\label{sec:lzm}\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_{zm}$ results on PSN-IRT 12 models.}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Model} & $l_{zm}$ & \\textbf{Flag} & \\textbf{\\#Bench.\\ Flagged} \\\\\n\\midrule\nGemini-1.5 & 18.42 & YES & 3 \\\\\nGPT-4 & $-$0.87 & no & 0 \\\\\nLlama-2-70B & $-$3.21 & YES & 1 \\\\\nClaude-3-Opus & 0.42 & no & 0 \\\\\nMistral-7B & $-$2.45 & no & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_{zm}$ vs.\\ single-benchmark detection (15\\% contamination).}\n\\label{tab:lzm-vs-single}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{Power} & \\textbf{FA Rate} \\\\\n\\midrule\n$l_z^*$ (MMLU only) & .96 & .979 & .042 \\\\\n$l_z^*$ (best single) & .96 & .979 & .042 \\\\\n$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.\n\n% ============================================================\n\\section{Large-Scale Empirical Study}\n\\label{sec:empirical}\n\n\\subsection{Two-Sided Detection on PSN-IRT Models}\n\\label{sec:two-sided}\n\nWe apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-sided detection results (selected model-benchmark pairs).}\n\\label{tab:two-sided-results}\n\\small\n\\begin{tabular}{llrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Bench.} & $l_z^*$ & \\textbf{Side} & \\textbf{Flag} \\\\\n\\midrule\nGemini-1.5 & MMLU & +34.75 & positive & YES \\\\\nGemini-1.5 & GSM8K & $-$15.71 & negative & YES \\\\\nGemini-1.5 & HumanEval & $-$12.37 & negative & YES \\\\\nGPT-4 & MMLU & $-$1.23 & --- & no \\\\\nLlama-2-70B & ARC-C & $-$3.87 & negative & YES \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{One-sided vs.\\ two-sided detection comparison (FDR = 0.05).}\n\\label{tab:one-vs-two}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Method} & \\textbf{Total} & \\textbf{Partial} & \\textbf{Full} & \\textbf{FDR} \\\\\n\\midrule\nOne-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\\\\nTwo-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGemini-1.5 on MMLU ($l_z^*=+34.75$, 95\\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\\% accuracy with estimated $\\hat{\\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\\ref{tab:one-vs-two}).\n\n\\subsection{Leaderboard Audit}\n\\label{sec:leaderboard}\n\nWe run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).\n\n\\begin{table}[t]\n\\centering\n\\caption{Leaderboard audit summary.}\n\\label{tab:leaderboard}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Bench.} & $n$ & \\textbf{Neg.} & \\textbf{Pos.} & \\textbf{Rate} & \\textbf{Med.\\ $l_z^*$} \\\\\n\\midrule\nMMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\\\\nHSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\\\\nARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\\\\nGSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\\\\nOverall & 2{,}847 & 255 & 87 & .12 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination rate by time period.}\n\\label{tab:temporal}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Period} & \\textbf{Models} & \\textbf{Flagged} & \\textbf{Rate} \\\\\n\\midrule\n2023 Q1--Q2 & 487 & 29 & .06 \\\\\n2023 Q3--Q4 & 891 & 98 & .11 \\\\\n2024 Q1--Q2 & 1{,}103 & 198 & .18 \\\\\n2024 Q3+ & 366 & 51 & .14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Most anomalous models (top 3 by $|l_z^*|$).}\n\\label{tab:top-anomalous}\n\\small\n\\begin{tabular}{llrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Bench.} & \\textbf{Acc.} & $l_z^*$ & \\textbf{Side} & \\textbf{Params} \\\\\n\\midrule\nanon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\\\\nllm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\\\\nbench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe audit reveals 342 flagged models (12\\% overall), with MMLU most affected at 15\\% (Table~\\ref{tab:leaderboard}). Contamination rates increase from 6\\% in early 2023 to 18\\% in early 2024 (Table~\\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\\%: about one-third of flagged models show anomalies on multiple benchmarks.\n\n\\subsection{Additional Benchmarks: BBH and MATH}\n\\label{sec:extra-bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{Power analysis across all 7 benchmarks (15\\% contamination).}\n\\label{tab:power-all}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Sim.} & \\textbf{Pred.} & \\textbf{5\\%} \\\\\n\\midrule\nHumanEval & 164 & .243 & .231 & .07 \\\\\nARC-C & 1{,}172 & .129 & .142 & .04 \\\\\nGSM8K & 1{,}319 & .578 & .561 & .22 \\\\\nMATH & 5{,}000 & .840 & .830 & .44 \\\\\nBBH & 6{,}511 & .890 & .880 & .52 \\\\\nHellaSwag & 10{,}042 & .733 & .748 & .34 \\\\\nMMLU & 14{,}042 & .979 & .981 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\\ref{tab:power-all}). All seven benchmarks fall within 1--2\\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\\text{items}}$ (1{,}172 vs.\\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\\delta$ term in Equation~\\ref{eq:power}.\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:domain}\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\\ GPT-4 (selected domains).}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Domain} & $n$ & \\multicolumn{2}{c}{\\textbf{Gemini-1.5}} & \\multicolumn{2}{c}{\\textbf{GPT-4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\\\\n\\midrule\nabstract\\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\\\\nprof\\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\\\\nhs\\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\\\\ncollege\\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\\\\nmiscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\\\\nclinical\\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level power as a function of $n_{\\text{items}}$.}\n\\label{tab:domain-power}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n$n_{\\text{items}}$ \\textbf{bin} & \\textbf{Domains} & \\textbf{Power} & \\textbf{Pred.} \\\\\n\\midrule\n100--150 & 22 & .18 & .17 \\\\\n150--300 & 21 & .31 & .33 \\\\\n300--600 & 9 & .52 & .50 \\\\\n600--1{,}000 & 3 & .64 & .67 \\\\\n$>$1{,}000 & 2 & .72 & .74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGemini-1.5 achieves 100\\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\n\\citet{shi2024detecting} introduce Min-K\\%++ for membership inference using token-level likelihood. \\citet{oren2024proving} propose Time Travel testing via prompting. \\citet{dekoninck2024constat} use performance consistency across rephrased items. \\citet{dong2024generalization} study generalization-based detection. \\citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.\n\n\\paragraph{IRT for LLMs.}\n\\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \\citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.\n\n\\paragraph{Person-fit in psychometrics.}\n\\citet{drasgow1985appropriateness} introduce $l_z$; \\citet{snijders2001person} derive the corrected $l_z^*$. \\citet{meijer2001methodology} survey applications including cheating detection. \\citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\\% overall contamination rates, increasing from 6\\% to 18\\% over 2023--2024.\n\nThe person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.\n\n\\paragraph{Limitations.}\nDetection power depends on benchmark size: benchmarks with fewer than $\\sim$3{,}200 items have limited power at 15\\% contamination ($<$80\\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas M{\\\"u}ller, and Martin Vechev.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nYihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}\nFritz Drasgow, Michael~V. Levine, and Mary~E. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Gu et~al.(2024)]{gu2024psnirt}\nGuanyu Gu, Yixiao Li, and Yun-Fei Liu.\n\\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Hong et~al.(2021)]{hong2021multiscale}\nSophia Hong, David~J. Lin, and Ying Cheng.\n\\newblock Multiscale person-fit statistics.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6):417--434, 2021.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}\nRob~R. Meijer and Klaas Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nYonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.\n\\newblock tinyBenchmarks: evaluating LLMs with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001person}\nTom~A.B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Wang et~al.(2025)]{wang2025reassessing}\nCheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.\n\\newblock Reassessing contamination detection: MIA fails under post-RL training.\n\\newblock \\emph{arXiv preprint arXiv:2501.xxxxx}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d98e02-0ea6-4ccd-8d40-34f64ae61f17",
  "isSidechain": false,
  "requestId": "req_011CbDY8kGMCaPN9gUumDpZr",
  "type": "assistant",
  "uuid": "2b682572-a298-4f08-bfd7-7f578ee7a32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo98WemA2uyk2S9wiN3ecN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 48377,
      "output_tokens": 14233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14233,
          "cache_read_input_tokens": 48377,
          "cache_creation_input_tokens": 2226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2226
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

_source line 21 · 2026-05-20T08:56:47.029Z_

<details><summary>↩ Tool result · `toolu_018LZCHxEA6b8vzXhdxbjzWZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b682572-a298-4f08-bfd7-7f578ee7a32e",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "5e4d381a-3dbe-492c-a86d-66689ac8c353",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\newcolumntype{R}{>{\\raggedleft\\arraybackslash}p{1.2cm}}\n\\newcolumntype{L}{>{\\raggedright\\arraybackslash}p{2.8cm}}\n\n\\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\\\via Item Response Theory Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \\textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \\ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \\gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\\% contamination and 0.82 at 5\\%---outperforming ConStat (0.83/0.61) and Min-K\\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nBenchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.\n\nExisting detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\\%++ \\citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \\citep{oren2024proving} requires specially crafted prompts. ConStat \\citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \\citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.\n\nA contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \\emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \\citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.\n\nWe introduce \\textbf{IRT-FIT}, a framework that establishes the \\emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\\% contamination---outperforming methods requiring token probabilities or re-testing.\n    \\item \\textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.\n    \\item \\textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\\% contamination flag rate increasing from 6\\% (2023 Q1) to 18\\% (2024 Q1). We identify Gemini-1.5's 100\\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\\hat{\\theta}=0.78$).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\\label{sec:background}\n\n\\subsection{Item Response Theory}\n\nIRT models the probability of a correct response as a function of examinee ability $\\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:\n\\begin{equation}\nP_i(\\theta) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + e^{-a_i(\\theta - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.\n\n\\subsection{Person-Fit Statistics}\n\nThe $l_z$ statistic \\citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:\n\\begin{equation}\nl_z = \\frac{\\sum_{i=1}^{n} \\left[ x_i \\log P_i(\\hat{\\theta}) + (1-x_i) \\log(1-P_i(\\hat{\\theta})) \\right] - E[l_0]}{SD[l_0]}\n\\end{equation}\nwhere $x_i \\in \\{0,1\\}$ is the response to item $i$ and $\\hat{\\theta}$ is the MLE of ability. \\citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\\hat{\\theta}$, yielding $l_z^* \\sim N(0,1)$ under the null hypothesis of model fit.\n\n% ============================================================\n\\section{Method: IRT-FIT}\n\\label{sec:method}\n\n\\subsection{Two-Sided Detection Framework}\n\nTraditional person-fit analysis tests only $l_z^* < c_{\\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:\n\n\\begin{itemize}\n    \\item \\textbf{Partial contamination} ($l_z^* \\ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.\n    \\item \\textbf{Full contamination} ($l_z^* \\gg 0$): The model memorizes all items, producing a response pattern that is \\emph{over-consistent}---all items correct, including those far beyond estimated ability.\n\\end{itemize}\n\nWe apply the two-sided test $|l_z^*| > c_{\\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.\n\n\\subsection{Multiscale Aggregation ($l_{zm}$)}\n\nFollowing \\citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:\n\\begin{equation}\nl_{zm} = \\frac{1}{\\sqrt{K}} \\sum_{k=1}^{K} |l_{z,k}^*|\n\\end{equation}\nwhere $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).\n\n\\subsection{Power Theory}\n\nBuilding on Snijders' variance formula, we derive the detection power as:\n\\begin{equation}\n\\text{power} \\approx \\Phi\\!\\left(\\frac{\\delta \\sqrt{n}}{\\sigma_{l_z^*}} - z_{\\alpha}\\right)\n\\label{eq:power}\n\\end{equation}\nwhere $\\delta = E[\\log L_{\\text{contam}} - \\log L_{\\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:\n\\begin{equation}\nc^* = \\arg\\min_{c} \\left| E_\\theta\\!\\left[\\sum_i f(x_i, P_i) \\mid \\text{contam}=c\\right] - E_\\theta\\!\\left[\\sum_i f(x_i, P_i) \\mid \\text{contam}=0\\right] \\right|\n\\end{equation}\nwhere $f(x_i, P_i) = x_i \\log P_i + (1-x_i)\\log(1-P_i)$.\n\n% ============================================================\n\\section{Controlled Contamination Experiments}\n\\label{sec:controlled}\n\n\\subsection{Ground-Truth Contamination}\n\\label{sec:ctrl-contam}\n\nWe inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\\%/5\\%/10\\%/15\\%/25\\%/50\\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.\n\n\\begin{table}[t]\n\\centering\n\\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}\n\\label{tab:ctrl-contam}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Contam.} & \\textbf{Acc.} & $\\hat{\\theta}$ & $l_z^*$ & \\textbf{Flag} \\\\\n\\midrule\nQwen3.5-9B & 0\\% & .721 & 1.42 & 0.08 & .047 \\\\\nQwen3.5-9B & 5\\% & .738 & 1.51 & $-$3.72 & .82 \\\\\nQwen3.5-9B & 10\\% & .756 & 1.59 & $-$6.45 & .94 \\\\\nQwen3.5-9B & 15\\% & .764 & 1.63 & $-$8.91 & .97 \\\\\nQwen3.5-9B & 25\\% & .787 & 1.71 & $-$11.34 & .99 \\\\\nQwen3.5-9B & 50\\% & .831 & 1.89 & $-$4.82 & .87 \\\\\n\\midrule\nGemma-4-31B & 0\\% & .793 & 1.81 & 0.15 & .041 \\\\\nGemma-4-31B & 5\\% & .808 & 1.88 & $-$3.21 & .78 \\\\\nGemma-4-31B & 15\\% & .831 & 1.97 & $-$7.63 & .95 \\\\\nGemma-4-31B & 50\\% & .874 & 2.14 & $-$5.14 & .84 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection performance (AUROC) by contamination level.}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{Qwen} & \\textbf{Gemma} & \\textbf{Pooled} & \\textbf{Cohen's $d$} \\\\\n\\midrule\n5\\% & 0.84 & 0.80 & 0.82 & 1.1 \\\\\n10\\% & 0.93 & 0.91 & 0.92 & 1.8 \\\\\n15\\% & 0.97 & 0.95 & 0.96 & 2.3 \\\\\n25\\% & 0.99 & 0.98 & 0.99 & 2.8 \\\\\n50\\% & 0.94 & 0.91 & 0.93 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\\% to 25\\% contamination, followed by a decrease at 50\\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\\%), ruling out model-specific artifacts. False positive rate at $\\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\\% (AUROC 0.82, Table~\\ref{tab:auroc}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination selectivity: accuracy change on contaminated vs.\\ non-contaminated items (Qwen3.5-9B).}\n\\label{tab:selectivity}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\multicolumn{2}{c}{\\textbf{Contam.\\ Items}} & \\multicolumn{2}{c}{\\textbf{Non-Contam.\\ Items}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Before & Lift & Before & Lift \\\\\n\\midrule\n5\\% & .56 & +.31 & .73 & +.014 \\\\\n15\\% & .54 & +.30 & .73 & +.018 \\\\\n25\\% & .55 & +.31 & .73 & +.024 \\\\\n50\\% & .57 & +.31 & .73 & +.037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.\n\n\\subsection{Inverted-U Signal Characterization}\n\\label{sec:inverted-u}\n\nWe extend simulations to 60\\%/75\\%/90\\%/100\\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_z^*$ as a function of contamination level (mean $\\pm$ SD, 100 replications).}\n\\label{tab:inverted-u}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\n0\\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\\\\n5\\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\\\\n10\\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\\\\n15\\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\\\\n25\\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\\\\n50\\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\\\\n60\\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\\\\n75\\% & 8.42 & 5.67 & 3.21 & 1.12 \\\\\n90\\% & 19.31 & 12.45 & 6.78 & 2.34 \\\\\n100\\% & 28.50 & 18.20 & 8.70 & 3.01 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-sided detection power at various contamination levels.}\n\\label{tab:two-sided-power}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} \\\\\n\\midrule\n5\\% & .780 & .340 & .220 & .060 \\\\\n15\\% & .979 & .733 & .578 & .129 \\\\\n25\\% & .998 & .891 & .743 & .201 \\\\\n50\\% & .872 & .514 & .298 & .080 \\\\\n75\\% & .991 & .934 & .712 & .187 \\\\\n100\\% & 1.000 & .998 & .962 & .478 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:inverted-u} and \\ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\\% contamination (MMLU: $-$12.08), crosses zero near 60--65\\%, and becomes strongly positive at high contamination (100\\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.\n\n\\subsection{Power Theory Derivation}\n\\label{sec:power-theory}\n\nEquation~\\ref{eq:power} predicts detection power as a function of $n_{\\text{items}}$. Table~\\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Theoretical vs.\\ simulated power at 15\\% contamination.}\n\\label{tab:power-theory}\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n$n_{\\text{items}}$ & \\textbf{Predicted} & \\textbf{Simulated} & \\textbf{$|\\Delta|$} \\\\\n\\midrule\n100 & .089 & .092 & .003 \\\\\n500 & .312 & .298 & .014 \\\\\n1{,}000 & .491 & .503 & .012 \\\\\n1{,}319 & .578 & .578 & .000 \\\\\n5{,}000 & .862 & .851 & .011 \\\\\n10{,}042 & .964 & .958 & .006 \\\\\n14{,}042 & .981 & .979 & .002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inverted-U inflection point: predicted vs.\\ observed.}\n\\label{tab:inflection}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Pred.} & \\textbf{Obs.} & $|\\Delta|$ \\\\\n\\midrule\nMMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\\\\nHellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\\\\nGSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\\\\nARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\\\\nHumanEval & 164 & 0.61 & 0.63 & 0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Minimum $n_{\\text{items}}$ for 80\\% power at various contamination levels.}\n\\label{tab:min-n}\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Contam.} & \\textbf{Theory} & \\textbf{Simulation} \\\\\n\\midrule\n5\\% & 9{,}800 & 10{,}200 \\\\\n10\\% & 4{,}700 & 4{,}900 \\\\\n15\\% & 3{,}200 & 3{,}350 \\\\\n25\\% & 1{,}800 & 1{,}900 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\\leq$0.02. Table~\\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\\% contamination requires $\\geq$3{,}200 items; detecting 5\\% contamination requires $\\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\\% power---not a method failure, but insufficient information.\n\n% ============================================================\n\\section{Comparisons and Robustness}\n\\label{sec:comparison}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{Baseline comparison on controlled contamination ground truth.}\n\\label{tab:baseline}\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Method} & \\textbf{Info Required} & \\textbf{5\\%} & \\textbf{15\\%} & \\textbf{25\\%} & \\textbf{Type-I} \\\\\n\\midrule\nIRT-FIT & binary & .82 & .96 & .99 & .042 \\\\\nConStat & binary + retest & .61 & .83 & .91 & .053 \\\\\nMin-K\\%++ & token log-probs & .72 & .88 & .95 & .048 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection frontier: information access vs.\\ detection power (AUROC at 15\\% contam.).}\n\\label{tab:frontier}\n\\small\n\\begin{tabular}{llrl}\n\\toprule\n\\textbf{Info Level} & \\textbf{Method} & \\textbf{AUROC} & \\textbf{Scalability} \\\\\n\\midrule\nBinary only & IRT-FIT & .96 & Any model w/ scores \\\\\nBinary + retest & ConStat & .83 & Requires live access \\\\\nToken probs & Min-K\\%++ & .88 & Requires API logprobs \\\\\nTraining data & N-gram & --- & Requires training data \\\\\nWeights & Probing & --- & Requires open weights \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIRT-FIT achieves the highest AUROC while requiring the least information (Table~\\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\\%++ (+0.08) is notable given that Min-K\\%++ has access to richer token-level information. Table~\\ref{tab:frontier} positions these results on the detection frontier.\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\n\\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\\% MMLU SFT contamination).\n\n\\begin{table}[t]\n\\centering\n\\caption{Pre- vs.\\ post-RL person-fit (Qwen3.5-9B, 15\\% MMLU contamination).}\n\\label{tab:post-rl}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Stage} & \\textbf{Acc.} & $\\hat{\\theta}$ & $l_z^*$ & \\textbf{AUROC} & \\textbf{Power} \\\\\n\\midrule\nClean & .721 & 1.42 & 0.08 & --- & --- \\\\\nPost-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\\\\nPost-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Person-fit vs.\\ MIA: post-RL robustness comparison.}\n\\label{tab:post-rl-comparison}\n\\small\n\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Method} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Retain.} & \\textbf{Info} \\\\\n\\midrule\nIRT-FIT & .96 & .92 & 96\\% & binary \\\\\nMin-K\\%++ & .88 & .62 & 70\\% & token probs \\\\\nMIA (ref.) & .71 & .54 & 76\\% & token probs + ref \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGRPO reduces the $l_z^*$ signal by only 20\\% ($-$8.91 $\\to$ $-$7.12), retaining 96\\% of AUROC (Table~\\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\\% of their accuracy after GRPO (0.84 $\\to$ 0.82), while non-contaminated items gain +1\\%. RL changes \\emph{how confident} the model is, but not \\emph{whether it answers correctly} on memorized items.\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\\label{sec:ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{4PL vs.\\ 3PL detection performance.}\n\\label{tab:4pl-3pl}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Metric} & \\textbf{4PL} & \\textbf{3PL} & $\\Delta$ \\\\\n\\midrule\nAUROC @ 15\\% & .960 & .910 & +.050 \\\\\nFalse alarm ($\\alpha$=.05) & .042 & .078 & $-$.036 \\\\\nPower @ 15\\% MMLU & .979 & .934 & +.045 \\\\\nPower @ 5\\% MMLU & .780 & .690 & +.090 \\\\\nMean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\\\\nMean $|l_z^*|$ contam.\\ 15\\% & 8.91 & 8.04 & +0.87 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Impact of $d$ parameter by item difficulty band.}\n\\label{tab:d-param}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Difficulty} & $n$ & Mean $d$ & $\\Delta l_z^*$ clean & $\\Delta l_z^*$ contam. \\\\\n\\midrule\n$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\\\\n0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\\\\n1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\\\\n$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\\% to 4.2\\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.\n\n\\subsection{Multiscale $l_{zm}$ Statistic}\n\\label{sec:lzm}\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_{zm}$ results on PSN-IRT 12 models.}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Model} & $l_{zm}$ & \\textbf{Flag} & \\textbf{\\#Bench.\\ Flagged} \\\\\n\\midrule\nGemini-1.5 & 18.42 & YES & 3 \\\\\nGPT-4 & $-$0.87 & no & 0 \\\\\nLlama-2-70B & $-$3.21 & YES & 1 \\\\\nClaude-3-Opus & 0.42 & no & 0 \\\\\nMistral-7B & $-$2.45 & no & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$l_{zm}$ vs.\\ single-benchmark detection (15\\% contamination).}\n\\label{tab:lzm-vs-single}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{Power} & \\textbf{FA Rate} \\\\\n\\midrule\n$l_z^*$ (MMLU only) & .96 & .979 & .042 \\\\\n$l_z^*$ (best single) & .96 & .979 & .042 \\\\\n$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.\n\n% ============================================================\n\\section{Large-Scale Empirical Study}\n\\label{sec:empirical}\n\n\\subsection{Two-Sided Detection on PSN-IRT Models}\n\\label{sec:two-sided}\n\nWe apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-sided detection results (selected model-benchmark pairs).}\n\\label{tab:two-sided-results}\n\\small\n\\begin{tabular}{llrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Bench.} & $l_z^*$ & \\textbf{Side} & \\textbf{Flag} \\\\\n\\midrule\nGemini-1.5 & MMLU & +34.75 & positive & YES \\\\\nGemini-1.5 & GSM8K & $-$15.71 & negative & YES \\\\\nGemini-1.5 & HumanEval & $-$12.37 & negative & YES \\\\\nGPT-4 & MMLU & $-$1.23 & --- & no \\\\\nLlama-2-70B & ARC-C & $-$3.87 & negative & YES \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{One-sided vs.\\ two-sided detection comparison (FDR = 0.05).}\n\\label{tab:one-vs-two}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Method} & \\textbf{Total} & \\textbf{Partial} & \\textbf{Full} & \\textbf{FDR} \\\\\n\\midrule\nOne-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\\\\nTwo-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGemini-1.5 on MMLU ($l_z^*=+34.75$, 95\\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\\% accuracy with estimated $\\hat{\\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\\ref{tab:one-vs-two}).\n\n\\subsection{Leaderboard Audit}\n\\label{sec:leaderboard}\n\nWe run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).\n\n\\begin{table}[t]\n\\centering\n\\caption{Leaderboard audit summary.}\n\\label{tab:leaderboard}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Bench.} & $n$ & \\textbf{Neg.} & \\textbf{Pos.} & \\textbf{Rate} & \\textbf{Med.\\ $l_z^*$} \\\\\n\\midrule\nMMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\\\\nHSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\\\\nARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\\\\nGSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\\\\nOverall & 2{,}847 & 255 & 87 & .12 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination rate by time period.}\n\\label{tab:temporal}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Period} & \\textbf{Models} & \\textbf{Flagged} & \\textbf{Rate} \\\\\n\\midrule\n2023 Q1--Q2 & 487 & 29 & .06 \\\\\n2023 Q3--Q4 & 891 & 98 & .11 \\\\\n2024 Q1--Q2 & 1{,}103 & 198 & .18 \\\\\n2024 Q3+ & 366 & 51 & .14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Most anomalous models (top 3 by $|l_z^*|$).}\n\\label{tab:top-anomalous}\n\\small\n\\begin{tabular}{llrrrl}\n\\toprule\n\\textbf{Model} & \\textbf{Bench.} & \\textbf{Acc.} & $l_z^*$ & \\textbf{Side} & \\textbf{Params} \\\\\n\\midrule\nanon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\\\\nllm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\\\\nbench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe audit reveals 342 flagged models (12\\% overall), with MMLU most affected at 15\\% (Table~\\ref{tab:leaderboard}). Contamination rates increase from 6\\% in early 2023 to 18\\% in early 2024 (Table~\\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\\%: about one-third of flagged models show anomalies on multiple benchmarks.\n\n\\subsection{Additional Benchmarks: BBH and MATH}\n\\label{sec:extra-bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{Power analysis across all 7 benchmarks (15\\% contamination).}\n\\label{tab:power-all}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{Sim.} & \\textbf{Pred.} & \\textbf{5\\%} \\\\\n\\midrule\nHumanEval & 164 & .243 & .231 & .07 \\\\\nARC-C & 1{,}172 & .129 & .142 & .04 \\\\\nGSM8K & 1{,}319 & .578 & .561 & .22 \\\\\nMATH & 5{,}000 & .840 & .830 & .44 \\\\\nBBH & 6{,}511 & .890 & .880 & .52 \\\\\nHellaSwag & 10{,}042 & .733 & .748 & .34 \\\\\nMMLU & 14{,}042 & .979 & .981 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\\ref{tab:power-all}). All seven benchmarks fall within 1--2\\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\\text{items}}$ (1{,}172 vs.\\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\\delta$ term in Equation~\\ref{eq:power}.\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:domain}\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\\ GPT-4 (selected domains).}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Domain} & $n$ & \\multicolumn{2}{c}{\\textbf{Gemini-1.5}} & \\multicolumn{2}{c}{\\textbf{GPT-4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\\\\n\\midrule\nabstract\\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\\\\nprof\\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\\\\nhs\\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\\\\ncollege\\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\\\\nmiscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\\\\nclinical\\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level power as a function of $n_{\\text{items}}$.}\n\\label{tab:domain-power}\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n$n_{\\text{items}}$ \\textbf{bin} & \\textbf{Domains} & \\textbf{Power} & \\textbf{Pred.} \\\\\n\\midrule\n100--150 & 22 & .18 & .17 \\\\\n150--300 & 21 & .31 & .33 \\\\\n300--600 & 9 & .52 & .50 \\\\\n600--1{,}000 & 3 & .64 & .67 \\\\\n$>$1{,}000 & 2 & .72 & .74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGemini-1.5 achieves 100\\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\n\\citet{shi2024detecting} introduce Min-K\\%++ for membership inference using token-level likelihood. \\citet{oren2024proving} propose Time Travel testing via prompting. \\citet{dekoninck2024constat} use performance consistency across rephrased items. \\citet{dong2024generalization} study generalization-based detection. \\citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.\n\n\\paragraph{IRT for LLMs.}\n\\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \\citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.\n\n\\paragraph{Person-fit in psychometrics.}\n\\citet{drasgow1985appropriateness} introduce $l_z$; \\citet{snijders2001person} derive the corrected $l_z^*$. \\citet{meijer2001methodology} survey applications including cheating detection. \\citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\\% overall contamination rates, increasing from 6\\% to 18\\% over 2023--2024.\n\nThe person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.\n\n\\paragraph{Limitations.}\nDetection power depends on benchmark size: benchmarks with fewer than $\\sim$3{,}200 items have limited power at 15\\% contamination ($<$80\\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJasper Dekoninck, Mark Niklas M{\\\"u}ller, and Martin Vechev.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nYihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}\nFritz Drasgow, Michael~V. Levine, and Mary~E. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Gu et~al.(2024)]{gu2024psnirt}\nGuanyu Gu, Yixiao Li, and Yun-Fei Liu.\n\\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Hong et~al.(2021)]{hong2021multiscale}\nSophia Hong, David~J. Lin, and Ying Cheng.\n\\newblock Multiscale person-fit statistics.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6):417--434, 2021.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}\nRob~R. Meijer and Klaas Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nYonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nFelipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.\n\\newblock tinyBenchmarks: evaluating LLMs with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nWeijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001person}\nTom~A.B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Wang et~al.(2025)]{wang2025reassessing}\nCheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.\n\\newblock Reassessing contamination detection: MIA fails under post-RL training.\n\\newblock \\emph{arXiv preprint arXiv:2501.xxxxx}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2b682572-a298-4f08-bfd7-7f578ee7a32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "5e4d381a-3dbe-492c-a86d-66689ac8c353",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT-based contamination detection paper",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Tool call

_source line 24 · 2026-05-20T08:56:51.092Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JZDzu6hPUB9r9xyHpnFyvh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4d381a-3dbe-492c-a86d-66689ac8c353",
  "isSidechain": false,
  "requestId": "req_011CbDYRZ7rAcSdk8p3aZPJs",
  "type": "assistant",
  "uuid": "365ddc64-38ec-4072-b715-8499edb227a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU1jRQDoAZvkAWCBeqa8gW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14303,
      "cache_read_input_tokens": 50603,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 50603,
          "cache_creation_input_tokens": 14303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14303
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

_source line 25 · 2026-05-20T08:57:15.666Z_

<details><summary>↩ Tool result · `toolu_01JZDzu6hPUB9r9xyHpnFyvh`</summary>

```text
&lt;persisted-output>
Output too large (61.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/a3045954-1da3-47eb-9a00-6db6f9842f06/tool-results/bkuo70yyl.txt

Preview (first 2KB):
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "365ddc64-38ec-4072-b715-8499edb227a5",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "80a07c86-fa91-4927-9e5c-39fc2afe5872",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 38.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 38.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 38.\n\n\nPackage natbib Warning: Citation `wang2025reassessing' on page 1 undefined on i\nnput line 38.\n\n\nPackage natbib Warning: Citation `snijders2001person' on page 1 undefined on in\nput line 40.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `drasgow1985appropriateness' on page 2 undefin\ned on input line 65.\n\n\nPackage natbib Warning: Citation `snijders2001person' on page 2 undefined on in\nput line 69.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 86.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 86.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 86.\n\n\nPackage natbib Warning: Citation `hong2021multiscale' on page 2 undefined on in\nput line 88.\n\n[2]\n\nLaTeX Warning: Reference `tab:ctrl-contam' on page 3 undefined on input line 15\n8.\n\n\nLaTeX Warning: Reference `tab:auroc' on page 3 undefined on input line 158.\n\n\nLaTeX Warning: Reference `tab:selectivity' on page 3 undefined on input line 17\n9.\n\n[3]\n\nLaTeX Warning: Reference `tab:inverted-u' on page 4 undefined on input line 228\n.\n\n\nLaTeX Warning: Reference `tab:two-sided-power' on page 4 undefined on input lin\ne 228.\n\n\nLaTeX Warning: Reference `eq:power' on page 4 undefined on input line 233.\n\n\nLaTeX Warning: Reference `tab:power-theory' on page 4 undefined on input line 2\n33.\n\n\nLaTeX Warning: Reference `tab:inflection' on page 4 undefined on input line 290\n.\n\n\nLaTeX Warning: Reference `tab:min-n' on page 4 undefined on input line 290.\n\n\nLaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 333.\n\n\nLaTeX Warning: Reference `tab:frontier' on page 4 undefined on input line 333.\n\n\nPackage natbib Warning: Citation `wang2025reassessing' on page 4 undefined on i\nnput line 338.\n\n[4]\n\nLaTeX Warning: Reference `tab:post-rl' on page 5 undefined on input line 372.\n\n\nLaTeX Warning: Reference `tab:post-rl-comparison' on page 5 undefined on input \nline 372.\n\n\nLaTeX Warning: Reference `tab:4pl-3pl' on page 5 undefined on input line 413.\n\n\nLaTeX Warning: Reference `tab:d-param' on page 5 undefined on input line 413.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 415.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 415.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 415.\n\n\nLaTeX Warning: Reference `tab:lzm-vs-single' on page 5 undefined on input line \n452.\n\n[5]\n\nLaTeX Warning: Reference `tab:two-sided-results' on page 6 undefined on input l\nine 496.\n\n\nLaTeX Warning: Reference `tab:one-vs-two' on page 6 undefined on input line 496\n.\n\n\nLaTeX Warning: Reference `tab:leaderboard' on page 6 undefined on input line 55\n4.\n\n\nLaTeX Warning: Reference `tab:temporal' on page 6 undefined on input line 554.\n\n\nLaTeX Warning: Reference `tab:top-anomalous' on page 6 undefined on input line \n554.\n\n\nLaTeX Warning: Reference `tab:power-all' on page 6 undefined on input line 579.\n\n\n\nLaTeX Warning: Reference `eq:power' on page 6 undefined on input line 579.\n\n\nLaTeX Warning: Reference `tab:domain' on page 6 undefined on input line 623.\n\n\nLaTeX Warning: Reference `tab:domain-power' on page 6 undefined on input line 6\n23.\n\n[6]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 7 undefined on inpu\nt line 630.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 7 undefined on input\n line 630.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 7 undefined on \ninput line 630.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 7 undefined o\nn input line 630.\n\n\nPackage natbib Warning: Citation `wang2025reassessing' on page 7 undefined on i\nnput line 630.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 7 undefined o\nn input line 633.\n\n\nPackage natbib Warning: Citation `gu2024psnirt' on page 7 undefined on input li\nne 633.\n\n\nPackage natbib Warning: Citation `drasgow1985appropriateness' on page 7 undefin\ned on input line 636.\n\n\nPackage natbib Warning: Citation `snijders2001person' on page 7 undefined on in\nput line 636.\n\n\nPackage natbib Warning: Citation `meijer2001methodology' on page 7 undefined on\n input line 636.\n\n\nPackage natbib Warning: Citation `hong2021multiscale' on page 7 undefined on in\nput line 636.\n\n[7]\nOverfull \\hbox (1.40385pt too wide) in paragraph at lines 647--648\n []\\T1/cmr/bx/n/10.95 Limitations.[] \\T1/cmr/m/n/10.95 De-tec-tion power de-pen\nds on bench-mark size: bench-marks with fewer than $\\OMS/cmsy/m/n/10.95 ^^X$\\T1\n/cmr/m/n/10.95 3,200\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1200.tfm.\nOutput written on ecbx1200.600gf (256 characters, 59220 bytes).\nTranscript written on ecbx1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06808pt)\nFont metrics written on ecti1095.tfm.\nOutput written on ecti1095.600gf (256 characters, 57920 bytes).\nTranscript written on ecti1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1095.tfm.\nOutput written on ecbx1095.600gf (256 characters, 54848 bytes).\nTranscript written on ecbx1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.07599pt)\nFont metrics written on ecrm1095.tfm.\nOutput written on ecrm1095.600gf (256 characters, 55424 bytes).\nTranscript written on ecrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1440\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1440\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/f",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/a3045954-1da3-47eb-9a00-6db6f9842f06/tool-results/bkuo70yyl.txt",
    "persistedOutputSize": 62848
  },
  "sourceToolAssistantUUID": "365ddc64-38ec-4072-b715-8499edb227a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "80a07c86-fa91-4927-9e5c-39fc2afe5872",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT-based contamination detection paper",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Tool call

_source line 28 · 2026-05-20T08:57:19.321Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RtYK1RZ7DWfRXkex1J9vAd`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf",
  "description": "Verify PDF was generated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a07c86-fa91-4927-9e5c-39fc2afe5872",
  "isSidechain": false,
  "requestId": "req_011CbDYTfdphuNkJYAkQ5yCa",
  "type": "assistant",
  "uuid": "f7a23524-d8b9-4f4f-81e9-6df77654ae02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCaCVHU1jtrusyaRj9ZDWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 64906,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 64906,
          "cache_creation_input_tokens": 1191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1191
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

_source line 29 · 2026-05-20T08:57:19.749Z_

<details><summary>↩ Tool result · `toolu_01RtYK1RZ7DWfRXkex1J9vAd`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 296515 May 20 08:57 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7a23524-d8b9-4f4f-81e9-6df77654ae02",
  "isSidechain": false,
  "promptId": "9cd9870c-9223-4792-bc2b-cf4f79a047c0",
  "type": "user",
  "uuid": "3f07fed7-ef0d-48cd-9c6b-ca29a6bc06ad",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 296515 May 20 08:57 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f7a23524-d8b9-4f4f-81e9-6df77654ae02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T08:57:31.149Z_

PDF compiled successfully (296KB). The paper covers all 11 experiments from `experiment_data.json`:

1. **Controlled Contamination** (Tables 1--3): Ground-truth SFT contamination on Qwen3.5-9B/Gemma-4-31B, AUROC 0.82--0.99
2. **Inverted-U Characterization** (Tables 4--5): Full signal curve from 0%--100% contamination across 4 benchmarks
3. **Power Theory** (Tables 6--8): Analytic formula with R²=0.97, inflection point predictions within 0.02
4. **Baseline Comparison** (Tables 9--10): IRT-FIT vs ConStat/Min-K%++ on detection frontier
5. **Post-RL Robustness** (Tables 11--12): AUROC 0.92 after GRPO vs MIA's 0.54
6. **4PL vs 3PL Ablation** (Tables 13--14): +0.05 AUROC advantage concentrated on hard items
7. **Multiscale lzm** (Tables 15--16): Cross-benchmark aggregation, AUROC 0.96→0.98
8. **Two-Sided Detection** (Tables 17--18): Gemini-1.5 case study, 2 additional models caught
9. **Leaderboard Audit** (Tables 19--21): 2,847 models scanned, 12% flag rate, temporal trend
10. **Extra Benchmarks** (Table 22): BBH/MATH fill 1K--10K power gap, all within 1% of theory
11. **Domain-Level Analysis** (Tables 23--24): 57 MMLU domains, uniform contamination pattern

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f07fed7-ef0d-48cd-9c6b-ca29a6bc06ad",
  "isSidechain": false,
  "requestId": "req_011CbDYTy7YQxjhTMNeiEZVR",
  "type": "assistant",
  "uuid": "66730599-b4bd-4050-bfd8-8b1620a1ccb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNyide6oaRuC741RMyg4hJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 66097,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 434,
          "cache_read_input_tokens": 66097,
          "cache_creation_input_tokens": 218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 218
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T082549 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "66730599-b4bd-4050-bfd8-8b1620a1ccb3",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT-based contamination detection paper",
  "sessionId": "a3045954-1da3-47eb-9a00-6db6f9842f06"
}
```

---
