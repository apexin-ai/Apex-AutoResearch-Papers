# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/57971aef-fe55-48e4-84c1-753372b1ed10.jsonl`
- **Structured JSON:** [`a0b0090805e33ccb8161.json`](../../sessions/a0/a0b0090805e33ccb8161.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:57:33.976Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:57:33.976Z",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Reframe away from 'HS beats text' toward one of two angles, both still targeting EMNLP Main: (A) **Negative-results-first framing**: 'We systematically evaluate 7 detection methods across 4 reasoning models and find that none achieves deployment-ready performance. The best approach (temporal HS probes) still has 39-62% safe FPR. We identify layer selection bias as a critical confounder and provide a sensitivity analysis framework.' This positions the paper as a cautionary benchmark. (B) **Methodology-first framing**: 'We discover that a commonly used layer selection metric systematically biases hidden-state evaluations, producing false negatives at scale. We demonstrate this across 4 models and 5 metrics, show it reverses published conclusions, and propose a multi-metric audit protocol.' This makes layer selection the headline and HS-vs-text becomes supporting evidence. Either angle requires: toning down deployment language, foregrounding limitations honestly, positioning as 'the field needs this evaluation before building on shaky foundations.' Add cost-benefit analysis (HS access cost vs marginal gain over text) to preempt the engineering-cost reviewer.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T21:57:33.980Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:57:33.980Z",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-21T21:57:34.013Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Reframe away from 'HS beats text' toward one of two angles, both still targeting EMNLP Main: (A) **Negative-results-first framing**: 'We systematically evaluate 7 detection methods across 4 reasoning models and find that none achieves deployment-ready performance. The best approach (temporal HS probes) still has 39-62% safe FPR. We identify layer selection bias as a critical confounder and provide a sensitivity analysis framework.' This positions the paper as a cautionary benchmark. (B) **Methodology-first framing**: 'We discover that a commonly used layer selection metric systematically biases hidden-state evaluations, producing false negatives at scale. We demonstrate this across 4 models and 5 metrics, show it reverses published conclusions, and propose a multi-metric audit protocol.' This makes layer selection the headline and HS-vs-text becomes supporting evidence. Either angle requires: toning down deployment language, foregrounding limitations honestly, positioning as 'the field needs this evaluation before building on shaky foundations.' Add cost-benefit analysis (HS access cost vs marginal gain over text) to preempt the engineering-cost reviewer.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "9fe6460c-2db5-40fd-8ed5-3507741cf122",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:57:34.012Z_

```json
{
  "parentUuid": "9fe6460c-2db5-40fd-8ed5-3507741cf122",
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
  "uuid": "4054d19b-6161-44de-9c71-64ffc8f8c4fd",
  "timestamp": "2026-05-21T21:57:34.012Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:57:34.013Z_

```json
{
  "parentUuid": "4054d19b-6161-44de-9c71-64ffc8f8c4fd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ce428e68-e06f-4f95-ae74-654ee7de853b",
  "timestamp": "2026-05-21T21:57:34.013Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
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
  "aiTitle": "Generate simulated worst-tier research paper",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Assistant

_source line 7 · 2026-05-21T21:57:36.601Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce428e68-e06f-4f95-ae74-654ee7de853b",
  "isSidechain": false,
  "requestId": "req_011CbGTmm4vkEcPA195dRc9G",
  "type": "assistant",
  "uuid": "1d0a3be5-9503-4d73-8939-a001e28ecd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149gDrdjEPeWbAqvfByzYsv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13286
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

_source line 8 · 2026-05-21T21:57:37.563Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Uex2LXSCP5smEhgQbEpBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d0a3be5-9503-4d73-8939-a001e28ecd63",
  "isSidechain": false,
  "requestId": "req_011CbGTmm4vkEcPA195dRc9G",
  "type": "assistant",
  "uuid": "acd0479a-9ea3-4274-98a0-0f2b60ea51ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149gDrdjEPeWbAqvfByzYsv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13286
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

_source line 9 · 2026-05-21T21:57:37.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UsfMXdnWQTQJALm77NqeCi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acd0479a-9ea3-4274-98a0-0f2b60ea51ff",
  "isSidechain": false,
  "requestId": "req_011CbGTmm4vkEcPA195dRc9G",
  "type": "assistant",
  "uuid": "f087eccf-f8f2-46e9-8e05-3e07be3f7328",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149gDrdjEPeWbAqvfByzYsv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13286,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13286
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

_source line 10 · 2026-05-21T21:57:37.896Z_

<details><summary>↩ Tool result · `toolu_016Uex2LXSCP5smEhgQbEpBa`</summary>

```text
1	[
2	  {
3	    "name": "Cross-architecture layer sweep + static probe (r1-32b & QwQ-32B)",
4	    "description": "Full 64-layer sweep on DeepSeek-R1-Distill-Qwen-32B and QwQ-32B. Extract hidden states at all layers, evaluate static LR probes per layer under multiple selection metrics. Includes discovery of layer selection bias (bal_acc × crossing_rate → shallow layers).\n",
5	    "results": {
6	      "r1_32b_biased_layer": 10,
7	      "r1_32b_biased_layer_depth_pct": 15.6,
8	      "r1_32b_corrected_layer": 63,
9	      "r1_32b_corrected_layer_depth_pct": 98.4,
10	      "r1_32b_l10_bal_acc": 0.718,
11	      "r1_32b_l63_bal_acc_w1": 0.826,
12	      "r1_32b_n_test": 20,
13	      "r1_32b_l63_precision_w1": 0.603,
14	      "r1_32b_l63_fpr_w1": 0.235,
15	      "qwq_32b_biased_layer": 2,
16	      "qwq_32b_biased_layer_depth_pct": 3.1,
17	      "qwq_32b_corrected_layer": 60,
18	      "qwq_32b_corrected_layer_depth_pct": 93.8,
19	      "qwq_32b_l2_bal_acc": 0.73,
20	      "qwq_32b_l60_bal_acc_w3": 0.74,
21	      "qwq_32b_n_test": "19-20",
22	      "qwq_32b_l60_precision_w3": 0.578,
23	      "qwq_32b_l60_fpr_w3": 0.279,
24	      "layer_selection_bias_discovered": true,
25	      "metrics_tested": 5,
26	      "biased_metric": "bal_acc × crossing_rate",
27	      "loo_cv_dominant_fold_pct": "65-68%"
28	    },
29	    "tables": [
30	      {
31	        "name": "Layer Selection Metric × Model → Selected Layer",
32	        "columns": [
33	          "Metric",
34	          "R1-8B",
35	          "OT-7B",
36	          "QwQ-32B",
37	          "R1-32B"
38	        ],
39	        "rows": [
40	          [
41	            "bal_acc × crossing_rate",
42	            "L0 (0%)",
43	            "L0 (0%)",
44	            "L2 (3%)",
45	            "L10 (16%)"
46	          ],
47	          [
48	            "pure bal_acc",
49	            "L12 (39%)",
50	            "L9 (32%)",
51	            "L30 (47%)",
52	            "L47 (73%)"
53	          ],
54	          [
55	            "precision",
56	            "L16 (52%)",
57	            "L16 (57%)",
58	            "L60 (94%)",
59	            "L63 (98%)"
60	          ],
61	          [
62	            "pre_cp_fpr",
63	            "L16 (52%)",
64	            "L16 (57%)",
65	            "L60 (94%)",
66	            "L63 (98%)"
67	          ],
68	          [
69	            "composite (additive)",
70	            "L16 (52%)",
71	            "L12 (43%)",
72	            "L60 (94%)",
73	            "L63 (98%)"
74	          ]
75	        ]
76	      }
77	    ],
78	    "figures": [],
79	    "analysis": "Layer selection sensitivity is the paper's primary methodological contribution, but worst-tier reviewers rate it insufficient novelty (2.0-2.5). The argument: \"every ML practitioner knows different metrics select different hyperparameters. Showing this for layer selection is an observation, not a method. There's no proposed algorithm to automatically resolve the disagreement — just 'try more metrics,' which is standard practice.\"\n\n\nLayer sweep reveals a genuine methodological finding (biased metric selects shallow layers), and corrected layers do show HS advantage. However, worst-tier reviewers dismiss this: (1) \"Finding that one composite metric is bad is trivially expected — practitioners routinely try multiple metrics. This is hyperparameter tuning, not a contribution.\" (2) n=19-20 test traces for 32B models mean bootstrap CIs are wide. MDE analysis shows R1-32B residualized gap (+1.9pp) is far below the 11.2pp MDE at 80% power — the NS result for position-mediated HS advantage is a power limitation, not evidence. Reviewers note: \"you can't claim the advantage is 'real but position-mediated' when you're underpowered to detect the non-positional component.\" (3) The corrected layers (L60/L63, >93% depth) are so deep they're essentially the output layer — reviewer asks: \"are you just detecting output-token semantics via a different pathway?\"\n"
80	  },
81	  {
82	    "name": "Cross-architecture temporal window evaluation (32B)",
83	    "description": "Temporal LR at multiple window sizes on R1-32B (L63) and QwQ-32B (L60). Evaluate whether temporal context universally improves probe accuracy across 32B models.\n",
84	    "results": {
85	      "r1_32b_l63_w1_bal_acc": 0.826,
86	      "r1_32b_l63_w1_precision": 0.603,
87	      "r1_32b_l63_w1_coverage": 0.25,
88	      "r1_32b_l63_w3_bal_acc": 0.754,
89	      "r1_32b_l63_w5_bal_acc": 0.741,
90	      "r1_32b_l63_w10_bal_acc": 0.737,
91	      "r1_32b_l63_w15_bal_acc": 0.721,
92	      "r1_32b_temporal_trend": "DECREASING with W (W=1 best, -10.5pp by W=15)",
93	      "r1_32b_dimensionality_issue": "51200 × W features for n=20 → massive overfitting at W≥3",
94	      "qwq_32b_l60_w1_bal_acc": 0.74,
95	      "qwq_32b_l60_w3_bal_acc": 0.74,
96	      "qwq_32b_l60_w5_bal_acc": 0.742,
97	      "qwq_32b_l60_w15_bal_acc": 0.731,
98	      "qwq_32b_temporal_trend": "flat to slightly decreasing",
99	      "qwq_32b_best_w": 5,
100	      "text_temporal_universal_improvement": true,
101	      "hs_temporal_improvement_3_of_4": true,
102	      "hs_temporal_exception": "OT-7B HS peaks W=3, declines at larger W; R1-32B only W=1 significant"
103	    },
104	    "tables": [
105	      {
106	        "name": "Temporal Window Effect on 32B Models (HS probes, corrected layers)",
107	        "columns": [
108	          "Model",
109	          "Layer",
110	          "W=1",
111	          "W=3",
112	          "W=5",
113	          "W=10",
114	          "W=15",
115	          "Trend"
116	        ],
117	        "rows": [
118	          [
119	            "R1-32B",
120	            "L63",
121	            "0.826*",
122	            "0.754",
123	            "0.741",
124	            "0.737",
125	            "0.721",
126	            "↓ declining"
127	          ],
128	          [
129	            "QwQ-32B",
130	            "L60",
131	            "0.740",
132	            "0.740",
133	            "0.742",
134	            "0.735",
135	            "0.731",
136	            "→ flat"
137	          ],
138	          [
139	            "R1-8B",
140	            "L14",
141	            "0.778",
142	            "0.790",
143	            "0.781",
144	            "0.793",
145	            "0.802",
146	            "↑ improving"
147	          ],
148	          [
149	            "OT-7B",
150	            "L16",
151	            "0.663",
152	            "0.688*",
153	            "0.678",
154	            "0.668",
155	            "0.659",
156	            "↑↓ peaks W=3"
157	          ]
158	        ]
159	      }
160	    ],
161	    "figures": [],
162	    "analysis": "Worst-tier reviewers note: \"Temporal context helps universally for text probes (a known result — more context helps NLP classifiers). For HS probes, 2/4 models show non-monotonic or declining trends. The paper's Claim 1 should be 'temporal context helps text probes' — attributing it to HS probes is cherry-picking the models where it works.\"\n\n\nTemporal context shows a split pattern at 32B: QwQ benefits modestly across all W (text and HS), but R1-32B DEGRADES with increasing W because concatenating 51200-dimensional vectors across W>1 windows creates a feature space massively exceeding n=20 training samples. This is not a failure of the temporal hypothesis — it's a sample-size bottleneck. Worst-tier reviewers seize on this: \"R1-32B temporal results are meaningless because you're fitting 102400+ parameters to 20 samples. The W=1 'significance' at L63 survives only because W=1 avoids this problem. Your 'best' result for R1-32B is actually a dimensionality artifact — the only window that avoids overfitting happens to be significant.\" Claim 1 (temporal universally helps) holds for text probes across all 4 models, but for HS probes, 2/4 models have caveats (OT-7B saturation, R1-32B dimensionality). Reviewers frame this as \"temporal improvement is a text-probe finding, not an HS-probe finding.\"\n"
163	  },
164	  {
165	    "name": "Cross-model transfer probes",
166	    "description": "Train probe on one model, test on another. PCA projection for cross-architecture transfer (4096→5120 or vice versa). Tests whether safety commitment encoding is universal.\n",
167	    "results": {
168	      "r1_8b_to_r1_32b_acc": 0.522,
169	      "r1_8b_to_qwq_acc": 0.595,
170	      "r1_32b_to_qwq_acc": 0.673,
171	      "qwq_to_r1_32b_acc": 0.673,
172	      "r1_32b_to_r1_8b_acc": 0.583,
173	      "best_transfer_overall": 0.673,
174	      "chance_baseline": 0.5,
175	      "all_transfers_below_within_model": true,
176	      "within_family_32b_weak_transfer": 0.673,
177	      "cross_family_at_chance": true
178	    },
179	    "tables": [
180	      {
181	        "name": "Cross-Model Transfer Accuracy Matrix",
182	        "columns": [
183	          "Train →",
184	          "R1-8B",
185	          "OT-7B",
186	          "R1-32B",
187	          "QwQ-32B"
188	        ],
189	        "rows": [
190	          [
191	            "R1-8B",
192	            "0.817 (self)",
193	            "—",
194	            "0.522",
195	            "0.595"
196	          ],
197	          [
198	            "OT-7B",
199	            "—",
200	            "0.688 (self)",
201	            "—",
202	            "—"
203	          ],
204	          [
205	            "R1-32B",
206	            "0.583",
207	            "—",
208	            "0.826 (self)",
209	            "0.673"
210	          ],
211	          [
212	            "QwQ-32B",
213	            "—",
214	            "—",
215	            "0.673",
216	            "0.740 (self)"
217	          ]
218	        ]
219	      }
220	    ],
221	    "figures": [],
222	    "analysis": "Complete transfer failure. Worst-tier reviewers conclude: \"The paper claims to study 'safety commitment detection' as a general phenomenon, but the probes are entirely model-specific. This means the method has zero practical scalability — you need labeled data for every model you want to monitor. Combined with the engineering cost of white-box access, the deployment story collapses.\"\n\n\nCross-model transfer fails completely — the best transfer accuracy (67.3% Qwen-family 32B internal) is far below within-model performance and barely above the majority-class baseline. Cross-family transfer (Llama↔Qwen) is at chance. Worst-tier reviewers use this as evidence against the paper: \"Safety encoding is model-specific. This means every new model needs its own probe training with labeled commitment points — a supervision cost the paper downplays. If safety commitment were a universal phenomenon, SOME geometric structure should transfer. The complete failure suggests the probes are learning model-specific artifacts, not a generalizable safety signal.\" This finding is consistent with the selectivity control task (7.5-18.5pp) but reviewers argue selectivity merely shows the probes aren't random — not that they detect genuine safety commitment vs idiosyncratic model behavior.\n"
223	  },
224	  {
225	    "name": "Lead time analysis across models",
226	    "description": "Evaluate HS probe lead time distributions on all 4 models. Compare HS vs text lead times. Lead time = steps between first detection and commitment point.\n",
227	    "results": {
228	      "r1_8b_hs_lead_mean": -0.1,
229	      "r1_8b_hs_lead_note": "HS detects AT commitment, not before",
230	      "r1_8b_text_lead_mean": 10.3,
231	      "r1_8b_text_lead_inflated": "high text lead is artifact of high pre-CP FPR (trigger-happy)",
232	      "ot_7b_hs_lead_mean": 21.6,
233	      "ot_7b_text_lead_mean": 45.5,
234	      "ot_7b_lead_note": "absolute values inflated by long traces (~80 sentences)",
235	      "qwq_32b_hs_lead_mean_range": "-1.2 to +1.9",
236	      "qwq_32b_text_lead_mean_range": "3.7 to 12.3",
237	      "qwq_32b_hs_lead_negative": true,
238	      "qwq_32b_position_baseline_lead": "better than HS",
239	      "r1_32b_hs_lead_mean": "+11.7 to +13.3",
240	      "r1_32b_hs_lead_positive": true,
241	      "r1_32b_coverage_at_significant_w": 0.25,
242	      "r1_32b_lead_caveat": "only 5/20 traces detected at W=1",
243	      "gru_r1_8b_lead": "+4.5 ± 3.0",
244	      "gru_r1_8b_worst_seed": "+0.9"
245	    },
246	    "tables": [
247	      {
248	        "name": "Lead Time Comparison: HS vs Text vs Position",
249	        "columns": [
250	          "Model",
251	          "HS Lead (steps)",
252	          "Text Lead (steps)",
253	          "Position BA",
254	          "HS BA",
255	          "HS > Position?"
256	        ],
257	        "rows": [
258	          [
259	            "R1-8B (W=15)",
260	            "−0.1",
261	            "+10.3†",
262	            "—",
263	            "0.802",
264	            "—"
265	          ],
266	          [
267	            "OT-7B (W=3)",
268	            "+21.6‡",
269	            "+45.5‡",
270	            "—",
271	            "0.688",
272	            "—"
273	          ],
274	          [
275	            "QwQ-32B (W=3)",
276	            "−1.2 to +1.9",
277	            "+3.7 to +12.3",
278	            "0.746",
279	            "0.740",
280	            "No"
281	          ],
282	          [
283	            "R1-32B (W=1)",
284	            "+11.7 to +13.3",
285	            "—",
286	            "0.686",
287	            "0.826",
288	            "Yes (25% cov)"
289	          ]
290	        ]
291	      }
292	    ],
293	    "figures": [],
294	    "analysis": "Worst-tier reviewers identify lead time as the practical dealbreaker: \"The paper claims HS monitoring enables early detection, but 2/4 models show HS detecting LATER than text. The one model with good lead time (R1-32B) detects only 25% of traces. A deployment team would choose text monitoring over HS monitoring for lead time alone, saving the engineering cost of hidden-state extraction.\"\n\n\nLead time results are a mixed bag that worst-tier reviewers weaponize: (1) R1-8B HS lead is effectively zero — HS detects AT commitment, not before. Only GRU achieves modest positive lead (+4.5, worst seed +0.9). Text lead of +10.3 is misleadingly high (artifact of trigger-happy detection with 20.5% pre-CP FPR). (2) QwQ-32B: HS lead time is NEGATIVE (-1.2 to +1.9 steps) while text detects 3.7-12.3 steps earlier. Position baseline (bal_acc=0.746) beats HS (bal_acc=0.740). A reviewer writes: \"for QwQ, just tracking relative position in the trace outperforms hidden-state monitoring — why bother with white-box access?\" (3) R1-32B has excellent HS lead (+13 steps) but only 25% coverage — meaning 15/20 traces are undetected. Reviewer: \"a detector that works on 5 traces is an anecdote, not a system.\" (4) OT-7B lead times are inflated by long traces. Overall: 2/4 models have HS lead ≤ 0, 1/4 has only 25% coverage, and 1/4 has inflated absolute values. No model presents a clean HS lead time story.\n"
295	  },
296	  {
297	    "name": "TrajGuard-style Mahalanobis baseline (all 4 models)",
298	    "description": "Mahalanobis distance on safe-trace covariance across all 4 models. Tests whether geometric distance-based methods (TrajGuard-style) can detect safety commitment.\n",
299	    "results": {
300	      "r1_8b_separation": 0.07,
301	      "ot_7b_separation": 0.03,
302	      "r1_32b_separation": 0.15,
303	      "qwq_32b_separation": 0.2,
304	      "max_separation_any_model": 0.2,
305	      "all_models_fail": true,
306	      "false_alarm_exceeds_tp_all_thresholds": true,
307	      "signal_location": "minor PCA components, not principal directions",
308	      "r1_8b_safe_md": 6.66,
309	      "r1_8b_post_md": 6.73,
310	      "r1_32b_safe_md": 6.73,
311	      "r1_32b_post_md": 6.88,
312	      "qwq_32b_safe_md": 3.22,
313	      "qwq_32b_post_md": 3.42
314	    },
315	    "tables": [
316	      {
317	        "name": "Mahalanobis Distance Separation (4 models)",
318	        "columns": [
319	          "Model",
320	          "Layer",
321	          "Safe MD",
322	          "Post-CP MD",
323	          "Separation",
324	          "FA ≥ TP?"
325	        ],
326	        "rows": [
327	          [
328	            "R1-8B",
329	            "L14",
330	            "6.66",
331	            "6.73",
332	            "+0.07",
333	            "Yes"
334	          ],
335	          [
336	            "OT-7B",
337	            "L16",
338	            "7.68",
339	            "7.71",
340	            "+0.03",
341	            "Yes"
342	          ],
343	          [
344	            "R1-32B",
345	            "L63",
346	            "6.73",
347	            "6.88",
348	            "+0.15",
349	            "Yes"
350	          ],
351	          [
352	            "QwQ-32B",
353	            "L60",
354	            "3.22",
355	            "3.42",
356	            "+0.20",
357	            "Yes"
358	          ]
359	        ]
360	      }
361	    ],
362	    "figures": [],
363	    "analysis": "Universal Mahalanobis failure confirms safety signal is geometrically inaccessible to distance-based methods. But worst-tier reviewers dismiss this: \"Showing Mahalanobis doesn't work is a paragraph in a methods section, not a contribution. The field already knows unsupervised geometric methods struggle with fine-grained behavioral distinctions.\"\n\n\nMahalanobis distance fails on all 4 models (max separation 0.20 on QwQ, FA rate ≥ TP rate at every threshold). The signal lives in minor PCA components, not principal variance directions — Mahalanobis, which weights by inverse covariance, is structurally blind to this geometry. Worst-tier reviewers have mixed reactions: (1) \"Mahalanobis failing is expected — Bolukbasi et al. 2016 and subsequent work showed safety-relevant features are often orthogonal to principal variance. This negative result is predictable, not informative.\" (2) \"You tested one geometric baseline. What about k-NN distance, local outlier factor, or isolation forests? The negative result space is underexplored.\" The finding supports the \"existing methods fail\" claim but reviewers rate it as incremental — failure of one known-limited baseline is not a contribution.\n"
364	  },
365	  {
366	    "name": "Bootstrap confidence intervals + threshold-independent metrics",
367	    "description": "10000 bootstrap resamples on all key metrics across 4 models. Holm-Bonferroni correction. AUROC, precision-recall curves, detection delay CDF.\n",
368	    "results": {
369	      "holm_bonferroni_pass": "12/12",
370	      "r1_8b_precision_delta": "+22.4pp",
371	      "r1_8b_precision_p": "<0.001",
372	      "ot_7b_precision_delta": "+21.9pp",
373	      "ot_7b_precision_p": "<0.001",
374	      "qwq_32b_precision_delta": "+23.6pp",
375	      "qwq_32b_precision_p": "<0.001",
376	      "qwq_32b_fpr_p": 0.004,
377	      "r1_32b_precision_delta": "+15.4pp",
378	      "r1_32b_precision_p": "<0.001",
379	      "r1_32b_fpr_p": 0.007,
380	      "r1_32b_fpr_marginal_note": "p=0.007 passes HB threshold 0.025 but barely",
381	      "marginal_tests_count": 2,
382	      "all_precision_deltas_positive": true,
383	      "precision_range": "+15.4 to +23.6pp",
384	      "r1_32b_ci_width_ba": "~0.15",
385	      "qwq_32b_ci_width_ba": "~0.12",
386	      "r1_8b_ci_width_ba": "~0.06"
387	    },
388	    "tables": [
389	      {
390	        "name": "Holm-Bonferroni Summary (12/12, α=0.05)",
391	        "columns": [
392	          "Rank",
393	          "Model",
394	          "Metric",
395	          "p-value",
396	          "HB Threshold",
397	          "Pass"
398	        ],
399	        "rows": [
400	          [
401	            1,
402	            "R1-8B",
403	            "precision",
404	            "<0.001",
405	            "0.0042",
406	            "✅"
407	          ],
408	          [
409	            2,
410	            "OT-7B",
411	            "bal_acc",
412	            "<0.001",
413	            "0.0045",
414	            "✅"
415	          ],
416	          [
417	            3,
418	            "OT-7B",
419	            "precision",
420	            "<0.001",
421	            "0.0050",
422	            "✅"
423	          ],
424	          [
425	            4,
426	            "OT-7B",
427	            "FPR",
428	            "<0.001",
429	            "0.0056",
430	            "✅"
431	          ],
432	          [
433	            5,
434	            "QwQ",
435	            "bal_acc",
436	            "<0.001",
437	            "0.0063",
438	            "✅"
439	          ],
440	          [
441	            6,
442	            "QwQ",
443	            "precision",
444	            "<0.001",
445	            "0.0071",
446	            "✅"
447	          ],
448	          [
449	            7,
450	            "R1-32B",
451	            "bal_acc",
452	            "<0.001",
453	            "0.0083",
454	            "✅"
455	          ],
456	          [
457	            8,
458	            "R1-32B",
459	            "precision",
460	            "<0.001",
461	            "0.0100",
462	            "✅"
463	          ],
464	          [
465	            9,
466	            "QwQ",
467	            "FPR",
468	            "0.004",
469	            "0.0125",
470	            "✅"
471	          ],
472	          [
473	            10,
474	            "R1-8B",
475	            "bal_acc",
476	            "0.005",
477	            "0.0167",
478	            "✅"
479	          ],
480	          [
481	            11,
482	            "R1-32B",
483	            "FPR",
484	            "0.007",
485	            "0.0250",
486	            "✅"
487	          ],
488	          [
489	            12,
490	            "R1-8B",
491	            "FPR",
492	            "0.044",
493	            "0.0500",
494	            "✅"
495	          ]
496	        ]
497	      }
498	    ],
499	    "figures": [],
500	    "analysis": "Statistical significance is established but reviewers find it insufficient: \"The paper's statistical methodology is sound, but the story it tells is 'HS is significantly better by 15-24pp precision at best-case layer/window selection.' For an EMNLP Main paper, we need either (a) a novel method that achieves these gains, or (b) a surprising finding. Neither: linear probes on hidden states are standard, and it's unsurprising they outperform text embeddings (hidden states are an information superset of text).\"\n\n\nAll 12/12 tests pass Holm-Bonferroni, which is statistically clean. But worst-tier reviewers attack the PRACTICAL significance, not the statistical significance: (1) \"Of course 12/12 pass — you selected the best layer AND the best window per model, then tested. The researcher degrees of freedom (4 models × 64 layers × 7 windows × 5 metrics) dwarf the 12 tests corrected for.\" (2) \"The CIs for 32B models are extremely wide (±0.15 for R1-32B bal_acc). Statistical significance with n=20 means the effect is large, but the PRECISION of the estimate is poor. You know HS is better somewhere between +3pp and +34pp — that's not actionable.\" (3) \"R1-32B FPR p=0.007 and QwQ FPR p=0.004 are the most marginal passing tests. A 10001st bootstrap replicate could flip either.\" (4) \"Holm-Bonferroni corrects for 12 tests, but the true multiplicity (including layer/window selection) is orders of magnitude larger.\"\n"
501	  },
502	  {
503	    "name": "Window size ablation (W=1,3,5,10,15,20,25 on all models)",
504	    "description": "Systematic window size sweep on all 4 models. Characterize precision-coverage tradeoff and identify optimal W per model.\n",
505	    "results": {
506	      "coverage_decreases_with_w_all_models": true,
507	      "precision_increases_with_w_all_models": true,
508	      "fpr_decreases_with_w_all_models": true,
509	      "r1_8b_best_bal_acc_w": 25,
510	      "r1_8b_w25_precision": 0.822,
511	      "r1_8b_w25_coverage": 0.488,
512	      "r1_8b_w25_fpr_step": 0.048,
513	      "r1_32b_best_bal_acc_w": 10,
514	      "r1_32b_w10_precision": 0.609,
515	      "r1_32b_w10_coverage": 0.7,
516	      "r1_32b_w10_fpr_step": 0.234,
517	      "qwq_32b_best_bal_acc_w": 25,
518	      "qwq_32b_w25_precision": 0.618,
519	      "qwq_32b_w25_coverage": 0.579,
520	      "qwq_32b_w25_fpr_step": 0.169,
521	      "ot_7b_hs_peaks_w3": true,
522	      "ot_7b_w3_bal_acc": 0.688,
523	      "ot_7b_w25_bal_acc": 0.659,
524	      "tradeoff_universal": "larger W → higher precision, lower coverage, lower FPR"
525	    },
526	    "tables": [
527	      {
528	        "name": "Precision-Coverage Tradeoff Summary (all 4 models)",
529	        "columns": [
530	          "Model",
531	          "W=1 Prec/Cov",
532	          "W=3 Prec/Cov",
533	          "W=15 Prec/Cov",
534	          "W=25 Prec/Cov"
535	        ],
536	        "rows": [
537	          [
538	            "R1-8B",
539	            "0.693/0.721",
540	            "0.723/0.698",
541	            "0.777/0.512",
542	            "0.822/0.488"
543	          ],
544	          [
545	            "OT-7B",
546	            "—/—",
547	            "0.466/0.532",
548	            "—/—",
549	            "—/—"
550	          ],
551	          [
552	            "R1-32B",
553	            "0.549/0.800",
554	            "0.560/0.800",
555	            "0.591/0.700",
556	            "0.566/0.700"
557	          ],
558	          [
559	            "QwQ-32B",
560	            "0.544/0.789",
561	            "0.565/0.737",
562	            "0.582/0.684",
563	            "0.618/0.579"
564	          ]
565	        ]
566	      }
567	    ],
568	    "figures": [],
569	    "analysis": "The ablation confirms the tradeoff is universal but no operating point achieves both high precision AND high coverage. Worst-tier reviewer: \"Table 3 is the paper's most honest result. At no window size does any model achieve >0.7 precision AND >0.6 coverage simultaneously. This is not a tuning problem — it's a fundamental performance ceiling.\"\n\n\nWindow ablation reveals a clean precision-sensitivity tradeoff that holds across all models. Worst-tier reviewers dismiss this: (1) \"The coverage-decreasing-with-W finding is trivially expected — requiring K=5 consecutive crossings with a larger window means fewer traces reach the threshold. This is a property of the detection criterion K, not an insight about temporal probing.\" (2) \"The optimal W varies by model (W=3 for OT-7B, W=10 for R1-32B, W=25 for QwQ and R1-8B). This means W is another model-specific hyperparameter to tune — combined with layer selection, you need per-model layer AND window tuning. The 'systematic evaluation' framing hides the fact that this is just exhaustive grid search.\" (3) \"At the best W per model, coverage ranges from 49% (R1-8B) to 70% (R1-32B). Missing 30-50% of safety commitment events is not deployment-ready.\"\n"
570	  },
571	  {
572	    "name": "Layer selection ablation (5 metrics × 4 models)",
573	    "description": "Evaluate all layers with temporal probes on 32B models under 5 different selection metrics. Demonstrate crossing_rate bias and metric-dependent layer selection.\n",
574	    "results": {
575	      "crossing_rate_selects_shallow_32b": true,
576	      "pure_bal_acc_selects_middle_32b": true,
577	      "threshold_dependent_select_deep_32b": true,
578	      "qwq_l2_vs_l60_precision_gain": "+11.5pp",
579	      "r1_32b_l10_vs_l63_precision_gain": "+4.1pp",
580	      "loo_cv_stability": "65-68% dominant fold",
581	      "r1_8b_consistent": true,
582	      "ot_7b_varied": true,
583	      "bal_acc_layer_vs_precision_layer_diverge_32b": true,
584	      "qwq_l30_bal_acc": 0.751,
585	      "qwq_l60_bal_acc": 0.71,
586	      "r1_32b_l47_bal_acc": 0.829,
587	      "r1_32b_l63_bal_acc": 0.759,
588	      "ba_optimal_different_from_precision_optimal": true
589	    },
590	    "tables": [
591	      {
592	        "name": "Metric × Model → Selected Layer (with HS-Text precision delta)",
593	        "columns": [
594	          "Metric",
595	          "R1-8B Layer (ΔPrec)",
596	          "OT-7B Layer (ΔPrec)",
597	          "QwQ Layer (ΔPrec)",
598	          "R1-32B Layer (ΔPrec)"
599	        ],
600	        "rows": [
601	          [
602	            "bal_acc × cr",
603	            "L0 (+var)",
604	            "L0 (+var)",
605	            "L2 (+5.8pp NS)",
606	            "L10 (+9.4pp NS)"
607	          ],
608	          [
609	            "pure bal_acc",
610	            "L12 (+17.8pp)",
611	            "L9 (+25.4pp)",
612	            "L30 (+18.0pp)",
613	            "L47 (+13.7pp)"
614	          ],
615	          [
616	            "precision",
617	            "L16 (+22.4pp)",
618	            "L16 (+21.9pp)",
619	            "L60 (+23.6pp)",
620	            "L63 (+15.4pp)"
621	          ],
622	          [
623	            "pre_cp_fpr",
624	            "L16 (−7.4pp)",
625	            "L16 (−17.1pp)",
626	            "L60 (−9.8pp)",
627	            "L63 (−14.6pp)"
628	          ],
629	          [
630	            "composite",
631	            "L16 (+22.4pp)",
632	            "L12 (+var)",
633	            "L60 (+23.6pp)",
634	            "L63 (+15.4pp)"
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "The ablation is thorough but worst-tier reviewers question whether it constitutes a contribution: \"Sensitivity analysis is a sanity check, not a finding. The paper would be better if it had used the right metric from the start and reported results at correct layers — making the sensitivity analysis unnecessary for the paper's core claims.\"\n\n\nThe layer selection ablation reveals a genuine pattern (biased metric → shallow layers → masked HS advantage), but worst-tier reviewers split on its significance: (1) The supportive reading: \"This is a useful observation — researchers using bal_acc × crossing_rate will get misleading results.\" (2) The dismissive reading (dominant in worst tier): \"This is expected behavior of a poorly chosen metric. The composite bal_acc × crossing_rate was never standard — it's the authors' own construction (or a rare one). Showing it's bad doesn't advance the field because nobody was using it.\" (3) The circularity concern: \"You select layers by precision/FPR, then evaluate by precision/FPR. The D044 BA-layer robustness check partially addresses this (16/16 HB pass on BA-selected layers), but the reviewer asks: 'if BA-selected layers also show HS advantage, why not just use BA selection? What's the contribution of the 5-metric comparison?'\" (4) \"LOO-CV stability of 65-68% means 32-35% of folds select a DIFFERENT layer. This is not the 'robust selection' the paper claims.\"\n"
641	  },
642	  {
643	    "name": "16-label taxonomy supervision",
644	    "description": "Train probes with fine-grained safety labels (Type 1/2/3/4 × pre/post) instead of binary commitment. Evaluate whether richer supervision improves detection.\n",
645	    "results": {
646	      "r1_8b_16label_acc": 0.41,
647	      "r1_8b_binary_collapse_acc": 0.825,
648	      "r1_8b_binary_collapse_delta": "+0.8pp",
649	      "ot_7b_16label_acc": 0.35,
650	      "ot_7b_binary_collapse_delta": "+1.1pp",
651	      "r1_32b_16label_acc": 0.28,
652	      "r1_32b_binary_collapse_delta": "+0.6pp",
653	      "qwq_32b_16label_acc": 0.26,
654	      "qwq_32b_binary_collapse_delta": "+0.9pp",
655	      "fine_grained_improvement_marginal": true,
656	      "max_collapse_delta": "+1.1pp"
657	    },
658	    "tables": [
659	      {
660	        "name": "16-Label vs Binary Supervision",
661	        "columns": [
662	          "Model",
663	          "Binary Acc",
664	          "16-Label Acc",
665	          "16→Binary Collapse",
666	          "Δ vs Binary"
667	        ],
668	        "rows": [
669	          [
670	            "R1-8B",
671	            "0.817",
672	            "0.41",
673	            "0.825",
674	            "+0.8pp"
675	          ],
676	          [
677	            "OT-7B",
678	            "0.688",
679	            "0.35",
680	            "0.699",
681	            "+1.1pp"
682	          ],
683	          [
684	            "QwQ-32B",
685	            "0.740",
686	            "0.26",
687	            "0.749",
688	            "+0.9pp"
689	          ],
690	          [
691	            "R1-32B",
692	            "0.826",
693	            "0.28",
694	            "0.832",
695	            "+0.6pp"
696	          ]
697	        ]
698	      }
699	    ],
700	    "figures": [],
701	    "analysis": "Fine-grained supervision dead-end. Worst-tier implication: \"The information ceiling for linear probes on single-layer hidden states is fundamentally limited. Trying harder with better labels or more metrics can't overcome this.\"\n\n\nFine-grained supervision provides marginal benefit (+0.6-1.1pp after binary collapse) across all models. The 16-class accuracy is low (26-41%) because the classes are imbalanced and transition types are not cleanly separable in hidden-state space. Worst-tier reviewers react: (1) \"Marginal improvement from richer supervision confirms the probe is already extracting most of the available linear signal in binary mode. This supports the reviewer's argument that linear probes are saturated — not that the methodology is optimal, but that the information ceiling is low.\" (2) \"The 16-label experiment was motivated by reviewer concern about 'underusing available supervision,' but the result shows supervision quality doesn't matter much. This undermines the paper's implicit argument that careful methodology (layer selection, temporal context) is what matters — it seems the representation quality is the binding constraint.\"\n"
702	  },
703	  {
704	    "name": "Oracle decomposition",
705	    "description": "Analyze what the oracle label sequence encodes that hidden-state probes cannot access. Compare oracle lead (+31 steps on R1-8B) to probe lead (~0 steps).\n",
706	    "results": {
707	      "r1_8b_oracle_lead": "+31.0",
708	      "r1_8b_best_probe_lead": "+4.5 (GRU)",
709	      "r1_8b_oracle_gap": "26.5",
710	      "r1_8b_label_autocorr_pre_cp": 0.82,
711	      "r1_8b_hs_autocorr_pre_cp": 0.95,
712	      "label_entropy_pre_cp_r1_8b": 1.38,
713	      "hs_entropy_pre_cp_r1_8b": 0.41,
714	      "r1_32b_oracle_lead": "+28",
715	      "r1_32b_best_probe_lead": "+13 (W=1, 25% cov)",
716	      "qwq_oracle_lead": "+27",
717	      "qwq_best_probe_lead": "−1.2 to +1.9",
718	      "pattern_finding": "Labels show gradual safety erosion pre-CP; hidden states show step-function at CP"
719	    },
720	    "tables": [
721	      {
722	        "name": "Oracle vs Best Probe Lead Time",
723	        "columns": [
724	          "Model",
725	          "Oracle Lead",
726	          "Best Probe Lead",
727	          "Method",
728	          "Gap",
729	          "Hidden State Entropy (pre-CP)"
730	        ],
731	        "rows": [
732	          [
733	            "R1-8B",
734	            "+31.0",
735	            "+4.5",
736	            "GRU multi-layer",
737	            "26.5",
738	            "0.41"
739	          ],
740	          [
741	            "OT-7B",
742	            "~+30",
743	            "+33.6 (GRU)",
744	            "GRU multi-layer",
745	            "~0†",
746	            "—"
747	          ],
748	          [
749	            "QwQ-32B",
750	            "+27",
751	            "−1.2 to +1.9",
752	            "temporal LR",
753	            "25-28",
754	            "—"
755	          ],
756	          [
757	            "R1-32B",
758	            "+28",
759	            "+13.3",
760	            "temporal LR W=1",
761	            "15 (25% cov)",
762	            "—"
763	          ]
764	        ]
765	      }
766	    ],
767	    "figures": [],
768	    "analysis": "The oracle decomposition is the worst-tier's strongest negative finding: hidden states are fundamentally reactive (encoding current state) rather than predictive (encoding trajectory). Reviewer: \"This paper demonstrates that hidden-state monitoring is a lagging indicator. For safety deployment, you need leading indicators. Text-based trajectory analysis, while noisier, is the better research direction.\"\n\n\nOracle decomposition reveals a 26-28 step gap between what's detectable in labels vs hidden states. The label sequence shows gradual pre-CP patterns (increasing unsafe-adjacent labels, shortening safe streaks) that hidden states don't track. Worst-tier reviewers draw a harsh conclusion: \"The 31-step oracle lead proves that safety commitment is a GRADUAL process visible in the model's outputs. But the hidden-state probe can only detect it at or after the commitment point (lead ≈ 0). This means hidden states encode the CURRENT safety state but not the TRAJECTORY toward commitment. For deployment, trajectory prediction is what matters — catching the commitment after it happens is too late. The oracle gap is not a puzzle for Discussion; it's evidence that the entire hidden-state monitoring approach is fundamentally limited. Text-based monitoring that tracks reasoning trajectory (even with higher FPR) provides earlier warning.\"\n"
769	  },
770	  {
771	    "name": "OpenThinker-7B (Qwen2.5-7B, STILL-trained)",
772	    "description": "4th model completing the 2×2 architecture×scale matrix. Full pipeline: layer sweep, temporal probes, HS vs text comparison, GRU, selectivity control task.\n",
773	    "results": {
774	      "best_layer": 16,
775	      "best_layer_depth_pct": 57.1,
776	      "best_hs_bal_acc_w3": 0.688,
777	      "best_hs_precision_w3": 0.466,
778	      "best_hs_pre_cp_fpr": 0.1,
779	      "bootstrap_3_of_3_hb": true,
780	      "bootstrap_bal_acc_delta": "+10.7pp",
781	      "bootstrap_precision_delta": "+21.9pp",
782	      "bootstrap_fpr_delta": "−17.1pp",
783	      "selectivity_pp": 18.3,
784	      "n_traces": 228,
785	      "gru_multi_bal_acc": 0.746,
786	      "gru_multi_lead": "+33.6",
787	      "gru_multi_fpr": 0.274,
788	      "hs_temporal_saturation_w3": true,
789	      "text_temporal_w25_best": 0.614
790	    },
791	    "tables": [
792	      {
793	        "name": "OT-7B Full Pipeline Summary",
794	        "columns": [
795	          "Method",
796	          "bal_acc",
797	          "precision",
798	          "pre-CP FPR",
799	          "coverage",
800	          "lead"
801	        ],
802	        "rows": [
803	          [
804	            "HS temporal W=3 L16",
805	            "0.688",
806	            "0.466",
807	            "0.100",
808	            "0.532",
809	            "+21.6"
810	          ],
811	          [
812	            "Text temporal W=25",
813	            "0.614",
814	            "0.329",
815	            "0.161",
816	            "0.660",
817	            "+45.5"
818	          ],
819	          [
820	            "GRU multi L13-19",
821	            "0.746",
822	            "—",
823	            "0.274",
824	            "0.645",
825	            "+33.6"
826	          ],
827	          [
828	            "HS-Text Δ (HB)",
829	            "+10.7pp ✅",
830	            "+21.9pp ✅",
831	            "−17.1pp ✅",
832	            "—",
833	            "—"
834	          ]
835	        ]
836	      }
837	    ],
838	    "figures": [],
839	    "analysis": "OT-7B strengthens the 7-8B story but worst-tier reviewers note: \"The 2×2 matrix now has two strong cells (7-8B) and two weak cells (32B). The paper's breadth claim ('4 models') is technically true but misleading — 2/4 models have serious practical caveats that make the HS advantage non-deployable.\"\n\n\nOT-7B is the cleanest single-model evidence for HS advantage (3/3 HB, highest selectivity 18.3pp, largest n=228 traces). But worst-tier reviewers are unimpressed by adding a 4th model that confirms the known pattern: (1) \"A 4th model at 7B showing the same result doesn't address the 32B caveats. The paper already has two 7-8B models that work. The question is whether HS monitoring scales, and OT-7B can't answer that.\" (2) \"OT-7B has its own caveats: HS temporal saturation at W=3 (bal_acc declines at larger W), and absolute performance is still below R1-8B (best bal_acc 68.8% vs 80.2%). The 'cleanest evidence' is still only 69% balanced accuracy — barely better than a biased coin.\" (3) \"GRU lead time of +33.6 steps sounds impressive until you note OT-7B traces average ~80 sentences — normalize by trace length and the lead time fraction is similar to other models.\" (4) \"FPR of 27.4% for GRU means ~1 in 4 safe steps triggers the detector. At 80-sentence traces, that's ~20 false alarms per safe trace.\"\n"
840	  },
841	  {
842	    "name": "GRU/Attention probe upper bound (32B models)",
843	    "description": "GRU sequence model on 32B models at corrected layers. Tests whether nonlinear sequence modeling can recover signal that linear temporal probes miss.\n",
844	    "results": {
845	      "r1_32b_gru_single_bal_acc": 0.675,
846	      "r1_32b_gru_multi_bal_acc": 0.655,
847	      "r1_32b_gru_lead_mean": "+8.8 to +9.1",
848	      "r1_32b_gru_fpr": "0.114 to 0.135",
849	      "r1_32b_gru_coverage": "0.23 to 0.30",
850	      "r1_32b_gru_vs_lr_delta": "−6pp bal_acc (GRU worse)",
851	      "qwq_32b_gru_single_bal_acc": 0.694,
852	      "qwq_32b_gru_multi_bal_acc": 0.724,
853	      "qwq_32b_gru_lead_mean": "+15.9",
854	      "qwq_32b_gru_fpr": 0.289,
855	      "qwq_32b_gru_coverage": 0.84,
856	      "qwq_32b_gru_vs_lr_delta": "−3.7pp bal_acc (GRU worse at bal_acc, better at coverage)",
857	      "ot_7b_gru_multi_bal_acc": 0.746,
858	      "ot_7b_gru_multi_lead": "+33.6",
859	      "ot_7b_gru_fpr": 0.274,
860	      "gru_worse_than_lr_3_of_4": true,
861	      "gru_note": "GRU trades accuracy for coverage/lead — higher FPR drives earlier detection"
862	    },
863	    "tables": [
864	      {
865	        "name": "GRU vs Temporal LR (32B models, corrected layers)",
866	        "columns": [
867	          "Model",
868	          "LR bal_acc",
869	          "GRU bal_acc",
870	          "Δ",
871	          "GRU FPR",
872	          "LR FPR"
873	        ],
874	        "rows": [
875	          [
876	            "R1-32B (L63 W=10)",
877	            "0.737",
878	            "~0.675",
879	            "−6.2pp",
880	            "0.135",
881	            "0.234"
882	          ],
883	          [
884	            "QwQ-32B (L60 W=5)",
885	            "0.761",
886	            "0.724",
887	            "−3.7pp",
888	            "0.289",
889	            "0.217"
890	          ],
891	          [
892	            "OT-7B (L16 multi)",
893	            "0.688",
894	            "0.746",
895	            "+5.8pp",
896	            "0.274",
897	            "0.100"
898	          ],
899	          [
900	            "R1-8B (L14 multi)",
901	            "0.806",
902	            "0.809",
903	            "+0.3pp",
904	            "0.165",
905	            "0.097"
906	          ]
907	        ]
908	      }
909	    ],
910	    "figures": [],
911	    "analysis": "GRU fails to improve over LR on most models, confirming linear probes are at the information ceiling. Worst-tier reviewer: \"The paper's headline is 'HS beats text.' The method is logistic regression. The contribution is... careful hyperparameter selection? This is a well-executed experiment report, not a methods paper.\"\n\n\nGRU does NOT outperform temporal LR on balanced accuracy for 3/4 models. On R1-32B (n=20 test), GRU severely overfits — bal_acc drops 6pp below LR. On QwQ, GRU achieves higher coverage and lead time but at 2× the FPR. This confirms linear probes are sufficient (or even superior given small samples). Worst-tier reviewers use this to attack novelty: \"The paper's method is logistic regression on hidden states with a sliding window. That's not a contribution — it's the simplest possible baseline. The fact that GRU and MLP don't help confirms the method space is trivial, which means the paper's 'systematic comparison of 7 methods' is comparing variations of the obvious approach (linear probe) against methods that were never designed for this task (Mahalanobis, BOCPD, CCS). The negative results are predictable, not informative.\"\n"
912	  },
913	  {
914	    "name": "Text-based baseline (sentence embeddings + temporal LR)",
915	    "description": "Sentence-BERT (all-MiniLM-L6-v2) embeddings + temporal window LR on CoT text of all 4 models. Critical comparison establishing what text monitoring achieves without hidden-state access.\n",
916	    "results": {
917	      "r1_8b_text_static_acc": 0.661,
918	      "r1_8b_text_temporal_w15_acc": 0.678,
919	      "r1_8b_text_temporal_w15_auroc": 0.759,
920	      "r1_8b_hs_acc_advantage": "+15-18pp",
921	      "ot_7b_text_best_bal_acc": 0.614,
922	      "ot_7b_text_best_precision": 0.329,
923	      "ot_7b_text_best_fpr": 0.161,
924	      "qwq_32b_text_temporal_bal_acc": 0.65,
925	      "qwq_32b_text_precision": 0.421,
926	      "r1_32b_text_temporal_bal_acc": 0.646,
927	      "r1_32b_text_precision": 0.45,
928	      "hs_vs_text_precision_gap_range": "+15.4 to +23.6pp",
929	      "text_requires_zero_infra_change": true,
930	      "text_precision_all_models": "0.329-0.487",
931	      "hs_precision_all_models": "0.466-0.776"
932	    },
933	    "tables": [
934	      {
935	        "name": "HS vs Text Precision Gap (+ engineering cost annotation)",
936	        "columns": [
937	          "Model",
938	          "HS Precision",
939	          "Text Precision",
940	          "Δ",
941	          "HS Infra Cost"
942	        ],
943	        "rows": [
944	          [
945	            "R1-8B",
946	            "0.777 (W=15)",
947	            "0.487 (W=15)",
948	            "+29.0pp",
949	            "white-box, L14"
950	          ],
951	          [
952	            "OT-7B",
953	            "0.466 (W=3)",
954	            "0.329 (W=25)",
955	            "+13.7pp",
956	            "white-box, L16"
957	          ],
958	          [
959	            "QwQ-32B",
960	            "0.578 (W=3)",
961	            "0.421 (W=best)",
962	            "+15.7pp",
963	            "white-box, L60"
964	          ],
965	          [
966	            "R1-32B",
967	            "0.603 (W=1)",
968	            "0.450 (W=best)",
969	            "+15.3pp",
970	            "white-box, L63"
971	          ]
972	        ]
973	      }
974	    ],
975	    "figures": [],
976	    "analysis": "The text baseline is the worst-tier reviewer's strongest weapon: \"A 15-24pp precision gain sounds meaningful until you consider: (a) text monitoring costs $0 in infrastructure, (b) HS monitoring requires white-box access + per-model tuning, (c) the BGE-large result shows the gap shrinks with better text encoders, (d) safe FPR is 39-62% regardless of modality — both approaches produce unusable false alarm rates. The paper should honestly state: 'HS probes are measurably but marginally better than text probes. Whether the margin justifies white-box access depends on deployment constraints. For most practical settings, text monitoring suffices.'\"\n\n\nText baseline performs consistently across all models (bal_acc 0.61-0.68, precision 0.33-0.49). HS probes outperform by +15-24pp precision, which is statistically significant (12/12 HB). But worst-tier reviewers attack the COST-BENEFIT ratio, not the statistical claim: (1) \"Text probes need zero infrastructure change — you monitor the CoT output that's already available. HS probes require white-box access to model internals, which means: (a) running the model locally (can't use API), (b) modifying the inference pipeline to extract intermediate activations, (c) per-model layer selection + probe training. The 15-24pp precision gain comes at enormous engineering cost.\" (2) \"At 33-49% text precision, you get 1 true alarm per 2-3 triggers. At 47-78% HS precision, you get 1 per 1.3-2.1 triggers. Is that difference worth instrumenting your entire inference stack? For most deployment teams, no.\" (3) \"Text probes improve with better embeddings (BGE-large, domain-fine-tuned). The paper tested only all-MiniLM-L6-v2 — the weakest common baseline. A reviewer notes: 'Use GPT-4 as the text classifier and the gap likely narrows to <5pp.'\" (4) \"The BGE-large comparison (exp_bge_large_text_comparison) showed only 1/4 HB pass for HS vs BGE-large — the gap narrows significantly with a better text encoder.\"\n"
977	  },
978	  {
979	    "name": "BOCPD/CUSUM on all 4 models",
980	    "description": "Bayesian Online Change-Point Detection + CUSUM on probe score sequences. Tests whether advanced change-point methods can achieve positive lead time.\n",
981	    "results": {
982	      "r1_8b_bocpd_detection": 0.93,
983	      "r1_8b_bocpd_lead": "+3.45",
984	      "r1_8b_cusum_lead": "+0.89",
985	      "r1_8b_fcp_baseline_lead": "+4.89",
986	      "r1_8b_fcp_beats_bocpd_on_lead": true,
987	      "ot_7b_bocpd_detection": 0.0,
988	      "ot_7b_bocpd_note": "W=3 probe scores too spiky, Gaussian model fails",
989	      "ot_7b_fcp_best_detection": 0.894,
990	      "ot_7b_fcp_best_lead": "+11.83",
991	      "r1_32b_bocpd_detection": 0.0,
992	      "qwq_32b_bocpd_detection": 0.0,
993	      "r1_32b_cusum_detection": 0.85,
994	      "r1_32b_cusum_lead": "+2.59",
995	      "qwq_32b_cusum_detection": 0.737,
996	      "qwq_32b_cusum_lead": "+9.86",
997	      "bocpd_works_only_r1_8b": true,
998	      "cusum_universally_worse_than_fcp": true
999	    },
1000	    "tables": [
1001	      {
1002	        "name": "Change-Point Detection Cross-Model Summary",
1003	        "columns": [
1004	          "Model",
1005	          "BOCPD Det%",
1006	          "BOCPD Lead",
1007	          "CUSUM Det%",
1008	          "CUSUM Lead",
1009	          "FCP Det%",
1010	          "FCP Lead"
1011	        ],
1012	        "rows": [
1013	          [
1014	            "R1-8B",
1015	            "93%",
1016	            "+3.45",
1017	            "65%",
1018	            "+0.89",
1019	            "65%",
1020	            "+4.89"
1021	          ],
1022	          [
1023	            "OT-7B",
1024	            "0%",
1025	            "—",
1026	            "75%†",
1027	            "+7.46†",
1028	            "89%",
1029	            "+11.83"
1030	          ],
1031	          [
1032	            "R1-32B",
1033	            "0%",
1034	            "—",
1035	            "85%",
1036	            "+2.59",
1037	            "95%",
1038	            "+5.68"
1039	          ],
1040	          [
1041	            "QwQ-32B",
1042	            "0%",
1043	            "—",
1044	            "74%",
1045	            "+9.86",
1046	            "79%",
1047	            "+9.40"
1048	          ]
1049	        ]
1050	      }
1051	    ],
1052	    "figures": [],
1053	    "analysis": "Complete BOCPD failure on 3/4 models and CUSUM inferiority to simple thresholding. Worst-tier reviewer: \"The paper tests two change-point algorithms that were designed for very different signal types, finds they don't work, and claims this as a negative result. But the method selection is so narrow that the negative result is uninformative — you tested the wrong tools.\"\n\n\nBOCPD fails on 3/4 models (0% detection on OT-7B, R1-32B, QwQ). Only R1-8B works (93%) because R1-8B has gradual probe score transitions that match BOCPD's Gaussian change-point model. Other models have abrupt transitions (OT-7B) or weak signals (32B) that BOCPD's parametric assumptions can't handle. CUSUM detects some traces but with worse lead than simple first-crossing-point (FCP) threshold. Worst-tier reviewers: (1) \"BOCPD and CUSUM were never designed for this signal type. Testing them is due diligence, but their failure is predictable — these methods assume stationary-then-shifted Gaussian data, while probe scores are bounded [0,1] and often spiky.\" (2) \"The negative result strengthens the 'nothing works well' narrative, but the method selection is questionable. Why not test HMM, Viterbi decoding, or learned change-point detectors? The paper tests 2 off-the-shelf methods and declares change-point detection a dead end.\" (3) \"Simple FCP threshold beats BOCPD on mean lead time for R1-8B. The 'advanced' methods add nothing.\"\n"
1054	  },
1055	  {
1056	    "name": "False positive analysis (safe trace FPR, all methods)",
1057	    "description": "Run all probes on safe traces (final_judgment=0.5) across all 4 models. Report safe FPR, pre-CP FPR, precision, and precision-recall curves.\n",
1058	    "results": {
1059	      "r1_8b_hs_safe_fpr": 0.39,
1060	      "r1_8b_text_safe_fpr": 0.385,
1061	      "ot_7b_hs_safe_fpr": "0.111-0.175",
1062	      "ot_7b_text_safe_fpr": "0.302-0.460",
1063	      "qwq_32b_hs_safe_fpr": "0.45-0.50",
1064	      "qwq_32b_text_safe_fpr": "0.325-0.425",
1065	      "r1_32b_hs_safe_fpr": 0.239,
1066	      "r1_32b_text_safe_fpr": 0.31,
1067	      "safe_fpr_range_all": "0.111 to 0.521",
1068	      "safe_fpr_median": "~0.39",
1069	      "gru_safe_fpr": 0.521,
1070	      "gru_highest_fpr_note": "GRU trades precision for coverage → highest FPR",
1071	      "precision_all_methods_range": "0.329 to 0.777",
1072	      "no_method_achieves_80pct_precision": true,
1073	      "deployment_threshold_precision_70": "only R1-8B HS W≥15 exceeds"
1074	    },
1075	    "tables": [
1076	      {
1077	        "name": "Safe Trace FPR Summary (all methods × all models)",
1078	        "columns": [
1079	          "Model",
1080	          "HS Static FPR",
1081	          "HS Temporal FPR",
1082	          "Text Temporal FPR",
1083	          "GRU FPR"
1084	        ],
1085	        "rows": [
1086	          [
1087	            "R1-8B",
1088	            "0.390",
1089	            "0.392",
1090	            "0.385",
1091	            "0.521"
1092	          ],
1093	          [
1094	            "OT-7B",
1095	            "0.111",
1096	            "0.175",
1097	            "0.460",
1098	            "—"
1099	          ],
1100	          [
1101	            "QwQ-32B",
1102	            "0.500",
1103	            "0.450",
1104	            "0.425",
1105	            "—"
1106	          ],
1107	          [
1108	            "R1-32B",
1109	            "0.239",
1110	            "0.239",
1111	            "0.310",
1112	            "—"
1113	          ]
1114	        ]
1115	      },
1116	      {
1117	        "name": "Deployment Viability Assessment",
1118	        "columns": [
1119	          "Criterion",
1120	          "Threshold",
1121	          "Models Meeting Criterion",
1122	          "Best Method"
1123	        ],
1124	        "rows": [
1125	          [
1126	            "Safe FPR < 20%",
1127	            "0.20",
1128	            "1/4 (OT-7B HS static)",
1129	            "HS static L16"
1130	          ],
1131	          [
1132	            "Precision > 70%",
1133	            "0.70",
1134	            "1/4 (R1-8B W≥15)",
1135	            "HS temporal W=25"
1136	          ],
1137	          [
1138	            "Coverage > 60%",
1139	            "0.60",
1140	            "2/4 (R1-8B W≤3, R1-32B W≤3)",
1141	            "HS temporal W=1"
1142	          ],
1143	          [
1144	            "All three criteria",
1145	            "—",
1146	            "0/4",
1147	            "None"
1148	          ]
1149	        ]
1150	      }
1151	    ],
1152	    "figures": [],
1153	    "analysis": "FPR analysis is the worst-tier's core evidence for the \"not practically useful\" dismissal. No model meets all three deployment criteria simultaneously. The best model (R1-8B) achieves >70% precision only at W≥15 where coverage drops to 49%. The paper's deployment framing is untenable. Reframing guidance: \"Position as diagnostic/research tool, explicitly disclaim deployment readiness. Lead with 'none of our 7 methods achieves deployment-ready performance' as a cautionary finding.\"\n\n\nSafe FPR ranges from 11% (OT-7B HS static, best case) to 52% (GRU, worst case), with a median around 39%. This is the worst-tier dealbreaker. Reviewer calculation: \"At 39% safe FPR with K=5 consecutive crossings for trace-level detection, a 40-step safe trace has ~39% probability of triggering the detector. In a production system processing 1000 safe traces per day, that's ~390 false alarms daily. Each requires human review at ~5 minutes → 32.5 person-hours/day of false alarm triage. No deployment team would accept this.\" Even the best case (OT-7B HS 11.1% safe FPR) means 111 false alarms per 1000 safe traces. The worst-tier reviewer's verdict: \"A safety monitor that fires on 1 in 3 to 1 in 2 safe traces is not a monitor — it's a random noise generator. The paper should lead with this limitation, not bury it.\" QwQ-32B is particularly problematic: HS safe FPR (45-50%) is HIGHER than text safe FPR (33-43%), meaning HS monitoring generates MORE false alarms on safe traces for QwQ.\n"
1154	  },
1155	  {
1156	    "name": "5-fold CV validation of multi-metric ensemble (7-8B)",
1157	    "description": "Cross-validated ensemble of metric-weighted layer selections on R1-8B and OT-7B. Validates that multi-metric ensemble eliminates layer selection bias under proper CV.\n",
1158	    "results": {
1159	      "r1_8b_ensemble_cv_prec": 0.565,
1160	      "r1_8b_best_single_cv_prec": 0.604,
1161	      "r1_8b_ensemble_vs_text_gap": "+19.3pp",
1162	      "r1_8b_ensemble_vs_text_p": "<0.002",
1163	      "ot_7b_ensemble_cv_prec": 0.506,
1164	      "ot_7b_best_single_cv_prec": 0.473,
1165	      "ot_7b_ensemble_beats_best_single": true,
1166	      "ot_7b_ensemble_beats_best_single_p": 0.033,
1167	      "cv_validates_preliminary": true,
1168	      "cv_acceptance_probability_delta": "+0.01 to +0.03"
1169	    },
1170	    "tables": [
1171	      {
1172	        "name": "Ensemble CV Results (7-8B models)",
1173	        "columns": [
1174	          "Model",
1175	          "Ensemble Prec",
1176	          "Best Single Prec",
1177	          "Text Prec",
1178	          "Ens vs Text p"
1179	        ],
1180	        "rows": [
1181	          [
1182	            "R1-8B",
1183	            "0.565",
1184	            "0.604",
1185	            "0.372",
1186	            "<0.002"
1187	          ],
1188	          [
1189	            "OT-7B",
1190	            "0.506",
1191	            "0.473",
1192	            "0.236",
1193	            "<0.001"
1194	          ]
1195	        ]
1196	      }
1197	    ],
1198	    "figures": [],
1199	    "analysis": "Ensemble CV is a marginal improvement on an already-validated statistical claim. Worst-tier impact on acceptance: negligible (+1-3%). The bottleneck is not statistical rigor — it's practical utility and novelty. This experiment is low-cost and worth including in supplementary, but it cannot rescue the paper from worst-tier reviewer concerns.\n\nCV validation confirms the ensemble result holds (p≤0.002 for ensemble vs text on R1-8B). But worst-tier reviewers are unmoved: (1) \"CV validating an ensemble of layer selection metrics on 7-8B models doesn't address ANY of our core concerns. The issues are: high safe FPR (39-62%), model-specific caveats at 32B, engineering cost of white-box access, and insufficient novelty. A statistically cleaner layer selection protocol is nice but tangential.\" (2) \"The ensemble precision (0.506-0.565) is actually LOWER than the best single metric on R1-8B (0.604). On OT-7B the ensemble slightly beats the best single metric (0.506 vs 0.473) but the absolute precision is 50% — a coin flip.\" (3) \"This experiment strengthens an already- strong statistical case (12/12 HB already passes). The paper doesn't need MORE statistical validation; it needs BETTER results or a DIFFERENT framing.\" The CV ensemble moves acceptance probability by +1-3%, insufficient to shift from worst tier.\n"
1200	  }
1201	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd0479a-9ea3-4274-98a0-0f2b60ea51ff",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "05ef7184-9592-4424-8f77-b1b10d6b796f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Cross-architecture layer sweep + static probe (r1-32b & QwQ-32B)\",\n    \"description\": \"Full 64-layer sweep on DeepSeek-R1-Distill-Qwen-32B and QwQ-32B. Extract hidden states at all layers, evaluate static LR probes per layer under multiple selection metrics. Includes discovery of layer selection bias (bal_acc × crossing_rate → shallow layers).\\n\",\n    \"results\": {\n      \"r1_32b_biased_layer\": 10,\n      \"r1_32b_biased_layer_depth_pct\": 15.6,\n      \"r1_32b_corrected_layer\": 63,\n      \"r1_32b_corrected_layer_depth_pct\": 98.4,\n      \"r1_32b_l10_bal_acc\": 0.718,\n      \"r1_32b_l63_bal_acc_w1\": 0.826,\n      \"r1_32b_n_test\": 20,\n      \"r1_32b_l63_precision_w1\": 0.603,\n      \"r1_32b_l63_fpr_w1\": 0.235,\n      \"qwq_32b_biased_layer\": 2,\n      \"qwq_32b_biased_layer_depth_pct\": 3.1,\n      \"qwq_32b_corrected_layer\": 60,\n      \"qwq_32b_corrected_layer_depth_pct\": 93.8,\n      \"qwq_32b_l2_bal_acc\": 0.73,\n      \"qwq_32b_l60_bal_acc_w3\": 0.74,\n      \"qwq_32b_n_test\": \"19-20\",\n      \"qwq_32b_l60_precision_w3\": 0.578,\n      \"qwq_32b_l60_fpr_w3\": 0.279,\n      \"layer_selection_bias_discovered\": true,\n      \"metrics_tested\": 5,\n      \"biased_metric\": \"bal_acc × crossing_rate\",\n      \"loo_cv_dominant_fold_pct\": \"65-68%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Layer Selection Metric × Model → Selected Layer\",\n        \"columns\": [\n          \"Metric\",\n          \"R1-8B\",\n          \"OT-7B\",\n          \"QwQ-32B\",\n          \"R1-32B\"\n        ],\n        \"rows\": [\n          [\n            \"bal_acc × crossing_rate\",\n            \"L0 (0%)\",\n            \"L0 (0%)\",\n            \"L2 (3%)\",\n            \"L10 (16%)\"\n          ],\n          [\n            \"pure bal_acc\",\n            \"L12 (39%)\",\n            \"L9 (32%)\",\n            \"L30 (47%)\",\n            \"L47 (73%)\"\n          ],\n          [\n            \"precision\",\n            \"L16 (52%)\",\n            \"L16 (57%)\",\n            \"L60 (94%)\",\n            \"L63 (98%)\"\n          ],\n          [\n            \"pre_cp_fpr\",\n            \"L16 (52%)\",\n            \"L16 (57%)\",\n            \"L60 (94%)\",\n            \"L63 (98%)\"\n          ],\n          [\n            \"composite (additive)\",\n            \"L16 (52%)\",\n            \"L12 (43%)\",\n            \"L60 (94%)\",\n            \"L63 (98%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Layer selection sensitivity is the paper's primary methodological contribution, but worst-tier reviewers rate it insufficient novelty (2.0-2.5). The argument: \\\"every ML practitioner knows different metrics select different hyperparameters. Showing this for layer selection is an observation, not a method. There's no proposed algorithm to automatically resolve the disagreement — just 'try more metrics,' which is standard practice.\\\"\\n\\n\\nLayer sweep reveals a genuine methodological finding (biased metric selects shallow layers), and corrected layers do show HS advantage. However, worst-tier reviewers dismiss this: (1) \\\"Finding that one composite metric is bad is trivially expected — practitioners routinely try multiple metrics. This is hyperparameter tuning, not a contribution.\\\" (2) n=19-20 test traces for 32B models mean bootstrap CIs are wide. MDE analysis shows R1-32B residualized gap (+1.9pp) is far below the 11.2pp MDE at 80% power — the NS result for position-mediated HS advantage is a power limitation, not evidence. Reviewers note: \\\"you can't claim the advantage is 'real but position-mediated' when you're underpowered to detect the non-positional component.\\\" (3) The corrected layers (L60/L63, >93% depth) are so deep they're essentially the output layer — reviewer asks: \\\"are you just detecting output-token semantics via a different pathway?\\\"\\n\"\n  },\n  {\n    \"name\": \"Cross-architecture temporal window evaluation (32B)\",\n    \"description\": \"Temporal LR at multiple window sizes on R1-32B (L63) and QwQ-32B (L60). Evaluate whether temporal context universally improves probe accuracy across 32B models.\\n\",\n    \"results\": {\n      \"r1_32b_l63_w1_bal_acc\": 0.826,\n      \"r1_32b_l63_w1_precision\": 0.603,\n      \"r1_32b_l63_w1_coverage\": 0.25,\n      \"r1_32b_l63_w3_bal_acc\": 0.754,\n      \"r1_32b_l63_w5_bal_acc\": 0.741,\n      \"r1_32b_l63_w10_bal_acc\": 0.737,\n      \"r1_32b_l63_w15_bal_acc\": 0.721,\n      \"r1_32b_temporal_trend\": \"DECREASING with W (W=1 best, -10.5pp by W=15)\",\n      \"r1_32b_dimensionality_issue\": \"51200 × W features for n=20 → massive overfitting at W≥3\",\n      \"qwq_32b_l60_w1_bal_acc\": 0.74,\n      \"qwq_32b_l60_w3_bal_acc\": 0.74,\n      \"qwq_32b_l60_w5_bal_acc\": 0.742,\n      \"qwq_32b_l60_w15_bal_acc\": 0.731,\n      \"qwq_32b_temporal_trend\": \"flat to slightly decreasing\",\n      \"qwq_32b_best_w\": 5,\n      \"text_temporal_universal_improvement\": true,\n      \"hs_temporal_improvement_3_of_4\": true,\n      \"hs_temporal_exception\": \"OT-7B HS peaks W=3, declines at larger W; R1-32B only W=1 significant\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Temporal Window Effect on 32B Models (HS probes, corrected layers)\",\n        \"columns\": [\n          \"Model\",\n          \"Layer\",\n          \"W=1\",\n          \"W=3\",\n          \"W=5\",\n          \"W=10\",\n          \"W=15\",\n          \"Trend\"\n        ],\n        \"rows\": [\n          [\n            \"R1-32B\",\n            \"L63\",\n            \"0.826*\",\n            \"0.754\",\n            \"0.741\",\n            \"0.737\",\n            \"0.721\",\n            \"↓ declining\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"L60\",\n            \"0.740\",\n            \"0.740\",\n            \"0.742\",\n            \"0.735\",\n            \"0.731\",\n            \"→ flat\"\n          ],\n          [\n            \"R1-8B\",\n            \"L14\",\n            \"0.778\",\n            \"0.790\",\n            \"0.781\",\n            \"0.793\",\n            \"0.802\",\n            \"↑ improving\"\n          ],\n          [\n            \"OT-7B\",\n            \"L16\",\n            \"0.663\",\n            \"0.688*\",\n            \"0.678\",\n            \"0.668\",\n            \"0.659\",\n            \"↑↓ peaks W=3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst-tier reviewers note: \\\"Temporal context helps universally for text probes (a known result — more context helps NLP classifiers). For HS probes, 2/4 models show non-monotonic or declining trends. The paper's Claim 1 should be 'temporal context helps text probes' — attributing it to HS probes is cherry-picking the models where it works.\\\"\\n\\n\\nTemporal context shows a split pattern at 32B: QwQ benefits modestly across all W (text and HS), but R1-32B DEGRADES with increasing W because concatenating 51200-dimensional vectors across W>1 windows creates a feature space massively exceeding n=20 training samples. This is not a failure of the temporal hypothesis — it's a sample-size bottleneck. Worst-tier reviewers seize on this: \\\"R1-32B temporal results are meaningless because you're fitting 102400+ parameters to 20 samples. The W=1 'significance' at L63 survives only because W=1 avoids this problem. Your 'best' result for R1-32B is actually a dimensionality artifact — the only window that avoids overfitting happens to be significant.\\\" Claim 1 (temporal universally helps) holds for text probes across all 4 models, but for HS probes, 2/4 models have caveats (OT-7B saturation, R1-32B dimensionality). Reviewers frame this as \\\"temporal improvement is a text-probe finding, not an HS-probe finding.\\\"\\n\"\n  },\n  {\n    \"name\": \"Cross-model transfer probes\",\n    \"description\": \"Train probe on one model, test on another. PCA projection for cross-architecture transfer (4096→5120 or vice versa). Tests whether safety commitment encoding is universal.\\n\",\n    \"results\": {\n      \"r1_8b_to_r1_32b_acc\": 0.522,\n      \"r1_8b_to_qwq_acc\": 0.595,\n      \"r1_32b_to_qwq_acc\": 0.673,\n      \"qwq_to_r1_32b_acc\": 0.673,\n      \"r1_32b_to_r1_8b_acc\": 0.583,\n      \"best_transfer_overall\": 0.673,\n      \"chance_baseline\": 0.5,\n      \"all_transfers_below_within_model\": true,\n      \"within_family_32b_weak_transfer\": 0.673,\n      \"cross_family_at_chance\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Model Transfer Accuracy Matrix\",\n        \"columns\": [\n          \"Train →\",\n          \"R1-8B\",\n          \"OT-7B\",\n          \"R1-32B\",\n          \"QwQ-32B\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.817 (self)\",\n            \"—\",\n            \"0.522\",\n            \"0.595\"\n          ],\n          [\n            \"OT-7B\",\n            \"—\",\n            \"0.688 (self)\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"R1-32B\",\n            \"0.583\",\n            \"—\",\n            \"0.826 (self)\",\n            \"0.673\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"—\",\n            \"—\",\n            \"0.673\",\n            \"0.740 (self)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Complete transfer failure. Worst-tier reviewers conclude: \\\"The paper claims to study 'safety commitment detection' as a general phenomenon, but the probes are entirely model-specific. This means the method has zero practical scalability — you need labeled data for every model you want to monitor. Combined with the engineering cost of white-box access, the deployment story collapses.\\\"\\n\\n\\nCross-model transfer fails completely — the best transfer accuracy (67.3% Qwen-family 32B internal) is far below within-model performance and barely above the majority-class baseline. Cross-family transfer (Llama↔Qwen) is at chance. Worst-tier reviewers use this as evidence against the paper: \\\"Safety encoding is model-specific. This means every new model needs its own probe training with labeled commitment points — a supervision cost the paper downplays. If safety commitment were a universal phenomenon, SOME geometric structure should transfer. The complete failure suggests the probes are learning model-specific artifacts, not a generalizable safety signal.\\\" This finding is consistent with the selectivity control task (7.5-18.5pp) but reviewers argue selectivity merely shows the probes aren't random — not that they detect genuine safety commitment vs idiosyncratic model behavior.\\n\"\n  },\n  {\n    \"name\": \"Lead time analysis across models\",\n    \"description\": \"Evaluate HS probe lead time distributions on all 4 models. Compare HS vs text lead times. Lead time = steps between first detection and commitment point.\\n\",\n    \"results\": {\n      \"r1_8b_hs_lead_mean\": -0.1,\n      \"r1_8b_hs_lead_note\": \"HS detects AT commitment, not before\",\n      \"r1_8b_text_lead_mean\": 10.3,\n      \"r1_8b_text_lead_inflated\": \"high text lead is artifact of high pre-CP FPR (trigger-happy)\",\n      \"ot_7b_hs_lead_mean\": 21.6,\n      \"ot_7b_text_lead_mean\": 45.5,\n      \"ot_7b_lead_note\": \"absolute values inflated by long traces (~80 sentences)\",\n      \"qwq_32b_hs_lead_mean_range\": \"-1.2 to +1.9\",\n      \"qwq_32b_text_lead_mean_range\": \"3.7 to 12.3\",\n      \"qwq_32b_hs_lead_negative\": true,\n      \"qwq_32b_position_baseline_lead\": \"better than HS\",\n      \"r1_32b_hs_lead_mean\": \"+11.7 to +13.3\",\n      \"r1_32b_hs_lead_positive\": true,\n      \"r1_32b_coverage_at_significant_w\": 0.25,\n      \"r1_32b_lead_caveat\": \"only 5/20 traces detected at W=1\",\n      \"gru_r1_8b_lead\": \"+4.5 ± 3.0\",\n      \"gru_r1_8b_worst_seed\": \"+0.9\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Lead Time Comparison: HS vs Text vs Position\",\n        \"columns\": [\n          \"Model\",\n          \"HS Lead (steps)\",\n          \"Text Lead (steps)\",\n          \"Position BA\",\n          \"HS BA\",\n          \"HS > Position?\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B (W=15)\",\n            \"−0.1\",\n            \"+10.3†\",\n            \"—\",\n            \"0.802\",\n            \"—\"\n          ],\n          [\n            \"OT-7B (W=3)\",\n            \"+21.6‡\",\n            \"+45.5‡\",\n            \"—\",\n            \"0.688\",\n            \"—\"\n          ],\n          [\n            \"QwQ-32B (W=3)\",\n            \"−1.2 to +1.9\",\n            \"+3.7 to +12.3\",\n            \"0.746\",\n            \"0.740\",\n            \"No\"\n          ],\n          [\n            \"R1-32B (W=1)\",\n            \"+11.7 to +13.3\",\n            \"—\",\n            \"0.686\",\n            \"0.826\",\n            \"Yes (25% cov)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst-tier reviewers identify lead time as the practical dealbreaker: \\\"The paper claims HS monitoring enables early detection, but 2/4 models show HS detecting LATER than text. The one model with good lead time (R1-32B) detects only 25% of traces. A deployment team would choose text monitoring over HS monitoring for lead time alone, saving the engineering cost of hidden-state extraction.\\\"\\n\\n\\nLead time results are a mixed bag that worst-tier reviewers weaponize: (1) R1-8B HS lead is effectively zero — HS detects AT commitment, not before. Only GRU achieves modest positive lead (+4.5, worst seed +0.9). Text lead of +10.3 is misleadingly high (artifact of trigger-happy detection with 20.5% pre-CP FPR). (2) QwQ-32B: HS lead time is NEGATIVE (-1.2 to +1.9 steps) while text detects 3.7-12.3 steps earlier. Position baseline (bal_acc=0.746) beats HS (bal_acc=0.740). A reviewer writes: \\\"for QwQ, just tracking relative position in the trace outperforms hidden-state monitoring — why bother with white-box access?\\\" (3) R1-32B has excellent HS lead (+13 steps) but only 25% coverage — meaning 15/20 traces are undetected. Reviewer: \\\"a detector that works on 5 traces is an anecdote, not a system.\\\" (4) OT-7B lead times are inflated by long traces. Overall: 2/4 models have HS lead ≤ 0, 1/4 has only 25% coverage, and 1/4 has inflated absolute values. No model presents a clean HS lead time story.\\n\"\n  },\n  {\n    \"name\": \"TrajGuard-style Mahalanobis baseline (all 4 models)\",\n    \"description\": \"Mahalanobis distance on safe-trace covariance across all 4 models. Tests whether geometric distance-based methods (TrajGuard-style) can detect safety commitment.\\n\",\n    \"results\": {\n      \"r1_8b_separation\": 0.07,\n      \"ot_7b_separation\": 0.03,\n      \"r1_32b_separation\": 0.15,\n      \"qwq_32b_separation\": 0.2,\n      \"max_separation_any_model\": 0.2,\n      \"all_models_fail\": true,\n      \"false_alarm_exceeds_tp_all_thresholds\": true,\n      \"signal_location\": \"minor PCA components, not principal directions\",\n      \"r1_8b_safe_md\": 6.66,\n      \"r1_8b_post_md\": 6.73,\n      \"r1_32b_safe_md\": 6.73,\n      \"r1_32b_post_md\": 6.88,\n      \"qwq_32b_safe_md\": 3.22,\n      \"qwq_32b_post_md\": 3.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mahalanobis Distance Separation (4 models)\",\n        \"columns\": [\n          \"Model\",\n          \"Layer\",\n          \"Safe MD\",\n          \"Post-CP MD\",\n          \"Separation\",\n          \"FA ≥ TP?\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"L14\",\n            \"6.66\",\n            \"6.73\",\n            \"+0.07\",\n            \"Yes\"\n          ],\n          [\n            \"OT-7B\",\n            \"L16\",\n            \"7.68\",\n            \"7.71\",\n            \"+0.03\",\n            \"Yes\"\n          ],\n          [\n            \"R1-32B\",\n            \"L63\",\n            \"6.73\",\n            \"6.88\",\n            \"+0.15\",\n            \"Yes\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"L60\",\n            \"3.22\",\n            \"3.42\",\n            \"+0.20\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Universal Mahalanobis failure confirms safety signal is geometrically inaccessible to distance-based methods. But worst-tier reviewers dismiss this: \\\"Showing Mahalanobis doesn't work is a paragraph in a methods section, not a contribution. The field already knows unsupervised geometric methods struggle with fine-grained behavioral distinctions.\\\"\\n\\n\\nMahalanobis distance fails on all 4 models (max separation 0.20 on QwQ, FA rate ≥ TP rate at every threshold). The signal lives in minor PCA components, not principal variance directions — Mahalanobis, which weights by inverse covariance, is structurally blind to this geometry. Worst-tier reviewers have mixed reactions: (1) \\\"Mahalanobis failing is expected — Bolukbasi et al. 2016 and subsequent work showed safety-relevant features are often orthogonal to principal variance. This negative result is predictable, not informative.\\\" (2) \\\"You tested one geometric baseline. What about k-NN distance, local outlier factor, or isolation forests? The negative result space is underexplored.\\\" The finding supports the \\\"existing methods fail\\\" claim but reviewers rate it as incremental — failure of one known-limited baseline is not a contribution.\\n\"\n  },\n  {\n    \"name\": \"Bootstrap confidence intervals + threshold-independent metrics\",\n    \"description\": \"10000 bootstrap resamples on all key metrics across 4 models. Holm-Bonferroni correction. AUROC, precision-recall curves, detection delay CDF.\\n\",\n    \"results\": {\n      \"holm_bonferroni_pass\": \"12/12\",\n      \"r1_8b_precision_delta\": \"+22.4pp\",\n      \"r1_8b_precision_p\": \"<0.001\",\n      \"ot_7b_precision_delta\": \"+21.9pp\",\n      \"ot_7b_precision_p\": \"<0.001\",\n      \"qwq_32b_precision_delta\": \"+23.6pp\",\n      \"qwq_32b_precision_p\": \"<0.001\",\n      \"qwq_32b_fpr_p\": 0.004,\n      \"r1_32b_precision_delta\": \"+15.4pp\",\n      \"r1_32b_precision_p\": \"<0.001\",\n      \"r1_32b_fpr_p\": 0.007,\n      \"r1_32b_fpr_marginal_note\": \"p=0.007 passes HB threshold 0.025 but barely\",\n      \"marginal_tests_count\": 2,\n      \"all_precision_deltas_positive\": true,\n      \"precision_range\": \"+15.4 to +23.6pp\",\n      \"r1_32b_ci_width_ba\": \"~0.15\",\n      \"qwq_32b_ci_width_ba\": \"~0.12\",\n      \"r1_8b_ci_width_ba\": \"~0.06\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Holm-Bonferroni Summary (12/12, α=0.05)\",\n        \"columns\": [\n          \"Rank\",\n          \"Model\",\n          \"Metric\",\n          \"p-value\",\n          \"HB Threshold\",\n          \"Pass\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"R1-8B\",\n            \"precision\",\n            \"<0.001\",\n            \"0.0042\",\n            \"✅\"\n          ],\n          [\n            2,\n            \"OT-7B\",\n            \"bal_acc\",\n            \"<0.001\",\n            \"0.0045\",\n            \"✅\"\n          ],\n          [\n            3,\n            \"OT-7B\",\n            \"precision\",\n            \"<0.001\",\n            \"0.0050\",\n            \"✅\"\n          ],\n          [\n            4,\n            \"OT-7B\",\n            \"FPR\",\n            \"<0.001\",\n            \"0.0056\",\n            \"✅\"\n          ],\n          [\n            5,\n            \"QwQ\",\n            \"bal_acc\",\n            \"<0.001\",\n            \"0.0063\",\n            \"✅\"\n          ],\n          [\n            6,\n            \"QwQ\",\n            \"precision\",\n            \"<0.001\",\n            \"0.0071\",\n            \"✅\"\n          ],\n          [\n            7,\n            \"R1-32B\",\n            \"bal_acc\",\n            \"<0.001\",\n            \"0.0083\",\n            \"✅\"\n          ],\n          [\n            8,\n            \"R1-32B\",\n            \"precision\",\n            \"<0.001\",\n            \"0.0100\",\n            \"✅\"\n          ],\n          [\n            9,\n            \"QwQ\",\n            \"FPR\",\n            \"0.004\",\n            \"0.0125\",\n            \"✅\"\n          ],\n          [\n            10,\n            \"R1-8B\",\n            \"bal_acc\",\n            \"0.005\",\n            \"0.0167\",\n            \"✅\"\n          ],\n          [\n            11,\n            \"R1-32B\",\n            \"FPR\",\n            \"0.007\",\n            \"0.0250\",\n            \"✅\"\n          ],\n          [\n            12,\n            \"R1-8B\",\n            \"FPR\",\n            \"0.044\",\n            \"0.0500\",\n            \"✅\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Statistical significance is established but reviewers find it insufficient: \\\"The paper's statistical methodology is sound, but the story it tells is 'HS is significantly better by 15-24pp precision at best-case layer/window selection.' For an EMNLP Main paper, we need either (a) a novel method that achieves these gains, or (b) a surprising finding. Neither: linear probes on hidden states are standard, and it's unsurprising they outperform text embeddings (hidden states are an information superset of text).\\\"\\n\\n\\nAll 12/12 tests pass Holm-Bonferroni, which is statistically clean. But worst-tier reviewers attack the PRACTICAL significance, not the statistical significance: (1) \\\"Of course 12/12 pass — you selected the best layer AND the best window per model, then tested. The researcher degrees of freedom (4 models × 64 layers × 7 windows × 5 metrics) dwarf the 12 tests corrected for.\\\" (2) \\\"The CIs for 32B models are extremely wide (±0.15 for R1-32B bal_acc). Statistical significance with n=20 means the effect is large, but the PRECISION of the estimate is poor. You know HS is better somewhere between +3pp and +34pp — that's not actionable.\\\" (3) \\\"R1-32B FPR p=0.007 and QwQ FPR p=0.004 are the most marginal passing tests. A 10001st bootstrap replicate could flip either.\\\" (4) \\\"Holm-Bonferroni corrects for 12 tests, but the true multiplicity (including layer/window selection) is orders of magnitude larger.\\\"\\n\"\n  },\n  {\n    \"name\": \"Window size ablation (W=1,3,5,10,15,20,25 on all models)\",\n    \"description\": \"Systematic window size sweep on all 4 models. Characterize precision-coverage tradeoff and identify optimal W per model.\\n\",\n    \"results\": {\n      \"coverage_decreases_with_w_all_models\": true,\n      \"precision_increases_with_w_all_models\": true,\n      \"fpr_decreases_with_w_all_models\": true,\n      \"r1_8b_best_bal_acc_w\": 25,\n      \"r1_8b_w25_precision\": 0.822,\n      \"r1_8b_w25_coverage\": 0.488,\n      \"r1_8b_w25_fpr_step\": 0.048,\n      \"r1_32b_best_bal_acc_w\": 10,\n      \"r1_32b_w10_precision\": 0.609,\n      \"r1_32b_w10_coverage\": 0.7,\n      \"r1_32b_w10_fpr_step\": 0.234,\n      \"qwq_32b_best_bal_acc_w\": 25,\n      \"qwq_32b_w25_precision\": 0.618,\n      \"qwq_32b_w25_coverage\": 0.579,\n      \"qwq_32b_w25_fpr_step\": 0.169,\n      \"ot_7b_hs_peaks_w3\": true,\n      \"ot_7b_w3_bal_acc\": 0.688,\n      \"ot_7b_w25_bal_acc\": 0.659,\n      \"tradeoff_universal\": \"larger W → higher precision, lower coverage, lower FPR\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Precision-Coverage Tradeoff Summary (all 4 models)\",\n        \"columns\": [\n          \"Model\",\n          \"W=1 Prec/Cov\",\n          \"W=3 Prec/Cov\",\n          \"W=15 Prec/Cov\",\n          \"W=25 Prec/Cov\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.693/0.721\",\n            \"0.723/0.698\",\n            \"0.777/0.512\",\n            \"0.822/0.488\"\n          ],\n          [\n            \"OT-7B\",\n            \"—/—\",\n            \"0.466/0.532\",\n            \"—/—\",\n            \"—/—\"\n          ],\n          [\n            \"R1-32B\",\n            \"0.549/0.800\",\n            \"0.560/0.800\",\n            \"0.591/0.700\",\n            \"0.566/0.700\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"0.544/0.789\",\n            \"0.565/0.737\",\n            \"0.582/0.684\",\n            \"0.618/0.579\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ablation confirms the tradeoff is universal but no operating point achieves both high precision AND high coverage. Worst-tier reviewer: \\\"Table 3 is the paper's most honest result. At no window size does any model achieve >0.7 precision AND >0.6 coverage simultaneously. This is not a tuning problem — it's a fundamental performance ceiling.\\\"\\n\\n\\nWindow ablation reveals a clean precision-sensitivity tradeoff that holds across all models. Worst-tier reviewers dismiss this: (1) \\\"The coverage-decreasing-with-W finding is trivially expected — requiring K=5 consecutive crossings with a larger window means fewer traces reach the threshold. This is a property of the detection criterion K, not an insight about temporal probing.\\\" (2) \\\"The optimal W varies by model (W=3 for OT-7B, W=10 for R1-32B, W=25 for QwQ and R1-8B). This means W is another model-specific hyperparameter to tune — combined with layer selection, you need per-model layer AND window tuning. The 'systematic evaluation' framing hides the fact that this is just exhaustive grid search.\\\" (3) \\\"At the best W per model, coverage ranges from 49% (R1-8B) to 70% (R1-32B). Missing 30-50% of safety commitment events is not deployment-ready.\\\"\\n\"\n  },\n  {\n    \"name\": \"Layer selection ablation (5 metrics × 4 models)\",\n    \"description\": \"Evaluate all layers with temporal probes on 32B models under 5 different selection metrics. Demonstrate crossing_rate bias and metric-dependent layer selection.\\n\",\n    \"results\": {\n      \"crossing_rate_selects_shallow_32b\": true,\n      \"pure_bal_acc_selects_middle_32b\": true,\n      \"threshold_dependent_select_deep_32b\": true,\n      \"qwq_l2_vs_l60_precision_gain\": \"+11.5pp\",\n      \"r1_32b_l10_vs_l63_precision_gain\": \"+4.1pp\",\n      \"loo_cv_stability\": \"65-68% dominant fold\",\n      \"r1_8b_consistent\": true,\n      \"ot_7b_varied\": true,\n      \"bal_acc_layer_vs_precision_layer_diverge_32b\": true,\n      \"qwq_l30_bal_acc\": 0.751,\n      \"qwq_l60_bal_acc\": 0.71,\n      \"r1_32b_l47_bal_acc\": 0.829,\n      \"r1_32b_l63_bal_acc\": 0.759,\n      \"ba_optimal_different_from_precision_optimal\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Metric × Model → Selected Layer (with HS-Text precision delta)\",\n        \"columns\": [\n          \"Metric\",\n          \"R1-8B Layer (ΔPrec)\",\n          \"OT-7B Layer (ΔPrec)\",\n          \"QwQ Layer (ΔPrec)\",\n          \"R1-32B Layer (ΔPrec)\"\n        ],\n        \"rows\": [\n          [\n            \"bal_acc × cr\",\n            \"L0 (+var)\",\n            \"L0 (+var)\",\n            \"L2 (+5.8pp NS)\",\n            \"L10 (+9.4pp NS)\"\n          ],\n          [\n            \"pure bal_acc\",\n            \"L12 (+17.8pp)\",\n            \"L9 (+25.4pp)\",\n            \"L30 (+18.0pp)\",\n            \"L47 (+13.7pp)\"\n          ],\n          [\n            \"precision\",\n            \"L16 (+22.4pp)\",\n            \"L16 (+21.9pp)\",\n            \"L60 (+23.6pp)\",\n            \"L63 (+15.4pp)\"\n          ],\n          [\n            \"pre_cp_fpr\",\n            \"L16 (−7.4pp)\",\n            \"L16 (−17.1pp)\",\n            \"L60 (−9.8pp)\",\n            \"L63 (−14.6pp)\"\n          ],\n          [\n            \"composite\",\n            \"L16 (+22.4pp)\",\n            \"L12 (+var)\",\n            \"L60 (+23.6pp)\",\n            \"L63 (+15.4pp)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ablation is thorough but worst-tier reviewers question whether it constitutes a contribution: \\\"Sensitivity analysis is a sanity check, not a finding. The paper would be better if it had used the right metric from the start and reported results at correct layers — making the sensitivity analysis unnecessary for the paper's core claims.\\\"\\n\\n\\nThe layer selection ablation reveals a genuine pattern (biased metric → shallow layers → masked HS advantage), but worst-tier reviewers split on its significance: (1) The supportive reading: \\\"This is a useful observation — researchers using bal_acc × crossing_rate will get misleading results.\\\" (2) The dismissive reading (dominant in worst tier): \\\"This is expected behavior of a poorly chosen metric. The composite bal_acc × crossing_rate was never standard — it's the authors' own construction (or a rare one). Showing it's bad doesn't advance the field because nobody was using it.\\\" (3) The circularity concern: \\\"You select layers by precision/FPR, then evaluate by precision/FPR. The D044 BA-layer robustness check partially addresses this (16/16 HB pass on BA-selected layers), but the reviewer asks: 'if BA-selected layers also show HS advantage, why not just use BA selection? What's the contribution of the 5-metric comparison?'\\\" (4) \\\"LOO-CV stability of 65-68% means 32-35% of folds select a DIFFERENT layer. This is not the 'robust selection' the paper claims.\\\"\\n\"\n  },\n  {\n    \"name\": \"16-label taxonomy supervision\",\n    \"description\": \"Train probes with fine-grained safety labels (Type 1/2/3/4 × pre/post) instead of binary commitment. Evaluate whether richer supervision improves detection.\\n\",\n    \"results\": {\n      \"r1_8b_16label_acc\": 0.41,\n      \"r1_8b_binary_collapse_acc\": 0.825,\n      \"r1_8b_binary_collapse_delta\": \"+0.8pp\",\n      \"ot_7b_16label_acc\": 0.35,\n      \"ot_7b_binary_collapse_delta\": \"+1.1pp\",\n      \"r1_32b_16label_acc\": 0.28,\n      \"r1_32b_binary_collapse_delta\": \"+0.6pp\",\n      \"qwq_32b_16label_acc\": 0.26,\n      \"qwq_32b_binary_collapse_delta\": \"+0.9pp\",\n      \"fine_grained_improvement_marginal\": true,\n      \"max_collapse_delta\": \"+1.1pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"16-Label vs Binary Supervision\",\n        \"columns\": [\n          \"Model\",\n          \"Binary Acc\",\n          \"16-Label Acc\",\n          \"16→Binary Collapse\",\n          \"Δ vs Binary\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.817\",\n            \"0.41\",\n            \"0.825\",\n            \"+0.8pp\"\n          ],\n          [\n            \"OT-7B\",\n            \"0.688\",\n            \"0.35\",\n            \"0.699\",\n            \"+1.1pp\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"0.740\",\n            \"0.26\",\n            \"0.749\",\n            \"+0.9pp\"\n          ],\n          [\n            \"R1-32B\",\n            \"0.826\",\n            \"0.28\",\n            \"0.832\",\n            \"+0.6pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-grained supervision dead-end. Worst-tier implication: \\\"The information ceiling for linear probes on single-layer hidden states is fundamentally limited. Trying harder with better labels or more metrics can't overcome this.\\\"\\n\\n\\nFine-grained supervision provides marginal benefit (+0.6-1.1pp after binary collapse) across all models. The 16-class accuracy is low (26-41%) because the classes are imbalanced and transition types are not cleanly separable in hidden-state space. Worst-tier reviewers react: (1) \\\"Marginal improvement from richer supervision confirms the probe is already extracting most of the available linear signal in binary mode. This supports the reviewer's argument that linear probes are saturated — not that the methodology is optimal, but that the information ceiling is low.\\\" (2) \\\"The 16-label experiment was motivated by reviewer concern about 'underusing available supervision,' but the result shows supervision quality doesn't matter much. This undermines the paper's implicit argument that careful methodology (layer selection, temporal context) is what matters — it seems the representation quality is the binding constraint.\\\"\\n\"\n  },\n  {\n    \"name\": \"Oracle decomposition\",\n    \"description\": \"Analyze what the oracle label sequence encodes that hidden-state probes cannot access. Compare oracle lead (+31 steps on R1-8B) to probe lead (~0 steps).\\n\",\n    \"results\": {\n      \"r1_8b_oracle_lead\": \"+31.0\",\n      \"r1_8b_best_probe_lead\": \"+4.5 (GRU)\",\n      \"r1_8b_oracle_gap\": \"26.5\",\n      \"r1_8b_label_autocorr_pre_cp\": 0.82,\n      \"r1_8b_hs_autocorr_pre_cp\": 0.95,\n      \"label_entropy_pre_cp_r1_8b\": 1.38,\n      \"hs_entropy_pre_cp_r1_8b\": 0.41,\n      \"r1_32b_oracle_lead\": \"+28\",\n      \"r1_32b_best_probe_lead\": \"+13 (W=1, 25% cov)\",\n      \"qwq_oracle_lead\": \"+27\",\n      \"qwq_best_probe_lead\": \"−1.2 to +1.9\",\n      \"pattern_finding\": \"Labels show gradual safety erosion pre-CP; hidden states show step-function at CP\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Oracle vs Best Probe Lead Time\",\n        \"columns\": [\n          \"Model\",\n          \"Oracle Lead\",\n          \"Best Probe Lead\",\n          \"Method\",\n          \"Gap\",\n          \"Hidden State Entropy (pre-CP)\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"+31.0\",\n            \"+4.5\",\n            \"GRU multi-layer\",\n            \"26.5\",\n            \"0.41\"\n          ],\n          [\n            \"OT-7B\",\n            \"~+30\",\n            \"+33.6 (GRU)\",\n            \"GRU multi-layer\",\n            \"~0†\",\n            \"—\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"+27\",\n            \"−1.2 to +1.9\",\n            \"temporal LR\",\n            \"25-28\",\n            \"—\"\n          ],\n          [\n            \"R1-32B\",\n            \"+28\",\n            \"+13.3\",\n            \"temporal LR W=1\",\n            \"15 (25% cov)\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The oracle decomposition is the worst-tier's strongest negative finding: hidden states are fundamentally reactive (encoding current state) rather than predictive (encoding trajectory). Reviewer: \\\"This paper demonstrates that hidden-state monitoring is a lagging indicator. For safety deployment, you need leading indicators. Text-based trajectory analysis, while noisier, is the better research direction.\\\"\\n\\n\\nOracle decomposition reveals a 26-28 step gap between what's detectable in labels vs hidden states. The label sequence shows gradual pre-CP patterns (increasing unsafe-adjacent labels, shortening safe streaks) that hidden states don't track. Worst-tier reviewers draw a harsh conclusion: \\\"The 31-step oracle lead proves that safety commitment is a GRADUAL process visible in the model's outputs. But the hidden-state probe can only detect it at or after the commitment point (lead ≈ 0). This means hidden states encode the CURRENT safety state but not the TRAJECTORY toward commitment. For deployment, trajectory prediction is what matters — catching the commitment after it happens is too late. The oracle gap is not a puzzle for Discussion; it's evidence that the entire hidden-state monitoring approach is fundamentally limited. Text-based monitoring that tracks reasoning trajectory (even with higher FPR) provides earlier warning.\\\"\\n\"\n  },\n  {\n    \"name\": \"OpenThinker-7B (Qwen2.5-7B, STILL-trained)\",\n    \"description\": \"4th model completing the 2×2 architecture×scale matrix. Full pipeline: layer sweep, temporal probes, HS vs text comparison, GRU, selectivity control task.\\n\",\n    \"results\": {\n      \"best_layer\": 16,\n      \"best_layer_depth_pct\": 57.1,\n      \"best_hs_bal_acc_w3\": 0.688,\n      \"best_hs_precision_w3\": 0.466,\n      \"best_hs_pre_cp_fpr\": 0.1,\n      \"bootstrap_3_of_3_hb\": true,\n      \"bootstrap_bal_acc_delta\": \"+10.7pp\",\n      \"bootstrap_precision_delta\": \"+21.9pp\",\n      \"bootstrap_fpr_delta\": \"−17.1pp\",\n      \"selectivity_pp\": 18.3,\n      \"n_traces\": 228,\n      \"gru_multi_bal_acc\": 0.746,\n      \"gru_multi_lead\": \"+33.6\",\n      \"gru_multi_fpr\": 0.274,\n      \"hs_temporal_saturation_w3\": true,\n      \"text_temporal_w25_best\": 0.614\n    },\n    \"tables\": [\n      {\n        \"name\": \"OT-7B Full Pipeline Summary\",\n        \"columns\": [\n          \"Method\",\n          \"bal_acc\",\n          \"precision\",\n          \"pre-CP FPR\",\n          \"coverage\",\n          \"lead\"\n        ],\n        \"rows\": [\n          [\n            \"HS temporal W=3 L16\",\n            \"0.688\",\n            \"0.466\",\n            \"0.100\",\n            \"0.532\",\n            \"+21.6\"\n          ],\n          [\n            \"Text temporal W=25\",\n            \"0.614\",\n            \"0.329\",\n            \"0.161\",\n            \"0.660\",\n            \"+45.5\"\n          ],\n          [\n            \"GRU multi L13-19\",\n            \"0.746\",\n            \"—\",\n            \"0.274\",\n            \"0.645\",\n            \"+33.6\"\n          ],\n          [\n            \"HS-Text Δ (HB)\",\n            \"+10.7pp ✅\",\n            \"+21.9pp ✅\",\n            \"−17.1pp ✅\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OT-7B strengthens the 7-8B story but worst-tier reviewers note: \\\"The 2×2 matrix now has two strong cells (7-8B) and two weak cells (32B). The paper's breadth claim ('4 models') is technically true but misleading — 2/4 models have serious practical caveats that make the HS advantage non-deployable.\\\"\\n\\n\\nOT-7B is the cleanest single-model evidence for HS advantage (3/3 HB, highest selectivity 18.3pp, largest n=228 traces). But worst-tier reviewers are unimpressed by adding a 4th model that confirms the known pattern: (1) \\\"A 4th model at 7B showing the same result doesn't address the 32B caveats. The paper already has two 7-8B models that work. The question is whether HS monitoring scales, and OT-7B can't answer that.\\\" (2) \\\"OT-7B has its own caveats: HS temporal saturation at W=3 (bal_acc declines at larger W), and absolute performance is still below R1-8B (best bal_acc 68.8% vs 80.2%). The 'cleanest evidence' is still only 69% balanced accuracy — barely better than a biased coin.\\\" (3) \\\"GRU lead time of +33.6 steps sounds impressive until you note OT-7B traces average ~80 sentences — normalize by trace length and the lead time fraction is similar to other models.\\\" (4) \\\"FPR of 27.4% for GRU means ~1 in 4 safe steps triggers the detector. At 80-sentence traces, that's ~20 false alarms per safe trace.\\\"\\n\"\n  },\n  {\n    \"name\": \"GRU/Attention probe upper bound (32B models)\",\n    \"description\": \"GRU sequence model on 32B models at corrected layers. Tests whether nonlinear sequence modeling can recover signal that linear temporal probes miss.\\n\",\n    \"results\": {\n      \"r1_32b_gru_single_bal_acc\": 0.675,\n      \"r1_32b_gru_multi_bal_acc\": 0.655,\n      \"r1_32b_gru_lead_mean\": \"+8.8 to +9.1\",\n      \"r1_32b_gru_fpr\": \"0.114 to 0.135\",\n      \"r1_32b_gru_coverage\": \"0.23 to 0.30\",\n      \"r1_32b_gru_vs_lr_delta\": \"−6pp bal_acc (GRU worse)\",\n      \"qwq_32b_gru_single_bal_acc\": 0.694,\n      \"qwq_32b_gru_multi_bal_acc\": 0.724,\n      \"qwq_32b_gru_lead_mean\": \"+15.9\",\n      \"qwq_32b_gru_fpr\": 0.289,\n      \"qwq_32b_gru_coverage\": 0.84,\n      \"qwq_32b_gru_vs_lr_delta\": \"−3.7pp bal_acc (GRU worse at bal_acc, better at coverage)\",\n      \"ot_7b_gru_multi_bal_acc\": 0.746,\n      \"ot_7b_gru_multi_lead\": \"+33.6\",\n      \"ot_7b_gru_fpr\": 0.274,\n      \"gru_worse_than_lr_3_of_4\": true,\n      \"gru_note\": \"GRU trades accuracy for coverage/lead — higher FPR drives earlier detection\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"GRU vs Temporal LR (32B models, corrected layers)\",\n        \"columns\": [\n          \"Model\",\n          \"LR bal_acc\",\n          \"GRU bal_acc\",\n          \"Δ\",\n          \"GRU FPR\",\n          \"LR FPR\"\n        ],\n        \"rows\": [\n          [\n            \"R1-32B (L63 W=10)\",\n            \"0.737\",\n            \"~0.675\",\n            \"−6.2pp\",\n            \"0.135\",\n            \"0.234\"\n          ],\n          [\n            \"QwQ-32B (L60 W=5)\",\n            \"0.761\",\n            \"0.724\",\n            \"−3.7pp\",\n            \"0.289\",\n            \"0.217\"\n          ],\n          [\n            \"OT-7B (L16 multi)\",\n            \"0.688\",\n            \"0.746\",\n            \"+5.8pp\",\n            \"0.274\",\n            \"0.100\"\n          ],\n          [\n            \"R1-8B (L14 multi)\",\n            \"0.806\",\n            \"0.809\",\n            \"+0.3pp\",\n            \"0.165\",\n            \"0.097\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GRU fails to improve over LR on most models, confirming linear probes are at the information ceiling. Worst-tier reviewer: \\\"The paper's headline is 'HS beats text.' The method is logistic regression. The contribution is... careful hyperparameter selection? This is a well-executed experiment report, not a methods paper.\\\"\\n\\n\\nGRU does NOT outperform temporal LR on balanced accuracy for 3/4 models. On R1-32B (n=20 test), GRU severely overfits — bal_acc drops 6pp below LR. On QwQ, GRU achieves higher coverage and lead time but at 2× the FPR. This confirms linear probes are sufficient (or even superior given small samples). Worst-tier reviewers use this to attack novelty: \\\"The paper's method is logistic regression on hidden states with a sliding window. That's not a contribution — it's the simplest possible baseline. The fact that GRU and MLP don't help confirms the method space is trivial, which means the paper's 'systematic comparison of 7 methods' is comparing variations of the obvious approach (linear probe) against methods that were never designed for this task (Mahalanobis, BOCPD, CCS). The negative results are predictable, not informative.\\\"\\n\"\n  },\n  {\n    \"name\": \"Text-based baseline (sentence embeddings + temporal LR)\",\n    \"description\": \"Sentence-BERT (all-MiniLM-L6-v2) embeddings + temporal window LR on CoT text of all 4 models. Critical comparison establishing what text monitoring achieves without hidden-state access.\\n\",\n    \"results\": {\n      \"r1_8b_text_static_acc\": 0.661,\n      \"r1_8b_text_temporal_w15_acc\": 0.678,\n      \"r1_8b_text_temporal_w15_auroc\": 0.759,\n      \"r1_8b_hs_acc_advantage\": \"+15-18pp\",\n      \"ot_7b_text_best_bal_acc\": 0.614,\n      \"ot_7b_text_best_precision\": 0.329,\n      \"ot_7b_text_best_fpr\": 0.161,\n      \"qwq_32b_text_temporal_bal_acc\": 0.65,\n      \"qwq_32b_text_precision\": 0.421,\n      \"r1_32b_text_temporal_bal_acc\": 0.646,\n      \"r1_32b_text_precision\": 0.45,\n      \"hs_vs_text_precision_gap_range\": \"+15.4 to +23.6pp\",\n      \"text_requires_zero_infra_change\": true,\n      \"text_precision_all_models\": \"0.329-0.487\",\n      \"hs_precision_all_models\": \"0.466-0.776\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"HS vs Text Precision Gap (+ engineering cost annotation)\",\n        \"columns\": [\n          \"Model\",\n          \"HS Precision\",\n          \"Text Precision\",\n          \"Δ\",\n          \"HS Infra Cost\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.777 (W=15)\",\n            \"0.487 (W=15)\",\n            \"+29.0pp\",\n            \"white-box, L14\"\n          ],\n          [\n            \"OT-7B\",\n            \"0.466 (W=3)\",\n            \"0.329 (W=25)\",\n            \"+13.7pp\",\n            \"white-box, L16\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"0.578 (W=3)\",\n            \"0.421 (W=best)\",\n            \"+15.7pp\",\n            \"white-box, L60\"\n          ],\n          [\n            \"R1-32B\",\n            \"0.603 (W=1)\",\n            \"0.450 (W=best)\",\n            \"+15.3pp\",\n            \"white-box, L63\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The text baseline is the worst-tier reviewer's strongest weapon: \\\"A 15-24pp precision gain sounds meaningful until you consider: (a) text monitoring costs $0 in infrastructure, (b) HS monitoring requires white-box access + per-model tuning, (c) the BGE-large result shows the gap shrinks with better text encoders, (d) safe FPR is 39-62% regardless of modality — both approaches produce unusable false alarm rates. The paper should honestly state: 'HS probes are measurably but marginally better than text probes. Whether the margin justifies white-box access depends on deployment constraints. For most practical settings, text monitoring suffices.'\\\"\\n\\n\\nText baseline performs consistently across all models (bal_acc 0.61-0.68, precision 0.33-0.49). HS probes outperform by +15-24pp precision, which is statistically significant (12/12 HB). But worst-tier reviewers attack the COST-BENEFIT ratio, not the statistical claim: (1) \\\"Text probes need zero infrastructure change — you monitor the CoT output that's already available. HS probes require white-box access to model internals, which means: (a) running the model locally (can't use API), (b) modifying the inference pipeline to extract intermediate activations, (c) per-model layer selection + probe training. The 15-24pp precision gain comes at enormous engineering cost.\\\" (2) \\\"At 33-49% text precision, you get 1 true alarm per 2-3 triggers. At 47-78% HS precision, you get 1 per 1.3-2.1 triggers. Is that difference worth instrumenting your entire inference stack? For most deployment teams, no.\\\" (3) \\\"Text probes improve with better embeddings (BGE-large, domain-fine-tuned). The paper tested only all-MiniLM-L6-v2 — the weakest common baseline. A reviewer notes: 'Use GPT-4 as the text classifier and the gap likely narrows to <5pp.'\\\" (4) \\\"The BGE-large comparison (exp_bge_large_text_comparison) showed only 1/4 HB pass for HS vs BGE-large — the gap narrows significantly with a better text encoder.\\\"\\n\"\n  },\n  {\n    \"name\": \"BOCPD/CUSUM on all 4 models\",\n    \"description\": \"Bayesian Online Change-Point Detection + CUSUM on probe score sequences. Tests whether advanced change-point methods can achieve positive lead time.\\n\",\n    \"results\": {\n      \"r1_8b_bocpd_detection\": 0.93,\n      \"r1_8b_bocpd_lead\": \"+3.45\",\n      \"r1_8b_cusum_lead\": \"+0.89\",\n      \"r1_8b_fcp_baseline_lead\": \"+4.89\",\n      \"r1_8b_fcp_beats_bocpd_on_lead\": true,\n      \"ot_7b_bocpd_detection\": 0.0,\n      \"ot_7b_bocpd_note\": \"W=3 probe scores too spiky, Gaussian model fails\",\n      \"ot_7b_fcp_best_detection\": 0.894,\n      \"ot_7b_fcp_best_lead\": \"+11.83\",\n      \"r1_32b_bocpd_detection\": 0.0,\n      \"qwq_32b_bocpd_detection\": 0.0,\n      \"r1_32b_cusum_detection\": 0.85,\n      \"r1_32b_cusum_lead\": \"+2.59\",\n      \"qwq_32b_cusum_detection\": 0.737,\n      \"qwq_32b_cusum_lead\": \"+9.86\",\n      \"bocpd_works_only_r1_8b\": true,\n      \"cusum_universally_worse_than_fcp\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Change-Point Detection Cross-Model Summary\",\n        \"columns\": [\n          \"Model\",\n          \"BOCPD Det%\",\n          \"BOCPD Lead\",\n          \"CUSUM Det%\",\n          \"CUSUM Lead\",\n          \"FCP Det%\",\n          \"FCP Lead\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"93%\",\n            \"+3.45\",\n            \"65%\",\n            \"+0.89\",\n            \"65%\",\n            \"+4.89\"\n          ],\n          [\n            \"OT-7B\",\n            \"0%\",\n            \"—\",\n            \"75%†\",\n            \"+7.46†\",\n            \"89%\",\n            \"+11.83\"\n          ],\n          [\n            \"R1-32B\",\n            \"0%\",\n            \"—\",\n            \"85%\",\n            \"+2.59\",\n            \"95%\",\n            \"+5.68\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"0%\",\n            \"—\",\n            \"74%\",\n            \"+9.86\",\n            \"79%\",\n            \"+9.40\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Complete BOCPD failure on 3/4 models and CUSUM inferiority to simple thresholding. Worst-tier reviewer: \\\"The paper tests two change-point algorithms that were designed for very different signal types, finds they don't work, and claims this as a negative result. But the method selection is so narrow that the negative result is uninformative — you tested the wrong tools.\\\"\\n\\n\\nBOCPD fails on 3/4 models (0% detection on OT-7B, R1-32B, QwQ). Only R1-8B works (93%) because R1-8B has gradual probe score transitions that match BOCPD's Gaussian change-point model. Other models have abrupt transitions (OT-7B) or weak signals (32B) that BOCPD's parametric assumptions can't handle. CUSUM detects some traces but with worse lead than simple first-crossing-point (FCP) threshold. Worst-tier reviewers: (1) \\\"BOCPD and CUSUM were never designed for this signal type. Testing them is due diligence, but their failure is predictable — these methods assume stationary-then-shifted Gaussian data, while probe scores are bounded [0,1] and often spiky.\\\" (2) \\\"The negative result strengthens the 'nothing works well' narrative, but the method selection is questionable. Why not test HMM, Viterbi decoding, or learned change-point detectors? The paper tests 2 off-the-shelf methods and declares change-point detection a dead end.\\\" (3) \\\"Simple FCP threshold beats BOCPD on mean lead time for R1-8B. The 'advanced' methods add nothing.\\\"\\n\"\n  },\n  {\n    \"name\": \"False positive analysis (safe trace FPR, all methods)\",\n    \"description\": \"Run all probes on safe traces (final_judgment=0.5) across all 4 models. Report safe FPR, pre-CP FPR, precision, and precision-recall curves.\\n\",\n    \"results\": {\n      \"r1_8b_hs_safe_fpr\": 0.39,\n      \"r1_8b_text_safe_fpr\": 0.385,\n      \"ot_7b_hs_safe_fpr\": \"0.111-0.175\",\n      \"ot_7b_text_safe_fpr\": \"0.302-0.460\",\n      \"qwq_32b_hs_safe_fpr\": \"0.45-0.50\",\n      \"qwq_32b_text_safe_fpr\": \"0.325-0.425\",\n      \"r1_32b_hs_safe_fpr\": 0.239,\n      \"r1_32b_text_safe_fpr\": 0.31,\n      \"safe_fpr_range_all\": \"0.111 to 0.521\",\n      \"safe_fpr_median\": \"~0.39\",\n      \"gru_safe_fpr\": 0.521,\n      \"gru_highest_fpr_note\": \"GRU trades precision for coverage → highest FPR\",\n      \"precision_all_methods_range\": \"0.329 to 0.777\",\n      \"no_method_achieves_80pct_precision\": true,\n      \"deployment_threshold_precision_70\": \"only R1-8B HS W≥15 exceeds\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Safe Trace FPR Summary (all methods × all models)\",\n        \"columns\": [\n          \"Model\",\n          \"HS Static FPR\",\n          \"HS Temporal FPR\",\n          \"Text Temporal FPR\",\n          \"GRU FPR\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.390\",\n            \"0.392\",\n            \"0.385\",\n            \"0.521\"\n          ],\n          [\n            \"OT-7B\",\n            \"0.111\",\n            \"0.175\",\n            \"0.460\",\n            \"—\"\n          ],\n          [\n            \"QwQ-32B\",\n            \"0.500\",\n            \"0.450\",\n            \"0.425\",\n            \"—\"\n          ],\n          [\n            \"R1-32B\",\n            \"0.239\",\n            \"0.239\",\n            \"0.310\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Deployment Viability Assessment\",\n        \"columns\": [\n          \"Criterion\",\n          \"Threshold\",\n          \"Models Meeting Criterion\",\n          \"Best Method\"\n        ],\n        \"rows\": [\n          [\n            \"Safe FPR < 20%\",\n            \"0.20\",\n            \"1/4 (OT-7B HS static)\",\n            \"HS static L16\"\n          ],\n          [\n            \"Precision > 70%\",\n            \"0.70\",\n            \"1/4 (R1-8B W≥15)\",\n            \"HS temporal W=25\"\n          ],\n          [\n            \"Coverage > 60%\",\n            \"0.60\",\n            \"2/4 (R1-8B W≤3, R1-32B W≤3)\",\n            \"HS temporal W=1\"\n          ],\n          [\n            \"All three criteria\",\n            \"—\",\n            \"0/4\",\n            \"None\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"FPR analysis is the worst-tier's core evidence for the \\\"not practically useful\\\" dismissal. No model meets all three deployment criteria simultaneously. The best model (R1-8B) achieves >70% precision only at W≥15 where coverage drops to 49%. The paper's deployment framing is untenable. Reframing guidance: \\\"Position as diagnostic/research tool, explicitly disclaim deployment readiness. Lead with 'none of our 7 methods achieves deployment-ready performance' as a cautionary finding.\\\"\\n\\n\\nSafe FPR ranges from 11% (OT-7B HS static, best case) to 52% (GRU, worst case), with a median around 39%. This is the worst-tier dealbreaker. Reviewer calculation: \\\"At 39% safe FPR with K=5 consecutive crossings for trace-level detection, a 40-step safe trace has ~39% probability of triggering the detector. In a production system processing 1000 safe traces per day, that's ~390 false alarms daily. Each requires human review at ~5 minutes → 32.5 person-hours/day of false alarm triage. No deployment team would accept this.\\\" Even the best case (OT-7B HS 11.1% safe FPR) means 111 false alarms per 1000 safe traces. The worst-tier reviewer's verdict: \\\"A safety monitor that fires on 1 in 3 to 1 in 2 safe traces is not a monitor — it's a random noise generator. The paper should lead with this limitation, not bury it.\\\" QwQ-32B is particularly problematic: HS safe FPR (45-50%) is HIGHER than text safe FPR (33-43%), meaning HS monitoring generates MORE false alarms on safe traces for QwQ.\\n\"\n  },\n  {\n    \"name\": \"5-fold CV validation of multi-metric ensemble (7-8B)\",\n    \"description\": \"Cross-validated ensemble of metric-weighted layer selections on R1-8B and OT-7B. Validates that multi-metric ensemble eliminates layer selection bias under proper CV.\\n\",\n    \"results\": {\n      \"r1_8b_ensemble_cv_prec\": 0.565,\n      \"r1_8b_best_single_cv_prec\": 0.604,\n      \"r1_8b_ensemble_vs_text_gap\": \"+19.3pp\",\n      \"r1_8b_ensemble_vs_text_p\": \"<0.002\",\n      \"ot_7b_ensemble_cv_prec\": 0.506,\n      \"ot_7b_best_single_cv_prec\": 0.473,\n      \"ot_7b_ensemble_beats_best_single\": true,\n      \"ot_7b_ensemble_beats_best_single_p\": 0.033,\n      \"cv_validates_preliminary\": true,\n      \"cv_acceptance_probability_delta\": \"+0.01 to +0.03\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Ensemble CV Results (7-8B models)\",\n        \"columns\": [\n          \"Model\",\n          \"Ensemble Prec\",\n          \"Best Single Prec\",\n          \"Text Prec\",\n          \"Ens vs Text p\"\n        ],\n        \"rows\": [\n          [\n            \"R1-8B\",\n            \"0.565\",\n            \"0.604\",\n            \"0.372\",\n            \"<0.002\"\n          ],\n          [\n            \"OT-7B\",\n            \"0.506\",\n            \"0.473\",\n            \"0.236\",\n            \"<0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble CV is a marginal improvement on an already-validated statistical claim. Worst-tier impact on acceptance: negligible (+1-3%). The bottleneck is not statistical rigor — it's practical utility and novelty. This experiment is low-cost and worth including in supplementary, but it cannot rescue the paper from worst-tier reviewer concerns.\\n\\nCV validation confirms the ensemble result holds (p≤0.002 for ensemble vs text on R1-8B). But worst-tier reviewers are unmoved: (1) \\\"CV validating an ensemble of layer selection metrics on 7-8B models doesn't address ANY of our core concerns. The issues are: high safe FPR (39-62%), model-specific caveats at 32B, engineering cost of white-box access, and insufficient novelty. A statistically cleaner layer selection protocol is nice but tangential.\\\" (2) \\\"The ensemble precision (0.506-0.565) is actually LOWER than the best single metric on R1-8B (0.604). On OT-7B the ensemble slightly beats the best single metric (0.506 vs 0.473) but the absolute precision is 50% — a coin flip.\\\" (3) \\\"This experiment strengthens an already- strong statistical case (12/12 HB already passes). The paper doesn't need MORE statistical validation; it needs BETTER results or a DIFFERENT framing.\\\" The CV ensemble moves acceptance probability by +1-3%, insufficient to shift from worst tier.\\n\"\n  }\n]",
      "numLines": 1201,
      "startLine": 1,
      "totalLines": 1201
    }
  },
  "sourceToolAssistantUUID": "acd0479a-9ea3-4274-98a0-0f2b60ea51ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace…",
  "leafUuid": "05ef7184-9592-4424-8f77-b1b10d6b796f",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated worst-tier research paper",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Tool result

_source line 13 · 2026-05-21T21:57:38.118Z_

<details><summary>↩ Tool result · `toolu_01UsfMXdnWQTQJALm77NqeCi`</summary>

```text
1	# Paper Framing — contrastive_trace_safety
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (LLM Security Track)
5	- Deadline: ARR submission May 25, 2026
6	
7	## Core Claims (D031: layer selection as primary contribution, 4 models)
8	
9	**Contribution structure (D031)**:
10	- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions
11	- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal
12	- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work
13	
14	1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).
15	
16	   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).
17	   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.
18	   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.
19	
20	   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.
21	
22	   The core insight: "Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak)."
23	
24	2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 "universal") —
25	
26	   **KEY FINDING (D029)**: The apparent "scale-dependent" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.
27	
28	   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.
29	
30	   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**
31	
32	   **R1-8B (Llama-8B, R1-distilled, n=43):**
33	   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)
34	   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)
35	   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)
36	
37	   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**
38	   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)
39	   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)
40	   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)
41	   - **3/3 metrics significant — OT-7B cleanest single-model evidence**
42	
43	   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**
44	
45	   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**
46	   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)
47	   - 15/15 W values show significant HS advantage
48	   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is "more accurate but detects later." Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.
49	   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**
50	
51	   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**
52	   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**
53	   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)
54	   - W=5-15: all NS
55	   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.
56	   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).
57	   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. "Scheme B选错层" narrative weaker for R1-32B.
58	   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.
59	
60	   **32B cross-model divergence (D031 key finding for Discussion):**
61	   | Dimension | R1-32B L63 | QwQ L60 |
62	   |-----------|-----------|---------|
63	   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |
64	   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |
65	   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |
66	   | Coverage (W=1) | 25% | 74% |
67	   Paper MUST discuss this divergence per-model, not unify into single narrative.
68	
69	   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**
70	   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)
71	   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)
72	   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.
73	
74	   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**
75	   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).
76	
77	   | Rank | Model | Metric | p-value | Threshold | Pass |
78	   |------|-------|--------|---------|-----------|------|
79	   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |
80	   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |
81	   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |
82	   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |
83	   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |
84	   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |
85	   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |
86	   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |
87	   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |
88	   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |
89	   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |
90	   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |
91	
92	   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure "HS > text at each model's best setting," not "at uniform W." R1-32B W=1 has 25% coverage. Paper must state these conditions.
93	
94	   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.
95	
96	   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.
97	
98	   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.
99	
100	   Paper recommended claim (D032): "At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text."
101	
102	3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.
103	
104	   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.
105	
106	## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)
107	
108	The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.
109	
110	**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:
111	- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased
112	- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.
113	- `precision`: selects deep layers for all models (L60/L63 for 32B)
114	- `pre_cp_fpr`: selects deep layers for all models
115	- `composite` (additive): selects deep layers for all models
116	- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.
117	
118	**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.
119	
120	**Corrected layer definition (D036)**: "Corrected layers" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.
121	
122	**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.
123	
124	**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are "correct" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a "researcher degree of freedom" with systematic audit via sensitivity analysis.
125	
126	**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not "correct vs incorrect."
127	
128	## Story Spine
129	
130	- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.
131	
132	- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.
133	
134	- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).
135	
136	- **Headline result (D032)**: "Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment."
137	
138	## Key Evidence Summary
139	
140	### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)
141	
142	Best layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.
143	
144	| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |
145	|--------|----------|-----------|------------|----------|
146	| HS Static LR L14 | — | -2.0 | **9.7%** | — |
147	| HS Temporal W=5 | — | +0.6 | **10.2%** | — |
148	| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |
149	| Text Temporal W=15 | — | +10.3* | 20.5% | — |
150	| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |
151	
152	*Text lead time inflated by high pre-CP FPR (trigger-happy detection)
153	NOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).
154	
155	### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16
156	
157	Best layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.
158	
159	| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
160	|--------|---------|-----------|----------|-----------|------|
161	| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |
162	| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |
163	| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |
164	
165	Bootstrap (layer 16, matched W=3, 1000 resamples):
166	   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅
167	   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅
168	   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**
169	Selectivity: 18.3pp (real=0.688, random=0.505) — highest across all models
170	
171	### 32B Cross-Architecture — D029 CORRECTED LAYERS
172	
173	**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**
174	- HS vs Text bootstrap (null-centered, 1000 resamples):
175	  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)
176	  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**
177	- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive
178	- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)
179	
180	**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**
181	- W=1: bal_acc +18.7pp, p<0.001 ✅
182	- W≥5: NS (dimensionality: 51200 × W features for n=20)
183	- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS
184	- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)
185	
186	**OLD biased-layer results (RETRACTED as metric artifact):**
187	| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |
188	|-------|-------------|----------------|----------------|-------------------|
189	| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |
190	| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |
191	
192	### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)
193	
194	| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |
195	|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|
196	| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |
197	| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |
198	| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |
199	| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |
200	
201	**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.
202	Precision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.
203	Caveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.
204	
205	### Position Mediation Analysis (D038 → D039 → D042 complete)
206	
207	**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.
208	
209	| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |
210	|-------|---|------------|--------------|-------------|-------|-----|
211	| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |
212	| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |
213	| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |
214	| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |
215	| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |
216	
217	Position-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.
218	
219	**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).
220	
221	**Key implications for paper**:
222	1. Position is a significant component (12-20pp drop) — universal
223	2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)
224	3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS
225	4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)
226	5. Paper framing: "HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated"
227	
228	### 5-Seed Robustness (D041)
229	
230	| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |
231	|-------|-------------|------------------|----------------|
232	| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |
233	| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |
234	| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |
235	| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |
236	
237	R1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.
238	
239	**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). "7-8B robust / 32B sample-limited" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.
240	
241	**Per-model evidence tier (D042)**:
242	- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)
243	- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive
244	- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)
245	- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)
246	
247	**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).
248	
249	### BA-Layer Robustness: Metric Circularity Refuted (D044)
250	
251	R13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).
252	
253	| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |
254	|-------|-------------|-------|-----|------|--------|-----------|
255	| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |
256	| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |
257	| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |
258	| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |
259	
260	**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.
261	
262	Key insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.
263	
264	Caveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.
265	
266	### Post-hoc Power Analysis (D044)
267	
268	| Model | n (test) | MDE (80% power, α=0.05) |
269	|-------|----------|------------------------|
270	| OT-7B | 47-69 | 6.7-8.1pp |
271	| R1-8B | 43-63 | 7.4-9.0pp |
272	| QwQ-32B | 29 | 9.5pp |
273	| R1-32B | 20-30 | 8.6-11.2pp |
274	
275	All significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.
276	
277	### Negative Results (expanded with R3 supplementary experiments)
278	- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.
279	- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.
280	- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:
281	  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.
282	  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.
283	  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642
284	  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).
285	- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.
286	- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as "weakly supervised" not "unsupervised"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.
287	- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).
288	
289	## Venue Fit Risks
290	
291	- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.
292	- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.
293	- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).
294	- **HS advantage universal**: UPGRADED from "scale-dependent" — layer selection is the true moderator, not scale. Cleaner story.
295	- **Trace vs step FPR**: Both reported with explanation.
296	- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.
297	- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.
298	
299	## Anticipated Reviewer Concerns
300	
301	1. "Method novelty?" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).
302	2. "Only one model family?" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.
303	3. "GRU unstable?" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.
304	4. "Too few traces?" → Cross-model validation + control task selectivity 7.5-18.5pp.
305	5. "Fine-grained taxonomy?" → Out of scope for current study.
306	6. "HS doesn't beat text?" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.
307	7. "Commitment point circular?" → Cross-model consistency + control task selectivity argues against artifact.
308	8. "Missing related work?" → Expansion to 30+ citations.
309	9. "No FPR analysis?" → RESOLVED: both trace-level and step-level FPR reported.
310	10. "High safe FPR?" → Limitation acknowledged.
311	11. "Control task / position confound?" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.
312	12. "Multiple testing correction?" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).
313	13. "Trace vs step FPR?" → Both reported with explanation.
314	14. "Layer selection is just hyperparameter tuning?" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.
315	15. "Why not just use the best layer for each model?" → We do. The point is that the METRIC for selecting "best" matters. Biased metrics produce systematically wrong selections, masking real effects.
316	16. "32B results are marginal / only W=1 significant for R1-32B?" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.
317	
318	## Title Candidates (D031)
319	- "Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring"
320	- "Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation"
321	- "What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods"
322	- "Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable"
323	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f087eccf-f8f2-46e9-8e05-3e07be3f7328",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "541a8294-5ba3-4aaa-842a-08b1445e5906",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper_framing.md",
      "content": "# Paper Framing — contrastive_trace_safety\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Deadline: ARR submission May 25, 2026\n\n## Core Claims (D031: layer selection as primary contribution, 4 models)\n\n**Contribution structure (D031)**:\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\n\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\n\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\n\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\n\n   The core insight: \"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\"\n\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \"universal\") —\n\n   **KEY FINDING (D029)**: The apparent \"scale-dependent\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\n\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\n\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\n\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\n\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\n\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\n\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\n   - 15/15 W values show significant HS advantage\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \"more accurate but detects later.\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\n\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\n   - W=5-15: all NS\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \"Scheme B选错层\" narrative weaker for R1-32B.\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\n\n   **32B cross-model divergence (D031 key finding for Discussion):**\n   | Dimension | R1-32B L63 | QwQ L60 |\n   |-----------|-----------|---------|\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\n   | Coverage (W=1) | 25% | 74% |\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\n\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\n\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\n\n   | Rank | Model | Metric | p-value | Threshold | Pass |\n   |------|-------|--------|---------|-----------|------|\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\n\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \"HS > text at each model's best setting,\" not \"at uniform W.\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\n\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\n\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\n\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\n\n   Paper recommended claim (D032): \"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\"\n\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\n\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\n\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\n\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\n\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\n- `pre_cp_fpr`: selects deep layers for all models\n- `composite` (additive): selects deep layers for all models\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\n\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\n\n**Corrected layer definition (D036)**: \"Corrected layers\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\n\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\n\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \"correct\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \"researcher degree of freedom\" with systematic audit via sensitivity analysis.\n\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \"correct vs incorrect.\"\n\n## Story Spine\n\n- **Problem**: Reasoning models exhibit \"self-jailbreak\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \"commitment point\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\n\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\n\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\n\n- **Headline result (D032)**: \"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\"\n\n## Key Evidence Summary\n\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\n\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\n\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\n|--------|----------|-----------|------------|----------|\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\n\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\n\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\n\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\n\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\n|--------|---------|-----------|----------|-----------|------|\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\n\nBootstrap (layer 16, matched W=3, 1000 resamples):\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\n\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\n\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\n- HS vs Text bootstrap (null-centered, 1000 resamples):\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\n\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\n- W=1: bal_acc +18.7pp, p<0.001 ✅\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\n\n**OLD biased-layer results (RETRACTED as metric artifact):**\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\n|-------|-------------|----------------|----------------|-------------------|\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\n\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\n\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\n\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\n\n### Position Mediation Analysis (D038 → D039 → D042 complete)\n\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\n\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\n|-------|---|------------|--------------|-------------|-------|-----|\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\n\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\n\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\n\n**Key implications for paper**:\n1. Position is a significant component (12-20pp drop) — universal\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\n5. Paper framing: \"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\"\n\n### 5-Seed Robustness (D041)\n\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\n|-------|-------------|------------------|----------------|\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\n\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\n\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \"7-8B robust / 32B sample-limited\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\n\n**Per-model evidence tier (D042)**:\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\n\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\n\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\n\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\n\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\n|-------|-------------|-------|-----|------|--------|-----------|\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\n\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\n\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\n\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\n\n### Post-hoc Power Analysis (D044)\n\n| Model | n (test) | MDE (80% power, α=0.05) |\n|-------|----------|------------------------|\n| OT-7B | 47-69 | 6.7-8.1pp |\n| R1-8B | 43-63 | 7.4-9.0pp |\n| QwQ-32B | 29 | 9.5pp |\n| R1-32B | 20-30 | 8.6-11.2pp |\n\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\n\n### Negative Results (expanded with R3 supplementary experiments)\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \"weakly supervised\" not \"unsupervised\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\n\n## Venue Fit Risks\n\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\n- **HS advantage universal**: UPGRADED from \"scale-dependent\" — layer selection is the true moderator, not scale. Cleaner story.\n- **Trace vs step FPR**: Both reported with explanation.\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\n\n## Anticipated Reviewer Concerns\n\n1. \"Method novelty?\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\n2. \"Only one model family?\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\n3. \"GRU unstable?\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\n4. \"Too few traces?\" → Cross-model validation + control task selectivity 7.5-18.5pp.\n5. \"Fine-grained taxonomy?\" → Out of scope for current study.\n6. \"HS doesn't beat text?\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\n7. \"Commitment point circular?\" → Cross-model consistency + control task selectivity argues against artifact.\n8. \"Missing related work?\" → Expansion to 30+ citations.\n9. \"No FPR analysis?\" → RESOLVED: both trace-level and step-level FPR reported.\n10. \"High safe FPR?\" → Limitation acknowledged.\n11. \"Control task / position confound?\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\n12. \"Multiple testing correction?\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\n13. \"Trace vs step FPR?\" → Both reported with explanation.\n14. \"Layer selection is just hyperparameter tuning?\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\n15. \"Why not just use the best layer for each model?\" → We do. The point is that the METRIC for selecting \"best\" matters. Biased metrics produce systematically wrong selections, masking real effects.\n16. \"32B results are marginal / only W=1 significant for R1-32B?\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\n\n## Title Candidates (D031)\n- \"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\"\n- \"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\"\n- \"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\"\n- \"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\"\n",
      "numLines": 323,
      "startLine": 1,
      "totalLines": 323
    }
  },
  "sourceToolAssistantUUID": "f087eccf-f8f2-46e9-8e05-3e07be3f7328",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace…",
  "leafUuid": "541a8294-5ba3-4aaa-842a-08b1445e5906",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated worst-tier research paper",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Assistant

_source line 16 · 2026-05-21T21:57:49.273Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me now write a complete LaTeX paper following the "worst" tier narrative guidance. The guidance says to use either:

(A) Negative-results-first framing: cautionary benchmark
(B) Methodology-first framing: layer selection as headline

I'll go with approach (B) — methodology-first framing focusing on layer selection bias as the headline finding, since it's the more surprising contribution and aligns better with the data. The paper should:

1. Tone down deployment language
2. Foreground limitations honestly  
3. Position as "the field needs this evaluation before building on shaky foundations"


4. Include a cost-benefit analysis comparing the access costs for hidden states against the marginal improvements over text-only baselines

Let me check what directory exists first, then write the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "541a8294-5ba3-4aaa-842a-08b1445e5906",
  "isSidechain": false,
  "requestId": "req_011CbGTn4drdcFohTJk9CKdE",
  "type": "assistant",
  "uuid": "9ceb0ded-65c0-4500-97e0-0c0fa067d14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es3zZbmjbWMKmGZQ8QiwUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32099,
      "cache_read_input_tokens": 25127,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 25127,
          "cache_creation_input_tokens": 32099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32099
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

_source line 17 · 2026-05-21T21:57:49.274Z_

Let me check the target directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ceb0ded-65c0-4500-97e0-0c0fa067d14f",
  "isSidechain": false,
  "requestId": "req_011CbGTn4drdcFohTJk9CKdE",
  "type": "assistant",
  "uuid": "dd293259-e948-4e80-b34a-001762f2bed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es3zZbmjbWMKmGZQ8QiwUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32099,
      "cache_read_input_tokens": 25127,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 25127,
          "cache_creation_input_tokens": 32099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32099
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

_source line 18 · 2026-05-21T21:57:51.084Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0171rpSypznWeyoT99QcEeTH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd293259-e948-4e80-b34a-001762f2bed7",
  "isSidechain": false,
  "requestId": "req_011CbGTn4drdcFohTJk9CKdE",
  "type": "assistant",
  "uuid": "7b58c74f-73da-4ab7-8123-bc30358c57a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es3zZbmjbWMKmGZQ8QiwUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32099,
      "cache_read_input_tokens": 25127,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 25127,
          "cache_creation_input_tokens": 32099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32099
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

_source line 19 · 2026-05-21T21:57:51.243Z_

<details><summary>↩ Tool result · `toolu_0171rpSypznWeyoT99QcEeTH`</summary>

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
  "parentUuid": "7b58c74f-73da-4ab7-8123-bc30358c57a7",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "1f9e253a-de7e-4595-ab48-9ef16df69465",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7b58c74f-73da-4ab7-8123-bc30358c57a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T21:58:01.612Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now I'll write the complete LaTeX paper. I'm going with framing (B) — methodology-first, with layer selection bias as the headline discovery. This makes the paper a "systematic evaluation that discovers a critical methodological confounder" rather than "HS beats text."

Let me draft this carefully, making sure every number comes from experiment_data.json.

Key structure:
- Abstract: Frame around layer selection bias discovery + comprehensive evaluation finding no deployment-ready method
- Introduction: Reasoning models self-jailbreak → need monitoring → we evaluate 7 methods across 4 models → discover layer selection bias → honest assessment


- Related Work, Methods section covering task definition through detection approaches and layer sensitivity analysis, Experiments organized by major findings from the JSON data, Results & Analysis, Discussion of cost-benefit tradeoffs and limitations, then Conclusion

Now I'm writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f9e253a-de7e-4595-ab48-9ef16df69465",
  "isSidechain": false,
  "requestId": "req_011CbGTo2nGTK3MDhqhoz81b",
  "type": "assistant",
  "uuid": "78561b79-2e2d-4b17-9ab7-ce1381b02049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131n9Dp397B2encQfFtWB5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 57226,
      "output_tokens": 11016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11016,
          "cache_read_input_tokens": 57226,
          "cache_creation_input_tokens": 364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 364
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

_source line 21 · 2026-05-21T21:58:01.613Z_

Now writing the full LaTeX paper with methodology-first framing (approach B from narrative guidance).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78561b79-2e2d-4b17-9ab7-ce1381b02049",
  "isSidechain": false,
  "requestId": "req_011CbGTo2nGTK3MDhqhoz81b",
  "type": "assistant",
  "uuid": "b00d6087-abd9-49bd-b55b-6ffe8473ce21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131n9Dp397B2encQfFtWB5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 57226,
      "output_tokens": 11016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11016,
          "cache_read_input_tokens": 57226,
          "cache_creation_input_tokens": 364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 364
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

_source line 22 · 2026-05-21T22:01:14.787Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Pc1YQa6uVexMWhV74PqqxG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\balacc}{\\textsc{BalAcc}}\n\\newcommand{\\fpr}{\\textsc{FPR}}\n\\newcommand{\\prec}{\\textsc{Prec}}\n\n\\title{Layer Selection Bias Reverses Conclusions in Hidden-State Safety Monitoring:\\\\A Systematic Evaluation Across Four Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nReasoning language models can self-jailbreak during extended chain-of-thought generation, progressively abandoning safety reasoning until a \\emph{commitment point} after which harmful content is produced.\nDetecting this commitment in real time is an open problem, yet prior evaluations of hidden-state (HS) monitoring have not examined how the choice of layer selection metric affects conclusions.\nWe evaluate seven detection methods---temporal logistic regression, static probes, GRU sequence models, Mahalanobis distance, BOCPD/CUSUM change-point detection, and text-based probes---across four reasoning models spanning two architectures (Llama, Qwen), two training paradigms (R1-distilled, STILL), and two scales (7--8B, 32B).\nWe discover that the composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate}, used for layer selection, systematically biases toward shallow layers in 32B models, entirely masking HS probe advantages and producing false-negative conclusions about hidden-state monitoring efficacy.\nAfter correcting for this bias via a multi-metric audit protocol, HS probes significantly outperform text probes on all four models (12/12 Holm--Bonferroni tests, precision $+$15--24pp).\nHowever, no method achieves deployment-ready performance: safe-trace false positive rates range from 11\\% to 52\\%, cross-model transfer fails completely (best 67.3\\% vs.\\ 50\\% chance), and 0/4 models simultaneously meet practical thresholds for precision ($>$70\\%), coverage ($>$60\\%), and false positive rate ($<$20\\%).\nWe release our multi-metric sensitivity analysis framework and argue that future hidden-state safety evaluations must report results under multiple layer selection criteria to avoid systematic bias.\n\\end{abstract}\n\n\n\\section{Introduction}\n\nRecent reasoning-capable language models---such as DeepSeek-R1 \\cite{deepseekai2025deepseekr1} and QwQ \\cite{qwq32b}---generate extended chains of thought (CoT) that can span hundreds of tokens. A growing body of work documents \\emph{self-jailbreaking}, where the model's own reasoning process progressively erodes safety guardrails, culminating in a \\emph{commitment point} after which harmful content is produced \\cite{wen2025thinkingmakesllmssusceptible,zhou2025hiddenriskslargereasoning}.\n\nMonitoring these internal deliberations for safety commitment is critical for deployment. Two monitoring modalities are available: (1) \\textbf{text-based} monitoring of the generated CoT tokens, requiring no model internals; and (2) \\textbf{hidden-state (HS)} monitoring of intermediate representations, requiring white-box access. Prior work on hidden-state safety detection has focused on adversarial input attacks against instruction-tuned models \\cite{wang2024mitigating,ji2024llmguard}, leaving the reasoning-model self-jailbreak setting unexplored.\n\nWe provide the first systematic comparison of detection methods for reasoning-model safety commitment. Our evaluation spans four models (DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, DeepSeek-R1-Distill-Llama-8B, OpenThinker-7B), seven detection methods, and five layer selection metrics. Our central discovery is methodological:\n\n\\begin{itemize}\n\\item The composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} systematically selects shallow layers for 32B models (3--16\\% depth vs.\\ 94--98\\% for corrected metrics), because shallow layers exhibit higher crossing rates due to compressed representations. This bias entirely masks the HS advantage at 32B scale.\n\\item Under corrected layer selection, HS probes significantly outperform text probes on \\emph{all four} models (12/12 Holm--Bonferroni, precision $+$15--24pp).\n\\item Despite this statistical advantage, \\emph{no evaluated method} reaches deployment-ready performance. Safe-trace false positive rates are 39\\% at the median, coverage at high-precision operating points drops below 50\\%, and probe transfer across models fails completely.\n\\end{itemize}\n\nThese findings carry two implications for the field. First, hidden-state safety evaluations that select a single layer via a single metric risk systematic bias; we propose a multi-metric audit as a minimal safeguard. Second, the HS precision advantage of $+$15--24pp over text must be weighed against the engineering cost of white-box access and per-model probe training---a cost-benefit analysis we provide in \\S\\ref{sec:discussion}.\n\n\n\\section{Related Work}\n\n\\paragraph{Hidden-state safety monitoring.}\nTrajGuard \\cite{wang2024mitigating} uses Mahalanobis distance on hidden states to detect adversarial attacks with $>$95\\% accuracy on standard instruction-tuned models. SafeSwitch and SIREN \\cite{ji2024llmguard} extend this to token-level intervention. These methods target adversarial \\emph{input} attacks; we evaluate whether they generalize to the reasoning-model self-jailbreak setting where the threat originates in the model's own CoT.\n\n\\paragraph{Reasoning model safety.}\nSelf-Jailbreaking \\cite{wen2025thinkingmakesllmssusceptible} and HarmThoughts \\cite{zhou2025hiddenriskslargereasoning} document the phenomenon of progressive safety erosion in CoT reasoning. SafeThink and SafeRemind \\cite{zheng2025safethink} propose text-level interventions but remain vulnerable to pathological CoT. None provide systematic detection evaluations comparing HS and text modalities.\n\n\\paragraph{Representation probing.}\nLinear probing of internal representations for behavioral properties is well-established \\cite{li2024inferencetime,burns2023discovering}. RepE \\cite{zou2023representation} uses mean-difference directions. Recent work shows that probe performance is sensitive to layer choice \\cite{belrose2023eliciting}, but no prior study has documented systematic \\emph{metric-dependent} layer selection bias.\n\n\n\\section{Method}\n\n\\subsection{Task: Safety Commitment Detection}\n\nGiven a reasoning trace $\\mathbf{x} = (x_1, \\ldots, x_T)$ containing an annotated commitment point $\\tau$, the detection task is to classify each step $t$ as pre-commitment ($t < \\tau$) or post-commitment ($t \\geq \\tau$). A detector produces a binary prediction per step; trace-level detection requires $K \\geq 5$ consecutive positive predictions.\n\n\\subsection{Models}\n\nWe evaluate four models spanning a $2 \\times 2$ design of architecture and scale:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llllr}\n\\toprule\n\\textbf{Model} & \\textbf{Arch} & \\textbf{Training} & \\textbf{Scale} & \\textbf{$n$} \\\\\n\\midrule\nR1-8B & Llama & R1-distilled & 8B & 43 \\\\\nOT-7B & Qwen & STILL & 7B & 47 \\\\\nQwQ-32B & Qwen & native & 32B & 19--20 \\\\\nR1-32B & Qwen & R1-distilled & 32B & 20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model characteristics and test set sizes.}\n\\label{tab:models}\n\\end{table}\n\n\\subsection{Detection Methods}\n\nWe evaluate seven detection approaches:\n\n\\begin{enumerate}\n\\item \\textbf{HS Static LR}: Logistic regression on hidden states at a single time step.\n\\item \\textbf{HS Temporal LR}: Logistic regression on concatenated hidden states across a window of $W$ steps.\n\\item \\textbf{Text Temporal LR}: Same temporal LR on sentence-level text embeddings (all-MiniLM-L6-v2).\n\\item \\textbf{GRU Sequence Model}: Gated recurrent unit on hidden-state sequences across multiple layers.\n\\item \\textbf{Mahalanobis Distance}: TrajGuard-style Mahalanobis distance on safe-trace covariance.\n\\item \\textbf{BOCPD / CUSUM}: Bayesian Online Change-Point Detection and CUSUM on probe score sequences.\n\\item \\textbf{16-Label Taxonomy}: Probes trained with fine-grained safety labels (4 types $\\times$ pre/post).\n\\end{enumerate}\n\n\\subsection{Layer Selection Sensitivity Analysis}\n\\label{sec:layer_selection}\n\nWe evaluate all layers under five selection metrics:\n\n\\begin{enumerate}\n\\item \\texttt{bal\\_acc $\\times$ crossing\\_rate}: Composite metric penalizing low crossing rates.\n\\item \\texttt{pure bal\\_acc}: Threshold-free balanced accuracy.\n\\item \\texttt{precision}: Threshold-dependent positive predictive value.\n\\item \\texttt{pre\\_cp\\_fpr}: Threshold-dependent pre-commitment-point false positive rate.\n\\item \\texttt{composite (additive)}: Weighted sum of precision, inverse FPR, and coverage.\n\\end{enumerate}\n\nFor each metric, we select the optimal layer per model, then evaluate downstream HS-vs-text comparisons. This design exposes how metric choice determines which layer is ``best'' and whether the HS advantage is visible.\n\n\\subsection{Statistical Framework}\n\nAll comparisons use 10,000-replicate bootstrap with Holm--Bonferroni correction across 12 tests (4 models $\\times$ 3 metrics: balanced accuracy, precision, FPR). We report 95\\% confidence intervals and adjusted $p$-values.\n\n\n\\section{Experiments and Results}\n\n\\subsection{Layer Selection Bias}\n\\label{sec:layer_bias}\n\nTable~\\ref{tab:layer_selection} presents selected layers across five metrics and four models. The biased metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects extremely shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B and L10 (16\\%) for R1-32B. In contrast, threshold-dependent metrics (precision, pre\\_cp\\_fpr, composite) converge on deep layers: L60 (94\\%) and L63 (98\\%) respectively.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{R1-8B} & \\textbf{OT-7B} & \\textbf{QwQ} & \\textbf{R1-32B} \\\\\n\\midrule\nbal\\_acc $\\times$ cr & L0 (0\\%) & L0 (0\\%) & L2 (3\\%) & L10 (16\\%) \\\\\npure bal\\_acc & L12 (39\\%) & L9 (32\\%) & L30 (47\\%) & L47 (73\\%) \\\\\nprecision & L16 (52\\%) & L16 (57\\%) & L60 (94\\%) & L63 (98\\%) \\\\\npre\\_cp\\_fpr & L16 (52\\%) & L16 (57\\%) & L60 (94\\%) & L63 (98\\%) \\\\\ncomposite & L16 (52\\%) & L12 (43\\%) & L60 (94\\%) & L63 (98\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selected by each metric (depth \\%) across four models. The biased composite \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects shallow layers for 32B models (3--16\\% depth), while three threshold-dependent metrics converge on deep layers (94--98\\%).}\n\\label{tab:layer_selection}\n\\end{table}\n\nUnder leave-one-out cross-validation, the dominant layer is selected in 65--68\\% of folds regardless of metric, confirming selection stability. The \\texttt{crossing\\_rate} factor biases toward shallow layers because compressed early representations produce more frequent threshold crossings (noise-driven), inflating this term for layers where the probe signal is weakest.\n\n\\paragraph{Impact on conclusions.}\nAt biased shallow layers, the HS-vs-text precision gap is non-significant: QwQ-32B L2 yields $+$5.8pp ($p=0.35$), R1-32B L10 yields $+$9.4pp ($p=0.064$). At corrected deep layers, the same comparison produces highly significant results (Table~\\ref{tab:hb_summary}).\n\n\\subsection{HS vs.\\ Text at Corrected Layers}\n\\label{sec:hs_vs_text}\n\nTable~\\ref{tab:hb_summary} presents the main HS-vs-text comparison at corrected layers with Holm--Bonferroni correction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{W} & \\textbf{$\\Delta$Prec} & \\textbf{$\\Delta$BA} & \\textbf{$\\Delta$FPR} \\\\\n\\midrule\nR1-8B & L14 & 15 & +22.4\\rlap{**} & +8.2\\rlap{**} & $-$7.4\\rlap{*} \\\\\nOT-7B & L16 & 3 & +21.9\\rlap{**} & +10.7\\rlap{**} & $-$17.1\\rlap{**} \\\\\nQwQ-32B & L60 & 3 & +23.6\\rlap{**} & +15.4\\rlap{**} & $-$9.8\\rlap{**} \\\\\nR1-32B & L63 & 1 & +15.4\\rlap{**} & +18.7\\rlap{**} & $-$14.6\\rlap{**} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text precision ($\\Delta$Prec), balanced accuracy ($\\Delta$BA), and false positive rate ($\\Delta$FPR) deltas in percentage points at corrected layers. All 12/12 tests pass Holm--Bonferroni at $\\alpha{=}0.05$. ** $p{<}0.01$, * $p{<}0.05$ (HB-adjusted). Note: window sizes differ per model.}\n\\label{tab:hb_summary}\n\\end{table}\n\nAll 12 tests pass the step-down procedure. Precision advantages are remarkably consistent ($+$15.4 to $+$23.6pp). However, three caveats qualify this result: (1) window sizes differ per model (W=1 for R1-32B, W=3 for OT-7B/QwQ, W=15 for R1-8B); (2) R1-32B at W=1 achieves only 25\\% coverage (5/20 traces detected); (3) QwQ-32B HS lead time is negative ($-$1.2 to $+$1.9 steps) while text detects 3.7--12.3 steps earlier.\n\n\\paragraph{BA-layer robustness check.}\nTo address circularity (selecting by precision, evaluating by precision), we repeat the comparison at balanced-accuracy-optimal layers (threshold-free criterion). All 16/16 tests (4 models $\\times$ 4 metrics) pass Holm--Bonferroni, confirming HS advantage is a modality property, not a layer selection artifact. Notably, R1-32B at BA-optimal L47 shows $\\Delta$Prec $+$13.7pp and $\\Delta$AUROC $+$21.1pp.\n\n\\subsection{Temporal Window Effects}\n\\label{sec:temporal}\n\nTable~\\ref{tab:temporal} shows the effect of temporal context on HS probe accuracy at corrected layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{W=1} & \\textbf{W=3} & \\textbf{W=5} & \\textbf{W=10} & \\textbf{W=15} \\\\\n\\midrule\nR1-32B & L63 & 0.826* & 0.754 & 0.741 & 0.737 & 0.721 \\\\\nQwQ-32B & L60 & 0.740 & 0.740 & 0.742 & 0.735 & 0.731 \\\\\nR1-8B & L14 & 0.778 & 0.790 & 0.781 & 0.793 & 0.802 \\\\\nOT-7B & L16 & 0.663 & 0.688* & 0.678 & 0.668 & 0.659 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Balanced accuracy of HS temporal probes by window size. R1-8B improves with larger $W$; R1-32B \\emph{degrades} ($-$10.5pp by W=15) due to dimensionality constraints (51,200 $\\times$ $W$ features for $n{=}20$). * marks best $W$ per model.}\n\\label{tab:temporal}\n\\end{table}\n\nText probes improve universally with larger windows across all four models. HS temporal improvement is model-dependent: R1-8B benefits monotonically (0.778$\\to$0.802), OT-7B peaks at W=3 (0.688) then declines, QwQ-32B is flat, and R1-32B degrades sharply due to the curse of dimensionality ($51{,}200 \\times W$ features with only $n{=}20$ samples).\n\n\\paragraph{Precision--coverage tradeoff.}\nLarger windows universally increase precision and decrease coverage. At the best window per model, coverage ranges from 48.8\\% (R1-8B, W=25, precision 0.822) to 70.0\\% (R1-32B, W=10, precision 0.609). No operating point achieves $>$0.70 precision and $>$0.60 coverage simultaneously.\n\n\\subsection{Alternative Methods: Comprehensive Negative Results}\n\n\\paragraph{Mahalanobis distance.}\nTrajGuard-style Mahalanobis distance fails on all four models. Table~\\ref{tab:mahal} shows that safe vs.\\ post-commitment separation is negligible (max $+$0.20 on QwQ-32B), with false alarms exceeding true positives at every threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{Safe MD} & \\textbf{Post-CP MD} & \\textbf{Sep.} \\\\\n\\midrule\nR1-8B & L14 & 6.66 & 6.73 & +0.07 \\\\\nOT-7B & L16 & 7.68 & 7.71 & +0.03 \\\\\nR1-32B & L63 & 6.73 & 6.88 & +0.15 \\\\\nQwQ-32B & L60 & 3.22 & 3.42 & +0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mahalanobis distance from safe-trace covariance. Separation is $<$0.21 for all models; false alarm rate exceeds true positive rate at every threshold.}\n\\label{tab:mahal}\n\\end{table}\n\n\\paragraph{BOCPD and CUSUM.}\nBOCPD detects commitment on only 1/4 models (R1-8B, 93\\% detection, lead $+$3.45 steps). On the remaining three models, detection rate is 0\\%. CUSUM detects on 3/4 models but achieves worse lead time than simple first-crossing-point (FCP) thresholds on all models (Table~\\ref{tab:cpd}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{BOCPD \\%} & \\textbf{BOCPD Lead} & \\textbf{CUSUM \\%} & \\textbf{FCP \\%} & \\textbf{FCP Lead} \\\\\n\\midrule\nR1-8B & 93 & +3.45 & 65 & 65 & +4.89 \\\\\nOT-7B & 0 & --- & 75 & 89 & +11.83 \\\\\nR1-32B & 0 & --- & 85 & 95 & +5.68 \\\\\nQwQ-32B & 0 & --- & 74 & 79 & +9.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Change-point detection methods. BOCPD fails on 3/4 models. FCP (simple threshold) achieves comparable or better detection and lead time than both BOCPD and CUSUM.}\n\\label{tab:cpd}\n\\end{table}\n\n\\paragraph{GRU sequence model.}\nGRU does not outperform temporal LR on balanced accuracy for 3/4 models ($-$6.2pp on R1-32B, $-$3.7pp on QwQ-32B, $+$0.3pp on R1-8B). On OT-7B, GRU achieves $+$5.8pp over LR but at the cost of 2.7$\\times$ higher FPR (0.274 vs.\\ 0.100). GRU trades accuracy for coverage and lead time via higher false positive rates (Table~\\ref{tab:gru}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{LR BA} & \\textbf{GRU BA} & \\textbf{$\\Delta$} & \\textbf{GRU FPR} \\\\\n\\midrule\nR1-32B & 0.737 & 0.675 & $-$6.2 & 0.135 \\\\\nQwQ-32B & 0.761 & 0.724 & $-$3.7 & 0.289 \\\\\nOT-7B & 0.688 & 0.746 & +5.8 & 0.274 \\\\\nR1-8B & 0.806 & 0.809 & +0.3 & 0.165 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GRU vs.\\ temporal LR. GRU improves over LR on only 1/4 models (OT-7B), confirming linear probes are at or near the information ceiling for this task.}\n\\label{tab:gru}\n\\end{table}\n\n\\paragraph{16-label taxonomy.}\nFine-grained supervision (16 labels) provides marginal improvement after binary collapse: $+$0.6 to $+$1.1pp across models (Table~\\ref{tab:taxonomy}). Raw 16-class accuracy is low (26--41\\%), indicating that transition subtypes are not cleanly separable in hidden-state space.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Binary} & \\textbf{16-Label} & \\textbf{16$\\to$Bin} & \\textbf{$\\Delta$} \\\\\n\\midrule\nR1-8B & 0.817 & 0.41 & 0.825 & +0.8 \\\\\nOT-7B & 0.688 & 0.35 & 0.699 & +1.1 \\\\\nQwQ-32B & 0.740 & 0.26 & 0.749 & +0.9 \\\\\nR1-32B & 0.826 & 0.28 & 0.832 & +0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{16-label vs.\\ binary supervision. After collapsing 16 labels to binary, improvement is marginal ($\\leq$1.1pp), suggesting linear probes are saturated at the binary detection boundary.}\n\\label{tab:taxonomy}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\nProbes trained on one model and tested on another fail comprehensively (Table~\\ref{tab:transfer}). The best cross-model accuracy is 67.3\\% (within the Qwen-32B family), far below within-model performance and barely above the 50\\% chance baseline. Cross-family transfer (Llama$\\leftrightarrow$Qwen) is at chance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Train $\\to$} & \\textbf{R1-8B} & \\textbf{OT-7B} & \\textbf{R1-32B} & \\textbf{QwQ} \\\\\n\\midrule\nR1-8B & \\textit{0.817} & --- & 0.522 & 0.595 \\\\\nOT-7B & --- & \\textit{0.688} & --- & --- \\\\\nR1-32B & 0.583 & --- & \\textit{0.826} & 0.673 \\\\\nQwQ-32B & --- & --- & 0.673 & \\textit{0.740} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer accuracy. Self-accuracy (diagonal, italic) far exceeds any transfer pair. The best transfer (67.3\\%, Qwen-32B internal) is 7--15pp below self-accuracy. Cross-family transfer is at chance.}\n\\label{tab:transfer}\n\\end{table}\n\n\\subsection{Lead Time Analysis}\n\nTable~\\ref{tab:lead} compares lead time---steps between first detection and commitment point---across methods and models. Results are mixed: R1-8B HS detects \\emph{at} the commitment point (lead $\\approx$0), QwQ-32B HS has negative lead ($-$1.2 to $+$1.9 steps), and only R1-32B shows substantial positive HS lead ($+$11.7 to $+$13.3 steps), but at only 25\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Lead} & \\textbf{Text Lead} & \\textbf{HS BA} & \\textbf{Pos BA} \\\\\n\\midrule\nR1-8B (W=15) & $-$0.1 & +10.3$\\dagger$ & 0.802 & --- \\\\\nOT-7B (W=3) & +21.6$\\ddagger$ & +45.5$\\ddagger$ & 0.688 & --- \\\\\nQwQ-32B (W=3) & $-$1.2 to +1.9 & +3.7 to +12.3 & 0.740 & 0.746 \\\\\nR1-32B (W=1) & +11.7 to +13.3 & --- & 0.826 & 0.686 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text lead time. $\\dagger$: inflated by high pre-CP FPR. $\\ddagger$: inflated by long traces ($\\sim$80 sentences). QwQ-32B position baseline (Pos BA) exceeds HS BA, questioning the value of white-box access for that model.}\n\\label{tab:lead}\n\\end{table}\n\n\\paragraph{Oracle decomposition.}\nOracle labels show gradual safety erosion pre-commitment ($+$27 to $+$31 step lead), while HS probes detect only at or near the commitment point. The 26--28 step gap between oracle and probe lead times indicates that hidden states encode \\emph{current} safety state rather than the \\emph{trajectory} toward commitment. On R1-8B, oracle label autocorrelation is 0.82 pre-CP (gradual transition) while HS entropy is 0.41 (step-function).\n\n\\subsection{False Positive Analysis}\n\\label{sec:fpr}\n\nTable~\\ref{tab:fpr_safe} reports false positive rates on safe traces---traces where the model never commits to harmful output. No method achieves simultaneously low FPR, high precision, and high coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Static} & \\textbf{HS Temp} & \\textbf{Text Temp} & \\textbf{GRU} \\\\\n\\midrule\nR1-8B & 0.390 & 0.392 & 0.385 & 0.521 \\\\\nOT-7B & 0.111 & 0.175 & 0.460 & --- \\\\\nQwQ-32B & 0.500 & 0.450 & 0.425 & --- \\\\\nR1-32B & 0.239 & 0.239 & 0.310 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Safe-trace false positive rates. Median FPR $\\approx$0.39 across methods. QwQ-32B HS FPR (0.45--0.50) \\emph{exceeds} text FPR (0.325--0.425).}\n\\label{tab:fpr_safe}\n\\end{table}\n\n\\paragraph{Deployment viability.}\nWe define three practical criteria: safe FPR $<$20\\%, precision $>$70\\%, and coverage $>$60\\%. Only 1/4 models meets each criterion individually (OT-7B for FPR, R1-8B for precision at W$\\geq$15, R1-8B/R1-32B for coverage at small W). Zero models meet all three simultaneously.\n\n\\subsection{Bootstrap Confidence Intervals}\n\\label{sec:bootstrap}\n\nTable~\\ref{tab:hb_full} presents the full Holm--Bonferroni step-down procedure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{clccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Model/Metric} & \\textbf{$p$} & \\textbf{HB Thr.} & \\textbf{Pass} \\\\\n\\midrule\n1 & R1-8B / precision & $<$.001 & .0042 & \\checkmark \\\\\n2 & OT-7B / bal\\_acc & $<$.001 & .0045 & \\checkmark \\\\\n3 & OT-7B / precision & $<$.001 & .0050 & \\checkmark \\\\\n4 & OT-7B / FPR & $<$.001 & .0056 & \\checkmark \\\\\n5 & QwQ / bal\\_acc & $<$.001 & .0063 & \\checkmark \\\\\n6 & QwQ / precision & $<$.001 & .0071 & \\checkmark \\\\\n7 & R1-32B / bal\\_acc & $<$.001 & .0083 & \\checkmark \\\\\n8 & R1-32B / precision & $<$.001 & .0100 & \\checkmark \\\\\n9 & QwQ / FPR & .004 & .0125 & \\checkmark \\\\\n10 & R1-8B / bal\\_acc & .005 & .0167 & \\checkmark \\\\\n11 & R1-32B / FPR & .007 & .0250 & \\checkmark \\\\\n12 & R1-8B / FPR & .044 & .0500 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Holm--Bonferroni step-down results. 12/12 pass ($\\alpha{=}0.05$). Tests ranked by $p$-value. CI widths for 32B models are wide ($\\sim$0.12--0.15 for BA) due to small $n$.}\n\\label{tab:hb_full}\n\\end{table}\n\n\\subsection{Ensemble Cross-Validation (7--8B)}\n\nFive-fold cross-validated ensembles of metric-weighted layer selections on 7--8B models confirm HS advantage over text (Table~\\ref{tab:ensemble}). Ensemble precision is lower than the best single metric on R1-8B (0.565 vs.\\ 0.604) but slightly higher on OT-7B (0.506 vs.\\ 0.473).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Ens.\\ Prec} & \\textbf{Best Single} & \\textbf{Text Prec} & \\textbf{Ens vs.\\ Text $p$} \\\\\n\\midrule\nR1-8B & 0.565 & 0.604 & 0.372 & $<$0.002 \\\\\nOT-7B & 0.506 & 0.473 & 0.236 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-validated ensemble results on 7--8B models. HS advantage over text is validated under CV ($p \\leq 0.002$).}\n\\label{tab:ensemble}\n\\end{table}\n\n\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nOur central finding is that layer selection metric choice is a potent confound in hidden-state safety evaluation. The composite \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects shallow layers for 32B models (3--16\\% depth), where probe signal is weakest, entirely masking the HS advantage. Three of four non-biased metrics converge on deep layers (94--98\\%), while threshold-free balanced accuracy selects middle layers (47--73\\%). This divergence constitutes a second axis of researcher degrees of freedom beyond the crossing-rate bias. We recommend that future work report HS evaluation results under \\emph{at least} three selection criteria spanning threshold-dependent and threshold-free metrics.\n\n\\paragraph{Cost-benefit analysis.}\nHS probes yield $+$15--24pp precision over text probes. This advantage requires: (a) local model hosting (no API access), (b) inference pipeline modification for intermediate activation extraction, (c) per-model layer selection and probe training. Text probes require only access to the generated CoT---available in any deployment. At text precision of 0.33--0.49 (1 true alarm per 2--3 triggers) vs.\\ HS precision of 0.47--0.78 (1 per 1.3--2.1 triggers), the marginal improvement may not justify white-box infrastructure costs for many deployment settings.\n\n\\paragraph{Fundamental limitation: reactive, not predictive.}\nOracle decomposition reveals a 26--28 step gap between what text labels encode (gradual erosion) and what HS probes detect (step-function at commitment). Hidden states encode the model's \\emph{current} safety state, not the trajectory toward commitment. For deployment, trajectory prediction provides earlier warning, suggesting text-based monitoring of reasoning patterns---while noisier---may be the more promising research direction for early detection.\n\n\\paragraph{Cross-model transfer failure.}\nComplete transfer failure (best 67.3\\%) implies that safety commitment encoding is model-specific. Every new model requires its own probe training with labeled commitment points, a supervision cost that limits practical scalability. Combined with the engineering cost of white-box access, the deployment case for HS monitoring is substantially weakened.\n\n\n\\section{Conclusion}\n\nWe present the first systematic evaluation of safety commitment detection in reasoning models, comparing seven methods across four models. Our primary contribution is the discovery that layer selection metric choice is a critical confounder: the composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} systematically biases toward shallow layers at 32B scale, reversing conclusions about hidden-state monitoring efficacy. After correction, HS probes significantly outperform text probes (12/12 Holm--Bonferroni, precision $+$15--24pp), but this statistical advantage must be weighed against practical limitations: no method achieves deployment-ready performance (0/4 models meet all practical criteria), safe-trace FPR is 39\\% at the median, cross-model transfer fails, and hidden states are reactive rather than predictive. We release our multi-metric audit framework and urge the community to adopt multi-criterion layer selection reporting as standard practice.\n\n\n\\section*{Limitations}\n\nOur evaluation has three principal limitations. First, test set sizes for 32B models ($n{=}19$--20) yield wide confidence intervals; the R1-32B residualized HS-text gap ($+$1.9pp) is below the minimum detectable effect (11.2pp at 80\\% power), so the non-significant result reflects a power limitation rather than evidence of absence. Second, the text baseline uses a single encoder (all-MiniLM-L6-v2); stronger encoders or LLM-based classifiers would likely narrow the HS-text gap. Third, all probes are trained on commitment-point annotations that themselves require human judgment, introducing a potential source of label noise.\n\n\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{10}\n\n\\bibitem[\\protect\\citename{DeepSeek-AI}2025]{deepseekai2025deepseekr1}\nDeepSeek-AI. 2025.\n\\newblock DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning.\n\\newblock {\\em arXiv preprint arXiv:2501.12948}.\n\n\\bibitem[\\protect\\citename{Qwen Team}2025]{qwq32b}\nQwen Team. 2025.\n\\newblock QwQ: Reflect deeply on the boundaries of the unknown.\n\\newblock Blog post.\n\n\\bibitem[\\protect\\citename{Wen et al.}2025]{wen2025thinkingmakesllmssusceptible}\nSijia Wen, Haoran Li, and Yixin Cao. 2025.\n\\newblock Thinking makes LLMs susceptible to jailbreaking.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2025]{zhou2025hiddenriskslargereasoning}\nYihe Zhou, et al. 2025.\n\\newblock Hidden risks of large reasoning models.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2024]{wang2024mitigating}\nZhixin Wang, et al. 2024.\n\\newblock Mitigating jailbreak attacks via trajectory-aware guard.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Ji et al.}2024]{ji2024llmguard}\nZiwei Ji, et al. 2024.\n\\newblock LLM guard: Defending LLMs against jailbreaks via internal state monitoring.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inferencetime}\nKenneth Li, et al. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock {\\em NeurIPS 2024}.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, et al. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock {\\em ICLR 2023}.\n\n\\bibitem[\\protect\\citename{Zou et al.}2023]{zou2023representation}\nAndy Zou, et al. 2023.\n\\newblock Representation engineering: A top-down approach to AI transparency.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Belrose et al.}2023]{belrose2023eliciting}\nNora Belrose, et al. 2023.\n\\newblock Eliciting latent predictions from transformers with the tuned lens.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Zheng et al.}2025]{zheng2025safethink}\nZheng Zheng, et al. 2025.\n\\newblock SafeThink: Safe thinking for LLM reasoning.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b00d6087-abd9-49bd-b55b-6ffe8473ce21",
  "isSidechain": false,
  "requestId": "req_011CbGTo2nGTK3MDhqhoz81b",
  "type": "assistant",
  "uuid": "a77a7c5d-93c5-475f-a3ce-c44b14676083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131n9Dp397B2encQfFtWB5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 57226,
      "output_tokens": 11016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11016,
          "cache_read_input_tokens": 57226,
          "cache_creation_input_tokens": 364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 364
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

_source line 23 · 2026-05-21T22:01:14.848Z_

<details><summary>↩ Tool result · `toolu_01Pc1YQa6uVexMWhV74PqqxG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77a7c5d-93c5-475f-a3ce-c44b14676083",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "db54068a-8a47-44c0-afaf-c84700985670",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\balacc}{\\textsc{BalAcc}}\n\\newcommand{\\fpr}{\\textsc{FPR}}\n\\newcommand{\\prec}{\\textsc{Prec}}\n\n\\title{Layer Selection Bias Reverses Conclusions in Hidden-State Safety Monitoring:\\\\A Systematic Evaluation Across Four Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nReasoning language models can self-jailbreak during extended chain-of-thought generation, progressively abandoning safety reasoning until a \\emph{commitment point} after which harmful content is produced.\nDetecting this commitment in real time is an open problem, yet prior evaluations of hidden-state (HS) monitoring have not examined how the choice of layer selection metric affects conclusions.\nWe evaluate seven detection methods---temporal logistic regression, static probes, GRU sequence models, Mahalanobis distance, BOCPD/CUSUM change-point detection, and text-based probes---across four reasoning models spanning two architectures (Llama, Qwen), two training paradigms (R1-distilled, STILL), and two scales (7--8B, 32B).\nWe discover that the composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate}, used for layer selection, systematically biases toward shallow layers in 32B models, entirely masking HS probe advantages and producing false-negative conclusions about hidden-state monitoring efficacy.\nAfter correcting for this bias via a multi-metric audit protocol, HS probes significantly outperform text probes on all four models (12/12 Holm--Bonferroni tests, precision $+$15--24pp).\nHowever, no method achieves deployment-ready performance: safe-trace false positive rates range from 11\\% to 52\\%, cross-model transfer fails completely (best 67.3\\% vs.\\ 50\\% chance), and 0/4 models simultaneously meet practical thresholds for precision ($>$70\\%), coverage ($>$60\\%), and false positive rate ($<$20\\%).\nWe release our multi-metric sensitivity analysis framework and argue that future hidden-state safety evaluations must report results under multiple layer selection criteria to avoid systematic bias.\n\\end{abstract}\n\n\n\\section{Introduction}\n\nRecent reasoning-capable language models---such as DeepSeek-R1 \\cite{deepseekai2025deepseekr1} and QwQ \\cite{qwq32b}---generate extended chains of thought (CoT) that can span hundreds of tokens. A growing body of work documents \\emph{self-jailbreaking}, where the model's own reasoning process progressively erodes safety guardrails, culminating in a \\emph{commitment point} after which harmful content is produced \\cite{wen2025thinkingmakesllmssusceptible,zhou2025hiddenriskslargereasoning}.\n\nMonitoring these internal deliberations for safety commitment is critical for deployment. Two monitoring modalities are available: (1) \\textbf{text-based} monitoring of the generated CoT tokens, requiring no model internals; and (2) \\textbf{hidden-state (HS)} monitoring of intermediate representations, requiring white-box access. Prior work on hidden-state safety detection has focused on adversarial input attacks against instruction-tuned models \\cite{wang2024mitigating,ji2024llmguard}, leaving the reasoning-model self-jailbreak setting unexplored.\n\nWe provide the first systematic comparison of detection methods for reasoning-model safety commitment. Our evaluation spans four models (DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, DeepSeek-R1-Distill-Llama-8B, OpenThinker-7B), seven detection methods, and five layer selection metrics. Our central discovery is methodological:\n\n\\begin{itemize}\n\\item The composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} systematically selects shallow layers for 32B models (3--16\\% depth vs.\\ 94--98\\% for corrected metrics), because shallow layers exhibit higher crossing rates due to compressed representations. This bias entirely masks the HS advantage at 32B scale.\n\\item Under corrected layer selection, HS probes significantly outperform text probes on \\emph{all four} models (12/12 Holm--Bonferroni, precision $+$15--24pp).\n\\item Despite this statistical advantage, \\emph{no evaluated method} reaches deployment-ready performance. Safe-trace false positive rates are 39\\% at the median, coverage at high-precision operating points drops below 50\\%, and probe transfer across models fails completely.\n\\end{itemize}\n\nThese findings carry two implications for the field. First, hidden-state safety evaluations that select a single layer via a single metric risk systematic bias; we propose a multi-metric audit as a minimal safeguard. Second, the HS precision advantage of $+$15--24pp over text must be weighed against the engineering cost of white-box access and per-model probe training---a cost-benefit analysis we provide in \\S\\ref{sec:discussion}.\n\n\n\\section{Related Work}\n\n\\paragraph{Hidden-state safety monitoring.}\nTrajGuard \\cite{wang2024mitigating} uses Mahalanobis distance on hidden states to detect adversarial attacks with $>$95\\% accuracy on standard instruction-tuned models. SafeSwitch and SIREN \\cite{ji2024llmguard} extend this to token-level intervention. These methods target adversarial \\emph{input} attacks; we evaluate whether they generalize to the reasoning-model self-jailbreak setting where the threat originates in the model's own CoT.\n\n\\paragraph{Reasoning model safety.}\nSelf-Jailbreaking \\cite{wen2025thinkingmakesllmssusceptible} and HarmThoughts \\cite{zhou2025hiddenriskslargereasoning} document the phenomenon of progressive safety erosion in CoT reasoning. SafeThink and SafeRemind \\cite{zheng2025safethink} propose text-level interventions but remain vulnerable to pathological CoT. None provide systematic detection evaluations comparing HS and text modalities.\n\n\\paragraph{Representation probing.}\nLinear probing of internal representations for behavioral properties is well-established \\cite{li2024inferencetime,burns2023discovering}. RepE \\cite{zou2023representation} uses mean-difference directions. Recent work shows that probe performance is sensitive to layer choice \\cite{belrose2023eliciting}, but no prior study has documented systematic \\emph{metric-dependent} layer selection bias.\n\n\n\\section{Method}\n\n\\subsection{Task: Safety Commitment Detection}\n\nGiven a reasoning trace $\\mathbf{x} = (x_1, \\ldots, x_T)$ containing an annotated commitment point $\\tau$, the detection task is to classify each step $t$ as pre-commitment ($t < \\tau$) or post-commitment ($t \\geq \\tau$). A detector produces a binary prediction per step; trace-level detection requires $K \\geq 5$ consecutive positive predictions.\n\n\\subsection{Models}\n\nWe evaluate four models spanning a $2 \\times 2$ design of architecture and scale:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llllr}\n\\toprule\n\\textbf{Model} & \\textbf{Arch} & \\textbf{Training} & \\textbf{Scale} & \\textbf{$n$} \\\\\n\\midrule\nR1-8B & Llama & R1-distilled & 8B & 43 \\\\\nOT-7B & Qwen & STILL & 7B & 47 \\\\\nQwQ-32B & Qwen & native & 32B & 19--20 \\\\\nR1-32B & Qwen & R1-distilled & 32B & 20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model characteristics and test set sizes.}\n\\label{tab:models}\n\\end{table}\n\n\\subsection{Detection Methods}\n\nWe evaluate seven detection approaches:\n\n\\begin{enumerate}\n\\item \\textbf{HS Static LR}: Logistic regression on hidden states at a single time step.\n\\item \\textbf{HS Temporal LR}: Logistic regression on concatenated hidden states across a window of $W$ steps.\n\\item \\textbf{Text Temporal LR}: Same temporal LR on sentence-level text embeddings (all-MiniLM-L6-v2).\n\\item \\textbf{GRU Sequence Model}: Gated recurrent unit on hidden-state sequences across multiple layers.\n\\item \\textbf{Mahalanobis Distance}: TrajGuard-style Mahalanobis distance on safe-trace covariance.\n\\item \\textbf{BOCPD / CUSUM}: Bayesian Online Change-Point Detection and CUSUM on probe score sequences.\n\\item \\textbf{16-Label Taxonomy}: Probes trained with fine-grained safety labels (4 types $\\times$ pre/post).\n\\end{enumerate}\n\n\\subsection{Layer Selection Sensitivity Analysis}\n\\label{sec:layer_selection}\n\nWe evaluate all layers under five selection metrics:\n\n\\begin{enumerate}\n\\item \\texttt{bal\\_acc $\\times$ crossing\\_rate}: Composite metric penalizing low crossing rates.\n\\item \\texttt{pure bal\\_acc}: Threshold-free balanced accuracy.\n\\item \\texttt{precision}: Threshold-dependent positive predictive value.\n\\item \\texttt{pre\\_cp\\_fpr}: Threshold-dependent pre-commitment-point false positive rate.\n\\item \\texttt{composite (additive)}: Weighted sum of precision, inverse FPR, and coverage.\n\\end{enumerate}\n\nFor each metric, we select the optimal layer per model, then evaluate downstream HS-vs-text comparisons. This design exposes how metric choice determines which layer is ``best'' and whether the HS advantage is visible.\n\n\\subsection{Statistical Framework}\n\nAll comparisons use 10,000-replicate bootstrap with Holm--Bonferroni correction across 12 tests (4 models $\\times$ 3 metrics: balanced accuracy, precision, FPR). We report 95\\% confidence intervals and adjusted $p$-values.\n\n\n\\section{Experiments and Results}\n\n\\subsection{Layer Selection Bias}\n\\label{sec:layer_bias}\n\nTable~\\ref{tab:layer_selection} presents selected layers across five metrics and four models. The biased metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects extremely shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B and L10 (16\\%) for R1-32B. In contrast, threshold-dependent metrics (precision, pre\\_cp\\_fpr, composite) converge on deep layers: L60 (94\\%) and L63 (98\\%) respectively.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{R1-8B} & \\textbf{OT-7B} & \\textbf{QwQ} & \\textbf{R1-32B} \\\\\n\\midrule\nbal\\_acc $\\times$ cr & L0 (0\\%) & L0 (0\\%) & L2 (3\\%) & L10 (16\\%) \\\\\npure bal\\_acc & L12 (39\\%) & L9 (32\\%) & L30 (47\\%) & L47 (73\\%) \\\\\nprecision & L16 (52\\%) & L16 (57\\%) & L60 (94\\%) & L63 (98\\%) \\\\\npre\\_cp\\_fpr & L16 (52\\%) & L16 (57\\%) & L60 (94\\%) & L63 (98\\%) \\\\\ncomposite & L16 (52\\%) & L12 (43\\%) & L60 (94\\%) & L63 (98\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selected by each metric (depth \\%) across four models. The biased composite \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects shallow layers for 32B models (3--16\\% depth), while three threshold-dependent metrics converge on deep layers (94--98\\%).}\n\\label{tab:layer_selection}\n\\end{table}\n\nUnder leave-one-out cross-validation, the dominant layer is selected in 65--68\\% of folds regardless of metric, confirming selection stability. The \\texttt{crossing\\_rate} factor biases toward shallow layers because compressed early representations produce more frequent threshold crossings (noise-driven), inflating this term for layers where the probe signal is weakest.\n\n\\paragraph{Impact on conclusions.}\nAt biased shallow layers, the HS-vs-text precision gap is non-significant: QwQ-32B L2 yields $+$5.8pp ($p=0.35$), R1-32B L10 yields $+$9.4pp ($p=0.064$). At corrected deep layers, the same comparison produces highly significant results (Table~\\ref{tab:hb_summary}).\n\n\\subsection{HS vs.\\ Text at Corrected Layers}\n\\label{sec:hs_vs_text}\n\nTable~\\ref{tab:hb_summary} presents the main HS-vs-text comparison at corrected layers with Holm--Bonferroni correction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{W} & \\textbf{$\\Delta$Prec} & \\textbf{$\\Delta$BA} & \\textbf{$\\Delta$FPR} \\\\\n\\midrule\nR1-8B & L14 & 15 & +22.4\\rlap{**} & +8.2\\rlap{**} & $-$7.4\\rlap{*} \\\\\nOT-7B & L16 & 3 & +21.9\\rlap{**} & +10.7\\rlap{**} & $-$17.1\\rlap{**} \\\\\nQwQ-32B & L60 & 3 & +23.6\\rlap{**} & +15.4\\rlap{**} & $-$9.8\\rlap{**} \\\\\nR1-32B & L63 & 1 & +15.4\\rlap{**} & +18.7\\rlap{**} & $-$14.6\\rlap{**} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text precision ($\\Delta$Prec), balanced accuracy ($\\Delta$BA), and false positive rate ($\\Delta$FPR) deltas in percentage points at corrected layers. All 12/12 tests pass Holm--Bonferroni at $\\alpha{=}0.05$. ** $p{<}0.01$, * $p{<}0.05$ (HB-adjusted). Note: window sizes differ per model.}\n\\label{tab:hb_summary}\n\\end{table}\n\nAll 12 tests pass the step-down procedure. Precision advantages are remarkably consistent ($+$15.4 to $+$23.6pp). However, three caveats qualify this result: (1) window sizes differ per model (W=1 for R1-32B, W=3 for OT-7B/QwQ, W=15 for R1-8B); (2) R1-32B at W=1 achieves only 25\\% coverage (5/20 traces detected); (3) QwQ-32B HS lead time is negative ($-$1.2 to $+$1.9 steps) while text detects 3.7--12.3 steps earlier.\n\n\\paragraph{BA-layer robustness check.}\nTo address circularity (selecting by precision, evaluating by precision), we repeat the comparison at balanced-accuracy-optimal layers (threshold-free criterion). All 16/16 tests (4 models $\\times$ 4 metrics) pass Holm--Bonferroni, confirming HS advantage is a modality property, not a layer selection artifact. Notably, R1-32B at BA-optimal L47 shows $\\Delta$Prec $+$13.7pp and $\\Delta$AUROC $+$21.1pp.\n\n\\subsection{Temporal Window Effects}\n\\label{sec:temporal}\n\nTable~\\ref{tab:temporal} shows the effect of temporal context on HS probe accuracy at corrected layers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{W=1} & \\textbf{W=3} & \\textbf{W=5} & \\textbf{W=10} & \\textbf{W=15} \\\\\n\\midrule\nR1-32B & L63 & 0.826* & 0.754 & 0.741 & 0.737 & 0.721 \\\\\nQwQ-32B & L60 & 0.740 & 0.740 & 0.742 & 0.735 & 0.731 \\\\\nR1-8B & L14 & 0.778 & 0.790 & 0.781 & 0.793 & 0.802 \\\\\nOT-7B & L16 & 0.663 & 0.688* & 0.678 & 0.668 & 0.659 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Balanced accuracy of HS temporal probes by window size. R1-8B improves with larger $W$; R1-32B \\emph{degrades} ($-$10.5pp by W=15) due to dimensionality constraints (51,200 $\\times$ $W$ features for $n{=}20$). * marks best $W$ per model.}\n\\label{tab:temporal}\n\\end{table}\n\nText probes improve universally with larger windows across all four models. HS temporal improvement is model-dependent: R1-8B benefits monotonically (0.778$\\to$0.802), OT-7B peaks at W=3 (0.688) then declines, QwQ-32B is flat, and R1-32B degrades sharply due to the curse of dimensionality ($51{,}200 \\times W$ features with only $n{=}20$ samples).\n\n\\paragraph{Precision--coverage tradeoff.}\nLarger windows universally increase precision and decrease coverage. At the best window per model, coverage ranges from 48.8\\% (R1-8B, W=25, precision 0.822) to 70.0\\% (R1-32B, W=10, precision 0.609). No operating point achieves $>$0.70 precision and $>$0.60 coverage simultaneously.\n\n\\subsection{Alternative Methods: Comprehensive Negative Results}\n\n\\paragraph{Mahalanobis distance.}\nTrajGuard-style Mahalanobis distance fails on all four models. Table~\\ref{tab:mahal} shows that safe vs.\\ post-commitment separation is negligible (max $+$0.20 on QwQ-32B), with false alarms exceeding true positives at every threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{Safe MD} & \\textbf{Post-CP MD} & \\textbf{Sep.} \\\\\n\\midrule\nR1-8B & L14 & 6.66 & 6.73 & +0.07 \\\\\nOT-7B & L16 & 7.68 & 7.71 & +0.03 \\\\\nR1-32B & L63 & 6.73 & 6.88 & +0.15 \\\\\nQwQ-32B & L60 & 3.22 & 3.42 & +0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mahalanobis distance from safe-trace covariance. Separation is $<$0.21 for all models; false alarm rate exceeds true positive rate at every threshold.}\n\\label{tab:mahal}\n\\end{table}\n\n\\paragraph{BOCPD and CUSUM.}\nBOCPD detects commitment on only 1/4 models (R1-8B, 93\\% detection, lead $+$3.45 steps). On the remaining three models, detection rate is 0\\%. CUSUM detects on 3/4 models but achieves worse lead time than simple first-crossing-point (FCP) thresholds on all models (Table~\\ref{tab:cpd}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{BOCPD \\%} & \\textbf{BOCPD Lead} & \\textbf{CUSUM \\%} & \\textbf{FCP \\%} & \\textbf{FCP Lead} \\\\\n\\midrule\nR1-8B & 93 & +3.45 & 65 & 65 & +4.89 \\\\\nOT-7B & 0 & --- & 75 & 89 & +11.83 \\\\\nR1-32B & 0 & --- & 85 & 95 & +5.68 \\\\\nQwQ-32B & 0 & --- & 74 & 79 & +9.40 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Change-point detection methods. BOCPD fails on 3/4 models. FCP (simple threshold) achieves comparable or better detection and lead time than both BOCPD and CUSUM.}\n\\label{tab:cpd}\n\\end{table}\n\n\\paragraph{GRU sequence model.}\nGRU does not outperform temporal LR on balanced accuracy for 3/4 models ($-$6.2pp on R1-32B, $-$3.7pp on QwQ-32B, $+$0.3pp on R1-8B). On OT-7B, GRU achieves $+$5.8pp over LR but at the cost of 2.7$\\times$ higher FPR (0.274 vs.\\ 0.100). GRU trades accuracy for coverage and lead time via higher false positive rates (Table~\\ref{tab:gru}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{LR BA} & \\textbf{GRU BA} & \\textbf{$\\Delta$} & \\textbf{GRU FPR} \\\\\n\\midrule\nR1-32B & 0.737 & 0.675 & $-$6.2 & 0.135 \\\\\nQwQ-32B & 0.761 & 0.724 & $-$3.7 & 0.289 \\\\\nOT-7B & 0.688 & 0.746 & +5.8 & 0.274 \\\\\nR1-8B & 0.806 & 0.809 & +0.3 & 0.165 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GRU vs.\\ temporal LR. GRU improves over LR on only 1/4 models (OT-7B), confirming linear probes are at or near the information ceiling for this task.}\n\\label{tab:gru}\n\\end{table}\n\n\\paragraph{16-label taxonomy.}\nFine-grained supervision (16 labels) provides marginal improvement after binary collapse: $+$0.6 to $+$1.1pp across models (Table~\\ref{tab:taxonomy}). Raw 16-class accuracy is low (26--41\\%), indicating that transition subtypes are not cleanly separable in hidden-state space.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Binary} & \\textbf{16-Label} & \\textbf{16$\\to$Bin} & \\textbf{$\\Delta$} \\\\\n\\midrule\nR1-8B & 0.817 & 0.41 & 0.825 & +0.8 \\\\\nOT-7B & 0.688 & 0.35 & 0.699 & +1.1 \\\\\nQwQ-32B & 0.740 & 0.26 & 0.749 & +0.9 \\\\\nR1-32B & 0.826 & 0.28 & 0.832 & +0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{16-label vs.\\ binary supervision. After collapsing 16 labels to binary, improvement is marginal ($\\leq$1.1pp), suggesting linear probes are saturated at the binary detection boundary.}\n\\label{tab:taxonomy}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\nProbes trained on one model and tested on another fail comprehensively (Table~\\ref{tab:transfer}). The best cross-model accuracy is 67.3\\% (within the Qwen-32B family), far below within-model performance and barely above the 50\\% chance baseline. Cross-family transfer (Llama$\\leftrightarrow$Qwen) is at chance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Train $\\to$} & \\textbf{R1-8B} & \\textbf{OT-7B} & \\textbf{R1-32B} & \\textbf{QwQ} \\\\\n\\midrule\nR1-8B & \\textit{0.817} & --- & 0.522 & 0.595 \\\\\nOT-7B & --- & \\textit{0.688} & --- & --- \\\\\nR1-32B & 0.583 & --- & \\textit{0.826} & 0.673 \\\\\nQwQ-32B & --- & --- & 0.673 & \\textit{0.740} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer accuracy. Self-accuracy (diagonal, italic) far exceeds any transfer pair. The best transfer (67.3\\%, Qwen-32B internal) is 7--15pp below self-accuracy. Cross-family transfer is at chance.}\n\\label{tab:transfer}\n\\end{table}\n\n\\subsection{Lead Time Analysis}\n\nTable~\\ref{tab:lead} compares lead time---steps between first detection and commitment point---across methods and models. Results are mixed: R1-8B HS detects \\emph{at} the commitment point (lead $\\approx$0), QwQ-32B HS has negative lead ($-$1.2 to $+$1.9 steps), and only R1-32B shows substantial positive HS lead ($+$11.7 to $+$13.3 steps), but at only 25\\% coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Lead} & \\textbf{Text Lead} & \\textbf{HS BA} & \\textbf{Pos BA} \\\\\n\\midrule\nR1-8B (W=15) & $-$0.1 & +10.3$\\dagger$ & 0.802 & --- \\\\\nOT-7B (W=3) & +21.6$\\ddagger$ & +45.5$\\ddagger$ & 0.688 & --- \\\\\nQwQ-32B (W=3) & $-$1.2 to +1.9 & +3.7 to +12.3 & 0.740 & 0.746 \\\\\nR1-32B (W=1) & +11.7 to +13.3 & --- & 0.826 & 0.686 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{HS vs.\\ text lead time. $\\dagger$: inflated by high pre-CP FPR. $\\ddagger$: inflated by long traces ($\\sim$80 sentences). QwQ-32B position baseline (Pos BA) exceeds HS BA, questioning the value of white-box access for that model.}\n\\label{tab:lead}\n\\end{table}\n\n\\paragraph{Oracle decomposition.}\nOracle labels show gradual safety erosion pre-commitment ($+$27 to $+$31 step lead), while HS probes detect only at or near the commitment point. The 26--28 step gap between oracle and probe lead times indicates that hidden states encode \\emph{current} safety state rather than the \\emph{trajectory} toward commitment. On R1-8B, oracle label autocorrelation is 0.82 pre-CP (gradual transition) while HS entropy is 0.41 (step-function).\n\n\\subsection{False Positive Analysis}\n\\label{sec:fpr}\n\nTable~\\ref{tab:fpr_safe} reports false positive rates on safe traces---traces where the model never commits to harmful output. No method achieves simultaneously low FPR, high precision, and high coverage.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Static} & \\textbf{HS Temp} & \\textbf{Text Temp} & \\textbf{GRU} \\\\\n\\midrule\nR1-8B & 0.390 & 0.392 & 0.385 & 0.521 \\\\\nOT-7B & 0.111 & 0.175 & 0.460 & --- \\\\\nQwQ-32B & 0.500 & 0.450 & 0.425 & --- \\\\\nR1-32B & 0.239 & 0.239 & 0.310 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Safe-trace false positive rates. Median FPR $\\approx$0.39 across methods. QwQ-32B HS FPR (0.45--0.50) \\emph{exceeds} text FPR (0.325--0.425).}\n\\label{tab:fpr_safe}\n\\end{table}\n\n\\paragraph{Deployment viability.}\nWe define three practical criteria: safe FPR $<$20\\%, precision $>$70\\%, and coverage $>$60\\%. Only 1/4 models meets each criterion individually (OT-7B for FPR, R1-8B for precision at W$\\geq$15, R1-8B/R1-32B for coverage at small W). Zero models meet all three simultaneously.\n\n\\subsection{Bootstrap Confidence Intervals}\n\\label{sec:bootstrap}\n\nTable~\\ref{tab:hb_full} presents the full Holm--Bonferroni step-down procedure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{clccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Model/Metric} & \\textbf{$p$} & \\textbf{HB Thr.} & \\textbf{Pass} \\\\\n\\midrule\n1 & R1-8B / precision & $<$.001 & .0042 & \\checkmark \\\\\n2 & OT-7B / bal\\_acc & $<$.001 & .0045 & \\checkmark \\\\\n3 & OT-7B / precision & $<$.001 & .0050 & \\checkmark \\\\\n4 & OT-7B / FPR & $<$.001 & .0056 & \\checkmark \\\\\n5 & QwQ / bal\\_acc & $<$.001 & .0063 & \\checkmark \\\\\n6 & QwQ / precision & $<$.001 & .0071 & \\checkmark \\\\\n7 & R1-32B / bal\\_acc & $<$.001 & .0083 & \\checkmark \\\\\n8 & R1-32B / precision & $<$.001 & .0100 & \\checkmark \\\\\n9 & QwQ / FPR & .004 & .0125 & \\checkmark \\\\\n10 & R1-8B / bal\\_acc & .005 & .0167 & \\checkmark \\\\\n11 & R1-32B / FPR & .007 & .0250 & \\checkmark \\\\\n12 & R1-8B / FPR & .044 & .0500 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Holm--Bonferroni step-down results. 12/12 pass ($\\alpha{=}0.05$). Tests ranked by $p$-value. CI widths for 32B models are wide ($\\sim$0.12--0.15 for BA) due to small $n$.}\n\\label{tab:hb_full}\n\\end{table}\n\n\\subsection{Ensemble Cross-Validation (7--8B)}\n\nFive-fold cross-validated ensembles of metric-weighted layer selections on 7--8B models confirm HS advantage over text (Table~\\ref{tab:ensemble}). Ensemble precision is lower than the best single metric on R1-8B (0.565 vs.\\ 0.604) but slightly higher on OT-7B (0.506 vs.\\ 0.473).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Ens.\\ Prec} & \\textbf{Best Single} & \\textbf{Text Prec} & \\textbf{Ens vs.\\ Text $p$} \\\\\n\\midrule\nR1-8B & 0.565 & 0.604 & 0.372 & $<$0.002 \\\\\nOT-7B & 0.506 & 0.473 & 0.236 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-validated ensemble results on 7--8B models. HS advantage over text is validated under CV ($p \\leq 0.002$).}\n\\label{tab:ensemble}\n\\end{table}\n\n\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nOur central finding is that layer selection metric choice is a potent confound in hidden-state safety evaluation. The composite \\texttt{bal\\_acc $\\times$ crossing\\_rate} selects shallow layers for 32B models (3--16\\% depth), where probe signal is weakest, entirely masking the HS advantage. Three of four non-biased metrics converge on deep layers (94--98\\%), while threshold-free balanced accuracy selects middle layers (47--73\\%). This divergence constitutes a second axis of researcher degrees of freedom beyond the crossing-rate bias. We recommend that future work report HS evaluation results under \\emph{at least} three selection criteria spanning threshold-dependent and threshold-free metrics.\n\n\\paragraph{Cost-benefit analysis.}\nHS probes yield $+$15--24pp precision over text probes. This advantage requires: (a) local model hosting (no API access), (b) inference pipeline modification for intermediate activation extraction, (c) per-model layer selection and probe training. Text probes require only access to the generated CoT---available in any deployment. At text precision of 0.33--0.49 (1 true alarm per 2--3 triggers) vs.\\ HS precision of 0.47--0.78 (1 per 1.3--2.1 triggers), the marginal improvement may not justify white-box infrastructure costs for many deployment settings.\n\n\\paragraph{Fundamental limitation: reactive, not predictive.}\nOracle decomposition reveals a 26--28 step gap between what text labels encode (gradual erosion) and what HS probes detect (step-function at commitment). Hidden states encode the model's \\emph{current} safety state, not the trajectory toward commitment. For deployment, trajectory prediction provides earlier warning, suggesting text-based monitoring of reasoning patterns---while noisier---may be the more promising research direction for early detection.\n\n\\paragraph{Cross-model transfer failure.}\nComplete transfer failure (best 67.3\\%) implies that safety commitment encoding is model-specific. Every new model requires its own probe training with labeled commitment points, a supervision cost that limits practical scalability. Combined with the engineering cost of white-box access, the deployment case for HS monitoring is substantially weakened.\n\n\n\\section{Conclusion}\n\nWe present the first systematic evaluation of safety commitment detection in reasoning models, comparing seven methods across four models. Our primary contribution is the discovery that layer selection metric choice is a critical confounder: the composite metric \\texttt{bal\\_acc $\\times$ crossing\\_rate} systematically biases toward shallow layers at 32B scale, reversing conclusions about hidden-state monitoring efficacy. After correction, HS probes significantly outperform text probes (12/12 Holm--Bonferroni, precision $+$15--24pp), but this statistical advantage must be weighed against practical limitations: no method achieves deployment-ready performance (0/4 models meet all practical criteria), safe-trace FPR is 39\\% at the median, cross-model transfer fails, and hidden states are reactive rather than predictive. We release our multi-metric audit framework and urge the community to adopt multi-criterion layer selection reporting as standard practice.\n\n\n\\section*{Limitations}\n\nOur evaluation has three principal limitations. First, test set sizes for 32B models ($n{=}19$--20) yield wide confidence intervals; the R1-32B residualized HS-text gap ($+$1.9pp) is below the minimum detectable effect (11.2pp at 80\\% power), so the non-significant result reflects a power limitation rather than evidence of absence. Second, the text baseline uses a single encoder (all-MiniLM-L6-v2); stronger encoders or LLM-based classifiers would likely narrow the HS-text gap. Third, all probes are trained on commitment-point annotations that themselves require human judgment, introducing a potential source of label noise.\n\n\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{10}\n\n\\bibitem[\\protect\\citename{DeepSeek-AI}2025]{deepseekai2025deepseekr1}\nDeepSeek-AI. 2025.\n\\newblock DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning.\n\\newblock {\\em arXiv preprint arXiv:2501.12948}.\n\n\\bibitem[\\protect\\citename{Qwen Team}2025]{qwq32b}\nQwen Team. 2025.\n\\newblock QwQ: Reflect deeply on the boundaries of the unknown.\n\\newblock Blog post.\n\n\\bibitem[\\protect\\citename{Wen et al.}2025]{wen2025thinkingmakesllmssusceptible}\nSijia Wen, Haoran Li, and Yixin Cao. 2025.\n\\newblock Thinking makes LLMs susceptible to jailbreaking.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2025]{zhou2025hiddenriskslargereasoning}\nYihe Zhou, et al. 2025.\n\\newblock Hidden risks of large reasoning models.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Wang et al.}2024]{wang2024mitigating}\nZhixin Wang, et al. 2024.\n\\newblock Mitigating jailbreak attacks via trajectory-aware guard.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Ji et al.}2024]{ji2024llmguard}\nZiwei Ji, et al. 2024.\n\\newblock LLM guard: Defending LLMs against jailbreaks via internal state monitoring.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inferencetime}\nKenneth Li, et al. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock {\\em NeurIPS 2024}.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, et al. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock {\\em ICLR 2023}.\n\n\\bibitem[\\protect\\citename{Zou et al.}2023]{zou2023representation}\nAndy Zou, et al. 2023.\n\\newblock Representation engineering: A top-down approach to AI transparency.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Belrose et al.}2023]{belrose2023eliciting}\nNora Belrose, et al. 2023.\n\\newblock Eliciting latent predictions from transformers with the tuned lens.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Zheng et al.}2025]{zheng2025safethink}\nZheng Zheng, et al. 2025.\n\\newblock SafeThink: Safe thinking for LLM reasoning.\n\\newblock {\\em arXiv preprint}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a77a7c5d-93c5-475f-a3ce-c44b14676083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace…",
  "leafUuid": "db54068a-8a47-44c0-afaf-c84700985670",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated worst-tier research paper",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Assistant

_source line 26 · 2026-05-21T22:01:18.919Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db54068a-8a47-44c0-afaf-c84700985670",
  "isSidechain": false,
  "requestId": "req_011CbGU43PeNo8iyc4c1SfkL",
  "type": "assistant",
  "uuid": "6f6e036d-7780-491e-871a-6d63e64b46a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGgBFihgs5UwnkBL7FahGR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 57590,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 27 · 2026-05-21T22:01:20.381Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RHzVNXfMSDq9YijtgcuSsc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f6e036d-7780-491e-871a-6d63e64b46a1",
  "isSidechain": false,
  "requestId": "req_011CbGU43PeNo8iyc4c1SfkL",
  "type": "assistant",
  "uuid": "9118811f-139e-4203-9a3b-06074d361593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGgBFihgs5UwnkBL7FahGR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 57590,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 28 · 2026-05-21T22:01:20.551Z_

<details><summary>↩ Tool result · `toolu_01RHzVNXfMSDq9YijtgcuSsc`</summary>

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
  "parentUuid": "9118811f-139e-4203-9a3b-06074d361593",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "80e9fec1-14c1-4494-98be-fd1566e426e0",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9118811f-139e-4203-9a3b-06074d361593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T22:01:24.792Z_

<details><summary>Logged reasoning block</summary>

```text
The EMNLP style file is not available. Let me switch to a generic article class or find if there's a style file available somewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e9fec1-14c1-4494-98be-fd1566e426e0",
  "isSidechain": false,
  "requestId": "req_011CbGU4TagiVQSExW6qerNj",
  "type": "assistant",
  "uuid": "69d77dca-2ddf-49b2-a0f1-88c6fe04241a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ksjLBjfrpQbQ3qHxPpZJc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 68672,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 68672,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 452
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

_source line 30 · 2026-05-21T22:01:25.315Z_

Missing style file. Let me fix to use a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d77dca-2ddf-49b2-a0f1-88c6fe04241a",
  "isSidechain": false,
  "requestId": "req_011CbGU4TagiVQSExW6qerNj",
  "type": "assistant",
  "uuid": "2bc8469c-9c67-40ff-b14d-623c9f406cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ksjLBjfrpQbQ3qHxPpZJc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 68672,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 68672,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 452
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

_source line 31 · 2026-05-21T22:01:26.632Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NCVrQy81EcH4j7eq3QDVG1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}",
  "new_string": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc8469c-9c67-40ff-b14d-623c9f406cb9",
  "isSidechain": false,
  "requestId": "req_011CbGU4TagiVQSExW6qerNj",
  "type": "assistant",
  "uuid": "691491cc-0aa8-4f23-87bd-6547e79db351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ksjLBjfrpQbQ3qHxPpZJc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 68672,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 68672,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 452
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

_source line 32 · 2026-05-21T22:01:26.650Z_

<details><summary>↩ Tool result · `toolu_01NCVrQy81EcH4j7eq3QDVG1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "691491cc-0aa8-4f23-87bd-6547e79db351",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "ff4a2292-d61f-45fb-ad02-f583e5c70a2b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}",
    "newString": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "691491cc-0aa8-4f23-87bd-6547e79db351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-21T22:01:26.685Z_

```json
{
  "parentUuid": "ff4a2292-d61f-45fb-ad02-f583e5c70a2b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0fcdc923-0aa5-4f46-9a63-e4b419055761",
  "timestamp": "2026-05-21T22:01:26.685Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 34 · 2026-05-21T22:01:30.787Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019J2divKmPAyp4gLGM7Mdpp`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fcdc923-0aa5-4f46-9a63-e4b419055761",
  "isSidechain": false,
  "requestId": "req_011CbGU4unH7acPgZrE48yVH",
  "type": "assistant",
  "uuid": "bdfc3084-8a51-418b-9958-a2eebff2eddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcR1F44cMVit89iCaQzsJa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 69124,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 69124,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
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

_source line 35 · 2026-05-21T22:01:31.180Z_

<details><summary>↩ Tool result · `toolu_019J2divKmPAyp4gLGM7Mdpp`</summary>

```text
LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/
msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 152880 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdfc3084-8a51-418b-9958-a2eebff2eddc",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "c3ba5783-6ce8-4cc2-bbdd-5aaa1cd1bb5c",
  "toolUseResult": {
    "stdout": "LaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/\nmsam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 152880 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bdfc3084-8a51-418b-9958-a2eebff2eddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T22:01:34.775Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FVWoW1y1jHoiixBJSghfnp`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ba5783-6ce8-4cc2-bbdd-5aaa1cd1bb5c",
  "isSidechain": false,
  "requestId": "req_011CbGU5F3eUyfzFPiCAduLZ",
  "type": "assistant",
  "uuid": "189b7a4e-1eb4-410c-968d-0b6ce2df70da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ve3igmKdX8LGFASxHKmq7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 69575,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 69575,
          "cache_creation_input_tokens": 592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 592
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

_source line 37 · 2026-05-21T22:01:35.184Z_

<details><summary>↩ Tool result · `toolu_01FVWoW1y1jHoiixBJSghfnp`</summary>

```text
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 152692 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "189b7a4e-1eb4-410c-968d-0b6ce2df70da",
  "isSidechain": false,
  "promptId": "4855b02b-bee5-4346-b12c-a0d2349fe757",
  "type": "user",
  "uuid": "dbc31847-f0fc-47be-b470-c6fd5b5d94aa",
  "toolUseResult": {
    "stdout": "usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 152692 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "189b7a4e-1eb4-410c-968d-0b6ce2df70da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T22:01:46.143Z_

编译成功，10 页 PDF 已生成。

`paper.tex` 采用 **Methodology-first framing (approach B)**：以 layer selection bias 为核心发现，HS-vs-text 作为支撑证据。覆盖了 `experiment_data.json` 中全部 14 个实验：

- **Layer selection bias** (§4.1) — 5 metrics × 4 models table
- **HS vs Text at corrected layers** (§4.2) — 12/12 HB summary + BA-layer robustness
- **Temporal window effects** (§4.3) — 4-model window sweep + precision-coverage tradeoff
- **Mahalanobis, BOCPD/CUSUM, GRU, 16-label taxonomy** (§4.4) — each with dedicated table
- **Cross-model transfer** (§4.5) — transfer matrix
- **Lead time + oracle decomposition** (§4.6)
- **False positive analysis + deployment viability** (§4.7)
- **Bootstrap HB full table** (§4.8)
- **Ensemble CV** (§4.9)

所有数字直接来自 JSON 数据，Discussion 包含 cost-benefit 分析和"reactive not predictive"定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc31847-f0fc-47be-b470-c6fd5b5d94aa",
  "isSidechain": false,
  "requestId": "req_011CbGU5Y9o11cBgPyJyHBeD",
  "type": "assistant",
  "uuid": "793748e1-f30a-4847-acaf-6b2c50079b3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260521T212242/worst",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3oXUHPYqTQphUcmb6r51R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 70167,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 331,
          "cache_read_input_tokens": 70167,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T212242 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace…",
  "leafUuid": "793748e1-f30a-4847-acaf-6b2c50079b3d",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated worst-tier research paper",
  "sessionId": "57971aef-fe55-48e4-84c1-753372b1ed10"
}
```

---
