# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd.jsonl`
- **Structured JSON:** [`02f972ad5975c25f6623.json`](../../sessions/02/02f972ad5975c25f6623.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:15:59.389Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:15:59.389Z",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：完全放弃 SDGD 方法贡献。论文 reframe 为纯系统性实证分析：首次控制实验揭示 schema complexity 不是一维问题——count 和 confusability 通过正交通道降低性能， 但 confusability 信号高度依赖模型和 embedding 选择。pairwise confusability 是 比 per-type 聚合更鲁棒的度量，但仅在特定 model×embedding×schema 组合下显著。 centrality confound 发现本身是方法论贡献。模型特异性（Qwen3 vs LLaMA）reframe 为 \"confusability effects are model-dependent\"——将弱点转为解释力。论文结构改为 \"question→controlled experiments→findings→implications\"。EMNLP Findings 是现实 预期，Main 可冲但 acceptance variance 大。SDGD 降为 appendix 中的 negative result case study，正文不再作为核心贡献。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T12:15:59.392Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:15:59.392Z",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-15T12:15:59.411Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：完全放弃 SDGD 方法贡献。论文 reframe 为纯系统性实证分析：首次控制实验揭示 schema complexity 不是一维问题——count 和 confusability 通过正交通道降低性能， 但 confusability 信号高度依赖模型和 embedding 选择。pairwise confusability 是 比 per-type 聚合更鲁棒的度量，但仅在特定 model×embedding×schema 组合下显著。 centrality confound 发现本身是方法论贡献。模型特异性（Qwen3 vs LLaMA）reframe 为 "confusability effects are model-dependent"——将弱点转为解释力。论文结构改为 "question→controlled experiments→findings→implications"。EMNLP Findings 是现实 预期，Main 可冲但 acceptance variance 大。SDGD 降为 appendix 中的 negative result case study，正文不再作为核心贡献。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "e0eecb8d-b6b0-44f1-a08c-1428cfba527d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:15:59.410Z_

```json
{
  "parentUuid": "e0eecb8d-b6b0-44f1-a08c-1428cfba527d",
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
  "uuid": "8a49713e-1118-4f8f-bdac-0de74b140b33",
  "timestamp": "2026-05-15T12:15:59.410Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:15:59.410Z_

```json
{
  "parentUuid": "8a49713e-1118-4f8f-bdac-0de74b140b33",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8f828fa0-d5b0-4396-8e64-671f8237f174",
  "timestamp": "2026-05-15T12:15:59.410Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
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
  "aiTitle": "Generate simulated research paper",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Assistant

_source line 7 · 2026-05-15T12:16:17.456Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f828fa0-d5b0-4396-8e64-671f8237f174",
  "isSidechain": false,
  "requestId": "req_011Cb4La36eLKxXttinNyBvX",
  "type": "assistant",
  "uuid": "5be0e3af-105c-4e9b-9bec-2e3aee0d526a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4pQCCYrMAufk3dnQJb8ix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11312,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11312
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

_source line 8 · 2026-05-15T12:16:18.463Z_

<details open><summary>🔧 Tool call — Read · `toolu_019xeLWmub97KhtjBQucHdAM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5be0e3af-105c-4e9b-9bec-2e3aee0d526a",
  "isSidechain": false,
  "requestId": "req_011Cb4La36eLKxXttinNyBvX",
  "type": "assistant",
  "uuid": "0bc9200d-5bae-4048-af03-971f6aeb153c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4pQCCYrMAufk3dnQJb8ix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11312,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11312
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

_source line 9 · 2026-05-15T12:16:18.836Z_

<details open><summary>🔧 Tool call — Read · `toolu_015hLztxoUbubHXgfkxXjS84`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bc9200d-5bae-4048-af03-971f6aeb153c",
  "isSidechain": false,
  "requestId": "req_011Cb4La36eLKxXttinNyBvX",
  "type": "assistant",
  "uuid": "17ea4f15-0450-4707-b182-932770fd0fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4pQCCYrMAufk3dnQJb8ix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11312,
      "cache_read_input_tokens": 11841,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11312
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

_source line 10 · 2026-05-15T12:16:18.871Z_

<details><summary>↩ Tool result · `toolu_019xeLWmub97KhtjBQucHdAM`</summary>

```text
1	[
2	  {
3	    "name": "MAVEN Full Confusability Study",
4	    "description": "MAVEN Event Detection（168 event types, FrameNet hierarchy）的完整 confusability 研究：500-sample 重跑 count curve + within-count BCS 相关 + pairwise/per-type 双 embedding 分析 + confusion rate 分析。核心跨任务（NER→ED）验证。\n",
5	    "results": {
6	      "count_curve_relaxed_f1": {
7	        "count_1": 0.098,
8	        "count_6": 0.112,
9	        "count_12": 0.155,
10	        "count_22": 0.192,
11	        "count_44": 0.238,
12	        "count_64": 0.241,
13	        "count_100": 0.243
14	      },
15	      "count_curve_exact_f1": {
16	        "count_1": 0.008,
17	        "count_6": 0.005,
18	        "count_12": 0.011,
19	        "count_22": 0.016,
20	        "count_44": 0.021,
21	        "count_64": 0.018
22	      },
23	      "count_curve_recall_trend": "monotonically increasing 0.07→0.19 (opposite of Few-NERD)",
24	      "count_curve_precision_trend": "roughly flat 0.15-0.40, noisy",
25	      "within_count_bcs_f1": {
26	        "count_6": {
27	          "r": 0.175,
28	          "p": 0.185,
29	          "n": 27,
30	          "direction": "positive",
31	          "verdict": "FAIL"
32	        },
33	        "count_12": {
34	          "r": 0.124,
35	          "p": 0.315,
36	          "n": 27,
37	          "direction": "positive",
38	          "verdict": "FAIL"
39	        },
40	        "partial_pooled": {
41	          "r": 0.142,
42	          "p": 0.108,
43	          "n": 54,
44	          "direction": "positive",
45	          "verdict": "FAIL"
46	        }
47	      },
48	      "pairwise_qwen3": {
49	        "pearson_r": -0.009,
50	        "pearson_p": 0.38,
51	        "n_pairs": 14028,
52	        "verdict": "FAIL"
53	      },
54	      "pairwise_minilm": {
55	        "pearson_r": 0.115,
56	        "pearson_p": 2.1e-42,
57	        "n_pairs": 14028,
58	        "spearman_rho": 0.128,
59	        "nonzero_spearman_rho": 0.185,
60	        "verdict": "PASS"
61	      },
62	      "per_type_qwen3": {
63	        "spearman_rho": 0.195,
64	        "p": 0.018,
65	        "direction": "positive_confounded"
66	      },
67	      "per_type_minilm": {
68	        "spearman_rho": 0.212,
69	        "p": 0.009,
70	        "direction": "positive_confounded"
71	      },
72	      "confusion_rate_extreme": {
73	        "count_6_ratio": 5.8,
74	        "count_12_ratio": 4.2
75	      },
76	      "confusion_rate_random": {
77	        "count_6_ratio": 1.4,
78	        "count_12_ratio": 1.3
79	      }
80	    },
81	    "tables": [
82	      "Table: MAVEN Count Curve (500 samples, relaxed matching)\n| Count | Relaxed F1 | Exact F1 | Recall | Precision | Pred/Gold |\n|-------|-----------|----------|--------|-----------|-----------|\n| 1     | 0.098     | 0.008    | 0.070  | 0.162     | 0.43      |\n| 6     | 0.112     | 0.005    | 0.085  | 0.165     | 0.52      |\n| 12    | 0.155     | 0.011    | 0.118  | 0.226     | 0.52      |\n| 22    | 0.192     | 0.016    | 0.148  | 0.274     | 0.54      |\n| 44    | 0.238     | 0.021    | 0.180  | 0.350     | 0.51      |\n| 64    | 0.241     | 0.018    | 0.182  | 0.358     | 0.51      |\n",
83	      "Table: MAVEN Within-Count BCS-F1 Correlation\n| Count | r     | p     | Direction | Verdict |\n|-------|-------|-------|-----------|---------|\n| 6     | +0.175| 0.185 | positive  | FAIL    |\n| 12    | +0.124| 0.315 | positive  | FAIL    |\n| Pooled| +0.142| 0.108 | positive  | FAIL    |\n",
84	      "Table: MAVEN Pairwise & Per-Type (2×2 embedding matrix)\n|          | Pairwise r (p)         | Per-type ρ (p)       |\n|----------|------------------------|----------------------|\n| Qwen3    | -0.009 (0.38) ✗        | +0.195 (0.018) ✗     |\n| MiniLM   | +0.115 (2.1e-42) ✓     | +0.212 (0.009) ✗     |\n"
85	    ],
86	    "figures": [],
87	    "analysis": "MAVEN 结果确认 centrality confound 假说：在语义同质 schema 中，per-type 和 within-count batch-level 分析均被 confound。唯一存活的信号是 MiniLM pairwise (r=0.115)，但 Qwen3 pairwise 失败，且效应量小（r²=1.3%）。MAVEN 的 count curve 反转是对 SDGD 方法的致命打击——如果更多 types 在 prompt 中反而帮助模型，那么 decomposition（减少 types）必然降低性能。worst tier 叙事中，MAVEN 作为 \"centrality confound case study\" 仍有方法论价值，但不支持 SDGD 的前提假设。\n\n\nMAVEN 的 168 event types 全部来自 FrameNet，同一语义域，导致 type embedding 分布高度同质。这造成三个后果：(1) count curve 反转——更多 types 为模型提供更 丰富的 event ontology 上下文，帮助模型理解每个 type 在 taxonomy 中的位置，因此 F1 随 count 增加而上升；(2) within-count BCS 相关为正方向——高 BCS batch 包含 语义中心的常见 event types（如 Killing, Attack, Movement），这些 types 在 training data 中频次高、定义清晰，LLM 本就擅长提取，因此高 BCS → 高 F1， 这是 centrality confound 而非 confusability 效应；(3) confusion rate 比 Few-NERD 低得多（5.8x vs 27.5x），因为 event trigger 本身是 verb/nominalization 而非 entity mention，type confusion 的表现形式不同（trigger 共享率高但不一定是 confusability 导致）。pairwise MiniLM 仍显著（r=0.115, p≈0），因为 n=14028 pair 提供了极大统计功效，即使效应量小也能检出——但这个 r 值比 Few-NERD 的 0.156 低， 且 Qwen3 pairwise 完全不显著，说明 pairwise 信号在同质 schema 上高度依赖 embedding 选择。\n"
88	  },
89	  {
90	    "name": "DocRED Confusability Study",
91	    "description": "DocRED（96 relation types）上的 confusability 研究：count curve + BCS 相关分析。 文档级 RE 的 scaling stress test。\n",
92	    "results": {
93	      "count_curve_f1": {
94	        "count_4": 0.185,
95	        "count_8": 0.192,
96	        "count_16": 0.198,
97	        "count_32": 0.203,
98	        "count_48": 0.208,
99	        "count_96": 0.195
100	      },
101	      "count_curve_trend": "near-flat with slight peak at count_48, no clear monotonic pattern",
102	      "within_count_bcs_f1": {
103	        "count_8": {
104	          "r": 0.032,
105	          "p": 0.62,
106	          "verdict": "FAIL"
107	        },
108	        "count_16": {
109	          "r": -0.058,
110	          "p": 0.48,
111	          "verdict": "FAIL"
112	        },
113	        "partial_pooled": {
114	          "r": -0.015,
115	          "p": 0.84,
116	          "verdict": "FAIL"
117	        }
118	      },
119	      "pairwise_qwen3": {
120	        "pearson_r": 0.023,
121	        "pearson_p": 0.14,
122	        "n_pairs": 4560,
123	        "verdict": "FAIL"
124	      },
125	      "pairwise_minilm": {
126	        "pearson_r": 0.031,
127	        "pearson_p": 0.08,
128	        "n_pairs": 4560,
129	        "verdict": "FAIL"
130	      },
131	      "per_type_bcs_f1": {
132	        "spearman_rho": -0.04,
133	        "p": 0.72,
134	        "verdict": "FAIL"
135	      },
136	      "confusion_rate_extreme_ratio": 1.8,
137	      "overall_baseline_f1": 0.195
138	    },
139	    "tables": [
140	      "Table: DocRED Count Curve (document-level RE)\n| Count | F1    | Recall | Precision | Confusion Rate |\n|-------|-------|--------|-----------|---------------|\n| 4     | 0.185 | 0.145  | 0.256     | 0.008         |\n| 8     | 0.192 | 0.152  | 0.261     | 0.012         |\n| 16    | 0.198 | 0.158  | 0.264     | 0.015         |\n| 32    | 0.203 | 0.165  | 0.258     | 0.018         |\n| 48    | 0.208 | 0.170  | 0.261     | 0.019         |\n| 96    | 0.195 | 0.160  | 0.250     | 0.022         |\n"
141	    ],
142	    "figures": [],
143	    "analysis": "DocRED 结果是完全的 null result。confusability 假说在文档级 RE 上完全不成立。 worst tier 叙事中，DocRED 证明 confusability 效应受限于 sentence-level 任务—— 文档级任务中其他复杂度维度（跨句推理、entity pair 组合）占主导。如果论文要报告 此结果，需要 reframe 为 \"boundary condition\"：confusability 效应在 type definitions 占 prompt 显著比例的任务中才成立。但此实验为 P1，worst tier 下可能 不运行（10 天内优先 P0 实验），视为 supplementary material。\n\n\nDocRED 是文档级 RE，每个样本包含多个句子和多个 entity pairs。性能瓶颈完全不在 type confusability 上，而在于：(1) 跨句推理能力——关系证据分散在多个句子中，LLM 需要 coreference 和 multi-hop reasoning；(2) entity pair 组合爆炸——文档中 n 个实体产生 O(n²) 个候选关系对，模型必须处理大量负样本；(3) 关系类型定义本身 依赖 entity type 约束（如 \"place_of_birth\" 要求 subject=person, object=location）， 这种结构化约束比 embedding 相似度更能预测性能。confusability 信号被这些更强的 因素完全淹没。count curve 近乎平坦，因为文档级 RE 的 prompt 长度主要由文档内容 （而非 type 定义）决定——96 个 relation type name 只占 prompt 的很小比例。\n"
144	  },
145	  {
146	    "name": "Count × Confusability Interaction Effect",
147	    "description": "Few-NERD 上 {low count=6, high count=22} × {low BCS, high BCS} 的 2×2 因子设计。 检验 count 和 confusability 的交互效应（additive vs multiplicative）。\n",
148	    "results": {
149	      "cell_means_f1": {
150	        "low_count_low_bcs": 0.348,
151	        "low_count_high_bcs": 0.312,
152	        "high_count_low_bcs": 0.298,
153	        "high_count_high_bcs": 0.255
154	      },
155	      "two_way_anova": {
156	        "count_main_effect": {
157	          "F": 7.82,
158	          "p": 0.008,
159	          "eta_sq": 0.14,
160	          "verdict": "SIGNIFICANT"
161	        },
162	        "bcs_main_effect": {
163	          "F": 2.93,
164	          "p": 0.094,
165	          "eta_sq": 0.06,
166	          "verdict": "MARGINAL"
167	        },
168	        "interaction": {
169	          "F": 0.31,
170	          "p": 0.582,
171	          "eta_sq": 0.006,
172	          "verdict": "NOT_SIGNIFICANT"
173	        }
174	      },
175	      "n_batches_per_cell": 12,
176	      "total_n": 48,
177	      "simple_effects": {
178	        "bcs_at_low_count": {
179	          "delta_f1": -0.036,
180	          "p": 0.22
181	        },
182	        "bcs_at_high_count": {
183	          "delta_f1": -0.043,
184	          "p": 0.18
185	        }
186	      }
187	    },
188	    "tables": [
189	      "Table: 2×2 Cell Means (F1, text_match)\n|                | Low BCS     | High BCS    | BCS Effect |\n|----------------|-------------|-------------|------------|\n| Low Count (6)  | 0.348       | 0.312       | Δ=-0.036   |\n| High Count (22)| 0.298       | 0.255       | Δ=-0.043   |\n| Count Effect   | Δ=-0.050   | Δ=-0.057   |            |\n",
190	      "Table: Two-Way ANOVA Results\n| Source       | F     | p     | η²    | Verdict     |\n|-------------|-------|-------|-------|-------------|\n| Count        | 7.82  | 0.008 | 0.14  | Significant |\n| BCS          | 2.93  | 0.094 | 0.06  | Marginal    |\n| Count × BCS  | 0.31  | 0.582 | 0.006 | NS          |\n"
191	    ],
192	    "figures": [],
193	    "analysis": "交互效应不显著是 worst tier 对 Claim 2（multi-channel degradation）的重大打击。 论文无法用 formal factorial design 证明两通道正交。只能退而求其次，基于 error taxonomy（exp-007）做 descriptive argument：count 降低 recall（omission）， confusability 增加 type confusion（substitution），两类错误机制不同→暗示正交。 但这种 descriptive 论证说服力远不如 significant interaction test。在 worst tier 叙事中，2×2 结果最多写一段文字报告 \"no significant interaction was detected, consistent with additive but not multiplicative independence\"。\n\n\n2×2 设计的统计功效受限：每个 cell 约 12 个 batch，总 n=48。在这个样本量下， 检测交互效应需要 η²≥0.10 的大效应量。实际中，count 的主效应最强（η²=0.14）， 因为 count 直接影响 prompt 长度和 attention 分配，信号最清晰。BCS 主效应仅为 marginal（p=0.094），因为 batch-level BCS 与 F1 的关系本就受到 type frequency distribution 等 confound 的干扰——exp-002 已经表明 batch-level 信号远弱于 pairwise-level。交互效应完全不显著（p=0.582），说明 count 和 confusability 的 联合效应是（弱）加性的，不存在 multiplicative synergy。这在 worst tier 中意味 着论文只能声称 \"两个通道可能独立\" 但无法用 formal interaction test 支撑。\n"
194	  },
195	  {
196	    "name": "Systematic Error Taxonomy by BCS Bins",
197	    "description": "对 Few-NERD exp-002 数据做系统 FP 分类（type_substitution / boundary_error / false_negative / hallucination），按 BCS bin 分析差异。机械层面支撑 multi-channel 模型。\n",
198	    "results": {
199	      "error_distribution_overall": {
200	        "type_substitution_pct": 0.18,
201	        "boundary_error_pct": 0.12,
202	        "spurious_extraction_pct": 0.45,
203	        "missed_entity_pct": 0.25
204	      },
205	      "type_substitution_by_bcs": {
206	        "extreme_high_bcs_rate": 0.058,
207	        "extreme_low_bcs_rate": 0.012,
208	        "extreme_ratio": 4.8,
209	        "random_high_bcs_rate": 0.022,
210	        "random_low_bcs_rate": 0.015,
211	        "random_ratio": 1.5
212	      },
213	      "boundary_error_by_bcs": {
214	        "high_bcs_rate": 0.041,
215	        "low_bcs_rate": 0.038,
216	        "ratio": 1.08,
217	        "verdict": "NO_EFFECT"
218	      },
219	      "missed_entity_by_count": {
220	        "count_6_miss_rate": 0.28,
221	        "count_22_miss_rate": 0.42,
222	        "count_64_miss_rate": 0.55,
223	        "trend": "monotonically increasing with count"
224	      },
225	      "missed_entity_by_bcs": {
226	        "high_bcs_miss_rate": 0.4,
227	        "low_bcs_miss_rate": 0.38,
228	        "ratio": 1.05,
229	        "verdict": "NO_EFFECT"
230	      },
231	      "hallucination_rate": 0.03,
232	      "hallucination_by_bcs": {
233	        "verdict": "NO_EFFECT"
234	      }
235	    },
236	    "tables": [
237	      "Table: Error Distribution Overall\n| Error Type          | Proportion | Primary Driver |\n|---------------------|------------|----------------|\n| Spurious Extraction | 45%        | Prompt format  |\n| Missed Entity       | 25%        | Count (recall) |\n| Type Substitution   | 18%        | BCS (confuse)  |\n| Boundary Error      | 12%        | Span detection |\n",
238	      "Table: Type Substitution Rate by BCS Condition\n| Condition     | High BCS | Low BCS | Ratio |\n|---------------|----------|---------|-------|\n| Extreme Batch | 0.058    | 0.012   | 4.8x  |\n| Random Batch  | 0.022    | 0.015   | 1.5x  |\n",
239	      "Table: Missed Entity Rate by Count\n| Count | Miss Rate | Δ vs Count_6 |\n|-------|-----------|--------------|\n| 6     | 0.28      | —            |\n| 22    | 0.42      | +0.14        |\n| 64    | 0.55      | +0.27        |\n"
240	    ],
241	    "figures": [],
242	    "analysis": "Error taxonomy 部分支持 multi-channel 模型：(1) type substitution 受 BCS 影响 （extreme 4.8x），(2) missed entity 受 count 影响（monotonic）。但 worst tier 下两个弱点：(a) type substitution 只占总 error 的 18%，不是 dominant mode—— reviewer 会质疑 \"如果 confusability 只解释 18% 的 error，实际影响有多大？\"； (b) random batch ratio 仅 1.5x，远低于 extreme 的 4.8x——说明自然分布下效应 很小。论文只能做 descriptive analysis，不能做 formal causal claim。在 worst tier 叙事中，error taxonomy 作为 supporting evidence 放在 analysis section， 不作为独立 finding。\n\n\nError taxonomy 的分类本身是 noisy 的——boundary error vs type substitution 的 区分依赖 text_match 容差设定。在 worst tier 下：(1) type substitution 在 extreme high-BCS batch 中确实更多（4.8x ratio），但 extreme batches 是刻意构造的极端 条件，random batches 中 ratio 仅 1.5x，实际场景中效应有限；(2) boundary error 不受 BCS 影响（ratio≈1.0），符合预期——boundary detection 是 span 层面的任务， 与 type confusability 无关；(3) missed entity（false negative）主要由 count 驱动（count_6 miss 28% vs count_64 miss 55%），不受 BCS 影响——支持 count→recall 通道；(4) 但整体 error 中 spurious extraction 占 45%，远超 type substitution 的 18%——这意味着 LLM 的主要问题是 \"提取不该提取的 span\" 而非 \"type 标错\"， confusability 只解释了一小部分 error。worst tier 的核心问题是：type confusion 不是 dominant error mode，因此 confusability 的实际影响被其他 error 源稀释。\n"
243	  },
244	  {
245	    "name": "LLaMA-3.3-70B Multi-Model Validation",
246	    "description": "用 LLaMA-3.3-70B-Instruct 复制 exp-002 protocol（Few-NERD, 25 random + extreme batches, count=6/12, pairwise + per-type 分析）。检验 confusability 效应的跨模型 泛化性。\n",
247	    "results": {
248	      "baseline_f1_count64": 0.378,
249	      "baseline_vs_qwen3": "Δ=-3.6pp (Qwen3=0.414)",
250	      "pairwise_qwen3_embed": {
251	        "pearson_r": 0.042,
252	        "pearson_p": 0.068,
253	        "n_pairs": 1953,
254	        "verdict": "NOT_SIGNIFICANT"
255	      },
256	      "pairwise_qwen3_embed_nonzero": {
257	        "spearman_rho": 0.078,
258	        "p": 0.12,
259	        "verdict": "NOT_SIGNIFICANT"
260	      },
261	      "per_type_bcs_f1": {
262	        "spearman_rho": -0.082,
263	        "p": 0.538,
264	        "n_types": 58,
265	        "partial_r_ctrl_logfreq": -0.055,
266	        "partial_p": 0.684,
267	        "verdict": "NOT_SIGNIFICANT"
268	      },
269	      "batch_f1_vs_bcs": {
270	        "count_6": {
271	          "r": 0.108,
272	          "p": 0.42
273	        },
274	        "count_12": {
275	          "r": 0.185,
276	          "p": 0.21
277	        },
278	        "partial_pooled": {
279	          "r": 0.138,
280	          "p": 0.16
281	        }
282	      },
283	      "confusion_rate_extreme": {
284	        "count_6_high": 0.025,
285	        "count_6_low": 0.01,
286	        "ratio_6": 2.5,
287	        "count_12_high": 0.032,
288	        "count_12_low": 0.015,
289	        "ratio_12": 2.1
290	      },
291	      "confusion_rate_random": {
292	        "count_6_ratio": 1.2,
293	        "count_12_ratio": 1.15
294	      },
295	      "cross_model_summary": {
296	        "qwen3_pairwise_r": 0.156,
297	        "llama_pairwise_r": 0.042,
298	        "qwen3_extreme_ratio": "10-28x",
299	        "llama_extreme_ratio": "2.1-2.5x",
300	        "qwen3_per_type_rho": -0.293,
301	        "llama_per_type_rho": -0.082
302	      }
303	    },
304	    "tables": [
305	      "Table: Cross-Model Comparison (Few-NERD)\n| Metric                    | Qwen3-32B    | LLaMA-3.3-70B | Ratio    |\n|---------------------------|-------------|---------------|----------|\n| Baseline F1 (count_64)    | 0.414       | 0.378         | 0.91x    |\n| Pairwise r (Qwen3 embed)  | 0.156***    | 0.042 (ns)    | 0.27x    |\n| Per-type ρ                | -0.293*     | -0.082 (ns)   | 0.28x    |\n| Extreme confusion ratio   | 10-28x      | 2.1-2.5x      | 0.10x    |\n| Random confusion ratio    | 1.7-2.4x    | 1.15-1.2x     | 0.50x    |\n",
306	      "Table: LLaMA Pairwise & Per-Type Statistics\n| Analysis        | Statistic | Value  | p     | Verdict |\n|-----------------|-----------|--------|-------|---------|\n| Pairwise        | Pearson r | 0.042  | 0.068 | NS      |\n| Pairwise NZ     | Spearman  | 0.078  | 0.120 | NS      |\n| Per-type        | Spearman  | -0.082 | 0.538 | NS      |\n| Per-type partial| Partial r | -0.055 | 0.684 | NS      |\n"
307	    ],
308	    "figures": [],
309	    "analysis": "LLaMA 结果是 worst tier 中最关键的 negative result。cross_model_significant = 1 （仅 Qwen3），这意味着 confusability 效应可能是 Qwen3 特有的，而非 LLM IE 的 普遍现象。论文必须显著降级 Claim 1 的 generalizability：从 \"confusability independently predicts degradation in training-free LLM IE\" 改为 \"confusability sensitivity varies substantially across model families, with Qwen3 showing strong effects (r=0.156) and LLaMA showing weak/null effects (r=0.042)\"。在 worst tier 叙事中，这可 reframe 为解释力：\"prior conflicting findings about schema complexity may be partly explained by model-dependent confusability sensitivity\"——将缺陷转为贡献，但 reviewer 是否买账取决于写作。\n\n\nLLaMA-3.3-70B 与 Qwen3-32B 在 confusability 敏感度上存在根本差异，原因可能是： (1) 模型规模差异——70B vs 32B，更大的模型有更大的 attention capacity，能更好地 处理 confusable types 的共现，因此 confusability 的 degradation 效应被缓解； (2) instruction tuning 差异——LLaMA-3.3 的 RLHF 训练可能更强调 precision 和 faithfulness，模型在不确定时倾向不输出（而非猜测相似 type），导致 type confusion error 本就少，confusability 信号弱；(3) internal representation 差异——LLaMA 的 embedding 空间对 Few-NERD types 的组织方式可能与 Qwen3 不同，Qwen3 embedding 中的 semantic proximity 模式不能直接迁移为 LLaMA 的 confusion 模式。\npairwise r=0.042 (p=0.068) 在 α=0.05 下不显著但接近边界——这是最棘手的 结果：不能说完全无信号（p=0.068），但也不能声称显著。在 worst tier 叙事中， 这被 reframe 为 \"confusability effects are model-dependent, with effect size varying by 4x across model families (r=0.156 Qwen3 vs r=0.042 LLaMA)\"。confusion rate ratio 也大幅下降（2.5x vs Qwen3 的 27.5x），进一步说明 LLaMA 对 type confusion 更鲁棒。\n"
310	  },
311	  {
312	    "name": "SDGD-zero on Few-NERD",
313	    "description": "Few-NERD 上的 SDGD-zero：Qwen3 embedding SCS + graph coloring (τ adaptive, k=1.0) 生成 confusability-minimizing batches，与 single-pass 对比。\n",
314	    "results": {
315	      "graph_stats": {
316	        "threshold_tau": 0.847,
317	        "n_edges": 142,
318	        "edge_density": 0.066,
319	        "chromatic_number": 8,
320	        "avg_batch_size": 8.25,
321	        "max_batch_size": 12,
322	        "min_batch_size": 4,
323	        "max_intra_batch_bcs": 0.842
324	      },
325	      "sdgd_zero": {
326	        "f1": 0.367,
327	        "precision": 0.318,
328	        "recall": 0.434,
329	        "pred_gold_ratio": 1.36
330	      },
331	      "single_pass": {
332	        "f1": 0.414,
333	        "precision": 0.648,
334	        "recall": 0.304
335	      },
336	      "delta_f1_vs_single_pass": -4.7,
337	      "delta_precision": -33.0,
338	      "delta_recall": 13.0,
339	      "per_batch_f1_range": [
340	        0.28,
341	        0.42
342	      ],
343	      "per_batch_recall_range": [
344	        0.35,
345	        0.52
346	      ],
347	      "per_batch_precision_range": [
348	        0.22,
349	        0.38
350	      ],
351	      "merge_stats": {
352	        "total_predictions": 4850,
353	        "unique_predictions_after_dedup": 4120,
354	        "cross_batch_span_overlap": 0.08,
355	        "predictions_per_sample_avg": 8.2,
356	        "gold_per_sample_avg": 5.9
357	      },
358	      "api_calls": "8x single-pass (8000 vs 1000 for 1000 samples)",
359	      "wall_clock_multiplier": 6.5
360	    },
361	    "tables": [
362	      "Table: SDGD-zero vs Single-Pass (Few-NERD, 66 types)\n| Method      | F1    | Precision | Recall | Pred/Gold | API Calls |\n|-------------|-------|-----------|--------|-----------|-----------|\n| Single-pass | 0.414 | 0.648     | 0.304  | 0.47      | 1x        |\n| SDGD-zero   | 0.367 | 0.318     | 0.434  | 1.36      | 8x        |\n| Δ           | -4.7pp| -33.0pp   | +13.0pp| +0.89     | +7x       |\n",
363	      "Table: SDGD-zero Per-Batch Breakdown (top 4 batches)\n| Batch | Types | Avg BCS | F1    | Recall | Precision |\n|-------|-------|---------|-------|--------|-----------|\n| 0     | 12    | 0.812   | 0.42  | 0.48   | 0.38      |\n| 1     | 10    | 0.795   | 0.38  | 0.45   | 0.33      |\n| 2     | 9     | 0.780   | 0.35  | 0.42   | 0.30      |\n| 3     | 8     | 0.763   | 0.32  | 0.40   | 0.27      |\n"
364	    ],
365	    "figures": [],
366	    "analysis": "SDGD-zero 的失败是 worst tier 的核心 negative result。直接否定 Claim 3。 failure mode 清晰且可解释：separating confusable types 剥夺了模型的 comparative disambiguation 能力。这是一个 informative negative result——它揭示了 LLM IE 中 type co-presence 的 dual role：(1) 增加 confusability（hypothesis 的前提）， (2) 提供 disambiguation context（SDGD 未预见的副作用）。在 worst tier 叙事中， 这个发现可以作为论文的一个 insight：\"confusability is a two-edged sword — the same type co-presence that causes confusion also enables disambiguation\"， 解释为什么简单的 separation strategy 不 work。但这最多放在 Discussion section， 不能作为 core contribution。\n\n\nSDGD-zero 失败的核心机制是 \"disambiguation context loss\"。当 confusable types 被分到不同 batch 时，每个 batch 中的模型只看到 pair 的一端。例如 person-other 在 batch A，person-politician 在 batch B。处理含政治人物的句子时：\n- Batch A（有 person-other，无 person-politician）：模型将政治人物标为\n  person-other（因为这是最接近的可用 type）→ FP for person-other\n- Batch B（有 person-politician，无 person-other）：模型将普通人标为\n  person-politician（同理）→ FP for person-politician\n\nmerge 后，同一实体可能被两个 batch 分别标为不同 type（cross-batch span overlap 8%），评估时只有一个是 TP，另一个是 FP。更严重的是，每个 batch 只有 ~8 types， 模型倾向过度提取（pred/gold=1.36 vs single-pass 的 0.47），precision 从 0.648 暴跌到 0.318。recall 确实从 0.304 提升到 0.434（smaller batch → 更多 attention 给每个 type），但 precision 损失远大于 recall 增益。\nF1 = 0.367 比 single-pass 的 0.414 低 4.7pp。SDGD 的前提假设（separating confusable types reduces confusion）是错误的——对 LLM 来说，看到 confusable types 的完整集合反而帮助 disambiguation。\n"
367	  },
368	  {
369	    "name": "SDGD-zero on MAVEN",
370	    "description": "MAVEN（168 event types）上的 SDGD-zero。用 adaptive threshold (k=1.0) 生成 confusability-minimizing batches。跨任务（NER→ED）验证 SDGD。\n",
371	    "results": {
372	      "graph_stats": {
373	        "embedding": "qwen3",
374	        "scs_mean": 0.216,
375	        "scs_std": 0.103,
376	        "threshold_tau": 0.319,
377	        "n_edges": 1850,
378	        "edge_density": 0.132,
379	        "chromatic_number": 15,
380	        "avg_batch_size": 11.2,
381	        "min_batch_size": 5,
382	        "max_batch_size": 18
383	      },
384	      "sdgd_zero": {
385	        "relaxed_f1": 0.168,
386	        "exact_f1": 0.012,
387	        "relaxed_recall": 0.13,
388	        "relaxed_precision": 0.238
389	      },
390	      "single_pass": {
391	        "relaxed_f1": 0.241,
392	        "exact_f1": 0.018
393	      },
394	      "delta_relaxed_f1": -7.3,
395	      "api_calls": "15x single-pass",
396	      "wall_clock_multiplier": 12.8
397	    },
398	    "tables": [
399	      "Table: SDGD-zero vs Single-Pass (MAVEN, 168 types)\n| Method      | Relaxed F1 | Exact F1 | API Calls | Wall-Clock |\n|-------------|-----------|----------|-----------|------------|\n| Single-pass | 0.241     | 0.018    | 1x        | 1x         |\n| SDGD-zero   | 0.168     | 0.012    | 15x       | 12.8x      |\n| Δ           | -7.3pp    | -0.6pp   | +14x      | +11.8x     |\n"
400	    ],
401	    "figures": [],
402	    "analysis": "MAVEN SDGD-zero 是最差的结果之一。15x API cost 换来 -7.3pp 性能下降。 与 Few-NERD 的 SDGD 失败共同构成 Claim 3 的致命反证：SDGD 在两个任务上 都差于 single-pass，且效果 consistent（方向一致、机制相同）。在 worst tier 叙事中，SDGD 相关实验（exp-008, 009, 010, 011, 013, 014）全部降级为 appendix 中的 negative result case study，正文仅用 1-2 段文字总结 \"we also explored confusability-minimizing decomposition, which failed because...\"。\n\n\nMAVEN 上 SDGD-zero 失败更严重（Δ=-7.3pp vs Few-NERD 的 -4.7pp），原因： (1) MAVEN count curve 是上升的——更多 types 帮助模型理解 event ontology， decomposition 直接损害这个优势；(2) adaptive τ=0.319（因 MAVEN Qwen3 SCS 分布集中在低值区间），graph 中 edge density=13.2%，coloring 产生 15 个 batch， 每个约 11 types——这比 single-pass 的 168 types 少了 93%的 type 上下文； (3) 15 个 batch 意味着 15x API 调用，wall-clock 12.8x 但性能反而更差—— cost-quality 全面恶化；(4) MAVEN event trigger 是 verb/nominalization，多个 event type 共享同一 trigger word（如 \"attack\" 可以是 Attack 也可以是 Conflict）， 模型需要看到完整 event taxonomy 才能正确 assign type。\n"
403	  },
404	  {
405	    "name": "SDGD-cal on Few-NERD",
406	    "description": "Few-NERD 上的 SDGD-cal：用 5-10 calibration examples 构建 empirical confusion matrix，替代 embedding SCS。与 SDGD-zero 和 single-pass 对比。\n",
407	    "results": {
408	      "calibration_stats": {
409	        "n_calibration_samples": 8,
410	        "calibration_api_calls": 8,
411	        "empirical_confusion_pairs_nonzero": 85,
412	        "spearman_vs_embedding_scs": 0.125,
413	        "p_vs_embedding_scs": 0.031
414	      },
415	      "graph_stats": {
416	        "threshold_tau": "adaptive on empirical confusion",
417	        "n_edges": 62,
418	        "chromatic_number": 7,
419	        "avg_batch_size": 9.4
420	      },
421	      "sdgd_cal": {
422	        "f1": 0.381,
423	        "precision": 0.342,
424	        "recall": 0.43,
425	        "pred_gold_ratio": 1.26
426	      },
427	      "comparison": {
428	        "vs_single_pass_delta": -3.3,
429	        "vs_sdgd_zero_delta": 1.4,
430	        "vs_random_delta": 0.7,
431	        "vs_random_p": 0.58
432	      },
433	      "single_pass_f1": 0.414,
434	      "sdgd_zero_f1": 0.367,
435	      "random_f1": 0.374
436	    },
437	    "tables": [
438	      "Table: SDGD-cal vs Baselines (Few-NERD)\n| Method      | F1    | Δ vs SP | Precision | Recall | API Overhead   |\n|-------------|-------|---------|-----------|--------|----------------|\n| Single-pass | 0.414 | —       | 0.648     | 0.304  | 1x             |\n| Random (k=8)| 0.374 | -4.0    | 0.335     | 0.425  | 8x             |\n| SDGD-zero   | 0.367 | -4.7    | 0.318     | 0.434  | 8x             |\n| SDGD-cal    | 0.381 | -3.3    | 0.342     | 0.430  | 7x + 8 calib   |\n"
439	    ],
440	    "figures": [],
441	    "analysis": "SDGD-cal 是 SDGD 方法线的 \"best effort\"——用 ground truth confusion 替代 proxy。 即使如此仍低于 single-pass 3.3pp。这最终否定了 confusability-minimizing decomposition 的整体方法路线：问题不在 confusion matrix 的质量，而在于 decomposition 本身损害了 LLM 的 disambiguation context。在 worst tier 叙事中， SDGD-cal 的 marginal improvement over SDGD-zero 可作为 exp-015（SCS validation） 的间接证据：embedding proxy 与 empirical confusion 仅弱相关（ρ=0.125），但这 不是失败的主因——即使 perfect confusion matrix 也不能拯救 decomposition strategy。\n\n\nSDGD-cal 比 SDGD-zero 好（+1.4pp），因为 empirical confusion matrix 比 embedding SCS 更准确地反映实际 model confusion：(1) 非零 confusion pair 只有 85 对（vs embedding SCS 的 142 条 edge），graph 更稀疏 → 7 个 batch（vs 8 个），每个 batch 更大 → 更多 type 上下文；(2) calibration 捕捉到一些 embedding SCS 预测不 到的 confusion pattern（如语义不近但 surface form 相似的 type pair）。但 SDGD-cal 仍低于 single-pass 3.3pp，因为 decomposition 的核心问题（disambiguation context loss）不因 confusion matrix 质量改善而消失。与 random batching 的差异仅 +0.7pp (p=0.58)，不显著——confusability-aware grouping 即使用了 empirical data 也没有 显著优势。calibration 的额外 cost（8 次 API 调用）换来的 improvement 微乎其微。\n"
442	  },
443	  {
444	    "name": "SDGD-cal on MAVEN",
445	    "description": "MAVEN（168 types）上的 SDGD-cal：empirical confusion matrix + graph coloring。 Full comparison table。\n",
446	    "results": {
447	      "calibration_stats": {
448	        "n_calibration_samples": 10,
449	        "empirical_confusion_pairs_nonzero": 210
450	      },
451	      "graph_stats": {
452	        "chromatic_number": 12,
453	        "avg_batch_size": 14.0
454	      },
455	      "sdgd_cal": {
456	        "relaxed_f1": 0.188,
457	        "exact_f1": 0.014
458	      },
459	      "comparison": {
460	        "vs_single_pass_delta": -5.3,
461	        "vs_sdgd_zero_delta": 2.0,
462	        "vs_random_delta": 0.8,
463	        "vs_random_p": 0.62
464	      },
465	      "single_pass_relaxed_f1": 0.241,
466	      "sdgd_zero_relaxed_f1": 0.168,
467	      "random_relaxed_f1": 0.18
468	    },
469	    "tables": [
470	      "Table: Full Comparison (MAVEN, 168 types, relaxed matching)\n| Method      | Relaxed F1 | Δ vs SP | API Calls      |\n|-------------|-----------|---------|----------------|\n| Single-pass | 0.241     | —       | 1x             |\n| Random (k=12)| 0.180    | -6.1    | 12x            |\n| SDGD-zero   | 0.168     | -7.3    | 15x            |\n| SDGD-cal    | 0.188     | -5.3    | 12x + 10 calib |\n"
471	    ],
472	    "figures": [],
473	    "analysis": "MAVEN SDGD-cal 确认 decomposition 在 event detection 上全面失败。所有方法 均差于 single-pass，且 MAVEN 的差距（5-7pp）比 Few-NERD（3-5pp）更大。 这强化了 worst tier 的核心结论：decomposition 不是通用 solution，type co-presence 在很多场景中是 feature 而非 bug。\n\n\n与 Few-NERD 相同模式：SDGD-cal 好于 SDGD-zero（+2.0pp）但仍远差于 single-pass （-5.3pp）。MAVEN 的 empirical confusion matrix 更密（210 nonzero pairs vs Few-NERD 的 85），因为 168 types 中很多 event type 确实会互相 confuse（尤其是 同一 FrameNet frame 下的 sibling types）。但 calibration 帮助有限——核心问题 仍然是 MAVEN 的性能与 type count 正相关，decomposition 损害性能。\n"
474	  },
475	  {
476	    "name": "Random Batching Ablation",
477	    "description": "与 SDGD-zero 相同 batch 数量 k，随机分组。隔离 confusability-aware grouping 的价值（排除 batch count reduction 的贡献）。\n",
478	    "results": {
479	      "fewnerd": {
480	        "random_f1": 0.374,
481	        "sdgd_zero_f1": 0.367,
482	        "delta_sdgd_vs_random": -0.7,
483	        "paired_t_p": 0.68,
484	        "n_random_seeds": 10,
485	        "random_f1_std": 0.018,
486	        "random_f1_range": [
487	          0.348,
488	          0.402
489	        ],
490	        "single_pass_f1": 0.414
491	      },
492	      "maven": {
493	        "random_relaxed_f1": 0.18,
494	        "sdgd_zero_relaxed_f1": 0.168,
495	        "delta_sdgd_vs_random": -1.2,
496	        "paired_t_p": 0.42,
497	        "n_random_seeds": 5
498	      },
499	      "interpretation": {
500	        "sdgd_vs_random_significant": false,
501	        "confusability_aware_grouping_benefit": null
502	      }
503	    },
504	    "tables": [
505	      "Table: Random vs SDGD-zero (Few-NERD, k=8)\n| Method     | Mean F1 | Std   | Range         | vs Single-Pass |\n|------------|---------|-------|---------------|----------------|\n| Random×10  | 0.374   | 0.018 | [0.348,0.402] | -4.0pp         |\n| SDGD-zero  | 0.367   | —     | —             | -4.7pp         |\n| Δ (SDGD-Random) | -0.7pp | — | —           | p=0.68 (NS)    |\n",
506	      "Table: Random vs SDGD-zero (MAVEN, k=15/12)\n| Method     | Relaxed F1 | vs Single-Pass |\n|------------|-----------|----------------|\n| Random×5   | 0.180     | -6.1pp         |\n| SDGD-zero  | 0.168     | -7.3pp         |\n| Δ          | -1.2pp    | p=0.42 (NS)    |\n"
507	    ],
508	    "figures": [],
509	    "analysis": "Random batching ablation 是 Claim 3 的 definitive kill shot。SDGD 不显著优于 random→confusability-aware grouping 无价值。combined with SDGD < single-pass→ decomposition 本身有害。Claim 3 完全不成立。在 worst tier 叙事中，这个实验 的 negative result 本身有教育意义：it demonstrates that the intuitive principle \"separate confusable types\" is wrong for LLM IE，因为 LLMs 使用 type co-presence 做 comparative reasoning。\n\n\nRandom batching 在 10 个 random seeds 上平均 F1=0.374（std=0.018），而 SDGD-zero F1=0.367。SDGD 比 random 差 0.7pp（p=0.68），差异不显著。实际上 SDGD 可能略 差于 random，因为 SDGD 刻意将 confusable types 分开——这意味着每个 batch 内的 types 都是 semantically distant 的，模型缺乏同一 semantic cluster 的 types 作为 disambiguation anchor。Random batching 偶尔会把 confusable types 放在一起 （概率约 1/k），这些 batch 的 disambiguation 更好，平均下来 random 反而略优。\n在 MAVEN 上同样：random F1=0.180 vs SDGD F1=0.168（Δ=-1.2pp, p=0.42）。 SDGD 的 confusability-aware grouping 不仅无益，可能有害。\n"
510	  },
511	  {
512	    "name": "Per-Type Splitting (UniNER-style) Ablation",
513	    "description": "1 type per batch（k=66/168）。Decomposition 的上界。揭示 latency-quality tradeoff。\n",
514	    "results": {
515	      "fewnerd": {
516	        "per_type_f1": 0.33,
517	        "per_type_precision": 0.225,
518	        "per_type_recall": 0.62,
519	        "api_calls": "66x single-pass",
520	        "wall_clock_multiplier": 48.0
521	      },
522	      "maven": {
523	        "per_type_relaxed_f1": 0.108,
524	        "api_calls": "168x single-pass",
525	        "wall_clock_multiplier": 135.0
526	      },
527	      "comparison_fewnerd": {
528	        "single_pass": 0.414,
529	        "sdgd_zero": 0.367,
530	        "random": 0.374,
531	        "per_type": 0.33
532	      },
533	      "ordering": "single-pass > random ≈ SDGD-zero > per-type"
534	    },
535	    "tables": [
536	      "Table: Full Method Comparison (Few-NERD)\n| Method      | F1    | Precision | Recall | API Calls | Wall-Clock |\n|-------------|-------|-----------|--------|-----------|------------|\n| Single-pass | 0.414 | 0.648     | 0.304  | 1x        | 1x         |\n| SDGD-cal    | 0.381 | 0.342     | 0.430  | 7x        | 5.5x       |\n| Random (k=8)| 0.374 | 0.335     | 0.425  | 8x        | 6.5x       |\n| SDGD-zero   | 0.367 | 0.318     | 0.434  | 8x        | 6.5x       |\n| Per-type    | 0.330 | 0.225     | 0.620  | 66x       | 48x        |\n",
537	      "Table: Full Method Comparison (MAVEN, relaxed)\n| Method      | Relaxed F1 | API Calls | Wall-Clock |\n|-------------|-----------|-----------|------------|\n| Single-pass | 0.241     | 1x        | 1x         |\n| SDGD-cal    | 0.188     | 12x       | 10x        |\n| Random      | 0.180     | 12x       | 10x        |\n| SDGD-zero   | 0.168     | 15x       | 12.8x      |\n| Per-type    | 0.108     | 168x      | 135x       |\n"
538	    ],
539	    "figures": [],
540	    "analysis": "Per-type ablation 完成了 decomposition failure 的完整图景。方法排序 single-pass > random ≈ SDGD > per-type 说明：(1) decomposition granularity 与 F1 反相关；(2) type co-presence 是 net positive（disambiguation > confusion）； (3) SDGD 的 confusability-aware grouping 不提供额外价值（≈ random）。 在 worst tier 叙事中，这个结果可 reframe 为 empirical finding：\"LLM IE benefits from full schema visibility; type co-presence enables comparative reasoning that outweighs confusability-induced errors\"——这本身是一个有价值 的 insight，但不是 method contribution。\n\n\nPer-type splitting 是 decomposition 的极端形式：每个 batch 只有 1 个 type。 这完全消除 type confusion（BCS=0），但也完全消除 disambiguation context。\nFew-NERD 结果（F1=0.330）几乎等于 exp003a count_1 的 F1=0.323——符合预期， 因为 per-type extraction 本质就是 count=1。precision 极低（0.225）因为模型 只知道一个 type，会把任何像样的 span 都标为该 type（massive over-extraction）。 recall 最高（0.620）因为模型 aggressively 搜索这个 type 的所有 instance。\nMAVEN 更惨（relaxed F1=0.108），因为 MAVEN 的 count_1 relaxed_F1 就只有 0.098。 168x API 调用使 wall-clock time 完全不可接受。\n排序 single-pass > random ≈ SDGD > per-type 证明：decomposition granularity 与性能成反比。batch 越大越好（更多 type context），单pass 最优。\n"
541	  },
542	  {
543	    "name": "Embedding SCS vs Empirical Confusion Validation",
544	    "description": "计算 embedding SCS（Qwen3 / MiniLM）与 empirical confusion matrix 之间的 rank correlation。验证 embedding proxy 对实际 model confusion 的预测力。\n",
545	    "results": {
546	      "qwen3_scs_vs_empirical": {
547	        "spearman_rho": 0.125,
548	        "p": 0.031,
549	        "kendall_tau": 0.092,
550	        "p_kendall": 0.044,
551	        "n_pairs_with_confusion": 85
552	      },
553	      "minilm_scs_vs_empirical": {
554	        "spearman_rho": 0.098,
555	        "p": 0.082,
556	        "kendall_tau": 0.071,
557	        "p_kendall": 0.115,
558	        "n_pairs_with_confusion": 85
559	      },
560	      "top_confused_pair_scs_rank": {
561	        "person_other_politician": {
562	          "scs_rank": 3,
563	          "confusion_rank": 1
564	        },
565	        "building_other_library": {
566	          "scs_rank": 45,
567	          "confusion_rank": 8,
568	          "comment": "high confusion, low SCS — embedding 未捕捉的 confusion pattern"
569	        }
570	      },
571	      "scs_false_positive_rate": 0.42,
572	      "scs_false_negative_rate": 0.35
573	    },
574	    "tables": [
575	      "Table: SCS vs Empirical Confusion Correlation\n| Embedding | Spearman ρ | p     | Kendall τ | p     |\n|-----------|-----------|-------|-----------|-------|\n| Qwen3     | 0.125     | 0.031 | 0.092     | 0.044 |\n| MiniLM    | 0.098     | 0.082 | 0.071     | 0.115 |\n",
576	      "Table: SCS Proxy Error Analysis\n| Metric              | Qwen3 | MiniLM |\n|---------------------|-------|--------|\n| False Positive Rate | 0.42  | 0.48   |\n| False Negative Rate | 0.35  | 0.40   |\n| Top-1 Match         | Yes   | No     |\n"
577	    ],
578	    "figures": [],
579	    "analysis": "SCS validation 结果解释了 SDGD 失败的一个次要原因（proxy 质量差），但不是主因 （主因是 decomposition 本身有害）。ρ=0.125 说明 embedding SCS 只能解释 ~1.6% 的 confusion variance——作为 graph 构建的基础远远不够。即使用 empirical confusion (exp-010 SDGD-cal) 也只比 random 好 0.7pp（不显著），所以 proxy 质量不是瓶颈。 在 worst tier 叙事中，SCS validation 作为 methodological finding 报告： \"embedding-based confusability proxies have limited predictive power for actual model confusion patterns, suggesting that confusability is mediated by factors beyond semantic similarity\"——这对未来工作有指导价值。\n\n\nEmbedding SCS 与 empirical confusion 仅弱相关（ρ=0.125），原因：(1) embedding similarity 反映 semantic proximity，但 model confusion 还受 surface form similarity、type definition wording、in-context position 等因素影响——这些因素 与 embedding space 正交；(2) SCS 是对称的（sim(A,B)=sim(B,A)），但实际 confusion 是非对称的（person-other → person-politician 的概率可能远高于反向）；(3) 42% 的 false positive rate 意味着 SCS 预测为 confusable 的 type pair 中近一半实际 不被 confuse——这些 false alarm 导致 SDGD-zero 过度分离 types，graph 变密， batch 数量过多。\nMiniLM SCS 更差（ρ=0.098, p=0.082），因为 MiniLM 是 general-purpose sentence embedding，不 align 到 Qwen3 的 internal representation。这解释了为什么 extraction model alignment 对 per-type signal 很重要（exp-002 中 Qwen3 per-type ρ=-0.293 vs MiniLM ρ≈0）。\n"
580	  },
581	  {
582	    "name": "Cross-Experiment Summary (for paper narrative)",
583	    "description": "综合所有实验的 worst tier 结果，构建论文核心 tables 和 narrative。\n",
584	    "results": {
585	      "claim1_pairwise_matrix": {
586	        "qwen3_fewnerd": "r=0.156*** ✓",
587	        "qwen3_maven": "r=-0.009 (ns) ✗",
588	        "qwen3_fewrel": "pending",
589	        "minilm_fewnerd": "not tested",
590	        "minilm_maven": "r=0.115*** ✓",
591	        "minilm_fewrel": "Δ=21-50pp ✓ (pilot)",
592	        "llama_fewnerd": "r=0.042 (ns) ✗",
593	        "significant_cells": 3,
594	        "total_cells": 7,
595	        "verdict": "partial — 3/7 significant, no single embedding/model universally works"
596	      },
597	      "claim2_evidence": {
598	        "count_recall_monotonic": true,
599	        "bcs_type_substitution_ratio_extreme": "4.8x",
600	        "bcs_type_substitution_ratio_random": "1.5x",
601	        "interaction_significant": false,
602	        "error_taxonomy_dominant_mode": "spurious extraction (45%), not type confusion (18%)",
603	        "verdict": "directional — channels exist but confusability channel is weak relative to other error sources"
604	      },
605	      "claim3_evidence": {
606	        "sdgd_zero_fewnerd": "F1=0.367, Δ=-4.7pp vs SP",
607	        "sdgd_zero_maven": "relF1=0.168, Δ=-7.3pp vs SP",
608	        "sdgd_cal_fewnerd": "F1=0.381, Δ=-3.3pp vs SP",
609	        "sdgd_cal_maven": "relF1=0.188, Δ=-5.3pp vs SP",
610	        "sdgd_vs_random_significant": false,
611	        "per_type_worst": true,
612	        "verdict": "FAILED — all decomposition methods inferior to single-pass"
613	      },
614	      "recommended_paper_structure": [
615	        "1. Introduction: 'What makes schemas complex for LLMs?'",
616	        "2. Related Work: decomposition approaches + empirical studies",
617	        "3. Experimental Setup: 3 tasks, 2 models, 2 embeddings",
618	        "4. Finding 1: Pairwise confusability predicts type confusion (model-dependent)",
619	        "5. Finding 2: Count and confusability act through distinguishable channels",
620	        "6. Finding 3: Per-type aggregation introduces centrality confound",
621	        "7. Finding 4: Confusability-minimizing decomposition fails (negative result)",
622	        "8. Discussion: implications for future work",
623	        "9. Conclusion"
624	      ],
625	      "recommended_venue": "EMNLP 2026 Findings (realistic), Main (stretch)"
626	    },
627	    "tables": [
628	      "Table: Pairwise SCS-Confusion Signal (Cross-Task × Cross-Model × Cross-Embedding)\n| Model  | Embedding | Few-NERD (NER) | MAVEN (ED) | FewRel (RE) |\n|--------|-----------|----------------|------------|-------------|\n| Qwen3  | Qwen3     | r=0.156***     | r=-0.009   | —           |\n| Qwen3  | MiniLM    | —              | r=0.115*** | Δ=21-50pp*  |\n| LLaMA  | Qwen3     | r=0.042        | —          | —           |\n*** p<0.001, * pilot only\n",
629	      "Table: SDGD Full Comparison (worst tier)\n| Method       | Few-NERD F1 | Δ vs SP | MAVEN relF1 | Δ vs SP |\n|-------------|-------------|---------|-------------|---------|\n| Single-pass  | 0.414       | —       | 0.241       | —       |\n| SDGD-cal     | 0.381       | -3.3    | 0.188       | -5.3    |\n| Random (=k)  | 0.374       | -4.0    | 0.180       | -6.1    |\n| SDGD-zero    | 0.367       | -4.7    | 0.168       | -7.3    |\n| Per-type     | 0.330       | -8.4    | 0.108       | -13.3   |\n"
630	    ],
631	    "figures": [],
632	    "analysis": "Worst tier 论文的核心卖点不是 positive findings 而是 systematic methodology 和 honest reporting。三个 takeaway：(1) confusability 信号存在但 model/embedding-dependent——未来工作不能假设 universal confusability measure； (2) per-type 聚合有 centrality confound——未来工作应使用 pairwise 分析； (3) confusability-minimizing decomposition 失败——LLM 需要 type co-presence 做 comparative reasoning，简单分离策略适得其反。这些 negative-but-informative results 加上 controlled experimental design 可以支撑一篇 Findings paper。\n\nWorst tier 总体图景：论文有两个可靠发现（pairwise confusability signal on Qwen3×FewNERD + MiniLM×MAVEN；centrality confound on MAVEN）和一系列 informative negative results（LLaMA 无信号、SDGD 全面失败、interaction 不显著）。叙事必须 从 \"we discover and exploit confusability\" 彻底转为 \"we systematically investigate schema complexity, finding that confusability effects are real but model-dependent, and that the intuitive decomposition strategy fails because LLMs need type co-presence for disambiguation\"。这种 \"honest empirical study with negative results\" 的论文在 EMNLP Findings 有先例（如 \"Do Prompt-Based Models Really Understand the Meaning of Their Prompts?\" ACL 2022），但需要极强的写作功力 和清晰的 takeaway。\n"
633	  }
634	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bc9200d-5bae-4048-af03-971f6aeb153c",
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "6ff45298-2c29-4061-b9e1-1be46157b77b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"MAVEN Full Confusability Study\",\n    \"description\": \"MAVEN Event Detection（168 event types, FrameNet hierarchy）的完整 confusability 研究：500-sample 重跑 count curve + within-count BCS 相关 + pairwise/per-type 双 embedding 分析 + confusion rate 分析。核心跨任务（NER→ED）验证。\\n\",\n    \"results\": {\n      \"count_curve_relaxed_f1\": {\n        \"count_1\": 0.098,\n        \"count_6\": 0.112,\n        \"count_12\": 0.155,\n        \"count_22\": 0.192,\n        \"count_44\": 0.238,\n        \"count_64\": 0.241,\n        \"count_100\": 0.243\n      },\n      \"count_curve_exact_f1\": {\n        \"count_1\": 0.008,\n        \"count_6\": 0.005,\n        \"count_12\": 0.011,\n        \"count_22\": 0.016,\n        \"count_44\": 0.021,\n        \"count_64\": 0.018\n      },\n      \"count_curve_recall_trend\": \"monotonically increasing 0.07→0.19 (opposite of Few-NERD)\",\n      \"count_curve_precision_trend\": \"roughly flat 0.15-0.40, noisy\",\n      \"within_count_bcs_f1\": {\n        \"count_6\": {\n          \"r\": 0.175,\n          \"p\": 0.185,\n          \"n\": 27,\n          \"direction\": \"positive\",\n          \"verdict\": \"FAIL\"\n        },\n        \"count_12\": {\n          \"r\": 0.124,\n          \"p\": 0.315,\n          \"n\": 27,\n          \"direction\": \"positive\",\n          \"verdict\": \"FAIL\"\n        },\n        \"partial_pooled\": {\n          \"r\": 0.142,\n          \"p\": 0.108,\n          \"n\": 54,\n          \"direction\": \"positive\",\n          \"verdict\": \"FAIL\"\n        }\n      },\n      \"pairwise_qwen3\": {\n        \"pearson_r\": -0.009,\n        \"pearson_p\": 0.38,\n        \"n_pairs\": 14028,\n        \"verdict\": \"FAIL\"\n      },\n      \"pairwise_minilm\": {\n        \"pearson_r\": 0.115,\n        \"pearson_p\": 2.1e-42,\n        \"n_pairs\": 14028,\n        \"spearman_rho\": 0.128,\n        \"nonzero_spearman_rho\": 0.185,\n        \"verdict\": \"PASS\"\n      },\n      \"per_type_qwen3\": {\n        \"spearman_rho\": 0.195,\n        \"p\": 0.018,\n        \"direction\": \"positive_confounded\"\n      },\n      \"per_type_minilm\": {\n        \"spearman_rho\": 0.212,\n        \"p\": 0.009,\n        \"direction\": \"positive_confounded\"\n      },\n      \"confusion_rate_extreme\": {\n        \"count_6_ratio\": 5.8,\n        \"count_12_ratio\": 4.2\n      },\n      \"confusion_rate_random\": {\n        \"count_6_ratio\": 1.4,\n        \"count_12_ratio\": 1.3\n      }\n    },\n    \"tables\": [\n      \"Table: MAVEN Count Curve (500 samples, relaxed matching)\\n| Count | Relaxed F1 | Exact F1 | Recall | Precision | Pred/Gold |\\n|-------|-----------|----------|--------|-----------|-----------|\\n| 1     | 0.098     | 0.008    | 0.070  | 0.162     | 0.43      |\\n| 6     | 0.112     | 0.005    | 0.085  | 0.165     | 0.52      |\\n| 12    | 0.155     | 0.011    | 0.118  | 0.226     | 0.52      |\\n| 22    | 0.192     | 0.016    | 0.148  | 0.274     | 0.54      |\\n| 44    | 0.238     | 0.021    | 0.180  | 0.350     | 0.51      |\\n| 64    | 0.241     | 0.018    | 0.182  | 0.358     | 0.51      |\\n\",\n      \"Table: MAVEN Within-Count BCS-F1 Correlation\\n| Count | r     | p     | Direction | Verdict |\\n|-------|-------|-------|-----------|---------|\\n| 6     | +0.175| 0.185 | positive  | FAIL    |\\n| 12    | +0.124| 0.315 | positive  | FAIL    |\\n| Pooled| +0.142| 0.108 | positive  | FAIL    |\\n\",\n      \"Table: MAVEN Pairwise & Per-Type (2×2 embedding matrix)\\n|          | Pairwise r (p)         | Per-type ρ (p)       |\\n|----------|------------------------|----------------------|\\n| Qwen3    | -0.009 (0.38) ✗        | +0.195 (0.018) ✗     |\\n| MiniLM   | +0.115 (2.1e-42) ✓     | +0.212 (0.009) ✗     |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 结果确认 centrality confound 假说：在语义同质 schema 中，per-type 和 within-count batch-level 分析均被 confound。唯一存活的信号是 MiniLM pairwise (r=0.115)，但 Qwen3 pairwise 失败，且效应量小（r²=1.3%）。MAVEN 的 count curve 反转是对 SDGD 方法的致命打击——如果更多 types 在 prompt 中反而帮助模型，那么 decomposition（减少 types）必然降低性能。worst tier 叙事中，MAVEN 作为 \\\"centrality confound case study\\\" 仍有方法论价值，但不支持 SDGD 的前提假设。\\n\\n\\nMAVEN 的 168 event types 全部来自 FrameNet，同一语义域，导致 type embedding 分布高度同质。这造成三个后果：(1) count curve 反转——更多 types 为模型提供更 丰富的 event ontology 上下文，帮助模型理解每个 type 在 taxonomy 中的位置，因此 F1 随 count 增加而上升；(2) within-count BCS 相关为正方向——高 BCS batch 包含 语义中心的常见 event types（如 Killing, Attack, Movement），这些 types 在 training data 中频次高、定义清晰，LLM 本就擅长提取，因此高 BCS → 高 F1， 这是 centrality confound 而非 confusability 效应；(3) confusion rate 比 Few-NERD 低得多（5.8x vs 27.5x），因为 event trigger 本身是 verb/nominalization 而非 entity mention，type confusion 的表现形式不同（trigger 共享率高但不一定是 confusability 导致）。pairwise MiniLM 仍显著（r=0.115, p≈0），因为 n=14028 pair 提供了极大统计功效，即使效应量小也能检出——但这个 r 值比 Few-NERD 的 0.156 低， 且 Qwen3 pairwise 完全不显著，说明 pairwise 信号在同质 schema 上高度依赖 embedding 选择。\\n\"\n  },\n  {\n    \"name\": \"DocRED Confusability Study\",\n    \"description\": \"DocRED（96 relation types）上的 confusability 研究：count curve + BCS 相关分析。 文档级 RE 的 scaling stress test。\\n\",\n    \"results\": {\n      \"count_curve_f1\": {\n        \"count_4\": 0.185,\n        \"count_8\": 0.192,\n        \"count_16\": 0.198,\n        \"count_32\": 0.203,\n        \"count_48\": 0.208,\n        \"count_96\": 0.195\n      },\n      \"count_curve_trend\": \"near-flat with slight peak at count_48, no clear monotonic pattern\",\n      \"within_count_bcs_f1\": {\n        \"count_8\": {\n          \"r\": 0.032,\n          \"p\": 0.62,\n          \"verdict\": \"FAIL\"\n        },\n        \"count_16\": {\n          \"r\": -0.058,\n          \"p\": 0.48,\n          \"verdict\": \"FAIL\"\n        },\n        \"partial_pooled\": {\n          \"r\": -0.015,\n          \"p\": 0.84,\n          \"verdict\": \"FAIL\"\n        }\n      },\n      \"pairwise_qwen3\": {\n        \"pearson_r\": 0.023,\n        \"pearson_p\": 0.14,\n        \"n_pairs\": 4560,\n        \"verdict\": \"FAIL\"\n      },\n      \"pairwise_minilm\": {\n        \"pearson_r\": 0.031,\n        \"pearson_p\": 0.08,\n        \"n_pairs\": 4560,\n        \"verdict\": \"FAIL\"\n      },\n      \"per_type_bcs_f1\": {\n        \"spearman_rho\": -0.04,\n        \"p\": 0.72,\n        \"verdict\": \"FAIL\"\n      },\n      \"confusion_rate_extreme_ratio\": 1.8,\n      \"overall_baseline_f1\": 0.195\n    },\n    \"tables\": [\n      \"Table: DocRED Count Curve (document-level RE)\\n| Count | F1    | Recall | Precision | Confusion Rate |\\n|-------|-------|--------|-----------|---------------|\\n| 4     | 0.185 | 0.145  | 0.256     | 0.008         |\\n| 8     | 0.192 | 0.152  | 0.261     | 0.012         |\\n| 16    | 0.198 | 0.158  | 0.264     | 0.015         |\\n| 32    | 0.203 | 0.165  | 0.258     | 0.018         |\\n| 48    | 0.208 | 0.170  | 0.261     | 0.019         |\\n| 96    | 0.195 | 0.160  | 0.250     | 0.022         |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 结果是完全的 null result。confusability 假说在文档级 RE 上完全不成立。 worst tier 叙事中，DocRED 证明 confusability 效应受限于 sentence-level 任务—— 文档级任务中其他复杂度维度（跨句推理、entity pair 组合）占主导。如果论文要报告 此结果，需要 reframe 为 \\\"boundary condition\\\"：confusability 效应在 type definitions 占 prompt 显著比例的任务中才成立。但此实验为 P1，worst tier 下可能 不运行（10 天内优先 P0 实验），视为 supplementary material。\\n\\n\\nDocRED 是文档级 RE，每个样本包含多个句子和多个 entity pairs。性能瓶颈完全不在 type confusability 上，而在于：(1) 跨句推理能力——关系证据分散在多个句子中，LLM 需要 coreference 和 multi-hop reasoning；(2) entity pair 组合爆炸——文档中 n 个实体产生 O(n²) 个候选关系对，模型必须处理大量负样本；(3) 关系类型定义本身 依赖 entity type 约束（如 \\\"place_of_birth\\\" 要求 subject=person, object=location）， 这种结构化约束比 embedding 相似度更能预测性能。confusability 信号被这些更强的 因素完全淹没。count curve 近乎平坦，因为文档级 RE 的 prompt 长度主要由文档内容 （而非 type 定义）决定——96 个 relation type name 只占 prompt 的很小比例。\\n\"\n  },\n  {\n    \"name\": \"Count × Confusability Interaction Effect\",\n    \"description\": \"Few-NERD 上 {low count=6, high count=22} × {low BCS, high BCS} 的 2×2 因子设计。 检验 count 和 confusability 的交互效应（additive vs multiplicative）。\\n\",\n    \"results\": {\n      \"cell_means_f1\": {\n        \"low_count_low_bcs\": 0.348,\n        \"low_count_high_bcs\": 0.312,\n        \"high_count_low_bcs\": 0.298,\n        \"high_count_high_bcs\": 0.255\n      },\n      \"two_way_anova\": {\n        \"count_main_effect\": {\n          \"F\": 7.82,\n          \"p\": 0.008,\n          \"eta_sq\": 0.14,\n          \"verdict\": \"SIGNIFICANT\"\n        },\n        \"bcs_main_effect\": {\n          \"F\": 2.93,\n          \"p\": 0.094,\n          \"eta_sq\": 0.06,\n          \"verdict\": \"MARGINAL\"\n        },\n        \"interaction\": {\n          \"F\": 0.31,\n          \"p\": 0.582,\n          \"eta_sq\": 0.006,\n          \"verdict\": \"NOT_SIGNIFICANT\"\n        }\n      },\n      \"n_batches_per_cell\": 12,\n      \"total_n\": 48,\n      \"simple_effects\": {\n        \"bcs_at_low_count\": {\n          \"delta_f1\": -0.036,\n          \"p\": 0.22\n        },\n        \"bcs_at_high_count\": {\n          \"delta_f1\": -0.043,\n          \"p\": 0.18\n        }\n      }\n    },\n    \"tables\": [\n      \"Table: 2×2 Cell Means (F1, text_match)\\n|                | Low BCS     | High BCS    | BCS Effect |\\n|----------------|-------------|-------------|------------|\\n| Low Count (6)  | 0.348       | 0.312       | Δ=-0.036   |\\n| High Count (22)| 0.298       | 0.255       | Δ=-0.043   |\\n| Count Effect   | Δ=-0.050   | Δ=-0.057   |            |\\n\",\n      \"Table: Two-Way ANOVA Results\\n| Source       | F     | p     | η²    | Verdict     |\\n|-------------|-------|-------|-------|-------------|\\n| Count        | 7.82  | 0.008 | 0.14  | Significant |\\n| BCS          | 2.93  | 0.094 | 0.06  | Marginal    |\\n| Count × BCS  | 0.31  | 0.582 | 0.006 | NS          |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"交互效应不显著是 worst tier 对 Claim 2（multi-channel degradation）的重大打击。 论文无法用 formal factorial design 证明两通道正交。只能退而求其次，基于 error taxonomy（exp-007）做 descriptive argument：count 降低 recall（omission）， confusability 增加 type confusion（substitution），两类错误机制不同→暗示正交。 但这种 descriptive 论证说服力远不如 significant interaction test。在 worst tier 叙事中，2×2 结果最多写一段文字报告 \\\"no significant interaction was detected, consistent with additive but not multiplicative independence\\\"。\\n\\n\\n2×2 设计的统计功效受限：每个 cell 约 12 个 batch，总 n=48。在这个样本量下， 检测交互效应需要 η²≥0.10 的大效应量。实际中，count 的主效应最强（η²=0.14）， 因为 count 直接影响 prompt 长度和 attention 分配，信号最清晰。BCS 主效应仅为 marginal（p=0.094），因为 batch-level BCS 与 F1 的关系本就受到 type frequency distribution 等 confound 的干扰——exp-002 已经表明 batch-level 信号远弱于 pairwise-level。交互效应完全不显著（p=0.582），说明 count 和 confusability 的 联合效应是（弱）加性的，不存在 multiplicative synergy。这在 worst tier 中意味 着论文只能声称 \\\"两个通道可能独立\\\" 但无法用 formal interaction test 支撑。\\n\"\n  },\n  {\n    \"name\": \"Systematic Error Taxonomy by BCS Bins\",\n    \"description\": \"对 Few-NERD exp-002 数据做系统 FP 分类（type_substitution / boundary_error / false_negative / hallucination），按 BCS bin 分析差异。机械层面支撑 multi-channel 模型。\\n\",\n    \"results\": {\n      \"error_distribution_overall\": {\n        \"type_substitution_pct\": 0.18,\n        \"boundary_error_pct\": 0.12,\n        \"spurious_extraction_pct\": 0.45,\n        \"missed_entity_pct\": 0.25\n      },\n      \"type_substitution_by_bcs\": {\n        \"extreme_high_bcs_rate\": 0.058,\n        \"extreme_low_bcs_rate\": 0.012,\n        \"extreme_ratio\": 4.8,\n        \"random_high_bcs_rate\": 0.022,\n        \"random_low_bcs_rate\": 0.015,\n        \"random_ratio\": 1.5\n      },\n      \"boundary_error_by_bcs\": {\n        \"high_bcs_rate\": 0.041,\n        \"low_bcs_rate\": 0.038,\n        \"ratio\": 1.08,\n        \"verdict\": \"NO_EFFECT\"\n      },\n      \"missed_entity_by_count\": {\n        \"count_6_miss_rate\": 0.28,\n        \"count_22_miss_rate\": 0.42,\n        \"count_64_miss_rate\": 0.55,\n        \"trend\": \"monotonically increasing with count\"\n      },\n      \"missed_entity_by_bcs\": {\n        \"high_bcs_miss_rate\": 0.4,\n        \"low_bcs_miss_rate\": 0.38,\n        \"ratio\": 1.05,\n        \"verdict\": \"NO_EFFECT\"\n      },\n      \"hallucination_rate\": 0.03,\n      \"hallucination_by_bcs\": {\n        \"verdict\": \"NO_EFFECT\"\n      }\n    },\n    \"tables\": [\n      \"Table: Error Distribution Overall\\n| Error Type          | Proportion | Primary Driver |\\n|---------------------|------------|----------------|\\n| Spurious Extraction | 45%        | Prompt format  |\\n| Missed Entity       | 25%        | Count (recall) |\\n| Type Substitution   | 18%        | BCS (confuse)  |\\n| Boundary Error      | 12%        | Span detection |\\n\",\n      \"Table: Type Substitution Rate by BCS Condition\\n| Condition     | High BCS | Low BCS | Ratio |\\n|---------------|----------|---------|-------|\\n| Extreme Batch | 0.058    | 0.012   | 4.8x  |\\n| Random Batch  | 0.022    | 0.015   | 1.5x  |\\n\",\n      \"Table: Missed Entity Rate by Count\\n| Count | Miss Rate | Δ vs Count_6 |\\n|-------|-----------|--------------|\\n| 6     | 0.28      | —            |\\n| 22    | 0.42      | +0.14        |\\n| 64    | 0.55      | +0.27        |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error taxonomy 部分支持 multi-channel 模型：(1) type substitution 受 BCS 影响 （extreme 4.8x），(2) missed entity 受 count 影响（monotonic）。但 worst tier 下两个弱点：(a) type substitution 只占总 error 的 18%，不是 dominant mode—— reviewer 会质疑 \\\"如果 confusability 只解释 18% 的 error，实际影响有多大？\\\"； (b) random batch ratio 仅 1.5x，远低于 extreme 的 4.8x——说明自然分布下效应 很小。论文只能做 descriptive analysis，不能做 formal causal claim。在 worst tier 叙事中，error taxonomy 作为 supporting evidence 放在 analysis section， 不作为独立 finding。\\n\\n\\nError taxonomy 的分类本身是 noisy 的——boundary error vs type substitution 的 区分依赖 text_match 容差设定。在 worst tier 下：(1) type substitution 在 extreme high-BCS batch 中确实更多（4.8x ratio），但 extreme batches 是刻意构造的极端 条件，random batches 中 ratio 仅 1.5x，实际场景中效应有限；(2) boundary error 不受 BCS 影响（ratio≈1.0），符合预期——boundary detection 是 span 层面的任务， 与 type confusability 无关；(3) missed entity（false negative）主要由 count 驱动（count_6 miss 28% vs count_64 miss 55%），不受 BCS 影响——支持 count→recall 通道；(4) 但整体 error 中 spurious extraction 占 45%，远超 type substitution 的 18%——这意味着 LLM 的主要问题是 \\\"提取不该提取的 span\\\" 而非 \\\"type 标错\\\"， confusability 只解释了一小部分 error。worst tier 的核心问题是：type confusion 不是 dominant error mode，因此 confusability 的实际影响被其他 error 源稀释。\\n\"\n  },\n  {\n    \"name\": \"LLaMA-3.3-70B Multi-Model Validation\",\n    \"description\": \"用 LLaMA-3.3-70B-Instruct 复制 exp-002 protocol（Few-NERD, 25 random + extreme batches, count=6/12, pairwise + per-type 分析）。检验 confusability 效应的跨模型 泛化性。\\n\",\n    \"results\": {\n      \"baseline_f1_count64\": 0.378,\n      \"baseline_vs_qwen3\": \"Δ=-3.6pp (Qwen3=0.414)\",\n      \"pairwise_qwen3_embed\": {\n        \"pearson_r\": 0.042,\n        \"pearson_p\": 0.068,\n        \"n_pairs\": 1953,\n        \"verdict\": \"NOT_SIGNIFICANT\"\n      },\n      \"pairwise_qwen3_embed_nonzero\": {\n        \"spearman_rho\": 0.078,\n        \"p\": 0.12,\n        \"verdict\": \"NOT_SIGNIFICANT\"\n      },\n      \"per_type_bcs_f1\": {\n        \"spearman_rho\": -0.082,\n        \"p\": 0.538,\n        \"n_types\": 58,\n        \"partial_r_ctrl_logfreq\": -0.055,\n        \"partial_p\": 0.684,\n        \"verdict\": \"NOT_SIGNIFICANT\"\n      },\n      \"batch_f1_vs_bcs\": {\n        \"count_6\": {\n          \"r\": 0.108,\n          \"p\": 0.42\n        },\n        \"count_12\": {\n          \"r\": 0.185,\n          \"p\": 0.21\n        },\n        \"partial_pooled\": {\n          \"r\": 0.138,\n          \"p\": 0.16\n        }\n      },\n      \"confusion_rate_extreme\": {\n        \"count_6_high\": 0.025,\n        \"count_6_low\": 0.01,\n        \"ratio_6\": 2.5,\n        \"count_12_high\": 0.032,\n        \"count_12_low\": 0.015,\n        \"ratio_12\": 2.1\n      },\n      \"confusion_rate_random\": {\n        \"count_6_ratio\": 1.2,\n        \"count_12_ratio\": 1.15\n      },\n      \"cross_model_summary\": {\n        \"qwen3_pairwise_r\": 0.156,\n        \"llama_pairwise_r\": 0.042,\n        \"qwen3_extreme_ratio\": \"10-28x\",\n        \"llama_extreme_ratio\": \"2.1-2.5x\",\n        \"qwen3_per_type_rho\": -0.293,\n        \"llama_per_type_rho\": -0.082\n      }\n    },\n    \"tables\": [\n      \"Table: Cross-Model Comparison (Few-NERD)\\n| Metric                    | Qwen3-32B    | LLaMA-3.3-70B | Ratio    |\\n|---------------------------|-------------|---------------|----------|\\n| Baseline F1 (count_64)    | 0.414       | 0.378         | 0.91x    |\\n| Pairwise r (Qwen3 embed)  | 0.156***    | 0.042 (ns)    | 0.27x    |\\n| Per-type ρ                | -0.293*     | -0.082 (ns)   | 0.28x    |\\n| Extreme confusion ratio   | 10-28x      | 2.1-2.5x      | 0.10x    |\\n| Random confusion ratio    | 1.7-2.4x    | 1.15-1.2x     | 0.50x    |\\n\",\n      \"Table: LLaMA Pairwise & Per-Type Statistics\\n| Analysis        | Statistic | Value  | p     | Verdict |\\n|-----------------|-----------|--------|-------|---------|\\n| Pairwise        | Pearson r | 0.042  | 0.068 | NS      |\\n| Pairwise NZ     | Spearman  | 0.078  | 0.120 | NS      |\\n| Per-type        | Spearman  | -0.082 | 0.538 | NS      |\\n| Per-type partial| Partial r | -0.055 | 0.684 | NS      |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLaMA 结果是 worst tier 中最关键的 negative result。cross_model_significant = 1 （仅 Qwen3），这意味着 confusability 效应可能是 Qwen3 特有的，而非 LLM IE 的 普遍现象。论文必须显著降级 Claim 1 的 generalizability：从 \\\"confusability independently predicts degradation in training-free LLM IE\\\" 改为 \\\"confusability sensitivity varies substantially across model families, with Qwen3 showing strong effects (r=0.156) and LLaMA showing weak/null effects (r=0.042)\\\"。在 worst tier 叙事中，这可 reframe 为解释力：\\\"prior conflicting findings about schema complexity may be partly explained by model-dependent confusability sensitivity\\\"——将缺陷转为贡献，但 reviewer 是否买账取决于写作。\\n\\n\\nLLaMA-3.3-70B 与 Qwen3-32B 在 confusability 敏感度上存在根本差异，原因可能是： (1) 模型规模差异——70B vs 32B，更大的模型有更大的 attention capacity，能更好地 处理 confusable types 的共现，因此 confusability 的 degradation 效应被缓解； (2) instruction tuning 差异——LLaMA-3.3 的 RLHF 训练可能更强调 precision 和 faithfulness，模型在不确定时倾向不输出（而非猜测相似 type），导致 type confusion error 本就少，confusability 信号弱；(3) internal representation 差异——LLaMA 的 embedding 空间对 Few-NERD types 的组织方式可能与 Qwen3 不同，Qwen3 embedding 中的 semantic proximity 模式不能直接迁移为 LLaMA 的 confusion 模式。\\npairwise r=0.042 (p=0.068) 在 α=0.05 下不显著但接近边界——这是最棘手的 结果：不能说完全无信号（p=0.068），但也不能声称显著。在 worst tier 叙事中， 这被 reframe 为 \\\"confusability effects are model-dependent, with effect size varying by 4x across model families (r=0.156 Qwen3 vs r=0.042 LLaMA)\\\"。confusion rate ratio 也大幅下降（2.5x vs Qwen3 的 27.5x），进一步说明 LLaMA 对 type confusion 更鲁棒。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on Few-NERD\",\n    \"description\": \"Few-NERD 上的 SDGD-zero：Qwen3 embedding SCS + graph coloring (τ adaptive, k=1.0) 生成 confusability-minimizing batches，与 single-pass 对比。\\n\",\n    \"results\": {\n      \"graph_stats\": {\n        \"threshold_tau\": 0.847,\n        \"n_edges\": 142,\n        \"edge_density\": 0.066,\n        \"chromatic_number\": 8,\n        \"avg_batch_size\": 8.25,\n        \"max_batch_size\": 12,\n        \"min_batch_size\": 4,\n        \"max_intra_batch_bcs\": 0.842\n      },\n      \"sdgd_zero\": {\n        \"f1\": 0.367,\n        \"precision\": 0.318,\n        \"recall\": 0.434,\n        \"pred_gold_ratio\": 1.36\n      },\n      \"single_pass\": {\n        \"f1\": 0.414,\n        \"precision\": 0.648,\n        \"recall\": 0.304\n      },\n      \"delta_f1_vs_single_pass\": -4.7,\n      \"delta_precision\": -33.0,\n      \"delta_recall\": 13.0,\n      \"per_batch_f1_range\": [\n        0.28,\n        0.42\n      ],\n      \"per_batch_recall_range\": [\n        0.35,\n        0.52\n      ],\n      \"per_batch_precision_range\": [\n        0.22,\n        0.38\n      ],\n      \"merge_stats\": {\n        \"total_predictions\": 4850,\n        \"unique_predictions_after_dedup\": 4120,\n        \"cross_batch_span_overlap\": 0.08,\n        \"predictions_per_sample_avg\": 8.2,\n        \"gold_per_sample_avg\": 5.9\n      },\n      \"api_calls\": \"8x single-pass (8000 vs 1000 for 1000 samples)\",\n      \"wall_clock_multiplier\": 6.5\n    },\n    \"tables\": [\n      \"Table: SDGD-zero vs Single-Pass (Few-NERD, 66 types)\\n| Method      | F1    | Precision | Recall | Pred/Gold | API Calls |\\n|-------------|-------|-----------|--------|-----------|-----------|\\n| Single-pass | 0.414 | 0.648     | 0.304  | 0.47      | 1x        |\\n| SDGD-zero   | 0.367 | 0.318     | 0.434  | 1.36      | 8x        |\\n| Δ           | -4.7pp| -33.0pp   | +13.0pp| +0.89     | +7x       |\\n\",\n      \"Table: SDGD-zero Per-Batch Breakdown (top 4 batches)\\n| Batch | Types | Avg BCS | F1    | Recall | Precision |\\n|-------|-------|---------|-------|--------|-----------|\\n| 0     | 12    | 0.812   | 0.42  | 0.48   | 0.38      |\\n| 1     | 10    | 0.795   | 0.38  | 0.45   | 0.33      |\\n| 2     | 9     | 0.780   | 0.35  | 0.42   | 0.30      |\\n| 3     | 8     | 0.763   | 0.32  | 0.40   | 0.27      |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-zero 的失败是 worst tier 的核心 negative result。直接否定 Claim 3。 failure mode 清晰且可解释：separating confusable types 剥夺了模型的 comparative disambiguation 能力。这是一个 informative negative result——它揭示了 LLM IE 中 type co-presence 的 dual role：(1) 增加 confusability（hypothesis 的前提）， (2) 提供 disambiguation context（SDGD 未预见的副作用）。在 worst tier 叙事中， 这个发现可以作为论文的一个 insight：\\\"confusability is a two-edged sword — the same type co-presence that causes confusion also enables disambiguation\\\"， 解释为什么简单的 separation strategy 不 work。但这最多放在 Discussion section， 不能作为 core contribution。\\n\\n\\nSDGD-zero 失败的核心机制是 \\\"disambiguation context loss\\\"。当 confusable types 被分到不同 batch 时，每个 batch 中的模型只看到 pair 的一端。例如 person-other 在 batch A，person-politician 在 batch B。处理含政治人物的句子时：\\n- Batch A（有 person-other，无 person-politician）：模型将政治人物标为\\n  person-other（因为这是最接近的可用 type）→ FP for person-other\\n- Batch B（有 person-politician，无 person-other）：模型将普通人标为\\n  person-politician（同理）→ FP for person-politician\\n\\nmerge 后，同一实体可能被两个 batch 分别标为不同 type（cross-batch span overlap 8%），评估时只有一个是 TP，另一个是 FP。更严重的是，每个 batch 只有 ~8 types， 模型倾向过度提取（pred/gold=1.36 vs single-pass 的 0.47），precision 从 0.648 暴跌到 0.318。recall 确实从 0.304 提升到 0.434（smaller batch → 更多 attention 给每个 type），但 precision 损失远大于 recall 增益。\\nF1 = 0.367 比 single-pass 的 0.414 低 4.7pp。SDGD 的前提假设（separating confusable types reduces confusion）是错误的——对 LLM 来说，看到 confusable types 的完整集合反而帮助 disambiguation。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on MAVEN\",\n    \"description\": \"MAVEN（168 event types）上的 SDGD-zero。用 adaptive threshold (k=1.0) 生成 confusability-minimizing batches。跨任务（NER→ED）验证 SDGD。\\n\",\n    \"results\": {\n      \"graph_stats\": {\n        \"embedding\": \"qwen3\",\n        \"scs_mean\": 0.216,\n        \"scs_std\": 0.103,\n        \"threshold_tau\": 0.319,\n        \"n_edges\": 1850,\n        \"edge_density\": 0.132,\n        \"chromatic_number\": 15,\n        \"avg_batch_size\": 11.2,\n        \"min_batch_size\": 5,\n        \"max_batch_size\": 18\n      },\n      \"sdgd_zero\": {\n        \"relaxed_f1\": 0.168,\n        \"exact_f1\": 0.012,\n        \"relaxed_recall\": 0.13,\n        \"relaxed_precision\": 0.238\n      },\n      \"single_pass\": {\n        \"relaxed_f1\": 0.241,\n        \"exact_f1\": 0.018\n      },\n      \"delta_relaxed_f1\": -7.3,\n      \"api_calls\": \"15x single-pass\",\n      \"wall_clock_multiplier\": 12.8\n    },\n    \"tables\": [\n      \"Table: SDGD-zero vs Single-Pass (MAVEN, 168 types)\\n| Method      | Relaxed F1 | Exact F1 | API Calls | Wall-Clock |\\n|-------------|-----------|----------|-----------|------------|\\n| Single-pass | 0.241     | 0.018    | 1x        | 1x         |\\n| SDGD-zero   | 0.168     | 0.012    | 15x       | 12.8x      |\\n| Δ           | -7.3pp    | -0.6pp   | +14x      | +11.8x     |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN SDGD-zero 是最差的结果之一。15x API cost 换来 -7.3pp 性能下降。 与 Few-NERD 的 SDGD 失败共同构成 Claim 3 的致命反证：SDGD 在两个任务上 都差于 single-pass，且效果 consistent（方向一致、机制相同）。在 worst tier 叙事中，SDGD 相关实验（exp-008, 009, 010, 011, 013, 014）全部降级为 appendix 中的 negative result case study，正文仅用 1-2 段文字总结 \\\"we also explored confusability-minimizing decomposition, which failed because...\\\"。\\n\\n\\nMAVEN 上 SDGD-zero 失败更严重（Δ=-7.3pp vs Few-NERD 的 -4.7pp），原因： (1) MAVEN count curve 是上升的——更多 types 帮助模型理解 event ontology， decomposition 直接损害这个优势；(2) adaptive τ=0.319（因 MAVEN Qwen3 SCS 分布集中在低值区间），graph 中 edge density=13.2%，coloring 产生 15 个 batch， 每个约 11 types——这比 single-pass 的 168 types 少了 93%的 type 上下文； (3) 15 个 batch 意味着 15x API 调用，wall-clock 12.8x 但性能反而更差—— cost-quality 全面恶化；(4) MAVEN event trigger 是 verb/nominalization，多个 event type 共享同一 trigger word（如 \\\"attack\\\" 可以是 Attack 也可以是 Conflict）， 模型需要看到完整 event taxonomy 才能正确 assign type。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on Few-NERD\",\n    \"description\": \"Few-NERD 上的 SDGD-cal：用 5-10 calibration examples 构建 empirical confusion matrix，替代 embedding SCS。与 SDGD-zero 和 single-pass 对比。\\n\",\n    \"results\": {\n      \"calibration_stats\": {\n        \"n_calibration_samples\": 8,\n        \"calibration_api_calls\": 8,\n        \"empirical_confusion_pairs_nonzero\": 85,\n        \"spearman_vs_embedding_scs\": 0.125,\n        \"p_vs_embedding_scs\": 0.031\n      },\n      \"graph_stats\": {\n        \"threshold_tau\": \"adaptive on empirical confusion\",\n        \"n_edges\": 62,\n        \"chromatic_number\": 7,\n        \"avg_batch_size\": 9.4\n      },\n      \"sdgd_cal\": {\n        \"f1\": 0.381,\n        \"precision\": 0.342,\n        \"recall\": 0.43,\n        \"pred_gold_ratio\": 1.26\n      },\n      \"comparison\": {\n        \"vs_single_pass_delta\": -3.3,\n        \"vs_sdgd_zero_delta\": 1.4,\n        \"vs_random_delta\": 0.7,\n        \"vs_random_p\": 0.58\n      },\n      \"single_pass_f1\": 0.414,\n      \"sdgd_zero_f1\": 0.367,\n      \"random_f1\": 0.374\n    },\n    \"tables\": [\n      \"Table: SDGD-cal vs Baselines (Few-NERD)\\n| Method      | F1    | Δ vs SP | Precision | Recall | API Overhead   |\\n|-------------|-------|---------|-----------|--------|----------------|\\n| Single-pass | 0.414 | —       | 0.648     | 0.304  | 1x             |\\n| Random (k=8)| 0.374 | -4.0    | 0.335     | 0.425  | 8x             |\\n| SDGD-zero   | 0.367 | -4.7    | 0.318     | 0.434  | 8x             |\\n| SDGD-cal    | 0.381 | -3.3    | 0.342     | 0.430  | 7x + 8 calib   |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-cal 是 SDGD 方法线的 \\\"best effort\\\"——用 ground truth confusion 替代 proxy。 即使如此仍低于 single-pass 3.3pp。这最终否定了 confusability-minimizing decomposition 的整体方法路线：问题不在 confusion matrix 的质量，而在于 decomposition 本身损害了 LLM 的 disambiguation context。在 worst tier 叙事中， SDGD-cal 的 marginal improvement over SDGD-zero 可作为 exp-015（SCS validation） 的间接证据：embedding proxy 与 empirical confusion 仅弱相关（ρ=0.125），但这 不是失败的主因——即使 perfect confusion matrix 也不能拯救 decomposition strategy。\\n\\n\\nSDGD-cal 比 SDGD-zero 好（+1.4pp），因为 empirical confusion matrix 比 embedding SCS 更准确地反映实际 model confusion：(1) 非零 confusion pair 只有 85 对（vs embedding SCS 的 142 条 edge），graph 更稀疏 → 7 个 batch（vs 8 个），每个 batch 更大 → 更多 type 上下文；(2) calibration 捕捉到一些 embedding SCS 预测不 到的 confusion pattern（如语义不近但 surface form 相似的 type pair）。但 SDGD-cal 仍低于 single-pass 3.3pp，因为 decomposition 的核心问题（disambiguation context loss）不因 confusion matrix 质量改善而消失。与 random batching 的差异仅 +0.7pp (p=0.58)，不显著——confusability-aware grouping 即使用了 empirical data 也没有 显著优势。calibration 的额外 cost（8 次 API 调用）换来的 improvement 微乎其微。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on MAVEN\",\n    \"description\": \"MAVEN（168 types）上的 SDGD-cal：empirical confusion matrix + graph coloring。 Full comparison table。\\n\",\n    \"results\": {\n      \"calibration_stats\": {\n        \"n_calibration_samples\": 10,\n        \"empirical_confusion_pairs_nonzero\": 210\n      },\n      \"graph_stats\": {\n        \"chromatic_number\": 12,\n        \"avg_batch_size\": 14.0\n      },\n      \"sdgd_cal\": {\n        \"relaxed_f1\": 0.188,\n        \"exact_f1\": 0.014\n      },\n      \"comparison\": {\n        \"vs_single_pass_delta\": -5.3,\n        \"vs_sdgd_zero_delta\": 2.0,\n        \"vs_random_delta\": 0.8,\n        \"vs_random_p\": 0.62\n      },\n      \"single_pass_relaxed_f1\": 0.241,\n      \"sdgd_zero_relaxed_f1\": 0.168,\n      \"random_relaxed_f1\": 0.18\n    },\n    \"tables\": [\n      \"Table: Full Comparison (MAVEN, 168 types, relaxed matching)\\n| Method      | Relaxed F1 | Δ vs SP | API Calls      |\\n|-------------|-----------|---------|----------------|\\n| Single-pass | 0.241     | —       | 1x             |\\n| Random (k=12)| 0.180    | -6.1    | 12x            |\\n| SDGD-zero   | 0.168     | -7.3    | 15x            |\\n| SDGD-cal    | 0.188     | -5.3    | 12x + 10 calib |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN SDGD-cal 确认 decomposition 在 event detection 上全面失败。所有方法 均差于 single-pass，且 MAVEN 的差距（5-7pp）比 Few-NERD（3-5pp）更大。 这强化了 worst tier 的核心结论：decomposition 不是通用 solution，type co-presence 在很多场景中是 feature 而非 bug。\\n\\n\\n与 Few-NERD 相同模式：SDGD-cal 好于 SDGD-zero（+2.0pp）但仍远差于 single-pass （-5.3pp）。MAVEN 的 empirical confusion matrix 更密（210 nonzero pairs vs Few-NERD 的 85），因为 168 types 中很多 event type 确实会互相 confuse（尤其是 同一 FrameNet frame 下的 sibling types）。但 calibration 帮助有限——核心问题 仍然是 MAVEN 的性能与 type count 正相关，decomposition 损害性能。\\n\"\n  },\n  {\n    \"name\": \"Random Batching Ablation\",\n    \"description\": \"与 SDGD-zero 相同 batch 数量 k，随机分组。隔离 confusability-aware grouping 的价值（排除 batch count reduction 的贡献）。\\n\",\n    \"results\": {\n      \"fewnerd\": {\n        \"random_f1\": 0.374,\n        \"sdgd_zero_f1\": 0.367,\n        \"delta_sdgd_vs_random\": -0.7,\n        \"paired_t_p\": 0.68,\n        \"n_random_seeds\": 10,\n        \"random_f1_std\": 0.018,\n        \"random_f1_range\": [\n          0.348,\n          0.402\n        ],\n        \"single_pass_f1\": 0.414\n      },\n      \"maven\": {\n        \"random_relaxed_f1\": 0.18,\n        \"sdgd_zero_relaxed_f1\": 0.168,\n        \"delta_sdgd_vs_random\": -1.2,\n        \"paired_t_p\": 0.42,\n        \"n_random_seeds\": 5\n      },\n      \"interpretation\": {\n        \"sdgd_vs_random_significant\": false,\n        \"confusability_aware_grouping_benefit\": null\n      }\n    },\n    \"tables\": [\n      \"Table: Random vs SDGD-zero (Few-NERD, k=8)\\n| Method     | Mean F1 | Std   | Range         | vs Single-Pass |\\n|------------|---------|-------|---------------|----------------|\\n| Random×10  | 0.374   | 0.018 | [0.348,0.402] | -4.0pp         |\\n| SDGD-zero  | 0.367   | —     | —             | -4.7pp         |\\n| Δ (SDGD-Random) | -0.7pp | — | —           | p=0.68 (NS)    |\\n\",\n      \"Table: Random vs SDGD-zero (MAVEN, k=15/12)\\n| Method     | Relaxed F1 | vs Single-Pass |\\n|------------|-----------|----------------|\\n| Random×5   | 0.180     | -6.1pp         |\\n| SDGD-zero  | 0.168     | -7.3pp         |\\n| Δ          | -1.2pp    | p=0.42 (NS)    |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Random batching ablation 是 Claim 3 的 definitive kill shot。SDGD 不显著优于 random→confusability-aware grouping 无价值。combined with SDGD < single-pass→ decomposition 本身有害。Claim 3 完全不成立。在 worst tier 叙事中，这个实验 的 negative result 本身有教育意义：it demonstrates that the intuitive principle \\\"separate confusable types\\\" is wrong for LLM IE，因为 LLMs 使用 type co-presence 做 comparative reasoning。\\n\\n\\nRandom batching 在 10 个 random seeds 上平均 F1=0.374（std=0.018），而 SDGD-zero F1=0.367。SDGD 比 random 差 0.7pp（p=0.68），差异不显著。实际上 SDGD 可能略 差于 random，因为 SDGD 刻意将 confusable types 分开——这意味着每个 batch 内的 types 都是 semantically distant 的，模型缺乏同一 semantic cluster 的 types 作为 disambiguation anchor。Random batching 偶尔会把 confusable types 放在一起 （概率约 1/k），这些 batch 的 disambiguation 更好，平均下来 random 反而略优。\\n在 MAVEN 上同样：random F1=0.180 vs SDGD F1=0.168（Δ=-1.2pp, p=0.42）。 SDGD 的 confusability-aware grouping 不仅无益，可能有害。\\n\"\n  },\n  {\n    \"name\": \"Per-Type Splitting (UniNER-style) Ablation\",\n    \"description\": \"1 type per batch（k=66/168）。Decomposition 的上界。揭示 latency-quality tradeoff。\\n\",\n    \"results\": {\n      \"fewnerd\": {\n        \"per_type_f1\": 0.33,\n        \"per_type_precision\": 0.225,\n        \"per_type_recall\": 0.62,\n        \"api_calls\": \"66x single-pass\",\n        \"wall_clock_multiplier\": 48.0\n      },\n      \"maven\": {\n        \"per_type_relaxed_f1\": 0.108,\n        \"api_calls\": \"168x single-pass\",\n        \"wall_clock_multiplier\": 135.0\n      },\n      \"comparison_fewnerd\": {\n        \"single_pass\": 0.414,\n        \"sdgd_zero\": 0.367,\n        \"random\": 0.374,\n        \"per_type\": 0.33\n      },\n      \"ordering\": \"single-pass > random ≈ SDGD-zero > per-type\"\n    },\n    \"tables\": [\n      \"Table: Full Method Comparison (Few-NERD)\\n| Method      | F1    | Precision | Recall | API Calls | Wall-Clock |\\n|-------------|-------|-----------|--------|-----------|------------|\\n| Single-pass | 0.414 | 0.648     | 0.304  | 1x        | 1x         |\\n| SDGD-cal    | 0.381 | 0.342     | 0.430  | 7x        | 5.5x       |\\n| Random (k=8)| 0.374 | 0.335     | 0.425  | 8x        | 6.5x       |\\n| SDGD-zero   | 0.367 | 0.318     | 0.434  | 8x        | 6.5x       |\\n| Per-type    | 0.330 | 0.225     | 0.620  | 66x       | 48x        |\\n\",\n      \"Table: Full Method Comparison (MAVEN, relaxed)\\n| Method      | Relaxed F1 | API Calls | Wall-Clock |\\n|-------------|-----------|-----------|------------|\\n| Single-pass | 0.241     | 1x        | 1x         |\\n| SDGD-cal    | 0.188     | 12x       | 10x        |\\n| Random      | 0.180     | 12x       | 10x        |\\n| SDGD-zero   | 0.168     | 15x       | 12.8x      |\\n| Per-type    | 0.108     | 168x      | 135x       |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type ablation 完成了 decomposition failure 的完整图景。方法排序 single-pass > random ≈ SDGD > per-type 说明：(1) decomposition granularity 与 F1 反相关；(2) type co-presence 是 net positive（disambiguation > confusion）； (3) SDGD 的 confusability-aware grouping 不提供额外价值（≈ random）。 在 worst tier 叙事中，这个结果可 reframe 为 empirical finding：\\\"LLM IE benefits from full schema visibility; type co-presence enables comparative reasoning that outweighs confusability-induced errors\\\"——这本身是一个有价值 的 insight，但不是 method contribution。\\n\\n\\nPer-type splitting 是 decomposition 的极端形式：每个 batch 只有 1 个 type。 这完全消除 type confusion（BCS=0），但也完全消除 disambiguation context。\\nFew-NERD 结果（F1=0.330）几乎等于 exp003a count_1 的 F1=0.323——符合预期， 因为 per-type extraction 本质就是 count=1。precision 极低（0.225）因为模型 只知道一个 type，会把任何像样的 span 都标为该 type（massive over-extraction）。 recall 最高（0.620）因为模型 aggressively 搜索这个 type 的所有 instance。\\nMAVEN 更惨（relaxed F1=0.108），因为 MAVEN 的 count_1 relaxed_F1 就只有 0.098。 168x API 调用使 wall-clock time 完全不可接受。\\n排序 single-pass > random ≈ SDGD > per-type 证明：decomposition granularity 与性能成反比。batch 越大越好（更多 type context），单pass 最优。\\n\"\n  },\n  {\n    \"name\": \"Embedding SCS vs Empirical Confusion Validation\",\n    \"description\": \"计算 embedding SCS（Qwen3 / MiniLM）与 empirical confusion matrix 之间的 rank correlation。验证 embedding proxy 对实际 model confusion 的预测力。\\n\",\n    \"results\": {\n      \"qwen3_scs_vs_empirical\": {\n        \"spearman_rho\": 0.125,\n        \"p\": 0.031,\n        \"kendall_tau\": 0.092,\n        \"p_kendall\": 0.044,\n        \"n_pairs_with_confusion\": 85\n      },\n      \"minilm_scs_vs_empirical\": {\n        \"spearman_rho\": 0.098,\n        \"p\": 0.082,\n        \"kendall_tau\": 0.071,\n        \"p_kendall\": 0.115,\n        \"n_pairs_with_confusion\": 85\n      },\n      \"top_confused_pair_scs_rank\": {\n        \"person_other_politician\": {\n          \"scs_rank\": 3,\n          \"confusion_rank\": 1\n        },\n        \"building_other_library\": {\n          \"scs_rank\": 45,\n          \"confusion_rank\": 8,\n          \"comment\": \"high confusion, low SCS — embedding 未捕捉的 confusion pattern\"\n        }\n      },\n      \"scs_false_positive_rate\": 0.42,\n      \"scs_false_negative_rate\": 0.35\n    },\n    \"tables\": [\n      \"Table: SCS vs Empirical Confusion Correlation\\n| Embedding | Spearman ρ | p     | Kendall τ | p     |\\n|-----------|-----------|-------|-----------|-------|\\n| Qwen3     | 0.125     | 0.031 | 0.092     | 0.044 |\\n| MiniLM    | 0.098     | 0.082 | 0.071     | 0.115 |\\n\",\n      \"Table: SCS Proxy Error Analysis\\n| Metric              | Qwen3 | MiniLM |\\n|---------------------|-------|--------|\\n| False Positive Rate | 0.42  | 0.48   |\\n| False Negative Rate | 0.35  | 0.40   |\\n| Top-1 Match         | Yes   | No     |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS validation 结果解释了 SDGD 失败的一个次要原因（proxy 质量差），但不是主因 （主因是 decomposition 本身有害）。ρ=0.125 说明 embedding SCS 只能解释 ~1.6% 的 confusion variance——作为 graph 构建的基础远远不够。即使用 empirical confusion (exp-010 SDGD-cal) 也只比 random 好 0.7pp（不显著），所以 proxy 质量不是瓶颈。 在 worst tier 叙事中，SCS validation 作为 methodological finding 报告： \\\"embedding-based confusability proxies have limited predictive power for actual model confusion patterns, suggesting that confusability is mediated by factors beyond semantic similarity\\\"——这对未来工作有指导价值。\\n\\n\\nEmbedding SCS 与 empirical confusion 仅弱相关（ρ=0.125），原因：(1) embedding similarity 反映 semantic proximity，但 model confusion 还受 surface form similarity、type definition wording、in-context position 等因素影响——这些因素 与 embedding space 正交；(2) SCS 是对称的（sim(A,B)=sim(B,A)），但实际 confusion 是非对称的（person-other → person-politician 的概率可能远高于反向）；(3) 42% 的 false positive rate 意味着 SCS 预测为 confusable 的 type pair 中近一半实际 不被 confuse——这些 false alarm 导致 SDGD-zero 过度分离 types，graph 变密， batch 数量过多。\\nMiniLM SCS 更差（ρ=0.098, p=0.082），因为 MiniLM 是 general-purpose sentence embedding，不 align 到 Qwen3 的 internal representation。这解释了为什么 extraction model alignment 对 per-type signal 很重要（exp-002 中 Qwen3 per-type ρ=-0.293 vs MiniLM ρ≈0）。\\n\"\n  },\n  {\n    \"name\": \"Cross-Experiment Summary (for paper narrative)\",\n    \"description\": \"综合所有实验的 worst tier 结果，构建论文核心 tables 和 narrative。\\n\",\n    \"results\": {\n      \"claim1_pairwise_matrix\": {\n        \"qwen3_fewnerd\": \"r=0.156*** ✓\",\n        \"qwen3_maven\": \"r=-0.009 (ns) ✗\",\n        \"qwen3_fewrel\": \"pending\",\n        \"minilm_fewnerd\": \"not tested\",\n        \"minilm_maven\": \"r=0.115*** ✓\",\n        \"minilm_fewrel\": \"Δ=21-50pp ✓ (pilot)\",\n        \"llama_fewnerd\": \"r=0.042 (ns) ✗\",\n        \"significant_cells\": 3,\n        \"total_cells\": 7,\n        \"verdict\": \"partial — 3/7 significant, no single embedding/model universally works\"\n      },\n      \"claim2_evidence\": {\n        \"count_recall_monotonic\": true,\n        \"bcs_type_substitution_ratio_extreme\": \"4.8x\",\n        \"bcs_type_substitution_ratio_random\": \"1.5x\",\n        \"interaction_significant\": false,\n        \"error_taxonomy_dominant_mode\": \"spurious extraction (45%), not type confusion (18%)\",\n        \"verdict\": \"directional — channels exist but confusability channel is weak relative to other error sources\"\n      },\n      \"claim3_evidence\": {\n        \"sdgd_zero_fewnerd\": \"F1=0.367, Δ=-4.7pp vs SP\",\n        \"sdgd_zero_maven\": \"relF1=0.168, Δ=-7.3pp vs SP\",\n        \"sdgd_cal_fewnerd\": \"F1=0.381, Δ=-3.3pp vs SP\",\n        \"sdgd_cal_maven\": \"relF1=0.188, Δ=-5.3pp vs SP\",\n        \"sdgd_vs_random_significant\": false,\n        \"per_type_worst\": true,\n        \"verdict\": \"FAILED — all decomposition methods inferior to single-pass\"\n      },\n      \"recommended_paper_structure\": [\n        \"1. Introduction: 'What makes schemas complex for LLMs?'\",\n        \"2. Related Work: decomposition approaches + empirical studies\",\n        \"3. Experimental Setup: 3 tasks, 2 models, 2 embeddings\",\n        \"4. Finding 1: Pairwise confusability predicts type confusion (model-dependent)\",\n        \"5. Finding 2: Count and confusability act through distinguishable channels\",\n        \"6. Finding 3: Per-type aggregation introduces centrality confound\",\n        \"7. Finding 4: Confusability-minimizing decomposition fails (negative result)\",\n        \"8. Discussion: implications for future work\",\n        \"9. Conclusion\"\n      ],\n      \"recommended_venue\": \"EMNLP 2026 Findings (realistic), Main (stretch)\"\n    },\n    \"tables\": [\n      \"Table: Pairwise SCS-Confusion Signal (Cross-Task × Cross-Model × Cross-Embedding)\\n| Model  | Embedding | Few-NERD (NER) | MAVEN (ED) | FewRel (RE) |\\n|--------|-----------|----------------|------------|-------------|\\n| Qwen3  | Qwen3     | r=0.156***     | r=-0.009   | —           |\\n| Qwen3  | MiniLM    | —              | r=0.115*** | Δ=21-50pp*  |\\n| LLaMA  | Qwen3     | r=0.042        | —          | —           |\\n*** p<0.001, * pilot only\\n\",\n      \"Table: SDGD Full Comparison (worst tier)\\n| Method       | Few-NERD F1 | Δ vs SP | MAVEN relF1 | Δ vs SP |\\n|-------------|-------------|---------|-------------|---------|\\n| Single-pass  | 0.414       | —       | 0.241       | —       |\\n| SDGD-cal     | 0.381       | -3.3    | 0.188       | -5.3    |\\n| Random (=k)  | 0.374       | -4.0    | 0.180       | -6.1    |\\n| SDGD-zero    | 0.367       | -4.7    | 0.168       | -7.3    |\\n| Per-type     | 0.330       | -8.4    | 0.108       | -13.3   |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst tier 论文的核心卖点不是 positive findings 而是 systematic methodology 和 honest reporting。三个 takeaway：(1) confusability 信号存在但 model/embedding-dependent——未来工作不能假设 universal confusability measure； (2) per-type 聚合有 centrality confound——未来工作应使用 pairwise 分析； (3) confusability-minimizing decomposition 失败——LLM 需要 type co-presence 做 comparative reasoning，简单分离策略适得其反。这些 negative-but-informative results 加上 controlled experimental design 可以支撑一篇 Findings paper。\\n\\nWorst tier 总体图景：论文有两个可靠发现（pairwise confusability signal on Qwen3×FewNERD + MiniLM×MAVEN；centrality confound on MAVEN）和一系列 informative negative results（LLaMA 无信号、SDGD 全面失败、interaction 不显著）。叙事必须 从 \\\"we discover and exploit confusability\\\" 彻底转为 \\\"we systematically investigate schema complexity, finding that confusability effects are real but model-dependent, and that the intuitive decomposition strategy fails because LLMs need type co-presence for disambiguation\\\"。这种 \\\"honest empirical study with negative results\\\" 的论文在 EMNLP Findings 有先例（如 \\\"Do Prompt-Based Models Really Understand the Meaning of Their Prompts?\\\" ACL 2022），但需要极强的写作功力 和清晰的 takeaway。\\n\"\n  }\n]",
      "numLines": 634,
      "startLine": 1,
      "totalLines": 634
    }
  },
  "sourceToolAssistantUUID": "0bc9200d-5bae-4048-af03-971f6aeb153c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T12:16:18.842Z_

<details><summary>↩ Tool result · `toolu_015hLztxoUbubHXgfkxXjS84`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (3 conditions) — Revised per D012
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).
16	
17	## Story Spine — Revised per D012
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.
24	
25	- **Three-task validation**:
26	  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio
27	  - RE (FewRel, 80 relations, cross-domain): Extreme-batch accuracy gap Δ=21-50pp
28	  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)
29	
30	- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD."
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
41	- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).
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
52	- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)
53	- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)
54	- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
55	- Immune to type frequency confound (operates at type-pair level)
56	
57	**MAVEN (ED)** — MiniLM embeddings:
58	- Pearson r=+0.120 (p≈0, n=11026 type pairs)
59	- Nonzero-only Spearman ρ=+0.191 (p<0.001)
60	- Cross-task replication on same-domain schema
61	- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas
62	
63	### Tier 2: STRONG SECONDARY — FewRel Extreme-Batch Comparison
64	
65	Large effect size, cross-task (RE), intuitive demonstration:
66	- count_4: low-BCS 91.7% vs high-BCS 70.8% (Δ=-20.9pp)
67	- count_8: low-BCS 100% vs high-BCS 50.0% (Δ=-50.0pp)
68	- count_16: low-BCS 91.7% vs high-BCS 43.1% (Δ=-48.6pp)
69	- Effect increases with count — consistent with multi-channel model
70	- MiniLM embeddings; pending: Qwen3 formal study
71	
72	### Tier 3: SUPPORTING — Few-NERD Per-type Analysis
73	
74	Bridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:
75	- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings
76	- Partial r=-0.200 (p=0.116) controlling for log-frequency
77	- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)
78	- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)
79	- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal
80	
81	### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound
82	
83	Methodological case study on when aggregated confusability measures fail:
84	- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction
85	- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation
86	- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure
87	- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)
88	- This is stronger than "domain boundary" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition
89	
90	### Tier 5: MECHANISTIC — Error Taxonomy
91	
92	Confusion rate differential demonstrates the mechanism:
93	- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
94	- Random batches: 1.7-2.4x ratio (still significant, smaller effect)
95	- Type confusion errors increase with count AND with confusability (additive)
96	
97	## Embedding Ablation (D010)
98	
99	2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}
100	
101	### Per-type (Layer 2)
102	| | Few-NERD | FewRel | MAVEN |
103	|---|---|---|---|
104	| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |
105	| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |
106	
107	### Pairwise (Layer 1)
108	| | Few-NERD | MAVEN |
109	|---|---|---|
110	| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |
111	| MiniLM | — | r=+0.120 ✓ |
112	
113	**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.
114	
115	## Venue Fit Risks
116	
117	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024).
118	- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.
119	- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).
120	- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.
121	- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.
122	
123	## Anticipated Reviewer Concerns
124	
125	| Concern | Response Strategy | Experiment |
126	|---------|------------------|------------|
127	| Only one model | LLaMA-3.3-70B replication | exp-012 |
128	| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |
129	| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |
130	| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |
131	| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |
132	| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |
133	| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |
134	| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |
135	| Latency overhead | Report API calls and wall-clock time | exp-008 |
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17ea4f15-0450-4707-b182-932770fd0fbc",
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "98645f88-c44e-49e7-bb3c-dd70cfe6f50c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (3 conditions) — Revised per D012\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): Extreme-batch accuracy gap Δ=21-50pp\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)\n- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.120 (p≈0, n=11026 type pairs)\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Extreme-Batch Comparison\n\nLarge effect size, cross-task (RE), intuitive demonstration:\n- count_4: low-BCS 91.7% vs high-BCS 70.8% (Δ=-20.9pp)\n- count_8: low-BCS 100% vs high-BCS 50.0% (Δ=-50.0pp)\n- count_16: low-BCS 91.7% vs high-BCS 43.1% (Δ=-48.6pp)\n- Effect increases with count — consistent with multi-channel model\n- MiniLM embeddings; pending: Qwen3 formal study\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy\n\nConfusion rate differential demonstrates the mechanism:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n- Type confusion errors increase with count AND with confusability (additive)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.120 ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  },
  "sourceToolAssistantUUID": "17ea4f15-0450-4707-b182-932770fd0fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "6ff45298-2c29-4061-b9e1-1be46157b77b",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Assistant

_source line 14 · 2026-05-15T12:17:03.533Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and the paper framing. Let me now write the LaTeX paper according to the "worst" tier narrative guidance:

Key narrative direction:
- Completely abandon SDGD as a method contribution
- Reframe as a pure systematic empirical analysis
- Schema complexity is not one-dimensional — count and confusability degrade performance through orthogonal channels
- Confusability signal is highly dependent on model and embedding choice
- Pairwise confusability is more robust than per-type aggregation, but only significant in specific model×embedding×schema combinations
- Centrality confound is itself a methodological contribution


- Model-specific effects show that confusability patterns vary significantly across architectures like Qwen3 and LLaMA, which I'll frame as a key finding rather than a limitation
- The paper will follow a question-driven structure moving from controlled experiments to findings and their implications, with SDGD relegated to a negative result appendix

Now I need to systematically cover all seven experiments: the MAVEN and DocRED confusability studies, the count-confusability interaction, the error taxonomy binned by confusability scores, the LLaMA validation across models, and the two SDGD-zero ablations on Few-NERD and MAVEN.

For the remaining experiments—SDGD-cal variants, random batching ablation, per-type splitting comparison, embedding validation against empirical confusion, and the cross-experiment summary—I'll integrate these into the findings sections to show how different training approaches and data organization strategies either amplify or mitigate the confusability effect.

The paper will open with the core question about schema complexity, establish the experimental setup with tasks and metrics, then present findings progressively: first showing that pairwise confusability predicts type confusion in a model-dependent way, then demonstrating that count and confusability operate through distinct mechanisms, and finally synthesizing how these insights apply across different training paradigms. I'm mapping out where each experiment fits into the paper structure—most of the SDGD variants belong in an appendix as negative result case studies rather than core contributions, but I still need dedicated sections or tables for every experiment in the data file. Now I'm ready to start writing the full paper using a standard neuroscience conference format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98645f88-c44e-49e7-bb3c-dd70cfe6f50c",
  "isSidechain": false,
  "requestId": "req_011Cb4LbULDNWQfoByVvb4Uc",
  "type": "assistant",
  "uuid": "69d2c775-2a66-4589-b9a6-0a7d982f34ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EnNWAw8Y4EsK1gy6kjjUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23010,
      "cache_read_input_tokens": 23153,
      "output_tokens": 1146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1146,
          "cache_read_input_tokens": 23153,
          "cache_creation_input_tokens": 23010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23010
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

_source line 15 · 2026-05-15T12:17:03.535Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d2c775-2a66-4589-b9a6-0a7d982f34ea",
  "isSidechain": false,
  "requestId": "req_011Cb4LbULDNWQfoByVvb4Uc",
  "type": "assistant",
  "uuid": "5e4fb6e7-8445-4710-86e3-7058786407e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EnNWAw8Y4EsK1gy6kjjUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23010,
      "cache_read_input_tokens": 23153,
      "output_tokens": 1146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1146,
          "cache_read_input_tokens": 23153,
          "cache_creation_input_tokens": 23010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23010
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

_source line 16 · 2026-05-15T12:17:06.059Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AUpZkh7ZSoaeTHoq9HjdhM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4fb6e7-8445-4710-86e3-7058786407e6",
  "isSidechain": false,
  "requestId": "req_011Cb4LbULDNWQfoByVvb4Uc",
  "type": "assistant",
  "uuid": "8af9eb13-395e-42db-aa7e-32cd4946b09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EnNWAw8Y4EsK1gy6kjjUK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23010,
      "cache_read_input_tokens": 23153,
      "output_tokens": 1146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1146,
          "cache_read_input_tokens": 23153,
          "cache_creation_input_tokens": 23010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23010
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

_source line 17 · 2026-05-15T12:17:06.298Z_

<details><summary>↩ Tool result · `toolu_01AUpZkh7ZSoaeTHoq9HjdhM`</summary>

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
  "parentUuid": "8af9eb13-395e-42db-aa7e-32cd4946b09e",
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "101a217c-c2bf-4bb1-982e-c0322dbcc4d5",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8af9eb13-395e-42db-aa7e-32cd4946b09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T12:17:25.393Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper. I need to be very careful with the data — every number must come from experiment_data.json.

Let me plan the paper structure carefully:

**Main Paper:**
1. Abstract
2. Introduction
3. Related Work
4. Experimental Setup (tasks, models, embeddings, metrics)
5. Finding 1: Pairwise Confusability Predicts Type Confusion (Model- and Embedding-Dependent)
   - 5.1 Few-NERD (Qwen3): r=0.156
   - 5.2 MAVEN results showing weaker correlations across different models
   - 5.3 Cross-model comparisons revealing substantial variation in predictive power
   - 5.4 Validating the embedding proxy against empirical confusion patterns
6. Finding 2: Count and Confusability Degrade Through Distinguishable Channels
   - 6.1 Task-specific count trajectories with different degradation patterns
   - 6.2 Factorial analysis examining independent effects
   - 6.3 Categorizing error types to understand failure modes
7. Finding 3: Per-Type Aggregation Introduces Centrality Confound
   - 7.1 MAVEN showing consistent positive effects when split by entity type
   - 7.2 DocRED providing a null case that clarifies the boundary conditions
8. Finding 4: Confusability-Minimizing Decomposition Fails
   - Pointing to appendix for detailed evidence
9. Discussion
10. Conclusion

Appendix sections covering ablations and method comparisons...

I'm consolidating the SDGD experiments as a negative result case study in the appendix rather than giving them prominence in the main narrative, which lets me keep each experiment's results in its own table while maintaining a cleaner paper structure. I'll use standard LaTeX packages to ensure compatibility with pdflatex compilation.

Writing the full LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "101a217c-c2bf-4bb1-982e-c0322dbcc4d5",
  "isSidechain": false,
  "requestId": "req_011Cb4LeyTFtuorMSxYGZKG8",
  "type": "assistant",
  "uuid": "4dcbda3c-952a-49ad-bf17-e40bea4997fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqpcMAwx1An2PNxb5NkXZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 46163,
      "output_tokens": 16624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16624,
          "cache_read_input_tokens": 46163,
          "cache_creation_input_tokens": 1172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1172
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

_source line 19 · 2026-05-15T12:17:25.398Z_

Writing the paper now. This is a comprehensive LaTeX document covering all 12 experiments plus the cross-experiment summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dcbda3c-952a-49ad-bf17-e40bea4997fc",
  "isSidechain": false,
  "requestId": "req_011Cb4LeyTFtuorMSxYGZKG8",
  "type": "assistant",
  "uuid": "6c86d70f-44d4-4108-8d09-32c5ee53f6f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqpcMAwx1An2PNxb5NkXZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 46163,
      "output_tokens": 16624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16624,
          "cache_read_input_tokens": 46163,
          "cache_creation_input_tokens": 1172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1172
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

_source line 20 · 2026-05-15T12:21:53.973Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QFY34WMS3Jd84Pr24zfrWN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[numbers]{natbib}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\newcommand{\\ie}{i.e.}\n\\newcommand{\\eg}{e.g.}\n\\newcommand{\\cf}{cf.}\n\\newcommand{\\etal}{et~al.}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\n\\title{Is Schema Complexity One-Dimensional?\\\\A Controlled Empirical Study of Type Count, Confusability,\\\\and Their Interaction in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\n\nTraining-free LLM information extraction degrades severely on complex schemas, yet what makes a schema ``complex'' remains poorly understood.\nWe present the first controlled empirical study that disentangles two dimensions of schema complexity---\\emph{type count} and \\emph{type confusability}---across three IE tasks (NER, event detection, relation extraction), two LLM families (Qwen3-32B, LLaMA-3.3-70B), and two embedding spaces (Qwen3, MiniLM).\nOur findings reveal that schema complexity is not one-dimensional.\n(1)~Pairwise type confusability significantly predicts type confusion errors on certain model$\\times$embedding$\\times$task combinations ($r{=}0.156$, $p{<}10^{-11}$ for Qwen3 on Few-NERD; $r{=}0.115$, $p{<}10^{-42}$ for MiniLM on MAVEN), but the signal is highly model-dependent---LLaMA-3.3-70B shows no significant effect ($r{=}0.042$, $p{=}0.068$).\n(2)~Count and confusability degrade performance through distinguishable error channels: count drives entity omission (miss rate $0.28{\\to}0.55$), while confusability drives type substitution ($4.8{\\times}$ higher in high-confusability batches).\n(3)~Per-type confusability aggregation introduces a centrality confound in semantically homogeneous schemas, where pairwise analysis remains valid.\n(4)~Counter-intuitively, confusability-minimizing schema decomposition \\emph{harms} performance ($\\Delta{=}{-}3.3$ to ${-}7.3$ F\\textsubscript{1} vs.\\ single-pass), because type co-presence provides disambiguation context that outweighs confusion costs.\nThese findings establish that confusability effects are real but not universal, and that the intuitive ``separate confusable types'' strategy fails for LLMs that leverage comparative type reasoning.\n\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nTraining-free LLM information extraction---using instruction-tuned LLMs with in-context type definitions but no task-specific training---has emerged as a practical paradigm for rapid deployment.\nHowever, performance degrades sharply as schema complexity increases: schemas with $50{+}$ types can exhibit $20{-}60$ F\\textsubscript{1} gaps compared to supervised baselines.\n\nPrior work has addressed this degradation through schema decomposition: splitting large schemas into smaller batches for independent extraction.\nUniNER~\\cite{universal_ner_2024} uses per-type splitting, processing one type at a time.\nGoLLIE~\\cite{gollie_2024} provides type definitions as structured code.\nLLM-PEE~\\cite{llmpee_2024} implicitly leverages similarity-based grouping.\nYet none of these approaches validates the \\emph{assumption} that drives decomposition: what exactly makes schemas complex for LLMs, and does reducing a specific complexity dimension actually help?\n\nWe pose a precise question: \\textbf{Is schema complexity one-dimensional, or do distinct dimensions degrade LLM extraction through separable mechanisms?}\nConcretely, we isolate two candidate dimensions: \\emph{type count} (how many types the LLM must consider simultaneously) and \\emph{type confusability} (how semantically similar co-present types are).\nThrough controlled experiments across three IE tasks, two LLMs, and two embedding spaces, we find:\n\n\\begin{enumerate}[leftmargin=2em,itemsep=2pt]\n\\item \\textbf{Pairwise confusability predicts type confusion}, but the effect is model- and embedding-dependent.\nQwen3-32B on Few-NERD shows $r{=}0.156$ ($p{<}10^{-11}$); LLaMA-3.3-70B on the same task shows $r{=}0.042$ (not significant).\nNo single embedding universally captures confusability across tasks.\n\n\\item \\textbf{Count and confusability act through distinguishable channels}: count increases entity omission (recall degrades monotonically), while confusability increases type substitution errors ($4.8{\\times}$ ratio in extreme conditions).\nHowever, a formal $2{\\times}2$ interaction test is not significant ($p{=}0.582$), consistent with weak additive independence.\n\n\\item \\textbf{Per-type confusability aggregation is confounded} in semantically homogeneous schemas.\nOn MAVEN (168 FrameNet-derived event types), per-type mean confusability correlates \\emph{positively} with F\\textsubscript{1} ($\\rho{=}{+}0.195$), because central, well-represented types have high mean similarity but are also easier to extract.\nPairwise analysis avoids this confound.\n\n\\item \\textbf{Decomposition fails}: all confusability-minimizing decomposition strategies (SDGD-zero, SDGD-cal, per-type splitting) perform \\emph{worse} than single-pass extraction, because separating confusable types removes the disambiguation context that LLMs use for comparative type reasoning.\n\\end{enumerate}\n\nThese results establish schema complexity as a multi-dimensional phenomenon whose effects are contingent on model architecture, embedding choice, and schema structure.\nThe negative decomposition result is itself informative: it reveals that LLMs exploit type co-presence for disambiguation, a mechanism that simple separation strategies destroy.\n\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Training-free LLM IE.}\nRecent work has shown that instruction-tuned LLMs can perform IE tasks zero-shot by providing type definitions in the prompt~\\cite{universal_ner_2024,gollie_2024,llmpee_2024}.\nPerformance is competitive on simple schemas ($5{-}15$ types) but degrades substantially on complex ones.\n\n\\paragraph{Schema decomposition.}\nUniNER~\\cite{universal_ner_2024} processes one type at a time, achieving 3.3 F\\textsubscript{1} gains on some benchmarks but at $k{\\times}$ API cost.\nLLM-PEE~\\cite{llmpee_2024} groups types by embedding similarity, implicitly targeting confusability reduction.\nNeither approach validates whether the targeted complexity dimension is actually causal.\n\n\\paragraph{Schema complexity analysis.}\nThe relationship between label set complexity and extraction performance has been studied in supervised settings~\\cite{few_nerd_2021,maven_2020}, but controlled isolation of individual complexity dimensions in the LLM setting is unexplored.\nOur work fills this gap with factorial experimental designs.\n\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n% ============================================================\n\n\\subsection{Tasks and Datasets}\n\nWe study three IE tasks with varying schema characteristics:\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse domains. Cross-domain schema with heterogeneous type semantics.\n\\item \\textbf{MAVEN} (Event Detection): 168 event types derived from FrameNet. Same-domain schema with homogeneous type semantics.\n\\item \\textbf{DocRED} (Relation Extraction): 96 relation types. Document-level task where extraction involves cross-sentence reasoning.\n\\end{itemize}\n\n\\subsection{Models}\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Qwen3-32B-Instruct}: Primary extraction model. All experiments except the cross-model study use this model.\n\\item \\textbf{LLaMA-3.3-70B-Instruct}: Cross-model validation (Section~\\ref{sec:crossmodel}).\n\\end{itemize}\n\n\\subsection{Confusability Measures}\n\nWe compute \\emph{Schema Confusability Score} (SCS) as the cosine similarity between type definition embeddings:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\cos(\\mathbf{e}(t_i), \\mathbf{e}(t_j))\n\\end{equation}\nwhere $\\mathbf{e}(\\cdot)$ denotes the embedding function. We use two embedding models:\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Qwen3 embeddings}: Derived from the extraction model's own representations.\n\\item \\textbf{MiniLM}: A general-purpose sentence embedding model (all-MiniLM-L6-v2).\n\\end{itemize}\n\n\\emph{Pairwise confusability} uses SCS directly between type pairs.\n\\emph{Per-type confusability} (Batch Confusability Score, BCS) averages SCS across all co-present types:\n$\\text{BCS}(t_i) = \\frac{1}{|B|-1}\\sum_{t_j \\in B \\setminus \\{t_i\\}} \\text{SCS}(t_i, t_j)$.\n\n\\subsection{Evaluation Protocol}\n\nFor NER and event detection, we report both relaxed F\\textsubscript{1} (partial span matching) and exact F\\textsubscript{1}.\nWe use controlled batch construction: for each \\emph{count} level, we sample random subsets of types and evaluate extraction on held-out test data.\nWithin-count experiments vary confusability (BCS) while holding count fixed, isolating the confusability effect.\n\n\n% ============================================================\n\\section{Finding 1: Pairwise Confusability Predicts Type Confusion}\n\\label{sec:finding1}\n% ============================================================\n\nWe investigate whether pairwise type confusability (SCS between type pairs) predicts actual type confusion errors.\nWe test this across tasks, models, and embeddings.\n\n\\subsection{Few-NERD: Qwen3 Embeddings}\n\\label{sec:fewnerd_pairwise}\n\nOn Few-NERD with Qwen3-32B extraction and Qwen3 embeddings, pairwise SCS significantly correlates with pairwise confusion rate: Pearson $r{=}0.156$ ($p{=}4.6{\\times}10^{-12}$, $n{=}1{,}953$ type pairs).\nAmong type pairs with nonzero confusion, Spearman $\\rho{=}0.254$ ($p{=}1.1{\\times}10^{-6}$).\nHigh-SCS pairs such as \\texttt{person-other}$\\leftrightarrow$\\texttt{person-politician} (SCS$=$0.934) account for the majority of type confusion errors.\n\nIn extreme batches (deliberately constructed to maximize or minimize BCS), the confusion rate ratio reaches $10{-}28{\\times}$ between high- and low-confusability conditions.\nRandom batches show a smaller but consistent ratio of $1.7{-}2.4{\\times}$.\n\n\\subsection{MAVEN: Embedding-Dependent Signal}\n\\label{sec:maven_pairwise}\n\nMAVEN presents a contrasting pattern across embeddings (Table~\\ref{tab:pairwise_matrix}).\nWith MiniLM embeddings, the pairwise signal is significant: $r{=}0.115$ ($p{=}2.1{\\times}10^{-42}$, $n{=}14{,}028$ pairs), with Spearman $\\rho{=}0.128$ (nonzero-only $\\rho{=}0.185$).\nHowever, Qwen3 embeddings yield $r{=}{-}0.009$ ($p{=}0.38$)---completely non-significant.\n\nThis divergence reveals that confusability measurement is not embedding-agnostic.\nIn semantically homogeneous schemas (MAVEN's FrameNet-derived types), the extraction model's own embedding space may not differentiate confusable type pairs effectively, while a general-purpose embedding preserves discriminative structure.\n\n\\subsection{Cross-Model Validation: LLaMA-3.3-70B}\n\\label{sec:crossmodel}\n\nTo test whether confusability effects generalize across model families, we replicate the Few-NERD protocol with LLaMA-3.3-70B-Instruct.\nTable~\\ref{tab:crossmodel} presents the comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model comparison on Few-NERD. Confusability effects are substantially weaker for LLaMA-3.3-70B across all metrics.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3-32B} & \\textbf{LLaMA-3.3-70B} \\\\\n\\midrule\nBaseline \\fone{} (count 64) & 0.414 & 0.378 \\\\\nPairwise $r$ (Qwen3 embed) & 0.156*** & 0.042 (ns) \\\\\nPer-type $\\rho$ & $-$0.293* & $-$0.082 (ns) \\\\\nExtreme confusion ratio & 10--28$\\times$ & 2.1--2.5$\\times$ \\\\\nRandom confusion ratio & 1.7--2.4$\\times$ & 1.15--1.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLLaMA-3.3-70B shows no significant pairwise signal ($r{=}0.042$, $p{=}0.068$), no significant per-type correlation ($\\rho{=}{-}0.082$, $p{=}0.538$), and dramatically lower confusion rate ratios ($2.1{-}2.5{\\times}$ vs.\\ $10{-}28{\\times}$).\nEven controlling for log-frequency, the partial correlation remains non-significant (partial $r{=}{-}0.055$, $p{=}0.684$).\n\n\\begin{table}[t]\n\\centering\n\\caption{LLaMA-3.3-70B detailed statistics on Few-NERD. No analysis reaches significance.}\n\\label{tab:llama_detail}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Analysis} & \\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} & \\textbf{Verdict} \\\\\n\\midrule\nPairwise & Pearson $r$ & 0.042 & 0.068 & NS \\\\\nPairwise (nonzero) & Spearman $\\rho$ & 0.078 & 0.120 & NS \\\\\nPer-type & Spearman $\\rho$ & $-$0.082 & 0.538 & NS \\\\\nPer-type (partial) & Partial $r$ & $-$0.055 & 0.684 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis $4{\\times}$ effect size difference ($r{=}0.156$ vs.\\ $r{=}0.042$) across model families implies that confusability sensitivity is model-dependent.\nPrior conflicting findings about schema complexity effects may be partly explained by this model dependence.\n\n\\subsection{Embedding Proxy Validation}\n\\label{sec:scs_validation}\n\nTo assess whether embedding-based SCS is a valid proxy for actual model confusion, we compare SCS rankings against an empirical confusion matrix derived from calibration data (Table~\\ref{tab:scs_validation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Correlation between embedding SCS and empirical confusion rates. Both embeddings show weak predictive power.}\n\\label{tab:scs_validation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} & \\textbf{Kendall $\\tau$} & \\textbf{$p$} \\\\\n\\midrule\nQwen3 & 0.125 & 0.031 & 0.092 & 0.044 \\\\\nMiniLM & 0.098 & 0.082 & 0.071 & 0.115 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{SCS proxy error analysis: false positive/negative rates for confusion prediction.}\n\\label{tab:scs_errors}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3} & \\textbf{MiniLM} \\\\\n\\midrule\nFalse Positive Rate & 0.42 & 0.48 \\\\\nFalse Negative Rate & 0.35 & 0.40 \\\\\nTop-1 Match & Yes & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3 SCS achieves $\\rho{=}0.125$ ($p{=}0.031$) against empirical confusion---statistically significant but explaining only ${\\sim}1.6\\%$ of confusion variance.\nThe false positive rate of $0.42$ indicates that $42\\%$ of type pairs predicted as confusable by SCS are not actually confused by the model.\nConfusability is mediated by factors beyond semantic similarity, including surface form similarity, type definition wording, and in-context position.\n\n\\subsection{Summary: Pairwise Signal Matrix}\n\nTable~\\ref{tab:pairwise_matrix} summarizes the full cross-task $\\times$ cross-model $\\times$ cross-embedding matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise SCS--confusion signal across tasks, models, and embeddings. Only 3 of 7 tested cells reach significance; no single embedding or model universally works.}\n\\label{tab:pairwise_matrix}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Embedding} & \\textbf{Few-NERD} & \\textbf{MAVEN} & \\textbf{DocRED} \\\\\n\\midrule\nQwen3 & Qwen3 & $r{=}0.156$*** & $r{=}{-}0.009$ & --- \\\\\nQwen3 & MiniLM & --- & $r{=}0.115$*** & --- \\\\\nLLaMA & Qwen3 & $r{=}0.042$ & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize *** $p<0.001$. Cells marked ``---'' were not tested.}\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n\\section{Finding 2: Count and Confusability Degrade Through Distinguishable Channels}\n\\label{sec:finding2}\n% ============================================================\n\n\\subsection{Count Curves Across Tasks}\n\\label{sec:count_curves}\n\nWe construct count curves by varying the number of types presented to the LLM while holding other factors constant.\nThe three tasks show strikingly different patterns:\n\n\\paragraph{Few-NERD.}\nRelaxed \\fone{} decreases monotonically with count (previously established), with recall declining as the primary driver.\n\n\\paragraph{MAVEN.}\nTable~\\ref{tab:maven_count} shows the \\emph{opposite} pattern: relaxed \\fone{} \\emph{increases} with count, from $0.098$ (count 1) to $0.243$ (count 100).\nRecall increases monotonically ($0.07{\\to}0.19$), while precision is roughly flat ($0.15{-}0.40$).\nThis reversal occurs because MAVEN's 168 FrameNet-derived types form a coherent ontology; more types in the prompt provide richer event taxonomy context that helps the model locate each type's position in the hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN count curve (500 samples, relaxed matching). Performance \\emph{increases} with type count---opposite of Few-NERD.}\n\\label{tab:maven_count}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{Count} & \\textbf{Relaxed \\fone{}} & \\textbf{Exact \\fone{}} & \\textbf{Recall} & \\textbf{Precision} & \\textbf{Pred/Gold} \\\\\n\\midrule\n1  & 0.098 & 0.008 & 0.070 & 0.162 & 0.43 \\\\\n6  & 0.112 & 0.005 & 0.085 & 0.165 & 0.52 \\\\\n12 & 0.155 & 0.011 & 0.118 & 0.226 & 0.52 \\\\\n22 & 0.192 & 0.016 & 0.148 & 0.274 & 0.54 \\\\\n44 & 0.238 & 0.021 & 0.180 & 0.350 & 0.51 \\\\\n64 & 0.241 & 0.018 & 0.182 & 0.358 & 0.51 \\\\\n100 & 0.243 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED.}\nTable~\\ref{tab:docred_count} shows an approximately flat count curve with no clear monotonic pattern.\n\\fone{} ranges from $0.185$ (count 4) to $0.208$ (count 48), with a slight decline at the full schema (count 96, \\fone{}$=$0.195).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED count curve (document-level RE). Performance is near-flat---schema complexity effects are dominated by cross-sentence reasoning demands.}\n\\label{tab:docred_count}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Count} & \\textbf{\\fone{}} & \\textbf{Recall} & \\textbf{Precision} & \\textbf{Confusion Rate} \\\\\n\\midrule\n4  & 0.185 & 0.145 & 0.256 & 0.008 \\\\\n8  & 0.192 & 0.152 & 0.261 & 0.012 \\\\\n16 & 0.198 & 0.158 & 0.264 & 0.015 \\\\\n32 & 0.203 & 0.165 & 0.258 & 0.018 \\\\\n48 & 0.208 & 0.170 & 0.261 & 0.019 \\\\\n96 & 0.195 & 0.160 & 0.250 & 0.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-task comparison reveals that count effects are task-dependent: monotonically negative (Few-NERD), monotonically positive (MAVEN), or negligible (DocRED).\n\n\\subsection{Within-Count BCS--\\fone{} Correlation}\n\\label{sec:within_count}\n\nTo isolate confusability from count, we examine the correlation between batch-level BCS and \\fone{} \\emph{within} fixed count levels.\n\n\\paragraph{MAVEN.} Table~\\ref{tab:maven_within_count} shows no significant within-count BCS--\\fone{} correlation, with both individual count levels and the pooled analysis failing to reach significance.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN within-count BCS--\\fone{} correlation. No significant relationship detected at any count level.}\n\\label{tab:maven_within_count}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Count} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Direction} & \\textbf{Verdict} \\\\\n\\midrule\n6  & $+$0.175 & 0.185 & Positive & Fail \\\\\n12 & $+$0.124 & 0.315 & Positive & Fail \\\\\nPooled & $+$0.142 & 0.108 & Positive & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe positive direction (higher BCS $\\to$ higher \\fone{}) is opposite to the confusability hypothesis and consistent with centrality confounding (Section~\\ref{sec:finding3}).\n\n\\paragraph{DocRED.} Within-count BCS--\\fone{} correlations are similarly non-significant: count 8 ($r{=}0.032$, $p{=}0.62$), count 16 ($r{=}{-}0.058$, $p{=}0.48$), pooled ($r{=}{-}0.015$, $p{=}0.84$).\nThe per-type BCS--\\fone{} correlation is also null ($\\rho{=}{-}0.04$, $p{=}0.72$).\n\n\\subsection{2$\\times$2 Factorial Design: Count $\\times$ Confusability Interaction}\n\\label{sec:factorial}\n\nWe test the interaction between count and confusability using a $2{\\times}2$ factorial design on Few-NERD: \\{low count$=$6, high count$=$22\\} $\\times$ \\{low BCS, high BCS\\}, with 12 batches per cell ($n{=}48$ total).\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ cell means (\\fone{}, text match) on Few-NERD. Both factors show directional effects, but the interaction is not significant.}\n\\label{tab:factorial_means}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\n\\midrule\nLow Count (6)  & 0.348 & 0.312 & $\\Delta{=}{-}0.036$ \\\\\nHigh Count (22) & 0.298 & 0.255 & $\\Delta{=}{-}0.043$ \\\\\n\\midrule\nCount Effect & $\\Delta{=}{-}0.050$ & $\\Delta{=}{-}0.057$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-way ANOVA results. Count is significant; BCS is marginal; the interaction is not significant.}\n\\label{tab:anova}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Source} & \\textbf{$F$} & \\textbf{$p$} & \\textbf{$\\eta^2$} & \\textbf{Verdict} \\\\\n\\midrule\nCount       & 7.82 & 0.008 & 0.14  & Significant \\\\\nBCS         & 2.93 & 0.094 & 0.06  & Marginal \\\\\nCount$\\times$BCS & 0.31 & 0.582 & 0.006 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe count main effect is significant ($F{=}7.82$, $p{=}0.008$, $\\eta^2{=}0.14$), while BCS is marginal ($F{=}2.93$, $p{=}0.094$, $\\eta^2{=}0.06$).\nThe interaction is not significant ($F{=}0.31$, $p{=}0.582$, $\\eta^2{=}0.006$), consistent with an additive (rather than multiplicative) combination of the two channels.\nSimple effects analysis shows that BCS effects are directionally consistent at both count levels but neither reaches significance individually (low count: $\\Delta{=}{-}0.036$, $p{=}0.22$; high count: $\\Delta{=}{-}0.043$, $p{=}0.18$).\n\n\n\\subsection{Error Taxonomy: Mechanistic Evidence for Distinct Channels}\n\\label{sec:error_taxonomy}\n\nWe perform a systematic error classification on Few-NERD extraction outputs, categorizing false positives into four types: type substitution, boundary error, spurious extraction, and missed entity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall error distribution. Spurious extraction dominates; type substitution (the channel most related to confusability) accounts for only 18\\%.}\n\\label{tab:error_dist}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Proportion} & \\textbf{Primary Driver} \\\\\n\\midrule\nSpurious Extraction & 45\\% & Prompt format \\\\\nMissed Entity       & 25\\% & Count (recall) \\\\\nType Substitution   & 18\\% & BCS (confusability) \\\\\nBoundary Error      & 12\\% & Span detection \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Type substitution by confusability.}\nIn extreme high-BCS batches, the type substitution rate reaches $0.058$, compared to $0.012$ in extreme low-BCS batches---a $4.8{\\times}$ ratio (Table~\\ref{tab:type_sub_bcs}).\nHowever, in \\emph{random} batches, the ratio drops to $1.5{\\times}$ ($0.022$ vs.\\ $0.015$), indicating that the effect is pronounced only under deliberately extreme conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Type substitution rate by BCS condition. The extreme ratio (4.8$\\times$) substantially exceeds the random ratio (1.5$\\times$).}\n\\label{tab:type_sub_bcs}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{High BCS} & \\textbf{Low BCS} & \\textbf{Ratio} \\\\\n\\midrule\nExtreme Batch & 0.058 & 0.012 & 4.8$\\times$ \\\\\nRandom Batch  & 0.022 & 0.015 & 1.5$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Missed entities by count.}\nThe miss rate increases monotonically with count: $0.28$ (count 6) $\\to$ $0.42$ (count 22) $\\to$ $0.55$ (count 64).\nCrucially, the miss rate does \\emph{not} vary with BCS (high BCS: $0.40$; low BCS: $0.38$; ratio $1.05$), confirming that count and confusability affect different error modes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Missed entity rate by count. Monotonically increasing, independent of BCS.}\n\\label{tab:miss_count}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Count} & \\textbf{Miss Rate} & \\textbf{$\\Delta$ vs.\\ Count 6} \\\\\n\\midrule\n6  & 0.28 & --- \\\\\n22 & 0.42 & $+$0.14 \\\\\n64 & 0.55 & $+$0.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Boundary errors and hallucination.}\nNeither boundary errors (high BCS: $0.041$; low BCS: $0.038$; ratio $1.08$) nor hallucination (rate $0.03$, no BCS effect) are influenced by confusability, as expected---these error modes are orthogonal to type semantics.\n\n\n% ============================================================\n\\section{Finding 3: Per-Type Aggregation Introduces Centrality Confound}\n\\label{sec:finding3}\n% ============================================================\n\n\\subsection{MAVEN: Positive Per-Type Correlation}\n\nOn MAVEN, per-type mean BCS correlates \\emph{positively} with per-type \\fone{} under both embeddings (Table~\\ref{tab:maven_pertype}).\nThis is the \\emph{opposite} of what the confusability hypothesis predicts.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN pairwise and per-type confusability analysis. Per-type correlations are positive (confounded); pairwise MiniLM is significant.}\n\\label{tab:maven_pertype}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Pairwise $r$ ($p$)} & \\textbf{Per-type $\\rho$ ($p$)} \\\\\n\\midrule\nQwen3  & $-$0.009 (0.38) & $+$0.195 (0.018) \\\\\nMiniLM & $+$0.115 ($2.1{\\times}10^{-42}$) & $+$0.212 (0.009) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is \\emph{centrality confounding}: in MAVEN's semantically homogeneous schema, types with high mean BCS are central, frequent types (e.g., \\textsc{Attack}, \\textsc{Movement}) that the LLM extracts well because they are well-represented in training data and have clear definitions.\nMean BCS conflates confusability with type centrality; per-type aggregation cannot separate these effects.\n\nCrucially, the pairwise analysis tells a different story.\nMiniLM pairwise SCS significantly predicts confusion ($r{=}0.115$, $p{<}10^{-42}$), demonstrating that pairwise analysis avoids the centrality confound.\nThe Qwen3 pairwise signal is null ($r{=}{-}0.009$), highlighting that embedding choice interacts with schema structure.\n\nThe confusion rate analysis further supports this: MAVEN's extreme confusion ratios ($5.8{\\times}$ at count 6, $4.2{\\times}$ at count 12) are lower than Few-NERD's ($10{-}28{\\times}$), while random ratios ($1.4{\\times}$, $1.3{\\times}$) are modest.\n\n\\subsection{DocRED: Null Result as Boundary Condition}\n\nDocRED yields complete null results across all confusability analyses (Section~\\ref{sec:within_count}).\nThe pairwise signal is non-significant for both Qwen3 ($r{=}0.023$, $p{=}0.14$) and MiniLM ($r{=}0.031$, $p{=}0.08$).\nThe per-type BCS--\\fone{} correlation is null ($\\rho{=}{-}0.04$, $p{=}0.72$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED pairwise confusability analysis. No significant signal detected with either embedding.}\n\\label{tab:docred_pairwise}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Pearson $r$} & \\textbf{$p$} & \\textbf{$n$ pairs} & \\textbf{Verdict} \\\\\n\\midrule\nQwen3  & 0.023 & 0.14 & 4,560 & NS \\\\\nMiniLM & 0.031 & 0.08 & 4,560 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis null result establishes a boundary condition: confusability effects require that type definitions occupy a significant fraction of the prompt.\nIn document-level RE, the document content dominates the prompt; type definitions are a small fraction, and performance bottlenecks lie in cross-sentence reasoning and entity pair combinatorics rather than type confusability.\n\n\n% ============================================================\n\\section{Finding 4: Confusability-Minimizing Decomposition Fails}\n\\label{sec:finding4}\n% ============================================================\n\nMotivated by the confusability signal in Section~\\ref{sec:finding1}, we tested whether separating confusable types into different batches (Schema DAG Decomposition, SDGD) could improve extraction.\nWe report a comprehensive negative result: all decomposition strategies perform worse than single-pass extraction.\nFull details and per-batch breakdowns are in Appendix~\\ref{app:sdgd}.\n\n\\subsection{Overview of Methods}\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Single-pass}: All types in one prompt.\n\\item \\textbf{SDGD-zero}: Graph coloring on the SCS-thresholded pairwise similarity graph (no calibration data).\n\\item \\textbf{SDGD-cal}: Graph coloring on an empirical confusion matrix from 8--10 calibration samples.\n\\item \\textbf{Random ($k$)}: Random batching with the same number of batches as SDGD.\n\\item \\textbf{Per-type}: One type per batch (UniNER-style).\n\\end{itemize}\n\n\\subsection{Results}\n\nTable~\\ref{tab:sdgd_main} presents the full comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full method comparison. All decomposition methods are inferior to single-pass. Ordering: single-pass $>$ SDGD-cal $\\gtrsim$ random $\\gtrsim$ SDGD-zero $>$ per-type. Methods are sorted by Few-NERD \\fone{}.}\n\\label{tab:sdgd_main}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\multicolumn{3}{c}{\\textbf{Few-NERD}} & \\multicolumn{2}{c}{\\textbf{MAVEN}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & \\fone{} & Prec. & Recall & Rel.\\ \\fone{} & API \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 0.241 & 1$\\times$ \\\\\nSDGD-cal    & 0.381 & 0.342 & 0.430 & 0.188 & 7--12$\\times$ \\\\\nRandom      & 0.374 & 0.335 & 0.425 & 0.180 & 8--12$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 0.168 & 8--15$\\times$ \\\\\nPer-type    & 0.330 & 0.225 & 0.620 & 0.108 & 66--168$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe consistent pattern across both tasks: decomposition increases recall (each batch focuses on fewer types, enabling more aggressive extraction) but devastates precision (without the full type set, the model cannot disambiguate, leading to massive over-extraction).\nThe precision--recall tradeoff is unfavorable: precision losses far exceed recall gains.\n\n\\paragraph{SDGD vs.\\ random is not significant.}\nSDGD-zero does not outperform random batching on either task (Few-NERD: $\\Delta{=}{-}0.7$pp, $p{=}0.68$; MAVEN: $\\Delta{=}{-}1.2$pp, $p{=}0.42$).\nConfusability-aware grouping provides no value over random partitioning.\n\n\\paragraph{Per-type splitting is worst.}\nThe extreme decomposition---one type per batch---yields the lowest \\fone{} (Few-NERD: $0.330$; MAVEN: $0.108$) at the highest cost ($66{-}168{\\times}$ API calls).\nThis confirms that decomposition granularity is inversely related to performance.\n\n\\paragraph{Root cause.}\nDecomposition removes \\emph{disambiguation context}: when confusable types are separated, each batch sees only one side of a confusable pair, and the model assigns the available type to any plausible mention.\nUpon merging batches, the same span may receive conflicting type assignments ($8\\%$ cross-batch span overlap), and the overall prediction count far exceeds gold annotations (pred/gold ratio $1.36$ vs.\\ single-pass $0.47$).\n\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Schema complexity is multi-dimensional but context-dependent.}\nOur results establish that count and confusability are distinguishable dimensions of schema complexity, but their effects are contingent on task structure, model architecture, and embedding choice.\nOn Few-NERD (cross-domain NER), count dominates; on MAVEN (same-domain ED), more types \\emph{help}; on DocRED (document-level RE), neither dimension matters.\n\n\\paragraph{Confusability effects are real but not universal.}\nThe pairwise confusability signal is significant for Qwen3 on Few-NERD and MiniLM on MAVEN, but absent for LLaMA-3.3-70B and for Qwen3 embeddings on MAVEN.\nThis model dependence suggests that confusability sensitivity is a property of the model's internal representation, not solely of the schema itself.\nThe $4{\\times}$ effect size difference between Qwen3 ($r{=}0.156$) and LLaMA ($r{=}0.042$) is itself a finding that may explain prior conflicting reports about schema complexity effects.\n\n\\paragraph{Per-type aggregation is unreliable.}\nThe centrality confound on MAVEN demonstrates that mean BCS (per-type averaged confusability) is not a valid measure in semantically homogeneous schemas.\nFuture work on schema complexity should use pairwise analysis to avoid this confound, or use empirical confusion matrices that bypass embedding proxy limitations.\n\n\\paragraph{Decomposition harms LLM IE.}\nThe most counter-intuitive finding is that confusability-minimizing decomposition \\emph{hurts} performance.\nLLMs use type co-presence for comparative reasoning: seeing confusable types together enables the model to reason about their distinctions.\nRemoving this context forces the model into uninformed guessing.\nThis insight has direct implications for decomposition-based approaches: they should be designed to \\emph{preserve} disambiguation context rather than minimize confusability.\n\n\\paragraph{Implications for future work.}\n(1)~Confusability-based methods should be evaluated per-model, not assumed universal.\n(2)~Schema decomposition for LLM IE needs fundamentally different principles---perhaps preserving confusable types together while reducing only the non-informative count overhead.\n(3)~Embedding-based confusability proxies need task-specific calibration, as no single embedding works universally.\n\n\\paragraph{Limitations.}\nOur study uses two LLM families; more models are needed to characterize the distribution of confusability sensitivity.\nThe $2{\\times}2$ factorial design has limited statistical power ($n{=}48$); larger-scale factorial experiments could detect smaller interaction effects.\nDocRED results may partly reflect the difficulty of zero-shot document-level RE rather than a true absence of confusability effects.\n\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe presented the first controlled empirical study isolating type count and type confusability as dimensions of schema complexity in training-free LLM information extraction.\nOur experiments across three IE tasks, two LLMs, and two embedding spaces reveal that:\n(1)~pairwise type confusability is a valid predictor of type confusion errors, but only for specific model$\\times$embedding combinations;\n(2)~count and confusability degrade performance through distinguishable error channels;\n(3)~per-type confusability aggregation introduces centrality confounds in homogeneous schemas; and\n(4)~confusability-minimizing decomposition is counter-productive because LLMs leverage type co-presence for disambiguation.\nThese findings reframe schema complexity as a multi-dimensional, model-dependent phenomenon and provide methodological guidance for future research on LLM IE with complex schemas.\n\n\n% ============================================================\n\\appendix\n\\section{SDGD Decomposition: Detailed Results}\n\\label{app:sdgd}\n% ============================================================\n\nThis appendix provides detailed results for all decomposition experiments, which are reported as negative results in the main paper (Section~\\ref{sec:finding4}).\n\n\\subsection{SDGD-zero on Few-NERD}\n\\label{app:sdgd_zero_fewnerd}\n\nGraph coloring on the Qwen3 SCS-thresholded graph ($\\tau{=}0.847$) produces 8 batches (avg.\\ size $8.25$, range $4{-}12$).\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero vs.\\ single-pass on Few-NERD (66 types).}\n\\label{tab:sdgd_zero_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{Pred/Gold} & \\textbf{API} \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 0.47 & 1$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 1.36 & 8$\\times$ \\\\\n$\\Delta$    & $-$4.7pp & $-$33.0pp & $+$13.0pp & $+$0.89 & $+$7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero per-batch breakdown (top 4 batches, Few-NERD).}\n\\label{tab:sdgd_zero_perbatch}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{Batch} & \\textbf{Types} & \\textbf{Avg BCS} & \\textbf{\\fone{}} & \\textbf{Recall} & \\textbf{Precision} \\\\\n\\midrule\n0 & 12 & 0.812 & 0.42 & 0.48 & 0.38 \\\\\n1 & 10 & 0.795 & 0.38 & 0.45 & 0.33 \\\\\n2 & 9  & 0.780 & 0.35 & 0.42 & 0.30 \\\\\n3 & 8  & 0.763 & 0.32 & 0.40 & 0.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGraph statistics: 142 edges, edge density $0.066$, chromatic number 8, max intra-batch BCS $0.842$.\nCross-batch span overlap: $8\\%$ of predictions appear in multiple batches.\nTotal predictions: $4{,}850$ (after dedup: $4{,}120$), averaging $8.2$ predictions per sample vs.\\ $5.9$ gold entities.\n\n\\subsection{SDGD-zero on MAVEN}\n\\label{app:sdgd_zero_maven}\n\nOn MAVEN (168 types), adaptive threshold $\\tau{=}0.319$ produces 15 batches (avg.\\ size $11.2$, range $5{-}18$), with edge density $0.132$ and $1{,}850$ edges.\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero vs.\\ single-pass on MAVEN (168 types, relaxed matching).}\n\\label{tab:sdgd_zero_maven}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{Exact \\fone{}} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.241 & 0.018 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-zero   & 0.168 & 0.012 & 15$\\times$ & 12.8$\\times$ \\\\\n$\\Delta$    & $-$7.3pp & $-$0.6pp & $+$14$\\times$ & $+$11.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe larger performance gap on MAVEN ($-$7.3pp vs.\\ $-$4.7pp on Few-NERD) is consistent with MAVEN's positive count curve: decomposition directly counteracts the benefit of full ontology visibility.\n\n\\subsection{SDGD-cal on Few-NERD}\n\\label{app:sdgd_cal_fewnerd}\n\nSDGD-cal uses 8 calibration samples to build an empirical confusion matrix, yielding 85 nonzero confusion pairs.\nThe empirical confusion matrix correlates weakly with embedding SCS ($\\rho{=}0.125$, $p{=}0.031$).\nGraph coloring produces 7 batches (avg.\\ size $9.4$).\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on Few-NERD.}\n\\label{tab:sdgd_cal_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{$\\Delta$ vs.\\ SP} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{API} \\\\\n\\midrule\nSingle-pass & 0.414 & --- & 0.648 & 0.304 & 1$\\times$ \\\\\nRandom ($k{=}8$) & 0.374 & $-$4.0 & 0.335 & 0.425 & 8$\\times$ \\\\\nSDGD-zero   & 0.367 & $-$4.7 & 0.318 & 0.434 & 8$\\times$ \\\\\nSDGD-cal    & 0.381 & $-$3.3 & 0.342 & 0.430 & 7$\\times$ $+$ 8 cal. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal marginally outperforms SDGD-zero ($+$1.4pp) and random ($+$0.7pp, $p{=}0.58$), but the improvement over random is not significant.\nEven with empirical confusion data, the decomposition penalty persists.\n\n\\subsection{SDGD-cal on MAVEN}\n\\label{app:sdgd_cal_maven}\n\nOn MAVEN, 10 calibration samples produce 210 nonzero confusion pairs.\nGraph coloring yields 12 batches (avg.\\ size $14.0$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Full comparison on MAVEN (168 types, relaxed matching).}\n\\label{tab:sdgd_cal_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{$\\Delta$ vs.\\ SP} & \\textbf{API} \\\\\n\\midrule\nSingle-pass  & 0.241 & --- & 1$\\times$ \\\\\nRandom ($k{=}12$) & 0.180 & $-$6.1 & 12$\\times$ \\\\\nSDGD-zero    & 0.168 & $-$7.3 & 15$\\times$ \\\\\nSDGD-cal     & 0.188 & $-$5.3 & 12$\\times$ $+$ 10 cal. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal outperforms SDGD-zero ($+$2.0pp) but not random ($+$0.8pp, $p{=}0.62$).\nThe same pattern as Few-NERD: calibration helps marginally, but decomposition remains inferior to single-pass.\n\n\\subsection{Random Batching Ablation}\n\\label{app:random}\n\nTo isolate the contribution of confusability-aware grouping from the batch count reduction effect, we compare SDGD-zero against random batching with the same number of batches.\n\n\\begin{table}[h]\n\\centering\n\\caption{Random vs.\\ SDGD-zero on Few-NERD ($k{=}8$, 10 random seeds).}\n\\label{tab:random_fewnerd}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean \\fone{}} & \\textbf{Std} & \\textbf{Range} & \\textbf{vs.\\ SP} \\\\\n\\midrule\nRandom$\\times$10 & 0.374 & 0.018 & [0.348, 0.402] & $-$4.0pp \\\\\nSDGD-zero & 0.367 & --- & --- & $-$4.7pp \\\\\n$\\Delta$ (SDGD$-$Random) & \\multicolumn{4}{c}{$-$0.7pp, $p{=}0.68$ (NS)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Random vs.\\ SDGD-zero on MAVEN.}\n\\label{tab:random_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{vs.\\ SP} & \\textbf{$p$ (paired)} \\\\\n\\midrule\nRandom$\\times$5 & 0.180 & $-$6.1pp & --- \\\\\nSDGD-zero & 0.168 & $-$7.3pp & --- \\\\\n$\\Delta$ & \\multicolumn{3}{c}{$-$1.2pp, $p{=}0.42$ (NS)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn both tasks, SDGD-zero does not significantly outperform random batching, confirming that confusability-aware grouping provides no measurable benefit.\nSDGD-zero may actually perform slightly \\emph{worse} than random, because deliberately separating confusable types removes same-cluster disambiguation anchors that random batching occasionally preserves.\n\n\\subsection{Per-Type Splitting Ablation}\n\\label{app:pertype}\n\nPer-type splitting (one type per batch) represents the extreme of decomposition---maximum confusability elimination but also maximum loss of disambiguation context.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-type splitting vs.\\ all methods on Few-NERD.}\n\\label{tab:pertype_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-cal    & 0.381 & 0.342 & 0.430 & 7$\\times$ & 5.5$\\times$ \\\\\nRandom ($k{=}8$) & 0.374 & 0.335 & 0.425 & 8$\\times$ & 6.5$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 8$\\times$ & 6.5$\\times$ \\\\\nPer-type    & 0.330 & 0.225 & 0.620 & 66$\\times$ & 48$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-type splitting vs.\\ all methods on MAVEN (relaxed matching).}\n\\label{tab:pertype_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.241 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-cal    & 0.188 & 12$\\times$ & 10$\\times$ \\\\\nRandom      & 0.180 & 12$\\times$ & 10$\\times$ \\\\\nSDGD-zero   & 0.168 & 15$\\times$ & 12.8$\\times$ \\\\\nPer-type    & 0.108 & 168$\\times$ & 135$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe method ordering is consistent across both tasks: single-pass $>$ SDGD-cal $\\gtrsim$ random $\\gtrsim$ SDGD-zero $>$ per-type.\nDecomposition granularity is inversely correlated with \\fone{}: larger batches (more type context) consistently outperform smaller ones.\nPer-type splitting achieves the highest recall (0.620 on Few-NERD) through aggressive per-type extraction, but precision collapses (0.225) as each batch drastically over-extracts.\n\n% ============================================================\n% References\n% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem{universal_ner_2024}\nW.~Zhou, S.~Zhang, Y.~Gu, M.~Chen, and H.~Peng.\n\\newblock Universal{NER}: Targeted distillation from large language models for open named entity recognition.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{gollie_2024}\nO.~Sainz, I.~Garc{\\'i}a-Ferrero, R.~Agerri, O.~L{\\'o}pez~de~Lacalle, G.~Rigau, and E.~Agirre.\n\\newblock Go{LLIE}: Annotation guidelines improve zero-shot information extraction.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{llmpee_2024}\nG.~Zaratiana, N.~Tomeh, P.~Holat, and T.~Charnois.\n\\newblock {LLM-PEE}: Prompt-based extraction with embedding similarity for entity extraction using large language models.\n\\newblock \\emph{arXiv preprint arXiv:2312.15805}, 2024.\n\n\\bibitem{few_nerd_2021}\nN.~Ding, G.~Xu, Y.~Chen, X.~Wang, X.~Han, P.~Xie, H.~Zheng, and Z.~Liu.\n\\newblock Few-{NERD}: A few-shot named entity recognition dataset.\n\\newblock In \\emph{Proc.\\ ACL-IJCNLP}, 2021.\n\n\\bibitem{maven_2020}\nX.~Wang, Z.~Wang, X.~Han, W.~Jiang, R.~Han, Z.~Liu, J.~Li, P.~Li, Y.~Lin, and J.~Zhou.\n\\newblock {MAVEN}: A massive general domain event detection dataset.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2020.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c86d70f-44d4-4108-8d09-32c5ee53f6f2",
  "isSidechain": false,
  "requestId": "req_011Cb4LeyTFtuorMSxYGZKG8",
  "type": "assistant",
  "uuid": "29af7aa0-52dd-4eae-a7b5-6fcc3fa6b60f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqpcMAwx1An2PNxb5NkXZy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 46163,
      "output_tokens": 16624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16624,
          "cache_read_input_tokens": 46163,
          "cache_creation_input_tokens": 1172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1172
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

_source line 21 · 2026-05-15T12:21:54.005Z_

<details><summary>↩ Tool result · `toolu_01QFY34WMS3Jd84Pr24zfrWN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29af7aa0-52dd-4eae-a7b5-6fcc3fa6b60f",
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "8812f519-c413-4a0e-b398-cd045c2b8e11",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[numbers]{natbib}\n\n\\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}\n\n\\newcommand{\\ie}{i.e.}\n\\newcommand{\\eg}{e.g.}\n\\newcommand{\\cf}{cf.}\n\\newcommand{\\etal}{et~al.}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\n\\title{Is Schema Complexity One-Dimensional?\\\\A Controlled Empirical Study of Type Count, Confusability,\\\\and Their Interaction in Training-Free LLM Information Extraction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\n\nTraining-free LLM information extraction degrades severely on complex schemas, yet what makes a schema ``complex'' remains poorly understood.\nWe present the first controlled empirical study that disentangles two dimensions of schema complexity---\\emph{type count} and \\emph{type confusability}---across three IE tasks (NER, event detection, relation extraction), two LLM families (Qwen3-32B, LLaMA-3.3-70B), and two embedding spaces (Qwen3, MiniLM).\nOur findings reveal that schema complexity is not one-dimensional.\n(1)~Pairwise type confusability significantly predicts type confusion errors on certain model$\\times$embedding$\\times$task combinations ($r{=}0.156$, $p{<}10^{-11}$ for Qwen3 on Few-NERD; $r{=}0.115$, $p{<}10^{-42}$ for MiniLM on MAVEN), but the signal is highly model-dependent---LLaMA-3.3-70B shows no significant effect ($r{=}0.042$, $p{=}0.068$).\n(2)~Count and confusability degrade performance through distinguishable error channels: count drives entity omission (miss rate $0.28{\\to}0.55$), while confusability drives type substitution ($4.8{\\times}$ higher in high-confusability batches).\n(3)~Per-type confusability aggregation introduces a centrality confound in semantically homogeneous schemas, where pairwise analysis remains valid.\n(4)~Counter-intuitively, confusability-minimizing schema decomposition \\emph{harms} performance ($\\Delta{=}{-}3.3$ to ${-}7.3$ F\\textsubscript{1} vs.\\ single-pass), because type co-presence provides disambiguation context that outweighs confusion costs.\nThese findings establish that confusability effects are real but not universal, and that the intuitive ``separate confusable types'' strategy fails for LLMs that leverage comparative type reasoning.\n\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nTraining-free LLM information extraction---using instruction-tuned LLMs with in-context type definitions but no task-specific training---has emerged as a practical paradigm for rapid deployment.\nHowever, performance degrades sharply as schema complexity increases: schemas with $50{+}$ types can exhibit $20{-}60$ F\\textsubscript{1} gaps compared to supervised baselines.\n\nPrior work has addressed this degradation through schema decomposition: splitting large schemas into smaller batches for independent extraction.\nUniNER~\\cite{universal_ner_2024} uses per-type splitting, processing one type at a time.\nGoLLIE~\\cite{gollie_2024} provides type definitions as structured code.\nLLM-PEE~\\cite{llmpee_2024} implicitly leverages similarity-based grouping.\nYet none of these approaches validates the \\emph{assumption} that drives decomposition: what exactly makes schemas complex for LLMs, and does reducing a specific complexity dimension actually help?\n\nWe pose a precise question: \\textbf{Is schema complexity one-dimensional, or do distinct dimensions degrade LLM extraction through separable mechanisms?}\nConcretely, we isolate two candidate dimensions: \\emph{type count} (how many types the LLM must consider simultaneously) and \\emph{type confusability} (how semantically similar co-present types are).\nThrough controlled experiments across three IE tasks, two LLMs, and two embedding spaces, we find:\n\n\\begin{enumerate}[leftmargin=2em,itemsep=2pt]\n\\item \\textbf{Pairwise confusability predicts type confusion}, but the effect is model- and embedding-dependent.\nQwen3-32B on Few-NERD shows $r{=}0.156$ ($p{<}10^{-11}$); LLaMA-3.3-70B on the same task shows $r{=}0.042$ (not significant).\nNo single embedding universally captures confusability across tasks.\n\n\\item \\textbf{Count and confusability act through distinguishable channels}: count increases entity omission (recall degrades monotonically), while confusability increases type substitution errors ($4.8{\\times}$ ratio in extreme conditions).\nHowever, a formal $2{\\times}2$ interaction test is not significant ($p{=}0.582$), consistent with weak additive independence.\n\n\\item \\textbf{Per-type confusability aggregation is confounded} in semantically homogeneous schemas.\nOn MAVEN (168 FrameNet-derived event types), per-type mean confusability correlates \\emph{positively} with F\\textsubscript{1} ($\\rho{=}{+}0.195$), because central, well-represented types have high mean similarity but are also easier to extract.\nPairwise analysis avoids this confound.\n\n\\item \\textbf{Decomposition fails}: all confusability-minimizing decomposition strategies (SDGD-zero, SDGD-cal, per-type splitting) perform \\emph{worse} than single-pass extraction, because separating confusable types removes the disambiguation context that LLMs use for comparative type reasoning.\n\\end{enumerate}\n\nThese results establish schema complexity as a multi-dimensional phenomenon whose effects are contingent on model architecture, embedding choice, and schema structure.\nThe negative decomposition result is itself informative: it reveals that LLMs exploit type co-presence for disambiguation, a mechanism that simple separation strategies destroy.\n\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Training-free LLM IE.}\nRecent work has shown that instruction-tuned LLMs can perform IE tasks zero-shot by providing type definitions in the prompt~\\cite{universal_ner_2024,gollie_2024,llmpee_2024}.\nPerformance is competitive on simple schemas ($5{-}15$ types) but degrades substantially on complex ones.\n\n\\paragraph{Schema decomposition.}\nUniNER~\\cite{universal_ner_2024} processes one type at a time, achieving 3.3 F\\textsubscript{1} gains on some benchmarks but at $k{\\times}$ API cost.\nLLM-PEE~\\cite{llmpee_2024} groups types by embedding similarity, implicitly targeting confusability reduction.\nNeither approach validates whether the targeted complexity dimension is actually causal.\n\n\\paragraph{Schema complexity analysis.}\nThe relationship between label set complexity and extraction performance has been studied in supervised settings~\\cite{few_nerd_2021,maven_2020}, but controlled isolation of individual complexity dimensions in the LLM setting is unexplored.\nOur work fills this gap with factorial experimental designs.\n\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n% ============================================================\n\n\\subsection{Tasks and Datasets}\n\nWe study three IE tasks with varying schema characteristics:\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse domains. Cross-domain schema with heterogeneous type semantics.\n\\item \\textbf{MAVEN} (Event Detection): 168 event types derived from FrameNet. Same-domain schema with homogeneous type semantics.\n\\item \\textbf{DocRED} (Relation Extraction): 96 relation types. Document-level task where extraction involves cross-sentence reasoning.\n\\end{itemize}\n\n\\subsection{Models}\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Qwen3-32B-Instruct}: Primary extraction model. All experiments except the cross-model study use this model.\n\\item \\textbf{LLaMA-3.3-70B-Instruct}: Cross-model validation (Section~\\ref{sec:crossmodel}).\n\\end{itemize}\n\n\\subsection{Confusability Measures}\n\nWe compute \\emph{Schema Confusability Score} (SCS) as the cosine similarity between type definition embeddings:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\cos(\\mathbf{e}(t_i), \\mathbf{e}(t_j))\n\\end{equation}\nwhere $\\mathbf{e}(\\cdot)$ denotes the embedding function. We use two embedding models:\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Qwen3 embeddings}: Derived from the extraction model's own representations.\n\\item \\textbf{MiniLM}: A general-purpose sentence embedding model (all-MiniLM-L6-v2).\n\\end{itemize}\n\n\\emph{Pairwise confusability} uses SCS directly between type pairs.\n\\emph{Per-type confusability} (Batch Confusability Score, BCS) averages SCS across all co-present types:\n$\\text{BCS}(t_i) = \\frac{1}{|B|-1}\\sum_{t_j \\in B \\setminus \\{t_i\\}} \\text{SCS}(t_i, t_j)$.\n\n\\subsection{Evaluation Protocol}\n\nFor NER and event detection, we report both relaxed F\\textsubscript{1} (partial span matching) and exact F\\textsubscript{1}.\nWe use controlled batch construction: for each \\emph{count} level, we sample random subsets of types and evaluate extraction on held-out test data.\nWithin-count experiments vary confusability (BCS) while holding count fixed, isolating the confusability effect.\n\n\n% ============================================================\n\\section{Finding 1: Pairwise Confusability Predicts Type Confusion}\n\\label{sec:finding1}\n% ============================================================\n\nWe investigate whether pairwise type confusability (SCS between type pairs) predicts actual type confusion errors.\nWe test this across tasks, models, and embeddings.\n\n\\subsection{Few-NERD: Qwen3 Embeddings}\n\\label{sec:fewnerd_pairwise}\n\nOn Few-NERD with Qwen3-32B extraction and Qwen3 embeddings, pairwise SCS significantly correlates with pairwise confusion rate: Pearson $r{=}0.156$ ($p{=}4.6{\\times}10^{-12}$, $n{=}1{,}953$ type pairs).\nAmong type pairs with nonzero confusion, Spearman $\\rho{=}0.254$ ($p{=}1.1{\\times}10^{-6}$).\nHigh-SCS pairs such as \\texttt{person-other}$\\leftrightarrow$\\texttt{person-politician} (SCS$=$0.934) account for the majority of type confusion errors.\n\nIn extreme batches (deliberately constructed to maximize or minimize BCS), the confusion rate ratio reaches $10{-}28{\\times}$ between high- and low-confusability conditions.\nRandom batches show a smaller but consistent ratio of $1.7{-}2.4{\\times}$.\n\n\\subsection{MAVEN: Embedding-Dependent Signal}\n\\label{sec:maven_pairwise}\n\nMAVEN presents a contrasting pattern across embeddings (Table~\\ref{tab:pairwise_matrix}).\nWith MiniLM embeddings, the pairwise signal is significant: $r{=}0.115$ ($p{=}2.1{\\times}10^{-42}$, $n{=}14{,}028$ pairs), with Spearman $\\rho{=}0.128$ (nonzero-only $\\rho{=}0.185$).\nHowever, Qwen3 embeddings yield $r{=}{-}0.009$ ($p{=}0.38$)---completely non-significant.\n\nThis divergence reveals that confusability measurement is not embedding-agnostic.\nIn semantically homogeneous schemas (MAVEN's FrameNet-derived types), the extraction model's own embedding space may not differentiate confusable type pairs effectively, while a general-purpose embedding preserves discriminative structure.\n\n\\subsection{Cross-Model Validation: LLaMA-3.3-70B}\n\\label{sec:crossmodel}\n\nTo test whether confusability effects generalize across model families, we replicate the Few-NERD protocol with LLaMA-3.3-70B-Instruct.\nTable~\\ref{tab:crossmodel} presents the comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model comparison on Few-NERD. Confusability effects are substantially weaker for LLaMA-3.3-70B across all metrics.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3-32B} & \\textbf{LLaMA-3.3-70B} \\\\\n\\midrule\nBaseline \\fone{} (count 64) & 0.414 & 0.378 \\\\\nPairwise $r$ (Qwen3 embed) & 0.156*** & 0.042 (ns) \\\\\nPer-type $\\rho$ & $-$0.293* & $-$0.082 (ns) \\\\\nExtreme confusion ratio & 10--28$\\times$ & 2.1--2.5$\\times$ \\\\\nRandom confusion ratio & 1.7--2.4$\\times$ & 1.15--1.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLLaMA-3.3-70B shows no significant pairwise signal ($r{=}0.042$, $p{=}0.068$), no significant per-type correlation ($\\rho{=}{-}0.082$, $p{=}0.538$), and dramatically lower confusion rate ratios ($2.1{-}2.5{\\times}$ vs.\\ $10{-}28{\\times}$).\nEven controlling for log-frequency, the partial correlation remains non-significant (partial $r{=}{-}0.055$, $p{=}0.684$).\n\n\\begin{table}[t]\n\\centering\n\\caption{LLaMA-3.3-70B detailed statistics on Few-NERD. No analysis reaches significance.}\n\\label{tab:llama_detail}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Analysis} & \\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} & \\textbf{Verdict} \\\\\n\\midrule\nPairwise & Pearson $r$ & 0.042 & 0.068 & NS \\\\\nPairwise (nonzero) & Spearman $\\rho$ & 0.078 & 0.120 & NS \\\\\nPer-type & Spearman $\\rho$ & $-$0.082 & 0.538 & NS \\\\\nPer-type (partial) & Partial $r$ & $-$0.055 & 0.684 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis $4{\\times}$ effect size difference ($r{=}0.156$ vs.\\ $r{=}0.042$) across model families implies that confusability sensitivity is model-dependent.\nPrior conflicting findings about schema complexity effects may be partly explained by this model dependence.\n\n\\subsection{Embedding Proxy Validation}\n\\label{sec:scs_validation}\n\nTo assess whether embedding-based SCS is a valid proxy for actual model confusion, we compare SCS rankings against an empirical confusion matrix derived from calibration data (Table~\\ref{tab:scs_validation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Correlation between embedding SCS and empirical confusion rates. Both embeddings show weak predictive power.}\n\\label{tab:scs_validation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} & \\textbf{Kendall $\\tau$} & \\textbf{$p$} \\\\\n\\midrule\nQwen3 & 0.125 & 0.031 & 0.092 & 0.044 \\\\\nMiniLM & 0.098 & 0.082 & 0.071 & 0.115 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{SCS proxy error analysis: false positive/negative rates for confusion prediction.}\n\\label{tab:scs_errors}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3} & \\textbf{MiniLM} \\\\\n\\midrule\nFalse Positive Rate & 0.42 & 0.48 \\\\\nFalse Negative Rate & 0.35 & 0.40 \\\\\nTop-1 Match & Yes & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3 SCS achieves $\\rho{=}0.125$ ($p{=}0.031$) against empirical confusion---statistically significant but explaining only ${\\sim}1.6\\%$ of confusion variance.\nThe false positive rate of $0.42$ indicates that $42\\%$ of type pairs predicted as confusable by SCS are not actually confused by the model.\nConfusability is mediated by factors beyond semantic similarity, including surface form similarity, type definition wording, and in-context position.\n\n\\subsection{Summary: Pairwise Signal Matrix}\n\nTable~\\ref{tab:pairwise_matrix} summarizes the full cross-task $\\times$ cross-model $\\times$ cross-embedding matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise SCS--confusion signal across tasks, models, and embeddings. Only 3 of 7 tested cells reach significance; no single embedding or model universally works.}\n\\label{tab:pairwise_matrix}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Embedding} & \\textbf{Few-NERD} & \\textbf{MAVEN} & \\textbf{DocRED} \\\\\n\\midrule\nQwen3 & Qwen3 & $r{=}0.156$*** & $r{=}{-}0.009$ & --- \\\\\nQwen3 & MiniLM & --- & $r{=}0.115$*** & --- \\\\\nLLaMA & Qwen3 & $r{=}0.042$ & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize *** $p<0.001$. Cells marked ``---'' were not tested.}\n\\end{tabular}\n\\end{table}\n\n\n% ============================================================\n\\section{Finding 2: Count and Confusability Degrade Through Distinguishable Channels}\n\\label{sec:finding2}\n% ============================================================\n\n\\subsection{Count Curves Across Tasks}\n\\label{sec:count_curves}\n\nWe construct count curves by varying the number of types presented to the LLM while holding other factors constant.\nThe three tasks show strikingly different patterns:\n\n\\paragraph{Few-NERD.}\nRelaxed \\fone{} decreases monotonically with count (previously established), with recall declining as the primary driver.\n\n\\paragraph{MAVEN.}\nTable~\\ref{tab:maven_count} shows the \\emph{opposite} pattern: relaxed \\fone{} \\emph{increases} with count, from $0.098$ (count 1) to $0.243$ (count 100).\nRecall increases monotonically ($0.07{\\to}0.19$), while precision is roughly flat ($0.15{-}0.40$).\nThis reversal occurs because MAVEN's 168 FrameNet-derived types form a coherent ontology; more types in the prompt provide richer event taxonomy context that helps the model locate each type's position in the hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN count curve (500 samples, relaxed matching). Performance \\emph{increases} with type count---opposite of Few-NERD.}\n\\label{tab:maven_count}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{Count} & \\textbf{Relaxed \\fone{}} & \\textbf{Exact \\fone{}} & \\textbf{Recall} & \\textbf{Precision} & \\textbf{Pred/Gold} \\\\\n\\midrule\n1  & 0.098 & 0.008 & 0.070 & 0.162 & 0.43 \\\\\n6  & 0.112 & 0.005 & 0.085 & 0.165 & 0.52 \\\\\n12 & 0.155 & 0.011 & 0.118 & 0.226 & 0.52 \\\\\n22 & 0.192 & 0.016 & 0.148 & 0.274 & 0.54 \\\\\n44 & 0.238 & 0.021 & 0.180 & 0.350 & 0.51 \\\\\n64 & 0.241 & 0.018 & 0.182 & 0.358 & 0.51 \\\\\n100 & 0.243 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED.}\nTable~\\ref{tab:docred_count} shows an approximately flat count curve with no clear monotonic pattern.\n\\fone{} ranges from $0.185$ (count 4) to $0.208$ (count 48), with a slight decline at the full schema (count 96, \\fone{}$=$0.195).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED count curve (document-level RE). Performance is near-flat---schema complexity effects are dominated by cross-sentence reasoning demands.}\n\\label{tab:docred_count}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Count} & \\textbf{\\fone{}} & \\textbf{Recall} & \\textbf{Precision} & \\textbf{Confusion Rate} \\\\\n\\midrule\n4  & 0.185 & 0.145 & 0.256 & 0.008 \\\\\n8  & 0.192 & 0.152 & 0.261 & 0.012 \\\\\n16 & 0.198 & 0.158 & 0.264 & 0.015 \\\\\n32 & 0.203 & 0.165 & 0.258 & 0.018 \\\\\n48 & 0.208 & 0.170 & 0.261 & 0.019 \\\\\n96 & 0.195 & 0.160 & 0.250 & 0.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-task comparison reveals that count effects are task-dependent: monotonically negative (Few-NERD), monotonically positive (MAVEN), or negligible (DocRED).\n\n\\subsection{Within-Count BCS--\\fone{} Correlation}\n\\label{sec:within_count}\n\nTo isolate confusability from count, we examine the correlation between batch-level BCS and \\fone{} \\emph{within} fixed count levels.\n\n\\paragraph{MAVEN.} Table~\\ref{tab:maven_within_count} shows no significant within-count BCS--\\fone{} correlation, with both individual count levels and the pooled analysis failing to reach significance.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN within-count BCS--\\fone{} correlation. No significant relationship detected at any count level.}\n\\label{tab:maven_within_count}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Count} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Direction} & \\textbf{Verdict} \\\\\n\\midrule\n6  & $+$0.175 & 0.185 & Positive & Fail \\\\\n12 & $+$0.124 & 0.315 & Positive & Fail \\\\\nPooled & $+$0.142 & 0.108 & Positive & Fail \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe positive direction (higher BCS $\\to$ higher \\fone{}) is opposite to the confusability hypothesis and consistent with centrality confounding (Section~\\ref{sec:finding3}).\n\n\\paragraph{DocRED.} Within-count BCS--\\fone{} correlations are similarly non-significant: count 8 ($r{=}0.032$, $p{=}0.62$), count 16 ($r{=}{-}0.058$, $p{=}0.48$), pooled ($r{=}{-}0.015$, $p{=}0.84$).\nThe per-type BCS--\\fone{} correlation is also null ($\\rho{=}{-}0.04$, $p{=}0.72$).\n\n\\subsection{2$\\times$2 Factorial Design: Count $\\times$ Confusability Interaction}\n\\label{sec:factorial}\n\nWe test the interaction between count and confusability using a $2{\\times}2$ factorial design on Few-NERD: \\{low count$=$6, high count$=$22\\} $\\times$ \\{low BCS, high BCS\\}, with 12 batches per cell ($n{=}48$ total).\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ cell means (\\fone{}, text match) on Few-NERD. Both factors show directional effects, but the interaction is not significant.}\n\\label{tab:factorial_means}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\n\\midrule\nLow Count (6)  & 0.348 & 0.312 & $\\Delta{=}{-}0.036$ \\\\\nHigh Count (22) & 0.298 & 0.255 & $\\Delta{=}{-}0.043$ \\\\\n\\midrule\nCount Effect & $\\Delta{=}{-}0.050$ & $\\Delta{=}{-}0.057$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Two-way ANOVA results. Count is significant; BCS is marginal; the interaction is not significant.}\n\\label{tab:anova}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Source} & \\textbf{$F$} & \\textbf{$p$} & \\textbf{$\\eta^2$} & \\textbf{Verdict} \\\\\n\\midrule\nCount       & 7.82 & 0.008 & 0.14  & Significant \\\\\nBCS         & 2.93 & 0.094 & 0.06  & Marginal \\\\\nCount$\\times$BCS & 0.31 & 0.582 & 0.006 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe count main effect is significant ($F{=}7.82$, $p{=}0.008$, $\\eta^2{=}0.14$), while BCS is marginal ($F{=}2.93$, $p{=}0.094$, $\\eta^2{=}0.06$).\nThe interaction is not significant ($F{=}0.31$, $p{=}0.582$, $\\eta^2{=}0.006$), consistent with an additive (rather than multiplicative) combination of the two channels.\nSimple effects analysis shows that BCS effects are directionally consistent at both count levels but neither reaches significance individually (low count: $\\Delta{=}{-}0.036$, $p{=}0.22$; high count: $\\Delta{=}{-}0.043$, $p{=}0.18$).\n\n\n\\subsection{Error Taxonomy: Mechanistic Evidence for Distinct Channels}\n\\label{sec:error_taxonomy}\n\nWe perform a systematic error classification on Few-NERD extraction outputs, categorizing false positives into four types: type substitution, boundary error, spurious extraction, and missed entity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall error distribution. Spurious extraction dominates; type substitution (the channel most related to confusability) accounts for only 18\\%.}\n\\label{tab:error_dist}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Error Type} & \\textbf{Proportion} & \\textbf{Primary Driver} \\\\\n\\midrule\nSpurious Extraction & 45\\% & Prompt format \\\\\nMissed Entity       & 25\\% & Count (recall) \\\\\nType Substitution   & 18\\% & BCS (confusability) \\\\\nBoundary Error      & 12\\% & Span detection \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Type substitution by confusability.}\nIn extreme high-BCS batches, the type substitution rate reaches $0.058$, compared to $0.012$ in extreme low-BCS batches---a $4.8{\\times}$ ratio (Table~\\ref{tab:type_sub_bcs}).\nHowever, in \\emph{random} batches, the ratio drops to $1.5{\\times}$ ($0.022$ vs.\\ $0.015$), indicating that the effect is pronounced only under deliberately extreme conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Type substitution rate by BCS condition. The extreme ratio (4.8$\\times$) substantially exceeds the random ratio (1.5$\\times$).}\n\\label{tab:type_sub_bcs}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{High BCS} & \\textbf{Low BCS} & \\textbf{Ratio} \\\\\n\\midrule\nExtreme Batch & 0.058 & 0.012 & 4.8$\\times$ \\\\\nRandom Batch  & 0.022 & 0.015 & 1.5$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Missed entities by count.}\nThe miss rate increases monotonically with count: $0.28$ (count 6) $\\to$ $0.42$ (count 22) $\\to$ $0.55$ (count 64).\nCrucially, the miss rate does \\emph{not} vary with BCS (high BCS: $0.40$; low BCS: $0.38$; ratio $1.05$), confirming that count and confusability affect different error modes.\n\n\\begin{table}[t]\n\\centering\n\\caption{Missed entity rate by count. Monotonically increasing, independent of BCS.}\n\\label{tab:miss_count}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Count} & \\textbf{Miss Rate} & \\textbf{$\\Delta$ vs.\\ Count 6} \\\\\n\\midrule\n6  & 0.28 & --- \\\\\n22 & 0.42 & $+$0.14 \\\\\n64 & 0.55 & $+$0.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Boundary errors and hallucination.}\nNeither boundary errors (high BCS: $0.041$; low BCS: $0.038$; ratio $1.08$) nor hallucination (rate $0.03$, no BCS effect) are influenced by confusability, as expected---these error modes are orthogonal to type semantics.\n\n\n% ============================================================\n\\section{Finding 3: Per-Type Aggregation Introduces Centrality Confound}\n\\label{sec:finding3}\n% ============================================================\n\n\\subsection{MAVEN: Positive Per-Type Correlation}\n\nOn MAVEN, per-type mean BCS correlates \\emph{positively} with per-type \\fone{} under both embeddings (Table~\\ref{tab:maven_pertype}).\nThis is the \\emph{opposite} of what the confusability hypothesis predicts.\n\n\\begin{table}[t]\n\\centering\n\\caption{MAVEN pairwise and per-type confusability analysis. Per-type correlations are positive (confounded); pairwise MiniLM is significant.}\n\\label{tab:maven_pertype}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Pairwise $r$ ($p$)} & \\textbf{Per-type $\\rho$ ($p$)} \\\\\n\\midrule\nQwen3  & $-$0.009 (0.38) & $+$0.195 (0.018) \\\\\nMiniLM & $+$0.115 ($2.1{\\times}10^{-42}$) & $+$0.212 (0.009) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is \\emph{centrality confounding}: in MAVEN's semantically homogeneous schema, types with high mean BCS are central, frequent types (e.g., \\textsc{Attack}, \\textsc{Movement}) that the LLM extracts well because they are well-represented in training data and have clear definitions.\nMean BCS conflates confusability with type centrality; per-type aggregation cannot separate these effects.\n\nCrucially, the pairwise analysis tells a different story.\nMiniLM pairwise SCS significantly predicts confusion ($r{=}0.115$, $p{<}10^{-42}$), demonstrating that pairwise analysis avoids the centrality confound.\nThe Qwen3 pairwise signal is null ($r{=}{-}0.009$), highlighting that embedding choice interacts with schema structure.\n\nThe confusion rate analysis further supports this: MAVEN's extreme confusion ratios ($5.8{\\times}$ at count 6, $4.2{\\times}$ at count 12) are lower than Few-NERD's ($10{-}28{\\times}$), while random ratios ($1.4{\\times}$, $1.3{\\times}$) are modest.\n\n\\subsection{DocRED: Null Result as Boundary Condition}\n\nDocRED yields complete null results across all confusability analyses (Section~\\ref{sec:within_count}).\nThe pairwise signal is non-significant for both Qwen3 ($r{=}0.023$, $p{=}0.14$) and MiniLM ($r{=}0.031$, $p{=}0.08$).\nThe per-type BCS--\\fone{} correlation is null ($\\rho{=}{-}0.04$, $p{=}0.72$).\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED pairwise confusability analysis. No significant signal detected with either embedding.}\n\\label{tab:docred_pairwise}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Pearson $r$} & \\textbf{$p$} & \\textbf{$n$ pairs} & \\textbf{Verdict} \\\\\n\\midrule\nQwen3  & 0.023 & 0.14 & 4,560 & NS \\\\\nMiniLM & 0.031 & 0.08 & 4,560 & NS \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis null result establishes a boundary condition: confusability effects require that type definitions occupy a significant fraction of the prompt.\nIn document-level RE, the document content dominates the prompt; type definitions are a small fraction, and performance bottlenecks lie in cross-sentence reasoning and entity pair combinatorics rather than type confusability.\n\n\n% ============================================================\n\\section{Finding 4: Confusability-Minimizing Decomposition Fails}\n\\label{sec:finding4}\n% ============================================================\n\nMotivated by the confusability signal in Section~\\ref{sec:finding1}, we tested whether separating confusable types into different batches (Schema DAG Decomposition, SDGD) could improve extraction.\nWe report a comprehensive negative result: all decomposition strategies perform worse than single-pass extraction.\nFull details and per-batch breakdowns are in Appendix~\\ref{app:sdgd}.\n\n\\subsection{Overview of Methods}\n\n\\begin{itemize}[leftmargin=1.5em,itemsep=2pt]\n\\item \\textbf{Single-pass}: All types in one prompt.\n\\item \\textbf{SDGD-zero}: Graph coloring on the SCS-thresholded pairwise similarity graph (no calibration data).\n\\item \\textbf{SDGD-cal}: Graph coloring on an empirical confusion matrix from 8--10 calibration samples.\n\\item \\textbf{Random ($k$)}: Random batching with the same number of batches as SDGD.\n\\item \\textbf{Per-type}: One type per batch (UniNER-style).\n\\end{itemize}\n\n\\subsection{Results}\n\nTable~\\ref{tab:sdgd_main} presents the full comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full method comparison. All decomposition methods are inferior to single-pass. Ordering: single-pass $>$ SDGD-cal $\\gtrsim$ random $\\gtrsim$ SDGD-zero $>$ per-type. Methods are sorted by Few-NERD \\fone{}.}\n\\label{tab:sdgd_main}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\multicolumn{3}{c}{\\textbf{Few-NERD}} & \\multicolumn{2}{c}{\\textbf{MAVEN}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & \\fone{} & Prec. & Recall & Rel.\\ \\fone{} & API \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 0.241 & 1$\\times$ \\\\\nSDGD-cal    & 0.381 & 0.342 & 0.430 & 0.188 & 7--12$\\times$ \\\\\nRandom      & 0.374 & 0.335 & 0.425 & 0.180 & 8--12$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 0.168 & 8--15$\\times$ \\\\\nPer-type    & 0.330 & 0.225 & 0.620 & 0.108 & 66--168$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe consistent pattern across both tasks: decomposition increases recall (each batch focuses on fewer types, enabling more aggressive extraction) but devastates precision (without the full type set, the model cannot disambiguate, leading to massive over-extraction).\nThe precision--recall tradeoff is unfavorable: precision losses far exceed recall gains.\n\n\\paragraph{SDGD vs.\\ random is not significant.}\nSDGD-zero does not outperform random batching on either task (Few-NERD: $\\Delta{=}{-}0.7$pp, $p{=}0.68$; MAVEN: $\\Delta{=}{-}1.2$pp, $p{=}0.42$).\nConfusability-aware grouping provides no value over random partitioning.\n\n\\paragraph{Per-type splitting is worst.}\nThe extreme decomposition---one type per batch---yields the lowest \\fone{} (Few-NERD: $0.330$; MAVEN: $0.108$) at the highest cost ($66{-}168{\\times}$ API calls).\nThis confirms that decomposition granularity is inversely related to performance.\n\n\\paragraph{Root cause.}\nDecomposition removes \\emph{disambiguation context}: when confusable types are separated, each batch sees only one side of a confusable pair, and the model assigns the available type to any plausible mention.\nUpon merging batches, the same span may receive conflicting type assignments ($8\\%$ cross-batch span overlap), and the overall prediction count far exceeds gold annotations (pred/gold ratio $1.36$ vs.\\ single-pass $0.47$).\n\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Schema complexity is multi-dimensional but context-dependent.}\nOur results establish that count and confusability are distinguishable dimensions of schema complexity, but their effects are contingent on task structure, model architecture, and embedding choice.\nOn Few-NERD (cross-domain NER), count dominates; on MAVEN (same-domain ED), more types \\emph{help}; on DocRED (document-level RE), neither dimension matters.\n\n\\paragraph{Confusability effects are real but not universal.}\nThe pairwise confusability signal is significant for Qwen3 on Few-NERD and MiniLM on MAVEN, but absent for LLaMA-3.3-70B and for Qwen3 embeddings on MAVEN.\nThis model dependence suggests that confusability sensitivity is a property of the model's internal representation, not solely of the schema itself.\nThe $4{\\times}$ effect size difference between Qwen3 ($r{=}0.156$) and LLaMA ($r{=}0.042$) is itself a finding that may explain prior conflicting reports about schema complexity effects.\n\n\\paragraph{Per-type aggregation is unreliable.}\nThe centrality confound on MAVEN demonstrates that mean BCS (per-type averaged confusability) is not a valid measure in semantically homogeneous schemas.\nFuture work on schema complexity should use pairwise analysis to avoid this confound, or use empirical confusion matrices that bypass embedding proxy limitations.\n\n\\paragraph{Decomposition harms LLM IE.}\nThe most counter-intuitive finding is that confusability-minimizing decomposition \\emph{hurts} performance.\nLLMs use type co-presence for comparative reasoning: seeing confusable types together enables the model to reason about their distinctions.\nRemoving this context forces the model into uninformed guessing.\nThis insight has direct implications for decomposition-based approaches: they should be designed to \\emph{preserve} disambiguation context rather than minimize confusability.\n\n\\paragraph{Implications for future work.}\n(1)~Confusability-based methods should be evaluated per-model, not assumed universal.\n(2)~Schema decomposition for LLM IE needs fundamentally different principles---perhaps preserving confusable types together while reducing only the non-informative count overhead.\n(3)~Embedding-based confusability proxies need task-specific calibration, as no single embedding works universally.\n\n\\paragraph{Limitations.}\nOur study uses two LLM families; more models are needed to characterize the distribution of confusability sensitivity.\nThe $2{\\times}2$ factorial design has limited statistical power ($n{=}48$); larger-scale factorial experiments could detect smaller interaction effects.\nDocRED results may partly reflect the difficulty of zero-shot document-level RE rather than a true absence of confusability effects.\n\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe presented the first controlled empirical study isolating type count and type confusability as dimensions of schema complexity in training-free LLM information extraction.\nOur experiments across three IE tasks, two LLMs, and two embedding spaces reveal that:\n(1)~pairwise type confusability is a valid predictor of type confusion errors, but only for specific model$\\times$embedding combinations;\n(2)~count and confusability degrade performance through distinguishable error channels;\n(3)~per-type confusability aggregation introduces centrality confounds in homogeneous schemas; and\n(4)~confusability-minimizing decomposition is counter-productive because LLMs leverage type co-presence for disambiguation.\nThese findings reframe schema complexity as a multi-dimensional, model-dependent phenomenon and provide methodological guidance for future research on LLM IE with complex schemas.\n\n\n% ============================================================\n\\appendix\n\\section{SDGD Decomposition: Detailed Results}\n\\label{app:sdgd}\n% ============================================================\n\nThis appendix provides detailed results for all decomposition experiments, which are reported as negative results in the main paper (Section~\\ref{sec:finding4}).\n\n\\subsection{SDGD-zero on Few-NERD}\n\\label{app:sdgd_zero_fewnerd}\n\nGraph coloring on the Qwen3 SCS-thresholded graph ($\\tau{=}0.847$) produces 8 batches (avg.\\ size $8.25$, range $4{-}12$).\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero vs.\\ single-pass on Few-NERD (66 types).}\n\\label{tab:sdgd_zero_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{Pred/Gold} & \\textbf{API} \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 0.47 & 1$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 1.36 & 8$\\times$ \\\\\n$\\Delta$    & $-$4.7pp & $-$33.0pp & $+$13.0pp & $+$0.89 & $+$7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero per-batch breakdown (top 4 batches, Few-NERD).}\n\\label{tab:sdgd_zero_perbatch}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\n\\textbf{Batch} & \\textbf{Types} & \\textbf{Avg BCS} & \\textbf{\\fone{}} & \\textbf{Recall} & \\textbf{Precision} \\\\\n\\midrule\n0 & 12 & 0.812 & 0.42 & 0.48 & 0.38 \\\\\n1 & 10 & 0.795 & 0.38 & 0.45 & 0.33 \\\\\n2 & 9  & 0.780 & 0.35 & 0.42 & 0.30 \\\\\n3 & 8  & 0.763 & 0.32 & 0.40 & 0.27 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGraph statistics: 142 edges, edge density $0.066$, chromatic number 8, max intra-batch BCS $0.842$.\nCross-batch span overlap: $8\\%$ of predictions appear in multiple batches.\nTotal predictions: $4{,}850$ (after dedup: $4{,}120$), averaging $8.2$ predictions per sample vs.\\ $5.9$ gold entities.\n\n\\subsection{SDGD-zero on MAVEN}\n\\label{app:sdgd_zero_maven}\n\nOn MAVEN (168 types), adaptive threshold $\\tau{=}0.319$ produces 15 batches (avg.\\ size $11.2$, range $5{-}18$), with edge density $0.132$ and $1{,}850$ edges.\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-zero vs.\\ single-pass on MAVEN (168 types, relaxed matching).}\n\\label{tab:sdgd_zero_maven}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{Exact \\fone{}} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.241 & 0.018 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-zero   & 0.168 & 0.012 & 15$\\times$ & 12.8$\\times$ \\\\\n$\\Delta$    & $-$7.3pp & $-$0.6pp & $+$14$\\times$ & $+$11.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe larger performance gap on MAVEN ($-$7.3pp vs.\\ $-$4.7pp on Few-NERD) is consistent with MAVEN's positive count curve: decomposition directly counteracts the benefit of full ontology visibility.\n\n\\subsection{SDGD-cal on Few-NERD}\n\\label{app:sdgd_cal_fewnerd}\n\nSDGD-cal uses 8 calibration samples to build an empirical confusion matrix, yielding 85 nonzero confusion pairs.\nThe empirical confusion matrix correlates weakly with embedding SCS ($\\rho{=}0.125$, $p{=}0.031$).\nGraph coloring produces 7 batches (avg.\\ size $9.4$).\n\n\\begin{table}[h]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on Few-NERD.}\n\\label{tab:sdgd_cal_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{$\\Delta$ vs.\\ SP} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{API} \\\\\n\\midrule\nSingle-pass & 0.414 & --- & 0.648 & 0.304 & 1$\\times$ \\\\\nRandom ($k{=}8$) & 0.374 & $-$4.0 & 0.335 & 0.425 & 8$\\times$ \\\\\nSDGD-zero   & 0.367 & $-$4.7 & 0.318 & 0.434 & 8$\\times$ \\\\\nSDGD-cal    & 0.381 & $-$3.3 & 0.342 & 0.430 & 7$\\times$ $+$ 8 cal. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal marginally outperforms SDGD-zero ($+$1.4pp) and random ($+$0.7pp, $p{=}0.58$), but the improvement over random is not significant.\nEven with empirical confusion data, the decomposition penalty persists.\n\n\\subsection{SDGD-cal on MAVEN}\n\\label{app:sdgd_cal_maven}\n\nOn MAVEN, 10 calibration samples produce 210 nonzero confusion pairs.\nGraph coloring yields 12 batches (avg.\\ size $14.0$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Full comparison on MAVEN (168 types, relaxed matching).}\n\\label{tab:sdgd_cal_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{$\\Delta$ vs.\\ SP} & \\textbf{API} \\\\\n\\midrule\nSingle-pass  & 0.241 & --- & 1$\\times$ \\\\\nRandom ($k{=}12$) & 0.180 & $-$6.1 & 12$\\times$ \\\\\nSDGD-zero    & 0.168 & $-$7.3 & 15$\\times$ \\\\\nSDGD-cal     & 0.188 & $-$5.3 & 12$\\times$ $+$ 10 cal. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSDGD-cal outperforms SDGD-zero ($+$2.0pp) but not random ($+$0.8pp, $p{=}0.62$).\nThe same pattern as Few-NERD: calibration helps marginally, but decomposition remains inferior to single-pass.\n\n\\subsection{Random Batching Ablation}\n\\label{app:random}\n\nTo isolate the contribution of confusability-aware grouping from the batch count reduction effect, we compare SDGD-zero against random batching with the same number of batches.\n\n\\begin{table}[h]\n\\centering\n\\caption{Random vs.\\ SDGD-zero on Few-NERD ($k{=}8$, 10 random seeds).}\n\\label{tab:random_fewnerd}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean \\fone{}} & \\textbf{Std} & \\textbf{Range} & \\textbf{vs.\\ SP} \\\\\n\\midrule\nRandom$\\times$10 & 0.374 & 0.018 & [0.348, 0.402] & $-$4.0pp \\\\\nSDGD-zero & 0.367 & --- & --- & $-$4.7pp \\\\\n$\\Delta$ (SDGD$-$Random) & \\multicolumn{4}{c}{$-$0.7pp, $p{=}0.68$ (NS)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Random vs.\\ SDGD-zero on MAVEN.}\n\\label{tab:random_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{vs.\\ SP} & \\textbf{$p$ (paired)} \\\\\n\\midrule\nRandom$\\times$5 & 0.180 & $-$6.1pp & --- \\\\\nSDGD-zero & 0.168 & $-$7.3pp & --- \\\\\n$\\Delta$ & \\multicolumn{3}{c}{$-$1.2pp, $p{=}0.42$ (NS)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn both tasks, SDGD-zero does not significantly outperform random batching, confirming that confusability-aware grouping provides no measurable benefit.\nSDGD-zero may actually perform slightly \\emph{worse} than random, because deliberately separating confusable types removes same-cluster disambiguation anchors that random batching occasionally preserves.\n\n\\subsection{Per-Type Splitting Ablation}\n\\label{app:pertype}\n\nPer-type splitting (one type per batch) represents the extreme of decomposition---maximum confusability elimination but also maximum loss of disambiguation context.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-type splitting vs.\\ all methods on Few-NERD.}\n\\label{tab:pertype_fewnerd}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\fone{}} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.414 & 0.648 & 0.304 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-cal    & 0.381 & 0.342 & 0.430 & 7$\\times$ & 5.5$\\times$ \\\\\nRandom ($k{=}8$) & 0.374 & 0.335 & 0.425 & 8$\\times$ & 6.5$\\times$ \\\\\nSDGD-zero   & 0.367 & 0.318 & 0.434 & 8$\\times$ & 6.5$\\times$ \\\\\nPer-type    & 0.330 & 0.225 & 0.620 & 66$\\times$ & 48$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-type splitting vs.\\ all methods on MAVEN (relaxed matching).}\n\\label{tab:pertype_maven}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Relaxed \\fone{}} & \\textbf{API} & \\textbf{Wall-Clock} \\\\\n\\midrule\nSingle-pass & 0.241 & 1$\\times$ & 1$\\times$ \\\\\nSDGD-cal    & 0.188 & 12$\\times$ & 10$\\times$ \\\\\nRandom      & 0.180 & 12$\\times$ & 10$\\times$ \\\\\nSDGD-zero   & 0.168 & 15$\\times$ & 12.8$\\times$ \\\\\nPer-type    & 0.108 & 168$\\times$ & 135$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe method ordering is consistent across both tasks: single-pass $>$ SDGD-cal $\\gtrsim$ random $\\gtrsim$ SDGD-zero $>$ per-type.\nDecomposition granularity is inversely correlated with \\fone{}: larger batches (more type context) consistently outperform smaller ones.\nPer-type splitting achieves the highest recall (0.620 on Few-NERD) through aggressive per-type extraction, but precision collapses (0.225) as each batch drastically over-extracts.\n\n% ============================================================\n% References\n% ============================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem{universal_ner_2024}\nW.~Zhou, S.~Zhang, Y.~Gu, M.~Chen, and H.~Peng.\n\\newblock Universal{NER}: Targeted distillation from large language models for open named entity recognition.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{gollie_2024}\nO.~Sainz, I.~Garc{\\'i}a-Ferrero, R.~Agerri, O.~L{\\'o}pez~de~Lacalle, G.~Rigau, and E.~Agirre.\n\\newblock Go{LLIE}: Annotation guidelines improve zero-shot information extraction.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem{llmpee_2024}\nG.~Zaratiana, N.~Tomeh, P.~Holat, and T.~Charnois.\n\\newblock {LLM-PEE}: Prompt-based extraction with embedding similarity for entity extraction using large language models.\n\\newblock \\emph{arXiv preprint arXiv:2312.15805}, 2024.\n\n\\bibitem{few_nerd_2021}\nN.~Ding, G.~Xu, Y.~Chen, X.~Wang, X.~Han, P.~Xie, H.~Zheng, and Z.~Liu.\n\\newblock Few-{NERD}: A few-shot named entity recognition dataset.\n\\newblock In \\emph{Proc.\\ ACL-IJCNLP}, 2021.\n\n\\bibitem{maven_2020}\nX.~Wang, Z.~Wang, X.~Han, W.~Jiang, R.~Han, Z.~Liu, J.~Li, P.~Li, Y.~Lin, and J.~Zhou.\n\\newblock {MAVEN}: A massive general domain event detection dataset.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2020.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "29af7aa0-52dd-4eae-a7b5-6fcc3fa6b60f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "8812f519-c413-4a0e-b398-cd045c2b8e11",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Tool call

_source line 24 · 2026-05-15T12:21:58.586Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JoBNGc3GLqQC48ZZYyfQM3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8812f519-c413-4a0e-b398-cd045c2b8e11",
  "isSidechain": false,
  "requestId": "req_011Cb4M2BZbyLTBBkRzUdGsP",
  "type": "assistant",
  "uuid": "2307c678-b297-4156-9028-9939a9b761c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSPNqKqX2LTd988WNo6TCf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16688,
      "cache_read_input_tokens": 47335,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 47335,
          "cache_creation_input_tokens": 16688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16688
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

_source line 25 · 2026-05-15T12:22:00.153Z_

<details><summary>↩ Tool result · `toolu_01JoBNGc3GLqQC48ZZYyfQM3`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `universal_ner_2024' on page 1 undefined on in
put line 51.


Package natbib Warning: Citation `gollie_2024' on page 1 undefined on input lin
e 52.


Package natbib Warning: Citation `llmpee_2024' on page 1 undefined on input lin
e 53.


Overfull \hbox (3.55803pt too wide) in paragraph at lines 61--64
[]\OT1/cmr/bx/n/10.95 Pairwise con-fus-abil-ity pre-dicts type con-fu-sion\OT1/
cmr/m/n/10.95 , but the ef-fect is model- and embedding-
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (13.15128pt too wide) in paragraph at lines 68--71
[]\OT1/cmr/bx/n/10.95 Per-type con-fus-abil-ity ag-gre-ga-tion is con-founded \
OT1/cmr/m/n/10.95 in se-man-ti-cally ho-mo-ge-neous schemas.

Package natbib Warning: Citation `universal_ner_2024' on page 2 undefined on in
put line 85.


Package natbib Warning: Citation `gollie_2024' on page 2 undefined on input lin
e 85.


Package natbib Warning: Citation `llmpee_2024' on page 2 undefined on input lin
e 85.


Package natbib Warning: Citation `universal_ner_2024' on page 2 undefined on in
put line 89.


Package natbib Warning: Citation `llmpee_2024' on page 2 undefined on input lin
e 90.


Package natbib Warning: Citation `few_nerd_2021' on page 2 undefined on input l
ine 94.


Package natbib Warning: Citation `maven_2020' on page 2 undefined on input line
 94.

[2]

LaTeX Warning: Reference `sec:crossmodel' on page 3 undefined on input line 117
.


Overfull \hbox (47.46207pt too wide) in paragraph at lines 132--135
\OT1/cmr/m/n/10.95 Con-fus-abil-ity Score, BCS) av-er-ages SCS across all co-pr
esent types: $[](\OML/cmm/m/it/10.95 t[]\OT1/cmr/m/n/10.95 ) = [] [][] [](\OML/
cmm/m/it/10.95 t[]; t[]\OT1/cmr/m/n/10.95 )$. 

LaTeX Warning: Reference `tab:pairwise_matrix' on page 3 undefined on input lin
e 164.


LaTeX Warning: Reference `tab:crossmodel' on page 3 undefined on input line 175
.

[3]

LaTeX Warning: Reference `tab:scs_validation' on page 4 undefined on input line
 221.


LaTeX Warning: Reference `tab:pairwise_matrix' on page 4 undefined on input lin
e 260.

[4]

LaTeX Warning: Reference `tab:maven_count' on page 5 undefined on input line 29
5.


LaTeX Warning: Reference `tab:docred_count' on page 5 undefined on input line 3
20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\mathsurround' on input line 344.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\z@' on input line 344.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 344.


LaTeX Warning: Reference `tab:maven_within_count' on page 5 undefined on input 
line 349.


LaTeX Warning: Reference `sec:finding3' on page 5 undefined on input line 367.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.

(/usr/share/texlive/texmf-dist/tex/latex/base/omscmr.fd) [5]

LaTeX Warning: Reference `tab:type_sub_bcs' on page 6 undefined on input line 4
38.


LaTeX Warning: Reference `tab:maven_pertype' on page 6 undefined on input line 
487.

[6]

LaTeX Warning: Reference `sec:within_count' on page 7 undefined on input line 5
16.


LaTeX Warning: Reference `sec:finding1' on page 7 undefined on input line 544.


LaTeX Warning: Reference `app:sdgd' on page 7 undefined on input line 546.

[7]

LaTeX Warning: Reference `tab:sdgd_main' on page 8 undefined on input line 560.


[8] [9]

LaTeX Warning: Reference `sec:finding4' on page 10 undefined on input line 653.



LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (1.7898pt too wide) in paragraph at lines 723--726
\OT1/cmr/m/n/10.95 con-fu-sion pairs. The em-pir-i-cal con-fu-sion ma-trix cor-
re-lates weakly with em-bed-ding SCS ($\OML/cmm/m/it/10.95 ^^Z[]\OT1/cmr/m/n/10
.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 125$,
[10]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[11]

Package natbib Warning: There were undefined citations.

[12] [13] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06952pt)
Font metrics written on tcrm1095.tfm.
Output written on tcrm1095.600gf (128 characters, 25592 bytes).
Transcript written on tcrm1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam1
0.pfb>
Output written on paper.pdf (13 pages, 276804 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (3.55803pt too wide) in paragraph at lines 61--64
[]\OT1/cmr/bx/n/10.95 Pairwise con-fus-abil-ity pre-dicts type con-fu-sion\OT1/
cmr/m/n/10.95 , but the ef-fect is model- and embedding-
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (13.15128pt too wide) in paragraph at lines 68--71
[]\OT1/cmr/bx/n/10.95 Per-type con-fus-abil-ity ag-gre-ga-tion is con-founded \
OT1/cmr/m/n/10.95 in se-man-ti-cally ho-mo-ge-neous schemas.
[2]
Overfull \hbox (47.46207pt too wide) in paragraph at lines 132--135
\OT1/cmr/m/n/10.95 Con-fus-abil-ity Score, BCS) av-er-ages SCS across all co-pr
esent types: $[](\OML/cmm/m/it/10.95 t[]\OT1/cmr/m/n/10.95 ) = [] [][] [](\OML/
cmm/m/it/10.95 t[]; t[]\OT1/cmr/m/n/10.95 )$. 
[3] [4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\mathsurround' on input line 344.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\z@' on input line 344.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 344.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\times' on input line 372.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 372.

(/usr/share/texlive/texmf-dist/tex/latex/base/omscmr.fd) [5] [6] [7] [8]
[9]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (1.7898pt too wide) in paragraph at lines 723--726
\OT1/cmr/m/n/10.95 con-fu-sion pairs. The em-pir-i-cal con-fu-sion ma-trix cor-
re-lates weakly with em-bed-ding SCS ($\OML/cmm/m/it/10.95 ^^Z[]\OT1/cmr/m/n/10
.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 125$,
[10]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[11] [12] [13] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam1
0.pfb>
Output written on paper.pdf (13 pages, 280549 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2307c678-b297-4156-9028-9939a9b761c6",
  "isSidechain": false,
  "promptId": "97b4ef60-8c01-4543-aaf8-b4ae04fb9257",
  "type": "user",
  "uuid": "a876f80a-f193-4fd8-8bc9-0b9e732e2f8a",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `universal_ner_2024' on page 1 undefined on in\nput line 51.\n\n\nPackage natbib Warning: Citation `gollie_2024' on page 1 undefined on input lin\ne 52.\n\n\nPackage natbib Warning: Citation `llmpee_2024' on page 1 undefined on input lin\ne 53.\n\n\nOverfull \\hbox (3.55803pt too wide) in paragraph at lines 61--64\n[]\\OT1/cmr/bx/n/10.95 Pairwise con-fus-abil-ity pre-dicts type con-fu-sion\\OT1/\ncmr/m/n/10.95 , but the ef-fect is model- and embedding-\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (13.15128pt too wide) in paragraph at lines 68--71\n[]\\OT1/cmr/bx/n/10.95 Per-type con-fus-abil-ity ag-gre-ga-tion is con-founded \\\nOT1/cmr/m/n/10.95 in se-man-ti-cally ho-mo-ge-neous schemas.\n\nPackage natbib Warning: Citation `universal_ner_2024' on page 2 undefined on in\nput line 85.\n\n\nPackage natbib Warning: Citation `gollie_2024' on page 2 undefined on input lin\ne 85.\n\n\nPackage natbib Warning: Citation `llmpee_2024' on page 2 undefined on input lin\ne 85.\n\n\nPackage natbib Warning: Citation `universal_ner_2024' on page 2 undefined on in\nput line 89.\n\n\nPackage natbib Warning: Citation `llmpee_2024' on page 2 undefined on input lin\ne 90.\n\n\nPackage natbib Warning: Citation `few_nerd_2021' on page 2 undefined on input l\nine 94.\n\n\nPackage natbib Warning: Citation `maven_2020' on page 2 undefined on input line\n 94.\n\n[2]\n\nLaTeX Warning: Reference `sec:crossmodel' on page 3 undefined on input line 117\n.\n\n\nOverfull \\hbox (47.46207pt too wide) in paragraph at lines 132--135\n\\OT1/cmr/m/n/10.95 Con-fus-abil-ity Score, BCS) av-er-ages SCS across all co-pr\nesent types: $[](\\OML/cmm/m/it/10.95 t[]\\OT1/cmr/m/n/10.95 ) = [] [][] [](\\OML/\ncmm/m/it/10.95 t[]; t[]\\OT1/cmr/m/n/10.95 )$. \n\nLaTeX Warning: Reference `tab:pairwise_matrix' on page 3 undefined on input lin\ne 164.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 3 undefined on input line 175\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:scs_validation' on page 4 undefined on input line\n 221.\n\n\nLaTeX Warning: Reference `tab:pairwise_matrix' on page 4 undefined on input lin\ne 260.\n\n[4]\n\nLaTeX Warning: Reference `tab:maven_count' on page 5 undefined on input line 29\n5.\n\n\nLaTeX Warning: Reference `tab:docred_count' on page 5 undefined on input line 3\n20.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\mathsurround' on input line 344.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\z@' on input line 344.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 344.\n\n\nLaTeX Warning: Reference `tab:maven_within_count' on page 5 undefined on input \nline 349.\n\n\nLaTeX Warning: Reference `sec:finding3' on page 5 undefined on input line 367.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n(/usr/share/texlive/texmf-dist/tex/latex/base/omscmr.fd) [5]\n\nLaTeX Warning: Reference `tab:type_sub_bcs' on page 6 undefined on input line 4\n38.\n\n\nLaTeX Warning: Reference `tab:maven_pertype' on page 6 undefined on input line \n487.\n\n[6]\n\nLaTeX Warning: Reference `sec:within_count' on page 7 undefined on input line 5\n16.\n\n\nLaTeX Warning: Reference `sec:finding1' on page 7 undefined on input line 544.\n\n\nLaTeX Warning: Reference `app:sdgd' on page 7 undefined on input line 546.\n\n[7]\n\nLaTeX Warning: Reference `tab:sdgd_main' on page 8 undefined on input line 560.\n\n\n[8] [9]\n\nLaTeX Warning: Reference `sec:finding4' on page 10 undefined on input line 653.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (1.7898pt too wide) in paragraph at lines 723--726\n\\OT1/cmr/m/n/10.95 con-fu-sion pairs. The em-pir-i-cal con-fu-sion ma-trix cor-\nre-lates weakly with em-bed-ding SCS ($\\OML/cmm/m/it/10.95 ^^Z[]\\OT1/cmr/m/n/10\n.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 125$,\n[10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11]\n\nPackage natbib Warning: There were undefined citations.\n\n[12] [13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam1\n0.pfb>\nOutput written on paper.pdf (13 pages, 276804 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (3.55803pt too wide) in paragraph at lines 61--64\n[]\\OT1/cmr/bx/n/10.95 Pairwise con-fus-abil-ity pre-dicts type con-fu-sion\\OT1/\ncmr/m/n/10.95 , but the ef-fect is model- and embedding-\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (13.15128pt too wide) in paragraph at lines 68--71\n[]\\OT1/cmr/bx/n/10.95 Per-type con-fus-abil-ity ag-gre-ga-tion is con-founded \\\nOT1/cmr/m/n/10.95 in se-man-ti-cally ho-mo-ge-neous schemas.\n[2]\nOverfull \\hbox (47.46207pt too wide) in paragraph at lines 132--135\n\\OT1/cmr/m/n/10.95 Con-fus-abil-ity Score, BCS) av-er-ages SCS across all co-pr\nesent types: $[](\\OML/cmm/m/it/10.95 t[]\\OT1/cmr/m/n/10.95 ) = [] [][] [](\\OML/\ncmm/m/it/10.95 t[]; t[]\\OT1/cmr/m/n/10.95 )$. \n[3] [4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\mathsurround' on input line 344.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\z@' on input line 344.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 344.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 372.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 372.\n\n(/usr/share/texlive/texmf-dist/tex/latex/base/omscmr.fd) [5] [6] [7] [8]\n[9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (1.7898pt too wide) in paragraph at lines 723--726\n\\OT1/cmr/m/n/10.95 con-fu-sion pairs. The em-pir-i-cal con-fu-sion ma-trix cor-\nre-lates weakly with em-bed-ding SCS ($\\OML/cmm/m/it/10.95 ^^Z[]\\OT1/cmr/m/n/10\n.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 125$,\n[10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11] [12] [13] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmcsc10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam1\n0.pfb>\nOutput written on paper.pdf (13 pages, 280549 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2307c678-b297-4156-9028-9939a9b761c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "a876f80a-f193-4fd8-8bc9-0b9e732e2f8a",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Assistant

_source line 28 · 2026-05-15T12:22:11.871Z_

编译成功，生成 13 页 PDF，无错误（仅有少量 overfull hbox 警告）。

论文结构：
- **正文**：Abstract, Introduction, Related Work, Experimental Setup, 4 个 Findings（pairwise confusability, multi-channel degradation, centrality confound, decomposition failure）, Discussion, Conclusion
- **附录**：SDGD 全部实验详细结果（SDGD-zero/cal on Few-NERD/MAVEN, random batching ablation, per-type splitting ablation）
- 覆盖了 `experiment_data.json` 中全部 12 个实验 + cross-experiment summary，每个实验有对应的 section 和 table
- 所有数字均来自实验数据，无编造

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a876f80a-f193-4fd8-8bc9-0b9e732e2f8a",
  "isSidechain": false,
  "requestId": "req_011Cb4M2dKQatVTHo8ALtj2T",
  "type": "assistant",
  "uuid": "692ea173-0796-40b7-8719-9a254a981523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nqu8Xa2xhqWBmEzVKr8voW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9165,
      "cache_read_input_tokens": 64023,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 64023,
          "cache_creation_input_tokens": 9165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9165
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T113743 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "692ea173-0796-40b7-8719-9a254a981523",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper",
  "sessionId": "6d7a5a19-b1bd-4793-b072-30ea1d0ec2fd"
}
```

---
