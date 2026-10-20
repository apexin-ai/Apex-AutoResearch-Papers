# Research conversation: 项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-rep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/43c1129e-1ff2-4956-a248-b1a9430c423b.jsonl`
- **Structured JSON:** [`fa76fde28b6af05e2b83.json`](../../sessions/fa/fa76fde28b6af05e2b83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T06:35:17.319Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T06:35:17.319Z",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "content": "项目：exec-sim-repair-verifier\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 1 critical, 19 warning\n一致性检查: 0 critical, 3 warning\n编译: ✅, 页数: 22\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T06:35:17.322Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T06:35:17.322Z",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

## Round 1

69 recorded events

### User

_source line 3 · 2026-05-21T06:35:17.368Z_

项目：exec-sim-repair-verifier
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 1 critical, 19 warning
一致性检查: 0 critical, 3 warning
编译: ✅, 页数: 22

请按照你的角色指令执行内容结构审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "3a29c682-685d-4180-ba0b-1125ef581e87",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T06:35:17.365Z_

```json
{
  "parentUuid": "3a29c682-685d-4180-ba0b-1125ef581e87",
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5c376677-5a1e-4011-994e-5017b96b0b58",
  "timestamp": "2026-05-21T06:35:17.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T06:35:17.365Z_

```json
{
  "parentUuid": "5c376677-5a1e-4011-994e-5017b96b0b58",
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
  "uuid": "102f5061-a95e-4fe3-92ca-51d46b611335",
  "timestamp": "2026-05-21T06:35:17.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T06:35:17.365Z_

```json
{
  "parentUuid": "102f5061-a95e-4fe3-92ca-51d46b611335",
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
  "uuid": "e5eece29-a7f6-4806-8173-ebee1d31c4f7",
  "timestamp": "2026-05-21T06:35:17.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7 · 2026-05-21T06:35:17.368Z_

```json
{
  "parentUuid": "e5eece29-a7f6-4806-8173-ebee1d31c4f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9230e718-feb3-4648-8f38-7851c1d38725",
  "timestamp": "2026-05-21T06:35:17.368Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Assistant

_source line 9 · 2026-05-21T06:35:22.208Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of the paper. Let me follow the execution flow:

1. Read `skills/global/paper-writing-norms.skill.md` and `skills/global/paper-quality-lessons.skill.md` for audit standards
2. Read all `.tex` files in the paper directory
3. Audit across all dimensions
4. Output structured findings

Let me start by reading the skill files and tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9230e718-feb3-4648-8f38-7851c1d38725",
  "isSidechain": false,
  "requestId": "req_011CbFFSfAnj69achqHNTkMh",
  "type": "assistant",
  "uuid": "f590b96b-61c4-414e-9444-4ec9df13308d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhA5GjqZaQ8kJYR1gYaeSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26986,
      "cache_read_input_tokens": 11452,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 26986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26986
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

_source line 10 · 2026-05-21T06:35:22.665Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f590b96b-61c4-414e-9444-4ec9df13308d",
  "isSidechain": false,
  "requestId": "req_011CbFFSfAnj69achqHNTkMh",
  "type": "assistant",
  "uuid": "32560db8-9d25-4423-93a0-a210a46b1756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhA5GjqZaQ8kJYR1gYaeSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26986,
      "cache_read_input_tokens": 11452,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 26986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26986
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

_source line 11 · 2026-05-21T06:35:23.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WwJi5aDrYxE5QR83ajBqLo`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32560db8-9d25-4423-93a0-a210a46b1756",
  "isSidechain": false,
  "requestId": "req_011CbFFSfAnj69achqHNTkMh",
  "type": "assistant",
  "uuid": "239448ee-cf3c-4920-a949-56471113836f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhA5GjqZaQ8kJYR1gYaeSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26986,
      "cache_read_input_tokens": 11452,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 26986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26986
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

_source line 12 · 2026-05-21T06:35:24.573Z_

<details><summary>↩ Tool result · `toolu_01EMnShHhpzosNMcaSknpfy3`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58fb5c43-ea12-4cb7-bac6-6de3ba03c16b",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "34e6eb0c-5053-40fc-8ec0-2a42cd166bbe",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
    ],
    "durationMs": 56,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "58fb5c43-ea12-4cb7-bac6-6de3ba03c16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T06:35:23.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KtHyLXjpnQyWENyMHsQfZ5`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239448ee-cf3c-4920-a949-56471113836f",
  "isSidechain": false,
  "requestId": "req_011CbFFSfAnj69achqHNTkMh",
  "type": "assistant",
  "uuid": "96dd3dda-76ca-4da5-8b34-72319df5f23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhA5GjqZaQ8kJYR1gYaeSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26986,
      "cache_read_input_tokens": 11452,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 26986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26986
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

_source line 14 · 2026-05-21T06:35:23.806Z_

<details><summary>↩ Tool result · `toolu_01WwJi5aDrYxE5QR83ajBqLo`</summary>

````text
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
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "239448ee-cf3c-4920-a949-56471113836f",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "62ead4ad-9f26-4ec2-adb0-f1ddb15d103f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "239448ee-cf3c-4920-a949-56471113836f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool result

_source line 15 · 2026-05-21T06:35:23.810Z_

<details><summary>↩ Tool result · `toolu_01KtHyLXjpnQyWENyMHsQfZ5`</summary>

````text
1	---
2	name: paper-quality-lessons
3	description: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 1
7	tags:
8	  - writing
9	  - paper
10	  - quality
11	  - checklist
12	  - review
13	roles:
14	  - agent
15	  - reviewer
16	  - director
17	  - paper_agent
18	---
19	
20	# 论文写作质量指南（NeurIPS 实战经验）
21	
22	> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。
23	> 每条规则都源自真实的 bug / 退回 / 审稿质疑。
24	
25	---
26	
27	## 一、数据诚信与溯源（最高优先级）
28	
29	### 1.1 数字必须有源头
30	
31	- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件
32	- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据
33	- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报
34	- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance
35	
36	> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。
37	
38	### 1.2 不同来源数据不能混用
39	
40	- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol
41	- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明
42	- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较
43	- 非等量对比必须显式标注（如 "at unmatched volumes"）
44	
45	> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。
46	
47	### 1.3 结论撤回后不可复活
48	
49	- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文
50	- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复
51	- 术语修正后不可回退（如 "same norm" → "same per-layer standard deviation"）
52	
53	---
54	
55	## 二、Claim 强度与数据匹配
56	
57	### 2.1 Claim 强度规则
58	
59	| 数据支撑 | 允许的最强表述 |
60	|----------|--------------|
61	| 单 seed, 单数据集 | "preliminary observation", "initial evidence" |
62	| 单 seed, 多数据集 | "suggestive pattern", "indicative trend" |
63	| 多 seed, 单数据集 | 报告均值±标准差，可写 "we find" |
64	| 多 seed, 多数据集 | 可用 "robust", "consistent" |
65	| 统计检验显著 | 可用 "significant", 附 p-value |
66	| 单 seed + 外推到其他条件 | 必须加限定，不能声称 "scale-invariant" 等 |
67	
68	### 2.2 禁止的过强表述
69	
70	- "remarkably stable" → 改为 "relatively stable" 或给出量化波动范围
71	- "confirmed" → 仅 "suggestive" 级别数据不能用
72	- "scale-invariant" → single-seed 验证不够
73	- "We attribute X to Y" → 如果是假说，必须改为 "We hypothesize" + "requiring causal verification"
74	- "roughly twice" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似
75	- "domain-agnostic" → 改为 "robust across N domains tested"
76	
77	### 2.3 Claim 降级机制
78	
79	当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：
80	- 独立 contribution → Discussion 段落
81	- 硬 claim → 加 caveat 的软 claim
82	- 正文数字 → 移入 Appendix
83	
84	---
85	
86	## 三、叙事与 Storytelling
87	
88	### 3.1 结构原则
89	
90	- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线
91	- Introduction 每条 Contribution 必须有对应的 section/table 支撑
92	- Discussion 不应重复 Results 的具体数字——引用表格编号
93	- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix
94	- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组
95	
96	### 3.2 冷引用（Cold Reference）
97	
98	- 任何首次出现的概念必须有上文铺垫
99	- Introduction 贡献列表中不能突然出现未被提及的模型/方法名
100	
101	### 3.3 不要用旧叙事套新数字
102	
103	新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。
104	
105	### 3.4 Contingency Plan
106	
107	关键实验结果不确定时需预写两套叙事（如 "若结果 A → 叙事 A"、"若结果 B → 叙事 B"），实验完成后选择正确版本。提交前必须确认只留了一套。
108	
109	### 3.5 不要基于中间值做叙事决策
110	
111	70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。
112	
113	---
114	
115	## 四、术语与一致性
116	
117	### 4.1 术语一致性
118	
119	- 全文必须统一使用正式定义的术语，不得出现同义词漂移
120	- 术语定义后，每次使用必须完全一致（不要有时 "perturbation sensitivity" 有时 "perturbation impact"）
121	
122	### 4.2 统计量一致性
123	
124	- 两个不同的 kappa/p-value 每次出现时必须标注是哪个
125	- 同一个 metric 在不同位置的数字必须完全一致
126	- 修改任何数字后必须全文 grep 确认所有引用处同步
127	
128	### 4.3 p-value 格式
129	
130	- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）
131	- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明
132	
133	### 4.4 例子与定义必须一致
134	
135	Taxonomy 中的定义和对应示例不能自相矛盾。如果定义说 "no new content"，示例中就不能包含新信息。
136	
137	---
138	
139	## 五、投稿前检查清单（Pre-Submission Checklist）
140	
141	### 5.1 占位符扫描（硬门禁）
142	
143	提交前必须 grep 扫描，以下模式要求**零匹配**：
144	```
145	XX.XX, PLACEHOLDER, [If , TODO, TBD, \placeholder{
146	```
147	所有条件占位段落（`[If ...]`）必须替换为最终文本。
148	
149	### 5.2 编译检查
150	
151	- [ ] 编译零 error
152	- [ ] 无 `??` 未解析引用
153	- [ ] 无 > 1pt 的 overfull hbox
154	- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）
155	- [ ] 使用当年 style file（`neurips_2026.sty`）
156	- [ ] Review 版启用行号
157	- [ ] 匿名审稿版无作者姓名、无致谢
158	
159	### 5.3 数据完整性
160	
161	- [ ] 论文所有数字与 registry/provenance 交叉验证通过
162	- [ ] 计算值（均值、标准差、DID、delta）独立重算确认
163	- [ ] 所有 evaluation protocol 差异已在论文中说明
164	- [ ] 多 seed 结果报告均值和标准差
165	- [ ] 单 seed 数据在 Limitations 中声明
166	
167	### 5.4 图表检查
168	
169	- [ ] 所有 figure PDF 存在且路径匹配
170	- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）
171	- [ ] 图中字体 ≥ 7pt
172	- [ ] 小数精度全表统一
173	- [ ] 最优结果加粗、次优下划线
174	- [ ] 表格标题（caption）自包含
175	- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）
176	
177	### 5.5 引用检查
178	
179	- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）
180	- [ ] 引用密度与目标会议近年录用论文同量级
181	- [ ] 引用键与 bib 条目 1:1 匹配
182	- [ ] 无孤儿 bib 条目
183	- [ ] 无幻觉引用（所有被引论文实际存在）
184	- [ ] 近年论文的年份/会议准确
185	- [ ] 审稿人要求的引用全部补齐
186	
187	### 5.6 匿名化检查
188	
189	- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）
190	- [ ] 配置文件无服务器路径
191	- [ ] Git history 已清理 author 信息（用 fresh repo）
192	- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）
193	- [ ] API Keys 通过环境变量，无泄露
194	
195	### 5.7 会议 Checklist 填写（如目标会议要求）
196	
197	- [ ] Claims: 摘要/Introduction 准确反映实验范围
198	- [ ] Limitations: 正文 Limitations 段 + Appendix 补充
199	- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）
200	- [ ] Reproducibility: 数据集公开、代码可用
201	- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间
202	- [ ] Compute: GPU 型号、训练时间、总 GPU-hours
203	- [ ] Licenses: 数据集/模型引用完整
204	- [ ] AI Assistants: 如实声明使用情况
205	- [ ] 每项认真回答（不要全写 N/A）
206	
207	### 5.8 叙事完整性
208	
209	- [ ] Conclusion 包含所有关键限定符（如 "under greedy decoding"）
210	- [ ] Abstract 与正文一致（不能一个写 "single seed" 另一个已是 "10 seeds"）
211	- [ ] 无 Appendix Version A/B 两套叙事残留
212	- [ ] 无 LaTeX 注释与正文混淆
213	- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）
214	- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）
215	- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）
216	
217	### 5.9 去 AI 风格检查
218	
219	- [ ] **`grep "—" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）
220	- [ ] **`grep " – " paper/*.tex` 全文清零**（解释性 en-dash 必须全删）
221	- [ ] 无 "-ing," 分词短语结尾（如 "..., demonstrating the effectiveness of..."）
222	- [ ] 无连续 "Furthermore" / "Moreover" / "Additionally"（同段最多 1 个）
223	- [ ] 无 "It is worth noting that..." / "Notably, ..."
224	- [ ] 无 "delve into" / "leverage" / "utilize" / "a myriad of" / "a plethora of"
225	- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段
226	
227	### 5.10 模板与同类论文核对
228	
229	- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）
230	- [ ] `\documentclass[]{}` 选项匹配 review / camera-ready 阶段
231	- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐
232	
233	---
234	
235	## 六、Reviewer 审查标准
236	
237	### 6.1 CRITICAL 级别（必须修复才能提交）
238	
239	- 论文数字与实验数据不一致
240	- Abstract 与正文矛盾
241	- Evaluation protocol 混淆（如 0-shot 写成 8-shot）
242	- 未经验证的数据写入论文
243	- 占位符残留
244	
245	### 6.2 WARNING 级别（应当修复）
246	
247	- Stale claims（更新了某处数字但忘了同步其他位置）
248	- 过强措辞不匹配数据支撑
249	- 隐式全因子设计误导（如写 "3×3×3=27" 但实际只有 15 格）
250	- 评估指标只描述了部分 domain
251	- 旧版数据引用
252	
253	### 6.3 数据一致性审查流程
254	
255	1. 从 registry 提取所有实验 metrics
256	2. 对照论文中每一个内联数字（到行号级别）
257	3. 独立重算所有衍生值
258	4. 不一致处标注为 CRITICAL
259	5. 近似表述检查实际比值是否在允许范围内
260	
261	---
262	
263	## 七、常见反模式速查表
264	
265	| 反模式 | 症状 | 修复方式 |
266	|--------|------|----------|
267	| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |
268	| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |
269	| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |
270	| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |
271	| 叙事超越数据 | "confirmed" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |
272	| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |
273	| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |
274	| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |
275	| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |
276	| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |
277	| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |
278	| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |
279	| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |
280	| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |
281	
282	---
283	
284	## 八、写论文前加载的 Skills
285	
286	写论文或做最终审查时，Director/Agent 应按需加载以下 skills：
287	- `latex-paper` — LaTeX 编译与格式
288	- `reference-audit` — 引用真实性审计
289	- `academic-writer` — ML 学术写作规范
290	- `paper-quality-lessons`（本 skill）— 实战经验教训
291	
292	---
293	
294	## 九、附录：投稿经验时间线教训
295	
296	1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改
297	2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备
298	3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理
299	4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证
300	5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿
301	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "96dd3dda-76ca-4da5-8b34-72319df5f23c",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "6bcda3f4-42bd-4056-985c-35622b6b8e3c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "content": "---\nname: paper-quality-lessons\ndescription: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 1\ntags:\n  - writing\n  - paper\n  - quality\n  - checklist\n  - review\nroles:\n  - agent\n  - reviewer\n  - director\n  - paper_agent\n---\n\n# 论文写作质量指南（NeurIPS 实战经验）\n\n> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。\n> 每条规则都源自真实的 bug / 退回 / 审稿质疑。\n\n---\n\n## 一、数据诚信与溯源（最高优先级）\n\n### 1.1 数字必须有源头\n\n- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件\n- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据\n- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报\n- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance\n\n> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。\n\n### 1.2 不同来源数据不能混用\n\n- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol\n- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明\n- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较\n- 非等量对比必须显式标注（如 \"at unmatched volumes\"）\n\n> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。\n\n### 1.3 结论撤回后不可复活\n\n- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文\n- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复\n- 术语修正后不可回退（如 \"same norm\" → \"same per-layer standard deviation\"）\n\n---\n\n## 二、Claim 强度与数据匹配\n\n### 2.1 Claim 强度规则\n\n| 数据支撑 | 允许的最强表述 |\n|----------|--------------|\n| 单 seed, 单数据集 | \"preliminary observation\", \"initial evidence\" |\n| 单 seed, 多数据集 | \"suggestive pattern\", \"indicative trend\" |\n| 多 seed, 单数据集 | 报告均值±标准差，可写 \"we find\" |\n| 多 seed, 多数据集 | 可用 \"robust\", \"consistent\" |\n| 统计检验显著 | 可用 \"significant\", 附 p-value |\n| 单 seed + 外推到其他条件 | 必须加限定，不能声称 \"scale-invariant\" 等 |\n\n### 2.2 禁止的过强表述\n\n- \"remarkably stable\" → 改为 \"relatively stable\" 或给出量化波动范围\n- \"confirmed\" → 仅 \"suggestive\" 级别数据不能用\n- \"scale-invariant\" → single-seed 验证不够\n- \"We attribute X to Y\" → 如果是假说，必须改为 \"We hypothesize\" + \"requiring causal verification\"\n- \"roughly twice\" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似\n- \"domain-agnostic\" → 改为 \"robust across N domains tested\"\n\n### 2.3 Claim 降级机制\n\n当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：\n- 独立 contribution → Discussion 段落\n- 硬 claim → 加 caveat 的软 claim\n- 正文数字 → 移入 Appendix\n\n---\n\n## 三、叙事与 Storytelling\n\n### 3.1 结构原则\n\n- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线\n- Introduction 每条 Contribution 必须有对应的 section/table 支撑\n- Discussion 不应重复 Results 的具体数字——引用表格编号\n- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix\n- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组\n\n### 3.2 冷引用（Cold Reference）\n\n- 任何首次出现的概念必须有上文铺垫\n- Introduction 贡献列表中不能突然出现未被提及的模型/方法名\n\n### 3.3 不要用旧叙事套新数字\n\n新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。\n\n### 3.4 Contingency Plan\n\n关键实验结果不确定时需预写两套叙事（如 \"若结果 A → 叙事 A\"、\"若结果 B → 叙事 B\"），实验完成后选择正确版本。提交前必须确认只留了一套。\n\n### 3.5 不要基于中间值做叙事决策\n\n70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。\n\n---\n\n## 四、术语与一致性\n\n### 4.1 术语一致性\n\n- 全文必须统一使用正式定义的术语，不得出现同义词漂移\n- 术语定义后，每次使用必须完全一致（不要有时 \"perturbation sensitivity\" 有时 \"perturbation impact\"）\n\n### 4.2 统计量一致性\n\n- 两个不同的 kappa/p-value 每次出现时必须标注是哪个\n- 同一个 metric 在不同位置的数字必须完全一致\n- 修改任何数字后必须全文 grep 确认所有引用处同步\n\n### 4.3 p-value 格式\n\n- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）\n- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明\n\n### 4.4 例子与定义必须一致\n\nTaxonomy 中的定义和对应示例不能自相矛盾。如果定义说 \"no new content\"，示例中就不能包含新信息。\n\n---\n\n## 五、投稿前检查清单（Pre-Submission Checklist）\n\n### 5.1 占位符扫描（硬门禁）\n\n提交前必须 grep 扫描，以下模式要求**零匹配**：\n```\nXX.XX, PLACEHOLDER, [If , TODO, TBD, \\placeholder{\n```\n所有条件占位段落（`[If ...]`）必须替换为最终文本。\n\n### 5.2 编译检查\n\n- [ ] 编译零 error\n- [ ] 无 `??` 未解析引用\n- [ ] 无 > 1pt 的 overfull hbox\n- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）\n- [ ] 使用当年 style file（`neurips_2026.sty`）\n- [ ] Review 版启用行号\n- [ ] 匿名审稿版无作者姓名、无致谢\n\n### 5.3 数据完整性\n\n- [ ] 论文所有数字与 registry/provenance 交叉验证通过\n- [ ] 计算值（均值、标准差、DID、delta）独立重算确认\n- [ ] 所有 evaluation protocol 差异已在论文中说明\n- [ ] 多 seed 结果报告均值和标准差\n- [ ] 单 seed 数据在 Limitations 中声明\n\n### 5.4 图表检查\n\n- [ ] 所有 figure PDF 存在且路径匹配\n- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）\n- [ ] 图中字体 ≥ 7pt\n- [ ] 小数精度全表统一\n- [ ] 最优结果加粗、次优下划线\n- [ ] 表格标题（caption）自包含\n- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）\n\n### 5.5 引用检查\n\n- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）\n- [ ] 引用密度与目标会议近年录用论文同量级\n- [ ] 引用键与 bib 条目 1:1 匹配\n- [ ] 无孤儿 bib 条目\n- [ ] 无幻觉引用（所有被引论文实际存在）\n- [ ] 近年论文的年份/会议准确\n- [ ] 审稿人要求的引用全部补齐\n\n### 5.6 匿名化检查\n\n- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）\n- [ ] 配置文件无服务器路径\n- [ ] Git history 已清理 author 信息（用 fresh repo）\n- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）\n- [ ] API Keys 通过环境变量，无泄露\n\n### 5.7 会议 Checklist 填写（如目标会议要求）\n\n- [ ] Claims: 摘要/Introduction 准确反映实验范围\n- [ ] Limitations: 正文 Limitations 段 + Appendix 补充\n- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）\n- [ ] Reproducibility: 数据集公开、代码可用\n- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间\n- [ ] Compute: GPU 型号、训练时间、总 GPU-hours\n- [ ] Licenses: 数据集/模型引用完整\n- [ ] AI Assistants: 如实声明使用情况\n- [ ] 每项认真回答（不要全写 N/A）\n\n### 5.8 叙事完整性\n\n- [ ] Conclusion 包含所有关键限定符（如 \"under greedy decoding\"）\n- [ ] Abstract 与正文一致（不能一个写 \"single seed\" 另一个已是 \"10 seeds\"）\n- [ ] 无 Appendix Version A/B 两套叙事残留\n- [ ] 无 LaTeX 注释与正文混淆\n- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）\n- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）\n- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）\n\n### 5.9 去 AI 风格检查\n\n- [ ] **`grep \"—\" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）\n- [ ] **`grep \" – \" paper/*.tex` 全文清零**（解释性 en-dash 必须全删）\n- [ ] 无 \"-ing,\" 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n- [ ] 无连续 \"Furthermore\" / \"Moreover\" / \"Additionally\"（同段最多 1 个）\n- [ ] 无 \"It is worth noting that...\" / \"Notably, ...\"\n- [ ] 无 \"delve into\" / \"leverage\" / \"utilize\" / \"a myriad of\" / \"a plethora of\"\n- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段\n\n### 5.10 模板与同类论文核对\n\n- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）\n- [ ] `\\documentclass[]{}` 选项匹配 review / camera-ready 阶段\n- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐\n\n---\n\n## 六、Reviewer 审查标准\n\n### 6.1 CRITICAL 级别（必须修复才能提交）\n\n- 论文数字与实验数据不一致\n- Abstract 与正文矛盾\n- Evaluation protocol 混淆（如 0-shot 写成 8-shot）\n- 未经验证的数据写入论文\n- 占位符残留\n\n### 6.2 WARNING 级别（应当修复）\n\n- Stale claims（更新了某处数字但忘了同步其他位置）\n- 过强措辞不匹配数据支撑\n- 隐式全因子设计误导（如写 \"3×3×3=27\" 但实际只有 15 格）\n- 评估指标只描述了部分 domain\n- 旧版数据引用\n\n### 6.3 数据一致性审查流程\n\n1. 从 registry 提取所有实验 metrics\n2. 对照论文中每一个内联数字（到行号级别）\n3. 独立重算所有衍生值\n4. 不一致处标注为 CRITICAL\n5. 近似表述检查实际比值是否在允许范围内\n\n---\n\n## 七、常见反模式速查表\n\n| 反模式 | 症状 | 修复方式 |\n|--------|------|----------|\n| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |\n| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |\n| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |\n| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |\n| 叙事超越数据 | \"confirmed\" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |\n| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |\n| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |\n| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |\n| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |\n| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |\n| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |\n| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |\n| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |\n| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |\n\n---\n\n## 八、写论文前加载的 Skills\n\n写论文或做最终审查时，Director/Agent 应按需加载以下 skills：\n- `latex-paper` — LaTeX 编译与格式\n- `reference-audit` — 引用真实性审计\n- `academic-writer` — ML 学术写作规范\n- `paper-quality-lessons`（本 skill）— 实战经验教训\n\n---\n\n## 九、附录：投稿经验时间线教训\n\n1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改\n2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备\n3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理\n4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证\n5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿\n",
      "numLines": 301,
      "startLine": 1,
      "totalLines": 301
    }
  },
  "sourceToolAssistantUUID": "96dd3dda-76ca-4da5-8b34-72319df5f23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 16 · 2026-05-21T06:35:24.504Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EMnShHhpzosNMcaSknpfy3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcda3f4-42bd-4056-985c-35622b6b8e3c",
  "isSidechain": false,
  "requestId": "req_011CbFFSfAnj69achqHNTkMh",
  "type": "assistant",
  "uuid": "58fb5c43-ea12-4cb7-bac6-6de3ba03c16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhA5GjqZaQ8kJYR1gYaeSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26986,
      "cache_read_input_tokens": 11452,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 26986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26986
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 19 war…",
  "leafUuid": "34e6eb0c-5053-40fc-8ec0-2a42cd166bbe",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Assistant

_source line 19 · 2026-05-21T06:35:27.755Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them all in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34e6eb0c-5053-40fc-8ec0-2a42cd166bbe",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "5c9f315f-8b32-413c-90c8-3c44675a630c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 20 · 2026-05-21T06:35:28.733Z_

审计标准已加载。现在读取所有 .tex 源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9f315f-8b32-413c-90c8-3c44675a630c",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "3a8d7bec-61f3-4472-94d1-34dc53999a96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 21 · 2026-05-21T06:35:29.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_019dKNuFv8P9J2wCjSNiGtWB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8d7bec-61f3-4472-94d1-34dc53999a96",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "0bb3102b-78d1-4cd0-b8cc-5730761eaf31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 22 · 2026-05-21T06:35:33.775Z_

<details><summary>↩ Tool result · `toolu_01HtFcCMgs3z4BbK9VHtgwk4`</summary>

```text
1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified under MIT license. Qwen3 models are released under Apache 2.0; DeepSeek-Coder under the DeepSeek License. All uses are consistent with their respective licenses. We do not release new artifacts in this submission.
23	
24	\paragraph{B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
25	Yes. All benchmarks are used for their intended purpose of evaluating code understanding and generation capabilities. SWE-bench Verified is used for repository-level evaluation as designed by its creators.
26	
27	\paragraph{B4. Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?}
28	Not applicable. Our datasets consist of code snippets and test cases from open-source repositories. The mutation-based data construction process operates on source code only and does not involve personal data or natural language content that could contain offensive material.
29	
30	\paragraph{B5. Did you provide documentation of the artifacts?}
31	Yes. Section~\ref{sec:setup} documents dataset statistics (sizes, splits, label distributions, majority baselines). The mutation-based data construction process is described in Section~\ref{sec:setup}. Appendix~\ref{app:hyperparams} provides full hyperparameter details.
32	
33	\paragraph{B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}
34	Yes. Section~\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48); repo-level ${\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\%).
35	
36	\subsection*{C. Did You Run Computational Experiments?}
37	
38	\paragraph{C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
39	Yes. Models: Qwen3-4B (${\sim}$4B parameters, LoRA rank 16 $\approx$ 4M trainable), Qwen3-8B (${\sim}$8B), DeepSeek-Coder-6.7B (${\sim}$6.7B). Infrastructure: 4$\times$ NVIDIA RTX 5090 GPUs. Total compute: approximately 150 GPU hours across all training runs (${\sim}$40 configurations including seeds, formulations, model sizes, and ablations). Appendix~\ref{app:hyperparams} provides per-run details.
40	
41	\paragraph{C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}
42	Yes. Section~\ref{sec:setup} reports the training configuration (LoRA rank 16, 3 epochs, 5 seeds with mixed precision). Appendix~\ref{app:hyperparams} provides full hyperparameter values. We use a fixed configuration rather than extensive hyperparameter search; repo-level models use validation accuracy for checkpoint selection.
43	
44	\paragraph{C3. Did you report descriptive statistics about your results with, e.g., error bars or confidence intervals?}
45	Yes. All multi-seed results report mean $\pm$ standard deviation. Confidence intervals use clustered bootstrap (114 problem clusters, 10K resamples; Section~\ref{sec:setup}). Equivalence testing uses TOST ($p = 0.007$, $\pm$2\pp{} margin; Section~\ref{sec:equivalence}). ICC quantifies within-problem correlation with design effect reported.
46	
47	\paragraph{C4. If you used existing packages, did you report the implementation and version numbers?}
48	Yes. Implementation uses HuggingFace Transformers (${\geq}$4.44), PEFT (${\geq}$0.12), PyTorch (${\geq}$2.0), bitsandbytes (${\geq}$0.43, for NF4 quantization), and Python 3.10. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} configurations are detailed in Appendix~\ref{app:hyperparams}. Exact version pinning is provided in the code repository.
49	
50	\subsection*{D. Did You Use Human Annotators?}
51	
52	Not applicable. This work uses no human annotators or participants. All labels are derived from automated test execution.
53	
54	\subsection*{E. AI Assistants}
55	
56	\paragraph{E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in any part of the paper writing or coding process?}
57	Yes. AI coding assistants were used during development of training and evaluation scripts. AI writing assistants were used for drafting and editing portions of the manuscript. All scientific claims, experimental design, and analysis were conducted and verified by the authors.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8415e36e-0483-4c59-bc80-6f663000a0d8",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "50c99351-d731-4aa6-9c95-1cf106e0c36f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex",
      "content": "% ARR Responsible NLP Research Checklist\n% Reference: https://aclrollingreview.org/responsibleNLPresearch/\n\n\\section*{Responsible NLP Research Checklist}\n\nThis paper follows the ARR Responsible NLP Research checklist.\n\n\\subsection*{A. For Every Submission}\n\n\\paragraph{A1. Did you describe the limitations of your work?}\nYes. Section~\\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.\n\n\\paragraph{A2. Did you discuss any potential risks of your work?}\nThis work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.\n\n\\subsection*{B. Did You Use or Create Scientific Artifacts?}\n\n\\paragraph{B1. Did you cite the creators of artifacts you used?}\nYes. All datasets (HumanEval~\\cite{chen2021humaneval}, MBPP~\\cite{austin2021mbpp}, SWE-bench Verified~\\cite{chowdhury2024swebenchverified}), models (Qwen3~\\cite{qwen2025qwen3}, DeepSeek-Coder~\\cite{guo2024deepseekcoder}), and methods (LoRA~\\cite{hu2022lora}, QLoRA~\\cite{dettmers2024qlora}) are cited in Sections~\\ref{sec:setup} and~\\ref{sec:formulations}.\n\n\\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}\nHumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified under MIT license. Qwen3 models are released under Apache 2.0; DeepSeek-Coder under the DeepSeek License. All uses are consistent with their respective licenses. We do not release new artifacts in this submission.\n\n\\paragraph{B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}\nYes. All benchmarks are used for their intended purpose of evaluating code understanding and generation capabilities. SWE-bench Verified is used for repository-level evaluation as designed by its creators.\n\n\\paragraph{B4. Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?}\nNot applicable. Our datasets consist of code snippets and test cases from open-source repositories. The mutation-based data construction process operates on source code only and does not involve personal data or natural language content that could contain offensive material.\n\n\\paragraph{B5. Did you provide documentation of the artifacts?}\nYes. Section~\\ref{sec:setup} documents dataset statistics (sizes, splits, label distributions, majority baselines). The mutation-based data construction process is described in Section~\\ref{sec:setup}. Appendix~\\ref{app:hyperparams} provides full hyperparameter details.\n\n\\paragraph{B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}\nYes. Section~\\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48); repo-level ${\\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\\%).\n\n\\subsection*{C. Did You Run Computational Experiments?}\n\n\\paragraph{C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\nYes. Models: Qwen3-4B (${\\sim}$4B parameters, LoRA rank 16 $\\approx$ 4M trainable), Qwen3-8B (${\\sim}$8B), DeepSeek-Coder-6.7B (${\\sim}$6.7B). Infrastructure: 4$\\times$ NVIDIA RTX 5090 GPUs. Total compute: approximately 150 GPU hours across all training runs (${\\sim}$40 configurations including seeds, formulations, model sizes, and ablations). Appendix~\\ref{app:hyperparams} provides per-run details.\n\n\\paragraph{C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}\nYes. Section~\\ref{sec:setup} reports the training configuration (LoRA rank 16, 3 epochs, 5 seeds with mixed precision). Appendix~\\ref{app:hyperparams} provides full hyperparameter values. We use a fixed configuration rather than extensive hyperparameter search; repo-level models use validation accuracy for checkpoint selection.\n\n\\paragraph{C3. Did you report descriptive statistics about your results with, e.g., error bars or confidence intervals?}\nYes. All multi-seed results report mean $\\pm$ standard deviation. Confidence intervals use clustered bootstrap (114 problem clusters, 10K resamples; Section~\\ref{sec:setup}). Equivalence testing uses TOST ($p = 0.007$, $\\pm$2\\pp{} margin; Section~\\ref{sec:equivalence}). ICC quantifies within-problem correlation with design effect reported.\n\n\\paragraph{C4. If you used existing packages, did you report the implementation and version numbers?}\nYes. Implementation uses HuggingFace Transformers (${\\geq}$4.44), PEFT (${\\geq}$0.12), PyTorch (${\\geq}$2.0), bitsandbytes (${\\geq}$0.43, for NF4 quantization), and Python 3.10. LoRA~\\cite{hu2022lora} and QLoRA~\\cite{dettmers2024qlora} configurations are detailed in Appendix~\\ref{app:hyperparams}. Exact version pinning is provided in the code repository.\n\n\\subsection*{D. Did You Use Human Annotators?}\n\nNot applicable. This work uses no human annotators or participants. All labels are derived from automated test execution.\n\n\\subsection*{E. AI Assistants}\n\n\\paragraph{E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in any part of the paper writing or coding process?}\nYes. AI coding assistants were used during development of training and evaluation scripts. AI writing assistants were used for drafting and editing portions of the manuscript. All scientific claims, experimental design, and analysis were conducted and verified by the authors.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  },
  "sourceToolAssistantUUID": "8415e36e-0483-4c59-bc80-6f663000a0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T06:35:29.233Z_

<details><summary>↩ Tool result · `toolu_019dKNuFv8P9J2wCjSNiGtWB`</summary>

```text
1	\begin{abstract}
2	LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. Our primary finding is function-level near-equivalence: \cls{} and \cwm{} achieve statistical equivalence across both families (TOST $p{=}0.007$, $\pm$2\pp{} margin, 5 seeds, Holm-Bonferroni corrected), establishing that classification is not inherently easier than generation when outputs are short (${\leq}$1.3\pp{} gap). \traj{} reaches parity on Qwen3 but exceeds the equivalence margin on DeepSeek-Coder (2.69\pp{}), revealing model-dependent sensitivity. At repository level, a robust per-test interaction ($z{=}-23.7$, $n{=}56{,}480$) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens from ${\leq}$1.3\pp{} to 19--26\pp{} in single-seed variant-level evaluation, driven by format collapse in generation-based simulation; gap magnitude depends on multiple confounds.
5	
6	Error complementarity across formulations (oracle ensemble: 90.63\%) and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb3102b-78d1-4cd0-b8cc-5730761eaf31",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "f61cc85d-07f1-42e6-b3cc-0455073f6aec",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nLLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\\cls{}), execution output generation (\\cwm{}), and trajectory-level patch scoring (\\traj{}). No prior work compares these formulations under matched conditions.\n\nWe present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\\leq}$8B LoRA fine-tuning. Our primary finding is function-level near-equivalence: \\cls{} and \\cwm{} achieve statistical equivalence across both families (TOST $p{=}0.007$, $\\pm$2\\pp{} margin, 5 seeds, Holm-Bonferroni corrected), establishing that classification is not inherently easier than generation when outputs are short (${\\leq}$1.3\\pp{} gap). \\traj{} reaches parity on Qwen3 but exceeds the equivalence margin on DeepSeek-Coder (2.69\\pp{}), revealing model-dependent sensitivity. At repository level, a robust per-test interaction ($z{=}-23.7$, $n{=}56{,}480$) confirms this equivalence collapses: the \\cls{}--\\cwm{} gap widens from ${\\leq}$1.3\\pp{} to 19--26\\pp{} in single-seed variant-level evaluation, driven by format collapse in generation-based simulation; gap magnitude depends on multiple confounds.\n\nError complementarity across formulations (oracle ensemble: 90.63\\%) and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.\n\\end{abstract}",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "0bb3102b-78d1-4cd0-b8cc-5730761eaf31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T06:35:29.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ULnEAoeXWRwvhw2FC2se3N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f61cc85d-07f1-42e6-b3cc-0455073f6aec",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "3f1d65d5-9cf7-4664-bc75-4a84d4fff06c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 25 · 2026-05-21T06:35:29.708Z_

<details><summary>↩ Tool result · `toolu_01ULnEAoeXWRwvhw2FC2se3N`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	These three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that isolates formulation effects from confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\S\ref{sec:repo}), error complementarity findings with practical ensemble implications (\S\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\S\ref{sec:conclusion}). The results reveal a three-layer structure. Fine-tuning is necessary under standard prompting (0-shot$\to$fine-tuned gains of 35--36\pp{} at repo level). After fine-tuning, \emph{formulation choice is governed by code complexity}: at function level, \cls{} and \cwm{} achieve statistical equivalence (TOST $p{=}0.007$, 5 seeds)---a non-obvious result given that \cwm{} predicts $O(L)$ tokens per test versus \cls{}'s single binary token; \traj{} reaches parity on Qwen3 but not DeepSeek-Coder. At repository level under our ${\leq}$8B LoRA protocol, a robust per-test interaction ($z{=}-23.7$) confirms complexity-dependent divergence; variant-level gap magnitude (19--26\pp{}, single-seed) is consistent across families but depends on multiple confounds (\S\ref{sec:threats}). Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Formulation near-equivalence at low complexity.} At function level, \cls{} and \cwm{} achieve statistical equivalence across two representative code LLM families; \traj{} reaches parity on Qwen3 but exceeds the equivalence margin on DeepSeek-Coder, revealing model-dependent sensitivity. Per-test classification matches trajectory-level accuracy while identifying which tests fail, though a re-repair pilot found no downstream benefit ($n{=}44$, $p{=}0.42$) (\S\ref{sec:func_results}, \S\ref{sec:equivalence}, \S\ref{sec:analysis}).
14	
15	\item \textbf{Complexity-dependent divergence.} A robust interaction ($z{=}-23.7$, $n{=}56{,}480$) confirms that formulations equivalent at function level (${\leq}$1.3\pp{}) diverge by 19--26\pp{} at repository level under ${\leq}$8B LoRA fine-tuning, driven by format collapse; variant-level analysis reveals three failure modes consistent across model families, though gap magnitude depends on single-seed evaluation and multiple confounds (\S\ref{sec:repo}, \S\ref{sec:threats}).
16	
17	\item \textbf{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary error patterns at function level (oracle ensemble: 90.63\%, +2.80\pp{}); at repo level, oracle routing across configurations reaches 95.83\% variant accuracy (+14.58\pp{} over best single), the strongest practical argument for exploring the formulation design space (\S\ref{sec:analysis}).
18	\end{itemize}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f1d65d5-9cf7-4664-bc75-4a84d4fff06c",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "c69daee1-77a6-4b29-a36c-0e474439be2a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\\cite{snell2024scaling}. Full execution verification is reliable but expensive (\\$1--3 per candidate at repository scale\\footnote{Based on per-instance costs reported by \\citet{yang2024sweagent} and \\citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \\textbf{generation-based simulation}~\\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \\textbf{trajectory-level scoring}~\\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \\textbf{per-test classification}~\\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.\n\nDespite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?\n\nThese three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that isolates formulation effects from confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\\S\\ref{sec:repo}), error complementarity findings with practical ensemble implications (\\S\\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\\S\\ref{sec:conclusion}). The results reveal a three-layer structure. Fine-tuning is necessary under standard prompting (0-shot$\\to$fine-tuned gains of 35--36\\pp{} at repo level). After fine-tuning, \\emph{formulation choice is governed by code complexity}: at function level, \\cls{} and \\cwm{} achieve statistical equivalence (TOST $p{=}0.007$, 5 seeds)---a non-obvious result given that \\cwm{} predicts $O(L)$ tokens per test versus \\cls{}'s single binary token; \\traj{} reaches parity on Qwen3 but not DeepSeek-Coder. At repository level under our ${\\leq}$8B LoRA protocol, a robust per-test interaction ($z{=}-23.7$) confirms complexity-dependent divergence; variant-level gap magnitude (19--26\\pp{}, single-seed) is consistent across families but depends on multiple confounds (\\S\\ref{sec:threats}). Figure~\\ref{fig:reformulation} illustrates the three formulations.\n\nWe make the following contributions:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Formulation near-equivalence at low complexity.} At function level, \\cls{} and \\cwm{} achieve statistical equivalence across two representative code LLM families; \\traj{} reaches parity on Qwen3 but exceeds the equivalence margin on DeepSeek-Coder, revealing model-dependent sensitivity. Per-test classification matches trajectory-level accuracy while identifying which tests fail, though a re-repair pilot found no downstream benefit ($n{=}44$, $p{=}0.42$) (\\S\\ref{sec:func_results}, \\S\\ref{sec:equivalence}, \\S\\ref{sec:analysis}).\n\n\\item \\textbf{Complexity-dependent divergence.} A robust interaction ($z{=}-23.7$, $n{=}56{,}480$) confirms that formulations equivalent at function level (${\\leq}$1.3\\pp{}) diverge by 19--26\\pp{} at repository level under ${\\leq}$8B LoRA fine-tuning, driven by format collapse; variant-level analysis reveals three failure modes consistent across model families, though gap magnitude depends on single-seed evaluation and multiple confounds (\\S\\ref{sec:repo}, \\S\\ref{sec:threats}).\n\n\\item \\textbf{Error complementarity.} \\cls{} and \\cwm{} exhibit partially complementary error patterns at function level (oracle ensemble: 90.63\\%, +2.80\\pp{}); at repo level, oracle routing across configurations reaches 95.83\\% variant accuracy (+14.58\\pp{} over best single), the strongest practical argument for exploring the formulation design space (\\S\\ref{sec:analysis}).\n\\end{itemize}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "3f1d65d5-9cf7-4664-bc75-4a84d4fff06c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T06:35:30.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_015M9bFZLa26VXkncVhmVhWS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69daee1-77a6-4b29-a36c-0e474439be2a",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "46d87222-3c2a-4ab9-92c9-6dd58ecd711c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 27 · 2026-05-21T06:35:30.175Z_

<details><summary>↩ Tool result · `toolu_015M9bFZLa26VXkncVhmVhWS`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. Our \cls{} provides per-test (process) supervision while \traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} enable parameter-efficient fine-tuning. Task framing~\cite{raffel2020t5,lewis2020bart,rajpurkar2016squad} affects model performance; we extend this to code verification, finding complexity moderates the tradeoff.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46d87222-3c2a-4ab9-92c9-6dd58ecd711c",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "a130af7e-2bc9-4697-90ab-3b10370fe478",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Execution Simulation and Verification.}\nExecution trace generation improves code reasoning~\\cite{nye2021scratchpad}, with extensions to output prediction~\\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\\cite{abdollahi2025demystifying}, and error detection~\\cite{li2024redo}. Verification formulations span trajectory-level reward~\\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\\cite{ni2023lever,chen2023codet}, learned metrics~\\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\\cite{wang2026verpo,tang2026execverify}. Aletheia~\\cite{venkatkrishna2026aletheia} compares training recipes; we compare \\emph{formulations}. Test-time scaling~\\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.\n\n\\paragraph{Process vs.\\ Outcome Supervision.}\nPRMs outperform ORMs for math reasoning~\\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. Our \\cls{} provides per-test (process) supervision while \\traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\\cwm{} generation vs.\\ \\cls{} classification).\n\n\\paragraph{Repair, Mutation Testing, and Task Framing.}\nCodeRL~\\cite{le2022coderl}, AlphaCode~\\cite{li2022alphacode,alphacode2023team}, and Reflexion~\\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\\cite{yang2024sweagent} and Agentless~\\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\\cite{yang2025aprsurvey}. Predictive mutation testing~\\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. LoRA~\\cite{hu2022lora} and QLoRA~\\cite{dettmers2024qlora} enable parameter-efficient fine-tuning. Task framing~\\cite{raffel2020t5,lewis2020bart,rajpurkar2016squad} affects model performance; we extend this to code verification, finding complexity moderates the tradeoff.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "46d87222-3c2a-4ab9-92c9-6dd58ecd711c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T06:35:30.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ko2Z1YAZS5tLAM3QLZHwE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a130af7e-2bc9-4697-90ab-3b10370fe478",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "6e3322a2-63c1-464a-8cb6-82769fcb2c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 29 · 2026-05-21T06:35:30.692Z_

<details><summary>↩ Tool result · `toolu_018ko2Z1YAZS5tLAM3QLZHwE`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$, making long outputs exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	For a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}$, where $k_{\text{eff}} = k / (1 + (k-1)\rho)$ accounts for within-patch correlation via ICC $\rho$~\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\Delta(k) = P_{\text{detect}}(k) - a_h$, with population expectation $\mathbb{E}[\Delta] = \sum_{k} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \S\ref{sec:experiments} and Appendix~\ref{app:oracle}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e3322a2-63c1-464a-8cb6-82769fcb2c19",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "f4156409-a912-4ca8-8f5b-a068d897a587",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nLet $p$ denote a candidate patch and $T = \\{t_1, \\ldots, t_n\\}$ its test suite, where each $t_i$ has label $y_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ from execution. Tests decompose into \\emph{fail-to-pass} ($T_{\\text{f2p}}$) and \\emph{pass-to-pass} ($T_{\\text{p2p}}$) subsets; a patch is correct iff $\\forall\\, t_i{:}\\ y_i = \\text{\\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.\n\n\\subsection{Verification Formulations}\n\\label{sec:formulations}\n\nLet $c_p$ denote the code context (unified diff) of patch $p$.\n\n\\paragraph{\\cls{} (per-test classification).} $f(c_p, t_i) \\rightarrow \\hat{y}_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\\hat{y}_p = \\bigwedge_{i} [\\hat{y}_i = \\text{\\textsc{Pass}}]$. Output cost: one token per test.\n\n\\paragraph{\\cwm{} (output generation).} $g(c_p, t_i) \\rightarrow \\hat{o}_i \\in \\Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\\hat{y}_i = \\text{\\textsc{Pass}}$ iff $\\hat{o}_i = o_i^*$.\\footnote{Exact string matching is conservative, consistent with \\citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\\sum_i |\\hat{o}_i|$ tokens.\n\n\\paragraph{\\traj{} (trajectory-level).} $h(c_p, T) \\rightarrow \\hat{y}_p \\in \\{\\text{\\textsc{Resolved}}, \\text{\\textsc{Unresolved}}\\}$ predicts a single patch verdict from all tests and provides no per-test signal. \\traj{} serves as a granularity control: \\cls{}--\\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.\n\n\\subsection{Formulation-Specific Failure Modes}\n\\label{sec:failure-modes}\n\nEach formulation has characteristic failure modes that differ in their sensitivity to code complexity:\n\n\\paragraph{Generation failure modes (\\cwm{}).} The open-ended output space introduces three failure modes: (1)~\\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$, making long outputs exponentially harder to predict exactly. We adopt exact string matching following the original \\cwm{} evaluation protocol~\\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\\textsc{Pass}).\n\n\\paragraph{Classification failure modes (\\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \\cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.\n\n\\paragraph{Trajectory-level failure modes (\\traj{}).} By collapsing all per-test information into a single binary verdict, \\traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \\emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.\n\n\\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \\S\\ref{sec:experiments}.\n\n\\subsection{Oracle Accuracy-Utility Framework}\n\\label{sec:oracle}\n\nFor a buggy patch with $k = |T_{\\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\\text{detect}}(k) = 1 - (1 - r)^{k_{\\text{eff}}}$, where $k_{\\text{eff}} = k / (1 + (k-1)\\rho)$ accounts for within-patch correlation via ICC $\\rho$~\\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\\Delta(k) = P_{\\text{detect}}(k) - a_h$, with population expectation $\\mathbb{E}[\\Delta] = \\sum_{k} P(|T_{\\text{f2p}}| = k) \\cdot \\Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \\S\\ref{sec:experiments} and Appendix~\\ref{app:oracle}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "6e3322a2-63c1-464a-8cb6-82769fcb2c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T06:35:31.591Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xt647hYqkVEHMF4XmEUyjb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4156409-a912-4ca8-8f5b-a068d897a587",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "dfc046db-79bc-44e5-adc8-011147b53969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 31 · 2026-05-21T06:35:31.598Z_

<details><summary>↩ Tool result · `toolu_01Xt647hYqkVEHMF4XmEUyjb`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations); per-test vs.\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2 percentage point (\pp{}) margin. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the four primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over seeds. Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{} evaluated on 1,032-sample subset (447 matched variants).}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & \underline{87.19 $\pm$ 0.37} \\
39	\traj{} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 68.70 \\
48	0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\
49	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
50	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
51	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
52	3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\
53	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
54	\midrule
55	Majority (pass) & --- & --- & 51.75 \\
56	\bottomrule
57	\end{tabular}}
58	\end{table}
59	
60	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} gap is model-dependent: $<$1\pp{} on Qwen3 but 2.69\pp{} on DeepSeek-Coder, exceeding the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 13--26\pp{}).
61	
62	
63	\subsection{Scaling Behavior}
64	\label{sec:scaling}
65	
66	Table~\ref{tab:scaling} compares all three formulations at two model sizes using seeds 42 and 123, both trained in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).
67	
68	\begin{table}[t]
69	\centering
70	\small
71	\caption{Model-size scaling: accuracy (\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \cls{} and \traj{} scale positively; \cwm{} does not.}
72	\label{tab:scaling}
73	\setlength{\tabcolsep}{4pt}
74	\begin{tabular}{llcccc}
75	\toprule
76	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{Mean} & \textbf{$\Delta$ 4B$\to$8B} \\
77	\midrule
78	\cls{} & 4B & 87.83 & 89.52 & \textbf{88.68} & \multirow{2}{*}{+1.27} \\
79	\cls{} & 8B & \textbf{90.48} & 89.40 & \textbf{89.94} & \\
80	\midrule
81	\cwm{} & 4B & 87.51 & 87.20 & \underline{87.36} & \multirow{2}{*}{$-$0.03} \\
82	\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\
83	\midrule
84	\traj{} & 4B & 85.27 & 86.72 & 86.00 & \multirow{2}{*}{+1.70} \\
85	\traj{} & 8B & 87.60 & 87.79 & \underline{87.70} & \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +1.70\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
91	
92	\cwm{} flat scaling ($-$0.03\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \emph{cannot} benefit from scale. At function level, outputs are short (integers, booleans) and format compliance is near-perfect; at repo level, output length grows to ${\sim}$477 tokens on average, and the same generation bottleneck manifests as format collapse (51--74\% unparseable; \S\ref{sec:repo}). \traj{} also shows no scaling benefit at repo level (72.92\% at both 4B and 8B); only \cls{} scales positively across both complexity levels.
93	
94	
95	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
96	\label{sec:equivalence}
97	
98	We compare \cls{} (aggregated via all-pass rule) against \traj{} on 523 variant-level instances across five seeds.\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16. Restricting to bfloat16 seeds only (3 seeds) yields $p{=}0.128$: consistent in direction but underpowered due to reduced seed coverage.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin, Holm-Bonferroni corrected). Our $\pm$2\pp{} threshold follows the SESOI framework~\cite{lakens2017}, set independently of the observed gap and grounded in deployment relevance: at function-level accuracy (85--88\%), a 2\pp{} difference corresponds to ${\sim}$38 per-test predictions across 1,890 tests (${\sim}$2--3 problems out of 114)---comparable to between-seed variation (0.37--0.97\pp{} std, Table~\ref{tab:main_results}) and checkpoint selection noise ($<$1\pp{}, \S\ref{sec:threats}). A difference within this range is indistinguishable from training noise for pipeline selection decisions. Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}), well below the pre-specified threshold. Within-problem predictions are correlated (intraclass correlation ICC $= 0.191$, $p < 0.0001$, design effect (DEFF) $= 3.97$); all statistical tests use clustered bootstrap accordingly. On DeepSeek-Coder, the observed \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence, but with only 2 seeds the comparison is underpowered. Notably, the DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin, indicating that \traj{} parity is model-dependent rather than universal; the \cls{}--\cwm{} equivalence is robust across both families. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy, a result that parallels process supervision~\cite{lightman2023letsverify}, where step-level verification enables error localization without accuracy cost.
99	
100	Oracle analysis on SWE-bench Verified (500 instances) shows that per-test advantage concentrates at $T \geq 2$ fail-to-pass tests (31.3\% of instances, contributing 55.3\% of the total oracle advantage; Appendix~\ref{app:oracle}).
101	
102	
103	\subsection{Repo-Level: Complexity-Dependent Divergence}
104	\label{sec:repo}
105	
106	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons rely on limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
107	
108	\begin{table}[t]
109	\centering
110	\small
111	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{} multi-seed runs in progress.}
112	\label{tab:repo_level}
113	\resizebox{\columnwidth}{!}{%
114	\setlength{\tabcolsep}{4pt}
115	\begin{tabular}{lcccc}
116	\toprule
117	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
118	\midrule
119	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
120	Qwen3-8B & \textbf{84.83 $\pm$ 0.66} & 72.92 / 81.25\textsuperscript{$\dagger$} & \tbd{} & 72.91 $\pm$ 3.61 \\
121	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & \tbd{} & 77.08 $\pm$ 3.61 \\
122	\midrule
123	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
124	0-shot (DeepSeek) & 48.50 & --- & --- & --- \\
125	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
126	\bottomrule
127	\end{tabular}}
128	
129	\vspace{2pt}
130	{\footnotesize \textsuperscript{$\dagger$}Individual-seed variant accuracy; multi-seed aggregate pending. \textsuperscript{$\ddagger$}One seed used truncate preprocessing (vs.\ drop for the other two), producing NaN validation loss and preventing checkpoint selection---a qualitatively different evaluation configuration (decision collapse; Table~\ref{tab:taxonomy}). The mean is over the two matched-preprocessing seeds. \textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses epoch-3 checkpoint (val loss undefined); see text for checkpoint sensitivity analysis.}
131	\end{table}
132	
133	Zero-shot prompting collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}).
134	
135	\paragraph{Formulation divergence (single-seed).} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). \cwm{} falls below majority baseline at both scales. These gaps suggest complexity-dependent formulation effectiveness, though single-seed design and multiple confounds (\S\ref{sec:threats}) preclude definitive causal attribution.
136	
137	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) under single-seed constraints. DeepSeek \cls{} degradation ranges from ${\sim}$4\pp{} (s42, drop preprocessing) to ${\sim}$12\pp{} (s123, truncate preprocessing), reflecting preprocessing and checkpoint selection sensitivity (Table~\ref{tab:taxonomy}). The \cls{}--\cwm{} gap magnitude also varies across families (20\pp{} for Qwen3 vs.\ 23--28\pp{} for DeepSeek), primarily reflecting checkpoint selection: DeepSeek \cwm{}'s val-selected checkpoint (56.70\%) underperforms its epoch-3 checkpoint (61.49\%), widening the apparent gap. Under matched checkpoint selection (epoch~3 for both), the cross-model gap difference narrows to ${\sim}$2\pp{} (Qwen3: 20.47\pp{} vs.\ DeepSeek: 22.89\pp{}), confirming the gap is formulation-driven rather than model-specific. Eval seq\_length differs between models (Appendix~\ref{app:threats}).
138	
139	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$, Appendix Table~\ref{tab:variant_level}) reveals three failure modes (Table~\ref{tab:taxonomy}): format collapse (\cwm{}, 51--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\%). Downsampling \cls{} training data to match \traj{}'s data volume yields 80.74\%, still 7.82\pp{} above \traj{}; this controls data volume but not label granularity (per-test vs.\ variant-level), and remains a single-seed comparison (Appendix~\ref{app:downsample}).
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
145	\label{tab:taxonomy}
146	\setlength{\tabcolsep}{3pt}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
150	\midrule
151	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
152	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
153	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
154	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), which inflates accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%; Appendix~\ref{app:parseable_bias}).
160	
161	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 19--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}).
162	
163	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects linear probability model with problem-level random intercepts ($n{=}56{,}480$ observations, 139 problem clusters, DeepSeek-Coder) confirms the interaction: the \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}) but diverge by 22\pp{} at repo level, confirming the divergence is not an artifact of aggregation. The cross-complexity analysis uses DeepSeek-Coder, the only family with both function- and repo-level \cwm{} evaluations under matched conditions. Across both model families at repo level, the \cwm{} deficit is $-$22\pp{} ($z{=}-64.4$, $p{<}0.001$); the model family effect is significant but small (+1.1\pp{} for Qwen3, $p{=}0.002$), and the formulation$\times$model interaction is likewise small (+1.6\pp{}, $p{=}0.006$). Formulation explains $>$95\% of the predictable variance; model identity modulates gap magnitude without changing direction (Appendix~\ref{app:interaction}).
164	
165	Additional repo-level limitations appear in Appendix~\ref{app:limitations}.
166	
167	
168	\subsection{Analysis}
169	\label{sec:analysis}
170	
171	\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict. The penalty ranges from 1.36\pp{} (DeepSeek s42) to 19\pp{} (Qwen3-4B), depending on fail recall and test count (Appendix Table~\ref{tab:variant_level}). Val-based checkpoint selection biases toward per-test accuracy at the expense of fail recall, which amplifies the penalty. \traj{} avoids this by predicting variant outcomes directly (72.91--77.08\%). The penalty is predictable from test count: function-level variants ($\bar{T} \approx 2.3$) incur negligible penalty, while repo-level variants ($\bar{T} \gg 10$) incur substantial penalty, both the \emph{advantage} and \emph{cost} of per-test granularity concentrate at high $T$ (Appendix~\ref{app:extended_analysis}(a)).
172	
173	\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short strings (integers, booleans); repo-level outputs are unconstrained execution traces (mean ${\sim}$477 tokens) where errors compound multiplicatively, and cause format collapse (53--74\% unparseable). Even among parseable outputs, accuracy (38--43\%) is below majority baseline, which indicates a semantic gap beyond format compliance (Appendix~\ref{app:qualitative}).
174	
175	\cls{} achieves 217$\times$ higher throughput than \cwm{} (1 output token vs.\ avg 477), consistent across both model families.
176	
177	\paragraph{Error complementarity.} At function level, \cls{} and \cwm{} exhibit partial complementarity: both are FP-dominant (over-predict failure), but at different rates (\cls{} 56.5\%, \cwm{} 70.3\%; Appendix~\ref{app:extended_analysis}(a)), so \cwm{} over-predicts failure on instances \cls{} correctly classifies. An oracle combination achieves 90.63\% (+2.80\pp{} over the best single formulation; single-seed estimate). At repo level, oracle routing across configurations reaches 95.83\% variant accuracy (+14.58\pp{} over the best single configuration, $n{=}48$), the strongest evidence that the formulation design space contains complementary solutions worth exploring. A re-repair pilot found no benefit from per-test diagnostics ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)). Extended analysis appears in Appendix~\ref{app:extended_analysis}.
178	
179	\subsection{Threats to Validity}
180	\label{sec:threats}
181	
182	We identify five potential confounds and assess their individual impact in Appendix~\ref{app:threats}: checkpoint selection (a checkpoint ablation on Qwen3-8B \cls{} s42 shows $<$1\pp{} variation: epoch~1 85.34\%, val-selected 84.48\%, final 85.29\%; \cwm{} epoch ablation shows $<$2\pp{} difference between epochs 2--3, suggesting training duration is not the primary driver of \cwm{} underperformance; NaN validation loss forces final-epoch default in all \cwm{} runs and DeepSeek s123), evaluation sequence length (${\sim}$1.5\pp{} for \cls{}), preprocessing (qualitative ranking holds; the ${\sim}$8\pp{} cross-configuration variance in DeepSeek \cls{} is predominantly preprocessing-driven), \traj{} training regime (downsample confirms formulation advantage), and \cwm{} scale/pretraining (primary limitation; all repo-level \cwm{} conclusions conditional on the ${\leq}$8B LoRA regime). The 19--26\pp{} gap exceeds any single assessed confound, but the combination of limited seeds and correlated confounds means definitive causal attribution requires the multi-seed replication currently underway. Holm-Bonferroni correction confirms the two core claims survive (adjusted $p{=}0.012$ and $p{=}0.021$; Table~\ref{tab:holm}).
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc046db-79bc-44e5-adc8-011147b53969",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "123716d8-3ceb-4ae6-99a8-ef1f48205d71",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe systematically compare \\cls{}, \\cwm{}, and \\traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\n\\emph{Function-level}: mutated variants from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\\emph{Repo-level}: per-test instances from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants. ${\\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\\%). Val-based checkpoint selection follows standard practice~\\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \\cls{} s123, all \\cwm{} runs, and Qwen3 \\traj{} runs; see Appendix~\\ref{app:hyperparams}).\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \\S\\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \\cls{} and \\cwm{}). Our \\cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Statistics.}\nConfidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations); per-test vs.\\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\\cite{schuirmann1987tost} with $\\pm$2 percentage point (\\pp{}) margin. Holm-Bonferroni correction~\\cite{holm1979} controls family-wise error rate across the four primary comparisons (Table~\\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations and model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\\pm$ std over seeds. Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \\traj{} evaluated on 1,032-sample subset (447 matched variants).}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Qwen3 (primary)}} \\\\\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & \\underline{87.19 $\\pm$ 0.37} \\\\\n\\traj{} (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{DeepSeek-Coder (cross-model consistency check)}} \\\\\n\\cls{} (fine-tuned) & 6.7B & 2 & \\textbf{86.85 $\\pm$ 0.11} \\\\\n\\cwm{} (fine-tuned) & 6.7B & 2 & \\underline{86.83 $\\pm$ 1.49} \\\\\n\\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\\pm$ 1.30 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Prompting baselines}} \\\\\n0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\\nZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\\\\nZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\\n\\midrule\nMajority (pass) & --- & --- & 51.75 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll three formulations achieve comparable accuracy on Qwen3-4B: \\cls{} 88.43\\% ($\\pm$0.78), \\cwm{} 87.19\\% ($\\pm$0.37), \\traj{} 86.30\\% ($\\pm$0.97). DeepSeek-Coder-6.7B shows: \\cls{} 86.85\\%, \\cwm{} 86.83\\%, \\traj{} 84.16\\%. The \\cls{}--\\cwm{} gap (0.02--1.24\\pp{}) is within seed noise in both families. However, the \\cls{}--\\traj{} gap is model-dependent: $<$1\\pp{} on Qwen3 but 2.69\\pp{} on DeepSeek-Coder, exceeding the $\\pm$2\\pp{} equivalence margin (\\S\\ref{sec:equivalence}). \\cls{} and \\cwm{} are robustly equivalent; \\traj{} parity is model-contingent. Zero-shot baselines (Tables~\\ref{tab:main_results} and~\\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\\to$fine-tuned gains of 35--36\\pp{}) and that formulation choice matters only at repo level (\\cls{} outperforms \\cwm{} by 13--26\\pp{}).\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares all three formulations at two model sizes using seeds 42 and 123, both trained in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \\cls{} and \\traj{} scale positively; \\cwm{} does not.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$ 4B$\\to$8B} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & \\textbf{88.68} & \\multirow{2}{*}{+1.27} \\\\\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & \\\\\n\\midrule\n\\cwm{} & 4B & 87.51 & 87.20 & \\underline{87.36} & \\multirow{2}{*}{$-$0.03} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\\\\n\\midrule\n\\traj{} & 4B & 85.27 & 86.72 & 86.00 & \\multirow{2}{*}{+1.70} \\\\\n\\traj{} & 8B & 87.60 & 87.79 & \\underline{87.70} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +1.70\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short (integers, booleans) and format compliance is near-perfect; at repo level, output length grows to ${\\sim}$477 tokens on average, and the same generation bottleneck manifests as format collapse (51--74\\% unparseable; \\S\\ref{sec:repo}). \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nWe compare \\cls{} (aggregated via all-pass rule) against \\traj{} on 523 variant-level instances across five seeds.\\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16. Restricting to bfloat16 seeds only (3 seeds) yields $p{=}0.128$: consistent in direction but underpowered due to reduced seed coverage.} The pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\\pm$2\\pp{} margin, Holm-Bonferroni corrected). Our $\\pm$2\\pp{} threshold follows the SESOI framework~\\cite{lakens2017}, set independently of the observed gap and grounded in deployment relevance: at function-level accuracy (85--88\\%), a 2\\pp{} difference corresponds to ${\\sim}$38 per-test predictions across 1,890 tests (${\\sim}$2--3 problems out of 114)---comparable to between-seed variation (0.37--0.97\\pp{} std, Table~\\ref{tab:main_results}) and checkpoint selection noise ($<$1\\pp{}, \\S\\ref{sec:threats}). A difference within this range is indistinguishable from training noise for pipeline selection decisions. Equivalence holds at margins as tight as $\\pm$1.52\\pp{} (Table~\\ref{tab:tost_sensitivity}), well below the pre-specified threshold. Within-problem predictions are correlated (intraclass correlation ICC $= 0.191$, $p < 0.0001$, design effect (DEFF) $= 3.97$); all statistical tests use clustered bootstrap accordingly. On DeepSeek-Coder, the observed \\cls{}--\\cwm{} gap of 0.02\\pp{} is consistent with equivalence, but with only 2 seeds the comparison is underpowered. Notably, the DeepSeek \\cls{}--\\traj{} gap (2.69\\pp{}) exceeds the $\\pm$2\\pp{} margin, indicating that \\traj{} parity is model-dependent rather than universal; the \\cls{}--\\cwm{} equivalence is robust across both families. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy, a result that parallels process supervision~\\cite{lightman2023letsverify}, where step-level verification enables error localization without accuracy cost.\n\nOracle analysis on SWE-bench Verified (500 instances) shows that per-test advantage concentrates at $T \\geq 2$ fail-to-pass tests (31.3\\% of instances, contributing 55.3\\% of the total oracle advantage; Appendix~\\ref{app:oracle}).\n\n\n\\subsection{Repo-Level: Complexity-Dependent Divergence}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons rely on limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\\S\\ref{sec:setup}); the test set has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \\cls{}/\\traj{}: mean $\\pm$ std over 3 seeds; DeepSeek \\cls{}: 2 seeds\\textsuperscript{$\\ddagger$}; DeepSeek \\traj{}: 3 seeds; Qwen3-4B: seed 42. \\cwm{} multi-seed runs in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{\\cls{} (\\%)} & \\textbf{\\cls{} Var.\\ (\\%)} & \\textbf{\\cwm{} (\\%)} & \\textbf{\\traj{} Var.\\ (\\%)\\textsuperscript{$\\diamond$}} \\\\\n\\midrule\nQwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\\\\nQwen3-8B & \\textbf{84.83 $\\pm$ 0.66} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & \\tbd{} & 72.91 $\\pm$ 3.61 \\\\\nDeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & \\tbd{} & 77.08 $\\pm$ 3.61 \\\\\n\\midrule\n0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\\\\n0-shot (DeepSeek) & 48.50 & --- & --- & --- \\\\\nMajority & 72.96 & 54.17 & 72.96 & 54.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}Individual-seed variant accuracy; multi-seed aggregate pending. \\textsuperscript{$\\ddagger$}One seed used truncate preprocessing (vs.\\ drop for the other two), producing NaN validation loss and preventing checkpoint selection---a qualitatively different evaluation configuration (decision collapse; Table~\\ref{tab:taxonomy}). The mean is over the two matched-preprocessing seeds. \\textsuperscript{$\\diamond$}Var.\\ columns: variant-level accuracy ($n{=}48$); \\cls{} aggregated via all-pass rule; \\traj{} by design. Per-test: $n{=}9{,}784$. \\cwm{} unparseable: 54\\% (4B); default to pass; parseable-only 38--43\\%, below majority. Eval seq\\_length differs across models (Appendix~\\ref{app:threats}). \\cwm{} uses epoch-3 checkpoint (val loss undefined); see text for checkpoint sensitivity analysis.}\n\\end{table}\n\nZero-shot prompting collapses to an always-predict-unresolved baseline (variant accuracy 45.83\\%, below majority 54.17\\%; Appendix~\\ref{app:few_shot}).\n\n\\paragraph{Formulation divergence (single-seed).} Under our 4--8B LoRA protocol, \\cls{} and \\cwm{} diverge on Qwen3: the gap is 25.59\\pp{} at 4B (\\cls{} 83.63\\% vs.\\ \\cwm{} 58.04\\%, seed 42; Figure~\\ref{fig:scaling_gap}) and 19.31\\pp{} at 8B (84.48\\% vs.\\ 65.17\\%). \\cwm{} falls below majority baseline at both scales. These gaps suggest complexity-dependent formulation effectiveness, though single-seed design and multiple confounds (\\S\\ref{sec:threats}) preclude definitive causal attribution.\n\n\\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\\cls{} $>$ \\cwm{}) under single-seed constraints. DeepSeek \\cls{} degradation ranges from ${\\sim}$4\\pp{} (s42, drop preprocessing) to ${\\sim}$12\\pp{} (s123, truncate preprocessing), reflecting preprocessing and checkpoint selection sensitivity (Table~\\ref{tab:taxonomy}). The \\cls{}--\\cwm{} gap magnitude also varies across families (20\\pp{} for Qwen3 vs.\\ 23--28\\pp{} for DeepSeek), primarily reflecting checkpoint selection: DeepSeek \\cwm{}'s val-selected checkpoint (56.70\\%) underperforms its epoch-3 checkpoint (61.49\\%), widening the apparent gap. Under matched checkpoint selection (epoch~3 for both), the cross-model gap difference narrows to ${\\sim}$2\\pp{} (Qwen3: 20.47\\pp{} vs.\\ DeepSeek: 22.89\\pp{}), confirming the gap is formulation-driven rather than model-specific. Eval seq\\_length differs between models (Appendix~\\ref{app:threats}).\n\n\\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$, Appendix Table~\\ref{tab:variant_level}) reveals three failure modes (Table~\\ref{tab:taxonomy}): format collapse (\\cwm{}, 51--74\\% unparseable), decision collapse (\\cls{} under truncate preprocessing, fail recall ${\\sim}$14\\%), and aggregation penalty (\\cls{} under drop preprocessing, fail recall 38--57\\%). Decision collapse is configuration-dependent, not model-inherent. \\traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\\%). Downsampling \\cls{} training data to match \\traj{}'s data volume yields 80.74\\%, still 7.82\\pp{} above \\traj{}; this controls data volume but not label granularity (per-test vs.\\ variant-level), and remains a single-seed comparison (Appendix~\\ref{app:downsample}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\\%.}\n\\label{tab:taxonomy}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Representative} & \\textbf{Fail Recall} & \\textbf{Variant Acc} \\\\\n\\midrule\nFormat collapse & \\cwm{} (all) & N/A & 48--52\\% \\\\\nDecision collapse & \\cls{} (DeepSeek, s123) & ${\\sim}$14\\% & 56\\% \\\\\nAggr.\\ penalty & \\cls{} (Qwen3-8B) & 51--57\\% & 73--81\\% \\\\\nAggr.\\ penalty & \\cls{} (DeepSeek, s42) & 38--51\\% & 79--81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Default assignment artifact.} The apparent \\cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\\%$\\to$73.8\\%), which inflates accuracy via majority-class default while parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%; Appendix~\\ref{app:parseable_bias}).\n\n\\paragraph{Complexity as moderator.} The \\cls{}--\\cwm{} gap widens from 1--3\\pp{} (function) to 19--26\\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\\% of this gap (Appendix~\\ref{app:ablations}).\n\n\\paragraph{Formulation$\\times$complexity interaction.} A mixed-effects linear probability model with problem-level random intercepts ($n{=}56{,}480$ observations, 139 problem clusters, DeepSeek-Coder) confirms the interaction: the \\cwm{} effect at function level is negligible ($\\hat{\\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}) but diverge by 22\\pp{} at repo level, confirming the divergence is not an artifact of aggregation. The cross-complexity analysis uses DeepSeek-Coder, the only family with both function- and repo-level \\cwm{} evaluations under matched conditions. Across both model families at repo level, the \\cwm{} deficit is $-$22\\pp{} ($z{=}-64.4$, $p{<}0.001$); the model family effect is significant but small (+1.1\\pp{} for Qwen3, $p{=}0.002$), and the formulation$\\times$model interaction is likewise small (+1.6\\pp{}, $p{=}0.006$). Formulation explains $>$95\\% of the predictable variance; model identity modulates gap magnitude without changing direction (Appendix~\\ref{app:interaction}).\n\nAdditional repo-level limitations appear in Appendix~\\ref{app:limitations}.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict. The penalty ranges from 1.36\\pp{} (DeepSeek s42) to 19\\pp{} (Qwen3-4B), depending on fail recall and test count (Appendix Table~\\ref{tab:variant_level}). Val-based checkpoint selection biases toward per-test accuracy at the expense of fail recall, which amplifies the penalty. \\traj{} avoids this by predicting variant outcomes directly (72.91--77.08\\%). The penalty is predictable from test count: function-level variants ($\\bar{T} \\approx 2.3$) incur negligible penalty, while repo-level variants ($\\bar{T} \\gg 10$) incur substantial penalty, both the \\emph{advantage} and \\emph{cost} of per-test granularity concentrate at high $T$ (Appendix~\\ref{app:extended_analysis}(a)).\n\n\\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short strings (integers, booleans); repo-level outputs are unconstrained execution traces (mean ${\\sim}$477 tokens) where errors compound multiplicatively, and cause format collapse (53--74\\% unparseable). Even among parseable outputs, accuracy (38--43\\%) is below majority baseline, which indicates a semantic gap beyond format compliance (Appendix~\\ref{app:qualitative}).\n\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} (1 output token vs.\\ avg 477), consistent across both model families.\n\n\\paragraph{Error complementarity.} At function level, \\cls{} and \\cwm{} exhibit partial complementarity: both are FP-dominant (over-predict failure), but at different rates (\\cls{} 56.5\\%, \\cwm{} 70.3\\%; Appendix~\\ref{app:extended_analysis}(a)), so \\cwm{} over-predicts failure on instances \\cls{} correctly classifies. An oracle combination achieves 90.63\\% (+2.80\\pp{} over the best single formulation; single-seed estimate). At repo level, oracle routing across configurations reaches 95.83\\% variant accuracy (+14.58\\pp{} over the best single configuration, $n{=}48$), the strongest evidence that the formulation design space contains complementary solutions worth exploring. A re-repair pilot found no benefit from per-test diagnostics ($n{=}44$, $p{=}0.42$; Appendix~\\ref{app:extended_analysis}(j)). Extended analysis appears in Appendix~\\ref{app:extended_analysis}.\n\n\\subsection{Threats to Validity}\n\\label{sec:threats}\n\nWe identify five potential confounds and assess their individual impact in Appendix~\\ref{app:threats}: checkpoint selection (a checkpoint ablation on Qwen3-8B \\cls{} s42 shows $<$1\\pp{} variation: epoch~1 85.34\\%, val-selected 84.48\\%, final 85.29\\%; \\cwm{} epoch ablation shows $<$2\\pp{} difference between epochs 2--3, suggesting training duration is not the primary driver of \\cwm{} underperformance; NaN validation loss forces final-epoch default in all \\cwm{} runs and DeepSeek s123), evaluation sequence length (${\\sim}$1.5\\pp{} for \\cls{}), preprocessing (qualitative ranking holds; the ${\\sim}$8\\pp{} cross-configuration variance in DeepSeek \\cls{} is predominantly preprocessing-driven), \\traj{} training regime (downsample confirms formulation advantage), and \\cwm{} scale/pretraining (primary limitation; all repo-level \\cwm{} conclusions conditional on the ${\\leq}$8B LoRA regime). The 19--26\\pp{} gap exceeds any single assessed confound, but the combination of limited seeds and correlated confounds means definitive causal attribution requires the multi-seed replication currently underway. Holm-Bonferroni correction confirms the two core claims survive (adjusted $p{=}0.012$ and $p{=}0.021$; Table~\\ref{tab:holm}).\n",
      "numLines": 183,
      "startLine": 1,
      "totalLines": 183
    }
  },
  "sourceToolAssistantUUID": "dfc046db-79bc-44e5-adc8-011147b53969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T06:35:32.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LvhXVRq4sRkBZqfAeJsAp9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "123716d8-3ceb-4ae6-99a8-ef1f48205d71",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "432fddd4-a423-4de4-9295-60a73593bdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 33 · 2026-05-21T06:35:32.080Z_

<details><summary>↩ Tool result · `toolu_01LvhXVRq4sRkBZqfAeJsAp9`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\pp{}). Per-test classification achieves 217$\times$ throughput while providing diagnostic signal whose downstream benefit was not confirmed ($n{=}44$, $p{=}0.42$). Complementary errors (oracle: 90.63\%/95.83\%) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA fine-tuning, a robust interaction ($z{=}-23.7$) confirms divergence (19--26\pp{}, single-seed variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). \cls{} is recommended for throughput; behavior at larger scale remains open~\cite{meta2025cwm}.
5	
6	\section*{Limitations}
7	
8	Most repo-level comparisons use a single seed; the gap magnitude (19--26\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training~\cite{meta2025cwm}; at larger scale, the generation bottleneck may diminish. However, matched comparison at controlled capacity isolates the formulation effect from scale confounds---complementary to work scaling execution simulators. Training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap for absolute accuracy remains untested, though the coupling effect supports relative ranking validity: our core finding---that formulation choice matters at repo level but not function level---concerns relative ordering, expected to be preserved under distributional shifts that affect all formulations equally (Appendix~\ref{app:limitations}). \traj{} training uses variant-level labels (386 instances vs.\ ${\sim}$70K for \cls{}/\cwm{}), which limits direct comparison. A re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)) found no benefit from per-test diagnostics. The mixed-effects regressions use 25--139 problem-level clusters (cross-model and cross-complexity respectively); fixed-effect estimates pool across $>$56K observations, but the random-effects structure has limited resolution for the 25-cluster model. Model coverage is limited to 6--8B code-specialized LLMs; generalization to larger or general-purpose models is untested. Extended discussion: Appendix~\ref{app:limitations}. All code, data, and model checkpoints will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "432fddd4-a423-4de4-9295-60a73593bdb8",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "aac43915-97b1-459e-a317-d69664d2ec84",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of three execution-free verification formulations (\\cls{}, \\cwm{}, \\traj{}). At function level, \\cls{} and \\cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \\traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\\pp{}). Per-test classification achieves 217$\\times$ throughput while providing diagnostic signal whose downstream benefit was not confirmed ($n{=}44$, $p{=}0.42$). Complementary errors (oracle: 90.63\\%/95.83\\%) motivate complexity-aware routing. At repository level under ${\\leq}$8B LoRA fine-tuning, a robust interaction ($z{=}-23.7$) confirms divergence (19--26\\pp{}, single-seed variant-level), with \\cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\\S\\ref{sec:threats}). \\cls{} is recommended for throughput; behavior at larger scale remains open~\\cite{meta2025cwm}.\n\n\\section*{Limitations}\n\nMost repo-level comparisons use a single seed; the gap magnitude (19--26\\pp{}) exceeds any single assessed confound (\\S\\ref{sec:threats}), but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. Our \\cwm{} baseline uses ${\\leq}$8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training~\\cite{meta2025cwm}; at larger scale, the generation bottleneck may diminish. However, matched comparison at controlled capacity isolates the formulation effect from scale confounds---complementary to work scaling execution simulators. Training data comprises synthetic mutations~\\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap for absolute accuracy remains untested, though the coupling effect supports relative ranking validity: our core finding---that formulation choice matters at repo level but not function level---concerns relative ordering, expected to be preserved under distributional shifts that affect all formulations equally (Appendix~\\ref{app:limitations}). \\traj{} training uses variant-level labels (386 instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}), which limits direct comparison. A re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\\ref{app:extended_analysis}(j)) found no benefit from per-test diagnostics. The mixed-effects regressions use 25--139 problem-level clusters (cross-model and cross-complexity respectively); fixed-effect estimates pool across $>$56K observations, but the random-effects structure has limited resolution for the 25-cluster model. Model coverage is limited to 6--8B code-specialized LLMs; generalization to larger or general-purpose models is untested. Extended discussion: Appendix~\\ref{app:limitations}. All code, data, and model checkpoints will be released upon acceptance.",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "432fddd4-a423-4de4-9295-60a73593bdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T06:35:32.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SpF5MRYf8Z1JSE7hnBKJuP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac43915-97b1-459e-a317-d69664d2ec84",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "8915a510-029a-4a74-859d-705d3ac74798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 35 · 2026-05-21T06:35:32.882Z_

<details><summary>↩ Tool result · `toolu_01SpF5MRYf8Z1JSE7hnBKJuP`</summary>

```text
1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
37	
38	\paragraph{Sensitivity to ICC estimate.}
39	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
40	
41	\section{Ablation Studies}
42	\label{app:ablations}
43	
44	\paragraph{LoRA rank sensitivity.}
45	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
46	
47	\begin{table}[h]
48	\centering
49	\small
50	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
51	\label{tab:rank_ablation}
52	\setlength{\tabcolsep}{4pt}
53	\begin{tabular}{lccccc}
54	\toprule
55	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
56	\midrule
57	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
58	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
59	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	
64	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
65	
66	\paragraph{Majority voting.}
67	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\footnote{These majority-voting values were computed from an unverified checkpoint and may differ slightly from the val-best checkpoint results.}
68	
69	\paragraph{Sequence-length ablation details.}
70	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
71	
72	\paragraph{Training data size control.}
73	\label{app:downsample}
74	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
75	
76	\paragraph{Few-shot prompting baselines.}
77	\label{app:few_shot}
78	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
79	
80	\begin{table}[h]
81	\centering
82	\small
83	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
84	\label{tab:few_shot}
85	\setlength{\tabcolsep}{4pt}
86	\begin{tabular}{lcccc}
87	\toprule
88	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
89	\midrule
90	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
91	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
92	\bottomrule
93	\end{tabular}
94	
95	\vspace{2pt}
96	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
97	\end{table}
98	
99	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
100	
101	\section{Repo-Level Per-Mutation Breakdown}
102	\label{app:repo_mutation}
103	
104	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy unavailable except gold (computed from parse rate 43.5\%, parseable acc 23.5\%).}
110	\label{tab:mutation_breakdown}
111	\resizebox{\columnwidth}{!}{%
112	\setlength{\tabcolsep}{3pt}
113	\begin{tabular}{lccccccc}
114	\toprule
115	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
116	\midrule
117	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
118	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
119	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
120	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
121	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
122	\bottomrule
123	\end{tabular}}
124	\end{table}
125	
126	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
127	
128	\begin{table}[h]
129	\centering
130	\small
131	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
132	\label{tab:cwm_mutation_parse}
133	\setlength{\tabcolsep}{4pt}
134	\begin{tabular}{lcccc}
135	\toprule
136	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
137	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
138	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
139	\midrule
140	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
141	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
142	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
143	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
144	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
150	
151	\section{Variant-Level Accuracy}
152	\label{app:variant_level}
153	
154	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
160	\label{tab:variant_level}
161	\setlength{\tabcolsep}{3pt}
162	\begin{tabular}{llcccc}
163	\toprule
164	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
165	\midrule
166	\multicolumn{6}{l}{\emph{\cls{}}} \\
167	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
168	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
169	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
170	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
171	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
172	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
173	\midrule
174	\multicolumn{6}{l}{\emph{\cwm{}}} \\
175	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
176	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
177	\midrule
178	\multicolumn{6}{l}{\emph{\traj{}}} \\
179	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
180	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
181	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
182	\midrule
183	Majority & --- & 72.96 & 54.17 & --- & --- \\
184	\bottomrule
185	\end{tabular}
186	\vspace{2pt}
187	
188	{\footnotesize $^\dagger$Preliminary; evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
189	\end{table}
190	
191	\section{Training Hyperparameters}
192	\label{app:hyperparams}
193	
194	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
195	
196	\begin{table}[h]
197	\centering
198	\small
199	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. Effective batch size is $\text{per-device} \times \text{grad.\ accum.} = 32$ in all cases. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
200	\label{tab:hyperparams}
201	\resizebox{\columnwidth}{!}{%
202	\setlength{\tabcolsep}{3pt}
203	\begin{tabular}{lcccccc}
204	\toprule
205	\textbf{Hyperparameter} & \textbf{Qwen3-4B \cls{}} & \textbf{Qwen3-4B \cwm{}} & \textbf{Qwen3-8B \cls{}} & \textbf{Qwen3-8B \cwm{}} & \textbf{DS-6.7B \cls{}} & \textbf{DS-6.7B \cwm{}} \\
206	\midrule
207	Base model & Qwen3-4B & Qwen3-4B & Qwen3-8B & Qwen3-8B & DS-Coder-6.7B & DS-Coder-6.7B \\
208	LoRA rank ($r$) & 16 & 16 & 16 & 16 & 16 & 16 \\
209	LoRA alpha ($\alpha$) & 32 & 32 & 32 & 32 & 32 & 32 \\
210	LoRA dropout & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 \\
211	LoRA targets & \multicolumn{6}{c}{\texttt{q\_proj, k\_proj, v\_proj, o\_proj}} \\
212	Learning rate & 5e-5 & 5e-5 & 5e-5 & 5e-5 & 2e-4 & 2e-4 \\
213	Optimizer & \multicolumn{6}{c}{AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$)} \\
214	Weight decay & 0.01 & 0.01 & 0.01 & 0.01 & 0.0 & 0.0 \\
215	Warmup ratio & 0.05 & 0.05 & 0.05 & 0.05 & 0.1 & 0.1 \\
216	LR scheduler & \multicolumn{6}{c}{Linear} \\
217	Per-device batch size & 2 & 1 & 1 & 1 & 2 & 1 \\
218	Gradient accumulation & 16 & 32 & 32 & 32 & 16 & 32 \\
219	Effective batch size & 32 & 32 & 32 & 32 & 32 & 32 \\
220	Max sequence length & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 \\
221	Epochs & 3 & 3 & 3 & 3 & 3 & 3 \\
222	Precision & bf16 & bf16 & bf16 & bf16 & bf16 & bf16 \\
223	Gradient checkpointing & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
224	Seeds (function) & \multicolumn{6}{c}{\{42, 123, 456, 789, 0\}\textsuperscript{$b$}} \\
225	Seeds (repo) & \multicolumn{6}{c}{\{42, 123, 456\}\textsuperscript{$c$}} \\
226	Training samples & 70,748 & 70,748 & 70,748 & 70,748 & 67,343$^a$ & 70,748 \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{2pt}
231	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
232	\end{table}
233	
234	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
235	
236	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
237	
238	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
239	
240	\paragraph{Compute budget.}
241	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$120 GPU-hours across 226 training runs and evaluations.
242	
243	\section{Val-Test Mutation Type Distribution}
244	\label{app:mutation_distribution}
245	
246	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
247	
248	\begin{table}[h]
249	\centering
250	\small
251	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
252	\label{tab:mutation_distribution}
253	\setlength{\tabcolsep}{3pt}
254	\begin{tabular}{lccccc}
255	\toprule
256	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
257	\midrule
258	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
259	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
260	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
261	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
262	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
268	
269	\section{Qualitative Error Analysis}
270	\label{app:qualitative}
271	
272	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
273	
274	\paragraph{\cwm{} failure modes.}
275	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
276	
277	\paragraph{\cls{} failure modes.}
278	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
279	
280	\paragraph{Complementarity.}
281	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
282	
283	\section{Extended Analysis}
284	\label{app:extended_analysis}
285	
286	\paragraph{(a) Error complementarity.}
287	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
288	
289	\paragraph{(b) CWM error mode breakdown.}
290	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
291	
292	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
293	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The divergence widens from 26\pp{} to 28\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs.
294	
295	\paragraph{(d) Variance compression.}
296	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
297	
298	\paragraph{(e) Per-test precision and recall.}
299	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
300	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
301	
302	\paragraph{(f) Block correlation.}
303	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
304	
305	\paragraph{(g) Failed interventions.}
306	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
307	
308	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
309	\item \textbf{Capacity (rank 32):} Doubling adapter parameters does not improve accuracy ($-$0.51\pp{}, within seed variance; Appendix~\ref{app:ablations}).
310	\item \textbf{Majority voting ($K{=}3$):} Accuracy \emph{decreases} by 0.68\pp{} (87.51\%$\to$86.83\%); 93.3\% of samples are unanimous across passes, and net flips are negative ($-$13), indicating errors are systematic bias rather than stochastic noise.
311	\item \textbf{Relaxed matching (L0--L4):} Tolerating format deviations \emph{decreases} accuracy from 58.04\% to 56.98\% (seed 42; Appendix~\ref{app:extended_analysis}(c)), because unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%).
312	\item \textbf{Model scaling (4B$\to$8B):} Parseable-only accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate increases (53.7\%$\to$73.8\%); the apparent accuracy gain is entirely a default-assignment artifact (\S\ref{sec:repo}).
313	\end{itemize}
314	
315	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
316	
317	\paragraph{(h) Per-mutation scaling patterns.}
318	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
319	
320	\paragraph{(i) Inference efficiency.}
321	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
322	
323	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
324	
325	\paragraph{(j) Re-repair pilot.}
326	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
327	
328	\section{TOST Margin Sensitivity}
329	\label{app:tost_sensitivity}
330	
331	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\traj{} comparison (gap $= -$0.45\pp{}, 523 variants, 114 clusters, clustered bootstrap).
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\caption{TOST margin sensitivity for \cls{}--\traj{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.52\pp{}.}
337	\label{tab:tost_sensitivity}
338	\setlength{\tabcolsep}{4pt}
339	\begin{tabular}{ccc}
340	\toprule
341	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
342	\midrule
343	1.0 & $\gg$0.05 & No \\
344	1.5 & 0.054 & No (borderline) \\
345	\textbf{1.52} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
346	1.71 & 0.027 & Yes \\
347	2.0 & 0.0087 & Yes \\
348	3.0 & $4.6{\times}10^{-5}$ & Yes \\
349	5.0 & $\ll$0.001 & Yes \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	The minimum equivalence margin is $\pm$1.52\pp{}, 0.48\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions.
355	
356	
357	\section{Variant-Level Effect Sizes}
358	\label{app:power}
359	
360	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
361	
362	\begin{table}[h]
363	\centering
364	\small
365	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
366	\label{tab:variant_power}
367	\setlength{\tabcolsep}{3pt}
368	\begin{tabular}{llccc}
369	\toprule
370	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
371	\midrule
372	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
373	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
374	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
375	\midrule
376	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
377	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
378	& Qwen3-8B & +8.33 & wide & 0.385 \\
379	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
380	\bottomrule
381	\end{tabular}
382	\end{table}
383	
384	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
385	
386	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
387	
388	
389	\section{Multiple Comparison Correction}
390	\label{app:holm}
391	
392	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the four primary statistical comparisons across this study ($k{=}4$, family-wise $\alpha{=}0.05$).
393	
394	\begin{table}[h]
395	\centering
396	\small
397	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}4$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
398	\label{tab:holm}
399	\setlength{\tabcolsep}{3pt}
400	\begin{tabular}{clcccc}
401	\toprule
402	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
403	\midrule
404	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$4 & 0.012 & \checkmark \\
405	2 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.0071 & $\times$3 & 0.021 & \checkmark \\
406	3 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
407	4 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	The two core claims survive correction: the repo-level \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level \cls{}--\traj{} equivalence (adjusted $p{=}0.021$). The repo-level \cwm{}--\traj{} comparison does not survive correction (adjusted $p{=}0.078$); we interpret this difference as directionally consistent but not confirmatory.
413	
414	\section{Mixed-Effects Regression}
415	\label{app:interaction}
416	
417	We fit mixed-effects linear probability models (LPM) to test the formulation$\times$complexity interaction formally. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield identical significance conclusions~\cite{angrist2009mostly}.
418	
419	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
420	
421	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$). Formulation explains $>$95\% of the predictable variance; model identity modulates gap magnitude without changing direction. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
422	
423	\section{CWM Parseable Bias Analysis}
424	\label{app:parseable_bias}
425	
426	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
427	
428	
429	\section{Threats to Validity (Full Analysis)}
430	\label{app:threats}
431	
432	We identify five potential confounds and assess their impact on our conclusions.
433	
434	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (all \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%---a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. No \cwm{} overtraining is observed: epoch 2 and 3 final checkpoints achieve comparable running accuracy (${\sim}$65\%, $<$2\pp{} difference) at matched settings.
435	
436	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 19--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$74\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
437	
438	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
439	
440	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap is more consistent with data scarcity (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) than with a formulation-level limitation.
441	
442	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
443	
444	Despite these confounds, the repo-level \cls{}--\cwm{} gap (19--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the four primary comparisons ($k{=}4$) confirms both the \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level equivalence (adjusted $p{=}0.021$) survive; the repo-level \cwm{}--\traj{} comparison is directionally consistent but does not survive correction (adjusted $p{=}0.078$; Table~\ref{tab:holm}). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
445	
446	
447	\section{Extended Limitations}
448	\label{app:limitations}
449	
450	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level TOST equivalence ($p = 0.007$, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases from 0.007 to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison is preliminary due to configuration and granularity differences.
451	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8915a510-029a-4a74-859d-705d3ac74798",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "5073774e-51b6-47ee-b325-94e40cabf9a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Oracle Accuracy-Utility Analysis}\n\\label{app:oracle}\n\nWe stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\\ trajectory-level oracle resolve rates under i.i.d.\\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \\S\\ref{sec:equivalence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \\S\\ref{sec:equivalence}). P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}\n\\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\\%) and concentrates at $T{=}2$ (19.1\\%, contributing 55.3\\% of total advantage).}\n\\label{fig:oracle_stratified}\n\\end{figure}\n\nTable~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\\%), where block-correlated advantage reaches 31.69\\pp{} (55.3\\% of total). The overall block-correlated advantage is 10.93\\pp{}, driven by the $T \\geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\\pp{} vs.\\ 18.49\\pp{} (1.7$\\times$). P2P regression is negligible (1.04\\% mean, 0\\% median); the practical value concentrates in F2P discrimination.\n\n\\paragraph{Sensitivity to ICC estimate.}\nThe analysis above uses ICC $= 0.191$ from function-level analysis (\\S\\ref{sec:equivalence}), where mean cluster size $\\bar{k} \\approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\\S\\ref{sec:repo}), a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA rank ablation for \\cwm{} 4B (seed 42, 3 epochs, lr $= 2{\\times}10^{-4}$). Rank-16 seed variance: 0.53\\pp{} (seeds 42 vs.\\ 456).}\n\\label{tab:rank_ablation}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{$\\alpha/r$} & \\textbf{Acc (\\%)} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{$\\Delta$} \\\\\n\\midrule\n$r{=}16$, $\\alpha{=}32$ & 2 & \\textbf{87.51} & --- & --- & --- \\\\\n$r{=}32$, $\\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\\\\n$r{=}32$, $\\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\\pp{} between seeds 42 and 456). The $\\alpha{=}64$ variant (matching the baseline $\\alpha/r{=}2$ ratio) rules out the confound that the $\\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.\n\n\\paragraph{Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\\footnote{These majority-voting values were computed from an unverified checkpoint and may differ slightly from the val-best checkpoint results.}\n\n\\paragraph{Sequence-length ablation details.}\nBoth formulations are trained with \\texttt{max\\_seq\\_length}$=$2,048. At inference, \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$512, leaving ${\\sim}$1,536 effective input tokens; \\cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\\cls{} 8B at 2,048 tokens) achieves 83.04\\%, only 1.44\\pp{} below the 8,192-token evaluation (84.48\\%), though truncation introduces 136 unparseable outputs (1.39\\% of test samples). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 25.00\\pp{} (98\\% of the full 25.59\\pp{} gap), confirming that input context disparity explains at most 3\\% of the difference.\n\n\\paragraph{Training data size control.}\n\\label{app:downsample}\nTo control for the training set size asymmetry between \\cls{} (${\\sim}$70K instances) and \\traj{} (386 variant-level instances, ${\\sim}$8K per-test equivalents, at repo level), we downsample \\cls{} training data to match \\traj{} in data volume. Downsampled \\cls{} (Qwen3-4B, seed 42) achieves 80.74\\% repo-level per-test accuracy, only 2.89\\pp{} below the full-data \\cls{} (83.63\\%) and still 7.82\\pp{} above \\traj{} (72.92\\%). The \\cls{} formulation advantage is not attributable to training data volume.\n\n\\paragraph{Few-shot prompting baselines.}\n\\label{app:few_shot}\nWe evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\\ref{tab:few_shot} reports both per-test and variant-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\\% per-test, 54.17\\% variant-level.}\n\\label{tab:few_shot}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{0-shot (per-test)} & \\textbf{3-shot (per-test)} & \\textbf{3-shot (variant)} \\\\\n\\midrule\nQwen3-8B & 49.90\\% & 71.61\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\nDeepSeek-6.7B & 48.54\\% & 46.28\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\ast$}Both models achieve 45.83\\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\\%), equivalent to an always-predict-unresolved baseline. The 100\\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}\n\\end{table}\n\nBoth models converge to exactly 45.83\\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\\% vs.\\ DeepSeek 46.28\\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\\% per-test); fine-tuning is a necessary condition for repo-level verification.\n\n\\section{Repo-Level Per-Mutation Breakdown}\n\\label{app:repo_mutation}\n\nTable~\\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \\cls{} produces 0\\% unparseable outputs; all values are direct classification accuracy. \\cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \\S\\ref{sec:repo}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-mutation test accuracy (\\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \\cls{} 8B reports two seeds; $\\Delta$ is mean 4B$\\to$8B gain for \\cls{}. \\cwm{} 4B per-mutation overall accuracy unavailable except gold (computed from parse rate 43.5\\%, parseable acc 23.5\\%).}\n\\label{tab:mutation_breakdown}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mutation} & \\textbf{$n$} & \\textbf{CLS 4B} & \\textbf{CLS 8B s42} & \\textbf{CLS 8B s123} & \\textbf{CWM 4B} & \\textbf{CWM 8B} & \\textbf{$\\Delta$ CLS} \\\\\n\\midrule\ngold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\\\\noperator\\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\\\\noff\\_by\\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \\textbf{+24.58} \\\\\nreturn\\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\\\\nboundary\\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:cwm_mutation_parse} shows that \\cwm{} generation quality degrades from 4B to 8B across all mutation types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\\%) for gold at both scales.}\n\\label{tab:cwm_mutation_parse}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Parse Rate (\\%)}} & \\multicolumn{2}{c}{\\textbf{Parse Acc (\\%)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Mutation} & \\textbf{4B} & \\textbf{8B} & \\textbf{4B} & \\textbf{8B} \\\\\n\\midrule\ngold & 43.5 & 23.9 & 23.5 & 16.5 \\\\\noperator\\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\\\\noff\\_by\\_one & 4.4 & 27.3 & 0.0 & 38.0 \\\\\nreturn\\_value & 48.8 & 26.9 & 27.0 & 56.9 \\\\\nboundary\\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey findings: (1)~Gold parse rate collapses from 43.5\\% to 23.9\\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\\%: the model generates outputs that fail exact-match even for correct code. (3)~\\texttt{off\\_by\\_one} is an anomaly: parse rate \\emph{increases} from 4.4\\% to 27.3\\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.\n\n\\section{Variant-Level Accuracy}\n\\label{app:variant_level}\n\nTable~\\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \\cls{}, the aggregation penalty (per-test $\\to$ variant-level drop) ranges from 1\\pp{} to 19\\pp{} and is largest for models with low fail recall under the all-pass rule. \\cwm{} variant-level accuracy (48--52\\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level per-test vs.\\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \\traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\\% (26/48).}\n\\label{tab:variant_level}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Per-test (\\%)} & \\textbf{Variant (\\%)} & \\textbf{Penalty (\\pp{})} & \\textbf{Fail Recall (\\%)} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cls{}}} \\\\\nQwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\\\\nQwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\\\\nQwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\\\\nDeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\\\\nDeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\\\\nDeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\\sim}$13.72 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cwm{}}} \\\\\nQwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\\\\nDeepSeek-6.7B$^\\dagger$ & s123 & --- & 47.92 & --- & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\traj{}}} \\\\\nQwen3-4B & s42 & --- & 72.92 & --- & --- \\\\\nQwen3-8B & s42 & --- & 70.83 & --- & --- \\\\\nDeepSeek-6.7B & 3-seed & --- & 77.08 $\\pm$ 3.61 & --- & --- \\\\\n\\midrule\nMajority & --- & 72.96 & 54.17 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\n{\\footnotesize $^\\dagger$Preliminary; evaluated on ${\\sim}$75\\% of test instances (7210--7668 of 9784). DeepSeek \\traj{} Table~\\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \\cls{}/\\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\\%, 66.7\\%, 79.2\\% respectively (6-seed mean 75.35 $\\pm$ 5.00\\%), consistent in direction.}\n\\end{table}\n\n\\section{Training Hyperparameters}\n\\label{app:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \\cls{} and \\cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$ for Qwen3, selected via grid search over $\\{5{\\times}10^{-5}, 1{\\times}10^{-4}, 2{\\times}10^{-4}\\}$ on held-out validation loss).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Training hyperparameters for \\cls{}/\\cwm{} configurations. Effective batch size is $\\text{per-device} \\times \\text{grad.\\ accum.} = 32$ in all cases. \\traj{} models use lr $= 2{\\times}10^{-4}$ due to the smaller training set (${\\sim}$8K function-level instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}); other hyperparameters are shared.}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Qwen3-4B \\cls{}} & \\textbf{Qwen3-4B \\cwm{}} & \\textbf{Qwen3-8B \\cls{}} & \\textbf{Qwen3-8B \\cwm{}} & \\textbf{DS-6.7B \\cls{}} & \\textbf{DS-6.7B \\cwm{}} \\\\\n\\midrule\nBase model & Qwen3-4B & Qwen3-4B & Qwen3-8B & Qwen3-8B & DS-Coder-6.7B & DS-Coder-6.7B \\\\\nLoRA rank ($r$) & 16 & 16 & 16 & 16 & 16 & 16 \\\\\nLoRA alpha ($\\alpha$) & 32 & 32 & 32 & 32 & 32 & 32 \\\\\nLoRA dropout & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 \\\\\nLoRA targets & \\multicolumn{6}{c}{\\texttt{q\\_proj, k\\_proj, v\\_proj, o\\_proj}} \\\\\nLearning rate & 5e-5 & 5e-5 & 5e-5 & 5e-5 & 2e-4 & 2e-4 \\\\\nOptimizer & \\multicolumn{6}{c}{AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.999$)} \\\\\nWeight decay & 0.01 & 0.01 & 0.01 & 0.01 & 0.0 & 0.0 \\\\\nWarmup ratio & 0.05 & 0.05 & 0.05 & 0.05 & 0.1 & 0.1 \\\\\nLR scheduler & \\multicolumn{6}{c}{Linear} \\\\\nPer-device batch size & 2 & 1 & 1 & 1 & 2 & 1 \\\\\nGradient accumulation & 16 & 32 & 32 & 32 & 16 & 32 \\\\\nEffective batch size & 32 & 32 & 32 & 32 & 32 & 32 \\\\\nMax sequence length & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 \\\\\nEpochs & 3 & 3 & 3 & 3 & 3 & 3 \\\\\nPrecision & bf16 & bf16 & bf16 & bf16 & bf16 & bf16 \\\\\nGradient checkpointing & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nSeeds (function) & \\multicolumn{6}{c}{\\{42, 123, 456, 789, 0\\}\\textsuperscript{$b$}} \\\\\nSeeds (repo) & \\multicolumn{6}{c}{\\{42, 123, 456\\}\\textsuperscript{$c$}} \\\\\nTraining samples & 70,748 & 70,748 & 70,748 & 70,748 & 67,343$^a$ & 70,748 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n\\end{table}\n\n\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n\n\\paragraph{Prompt templates.} Prompt templates for all formulations (\\cls{}, \\cwm{}, \\traj{}) are provided in the code repository. \\cls{} uses a binary classification template (``Does this test pass or fail?''); \\cwm{} uses an execution simulation template (``What is the output of this test?''); \\traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').\n\n\\paragraph{Mutation operators.} We use five mutation types: (1)~\\emph{gold}: unmodified code (all tests pass); (2)~\\emph{operator\\_swap}: replaces comparison or arithmetic operators (e.g., \\texttt{<} $\\to$ \\texttt{<=}); (3)~\\emph{off\\_by\\_one}: shifts loop bounds or array indices by $\\pm$1; (4)~\\emph{return\\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\\emph{boundary\\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\\sim}$120 GPU-hours across 226 training runs and evaluations.\n\n\\section{Val-Test Mutation Type Distribution}\n\\label{app:mutation_distribution}\n\nTable~\\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \\texttt{operator\\_swap}, which nearly doubles from val (19.1\\%) to test (34.3\\%), while \\texttt{off\\_by\\_one} shrinks from 10.0\\% to 1.9\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level mutation type distribution: validation vs.\\ test set, with per-type \\cls{} accuracy at two model sizes (seed 42). Shift = test\\% $-$ val\\%.}\n\\label{tab:mutation_distribution}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mutation Type} & \\textbf{Val (\\%)} & \\textbf{Test (\\%)} & \\textbf{Shift} & \\textbf{\\cls{} 4B} & \\textbf{\\cls{} 8B} \\\\\n\\midrule\ngold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\\\\noperator\\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\\\\nboundary\\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\\\\nreturn\\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\\\\noff\\_by\\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\texttt{operator\\_swap} shift is the primary source of val-test distribution mismatch. Since \\cls{} achieves moderate accuracy on this type (78.9--81.4\\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\\texttt{boundary\\_removal} represents a scale-invariant difficulty ceiling at ${\\sim}$47\\% across both model sizes: this mutation type resists capacity scaling; (2)~\\texttt{off\\_by\\_one} shows the largest scaling gain (+28.4\\pp{}, 58.5\\%$\\to$86.9\\%) but its small test share (1.9\\%) limits its contribution to overall accuracy differences across scales.\n\n\\section{Qualitative Error Analysis}\n\\label{app:qualitative}\n\nTo complement the quantitative divergence reported in \\S\\ref{sec:repo}, we examine representative errors from each formulation at repository level.\n\n\\paragraph{\\cwm{} failure modes.}\nTwo patterns account for the majority of unparseable \\cwm{} outputs on Qwen3. (1)~\\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \\texttt{django\\_\\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \\texttt{from \\_pytest.config import \\_parse\\_pytest\\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\\S\\ref{sec:repo}).\n\n\\paragraph{\\cls{} failure modes.}\n\\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \\emph{cross-concern value propagation}: a boundary removal mutation in \\texttt{pytest} converts a guarded attribute access (\\texttt{if xfailed and not xfailed.run}) to \\texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \\emph{mathematical equivalence}: on \\texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\\% of all function-level false negatives.\n\n\\paragraph{Complementarity.}\nThese failure patterns operate at different levels: \\cwm{} fails at the format level (producing no usable signal), while \\cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \\cwm{}'s higher FP rate (70.3\\% vs.\\ 56.5\\%) means it over-predicts failure on instances \\cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\\%; \\S\\ref{app:extended_analysis}, paragraph a).\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \\cls{} errors (seed 42), 56.5\\% are false positives (PASS $\\to$ FAIL); among \\cwm{} errors, 70.3\\% are false positives. Both formulations over-predict failure, but \\cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \\cls{} correctly accepts. An oracle combination achieves 90.63\\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\\pp{} over the best single formulation, \\cls{} 87.83\\%; single-seed estimate, seed 42). The complementarity arises from different \\emph{degrees} of fail-bias rather than opposite error directions: \\cwm{}'s generation bottleneck produces aggressive failure predictions, while \\cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAmong unparseable \\cwm{} outputs (Qwen3, repo-level), 76.9\\% contain no execution keywords; 22.9\\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nRelaxed matching (tolerating format deviations, L0--L4) \\emph{decreases} \\cwm{} accuracy: 58.04\\%$\\to$56.98\\% (seed 42) and 59.09\\%$\\to$55.91\\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (42--53\\%). The divergence widens from 26\\pp{} to 28\\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and \\traj{} (0.97\\pp{}) at function level. If \\cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\n\\cls{} achieves fail \\fone{} 87.59\\% (precision 86.20\\%, recall 89.04\\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812\nMulti-F2P instances (6--10 tests) reach 96.3\\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.\n\n\\paragraph{(f) Block correlation.}\nWithin-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\\times$ more all-correct problems than i.i.d.\\ expectation). All statistical tests use clustered bootstrap accordingly.\n\n\\paragraph{(g) Failed interventions.}\nWe systematically tested four interventions targeting different hypothesized causes of \\cwm{} repo-level degradation; all failed:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]\n\\item \\textbf{Capacity (rank 32):} Doubling adapter parameters does not improve accuracy ($-$0.51\\pp{}, within seed variance; Appendix~\\ref{app:ablations}).\n\\item \\textbf{Majority voting ($K{=}3$):} Accuracy \\emph{decreases} by 0.68\\pp{} (87.51\\%$\\to$86.83\\%); 93.3\\% of samples are unanimous across passes, and net flips are negative ($-$13), indicating errors are systematic bias rather than stochastic noise.\n\\item \\textbf{Relaxed matching (L0--L4):} Tolerating format deviations \\emph{decreases} accuracy from 58.04\\% to 56.98\\% (seed 42; Appendix~\\ref{app:extended_analysis}(c)), because unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (38--43\\%).\n\\item \\textbf{Model scaling (4B$\\to$8B):} Parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%) while unparseable rate increases (53.7\\%$\\to$73.8\\%); the apparent accuracy gain is entirely a default-assignment artifact (\\S\\ref{sec:repo}).\n\\end{itemize}\n\n\\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\\leq}$8B generation models can handle, independent of these surface-level factors.\n\n\\paragraph{(h) Per-mutation scaling patterns.}\nScaling benefits are highly non-uniform across mutation types (Table~\\ref{tab:mutation_breakdown}). \\texttt{off\\_by\\_one} shows the largest \\cls{} scaling gain: 58.5\\% (4B) to 86.9\\% (8B, $+$28.4\\pp{}). In contrast, \\texttt{boundary\\_removal} is scale-invariant at ${\\sim}$47\\% across both sizes, which marks an intrinsic difficulty ceiling. For \\cwm{}, gold mutation parse rate collapses from 43.5\\% (4B) to 23.9\\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\\texttt{operator\\_swap} shifts from 19.1\\% to 34.3\\%; Table~\\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \\cls{} performance on \\texttt{operator\\_swap} (78.9--81.4\\%) is close to the overall mean.\n\n\\paragraph{(i) Inference efficiency.}\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} at repo level (853 vs.\\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \\cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\\cls{}) vs.\\ 16.3s (\\cwm{}). At the observed unparseable rate of 73.8\\% (8B), the majority of \\cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \\cls{}--\\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.\n\nThe \\cls{}--\\traj{} efficiency comparison is more nuanced, because \\cls{} makes one call per test while \\traj{} makes one call per instance. Per-call, \\cls{} is 20--138$\\times$ faster (depending on input length: 47ms for short contexts vs.\\ 2,632ms for \\traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \\approx 2.3$), \\cls{} is ${\\sim}$24$\\times$ faster (108ms vs.\\ 2,632ms per instance); at repo level ($|T| \\approx 12.3$, ${\\sim}$70ms/call with longer inputs), \\cls{} is ${\\sim}$3$\\times$ faster (861ms vs.\\ 2,631ms). A crossover exists at $|T| \\approx 50$ tests, beyond which \\traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \\cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.\n\n\\paragraph{(j) Re-repair pilot.}\nWe tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\\%$, $p = 0.42$, effect size $\\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.\n\n\\section{TOST Margin Sensitivity}\n\\label{app:tost_sensitivity}\n\nTable~\\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \\cls{}--\\traj{} comparison (gap $= -$0.45\\pp{}, 523 variants, 114 clusters, clustered bootstrap).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST margin sensitivity for \\cls{}--\\traj{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\\alpha = 0.05$ is $\\pm$1.52\\pp{}.}\n\\label{tab:tost_sensitivity}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Margin ($\\pm$\\pp{})} & \\textbf{$p$-value} & \\textbf{Equivalent ($\\alpha{=}0.05$)?} \\\\\n\\midrule\n1.0 & $\\gg$0.05 & No \\\\\n1.5 & 0.054 & No (borderline) \\\\\n\\textbf{1.52} & ${\\sim}$\\textbf{0.05} & \\textbf{Smallest margin} \\\\\n1.71 & 0.027 & Yes \\\\\n2.0 & 0.0087 & Yes \\\\\n3.0 & $4.6{\\times}10^{-5}$ & Yes \\\\\n5.0 & $\\ll$0.001 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe minimum equivalence margin is $\\pm$1.52\\pp{}, 0.48\\pp{} below our pre-specified $\\pm$2\\pp{} threshold. The $\\pm$2\\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\\%), a 2\\pp{} per-test difference corresponds to ${\\sim}$38 additional errors across 1,890 tests (${\\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\\pp{}) and checkpoint selection noise ($<$1\\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions.\n\n\n\\section{Variant-Level Effect Sizes}\n\\label{app:power}\n\nTable~\\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variant-level bootstrap analysis ($n{=}48$). \\cls{}--\\cwm{} uses paired bootstrap (same variants, same seed); \\cls{}--\\traj{} uses unpaired bootstrap (per-variant \\traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\\sim}$25\\pp{}.}\n\\label{tab:variant_power}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Config} & \\textbf{$\\Delta$ (\\pp{})} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\cwm{} (paired)}} \\\\\n& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\\\\n& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\traj{} (unpaired)}} \\\\\n& Qwen3-4B & $-$4.17 & wide & 0.740 \\\\\n& Qwen3-8B & +8.33 & wide & 0.385 \\\\\n& DeepSeek-6.7B & 0.00 & wide & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n\nThe \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n\n\n\\section{Multiple Comparison Correction}\n\\label{app:holm}\n\nTable~\\ref{tab:holm} applies Holm-Bonferroni correction~\\cite{holm1979} to the four primary statistical comparisons across this study ($k{=}4$, family-wise $\\alpha{=}0.05$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni correction for primary comparisons ($k{=}4$). Comparisons ranked by raw $p$-value; each tested against $\\alpha / (k - \\text{rank} + 1)$.}\n\\label{tab:holm}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{clcccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Comparison} & \\textbf{Raw $p$} & \\textbf{Factor} & \\textbf{Adj $p$} & \\textbf{Sig.?} \\\\\n\\midrule\n1 & Repo: \\cls{} vs \\cwm{} & 0.003 & $\\times$4 & 0.012 & \\checkmark \\\\\n2 & Func: \\cls{} vs \\traj{} (TOST $\\pm$2\\pp{}) & 0.0071 & $\\times$3 & 0.021 & \\checkmark \\\\\n3 & Repo: \\cwm{} vs \\traj{} & 0.039 & $\\times$2 & 0.078 & --- \\\\\n4 & Repo: \\cls{} vs \\traj{} & 0.385 & $\\times$1 & 0.385 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe two core claims survive correction: the repo-level \\cls{}--\\cwm{} gap (adjusted $p{=}0.012$) and function-level \\cls{}--\\traj{} equivalence (adjusted $p{=}0.021$). The repo-level \\cwm{}--\\traj{} comparison does not survive correction (adjusted $p{=}0.078$); we interpret this difference as directionally consistent but not confirmatory.\n\n\\section{Mixed-Effects Regression}\n\\label{app:interaction}\n\nWe fit mixed-effects linear probability models (LPM) to test the formulation$\\times$complexity interaction formally. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield identical significance conclusions~\\cite{angrist2009mostly}.\n\n\\paragraph{Cross-complexity model (DeepSeek-Coder).} \\texttt{correct $\\sim$ formulation $\\times$ complexity + (1|problem\\_id)}, $n{=}56{,}480$ observations (\\cls{} + \\cwm{} $\\times$ function + repo), 139 problem clusters. The \\cwm{} main effect at function level is non-significant ($\\hat{\\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \\cwm{}$\\times$repo interaction is highly significant ($\\hat{\\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}, $p{=}0.805$) but diverge by 22\\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.\n\n\\paragraph{Repo-level cross-model model.} \\texttt{correct $\\sim$ formulation $\\times$ model + (1|problem\\_id)}, both model families, repo level only. \\cwm{} deficit: $\\hat{\\beta}{=}-0.22$ ($-$22\\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$). Formulation$\\times$model interaction: +1.6\\pp{} less \\cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$). Formulation explains $>$95\\% of the predictable variance; model identity modulates gap magnitude without changing direction. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.\n\n\\section{CWM Parseable Bias Analysis}\n\\label{app:parseable_bias}\n\nThe default-to-pass assignment for unparseable \\cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\\% vs.\\ 68.3\\%, $\\chi^2$ $p = 5.9 \\times 10^{-10}$), and \\cls{} models achieve higher accuracy on unparseable instances (86.4\\% vs.\\ 79.1\\%, $p = 3.3 \\times 10^{-18}$). This indicates that \\cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \\cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.\n\n\n\\section{Threats to Validity (Full Analysis)}\n\\label{app:threats}\n\nWe identify five potential confounds and assess their impact on our conclusions.\n\n\\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (all \\cwm{} repo-level runs, DeepSeek \\cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \\cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\\%, val-selected (ckpt-3600) 84.48\\%, and final epoch (ckpt-6633) 85.29\\%---a $<$1\\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \\traj{} comparison (epoch 2: 72.92\\% vs.\\ epoch 3: 70.83\\%) shows a slightly larger ${\\sim}$2\\pp{} shift. No \\cwm{} overtraining is observed: epoch 2 and 3 final checkpoints achieve comparable running accuracy (${\\sim}$65\\%, $<$2\\pp{} difference) at matched settings.\n\n\\paragraph{Evaluation sequence length.} \\cwm{} accuracy varies by ${\\sim}$9\\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\\sim}$65\\% vs.\\ seq4096: ${\\sim}$56\\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \\cls{} is invariant to this parameter. Cross-model \\cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\\sim}$1.5\\pp{} difference for \\cls{} (Appendix~\\ref{app:ablations}), insufficient to explain the 19--26\\pp{} gap. Furthermore, increasing Qwen3-8B \\cwm{} evaluation from seq4096 to seq8192 \\emph{raises} the unparseable rate (63.7\\%$\\to$74\\%) while changing accuracy by only 0.81\\pp{} (64.36\\%$\\to$65.17\\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.\n\n\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n\n\\paragraph{\\traj{} training regime.} \\traj{} uses a different training configuration: smaller training set (${\\sim}$400 repo-level variants vs.\\ ${\\sim}$70K per-test instances), higher learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \\cls{} formulation advantage persists at matched data volume (80.74\\% vs.\\ 72.92\\%; Appendix~\\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\\ variant-level). Crucially, \\traj{} achieves statistical equivalence with \\cls{} at function level (${\\leq}$1.3\\pp{}, \\S\\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap is more consistent with data scarcity (${\\sim}$400 variants vs.\\ ${\\sim}$70K per-test instances) than with a formulation-level limitation.\n\n\\paragraph{\\cwm{} scale and pretraining.} Our \\cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \\cwm{} conclusions are conditional on the ${\\leq}$8B LoRA regime.\n\nDespite these confounds, the repo-level \\cls{}--\\cwm{} gap (19--26\\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\\sim}$11.5\\pp{}), the gap retains ${\\geq}$7.5\\pp{} margin; confounds predominantly disadvantage \\cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\\sim}$25\\pp{}~\\cite{hoenig2001}; the \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, while the \\cls{}--\\traj{} gap ($<$10\\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the four primary comparisons ($k{=}4$) confirms both the \\cls{}--\\cwm{} gap (adjusted $p{=}0.012$) and function-level equivalence (adjusted $p{=}0.021$) survive; the repo-level \\cwm{}--\\traj{} comparison is directionally consistent but does not survive correction (adjusted $p{=}0.078$; Table~\\ref{tab:holm}). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\nThe same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \\cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\\ref{tab:mutation_distribution}): \\texttt{operator\\_swap} shifts from 19.1\\% (val) to 34.3\\% (test), the largest single-type distribution mismatch (+15.2\\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \\emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \\emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \\traj{} training configuration differs from \\cls{}/\\cwm{}: smaller training set (${\\sim}$400 vs.\\ ${\\sim}$70K instances), different learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\\ per-test $n{=}9{,}784$). The function-level TOST equivalence ($p = 0.007$, $\\pm$2\\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases from 0.007 to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \\cls{}--\\traj{} comparison is preliminary due to configuration and granularity differences.\n",
      "numLines": 451,
      "startLine": 1,
      "totalLines": 451
    }
  },
  "sourceToolAssistantUUID": "8915a510-029a-4a74-859d-705d3ac74798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T06:35:33.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BwEJUvpkpx5Ciyi597uydY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5073774e-51b6-47ee-b325-94e40cabf9a0",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "b8d425bd-fcca-4e76-913d-c4353bed9ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 37 · 2026-05-21T06:35:33.029Z_

<details><summary>↩ Tool result · `toolu_01BwEJUvpkpx5Ciyi597uydY`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	\newcommand{\tbd}{\textsc{tbd}}
29	
30	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\input{abstract}
37	
38	\input{introduction}
39	
40	\begin{figure*}[t]
41	\centering
42	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
43	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
44	\label{fig:reformulation}
45	\end{figure*}
46	
47	\input{method}
48	
49	\input{experiments}
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
54	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 19--26\pp{} with \cwm{} falling below majority baseline.}
55	\label{fig:scaling_gap}
56	\end{figure}
57	
58	
59	\input{related_work}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\input{checklist}
66	
67	\input{appendix}
68	
69	\end{document}
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8d425bd-fcca-4e76-913d-c4353bed9ba4",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "1b69a051-2acf-43df-9ead-c235686f16f2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n% ACL style (review mode for anonymous ARR submission)\n\\usepackage[review]{acl}\n\n% Math\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n% Tables\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n% Graphics\n\\usepackage{graphicx}\n\\graphicspath{{../../artifacts/}}\n\n% Lists\n\\usepackage{enumitem}\n\n% Custom commands\n\\newcommand{\\cls}{\\textsc{Cls}}\n\\newcommand{\\cwm}{\\textsc{Cwm}}\n\\newcommand{\\traj}{\\textsc{Traj}}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\tbd}{\\textsc{tbd}}\n\n\\title{The Formulation Design Space for Execution-Free Code Verification:\\\\A Systematic Empirical Study}\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig1_reformulation.pdf}\n\\caption{Three verification formulations. \\textbf{Left:} \\cls{} predicts binary pass/fail per test (1 output token). \\textbf{Center:} \\cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \\textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}\n\\label{fig:reformulation}\n\\end{figure*}\n\n\\input{method}\n\n\\input{experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_scaling_gap.pdf}\n\\caption{Gap amplification from function to repo level. At function level, the \\cls{}--\\cwm{} gap is 1--3\\pp{}; at repo level, it widens to 19--26\\pp{} with \\cwm{} falling below majority baseline.}\n\\label{fig:scaling_gap}\n\\end{figure}\n\n\n\\input{related_work}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{checklist}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  },
  "sourceToolAssistantUUID": "b8d425bd-fcca-4e76-913d-c4353bed9ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T06:35:33.770Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HtFcCMgs3z4BbK9VHtgwk4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b69a051-2acf-43df-9ead-c235686f16f2",
  "isSidechain": false,
  "requestId": "req_011CbFFTC6e2zCbuMbv8Znm7",
  "type": "assistant",
  "uuid": "8415e36e-0483-4c59-bc80-6f663000a0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159nSH3nJ2JwqdExkixEBQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 38438,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 38438,
          "cache_creation_input_tokens": 11973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11973
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

_source line 39 · 2026-05-21T06:35:33.964Z_

```json
{
  "parentUuid": "50c99351-d731-4aa6-9c95-1cf106e0c36f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2a5cc163-4b47-425c-bcec-254c48f10035",
  "timestamp": "2026-05-21T06:35:33.964Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 19 war…",
  "leafUuid": "2a5cc163-4b47-425c-bcec-254c48f10035",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Assistant

_source line 42 · 2026-05-21T06:35:37.899Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files. Let me perform the systematic content structure audit across all dimensions.

Let me also search for specific patterns (em-dash, AI style markers, etc.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a5cc163-4b47-425c-bcec-254c48f10035",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "b62e205f-6631-4442-8302-5b65d350856a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 43 · 2026-05-21T06:35:38.627Z_

所有源文件已读取。现在执行去 AI 风格扫描和符号一致性检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b62e205f-6631-4442-8302-5b65d350856a",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "31a736fb-7b7a-4e12-8be4-4b13b23de3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 44 · 2026-05-21T06:35:40.548Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011ZtZaLR9U2Fzj6tSdjiWnD`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a736fb-7b7a-4e12-8be4-4b13b23de3c0",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "afafd0dc-83d1-4be3-8a93-c5627861cc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 45 · 2026-05-21T06:35:47.881Z_

<details><summary>↩ Tool result · `toolu_01Ep9oQ1ch7AwMKG7ecoPqP4`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e342031a-9534-4536-a85f-5b120b7a83a7",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "6f903794-bedf-41c3-b666-6caed6fb4374",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "e342031a-9534-4536-a85f-5b120b7a83a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T06:35:40.580Z_

<details><summary>↩ Tool result · `toolu_011ZtZaLR9U2Fzj6tSdjiWnD`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afafd0dc-83d1-4be3-8a93-c5627861cc13",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "d674b725-12e0-483a-a299-ccf078f7e61c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "afafd0dc-83d1-4be3-8a93-c5627861cc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T06:35:41.631Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Jpvjbue45whSAJYhyeRwSV`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d674b725-12e0-483a-a299-ccf078f7e61c",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "8774bca8-783e-4151-8813-7199a1085e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 48 · 2026-05-21T06:35:41.674Z_

<details><summary>↩ Tool result · `toolu_01Jpvjbue45whSAJYhyeRwSV`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8774bca8-783e-4151-8813-7199a1085e24",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "46f74e16-6867-488e-8943-db45ef16261d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "8774bca8-783e-4151-8813-7199a1085e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T06:35:43.398Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CPyvcAgNTYqT3ZwrQKTo4f`</summary>

```json
{
  "pattern": ", (highlighting|demonstrating|establishing|enabling|suggesting|indicating|revealing|confirming|showing|making|providing|ensuring|leveraging|utilizing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46f74e16-6867-488e-8943-db45ef16261d",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "450d14e9-c65f-45f3-b94a-2599012ceb0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 50 · 2026-05-21T06:35:43.468Z_

<details><summary>↩ Tool result · `toolu_01CPyvcAgNTYqT3ZwrQKTo4f`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:98:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:137:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:163:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:182:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex:22:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:70:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:149:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:310:\item \textbf{Majority voting ($K{=}3$):} Accuracy \emph{decreases} by 0.68\pp{} (87.51\%$\to$86.83\%); 93.3\% of samples are unanimous across passes, and net flips are negative ($-$13), indicating errors are systematic bias rather than stochastic noise.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:384:At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:419:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:426:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:434:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:436:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:440:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "450d14e9-c65f-45f3-b94a-2599012ceb0f",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "5d930fce-d985-4a34-a2c7-d09243e8d5d9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:98:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:137:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:163:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:182:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex:22:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:4:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:70:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:149:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:310:\\item \\textbf{Majority voting ($K{=}3$):} Accuracy \\emph{decreases} by 0.68\\pp{} (87.51\\%$\\to$86.83\\%); 93.3\\% of samples are unanimous across passes, and net flips are negative ($-$13), indicating errors are systematic bias rather than stochastic noise.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:384:At $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:419:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:426:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:434:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:436:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:440:[Omitted long matching line]",
    "numLines": 16
  },
  "sourceToolAssistantUUID": "450d14e9-c65f-45f3-b94a-2599012ceb0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T06:35:45.722Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015dihpPcZRqRGbmEQ2Dakxe`</summary>

```json
{
  "pattern": "(It is worth noting|Notably|Importantly|Furthermore|Moreover|Additionally|delve|leverage|utilize|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d930fce-d985-4a34-a2c7-d09243e8d5d9",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "d1d72540-72db-402a-8a27-47337c934515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 52 · 2026-05-21T06:35:45.750Z_

<details><summary>↩ Tool result · `toolu_015dihpPcZRqRGbmEQ2Dakxe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:98:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:318:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:436:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1d72540-72db-402a-8a27-47337c934515",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "de3bbdc6-5549-4241-b76c-9c0dfbcf2a9e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:98:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:318:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:436:[Omitted long matching line]",
    "numLines": 5
  },
  "sourceToolAssistantUUID": "d1d72540-72db-402a-8a27-47337c934515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T06:35:46.667Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WMBhPgzfM9cJ6iZsLtdYw8`</summary>

```json
{
  "pattern": "\\\\tbd",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de3bbdc6-5549-4241-b76c-9c0dfbcf2a9e",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "47f6b435-f5d2-43f8-9374-f2b47fa9f991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 54 · 2026-05-21T06:35:46.686Z_

<details><summary>↩ Tool result · `toolu_01WMBhPgzfM9cJ6iZsLtdYw8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:120:Qwen3-8B & \textbf{84.83 $\pm$ 0.66} & 72.92 / 81.25\textsuperscript{$\dagger$} & \tbd{} & 72.91 $\pm$ 3.61 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:121:DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & \tbd{} & 77.08 $\pm$ 3.61 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex:28:\newcommand{\tbd}{\textsc{tbd}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47f6b435-f5d2-43f8-9374-f2b47fa9f991",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "f4f3ab17-76d6-40f0-94fd-2cf2625f604f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:120:Qwen3-8B & \\textbf{84.83 $\\pm$ 0.66} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & \\tbd{} & 72.91 $\\pm$ 3.61 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:121:DeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & \\tbd{} & 77.08 $\\pm$ 3.61 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex:28:\\newcommand{\\tbd}{\\textsc{tbd}}",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "47f6b435-f5d2-43f8-9374-f2b47fa9f991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T06:35:47.870Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ep9oQ1ch7AwMKG7ecoPqP4`</summary>

```json
{
  "pattern": "(TODO|TBD|PLACEHOLDER|XX\\.XX|\\[If )",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f3ab17-76d6-40f0-94fd-2cf2625f604f",
  "isSidechain": false,
  "requestId": "req_011CbFFTt8BV7T4dj3nukqqE",
  "type": "assistant",
  "uuid": "e342031a-9534-4536-a85f-5b120b7a83a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Baf3AjLmivbi5a7PkMxeK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33326,
      "cache_read_input_tokens": 50411,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 50411,
          "cache_creation_input_tokens": 33326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33326
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

_source line 56 · 2026-05-21T06:35:52.355Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now also check for specific things: word count of limitations, check for "significantly" usage, and search for how many words are in the Limitations section.

Let me also check for "state-of-the-art" claims and "significantly outperforms" patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f903794-bedf-41c3-b666-6caed6fb4374",
  "isSidechain": false,
  "requestId": "req_011CbFFUumgFgABkvuiBt4Bj",
  "type": "assistant",
  "uuid": "9a818f04-0e48-40b5-b42e-4c2c33c57851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YC6yhMm4p31GmNw3sAhTu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2626,
      "cache_read_input_tokens": 83737,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 83737,
          "cache_creation_input_tokens": 2626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2626
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

_source line 57 · 2026-05-21T06:35:53.817Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015Kq5D8ML2w3odARmYG3Xoe`</summary>

```json
{
  "pattern": "(state.of.the.art|significantly outperform|significantly better|significantly improve)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a818f04-0e48-40b5-b42e-4c2c33c57851",
  "isSidechain": false,
  "requestId": "req_011CbFFUumgFgABkvuiBt4Bj",
  "type": "assistant",
  "uuid": "cee032dc-3de5-4d61-a4b5-04080825a324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YC6yhMm4p31GmNw3sAhTu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2626,
      "cache_read_input_tokens": 83737,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 83737,
          "cache_creation_input_tokens": 2626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2626
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

_source line 58 · 2026-05-21T06:35:53.847Z_

<details><summary>↩ Tool result · `toolu_015Kq5D8ML2w3odARmYG3Xoe`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cee032dc-3de5-4d61-a4b5-04080825a324",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "101147e0-6ffe-4526-a111-f1f1c9844318",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "cee032dc-3de5-4d61-a4b5-04080825a324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T06:35:55.236Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017gY8m1HKT4PzJHZjEKGCpW`</summary>

```json
{
  "pattern": ", revealing ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "101147e0-6ffe-4526-a111-f1f1c9844318",
  "isSidechain": false,
  "requestId": "req_011CbFFUumgFgABkvuiBt4Bj",
  "type": "assistant",
  "uuid": "acba66c1-8a1d-46d1-bbf8-b361c1fa6814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YC6yhMm4p31GmNw3sAhTu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2626,
      "cache_read_input_tokens": 83737,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 83737,
          "cache_creation_input_tokens": 2626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2626
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

_source line 60 · 2026-05-21T06:35:55.253Z_

<details><summary>↩ Tool result · `toolu_017gY8m1HKT4PzJHZjEKGCpW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:13:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acba66c1-8a1d-46d1-bbf8-b361c1fa6814",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "5ca2c2c3-87f4-4404-8cfa-306755f91fc2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:4:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:13:[Omitted long matching line]",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "acba66c1-8a1d-46d1-bbf8-b361c1fa6814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T06:35:56.326Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rx4kdyBgozYwzpNoFhdATr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && sed -n '/\\\\section\\*{Limitations}/,/\\\\section/p' conclusion.tex | wc -w",
  "description": "Count words in Limitations section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ca2c2c3-87f4-4404-8cfa-306755f91fc2",
  "isSidechain": false,
  "requestId": "req_011CbFFUumgFgABkvuiBt4Bj",
  "type": "assistant",
  "uuid": "31c5d3b2-eb9e-424a-9f49-ba7fac91269e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YC6yhMm4p31GmNw3sAhTu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2626,
      "cache_read_input_tokens": 83737,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 83737,
          "cache_creation_input_tokens": 2626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2626
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 19 war…",
  "leafUuid": "31c5d3b2-eb9e-424a-9f49-ba7fac91269e",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Tool result

_source line 64 · 2026-05-21T06:35:56.780Z_

<details><summary>↩ Tool result · `toolu_01Rx4kdyBgozYwzpNoFhdATr`</summary>

```text
208
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31c5d3b2-eb9e-424a-9f49-ba7fac91269e",
  "isSidechain": false,
  "promptId": "60fdae86-97ee-4c63-88c7-efdc06e33663",
  "type": "user",
  "uuid": "f28d296a-ec0c-4328-b420-729f1387159e",
  "toolUseResult": {
    "stdout": "208",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "31c5d3b2-eb9e-424a-9f49-ba7fac91269e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-21T06:35:56.793Z_

```json
{
  "parentUuid": "f28d296a-ec0c-4328-b420-729f1387159e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "07fc397e-3741-4669-98da-df21e282934e",
  "timestamp": "2026-05-21T06:35:56.793Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 66 · 2026-05-21T06:37:34.681Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the comprehensive audit. I've read all the files and performed the necessary scans. Let me analyze all the dimensions systematically.

## 1. 叙事一致性 (CRITICAL)

### Abstract 的"问题" == Intro 的"问题"？

**Abstract** says: "LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged... No prior work compares these formulations under matched conditions."


**Intro** says: "LLM-based automated program repair systems increasingly rely on test-time compute scaling... driving demand for execution-free alternatives. Three distinct formulations have emerged... Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant."

✅ These are aligned.

### Intro 的"贡献列表" == Method 实际做了什么？

The intro lists three main contributions: showing that certain formulations are nearly equivalent at low complexity with model-dependent behavior, demonstrating how the gap between function-level and repository-level performance widens significantly as complexity increases, and a third contribution that appears to be cut off. Let me check if the methods section actually delivers on these claims.

The methods section covers the three formulations, their failure modes, and an oracle accuracy-utility framework to evaluate them. The experiments validate all three contributions. ✅ Aligned.

### Method 的"为什么这样设计" == Intro 的"gap"？

The intro identifies the gap as the lack of systematic comparison while holding model capacity, training data, and compute constant. The method is explicitly designed as a matched comparison framework to address this. ✅ Aligned.

### Experiments 验证的 == Intro 声称的贡献？

Looking at how the experiments map to the claimed contributions: the near-equivalence claim is verified through function-level results and equivalence testing, the complexity divergence is confirmed through repository-level analysis, and I need to verify the third contribution is actually tested.

### Conclusion 总结的 == Experiments 的结论？

The conclusion statements all trace back to specific experimental results—the statistical equivalence at function level, TRAJ's performance gap on different models, the throughput gains from per-test classification, the oracle's complementary error rates, and the robust interaction effect at repository level. The recommendation for CLS based on throughput also follows from the data. The narrative holds together well, though I should check if there are any gaps between what's claimed and what's actually demonstrated.

Looking at the framing more carefully, there's a tension I need to resolve. The abstract and introduction build up this three-layer structure—fine-tuning necessity, formulation choice driven by complexity, then error complementarity—but the experiments don't always make this structure explicit. More importantly, the abstract frames the equivalence between CLS and CWM as "non-obvious" given the token count difference, and the introduction emphasizes this same point. But the method section actually explains why this equivalence should be expected when outputs are short and structured, which somewhat undermines the "non-obvious" framing. I need to check if this is a genuine inconsistency or if the claim is still defensible given the empirical results.

There's also a critical blocker: Table 4 has placeholder entries for CWM at 8B Qwen3 and DeepSeek. This needs to be resolved before submission.

On the structural side, the abstract and introduction are both solid in their coverage—problem, method, results, and significance are all there. The abstract is data-heavy but within word limits. The introduction builds background and problem importance, though I should verify the existing work section flows properly.

The related work section uses thematic grouping effectively and avoids just listing papers. Now checking how well the contributions map to the actual results sections—the first two contributions about equivalence at low complexity and complexity-dependent divergence are well-supported by the tables and analysis. The third contribution on error complementarity needs verification.

I notice section 5.3 on scaling behavior is substantial content about how performance changes from 4B to 8B models, but it's not explicitly called out as its own contribution even though it's a meaningful finding about CWM's limitations. The title accurately reflects the systematic empirical approach and the three-formulation comparison without overstating the scope, and the abstract correctly identifies Qwen3 and DeepSeek-Coder as the two representative families used in the experiments.

Now checking the claim strength: the statistical equivalence claim is properly supported by TOST with multiple comparison correction, the interaction effect has strong regression backing, the performance gaps are appropriately flagged as single-seed estimates, and the throughput advantage is grounded in efficiency analysis. The oracle ensemble result is similarly qualified. I don't see overconfident language like "significantly outperforms" or "state-of-the-art," and the paper appropriately acknowledges the limitations from single-seed design and potential confounds.

Moving to experimental rigor: the main results table reports means and standard deviations across multiple seeds (5 for Qwen3, 2 for DeepSeek), single-seed comparisons are clearly marked, and the baselines are comprehensive—including zero-shot, LLM-as-judge, few-shot ICL, and majority voting from recent papers. The method has three core components with ablations covering...

Generating markdown table...

I notice there's a discrepancy in the reported compute budgets — the appendix claims around 120 GPU-hours across 226 runs, while the checklist lists approximately 150 GPU-hours for about 40 configurations. These numbers don't align and need clarification. Moving on to check notation consistency, I see the custom commands are being used uniformly throughout the paper.

Now I'm verifying that all key terminology is properly defined at first mention — ICC, TOST, DEFF, F2P/P2P, and SESOI all check out. Holm-Bonferroni appears in section 5.1 as a correction method without extensive definition, but that should be acceptable for the target audience.

The section flow from Methods through the experimental sequence feels logical, progressing naturally from functional analysis through scaling, equivalence testing, reproducibility, and finally to threat assessment.

Looking at the transitions between subsections, they're fairly abrupt — each section stands alone without explicit connective sentences bridging them. The Discussion is woven into the Analysis section rather than separated out, which works since it interprets findings rather than just restating numbers.

For the Limitations section, I'm checking that it meets the threshold of over 150 words and covers distinct constraints: the single-seed nature of repository-level comparisons, the CWM baseline being limited to 8B LoRA rather than the full 32B model, and the reliance on synthetic mutations. The section comes in at around 208 words, so that's solid.

Now I'm scanning for AI-style markers — em-dashes and en-dashes both show zero hits, which is good. For the -ing participle phrases, I'm finding several scattered through the abstract, introduction, and experiments sections like "establishing that classification is not inherently easier," "revealing model-dependent sensitivity," and "providing diagnostic information." These are present but not overwhelming.

I'm also checking for filler words and found "Notably" in the experiments section, though the usual suspects like "Furthermore," "leverage," and "utilize" aren't appearing in the main text. The paragraph structure is generally solid, though the introduction's third paragraph runs quite long as one massive block.

There's a critical issue though — Table 4 has two \tbd{} placeholder entries that need to be filled in.

I'm also noticing some inconsistencies in the reported numbers. The appendix mentions around 120 GPU-hours across 226 training runs, but the checklist says approximately 150 GPU hours across 40 configurations. These don't align. And the introduction's third paragraph is trying to pack too much in — it's essentially duplicating what the abstract and contributions should cover, making the whole section feel redundant and dense rather than flowing naturally into the paper.

The abstract itself is also number-heavy with specific statistics like TOST p-values, confidence intervals, seed counts, and effect sizes. That's a lot of quantitative detail for an abstract when typically you'd want just 2-3 key numbers. Then there's the issue that Table 4 explicitly says the CWM multi-seed runs are still in progress, which combined with the \tbd{} placeholders suggests the experiments aren't actually complete yet.

One more thing — the Related Work section comes after Experiments, which is fine structurally, but it's compressed into just a single page with three paragraphs. For a paper claiming to be a systematic empirical study, that feels thin for covering the landscape of related work.

The failure mode taxonomy sits in the Method section where it reads more like motivation or hypothesis than actual methodology. The first contribution in the intro is also packed too densely — it's trying to cover CLS-CWM equivalence, model-dependency findings, per-test granularity, and a negative result all in one bullet point. And Table 4's footnotes are problematic: there are four different footnote markers with a dense block of qualifications that really should be clearer for readers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07fc397e-3741-4669-98da-df21e282934e",
  "isSidechain": false,
  "requestId": "req_011CbFFVZmSLdx8LT2oBYrBV",
  "type": "assistant",
  "uuid": "7b74a9e1-6d92-4b4d-b487-8c78e93d5e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bc53qqDd4U4by3pY55Du1s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 86363,
      "output_tokens": 6483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6483,
          "cache_read_input_tokens": 86363,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
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

_source line 67 · 2026-05-21T06:38:23.301Z_

审计完成。以下是结构化 findings：

```
[CONTENT_AUDIT_START]

=== 叙事一致性 (CRITICAL 级) ===

- [critical] [叙事一致性] Table 4 (repo_level) 包含两处 \tbd{} 占位符（experiments.tex:120-121，Qwen3-8B CWM 和 DeepSeek-6.7B CWM），且 caption 明确写"CWM multi-seed runs in progress"。论文正在用未完成的实验数据投稿，审稿人会认为工作不完整。这是 desk reject 级别问题。

- [warning] [叙事一致性] Intro 第3段与 Abstract 高度重复：同一组数字（TOST p=0.007, z=-23.7, 19-26pp, 90.63%/95.83%）在 Abstract、Intro 第3段、Contribution 列表中出现三次。Intro 第3段应该讲故事（洞察→方法→发现的逻辑链），而非重新罗列 Abstract 中已给出的定量结论。

- [warning] [叙事一致性] Method §3.2 的 "Complexity dependence" 段预测"when execution outputs are short and structured, all formulations should perform comparably"，但 Intro 和 Abstract 将 function-level 等价性包装为"non-obvious result"。Method 自己给出了理论预期，Intro 却说出乎意料——叙事矛盾。建议：要么 Intro 改为"consistent with theoretical analysis"，要么 Method 弱化预测语气。

- [info] [叙事一致性] §5.3 Scaling Behavior 是实质性子发现（CWM 不随 scale 提升），但三条 contribution 列表中没有对应条目。这些内容服务于 contribution 2（complexity divergence），但读者可能困惑这段与贡献的对应关系。

=== 章节结构 ===

- [warning] [章节结构] Abstract 数字密度过高：TOST p=0.007, ±2pp, 5 seeds, Holm-Bonferroni, ≤1.3pp, 2.69pp, z=-23.7, n=56,480, 19-26pp, 90.63%。Paper-writing-norms 要求 Abstract 最多 2-3 个关键数字。当前读起来像 Results 的压缩版而非独立的故事单元。

- [warning] [章节结构] Intro Contribution 1 过载：单条 bullet 包含 CLS-CWM 等价性、TRAJ 模型依赖性、per-test granularity 价值、re-repair pilot 负面结果（n=44, p=0.42）四个独立发现。建议将 re-repair 负面结果移出 contribution 列表，降级到 Analysis 段。

- [info] [章节结构] Related Work 压缩为 3 段约 250 words，对于"systematic empirical study"偏薄。三种 formulation 各自的文献脉络可以更充分展开，帮助审稿人理解 positioning。

=== 贡献-范围对齐 ===

- [info] [贡献-范围] Title 用"Formulation Design Space"暗示设计空间的系统性探索，但实际只比较了三种已有 formulation 的表现。Title 与方法论贡献（matched comparison framework）对齐良好，但可能让期待新 formulation 设计的读者失望。这是 framing 选择，不是错误。

=== Claim 强度匹配 ===

- [info] [Claim强度] "oracle ensemble: 90.63%" (abstract.tex:6, introduction.tex:17) 和 "95.83%" 均为 single-seed estimates，但 Abstract 和 Intro 未标注 single-seed 限定。Experiments §5.7 中有标注（"single-seed estimate"），但 Abstract/Intro 的读者不会看到这个限定。

- [info] [Claim强度] "217× higher throughput"（experiments.tex:175, conclusion.tex:4）是 formulation-inherent 的推导（1 token vs O(L) tokens），但实际测量值来自特定硬件和输入长度。Conclusion 中作为推荐依据使用时未加条件限定。

=== 实验严谨性 ===

- [warning] [实验严谨] repo-level 核心对比（19-26pp gap）仅基于 single-seed variant-level evaluation（n=48）。虽然 per-test interaction 有 56K observations 支撑（z=-23.7），但 variant-level gap magnitude（审稿人最关心的数字）的置信度有限。论文在 Threats §5.8 和 Limitations 中承认了这点，但 Abstract/Intro 中 "19-26pp" 以确定性语气出现，未附 single-seed 标注。

- [warning] [实验严谨] DeepSeek-Coder 仅 2 seeds（function-level）。Table 1 为其报告 std，但 n=2 的 std 几乎无统计意义。Caption 有标注"not inferential"✓，但视觉上与 5-seed Qwen3 结果并列，读者可能高估其可靠性。

=== 可复现性披露 ===

- [warning] [可复现性] 计算预算不一致：Appendix §E (appendix.tex:241) 写"~120 GPU-hours across 226 training runs"，Checklist C1 (checklist.tex:39) 写"approximately 150 GPU hours across all training runs (~40 configurations)"。数字和运行次数均矛盾（226 vs ~40, 120 vs 150）。

- [info] [可复现性] 数据构建过程（mutation operators）仅在 Appendix §E 简要描述。主文 §5.1 提到"mutated variants from HumanEval and MBPP (five mutation types)"但未解释 mutation 细节。对于可复现性，mutation 操作定义应更突出。

=== 符号/术语一致性 ===

- [info] [术语] "LPM" (Linear Probability Model) 在 Appendix §H (appendix.tex:417) 首次使用时有定义✓。"SESOI" 在 §5.4 首次使用时有定义✓。"DEFF" (design effect) 在 §5.4 首次使用时有定义✓。整体符号系统一致。

=== 章节过渡与逻辑流 ===

- [info] [过渡] Experiments 子节（§5.2→§5.3→§5.4→§5.5→§5.7→§5.8）之间缺少过渡句。各节直接开始新话题，读者需要自行理解逻辑链。§5.3 Scaling Behavior 插在 Function-Level Results 和 Equivalence 之间，打断了"func-level 结果→等价性检验"的自然叙事。

=== Limitations 诚实度 ===

- [info] [Limitations] 208 words ✓，6 个 distinct limitations ✓，均为实质性限制（非"future work will"回避式）✓。Limitations 质量良好。

=== 去 AI 风格 ===

- [warning] [去AI] abstract.tex:4 ", establishing that classification is not inherently easier..." — -ing 分词短语结尾，典型 AI 写法
- [warning] [去AI] abstract.tex:4 ", revealing model-dependent sensitivity" — -ing 分词短语结尾
- [warning] [去AI] introduction.tex:13 ", revealing model-dependent sensitivity" — 同上，且与 Abstract 重复使用完全相同的 -ing 短语
- [warning] [去AI] experiments.tex:98 "Notably, the DeepSeek..." — filler word "Notably"
- [warning] [去AI] experiments.tex:98 ", providing diagnostic information..." — -ing 分词短语
- [warning] [去AI] experiments.tex:137 ", confirming the gap is formulation-driven" — -ing 分词短语
- [warning] [去AI] method.tex:22 ", making long outputs exponentially harder" — -ing 分词短语
- [info] [去AI] em-dash (—) 和解释性 en-dash (–) 扫描为零 ✓

[CONTENT_AUDIT_END]
```

**摘要**：1 critical（\tbd{} 占位符），11 warning（叙事重复、Abstract 数字过密、-ing AI 痕迹、计算预算不一致、single-seed claim 限定缺失），8 info。最紧急的是 Table 4 的 \tbd{} 占位符——投稿前必须填入实际数据或删除对应行。叙事一致性整体良好，主要问题是 Abstract/Intro 信息密度过高导致重复，以及 ~6 处 -ing 分词短语的 AI 风格残留。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b74a9e1-6d92-4b4d-b487-8c78e93d5e0e",
  "isSidechain": false,
  "requestId": "req_011CbFFVZmSLdx8LT2oBYrBV",
  "type": "assistant",
  "uuid": "d36f5928-07ff-49db-b72c-77d41cafbaa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bc53qqDd4U4by3pY55Du1s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 86363,
      "output_tokens": 6483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6483,
          "cache_read_input_tokens": 86363,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
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

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 19 war…",
  "leafUuid": "d36f5928-07ff-49db-b72c-77d41cafbaa8",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 19 war…",
  "leafUuid": "d36f5928-07ff-49db-b72c-77d41cafbaa8",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper structure for EMNLP 2026 submission",
  "sessionId": "43c1129e-1ff2-4956-a248-b1a9430c423b"
}
```

---
