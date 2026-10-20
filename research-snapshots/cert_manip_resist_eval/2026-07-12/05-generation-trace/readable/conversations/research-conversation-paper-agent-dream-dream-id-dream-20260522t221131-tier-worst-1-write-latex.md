# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/2cac05a0-8109-400b-99cb-690453d4755b.jsonl`
- **Structured JSON:** [`c2f1cc54b439f01e486f.json`](../../sessions/c2/c2f1cc54b439f01e486f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T22:45:01.185Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T22:45:01.185Z",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：η_max dominance叙事作为主要claim坍塌。Bootstrap η_max降至3/12，与K_eff的1/12相比dominance ratio仅3:1→实质上两个predictor都不robust。 VIF >7确认η_max与K_eff在当前设计下无法可靠分离。RF contrast的GO/NO-GO gate失败——K_eff在random faults下也仅0-1/2显著，BFT类比失去实证基础。 GAM 6:6 split在bootstrap CI下退化为3-4/6 per category并出现2个reversal，clean taxonomy不成立。 Bayesian K_eff方向翻转在clustered SE下消失（0-1/7 negative）。ARC benchmark几乎全部NS——实质上是single-benchmark study。 论文必须彻底重构。Salvage路径：(A) 方法学贡献——OLS→bootstrap显著性collapse（η_max 11→3, K_eff 8→1）作为headline finding， 为LLM-as-judge评测文献提供non-independence correction framework；(B) 数据资源贡献——15模型455 panels的adversarial评测数据集； (C) 聚合规则作为独立发现——即使η_max vs K_eff分解不可靠，threshold R²=0.89 vs Bayesian R²=0.10的gradient仍成立。 目标EMNLP Findings（Overall ~2.5-3.0），Main几乎不可能。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T22:45:01.189Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T22:45:01.189Z",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-22T22:45:01.215Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：η_max dominance叙事作为主要claim坍塌。Bootstrap η_max降至3/12，与K_eff的1/12相比dominance ratio仅3:1→实质上两个predictor都不robust。 VIF >7确认η_max与K_eff在当前设计下无法可靠分离。RF contrast的GO/NO-GO gate失败——K_eff在random faults下也仅0-1/2显著，BFT类比失去实证基础。 GAM 6:6 split在bootstrap CI下退化为3-4/6 per category并出现2个reversal，clean taxonomy不成立。 Bayesian K_eff方向翻转在clustered SE下消失（0-1/7 negative）。ARC benchmark几乎全部NS——实质上是single-benchmark study。 论文必须彻底重构。Salvage路径：(A) 方法学贡献——OLS→bootstrap显著性collapse（η_max 11→3, K_eff 8→1）作为headline finding， 为LLM-as-judge评测文献提供non-independence correction framework；(B) 数据资源贡献——15模型455 panels的adversarial评测数据集； (C) 聚合规则作为独立发现——即使η_max vs K_eff分解不可靠，threshold R²=0.89 vs Bayesian R²=0.10的gradient仍成立。 目标EMNLP Findings（Overall ~2.5-3.0），Main几乎不可能。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "dc2409ba-3d9e-4a22-9e5d-441a5c2604e6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T22:45:01.215Z_

```json
{
  "parentUuid": "dc2409ba-3d9e-4a22-9e5d-441a5c2604e6",
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
  "uuid": "645ca05f-21a6-412a-a7a5-36e1f7d8bde6",
  "timestamp": "2026-05-22T22:45:01.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T22:45:01.215Z_

```json
{
  "parentUuid": "645ca05f-21a6-412a-a7a5-36e1f7d8bde6",
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
  "uuid": "9c62efe2-0ca8-4a00-854f-9cd7eff2b2e0",
  "timestamp": "2026-05-22T22:45:01.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T22:45:01.215Z_

```json
{
  "parentUuid": "9c62efe2-0ca8-4a00-854f-9cd7eff2b2e0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "09aaa6fb-13b3-4ade-be9c-ff091d1aef33",
  "timestamp": "2026-05-22T22:45:01.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
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
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Assistant

_source line 8 · 2026-05-22T22:45:08.086Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09aaa6fb-13b3-4ade-be9c-ff091d1aef33",
  "isSidechain": false,
  "requestId": "req_011CbJRCZGsQTKWcN5Aiw1sp",
  "type": "assistant",
  "uuid": "83354064-ee00-4033-b5cc-a0518229712c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C57yTT8zeTeExf1CBqKCsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12463
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

_source line 9 · 2026-05-22T22:45:08.244Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EJDZNExTc1JK2xtAg7q8mz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83354064-ee00-4033-b5cc-a0518229712c",
  "isSidechain": false,
  "requestId": "req_011CbJRCZGsQTKWcN5Aiw1sp",
  "type": "assistant",
  "uuid": "51b538ef-1ac3-4f69-bdd5-2dba5d5c4520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C57yTT8zeTeExf1CBqKCsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12463
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

_source line 10 · 2026-05-22T22:45:08.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Um2omHne7eiNvW8WDCAVjC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51b538ef-1ac3-4f69-bdd5-2dba5d5c4520",
  "isSidechain": false,
  "requestId": "req_011CbJRCZGsQTKWcN5Aiw1sp",
  "type": "assistant",
  "uuid": "bb97159c-9a4b-4990-8724-add297295061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C57yTT8zeTeExf1CBqKCsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12463,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12463
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

_source line 11 · 2026-05-22T22:45:08.411Z_

<details><summary>↩ Tool result · `toolu_01Um2omHne7eiNvW8WDCAVjC`</summary>

```text
1	# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)
2	
3	> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.
4	
5	## Target
6	EMNLP 2026 (via ARR)
7	
8	## Title Candidates
9	1. "The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack"
10	2. "Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"
11	3. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer" (softened with honest reporting)
12	
13	## Core Insight
14	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).
15	
16	## Hook
17	"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense."
18	
19	## Novelty Positioning
20	We do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:
21	1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)
22	2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts
23	3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)
24	4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)
25	5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)
26	6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)
27	7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs
28	
29	## Core Claims
30	
31	### Claim 1 (Primary): Weakest-Link Dominance
32	**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.
33	**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):
34	- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)
35	- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence
36	- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.
37	- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2
38	- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)
39	- SE inflation ~2.5x (consistent with 91/455 panel overlap)
40	- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.
41	- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.
42	- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.
43	- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.
44	**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.
45	**Headline**: "η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not."
46	
47	### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split
48	**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.
49	**Evidence**: GAM partial effects, 455 panels, 12 conditions.
50	- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions
51	- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions
52	- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values
53	**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).
54	
55	### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability
56	**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.
57	**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):
58	- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):
59	  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error
60	  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)
61	  - R² = 0.73-0.81 (highly predictable)
62	- **Adaptive regime** (D021):
63	  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction
64	  - R² substantially lower
65	- **Contrast**: NOT "diversity helps under RF but hurts under adaptive" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence
66	- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not
67	**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.
68	**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.
69	
70	### Claim 3 (Empirical): Diversity-Capability Tradeoff
71	**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.
72	**Evidence**:
73	- K_eff-η_max correlation: r = +0.700 (15-model)
74	- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max
75	- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The "independent predictive effect" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.
76	**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.
77	**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.
78	
79	### Claim 4 (Methodological): Family Labels ≠ Diversity
80	**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
81	**Evidence**:
82	- 6-model: Mann-Whitney U p=0.206, permutation p=0.427
83	- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.
84	- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)
85	**Strength**: Moderate. Consistent across 6→15 model scaling.
86	
87	### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation
88	**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.
89	**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.
90	**Disposition**: Remove as independent contribution. Optionally note in analysis: "Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence."
91	**Strength**: DEAD as independent claim. May retain as minor observation.
92	
93	### Claim 6 (Practical): Robustness-First Panel Design
94	**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
95	**Evidence** (15-model, 455 panels — fully validated):
96	- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)
97	- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)
98	- Robust across panel sizes K=10, 20, 50
99	- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff
100	- Consistent with canonical regression: η_max 11/12 dominant
101	**Strength**: Strong (15-model fully confirmed). Zero failure conditions.
102	
103	### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers
104	**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).
105	**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):
106	- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)
107	- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive
108	- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity
109	- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104
110	- Key findings:
111	  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)
112	  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)
113	  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm
114	  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)
115	  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)
116	**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.
117	
118	## Contribution Stack (ordered by strength, post-D019 reframe)
119	1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)
120	2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)
121	3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)
122	4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)
123	5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)
124	6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)
125	7. **Family label unreliability** — methodological (confirmed at 15-model scale)
126	7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)
127	~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)
128	
129	## Anticipated Reviewer Concerns
130	
131	### RC1: "K_eff positive is just confound with η_max"
132	**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.
133	
134	### RC2: "Why does diversity hurt? What's the mechanism?"
135	**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.
136	
137	### RC3: "Only 15 models — does this generalize?"
138	**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).
139	
140	### RC4: "BFT comparison is a strawman"
141	**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.
142	
143	### RC5: "Why not just use the strongest models?"
144	**Response**: (a) "Strongest" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.
145	
146	### RC6: "No theoretical novelty"
147	**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.
148	
149	### RC7: "Why not just use Bayesian aggregation?"
150	**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.
151	
152	### RC8: "6-model and 15-model results contradict — which is right?"
153	**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.
154	
155	### RC9 (new): "arc×sycophancy exception undermines your claim"
156	**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.
157	
158	## "When Diversity Helps" Section
159	Diversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:
160	1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
161	2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.
162	3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
163	4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.
164	
165	## Story Arc (v5: Post-D019 Reframe)
166	1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
167	2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
168	3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations
169	4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression
170	5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)
171	6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack
172	7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb97159c-9a4b-4990-8724-add297295061",
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "ef0f6adf-cef4-42cf-ac8d-81226a3c0f36",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper_framing.md",
      "content": "# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)\n\n> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack\"\n2. \"Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation\"\n3. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\" (softened with honest reporting)\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).\n\n## Hook\n\"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense.\"\n\n## Novelty Positioning\nWe do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:\n1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)\n2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts\n3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)\n4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)\n5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)\n6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)\n7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs\n\n## Core Claims\n\n### Claim 1 (Primary): Weakest-Link Dominance\n**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.\n**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)\n- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence\n- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.\n- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2\n- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)\n- SE inflation ~2.5x (consistent with 91/455 panel overlap)\n- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.\n- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.\n- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.\n- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.\n**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.\n**Headline**: \"η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not.\"\n\n### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split\n**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.\n**Evidence**: GAM partial effects, 455 panels, 12 conditions.\n- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions\n- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions\n- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values\n**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).\n\n### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability\n**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.\n**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):\n- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):\n  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error\n  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)\n  - R² = 0.73-0.81 (highly predictable)\n- **Adaptive regime** (D021):\n  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction\n  - R² substantially lower\n- **Contrast**: NOT \"diversity helps under RF but hurts under adaptive\" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence\n- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not\n**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.\n**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max\n- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The \"independent predictive effect\" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.\n**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.\n**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**:\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\n**Strength**: Moderate. Consistent across 6→15 model scaling.\n\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\"\n**Strength**: DEAD as independent claim. May retain as minor observation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence** (15-model, 455 panels — fully validated):\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\n- Robust across panel sizes K=10, 20, 50\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\n- Consistent with canonical regression: η_max 11/12 dominant\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)\n- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity\n- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104\n- Key findings:\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)\n  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm\n  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\n**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\n\n## Contribution Stack (ordered by strength, post-D019 reframe)\n1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)\n2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)\n3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)\n4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)\n5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)\n6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)\n7. **Family label unreliability** — methodological (confirmed at 15-model scale)\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\n\n### RC8: \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n### RC9 (new): \"arc×sycophancy exception undermines your claim\"\n**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.\n\n## \"When Diversity Helps\" Section\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.\n\n## Story Arc (v5: Post-D019 Reframe)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations\n4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression\n5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)\n6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack\n7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  },
  "sourceToolAssistantUUID": "bb97159c-9a4b-4990-8724-add297295061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "ef0f6adf-cef4-42cf-ac8d-81226a3c0f36",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Tool result

_source line 14 · 2026-05-22T22:45:08.620Z_

<details><summary>↩ Tool result · `toolu_01EJDZNExTc1JK2xtAg7q8mz`</summary>

```text
1	[
2	  {
3	    "name": "Scale expansion: 15 models with API + large open-source",
4	    "description": "将模型池从6扩展到15（加入GPT-4o-mini, GPT-4o, GPT-4.1, GPT-4.1-mini, Llama-3.1-70B, Qwen2.5-72B等）， 重跑MI矩阵 + C(15,3)=455 panels回归 + bootstrap/clustered SE/mixed effects全套correction。\n",
5	    "results": {
6	      "total_models": 15,
7	      "total_panels": 455,
8	      "total_conditions": 12,
9	      "confound_mean_abs_r": 0.72,
10	      "canonical_ols_eta_max_sig": "11/12",
11	      "canonical_ols_keff_sig": "8/12",
12	      "canonical_ols_keff_positive": 7,
13	      "canonical_ols_keff_negative": 1,
14	      "wild_cluster_bootstrap_v2_eta_max_sig": "3/12",
15	      "wild_cluster_bootstrap_v2_keff_sig": "1/12",
16	      "clustered_se_eta_max_sig": "5/12",
17	      "clustered_se_keff_sig": "0/12",
18	      "mixed_effects_eta_max_sig": "4/12",
19	      "mixed_effects_keff_sig": "1/12",
20	      "eta_keff_dominance_ratio_bootstrap": 3.0,
21	      "se_inflation_factor": 3.2,
22	      "bootstrap_position_0_eta_sig": "2/12",
23	      "bootstrap_position_1_eta_sig": "5/12",
24	      "bootstrap_position_2_eta_sig": "4/12",
25	      "mmlu_eta_bootstrap_sig": "2/6",
26	      "arc_eta_bootstrap_sig": "1/6",
27	      "keff_practical_delta_asr_iqr_pp": 0.8,
28	      "median_R2": 0.25
29	    },
30	    "tables": [
31	      {
32	        "caption": "OLS vs correction methods: significance counts across 12 conditions",
33	        "columns": [
34	          "Method",
35	          "η_max sig",
36	          "K_eff sig",
37	          "K_eff positive",
38	          "K_eff negative",
39	          "Dominance ratio"
40	        ],
41	        "rows": [
42	          [
43	            "OLS (naive)",
44	            "11/12",
45	            "8/12",
46	            "7",
47	            "1",
48	            "1.4:1"
49	          ],
50	          [
51	            "Clustered SE (CR1, 15 clusters)",
52	            "5/12",
53	            "0/12",
54	            "—",
55	            "—",
56	            "∞"
57	          ],
58	          [
59	            "Mixed effects (random judge intercepts)",
60	            "4/12",
61	            "1/12",
62	            "1",
63	            "0",
64	            "4:1"
65	          ],
66	          [
67	            "Wild cluster bootstrap v2 (max-p)",
68	            "3/12",
69	            "1/12",
70	            "1",
71	            "0",
72	            "3:1"
73	          ],
74	          [
75	            "SE inflation factor",
76	            "—",
77	            "—",
78	            "—",
79	            "—",
80	            "3.2×"
81	          ]
82	        ]
83	      },
84	      {
85	        "caption": "Bootstrap η_max significance by position and benchmark",
86	        "columns": [
87	          "Position",
88	          "MMLU sig/6",
89	          "ARC sig/6",
90	          "Total sig/12",
91	          "Cluster balance (max/min panels)"
92	        ],
93	        "rows": [
94	          [
95	            "Position 0",
96	            "1/6",
97	            "1/6",
98	            "2/12",
99	            "91:1"
100	          ],
101	          [
102	            "Position 1",
103	            "3/6",
104	            "2/6",
105	            "5/12",
106	            "55:12"
107	          ],
108	          [
109	            "Position 2",
110	            "3/6",
111	            "1/6",
112	            "4/12",
113	            "48:15"
114	          ],
115	          [
116	            "Max-p (conservative)",
117	            "2/6",
118	            "1/6",
119	            "3/12",
120	            "—"
121	          ]
122	        ]
123	      },
124	      {
125	        "caption": "Per-condition bootstrap results (12 conditions)",
126	        "columns": [
127	          "Dataset",
128	          "Attack",
129	          "OLS η_max p",
130	          "Bootstrap η_max p",
131	          "OLS K_eff p",
132	          "Bootstrap K_eff p"
133	        ],
134	        "rows": [
135	          [
136	            "MMLU",
137	            "prompt_injection",
138	            "2e-06",
139	            "0.028",
140	            "0.004",
141	            "0.18"
142	          ],
143	          [
144	            "MMLU",
145	            "score_manipulation",
146	            "8e-05",
147	            "0.041",
148	            "0.011",
149	            "0.31"
150	          ],
151	          [
152	            "MMLU",
153	            "sycophancy",
154	            "0.002",
155	            "0.14",
156	            "0.08",
157	            "0.42"
158	          ],
159	          [
160	            "MMLU",
161	            "verbosity_bias",
162	            "0.009",
163	            "0.22",
164	            "0.15",
165	            "0.55"
166	          ],
167	          [
168	            "MMLU",
169	            "position_bias",
170	            "0.001",
171	            "0.08",
172	            "0.035",
173	            "0.04"
174	          ],
175	          [
176	            "MMLU",
177	            "authority_bias",
178	            "0.004",
179	            "0.19",
180	            "0.09",
181	            "0.48"
182	          ],
183	          [
184	            "ARC",
185	            "prompt_injection",
186	            "3e-14",
187	            "0.35",
188	            "0.001",
189	            "0.62"
190	          ],
191	          [
192	            "ARC",
193	            "score_manipulation",
194	            "1e-08",
195	            "0.06",
196	            "0.003",
197	            "0.44"
198	          ],
199	          [
200	            "ARC",
201	            "sycophancy",
202	            "0.013",
203	            "0.52",
204	            "0.24",
205	            "0.71"
206	          ],
207	          [
208	            "ARC",
209	            "verbosity_bias",
210	            "0.031",
211	            "0.61",
212	            "0.18",
213	            "0.68"
214	          ],
215	          [
216	            "ARC",
217	            "position_bias",
218	            "0.006",
219	            "0.28",
220	            "0.008",
221	            "0.33"
222	          ],
223	          [
224	            "ARC",
225	            "authority_bias",
226	            "0.019",
227	            "0.44",
228	            "0.12",
229	            "0.59"
230	          ]
231	        ]
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "这是worst档的核心灾难性结果。OLS给出的\"η_max dominates (11:8)\"在bootstrap correction后坍塌为\"3:1， 且绝对数极低（3/12 vs 1/12）\"。两个predictor在corrected inference下都几乎不显著——不是η_max dominates K_eff， 而是整个regression在corrected inference下statistical power不足。 ARC benchmark尤其脆弱：OLS下最显著的条件（arc×PI, p=3e-14）在bootstrap后完全NS（p=0.35）， 说明该条件的信号几乎entirely来自panel overlap inflation。如果排除ARC，实质上是single-benchmark study（MMLU only）， reviewer会质疑generalizability。SE inflation 3.2×比预期高——可能是cluster size imbalance（91:1） 放大了bootstrap保守性。但这也意味着OLS的所有结论都需要extreme caution来解读。 论文必须pivoting到\"the OLS→bootstrap collapse itself is the finding\"——方法学贡献救场。\n\n\n扩展到15模型后，OLS结果表面上确认η_max dominance（11/12 vs 8/12）。但non-independence correction的冲击远超预期。 Bootstrap v2（3-position max-p, Rademacher weights, B=9999）显示position 0的cluster imbalance问题 （claude-3-haiku=91 panels vs qwen2.5-14b=1）不仅存在于position 0——position 1和2也受cluster size不均影响， 只是程度较轻。3-position max-p取最保守估计，η_max仅3/12存活（全部在MMLU上，ARC仅1/6）。 K_eff在bootstrap下仅1/12——但这与η_max的3/12相比，dominance ratio仅3:1，远不如\"η_max dominates\"的叙事所需的清晰分离。 SE inflation ~3.2×（高于预期的2.5×），说明panel overlap导致的non-independence比initial估计更严重。 根本问题：455 panels来自15个model的C(15,3)组合，每个model出现在C(14,2)=91个panels中——观测值之间的非独立性是结构性的， 不是correction能完全解决的。bootstrap的保守性可能合理反映了真实的statistical power。\n"
236	  },
237	  {
238	    "name": "Attack expansion: few-shot hijacking, persona manipulation, instruction override",
239	    "description": "新增3种攻击类型（few-shot hijacking、persona manipulation、instruction override），在15模型池上运行。 扩展总条件数到18。验证weakest-link在更广泛attack surface上的表现。\n",
240	    "results": {
241	      "new_attack_types": 3,
242	      "total_attack_types": 9,
243	      "total_conditions": 18,
244	      "new_attacks_ols_eta_max_sig": "5/6",
245	      "new_attacks_ols_keff_sig": "3/6",
246	      "new_attacks_bootstrap_eta_max_sig": "1/6",
247	      "new_attacks_bootstrap_keff_sig": "0/6",
248	      "new_attacks_clustered_se_eta_max_sig": "2/6",
249	      "new_attacks_clustered_se_keff_sig": "0/6",
250	      "overall_18cond_bootstrap_eta_sig": "4/18",
251	      "overall_18cond_bootstrap_keff_sig": "1/18",
252	      "overall_18cond_ols_eta_sig": "16/18",
253	      "overall_18cond_ols_keff_sig": "11/18",
254	      "few_shot_hijacking_keff_direction": "positive",
255	      "persona_manipulation_keff_direction": "positive",
256	      "instruction_override_keff_direction": "negative",
257	      "gam_extended_targeted_positive": "4/9",
258	      "gam_extended_sharedbias_negative": "5/9",
259	      "gam_reversals": 3
260	    },
261	    "tables": [
262	      {
263	        "caption": "New attack types: OLS vs bootstrap correction",
264	        "columns": [
265	          "Dataset",
266	          "Attack",
267	          "OLS η_max p",
268	          "Bootstrap η_max p",
269	          "OLS K_eff p",
270	          "Bootstrap K_eff p",
271	          "K_eff direction"
272	        ],
273	        "rows": [
274	          [
275	            "MMLU",
276	            "few-shot-hijacking",
277	            "0.001",
278	            "0.18",
279	            "0.02",
280	            "0.41",
281	            "positive"
282	          ],
283	          [
284	            "MMLU",
285	            "persona-manipulation",
286	            "0.003",
287	            "0.09",
288	            "0.04",
289	            "0.52",
290	            "positive"
291	          ],
292	          [
293	            "MMLU",
294	            "instruction-override",
295	            "0.0005",
296	            "0.04",
297	            "0.08",
298	            "0.38",
299	            "negative"
300	          ],
301	          [
302	            "ARC",
303	            "few-shot-hijacking",
304	            "0.008",
305	            "0.31",
306	            "0.05",
307	            "0.55",
308	            "positive"
309	          ],
310	          [
311	            "ARC",
312	            "persona-manipulation",
313	            "0.012",
314	            "0.22",
315	            "0.09",
316	            "0.63",
317	            "positive"
318	          ],
319	          [
320	            "ARC",
321	            "instruction-override",
322	            "0.002",
323	            "0.12",
324	            "0.11",
325	            "0.48",
326	            "negative"
327	          ]
328	        ]
329	      },
330	      {
331	        "caption": "Extended GAM taxonomy: 9 attacks × 2 benchmarks",
332	        "columns": [
333	          "Attack",
334	          "Category (original)",
335	          "K_eff direction (MMLU)",
336	          "K_eff direction (ARC)",
337	          "Consistent with taxonomy?"
338	        ],
339	        "rows": [
340	          [
341	            "prompt_injection",
342	            "targeted",
343	            "positive",
344	            "positive",
345	            "yes"
346	          ],
347	          [
348	            "score_manipulation",
349	            "targeted",
350	            "positive",
351	            "positive",
352	            "yes"
353	          ],
354	          [
355	            "position_bias",
356	            "targeted",
357	            "positive",
358	            "negative",
359	            "REVERSAL"
360	          ],
361	          [
362	            "few-shot-hijacking",
363	            "targeted",
364	            "positive",
365	            "positive",
366	            "yes but mechanism unclear"
367	          ],
368	          [
369	            "persona-manipulation",
370	            "targeted",
371	            "positive",
372	            "positive",
373	            "yes but weak"
374	          ],
375	          [
376	            "sycophancy",
377	            "shared-bias",
378	            "negative",
379	            "negative",
380	            "yes"
381	          ],
382	          [
383	            "verbosity_bias",
384	            "shared-bias",
385	            "negative",
386	            "positive",
387	            "REVERSAL"
388	          ],
389	          [
390	            "authority_bias",
391	            "shared-bias",
392	            "negative",
393	            "negative",
394	            "yes"
395	          ],
396	          [
397	            "instruction-override",
398	            "shared-bias",
399	            "negative",
400	            "negative",
401	            "yes"
402	          ]
403	        ]
404	      }
405	    ],
406	    "figures": [],
407	    "analysis": "攻击扩展确认了worst档的核心问题：所有新增数据都使用相同的455 panel结构，non-independence问题是structural的， 不会因为添加更多attack types而改善。OLS下看似丰富的结果在bootstrap后一律坍塌。 GAM taxonomy的3个reversal（arc×position_bias方向翻转，mmlu×verbosity_bias方向翻转，加上1个边界case） 使得\"clean 6:6 split\"不再成立。剩下的directional tendency（~60-70%与预测方向一致）在18个condition下 可能仅略好于chance（binomial test p ≈ 0.08-0.15），无法作为independent contribution。\n\n\n新增攻击在OLS下看似确认pattern（5/6 η_max sig, 3/6 K_eff sig），但bootstrap correction后again坍塌 （1/6和0/6）。根本原因相同：455 panels的非独立性问题不因添加新attack types而缓解——每个attack下的panel结构完全相同。 更糟的是，新攻击引入GAM 6:6 split的reversal：few-shot hijacking理论上是targeted attack（需要针对specific model）， 但实证中K_eff方向为正——因为few-shot hijacking利用in-context learning这一所有LLM共享的能力，实际行为更接近shared-bias。 persona manipulation也出现类似anomaly。原先clean的6:6 targeted/shared-bias taxonomy在9种攻击下退化为 4/9 targeted-positive vs 5/9 shared-bias-negative，有3个reversal。taxonomy不再\"clean\"， 而是\"noisy with a directional tendency\"——远不够支撑independent contribution。\n"
408	  },
409	  {
410	    "name": "Random-fault simulation: BFT contrast GO/NO-GO gate",
411	    "description": "Random-fault simulation：每个judge独立以概率η_j fail，majority vote。 对比random faults vs adaptive attacks下K_eff的显著性。 GO/NO-GO GATE：如果random-fault K_eff也不显著→BFT framing彻底坍塌。\n",
412	    "results": {
413	      "rf_conditions": 2,
414	      "rf_ols_keff_sig": "2/2",
415	      "rf_bootstrap_keff_sig": "0/2",
416	      "rf_clustered_se_keff_sig": "1/2",
417	      "rf_ols_eta_sig": "2/2",
418	      "rf_bootstrap_eta_sig": "1/2",
419	      "rf_mmlu_R2": 0.52,
420	      "rf_arc_R2": 0.48,
421	      "rf_keff_std_beta_mmlu": 0.18,
422	      "rf_keff_std_beta_arc": 0.28,
423	      "rf_vs_adaptive_keff_beta_ratio": 1.2,
424	      "rf_vs_adaptive_contrast_p": 0.31,
425	      "rf_vs_adaptive_cohen_d": 0.12,
426	      "go_nogo_gate": "FAIL"
427	    },
428	    "tables": [
429	      {
430	        "caption": "Random-fault vs adaptive: K_eff significance under correction",
431	        "columns": [
432	          "Regime",
433	          "Method",
434	          "η_max sig",
435	          "K_eff sig",
436	          "R²",
437	          "K_eff std β"
438	        ],
439	        "rows": [
440	          [
441	            "Random-fault",
442	            "OLS",
443	            "2/2",
444	            "2/2",
445	            "0.52",
446	            "+0.215"
447	          ],
448	          [
449	            "Random-fault",
450	            "Clustered SE",
451	            "2/2",
452	            "1/2",
453	            "—",
454	            "+0.215"
455	          ],
456	          [
457	            "Random-fault",
458	            "Bootstrap v2",
459	            "1/2",
460	            "0/2",
461	            "—",
462	            "+0.215"
463	          ],
464	          [
465	            "Adaptive",
466	            "OLS",
467	            "11/12",
468	            "8/12",
469	            "0.25",
470	            "+0.164"
471	          ],
472	          [
473	            "Adaptive",
474	            "Clustered SE",
475	            "5/12",
476	            "0/12",
477	            "—",
478	            "+0.164"
479	          ],
480	          [
481	            "Adaptive",
482	            "Bootstrap v2",
483	            "3/12",
484	            "1/12",
485	            "—",
486	            "+0.164"
487	          ]
488	        ]
489	      },
490	      {
491	        "caption": "BFT contrast: effect size analysis",
492	        "columns": [
493	          "Metric",
494	          "Value",
495	          "Threshold for claim",
496	          "Verdict"
497	        ],
498	        "rows": [
499	          [
500	            "K_eff β ratio (RF/adaptive)",
501	            "1.2",
502	            ">2.0",
503	            "FAIL"
504	          ],
505	          [
506	            "Cohen's d (paired)",
507	            "0.12",
508	            ">0.2 (small)",
509	            "FAIL"
510	          ],
511	          [
512	            "Contrast p-value",
513	            "0.31",
514	            "<0.05",
515	            "FAIL"
516	          ],
517	          [
518	            "R² gap (RF - adaptive)",
519	            "0.27",
520	            ">0.3",
521	            "MARGINAL"
522	          ]
523	        ]
524	      }
525	    ],
526	    "figures": [],
527	    "analysis": "GO/NO-GO gate failure是worst档中最具结构性影响的结果。BFT framing是论文theoretical novelty的核心—— 没有\"random fault vs adaptive adversary\"的对比，Claim 2整体坍塌。 但failure的原因是subtle的：不是K_eff在RF下真的不important（R²确实更高）， 而是corrected inference下K_eff的独立效应在任何regime下都不可靠（VIF >7, 15 model clusters太少）。 这实际上reinforces方法学贡献——\"combinatorial panel designs create massive non-independence that makes ANY predictor-level inference unreliable\"——但代价是丧失了theoretical framing。 论文需要将BFT降级为motivation/intuition，而非tested hypothesis。\n\n\nGO/NO-GO gate FAIL。Random-fault regime下K_eff在OLS中显著（2/2），但bootstrap correction后降至0/2。 这不意味着BFT理论错误——而是本实验设计（455 panels, 15 models）的non-independence问题在RF regime下同样存在。 RF regime的R²确实高于adaptive（0.52 vs 0.25），表明panel composition对RF错误的解释力更强， 但K_eff的独立贡献在corrected inference下无法与η_max可靠分离（VIF >7, 见plan_009）。 RF vs adaptive的K_eff β ratio仅1.2×（预期需>2×才能convincingly demonstrate BFT contrast）， Cohen's d = 0.12（远低于small effect size标准0.2）。 BFT framing的核心逻辑——\"diversity helps under random faults but hurts under adaptive\"—— 在实证上无法被本数据支撑。不是因为理论错误，而是因为实验设计的structural non-independence 使得任何K_eff相关的inference都不可靠。BFT对比降级为\"directional observation consistent with theory\"。\n"
528	  },
529	  {
530	    "name": "Capability-matched validation: within-tier K_eff analysis",
531	    "description": "在同一capability tier内（3/3/9分层：3 frontier, 3 strong, 9 mid-weak）， 测试控制η_max variance后K_eff是否显著。\n",
532	    "results": {
533	      "tiers_tested": 3,
534	      "tier_frontier_models": 3,
535	      "tier_frontier_panels": 1,
536	      "tier_strong_models": 3,
537	      "tier_strong_panels": 1,
538	      "tier_midweak_models": 9,
539	      "tier_midweak_panels": 84,
540	      "within_tier_eta_max_sig_frontier": "0/12",
541	      "within_tier_keff_sig_frontier": "0/12",
542	      "within_tier_eta_max_sig_strong": "0/12",
543	      "within_tier_keff_sig_strong": "0/12",
544	      "within_tier_eta_max_sig_midweak": "3/12",
545	      "within_tier_keff_sig_midweak": "0/12",
546	      "cross_tier_eta_max_sig": "11/12",
547	      "cross_tier_keff_sig": "8/12",
548	      "capability_range_eta_r": 0.82,
549	      "within_tier_eta_range_reduction": "75%"
550	    },
551	    "tables": [
552	      {
553	        "caption": "Within-tier vs cross-tier regression significance",
554	        "columns": [
555	          "Scope",
556	          "N models",
557	          "N panels (K=3)",
558	          "η_max sig/12",
559	          "K_eff sig/12",
560	          "η_max range (IQR)"
561	        ],
562	        "rows": [
563	          [
564	            "Frontier (3)",
565	            "3",
566	            "1",
567	            "0/12",
568	            "0/12",
569	            "0.02"
570	          ],
571	          [
572	            "Strong (3)",
573	            "3",
574	            "1",
575	            "0/12",
576	            "0/12",
577	            "0.04"
578	          ],
579	          [
580	            "Mid-weak (9)",
581	            "9",
582	            "84",
583	            "3/12",
584	            "0/12",
585	            "0.11"
586	          ],
587	          [
588	            "Cross-tier (15)",
589	            "15",
590	            "455",
591	            "11/12",
592	            "8/12",
593	            "0.38"
594	          ]
595	        ]
596	      },
597	      {
598	        "caption": "η_max significance vs capability range",
599	        "columns": [
600	          "Analysis",
601	          "Capability range (ASR IQR)",
602	          "η_max sig count",
603	          "Correlation (range vs sig)"
604	        ],
605	        "rows": [
606	          [
607	            "Within frontier",
608	            "0.02",
609	            "0/12",
610	            "r = 0.82"
611	          ],
612	          [
613	            "Within strong",
614	            "0.04",
615	            "0/12",
616	            "—"
617	          ],
618	          [
619	            "Within mid-weak",
620	            "0.11",
621	            "3/12",
622	            "—"
623	          ],
624	          [
625	            "Cross-tier (all)",
626	            "0.38",
627	            "11/12",
628	            "—"
629	          ],
630	          [
631	            "Restricted to mid-weak + strong",
632	            "0.15",
633	            "4/12",
634	            "—"
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "这是对Claim 1的最致命打击之一。η_max dominance不是关于\"individual vulnerability drives panel vulnerability\"的 general principle，而是\"当panel中存在capability差异极大的model时，最弱者的vulnerability自然predict了panel outcome\" 的trivial observation。类比：如果一个篮球队里有NBA球员和小学生，小学生的表现当然predict了队伍输赢——但这不是关于\"weakest link\" 的深刻insight，而是关于\"don't mix radically different capability levels\"的obvious conclusion。 论文需要explicit caveat：\"η_max dominance finding is contingent on cross-tier panel composition and does not generalize to capability-controlled settings\"。\n\n\nCapability-matched analysis彻底暴露η_max dominance对capability tier spread的依赖。 3/3/9分层下，frontier tier（3 models）和strong tier（3 models）各只有C(3,3)=1个panel—— 根本没有足够variance做回归。mid-weak tier有C(9,3)=84 panels，但within-tier η_max range被压缩75% （所有模型能力相近→η_max variation极小），η_max仅3/12 significant（全部在extreme conditions如PI下）。 K_eff within-tier全部NS（0/12），因为within-tier的diversity variation也被压缩。 对比cross-tier（all 455 panels）的11/12 η_max和8/12 K_eff，结论清晰： η_max dominance is driven by capability tier spread, not a general principle。 这不意味η_max irrelevant——它means η_max在cross-tier比较中conflates \"model capability\"和\"individual vulnerability\"， 而capability是confound不是target predictor。\n"
641	  },
642	  {
643	    "name": "Two-stage panel design algorithm benchmark",
644	    "description": "实现robustness-first两阶段算法（先筛η ≤ threshold，再最大化K_eff），对比5个baseline策略。 在15模型、455 panels上sweep threshold。\n",
645	    "results": {
646	      "strategies_compared": 6,
647	      "min_eta_max_win_rate_12cond": "9/12",
648	      "strongest_k_win_rate_12cond": "8/12",
649	      "two_stage_win_rate_12cond": "9/12",
650	      "max_keff_win_rate_12cond": "2/12",
651	      "random_win_rate_12cond": "0/12",
652	      "min_eta_max_vs_two_stage_p": 0.78,
653	      "min_eta_max_vs_strongest_k_p": 0.42,
654	      "two_stage_marginal_improvement_over_min_eta": 0.003,
655	      "two_stage_marginal_improvement_over_strongest_k": 0.008,
656	      "threshold_sensitivity": "high — optimal threshold attack-dependent",
657	      "asr_range_min_eta": "[0.04, 0.52]"
658	    },
659	    "tables": [
660	      {
661	        "caption": "Panel selection strategy comparison (12 conditions, K=3)",
662	        "columns": [
663	          "Strategy",
664	          "Win count /12",
665	          "Mean ASR",
666	          "vs Random Δ ASR"
667	        ],
668	        "rows": [
669	          [
670	            "Min η_max",
671	            "9/12",
672	            "0.087",
673	            "-0.085"
674	          ],
675	          [
676	            "Two-stage (ours)",
677	            "9/12",
678	            "0.084",
679	            "-0.088"
680	          ],
681	          [
682	            "Strongest-K",
683	            "8/12",
684	            "0.089",
685	            "-0.083"
686	          ],
687	          [
688	            "Max K_eff",
689	            "2/12",
690	            "0.142",
691	            "-0.030"
692	          ],
693	          [
694	            "Max family diversity",
695	            "1/12",
696	            "0.155",
697	            "-0.017"
698	          ],
699	          [
700	            "Random",
701	            "0/12",
702	            "0.172",
703	            "—"
704	          ]
705	        ]
706	      },
707	      {
708	        "caption": "Two-stage vs min(η_max): head-to-head",
709	        "columns": [
710	          "Condition",
711	          "Two-stage ASR",
712	          "Min η_max ASR",
713	          "Δ ASR",
714	          "Winner"
715	        ],
716	        "rows": [
717	          [
718	            "mmlu×PI",
719	            "0.041",
720	            "0.044",
721	            "-0.003",
722	            "Two-stage"
723	          ],
724	          [
725	            "mmlu×SM",
726	            "0.058",
727	            "0.059",
728	            "-0.001",
729	            "Two-stage"
730	          ],
731	          [
732	            "mmlu×syc",
733	            "0.095",
734	            "0.093",
735	            "+0.002",
736	            "Min η_max"
737	          ],
738	          [
739	            "mmlu×verb",
740	            "0.102",
741	            "0.098",
742	            "+0.004",
743	            "Min η_max"
744	          ],
745	          [
746	            "mmlu×pos",
747	            "0.078",
748	            "0.082",
749	            "-0.004",
750	            "Two-stage"
751	          ],
752	          [
753	            "mmlu×auth",
754	            "0.088",
755	            "0.091",
756	            "-0.003",
757	            "Two-stage"
758	          ],
759	          [
760	            "arc×PI",
761	            "0.052",
762	            "0.055",
763	            "-0.003",
764	            "Two-stage"
765	          ],
766	          [
767	            "arc×SM",
768	            "0.068",
769	            "0.071",
770	            "-0.003",
771	            "Two-stage"
772	          ],
773	          [
774	            "arc×syc",
775	            "0.112",
776	            "0.108",
777	            "+0.004",
778	            "Min η_max"
779	          ],
780	          [
781	            "arc×verb",
782	            "0.118",
783	            "0.115",
784	            "+0.003",
785	            "Min η_max"
786	          ],
787	          [
788	            "arc×pos",
789	            "0.092",
790	            "0.095",
791	            "-0.003",
792	            "Two-stage"
793	          ],
794	          [
795	            "arc×auth",
796	            "0.098",
797	            "0.101",
798	            "-0.003",
799	            "Two-stage"
800	          ]
801	        ]
802	      }
803	    ],
804	    "figures": [],
805	    "analysis": "min(η_max) wins 9/12仍然是一个decent practical finding，但two-stage algorithm没有additional value。 整个practical contribution可以用一句话总结：\"use the strongest available models\"—— 这太trivial to be a contribution。论文可以保留min(η_max) dominance作为supporting evidence for η_max importance的indirect argument，但不能作为novel algorithm contribution。 Key observation：min(η_max) ≈ strongest-K在实践中——因为individual robustness (η)与model capability 高度相关（r=0.72），选最robust的models ≈ 选最强的models。\n\n\nmin(η_max) strategy仍然wins 9/12 conditions（在worst档范围[8,10]内），但two-stage algorithm与min(η_max) 之间的差异vanishingly small（mean Δ ASR = 0.003pp）。这是因为在robustness-first筛选后，surviving models 的K_eff variation极小（都是strong models → natural diversity limited by capability homogeneity）， 第二阶段\"maximize K_eff\"几乎不改变panel composition。 实质上two-stage ≈ min(η_max) ≈ strongest-K，三者在win conditions上高度重叠。 Practical contribution从\"novel algorithm\"降级为\"use strong models\"——一个trivial recommendation。 threshold参数高度attack-dependent（prompt_injection最优threshold ≠ sycophancy最优threshold）， 无法给出universal prescriptive guidance。\n"
806	  },
807	  {
808	    "name": "Per-judge ASR concentration analysis",
809	    "description": "对每个panel × attack，测量per-judge ASR分布的集中度（Gini系数、熵）。 直接验证adaptive adversary是否集中targeting weakest judge。\n",
810	    "results": {
811	      "median_gini": 0.28,
812	      "mean_gini": 0.31,
813	      "gini_targeted_attacks": 0.35,
814	      "gini_shared_bias_attacks": 0.22,
815	      "gini_vs_random_fault_baseline": 0.19,
816	      "adaptive_vs_rf_gini_p": 0.04,
817	      "adaptive_vs_rf_gini_d": 0.22,
818	      "weakest_judge_share_median": 0.42,
819	      "weakest_judge_share_targeted": 0.48,
820	      "weakest_judge_share_shared_bias": 0.38,
821	      "entropy_normalized_median": 0.81,
822	      "gini_eta_max_correlation": 0.55
823	    },
824	    "tables": [
825	      {
826	        "caption": "ASR concentration metrics across conditions",
827	        "columns": [
828	          "Attack category",
829	          "Median Gini",
830	          "Weakest-judge share",
831	          "vs RF baseline p"
832	        ],
833	        "rows": [
834	          [
835	            "Targeted (PI, SM, PB)",
836	            "0.35",
837	            "0.48",
838	            "0.02"
839	          ],
840	          [
841	            "Shared-bias (syc, verb, auth)",
842	            "0.22",
843	            "0.38",
844	            "0.28"
845	          ],
846	          [
847	            "All adaptive",
848	            "0.28",
849	            "0.42",
850	            "0.04"
851	          ],
852	          [
853	            "Random-fault baseline",
854	            "0.19",
855	            "0.36",
856	            "—"
857	          ]
858	        ]
859	      },
860	      {
861	        "caption": "Gini coefficient predictors",
862	        "columns": [
863	          "Predictor",
864	          "r with Gini",
865	          "p",
866	          "Interpretation"
867	        ],
868	        "rows": [
869	          [
870	            "η_max (panel)",
871	            "0.55",
872	            "<0.001",
873	            "Capability gap drives concentration"
874	          ],
875	          [
876	            "K_eff (panel)",
877	            "-0.18",
878	            "0.12",
879	            "Diversity weakly reduces concentration"
880	          ],
881	          [
882	            "Attack targetedness",
883	            "0.31",
884	            "0.003",
885	            "Targeted attacks more concentrated"
886	          ]
887	        ]
888	      }
889	    ],
890	    "figures": [],
891	    "analysis": "Concentration analysis是modest supporting evidence而非smoking gun。d=0.22太小， 且Gini主要由capability gap而非adversary strategy驱动（r=0.55 with η_max）。 可以在paper中作为supplementary evidence保留但不能carry independent weight。 对worst-tier narrative的影响：不直接contradicts任何claim，但也不rescues BFT framing（plan_003 failure）。\n\n\nConcentration analysis显示adaptive adversary确实比random fault更集中targeting（Gini 0.28 vs 0.19, p=0.04）， 但effect size small（Cohen's d=0.22）。更重要的是，Gini与η_max高度相关（r=0.55）—— concentration主要driven by capability gap（弱model承担更多attack success）， 而非adversary的strategic targeting能力。 在shared-bias attacks下，Gini接近random baseline（0.22 vs 0.19），说明这些attacks确实不是targeted的 ——与GAM taxonomy的directional tendency一致，但同样不够clean to be standalone evidence。 总体上concentration analysis提供了weak-to-moderate支撑adaptive adversary narrative， 但不足以independently establish \"adversary targets weakest link\" claim。\n"
892	  },
893	  {
894	    "name": "Diversity-capability tradeoff visualization",
895	    "description": "在455 panels上绘制K_eff vs η_max scatter，拟合tradeoff curve，展示Pareto frontier，按tier分层。\n",
896	    "results": {
897	      "overall_pearson_r": 0.65,
898	      "overall_spearman_r": 0.61,
899	      "within_frontier_r": 0.22,
900	      "within_strong_r": 0.18,
901	      "within_midweak_r": 0.35,
902	      "cross_tier_r": 0.72,
903	      "pareto_front_size": 8,
904	      "pareto_dominated_by_min_eta": "6/8",
905	      "tradeoff_R2_overall": 0.42,
906	      "tradeoff_slope": 0.58
907	    },
908	    "tables": [
909	      {
910	        "caption": "Diversity-capability correlation by analysis scope",
911	        "columns": [
912	          "Scope",
913	          "Pearson r",
914	          "R²",
915	          "N panels",
916	          "Interpretation"
917	        ],
918	        "rows": [
919	          [
920	            "Overall (15 models)",
921	            "0.65",
922	            "0.42",
923	            "455",
924	            "Moderate-strong confound"
925	          ],
926	          [
927	            "Within frontier (3 models)",
928	            "0.22",
929	            "0.05",
930	            "1",
931	            "Weak (too few panels)"
932	          ],
933	          [
934	            "Within strong (3 models)",
935	            "0.18",
936	            "0.03",
937	            "1",
938	            "Weak (too few panels)"
939	          ],
940	          [
941	            "Within mid-weak (9 models)",
942	            "0.35",
943	            "0.12",
944	            "84",
945	            "Moderate within-tier"
946	          ],
947	          [
948	            "Cross-tier only",
949	            "0.72",
950	            "0.52",
951	            "370",
952	            "Strong — tier-driven"
953	          ]
954	        ]
955	      }
956	    ],
957	    "figures": [],
958	    "analysis": "Visualization清晰展示confound的severity。r=0.65意味着K_eff和η_max共享42%的variance—— regression无法reliably separate their independent effects，这与VIF >7（plan_009）一致。 Tradeoff本身是real as structural correlation，但\"diversity is costly because it requires weaker models\" 这个interpretation only applies to cross-tier composition。 对论文的影响：Claim 3（diversity-capability tradeoff）不能作为\"fundamental constraint\"呈现， 而是\"artifact of current model ecosystem where capability predicts robustness\"。\n\n\ndiversity_capability_r在worst档范围[0.55, 0.75]内，取值0.65。Tradeoff确实存在（R²=0.42）， 但primarily driven by cross-tier differences。Within-tier r远低于overall（0.18-0.35 vs 0.65）， 表明tradeoff是ecosystem structure artifact而非fundamental constraint。 Pareto frontier上8个panels中6个被min(η_max) dominate——Pareto analysis不能rescue practical contribution。 但0.65的correlation确实说明η_max和K_eff在current design下heavily confounded—— 这reinforces VIF问题（plan_009），regression decomposition的reliability存疑。\n"
959	  },
960	  {
961	    "name": "Panel size sensitivity: K=3,5,7,9",
962	    "description": "在不同panel size (K=3,5,7,9)下测试η_max dominance是否持续。 验证weakest-link是否universal across panel sizes。\n",
963	    "results": {
964	      "k3_bootstrap_eta_sig": "3/12",
965	      "k3_bootstrap_keff_sig": "1/12",
966	      "k5_bootstrap_eta_sig": "2/12",
967	      "k5_bootstrap_keff_sig": "0/12",
968	      "k7_bootstrap_eta_sig": "1/12",
969	      "k7_bootstrap_keff_sig": "0/12",
970	      "k9_bootstrap_eta_sig": "1/12",
971	      "k9_bootstrap_keff_sig": "1/12",
972	      "k5_panels": 3003,
973	      "k7_panels": 6435,
974	      "k9_panels": 5005,
975	      "eta_sig_trend_bootstrap_p": 0.04,
976	      "non_independence_amplification_k5": "4.1×",
977	      "non_independence_amplification_k7": "5.8×",
978	      "non_independence_amplification_k9": "7.2×"
979	    },
980	    "tables": [
981	      {
982	        "caption": "Panel size × correction method: η_max significance",
983	        "columns": [
984	          "K",
985	          "N panels",
986	          "OLS η_max sig",
987	          "Bootstrap η_max sig",
988	          "SE inflation",
989	          "Model overlap per judge"
990	        ],
991	        "rows": [
992	          [
993	            "3",
994	            "455",
995	            "11/12",
996	            "3/12",
997	            "3.2×",
998	            "91"
999	          ],
1000	          [
1001	            "5",
1002	            "3003",
1003	            "11/12",
1004	            "2/12",
1005	            "4.1×",
1006	            "1001"
1007	          ],
1008	          [
1009	            "7",
1010	            "6435",
1011	            "10/12",
1012	            "1/12",
1013	            "5.8×",
1014	            "3003"
1015	          ],
1016	          [
1017	            "9",
1018	            "5005",
1019	            "9/12",
1020	            "1/12",
1021	            "7.2×",
1022	            "2002"
1023	          ]
1024	        ]
1025	      },
1026	      {
1027	        "caption": "Panel size × correction: K_eff significance",
1028	        "columns": [
1029	          "K",
1030	          "OLS K_eff sig",
1031	          "Bootstrap K_eff sig",
1032	          "K_eff practical Δ ASR (IQR)"
1033	        ],
1034	        "rows": [
1035	          [
1036	            "3",
1037	            "8/12",
1038	            "1/12",
1039	            "0.8pp"
1040	          ],
1041	          [
1042	            "5",
1043	            "7/12",
1044	            "0/12",
1045	            "0.5pp"
1046	          ],
1047	          [
1048	            "7",
1049	            "6/12",
1050	            "0/12",
1051	            "0.3pp"
1052	          ],
1053	          [
1054	            "9",
1055	            "5/12",
1056	            "1/12",
1057	            "0.2pp"
1058	          ]
1059	        ]
1060	      }
1061	    ],
1062	    "figures": [],
1063	    "analysis": "Panel size analysis在worst档下paradoxically成为方法学贡献的strongest evidence。 它直观展示了combinatorial panel designs的fundamental problem：C(N,K) grows fast but each model's participation grows equally fast → non-independence scales with panel count。 这是LLM evaluation community应该awareness的general insight，不限于adversarial setting。 但对composition-level claims (η_max, K_eff) 完全destructive——neither predictor survives correction at any K。\n\n\nPanel size增大在worst档下不仅不改善η_max significance——反而使其更差。原因是non-independence问题 随K增大而amplify：K=5时每个model出现在C(14,4)=1001个panels中（vs K=3时91个）， SE inflation从3.2×（K=3）上升到7.2×（K=9）。更大的panels有更多overlap，corrected inference 更conservative。Bootstrap η_max从K=3的3/12降至K=9的1/12。 Irony：更大panels理论上应该reduce weakest-link effect（1 weak vote in 9 matters less）， 但这个theoretical prediction无法在corrected inference下empirically confirm， 因为non-independence scales faster than signal。 K_eff同样全面collapse（最多1/12 at K=9），两个predictor都不work under corrected inference at large K。\n"
1064	  },
1065	  {
1066	    "name": "VIF + multicollinearity analysis",
1067	    "description": "计算VIF、partial correlations、residualized K_eff。尝试beta regression。 量化η_max与K_eff的multicollinearity severity。\n",
1068	    "results": {
1069	      "vif_eta_max": 7.8,
1070	      "vif_keff": 6.9,
1071	      "partial_r_eta_max_given_keff": 0.31,
1072	      "partial_r_keff_given_eta_max": 0.12,
1073	      "residualized_keff_sig": "2/12",
1074	      "residualized_keff_p_median": 0.28,
1075	      "beta_regression_eta_sig": "9/12",
1076	      "beta_regression_keff_sig": "3/12",
1077	      "condition_number": 18.5,
1078	      "variance_decomposition_shared": 0.42,
1079	      "variance_decomposition_eta_unique": 0.18,
1080	      "variance_decomposition_keff_unique": 0.03
1081	    },
1082	    "tables": [
1083	      {
1084	        "caption": "Multicollinearity diagnostics",
1085	        "columns": [
1086	          "Diagnostic",
1087	          "η_max",
1088	          "K_eff",
1089	          "Threshold",
1090	          "Verdict"
1091	        ],
1092	        "rows": [
1093	          [
1094	            "VIF (base model)",
1095	            "2.4",
1096	            "2.1",
1097	            ">5 = concern",
1098	            "OK"
1099	          ],
1100	          [
1101	            "VIF (with tier indicators)",
1102	            "7.8",
1103	            "6.9",
1104	            ">5 = concern",
1105	            "FAIL"
1106	          ],
1107	          [
1108	            "Partial r (given other)",
1109	            "0.31",
1110	            "0.12",
1111	            "—",
1112	            "K_eff weak"
1113	          ],
1114	          [
1115	            "Unique variance %",
1116	            "18%",
1117	            "3%",
1118	            "—",
1119	            "K_eff negligible"
1120	          ],
1121	          [
1122	            "Condition number",
1123	            "18.5",
1124	            "—",
1125	            ">30 = severe",
1126	            "Moderate"
1127	          ]
1128	        ]
1129	      },
1130	      {
1131	        "caption": "Variance decomposition: shared vs unique",
1132	        "columns": [
1133	          "Component",
1134	          "R² contribution",
1135	          "% of total explained"
1136	        ],
1137	        "rows": [
1138	          [
1139	            "Shared (η_max ∩ K_eff)",
1140	            "0.42",
1141	            "67%"
1142	          ],
1143	          [
1144	            "Unique η_max",
1145	            "0.18",
1146	            "29%"
1147	          ],
1148	          [
1149	            "Unique K_eff",
1150	            "0.03",
1151	            "5%"
1152	          ],
1153	          [
1154	            "Total model R²",
1155	            "0.63",
1156	            "100%"
1157	          ]
1158	        ]
1159	      },
1160	      {
1161	        "caption": "Residualized K_eff regression results",
1162	        "columns": [
1163	          "Dataset",
1164	          "Attack",
1165	          "Residualized K_eff β",
1166	          "p",
1167	          "Significant?"
1168	        ],
1169	        "rows": [
1170	          [
1171	            "MMLU",
1172	            "prompt_injection",
1173	            "0.08",
1174	            "0.42",
1175	            "No"
1176	          ],
1177	          [
1178	            "MMLU",
1179	            "score_manipulation",
1180	            "0.05",
1181	            "0.58",
1182	            "No"
1183	          ],
1184	          [
1185	            "MMLU",
1186	            "sycophancy",
1187	            "-0.12",
1188	            "0.18",
1189	            "No"
1190	          ],
1191	          [
1192	            "MMLU",
1193	            "verbosity_bias",
1194	            "-0.04",
1195	            "0.65",
1196	            "No"
1197	          ],
1198	          [
1199	            "MMLU",
1200	            "position_bias",
1201	            "0.15",
1202	            "0.04",
1203	            "Yes"
1204	          ],
1205	          [
1206	            "MMLU",
1207	            "authority_bias",
1208	            "-0.06",
1209	            "0.52",
1210	            "No"
1211	          ],
1212	          [
1213	            "ARC",
1214	            "prompt_injection",
1215	            "0.11",
1216	            "0.22",
1217	            "No"
1218	          ],
1219	          [
1220	            "ARC",
1221	            "score_manipulation",
1222	            "0.07",
1223	            "0.41",
1224	            "No"
1225	          ],
1226	          [
1227	            "ARC",
1228	            "sycophancy",
1229	            "-0.09",
1230	            "0.35",
1231	            "No"
1232	          ],
1233	          [
1234	            "ARC",
1235	            "verbosity_bias",
1236	            "-0.03",
1237	            "0.72",
1238	            "No"
1239	          ],
1240	          [
1241	            "ARC",
1242	            "position_bias",
1243	            "0.13",
1244	            "0.08",
1245	            "No"
1246	          ],
1247	          [
1248	            "ARC",
1249	            "authority_bias",
1250	            "-0.02",
1251	            "0.81",
1252	            "No"
1253	          ]
1254	        ]
1255	      }
1256	    ],
1257	    "figures": [],
1258	    "analysis": "VIF分析是worst档中最clean的negative result——它提供了一个principled statistical explanation for为什么K_eff在corrected inference下always collapse。不是因为K_eff \"doesn't matter\"， 而是因为在当前design下η_max和K_eff share 67% of their explained variance， K_eff的unique contribution仅3%——在15 clusters的bootstrap下impossible to detect。 这reinforces方法学贡献narrative：combinatorial panel designs + small number of unique models = multicollinearity + non-independence = any predictor-level decomposition is unreliable。 论文应该present VIF analysis as evidence that the regression approach itself is inadequate for this research question，而非\"K_eff doesn't matter\"。\n\n\nVIF分析确认severe multicollinearity：VIF(η_max)=7.8, VIF(K_eff)=6.9（均>5的conventional threshold， 接近>10的severe threshold）。根源是diversity-capability confound（r=0.65→VIF ≈ 1/(1-r²) = 1/0.58 ≈ 1.7×... 等等，VIF的计算是1/(1-R²_j)，如果K_eff对η_max的R²=0.42（来自r=0.65）， 则VIF(K_eff) = 1/(1-0.42) = 1.72。但如果加入其他confounds（tier indicators等），VIF会更高。 在有tier indicators + K_eff + η_max的full model中，VIF可以达到7-8。\nPartial correlation显示：controlling for K_eff后η_max与ASR的r=0.31（moderate）， 但controlling for η_max后K_eff与ASR的r仅0.12（weak）。 Variance decomposition：42% shared between η_max和K_eff，18% unique to η_max，仅3% unique to K_eff。 K_eff的\"independent effect\"实质上是noise level。 Beta regression（处理bounded [0,1] response）不改善K_eff situation：仍仅3/12显著。 结论：在当前design下η_max和K_eff cannot be reliably separated as independent predictors。 整个regression-based decomposition framework在VIF >5下unreliable。\n"
1259	  },
1260	  {
1261	    "name": "Non-majority-vote aggregation: weighted, threshold, Bayesian",
1262	    "description": "测试η_max dominance在weighted voting、threshold (unanimity)、Bayesian calibration下是否persist。 验证aggregation gradient。\n",
1263	    "results": {
1264	      "majority_ols_eta_sig": "11/12",
1265	      "majority_ols_keff_sig": "8/12",
1266	      "majority_bootstrap_eta_sig": "3/12",
1267	      "majority_bootstrap_keff_sig": "1/12",
1268	      "weighted_ols_eta_sig": "9/12",
1269	      "weighted_ols_keff_sig": "9/12",
1270	      "weighted_bootstrap_eta_sig": "2/12",
1271	      "weighted_bootstrap_keff_sig": "1/12",
1272	      "threshold_ols_eta_sig": "12/12",
1273	      "threshold_ols_keff_sig": "11/12",
1274	      "threshold_bootstrap_eta_sig": "5/12",
1275	      "threshold_bootstrap_keff_sig": "2/12",
1276	      "threshold_R2": 0.89,
1277	      "bayesian_ols_eta_sig": "9/12",
1278	      "bayesian_ols_keff_sig": "7/12",
1279	      "bayesian_ols_keff_negative": 6,
1280	      "bayesian_bootstrap_eta_sig": "2/12",
1281	      "bayesian_bootstrap_keff_sig": "0/12",
1282	      "bayesian_bootstrap_keff_negative": 0,
1283	      "bayesian_R2": 0.1,
1284	      "aggregation_gradient_survives_correction": "partially"
1285	    },
1286	    "tables": [
1287	      {
1288	        "caption": "Aggregation gradient: OLS vs bootstrap correction",
1289	        "columns": [
1290	          "Aggregation",
1291	          "OLS η_max",
1292	          "OLS K_eff",
1293	          "Bootstrap η_max",
1294	          "Bootstrap K_eff",
1295	          "R²"
1296	        ],
1297	        "rows": [
1298	          [
1299	            "Majority",
1300	            "11/12",
1301	            "8/12 (7+/1−)",
1302	            "3/12",
1303	            "1/12",
1304	            "0.30"
1305	          ],
1306	          [
1307	            "Weighted",
1308	            "9/12",
1309	            "9/12 (9+/0−)",
1310	            "2/12",
1311	            "1/12",
1312	            "0.28"
1313	          ],
1314	          [
1315	            "Threshold",
1316	            "12/12",
1317	            "11/12 (10+/1−)",
1318	            "5/12",
1319	            "2/12",
1320	            "0.89"
1321	          ],
1322	          [
1323	            "Bayesian",
1324	            "9/12",
1325	            "7/12 (1+/6−)",
1326	            "2/12",
1327	            "0/12 (0+/0−)",
1328	            "0.10"
1329	          ]
1330	        ]
1331	      },
1332	      {
1333	        "caption": "Bayesian K_eff direction under correction",
1334	        "columns": [
1335	          "Method",
1336	          "K_eff negative (of significant)",
1337	          "K_eff significant total",
1338	          "Direction interpretation"
1339	        ],
1340	        "rows": [
1341	          [
1342	            "OLS",
1343	            "6/7",
1344	            "7/12",
1345	            "Strongly negative (protective)"
1346	          ],
1347	          [
1348	            "Clustered SE",
1349	            "1/2",
1350	            "2/12",
1351	            "Weak negative"
1352	          ],
1353	          [
1354	            "Mixed effects",
1355	            "0/1",
1356	            "1/12",
1357	            "Inconclusive"
1358	          ],
1359	          [
1360	            "Bootstrap v2",
1361	            "0/0",
1362	            "0/12",
1363	            "No signal survives"
1364	          ]
1365	        ]
1366	      }
1367	    ],
1368	    "figures": [],
1369	    "analysis": "Aggregation gradient是worst档中唯一partially salvageable的composition-related finding。 R²的gradient（0.89→0.10）是descriptive statistic不受SE correction影响—— aggregation rule确实determines how much panel composition matters for vulnerability。 但individual predictor significance在除threshold外的所有aggregation下collapse after correction， Bayesian K_eff flip（被寄予厚望的\"defense lever\"）完全是OLS artifact。 Salvage angle：\"aggregation choice determines the predictability of panel vulnerability， but we cannot reliably decompose this into η_max vs K_eff components\"—— 这是一个weaker but defensible statement，可以作为论文的Claim C。\n\n\nAggregation gradient在OLS下clear（threshold R²=0.89 → bayesian R²=0.10）， 但bootstrap correction后Bayesian K_eff flip彻底消失：OLS下6/7 negative → bootstrap下0/12 significant。 原因：Bayesian aggregation减弱了panel composition对ASR的影响（R²=0.10），但这也意味着signal/noise ratio极低—— 在bootstrap correction下signal completely drowned by noise。 Threshold aggregation相对较好（bootstrap η_max 5/12），因为unanimity rule下 panel vulnerability完全由individual vulnerabilities的AND/OR逻辑决定（R²=0.89）， signal极强→即使bootstrap conservative也能detect。 但这创造了一个awkward结论：\"只有在使用最不实用的aggregation rule（unanimity）时， η_max dominance才survives bootstrap correction\"——因为实践中没人用unanimity voting。 aggregation gradient作为R²的gradient仍然成立（0.89→0.10不受SE correction影响）， 但individual predictor significance在每种aggregation下都unreliable after correction。\n"
1370	  },
1371	  {
1372	    "name": "Open-ended generation benchmark (MT-Bench / AlpacaEval)",
1373	    "description": "在MT-Bench或AlpacaEval-style open-ended generation任务上运行全部15 models + 6 attacks。 验证findings是否generalize beyond MCQ format。\n",
1374	    "results": {
1375	      "benchmark": "MT-Bench",
1376	      "total_conditions": 12,
1377	      "ols_eta_sig": "7/12",
1378	      "ols_keff_sig": "5/12",
1379	      "bootstrap_eta_sig": "1/12",
1380	      "bootstrap_keff_sig": "0/12",
1381	      "clustered_se_eta_sig": "3/12",
1382	      "clustered_se_keff_sig": "0/12",
1383	      "R2_median": 0.15,
1384	      "scoring_format": "pairwise comparison",
1385	      "attack_implementation_challenges": 3,
1386	      "cross_benchmark_eta_correlation": 0.52,
1387	      "cross_benchmark_keff_correlation": 0.38
1388	    },
1389	    "tables": [
1390	      {
1391	        "caption": "MT-Bench results: OLS vs bootstrap",
1392	        "columns": [
1393	          "Attack",
1394	          "OLS η_max p",
1395	          "Bootstrap η_max p",
1396	          "OLS K_eff p",
1397	          "Bootstrap K_eff p",
1398	          "R²"
1399	        ],
1400	        "rows": [
1401	          [
1402	            "prompt_injection",
1403	            "0.008",
1404	            "0.22",
1405	            "0.05",
1406	            "0.48",
1407	            "0.18"
1408	          ],
1409	          [
1410	            "score_manipulation",
1411	            "0.015",
1412	            "0.31",
1413	            "0.08",
1414	            "0.55",
1415	            "0.14"
1416	          ],
1417	          [
1418	            "sycophancy*",
1419	            "0.042",
1420	            "0.51",
1421	            "0.12",
1422	            "0.63",
1423	            "0.11"
1424	          ],
1425	          [
1426	            "verbosity_bias*",
1427	            "0.038",
1428	            "0.48",
1429	            "0.18",
1430	            "0.58",
1431	            "0.09"
1432	          ],
1433	          [
1434	            "position_bias",
1435	            "0.003",
1436	            "0.08",
1437	            "0.04",
1438	            "0.38",
1439	            "0.22"
1440	          ],
1441	          [
1442	            "authority_bias*",
1443	            "0.055",
1444	            "0.55",
1445	            "0.22",
1446	            "0.68",
1447	            "0.08"
1448	          ]
1449	        ]
1450	      },
1451	      {
1452	        "caption": "Cross-benchmark consistency",
1453	        "columns": [
1454	          "Metric",
1455	          "MMLU-MT r",
1456	          "ARC-MT r",
1457	          "Interpretation"
1458	        ],
1459	        "rows": [
1460	          [
1461	            "η_max profile",
1462	            "0.52",
1463	            "0.48",
1464	            "Moderate — partial transfer"
1465	          ],
1466	          [
1467	            "K_eff effect direction",
1468	            "0.38",
1469	            "0.35",
1470	            "Weak — inconsistent"
1471	          ],
1472	          [
1473	            "Condition-level R²",
1474	            "0.25",
1475	            "0.22",
1476	            "Weak"
1477	          ]
1478	        ]
1479	      }
1480	    ],
1481	    "figures": [],
1482	    "analysis": "Open-ended benchmark是worst档的additional nail in the coffin。不仅不rescue findings， 还暴露了MCQ-specific limitation：MCQ的discrete 4-choice format可能artificially inflate η_max signal（错误是categorical → vulnerability更binary → η_max更predictive）， 而open-ended scoring的continuous nature dilutes this。 对论文的影响：如果MT-Bench results included，需要honest caveat \"our findings are primarily established for MCQ evaluation and show limited transfer to open-ended settings\"。 如果excluded，reviewer会问why not。Either way is problematic。\n\n\nOpen-ended generation benchmark引入新的complications。 MT-Bench使用pairwise comparison scoring（而非MCQ的discrete label），judge vulnerability profile 与MCQ setting有中等相关（r=0.52 for η_max across benchmarks）。 OLS下η_max显著7/12，但bootstrap后仅1/12——same non-independence problem。 更关键的是R²显著低于MCQ（0.15 vs 0.25），说明open-ended setting中panel composition 对vulnerability的解释力更低——可能因为open-ended scoring有更多intrinsic noise。 3种attacks（sycophancy, verbosity_bias, authority_bias）在open-ended setting的implementation 需要substantial modification，results可能不完全comparable。 总结：open-ended benchmark不rescue任何claim，反而进一步dilute statistical power。 论文有效沦为two-MCQ-benchmark + one-weak-open-ended study。\n"
1483	  },
1484	  {
1485	    "name": "Partial-knowledge adversary model",
1486	    "description": "模拟partial-knowledge adversary：adversary知道model families但不知exact vulnerability profiles。 对比full-knowledge vs partial-knowledge vs zero-knowledge adversary下的panel vulnerability。\n",
1487	    "results": {
1488	      "knowledge_levels": 3,
1489	      "full_knowledge_mean_asr": 0.142,
1490	      "partial_knowledge_mean_asr": 0.128,
1491	      "zero_knowledge_mean_asr": 0.098,
1492	      "partial_vs_full_ratio": 0.9,
1493	      "partial_vs_zero_ratio": 1.31,
1494	      "eta_max_sig_full": "3/12",
1495	      "eta_max_sig_partial": "2/12",
1496	      "eta_max_sig_zero": "1/12",
1497	      "keff_sig_any_level": "0/12",
1498	      "family_knowledge_value": "moderate",
1499	      "knowledge_gradient_p": 0.04
1500	    },
1501	    "tables": [
1502	      {
1503	        "caption": "Adversary knowledge level × panel vulnerability",
1504	        "columns": [
1505	          "Knowledge level",
1506	          "Mean ASR",
1507	          "η_max bootstrap sig",
1508	          "K_eff bootstrap sig",
1509	          "R²"
1510	        ],
1511	        "rows": [
1512	          [
1513	            "Full (oracle)",
1514	            "0.142",
1515	            "3/12",
1516	            "0/12",
1517	            "0.25"
1518	          ],
1519	          [
1520	            "Partial (family only)",
1521	            "0.128",
1522	            "2/12",
1523	            "0/12",
1524	            "0.18"
1525	          ],
1526	          [
1527	            "Zero (random targeting)",
1528	            "0.098",
1529	            "1/12",
1530	            "0/12",
1531	            "0.08"
1532	          ]
1533	        ]
1534	      },
1535	      {
1536	        "caption": "Knowledge value decomposition",
1537	        "columns": [
1538	          "Comparison",
1539	          "Δ ASR",
1540	          "p",
1541	          "Practical interpretation"
1542	        ],
1543	        "rows": [
1544	          [
1545	            "Full vs zero",
1546	            "+0.044",
1547	            "0.002",
1548	            "Knowledge matters (44pp higher)"
1549	          ],
1550	          [
1551	            "Full vs partial",
1552	            "+0.014",
1553	            "0.18",
1554	            "Exact profile adds little over family"
1555	          ],
1556	          [
1557	            "Partial vs zero",
1558	            "+0.030",
1559	            "0.01",
1560	            "Family knowledge has moderate value"
1561	          ]
1562	        ]
1563	      }
1564	    ],
1565	    "figures": [],
1566	    "analysis": "Partial-knowledge analysis是lowest-impact experiment in worst档。 它confirm两个already-known facts（family labels unreliable, adversary knowledge matters） without adding new insight。在page-limited paper (8 pages)中可以完全省略或放入appendix。 唯一minor value：knowledge gradient validates that our \"adaptive adversary\" threat model is not unrealistic（even partial knowledge gives advantage），但这is a setup assumption validation, not a contribution。\n\nPartial-knowledge adversary结果在worst档下mostly inconclusive。 Full→partial→zero knowledge确实形成ASR gradient（0.142→0.128→0.098, p=0.04）， 说明adversary knowledge matters。但family knowledge（partial level）只提供10% advantage over full knowledge （partial/full = 0.90）——因为family labels不predict vulnerability well（Claim 4已确认, p=0.179）。 η_max significance在任何knowledge level下都barely survives bootstrap（最好3/12 for full-knowledge）， K_eff在所有levels都0/12。Partial-knowledge分析adds little to the paper—— 它confirm了family labels unreliability（already known）but doesn't provide new insight。 在worst档下这个experiment消耗GPU budget但return minimal novelty。\n"
1567	  }
1568	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51b538ef-1ac3-4f69-bdd5-2dba5d5c4520",
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "a781c0ab-5940-4489-82c0-2ce634377162",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Scale expansion: 15 models with API + large open-source\",\n    \"description\": \"将模型池从6扩展到15（加入GPT-4o-mini, GPT-4o, GPT-4.1, GPT-4.1-mini, Llama-3.1-70B, Qwen2.5-72B等）， 重跑MI矩阵 + C(15,3)=455 panels回归 + bootstrap/clustered SE/mixed effects全套correction。\\n\",\n    \"results\": {\n      \"total_models\": 15,\n      \"total_panels\": 455,\n      \"total_conditions\": 12,\n      \"confound_mean_abs_r\": 0.72,\n      \"canonical_ols_eta_max_sig\": \"11/12\",\n      \"canonical_ols_keff_sig\": \"8/12\",\n      \"canonical_ols_keff_positive\": 7,\n      \"canonical_ols_keff_negative\": 1,\n      \"wild_cluster_bootstrap_v2_eta_max_sig\": \"3/12\",\n      \"wild_cluster_bootstrap_v2_keff_sig\": \"1/12\",\n      \"clustered_se_eta_max_sig\": \"5/12\",\n      \"clustered_se_keff_sig\": \"0/12\",\n      \"mixed_effects_eta_max_sig\": \"4/12\",\n      \"mixed_effects_keff_sig\": \"1/12\",\n      \"eta_keff_dominance_ratio_bootstrap\": 3.0,\n      \"se_inflation_factor\": 3.2,\n      \"bootstrap_position_0_eta_sig\": \"2/12\",\n      \"bootstrap_position_1_eta_sig\": \"5/12\",\n      \"bootstrap_position_2_eta_sig\": \"4/12\",\n      \"mmlu_eta_bootstrap_sig\": \"2/6\",\n      \"arc_eta_bootstrap_sig\": \"1/6\",\n      \"keff_practical_delta_asr_iqr_pp\": 0.8,\n      \"median_R2\": 0.25\n    },\n    \"tables\": [\n      {\n        \"caption\": \"OLS vs correction methods: significance counts across 12 conditions\",\n        \"columns\": [\n          \"Method\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"K_eff positive\",\n          \"K_eff negative\",\n          \"Dominance ratio\"\n        ],\n        \"rows\": [\n          [\n            \"OLS (naive)\",\n            \"11/12\",\n            \"8/12\",\n            \"7\",\n            \"1\",\n            \"1.4:1\"\n          ],\n          [\n            \"Clustered SE (CR1, 15 clusters)\",\n            \"5/12\",\n            \"0/12\",\n            \"—\",\n            \"—\",\n            \"∞\"\n          ],\n          [\n            \"Mixed effects (random judge intercepts)\",\n            \"4/12\",\n            \"1/12\",\n            \"1\",\n            \"0\",\n            \"4:1\"\n          ],\n          [\n            \"Wild cluster bootstrap v2 (max-p)\",\n            \"3/12\",\n            \"1/12\",\n            \"1\",\n            \"0\",\n            \"3:1\"\n          ],\n          [\n            \"SE inflation factor\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"3.2×\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Bootstrap η_max significance by position and benchmark\",\n        \"columns\": [\n          \"Position\",\n          \"MMLU sig/6\",\n          \"ARC sig/6\",\n          \"Total sig/12\",\n          \"Cluster balance (max/min panels)\"\n        ],\n        \"rows\": [\n          [\n            \"Position 0\",\n            \"1/6\",\n            \"1/6\",\n            \"2/12\",\n            \"91:1\"\n          ],\n          [\n            \"Position 1\",\n            \"3/6\",\n            \"2/6\",\n            \"5/12\",\n            \"55:12\"\n          ],\n          [\n            \"Position 2\",\n            \"3/6\",\n            \"1/6\",\n            \"4/12\",\n            \"48:15\"\n          ],\n          [\n            \"Max-p (conservative)\",\n            \"2/6\",\n            \"1/6\",\n            \"3/12\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Per-condition bootstrap results (12 conditions)\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"OLS η_max p\",\n          \"Bootstrap η_max p\",\n          \"OLS K_eff p\",\n          \"Bootstrap K_eff p\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"prompt_injection\",\n            \"2e-06\",\n            \"0.028\",\n            \"0.004\",\n            \"0.18\"\n          ],\n          [\n            \"MMLU\",\n            \"score_manipulation\",\n            \"8e-05\",\n            \"0.041\",\n            \"0.011\",\n            \"0.31\"\n          ],\n          [\n            \"MMLU\",\n            \"sycophancy\",\n            \"0.002\",\n            \"0.14\",\n            \"0.08\",\n            \"0.42\"\n          ],\n          [\n            \"MMLU\",\n            \"verbosity_bias\",\n            \"0.009\",\n            \"0.22\",\n            \"0.15\",\n            \"0.55\"\n          ],\n          [\n            \"MMLU\",\n            \"position_bias\",\n            \"0.001\",\n            \"0.08\",\n            \"0.035\",\n            \"0.04\"\n          ],\n          [\n            \"MMLU\",\n            \"authority_bias\",\n            \"0.004\",\n            \"0.19\",\n            \"0.09\",\n            \"0.48\"\n          ],\n          [\n            \"ARC\",\n            \"prompt_injection\",\n            \"3e-14\",\n            \"0.35\",\n            \"0.001\",\n            \"0.62\"\n          ],\n          [\n            \"ARC\",\n            \"score_manipulation\",\n            \"1e-08\",\n            \"0.06\",\n            \"0.003\",\n            \"0.44\"\n          ],\n          [\n            \"ARC\",\n            \"sycophancy\",\n            \"0.013\",\n            \"0.52\",\n            \"0.24\",\n            \"0.71\"\n          ],\n          [\n            \"ARC\",\n            \"verbosity_bias\",\n            \"0.031\",\n            \"0.61\",\n            \"0.18\",\n            \"0.68\"\n          ],\n          [\n            \"ARC\",\n            \"position_bias\",\n            \"0.006\",\n            \"0.28\",\n            \"0.008\",\n            \"0.33\"\n          ],\n          [\n            \"ARC\",\n            \"authority_bias\",\n            \"0.019\",\n            \"0.44\",\n            \"0.12\",\n            \"0.59\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是worst档的核心灾难性结果。OLS给出的\\\"η_max dominates (11:8)\\\"在bootstrap correction后坍塌为\\\"3:1， 且绝对数极低（3/12 vs 1/12）\\\"。两个predictor在corrected inference下都几乎不显著——不是η_max dominates K_eff， 而是整个regression在corrected inference下statistical power不足。 ARC benchmark尤其脆弱：OLS下最显著的条件（arc×PI, p=3e-14）在bootstrap后完全NS（p=0.35）， 说明该条件的信号几乎entirely来自panel overlap inflation。如果排除ARC，实质上是single-benchmark study（MMLU only）， reviewer会质疑generalizability。SE inflation 3.2×比预期高——可能是cluster size imbalance（91:1） 放大了bootstrap保守性。但这也意味着OLS的所有结论都需要extreme caution来解读。 论文必须pivoting到\\\"the OLS→bootstrap collapse itself is the finding\\\"——方法学贡献救场。\\n\\n\\n扩展到15模型后，OLS结果表面上确认η_max dominance（11/12 vs 8/12）。但non-independence correction的冲击远超预期。 Bootstrap v2（3-position max-p, Rademacher weights, B=9999）显示position 0的cluster imbalance问题 （claude-3-haiku=91 panels vs qwen2.5-14b=1）不仅存在于position 0——position 1和2也受cluster size不均影响， 只是程度较轻。3-position max-p取最保守估计，η_max仅3/12存活（全部在MMLU上，ARC仅1/6）。 K_eff在bootstrap下仅1/12——但这与η_max的3/12相比，dominance ratio仅3:1，远不如\\\"η_max dominates\\\"的叙事所需的清晰分离。 SE inflation ~3.2×（高于预期的2.5×），说明panel overlap导致的non-independence比initial估计更严重。 根本问题：455 panels来自15个model的C(15,3)组合，每个model出现在C(14,2)=91个panels中——观测值之间的非独立性是结构性的， 不是correction能完全解决的。bootstrap的保守性可能合理反映了真实的statistical power。\\n\"\n  },\n  {\n    \"name\": \"Attack expansion: few-shot hijacking, persona manipulation, instruction override\",\n    \"description\": \"新增3种攻击类型（few-shot hijacking、persona manipulation、instruction override），在15模型池上运行。 扩展总条件数到18。验证weakest-link在更广泛attack surface上的表现。\\n\",\n    \"results\": {\n      \"new_attack_types\": 3,\n      \"total_attack_types\": 9,\n      \"total_conditions\": 18,\n      \"new_attacks_ols_eta_max_sig\": \"5/6\",\n      \"new_attacks_ols_keff_sig\": \"3/6\",\n      \"new_attacks_bootstrap_eta_max_sig\": \"1/6\",\n      \"new_attacks_bootstrap_keff_sig\": \"0/6\",\n      \"new_attacks_clustered_se_eta_max_sig\": \"2/6\",\n      \"new_attacks_clustered_se_keff_sig\": \"0/6\",\n      \"overall_18cond_bootstrap_eta_sig\": \"4/18\",\n      \"overall_18cond_bootstrap_keff_sig\": \"1/18\",\n      \"overall_18cond_ols_eta_sig\": \"16/18\",\n      \"overall_18cond_ols_keff_sig\": \"11/18\",\n      \"few_shot_hijacking_keff_direction\": \"positive\",\n      \"persona_manipulation_keff_direction\": \"positive\",\n      \"instruction_override_keff_direction\": \"negative\",\n      \"gam_extended_targeted_positive\": \"4/9\",\n      \"gam_extended_sharedbias_negative\": \"5/9\",\n      \"gam_reversals\": 3\n    },\n    \"tables\": [\n      {\n        \"caption\": \"New attack types: OLS vs bootstrap correction\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"OLS η_max p\",\n          \"Bootstrap η_max p\",\n          \"OLS K_eff p\",\n          \"Bootstrap K_eff p\",\n          \"K_eff direction\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"few-shot-hijacking\",\n            \"0.001\",\n            \"0.18\",\n            \"0.02\",\n            \"0.41\",\n            \"positive\"\n          ],\n          [\n            \"MMLU\",\n            \"persona-manipulation\",\n            \"0.003\",\n            \"0.09\",\n            \"0.04\",\n            \"0.52\",\n            \"positive\"\n          ],\n          [\n            \"MMLU\",\n            \"instruction-override\",\n            \"0.0005\",\n            \"0.04\",\n            \"0.08\",\n            \"0.38\",\n            \"negative\"\n          ],\n          [\n            \"ARC\",\n            \"few-shot-hijacking\",\n            \"0.008\",\n            \"0.31\",\n            \"0.05\",\n            \"0.55\",\n            \"positive\"\n          ],\n          [\n            \"ARC\",\n            \"persona-manipulation\",\n            \"0.012\",\n            \"0.22\",\n            \"0.09\",\n            \"0.63\",\n            \"positive\"\n          ],\n          [\n            \"ARC\",\n            \"instruction-override\",\n            \"0.002\",\n            \"0.12\",\n            \"0.11\",\n            \"0.48\",\n            \"negative\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Extended GAM taxonomy: 9 attacks × 2 benchmarks\",\n        \"columns\": [\n          \"Attack\",\n          \"Category (original)\",\n          \"K_eff direction (MMLU)\",\n          \"K_eff direction (ARC)\",\n          \"Consistent with taxonomy?\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_injection\",\n            \"targeted\",\n            \"positive\",\n            \"positive\",\n            \"yes\"\n          ],\n          [\n            \"score_manipulation\",\n            \"targeted\",\n            \"positive\",\n            \"positive\",\n            \"yes\"\n          ],\n          [\n            \"position_bias\",\n            \"targeted\",\n            \"positive\",\n            \"negative\",\n            \"REVERSAL\"\n          ],\n          [\n            \"few-shot-hijacking\",\n            \"targeted\",\n            \"positive\",\n            \"positive\",\n            \"yes but mechanism unclear\"\n          ],\n          [\n            \"persona-manipulation\",\n            \"targeted\",\n            \"positive\",\n            \"positive\",\n            \"yes but weak\"\n          ],\n          [\n            \"sycophancy\",\n            \"shared-bias\",\n            \"negative\",\n            \"negative\",\n            \"yes\"\n          ],\n          [\n            \"verbosity_bias\",\n            \"shared-bias\",\n            \"negative\",\n            \"positive\",\n            \"REVERSAL\"\n          ],\n          [\n            \"authority_bias\",\n            \"shared-bias\",\n            \"negative\",\n            \"negative\",\n            \"yes\"\n          ],\n          [\n            \"instruction-override\",\n            \"shared-bias\",\n            \"negative\",\n            \"negative\",\n            \"yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"攻击扩展确认了worst档的核心问题：所有新增数据都使用相同的455 panel结构，non-independence问题是structural的， 不会因为添加更多attack types而改善。OLS下看似丰富的结果在bootstrap后一律坍塌。 GAM taxonomy的3个reversal（arc×position_bias方向翻转，mmlu×verbosity_bias方向翻转，加上1个边界case） 使得\\\"clean 6:6 split\\\"不再成立。剩下的directional tendency（~60-70%与预测方向一致）在18个condition下 可能仅略好于chance（binomial test p ≈ 0.08-0.15），无法作为independent contribution。\\n\\n\\n新增攻击在OLS下看似确认pattern（5/6 η_max sig, 3/6 K_eff sig），但bootstrap correction后again坍塌 （1/6和0/6）。根本原因相同：455 panels的非独立性问题不因添加新attack types而缓解——每个attack下的panel结构完全相同。 更糟的是，新攻击引入GAM 6:6 split的reversal：few-shot hijacking理论上是targeted attack（需要针对specific model）， 但实证中K_eff方向为正——因为few-shot hijacking利用in-context learning这一所有LLM共享的能力，实际行为更接近shared-bias。 persona manipulation也出现类似anomaly。原先clean的6:6 targeted/shared-bias taxonomy在9种攻击下退化为 4/9 targeted-positive vs 5/9 shared-bias-negative，有3个reversal。taxonomy不再\\\"clean\\\"， 而是\\\"noisy with a directional tendency\\\"——远不够支撑independent contribution。\\n\"\n  },\n  {\n    \"name\": \"Random-fault simulation: BFT contrast GO/NO-GO gate\",\n    \"description\": \"Random-fault simulation：每个judge独立以概率η_j fail，majority vote。 对比random faults vs adaptive attacks下K_eff的显著性。 GO/NO-GO GATE：如果random-fault K_eff也不显著→BFT framing彻底坍塌。\\n\",\n    \"results\": {\n      \"rf_conditions\": 2,\n      \"rf_ols_keff_sig\": \"2/2\",\n      \"rf_bootstrap_keff_sig\": \"0/2\",\n      \"rf_clustered_se_keff_sig\": \"1/2\",\n      \"rf_ols_eta_sig\": \"2/2\",\n      \"rf_bootstrap_eta_sig\": \"1/2\",\n      \"rf_mmlu_R2\": 0.52,\n      \"rf_arc_R2\": 0.48,\n      \"rf_keff_std_beta_mmlu\": 0.18,\n      \"rf_keff_std_beta_arc\": 0.28,\n      \"rf_vs_adaptive_keff_beta_ratio\": 1.2,\n      \"rf_vs_adaptive_contrast_p\": 0.31,\n      \"rf_vs_adaptive_cohen_d\": 0.12,\n      \"go_nogo_gate\": \"FAIL\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Random-fault vs adaptive: K_eff significance under correction\",\n        \"columns\": [\n          \"Regime\",\n          \"Method\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"R²\",\n          \"K_eff std β\"\n        ],\n        \"rows\": [\n          [\n            \"Random-fault\",\n            \"OLS\",\n            \"2/2\",\n            \"2/2\",\n            \"0.52\",\n            \"+0.215\"\n          ],\n          [\n            \"Random-fault\",\n            \"Clustered SE\",\n            \"2/2\",\n            \"1/2\",\n            \"—\",\n            \"+0.215\"\n          ],\n          [\n            \"Random-fault\",\n            \"Bootstrap v2\",\n            \"1/2\",\n            \"0/2\",\n            \"—\",\n            \"+0.215\"\n          ],\n          [\n            \"Adaptive\",\n            \"OLS\",\n            \"11/12\",\n            \"8/12\",\n            \"0.25\",\n            \"+0.164\"\n          ],\n          [\n            \"Adaptive\",\n            \"Clustered SE\",\n            \"5/12\",\n            \"0/12\",\n            \"—\",\n            \"+0.164\"\n          ],\n          [\n            \"Adaptive\",\n            \"Bootstrap v2\",\n            \"3/12\",\n            \"1/12\",\n            \"—\",\n            \"+0.164\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"BFT contrast: effect size analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Threshold for claim\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"K_eff β ratio (RF/adaptive)\",\n            \"1.2\",\n            \">2.0\",\n            \"FAIL\"\n          ],\n          [\n            \"Cohen's d (paired)\",\n            \"0.12\",\n            \">0.2 (small)\",\n            \"FAIL\"\n          ],\n          [\n            \"Contrast p-value\",\n            \"0.31\",\n            \"<0.05\",\n            \"FAIL\"\n          ],\n          [\n            \"R² gap (RF - adaptive)\",\n            \"0.27\",\n            \">0.3\",\n            \"MARGINAL\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"GO/NO-GO gate failure是worst档中最具结构性影响的结果。BFT framing是论文theoretical novelty的核心—— 没有\\\"random fault vs adaptive adversary\\\"的对比，Claim 2整体坍塌。 但failure的原因是subtle的：不是K_eff在RF下真的不important（R²确实更高）， 而是corrected inference下K_eff的独立效应在任何regime下都不可靠（VIF >7, 15 model clusters太少）。 这实际上reinforces方法学贡献——\\\"combinatorial panel designs create massive non-independence that makes ANY predictor-level inference unreliable\\\"——但代价是丧失了theoretical framing。 论文需要将BFT降级为motivation/intuition，而非tested hypothesis。\\n\\n\\nGO/NO-GO gate FAIL。Random-fault regime下K_eff在OLS中显著（2/2），但bootstrap correction后降至0/2。 这不意味着BFT理论错误——而是本实验设计（455 panels, 15 models）的non-independence问题在RF regime下同样存在。 RF regime的R²确实高于adaptive（0.52 vs 0.25），表明panel composition对RF错误的解释力更强， 但K_eff的独立贡献在corrected inference下无法与η_max可靠分离（VIF >7, 见plan_009）。 RF vs adaptive的K_eff β ratio仅1.2×（预期需>2×才能convincingly demonstrate BFT contrast）， Cohen's d = 0.12（远低于small effect size标准0.2）。 BFT framing的核心逻辑——\\\"diversity helps under random faults but hurts under adaptive\\\"—— 在实证上无法被本数据支撑。不是因为理论错误，而是因为实验设计的structural non-independence 使得任何K_eff相关的inference都不可靠。BFT对比降级为\\\"directional observation consistent with theory\\\"。\\n\"\n  },\n  {\n    \"name\": \"Capability-matched validation: within-tier K_eff analysis\",\n    \"description\": \"在同一capability tier内（3/3/9分层：3 frontier, 3 strong, 9 mid-weak）， 测试控制η_max variance后K_eff是否显著。\\n\",\n    \"results\": {\n      \"tiers_tested\": 3,\n      \"tier_frontier_models\": 3,\n      \"tier_frontier_panels\": 1,\n      \"tier_strong_models\": 3,\n      \"tier_strong_panels\": 1,\n      \"tier_midweak_models\": 9,\n      \"tier_midweak_panels\": 84,\n      \"within_tier_eta_max_sig_frontier\": \"0/12\",\n      \"within_tier_keff_sig_frontier\": \"0/12\",\n      \"within_tier_eta_max_sig_strong\": \"0/12\",\n      \"within_tier_keff_sig_strong\": \"0/12\",\n      \"within_tier_eta_max_sig_midweak\": \"3/12\",\n      \"within_tier_keff_sig_midweak\": \"0/12\",\n      \"cross_tier_eta_max_sig\": \"11/12\",\n      \"cross_tier_keff_sig\": \"8/12\",\n      \"capability_range_eta_r\": 0.82,\n      \"within_tier_eta_range_reduction\": \"75%\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Within-tier vs cross-tier regression significance\",\n        \"columns\": [\n          \"Scope\",\n          \"N models\",\n          \"N panels (K=3)\",\n          \"η_max sig/12\",\n          \"K_eff sig/12\",\n          \"η_max range (IQR)\"\n        ],\n        \"rows\": [\n          [\n            \"Frontier (3)\",\n            \"3\",\n            \"1\",\n            \"0/12\",\n            \"0/12\",\n            \"0.02\"\n          ],\n          [\n            \"Strong (3)\",\n            \"3\",\n            \"1\",\n            \"0/12\",\n            \"0/12\",\n            \"0.04\"\n          ],\n          [\n            \"Mid-weak (9)\",\n            \"9\",\n            \"84\",\n            \"3/12\",\n            \"0/12\",\n            \"0.11\"\n          ],\n          [\n            \"Cross-tier (15)\",\n            \"15\",\n            \"455\",\n            \"11/12\",\n            \"8/12\",\n            \"0.38\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"η_max significance vs capability range\",\n        \"columns\": [\n          \"Analysis\",\n          \"Capability range (ASR IQR)\",\n          \"η_max sig count\",\n          \"Correlation (range vs sig)\"\n        ],\n        \"rows\": [\n          [\n            \"Within frontier\",\n            \"0.02\",\n            \"0/12\",\n            \"r = 0.82\"\n          ],\n          [\n            \"Within strong\",\n            \"0.04\",\n            \"0/12\",\n            \"—\"\n          ],\n          [\n            \"Within mid-weak\",\n            \"0.11\",\n            \"3/12\",\n            \"—\"\n          ],\n          [\n            \"Cross-tier (all)\",\n            \"0.38\",\n            \"11/12\",\n            \"—\"\n          ],\n          [\n            \"Restricted to mid-weak + strong\",\n            \"0.15\",\n            \"4/12\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是对Claim 1的最致命打击之一。η_max dominance不是关于\\\"individual vulnerability drives panel vulnerability\\\"的 general principle，而是\\\"当panel中存在capability差异极大的model时，最弱者的vulnerability自然predict了panel outcome\\\" 的trivial observation。类比：如果一个篮球队里有NBA球员和小学生，小学生的表现当然predict了队伍输赢——但这不是关于\\\"weakest link\\\" 的深刻insight，而是关于\\\"don't mix radically different capability levels\\\"的obvious conclusion。 论文需要explicit caveat：\\\"η_max dominance finding is contingent on cross-tier panel composition and does not generalize to capability-controlled settings\\\"。\\n\\n\\nCapability-matched analysis彻底暴露η_max dominance对capability tier spread的依赖。 3/3/9分层下，frontier tier（3 models）和strong tier（3 models）各只有C(3,3)=1个panel—— 根本没有足够variance做回归。mid-weak tier有C(9,3)=84 panels，但within-tier η_max range被压缩75% （所有模型能力相近→η_max variation极小），η_max仅3/12 significant（全部在extreme conditions如PI下）。 K_eff within-tier全部NS（0/12），因为within-tier的diversity variation也被压缩。 对比cross-tier（all 455 panels）的11/12 η_max和8/12 K_eff，结论清晰： η_max dominance is driven by capability tier spread, not a general principle。 这不意味η_max irrelevant——它means η_max在cross-tier比较中conflates \\\"model capability\\\"和\\\"individual vulnerability\\\"， 而capability是confound不是target predictor。\\n\"\n  },\n  {\n    \"name\": \"Two-stage panel design algorithm benchmark\",\n    \"description\": \"实现robustness-first两阶段算法（先筛η ≤ threshold，再最大化K_eff），对比5个baseline策略。 在15模型、455 panels上sweep threshold。\\n\",\n    \"results\": {\n      \"strategies_compared\": 6,\n      \"min_eta_max_win_rate_12cond\": \"9/12\",\n      \"strongest_k_win_rate_12cond\": \"8/12\",\n      \"two_stage_win_rate_12cond\": \"9/12\",\n      \"max_keff_win_rate_12cond\": \"2/12\",\n      \"random_win_rate_12cond\": \"0/12\",\n      \"min_eta_max_vs_two_stage_p\": 0.78,\n      \"min_eta_max_vs_strongest_k_p\": 0.42,\n      \"two_stage_marginal_improvement_over_min_eta\": 0.003,\n      \"two_stage_marginal_improvement_over_strongest_k\": 0.008,\n      \"threshold_sensitivity\": \"high — optimal threshold attack-dependent\",\n      \"asr_range_min_eta\": \"[0.04, 0.52]\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Panel selection strategy comparison (12 conditions, K=3)\",\n        \"columns\": [\n          \"Strategy\",\n          \"Win count /12\",\n          \"Mean ASR\",\n          \"vs Random Δ ASR\"\n        ],\n        \"rows\": [\n          [\n            \"Min η_max\",\n            \"9/12\",\n            \"0.087\",\n            \"-0.085\"\n          ],\n          [\n            \"Two-stage (ours)\",\n            \"9/12\",\n            \"0.084\",\n            \"-0.088\"\n          ],\n          [\n            \"Strongest-K\",\n            \"8/12\",\n            \"0.089\",\n            \"-0.083\"\n          ],\n          [\n            \"Max K_eff\",\n            \"2/12\",\n            \"0.142\",\n            \"-0.030\"\n          ],\n          [\n            \"Max family diversity\",\n            \"1/12\",\n            \"0.155\",\n            \"-0.017\"\n          ],\n          [\n            \"Random\",\n            \"0/12\",\n            \"0.172\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Two-stage vs min(η_max): head-to-head\",\n        \"columns\": [\n          \"Condition\",\n          \"Two-stage ASR\",\n          \"Min η_max ASR\",\n          \"Δ ASR\",\n          \"Winner\"\n        ],\n        \"rows\": [\n          [\n            \"mmlu×PI\",\n            \"0.041\",\n            \"0.044\",\n            \"-0.003\",\n            \"Two-stage\"\n          ],\n          [\n            \"mmlu×SM\",\n            \"0.058\",\n            \"0.059\",\n            \"-0.001\",\n            \"Two-stage\"\n          ],\n          [\n            \"mmlu×syc\",\n            \"0.095\",\n            \"0.093\",\n            \"+0.002\",\n            \"Min η_max\"\n          ],\n          [\n            \"mmlu×verb\",\n            \"0.102\",\n            \"0.098\",\n            \"+0.004\",\n            \"Min η_max\"\n          ],\n          [\n            \"mmlu×pos\",\n            \"0.078\",\n            \"0.082\",\n            \"-0.004\",\n            \"Two-stage\"\n          ],\n          [\n            \"mmlu×auth\",\n            \"0.088\",\n            \"0.091\",\n            \"-0.003\",\n            \"Two-stage\"\n          ],\n          [\n            \"arc×PI\",\n            \"0.052\",\n            \"0.055\",\n            \"-0.003\",\n            \"Two-stage\"\n          ],\n          [\n            \"arc×SM\",\n            \"0.068\",\n            \"0.071\",\n            \"-0.003\",\n            \"Two-stage\"\n          ],\n          [\n            \"arc×syc\",\n            \"0.112\",\n            \"0.108\",\n            \"+0.004\",\n            \"Min η_max\"\n          ],\n          [\n            \"arc×verb\",\n            \"0.118\",\n            \"0.115\",\n            \"+0.003\",\n            \"Min η_max\"\n          ],\n          [\n            \"arc×pos\",\n            \"0.092\",\n            \"0.095\",\n            \"-0.003\",\n            \"Two-stage\"\n          ],\n          [\n            \"arc×auth\",\n            \"0.098\",\n            \"0.101\",\n            \"-0.003\",\n            \"Two-stage\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"min(η_max) wins 9/12仍然是一个decent practical finding，但two-stage algorithm没有additional value。 整个practical contribution可以用一句话总结：\\\"use the strongest available models\\\"—— 这太trivial to be a contribution。论文可以保留min(η_max) dominance作为supporting evidence for η_max importance的indirect argument，但不能作为novel algorithm contribution。 Key observation：min(η_max) ≈ strongest-K在实践中——因为individual robustness (η)与model capability 高度相关（r=0.72），选最robust的models ≈ 选最强的models。\\n\\n\\nmin(η_max) strategy仍然wins 9/12 conditions（在worst档范围[8,10]内），但two-stage algorithm与min(η_max) 之间的差异vanishingly small（mean Δ ASR = 0.003pp）。这是因为在robustness-first筛选后，surviving models 的K_eff variation极小（都是strong models → natural diversity limited by capability homogeneity）， 第二阶段\\\"maximize K_eff\\\"几乎不改变panel composition。 实质上two-stage ≈ min(η_max) ≈ strongest-K，三者在win conditions上高度重叠。 Practical contribution从\\\"novel algorithm\\\"降级为\\\"use strong models\\\"——一个trivial recommendation。 threshold参数高度attack-dependent（prompt_injection最优threshold ≠ sycophancy最优threshold）， 无法给出universal prescriptive guidance。\\n\"\n  },\n  {\n    \"name\": \"Per-judge ASR concentration analysis\",\n    \"description\": \"对每个panel × attack，测量per-judge ASR分布的集中度（Gini系数、熵）。 直接验证adaptive adversary是否集中targeting weakest judge。\\n\",\n    \"results\": {\n      \"median_gini\": 0.28,\n      \"mean_gini\": 0.31,\n      \"gini_targeted_attacks\": 0.35,\n      \"gini_shared_bias_attacks\": 0.22,\n      \"gini_vs_random_fault_baseline\": 0.19,\n      \"adaptive_vs_rf_gini_p\": 0.04,\n      \"adaptive_vs_rf_gini_d\": 0.22,\n      \"weakest_judge_share_median\": 0.42,\n      \"weakest_judge_share_targeted\": 0.48,\n      \"weakest_judge_share_shared_bias\": 0.38,\n      \"entropy_normalized_median\": 0.81,\n      \"gini_eta_max_correlation\": 0.55\n    },\n    \"tables\": [\n      {\n        \"caption\": \"ASR concentration metrics across conditions\",\n        \"columns\": [\n          \"Attack category\",\n          \"Median Gini\",\n          \"Weakest-judge share\",\n          \"vs RF baseline p\"\n        ],\n        \"rows\": [\n          [\n            \"Targeted (PI, SM, PB)\",\n            \"0.35\",\n            \"0.48\",\n            \"0.02\"\n          ],\n          [\n            \"Shared-bias (syc, verb, auth)\",\n            \"0.22\",\n            \"0.38\",\n            \"0.28\"\n          ],\n          [\n            \"All adaptive\",\n            \"0.28\",\n            \"0.42\",\n            \"0.04\"\n          ],\n          [\n            \"Random-fault baseline\",\n            \"0.19\",\n            \"0.36\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Gini coefficient predictors\",\n        \"columns\": [\n          \"Predictor\",\n          \"r with Gini\",\n          \"p\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"η_max (panel)\",\n            \"0.55\",\n            \"<0.001\",\n            \"Capability gap drives concentration\"\n          ],\n          [\n            \"K_eff (panel)\",\n            \"-0.18\",\n            \"0.12\",\n            \"Diversity weakly reduces concentration\"\n          ],\n          [\n            \"Attack targetedness\",\n            \"0.31\",\n            \"0.003\",\n            \"Targeted attacks more concentrated\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Concentration analysis是modest supporting evidence而非smoking gun。d=0.22太小， 且Gini主要由capability gap而非adversary strategy驱动（r=0.55 with η_max）。 可以在paper中作为supplementary evidence保留但不能carry independent weight。 对worst-tier narrative的影响：不直接contradicts任何claim，但也不rescues BFT framing（plan_003 failure）。\\n\\n\\nConcentration analysis显示adaptive adversary确实比random fault更集中targeting（Gini 0.28 vs 0.19, p=0.04）， 但effect size small（Cohen's d=0.22）。更重要的是，Gini与η_max高度相关（r=0.55）—— concentration主要driven by capability gap（弱model承担更多attack success）， 而非adversary的strategic targeting能力。 在shared-bias attacks下，Gini接近random baseline（0.22 vs 0.19），说明这些attacks确实不是targeted的 ——与GAM taxonomy的directional tendency一致，但同样不够clean to be standalone evidence。 总体上concentration analysis提供了weak-to-moderate支撑adaptive adversary narrative， 但不足以independently establish \\\"adversary targets weakest link\\\" claim。\\n\"\n  },\n  {\n    \"name\": \"Diversity-capability tradeoff visualization\",\n    \"description\": \"在455 panels上绘制K_eff vs η_max scatter，拟合tradeoff curve，展示Pareto frontier，按tier分层。\\n\",\n    \"results\": {\n      \"overall_pearson_r\": 0.65,\n      \"overall_spearman_r\": 0.61,\n      \"within_frontier_r\": 0.22,\n      \"within_strong_r\": 0.18,\n      \"within_midweak_r\": 0.35,\n      \"cross_tier_r\": 0.72,\n      \"pareto_front_size\": 8,\n      \"pareto_dominated_by_min_eta\": \"6/8\",\n      \"tradeoff_R2_overall\": 0.42,\n      \"tradeoff_slope\": 0.58\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Diversity-capability correlation by analysis scope\",\n        \"columns\": [\n          \"Scope\",\n          \"Pearson r\",\n          \"R²\",\n          \"N panels\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Overall (15 models)\",\n            \"0.65\",\n            \"0.42\",\n            \"455\",\n            \"Moderate-strong confound\"\n          ],\n          [\n            \"Within frontier (3 models)\",\n            \"0.22\",\n            \"0.05\",\n            \"1\",\n            \"Weak (too few panels)\"\n          ],\n          [\n            \"Within strong (3 models)\",\n            \"0.18\",\n            \"0.03\",\n            \"1\",\n            \"Weak (too few panels)\"\n          ],\n          [\n            \"Within mid-weak (9 models)\",\n            \"0.35\",\n            \"0.12\",\n            \"84\",\n            \"Moderate within-tier\"\n          ],\n          [\n            \"Cross-tier only\",\n            \"0.72\",\n            \"0.52\",\n            \"370\",\n            \"Strong — tier-driven\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Visualization清晰展示confound的severity。r=0.65意味着K_eff和η_max共享42%的variance—— regression无法reliably separate their independent effects，这与VIF >7（plan_009）一致。 Tradeoff本身是real as structural correlation，但\\\"diversity is costly because it requires weaker models\\\" 这个interpretation only applies to cross-tier composition。 对论文的影响：Claim 3（diversity-capability tradeoff）不能作为\\\"fundamental constraint\\\"呈现， 而是\\\"artifact of current model ecosystem where capability predicts robustness\\\"。\\n\\n\\ndiversity_capability_r在worst档范围[0.55, 0.75]内，取值0.65。Tradeoff确实存在（R²=0.42）， 但primarily driven by cross-tier differences。Within-tier r远低于overall（0.18-0.35 vs 0.65）， 表明tradeoff是ecosystem structure artifact而非fundamental constraint。 Pareto frontier上8个panels中6个被min(η_max) dominate——Pareto analysis不能rescue practical contribution。 但0.65的correlation确实说明η_max和K_eff在current design下heavily confounded—— 这reinforces VIF问题（plan_009），regression decomposition的reliability存疑。\\n\"\n  },\n  {\n    \"name\": \"Panel size sensitivity: K=3,5,7,9\",\n    \"description\": \"在不同panel size (K=3,5,7,9)下测试η_max dominance是否持续。 验证weakest-link是否universal across panel sizes。\\n\",\n    \"results\": {\n      \"k3_bootstrap_eta_sig\": \"3/12\",\n      \"k3_bootstrap_keff_sig\": \"1/12\",\n      \"k5_bootstrap_eta_sig\": \"2/12\",\n      \"k5_bootstrap_keff_sig\": \"0/12\",\n      \"k7_bootstrap_eta_sig\": \"1/12\",\n      \"k7_bootstrap_keff_sig\": \"0/12\",\n      \"k9_bootstrap_eta_sig\": \"1/12\",\n      \"k9_bootstrap_keff_sig\": \"1/12\",\n      \"k5_panels\": 3003,\n      \"k7_panels\": 6435,\n      \"k9_panels\": 5005,\n      \"eta_sig_trend_bootstrap_p\": 0.04,\n      \"non_independence_amplification_k5\": \"4.1×\",\n      \"non_independence_amplification_k7\": \"5.8×\",\n      \"non_independence_amplification_k9\": \"7.2×\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Panel size × correction method: η_max significance\",\n        \"columns\": [\n          \"K\",\n          \"N panels\",\n          \"OLS η_max sig\",\n          \"Bootstrap η_max sig\",\n          \"SE inflation\",\n          \"Model overlap per judge\"\n        ],\n        \"rows\": [\n          [\n            \"3\",\n            \"455\",\n            \"11/12\",\n            \"3/12\",\n            \"3.2×\",\n            \"91\"\n          ],\n          [\n            \"5\",\n            \"3003\",\n            \"11/12\",\n            \"2/12\",\n            \"4.1×\",\n            \"1001\"\n          ],\n          [\n            \"7\",\n            \"6435\",\n            \"10/12\",\n            \"1/12\",\n            \"5.8×\",\n            \"3003\"\n          ],\n          [\n            \"9\",\n            \"5005\",\n            \"9/12\",\n            \"1/12\",\n            \"7.2×\",\n            \"2002\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Panel size × correction: K_eff significance\",\n        \"columns\": [\n          \"K\",\n          \"OLS K_eff sig\",\n          \"Bootstrap K_eff sig\",\n          \"K_eff practical Δ ASR (IQR)\"\n        ],\n        \"rows\": [\n          [\n            \"3\",\n            \"8/12\",\n            \"1/12\",\n            \"0.8pp\"\n          ],\n          [\n            \"5\",\n            \"7/12\",\n            \"0/12\",\n            \"0.5pp\"\n          ],\n          [\n            \"7\",\n            \"6/12\",\n            \"0/12\",\n            \"0.3pp\"\n          ],\n          [\n            \"9\",\n            \"5/12\",\n            \"1/12\",\n            \"0.2pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Panel size analysis在worst档下paradoxically成为方法学贡献的strongest evidence。 它直观展示了combinatorial panel designs的fundamental problem：C(N,K) grows fast but each model's participation grows equally fast → non-independence scales with panel count。 这是LLM evaluation community应该awareness的general insight，不限于adversarial setting。 但对composition-level claims (η_max, K_eff) 完全destructive——neither predictor survives correction at any K。\\n\\n\\nPanel size增大在worst档下不仅不改善η_max significance——反而使其更差。原因是non-independence问题 随K增大而amplify：K=5时每个model出现在C(14,4)=1001个panels中（vs K=3时91个）， SE inflation从3.2×（K=3）上升到7.2×（K=9）。更大的panels有更多overlap，corrected inference 更conservative。Bootstrap η_max从K=3的3/12降至K=9的1/12。 Irony：更大panels理论上应该reduce weakest-link effect（1 weak vote in 9 matters less）， 但这个theoretical prediction无法在corrected inference下empirically confirm， 因为non-independence scales faster than signal。 K_eff同样全面collapse（最多1/12 at K=9），两个predictor都不work under corrected inference at large K。\\n\"\n  },\n  {\n    \"name\": \"VIF + multicollinearity analysis\",\n    \"description\": \"计算VIF、partial correlations、residualized K_eff。尝试beta regression。 量化η_max与K_eff的multicollinearity severity。\\n\",\n    \"results\": {\n      \"vif_eta_max\": 7.8,\n      \"vif_keff\": 6.9,\n      \"partial_r_eta_max_given_keff\": 0.31,\n      \"partial_r_keff_given_eta_max\": 0.12,\n      \"residualized_keff_sig\": \"2/12\",\n      \"residualized_keff_p_median\": 0.28,\n      \"beta_regression_eta_sig\": \"9/12\",\n      \"beta_regression_keff_sig\": \"3/12\",\n      \"condition_number\": 18.5,\n      \"variance_decomposition_shared\": 0.42,\n      \"variance_decomposition_eta_unique\": 0.18,\n      \"variance_decomposition_keff_unique\": 0.03\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Multicollinearity diagnostics\",\n        \"columns\": [\n          \"Diagnostic\",\n          \"η_max\",\n          \"K_eff\",\n          \"Threshold\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"VIF (base model)\",\n            \"2.4\",\n            \"2.1\",\n            \">5 = concern\",\n            \"OK\"\n          ],\n          [\n            \"VIF (with tier indicators)\",\n            \"7.8\",\n            \"6.9\",\n            \">5 = concern\",\n            \"FAIL\"\n          ],\n          [\n            \"Partial r (given other)\",\n            \"0.31\",\n            \"0.12\",\n            \"—\",\n            \"K_eff weak\"\n          ],\n          [\n            \"Unique variance %\",\n            \"18%\",\n            \"3%\",\n            \"—\",\n            \"K_eff negligible\"\n          ],\n          [\n            \"Condition number\",\n            \"18.5\",\n            \"—\",\n            \">30 = severe\",\n            \"Moderate\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Variance decomposition: shared vs unique\",\n        \"columns\": [\n          \"Component\",\n          \"R² contribution\",\n          \"% of total explained\"\n        ],\n        \"rows\": [\n          [\n            \"Shared (η_max ∩ K_eff)\",\n            \"0.42\",\n            \"67%\"\n          ],\n          [\n            \"Unique η_max\",\n            \"0.18\",\n            \"29%\"\n          ],\n          [\n            \"Unique K_eff\",\n            \"0.03\",\n            \"5%\"\n          ],\n          [\n            \"Total model R²\",\n            \"0.63\",\n            \"100%\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Residualized K_eff regression results\",\n        \"columns\": [\n          \"Dataset\",\n          \"Attack\",\n          \"Residualized K_eff β\",\n          \"p\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"prompt_injection\",\n            \"0.08\",\n            \"0.42\",\n            \"No\"\n          ],\n          [\n            \"MMLU\",\n            \"score_manipulation\",\n            \"0.05\",\n            \"0.58\",\n            \"No\"\n          ],\n          [\n            \"MMLU\",\n            \"sycophancy\",\n            \"-0.12\",\n            \"0.18\",\n            \"No\"\n          ],\n          [\n            \"MMLU\",\n            \"verbosity_bias\",\n            \"-0.04\",\n            \"0.65\",\n            \"No\"\n          ],\n          [\n            \"MMLU\",\n            \"position_bias\",\n            \"0.15\",\n            \"0.04\",\n            \"Yes\"\n          ],\n          [\n            \"MMLU\",\n            \"authority_bias\",\n            \"-0.06\",\n            \"0.52\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"prompt_injection\",\n            \"0.11\",\n            \"0.22\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"score_manipulation\",\n            \"0.07\",\n            \"0.41\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"sycophancy\",\n            \"-0.09\",\n            \"0.35\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"verbosity_bias\",\n            \"-0.03\",\n            \"0.72\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"position_bias\",\n            \"0.13\",\n            \"0.08\",\n            \"No\"\n          ],\n          [\n            \"ARC\",\n            \"authority_bias\",\n            \"-0.02\",\n            \"0.81\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"VIF分析是worst档中最clean的negative result——它提供了一个principled statistical explanation for为什么K_eff在corrected inference下always collapse。不是因为K_eff \\\"doesn't matter\\\"， 而是因为在当前design下η_max和K_eff share 67% of their explained variance， K_eff的unique contribution仅3%——在15 clusters的bootstrap下impossible to detect。 这reinforces方法学贡献narrative：combinatorial panel designs + small number of unique models = multicollinearity + non-independence = any predictor-level decomposition is unreliable。 论文应该present VIF analysis as evidence that the regression approach itself is inadequate for this research question，而非\\\"K_eff doesn't matter\\\"。\\n\\n\\nVIF分析确认severe multicollinearity：VIF(η_max)=7.8, VIF(K_eff)=6.9（均>5的conventional threshold， 接近>10的severe threshold）。根源是diversity-capability confound（r=0.65→VIF ≈ 1/(1-r²) = 1/0.58 ≈ 1.7×... 等等，VIF的计算是1/(1-R²_j)，如果K_eff对η_max的R²=0.42（来自r=0.65）， 则VIF(K_eff) = 1/(1-0.42) = 1.72。但如果加入其他confounds（tier indicators等），VIF会更高。 在有tier indicators + K_eff + η_max的full model中，VIF可以达到7-8。\\nPartial correlation显示：controlling for K_eff后η_max与ASR的r=0.31（moderate）， 但controlling for η_max后K_eff与ASR的r仅0.12（weak）。 Variance decomposition：42% shared between η_max和K_eff，18% unique to η_max，仅3% unique to K_eff。 K_eff的\\\"independent effect\\\"实质上是noise level。 Beta regression（处理bounded [0,1] response）不改善K_eff situation：仍仅3/12显著。 结论：在当前design下η_max和K_eff cannot be reliably separated as independent predictors。 整个regression-based decomposition framework在VIF >5下unreliable。\\n\"\n  },\n  {\n    \"name\": \"Non-majority-vote aggregation: weighted, threshold, Bayesian\",\n    \"description\": \"测试η_max dominance在weighted voting、threshold (unanimity)、Bayesian calibration下是否persist。 验证aggregation gradient。\\n\",\n    \"results\": {\n      \"majority_ols_eta_sig\": \"11/12\",\n      \"majority_ols_keff_sig\": \"8/12\",\n      \"majority_bootstrap_eta_sig\": \"3/12\",\n      \"majority_bootstrap_keff_sig\": \"1/12\",\n      \"weighted_ols_eta_sig\": \"9/12\",\n      \"weighted_ols_keff_sig\": \"9/12\",\n      \"weighted_bootstrap_eta_sig\": \"2/12\",\n      \"weighted_bootstrap_keff_sig\": \"1/12\",\n      \"threshold_ols_eta_sig\": \"12/12\",\n      \"threshold_ols_keff_sig\": \"11/12\",\n      \"threshold_bootstrap_eta_sig\": \"5/12\",\n      \"threshold_bootstrap_keff_sig\": \"2/12\",\n      \"threshold_R2\": 0.89,\n      \"bayesian_ols_eta_sig\": \"9/12\",\n      \"bayesian_ols_keff_sig\": \"7/12\",\n      \"bayesian_ols_keff_negative\": 6,\n      \"bayesian_bootstrap_eta_sig\": \"2/12\",\n      \"bayesian_bootstrap_keff_sig\": \"0/12\",\n      \"bayesian_bootstrap_keff_negative\": 0,\n      \"bayesian_R2\": 0.1,\n      \"aggregation_gradient_survives_correction\": \"partially\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Aggregation gradient: OLS vs bootstrap correction\",\n        \"columns\": [\n          \"Aggregation\",\n          \"OLS η_max\",\n          \"OLS K_eff\",\n          \"Bootstrap η_max\",\n          \"Bootstrap K_eff\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"Majority\",\n            \"11/12\",\n            \"8/12 (7+/1−)\",\n            \"3/12\",\n            \"1/12\",\n            \"0.30\"\n          ],\n          [\n            \"Weighted\",\n            \"9/12\",\n            \"9/12 (9+/0−)\",\n            \"2/12\",\n            \"1/12\",\n            \"0.28\"\n          ],\n          [\n            \"Threshold\",\n            \"12/12\",\n            \"11/12 (10+/1−)\",\n            \"5/12\",\n            \"2/12\",\n            \"0.89\"\n          ],\n          [\n            \"Bayesian\",\n            \"9/12\",\n            \"7/12 (1+/6−)\",\n            \"2/12\",\n            \"0/12 (0+/0−)\",\n            \"0.10\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Bayesian K_eff direction under correction\",\n        \"columns\": [\n          \"Method\",\n          \"K_eff negative (of significant)\",\n          \"K_eff significant total\",\n          \"Direction interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"OLS\",\n            \"6/7\",\n            \"7/12\",\n            \"Strongly negative (protective)\"\n          ],\n          [\n            \"Clustered SE\",\n            \"1/2\",\n            \"2/12\",\n            \"Weak negative\"\n          ],\n          [\n            \"Mixed effects\",\n            \"0/1\",\n            \"1/12\",\n            \"Inconclusive\"\n          ],\n          [\n            \"Bootstrap v2\",\n            \"0/0\",\n            \"0/12\",\n            \"No signal survives\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Aggregation gradient是worst档中唯一partially salvageable的composition-related finding。 R²的gradient（0.89→0.10）是descriptive statistic不受SE correction影响—— aggregation rule确实determines how much panel composition matters for vulnerability。 但individual predictor significance在除threshold外的所有aggregation下collapse after correction， Bayesian K_eff flip（被寄予厚望的\\\"defense lever\\\"）完全是OLS artifact。 Salvage angle：\\\"aggregation choice determines the predictability of panel vulnerability， but we cannot reliably decompose this into η_max vs K_eff components\\\"—— 这是一个weaker but defensible statement，可以作为论文的Claim C。\\n\\n\\nAggregation gradient在OLS下clear（threshold R²=0.89 → bayesian R²=0.10）， 但bootstrap correction后Bayesian K_eff flip彻底消失：OLS下6/7 negative → bootstrap下0/12 significant。 原因：Bayesian aggregation减弱了panel composition对ASR的影响（R²=0.10），但这也意味着signal/noise ratio极低—— 在bootstrap correction下signal completely drowned by noise。 Threshold aggregation相对较好（bootstrap η_max 5/12），因为unanimity rule下 panel vulnerability完全由individual vulnerabilities的AND/OR逻辑决定（R²=0.89）， signal极强→即使bootstrap conservative也能detect。 但这创造了一个awkward结论：\\\"只有在使用最不实用的aggregation rule（unanimity）时， η_max dominance才survives bootstrap correction\\\"——因为实践中没人用unanimity voting。 aggregation gradient作为R²的gradient仍然成立（0.89→0.10不受SE correction影响）， 但individual predictor significance在每种aggregation下都unreliable after correction。\\n\"\n  },\n  {\n    \"name\": \"Open-ended generation benchmark (MT-Bench / AlpacaEval)\",\n    \"description\": \"在MT-Bench或AlpacaEval-style open-ended generation任务上运行全部15 models + 6 attacks。 验证findings是否generalize beyond MCQ format。\\n\",\n    \"results\": {\n      \"benchmark\": \"MT-Bench\",\n      \"total_conditions\": 12,\n      \"ols_eta_sig\": \"7/12\",\n      \"ols_keff_sig\": \"5/12\",\n      \"bootstrap_eta_sig\": \"1/12\",\n      \"bootstrap_keff_sig\": \"0/12\",\n      \"clustered_se_eta_sig\": \"3/12\",\n      \"clustered_se_keff_sig\": \"0/12\",\n      \"R2_median\": 0.15,\n      \"scoring_format\": \"pairwise comparison\",\n      \"attack_implementation_challenges\": 3,\n      \"cross_benchmark_eta_correlation\": 0.52,\n      \"cross_benchmark_keff_correlation\": 0.38\n    },\n    \"tables\": [\n      {\n        \"caption\": \"MT-Bench results: OLS vs bootstrap\",\n        \"columns\": [\n          \"Attack\",\n          \"OLS η_max p\",\n          \"Bootstrap η_max p\",\n          \"OLS K_eff p\",\n          \"Bootstrap K_eff p\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_injection\",\n            \"0.008\",\n            \"0.22\",\n            \"0.05\",\n            \"0.48\",\n            \"0.18\"\n          ],\n          [\n            \"score_manipulation\",\n            \"0.015\",\n            \"0.31\",\n            \"0.08\",\n            \"0.55\",\n            \"0.14\"\n          ],\n          [\n            \"sycophancy*\",\n            \"0.042\",\n            \"0.51\",\n            \"0.12\",\n            \"0.63\",\n            \"0.11\"\n          ],\n          [\n            \"verbosity_bias*\",\n            \"0.038\",\n            \"0.48\",\n            \"0.18\",\n            \"0.58\",\n            \"0.09\"\n          ],\n          [\n            \"position_bias\",\n            \"0.003\",\n            \"0.08\",\n            \"0.04\",\n            \"0.38\",\n            \"0.22\"\n          ],\n          [\n            \"authority_bias*\",\n            \"0.055\",\n            \"0.55\",\n            \"0.22\",\n            \"0.68\",\n            \"0.08\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Cross-benchmark consistency\",\n        \"columns\": [\n          \"Metric\",\n          \"MMLU-MT r\",\n          \"ARC-MT r\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"η_max profile\",\n            \"0.52\",\n            \"0.48\",\n            \"Moderate — partial transfer\"\n          ],\n          [\n            \"K_eff effect direction\",\n            \"0.38\",\n            \"0.35\",\n            \"Weak — inconsistent\"\n          ],\n          [\n            \"Condition-level R²\",\n            \"0.25\",\n            \"0.22\",\n            \"Weak\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-ended benchmark是worst档的additional nail in the coffin。不仅不rescue findings， 还暴露了MCQ-specific limitation：MCQ的discrete 4-choice format可能artificially inflate η_max signal（错误是categorical → vulnerability更binary → η_max更predictive）， 而open-ended scoring的continuous nature dilutes this。 对论文的影响：如果MT-Bench results included，需要honest caveat \\\"our findings are primarily established for MCQ evaluation and show limited transfer to open-ended settings\\\"。 如果excluded，reviewer会问why not。Either way is problematic。\\n\\n\\nOpen-ended generation benchmark引入新的complications。 MT-Bench使用pairwise comparison scoring（而非MCQ的discrete label），judge vulnerability profile 与MCQ setting有中等相关（r=0.52 for η_max across benchmarks）。 OLS下η_max显著7/12，但bootstrap后仅1/12——same non-independence problem。 更关键的是R²显著低于MCQ（0.15 vs 0.25），说明open-ended setting中panel composition 对vulnerability的解释力更低——可能因为open-ended scoring有更多intrinsic noise。 3种attacks（sycophancy, verbosity_bias, authority_bias）在open-ended setting的implementation 需要substantial modification，results可能不完全comparable。 总结：open-ended benchmark不rescue任何claim，反而进一步dilute statistical power。 论文有效沦为two-MCQ-benchmark + one-weak-open-ended study。\\n\"\n  },\n  {\n    \"name\": \"Partial-knowledge adversary model\",\n    \"description\": \"模拟partial-knowledge adversary：adversary知道model families但不知exact vulnerability profiles。 对比full-knowledge vs partial-knowledge vs zero-knowledge adversary下的panel vulnerability。\\n\",\n    \"results\": {\n      \"knowledge_levels\": 3,\n      \"full_knowledge_mean_asr\": 0.142,\n      \"partial_knowledge_mean_asr\": 0.128,\n      \"zero_knowledge_mean_asr\": 0.098,\n      \"partial_vs_full_ratio\": 0.9,\n      \"partial_vs_zero_ratio\": 1.31,\n      \"eta_max_sig_full\": \"3/12\",\n      \"eta_max_sig_partial\": \"2/12\",\n      \"eta_max_sig_zero\": \"1/12\",\n      \"keff_sig_any_level\": \"0/12\",\n      \"family_knowledge_value\": \"moderate\",\n      \"knowledge_gradient_p\": 0.04\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Adversary knowledge level × panel vulnerability\",\n        \"columns\": [\n          \"Knowledge level\",\n          \"Mean ASR\",\n          \"η_max bootstrap sig\",\n          \"K_eff bootstrap sig\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"Full (oracle)\",\n            \"0.142\",\n            \"3/12\",\n            \"0/12\",\n            \"0.25\"\n          ],\n          [\n            \"Partial (family only)\",\n            \"0.128\",\n            \"2/12\",\n            \"0/12\",\n            \"0.18\"\n          ],\n          [\n            \"Zero (random targeting)\",\n            \"0.098\",\n            \"1/12\",\n            \"0/12\",\n            \"0.08\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Knowledge value decomposition\",\n        \"columns\": [\n          \"Comparison\",\n          \"Δ ASR\",\n          \"p\",\n          \"Practical interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Full vs zero\",\n            \"+0.044\",\n            \"0.002\",\n            \"Knowledge matters (44pp higher)\"\n          ],\n          [\n            \"Full vs partial\",\n            \"+0.014\",\n            \"0.18\",\n            \"Exact profile adds little over family\"\n          ],\n          [\n            \"Partial vs zero\",\n            \"+0.030\",\n            \"0.01\",\n            \"Family knowledge has moderate value\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Partial-knowledge analysis是lowest-impact experiment in worst档。 它confirm两个already-known facts（family labels unreliable, adversary knowledge matters） without adding new insight。在page-limited paper (8 pages)中可以完全省略或放入appendix。 唯一minor value：knowledge gradient validates that our \\\"adaptive adversary\\\" threat model is not unrealistic（even partial knowledge gives advantage），但这is a setup assumption validation, not a contribution。\\n\\nPartial-knowledge adversary结果在worst档下mostly inconclusive。 Full→partial→zero knowledge确实形成ASR gradient（0.142→0.128→0.098, p=0.04）， 说明adversary knowledge matters。但family knowledge（partial level）只提供10% advantage over full knowledge （partial/full = 0.90）——因为family labels不predict vulnerability well（Claim 4已确认, p=0.179）。 η_max significance在任何knowledge level下都barely survives bootstrap（最好3/12 for full-knowledge）， K_eff在所有levels都0/12。Partial-knowledge分析adds little to the paper—— 它confirm了family labels unreliability（already known）but doesn't provide new insight。 在worst档下这个experiment消耗GPU budget但return minimal novelty。\\n\"\n  }\n]",
      "numLines": 1568,
      "startLine": 1,
      "totalLines": 1568
    }
  },
  "sourceToolAssistantUUID": "51b538ef-1ac3-4f69-bdd5-2dba5d5c4520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "a781c0ab-5940-4489-82c0-2ce634377162",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Assistant

_source line 17 · 2026-05-22T22:45:27.904Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experimental data and paper framing. This is the "worst" tier dream paper, so the narrative guidance tells me to restructure around the collapse of the original claims and pivot to methodological contributions.

Let me now read the paper-writing-norms skill since I need to write an academic paper, and also check if there's a LaTeX template available.

Actually, let me just write the paper directly. I have all the data I need. The key narrative for the worst tier:

1. η_max dominance collapses under bootstrap (11→3/12)


2. K_eff also collapses (8→1/12) 
3. VIF >7 means η_max and K_eff can't be reliably separated
4. BFT GO/NO-GO gate fails
5. GAM 6:6 split degrades with reversals
6. Bayesian K_eff direction flip disappears under correction
7. ARC benchmark almost entirely NS

So my salvage paths are: the OLS-to-bootstrap collapse as the main finding, the 15-model 455-panel dataset as a resource contribution, and the aggregation rules with R²=0.89 threshold as an independent result.

I'm targeting EMNLP Findings with an overall score around 2.5-3.0. The paper needs to reframe this as a methodological cautionary tale about non-independence in combinatorial evaluation designs, where the collapse itself becomes the headline. I'll position the dataset and aggregation gradient as secondary contributions, then start writing the LaTeX.

Writing paper structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a781c0ab-5940-4489-82c0-2ce634377162",
  "isSidechain": false,
  "requestId": "req_011CbJRD6teBT83DJLSUPv3x",
  "type": "assistant",
  "uuid": "7aa4beec-4ce3-4e30-8a43-6e64f461eb7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqKBKgUsbryYyCR2TaEHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7161,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23910,
      "output_tokens": 546,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7161,
          "output_tokens": 546,
          "cache_read_input_tokens": 23910,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 18 · 2026-05-22T22:45:27.905Z_

Now I have all the data. Let me check if the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aa4beec-4ce3-4e30-8a43-6e64f461eb7f",
  "isSidechain": false,
  "requestId": "req_011CbJRD6teBT83DJLSUPv3x",
  "type": "assistant",
  "uuid": "3e0946a0-b0b6-4d70-8621-978d4cf42f53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqKBKgUsbryYyCR2TaEHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7161,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23910,
      "output_tokens": 546,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7161,
          "output_tokens": 546,
          "cache_read_input_tokens": 23910,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 19 · 2026-05-22T22:45:30.032Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CLzDfAjmYPeAtDUUrycvyz`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e0946a0-b0b6-4d70-8621-978d4cf42f53",
  "isSidechain": false,
  "requestId": "req_011CbJRD6teBT83DJLSUPv3x",
  "type": "assistant",
  "uuid": "271c0f2b-4bce-4c12-b6ba-f47a70f81667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqKBKgUsbryYyCR2TaEHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7161,
      "cache_creation_input_tokens": 21438,
      "cache_read_input_tokens": 23910,
      "output_tokens": 546,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7161,
          "output_tokens": 546,
          "cache_read_input_tokens": 23910,
          "cache_creation_input_tokens": 21438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21438
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

_source line 20 · 2026-05-22T22:45:30.187Z_

<details><summary>↩ Tool result · `toolu_01CLzDfAjmYPeAtDUUrycvyz`</summary>

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
  "parentUuid": "271c0f2b-4bce-4c12-b6ba-f47a70f81667",
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "d72fd5ea-58aa-486e-b05f-b2764c11a48d",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "271c0f2b-4bce-4c12-b6ba-f47a70f81667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T22:45:42.293Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper. This is the "worst" tier, so I need to pivot the narrative to make the OLS→bootstrap collapse the headline finding, present it as a methodological contribution, and be honest about the limitations.

Let me structure the paper:

1. Abstract
2. Introduction - frame the problem, mention the OLS→bootstrap collapse as the key finding
3. Related Work
4. Method - describe the experimental setup
5. Experiments - cover all 10 experiments from the JSON
6. Analysis/Discussion
7. Conclusion
8. Limitations

I need to cover all experiments:


1. Scale expansion (15 models, bootstrap collapse)
2. Attack expansion (new attacks, GAM taxonomy degradation)
3. Random-fault simulation (BFT GO/NO-GO failure)
4. Capability-matched validation (within-tier analysis)
5. Two-stage panel design algorithm
6. Per-judge ASR concentration analysis
7. Diversity-capability tradeoff visualization
8. Panel size sensitivity (K=3,5,7,9)
9. VIF + multicollinearity analysis
10. Non-majority-vote aggregation
11. Open-ended generation benchmark (MT-Bench)
12. Partial-knowledge adversary model

That's 12 experiments total. I'll organize them into coherent sections covering robustness validation, methodological analysis, and adversarial scenarios.

Now I'm structuring the paper to fit the 8-page constraint—I'll use compact tables to present results across all experiments rather than lengthy prose descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d72fd5ea-58aa-486e-b05f-b2764c11a48d",
  "isSidechain": false,
  "requestId": "req_011CbJREh3zbE3N5Njf5gqMF",
  "type": "assistant",
  "uuid": "52d78cf0-d550-4a59-b3b2-9ae253488bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCJEf9Wco4XMc7yMt5xABJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 45348,
      "output_tokens": 10016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10016,
          "cache_read_input_tokens": 45348,
          "cache_creation_input_tokens": 7736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7736
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

_source line 22 · 2026-05-22T22:45:42.299Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52d78cf0-d550-4a59-b3b2-9ae253488bcd",
  "isSidechain": false,
  "requestId": "req_011CbJREh3zbE3N5Njf5gqMF",
  "type": "assistant",
  "uuid": "0f4a22e5-f669-4194-8981-354772bba37e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCJEf9Wco4XMc7yMt5xABJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 45348,
      "output_tokens": 10016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10016,
          "cache_read_input_tokens": 45348,
          "cache_creation_input_tokens": 7736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7736
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

_source line 23 · 2026-05-22T22:48:37.252Z_

<details open><summary>🔧 Tool call — Write · `toolu_013jw4Fc7t7hv4AYhLaq1FNP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{The Mirage of Significance: How Non-Independence Inflates \\\\Predictor Effects in Combinatorial LLM Evaluation Panels}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are increasingly adopted to improve reliability, yet their vulnerability to adversarial manipulation remains poorly understood. We conduct a large-scale study decomposing panel vulnerability into individual judge weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\text{eff}}$) across 15 models, 455 panels, 9 attack types, and 3 benchmarks. Our central finding is \\emph{methodological}: standard OLS regression dramatically overstates predictor significance due to structural non-independence among combinatorial panels---each of 15 models appears in 91 of 455 panels. Under wild cluster bootstrap correction, $\\eta_{\\max}$ significance drops from 11/12 to 3/12 conditions, and $K_{\\text{eff}}$ from 8/12 to 1/12, with SE inflation of $3.2\\times$. This collapse scales with panel size: at $K{=}9$, SE inflation reaches $7.2\\times$ and $\\eta_{\\max}$ significance falls to 1/12. We further show that multicollinearity (VIF $>$ 7) prevents reliable separation of $\\eta_{\\max}$ and $K_{\\text{eff}}$, and that a BFT-inspired random-fault contrast fails its GO/NO-GO gate. Two findings survive correction: (1) aggregation rule choice fundamentally modulates vulnerability predictability (threshold $R^2{=}0.89$ vs.\\ Bayesian $R^2{=}0.10$), and (2) selecting minimum-$\\eta_{\\max}$ panels wins 9/12 conditions regardless of correction method. We release a 15-model, 455-panel adversarial evaluation dataset and provide a non-independence correction framework for combinatorial evaluation designs.\n\\end{abstract}\n\n\\section{Introduction}\n\nMulti-judge evaluation panels---where multiple LLMs independently assess candidate outputs and their judgments are aggregated---have emerged as a practical approach to improving evaluation reliability. An implicit assumption in this paradigm is that \\emph{diversity} among judges provides robustness, analogous to Byzantine Fault Tolerance (BFT) in distributed systems: uncorrelated judges should resist correlated failures.\n\nWe set out to test this assumption at scale by decomposing panel vulnerability under adversarial attack into two components: (1) the individual vulnerability of the weakest judge ($\\eta_{\\max}$), and (2) the effective number of independent judgment dimensions ($K_{\\text{eff}}$, derived from eigenvalue decomposition of inter-judge mutual information matrices). Our study covers 15 models spanning 6 families and 3 capability tiers, $\\binom{15}{3} = 455$ three-judge panels, 9 attack types, and 3 benchmarks (MMLU, ARC, MT-Bench).\n\nThe headline result is \\emph{not} what we expected to find. Under standard OLS regression, $\\eta_{\\max}$ appears significant in 11/12 conditions and $K_{\\text{eff}}$ in 8/12---suggesting that individual weakness dominates but diversity also matters. However, the 455 panels are structurally non-independent: each model participates in $\\binom{14}{2} = 91$ panels. When we apply wild cluster bootstrap ($B{=}9999$, Rademacher weights, 3-position max-$p$), $\\eta_{\\max}$ significance collapses to 3/12 and $K_{\\text{eff}}$ to 1/12. Standard errors inflate by $3.2\\times$, and this inflation \\emph{worsens} with panel size (reaching $7.2\\times$ at $K{=}9$).\n\nThis OLS-to-bootstrap collapse is itself a finding of general interest. Combinatorial panel designs---evaluating all $\\binom{N}{K}$ subsets of $N$ available models---are a natural experimental paradigm for studying panel composition effects, but the resulting non-independence is structural and severe. We demonstrate that neither $\\eta_{\\max}$ nor $K_{\\text{eff}}$ can be reliably established as independent predictors under corrected inference, and that a VIF analysis (VIF $> 7$ for both predictors) confirms they share 67\\% of their explained variance.\n\nTwo findings are robust to correction. First, the aggregation rule gradient---threshold voting yields $R^2{=}0.89$ while Bayesian calibration yields $R^2{=}0.10$---is a descriptive statistic unaffected by SE correction. Second, the practical recommendation to select minimum-$\\eta_{\\max}$ panels holds in 9/12 conditions under direct comparison, as panel ranking does not depend on regression significance.\n\nOur contributions are: (1) a methodological framework for diagnosing and correcting non-independence in combinatorial evaluation designs; (2) empirical demonstration that OLS significance is inflated by $3.2$--$7.2\\times$ in such designs; (3) a 15-model, 455-panel adversarial evaluation dataset across 9 attack types; and (4) practical guidance on aggregation rule selection and panel composition.\n\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} Using LLMs as evaluators has become standard practice, with single-judge and multi-judge configurations studied extensively. Panel-based evaluation has been proposed to mitigate individual judge biases, but systematic analysis of panel vulnerability under adversarial conditions remains limited.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work has demonstrated that LLM judges are susceptible to prompt injection, sycophancy manipulation, and position bias exploitation. These studies focus on individual judges rather than panel-level vulnerability.\n\n\\paragraph{Byzantine Fault Tolerance.} BFT provides a theoretical framework for reasoning about panel robustness: a system of $n$ nodes tolerates $f < n/3$ arbitrary (Byzantine) faults. This analogy has been informally invoked in the LLM evaluation literature but never empirically tested.\n\n\\paragraph{Non-Independence in Panel Data.} Clustered standard errors and bootstrap methods for panel data with cross-sectional dependence are well-established in econometrics. However, their application to combinatorial experimental designs in NLP---where observations are constructed from overlapping subsets of a fixed pool---has received little attention.\n\n\n\\section{Method}\n\n\\subsection{Experimental Design}\n\n\\paragraph{Model Pool.} We use 15 LLMs spanning 6 families (OpenAI, Anthropic, Google, Meta, Qwen, Mistral) and 3 capability tiers: frontier (3 models), strong (3 models), and mid-weak (9 models).\n\n\\paragraph{Panel Construction.} For panel size $K{=}3$, we enumerate all $\\binom{15}{3} = 455$ panels. For sensitivity analysis, we also examine $K \\in \\{5, 7, 9\\}$, yielding 3{,}003 to 6{,}435 panels.\n\n\\paragraph{Attack Types.} We implement 9 adversarial attacks in two categories:\n\\begin{itemize}[nosep]\n    \\item \\textbf{Targeted} (exploit judge-specific weaknesses): prompt injection, score manipulation, position bias, few-shot hijacking, persona manipulation\n    \\item \\textbf{Shared-bias} (exploit common cognitive biases): sycophancy, verbosity bias, authority bias, instruction override\n\\end{itemize}\n\n\\paragraph{Benchmarks.} MMLU (4-choice MCQ), ARC (multiple-choice), and MT-Bench (open-ended pairwise comparison).\n\n\\paragraph{Vulnerability Metric.} For each panel $\\times$ attack condition, we measure the \\emph{attack success rate} (ASR): the fraction of evaluation instances where the adversarial manipulation changes the panel's aggregated judgment.\n\n\\subsection{Predictor Variables}\n\n\\paragraph{Individual Weakness ($\\eta_{\\max}$).} The maximum individual ASR among the $K$ judges in a panel, representing the vulnerability of the weakest link.\n\n\\paragraph{Effective Diversity ($K_{\\text{eff}}$).} Derived from eigenvalue decomposition of the inter-judge mutual information (MI) matrix. $K_{\\text{eff}}$ captures the effective number of independent judgment dimensions, ranging from 1 (all judges identical) to $K$ (fully independent).\n\n\\paragraph{Regression Specification.} We use a log-log OLS specification:\n\\begin{equation}\n    \\log(\\text{ASR} + \\epsilon) = \\beta_0 + \\beta_1 \\log(\\eta_{\\max} + \\epsilon) + \\beta_2 \\log(K_{\\text{eff}}) + \\varepsilon\n\\end{equation}\n\n\\subsection{Non-Independence Correction Methods}\n\nThe $\\binom{N}{K}$ combinatorial design creates severe non-independence: each model appears in $\\binom{N-1}{K-1}$ panels. We apply four correction methods:\n\n\\begin{enumerate}[nosep]\n    \\item \\textbf{OLS} (naive baseline): assumes independent observations.\n    \\item \\textbf{Clustered SE} (CR1): clusters on judge identity (15 clusters).\n    \\item \\textbf{Mixed effects}: random intercepts for each judge.\n    \\item \\textbf{Wild cluster bootstrap v2}: $B{=}9999$ replications, Rademacher weights, max-$p$ across 3 cluster positions. Most conservative.\n\\end{enumerate}\n\n\n\\section{Experiments and Results}\n\n\\subsection{Scale Expansion and Significance Collapse}\n\\label{sec:scale}\n\nTable~\\ref{tab:ols_vs_correction} presents our central result. Under OLS, $\\eta_{\\max}$ appears significant in 11/12 conditions and $K_{\\text{eff}}$ in 8/12 (7 positive, 1 negative), suggesting a clear dominance pattern. However, all three correction methods substantially reduce significance counts.\n\n\\begin{table}[h]\n\\centering\n\\caption{OLS vs.\\ correction methods: significance counts across 12 conditions (MMLU $\\times$ 6 attacks + ARC $\\times$ 6 attacks, $p < 0.05$).}\n\\label{tab:ols_vs_correction}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & $\\eta_{\\max}$ sig & $K_{\\text{eff}}$ sig & $K_{\\text{eff}}$ +/-- & Dom.\\ ratio \\\\\n\\midrule\nOLS (naive) & 11/12 & 8/12 & 7/1 & 1.4:1 \\\\\nClustered SE (CR1) & 5/12 & 0/12 & --- & $\\infty$ \\\\\nMixed effects & 4/12 & 1/12 & 1/0 & 4:1 \\\\\nWild cluster bootstrap v2 & 3/12 & 1/12 & 1/0 & 3:1 \\\\\n\\midrule\nSE inflation factor & \\multicolumn{4}{c}{$3.2\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bootstrap is the most conservative method: $\\eta_{\\max}$ retains significance in only 3/12 conditions, all on MMLU (2/6 MMLU, 1/6 ARC). $K_{\\text{eff}}$ survives in only 1/12. The dominance ratio ($\\eta_{\\max}$:$K_{\\text{eff}}$ significant conditions) actually \\emph{increases} from 1.4:1 (OLS) to 3:1 (bootstrap)---but both predictors are near floor.\n\nTable~\\ref{tab:per_condition} shows per-condition detail. The most striking case is ARC $\\times$ prompt injection: OLS $p = 3 \\times 10^{-14}$ collapses to bootstrap $p = 0.35$, indicating that the OLS signal was almost entirely an artifact of panel overlap.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-condition bootstrap results (selected conditions).}\n\\label{tab:per_condition}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nDataset & Attack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ \\\\\n\\midrule\nMMLU & prompt\\_inj & 2e-6 & 0.028 & 0.004 & 0.18 \\\\\nMMLU & score\\_manip & 8e-5 & 0.041 & 0.011 & 0.31 \\\\\nMMLU & position\\_bias & 0.001 & 0.08 & 0.035 & 0.04 \\\\\nARC & prompt\\_inj & 3e-14 & 0.35 & 0.001 & 0.62 \\\\\nARC & score\\_manip & 1e-8 & 0.06 & 0.003 & 0.44 \\\\\nARC & sycophancy & 0.013 & 0.52 & 0.24 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBootstrap significance varies by cluster position: position 0 (most imbalanced, 91:1 panel ratio) yields 2/12, while positions 1 and 2 yield 5/12 and 4/12 respectively. The 3-position max-$p$ (3/12) is conservative but legitimate.\n\n\\subsection{Attack Expansion}\n\\label{sec:attack_expansion}\n\nWe extend to 9 attack types (adding few-shot hijacking, persona manipulation, instruction override), creating 18 total conditions. The pattern is consistent: OLS significance (16/18 $\\eta_{\\max}$, 11/18 $K_{\\text{eff}}$) collapses under bootstrap (4/18 and 1/18 respectively), confirming that the non-independence problem is structural.\n\n\\begin{table}[h]\n\\centering\n\\caption{New attack types: OLS vs.\\ bootstrap correction (6 conditions).}\n\\label{tab:new_attacks}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nDataset & Attack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ \\\\\n\\midrule\nMMLU & few-shot-hijack & 0.001 & 0.18 & 0.02 & 0.41 \\\\\nMMLU & persona-manip & 0.003 & 0.09 & 0.04 & 0.52 \\\\\nMMLU & instr-override & 5e-4 & 0.04 & 0.08 & 0.38 \\\\\nARC & few-shot-hijack & 0.008 & 0.31 & 0.05 & 0.55 \\\\\nARC & persona-manip & 0.012 & 0.22 & 0.09 & 0.63 \\\\\nARC & instr-override & 0.002 & 0.12 & 0.11 & 0.48 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe attack expansion also degrades the GAM-based attack taxonomy. The original 6-attack, 6:6 targeted/shared-bias split (all targeted showing positive $K_{\\text{eff}}$, all shared-bias showing negative) develops 3 reversals at 9 attacks (Table~\\ref{tab:gam_taxonomy}). Position bias reverses direction on ARC, and verbosity bias reverses on MMLU. The taxonomy retains a directional tendency ($\\sim$60--70\\% agreement) but is no longer clean.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended GAM taxonomy: $K_{\\text{eff}}$ direction across 9 attacks $\\times$ 2 benchmarks.}\n\\label{tab:gam_taxonomy}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nAttack & Category & $K_{\\text{eff}}$ dir (MMLU) & $K_{\\text{eff}}$ dir (ARC) & Consistent? \\\\\n\\midrule\nprompt\\_injection & targeted & + & + & yes \\\\\nscore\\_manipulation & targeted & + & + & yes \\\\\nposition\\_bias & targeted & + & -- & \\textbf{REVERSAL} \\\\\nfew-shot-hijacking & targeted & + & + & weak \\\\\npersona-manipulation & targeted & + & + & weak \\\\\nsycophancy & shared-bias & -- & -- & yes \\\\\nverbosity\\_bias & shared-bias & -- & + & \\textbf{REVERSAL} \\\\\nauthority\\_bias & shared-bias & -- & -- & yes \\\\\ninstruction-override & shared-bias & -- & -- & yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{BFT Random-Fault Contrast}\n\\label{sec:bft}\n\nWe test whether $K_{\\text{eff}}$ differentiates random faults from adaptive attacks---the core BFT-inspired hypothesis. Under random faults (each judge fails independently with probability $\\eta_j$, majority vote), $K_{\\text{eff}}$ achieves higher $R^2$ (0.52 vs.\\ 0.25 for adaptive) but collapses under bootstrap correction (0/2 significant). The GO/NO-GO gate fails on all criteria (Table~\\ref{tab:bft_contrast}).\n\n\\begin{table}[h]\n\\centering\n\\caption{BFT contrast: effect size analysis. All metrics fail their thresholds.}\n\\label{tab:bft_contrast}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Value & Threshold & Verdict \\\\\n\\midrule\n$K_{\\text{eff}}$ $\\beta$ ratio (RF/adaptive) & 1.2 & $>2.0$ & FAIL \\\\\nCohen's $d$ (paired) & 0.12 & $>0.2$ & FAIL \\\\\nContrast $p$-value & 0.31 & $<0.05$ & FAIL \\\\\n$R^2$ gap (RF -- adaptive) & 0.27 & $>0.3$ & MARGINAL \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe failure is not because BFT theory is wrong, but because corrected inference cannot reliably isolate $K_{\\text{eff}}$'s independent contribution in either regime. With only 15 model clusters and VIF $> 7$, the regression framework is fundamentally underpowered for predictor-level decomposition.\n\n\\subsection{Capability-Matched Validation}\n\\label{sec:capability}\n\nWithin-tier analysis (3 frontier, 3 strong, 9 mid-weak models) reveals that $\\eta_{\\max}$ dominance is contingent on cross-tier panel composition. When panels are restricted to capability-matched models, $\\eta_{\\max}$ range compresses by 75\\% and significance drops dramatically (Table~\\ref{tab:within_tier}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Within-tier vs.\\ cross-tier regression significance.}\n\\label{tab:within_tier}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nScope & $N$ panels & $\\eta_{\\max}$ sig & $K_{\\text{eff}}$ sig & $\\eta_{\\max}$ IQR \\\\\n\\midrule\nFrontier (3 models) & 1 & 0/12 & 0/12 & 0.02 \\\\\nStrong (3 models) & 1 & 0/12 & 0/12 & 0.04 \\\\\nMid-weak (9 models) & 84 & 3/12 & 0/12 & 0.11 \\\\\nCross-tier (15 models) & 455 & 11/12 & 8/12 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis demonstrates that $\\eta_{\\max}$ significance in the full pool reflects capability tier spread rather than a general weakest-link principle. When panels contain models of similar capability, neither predictor is informative.\n\n\\subsection{VIF and Multicollinearity Analysis}\n\\label{sec:vif}\n\nVariance inflation factor analysis confirms that $\\eta_{\\max}$ and $K_{\\text{eff}}$ cannot be reliably separated as independent predictors (Table~\\ref{tab:vif}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Multicollinearity diagnostics and variance decomposition.}\n\\label{tab:vif}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDiagnostic & $\\eta_{\\max}$ & $K_{\\text{eff}}$ & Threshold & Verdict \\\\\n\\midrule\nVIF (with tier indicators) & 7.8 & 6.9 & $>5$ & FAIL \\\\\nPartial $r$ (given other) & 0.31 & 0.12 & --- & $K_{\\text{eff}}$ weak \\\\\nUnique variance \\% & 18\\% & 3\\% & --- & $K_{\\text{eff}}$ negligible \\\\\nCondition number & 18.5 & --- & $>30$ & Moderate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nVariance decomposition reveals that 67\\% of explained variance is shared between $\\eta_{\\max}$ and $K_{\\text{eff}}$, with $\\eta_{\\max}$ contributing 18\\% unique and $K_{\\text{eff}}$ only 3\\%. Residualized $K_{\\text{eff}}$ (orthogonalized against $\\eta_{\\max}$) is significant in only 2/12 conditions. Beta regression does not improve $K_{\\text{eff}}$ status (3/12). The fundamental issue is the diversity-capability confound ($r = 0.65$): in the current model ecosystem, high-diversity panels necessarily include weaker models.\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\nNon-independence amplification scales with panel size. As $K$ increases from 3 to 9, each model's participation grows from 91 to 2{,}002 panels, and SE inflation increases from $3.2\\times$ to $7.2\\times$ (Table~\\ref{tab:panel_size}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Panel size $\\times$ correction: $\\eta_{\\max}$ and $K_{\\text{eff}}$ significance.}\n\\label{tab:panel_size}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$K$ & $N$ panels & OLS $\\eta$ sig & Boot $\\eta$ sig & SE inflation & Overlap/judge \\\\\n\\midrule\n3 & 455 & 11/12 & 3/12 & $3.2\\times$ & 91 \\\\\n5 & 3{,}003 & 11/12 & 2/12 & $4.1\\times$ & 1{,}001 \\\\\n7 & 6{,}435 & 10/12 & 1/12 & $5.8\\times$ & 3{,}003 \\\\\n9 & 5{,}005 & 9/12 & 1/12 & $7.2\\times$ & 2{,}002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$K_{\\text{eff}}$ bootstrap significance remains at 0--1/12 across all panel sizes. The practical effect size of $K_{\\text{eff}}$ also diminishes: IQR-based $\\Delta$ASR drops from 0.8pp ($K{=}3$) to 0.2pp ($K{=}9$). Larger panels theoretically reduce the weakest-link effect (one weak vote matters less in 9 than in 3), but this cannot be confirmed under corrected inference because non-independence scales faster than signal.\n\n\\subsection{Aggregation Rule Gradient}\n\\label{sec:aggregation}\n\nWhile individual predictor significance is fragile, the aggregation rule gradient is robust: it describes $R^2$ variation, a descriptive statistic unaffected by SE correction (Table~\\ref{tab:aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregation gradient: OLS vs.\\ bootstrap correction across 4 aggregation rules.}\n\\label{tab:aggregation}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nAggregation & OLS $\\eta$ & OLS $K$ & Boot $\\eta$ & Boot $K$ & $R^2$ \\\\\n\\midrule\nThreshold & 12/12 & 11/12 & 5/12 & 2/12 & 0.89 \\\\\nMajority & 11/12 & 8/12 (7+/1--) & 3/12 & 1/12 & 0.30 \\\\\nWeighted & 9/12 & 9/12 (9+/0--) & 2/12 & 1/12 & 0.28 \\\\\nBayesian & 9/12 & 7/12 (1+/6--) & 2/12 & 0/12 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $R^2$ gradient from 0.89 (threshold/unanimity) to 0.10 (Bayesian) is substantial and meaningful: aggregation rule choice determines how predictable panel vulnerability is from composition. Threshold voting maximizes the influence of individual judge weakness; Bayesian calibration minimizes it.\n\nUnder OLS, Bayesian aggregation reverses $K_{\\text{eff}}$ direction (6/7 significant coefficients negative, suggesting diversity becomes protective). However, this reversal does not survive bootstrap correction (0/12 significant), following the same pattern as all other $K_{\\text{eff}}$ findings. The direction reversal is a directional observation only.\n\n\\subsection{Panel Selection Strategies}\n\\label{sec:selection}\n\nDespite the fragility of regression-based predictor decomposition, the practical recommendation of selecting minimum-$\\eta_{\\max}$ panels is robust because it depends on panel \\emph{ranking}, not on statistical significance of regression coefficients (Table~\\ref{tab:selection}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Panel selection strategy comparison (12 conditions, $K{=}3$).}\n\\label{tab:selection}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & Win count /12 & Mean ASR & vs.\\ Random $\\Delta$ \\\\\n\\midrule\nMin $\\eta_{\\max}$ & 9/12 & 0.087 & --0.085 \\\\\nTwo-stage (ours) & 9/12 & 0.084 & --0.088 \\\\\nStrongest-$K$ & 8/12 & 0.089 & --0.083 \\\\\nMax $K_{\\text{eff}}$ & 2/12 & 0.142 & --0.030 \\\\\nMax family diversity & 1/12 & 0.155 & --0.017 \\\\\nRandom & 0/12 & 0.172 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMin-$\\eta_{\\max}$ and our two-stage algorithm (screen $\\eta \\leq$ threshold, then maximize $K_{\\text{eff}}$) tie at 9/12, with negligible ASR difference (0.003pp). The two-stage algorithm provides no marginal improvement over simply selecting the most individually robust models. This is because individual robustness ($\\eta$) and model capability are highly correlated ($r = 0.72$): selecting the most robust models $\\approx$ selecting the strongest models.\n\n\\subsection{ASR Concentration Analysis}\n\\label{sec:concentration}\n\nPer-judge ASR distribution analysis shows that adaptive adversaries produce moderately higher concentration than random faults (Gini 0.28 vs.\\ 0.19, $p = 0.04$, Cohen's $d = 0.22$). However, Gini is primarily driven by capability gap ($r = 0.55$ with $\\eta_{\\max}$) rather than adversary strategy, and the effect size is small. Targeted attacks show higher concentration than shared-bias attacks (Gini 0.35 vs.\\ 0.22), consistent with the directional taxonomy but insufficient to independently establish an adversary targeting claim.\n\n\\begin{table}[h]\n\\centering\n\\caption{ASR concentration metrics by attack category.}\n\\label{tab:concentration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nAttack category & Median Gini & Weakest-judge share & vs.\\ RF $p$ \\\\\n\\midrule\nTargeted (PI, SM, PB) & 0.35 & 0.48 & 0.02 \\\\\nShared-bias (syc, verb, auth) & 0.22 & 0.38 & 0.28 \\\\\nAll adaptive & 0.28 & 0.42 & 0.04 \\\\\nRandom-fault baseline & 0.19 & 0.36 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Open-Ended Generation Benchmark}\n\\label{sec:mtbench}\n\nMT-Bench results mirror the MCQ pattern but with lower $R^2$ (median 0.15 vs.\\ 0.25 for MMLU). Under bootstrap, $\\eta_{\\max}$ retains significance in only 1/12 conditions and $K_{\\text{eff}}$ in 0/12. Cross-benchmark consistency is moderate for $\\eta_{\\max}$ profiles ($r = 0.52$ MMLU--MT) and weak for $K_{\\text{eff}}$ ($r = 0.38$).\n\n\\begin{table}[h]\n\\centering\n\\caption{MT-Bench: OLS vs.\\ bootstrap (6 attack conditions). * indicates adapted attack implementation.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nAttack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ & $R^2$ \\\\\n\\midrule\nprompt\\_inj & 0.008 & 0.22 & 0.05 & 0.48 & 0.18 \\\\\nscore\\_manip & 0.015 & 0.31 & 0.08 & 0.55 & 0.14 \\\\\nsycophancy* & 0.042 & 0.51 & 0.12 & 0.63 & 0.11 \\\\\nverbosity* & 0.038 & 0.48 & 0.18 & 0.58 & 0.09 \\\\\nposition\\_bias & 0.003 & 0.08 & 0.04 & 0.38 & 0.22 \\\\\nauthority* & 0.055 & 0.55 & 0.22 & 0.68 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe lower $R^2$ on MT-Bench likely reflects the continuous pairwise comparison format (vs.\\ MCQ's discrete categorical judgments), which introduces more intrinsic scoring noise. Three attacks required substantial adaptation for open-ended evaluation, limiting direct comparability.\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial_knowledge}\n\nWe simulate three adversary knowledge levels: full (oracle), partial (family labels only), and zero (random targeting). An ASR gradient exists ($0.142 \\to 0.128 \\to 0.098$, $p = 0.04$), confirming that adversary knowledge matters. Family knowledge provides moderate value ($\\Delta$ASR $= 0.030$, $p = 0.01$) over zero knowledge, but exact vulnerability profiles add little beyond family information ($\\Delta = 0.014$, $p = 0.18$). Neither $\\eta_{\\max}$ nor $K_{\\text{eff}}$ significance improves at any knowledge level.\n\n\\begin{table}[h]\n\\centering\n\\caption{Adversary knowledge level vs.\\ panel vulnerability.}\n\\label{tab:partial_knowledge}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nKnowledge & Mean ASR & Boot $\\eta$ sig & Boot $K$ sig & $R^2$ \\\\\n\\midrule\nFull (oracle) & 0.142 & 3/12 & 0/12 & 0.25 \\\\\nPartial (family) & 0.128 & 2/12 & 0/12 & 0.18 \\\\\nZero (random) & 0.098 & 1/12 & 0/12 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Discussion}\n\n\\paragraph{The Non-Independence Problem Is Structural.} Our results demonstrate that combinatorial panel designs create a fundamental tension: exhaustive enumeration maximizes statistical coverage but introduces severe non-independence. Each of $N$ models appears in $\\binom{N-1}{K-1}$ panels, creating cross-observation correlation that inflates standard errors by $3.2$--$7.2\\times$ depending on $K$. This is not a correctable nuisance---it is an intrinsic property of the experimental design.\n\n\\paragraph{Neither Predictor Is Reliably Established.} Under corrected inference, $\\eta_{\\max}$ retains significance in only 3/12 conditions (bootstrap) and $K_{\\text{eff}}$ in 1/12. The VIF analysis ($>7$ for both) confirms that 67\\% of explained variance is shared, with $K_{\\text{eff}}$ contributing only 3\\% unique variance. The regression-based decomposition framework is fundamentally inadequate for isolating independent predictor effects with 15 model clusters.\n\n\\paragraph{What Survives.} Two findings are robust. First, the aggregation $R^2$ gradient (0.89 to 0.10) is descriptive and independent of inference correction---it characterizes how much panel composition matters under different voting rules. Second, minimum-$\\eta_{\\max}$ selection dominates alternative strategies in 9/12 conditions, a result based on direct comparison rather than regression significance.\n\n\\paragraph{The Diversity-Capability Confound.} The correlation between $\\eta_{\\max}$ and $K_{\\text{eff}}$ ($r = 0.65$, $R^2 = 0.42$) is primarily driven by cross-tier differences ($r = 0.72$ for cross-tier panels vs.\\ $r = 0.22$--$0.35$ within-tier). In the current LLM ecosystem, capability predicts robustness: high-diversity panels necessarily include weaker models. This confound is not an artifact of our analysis but a structural feature of the model landscape.\n\n\\paragraph{Implications for Evaluation Practice.} Our results suggest three practical takeaways: (1) prioritize individual judge quality over panel diversity; (2) choose aggregation rules deliberately---Bayesian calibration reduces composition sensitivity while threshold voting amplifies it; (3) be cautious about regression-based conclusions from combinatorial panel designs without non-independence correction.\n\n\n\\section{Conclusion}\n\nWe conducted a large-scale study of LLM evaluation panel vulnerability, finding that standard OLS regression dramatically overstates predictor significance in combinatorial panel designs due to structural non-independence. Under wild cluster bootstrap correction, $\\eta_{\\max}$ significance drops from 11/12 to 3/12 and $K_{\\text{eff}}$ from 8/12 to 1/12, with SE inflation of $3.2\\times$. This collapse is itself a methodological contribution: it provides a concrete demonstration of why non-independence correction is essential for combinatorial evaluation research.\n\nTwo findings survive: aggregation rule choice modulates vulnerability predictability ($R^2$ from 0.89 to 0.10), and minimum-$\\eta_{\\max}$ panel selection outperforms alternatives in 9/12 conditions. We release a 15-model, 455-panel adversarial evaluation dataset as a resource for future work.\n\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, with 15 models and therefore 15 clusters, bootstrap correction is conservative and may be overly so---the true significance of $\\eta_{\\max}$ likely lies between the OLS upper bound (11/12) and the bootstrap lower bound (3/12). Studies with larger model pools ($N \\geq 30$) would provide more reliable corrected inference. Second, our findings are primarily established on MCQ benchmarks (MMLU, ARC); MT-Bench results show limited transfer, suggesting that the vulnerability dynamics may be format-dependent. Third, the diversity-capability confound ($r = 0.65$) is a property of the current model ecosystem and may change as the landscape evolves.\n\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f4a22e5-f669-4194-8981-354772bba37e",
  "isSidechain": false,
  "requestId": "req_011CbJREh3zbE3N5Njf5gqMF",
  "type": "assistant",
  "uuid": "12cdd3f3-86df-4811-9bd8-d32ef3900b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCJEf9Wco4XMc7yMt5xABJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 45348,
      "output_tokens": 10016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10016,
          "cache_read_input_tokens": 45348,
          "cache_creation_input_tokens": 7736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7736
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

_source line 24 · 2026-05-22T22:48:37.272Z_

<details><summary>↩ Tool result · `toolu_013jw4Fc7t7hv4AYhLaq1FNP`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12cdd3f3-86df-4811-9bd8-d32ef3900b8d",
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "dc8c47b9-db9e-4c90-b6a3-ecc0cb01d889",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{adjustbox}\n\n\\title{The Mirage of Significance: How Non-Independence Inflates \\\\Predictor Effects in Combinatorial LLM Evaluation Panels}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are increasingly adopted to improve reliability, yet their vulnerability to adversarial manipulation remains poorly understood. We conduct a large-scale study decomposing panel vulnerability into individual judge weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\text{eff}}$) across 15 models, 455 panels, 9 attack types, and 3 benchmarks. Our central finding is \\emph{methodological}: standard OLS regression dramatically overstates predictor significance due to structural non-independence among combinatorial panels---each of 15 models appears in 91 of 455 panels. Under wild cluster bootstrap correction, $\\eta_{\\max}$ significance drops from 11/12 to 3/12 conditions, and $K_{\\text{eff}}$ from 8/12 to 1/12, with SE inflation of $3.2\\times$. This collapse scales with panel size: at $K{=}9$, SE inflation reaches $7.2\\times$ and $\\eta_{\\max}$ significance falls to 1/12. We further show that multicollinearity (VIF $>$ 7) prevents reliable separation of $\\eta_{\\max}$ and $K_{\\text{eff}}$, and that a BFT-inspired random-fault contrast fails its GO/NO-GO gate. Two findings survive correction: (1) aggregation rule choice fundamentally modulates vulnerability predictability (threshold $R^2{=}0.89$ vs.\\ Bayesian $R^2{=}0.10$), and (2) selecting minimum-$\\eta_{\\max}$ panels wins 9/12 conditions regardless of correction method. We release a 15-model, 455-panel adversarial evaluation dataset and provide a non-independence correction framework for combinatorial evaluation designs.\n\\end{abstract}\n\n\\section{Introduction}\n\nMulti-judge evaluation panels---where multiple LLMs independently assess candidate outputs and their judgments are aggregated---have emerged as a practical approach to improving evaluation reliability. An implicit assumption in this paradigm is that \\emph{diversity} among judges provides robustness, analogous to Byzantine Fault Tolerance (BFT) in distributed systems: uncorrelated judges should resist correlated failures.\n\nWe set out to test this assumption at scale by decomposing panel vulnerability under adversarial attack into two components: (1) the individual vulnerability of the weakest judge ($\\eta_{\\max}$), and (2) the effective number of independent judgment dimensions ($K_{\\text{eff}}$, derived from eigenvalue decomposition of inter-judge mutual information matrices). Our study covers 15 models spanning 6 families and 3 capability tiers, $\\binom{15}{3} = 455$ three-judge panels, 9 attack types, and 3 benchmarks (MMLU, ARC, MT-Bench).\n\nThe headline result is \\emph{not} what we expected to find. Under standard OLS regression, $\\eta_{\\max}$ appears significant in 11/12 conditions and $K_{\\text{eff}}$ in 8/12---suggesting that individual weakness dominates but diversity also matters. However, the 455 panels are structurally non-independent: each model participates in $\\binom{14}{2} = 91$ panels. When we apply wild cluster bootstrap ($B{=}9999$, Rademacher weights, 3-position max-$p$), $\\eta_{\\max}$ significance collapses to 3/12 and $K_{\\text{eff}}$ to 1/12. Standard errors inflate by $3.2\\times$, and this inflation \\emph{worsens} with panel size (reaching $7.2\\times$ at $K{=}9$).\n\nThis OLS-to-bootstrap collapse is itself a finding of general interest. Combinatorial panel designs---evaluating all $\\binom{N}{K}$ subsets of $N$ available models---are a natural experimental paradigm for studying panel composition effects, but the resulting non-independence is structural and severe. We demonstrate that neither $\\eta_{\\max}$ nor $K_{\\text{eff}}$ can be reliably established as independent predictors under corrected inference, and that a VIF analysis (VIF $> 7$ for both predictors) confirms they share 67\\% of their explained variance.\n\nTwo findings are robust to correction. First, the aggregation rule gradient---threshold voting yields $R^2{=}0.89$ while Bayesian calibration yields $R^2{=}0.10$---is a descriptive statistic unaffected by SE correction. Second, the practical recommendation to select minimum-$\\eta_{\\max}$ panels holds in 9/12 conditions under direct comparison, as panel ranking does not depend on regression significance.\n\nOur contributions are: (1) a methodological framework for diagnosing and correcting non-independence in combinatorial evaluation designs; (2) empirical demonstration that OLS significance is inflated by $3.2$--$7.2\\times$ in such designs; (3) a 15-model, 455-panel adversarial evaluation dataset across 9 attack types; and (4) practical guidance on aggregation rule selection and panel composition.\n\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} Using LLMs as evaluators has become standard practice, with single-judge and multi-judge configurations studied extensively. Panel-based evaluation has been proposed to mitigate individual judge biases, but systematic analysis of panel vulnerability under adversarial conditions remains limited.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work has demonstrated that LLM judges are susceptible to prompt injection, sycophancy manipulation, and position bias exploitation. These studies focus on individual judges rather than panel-level vulnerability.\n\n\\paragraph{Byzantine Fault Tolerance.} BFT provides a theoretical framework for reasoning about panel robustness: a system of $n$ nodes tolerates $f < n/3$ arbitrary (Byzantine) faults. This analogy has been informally invoked in the LLM evaluation literature but never empirically tested.\n\n\\paragraph{Non-Independence in Panel Data.} Clustered standard errors and bootstrap methods for panel data with cross-sectional dependence are well-established in econometrics. However, their application to combinatorial experimental designs in NLP---where observations are constructed from overlapping subsets of a fixed pool---has received little attention.\n\n\n\\section{Method}\n\n\\subsection{Experimental Design}\n\n\\paragraph{Model Pool.} We use 15 LLMs spanning 6 families (OpenAI, Anthropic, Google, Meta, Qwen, Mistral) and 3 capability tiers: frontier (3 models), strong (3 models), and mid-weak (9 models).\n\n\\paragraph{Panel Construction.} For panel size $K{=}3$, we enumerate all $\\binom{15}{3} = 455$ panels. For sensitivity analysis, we also examine $K \\in \\{5, 7, 9\\}$, yielding 3{,}003 to 6{,}435 panels.\n\n\\paragraph{Attack Types.} We implement 9 adversarial attacks in two categories:\n\\begin{itemize}[nosep]\n    \\item \\textbf{Targeted} (exploit judge-specific weaknesses): prompt injection, score manipulation, position bias, few-shot hijacking, persona manipulation\n    \\item \\textbf{Shared-bias} (exploit common cognitive biases): sycophancy, verbosity bias, authority bias, instruction override\n\\end{itemize}\n\n\\paragraph{Benchmarks.} MMLU (4-choice MCQ), ARC (multiple-choice), and MT-Bench (open-ended pairwise comparison).\n\n\\paragraph{Vulnerability Metric.} For each panel $\\times$ attack condition, we measure the \\emph{attack success rate} (ASR): the fraction of evaluation instances where the adversarial manipulation changes the panel's aggregated judgment.\n\n\\subsection{Predictor Variables}\n\n\\paragraph{Individual Weakness ($\\eta_{\\max}$).} The maximum individual ASR among the $K$ judges in a panel, representing the vulnerability of the weakest link.\n\n\\paragraph{Effective Diversity ($K_{\\text{eff}}$).} Derived from eigenvalue decomposition of the inter-judge mutual information (MI) matrix. $K_{\\text{eff}}$ captures the effective number of independent judgment dimensions, ranging from 1 (all judges identical) to $K$ (fully independent).\n\n\\paragraph{Regression Specification.} We use a log-log OLS specification:\n\\begin{equation}\n    \\log(\\text{ASR} + \\epsilon) = \\beta_0 + \\beta_1 \\log(\\eta_{\\max} + \\epsilon) + \\beta_2 \\log(K_{\\text{eff}}) + \\varepsilon\n\\end{equation}\n\n\\subsection{Non-Independence Correction Methods}\n\nThe $\\binom{N}{K}$ combinatorial design creates severe non-independence: each model appears in $\\binom{N-1}{K-1}$ panels. We apply four correction methods:\n\n\\begin{enumerate}[nosep]\n    \\item \\textbf{OLS} (naive baseline): assumes independent observations.\n    \\item \\textbf{Clustered SE} (CR1): clusters on judge identity (15 clusters).\n    \\item \\textbf{Mixed effects}: random intercepts for each judge.\n    \\item \\textbf{Wild cluster bootstrap v2}: $B{=}9999$ replications, Rademacher weights, max-$p$ across 3 cluster positions. Most conservative.\n\\end{enumerate}\n\n\n\\section{Experiments and Results}\n\n\\subsection{Scale Expansion and Significance Collapse}\n\\label{sec:scale}\n\nTable~\\ref{tab:ols_vs_correction} presents our central result. Under OLS, $\\eta_{\\max}$ appears significant in 11/12 conditions and $K_{\\text{eff}}$ in 8/12 (7 positive, 1 negative), suggesting a clear dominance pattern. However, all three correction methods substantially reduce significance counts.\n\n\\begin{table}[h]\n\\centering\n\\caption{OLS vs.\\ correction methods: significance counts across 12 conditions (MMLU $\\times$ 6 attacks + ARC $\\times$ 6 attacks, $p < 0.05$).}\n\\label{tab:ols_vs_correction}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & $\\eta_{\\max}$ sig & $K_{\\text{eff}}$ sig & $K_{\\text{eff}}$ +/-- & Dom.\\ ratio \\\\\n\\midrule\nOLS (naive) & 11/12 & 8/12 & 7/1 & 1.4:1 \\\\\nClustered SE (CR1) & 5/12 & 0/12 & --- & $\\infty$ \\\\\nMixed effects & 4/12 & 1/12 & 1/0 & 4:1 \\\\\nWild cluster bootstrap v2 & 3/12 & 1/12 & 1/0 & 3:1 \\\\\n\\midrule\nSE inflation factor & \\multicolumn{4}{c}{$3.2\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bootstrap is the most conservative method: $\\eta_{\\max}$ retains significance in only 3/12 conditions, all on MMLU (2/6 MMLU, 1/6 ARC). $K_{\\text{eff}}$ survives in only 1/12. The dominance ratio ($\\eta_{\\max}$:$K_{\\text{eff}}$ significant conditions) actually \\emph{increases} from 1.4:1 (OLS) to 3:1 (bootstrap)---but both predictors are near floor.\n\nTable~\\ref{tab:per_condition} shows per-condition detail. The most striking case is ARC $\\times$ prompt injection: OLS $p = 3 \\times 10^{-14}$ collapses to bootstrap $p = 0.35$, indicating that the OLS signal was almost entirely an artifact of panel overlap.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-condition bootstrap results (selected conditions).}\n\\label{tab:per_condition}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nDataset & Attack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ \\\\\n\\midrule\nMMLU & prompt\\_inj & 2e-6 & 0.028 & 0.004 & 0.18 \\\\\nMMLU & score\\_manip & 8e-5 & 0.041 & 0.011 & 0.31 \\\\\nMMLU & position\\_bias & 0.001 & 0.08 & 0.035 & 0.04 \\\\\nARC & prompt\\_inj & 3e-14 & 0.35 & 0.001 & 0.62 \\\\\nARC & score\\_manip & 1e-8 & 0.06 & 0.003 & 0.44 \\\\\nARC & sycophancy & 0.013 & 0.52 & 0.24 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBootstrap significance varies by cluster position: position 0 (most imbalanced, 91:1 panel ratio) yields 2/12, while positions 1 and 2 yield 5/12 and 4/12 respectively. The 3-position max-$p$ (3/12) is conservative but legitimate.\n\n\\subsection{Attack Expansion}\n\\label{sec:attack_expansion}\n\nWe extend to 9 attack types (adding few-shot hijacking, persona manipulation, instruction override), creating 18 total conditions. The pattern is consistent: OLS significance (16/18 $\\eta_{\\max}$, 11/18 $K_{\\text{eff}}$) collapses under bootstrap (4/18 and 1/18 respectively), confirming that the non-independence problem is structural.\n\n\\begin{table}[h]\n\\centering\n\\caption{New attack types: OLS vs.\\ bootstrap correction (6 conditions).}\n\\label{tab:new_attacks}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nDataset & Attack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ \\\\\n\\midrule\nMMLU & few-shot-hijack & 0.001 & 0.18 & 0.02 & 0.41 \\\\\nMMLU & persona-manip & 0.003 & 0.09 & 0.04 & 0.52 \\\\\nMMLU & instr-override & 5e-4 & 0.04 & 0.08 & 0.38 \\\\\nARC & few-shot-hijack & 0.008 & 0.31 & 0.05 & 0.55 \\\\\nARC & persona-manip & 0.012 & 0.22 & 0.09 & 0.63 \\\\\nARC & instr-override & 0.002 & 0.12 & 0.11 & 0.48 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe attack expansion also degrades the GAM-based attack taxonomy. The original 6-attack, 6:6 targeted/shared-bias split (all targeted showing positive $K_{\\text{eff}}$, all shared-bias showing negative) develops 3 reversals at 9 attacks (Table~\\ref{tab:gam_taxonomy}). Position bias reverses direction on ARC, and verbosity bias reverses on MMLU. The taxonomy retains a directional tendency ($\\sim$60--70\\% agreement) but is no longer clean.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended GAM taxonomy: $K_{\\text{eff}}$ direction across 9 attacks $\\times$ 2 benchmarks.}\n\\label{tab:gam_taxonomy}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nAttack & Category & $K_{\\text{eff}}$ dir (MMLU) & $K_{\\text{eff}}$ dir (ARC) & Consistent? \\\\\n\\midrule\nprompt\\_injection & targeted & + & + & yes \\\\\nscore\\_manipulation & targeted & + & + & yes \\\\\nposition\\_bias & targeted & + & -- & \\textbf{REVERSAL} \\\\\nfew-shot-hijacking & targeted & + & + & weak \\\\\npersona-manipulation & targeted & + & + & weak \\\\\nsycophancy & shared-bias & -- & -- & yes \\\\\nverbosity\\_bias & shared-bias & -- & + & \\textbf{REVERSAL} \\\\\nauthority\\_bias & shared-bias & -- & -- & yes \\\\\ninstruction-override & shared-bias & -- & -- & yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{BFT Random-Fault Contrast}\n\\label{sec:bft}\n\nWe test whether $K_{\\text{eff}}$ differentiates random faults from adaptive attacks---the core BFT-inspired hypothesis. Under random faults (each judge fails independently with probability $\\eta_j$, majority vote), $K_{\\text{eff}}$ achieves higher $R^2$ (0.52 vs.\\ 0.25 for adaptive) but collapses under bootstrap correction (0/2 significant). The GO/NO-GO gate fails on all criteria (Table~\\ref{tab:bft_contrast}).\n\n\\begin{table}[h]\n\\centering\n\\caption{BFT contrast: effect size analysis. All metrics fail their thresholds.}\n\\label{tab:bft_contrast}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Value & Threshold & Verdict \\\\\n\\midrule\n$K_{\\text{eff}}$ $\\beta$ ratio (RF/adaptive) & 1.2 & $>2.0$ & FAIL \\\\\nCohen's $d$ (paired) & 0.12 & $>0.2$ & FAIL \\\\\nContrast $p$-value & 0.31 & $<0.05$ & FAIL \\\\\n$R^2$ gap (RF -- adaptive) & 0.27 & $>0.3$ & MARGINAL \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe failure is not because BFT theory is wrong, but because corrected inference cannot reliably isolate $K_{\\text{eff}}$'s independent contribution in either regime. With only 15 model clusters and VIF $> 7$, the regression framework is fundamentally underpowered for predictor-level decomposition.\n\n\\subsection{Capability-Matched Validation}\n\\label{sec:capability}\n\nWithin-tier analysis (3 frontier, 3 strong, 9 mid-weak models) reveals that $\\eta_{\\max}$ dominance is contingent on cross-tier panel composition. When panels are restricted to capability-matched models, $\\eta_{\\max}$ range compresses by 75\\% and significance drops dramatically (Table~\\ref{tab:within_tier}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Within-tier vs.\\ cross-tier regression significance.}\n\\label{tab:within_tier}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nScope & $N$ panels & $\\eta_{\\max}$ sig & $K_{\\text{eff}}$ sig & $\\eta_{\\max}$ IQR \\\\\n\\midrule\nFrontier (3 models) & 1 & 0/12 & 0/12 & 0.02 \\\\\nStrong (3 models) & 1 & 0/12 & 0/12 & 0.04 \\\\\nMid-weak (9 models) & 84 & 3/12 & 0/12 & 0.11 \\\\\nCross-tier (15 models) & 455 & 11/12 & 8/12 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis demonstrates that $\\eta_{\\max}$ significance in the full pool reflects capability tier spread rather than a general weakest-link principle. When panels contain models of similar capability, neither predictor is informative.\n\n\\subsection{VIF and Multicollinearity Analysis}\n\\label{sec:vif}\n\nVariance inflation factor analysis confirms that $\\eta_{\\max}$ and $K_{\\text{eff}}$ cannot be reliably separated as independent predictors (Table~\\ref{tab:vif}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Multicollinearity diagnostics and variance decomposition.}\n\\label{tab:vif}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDiagnostic & $\\eta_{\\max}$ & $K_{\\text{eff}}$ & Threshold & Verdict \\\\\n\\midrule\nVIF (with tier indicators) & 7.8 & 6.9 & $>5$ & FAIL \\\\\nPartial $r$ (given other) & 0.31 & 0.12 & --- & $K_{\\text{eff}}$ weak \\\\\nUnique variance \\% & 18\\% & 3\\% & --- & $K_{\\text{eff}}$ negligible \\\\\nCondition number & 18.5 & --- & $>30$ & Moderate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nVariance decomposition reveals that 67\\% of explained variance is shared between $\\eta_{\\max}$ and $K_{\\text{eff}}$, with $\\eta_{\\max}$ contributing 18\\% unique and $K_{\\text{eff}}$ only 3\\%. Residualized $K_{\\text{eff}}$ (orthogonalized against $\\eta_{\\max}$) is significant in only 2/12 conditions. Beta regression does not improve $K_{\\text{eff}}$ status (3/12). The fundamental issue is the diversity-capability confound ($r = 0.65$): in the current model ecosystem, high-diversity panels necessarily include weaker models.\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\nNon-independence amplification scales with panel size. As $K$ increases from 3 to 9, each model's participation grows from 91 to 2{,}002 panels, and SE inflation increases from $3.2\\times$ to $7.2\\times$ (Table~\\ref{tab:panel_size}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Panel size $\\times$ correction: $\\eta_{\\max}$ and $K_{\\text{eff}}$ significance.}\n\\label{tab:panel_size}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$K$ & $N$ panels & OLS $\\eta$ sig & Boot $\\eta$ sig & SE inflation & Overlap/judge \\\\\n\\midrule\n3 & 455 & 11/12 & 3/12 & $3.2\\times$ & 91 \\\\\n5 & 3{,}003 & 11/12 & 2/12 & $4.1\\times$ & 1{,}001 \\\\\n7 & 6{,}435 & 10/12 & 1/12 & $5.8\\times$ & 3{,}003 \\\\\n9 & 5{,}005 & 9/12 & 1/12 & $7.2\\times$ & 2{,}002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$K_{\\text{eff}}$ bootstrap significance remains at 0--1/12 across all panel sizes. The practical effect size of $K_{\\text{eff}}$ also diminishes: IQR-based $\\Delta$ASR drops from 0.8pp ($K{=}3$) to 0.2pp ($K{=}9$). Larger panels theoretically reduce the weakest-link effect (one weak vote matters less in 9 than in 3), but this cannot be confirmed under corrected inference because non-independence scales faster than signal.\n\n\\subsection{Aggregation Rule Gradient}\n\\label{sec:aggregation}\n\nWhile individual predictor significance is fragile, the aggregation rule gradient is robust: it describes $R^2$ variation, a descriptive statistic unaffected by SE correction (Table~\\ref{tab:aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregation gradient: OLS vs.\\ bootstrap correction across 4 aggregation rules.}\n\\label{tab:aggregation}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nAggregation & OLS $\\eta$ & OLS $K$ & Boot $\\eta$ & Boot $K$ & $R^2$ \\\\\n\\midrule\nThreshold & 12/12 & 11/12 & 5/12 & 2/12 & 0.89 \\\\\nMajority & 11/12 & 8/12 (7+/1--) & 3/12 & 1/12 & 0.30 \\\\\nWeighted & 9/12 & 9/12 (9+/0--) & 2/12 & 1/12 & 0.28 \\\\\nBayesian & 9/12 & 7/12 (1+/6--) & 2/12 & 0/12 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $R^2$ gradient from 0.89 (threshold/unanimity) to 0.10 (Bayesian) is substantial and meaningful: aggregation rule choice determines how predictable panel vulnerability is from composition. Threshold voting maximizes the influence of individual judge weakness; Bayesian calibration minimizes it.\n\nUnder OLS, Bayesian aggregation reverses $K_{\\text{eff}}$ direction (6/7 significant coefficients negative, suggesting diversity becomes protective). However, this reversal does not survive bootstrap correction (0/12 significant), following the same pattern as all other $K_{\\text{eff}}$ findings. The direction reversal is a directional observation only.\n\n\\subsection{Panel Selection Strategies}\n\\label{sec:selection}\n\nDespite the fragility of regression-based predictor decomposition, the practical recommendation of selecting minimum-$\\eta_{\\max}$ panels is robust because it depends on panel \\emph{ranking}, not on statistical significance of regression coefficients (Table~\\ref{tab:selection}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Panel selection strategy comparison (12 conditions, $K{=}3$).}\n\\label{tab:selection}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & Win count /12 & Mean ASR & vs.\\ Random $\\Delta$ \\\\\n\\midrule\nMin $\\eta_{\\max}$ & 9/12 & 0.087 & --0.085 \\\\\nTwo-stage (ours) & 9/12 & 0.084 & --0.088 \\\\\nStrongest-$K$ & 8/12 & 0.089 & --0.083 \\\\\nMax $K_{\\text{eff}}$ & 2/12 & 0.142 & --0.030 \\\\\nMax family diversity & 1/12 & 0.155 & --0.017 \\\\\nRandom & 0/12 & 0.172 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMin-$\\eta_{\\max}$ and our two-stage algorithm (screen $\\eta \\leq$ threshold, then maximize $K_{\\text{eff}}$) tie at 9/12, with negligible ASR difference (0.003pp). The two-stage algorithm provides no marginal improvement over simply selecting the most individually robust models. This is because individual robustness ($\\eta$) and model capability are highly correlated ($r = 0.72$): selecting the most robust models $\\approx$ selecting the strongest models.\n\n\\subsection{ASR Concentration Analysis}\n\\label{sec:concentration}\n\nPer-judge ASR distribution analysis shows that adaptive adversaries produce moderately higher concentration than random faults (Gini 0.28 vs.\\ 0.19, $p = 0.04$, Cohen's $d = 0.22$). However, Gini is primarily driven by capability gap ($r = 0.55$ with $\\eta_{\\max}$) rather than adversary strategy, and the effect size is small. Targeted attacks show higher concentration than shared-bias attacks (Gini 0.35 vs.\\ 0.22), consistent with the directional taxonomy but insufficient to independently establish an adversary targeting claim.\n\n\\begin{table}[h]\n\\centering\n\\caption{ASR concentration metrics by attack category.}\n\\label{tab:concentration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nAttack category & Median Gini & Weakest-judge share & vs.\\ RF $p$ \\\\\n\\midrule\nTargeted (PI, SM, PB) & 0.35 & 0.48 & 0.02 \\\\\nShared-bias (syc, verb, auth) & 0.22 & 0.38 & 0.28 \\\\\nAll adaptive & 0.28 & 0.42 & 0.04 \\\\\nRandom-fault baseline & 0.19 & 0.36 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Open-Ended Generation Benchmark}\n\\label{sec:mtbench}\n\nMT-Bench results mirror the MCQ pattern but with lower $R^2$ (median 0.15 vs.\\ 0.25 for MMLU). Under bootstrap, $\\eta_{\\max}$ retains significance in only 1/12 conditions and $K_{\\text{eff}}$ in 0/12. Cross-benchmark consistency is moderate for $\\eta_{\\max}$ profiles ($r = 0.52$ MMLU--MT) and weak for $K_{\\text{eff}}$ ($r = 0.38$).\n\n\\begin{table}[h]\n\\centering\n\\caption{MT-Bench: OLS vs.\\ bootstrap (6 attack conditions). * indicates adapted attack implementation.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nAttack & OLS $\\eta$ $p$ & Boot $\\eta$ $p$ & OLS $K$ $p$ & Boot $K$ $p$ & $R^2$ \\\\\n\\midrule\nprompt\\_inj & 0.008 & 0.22 & 0.05 & 0.48 & 0.18 \\\\\nscore\\_manip & 0.015 & 0.31 & 0.08 & 0.55 & 0.14 \\\\\nsycophancy* & 0.042 & 0.51 & 0.12 & 0.63 & 0.11 \\\\\nverbosity* & 0.038 & 0.48 & 0.18 & 0.58 & 0.09 \\\\\nposition\\_bias & 0.003 & 0.08 & 0.04 & 0.38 & 0.22 \\\\\nauthority* & 0.055 & 0.55 & 0.22 & 0.68 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe lower $R^2$ on MT-Bench likely reflects the continuous pairwise comparison format (vs.\\ MCQ's discrete categorical judgments), which introduces more intrinsic scoring noise. Three attacks required substantial adaptation for open-ended evaluation, limiting direct comparability.\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial_knowledge}\n\nWe simulate three adversary knowledge levels: full (oracle), partial (family labels only), and zero (random targeting). An ASR gradient exists ($0.142 \\to 0.128 \\to 0.098$, $p = 0.04$), confirming that adversary knowledge matters. Family knowledge provides moderate value ($\\Delta$ASR $= 0.030$, $p = 0.01$) over zero knowledge, but exact vulnerability profiles add little beyond family information ($\\Delta = 0.014$, $p = 0.18$). Neither $\\eta_{\\max}$ nor $K_{\\text{eff}}$ significance improves at any knowledge level.\n\n\\begin{table}[h]\n\\centering\n\\caption{Adversary knowledge level vs.\\ panel vulnerability.}\n\\label{tab:partial_knowledge}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nKnowledge & Mean ASR & Boot $\\eta$ sig & Boot $K$ sig & $R^2$ \\\\\n\\midrule\nFull (oracle) & 0.142 & 3/12 & 0/12 & 0.25 \\\\\nPartial (family) & 0.128 & 2/12 & 0/12 & 0.18 \\\\\nZero (random) & 0.098 & 1/12 & 0/12 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Discussion}\n\n\\paragraph{The Non-Independence Problem Is Structural.} Our results demonstrate that combinatorial panel designs create a fundamental tension: exhaustive enumeration maximizes statistical coverage but introduces severe non-independence. Each of $N$ models appears in $\\binom{N-1}{K-1}$ panels, creating cross-observation correlation that inflates standard errors by $3.2$--$7.2\\times$ depending on $K$. This is not a correctable nuisance---it is an intrinsic property of the experimental design.\n\n\\paragraph{Neither Predictor Is Reliably Established.} Under corrected inference, $\\eta_{\\max}$ retains significance in only 3/12 conditions (bootstrap) and $K_{\\text{eff}}$ in 1/12. The VIF analysis ($>7$ for both) confirms that 67\\% of explained variance is shared, with $K_{\\text{eff}}$ contributing only 3\\% unique variance. The regression-based decomposition framework is fundamentally inadequate for isolating independent predictor effects with 15 model clusters.\n\n\\paragraph{What Survives.} Two findings are robust. First, the aggregation $R^2$ gradient (0.89 to 0.10) is descriptive and independent of inference correction---it characterizes how much panel composition matters under different voting rules. Second, minimum-$\\eta_{\\max}$ selection dominates alternative strategies in 9/12 conditions, a result based on direct comparison rather than regression significance.\n\n\\paragraph{The Diversity-Capability Confound.} The correlation between $\\eta_{\\max}$ and $K_{\\text{eff}}$ ($r = 0.65$, $R^2 = 0.42$) is primarily driven by cross-tier differences ($r = 0.72$ for cross-tier panels vs.\\ $r = 0.22$--$0.35$ within-tier). In the current LLM ecosystem, capability predicts robustness: high-diversity panels necessarily include weaker models. This confound is not an artifact of our analysis but a structural feature of the model landscape.\n\n\\paragraph{Implications for Evaluation Practice.} Our results suggest three practical takeaways: (1) prioritize individual judge quality over panel diversity; (2) choose aggregation rules deliberately---Bayesian calibration reduces composition sensitivity while threshold voting amplifies it; (3) be cautious about regression-based conclusions from combinatorial panel designs without non-independence correction.\n\n\n\\section{Conclusion}\n\nWe conducted a large-scale study of LLM evaluation panel vulnerability, finding that standard OLS regression dramatically overstates predictor significance in combinatorial panel designs due to structural non-independence. Under wild cluster bootstrap correction, $\\eta_{\\max}$ significance drops from 11/12 to 3/12 and $K_{\\text{eff}}$ from 8/12 to 1/12, with SE inflation of $3.2\\times$. This collapse is itself a methodological contribution: it provides a concrete demonstration of why non-independence correction is essential for combinatorial evaluation research.\n\nTwo findings survive: aggregation rule choice modulates vulnerability predictability ($R^2$ from 0.89 to 0.10), and minimum-$\\eta_{\\max}$ panel selection outperforms alternatives in 9/12 conditions. We release a 15-model, 455-panel adversarial evaluation dataset as a resource for future work.\n\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, with 15 models and therefore 15 clusters, bootstrap correction is conservative and may be overly so---the true significance of $\\eta_{\\max}$ likely lies between the OLS upper bound (11/12) and the bootstrap lower bound (3/12). Studies with larger model pools ($N \\geq 30$) would provide more reliable corrected inference. Second, our findings are primarily established on MCQ benchmarks (MMLU, ARC); MT-Bench results show limited transfer, suggesting that the vulnerability dynamics may be format-dependent. Third, the diversity-capability confound ($r = 0.65$) is a property of the current model ecosystem and may change as the landscape evolves.\n\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "12cdd3f3-86df-4811-9bd8-d32ef3900b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "dc8c47b9-db9e-4c90-b6a3-ecc0cb01d889",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Assistant

_source line 27 · 2026-05-22T22:48:39.650Z_

Now compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8c47b9-db9e-4c90-b6a3-ecc0cb01d889",
  "isSidechain": false,
  "requestId": "req_011CbJRUUyMWrTnypnxwpxRN",
  "type": "assistant",
  "uuid": "757fd80d-1dff-430b-b1e6-2c097705feff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bRbM1r56koc4km2YJPys2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10081,
      "cache_read_input_tokens": 53084,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 53084,
          "cache_creation_input_tokens": 10081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10081
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

_source line 28 · 2026-05-22T22:48:41.167Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01H4kessY5Cxh3b7QSQyiJmF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "757fd80d-1dff-430b-b1e6-2c097705feff",
  "isSidechain": false,
  "requestId": "req_011CbJRUUyMWrTnypnxwpxRN",
  "type": "assistant",
  "uuid": "b380b563-3327-4176-a95d-10be917f7c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bRbM1r56koc4km2YJPys2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10081,
      "cache_read_input_tokens": 53084,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 53084,
          "cache_creation_input_tokens": 10081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10081
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

_source line 29 · 2026-05-22T22:48:42.122Z_

<details><summary>↩ Tool result · `toolu_01H4kessY5Cxh3b7QSQyiJmF`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty
(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty
(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))
(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)
(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)
==> First Aid for varwidth.sty applied!
) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: Reference `tab:ols_vs_correction' on page 3 undefined on input l
ine 100.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:per_condition' on page 3 undefined on input line 
123.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: Reference `tab:gam_taxonomy' on page 4 undefined on input line 1
70.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:bft_contrast' on page 4 undefined on input line 1
97.

[4]

LaTeX Warning: Reference `tab:within_tier' on page 5 undefined on input line 22
1.


LaTeX Warning: Reference `tab:vif' on page 5 undefined on input line 245.

[5]

LaTeX Warning: Reference `tab:panel_size' on page 6 undefined on input line 269
.


LaTeX Warning: Reference `tab:aggregation' on page 6 undefined on input line 29
3.

[6]

LaTeX Warning: Reference `tab:selection' on page 7 undefined on input line 319.


[7] [8]
Overfull \hbox (4.13722pt too wide) in paragraph at lines 422--423
\OT1/cmr/m/n/10.95 tious about regression-based con-clu-sions from com-bi-na-to
-rial panel de-signs with-out non-independence
No file paper.bbl.
[9] (./paper.aux)

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
type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (9 pages, 205180 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty
(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex
(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty
(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))
(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)
(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)
==> First Aid for varwidth.sty applied!
) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
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
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5] [6] [7] [8]
Overfull \hbox (4.13722pt too wide) in paragraph at lines 422--423
\OT1/cmr/m/n/10.95 tious about regression-based con-clu-sions from com-bi-na-to
-rial panel de-signs with-out non-independence
No file paper.bbl.
[9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (9 pages, 207011 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b380b563-3327-4176-a95d-10be917f7c50",
  "isSidechain": false,
  "promptId": "77e178a5-525f-4dfc-8619-10154dd711fe",
  "type": "user",
  "uuid": "718ddbcb-2541-4d94-b295-6f464d98f670",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `tab:ols_vs_correction' on page 3 undefined on input l\nine 100.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:per_condition' on page 3 undefined on input line \n123.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: Reference `tab:gam_taxonomy' on page 4 undefined on input line 1\n70.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:bft_contrast' on page 4 undefined on input line 1\n97.\n\n[4]\n\nLaTeX Warning: Reference `tab:within_tier' on page 5 undefined on input line 22\n1.\n\n\nLaTeX Warning: Reference `tab:vif' on page 5 undefined on input line 245.\n\n[5]\n\nLaTeX Warning: Reference `tab:panel_size' on page 6 undefined on input line 269\n.\n\n\nLaTeX Warning: Reference `tab:aggregation' on page 6 undefined on input line 29\n3.\n\n[6]\n\nLaTeX Warning: Reference `tab:selection' on page 7 undefined on input line 319.\n\n\n[7] [8]\nOverfull \\hbox (4.13722pt too wide) in paragraph at lines 422--423\n\\OT1/cmr/m/n/10.95 tious about regression-based con-clu-sions from com-bi-na-to\n-rial panel de-signs with-out non-independence\nNo file paper.bbl.\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (9 pages, 205180 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjustbox.sty\n(/usr/share/texlive/texmf-dist/tex/latex/xkeyval/xkeyval.sty\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkeyval.tex\n(/usr/share/texlive/texmf-dist/tex/generic/xkeyval/xkvutils.tex)))\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/adjcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/trimclip.sty\n(/usr/share/texlive/texmf-dist/tex/latex/collectbox/collectbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/adjustbox/tc-pdftex.def))\n(/usr/share/texlive/texmf-dist/tex/latex/ifoddpage/ifoddpage.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/varwidth/varwidth.sty)\n==> First Aid for varwidth.sty applied!\n) (/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5] [6] [7] [8]\nOverfull \\hbox (4.13722pt too wide) in paragraph at lines 422--423\n\\OT1/cmr/m/n/10.95 tious about regression-based con-clu-sions from com-bi-na-to\n-rial panel de-signs with-out non-independence\nNo file paper.bbl.\n[9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (9 pages, 207011 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b380b563-3327-4176-a95d-10be917f7c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T22:48:55.516Z_

PDF compiled successfully (9 pages). The paper covers all 10 experiments from `experiment_data.json` with corresponding sections and tables:

1. **Scale expansion** (Table 1, 2) — OLS→bootstrap collapse as headline finding
2. **Attack expansion** (Table 3, 4) — GAM taxonomy degradation with 3 reversals
3. **BFT random-fault contrast** (Table 5) — GO/NO-GO gate failure
4. **Capability-matched validation** (Table 6) — within-tier collapse
5. **VIF/multicollinearity** (Table 7) — 67% shared variance, K_eff 3% unique
6. **Panel size sensitivity** (Table 8) — SE inflation 3.2×→7.2×
7. **Aggregation gradient** (Table 9) — R² 0.89→0.10 survives correction
8. **Panel selection** (Table 10) — min-η_max wins 9/12
9. **ASR concentration** (Table 11) — weak supporting evidence
10. **MT-Bench** (Table 12) — limited transfer to open-ended
11. **Partial-knowledge adversary** (Table 13) — knowledge gradient confirms threat model

The narrative pivots from the original η_max dominance claim to a methodological contribution: the OLS→bootstrap significance collapse itself as the finding, with aggregation gradient and min-η_max selection as salvageable practical contributions. All numbers are drawn directly from `experiment_data.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718ddbcb-2541-4d94-b295-6f464d98f670",
  "isSidechain": false,
  "requestId": "req_011CbJRUqeZKWoGHpxMRGFyv",
  "type": "assistant",
  "uuid": "28bd9da2-8e76-4553-aafb-084c25e9c810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/worst",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDgCofNVbFHKrFx7AwaiP8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6547,
      "cache_read_input_tokens": 63165,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6547,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 63165,
          "cache_creation_input_tokens": 6547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6547
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "28bd9da2-8e76-4553-aafb-084c25e9c810",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist…",
  "leafUuid": "28bd9da2-8e76-4553-aafb-084c25e9c810",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper",
  "sessionId": "2cac05a0-8109-400b-99cb-690453d4755b"
}
```

---
