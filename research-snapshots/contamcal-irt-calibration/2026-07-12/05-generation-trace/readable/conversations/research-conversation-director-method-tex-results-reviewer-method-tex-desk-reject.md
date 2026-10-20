# Research conversation: [Director 指令] **[紧急修复] method.tex 三个根本性问题 — 写 Results 前必须先改** Reviewer 发现 method.tex 描述的模型/信号与实际实验不匹配，属于 desk-reject 级问题

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/bc252caf-e2b6-4080-ba11-8234b25ce5fe.jsonl`
- **Structured JSON:** [`371823b75529b88b32b2.json`](../../sessions/37/371823b75529b88b32b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T02:37:25.072Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T02:37:25.072Z",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "content": "[Director 指令] **[紧急修复] method.tex 三个根本性问题 — 写 Results 前必须先改**\n\nReviewer 发现 method.tex 描述的模型/信号与实际实验不匹配，属于 desk-reject 级问题。\n\n**决策（不可商议）：**\n\n1. **Primary model = 2PL+γ**（不是 4PL+γ）\n   - 所有冻结数据用的是 2PL+γ\n   - 修改 method.tex：2PL+γ 作为主要呈现，4PL 可作为 \"general framework\" 一句带过或放 appendix\n   - 校准公式、先验、所有引用 c_j/d_j 的地方都要改\n   - writing_plan 已经写了 \"2PL+γ as primary\"，method.tex 必须对齐\n\n2. **Signal 数量 = 3**（不是 4）\n   - 删除 ConStat (s3) 作为实际使用信号的描述\n   - 可以在一句话中说 \"We initially considered ConStat but excluded it due to computational cost (requires per-item paraphrase generation at inference time)\"\n   - RRF 描述用 3 信号：s1_embedding + s2_minkpp + s4_selfcritique\n\n3. **删除 KDS ablation 声明**\n   - method.tex line 35 \"We include KDS in ablation experiments\" — 删除，无数据支撑\n   - 删除所有与 KDS 相关的描述\n\n**附带修复：**\n- 删除 RL 叙事过重的段落（我们没有 RL 实验，只有 Instruct 观测数据）\n- 删除 TODO 注释 (line 25)\n- **N≥50 threshold 存疑**：Fisher heatmap N=30 已达 power=1.0, bias=0.008。N≥50 可能太保守。暂时改为 \"N≥30 for high-AUC signals (AUC≥0.70)\"，等 N50 数据跑完后再决定最终表述。\n\n先修 method.tex + introduction.tex（4→3 signals 的地方），然后再继续 Results。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T02:37:25.079Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T02:37:25.079Z",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-17T02:37:25.138Z_

[Director 指令] **[紧急修复] method.tex 三个根本性问题 — 写 Results 前必须先改**

Reviewer 发现 method.tex 描述的模型/信号与实际实验不匹配，属于 desk-reject 级问题。

**决策（不可商议）：**

1. **Primary model = 2PL+γ**（不是 4PL+γ）
   - 所有冻结数据用的是 2PL+γ
   - 修改 method.tex：2PL+γ 作为主要呈现，4PL 可作为 "general framework" 一句带过或放 appendix
   - 校准公式、先验、所有引用 c_j/d_j 的地方都要改
   - writing_plan 已经写了 "2PL+γ as primary"，method.tex 必须对齐

2. **Signal 数量 = 3**（不是 4）
   - 删除 ConStat (s3) 作为实际使用信号的描述
   - 可以在一句话中说 "We initially considered ConStat but excluded it due to computational cost (requires per-item paraphrase generation at inference time)"
   - RRF 描述用 3 信号：s1_embedding + s2_minkpp + s4_selfcritique

3. **删除 KDS ablation 声明**
   - method.tex line 35 "We include KDS in ablation experiments" — 删除，无数据支撑
   - 删除所有与 KDS 相关的描述

**附带修复：**
- 删除 RL 叙事过重的段落（我们没有 RL 实验，只有 Instruct 观测数据）
- 删除 TODO 注释 (line 25)
- **N≥50 threshold 存疑**：Fisher heatmap N=30 已达 power=1.0, bias=0.008。N≥50 可能太保守。暂时改为 "N≥30 for high-AUC signals (AUC≥0.70)"，等 N50 数据跑完后再决定最终表述。

先修 method.tex + introduction.tex（4→3 signals 的地方），然后再继续 Results。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "a6983a05-d70c-4ced-aa41-7554d6ca878a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T02:37:25.137Z_

```json
{
  "parentUuid": "a6983a05-d70c-4ced-aa41-7554d6ca878a",
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9e196a0f-efc7-48bc-8992-0cdd993e619f",
  "timestamp": "2026-05-17T02:37:25.137Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T02:37:25.137Z_

```json
{
  "parentUuid": "9e196a0f-efc7-48bc-8992-0cdd993e619f",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "112f2efe-54e9-40b9-8553-99a9628b9b00",
  "timestamp": "2026-05-17T02:37:25.137Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T02:37:25.137Z_

```json
{
  "parentUuid": "112f2efe-54e9-40b9-8553-99a9628b9b00",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0552b78f-79a1-492d-a80d-89cccb6da662",
  "timestamp": "2026-05-17T02:37:25.137Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
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
  "aiTitle": "Fix method.tex: 2PL model, 3 signals, remove KDS ablation",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---

### Assistant

_source line 8 · 2026-05-17T02:37:30.705Z_

<details><summary>Logged reasoning block</summary>

```text
Director 指令要求修复 method.tex 的三个根本性问题，属于 Patch 模式（已存在 .tex 文件）。让我先理解变更，然后执行修改。

需要做的：
1. 读取当前 method.tex
2. 读取 introduction.tex（检查 4→3 signals 的引用）
3. 读取 writing_plan.yaml 确认上下文
4. 执行修改

按 Patch 流水线 Phase A — 理解变更，先读取相关文件。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0552b78f-79a1-492d-a80d-89cccb6da662",
  "isSidechain": false,
  "requestId": "req_011Cb7N4vu1xjnERe8vL1vDi",
  "type": "assistant",
  "uuid": "e18ffda4-5f46-4a19-afb3-e8278da8b4ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXxrDEJRt3PRaRCo2jbkQA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21745,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21745
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

_source line 9 · 2026-05-17T02:37:31.709Z_

收到，Patch 模式启动。Phase A — 理解变更范围。先读取 method.tex 和 introduction.tex。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e18ffda4-5f46-4a19-afb3-e8278da8b4ef",
  "isSidechain": false,
  "requestId": "req_011Cb7N4vu1xjnERe8vL1vDi",
  "type": "assistant",
  "uuid": "e29d23ed-cc09-4682-94f5-805b251f5fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXxrDEJRt3PRaRCo2jbkQA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21745,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21745
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

_source line 10 · 2026-05-17T02:37:33.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PX3MRFYpaGFbNkK8PBqkVN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e29d23ed-cc09-4682-94f5-805b251f5fbf",
  "isSidechain": false,
  "requestId": "req_011Cb7N4vu1xjnERe8vL1vDi",
  "type": "assistant",
  "uuid": "a6f22d54-d6bc-4247-a36d-17f5429e1e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXxrDEJRt3PRaRCo2jbkQA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21745,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21745
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

_source line 11 · 2026-05-17T02:37:33.317Z_

<details><summary>↩ Tool result · reported error · `toolu_01PX3MRFYpaGFbNkK8PBqkVN`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6f22d54-d6bc-4247-a36d-17f5429e1e1d",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "49bda372-6e0e-4a49-b854-5589551a3e2a",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.",
  "sourceToolAssistantUUID": "a6f22d54-d6bc-4247-a36d-17f5429e1e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T02:37:34.459Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XuY9hkybquFeJz8gtTCDkc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bda372-6e0e-4a49-b854-5589551a3e2a",
  "isSidechain": false,
  "requestId": "req_011Cb7N4vu1xjnERe8vL1vDi",
  "type": "assistant",
  "uuid": "dae30287-e29c-43b6-b7d1-6d91df062504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXxrDEJRt3PRaRCo2jbkQA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21745,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21745
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

_source line 13 · 2026-05-17T02:37:34.467Z_

<details><summary>↩ Tool result · reported error · `toolu_01XuY9hkybquFeJz8gtTCDkc`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dae30287-e29c-43b6-b7d1-6d91df062504",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "14ee9c4d-d24b-41e6-9fdf-8ee33ebb0d69",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.",
  "sourceToolAssistantUUID": "dae30287-e29c-43b6-b7d1-6d91df062504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T02:37:34.561Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UCNBFBvpbum5KvPTKA6vsZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ee9c4d-d24b-41e6-9fdf-8ee33ebb0d69",
  "isSidechain": false,
  "requestId": "req_011Cb7N4vu1xjnERe8vL1vDi",
  "type": "assistant",
  "uuid": "3a23b168-8225-4f69-9e84-5440ae829c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXxrDEJRt3PRaRCo2jbkQA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21745,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21745
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

_source line 15 · 2026-05-17T02:37:34.695Z_

<details><summary>↩ Tool result · `toolu_01UCNBFBvpbum5KvPTKA6vsZ`</summary>

```text
1	## writing_plan.yaml — contamcal-irt-calibration
2	## Generated: 2026-05-16 | Paper Agent Step 1 (REFRAME D118/D119/D120)
3	## Status: PENDING_APPROVAL
4	
5	meta:
6	  venue: "EMNLP 2026 ARR May 25"
7	  track: "Machine Learning for NLP / Resources and Evaluation"
8	  deadline: "2026-05-25"
9	  days_remaining: 9
10	  page_limit: 8  # + unlimited appendix
11	  template: "acl_latex (ARR format)"
12	  template_note: "Use acl-style-files from github.com/acl-org/acl-style-files"
13	  special_theme: "New Missions for NLP Research"
14	  framing_doc: "paper_framing.md (D118/D119/D120 reframe: diagnostic-led)"
15	  total_word_budget: 5800
16	  review_round: 1
17	  target_score: "Weak Reject → Weak Accept"
18	
19	title: >
20	  Domain-Differential Contamination Effects:
21	  Diagnosis via Item Response Theory
22	
23	core_claims:
24	  C1:
25	    name: "Characterization (PRIMARY)"
26	    summary: >
27	      MMLU domain heterogeneity: Math γ=0.97, Science γ=0.84 (significant, PPP acceptable);
28	      pooled γ≈0 is dilution masking (D119), NOT absence of effect.
29	      Cross-benchmark: ARC forgetting (γ<0) vs GSM8K inflation (γ>0).
30	      Scale-dependent: 0.5B catastrophic → 3B mild → 7B negligible.
31	    evidence: [exp-006, exp-001]
32	    key_data: "Domain IRT N=24 (MMLU 8 domains), per-benchmark IRT"
33	    priority: 1
34	  C2:
35	    name: "Signal Failure (CO-PRIMARY)"
36	    summary: >
37	      Min-K++ directional reversal (Cohen's d = -1.55 to -1.98).
38	      Cross-family replication: Qwen + Llama both exhibit reversal.
39	      S1 embedding only reliable signal (AUC>0.95 at d005).
40	      RRF degrades to S1-only in practice.
41	    evidence: [exp-008, exp-002]
42	    key_data: "Signal eval 0.5B/1.5B/3B, Llama cross-family (exploratory N=4)"
43	    priority: 1
44	  C3:
45	    name: "Identifiability"
46	    summary: >
47	      Fisher Info: recovery succeeds down to AUC=0.55 (lowest tested) at N≥50.
48	      CI width ∝ N^{-0.48}. LLM eval N=8-30 creates domain-method mismatch.
49	      Triple impossibility limited to "IRT + membership-inference specific" (C3 fix).
50	    evidence: [exp-004]
51	    key_data: "Sim sweep 20 conditions × 200 runs"
52	    priority: 2
53	  C4:
54	    name: "Conditional Calibration (DEMOTED)"
55	    summary: >
56	      KEY FINDING: vanilla 2PL ≈ 2PL+γ on calibration MAE (GSM8K: 0.0063 vs 0.0062;
57	      MMLU: 0.0068 vs 0.0070; ARC: 0.0158 vs 0.0201). γ does NOT improve calibration.
58	      Calibration improvement entirely from IRT ability estimation (θ separation from noise).
59	      γ value is DIAGNOSTIC (domain-level heterogeneity detection), not calibration.
60	      Gating criterion: γ significant + PPP∈[0.1,0.9] + calibrated MAE < raw MAE.
61	      ARC MAE=0.035 (passes). GSM8K overcorrection 11× (fails gating → honest negative).
62	      D120: calibration value decomposition — all calibration benefit from θ, not γ.
63	    evidence: [exp-006]
64	    priority: 3
65	    narrative_constraint: >
66	      NEVER imply γ brings calibration improvement. Two distinct values:
67	      (a) IRT framework → calibration (robust θ estimation even without γ);
68	      (b) γ → domain-level diagnosis (which domains inflated/deflated, direction, magnitude).
69	      This STRENGTHENS the diagnostic framing (D118).
70	
71	paper_outline:
72	  abstract:
73	    word_budget: 200
74	    dependencies: [introduction, results, conclusion]
75	    key_numbers: ["MMLU Math γ=0.97", "dilution masking pooled γ≈0", "Min-K++ Cohen's d=-1.55 to -1.98", "ARC MAE=0.035", "N≥50 threshold"]
76	    notes: "Diagnostic framing. Lead with domain heterogeneity + dilution masking. Signal failure as co-primary."
77	
78	  introduction:
79	    word_budget: 850
80	    dependencies: [method, results]
81	    subsections:
82	      - "Problem: contamination undermines benchmark reliability; aggregate metrics mask heterogeneous effects"
83	      - "Gap: detection methods flag but don't diagnose or calibrate; mitigation provably fails (Emperor's)"
84	      - "Our approach: IRT-based diagnostic framework revealing domain-differential effects"
85	      - "4 contributions: (1) domain heterogeneity + dilution masking, (2) signal failure, (3) identifiability bounds, (4) conditional calibration"
86	    notes: "D118: 'diagnostic findings + conditional calibration' framing. D119: dilution masking replaces Simpson's Paradox."
87	
88	  related_work:
89	    word_budget: 700
90	    dependencies: [literature_map]
91	    subsections:
92	      - "Contamination detection (Min-K++, ConStat, KDS, CDD, Self-Critique)"
93	      - "IRT for LLM evaluation (Lalor, TinyBenchmarks, Growing Pains, HiBayES)"
94	      - "Item compromise in educational measurement (Eckerly, Sinharay, DIF)"
95	      - "Contamination mitigation + DCR qualitative comparison (W1 fix)"
96	      - "Calibration disambiguation"
97	    notes: "W1: expand DCR comparison (qualitative table). Cite TED/CDD as closest competitors."
98	
99	  method:
100	    word_budget: 1100
101	    dependencies: []
102	    subsections:
103	      - name: "3.1 Problem Formulation"
104	        content: "Given model j, benchmark k with items i. Goal: diagnose contamination effects at domain level + estimate θ_j^clean. Three IRT adaptations."
105	      - name: "3.2 Stage 1: Multi-Signal Exposure Mapping"
106	        content: "4 signals (S1-S4), RRF aggregation. Meta-circularity argument. Note S2/S4 failure modes."
107	      - name: "3.3 Stage 2: Contamination-Augmented IRT"
108	        content: "2PL+γ model: P(y=1) = 1/(1+exp(-a_i(θ_j - b_i + γ_k·e_ij))). Per-domain γ_k within benchmark. Stan NUTS."
109	      - name: "3.4 Fisher Information and Identifiability"
110	        content: "Derive I(γ). AUC=0.55 structural, N≥50 practical. CI width scaling. Domain-method mismatch."
111	      - name: "3.5 Calibration Value Decomposition (D120/D121)"
112	        content: >
113	          ALREADY WRITTEN in method.tex §3.4 as 'Calibration value decomposition' paragraph.
114	          Key message: vanilla 2PL ≈ 2PL+γ on calibration MAE (all benchmarks). Calibration
115	          benefit entirely from IRT θ estimation. γ provides diagnostic value only.
116	          Numbers: GSM8K 0.0063 vs 0.0062; MMLU 0.0068 vs 0.0070; ARC 0.0158 vs 0.0201.
117	    notes: "2PL+γ as primary model (domain-level). 4PL for MC benchmarks (ARC/MMLU). Full Fisher derivation in appendix."
118	
119	  experimental_setup:
120	    word_budget: 600
121	    dependencies: [method]
122	    subsections:
123	      - name: "4.1 Controlled SFT Injection"
124	        content: "Qwen2.5 (0.5B, 1.5B, 3B). 4 dosages (d000/d005/d025/d100). 2 seeds × 3 scales = N=24 models. LoRA alpha=32. QC-filtered injection."
125	      - name: "4.2 Cross-Family Analysis"
126	        content: >
127	          Llama-3.2-3B: d000 + d005/d025/d100 (single seed, N=4 additional). Exploratory.
128	          PURPOSE: test family-specificity of contamination patterns, NOT confirm generalizability.
129	          D123: Llama d100 MMLU excluded (catastrophic collapse, all output 'A', acc=0.34).
130	          Effective Llama MMLU range: d000-d025. ARC/GSM8K d100 normal.
131	          REQUIRED power analysis: Use Qwen N=24 γ effect sizes as reference
132	          (Math γ=0.97, GSM8K γ≈0.06). Compute statistical power at N=4 for each.
133	          Cross-family IRT pooling FINAL v3 CLEAN (replaces all prior versions):
134	            Pooled (Qwen+Llama):
135	              - ARC (N=20): γ=0.002, CI=[-0.57, 0.60], PPP=0.449, calMAE=0.015, ΔMAE=0.055
136	              - MMLU (N=20): γ=0.213, CI=[-0.78, 1.25], PPP=0.865, calMAE=0.017, ΔMAE=0.028
137	              - GSM8K (N=28): γ=-0.110, CI=[-0.52, 0.28], PPP=0.832, calMAE=0.008, ΔMAE=0.171
138	            Qwen-only baseline:
139	              - ARC (N=16): γ=0.727, CI excludes zero
140	              - MMLU (N=16): γ=0.655, CI does NOT exclude zero
141	              - GSM8K (N=24): γ=0.064, CI does NOT exclude zero
142	            KEY NARRATIVE NUMBER: ARC γ = 0.73 → 0.002 (strongest family-specificity evidence)
143	            NOTE: v2 MMLU γ=0.71 was WRONG (RRF missing s4). Correct value = 0.213.
144	          THREE-LAYER FRAMING:
145	            (1) IRT calibration generalizes cross-family (calMAE low, ΔMAE large) — STRONGEST claim
146	            (2) γ diagnostic value only within-family (Qwen: Math 0.97, Science 0.84; pooled: γ≈0)
147	            (3) Family-specificity itself is diagnostic (different families react differently to SFT)
148	          RED LINES:
149	            ✅ "IRT calibration generalizes across model families"
150	            ✅ "γ provides within-family contamination diagnostics"
151	            ✅ "cross-family analysis reveals family-specific contamination mechanisms"
152	            ❌ "cross-family validation confirms contamination detection"
153	            ❌ "γ is a universal contamination indicator"
154	      - name: "4.3 Benchmarks, Domains, and Evaluation"
155	        content: "MMLU (57 subjects → 8 cognitive domains), ARC-C (1172 items), GSM8K (1319 items). 6 metrics. Domain stratification strategy."
156	      - name: "4.4 Baselines"
157	        content: "7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR."
158	    notes: "D045: 0.5B MMLU/ARC excluded from IRT (position bias). 3B data FROZEN and available."
159	
160	  results:
161	    word_budget: 1500
162	    dependencies: [experimental_setup, figures, tables]
163	    subsections:
164	      - name: "5.1 Domain-Differential Contamination (C1)"
165	        content: >
166	          MMLU domain heterogeneity: Math γ=0.97, Science γ=0.84, CS_Eng≈0, non-STEM PPP=1 (model misfit).
167	          Dilution masking (D119): pooled γ≈0 because positive STEM effects diluted by null/misfit non-STEM.
168	          Cross-benchmark: ARC γ<0 (forgetting), GSM8K γ>0 (inflation).
169	          Scale story: 0.5B catastrophic → 3B mild.
170	          Cross-family analysis (D122 v3 FINAL CLEAN):
171	            Pooling Qwen+Llama → γ vanishes on ALL benchmarks:
172	              ARC: 0.73→0.002; MMLU: 0.655→0.213; GSM8K: 0.064→-0.110 (all CI include zero)
173	            Only ARC Qwen-only had CI excluding zero — pooling eliminates it completely.
174	            calMAE remains low (GSM8K 0.008, ARC 0.015, MMLU 0.017) with large ΔMAE.
175	            Three-layer conclusion: (1) θ calibration cross-family valid, (2) γ within-family only,
176	            (3) family-specificity is itself a diagnostic finding.
177	            Llama d100 ARC acc=0.60 (no inflation despite contamination) vs Qwen pattern → different mechanisms.
178	        claims: [C1]
179	        key_tables: [table_domain_gamma]
180	        key_figures: [fig_domain_gamma, fig_dose_response]
181	      - name: "5.2 Detection Signal Failure (C2)"
182	        content: >
183	          S1 AUC>0.95 at d005. Min-K++ reversal Cohen's d=-1.55 to -1.98.
184	          Cross-family signal: Llama-3.2-3B replicates Min-K++ reversal direction (exploratory, N=4).
185	          RRF = S1-only in practice.
186	          NOTE (D122): Cross-family γ pooling shows family-specificity (§5.1 cross-ref).
187	          Signal direction replicates, but γ magnitude is family-specific.
188	        claims: [C2]
189	        key_figures: [fig_signal_heatmap]
190	      - name: "5.3 Identifiability Boundaries (C3)"
191	        content: >
192	          Sim sweep: recovery at AUC=0.55 (lowest tested), N≥50. CI ∝ N^{-0.48}.
193	          LLM eval operates at N=8-30: IRT-specific impossibility (not general impossibility).
194	          Fisher Info N×identifiability heatmap.
195	        claims: [C3]
196	        key_figures: [fig_identifiability_heatmap]
197	      - name: "5.4 Conditional Calibration (C4)"
198	        content: >
199	          KEY NARRATIVE: Show vanilla 2PL baseline alongside 2PL+γ. Explicitly state γ does NOT
200	          improve calibration (GSM8K: 0.0063 vs 0.0062; MMLU: 0.0068 vs 0.0070; ARC: 0.0158 vs 0.0201).
201	          Calibration benefit entirely from IRT ability estimation.
202	          γ value is DIAGNOSTIC: domain-differential heterogeneity detection (§5.1).
203	          ARC: MAE=0.035, Kendall τ=0.756, beats all baselines.
204	          GSM8K: gating criterion fails (γ non-significant with S1). Overcorrection as honest negative.
205	          Coverage below nominal: directional indicators, not precise CIs.
206	          Frame positively: this confirms D118 "Diagnosis via IRT" — γ reveals hidden structure
207	          that aggregate calibration cannot, strengthening the diagnostic contribution.
208	        claims: [C4]
209	        key_tables: [table_baselines]
210	        key_figures: [fig_calibration]
211	        narrative_constraint: "NEVER imply γ improves calibration numbers. Show vanilla 2PL as explicit comparison."
212	    notes: "All sections use FROZEN data (3B included). Llama marked 'exploratory'."
213	
214	  discussion:
215	    word_budget: 500
216	    dependencies: [results]
217	    subsections:
218	      - "Dilution masking implications: aggregate benchmark scores as unreliable contamination indicators"
219	      - "Non-STEM model misfit: boundary of additive γ formulation → future multidimensional IRT"
220	      - "Limitations: single primary family (Qwen2.5), SFT ≠ real contamination, N<50 in practice"
221	      - "0.5B position bias (D045): capacity threshold for MC evaluation"
222	      - name: "SFT ≠ real contamination (W6, expanded with D123)"
223	        content: >
224	          Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34) while
225	          ARC/GSM8K d100 behave normally. Format-specific: 100% SFT on MC items causes
226	          format overfitting (position bias collapse), not present in open-ended (GSM8K)
227	          or mixed-format (ARC). This artifact would not occur in natural contamination
228	          (gradual, heterogeneous sources). Brief mention, not core claim.
229	          Also supports capacity × format interaction for Min-K++ reversal explanation.
230	      - "Future work: multi-family, 7B+, RL observational, data attribution signals"
231	    notes: "Honest about scope. C3 impossibility limited to IRT+MIA framework."
232	
233	  conclusion:
234	    word_budget: 350
235	    dependencies: [discussion]
236	    notes: >
237	      Restate: diagnostic framework reveals hidden structure. Dilution masking as key insight.
238	      IRT provides calibration via θ estimation; γ provides domain-level diagnosis.
239	      These are complementary, independent values. Honest about γ's non-contribution to calibration numbers.
240	
241	  appendix:
242	    sections:
243	      - name: "A: Fisher Information Derivation"
244	        source: "artifacts/fisher_info_derivation/fisher_info_appendix.tex"
245	      - name: "B: Simulation Sweep Full Results"
246	        data_source: "exp-004"
247	      - name: "C: Measurement Error Analysis (Negative)"
248	        data_source: "exp-005"
249	      - name: "D: 0.5B Position Bias Analysis"
250	        data_source: "exp-001"
251	      - name: "E: Llama Cross-Family Analysis + Power Analysis"
252	        notes: >
253	          Single seed N=4. Post-hoc power. Exploratory status.
254	          D122: Report pooled γ results honestly (GSM8K γ≈0; ARC γ=0.55 CI crosses zero, PPP=0.024).
255	          Frame as family-specificity evidence, not failure. Compare Qwen-only vs pooled.
256	          IRT θ valid cross-family; γ family-specific → supports per-family modeling recommendation.
257	      - name: "F: DCR Qualitative Comparison Table (W1)"
258	        notes: "Feature-by-feature comparison with DCR. No head-to-head numbers (no code access)."
259	      - name: "G: Full Domain-Level IRT Diagnostics"
260	        notes: "All 8 MMLU domains: γ, CI, PPP, Rhat, ESS. Non-STEM misfit discussion."
261	
262	visualization_plan:
263	  fig_pipeline:
264	    type: "conceptual_diagram"
265	    description: "ContamCal 2-stage diagnostic pipeline. Emphasize 'diagnosis' framing: signals → domain-level IRT → characterization + conditional calibration."
266	    placement: "Section 3 (Method)"
267	    aspect_ratio: "2:1"
268	    tool: "matplotlib"
269	    data_source: null
270	    output: "figures/paper/fig_pipeline.pdf"
271	    status: "DONE (may need minor label update for 'diagnosis' framing)"
272	
273	  fig_domain_gamma:
274	    type: "bar_chart_with_ci"
275	    description: >
276	      NEW (flagship C1 figure). MMLU domain-level γ estimates.
277	      X-axis: 8 MMLU domains (ordered by γ: Math > Science > CS_Eng > ... > non-STEM).
278	      Y-axis: γ estimate. Error bars = 95% CI.
279	      Color: green (significant + PPP OK) / gray (non-significant) / red (PPP=1, model misfit).
280	      Horizontal dashed line at γ=0. Annotate pooled γ≈0 with "dilution masking" label.
281	    placement: "Section 5.1 (flagship)"
282	    aspect_ratio: "3:2"
283	    tool: "matplotlib"
284	    data_source: "registry: exp-006 domain-level IRT N=24 (Math/Science/CS_Eng/non-STEM domains)"
285	    output: "figures/paper/fig_domain_gamma.pdf"
286	
287	  fig_dose_response:
288	    type: "line_plot"
289	    description: >
290	      Dosage vs accuracy for ARC, GSM8K, MMLU. NOW WITH 3B DATA (3B FROZEN).
291	      Three scales: 0.5B, 1.5B, 3B. Error bars from 2 seeds.
292	      Shows scale-dependence + benchmark-dependence.
293	    placement: "Section 5.1"
294	    aspect_ratio: "3:2"
295	    tool: "matplotlib"
296	    data_source: "registry: exp-001 eval results (aligned, all scales × dosages × seeds)"
297	    output: "figures/paper/fig_dose_response.pdf"
298	    status: "NEEDS REGENERATION (old version has [PENDING-3B], now 3B is FROZEN)"
299	
300	  fig_signal_heatmap:
301	    type: "heatmap"
302	    description: >
303	      Signal AUC × scale × dosage. Annotate Min-K++ reversal (Cohen's d).
304	      Include Llama cross-family row if data available (mark exploratory).
305	    placement: "Section 5.2"
306	    aspect_ratio: "4:3"
307	    tool: "matplotlib"
308	    data_source: "registry: exp-008 signal eval + Llama signals"
309	    output: "figures/paper/fig_signal_heatmap.pdf"
310	
311	  fig_identifiability_heatmap:
312	    type: "heatmap"
313	    description: >
314	      W4 fix: N (y-axis) × AUC (x-axis) → γ recovery quality (color = bias or RMSE).
315	      Mark actual operating points. Shade structural/practical identifiability regions.
316	      Replaces old 'phase diagram' — heatmap is more informative per reviewer.
317	    placement: "Section 5.3"
318	    aspect_ratio: "1:1"
319	    tool: "matplotlib"
320	    data_source: "registry: exp-004 sim_sweep (20 conditions, 200 runs)"
321	    output: "figures/paper/fig_identifiability_heatmap.pdf"
322	
323	  fig_calibration:
324	    type: "scatter_with_ci"
325	    description: >
326	      Calibrated vs true accuracy scatter. Include 3B data.
327	      MUST include vanilla 2PL baseline (separate marker/color) alongside 2PL+γ.
328	      Key visual: vanilla 2PL and 2PL+γ points nearly overlap, demonstrating
329	      calibration parity. Color by benchmark. Annotate ARC (good) vs GSM8K (overcorrection).
330	      Director note: "会增加 vanilla 2PL 对照条"
331	    placement: "Section 5.4"
332	    aspect_ratio: "1:1"
333	    tool: "matplotlib"
334	    data_source: "registry: exp-006 IRT calibration results (both vanilla 2PL and 2PL+γ)"
335	    output: "figures/paper/fig_calibration.pdf"
336	    status: "NEEDS REGENERATION (vanilla 2PL comparison added)"
337	
338	table_plan:
339	  table_domain_gamma:
340	    type: "parameter_summary"
341	    description: "Domain-level IRT γ estimates (MMLU 8 domains + ARC + GSM8K)"
342	    columns: ["Domain/Benchmark", "N_items", "γ̂", "95% CI", "Sig?", "PPP", "Interpretation"]
343	    data_source: "exp-006 domain-level IRT (N=24 models)"
344	    placement: "Section 5.1"
345	    rows:
346	      - "MMLU: Math — γ=+0.97, CI excludes 0, PPP=0.44, Strong inflation"
347	      - "MMLU: Science — γ=+0.84, CI excludes 0, PPP=0.81, Strong inflation"
348	      - "MMLU: CS_Eng — γ=+0.20, CI includes 0, PPP=0.89, Null"
349	      - "MMLU: Non-STEM (5 domains) — PPP≈1.0, Model misfit (see Appendix G)"
350	      - "MMLU: Pooled — γ≈0, dilution masking"
351	      - "ARC-Challenge — γ=-1.46, CI excludes 0, Forgetting"
352	      - "GSM8K — γ non-significant (S1), Inflation via oracle only"
353	      - "[3B rows from FROZEN data]"
354	
355	  table_baselines:
356	    type: "comparison"
357	    description: "Calibration performance: ContamCal vs 7 baselines + DCR qualitative"
358	    columns: ["Method", "ARC MAE↓", "ARC τ↑", "ARC C95%", "Notes"]
359	    data_source: "exp-006 baseline comparisons"
360	    placement: "Section 5.4"
361	    notes: "W1: add qualitative DCR comparison column. Include 3B data."
362	
363	  table_dcr_comparison:
364	    type: "qualitative"
365	    description: "W1 fix: DCR vs ContamCal feature comparison"
366	    columns: ["Feature", "DCR", "ContamCal"]
367	    placement: "Section 2 (Related Work) or Section 5.4"
368	    rows:
369	      - "Uncertainty quantification: ✗ / ✓ (Bayesian CIs)"
370	      - "Domain-level diagnosis: ✗ / ✓ (per-domain γ)"
371	      - "Identifiability analysis: ✗ / ✓ (Fisher Info)"
372	      - "Signal failure detection: ✗ / ✓ (Min-K++ reversal)"
373	      - "Adjusted accuracy: ✓ / ✓"
374	      - "Multi-benchmark: ✓ / ✓"
375	      - "Requires reference set: ✓ (fuzzy match) / ✗ (signal-based)"
376	
377	literature_strategy:
378	  citation_budget: "40-50 total"
379	  macro_context: "Contamination is systemic; detection exists but diagnosis doesn't; educational measurement solved analogous problem decades ago."
380	  micro_clusters:
381	    contamination_detection:
382	      target_count: 8
383	      must_cite: ["zhang2024minkpp", "dekoninck2024constat", "dong2024kds", "shi2024cdd", "weller2024selfcritique", "golchin2024time"]
384	    irt_for_llm:
385	      target_count: 6
386	      must_cite: ["lalor2024aaai", "polo2024tinybenchmarks", "burnell2023multidimensional"]
387	    item_compromise_irt:
388	      target_count: 5
389	      must_cite: ["eckerly2017", "sinharay2017", "deboeck2004", "holland1993dif", "adams1997"]
390	    benchmark_reliability:
391	      target_count: 5
392	      must_cite: ["livebench2024", "empcloths2025", "zheng2023chatbot", "liang2023helm"]
393	    calibration_uq:
394	      target_count: 4
395	      must_cite: ["guo2017calibration", "angelopoulos2023conformal", "talts2018sbc"]
396	    mia_foundations:
397	      target_count: 3
398	      must_cite: ["shokri2017membership", "carlini2022extracting"]
399	    contamination_mitigation:
400	      target_count: 4
401	      must_cite: ["oren2024dcr"]
402	    irt_methodology:
403	      target_count: 3
404	      must_cite: ["sanmartin2009", "reckase2009", "mislevy1986"]
405	
406	writing_order:
407	  - section: "method"
408	    rationale: "No data dependency. Sets notation. Include D120 decomposition."
409	  - section: "experimental_setup"
410	    rationale: "Defines design. 3B FROZEN, Llama exploratory."
411	  - section: "results"
412	    rationale: "Core contribution. Domain heterogeneity as flagship."
413	  - section: "related_work"
414	    rationale: "Needs literature_map. DCR expanded comparison (W1)."
415	  - section: "discussion"
416	    rationale: "Dilution masking implications. Model misfit boundary."
417	  - section: "introduction"
418	    rationale: "Diagnostic framing. Lead with dilution masking insight."
419	  - section: "conclusion"
420	    rationale: "Summarizes diagnostic findings."
421	  - section: "abstract"
422	    rationale: "Write last."
423	
424	data_availability:
425	  frozen:
426	    - "Qwen 0.5B/1.5B/3B: all dosages × 2 seeds, SFT + eval + signals ✅ FROZEN"
427	    - "Domain-level IRT N=24 (MMLU 8 domains): Math/Science confirmed ✅"
428	    - "Pooled IRT 2PL+γ N=24 ✅"
429	    - "Min-K++ reversal cross-family (Qwen + Llama) ✅"
430	    - "exp-004 sim_sweep (20 conditions, 200 runs)"
431	  in_progress:
432	    - "Llama-3.2-3B: d000 eval ✅, d005/d025/d100 eval/signals in progress → mark exploratory (single seed, N=4)"
433	  constraints:
434	    - "GSM8K d005 s123: 63.08% anomaly, temporarily unavailable"
435	    - "D045: 0.5B MMLU/ARC excluded from IRT (position bias)"
436	    - "Llama data: exploratory only, post-hoc power analysis required"
437	    - "D123: Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34). Effective Llama MMLU range: d000-d025 only. ARC/GSM8K d100 normal."
438	  excluded_from_paper:
439	    - "7B/72B (rebuttal)"
440	    - "Multi-family beyond Llama-3.2-3B (rebuttal)"
441	    - "RL observational (rebuttal)"
442	
443	review_fixes:
444	  C1: "Add 1.5B/3B complete data to Table 1/2 (data available)"
445	  C2: "Llama N=4 + post-hoc power analysis + 'exploratory' label"
446	  C3: "Triple impossibility limited to 'IRT + membership-inference specific'"
447	  W1: "Expand DCR comparison (qualitative table, no head-to-head numbers)"
448	  W2: "Title → diagnostic framing (D118 approved)"
449	  W4: "Fisher Info N×identifiability heatmap (replaces phase diagram)"
450	  D119: "dilution masking replaces Simpson's Paradox throughout"
451	  D120: "calibration value decomposition paragraph in Method + Results"
452	
453	key_decisions:
454	  - "D118: Title → 'Domain-Differential Contamination Effects: Diagnosis via IRT'"
455	  - "D119: dilution masking replaces Simpson's Paradox"
456	  - "D120: GSM8K calibration value from ability estimation (decomposition)"
457	  - "D121: vanilla 2PL ≈ 2PL+γ calibration MAE on all benchmarks — γ provides NO calibration improvement, only diagnostic value. Calibration entirely from IRT θ estimation."
458	  - "D122 v3 CLEAN: Cross-family pooled IRT — ARC(N=20) γ=0.002, MMLU(N=20) γ=0.213, GSM8K(N=28) γ=-0.110, ALL CI include zero. Qwen-only: ARC γ=0.727 CI excl zero, MMLU γ=0.655 no, GSM8K γ=0.064 no. Key number: ARC 0.73→0.002. v2 MMLU γ=0.71 was WRONG (RRF bug). Three-layer framing unchanged. Red lines: never claim γ universal."
459	  - "D123: Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34). Format-specific SFT overfitting. Exclude from IRT. Mention in Discussion as 'SFT ≠ real contamination' evidence. Not core claim."
460	  - "D039: Characterization-led framing, calibration demoted to Claim 4"
461	  - "D045: Exclude 0.5B MMLU/ARC from IRT (position bias)"
462	  - "D053: Per-benchmark independent IRT only"
463	  - "D055: WITHDRAWN — all checkpoints alpha=32"
464	  - "D056: Coverage collapse = model misspecification"
465	  - "D060: P1/P2 → rebuttal scope"
466	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a23b168-8225-4f69-9e84-5440ae829c56",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "22fae560-2911-4db7-9d6b-a4c43e74e0d0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml",
      "content": "## writing_plan.yaml — contamcal-irt-calibration\n## Generated: 2026-05-16 | Paper Agent Step 1 (REFRAME D118/D119/D120)\n## Status: PENDING_APPROVAL\n\nmeta:\n  venue: \"EMNLP 2026 ARR May 25\"\n  track: \"Machine Learning for NLP / Resources and Evaluation\"\n  deadline: \"2026-05-25\"\n  days_remaining: 9\n  page_limit: 8  # + unlimited appendix\n  template: \"acl_latex (ARR format)\"\n  template_note: \"Use acl-style-files from github.com/acl-org/acl-style-files\"\n  special_theme: \"New Missions for NLP Research\"\n  framing_doc: \"paper_framing.md (D118/D119/D120 reframe: diagnostic-led)\"\n  total_word_budget: 5800\n  review_round: 1\n  target_score: \"Weak Reject → Weak Accept\"\n\ntitle: >\n  Domain-Differential Contamination Effects:\n  Diagnosis via Item Response Theory\n\ncore_claims:\n  C1:\n    name: \"Characterization (PRIMARY)\"\n    summary: >\n      MMLU domain heterogeneity: Math γ=0.97, Science γ=0.84 (significant, PPP acceptable);\n      pooled γ≈0 is dilution masking (D119), NOT absence of effect.\n      Cross-benchmark: ARC forgetting (γ<0) vs GSM8K inflation (γ>0).\n      Scale-dependent: 0.5B catastrophic → 3B mild → 7B negligible.\n    evidence: [exp-006, exp-001]\n    key_data: \"Domain IRT N=24 (MMLU 8 domains), per-benchmark IRT\"\n    priority: 1\n  C2:\n    name: \"Signal Failure (CO-PRIMARY)\"\n    summary: >\n      Min-K++ directional reversal (Cohen's d = -1.55 to -1.98).\n      Cross-family replication: Qwen + Llama both exhibit reversal.\n      S1 embedding only reliable signal (AUC>0.95 at d005).\n      RRF degrades to S1-only in practice.\n    evidence: [exp-008, exp-002]\n    key_data: \"Signal eval 0.5B/1.5B/3B, Llama cross-family (exploratory N=4)\"\n    priority: 1\n  C3:\n    name: \"Identifiability\"\n    summary: >\n      Fisher Info: recovery succeeds down to AUC=0.55 (lowest tested) at N≥50.\n      CI width ∝ N^{-0.48}. LLM eval N=8-30 creates domain-method mismatch.\n      Triple impossibility limited to \"IRT + membership-inference specific\" (C3 fix).\n    evidence: [exp-004]\n    key_data: \"Sim sweep 20 conditions × 200 runs\"\n    priority: 2\n  C4:\n    name: \"Conditional Calibration (DEMOTED)\"\n    summary: >\n      KEY FINDING: vanilla 2PL ≈ 2PL+γ on calibration MAE (GSM8K: 0.0063 vs 0.0062;\n      MMLU: 0.0068 vs 0.0070; ARC: 0.0158 vs 0.0201). γ does NOT improve calibration.\n      Calibration improvement entirely from IRT ability estimation (θ separation from noise).\n      γ value is DIAGNOSTIC (domain-level heterogeneity detection), not calibration.\n      Gating criterion: γ significant + PPP∈[0.1,0.9] + calibrated MAE < raw MAE.\n      ARC MAE=0.035 (passes). GSM8K overcorrection 11× (fails gating → honest negative).\n      D120: calibration value decomposition — all calibration benefit from θ, not γ.\n    evidence: [exp-006]\n    priority: 3\n    narrative_constraint: >\n      NEVER imply γ brings calibration improvement. Two distinct values:\n      (a) IRT framework → calibration (robust θ estimation even without γ);\n      (b) γ → domain-level diagnosis (which domains inflated/deflated, direction, magnitude).\n      This STRENGTHENS the diagnostic framing (D118).\n\npaper_outline:\n  abstract:\n    word_budget: 200\n    dependencies: [introduction, results, conclusion]\n    key_numbers: [\"MMLU Math γ=0.97\", \"dilution masking pooled γ≈0\", \"Min-K++ Cohen's d=-1.55 to -1.98\", \"ARC MAE=0.035\", \"N≥50 threshold\"]\n    notes: \"Diagnostic framing. Lead with domain heterogeneity + dilution masking. Signal failure as co-primary.\"\n\n  introduction:\n    word_budget: 850\n    dependencies: [method, results]\n    subsections:\n      - \"Problem: contamination undermines benchmark reliability; aggregate metrics mask heterogeneous effects\"\n      - \"Gap: detection methods flag but don't diagnose or calibrate; mitigation provably fails (Emperor's)\"\n      - \"Our approach: IRT-based diagnostic framework revealing domain-differential effects\"\n      - \"4 contributions: (1) domain heterogeneity + dilution masking, (2) signal failure, (3) identifiability bounds, (4) conditional calibration\"\n    notes: \"D118: 'diagnostic findings + conditional calibration' framing. D119: dilution masking replaces Simpson's Paradox.\"\n\n  related_work:\n    word_budget: 700\n    dependencies: [literature_map]\n    subsections:\n      - \"Contamination detection (Min-K++, ConStat, KDS, CDD, Self-Critique)\"\n      - \"IRT for LLM evaluation (Lalor, TinyBenchmarks, Growing Pains, HiBayES)\"\n      - \"Item compromise in educational measurement (Eckerly, Sinharay, DIF)\"\n      - \"Contamination mitigation + DCR qualitative comparison (W1 fix)\"\n      - \"Calibration disambiguation\"\n    notes: \"W1: expand DCR comparison (qualitative table). Cite TED/CDD as closest competitors.\"\n\n  method:\n    word_budget: 1100\n    dependencies: []\n    subsections:\n      - name: \"3.1 Problem Formulation\"\n        content: \"Given model j, benchmark k with items i. Goal: diagnose contamination effects at domain level + estimate θ_j^clean. Three IRT adaptations.\"\n      - name: \"3.2 Stage 1: Multi-Signal Exposure Mapping\"\n        content: \"4 signals (S1-S4), RRF aggregation. Meta-circularity argument. Note S2/S4 failure modes.\"\n      - name: \"3.3 Stage 2: Contamination-Augmented IRT\"\n        content: \"2PL+γ model: P(y=1) = 1/(1+exp(-a_i(θ_j - b_i + γ_k·e_ij))). Per-domain γ_k within benchmark. Stan NUTS.\"\n      - name: \"3.4 Fisher Information and Identifiability\"\n        content: \"Derive I(γ). AUC=0.55 structural, N≥50 practical. CI width scaling. Domain-method mismatch.\"\n      - name: \"3.5 Calibration Value Decomposition (D120/D121)\"\n        content: >\n          ALREADY WRITTEN in method.tex §3.4 as 'Calibration value decomposition' paragraph.\n          Key message: vanilla 2PL ≈ 2PL+γ on calibration MAE (all benchmarks). Calibration\n          benefit entirely from IRT θ estimation. γ provides diagnostic value only.\n          Numbers: GSM8K 0.0063 vs 0.0062; MMLU 0.0068 vs 0.0070; ARC 0.0158 vs 0.0201.\n    notes: \"2PL+γ as primary model (domain-level). 4PL for MC benchmarks (ARC/MMLU). Full Fisher derivation in appendix.\"\n\n  experimental_setup:\n    word_budget: 600\n    dependencies: [method]\n    subsections:\n      - name: \"4.1 Controlled SFT Injection\"\n        content: \"Qwen2.5 (0.5B, 1.5B, 3B). 4 dosages (d000/d005/d025/d100). 2 seeds × 3 scales = N=24 models. LoRA alpha=32. QC-filtered injection.\"\n      - name: \"4.2 Cross-Family Analysis\"\n        content: >\n          Llama-3.2-3B: d000 + d005/d025/d100 (single seed, N=4 additional). Exploratory.\n          PURPOSE: test family-specificity of contamination patterns, NOT confirm generalizability.\n          D123: Llama d100 MMLU excluded (catastrophic collapse, all output 'A', acc=0.34).\n          Effective Llama MMLU range: d000-d025. ARC/GSM8K d100 normal.\n          REQUIRED power analysis: Use Qwen N=24 γ effect sizes as reference\n          (Math γ=0.97, GSM8K γ≈0.06). Compute statistical power at N=4 for each.\n          Cross-family IRT pooling FINAL v3 CLEAN (replaces all prior versions):\n            Pooled (Qwen+Llama):\n              - ARC (N=20): γ=0.002, CI=[-0.57, 0.60], PPP=0.449, calMAE=0.015, ΔMAE=0.055\n              - MMLU (N=20): γ=0.213, CI=[-0.78, 1.25], PPP=0.865, calMAE=0.017, ΔMAE=0.028\n              - GSM8K (N=28): γ=-0.110, CI=[-0.52, 0.28], PPP=0.832, calMAE=0.008, ΔMAE=0.171\n            Qwen-only baseline:\n              - ARC (N=16): γ=0.727, CI excludes zero\n              - MMLU (N=16): γ=0.655, CI does NOT exclude zero\n              - GSM8K (N=24): γ=0.064, CI does NOT exclude zero\n            KEY NARRATIVE NUMBER: ARC γ = 0.73 → 0.002 (strongest family-specificity evidence)\n            NOTE: v2 MMLU γ=0.71 was WRONG (RRF missing s4). Correct value = 0.213.\n          THREE-LAYER FRAMING:\n            (1) IRT calibration generalizes cross-family (calMAE low, ΔMAE large) — STRONGEST claim\n            (2) γ diagnostic value only within-family (Qwen: Math 0.97, Science 0.84; pooled: γ≈0)\n            (3) Family-specificity itself is diagnostic (different families react differently to SFT)\n          RED LINES:\n            ✅ \"IRT calibration generalizes across model families\"\n            ✅ \"γ provides within-family contamination diagnostics\"\n            ✅ \"cross-family analysis reveals family-specific contamination mechanisms\"\n            ❌ \"cross-family validation confirms contamination detection\"\n            ❌ \"γ is a universal contamination indicator\"\n      - name: \"4.3 Benchmarks, Domains, and Evaluation\"\n        content: \"MMLU (57 subjects → 8 cognitive domains), ARC-C (1172 items), GSM8K (1319 items). 6 metrics. Domain stratification strategy.\"\n      - name: \"4.4 Baselines\"\n        content: \"7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR.\"\n    notes: \"D045: 0.5B MMLU/ARC excluded from IRT (position bias). 3B data FROZEN and available.\"\n\n  results:\n    word_budget: 1500\n    dependencies: [experimental_setup, figures, tables]\n    subsections:\n      - name: \"5.1 Domain-Differential Contamination (C1)\"\n        content: >\n          MMLU domain heterogeneity: Math γ=0.97, Science γ=0.84, CS_Eng≈0, non-STEM PPP=1 (model misfit).\n          Dilution masking (D119): pooled γ≈0 because positive STEM effects diluted by null/misfit non-STEM.\n          Cross-benchmark: ARC γ<0 (forgetting), GSM8K γ>0 (inflation).\n          Scale story: 0.5B catastrophic → 3B mild.\n          Cross-family analysis (D122 v3 FINAL CLEAN):\n            Pooling Qwen+Llama → γ vanishes on ALL benchmarks:\n              ARC: 0.73→0.002; MMLU: 0.655→0.213; GSM8K: 0.064→-0.110 (all CI include zero)\n            Only ARC Qwen-only had CI excluding zero — pooling eliminates it completely.\n            calMAE remains low (GSM8K 0.008, ARC 0.015, MMLU 0.017) with large ΔMAE.\n            Three-layer conclusion: (1) θ calibration cross-family valid, (2) γ within-family only,\n            (3) family-specificity is itself a diagnostic finding.\n            Llama d100 ARC acc=0.60 (no inflation despite contamination) vs Qwen pattern → different mechanisms.\n        claims: [C1]\n        key_tables: [table_domain_gamma]\n        key_figures: [fig_domain_gamma, fig_dose_response]\n      - name: \"5.2 Detection Signal Failure (C2)\"\n        content: >\n          S1 AUC>0.95 at d005. Min-K++ reversal Cohen's d=-1.55 to -1.98.\n          Cross-family signal: Llama-3.2-3B replicates Min-K++ reversal direction (exploratory, N=4).\n          RRF = S1-only in practice.\n          NOTE (D122): Cross-family γ pooling shows family-specificity (§5.1 cross-ref).\n          Signal direction replicates, but γ magnitude is family-specific.\n        claims: [C2]\n        key_figures: [fig_signal_heatmap]\n      - name: \"5.3 Identifiability Boundaries (C3)\"\n        content: >\n          Sim sweep: recovery at AUC=0.55 (lowest tested), N≥50. CI ∝ N^{-0.48}.\n          LLM eval operates at N=8-30: IRT-specific impossibility (not general impossibility).\n          Fisher Info N×identifiability heatmap.\n        claims: [C3]\n        key_figures: [fig_identifiability_heatmap]\n      - name: \"5.4 Conditional Calibration (C4)\"\n        content: >\n          KEY NARRATIVE: Show vanilla 2PL baseline alongside 2PL+γ. Explicitly state γ does NOT\n          improve calibration (GSM8K: 0.0063 vs 0.0062; MMLU: 0.0068 vs 0.0070; ARC: 0.0158 vs 0.0201).\n          Calibration benefit entirely from IRT ability estimation.\n          γ value is DIAGNOSTIC: domain-differential heterogeneity detection (§5.1).\n          ARC: MAE=0.035, Kendall τ=0.756, beats all baselines.\n          GSM8K: gating criterion fails (γ non-significant with S1). Overcorrection as honest negative.\n          Coverage below nominal: directional indicators, not precise CIs.\n          Frame positively: this confirms D118 \"Diagnosis via IRT\" — γ reveals hidden structure\n          that aggregate calibration cannot, strengthening the diagnostic contribution.\n        claims: [C4]\n        key_tables: [table_baselines]\n        key_figures: [fig_calibration]\n        narrative_constraint: \"NEVER imply γ improves calibration numbers. Show vanilla 2PL as explicit comparison.\"\n    notes: \"All sections use FROZEN data (3B included). Llama marked 'exploratory'.\"\n\n  discussion:\n    word_budget: 500\n    dependencies: [results]\n    subsections:\n      - \"Dilution masking implications: aggregate benchmark scores as unreliable contamination indicators\"\n      - \"Non-STEM model misfit: boundary of additive γ formulation → future multidimensional IRT\"\n      - \"Limitations: single primary family (Qwen2.5), SFT ≠ real contamination, N<50 in practice\"\n      - \"0.5B position bias (D045): capacity threshold for MC evaluation\"\n      - name: \"SFT ≠ real contamination (W6, expanded with D123)\"\n        content: >\n          Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34) while\n          ARC/GSM8K d100 behave normally. Format-specific: 100% SFT on MC items causes\n          format overfitting (position bias collapse), not present in open-ended (GSM8K)\n          or mixed-format (ARC). This artifact would not occur in natural contamination\n          (gradual, heterogeneous sources). Brief mention, not core claim.\n          Also supports capacity × format interaction for Min-K++ reversal explanation.\n      - \"Future work: multi-family, 7B+, RL observational, data attribution signals\"\n    notes: \"Honest about scope. C3 impossibility limited to IRT+MIA framework.\"\n\n  conclusion:\n    word_budget: 350\n    dependencies: [discussion]\n    notes: >\n      Restate: diagnostic framework reveals hidden structure. Dilution masking as key insight.\n      IRT provides calibration via θ estimation; γ provides domain-level diagnosis.\n      These are complementary, independent values. Honest about γ's non-contribution to calibration numbers.\n\n  appendix:\n    sections:\n      - name: \"A: Fisher Information Derivation\"\n        source: \"artifacts/fisher_info_derivation/fisher_info_appendix.tex\"\n      - name: \"B: Simulation Sweep Full Results\"\n        data_source: \"exp-004\"\n      - name: \"C: Measurement Error Analysis (Negative)\"\n        data_source: \"exp-005\"\n      - name: \"D: 0.5B Position Bias Analysis\"\n        data_source: \"exp-001\"\n      - name: \"E: Llama Cross-Family Analysis + Power Analysis\"\n        notes: >\n          Single seed N=4. Post-hoc power. Exploratory status.\n          D122: Report pooled γ results honestly (GSM8K γ≈0; ARC γ=0.55 CI crosses zero, PPP=0.024).\n          Frame as family-specificity evidence, not failure. Compare Qwen-only vs pooled.\n          IRT θ valid cross-family; γ family-specific → supports per-family modeling recommendation.\n      - name: \"F: DCR Qualitative Comparison Table (W1)\"\n        notes: \"Feature-by-feature comparison with DCR. No head-to-head numbers (no code access).\"\n      - name: \"G: Full Domain-Level IRT Diagnostics\"\n        notes: \"All 8 MMLU domains: γ, CI, PPP, Rhat, ESS. Non-STEM misfit discussion.\"\n\nvisualization_plan:\n  fig_pipeline:\n    type: \"conceptual_diagram\"\n    description: \"ContamCal 2-stage diagnostic pipeline. Emphasize 'diagnosis' framing: signals → domain-level IRT → characterization + conditional calibration.\"\n    placement: \"Section 3 (Method)\"\n    aspect_ratio: \"2:1\"\n    tool: \"matplotlib\"\n    data_source: null\n    output: \"figures/paper/fig_pipeline.pdf\"\n    status: \"DONE (may need minor label update for 'diagnosis' framing)\"\n\n  fig_domain_gamma:\n    type: \"bar_chart_with_ci\"\n    description: >\n      NEW (flagship C1 figure). MMLU domain-level γ estimates.\n      X-axis: 8 MMLU domains (ordered by γ: Math > Science > CS_Eng > ... > non-STEM).\n      Y-axis: γ estimate. Error bars = 95% CI.\n      Color: green (significant + PPP OK) / gray (non-significant) / red (PPP=1, model misfit).\n      Horizontal dashed line at γ=0. Annotate pooled γ≈0 with \"dilution masking\" label.\n    placement: \"Section 5.1 (flagship)\"\n    aspect_ratio: \"3:2\"\n    tool: \"matplotlib\"\n    data_source: \"registry: exp-006 domain-level IRT N=24 (Math/Science/CS_Eng/non-STEM domains)\"\n    output: \"figures/paper/fig_domain_gamma.pdf\"\n\n  fig_dose_response:\n    type: \"line_plot\"\n    description: >\n      Dosage vs accuracy for ARC, GSM8K, MMLU. NOW WITH 3B DATA (3B FROZEN).\n      Three scales: 0.5B, 1.5B, 3B. Error bars from 2 seeds.\n      Shows scale-dependence + benchmark-dependence.\n    placement: \"Section 5.1\"\n    aspect_ratio: \"3:2\"\n    tool: \"matplotlib\"\n    data_source: \"registry: exp-001 eval results (aligned, all scales × dosages × seeds)\"\n    output: \"figures/paper/fig_dose_response.pdf\"\n    status: \"NEEDS REGENERATION (old version has [PENDING-3B], now 3B is FROZEN)\"\n\n  fig_signal_heatmap:\n    type: \"heatmap\"\n    description: >\n      Signal AUC × scale × dosage. Annotate Min-K++ reversal (Cohen's d).\n      Include Llama cross-family row if data available (mark exploratory).\n    placement: \"Section 5.2\"\n    aspect_ratio: \"4:3\"\n    tool: \"matplotlib\"\n    data_source: \"registry: exp-008 signal eval + Llama signals\"\n    output: \"figures/paper/fig_signal_heatmap.pdf\"\n\n  fig_identifiability_heatmap:\n    type: \"heatmap\"\n    description: >\n      W4 fix: N (y-axis) × AUC (x-axis) → γ recovery quality (color = bias or RMSE).\n      Mark actual operating points. Shade structural/practical identifiability regions.\n      Replaces old 'phase diagram' — heatmap is more informative per reviewer.\n    placement: \"Section 5.3\"\n    aspect_ratio: \"1:1\"\n    tool: \"matplotlib\"\n    data_source: \"registry: exp-004 sim_sweep (20 conditions, 200 runs)\"\n    output: \"figures/paper/fig_identifiability_heatmap.pdf\"\n\n  fig_calibration:\n    type: \"scatter_with_ci\"\n    description: >\n      Calibrated vs true accuracy scatter. Include 3B data.\n      MUST include vanilla 2PL baseline (separate marker/color) alongside 2PL+γ.\n      Key visual: vanilla 2PL and 2PL+γ points nearly overlap, demonstrating\n      calibration parity. Color by benchmark. Annotate ARC (good) vs GSM8K (overcorrection).\n      Director note: \"会增加 vanilla 2PL 对照条\"\n    placement: \"Section 5.4\"\n    aspect_ratio: \"1:1\"\n    tool: \"matplotlib\"\n    data_source: \"registry: exp-006 IRT calibration results (both vanilla 2PL and 2PL+γ)\"\n    output: \"figures/paper/fig_calibration.pdf\"\n    status: \"NEEDS REGENERATION (vanilla 2PL comparison added)\"\n\ntable_plan:\n  table_domain_gamma:\n    type: \"parameter_summary\"\n    description: \"Domain-level IRT γ estimates (MMLU 8 domains + ARC + GSM8K)\"\n    columns: [\"Domain/Benchmark\", \"N_items\", \"γ̂\", \"95% CI\", \"Sig?\", \"PPP\", \"Interpretation\"]\n    data_source: \"exp-006 domain-level IRT (N=24 models)\"\n    placement: \"Section 5.1\"\n    rows:\n      - \"MMLU: Math — γ=+0.97, CI excludes 0, PPP=0.44, Strong inflation\"\n      - \"MMLU: Science — γ=+0.84, CI excludes 0, PPP=0.81, Strong inflation\"\n      - \"MMLU: CS_Eng — γ=+0.20, CI includes 0, PPP=0.89, Null\"\n      - \"MMLU: Non-STEM (5 domains) — PPP≈1.0, Model misfit (see Appendix G)\"\n      - \"MMLU: Pooled — γ≈0, dilution masking\"\n      - \"ARC-Challenge — γ=-1.46, CI excludes 0, Forgetting\"\n      - \"GSM8K — γ non-significant (S1), Inflation via oracle only\"\n      - \"[3B rows from FROZEN data]\"\n\n  table_baselines:\n    type: \"comparison\"\n    description: \"Calibration performance: ContamCal vs 7 baselines + DCR qualitative\"\n    columns: [\"Method\", \"ARC MAE↓\", \"ARC τ↑\", \"ARC C95%\", \"Notes\"]\n    data_source: \"exp-006 baseline comparisons\"\n    placement: \"Section 5.4\"\n    notes: \"W1: add qualitative DCR comparison column. Include 3B data.\"\n\n  table_dcr_comparison:\n    type: \"qualitative\"\n    description: \"W1 fix: DCR vs ContamCal feature comparison\"\n    columns: [\"Feature\", \"DCR\", \"ContamCal\"]\n    placement: \"Section 2 (Related Work) or Section 5.4\"\n    rows:\n      - \"Uncertainty quantification: ✗ / ✓ (Bayesian CIs)\"\n      - \"Domain-level diagnosis: ✗ / ✓ (per-domain γ)\"\n      - \"Identifiability analysis: ✗ / ✓ (Fisher Info)\"\n      - \"Signal failure detection: ✗ / ✓ (Min-K++ reversal)\"\n      - \"Adjusted accuracy: ✓ / ✓\"\n      - \"Multi-benchmark: ✓ / ✓\"\n      - \"Requires reference set: ✓ (fuzzy match) / ✗ (signal-based)\"\n\nliterature_strategy:\n  citation_budget: \"40-50 total\"\n  macro_context: \"Contamination is systemic; detection exists but diagnosis doesn't; educational measurement solved analogous problem decades ago.\"\n  micro_clusters:\n    contamination_detection:\n      target_count: 8\n      must_cite: [\"zhang2024minkpp\", \"dekoninck2024constat\", \"dong2024kds\", \"shi2024cdd\", \"weller2024selfcritique\", \"golchin2024time\"]\n    irt_for_llm:\n      target_count: 6\n      must_cite: [\"lalor2024aaai\", \"polo2024tinybenchmarks\", \"burnell2023multidimensional\"]\n    item_compromise_irt:\n      target_count: 5\n      must_cite: [\"eckerly2017\", \"sinharay2017\", \"deboeck2004\", \"holland1993dif\", \"adams1997\"]\n    benchmark_reliability:\n      target_count: 5\n      must_cite: [\"livebench2024\", \"empcloths2025\", \"zheng2023chatbot\", \"liang2023helm\"]\n    calibration_uq:\n      target_count: 4\n      must_cite: [\"guo2017calibration\", \"angelopoulos2023conformal\", \"talts2018sbc\"]\n    mia_foundations:\n      target_count: 3\n      must_cite: [\"shokri2017membership\", \"carlini2022extracting\"]\n    contamination_mitigation:\n      target_count: 4\n      must_cite: [\"oren2024dcr\"]\n    irt_methodology:\n      target_count: 3\n      must_cite: [\"sanmartin2009\", \"reckase2009\", \"mislevy1986\"]\n\nwriting_order:\n  - section: \"method\"\n    rationale: \"No data dependency. Sets notation. Include D120 decomposition.\"\n  - section: \"experimental_setup\"\n    rationale: \"Defines design. 3B FROZEN, Llama exploratory.\"\n  - section: \"results\"\n    rationale: \"Core contribution. Domain heterogeneity as flagship.\"\n  - section: \"related_work\"\n    rationale: \"Needs literature_map. DCR expanded comparison (W1).\"\n  - section: \"discussion\"\n    rationale: \"Dilution masking implications. Model misfit boundary.\"\n  - section: \"introduction\"\n    rationale: \"Diagnostic framing. Lead with dilution masking insight.\"\n  - section: \"conclusion\"\n    rationale: \"Summarizes diagnostic findings.\"\n  - section: \"abstract\"\n    rationale: \"Write last.\"\n\ndata_availability:\n  frozen:\n    - \"Qwen 0.5B/1.5B/3B: all dosages × 2 seeds, SFT + eval + signals ✅ FROZEN\"\n    - \"Domain-level IRT N=24 (MMLU 8 domains): Math/Science confirmed ✅\"\n    - \"Pooled IRT 2PL+γ N=24 ✅\"\n    - \"Min-K++ reversal cross-family (Qwen + Llama) ✅\"\n    - \"exp-004 sim_sweep (20 conditions, 200 runs)\"\n  in_progress:\n    - \"Llama-3.2-3B: d000 eval ✅, d005/d025/d100 eval/signals in progress → mark exploratory (single seed, N=4)\"\n  constraints:\n    - \"GSM8K d005 s123: 63.08% anomaly, temporarily unavailable\"\n    - \"D045: 0.5B MMLU/ARC excluded from IRT (position bias)\"\n    - \"Llama data: exploratory only, post-hoc power analysis required\"\n    - \"D123: Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34). Effective Llama MMLU range: d000-d025 only. ARC/GSM8K d100 normal.\"\n  excluded_from_paper:\n    - \"7B/72B (rebuttal)\"\n    - \"Multi-family beyond Llama-3.2-3B (rebuttal)\"\n    - \"RL observational (rebuttal)\"\n\nreview_fixes:\n  C1: \"Add 1.5B/3B complete data to Table 1/2 (data available)\"\n  C2: \"Llama N=4 + post-hoc power analysis + 'exploratory' label\"\n  C3: \"Triple impossibility limited to 'IRT + membership-inference specific'\"\n  W1: \"Expand DCR comparison (qualitative table, no head-to-head numbers)\"\n  W2: \"Title → diagnostic framing (D118 approved)\"\n  W4: \"Fisher Info N×identifiability heatmap (replaces phase diagram)\"\n  D119: \"dilution masking replaces Simpson's Paradox throughout\"\n  D120: \"calibration value decomposition paragraph in Method + Results\"\n\nkey_decisions:\n  - \"D118: Title → 'Domain-Differential Contamination Effects: Diagnosis via IRT'\"\n  - \"D119: dilution masking replaces Simpson's Paradox\"\n  - \"D120: GSM8K calibration value from ability estimation (decomposition)\"\n  - \"D121: vanilla 2PL ≈ 2PL+γ calibration MAE on all benchmarks — γ provides NO calibration improvement, only diagnostic value. Calibration entirely from IRT θ estimation.\"\n  - \"D122 v3 CLEAN: Cross-family pooled IRT — ARC(N=20) γ=0.002, MMLU(N=20) γ=0.213, GSM8K(N=28) γ=-0.110, ALL CI include zero. Qwen-only: ARC γ=0.727 CI excl zero, MMLU γ=0.655 no, GSM8K γ=0.064 no. Key number: ARC 0.73→0.002. v2 MMLU γ=0.71 was WRONG (RRF bug). Three-layer framing unchanged. Red lines: never claim γ universal.\"\n  - \"D123: Llama-3.2-3B d100 MMLU catastrophic collapse (all output 'A', acc=0.34). Format-specific SFT overfitting. Exclude from IRT. Mention in Discussion as 'SFT ≠ real contamination' evidence. Not core claim.\"\n  - \"D039: Characterization-led framing, calibration demoted to Claim 4\"\n  - \"D045: Exclude 0.5B MMLU/ARC from IRT (position bias)\"\n  - \"D053: Per-benchmark independent IRT only\"\n  - \"D055: WITHDRAWN — all checkpoints alpha=32\"\n  - \"D056: Coverage collapse = model misspecification\"\n  - \"D060: P1/P2 → rebuttal scope\"\n",
      "numLines": 466,
      "startLine": 1,
      "totalLines": 466
    }
  },
  "sourceToolAssistantUUID": "3a23b168-8225-4f69-9e84-5440ae829c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **[紧急修复] method.tex 三个根本性问题 — 写 Results 前必须先改**  Reviewer 发现 method.tex 描述的模型/信号与实际实验不匹配，属于 desk-reject 级问题。  **决策（不可商议）：**  1. **Primary model = 2PL+γ**（不是 4PL+γ）    - 所有冻结数据用的是 2PL+γ…",
  "leafUuid": "22fae560-2911-4db7-9d6b-a4c43e74e0d0",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix method.tex: 2PL model, 3 signals, remove KDS ablation",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---

### Assistant

_source line 18 · 2026-05-17T02:37:38.137Z_

文件路径可能不同。让我找到实际的 tex 文件位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22fae560-2911-4db7-9d6b-a4c43e74e0d0",
  "isSidechain": false,
  "requestId": "req_011Cb7N5dntgHA66fz7uEhzm",
  "type": "assistant",
  "uuid": "9d6a6618-d0f5-4b5d-a96e-410c505a65dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gz3VXXDV7EBVRFJsp8zMRh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10182,
      "cache_read_input_tokens": 33586,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 33586,
          "cache_creation_input_tokens": 10182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10182
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

_source line 19 · 2026-05-17T02:37:40.182Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013wi4ozXsfY2AkCymNZLyb9`</summary>

```json
{
  "pattern": "**/method.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d6a6618-d0f5-4b5d-a96e-410c505a65dc",
  "isSidechain": false,
  "requestId": "req_011Cb7N5dntgHA66fz7uEhzm",
  "type": "assistant",
  "uuid": "9d6cd03a-676f-4b42-be71-63c160a7a8ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gz3VXXDV7EBVRFJsp8zMRh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10182,
      "cache_read_input_tokens": 33586,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 33586,
          "cache_creation_input_tokens": 10182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10182
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

_source line 20 · 2026-05-17T02:37:40.276Z_

<details><summary>↩ Tool result · `toolu_013wi4ozXsfY2AkCymNZLyb9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d6cd03a-676f-4b42-be71-63c160a7a8ea",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "dc69a4c0-c145-49c9-b950-c23eed953fc2",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
    ],
    "durationMs": 80,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9d6cd03a-676f-4b42-be71-63c160a7a8ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T02:37:40.464Z_

<details><summary>↩ Tool result · `toolu_01RQHdW5S8HngqiDTtuJJbNm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e879206-4197-4e02-8d8c-c3cf335c996b",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "b6ebaeb9-6157-4973-adcf-f21732fde60b",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex"
    ],
    "durationMs": 54,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0e879206-4197-4e02-8d8c-c3cf335c996b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T02:37:40.406Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RQHdW5S8HngqiDTtuJJbNm`</summary>

```json
{
  "pattern": "**/introduction.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc69a4c0-c145-49c9-b950-c23eed953fc2",
  "isSidechain": false,
  "requestId": "req_011Cb7N5dntgHA66fz7uEhzm",
  "type": "assistant",
  "uuid": "0e879206-4197-4e02-8d8c-c3cf335c996b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gz3VXXDV7EBVRFJsp8zMRh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10182,
      "cache_read_input_tokens": 33586,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 33586,
          "cache_creation_input_tokens": 10182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10182
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

_source line 23 · 2026-05-17T02:37:43.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_012SwdsiCkB7jErzHvQaU9PW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ebaeb9-6157-4973-adcf-f21732fde60b",
  "isSidechain": false,
  "requestId": "req_011Cb7N64MWRheq1CDe94vdR",
  "type": "assistant",
  "uuid": "48603e22-687c-4a64-a982-7b3edbd46bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtJrJdgGYfAxMfJZLH96nu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 43768,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 43768,
          "cache_creation_input_tokens": 355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 355
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

_source line 24 · 2026-05-17T02:37:43.395Z_

<details><summary>↩ Tool result · `toolu_012SwdsiCkB7jErzHvQaU9PW`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages. Stage~1 (\S\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\S\ref{sec:stage2}--\S\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.
5	
6	\subsection{Stage 1: Multi-Signal Provenance Mapping}
7	\label{sec:stage1}
8	
9	For each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.
10	
11	\paragraph{Embedding-based near-duplicate retrieval.}
12	We embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.
13	
14	\paragraph{Min-K\%++ membership inference.}
15	Following \citet{duan2025minkpp}, we compute the average log-probability of the $k\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.
16	
17	\paragraph{ConStat performance gap.}
18	For each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.
19	
20	\paragraph{Self-Critique entropy collapse.}
21	When model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\S\ref{sec:signal_survival}).
22	
23	\paragraph{Signal survival analysis.}
24	\label{sec:signal_survival}
25	Prior work suggests that detection signals do not degrade uniformly across training regimes. \citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \S\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results
26	
27	\paragraph{RRF aggregation.}
28	We aggregate the four signals via reciprocal rank fusion \citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:
29	\begin{equation}
30	\label{eq:rrf}
31	    e_{ij} = \sum_{s=1}^{4} \frac{1}{k + r_{s,i}(j)},
32	\end{equation}
33	where $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.
34	
35	We note that KDS \citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.
36	
37	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
38	\label{sec:stage2}
39	
40	\paragraph{Model specification.}
41	We augment the standard four-parameter logistic (4PL) IRT model \citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:
42	\begin{equation}
43	\label{eq:4pl}
44	    P(y_{ij} = 1 \mid \boldsymbol{\psi}) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}\bigr),
45	\end{equation}
46	where $\sigma(\cdot)$ denotes the logistic function, $y_{ij} \in \{0,1\}$ is the binary response, and $\boldsymbol{\psi}$ collects all parameters. The standard IRT parameters are: $\theta_i \in \mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \in \mathbb{R}$ (difficulty of item~$j$), $c_j \in [0,1]$ (guessing/lower asymptote), and $d_j \in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\gamma \in \mathbb{R}$ (global contamination effect) and $\tau_{ij} \geq 0$ (latent true exposure of model~$i$ to item~$j$).
47	
48	The additive structure $a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\gamma \cdot \tau_{ij} / a_j$ units on the ability scale. When $\tau_{ij} = 0$ (no contamination), Eq.~\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\gamma$ indicates that contamination inflates performance, as expected.
49	
50	\paragraph{Measurement error model.}
51	The latent exposure $\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:
52	\begin{equation}
53	\label{eq:measurement_error}
54	    \tau_{ij} \sim \mathcal{N}(e_{ij},\, \sigma_e^2),
55	\end{equation}
56	where $\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\theta_i$ and contamination effect~$\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\S\ref{sec:signal_survival})---the posterior distribution of~$\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.
57	
58	\paragraph{Prior specification.}
59	We assign the following priors:
60	\begin{align}
61	    \theta_i &\sim \mathcal{N}(0, 1), \label{eq:prior_theta} \\
62	    a_j &\sim \text{LogNormal}(0, 0.5), \label{eq:prior_a} \\
63	    b_j &\sim \mathcal{N}(0, 1), \label{eq:prior_b} \\
64	    c_j &\sim \text{Beta}(5, 20), \label{eq:prior_c} \\
65	    d_j &\sim \text{Beta}(20, 5), \label{eq:prior_d} \\
66	    \gamma &\sim \mathcal{N}(0, 1). \label{eq:prior_gamma}
67	\end{align}
68	The $\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\approx 0.2$) but non-negligible for multiple-choice items. The $\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\mathcal{N}(0, 1)$ prior on~$\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\mathcal{N}(0, 0.5)$ and $\mathcal{N}(0, 2)$ to assess robustness to this specification (\S\ref{sec:experiments}).
69	
70	\paragraph{Connection to item compromise IRT.}
71	Equation~\eqref{eq:4pl} extends the item compromise IRT tradition \citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.
72	
73	\emph{Adaptation~1: Independent examinees $\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\S\ref{sec:experiments}).
74	
75	\emph{Adaptation~2: Binary leakage $\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \in \{0, 1\}$ \citep{sinharay2017}. We generalize to continuous exposure scores $\tau_{ij} \in \mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \citep{maris2009}.
76	
77	\emph{Adaptation~3: Stable ability $\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\S\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.
78	
79	\subsection{Bayesian Inference}
80	\label{sec:inference}
81	
82	We perform full Bayesian inference using the No-U-Turn Sampler \citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\hat{R} < 1.01$ for all parameters, effective sample size $\text{ESS} > 400$ per parameter, and fewer than 0.1\% divergent transitions. The target acceptance probability is set to $\texttt{adapt\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.
83	
84	\paragraph{Per-benchmark fitting.}
85	Rather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\gamma_k$ (\S\ref{sec:calibrated}), the primary specification in our framework.
86	
87	\paragraph{Few-examinee regime.}
88	Standard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\S\ref{sec:experiments}). Automatic differentiation variational inference \citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.
89	
90	\subsection{Calibrated Score Computation}
91	\label{sec:calibrated}
92	
93	Given the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:
94	\begin{equation}
95	\label{eq:calibrated}
96	    \text{Acc}_{i}^{\text{cal}} = \frac{1}{|B|} \sum_{j \in B}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[ c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j)\bigr) \right],
97	\end{equation}
98	where the expectation is taken over posterior draws of~$\boldsymbol{\psi}$ and the contamination term $\gamma \cdot \tau_{ij}$ has been removed. This counterfactual quantity answers: \emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}
99	
100	In practice, we approximate Eq.~\eqref{eq:calibrated} by averaging over $L$ posterior draws $\{\boldsymbol{\psi}^{(\ell)}\}_{\ell=1}^{L}$:
101	\begin{equation}
102	\label{eq:calibrated_mc}
103	    \widehat{\text{Acc}}_{i}^{\text{cal}} = \frac{1}{L} \sum_{\ell=1}^{L} \frac{1}{|B|} \sum_{j \in B} \left[ c_j^{(\ell)} + (d_j^{(\ell)} - c_j^{(\ell)})\,\sigma\!\bigl(a_j^{(\ell)}(\theta_i^{(\ell)} - b_j^{(\ell)})\bigr) \right].
104	\end{equation}
105	Credible intervals at level~$\alpha$ are obtained from the empirical quantiles of $\{\text{Acc}_{i}^{\text{cal},(\ell)}\}_{\ell=1}^{L}$. We report 50\%, 80\%, and 95\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.
106	
107	\paragraph{Per-benchmark contamination effects.}
108	Since we fit independent models per benchmark (\S\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\gamma_k$:
109	\begin{equation}
110	\label{eq:per_benchmark_gamma}
111	    P(y_{ij} = 1 \mid \boldsymbol{\psi}_k) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma_k \cdot \tau_{ij}\bigr),
112	\end{equation}
113	where $\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\gamma_k \sim \mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks.
114	
115	\paragraph{Calibration value decomposition.}
116	The calibrated score in Eq.~\eqref{eq:calibrated} depends on the ability estimate~$\theta_i$, not on $\gamma_k$ directly. Two distinct mechanisms contribute to calibration quality: (a)~the IRT ability estimation itself, which separates stable model capability from item-specific noise regardless of the contamination model; and (b)~the explicit $\gamma_k$ correction, which reweights items based on exposure during the joint estimation of~$\theta_i$. In principle, including $\gamma_k$ should yield better $\theta_i$ estimates by absorbing contamination variance. In practice, we compare calibration MAE between the full model (2PL+$\gamma$) and vanilla 2PL ($\gamma\!=\!0$) to quantify the marginal calibration contribution of the contamination covariate (\S\ref{sec:results}). The $\gamma_k$ parameters serve a complementary diagnostic role: they reveal which domains or benchmarks exhibit inflation, deflation, or model misfit, providing actionable characterization that aggregate calibration metrics cannot deliver.
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48603e22-687c-4a64-a982-7b3edbd46bb1",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "fc73dca0-4c2b-4e5c-8cc9-4a50a9bdc8dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages. Stage~1 (\\S\\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\\S\\ref{sec:stage2}--\\S\\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.\n\n\\subsection{Stage 1: Multi-Signal Provenance Mapping}\n\\label{sec:stage1}\n\nFor each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.\n\n\\paragraph{Embedding-based near-duplicate retrieval.}\nWe embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.\n\n\\paragraph{Min-K\\%++ membership inference.}\nFollowing \\citet{duan2025minkpp}, we compute the average log-probability of the $k\\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.\n\n\\paragraph{ConStat performance gap.}\nFor each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \\citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.\n\n\\paragraph{Self-Critique entropy collapse.}\nWhen model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \\citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\\S\\ref{sec:signal_survival}).\n\n\\paragraph{Signal survival analysis.}\n\\label{sec:signal_survival}\nPrior work suggests that detection signals do not degrade uniformly across training regimes. \\citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \\S\\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results\n\n\\paragraph{RRF aggregation.}\nWe aggregate the four signals via reciprocal rank fusion \\citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s,i}(j)},\n\\end{equation}\nwhere $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.\n\nWe note that KDS \\citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n\n\\paragraph{Model specification.}\nWe augment the standard four-parameter logistic (4PL) IRT model \\citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:\n\\begin{equation}\n\\label{eq:4pl}\n    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ denotes the logistic function, $y_{ij} \\in \\{0,1\\}$ is the binary response, and $\\boldsymbol{\\psi}$ collects all parameters. The standard IRT parameters are: $\\theta_i \\in \\mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \\in \\mathbb{R}$ (difficulty of item~$j$), $c_j \\in [0,1]$ (guessing/lower asymptote), and $d_j \\in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\\gamma \\in \\mathbb{R}$ (global contamination effect) and $\\tau_{ij} \\geq 0$ (latent true exposure of model~$i$ to item~$j$).\n\nThe additive structure $a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\\gamma \\cdot \\tau_{ij} / a_j$ units on the ability scale. When $\\tau_{ij} = 0$ (no contamination), Eq.~\\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\\gamma$ indicates that contamination inflates performance, as expected.\n\n\\paragraph{Measurement error model.}\nThe latent exposure $\\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:\n\\begin{equation}\n\\label{eq:measurement_error}\n    \\tau_{ij} \\sim \\mathcal{N}(e_{ij},\\, \\sigma_e^2),\n\\end{equation}\nwhere $\\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\\theta_i$ and contamination effect~$\\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\\S\\ref{sec:signal_survival})---the posterior distribution of~$\\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.\n\n\\paragraph{Prior specification.}\nWe assign the following priors:\n\\begin{align}\n    \\theta_i &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_theta} \\\\\n    a_j &\\sim \\text{LogNormal}(0, 0.5), \\label{eq:prior_a} \\\\\n    b_j &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_b} \\\\\n    c_j &\\sim \\text{Beta}(5, 20), \\label{eq:prior_c} \\\\\n    d_j &\\sim \\text{Beta}(20, 5), \\label{eq:prior_d} \\\\\n    \\gamma &\\sim \\mathcal{N}(0, 1). \\label{eq:prior_gamma}\n\\end{align}\nThe $\\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\\approx 0.2$) but non-negligible for multiple-choice items. The $\\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\\mathcal{N}(0, 1)$ prior on~$\\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\\mathcal{N}(0, 0.5)$ and $\\mathcal{N}(0, 2)$ to assess robustness to this specification (\\S\\ref{sec:experiments}).\n\n\\paragraph{Connection to item compromise IRT.}\nEquation~\\eqref{eq:4pl} extends the item compromise IRT tradition \\citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.\n\n\\emph{Adaptation~1: Independent examinees $\\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \\citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\\S\\ref{sec:experiments}).\n\n\\emph{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \\in \\{0, 1\\}$ \\citep{sinharay2017}. We generalize to continuous exposure scores $\\tau_{ij} \\in \\mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \\citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \\citep{maris2009}.\n\n\\emph{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\\S\\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.\n\n\\subsection{Bayesian Inference}\n\\label{sec:inference}\n\nWe perform full Bayesian inference using the No-U-Turn Sampler \\citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \\citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\\hat{R} < 1.01$ for all parameters, effective sample size $\\text{ESS} > 400$ per parameter, and fewer than 0.1\\% divergent transitions. The target acceptance probability is set to $\\texttt{adapt\\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.\n\n\\paragraph{Per-benchmark fitting.}\nRather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \\citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\\gamma_k$ (\\S\\ref{sec:calibrated}), the primary specification in our framework.\n\n\\paragraph{Few-examinee regime.}\nStandard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \\citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \\citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\\S\\ref{sec:experiments}). Automatic differentiation variational inference \\citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.\n\n\\subsection{Calibrated Score Computation}\n\\label{sec:calibrated}\n\nGiven the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{i}^{\\text{cal}} = \\frac{1}{|B|} \\sum_{j \\in B}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[ c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j)\\bigr) \\right],\n\\end{equation}\nwhere the expectation is taken over posterior draws of~$\\boldsymbol{\\psi}$ and the contamination term $\\gamma \\cdot \\tau_{ij}$ has been removed. This counterfactual quantity answers: \\emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}\n\nIn practice, we approximate Eq.~\\eqref{eq:calibrated} by averaging over $L$ posterior draws $\\{\\boldsymbol{\\psi}^{(\\ell)}\\}_{\\ell=1}^{L}$:\n\\begin{equation}\n\\label{eq:calibrated_mc}\n    \\widehat{\\text{Acc}}_{i}^{\\text{cal}} = \\frac{1}{L} \\sum_{\\ell=1}^{L} \\frac{1}{|B|} \\sum_{j \\in B} \\left[ c_j^{(\\ell)} + (d_j^{(\\ell)} - c_j^{(\\ell)})\\,\\sigma\\!\\bigl(a_j^{(\\ell)}(\\theta_i^{(\\ell)} - b_j^{(\\ell)})\\bigr) \\right].\n\\end{equation}\nCredible intervals at level~$\\alpha$ are obtained from the empirical quantiles of $\\{\\text{Acc}_{i}^{\\text{cal},(\\ell)}\\}_{\\ell=1}^{L}$. We report 50\\%, 80\\%, and 95\\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.\n\n\\paragraph{Per-benchmark contamination effects.}\nSince we fit independent models per benchmark (\\S\\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\\gamma_k$:\n\\begin{equation}\n\\label{eq:per_benchmark_gamma}\n    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}_k) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma_k \\cdot \\tau_{ij}\\bigr),\n\\end{equation}\nwhere $\\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\\gamma_k \\sim \\mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks.\n\n\\paragraph{Calibration value decomposition.}\nThe calibrated score in Eq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_i$, not on $\\gamma_k$ directly. Two distinct mechanisms contribute to calibration quality: (a)~the IRT ability estimation itself, which separates stable model capability from item-specific noise regardless of the contamination model; and (b)~the explicit $\\gamma_k$ correction, which reweights items based on exposure during the joint estimation of~$\\theta_i$. In principle, including $\\gamma_k$ should yield better $\\theta_i$ estimates by absorbing contamination variance. In practice, we compare calibration MAE between the full model (2PL+$\\gamma$) and vanilla 2PL ($\\gamma\\!=\\!0$) to quantify the marginal calibration contribution of the contamination covariate (\\S\\ref{sec:results}). The $\\gamma_k$ parameters serve a complementary diagnostic role: they reveal which domains or benchmarks exhibit inflation, deflation, or model misfit, providing actionable characterization that aggregate calibration metrics cannot deliver.\n",
      "numLines": 117,
      "startLine": 1,
      "totalLines": 117
    }
  },
  "sourceToolAssistantUUID": "48603e22-687c-4a64-a982-7b3edbd46bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T02:37:43.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HuyF7uEi2n8yyFjQ3FPd3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc73dca0-4c2b-4e5c-8cc9-4a50a9bdc8dc",
  "isSidechain": false,
  "requestId": "req_011Cb7N64MWRheq1CDe94vdR",
  "type": "assistant",
  "uuid": "a07bea8d-ace5-47be-b61a-383564ca5366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtJrJdgGYfAxMfJZLH96nu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 43768,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 43768,
          "cache_creation_input_tokens": 355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 355
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

_source line 26 · 2026-05-17T02:37:43.861Z_

<details><summary>↩ Tool result · `toolu_01HuyF7uEi2n8yyFjQ3FPd3n`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language model (LLM) evaluation increasingly relies on standardized benchmarks to compare models and track progress, yet mounting evidence reveals that these benchmarks are systematically compromised by training data contamination \citep{chang2025benchmarking}. \citet{yang2026rl} demonstrate that rephrased benchmark items appearing in training corpora inflate MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination, and that reinforcement learning (RL) post-training with GRPO further amplifies contamination-driven gains while simultaneously concealing the detection signals that would reveal them. Dose-response analyses confirm a monotonic relationship between contamination exposure and score inflation, with effects persisting across model scales \citep{dong2026dose}. Even minor perturbations to benchmark item surface forms---which should not affect genuinely capable models---produce substantial accuracy drops, questioning the validity of reported scores \citep{wang2025fragility}. Together, these findings point to a reliability crisis in LLM evaluation: reported benchmark scores increasingly conflate memorization with generalizable capability \citep{rao2026silicon}.
5	
6	Several methods have been developed to detect benchmark contamination. Min-K\%++ \citep{duan2025minkpp} and Time Travel \citep{oren2024proving} perform membership inference against pre-training corpora; ConStat \citep{dekoninck2024constat} measures performance gaps between original and paraphrased items; Self-Critique \citep{wust2025selfcritique} identifies memorization through entropy collapse in model self-evaluations; and KDS \citep{xu2025kds} uses knowledge distillation signatures to flag leaked items. While these methods can detect contamination, none produces calibrated benchmark scores that answer the central evaluation question: \emph{what would this model's accuracy be had it never seen the test data?} On the psychometric side, item response theory (IRT) has been increasingly applied to LLM evaluation. PSN-IRT \citep{gu2026psnirt} models item difficulty and discrimination but does not account for contamination. \citet{polo2026growing} validate IRT at the scale of 400+ models yet treat all items as equally trustworthy. ATLAS \citep{lyu2025atlas} and \citet{lalor2024irt} further develop IRT-based evaluation without contamination modeling, and TinyBenchmarks \citep{polo2024tinybenchmarks} demonstrates that carefully selected item subsets can approximate full benchmark scores, but again without contamination awareness. HiBayES \citep{zhuang2025hibayes} provides hierarchical Bayesian uncertainty quantification but ignores item compromise. Inference-time decontamination \citep{yang2024inference} and targeted probing \citep{han2026probing} attempt to adjust or detect contamination effects at evaluation time, but neither produces fully calibrated scores with uncertainty quantification. The closest predecessor, DCR \citep{li2025dcr}, provides adjusted accuracy through fuzzy inference over detection signals but offers no uncertainty bounds and does not address the systematic signal degradation under RL post-training that we document in this work.
7	
8	The case for post-hoc calibration rests on a sobering empirical finding: contamination prevention does not work. \citet{xu2025emperor} systematically evaluate twenty mitigation strategies---including item rephrasing, option shuffling, filtering, and dynamic benchmark construction---and find that none reliably eliminates contamination effects across models and benchmarks. \citet{zhang2025forget} further demonstrate that standard decontamination procedures fail to fully remove memorized content from model weights. While dynamic benchmarks such as LiveBench \citep{white2024livebench} sidestep contamination by continuously generating new items, and efficient evaluation via item subsampling \citep{polo2024tinybenchmarks} can mitigate item-specific biases, neither approach provides calibrated scores for existing contaminated benchmarks. These findings motivate a paradigm shift from contamination \emph{elimination} to contamination \emph{adjustment}: rather than attempting to remove a confounder that resists removal, we measure it and statistically control for it. The analogy to observational causal inference is instructive---when randomization is infeasible, valid estimates are obtained not by eliminating confounders but by measuring and adjusting for them under clearly stated assumptions. ContamCal instantiates this ``statistical safety net'' philosophy for benchmark evaluation.
9	
10	Our approach is grounded in educational measurement's longstanding treatment of item compromise---the leaking of test content to examinees prior to administration. Item compromise IRT models \citep{eckerly2017,sinharay2017} incorporate exposure indicators as covariates within the item response function, enabling joint estimation of compromise effects alongside standard item and person parameters. Explanatory IRT \citep{deboeck2004,adams1997} provides the broader theoretical framework for embedding external covariates in item response models. Adapting this psychometric tradition to LLM evaluation requires three non-trivial structural modifications. First, whereas educational IRT assumes independent examinees, LLM evaluation involves individual models producing all responses to a shared item pool, fundamentally altering local independence semantics \citep{mislevy1986}. Second, binary leakage indicators (compromised vs.\ uncompromised) must be replaced with continuous exposure scores derived from noisy, imperfect detection signals---necessitating a measurement error model that propagates detection uncertainty into ability estimates. Third, stable examinee ability must give way to regime-conditional ability, as models undergoing supervised fine-tuning (SFT) versus RL post-training exhibit qualitatively different contamination signatures that affect both detection signal reliability and contamination effect magnitude.
11	
12	We propose ContamCal, a two-stage framework that provides both calibrated benchmark scores and domain-level contamination diagnosis. In Stage~1 (\emph{Multi-Signal Provenance Mapping}), four training-free detection signals---embedding-based near-duplicate retrieval, Min-K\%++ membership inference, ConStat performance gaps, and Self-Critique entropy collapse---are aggregated via reciprocal rank fusion \citep[RRF;][]{cormack2009} to produce per-item exposure scores. RRF is a deliberate design choice: a learned aggregator would face meta-circularity, as its own training data may be contaminated, precluding unbiased weight estimation. In Stage~2 (\emph{Contamination-Augmented IRT}), exposure scores enter an IRT model as covariates with per-domain contamination effect parameters~$\gamma_k$, estimated jointly with item and ability parameters via Bayesian inference. A measurement error model treats the observed exposure scores as noisy proxies for latent contamination status, automatically propagating detection uncertainty into posterior estimates. The framework delivers two distinct outputs: (a)~calibrated scores from the IRT ability estimates~$\theta_i$, obtained by marginalizing over posterior uncertainty with 50\%/80\%/95\% credible intervals; and (b)~domain-level contamination diagnosis from the~$\gamma_k$ parameters, revealing which cognitive domains are inflated, deflated, or unaffected. Empirically, we find that the calibration benefit arises from IRT ability estimation itself rather than from the explicit $\gamma$ correction, while $\gamma$ provides diagnostic information that aggregate metrics cannot capture. Models trained via RL receive appropriately wider intervals, reflecting the genuine epistemic uncertainty that arises when detection signals are degraded.
13	
14	Our contributions are organized hierarchically. At the core: (1)~domain-differential contamination characterization revealing that aggregate benchmark metrics mask heterogeneous effects across cognitive domains (MMLU Math $\gamma\!=\!0.97$ vs.\ pooled $\gamma\!\approx\!0$), a dilution masking phenomenon where opposing domain-level effects cancel at the benchmark level; (2)~a signal failure analysis demonstrating that Min-K\%++ exhibits directional reversal under contamination (Cohen's $d\!=\!{-}1.55$ to ${-}1.98$), with consistent reversal direction observed on Llama-3.2-3B (exploratory, $N\!=\!4$); and (3)~identifiability boundaries establishing that reliable $\gamma$ recovery requires $N\!\geq\!50$ models and signal $\text{AUC}\!\geq\!0.55$, while typical LLM evaluation operates at $N\!=\!8$--$30$, creating a domain-method mismatch. Supporting these diagnostic findings: (4)~a calibration value decomposition showing that IRT ability estimation provides calibration (vanilla 2PL matches 2PL+$\gamma$ on MAE), while the $\gamma$ parameter independently provides domain-level diagnosis that aggregate methods cannot deliver; and (5)~controlled validation through SFT contamination injection across three model scales (0.5B--3B) within the Qwen2.5 family, with cross-family analysis on Llama-3.2-3B revealing family-specific contamination patterns that support per-family modeling.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a07bea8d-ace5-47be-b61a-383564ca5366",
  "isSidechain": false,
  "promptId": "e79e3c2d-1b55-44c4-ac83-d3b9bc0e7974",
  "type": "user",
  "uuid": "87ecd9c1-b84f-41ca-9fae-7c2f94aabcc4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language model (LLM) evaluation increasingly relies on standardized benchmarks to compare models and track progress, yet mounting evidence reveals that these benchmarks are systematically compromised by training data contamination \\citep{chang2025benchmarking}. \\citet{yang2026rl} demonstrate that rephrased benchmark items appearing in training corpora inflate MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination, and that reinforcement learning (RL) post-training with GRPO further amplifies contamination-driven gains while simultaneously concealing the detection signals that would reveal them. Dose-response analyses confirm a monotonic relationship between contamination exposure and score inflation, with effects persisting across model scales \\citep{dong2026dose}. Even minor perturbations to benchmark item surface forms---which should not affect genuinely capable models---produce substantial accuracy drops, questioning the validity of reported scores \\citep{wang2025fragility}. Together, these findings point to a reliability crisis in LLM evaluation: reported benchmark scores increasingly conflate memorization with generalizable capability \\citep{rao2026silicon}.\n\nSeveral methods have been developed to detect benchmark contamination. Min-K\\%++ \\citep{duan2025minkpp} and Time Travel \\citep{oren2024proving} perform membership inference against pre-training corpora; ConStat \\citep{dekoninck2024constat} measures performance gaps between original and paraphrased items; Self-Critique \\citep{wust2025selfcritique} identifies memorization through entropy collapse in model self-evaluations; and KDS \\citep{xu2025kds} uses knowledge distillation signatures to flag leaked items. While these methods can detect contamination, none produces calibrated benchmark scores that answer the central evaluation question: \\emph{what would this model's accuracy be had it never seen the test data?} On the psychometric side, item response theory (IRT) has been increasingly applied to LLM evaluation. PSN-IRT \\citep{gu2026psnirt} models item difficulty and discrimination but does not account for contamination. \\citet{polo2026growing} validate IRT at the scale of 400+ models yet treat all items as equally trustworthy. ATLAS \\citep{lyu2025atlas} and \\citet{lalor2024irt} further develop IRT-based evaluation without contamination modeling, and TinyBenchmarks \\citep{polo2024tinybenchmarks} demonstrates that carefully selected item subsets can approximate full benchmark scores, but again without contamination awareness. HiBayES \\citep{zhuang2025hibayes} provides hierarchical Bayesian uncertainty quantification but ignores item compromise. Inference-time decontamination \\citep{yang2024inference} and targeted probing \\citep{han2026probing} attempt to adjust or detect contamination effects at evaluation time, but neither produces fully calibrated scores with uncertainty quantification. The closest predecessor, DCR \\citep{li2025dcr}, provides adjusted accuracy through fuzzy inference over detection signals but offers no uncertainty bounds and does not address the systematic signal degradation under RL post-training that we document in this work.\n\nThe case for post-hoc calibration rests on a sobering empirical finding: contamination prevention does not work. \\citet{xu2025emperor} systematically evaluate twenty mitigation strategies---including item rephrasing, option shuffling, filtering, and dynamic benchmark construction---and find that none reliably eliminates contamination effects across models and benchmarks. \\citet{zhang2025forget} further demonstrate that standard decontamination procedures fail to fully remove memorized content from model weights. While dynamic benchmarks such as LiveBench \\citep{white2024livebench} sidestep contamination by continuously generating new items, and efficient evaluation via item subsampling \\citep{polo2024tinybenchmarks} can mitigate item-specific biases, neither approach provides calibrated scores for existing contaminated benchmarks. These findings motivate a paradigm shift from contamination \\emph{elimination} to contamination \\emph{adjustment}: rather than attempting to remove a confounder that resists removal, we measure it and statistically control for it. The analogy to observational causal inference is instructive---when randomization is infeasible, valid estimates are obtained not by eliminating confounders but by measuring and adjusting for them under clearly stated assumptions. ContamCal instantiates this ``statistical safety net'' philosophy for benchmark evaluation.\n\nOur approach is grounded in educational measurement's longstanding treatment of item compromise---the leaking of test content to examinees prior to administration. Item compromise IRT models \\citep{eckerly2017,sinharay2017} incorporate exposure indicators as covariates within the item response function, enabling joint estimation of compromise effects alongside standard item and person parameters. Explanatory IRT \\citep{deboeck2004,adams1997} provides the broader theoretical framework for embedding external covariates in item response models. Adapting this psychometric tradition to LLM evaluation requires three non-trivial structural modifications. First, whereas educational IRT assumes independent examinees, LLM evaluation involves individual models producing all responses to a shared item pool, fundamentally altering local independence semantics \\citep{mislevy1986}. Second, binary leakage indicators (compromised vs.\\ uncompromised) must be replaced with continuous exposure scores derived from noisy, imperfect detection signals---necessitating a measurement error model that propagates detection uncertainty into ability estimates. Third, stable examinee ability must give way to regime-conditional ability, as models undergoing supervised fine-tuning (SFT) versus RL post-training exhibit qualitatively different contamination signatures that affect both detection signal reliability and contamination effect magnitude.\n\nWe propose ContamCal, a two-stage framework that provides both calibrated benchmark scores and domain-level contamination diagnosis. In Stage~1 (\\emph{Multi-Signal Provenance Mapping}), four training-free detection signals---embedding-based near-duplicate retrieval, Min-K\\%++ membership inference, ConStat performance gaps, and Self-Critique entropy collapse---are aggregated via reciprocal rank fusion \\citep[RRF;][]{cormack2009} to produce per-item exposure scores. RRF is a deliberate design choice: a learned aggregator would face meta-circularity, as its own training data may be contaminated, precluding unbiased weight estimation. In Stage~2 (\\emph{Contamination-Augmented IRT}), exposure scores enter an IRT model as covariates with per-domain contamination effect parameters~$\\gamma_k$, estimated jointly with item and ability parameters via Bayesian inference. A measurement error model treats the observed exposure scores as noisy proxies for latent contamination status, automatically propagating detection uncertainty into posterior estimates. The framework delivers two distinct outputs: (a)~calibrated scores from the IRT ability estimates~$\\theta_i$, obtained by marginalizing over posterior uncertainty with 50\\%/80\\%/95\\% credible intervals; and (b)~domain-level contamination diagnosis from the~$\\gamma_k$ parameters, revealing which cognitive domains are inflated, deflated, or unaffected. Empirically, we find that the calibration benefit arises from IRT ability estimation itself rather than from the explicit $\\gamma$ correction, while $\\gamma$ provides diagnostic information that aggregate metrics cannot capture. Models trained via RL receive appropriately wider intervals, reflecting the genuine epistemic uncertainty that arises when detection signals are degraded.\n\nOur contributions are organized hierarchically. At the core: (1)~domain-differential contamination characterization revealing that aggregate benchmark metrics mask heterogeneous effects across cognitive domains (MMLU Math $\\gamma\\!=\\!0.97$ vs.\\ pooled $\\gamma\\!\\approx\\!0$), a dilution masking phenomenon where opposing domain-level effects cancel at the benchmark level; (2)~a signal failure analysis demonstrating that Min-K\\%++ exhibits directional reversal under contamination (Cohen's $d\\!=\\!{-}1.55$ to ${-}1.98$), with consistent reversal direction observed on Llama-3.2-3B (exploratory, $N\\!=\\!4$); and (3)~identifiability boundaries establishing that reliable $\\gamma$ recovery requires $N\\!\\geq\\!50$ models and signal $\\text{AUC}\\!\\geq\\!0.55$, while typical LLM evaluation operates at $N\\!=\\!8$--$30$, creating a domain-method mismatch. Supporting these diagnostic findings: (4)~a calibration value decomposition showing that IRT ability estimation provides calibration (vanilla 2PL matches 2PL+$\\gamma$ on MAE), while the $\\gamma$ parameter independently provides domain-level diagnosis that aggregate methods cannot deliver; and (5)~controlled validation through SFT contamination injection across three model scales (0.5B--3B) within the Qwen2.5 family, with cross-family analysis on Llama-3.2-3B revealing family-specific contamination patterns that support per-family modeling.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  },
  "sourceToolAssistantUUID": "a07bea8d-ace5-47be-b61a-383564ca5366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **[紧急修复] method.tex 三个根本性问题 — 写 Results 前必须先改**  Reviewer 发现 method.tex 描述的模型/信号与实际实验不匹配，属于 desk-reject 级问题。  **决策（不可商议）：**  1. **Primary model = 2PL+γ**（不是 4PL+γ）    - 所有冻结数据用的是 2PL+γ…",
  "leafUuid": "87ecd9c1-b84f-41ca-9fae-7c2f94aabcc4",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix method.tex: 2PL model, 3 signals, remove KDS ablation",
  "sessionId": "bc252caf-e2b6-4080-ba11-8234b25ce5fe"
}
```

---
