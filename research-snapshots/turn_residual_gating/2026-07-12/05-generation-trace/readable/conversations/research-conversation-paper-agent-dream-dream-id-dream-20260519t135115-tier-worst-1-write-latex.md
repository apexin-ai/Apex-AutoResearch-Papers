# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/063c223b-1298-4925-9492-76a20e766aab.jsonl`
- **Structured JSON:** [`a916e7a97ba6f97a8a1d.json`](../../sessions/a9/a916e7a97ba6f97a8a1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T14:21:34.470Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T14:21:34.470Z",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：\"Structural barrier\" claim 不成立。Reframe 为 Qwen 单模型深度案例研究： \"failure mode taxonomy of residual gating under NTP dominance\"。 Llama-3 差异变成 \"architecture-dependent susceptibility\" 的分析点。 Held-out eval 暴露训练 eval 的 memorization 成分，30x gap 缩至 ~8x， 但仍存在 meaningful gap (≥5x) 可支撑弱化版 claim。 梯度冲突数据 noisy，无法作为独立 claim，降级为辅助证据。 论文降为 Findings 2.5-3.0，需靠方法论贡献 (v1-v7 设计空间 + 四路消融) 和 Qwen 上的 detailed mechanistic case study 撑住。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T14:21:34.473Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T14:21:34.473Z",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-19T14:21:34.493Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance："Structural barrier" claim 不成立。Reframe 为 Qwen 单模型深度案例研究： "failure mode taxonomy of residual gating under NTP dominance"。 Llama-3 差异变成 "architecture-dependent susceptibility" 的分析点。 Held-out eval 暴露训练 eval 的 memorization 成分，30x gap 缩至 ~8x， 但仍存在 meaningful gap (≥5x) 可支撑弱化版 claim。 梯度冲突数据 noisy，无法作为独立 claim，降级为辅助证据。 论文降为 Findings 2.5-3.0，需靠方法论贡献 (v1-v7 设计空间 + 四路消融) 和 Qwen 上的 detailed mechanistic case study 撑住。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "e55b4227-ba37-408f-ab77-6957bfde5443",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T14:21:34.492Z_

```json
{
  "parentUuid": "e55b4227-ba37-408f-ab77-6957bfde5443",
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
  "uuid": "99dc8b40-a291-4919-813b-04fb15e0677b",
  "timestamp": "2026-05-19T14:21:34.492Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T14:21:34.492Z_

```json
{
  "parentUuid": "99dc8b40-a291-4919-813b-04fb15e0677b",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "5c5eab89-f72b-43e4-9a4a-76b218d0427e",
  "timestamp": "2026-05-19T14:21:34.492Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T14:21:34.492Z_

```json
{
  "parentUuid": "5c5eab89-f72b-43e4-9a4a-76b218d0427e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7eb97cab-cb3c-4c6d-aa69-a5e9ba772c03",
  "timestamp": "2026-05-19T14:21:34.492Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper with residual gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Assistant

_source line 8 · 2026-05-19T14:21:37.260Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eb97cab-cb3c-4c6d-aa69-a5e9ba772c03",
  "isSidechain": false,
  "requestId": "req_011CbC5P9FwvpXvFCjukHiqC",
  "type": "assistant",
  "uuid": "3c4bf259-d799-4ac5-bdb3-374bcd7cabae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kLdQptvQLKwke8tLq6dsA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12157,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12157
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

_source line 9 · 2026-05-19T14:21:38.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PZ2hE5MTZ5EQTLVMt21f3W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4bf259-d799-4ac5-bdb3-374bcd7cabae",
  "isSidechain": false,
  "requestId": "req_011CbC5P9FwvpXvFCjukHiqC",
  "type": "assistant",
  "uuid": "74e4d828-9209-4664-9c4b-87ba5c58baa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kLdQptvQLKwke8tLq6dsA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12157,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12157
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

_source line 10 · 2026-05-19T14:21:38.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_014imGgB2hazCUkmQvmJGSK4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74e4d828-9209-4664-9c4b-87ba5c58baa9",
  "isSidechain": false,
  "requestId": "req_011CbC5P9FwvpXvFCjukHiqC",
  "type": "assistant",
  "uuid": "9d2850aa-4d33-4419-a2b5-dd850942f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kLdQptvQLKwke8tLq6dsA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12157,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12157
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

_source line 11 · 2026-05-19T14:21:38.589Z_

<details><summary>↩ Tool result · `toolu_01PZ2hE5MTZ5EQTLVMt21f3W`</summary>

```text
1	[
2	  {
3	    "name": "Gradient conflict analysis (Qwen v7)",
4	    "description": "在 v7 的 3 个 epoch checkpoint 上测量每层 gate 参数的 NTP vs GAR 梯度余弦相似度和幅度比，量化两个 loss 的竞争关系。\n",
5	    "results": {
6	      "epoch0_ckpt_cos_sim_mean": -0.031,
7	      "epoch0_ckpt_cos_sim_std": 0.042,
8	      "epoch1_ckpt_cos_sim_mean": 0.008,
9	      "epoch1_ckpt_cos_sim_std": 0.038,
10	      "epoch2_ckpt_cos_sim_mean": -0.019,
11	      "epoch2_ckpt_cos_sim_std": 0.045,
12	      "cross_checkpoint_sign_stable_layers": 9,
13	      "cross_checkpoint_sign_flip_layers": 19,
14	      "epoch0_mag_ratio_mean": 5.2,
15	      "epoch1_mag_ratio_mean": 3.8,
16	      "epoch2_mag_ratio_mean": 6.1,
17	      "mag_ratio_range": "[2.1, 7.8]",
18	      "layers_with_consistent_negative_cos": "[L3, L4, L12, L14, L20, L23, L9, L8, L11]",
19	      "layers_with_consistent_positive_cos": "[L1, L26, L27]",
20	      "layers_with_sign_flip": "[L0, L2, L5, L6, L7, L10, L13, L15, L16, L17, L18, L19, L21, L22, L24, L25]"
21	    },
22	    "tables": [
23	      {
24	        "table_id": "T_grad_conflict",
25	        "caption": "Per-layer NTP vs GAR gradient statistics across 3 epoch checkpoints",
26	        "columns": [
27	          "Layer",
28	          "Epoch0 cos_sim",
29	          "Epoch1 cos_sim",
30	          "Epoch2 cos_sim",
31	          "Sign stable?",
32	          "Avg mag_ratio"
33	        ],
34	        "sample_rows": [
35	          [
36	            "L3",
37	            -0.048,
38	            -0.022,
39	            -0.041,
40	            "Yes (neg)",
41	            5.8
42	          ],
43	          [
44	            "L4",
45	            -0.052,
46	            -0.018,
47	            -0.039,
48	            "Yes (neg)",
49	            6.2
50	          ],
51	          [
52	            "L14",
53	            -0.039,
54	            -0.011,
55	            -0.028,
56	            "Yes (neg)",
57	            4.9
58	          ],
59	          [
60	            "L1",
61	            0.021,
62	            0.035,
63	            0.018,
64	            "Yes (pos)",
65	            3.1
66	          ],
67	          [
68	            "L15",
69	            -0.018,
70	            0.029,
71	            -0.007,
72	            "No",
73	            4.5
74	          ],
75	          [
76	            "L22",
77	            0.012,
78	            -0.031,
79	            0.008,
80	            "No",
81	            5.3
82	          ]
83	        ]
84	      }
85	    ],
86	    "figures": [],
87	    "analysis": "梯度冲突数据的 noisy 本质意味着 SP2 (\"NTP-GAR 梯度竞争的逐层量化\") 需要 大幅弱化。不能说 \"系统性梯度冲突导致 gate 反向学习\"，只能说 \"NTP 梯度幅度 显著大于 GAR (3-6x)，在部分层和训练阶段存在方向冲突，为 NTP dominance 提供了部分解释\"。这削弱了论文的第二大卖点，需要在 Analysis section 加入更多 caveats。幅度比的存在仍支持 \"NTP dominates gate updates\" 的 弱版本 claim。\n\n\n在 worst 档下，梯度冲突信号存在但极度 noisy。cos_sim 均值在 [-0.05, 0.05] 之间波动，跨 checkpoint 符号不稳定（19/28 层出现符号翻转）。这意味着： (1) 不能 claim \"NTP 和 GAR 梯度系统性冲突\"——只能说 \"在部分层和部分训练阶段 存在冲突趋势\"；(2) 幅度比仍显示 NTP 梯度 ~3-6x 大于 GAR 梯度，但这个 ratio 不如预期的 7-15x 那么 dramatic；(3) epoch1 的 cos_sim 甚至变为正值，暗示 在训练中期 NTP 和 GAR 梯度可能短暂对齐（GAR 快速上升阶段），只在 epoch0 和 epoch2 呈现弱冲突。整体上，梯度冲突不能作为独立的 mechanistic claim， 只能作为 gate 反向 turn conditioning (NF1) 的辅助解释之一。\n"
88	  },
89	  {
90	    "name": "Attention heatmap visualization",
91	    "description": "4 个模型 (Base/TG/UG/LoRA-only) x 3 conversations x 28 layers 的 attention heatmap，可视化各模型对 goal tokens 的 attention 分布差异。\n",
92	    "results": {
93	      "base_goal_attention_pattern": "diffuse, declining over turns",
94	      "tg_goal_attention_pattern": "similar to LoRA-only; no visible gate-driven enhancement at late turns",
95	      "ug_goal_attention_pattern": "nearly identical to TG",
96	      "lora_goal_attention_pattern": "slightly sharper than base at early turns, same decay",
97	      "tg_vs_lora_visual_diff": "indistinguishable at turns 10+",
98	      "layers_with_any_visible_diff": "[L3, L4, L12]",
99	      "layers_with_no_diff": "remaining 25 layers",
100	      "cross_conversation_consistency": "low — pattern varies substantially across 3 conversations"
101	    },
102	    "tables": [],
103	    "figures": [],
104	    "analysis": "Attention heatmap 不会成为论文的亮点图。它们确认了四路消融的定量结果 （gating 无增量贡献），但不提供额外的 mechanistic insight。建议将 heatmap 降级为 appendix figure，主 analysis section 用定量的 GAR/PPL 对比表 + gate profile 图即可。跨 conversation 的不一致性 是一个小 concern——需要在论文中承认 attention pattern 的 high variance， 并说明为什么 GAR 作为 aggregated metric 比 individual heatmap 更可靠。\n\n\n在 worst 档下，attention heatmap 不会产生 compelling 的视觉叙事。因为： (1) 推理时 gate attenuation 仅 2-7%，对 attention pattern 的实际影响 极小，肉眼难以区分 TG vs LoRA-only；(2) Base model 本身的 attention pattern 高度 variable（跨 conversation 不一致），使得对比图缺乏 clean signal；(3) 仅在 gate 值最低的 L3/L4 层可能看到微弱差异， 但差异幅度在 noise 范围内。这些 heatmap 只能放在 appendix 作为 supplementary evidence，不能作为主图。\n"
105	  },
106	  {
107	    "name": "Held-out eval (50 convs, idx>=8000)",
108	    "description": "用 UltraChat 中 idx>=8000 的 50 条全新对话重跑四路 eval， 检验训练 eval 上的 30x gap 是否存在 memorization confound。\n",
109	    "results": {
110	      "heldout_base_dongre_mid_gar": 0.0028,
111	      "heldout_tg_dongre_mid_gar": 0.032,
112	      "heldout_ug_dongre_mid_gar": 0.029,
113	      "heldout_lora_dongre_mid_gar": 0.022,
114	      "heldout_tg_training_gar": 0.48,
115	      "heldout_gap_ratio": 15,
116	      "heldout_tg_minus_lora_dongre_gar": 0.01,
117	      "heldout_tg_minus_lora_significant": "marginal (p=0.08, paired t-test)",
118	      "heldout_base_ours_mid_gar": 0.0095,
119	      "heldout_tg_ours_mid_gar": 0.038,
120	      "heldout_ug_ours_mid_gar": 0.035,
121	      "heldout_lora_ours_mid_gar": 0.028,
122	      "heldout_base_ppl": 4.35,
123	      "heldout_tg_ppl": 2.71,
124	      "heldout_ug_ppl": 2.68,
125	      "heldout_lora_ppl": 2.69,
126	      "original_tg_dongre_mid_gar": 0.0157,
127	      "original_gap_ratio": 30,
128	      "gap_ratio_change": "30x → 15x (held-out TG GAR 翻倍)"
129	    },
130	    "tables": [
131	      {
132	        "table_id": "T_heldout_4way",
133	        "caption": "Four-way eval on held-out conversations (n=50, UltraChat idx≥8000)",
134	        "columns": [
135	          "Model",
136	          "GAR-Dongre mid",
137	          "GAR-Ours mid",
138	          "PPL",
139	          "Recovery (pp)"
140	        ],
141	        "sample_rows": [
142	          [
143	            "Base",
144	            0.0028,
145	            0.0095,
146	            4.35,
147	            "-"
148	          ],
149	          [
150	            "TG (v7)",
151	            0.032,
152	            0.038,
153	            2.71,
154	            2.92
155	          ],
156	          [
157	            "UG",
158	            0.029,
159	            0.035,
160	            2.68,
161	            2.62
162	          ],
163	          [
164	            "LoRA-only",
165	            0.022,
166	            0.028,
167	            2.69,
168	            1.92
169	          ]
170	        ]
171	      },
172	      {
173	        "table_id": "T_gap_comparison",
174	        "caption": "Training-inference GAR gap: original eval vs held-out",
175	        "columns": [
176	          "Eval set",
177	          "Training GAR",
178	          "Inference GAR (TG Dongre)",
179	          "Gap ratio"
180	        ],
181	        "sample_rows": [
182	          [
183	            "Original (n=5)",
184	            0.48,
185	            0.0157,
186	            "30.6x"
187	          ],
188	          [
189	            "Held-out (n=50)",
190	            0.48,
191	            0.032,
192	            "15.0x"
193	          ]
194	        ]
195	      }
196	    ],
197	    "figures": [],
198	    "analysis": "Held-out eval 是 worst 档下最大的 narrative 冲击。两个后果： (1) 30x→15x 需要重写 abstract/intro 中所有引用 \"30x\" 的地方。15x 仍然 dramatic enough 支撑 distribution shift story，但不如 30x 那么 catchy。 需要改为 \"15-30x depending on eval set\" 的表述。 (2) TG > LoRA-only (Δ=0.010, p=0.08) 更麻烦。必须在论文中正面 address： \"On held-out data, ThreadGate shows a marginal but non-significant advantage, suggesting that gating may capture a small real signal that is amplified by memorization on the training eval set.\" 这把 C4 从 \"zero contribution\" 弱化为 \"negligible contribution\"。对论文整体 narrative 不致命但增加 reviewer 攻击面。\n\n\n在 worst 档下，held-out eval 暴露了两个 confound： (1) 训练 eval 上的 TG dongre GAR (0.0157) 被 training data proximity 压低了—— held-out 上反而更高 (0.032)，因为 held-out conversations 的 topic 分布 略有不同，TG 的微弱 attention 干预在某些 topic 上意外有效。这使得 30x gap 缩至 ~15x。虽然 15x 仍然很大，但 narrative 从 \"完全不泛化\" 变成 \"严重但非完全的泛化失败\"，弱化了 C2 的 dramatic 程度。 (2) 更致命的是，TG 在 held-out 上展现出对 LoRA-only 微弱但一致的增量优势 (Δ=0.010, p=0.08)。虽然不显著，但方向一致且跨多个 conversation 可见。 这直接挑战了 \"gating provides zero incremental contribution\" 的 claim (C4)。 在 worst 档下，审稿人会抓住这个 marginal positive 说 \"gating 可能有微弱效果， 你的 negative result 不够 clean\"。 PPL 在 held-out 上稳定，排除 NTP 质量的 confound。 整体效果：30x → 15x 仍支持 distribution shift story 但弱化； TG > LoRA-only 的微弱增量迫使论文承认 \"gating 非零贡献\" 的可能性。\n"
199	  },
200	  {
201	    "name": "Llama-3.1-8B Phase 1 GAR diagnosis",
202	    "description": "在 Llama-3.1-8B 上复现 Phase 1 GAR 衰减诊断，确认 GAR decay 是否跨模型存在。\n",
203	    "results": {
204	      "llama3_turn1_avg_gar": 0.0285,
205	      "llama3_mid_turns_avg_gar": 0.0148,
206	      "llama3_relative_drop": 0.481,
207	      "llama3_num_conversations": 5,
208	      "llama3_num_turns": 10,
209	      "llama3_per_turn_avg_gar": [
210	        0.0285,
211	        0.0221,
212	        0.0198,
213	        0.0172,
214	        0.0155,
215	        0.0142,
216	        0.0131,
217	        0.0128,
218	        0.0135,
219	        0.0119
220	      ],
221	      "qwen_relative_drop_comparison": 0.708,
222	      "llama3_decay_shape": "gradual linear, no sharp drop"
223	    },
224	    "tables": [
225	      {
226	        "table_id": "T_llama3_gar_diag",
227	        "caption": "Llama-3.1-8B GAR degradation across 10 turns (n=5 conversations)",
228	        "columns": [
229	          "Turn",
230	          "Avg GAR",
231	          "Relative to Turn 1"
232	        ],
233	        "sample_rows": [
234	          [
235	            1,
236	            0.0285,
237	            "1.00"
238	          ],
239	          [
240	            5,
241	            0.0155,
242	            "0.54"
243	          ],
244	          [
245	            10,
246	            0.0119,
247	            "0.42"
248	          ]
249	        ]
250	      }
251	    ],
252	    "figures": [],
253	    "analysis": "Llama-3 的 GAR decay 比 Qwen 温和 ~30 个百分点，说明 GAR 衰减的严重程度 确实是 architecture-dependent。这不否认问题的存在，但否认了 \"universal structural phenomenon\" 的强 claim。论文需要改为 \"GAR degradation exists across architectures but varies in severity\"。\n\n\nLlama-3.1-8B 的 GAR decay 存在但显著弱于 Qwen。原因： (1) Llama-3 的 attention 架构 (GQA with 8 KV heads vs Qwen 的 GQA) 可能天然对 goal token 的 attention 更 robust；(2) Llama-3 的预训练 数据分布可能使其在多轮对话中保持更均匀的 attention 分布； (3) 48% 的 relative drop 虽然存在，但远低于 Qwen 的 71%，且衰减 曲线是 gradual linear 而非 Qwen 的 sharp early drop。 在 worst 档下，这意味着 \"GAR 衰减的严重程度是 architecture-dependent\"， 直接挑战了 \"structural phenomenon\" 的 universality claim。但 GAR 衰减确实存在 (48% 仍然是有意义的)，可以重新框架为 \"susceptibility varies by architecture\"。\n"
254	  },
255	  {
256	    "name": "Llama-3.1-8B ThreadGate v7 training",
257	    "description": "在 Llama-3.1-8B 上复制 Qwen v7 的 ThreadGate 训练 setup (MSE+gate_div, 3 epochs)。\n",
258	    "results": {
259	      "llama3_tg_training_gar_peak": 0.09,
260	      "llama3_tg_convergence_phase": "A(gs0-100):plateau@0.01 B(gs100-200):slow_rise C(gs200+):plateau@0.09",
261	      "llama3_tg_epochs_completed": 3,
262	      "llama3_tg_final_avg_ntp": 0.78,
263	      "llama3_tg_final_avg_gar": 0.008,
264	      "llama3_tg_final_gate_mean": 0.962,
265	      "llama3_tg_final_gate_std": 0.028,
266	      "llama3_tg_final_gate_min": 0.891,
267	      "llama3_tg_final_gate_max": 0.996,
268	      "llama3_tg_training_time_hours": 7.2,
269	      "llama3_tg_phase_transition": "weak — no sharp phase B like Qwen",
270	      "llama3_tg_gate_profile_L3": 0.891,
271	      "llama3_tg_gate_profile_L4": 0.903,
272	      "llama3_gate_reversed_layers": 11,
273	      "llama3_gate_reversed_layers_frac": 0.34
274	    },
275	    "tables": [
276	      {
277	        "table_id": "T_llama3_tg_training",
278	        "caption": "Llama-3.1-8B ThreadGate v7 training dynamics",
279	        "columns": [
280	          "Metric",
281	          "Llama-3",
282	          "Qwen (reference)"
283	        ],
284	        "sample_rows": [
285	          [
286	            "Training GAR peak",
287	            0.09,
288	            0.48
289	          ],
290	          [
291	            "Gate mean (final)",
292	            0.962,
293	            0.934
294	          ],
295	          [
296	            "Gate std (final)",
297	            0.028,
298	            0.049
299	          ],
300	          [
301	            "Reversed layers frac",
302	            "34%",
303	            "96%"
304	          ],
305	          [
306	            "Phase transition",
307	            "weak/absent",
308	            "sharp at gs75-144"
309	          ]
310	        ]
311	      }
312	    ],
313	    "figures": [],
314	    "analysis": "Llama-3 的训练不收敛（GAR peak 仅 0.09）是 worst 档的核心问题。 这可以解读为：(a) MSE+gate_div loss 设计是 Qwen-specific 的，不 transfer 到 Llama → 弱化 \"principled loss design\" 的 claim；(b) Llama-3 的 NTP dominance 更强（NTP loss 更低、梯度更大），gates 更难 escape NTP control → 支持 \"NTP dominance\" story 但无法用 GAR gap 量化（因为 训练 GAR 本身就很低）。论文需要承认这个差异，并将其 reframe 为 \"training convergence itself is architecture-dependent\"。\n\n\n在 worst 档下，Llama-3 的 ThreadGate 训练严重受阻： (1) 训练 GAR 仅达到 0.09（Qwen 达 0.48），因为 Llama-3 的 NTP loss landscape 更平坦，gate 更难找到能提升 GAR 的干预方向； (2) 没有 Qwen 上清晰的三阶段动力学——Phase B 的 rapid rise 变成 缓慢爬升，暗示 MSE+gate_div loss 设计可能不是 Llama-3 的最优方案； (3) gate mean 更高 (0.962 vs Qwen 0.934)，gate std 更小 (0.028 vs 0.049)， 说明 gates 几乎没有学到有意义的 layer-selective behavior； (4) 只有 11/32 层出现 gate reversal（Qwen 是 27/28），说明 NF1 (反向 turn conditioning) 在 Llama 上不 universal，部分层的 gate 甚至朝 \"正确\" 方向微弱调整。 这使得 \"gate reversal 是 NTP dominance 的必然结果\" 这一 claim 不成立， gate behavior 变成 architecture-dependent。\n"
315	  },
316	  {
317	    "name": "Llama-3.1-8B LoRA-only training",
318	    "description": "Llama-3.1-8B 上的 LoRA-only 消融（无 gating），作为 cross-model gating redundancy 验证的基准。\n",
319	    "results": {
320	      "llama3_lora_epochs_completed": 3,
321	      "llama3_lora_global_steps": 3000,
322	      "llama3_lora_training_time_hours": 7.0,
323	      "llama3_lora_final_ntp_loss": 0.77,
324	      "llama3_lora_final_lora_size_mb": 20
325	    },
326	    "tables": [],
327	    "figures": [],
328	    "analysis": "LoRA-only 作为 baseline 无 surprise。关键对比在 plan_012 的 eval 中。\n\n\nLoRA-only training 在 Llama-3 上正常完成，与 Qwen 类似。LoRA 在 Llama-3 上的 NTP loss 收敛更好 (0.77 vs Qwen 0.95)，可能因为 Llama-3 的 base NTP 性能和 LoRA 适配效率不同。这本身不是问题—— 它为 plan_012 的 3-way eval 提供一个 clean baseline。\n"
329	  },
330	  {
331	    "name": "Llama-3.1-8B 3-way eval",
332	    "description": "Llama-3.1-8B 上 Base/TG/LoRA-only 的 3-way eval（GAR + PPL）， 使用 held-out data。\n",
333	    "results": {
334	      "llama3_base_dongre_mid_gar": 0.0135,
335	      "llama3_tg_dongre_mid_gar": 0.038,
336	      "llama3_lora_dongre_mid_gar": 0.025,
337	      "llama3_tg_gap_ratio": 2.4,
338	      "llama3_tg_minus_lora_dongre_gar": 0.013,
339	      "llama3_tg_minus_lora_significant": "marginal (p=0.06)",
340	      "llama3_base_ppl": 3.85,
341	      "llama3_tg_ppl": 2.48,
342	      "llama3_lora_ppl": 2.42,
343	      "llama3_tg_ppl_penalty": 0.06,
344	      "llama3_base_ours_mid_gar": 0.0182,
345	      "llama3_tg_ours_mid_gar": 0.045,
346	      "llama3_lora_ours_mid_gar": 0.031
347	    },
348	    "tables": [
349	      {
350	        "table_id": "T_llama3_3way_eval",
351	        "caption": "Llama-3.1-8B 3-way eval (Base/TG/LoRA-only)",
352	        "columns": [
353	          "Model",
354	          "GAR-Dongre mid",
355	          "GAR-Ours mid",
356	          "PPL",
357	          "Training GAR",
358	          "Gap ratio"
359	        ],
360	        "sample_rows": [
361	          [
362	            "Base",
363	            0.0135,
364	            0.0182,
365	            3.85,
366	            "-",
367	            "-"
368	          ],
369	          [
370	            "TG (v7)",
371	            0.038,
372	            0.045,
373	            2.48,
374	            0.09,
375	            "2.4x"
376	          ],
377	          [
378	            "LoRA-only",
379	            0.025,
380	            0.031,
381	            2.42,
382	            "-",
383	            "-"
384	          ]
385	        ]
386	      },
387	      {
388	        "table_id": "T_crossmodel_comparison",
389	        "caption": "Cross-model comparison: Qwen vs Llama-3",
390	        "columns": [
391	          "Metric",
392	          "Qwen-2.5-7B",
393	          "Llama-3.1-8B"
394	        ],
395	        "sample_rows": [
396	          [
397	            "Training GAR peak",
398	            0.48,
399	            0.09
400	          ],
401	          [
402	            "Inference GAR (TG Dongre)",
403	            "0.016-0.032",
404	            0.038
405	          ],
406	          [
407	            "Gap ratio",
408	            "15-30x",
409	            "2.4x"
410	          ],
411	          [
412	            "TG - LoRA Δ GAR",
413	            "0.002-0.010",
414	            0.013
415	          ],
416	          [
417	            "Gate reversal fraction",
418	            "96%",
419	            "34%"
420	          ],
421	          [
422	            "Base GAR (Dongre mid)",
423	            0.003,
424	            0.0135
425	          ]
426	        ]
427	      }
428	    ],
429	    "figures": [],
430	    "analysis": "Llama-3 eval 的结果迫使论文从 \"universal structural barrier\" 转向 \"architecture-dependent susceptibility\"。具体 reframe： - Qwen 上 GAR gap 15-30x = severe distribution shift - Llama-3 上 GAR gap 2.4x = moderate generalization loss - 两者的差异可能来自 (a) base GAR robustness 不同 (Llama base GAR 4.5x\n  higher), (b) attention 架构差异, (c) pretraining data 差异\n- Gating 的微弱正面增量在两个模型上都出现 (Δ=0.010-0.013)，\n  虽然不显著但挑战 \"zero contribution\" 叙事\n论文需要 reframe：不是 \"gating 无用\"，而是 \"gating 的贡献在 Qwen 上 可忽略、在 Llama 上微弱但一致，overall 不足以 overcome distribution shift 的主要效应\"。\n\n\n在 worst 档下，Llama-3 的 eval 产生最致命的结果： (1) Training-inference GAR gap 仅 2.4x (0.09→0.038)，远低于 Qwen 的 15-30x。虽然 gap 仍存在，但 reviewer 会说 \"2.4x 不算 distribution shift barrier，只是 moderate generalization loss\"； (2) 更致命的是 TG > LoRA-only 0.013 (p=0.06)——gating 在 Llama-3 上 展现出微弱但一致的正面增量贡献。这直接矛盾 \"gating provides zero incremental contribution\" 的 claim。虽然 p>0.05 不显著，但方向 一致 + 两个模型上都出现微弱正面趋势 (Qwen held-out Δ=0.010, Llama-3 Δ=0.013) 构成 convergent weak evidence for gating utility； (3) PPL 上 TG 微弱劣于 LoRA-only (2.48 vs 2.42)，说明 gating 有 小的 NTP 代价，但幅度可忽略； (4) Base model 的 dongre GAR (0.0135) 甚至高于 Qwen base (0.003)， 进一步证实 Llama-3 的 attention 对 goal tokens 天然更 robust。 整体效果：Llama-3 上没有复现 Qwen 的 dramatic failure pattern。 \"Structural barrier\" claim 在跨模型层面不成立。\n"
431	  },
432	  {
433	    "name": "Llama-3.1-8B gradient conflict analysis",
434	    "description": "Llama-3.1-8B 上的 NTP vs GAR 梯度冲突分析，验证梯度竞争是否跨模型存在。\n",
435	    "results": {
436	      "llama3_grad_cos_sim_mean": 0.012,
437	      "llama3_grad_cos_sim_std": 0.048,
438	      "llama3_grad_sign_stable_layers": 7,
439	      "llama3_grad_sign_flip_layers": 25,
440	      "llama3_grad_mag_ratio_mean": 3.2,
441	      "llama3_grad_mag_ratio_range": "[1.8, 5.1]",
442	      "llama3_grad_cos_sim_overall_sign": "positive (not conflicting)"
443	    },
444	    "tables": [
445	      {
446	        "table_id": "T_llama3_grad",
447	        "caption": "Llama-3 vs Qwen gradient conflict comparison",
448	        "columns": [
449	          "Metric",
450	          "Qwen",
451	          "Llama-3"
452	        ],
453	        "sample_rows": [
454	          [
455	            "cos_sim mean",
456	            "-0.031 to +0.008",
457	            "+0.012"
458	          ],
459	          [
460	            "Sign-stable layers",
461	            "9/28 (32%)",
462	            "7/32 (22%)"
463	          ],
464	          [
465	            "mag_ratio mean",
466	            "5.2",
467	            "3.2"
468	          ],
469	          [
470	            "Overall direction",
471	            "weakly conflicting",
472	            "not conflicting"
473	          ]
474	        ]
475	      }
476	    ],
477	    "figures": [],
478	    "analysis": "Llama-3 梯度冲突不复现，彻底否定了 \"model-agnostic NTP-GAR gradient competition\" 作为独立 claim 的可行性。论文必须将梯度冲突分析 scope 限制为 Qwen 上的 observation，在 Discussion 中承认其 architecture-dependence。 SP2 从 \"NTP-GAR 梯度竞争的逐层量化\" 弱化为 \"Qwen 上观察到的 NTP-GAR 梯度不对齐趋势（跨模型不 universal）\"。\n\n\n在 worst 档下，Llama-3 的梯度冲突分析产生最坏结果：cos_sim 均值为正 (0.012)， 意味着 NTP 和 GAR 梯度在 Llama-3 上平均不冲突甚至微弱对齐。这与 Qwen 上 的微弱负 cos_sim (-0.031 to -0.019) 方向相反。原因： (1) Llama-3 训练 GAR 仅达 0.09，GAR loss 在训练后期近乎 saturated， 其梯度方向变得 random（接近零向量加噪声）； (2) 幅度比更低 (3.2x vs Qwen 5.2x)，因为 Llama-3 的 LoRA 适配使 NTP 梯度也相对较小。 结果：梯度冲突在 Llama-3 上不复现，SP2 的 \"model-agnostic gradient competition\" claim 完全不成立。\n"
479	  },
480	  {
481	    "name": "Downstream task sanity check",
482	    "description": "简单的 instruction retention 下游任务：测试模型在多轮对话后是否仍能 执行 system prompt 中的指令（如格式约束、persona 保持）。\n",
483	    "results": {
484	      "base_instruction_retention_turn1": 0.82,
485	      "base_instruction_retention_turn10": 0.61,
486	      "base_retention_drop": 0.256,
487	      "tg_instruction_retention_turn1": 0.84,
488	      "tg_instruction_retention_turn10": 0.63,
489	      "tg_retention_drop": 0.25,
490	      "lora_instruction_retention_turn1": 0.83,
491	      "lora_instruction_retention_turn10": 0.62,
492	      "lora_retention_drop": 0.253,
493	      "tg_vs_lora_retention_diff": 0.01,
494	      "gar_retention_correlation": 0.31,
495	      "gar_retention_correlation_p": 0.18
496	    },
497	    "tables": [
498	      {
499	        "table_id": "T_downstream",
500	        "caption": "Instruction retention across turns (downstream sanity check)",
501	        "columns": [
502	          "Model",
503	          "Turn 1 retention",
504	          "Turn 10 retention",
505	          "Drop"
506	        ],
507	        "sample_rows": [
508	          [
509	            "Base",
510	            0.82,
511	            0.61,
512	            "25.6%"
513	          ],
514	          [
515	            "TG (v7)",
516	            0.84,
517	            0.63,
518	            "25.0%"
519	          ],
520	          [
521	            "LoRA-only",
522	            0.83,
523	            0.62,
524	            "25.3%"
525	          ]
526	        ]
527	      }
528	    ],
529	    "figures": [],
530	    "analysis": "GAR 与下游 task 的弱相关加重了 W3 (\"GAR as sole proxy metric\")。 论文需要在 Limitations 中承认 GAR 是 attention-level 的 proxy 而非 direct performance measure，并在 Discussion 中论证为什么 attention mechanism 的研究仍然有价值（即使与 task performance 的相关不完美）。 正面是：instruction retention 确实衰减，验证了多轮退化是 real problem， 只是 GAR 不是它的 perfect proxy。\n\n在 worst 档下，downstream task 结果 mixed： (1) Instruction retention 确实随 turn 衰减 (~25%)，与 GAR decay 方向 一致，但相关性弱 (r=0.31, p=0.18)。这说明 GAR 不是 instruction retention 的 clean proxy——attention 衰减和 task performance 衰减 之间有关系但不紧密； (2) TG vs LoRA-only 的 retention 差异可忽略 (Δ=0.01)，与 GAR eval 一致（gating 无实质帮助）； (3) 所有 fine-tuned 模型比 base 略好但差异小，说明 LoRA 训练本身 （而非 gating）带来微弱改善。 整体：GAR 与下游 task 的弱相关性是 worst 档的额外风险——reviewer 可能 质疑 \"如果 GAR 和实际 task performance 相关性不强，为什么要关注 GAR？\" 但 25% 的 retention drop 本身是 real 的，只是 GAR 作为其 proxy 不够 precise。\n"
531	  }
532	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e4d828-9209-4664-9c4b-87ba5c58baa9",
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "dbf5ec3a-18a7-4c0f-84e3-c64f3a0fbfc6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Gradient conflict analysis (Qwen v7)\",\n    \"description\": \"在 v7 的 3 个 epoch checkpoint 上测量每层 gate 参数的 NTP vs GAR 梯度余弦相似度和幅度比，量化两个 loss 的竞争关系。\\n\",\n    \"results\": {\n      \"epoch0_ckpt_cos_sim_mean\": -0.031,\n      \"epoch0_ckpt_cos_sim_std\": 0.042,\n      \"epoch1_ckpt_cos_sim_mean\": 0.008,\n      \"epoch1_ckpt_cos_sim_std\": 0.038,\n      \"epoch2_ckpt_cos_sim_mean\": -0.019,\n      \"epoch2_ckpt_cos_sim_std\": 0.045,\n      \"cross_checkpoint_sign_stable_layers\": 9,\n      \"cross_checkpoint_sign_flip_layers\": 19,\n      \"epoch0_mag_ratio_mean\": 5.2,\n      \"epoch1_mag_ratio_mean\": 3.8,\n      \"epoch2_mag_ratio_mean\": 6.1,\n      \"mag_ratio_range\": \"[2.1, 7.8]\",\n      \"layers_with_consistent_negative_cos\": \"[L3, L4, L12, L14, L20, L23, L9, L8, L11]\",\n      \"layers_with_consistent_positive_cos\": \"[L1, L26, L27]\",\n      \"layers_with_sign_flip\": \"[L0, L2, L5, L6, L7, L10, L13, L15, L16, L17, L18, L19, L21, L22, L24, L25]\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_grad_conflict\",\n        \"caption\": \"Per-layer NTP vs GAR gradient statistics across 3 epoch checkpoints\",\n        \"columns\": [\n          \"Layer\",\n          \"Epoch0 cos_sim\",\n          \"Epoch1 cos_sim\",\n          \"Epoch2 cos_sim\",\n          \"Sign stable?\",\n          \"Avg mag_ratio\"\n        ],\n        \"sample_rows\": [\n          [\n            \"L3\",\n            -0.048,\n            -0.022,\n            -0.041,\n            \"Yes (neg)\",\n            5.8\n          ],\n          [\n            \"L4\",\n            -0.052,\n            -0.018,\n            -0.039,\n            \"Yes (neg)\",\n            6.2\n          ],\n          [\n            \"L14\",\n            -0.039,\n            -0.011,\n            -0.028,\n            \"Yes (neg)\",\n            4.9\n          ],\n          [\n            \"L1\",\n            0.021,\n            0.035,\n            0.018,\n            \"Yes (pos)\",\n            3.1\n          ],\n          [\n            \"L15\",\n            -0.018,\n            0.029,\n            -0.007,\n            \"No\",\n            4.5\n          ],\n          [\n            \"L22\",\n            0.012,\n            -0.031,\n            0.008,\n            \"No\",\n            5.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"梯度冲突数据的 noisy 本质意味着 SP2 (\\\"NTP-GAR 梯度竞争的逐层量化\\\") 需要 大幅弱化。不能说 \\\"系统性梯度冲突导致 gate 反向学习\\\"，只能说 \\\"NTP 梯度幅度 显著大于 GAR (3-6x)，在部分层和训练阶段存在方向冲突，为 NTP dominance 提供了部分解释\\\"。这削弱了论文的第二大卖点，需要在 Analysis section 加入更多 caveats。幅度比的存在仍支持 \\\"NTP dominates gate updates\\\" 的 弱版本 claim。\\n\\n\\n在 worst 档下，梯度冲突信号存在但极度 noisy。cos_sim 均值在 [-0.05, 0.05] 之间波动，跨 checkpoint 符号不稳定（19/28 层出现符号翻转）。这意味着： (1) 不能 claim \\\"NTP 和 GAR 梯度系统性冲突\\\"——只能说 \\\"在部分层和部分训练阶段 存在冲突趋势\\\"；(2) 幅度比仍显示 NTP 梯度 ~3-6x 大于 GAR 梯度，但这个 ratio 不如预期的 7-15x 那么 dramatic；(3) epoch1 的 cos_sim 甚至变为正值，暗示 在训练中期 NTP 和 GAR 梯度可能短暂对齐（GAR 快速上升阶段），只在 epoch0 和 epoch2 呈现弱冲突。整体上，梯度冲突不能作为独立的 mechanistic claim， 只能作为 gate 反向 turn conditioning (NF1) 的辅助解释之一。\\n\"\n  },\n  {\n    \"name\": \"Attention heatmap visualization\",\n    \"description\": \"4 个模型 (Base/TG/UG/LoRA-only) x 3 conversations x 28 layers 的 attention heatmap，可视化各模型对 goal tokens 的 attention 分布差异。\\n\",\n    \"results\": {\n      \"base_goal_attention_pattern\": \"diffuse, declining over turns\",\n      \"tg_goal_attention_pattern\": \"similar to LoRA-only; no visible gate-driven enhancement at late turns\",\n      \"ug_goal_attention_pattern\": \"nearly identical to TG\",\n      \"lora_goal_attention_pattern\": \"slightly sharper than base at early turns, same decay\",\n      \"tg_vs_lora_visual_diff\": \"indistinguishable at turns 10+\",\n      \"layers_with_any_visible_diff\": \"[L3, L4, L12]\",\n      \"layers_with_no_diff\": \"remaining 25 layers\",\n      \"cross_conversation_consistency\": \"low — pattern varies substantially across 3 conversations\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Attention heatmap 不会成为论文的亮点图。它们确认了四路消融的定量结果 （gating 无增量贡献），但不提供额外的 mechanistic insight。建议将 heatmap 降级为 appendix figure，主 analysis section 用定量的 GAR/PPL 对比表 + gate profile 图即可。跨 conversation 的不一致性 是一个小 concern——需要在论文中承认 attention pattern 的 high variance， 并说明为什么 GAR 作为 aggregated metric 比 individual heatmap 更可靠。\\n\\n\\n在 worst 档下，attention heatmap 不会产生 compelling 的视觉叙事。因为： (1) 推理时 gate attenuation 仅 2-7%，对 attention pattern 的实际影响 极小，肉眼难以区分 TG vs LoRA-only；(2) Base model 本身的 attention pattern 高度 variable（跨 conversation 不一致），使得对比图缺乏 clean signal；(3) 仅在 gate 值最低的 L3/L4 层可能看到微弱差异， 但差异幅度在 noise 范围内。这些 heatmap 只能放在 appendix 作为 supplementary evidence，不能作为主图。\\n\"\n  },\n  {\n    \"name\": \"Held-out eval (50 convs, idx>=8000)\",\n    \"description\": \"用 UltraChat 中 idx>=8000 的 50 条全新对话重跑四路 eval， 检验训练 eval 上的 30x gap 是否存在 memorization confound。\\n\",\n    \"results\": {\n      \"heldout_base_dongre_mid_gar\": 0.0028,\n      \"heldout_tg_dongre_mid_gar\": 0.032,\n      \"heldout_ug_dongre_mid_gar\": 0.029,\n      \"heldout_lora_dongre_mid_gar\": 0.022,\n      \"heldout_tg_training_gar\": 0.48,\n      \"heldout_gap_ratio\": 15,\n      \"heldout_tg_minus_lora_dongre_gar\": 0.01,\n      \"heldout_tg_minus_lora_significant\": \"marginal (p=0.08, paired t-test)\",\n      \"heldout_base_ours_mid_gar\": 0.0095,\n      \"heldout_tg_ours_mid_gar\": 0.038,\n      \"heldout_ug_ours_mid_gar\": 0.035,\n      \"heldout_lora_ours_mid_gar\": 0.028,\n      \"heldout_base_ppl\": 4.35,\n      \"heldout_tg_ppl\": 2.71,\n      \"heldout_ug_ppl\": 2.68,\n      \"heldout_lora_ppl\": 2.69,\n      \"original_tg_dongre_mid_gar\": 0.0157,\n      \"original_gap_ratio\": 30,\n      \"gap_ratio_change\": \"30x → 15x (held-out TG GAR 翻倍)\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_heldout_4way\",\n        \"caption\": \"Four-way eval on held-out conversations (n=50, UltraChat idx≥8000)\",\n        \"columns\": [\n          \"Model\",\n          \"GAR-Dongre mid\",\n          \"GAR-Ours mid\",\n          \"PPL\",\n          \"Recovery (pp)\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Base\",\n            0.0028,\n            0.0095,\n            4.35,\n            \"-\"\n          ],\n          [\n            \"TG (v7)\",\n            0.032,\n            0.038,\n            2.71,\n            2.92\n          ],\n          [\n            \"UG\",\n            0.029,\n            0.035,\n            2.68,\n            2.62\n          ],\n          [\n            \"LoRA-only\",\n            0.022,\n            0.028,\n            2.69,\n            1.92\n          ]\n        ]\n      },\n      {\n        \"table_id\": \"T_gap_comparison\",\n        \"caption\": \"Training-inference GAR gap: original eval vs held-out\",\n        \"columns\": [\n          \"Eval set\",\n          \"Training GAR\",\n          \"Inference GAR (TG Dongre)\",\n          \"Gap ratio\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Original (n=5)\",\n            0.48,\n            0.0157,\n            \"30.6x\"\n          ],\n          [\n            \"Held-out (n=50)\",\n            0.48,\n            0.032,\n            \"15.0x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Held-out eval 是 worst 档下最大的 narrative 冲击。两个后果： (1) 30x→15x 需要重写 abstract/intro 中所有引用 \\\"30x\\\" 的地方。15x 仍然 dramatic enough 支撑 distribution shift story，但不如 30x 那么 catchy。 需要改为 \\\"15-30x depending on eval set\\\" 的表述。 (2) TG > LoRA-only (Δ=0.010, p=0.08) 更麻烦。必须在论文中正面 address： \\\"On held-out data, ThreadGate shows a marginal but non-significant advantage, suggesting that gating may capture a small real signal that is amplified by memorization on the training eval set.\\\" 这把 C4 从 \\\"zero contribution\\\" 弱化为 \\\"negligible contribution\\\"。对论文整体 narrative 不致命但增加 reviewer 攻击面。\\n\\n\\n在 worst 档下，held-out eval 暴露了两个 confound： (1) 训练 eval 上的 TG dongre GAR (0.0157) 被 training data proximity 压低了—— held-out 上反而更高 (0.032)，因为 held-out conversations 的 topic 分布 略有不同，TG 的微弱 attention 干预在某些 topic 上意外有效。这使得 30x gap 缩至 ~15x。虽然 15x 仍然很大，但 narrative 从 \\\"完全不泛化\\\" 变成 \\\"严重但非完全的泛化失败\\\"，弱化了 C2 的 dramatic 程度。 (2) 更致命的是，TG 在 held-out 上展现出对 LoRA-only 微弱但一致的增量优势 (Δ=0.010, p=0.08)。虽然不显著，但方向一致且跨多个 conversation 可见。 这直接挑战了 \\\"gating provides zero incremental contribution\\\" 的 claim (C4)。 在 worst 档下，审稿人会抓住这个 marginal positive 说 \\\"gating 可能有微弱效果， 你的 negative result 不够 clean\\\"。 PPL 在 held-out 上稳定，排除 NTP 质量的 confound。 整体效果：30x → 15x 仍支持 distribution shift story 但弱化； TG > LoRA-only 的微弱增量迫使论文承认 \\\"gating 非零贡献\\\" 的可能性。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Phase 1 GAR diagnosis\",\n    \"description\": \"在 Llama-3.1-8B 上复现 Phase 1 GAR 衰减诊断，确认 GAR decay 是否跨模型存在。\\n\",\n    \"results\": {\n      \"llama3_turn1_avg_gar\": 0.0285,\n      \"llama3_mid_turns_avg_gar\": 0.0148,\n      \"llama3_relative_drop\": 0.481,\n      \"llama3_num_conversations\": 5,\n      \"llama3_num_turns\": 10,\n      \"llama3_per_turn_avg_gar\": [\n        0.0285,\n        0.0221,\n        0.0198,\n        0.0172,\n        0.0155,\n        0.0142,\n        0.0131,\n        0.0128,\n        0.0135,\n        0.0119\n      ],\n      \"qwen_relative_drop_comparison\": 0.708,\n      \"llama3_decay_shape\": \"gradual linear, no sharp drop\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_llama3_gar_diag\",\n        \"caption\": \"Llama-3.1-8B GAR degradation across 10 turns (n=5 conversations)\",\n        \"columns\": [\n          \"Turn\",\n          \"Avg GAR\",\n          \"Relative to Turn 1\"\n        ],\n        \"sample_rows\": [\n          [\n            1,\n            0.0285,\n            \"1.00\"\n          ],\n          [\n            5,\n            0.0155,\n            \"0.54\"\n          ],\n          [\n            10,\n            0.0119,\n            \"0.42\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama-3 的 GAR decay 比 Qwen 温和 ~30 个百分点，说明 GAR 衰减的严重程度 确实是 architecture-dependent。这不否认问题的存在，但否认了 \\\"universal structural phenomenon\\\" 的强 claim。论文需要改为 \\\"GAR degradation exists across architectures but varies in severity\\\"。\\n\\n\\nLlama-3.1-8B 的 GAR decay 存在但显著弱于 Qwen。原因： (1) Llama-3 的 attention 架构 (GQA with 8 KV heads vs Qwen 的 GQA) 可能天然对 goal token 的 attention 更 robust；(2) Llama-3 的预训练 数据分布可能使其在多轮对话中保持更均匀的 attention 分布； (3) 48% 的 relative drop 虽然存在，但远低于 Qwen 的 71%，且衰减 曲线是 gradual linear 而非 Qwen 的 sharp early drop。 在 worst 档下，这意味着 \\\"GAR 衰减的严重程度是 architecture-dependent\\\"， 直接挑战了 \\\"structural phenomenon\\\" 的 universality claim。但 GAR 衰减确实存在 (48% 仍然是有意义的)，可以重新框架为 \\\"susceptibility varies by architecture\\\"。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B ThreadGate v7 training\",\n    \"description\": \"在 Llama-3.1-8B 上复制 Qwen v7 的 ThreadGate 训练 setup (MSE+gate_div, 3 epochs)。\\n\",\n    \"results\": {\n      \"llama3_tg_training_gar_peak\": 0.09,\n      \"llama3_tg_convergence_phase\": \"A(gs0-100):plateau@0.01 B(gs100-200):slow_rise C(gs200+):plateau@0.09\",\n      \"llama3_tg_epochs_completed\": 3,\n      \"llama3_tg_final_avg_ntp\": 0.78,\n      \"llama3_tg_final_avg_gar\": 0.008,\n      \"llama3_tg_final_gate_mean\": 0.962,\n      \"llama3_tg_final_gate_std\": 0.028,\n      \"llama3_tg_final_gate_min\": 0.891,\n      \"llama3_tg_final_gate_max\": 0.996,\n      \"llama3_tg_training_time_hours\": 7.2,\n      \"llama3_tg_phase_transition\": \"weak — no sharp phase B like Qwen\",\n      \"llama3_tg_gate_profile_L3\": 0.891,\n      \"llama3_tg_gate_profile_L4\": 0.903,\n      \"llama3_gate_reversed_layers\": 11,\n      \"llama3_gate_reversed_layers_frac\": 0.34\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_llama3_tg_training\",\n        \"caption\": \"Llama-3.1-8B ThreadGate v7 training dynamics\",\n        \"columns\": [\n          \"Metric\",\n          \"Llama-3\",\n          \"Qwen (reference)\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Training GAR peak\",\n            0.09,\n            0.48\n          ],\n          [\n            \"Gate mean (final)\",\n            0.962,\n            0.934\n          ],\n          [\n            \"Gate std (final)\",\n            0.028,\n            0.049\n          ],\n          [\n            \"Reversed layers frac\",\n            \"34%\",\n            \"96%\"\n          ],\n          [\n            \"Phase transition\",\n            \"weak/absent\",\n            \"sharp at gs75-144\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama-3 的训练不收敛（GAR peak 仅 0.09）是 worst 档的核心问题。 这可以解读为：(a) MSE+gate_div loss 设计是 Qwen-specific 的，不 transfer 到 Llama → 弱化 \\\"principled loss design\\\" 的 claim；(b) Llama-3 的 NTP dominance 更强（NTP loss 更低、梯度更大），gates 更难 escape NTP control → 支持 \\\"NTP dominance\\\" story 但无法用 GAR gap 量化（因为 训练 GAR 本身就很低）。论文需要承认这个差异，并将其 reframe 为 \\\"training convergence itself is architecture-dependent\\\"。\\n\\n\\n在 worst 档下，Llama-3 的 ThreadGate 训练严重受阻： (1) 训练 GAR 仅达到 0.09（Qwen 达 0.48），因为 Llama-3 的 NTP loss landscape 更平坦，gate 更难找到能提升 GAR 的干预方向； (2) 没有 Qwen 上清晰的三阶段动力学——Phase B 的 rapid rise 变成 缓慢爬升，暗示 MSE+gate_div loss 设计可能不是 Llama-3 的最优方案； (3) gate mean 更高 (0.962 vs Qwen 0.934)，gate std 更小 (0.028 vs 0.049)， 说明 gates 几乎没有学到有意义的 layer-selective behavior； (4) 只有 11/32 层出现 gate reversal（Qwen 是 27/28），说明 NF1 (反向 turn conditioning) 在 Llama 上不 universal，部分层的 gate 甚至朝 \\\"正确\\\" 方向微弱调整。 这使得 \\\"gate reversal 是 NTP dominance 的必然结果\\\" 这一 claim 不成立， gate behavior 变成 architecture-dependent。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B LoRA-only training\",\n    \"description\": \"Llama-3.1-8B 上的 LoRA-only 消融（无 gating），作为 cross-model gating redundancy 验证的基准。\\n\",\n    \"results\": {\n      \"llama3_lora_epochs_completed\": 3,\n      \"llama3_lora_global_steps\": 3000,\n      \"llama3_lora_training_time_hours\": 7.0,\n      \"llama3_lora_final_ntp_loss\": 0.77,\n      \"llama3_lora_final_lora_size_mb\": 20\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"LoRA-only 作为 baseline 无 surprise。关键对比在 plan_012 的 eval 中。\\n\\n\\nLoRA-only training 在 Llama-3 上正常完成，与 Qwen 类似。LoRA 在 Llama-3 上的 NTP loss 收敛更好 (0.77 vs Qwen 0.95)，可能因为 Llama-3 的 base NTP 性能和 LoRA 适配效率不同。这本身不是问题—— 它为 plan_012 的 3-way eval 提供一个 clean baseline。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B 3-way eval\",\n    \"description\": \"Llama-3.1-8B 上 Base/TG/LoRA-only 的 3-way eval（GAR + PPL）， 使用 held-out data。\\n\",\n    \"results\": {\n      \"llama3_base_dongre_mid_gar\": 0.0135,\n      \"llama3_tg_dongre_mid_gar\": 0.038,\n      \"llama3_lora_dongre_mid_gar\": 0.025,\n      \"llama3_tg_gap_ratio\": 2.4,\n      \"llama3_tg_minus_lora_dongre_gar\": 0.013,\n      \"llama3_tg_minus_lora_significant\": \"marginal (p=0.06)\",\n      \"llama3_base_ppl\": 3.85,\n      \"llama3_tg_ppl\": 2.48,\n      \"llama3_lora_ppl\": 2.42,\n      \"llama3_tg_ppl_penalty\": 0.06,\n      \"llama3_base_ours_mid_gar\": 0.0182,\n      \"llama3_tg_ours_mid_gar\": 0.045,\n      \"llama3_lora_ours_mid_gar\": 0.031\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_llama3_3way_eval\",\n        \"caption\": \"Llama-3.1-8B 3-way eval (Base/TG/LoRA-only)\",\n        \"columns\": [\n          \"Model\",\n          \"GAR-Dongre mid\",\n          \"GAR-Ours mid\",\n          \"PPL\",\n          \"Training GAR\",\n          \"Gap ratio\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Base\",\n            0.0135,\n            0.0182,\n            3.85,\n            \"-\",\n            \"-\"\n          ],\n          [\n            \"TG (v7)\",\n            0.038,\n            0.045,\n            2.48,\n            0.09,\n            \"2.4x\"\n          ],\n          [\n            \"LoRA-only\",\n            0.025,\n            0.031,\n            2.42,\n            \"-\",\n            \"-\"\n          ]\n        ]\n      },\n      {\n        \"table_id\": \"T_crossmodel_comparison\",\n        \"caption\": \"Cross-model comparison: Qwen vs Llama-3\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen-2.5-7B\",\n          \"Llama-3.1-8B\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Training GAR peak\",\n            0.48,\n            0.09\n          ],\n          [\n            \"Inference GAR (TG Dongre)\",\n            \"0.016-0.032\",\n            0.038\n          ],\n          [\n            \"Gap ratio\",\n            \"15-30x\",\n            \"2.4x\"\n          ],\n          [\n            \"TG - LoRA Δ GAR\",\n            \"0.002-0.010\",\n            0.013\n          ],\n          [\n            \"Gate reversal fraction\",\n            \"96%\",\n            \"34%\"\n          ],\n          [\n            \"Base GAR (Dongre mid)\",\n            0.003,\n            0.0135\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama-3 eval 的结果迫使论文从 \\\"universal structural barrier\\\" 转向 \\\"architecture-dependent susceptibility\\\"。具体 reframe： - Qwen 上 GAR gap 15-30x = severe distribution shift - Llama-3 上 GAR gap 2.4x = moderate generalization loss - 两者的差异可能来自 (a) base GAR robustness 不同 (Llama base GAR 4.5x\\n  higher), (b) attention 架构差异, (c) pretraining data 差异\\n- Gating 的微弱正面增量在两个模型上都出现 (Δ=0.010-0.013)，\\n  虽然不显著但挑战 \\\"zero contribution\\\" 叙事\\n论文需要 reframe：不是 \\\"gating 无用\\\"，而是 \\\"gating 的贡献在 Qwen 上 可忽略、在 Llama 上微弱但一致，overall 不足以 overcome distribution shift 的主要效应\\\"。\\n\\n\\n在 worst 档下，Llama-3 的 eval 产生最致命的结果： (1) Training-inference GAR gap 仅 2.4x (0.09→0.038)，远低于 Qwen 的 15-30x。虽然 gap 仍存在，但 reviewer 会说 \\\"2.4x 不算 distribution shift barrier，只是 moderate generalization loss\\\"； (2) 更致命的是 TG > LoRA-only 0.013 (p=0.06)——gating 在 Llama-3 上 展现出微弱但一致的正面增量贡献。这直接矛盾 \\\"gating provides zero incremental contribution\\\" 的 claim。虽然 p>0.05 不显著，但方向 一致 + 两个模型上都出现微弱正面趋势 (Qwen held-out Δ=0.010, Llama-3 Δ=0.013) 构成 convergent weak evidence for gating utility； (3) PPL 上 TG 微弱劣于 LoRA-only (2.48 vs 2.42)，说明 gating 有 小的 NTP 代价，但幅度可忽略； (4) Base model 的 dongre GAR (0.0135) 甚至高于 Qwen base (0.003)， 进一步证实 Llama-3 的 attention 对 goal tokens 天然更 robust。 整体效果：Llama-3 上没有复现 Qwen 的 dramatic failure pattern。 \\\"Structural barrier\\\" claim 在跨模型层面不成立。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B gradient conflict analysis\",\n    \"description\": \"Llama-3.1-8B 上的 NTP vs GAR 梯度冲突分析，验证梯度竞争是否跨模型存在。\\n\",\n    \"results\": {\n      \"llama3_grad_cos_sim_mean\": 0.012,\n      \"llama3_grad_cos_sim_std\": 0.048,\n      \"llama3_grad_sign_stable_layers\": 7,\n      \"llama3_grad_sign_flip_layers\": 25,\n      \"llama3_grad_mag_ratio_mean\": 3.2,\n      \"llama3_grad_mag_ratio_range\": \"[1.8, 5.1]\",\n      \"llama3_grad_cos_sim_overall_sign\": \"positive (not conflicting)\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_llama3_grad\",\n        \"caption\": \"Llama-3 vs Qwen gradient conflict comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen\",\n          \"Llama-3\"\n        ],\n        \"sample_rows\": [\n          [\n            \"cos_sim mean\",\n            \"-0.031 to +0.008\",\n            \"+0.012\"\n          ],\n          [\n            \"Sign-stable layers\",\n            \"9/28 (32%)\",\n            \"7/32 (22%)\"\n          ],\n          [\n            \"mag_ratio mean\",\n            \"5.2\",\n            \"3.2\"\n          ],\n          [\n            \"Overall direction\",\n            \"weakly conflicting\",\n            \"not conflicting\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama-3 梯度冲突不复现，彻底否定了 \\\"model-agnostic NTP-GAR gradient competition\\\" 作为独立 claim 的可行性。论文必须将梯度冲突分析 scope 限制为 Qwen 上的 observation，在 Discussion 中承认其 architecture-dependence。 SP2 从 \\\"NTP-GAR 梯度竞争的逐层量化\\\" 弱化为 \\\"Qwen 上观察到的 NTP-GAR 梯度不对齐趋势（跨模型不 universal）\\\"。\\n\\n\\n在 worst 档下，Llama-3 的梯度冲突分析产生最坏结果：cos_sim 均值为正 (0.012)， 意味着 NTP 和 GAR 梯度在 Llama-3 上平均不冲突甚至微弱对齐。这与 Qwen 上 的微弱负 cos_sim (-0.031 to -0.019) 方向相反。原因： (1) Llama-3 训练 GAR 仅达 0.09，GAR loss 在训练后期近乎 saturated， 其梯度方向变得 random（接近零向量加噪声）； (2) 幅度比更低 (3.2x vs Qwen 5.2x)，因为 Llama-3 的 LoRA 适配使 NTP 梯度也相对较小。 结果：梯度冲突在 Llama-3 上不复现，SP2 的 \\\"model-agnostic gradient competition\\\" claim 完全不成立。\\n\"\n  },\n  {\n    \"name\": \"Downstream task sanity check\",\n    \"description\": \"简单的 instruction retention 下游任务：测试模型在多轮对话后是否仍能 执行 system prompt 中的指令（如格式约束、persona 保持）。\\n\",\n    \"results\": {\n      \"base_instruction_retention_turn1\": 0.82,\n      \"base_instruction_retention_turn10\": 0.61,\n      \"base_retention_drop\": 0.256,\n      \"tg_instruction_retention_turn1\": 0.84,\n      \"tg_instruction_retention_turn10\": 0.63,\n      \"tg_retention_drop\": 0.25,\n      \"lora_instruction_retention_turn1\": 0.83,\n      \"lora_instruction_retention_turn10\": 0.62,\n      \"lora_retention_drop\": 0.253,\n      \"tg_vs_lora_retention_diff\": 0.01,\n      \"gar_retention_correlation\": 0.31,\n      \"gar_retention_correlation_p\": 0.18\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T_downstream\",\n        \"caption\": \"Instruction retention across turns (downstream sanity check)\",\n        \"columns\": [\n          \"Model\",\n          \"Turn 1 retention\",\n          \"Turn 10 retention\",\n          \"Drop\"\n        ],\n        \"sample_rows\": [\n          [\n            \"Base\",\n            0.82,\n            0.61,\n            \"25.6%\"\n          ],\n          [\n            \"TG (v7)\",\n            0.84,\n            0.63,\n            \"25.0%\"\n          ],\n          [\n            \"LoRA-only\",\n            0.83,\n            0.62,\n            \"25.3%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GAR 与下游 task 的弱相关加重了 W3 (\\\"GAR as sole proxy metric\\\")。 论文需要在 Limitations 中承认 GAR 是 attention-level 的 proxy 而非 direct performance measure，并在 Discussion 中论证为什么 attention mechanism 的研究仍然有价值（即使与 task performance 的相关不完美）。 正面是：instruction retention 确实衰减，验证了多轮退化是 real problem， 只是 GAR 不是它的 perfect proxy。\\n\\n在 worst 档下，downstream task 结果 mixed： (1) Instruction retention 确实随 turn 衰减 (~25%)，与 GAR decay 方向 一致，但相关性弱 (r=0.31, p=0.18)。这说明 GAR 不是 instruction retention 的 clean proxy——attention 衰减和 task performance 衰减 之间有关系但不紧密； (2) TG vs LoRA-only 的 retention 差异可忽略 (Δ=0.01)，与 GAR eval 一致（gating 无实质帮助）； (3) 所有 fine-tuned 模型比 base 略好但差异小，说明 LoRA 训练本身 （而非 gating）带来微弱改善。 整体：GAR 与下游 task 的弱相关性是 worst 档的额外风险——reviewer 可能 质疑 \\\"如果 GAR 和实际 task performance 相关性不强，为什么要关注 GAR？\\\" 但 25% 的 retention drop 本身是 real 的，只是 GAR 作为其 proxy 不够 precise。\\n\"\n  }\n]",
      "numLines": 532,
      "startLine": 1,
      "totalLines": 532
    }
  },
  "sourceToolAssistantUUID": "74e4d828-9209-4664-9c4b-87ba5c58baa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T14:21:38.484Z_

<details><summary>↩ Tool result · `toolu_014imGgB2hazCUkmQvmJGSK4`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x 断层的定量证据）。这个 insight 对所有在 teacher-forcing 下优化的 attention auxiliary loss 都有警示意义。
4	> Novelty 排序: (1) teacher-forcing→generation 分布偏移 > (2) NTP-GAR 梯度竞争导致 gate 反向学习 > (3) negative result 本身
5	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
6	> 最后更新: 2026-05-19 (Reviewer 评估后 reframe: distribution shift insight 为核心卖点)
7	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
8	
9	---
10	
11	## 1. Title Candidates
12	
13	- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
14	- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference
15	- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue
16	
17	推荐 T1: "Lightweight Gating" 比 "Residual Gating" 覆盖更广（含 uniform gate），"Mechanistic Analysis" 突出 insight 而非 negative result。
18	
19	---
20	
21	## 2. Story Arc
22	
23	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results demonstrate that auxiliary attention losses optimized under teacher-forcing face a fundamental generalization barrier.
24	
25	---
26	
27	## 3. Core Claims
28	
29	| # | Claim | 支撑 | 状态 |
30	|---|-------|------|------|
31	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | 已验证 |
32	| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | 已验证 |
33	| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突实验 (待做) | NF1/NF2/NF3 已验证，梯度冲突量化待做 |
34	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 是否在不改善 GAR 的同时还损害 NTP 质量 | 四路 eval on standard_conversations: GAR + PPL (待做) | 待 eval 确认 |
35	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | 待做 |
36	
37	---
38	
39	## 4. Negative Findings (NF)
40	
41	| # | Finding | 证据 | 叙事角色 |
42	|---|---------|------|----------|
43	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
44	| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |
45	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
46	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
47	
48	---
49	
50	## 5. Key Selling Points
51	
52	**SP1 (核心卖点): Teacher-forcing→generation 分布偏移的定量证据。** 30x training-inference GAR gap 不是 gating 的特有问题，而是所有在 teacher-forcing 下优化 auxiliary attention loss 的方法都面临的结构性障碍。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。这个 insight 超越 residual gating，对整个 attention steering 领域有警示意义。
53	
54	**SP2: NTP-GAR 梯度竞争的逐层量化。** NTP loss 在 gate 参数上的梯度方向与 GAR loss 冲突，且幅度远大于 GAR（定量测量待做）。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。
55	
56	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。
57	
58	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
59	
60	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
61	
62	---
63	
64	## 6. Anticipated Reviewer Concerns
65	
66	| # | 严重度 | 预期质疑 | 回应策略 |
67	|---|--------|----------|----------|
68	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
69	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
70	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
71	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
72	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
73	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
74	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
75	| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
76	
77	---
78	
79	## 7. Dongre et al. 关系定位
80	
81	| 维度 | Dongre et al. | 本文 |
82	|------|---------------|------|
83	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
84	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
85	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
86	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
87	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
88	
89	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
90	
91	共同推论: 两种独立干预路线均失败 → 在 teacher-forcing 下优化的 auxiliary attention loss 面临结构性泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。
92	
93	---
94	
95	## 8. GAR 定义策略
96	
97	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
98	|------|------|------------|----------------|------|
99	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
100	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
101	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
102	
103	两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。
104	
105	---
106	
107	## 9. 论文结构草案
108	
109	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
110	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
111	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
112	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
113	5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
114	6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)
115	7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段
116	8. **Discussion**: 为什么 residual gating 不够 → 对所有 attention steering 方法的启示 → 潜在解决方向 (inference-time intervention / decoupled pathway / GAR-aware decoding)
117	9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议
118	
119	### 贡献列表（按 novelty 排序）
120	
121	1. **Teacher-forcing distribution shift 的定量证据**: 首次量化 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x training-inference GAR gap），对所有在 teacher-forcing 下优化的 attention steering 方法有广泛警示意义
122	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
123	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
124	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
125	
126	---
127	
128	## 10. 竞争力评估（Reviewer 估分 2026-05-19）
129	
130	- **不含 Llama-3**: Findings 3.0（紧绷）。单模型是致命弱点（W1）。
131	- **含 Llama-3 跨模型验证**: 3.0-3.5。distribution shift insight 的泛化性 + 跨模型 convergent evidence 是升级关键。
132	- **冲 Main 条件**: Llama-3 复现 + 梯度冲突量化做扎实 + constructive future directions + 可选的下游任务 sanity check。
133	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "teacher-forcing distribution shift 摧毁了 auxiliary attention loss 的泛化性"（强，对领域有广泛警示意义）。
134	- **风险**: W2（"没调对参数"）和 W5（"exposure bias 已知"）需要在论文中显式 address。
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d2850aa-4d33-4419-a2b5-dd850942f86e",
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "0c70646e-28b3-4339-8656-312ee06ca8ba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x 断层的定量证据）。这个 insight 对所有在 teacher-forcing 下优化的 attention auxiliary loss 都有警示意义。\n> Novelty 排序: (1) teacher-forcing→generation 分布偏移 > (2) NTP-GAR 梯度竞争导致 gate 反向学习 > (3) negative result 本身\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-19 (Reviewer 评估后 reframe: distribution shift insight 为核心卖点)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n\n---\n\n## 1. Title Candidates\n\n- **T1 (推荐)**: Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n- **T2**: The Distribution Shift Trap: Why Training-Time Attention Steering Fails at Inference\n- **T3**: Residual Gating Cannot Recover Goal Attention in Multi-Turn Dialogue\n\n推荐 T1: \"Lightweight Gating\" 比 \"Residual Gating\" 覆盖更广（含 uniform gate），\"Mechanistic Analysis\" 突出 insight 而非 negative result。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Attention Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), but this improvement completely fails to transfer to inference (GAR = 0.016, a 30x gap). Our central finding is that teacher-forcing training creates a fundamental distribution shift: attention patterns learned under teacher-forced contexts do not generalize to autoregressive generation, where the model conditions on its own outputs. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Combined with Dongre et al.'s independent failure of goal re-injection, our results demonstrate that auxiliary attention losses optimized under teacher-forcing face a fundamental generalization barrier.\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | 已验证 |\n| C2 | Residual gating 在训练端可有效优化 GAR (0.02→0.48)，但推理时完全不泛化 (GAR=0.016, 30x 断层) | v7 训练曲线 + D015/D017 confirmed non-bug | 已验证 |\n| C3 | 三个耦合失败机制的因果分析: NF1 反向 turn conditioning + NF2 30x 泛化 gap + NF3 gate 干预强度不足 2-7% | D014 gate-profile 分析 + D015 代码验证 + 梯度冲突实验 (待做) | NF1/NF2/NF3 已验证，梯度冲突量化待做 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。PPL 对比揭示 gating 是否在不改善 GAR 的同时还损害 NTP 质量 | 四路 eval on standard_conversations: GAR + PPL (待做) | 待 eval 确认 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Llama 实验 (待做) | 待做 |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 30x training-inference GAR gap: 训练 GAR=0.48 vs 推理 GAR=0.016 | D015 代码逐行验证非 bug，是 attention pattern 不泛化 | 核心 negative finding，对所有辅助 attention loss 方法有警示意义 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Teacher-forcing→generation 分布偏移的定量证据。** 30x training-inference GAR gap 不是 gating 的特有问题，而是所有在 teacher-forcing 下优化 auxiliary attention loss 的方法都面临的结构性障碍。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。这个 insight 超越 residual gating，对整个 attention steering 领域有警示意义。\n\n**SP2: NTP-GAR 梯度竞争的逐层量化。** NTP loss 在 gate 参数上的梯度方向与 GAR loss 冲突，且幅度远大于 GAR（定量测量待做）。这导致 gates 学到反向 turn conditioning（NF1），是分布偏移的放大器。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融 (TG/UG/LoRA-only/Base) 严格隔离贡献。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（30x 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 30x gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → 在 teacher-forcing 下优化的 auxiliary attention loss 面临结构性泛化障碍 → 需要 inference-time 干预或 exposure bias mitigation。\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n两种定义下推理 GAR 均极低 (~0.016)，与训练 GAR (0.48) 形成 30x 断层。定义差异不影响 negative finding。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构 + MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: 四路消融 (TG/UG/LoRA-only/Base) with GAR + PPL dual metrics + 跨模型验证 (Llama-3.1-8B)\n7. **Analysis**: NTP-GAR 梯度冲突 + 30x 泛化 gap 分析 + gate profile + attention 可视化 + 训练动力学三阶段\n8. **Discussion**: 为什么 residual gating 不够 → 对所有 attention steering 方法的启示 → 潜在解决方向 (inference-time intervention / decoupled pathway / GAR-aware decoding)\n9. **Conclusion**: negative result 总结 + 对社区的 actionable 建议\n\n### 贡献列表（按 novelty 排序）\n\n1. **Teacher-forcing distribution shift 的定量证据**: 首次量化 teacher-forcing→generation 分布偏移如何摧毁 auxiliary attention loss 的泛化性（30x training-inference GAR gap），对所有在 teacher-forcing 下优化的 attention steering 方法有广泛警示意义\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n\n---\n\n## 10. 竞争力评估（Reviewer 估分 2026-05-19）\n\n- **不含 Llama-3**: Findings 3.0（紧绷）。单模型是致命弱点（W1）。\n- **含 Llama-3 跨模型验证**: 3.0-3.5。distribution shift insight 的泛化性 + 跨模型 convergent evidence 是升级关键。\n- **冲 Main 条件**: Llama-3 复现 + 梯度冲突量化做扎实 + constructive future directions + 可选的下游任务 sanity check。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"teacher-forcing distribution shift 摧毁了 auxiliary attention loss 的泛化性\"（强，对领域有广泛警示意义）。\n- **风险**: W2（\"没调对参数\"）和 W5（\"exposure bias 已知\"）需要在论文中显式 address。\n",
      "numLines": 135,
      "startLine": 1,
      "totalLines": 135
    }
  },
  "sourceToolAssistantUUID": "9d2850aa-4d33-4419-a2b5-dd850942f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "dbf5ec3a-18a7-4c0f-84e3-c64f3a0fbfc6",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper with residual gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Assistant

_source line 15 · 2026-05-19T14:22:12.533Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and the paper framing. Let me also check if the paper-writing-norms skill exists as referenced in the CLAUDE.md, and read the LaTeX paper skill for template guidance.

Let me now synthesize the data and write a complete paper. The narrative guidance says:
- "Structural barrier" claim doesn't hold. Reframe as Qwen single-model depth case study: "failure mode taxonomy of residual gating under NTP dominance"
- Llama-3 differences become "architecture-dependent susceptibility" analysis point
- Held-out eval exposes training eval memorization component, 30x gap shrinks to ~8x (but data says 15x), but still meaningful gap (≥5x) can support weakened claim


- Gradient conflict data is too noisy to stand as an independent claim, so I'll use it only as supporting evidence
- The paper targets Findings 2.5-3.0, which means I need a solid methodology contribution through the v1-v7 design space and four-way ablation, plus a detailed mechanistic case study focused on Qwen

I need to correct the narrative—the actual data shows the 30x gap narrows to 15x, not 8x, so I'll use those real numbers. Now I'm framing this as a Qwen-focused mechanistic case study with Llama-3 serving as an architecture-dependent susceptibility analysis point, and I'll weaken the broader claims accordingly.

For the paper structure, I'm laying out: Abstract, Introduction, Related Work, Background on GAR and residual stream persistence, Method covering ThreadGate and the loss design space, then Experiments with setup, the Qwen four-way ablation, Llama-3 cross-model analysis, training-inference gap analysis, gradient conflict analysis, downstream task sanity checks, and attention visualization. Finally Analysis and Conclusion.

I'm pulling the key experiments from the data: the gradient conflict analysis on Qwen v7, attention heatmap visualization, and the held-out evaluation results.

Writing the LaTeX now in ACL/EMNLP format... the task says "default venue", I'll use the ACL anthology style.

Actually, let me keep it simpler - use article class since we might not have the ACL style files. Let me check what's available.

Actually, I should use a standard LaTeX article class. The task says "够审级" - good enough for review, not submission quality. Let me use a clean article format.

Let me write a comprehensive paper now. I'm looking at the key experimental results: Qwen shows a 30x gap narrowing to 15x on held-out data, with TG outperforming LoRA by 0.010 points (marginal at p=0.08), while Llama-3 demonstrates a smaller 2.4x gap and similar marginal TG advantage. The gradient analysis reveals divergent patterns between models, instruction retention drops consistently around 25% across the board, and gate reversal rates differ dramatically between Qwen and Llama-3. I need to reframe this around failure mode taxonomy under NTP dominance rather than structural barriers, with Qwen as the detailed case study.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c70646e-28b3-4339-8656-312ee06ca8ba",
  "isSidechain": false,
  "requestId": "req_011CbC5PSkASZSLYpSVdAyBQ",
  "type": "assistant",
  "uuid": "d17e8adb-9fe4-41d8-97b4-da9608bee83a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgbrhEd2gYiqN1b3kzdHwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 23604,
      "output_tokens": 1365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1365,
          "cache_read_input_tokens": 23604,
          "cache_creation_input_tokens": 16431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16431
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

_source line 16 · 2026-05-19T14:22:12.537Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d17e8adb-9fe4-41d8-97b4-da9608bee83a",
  "isSidechain": false,
  "requestId": "req_011CbC5PSkASZSLYpSVdAyBQ",
  "type": "assistant",
  "uuid": "cd14658c-d323-4fdd-a2b8-fc8c15168925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgbrhEd2gYiqN1b3kzdHwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 23604,
      "output_tokens": 1365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1365,
          "cache_read_input_tokens": 23604,
          "cache_creation_input_tokens": 16431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16431
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

_source line 17 · 2026-05-19T14:22:13.197Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012TiUcaXZExXPKGr9pEc9sV`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd14658c-d323-4fdd-a2b8-fc8c15168925",
  "isSidechain": false,
  "requestId": "req_011CbC5PSkASZSLYpSVdAyBQ",
  "type": "assistant",
  "uuid": "3d85e58f-de38-45ae-9bfa-6f3f46c961c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgbrhEd2gYiqN1b3kzdHwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16431,
      "cache_read_input_tokens": 23604,
      "output_tokens": 1365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1365,
          "cache_read_input_tokens": 23604,
          "cache_creation_input_tokens": 16431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16431
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

_source line 18 · 2026-05-19T14:22:13.358Z_

<details><summary>↩ Tool result · `toolu_012TiUcaXZExXPKGr9pEc9sV`</summary>

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
  "parentUuid": "3d85e58f-de38-45ae-9bfa-6f3f46c961c4",
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "ec1ec1d3-fe35-41cd-a818-8ccbe24ac2d6",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3d85e58f-de38-45ae-9bfa-6f3f46c961c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T14:25:01.236Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DEzLPqhG1agNunzB4WeCWx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\n\\title{Failure Mode Taxonomy of Residual Gating for Multi-Turn Attention Recovery:\\\\A Mechanistic Case Study under Next-Token Prediction Dominance}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% =========================================================================\n\\begin{abstract}\nMulti-turn dialogue performance in large language models degrades as conversations lengthen, with goal attention ratio (GAR) declining by 48--71\\% across architectures. Prior work shows that goal-relevant information persists in the residual stream even as the attention channel closes, motivating residual gating as an architectural intervention. We implement ThreadGate, a per-layer gating module trained jointly with next-token prediction (NTP) and GAR objectives, and conduct a systematic study spanning seven loss configurations (v1--v7) and four-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base). On Qwen-2.5-7B, ThreadGate achieves 0.48 training GAR but only 0.032 at inference on held-out data, revealing a 15$\\times$ training-inference gap that persists across evaluation sets. Four-way ablation shows ThreadGate provides only marginal, non-significant improvement over LoRA-only ($\\Delta$=0.010, $p$=0.08). Cross-architecture analysis on Llama-3.1-8B reveals architecture-dependent susceptibility: GAR degradation is milder (48\\% vs.\\ 71\\%), the training-inference gap shrinks to 2.4$\\times$, and gate reversal affects only 34\\% of layers versus 96\\% in Qwen. NTP gradient magnitude dominates GAR gradients by 3--6$\\times$, though directional conflict is noisy and architecture-dependent. Downstream instruction retention correlates weakly with GAR ($r$=0.31, $p$=0.18), suggesting GAR captures only part of the multi-turn degradation phenomenon. We contribute a failure mode taxonomy---reverse turn conditioning, training-inference distribution shift, and insufficient gate intervention---and discuss implications for auxiliary attention losses optimized under teacher forcing.\n\\end{abstract}\n\n% =========================================================================\n\\section{Introduction}\n\nLarge language models exhibit systematic performance degradation in multi-turn dialogue as conversation length increases \\citep{dongre2026gar}. This degradation manifests across multiple dimensions: instruction following accuracy drops, goal-relevant information receives progressively less attention, and response quality declines. Dongre et al.\\ quantify this through the Goal Attention Ratio (GAR), documenting 27--48\\% drops over extended conversations across twelve models, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes.\n\nThis creates a natural hypothesis: if goal information remains in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We test this hypothesis through ThreadGate, a per-layer gating module that modulates residual stream updates based on learned attention steering signals, trained jointly with NTP and GAR objectives.\n\nOur investigation yields a detailed taxonomy of failure modes rather than a clean negative result. On Qwen-2.5-7B, ThreadGate successfully optimizes GAR during training (0.02$\\to$0.48), but on held-out conversations the training-inference gap is 15$\\times$, with inference GAR reaching only 0.032. Four-way ablation (ThreadGate vs.\\ Uniform Gate vs.\\ LoRA-only vs.\\ Base) reveals that gating provides marginal, statistically non-significant improvement over LoRA adaptation alone. We identify three coupled failure mechanisms: (1) \\textbf{reverse turn conditioning}---NTP gradients push gates toward identity, causing 96\\% of layers to suppress intervention where it is most needed; (2) \\textbf{training-inference distribution shift}---attention patterns learned under teacher forcing do not transfer to autoregressive generation; (3) \\textbf{insufficient intervention magnitude}---gates attenuate residual updates by only 2--7\\% at inference.\n\nCross-architecture analysis on Llama-3.1-8B reveals that both the severity of GAR degradation and the effectiveness of gating are architecture-dependent. Llama-3 exhibits milder GAR decay (48\\% vs.\\ 71\\%), a much smaller training-inference gap (2.4$\\times$), and gate reversal in only 34\\% of layers. These differences challenge any universality claim but reinforce the value of architecture-specific mechanistic analysis.\n\nOur contributions are: (1) a detailed failure mode taxonomy of residual gating under NTP dominance, grounded in a systematic design space exploration (v1--v7) and four-way ablation; (2) quantitative evidence that teacher-forcing distribution shift degrades auxiliary attention loss generalization, with gap magnitudes of 2.4--15$\\times$ depending on architecture; (3) cross-architecture comparison revealing architecture-dependent susceptibility to multi-turn attention degradation; (4) a downstream sanity check establishing the partial but imperfect correspondence between GAR and instruction retention.\n\n% =========================================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn dialogue degradation.}\nPerformance degradation in extended conversations has been documented across model families \\citep{dongre2026gar}. Attention dilution, where goal-relevant tokens receive progressively less attention as context grows, is one proposed mechanism. Dongre et al.\\ introduce GAR as a quantitative measure and show that goal information persists in residual streams despite attention channel closure.\n\n\\paragraph{Residual gating and adaptive computation.}\nGating mechanisms on residual connections have been explored for adaptive depth \\citep{elbayad2020depth}, mixture of experts \\citep{shazeer2017moe}, and layer-selective computation. Our work applies per-layer scalar gating specifically to steer attention toward goal tokens, differing from prior work in objective (attention recovery rather than efficiency).\n\n\\paragraph{Attention steering and intervention.}\nMethods for steering attention include attention supervision \\citep{liu2016attn}, auxiliary attention losses, and inference-time intervention \\citep{li2023iti}. Our work connects to the exposure bias literature \\citep{ranzato2016sequence, bengio2015scheduled}: teacher-forcing creates distributional mismatch between training and inference, which we show specifically disrupts auxiliary attention loss generalization.\n\n% =========================================================================\n\\section{Background}\n\n\\subsection{Goal Attention Ratio}\n\nFollowing Dongre et al., we define the Goal Attention Ratio (GAR) as the fraction of attention mass allocated to goal-relevant tokens. Let $\\mathcal{G}$ denote the set of goal token positions (system prompt task tokens) and $\\alpha_{i,j}^{(l,h)}$ denote the attention weight from position $i$ to position $j$ at layer $l$, head $h$. GAR-Dongre is:\n\\begin{equation}\n\\text{GAR}(i) = \\frac{1}{L \\cdot H} \\sum_{l,h} \\sum_{j \\in \\mathcal{G}} \\alpha_{i,j}^{(l,h)}\n\\end{equation}\nwhere response token positions $i$ are averaged. We report GAR at mid-conversation turns following Dongre et al.'s protocol.\n\nWe also define GAR-Ours, which extends goal tokens to include the first user query and uses last-token-per-turn as response positions for more stable measurement. Both definitions yield consistent results in our experiments.\n\n\\subsection{Residual Stream Persistence}\n\nDongre et al.\\ demonstrate via linear probes that goal-relevant information persists in the residual stream (AUC$=$0.98) even when attention to goal tokens drops substantially. This persistence motivates our intervention: if information is present but attention fails to route it, modulating the residual connection should help.\n\n% =========================================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate introduces a learnable scalar gate $g_l \\in (0,1)$ at each transformer layer $l$. The gated residual update becomes:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\end{equation}\nwhere $f_l$ is the standard transformer block output. Each $g_l$ is parameterized as $g_l = \\sigma(w_l)$ with learnable scalar $w_l$, initialized such that $g_l \\approx 1$ (identity initialization). The model backbone is augmented with LoRA adapters (rank 16) for efficient fine-tuning.\n\n\\subsection{Loss Design Space: v1--v7}\n\nWe explore seven loss configurations spanning four loss families:\n\n\\begin{itemize}\n\\item \\textbf{v1--v2 (Cumulative)}: Direct GAR maximization via cumulative attention reward. Failed to converge---GAR remained near baseline.\n\\item \\textbf{v3--v5 (Maximize)}: Direct GAR maximization with different normalization schemes. Unstable training dynamics.\n\\item \\textbf{v6 (Smooth saturation)}: Saturating reward to prevent attention collapse. Partial convergence.\n\\item \\textbf{v7 (MSE target + gate divergence)}: $\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_1 \\mathcal{L}_{\\text{MSE}} + \\lambda_2 \\mathcal{L}_{\\text{gate\\_div}}$, where $\\mathcal{L}_{\\text{MSE}}$ targets a GAR value and $\\mathcal{L}_{\\text{gate\\_div}}$ encourages gate diversity. \\textbf{Only configuration achieving training convergence.}\n\\end{itemize}\n\nThe v7 joint loss balances NTP quality preservation with GAR optimization. The MSE component provides a stable gradient signal by targeting a specific GAR value rather than unbounded maximization, while gate divergence regularization prevents gates from collapsing to uniform values.\n\n\\subsection{Training Setup}\n\nWe train on UltraChat multi-turn conversations (3 epochs, conversations with index $<$8000). Qwen-2.5-7B and Llama-3.1-8B serve as base models. LoRA rank is 16 for all configurations. Four-way ablation: ThreadGate (v7), Uniform Gate (UG, shared gate across layers), LoRA-only (no gating), and Base (no fine-tuning).\n\n% =========================================================================\n\\section{Experiments}\n\n\\subsection{Qwen-2.5-7B: Four-Way Ablation on Held-Out Data}\n\nWe evaluate all four configurations on 50 held-out UltraChat conversations (index$\\geq$8000) unseen during training. Table~\\ref{tab:heldout_4way} presents the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Four-way evaluation on held-out conversations ($n$=50, UltraChat idx$\\geq$8000). Recovery (pp) = GAR improvement over Base in percentage points $\\times$100.}\n\\label{tab:heldout_4way}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & GAR-D mid & GAR-O mid & PPL & Recovery \\\\\n\\midrule\nBase       & 0.0028 & 0.0095 & 4.35 & -- \\\\\nTG (v7)    & 0.032  & 0.038  & 2.71 & 2.92 \\\\\nUG         & 0.029  & 0.035  & 2.68 & 2.62 \\\\\nLoRA-only  & 0.022  & 0.028  & 2.69 & 1.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll fine-tuned models substantially improve over Base in both GAR and PPL, but the differences \\emph{among} fine-tuned models are small. ThreadGate achieves the highest GAR (0.032 Dongre, 0.038 Ours) but the advantage over LoRA-only is marginal ($\\Delta$=0.010 Dongre, $p$=0.08 paired $t$-test). Uniform Gate performs between TG and LoRA-only. PPL is comparable across fine-tuned variants (2.68--2.71), indicating no meaningful NTP quality penalty from gating.\n\n\\subsection{Training-Inference GAR Gap}\n\nTable~\\ref{tab:gap} compares the training-inference GAR gap across evaluation sets.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training-inference GAR gap: original evaluation set vs.\\ held-out.}\n\\label{tab:gap}\n\\begin{tabular}{lccc}\n\\toprule\nEval set & Training GAR & Inference GAR (TG-D) & Gap ratio \\\\\n\\midrule\nOriginal ($n$=5)   & 0.48 & 0.0157 & 30.6$\\times$ \\\\\nHeld-out ($n$=50)  & 0.48 & 0.032  & 15.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe original 30$\\times$ gap shrinks to 15$\\times$ on held-out data, indicating that the original evaluation set underestimated inference GAR due to limited sample size and potential topic distribution effects. The 15$\\times$ gap remains substantial: attention patterns learned under teacher forcing transfer poorly to autoregressive generation, but the magnitude is less dramatic than initially observed. We report the 15$\\times$ held-out figure as our primary estimate.\n\n\\subsection{Llama-3.1-8B: GAR Degradation Diagnosis}\n\nTo assess cross-architecture generality, we first measure baseline GAR degradation on Llama-3.1-8B (Table~\\ref{tab:llama_diag}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Llama-3.1-8B GAR degradation across 10 turns ($n$=5 conversations).}\n\\label{tab:llama_diag}\n\\begin{tabular}{ccc}\n\\toprule\nTurn & Avg GAR & Relative to Turn 1 \\\\\n\\midrule\n1  & 0.0285 & 1.00 \\\\\n2  & 0.0221 & 0.78 \\\\\n3  & 0.0198 & 0.69 \\\\\n4  & 0.0172 & 0.60 \\\\\n5  & 0.0155 & 0.54 \\\\\n6  & 0.0142 & 0.50 \\\\\n7  & 0.0131 & 0.46 \\\\\n8  & 0.0128 & 0.45 \\\\\n9  & 0.0135 & 0.47 \\\\\n10 & 0.0119 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama-3 exhibits GAR degradation (48\\% relative drop by turn 10) but substantially milder than Qwen (71\\%). The decay is gradual and approximately linear, lacking the sharp early drop observed in Qwen. This confirms that multi-turn GAR degradation exists across architectures but varies in severity.\n\n\\subsection{Llama-3.1-8B: ThreadGate Training and Evaluation}\n\nWe replicate the v7 ThreadGate setup on Llama-3.1-8B. Table~\\ref{tab:llama_training} compares training dynamics.\n\n\\begin{table}[h]\n\\centering\n\\caption{ThreadGate v7 training dynamics: Llama-3 vs.\\ Qwen.}\n\\label{tab:llama_training}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Llama-3 & Qwen \\\\\n\\midrule\nTraining GAR peak      & 0.09   & 0.48 \\\\\nGate mean (final)      & 0.962  & 0.934 \\\\\nGate std (final)       & 0.028  & 0.049 \\\\\nReversed layers frac   & 34\\%   & 96\\% \\\\\nPhase transition       & weak/absent & sharp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate training on Llama-3 achieves only 0.09 peak GAR versus 0.48 on Qwen, with gates remaining near identity (mean 0.962, std 0.028). Only 34\\% of layers exhibit gate reversal compared to 96\\% on Qwen. The clear three-phase training dynamics (plateau $\\to$ transition $\\to$ convergence) observed on Qwen are absent; Llama-3 shows a weak, gradual rise without a sharp phase transition. This suggests the MSE+gate\\_div loss design, while effective for Qwen, does not transfer well to Llama-3's optimization landscape.\n\nTable~\\ref{tab:llama_eval} presents the three-way evaluation on Llama-3.\n\n\\begin{table}[h]\n\\centering\n\\caption{Llama-3.1-8B three-way evaluation (Base / TG / LoRA-only).}\n\\label{tab:llama_eval}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GAR-D mid & GAR-O mid & PPL & Train GAR & Gap \\\\\n\\midrule\nBase       & 0.0135 & 0.0182 & 3.85 & --   & -- \\\\\nTG (v7)    & 0.038  & 0.045  & 2.48 & 0.09 & 2.4$\\times$ \\\\\nLoRA-only  & 0.025  & 0.031  & 2.42 & --   & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe training-inference gap on Llama-3 is only 2.4$\\times$ (0.09$\\to$0.038), dramatically smaller than Qwen's 15$\\times$. ThreadGate shows a marginal advantage over LoRA-only ($\\Delta$=0.013, $p$=0.06) that is directionally consistent across both architectures but not statistically significant. PPL shows a negligible penalty for gating (2.48 vs.\\ 2.42).\n\n\\subsection{Cross-Architecture Comparison}\n\nTable~\\ref{tab:crossmodel} synthesizes the cross-architecture comparison.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B \\\\\n\\midrule\nBase GAR (Dongre mid)     & 0.003        & 0.0135 \\\\\nGAR relative drop         & 71\\%         & 48\\% \\\\\nTraining GAR peak         & 0.48         & 0.09 \\\\\nInference GAR (TG Dongre) & 0.016--0.032 & 0.038 \\\\\nGap ratio                 & 15--30$\\times$     & 2.4$\\times$ \\\\\nTG $-$ LoRA $\\Delta$GAR   & 0.002--0.010 & 0.013 \\\\\nGate reversal fraction    & 96\\%         & 34\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two architectures exhibit qualitatively different failure profiles. Qwen shows severe GAR degradation, successful training-time optimization but dramatic inference failure, and near-universal gate reversal. Llama-3 shows moderate GAR degradation, poor training convergence, a small training-inference gap, and limited gate reversal. These differences likely stem from architectural factors (GQA configuration, pretraining data distribution) and indicate that both the severity of multi-turn attention degradation and the feasibility of gating interventions are architecture-dependent.\n\n\\subsection{Gradient Conflict Analysis}\n\nWe measure per-layer cosine similarity and magnitude ratio between NTP and GAR gradients on gate parameters across three epoch checkpoints.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer NTP vs.\\ GAR gradient statistics on Qwen v7 (selected layers across 3 epochs).}\n\\label{tab:grad_qwen}\n\\begin{tabular}{lccccc}\n\\toprule\nLayer & Ep0 cos & Ep1 cos & Ep2 cos & Stable? & Avg mag ratio \\\\\n\\midrule\nL3  & $-$0.048 & $-$0.022 & $-$0.041 & Yes (neg) & 5.8 \\\\\nL4  & $-$0.052 & $-$0.018 & $-$0.039 & Yes (neg) & 6.2 \\\\\nL14 & $-$0.039 & $-$0.011 & $-$0.028 & Yes (neg) & 4.9 \\\\\nL1  & +0.021 & +0.035 & +0.018 & Yes (pos) & 3.1 \\\\\nL15 & $-$0.018 & +0.029 & $-$0.007 & No & 4.5 \\\\\nL22 & +0.012 & $-$0.031 & +0.008 & No & 5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, cosine similarity between NTP and GAR gradients is small in magnitude (mean $-$0.031 to $+$0.008 across epochs) with high variance (std 0.038--0.045). Only 9 of 28 layers show sign-stable cosine similarity across checkpoints; the remaining 19 exhibit sign flips. NTP gradient magnitude consistently exceeds GAR by 3.8--6.1$\\times$ (range 2.1--7.8$\\times$). The magnitude asymmetry is the more robust signal: even without consistent directional conflict, NTP gradients dominate gate parameter updates.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient conflict comparison: Qwen vs.\\ Llama-3.}\n\\label{tab:grad_cross}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen & Llama-3 \\\\\n\\midrule\ncos\\_sim mean            & $-$0.031 to $+$0.008 & $+$0.012 \\\\\nSign-stable layers       & 9/28 (32\\%) & 7/32 (22\\%) \\\\\nmag\\_ratio mean          & 5.2 & 3.2 \\\\\nOverall direction        & weakly conflicting & not conflicting \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Llama-3, the overall cosine similarity is positive ($+$0.012), indicating no directional conflict between NTP and GAR gradients. The magnitude ratio is also smaller (3.2$\\times$). The absence of gradient conflict on Llama-3 is consistent with its poor training convergence (GAR peaks at only 0.09): when GAR loss is near-saturated, its gradients approach noise, making cosine similarity measurements unreliable. We therefore treat gradient conflict as supporting evidence for the Qwen case study rather than a general mechanistic claim.\n\n\\subsection{Downstream Task: Instruction Retention}\n\nTo assess whether GAR captures a practically meaningful phenomenon, we measure instruction retention---the ability to follow system prompt constraints---across conversation turns (Table~\\ref{tab:downstream}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction retention across turns (downstream sanity check, Qwen).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Turn 1 & Turn 10 & Drop \\\\\n\\midrule\nBase       & 0.82 & 0.61 & 25.6\\% \\\\\nTG (v7)    & 0.84 & 0.63 & 25.0\\% \\\\\nLoRA-only  & 0.83 & 0.62 & 25.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction retention degrades by approximately 25\\% from turn 1 to turn 10 across all models, confirming that multi-turn degradation is a real downstream phenomenon. However, GAR correlates only weakly with instruction retention ($r$=0.31, $p$=0.18), and ThreadGate provides negligible improvement over LoRA-only ($\\Delta$=0.01). This suggests GAR captures part of the multi-turn degradation mechanism but is not a precise proxy for task-level performance.\n\n\\subsection{Attention Heatmap Visualization}\n\nWe visualize attention patterns across four models (Base / TG / UG / LoRA-only) on three conversations across all 28 Qwen layers. Base attention to goal tokens is diffuse and declines over turns. ThreadGate and LoRA-only patterns are visually indistinguishable at turns beyond 10. Only layers L3, L4, and L12---where gates deviate most from identity---show any visible difference, but this difference is within the noise range of cross-conversation variability. We include these visualizations in the supplementary material as they confirm the quantitative findings (gating provides minimal incremental attention redistribution at inference) but do not add independent mechanistic insight.\n\n% =========================================================================\n\\section{Analysis}\n\n\\subsection{Failure Mode Taxonomy}\n\nOur experiments reveal three coupled failure modes of residual gating under NTP dominance:\n\n\\paragraph{FM1: Reverse turn conditioning.}\nOn Qwen, 96\\% of layers (27/28) develop gates with negative turn-GAR correlation: gates suppress more strongly at early turns (where GAR is naturally higher) and become passive at late turns (where intervention is most needed). This occurs because NTP loss, which dominates gate gradients by 3--6$\\times$, pushes gates toward identity to preserve language modeling quality. At late turns where NTP loss is highest, the push toward identity is strongest, precisely counteracting the intended GAR-recovery behavior. On Llama-3, this reversal is limited to 34\\% of layers, consistent with its lower NTP-GAR gradient magnitude ratio (3.2$\\times$).\n\n\\paragraph{FM2: Training-inference distribution shift.}\nDuring training under teacher forcing, the model observes gold context and learns attention patterns conditioned on this distribution. At inference, the model conditions on its own generated tokens, creating a distributional mismatch. On Qwen, this manifests as a 15$\\times$ gap between training GAR (0.48) and held-out inference GAR (0.032). The gap is dramatically smaller on Llama-3 (2.4$\\times$), partly because training GAR itself is much lower (0.09), yielding less room for distribution shift to erode gains.\n\n\\paragraph{FM3: Insufficient intervention magnitude.}\nAt inference, Qwen gates cluster near identity (mean 0.934, range 0.891--0.996), attenuating residual updates by only 2--7\\%. This attenuation is far too weak to meaningfully redistribute attention. Llama-3 gates are even closer to identity (mean 0.962, range 0.891--0.996). The insufficient magnitude is a consequence of FM1: NTP dominance prevents gates from learning aggressive intervention strategies.\n\n\\subsection{Architecture-Dependent Susceptibility}\n\nThe cross-architecture comparison reveals that susceptibility to multi-turn attention degradation---and to residual gating failure---varies substantially by architecture. Llama-3's base GAR (0.0135) is 4.5$\\times$ higher than Qwen's (0.003), suggesting that Llama-3's attention distribution is inherently more robust to context lengthening. This higher baseline robustness means there is less room for degradation and less need for gating intervention. The architectural differences (GQA configuration, pretraining data distribution, model depth) likely contribute to this divergence, though isolating individual factors is beyond our scope.\n\n\\subsection{Gradient Conflict: Supporting Evidence with Caveats}\n\nThe gradient conflict analysis provides partial mechanistic insight but with important limitations. On Qwen, NTP gradient magnitude consistently exceeds GAR by 3--6$\\times$, supporting the claim that NTP dominates gate updates. However, directional conflict (negative cosine similarity) is noisy: only 9/28 layers show stable negative cosine across epochs, and epoch 1 shows near-zero or positive mean cosine similarity, suggesting transient alignment during rapid GAR improvement phases. On Llama-3, there is no directional conflict (positive cosine), and magnitude asymmetry is smaller (3.2$\\times$). We interpret gradient conflict as one contributing factor to gate reversal on Qwen, not as a universal mechanism.\n\n\\subsection{GAR as a Proxy Metric}\n\nThe weak correlation between GAR and instruction retention ($r$=0.31) raises the question of why GAR warrants study. We argue that attention mechanism analysis remains valuable independent of downstream task correlation: (1) the 25\\% instruction retention drop confirms multi-turn degradation is real; (2) GAR captures the attention-level component of this degradation, which may combine with other mechanisms (positional encoding effects, context window saturation) to produce the downstream effect; (3) understanding why attention steering fails at the mechanism level informs the design of future interventions even if GAR is not a perfect proxy.\n\n% =========================================================================\n\\section{Discussion}\n\n\\subsection{Implications for Auxiliary Attention Losses}\n\nOur results suggest that any auxiliary attention loss optimized under teacher forcing faces distribution shift at inference. The 15$\\times$ gap on Qwen, while less dramatic than initial estimates, represents a substantial generalization failure. That this gap is only 2.4$\\times$ on Llama-3 does not invalidate the concern---it indicates that vulnerability is architecture-dependent, and practitioners cannot know a priori whether their target architecture is closer to the Qwen or Llama-3 regime.\n\n\\subsection{Limitations}\n\nSeveral limitations constrain our conclusions. First, our study covers only two architectures (Qwen-2.5-7B, Llama-3.1-8B) at the 7--8B scale; larger models and different architecture families may behave differently. Second, the marginal positive signal from gating ($\\Delta$=0.010--0.013 across architectures, $p$=0.06--0.08) leaves open the possibility that gating provides a small real benefit obscured by limited statistical power. Third, GAR's weak correlation with downstream performance ($r$=0.31) limits the practical significance of our attention-level findings. Fourth, our loss design space, while spanning seven configurations, does not exhaust all possibilities---reinforcement learning-based approaches, inference-time intervention, or exposure bias mitigation techniques remain unexplored. Fifth, gradient conflict analysis is noisy and architecture-dependent, limiting its value as a standalone mechanistic claim.\n\n\\subsection{Future Directions}\n\nOur failure mode taxonomy suggests several promising directions: (1) \\textbf{inference-time attention intervention} that bypasses the training-inference distribution shift entirely by modifying attention at generation time; (2) \\textbf{decoupled goal-processing pathways} that maintain a separate channel for goal information outside the main residual stream; (3) \\textbf{GAR-aware decoding} strategies that incorporate attention distribution quality into the generation process; (4) \\textbf{exposure bias mitigation} techniques (scheduled sampling, sequence-level training) applied to auxiliary attention losses to reduce the training-inference distributional mismatch.\n\n% =========================================================================\n\\section{Conclusion}\n\nWe present a mechanistic case study of residual gating for multi-turn attention recovery, focusing on failure modes under next-token prediction dominance. Through systematic exploration of seven loss configurations and four-way ablation on Qwen-2.5-7B, complemented by cross-architecture analysis on Llama-3.1-8B, we identify three coupled failure mechanisms: reverse turn conditioning, training-inference distribution shift (15$\\times$ on Qwen, 2.4$\\times$ on Llama-3), and insufficient gate intervention magnitude. Gating provides only marginal, non-significant improvement over LoRA-only adaptation, and both the severity of multi-turn degradation and the nature of gating failure are architecture-dependent. Our failure mode taxonomy and design space exploration provide negative baselines and mechanistic insights for future work on attention steering in multi-turn dialogue.\n\n% =========================================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026gar}\nDongre, A., et~al. (2026).\n\\newblock Goal attention degradation in multi-turn dialogue: Measurement, mechanisms, and implications.\n\\newblock \\emph{Proceedings of ACL 2026}.\n\n\\bibitem[Elbayad et~al.(2020)]{elbayad2020depth}\nElbayad, M., Gu, J., Grave, E., and Auli, M. (2020).\n\\newblock Depth-adaptive transformer.\n\\newblock \\emph{Proceedings of ICLR 2020}.\n\n\\bibitem[Li et~al.(2023)]{li2023iti}\nLi, K., Patel, O., Vi{\\'e}gas, F., Pfister, H., and Wattenberg, M. (2023).\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock \\emph{Proceedings of NeurIPS 2023}.\n\n\\bibitem[Liu et~al.(2016)]{liu2016attn}\nLiu, L., Utiyama, M., Finch, A., and Sumita, E. (2016).\n\\newblock Neural machine translation with supervised attention.\n\\newblock \\emph{Proceedings of COLING 2016}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nRanzato, M., Chopra, S., Auli, M., and Zaremba, W. (2016).\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock \\emph{Proceedings of ICLR 2016}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nBengio, S., Vinyals, O., Jaitly, N., and Shazeer, N. (2015).\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock \\emph{Proceedings of NeurIPS 2015}.\n\n\\bibitem[Shazeer et~al.(2017)]{shazeer2017moe}\nShazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., and Dean, J. (2017).\n\\newblock Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.\n\\newblock \\emph{Proceedings of ICLR 2017}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1ec1d3-fe35-41cd-a818-8ccbe24ac2d6",
  "isSidechain": false,
  "requestId": "req_011CbC5S1L38rqDctpruUxvp",
  "type": "assistant",
  "uuid": "ca9bbffa-7606-4fe8-975d-ffc19ec4fe6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwYPnySVGdYUqPRe2PqzLm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 40035,
      "output_tokens": 8963,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8963,
          "cache_read_input_tokens": 40035,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1392
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

_source line 20 · 2026-05-19T14:25:01.266Z_

<details><summary>↩ Tool result · `toolu_01DEzLPqhG1agNunzB4WeCWx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca9bbffa-7606-4fe8-975d-ffc19ec4fe6b",
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "5bdd2c9f-97ce-4cec-b6a3-d20fc2076291",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\n\\title{Failure Mode Taxonomy of Residual Gating for Multi-Turn Attention Recovery:\\\\A Mechanistic Case Study under Next-Token Prediction Dominance}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% =========================================================================\n\\begin{abstract}\nMulti-turn dialogue performance in large language models degrades as conversations lengthen, with goal attention ratio (GAR) declining by 48--71\\% across architectures. Prior work shows that goal-relevant information persists in the residual stream even as the attention channel closes, motivating residual gating as an architectural intervention. We implement ThreadGate, a per-layer gating module trained jointly with next-token prediction (NTP) and GAR objectives, and conduct a systematic study spanning seven loss configurations (v1--v7) and four-way ablation (ThreadGate / Uniform Gate / LoRA-only / Base). On Qwen-2.5-7B, ThreadGate achieves 0.48 training GAR but only 0.032 at inference on held-out data, revealing a 15$\\times$ training-inference gap that persists across evaluation sets. Four-way ablation shows ThreadGate provides only marginal, non-significant improvement over LoRA-only ($\\Delta$=0.010, $p$=0.08). Cross-architecture analysis on Llama-3.1-8B reveals architecture-dependent susceptibility: GAR degradation is milder (48\\% vs.\\ 71\\%), the training-inference gap shrinks to 2.4$\\times$, and gate reversal affects only 34\\% of layers versus 96\\% in Qwen. NTP gradient magnitude dominates GAR gradients by 3--6$\\times$, though directional conflict is noisy and architecture-dependent. Downstream instruction retention correlates weakly with GAR ($r$=0.31, $p$=0.18), suggesting GAR captures only part of the multi-turn degradation phenomenon. We contribute a failure mode taxonomy---reverse turn conditioning, training-inference distribution shift, and insufficient gate intervention---and discuss implications for auxiliary attention losses optimized under teacher forcing.\n\\end{abstract}\n\n% =========================================================================\n\\section{Introduction}\n\nLarge language models exhibit systematic performance degradation in multi-turn dialogue as conversation length increases \\citep{dongre2026gar}. This degradation manifests across multiple dimensions: instruction following accuracy drops, goal-relevant information receives progressively less attention, and response quality declines. Dongre et al.\\ quantify this through the Goal Attention Ratio (GAR), documenting 27--48\\% drops over extended conversations across twelve models, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes.\n\nThis creates a natural hypothesis: if goal information remains in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We test this hypothesis through ThreadGate, a per-layer gating module that modulates residual stream updates based on learned attention steering signals, trained jointly with NTP and GAR objectives.\n\nOur investigation yields a detailed taxonomy of failure modes rather than a clean negative result. On Qwen-2.5-7B, ThreadGate successfully optimizes GAR during training (0.02$\\to$0.48), but on held-out conversations the training-inference gap is 15$\\times$, with inference GAR reaching only 0.032. Four-way ablation (ThreadGate vs.\\ Uniform Gate vs.\\ LoRA-only vs.\\ Base) reveals that gating provides marginal, statistically non-significant improvement over LoRA adaptation alone. We identify three coupled failure mechanisms: (1) \\textbf{reverse turn conditioning}---NTP gradients push gates toward identity, causing 96\\% of layers to suppress intervention where it is most needed; (2) \\textbf{training-inference distribution shift}---attention patterns learned under teacher forcing do not transfer to autoregressive generation; (3) \\textbf{insufficient intervention magnitude}---gates attenuate residual updates by only 2--7\\% at inference.\n\nCross-architecture analysis on Llama-3.1-8B reveals that both the severity of GAR degradation and the effectiveness of gating are architecture-dependent. Llama-3 exhibits milder GAR decay (48\\% vs.\\ 71\\%), a much smaller training-inference gap (2.4$\\times$), and gate reversal in only 34\\% of layers. These differences challenge any universality claim but reinforce the value of architecture-specific mechanistic analysis.\n\nOur contributions are: (1) a detailed failure mode taxonomy of residual gating under NTP dominance, grounded in a systematic design space exploration (v1--v7) and four-way ablation; (2) quantitative evidence that teacher-forcing distribution shift degrades auxiliary attention loss generalization, with gap magnitudes of 2.4--15$\\times$ depending on architecture; (3) cross-architecture comparison revealing architecture-dependent susceptibility to multi-turn attention degradation; (4) a downstream sanity check establishing the partial but imperfect correspondence between GAR and instruction retention.\n\n% =========================================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn dialogue degradation.}\nPerformance degradation in extended conversations has been documented across model families \\citep{dongre2026gar}. Attention dilution, where goal-relevant tokens receive progressively less attention as context grows, is one proposed mechanism. Dongre et al.\\ introduce GAR as a quantitative measure and show that goal information persists in residual streams despite attention channel closure.\n\n\\paragraph{Residual gating and adaptive computation.}\nGating mechanisms on residual connections have been explored for adaptive depth \\citep{elbayad2020depth}, mixture of experts \\citep{shazeer2017moe}, and layer-selective computation. Our work applies per-layer scalar gating specifically to steer attention toward goal tokens, differing from prior work in objective (attention recovery rather than efficiency).\n\n\\paragraph{Attention steering and intervention.}\nMethods for steering attention include attention supervision \\citep{liu2016attn}, auxiliary attention losses, and inference-time intervention \\citep{li2023iti}. Our work connects to the exposure bias literature \\citep{ranzato2016sequence, bengio2015scheduled}: teacher-forcing creates distributional mismatch between training and inference, which we show specifically disrupts auxiliary attention loss generalization.\n\n% =========================================================================\n\\section{Background}\n\n\\subsection{Goal Attention Ratio}\n\nFollowing Dongre et al., we define the Goal Attention Ratio (GAR) as the fraction of attention mass allocated to goal-relevant tokens. Let $\\mathcal{G}$ denote the set of goal token positions (system prompt task tokens) and $\\alpha_{i,j}^{(l,h)}$ denote the attention weight from position $i$ to position $j$ at layer $l$, head $h$. GAR-Dongre is:\n\\begin{equation}\n\\text{GAR}(i) = \\frac{1}{L \\cdot H} \\sum_{l,h} \\sum_{j \\in \\mathcal{G}} \\alpha_{i,j}^{(l,h)}\n\\end{equation}\nwhere response token positions $i$ are averaged. We report GAR at mid-conversation turns following Dongre et al.'s protocol.\n\nWe also define GAR-Ours, which extends goal tokens to include the first user query and uses last-token-per-turn as response positions for more stable measurement. Both definitions yield consistent results in our experiments.\n\n\\subsection{Residual Stream Persistence}\n\nDongre et al.\\ demonstrate via linear probes that goal-relevant information persists in the residual stream (AUC$=$0.98) even when attention to goal tokens drops substantially. This persistence motivates our intervention: if information is present but attention fails to route it, modulating the residual connection should help.\n\n% =========================================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate introduces a learnable scalar gate $g_l \\in (0,1)$ at each transformer layer $l$. The gated residual update becomes:\n\\begin{equation}\n\\mathbf{x}_{l+1} = \\mathbf{x}_l + g_l \\cdot f_l(\\mathbf{x}_l)\n\\end{equation}\nwhere $f_l$ is the standard transformer block output. Each $g_l$ is parameterized as $g_l = \\sigma(w_l)$ with learnable scalar $w_l$, initialized such that $g_l \\approx 1$ (identity initialization). The model backbone is augmented with LoRA adapters (rank 16) for efficient fine-tuning.\n\n\\subsection{Loss Design Space: v1--v7}\n\nWe explore seven loss configurations spanning four loss families:\n\n\\begin{itemize}\n\\item \\textbf{v1--v2 (Cumulative)}: Direct GAR maximization via cumulative attention reward. Failed to converge---GAR remained near baseline.\n\\item \\textbf{v3--v5 (Maximize)}: Direct GAR maximization with different normalization schemes. Unstable training dynamics.\n\\item \\textbf{v6 (Smooth saturation)}: Saturating reward to prevent attention collapse. Partial convergence.\n\\item \\textbf{v7 (MSE target + gate divergence)}: $\\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_1 \\mathcal{L}_{\\text{MSE}} + \\lambda_2 \\mathcal{L}_{\\text{gate\\_div}}$, where $\\mathcal{L}_{\\text{MSE}}$ targets a GAR value and $\\mathcal{L}_{\\text{gate\\_div}}$ encourages gate diversity. \\textbf{Only configuration achieving training convergence.}\n\\end{itemize}\n\nThe v7 joint loss balances NTP quality preservation with GAR optimization. The MSE component provides a stable gradient signal by targeting a specific GAR value rather than unbounded maximization, while gate divergence regularization prevents gates from collapsing to uniform values.\n\n\\subsection{Training Setup}\n\nWe train on UltraChat multi-turn conversations (3 epochs, conversations with index $<$8000). Qwen-2.5-7B and Llama-3.1-8B serve as base models. LoRA rank is 16 for all configurations. Four-way ablation: ThreadGate (v7), Uniform Gate (UG, shared gate across layers), LoRA-only (no gating), and Base (no fine-tuning).\n\n% =========================================================================\n\\section{Experiments}\n\n\\subsection{Qwen-2.5-7B: Four-Way Ablation on Held-Out Data}\n\nWe evaluate all four configurations on 50 held-out UltraChat conversations (index$\\geq$8000) unseen during training. Table~\\ref{tab:heldout_4way} presents the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{Four-way evaluation on held-out conversations ($n$=50, UltraChat idx$\\geq$8000). Recovery (pp) = GAR improvement over Base in percentage points $\\times$100.}\n\\label{tab:heldout_4way}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & GAR-D mid & GAR-O mid & PPL & Recovery \\\\\n\\midrule\nBase       & 0.0028 & 0.0095 & 4.35 & -- \\\\\nTG (v7)    & 0.032  & 0.038  & 2.71 & 2.92 \\\\\nUG         & 0.029  & 0.035  & 2.68 & 2.62 \\\\\nLoRA-only  & 0.022  & 0.028  & 2.69 & 1.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll fine-tuned models substantially improve over Base in both GAR and PPL, but the differences \\emph{among} fine-tuned models are small. ThreadGate achieves the highest GAR (0.032 Dongre, 0.038 Ours) but the advantage over LoRA-only is marginal ($\\Delta$=0.010 Dongre, $p$=0.08 paired $t$-test). Uniform Gate performs between TG and LoRA-only. PPL is comparable across fine-tuned variants (2.68--2.71), indicating no meaningful NTP quality penalty from gating.\n\n\\subsection{Training-Inference GAR Gap}\n\nTable~\\ref{tab:gap} compares the training-inference GAR gap across evaluation sets.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training-inference GAR gap: original evaluation set vs.\\ held-out.}\n\\label{tab:gap}\n\\begin{tabular}{lccc}\n\\toprule\nEval set & Training GAR & Inference GAR (TG-D) & Gap ratio \\\\\n\\midrule\nOriginal ($n$=5)   & 0.48 & 0.0157 & 30.6$\\times$ \\\\\nHeld-out ($n$=50)  & 0.48 & 0.032  & 15.0$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe original 30$\\times$ gap shrinks to 15$\\times$ on held-out data, indicating that the original evaluation set underestimated inference GAR due to limited sample size and potential topic distribution effects. The 15$\\times$ gap remains substantial: attention patterns learned under teacher forcing transfer poorly to autoregressive generation, but the magnitude is less dramatic than initially observed. We report the 15$\\times$ held-out figure as our primary estimate.\n\n\\subsection{Llama-3.1-8B: GAR Degradation Diagnosis}\n\nTo assess cross-architecture generality, we first measure baseline GAR degradation on Llama-3.1-8B (Table~\\ref{tab:llama_diag}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Llama-3.1-8B GAR degradation across 10 turns ($n$=5 conversations).}\n\\label{tab:llama_diag}\n\\begin{tabular}{ccc}\n\\toprule\nTurn & Avg GAR & Relative to Turn 1 \\\\\n\\midrule\n1  & 0.0285 & 1.00 \\\\\n2  & 0.0221 & 0.78 \\\\\n3  & 0.0198 & 0.69 \\\\\n4  & 0.0172 & 0.60 \\\\\n5  & 0.0155 & 0.54 \\\\\n6  & 0.0142 & 0.50 \\\\\n7  & 0.0131 & 0.46 \\\\\n8  & 0.0128 & 0.45 \\\\\n9  & 0.0135 & 0.47 \\\\\n10 & 0.0119 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama-3 exhibits GAR degradation (48\\% relative drop by turn 10) but substantially milder than Qwen (71\\%). The decay is gradual and approximately linear, lacking the sharp early drop observed in Qwen. This confirms that multi-turn GAR degradation exists across architectures but varies in severity.\n\n\\subsection{Llama-3.1-8B: ThreadGate Training and Evaluation}\n\nWe replicate the v7 ThreadGate setup on Llama-3.1-8B. Table~\\ref{tab:llama_training} compares training dynamics.\n\n\\begin{table}[h]\n\\centering\n\\caption{ThreadGate v7 training dynamics: Llama-3 vs.\\ Qwen.}\n\\label{tab:llama_training}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Llama-3 & Qwen \\\\\n\\midrule\nTraining GAR peak      & 0.09   & 0.48 \\\\\nGate mean (final)      & 0.962  & 0.934 \\\\\nGate std (final)       & 0.028  & 0.049 \\\\\nReversed layers frac   & 34\\%   & 96\\% \\\\\nPhase transition       & weak/absent & sharp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate training on Llama-3 achieves only 0.09 peak GAR versus 0.48 on Qwen, with gates remaining near identity (mean 0.962, std 0.028). Only 34\\% of layers exhibit gate reversal compared to 96\\% on Qwen. The clear three-phase training dynamics (plateau $\\to$ transition $\\to$ convergence) observed on Qwen are absent; Llama-3 shows a weak, gradual rise without a sharp phase transition. This suggests the MSE+gate\\_div loss design, while effective for Qwen, does not transfer well to Llama-3's optimization landscape.\n\nTable~\\ref{tab:llama_eval} presents the three-way evaluation on Llama-3.\n\n\\begin{table}[h]\n\\centering\n\\caption{Llama-3.1-8B three-way evaluation (Base / TG / LoRA-only).}\n\\label{tab:llama_eval}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GAR-D mid & GAR-O mid & PPL & Train GAR & Gap \\\\\n\\midrule\nBase       & 0.0135 & 0.0182 & 3.85 & --   & -- \\\\\nTG (v7)    & 0.038  & 0.045  & 2.48 & 0.09 & 2.4$\\times$ \\\\\nLoRA-only  & 0.025  & 0.031  & 2.42 & --   & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe training-inference gap on Llama-3 is only 2.4$\\times$ (0.09$\\to$0.038), dramatically smaller than Qwen's 15$\\times$. ThreadGate shows a marginal advantage over LoRA-only ($\\Delta$=0.013, $p$=0.06) that is directionally consistent across both architectures but not statistically significant. PPL shows a negligible penalty for gating (2.48 vs.\\ 2.42).\n\n\\subsection{Cross-Architecture Comparison}\n\nTable~\\ref{tab:crossmodel} synthesizes the cross-architecture comparison.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen-2.5-7B & Llama-3.1-8B \\\\\n\\midrule\nBase GAR (Dongre mid)     & 0.003        & 0.0135 \\\\\nGAR relative drop         & 71\\%         & 48\\% \\\\\nTraining GAR peak         & 0.48         & 0.09 \\\\\nInference GAR (TG Dongre) & 0.016--0.032 & 0.038 \\\\\nGap ratio                 & 15--30$\\times$     & 2.4$\\times$ \\\\\nTG $-$ LoRA $\\Delta$GAR   & 0.002--0.010 & 0.013 \\\\\nGate reversal fraction    & 96\\%         & 34\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two architectures exhibit qualitatively different failure profiles. Qwen shows severe GAR degradation, successful training-time optimization but dramatic inference failure, and near-universal gate reversal. Llama-3 shows moderate GAR degradation, poor training convergence, a small training-inference gap, and limited gate reversal. These differences likely stem from architectural factors (GQA configuration, pretraining data distribution) and indicate that both the severity of multi-turn attention degradation and the feasibility of gating interventions are architecture-dependent.\n\n\\subsection{Gradient Conflict Analysis}\n\nWe measure per-layer cosine similarity and magnitude ratio between NTP and GAR gradients on gate parameters across three epoch checkpoints.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer NTP vs.\\ GAR gradient statistics on Qwen v7 (selected layers across 3 epochs).}\n\\label{tab:grad_qwen}\n\\begin{tabular}{lccccc}\n\\toprule\nLayer & Ep0 cos & Ep1 cos & Ep2 cos & Stable? & Avg mag ratio \\\\\n\\midrule\nL3  & $-$0.048 & $-$0.022 & $-$0.041 & Yes (neg) & 5.8 \\\\\nL4  & $-$0.052 & $-$0.018 & $-$0.039 & Yes (neg) & 6.2 \\\\\nL14 & $-$0.039 & $-$0.011 & $-$0.028 & Yes (neg) & 4.9 \\\\\nL1  & +0.021 & +0.035 & +0.018 & Yes (pos) & 3.1 \\\\\nL15 & $-$0.018 & +0.029 & $-$0.007 & No & 4.5 \\\\\nL22 & +0.012 & $-$0.031 & +0.008 & No & 5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, cosine similarity between NTP and GAR gradients is small in magnitude (mean $-$0.031 to $+$0.008 across epochs) with high variance (std 0.038--0.045). Only 9 of 28 layers show sign-stable cosine similarity across checkpoints; the remaining 19 exhibit sign flips. NTP gradient magnitude consistently exceeds GAR by 3.8--6.1$\\times$ (range 2.1--7.8$\\times$). The magnitude asymmetry is the more robust signal: even without consistent directional conflict, NTP gradients dominate gate parameter updates.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient conflict comparison: Qwen vs.\\ Llama-3.}\n\\label{tab:grad_cross}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Qwen & Llama-3 \\\\\n\\midrule\ncos\\_sim mean            & $-$0.031 to $+$0.008 & $+$0.012 \\\\\nSign-stable layers       & 9/28 (32\\%) & 7/32 (22\\%) \\\\\nmag\\_ratio mean          & 5.2 & 3.2 \\\\\nOverall direction        & weakly conflicting & not conflicting \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Llama-3, the overall cosine similarity is positive ($+$0.012), indicating no directional conflict between NTP and GAR gradients. The magnitude ratio is also smaller (3.2$\\times$). The absence of gradient conflict on Llama-3 is consistent with its poor training convergence (GAR peaks at only 0.09): when GAR loss is near-saturated, its gradients approach noise, making cosine similarity measurements unreliable. We therefore treat gradient conflict as supporting evidence for the Qwen case study rather than a general mechanistic claim.\n\n\\subsection{Downstream Task: Instruction Retention}\n\nTo assess whether GAR captures a practically meaningful phenomenon, we measure instruction retention---the ability to follow system prompt constraints---across conversation turns (Table~\\ref{tab:downstream}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction retention across turns (downstream sanity check, Qwen).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Turn 1 & Turn 10 & Drop \\\\\n\\midrule\nBase       & 0.82 & 0.61 & 25.6\\% \\\\\nTG (v7)    & 0.84 & 0.63 & 25.0\\% \\\\\nLoRA-only  & 0.83 & 0.62 & 25.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction retention degrades by approximately 25\\% from turn 1 to turn 10 across all models, confirming that multi-turn degradation is a real downstream phenomenon. However, GAR correlates only weakly with instruction retention ($r$=0.31, $p$=0.18), and ThreadGate provides negligible improvement over LoRA-only ($\\Delta$=0.01). This suggests GAR captures part of the multi-turn degradation mechanism but is not a precise proxy for task-level performance.\n\n\\subsection{Attention Heatmap Visualization}\n\nWe visualize attention patterns across four models (Base / TG / UG / LoRA-only) on three conversations across all 28 Qwen layers. Base attention to goal tokens is diffuse and declines over turns. ThreadGate and LoRA-only patterns are visually indistinguishable at turns beyond 10. Only layers L3, L4, and L12---where gates deviate most from identity---show any visible difference, but this difference is within the noise range of cross-conversation variability. We include these visualizations in the supplementary material as they confirm the quantitative findings (gating provides minimal incremental attention redistribution at inference) but do not add independent mechanistic insight.\n\n% =========================================================================\n\\section{Analysis}\n\n\\subsection{Failure Mode Taxonomy}\n\nOur experiments reveal three coupled failure modes of residual gating under NTP dominance:\n\n\\paragraph{FM1: Reverse turn conditioning.}\nOn Qwen, 96\\% of layers (27/28) develop gates with negative turn-GAR correlation: gates suppress more strongly at early turns (where GAR is naturally higher) and become passive at late turns (where intervention is most needed). This occurs because NTP loss, which dominates gate gradients by 3--6$\\times$, pushes gates toward identity to preserve language modeling quality. At late turns where NTP loss is highest, the push toward identity is strongest, precisely counteracting the intended GAR-recovery behavior. On Llama-3, this reversal is limited to 34\\% of layers, consistent with its lower NTP-GAR gradient magnitude ratio (3.2$\\times$).\n\n\\paragraph{FM2: Training-inference distribution shift.}\nDuring training under teacher forcing, the model observes gold context and learns attention patterns conditioned on this distribution. At inference, the model conditions on its own generated tokens, creating a distributional mismatch. On Qwen, this manifests as a 15$\\times$ gap between training GAR (0.48) and held-out inference GAR (0.032). The gap is dramatically smaller on Llama-3 (2.4$\\times$), partly because training GAR itself is much lower (0.09), yielding less room for distribution shift to erode gains.\n\n\\paragraph{FM3: Insufficient intervention magnitude.}\nAt inference, Qwen gates cluster near identity (mean 0.934, range 0.891--0.996), attenuating residual updates by only 2--7\\%. This attenuation is far too weak to meaningfully redistribute attention. Llama-3 gates are even closer to identity (mean 0.962, range 0.891--0.996). The insufficient magnitude is a consequence of FM1: NTP dominance prevents gates from learning aggressive intervention strategies.\n\n\\subsection{Architecture-Dependent Susceptibility}\n\nThe cross-architecture comparison reveals that susceptibility to multi-turn attention degradation---and to residual gating failure---varies substantially by architecture. Llama-3's base GAR (0.0135) is 4.5$\\times$ higher than Qwen's (0.003), suggesting that Llama-3's attention distribution is inherently more robust to context lengthening. This higher baseline robustness means there is less room for degradation and less need for gating intervention. The architectural differences (GQA configuration, pretraining data distribution, model depth) likely contribute to this divergence, though isolating individual factors is beyond our scope.\n\n\\subsection{Gradient Conflict: Supporting Evidence with Caveats}\n\nThe gradient conflict analysis provides partial mechanistic insight but with important limitations. On Qwen, NTP gradient magnitude consistently exceeds GAR by 3--6$\\times$, supporting the claim that NTP dominates gate updates. However, directional conflict (negative cosine similarity) is noisy: only 9/28 layers show stable negative cosine across epochs, and epoch 1 shows near-zero or positive mean cosine similarity, suggesting transient alignment during rapid GAR improvement phases. On Llama-3, there is no directional conflict (positive cosine), and magnitude asymmetry is smaller (3.2$\\times$). We interpret gradient conflict as one contributing factor to gate reversal on Qwen, not as a universal mechanism.\n\n\\subsection{GAR as a Proxy Metric}\n\nThe weak correlation between GAR and instruction retention ($r$=0.31) raises the question of why GAR warrants study. We argue that attention mechanism analysis remains valuable independent of downstream task correlation: (1) the 25\\% instruction retention drop confirms multi-turn degradation is real; (2) GAR captures the attention-level component of this degradation, which may combine with other mechanisms (positional encoding effects, context window saturation) to produce the downstream effect; (3) understanding why attention steering fails at the mechanism level informs the design of future interventions even if GAR is not a perfect proxy.\n\n% =========================================================================\n\\section{Discussion}\n\n\\subsection{Implications for Auxiliary Attention Losses}\n\nOur results suggest that any auxiliary attention loss optimized under teacher forcing faces distribution shift at inference. The 15$\\times$ gap on Qwen, while less dramatic than initial estimates, represents a substantial generalization failure. That this gap is only 2.4$\\times$ on Llama-3 does not invalidate the concern---it indicates that vulnerability is architecture-dependent, and practitioners cannot know a priori whether their target architecture is closer to the Qwen or Llama-3 regime.\n\n\\subsection{Limitations}\n\nSeveral limitations constrain our conclusions. First, our study covers only two architectures (Qwen-2.5-7B, Llama-3.1-8B) at the 7--8B scale; larger models and different architecture families may behave differently. Second, the marginal positive signal from gating ($\\Delta$=0.010--0.013 across architectures, $p$=0.06--0.08) leaves open the possibility that gating provides a small real benefit obscured by limited statistical power. Third, GAR's weak correlation with downstream performance ($r$=0.31) limits the practical significance of our attention-level findings. Fourth, our loss design space, while spanning seven configurations, does not exhaust all possibilities---reinforcement learning-based approaches, inference-time intervention, or exposure bias mitigation techniques remain unexplored. Fifth, gradient conflict analysis is noisy and architecture-dependent, limiting its value as a standalone mechanistic claim.\n\n\\subsection{Future Directions}\n\nOur failure mode taxonomy suggests several promising directions: (1) \\textbf{inference-time attention intervention} that bypasses the training-inference distribution shift entirely by modifying attention at generation time; (2) \\textbf{decoupled goal-processing pathways} that maintain a separate channel for goal information outside the main residual stream; (3) \\textbf{GAR-aware decoding} strategies that incorporate attention distribution quality into the generation process; (4) \\textbf{exposure bias mitigation} techniques (scheduled sampling, sequence-level training) applied to auxiliary attention losses to reduce the training-inference distributional mismatch.\n\n% =========================================================================\n\\section{Conclusion}\n\nWe present a mechanistic case study of residual gating for multi-turn attention recovery, focusing on failure modes under next-token prediction dominance. Through systematic exploration of seven loss configurations and four-way ablation on Qwen-2.5-7B, complemented by cross-architecture analysis on Llama-3.1-8B, we identify three coupled failure mechanisms: reverse turn conditioning, training-inference distribution shift (15$\\times$ on Qwen, 2.4$\\times$ on Llama-3), and insufficient gate intervention magnitude. Gating provides only marginal, non-significant improvement over LoRA-only adaptation, and both the severity of multi-turn degradation and the nature of gating failure are architecture-dependent. Our failure mode taxonomy and design space exploration provide negative baselines and mechanistic insights for future work on attention steering in multi-turn dialogue.\n\n% =========================================================================\n\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026gar}\nDongre, A., et~al. (2026).\n\\newblock Goal attention degradation in multi-turn dialogue: Measurement, mechanisms, and implications.\n\\newblock \\emph{Proceedings of ACL 2026}.\n\n\\bibitem[Elbayad et~al.(2020)]{elbayad2020depth}\nElbayad, M., Gu, J., Grave, E., and Auli, M. (2020).\n\\newblock Depth-adaptive transformer.\n\\newblock \\emph{Proceedings of ICLR 2020}.\n\n\\bibitem[Li et~al.(2023)]{li2023iti}\nLi, K., Patel, O., Vi{\\'e}gas, F., Pfister, H., and Wattenberg, M. (2023).\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock \\emph{Proceedings of NeurIPS 2023}.\n\n\\bibitem[Liu et~al.(2016)]{liu2016attn}\nLiu, L., Utiyama, M., Finch, A., and Sumita, E. (2016).\n\\newblock Neural machine translation with supervised attention.\n\\newblock \\emph{Proceedings of COLING 2016}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nRanzato, M., Chopra, S., Auli, M., and Zaremba, W. (2016).\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock \\emph{Proceedings of ICLR 2016}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nBengio, S., Vinyals, O., Jaitly, N., and Shazeer, N. (2015).\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock \\emph{Proceedings of NeurIPS 2015}.\n\n\\bibitem[Shazeer et~al.(2017)]{shazeer2017moe}\nShazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., and Dean, J. (2017).\n\\newblock Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.\n\\newblock \\emph{Proceedings of ICLR 2017}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ca9bbffa-7606-4fe8-975d-ffc19ec4fe6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "5bdd2c9f-97ce-4cec-b6a3-d20fc2076291",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper with residual gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Tool call

_source line 23 · 2026-05-19T14:25:05.625Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TL5kjgKK2P6YQhNtHVJ3zu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdd2c9f-97ce-4cec-b6a3-d20fc2076291",
  "isSidechain": false,
  "requestId": "req_011CbC5ePEzixPwZAUwHL5SS",
  "type": "assistant",
  "uuid": "20846539-2f13-4e62-8289-036a6b0179a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYLWdwnjK3CTUFD4i6fhEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9030,
      "cache_read_input_tokens": 41427,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 41427,
          "cache_creation_input_tokens": 9030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9030
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

_source line 24 · 2026-05-19T14:25:07.104Z_

<details><summary>↩ Tool result · `toolu_01TL5kjgKK2P6YQhNtHVJ3zu`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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

Package natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l
ine 29.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/en
c/dvips/cm-super/cm-super-t1.enc}]

Package natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l
ine 43.


Package natbib Warning: Citation `elbayad2020depth' on page 2 undefined on inpu
t line 46.


Package natbib Warning: Citation `shazeer2017moe' on page 2 undefined on input 
line 46.


Package natbib Warning: Citation `liu2016attn' on page 2 undefined on input lin
e 49.


Package natbib Warning: Citation `li2023iti' on page 2 undefined on input line 
49.


Package natbib Warning: Citation `ranzato2016sequence' on page 2 undefined on i
nput line 49.


Package natbib Warning: Citation `bengio2015scheduled' on page 2 undefined on i
nput line 49.

[2]

LaTeX Warning: Reference `tab:heldout_4way' on page 3 undefined on input line 1
01.

[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]

LaTeX Warning: Reference `tab:gap' on page 4 undefined on input line 123.


LaTeX Warning: Reference `tab:llama_diag' on page 4 undefined on input line 143
.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:llama_training' on page 4 undefined on input line
 171.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: Reference `tab:llama_eval' on page 5 undefined on input line 192
.


LaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 213
.


LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: Reference `tab:downstream' on page 6 undefined on input line 280
.

[6] [7]
Overfull \hbox (6.3947pt too wide) in paragraph at lines 321--322
\T1/cmr/m/n/10.95 The cross-architecture com-par-i-son re-veals that sus-cep-ti
-bil-ity to multi-turn at-ten-tion degradation---
[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><
/usr/share/texmf/fonts/type1/public/cm-super/sfbx1000.pfb>&lt;/usr/share/texmf/fon
ts/type1/public/cm-super/sfbx1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-s
uper/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1440.pfb>&lt;/
usr/share/texmf/fonts/type1/public/cm-super/sfrm0800.pfb>&lt;/usr/share/texmf/font
s/type1/public/cm-super/sfrm1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-su
per/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1200.pfb>&lt;/u
sr/share/texmf/fonts/type1/public/cm-super/sfrm1728.pfb>&lt;/usr/share/texmf/fonts
/type1/public/cm-super/sfti1095.pfb>
Output written on paper.pdf (9 pages, 316856 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-
super-t1.enc}] [2] [3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.en
c}]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5] [6] [7]
Overfull \hbox (6.3947pt too wide) in paragraph at lines 321--322
\T1/cmr/m/n/10.95 The cross-architecture com-par-i-son re-veals that sus-cep-ti
-bil-ity to multi-turn at-ten-tion degradation---
[8] [9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><
/usr/share/texmf/fonts/type1/public/cm-super/sfbx1000.pfb>&lt;/usr/share/texmf/fon
ts/type1/public/cm-super/sfbx1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-s
uper/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1440.pfb>&lt;/
usr/share/texmf/fonts/type1/public/cm-super/sfrm0800.pfb>&lt;/usr/share/texmf/font
s/type1/public/cm-super/sfrm1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-su
per/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1200.pfb>&lt;/u
sr/share/texmf/fonts/type1/public/cm-super/sfrm1728.pfb>&lt;/usr/share/texmf/fonts
/type1/public/cm-super/sfti1095.pfb>
Output written on paper.pdf (9 pages, 320031 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20846539-2f13-4e62-8289-036a6b0179a9",
  "isSidechain": false,
  "promptId": "ce64fa14-0076-4da1-ab2f-f34b7643b09a",
  "type": "user",
  "uuid": "cdecb7bd-62f6-43c4-b577-290f3999f4bf",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `dongre2026gar' on page 1 undefined on input l\nine 29.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/en\nc/dvips/cm-super/cm-super-t1.enc}]\n\nPackage natbib Warning: Citation `dongre2026gar' on page 2 undefined on input l\nine 43.\n\n\nPackage natbib Warning: Citation `elbayad2020depth' on page 2 undefined on inpu\nt line 46.\n\n\nPackage natbib Warning: Citation `shazeer2017moe' on page 2 undefined on input \nline 46.\n\n\nPackage natbib Warning: Citation `liu2016attn' on page 2 undefined on input lin\ne 49.\n\n\nPackage natbib Warning: Citation `li2023iti' on page 2 undefined on input line \n49.\n\n\nPackage natbib Warning: Citation `ranzato2016sequence' on page 2 undefined on i\nnput line 49.\n\n\nPackage natbib Warning: Citation `bengio2015scheduled' on page 2 undefined on i\nnput line 49.\n\n[2]\n\nLaTeX Warning: Reference `tab:heldout_4way' on page 3 undefined on input line 1\n01.\n\n[3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.enc}]\n\nLaTeX Warning: Reference `tab:gap' on page 4 undefined on input line 123.\n\n\nLaTeX Warning: Reference `tab:llama_diag' on page 4 undefined on input line 143\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:llama_training' on page 4 undefined on input line\n 171.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: Reference `tab:llama_eval' on page 5 undefined on input line 192\n.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 213\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: Reference `tab:downstream' on page 6 undefined on input line 280\n.\n\n[6] [7]\nOverfull \\hbox (6.3947pt too wide) in paragraph at lines 321--322\n\\T1/cmr/m/n/10.95 The cross-architecture com-par-i-son re-veals that sus-cep-ti\n-bil-ity to multi-turn at-ten-tion degradation---\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><\n/usr/share/texmf/fonts/type1/public/cm-super/sfbx1000.pfb>&lt;/usr/share/texmf/fon\nts/type1/public/cm-super/sfbx1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-s\nuper/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1440.pfb>&lt;/\nusr/share/texmf/fonts/type1/public/cm-super/sfrm0800.pfb>&lt;/usr/share/texmf/font\ns/type1/public/cm-super/sfrm1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-su\nper/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1200.pfb>&lt;/u\nsr/share/texmf/fonts/type1/public/cm-super/sfrm1728.pfb>&lt;/usr/share/texmf/fonts\n/type1/public/cm-super/sfti1095.pfb>\nOutput written on paper.pdf (9 pages, 316856 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-\nsuper-t1.enc}] [2] [3{/usr/share/texmf/fonts/enc/dvips/cm-super/cm-super-ts1.en\nc}]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] [6] [7]\nOverfull \\hbox (6.3947pt too wide) in paragraph at lines 321--322\n\\T1/cmr/m/n/10.95 The cross-architecture com-par-i-son re-veals that sus-cep-ti\n-bil-ity to multi-turn at-ten-tion degradation---\n[8] [9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb><\n/usr/share/texmf/fonts/type1/public/cm-super/sfbx1000.pfb>&lt;/usr/share/texmf/fon\nts/type1/public/cm-super/sfbx1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-s\nuper/sfbx1200.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfbx1440.pfb>&lt;/\nusr/share/texmf/fonts/type1/public/cm-super/sfrm0800.pfb>&lt;/usr/share/texmf/font\ns/type1/public/cm-super/sfrm1000.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-su\nper/sfrm1095.pfb>&lt;/usr/share/texmf/fonts/type1/public/cm-super/sfrm1200.pfb>&lt;/u\nsr/share/texmf/fonts/type1/public/cm-super/sfrm1728.pfb>&lt;/usr/share/texmf/fonts\n/type1/public/cm-super/sfti1095.pfb>\nOutput written on paper.pdf (9 pages, 320031 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "20846539-2f13-4e62-8289-036a6b0179a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T14:25:15.458Z_

编译成功，9 页 PDF。所有 8 个实验均有对应 section/table，论文按 narrative guidance 重构为 Qwen 单模型深度案例研究 + Llama-3 architecture-dependent susceptibility 分析，claims 已弱化至 worst tier 水平。

输出：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdecb7bd-62f6-43c4-b577-290f3999f4bf",
  "isSidechain": false,
  "requestId": "req_011CbC5epAwQgvUVuRZXa39N",
  "type": "assistant",
  "uuid": "aaa16d0d-3f12-4669-b1e1-d80f36ded19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KY1LrMCZcjarbPhhoCz5X8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6208,
      "cache_read_input_tokens": 50457,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 50457,
          "cache_creation_input_tokens": 6208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6208
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T135115 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "aaa16d0d-3f12-4669-b1e1-d80f36ded19d",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper with residual gating",
  "sessionId": "063c223b-1298-4925-9492-76a20e766aab"
}
```

---
