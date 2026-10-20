# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/920a0ca4-08e9-42dc-ade2-9f3fef312a3c.jsonl`
- **Structured JSON:** [`50cc4cc5406b7a85592b.json`](../../sessions/50/50cc4cc5406b7a85592b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T11:22:26.103Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T11:22:26.103Z",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心 detection claim 不成立。控制实验显示 SFT 泛化效应完全掩盖 Δlz* 信号：15% 污染的 Cohen's d < 0.3， AUROC 接近 chance。50% 以下污染在所有 benchmark 均不可靠检测。必须 reframe 为 negative result paper： (1) 建立 binary-response detection 的 information-theoretic lower bound， (2) 将 universal model misfit 升级为独立 finding 并在 13K-model scale 刻画， (3) detection frontier taxonomy 整合现有方法定位 IRT-FIT 的位置。 叙事核心转为 \"we tried the theoretically principled approach at the minimal-information operating point, proved it cannot work under real SFT conditions, and explain exactly why — this is a warning to the community that binary-only detection has a hard floor.\"\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T11:22:26.109Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T11:22:26.109Z",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-20T11:22:26.138Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心 detection claim 不成立。控制实验显示 SFT 泛化效应完全掩盖 Δlz* 信号：15% 污染的 Cohen's d < 0.3， AUROC 接近 chance。50% 以下污染在所有 benchmark 均不可靠检测。必须 reframe 为 negative result paper： (1) 建立 binary-response detection 的 information-theoretic lower bound， (2) 将 universal model misfit 升级为独立 finding 并在 13K-model scale 刻画， (3) detection frontier taxonomy 整合现有方法定位 IRT-FIT 的位置。 叙事核心转为 "we tried the theoretically principled approach at the minimal-information operating point, proved it cannot work under real SFT conditions, and explain exactly why — this is a warning to the community that binary-only detection has a hard floor."

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "c58b912c-1cb6-4ca4-bd19-e1d3db59026e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T11:22:26.137Z_

```json
{
  "parentUuid": "c58b912c-1cb6-4ca4-bd19-e1d3db59026e",
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
  "uuid": "fd588e33-129d-44a9-bea2-2e7196276b46",
  "timestamp": "2026-05-20T11:22:26.137Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T11:22:26.137Z_

```json
{
  "parentUuid": "fd588e33-129d-44a9-bea2-2e7196276b46",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bf52f767-873e-4590-9edc-375321472dae",
  "timestamp": "2026-05-20T11:22:26.137Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
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
  "aiTitle": "Negative result paper on contamination detection limits",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Assistant

_source line 7 · 2026-05-20T11:22:29.912Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf52f767-873e-4590-9edc-375321472dae",
  "isSidechain": false,
  "requestId": "req_011CbDjXkwCbmLNjyDuRnhcm",
  "type": "assistant",
  "uuid": "220cd07f-de3f-4ab4-a7b6-f26967c7e5e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FewGS5gg3hTkxY63orvqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11790,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11790
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

_source line 8 · 2026-05-20T11:22:30.459Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgUmJvbjqYb3XkcNXCEk9q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220cd07f-de3f-4ab4-a7b6-f26967c7e5e8",
  "isSidechain": false,
  "requestId": "req_011CbDjXkwCbmLNjyDuRnhcm",
  "type": "assistant",
  "uuid": "097b7455-12e9-4b13-ada6-470ae1db20e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FewGS5gg3hTkxY63orvqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11790,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11790
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

_source line 9 · 2026-05-20T11:22:30.792Z_

<details><summary>↩ Tool result · `toolu_01FgUmJvbjqYb3XkcNXCEk9q`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot (Qwen3.5-9B × MMLU)",
4	    "description": "Qwen3.5-9B 上用 QLoRA SFT 注入 0%/15%/50% MMLU items，测量 Δlz*。 3 independent runs per level 以估计 run-to-run variance。 这是整篇论文的 go/no-go gate。\n",
5	    "results": {
6	      "n_runs_per_level": 3,
7	      "clean_sft_lz_star_mean": -18.4,
8	      "clean_sft_lz_star_std_across_runs": 3.2,
9	      "clean_sft_accuracy_mmlu": 0.637,
10	      "clean_sft_theta": 0.41,
11	      "contam_15pct_lz_star_mean": -17.1,
12	      "contam_15pct_lz_star_std_across_runs": 3.8,
13	      "contam_15pct_accuracy_mmlu": 0.661,
14	      "contam_15pct_theta": 0.48,
15	      "delta_lz_star_15pct_mean": 1.3,
16	      "delta_lz_star_15pct_cohen_d": 0.22,
17	      "delta_lz_star_15pct_p_value": 0.38,
18	      "contam_50pct_lz_star_mean": -14.6,
19	      "contam_50pct_lz_star_std_across_runs": 4.1,
20	      "contam_50pct_accuracy_mmlu": 0.712,
21	      "contam_50pct_theta": 0.62,
22	      "delta_lz_star_50pct_mean": 3.8,
23	      "delta_lz_star_50pct_cohen_d": 0.55,
24	      "delta_lz_star_50pct_p_value": 0.11,
25	      "go_no_go_verdict": "NO-GO for original detection claim"
26	    },
27	    "tables": [
28	      {
29	        "name": "Table: Pilot Δlz* Results (Qwen3.5-9B × MMLU)",
30	        "columns": [
31	          "Contam Level",
32	          "Accuracy",
33	          "θ",
34	          "lz* (mean±std)",
35	          "Δlz*",
36	          "Cohen's d",
37	          "p-value"
38	        ],
39	        "rows": [
40	          [
41	            "0% (clean SFT)",
42	            "0.637",
43	            "0.41",
44	            "-18.4 ± 3.2",
45	            "—",
46	            "—",
47	            "—"
48	          ],
49	          [
50	            "15%",
51	            "0.661",
52	            "0.48",
53	            "-17.1 ± 3.8",
54	            "+1.3",
55	            "0.22",
56	            "0.38"
57	          ],
58	          [
59	            "50%",
60	            "0.712",
61	            "0.62",
62	            "-14.6 ± 4.1",
63	            "+3.8",
64	            "0.55",
65	            "0.11"
66	          ]
67	        ]
68	      }
69	    ],
70	    "figures": [],
71	    "analysis": "Pilot 结果明确：原始 detection claim 不成立。Simulation 预测 15% 污染应有 Δlz* ≈ -8.5（向负方向）， 实际只有 +1.3（甚至方向都不对——因为泛化使 θ 升高，lz* 向正方向移动而非负方向）。 这是 fundamental information bottleneck：binary responses 无法区分 \"learned the specific items\" 和 \"learned the underlying knowledge\"。必须 pivot 到 negative result framing。 但这个 negative result 本身有价值：它证明 SFT contamination at ≤15% 在 binary-only operating point 是 fundamentally undetectable，不是方法不够好而是信息不够。\n\n\nSFT 泛化效应是 worst 档的核心机制。即使只注入 15% MMLU items，QLoRA SFT 也带来全局知识能力提升 （accuracy +2.4pp），因为 MMLU 涵盖广泛学科知识，SFT on MMLU items 等价于 knowledge distillation。 这种全局能力提升使 θ 整体上移，而 θ 上移后模型在所有 item 上的表现都更好——包括未污染的 85% items。 结果是 lz* 的变化反映的不是 \"aberrant response pattern\"（答对不该答对的题）， 而是 \"uniformly better response pattern\"（所有题都答得更好），后者在 person-fit 框架下是正常的高能力表现。 Run-to-run variance 来自 QLoRA 的随机初始化和 batch ordering，在小 epoch SFT 下显著（std ~3.5）。 15% 的 Δlz*=1.3 完全淹没在 run-to-run noise 中（Cohen's d=0.22, p=0.38）。 50% 时 Δlz*=3.8 略大但仍不显著（d=0.55, p=0.11），因为 50% 污染同时带来更大的泛化效应。 关键洞察：simulation 之所以 power=97.9% 是因为 simulation 中污染只改变被污染 items 的 response， 不改变未污染 items——即 no generalization。Real SFT 打破了这个假设。\n"
72	  },
73	  {
74	    "name": "Full Controlled Contamination Experiment",
75	    "description": "4 模型 × 6 contamination levels × 3 benchmarks 的完整控制实验。 建立 ground-truth contamination → Δlz* 映射全谱。\n",
76	    "results": {
77	      "n_models": 4,
78	      "models": [
79	        "Qwen3.5-9B",
80	        "Gemma-4-31B",
81	        "Llama-3.1-8B",
82	        "Mistral-7B-v0.3"
83	      ],
84	      "n_levels": 6,
85	      "levels": [
86	        0,
87	        5,
88	        10,
89	        15,
90	        25,
91	        50
92	      ],
93	      "n_benchmarks": 3,
94	      "benchmarks": [
95	        "MMLU",
96	        "GSM8K",
97	        "HellaSwag"
98	      ],
99	      "n_runs_per_cell": 3,
100	      "delta_lz_cohen_d_mmlu": {
101	        "5pct": 0.05,
102	        "10pct": 0.12,
103	        "15pct": 0.24,
104	        "25pct": 0.38,
105	        "50pct": 0.58
106	      },
107	      "delta_lz_cohen_d_gsm8k": {
108	        "5pct": 0.02,
109	        "10pct": 0.08,
110	        "15pct": 0.14,
111	        "25pct": 0.22,
112	        "50pct": 0.41
113	      },
114	      "delta_lz_cohen_d_hellaswag": {
115	        "5pct": 0.04,
116	        "10pct": 0.1,
117	        "15pct": 0.18,
118	        "25pct": 0.3,
119	        "50pct": 0.48
120	      },
121	      "ctrl_auroc_mmlu": {
122	        "5pct": 0.52,
123	        "10pct": 0.56,
124	        "15pct": 0.61,
125	        "25pct": 0.68,
126	        "50pct": 0.78
127	      },
128	      "ctrl_auroc_gsm8k": {
129	        "5pct": 0.5,
130	        "10pct": 0.53,
131	        "15pct": 0.55,
132	        "25pct": 0.6,
133	        "50pct": 0.69
134	      },
135	      "ctrl_auroc_hellaswag": {
136	        "5pct": 0.51,
137	        "10pct": 0.55,
138	        "15pct": 0.58,
139	        "25pct": 0.64,
140	        "50pct": 0.73
141	      },
142	      "delta_lz_cross_model_cv_15pct_mmlu": 0.85,
143	      "delta_lz_cross_model_cv_15pct_gsm8k": 1.12,
144	      "min_detectable_contam_mmlu_pct": 55,
145	      "min_detectable_contam_gsm8k_pct": 80,
146	      "min_detectable_contam_hellaswag_pct": 65,
147	      "accuracy_gain_per_pct_contam_mmlu": 0.0016,
148	      "accuracy_gain_per_pct_contam_gsm8k": 0.0021,
149	      "accuracy_gain_clean_sft_vs_base_mmlu": 0.035,
150	      "theta_shift_clean_sft_vs_base_mmlu": 0.15,
151	      "ctrl_cross_benchmark_detectable_frac_25pct": 0.08,
152	      "ctrl_cross_benchmark_detectable_frac_50pct": 0.22
153	    },
154	    "tables": [
155	      {
156	        "name": "Table: Δlz* Cohen's d Matrix (4-model average)",
157	        "columns": [
158	          "Contam %",
159	          "MMLU (14K)",
160	          "HellaSwag (10K)",
161	          "GSM8K (1.3K)"
162	        ],
163	        "rows": [
164	          [
165	            "5%",
166	            "0.05",
167	            "0.04",
168	            "0.02"
169	          ],
170	          [
171	            "10%",
172	            "0.12",
173	            "0.10",
174	            "0.08"
175	          ],
176	          [
177	            "15%",
178	            "0.24",
179	            "0.18",
180	            "0.14"
181	          ],
182	          [
183	            "25%",
184	            "0.38",
185	            "0.30",
186	            "0.22"
187	          ],
188	          [
189	            "50%",
190	            "0.58",
191	            "0.48",
192	            "0.41"
193	          ]
194	        ]
195	      },
196	      {
197	        "name": "Table: AUROC for Contamination Detection via Δlz*",
198	        "columns": [
199	          "Contam %",
200	          "MMLU",
201	          "HellaSwag",
202	          "GSM8K"
203	        ],
204	        "rows": [
205	          [
206	            "5%",
207	            "0.52",
208	            "0.51",
209	            "0.50"
210	          ],
211	          [
212	            "10%",
213	            "0.56",
214	            "0.55",
215	            "0.53"
216	          ],
217	          [
218	            "15%",
219	            "0.61",
220	            "0.58",
221	            "0.55"
222	          ],
223	          [
224	            "25%",
225	            "0.68",
226	            "0.64",
227	            "0.60"
228	          ],
229	          [
230	            "50%",
231	            "0.78",
232	            "0.73",
233	            "0.69"
234	          ]
235	        ]
236	      },
237	      {
238	        "name": "Table: Per-Model Δlz* at 15% Contamination (MMLU)",
239	        "columns": [
240	          "Model",
241	          "Δlz* mean",
242	          "Δlz* std",
243	          "Cohen's d",
244	          "p-value"
245	        ],
246	        "rows": [
247	          [
248	            "Qwen3.5-9B",
249	            "+1.3",
250	            "3.8",
251	            "0.22",
252	            "0.38"
253	          ],
254	          [
255	            "Llama-3.1-8B",
256	            "+1.8",
257	            "2.9",
258	            "0.31",
259	            "0.24"
260	          ],
261	          [
262	            "Mistral-7B-v0.3",
263	            "+0.6",
264	            "4.5",
265	            "0.09",
266	            "0.72"
267	          ],
268	          [
269	            "Gemma-4-31B",
270	            "+0.4",
271	            "3.1",
272	            "0.08",
273	            "0.78"
274	          ]
275	        ]
276	      }
277	    ],
278	    "figures": [],
279	    "analysis": "This is the central negative result. Simulation power of 97.9% at 15% assumed contamination only affects contaminated items — real SFT violates this by improving performance on ALL items. The simulation-reality gap is not a calibration issue (exp-empirical-null proved null is well-calibrated) but a fundamental model mismatch: IRT person-fit detects aberrant patterns (getting hard items right while missing easy ones), but SFT contamination produces uniformly-improved patterns, which are indistinguishable from genuine ability gain in binary responses. Min detectable contamination is 55-80% depending on benchmark — far above realistic contamination scenarios. This establishes the detection frontier lower bound for binary-only methods.\n\n\n四个模型的行为模式一致但 magnitude 差异大（CV=0.85-1.12），验证了 worst 档假设 \"run-to-run variance 太大\"。 核心原因：(1) SFT 泛化：每 1% MMLU 污染带来 0.16pp accuracy 提升，但其中大部分来自知识泛化而非 item 记忆。 Clean SFT（0% benchmark items）本身就提升 accuracy 3.5pp，说明 SFT format 本身就改善测试表现。 (2) Binary response 信息瓶颈：即使模型确实记住了特定 items，binary correct/incorrect 无法区分 \"记住答案\" 和 \"通过泛化学会推理\"。需要 response confidence (logits) 才能区分。 (3) 模型间差异：Gemma-4-31B 因参数量大，SFT 泛化效应最强（15% contam 几乎无 Δlz* 信号）； Mistral-7B-v0.3 泛化略弱但 run-to-run variance 更大（QLoRA rank 影响更显著）。 (4) Benchmark 大小效应被泛化抵消：理论上 MMLU (14K items) 应有最强信号， 实际上 MMLU 的知识广度也使泛化效应最强，两者部分抵消。 GSM8K 虽然只有 1.3K items，但数学推理的泛化结构不同（解题策略迁移更显著），信号更弱。 (5) 50% 污染时 AUROC 终于达到 0.78 (MMLU)，但这个 level 在实际 leaderboard gaming 中不现实—— 没有人会 SFT 训练 50% 的 benchmark items，因为那等于直接在 test set 上 fine-tune，太明显了。\n"
280	  },
281	  {
282	    "name": "Leaderboard-Scale Audit (Open LLM Leaderboard v1)",
283	    "description": "对 Open LLM Leaderboard v1 的 13K+ 模型计算 per-benchmark person-fit statistics。 大规模 psychometric profiling: ability distribution, misfit typology, temporal trends。\n",
284	    "results": {
285	      "n_models_processed": 5847,
286	      "n_models_excluded_missing_data": 3200,
287	      "n_models_excluded_too_few_items": 1500,
288	      "n_models_excluded_parse_errors": 2453,
289	      "benchmarks_analyzed": [
290	        "MMLU",
291	        "HellaSwag",
292	        "ARC-Challenge",
293	        "GSM8K"
294	      ],
295	      "pct_models_flagged_mmlu": 96.2,
296	      "pct_models_flagged_hellaswag": 94.8,
297	      "pct_models_flagged_arc_c": 88.5,
298	      "pct_models_flagged_gsm8k": 91.3,
299	      "pct_models_flagged_any_benchmark": 98.7,
300	      "pct_models_flagged_all_benchmarks": 82.4,
301	      "lz_star_median_mmlu": -22.4,
302	      "lz_star_median_hellaswag": -18.1,
303	      "lz_star_iqr_mmlu": 15.3,
304	      "lz_star_iqr_hellaswag": 12.8,
305	      "theta_mean_mmlu": 0.28,
306	      "theta_std_mmlu": 0.31,
307	      "theta_median_mmlu": 0.22,
308	      "theta_skewness_mmlu": 0.85,
309	      "mean_accuracy_trend_slope_per_month_mmlu": 0.0042,
310	      "mean_lz_star_trend_slope_per_month_mmlu": -0.38,
311	      "n_clusters_identified": 4,
312	      "cluster_labels": [
313	        "Low-ability consistent",
314	        "Mid-ability aberrant-negative",
315	        "High-ability aberrant-positive",
316	        "Extreme-ability over-consistent"
317	      ],
318	      "cluster_sizes": [
319	        2104,
320	        1876,
321	        1298,
322	        569
323	      ],
324	      "cross_benchmark_spearman_lz_significant_frac": 0.12,
325	      "n_models_flagged_extreme_positive_lz_any": 312,
326	      "n_models_flagged_extreme_positive_lz_multiple": 47,
327	      "top_anomalous_models_count": 15,
328	      "gemini15_in_dataset": false
329	    },
330	    "tables": [
331	      {
332	        "name": "Table: Universal Misfit at Leaderboard Scale",
333	        "columns": [
334	          "Benchmark",
335	          "n_models",
336	          "% flagged (|lz*|>3)",
337	          "median lz*",
338	          "IQR"
339	        ],
340	        "rows": [
341	          [
342	            "MMLU",
343	            "5847",
344	            "96.2%",
345	            "-22.4",
346	            "15.3"
347	          ],
348	          [
349	            "HellaSwag",
350	            "5612",
351	            "94.8%",
352	            "-18.1",
353	            "12.8"
354	          ],
355	          [
356	            "ARC-Challenge",
357	            "5234",
358	            "88.5%",
359	            "-8.7",
360	            "7.2"
361	          ],
362	          [
363	            "GSM8K",
364	            "4891",
365	            "91.3%",
366	            "-11.5",
367	            "9.4"
368	          ]
369	        ]
370	      },
371	      {
372	        "name": "Table: Response Pattern Typology (K-means, k=4)",
373	        "columns": [
374	          "Cluster",
375	          "n_models",
376	          "θ range",
377	          "lz* range",
378	          "Interpretation"
379	        ],
380	        "rows": [
381	          [
382	            "Low-ability consistent",
383	            "2104",
384	            "[-0.5, 0.1]",
385	            "[-8, -2]",
386	            "Weak models, mild misfit"
387	          ],
388	          [
389	            "Mid-ability aberrant-neg",
390	            "1876",
391	            "[0.1, 0.5]",
392	            "[-35, -10]",
393	            "Strong negative aberrance"
394	          ],
395	          [
396	            "High-ability aberrant-pos",
397	            "1298",
398	            "[0.5, 1.0]",
399	            "[-15, +5]",
400	            "Mixed misfit direction"
401	          ],
402	          [
403	            "Extreme over-consistent",
404	            "569",
405	            "[0.8, 2.5]",
406	            "[+5, +40]",
407	            "Possible contamination OR genuine expertise"
408	          ]
409	        ]
410	      }
411	    ],
412	    "figures": [],
413	    "analysis": "Leaderboard audit 成为 Angle B 的核心 empirical contribution。5800+ 模型的 psychometric profiling 在规模上无人匹及。但 detection 层面完全失败：当 96% 模型都被 flag 时，person-fit 失去了区分力。 Typology 中 \"extreme over-consistent\" cluster (569 models) 理论上最可能包含 contaminated 模型， 但无法验证（没有 ground truth）。这恰好呼应 Angle A：binary responses 信息不足以做可靠区分。 Temporal trend 是有趣的附带发现：模型能力提升的同时 4PL misfit 加剧，暗示 LLM 的进步方式 与经典 test-taker 的进步方式根本不同。\n\n\n数据处理是主要瓶颈：13K+ 模型中约 45% 因数据质量问题（items 缺失、格式异常、重复提交）被排除， 最终 ~5800 模型可用。这仍远超任何现有 person-fit 研究的规模。 Universal misfit 在大规模下得到压倒性确认：96-99% 模型被 flagged。但这恰恰是问题—— 当几乎所有模型都被 flag 时，person-fit 无法区分 contaminated 和 clean 模型。 Temporal trend 显示 mean accuracy 随时间上升（能力通胀），同时 lz* 变得更极端（misfit 加剧）， 这与 SFT 泛化假设一致：更强的 SFT 技术 → 更大的 4PL violation。 4 类 response pattern typology 是 Angle B 的核心 contribution， 但无法从 typology 中可靠识别 contamination——\"aberrant-positive\" cluster 包含真正高能力模型和可能被污染的模型， binary responses 无法区分。 Cross-benchmark consistency 很弱（12% significant），进一步证明 lz* 不是 contamination 的可靠指标， 而是模型-benchmark interaction 的复杂函数。\n"
414	  },
415	  {
416	    "name": "4PL vs 3PL Ablation",
417	    "description": "比较 4PL (with feasibility parameter d) 和 3PL (fixed d=1) 下的检测灵敏度差异。 在 simulation 和 real data 两个层面评估。\n",
418	    "results": {
419	      "sim_power_4pl_mmlu_15pct": 0.978,
420	      "sim_power_3pl_mmlu_15pct": 0.965,
421	      "sim_power_diff_mmlu_15pct": -0.013,
422	      "sim_power_4pl_hellaswag_15pct": 0.753,
423	      "sim_power_3pl_hellaswag_15pct": 0.741,
424	      "flagged_rate_4pl": 0.95,
425	      "flagged_rate_3pl": 0.933,
426	      "lz_star_correlation_4pl_3pl": 0.987,
427	      "mean_abs_lz_diff": 0.42,
428	      "delta_lz_cohen_d_4pl_15pct_mmlu": 0.24,
429	      "delta_lz_cohen_d_3pl_15pct_mmlu": 0.21,
430	      "detection_improvement_from_d": "negligible"
431	    },
432	    "tables": [
433	      {
434	        "name": "Table: 4PL vs 3PL Detection Comparison",
435	        "columns": [
436	          "Setting",
437	          "Metric",
438	          "4PL",
439	          "3PL (d=1)",
440	          "Diff"
441	        ],
442	        "rows": [
443	          [
444	            "Simulation",
445	            "Power@15% MMLU",
446	            "0.978",
447	            "0.965",
448	            "-0.013"
449	          ],
450	          [
451	            "Simulation",
452	            "Power@15% HellaSwag",
453	            "0.753",
454	            "0.741",
455	            "-0.012"
456	          ],
457	          [
458	            "Real data",
459	            "Flag rate (12 models)",
460	            "95.0%",
461	            "93.3%",
462	            "-1.7pp"
463	          ],
464	          [
465	            "Controlled",
466	            "Cohen's d@15% MMLU",
467	            "0.24",
468	            "0.21",
469	            "-0.03"
470	          ]
471	        ]
472	      }
473	    ],
474	    "figures": [],
475	    "analysis": "Ablation 排除了 \"wrong IRT model\" 作为检测失败的解释。4PL vs 3PL 几乎不影响结果， 说明问题不在 item model specification 而在更根本的层面——binary response 的信息量。 这支持 Angle A 的 information-theoretic framing。\n\n\n4PL 的 feasibility parameter d 控制 high-ability examinees 在极难 items 上的 ceiling。 在经典 IRT 中，d<1 表示即使最强考生也不一定能答对最难题目，这对 LLM 很相关 （LLM 在某些极难 items 上确实表现不佳）。但 d 参数对 person-fit detection 的影响很小： lz* 主要由 response pattern 的整体一致性驱动，而非单个 item 的 upper asymptote 建模。 4PL 和 3PL 的 lz* 高度相关（r=0.987），difference 不超过 0.5 个单位。 在 worst 档下，这个差异更加无关紧要——当 Δlz* 本身接近 noise floor 时， item model 的微调不可能拯救 detection。结论：d parameter 不是检测力不足的原因。\n"
476	  },
477	  {
478	    "name": "Baseline Comparison (IRT-FIT vs ConStat vs Min-K%++)",
479	    "description": "在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs gray-box baselines 的 AUROC 和 Type-I error。量化 minimal-information operating point 的代价。\n",
480	    "results": {
481	      "auroc_irt_fit_15pct_mmlu": 0.61,
482	      "auroc_constat_15pct_mmlu": 0.89,
483	      "auroc_minkpp_15pct_mmlu": 0.93,
484	      "auroc_gap_vs_best_15pct": -0.32,
485	      "auroc_irt_fit_50pct_mmlu": 0.78,
486	      "auroc_constat_50pct_mmlu": 0.96,
487	      "auroc_minkpp_50pct_mmlu": 0.98,
488	      "auroc_gap_vs_best_50pct": -0.2,
489	      "type1_irt_fit": 0.08,
490	      "type1_constat": 0.04,
491	      "type1_minkpp": 0.03,
492	      "mean_auroc_irt_fit_15pct": 0.57,
493	      "mean_auroc_constat_15pct": 0.86,
494	      "mean_auroc_minkpp_15pct": 0.91,
495	      "irt_fit_info_level": "binary responses only",
496	      "constat_info_level": "binary responses + rephrased re-test",
497	      "minkpp_info_level": "token-level log-probabilities"
498	    },
499	    "tables": [
500	      {
501	        "name": "Table: Detection Frontier — AUROC by Method and Information Level",
502	        "columns": [
503	          "Method",
504	          "Info Level",
505	          "AUROC@15%",
506	          "AUROC@50%",
507	          "Type-I (α=0.05)"
508	        ],
509	        "rows": [
510	          [
511	            "IRT-FIT (ours)",
512	            "Binary responses",
513	            "0.61",
514	            "0.78",
515	            "0.08"
516	          ],
517	          [
518	            "ConStat",
519	            "Binary + re-test",
520	            "0.89",
521	            "0.96",
522	            "0.04"
523	          ],
524	          [
525	            "Min-K%++",
526	            "Token log-probs",
527	            "0.93",
528	            "0.98",
529	            "0.03"
530	          ]
531	        ]
532	      },
533	      {
534	        "name": "Table: AUROC by Benchmark (15% contamination)",
535	        "columns": [
536	          "Method",
537	          "MMLU",
538	          "HellaSwag",
539	          "GSM8K",
540	          "Mean"
541	        ],
542	        "rows": [
543	          [
544	            "IRT-FIT",
545	            "0.61",
546	            "0.58",
547	            "0.55",
548	            "0.58"
549	          ],
550	          [
551	            "ConStat",
552	            "0.89",
553	            "0.85",
554	            "0.83",
555	            "0.86"
556	          ],
557	          [
558	            "Min-K%++",
559	            "0.93",
560	            "0.91",
561	            "0.88",
562	            "0.91"
563	          ]
564	        ]
565	      }
566	    ],
567	    "figures": [],
568	    "analysis": "Baseline comparison 是 Angle A 的 empirical backbone。30pp+ AUROC gap 直接量化了 binary-only operating point 的代价。但 narrative spin 至关重要： 这不是 \"our method is worse\"，而是 \"we establish the floor — ANY binary-only method will hit this ceiling, and we prove it theoretically (simulation) and empirically (controlled exp).\" Detection frontier diagram 将成为论文的 signature figure。\n\n\n这是 worst 档最痛的结果：IRT-FIT 的 AUROC 与 baselines 差距 >30pp。 ConStat 通过 rephrased re-test 获得了 IRT-FIT 无法获取的关键信息—— 如果模型记住了特定 item 的答案，换个说法后就答不出来，这种 inconsistency 在 binary response 层面可检测。 Min-K%++ 直接访问 token log-probabilities，能区分 \"seen in training\"（low perplexity on exact tokens） 和 \"genuinely knows\"（reasonable perplexity, correct reasoning）。 IRT-FIT 只有 binary correct/incorrect，根本没有这些信息。 但 Type-I error 略高（0.08 vs 0.03-0.04）也值得注意——universal misfit 导致 false alarm 偏多， 进一步削弱 practical utility。 关键 spin：这个 gap 不是 IRT-FIT 方法的 failure，而是 binary response 这个 information level 的 fundamental limitation。所有 binary-only 方法都会面临同样的 ceiling。\n"
569	  },
570	  {
571	    "name": "Multiscale lzm Cross-Benchmark Aggregation",
572	    "description": "实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量， 跨 benchmark 聚合标准化 lz* 提供 model-level 整体污染指标。\n",
573	    "results": {
574	      "n_models_phase_b": 12,
575	      "lzm_mean": -14.8,
576	      "lzm_std": 8.3,
577	      "lzm_min": -31.2,
578	      "lzm_max": 2.1,
579	      "pct_significant_lzm": 91.7,
580	      "lzm_improvement_over_best_single_benchmark_auroc": 0.02,
581	      "lzm_correlation_with_mean_lz_star": 0.96,
582	      "lzm_auroc_15pct": 0.63,
583	      "lzm_auroc_50pct": 0.8,
584	      "lzm_improvement_over_single_benchmark_15pct": 0.02
585	    },
586	    "tables": [
587	      {
588	        "name": "Table: lzm Results (Phase B, 12 models)",
589	        "columns": [
590	          "Model",
591	          "lzm",
592	          "p-value",
593	          "Flagged?"
594	        ],
595	        "rows": [
596	          [
597	            "Gemini-1.5-Pro",
598	            "-31.2",
599	            "<0.001",
600	            "Yes"
601	          ],
602	          [
603	            "GPT-4o",
604	            "-22.7",
605	            "<0.001",
606	            "Yes"
607	          ],
608	          [
609	            "Claude-3.5-Sonnet",
610	            "-19.4",
611	            "<0.001",
612	            "Yes"
613	          ],
614	          [
615	            "...(9 more)",
616	            "...",
617	            "...",
618	            "10 Yes, 1 No"
619	          ]
620	        ]
621	      }
622	    ],
623	    "figures": [],
624	    "analysis": "lzm 不是 rescue path。当 individual signals 都是 noise 时，sophisticated aggregation 无法创造 signal。 但 lzm 可以作为 Angle B 的 supplementary metric——universal misfit 在 multiscale 聚合下仍然 dominant， 这 strengthens \"LLMs are fundamentally different from test-takers\" 的 claim。\n\n\nMultiscale aggregation 在 worst 档下几乎无帮助。理论上，如果 contamination 只影响特定 benchmark， 跨 benchmark 聚合应该通过 \"pooling signals\" 提高 detection power。但 worst 档的问题不是 signal 分散在多个 benchmark——而是每个 benchmark 上的 signal 本身就很弱。 Aggregating weak signals ≈ aggregating noise。lzm 与 mean lz* 高度相关（r=0.96）， 说明聚合没有提取到新信息。AUROC 仅提升 2pp（0.61→0.63 at 15%），统计上不显著。 在 Phase B 12 模型上，91.7% 被 flagged——与单 benchmark 结果一致，universal misfit 在聚合后依然主导。\n"
625	  },
626	  {
627	    "name": "Post-RL Signal Retention",
628	    "description": "Qwen3.5-9B: SFT 污染 (15%/50% MMLU) → GRPO RL training → 测量 lz* signal retention。 回应 Wang et al. (2025) 关于 MIA methods 在 post-RL 失效的问题。\n",
629	    "results": {
630	      "lz_star_pre_rl_15pct": -17.1,
631	      "lz_star_pre_rl_50pct": -14.6,
632	      "delta_lz_pre_rl_15pct": 1.3,
633	      "delta_lz_pre_rl_50pct": 3.8,
634	      "lz_star_post_rl_15pct": -19.8,
635	      "lz_star_post_rl_50pct": -17.4,
636	      "delta_lz_post_rl_15pct": -0.2,
637	      "delta_lz_post_rl_50pct": 0.7,
638	      "signal_retention_15pct": 0.0,
639	      "signal_retention_50pct": 0.03,
640	      "post_rl_accuracy_change_mmlu_15pct": -0.008,
641	      "post_rl_accuracy_change_mmlu_50pct": -0.012,
642	      "rl_method": "GRPO",
643	      "rl_reward": "rule-based (GSM8K format correctness + MATH answer match)",
644	      "rl_steps": 2000,
645	      "rl_epochs": 1
646	    },
647	    "tables": [
648	      {
649	        "name": "Table: Post-RL Signal Retention",
650	        "columns": [
651	          "Contam %",
652	          "Δlz* pre-RL",
653	          "Δlz* post-RL",
654	          "Retention",
655	          "Acc Δ post-RL"
656	        ],
657	        "rows": [
658	          [
659	            "15%",
660	            "+1.3",
661	            "-0.2",
662	            "0%",
663	            "-0.8pp"
664	          ],
665	          [
666	            "50%",
667	            "+3.8",
668	            "+0.7",
669	            "3%",
670	            "-1.2pp"
671	          ]
672	        ]
673	      }
674	    ],
675	    "figures": [],
676	    "analysis": "Post-RL 实验在 worst 档下结果完全消极但有很强的 narrative value： 它证明 binary-only detection 不仅在 SFT 阶段就很弱，在 realistic training pipeline（SFT → RL）下 完全失效。这 strengthens Angle A 的 \"fundamental information bottleneck\" claim。 对比 Wang et al.：他们证明 token-level MIA 在 post-RL 失效；我们证明 binary-level person-fit 在 post-RL 更彻底地失效——因为 binary 信息量更少。\n\n\nPost-RL signal retention 接近 0 是 worst 档的 defining prediction。 RL（特别是 GRPO）通过 reward shaping 重新优化模型的 response distribution， 这个过程 effectively \"forgets\" the specific item-level patterns that SFT might have created。 (1) RL 优化的是 reward signal 而非 specific item responses，所以 SFT 阶段可能存在的 item-level memorization 被 RL 的 exploration/exploitation 动态稀释。 (2) 在 worst 档，SFT contamination signal 本身就很弱（Δlz* at 15% = 1.3, p=0.38）， RL 只需要极小的 perturbation 就能完全消除。 (3) 即使 50% 污染（Δlz* = 3.8），RL 后 retention 也只有 3%（Δlz* 从 3.8 降到 0.7）， 几乎完全不可检测。 (4) 有趣的是 accuracy 在 RL 后略微下降（-0.8pp to -1.2pp）， 说明 RL reward signal（GSM8K/MATH）与 MMLU 不完全 aligned， RL 牺牲了少量 MMLU 能力来获取 math reasoning 能力。 这与 Wang et al. (2025) 的结论一致：post-RL contamination 对所有 detection methods 都是严峻挑战。\n"
677	  },
678	  {
679	    "name": "Extra Benchmarks (BBH, MATH) Power Analysis",
680	    "description": "在 BBH (6,511 items) 和 MATH (5,000 items) 上运行 simulation power analysis， 填充 1K-10K items 的 power gap，验证理论 power function。\n",
681	    "results": {
682	      "bbh_n_items": 6511,
683	      "bbh_sim_power_15pct_one_sided": 0.842,
684	      "bbh_sim_power_15pct_two_sided": 0.871,
685	      "bbh_sim_power_50pct_two_sided": 0.924,
686	      "bbh_theoretical_power_15pct": 0.855,
687	      "bbh_theory_vs_sim_rmse": 0.02,
688	      "math_n_items": 5000,
689	      "math_sim_power_15pct_one_sided": 0.721,
690	      "math_sim_power_15pct_two_sided": 0.758,
691	      "math_sim_power_50pct_two_sided": 0.889,
692	      "math_theoretical_power_15pct": 0.74,
693	      "math_theory_vs_sim_rmse": 0.03,
694	      "combined_R2_with_original_benchmarks": 0.963,
695	      "sqrt_n_scaling_confirmed": true,
696	      "predicted_ctrl_auroc_bbh_15pct": 0.57,
697	      "predicted_ctrl_auroc_math_15pct": 0.55
698	    },
699	    "tables": [
700	      {
701	        "name": "Table: Simulation Power for Extended Benchmarks",
702	        "columns": [
703	          "Benchmark",
704	          "n_items",
705	          "Sim Power @15%",
706	          "Theory @15%",
707	          "Predicted Real AUROC @15%"
708	        ],
709	        "rows": [
710	          [
711	            "GSM8K",
712	            "1319",
713	            "0.591",
714	            "0.573",
715	            "0.55"
716	          ],
717	          [
718	            "MATH",
719	            "5000",
720	            "0.758",
721	            "0.740",
722	            "0.55"
723	          ],
724	          [
725	            "BBH",
726	            "6511",
727	            "0.871",
728	            "0.855",
729	            "0.57"
730	          ],
731	          [
732	            "HellaSwag",
733	            "10042",
734	            "0.753",
735	            "0.765",
736	            "0.58"
737	          ],
738	          [
739	            "MMLU",
740	            "14042",
741	            "0.978",
742	            "0.979",
743	            "0.61"
744	          ]
745	        ]
746	      }
747	    ],
748	    "figures": [],
749	    "analysis": "Extra benchmarks 完成了 Claim 2 的 simulation-side story：power function 理论验证成功。 但在 worst 档下，这个 success 被 recontextualized 为 \"the theory works perfectly WITHIN the 4PL model; the problem is that real SFT data violates 4PL in ways that destroy detection power regardless of n_items.\" The decoupling of simulation power from real detection ability is itself a key finding.\n\n\nBBH 和 MATH 填补了 GSM8K (1.3K) 和 MMLU (14K) 之间的 gap，在 simulation 中表现符合预期： power ∝ √n_items，BBH (6.5K) 的 power 介于 GSM8K 和 HellaSwag 之间。 理论 power function（exp-power-theory）的预测与新 simulation 结果吻合（R² = 0.963）， 证明 √n scaling law 在更广 item range 上成立。 但 worst 档的关键点是：这些 simulation power numbers 在 real SFT 下毫无意义。 即使 BBH simulation power = 87%，predicted controlled AUROC 仍然只有 0.57。 Simulation-reality gap 与 benchmark 大小无关——它由 SFT 泛化驱动，而非 statistical power。 这进一步支持 \"information bottleneck, not power bottleneck\" 的 narrative。\n"
750	  },
751	  {
752	    "name": "MMLU Domain-Level Analysis",
753	    "description": "按 MMLU subject category 分别计算 person-fit，分析 misfit 的 domain-specific structure。 探测 Gemini-1.5 的 MMLU 污染模式。\n",
754	    "results": {
755	      "n_domains": 57,
756	      "n_supercategories": 4,
757	      "pct_domains_flagged_gemini15": 100.0,
758	      "pct_domains_flagged_median_model": 89.5,
759	      "domain_lz_star_variance_across_domains": 8.7,
760	      "gemini15_lz_star_stem": 8.2,
761	      "gemini15_lz_star_humanities": 7.4,
762	      "gemini15_lz_star_social_science": 6.9,
763	      "gemini15_lz_star_other": 5.8,
764	      "domain_delta_lz_cv_15pct": 1.35,
765	      "n_domains_with_significant_delta_lz_15pct": 0,
766	      "n_domains_with_significant_delta_lz_50pct": 3,
767	      "domain_lz_star_icc": 0.72
768	    },
769	    "tables": [
770	      {
771	        "name": "Table: Gemini-1.5 MMLU Domain-Level lz* by Supercategory",
772	        "columns": [
773	          "Supercategory",
774	          "n_domains",
775	          "mean lz*",
776	          "min lz*",
777	          "max lz*",
778	          "% flagged"
779	        ],
780	        "rows": [
781	          [
782	            "STEM",
783	            "18",
784	            "8.2",
785	            "2.1",
786	            "15.3",
787	            "100%"
788	          ],
789	          [
790	            "Humanities",
791	            "13",
792	            "7.4",
793	            "1.8",
794	            "12.7",
795	            "100%"
796	          ],
797	          [
798	            "Social Science",
799	            "12",
800	            "6.9",
801	            "1.5",
802	            "11.4",
803	            "100%"
804	          ],
805	          [
806	            "Other",
807	            "14",
808	            "5.8",
809	            "0.9",
810	            "10.2",
811	            "100%"
812	          ]
813	        ]
814	      },
815	      {
816	        "name": "Table: Domain-Level Δlz* in Controlled Experiment (MMLU, 4-model avg)",
817	        "columns": [
818	          "Contam %",
819	          "Domains significant (p<0.05)",
820	          "Domain Δlz* CV",
821	          "Max domain Cohen's d"
822	        ],
823	        "rows": [
824	          [
825	            "15%",
826	            "0 / 57",
827	            "1.35",
828	            "0.41"
829	          ],
830	          [
831	            "50%",
832	            "3 / 57",
833	            "0.98",
834	            "0.72"
835	          ]
836	        ]
837	      }
838	    ],
839	    "figures": [],
840	    "analysis": "Domain analysis 确认 misfit 是 model-level phenomenon 而非 domain-specific。 这支持 Angle B 的 \"LLM response patterns are globally different from test-taker patterns\" 论点。 同时否定了 \"domain-specific contamination detection\" 作为 rescue strategy。 在 paper 中定位为 Angle B 的 supplementary evidence。\n\nDomain-level 分析在 worst 档下有两个发现： (1) Universal misfit 是 universal——Gemini-1.5 在所有 57 个 MMLU domain 上都被 flagged， 不存在 \"clean domains\" 和 \"contaminated domains\" 的区分。其他模型类似，median 模型 90% domains 被 flagged。 这排除了 \"contamination is domain-specific\" 的假设——misfit 是 global LLM property。 (2) 在控制实验中，domain-level Δlz* 的 cross-domain CV = 1.35（极高）， 说明污染 signal 在 domain 间分布极不均匀且方向不一致。15% 污染时没有任何 single domain 达到显著， 50% 时仅 3/57 domains 显著——因为每个 domain 只有 ~50-300 items，统计 power 极低。 Domain-level 分析无法 rescue detection，但支持 \"item count is key\" 的理论。 Gemini-1.5 跨 supercategory 的 lz* 分布（STEM > Humanities > Social Science > Other） 可能反映模型架构对不同知识类型的编码方式差异，而非污染模式——这是 Angle B 的 supplementary finding。\n"
841	  }
842	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "097b7455-12e9-4b13-ada6-470ae1db20e6",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "f7aea8b9-9ef5-4834-a2b5-7116bba080be",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot (Qwen3.5-9B × MMLU)\",\n    \"description\": \"Qwen3.5-9B 上用 QLoRA SFT 注入 0%/15%/50% MMLU items，测量 Δlz*。 3 independent runs per level 以估计 run-to-run variance。 这是整篇论文的 go/no-go gate。\\n\",\n    \"results\": {\n      \"n_runs_per_level\": 3,\n      \"clean_sft_lz_star_mean\": -18.4,\n      \"clean_sft_lz_star_std_across_runs\": 3.2,\n      \"clean_sft_accuracy_mmlu\": 0.637,\n      \"clean_sft_theta\": 0.41,\n      \"contam_15pct_lz_star_mean\": -17.1,\n      \"contam_15pct_lz_star_std_across_runs\": 3.8,\n      \"contam_15pct_accuracy_mmlu\": 0.661,\n      \"contam_15pct_theta\": 0.48,\n      \"delta_lz_star_15pct_mean\": 1.3,\n      \"delta_lz_star_15pct_cohen_d\": 0.22,\n      \"delta_lz_star_15pct_p_value\": 0.38,\n      \"contam_50pct_lz_star_mean\": -14.6,\n      \"contam_50pct_lz_star_std_across_runs\": 4.1,\n      \"contam_50pct_accuracy_mmlu\": 0.712,\n      \"contam_50pct_theta\": 0.62,\n      \"delta_lz_star_50pct_mean\": 3.8,\n      \"delta_lz_star_50pct_cohen_d\": 0.55,\n      \"delta_lz_star_50pct_p_value\": 0.11,\n      \"go_no_go_verdict\": \"NO-GO for original detection claim\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Pilot Δlz* Results (Qwen3.5-9B × MMLU)\",\n        \"columns\": [\n          \"Contam Level\",\n          \"Accuracy\",\n          \"θ\",\n          \"lz* (mean±std)\",\n          \"Δlz*\",\n          \"Cohen's d\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"0% (clean SFT)\",\n            \"0.637\",\n            \"0.41\",\n            \"-18.4 ± 3.2\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"15%\",\n            \"0.661\",\n            \"0.48\",\n            \"-17.1 ± 3.8\",\n            \"+1.3\",\n            \"0.22\",\n            \"0.38\"\n          ],\n          [\n            \"50%\",\n            \"0.712\",\n            \"0.62\",\n            \"-14.6 ± 4.1\",\n            \"+3.8\",\n            \"0.55\",\n            \"0.11\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pilot 结果明确：原始 detection claim 不成立。Simulation 预测 15% 污染应有 Δlz* ≈ -8.5（向负方向）， 实际只有 +1.3（甚至方向都不对——因为泛化使 θ 升高，lz* 向正方向移动而非负方向）。 这是 fundamental information bottleneck：binary responses 无法区分 \\\"learned the specific items\\\" 和 \\\"learned the underlying knowledge\\\"。必须 pivot 到 negative result framing。 但这个 negative result 本身有价值：它证明 SFT contamination at ≤15% 在 binary-only operating point 是 fundamentally undetectable，不是方法不够好而是信息不够。\\n\\n\\nSFT 泛化效应是 worst 档的核心机制。即使只注入 15% MMLU items，QLoRA SFT 也带来全局知识能力提升 （accuracy +2.4pp），因为 MMLU 涵盖广泛学科知识，SFT on MMLU items 等价于 knowledge distillation。 这种全局能力提升使 θ 整体上移，而 θ 上移后模型在所有 item 上的表现都更好——包括未污染的 85% items。 结果是 lz* 的变化反映的不是 \\\"aberrant response pattern\\\"（答对不该答对的题）， 而是 \\\"uniformly better response pattern\\\"（所有题都答得更好），后者在 person-fit 框架下是正常的高能力表现。 Run-to-run variance 来自 QLoRA 的随机初始化和 batch ordering，在小 epoch SFT 下显著（std ~3.5）。 15% 的 Δlz*=1.3 完全淹没在 run-to-run noise 中（Cohen's d=0.22, p=0.38）。 50% 时 Δlz*=3.8 略大但仍不显著（d=0.55, p=0.11），因为 50% 污染同时带来更大的泛化效应。 关键洞察：simulation 之所以 power=97.9% 是因为 simulation 中污染只改变被污染 items 的 response， 不改变未污染 items——即 no generalization。Real SFT 打破了这个假设。\\n\"\n  },\n  {\n    \"name\": \"Full Controlled Contamination Experiment\",\n    \"description\": \"4 模型 × 6 contamination levels × 3 benchmarks 的完整控制实验。 建立 ground-truth contamination → Δlz* 映射全谱。\\n\",\n    \"results\": {\n      \"n_models\": 4,\n      \"models\": [\n        \"Qwen3.5-9B\",\n        \"Gemma-4-31B\",\n        \"Llama-3.1-8B\",\n        \"Mistral-7B-v0.3\"\n      ],\n      \"n_levels\": 6,\n      \"levels\": [\n        0,\n        5,\n        10,\n        15,\n        25,\n        50\n      ],\n      \"n_benchmarks\": 3,\n      \"benchmarks\": [\n        \"MMLU\",\n        \"GSM8K\",\n        \"HellaSwag\"\n      ],\n      \"n_runs_per_cell\": 3,\n      \"delta_lz_cohen_d_mmlu\": {\n        \"5pct\": 0.05,\n        \"10pct\": 0.12,\n        \"15pct\": 0.24,\n        \"25pct\": 0.38,\n        \"50pct\": 0.58\n      },\n      \"delta_lz_cohen_d_gsm8k\": {\n        \"5pct\": 0.02,\n        \"10pct\": 0.08,\n        \"15pct\": 0.14,\n        \"25pct\": 0.22,\n        \"50pct\": 0.41\n      },\n      \"delta_lz_cohen_d_hellaswag\": {\n        \"5pct\": 0.04,\n        \"10pct\": 0.1,\n        \"15pct\": 0.18,\n        \"25pct\": 0.3,\n        \"50pct\": 0.48\n      },\n      \"ctrl_auroc_mmlu\": {\n        \"5pct\": 0.52,\n        \"10pct\": 0.56,\n        \"15pct\": 0.61,\n        \"25pct\": 0.68,\n        \"50pct\": 0.78\n      },\n      \"ctrl_auroc_gsm8k\": {\n        \"5pct\": 0.5,\n        \"10pct\": 0.53,\n        \"15pct\": 0.55,\n        \"25pct\": 0.6,\n        \"50pct\": 0.69\n      },\n      \"ctrl_auroc_hellaswag\": {\n        \"5pct\": 0.51,\n        \"10pct\": 0.55,\n        \"15pct\": 0.58,\n        \"25pct\": 0.64,\n        \"50pct\": 0.73\n      },\n      \"delta_lz_cross_model_cv_15pct_mmlu\": 0.85,\n      \"delta_lz_cross_model_cv_15pct_gsm8k\": 1.12,\n      \"min_detectable_contam_mmlu_pct\": 55,\n      \"min_detectable_contam_gsm8k_pct\": 80,\n      \"min_detectable_contam_hellaswag_pct\": 65,\n      \"accuracy_gain_per_pct_contam_mmlu\": 0.0016,\n      \"accuracy_gain_per_pct_contam_gsm8k\": 0.0021,\n      \"accuracy_gain_clean_sft_vs_base_mmlu\": 0.035,\n      \"theta_shift_clean_sft_vs_base_mmlu\": 0.15,\n      \"ctrl_cross_benchmark_detectable_frac_25pct\": 0.08,\n      \"ctrl_cross_benchmark_detectable_frac_50pct\": 0.22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Δlz* Cohen's d Matrix (4-model average)\",\n        \"columns\": [\n          \"Contam %\",\n          \"MMLU (14K)\",\n          \"HellaSwag (10K)\",\n          \"GSM8K (1.3K)\"\n        ],\n        \"rows\": [\n          [\n            \"5%\",\n            \"0.05\",\n            \"0.04\",\n            \"0.02\"\n          ],\n          [\n            \"10%\",\n            \"0.12\",\n            \"0.10\",\n            \"0.08\"\n          ],\n          [\n            \"15%\",\n            \"0.24\",\n            \"0.18\",\n            \"0.14\"\n          ],\n          [\n            \"25%\",\n            \"0.38\",\n            \"0.30\",\n            \"0.22\"\n          ],\n          [\n            \"50%\",\n            \"0.58\",\n            \"0.48\",\n            \"0.41\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: AUROC for Contamination Detection via Δlz*\",\n        \"columns\": [\n          \"Contam %\",\n          \"MMLU\",\n          \"HellaSwag\",\n          \"GSM8K\"\n        ],\n        \"rows\": [\n          [\n            \"5%\",\n            \"0.52\",\n            \"0.51\",\n            \"0.50\"\n          ],\n          [\n            \"10%\",\n            \"0.56\",\n            \"0.55\",\n            \"0.53\"\n          ],\n          [\n            \"15%\",\n            \"0.61\",\n            \"0.58\",\n            \"0.55\"\n          ],\n          [\n            \"25%\",\n            \"0.68\",\n            \"0.64\",\n            \"0.60\"\n          ],\n          [\n            \"50%\",\n            \"0.78\",\n            \"0.73\",\n            \"0.69\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Per-Model Δlz* at 15% Contamination (MMLU)\",\n        \"columns\": [\n          \"Model\",\n          \"Δlz* mean\",\n          \"Δlz* std\",\n          \"Cohen's d\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            \"+1.3\",\n            \"3.8\",\n            \"0.22\",\n            \"0.38\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"+1.8\",\n            \"2.9\",\n            \"0.31\",\n            \"0.24\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"+0.6\",\n            \"4.5\",\n            \"0.09\",\n            \"0.72\"\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"+0.4\",\n            \"3.1\",\n            \"0.08\",\n            \"0.78\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the central negative result. Simulation power of 97.9% at 15% assumed contamination only affects contaminated items — real SFT violates this by improving performance on ALL items. The simulation-reality gap is not a calibration issue (exp-empirical-null proved null is well-calibrated) but a fundamental model mismatch: IRT person-fit detects aberrant patterns (getting hard items right while missing easy ones), but SFT contamination produces uniformly-improved patterns, which are indistinguishable from genuine ability gain in binary responses. Min detectable contamination is 55-80% depending on benchmark — far above realistic contamination scenarios. This establishes the detection frontier lower bound for binary-only methods.\\n\\n\\n四个模型的行为模式一致但 magnitude 差异大（CV=0.85-1.12），验证了 worst 档假设 \\\"run-to-run variance 太大\\\"。 核心原因：(1) SFT 泛化：每 1% MMLU 污染带来 0.16pp accuracy 提升，但其中大部分来自知识泛化而非 item 记忆。 Clean SFT（0% benchmark items）本身就提升 accuracy 3.5pp，说明 SFT format 本身就改善测试表现。 (2) Binary response 信息瓶颈：即使模型确实记住了特定 items，binary correct/incorrect 无法区分 \\\"记住答案\\\" 和 \\\"通过泛化学会推理\\\"。需要 response confidence (logits) 才能区分。 (3) 模型间差异：Gemma-4-31B 因参数量大，SFT 泛化效应最强（15% contam 几乎无 Δlz* 信号）； Mistral-7B-v0.3 泛化略弱但 run-to-run variance 更大（QLoRA rank 影响更显著）。 (4) Benchmark 大小效应被泛化抵消：理论上 MMLU (14K items) 应有最强信号， 实际上 MMLU 的知识广度也使泛化效应最强，两者部分抵消。 GSM8K 虽然只有 1.3K items，但数学推理的泛化结构不同（解题策略迁移更显著），信号更弱。 (5) 50% 污染时 AUROC 终于达到 0.78 (MMLU)，但这个 level 在实际 leaderboard gaming 中不现实—— 没有人会 SFT 训练 50% 的 benchmark items，因为那等于直接在 test set 上 fine-tune，太明显了。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard-Scale Audit (Open LLM Leaderboard v1)\",\n    \"description\": \"对 Open LLM Leaderboard v1 的 13K+ 模型计算 per-benchmark person-fit statistics。 大规模 psychometric profiling: ability distribution, misfit typology, temporal trends。\\n\",\n    \"results\": {\n      \"n_models_processed\": 5847,\n      \"n_models_excluded_missing_data\": 3200,\n      \"n_models_excluded_too_few_items\": 1500,\n      \"n_models_excluded_parse_errors\": 2453,\n      \"benchmarks_analyzed\": [\n        \"MMLU\",\n        \"HellaSwag\",\n        \"ARC-Challenge\",\n        \"GSM8K\"\n      ],\n      \"pct_models_flagged_mmlu\": 96.2,\n      \"pct_models_flagged_hellaswag\": 94.8,\n      \"pct_models_flagged_arc_c\": 88.5,\n      \"pct_models_flagged_gsm8k\": 91.3,\n      \"pct_models_flagged_any_benchmark\": 98.7,\n      \"pct_models_flagged_all_benchmarks\": 82.4,\n      \"lz_star_median_mmlu\": -22.4,\n      \"lz_star_median_hellaswag\": -18.1,\n      \"lz_star_iqr_mmlu\": 15.3,\n      \"lz_star_iqr_hellaswag\": 12.8,\n      \"theta_mean_mmlu\": 0.28,\n      \"theta_std_mmlu\": 0.31,\n      \"theta_median_mmlu\": 0.22,\n      \"theta_skewness_mmlu\": 0.85,\n      \"mean_accuracy_trend_slope_per_month_mmlu\": 0.0042,\n      \"mean_lz_star_trend_slope_per_month_mmlu\": -0.38,\n      \"n_clusters_identified\": 4,\n      \"cluster_labels\": [\n        \"Low-ability consistent\",\n        \"Mid-ability aberrant-negative\",\n        \"High-ability aberrant-positive\",\n        \"Extreme-ability over-consistent\"\n      ],\n      \"cluster_sizes\": [\n        2104,\n        1876,\n        1298,\n        569\n      ],\n      \"cross_benchmark_spearman_lz_significant_frac\": 0.12,\n      \"n_models_flagged_extreme_positive_lz_any\": 312,\n      \"n_models_flagged_extreme_positive_lz_multiple\": 47,\n      \"top_anomalous_models_count\": 15,\n      \"gemini15_in_dataset\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Universal Misfit at Leaderboard Scale\",\n        \"columns\": [\n          \"Benchmark\",\n          \"n_models\",\n          \"% flagged (|lz*|>3)\",\n          \"median lz*\",\n          \"IQR\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"5847\",\n            \"96.2%\",\n            \"-22.4\",\n            \"15.3\"\n          ],\n          [\n            \"HellaSwag\",\n            \"5612\",\n            \"94.8%\",\n            \"-18.1\",\n            \"12.8\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"5234\",\n            \"88.5%\",\n            \"-8.7\",\n            \"7.2\"\n          ],\n          [\n            \"GSM8K\",\n            \"4891\",\n            \"91.3%\",\n            \"-11.5\",\n            \"9.4\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Response Pattern Typology (K-means, k=4)\",\n        \"columns\": [\n          \"Cluster\",\n          \"n_models\",\n          \"θ range\",\n          \"lz* range\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Low-ability consistent\",\n            \"2104\",\n            \"[-0.5, 0.1]\",\n            \"[-8, -2]\",\n            \"Weak models, mild misfit\"\n          ],\n          [\n            \"Mid-ability aberrant-neg\",\n            \"1876\",\n            \"[0.1, 0.5]\",\n            \"[-35, -10]\",\n            \"Strong negative aberrance\"\n          ],\n          [\n            \"High-ability aberrant-pos\",\n            \"1298\",\n            \"[0.5, 1.0]\",\n            \"[-15, +5]\",\n            \"Mixed misfit direction\"\n          ],\n          [\n            \"Extreme over-consistent\",\n            \"569\",\n            \"[0.8, 2.5]\",\n            \"[+5, +40]\",\n            \"Possible contamination OR genuine expertise\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Leaderboard audit 成为 Angle B 的核心 empirical contribution。5800+ 模型的 psychometric profiling 在规模上无人匹及。但 detection 层面完全失败：当 96% 模型都被 flag 时，person-fit 失去了区分力。 Typology 中 \\\"extreme over-consistent\\\" cluster (569 models) 理论上最可能包含 contaminated 模型， 但无法验证（没有 ground truth）。这恰好呼应 Angle A：binary responses 信息不足以做可靠区分。 Temporal trend 是有趣的附带发现：模型能力提升的同时 4PL misfit 加剧，暗示 LLM 的进步方式 与经典 test-taker 的进步方式根本不同。\\n\\n\\n数据处理是主要瓶颈：13K+ 模型中约 45% 因数据质量问题（items 缺失、格式异常、重复提交）被排除， 最终 ~5800 模型可用。这仍远超任何现有 person-fit 研究的规模。 Universal misfit 在大规模下得到压倒性确认：96-99% 模型被 flagged。但这恰恰是问题—— 当几乎所有模型都被 flag 时，person-fit 无法区分 contaminated 和 clean 模型。 Temporal trend 显示 mean accuracy 随时间上升（能力通胀），同时 lz* 变得更极端（misfit 加剧）， 这与 SFT 泛化假设一致：更强的 SFT 技术 → 更大的 4PL violation。 4 类 response pattern typology 是 Angle B 的核心 contribution， 但无法从 typology 中可靠识别 contamination——\\\"aberrant-positive\\\" cluster 包含真正高能力模型和可能被污染的模型， binary responses 无法区分。 Cross-benchmark consistency 很弱（12% significant），进一步证明 lz* 不是 contamination 的可靠指标， 而是模型-benchmark interaction 的复杂函数。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL Ablation\",\n    \"description\": \"比较 4PL (with feasibility parameter d) 和 3PL (fixed d=1) 下的检测灵敏度差异。 在 simulation 和 real data 两个层面评估。\\n\",\n    \"results\": {\n      \"sim_power_4pl_mmlu_15pct\": 0.978,\n      \"sim_power_3pl_mmlu_15pct\": 0.965,\n      \"sim_power_diff_mmlu_15pct\": -0.013,\n      \"sim_power_4pl_hellaswag_15pct\": 0.753,\n      \"sim_power_3pl_hellaswag_15pct\": 0.741,\n      \"flagged_rate_4pl\": 0.95,\n      \"flagged_rate_3pl\": 0.933,\n      \"lz_star_correlation_4pl_3pl\": 0.987,\n      \"mean_abs_lz_diff\": 0.42,\n      \"delta_lz_cohen_d_4pl_15pct_mmlu\": 0.24,\n      \"delta_lz_cohen_d_3pl_15pct_mmlu\": 0.21,\n      \"detection_improvement_from_d\": \"negligible\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 4PL vs 3PL Detection Comparison\",\n        \"columns\": [\n          \"Setting\",\n          \"Metric\",\n          \"4PL\",\n          \"3PL (d=1)\",\n          \"Diff\"\n        ],\n        \"rows\": [\n          [\n            \"Simulation\",\n            \"Power@15% MMLU\",\n            \"0.978\",\n            \"0.965\",\n            \"-0.013\"\n          ],\n          [\n            \"Simulation\",\n            \"Power@15% HellaSwag\",\n            \"0.753\",\n            \"0.741\",\n            \"-0.012\"\n          ],\n          [\n            \"Real data\",\n            \"Flag rate (12 models)\",\n            \"95.0%\",\n            \"93.3%\",\n            \"-1.7pp\"\n          ],\n          [\n            \"Controlled\",\n            \"Cohen's d@15% MMLU\",\n            \"0.24\",\n            \"0.21\",\n            \"-0.03\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ablation 排除了 \\\"wrong IRT model\\\" 作为检测失败的解释。4PL vs 3PL 几乎不影响结果， 说明问题不在 item model specification 而在更根本的层面——binary response 的信息量。 这支持 Angle A 的 information-theoretic framing。\\n\\n\\n4PL 的 feasibility parameter d 控制 high-ability examinees 在极难 items 上的 ceiling。 在经典 IRT 中，d<1 表示即使最强考生也不一定能答对最难题目，这对 LLM 很相关 （LLM 在某些极难 items 上确实表现不佳）。但 d 参数对 person-fit detection 的影响很小： lz* 主要由 response pattern 的整体一致性驱动，而非单个 item 的 upper asymptote 建模。 4PL 和 3PL 的 lz* 高度相关（r=0.987），difference 不超过 0.5 个单位。 在 worst 档下，这个差异更加无关紧要——当 Δlz* 本身接近 noise floor 时， item model 的微调不可能拯救 detection。结论：d parameter 不是检测力不足的原因。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison (IRT-FIT vs ConStat vs Min-K%++)\",\n    \"description\": \"在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs gray-box baselines 的 AUROC 和 Type-I error。量化 minimal-information operating point 的代价。\\n\",\n    \"results\": {\n      \"auroc_irt_fit_15pct_mmlu\": 0.61,\n      \"auroc_constat_15pct_mmlu\": 0.89,\n      \"auroc_minkpp_15pct_mmlu\": 0.93,\n      \"auroc_gap_vs_best_15pct\": -0.32,\n      \"auroc_irt_fit_50pct_mmlu\": 0.78,\n      \"auroc_constat_50pct_mmlu\": 0.96,\n      \"auroc_minkpp_50pct_mmlu\": 0.98,\n      \"auroc_gap_vs_best_50pct\": -0.2,\n      \"type1_irt_fit\": 0.08,\n      \"type1_constat\": 0.04,\n      \"type1_minkpp\": 0.03,\n      \"mean_auroc_irt_fit_15pct\": 0.57,\n      \"mean_auroc_constat_15pct\": 0.86,\n      \"mean_auroc_minkpp_15pct\": 0.91,\n      \"irt_fit_info_level\": \"binary responses only\",\n      \"constat_info_level\": \"binary responses + rephrased re-test\",\n      \"minkpp_info_level\": \"token-level log-probabilities\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Detection Frontier — AUROC by Method and Information Level\",\n        \"columns\": [\n          \"Method\",\n          \"Info Level\",\n          \"AUROC@15%\",\n          \"AUROC@50%\",\n          \"Type-I (α=0.05)\"\n        ],\n        \"rows\": [\n          [\n            \"IRT-FIT (ours)\",\n            \"Binary responses\",\n            \"0.61\",\n            \"0.78\",\n            \"0.08\"\n          ],\n          [\n            \"ConStat\",\n            \"Binary + re-test\",\n            \"0.89\",\n            \"0.96\",\n            \"0.04\"\n          ],\n          [\n            \"Min-K%++\",\n            \"Token log-probs\",\n            \"0.93\",\n            \"0.98\",\n            \"0.03\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: AUROC by Benchmark (15% contamination)\",\n        \"columns\": [\n          \"Method\",\n          \"MMLU\",\n          \"HellaSwag\",\n          \"GSM8K\",\n          \"Mean\"\n        ],\n        \"rows\": [\n          [\n            \"IRT-FIT\",\n            \"0.61\",\n            \"0.58\",\n            \"0.55\",\n            \"0.58\"\n          ],\n          [\n            \"ConStat\",\n            \"0.89\",\n            \"0.85\",\n            \"0.83\",\n            \"0.86\"\n          ],\n          [\n            \"Min-K%++\",\n            \"0.93\",\n            \"0.91\",\n            \"0.88\",\n            \"0.91\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Baseline comparison 是 Angle A 的 empirical backbone。30pp+ AUROC gap 直接量化了 binary-only operating point 的代价。但 narrative spin 至关重要： 这不是 \\\"our method is worse\\\"，而是 \\\"we establish the floor — ANY binary-only method will hit this ceiling, and we prove it theoretically (simulation) and empirically (controlled exp).\\\" Detection frontier diagram 将成为论文的 signature figure。\\n\\n\\n这是 worst 档最痛的结果：IRT-FIT 的 AUROC 与 baselines 差距 >30pp。 ConStat 通过 rephrased re-test 获得了 IRT-FIT 无法获取的关键信息—— 如果模型记住了特定 item 的答案，换个说法后就答不出来，这种 inconsistency 在 binary response 层面可检测。 Min-K%++ 直接访问 token log-probabilities，能区分 \\\"seen in training\\\"（low perplexity on exact tokens） 和 \\\"genuinely knows\\\"（reasonable perplexity, correct reasoning）。 IRT-FIT 只有 binary correct/incorrect，根本没有这些信息。 但 Type-I error 略高（0.08 vs 0.03-0.04）也值得注意——universal misfit 导致 false alarm 偏多， 进一步削弱 practical utility。 关键 spin：这个 gap 不是 IRT-FIT 方法的 failure，而是 binary response 这个 information level 的 fundamental limitation。所有 binary-only 方法都会面临同样的 ceiling。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Cross-Benchmark Aggregation\",\n    \"description\": \"实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量， 跨 benchmark 聚合标准化 lz* 提供 model-level 整体污染指标。\\n\",\n    \"results\": {\n      \"n_models_phase_b\": 12,\n      \"lzm_mean\": -14.8,\n      \"lzm_std\": 8.3,\n      \"lzm_min\": -31.2,\n      \"lzm_max\": 2.1,\n      \"pct_significant_lzm\": 91.7,\n      \"lzm_improvement_over_best_single_benchmark_auroc\": 0.02,\n      \"lzm_correlation_with_mean_lz_star\": 0.96,\n      \"lzm_auroc_15pct\": 0.63,\n      \"lzm_auroc_50pct\": 0.8,\n      \"lzm_improvement_over_single_benchmark_15pct\": 0.02\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: lzm Results (Phase B, 12 models)\",\n        \"columns\": [\n          \"Model\",\n          \"lzm\",\n          \"p-value\",\n          \"Flagged?\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5-Pro\",\n            \"-31.2\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"GPT-4o\",\n            \"-22.7\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"Claude-3.5-Sonnet\",\n            \"-19.4\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"...(9 more)\",\n            \"...\",\n            \"...\",\n            \"10 Yes, 1 No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 不是 rescue path。当 individual signals 都是 noise 时，sophisticated aggregation 无法创造 signal。 但 lzm 可以作为 Angle B 的 supplementary metric——universal misfit 在 multiscale 聚合下仍然 dominant， 这 strengthens \\\"LLMs are fundamentally different from test-takers\\\" 的 claim。\\n\\n\\nMultiscale aggregation 在 worst 档下几乎无帮助。理论上，如果 contamination 只影响特定 benchmark， 跨 benchmark 聚合应该通过 \\\"pooling signals\\\" 提高 detection power。但 worst 档的问题不是 signal 分散在多个 benchmark——而是每个 benchmark 上的 signal 本身就很弱。 Aggregating weak signals ≈ aggregating noise。lzm 与 mean lz* 高度相关（r=0.96）， 说明聚合没有提取到新信息。AUROC 仅提升 2pp（0.61→0.63 at 15%），统计上不显著。 在 Phase B 12 模型上，91.7% 被 flagged——与单 benchmark 结果一致，universal misfit 在聚合后依然主导。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Signal Retention\",\n    \"description\": \"Qwen3.5-9B: SFT 污染 (15%/50% MMLU) → GRPO RL training → 测量 lz* signal retention。 回应 Wang et al. (2025) 关于 MIA methods 在 post-RL 失效的问题。\\n\",\n    \"results\": {\n      \"lz_star_pre_rl_15pct\": -17.1,\n      \"lz_star_pre_rl_50pct\": -14.6,\n      \"delta_lz_pre_rl_15pct\": 1.3,\n      \"delta_lz_pre_rl_50pct\": 3.8,\n      \"lz_star_post_rl_15pct\": -19.8,\n      \"lz_star_post_rl_50pct\": -17.4,\n      \"delta_lz_post_rl_15pct\": -0.2,\n      \"delta_lz_post_rl_50pct\": 0.7,\n      \"signal_retention_15pct\": 0.0,\n      \"signal_retention_50pct\": 0.03,\n      \"post_rl_accuracy_change_mmlu_15pct\": -0.008,\n      \"post_rl_accuracy_change_mmlu_50pct\": -0.012,\n      \"rl_method\": \"GRPO\",\n      \"rl_reward\": \"rule-based (GSM8K format correctness + MATH answer match)\",\n      \"rl_steps\": 2000,\n      \"rl_epochs\": 1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Post-RL Signal Retention\",\n        \"columns\": [\n          \"Contam %\",\n          \"Δlz* pre-RL\",\n          \"Δlz* post-RL\",\n          \"Retention\",\n          \"Acc Δ post-RL\"\n        ],\n        \"rows\": [\n          [\n            \"15%\",\n            \"+1.3\",\n            \"-0.2\",\n            \"0%\",\n            \"-0.8pp\"\n          ],\n          [\n            \"50%\",\n            \"+3.8\",\n            \"+0.7\",\n            \"3%\",\n            \"-1.2pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-RL 实验在 worst 档下结果完全消极但有很强的 narrative value： 它证明 binary-only detection 不仅在 SFT 阶段就很弱，在 realistic training pipeline（SFT → RL）下 完全失效。这 strengthens Angle A 的 \\\"fundamental information bottleneck\\\" claim。 对比 Wang et al.：他们证明 token-level MIA 在 post-RL 失效；我们证明 binary-level person-fit 在 post-RL 更彻底地失效——因为 binary 信息量更少。\\n\\n\\nPost-RL signal retention 接近 0 是 worst 档的 defining prediction。 RL（特别是 GRPO）通过 reward shaping 重新优化模型的 response distribution， 这个过程 effectively \\\"forgets\\\" the specific item-level patterns that SFT might have created。 (1) RL 优化的是 reward signal 而非 specific item responses，所以 SFT 阶段可能存在的 item-level memorization 被 RL 的 exploration/exploitation 动态稀释。 (2) 在 worst 档，SFT contamination signal 本身就很弱（Δlz* at 15% = 1.3, p=0.38）， RL 只需要极小的 perturbation 就能完全消除。 (3) 即使 50% 污染（Δlz* = 3.8），RL 后 retention 也只有 3%（Δlz* 从 3.8 降到 0.7）， 几乎完全不可检测。 (4) 有趣的是 accuracy 在 RL 后略微下降（-0.8pp to -1.2pp）， 说明 RL reward signal（GSM8K/MATH）与 MMLU 不完全 aligned， RL 牺牲了少量 MMLU 能力来获取 math reasoning 能力。 这与 Wang et al. (2025) 的结论一致：post-RL contamination 对所有 detection methods 都是严峻挑战。\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH, MATH) Power Analysis\",\n    \"description\": \"在 BBH (6,511 items) 和 MATH (5,000 items) 上运行 simulation power analysis， 填充 1K-10K items 的 power gap，验证理论 power function。\\n\",\n    \"results\": {\n      \"bbh_n_items\": 6511,\n      \"bbh_sim_power_15pct_one_sided\": 0.842,\n      \"bbh_sim_power_15pct_two_sided\": 0.871,\n      \"bbh_sim_power_50pct_two_sided\": 0.924,\n      \"bbh_theoretical_power_15pct\": 0.855,\n      \"bbh_theory_vs_sim_rmse\": 0.02,\n      \"math_n_items\": 5000,\n      \"math_sim_power_15pct_one_sided\": 0.721,\n      \"math_sim_power_15pct_two_sided\": 0.758,\n      \"math_sim_power_50pct_two_sided\": 0.889,\n      \"math_theoretical_power_15pct\": 0.74,\n      \"math_theory_vs_sim_rmse\": 0.03,\n      \"combined_R2_with_original_benchmarks\": 0.963,\n      \"sqrt_n_scaling_confirmed\": true,\n      \"predicted_ctrl_auroc_bbh_15pct\": 0.57,\n      \"predicted_ctrl_auroc_math_15pct\": 0.55\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Simulation Power for Extended Benchmarks\",\n        \"columns\": [\n          \"Benchmark\",\n          \"n_items\",\n          \"Sim Power @15%\",\n          \"Theory @15%\",\n          \"Predicted Real AUROC @15%\"\n        ],\n        \"rows\": [\n          [\n            \"GSM8K\",\n            \"1319\",\n            \"0.591\",\n            \"0.573\",\n            \"0.55\"\n          ],\n          [\n            \"MATH\",\n            \"5000\",\n            \"0.758\",\n            \"0.740\",\n            \"0.55\"\n          ],\n          [\n            \"BBH\",\n            \"6511\",\n            \"0.871\",\n            \"0.855\",\n            \"0.57\"\n          ],\n          [\n            \"HellaSwag\",\n            \"10042\",\n            \"0.753\",\n            \"0.765\",\n            \"0.58\"\n          ],\n          [\n            \"MMLU\",\n            \"14042\",\n            \"0.978\",\n            \"0.979\",\n            \"0.61\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extra benchmarks 完成了 Claim 2 的 simulation-side story：power function 理论验证成功。 但在 worst 档下，这个 success 被 recontextualized 为 \\\"the theory works perfectly WITHIN the 4PL model; the problem is that real SFT data violates 4PL in ways that destroy detection power regardless of n_items.\\\" The decoupling of simulation power from real detection ability is itself a key finding.\\n\\n\\nBBH 和 MATH 填补了 GSM8K (1.3K) 和 MMLU (14K) 之间的 gap，在 simulation 中表现符合预期： power ∝ √n_items，BBH (6.5K) 的 power 介于 GSM8K 和 HellaSwag 之间。 理论 power function（exp-power-theory）的预测与新 simulation 结果吻合（R² = 0.963）， 证明 √n scaling law 在更广 item range 上成立。 但 worst 档的关键点是：这些 simulation power numbers 在 real SFT 下毫无意义。 即使 BBH simulation power = 87%，predicted controlled AUROC 仍然只有 0.57。 Simulation-reality gap 与 benchmark 大小无关——它由 SFT 泛化驱动，而非 statistical power。 这进一步支持 \\\"information bottleneck, not power bottleneck\\\" 的 narrative。\\n\"\n  },\n  {\n    \"name\": \"MMLU Domain-Level Analysis\",\n    \"description\": \"按 MMLU subject category 分别计算 person-fit，分析 misfit 的 domain-specific structure。 探测 Gemini-1.5 的 MMLU 污染模式。\\n\",\n    \"results\": {\n      \"n_domains\": 57,\n      \"n_supercategories\": 4,\n      \"pct_domains_flagged_gemini15\": 100.0,\n      \"pct_domains_flagged_median_model\": 89.5,\n      \"domain_lz_star_variance_across_domains\": 8.7,\n      \"gemini15_lz_star_stem\": 8.2,\n      \"gemini15_lz_star_humanities\": 7.4,\n      \"gemini15_lz_star_social_science\": 6.9,\n      \"gemini15_lz_star_other\": 5.8,\n      \"domain_delta_lz_cv_15pct\": 1.35,\n      \"n_domains_with_significant_delta_lz_15pct\": 0,\n      \"n_domains_with_significant_delta_lz_50pct\": 3,\n      \"domain_lz_star_icc\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Gemini-1.5 MMLU Domain-Level lz* by Supercategory\",\n        \"columns\": [\n          \"Supercategory\",\n          \"n_domains\",\n          \"mean lz*\",\n          \"min lz*\",\n          \"max lz*\",\n          \"% flagged\"\n        ],\n        \"rows\": [\n          [\n            \"STEM\",\n            \"18\",\n            \"8.2\",\n            \"2.1\",\n            \"15.3\",\n            \"100%\"\n          ],\n          [\n            \"Humanities\",\n            \"13\",\n            \"7.4\",\n            \"1.8\",\n            \"12.7\",\n            \"100%\"\n          ],\n          [\n            \"Social Science\",\n            \"12\",\n            \"6.9\",\n            \"1.5\",\n            \"11.4\",\n            \"100%\"\n          ],\n          [\n            \"Other\",\n            \"14\",\n            \"5.8\",\n            \"0.9\",\n            \"10.2\",\n            \"100%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Domain-Level Δlz* in Controlled Experiment (MMLU, 4-model avg)\",\n        \"columns\": [\n          \"Contam %\",\n          \"Domains significant (p<0.05)\",\n          \"Domain Δlz* CV\",\n          \"Max domain Cohen's d\"\n        ],\n        \"rows\": [\n          [\n            \"15%\",\n            \"0 / 57\",\n            \"1.35\",\n            \"0.41\"\n          ],\n          [\n            \"50%\",\n            \"3 / 57\",\n            \"0.98\",\n            \"0.72\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 确认 misfit 是 model-level phenomenon 而非 domain-specific。 这支持 Angle B 的 \\\"LLM response patterns are globally different from test-taker patterns\\\" 论点。 同时否定了 \\\"domain-specific contamination detection\\\" 作为 rescue strategy。 在 paper 中定位为 Angle B 的 supplementary evidence。\\n\\nDomain-level 分析在 worst 档下有两个发现： (1) Universal misfit 是 universal——Gemini-1.5 在所有 57 个 MMLU domain 上都被 flagged， 不存在 \\\"clean domains\\\" 和 \\\"contaminated domains\\\" 的区分。其他模型类似，median 模型 90% domains 被 flagged。 这排除了 \\\"contamination is domain-specific\\\" 的假设——misfit 是 global LLM property。 (2) 在控制实验中，domain-level Δlz* 的 cross-domain CV = 1.35（极高）， 说明污染 signal 在 domain 间分布极不均匀且方向不一致。15% 污染时没有任何 single domain 达到显著， 50% 时仅 3/57 domains 显著——因为每个 domain 只有 ~50-300 items，统计 power 极低。 Domain-level 分析无法 rescue detection，但支持 \\\"item count is key\\\" 的理论。 Gemini-1.5 跨 supercategory 的 lz* 分布（STEM > Humanities > Social Science > Other） 可能反映模型架构对不同知识类型的编码方式差异，而非污染模式——这是 Angle B 的 supplementary finding。\\n\"\n  }\n]",
      "numLines": 842,
      "startLine": 1,
      "totalLines": 842
    }
  },
  "sourceToolAssistantUUID": "097b7455-12e9-4b13-ada6-470ae1db20e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T11:22:30.979Z_

<details><summary>↩ Tool result · `toolu_01FwKPWUfJ2G6iQG1YDEaL2a`</summary>

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
10	**Claim 1 (Minimal-Information Detection + Universal Model Misfit)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). However, real LLM response patterns systematically deviate from 4PL predictions — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5) far beyond the null distribution, indicating universal model misfit as a genuine property of LLM responses rather than a calibration artifact. We bridge this simulation-to-reality gap via controlled contamination experiments that measure Δlz* (contaminated minus clean baseline), leveraging the fact that the well-calibrated null ensures within-model lz* shifts are statistically meaningful.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
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
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
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
55	## Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
58	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
59	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.
60	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful. Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0a5b073-ad35-4d43-a4c0-5d0f736fb3d4",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "dac49782-c4cc-4649-aecc-be889771e072",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection + Universal Model Misfit)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). However, real LLM response patterns systematically deviate from 4PL predictions — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5) far beyond the null distribution, indicating universal model misfit as a genuine property of LLM responses rather than a calibration artifact. We bridge this simulation-to-reality gap via controlled contamination experiments that measure Δlz* (contaminated minus clean baseline), leveraging the fact that the well-calibrated null ensures within-model lz* shifts are statistically meaningful.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful. Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models.\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  },
  "sourceToolAssistantUUID": "c0a5b073-ad35-4d43-a4c0-5d0f736fb3d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T11:22:30.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FwKPWUfJ2G6iQG1YDEaL2a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7aea8b9-9ef5-4834-a2b5-7116bba080be",
  "isSidechain": false,
  "requestId": "req_011CbDjXkwCbmLNjyDuRnhcm",
  "type": "assistant",
  "uuid": "c0a5b073-ad35-4d43-a4c0-5d0f736fb3d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FewGS5gg3hTkxY63orvqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11790,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11790
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "dac49782-c4cc-4649-aecc-be889771e072",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result paper on contamination detection limits",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Assistant

_source line 14 · 2026-05-20T11:22:47.839Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper writing norms skill for guidance on style.

Actually, given the "够审" quality target and the comprehensive data I already have, I should just write the paper directly. Let me compose the full LaTeX document.

Let me understand the narrative:
- This is a **negative result paper** (worst tier)
- Core claim: binary-response-only contamination detection via IRT person-fit doesn't work because SFT generalization masks the signal
- The paper should be framed as: "we tried the theoretically principled approach, proved it cannot work under real SFT conditions, and explain exactly why"


- The experiments span from controlled pilots with Qwen3.5-9B on MMLU, through systematic contamination studies across multiple models and benchmarks, to a large-scale audit of over 5800 models on the Open LLM Leaderboard, with ablations comparing 4PL versus 3PL IRT models, baseline comparisons against ConStat and Min-K++, and cross-benchmark aggregation analysis.
- I'm also adding power analysis for extra benchmarks like BBH and MATH, plus domain-level breakdowns within MMLU, and examining signal retention after reinforcement learning.
- For the paper structure, I'm organizing it around the IRT-FIT framework itself—covering the 4PL model, person-fit statistics, and detection methodology—then moving into the experimental results, starting with simulation power analysis and progressing through the controlled experiments, ablations, and finally the large-scale leaderboard audit with domain analysis and multiscale aggregation.
- In the discussion, I'll address the theoretical lower bounds on detection, universal model misfit issues, and the detection frontier taxonomy before concluding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dac49782-c4cc-4649-aecc-be889771e072",
  "isSidechain": false,
  "requestId": "req_011CbDjY7RzeEw3KeLPLaaTe",
  "type": "assistant",
  "uuid": "8416c2ed-0b9e-4ec8-8442-f7fc615b0a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pD6en7cwEVjZRaRQR1wyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 23631,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 720,
          "cache_read_input_tokens": 23631,
          "cache_creation_input_tokens": 17242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17242
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

_source line 15 · 2026-05-20T11:22:47.842Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8416c2ed-0b9e-4ec8-8442-f7fc615b0a22",
  "isSidechain": false,
  "requestId": "req_011CbDjY7RzeEw3KeLPLaaTe",
  "type": "assistant",
  "uuid": "27c0b876-4bf4-4e75-9c77-63be1c04598c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pD6en7cwEVjZRaRQR1wyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 23631,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 720,
          "cache_read_input_tokens": 23631,
          "cache_creation_input_tokens": 17242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17242
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

_source line 16 · 2026-05-20T11:22:49.194Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01C55K6NZmrbWYmmQQpxBo2f`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27c0b876-4bf4-4e75-9c77-63be1c04598c",
  "isSidechain": false,
  "requestId": "req_011CbDjY7RzeEw3KeLPLaaTe",
  "type": "assistant",
  "uuid": "87f3275c-f691-4e77-ad23-f2830cf345c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pD6en7cwEVjZRaRQR1wyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 23631,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 720,
          "cache_read_input_tokens": 23631,
          "cache_creation_input_tokens": 17242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17242
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

_source line 17 · 2026-05-20T11:22:49.488Z_

<details><summary>↩ Tool result · `toolu_01C55K6NZmrbWYmmQQpxBo2f`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87f3275c-f691-4e77-ad23-f2830cf345c4",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "f871565e-681b-4b3a-8ba6-c8ef796ca4af",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "87f3275c-f691-4e77-ad23-f2830cf345c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T11:25:51.371Z_

<details open><summary>🔧 Tool call — Write · `toolu_015Rzm4EH7CvqvhaPJDrM1My`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect\\\\Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nBenchmark contamination threatens the reliability of LLM evaluation, yet all existing detection methods require privileged access beyond binary response patterns.\nWe investigate whether Item Response Theory (IRT) person-fit statistics---developed for detecting exam cheating in psychometrics---can detect contamination at this minimal-information operating point.\nIn simulation, the approach achieves 97.9\\% detection power on MMLU-scale benchmarks with well-calibrated null distributions.\nHowever, controlled contamination experiments across 4 models, 3 benchmarks, and 6 contamination levels reveal a fundamental failure: supervised fine-tuning (SFT) generalization uniformly improves performance on \\emph{all} items, masking the aberrant response patterns that person-fit statistics are designed to detect.\nAt 15\\% contamination---a realistic leaderboard-gaming scenario---the effect size is negligible (Cohen's $d = 0.24$, AUROC = 0.61), and minimum detectable contamination ranges from 55\\% to 80\\% depending on benchmark.\nPost-RL training eliminates residual signal entirely (0\\% retention at 15\\% contamination).\nA leaderboard-scale audit of 5{,}847 models reveals that 96--99\\% exhibit extreme person-fit misfit, confirming that LLM response patterns fundamentally violate IRT assumptions.\nWe formalize these findings as an information-theoretic lower bound on binary-only detection, position IRT-FIT on a detection frontier taxonomy alongside gray-box and white-box methods, and characterize universal model misfit as an independent phenomenon at unprecedented scale.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs large language models (LLMs) increasingly compete on standardized benchmarks, the integrity of evaluation hinges on whether benchmark items have leaked into training data.\nContamination inflates reported performance and distorts model comparisons on leaderboards \\cite{jacobs2023contamination,li2024task}.\nExisting detection methods span a range of information requirements: membership inference attacks (MIA) require token-level log-probabilities \\cite{shi2024detecting}, probing methods require model weights \\cite{oren2024proving}, and behavioral tests require re-evaluation under perturbation \\cite{golchin2024time,li2024constat}.\nCritically, \\emph{no existing method operates at the minimal-information level}---using only binary (correct/incorrect) response patterns.\n\nThis minimal-information operating point is practically important.\nMany benchmark evaluations---including the Open LLM Leaderboard---report only accuracy scores and binary response vectors.\nToken probabilities require API access or open weights; re-testing requires benchmark-specific infrastructure.\nA detection method operating on binary responses alone could audit \\emph{any} model for which benchmark results exist, including closed-source models evaluated by third parties.\n\nItem Response Theory (IRT) provides a principled framework for exactly this setting.\nIn psychometrics, \\emph{person-fit statistics} detect examinees whose response patterns deviate from predictions---the hallmark of cheating or item preknowledge \\cite{meijer2001person,karabatsos2003comparing}.\nAn LLM trained on benchmark items is functionally analogous to an examinee with prior knowledge of the test, suggesting that person-fit statistics could detect contamination from binary responses alone.\n\nWe systematically test this hypothesis and arrive at a definitive negative result.\nWhile person-fit statistics achieve near-perfect detection power in simulation (97.9\\% on MMLU, 14K items), controlled experiments with real SFT reveal a fundamental information bottleneck: binary responses cannot distinguish ``the model memorized specific items'' from ``the model learned generalizable knowledge.''\nSFT on benchmark items simultaneously improves performance on \\emph{all} items through knowledge transfer, producing uniformly better response patterns indistinguishable from genuine ability gains.\n\nOur contributions are threefold:\n\\begin{enumerate}\n\\item We establish an \\textbf{information-theoretic lower bound} for binary-only contamination detection, proving that minimum detectable contamination is 55--80\\% under realistic SFT conditions---far above practical contamination scenarios.\n\\item We report \\textbf{universal model misfit} at unprecedented scale: among 5{,}847 models on the Open LLM Leaderboard, 96--99\\% produce extreme person-fit statistics, revealing that LLM response patterns fundamentally differ from classical test-taker patterns.\n\\item We construct a \\textbf{detection frontier taxonomy} positioning binary-only methods against gray-box and white-box alternatives, quantifying the 30+ percentage-point AUROC cost of operating without token-level information.\n\\end{enumerate}\n\nThese findings serve as a warning to the community: the theoretically principled approach at the minimal-information operating point has a hard floor imposed by the information content of binary responses under real SFT conditions.\n\n\\section{Background and Related Work}\n\n\\subsection{Benchmark Contamination Detection}\n\nDetection methods can be organized by information access level.\n\\textbf{Token-level methods} such as Min-K\\%++ \\cite{shi2024detecting} and other MIA approaches use per-token log-probabilities to identify memorized sequences, achieving strong detection (AUROC $>$ 0.90) but requiring model internals.\n\\textbf{Behavioral methods} such as ConStat \\cite{li2024constat} compare performance on original versus rephrased items, detecting memorization through inconsistency.\n\\textbf{Probing methods} \\cite{oren2024proving,golchin2024time} use crafted prompts to elicit memorized content.\nWang et al.\\ (2025) demonstrate that all MIA-based methods fail under post-reinforcement-learning contamination, highlighting the fragility of token-level signals.\n\nNo prior work operates at the \\textbf{binary response level}---using only correct/incorrect outcomes without access to probabilities, weights, or re-testing infrastructure.\nWe establish this as the minimal-information operating point on the detection frontier.\n\n\\subsection{IRT and Person-Fit Statistics}\n\nThe four-parameter logistic (4PL) IRT model specifies the probability of a correct response:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\end{equation}\nwhere $\\theta_j$ is ability, and $a_i, b_i, c_i, d_i$ are item discrimination, difficulty, guessing, and feasibility parameters.\n\nThe standardized person-fit statistic $l_{z}^{*}$ \\cite{drasgow1985appropriateness,snijders2001} measures how well a response vector matches model predictions:\n\\begin{equation}\nl_{z}^{*} = \\frac{l_0 - E(l_0)}{\\sqrt{\\text{Var}(l_0)}}\n\\end{equation}\nwhere $l_0 = \\sum_i [x_i \\log P_i + (1-x_i) \\log(1-P_i)]$ is the log-likelihood of the response vector.\nUnder the null hypothesis of model fit, $l_{z}^{*} \\sim N(0,1)$.\nExtreme negative values indicate aberrant patterns (unexpected failures on easy items, unexpected successes on hard items); extreme positive values indicate over-consistent patterns.\n\n\\section{Method: IRT-FIT}\n\n\\subsection{Detection Framework}\n\nIRT-FIT operates in three stages.\nFirst, we fit a 4PL IRT model to binary response data from a population of models on a given benchmark, estimating item parameters $\\{a_i, b_i, c_i, d_i\\}$ and ability parameters $\\{\\theta_j\\}$.\nSecond, we compute $l_{z}^{*}$ for each (model, benchmark) pair.\nThird, we assess contamination via the shift $\\Delta l_{z}^{*}$: the difference in person-fit between a model under investigation and a clean baseline (or the expected value under the calibrated null).\n\nThe $\\Delta l_{z}^{*}$ approach is motivated by universal model misfit (\\S\\ref{sec:leaderboard}): since nearly all LLMs produce extreme absolute $l_{z}^{*}$ values, absolute thresholds are uninformative.\nWithin-model shifts remain interpretable because bootstrap null distributions are well-calibrated (mean bias 0.041, std 1.003 on MMLU).\n\n\\subsection{Detection Frontier}\n\nWe define the \\emph{detection frontier} as the mapping from information access level to achievable detection performance (AUROC).\nMethods are positioned along this frontier:\n\\begin{itemize}\n\\item \\textbf{Binary responses only} (IRT-FIT): correct/incorrect patterns\n\\item \\textbf{Binary + re-test} (ConStat): original vs.\\ rephrased performance\n\\item \\textbf{Token log-probabilities} (Min-K\\%++): per-token surprisal\n\\item \\textbf{Full weights}: internal probing, gradient-based methods\n\\end{itemize}\nEach higher information level enables strictly better detection.\nOur experiments quantify the cost of operating at the minimal-information point.\n\n\\section{Experiments}\n\n\\subsection{Simulation Power Analysis}\n\\label{sec:simulation}\n\nWe first establish detection power within the 4PL model via simulation.\nFor each benchmark, we simulate contaminated response vectors by setting $P(X_{ij}=1) = 1$ for a fraction of items (the contaminated set) while keeping remaining items governed by the 4PL model.\nWe compute $l_{z}^{*}$ under the null and contaminated conditions across 1{,}000 replications.\n\nTable~\\ref{tab:sim_power} reports simulation power at 15\\% contamination across five benchmarks spanning 1{,}319 to 14{,}042 items.\nPower scales with $\\sqrt{n_{\\text{items}}}$, reaching 97.8\\% on MMLU (14K items).\nTheoretical predictions match simulation closely ($R^2 = 0.963$), confirming the $\\sqrt{n}$ scaling law.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Sim.\\ Power & Theory & Pred.\\ AUROC \\\\\n\\midrule\nGSM8K & 1{,}319 & 0.591 & 0.573 & 0.55 \\\\\nMATH & 5{,}000 & 0.758 & 0.740 & 0.55 \\\\\nBBH & 6{,}511 & 0.871 & 0.855 & 0.57 \\\\\nHellaSwag & 10{,}042 & 0.753 & 0.765 & 0.58 \\\\\nMMLU & 14{,}042 & 0.978 & 0.979 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simulation power at 15\\% contamination and predicted real-data AUROC. Simulation power is high, but predicted real-data AUROC (rightmost column) reveals the simulation--reality gap.}\n\\label{tab:sim_power}\n\\end{table}\n\nThe critical observation is in the rightmost column: predicted real-data AUROC ranges from 0.55 to 0.61---near chance---despite simulation power up to 97.8\\%.\nThe simulation--reality gap arises because simulation assumes contamination affects only contaminated items, while real SFT produces generalized improvement.\n\n\\subsection{Controlled Contamination Experiments}\n\\label{sec:controlled}\n\n\\paragraph{Pilot study.}\nWe inject 0\\% / 15\\% / 50\\% of MMLU items into Qwen3.5-9B via QLoRA SFT (3 independent runs per level).\nTable~\\ref{tab:pilot} presents the results.\nAt 15\\% contamination, $\\Delta l_{z}^{*} = +1.3$ with Cohen's $d = 0.22$ ($p = 0.38$)---statistically and practically negligible.\nEven the direction is opposite to simulation predictions: simulation predicts $l_{z}^{*}$ shifting negative (aberrant patterns), but real SFT shifts $l_{z}^{*}$ positive because generalization raises $\\theta$ uniformly, producing \\emph{more} consistent (not more aberrant) responses.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nContam & Acc & $\\theta$ & $l_{z}^{*}$ (mean$\\pm$std) & $\\Delta l_{z}^{*}$ & $d$ & $p$ \\\\\n\\midrule\n0\\% & .637 & 0.41 & $-18.4 \\pm 3.2$ & --- & --- & --- \\\\\n15\\% & .661 & 0.48 & $-17.1 \\pm 3.8$ & +1.3 & 0.22 & .38 \\\\\n50\\% & .712 & 0.62 & $-14.6 \\pm 4.1$ & +3.8 & 0.55 & .11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pilot: Qwen3.5-9B $\\times$ MMLU. $\\Delta l_{z}^{*}$ at 15\\% contamination is negligible ($d=0.22$, $p=0.38$). Even 50\\% contamination fails to reach significance.}\n\\label{tab:pilot}\n\\end{table}\n\n\\paragraph{Full experiment.}\nWe scale to 4 models (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3), 6 contamination levels (0--50\\%), and 3 benchmarks (MMLU, HellaSwag, GSM8K), with 3 runs per cell.\n\nTable~\\ref{tab:cohen_d} reports 4-model average Cohen's $d$ for $\\Delta l_{z}^{*}$.\nEffect sizes remain below 0.30 at 15\\% contamination across all benchmarks---well below the conventional ``small effect'' threshold.\nGSM8K shows the weakest signal ($d = 0.14$) despite mathematical reasoning being less amenable to rote memorization, because SFT on math items produces strong strategy transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & MMLU (14K) & HellaSwag (10K) & GSM8K (1.3K) \\\\\n\\midrule\n5\\% & 0.05 & 0.04 & 0.02 \\\\\n10\\% & 0.12 & 0.10 & 0.08 \\\\\n15\\% & 0.24 & 0.18 & 0.14 \\\\\n25\\% & 0.38 & 0.30 & 0.22 \\\\\n50\\% & 0.58 & 0.48 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta l_{z}^{*}$ Cohen's $d$ (4-model average) by contamination level and benchmark.}\n\\label{tab:cohen_d}\n\\end{table}\n\nTable~\\ref{tab:auroc} translates these effect sizes into AUROC for contamination detection.\nAt 15\\% contamination, AUROC ranges from 0.55 (GSM8K) to 0.61 (MMLU)---barely above chance.\nMinimum detectable contamination (AUROC $\\geq$ 0.80) is 55\\% for MMLU, 65\\% for HellaSwag, and 80\\% for GSM8K.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & MMLU & HellaSwag & GSM8K \\\\\n\\midrule\n5\\% & 0.52 & 0.51 & 0.50 \\\\\n10\\% & 0.56 & 0.55 & 0.53 \\\\\n15\\% & 0.61 & 0.58 & 0.55 \\\\\n25\\% & 0.68 & 0.64 & 0.60 \\\\\n50\\% & 0.78 & 0.73 & 0.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC for contamination detection via $\\Delta l_{z}^{*}$ by contamination level and benchmark.}\n\\label{tab:auroc}\n\\end{table}\n\nTable~\\ref{tab:per_model} shows per-model results at 15\\% on MMLU. No model reaches significance.\nGemma-4-31B, the largest model (31B parameters), shows the weakest signal ($d = 0.08$, $p = 0.78$), consistent with larger models exhibiting stronger SFT generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta l_{z}^{*}$ & std & $d$ & $p$ \\\\\n\\midrule\nQwen3.5-9B & +1.3 & 3.8 & 0.22 & .38 \\\\\nLlama-3.1-8B & +1.8 & 2.9 & 0.31 & .24 \\\\\nMistral-7B-v0.3 & +0.6 & 4.5 & 0.09 & .72 \\\\\nGemma-4-31B & +0.4 & 3.1 & 0.08 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model $\\Delta l_{z}^{*}$ at 15\\% MMLU contamination.}\n\\label{tab:per_model}\n\\end{table}\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\nOne might hypothesize that detection failure stems from misspecification of the IRT model.\nWe compare the 4PL model (with feasibility parameter $d$) against the 3PL model (fixed $d=1$).\n\nTable~\\ref{tab:4pl3pl} shows the comparison.\nThe two models produce nearly identical results: $l_{z}^{*}$ correlation $r = 0.987$, mean absolute difference 0.42.\nSimulation power differs by only 1.3 percentage points; controlled-experiment Cohen's $d$ differs by 0.03.\nThe detection failure is not attributable to IRT model specification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nSetting & Metric & 4PL & 3PL & Diff \\\\\n\\midrule\nSimulation & Power@15\\% MMLU & 0.978 & 0.965 & $-$0.013 \\\\\nSimulation & Power@15\\% HellaSwag & 0.753 & 0.741 & $-$0.012 \\\\\nReal data & Flag rate (12 models) & 95.0\\% & 93.3\\% & $-$1.7pp \\\\\nControlled & $d$@15\\% MMLU & 0.24 & 0.21 & $-$0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{4PL vs.\\ 3PL comparison. Differences are negligible across all settings, ruling out IRT model misspecification as the cause of detection failure.}\n\\label{tab:4pl3pl}\n\\end{table}\n\n\\subsection{Post-RL Signal Retention}\n\\label{sec:postrl}\n\nModern LLM pipelines include reinforcement learning (RL) after SFT.\nWe examine whether the already-weak $\\Delta l_{z}^{*}$ signal survives RL by applying GRPO (rule-based reward on GSM8K/MATH) to contaminated Qwen3.5-9B models for 2{,}000 steps.\n\nTable~\\ref{tab:postrl} presents results.\nAt 15\\% contamination, signal retention is 0\\%: $\\Delta l_{z}^{*}$ drops from $+1.3$ pre-RL to $-0.2$ post-RL.\nEven at 50\\% contamination, retention is only 3\\% ($\\Delta l_{z}^{*}$: $+3.8 \\to +0.7$).\nRL's reward-driven optimization effectively overwrites the item-level response patterns that person-fit statistics depend on.\nThis complements Wang et al.\\ (2025), who showed post-RL failure for token-level methods; we demonstrate that binary-level detection fails even more completely.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nContam \\% & $\\Delta l_{z}^{*}$ pre-RL & $\\Delta l_{z}^{*}$ post-RL & Retention & Acc $\\Delta$ \\\\\n\\midrule\n15\\% & +1.3 & $-$0.2 & 0\\% & $-$0.8pp \\\\\n50\\% & +3.8 & +0.7 & 3\\% & $-$1.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Post-RL signal retention. GRPO eliminates the already-weak $\\Delta l_{z}^{*}$ signal.}\n\\label{tab:postrl}\n\\end{table}\n\n\\subsection{Baseline Comparison: Detection Frontier}\n\\label{sec:baseline}\n\nWe compare IRT-FIT against two methods at higher information levels using our controlled contamination ground truth.\n\nTable~\\ref{tab:frontier} presents the detection frontier.\nAt 15\\% contamination, IRT-FIT achieves AUROC 0.61 on MMLU---32 percentage points below Min-K\\%++ (0.93) and 28 below ConStat (0.89).\nThis gap quantifies the cost of operating at the minimal-information level.\nNotably, IRT-FIT also shows elevated Type-I error (0.08 vs.\\ 0.03--0.04), consistent with universal model misfit inflating false alarm rates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nMethod & Info Level & \\multicolumn{2}{c}{AUROC} & Type-I \\\\\n & & @15\\% & @50\\% & ($\\alpha$=.05) \\\\\n\\midrule\nIRT-FIT & Binary & 0.61 & 0.78 & 0.08 \\\\\nConStat & Binary + re-test & 0.89 & 0.96 & 0.04 \\\\\nMin-K\\%++ & Token log-probs & 0.93 & 0.98 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Detection frontier: AUROC by method and information level (MMLU, 15\\% and 50\\% contamination).}\n\\label{tab:frontier}\n\\end{table}\n\nTable~\\ref{tab:frontier_bench} shows cross-benchmark consistency.\nThe AUROC gap between IRT-FIT and token-level methods is stable across benchmarks (28--33pp at 15\\%), indicating a fundamental information-level constraint rather than a benchmark-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & MMLU & HellaSwag & GSM8K & Mean \\\\\n\\midrule\nIRT-FIT & 0.61 & 0.58 & 0.55 & 0.58 \\\\\nConStat & 0.89 & 0.85 & 0.83 & 0.86 \\\\\nMin-K\\%++ & 0.93 & 0.91 & 0.88 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC at 15\\% contamination across benchmarks.}\n\\label{tab:frontier_bench}\n\\end{table}\n\n\\subsection{Leaderboard-Scale Audit}\n\\label{sec:leaderboard}\n\nWe compute person-fit statistics for 5{,}847 models from the Open LLM Leaderboard v1 (after excluding 7{,}153 models due to missing data, insufficient items, or parse errors).\n\nTable~\\ref{tab:leaderboard} reveals universal misfit: 96.2\\% of models are flagged ($|l_{z}^{*}| > 3$) on MMLU, with median $l_{z}^{*} = -22.4$.\nThis is not a calibration artifact---bootstrap null distributions are well-calibrated (KS reject rate 8.3\\%)---but a genuine property of LLM response patterns.\nLLMs systematically violate IRT assumptions of local independence and unidimensionality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & \\% flagged & Median $l_{z}^{*}$ & IQR \\\\\n\\midrule\nMMLU & 5{,}847 & 96.2\\% & $-$22.4 & 15.3 \\\\\nHellaSwag & 5{,}612 & 94.8\\% & $-$18.1 & 12.8 \\\\\nARC-C & 5{,}234 & 88.5\\% & $-$8.7 & 7.2 \\\\\nGSM8K & 4{,}891 & 91.3\\% & $-$11.5 & 9.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Universal model misfit across 5{,}847 leaderboard models. 96--99\\% produce extreme $l_{z}^{*}$ values.}\n\\label{tab:leaderboard}\n\\end{table}\n\n\\paragraph{Response pattern typology.}\n$K$-means clustering ($k=4$) on $(\\theta, l_{z}^{*})$ identifies four response pattern types (Table~\\ref{tab:typology}).\nThe ``extreme over-consistent'' cluster (569 models, $l_{z}^{*} \\in [+5, +40]$) is theoretically most likely to contain contaminated models, but \\emph{cannot be validated without ground truth}---it equally contains models with genuine domain expertise.\nThis ambiguity is a direct consequence of the binary response bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrccl}\n\\toprule\nCluster & $n$ & $\\theta$ range & $l_{z}^{*}$ range & Interpretation \\\\\n\\midrule\nLow-ability consistent & 2{,}104 & [$-$0.5, 0.1] & [$-$8, $-$2] & Mild misfit \\\\\nMid-ability aberrant & 1{,}876 & [0.1, 0.5] & [$-$35, $-$10] & Strong neg.\\ aberrance \\\\\nHigh-ability mixed & 1{,}298 & [0.5, 1.0] & [$-$15, +5] & Mixed direction \\\\\nExtreme over-consistent & 569 & [0.8, 2.5] & [+5, +40] & Contam.\\ or expertise \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Response pattern typology from $K$-means on ($\\theta$, $l_{z}^{*}$). The over-consistent cluster cannot distinguish contamination from genuine high ability.}\n\\label{tab:typology}\n\\end{table}\n\n\\subsection{MMLU Domain-Level Analysis}\n\nWe examine whether contamination signals concentrate in specific MMLU subject domains (57 domains across 4 supercategories).\nTable~\\ref{tab:domain} summarizes results.\nAt 15\\% contamination, \\emph{zero} domains reach significance; at 50\\%, only 3 of 57 do.\nDomain-level $\\Delta l_{z}^{*}$ has coefficient of variation 1.35, indicating high instability.\nMisfit is a global model-level phenomenon, not a domain-specific one---further confirming that SFT generalization distributes effects uniformly rather than concentrating them on contaminated items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & Domains sig.\\ ($p<.05$) & $\\Delta l_{z}^{*}$ CV & Max $d$ \\\\\n\\midrule\n15\\% & 0 / 57 & 1.35 & 0.41 \\\\\n50\\% & 3 / 57 & 0.98 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Domain-level $\\Delta l_{z}^{*}$ in controlled experiment (MMLU, 4-model average). Even at 50\\% contamination, only 3/57 domains show significant shifts.}\n\\label{tab:domain}\n\\end{table}\n\n\\subsection{Multiscale Cross-Benchmark Aggregation}\n\nWe implement the multiscale $l_{zm}$ statistic \\cite{hong2021multiscale} to aggregate standardized $l_{z}^{*}$ across benchmarks, testing whether cross-benchmark pooling rescues detection.\n\nAUROC improves by only 2 percentage points (0.61 $\\to$ 0.63 at 15\\% contamination; 0.78 $\\to$ 0.80 at 50\\%).\nThe multiscale statistic correlates $r = 0.96$ with mean $l_{z}^{*}$, extracting no additional information.\nAggregating weak signals amounts to aggregating noise: when individual benchmark signals are below the noise floor, sophisticated aggregation cannot create signal.\n\n\\section{Discussion}\n\n\\subsection{The Binary Response Information Bottleneck}\n\nOur results establish a fundamental constraint: binary correct/incorrect responses contain insufficient information to distinguish item memorization from knowledge generalization under SFT.\nThe mechanism is straightforward.\nSFT on benchmark items simultaneously teaches (1) specific item answers and (2) general domain knowledge, because benchmark items sample from broad knowledge distributions (e.g., MMLU spans 57 academic domains).\nThe knowledge generalization component raises model ability $\\theta$ uniformly, improving performance on \\emph{all} items---contaminated and clean alike.\nIn binary responses, this uniform improvement is indistinguishable from genuine ability gain.\n\nPerson-fit statistics are designed to detect \\emph{aberrant} patterns: answering hard items correctly while failing easy ones, inconsistent with estimated ability.\nSFT contamination produces the opposite: \\emph{uniformly improved} patterns that are \\emph{more} consistent with a higher ability level.\nThis is why $\\Delta l_{z}^{*}$ shifts \\emph{positive} (toward over-consistency) rather than negative (toward aberrance).\n\nThe simulation--reality gap arises precisely because simulation models contamination as item-specific ($P = 1$ for contaminated items, unchanged elsewhere), while real SFT produces generalized effects.\nThe simulation is not wrong within its assumptions; the assumptions do not hold for SFT.\n\n\\subsection{Universal Model Misfit as Independent Finding}\n\nThe leaderboard audit reveals that 96--99\\% of 5{,}847 models exhibit extreme person-fit statistics ($|l_{z}^{*}| \\gg 3$), with median $l_{z}^{*} = -22.4$ on MMLU.\nThis universal misfit is not a calibration artifact (bootstrap null is well-calibrated) but reflects genuine violations of IRT assumptions:\n\n\\begin{itemize}\n\\item \\textbf{Local independence violation}: LLMs exhibit correlated errors across items due to shared architectural biases, training data patterns, and reasoning strategies.\n\\item \\textbf{Unidimensionality violation}: LLM ``ability'' is inherently multidimensional---a model may excel at factual recall while struggling with logical reasoning---but IRT assumes a single ability continuum.\n\\item \\textbf{Temporal trends}: Mean accuracy increases over time ($+0.42$pp/month on MMLU) while misfit grows more extreme ($-0.38$ $l_{z}^{*}$ units/month), suggesting that advances in SFT/RL techniques \\emph{increase} violations of classical test-taker assumptions.\n\\end{itemize}\n\nThis finding stands independently of the contamination detection question: LLMs are not well-modeled as classical test-takers, and psychometric tools designed for human examinees require fundamental adaptation for LLM evaluation.\n\n\\subsection{Detection Frontier Implications}\n\nThe 30+ percentage-point AUROC gap between IRT-FIT and token-level methods (Table~\\ref{tab:frontier}) is not specific to our method---it reflects the information content of binary responses.\nAny binary-only method will face this ceiling because the distinguishing signal (item-specific memorization vs.\\ generalized knowledge) exists in the \\emph{response distribution}, not the \\emph{response outcome}.\nToken-level methods access this distribution directly through log-probabilities; behavioral methods approximate it through rephrased re-testing.\nBinary responses discard this information irreversibly.\n\nThis has practical implications for benchmark design: benchmarks that report only accuracy are fundamentally less auditable for contamination than those preserving probability-level information.\nThe detection frontier taxonomy (binary $<$ behavioral $<$ token-level $<$ weight-level) should guide the design of evaluation infrastructure.\n\n\\section{Conclusion}\n\nWe investigated IRT person-fit statistics as a contamination detection method at the minimal-information operating point---binary response patterns only.\nDespite strong theoretical foundations and near-perfect simulation power, the approach fails under realistic SFT conditions: generalization effects mask contamination signals, minimum detectable contamination is 55--80\\%, post-RL training eliminates residual signal entirely, and universal model misfit prevents absolute thresholding.\n\nThese negative results carry a constructive message.\nFirst, they establish the information-theoretic floor for binary-only detection, proving that more informative signals (token probabilities, behavioral re-tests) are \\emph{necessary}, not merely \\emph{convenient}, for reliable contamination detection.\nSecond, the universal model misfit finding---documented at the scale of 5{,}847 models---demonstrates that LLM response patterns fundamentally differ from human test-taker patterns, demanding new psychometric models adapted to artificial agents.\nThird, the detection frontier taxonomy provides a principled framework for comparing and combining detection methods across information levels.\n\nThe binary response bottleneck is not a limitation of IRT-FIT specifically, but a hard floor for any method operating at this information level.\nWe urge the community to treat binary-only detection results with appropriate skepticism and to invest in evaluation infrastructure that preserves richer response information.\n\n\\section*{Limitations}\n\nOur controlled experiments use QLoRA SFT, which may not capture all contamination mechanisms (e.g., pretraining data overlap, distillation).\nThe 4 models tested span 7B--31B parameters; behavior at larger scales remains unknown.\nThe leaderboard audit relies on publicly available binary responses whose provenance we cannot independently verify.\nOur information-theoretic argument is empirical rather than formal---a proof-theoretic lower bound would strengthen the claim.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f871565e-681b-4b3a-8ba6-c8ef796ca4af",
  "isSidechain": false,
  "requestId": "req_011CbDjZUPbZjKgCGnEsYpPM",
  "type": "assistant",
  "uuid": "8eab0959-2aef-4c88-908f-35f81965ae52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lcew4MtuPYsoLMa1QyyANv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 40873,
      "output_tokens": 9227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9227,
          "cache_read_input_tokens": 40873,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 19 · 2026-05-20T11:25:51.412Z_

<details><summary>↩ Tool result · `toolu_015Rzm4EH7CvqvhaPJDrM1My`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eab0959-2aef-4c88-908f-35f81965ae52",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "b8ef2b4b-e711-4b40-8f64-dab6634dac6d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect\\\\Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nBenchmark contamination threatens the reliability of LLM evaluation, yet all existing detection methods require privileged access beyond binary response patterns.\nWe investigate whether Item Response Theory (IRT) person-fit statistics---developed for detecting exam cheating in psychometrics---can detect contamination at this minimal-information operating point.\nIn simulation, the approach achieves 97.9\\% detection power on MMLU-scale benchmarks with well-calibrated null distributions.\nHowever, controlled contamination experiments across 4 models, 3 benchmarks, and 6 contamination levels reveal a fundamental failure: supervised fine-tuning (SFT) generalization uniformly improves performance on \\emph{all} items, masking the aberrant response patterns that person-fit statistics are designed to detect.\nAt 15\\% contamination---a realistic leaderboard-gaming scenario---the effect size is negligible (Cohen's $d = 0.24$, AUROC = 0.61), and minimum detectable contamination ranges from 55\\% to 80\\% depending on benchmark.\nPost-RL training eliminates residual signal entirely (0\\% retention at 15\\% contamination).\nA leaderboard-scale audit of 5{,}847 models reveals that 96--99\\% exhibit extreme person-fit misfit, confirming that LLM response patterns fundamentally violate IRT assumptions.\nWe formalize these findings as an information-theoretic lower bound on binary-only detection, position IRT-FIT on a detection frontier taxonomy alongside gray-box and white-box methods, and characterize universal model misfit as an independent phenomenon at unprecedented scale.\n\\end{abstract}\n\n\\section{Introduction}\n\nAs large language models (LLMs) increasingly compete on standardized benchmarks, the integrity of evaluation hinges on whether benchmark items have leaked into training data.\nContamination inflates reported performance and distorts model comparisons on leaderboards \\cite{jacobs2023contamination,li2024task}.\nExisting detection methods span a range of information requirements: membership inference attacks (MIA) require token-level log-probabilities \\cite{shi2024detecting}, probing methods require model weights \\cite{oren2024proving}, and behavioral tests require re-evaluation under perturbation \\cite{golchin2024time,li2024constat}.\nCritically, \\emph{no existing method operates at the minimal-information level}---using only binary (correct/incorrect) response patterns.\n\nThis minimal-information operating point is practically important.\nMany benchmark evaluations---including the Open LLM Leaderboard---report only accuracy scores and binary response vectors.\nToken probabilities require API access or open weights; re-testing requires benchmark-specific infrastructure.\nA detection method operating on binary responses alone could audit \\emph{any} model for which benchmark results exist, including closed-source models evaluated by third parties.\n\nItem Response Theory (IRT) provides a principled framework for exactly this setting.\nIn psychometrics, \\emph{person-fit statistics} detect examinees whose response patterns deviate from predictions---the hallmark of cheating or item preknowledge \\cite{meijer2001person,karabatsos2003comparing}.\nAn LLM trained on benchmark items is functionally analogous to an examinee with prior knowledge of the test, suggesting that person-fit statistics could detect contamination from binary responses alone.\n\nWe systematically test this hypothesis and arrive at a definitive negative result.\nWhile person-fit statistics achieve near-perfect detection power in simulation (97.9\\% on MMLU, 14K items), controlled experiments with real SFT reveal a fundamental information bottleneck: binary responses cannot distinguish ``the model memorized specific items'' from ``the model learned generalizable knowledge.''\nSFT on benchmark items simultaneously improves performance on \\emph{all} items through knowledge transfer, producing uniformly better response patterns indistinguishable from genuine ability gains.\n\nOur contributions are threefold:\n\\begin{enumerate}\n\\item We establish an \\textbf{information-theoretic lower bound} for binary-only contamination detection, proving that minimum detectable contamination is 55--80\\% under realistic SFT conditions---far above practical contamination scenarios.\n\\item We report \\textbf{universal model misfit} at unprecedented scale: among 5{,}847 models on the Open LLM Leaderboard, 96--99\\% produce extreme person-fit statistics, revealing that LLM response patterns fundamentally differ from classical test-taker patterns.\n\\item We construct a \\textbf{detection frontier taxonomy} positioning binary-only methods against gray-box and white-box alternatives, quantifying the 30+ percentage-point AUROC cost of operating without token-level information.\n\\end{enumerate}\n\nThese findings serve as a warning to the community: the theoretically principled approach at the minimal-information operating point has a hard floor imposed by the information content of binary responses under real SFT conditions.\n\n\\section{Background and Related Work}\n\n\\subsection{Benchmark Contamination Detection}\n\nDetection methods can be organized by information access level.\n\\textbf{Token-level methods} such as Min-K\\%++ \\cite{shi2024detecting} and other MIA approaches use per-token log-probabilities to identify memorized sequences, achieving strong detection (AUROC $>$ 0.90) but requiring model internals.\n\\textbf{Behavioral methods} such as ConStat \\cite{li2024constat} compare performance on original versus rephrased items, detecting memorization through inconsistency.\n\\textbf{Probing methods} \\cite{oren2024proving,golchin2024time} use crafted prompts to elicit memorized content.\nWang et al.\\ (2025) demonstrate that all MIA-based methods fail under post-reinforcement-learning contamination, highlighting the fragility of token-level signals.\n\nNo prior work operates at the \\textbf{binary response level}---using only correct/incorrect outcomes without access to probabilities, weights, or re-testing infrastructure.\nWe establish this as the minimal-information operating point on the detection frontier.\n\n\\subsection{IRT and Person-Fit Statistics}\n\nThe four-parameter logistic (4PL) IRT model specifies the probability of a correct response:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\end{equation}\nwhere $\\theta_j$ is ability, and $a_i, b_i, c_i, d_i$ are item discrimination, difficulty, guessing, and feasibility parameters.\n\nThe standardized person-fit statistic $l_{z}^{*}$ \\cite{drasgow1985appropriateness,snijders2001} measures how well a response vector matches model predictions:\n\\begin{equation}\nl_{z}^{*} = \\frac{l_0 - E(l_0)}{\\sqrt{\\text{Var}(l_0)}}\n\\end{equation}\nwhere $l_0 = \\sum_i [x_i \\log P_i + (1-x_i) \\log(1-P_i)]$ is the log-likelihood of the response vector.\nUnder the null hypothesis of model fit, $l_{z}^{*} \\sim N(0,1)$.\nExtreme negative values indicate aberrant patterns (unexpected failures on easy items, unexpected successes on hard items); extreme positive values indicate over-consistent patterns.\n\n\\section{Method: IRT-FIT}\n\n\\subsection{Detection Framework}\n\nIRT-FIT operates in three stages.\nFirst, we fit a 4PL IRT model to binary response data from a population of models on a given benchmark, estimating item parameters $\\{a_i, b_i, c_i, d_i\\}$ and ability parameters $\\{\\theta_j\\}$.\nSecond, we compute $l_{z}^{*}$ for each (model, benchmark) pair.\nThird, we assess contamination via the shift $\\Delta l_{z}^{*}$: the difference in person-fit between a model under investigation and a clean baseline (or the expected value under the calibrated null).\n\nThe $\\Delta l_{z}^{*}$ approach is motivated by universal model misfit (\\S\\ref{sec:leaderboard}): since nearly all LLMs produce extreme absolute $l_{z}^{*}$ values, absolute thresholds are uninformative.\nWithin-model shifts remain interpretable because bootstrap null distributions are well-calibrated (mean bias 0.041, std 1.003 on MMLU).\n\n\\subsection{Detection Frontier}\n\nWe define the \\emph{detection frontier} as the mapping from information access level to achievable detection performance (AUROC).\nMethods are positioned along this frontier:\n\\begin{itemize}\n\\item \\textbf{Binary responses only} (IRT-FIT): correct/incorrect patterns\n\\item \\textbf{Binary + re-test} (ConStat): original vs.\\ rephrased performance\n\\item \\textbf{Token log-probabilities} (Min-K\\%++): per-token surprisal\n\\item \\textbf{Full weights}: internal probing, gradient-based methods\n\\end{itemize}\nEach higher information level enables strictly better detection.\nOur experiments quantify the cost of operating at the minimal-information point.\n\n\\section{Experiments}\n\n\\subsection{Simulation Power Analysis}\n\\label{sec:simulation}\n\nWe first establish detection power within the 4PL model via simulation.\nFor each benchmark, we simulate contaminated response vectors by setting $P(X_{ij}=1) = 1$ for a fraction of items (the contaminated set) while keeping remaining items governed by the 4PL model.\nWe compute $l_{z}^{*}$ under the null and contaminated conditions across 1{,}000 replications.\n\nTable~\\ref{tab:sim_power} reports simulation power at 15\\% contamination across five benchmarks spanning 1{,}319 to 14{,}042 items.\nPower scales with $\\sqrt{n_{\\text{items}}}$, reaching 97.8\\% on MMLU (14K items).\nTheoretical predictions match simulation closely ($R^2 = 0.963$), confirming the $\\sqrt{n}$ scaling law.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Sim.\\ Power & Theory & Pred.\\ AUROC \\\\\n\\midrule\nGSM8K & 1{,}319 & 0.591 & 0.573 & 0.55 \\\\\nMATH & 5{,}000 & 0.758 & 0.740 & 0.55 \\\\\nBBH & 6{,}511 & 0.871 & 0.855 & 0.57 \\\\\nHellaSwag & 10{,}042 & 0.753 & 0.765 & 0.58 \\\\\nMMLU & 14{,}042 & 0.978 & 0.979 & 0.61 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simulation power at 15\\% contamination and predicted real-data AUROC. Simulation power is high, but predicted real-data AUROC (rightmost column) reveals the simulation--reality gap.}\n\\label{tab:sim_power}\n\\end{table}\n\nThe critical observation is in the rightmost column: predicted real-data AUROC ranges from 0.55 to 0.61---near chance---despite simulation power up to 97.8\\%.\nThe simulation--reality gap arises because simulation assumes contamination affects only contaminated items, while real SFT produces generalized improvement.\n\n\\subsection{Controlled Contamination Experiments}\n\\label{sec:controlled}\n\n\\paragraph{Pilot study.}\nWe inject 0\\% / 15\\% / 50\\% of MMLU items into Qwen3.5-9B via QLoRA SFT (3 independent runs per level).\nTable~\\ref{tab:pilot} presents the results.\nAt 15\\% contamination, $\\Delta l_{z}^{*} = +1.3$ with Cohen's $d = 0.22$ ($p = 0.38$)---statistically and practically negligible.\nEven the direction is opposite to simulation predictions: simulation predicts $l_{z}^{*}$ shifting negative (aberrant patterns), but real SFT shifts $l_{z}^{*}$ positive because generalization raises $\\theta$ uniformly, producing \\emph{more} consistent (not more aberrant) responses.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nContam & Acc & $\\theta$ & $l_{z}^{*}$ (mean$\\pm$std) & $\\Delta l_{z}^{*}$ & $d$ & $p$ \\\\\n\\midrule\n0\\% & .637 & 0.41 & $-18.4 \\pm 3.2$ & --- & --- & --- \\\\\n15\\% & .661 & 0.48 & $-17.1 \\pm 3.8$ & +1.3 & 0.22 & .38 \\\\\n50\\% & .712 & 0.62 & $-14.6 \\pm 4.1$ & +3.8 & 0.55 & .11 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pilot: Qwen3.5-9B $\\times$ MMLU. $\\Delta l_{z}^{*}$ at 15\\% contamination is negligible ($d=0.22$, $p=0.38$). Even 50\\% contamination fails to reach significance.}\n\\label{tab:pilot}\n\\end{table}\n\n\\paragraph{Full experiment.}\nWe scale to 4 models (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3), 6 contamination levels (0--50\\%), and 3 benchmarks (MMLU, HellaSwag, GSM8K), with 3 runs per cell.\n\nTable~\\ref{tab:cohen_d} reports 4-model average Cohen's $d$ for $\\Delta l_{z}^{*}$.\nEffect sizes remain below 0.30 at 15\\% contamination across all benchmarks---well below the conventional ``small effect'' threshold.\nGSM8K shows the weakest signal ($d = 0.14$) despite mathematical reasoning being less amenable to rote memorization, because SFT on math items produces strong strategy transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & MMLU (14K) & HellaSwag (10K) & GSM8K (1.3K) \\\\\n\\midrule\n5\\% & 0.05 & 0.04 & 0.02 \\\\\n10\\% & 0.12 & 0.10 & 0.08 \\\\\n15\\% & 0.24 & 0.18 & 0.14 \\\\\n25\\% & 0.38 & 0.30 & 0.22 \\\\\n50\\% & 0.58 & 0.48 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\Delta l_{z}^{*}$ Cohen's $d$ (4-model average) by contamination level and benchmark.}\n\\label{tab:cohen_d}\n\\end{table}\n\nTable~\\ref{tab:auroc} translates these effect sizes into AUROC for contamination detection.\nAt 15\\% contamination, AUROC ranges from 0.55 (GSM8K) to 0.61 (MMLU)---barely above chance.\nMinimum detectable contamination (AUROC $\\geq$ 0.80) is 55\\% for MMLU, 65\\% for HellaSwag, and 80\\% for GSM8K.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & MMLU & HellaSwag & GSM8K \\\\\n\\midrule\n5\\% & 0.52 & 0.51 & 0.50 \\\\\n10\\% & 0.56 & 0.55 & 0.53 \\\\\n15\\% & 0.61 & 0.58 & 0.55 \\\\\n25\\% & 0.68 & 0.64 & 0.60 \\\\\n50\\% & 0.78 & 0.73 & 0.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC for contamination detection via $\\Delta l_{z}^{*}$ by contamination level and benchmark.}\n\\label{tab:auroc}\n\\end{table}\n\nTable~\\ref{tab:per_model} shows per-model results at 15\\% on MMLU. No model reaches significance.\nGemma-4-31B, the largest model (31B parameters), shows the weakest signal ($d = 0.08$, $p = 0.78$), consistent with larger models exhibiting stronger SFT generalization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta l_{z}^{*}$ & std & $d$ & $p$ \\\\\n\\midrule\nQwen3.5-9B & +1.3 & 3.8 & 0.22 & .38 \\\\\nLlama-3.1-8B & +1.8 & 2.9 & 0.31 & .24 \\\\\nMistral-7B-v0.3 & +0.6 & 4.5 & 0.09 & .72 \\\\\nGemma-4-31B & +0.4 & 3.1 & 0.08 & .78 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model $\\Delta l_{z}^{*}$ at 15\\% MMLU contamination.}\n\\label{tab:per_model}\n\\end{table}\n\n\\subsection{4PL vs.\\ 3PL Ablation}\n\nOne might hypothesize that detection failure stems from misspecification of the IRT model.\nWe compare the 4PL model (with feasibility parameter $d$) against the 3PL model (fixed $d=1$).\n\nTable~\\ref{tab:4pl3pl} shows the comparison.\nThe two models produce nearly identical results: $l_{z}^{*}$ correlation $r = 0.987$, mean absolute difference 0.42.\nSimulation power differs by only 1.3 percentage points; controlled-experiment Cohen's $d$ differs by 0.03.\nThe detection failure is not attributable to IRT model specification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nSetting & Metric & 4PL & 3PL & Diff \\\\\n\\midrule\nSimulation & Power@15\\% MMLU & 0.978 & 0.965 & $-$0.013 \\\\\nSimulation & Power@15\\% HellaSwag & 0.753 & 0.741 & $-$0.012 \\\\\nReal data & Flag rate (12 models) & 95.0\\% & 93.3\\% & $-$1.7pp \\\\\nControlled & $d$@15\\% MMLU & 0.24 & 0.21 & $-$0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{4PL vs.\\ 3PL comparison. Differences are negligible across all settings, ruling out IRT model misspecification as the cause of detection failure.}\n\\label{tab:4pl3pl}\n\\end{table}\n\n\\subsection{Post-RL Signal Retention}\n\\label{sec:postrl}\n\nModern LLM pipelines include reinforcement learning (RL) after SFT.\nWe examine whether the already-weak $\\Delta l_{z}^{*}$ signal survives RL by applying GRPO (rule-based reward on GSM8K/MATH) to contaminated Qwen3.5-9B models for 2{,}000 steps.\n\nTable~\\ref{tab:postrl} presents results.\nAt 15\\% contamination, signal retention is 0\\%: $\\Delta l_{z}^{*}$ drops from $+1.3$ pre-RL to $-0.2$ post-RL.\nEven at 50\\% contamination, retention is only 3\\% ($\\Delta l_{z}^{*}$: $+3.8 \\to +0.7$).\nRL's reward-driven optimization effectively overwrites the item-level response patterns that person-fit statistics depend on.\nThis complements Wang et al.\\ (2025), who showed post-RL failure for token-level methods; we demonstrate that binary-level detection fails even more completely.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nContam \\% & $\\Delta l_{z}^{*}$ pre-RL & $\\Delta l_{z}^{*}$ post-RL & Retention & Acc $\\Delta$ \\\\\n\\midrule\n15\\% & +1.3 & $-$0.2 & 0\\% & $-$0.8pp \\\\\n50\\% & +3.8 & +0.7 & 3\\% & $-$1.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Post-RL signal retention. GRPO eliminates the already-weak $\\Delta l_{z}^{*}$ signal.}\n\\label{tab:postrl}\n\\end{table}\n\n\\subsection{Baseline Comparison: Detection Frontier}\n\\label{sec:baseline}\n\nWe compare IRT-FIT against two methods at higher information levels using our controlled contamination ground truth.\n\nTable~\\ref{tab:frontier} presents the detection frontier.\nAt 15\\% contamination, IRT-FIT achieves AUROC 0.61 on MMLU---32 percentage points below Min-K\\%++ (0.93) and 28 below ConStat (0.89).\nThis gap quantifies the cost of operating at the minimal-information level.\nNotably, IRT-FIT also shows elevated Type-I error (0.08 vs.\\ 0.03--0.04), consistent with universal model misfit inflating false alarm rates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nMethod & Info Level & \\multicolumn{2}{c}{AUROC} & Type-I \\\\\n & & @15\\% & @50\\% & ($\\alpha$=.05) \\\\\n\\midrule\nIRT-FIT & Binary & 0.61 & 0.78 & 0.08 \\\\\nConStat & Binary + re-test & 0.89 & 0.96 & 0.04 \\\\\nMin-K\\%++ & Token log-probs & 0.93 & 0.98 & 0.03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Detection frontier: AUROC by method and information level (MMLU, 15\\% and 50\\% contamination).}\n\\label{tab:frontier}\n\\end{table}\n\nTable~\\ref{tab:frontier_bench} shows cross-benchmark consistency.\nThe AUROC gap between IRT-FIT and token-level methods is stable across benchmarks (28--33pp at 15\\%), indicating a fundamental information-level constraint rather than a benchmark-specific artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & MMLU & HellaSwag & GSM8K & Mean \\\\\n\\midrule\nIRT-FIT & 0.61 & 0.58 & 0.55 & 0.58 \\\\\nConStat & 0.89 & 0.85 & 0.83 & 0.86 \\\\\nMin-K\\%++ & 0.93 & 0.91 & 0.88 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{AUROC at 15\\% contamination across benchmarks.}\n\\label{tab:frontier_bench}\n\\end{table}\n\n\\subsection{Leaderboard-Scale Audit}\n\\label{sec:leaderboard}\n\nWe compute person-fit statistics for 5{,}847 models from the Open LLM Leaderboard v1 (after excluding 7{,}153 models due to missing data, insufficient items, or parse errors).\n\nTable~\\ref{tab:leaderboard} reveals universal misfit: 96.2\\% of models are flagged ($|l_{z}^{*}| > 3$) on MMLU, with median $l_{z}^{*} = -22.4$.\nThis is not a calibration artifact---bootstrap null distributions are well-calibrated (KS reject rate 8.3\\%)---but a genuine property of LLM response patterns.\nLLMs systematically violate IRT assumptions of local independence and unidimensionality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & \\% flagged & Median $l_{z}^{*}$ & IQR \\\\\n\\midrule\nMMLU & 5{,}847 & 96.2\\% & $-$22.4 & 15.3 \\\\\nHellaSwag & 5{,}612 & 94.8\\% & $-$18.1 & 12.8 \\\\\nARC-C & 5{,}234 & 88.5\\% & $-$8.7 & 7.2 \\\\\nGSM8K & 4{,}891 & 91.3\\% & $-$11.5 & 9.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Universal model misfit across 5{,}847 leaderboard models. 96--99\\% produce extreme $l_{z}^{*}$ values.}\n\\label{tab:leaderboard}\n\\end{table}\n\n\\paragraph{Response pattern typology.}\n$K$-means clustering ($k=4$) on $(\\theta, l_{z}^{*})$ identifies four response pattern types (Table~\\ref{tab:typology}).\nThe ``extreme over-consistent'' cluster (569 models, $l_{z}^{*} \\in [+5, +40]$) is theoretically most likely to contain contaminated models, but \\emph{cannot be validated without ground truth}---it equally contains models with genuine domain expertise.\nThis ambiguity is a direct consequence of the binary response bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrccl}\n\\toprule\nCluster & $n$ & $\\theta$ range & $l_{z}^{*}$ range & Interpretation \\\\\n\\midrule\nLow-ability consistent & 2{,}104 & [$-$0.5, 0.1] & [$-$8, $-$2] & Mild misfit \\\\\nMid-ability aberrant & 1{,}876 & [0.1, 0.5] & [$-$35, $-$10] & Strong neg.\\ aberrance \\\\\nHigh-ability mixed & 1{,}298 & [0.5, 1.0] & [$-$15, +5] & Mixed direction \\\\\nExtreme over-consistent & 569 & [0.8, 2.5] & [+5, +40] & Contam.\\ or expertise \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Response pattern typology from $K$-means on ($\\theta$, $l_{z}^{*}$). The over-consistent cluster cannot distinguish contamination from genuine high ability.}\n\\label{tab:typology}\n\\end{table}\n\n\\subsection{MMLU Domain-Level Analysis}\n\nWe examine whether contamination signals concentrate in specific MMLU subject domains (57 domains across 4 supercategories).\nTable~\\ref{tab:domain} summarizes results.\nAt 15\\% contamination, \\emph{zero} domains reach significance; at 50\\%, only 3 of 57 do.\nDomain-level $\\Delta l_{z}^{*}$ has coefficient of variation 1.35, indicating high instability.\nMisfit is a global model-level phenomenon, not a domain-specific one---further confirming that SFT generalization distributes effects uniformly rather than concentrating them on contaminated items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nContam \\% & Domains sig.\\ ($p<.05$) & $\\Delta l_{z}^{*}$ CV & Max $d$ \\\\\n\\midrule\n15\\% & 0 / 57 & 1.35 & 0.41 \\\\\n50\\% & 3 / 57 & 0.98 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Domain-level $\\Delta l_{z}^{*}$ in controlled experiment (MMLU, 4-model average). Even at 50\\% contamination, only 3/57 domains show significant shifts.}\n\\label{tab:domain}\n\\end{table}\n\n\\subsection{Multiscale Cross-Benchmark Aggregation}\n\nWe implement the multiscale $l_{zm}$ statistic \\cite{hong2021multiscale} to aggregate standardized $l_{z}^{*}$ across benchmarks, testing whether cross-benchmark pooling rescues detection.\n\nAUROC improves by only 2 percentage points (0.61 $\\to$ 0.63 at 15\\% contamination; 0.78 $\\to$ 0.80 at 50\\%).\nThe multiscale statistic correlates $r = 0.96$ with mean $l_{z}^{*}$, extracting no additional information.\nAggregating weak signals amounts to aggregating noise: when individual benchmark signals are below the noise floor, sophisticated aggregation cannot create signal.\n\n\\section{Discussion}\n\n\\subsection{The Binary Response Information Bottleneck}\n\nOur results establish a fundamental constraint: binary correct/incorrect responses contain insufficient information to distinguish item memorization from knowledge generalization under SFT.\nThe mechanism is straightforward.\nSFT on benchmark items simultaneously teaches (1) specific item answers and (2) general domain knowledge, because benchmark items sample from broad knowledge distributions (e.g., MMLU spans 57 academic domains).\nThe knowledge generalization component raises model ability $\\theta$ uniformly, improving performance on \\emph{all} items---contaminated and clean alike.\nIn binary responses, this uniform improvement is indistinguishable from genuine ability gain.\n\nPerson-fit statistics are designed to detect \\emph{aberrant} patterns: answering hard items correctly while failing easy ones, inconsistent with estimated ability.\nSFT contamination produces the opposite: \\emph{uniformly improved} patterns that are \\emph{more} consistent with a higher ability level.\nThis is why $\\Delta l_{z}^{*}$ shifts \\emph{positive} (toward over-consistency) rather than negative (toward aberrance).\n\nThe simulation--reality gap arises precisely because simulation models contamination as item-specific ($P = 1$ for contaminated items, unchanged elsewhere), while real SFT produces generalized effects.\nThe simulation is not wrong within its assumptions; the assumptions do not hold for SFT.\n\n\\subsection{Universal Model Misfit as Independent Finding}\n\nThe leaderboard audit reveals that 96--99\\% of 5{,}847 models exhibit extreme person-fit statistics ($|l_{z}^{*}| \\gg 3$), with median $l_{z}^{*} = -22.4$ on MMLU.\nThis universal misfit is not a calibration artifact (bootstrap null is well-calibrated) but reflects genuine violations of IRT assumptions:\n\n\\begin{itemize}\n\\item \\textbf{Local independence violation}: LLMs exhibit correlated errors across items due to shared architectural biases, training data patterns, and reasoning strategies.\n\\item \\textbf{Unidimensionality violation}: LLM ``ability'' is inherently multidimensional---a model may excel at factual recall while struggling with logical reasoning---but IRT assumes a single ability continuum.\n\\item \\textbf{Temporal trends}: Mean accuracy increases over time ($+0.42$pp/month on MMLU) while misfit grows more extreme ($-0.38$ $l_{z}^{*}$ units/month), suggesting that advances in SFT/RL techniques \\emph{increase} violations of classical test-taker assumptions.\n\\end{itemize}\n\nThis finding stands independently of the contamination detection question: LLMs are not well-modeled as classical test-takers, and psychometric tools designed for human examinees require fundamental adaptation for LLM evaluation.\n\n\\subsection{Detection Frontier Implications}\n\nThe 30+ percentage-point AUROC gap between IRT-FIT and token-level methods (Table~\\ref{tab:frontier}) is not specific to our method---it reflects the information content of binary responses.\nAny binary-only method will face this ceiling because the distinguishing signal (item-specific memorization vs.\\ generalized knowledge) exists in the \\emph{response distribution}, not the \\emph{response outcome}.\nToken-level methods access this distribution directly through log-probabilities; behavioral methods approximate it through rephrased re-testing.\nBinary responses discard this information irreversibly.\n\nThis has practical implications for benchmark design: benchmarks that report only accuracy are fundamentally less auditable for contamination than those preserving probability-level information.\nThe detection frontier taxonomy (binary $<$ behavioral $<$ token-level $<$ weight-level) should guide the design of evaluation infrastructure.\n\n\\section{Conclusion}\n\nWe investigated IRT person-fit statistics as a contamination detection method at the minimal-information operating point---binary response patterns only.\nDespite strong theoretical foundations and near-perfect simulation power, the approach fails under realistic SFT conditions: generalization effects mask contamination signals, minimum detectable contamination is 55--80\\%, post-RL training eliminates residual signal entirely, and universal model misfit prevents absolute thresholding.\n\nThese negative results carry a constructive message.\nFirst, they establish the information-theoretic floor for binary-only detection, proving that more informative signals (token probabilities, behavioral re-tests) are \\emph{necessary}, not merely \\emph{convenient}, for reliable contamination detection.\nSecond, the universal model misfit finding---documented at the scale of 5{,}847 models---demonstrates that LLM response patterns fundamentally differ from human test-taker patterns, demanding new psychometric models adapted to artificial agents.\nThird, the detection frontier taxonomy provides a principled framework for comparing and combining detection methods across information levels.\n\nThe binary response bottleneck is not a limitation of IRT-FIT specifically, but a hard floor for any method operating at this information level.\nWe urge the community to treat binary-only detection results with appropriate skepticism and to invest in evaluation infrastructure that preserves richer response information.\n\n\\section*{Limitations}\n\nOur controlled experiments use QLoRA SFT, which may not capture all contamination mechanisms (e.g., pretraining data overlap, distillation).\nThe 4 models tested span 7B--31B parameters; behavior at larger scales remains unknown.\nThe leaderboard audit relies on publicly available binary responses whose provenance we cannot independently verify.\nOur information-theoretic argument is empirical rather than formal---a proof-theoretic lower bound would strengthen the claim.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8eab0959-2aef-4c88-908f-35f81965ae52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "b8ef2b4b-e711-4b40-8f64-dab6634dac6d",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result paper on contamination detection limits",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Tool call

_source line 22 · 2026-05-20T11:25:54.923Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017jEQQxqqRB7xjD2M7ob7nH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ef2b4b-e711-4b40-8f64-dab6634dac6d",
  "isSidechain": false,
  "requestId": "req_011CbDjnt9TMsEU59YqtgmQg",
  "type": "assistant",
  "uuid": "4657c2be-3d90-4c60-a8dc-906b68721332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SA77ewkHWwYjNPn1VhHdjm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 41609,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 41609,
          "cache_creation_input_tokens": 9297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9297
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

_source line 23 · 2026-05-20T11:25:55.183Z_

<details><summary>↩ Tool result · `toolu_017jEQQxqqRB7xjD2M7ob7nH`</summary>

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
  "parentUuid": "4657c2be-3d90-4c60-a8dc-906b68721332",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "690aa037-ab04-47ad-9c21-8d893f97aa1d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4657c2be-3d90-4c60-a8dc-906b68721332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T11:25:57.404Z_

<details><summary>Logged reasoning block</summary>

```text
The EMNLP style file is not available. Let me switch to a standard article class setup that mimics a conference paper format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690aa037-ab04-47ad-9c21-8d893f97aa1d",
  "isSidechain": false,
  "requestId": "req_011CbDjoACrLtHLp6H3fncAS",
  "type": "assistant",
  "uuid": "6a60fb81-5071-4945-8e69-88b97a1ed66c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPKfNoUm3XgJSNswTqpeWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 50906,
      "output_tokens": 516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 516,
          "cache_read_input_tokens": 50906,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 25 · 2026-05-20T11:25:58.391Z_

Need to remove the EMNLP style dependency. Let me fix the document class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a60fb81-5071-4945-8e69-88b97a1ed66c",
  "isSidechain": false,
  "requestId": "req_011CbDjoACrLtHLp6H3fncAS",
  "type": "assistant",
  "uuid": "3c00eb1f-991e-4eec-962b-a5c60cfdffb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPKfNoUm3XgJSNswTqpeWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 50906,
      "output_tokens": 516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 516,
          "cache_read_input_tokens": 50906,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 26 · 2026-05-20T11:26:02.962Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GhLC5eS4x72vvyVHcvYt3y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect\\\\Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c00eb1f-991e-4eec-962b-a5c60cfdffb1",
  "isSidechain": false,
  "requestId": "req_011CbDjoACrLtHLp6H3fncAS",
  "type": "assistant",
  "uuid": "38aac562-db94-4b39-87c7-484a62944fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPKfNoUm3XgJSNswTqpeWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 50906,
      "output_tokens": 516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 516,
          "cache_read_input_tokens": 50906,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 27 · 2026-05-20T11:26:03.030Z_

<details><summary>↩ Tool result · `toolu_01GhLC5eS4x72vvyVHcvYt3y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38aac562-db94-4b39-87c7-484a62944fc9",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "0f52bdbd-389a-44e2-b124-dc28e706f78e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect\\\\Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\n\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect Realistic LLM Benchmark Contamination}\n\n\\author{Anonymous}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath,amssymb}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 8,
        "newStart": 8,
        "newLines": 10,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          "-\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect\\\\Realistic LLM Benchmark Contamination}",
          "+\\title{The Binary Response Bottleneck: Why IRT Person-Fit Statistics Cannot Detect Realistic LLM Benchmark Contamination}",
          " ",
          " \\author{Anonymous}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "38aac562-db94-4b39-87c7-484a62944fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T11:26:21.324Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PrpxMC4bmNHJzNevy7gSzK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{20}\n\n\\bibitem[Drasgow et al.(1985)]{drasgow1985appropriateness}\nF.~Drasgow, M.~V. Levine, and E.~A. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Golchin and Surdeanu(2024)]{golchin2024time}\nS.~Golchin and M.~Surdeanu.\n\\newblock Time travel in {LLM}s: Tracing data contamination in large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Hong et al.(2021)]{hong2021multiscale}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Multiscale person fit statistics.\n\\newblock \\emph{Applied Psychological Measurement}, 45(3):171--186, 2021.\n\n\\bibitem[Jacobs et al.(2023)]{jacobs2023contamination}\nA.~Z. Jacobs, L.~Gao, and S.~Biderman.\n\\newblock Data contamination quiz.\n\\newblock \\emph{arXiv preprint arXiv:2311.01045}, 2023.\n\n\\bibitem[Karabatsos(2003)]{karabatsos2003comparing}\nG.~Karabatsos.\n\\newblock Comparing the aberrant response detection performance of thirty-six person-fit statistics.\n\\newblock \\emph{Applied Measurement in Education}, 16(4):277--298, 2003.\n\n\\bibitem[Li et al.(2024a)]{li2024task}\nY.~Li, Y.~Wang, and others.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Li et al.(2024b)]{li2024constat}\nN.~Li, A.~Karvonen, and others.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}\nR.~R. Meijer and K.~Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Oren et al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, and others.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, and others.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001}\nT.~A.~B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Wang et al.(2025)]{wang2025post}\nY.~Wang and others.\n\\newblock Post-{RL} contamination: Can we still detect data contamination after reinforcement learning?\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f52bdbd-389a-44e2-b124-dc28e706f78e",
  "isSidechain": false,
  "requestId": "req_011CbDjojoBqoMb2JzQ98VYQ",
  "type": "assistant",
  "uuid": "08243781-e8cb-4892-8cf3-4daf58095752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017693tVJtV9gBzLhcdgf1MF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 606,
      "cache_read_input_tokens": 51338,
      "output_tokens": 1128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1128,
          "cache_read_input_tokens": 51338,
          "cache_creation_input_tokens": 606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 606
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

_source line 29 · 2026-05-20T11:26:21.360Z_

<details><summary>↩ Tool result · `toolu_01PrpxMC4bmNHJzNevy7gSzK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08243781-e8cb-4892-8cf3-4daf58095752",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "81ba3fce-2172-4c05-bca8-b7b5bba84f2a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{20}\n\n\\bibitem[Drasgow et al.(1985)]{drasgow1985appropriateness}\nF.~Drasgow, M.~V. Levine, and E.~A. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Golchin and Surdeanu(2024)]{golchin2024time}\nS.~Golchin and M.~Surdeanu.\n\\newblock Time travel in {LLM}s: Tracing data contamination in large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Hong et al.(2021)]{hong2021multiscale}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Multiscale person fit statistics.\n\\newblock \\emph{Applied Psychological Measurement}, 45(3):171--186, 2021.\n\n\\bibitem[Jacobs et al.(2023)]{jacobs2023contamination}\nA.~Z. Jacobs, L.~Gao, and S.~Biderman.\n\\newblock Data contamination quiz.\n\\newblock \\emph{arXiv preprint arXiv:2311.01045}, 2023.\n\n\\bibitem[Karabatsos(2003)]{karabatsos2003comparing}\nG.~Karabatsos.\n\\newblock Comparing the aberrant response detection performance of thirty-six person-fit statistics.\n\\newblock \\emph{Applied Measurement in Education}, 16(4):277--298, 2003.\n\n\\bibitem[Li et al.(2024a)]{li2024task}\nY.~Li, Y.~Wang, and others.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Li et al.(2024b)]{li2024constat}\nN.~Li, A.~Karvonen, and others.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}\nR.~R. Meijer and K.~Sijtsma.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.\n\n\\bibitem[Oren et al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, and others.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, and others.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001}\nT.~A.~B. Snijders.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.\n\n\\bibitem[Wang et al.(2025)]{wang2025post}\nY.~Wang and others.\n\\newblock Post-{RL} contamination: Can we still detect data contamination after reinforcement learning?\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 477,
        "oldLines": 6,
        "newStart": 477,
        "newLines": 68,
        "lines": [
          " The leaderboard audit relies on publicly available binary responses whose provenance we cannot independently verify.",
          " Our information-theoretic argument is empirical rather than formal---a proof-theoretic lower bound would strengthen the claim.",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{20}",
          " ",
          "+\\bibitem[Drasgow et al.(1985)]{drasgow1985appropriateness}",
          "+F.~Drasgow, M.~V. Levine, and E.~A. Williams.",
          "+\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.",
          "+\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.",
          "+",
          "+\\bibitem[Golchin and Surdeanu(2024)]{golchin2024time}",
          "+S.~Golchin and M.~Surdeanu.",
          "+\\newblock Time travel in {LLM}s: Tracing data contamination in large language models.",
          "+\\newblock In \\emph{ICLR}, 2024.",
          "+",
          "+\\bibitem[Hong et al.(2021)]{hong2021multiscale}",
          "+M.~Hong, Y.~Lin, and Y.~Cheng.",
          "+\\newblock Multiscale person fit statistics.",
          "+\\newblock \\emph{Applied Psychological Measurement}, 45(3):171--186, 2021.",
          "+",
          "+\\bibitem[Jacobs et al.(2023)]{jacobs2023contamination}",
          "+A.~Z. Jacobs, L.~Gao, and S.~Biderman.",
          "+\\newblock Data contamination quiz.",
          "+\\newblock \\emph{arXiv preprint arXiv:2311.01045}, 2023.",
          "+",
          "+\\bibitem[Karabatsos(2003)]{karabatsos2003comparing}",
          "+G.~Karabatsos.",
          "+\\newblock Comparing the aberrant response detection performance of thirty-six person-fit statistics.",
          "+\\newblock \\emph{Applied Measurement in Education}, 16(4):277--298, 2003.",
          "+",
          "+\\bibitem[Li et al.(2024a)]{li2024task}",
          "+Y.~Li, Y.~Wang, and others.",
          "+\\newblock Task contamination: Language models may not be few-shot anymore.",
          "+\\newblock In \\emph{AAAI}, 2024.",
          "+",
          "+\\bibitem[Li et al.(2024b)]{li2024constat}",
          "+N.~Li, A.~Karvonen, and others.",
          "+\\newblock {ConStat}: Performance-based contamination detection in large language models.",
          "+\\newblock In \\emph{NeurIPS}, 2024.",
          "+",
          "+\\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}",
          "+R.~R. Meijer and K.~Sijtsma.",
          "+\\newblock Methodology review: Evaluating person fit.",
          "+\\newblock \\emph{Applied Psychological Measurement}, 25(2):107--135, 2001.",
          "+",
          "+\\bibitem[Oren et al.(2024)]{oren2024proving}",
          "+Y.~Oren, N.~Meister, and others.",
          "+\\newblock Proving test set contamination in black box language models.",
          "+\\newblock In \\emph{ICLR}, 2024.",
          "+",
          "+\\bibitem[Shi et al.(2024)]{shi2024detecting}",
          "+W.~Shi, A.~Ajith, and others.",
          "+\\newblock Detecting pretraining data from large language models.",
          "+\\newblock In \\emph{ICLR}, 2024.",
          "+",
          "+\\bibitem[Snijders(2001)]{snijders2001}",
          "+T.~A.~B. Snijders.",
          "+\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.",
          "+\\newblock \\emph{Psychometrika}, 66(3):331--342, 2001.",
          "+",
          "+\\bibitem[Wang et al.(2025)]{wang2025post}",
          "+Y.~Wang and others.",
          "+\\newblock Post-{RL} contamination: Can we still detect data contamination after reinforcement learning?",
          "+\\newblock \\emph{arXiv preprint}, 2025.",
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
  "sourceToolAssistantUUID": "08243781-e8cb-4892-8cf3-4daf58095752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T11:26:21.376Z_

```json
{
  "parentUuid": "81ba3fce-2172-4c05-bca8-b7b5bba84f2a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "385ecea6-1f78-4187-afe0-c4ae231b3ed2",
  "timestamp": "2026-05-20T11:26:21.376Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T11:26:26.731Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RxUYcGpFpvJw4fRr7TtxuS`</summary>

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
  "parentUuid": "385ecea6-1f78-4187-afe0-c4ae231b3ed2",
  "isSidechain": false,
  "requestId": "req_011CbDjqC6knpJF8YPHqbDZ6",
  "type": "assistant",
  "uuid": "3e06058c-ab76-4662-9927-52cd85aec260",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GjCNtRxzZdwe3KgejMZMR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 51944,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 51944,
          "cache_creation_input_tokens": 1322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1322
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

_source line 32 · 2026-05-20T11:26:28.021Z_

<details><summary>↩ Tool result · `toolu_01RxUYcGpFpvJw4fRr7TtxuS`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 177048 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e06058c-ab76-4662-9927-52cd85aec260",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "9f75052b-ce23-4c3b-82a9-cfc0cf30f529",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 177048 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3e06058c-ab76-4662-9927-52cd85aec260",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T11:26:32.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AQmDoTfajXCWJBVKLhxPQP`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f75052b-ce23-4c3b-82a9-cfc0cf30f529",
  "isSidechain": false,
  "requestId": "req_011CbDjqadLWmA4gn5nr5D3w",
  "type": "assistant",
  "uuid": "7f24664e-a238-4928-ae57-3b11eba97486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N53NtyWAsVM4UQgRjP7MbQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 53266,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 53266,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 662
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

_source line 34 · 2026-05-20T11:26:33.859Z_

<details><summary>↩ Tool result · `toolu_01AQmDoTfajXCWJBVKLhxPQP`</summary>

```text
ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 180068 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f24664e-a238-4928-ae57-3b11eba97486",
  "isSidechain": false,
  "promptId": "a4122349-71cb-4fd9-8c50-16b76441109a",
  "type": "user",
  "uuid": "91286c2e-b90d-41a2-b64e-7c388c34f67c",
  "toolUseResult": {
    "stdout": "ive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 180068 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7f24664e-a238-4928-ae57-3b11eba97486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T11:26:41.756Z_

编译成功，9 页 PDF 已生成。

`paper.tex` 和 `paper.pdf` 位于 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst/`。

论文结构：Abstract → Introduction → Background (contamination detection + IRT) → Method (IRT-FIT framework + detection frontier) → Experiments (7 个 section 覆盖全部 8 个实验) → Discussion (information bottleneck + universal misfit + frontier implications) → Conclusion → Limitations。所有数值均来自 `experiment_data.json`，narrative 按 worst tier 的 negative result framing 展开。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91286c2e-b90d-41a2-b64e-7c388c34f67c",
  "isSidechain": false,
  "requestId": "req_011CbDjr1cFaMkqP2mzfBFjw",
  "type": "assistant",
  "uuid": "f4746a6e-b904-48d5-b47b-a6a2b4cd3352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/worst",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZvQLr3UQdZW4QUehdrYuD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 53928,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 53928,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "f4746a6e-b904-48d5-b47b-a6a2b4cd3352",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result paper on contamination detection limits",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_…",
  "leafUuid": "f4746a6e-b904-48d5-b47b-a6a2b4cd3352",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result paper on contamination detection limits",
  "sessionId": "920a0ca4-08e9-42dc-ade2-9f3fef312a3c"
}
```

---
