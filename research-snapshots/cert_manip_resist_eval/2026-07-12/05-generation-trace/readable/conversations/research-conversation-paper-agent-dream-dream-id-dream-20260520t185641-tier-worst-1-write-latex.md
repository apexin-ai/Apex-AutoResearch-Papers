# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5.jsonl`
- **Structured JSON:** [`ed29a98cf675a9e23327.json`](../../sessions/ed/ed29a98cf675a9e23327.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:32:50.907Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:32:50.907Z",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English? A systematic study across 2 architectures and 20 languages.' Value proposition shifts from method contribution to first large-scale answer on whether this research line generalizes. CaCLR is reported as a rigorous negative result — consistency-based objectives do not help when the cross-lingual correctness signal is this noisy. Decomposition is reported as evidence that difficulty and capability are entangled in multilingual representations, contradicting the clean separation assumed by English-only prior work. Pareto frontier is real on Qwen3 but fails to replicate cleanly on Llama 4 Scout — reported as architecture-dependence finding rather than universal law. Orthogonality (Claim 4) survives as the one mechanistic takeaway: output-based calibration is structurally limited everywhere, not just English. Target EACL with framing that negative/diagnostic results at this scale (2 models × 20 languages × all layers) are community-valuable when the field is actively expanding probe-based methods without multilingual validation.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:32:50.910Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:32:50.910Z",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-20T19:32:50.939Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English? A systematic study across 2 architectures and 20 languages.' Value proposition shifts from method contribution to first large-scale answer on whether this research line generalizes. CaCLR is reported as a rigorous negative result — consistency-based objectives do not help when the cross-lingual correctness signal is this noisy. Decomposition is reported as evidence that difficulty and capability are entangled in multilingual representations, contradicting the clean separation assumed by English-only prior work. Pareto frontier is real on Qwen3 but fails to replicate cleanly on Llama 4 Scout — reported as architecture-dependence finding rather than universal law. Orthogonality (Claim 4) survives as the one mechanistic takeaway: output-based calibration is structurally limited everywhere, not just English. Target EACL with framing that negative/diagnostic results at this scale (2 models × 20 languages × all layers) are community-valuable when the field is actively expanding probe-based methods without multilingual validation.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "42eb94fd-d7e2-40be-a72f-117621dcda7a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:32:50.939Z_

```json
{
  "parentUuid": "42eb94fd-d7e2-40be-a72f-117621dcda7a",
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
  "uuid": "249e1bf3-5f35-43ae-b856-22f20a4b824c",
  "timestamp": "2026-05-20T19:32:50.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:32:50.939Z_

```json
{
  "parentUuid": "249e1bf3-5f35-43ae-b856-22f20a4b824c",
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
  "uuid": "5a8546fb-4e5b-4bbc-a738-eb89422f0e50",
  "timestamp": "2026-05-20T19:32:50.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T19:32:50.939Z_

```json
{
  "parentUuid": "5a8546fb-4e5b-4bbc-a738-eb89422f0e50",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5597c3f0-261e-4fd5-9086-5594f0858d8c",
  "timestamp": "2026-05-20T19:32:50.939Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
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
  "aiTitle": "Generate multilingual calibration diagnostic paper",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:32:53.322Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5597c3f0-261e-4fd5-9086-5594f0858d8c",
  "isSidechain": false,
  "requestId": "req_011CbENvnBKDK2Cdur5c2FbA",
  "type": "assistant",
  "uuid": "0c0e8bd4-fe1b-4b98-aaf5-f35b02f4668e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAQe5BptQBJVE6ALWdmpmo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11969,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11969
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

_source line 9 · 2026-05-20T19:32:54.288Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YE7thbNWwpkBD8D5TjKWFF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c0e8bd4-fe1b-4b98-aaf5-f35b02f4668e",
  "isSidechain": false,
  "requestId": "req_011CbENvnBKDK2Cdur5c2FbA",
  "type": "assistant",
  "uuid": "1631f04d-9faa-49d6-90e6-58eb18f6223b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAQe5BptQBJVE6ALWdmpmo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11969,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11969
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

_source line 10 · 2026-05-20T19:32:54.572Z_

<details open><summary>🔧 Tool call — Read · `toolu_018jehhYGSto1SELbtDFEYeo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1631f04d-9faa-49d6-90e6-58eb18f6223b",
  "isSidechain": false,
  "requestId": "req_011CbENvnBKDK2Cdur5c2FbA",
  "type": "assistant",
  "uuid": "ae84f20e-eabd-4dec-9647-0ebc5f742f63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAQe5BptQBJVE6ALWdmpmo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11969,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11969
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

_source line 11 · 2026-05-20T19:32:54.578Z_

<details><summary>↩ Tool result · `toolu_018jehhYGSto1SELbtDFEYeo`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
15	- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
16	- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.
24	- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.
25	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.
26	
27	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
28	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
29	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
30	
31	## Story Spine
32	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
33	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
34	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.
35	- **Headline template**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
36	
37	## Field-Level Significance
38	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
39	
40	## Anticipated Reviewer Concerns & Responses
41	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.
42	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
43	3. **"Mean-shift too weak"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.
44	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
45	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
46	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
47	
48	## Differentiation from Closest Prior Work
49	| Paper | Their Focus | Our Difference |
50	|-------|-------------|----------------|
51	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |
52	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
53	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
54	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
55	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae84f20e-eabd-4dec-9647-0ebc5f742f63",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "c79cce0c-5046-4b33-a64b-3532b7c3f2c4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "ae84f20e-eabd-4dec-9647-0ebc5f742f63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:32:54.749Z_

<details><summary>↩ Tool result · `toolu_01YE7thbNWwpkBD8D5TjKWFF`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)",
4	    "description": "Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.\n",
5	    "results": {
6	      "en_auroc_best_layer": 0.776,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.612,
10	        0.776
11	      ],
12	      "en_ece_raw_best": 0.172,
13	      "en_ece_tempcal_best": 0.068,
14	      "temp_scaling_T": 5.83,
15	      "zs_transfer_auroc_mean_19lang": 0.621,
16	      "zs_transfer_auroc_median_19lang": 0.633,
17	      "zs_transfer_auroc_std_19lang": 0.054,
18	      "zs_transfer_drop_mean_pp": 15.5,
19	      "zs_pass_rate_19lang": 0.368,
20	      "zs_pass_langs": [
21	        "zh",
22	        "fr",
23	        "de",
24	        "es",
25	        "ja",
26	        "ru",
27	        "ko"
28	      ],
29	      "zs_fail_langs": [
30	        "ar",
31	        "hi",
32	        "sw",
33	        "yo",
34	        "te",
35	        "bn",
36	        "ta",
37	        "th",
38	        "vi",
39	        "uk",
40	        "id",
41	        "pl"
42	      ],
43	      "mean_shift_improves_count": 0,
44	      "mean_shift_mean_delta_ece_pp": 3.14,
45	      "linproj_auroc_mean_19lang": 0.648,
46	      "linproj_improves_over_zs_count": 13,
47	      "linproj_mean_delta_auroc_vs_zs_pp": 2.7,
48	      "fewshot25_auroc_mean_19lang": 0.654,
49	      "fewshot25_improves_over_zs_count": 14,
50	      "fewshot100_auroc_mean_19lang": 0.671,
51	      "fewshot100_improves_over_zs_count": 16,
52	      "pareto_depth_transfer_rank_corr": 0.41,
53	      "pareto_frontier_monotonic": false,
54	      "pareto_n_dominated_layers": 6,
55	      "transfer_by_family": {
56	        "indo_european_germanic": {
57	          "mean": 0.672,
58	          "langs": [
59	            "de",
60	            "en"
61	          ]
62	        },
63	        "indo_european_romance": {
64	          "mean": 0.661,
65	          "langs": [
66	            "fr",
67	            "es"
68	          ]
69	        },
70	        "indo_european_slavic": {
71	          "mean": 0.629,
72	          "langs": [
73	            "ru",
74	            "uk",
75	            "pl"
76	          ]
77	        },
78	        "indo_european_indic": {
79	          "mean": 0.598,
80	          "langs": [
81	            "hi",
82	            "bn",
83	            "te",
84	            "ta"
85	          ]
86	        },
87	        "sino_tibetan": {
88	          "mean": 0.668,
89	          "langs": [
90	            "zh"
91	          ]
92	        },
93	        "japonic": {
94	          "mean": 0.651,
95	          "langs": [
96	            "ja"
97	          ]
98	        },
99	        "koreanic": {
100	          "mean": 0.648,
101	          "langs": [
102	            "ko"
103	          ]
104	        },
105	        "afroasiatic": {
106	          "mean": 0.612,
107	          "langs": [
108	            "ar"
109	          ]
110	        },
111	        "niger_congo": {
112	          "mean": 0.543,
113	          "langs": [
114	            "sw",
115	            "yo"
116	          ]
117	        },
118	        "tai_kadai": {
119	          "mean": 0.591,
120	          "langs": [
121	            "th"
122	          ]
123	        },
124	        "austronesian": {
125	          "mean": 0.618,
126	          "langs": [
127	            "id"
128	          ]
129	        },
130	        "austroasiatic": {
131	          "mean": 0.607,
132	          "langs": [
133	            "vi"
134	          ]
135	        }
136	      }
137	    },
138	    "tables": [
139	      {
140	        "name": "Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)",
141	        "columns": [
142	          "layer",
143	          "depth_pct",
144	          "logreg_auroc",
145	          "mlp_auroc",
146	          "ece_raw",
147	          "ece_tempcal"
148	        ],
149	        "rows": [
150	          [
151	            4,
152	            4,
153	            0.612,
154	            0.618,
155	            0.298,
156	            0.192
157	          ],
158	          [
159	            16,
160	            17,
161	            0.653,
162	            0.661,
163	            0.251,
164	            0.148
165	          ],
166	          [
167	            28,
168	            30,
169	            0.694,
170	            0.708,
171	            0.224,
172	            0.121
173	          ],
174	          [
175	            40,
176	            43,
177	            0.721,
178	            0.737,
179	            0.203,
180	            0.098
181	          ],
182	          [
183	            52,
184	            55,
185	            0.742,
186	            0.755,
187	            0.191,
188	            0.082
189	          ],
190	          [
191	            60,
192	            64,
193	            0.758,
194	            0.769,
195	            0.183,
196	            0.075
197	          ],
198	          [
199	            72,
200	            77,
201	            0.776,
202	            0.783,
203	            0.172,
204	            0.068
205	          ],
206	          [
207	            80,
208	            85,
209	            0.771,
210	            0.779,
211	            0.176,
212	            0.071
213	          ],
214	          [
215	            88,
216	            94,
217	            0.753,
218	            0.762,
219	            0.185,
220	            0.079
221	          ],
222	          [
223	            92,
224	            98,
225	            0.728,
226	            0.739,
227	            0.198,
228	            0.091
229	          ]
230	        ]
231	      },
232	      {
233	        "name": "Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)",
234	        "columns": [
235	          "language",
236	          "family",
237	          "resource_tier",
238	          "best_zs_layer",
239	          "best_zs_auroc",
240	          "en_auroc_at_same_layer",
241	          "drop_pp"
242	        ],
243	        "rows": [
244	          [
245	            "zh",
246	            "sino_tibetan",
247	            "high",
248	            52,
249	            0.668,
250	            0.742,
251	            7.4
252	          ],
253	          [
254	            "fr",
255	            "romance",
256	            "high",
257	            52,
258	            0.672,
259	            0.742,
260	            7.0
261	          ],
262	          [
263	            "de",
264	            "germanic",
265	            "high",
266	            52,
267	            0.671,
268	            0.742,
269	            7.1
270	          ],
271	          [
272	            "es",
273	            "romance",
274	            "high",
275	            52,
276	            0.661,
277	            0.742,
278	            8.1
279	          ],
280	          [
281	            "ja",
282	            "japonic",
283	            "high",
284	            48,
285	            0.651,
286	            0.735,
287	            8.4
288	          ],
289	          [
290	            "ru",
291	            "slavic",
292	            "high",
293	            48,
294	            0.644,
295	            0.735,
296	            9.1
297	          ],
298	          [
299	            "ko",
300	            "koreanic",
301	            "high",
302	            48,
303	            0.648,
304	            0.735,
305	            8.7
306	          ],
307	          [
308	            "ar",
309	            "afroasiatic",
310	            "mid",
311	            40,
312	            0.612,
313	            0.721,
314	            10.9
315	          ],
316	          [
317	            "hi",
318	            "indic",
319	            "mid",
320	            40,
321	            0.618,
322	            0.721,
323	            10.3
324	          ],
325	          [
326	            "vi",
327	            "austroasiatic",
328	            "mid",
329	            40,
330	            0.607,
331	            0.721,
332	            11.4
333	          ],
334	          [
335	            "id",
336	            "austronesian",
337	            "mid",
338	            40,
339	            0.618,
340	            0.721,
341	            10.3
342	          ],
343	          [
344	            "th",
345	            "tai_kadai",
346	            "mid",
347	            40,
348	            0.591,
349	            0.721,
350	            13.0
351	          ],
352	          [
353	            "pl",
354	            "slavic",
355	            "mid",
356	            40,
357	            0.621,
358	            0.721,
359	            10.0
360	          ],
361	          [
362	            "uk",
363	            "slavic",
364	            "mid",
365	            40,
366	            0.614,
367	            0.721,
368	            10.7
369	          ],
370	          [
371	            "bn",
372	            "indic",
373	            "low",
374	            28,
375	            0.583,
376	            0.694,
377	            11.1
378	          ],
379	          [
380	            "te",
381	            "indic",
382	            "low",
383	            28,
384	            0.571,
385	            0.694,
386	            12.3
387	          ],
388	          [
389	            "ta",
390	            "indic",
391	            "low",
392	            28,
393	            0.568,
394	            0.694,
395	            12.6
396	          ],
397	          [
398	            "sw",
399	            "niger_congo",
400	            "low",
401	            28,
402	            0.557,
403	            0.694,
404	            13.7
405	          ],
406	          [
407	            "yo",
408	            "niger_congo",
409	            "low",
410	            28,
411	            0.529,
412	            0.694,
413	            16.5
414	          ]
415	        ]
416	      },
417	      {
418	        "name": "Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)",
419	        "columns": [
420	          "method",
421	          "auroc_mean",
422	          "auroc_std",
423	          "pass_rate",
424	          "ece_mean",
425	          "delta_vs_zs_pp"
426	        ],
427	        "rows": [
428	          [
429	            "zero_shot",
430	            0.621,
431	            0.054,
432	            0.368,
433	            0.194,
434	            0.0
435	          ],
436	          [
437	            "mean_shift",
438	            0.604,
439	            0.067,
440	            0.263,
441	            0.225,
442	            -1.7
443	          ],
444	          [
445	            "linear_projection",
446	            0.648,
447	            0.048,
448	            0.526,
449	            0.171,
450	            2.7
451	          ],
452	          [
453	            "few_shot_25",
454	            0.654,
455	            0.045,
456	            0.526,
457	            0.166,
458	            3.3
459	          ],
460	          [
461	            "few_shot_100",
462	            0.671,
463	            0.041,
464	            0.632,
465	            0.152,
466	            5.0
467	          ]
468	        ]
469	      }
470	    ],
471	    "figures": [],
472	    "analysis": "The Pareto frontier is real on Qwen3-235B but weak: rank correlation of 0.41 means the depth-transfer tradeoff explains only ~17% of variance. MoE routing creates non-monotonic perturbations at mid-depth. The practical implication is limited — the frontier provides modest guidance for layer selection but is not a reliable engineering tool. Zero-shot transfer fails for 12/19 languages (AUROC < 0.65), with a clear resource-tier gradient. The field should not assume English-trained correctness probes transfer to low-resource languages. Mean-shift is confirmed dead at scale. Linear projection and few-shot are the only viable transfer methods, with few-shot-100 achieving the best results — but requiring 100 labeled examples per language partially negates the zero-label promise.\n\n\nQwen3-235B is a much larger MoE model than the MVP's Qwen2.5-7B. English AUROC at 0.776 improves modestly over MVP's 0.754 because the model is more capable and the correctness signal is more linearly accessible in larger models, but gains are sublinear — the larger model also has more complex, distributed representations that resist simple linear probing. Zero-shot transfer mean of 0.621 reflects the worst-tier prediction that transfer is unreliable: high-resource Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer adequately because their representations share more subspace structure with English at intermediate layers, but low-resource languages (sw, yo, te, bn) and languages with very different morphology (th, ta) fail because the MoE routing creates language-specific expert patterns that are opaque to an English-trained linear probe. Mean-shift fails entirely (0/19) because the mean activation difference between languages conflates content, style, and script differences — subtracting it removes useful signal. The Pareto frontier rank correlation of 0.41 is real but moderate: the general trend (deeper = better English, worse transfer) holds, but MoE routing introduces non-monotonic noise at mid-depth layers where expert activation patterns shift. The 7/19 pass rate reflects that only typologically close or high-resource languages have enough representational overlap with English for zero-shot transfer to work.\n"
473	  },
474	  {
475	    "name": "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)",
476	    "description": "Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions.\n",
477	    "results": {
478	      "en_auroc_best_layer": 0.749,
479	      "en_best_layer_idx": 36,
480	      "en_auroc_range": [
481	        0.598,
482	        0.749
483	      ],
484	      "en_ece_raw_best": 0.188,
485	      "en_ece_tempcal_best": 0.074,
486	      "temp_scaling_T": 5.47,
487	      "zs_transfer_auroc_mean_19lang": 0.594,
488	      "zs_transfer_auroc_median_19lang": 0.601,
489	      "zs_transfer_auroc_std_19lang": 0.061,
490	      "zs_transfer_drop_mean_pp": 18.2,
491	      "zs_pass_rate_19lang": 0.211,
492	      "zs_pass_langs": [
493	        "zh",
494	        "fr",
495	        "de",
496	        "es"
497	      ],
498	      "zs_fail_langs": [
499	        "ja",
500	        "ru",
501	        "ko",
502	        "ar",
503	        "hi",
504	        "sw",
505	        "yo",
506	        "te",
507	        "bn",
508	        "ta",
509	        "th",
510	        "vi",
511	        "uk",
512	        "id",
513	        "pl"
514	      ],
515	      "mean_shift_improves_count": 0,
516	      "mean_shift_mean_delta_ece_pp": 4.21,
517	      "linproj_auroc_mean_19lang": 0.623,
518	      "linproj_improves_over_zs_count": 11,
519	      "fewshot25_auroc_mean_19lang": 0.631,
520	      "fewshot100_auroc_mean_19lang": 0.652,
521	      "pareto_depth_transfer_rank_corr": 0.22,
522	      "pareto_frontier_monotonic": false,
523	      "pareto_n_dominated_layers": 3,
524	      "pareto_frontier_agreement_with_qwen3": 0.33,
525	      "nonmonotonic_layers": [
526	        20,
527	        24,
528	        28
529	      ]
530	    },
531	    "tables": [
532	      {
533	        "name": "Table 4: Llama 4 Scout English Probe Performance by Layer",
534	        "columns": [
535	          "layer",
536	          "depth_pct",
537	          "logreg_auroc",
538	          "mlp_auroc",
539	          "ece_raw",
540	          "ece_tempcal"
541	        ],
542	        "rows": [
543	          [
544	            4,
545	            8,
546	            0.598,
547	            0.604,
548	            0.312,
549	            0.201
550	          ],
551	          [
552	            8,
553	            17,
554	            0.631,
555	            0.641,
556	            0.274,
557	            0.168
558	          ],
559	          [
560	            12,
561	            25,
562	            0.668,
563	            0.679,
564	            0.241,
565	            0.137
566	          ],
567	          [
568	            16,
569	            33,
570	            0.694,
571	            0.706,
572	            0.218,
573	            0.112
574	          ],
575	          [
576	            20,
577	            42,
578	            0.712,
579	            0.722,
580	            0.205,
581	            0.098
582	          ],
583	          [
584	            24,
585	            50,
586	            0.726,
587	            0.735,
588	            0.196,
589	            0.088
590	          ],
591	          [
592	            28,
593	            58,
594	            0.734,
595	            0.743,
596	            0.192,
597	            0.083
598	          ],
599	          [
600	            32,
601	            67,
602	            0.741,
603	            0.749,
604	            0.189,
605	            0.078
606	          ],
607	          [
608	            36,
609	            75,
610	            0.749,
611	            0.755,
612	            0.188,
613	            0.074
614	          ],
615	          [
616	            40,
617	            83,
618	            0.744,
619	            0.751,
620	            0.19,
621	            0.077
622	          ],
623	          [
624	            44,
625	            92,
626	            0.731,
627	            0.738,
628	            0.195,
629	            0.084
630	          ],
631	          [
632	            48,
633	            100,
634	            0.708,
635	            0.718,
636	            0.209,
637	            0.097
638	          ]
639	        ]
640	      },
641	      {
642	        "name": "Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language (Best Transfer Layer)",
643	        "columns": [
644	          "language",
645	          "best_zs_layer",
646	          "best_zs_auroc",
647	          "drop_vs_en_pp"
648	        ],
649	        "rows": [
650	          [
651	            "zh",
652	            24,
653	            0.658,
654	            6.8
655	          ],
656	          [
657	            "fr",
658	            24,
659	            0.662,
660	            6.4
661	          ],
662	          [
663	            "de",
664	            24,
665	            0.655,
666	            7.1
667	          ],
668	          [
669	            "es",
670	            24,
671	            0.651,
672	            7.5
673	          ],
674	          [
675	            "ja",
676	            20,
677	            0.631,
678	            8.1
679	          ],
680	          [
681	            "ru",
682	            20,
683	            0.622,
684	            9.0
685	          ],
686	          [
687	            "ko",
688	            20,
689	            0.627,
690	            8.5
691	          ],
692	          [
693	            "ar",
694	            16,
695	            0.589,
696	            10.5
697	          ],
698	          [
699	            "hi",
700	            16,
701	            0.594,
702	            10.0
703	          ],
704	          [
705	            "vi",
706	            16,
707	            0.581,
708	            11.3
709	          ],
710	          [
711	            "id",
712	            16,
713	            0.591,
714	            10.3
715	          ],
716	          [
717	            "th",
718	            16,
719	            0.568,
720	            12.6
721	          ],
722	          [
723	            "pl",
724	            20,
725	            0.608,
726	            10.4
727	          ],
728	          [
729	            "uk",
730	            16,
731	            0.592,
732	            10.2
733	          ],
734	          [
735	            "bn",
736	            12,
737	            0.556,
738	            11.2
739	          ],
740	          [
741	            "te",
742	            12,
743	            0.541,
744	            12.7
745	          ],
746	          [
747	            "ta",
748	            12,
749	            0.538,
750	            13.0
751	          ],
752	          [
753	            "sw",
754	            12,
755	            0.524,
756	            14.4
757	          ],
758	          [
759	            "yo",
760	            12,
761	            0.498,
762	            17.0
763	          ]
764	        ]
765	      },
766	      {
767	        "name": "Table 6: Cross-Architecture Pareto Frontier Agreement",
768	        "columns": [
769	          "metric",
770	          "qwen3_235b",
771	          "llama4_scout",
772	          "agreement"
773	        ],
774	        "rows": [
775	          [
776	            "rank_corr_depth_vs_transfer",
777	            0.41,
778	            0.22,
779	            "—"
780	          ],
781	          [
782	            "pareto_optimal_layer_count",
783	            "6/24",
784	            "3/12",
785	            "—"
786	          ],
787	          [
788	            "best_transfer_layer_pct_depth",
789	            "55%",
790	            "50%",
791	            "—"
792	          ],
793	          [
794	            "zs_mean_auroc",
795	            0.621,
796	            0.594,
797	            "—"
798	          ],
799	          [
800	            "optimal_layer_rank_agreement_tau",
801	            "—",
802	            "—",
803	            0.33
804	          ],
805	          [
806	            "pass_lang_overlap_jaccard",
807	            "—",
808	            "—",
809	            0.44
810	          ]
811	        ]
812	      }
813	    ],
814	    "figures": [],
815	    "analysis": "Llama 4 Scout is the worst-tier's smoking gun for the diagnostic reframe. The Pareto frontier essentially doesn't exist on this architecture (rank corr 0.22, only 3 non-dominated layers). This is the strongest evidence for the diagnostic paper's thesis: the depth-transfer tradeoff from Claim 1 is not a universal property of transformers but an architecture-dependent phenomenon that cannot be assumed to generalize. The 0.33 cross-architecture agreement means practitioners cannot use findings from one model to guide layer selection on another. For the paper, this transforms from a weakness into a key finding: the field cannot assume probe-based calibration will behave consistently across architectures.\n\n\nLlama 4 Scout is the worst-tier's key failure point. Its Pareto frontier is flat/non-monotonic (rank correlation 0.22) because Llama 4 Scout's MoE architecture uses a different routing strategy than Qwen3-235B: its experts are more language-specialized at intermediate layers, meaning the English correctness direction at layers 20-28 is entangled with English-specific expert activations in ways that neither degrade nor improve monotonically with depth. English AUROC peaks at 0.749 (lower than Qwen3's 0.776) because Llama 4 Scout's 48 layers compress the representational hierarchy — the same functional stages are packed into fewer layers, leaving less room for a clean correctness signal to emerge. Zero-shot transfer is worse overall (mean 0.594 vs Qwen3's 0.621) because Llama 4 Scout's training data distribution is more English-centric, and its MoE routing assigns non-English tokens to a sparser expert set that shares less structure with the English experts. Only 4/19 languages pass the 0.65 threshold. The 0.33 cross-architecture Pareto agreement means the optimal layer for a given language on Qwen3 does not predict the optimal layer on Llama 4 — the tradeoff is architecture-specific, not a universal property of transformer depth.\n"
816	  },
817	  {
818	    "name": "CaCLR Implementation and Comparative Evaluation",
819	    "description": "Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency). Train CaCLR probes using English labels + unlabeled parallel activations. Compare vs all 5 transfer conditions across full Pareto frontier for both models × 20 languages.\n",
820	    "results": {
821	      "caclr_auroc_mean_qwen3": 0.645,
822	      "caclr_auroc_mean_llama4": 0.618,
823	      "caclr_vs_linproj_auroc_delta_pp_qwen3": -0.3,
824	      "caclr_vs_linproj_auroc_delta_pp_llama4": -0.5,
825	      "caclr_vs_zs_auroc_delta_pp_qwen3": 2.4,
826	      "caclr_vs_zs_auroc_delta_pp_llama4": 2.4,
827	      "caclr_vs_fewshot100_auroc_delta_pp_qwen3": -2.6,
828	      "caclr_vs_fewshot100_auroc_delta_pp_llama4": -3.4,
829	      "caclr_improvement_pass_rate_qwen3": 0.47,
830	      "caclr_improvement_pass_rate_llama4": 0.37,
831	      "caclr_ece_mean_qwen3": 0.174,
832	      "caclr_ece_mean_llama4": 0.189,
833	      "caclr_ece_reduction_vs_tempcal_pct_qwen3": 7.2,
834	      "caclr_ece_reduction_vs_tempcal_pct_llama4": 3.8,
835	      "best_alpha": 0.3,
836	      "best_beta": 0.05,
837	      "alpha_sensitivity": "moderate — ±0.1 changes AUROC by ~0.5pp",
838	      "beta_sensitivity": "flat — β from 0.01 to 0.5 changes AUROC by <0.3pp, indicating consistency loss is inert",
839	      "caclr_no_consistency_auroc_mean": 0.647,
840	      "caclr_no_sbece_auroc_mean": 0.629,
841	      "caclr_bce_only_auroc_mean": 0.621,
842	      "caclr_per_lang_qwen3": {
843	        "zh": {
844	          "auroc": 0.671,
845	          "delta_vs_zs": 0.3,
846	          "delta_vs_linproj": -0.8
847	        },
848	        "fr": {
849	          "auroc": 0.668,
850	          "delta_vs_zs": -0.4,
851	          "delta_vs_linproj": -1.2
852	        },
853	        "de": {
854	          "auroc": 0.665,
855	          "delta_vs_zs": -0.6,
856	          "delta_vs_linproj": -0.9
857	        },
858	        "es": {
859	          "auroc": 0.658,
860	          "delta_vs_zs": -0.3,
861	          "delta_vs_linproj": -0.7
862	        },
863	        "ja": {
864	          "auroc": 0.649,
865	          "delta_vs_zs": -0.2,
866	          "delta_vs_linproj": -0.4
867	        },
868	        "ru": {
869	          "auroc": 0.641,
870	          "delta_vs_zs": -0.3,
871	          "delta_vs_linproj": -0.6
872	        },
873	        "ko": {
874	          "auroc": 0.647,
875	          "delta_vs_zs": -0.1,
876	          "delta_vs_linproj": -0.3
877	        },
878	        "ar": {
879	          "auroc": 0.628,
880	          "delta_vs_zs": 1.6,
881	          "delta_vs_linproj": 0.2
882	        },
883	        "hi": {
884	          "auroc": 0.635,
885	          "delta_vs_zs": 1.7,
886	          "delta_vs_linproj": 0.1
887	        },
888	        "vi": {
889	          "auroc": 0.621,
890	          "delta_vs_zs": 1.4,
891	          "delta_vs_linproj": -0.3
892	        },
893	        "id": {
894	          "auroc": 0.633,
895	          "delta_vs_zs": 1.5,
896	          "delta_vs_linproj": -0.1
897	        },
898	        "th": {
899	          "auroc": 0.607,
900	          "delta_vs_zs": 1.6,
901	          "delta_vs_linproj": 0.3
902	        },
903	        "pl": {
904	          "auroc": 0.638,
905	          "delta_vs_zs": 1.7,
906	          "delta_vs_linproj": 0.1
907	        },
908	        "uk": {
909	          "auroc": 0.631,
910	          "delta_vs_zs": 1.7,
911	          "delta_vs_linproj": 0.2
912	        },
913	        "bn": {
914	          "auroc": 0.601,
915	          "delta_vs_zs": 1.8,
916	          "delta_vs_linproj": 0.5
917	        },
918	        "te": {
919	          "auroc": 0.589,
920	          "delta_vs_zs": 1.8,
921	          "delta_vs_linproj": 0.4
922	        },
923	        "ta": {
924	          "auroc": 0.587,
925	          "delta_vs_zs": 1.9,
926	          "delta_vs_linproj": 0.6
927	        },
928	        "sw": {
929	          "auroc": 0.578,
930	          "delta_vs_zs": 2.1,
931	          "delta_vs_linproj": 0.9
932	        },
933	        "yo": {
934	          "auroc": 0.551,
935	          "delta_vs_zs": 2.2,
936	          "delta_vs_linproj": 0.7
937	        }
938	      }
939	    },
940	    "tables": [
941	      {
942	        "name": "Table 7: Transfer Method Comparison Summary (19-Language Mean, Both Architectures)",
943	        "columns": [
944	          "method",
945	          "qwen3_auroc",
946	          "qwen3_ece",
947	          "llama4_auroc",
948	          "llama4_ece",
949	          "labels_needed"
950	        ],
951	        "rows": [
952	          [
953	            "zero_shot",
954	            0.621,
955	            0.194,
956	            0.594,
957	            0.212,
958	            "0 target"
959	          ],
960	          [
961	            "mean_shift",
962	            0.604,
963	            0.225,
964	            0.571,
965	            0.248,
966	            "0 target (fails)"
967	          ],
968	          [
969	            "linear_projection",
970	            0.648,
971	            0.171,
972	            0.623,
973	            0.189,
974	            "~50 parallel"
975	          ],
976	          [
977	            "CaCLR",
978	            0.645,
979	            0.174,
980	            0.618,
981	            0.193,
982	            "0 target + parallel"
983	          ],
984	          [
985	            "few_shot_25",
986	            0.654,
987	            0.166,
988	            0.631,
989	            0.182,
990	            "25 target"
991	          ],
992	          [
993	            "few_shot_100",
994	            0.671,
995	            0.152,
996	            0.652,
997	            0.168,
998	            "100 target"
999	          ]
1000	        ]
1001	      },
1002	      {
1003	        "name": "Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)",
1004	        "columns": [
1005	          "variant",
1006	          "auroc_mean",
1007	          "ece_mean",
1008	          "delta_vs_full_pp"
1009	        ],
1010	        "rows": [
1011	          [
1012	            "Full CaCLR (BCE+SB-ECE+Consistency)",
1013	            0.645,
1014	            0.174,
1015	            0.0
1016	          ],
1017	          [
1018	            "CaCLR − Consistency (BCE+SB-ECE)",
1019	            0.647,
1020	            0.172,
1021	            0.2
1022	          ],
1023	          [
1024	            "CaCLR − SB-ECE (BCE+Consistency)",
1025	            0.629,
1026	            0.188,
1027	            -1.6
1028	          ],
1029	          [
1030	            "BCE Only (= zero-shot probe)",
1031	            0.621,
1032	            0.194,
1033	            -2.4
1034	          ],
1035	          [
1036	            "Linear Projection",
1037	            0.648,
1038	            0.171,
1039	            0.3
1040	          ]
1041	        ]
1042	      }
1043	    ],
1044	    "figures": [],
1045	    "analysis": "CaCLR is a rigorous negative result. The consistency loss term — the core methodological novelty — is inert. This is not a hyperparameter tuning failure; β is swept over 3 orders of magnitude and the landscape is flat. The SB-ECE term provides modest calibration regularization, but this benefit is available without any cross-lingual machinery. Linear projection achieves the same or better results with a simpler mechanism. For the paper, this is framed as: \"consistency-based cross-lingual alignment objectives do not help when the underlying correctness signal has low cross-lingual SNR. This negative result saves the community from pursuing distributional-matching approaches (adversarial, MMD, consistency) for this problem class.\"\n\n\nCaCLR's consistency loss (L_consistency) is designed to align cross-lingual probe activations so that the English probe generalizes. In the worst tier, this fails because the cross-lingual correctness signal is too noisy for the consistency objective to find meaningful invariances. The unlabeled parallel activations contain language-specific variance (script, morphology, tokenization artifacts) that dominates the correctness signal, so minimizing distributional distance between languages collapses both signal and noise. The hyperparameter search confirms this: β (consistency weight) is driven to near-zero (0.05), and removing the consistency term entirely slightly improves performance (+0.2pp). The SB-ECE term helps modestly because it acts as a calibration regularizer on the English side, but this benefit doesn't compound with consistency. CaCLR ends up being essentially \"zero-shot + SB-ECE regularization\" — functionally a slightly calibration-aware version of the base probe. Linear projection beats CaCLR because projection directly estimates and applies the affine transformation between language representation subspaces, which is a more efficient use of the few available parallel datapoints than trying to learn an invariant representation. The key insight: simple alignment (linproj) outperforms principled invariance (CaCLR) when the signal-to-noise ratio of the target signal is low. For high-resource languages that already transfer well, CaCLR's overhead yields no benefit; for low-resource languages where help is needed, the consistency signal is too noisy to learn from.\n"
1046	  },
1047	  {
1048	    "name": "Difficulty-Controlled Ablation (Decomposition)",
1049	    "description": "Train IRT difficulty probes, project out difficulty direction from activations, retrain correctness probes on residuals, evaluate transfer. 10 representative languages × 8 representative layers per model.\n",
1050	    "results": {
1051	      "difficulty_probe_r2_en_qwen3": 0.52,
1052	      "difficulty_probe_r2_en_llama4": 0.47,
1053	      "difficulty_probe_transfer_r2_mean_9lang": 0.41,
1054	      "decomp_difficulty_var_explained_pct_qwen3": 14.3,
1055	      "decomp_difficulty_var_explained_pct_llama4": 11.8,
1056	      "correctness_residual_auroc_en_qwen3": 0.738,
1057	      "correctness_residual_auroc_en_llama4": 0.711,
1058	      "correctness_residual_transfer_auroc_mean_qwen3": 0.607,
1059	      "correctness_residual_transfer_auroc_mean_llama4": 0.581,
1060	      "transfer_improvement_after_projection": false,
1061	      "transfer_delta_after_projection_pp_qwen3": -1.4,
1062	      "transfer_delta_after_projection_pp_llama4": -1.3,
1063	      "difficulty_correctness_cosine_mean_qwen3": 0.34,
1064	      "difficulty_correctness_cosine_mean_llama4": 0.38,
1065	      "difficulty_correctness_cosine_std": 0.11,
1066	      "subspace_overlap_mean_angle_deg": 58
1067	    },
1068	    "tables": [
1069	      {
1070	        "name": "Table 9: Difficulty Probe Quality (Ridge Regression, R² on Held-Out)",
1071	        "columns": [
1072	          "language",
1073	          "qwen3_r2",
1074	          "llama4_r2",
1075	          "is_transfer"
1076	        ],
1077	        "rows": [
1078	          [
1079	            "en",
1080	            0.52,
1081	            0.47,
1082	            false
1083	          ],
1084	          [
1085	            "zh",
1086	            0.48,
1087	            0.43,
1088	            true
1089	          ],
1090	          [
1091	            "fr",
1092	            0.47,
1093	            0.42,
1094	            true
1095	          ],
1096	          [
1097	            "de",
1098	            0.46,
1099	            0.41,
1100	            true
1101	          ],
1102	          [
1103	            "ar",
1104	            0.42,
1105	            0.37,
1106	            true
1107	          ],
1108	          [
1109	            "hi",
1110	            0.41,
1111	            0.36,
1112	            true
1113	          ],
1114	          [
1115	            "ja",
1116	            0.44,
1117	            0.39,
1118	            true
1119	          ],
1120	          [
1121	            "ko",
1122	            0.43,
1123	            0.38,
1124	            true
1125	          ],
1126	          [
1127	            "sw",
1128	            0.33,
1129	            0.28,
1130	            true
1131	          ],
1132	          [
1133	            "yo",
1134	            0.29,
1135	            0.24,
1136	            true
1137	          ]
1138	        ]
1139	      },
1140	      {
1141	        "name": "Table 10: Decomposition Transfer Ablation (9-Language Mean)",
1142	        "columns": [
1143	          "condition",
1144	          "qwen3_auroc",
1145	          "qwen3_delta_pp",
1146	          "llama4_auroc",
1147	          "llama4_delta_pp"
1148	        ],
1149	        "rows": [
1150	          [
1151	            "Full activations (baseline)",
1152	            0.621,
1153	            0.0,
1154	            0.594,
1155	            0.0
1156	          ],
1157	          [
1158	            "Residual (difficulty projected out)",
1159	            0.607,
1160	            -1.4,
1161	            0.581,
1162	            -1.3
1163	          ],
1164	          [
1165	            "Difficulty component only",
1166	            0.568,
1167	            -5.3,
1168	            0.551,
1169	            -4.3
1170	          ],
1171	          [
1172	            "Random direction projected out (ctrl)",
1173	            0.618,
1174	            -0.3,
1175	            0.591,
1176	            -0.3
1177	          ]
1178	        ]
1179	      }
1180	    ],
1181	    "figures": [],
1182	    "analysis": "Decomposition fails as a prescriptive tool. The difficulty-shared component, far from being a confound, is actually one of the more reliable cross-lingual bridges — removing it hurts. The capability-specific residual is more language-dependent, not less, because it captures idiosyncratic encoding patterns. For the diagnostic paper, this finding is reframed as: \"difficulty and capability are entangled in multilingual representations, unlike the clean separation reported in English-only work. This entanglement may be fundamental to how multilingual models represent knowledge — the shared difficulty structure is load-bearing for cross-lingual transfer, not a confound to be controlled for.\"\n\n\nIn the worst tier, difficulty and capability are entangled in cross-lingual representations. The difficulty direction explains only 14% (Qwen3) / 12% (Llama4) of correctness probe variance — real but modest. Critically, projecting out difficulty makes transfer WORSE (-1.3 to -1.4pp), not better. This is because the difficulty-shared component actually carries useful cross-lingual signal: questions that are hard in English tend to be hard everywhere due to shared conceptual complexity, and this shared difficulty signal is one of the few reliable cross-lingual bridges for the correctness probe. Removing it strips away a genuine cross-lingual invariance. The residual \"capability-specific\" component is more language-dependent, not less — it contains the idiosyncratic ways each language's tokens encode competence, which are precisely the non-transferable signals. The cosine similarity of 0.34-0.38 between difficulty and correctness directions confirms they are neither orthogonal nor aligned — they share a moderate subspace that cannot be cleanly separated. This contradicts the paper's original Claim 2 hypothesis that decomposition would be prescriptive. The decomposition is real but useless: it describes variance structure without enabling better transfer.\n"
1183	  },
1184	  {
1185	    "name": "Cross-Lingual Orthogonality Analysis",
1186	    "description": "Extract verbalized confidence direction, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\n",
1187	    "results": {
1188	      "orthogonality_cosine_mean_overall": 0.072,
1189	      "orthogonality_cosine_std_overall": 0.038,
1190	      "orthogonality_cosine_mean_qwen3": 0.068,
1191	      "orthogonality_cosine_mean_llama4": 0.076,
1192	      "orthogonality_cosine_range": [
1193	        0.018,
1194	        0.148
1195	      ],
1196	      "orthogonality_cosine_high_resource": 0.054,
1197	      "orthogonality_cosine_mid_resource": 0.071,
1198	      "orthogonality_cosine_low_resource": 0.098,
1199	      "pct_langs_cosine_below_0_1": 0.75,
1200	      "pct_langs_cosine_below_0_05": 0.35,
1201	      "confidence_probe_r2_mean": 0.68,
1202	      "confidence_probe_transfer_drops": true
1203	    },
1204	    "tables": [
1205	      {
1206	        "name": "Table 11: Correctness-Confidence Cosine Similarity by Language",
1207	        "columns": [
1208	          "language",
1209	          "resource_tier",
1210	          "qwen3_cosine",
1211	          "llama4_cosine",
1212	          "mean_cosine"
1213	        ],
1214	        "rows": [
1215	          [
1216	            "en",
1217	            "high",
1218	            0.038,
1219	            0.041,
1220	            0.04
1221	          ],
1222	          [
1223	            "zh",
1224	            "high",
1225	            0.042,
1226	            0.049,
1227	            0.046
1228	          ],
1229	          [
1230	            "fr",
1231	            "high",
1232	            0.045,
1233	            0.051,
1234	            0.048
1235	          ],
1236	          [
1237	            "de",
1238	            "high",
1239	            0.047,
1240	            0.054,
1241	            0.051
1242	          ],
1243	          [
1244	            "es",
1245	            "high",
1246	            0.049,
1247	            0.056,
1248	            0.053
1249	          ],
1250	          [
1251	            "ja",
1252	            "high",
1253	            0.055,
1254	            0.062,
1255	            0.059
1256	          ],
1257	          [
1258	            "ru",
1259	            "high",
1260	            0.058,
1261	            0.064,
1262	            0.061
1263	          ],
1264	          [
1265	            "ko",
1266	            "high",
1267	            0.061,
1268	            0.068,
1269	            0.065
1270	          ],
1271	          [
1272	            "ar",
1273	            "mid",
1274	            0.063,
1275	            0.072,
1276	            0.068
1277	          ],
1278	          [
1279	            "hi",
1280	            "mid",
1281	            0.065,
1282	            0.075,
1283	            0.07
1284	          ],
1285	          [
1286	            "vi",
1287	            "mid",
1288	            0.068,
1289	            0.077,
1290	            0.073
1291	          ],
1292	          [
1293	            "id",
1294	            "mid",
1295	            0.064,
1296	            0.073,
1297	            0.069
1298	          ],
1299	          [
1300	            "th",
1301	            "mid",
1302	            0.072,
1303	            0.082,
1304	            0.077
1305	          ],
1306	          [
1307	            "pl",
1308	            "mid",
1309	            0.059,
1310	            0.067,
1311	            0.063
1312	          ],
1313	          [
1314	            "uk",
1315	            "mid",
1316	            0.062,
1317	            0.071,
1318	            0.067
1319	          ],
1320	          [
1321	            "bn",
1322	            "low",
1323	            0.081,
1324	            0.092,
1325	            0.087
1326	          ],
1327	          [
1328	            "te",
1329	            "low",
1330	            0.088,
1331	            0.098,
1332	            0.093
1333	          ],
1334	          [
1335	            "ta",
1336	            "low",
1337	            0.091,
1338	            0.103,
1339	            0.097
1340	          ],
1341	          [
1342	            "sw",
1343	            "low",
1344	            0.098,
1345	            0.112,
1346	            0.105
1347	          ],
1348	          [
1349	            "yo",
1350	            "low",
1351	            0.112,
1352	            0.148,
1353	            0.13
1354	          ]
1355	        ]
1356	      },
1357	      {
1358	        "name": "Table 12: Orthogonality by Resource Tier (Mean Cosine ± Std)",
1359	        "columns": [
1360	          "resource_tier",
1361	          "n_langs",
1362	          "qwen3_mean",
1363	          "llama4_mean",
1364	          "overall_mean",
1365	          "std"
1366	        ],
1367	        "rows": [
1368	          [
1369	            "high",
1370	            8,
1371	            0.049,
1372	            0.056,
1373	            0.054,
1374	            0.009
1375	          ],
1376	          [
1377	            "mid",
1378	            7,
1379	            0.065,
1380	            0.074,
1381	            0.071,
1382	            0.005
1383	          ],
1384	          [
1385	            "low",
1386	            5,
1387	            0.094,
1388	            0.111,
1389	            0.098,
1390	            0.016
1391	          ],
1392	          [
1393	            "all",
1394	            20,
1395	            0.066,
1396	            0.076,
1397	            0.072,
1398	            0.022
1399	          ]
1400	        ]
1401	      }
1402	    ],
1403	    "figures": [],
1404	    "analysis": "Claim 4 survives in the worst tier but its contribution is incremental. Orthogonality persists (mean 0.072, all < 0.15) — output-based calibration is indeed structurally limited everywhere. The resource-tier gradient (high: 0.054, mid: 0.071, low: 0.098) is novel but the effect size is modest. The correlation between orthogonality and transfer success is intriguing but not causal. For the diagnostic paper, this is framed as the one mechanistic takeaway: \"the correctness-confidence dissociation is a multilingual phenomenon, confirming that output-based calibration methods face a structural ceiling regardless of language. However, this ceiling is slightly lower for low-resource languages, suggesting that the dissociation partly reflects representation quality rather than a pure architectural invariant.\"\n\n\nOrthogonality persists cross-lingually (mean cosine 0.072, all languages below 0.15) because it is a structural property of how LLMs represent confidence vs correctness — the model's verbalized confidence is calibrated to appear confident regardless of actual correctness, and this dissociation is encoded geometrically at the representation level. However, the worst-tier variance is higher than Miao & Ungar's English-only finding (std 0.038 vs their ~0.01): low-resource languages show less orthogonality (cosine ~0.098) because the model has less capacity to maintain the confidence-correctness dissociation for languages with limited training data — when the model is uncertain due to lack of language-specific knowledge, both its correctness and confidence signals degrade in correlated ways, slightly breaking orthogonality. Reviewers may see this as incremental: Miao & Ungar showed orthogonality for English, we extend to 20 languages, but the finding is qualitatively the same. The resource- tier modulation is the one novel angle but the effect size is modest (0.054 vs 0.098).\n"
1405	  },
1406	  {
1407	    "name": "Probe Complexity Comparison",
1408	    "description": "Compare logistic regression vs 2-layer MLP at each probed layer for both models. Test hypothesis that linear probes transfer better cross-lingually.\n",
1409	    "results": {
1410	      "mlp_vs_logreg_en_auroc_delta_mean_pp_qwen3": 1.1,
1411	      "mlp_vs_logreg_en_auroc_delta_mean_pp_llama4": 0.9,
1412	      "mlp_vs_logreg_transfer_auroc_delta_mean_pp_qwen3": -0.4,
1413	      "mlp_vs_logreg_transfer_auroc_delta_mean_pp_llama4": -0.2,
1414	      "hypothesis_linear_transfers_better": "weak support",
1415	      "effect_size_cohens_d": 0.18,
1416	      "mlp_advantage_shallow_layers_pp": 0.6,
1417	      "mlp_advantage_deep_layers_pp": 1.4,
1418	      "logreg_transfer_advantage_shallow_pp": 0.1,
1419	      "logreg_transfer_advantage_deep_pp": 0.7
1420	    },
1421	    "tables": [
1422	      {
1423	        "name": "Table 13: Probe Complexity Comparison (Mean Across All Layers)",
1424	        "columns": [
1425	          "model",
1426	          "probe",
1427	          "en_auroc_mean",
1428	          "transfer_auroc_mean",
1429	          "en_ece_mean",
1430	          "transfer_ece_mean"
1431	        ],
1432	        "rows": [
1433	          [
1434	            "qwen3",
1435	            "logreg",
1436	            0.714,
1437	            0.621,
1438	            0.206,
1439	            0.194
1440	          ],
1441	          [
1442	            "qwen3",
1443	            "mlp",
1444	            0.725,
1445	            0.617,
1446	            0.198,
1447	            0.197
1448	          ],
1449	          [
1450	            "llama4",
1451	            "logreg",
1452	            0.697,
1453	            0.594,
1454	            0.219,
1455	            0.212
1456	          ],
1457	          [
1458	            "llama4",
1459	            "mlp",
1460	            0.706,
1461	            0.592,
1462	            0.212,
1463	            0.214
1464	          ]
1465	        ]
1466	      }
1467	    ],
1468	    "figures": [],
1469	    "analysis": "Probe complexity is a non-finding. The effect is real but negligible (Cohen's d 0.18). Logistic regression is the correct default choice: nearly identical performance with fewer hyperparameters and better interpretability. This goes into the supplementary as a methods validation, not a main finding.\n\n\nThe hypothesis that linear probes transfer better receives only weak support. MLP probes are ~1pp better in English because the 2-layer MLP captures mild nonlinearities in the correctness signal (interaction effects between representation dimensions). But the cross-lingual transfer difference is tiny (-0.2 to -0.4pp favoring logistic regression) and inconsistent across languages and layers — Cohen's d of 0.18 means the effect would be invisible without large sample sizes. The interaction with depth is the most interesting signal: at deep layers, MLP probes overfit to English-specific patterns more (1.4pp English advantage) and consequently transfer worse (0.7pp transfer penalty). But even this effect is too small to be practically actionable. For the paper, this confirms logistic regression as the appropriate probe choice (simpler, nearly as good) but doesn't generate a standalone finding.\n"
1470	  },
1471	  {
1472	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1473	    "description": "Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and MMLU-ProX (translated MMLU, 20 languages).\n",
1474	    "results": {
1475	      "belebele_en_auroc_qwen3": 0.741,
1476	      "belebele_en_auroc_llama4": 0.718,
1477	      "belebele_zs_transfer_mean_qwen3": 0.598,
1478	      "belebele_zs_transfer_mean_llama4": 0.572,
1479	      "belebele_drop_vs_globalmmlu_pp": 2.3,
1480	      "belebele_caclr_delta_vs_linproj_pp": -0.6,
1481	      "mmlupx_en_auroc_qwen3": 0.762,
1482	      "mmlupx_en_auroc_llama4": 0.738,
1483	      "mmlupx_zs_transfer_mean_qwen3": 0.583,
1484	      "mmlupx_zs_transfer_mean_llama4": 0.557,
1485	      "mmlupx_drop_vs_globalmmlu_pp": 3.8,
1486	      "mmlupx_caclr_delta_vs_linproj_pp": -0.9,
1487	      "lang_rank_correlation_globalmmlu_vs_belebele": 0.82,
1488	      "lang_rank_correlation_globalmmlu_vs_mmlupx": 0.71
1489	    },
1490	    "tables": [
1491	      {
1492	        "name": "Table 14: Cross-Benchmark Generalization (19-Language Mean)",
1493	        "columns": [
1494	          "benchmark",
1495	          "metric",
1496	          "qwen3",
1497	          "llama4"
1498	        ],
1499	        "rows": [
1500	          [
1501	            "GlobalMMLU",
1502	            "zs_transfer_auroc",
1503	            0.621,
1504	            0.594
1505	          ],
1506	          [
1507	            "Belebele",
1508	            "zs_transfer_auroc",
1509	            0.598,
1510	            0.572
1511	          ],
1512	          [
1513	            "MMLU-ProX",
1514	            "zs_transfer_auroc",
1515	            0.583,
1516	            0.557
1517	          ],
1518	          [
1519	            "GlobalMMLU",
1520	            "caclr_vs_linproj_pp",
1521	            -0.3,
1522	            -0.5
1523	          ],
1524	          [
1525	            "Belebele",
1526	            "caclr_vs_linproj_pp",
1527	            -0.6,
1528	            -0.8
1529	          ],
1530	          [
1531	            "MMLU-ProX",
1532	            "caclr_vs_linproj_pp",
1533	            -0.9,
1534	            -1.2
1535	          ]
1536	        ]
1537	      }
1538	    ],
1539	    "figures": [],
1540	    "analysis": "Results partially generalize: Belebele confirms the main findings, MMLU-ProX is noisier due to translation artifacts. The language ranking is stable across benchmarks (which languages transfer well vs poorly is consistent), but absolute performance degrades with benchmark domain shift. CaCLR's negative result is robust across all three benchmarks — it never beats linear projection. For the paper, include Belebele in the main results and MMLU-ProX in supplementary with a note about translation artifacts.\n\n\nBelebele partially replicates GlobalMMLU findings because it is also a high-quality, natively multilingual benchmark where translation artifacts are minimal. The 2.3pp drop reflects the domain shift (reading comprehension vs knowledge questions) but the relative ranking of languages is preserved (rank corr 0.82). MMLU-ProX shows worse transfer (3.8pp drop) because it is machine-translated from English MMLU — translation artifacts create systematic distributional shifts that the English-trained correctness probe cannot handle. The translation introduces new failure modes: ambiguous translations for domain-specific terms, cultural references that don't transfer, and occasional errors in low-resource translations. CaCLR is again no better than linear projection on either benchmark, confirming the negative result generalizes beyond the training benchmark.\n"
1541	  },
1542	  {
1543	    "name": "INT8 Validation Ablation",
1544	    "description": "Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset. Validate that INT8 quantization doesn't distort correctness signals.\n",
1545	    "results": {
1546	      "int8_vs_fp16_auroc_delta_mean_pp": -0.3,
1547	      "int8_vs_fp16_auroc_delta_max_pp": -0.7,
1548	      "int8_vs_fp16_ece_delta_mean_pp": 0.2,
1549	      "int8_vs_fp16_activation_cosine_sim_mean": 0.994,
1550	      "int8_vs_fp16_rank_correlation_layers": 0.98,
1551	      "validation_passes": true
1552	    },
1553	    "tables": [
1554	      {
1555	        "name": "Table S1 (supplementary): INT8 vs FP16 Probing Comparison",
1556	        "columns": [
1557	          "layer",
1558	          "fp16_auroc",
1559	          "int8_auroc",
1560	          "delta_pp",
1561	          "activation_cosine"
1562	        ],
1563	        "rows": [
1564	          [
1565	            8,
1566	            0.637,
1567	            0.633,
1568	            -0.4,
1569	            0.993
1570	          ],
1571	          [
1572	            16,
1573	            0.7,
1574	            0.697,
1575	            -0.3,
1576	            0.994
1577	          ],
1578	          [
1579	            24,
1580	            0.731,
1581	            0.729,
1582	            -0.2,
1583	            0.995
1584	          ],
1585	          [
1586	            32,
1587	            0.746,
1588	            0.743,
1589	            -0.3,
1590	            0.994
1591	          ],
1592	          [
1593	            40,
1594	            0.748,
1595	            0.741,
1596	            -0.7,
1597	            0.992
1598	          ]
1599	        ]
1600	      }
1601	    ],
1602	    "figures": [],
1603	    "analysis": "INT8 validation passes. Quantization is not a confound for any findings in this paper. Include in supplementary appendix as one paragraph + Table S1.\n\n\nINT8 quantization introduces minimal distortion to correctness signals. The 0.3pp mean AUROC difference is within noise — INT8 preserves the relative ordering of activations that linear probes rely on, even though absolute magnitudes shift slightly. The 0.994 cosine similarity between INT8 and FP16 activations confirms near-perfect directional alignment. This is expected because correctness is encoded in the direction of activations, not their magnitude, and INT8 preserves directions well. The layer ranking is identical (rank corr 0.98). This ablation passes cleanly even in the worst tier — quantization artifacts are not the source of any failures observed elsewhere.\n"
1604	  },
1605	  {
1606	    "name": "Gemma 4 31B Dense — Third Architecture (Camera-Ready)",
1607	    "description": "Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense architecture, FP16). Provides dense-vs-MoE architectural contrast for camera-ready extension.\n",
1608	    "results": {
1609	      "en_auroc_best_layer": 0.761,
1610	      "en_best_layer_idx": 45,
1611	      "zs_transfer_auroc_mean_19lang": 0.608,
1612	      "zs_transfer_drop_mean_pp": 16.8,
1613	      "pareto_depth_transfer_rank_corr": 0.48,
1614	      "pareto_frontier_agreement_with_qwen3": 0.42,
1615	      "pareto_frontier_agreement_with_llama4": 0.29,
1616	      "caclr_vs_linproj_pp": -0.2,
1617	      "dense_vs_moe_finding": "Dense architecture shows cleaner Pareto frontier (rank corr 0.48 vs 0.41/0.22 for MoE models) — MoE routing is a source of non-monotonic noise in the depth-transfer relationship"
1618	    },
1619	    "tables": [
1620	      {
1621	        "name": "Table 15: Three-Architecture Comparison Summary",
1622	        "columns": [
1623	          "model",
1624	          "type",
1625	          "layers",
1626	          "en_auroc",
1627	          "transfer_auroc",
1628	          "pareto_rank_corr",
1629	          "pareto_agreement_mean"
1630	        ],
1631	        "rows": [
1632	          [
1633	            "Qwen3-235B",
1634	            "MoE",
1635	            94,
1636	            0.776,
1637	            0.621,
1638	            0.41,
1639	            0.38
1640	          ],
1641	          [
1642	            "Llama4-Scout",
1643	            "MoE",
1644	            48,
1645	            0.749,
1646	            0.594,
1647	            0.22,
1648	            0.31
1649	          ],
1650	          [
1651	            "Gemma4-31B",
1652	            "Dense",
1653	            60,
1654	            0.761,
1655	            0.608,
1656	            0.48,
1657	            0.36
1658	          ]
1659	        ]
1660	      }
1661	    ],
1662	    "figures": [],
1663	    "analysis": "Gemma4 confirms the diagnostic paper's thesis from a new angle: the Pareto frontier is more coherent in dense architectures, implicating MoE routing as a specific source of cross-lingual transfer noise. For camera-ready, this strengthens the \"architecture matters\" message without changing the core worst-tier narrative.\n\n\nGemma 4 31B Dense shows a cleaner (but still moderate) Pareto frontier because dense architectures have more homogeneous layer-to-layer representation transformations — no expert routing to create non-monotonic jumps. The rank correlation of 0.48 is the highest of the three architectures but still in the worst tier range. English AUROC of 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent with its intermediate model size. Transfer is intermediate too (0.608). Cross-architecture agreement remains low (0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence. The dense-vs-MoE contrast is the main value-add for camera-ready: it demonstrates that MoE routing is a specific source of frontier noise, not just model variation.\n"
1664	  },
1665	  {
1666	    "name": "Extended Language Coverage (50+ Languages, Camera-Ready)",
1667	    "description": "Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.\n",
1668	    "results": {
1669	      "total_languages": 52,
1670	      "zs_transfer_auroc_mean_51lang": 0.587,
1671	      "zs_pass_rate_51lang": 0.235,
1672	      "new_lang_families_added": 5,
1673	      "low_resource_auroc_mean_new_langs": 0.548,
1674	      "worst_language_auroc": 0.491,
1675	      "resource_tier_gradient_steeper": true
1676	    },
1677	    "tables": [
1678	      {
1679	        "name": "Table 16: Transfer Success by Resource Tier (Expanded 52-Language Set, Qwen3)",
1680	        "columns": [
1681	          "resource_tier",
1682	          "n_langs",
1683	          "zs_auroc_mean",
1684	          "zs_auroc_std",
1685	          "pass_rate"
1686	        ],
1687	        "rows": [
1688	          [
1689	            "high",
1690	            10,
1691	            0.653,
1692	            0.018,
1693	            0.7
1694	          ],
1695	          [
1696	            "mid",
1697	            18,
1698	            0.603,
1699	            0.024,
1700	            0.28
1701	          ],
1702	          [
1703	            "low",
1704	            14,
1705	            0.558,
1706	            0.031,
1707	            0.07
1708	          ],
1709	          [
1710	            "very_low",
1711	            10,
1712	            0.521,
1713	            0.022,
1714	            0.0
1715	          ]
1716	        ]
1717	      }
1718	    ],
1719	    "figures": [],
1720	    "analysis": "Extended coverage is the nail in the coffin for universal probe-based calibration. With 52 languages, the majority fail to transfer. The resource-tier gradient is steep and monotonic. This is the strongest evidence for the diagnostic paper's conclusion: \"this research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\"\n\nExpanding to 50+ languages worsens the aggregate picture because the additional languages are predominantly low- and very-low-resource. Many of these languages (e.g., Amharic, Lao, Mongolian, Georgian) have minimal representation in the models' training data, so their internal representations share even less structure with English. The pass rate drops from ~37% (7/19) to ~24% (12/51), and some languages approach chance (AUROC ~0.49). For the paper, this strengthens the diagnostic message: \"probe-based calibration has a severe language barrier that scales with the number of languages you try to cover.\"\n"
1721	  }
1722	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1631f04d-9faa-49d6-90e6-58eb18f6223b",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "adad38cf-e086-425e-8157-55862e38b1f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)\",\n    \"description\": \"Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.776,\n      \"en_best_layer_idx\": 72,\n      \"en_auroc_range\": [\n        0.612,\n        0.776\n      ],\n      \"en_ece_raw_best\": 0.172,\n      \"en_ece_tempcal_best\": 0.068,\n      \"temp_scaling_T\": 5.83,\n      \"zs_transfer_auroc_mean_19lang\": 0.621,\n      \"zs_transfer_auroc_median_19lang\": 0.633,\n      \"zs_transfer_auroc_std_19lang\": 0.054,\n      \"zs_transfer_drop_mean_pp\": 15.5,\n      \"zs_pass_rate_19lang\": 0.368,\n      \"zs_pass_langs\": [\n        \"zh\",\n        \"fr\",\n        \"de\",\n        \"es\",\n        \"ja\",\n        \"ru\",\n        \"ko\"\n      ],\n      \"zs_fail_langs\": [\n        \"ar\",\n        \"hi\",\n        \"sw\",\n        \"yo\",\n        \"te\",\n        \"bn\",\n        \"ta\",\n        \"th\",\n        \"vi\",\n        \"uk\",\n        \"id\",\n        \"pl\"\n      ],\n      \"mean_shift_improves_count\": 0,\n      \"mean_shift_mean_delta_ece_pp\": 3.14,\n      \"linproj_auroc_mean_19lang\": 0.648,\n      \"linproj_improves_over_zs_count\": 13,\n      \"linproj_mean_delta_auroc_vs_zs_pp\": 2.7,\n      \"fewshot25_auroc_mean_19lang\": 0.654,\n      \"fewshot25_improves_over_zs_count\": 14,\n      \"fewshot100_auroc_mean_19lang\": 0.671,\n      \"fewshot100_improves_over_zs_count\": 16,\n      \"pareto_depth_transfer_rank_corr\": 0.41,\n      \"pareto_frontier_monotonic\": false,\n      \"pareto_n_dominated_layers\": 6,\n      \"transfer_by_family\": {\n        \"indo_european_germanic\": {\n          \"mean\": 0.672,\n          \"langs\": [\n            \"de\",\n            \"en\"\n          ]\n        },\n        \"indo_european_romance\": {\n          \"mean\": 0.661,\n          \"langs\": [\n            \"fr\",\n            \"es\"\n          ]\n        },\n        \"indo_european_slavic\": {\n          \"mean\": 0.629,\n          \"langs\": [\n            \"ru\",\n            \"uk\",\n            \"pl\"\n          ]\n        },\n        \"indo_european_indic\": {\n          \"mean\": 0.598,\n          \"langs\": [\n            \"hi\",\n            \"bn\",\n            \"te\",\n            \"ta\"\n          ]\n        },\n        \"sino_tibetan\": {\n          \"mean\": 0.668,\n          \"langs\": [\n            \"zh\"\n          ]\n        },\n        \"japonic\": {\n          \"mean\": 0.651,\n          \"langs\": [\n            \"ja\"\n          ]\n        },\n        \"koreanic\": {\n          \"mean\": 0.648,\n          \"langs\": [\n            \"ko\"\n          ]\n        },\n        \"afroasiatic\": {\n          \"mean\": 0.612,\n          \"langs\": [\n            \"ar\"\n          ]\n        },\n        \"niger_congo\": {\n          \"mean\": 0.543,\n          \"langs\": [\n            \"sw\",\n            \"yo\"\n          ]\n        },\n        \"tai_kadai\": {\n          \"mean\": 0.591,\n          \"langs\": [\n            \"th\"\n          ]\n        },\n        \"austronesian\": {\n          \"mean\": 0.618,\n          \"langs\": [\n            \"id\"\n          ]\n        },\n        \"austroasiatic\": {\n          \"mean\": 0.607,\n          \"langs\": [\n            \"vi\"\n          ]\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"logreg_auroc\",\n          \"mlp_auroc\",\n          \"ece_raw\",\n          \"ece_tempcal\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.612,\n            0.618,\n            0.298,\n            0.192\n          ],\n          [\n            16,\n            17,\n            0.653,\n            0.661,\n            0.251,\n            0.148\n          ],\n          [\n            28,\n            30,\n            0.694,\n            0.708,\n            0.224,\n            0.121\n          ],\n          [\n            40,\n            43,\n            0.721,\n            0.737,\n            0.203,\n            0.098\n          ],\n          [\n            52,\n            55,\n            0.742,\n            0.755,\n            0.191,\n            0.082\n          ],\n          [\n            60,\n            64,\n            0.758,\n            0.769,\n            0.183,\n            0.075\n          ],\n          [\n            72,\n            77,\n            0.776,\n            0.783,\n            0.172,\n            0.068\n          ],\n          [\n            80,\n            85,\n            0.771,\n            0.779,\n            0.176,\n            0.071\n          ],\n          [\n            88,\n            94,\n            0.753,\n            0.762,\n            0.185,\n            0.079\n          ],\n          [\n            92,\n            98,\n            0.728,\n            0.739,\n            0.198,\n            0.091\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)\",\n        \"columns\": [\n          \"language\",\n          \"family\",\n          \"resource_tier\",\n          \"best_zs_layer\",\n          \"best_zs_auroc\",\n          \"en_auroc_at_same_layer\",\n          \"drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"sino_tibetan\",\n            \"high\",\n            52,\n            0.668,\n            0.742,\n            7.4\n          ],\n          [\n            \"fr\",\n            \"romance\",\n            \"high\",\n            52,\n            0.672,\n            0.742,\n            7.0\n          ],\n          [\n            \"de\",\n            \"germanic\",\n            \"high\",\n            52,\n            0.671,\n            0.742,\n            7.1\n          ],\n          [\n            \"es\",\n            \"romance\",\n            \"high\",\n            52,\n            0.661,\n            0.742,\n            8.1\n          ],\n          [\n            \"ja\",\n            \"japonic\",\n            \"high\",\n            48,\n            0.651,\n            0.735,\n            8.4\n          ],\n          [\n            \"ru\",\n            \"slavic\",\n            \"high\",\n            48,\n            0.644,\n            0.735,\n            9.1\n          ],\n          [\n            \"ko\",\n            \"koreanic\",\n            \"high\",\n            48,\n            0.648,\n            0.735,\n            8.7\n          ],\n          [\n            \"ar\",\n            \"afroasiatic\",\n            \"mid\",\n            40,\n            0.612,\n            0.721,\n            10.9\n          ],\n          [\n            \"hi\",\n            \"indic\",\n            \"mid\",\n            40,\n            0.618,\n            0.721,\n            10.3\n          ],\n          [\n            \"vi\",\n            \"austroasiatic\",\n            \"mid\",\n            40,\n            0.607,\n            0.721,\n            11.4\n          ],\n          [\n            \"id\",\n            \"austronesian\",\n            \"mid\",\n            40,\n            0.618,\n            0.721,\n            10.3\n          ],\n          [\n            \"th\",\n            \"tai_kadai\",\n            \"mid\",\n            40,\n            0.591,\n            0.721,\n            13.0\n          ],\n          [\n            \"pl\",\n            \"slavic\",\n            \"mid\",\n            40,\n            0.621,\n            0.721,\n            10.0\n          ],\n          [\n            \"uk\",\n            \"slavic\",\n            \"mid\",\n            40,\n            0.614,\n            0.721,\n            10.7\n          ],\n          [\n            \"bn\",\n            \"indic\",\n            \"low\",\n            28,\n            0.583,\n            0.694,\n            11.1\n          ],\n          [\n            \"te\",\n            \"indic\",\n            \"low\",\n            28,\n            0.571,\n            0.694,\n            12.3\n          ],\n          [\n            \"ta\",\n            \"indic\",\n            \"low\",\n            28,\n            0.568,\n            0.694,\n            12.6\n          ],\n          [\n            \"sw\",\n            \"niger_congo\",\n            \"low\",\n            28,\n            0.557,\n            0.694,\n            13.7\n          ],\n          [\n            \"yo\",\n            \"niger_congo\",\n            \"low\",\n            28,\n            0.529,\n            0.694,\n            16.5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean\",\n          \"auroc_std\",\n          \"pass_rate\",\n          \"ece_mean\",\n          \"delta_vs_zs_pp\"\n        ],\n        \"rows\": [\n          [\n            \"zero_shot\",\n            0.621,\n            0.054,\n            0.368,\n            0.194,\n            0.0\n          ],\n          [\n            \"mean_shift\",\n            0.604,\n            0.067,\n            0.263,\n            0.225,\n            -1.7\n          ],\n          [\n            \"linear_projection\",\n            0.648,\n            0.048,\n            0.526,\n            0.171,\n            2.7\n          ],\n          [\n            \"few_shot_25\",\n            0.654,\n            0.045,\n            0.526,\n            0.166,\n            3.3\n          ],\n          [\n            \"few_shot_100\",\n            0.671,\n            0.041,\n            0.632,\n            0.152,\n            5.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The Pareto frontier is real on Qwen3-235B but weak: rank correlation of 0.41 means the depth-transfer tradeoff explains only ~17% of variance. MoE routing creates non-monotonic perturbations at mid-depth. The practical implication is limited — the frontier provides modest guidance for layer selection but is not a reliable engineering tool. Zero-shot transfer fails for 12/19 languages (AUROC < 0.65), with a clear resource-tier gradient. The field should not assume English-trained correctness probes transfer to low-resource languages. Mean-shift is confirmed dead at scale. Linear projection and few-shot are the only viable transfer methods, with few-shot-100 achieving the best results — but requiring 100 labeled examples per language partially negates the zero-label promise.\\n\\n\\nQwen3-235B is a much larger MoE model than the MVP's Qwen2.5-7B. English AUROC at 0.776 improves modestly over MVP's 0.754 because the model is more capable and the correctness signal is more linearly accessible in larger models, but gains are sublinear — the larger model also has more complex, distributed representations that resist simple linear probing. Zero-shot transfer mean of 0.621 reflects the worst-tier prediction that transfer is unreliable: high-resource Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer adequately because their representations share more subspace structure with English at intermediate layers, but low-resource languages (sw, yo, te, bn) and languages with very different morphology (th, ta) fail because the MoE routing creates language-specific expert patterns that are opaque to an English-trained linear probe. Mean-shift fails entirely (0/19) because the mean activation difference between languages conflates content, style, and script differences — subtracting it removes useful signal. The Pareto frontier rank correlation of 0.41 is real but moderate: the general trend (deeper = better English, worse transfer) holds, but MoE routing introduces non-monotonic noise at mid-depth layers where expert activation patterns shift. The 7/19 pass rate reflects that only typologically close or high-resource languages have enough representational overlap with English for zero-shot transfer to work.\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)\",\n    \"description\": \"Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.749,\n      \"en_best_layer_idx\": 36,\n      \"en_auroc_range\": [\n        0.598,\n        0.749\n      ],\n      \"en_ece_raw_best\": 0.188,\n      \"en_ece_tempcal_best\": 0.074,\n      \"temp_scaling_T\": 5.47,\n      \"zs_transfer_auroc_mean_19lang\": 0.594,\n      \"zs_transfer_auroc_median_19lang\": 0.601,\n      \"zs_transfer_auroc_std_19lang\": 0.061,\n      \"zs_transfer_drop_mean_pp\": 18.2,\n      \"zs_pass_rate_19lang\": 0.211,\n      \"zs_pass_langs\": [\n        \"zh\",\n        \"fr\",\n        \"de\",\n        \"es\"\n      ],\n      \"zs_fail_langs\": [\n        \"ja\",\n        \"ru\",\n        \"ko\",\n        \"ar\",\n        \"hi\",\n        \"sw\",\n        \"yo\",\n        \"te\",\n        \"bn\",\n        \"ta\",\n        \"th\",\n        \"vi\",\n        \"uk\",\n        \"id\",\n        \"pl\"\n      ],\n      \"mean_shift_improves_count\": 0,\n      \"mean_shift_mean_delta_ece_pp\": 4.21,\n      \"linproj_auroc_mean_19lang\": 0.623,\n      \"linproj_improves_over_zs_count\": 11,\n      \"fewshot25_auroc_mean_19lang\": 0.631,\n      \"fewshot100_auroc_mean_19lang\": 0.652,\n      \"pareto_depth_transfer_rank_corr\": 0.22,\n      \"pareto_frontier_monotonic\": false,\n      \"pareto_n_dominated_layers\": 3,\n      \"pareto_frontier_agreement_with_qwen3\": 0.33,\n      \"nonmonotonic_layers\": [\n        20,\n        24,\n        28\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Llama 4 Scout English Probe Performance by Layer\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"logreg_auroc\",\n          \"mlp_auroc\",\n          \"ece_raw\",\n          \"ece_tempcal\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.598,\n            0.604,\n            0.312,\n            0.201\n          ],\n          [\n            8,\n            17,\n            0.631,\n            0.641,\n            0.274,\n            0.168\n          ],\n          [\n            12,\n            25,\n            0.668,\n            0.679,\n            0.241,\n            0.137\n          ],\n          [\n            16,\n            33,\n            0.694,\n            0.706,\n            0.218,\n            0.112\n          ],\n          [\n            20,\n            42,\n            0.712,\n            0.722,\n            0.205,\n            0.098\n          ],\n          [\n            24,\n            50,\n            0.726,\n            0.735,\n            0.196,\n            0.088\n          ],\n          [\n            28,\n            58,\n            0.734,\n            0.743,\n            0.192,\n            0.083\n          ],\n          [\n            32,\n            67,\n            0.741,\n            0.749,\n            0.189,\n            0.078\n          ],\n          [\n            36,\n            75,\n            0.749,\n            0.755,\n            0.188,\n            0.074\n          ],\n          [\n            40,\n            83,\n            0.744,\n            0.751,\n            0.19,\n            0.077\n          ],\n          [\n            44,\n            92,\n            0.731,\n            0.738,\n            0.195,\n            0.084\n          ],\n          [\n            48,\n            100,\n            0.708,\n            0.718,\n            0.209,\n            0.097\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language (Best Transfer Layer)\",\n        \"columns\": [\n          \"language\",\n          \"best_zs_layer\",\n          \"best_zs_auroc\",\n          \"drop_vs_en_pp\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            24,\n            0.658,\n            6.8\n          ],\n          [\n            \"fr\",\n            24,\n            0.662,\n            6.4\n          ],\n          [\n            \"de\",\n            24,\n            0.655,\n            7.1\n          ],\n          [\n            \"es\",\n            24,\n            0.651,\n            7.5\n          ],\n          [\n            \"ja\",\n            20,\n            0.631,\n            8.1\n          ],\n          [\n            \"ru\",\n            20,\n            0.622,\n            9.0\n          ],\n          [\n            \"ko\",\n            20,\n            0.627,\n            8.5\n          ],\n          [\n            \"ar\",\n            16,\n            0.589,\n            10.5\n          ],\n          [\n            \"hi\",\n            16,\n            0.594,\n            10.0\n          ],\n          [\n            \"vi\",\n            16,\n            0.581,\n            11.3\n          ],\n          [\n            \"id\",\n            16,\n            0.591,\n            10.3\n          ],\n          [\n            \"th\",\n            16,\n            0.568,\n            12.6\n          ],\n          [\n            \"pl\",\n            20,\n            0.608,\n            10.4\n          ],\n          [\n            \"uk\",\n            16,\n            0.592,\n            10.2\n          ],\n          [\n            \"bn\",\n            12,\n            0.556,\n            11.2\n          ],\n          [\n            \"te\",\n            12,\n            0.541,\n            12.7\n          ],\n          [\n            \"ta\",\n            12,\n            0.538,\n            13.0\n          ],\n          [\n            \"sw\",\n            12,\n            0.524,\n            14.4\n          ],\n          [\n            \"yo\",\n            12,\n            0.498,\n            17.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Cross-Architecture Pareto Frontier Agreement\",\n        \"columns\": [\n          \"metric\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"agreement\"\n        ],\n        \"rows\": [\n          [\n            \"rank_corr_depth_vs_transfer\",\n            0.41,\n            0.22,\n            \"—\"\n          ],\n          [\n            \"pareto_optimal_layer_count\",\n            \"6/24\",\n            \"3/12\",\n            \"—\"\n          ],\n          [\n            \"best_transfer_layer_pct_depth\",\n            \"55%\",\n            \"50%\",\n            \"—\"\n          ],\n          [\n            \"zs_mean_auroc\",\n            0.621,\n            0.594,\n            \"—\"\n          ],\n          [\n            \"optimal_layer_rank_agreement_tau\",\n            \"—\",\n            \"—\",\n            0.33\n          ],\n          [\n            \"pass_lang_overlap_jaccard\",\n            \"—\",\n            \"—\",\n            0.44\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout is the worst-tier's smoking gun for the diagnostic reframe. The Pareto frontier essentially doesn't exist on this architecture (rank corr 0.22, only 3 non-dominated layers). This is the strongest evidence for the diagnostic paper's thesis: the depth-transfer tradeoff from Claim 1 is not a universal property of transformers but an architecture-dependent phenomenon that cannot be assumed to generalize. The 0.33 cross-architecture agreement means practitioners cannot use findings from one model to guide layer selection on another. For the paper, this transforms from a weakness into a key finding: the field cannot assume probe-based calibration will behave consistently across architectures.\\n\\n\\nLlama 4 Scout is the worst-tier's key failure point. Its Pareto frontier is flat/non-monotonic (rank correlation 0.22) because Llama 4 Scout's MoE architecture uses a different routing strategy than Qwen3-235B: its experts are more language-specialized at intermediate layers, meaning the English correctness direction at layers 20-28 is entangled with English-specific expert activations in ways that neither degrade nor improve monotonically with depth. English AUROC peaks at 0.749 (lower than Qwen3's 0.776) because Llama 4 Scout's 48 layers compress the representational hierarchy — the same functional stages are packed into fewer layers, leaving less room for a clean correctness signal to emerge. Zero-shot transfer is worse overall (mean 0.594 vs Qwen3's 0.621) because Llama 4 Scout's training data distribution is more English-centric, and its MoE routing assigns non-English tokens to a sparser expert set that shares less structure with the English experts. Only 4/19 languages pass the 0.65 threshold. The 0.33 cross-architecture Pareto agreement means the optimal layer for a given language on Qwen3 does not predict the optimal layer on Llama 4 — the tradeoff is architecture-specific, not a universal property of transformer depth.\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency). Train CaCLR probes using English labels + unlabeled parallel activations. Compare vs all 5 transfer conditions across full Pareto frontier for both models × 20 languages.\\n\",\n    \"results\": {\n      \"caclr_auroc_mean_qwen3\": 0.645,\n      \"caclr_auroc_mean_llama4\": 0.618,\n      \"caclr_vs_linproj_auroc_delta_pp_qwen3\": -0.3,\n      \"caclr_vs_linproj_auroc_delta_pp_llama4\": -0.5,\n      \"caclr_vs_zs_auroc_delta_pp_qwen3\": 2.4,\n      \"caclr_vs_zs_auroc_delta_pp_llama4\": 2.4,\n      \"caclr_vs_fewshot100_auroc_delta_pp_qwen3\": -2.6,\n      \"caclr_vs_fewshot100_auroc_delta_pp_llama4\": -3.4,\n      \"caclr_improvement_pass_rate_qwen3\": 0.47,\n      \"caclr_improvement_pass_rate_llama4\": 0.37,\n      \"caclr_ece_mean_qwen3\": 0.174,\n      \"caclr_ece_mean_llama4\": 0.189,\n      \"caclr_ece_reduction_vs_tempcal_pct_qwen3\": 7.2,\n      \"caclr_ece_reduction_vs_tempcal_pct_llama4\": 3.8,\n      \"best_alpha\": 0.3,\n      \"best_beta\": 0.05,\n      \"alpha_sensitivity\": \"moderate — ±0.1 changes AUROC by ~0.5pp\",\n      \"beta_sensitivity\": \"flat — β from 0.01 to 0.5 changes AUROC by <0.3pp, indicating consistency loss is inert\",\n      \"caclr_no_consistency_auroc_mean\": 0.647,\n      \"caclr_no_sbece_auroc_mean\": 0.629,\n      \"caclr_bce_only_auroc_mean\": 0.621,\n      \"caclr_per_lang_qwen3\": {\n        \"zh\": {\n          \"auroc\": 0.671,\n          \"delta_vs_zs\": 0.3,\n          \"delta_vs_linproj\": -0.8\n        },\n        \"fr\": {\n          \"auroc\": 0.668,\n          \"delta_vs_zs\": -0.4,\n          \"delta_vs_linproj\": -1.2\n        },\n        \"de\": {\n          \"auroc\": 0.665,\n          \"delta_vs_zs\": -0.6,\n          \"delta_vs_linproj\": -0.9\n        },\n        \"es\": {\n          \"auroc\": 0.658,\n          \"delta_vs_zs\": -0.3,\n          \"delta_vs_linproj\": -0.7\n        },\n        \"ja\": {\n          \"auroc\": 0.649,\n          \"delta_vs_zs\": -0.2,\n          \"delta_vs_linproj\": -0.4\n        },\n        \"ru\": {\n          \"auroc\": 0.641,\n          \"delta_vs_zs\": -0.3,\n          \"delta_vs_linproj\": -0.6\n        },\n        \"ko\": {\n          \"auroc\": 0.647,\n          \"delta_vs_zs\": -0.1,\n          \"delta_vs_linproj\": -0.3\n        },\n        \"ar\": {\n          \"auroc\": 0.628,\n          \"delta_vs_zs\": 1.6,\n          \"delta_vs_linproj\": 0.2\n        },\n        \"hi\": {\n          \"auroc\": 0.635,\n          \"delta_vs_zs\": 1.7,\n          \"delta_vs_linproj\": 0.1\n        },\n        \"vi\": {\n          \"auroc\": 0.621,\n          \"delta_vs_zs\": 1.4,\n          \"delta_vs_linproj\": -0.3\n        },\n        \"id\": {\n          \"auroc\": 0.633,\n          \"delta_vs_zs\": 1.5,\n          \"delta_vs_linproj\": -0.1\n        },\n        \"th\": {\n          \"auroc\": 0.607,\n          \"delta_vs_zs\": 1.6,\n          \"delta_vs_linproj\": 0.3\n        },\n        \"pl\": {\n          \"auroc\": 0.638,\n          \"delta_vs_zs\": 1.7,\n          \"delta_vs_linproj\": 0.1\n        },\n        \"uk\": {\n          \"auroc\": 0.631,\n          \"delta_vs_zs\": 1.7,\n          \"delta_vs_linproj\": 0.2\n        },\n        \"bn\": {\n          \"auroc\": 0.601,\n          \"delta_vs_zs\": 1.8,\n          \"delta_vs_linproj\": 0.5\n        },\n        \"te\": {\n          \"auroc\": 0.589,\n          \"delta_vs_zs\": 1.8,\n          \"delta_vs_linproj\": 0.4\n        },\n        \"ta\": {\n          \"auroc\": 0.587,\n          \"delta_vs_zs\": 1.9,\n          \"delta_vs_linproj\": 0.6\n        },\n        \"sw\": {\n          \"auroc\": 0.578,\n          \"delta_vs_zs\": 2.1,\n          \"delta_vs_linproj\": 0.9\n        },\n        \"yo\": {\n          \"auroc\": 0.551,\n          \"delta_vs_zs\": 2.2,\n          \"delta_vs_linproj\": 0.7\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Transfer Method Comparison Summary (19-Language Mean, Both Architectures)\",\n        \"columns\": [\n          \"method\",\n          \"qwen3_auroc\",\n          \"qwen3_ece\",\n          \"llama4_auroc\",\n          \"llama4_ece\",\n          \"labels_needed\"\n        ],\n        \"rows\": [\n          [\n            \"zero_shot\",\n            0.621,\n            0.194,\n            0.594,\n            0.212,\n            \"0 target\"\n          ],\n          [\n            \"mean_shift\",\n            0.604,\n            0.225,\n            0.571,\n            0.248,\n            \"0 target (fails)\"\n          ],\n          [\n            \"linear_projection\",\n            0.648,\n            0.171,\n            0.623,\n            0.189,\n            \"~50 parallel\"\n          ],\n          [\n            \"CaCLR\",\n            0.645,\n            0.174,\n            0.618,\n            0.193,\n            \"0 target + parallel\"\n          ],\n          [\n            \"few_shot_25\",\n            0.654,\n            0.166,\n            0.631,\n            0.182,\n            \"25 target\"\n          ],\n          [\n            \"few_shot_100\",\n            0.671,\n            0.152,\n            0.652,\n            0.168,\n            \"100 target\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)\",\n        \"columns\": [\n          \"variant\",\n          \"auroc_mean\",\n          \"ece_mean\",\n          \"delta_vs_full_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Full CaCLR (BCE+SB-ECE+Consistency)\",\n            0.645,\n            0.174,\n            0.0\n          ],\n          [\n            \"CaCLR − Consistency (BCE+SB-ECE)\",\n            0.647,\n            0.172,\n            0.2\n          ],\n          [\n            \"CaCLR − SB-ECE (BCE+Consistency)\",\n            0.629,\n            0.188,\n            -1.6\n          ],\n          [\n            \"BCE Only (= zero-shot probe)\",\n            0.621,\n            0.194,\n            -2.4\n          ],\n          [\n            \"Linear Projection\",\n            0.648,\n            0.171,\n            0.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR is a rigorous negative result. The consistency loss term — the core methodological novelty — is inert. This is not a hyperparameter tuning failure; β is swept over 3 orders of magnitude and the landscape is flat. The SB-ECE term provides modest calibration regularization, but this benefit is available without any cross-lingual machinery. Linear projection achieves the same or better results with a simpler mechanism. For the paper, this is framed as: \\\"consistency-based cross-lingual alignment objectives do not help when the underlying correctness signal has low cross-lingual SNR. This negative result saves the community from pursuing distributional-matching approaches (adversarial, MMD, consistency) for this problem class.\\\"\\n\\n\\nCaCLR's consistency loss (L_consistency) is designed to align cross-lingual probe activations so that the English probe generalizes. In the worst tier, this fails because the cross-lingual correctness signal is too noisy for the consistency objective to find meaningful invariances. The unlabeled parallel activations contain language-specific variance (script, morphology, tokenization artifacts) that dominates the correctness signal, so minimizing distributional distance between languages collapses both signal and noise. The hyperparameter search confirms this: β (consistency weight) is driven to near-zero (0.05), and removing the consistency term entirely slightly improves performance (+0.2pp). The SB-ECE term helps modestly because it acts as a calibration regularizer on the English side, but this benefit doesn't compound with consistency. CaCLR ends up being essentially \\\"zero-shot + SB-ECE regularization\\\" — functionally a slightly calibration-aware version of the base probe. Linear projection beats CaCLR because projection directly estimates and applies the affine transformation between language representation subspaces, which is a more efficient use of the few available parallel datapoints than trying to learn an invariant representation. The key insight: simple alignment (linproj) outperforms principled invariance (CaCLR) when the signal-to-noise ratio of the target signal is low. For high-resource languages that already transfer well, CaCLR's overhead yields no benefit; for low-resource languages where help is needed, the consistency signal is too noisy to learn from.\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation (Decomposition)\",\n    \"description\": \"Train IRT difficulty probes, project out difficulty direction from activations, retrain correctness probes on residuals, evaluate transfer. 10 representative languages × 8 representative layers per model.\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_en_qwen3\": 0.52,\n      \"difficulty_probe_r2_en_llama4\": 0.47,\n      \"difficulty_probe_transfer_r2_mean_9lang\": 0.41,\n      \"decomp_difficulty_var_explained_pct_qwen3\": 14.3,\n      \"decomp_difficulty_var_explained_pct_llama4\": 11.8,\n      \"correctness_residual_auroc_en_qwen3\": 0.738,\n      \"correctness_residual_auroc_en_llama4\": 0.711,\n      \"correctness_residual_transfer_auroc_mean_qwen3\": 0.607,\n      \"correctness_residual_transfer_auroc_mean_llama4\": 0.581,\n      \"transfer_improvement_after_projection\": false,\n      \"transfer_delta_after_projection_pp_qwen3\": -1.4,\n      \"transfer_delta_after_projection_pp_llama4\": -1.3,\n      \"difficulty_correctness_cosine_mean_qwen3\": 0.34,\n      \"difficulty_correctness_cosine_mean_llama4\": 0.38,\n      \"difficulty_correctness_cosine_std\": 0.11,\n      \"subspace_overlap_mean_angle_deg\": 58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Difficulty Probe Quality (Ridge Regression, R² on Held-Out)\",\n        \"columns\": [\n          \"language\",\n          \"qwen3_r2\",\n          \"llama4_r2\",\n          \"is_transfer\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            0.52,\n            0.47,\n            false\n          ],\n          [\n            \"zh\",\n            0.48,\n            0.43,\n            true\n          ],\n          [\n            \"fr\",\n            0.47,\n            0.42,\n            true\n          ],\n          [\n            \"de\",\n            0.46,\n            0.41,\n            true\n          ],\n          [\n            \"ar\",\n            0.42,\n            0.37,\n            true\n          ],\n          [\n            \"hi\",\n            0.41,\n            0.36,\n            true\n          ],\n          [\n            \"ja\",\n            0.44,\n            0.39,\n            true\n          ],\n          [\n            \"ko\",\n            0.43,\n            0.38,\n            true\n          ],\n          [\n            \"sw\",\n            0.33,\n            0.28,\n            true\n          ],\n          [\n            \"yo\",\n            0.29,\n            0.24,\n            true\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Decomposition Transfer Ablation (9-Language Mean)\",\n        \"columns\": [\n          \"condition\",\n          \"qwen3_auroc\",\n          \"qwen3_delta_pp\",\n          \"llama4_auroc\",\n          \"llama4_delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Full activations (baseline)\",\n            0.621,\n            0.0,\n            0.594,\n            0.0\n          ],\n          [\n            \"Residual (difficulty projected out)\",\n            0.607,\n            -1.4,\n            0.581,\n            -1.3\n          ],\n          [\n            \"Difficulty component only\",\n            0.568,\n            -5.3,\n            0.551,\n            -4.3\n          ],\n          [\n            \"Random direction projected out (ctrl)\",\n            0.618,\n            -0.3,\n            0.591,\n            -0.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition fails as a prescriptive tool. The difficulty-shared component, far from being a confound, is actually one of the more reliable cross-lingual bridges — removing it hurts. The capability-specific residual is more language-dependent, not less, because it captures idiosyncratic encoding patterns. For the diagnostic paper, this finding is reframed as: \\\"difficulty and capability are entangled in multilingual representations, unlike the clean separation reported in English-only work. This entanglement may be fundamental to how multilingual models represent knowledge — the shared difficulty structure is load-bearing for cross-lingual transfer, not a confound to be controlled for.\\\"\\n\\n\\nIn the worst tier, difficulty and capability are entangled in cross-lingual representations. The difficulty direction explains only 14% (Qwen3) / 12% (Llama4) of correctness probe variance — real but modest. Critically, projecting out difficulty makes transfer WORSE (-1.3 to -1.4pp), not better. This is because the difficulty-shared component actually carries useful cross-lingual signal: questions that are hard in English tend to be hard everywhere due to shared conceptual complexity, and this shared difficulty signal is one of the few reliable cross-lingual bridges for the correctness probe. Removing it strips away a genuine cross-lingual invariance. The residual \\\"capability-specific\\\" component is more language-dependent, not less — it contains the idiosyncratic ways each language's tokens encode competence, which are precisely the non-transferable signals. The cosine similarity of 0.34-0.38 between difficulty and correctness directions confirms they are neither orthogonal nor aligned — they share a moderate subspace that cannot be cleanly separated. This contradicts the paper's original Claim 2 hypothesis that decomposition would be prescriptive. The decomposition is real but useless: it describes variance structure without enabling better transfer.\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Extract verbalized confidence direction, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\\n\",\n    \"results\": {\n      \"orthogonality_cosine_mean_overall\": 0.072,\n      \"orthogonality_cosine_std_overall\": 0.038,\n      \"orthogonality_cosine_mean_qwen3\": 0.068,\n      \"orthogonality_cosine_mean_llama4\": 0.076,\n      \"orthogonality_cosine_range\": [\n        0.018,\n        0.148\n      ],\n      \"orthogonality_cosine_high_resource\": 0.054,\n      \"orthogonality_cosine_mid_resource\": 0.071,\n      \"orthogonality_cosine_low_resource\": 0.098,\n      \"pct_langs_cosine_below_0_1\": 0.75,\n      \"pct_langs_cosine_below_0_05\": 0.35,\n      \"confidence_probe_r2_mean\": 0.68,\n      \"confidence_probe_transfer_drops\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Correctness-Confidence Cosine Similarity by Language\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"qwen3_cosine\",\n          \"llama4_cosine\",\n          \"mean_cosine\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"high\",\n            0.038,\n            0.041,\n            0.04\n          ],\n          [\n            \"zh\",\n            \"high\",\n            0.042,\n            0.049,\n            0.046\n          ],\n          [\n            \"fr\",\n            \"high\",\n            0.045,\n            0.051,\n            0.048\n          ],\n          [\n            \"de\",\n            \"high\",\n            0.047,\n            0.054,\n            0.051\n          ],\n          [\n            \"es\",\n            \"high\",\n            0.049,\n            0.056,\n            0.053\n          ],\n          [\n            \"ja\",\n            \"high\",\n            0.055,\n            0.062,\n            0.059\n          ],\n          [\n            \"ru\",\n            \"high\",\n            0.058,\n            0.064,\n            0.061\n          ],\n          [\n            \"ko\",\n            \"high\",\n            0.061,\n            0.068,\n            0.065\n          ],\n          [\n            \"ar\",\n            \"mid\",\n            0.063,\n            0.072,\n            0.068\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.065,\n            0.075,\n            0.07\n          ],\n          [\n            \"vi\",\n            \"mid\",\n            0.068,\n            0.077,\n            0.073\n          ],\n          [\n            \"id\",\n            \"mid\",\n            0.064,\n            0.073,\n            0.069\n          ],\n          [\n            \"th\",\n            \"mid\",\n            0.072,\n            0.082,\n            0.077\n          ],\n          [\n            \"pl\",\n            \"mid\",\n            0.059,\n            0.067,\n            0.063\n          ],\n          [\n            \"uk\",\n            \"mid\",\n            0.062,\n            0.071,\n            0.067\n          ],\n          [\n            \"bn\",\n            \"low\",\n            0.081,\n            0.092,\n            0.087\n          ],\n          [\n            \"te\",\n            \"low\",\n            0.088,\n            0.098,\n            0.093\n          ],\n          [\n            \"ta\",\n            \"low\",\n            0.091,\n            0.103,\n            0.097\n          ],\n          [\n            \"sw\",\n            \"low\",\n            0.098,\n            0.112,\n            0.105\n          ],\n          [\n            \"yo\",\n            \"low\",\n            0.112,\n            0.148,\n            0.13\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Orthogonality by Resource Tier (Mean Cosine ± Std)\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"qwen3_mean\",\n          \"llama4_mean\",\n          \"overall_mean\",\n          \"std\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            8,\n            0.049,\n            0.056,\n            0.054,\n            0.009\n          ],\n          [\n            \"mid\",\n            7,\n            0.065,\n            0.074,\n            0.071,\n            0.005\n          ],\n          [\n            \"low\",\n            5,\n            0.094,\n            0.111,\n            0.098,\n            0.016\n          ],\n          [\n            \"all\",\n            20,\n            0.066,\n            0.076,\n            0.072,\n            0.022\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 4 survives in the worst tier but its contribution is incremental. Orthogonality persists (mean 0.072, all < 0.15) — output-based calibration is indeed structurally limited everywhere. The resource-tier gradient (high: 0.054, mid: 0.071, low: 0.098) is novel but the effect size is modest. The correlation between orthogonality and transfer success is intriguing but not causal. For the diagnostic paper, this is framed as the one mechanistic takeaway: \\\"the correctness-confidence dissociation is a multilingual phenomenon, confirming that output-based calibration methods face a structural ceiling regardless of language. However, this ceiling is slightly lower for low-resource languages, suggesting that the dissociation partly reflects representation quality rather than a pure architectural invariant.\\\"\\n\\n\\nOrthogonality persists cross-lingually (mean cosine 0.072, all languages below 0.15) because it is a structural property of how LLMs represent confidence vs correctness — the model's verbalized confidence is calibrated to appear confident regardless of actual correctness, and this dissociation is encoded geometrically at the representation level. However, the worst-tier variance is higher than Miao & Ungar's English-only finding (std 0.038 vs their ~0.01): low-resource languages show less orthogonality (cosine ~0.098) because the model has less capacity to maintain the confidence-correctness dissociation for languages with limited training data — when the model is uncertain due to lack of language-specific knowledge, both its correctness and confidence signals degrade in correlated ways, slightly breaking orthogonality. Reviewers may see this as incremental: Miao & Ungar showed orthogonality for English, we extend to 20 languages, but the finding is qualitatively the same. The resource- tier modulation is the one novel angle but the effect size is modest (0.054 vs 0.098).\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Compare logistic regression vs 2-layer MLP at each probed layer for both models. Test hypothesis that linear probes transfer better cross-lingually.\\n\",\n    \"results\": {\n      \"mlp_vs_logreg_en_auroc_delta_mean_pp_qwen3\": 1.1,\n      \"mlp_vs_logreg_en_auroc_delta_mean_pp_llama4\": 0.9,\n      \"mlp_vs_logreg_transfer_auroc_delta_mean_pp_qwen3\": -0.4,\n      \"mlp_vs_logreg_transfer_auroc_delta_mean_pp_llama4\": -0.2,\n      \"hypothesis_linear_transfers_better\": \"weak support\",\n      \"effect_size_cohens_d\": 0.18,\n      \"mlp_advantage_shallow_layers_pp\": 0.6,\n      \"mlp_advantage_deep_layers_pp\": 1.4,\n      \"logreg_transfer_advantage_shallow_pp\": 0.1,\n      \"logreg_transfer_advantage_deep_pp\": 0.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Probe Complexity Comparison (Mean Across All Layers)\",\n        \"columns\": [\n          \"model\",\n          \"probe\",\n          \"en_auroc_mean\",\n          \"transfer_auroc_mean\",\n          \"en_ece_mean\",\n          \"transfer_ece_mean\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3\",\n            \"logreg\",\n            0.714,\n            0.621,\n            0.206,\n            0.194\n          ],\n          [\n            \"qwen3\",\n            \"mlp\",\n            0.725,\n            0.617,\n            0.198,\n            0.197\n          ],\n          [\n            \"llama4\",\n            \"logreg\",\n            0.697,\n            0.594,\n            0.219,\n            0.212\n          ],\n          [\n            \"llama4\",\n            \"mlp\",\n            0.706,\n            0.592,\n            0.212,\n            0.214\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Probe complexity is a non-finding. The effect is real but negligible (Cohen's d 0.18). Logistic regression is the correct default choice: nearly identical performance with fewer hyperparameters and better interpretability. This goes into the supplementary as a methods validation, not a main finding.\\n\\n\\nThe hypothesis that linear probes transfer better receives only weak support. MLP probes are ~1pp better in English because the 2-layer MLP captures mild nonlinearities in the correctness signal (interaction effects between representation dimensions). But the cross-lingual transfer difference is tiny (-0.2 to -0.4pp favoring logistic regression) and inconsistent across languages and layers — Cohen's d of 0.18 means the effect would be invisible without large sample sizes. The interaction with depth is the most interesting signal: at deep layers, MLP probes overfit to English-specific patterns more (1.4pp English advantage) and consequently transfer worse (0.7pp transfer penalty). But even this effect is too small to be practically actionable. For the paper, this confirms logistic regression as the appropriate probe choice (simpler, nearly as good) but doesn't generate a standalone finding.\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and MMLU-ProX (translated MMLU, 20 languages).\\n\",\n    \"results\": {\n      \"belebele_en_auroc_qwen3\": 0.741,\n      \"belebele_en_auroc_llama4\": 0.718,\n      \"belebele_zs_transfer_mean_qwen3\": 0.598,\n      \"belebele_zs_transfer_mean_llama4\": 0.572,\n      \"belebele_drop_vs_globalmmlu_pp\": 2.3,\n      \"belebele_caclr_delta_vs_linproj_pp\": -0.6,\n      \"mmlupx_en_auroc_qwen3\": 0.762,\n      \"mmlupx_en_auroc_llama4\": 0.738,\n      \"mmlupx_zs_transfer_mean_qwen3\": 0.583,\n      \"mmlupx_zs_transfer_mean_llama4\": 0.557,\n      \"mmlupx_drop_vs_globalmmlu_pp\": 3.8,\n      \"mmlupx_caclr_delta_vs_linproj_pp\": -0.9,\n      \"lang_rank_correlation_globalmmlu_vs_belebele\": 0.82,\n      \"lang_rank_correlation_globalmmlu_vs_mmlupx\": 0.71\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Cross-Benchmark Generalization (19-Language Mean)\",\n        \"columns\": [\n          \"benchmark\",\n          \"metric\",\n          \"qwen3\",\n          \"llama4\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            \"zs_transfer_auroc\",\n            0.621,\n            0.594\n          ],\n          [\n            \"Belebele\",\n            \"zs_transfer_auroc\",\n            0.598,\n            0.572\n          ],\n          [\n            \"MMLU-ProX\",\n            \"zs_transfer_auroc\",\n            0.583,\n            0.557\n          ],\n          [\n            \"GlobalMMLU\",\n            \"caclr_vs_linproj_pp\",\n            -0.3,\n            -0.5\n          ],\n          [\n            \"Belebele\",\n            \"caclr_vs_linproj_pp\",\n            -0.6,\n            -0.8\n          ],\n          [\n            \"MMLU-ProX\",\n            \"caclr_vs_linproj_pp\",\n            -0.9,\n            -1.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Results partially generalize: Belebele confirms the main findings, MMLU-ProX is noisier due to translation artifacts. The language ranking is stable across benchmarks (which languages transfer well vs poorly is consistent), but absolute performance degrades with benchmark domain shift. CaCLR's negative result is robust across all three benchmarks — it never beats linear projection. For the paper, include Belebele in the main results and MMLU-ProX in supplementary with a note about translation artifacts.\\n\\n\\nBelebele partially replicates GlobalMMLU findings because it is also a high-quality, natively multilingual benchmark where translation artifacts are minimal. The 2.3pp drop reflects the domain shift (reading comprehension vs knowledge questions) but the relative ranking of languages is preserved (rank corr 0.82). MMLU-ProX shows worse transfer (3.8pp drop) because it is machine-translated from English MMLU — translation artifacts create systematic distributional shifts that the English-trained correctness probe cannot handle. The translation introduces new failure modes: ambiguous translations for domain-specific terms, cultural references that don't transfer, and occasional errors in low-resource translations. CaCLR is again no better than linear projection on either benchmark, confirming the negative result generalizes beyond the training benchmark.\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset. Validate that INT8 quantization doesn't distort correctness signals.\\n\",\n    \"results\": {\n      \"int8_vs_fp16_auroc_delta_mean_pp\": -0.3,\n      \"int8_vs_fp16_auroc_delta_max_pp\": -0.7,\n      \"int8_vs_fp16_ece_delta_mean_pp\": 0.2,\n      \"int8_vs_fp16_activation_cosine_sim_mean\": 0.994,\n      \"int8_vs_fp16_rank_correlation_layers\": 0.98,\n      \"validation_passes\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1 (supplementary): INT8 vs FP16 Probing Comparison\",\n        \"columns\": [\n          \"layer\",\n          \"fp16_auroc\",\n          \"int8_auroc\",\n          \"delta_pp\",\n          \"activation_cosine\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.637,\n            0.633,\n            -0.4,\n            0.993\n          ],\n          [\n            16,\n            0.7,\n            0.697,\n            -0.3,\n            0.994\n          ],\n          [\n            24,\n            0.731,\n            0.729,\n            -0.2,\n            0.995\n          ],\n          [\n            32,\n            0.746,\n            0.743,\n            -0.3,\n            0.994\n          ],\n          [\n            40,\n            0.748,\n            0.741,\n            -0.7,\n            0.992\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8 validation passes. Quantization is not a confound for any findings in this paper. Include in supplementary appendix as one paragraph + Table S1.\\n\\n\\nINT8 quantization introduces minimal distortion to correctness signals. The 0.3pp mean AUROC difference is within noise — INT8 preserves the relative ordering of activations that linear probes rely on, even though absolute magnitudes shift slightly. The 0.994 cosine similarity between INT8 and FP16 activations confirms near-perfect directional alignment. This is expected because correctness is encoded in the direction of activations, not their magnitude, and INT8 preserves directions well. The layer ranking is identical (rank corr 0.98). This ablation passes cleanly even in the worst tier — quantization artifacts are not the source of any failures observed elsewhere.\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture (Camera-Ready)\",\n    \"description\": \"Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense architecture, FP16). Provides dense-vs-MoE architectural contrast for camera-ready extension.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.761,\n      \"en_best_layer_idx\": 45,\n      \"zs_transfer_auroc_mean_19lang\": 0.608,\n      \"zs_transfer_drop_mean_pp\": 16.8,\n      \"pareto_depth_transfer_rank_corr\": 0.48,\n      \"pareto_frontier_agreement_with_qwen3\": 0.42,\n      \"pareto_frontier_agreement_with_llama4\": 0.29,\n      \"caclr_vs_linproj_pp\": -0.2,\n      \"dense_vs_moe_finding\": \"Dense architecture shows cleaner Pareto frontier (rank corr 0.48 vs 0.41/0.22 for MoE models) — MoE routing is a source of non-monotonic noise in the depth-transfer relationship\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Three-Architecture Comparison Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_auroc\",\n          \"transfer_auroc\",\n          \"pareto_rank_corr\",\n          \"pareto_agreement_mean\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE\",\n            94,\n            0.776,\n            0.621,\n            0.41,\n            0.38\n          ],\n          [\n            \"Llama4-Scout\",\n            \"MoE\",\n            48,\n            0.749,\n            0.594,\n            0.22,\n            0.31\n          ],\n          [\n            \"Gemma4-31B\",\n            \"Dense\",\n            60,\n            0.761,\n            0.608,\n            0.48,\n            0.36\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma4 confirms the diagnostic paper's thesis from a new angle: the Pareto frontier is more coherent in dense architectures, implicating MoE routing as a specific source of cross-lingual transfer noise. For camera-ready, this strengthens the \\\"architecture matters\\\" message without changing the core worst-tier narrative.\\n\\n\\nGemma 4 31B Dense shows a cleaner (but still moderate) Pareto frontier because dense architectures have more homogeneous layer-to-layer representation transformations — no expert routing to create non-monotonic jumps. The rank correlation of 0.48 is the highest of the three architectures but still in the worst tier range. English AUROC of 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent with its intermediate model size. Transfer is intermediate too (0.608). Cross-architecture agreement remains low (0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence. The dense-vs-MoE contrast is the main value-add for camera-ready: it demonstrates that MoE routing is a specific source of frontier noise, not just model variation.\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages, Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_transfer_auroc_mean_51lang\": 0.587,\n      \"zs_pass_rate_51lang\": 0.235,\n      \"new_lang_families_added\": 5,\n      \"low_resource_auroc_mean_new_langs\": 0.548,\n      \"worst_language_auroc\": 0.491,\n      \"resource_tier_gradient_steeper\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Transfer Success by Resource Tier (Expanded 52-Language Set, Qwen3)\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"zs_auroc_mean\",\n          \"zs_auroc_std\",\n          \"pass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            10,\n            0.653,\n            0.018,\n            0.7\n          ],\n          [\n            \"mid\",\n            18,\n            0.603,\n            0.024,\n            0.28\n          ],\n          [\n            \"low\",\n            14,\n            0.558,\n            0.031,\n            0.07\n          ],\n          [\n            \"very_low\",\n            10,\n            0.521,\n            0.022,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extended coverage is the nail in the coffin for universal probe-based calibration. With 52 languages, the majority fail to transfer. The resource-tier gradient is steep and monotonic. This is the strongest evidence for the diagnostic paper's conclusion: \\\"this research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\\\"\\n\\nExpanding to 50+ languages worsens the aggregate picture because the additional languages are predominantly low- and very-low-resource. Many of these languages (e.g., Amharic, Lao, Mongolian, Georgian) have minimal representation in the models' training data, so their internal representations share even less structure with English. The pass rate drops from ~37% (7/19) to ~24% (12/51), and some languages approach chance (AUROC ~0.49). For the paper, this strengthens the diagnostic message: \\\"probe-based calibration has a severe language barrier that scales with the number of languages you try to cover.\\\"\\n\"\n  }\n]",
      "numLines": 1722,
      "startLine": 1,
      "totalLines": 1722
    }
  },
  "sourceToolAssistantUUID": "1631f04d-9faa-49d6-90e6-58eb18f6223b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "adad38cf-e086-425e-8157-55862e38b1f8",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate multilingual calibration diagnostic paper",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Assistant

_source line 15 · 2026-05-20T19:33:12.744Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me synthesize the experiment data and paper framing to write a complete LaTeX paper. The narrative guidance says this should be framed as a field-level diagnostic paper: "Does probe-based calibration work beyond English?" with negative results as the main contribution.

Key points from the narrative guidance:
1. Full reframe to field-level diagnostic paper
2. CaCLR reported as rigorous negative result
3. Decomposition reported as evidence of entanglement contradicting English-only prior work
4. Pareto frontier real on Qwen3 but fails on Llama 4 Scout — architecture-dependence


5. Orthogonality survives as a mechanistic finding worth reporting
6. Target EACL

Now I'm mapping out the paper structure: abstract, introduction, related work, then the methods section covering the probing setup, transfer conditions, CaCLR, decomposition, and orthogonality measurement. The experiments section will walk through English probe performance, zero-shot transfer results, transfer method comparisons, Pareto frontier analysis, and CaCLR evaluation across the different model and language combinations.

I've got a lot of experimental results to fit in—decomposition analysis, cross-lingual orthogonality patterns, probe complexity studies, cross-benchmark generalization, comparisons across three architectures, extended language coverage, plus INT8 validation in the appendix. The challenge is including all these experiments while keeping the paper readable, so I'll need to be strategic about condensing some tables and grouping related findings together rather than presenting each one separately. Writing the paper in ACL format...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adad38cf-e086-425e-8157-55862e38b1f8",
  "isSidechain": false,
  "requestId": "req_011CbENw4Q8R99Vf3jycFMUi",
  "type": "assistant",
  "uuid": "625c1558-d4d2-405c-b8a6-70455e03ed7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcLNrXobj4tbgUbke1djfe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 20584,
      "cache_read_input_tokens": 23416,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1710,
          "output_tokens": 962,
          "cache_read_input_tokens": 23416,
          "cache_creation_input_tokens": 20584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20584
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

_source line 16 · 2026-05-20T19:33:12.747Z_

Now let me check that the output directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "625c1558-d4d2-405c-b8a6-70455e03ed7c",
  "isSidechain": false,
  "requestId": "req_011CbENw4Q8R99Vf3jycFMUi",
  "type": "assistant",
  "uuid": "d27e9caa-d3ce-4c0c-857d-c2287e93584a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcLNrXobj4tbgUbke1djfe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 20584,
      "cache_read_input_tokens": 23416,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1710,
          "output_tokens": 962,
          "cache_read_input_tokens": 23416,
          "cache_creation_input_tokens": 20584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20584
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

_source line 17 · 2026-05-20T19:33:14.671Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R5s3kSzKZBWMnPMQMjfMJp`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d27e9caa-d3ce-4c0c-857d-c2287e93584a",
  "isSidechain": false,
  "requestId": "req_011CbENw4Q8R99Vf3jycFMUi",
  "type": "assistant",
  "uuid": "e6b55032-8a01-4183-a0c4-9180f85f84e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcLNrXobj4tbgUbke1djfe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 20584,
      "cache_read_input_tokens": 23416,
      "output_tokens": 962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1710,
          "output_tokens": 962,
          "cache_read_input_tokens": 23416,
          "cache_creation_input_tokens": 20584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20584
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

_source line 18 · 2026-05-20T19:33:14.819Z_

<details><summary>↩ Tool result · `toolu_01R5s3kSzKZBWMnPMQMjfMJp`</summary>

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
  "parentUuid": "e6b55032-8a01-4183-a0c4-9180f85f84e6",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "8afa4bfa-cf49-466d-953c-552c3ce131c3",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e6b55032-8a01-4183-a0c4-9180f85f84e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:36:26.113Z_

<details open><summary>🔧 Tool call — Write · `toolu_012o1QmLHLsaK5tGZP2RrBwH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\pareto}{Pareto}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{Does Probe-Based Calibration Work Beyond English?\\\\A Systematic Study Across 3 Architectures and 52 Languages}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration---training linear probes on internal representations to predict answer correctness---has emerged as a promising alternative to output-based calibration for LLMs.\nHowever, all existing work validates exclusively in English.\nWe present the first large-scale study of whether this research line generalizes cross-lingually, evaluating correctness probes across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), up to 52 languages, and 5 transfer conditions on GlobalMMLU, Belebele, and MMLU-ProX.\nOur findings are predominantly negative.\n(1)~English-trained probes fail to transfer to 12 of 19 target languages in zero-shot on Qwen3-235B, with a clear resource-tier gradient.\n(2)~The depth--transferability Pareto frontier is architecture-dependent: moderate on Qwen3 ($\\rho{=}0.41$), negligible on Llama~4 Scout ($\\rho{=}0.22$), with only $0.33$ cross-architecture agreement.\n(3)~CaCLR, a consistency-based training objective, provides no benefit over simple linear projection---the consistency loss is inert across $3$ orders of magnitude of its weight.\n(4)~Difficulty and capability are entangled in multilingual representations: projecting out difficulty \\emph{hurts} transfer by $1.3$--$1.4$~pp, contradicting the clean separation assumed by English-only prior work.\nThe one positive finding is that correctness--confidence orthogonality persists across all 20 languages (mean cosine $0.072$), confirming output-based calibration is structurally limited regardless of language.\nThese results establish that probe-based calibration requires fundamental methodological advances before it can serve non-English users.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n%------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying LLMs in high-stakes settings.\nFor non-English languages, the calibration problem is acute: multilingual LLMs exhibit substantially worse calibration outside English, yet the vast majority of calibration research targets English exclusively.\n\nA recent line of work proposes \\emph{probe-based calibration}: training linear probes on internal model representations to predict whether a given answer is correct \\citep{miao-etal-2024-coral,burns2023discovering,miao-ungar-2026}.\nThese probes access a ``correctness direction'' in representation space that is orthogonal to the model's verbalized confidence, offering calibration signals unavailable to output-based methods like temperature scaling.\nResults in English are promising, but a fundamental question remains unanswered: \\emph{does this approach work for non-English languages?}\n\nThis question is not merely academic.\nThe field is actively expanding probe-based methods---from single-task to cross-task transfer \\citep{miao-etal-2024-coral}, from probing to representation steering \\citep{miao-ungar-2026}, and from English to multilingual knowledge-boundary probes \\citep{xiao-etal-2025}.\nYet no work has tested whether the correctness direction itself transfers across languages in a calibration-relevant manner.\n\nWe conduct the first systematic study of cross-lingual probe-based calibration, spanning 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, and CaCLR---a novel consistency-based objective).\nOur study is designed as a field-level diagnostic: regardless of whether results are positive or negative, they answer whether this research line generalizes.\n\nOur main findings are:\n\\begin{itemize}\n\\item \\textbf{Transfer largely fails.} Zero-shot probe transfer succeeds for only 7 of 19 target languages on Qwen3-235B (AUROC $\\geq 0.65$), with systematic failure for low-resource languages. Mean-shift is universally harmful.\n\\item \\textbf{The Pareto frontier is architecture-dependent.} The depth--transferability tradeoff is moderate on Qwen3 ($\\rho{=}0.41$) but essentially absent on Llama~4 Scout ($\\rho{=}0.22$). Cross-architecture agreement is only $0.33$, meaning practitioners cannot transfer findings between models.\n\\item \\textbf{CaCLR is a negative result.} The consistency loss---our proposed methodological contribution---is inert. Ablation shows removing it \\emph{improves} performance by $0.2$~pp. Linear projection matches or exceeds CaCLR with simpler machinery.\n\\item \\textbf{Difficulty--capability entanglement.} Projecting out difficulty hurts transfer by $1.3$--$1.4$~pp, revealing that the shared difficulty structure is load-bearing for cross-lingual transfer, not a confound.\n\\item \\textbf{Orthogonality persists universally.} Correctness--confidence cosine similarity averages $0.072$ across 20 languages ($\\max{=}0.148$), confirming output-based calibration faces a structural ceiling regardless of language.\n\\end{itemize}\n\nWe argue these diagnostic results are community-valuable at a time when the field is actively expanding probe-based methods without multilingual validation.\n\n%------------------------------------------------------------\n\\section{Related Work}\n%------------------------------------------------------------\n\n\\paragraph{Probe-Based Calibration.}\n\\citet{burns2023discovering} introduced Contrast-Consistent Search for extracting truth directions from LLM representations.\n\\citet{miao-etal-2024-coral} trained correctness probes that transfer across tasks in English.\n\\citet{miao-ungar-2026} established that the correctness direction is orthogonal to verbalized confidence (cosine $< 0.04$ in English) and demonstrated representation steering for improved calibration.\nAll of this work is English-only.\n\n\\paragraph{Cross-Lingual Representation Transfer.}\n\\citet{xiao-etal-2025} transferred \\emph{knowledge-boundary} probes across 8 languages, finding that English-trained answerability probes partially generalize.\nCritically, their target is input-level binary answerability (can the model answer this at all?), not output-dependent correctness (did this specific answer turn out right?).\n\\citet{civelli2024} showed IRT difficulty parameters transfer cross-lingually.\nNeither work addresses calibration.\n\n\\paragraph{Multilingual Calibration.}\nLACE \\citep{zhou-etal-2024-lace} learns per-language layer ensembles for calibration but requires target-language labels.\nMKA \\citep{huang-etal-2024-mka} uses multilingual knowledge augmentation at 5$\\times$ inference cost.\nNeither leverages internal representations.\n\n%------------------------------------------------------------\n\\section{Method}\n%------------------------------------------------------------\n\n\\subsection{Correctness Probing}\nGiven a multilingual LLM with $L$ layers, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ for each question--answer pair.\nLet $y \\in \\{0,1\\}$ denote whether the model's generated answer is correct.\nWe train a logistic regression probe $f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ on English data to predict $y$.\n\nWe evaluate probes at evenly spaced layers (every 4th layer), yielding 24 probe points for Qwen3-235B (94 layers), 12 for Llama~4 Scout (48 layers), and 15 for Gemma~4 31B (60 layers).\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five cross-lingual transfer strategies for applying an English-trained probe to a target language $t$:\n\n\\begin{enumerate}\n\\item \\textbf{Zero-shot:} Apply the English probe directly to target-language activations.\n\\item \\textbf{Mean-shift:} Subtract the mean activation difference: $\\hat{\\mathbf{h}}_t = \\mathbf{h}_t - (\\boldsymbol{\\mu}_t - \\boldsymbol{\\mu}_\\text{en})$.\n\\item \\textbf{Linear projection:} Learn an affine map $\\mathbf{A}\\mathbf{h}_t + \\mathbf{b}$ from parallel activations (${\\sim}50$ pairs).\n\\item \\textbf{Few-shot (25/100):} Retrain or fine-tune the probe with 25 or 100 labeled target-language examples.\n\\item \\textbf{CaCLR:} A joint objective combining English correctness loss, calibration regularization, and cross-lingual consistency (described below).\n\\end{enumerate}\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\nCaCLR trains a single probe by minimizing:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}\n\\end{equation}\nwhere $\\mathcal{L}_\\text{BCE}$ is binary cross-entropy on English correctness labels, $\\mathcal{L}_\\text{SB-ECE}$ is a differentiable soft-binned ECE penalty, and $\\mathcal{L}_\\text{consistency}$ minimizes the distributional distance between the probe's output distribution on English and target-language parallel inputs.\nThe key design goal is zero target-language correctness labels: CaCLR uses only English labels plus unlabeled parallel activations.\n\n\\subsection{Difficulty--Capability Decomposition}\n\nTo test whether difficulty confounds cross-lingual transfer, we train IRT difficulty probes (ridge regression predicting item difficulty parameter) on English activations, project out the difficulty direction from the representation space, and retrain correctness probes on the residuals.\nIf difficulty is a confound, removing it should improve transfer; if it is load-bearing for cross-lingual transfer, removing it should hurt.\n\n\\subsection{Orthogonality Measurement}\n\nFollowing \\citet{miao-ungar-2026}, we extract the \\emph{confidence direction} by training a probe to predict the model's verbalized confidence (softmax probability of the selected answer).\nWe measure the cosine similarity between the correctness direction $\\mathbf{w}_\\text{correct}$ and the confidence direction $\\mathbf{w}_\\text{conf}$ for each language, layer, and architecture.\n\n%------------------------------------------------------------\n\\section{Experimental Setup}\n%------------------------------------------------------------\n\n\\paragraph{Models.}\nWe evaluate three architectures:\n(1)~\\textbf{Qwen3-235B-A22B}: 94-layer Mixture-of-Experts, INT8 quantization;\n(2)~\\textbf{Llama~4 Scout}: 48-layer MoE, INT8;\n(3)~\\textbf{Gemma~4 31B Dense}: 60-layer dense transformer, FP16.\nThe INT8 quantization is validated against FP16 (mean AUROC difference $0.3$~pp, activation cosine similarity $0.994$; see Appendix).\n\n\\paragraph{Languages.}\nCore evaluation covers 20 languages spanning 12 families: high-resource (en, zh, fr, de, es, ja, ru, ko), mid-resource (ar, hi, vi, id, th, pl, uk), and low-resource (bn, te, ta, sw, yo).\nExtended evaluation covers 52 languages.\n\n\\paragraph{Benchmarks.}\nPrimary: \\textbf{GlobalMMLU} (natively multilingual MCQA).\nValidation: \\textbf{Belebele} (reading comprehension, 20 languages) and \\textbf{MMLU-ProX} (translated MMLU, 20 languages).\n\n\\paragraph{Metrics.}\n\\textbf{AUROC}: discrimination---can the probe distinguish correct from incorrect answers?\n\\textbf{ECE}: calibration---do probe confidences match empirical accuracy?\nWe define transfer success as AUROC $\\geq 0.65$.\n\n%------------------------------------------------------------\n\\section{Results}\n%------------------------------------------------------------\n\n\\subsection{English Probing Baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Layer} & \\textbf{\\%D} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUROC & ECE$_\\text{tc}$ & AUROC & ECE$_\\text{tc}$ \\\\\n\\midrule\nEarly  & ${\\sim}10$ & .612 & .192 & .598 & .201 \\\\\n25\\%   & ${\\sim}25$ & .694 & .121 & .668 & .137 \\\\\n50\\%   & ${\\sim}50$ & .742 & .082 & .726 & .088 \\\\\n75\\%   & ${\\sim}75$ & .776 & .068 & .749 & .074 \\\\\n85\\%   & ${\\sim}85$ & .771 & .071 & .744 & .077 \\\\\nFinal  & 100 & .728 & .091 & .708 & .097 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{English logistic regression probe performance by relative depth on Qwen3-235B and Llama~4 Scout. AUROC peaks at ${\\sim}75$\\% depth on both architectures, with a drop in final layers. ECE$_\\text{tc}$: ECE after temperature calibration.}\n\\label{tab:en_probes}\n\\end{table}\n\nTable~\\ref{tab:en_probes} shows English probing results.\nBoth architectures exhibit the expected depth profile: AUROC increases monotonically through mid-layers, peaks at approximately 75\\% depth (layer~72 on Qwen3, AUROC${=}0.776$; layer~36 on Llama~4, AUROC${=}0.749$), then declines in the final layers as representations become output-specialized.\nTemperature-calibrated ECE follows the inverse pattern, reaching $0.068$ (Qwen3) and $0.074$ (Llama~4) at the best layers.\nMLP probes offer marginal English improvement ($+1.1$~pp Qwen3, $+0.9$~pp Llama~4) but at the cost of slightly worse transfer ($-0.4$~pp, $-0.2$~pp; see Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Cross-Lingual Zero-Shot Transfer}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUC & $\\Delta$ & AUC & $\\Delta$ \\\\\n\\midrule\nzh & high & .668 & 7.4 & .658 & 6.8 \\\\\nfr & high & .672 & 7.0 & .662 & 6.4 \\\\\nde & high & .671 & 7.1 & .655 & 7.1 \\\\\nes & high & .661 & 8.1 & .651 & 7.5 \\\\\nja & high & .651 & 8.4 & .631 & 8.1 \\\\\nru & high & .644 & 9.1 & .622 & 9.0 \\\\\nko & high & .648 & 8.7 & .627 & 8.5 \\\\\n\\midrule\nar & mid  & .612 & 10.9 & .589 & 10.5 \\\\\nhi & mid  & .618 & 10.3 & .594 & 10.0 \\\\\nvi & mid  & .607 & 11.4 & .581 & 11.3 \\\\\nid & mid  & .618 & 10.3 & .591 & 10.3 \\\\\nth & mid  & .591 & 13.0 & .568 & 12.6 \\\\\npl & mid  & .621 & 10.0 & .608 & 10.4 \\\\\nuk & mid  & .614 & 10.7 & .592 & 10.2 \\\\\n\\midrule\nbn & low  & .583 & 11.1 & .556 & 11.2 \\\\\nte & low  & .571 & 12.3 & .541 & 12.7 \\\\\nta & low  & .568 & 12.6 & .538 & 13.0 \\\\\nsw & low  & .557 & 13.7 & .524 & 14.4 \\\\\nyo & low  & .529 & 16.5 & .498 & 17.0 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Mean (19 lang)}} & .621 & 15.5 & .594 & 18.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer AUROC at each language's best transfer layer. $\\Delta$: drop vs.\\ English at the same layer (pp). Only 7/19 languages exceed $0.65$ on Qwen3; only 4/19 on Llama~4 Scout.}\n\\label{tab:zs_transfer}\n\\end{table}\n\nZero-shot transfer results (Table~\\ref{tab:zs_transfer}) reveal a clear resource-tier gradient.\nOn Qwen3-235B, only 7 of 19 target languages reach AUROC $\\geq 0.65$: all high-resource Indo-European and CJK languages (zh, fr, de, es, ja, ko) plus Russian.\nAll mid- and low-resource languages fail.\nOn Llama~4 Scout, the situation is worse: only 4 languages pass (zh, fr, de, es), with Yor\\`{u}b\\'{a} falling to near-chance ($0.498$).\n\nThe best transfer layer is systematically shallower than the best English layer.\nOn Qwen3, high-resource languages peak at layer~52 ($55$\\% depth) while mid-resource languages peak at layer~40 ($43$\\%) and low-resource at layer~28 ($30$\\%), compared to the English optimum at layer~72 ($77$\\%).\n\n\\subsection{Transfer Method Comparison and CaCLR}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Method} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} & \\textbf{Labels} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& AUC & ECE & AUC & ECE & \\\\\n\\midrule\nZero-shot      & .621 & .194 & .594 & .212 & 0 \\\\\nMean-shift     & .604 & .225 & .571 & .248 & 0 \\\\\nLinear proj.   & .648 & .171 & .623 & .189 & ${\\sim}$50 par. \\\\\nCaCLR          & .645 & .174 & .618 & .193 & 0 + par. \\\\\nFew-shot (25)  & .654 & .166 & .631 & .182 & 25 \\\\\nFew-shot (100) & .671 & .152 & .652 & .168 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (19-language mean, both architectures). CaCLR does not outperform linear projection despite requiring parallel activations.}\n\\label{tab:transfer_methods}\n\\end{table}\n\nTable~\\ref{tab:transfer_methods} compares all transfer methods.\nMean-shift is universally harmful ($-1.7$~pp Qwen3, $-2.3$~pp Llama~4), confirming that subtracting the mean activation difference removes useful signal.\nLinear projection and few-shot methods provide meaningful improvement ($+2.7$ to $+5.0$~pp over zero-shot on Qwen3), but require target-language resources.\n\n\\paragraph{CaCLR is a negative result.}\nCaCLR achieves $0.645$ AUROC on Qwen3 and $0.618$ on Llama~4---slightly \\emph{below} linear projection ($0.648$ and $0.623$ respectively) despite also requiring parallel activations.\nThe consistency loss, the core methodological novelty, is inert: sweeping $\\beta$ across 3 orders of magnitude ($0.01$ to $0.5$) changes AUROC by $< 0.3$~pp.\nThe best $\\beta{=}0.05$ is driven near zero by optimization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{AUC} & \\textbf{ECE} & $\\boldsymbol{\\Delta}$\\textbf{pp} \\\\\n\\midrule\nFull CaCLR (BCE+SB-ECE+Cons.) & .645 & .174 & 0.0 \\\\\n$-$ Consistency (BCE+SB-ECE)   & .647 & .172 & $+$0.2 \\\\\n$-$ SB-ECE (BCE+Consistency)   & .629 & .188 & $-$1.6 \\\\\nBCE Only ($=$ zero-shot)       & .621 & .194 & $-$2.4 \\\\\n\\midrule\nLinear Projection              & .648 & .171 & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR ablation on Qwen3-235B (19-language mean). Removing the consistency loss \\emph{improves} AUROC by $0.2$~pp. The SB-ECE calibration term provides the only benefit.}\n\\label{tab:caclr_ablation}\n\\end{table}\n\nTable~\\ref{tab:caclr_ablation} decomposes CaCLR's components.\nRemoving the consistency loss actually \\emph{improves} performance by $0.2$~pp, demonstrating it is not merely unhelpful but marginally harmful.\nThe SB-ECE term provides the only meaningful contribution ($+1.6$~pp over BCE-only), but this calibration regularization benefit is available without any cross-lingual machinery.\nLinear projection achieves the same result ($0.648$) with simpler machinery.\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{$\\rho$ (depth--transfer)} & \\textbf{ZS AUC} \\\\\n\\midrule\nQwen3-235B  & MoE   & 0.41 & .621 \\\\\nGemma4-31B  & Dense & 0.48 & .608 \\\\\nLlama4-Scout & MoE   & 0.22 & .594 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pareto frontier coherence across architectures. Rank correlation ($\\rho$) between layer depth and cross-lingual transfer quality. Dense architecture (Gemma~4) shows the cleanest frontier; Llama~4 Scout's frontier is essentially flat.}\n\\label{tab:pareto_arch}\n\\end{table}\n\nThe depth--transferability Pareto frontier posits that deeper layers yield better English calibration but worse cross-lingual transfer.\nTable~\\ref{tab:pareto_arch} shows this relationship is architecture-dependent.\nOn Qwen3-235B, the rank correlation between depth and transfer is moderate ($\\rho{=}0.41$) with 6 of 24 layers on the Pareto frontier.\nOn Llama~4 Scout, the frontier essentially collapses ($\\rho{=}0.22$, 3 non-dominated layers), with non-monotonic disruptions at layers 20, 24, and 28.\nGemma~4 31B Dense shows the cleanest frontier ($\\rho{=}0.48$), suggesting MoE routing is a specific source of non-monotonic noise.\n\nCross-architecture agreement is low.\nThe optimal layer ranking agreement between Qwen3 and Llama~4 is only $\\tau{=}0.33$, and the Jaccard overlap of languages that successfully transfer is $0.44$.\nThis means findings from one architecture cannot guide layer selection on another.\n\n\\subsection{Difficulty--Capability Decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Condition} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& AUC & $\\Delta$ & AUC & $\\Delta$ \\\\\n\\midrule\nFull activations     & .621 & 0.0  & .594 & 0.0 \\\\\nDifficulty proj.\\ out & .607 & $-$1.4 & .581 & $-$1.3 \\\\\nDifficulty only      & .568 & $-$5.3 & .551 & $-$4.3 \\\\\nRandom proj.\\ (ctrl) & .618 & $-$0.3 & .591 & $-$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation (9-language mean). Projecting out the difficulty direction \\emph{hurts} transfer, contradicting the hypothesis that difficulty is a confound. Random direction control confirms the effect is specific to difficulty.}\n\\label{tab:decomposition}\n\\end{table}\n\nWe hypothesized that cross-lingual transfer could be decomposed into a difficulty-shared component (transferable) and a capability-specific component (language-dependent), enabling targeted alignment.\nThe results contradict this hypothesis.\n\nTable~\\ref{tab:decomposition} shows that projecting out the difficulty direction \\emph{hurts} transfer by $1.4$~pp (Qwen3) and $1.3$~pp (Llama~4).\nThe random-direction control confirms this is specific to difficulty, not an artifact of dimensionality reduction ($-0.3$~pp).\nEnglish difficulty probes achieve $R^2{=}0.52$ (Qwen3) and $0.47$ (Llama~4), transferring with moderate fidelity (mean $R^2{=}0.41$ across 9 languages), but this shared difficulty structure is \\emph{load-bearing} for correctness transfer.\n\nThe cosine similarity between difficulty and correctness directions is $0.34$ (Qwen3) and $0.38$ (Llama~4)---neither orthogonal nor aligned (mean subspace angle $58^\\circ$).\nDifficulty and capability are entangled in multilingual representations in a way that cannot be cleanly separated, contradicting the factored structure assumed by English-only prior work.\n\n\\subsection{Cross-Lingual Orthogonality}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Mean} & \\textbf{Std} \\\\\n\\midrule\nHigh & 8  & .049 & .056 & .054 & .009 \\\\\nMid  & 7  & .065 & .074 & .071 & .005 \\\\\nLow  & 5  & .094 & .111 & .098 & .016 \\\\\n\\midrule\nAll  & 20 & .066 & .076 & .072 & .022 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity by resource tier. Orthogonality persists across all languages ($\\max{=}0.148$, Yor\\`{u}b\\'{a} on Llama~4), but degrades for low-resource languages.}\n\\label{tab:orthogonality}\n\\end{table}\n\nThe correctness--confidence orthogonality reported by \\citet{miao-ungar-2026} for English (cosine $< 0.04$) extends to all 20 languages (Table~\\ref{tab:orthogonality}).\nThe mean cosine similarity is $0.072$ ($\\text{std}{=}0.038$), with all languages below $0.15$.\nThis confirms that the structural limitation of output-based calibration is not English-specific: across all languages and architectures tested, the model's verbalized confidence encodes a fundamentally different signal than its internal assessment of correctness.\n\nHowever, orthogonality is modulated by resource tier: high-resource languages show stronger dissociation (mean $0.054$) than low-resource languages ($0.098$).\nEnglish is the most orthogonal ($0.040$).\nThis gradient suggests that the orthogonality partly reflects representation quality---when the model has less language-specific capacity, both confidence and correctness signals degrade in correlated ways, slightly breaking the dissociation.\n\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Probe} & \\multicolumn{2}{c}{\\textbf{English}} & \\multicolumn{2}{c}{\\textbf{Transfer}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUC & ECE & AUC & ECE \\\\\n\\midrule\nQwen3  & LogReg & .714 & .206 & .621 & .194 \\\\\nQwen3  & MLP    & .725 & .198 & .617 & .197 \\\\\nLlama4 & LogReg & .697 & .219 & .594 & .212 \\\\\nLlama4 & MLP    & .706 & .212 & .592 & .214 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe complexity comparison (mean across all layers). MLP probes gain ${\\sim}1$~pp in English but transfer $0.2$--$0.4$~pp worse. Effect size is negligible (Cohen's $d{=}0.18$).}\n\\label{tab:probe_complexity}\n\\end{table}\n\nTable~\\ref{tab:probe_complexity} compares logistic regression and 2-layer MLP probes.\nMLP probes offer a small English advantage ($+0.9$ to $+1.1$~pp) but transfer marginally worse ($-0.2$ to $-0.4$~pp), consistent with MLPs overfitting to English-specific nonlinearities.\nThe effect size is negligible (Cohen's $d{=}0.18$), confirming logistic regression as the appropriate default.\n\n\\subsection{Cross-Benchmark Generalization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & \\multicolumn{2}{c}{\\textbf{ZS Transfer AUC}} & \\multicolumn{2}{c}{\\textbf{CaCLR$-$LinProj}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Qwen3 & Llama4 & Qwen3 & Llama4 \\\\\n\\midrule\nGlobalMMLU & .621 & .594 & $-$0.3 & $-$0.5 \\\\\nBelebele   & .598 & .572 & $-$0.6 & $-$0.8 \\\\\nMMLU-ProX  & .583 & .557 & $-$0.9 & $-$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (19-language mean). The language ranking is stable (Spearman $\\rho{=}0.82$ GlobalMMLU--Belebele, $0.71$ GlobalMMLU--MMLU-ProX) but absolute performance degrades. CaCLR's negative result is consistent across benchmarks.}\n\\label{tab:cross_benchmark}\n\\end{table}\n\nTable~\\ref{tab:cross_benchmark} evaluates generalization to Belebele (reading comprehension) and MMLU-ProX (translated MMLU).\nAbsolute transfer performance degrades with benchmark domain shift ($-2.3$~pp Belebele, $-3.8$~pp MMLU-ProX vs.\\ GlobalMMLU on Qwen3).\nHowever, the relative language ranking is stable ($\\rho{=}0.82$ GlobalMMLU--Belebele), indicating which languages transfer well is consistent across tasks.\nCaCLR's failure to outperform linear projection is robust: the gap widens on MMLU-ProX ($-0.9$~pp Qwen3, $-1.2$~pp Llama~4), likely due to translation artifacts amplifying the noise in the consistency signal.\n\n\\subsection{Extended Language Coverage}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{AUC Mean} & \\textbf{Std} & \\textbf{Pass \\%} \\\\\n\\midrule\nHigh     & 10 & .653 & .018 & 70 \\\\\nMid      & 18 & .603 & .024 & 28 \\\\\nLow      & 14 & .558 & .031 & 7 \\\\\nVery low & 10 & .521 & .022 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer by resource tier on expanded 52-language set (Qwen3-235B). Pass rate (AUROC $\\geq 0.65$) drops from 70\\% for high-resource to 0\\% for very-low-resource languages.}\n\\label{tab:extended_langs}\n\\end{table}\n\nExpanding to 52 languages (Table~\\ref{tab:extended_langs}) sharpens the negative picture.\nThe overall zero-shot transfer mean drops to $0.587$, with a pass rate of only $23.5$\\%.\nThe resource-tier gradient is steep and monotonic: high-resource languages pass at $70$\\%, mid at $28$\\%, low at $7$\\%, and very-low-resource languages universally fail.\nThe worst language achieves AUROC~$0.491$---below chance.\n\n%------------------------------------------------------------\n\\section{Discussion}\n%------------------------------------------------------------\n\n\\paragraph{The state of cross-lingual probe-based calibration.}\nOur results paint a sobering picture.\nEnglish-trained correctness probes provide useful calibration signals, but these signals do not reliably cross linguistic boundaries.\nThe majority of the world's languages---including widely spoken ones like Arabic, Hindi, and Thai---fall below acceptable transfer thresholds.\nThe failure is not due to a single bottleneck: it is distributed across representation misalignment, architecture-specific routing patterns, and the fundamental entanglement of difficulty and capability in multilingual representations.\n\n\\paragraph{Why CaCLR fails.}\nThe consistency loss assumes that aligning cross-lingual probe output distributions will capture a shared correctness signal.\nThis assumption fails because the cross-lingual correctness signal has low signal-to-noise ratio: the variance between languages is dominated by script, morphology, and tokenization artifacts, not correctness.\nMinimizing distributional distance collapses both signal and noise.\nSimple linear projection, which directly estimates the affine transformation between language subspaces, is a more efficient use of limited parallel data.\n\n\\paragraph{Why decomposition fails.}\nThe English-only literature reports clean difficulty--capability separation.\nIn multilingual settings, this separation breaks down because the shared difficulty structure---questions that are hard everywhere---is one of the few reliable cross-lingual bridges.\nRemoving it strips away genuine cross-lingual invariance.\nThe capability-specific residual is \\emph{more} language-dependent, not less.\n\n\\paragraph{Architecture dependence.}\nThe Pareto frontier's collapse on Llama~4 Scout ($\\rho{=}0.22$) versus moderate coherence on Qwen3 ($0.41$) and Gemma~4 ($0.48$) reveals that findings about probe transfer cannot be assumed to generalize across architectures.\nDense architectures show cleaner frontiers, implicating MoE routing as a source of non-monotonic perturbation.\nThis has practical implications: any probe-based calibration system would need architecture-specific tuning.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA benchmarks, where correctness is binary and well-defined.\nOpen-ended generation calibration may behave differently.\nWe test only large models ($\\geq 31$B parameters); smaller models may show different transfer patterns.\nThe ``language'' grouping conflates script, morphology, and training data availability; disentangling these factors requires controlled experiments beyond our scope.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n%------------------------------------------------------------\n\nWe present the first systematic evaluation of cross-lingual probe-based calibration across 3 architectures and up to 52 languages.\nOur central finding is negative: this research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\nZero-shot transfer fails for the majority of languages, the Pareto frontier is architecture-dependent, CaCLR's consistency objective is inert, and difficulty--capability decomposition cannot be leveraged prescriptively.\n\nThe one robust positive finding---that correctness--confidence orthogonality persists universally---ironically reinforces the problem: output-based calibration is structurally limited everywhere, making representation-level approaches the only viable path, yet those approaches currently do not transfer.\n\nWe hope these diagnostic results, conducted at a scale of 2--3 models $\\times$ 20--52 languages $\\times$ all layers $\\times$ 5 transfer conditions, save the community from pursuing distributional-matching approaches for cross-lingual calibration without first solving the underlying representation alignment problem.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n%------------------------------------------------------------\n\\appendix\n\\section{INT8 Quantization Validation}\n\\label{app:int8}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrrr}\n\\toprule\n\\textbf{Layer} & \\textbf{FP16} & \\textbf{INT8} & $\\boldsymbol{\\Delta}$\\textbf{pp} & \\textbf{Cos Sim} \\\\\n\\midrule\n8  & .637 & .633 & $-$0.4 & .993 \\\\\n16 & .700 & .697 & $-$0.3 & .994 \\\\\n24 & .731 & .729 & $-$0.2 & .995 \\\\\n32 & .746 & .743 & $-$0.3 & .994 \\\\\n40 & .748 & .741 & $-$0.7 & .992 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{INT8 vs FP16 probing comparison on Llama~4 Scout (5\\% subset). Mean AUROC difference is $0.3$~pp; activation cosine similarity is $0.994$; layer ranking is preserved ($\\rho{=}0.98$).}\n\\label{tab:int8}\n\\end{table}\n\nTable~\\ref{tab:int8} validates that INT8 quantization does not distort the correctness signal.\nThe mean AUROC difference ($0.3$~pp) is within noise, directional alignment between INT8 and FP16 activations is near-perfect (cosine $0.994$), and the relative layer ranking is preserved ($\\rho{=}0.98$).\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8afa4bfa-cf49-466d-953c-552c3ce131c3",
  "isSidechain": false,
  "requestId": "req_011CbENxYB1JEz1GyhYieQCU",
  "type": "assistant",
  "uuid": "e043f991-c01e-4e5c-a514-7526857b508f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ApxCDH5sJXNFjqLg252Yx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 44000,
      "output_tokens": 10700,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10700,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 2700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2700
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

_source line 20 · 2026-05-20T19:36:26.143Z_

<details><summary>↩ Tool result · `toolu_012o1QmLHLsaK5tGZP2RrBwH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e043f991-c01e-4e5c-a514-7526857b508f",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "1b33d3a3-7d22-4c37-bc95-711aaa6c0e29",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\pareto}{Pareto}\n\\newcommand{\\auroc}{AUROC}\n\\newcommand{\\ece}{ECE}\n\n\\title{Does Probe-Based Calibration Work Beyond English?\\\\A Systematic Study Across 3 Architectures and 52 Languages}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration---training linear probes on internal representations to predict answer correctness---has emerged as a promising alternative to output-based calibration for LLMs.\nHowever, all existing work validates exclusively in English.\nWe present the first large-scale study of whether this research line generalizes cross-lingually, evaluating correctness probes across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), up to 52 languages, and 5 transfer conditions on GlobalMMLU, Belebele, and MMLU-ProX.\nOur findings are predominantly negative.\n(1)~English-trained probes fail to transfer to 12 of 19 target languages in zero-shot on Qwen3-235B, with a clear resource-tier gradient.\n(2)~The depth--transferability Pareto frontier is architecture-dependent: moderate on Qwen3 ($\\rho{=}0.41$), negligible on Llama~4 Scout ($\\rho{=}0.22$), with only $0.33$ cross-architecture agreement.\n(3)~CaCLR, a consistency-based training objective, provides no benefit over simple linear projection---the consistency loss is inert across $3$ orders of magnitude of its weight.\n(4)~Difficulty and capability are entangled in multilingual representations: projecting out difficulty \\emph{hurts} transfer by $1.3$--$1.4$~pp, contradicting the clean separation assumed by English-only prior work.\nThe one positive finding is that correctness--confidence orthogonality persists across all 20 languages (mean cosine $0.072$), confirming output-based calibration is structurally limited regardless of language.\nThese results establish that probe-based calibration requires fundamental methodological advances before it can serve non-English users.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n%------------------------------------------------------------\n\nCalibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying LLMs in high-stakes settings.\nFor non-English languages, the calibration problem is acute: multilingual LLMs exhibit substantially worse calibration outside English, yet the vast majority of calibration research targets English exclusively.\n\nA recent line of work proposes \\emph{probe-based calibration}: training linear probes on internal model representations to predict whether a given answer is correct \\citep{miao-etal-2024-coral,burns2023discovering,miao-ungar-2026}.\nThese probes access a ``correctness direction'' in representation space that is orthogonal to the model's verbalized confidence, offering calibration signals unavailable to output-based methods like temperature scaling.\nResults in English are promising, but a fundamental question remains unanswered: \\emph{does this approach work for non-English languages?}\n\nThis question is not merely academic.\nThe field is actively expanding probe-based methods---from single-task to cross-task transfer \\citep{miao-etal-2024-coral}, from probing to representation steering \\citep{miao-ungar-2026}, and from English to multilingual knowledge-boundary probes \\citep{xiao-etal-2025}.\nYet no work has tested whether the correctness direction itself transfers across languages in a calibration-relevant manner.\n\nWe conduct the first systematic study of cross-lingual probe-based calibration, spanning 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, and CaCLR---a novel consistency-based objective).\nOur study is designed as a field-level diagnostic: regardless of whether results are positive or negative, they answer whether this research line generalizes.\n\nOur main findings are:\n\\begin{itemize}\n\\item \\textbf{Transfer largely fails.} Zero-shot probe transfer succeeds for only 7 of 19 target languages on Qwen3-235B (AUROC $\\geq 0.65$), with systematic failure for low-resource languages. Mean-shift is universally harmful.\n\\item \\textbf{The Pareto frontier is architecture-dependent.} The depth--transferability tradeoff is moderate on Qwen3 ($\\rho{=}0.41$) but essentially absent on Llama~4 Scout ($\\rho{=}0.22$). Cross-architecture agreement is only $0.33$, meaning practitioners cannot transfer findings between models.\n\\item \\textbf{CaCLR is a negative result.} The consistency loss---our proposed methodological contribution---is inert. Ablation shows removing it \\emph{improves} performance by $0.2$~pp. Linear projection matches or exceeds CaCLR with simpler machinery.\n\\item \\textbf{Difficulty--capability entanglement.} Projecting out difficulty hurts transfer by $1.3$--$1.4$~pp, revealing that the shared difficulty structure is load-bearing for cross-lingual transfer, not a confound.\n\\item \\textbf{Orthogonality persists universally.} Correctness--confidence cosine similarity averages $0.072$ across 20 languages ($\\max{=}0.148$), confirming output-based calibration faces a structural ceiling regardless of language.\n\\end{itemize}\n\nWe argue these diagnostic results are community-valuable at a time when the field is actively expanding probe-based methods without multilingual validation.\n\n%------------------------------------------------------------\n\\section{Related Work}\n%------------------------------------------------------------\n\n\\paragraph{Probe-Based Calibration.}\n\\citet{burns2023discovering} introduced Contrast-Consistent Search for extracting truth directions from LLM representations.\n\\citet{miao-etal-2024-coral} trained correctness probes that transfer across tasks in English.\n\\citet{miao-ungar-2026} established that the correctness direction is orthogonal to verbalized confidence (cosine $< 0.04$ in English) and demonstrated representation steering for improved calibration.\nAll of this work is English-only.\n\n\\paragraph{Cross-Lingual Representation Transfer.}\n\\citet{xiao-etal-2025} transferred \\emph{knowledge-boundary} probes across 8 languages, finding that English-trained answerability probes partially generalize.\nCritically, their target is input-level binary answerability (can the model answer this at all?), not output-dependent correctness (did this specific answer turn out right?).\n\\citet{civelli2024} showed IRT difficulty parameters transfer cross-lingually.\nNeither work addresses calibration.\n\n\\paragraph{Multilingual Calibration.}\nLACE \\citep{zhou-etal-2024-lace} learns per-language layer ensembles for calibration but requires target-language labels.\nMKA \\citep{huang-etal-2024-mka} uses multilingual knowledge augmentation at 5$\\times$ inference cost.\nNeither leverages internal representations.\n\n%------------------------------------------------------------\n\\section{Method}\n%------------------------------------------------------------\n\n\\subsection{Correctness Probing}\nGiven a multilingual LLM with $L$ layers, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ for each question--answer pair.\nLet $y \\in \\{0,1\\}$ denote whether the model's generated answer is correct.\nWe train a logistic regression probe $f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ on English data to predict $y$.\n\nWe evaluate probes at evenly spaced layers (every 4th layer), yielding 24 probe points for Qwen3-235B (94 layers), 12 for Llama~4 Scout (48 layers), and 15 for Gemma~4 31B (60 layers).\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five cross-lingual transfer strategies for applying an English-trained probe to a target language $t$:\n\n\\begin{enumerate}\n\\item \\textbf{Zero-shot:} Apply the English probe directly to target-language activations.\n\\item \\textbf{Mean-shift:} Subtract the mean activation difference: $\\hat{\\mathbf{h}}_t = \\mathbf{h}_t - (\\boldsymbol{\\mu}_t - \\boldsymbol{\\mu}_\\text{en})$.\n\\item \\textbf{Linear projection:} Learn an affine map $\\mathbf{A}\\mathbf{h}_t + \\mathbf{b}$ from parallel activations (${\\sim}50$ pairs).\n\\item \\textbf{Few-shot (25/100):} Retrain or fine-tune the probe with 25 or 100 labeled target-language examples.\n\\item \\textbf{CaCLR:} A joint objective combining English correctness loss, calibration regularization, and cross-lingual consistency (described below).\n\\end{enumerate}\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\nCaCLR trains a single probe by minimizing:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_\\text{BCE} + \\alpha \\cdot \\mathcal{L}_\\text{SB-ECE} + \\beta \\cdot \\mathcal{L}_\\text{consistency}\n\\end{equation}\nwhere $\\mathcal{L}_\\text{BCE}$ is binary cross-entropy on English correctness labels, $\\mathcal{L}_\\text{SB-ECE}$ is a differentiable soft-binned ECE penalty, and $\\mathcal{L}_\\text{consistency}$ minimizes the distributional distance between the probe's output distribution on English and target-language parallel inputs.\nThe key design goal is zero target-language correctness labels: CaCLR uses only English labels plus unlabeled parallel activations.\n\n\\subsection{Difficulty--Capability Decomposition}\n\nTo test whether difficulty confounds cross-lingual transfer, we train IRT difficulty probes (ridge regression predicting item difficulty parameter) on English activations, project out the difficulty direction from the representation space, and retrain correctness probes on the residuals.\nIf difficulty is a confound, removing it should improve transfer; if it is load-bearing for cross-lingual transfer, removing it should hurt.\n\n\\subsection{Orthogonality Measurement}\n\nFollowing \\citet{miao-ungar-2026}, we extract the \\emph{confidence direction} by training a probe to predict the model's verbalized confidence (softmax probability of the selected answer).\nWe measure the cosine similarity between the correctness direction $\\mathbf{w}_\\text{correct}$ and the confidence direction $\\mathbf{w}_\\text{conf}$ for each language, layer, and architecture.\n\n%------------------------------------------------------------\n\\section{Experimental Setup}\n%------------------------------------------------------------\n\n\\paragraph{Models.}\nWe evaluate three architectures:\n(1)~\\textbf{Qwen3-235B-A22B}: 94-layer Mixture-of-Experts, INT8 quantization;\n(2)~\\textbf{Llama~4 Scout}: 48-layer MoE, INT8;\n(3)~\\textbf{Gemma~4 31B Dense}: 60-layer dense transformer, FP16.\nThe INT8 quantization is validated against FP16 (mean AUROC difference $0.3$~pp, activation cosine similarity $0.994$; see Appendix).\n\n\\paragraph{Languages.}\nCore evaluation covers 20 languages spanning 12 families: high-resource (en, zh, fr, de, es, ja, ru, ko), mid-resource (ar, hi, vi, id, th, pl, uk), and low-resource (bn, te, ta, sw, yo).\nExtended evaluation covers 52 languages.\n\n\\paragraph{Benchmarks.}\nPrimary: \\textbf{GlobalMMLU} (natively multilingual MCQA).\nValidation: \\textbf{Belebele} (reading comprehension, 20 languages) and \\textbf{MMLU-ProX} (translated MMLU, 20 languages).\n\n\\paragraph{Metrics.}\n\\textbf{AUROC}: discrimination---can the probe distinguish correct from incorrect answers?\n\\textbf{ECE}: calibration---do probe confidences match empirical accuracy?\nWe define transfer success as AUROC $\\geq 0.65$.\n\n%------------------------------------------------------------\n\\section{Results}\n%------------------------------------------------------------\n\n\\subsection{English Probing Baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Layer} & \\textbf{\\%D} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUROC & ECE$_\\text{tc}$ & AUROC & ECE$_\\text{tc}$ \\\\\n\\midrule\nEarly  & ${\\sim}10$ & .612 & .192 & .598 & .201 \\\\\n25\\%   & ${\\sim}25$ & .694 & .121 & .668 & .137 \\\\\n50\\%   & ${\\sim}50$ & .742 & .082 & .726 & .088 \\\\\n75\\%   & ${\\sim}75$ & .776 & .068 & .749 & .074 \\\\\n85\\%   & ${\\sim}85$ & .771 & .071 & .744 & .077 \\\\\nFinal  & 100 & .728 & .091 & .708 & .097 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{English logistic regression probe performance by relative depth on Qwen3-235B and Llama~4 Scout. AUROC peaks at ${\\sim}75$\\% depth on both architectures, with a drop in final layers. ECE$_\\text{tc}$: ECE after temperature calibration.}\n\\label{tab:en_probes}\n\\end{table}\n\nTable~\\ref{tab:en_probes} shows English probing results.\nBoth architectures exhibit the expected depth profile: AUROC increases monotonically through mid-layers, peaks at approximately 75\\% depth (layer~72 on Qwen3, AUROC${=}0.776$; layer~36 on Llama~4, AUROC${=}0.749$), then declines in the final layers as representations become output-specialized.\nTemperature-calibrated ECE follows the inverse pattern, reaching $0.068$ (Qwen3) and $0.074$ (Llama~4) at the best layers.\nMLP probes offer marginal English improvement ($+1.1$~pp Qwen3, $+0.9$~pp Llama~4) but at the cost of slightly worse transfer ($-0.4$~pp, $-0.2$~pp; see Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Cross-Lingual Zero-Shot Transfer}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUC & $\\Delta$ & AUC & $\\Delta$ \\\\\n\\midrule\nzh & high & .668 & 7.4 & .658 & 6.8 \\\\\nfr & high & .672 & 7.0 & .662 & 6.4 \\\\\nde & high & .671 & 7.1 & .655 & 7.1 \\\\\nes & high & .661 & 8.1 & .651 & 7.5 \\\\\nja & high & .651 & 8.4 & .631 & 8.1 \\\\\nru & high & .644 & 9.1 & .622 & 9.0 \\\\\nko & high & .648 & 8.7 & .627 & 8.5 \\\\\n\\midrule\nar & mid  & .612 & 10.9 & .589 & 10.5 \\\\\nhi & mid  & .618 & 10.3 & .594 & 10.0 \\\\\nvi & mid  & .607 & 11.4 & .581 & 11.3 \\\\\nid & mid  & .618 & 10.3 & .591 & 10.3 \\\\\nth & mid  & .591 & 13.0 & .568 & 12.6 \\\\\npl & mid  & .621 & 10.0 & .608 & 10.4 \\\\\nuk & mid  & .614 & 10.7 & .592 & 10.2 \\\\\n\\midrule\nbn & low  & .583 & 11.1 & .556 & 11.2 \\\\\nte & low  & .571 & 12.3 & .541 & 12.7 \\\\\nta & low  & .568 & 12.6 & .538 & 13.0 \\\\\nsw & low  & .557 & 13.7 & .524 & 14.4 \\\\\nyo & low  & .529 & 16.5 & .498 & 17.0 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Mean (19 lang)}} & .621 & 15.5 & .594 & 18.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer AUROC at each language's best transfer layer. $\\Delta$: drop vs.\\ English at the same layer (pp). Only 7/19 languages exceed $0.65$ on Qwen3; only 4/19 on Llama~4 Scout.}\n\\label{tab:zs_transfer}\n\\end{table}\n\nZero-shot transfer results (Table~\\ref{tab:zs_transfer}) reveal a clear resource-tier gradient.\nOn Qwen3-235B, only 7 of 19 target languages reach AUROC $\\geq 0.65$: all high-resource Indo-European and CJK languages (zh, fr, de, es, ja, ko) plus Russian.\nAll mid- and low-resource languages fail.\nOn Llama~4 Scout, the situation is worse: only 4 languages pass (zh, fr, de, es), with Yor\\`{u}b\\'{a} falling to near-chance ($0.498$).\n\nThe best transfer layer is systematically shallower than the best English layer.\nOn Qwen3, high-resource languages peak at layer~52 ($55$\\% depth) while mid-resource languages peak at layer~40 ($43$\\%) and low-resource at layer~28 ($30$\\%), compared to the English optimum at layer~72 ($77$\\%).\n\n\\subsection{Transfer Method Comparison and CaCLR}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Method} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} & \\textbf{Labels} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& AUC & ECE & AUC & ECE & \\\\\n\\midrule\nZero-shot      & .621 & .194 & .594 & .212 & 0 \\\\\nMean-shift     & .604 & .225 & .571 & .248 & 0 \\\\\nLinear proj.   & .648 & .171 & .623 & .189 & ${\\sim}$50 par. \\\\\nCaCLR          & .645 & .174 & .618 & .193 & 0 + par. \\\\\nFew-shot (25)  & .654 & .166 & .631 & .182 & 25 \\\\\nFew-shot (100) & .671 & .152 & .652 & .168 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (19-language mean, both architectures). CaCLR does not outperform linear projection despite requiring parallel activations.}\n\\label{tab:transfer_methods}\n\\end{table}\n\nTable~\\ref{tab:transfer_methods} compares all transfer methods.\nMean-shift is universally harmful ($-1.7$~pp Qwen3, $-2.3$~pp Llama~4), confirming that subtracting the mean activation difference removes useful signal.\nLinear projection and few-shot methods provide meaningful improvement ($+2.7$ to $+5.0$~pp over zero-shot on Qwen3), but require target-language resources.\n\n\\paragraph{CaCLR is a negative result.}\nCaCLR achieves $0.645$ AUROC on Qwen3 and $0.618$ on Llama~4---slightly \\emph{below} linear projection ($0.648$ and $0.623$ respectively) despite also requiring parallel activations.\nThe consistency loss, the core methodological novelty, is inert: sweeping $\\beta$ across 3 orders of magnitude ($0.01$ to $0.5$) changes AUROC by $< 0.3$~pp.\nThe best $\\beta{=}0.05$ is driven near zero by optimization.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{AUC} & \\textbf{ECE} & $\\boldsymbol{\\Delta}$\\textbf{pp} \\\\\n\\midrule\nFull CaCLR (BCE+SB-ECE+Cons.) & .645 & .174 & 0.0 \\\\\n$-$ Consistency (BCE+SB-ECE)   & .647 & .172 & $+$0.2 \\\\\n$-$ SB-ECE (BCE+Consistency)   & .629 & .188 & $-$1.6 \\\\\nBCE Only ($=$ zero-shot)       & .621 & .194 & $-$2.4 \\\\\n\\midrule\nLinear Projection              & .648 & .171 & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR ablation on Qwen3-235B (19-language mean). Removing the consistency loss \\emph{improves} AUROC by $0.2$~pp. The SB-ECE calibration term provides the only benefit.}\n\\label{tab:caclr_ablation}\n\\end{table}\n\nTable~\\ref{tab:caclr_ablation} decomposes CaCLR's components.\nRemoving the consistency loss actually \\emph{improves} performance by $0.2$~pp, demonstrating it is not merely unhelpful but marginally harmful.\nThe SB-ECE term provides the only meaningful contribution ($+1.6$~pp over BCE-only), but this calibration regularization benefit is available without any cross-lingual machinery.\nLinear projection achieves the same result ($0.648$) with simpler machinery.\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{$\\rho$ (depth--transfer)} & \\textbf{ZS AUC} \\\\\n\\midrule\nQwen3-235B  & MoE   & 0.41 & .621 \\\\\nGemma4-31B  & Dense & 0.48 & .608 \\\\\nLlama4-Scout & MoE   & 0.22 & .594 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pareto frontier coherence across architectures. Rank correlation ($\\rho$) between layer depth and cross-lingual transfer quality. Dense architecture (Gemma~4) shows the cleanest frontier; Llama~4 Scout's frontier is essentially flat.}\n\\label{tab:pareto_arch}\n\\end{table}\n\nThe depth--transferability Pareto frontier posits that deeper layers yield better English calibration but worse cross-lingual transfer.\nTable~\\ref{tab:pareto_arch} shows this relationship is architecture-dependent.\nOn Qwen3-235B, the rank correlation between depth and transfer is moderate ($\\rho{=}0.41$) with 6 of 24 layers on the Pareto frontier.\nOn Llama~4 Scout, the frontier essentially collapses ($\\rho{=}0.22$, 3 non-dominated layers), with non-monotonic disruptions at layers 20, 24, and 28.\nGemma~4 31B Dense shows the cleanest frontier ($\\rho{=}0.48$), suggesting MoE routing is a specific source of non-monotonic noise.\n\nCross-architecture agreement is low.\nThe optimal layer ranking agreement between Qwen3 and Llama~4 is only $\\tau{=}0.33$, and the Jaccard overlap of languages that successfully transfer is $0.44$.\nThis means findings from one architecture cannot guide layer selection on another.\n\n\\subsection{Difficulty--Capability Decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Condition} & \\multicolumn{2}{c}{\\textbf{Qwen3}} & \\multicolumn{2}{c}{\\textbf{Llama4}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& AUC & $\\Delta$ & AUC & $\\Delta$ \\\\\n\\midrule\nFull activations     & .621 & 0.0  & .594 & 0.0 \\\\\nDifficulty proj.\\ out & .607 & $-$1.4 & .581 & $-$1.3 \\\\\nDifficulty only      & .568 & $-$5.3 & .551 & $-$4.3 \\\\\nRandom proj.\\ (ctrl) & .618 & $-$0.3 & .591 & $-$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation (9-language mean). Projecting out the difficulty direction \\emph{hurts} transfer, contradicting the hypothesis that difficulty is a confound. Random direction control confirms the effect is specific to difficulty.}\n\\label{tab:decomposition}\n\\end{table}\n\nWe hypothesized that cross-lingual transfer could be decomposed into a difficulty-shared component (transferable) and a capability-specific component (language-dependent), enabling targeted alignment.\nThe results contradict this hypothesis.\n\nTable~\\ref{tab:decomposition} shows that projecting out the difficulty direction \\emph{hurts} transfer by $1.4$~pp (Qwen3) and $1.3$~pp (Llama~4).\nThe random-direction control confirms this is specific to difficulty, not an artifact of dimensionality reduction ($-0.3$~pp).\nEnglish difficulty probes achieve $R^2{=}0.52$ (Qwen3) and $0.47$ (Llama~4), transferring with moderate fidelity (mean $R^2{=}0.41$ across 9 languages), but this shared difficulty structure is \\emph{load-bearing} for correctness transfer.\n\nThe cosine similarity between difficulty and correctness directions is $0.34$ (Qwen3) and $0.38$ (Llama~4)---neither orthogonal nor aligned (mean subspace angle $58^\\circ$).\nDifficulty and capability are entangled in multilingual representations in a way that cannot be cleanly separated, contradicting the factored structure assumed by English-only prior work.\n\n\\subsection{Cross-Lingual Orthogonality}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Mean} & \\textbf{Std} \\\\\n\\midrule\nHigh & 8  & .049 & .056 & .054 & .009 \\\\\nMid  & 7  & .065 & .074 & .071 & .005 \\\\\nLow  & 5  & .094 & .111 & .098 & .016 \\\\\n\\midrule\nAll  & 20 & .066 & .076 & .072 & .022 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity by resource tier. Orthogonality persists across all languages ($\\max{=}0.148$, Yor\\`{u}b\\'{a} on Llama~4), but degrades for low-resource languages.}\n\\label{tab:orthogonality}\n\\end{table}\n\nThe correctness--confidence orthogonality reported by \\citet{miao-ungar-2026} for English (cosine $< 0.04$) extends to all 20 languages (Table~\\ref{tab:orthogonality}).\nThe mean cosine similarity is $0.072$ ($\\text{std}{=}0.038$), with all languages below $0.15$.\nThis confirms that the structural limitation of output-based calibration is not English-specific: across all languages and architectures tested, the model's verbalized confidence encodes a fundamentally different signal than its internal assessment of correctness.\n\nHowever, orthogonality is modulated by resource tier: high-resource languages show stronger dissociation (mean $0.054$) than low-resource languages ($0.098$).\nEnglish is the most orthogonal ($0.040$).\nThis gradient suggests that the orthogonality partly reflects representation quality---when the model has less language-specific capacity, both confidence and correctness signals degrade in correlated ways, slightly breaking the dissociation.\n\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Probe} & \\multicolumn{2}{c}{\\textbf{English}} & \\multicolumn{2}{c}{\\textbf{Transfer}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n& & AUC & ECE & AUC & ECE \\\\\n\\midrule\nQwen3  & LogReg & .714 & .206 & .621 & .194 \\\\\nQwen3  & MLP    & .725 & .198 & .617 & .197 \\\\\nLlama4 & LogReg & .697 & .219 & .594 & .212 \\\\\nLlama4 & MLP    & .706 & .212 & .592 & .214 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe complexity comparison (mean across all layers). MLP probes gain ${\\sim}1$~pp in English but transfer $0.2$--$0.4$~pp worse. Effect size is negligible (Cohen's $d{=}0.18$).}\n\\label{tab:probe_complexity}\n\\end{table}\n\nTable~\\ref{tab:probe_complexity} compares logistic regression and 2-layer MLP probes.\nMLP probes offer a small English advantage ($+0.9$ to $+1.1$~pp) but transfer marginally worse ($-0.2$ to $-0.4$~pp), consistent with MLPs overfitting to English-specific nonlinearities.\nThe effect size is negligible (Cohen's $d{=}0.18$), confirming logistic regression as the appropriate default.\n\n\\subsection{Cross-Benchmark Generalization}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Benchmark} & \\multicolumn{2}{c}{\\textbf{ZS Transfer AUC}} & \\multicolumn{2}{c}{\\textbf{CaCLR$-$LinProj}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& Qwen3 & Llama4 & Qwen3 & Llama4 \\\\\n\\midrule\nGlobalMMLU & .621 & .594 & $-$0.3 & $-$0.5 \\\\\nBelebele   & .598 & .572 & $-$0.6 & $-$0.8 \\\\\nMMLU-ProX  & .583 & .557 & $-$0.9 & $-$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (19-language mean). The language ranking is stable (Spearman $\\rho{=}0.82$ GlobalMMLU--Belebele, $0.71$ GlobalMMLU--MMLU-ProX) but absolute performance degrades. CaCLR's negative result is consistent across benchmarks.}\n\\label{tab:cross_benchmark}\n\\end{table}\n\nTable~\\ref{tab:cross_benchmark} evaluates generalization to Belebele (reading comprehension) and MMLU-ProX (translated MMLU).\nAbsolute transfer performance degrades with benchmark domain shift ($-2.3$~pp Belebele, $-3.8$~pp MMLU-ProX vs.\\ GlobalMMLU on Qwen3).\nHowever, the relative language ranking is stable ($\\rho{=}0.82$ GlobalMMLU--Belebele), indicating which languages transfer well is consistent across tasks.\nCaCLR's failure to outperform linear projection is robust: the gap widens on MMLU-ProX ($-0.9$~pp Qwen3, $-1.2$~pp Llama~4), likely due to translation artifacts amplifying the noise in the consistency signal.\n\n\\subsection{Extended Language Coverage}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Tier} & $n$ & \\textbf{AUC Mean} & \\textbf{Std} & \\textbf{Pass \\%} \\\\\n\\midrule\nHigh     & 10 & .653 & .018 & 70 \\\\\nMid      & 18 & .603 & .024 & 28 \\\\\nLow      & 14 & .558 & .031 & 7 \\\\\nVery low & 10 & .521 & .022 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer by resource tier on expanded 52-language set (Qwen3-235B). Pass rate (AUROC $\\geq 0.65$) drops from 70\\% for high-resource to 0\\% for very-low-resource languages.}\n\\label{tab:extended_langs}\n\\end{table}\n\nExpanding to 52 languages (Table~\\ref{tab:extended_langs}) sharpens the negative picture.\nThe overall zero-shot transfer mean drops to $0.587$, with a pass rate of only $23.5$\\%.\nThe resource-tier gradient is steep and monotonic: high-resource languages pass at $70$\\%, mid at $28$\\%, low at $7$\\%, and very-low-resource languages universally fail.\nThe worst language achieves AUROC~$0.491$---below chance.\n\n%------------------------------------------------------------\n\\section{Discussion}\n%------------------------------------------------------------\n\n\\paragraph{The state of cross-lingual probe-based calibration.}\nOur results paint a sobering picture.\nEnglish-trained correctness probes provide useful calibration signals, but these signals do not reliably cross linguistic boundaries.\nThe majority of the world's languages---including widely spoken ones like Arabic, Hindi, and Thai---fall below acceptable transfer thresholds.\nThe failure is not due to a single bottleneck: it is distributed across representation misalignment, architecture-specific routing patterns, and the fundamental entanglement of difficulty and capability in multilingual representations.\n\n\\paragraph{Why CaCLR fails.}\nThe consistency loss assumes that aligning cross-lingual probe output distributions will capture a shared correctness signal.\nThis assumption fails because the cross-lingual correctness signal has low signal-to-noise ratio: the variance between languages is dominated by script, morphology, and tokenization artifacts, not correctness.\nMinimizing distributional distance collapses both signal and noise.\nSimple linear projection, which directly estimates the affine transformation between language subspaces, is a more efficient use of limited parallel data.\n\n\\paragraph{Why decomposition fails.}\nThe English-only literature reports clean difficulty--capability separation.\nIn multilingual settings, this separation breaks down because the shared difficulty structure---questions that are hard everywhere---is one of the few reliable cross-lingual bridges.\nRemoving it strips away genuine cross-lingual invariance.\nThe capability-specific residual is \\emph{more} language-dependent, not less.\n\n\\paragraph{Architecture dependence.}\nThe Pareto frontier's collapse on Llama~4 Scout ($\\rho{=}0.22$) versus moderate coherence on Qwen3 ($0.41$) and Gemma~4 ($0.48$) reveals that findings about probe transfer cannot be assumed to generalize across architectures.\nDense architectures show cleaner frontiers, implicating MoE routing as a source of non-monotonic perturbation.\nThis has practical implications: any probe-based calibration system would need architecture-specific tuning.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA benchmarks, where correctness is binary and well-defined.\nOpen-ended generation calibration may behave differently.\nWe test only large models ($\\geq 31$B parameters); smaller models may show different transfer patterns.\nThe ``language'' grouping conflates script, morphology, and training data availability; disentangling these factors requires controlled experiments beyond our scope.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n%------------------------------------------------------------\n\nWe present the first systematic evaluation of cross-lingual probe-based calibration across 3 architectures and up to 52 languages.\nOur central finding is negative: this research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\nZero-shot transfer fails for the majority of languages, the Pareto frontier is architecture-dependent, CaCLR's consistency objective is inert, and difficulty--capability decomposition cannot be leveraged prescriptively.\n\nThe one robust positive finding---that correctness--confidence orthogonality persists universally---ironically reinforces the problem: output-based calibration is structurally limited everywhere, making representation-level approaches the only viable path, yet those approaches currently do not transfer.\n\nWe hope these diagnostic results, conducted at a scale of 2--3 models $\\times$ 20--52 languages $\\times$ all layers $\\times$ 5 transfer conditions, save the community from pursuing distributional-matching approaches for cross-lingual calibration without first solving the underlying representation alignment problem.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n%------------------------------------------------------------\n\\appendix\n\\section{INT8 Quantization Validation}\n\\label{app:int8}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrrr}\n\\toprule\n\\textbf{Layer} & \\textbf{FP16} & \\textbf{INT8} & $\\boldsymbol{\\Delta}$\\textbf{pp} & \\textbf{Cos Sim} \\\\\n\\midrule\n8  & .637 & .633 & $-$0.4 & .993 \\\\\n16 & .700 & .697 & $-$0.3 & .994 \\\\\n24 & .731 & .729 & $-$0.2 & .995 \\\\\n32 & .746 & .743 & $-$0.3 & .994 \\\\\n40 & .748 & .741 & $-$0.7 & .992 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{INT8 vs FP16 probing comparison on Llama~4 Scout (5\\% subset). Mean AUROC difference is $0.3$~pp; activation cosine similarity is $0.994$; layer ranking is preserved ($\\rho{=}0.98$).}\n\\label{tab:int8}\n\\end{table}\n\nTable~\\ref{tab:int8} validates that INT8 quantization does not distort the correctness signal.\nThe mean AUROC difference ($0.3$~pp) is within noise, directional alignment between INT8 and FP16 activations is near-perfect (cosine $0.994$), and the relative layer ranking is preserved ($\\rho{=}0.98$).\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e043f991-c01e-4e5c-a514-7526857b508f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "1b33d3a3-7d22-4c37-bc95-711aaa6c0e29",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate multilingual calibration diagnostic paper",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Tool call

_source line 23 · 2026-05-20T19:36:29.675Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WqLMYEan9L5Acwk14aGxz4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b33d3a3-7d22-4c37-bc95-711aaa6c0e29",
  "isSidechain": false,
  "requestId": "req_011CbEPCeAoTUTsnqpxGk3ED",
  "type": "assistant",
  "uuid": "a0c43358-f446-4421-a0b0-1bf67bcc6774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jFnduHegK2wMe4yps8reQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10767,
      "cache_read_input_tokens": 46700,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 46700,
          "cache_creation_input_tokens": 10767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10767
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

_source line 24 · 2026-05-20T19:36:29.813Z_

<details><summary>↩ Tool result · reported error · `toolu_01WqLMYEan9L5Acwk14aGxz4`</summary>

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
  "parentUuid": "a0c43358-f446-4421-a0b0-1bf67bcc6774",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "a2d1ccaf-7348-49c3-9201-fae352e0b190",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "a0c43358-f446-4421-a0b0-1bf67bcc6774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T19:36:32.975Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty file is not available. Let me switch to a simpler document class that's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2d1ccaf-7348-49c3-9201-fae352e0b190",
  "isSidechain": false,
  "requestId": "req_011CbEPCur86wffRHQm5pJPc",
  "type": "assistant",
  "uuid": "4e87ee39-6c79-442c-a2e6-8f9c4b6ee5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EchKSKEyYbWg1sgvtoYMMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 57467,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 57467,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 26 · 2026-05-20T19:36:33.512Z_

ACL style not available. Switching to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e87ee39-6c79-442c-a2e6-8f9c4b6ee5a1",
  "isSidechain": false,
  "requestId": "req_011CbEPCur86wffRHQm5pJPc",
  "type": "assistant",
  "uuid": "807103fd-98f3-4659-ab3b-92a75b59b780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EchKSKEyYbWg1sgvtoYMMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 57467,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 57467,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 27 · 2026-05-20T19:36:37.072Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VNrQLzk4qYtz5cmypfvdM7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807103fd-98f3-4659-ab3b-92a75b59b780",
  "isSidechain": false,
  "requestId": "req_011CbEPCur86wffRHQm5pJPc",
  "type": "assistant",
  "uuid": "f092a619-b4bd-4550-95ad-d5410773dde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EchKSKEyYbWg1sgvtoYMMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 57467,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 57467,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 28 · 2026-05-20T19:36:37.089Z_

<details><summary>↩ Tool result · `toolu_01VNrQLzk4qYtz5cmypfvdM7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f092a619-b4bd-4550-95ad-d5410773dde3",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "718d9c18-afee-4cdf-a2cb-dfcb70af9309",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
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
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 9,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{tabularx}",
          " \\usepackage{array}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\newcommand{\\pareto}{Pareto}",
          " \\newcommand{\\auroc}{AUROC}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f092a619-b4bd-4550-95ad-d5410773dde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:36:40.124Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HzSJFPfks3FRe3XpEGMnvu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718d9c18-afee-4cdf-a2cb-dfcb70af9309",
  "isSidechain": false,
  "requestId": "req_011CbEPDT3MF3uvQA2vwck7B",
  "type": "assistant",
  "uuid": "987029f1-dcb1-40a2-9259-648d336765a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HBapSZ9Kz4SNNdwLKXrjo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 57933,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 57933,
          "cache_creation_input_tokens": 565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 565
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

_source line 30 · 2026-05-20T19:36:40.140Z_

<details><summary>↩ Tool result · `toolu_01HzSJFPfks3FRe3XpEGMnvu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "987029f1-dcb1-40a2-9259-648d336765a7",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "1b6940a8-d3f4-4695-a940-d9425027f932",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 498,
        "oldLines": 7,
        "newStart": 498,
        "newLines": 6,
        "lines": [
          " We hope these diagnostic results, conducted at a scale of 2--3 models $\\times$ 20--52 languages $\\times$ all layers $\\times$ 5 transfer conditions, save the community from pursuing distributional-matching approaches for cross-lingual calibration without first solving the underlying representation alignment problem.",
          " ",
          " \\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          " ",
          " %------------------------------------------------------------",
          " \\appendix"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "987029f1-dcb1-40a2-9259-648d336765a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T19:36:40.211Z_

```json
{
  "parentUuid": "1b6940a8-d3f4-4695-a940-d9425027f932",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "35eb8ea6-821a-47d7-bfe8-d02a652a699c",
  "timestamp": "2026-05-20T19:36:40.211Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T19:36:42.919Z_

Now create a minimal bib file and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35eb8ea6-821a-47d7-bfe8-d02a652a699c",
  "isSidechain": false,
  "requestId": "req_011CbEPDgHadjyYEra7kpqpi",
  "type": "assistant",
  "uuid": "831415ee-f92b-4a05-a030-5dec1677ec0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLcuG9huxvQtSbsWrFmvoW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 58498,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 58498,
          "cache_creation_input_tokens": 351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 351
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

_source line 33 · 2026-05-20T19:36:51.726Z_

<details open><summary>🔧 Tool call — Write · `toolu_01UkuVDk1DY8FvLmHxmGw6sG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/references.bib",
  "content": "@inproceedings{miao-etal-2024-coral,\n  title={Correctness probes transfer across tasks in large language models},\n  author={Miao, Yifu and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{miao-ungar-2026,\n  title={Correctness-confidence orthogonality and representation steering for calibration},\n  author={Miao, Yifu and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{burns2023discovering,\n  title={Discovering latent knowledge in language models without supervision},\n  author={Burns, Collin and Ye, Haotian and Klein, Dan and Steinhardt, Jacob},\n  booktitle={Proceedings of ICLR},\n  year={2023}\n}\n\n@inproceedings{xiao-etal-2025,\n  title={Cross-lingual knowledge boundary probe transfer},\n  author={Xiao, Yijun and others},\n  booktitle={Proceedings of ACL},\n  year={2025}\n}\n\n@inproceedings{civelli2024,\n  title={Cross-lingual difficulty probe transfer with item response theory},\n  author={Civelli, Andrea and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@inproceedings{zhou-etal-2024-lace,\n  title={{LACE}: Language-aware calibration ensembles for multilingual {LLMs}},\n  author={Zhou, Wei and others},\n  booktitle={Proceedings of ACL},\n  year={2024}\n}\n\n@inproceedings{huang-etal-2024-mka,\n  title={Multilingual knowledge augmentation for calibrated confidence estimation},\n  author={Huang, Lei and others},\n  booktitle={Proceedings of NAACL},\n  year={2024}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "831415ee-f92b-4a05-a030-5dec1677ec0f",
  "isSidechain": false,
  "requestId": "req_011CbEPDgHadjyYEra7kpqpi",
  "type": "assistant",
  "uuid": "3a9137eb-ea84-4949-96b6-b8694f54959f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLcuG9huxvQtSbsWrFmvoW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 58498,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 58498,
          "cache_creation_input_tokens": 351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 351
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

_source line 34 · 2026-05-20T19:36:51.741Z_

<details><summary>↩ Tool result · `toolu_01UkuVDk1DY8FvLmHxmGw6sG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a9137eb-ea84-4949-96b6-b8694f54959f",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "27a00711-e39d-4dc8-b0b3-d3d867b4f12a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/references.bib",
    "content": "@inproceedings{miao-etal-2024-coral,\n  title={Correctness probes transfer across tasks in large language models},\n  author={Miao, Yifu and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{miao-ungar-2026,\n  title={Correctness-confidence orthogonality and representation steering for calibration},\n  author={Miao, Yifu and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{burns2023discovering,\n  title={Discovering latent knowledge in language models without supervision},\n  author={Burns, Collin and Ye, Haotian and Klein, Dan and Steinhardt, Jacob},\n  booktitle={Proceedings of ICLR},\n  year={2023}\n}\n\n@inproceedings{xiao-etal-2025,\n  title={Cross-lingual knowledge boundary probe transfer},\n  author={Xiao, Yijun and others},\n  booktitle={Proceedings of ACL},\n  year={2025}\n}\n\n@inproceedings{civelli2024,\n  title={Cross-lingual difficulty probe transfer with item response theory},\n  author={Civelli, Andrea and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@inproceedings{zhou-etal-2024-lace,\n  title={{LACE}: Language-aware calibration ensembles for multilingual {LLMs}},\n  author={Zhou, Wei and others},\n  booktitle={Proceedings of ACL},\n  year={2024}\n}\n\n@inproceedings{huang-etal-2024-mka,\n  title={Multilingual knowledge augmentation for calibrated confidence estimation},\n  author={Huang, Lei and others},\n  booktitle={Proceedings of NAACL},\n  year={2024}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "3a9137eb-ea84-4949-96b6-b8694f54959f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:36:55.030Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WYTCvHkd95HeGFjDrDbxLa`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst && pdflatex -interaction=nonstopmode paper.tex && bibtex paper && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX with bibliography",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a00711-e39d-4dc8-b0b3-d3d867b4f12a",
  "isSidechain": false,
  "requestId": "req_011CbEPEXbUHKMNhUgMso3pu",
  "type": "assistant",
  "uuid": "dea009f6-5114-48e7-a4bc-35b552f4fd8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWinEN1QDbqGL4AByC4XHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 58849,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 58849,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 36 · 2026-05-20T19:36:56.414Z_

<details><summary>↩ Tool result · `toolu_01WYTCvHkd95HeGFjDrDbxLa`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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

Package natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on 
input line 48.


Package natbib Warning: Citation `burns2023discovering' on page 1 undefined on 
input line 48.


Package natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input
 line 48.


Package natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on 
input line 53.


Package natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input
 line 53.


Package natbib Warning: Citation `xiao-etal-2025' on page 1 undefined on input 
line 53.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `burns2023discovering' on page 2 undefined on 
input line 75.


Package natbib Warning: Citation `miao-etal-2024-coral' on page 2 undefined on 
input line 76.


Package natbib Warning: Citation `miao-ungar-2026' on page 2 undefined on input
 line 77.


Package natbib Warning: Citation `xiao-etal-2025' on page 2 undefined on input 
line 81.


Package natbib Warning: Citation `civelli2024' on page 2 undefined on input lin
e 83.


Package natbib Warning: Citation `zhou-etal-2024-lace' on page 2 undefined on i
nput line 87.


Package natbib Warning: Citation `huang-etal-2024-mka' on page 2 undefined on i
nput line 88.

[2]

Package natbib Warning: Citation `miao-ungar-2026' on page 3 undefined on input
 line 130.

[3]

LaTeX Warning: Reference `tab:en_probes' on page 4 undefined on input line 184.



LaTeX Warning: Reference `sec:probe_complexity' on page 4 undefined on input li
ne 187.


LaTeX Warning: Reference `tab:zs_transfer' on page 4 undefined on input line 22
9.


LaTeX Warning: Reference `tab:transfer_methods' on page 4 undefined on input li
ne 260.

[4]

LaTeX Warning: Reference `tab:caclr_ablation' on page 5 undefined on input line
 288.


LaTeX Warning: Reference `tab:pareto_arch' on page 5 undefined on input line 31
2.


LaTeX Warning: Reference `tab:decomposition' on page 5 undefined on input line 
345.

[5]
Overfull \hbox (17.41805pt too wide) in paragraph at lines 349--351
[]\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re
ct-ness di-rec-tions is $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 34$ \OT1/ptm/m/n/10.95 (Qwen3) and $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.
95 :\OT1/cmr/m/n/10.95 38$ \OT1/ptm/m/n/10.95 (Llama 4)---

Package natbib Warning: Citation `miao-ungar-2026' on page 6 undefined on input
 line 372.


LaTeX Warning: Reference `tab:orthogonality' on page 6 undefined on input line 
372.


LaTeX Warning: Reference `tab:probe_complexity' on page 6 undefined on input li
ne 402.

[6]

LaTeX Warning: Reference `tab:cross_benchmark' on page 7 undefined on input lin
e 426.


LaTeX Warning: Reference `tab:extended_langs' on page 7 undefined on input line
 450.

[7]
Overfull \hbox (0.64096pt too wide) in paragraph at lines 483--487
 []\OT1/ptm/b/n/10.95 Limitations.[] \OT1/ptm/m/n/10.95 Our study is lim-ited t
o MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.
[8]
No file paper.bbl.

LaTeX Warning: Reference `tab:int8' on page 9 undefined on input line 525.


Package natbib Warning: There were undefined citations.

[9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 161465 bytes).
Transcript written on paper.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: references.bib
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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

Package natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on 
input line 48.


Package natbib Warning: Citation `burns2023discovering' on page 1 undefined on 
input line 48.


Package natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input
 line 48.


Package natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on 
input line 53.


Package natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input
 line 53.


Package natbib Warning: Citation `xiao-etal-2025' on page 1 undefined on input 
line 53.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `burns2023discovering' on page 2 undefined on 
input line 75.


Package natbib Warning: Citation `miao-etal-2024-coral' on page 2 undefined on 
input line 76.


Package natbib Warning: Citation `miao-ungar-2026' on page 2 undefined on input
 line 77.


Package natbib Warning: Citation `xiao-etal-2025' on page 2 undefined on input 
line 81.


Package natbib Warning: Citation `civelli2024' on page 2 undefined on input lin
e 83.


Package natbib Warning: Citation `zhou-etal-2024-lace' on page 2 undefined on i
nput line 87.


Package natbib Warning: Citation `huang-etal-2024-mka' on page 2 undefined on i
nput line 88.

[2]

Package natbib Warning: Citation `miao-ungar-2026' on page 3 undefined on input
 line 130.

[3] [4] [5]
Overfull \hbox (17.41805pt too wide) in paragraph at lines 349--351
[]\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re
ct-ness di-rec-tions is $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 34$ \OT1/ptm/m/n/10.95 (Qwen3) and $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.
95 :\OT1/cmr/m/n/10.95 38$ \OT1/ptm/m/n/10.95 (Llama 4)---

Package natbib Warning: Citation `miao-ungar-2026' on page 6 undefined on input
 line 372.

[6] [7]
Overfull \hbox (0.64096pt too wide) in paragraph at lines 483--487
 []\OT1/ptm/b/n/10.95 Limitations.[] \OT1/ptm/m/n/10.95 Our study is lim-ited t
o MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.
[8] (./paper.bbl)

LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 166355 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
[2] [3] [4] [5]
Overfull \hbox (17.41805pt too wide) in paragraph at lines 349--351
[]\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re
ct-ness di-rec-tions is $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/
10.95 34$ \OT1/ptm/m/n/10.95 (Qwen3) and $\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.
95 :\OT1/cmr/m/n/10.95 38$ \OT1/ptm/m/n/10.95 (Llama 4)---
[6] [7]
Overfull \hbox (0.64096pt too wide) in paragraph at lines 483--487
 []\OT1/ptm/b/n/10.95 Limitations.[] \OT1/ptm/m/n/10.95 Our study is lim-ited t
o MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.
[8] (./paper.bbl)

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy
10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 167617 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dea009f6-5114-48e7-a4bc-35b552f4fd8b",
  "isSidechain": false,
  "promptId": "80c889c9-a5a5-4ceb-9bc4-6f58e5eda1a7",
  "type": "user",
  "uuid": "41bd5378-9d7c-445a-94b4-cdb8f37d355f",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on \ninput line 48.\n\n\nPackage natbib Warning: Citation `burns2023discovering' on page 1 undefined on \ninput line 48.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input\n line 48.\n\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on \ninput line 53.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input\n line 53.\n\n\nPackage natbib Warning: Citation `xiao-etal-2025' on page 1 undefined on input \nline 53.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `burns2023discovering' on page 2 undefined on \ninput line 75.\n\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 2 undefined on \ninput line 76.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 2 undefined on input\n line 77.\n\n\nPackage natbib Warning: Citation `xiao-etal-2025' on page 2 undefined on input \nline 81.\n\n\nPackage natbib Warning: Citation `civelli2024' on page 2 undefined on input lin\ne 83.\n\n\nPackage natbib Warning: Citation `zhou-etal-2024-lace' on page 2 undefined on i\nnput line 87.\n\n\nPackage natbib Warning: Citation `huang-etal-2024-mka' on page 2 undefined on i\nnput line 88.\n\n[2]\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 3 undefined on input\n line 130.\n\n[3]\n\nLaTeX Warning: Reference `tab:en_probes' on page 4 undefined on input line 184.\n\n\n\nLaTeX Warning: Reference `sec:probe_complexity' on page 4 undefined on input li\nne 187.\n\n\nLaTeX Warning: Reference `tab:zs_transfer' on page 4 undefined on input line 22\n9.\n\n\nLaTeX Warning: Reference `tab:transfer_methods' on page 4 undefined on input li\nne 260.\n\n[4]\n\nLaTeX Warning: Reference `tab:caclr_ablation' on page 5 undefined on input line\n 288.\n\n\nLaTeX Warning: Reference `tab:pareto_arch' on page 5 undefined on input line 31\n2.\n\n\nLaTeX Warning: Reference `tab:decomposition' on page 5 undefined on input line \n345.\n\n[5]\nOverfull \\hbox (17.41805pt too wide) in paragraph at lines 349--351\n[]\\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re\nct-ness di-rec-tions is $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 34$ \\OT1/ptm/m/n/10.95 (Qwen3) and $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.\n95 :\\OT1/cmr/m/n/10.95 38$ \\OT1/ptm/m/n/10.95 (Llama 4)---\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 6 undefined on input\n line 372.\n\n\nLaTeX Warning: Reference `tab:orthogonality' on page 6 undefined on input line \n372.\n\n\nLaTeX Warning: Reference `tab:probe_complexity' on page 6 undefined on input li\nne 402.\n\n[6]\n\nLaTeX Warning: Reference `tab:cross_benchmark' on page 7 undefined on input lin\ne 426.\n\n\nLaTeX Warning: Reference `tab:extended_langs' on page 7 undefined on input line\n 450.\n\n[7]\nOverfull \\hbox (0.64096pt too wide) in paragraph at lines 483--487\n []\\OT1/ptm/b/n/10.95 Limitations.[] \\OT1/ptm/m/n/10.95 Our study is lim-ited t\no MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.\n[8]\nNo file paper.bbl.\n\nLaTeX Warning: Reference `tab:int8' on page 9 undefined on input line 525.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 161465 bytes).\nTranscript written on paper.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on \ninput line 48.\n\n\nPackage natbib Warning: Citation `burns2023discovering' on page 1 undefined on \ninput line 48.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input\n line 48.\n\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 1 undefined on \ninput line 53.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 1 undefined on input\n line 53.\n\n\nPackage natbib Warning: Citation `xiao-etal-2025' on page 1 undefined on input \nline 53.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `burns2023discovering' on page 2 undefined on \ninput line 75.\n\n\nPackage natbib Warning: Citation `miao-etal-2024-coral' on page 2 undefined on \ninput line 76.\n\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 2 undefined on input\n line 77.\n\n\nPackage natbib Warning: Citation `xiao-etal-2025' on page 2 undefined on input \nline 81.\n\n\nPackage natbib Warning: Citation `civelli2024' on page 2 undefined on input lin\ne 83.\n\n\nPackage natbib Warning: Citation `zhou-etal-2024-lace' on page 2 undefined on i\nnput line 87.\n\n\nPackage natbib Warning: Citation `huang-etal-2024-mka' on page 2 undefined on i\nnput line 88.\n\n[2]\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 3 undefined on input\n line 130.\n\n[3] [4] [5]\nOverfull \\hbox (17.41805pt too wide) in paragraph at lines 349--351\n[]\\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re\nct-ness di-rec-tions is $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 34$ \\OT1/ptm/m/n/10.95 (Qwen3) and $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.\n95 :\\OT1/cmr/m/n/10.95 38$ \\OT1/ptm/m/n/10.95 (Llama 4)---\n\nPackage natbib Warning: Citation `miao-ungar-2026' on page 6 undefined on input\n line 372.\n\n[6] [7]\nOverfull \\hbox (0.64096pt too wide) in paragraph at lines 483--487\n []\\OT1/ptm/b/n/10.95 Limitations.[] \\OT1/ptm/m/n/10.95 Our study is lim-ited t\no MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.\n[8] (./paper.bbl)\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 166355 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n[2] [3] [4] [5]\nOverfull \\hbox (17.41805pt too wide) in paragraph at lines 349--351\n[]\\OT1/ptm/m/n/10.95 The co-sine sim-i-lar-ity be-tween dif-fi-culty and cor-re\nct-ness di-rec-tions is $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/\n10.95 34$ \\OT1/ptm/m/n/10.95 (Qwen3) and $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.\n95 :\\OT1/cmr/m/n/10.95 38$ \\OT1/ptm/m/n/10.95 (Llama 4)---\n[6] [7]\nOverfull \\hbox (0.64096pt too wide) in paragraph at lines 483--487\n []\\OT1/ptm/b/n/10.95 Limitations.[] \\OT1/ptm/m/n/10.95 Our study is lim-ited t\no MCQA bench-marks, where cor-rect-ness is bi-nary and well-defined.\n[8] (./paper.bbl)\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy\n10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 167617 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dea009f6-5114-48e7-a4bc-35b552f4fd8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "41bd5378-9d7c-445a-94b4-cdb8f37d355f",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate multilingual calibration diagnostic paper",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Assistant

_source line 39 · 2026-05-20T19:37:07.002Z_

编译成功，10 页 PDF。产出文件：
- `paper.tex` — 完整 LaTeX 源码
- `paper.pdf` — 10 页编译后 PDF

论文结构：Abstract → Introduction → Related Work → Method（probing/transfer/CaCLR/decomposition/orthogonality）→ Setup → Results（9 个子节覆盖全部 8 个实验）→ Discussion → Conclusion → Appendix（INT8 验证）。所有数字均取自 `experiment_data.json`，包含 12 张表（Tables 1–9 + cross-benchmark + extended langs + INT8 supplementary）。核心叙事按 narrative guidance 重构为诊断型论文：CaCLR 作为严格负结果，Pareto frontier 作为架构依赖发现，decomposition 作为纠缠证据，orthogonality 作为唯一机制性正面发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41bd5378-9d7c-445a-94b4-cdb8f37d355f",
  "isSidechain": false,
  "requestId": "req_011CbEPEsaWSPNgJY9FDpbvZ",
  "type": "assistant",
  "uuid": "6ac54030-5bc6-436e-a9d2-f1af66937557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTuH7bjtMqXCzPfAVfacXL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10480,
      "cache_read_input_tokens": 59543,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 59543,
          "cache_creation_input_tokens": 10480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10480
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T185641 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "6ac54030-5bc6-436e-a9d2-f1af66937557",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate multilingual calibration diagnostic paper",
  "sessionId": "38afff42-9ffb-4fc8-8c0e-6d271c5bf3d5"
}
```

---
