# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/93fd10ce-8877-4672-be96-d4a16ab6d261.jsonl`
- **Structured JSON:** [`4b16516495ea7db684d1.json`](../../sessions/4b/4b16516495ea7db684d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:29:11.982Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:29:11.982Z",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。以 Simpson's Paradox 几何洞见为核心新颖性开篇—— raw CKA-transfer correlation 为负（depth confound），partial correlation controlling for depth 在双架构上均显著为正（p < 0.01），揭示 within-layer CKA genuinely predicts transfer quality。CaCLR 作为正面方法贡献（+3.5pp mean over ZS），不是 headline 但 构成因果链第三环。标题强调 'geometric analysis reveals when and why cross-lingual calibration transfer succeeds'。四条 claim 完整因果链保留：Pareto discovery（architecture- dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs capability separation）→ CaCLR method（consistency loss provides measurable gain at deep layers）→ CKA geometric explanation（Simpson's Paradox, subspace persistence）。 Control task warning（28% low-resource artifacts）和 linear projection sample efficiency （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52） 为 practitioner 提供直接指导。无需弱化任何 claims。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T05:29:11.986Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:29:11.986Z",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-21T05:29:12.006Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。以 Simpson's Paradox 几何洞见为核心新颖性开篇—— raw CKA-transfer correlation 为负（depth confound），partial correlation controlling for depth 在双架构上均显著为正（p < 0.01），揭示 within-layer CKA genuinely predicts transfer quality。CaCLR 作为正面方法贡献（+3.5pp mean over ZS），不是 headline 但 构成因果链第三环。标题强调 'geometric analysis reveals when and why cross-lingual calibration transfer succeeds'。四条 claim 完整因果链保留：Pareto discovery（architecture- dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs capability separation）→ CaCLR method（consistency loss provides measurable gain at deep layers）→ CKA geometric explanation（Simpson's Paradox, subspace persistence）。 Control task warning（28% low-resource artifacts）和 linear projection sample efficiency （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52） 为 practitioner 提供直接指导。无需弱化任何 claims。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "f6dc6897-cd16-45d3-b64f-38ba72b81036",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:29:12.005Z_

```json
{
  "parentUuid": "f6dc6897-cd16-45d3-b64f-38ba72b81036",
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
  "uuid": "2379515d-defa-434e-bd44-2268db397c3c",
  "timestamp": "2026-05-21T05:29:12.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:29:12.005Z_

```json
{
  "parentUuid": "2379515d-defa-434e-bd44-2268db397c3c",
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
  "uuid": "a6e7b8f2-86ac-4506-a324-7124709888c1",
  "timestamp": "2026-05-21T05:29:12.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T05:29:12.005Z_

```json
{
  "parentUuid": "a6e7b8f2-86ac-4506-a324-7124709888c1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "59e84a7f-c38b-4d9b-b71c-c7e3b1efe0f2",
  "timestamp": "2026-05-21T05:29:12.005Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
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
  "aiTitle": "Generate cross-lingual calibration transfer paper",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Assistant

_source line 8 · 2026-05-21T05:29:14.784Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e84a7f-c38b-4d9b-b71c-c7e3b1efe0f2",
  "isSidechain": false,
  "requestId": "req_011CbFAQMgw3H5vVHTCAvfkk",
  "type": "assistant",
  "uuid": "4295f743-b10e-46d3-9238-b8f74704cd72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2UHANrtG6pERDo8u1Ch1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 9 · 2026-05-21T05:29:15.742Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GHV62fTB3ahnsfgiuk5QxX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4295f743-b10e-46d3-9238-b8f74704cd72",
  "isSidechain": false,
  "requestId": "req_011CbFAQMgw3H5vVHTCAvfkk",
  "type": "assistant",
  "uuid": "2c6707ed-977f-49c6-8bb4-3130472df7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2UHANrtG6pERDo8u1Ch1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 10 · 2026-05-21T05:29:15.990Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbbnGznd8kDgVLDEUWEJgz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c6707ed-977f-49c6-8bb4-3130472df7e0",
  "isSidechain": false,
  "requestId": "req_011CbFAQMgw3H5vVHTCAvfkk",
  "type": "assistant",
  "uuid": "8855c060-afc5-43f4-85da-5716df43153f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2UHANrtG6pERDo8u1Ch1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 11 · 2026-05-21T05:29:15.997Z_

<details><summary>↩ Tool result · `toolu_01NbbnGznd8kDgVLDEUWEJgz`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	### Key Empirical Contributions (elevated from appendix to main body, D012)
36	- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
37	- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
38	- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.
39	
40	## Story Spine
41	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
42	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
43	- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
44	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
45	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
46	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
47	
48	## Field-Level Significance
49	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
50	
51	## Anticipated Reviewer Concerns & Responses
52	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
53	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
54	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
55	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
56	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
57	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
58	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
59	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
60	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
61	10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
62	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
63	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
64	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
65	14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.
66	
67	## Additional Related Work Coverage (Dream-identified gaps)
68	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
69	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
70	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
71	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
72	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
73	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
74	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
75	
76	## Differentiation from Closest Prior Work
77	| Paper | Their Focus | Our Difference |
78	|-------|-------------|----------------|
79	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
80	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
81	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
82	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
83	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8855c060-afc5-43f4-85da-5716df43153f",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "7203da28-cb02-4bd5-84de-75729aff38ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "8855c060-afc5-43f4-85da-5716df43153f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T05:29:16.093Z_

<details><summary>↩ Tool result · `toolu_01GHV62fTB3ahnsfgiuk5QxX`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th), 20 typologically diverse languages, English logistic regression probes, 5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100, CaCLR。重点验证 MVP 发现的 strong depth-transferability tradeoff 是否在大模型上保持。\n",
5	    "results": {
6	      "en_best_auroc": 0.81,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.58,
10	        0.81
11	      ],
12	      "en_ece_raw_best": 0.168,
13	      "zs_mean_auroc_20lang_best_transfer_layer": 0.72,
14	      "zs_best_transfer_layer_idx": 52,
15	      "zs_pass_rate_20lang": 0.9,
16	      "zs_fail_langs": [
17	        "yo",
18	        "te"
19	      ],
20	      "zs_auroc_by_tier": {
21	        "HIGH_mean": 0.76,
22	        "MID_mean": 0.72,
23	        "LOW_mean": 0.63
24	      },
25	      "zs_auroc_selected": {
26	        "zh": 0.77,
27	        "es": 0.76,
28	        "fr": 0.76,
29	        "de": 0.77,
30	        "ja": 0.75,
31	        "nl": 0.76,
32	        "pt": 0.75,
33	        "it": 0.75,
34	        "ar": 0.73,
35	        "hi": 0.71,
36	        "ko": 0.72,
37	        "tr": 0.71,
38	        "ru": 0.74,
39	        "vi": 0.7,
40	        "th": 0.69,
41	        "sw": 0.63,
42	        "bn": 0.65,
43	        "yo": 0.57,
44	        "ig": 0.61,
45	        "te": 0.58
46	      },
47	      "per_lang_spearman_rho_median": -0.64,
48	      "per_lang_significant_at_005": 15,
49	      "global_spearman_rho": -0.91,
50	      "global_spearman_p": 0.0001,
51	      "pareto_frontier_layers": [
52	        40,
53	        44,
54	        48,
55	        52,
56	        56
57	      ],
58	      "pareto_en_zs_gap_at_knee_pp": 4.2,
59	      "mean_shift_delta_auroc": 0.0,
60	      "linproj_200pairs_mean_auroc": 0.74,
61	      "fewshot_25_mean_auroc": 0.708,
62	      "fewshot_100_mean_auroc": 0.735
63	    },
64	    "tables": [
65	      {
66	        "name": "Table 1: Qwen3-235B Pareto Frontier (selected layers)",
67	        "columns": [
68	          "layer_idx",
69	          "depth_pct",
70	          "en_auroc",
71	          "zs_mean_20",
72	          "zs_drop_pp",
73	          "on_pareto"
74	        ],
75	        "rows": [
76	          [
77	            4,
78	            4,
79	            0.58,
80	            0.572,
81	            0.8,
82	            false
83	          ],
84	          [
85	            12,
86	            13,
87	            0.645,
88	            0.632,
89	            1.3,
90	            false
91	          ],
92	          [
93	            20,
94	            21,
95	            0.71,
96	            0.695,
97	            1.5,
98	            false
99	          ],
100	          [
101	            28,
102	            30,
103	            0.752,
104	            0.733,
105	            1.9,
106	            false
107	          ],
108	          [
109	            36,
110	            38,
111	            0.778,
112	            0.752,
113	            2.6,
114	            false
115	          ],
116	          [
117	            40,
118	            43,
119	            0.788,
120	            0.748,
121	            4.0,
122	            true
123	          ],
124	          [
125	            44,
126	            47,
127	            0.796,
128	            0.74,
129	            5.6,
130	            true
131	          ],
132	          [
133	            48,
134	            51,
135	            0.802,
136	            0.732,
137	            7.0,
138	            true
139	          ],
140	          [
141	            52,
142	            55,
143	            0.806,
144	            0.72,
145	            8.6,
146	            true
147	          ],
148	          [
149	            56,
150	            60,
151	            0.808,
152	            0.706,
153	            10.2,
154	            true
155	          ],
156	          [
157	            60,
158	            64,
159	            0.81,
160	            0.69,
161	            12.0,
162	            false
163	          ],
164	          [
165	            68,
166	            72,
167	            0.81,
168	            0.661,
169	            14.9,
170	            false
171	          ],
172	          [
173	            72,
174	            77,
175	            0.81,
176	            0.638,
177	            17.2,
178	            false
179	          ],
180	          [
181	            80,
182	            85,
183	            0.805,
184	            0.601,
185	            20.4,
186	            false
187	          ],
188	          [
189	            88,
190	            94,
191	            0.792,
192	            0.558,
193	            23.4,
194	            false
195	          ],
196	          [
197	            92,
198	            98,
199	            0.778,
200	            0.531,
201	            24.7,
202	            false
203	          ]
204	        ]
205	      },
206	      {
207	        "name": "Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3",
208	        "columns": [
209	          "language",
210	          "tier",
211	          "spearman_rho",
212	          "p_value",
213	          "significant"
214	        ],
215	        "rows": [
216	          [
217	            "zh",
218	            "HIGH",
219	            -0.72,
220	            0.001,
221	            true
222	          ],
223	          [
224	            "es",
225	            "HIGH",
226	            -0.68,
227	            0.002,
228	            true
229	          ],
230	          [
231	            "fr",
232	            "HIGH",
233	            -0.7,
234	            0.001,
235	            true
236	          ],
237	          [
238	            "de",
239	            "HIGH",
240	            -0.69,
241	            0.002,
242	            true
243	          ],
244	          [
245	            "ja",
246	            "HIGH",
247	            -0.74,
248	            0.001,
249	            true
250	          ],
251	          [
252	            "nl",
253	            "HIGH",
254	            -0.67,
255	            0.003,
256	            true
257	          ],
258	          [
259	            "pt",
260	            "MID",
261	            -0.65,
262	            0.004,
263	            true
264	          ],
265	          [
266	            "it",
267	            "MID",
268	            -0.66,
269	            0.003,
270	            true
271	          ],
272	          [
273	            "ar",
274	            "MID",
275	            -0.71,
276	            0.001,
277	            true
278	          ],
279	          [
280	            "hi",
281	            "MID",
282	            -0.63,
283	            0.005,
284	            true
285	          ],
286	          [
287	            "ko",
288	            "MID",
289	            -0.67,
290	            0.003,
291	            true
292	          ],
293	          [
294	            "tr",
295	            "MID",
296	            -0.62,
297	            0.006,
298	            true
299	          ],
300	          [
301	            "ru",
302	            "MID",
303	            -0.69,
304	            0.002,
305	            true
306	          ],
307	          [
308	            "vi",
309	            "MID",
310	            -0.61,
311	            0.008,
312	            true
313	          ],
314	          [
315	            "th",
316	            "MID",
317	            -0.58,
318	            0.012,
319	            true
320	          ],
321	          [
322	            "sw",
323	            "LOW",
324	            -0.52,
325	            0.025,
326	            true
327	          ],
328	          [
329	            "bn",
330	            "LOW",
331	            -0.55,
332	            0.018,
333	            false
334	          ],
335	          [
336	            "yo",
337	            "LOW",
338	            -0.48,
339	            0.042,
340	            false
341	          ],
342	          [
343	            "ig",
344	            "LOW",
345	            -0.51,
346	            0.028,
347	            false
348	          ],
349	          [
350	            "te",
351	            "LOW",
352	            -0.45,
353	            0.058,
354	            false
355	          ]
356	        ]
357	      }
358	    ],
359	    "figures": [],
360	    "analysis": "Qwen3-235B 展现 strong, consistent depth-transferability tradeoff： global Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。 Pareto frontier 包含 5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal (L72) 与 ZS-optimal (L52) 相隔 20 层 / 22pp depth，远大于 MVP 的 3 层 间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多 空间进行 language-specific specialization。High-resource 语言在 Pareto knee 以下也保持 AUROC > 0.74，但 low-resource 在 70% depth 后急剧下降。 这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer 对 low-resource 影响更大（CKA 基线更低，cliff 更早触及）。\n\n\nQwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear probing scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability tradeoff 比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal layer (L52, 55% depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于 Qwen 架构特征：MoE routing 在深层产生 language-specific expert 激活模式， 导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。 15/20 languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是 跨语言一致的。2 个 fail 语言（yo, te）的 AUROC < 0.60 因为 Qwen3 pretraining corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding 层的 representation quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为 StandardScaler + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。 Linear projection (200 pairs) 提供 +2pp 因为 Procrustes alignment 捕获了 correctness subspace 的旋转，但不触及 distributional matching。\n"
361	  },
362	  {
363	    "name": "Full Pareto Frontier — Llama 4 Scout",
364	    "description": "48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed tradeoff pattern 是否是 Llama 架构家族特征。\n",
365	    "results": {
366	      "en_best_auroc": 0.79,
367	      "en_best_layer_idx": 36,
368	      "en_auroc_range": [
369	        0.56,
370	        0.79
371	      ],
372	      "en_ece_raw_best": 0.182,
373	      "zs_mean_auroc_20lang_best_transfer_layer": 0.7,
374	      "zs_best_transfer_layer_idx": 28,
375	      "zs_pass_rate_20lang": 0.85,
376	      "zs_fail_langs": [
377	        "yo",
378	        "te",
379	        "ig"
380	      ],
381	      "zs_auroc_by_tier": {
382	        "HIGH_mean": 0.74,
383	        "MID_mean": 0.7,
384	        "LOW_mean": 0.61
385	      },
386	      "per_lang_spearman_rho_median": -0.28,
387	      "per_lang_significant_at_005": 6,
388	      "per_lang_positive_rho_langs": [
389	        "ar",
390	        "hi",
391	        "ko"
392	      ],
393	      "global_spearman_rho": -0.78,
394	      "global_spearman_p": 0.003,
395	      "pareto_frontier_layers": [
396	        20,
397	        24,
398	        28
399	      ],
400	      "mean_shift_delta_auroc": 0.0,
401	      "linproj_200pairs_mean_auroc": 0.718,
402	      "fewshot_25_mean_auroc": 0.692,
403	      "fewshot_100_mean_auroc": 0.718
404	    },
405	    "tables": [
406	      {
407	        "name": "Table 3: Llama 4 Scout Pareto Frontier",
408	        "columns": [
409	          "layer_idx",
410	          "depth_pct",
411	          "en_auroc",
412	          "zs_mean_20",
413	          "zs_drop_pp",
414	          "on_pareto"
415	        ],
416	        "rows": [
417	          [
418	            4,
419	            8,
420	            0.56,
421	            0.552,
422	            0.8,
423	            false
424	          ],
425	          [
426	            8,
427	            17,
428	            0.635,
429	            0.625,
430	            1.0,
431	            false
432	          ],
433	          [
434	            12,
435	            25,
436	            0.695,
437	            0.682,
438	            1.3,
439	            false
440	          ],
441	          [
442	            16,
443	            33,
444	            0.735,
445	            0.718,
446	            1.7,
447	            false
448	          ],
449	          [
450	            20,
451	            42,
452	            0.758,
453	            0.724,
454	            3.4,
455	            true
456	          ],
457	          [
458	            24,
459	            50,
460	            0.772,
461	            0.714,
462	            5.8,
463	            true
464	          ],
465	          [
466	            28,
467	            58,
468	            0.782,
469	            0.7,
470	            8.2,
471	            true
472	          ],
473	          [
474	            32,
475	            67,
476	            0.789,
477	            0.681,
478	            10.8,
479	            false
480	          ],
481	          [
482	            36,
483	            75,
484	            0.79,
485	            0.655,
486	            13.5,
487	            false
488	          ],
489	          [
490	            40,
491	            83,
492	            0.785,
493	            0.625,
494	            16.0,
495	            false
496	          ],
497	          [
498	            44,
499	            92,
500	            0.772,
501	            0.589,
502	            18.3,
503	            false
504	          ],
505	          [
506	            48,
507	            100,
508	            0.748,
509	            0.548,
510	            20.0,
511	            false
512	          ]
513	        ]
514	      },
515	      {
516	        "name": "Table 4: Architecture-Dependent Pareto Comparison",
517	        "columns": [
518	          "metric",
519	          "Qwen3_235B",
520	          "Llama4_Scout",
521	          "interpretation"
522	        ],
523	        "rows": [
524	          [
525	            "global_rho",
526	            -0.91,
527	            -0.78,
528	            "both significant but Qwen stronger"
529	          ],
530	          [
531	            "per_lang_sig_count",
532	            "15/20",
533	            "6/20",
534	            "Qwen consistent, Llama mixed"
535	          ],
536	          [
537	            "median_per_lang_rho",
538	            -0.64,
539	            -0.28,
540	            "2.3x difference in effect size"
541	          ],
542	          [
543	            "positive_rho_langs",
544	            0,
545	            3,
546	            "Llama has ar/hi/ko reversed"
547	          ],
548	          [
549	            "best_transfer_depth_pct",
550	            55,
551	            58,
552	            "comparable location"
553	          ],
554	          [
555	            "en_zs_gap_at_knee_pp",
556	            4.2,
557	            3.4,
558	            "comparable magnitude"
559	          ]
560	        ]
561	      },
562	      {
563	        "name": "Table 5: Transfer Conditions Comparison (both models, at best-transfer layer)",
564	        "columns": [
565	          "condition",
566	          "Qwen3_mean_20",
567	          "Llama4_mean_20",
568	          "combined_mean"
569	        ],
570	        "rows": [
571	          [
572	            "zero-shot",
573	            0.72,
574	            0.7,
575	            0.71
576	          ],
577	          [
578	            "mean-shift",
579	            0.72,
580	            0.7,
581	            0.71
582	          ],
583	          [
584	            "linear_proj_200",
585	            0.74,
586	            0.718,
587	            0.729
588	          ],
589	          [
590	            "few-shot-25",
591	            0.708,
592	            0.692,
593	            0.7
594	          ],
595	          [
596	            "few-shot-100",
597	            0.735,
598	            0.718,
599	            0.727
600	          ]
601	        ]
602	      }
603	    ],
604	    "figures": [],
605	    "analysis": "Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的 global rho 都显著（满足 pareto_spearman_rho_significant_archs = 2 的 约束），但 effect size 差异明显。Qwen3 的 strong tradeoff 意味着 practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择； Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 \"free-ride\" 深层的 EN improvement 而不牺牲 transfer。这一差异无法从 domain adaptation theory 预测——它是架构特有的 empirical finding。 Best-transfer depth 在两个架构上收敛至 55-58%，暗示一个 universal \"mid-depth transfer zone\"，但 frontier 的 steepness 是 architecture-specific。\n\n\nLlama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language 分析揭示了明显的异质性：仅 6/20 languages 有显著负 ρ，而 ar/hi/ko 展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31 优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta 的训练策略使 ar/hi/ko 在深层保持更好的 cross-lingual alignment，可能 因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。 Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language 分析揭示这不是 universal pattern。与 Qwen3 的对比清晰：Qwen3 的 15/20 significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一 architecture-dependent tradeoff strength 是 Claim 1 的核心发现。\n"
606	  },
607	  {
608	    "name": "CKA Cross-Lingual Similarity & Simpson's Paradox Analysis",
609	    "description": "Linear CKA (EN vs each target) at every probed layer, 20 languages × 2 models。核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b) partial Spearman controlling for normalized depth — THE single most important analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。验证 pilot finding 的 Simpson's Paradox 在 full-scale 上双架构复现。\n",
610	    "results": {
611	      "qwen3_raw_rho": -0.36,
612	      "qwen3_raw_p": 0.0001,
613	      "llama4_raw_rho": -0.41,
614	      "llama4_raw_p": 0.0001,
615	      "qwen3_partial_rho": 0.48,
616	      "qwen3_partial_p": 0.002,
617	      "qwen3_partial_bootstrap_ci_95": [
618	        0.31,
619	        0.62
620	      ],
621	      "llama4_partial_rho": 0.41,
622	      "llama4_partial_p": 0.008,
623	      "llama4_partial_bootstrap_ci_95": [
624	        0.22,
625	        0.57
626	      ],
627	      "simpson_paradox_confirmed_both_archs": true,
628	      "qwen3_per_layer_positive_count": 18,
629	      "qwen3_per_layer_significant_count": 6,
630	      "llama4_per_layer_positive_count": 9,
631	      "llama4_per_layer_significant_count": 3,
632	      "qwen3_cka_peak_layer": 16,
633	      "qwen3_cka_peak_value": 0.82,
634	      "qwen3_cka_at_en_optimal_layer": 0.28,
635	      "qwen3_cka_cliff_onset_depth_pct": 55,
636	      "llama4_cka_peak_layer": 12,
637	      "llama4_cka_peak_value": 0.84,
638	      "llama4_cka_at_en_optimal_layer": 0.35,
639	      "llama4_cka_cliff_onset_depth_pct": 50,
640	      "transfer_collapse_cka_threshold": 0.35,
641	      "below_threshold_mean_zs_auroc": 0.58,
642	      "above_threshold_mean_zs_auroc": 0.72,
643	      "correctness_subspace_angle_within_layer_mean_deg": 12.4,
644	      "correctness_subspace_angle_across_layer_mean_deg": 38.7,
645	      "correctness_direction_persists_despite_global_cka_decline": true
646	    },
647	    "tables": [
648	      {
649	        "name": "Table 6: Simpson's Paradox — Raw vs Partial Correlation",
650	        "columns": [
651	          "model",
652	          "analysis",
653	          "spearman_rho",
654	          "p_value",
655	          "bootstrap_95CI",
656	          "interpretation"
657	        ],
658	        "rows": [
659	          [
660	            "Qwen3-235B",
661	            "raw pooled (CKA vs ZS AUROC)",
662	            -0.36,
663	            "<0.001",
664	            "[-0.44, -0.27]",
665	            "negative — depth confound"
666	          ],
667	          [
668	            "Qwen3-235B",
669	            "partial (controlling depth)",
670	            0.48,
671	            0.002,
672	            "[+0.31, +0.62]",
673	            "positive — genuine geometric signal"
674	          ],
675	          [
676	            "Llama4 Scout",
677	            "raw pooled (CKA vs ZS AUROC)",
678	            -0.41,
679	            "<0.001",
680	            "[-0.50, -0.31]",
681	            "negative — depth confound"
682	          ],
683	          [
684	            "Llama4 Scout",
685	            "partial (controlling depth)",
686	            0.41,
687	            0.008,
688	            "[+0.22, +0.57]",
689	            "positive — genuine geometric signal"
690	          ]
691	        ]
692	      },
693	      {
694	        "name": "Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)",
695	        "columns": [
696	          "layer_idx",
697	          "depth_pct",
698	          "mean_CKA_20lang",
699	          "spearman_rho_n20",
700	          "p_value"
701	        ],
702	        "rows": [
703	          [
704	            12,
705	            13,
706	            0.78,
707	            0.52,
708	            0.019
709	          ],
710	          [
711	            20,
712	            21,
713	            0.81,
714	            0.48,
715	            0.032
716	          ],
717	          [
718	            28,
719	            30,
720	            0.76,
721	            0.55,
722	            0.012
723	          ],
724	          [
725	            36,
726	            38,
727	            0.68,
728	            0.51,
729	            0.022
730	          ],
731	          [
732	            44,
733	            47,
734	            0.56,
735	            0.46,
736	            0.041
737	          ],
738	          [
739	            52,
740	            55,
741	            0.45,
742	            0.43,
743	            0.058
744	          ],
745	          [
746	            60,
747	            64,
748	            0.38,
749	            0.38,
750	            0.098
751	          ],
752	          [
753	            68,
754	            72,
755	            0.3,
756	            0.33,
757	            0.155
758	          ],
759	          [
760	            72,
761	            77,
762	            0.28,
763	            0.28,
764	            0.231
765	          ],
766	          [
767	            80,
768	            85,
769	            0.22,
770	            0.21,
771	            0.372
772	          ]
773	        ]
774	      },
775	      {
776	        "name": "Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)",
777	        "columns": [
778	          "depth_pct",
779	          "HIGH_CKA",
780	          "MID_CKA",
781	          "LOW_CKA",
782	          "overall_CKA"
783	        ],
784	        "rows": [
785	          [
786	            13,
787	            0.86,
788	            0.79,
789	            0.62,
790	            0.78
791	          ],
792	          [
793	            30,
794	            0.84,
795	            0.77,
796	            0.58,
797	            0.76
798	          ],
799	          [
800	            47,
801	            0.68,
802	            0.56,
803	            0.35,
804	            0.56
805	          ],
806	          [
807	            64,
808	            0.48,
809	            0.37,
810	            0.22,
811	            0.38
812	          ],
813	          [
814	            77,
815	            0.38,
816	            0.27,
817	            0.14,
818	            0.28
819	          ],
820	          [
821	            94,
822	            0.25,
823	            0.18,
824	            0.09,
825	            0.19
826	          ]
827	        ]
828	      },
829	      {
830	        "name": "Table 9: Subspace Angle Analysis (correctness direction)",
831	        "columns": [
832	          "comparison_type",
833	          "mean_angle_deg",
834	          "std_deg",
835	          "interpretation"
836	        ],
837	        "rows": [
838	          [
839	            "within-layer cross-language (same layer, different langs)",
840	            12.4,
841	            5.8,
842	            "highly aligned — correctness direction is near-universal"
843	          ],
844	          [
845	            "cross-layer same-language (same lang, different layers)",
846	            38.7,
847	            11.2,
848	            "significant drift — direction rotates with depth"
849	          ],
850	          [
851	            "random baseline (shuffled)",
852	            87.3,
853	            2.1,
854	            "near-orthogonal — signal is non-trivial"
855	          ]
856	        ]
857	      }
858	    ],
859	    "figures": [],
860	    "analysis": "Simpson's Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002, Llama=+0.41 p=0.008），是本文的核心几何洞见。这不是 trivially expected from measurement overlap（CKA 和 transfer AUROC 都衡量 EN-target 相似性） ——sign reversal 从负到正是 non-trivial 的。\nSubspace angle analysis 提供 mechanistic grounding：correctness direction 在同一 layer 内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差 ~39°（significant rotation）。这解释了为何 CKA（衡量全局 representation similarity）与 transfer（衡量 correctness direction alignment）的关系 需要控制 depth 后才能显现：全局 CKA 下降反映的是 non-correctness dimensions 的 divergence，correctness subspace 本身作为 low-dimensional feature 持续存在。\nCKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异： Qwen3 的 CKA cliff 更陡（L52→L60 从 0.45 降至 0.38），导致更多语言 在 deep layers 穿越 threshold → strong tradeoff；Llama4 的 cliff 更缓 （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越 threshold → weak/mixed tradeoff。\n这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成 完整的 geometric explanation：architecture-dependent CKA cliff steepness → architecture-dependent Pareto frontier strength。\n\n\nSimpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper → representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe stronger → higher absolute AUROC up to a point），创造了一个 confound。 Raw pooled correlation 为负是因为 shallow layers 有 high CKA 但 low AUROC （probe 本身弱），deep layers 有 low CKA 但 higher AUROC（probe 强虽然 transfer degrades）。控制 depth 后，within 每个 layer，higher CKA 的 语言确实有 better transfer，partial rho 为正。\nMVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。 Full-scale（20 langs × 12-24 layers）增强统计 power：per-layer test 从 n=5 增至 n=20，partial correlation 的 bootstrap CI 不含零。\nQwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA cliff 一致：Qwen 的 CKA 变异范围更大（peak 0.82 → floor 0.28 vs Llama 0.84 → 0.35），为 partial correlation 提供更多 signal。\nMVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为： (1) n 从 5 增至 20 语言，power 大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言）， 扩大了 within-layer variance。\nCKA cliff threshold ~0.35 标记了 \"transfer collapse zone\"：当 CKA 低于此阈值时，correctness direction 的 cross-lingual overlap 不足以 支撑 zero-shot transfer。Subspace angle analysis 揭示 correctness direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨 layer 旋转 ~39°（significant drift），解释了为何 within-layer CKA 预测 transfer 但 raw pooled 不预测。\n"
861	  },
862	  {
863	    "name": "CaCLR Implementation and Comparative Evaluation",
864	    "description": "L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits). English labels + parallel activations from GlobalMMLU test-split 70/30 partition. Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier, both models × 20 languages. α sweep [0.01–10], β sweep [0.001–1.0] across 3 OOM.\n",
865	    "results": {
866	      "best_alpha": 0.1,
867	      "best_beta": 0.05,
868	      "caclr_mean_delta_auroc_vs_zs": 0.035,
869	      "caclr_mean_delta_auroc_vs_linproj": 0.015,
870	      "caclr_improvement_at_deep_layers_pp": 4.8,
871	      "caclr_improvement_at_shallow_layers_pp": 1.2,
872	      "caclr_improvement_pass_rate": 0.88,
873	      "qwen3_caclr_mean_auroc_20lang": 0.757,
874	      "qwen3_caclr_delta_vs_zs_pp": 3.7,
875	      "qwen3_caclr_ece_mean": 0.078,
876	      "llama4_caclr_mean_auroc_20lang": 0.733,
877	      "llama4_caclr_delta_vs_zs_pp": 3.3,
878	      "llama4_caclr_ece_mean": 0.085,
879	      "beta_0001_delta_pp": 0.5,
880	      "beta_001_delta_pp": 1.8,
881	      "beta_005_delta_pp": 3.5,
882	      "beta_01_delta_pp": 3.2,
883	      "beta_10_delta_pp": 0.8,
884	      "alpha_001_ece_improvement_pp": 1.5,
885	      "alpha_01_ece_improvement_pp": 3.2,
886	      "alpha_10_ece_improvement_pp": 2.8,
887	      "alpha_100_ece_improvement_pp": -0.5,
888	      "bce_only_auroc": 0.71,
889	      "bce_sbece_auroc": 0.722,
890	      "bce_consistency_auroc": 0.738,
891	      "bce_sbece_consistency_auroc": 0.745,
892	      "mmd_kernel": "Gaussian RBF, bandwidth=median heuristic",
893	      "optimizer": "Adam, lr=1e-3, linear warmup 10%",
894	      "epochs": 50,
895	      "early_stopping": "patience=10, monitor=val_auroc",
896	      "initialization": "from standard LR solution",
897	      "batch_size": 256,
898	      "mmd_items": "same items as BCE (overlapping)",
899	      "parallel_set_size_range": [
900	        1800,
901	        4200
902	      ]
903	    },
904	    "tables": [
905	      {
906	        "name": "Table 10: β Sweep — Consistency Loss Effect",
907	        "columns": [
908	          "beta",
909	          "mean_delta_auroc_vs_zs_pp",
910	          "mean_delta_ece_pp",
911	          "note"
912	        ],
913	        "rows": [
914	          [
915	            0.0,
916	            0.0,
917	            0.0,
918	            "baseline (BCE only)"
919	          ],
920	          [
921	            0.001,
922	            0.5,
923	            -0.3,
924	            "marginal improvement"
925	          ],
926	          [
927	            0.01,
928	            1.8,
929	            -1.1,
930	            "clear positive signal"
931	          ],
932	          [
933	            0.05,
934	            3.5,
935	            -2.4,
936	            "optimal — best tradeoff"
937	          ],
938	          [
939	            0.1,
940	            3.2,
941	            -2.0,
942	            "slight over-regularization"
943	          ],
944	          [
945	            1.0,
946	            0.8,
947	            -0.5,
948	            "MMD dominates, probe accuracy degrades"
949	          ]
950	        ]
951	      },
952	      {
953	        "name": "Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)",
954	        "columns": [
955	          "method",
956	          "auroc_mean_20",
957	          "ece_mean_20",
958	          "requires_labels",
959	          "key_resource"
960	        ],
961	        "rows": [
962	          [
963	            "zero-shot",
964	            0.71,
965	            0.118,
966	            "none",
967	            "—"
968	          ],
969	          [
970	            "mean-shift",
971	            0.71,
972	            0.118,
973	            "none",
974	            "—"
975	          ],
976	          [
977	            "linear_proj_50",
978	            0.725,
979	            0.098,
980	            "50 parallel pairs",
981	            "Procrustes"
982	          ],
983	          [
984	            "linear_proj_200",
985	            0.729,
986	            0.095,
987	            "200 parallel pairs",
988	            "Procrustes"
989	          ],
990	          [
991	            "few-shot-25",
992	            0.7,
993	            0.102,
994	            "25 labeled",
995	            "target labels"
996	          ],
997	          [
998	            "few-shot-100",
999	            0.727,
1000	            0.088,
1001	            "100 labeled",
1002	            "target labels"
1003	          ],
1004	          [
1005	            "CaCLR",
1006	            0.745,
1007	            0.082,
1008	            "none",
1009	            "parallel activations"
1010	          ]
1011	        ]
1012	      },
1013	      {
1014	        "name": "Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)",
1015	        "columns": [
1016	          "depth_pct",
1017	          "zs_auroc",
1018	          "caclr_auroc",
1019	          "delta_pp"
1020	        ],
1021	        "rows": [
1022	          [
1023	            30,
1024	            0.733,
1025	            0.745,
1026	            1.2
1027	          ],
1028	          [
1029	            43,
1030	            0.748,
1031	            0.766,
1032	            1.8
1033	          ],
1034	          [
1035	            55,
1036	            0.72,
1037	            0.752,
1038	            3.2
1039	          ],
1040	          [
1041	            64,
1042	            0.69,
1043	            0.738,
1044	            4.8
1045	          ],
1046	          [
1047	            77,
1048	            0.638,
1049	            0.688,
1050	            5.0
1051	          ],
1052	          [
1053	            85,
1054	            0.601,
1055	            0.641,
1056	            4.0
1057	          ]
1058	        ]
1059	      }
1060	    ],
1061	    "figures": [],
1062	    "analysis": "CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC improvement（实际 deep-layer mean = +4.8pp），且 β sweep across 3 OOM 清晰展现最优区间。Component ablation 证实 L_consistency 是主要 contributor（+2.8pp），L_SB-ECE 提供 complementary calibration improvement（+0.7pp ECE, +0.7pp AUROC synergy）。\nCaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用 training dynamics（gradient 信号引导 probe 朝 language-invariant direction 收敛），而 Procrustes 只做 post-hoc geometric correction。但差距不大 是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit distributions，不能做 full subspace alignment。\nDeep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers 的 capability-specific component 更大，CaCLR 的 consistency loss 正好 在这些 layers 有更多 signal 来 exploit。这构成 Pareto→Decomposition→CaCLR→CKA 因果链的第三环。\n\n\nCaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习 language-invariant features：EN 和 target-language 的 probe 输出分布 应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的 logit mean 和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的 \"universal correctness subspace\"。\n+3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能 捕获 first-order distributional alignment（mean/variance matching）， 但无法完成 full rotational alignment（需要 d-dimensional 操作）。Linear projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化 probe 本身；CaCLR 的优势在于 end-to-end 优化但受 1-D 约束。两者差距 仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性 投影解决的）而非 distributional（MMD 解决的）。\nβ sweep across 3 OOM 清晰展现 \"sweet spot\"：β=0.001 太弱（gradient noise > signal），β=1.0 太强（MMD 主导 BCE，probe accuracy 下降 2pp）。 Optimal β=0.05 平衡了 accuracy 和 consistency。\nDeep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为 deep layers 有更大的 capability-specific component（Claim 2 decomposition 所揭示），CaCLR 的 consistency loss 正好 target 这个 component。这与 difficulty-capability decomposition 形成因果闭环。\n88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving pairs 是 HIGH-resource languages（如 Qwen3-zh, Qwen3-nl）on shallow layers where ZS transfer 已经接近 ceiling。\n"
1063	  },
1064	  {
1065	    "name": "Difficulty-Controlled Ablation (Decomposition)",
1066	    "description": "IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。包含 random-direction control。\n",
1067	    "results": {
1068	      "difficulty_probe_r2_mean": 0.68,
1069	      "difficulty_probe_r2_range": [
1070	        0.55,
1071	        0.78
1072	      ],
1073	      "difficulty_var_explained_pct": 65,
1074	      "capability_var_explained_pct": 35,
1075	      "difficulty_transfer_degradation_share_pct": 12,
1076	      "capability_transfer_degradation_share_pct": 88,
1077	      "decomp_capability_delta_auroc": 0.03,
1078	      "residual_en_auroc_drop_pp": 4.5,
1079	      "residual_zs_transfer_drop_pp": 0.8,
1080	      "random_direction_control_delta_pp": -1.2,
1081	      "prescriptive_accuracy": 0.78,
1082	      "capability_transfer_drop_by_depth": {
1083	        "20pct": 0.6,
1084	        "50pct": 2.8,
1085	        "80pct": 8.5
1086	      }
1087	    },
1088	    "tables": [
1089	      {
1090	        "name": "Table 13: Decomposition Results",
1091	        "columns": [
1092	          "component",
1093	          "var_pct",
1094	          "transfer_auroc_mean",
1095	          "transfer_drop_pp",
1096	          "degradation_share_pct"
1097	        ],
1098	        "rows": [
1099	          [
1100	            "full_correctness",
1101	            100,
1102	            0.71,
1103	            9.0,
1104	            100
1105	          ],
1106	          [
1107	            "difficulty_shared",
1108	            65,
1109	            0.698,
1110	            1.1,
1111	            12
1112	          ],
1113	          [
1114	            "capability_specific",
1115	            35,
1116	            0.615,
1117	            12.8,
1118	            88
1119	          ]
1120	        ]
1121	      },
1122	      {
1123	        "name": "Table 14: Capability Transfer Drop by Depth",
1124	        "columns": [
1125	          "depth_band",
1126	          "difficulty_drop_pp",
1127	          "capability_drop_pp",
1128	          "ratio"
1129	        ],
1130	        "rows": [
1131	          [
1132	            "20-30%",
1133	            0.2,
1134	            0.6,
1135	            "3×"
1136	          ],
1137	          [
1138	            "40-50%",
1139	            0.6,
1140	            2.8,
1141	            "4.7×"
1142	          ],
1143	          [
1144	            "60-70%",
1145	            1.0,
1146	            5.6,
1147	            "5.6×"
1148	          ],
1149	          [
1150	            "75-90%",
1151	            1.5,
1152	            8.5,
1153	            "5.7×"
1154	          ]
1155	        ]
1156	      }
1157	    ],
1158	    "figures": [],
1159	    "analysis": "Decomposition 清晰分离 transferable vs non-transferable components。 Difficulty 占大部分 variance 但 near-perfectly transfers（仅 12% degradation share），capability 占少数但驱动几乎所有 degradation。 这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty dominates there）但在 deep layers 失败（capability grows）。 Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的， 而是可以指导 alignment strategy selection。\n\n\nIRT difficulty 是 language-agnostic property：hard questions are hard everywhere。Ridge regression captures this linearly (R²=0.68, 与 Civelli et al. 的 shared difficulty finding 一致)。Difficulty 占 correctness variance 的 65% 但仅贡献 12% 的 transfer degradation， 因为 difficulty signal 本质上是 universal 的。Capability-specific residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且 degradation 随 depth 指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。\n这一 decomposition 解释了 Pareto frontier 的 mechanistic origin： deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent competence），而这个 component 恰好是 最难 transfer 的。CaCLR 的 consistency loss works precisely because it targets this component。\nRandom-direction control（-1.2pp, 随机方向 projection 反而损害）确认 difficulty direction 不是 arbitrary dimensionality reduction 的 artifact， 而是 genuine signal。\nPrescriptive accuracy 78%：给定语言-layer 的 difficulty/capability ratio，预测应使用 zero-shot（difficulty-dominant）还是 CaCLR （capability-dominant）策略，在 78% 的 cases 中正确。\n"
1160	  },
1161	  {
1162	    "name": "Linear Projection Sensitivity Analysis",
1163	    "description": "Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。 Both models × 5 representative layers × 20 languages。确定最小数据需求 和 resource-tier 分层饱和。\n",
1164	    "results": {
1165	      "pairs_to_95pct_overall": 42,
1166	      "pairs_to_95pct_HIGH": 22,
1167	      "pairs_to_95pct_MID": 38,
1168	      "pairs_to_95pct_LOW": 48,
1169	      "pairs_10_pct_of_200": 0.72,
1170	      "pairs_20_pct_of_200": 0.86,
1171	      "pairs_30_pct_of_200": 0.92,
1172	      "pairs_50_pct_of_200": 0.97,
1173	      "pairs_100_pct_of_200": 0.99,
1174	      "pairs_200_baseline_auroc_mean": 0.729,
1175	      "procrustes_reversal_threshold": 0.52,
1176	      "procrustes_helps_below_threshold_delta_pp": 3.8,
1177	      "procrustes_hurts_above_threshold_delta_pp": -1.2
1178	    },
1179	    "tables": [
1180	      {
1181	        "name": "Table 15: Projection Sample Efficiency",
1182	        "columns": [
1183	          "n_pairs",
1184	          "pct_of_200pair_performance",
1185	          "mean_auroc",
1186	          "note"
1187	        ],
1188	        "rows": [
1189	          [
1190	            10,
1191	            72,
1192	            0.724,
1193	            "unstable, high variance across runs"
1194	          ],
1195	          [
1196	            20,
1197	            86,
1198	            0.728,
1199	            "captures dominant rotation"
1200	          ],
1201	          [
1202	            30,
1203	            92,
1204	            0.731,
1205	            "near plateau for HIGH langs"
1206	          ],
1207	          [
1208	            50,
1209	            97,
1210	            0.734,
1211	            "near plateau for all tiers"
1212	          ],
1213	          [
1214	            100,
1215	            99,
1216	            0.737,
1217	            "marginal returns"
1218	          ],
1219	          [
1220	            200,
1221	            100,
1222	            0.729,
1223	            "baseline (reference)"
1224	          ]
1225	        ]
1226	      },
1227	      {
1228	        "name": "Table 16: Saturation by Resource Tier",
1229	        "columns": [
1230	          "tier",
1231	          "pairs_to_90pct",
1232	          "pairs_to_95pct",
1233	          "interpretation"
1234	        ],
1235	        "rows": [
1236	          [
1237	            "HIGH",
1238	            15,
1239	            22,
1240	            "rotation is simple, low effective rank"
1241	          ],
1242	          [
1243	            "MID",
1244	            25,
1245	            38,
1246	            "moderate rotation complexity"
1247	          ],
1248	          [
1249	            "LOW",
1250	            35,
1251	            48,
1252	            "complex rotation, more data needed"
1253	          ]
1254	        ]
1255	      },
1256	      {
1257	        "name": "Table 17: Procrustes Effect Reversal",
1258	        "columns": [
1259	          "zs_auroc_range",
1260	          "n_lang_layer_pairs",
1261	          "mean_delta_pp",
1262	          "direction"
1263	        ],
1264	        "rows": [
1265	          [
1266	            "<0.45",
1267	            42,
1268	            5.2,
1269	            "strong positive"
1270	          ],
1271	          [
1272	            "0.45-0.52",
1273	            68,
1274	            2.4,
1275	            "moderate positive"
1276	          ],
1277	          [
1278	            "0.52-0.60",
1279	            95,
1280	            0.3,
1281	            "near-zero (transition zone)"
1282	          ],
1283	          [
1284	            "0.60-0.70",
1285	            88,
1286	            -1.2,
1287	            "negative — hurts"
1288	          ],
1289	          [
1290	            ">0.70",
1291	            47,
1292	            -0.8,
1293	            "slight negative"
1294	          ]
1295	        ]
1296	      }
1297	    ],
1298	    "figures": [],
1299	    "analysis": "~42 pairs to 95% performance 是 directly actionable 的 practical finding：对于大多数语言，仅需 <50 parallel sentences 即可达到接近 supervised-level alignment。Resource-tier stratification（HIGH 22 vs LOW 48 pairs）提供了 per-language guidance。\nProcrustes reversal at 0.52 与 CKA threshold 0.35 形成对应： CKA < 0.35 的 language-layer combinations 对应 ZS < 0.52（ 因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的 区域。这构成了 geometric explanation 的 practical corollary。\n\n\nLinear projection (Procrustes) 学习 EN→target 的 rotation matrix。 20 pairs 即可估计 dominant rotational components（correctness subspace 是 low-dimensional 的，前几个 principal angles 解释 90%+ 的 alignment structure）。42 pairs 达到 95% 因为边际的 minor components 需要更多 data 来稳定估计。\nResource-tier stratification 清晰：HIGH languages（zh/es/de 等）的 activation distributions 与 EN 更相似，rotation matrix 的 effective rank 更低（fewer parameters to estimate），22 pairs 即可。LOW languages 需要估计更 complex rotation（effective rank 更高），48 pairs。\nProcrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时， correctness direction 严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。 当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes 引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35 （与 plan_011 的 cliff threshold 一致）。\n这一 finding 直接 actionable：practitioners 应先测 ZS transfer， only apply Procrustes when baseline < 0.52。\n"
1300	  },
1301	  {
1302	    "name": "Probing Control Tasks — Full-Scale Hewitt & Liang (2019)",
1303	    "description": "Extend MVP English-only control task analysis to 20 languages × 2 architectures。Train probes on randomly permuted labels, compute selectivity = real_AUROC - control_AUROC。Identify capacity artifacts by language, layer, and model。\n",
1304	    "results": {
1305	      "en_selectivity_range": [
1306	        0.02,
1307	        0.26
1308	      ],
1309	      "en_selectivity_meaningful_layers": [
1310	        16,
1311	        20,
1312	        24,
1313	        27
1314	      ],
1315	      "control_artifact_rate_lowres": 0.27,
1316	      "control_artifact_rate_midres": 0.05,
1317	      "control_artifact_rate_highres": 0.03,
1318	      "low_res_langs_most_affected": [
1319	        "yo",
1320	        "ig",
1321	        "te",
1322	        "sw"
1323	      ],
1324	      "artifact_concentration_depth": "60-100% depth",
1325	      "cross_lingual_selectivity_mean": {
1326	        "HIGH": 0.22,
1327	        "MID": 0.18,
1328	        "LOW": 0.09
1329	      },
1330	      "languages_with_any_meaningful_selectivity": 17,
1331	      "control_auroc_mean_all": 0.495,
1332	      "control_auroc_std": 0.008
1333	    },
1334	    "tables": [
1335	      {
1336	        "name": "Table 18: Selectivity by Resource Tier and Depth",
1337	        "columns": [
1338	          "depth_band",
1339	          "HIGH_selectivity",
1340	          "MID_selectivity",
1341	          "LOW_selectivity"
1342	        ],
1343	        "rows": [
1344	          [
1345	            "0-30%",
1346	            0.04,
1347	            0.03,
1348	            0.01
1349	          ],
1350	          [
1351	            "30-60%",
1352	            0.18,
1353	            0.14,
1354	            0.06
1355	          ],
1356	          [
1357	            "60-80%",
1358	            0.28,
1359	            0.22,
1360	            0.1
1361	          ],
1362	          [
1363	            "80-100%",
1364	            0.25,
1365	            0.2,
1366	            0.08
1367	          ]
1368	        ]
1369	      },
1370	      {
1371	        "name": "Table 19: Artifact Rates by Tier",
1372	        "columns": [
1373	          "tier",
1374	          "n_lang_layer_combinations",
1375	          "artifact_count",
1376	          "artifact_rate"
1377	        ],
1378	        "rows": [
1379	          [
1380	            "HIGH",
1381	            384,
1382	            12,
1383	            "3%"
1384	          ],
1385	          [
1386	            "MID",
1387	            336,
1388	            17,
1389	            "5%"
1390	          ],
1391	          [
1392	            "LOW",
1393	            240,
1394	            65,
1395	            "27%"
1396	          ],
1397	          [
1398	            "total",
1399	            960,
1400	            94,
1401	            "10%"
1402	          ]
1403	        ]
1404	      }
1405	    ],
1406	    "figures": [],
1407	    "analysis": "27% low-resource artifact rate 是 methodological warning for the field： cross-lingual probing studies 如果不做 selectivity checks 会高估 low-resource transfer quality。重要的是 artifacts 集中在 low-resource + deep layers，不波及 mid/high-resource 或 shallow layers，因此本文的 核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。\n\n\nMVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual extension 揭示了 resource-tier dependent artifact pattern：\nLOW-resource languages 的 27% artifact rate 源于两个因素：(1) these languages 在 model pretraining 中占比极低，activation distributions 相对 high-resource 更 \"shallow\" (less structured)，linear probes 更容易 通过 capacity 而非 genuine signal 拟合少量 patterns；(2) GlobalMMLU 的 low-resource translations 质量较低，引入 noise 使 correctness signal 更弱，selectivity 更接近 chance。\nMid/high-resource 的 artifact rate 极低（3-5%）因为 representation quality 高，probe 有 genuine signal 可以 leverage。\nArtifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的 low-resource CKA 已经很低（<0.2），cross-lingual activation structure 不足以支撑 genuine correctness probing，probe 退化为 memorizing dataset-specific patterns。\n这一 finding 是 field-level contribution：此前没有人在 cross-lingual probing 中检查 selectivity controls。28% 的 low-resource artifact rate 意味着没有 control tasks 的 cross-lingual probing 结果 （包括 Xiao et al.）需要谨慎解读。\n"
1408	  },
1409	  {
1410	    "name": "Cross-Lingual Correctness-Confidence Orthogonality",
1411	    "description": "Extract verbalized confidence direction, compute cosine similarity with correctness direction, 20 languages × 2 architectures。 Supporting evidence for Claim 4 (subsection)。\n",
1412	    "results": {
1413	      "cosine_mean_overall": 0.05,
1414	      "cosine_range": [
1415	        0.02,
1416	        0.09
1417	      ],
1418	      "cosine_en": 0.03,
1419	      "all_below_0p10": true,
1420	      "qwen3_cosine_mean": 0.046,
1421	      "llama4_cosine_mean": 0.054,
1422	      "HIGH_cosine_mean": 0.038,
1423	      "MID_cosine_mean": 0.052,
1424	      "LOW_cosine_mean": 0.072,
1425	      "resource_tier_correlation": -0.66
1426	    },
1427	    "tables": [
1428	      {
1429	        "name": "Table 20: Orthogonality by Tier (cosine similarity)",
1430	        "columns": [
1431	          "tier",
1432	          "n_langs",
1433	          "qwen3_mean",
1434	          "llama4_mean",
1435	          "combined_mean"
1436	        ],
1437	        "rows": [
1438	          [
1439	            "HIGH",
1440	            8,
1441	            0.035,
1442	            0.041,
1443	            0.038
1444	          ],
1445	          [
1446	            "MID",
1447	            7,
1448	            0.048,
1449	            0.056,
1450	            0.052
1451	          ],
1452	          [
1453	            "LOW",
1454	            5,
1455	            0.066,
1456	            0.078,
1457	            0.072
1458	          ]
1459	        ]
1460	      }
1461	    ],
1462	    "figures": [],
1463	    "analysis": "Orthogonality universally holds (39/40 pairs below 0.10, all 40 below 0.095)，confirming output-based calibration methods are structurally limited across languages。Resource-tier gradient 是新 finding，但 effect size 小（range only 0.034），作为 subsection 足够。\n\n\nMiao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension to 20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映 transformer 的 structural property：verbalized confidence 由 language modeling head 从 surface-level token probabilities 生成，correctness 由 intermediate representations geometry 编码，两者 architecturally decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation in low-resource languages 更 noisy，不完全 decoupled。Resource-tier gradient（r=-0.66）说明更好的 multilingual training → 更清晰的 correctness/confidence separation。\n"
1464	  },
1465	  {
1466	    "name": "Probe Complexity Comparison",
1467	    "description": "Logistic regression vs 2-layer MLP at each probed layer, both models。 Validates linear probe choice for transfer。\n",
1468	    "results": {
1469	      "logreg_en_auroc_best": 0.81,
1470	      "mlp_en_auroc_best": 0.83,
1471	      "mlp_en_gain_pp": 2.0,
1472	      "logreg_zs_drop_mean_pp": 9.0,
1473	      "mlp_zs_drop_mean_pp": 14.5,
1474	      "logreg_transfer_advantage_pp": 5.5,
1475	      "logreg_advantage_shallow_pp": 2.0,
1476	      "logreg_advantage_deep_pp": 8.2
1477	    },
1478	    "tables": [
1479	      {
1480	        "name": "Table S2: Probe Complexity (Qwen3, at EN-optimal layer)",
1481	        "columns": [
1482	          "probe_type",
1483	          "en_auroc",
1484	          "zs_mean_20",
1485	          "zs_drop_pp"
1486	        ],
1487	        "rows": [
1488	          [
1489	            "logistic_regression",
1490	            0.81,
1491	            0.72,
1492	            9.0
1493	          ],
1494	          [
1495	            "mlp_2layer_h128",
1496	            0.83,
1497	            0.685,
1498	            14.5
1499	          ]
1500	        ]
1501	      }
1502	    ],
1503	    "figures": [],
1504	    "analysis": "Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp EN performance 换取 5.5pp transfer improvement。Depth interaction confirms nonlinear language-specific features drive deep-layer degradation。\n\n\nLinear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace 是 near-universal linear structure（subspace angle ~12° from plan_011）。 MLPs fit nonlinear decision boundaries that overfit EN-specific feature interactions，gaining +2pp EN AUROC but losing 5.5pp transfer。Gap 在 deep layers 放大（+8.2pp advantage for logreg at 80% depth）因为 deep layers 有更多 language-specific nonlinear structure for MLP to exploit。 This justifies logreg as primary probe and supports geometric interpretation of Pareto frontier。\n"
1505	  },
1506	  {
1507	    "name": "Cross-Benchmark Generalization (Belebele + MMLU-ProX)",
1508	    "description": "Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages each)。Tests domain generalization。\n",
1509	    "results": {
1510	      "belebele_zs_mean_20": 0.695,
1511	      "belebele_caclr_mean_20": 0.728,
1512	      "belebele_caclr_delta_pp": 3.3,
1513	      "mmlupx_zs_mean_20": 0.68,
1514	      "mmlupx_caclr_mean_20": 0.715,
1515	      "mmlupx_caclr_delta_pp": 3.5,
1516	      "cross_benchmark_caclr_cv": 0.04
1517	    },
1518	    "tables": [
1519	      {
1520	        "name": "Table 21: Cross-Benchmark CaCLR Generalization",
1521	        "columns": [
1522	          "benchmark",
1523	          "zs_mean_20",
1524	          "caclr_mean_20",
1525	          "delta_pp"
1526	        ],
1527	        "rows": [
1528	          [
1529	            "GlobalMMLU",
1530	            0.71,
1531	            0.745,
1532	            3.5
1533	          ],
1534	          [
1535	            "Belebele",
1536	            0.695,
1537	            0.728,
1538	            3.3
1539	          ],
1540	          [
1541	            "MMLU-ProX",
1542	            0.68,
1543	            0.715,
1544	            3.5
1545	          ]
1546	        ]
1547	      }
1548	    ],
1549	    "figures": [],
1550	    "analysis": "CaCLR generalizes across benchmarks with low variance。Cross-benchmark consistency is the strongest defense against overfitting concerns。\n\n\nBelebele (reading comprehension) 和 MMLU-ProX (harder factual) 的 baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement 幅度 consistent（3.3-3.5pp vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实 CaCLR addresses 一个 fundamental representation alignment issue 而非 overfitting to specific benchmark。\n"
1551	  },
1552	  {
1553	    "name": "Quantization Validation Ablation",
1554	    "description": "(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset。\n",
1555	    "results": {
1556	      "llama4_w4a16_fp16_auroc_diff_mean_pp": 0.3,
1557	      "llama4_w4a16_fp16_auroc_diff_max_pp": 0.8,
1558	      "llama4_rank_correlation": 0.996,
1559	      "qwen3_int4_fp16_auroc_diff_mean_pp": 0.5,
1560	      "qwen3_int4_fp16_auroc_diff_max_pp": 1.1,
1561	      "qwen3_rank_correlation": 0.994,
1562	      "conclusion": "quantization introduces negligible distortion for probing"
1563	    },
1564	    "tables": [
1565	      {
1566	        "name": "Table S3: Quantization Comparison (5 representative layers)",
1567	        "columns": [
1568	          "model",
1569	          "layer",
1570	          "fp16_auroc",
1571	          "quant_auroc",
1572	          "diff_pp"
1573	        ],
1574	        "rows": [
1575	          [
1576	            "Llama4",
1577	            8,
1578	            0.637,
1579	            0.634,
1580	            0.3
1581	          ],
1582	          [
1583	            "Llama4",
1584	            16,
1585	            0.737,
1586	            0.735,
1587	            0.2
1588	          ],
1589	          [
1590	            "Llama4",
1591	            28,
1592	            0.784,
1593	            0.781,
1594	            0.3
1595	          ],
1596	          [
1597	            "Llama4",
1598	            36,
1599	            0.792,
1600	            0.789,
1601	            0.3
1602	          ],
1603	          [
1604	            "Llama4",
1605	            44,
1606	            0.774,
1607	            0.77,
1608	            0.4
1609	          ],
1610	          [
1611	            "Qwen3",
1612	            20,
1613	            0.712,
1614	            0.708,
1615	            0.4
1616	          ],
1617	          [
1618	            "Qwen3",
1619	            36,
1620	            0.78,
1621	            0.775,
1622	            0.5
1623	          ],
1624	          [
1625	            "Qwen3",
1626	            52,
1627	            0.808,
1628	            0.803,
1629	            0.5
1630	          ],
1631	          [
1632	            "Qwen3",
1633	            68,
1634	            0.812,
1635	            0.806,
1636	            0.6
1637	          ],
1638	          [
1639	            "Qwen3",
1640	            80,
1641	            0.807,
1642	            0.8,
1643	            0.7
1644	          ]
1645	        ]
1646	      }
1647	    ],
1648	    "figures": [],
1649	    "analysis": "Quantization safe for both models。Preempts reviewer concern #5。\n\n\nW4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction 的 angular structure 仍 robust（0.5pp mean diff）， 因为 quantization noise 近似 isotropic，不 preferentially distort correctness-relevant directions。Rank correlation > 0.994 确认 Pareto frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3) 因为 Int4 比 W4A16 更 lossy。\n"
1650	  },
1651	  {
1652	    "name": "Gemma 4 31B Dense — Third Architecture (Camera-Ready)",
1653	    "description": "Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16), 20 languages。Provides dense vs MoE contrast for camera-ready。\n",
1654	    "results": {
1655	      "en_best_auroc": 0.8,
1656	      "en_best_layer_idx": 45,
1657	      "zs_mean_20lang": 0.71,
1658	      "zs_best_transfer_layer_idx": 36,
1659	      "global_spearman_rho": -0.85,
1660	      "per_lang_rho_median": -0.58,
1661	      "caclr_delta_vs_zs_pp": 3.0,
1662	      "simpson_partial_rho": 0.44,
1663	      "simpson_partial_p": 0.004
1664	    },
1665	    "tables": [
1666	      {
1667	        "name": "Table 22: Three-Architecture Summary",
1668	        "columns": [
1669	          "model",
1670	          "type",
1671	          "layers",
1672	          "en_best",
1673	          "zs_mean_20",
1674	          "pareto_rho",
1675	          "simpson_partial_rho",
1676	          "caclr_delta_pp"
1677	        ],
1678	        "rows": [
1679	          [
1680	            "Qwen3-235B",
1681	            "MoE",
1682	            94,
1683	            0.81,
1684	            0.72,
1685	            -0.91,
1686	            0.48,
1687	            3.7
1688	          ],
1689	          [
1690	            "Llama4 Scout",
1691	            "MoE",
1692	            48,
1693	            0.79,
1694	            0.7,
1695	            -0.78,
1696	            0.41,
1697	            3.3
1698	          ],
1699	          [
1700	            "Gemma4 31B",
1701	            "Dense",
1702	            60,
1703	            0.8,
1704	            0.71,
1705	            -0.85,
1706	            0.44,
1707	            3.0
1708	          ]
1709	        ]
1710	      }
1711	    ],
1712	    "figures": [],
1713	    "analysis": "Three-architecture replication 是 universality claim 最强证据： Simpson's Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在 55-60% depth 处一致出现 knee，CaCLR 提供 3-3.7pp consistent gain。 Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth 的 property 而非 routing architecture 的。\n\n\nGemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two MoE models），different pretraining recipe（Google vs Alibaba/Meta）， 60 layers（between Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models 因为 31B dense < 22B MoE active (MoE routing 提供 effective capacity boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91) 和 Llama (-0.78) 之间。Simpson's partial correlation 仍然显著 (rho=+0.44, p=0.004)， 确认 geometric insight 是 architecture-universal 而非 MoE-specific。\n"
1714	  },
1715	  {
1716	    "name": "Extended Language Coverage (Camera-Ready)",
1717	    "description": "Expand from 20 to 50+ languages for camera-ready。\n",
1718	    "results": {
1719	      "total_languages": 50,
1720	      "zs_pass_rate_50lang": 0.84,
1721	      "zs_auroc_above_060_count": 42,
1722	      "caclr_improvement_positive_count": 47,
1723	      "mean_zs_auroc_50lang": 0.69,
1724	      "mean_caclr_auroc_50lang": 0.72,
1725	      "pareto_frontier_holds_all_langs": true,
1726	      "new_families": [
1727	        "Austronesian",
1728	        "Dravidian",
1729	        "Uralic",
1730	        "Kartvelian",
1731	        "Niger-Congo_B"
1732	      ]
1733	    },
1734	    "tables": [
1735	      {
1736	        "name": "Table 23: Extended Coverage by Tier",
1737	        "columns": [
1738	          "tier",
1739	          "n_langs",
1740	          "zs_mean",
1741	          "caclr_mean",
1742	          "caclr_gain_pp"
1743	        ],
1744	        "rows": [
1745	          [
1746	            "HIGH",
1747	            10,
1748	            0.75,
1749	            0.78,
1750	            2.8
1751	          ],
1752	          [
1753	            "MID",
1754	            24,
1755	            0.71,
1756	            0.74,
1757	            3.5
1758	          ],
1759	          [
1760	            "LOW",
1761	            12,
1762	            0.62,
1763	            0.66,
1764	            4.2
1765	          ],
1766	          [
1767	            "VERY_LOW",
1768	            4,
1769	            0.53,
1770	            0.58,
1771	            5.0
1772	          ]
1773	        ]
1774	      }
1775	    ],
1776	    "figures": [],
1777	    "analysis": "50-language extension 确认 all findings at scale。Resource-tier gradient smooth, CaCLR benefit inversely correlated with resource level, no language family shows anomalous behavior。\n\nExpansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian, Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely low-resource 语言（Amharic, Khmer, Lao）可能 < 0.55 但代表 edge cases。 CaCLR 在 94% 的新增语言上 positive 因为 consistency loss mechanism 是 language-agnostic。Pareto frontier structure 在 50 languages 上 完全保持。\n"
1778	  }
1779	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c6707ed-977f-49c6-8bb4-3130472df7e0",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "f2dc5be3-178b-492f-a988-20c286bc96fa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B\",\n    \"description\": \"94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th), 20 typologically diverse languages, English logistic regression probes, 5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100, CaCLR。重点验证 MVP 发现的 strong depth-transferability tradeoff 是否在大模型上保持。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.81,\n      \"en_best_layer_idx\": 72,\n      \"en_auroc_range\": [\n        0.58,\n        0.81\n      ],\n      \"en_ece_raw_best\": 0.168,\n      \"zs_mean_auroc_20lang_best_transfer_layer\": 0.72,\n      \"zs_best_transfer_layer_idx\": 52,\n      \"zs_pass_rate_20lang\": 0.9,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"te\"\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.76,\n        \"MID_mean\": 0.72,\n        \"LOW_mean\": 0.63\n      },\n      \"zs_auroc_selected\": {\n        \"zh\": 0.77,\n        \"es\": 0.76,\n        \"fr\": 0.76,\n        \"de\": 0.77,\n        \"ja\": 0.75,\n        \"nl\": 0.76,\n        \"pt\": 0.75,\n        \"it\": 0.75,\n        \"ar\": 0.73,\n        \"hi\": 0.71,\n        \"ko\": 0.72,\n        \"tr\": 0.71,\n        \"ru\": 0.74,\n        \"vi\": 0.7,\n        \"th\": 0.69,\n        \"sw\": 0.63,\n        \"bn\": 0.65,\n        \"yo\": 0.57,\n        \"ig\": 0.61,\n        \"te\": 0.58\n      },\n      \"per_lang_spearman_rho_median\": -0.64,\n      \"per_lang_significant_at_005\": 15,\n      \"global_spearman_rho\": -0.91,\n      \"global_spearman_p\": 0.0001,\n      \"pareto_frontier_layers\": [\n        40,\n        44,\n        48,\n        52,\n        56\n      ],\n      \"pareto_en_zs_gap_at_knee_pp\": 4.2,\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linproj_200pairs_mean_auroc\": 0.74,\n      \"fewshot_25_mean_auroc\": 0.708,\n      \"fewshot_100_mean_auroc\": 0.735\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier (selected layers)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.58,\n            0.572,\n            0.8,\n            false\n          ],\n          [\n            12,\n            13,\n            0.645,\n            0.632,\n            1.3,\n            false\n          ],\n          [\n            20,\n            21,\n            0.71,\n            0.695,\n            1.5,\n            false\n          ],\n          [\n            28,\n            30,\n            0.752,\n            0.733,\n            1.9,\n            false\n          ],\n          [\n            36,\n            38,\n            0.778,\n            0.752,\n            2.6,\n            false\n          ],\n          [\n            40,\n            43,\n            0.788,\n            0.748,\n            4.0,\n            true\n          ],\n          [\n            44,\n            47,\n            0.796,\n            0.74,\n            5.6,\n            true\n          ],\n          [\n            48,\n            51,\n            0.802,\n            0.732,\n            7.0,\n            true\n          ],\n          [\n            52,\n            55,\n            0.806,\n            0.72,\n            8.6,\n            true\n          ],\n          [\n            56,\n            60,\n            0.808,\n            0.706,\n            10.2,\n            true\n          ],\n          [\n            60,\n            64,\n            0.81,\n            0.69,\n            12.0,\n            false\n          ],\n          [\n            68,\n            72,\n            0.81,\n            0.661,\n            14.9,\n            false\n          ],\n          [\n            72,\n            77,\n            0.81,\n            0.638,\n            17.2,\n            false\n          ],\n          [\n            80,\n            85,\n            0.805,\n            0.601,\n            20.4,\n            false\n          ],\n          [\n            88,\n            94,\n            0.792,\n            0.558,\n            23.4,\n            false\n          ],\n          [\n            92,\n            98,\n            0.778,\n            0.531,\n            24.7,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3\",\n        \"columns\": [\n          \"language\",\n          \"tier\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"significant\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            -0.72,\n            0.001,\n            true\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            -0.68,\n            0.002,\n            true\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            -0.7,\n            0.001,\n            true\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            -0.69,\n            0.002,\n            true\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            -0.74,\n            0.001,\n            true\n          ],\n          [\n            \"nl\",\n            \"HIGH\",\n            -0.67,\n            0.003,\n            true\n          ],\n          [\n            \"pt\",\n            \"MID\",\n            -0.65,\n            0.004,\n            true\n          ],\n          [\n            \"it\",\n            \"MID\",\n            -0.66,\n            0.003,\n            true\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            -0.71,\n            0.001,\n            true\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            -0.63,\n            0.005,\n            true\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            -0.67,\n            0.003,\n            true\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            -0.62,\n            0.006,\n            true\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            -0.69,\n            0.002,\n            true\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            -0.61,\n            0.008,\n            true\n          ],\n          [\n            \"th\",\n            \"MID\",\n            -0.58,\n            0.012,\n            true\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            -0.52,\n            0.025,\n            true\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            -0.55,\n            0.018,\n            false\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            -0.48,\n            0.042,\n            false\n          ],\n          [\n            \"ig\",\n            \"LOW\",\n            -0.51,\n            0.028,\n            false\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            -0.45,\n            0.058,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 展现 strong, consistent depth-transferability tradeoff： global Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。 Pareto frontier 包含 5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal (L72) 与 ZS-optimal (L52) 相隔 20 层 / 22pp depth，远大于 MVP 的 3 层 间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多 空间进行 language-specific specialization。High-resource 语言在 Pareto knee 以下也保持 AUROC > 0.74，但 low-resource 在 70% depth 后急剧下降。 这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer 对 low-resource 影响更大（CKA 基线更低，cliff 更早触及）。\\n\\n\\nQwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear probing scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability tradeoff 比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal layer (L52, 55% depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于 Qwen 架构特征：MoE routing 在深层产生 language-specific expert 激活模式， 导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。 15/20 languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是 跨语言一致的。2 个 fail 语言（yo, te）的 AUROC < 0.60 因为 Qwen3 pretraining corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding 层的 representation quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为 StandardScaler + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。 Linear projection (200 pairs) 提供 +2pp 因为 Procrustes alignment 捕获了 correctness subspace 的旋转，但不触及 distributional matching。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout\",\n    \"description\": \"48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed tradeoff pattern 是否是 Llama 架构家族特征。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.79,\n      \"en_best_layer_idx\": 36,\n      \"en_auroc_range\": [\n        0.56,\n        0.79\n      ],\n      \"en_ece_raw_best\": 0.182,\n      \"zs_mean_auroc_20lang_best_transfer_layer\": 0.7,\n      \"zs_best_transfer_layer_idx\": 28,\n      \"zs_pass_rate_20lang\": 0.85,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"te\",\n        \"ig\"\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.74,\n        \"MID_mean\": 0.7,\n        \"LOW_mean\": 0.61\n      },\n      \"per_lang_spearman_rho_median\": -0.28,\n      \"per_lang_significant_at_005\": 6,\n      \"per_lang_positive_rho_langs\": [\n        \"ar\",\n        \"hi\",\n        \"ko\"\n      ],\n      \"global_spearman_rho\": -0.78,\n      \"global_spearman_p\": 0.003,\n      \"pareto_frontier_layers\": [\n        20,\n        24,\n        28\n      ],\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linproj_200pairs_mean_auroc\": 0.718,\n      \"fewshot_25_mean_auroc\": 0.692,\n      \"fewshot_100_mean_auroc\": 0.718\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier\",\n        \"columns\": [\n          \"layer_idx\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.56,\n            0.552,\n            0.8,\n            false\n          ],\n          [\n            8,\n            17,\n            0.635,\n            0.625,\n            1.0,\n            false\n          ],\n          [\n            12,\n            25,\n            0.695,\n            0.682,\n            1.3,\n            false\n          ],\n          [\n            16,\n            33,\n            0.735,\n            0.718,\n            1.7,\n            false\n          ],\n          [\n            20,\n            42,\n            0.758,\n            0.724,\n            3.4,\n            true\n          ],\n          [\n            24,\n            50,\n            0.772,\n            0.714,\n            5.8,\n            true\n          ],\n          [\n            28,\n            58,\n            0.782,\n            0.7,\n            8.2,\n            true\n          ],\n          [\n            32,\n            67,\n            0.789,\n            0.681,\n            10.8,\n            false\n          ],\n          [\n            36,\n            75,\n            0.79,\n            0.655,\n            13.5,\n            false\n          ],\n          [\n            40,\n            83,\n            0.785,\n            0.625,\n            16.0,\n            false\n          ],\n          [\n            44,\n            92,\n            0.772,\n            0.589,\n            18.3,\n            false\n          ],\n          [\n            48,\n            100,\n            0.748,\n            0.548,\n            20.0,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Architecture-Dependent Pareto Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"Qwen3_235B\",\n          \"Llama4_Scout\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"global_rho\",\n            -0.91,\n            -0.78,\n            \"both significant but Qwen stronger\"\n          ],\n          [\n            \"per_lang_sig_count\",\n            \"15/20\",\n            \"6/20\",\n            \"Qwen consistent, Llama mixed\"\n          ],\n          [\n            \"median_per_lang_rho\",\n            -0.64,\n            -0.28,\n            \"2.3x difference in effect size\"\n          ],\n          [\n            \"positive_rho_langs\",\n            0,\n            3,\n            \"Llama has ar/hi/ko reversed\"\n          ],\n          [\n            \"best_transfer_depth_pct\",\n            55,\n            58,\n            \"comparable location\"\n          ],\n          [\n            \"en_zs_gap_at_knee_pp\",\n            4.2,\n            3.4,\n            \"comparable magnitude\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Transfer Conditions Comparison (both models, at best-transfer layer)\",\n        \"columns\": [\n          \"condition\",\n          \"Qwen3_mean_20\",\n          \"Llama4_mean_20\",\n          \"combined_mean\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.72,\n            0.7,\n            0.71\n          ],\n          [\n            \"mean-shift\",\n            0.72,\n            0.7,\n            0.71\n          ],\n          [\n            \"linear_proj_200\",\n            0.74,\n            0.718,\n            0.729\n          ],\n          [\n            \"few-shot-25\",\n            0.708,\n            0.692,\n            0.7\n          ],\n          [\n            \"few-shot-100\",\n            0.735,\n            0.718,\n            0.727\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的 global rho 都显著（满足 pareto_spearman_rho_significant_archs = 2 的 约束），但 effect size 差异明显。Qwen3 的 strong tradeoff 意味着 practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择； Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 \\\"free-ride\\\" 深层的 EN improvement 而不牺牲 transfer。这一差异无法从 domain adaptation theory 预测——它是架构特有的 empirical finding。 Best-transfer depth 在两个架构上收敛至 55-58%，暗示一个 universal \\\"mid-depth transfer zone\\\"，但 frontier 的 steepness 是 architecture-specific。\\n\\n\\nLlama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language 分析揭示了明显的异质性：仅 6/20 languages 有显著负 ρ，而 ar/hi/ko 展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31 优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta 的训练策略使 ar/hi/ko 在深层保持更好的 cross-lingual alignment，可能 因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。 Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language 分析揭示这不是 universal pattern。与 Qwen3 的对比清晰：Qwen3 的 15/20 significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一 architecture-dependent tradeoff strength 是 Claim 1 的核心发现。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\",\n    \"description\": \"Linear CKA (EN vs each target) at every probed layer, 20 languages × 2 models。核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b) partial Spearman controlling for normalized depth — THE single most important analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。验证 pilot finding 的 Simpson's Paradox 在 full-scale 上双架构复现。\\n\",\n    \"results\": {\n      \"qwen3_raw_rho\": -0.36,\n      \"qwen3_raw_p\": 0.0001,\n      \"llama4_raw_rho\": -0.41,\n      \"llama4_raw_p\": 0.0001,\n      \"qwen3_partial_rho\": 0.48,\n      \"qwen3_partial_p\": 0.002,\n      \"qwen3_partial_bootstrap_ci_95\": [\n        0.31,\n        0.62\n      ],\n      \"llama4_partial_rho\": 0.41,\n      \"llama4_partial_p\": 0.008,\n      \"llama4_partial_bootstrap_ci_95\": [\n        0.22,\n        0.57\n      ],\n      \"simpson_paradox_confirmed_both_archs\": true,\n      \"qwen3_per_layer_positive_count\": 18,\n      \"qwen3_per_layer_significant_count\": 6,\n      \"llama4_per_layer_positive_count\": 9,\n      \"llama4_per_layer_significant_count\": 3,\n      \"qwen3_cka_peak_layer\": 16,\n      \"qwen3_cka_peak_value\": 0.82,\n      \"qwen3_cka_at_en_optimal_layer\": 0.28,\n      \"qwen3_cka_cliff_onset_depth_pct\": 55,\n      \"llama4_cka_peak_layer\": 12,\n      \"llama4_cka_peak_value\": 0.84,\n      \"llama4_cka_at_en_optimal_layer\": 0.35,\n      \"llama4_cka_cliff_onset_depth_pct\": 50,\n      \"transfer_collapse_cka_threshold\": 0.35,\n      \"below_threshold_mean_zs_auroc\": 0.58,\n      \"above_threshold_mean_zs_auroc\": 0.72,\n      \"correctness_subspace_angle_within_layer_mean_deg\": 12.4,\n      \"correctness_subspace_angle_across_layer_mean_deg\": 38.7,\n      \"correctness_direction_persists_despite_global_cka_decline\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Simpson's Paradox — Raw vs Partial Correlation\",\n        \"columns\": [\n          \"model\",\n          \"analysis\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"bootstrap_95CI\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"raw pooled (CKA vs ZS AUROC)\",\n            -0.36,\n            \"<0.001\",\n            \"[-0.44, -0.27]\",\n            \"negative — depth confound\"\n          ],\n          [\n            \"Qwen3-235B\",\n            \"partial (controlling depth)\",\n            0.48,\n            0.002,\n            \"[+0.31, +0.62]\",\n            \"positive — genuine geometric signal\"\n          ],\n          [\n            \"Llama4 Scout\",\n            \"raw pooled (CKA vs ZS AUROC)\",\n            -0.41,\n            \"<0.001\",\n            \"[-0.50, -0.31]\",\n            \"negative — depth confound\"\n          ],\n          [\n            \"Llama4 Scout\",\n            \"partial (controlling depth)\",\n            0.41,\n            0.008,\n            \"[+0.22, +0.57]\",\n            \"positive — genuine geometric signal\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"depth_pct\",\n          \"mean_CKA_20lang\",\n          \"spearman_rho_n20\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            12,\n            13,\n            0.78,\n            0.52,\n            0.019\n          ],\n          [\n            20,\n            21,\n            0.81,\n            0.48,\n            0.032\n          ],\n          [\n            28,\n            30,\n            0.76,\n            0.55,\n            0.012\n          ],\n          [\n            36,\n            38,\n            0.68,\n            0.51,\n            0.022\n          ],\n          [\n            44,\n            47,\n            0.56,\n            0.46,\n            0.041\n          ],\n          [\n            52,\n            55,\n            0.45,\n            0.43,\n            0.058\n          ],\n          [\n            60,\n            64,\n            0.38,\n            0.38,\n            0.098\n          ],\n          [\n            68,\n            72,\n            0.3,\n            0.33,\n            0.155\n          ],\n          [\n            72,\n            77,\n            0.28,\n            0.28,\n            0.231\n          ],\n          [\n            80,\n            85,\n            0.22,\n            0.21,\n            0.372\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"HIGH_CKA\",\n          \"MID_CKA\",\n          \"LOW_CKA\",\n          \"overall_CKA\"\n        ],\n        \"rows\": [\n          [\n            13,\n            0.86,\n            0.79,\n            0.62,\n            0.78\n          ],\n          [\n            30,\n            0.84,\n            0.77,\n            0.58,\n            0.76\n          ],\n          [\n            47,\n            0.68,\n            0.56,\n            0.35,\n            0.56\n          ],\n          [\n            64,\n            0.48,\n            0.37,\n            0.22,\n            0.38\n          ],\n          [\n            77,\n            0.38,\n            0.27,\n            0.14,\n            0.28\n          ],\n          [\n            94,\n            0.25,\n            0.18,\n            0.09,\n            0.19\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Subspace Angle Analysis (correctness direction)\",\n        \"columns\": [\n          \"comparison_type\",\n          \"mean_angle_deg\",\n          \"std_deg\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"within-layer cross-language (same layer, different langs)\",\n            12.4,\n            5.8,\n            \"highly aligned — correctness direction is near-universal\"\n          ],\n          [\n            \"cross-layer same-language (same lang, different layers)\",\n            38.7,\n            11.2,\n            \"significant drift — direction rotates with depth\"\n          ],\n          [\n            \"random baseline (shuffled)\",\n            87.3,\n            2.1,\n            \"near-orthogonal — signal is non-trivial\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002, Llama=+0.41 p=0.008），是本文的核心几何洞见。这不是 trivially expected from measurement overlap（CKA 和 transfer AUROC 都衡量 EN-target 相似性） ——sign reversal 从负到正是 non-trivial 的。\\nSubspace angle analysis 提供 mechanistic grounding：correctness direction 在同一 layer 内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差 ~39°（significant rotation）。这解释了为何 CKA（衡量全局 representation similarity）与 transfer（衡量 correctness direction alignment）的关系 需要控制 depth 后才能显现：全局 CKA 下降反映的是 non-correctness dimensions 的 divergence，correctness subspace 本身作为 low-dimensional feature 持续存在。\\nCKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异： Qwen3 的 CKA cliff 更陡（L52→L60 从 0.45 降至 0.38），导致更多语言 在 deep layers 穿越 threshold → strong tradeoff；Llama4 的 cliff 更缓 （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越 threshold → weak/mixed tradeoff。\\n这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成 完整的 geometric explanation：architecture-dependent CKA cliff steepness → architecture-dependent Pareto frontier strength。\\n\\n\\nSimpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper → representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe stronger → higher absolute AUROC up to a point），创造了一个 confound。 Raw pooled correlation 为负是因为 shallow layers 有 high CKA 但 low AUROC （probe 本身弱），deep layers 有 low CKA 但 higher AUROC（probe 强虽然 transfer degrades）。控制 depth 后，within 每个 layer，higher CKA 的 语言确实有 better transfer，partial rho 为正。\\nMVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。 Full-scale（20 langs × 12-24 layers）增强统计 power：per-layer test 从 n=5 增至 n=20，partial correlation 的 bootstrap CI 不含零。\\nQwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA cliff 一致：Qwen 的 CKA 变异范围更大（peak 0.82 → floor 0.28 vs Llama 0.84 → 0.35），为 partial correlation 提供更多 signal。\\nMVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为： (1) n 从 5 增至 20 语言，power 大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言）， 扩大了 within-layer variance。\\nCKA cliff threshold ~0.35 标记了 \\\"transfer collapse zone\\\"：当 CKA 低于此阈值时，correctness direction 的 cross-lingual overlap 不足以 支撑 zero-shot transfer。Subspace angle analysis 揭示 correctness direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨 layer 旋转 ~39°（significant drift），解释了为何 within-layer CKA 预测 transfer 但 raw pooled 不预测。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits). English labels + parallel activations from GlobalMMLU test-split 70/30 partition. Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier, both models × 20 languages. α sweep [0.01–10], β sweep [0.001–1.0] across 3 OOM.\\n\",\n    \"results\": {\n      \"best_alpha\": 0.1,\n      \"best_beta\": 0.05,\n      \"caclr_mean_delta_auroc_vs_zs\": 0.035,\n      \"caclr_mean_delta_auroc_vs_linproj\": 0.015,\n      \"caclr_improvement_at_deep_layers_pp\": 4.8,\n      \"caclr_improvement_at_shallow_layers_pp\": 1.2,\n      \"caclr_improvement_pass_rate\": 0.88,\n      \"qwen3_caclr_mean_auroc_20lang\": 0.757,\n      \"qwen3_caclr_delta_vs_zs_pp\": 3.7,\n      \"qwen3_caclr_ece_mean\": 0.078,\n      \"llama4_caclr_mean_auroc_20lang\": 0.733,\n      \"llama4_caclr_delta_vs_zs_pp\": 3.3,\n      \"llama4_caclr_ece_mean\": 0.085,\n      \"beta_0001_delta_pp\": 0.5,\n      \"beta_001_delta_pp\": 1.8,\n      \"beta_005_delta_pp\": 3.5,\n      \"beta_01_delta_pp\": 3.2,\n      \"beta_10_delta_pp\": 0.8,\n      \"alpha_001_ece_improvement_pp\": 1.5,\n      \"alpha_01_ece_improvement_pp\": 3.2,\n      \"alpha_10_ece_improvement_pp\": 2.8,\n      \"alpha_100_ece_improvement_pp\": -0.5,\n      \"bce_only_auroc\": 0.71,\n      \"bce_sbece_auroc\": 0.722,\n      \"bce_consistency_auroc\": 0.738,\n      \"bce_sbece_consistency_auroc\": 0.745,\n      \"mmd_kernel\": \"Gaussian RBF, bandwidth=median heuristic\",\n      \"optimizer\": \"Adam, lr=1e-3, linear warmup 10%\",\n      \"epochs\": 50,\n      \"early_stopping\": \"patience=10, monitor=val_auroc\",\n      \"initialization\": \"from standard LR solution\",\n      \"batch_size\": 256,\n      \"mmd_items\": \"same items as BCE (overlapping)\",\n      \"parallel_set_size_range\": [\n        1800,\n        4200\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: β Sweep — Consistency Loss Effect\",\n        \"columns\": [\n          \"beta\",\n          \"mean_delta_auroc_vs_zs_pp\",\n          \"mean_delta_ece_pp\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.0,\n            0.0,\n            \"baseline (BCE only)\"\n          ],\n          [\n            0.001,\n            0.5,\n            -0.3,\n            \"marginal improvement\"\n          ],\n          [\n            0.01,\n            1.8,\n            -1.1,\n            \"clear positive signal\"\n          ],\n          [\n            0.05,\n            3.5,\n            -2.4,\n            \"optimal — best tradeoff\"\n          ],\n          [\n            0.1,\n            3.2,\n            -2.0,\n            \"slight over-regularization\"\n          ],\n          [\n            1.0,\n            0.8,\n            -0.5,\n            \"MMD dominates, probe accuracy degrades\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean_20\",\n          \"ece_mean_20\",\n          \"requires_labels\",\n          \"key_resource\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.71,\n            0.118,\n            \"none\",\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.71,\n            0.118,\n            \"none\",\n            \"—\"\n          ],\n          [\n            \"linear_proj_50\",\n            0.725,\n            0.098,\n            \"50 parallel pairs\",\n            \"Procrustes\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.729,\n            0.095,\n            \"200 parallel pairs\",\n            \"Procrustes\"\n          ],\n          [\n            \"few-shot-25\",\n            0.7,\n            0.102,\n            \"25 labeled\",\n            \"target labels\"\n          ],\n          [\n            \"few-shot-100\",\n            0.727,\n            0.088,\n            \"100 labeled\",\n            \"target labels\"\n          ],\n          [\n            \"CaCLR\",\n            0.745,\n            0.082,\n            \"none\",\n            \"parallel activations\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"zs_auroc\",\n          \"caclr_auroc\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            30,\n            0.733,\n            0.745,\n            1.2\n          ],\n          [\n            43,\n            0.748,\n            0.766,\n            1.8\n          ],\n          [\n            55,\n            0.72,\n            0.752,\n            3.2\n          ],\n          [\n            64,\n            0.69,\n            0.738,\n            4.8\n          ],\n          [\n            77,\n            0.638,\n            0.688,\n            5.0\n          ],\n          [\n            85,\n            0.601,\n            0.641,\n            4.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC improvement（实际 deep-layer mean = +4.8pp），且 β sweep across 3 OOM 清晰展现最优区间。Component ablation 证实 L_consistency 是主要 contributor（+2.8pp），L_SB-ECE 提供 complementary calibration improvement（+0.7pp ECE, +0.7pp AUROC synergy）。\\nCaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用 training dynamics（gradient 信号引导 probe 朝 language-invariant direction 收敛），而 Procrustes 只做 post-hoc geometric correction。但差距不大 是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit distributions，不能做 full subspace alignment。\\nDeep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers 的 capability-specific component 更大，CaCLR 的 consistency loss 正好 在这些 layers 有更多 signal 来 exploit。这构成 Pareto→Decomposition→CaCLR→CKA 因果链的第三环。\\n\\n\\nCaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习 language-invariant features：EN 和 target-language 的 probe 输出分布 应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的 logit mean 和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的 \\\"universal correctness subspace\\\"。\\n+3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能 捕获 first-order distributional alignment（mean/variance matching）， 但无法完成 full rotational alignment（需要 d-dimensional 操作）。Linear projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化 probe 本身；CaCLR 的优势在于 end-to-end 优化但受 1-D 约束。两者差距 仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性 投影解决的）而非 distributional（MMD 解决的）。\\nβ sweep across 3 OOM 清晰展现 \\\"sweet spot\\\"：β=0.001 太弱（gradient noise > signal），β=1.0 太强（MMD 主导 BCE，probe accuracy 下降 2pp）。 Optimal β=0.05 平衡了 accuracy 和 consistency。\\nDeep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为 deep layers 有更大的 capability-specific component（Claim 2 decomposition 所揭示），CaCLR 的 consistency loss 正好 target 这个 component。这与 difficulty-capability decomposition 形成因果闭环。\\n88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving pairs 是 HIGH-resource languages（如 Qwen3-zh, Qwen3-nl）on shallow layers where ZS transfer 已经接近 ceiling。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation (Decomposition)\",\n    \"description\": \"IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。包含 random-direction control。\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_mean\": 0.68,\n      \"difficulty_probe_r2_range\": [\n        0.55,\n        0.78\n      ],\n      \"difficulty_var_explained_pct\": 65,\n      \"capability_var_explained_pct\": 35,\n      \"difficulty_transfer_degradation_share_pct\": 12,\n      \"capability_transfer_degradation_share_pct\": 88,\n      \"decomp_capability_delta_auroc\": 0.03,\n      \"residual_en_auroc_drop_pp\": 4.5,\n      \"residual_zs_transfer_drop_pp\": 0.8,\n      \"random_direction_control_delta_pp\": -1.2,\n      \"prescriptive_accuracy\": 0.78,\n      \"capability_transfer_drop_by_depth\": {\n        \"20pct\": 0.6,\n        \"50pct\": 2.8,\n        \"80pct\": 8.5\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Decomposition Results\",\n        \"columns\": [\n          \"component\",\n          \"var_pct\",\n          \"transfer_auroc_mean\",\n          \"transfer_drop_pp\",\n          \"degradation_share_pct\"\n        ],\n        \"rows\": [\n          [\n            \"full_correctness\",\n            100,\n            0.71,\n            9.0,\n            100\n          ],\n          [\n            \"difficulty_shared\",\n            65,\n            0.698,\n            1.1,\n            12\n          ],\n          [\n            \"capability_specific\",\n            35,\n            0.615,\n            12.8,\n            88\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 14: Capability Transfer Drop by Depth\",\n        \"columns\": [\n          \"depth_band\",\n          \"difficulty_drop_pp\",\n          \"capability_drop_pp\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"20-30%\",\n            0.2,\n            0.6,\n            \"3×\"\n          ],\n          [\n            \"40-50%\",\n            0.6,\n            2.8,\n            \"4.7×\"\n          ],\n          [\n            \"60-70%\",\n            1.0,\n            5.6,\n            \"5.6×\"\n          ],\n          [\n            \"75-90%\",\n            1.5,\n            8.5,\n            \"5.7×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 清晰分离 transferable vs non-transferable components。 Difficulty 占大部分 variance 但 near-perfectly transfers（仅 12% degradation share），capability 占少数但驱动几乎所有 degradation。 这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty dominates there）但在 deep layers 失败（capability grows）。 Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的， 而是可以指导 alignment strategy selection。\\n\\n\\nIRT difficulty 是 language-agnostic property：hard questions are hard everywhere。Ridge regression captures this linearly (R²=0.68, 与 Civelli et al. 的 shared difficulty finding 一致)。Difficulty 占 correctness variance 的 65% 但仅贡献 12% 的 transfer degradation， 因为 difficulty signal 本质上是 universal 的。Capability-specific residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且 degradation 随 depth 指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。\\n这一 decomposition 解释了 Pareto frontier 的 mechanistic origin： deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent competence），而这个 component 恰好是 最难 transfer 的。CaCLR 的 consistency loss works precisely because it targets this component。\\nRandom-direction control（-1.2pp, 随机方向 projection 反而损害）确认 difficulty direction 不是 arbitrary dimensionality reduction 的 artifact， 而是 genuine signal。\\nPrescriptive accuracy 78%：给定语言-layer 的 difficulty/capability ratio，预测应使用 zero-shot（difficulty-dominant）还是 CaCLR （capability-dominant）策略，在 78% 的 cases 中正确。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。 Both models × 5 representative layers × 20 languages。确定最小数据需求 和 resource-tier 分层饱和。\\n\",\n    \"results\": {\n      \"pairs_to_95pct_overall\": 42,\n      \"pairs_to_95pct_HIGH\": 22,\n      \"pairs_to_95pct_MID\": 38,\n      \"pairs_to_95pct_LOW\": 48,\n      \"pairs_10_pct_of_200\": 0.72,\n      \"pairs_20_pct_of_200\": 0.86,\n      \"pairs_30_pct_of_200\": 0.92,\n      \"pairs_50_pct_of_200\": 0.97,\n      \"pairs_100_pct_of_200\": 0.99,\n      \"pairs_200_baseline_auroc_mean\": 0.729,\n      \"procrustes_reversal_threshold\": 0.52,\n      \"procrustes_helps_below_threshold_delta_pp\": 3.8,\n      \"procrustes_hurts_above_threshold_delta_pp\": -1.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Projection Sample Efficiency\",\n        \"columns\": [\n          \"n_pairs\",\n          \"pct_of_200pair_performance\",\n          \"mean_auroc\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            10,\n            72,\n            0.724,\n            \"unstable, high variance across runs\"\n          ],\n          [\n            20,\n            86,\n            0.728,\n            \"captures dominant rotation\"\n          ],\n          [\n            30,\n            92,\n            0.731,\n            \"near plateau for HIGH langs\"\n          ],\n          [\n            50,\n            97,\n            0.734,\n            \"near plateau for all tiers\"\n          ],\n          [\n            100,\n            99,\n            0.737,\n            \"marginal returns\"\n          ],\n          [\n            200,\n            100,\n            0.729,\n            \"baseline (reference)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 16: Saturation by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"pairs_to_90pct\",\n          \"pairs_to_95pct\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            15,\n            22,\n            \"rotation is simple, low effective rank\"\n          ],\n          [\n            \"MID\",\n            25,\n            38,\n            \"moderate rotation complexity\"\n          ],\n          [\n            \"LOW\",\n            35,\n            48,\n            \"complex rotation, more data needed\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: Procrustes Effect Reversal\",\n        \"columns\": [\n          \"zs_auroc_range\",\n          \"n_lang_layer_pairs\",\n          \"mean_delta_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"<0.45\",\n            42,\n            5.2,\n            \"strong positive\"\n          ],\n          [\n            \"0.45-0.52\",\n            68,\n            2.4,\n            \"moderate positive\"\n          ],\n          [\n            \"0.52-0.60\",\n            95,\n            0.3,\n            \"near-zero (transition zone)\"\n          ],\n          [\n            \"0.60-0.70\",\n            88,\n            -1.2,\n            \"negative — hurts\"\n          ],\n          [\n            \">0.70\",\n            47,\n            -0.8,\n            \"slight negative\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"~42 pairs to 95% performance 是 directly actionable 的 practical finding：对于大多数语言，仅需 <50 parallel sentences 即可达到接近 supervised-level alignment。Resource-tier stratification（HIGH 22 vs LOW 48 pairs）提供了 per-language guidance。\\nProcrustes reversal at 0.52 与 CKA threshold 0.35 形成对应： CKA < 0.35 的 language-layer combinations 对应 ZS < 0.52（ 因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的 区域。这构成了 geometric explanation 的 practical corollary。\\n\\n\\nLinear projection (Procrustes) 学习 EN→target 的 rotation matrix。 20 pairs 即可估计 dominant rotational components（correctness subspace 是 low-dimensional 的，前几个 principal angles 解释 90%+ 的 alignment structure）。42 pairs 达到 95% 因为边际的 minor components 需要更多 data 来稳定估计。\\nResource-tier stratification 清晰：HIGH languages（zh/es/de 等）的 activation distributions 与 EN 更相似，rotation matrix 的 effective rank 更低（fewer parameters to estimate），22 pairs 即可。LOW languages 需要估计更 complex rotation（effective rank 更高），48 pairs。\\nProcrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时， correctness direction 严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。 当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes 引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35 （与 plan_011 的 cliff threshold 一致）。\\n这一 finding 直接 actionable：practitioners 应先测 ZS transfer， only apply Procrustes when baseline < 0.52。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Full-Scale Hewitt & Liang (2019)\",\n    \"description\": \"Extend MVP English-only control task analysis to 20 languages × 2 architectures。Train probes on randomly permuted labels, compute selectivity = real_AUROC - control_AUROC。Identify capacity artifacts by language, layer, and model。\\n\",\n    \"results\": {\n      \"en_selectivity_range\": [\n        0.02,\n        0.26\n      ],\n      \"en_selectivity_meaningful_layers\": [\n        16,\n        20,\n        24,\n        27\n      ],\n      \"control_artifact_rate_lowres\": 0.27,\n      \"control_artifact_rate_midres\": 0.05,\n      \"control_artifact_rate_highres\": 0.03,\n      \"low_res_langs_most_affected\": [\n        \"yo\",\n        \"ig\",\n        \"te\",\n        \"sw\"\n      ],\n      \"artifact_concentration_depth\": \"60-100% depth\",\n      \"cross_lingual_selectivity_mean\": {\n        \"HIGH\": 0.22,\n        \"MID\": 0.18,\n        \"LOW\": 0.09\n      },\n      \"languages_with_any_meaningful_selectivity\": 17,\n      \"control_auroc_mean_all\": 0.495,\n      \"control_auroc_std\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Selectivity by Resource Tier and Depth\",\n        \"columns\": [\n          \"depth_band\",\n          \"HIGH_selectivity\",\n          \"MID_selectivity\",\n          \"LOW_selectivity\"\n        ],\n        \"rows\": [\n          [\n            \"0-30%\",\n            0.04,\n            0.03,\n            0.01\n          ],\n          [\n            \"30-60%\",\n            0.18,\n            0.14,\n            0.06\n          ],\n          [\n            \"60-80%\",\n            0.28,\n            0.22,\n            0.1\n          ],\n          [\n            \"80-100%\",\n            0.25,\n            0.2,\n            0.08\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 19: Artifact Rates by Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_lang_layer_combinations\",\n          \"artifact_count\",\n          \"artifact_rate\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            384,\n            12,\n            \"3%\"\n          ],\n          [\n            \"MID\",\n            336,\n            17,\n            \"5%\"\n          ],\n          [\n            \"LOW\",\n            240,\n            65,\n            \"27%\"\n          ],\n          [\n            \"total\",\n            960,\n            94,\n            \"10%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"27% low-resource artifact rate 是 methodological warning for the field： cross-lingual probing studies 如果不做 selectivity checks 会高估 low-resource transfer quality。重要的是 artifacts 集中在 low-resource + deep layers，不波及 mid/high-resource 或 shallow layers，因此本文的 核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。\\n\\n\\nMVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual extension 揭示了 resource-tier dependent artifact pattern：\\nLOW-resource languages 的 27% artifact rate 源于两个因素：(1) these languages 在 model pretraining 中占比极低，activation distributions 相对 high-resource 更 \\\"shallow\\\" (less structured)，linear probes 更容易 通过 capacity 而非 genuine signal 拟合少量 patterns；(2) GlobalMMLU 的 low-resource translations 质量较低，引入 noise 使 correctness signal 更弱，selectivity 更接近 chance。\\nMid/high-resource 的 artifact rate 极低（3-5%）因为 representation quality 高，probe 有 genuine signal 可以 leverage。\\nArtifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的 low-resource CKA 已经很低（<0.2），cross-lingual activation structure 不足以支撑 genuine correctness probing，probe 退化为 memorizing dataset-specific patterns。\\n这一 finding 是 field-level contribution：此前没有人在 cross-lingual probing 中检查 selectivity controls。28% 的 low-resource artifact rate 意味着没有 control tasks 的 cross-lingual probing 结果 （包括 Xiao et al.）需要谨慎解读。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Correctness-Confidence Orthogonality\",\n    \"description\": \"Extract verbalized confidence direction, compute cosine similarity with correctness direction, 20 languages × 2 architectures。 Supporting evidence for Claim 4 (subsection)。\\n\",\n    \"results\": {\n      \"cosine_mean_overall\": 0.05,\n      \"cosine_range\": [\n        0.02,\n        0.09\n      ],\n      \"cosine_en\": 0.03,\n      \"all_below_0p10\": true,\n      \"qwen3_cosine_mean\": 0.046,\n      \"llama4_cosine_mean\": 0.054,\n      \"HIGH_cosine_mean\": 0.038,\n      \"MID_cosine_mean\": 0.052,\n      \"LOW_cosine_mean\": 0.072,\n      \"resource_tier_correlation\": -0.66\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 20: Orthogonality by Tier (cosine similarity)\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"qwen3_mean\",\n          \"llama4_mean\",\n          \"combined_mean\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            8,\n            0.035,\n            0.041,\n            0.038\n          ],\n          [\n            \"MID\",\n            7,\n            0.048,\n            0.056,\n            0.052\n          ],\n          [\n            \"LOW\",\n            5,\n            0.066,\n            0.078,\n            0.072\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality universally holds (39/40 pairs below 0.10, all 40 below 0.095)，confirming output-based calibration methods are structurally limited across languages。Resource-tier gradient 是新 finding，但 effect size 小（range only 0.034），作为 subsection 足够。\\n\\n\\nMiao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension to 20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映 transformer 的 structural property：verbalized confidence 由 language modeling head 从 surface-level token probabilities 生成，correctness 由 intermediate representations geometry 编码，两者 architecturally decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation in low-resource languages 更 noisy，不完全 decoupled。Resource-tier gradient（r=-0.66）说明更好的 multilingual training → 更清晰的 correctness/confidence separation。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer, both models。 Validates linear probe choice for transfer。\\n\",\n    \"results\": {\n      \"logreg_en_auroc_best\": 0.81,\n      \"mlp_en_auroc_best\": 0.83,\n      \"mlp_en_gain_pp\": 2.0,\n      \"logreg_zs_drop_mean_pp\": 9.0,\n      \"mlp_zs_drop_mean_pp\": 14.5,\n      \"logreg_transfer_advantage_pp\": 5.5,\n      \"logreg_advantage_shallow_pp\": 2.0,\n      \"logreg_advantage_deep_pp\": 8.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Probe Complexity (Qwen3, at EN-optimal layer)\",\n        \"columns\": [\n          \"probe_type\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"zs_drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"logistic_regression\",\n            0.81,\n            0.72,\n            9.0\n          ],\n          [\n            \"mlp_2layer_h128\",\n            0.83,\n            0.685,\n            14.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp EN performance 换取 5.5pp transfer improvement。Depth interaction confirms nonlinear language-specific features drive deep-layer degradation。\\n\\n\\nLinear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace 是 near-universal linear structure（subspace angle ~12° from plan_011）。 MLPs fit nonlinear decision boundaries that overfit EN-specific feature interactions，gaining +2pp EN AUROC but losing 5.5pp transfer。Gap 在 deep layers 放大（+8.2pp advantage for logreg at 80% depth）因为 deep layers 有更多 language-specific nonlinear structure for MLP to exploit。 This justifies logreg as primary probe and supports geometric interpretation of Pareto frontier。\\n\"\n  },\n  {\n    \"name\": \"Cross-Benchmark Generalization (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages each)。Tests domain generalization。\\n\",\n    \"results\": {\n      \"belebele_zs_mean_20\": 0.695,\n      \"belebele_caclr_mean_20\": 0.728,\n      \"belebele_caclr_delta_pp\": 3.3,\n      \"mmlupx_zs_mean_20\": 0.68,\n      \"mmlupx_caclr_mean_20\": 0.715,\n      \"mmlupx_caclr_delta_pp\": 3.5,\n      \"cross_benchmark_caclr_cv\": 0.04\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Cross-Benchmark CaCLR Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_mean_20\",\n          \"caclr_mean_20\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.71,\n            0.745,\n            3.5\n          ],\n          [\n            \"Belebele\",\n            0.695,\n            0.728,\n            3.3\n          ],\n          [\n            \"MMLU-ProX\",\n            0.68,\n            0.715,\n            3.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR generalizes across benchmarks with low variance。Cross-benchmark consistency is the strongest defense against overfitting concerns。\\n\\n\\nBelebele (reading comprehension) 和 MMLU-ProX (harder factual) 的 baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement 幅度 consistent（3.3-3.5pp vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实 CaCLR addresses 一个 fundamental representation alignment issue 而非 overfitting to specific benchmark。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset。\\n\",\n    \"results\": {\n      \"llama4_w4a16_fp16_auroc_diff_mean_pp\": 0.3,\n      \"llama4_w4a16_fp16_auroc_diff_max_pp\": 0.8,\n      \"llama4_rank_correlation\": 0.996,\n      \"qwen3_int4_fp16_auroc_diff_mean_pp\": 0.5,\n      \"qwen3_int4_fp16_auroc_diff_max_pp\": 1.1,\n      \"qwen3_rank_correlation\": 0.994,\n      \"conclusion\": \"quantization introduces negligible distortion for probing\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Quantization Comparison (5 representative layers)\",\n        \"columns\": [\n          \"model\",\n          \"layer\",\n          \"fp16_auroc\",\n          \"quant_auroc\",\n          \"diff_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Llama4\",\n            8,\n            0.637,\n            0.634,\n            0.3\n          ],\n          [\n            \"Llama4\",\n            16,\n            0.737,\n            0.735,\n            0.2\n          ],\n          [\n            \"Llama4\",\n            28,\n            0.784,\n            0.781,\n            0.3\n          ],\n          [\n            \"Llama4\",\n            36,\n            0.792,\n            0.789,\n            0.3\n          ],\n          [\n            \"Llama4\",\n            44,\n            0.774,\n            0.77,\n            0.4\n          ],\n          [\n            \"Qwen3\",\n            20,\n            0.712,\n            0.708,\n            0.4\n          ],\n          [\n            \"Qwen3\",\n            36,\n            0.78,\n            0.775,\n            0.5\n          ],\n          [\n            \"Qwen3\",\n            52,\n            0.808,\n            0.803,\n            0.5\n          ],\n          [\n            \"Qwen3\",\n            68,\n            0.812,\n            0.806,\n            0.6\n          ],\n          [\n            \"Qwen3\",\n            80,\n            0.807,\n            0.8,\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization safe for both models。Preempts reviewer concern #5。\\n\\n\\nW4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction 的 angular structure 仍 robust（0.5pp mean diff）， 因为 quantization noise 近似 isotropic，不 preferentially distort correctness-relevant directions。Rank correlation > 0.994 确认 Pareto frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3) 因为 Int4 比 W4A16 更 lossy。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture (Camera-Ready)\",\n    \"description\": \"Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16), 20 languages。Provides dense vs MoE contrast for camera-ready。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.8,\n      \"en_best_layer_idx\": 45,\n      \"zs_mean_20lang\": 0.71,\n      \"zs_best_transfer_layer_idx\": 36,\n      \"global_spearman_rho\": -0.85,\n      \"per_lang_rho_median\": -0.58,\n      \"caclr_delta_vs_zs_pp\": 3.0,\n      \"simpson_partial_rho\": 0.44,\n      \"simpson_partial_p\": 0.004\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: Three-Architecture Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_best\",\n          \"zs_mean_20\",\n          \"pareto_rho\",\n          \"simpson_partial_rho\",\n          \"caclr_delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE\",\n            94,\n            0.81,\n            0.72,\n            -0.91,\n            0.48,\n            3.7\n          ],\n          [\n            \"Llama4 Scout\",\n            \"MoE\",\n            48,\n            0.79,\n            0.7,\n            -0.78,\n            0.41,\n            3.3\n          ],\n          [\n            \"Gemma4 31B\",\n            \"Dense\",\n            60,\n            0.8,\n            0.71,\n            -0.85,\n            0.44,\n            3.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Three-architecture replication 是 universality claim 最强证据： Simpson's Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在 55-60% depth 处一致出现 knee，CaCLR 提供 3-3.7pp consistent gain。 Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth 的 property 而非 routing architecture 的。\\n\\n\\nGemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two MoE models），different pretraining recipe（Google vs Alibaba/Meta）， 60 layers（between Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models 因为 31B dense < 22B MoE active (MoE routing 提供 effective capacity boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91) 和 Llama (-0.78) 之间。Simpson's partial correlation 仍然显著 (rho=+0.44, p=0.004)， 确认 geometric insight 是 architecture-universal 而非 MoE-specific。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready。\\n\",\n    \"results\": {\n      \"total_languages\": 50,\n      \"zs_pass_rate_50lang\": 0.84,\n      \"zs_auroc_above_060_count\": 42,\n      \"caclr_improvement_positive_count\": 47,\n      \"mean_zs_auroc_50lang\": 0.69,\n      \"mean_caclr_auroc_50lang\": 0.72,\n      \"pareto_frontier_holds_all_langs\": true,\n      \"new_families\": [\n        \"Austronesian\",\n        \"Dravidian\",\n        \"Uralic\",\n        \"Kartvelian\",\n        \"Niger-Congo_B\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 23: Extended Coverage by Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"zs_mean\",\n          \"caclr_mean\",\n          \"caclr_gain_pp\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            10,\n            0.75,\n            0.78,\n            2.8\n          ],\n          [\n            \"MID\",\n            24,\n            0.71,\n            0.74,\n            3.5\n          ],\n          [\n            \"LOW\",\n            12,\n            0.62,\n            0.66,\n            4.2\n          ],\n          [\n            \"VERY_LOW\",\n            4,\n            0.53,\n            0.58,\n            5.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"50-language extension 确认 all findings at scale。Resource-tier gradient smooth, CaCLR benefit inversely correlated with resource level, no language family shows anomalous behavior。\\n\\nExpansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian, Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely low-resource 语言（Amharic, Khmer, Lao）可能 < 0.55 但代表 edge cases。 CaCLR 在 94% 的新增语言上 positive 因为 consistency loss mechanism 是 language-agnostic。Pareto frontier structure 在 50 languages 上 完全保持。\\n\"\n  }\n]",
      "numLines": 1779,
      "startLine": 1,
      "totalLines": 1779
    }
  },
  "sourceToolAssistantUUID": "2c6707ed-977f-49c6-8bb4-3130472df7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "f2dc5be3-178b-492f-a988-20c286bc96fa",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration transfer paper",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Assistant

_source line 15 · 2026-05-21T05:29:48.664Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also load the research and writing skills for reference on style.

Actually, looking at the instructions, I should just write the paper directly. Let me compose a complete LaTeX paper based on:

1. The experiment data (10 experiments with detailed results)
2. The paper framing (claims, story spine, related work)
3. The narrative guidance (Simpson's Paradox as core novelty, CaCLR as positive method, four-claim causal chain)

Let me structure the paper:
- Abstract
- Introduction
- Related Work
- Method (probing setup, decomposition, CaCLR, CKA analysis)


- Experiments section covering all ten experiments with results tables
- Results and analysis discussion
- Conclusion

I'm planning out the full structure with detailed sections for experimental setup including model specifications, and then I'll generate the LaTeX document with all the experiment tables and findings. I'm recounting the experiments more carefully—there are actually thirteen distinct experiments total, including the probe complexity comparison that I initially separated, quantization validation, a third architecture test, and extended language coverage across more languages.

Now I'm planning the paper structure strategically, deciding which tables belong in the main body versus the appendix to keep things readable while still being comprehensive. I'm prioritizing the key summary tables first—the three-architecture comparison, the Pareto frontiers for both major models, and the architecture-dependent comparisons—then working through the transfer conditions and other experimental results. Continuing through the remaining experimental tables covering Procrustes effects, resource tier analysis, cross-benchmark generalization, and the supplementary appendix tables with language-specific correlations and saturation metrics.

Now I'm organizing the full paper structure—I have thirteen experiments worth of data to integrate, and I need to make sure every result is sourced directly from the experiment data while keeping the presentation compact for a conference submission. Let me start drafting the complete paper with proper ACL formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2dc5be3-178b-492f-a988-20c286bc96fa",
  "isSidechain": false,
  "requestId": "req_011CbFAQf1yXxFcc3cqeAEBa",
  "type": "assistant",
  "uuid": "b5cd3f00-c410-4ad0-827a-9739b9977dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dx4UP6FbR4XT1yhs9fhYmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 24009,
      "cache_read_input_tokens": 23476,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 1882,
          "cache_read_input_tokens": 23476,
          "cache_creation_input_tokens": 24009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24009
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

_source line 16 · 2026-05-21T05:29:48.666Z_

Now let me load the writing skill for style reference, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5cd3f00-c410-4ad0-827a-9739b9977dea",
  "isSidechain": false,
  "requestId": "req_011CbFAQf1yXxFcc3cqeAEBa",
  "type": "assistant",
  "uuid": "ef2edbe4-9107-42e6-8b5d-b06357b1dc11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dx4UP6FbR4XT1yhs9fhYmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 24009,
      "cache_read_input_tokens": 23476,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 1882,
          "cache_read_input_tokens": 23476,
          "cache_creation_input_tokens": 24009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24009
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

_source line 17 · 2026-05-21T05:29:51.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJNM8hCv26nA2PU5kwRHcj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef2edbe4-9107-42e6-8b5d-b06357b1dc11",
  "isSidechain": false,
  "requestId": "req_011CbFAQf1yXxFcc3cqeAEBa",
  "type": "assistant",
  "uuid": "231a8164-5961-4a0d-a948-c0d0d2e82c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dx4UP6FbR4XT1yhs9fhYmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 24009,
      "cache_read_input_tokens": 23476,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 1882,
          "cache_read_input_tokens": 23476,
          "cache_creation_input_tokens": 24009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24009
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

_source line 18 · 2026-05-21T05:29:51.188Z_

<details><summary>↩ Tool result · `toolu_01WJNM8hCv26nA2PU5kwRHcj`</summary>

```text
1	---
2	name: xling-calib-direction-writing
3	description: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Writing Patterns (8 papers)
8	
9	## Narrative
10	
11	**Story type**: "突破局限型" (7/8). Blind spot → reveal → fill. High conf.
12	
13	**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.
14	
15	**Hooks** (pick one):
16	- English-centric gap: "Prior work focuses on English, leaving X unexplored" (xiao, zhou). 2/8.
17	- Name the meta-problem: "Square One Bias" (zhou) — forces acknowledgment.
18	- Cognitive dissonance: "LLMs are surprisingly well-calibrated" (joshi) — contradicts expectation.
19	- Pain narrowing: "most dangerous hallucination — confident wrong answers" (ji).
20	
21	**Tension**: Show standard practice actively fails, not just untried. "Fine-tuning doesn't change alignment" (liu). "Final layer overwrites multilingual signals" (zhou). "Aggregate correlation masks instance-level failure" (ravisankar). 3/8. High conf.
22	
23	## Insight Delivery
24	
25	**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.
26	
27	**Negative-as-evidence** (2/8): "X doesn't work" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).
28	
29	**"Finding the knob"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.
30	
31	## Figures
32	
33	**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.
34	
35	**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.
36	
37	**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.
38	
39	**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.
40	
41	**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.
42	
43	## Tables
44	
45	**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.
46	
47	**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.
48	
49	**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.
50	
51	**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "231a8164-5961-4a0d-a948-c0d0d2e82c59",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "7afd260e-cfc9-4464-b3f7-9666ebd36e11",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
      "content": "---\nname: xling-calib-direction-writing\ndescription: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations\ntype: skill\n---\n\n# Cross-Lingual Calibration — Writing Patterns (8 papers)\n\n## Narrative\n\n**Story type**: \"突破局限型\" (7/8). Blind spot → reveal → fill. High conf.\n\n**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.\n\n**Hooks** (pick one):\n- English-centric gap: \"Prior work focuses on English, leaving X unexplored\" (xiao, zhou). 2/8.\n- Name the meta-problem: \"Square One Bias\" (zhou) — forces acknowledgment.\n- Cognitive dissonance: \"LLMs are surprisingly well-calibrated\" (joshi) — contradicts expectation.\n- Pain narrowing: \"most dangerous hallucination — confident wrong answers\" (ji).\n\n**Tension**: Show standard practice actively fails, not just untried. \"Fine-tuning doesn't change alignment\" (liu). \"Final layer overwrites multilingual signals\" (zhou). \"Aggregate correlation masks instance-level failure\" (ravisankar). 3/8. High conf.\n\n## Insight Delivery\n\n**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.\n\n**Negative-as-evidence** (2/8): \"X doesn't work\" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).\n\n**\"Finding the knob\"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.\n\n## Figures\n\n**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.\n\n**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.\n\n**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.\n\n**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.\n\n**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.\n\n## Tables\n\n**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.\n\n**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.\n\n**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.\n\n**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "231a8164-5961-4a0d-a948-c0d0d2e82c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T05:29:51.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015kDZGmvnU6twZL79b1ci2z`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7afd260e-cfc9-4464-b3f7-9666ebd36e11",
  "isSidechain": false,
  "requestId": "req_011CbFAQf1yXxFcc3cqeAEBa",
  "type": "assistant",
  "uuid": "614d2c7a-6791-4dbd-be14-3708aee818bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dx4UP6FbR4XT1yhs9fhYmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4437,
      "cache_creation_input_tokens": 24009,
      "cache_read_input_tokens": 23476,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4437,
          "output_tokens": 1882,
          "cache_read_input_tokens": 23476,
          "cache_creation_input_tokens": 24009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24009
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

_source line 20 · 2026-05-21T05:29:52.158Z_

<details><summary>↩ Tool result · `toolu_015kDZGmvnU6twZL79b1ci2z`</summary>

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
  "parentUuid": "614d2c7a-6791-4dbd-be14-3708aee818bc",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "a4498880-96be-488f-98fd-7e7cda054d63",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "614d2c7a-6791-4dbd-be14-3708aee818bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T05:30:29.787Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the context I need. Let me write the full paper. I'll structure it as an EACL-format paper with all the required sections and tables covering every experiment.

Let me carefully compose the LaTeX now. I need to be particularly careful with:
1. Every number must come from experiment_data.json
2. Every experiment needs a section/table
3. Simpson's Paradox as core novelty
4. Four-claim causal chain

Let me write this comprehensively. The paper should use acl style (for EACL). Let me use the standard acl_natbib style since I don't have the actual style files. 

Actually, I'll go with a simple article class and reasonable academic formatting instead—the goal is to make it reviewable, not camera-ready. Now I need to plan out the table numbering carefully: Table 1 for the three-architecture summary, Table 2 for Qwen3-235B's Pareto frontier, Table 3 for Llama 4 Scout, Table 4 for architecture-dependent comparison, Table 5 for transfer conditions, Table 6 for Simpson's Paradox showing raw versus partial correlation, Table 7 for per-layer CKA-transfer correlation on Qwen3, and Table 8 continuing from there.

Then I have Tables 9 through 20 covering subspace angle analysis, decomposition results, capability transfer drop by depth, CaCLR comparisons, beta sweep effects, depth profiles, sample efficiency, Procrustes effects, selectivity by tier and depth, artifact rates, cross-lingual orthogonality, and cross-benchmark generalization. The appendix will have Tables A1 through A5 with per-language Spearman correlations, CKA heatmap summaries, saturation by tier, and probe complexity comparisons.

The user wants every experiment from the JSON file covered, so I need to be comprehensive even though it's a lot of tables. I'll merge strategically where it makes sense but ensure full coverage. Now I'm drafting the full LaTeX document with all the necessary packages and structure.

Writing LaTeX document... Now I'm organizing the key experimental results across all three models—Qwen3-235B shows the strongest transfer with a 0.72 zero-shot AUROC and consistent negative correlation across languages, while Llama 4 Scout demonstrates weaker transfer at 0.70 with more variable per-language patterns, and Gemma 4 31B reveals Simpson's Paradox where the aggregate correlation reverses when controlling for language. I need to track these precise metrics throughout the paper to support each claim about when calibration transfer succeeds. Looking at the linear projection results, I need 42 pairs to reach 95% accuracy, and the Procrustes reversal threshold sits at 0.52—improvements drop below that threshold but turn negative above it. The control tasks show artifact rates decrease sharply with resolution, from 27% at low-res down to just 3% at high-res. Across all orthogonality measures, cosine similarities stay well below 0.10, with the lowest resolution showing slightly higher values at 0.072. Finally, checking performance on other benchmarks, CaCLR consistently outperforms zero-shot by about 3.3-3.5 percentage points across GlobalMMLU, Belebele, and MMLU-ProX.

The probe complexity analysis reveals that linear readout achieves 0.81 accuracy with a 9-point zero-shot drop, while the MLP version reaches 0.83 but suffers a steeper 14.5-point decline—though linear transfer still maintains a 5.5-point advantage. Quantization experiments show minimal degradation: Llama4 at 4-bit weights loses just 0.3 percentage points with near-perfect rank correlation, and Qwen3 Int4 performs similarly at 0.5 points with 0.994 correlation. Testing across 50 languages yields an 84% pass rate with 47 showing positive CaCLR gains.

Now I'm ready to write the paper—I'll structure it thoroughly while keeping the presentation efficient, and I'll build out the bibliography with all the key references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4498880-96be-488f-98fd-7e7cda054d63",
  "isSidechain": false,
  "requestId": "req_011CbFATKBTZVJtYEd8qjyuR",
  "type": "assistant",
  "uuid": "9715f8a4-9bb0-4acd-9aea-e10a9410327f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MxajJ2gVk4Y63VaSKhxi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7294,
      "cache_read_input_tokens": 47485,
      "output_tokens": 20346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20346,
          "cache_read_input_tokens": 47485,
          "cache_creation_input_tokens": 7294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7294
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

_source line 22 · 2026-05-21T05:30:29.789Z_

Writing the complete LaTeX paper now. This covers all 13 experiments with corresponding sections and tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9715f8a4-9bb0-4acd-9aea-e10a9410327f",
  "isSidechain": false,
  "requestId": "req_011CbFATKBTZVJtYEd8qjyuR",
  "type": "assistant",
  "uuid": "5a792c7c-bbe0-41b8-beb7-83e7e3a9c754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MxajJ2gVk4Y63VaSKhxi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7294,
      "cache_read_input_tokens": 47485,
      "output_tokens": 20346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20346,
          "cache_read_input_tokens": 47485,
          "cache_creation_input_tokens": 7294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7294
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

_source line 23 · 2026-05-21T05:35:42.984Z_

<details open><summary>🔧 Tool call — Write · `toolu_0111iMTFEimA2WyEexoCvMeR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{array}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}\n\n\\newcommand{\\rmark}{\\textcolor{red}{$\\rho$}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{Geometric Analysis Reveals When and Why\\\\Cross-Lingual Calibration Transfer Succeeds}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nProbe-based calibration methods can detect whether a language model's internal representations encode answer correctness, but all existing approaches are English-only. We present the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B Dense), 50 languages, and five transfer conditions. Our analysis reveals four interconnected findings forming a causal chain. \\textbf{(1)}~A depth-transferability Pareto frontier whose strength is architecture-dependent: Qwen3 exhibits a strong, consistent tradeoff (per-language Spearman $\\rho$ significant in 15/20 languages) while Llama~4 shows a weak, language-specific pattern (6/20 significant; three languages exhibit reversed trends). \\textbf{(2)}~Decomposing correctness into difficulty-shared (65\\% variance, 12\\% of transfer degradation) and capability-specific (35\\% variance, 88\\% of degradation) components reveals that capability-specific representations drive deep-layer transfer failure. \\textbf{(3)}~CaCLR, a consistency-regularized calibration method requiring no target-language labels, provides a mean improvement of +3.5\\pp{} AUROC over zero-shot transfer, with gains concentrated at deep layers (+4.8\\pp). \\textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship---raw correlation is negative ($\\rho = -0.36$ to $-0.41$; depth confound) but partial correlation controlling for depth is significantly positive ($\\rho = +0.41$ to $+0.48$; $p < 0.01$ on both architectures)---reveals that within-layer cross-lingual CKA genuinely predicts transfer quality while the correctness direction occupies a near-universal subspace (within-layer angle $12.4^{\\circ}$). We additionally find that 28\\% of low-resource probing results are capacity artifacts, and that Procrustes alignment reverses direction at a threshold of $\\sim$0.52 zero-shot AUROC. Code and probes will be released.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nMultilingual large language models suffer from a persistent calibration gap: non-English languages exhibit expected calibration error (ECE) up to five times worse than English \\cite{joshi2024llm}. Output-based recalibration methods such as temperature scaling require per-language calibration data, while ensemble approaches like MKA incur multiplicative inference costs \\cite{zhou2024lace}. Recent work on probe-based calibration offers an alternative: linear probes trained on internal representations can detect whether a model ``knows'' the answer is correct, and this correctness direction is nearly orthogonal to the model's verbalized confidence \\cite{miao2026coral,miao2026steering}. However, the entire probe-based calibration literature is English-only.\n\nCan English-trained correctness probes transfer to other languages without target-language labels? If so, under what conditions, and why does transfer succeed or fail? These questions are fundamental to the viability of representation-level calibration beyond English. Xiao et al.\\ \\cite{xiao2025crosslingual} transferred \\emph{knowledge boundary} probes---binary answerability classifiers at the input level---and found encouraging results in 8 languages. But correctness probing targets a fundamentally different signal: output-dependent accuracy on specific items, not input-level answerability. The cross-lingual properties of correctness representations remain unexplored.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer. Probing three architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense) across 20--50 typologically diverse languages on GlobalMMLU, we discover a \\emph{depth-transferability Pareto frontier}: deeper layers yield better English probes but progressively degrade in zero-shot cross-lingual transfer. The frontier's strength is architecture-dependent---strong and consistent on Qwen3, weak and language-specific on Llama~4. A geometric analysis based on centered kernel alignment (CKA) reveals a Simpson's Paradox at the heart of this phenomenon: pooling across layers, CKA and transfer quality correlate \\emph{negatively} (depth confound), but controlling for layer depth, higher within-layer CKA significantly predicts better transfer ($p < 0.01$ on both architectures). The correctness direction itself occupies a near-universal low-dimensional subspace (cross-language angle $12.4^{\\circ}$ within each layer) that persists even as global representations specialize by language.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Pareto discovery.} We identify an architecture-dependent depth-transferability tradeoff across three architectures and 20 languages, with Pareto knee at 55--58\\% depth.\n\\item \\textbf{Decomposition analysis.} We decompose correctness into difficulty-shared and capability-specific components, showing that capability drives 88\\% of transfer degradation despite accounting for only 35\\% of variance.\n\\item \\textbf{CaCLR method.} A consistency-regularized calibration approach providing +3.5\\pp{} mean AUROC gain without target-language labels, with gains concentrated at deep layers.\n\\item \\textbf{CKA geometric explanation.} The Simpson's Paradox, subspace persistence ($12.4^{\\circ}$ within-layer, $38.7^{\\circ}$ cross-layer), and CKA cliff threshold ($\\sim$0.35) together explain when and why transfer succeeds.\n\\end{enumerate}\nAdditionally, we report that 28\\% of low-resource probing results are capacity artifacts (a methodological warning for the field), that Procrustes alignment with $\\sim$42 parallel pairs reaches 95\\% of full performance, and that Procrustes helps below a zero-shot AUROC threshold of $\\sim$0.52 but \\emph{hurts} above it.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Probe-based calibration.}\nLinear probes trained on internal representations to detect answer correctness were introduced by Miao et al.\\ \\cite{miao2026coral} (CORAL) and extended to confidence--correctness steering vectors \\cite{miao2026steering}. CCPS \\cite{ji2024llm} identifies ``truth-telling'' and ``confidence'' directions in representation space. Ji et al.\\ \\cite{ji2024llm} demonstrate that the correctness direction and verbalized confidence are nearly orthogonal. All of these operate exclusively in English.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al.\\ \\cite{xiao2025crosslingual} transfer knowledge-boundary probes across 8 languages, reporting that mean-shift alignment and Procrustes rotation improve transfer. Their target is binary answerability (input-level), not correctness (output-dependent accuracy), and they evaluate probing accuracy rather than calibration. Civelli et al.\\ \\cite{civelli2024crosslingual} show that IRT difficulty transfers well cross-lingually. We decompose correctness into difficulty-shared and capability-specific components, directly building on their finding.\n\n\\paragraph{Cross-lingual representation alignment.}\nStatic cross-lingual alignment methods such as MUSE \\cite{conneau2018word} and VecMap \\cite{artetxe2018robust} demonstrate that Procrustes rotation effectively aligns embedding spaces with minimal parallel data. Our linear projection applies this principle at the sentence-level correctness representation, and we characterize sample efficiency across resource tiers.\n\n\\paragraph{Representation similarity.}\nCentered kernel alignment (CKA; \\cite{kornblith2019similarity}) and SVCCA \\cite{raghu2017svcca} quantify representation similarity across models and layers. We use CKA to measure cross-lingual similarity at each layer, revealing a Simpson's Paradox when the depth confound is controlled.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\cite{bendavid2010theory} formalize transfer error via $\\mathcal{H}$-divergence. Zhao et al.\\ \\cite{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly relevant to understanding why CaCLR's MMD-based matching provides bounded rather than unbounded improvement.\n\n\\paragraph{Conformal prediction.}\nDistribution-free coverage guarantees \\cite{angelopoulos2023conformal} provide complementary calibration. Unlike our zero-label approach, conformal methods require per-language calibration data; the two are complementary.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Cross-Lingual Correctness Probing}\n\\label{sec:method:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract hidden-state representations at layer $l$ for each MCQA item in GlobalMMLU. An English logistic regression probe is trained:\n\\begin{equation}\np(\\text{correct} \\mid \\mathbf{h}_l^{\\text{en}}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l^{\\text{en}} + b_l)\n\\end{equation}\nwhere $\\mathbf{h}_l^{\\text{en}}$ is the pooled hidden state at layer $l$ for an English input. We evaluate this probe on target language representations $\\mathbf{h}_l^{\\text{tgt}}$ without any target-language labels (zero-shot transfer). We also evaluate under four additional conditions: (a)~mean-shift alignment, (b)~Procrustes linear projection with varying numbers of parallel pairs, (c)~few-shot fine-tuning with 25 or 100 target-language labels, and (d)~CaCLR (Section~\\ref{sec:method:caclr}).\n\nWe select logistic regression over nonlinear probes because linear probes better capture the language-agnostic linear structure of the correctness subspace. Empirically, MLPs gain +2\\pp{} English AUROC but lose 5.5\\pp{} in transfer (Section~\\ref{sec:probe_complexity}).\n\n\\paragraph{Mean-shift invariance.} Under StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits. Since AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically. Our data confirms this across all languages and layers.\n\n\\subsection{CaCLR: Calibration via Cross-Lingual Regularization}\n\\label{sec:method:caclr}\n\nCaCLR optimizes a joint loss over English labels and cross-lingual distributional consistency:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English correctness labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is a soft-binned ECE loss, and $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) between English and target-language probe logits:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2_k\\big(\\{f(\\mathbf{h}_l^{\\text{en},i})\\}_{i=1}^n, \\{f(\\mathbf{h}_l^{\\text{tgt},i})\\}_{i=1}^n\\big)\n\\end{equation}\nwhere $f(\\cdot) = \\mathbf{w}^\\top(\\cdot) + b$ denotes the probe logit (1-D for linear probes), and $k$ is a Gaussian RBF kernel with bandwidth set by the median heuristic. The parallel activations come from GlobalMMLU test split (70/30 partition for train/eval); no target-language \\emph{labels} are used. We optimize with Adam ($\\text{lr}=10^{-3}$, linear warmup 10\\%), batch size 256, 50 epochs with early stopping (patience 10, monitoring validation AUROC). The probe is initialized from the standard logistic regression solution.\n\nCaCLR operates on 1-D logits---a design constraint of the linear probe. MMD in 1-D effectively matches mean and variance of the logit distributions across languages, equivalent to nudging the probe direction toward the universal correctness subspace revealed by our CKA analysis (Section~\\ref{sec:cka}). However, it cannot perform full rotational alignment, which limits its ceiling compared to explicit Procrustes rotation.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:method:decomposition}\n\nFollowing Civelli et al.\\ \\cite{civelli2024crosslingual}, we train an IRT difficulty probe (Ridge regression) on item difficulty estimates, then project out the difficulty direction from the hidden states and retrain correctness probes on the residual representations. This decomposes correctness variance into:\n\\begin{itemize}\n\\item \\textbf{Difficulty-shared}: language-agnostic item difficulty information (hard items are hard everywhere).\n\\item \\textbf{Capability-specific}: language-dependent competence that varies across languages and depths.\n\\end{itemize}\nA random-direction control confirms that the decomposition captures genuine structure rather than arbitrary dimensionality reduction.\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:method:cka}\n\nWe compute linear CKA between English and each target language at every probed layer. Three analyses probe the geometry:\n\\begin{enumerate}\n\\item \\textbf{Same-layer cross-language correlation}: at each layer, Spearman correlation between CKA$_l(\\text{en}, \\text{tgt})$ and zero-shot AUROC$_l(\\text{tgt})$ across $n=20$ languages.\n\\item \\textbf{Partial Spearman correlation}: controlling for normalized depth, testing whether CKA predicts transfer beyond the depth confound.\n\\item \\textbf{Subspace angle analysis}: measuring the angular deviation of the correctness direction $\\mathbf{w}_l$ across languages within the same layer and across layers.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\subsection{Models}\n\nWe evaluate three architectures spanning MoE and dense designs:\n\n\\begin{table}[h]\n\\centering\n\\caption{Model specifications and summary results across 20 languages.}\n\\label{tab:three_arch}\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nModel & Type & Layers & EN Best & ZS Mean & Pareto $\\rho$ & Simpson $\\rho_{\\text{partial}}$ & CaCLR $\\Delta$\\pp \\\\\n\\midrule\nQwen3-235B & MoE & 94 & 0.81 & 0.72 & $-0.91$ & $+0.48$ & $+3.7$ \\\\\nLlama~4 Scout & MoE & 48 & 0.79 & 0.70 & $-0.78$ & $+0.41$ & $+3.3$ \\\\\nGemma~4 31B & Dense & 60 & 0.80 & 0.71 & $-0.85$ & $+0.44$ & $+3.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3-235B-A22B is a 94-layer MoE model ($\\sim$22B active parameters) run under GPTQ-Int4 quantization. Llama~4 Scout is a 48-layer MoE model (17B$\\times$16 experts, top-2 routing) under W4A16. Gemma~4 31B is a 60-layer dense model run in FP16. We probe every 4th layer (24 layers for Qwen3, 12 for Llama~4, 15 for Gemma~4). Quantization validation (Section~\\ref{sec:quant}) confirms negligible distortion (mean $\\leq 0.5\\pp$, rank correlation $\\geq 0.994$).\n\n\\subsection{Languages and Benchmarks}\n\nOur core evaluation covers 20 typologically diverse languages grouped by resource tier: HIGH (zh, es, fr, de, ja, nl, pt, it), MID (ar, hi, ko, tr, ru, vi, th), and LOW (sw, bn, yo, ig, te). Extended evaluation (Section~\\ref{sec:extended}) expands to 50 languages including Austronesian, Dravidian, Uralic, Kartvelian, and additional Niger-Congo families. Primary benchmark is GlobalMMLU; cross-benchmark generalization is assessed on Belebele and MMLU-ProX (Section~\\ref{sec:cross_benchmark}).\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B.}\nTable~\\ref{tab:qwen_pareto} shows the layer-wise profile. The English-optimal layer (L72, 77\\% depth, AUROC 0.81) and zero-shot-optimal layer (L52, 55\\% depth, AUROC 0.72) are separated by 20 layers. The Pareto frontier spans layers L40--L56 with a knee gap of 4.2\\pp. The global Spearman correlation between depth and zero-shot AUROC is $\\rho = -0.91$ ($p < 0.001$), and 15 of 20 per-language correlations are significantly negative ($p < 0.05$). The two languages failing the 0.60 AUROC threshold are Yoruba (0.57) and Telugu (0.58), both extremely low-resource in pretraining data.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen3-235B Pareto frontier. Selected layers from 24 probed (every 4th of 94). $\\checkmark$ marks Pareto-optimal layers.}\n\\label{tab:qwen_pareto}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nLayer & Depth\\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp & Pareto \\\\\n\\midrule\n4  & 4  & 0.580 & 0.572 & 0.8  & \\\\\n12 & 13 & 0.645 & 0.632 & 1.3  & \\\\\n20 & 21 & 0.710 & 0.695 & 1.5  & \\\\\n28 & 30 & 0.752 & 0.733 & 1.9  & \\\\\n36 & 38 & 0.778 & 0.752 & 2.6  & \\\\\n40 & 43 & 0.788 & 0.748 & 4.0  & $\\checkmark$ \\\\\n44 & 47 & 0.796 & 0.740 & 5.6  & $\\checkmark$ \\\\\n48 & 51 & 0.802 & 0.732 & 7.0  & $\\checkmark$ \\\\\n52 & 55 & 0.806 & 0.720 & 8.6  & $\\checkmark$ \\\\\n56 & 60 & 0.808 & 0.706 & 10.2 & $\\checkmark$ \\\\\n60 & 64 & 0.810 & 0.690 & 12.0 & \\\\\n68 & 72 & 0.810 & 0.661 & 14.9 & \\\\\n72 & 77 & 0.810 & 0.638 & 17.2 & \\\\\n80 & 85 & 0.805 & 0.601 & 20.4 & \\\\\n88 & 94 & 0.792 & 0.558 & 23.4 & \\\\\n92 & 98 & 0.778 & 0.531 & 24.7 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama~4 Scout.}\nTable~\\ref{tab:llama_pareto} shows a qualitatively different pattern. While the global $\\rho = -0.78$ is significant ($p = 0.003$), only 6 of 20 per-language correlations reach significance. Three languages (ar, hi, ko) exhibit \\emph{positive} $\\rho$---deeper layers improve transfer. The Pareto frontier is narrower (L20--L28) with a smaller knee gap of 3.4\\pp. The median per-language $\\rho$ is $-0.28$, compared to $-0.64$ for Qwen3.\n\n\\begin{table}[t]\n\\centering\n\\caption{Llama~4 Scout Pareto frontier.}\n\\label{tab:llama_pareto}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nLayer & Depth\\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp & Pareto \\\\\n\\midrule\n4  & 8   & 0.560 & 0.552 & 0.8  & \\\\\n8  & 17  & 0.635 & 0.625 & 1.0  & \\\\\n12 & 25  & 0.695 & 0.682 & 1.3  & \\\\\n16 & 33  & 0.735 & 0.718 & 1.7  & \\\\\n20 & 42  & 0.758 & 0.724 & 3.4  & $\\checkmark$ \\\\\n24 & 50  & 0.772 & 0.714 & 5.8  & $\\checkmark$ \\\\\n28 & 58  & 0.782 & 0.700 & 8.2  & $\\checkmark$ \\\\\n32 & 67  & 0.789 & 0.681 & 10.8 & \\\\\n36 & 75  & 0.790 & 0.655 & 13.5 & \\\\\n40 & 83  & 0.785 & 0.625 & 16.0 & \\\\\n44 & 92  & 0.772 & 0.589 & 18.3 & \\\\\n48 & 100 & 0.748 & 0.548 & 20.0 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture comparison.}\nTable~\\ref{tab:arch_compare} quantifies the architecture-dependent tradeoff. The 2.3$\\times$ difference in median per-language effect size ($-0.64$ vs.\\ $-0.28$) is the core observation: on Qwen3, practitioners must explicitly choose between English accuracy and transfer quality; on Llama~4, some languages can ``free-ride'' deep-layer improvements. The best-transfer depth converges to 55--58\\% across both architectures, suggesting a universal mid-depth transfer zone whose \\emph{steepness} is architecture-specific.\n\n\\begin{table}[t]\n\\centering\n\\caption{Architecture-dependent Pareto comparison.}\n\\label{tab:arch_compare}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3-235B & Llama~4 Scout & Interpretation \\\\\n\\midrule\nGlobal $\\rho$ & $-0.91$ & $-0.78$ & Both significant, Qwen stronger \\\\\nPer-lang sig.\\ count & 15/20 & 6/20 & Qwen consistent, Llama mixed \\\\\nMedian per-lang $\\rho$ & $-0.64$ & $-0.28$ & 2.3$\\times$ effect size difference \\\\\nPositive-$\\rho$ langs & 0 & 3 & Llama: ar/hi/ko reversed \\\\\nBest transfer depth\\% & 55 & 58 & Comparable location \\\\\nEN--ZS gap at knee\\pp & 4.2 & 3.4 & Comparable magnitude \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Transfer conditions.}\nTable~\\ref{tab:transfer_conditions} compares five transfer methods at the best-transfer layer. Mean-shift yields $\\Delta\\text{AUROC} = 0.0$ (as proven by the rank-invariance argument). Linear projection (+1.9\\pp{} combined) and few-shot-100 (+1.7\\pp) provide moderate gains. CaCLR (+3.5\\pp) provides the largest zero-label improvement.\n\n\\begin{table}[t]\n\\centering\n\\caption{Transfer conditions at best-transfer layer (both models averaged).}\n\\label{tab:transfer_conditions}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Qwen3 & Llama~4 & Combined & Requires \\\\\n\\midrule\nZero-shot     & 0.720 & 0.700 & 0.710 & --- \\\\\nMean-shift    & 0.720 & 0.700 & 0.710 & --- \\\\\nLinProj (200) & 0.740 & 0.718 & 0.729 & 200 parallel pairs \\\\\nFew-shot (25) & 0.708 & 0.692 & 0.700 & 25 target labels \\\\\nFew-shot (100)& 0.735 & 0.718 & 0.727 & 100 target labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Simpson's Paradox in CKA--Transfer Relationship}\n\\label{sec:cka}\n%------------------------------------------------------------------------------\n\nThe central geometric finding is a Simpson's Paradox. When CKA values and zero-shot AUROC are pooled across all layers and languages, the Spearman correlation is \\emph{negative}: $\\rho = -0.36$ ($p < 0.001$) for Qwen3 and $\\rho = -0.41$ ($p < 0.001$) for Llama~4. This arises because shallow layers have high CKA but weak probes (low AUROC), while deep layers have low CKA but strong probes (high AUROC before transfer degradation kicks in).\n\nControlling for normalized depth reverses the sign. The partial Spearman correlation is $\\rho = +0.48$ ($p = 0.002$, 95\\% bootstrap CI $[+0.31, +0.62]$) for Qwen3 and $\\rho = +0.41$ ($p = 0.008$, CI $[+0.22, +0.57]$) for Llama~4 (Table~\\ref{tab:simpson}). Within each layer, higher cross-lingual CKA genuinely predicts better transfer. This finding replicates on Gemma~4 31B ($\\rho_{\\text{partial}} = +0.44$, $p = 0.004$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation between CKA and zero-shot transfer AUROC.}\n\\label{tab:simpson}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Analysis & $\\rho$ & $p$ & Bootstrap 95\\% CI & Sign \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-235B}\n & Raw pooled  & $-0.36$ & $<$0.001 & $[-0.44, -0.27]$ & negative \\\\\n & Partial (depth) & $+0.48$ & 0.002 & $[+0.31, +0.62]$ & positive \\\\\n\\midrule\n\\multirow{2}{*}{Llama~4 Scout}\n & Raw pooled  & $-0.41$ & $<$0.001 & $[-0.50, -0.31]$ & negative \\\\\n & Partial (depth) & $+0.41$ & 0.008 & $[+0.22, +0.57]$ & positive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-layer correlations.}\nTable~\\ref{tab:per_layer_cka} shows that on Qwen3, 18 of 24 per-layer correlations are positive and 6 reach significance at $p < 0.05$ ($n = 20$ languages per layer). The signal is strongest at intermediate depths (13--38\\%) where CKA variance across languages is largest, and weakens at deep layers where CKA collapses toward a floor ($\\sim$0.22--0.28).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-layer CKA--transfer correlation on Qwen3-235B (selected layers, $n=20$ languages per layer).}\n\\label{tab:per_layer_cka}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nLayer & Depth\\% & Mean CKA$_{20}$ & Spearman $\\rho$ & $p$ \\\\\n\\midrule\n12 & 13 & 0.78 & 0.52 & 0.019 \\\\\n20 & 21 & 0.81 & 0.48 & 0.032 \\\\\n28 & 30 & 0.76 & 0.55 & 0.012 \\\\\n36 & 38 & 0.68 & 0.51 & 0.022 \\\\\n44 & 47 & 0.56 & 0.46 & 0.041 \\\\\n52 & 55 & 0.45 & 0.43 & 0.058 \\\\\n60 & 64 & 0.38 & 0.38 & 0.098 \\\\\n68 & 72 & 0.30 & 0.33 & 0.155 \\\\\n72 & 77 & 0.28 & 0.28 & 0.231 \\\\\n80 & 85 & 0.22 & 0.21 & 0.372 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace} reveals why within-layer CKA predicts transfer: the correctness direction is near-universal within each layer (mean cross-language angle $12.4^{\\circ} \\pm 5.8^{\\circ}$) but rotates substantially across layers ($38.7^{\\circ} \\pm 11.2^{\\circ}$). The random baseline ($87.3^{\\circ} \\pm 2.1^{\\circ}$, near-orthogonal) confirms these angles reflect genuine structure. Global CKA decline reflects divergence in \\emph{non-correctness} dimensions; the correctness subspace itself persists as a low-dimensional feature. This explains why raw CKA (mixing correctness and non-correctness dimensions) misleads while within-layer CKA (where depth is held constant) captures the relevant alignment.\n\n\\begin{table}[t]\n\\centering\n\\caption{Subspace angle analysis of the correctness direction.}\n\\label{tab:subspace}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & Mean Angle & Std & Interpretation \\\\\n\\midrule\nWithin-layer, cross-language & $12.4^{\\circ}$ & $5.8^{\\circ}$ & Near-universal direction \\\\\nCross-layer, same-language   & $38.7^{\\circ}$ & $11.2^{\\circ}$ & Significant rotation \\\\\nRandom baseline (shuffled)   & $87.3^{\\circ}$ & $2.1^{\\circ}$ & Near-orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CKA cliff and transfer collapse.}\nCKA drops sharply at 55\\% depth on Qwen3 and 50\\% on Llama~4. A collapse threshold of CKA $\\approx 0.35$ separates two regimes: language-layer pairs above this threshold achieve mean zero-shot AUROC of 0.72, while those below achieve only 0.58. Qwen3's steeper cliff (peak 0.82 $\\to$ floor 0.28 at EN-optimal layer) drives more languages below threshold at deep layers, producing the stronger Pareto tradeoff. Llama~4's shallower cliff (0.84 $\\to$ 0.35) allows ar/hi/ko to remain above threshold throughout, explaining their anomalous positive depth--transfer relationship.\n\n%------------------------------------------------------------------------------\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n%------------------------------------------------------------------------------\n\nThe IRT difficulty probe achieves $R^2 = 0.68$ (range 0.55--0.78 across layers and models). Table~\\ref{tab:decomposition} shows the decomposition: the difficulty-shared component accounts for 65\\% of correctness variance but only 12\\% of transfer degradation. The capability-specific residual accounts for 35\\% of variance but drives 88\\% of degradation. Projecting out difficulty reduces English AUROC by only 4.5\\pp{} (from 0.81 to $\\sim$0.765) while reducing the zero-shot transfer gap by 0.8\\pp---confirming that difficulty is nearly perfectly transferable while capability is the bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty--capability decomposition of correctness transfer. Combined across both architectures and 10 languages $\\times$ 8 layers.}\n\\label{tab:decomposition}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Var.\\% & Transfer AUROC & Transfer Drop\\pp & Degradation Share \\\\\n\\midrule\nFull correctness    & 100 & 0.710 & 9.0  & 100\\% \\\\\nDifficulty-shared   & 65  & 0.698 & 1.1  & 12\\% \\\\\nCapability-specific & 35  & 0.615 & 12.8 & 88\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cap_by_depth} shows that capability-driven transfer degradation accelerates with depth. At 20--30\\% depth, the difficulty-to-capability degradation ratio is 3$\\times$; at 75--90\\% it reaches 5.7$\\times$. This matches the CKA cliff: deep layers accumulate more capability-specific (language-dependent) information, and the CKA decline reflects exactly this divergence. The decomposition is prescriptive: it correctly predicts which alignment strategy is needed (zero-shot for difficulty-dominant vs.\\ CaCLR for capability-dominant combinations) with 78\\% accuracy.\n\nA random-direction control ($-1.2\\pp$ when projecting out a random direction) confirms the decomposition captures genuine structure.\n\n\\begin{table}[t]\n\\centering\n\\caption{Capability-specific transfer degradation by depth.}\n\\label{tab:cap_by_depth}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth Band & Difficulty Drop\\pp & Capability Drop\\pp & Ratio \\\\\n\\midrule\n20--30\\% & 0.2 & 0.6 & 3$\\times$ \\\\\n40--50\\% & 0.6 & 2.8 & 4.7$\\times$ \\\\\n60--70\\% & 1.0 & 5.6 & 5.6$\\times$ \\\\\n75--90\\% & 1.5 & 8.5 & 5.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{CaCLR Evaluation}\n\\label{sec:caclr}\n%------------------------------------------------------------------------------\n\n\\paragraph{Consistency loss effect.}\nTable~\\ref{tab:beta_sweep} shows the $\\beta$ sweep across three orders of magnitude. The optimal $\\beta = 0.05$ achieves +3.5\\pp{} AUROC and $-2.4\\pp$ ECE improvement. Below $\\beta = 0.001$, gradient noise exceeds signal; above $\\beta = 1.0$, MMD dominates BCE and probe accuracy degrades. The optimal $\\alpha = 0.1$ provides $-3.2\\pp$ ECE improvement.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\beta$ sweep for the consistency loss ($\\alpha = 0.1$ fixed). Combined across both architectures at best-transfer layer.}\n\\label{tab:beta_sweep}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n$\\beta$ & $\\Delta$AUROC\\pp{} vs ZS & $\\Delta$ECE\\pp & Note \\\\\n\\midrule\n0.0   & 0.0   & 0.0    & Baseline (BCE only) \\\\\n0.001 & +0.5  & $-0.3$ & Marginal improvement \\\\\n0.01  & +1.8  & $-1.1$ & Clear positive signal \\\\\n0.05  & +3.5  & $-2.4$ & Optimal tradeoff \\\\\n0.1   & +3.2  & $-2.0$ & Slight over-regularization \\\\\n1.0   & +0.8  & $-0.5$ & MMD dominates \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Component ablation.}\nBCE-only achieves AUROC 0.710; adding SB-ECE (+0.012 to 0.722) primarily improves calibration. Adding consistency loss alone (+0.028 to 0.738) is the primary contributor. The full CaCLR (+0.035 to 0.745) shows a synergy between the two regularizers.\n\n\\paragraph{Comparison with all methods.}\nTable~\\ref{tab:caclr_compare} places CaCLR in context. CaCLR achieves the highest AUROC (0.745) and second-lowest ECE (0.082, after few-shot-100 at 0.088) among all methods, without requiring any target-language labels. It surpasses linear projection by 1.6\\pp{} AUROC because end-to-end gradient optimization can exploit training dynamics beyond post-hoc geometric correction. However, the gap is modest---consistent with the 1-D MMD limitation: it matches scalar logit distributions but cannot perform full subspace rotation.\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR vs.\\ all transfer methods (both models averaged at best-transfer layer).}\n\\label{tab:caclr_compare}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nMethod & AUROC & ECE & Labels Required & Key Resource \\\\\n\\midrule\nZero-shot       & 0.710 & 0.118 & None & --- \\\\\nMean-shift      & 0.710 & 0.118 & None & --- \\\\\nLinProj (50)    & 0.725 & 0.098 & 50 parallel & Procrustes \\\\\nLinProj (200)   & 0.729 & 0.095 & 200 parallel & Procrustes \\\\\nFew-shot (25)   & 0.700 & 0.102 & 25 labeled & Target labels \\\\\nFew-shot (100)  & 0.727 & 0.088 & 100 labeled & Target labels \\\\\n\\textbf{CaCLR}  & \\textbf{0.745} & \\textbf{0.082} & None & Parallel activations \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth profile.}\nTable~\\ref{tab:caclr_depth} shows CaCLR's improvement on Qwen3 as a function of depth. The gain grows from +1.2\\pp{} at 30\\% depth to +4.8--5.0\\pp{} at 64--77\\% depth, then moderates to +4.0\\pp{} at 85\\%. This pattern aligns with the decomposition analysis: deep layers have larger capability-specific components, providing more signal for the consistency loss to exploit. CaCLR improves in 88\\% of model-language pairs (35/40); the 5 non-improving pairs are high-resource languages on shallow layers where zero-shot transfer is already near ceiling.\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR depth profile on Qwen3-235B.}\n\\label{tab:caclr_depth}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\nDepth\\% & ZS AUROC & CaCLR AUROC & $\\Delta$\\pp \\\\\n\\midrule\n30 & 0.733 & 0.745 & +1.2 \\\\\n43 & 0.748 & 0.766 & +1.8 \\\\\n55 & 0.720 & 0.752 & +3.2 \\\\\n64 & 0.690 & 0.738 & +4.8 \\\\\n77 & 0.638 & 0.688 & +5.0 \\\\\n85 & 0.601 & 0.641 & +4.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen3 specifically, CaCLR achieves mean AUROC 0.757 (+3.7\\pp{} vs.\\ ZS) with ECE 0.078. On Llama~4, mean AUROC 0.733 (+3.3\\pp) with ECE 0.085.\n\n%------------------------------------------------------------------------------\n\\subsection{Linear Projection Sensitivity}\n\\label{sec:linproj}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:proj_efficiency} characterizes Procrustes alignment sample efficiency. Performance reaches 95\\% of the 200-pair baseline at $\\sim$42 parallel pairs overall, with resource-tier stratification: HIGH languages saturate at 22 pairs (simple rotation, low effective rank), MID at 38, and LOW at 48 (complex rotation, more parameters to estimate).\n\n\\begin{table}[t]\n\\centering\n\\caption{Procrustes linear projection: sample efficiency.}\n\\label{tab:proj_efficiency}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$n$ Pairs & \\% of 200-Pair & Mean AUROC & Note \\\\\n\\midrule\n10  & 72\\% & 0.724 & High variance \\\\\n20  & 86\\% & 0.728 & Dominant rotation captured \\\\\n30  & 92\\% & 0.731 & Near plateau for HIGH \\\\\n50  & 97\\% & 0.734 & Near plateau for all tiers \\\\\n100 & 99\\% & 0.737 & Marginal returns \\\\\n200 & 100\\% & 0.729 & Reference baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Procrustes effect reversal.}\nTable~\\ref{tab:procrustes_reversal} reveals a striking non-monotonicity. When zero-shot AUROC is below $\\sim$0.52, Procrustes alignment helps substantially (+5.2\\pp{} for AUROC $< 0.45$; +2.4\\pp{} for $0.45$--$0.52$). But when zero-shot AUROC exceeds 0.60, Procrustes \\emph{hurts} ($-1.2\\pp$): the correctness directions are already well-aligned, and Procrustes introduces estimation noise. The threshold of 0.52 corresponds to CKA $\\approx 0.35$ (the transfer collapse threshold from Section~\\ref{sec:cka}), providing a geometric explanation for when alignment is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Procrustes effect reversal by zero-shot AUROC range.}\n\\label{tab:procrustes_reversal}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\nZS AUROC Range & $n$ Pairs & Mean $\\Delta$\\pp & Direction \\\\\n\\midrule\n$<$0.45      & 42  & +5.2  & Strong positive \\\\\n0.45--0.52   & 68  & +2.4  & Moderate positive \\\\\n0.52--0.60   & 95  & +0.3  & Transition zone \\\\\n0.60--0.70   & 88  & $-1.2$ & Negative \\\\\n$>$0.70      & 47  & $-0.8$ & Slight negative \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n%------------------------------------------------------------------------------\n\nFollowing Hewitt \\& Liang \\cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC). Table~\\ref{tab:control_selectivity} shows selectivity by resource tier and depth. Control probes achieve mean AUROC 0.495 ($\\pm 0.008$), confirming near-chance performance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selectivity by resource tier and depth band.}\n\\label{tab:control_selectivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth Band & HIGH & MID & LOW \\\\\n\\midrule\n0--30\\%   & 0.04 & 0.03 & 0.01 \\\\\n30--60\\%  & 0.18 & 0.14 & 0.06 \\\\\n60--80\\%  & 0.28 & 0.22 & 0.10 \\\\\n80--100\\% & 0.25 & 0.20 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:artifact_rates} presents artifact rates---the fraction of language-layer combinations where selectivity falls below a meaningful threshold. The finding is striking: \\textbf{27\\% of low-resource probing results are capacity artifacts}, concentrated at 60--100\\% depth. Mid- and high-resource artifact rates are low (5\\% and 3\\%). The most affected languages are yo, ig, te, and sw---all extremely low-resource in model pretraining.\n\n\\begin{table}[t]\n\\centering\n\\caption{Artifact rates by resource tier.}\n\\label{tab:artifact_rates}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Combinations & Artifact Count & Rate \\\\\n\\midrule\nHIGH  & 384 & 12 & 3\\% \\\\\nMID   & 336 & 17 & 5\\% \\\\\nLOW   & 240 & 65 & 27\\% \\\\\n\\midrule\nTotal & 960 & 94 & 10\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is, to our knowledge, the first application of probing control tasks to a cross-lingual transfer setting. The 27\\% low-resource artifact rate implies that cross-lingual probing studies without selectivity checks---including Xiao et al.\\ \\cite{xiao2025crosslingual}---may overestimate low-resource transfer quality. Our core Pareto and CKA analyses are unaffected because they are driven primarily by mid- and high-resource patterns, where artifact rates are $\\leq$5\\%.\n\n%------------------------------------------------------------------------------\n\\subsection{Cross-Lingual Correctness--Confidence Orthogonality}\n\\label{sec:orthogonality}\n%------------------------------------------------------------------------------\n\nExtending the English-only finding of Miao \\& Ungar \\cite{miao2026steering} (cosine $<$ 0.04 at 7--8B scale), we measure the cosine similarity between the verbalized confidence direction and the correctness direction across 20 languages and both architectures. Table~\\ref{tab:ortho} shows the results. The overall mean cosine is 0.05 (range 0.02--0.09); all 40 model-language pairs fall below 0.10. This confirms that output-based calibration methods are structurally limited across languages---not just in English.\n\nA resource-tier gradient emerges: HIGH 0.038, MID 0.052, LOW 0.072 ($r = -0.66$ between resource level and cosine). Better multilingual training produces cleaner separation between the correctness and confidence directions, though the effect size is small (range 0.034).\n\n\\begin{table}[t]\n\\centering\n\\caption{Correctness--confidence cosine similarity by resource tier.}\n\\label{tab:ortho}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Langs & Qwen3 Mean & Llama~4 Mean & Combined \\\\\n\\midrule\nHIGH & 8 & 0.035 & 0.041 & 0.038 \\\\\nMID  & 7 & 0.048 & 0.056 & 0.052 \\\\\nLOW  & 5 & 0.066 & 0.078 & 0.072 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Additional Analysis}\n\\label{sec:additional}\n%==============================================================================\n\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\nTable~\\ref{tab:probe_complexity} compares logistic regression and 2-layer MLP probes on Qwen3 at the English-optimal layer. The MLP gains +2\\pp{} English AUROC (0.83 vs.\\ 0.81) but suffers 5.5\\pp{} worse transfer (14.5\\pp{} vs.\\ 9.0\\pp{} zero-shot drop). The advantage of linear probes grows with depth: +2\\pp{} at shallow layers, +8.2\\pp{} at 80\\% depth. This validates the linear probe choice and supports the geometric interpretation: correctness transfer relies on a linear, language-agnostic subspace that MLPs overfit by exploiting language-specific nonlinear features.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe complexity comparison (Qwen3, EN-optimal layer).}\n\\label{tab:probe_complexity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nProbe Type & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp \\\\\n\\midrule\nLogistic regression   & 0.81 & 0.720 & 9.0 \\\\\nMLP (2-layer, $h$=128) & 0.83 & 0.685 & 14.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_benchmark}\n\nTable~\\ref{tab:cross_bench} evaluates CaCLR on three benchmarks. The improvement is consistent: +3.5\\pp{} on GlobalMMLU, +3.3\\pp{} on Belebele (reading comprehension), and +3.5\\pp{} on MMLU-ProX (harder factual). Cross-benchmark coefficient of variation is 0.04, confirming that CaCLR addresses a fundamental representation alignment issue rather than overfitting to a specific benchmark's distribution.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark CaCLR generalization (both models, 20 languages).}\n\\label{tab:cross_bench}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & ZS Mean$_{20}$ & CaCLR Mean$_{20}$ & $\\Delta$\\pp \\\\\n\\midrule\nGlobalMMLU & 0.710 & 0.745 & +3.5 \\\\\nBelebele   & 0.695 & 0.728 & +3.3 \\\\\nMMLU-ProX  & 0.680 & 0.715 & +3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\nTable~\\ref{tab:quant} validates that quantization introduces negligible distortion. W4A16 on Llama~4 preserves 16-bit activations, yielding mean AUROC difference of 0.3\\pp{} (max 0.8\\pp) and rank correlation 0.996. GPTQ-Int4 on Qwen3 is more aggressive but still achieves mean difference 0.5\\pp{} (max 1.1\\pp) and rank correlation 0.994. The Pareto frontier ordering is fully preserved under both quantization schemes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Quantization validation at 5 representative layers per model.}\n\\label{tab:quant}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nModel & Layer & FP16 AUROC & Quant AUROC & $\\Delta$\\pp \\\\\n\\midrule\nLlama~4 & L8  & 0.637 & 0.634 & 0.3 \\\\\nLlama~4 & L16 & 0.737 & 0.735 & 0.2 \\\\\nLlama~4 & L28 & 0.784 & 0.781 & 0.3 \\\\\nLlama~4 & L36 & 0.792 & 0.789 & 0.3 \\\\\nLlama~4 & L44 & 0.774 & 0.770 & 0.4 \\\\\n\\midrule\nQwen3 & L20 & 0.712 & 0.708 & 0.4 \\\\\nQwen3 & L36 & 0.780 & 0.775 & 0.5 \\\\\nQwen3 & L52 & 0.808 & 0.803 & 0.5 \\\\\nQwen3 & L68 & 0.812 & 0.806 & 0.6 \\\\\nQwen3 & L80 & 0.807 & 0.800 & 0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Third Architecture: Gemma~4 31B Dense}\n\\label{sec:gemma}\n\nGemma~4 31B Dense serves as a dense-architecture contrast to the two MoE models. The English-optimal layer is L45 (AUROC 0.80), and the best-transfer layer is L36 (zero-shot mean 0.71). The global Spearman $\\rho = -0.85$ falls between Qwen3 ($-0.91$) and Llama~4 ($-0.78$). Simpson's Paradox replicates: $\\rho_{\\text{partial}} = +0.44$ ($p = 0.004$). CaCLR provides +3.0\\pp. These results (incorporated into Table~\\ref{tab:three_arch}) confirm that the depth-transferability tradeoff and Simpson's Paradox are properties of transformer depth, not of MoE routing or any single architecture family.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding from 20 to 50 languages (Table~\\ref{tab:extended}), we confirm all findings at scale. Zero-shot transfer achieves AUROC $\\geq 0.60$ in 42/50 languages (84\\% pass rate). CaCLR improves 47/50 languages. The resource-tier gradient is smooth and extends to a VERY\\_LOW tier (4 languages, mean ZS 0.53, CaCLR +5.0\\pp). The Pareto frontier structure, Simpson's Paradox, and CaCLR benefit pattern all hold across the expanded language set, with no language family showing anomalous behavior. CaCLR's benefit is inversely correlated with resource level, providing the largest gains for the languages that need it most.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended 50-language coverage by resource tier.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Langs & ZS Mean & CaCLR Mean & $\\Delta$\\pp \\\\\n\\midrule\nHIGH      & 10 & 0.75 & 0.78 & +2.8 \\\\\nMID       & 24 & 0.71 & 0.74 & +3.5 \\\\\nLOW       & 12 & 0.62 & 0.66 & +4.2 \\\\\nVERY\\_LOW & 4  & 0.53 & 0.58 & +5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{The causal chain.}\nOur four claims form an explanatory sequence. The Pareto frontier (Claim~1) establishes the empirical phenomenon: deeper probes are better for English but worse for transfer, with architecture-dependent severity. The decomposition (Claim~2) reveals the mechanism: capability-specific representations drive 88\\% of degradation and grow with depth. CaCLR (Claim~3) tests whether distributional matching can shift this frontier, and succeeds with +3.5\\pp{} mean improvement concentrated at deep layers where capability-specific content is largest. The CKA analysis (Claim~4) provides geometric grounding: the Simpson's Paradox shows that within-layer CKA genuinely predicts transfer, the subspace persistence explains why zero-shot transfer works at all, and the CKA cliff threshold connects to both the Pareto steepness and the Procrustes reversal point.\n\n\\paragraph{Practical implications.}\nFor practitioners deploying multilingual calibration probes: (1)~select layers at 55--60\\% depth rather than the English-optimal layer; (2)~check zero-shot AUROC before applying alignment---Procrustes helps below 0.52 but hurts above 0.60; (3)~if parallel data is available, $\\sim$42 pairs suffice for 95\\% of optimal performance; (4)~apply selectivity controls for low-resource languages to avoid capacity artifacts.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA evaluation; generalization to open-ended generation requires further investigation. CaCLR operates on 1-D logits due to the linear probe constraint, limiting its alignment capacity. The architecture comparison involves $n=3$ architectures that differ simultaneously in type, scale, and training data; we cannot causally attribute tradeoff differences to specific architectural features. The 27\\% low-resource artifact rate, while a warning for the field, means our low-resource conclusions should be interpreted with caution.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures and up to 50 languages. The depth-transferability Pareto frontier is real, architecture-dependent, and geometrically grounded: a Simpson's Paradox in the CKA--transfer relationship reveals that within-layer cross-lingual similarity genuinely predicts transfer quality once the depth confound is controlled. The correctness direction occupies a near-universal subspace ($12.4^{\\circ}$ within-layer angle) that persists even as global representations diverge. CaCLR provides a consistent +3.5\\pp{} improvement without target-language labels, with gains largest at deep layers where capability-specific content dominates. These findings establish that probe-based calibration is viable beyond English and provide geometric understanding of when and why it works.\n\n%==============================================================================\n% References\n%==============================================================================\n\\begin{thebibliography}{30}\n\n\\bibitem{joshi2024llm}\nJoshi, N., et al.\n\\newblock Are LLMs Calibrated? A Comprehensive Survey of Calibration in Large Language Models.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem{zhou2024lace}\nZhou, T., et al.\n\\newblock LACE: Layer-Adaptive Calibration Ensemble for Multilingual LLMs.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{miao2026coral}\nMiao, Y., et al.\n\\newblock CORAL: Cross-Task Correctness Probes for LLM Calibration.\n\\newblock In \\emph{Proc.\\ NAACL}, 2026.\n\n\\bibitem{miao2026steering}\nMiao, Y. and Ungar, L.\n\\newblock Steering Vectors for Confidence-Correctness Alignment.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem{ji2024llm}\nJi, Z., et al.\n\\newblock LLM Internal States Reveal Hallucination Risk.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{xiao2025crosslingual}\nXiao, Y., et al.\n\\newblock Cross-Lingual Transfer of Knowledge Boundary Probes.\n\\newblock In \\emph{Proc.\\ ACL}, 2025.\n\n\\bibitem{civelli2024crosslingual}\nCivelli, A., et al.\n\\newblock Cross-Lingual Difficulty Probes.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem{conneau2018word}\nConneau, A., et al.\n\\newblock Word Translation Without Parallel Data.\n\\newblock In \\emph{Proc.\\ ICLR}, 2018.\n\n\\bibitem{artetxe2018robust}\nArtetxe, M., et al.\n\\newblock A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings.\n\\newblock In \\emph{Proc.\\ ACL}, 2018.\n\n\\bibitem{kornblith2019similarity}\nKornblith, S., et al.\n\\newblock Similarity of Neural Network Representations Revisited.\n\\newblock In \\emph{Proc.\\ ICML}, 2019.\n\n\\bibitem{raghu2017svcca}\nRaghu, M., et al.\n\\newblock SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2017.\n\n\\bibitem{bendavid2010theory}\nBen-David, S., et al.\n\\newblock A Theory of Learning from Different Domains.\n\\newblock \\emph{Machine Learning}, 79(1-2):151--175, 2010.\n\n\\bibitem{zhao2019learning}\nZhao, H., et al.\n\\newblock On Learning Invariant Representations for Domain Adaptation.\n\\newblock In \\emph{Proc.\\ ICML}, 2019.\n\n\\bibitem{angelopoulos2023conformal}\nAngelopoulos, A. and Bates, S.\n\\newblock Conformal Prediction: A Gentle Introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 2023.\n\n\\bibitem{hewitt2019designing}\nHewitt, J. and Liang, P.\n\\newblock Designing and Interpreting Probes with Control Tasks.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2019.\n\n\\bibitem{pires2019multilingual}\nPires, T., Schlinger, E., and Garrette, D.\n\\newblock How Multilingual is Multilingual BERT?\n\\newblock In \\emph{Proc.\\ ACL}, 2019.\n\n\\bibitem{wu2019beto}\nWu, S. and Dredze, M.\n\\newblock Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2019.\n\n\\end{thebibliography}\n\n%==============================================================================\n\\appendix\n\\section{Per-Language Spearman Correlations (Qwen3-235B)}\n\\label{app:per_lang}\n\nTable~\\ref{tab:per_lang_rho} reports per-language Spearman $\\rho$ between layer depth and zero-shot AUROC on Qwen3-235B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) on Qwen3-235B.}\n\\label{tab:per_lang_rho}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nLanguage & Tier & $\\rho$ & $p$ & Significant \\\\\n\\midrule\nzh & HIGH & $-0.72$ & 0.001 & $\\checkmark$ \\\\\nes & HIGH & $-0.68$ & 0.002 & $\\checkmark$ \\\\\nfr & HIGH & $-0.70$ & 0.001 & $\\checkmark$ \\\\\nde & HIGH & $-0.69$ & 0.002 & $\\checkmark$ \\\\\nja & HIGH & $-0.74$ & 0.001 & $\\checkmark$ \\\\\nnl & HIGH & $-0.67$ & 0.003 & $\\checkmark$ \\\\\npt & MID  & $-0.65$ & 0.004 & $\\checkmark$ \\\\\nit & MID  & $-0.66$ & 0.003 & $\\checkmark$ \\\\\nar & MID  & $-0.71$ & 0.001 & $\\checkmark$ \\\\\nhi & MID  & $-0.63$ & 0.005 & $\\checkmark$ \\\\\nko & MID  & $-0.67$ & 0.003 & $\\checkmark$ \\\\\ntr & MID  & $-0.62$ & 0.006 & $\\checkmark$ \\\\\nru & MID  & $-0.69$ & 0.002 & $\\checkmark$ \\\\\nvi & MID  & $-0.61$ & 0.008 & $\\checkmark$ \\\\\nth & MID  & $-0.58$ & 0.012 & $\\checkmark$ \\\\\nsw & LOW  & $-0.52$ & 0.025 & $\\checkmark$ \\\\\nbn & LOW  & $-0.55$ & 0.018 & \\\\\nyo & LOW  & $-0.48$ & 0.042 & \\\\\nig & LOW  & $-0.51$ & 0.028 & \\\\\nte & LOW  & $-0.45$ & 0.058 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{CKA Heatmap Summary by Resource Tier}\n\\label{app:cka_heatmap}\n\nTable~\\ref{tab:cka_heatmap} shows mean CKA (EN vs.\\ target) on Qwen3-235B by depth and resource tier.\n\n\\begin{table}[h]\n\\centering\n\\caption{CKA heatmap summary (Qwen3, mean across 20 languages by tier).}\n\\label{tab:cka_heatmap}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nDepth\\% & HIGH & MID & LOW & Overall \\\\\n\\midrule\n13 & 0.86 & 0.79 & 0.62 & 0.78 \\\\\n30 & 0.84 & 0.77 & 0.58 & 0.76 \\\\\n47 & 0.68 & 0.56 & 0.35 & 0.56 \\\\\n64 & 0.48 & 0.37 & 0.22 & 0.38 \\\\\n77 & 0.38 & 0.27 & 0.14 & 0.28 \\\\\n94 & 0.25 & 0.18 & 0.09 & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Language Zero-Shot AUROC (Qwen3-235B)}\n\\label{app:per_lang_auroc}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-language zero-shot AUROC at best-transfer layer (L52) on Qwen3-235B.}\n\\label{tab:per_lang_auroc}\n\\small\n\\begin{tabular}{llc||llc}\n\\toprule\nLang & Tier & AUROC & Lang & Tier & AUROC \\\\\n\\midrule\nzh & HIGH & 0.77 & tr & MID & 0.71 \\\\\nes & HIGH & 0.76 & ru & MID & 0.74 \\\\\nfr & HIGH & 0.76 & vi & MID & 0.70 \\\\\nde & HIGH & 0.77 & th & MID & 0.69 \\\\\nja & HIGH & 0.75 & sw & LOW & 0.63 \\\\\nnl & HIGH & 0.76 & bn & LOW & 0.65 \\\\\npt & MID  & 0.75 & yo & LOW & 0.57 \\\\\nit & MID  & 0.75 & ig & LOW & 0.61 \\\\\nar & MID  & 0.73 & te & LOW & 0.58 \\\\\nhi & MID  & 0.71 & & & \\\\\nko & MID  & 0.72 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Projection Saturation by Resource Tier}\n\\label{app:proj_saturation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Procrustes alignment saturation by resource tier.}\n\\label{tab:proj_saturation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTier & Pairs to 90\\% & Pairs to 95\\% & Interpretation \\\\\n\\midrule\nHIGH & 15 & 22 & Low effective rank \\\\\nMID  & 25 & 38 & Moderate complexity \\\\\nLOW  & 35 & 48 & Complex rotation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a792c7c-bbe0-41b8-beb7-83e7e3a9c754",
  "isSidechain": false,
  "requestId": "req_011CbFATKBTZVJtYEd8qjyuR",
  "type": "assistant",
  "uuid": "badb839d-99bc-483a-8f6a-097bbb8acefc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MxajJ2gVk4Y63VaSKhxi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7294,
      "cache_read_input_tokens": 47485,
      "output_tokens": 20346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20346,
          "cache_read_input_tokens": 47485,
          "cache_creation_input_tokens": 7294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7294
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

_source line 24 · 2026-05-21T05:35:43.009Z_

<details><summary>↩ Tool result · `toolu_0111iMTFEimA2WyEexoCvMeR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "badb839d-99bc-483a-8f6a-097bbb8acefc",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "ef992eae-18cb-465b-beea-5ac06751c207",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{array}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}\n\n\\newcommand{\\rmark}{\\textcolor{red}{$\\rho$}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\n\\title{Geometric Analysis Reveals When and Why\\\\Cross-Lingual Calibration Transfer Succeeds}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nProbe-based calibration methods can detect whether a language model's internal representations encode answer correctness, but all existing approaches are English-only. We present the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B Dense), 50 languages, and five transfer conditions. Our analysis reveals four interconnected findings forming a causal chain. \\textbf{(1)}~A depth-transferability Pareto frontier whose strength is architecture-dependent: Qwen3 exhibits a strong, consistent tradeoff (per-language Spearman $\\rho$ significant in 15/20 languages) while Llama~4 shows a weak, language-specific pattern (6/20 significant; three languages exhibit reversed trends). \\textbf{(2)}~Decomposing correctness into difficulty-shared (65\\% variance, 12\\% of transfer degradation) and capability-specific (35\\% variance, 88\\% of degradation) components reveals that capability-specific representations drive deep-layer transfer failure. \\textbf{(3)}~CaCLR, a consistency-regularized calibration method requiring no target-language labels, provides a mean improvement of +3.5\\pp{} AUROC over zero-shot transfer, with gains concentrated at deep layers (+4.8\\pp). \\textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship---raw correlation is negative ($\\rho = -0.36$ to $-0.41$; depth confound) but partial correlation controlling for depth is significantly positive ($\\rho = +0.41$ to $+0.48$; $p < 0.01$ on both architectures)---reveals that within-layer cross-lingual CKA genuinely predicts transfer quality while the correctness direction occupies a near-universal subspace (within-layer angle $12.4^{\\circ}$). We additionally find that 28\\% of low-resource probing results are capacity artifacts, and that Procrustes alignment reverses direction at a threshold of $\\sim$0.52 zero-shot AUROC. Code and probes will be released.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nMultilingual large language models suffer from a persistent calibration gap: non-English languages exhibit expected calibration error (ECE) up to five times worse than English \\cite{joshi2024llm}. Output-based recalibration methods such as temperature scaling require per-language calibration data, while ensemble approaches like MKA incur multiplicative inference costs \\cite{zhou2024lace}. Recent work on probe-based calibration offers an alternative: linear probes trained on internal representations can detect whether a model ``knows'' the answer is correct, and this correctness direction is nearly orthogonal to the model's verbalized confidence \\cite{miao2026coral,miao2026steering}. However, the entire probe-based calibration literature is English-only.\n\nCan English-trained correctness probes transfer to other languages without target-language labels? If so, under what conditions, and why does transfer succeed or fail? These questions are fundamental to the viability of representation-level calibration beyond English. Xiao et al.\\ \\cite{xiao2025crosslingual} transferred \\emph{knowledge boundary} probes---binary answerability classifiers at the input level---and found encouraging results in 8 languages. But correctness probing targets a fundamentally different signal: output-dependent accuracy on specific items, not input-level answerability. The cross-lingual properties of correctness representations remain unexplored.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer. Probing three architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense) across 20--50 typologically diverse languages on GlobalMMLU, we discover a \\emph{depth-transferability Pareto frontier}: deeper layers yield better English probes but progressively degrade in zero-shot cross-lingual transfer. The frontier's strength is architecture-dependent---strong and consistent on Qwen3, weak and language-specific on Llama~4. A geometric analysis based on centered kernel alignment (CKA) reveals a Simpson's Paradox at the heart of this phenomenon: pooling across layers, CKA and transfer quality correlate \\emph{negatively} (depth confound), but controlling for layer depth, higher within-layer CKA significantly predicts better transfer ($p < 0.01$ on both architectures). The correctness direction itself occupies a near-universal low-dimensional subspace (cross-language angle $12.4^{\\circ}$ within each layer) that persists even as global representations specialize by language.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Pareto discovery.} We identify an architecture-dependent depth-transferability tradeoff across three architectures and 20 languages, with Pareto knee at 55--58\\% depth.\n\\item \\textbf{Decomposition analysis.} We decompose correctness into difficulty-shared and capability-specific components, showing that capability drives 88\\% of transfer degradation despite accounting for only 35\\% of variance.\n\\item \\textbf{CaCLR method.} A consistency-regularized calibration approach providing +3.5\\pp{} mean AUROC gain without target-language labels, with gains concentrated at deep layers.\n\\item \\textbf{CKA geometric explanation.} The Simpson's Paradox, subspace persistence ($12.4^{\\circ}$ within-layer, $38.7^{\\circ}$ cross-layer), and CKA cliff threshold ($\\sim$0.35) together explain when and why transfer succeeds.\n\\end{enumerate}\nAdditionally, we report that 28\\% of low-resource probing results are capacity artifacts (a methodological warning for the field), that Procrustes alignment with $\\sim$42 parallel pairs reaches 95\\% of full performance, and that Procrustes helps below a zero-shot AUROC threshold of $\\sim$0.52 but \\emph{hurts} above it.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Probe-based calibration.}\nLinear probes trained on internal representations to detect answer correctness were introduced by Miao et al.\\ \\cite{miao2026coral} (CORAL) and extended to confidence--correctness steering vectors \\cite{miao2026steering}. CCPS \\cite{ji2024llm} identifies ``truth-telling'' and ``confidence'' directions in representation space. Ji et al.\\ \\cite{ji2024llm} demonstrate that the correctness direction and verbalized confidence are nearly orthogonal. All of these operate exclusively in English.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al.\\ \\cite{xiao2025crosslingual} transfer knowledge-boundary probes across 8 languages, reporting that mean-shift alignment and Procrustes rotation improve transfer. Their target is binary answerability (input-level), not correctness (output-dependent accuracy), and they evaluate probing accuracy rather than calibration. Civelli et al.\\ \\cite{civelli2024crosslingual} show that IRT difficulty transfers well cross-lingually. We decompose correctness into difficulty-shared and capability-specific components, directly building on their finding.\n\n\\paragraph{Cross-lingual representation alignment.}\nStatic cross-lingual alignment methods such as MUSE \\cite{conneau2018word} and VecMap \\cite{artetxe2018robust} demonstrate that Procrustes rotation effectively aligns embedding spaces with minimal parallel data. Our linear projection applies this principle at the sentence-level correctness representation, and we characterize sample efficiency across resource tiers.\n\n\\paragraph{Representation similarity.}\nCentered kernel alignment (CKA; \\cite{kornblith2019similarity}) and SVCCA \\cite{raghu2017svcca} quantify representation similarity across models and layers. We use CKA to measure cross-lingual similarity at each layer, revealing a Simpson's Paradox when the depth confound is controlled.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\cite{bendavid2010theory} formalize transfer error via $\\mathcal{H}$-divergence. Zhao et al.\\ \\cite{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly relevant to understanding why CaCLR's MMD-based matching provides bounded rather than unbounded improvement.\n\n\\paragraph{Conformal prediction.}\nDistribution-free coverage guarantees \\cite{angelopoulos2023conformal} provide complementary calibration. Unlike our zero-label approach, conformal methods require per-language calibration data; the two are complementary.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Cross-Lingual Correctness Probing}\n\\label{sec:method:probing}\n\nGiven a multilingual LLM with $L$ layers, we extract hidden-state representations at layer $l$ for each MCQA item in GlobalMMLU. An English logistic regression probe is trained:\n\\begin{equation}\np(\\text{correct} \\mid \\mathbf{h}_l^{\\text{en}}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l^{\\text{en}} + b_l)\n\\end{equation}\nwhere $\\mathbf{h}_l^{\\text{en}}$ is the pooled hidden state at layer $l$ for an English input. We evaluate this probe on target language representations $\\mathbf{h}_l^{\\text{tgt}}$ without any target-language labels (zero-shot transfer). We also evaluate under four additional conditions: (a)~mean-shift alignment, (b)~Procrustes linear projection with varying numbers of parallel pairs, (c)~few-shot fine-tuning with 25 or 100 target-language labels, and (d)~CaCLR (Section~\\ref{sec:method:caclr}).\n\nWe select logistic regression over nonlinear probes because linear probes better capture the language-agnostic linear structure of the correctness subspace. Empirically, MLPs gain +2\\pp{} English AUROC but lose 5.5\\pp{} in transfer (Section~\\ref{sec:probe_complexity}).\n\n\\paragraph{Mean-shift invariance.} Under StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits. Since AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically. Our data confirms this across all languages and layers.\n\n\\subsection{CaCLR: Calibration via Cross-Lingual Regularization}\n\\label{sec:method:caclr}\n\nCaCLR optimizes a joint loss over English labels and cross-lingual distributional consistency:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{BCE}}$ is binary cross-entropy on English correctness labels, $\\mathcal{L}_{\\text{SB-ECE}}$ is a soft-binned ECE loss, and $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) between English and target-language probe logits:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2_k\\big(\\{f(\\mathbf{h}_l^{\\text{en},i})\\}_{i=1}^n, \\{f(\\mathbf{h}_l^{\\text{tgt},i})\\}_{i=1}^n\\big)\n\\end{equation}\nwhere $f(\\cdot) = \\mathbf{w}^\\top(\\cdot) + b$ denotes the probe logit (1-D for linear probes), and $k$ is a Gaussian RBF kernel with bandwidth set by the median heuristic. The parallel activations come from GlobalMMLU test split (70/30 partition for train/eval); no target-language \\emph{labels} are used. We optimize with Adam ($\\text{lr}=10^{-3}$, linear warmup 10\\%), batch size 256, 50 epochs with early stopping (patience 10, monitoring validation AUROC). The probe is initialized from the standard logistic regression solution.\n\nCaCLR operates on 1-D logits---a design constraint of the linear probe. MMD in 1-D effectively matches mean and variance of the logit distributions across languages, equivalent to nudging the probe direction toward the universal correctness subspace revealed by our CKA analysis (Section~\\ref{sec:cka}). However, it cannot perform full rotational alignment, which limits its ceiling compared to explicit Procrustes rotation.\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:method:decomposition}\n\nFollowing Civelli et al.\\ \\cite{civelli2024crosslingual}, we train an IRT difficulty probe (Ridge regression) on item difficulty estimates, then project out the difficulty direction from the hidden states and retrain correctness probes on the residual representations. This decomposes correctness variance into:\n\\begin{itemize}\n\\item \\textbf{Difficulty-shared}: language-agnostic item difficulty information (hard items are hard everywhere).\n\\item \\textbf{Capability-specific}: language-dependent competence that varies across languages and depths.\n\\end{itemize}\nA random-direction control confirms that the decomposition captures genuine structure rather than arbitrary dimensionality reduction.\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:method:cka}\n\nWe compute linear CKA between English and each target language at every probed layer. Three analyses probe the geometry:\n\\begin{enumerate}\n\\item \\textbf{Same-layer cross-language correlation}: at each layer, Spearman correlation between CKA$_l(\\text{en}, \\text{tgt})$ and zero-shot AUROC$_l(\\text{tgt})$ across $n=20$ languages.\n\\item \\textbf{Partial Spearman correlation}: controlling for normalized depth, testing whether CKA predicts transfer beyond the depth confound.\n\\item \\textbf{Subspace angle analysis}: measuring the angular deviation of the correctness direction $\\mathbf{w}_l$ across languages within the same layer and across layers.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\subsection{Models}\n\nWe evaluate three architectures spanning MoE and dense designs:\n\n\\begin{table}[h]\n\\centering\n\\caption{Model specifications and summary results across 20 languages.}\n\\label{tab:three_arch}\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nModel & Type & Layers & EN Best & ZS Mean & Pareto $\\rho$ & Simpson $\\rho_{\\text{partial}}$ & CaCLR $\\Delta$\\pp \\\\\n\\midrule\nQwen3-235B & MoE & 94 & 0.81 & 0.72 & $-0.91$ & $+0.48$ & $+3.7$ \\\\\nLlama~4 Scout & MoE & 48 & 0.79 & 0.70 & $-0.78$ & $+0.41$ & $+3.3$ \\\\\nGemma~4 31B & Dense & 60 & 0.80 & 0.71 & $-0.85$ & $+0.44$ & $+3.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen3-235B-A22B is a 94-layer MoE model ($\\sim$22B active parameters) run under GPTQ-Int4 quantization. Llama~4 Scout is a 48-layer MoE model (17B$\\times$16 experts, top-2 routing) under W4A16. Gemma~4 31B is a 60-layer dense model run in FP16. We probe every 4th layer (24 layers for Qwen3, 12 for Llama~4, 15 for Gemma~4). Quantization validation (Section~\\ref{sec:quant}) confirms negligible distortion (mean $\\leq 0.5\\pp$, rank correlation $\\geq 0.994$).\n\n\\subsection{Languages and Benchmarks}\n\nOur core evaluation covers 20 typologically diverse languages grouped by resource tier: HIGH (zh, es, fr, de, ja, nl, pt, it), MID (ar, hi, ko, tr, ru, vi, th), and LOW (sw, bn, yo, ig, te). Extended evaluation (Section~\\ref{sec:extended}) expands to 50 languages including Austronesian, Dravidian, Uralic, Kartvelian, and additional Niger-Congo families. Primary benchmark is GlobalMMLU; cross-benchmark generalization is assessed on Belebele and MMLU-ProX (Section~\\ref{sec:cross_benchmark}).\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\\label{sec:pareto}\n\n\\paragraph{Qwen3-235B.}\nTable~\\ref{tab:qwen_pareto} shows the layer-wise profile. The English-optimal layer (L72, 77\\% depth, AUROC 0.81) and zero-shot-optimal layer (L52, 55\\% depth, AUROC 0.72) are separated by 20 layers. The Pareto frontier spans layers L40--L56 with a knee gap of 4.2\\pp. The global Spearman correlation between depth and zero-shot AUROC is $\\rho = -0.91$ ($p < 0.001$), and 15 of 20 per-language correlations are significantly negative ($p < 0.05$). The two languages failing the 0.60 AUROC threshold are Yoruba (0.57) and Telugu (0.58), both extremely low-resource in pretraining data.\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen3-235B Pareto frontier. Selected layers from 24 probed (every 4th of 94). $\\checkmark$ marks Pareto-optimal layers.}\n\\label{tab:qwen_pareto}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nLayer & Depth\\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp & Pareto \\\\\n\\midrule\n4  & 4  & 0.580 & 0.572 & 0.8  & \\\\\n12 & 13 & 0.645 & 0.632 & 1.3  & \\\\\n20 & 21 & 0.710 & 0.695 & 1.5  & \\\\\n28 & 30 & 0.752 & 0.733 & 1.9  & \\\\\n36 & 38 & 0.778 & 0.752 & 2.6  & \\\\\n40 & 43 & 0.788 & 0.748 & 4.0  & $\\checkmark$ \\\\\n44 & 47 & 0.796 & 0.740 & 5.6  & $\\checkmark$ \\\\\n48 & 51 & 0.802 & 0.732 & 7.0  & $\\checkmark$ \\\\\n52 & 55 & 0.806 & 0.720 & 8.6  & $\\checkmark$ \\\\\n56 & 60 & 0.808 & 0.706 & 10.2 & $\\checkmark$ \\\\\n60 & 64 & 0.810 & 0.690 & 12.0 & \\\\\n68 & 72 & 0.810 & 0.661 & 14.9 & \\\\\n72 & 77 & 0.810 & 0.638 & 17.2 & \\\\\n80 & 85 & 0.805 & 0.601 & 20.4 & \\\\\n88 & 94 & 0.792 & 0.558 & 23.4 & \\\\\n92 & 98 & 0.778 & 0.531 & 24.7 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama~4 Scout.}\nTable~\\ref{tab:llama_pareto} shows a qualitatively different pattern. While the global $\\rho = -0.78$ is significant ($p = 0.003$), only 6 of 20 per-language correlations reach significance. Three languages (ar, hi, ko) exhibit \\emph{positive} $\\rho$---deeper layers improve transfer. The Pareto frontier is narrower (L20--L28) with a smaller knee gap of 3.4\\pp. The median per-language $\\rho$ is $-0.28$, compared to $-0.64$ for Qwen3.\n\n\\begin{table}[t]\n\\centering\n\\caption{Llama~4 Scout Pareto frontier.}\n\\label{tab:llama_pareto}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nLayer & Depth\\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp & Pareto \\\\\n\\midrule\n4  & 8   & 0.560 & 0.552 & 0.8  & \\\\\n8  & 17  & 0.635 & 0.625 & 1.0  & \\\\\n12 & 25  & 0.695 & 0.682 & 1.3  & \\\\\n16 & 33  & 0.735 & 0.718 & 1.7  & \\\\\n20 & 42  & 0.758 & 0.724 & 3.4  & $\\checkmark$ \\\\\n24 & 50  & 0.772 & 0.714 & 5.8  & $\\checkmark$ \\\\\n28 & 58  & 0.782 & 0.700 & 8.2  & $\\checkmark$ \\\\\n32 & 67  & 0.789 & 0.681 & 10.8 & \\\\\n36 & 75  & 0.790 & 0.655 & 13.5 & \\\\\n40 & 83  & 0.785 & 0.625 & 16.0 & \\\\\n44 & 92  & 0.772 & 0.589 & 18.3 & \\\\\n48 & 100 & 0.748 & 0.548 & 20.0 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture comparison.}\nTable~\\ref{tab:arch_compare} quantifies the architecture-dependent tradeoff. The 2.3$\\times$ difference in median per-language effect size ($-0.64$ vs.\\ $-0.28$) is the core observation: on Qwen3, practitioners must explicitly choose between English accuracy and transfer quality; on Llama~4, some languages can ``free-ride'' deep-layer improvements. The best-transfer depth converges to 55--58\\% across both architectures, suggesting a universal mid-depth transfer zone whose \\emph{steepness} is architecture-specific.\n\n\\begin{table}[t]\n\\centering\n\\caption{Architecture-dependent Pareto comparison.}\n\\label{tab:arch_compare}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Qwen3-235B & Llama~4 Scout & Interpretation \\\\\n\\midrule\nGlobal $\\rho$ & $-0.91$ & $-0.78$ & Both significant, Qwen stronger \\\\\nPer-lang sig.\\ count & 15/20 & 6/20 & Qwen consistent, Llama mixed \\\\\nMedian per-lang $\\rho$ & $-0.64$ & $-0.28$ & 2.3$\\times$ effect size difference \\\\\nPositive-$\\rho$ langs & 0 & 3 & Llama: ar/hi/ko reversed \\\\\nBest transfer depth\\% & 55 & 58 & Comparable location \\\\\nEN--ZS gap at knee\\pp & 4.2 & 3.4 & Comparable magnitude \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Transfer conditions.}\nTable~\\ref{tab:transfer_conditions} compares five transfer methods at the best-transfer layer. Mean-shift yields $\\Delta\\text{AUROC} = 0.0$ (as proven by the rank-invariance argument). Linear projection (+1.9\\pp{} combined) and few-shot-100 (+1.7\\pp) provide moderate gains. CaCLR (+3.5\\pp) provides the largest zero-label improvement.\n\n\\begin{table}[t]\n\\centering\n\\caption{Transfer conditions at best-transfer layer (both models averaged).}\n\\label{tab:transfer_conditions}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Qwen3 & Llama~4 & Combined & Requires \\\\\n\\midrule\nZero-shot     & 0.720 & 0.700 & 0.710 & --- \\\\\nMean-shift    & 0.720 & 0.700 & 0.710 & --- \\\\\nLinProj (200) & 0.740 & 0.718 & 0.729 & 200 parallel pairs \\\\\nFew-shot (25) & 0.708 & 0.692 & 0.700 & 25 target labels \\\\\nFew-shot (100)& 0.735 & 0.718 & 0.727 & 100 target labels \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Simpson's Paradox in CKA--Transfer Relationship}\n\\label{sec:cka}\n%------------------------------------------------------------------------------\n\nThe central geometric finding is a Simpson's Paradox. When CKA values and zero-shot AUROC are pooled across all layers and languages, the Spearman correlation is \\emph{negative}: $\\rho = -0.36$ ($p < 0.001$) for Qwen3 and $\\rho = -0.41$ ($p < 0.001$) for Llama~4. This arises because shallow layers have high CKA but weak probes (low AUROC), while deep layers have low CKA but strong probes (high AUROC before transfer degradation kicks in).\n\nControlling for normalized depth reverses the sign. The partial Spearman correlation is $\\rho = +0.48$ ($p = 0.002$, 95\\% bootstrap CI $[+0.31, +0.62]$) for Qwen3 and $\\rho = +0.41$ ($p = 0.008$, CI $[+0.22, +0.57]$) for Llama~4 (Table~\\ref{tab:simpson}). Within each layer, higher cross-lingual CKA genuinely predicts better transfer. This finding replicates on Gemma~4 31B ($\\rho_{\\text{partial}} = +0.44$, $p = 0.004$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation between CKA and zero-shot transfer AUROC.}\n\\label{tab:simpson}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Analysis & $\\rho$ & $p$ & Bootstrap 95\\% CI & Sign \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-235B}\n & Raw pooled  & $-0.36$ & $<$0.001 & $[-0.44, -0.27]$ & negative \\\\\n & Partial (depth) & $+0.48$ & 0.002 & $[+0.31, +0.62]$ & positive \\\\\n\\midrule\n\\multirow{2}{*}{Llama~4 Scout}\n & Raw pooled  & $-0.41$ & $<$0.001 & $[-0.50, -0.31]$ & negative \\\\\n & Partial (depth) & $+0.41$ & 0.008 & $[+0.22, +0.57]$ & positive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-layer correlations.}\nTable~\\ref{tab:per_layer_cka} shows that on Qwen3, 18 of 24 per-layer correlations are positive and 6 reach significance at $p < 0.05$ ($n = 20$ languages per layer). The signal is strongest at intermediate depths (13--38\\%) where CKA variance across languages is largest, and weakens at deep layers where CKA collapses toward a floor ($\\sim$0.22--0.28).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-layer CKA--transfer correlation on Qwen3-235B (selected layers, $n=20$ languages per layer).}\n\\label{tab:per_layer_cka}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nLayer & Depth\\% & Mean CKA$_{20}$ & Spearman $\\rho$ & $p$ \\\\\n\\midrule\n12 & 13 & 0.78 & 0.52 & 0.019 \\\\\n20 & 21 & 0.81 & 0.48 & 0.032 \\\\\n28 & 30 & 0.76 & 0.55 & 0.012 \\\\\n36 & 38 & 0.68 & 0.51 & 0.022 \\\\\n44 & 47 & 0.56 & 0.46 & 0.041 \\\\\n52 & 55 & 0.45 & 0.43 & 0.058 \\\\\n60 & 64 & 0.38 & 0.38 & 0.098 \\\\\n68 & 72 & 0.30 & 0.33 & 0.155 \\\\\n72 & 77 & 0.28 & 0.28 & 0.231 \\\\\n80 & 85 & 0.22 & 0.21 & 0.372 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Subspace angle analysis.}\nTable~\\ref{tab:subspace} reveals why within-layer CKA predicts transfer: the correctness direction is near-universal within each layer (mean cross-language angle $12.4^{\\circ} \\pm 5.8^{\\circ}$) but rotates substantially across layers ($38.7^{\\circ} \\pm 11.2^{\\circ}$). The random baseline ($87.3^{\\circ} \\pm 2.1^{\\circ}$, near-orthogonal) confirms these angles reflect genuine structure. Global CKA decline reflects divergence in \\emph{non-correctness} dimensions; the correctness subspace itself persists as a low-dimensional feature. This explains why raw CKA (mixing correctness and non-correctness dimensions) misleads while within-layer CKA (where depth is held constant) captures the relevant alignment.\n\n\\begin{table}[t]\n\\centering\n\\caption{Subspace angle analysis of the correctness direction.}\n\\label{tab:subspace}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & Mean Angle & Std & Interpretation \\\\\n\\midrule\nWithin-layer, cross-language & $12.4^{\\circ}$ & $5.8^{\\circ}$ & Near-universal direction \\\\\nCross-layer, same-language   & $38.7^{\\circ}$ & $11.2^{\\circ}$ & Significant rotation \\\\\nRandom baseline (shuffled)   & $87.3^{\\circ}$ & $2.1^{\\circ}$ & Near-orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CKA cliff and transfer collapse.}\nCKA drops sharply at 55\\% depth on Qwen3 and 50\\% on Llama~4. A collapse threshold of CKA $\\approx 0.35$ separates two regimes: language-layer pairs above this threshold achieve mean zero-shot AUROC of 0.72, while those below achieve only 0.58. Qwen3's steeper cliff (peak 0.82 $\\to$ floor 0.28 at EN-optimal layer) drives more languages below threshold at deep layers, producing the stronger Pareto tradeoff. Llama~4's shallower cliff (0.84 $\\to$ 0.35) allows ar/hi/ko to remain above threshold throughout, explaining their anomalous positive depth--transfer relationship.\n\n%------------------------------------------------------------------------------\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n%------------------------------------------------------------------------------\n\nThe IRT difficulty probe achieves $R^2 = 0.68$ (range 0.55--0.78 across layers and models). Table~\\ref{tab:decomposition} shows the decomposition: the difficulty-shared component accounts for 65\\% of correctness variance but only 12\\% of transfer degradation. The capability-specific residual accounts for 35\\% of variance but drives 88\\% of degradation. Projecting out difficulty reduces English AUROC by only 4.5\\pp{} (from 0.81 to $\\sim$0.765) while reducing the zero-shot transfer gap by 0.8\\pp---confirming that difficulty is nearly perfectly transferable while capability is the bottleneck.\n\n\\begin{table}[t]\n\\centering\n\\caption{Difficulty--capability decomposition of correctness transfer. Combined across both architectures and 10 languages $\\times$ 8 layers.}\n\\label{tab:decomposition}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nComponent & Var.\\% & Transfer AUROC & Transfer Drop\\pp & Degradation Share \\\\\n\\midrule\nFull correctness    & 100 & 0.710 & 9.0  & 100\\% \\\\\nDifficulty-shared   & 65  & 0.698 & 1.1  & 12\\% \\\\\nCapability-specific & 35  & 0.615 & 12.8 & 88\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cap_by_depth} shows that capability-driven transfer degradation accelerates with depth. At 20--30\\% depth, the difficulty-to-capability degradation ratio is 3$\\times$; at 75--90\\% it reaches 5.7$\\times$. This matches the CKA cliff: deep layers accumulate more capability-specific (language-dependent) information, and the CKA decline reflects exactly this divergence. The decomposition is prescriptive: it correctly predicts which alignment strategy is needed (zero-shot for difficulty-dominant vs.\\ CaCLR for capability-dominant combinations) with 78\\% accuracy.\n\nA random-direction control ($-1.2\\pp$ when projecting out a random direction) confirms the decomposition captures genuine structure.\n\n\\begin{table}[t]\n\\centering\n\\caption{Capability-specific transfer degradation by depth.}\n\\label{tab:cap_by_depth}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth Band & Difficulty Drop\\pp & Capability Drop\\pp & Ratio \\\\\n\\midrule\n20--30\\% & 0.2 & 0.6 & 3$\\times$ \\\\\n40--50\\% & 0.6 & 2.8 & 4.7$\\times$ \\\\\n60--70\\% & 1.0 & 5.6 & 5.6$\\times$ \\\\\n75--90\\% & 1.5 & 8.5 & 5.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{CaCLR Evaluation}\n\\label{sec:caclr}\n%------------------------------------------------------------------------------\n\n\\paragraph{Consistency loss effect.}\nTable~\\ref{tab:beta_sweep} shows the $\\beta$ sweep across three orders of magnitude. The optimal $\\beta = 0.05$ achieves +3.5\\pp{} AUROC and $-2.4\\pp$ ECE improvement. Below $\\beta = 0.001$, gradient noise exceeds signal; above $\\beta = 1.0$, MMD dominates BCE and probe accuracy degrades. The optimal $\\alpha = 0.1$ provides $-3.2\\pp$ ECE improvement.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\beta$ sweep for the consistency loss ($\\alpha = 0.1$ fixed). Combined across both architectures at best-transfer layer.}\n\\label{tab:beta_sweep}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n$\\beta$ & $\\Delta$AUROC\\pp{} vs ZS & $\\Delta$ECE\\pp & Note \\\\\n\\midrule\n0.0   & 0.0   & 0.0    & Baseline (BCE only) \\\\\n0.001 & +0.5  & $-0.3$ & Marginal improvement \\\\\n0.01  & +1.8  & $-1.1$ & Clear positive signal \\\\\n0.05  & +3.5  & $-2.4$ & Optimal tradeoff \\\\\n0.1   & +3.2  & $-2.0$ & Slight over-regularization \\\\\n1.0   & +0.8  & $-0.5$ & MMD dominates \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Component ablation.}\nBCE-only achieves AUROC 0.710; adding SB-ECE (+0.012 to 0.722) primarily improves calibration. Adding consistency loss alone (+0.028 to 0.738) is the primary contributor. The full CaCLR (+0.035 to 0.745) shows a synergy between the two regularizers.\n\n\\paragraph{Comparison with all methods.}\nTable~\\ref{tab:caclr_compare} places CaCLR in context. CaCLR achieves the highest AUROC (0.745) and second-lowest ECE (0.082, after few-shot-100 at 0.088) among all methods, without requiring any target-language labels. It surpasses linear projection by 1.6\\pp{} AUROC because end-to-end gradient optimization can exploit training dynamics beyond post-hoc geometric correction. However, the gap is modest---consistent with the 1-D MMD limitation: it matches scalar logit distributions but cannot perform full subspace rotation.\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR vs.\\ all transfer methods (both models averaged at best-transfer layer).}\n\\label{tab:caclr_compare}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nMethod & AUROC & ECE & Labels Required & Key Resource \\\\\n\\midrule\nZero-shot       & 0.710 & 0.118 & None & --- \\\\\nMean-shift      & 0.710 & 0.118 & None & --- \\\\\nLinProj (50)    & 0.725 & 0.098 & 50 parallel & Procrustes \\\\\nLinProj (200)   & 0.729 & 0.095 & 200 parallel & Procrustes \\\\\nFew-shot (25)   & 0.700 & 0.102 & 25 labeled & Target labels \\\\\nFew-shot (100)  & 0.727 & 0.088 & 100 labeled & Target labels \\\\\n\\textbf{CaCLR}  & \\textbf{0.745} & \\textbf{0.082} & None & Parallel activations \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Depth profile.}\nTable~\\ref{tab:caclr_depth} shows CaCLR's improvement on Qwen3 as a function of depth. The gain grows from +1.2\\pp{} at 30\\% depth to +4.8--5.0\\pp{} at 64--77\\% depth, then moderates to +4.0\\pp{} at 85\\%. This pattern aligns with the decomposition analysis: deep layers have larger capability-specific components, providing more signal for the consistency loss to exploit. CaCLR improves in 88\\% of model-language pairs (35/40); the 5 non-improving pairs are high-resource languages on shallow layers where zero-shot transfer is already near ceiling.\n\n\\begin{table}[t]\n\\centering\n\\caption{CaCLR depth profile on Qwen3-235B.}\n\\label{tab:caclr_depth}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\nDepth\\% & ZS AUROC & CaCLR AUROC & $\\Delta$\\pp \\\\\n\\midrule\n30 & 0.733 & 0.745 & +1.2 \\\\\n43 & 0.748 & 0.766 & +1.8 \\\\\n55 & 0.720 & 0.752 & +3.2 \\\\\n64 & 0.690 & 0.738 & +4.8 \\\\\n77 & 0.638 & 0.688 & +5.0 \\\\\n85 & 0.601 & 0.641 & +4.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen3 specifically, CaCLR achieves mean AUROC 0.757 (+3.7\\pp{} vs.\\ ZS) with ECE 0.078. On Llama~4, mean AUROC 0.733 (+3.3\\pp) with ECE 0.085.\n\n%------------------------------------------------------------------------------\n\\subsection{Linear Projection Sensitivity}\n\\label{sec:linproj}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:proj_efficiency} characterizes Procrustes alignment sample efficiency. Performance reaches 95\\% of the 200-pair baseline at $\\sim$42 parallel pairs overall, with resource-tier stratification: HIGH languages saturate at 22 pairs (simple rotation, low effective rank), MID at 38, and LOW at 48 (complex rotation, more parameters to estimate).\n\n\\begin{table}[t]\n\\centering\n\\caption{Procrustes linear projection: sample efficiency.}\n\\label{tab:proj_efficiency}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$n$ Pairs & \\% of 200-Pair & Mean AUROC & Note \\\\\n\\midrule\n10  & 72\\% & 0.724 & High variance \\\\\n20  & 86\\% & 0.728 & Dominant rotation captured \\\\\n30  & 92\\% & 0.731 & Near plateau for HIGH \\\\\n50  & 97\\% & 0.734 & Near plateau for all tiers \\\\\n100 & 99\\% & 0.737 & Marginal returns \\\\\n200 & 100\\% & 0.729 & Reference baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Procrustes effect reversal.}\nTable~\\ref{tab:procrustes_reversal} reveals a striking non-monotonicity. When zero-shot AUROC is below $\\sim$0.52, Procrustes alignment helps substantially (+5.2\\pp{} for AUROC $< 0.45$; +2.4\\pp{} for $0.45$--$0.52$). But when zero-shot AUROC exceeds 0.60, Procrustes \\emph{hurts} ($-1.2\\pp$): the correctness directions are already well-aligned, and Procrustes introduces estimation noise. The threshold of 0.52 corresponds to CKA $\\approx 0.35$ (the transfer collapse threshold from Section~\\ref{sec:cka}), providing a geometric explanation for when alignment is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Procrustes effect reversal by zero-shot AUROC range.}\n\\label{tab:procrustes_reversal}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\nZS AUROC Range & $n$ Pairs & Mean $\\Delta$\\pp & Direction \\\\\n\\midrule\n$<$0.45      & 42  & +5.2  & Strong positive \\\\\n0.45--0.52   & 68  & +2.4  & Moderate positive \\\\\n0.52--0.60   & 95  & +0.3  & Transition zone \\\\\n0.60--0.70   & 88  & $-1.2$ & Negative \\\\\n$>$0.70      & 47  & $-0.8$ & Slight negative \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Control Task Analysis}\n\\label{sec:control}\n%------------------------------------------------------------------------------\n\nFollowing Hewitt \\& Liang \\cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC). Table~\\ref{tab:control_selectivity} shows selectivity by resource tier and depth. Control probes achieve mean AUROC 0.495 ($\\pm 0.008$), confirming near-chance performance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selectivity by resource tier and depth band.}\n\\label{tab:control_selectivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDepth Band & HIGH & MID & LOW \\\\\n\\midrule\n0--30\\%   & 0.04 & 0.03 & 0.01 \\\\\n30--60\\%  & 0.18 & 0.14 & 0.06 \\\\\n60--80\\%  & 0.28 & 0.22 & 0.10 \\\\\n80--100\\% & 0.25 & 0.20 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:artifact_rates} presents artifact rates---the fraction of language-layer combinations where selectivity falls below a meaningful threshold. The finding is striking: \\textbf{27\\% of low-resource probing results are capacity artifacts}, concentrated at 60--100\\% depth. Mid- and high-resource artifact rates are low (5\\% and 3\\%). The most affected languages are yo, ig, te, and sw---all extremely low-resource in model pretraining.\n\n\\begin{table}[t]\n\\centering\n\\caption{Artifact rates by resource tier.}\n\\label{tab:artifact_rates}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Combinations & Artifact Count & Rate \\\\\n\\midrule\nHIGH  & 384 & 12 & 3\\% \\\\\nMID   & 336 & 17 & 5\\% \\\\\nLOW   & 240 & 65 & 27\\% \\\\\n\\midrule\nTotal & 960 & 94 & 10\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is, to our knowledge, the first application of probing control tasks to a cross-lingual transfer setting. The 27\\% low-resource artifact rate implies that cross-lingual probing studies without selectivity checks---including Xiao et al.\\ \\cite{xiao2025crosslingual}---may overestimate low-resource transfer quality. Our core Pareto and CKA analyses are unaffected because they are driven primarily by mid- and high-resource patterns, where artifact rates are $\\leq$5\\%.\n\n%------------------------------------------------------------------------------\n\\subsection{Cross-Lingual Correctness--Confidence Orthogonality}\n\\label{sec:orthogonality}\n%------------------------------------------------------------------------------\n\nExtending the English-only finding of Miao \\& Ungar \\cite{miao2026steering} (cosine $<$ 0.04 at 7--8B scale), we measure the cosine similarity between the verbalized confidence direction and the correctness direction across 20 languages and both architectures. Table~\\ref{tab:ortho} shows the results. The overall mean cosine is 0.05 (range 0.02--0.09); all 40 model-language pairs fall below 0.10. This confirms that output-based calibration methods are structurally limited across languages---not just in English.\n\nA resource-tier gradient emerges: HIGH 0.038, MID 0.052, LOW 0.072 ($r = -0.66$ between resource level and cosine). Better multilingual training produces cleaner separation between the correctness and confidence directions, though the effect size is small (range 0.034).\n\n\\begin{table}[t]\n\\centering\n\\caption{Correctness--confidence cosine similarity by resource tier.}\n\\label{tab:ortho}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Langs & Qwen3 Mean & Llama~4 Mean & Combined \\\\\n\\midrule\nHIGH & 8 & 0.035 & 0.041 & 0.038 \\\\\nMID  & 7 & 0.048 & 0.056 & 0.052 \\\\\nLOW  & 5 & 0.066 & 0.078 & 0.072 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Additional Analysis}\n\\label{sec:additional}\n%==============================================================================\n\n\\subsection{Probe Complexity}\n\\label{sec:probe_complexity}\n\nTable~\\ref{tab:probe_complexity} compares logistic regression and 2-layer MLP probes on Qwen3 at the English-optimal layer. The MLP gains +2\\pp{} English AUROC (0.83 vs.\\ 0.81) but suffers 5.5\\pp{} worse transfer (14.5\\pp{} vs.\\ 9.0\\pp{} zero-shot drop). The advantage of linear probes grows with depth: +2\\pp{} at shallow layers, +8.2\\pp{} at 80\\% depth. This validates the linear probe choice and supports the geometric interpretation: correctness transfer relies on a linear, language-agnostic subspace that MLPs overfit by exploiting language-specific nonlinear features.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe complexity comparison (Qwen3, EN-optimal layer).}\n\\label{tab:probe_complexity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nProbe Type & EN AUROC & ZS Mean$_{20}$ & ZS Drop\\pp \\\\\n\\midrule\nLogistic regression   & 0.81 & 0.720 & 9.0 \\\\\nMLP (2-layer, $h$=128) & 0.83 & 0.685 & 14.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_benchmark}\n\nTable~\\ref{tab:cross_bench} evaluates CaCLR on three benchmarks. The improvement is consistent: +3.5\\pp{} on GlobalMMLU, +3.3\\pp{} on Belebele (reading comprehension), and +3.5\\pp{} on MMLU-ProX (harder factual). Cross-benchmark coefficient of variation is 0.04, confirming that CaCLR addresses a fundamental representation alignment issue rather than overfitting to a specific benchmark's distribution.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-benchmark CaCLR generalization (both models, 20 languages).}\n\\label{tab:cross_bench}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & ZS Mean$_{20}$ & CaCLR Mean$_{20}$ & $\\Delta$\\pp \\\\\n\\midrule\nGlobalMMLU & 0.710 & 0.745 & +3.5 \\\\\nBelebele   & 0.695 & 0.728 & +3.3 \\\\\nMMLU-ProX  & 0.680 & 0.715 & +3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\nTable~\\ref{tab:quant} validates that quantization introduces negligible distortion. W4A16 on Llama~4 preserves 16-bit activations, yielding mean AUROC difference of 0.3\\pp{} (max 0.8\\pp) and rank correlation 0.996. GPTQ-Int4 on Qwen3 is more aggressive but still achieves mean difference 0.5\\pp{} (max 1.1\\pp) and rank correlation 0.994. The Pareto frontier ordering is fully preserved under both quantization schemes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Quantization validation at 5 representative layers per model.}\n\\label{tab:quant}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nModel & Layer & FP16 AUROC & Quant AUROC & $\\Delta$\\pp \\\\\n\\midrule\nLlama~4 & L8  & 0.637 & 0.634 & 0.3 \\\\\nLlama~4 & L16 & 0.737 & 0.735 & 0.2 \\\\\nLlama~4 & L28 & 0.784 & 0.781 & 0.3 \\\\\nLlama~4 & L36 & 0.792 & 0.789 & 0.3 \\\\\nLlama~4 & L44 & 0.774 & 0.770 & 0.4 \\\\\n\\midrule\nQwen3 & L20 & 0.712 & 0.708 & 0.4 \\\\\nQwen3 & L36 & 0.780 & 0.775 & 0.5 \\\\\nQwen3 & L52 & 0.808 & 0.803 & 0.5 \\\\\nQwen3 & L68 & 0.812 & 0.806 & 0.6 \\\\\nQwen3 & L80 & 0.807 & 0.800 & 0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Third Architecture: Gemma~4 31B Dense}\n\\label{sec:gemma}\n\nGemma~4 31B Dense serves as a dense-architecture contrast to the two MoE models. The English-optimal layer is L45 (AUROC 0.80), and the best-transfer layer is L36 (zero-shot mean 0.71). The global Spearman $\\rho = -0.85$ falls between Qwen3 ($-0.91$) and Llama~4 ($-0.78$). Simpson's Paradox replicates: $\\rho_{\\text{partial}} = +0.44$ ($p = 0.004$). CaCLR provides +3.0\\pp. These results (incorporated into Table~\\ref{tab:three_arch}) confirm that the depth-transferability tradeoff and Simpson's Paradox are properties of transformer depth, not of MoE routing or any single architecture family.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding from 20 to 50 languages (Table~\\ref{tab:extended}), we confirm all findings at scale. Zero-shot transfer achieves AUROC $\\geq 0.60$ in 42/50 languages (84\\% pass rate). CaCLR improves 47/50 languages. The resource-tier gradient is smooth and extends to a VERY\\_LOW tier (4 languages, mean ZS 0.53, CaCLR +5.0\\pp). The Pareto frontier structure, Simpson's Paradox, and CaCLR benefit pattern all hold across the expanded language set, with no language family showing anomalous behavior. CaCLR's benefit is inversely correlated with resource level, providing the largest gains for the languages that need it most.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended 50-language coverage by resource tier.}\n\\label{tab:extended}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ Langs & ZS Mean & CaCLR Mean & $\\Delta$\\pp \\\\\n\\midrule\nHIGH      & 10 & 0.75 & 0.78 & +2.8 \\\\\nMID       & 24 & 0.71 & 0.74 & +3.5 \\\\\nLOW       & 12 & 0.62 & 0.66 & +4.2 \\\\\nVERY\\_LOW & 4  & 0.53 & 0.58 & +5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{The causal chain.}\nOur four claims form an explanatory sequence. The Pareto frontier (Claim~1) establishes the empirical phenomenon: deeper probes are better for English but worse for transfer, with architecture-dependent severity. The decomposition (Claim~2) reveals the mechanism: capability-specific representations drive 88\\% of degradation and grow with depth. CaCLR (Claim~3) tests whether distributional matching can shift this frontier, and succeeds with +3.5\\pp{} mean improvement concentrated at deep layers where capability-specific content is largest. The CKA analysis (Claim~4) provides geometric grounding: the Simpson's Paradox shows that within-layer CKA genuinely predicts transfer, the subspace persistence explains why zero-shot transfer works at all, and the CKA cliff threshold connects to both the Pareto steepness and the Procrustes reversal point.\n\n\\paragraph{Practical implications.}\nFor practitioners deploying multilingual calibration probes: (1)~select layers at 55--60\\% depth rather than the English-optimal layer; (2)~check zero-shot AUROC before applying alignment---Procrustes helps below 0.52 but hurts above 0.60; (3)~if parallel data is available, $\\sim$42 pairs suffice for 95\\% of optimal performance; (4)~apply selectivity controls for low-resource languages to avoid capacity artifacts.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA evaluation; generalization to open-ended generation requires further investigation. CaCLR operates on 1-D logits due to the linear probe constraint, limiting its alignment capacity. The architecture comparison involves $n=3$ architectures that differ simultaneously in type, scale, and training data; we cannot causally attribute tradeoff differences to specific architectural features. The 27\\% low-resource artifact rate, while a warning for the field, means our low-resource conclusions should be interpreted with caution.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures and up to 50 languages. The depth-transferability Pareto frontier is real, architecture-dependent, and geometrically grounded: a Simpson's Paradox in the CKA--transfer relationship reveals that within-layer cross-lingual similarity genuinely predicts transfer quality once the depth confound is controlled. The correctness direction occupies a near-universal subspace ($12.4^{\\circ}$ within-layer angle) that persists even as global representations diverge. CaCLR provides a consistent +3.5\\pp{} improvement without target-language labels, with gains largest at deep layers where capability-specific content dominates. These findings establish that probe-based calibration is viable beyond English and provide geometric understanding of when and why it works.\n\n%==============================================================================\n% References\n%==============================================================================\n\\begin{thebibliography}{30}\n\n\\bibitem{joshi2024llm}\nJoshi, N., et al.\n\\newblock Are LLMs Calibrated? A Comprehensive Survey of Calibration in Large Language Models.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem{zhou2024lace}\nZhou, T., et al.\n\\newblock LACE: Layer-Adaptive Calibration Ensemble for Multilingual LLMs.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{miao2026coral}\nMiao, Y., et al.\n\\newblock CORAL: Cross-Task Correctness Probes for LLM Calibration.\n\\newblock In \\emph{Proc.\\ NAACL}, 2026.\n\n\\bibitem{miao2026steering}\nMiao, Y. and Ungar, L.\n\\newblock Steering Vectors for Confidence-Correctness Alignment.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem{ji2024llm}\nJi, Z., et al.\n\\newblock LLM Internal States Reveal Hallucination Risk.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{xiao2025crosslingual}\nXiao, Y., et al.\n\\newblock Cross-Lingual Transfer of Knowledge Boundary Probes.\n\\newblock In \\emph{Proc.\\ ACL}, 2025.\n\n\\bibitem{civelli2024crosslingual}\nCivelli, A., et al.\n\\newblock Cross-Lingual Difficulty Probes.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2024.\n\n\\bibitem{conneau2018word}\nConneau, A., et al.\n\\newblock Word Translation Without Parallel Data.\n\\newblock In \\emph{Proc.\\ ICLR}, 2018.\n\n\\bibitem{artetxe2018robust}\nArtetxe, M., et al.\n\\newblock A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings.\n\\newblock In \\emph{Proc.\\ ACL}, 2018.\n\n\\bibitem{kornblith2019similarity}\nKornblith, S., et al.\n\\newblock Similarity of Neural Network Representations Revisited.\n\\newblock In \\emph{Proc.\\ ICML}, 2019.\n\n\\bibitem{raghu2017svcca}\nRaghu, M., et al.\n\\newblock SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2017.\n\n\\bibitem{bendavid2010theory}\nBen-David, S., et al.\n\\newblock A Theory of Learning from Different Domains.\n\\newblock \\emph{Machine Learning}, 79(1-2):151--175, 2010.\n\n\\bibitem{zhao2019learning}\nZhao, H., et al.\n\\newblock On Learning Invariant Representations for Domain Adaptation.\n\\newblock In \\emph{Proc.\\ ICML}, 2019.\n\n\\bibitem{angelopoulos2023conformal}\nAngelopoulos, A. and Bates, S.\n\\newblock Conformal Prediction: A Gentle Introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 2023.\n\n\\bibitem{hewitt2019designing}\nHewitt, J. and Liang, P.\n\\newblock Designing and Interpreting Probes with Control Tasks.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2019.\n\n\\bibitem{pires2019multilingual}\nPires, T., Schlinger, E., and Garrette, D.\n\\newblock How Multilingual is Multilingual BERT?\n\\newblock In \\emph{Proc.\\ ACL}, 2019.\n\n\\bibitem{wu2019beto}\nWu, S. and Dredze, M.\n\\newblock Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.\n\\newblock In \\emph{Proc.\\ EMNLP}, 2019.\n\n\\end{thebibliography}\n\n%==============================================================================\n\\appendix\n\\section{Per-Language Spearman Correlations (Qwen3-235B)}\n\\label{app:per_lang}\n\nTable~\\ref{tab:per_lang_rho} reports per-language Spearman $\\rho$ between layer depth and zero-shot AUROC on Qwen3-235B.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) on Qwen3-235B.}\n\\label{tab:per_lang_rho}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nLanguage & Tier & $\\rho$ & $p$ & Significant \\\\\n\\midrule\nzh & HIGH & $-0.72$ & 0.001 & $\\checkmark$ \\\\\nes & HIGH & $-0.68$ & 0.002 & $\\checkmark$ \\\\\nfr & HIGH & $-0.70$ & 0.001 & $\\checkmark$ \\\\\nde & HIGH & $-0.69$ & 0.002 & $\\checkmark$ \\\\\nja & HIGH & $-0.74$ & 0.001 & $\\checkmark$ \\\\\nnl & HIGH & $-0.67$ & 0.003 & $\\checkmark$ \\\\\npt & MID  & $-0.65$ & 0.004 & $\\checkmark$ \\\\\nit & MID  & $-0.66$ & 0.003 & $\\checkmark$ \\\\\nar & MID  & $-0.71$ & 0.001 & $\\checkmark$ \\\\\nhi & MID  & $-0.63$ & 0.005 & $\\checkmark$ \\\\\nko & MID  & $-0.67$ & 0.003 & $\\checkmark$ \\\\\ntr & MID  & $-0.62$ & 0.006 & $\\checkmark$ \\\\\nru & MID  & $-0.69$ & 0.002 & $\\checkmark$ \\\\\nvi & MID  & $-0.61$ & 0.008 & $\\checkmark$ \\\\\nth & MID  & $-0.58$ & 0.012 & $\\checkmark$ \\\\\nsw & LOW  & $-0.52$ & 0.025 & $\\checkmark$ \\\\\nbn & LOW  & $-0.55$ & 0.018 & \\\\\nyo & LOW  & $-0.48$ & 0.042 & \\\\\nig & LOW  & $-0.51$ & 0.028 & \\\\\nte & LOW  & $-0.45$ & 0.058 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{CKA Heatmap Summary by Resource Tier}\n\\label{app:cka_heatmap}\n\nTable~\\ref{tab:cka_heatmap} shows mean CKA (EN vs.\\ target) on Qwen3-235B by depth and resource tier.\n\n\\begin{table}[h]\n\\centering\n\\caption{CKA heatmap summary (Qwen3, mean across 20 languages by tier).}\n\\label{tab:cka_heatmap}\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\nDepth\\% & HIGH & MID & LOW & Overall \\\\\n\\midrule\n13 & 0.86 & 0.79 & 0.62 & 0.78 \\\\\n30 & 0.84 & 0.77 & 0.58 & 0.76 \\\\\n47 & 0.68 & 0.56 & 0.35 & 0.56 \\\\\n64 & 0.48 & 0.37 & 0.22 & 0.38 \\\\\n77 & 0.38 & 0.27 & 0.14 & 0.28 \\\\\n94 & 0.25 & 0.18 & 0.09 & 0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Language Zero-Shot AUROC (Qwen3-235B)}\n\\label{app:per_lang_auroc}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-language zero-shot AUROC at best-transfer layer (L52) on Qwen3-235B.}\n\\label{tab:per_lang_auroc}\n\\small\n\\begin{tabular}{llc||llc}\n\\toprule\nLang & Tier & AUROC & Lang & Tier & AUROC \\\\\n\\midrule\nzh & HIGH & 0.77 & tr & MID & 0.71 \\\\\nes & HIGH & 0.76 & ru & MID & 0.74 \\\\\nfr & HIGH & 0.76 & vi & MID & 0.70 \\\\\nde & HIGH & 0.77 & th & MID & 0.69 \\\\\nja & HIGH & 0.75 & sw & LOW & 0.63 \\\\\nnl & HIGH & 0.76 & bn & LOW & 0.65 \\\\\npt & MID  & 0.75 & yo & LOW & 0.57 \\\\\nit & MID  & 0.75 & ig & LOW & 0.61 \\\\\nar & MID  & 0.73 & te & LOW & 0.58 \\\\\nhi & MID  & 0.71 & & & \\\\\nko & MID  & 0.72 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Projection Saturation by Resource Tier}\n\\label{app:proj_saturation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Procrustes alignment saturation by resource tier.}\n\\label{tab:proj_saturation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTier & Pairs to 90\\% & Pairs to 95\\% & Interpretation \\\\\n\\midrule\nHIGH & 15 & 22 & Low effective rank \\\\\nMID  & 25 & 38 & Moderate complexity \\\\\nLOW  & 35 & 48 & Complex rotation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "badb839d-99bc-483a-8f6a-097bbb8acefc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "ef992eae-18cb-465b-beea-5ac06751c207",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration transfer paper",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Assistant

_source line 27 · 2026-05-21T05:35:47.061Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef992eae-18cb-465b-beea-5ac06751c207",
  "isSidechain": false,
  "requestId": "req_011CbFAuBFBgvB7FiJQCxCpv",
  "type": "assistant",
  "uuid": "da962175-d741-48bd-ad8b-acb96651a430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsSGS4gufqxKyYH9vkbCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20410,
      "cache_read_input_tokens": 54779,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 54779,
          "cache_creation_input_tokens": 20410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20410
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

_source line 28 · 2026-05-21T05:35:48.364Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019VZqS3Zjjw1rLEUrbcA71S`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da962175-d741-48bd-ad8b-acb96651a430",
  "isSidechain": false,
  "requestId": "req_011CbFAuBFBgvB7FiJQCxCpv",
  "type": "assistant",
  "uuid": "547dc145-bce1-47ee-96fa-ba04e5eee41b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsSGS4gufqxKyYH9vkbCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20410,
      "cache_read_input_tokens": 54779,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 54779,
          "cache_creation_input_tokens": 20410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20410
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

_source line 29 · 2026-05-21T05:35:49.522Z_

<details><summary>↩ Tool result · `toolu_019VZqS3Zjjw1rLEUrbcA71S`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
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

LaTeX Warning: Citation `joshi2024llm' on page 1 undefined on input line 39.


LaTeX Warning: Citation `zhou2024lace' on page 1 undefined on input line 39.


LaTeX Warning: Citation `miao2026coral' on page 1 undefined on input line 39.


LaTeX Warning: Citation `miao2026steering' on page 1 undefined on input line 39
.


LaTeX Warning: Citation `xiao2025crosslingual' on page 1 undefined on input lin
e 41.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (6.78914pt too wide) in paragraph at lines 48--49
[]\OT1/cmr/bx/n/10.95 Decomposition anal-y-sis. \OT1/cmr/m/n/10.95 We de-com-po
se cor-rect-ness into difficulty-shared and capability-

LaTeX Warning: Citation `miao2026coral' on page 2 undefined on input line 60.


LaTeX Warning: Citation `miao2026steering' on page 2 undefined on input line 60
.


LaTeX Warning: Citation `ji2024llm' on page 2 undefined on input line 60.


LaTeX Warning: Citation `ji2024llm' on page 2 undefined on input line 60.


LaTeX Warning: Citation `xiao2025crosslingual' on page 2 undefined on input lin
e 63.


LaTeX Warning: Citation `civelli2024crosslingual' on page 2 undefined on input 
line 63.


LaTeX Warning: Citation `conneau2018word' on page 2 undefined on input line 66.



LaTeX Warning: Citation `artetxe2018robust' on page 2 undefined on input line 6
6.


LaTeX Warning: Citation `kornblith2019similarity' on page 2 undefined on input 
line 69.


LaTeX Warning: Citation `raghu2017svcca' on page 2 undefined on input line 69.


LaTeX Warning: Citation `bendavid2010theory' on page 2 undefined on input line 
72.


LaTeX Warning: Citation `zhao2019learning' on page 2 undefined on input line 72
.


Overfull \hbox (3.2219pt too wide) in paragraph at lines 72--73
\OT1/cmr/m/n/10.95 differ---directly rel-e-vant to un-der-stand-ing why Ca-CLR'
s MMD-based match-ing pro-vides bounded
[2]

LaTeX Warning: Citation `angelopoulos2023conformal' on page 3 undefined on inpu
t line 75.


LaTeX Warning: Reference `sec:method:caclr' on page 3 undefined on input line 8
9.


LaTeX Warning: Reference `sec:probe_complexity' on page 3 undefined on input li
ne 91.


LaTeX Warning: Reference `sec:cka' on page 3 undefined on input line 108.


LaTeX Warning: Citation `civelli2024crosslingual' on page 3 undefined on input 
line 113.

[3]
Overfull \hbox (0.65135pt too wide) in paragraph at lines 144--153
 [][] 

LaTeX Warning: Reference `sec:quant' on page 4 undefined on input line 155.


LaTeX Warning: Reference `sec:extended' on page 4 undefined on input line 159.


LaTeX Warning: Reference `sec:cross_benchmark' on page 4 undefined on input lin
e 159.


LaTeX Warning: Reference `tab:qwen_pareto' on page 4 undefined on input line 17
0.

[4]

LaTeX Warning: Reference `tab:llama_pareto' on page 5 undefined on input line 2
02.


LaTeX Warning: Reference `tab:arch_compare' on page 5 undefined on input line 2
30.


LaTeX Warning: Reference `tab:transfer_conditions' on page 5 undefined on input
 line 252.

[5]

LaTeX Warning: Reference `tab:simpson' on page 6 undefined on input line 279.


LaTeX Warning: Reference `tab:per_layer_cka' on page 6 undefined on input line 
302.


LaTeX Warning: Reference `tab:subspace' on page 6 undefined on input line 328.

[6]

LaTeX Warning: Reference `tab:decomposition' on page 7 undefined on input line 
354.


LaTeX Warning: Reference `tab:cap_by_depth' on page 7 undefined on input line 3
72.


LaTeX Warning: Reference `tab:beta_sweep' on page 7 undefined on input line 399
.

[7]

LaTeX Warning: Reference `tab:caclr_compare' on page 8 undefined on input line 
424.


LaTeX Warning: Reference `tab:caclr_depth' on page 8 undefined on input line 44
7.


LaTeX Warning: Reference `tab:proj_efficiency' on page 8 undefined on input lin
e 475.


LaTeX Warning: Reference `tab:procrustes_reversal' on page 8 undefined on input
 line 497.


LaTeX Warning: Reference `sec:cka' on page 8 undefined on input line 497.

[8]

LaTeX Warning: Citation `hewitt2019designing' on page 9 undefined on input line
 522.


LaTeX Warning: Reference `tab:control_selectivity' on page 9 undefined on input
 line 522.


LaTeX Warning: Reference `tab:artifact_rates' on page 9 undefined on input line
 541.


LaTeX Warning: Citation `xiao2025crosslingual' on page 9 undefined on input lin
e 561.


LaTeX Warning: Citation `miao2026steering' on page 9 undefined on input line 56
8.


LaTeX Warning: Reference `tab:ortho' on page 9 undefined on input line 568.


LaTeX Warning: Reference `tab:probe_complexity' on page 9 undefined on input li
ne 596.

[9]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:cross_bench' on page 10 undefined on input line 6
16.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:quant' on page 10 undefined on input line 637.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:three_arch' on page 10 undefined on input line 66
6.

[10]

LaTeX Warning: Reference `tab:extended' on page 11 undefined on input line 671.



LaTeX Warning: `h' float specifier changed to `ht'.

[11] [12]

LaTeX Warning: Reference `tab:per_lang_rho' on page 13 undefined on input line 
808.

[13]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:cka_heatmap' on page 14 undefined on input line 8
46.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[14] [15] [16] (./paper.aux)

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
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (16 pages, 239931 bytes).
Transcript written on paper.log.
LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[14] [15] [16] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (16 pages, 244543 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "547dc145-bce1-47ee-96fa-ba04e5eee41b",
  "isSidechain": false,
  "promptId": "933d6abc-22b2-439d-86e5-88087e8e3a89",
  "type": "user",
  "uuid": "72b9ec48-3211-4d58-a0a6-a8ff57b7b85b",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `joshi2024llm' on page 1 undefined on input line 39.\n\n\nLaTeX Warning: Citation `zhou2024lace' on page 1 undefined on input line 39.\n\n\nLaTeX Warning: Citation `miao2026coral' on page 1 undefined on input line 39.\n\n\nLaTeX Warning: Citation `miao2026steering' on page 1 undefined on input line 39\n.\n\n\nLaTeX Warning: Citation `xiao2025crosslingual' on page 1 undefined on input lin\ne 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (6.78914pt too wide) in paragraph at lines 48--49\n[]\\OT1/cmr/bx/n/10.95 Decomposition anal-y-sis. \\OT1/cmr/m/n/10.95 We de-com-po\nse cor-rect-ness into difficulty-shared and capability-\n\nLaTeX Warning: Citation `miao2026coral' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Citation `miao2026steering' on page 2 undefined on input line 60\n.\n\n\nLaTeX Warning: Citation `ji2024llm' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Citation `ji2024llm' on page 2 undefined on input line 60.\n\n\nLaTeX Warning: Citation `xiao2025crosslingual' on page 2 undefined on input lin\ne 63.\n\n\nLaTeX Warning: Citation `civelli2024crosslingual' on page 2 undefined on input \nline 63.\n\n\nLaTeX Warning: Citation `conneau2018word' on page 2 undefined on input line 66.\n\n\n\nLaTeX Warning: Citation `artetxe2018robust' on page 2 undefined on input line 6\n6.\n\n\nLaTeX Warning: Citation `kornblith2019similarity' on page 2 undefined on input \nline 69.\n\n\nLaTeX Warning: Citation `raghu2017svcca' on page 2 undefined on input line 69.\n\n\nLaTeX Warning: Citation `bendavid2010theory' on page 2 undefined on input line \n72.\n\n\nLaTeX Warning: Citation `zhao2019learning' on page 2 undefined on input line 72\n.\n\n\nOverfull \\hbox (3.2219pt too wide) in paragraph at lines 72--73\n\\OT1/cmr/m/n/10.95 differ---directly rel-e-vant to un-der-stand-ing why Ca-CLR'\ns MMD-based match-ing pro-vides bounded\n[2]\n\nLaTeX Warning: Citation `angelopoulos2023conformal' on page 3 undefined on inpu\nt line 75.\n\n\nLaTeX Warning: Reference `sec:method:caclr' on page 3 undefined on input line 8\n9.\n\n\nLaTeX Warning: Reference `sec:probe_complexity' on page 3 undefined on input li\nne 91.\n\n\nLaTeX Warning: Reference `sec:cka' on page 3 undefined on input line 108.\n\n\nLaTeX Warning: Citation `civelli2024crosslingual' on page 3 undefined on input \nline 113.\n\n[3]\nOverfull \\hbox (0.65135pt too wide) in paragraph at lines 144--153\n [][] \n\nLaTeX Warning: Reference `sec:quant' on page 4 undefined on input line 155.\n\n\nLaTeX Warning: Reference `sec:extended' on page 4 undefined on input line 159.\n\n\nLaTeX Warning: Reference `sec:cross_benchmark' on page 4 undefined on input lin\ne 159.\n\n\nLaTeX Warning: Reference `tab:qwen_pareto' on page 4 undefined on input line 17\n0.\n\n[4]\n\nLaTeX Warning: Reference `tab:llama_pareto' on page 5 undefined on input line 2\n02.\n\n\nLaTeX Warning: Reference `tab:arch_compare' on page 5 undefined on input line 2\n30.\n\n\nLaTeX Warning: Reference `tab:transfer_conditions' on page 5 undefined on input\n line 252.\n\n[5]\n\nLaTeX Warning: Reference `tab:simpson' on page 6 undefined on input line 279.\n\n\nLaTeX Warning: Reference `tab:per_layer_cka' on page 6 undefined on input line \n302.\n\n\nLaTeX Warning: Reference `tab:subspace' on page 6 undefined on input line 328.\n\n[6]\n\nLaTeX Warning: Reference `tab:decomposition' on page 7 undefined on input line \n354.\n\n\nLaTeX Warning: Reference `tab:cap_by_depth' on page 7 undefined on input line 3\n72.\n\n\nLaTeX Warning: Reference `tab:beta_sweep' on page 7 undefined on input line 399\n.\n\n[7]\n\nLaTeX Warning: Reference `tab:caclr_compare' on page 8 undefined on input line \n424.\n\n\nLaTeX Warning: Reference `tab:caclr_depth' on page 8 undefined on input line 44\n7.\n\n\nLaTeX Warning: Reference `tab:proj_efficiency' on page 8 undefined on input lin\ne 475.\n\n\nLaTeX Warning: Reference `tab:procrustes_reversal' on page 8 undefined on input\n line 497.\n\n\nLaTeX Warning: Reference `sec:cka' on page 8 undefined on input line 497.\n\n[8]\n\nLaTeX Warning: Citation `hewitt2019designing' on page 9 undefined on input line\n 522.\n\n\nLaTeX Warning: Reference `tab:control_selectivity' on page 9 undefined on input\n line 522.\n\n\nLaTeX Warning: Reference `tab:artifact_rates' on page 9 undefined on input line\n 541.\n\n\nLaTeX Warning: Citation `xiao2025crosslingual' on page 9 undefined on input lin\ne 561.\n\n\nLaTeX Warning: Citation `miao2026steering' on page 9 undefined on input line 56\n8.\n\n\nLaTeX Warning: Reference `tab:ortho' on page 9 undefined on input line 568.\n\n\nLaTeX Warning: Reference `tab:probe_complexity' on page 9 undefined on input li\nne 596.\n\n[9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:cross_bench' on page 10 undefined on input line 6\n16.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:quant' on page 10 undefined on input line 637.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:three_arch' on page 10 undefined on input line 66\n6.\n\n[10]\n\nLaTeX Warning: Reference `tab:extended' on page 11 undefined on input line 671.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11] [12]\n\nLaTeX Warning: Reference `tab:per_lang_rho' on page 13 undefined on input line \n808.\n\n[13]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:cka_heatmap' on page 14 undefined on input line 8\n46.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[14] [15] [16] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (16 pages, 239931 bytes).\nTranscript written on paper.log.\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[14] [15] [16] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (16 pages, 244543 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "547dc145-bce1-47ee-96fa-ba04e5eee41b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-21T05:35:49.529Z_

```json
{
  "parentUuid": "72b9ec48-3211-4d58-a0a6-a8ff57b7b85b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bafe3124-dee4-475c-a3a7-b1e00687cd02",
  "timestamp": "2026-05-21T05:35:49.529Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-21T05:35:57.103Z_

编译成功，16 页 PDF，无错误。所有交叉引用在第二次编译后已解析。

产出：
- `paper.tex` — 完整 LaTeX 源码（Abstract / Introduction / Related Work / Method / Experimental Setup / Results 6 子节 / Additional Analysis 5 子节 / Discussion / Conclusion / Appendix 4 节）
- `paper.pdf` — 16 页编译产物

覆盖全部 13 个实验，包含 20+ 张表（主体 + 附录），每个定量 claim 均来自 `experiment_data.json`。四条因果链完整保留：Pareto → Decomposition → CaCLR → CKA Simpson's Paradox。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bafe3124-dee4-475c-a3a7-b1e00687cd02",
  "isSidechain": false,
  "requestId": "req_011CbFAuf6144sT2PVPm2FvE",
  "type": "assistant",
  "uuid": "c60b42ce-2798-426b-aa95-05530dd3bdeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmcX4m6srzqx5sZasYFUBP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5457,
      "cache_read_input_tokens": 75189,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5457,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 75189,
          "cache_creation_input_tokens": 5457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5457
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T044911 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "c60b42ce-2798-426b-aa95-05530dd3bdeb",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate cross-lingual calibration transfer paper",
  "sessionId": "93fd10ce-8877-4672-be96-d4a16ab6d261"
}
```

---
