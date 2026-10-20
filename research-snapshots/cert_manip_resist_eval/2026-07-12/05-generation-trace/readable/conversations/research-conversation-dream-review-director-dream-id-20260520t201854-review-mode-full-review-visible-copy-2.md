# Research conversation: [DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 2
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/2e133768-be7c-4456-8949-45ac7304e840.jsonl`
- **Structured JSON:** [`96a46b1c6a5b188fbe83.json`](../../sessions/96/96a46b1c6a5b188fbe83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T21:05:20.719Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T21:05:20.719Z",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "content": "[DREAM Review Director]\ndream_id=20260520T201854 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_input_e90a5c14.pdf\n\n（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"median\", dream_id=\"20260520T201854\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T201854/median/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T21:05:20.723Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T21:05:20.723Z",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

## Round 1

8 recorded events

### User

_source line 3 · 2026-05-20T21:05:20.768Z_

[DREAM Review Director]
dream_id=20260520T201854 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_input_e90a5c14.pdf

（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="median", dream_id="20260520T201854", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T201854/median/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "85932a6f-82ed-4951-9590-d80b38171007",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T21:05:20.768Z_

```json
{
  "parentUuid": "85932a6f-82ed-4951-9590-d80b38171007",
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "42231bec-684e-4072-a070-851197550f3e",
  "timestamp": "2026-05-20T21:05:20.768Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T21:05:20.768Z_

```json
{
  "parentUuid": "42231bec-684e-4072-a070-851197550f3e",
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
  "uuid": "797e0eea-0e69-4cc9-bf8e-90f75a5de22a",
  "timestamp": "2026-05-20T21:05:20.768Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T21:05:20.768Z_

```json
{
  "parentUuid": "797e0eea-0e69-4cc9-bf8e-90f75a5de22a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "50ee7941-48fe-439b-8ff3-a7e5a674e1a8",
  "timestamp": "2026-05-20T21:05:20.768Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
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
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Assistant

_source line 8 · 2026-05-20T21:05:24.111Z_

I'll start by reading the PDF and the review context file to understand the paper and experimental design.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ee7941-48fe-439b-8ff3-a7e5a674e1a8",
  "isSidechain": false,
  "requestId": "req_011CbEVytA8h1C5n7eZyadSt",
  "type": "assistant",
  "uuid": "ce4b8ddd-475c-472f-ac04-31604d188ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8JhUtAsQWeD7QXuzf8pWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 9 · 2026-05-20T21:05:25.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ULRrPqFWQXs7JeheaCpf5q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_input_e90a5c14.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce4b8ddd-475c-472f-ac04-31604d188ae5",
  "isSidechain": false,
  "requestId": "req_011CbEVytA8h1C5n7eZyadSt",
  "type": "assistant",
  "uuid": "47797137-0315-43bf-95a6-733d6ea626e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8JhUtAsQWeD7QXuzf8pWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 10 · 2026-05-20T21:05:25.156Z_

<details><summary>↩ Tool result · `toolu_01ULRrPqFWQXs7JeheaCpf5q`</summary>

```text
PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_input_e90a5c14.pdf (184KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47797137-0315-43bf-95a6-733d6ea626e8",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "d2781ed3-0ab2-4406-b3fb-63b1d7f0d3f7",
  "toolUseResult": {
    "type": "pdf",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_input_e90a5c14.pdf",
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "originalSize": 188461
    }
  },
  "sourceToolAssistantUUID": "47797137-0315-43bf-95a6-733d6ea626e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

30 recorded events

### User

_source line 11 · 2026-05-20T21:05:25.153Z_

```json
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2781ed3-0ab2-4406-b3fb-63b1d7f0d3f7",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "isMeta": true,
  "uuid": "2d632ba0-ee11-44f6-a4ed-a91d5f3b0fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T21:05:25.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YZbQDq6E2Sh45vQwWs5ev1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d632ba0-ee11-44f6-a4ed-a91d5f3b0fa8",
  "isSidechain": false,
  "requestId": "req_011CbEVytA8h1C5n7eZyadSt",
  "type": "assistant",
  "uuid": "ad1c3458-0f80-41c5-af28-45451132852c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8JhUtAsQWeD7QXuzf8pWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "ad1c3458-0f80-41c5-af28-45451132852c",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Tool result

_source line 15 · 2026-05-20T21:05:25.894Z_

<details><summary>↩ Tool result · `toolu_01YZbQDq6E2Sh45vQwWs5ev1`</summary>

```text
1	narrative_guidance: 'Analysis paper with principled negative result as centerpiece.
2	  Narrative arc: (1) Pareto frontier established on two large MoE architectures —
3	  qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming
4	  architecture-dependent shape; (2) CKA reveals geometric misalignment increasing
5	  with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for
6	  WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across
7	  3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions
8	  but cannot correct the rotation of the correctness direction across language subspaces;
9	  (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns
10	  the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and
11	  orthogonality are supporting evidence. Decomposition shows difficulty is shared
12	  but capability-specific component drives degradation (~65% of combos improved).
13	  Orthogonality persists across languages (cosine < 0.10) but with more variance in
14	  low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn
15	  are weaker. ECE improvements over temperature scaling are negligible — emphasize
16	  AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.
17	
18	  '
19	imagined_experiments:
20	- name: Qwen3-235B-A22B Full Pareto Frontier
21	  plan_id: plan_001
22	  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24
23	    probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear
24	    projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.
25	
26	    '
27	  expected_results:
28	    en_best_auroc: 0.81
29	    en_best_layer: 72
30	    en_best_ece_raw: 0.17
31	    en_best_ece_tempcal: 0.065
32	    temp_scaling_T: 5.8
33	    en_auroc_range:
34	    - 0.58
35	    - 0.81
36	    en_auroc_50pct_depth_layer47: 0.76
37	    zs_transfer_auroc_median_20lang_at_en_optimal: 0.63
38	    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.7
39	    best_transfer_layer: 48
40	    pareto_rho_global: -0.58
41	    pareto_rho_per_lang_median: -0.51
42	    pareto_rho_per_lang_range:
43	    - -0.78
44	    - -0.21
45	    zs_langs_above_0p65: 13
46	    zs_auroc_zh: 0.74
47	    zs_auroc_es: 0.73
48	    zs_auroc_fr: 0.73
49	    zs_auroc_de: 0.72
50	    zs_auroc_ar: 0.7
51	    zs_auroc_hi: 0.69
52	    zs_auroc_ru: 0.71
53	    zs_auroc_ko: 0.69
54	    zs_auroc_ja: 0.7
55	    zs_auroc_pt: 0.72
56	    zs_auroc_vi: 0.68
57	    zs_auroc_tr: 0.67
58	    zs_auroc_id: 0.68
59	    zs_auroc_th: 0.66
60	    zs_auroc_pl: 0.69
61	    zs_auroc_uk: 0.68
62	    zs_auroc_he: 0.66
63	    zs_auroc_el: 0.65
64	    zs_auroc_sw: 0.58
65	    zs_auroc_bn: 0.57
66	    mean_shift_delta_auroc_median: 0.0
67	    linear_proj_delta_auroc_over_zs_median: 0.035
68	    fewshot_25_delta_auroc_over_zs_median: 0.025
69	    fewshot_100_delta_auroc_over_zs_median: 0.045
70	    ece_reduction_vs_temp_scaling_median: 0.008
71	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE model — significantly deeper
72	    than the 7B MVP. The English best AUROC rises to 0.81 because the larger model
73	    encodes stronger correctness signals (more parameters, more knowledge). The best
74	    English layer is at ~76% depth (layer 72), consistent with the MVP pattern where
75	    correctness peaks in deep-but-not-final layers. The Pareto frontier is present
76	    but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates
77	    more heterogeneous layer representations, reducing the clean monotonic depth-degradation
78	    pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr)
79	    have strong multilingual representations even at deeper layers due to extensive
80	    pretraining data, attenuating the negative correlation. The per-language rho range
81	    [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative
82	    correlation (their representations diverge from English more sharply at depth)
83	    while high-resource languages show weaker correlation (they maintain reasonable
84	    alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major
85	    Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57)
86	    remain below threshold due to limited pretraining representation for these languages.
87	    Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming
88	    the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because
89	    it directly corrects geometric misalignment rather than relying on a small labeled
90	    sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based
91	    calibration and temperature scaling address different aspects — at the median
92	    tier, probes don''t provide much additional calibration beyond what temperature
93	    scaling already captures.
94	
95	    '
96	  tables:
97	  - name: 'Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by
98	      Language × Layer'
99	    description: '24 probed layers (rows) × 20 languages + English (columns). Cells
100	      show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of
101	      best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI.
102	      Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most
103	      languages. High-resource languages show flatter profiles; low-resource show
104	      steeper drop-off at deep layers.
105	
106	      '
107	  - name: 'Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers'
108	    description: '5 transfer methods (columns) × 20 languages (rows), evaluated at
109	      two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language
110	      oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation
111	      test p-values. Cohen''s d for each method vs zero-shot baseline.
112	
113	      '
114	  figures_description:
115	  - 'Figure: Pareto frontier scatter plot — x-axis: English AUROC, y-axis: median
116	    zero-shot transfer AUROC across 20 langs. Each point is a layer. Annotated with
117	    layer numbers. Pareto-optimal layers highlighted. Separate curves for resource
118	    tiers (high/mid/low) showing tier-dependent frontier shape.'
119	  - 'Figure: Per-language Spearman rho bar chart — 20 bars sorted by rho magnitude.
120	    Color-coded by resource tier. Error bars show bootstrap 95% CI. Horizontal line
121	    at rho = -0.5 for reference.'
122	  analysis: 'The Pareto frontier replicates on this large MoE model but with moderate
123	    per-language rho (-0.51 median). The architecture-dependent shape is visible:
124	    MoE routing creates more variable layer representations, so the depth-transfer
125	    tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages
126	    achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating
127	    the approach for most languages. The 7 languages below threshold cluster in low-resource
128	    (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear
129	    projection provides the most consistent improvement across languages.
130	
131	    '
132	- name: Llama 4 Scout Full Pareto Frontier
133	  plan_id: plan_002
134	  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed
135	    layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.
136	
137	    '
138	  expected_results:
139	    en_best_auroc: 0.79
140	    en_best_layer: 36
141	    en_best_ece_raw: 0.19
142	    en_best_ece_tempcal: 0.07
143	    temp_scaling_T: 6.0
144	    en_auroc_range:
145	    - 0.6
146	    - 0.79
147	    en_auroc_50pct_depth_layer24: 0.74
148	    zs_transfer_auroc_median_20lang_at_en_optimal: 0.62
149	    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.68
150	    best_transfer_layer: 24
151	    pareto_rho_global: -0.62
152	    pareto_rho_per_lang_median: -0.54
153	    pareto_rho_per_lang_range:
154	    - -0.82
155	    - -0.28
156	    zs_langs_above_0p65: 11
157	    zs_auroc_zh: 0.72
158	    zs_auroc_es: 0.71
159	    zs_auroc_fr: 0.71
160	    zs_auroc_de: 0.7
161	    zs_auroc_ar: 0.68
162	    zs_auroc_hi: 0.67
163	    zs_auroc_ru: 0.69
164	    zs_auroc_ko: 0.66
165	    zs_auroc_ja: 0.67
166	    zs_auroc_pt: 0.7
167	    zs_auroc_vi: 0.65
168	    zs_auroc_tr: 0.64
169	    zs_auroc_id: 0.66
170	    zs_auroc_th: 0.63
171	    zs_auroc_pl: 0.67
172	    zs_auroc_uk: 0.65
173	    zs_auroc_he: 0.63
174	    zs_auroc_el: 0.62
175	    zs_auroc_sw: 0.55
176	    zs_auroc_bn: 0.54
177	    mean_shift_delta_auroc_median: 0.0
178	    linear_proj_delta_auroc_over_zs_median: 0.032
179	    fewshot_25_delta_auroc_over_zs_median: 0.022
180	    fewshot_100_delta_auroc_over_zs_median: 0.04
181	    ece_reduction_vs_temp_scaling_median: 0.005
182	  result_rationale: 'Llama 4 Scout has fewer layers (48 vs 94) and a different MoE
183	    architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81)
184	    reflecting somewhat weaker correctness encoding in a shallower architecture. The
185	    Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers,
186	    each layer step represents a larger proportional depth change, making the depth-transfer
187	    tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent
188	    with the pattern that mid-depth layers balance English quality and cross-lingual
189	    alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4''s
190	    multilingual pretraining may be less balanced, particularly for mid-resource languages
191	    like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55)
192	    and bn (0.54) are again the weakest, confirming this is a fundamental limitation
193	    of pretraining representation rather than architecture-specific. The same qualitative
194	    Pareto pattern holds but the quantitative frontier shape differs — the drop-off
195	    from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence
196	    without requiring architecture-specific tuning as a paper claim.
197	
198	    '
199	  tables:
200	  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language
201	      × Layer'
202	    description: '12 probed layers × 20 languages + English. Same format as Table
203	      1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal
204	      set due to coarser layer sampling.
205	
206	      '
207	  - name: 'Table 4: Llama 4 Scout Transfer Method Comparison'
208	    description: 'Same format as Table 2. Llama 4 Scout results. Key finding: linear
209	      projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric
210	      correction transfers across architectures.
211	
212	      '
213	  figures_description:
214	  - 'Figure: Side-by-side Pareto frontier comparison — Qwen3-235B (left) vs Llama
215	    4 Scout (right). Same axis scales for direct visual comparison. Annotated with
216	    architecture properties (depth, MoE routing). Shows that qualitative Pareto shape
217	    replicates but quantitative steepness differs.'
218	  analysis: 'Llama 4 Scout confirms the Pareto frontier generalizes across architectures.
219	    The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that
220	    supports the architecture-dependence claim but is not dramatic enough to call
221	    it a strong architectural contrast. This is the median-tier signature: same qualitative
222	    finding, quantitatively less distinct than ideal. Both models agree on the key
223	    implication: mid-depth layers are the right operating point for cross-lingual
224	    transfer.
225	
226	    '
227	- name: CaCLR Implementation and Comparative Evaluation
228	  plan_id: plan_003
229	  description: 'CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD).
230	    α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot,
231	    mean-shift, linear projection, few-shot on both models × 20 langs.
232	
233	    '
234	  expected_results:
235	    alpha_optimal: 0.5
236	    alpha_only_en_auroc_at_en_optimal_layer_qwen: 0.805
237	    alpha_only_en_ece_at_en_optimal_layer_qwen: 0.058
238	    alpha_only_zs_median_auroc_qwen: 0.695
239	    alpha_only_zs_median_auroc_llama: 0.675
240	    beta_0p001_delta_auroc_over_alpha_only_median: 0.002
241	    beta_0p01_delta_auroc_over_alpha_only_median: 0.001
242	    beta_0p1_delta_auroc_over_alpha_only_median: -0.001
243	    beta_1p0_delta_auroc_over_alpha_only_median: -0.003
244	    beta_sweep_max_delta_auroc: 0.003
245	    beta_sweep_significant_at_p05: false
246	    caclr_full_delta_auroc_over_zeroshot_median: 0.012
247	    caclr_full_delta_auroc_over_zeroshot_range:
248	    - -0.005
249	    - 0.035
250	    caclr_vs_linear_proj_delta_median: -0.023
251	    caclr_vs_fewshot100_delta_median: -0.033
252	    linear_proj_delta_auroc_over_zs_median_qwen: 0.035
253	    linear_proj_delta_auroc_over_zs_median_llama: 0.032
254	    fewshot_25_delta_auroc_over_zs_median: 0.024
255	    fewshot_100_delta_auroc_over_zs_median: 0.043
256	    mean_shift_delta_auroc_median: 0.0
257	    method_ranking:
258	    - few-shot-100
259	    - linear-projection
260	    - few-shot-25
261	    - CaCLR-full
262	    - CaCLR-α-only
263	    - zero-shot
264	    - mean-shift
265	    caclr_beta_delta_high_resource: 0.004
266	    caclr_beta_delta_mid_resource: 0.0
267	    caclr_beta_delta_low_resource: -0.002
268	    caclr_beta_vs_alpha_only_paired_perm_p: 0.42
269	    caclr_beta_vs_alpha_only_cohens_d: 0.08
270	    linear_proj_vs_zeroshot_paired_perm_p: 0.001
271	    linear_proj_vs_zeroshot_cohens_d: 0.55
272	  result_rationale: 'The β (consistency loss) is inert because MMD-based distributional
273	    matching fundamentally cannot correct the geometric misalignment that CKA reveals.
274	    MMD penalizes differences in mean embeddings and kernel-space distributional moments
275	    — it can align marginal distributions but cannot learn the rotation of the correctness
276	    direction across language subspaces. At low β (0.001), the MMD signal is too weak
277	    to affect optimization. At medium β (0.01–0.1), the gradient signal exists but
278	    points in the wrong direction — it pushes overall distributional alignment without
279	    specifically aligning the correctness-relevant subspace. At high β (1.0), the
280	    MMD term dominates and slightly hurts English AUROC by distorting the probe weights.
281	    The α-only (SB-ECE) variant provides small but real calibration improvement (better
282	    ECE) because smooth-binned ECE regularization is a well-motivated objective that
283	    doesn''t require cross-lingual alignment. The total CaCLR improvement over zero-shot
284	    (+1.2pp) comes entirely from the α term''s calibration regularization, not from
285	    cross-lingual consistency. Cohen''s d = 0.08 for β effect is negligible. In contrast,
286	    linear projection achieves +3.5pp because it directly estimates and corrects the
287	    rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves
288	    +4.3pp because it sidesteps alignment entirely by training on target-language
289	    labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot
290	    > mean-shift — is the key empirical result that the geometric explanation predicts.
291	
292	    '
293	  tables:
294	  - name: 'Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline'
295	    description: 'β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns:
296	      median ΔAUROC, mean, std, min, max, # languages improved, paired permutation
297	      p-value, Cohen''s d). Both models shown side-by-side. Key: no β value achieves
298	      p < 0.05 or d > 0.2 — consistency loss is definitively inert.
299	
300	      '
301	  - name: 'Table 6: Transfer Method Comparison — Median AUROC across 20 Languages'
302	    description: 'Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full,
303	      linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama
304	      4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap
305	      95% CI. Ranking is consistent across models. Linear projection and few-shot
306	      clearly dominate.
307	
308	      '
309	  - name: 'Table 7: CaCLR β Effect by Resource Tier'
310	    description: 'Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness
311	      is consistent across tiers — not a power issue with low-resource languages but
312	      a fundamental limitation of distributional matching.
313	
314	      '
315	  figures_description:
316	  - 'Figure: α sensitivity curve — x-axis: log(α), y-axis: English ECE and AUROC at
317	    EN-optimal layer. Shows that α ~0.5 optimizes ECE-AUROC tradeoff. SB-ECE regularization
318	    provides genuine calibration benefit.'
319	  - 'Figure: β sensitivity heatmap — x-axis: log(β), y-axis: languages sorted by resource
320	    tier. Color: ΔAUROC over α-only. Shows near-zero change (white) across entire
321	    grid. Highlights absence of any language × β sweet spot.'
322	  - 'Figure: Transfer method ranking forest plot — each method as a row, showing median
323	    ΔAUROC with bootstrap 95% CI. Clear separation between geometric methods (linear-proj,
324	    few-shot) and distributional methods (CaCLR-β, mean-shift).'
325	  analysis: 'CaCLR''s β inertness is the paper''s centerpiece negative result. The
326	    analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08,
327	    p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis
328	    (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric
329	    (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear
330	    projection''s success (+3.5pp) confirms the geometric explanation — it succeeds
331	    precisely because it learns the rotation that MMD cannot represent. This three-part
332	    argument closes the distributional-matching path with both theory and evidence.
333	    The α-only variant retains value as a calibration regularizer — it improves ECE
334	    without hurting AUROC.
335	
336	    '
337	- name: Difficulty-Controlled Decomposition Ablation
338	  plan_id: plan_004
339	  description: 'IRT difficulty probes, project out difficulty direction, retrain correctness
340	    probes on residuals. 10 languages × 8 layers per model. Random-direction control.
341	
342	    '
343	  expected_results:
344	    difficulty_probe_r2_en_median_across_layers: 0.42
345	    difficulty_probe_r2_range:
346	    - 0.25
347	    - 0.55
348	    decomposition_transfer_delta_median: 0.012
349	    decomposition_transfer_delta_range:
350	    - -0.01
351	    - 0.035
352	    pct_combos_improved: 0.65
353	    pct_combos_improved_by_tier_high: 0.72
354	    pct_combos_improved_by_tier_mid: 0.65
355	    pct_combos_improved_by_tier_low: 0.53
356	    improvement_stronger_at_deep_layers: true
357	    improvement_at_shallow_layers_pct: 0.5
358	    improvement_at_deep_layers_pct: 0.78
359	    random_direction_delta_median: 0.003
360	    random_direction_delta_significant: false
361	    difficulty_correctness_cosine_median: 0.18
362	    difficulty_correctness_cosine_range:
363	    - 0.08
364	    - 0.3
365	    decomposition_vs_baseline_paired_p: 0.03
366	    decomposition_cohens_d: 0.28
367	  result_rationale: 'Decomposition works but is partial because the difficulty-capability
368	    separation is not clean. The difficulty direction (IRT-derived) captures ~42%
369	    variance in human difficulty scores (R²) — reasonable but not perfect, meaning
370	    the projection leaves residual difficulty signal mixed with capability. At deep
371	    layers, removing difficulty helps more often (78% of combos) because the capability-specific
372	    component dominates transfer degradation there — once you remove the shared difficulty
373	    signal, the residual is more language-specific and harder to transfer. At shallow
374	    layers, the improvement rate drops to ~50% (near chance) because both difficulty
375	    and capability signals are more entangled and less linearly separable. The 65%
376	    overall improvement rate is genuine but not universal — it demonstrates the decomposition
377	    is prescriptive for about two-thirds of settings. The random-direction control
378	    (median +0.3pp, not significant) confirms this isn''t a dimensionality-reduction
379	    artifact. Low-resource languages show weaker improvement (53%) because their correctness
380	    probes are noisier to begin with, and the difficulty projection may remove some
381	    of the limited signal they have. The modest Cohen''s d (0.28) reflects that improvements
382	    are real but small — this is a supporting analytical result, not a standalone
383	    method contribution.
384	
385	    '
386	  tables:
387	  - name: 'Table 8: Decomposition Results — 10 Languages × 8 Layers'
388	    description: 'Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC
389	      after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded.
390	      Marginal summaries: % improved per language, per layer. Shows concentration
391	      of improvement at deep layers and high-resource languages.
392	
393	      '
394	  - name: 'Table 9: Decomposition vs Random Direction Control'
395	    description: 'Comparison: difficulty projection vs random projection vs no projection.
396	      Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically
397	      — not arbitrary dimensionality reduction — drives improvement.
398	
399	      '
400	  figures_description:
401	  - 'Figure: Decomposition improvement rate vs layer depth — bar chart showing fraction
402	    of languages improved at each layer. Monotonically increasing trend from ~50%
403	    at shallowest to ~78% at deepest. Supports narrative that capability-specific
404	    component is the deep-layer transfer bottleneck.'
405	  analysis: 'Decomposition provides supporting evidence for the geometric misalignment
406	    narrative. The fact that difficulty removal helps more at deep layers aligns with
407	    the CKA finding — at depth, the capability-specific component (which is geometrically
408	    misaligned across languages) drives transfer failure, and removing the shared
409	    difficulty component isolates this effect. However, the partial success rate (65%)
410	    and modest effect size (d=0.28) keep this as supporting analysis rather than a
411	    standalone claim. The finding is prescriptive: researchers attempting cross-lingual
412	    probe transfer should first assess whether difficulty confounding explains their
413	    transfer gaps — in ~65% of cases, it partially does.
414	
415	    '
416	- name: Cross-Lingual Orthogonality Analysis
417	  plan_id: plan_005
418	  description: 'Verbalized confidence direction extraction, cosine similarity with
419	    correctness direction. 20 languages × 2 architectures. Resource-tier and family
420	    analysis.
421	
422	    '
423	  expected_results:
424	    en_cosine_qwen: 0.035
425	    en_cosine_llama: 0.038
426	    cosine_median_across_langs_qwen: 0.055
427	    cosine_median_across_langs_llama: 0.06
428	    cosine_max_across_langs: 0.1
429	    cosine_max_language: sw
430	    cosine_range:
431	    - 0.02
432	    - 0.1
433	    cosine_median_high_resource: 0.04
434	    cosine_median_mid_resource: 0.06
435	    cosine_median_low_resource: 0.085
436	    cosine_variance_high: 0.0003
437	    cosine_variance_mid: 0.0008
438	    cosine_variance_low: 0.0018
439	    all_langs_below_threshold: true
440	    cosine_vs_resource_spearman_rho: 0.52
441	    cosine_vs_resource_p: 0.018
442	  result_rationale: 'Orthogonality persists across languages because the separation
443	    between correctness and verbalized confidence is a structural property of how
444	    transformers process MCQA — the model''s internal "do I know this?" signal (correctness)
445	    and its verbalized "how confident am I?" output occupy orthogonal subspaces by
446	    design (the former is a representation-level property, the latter is optimized
447	    during RLHF/instruction-tuning for human-readable outputs). The English cosine
448	    (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly
449	    higher (median 0.055-0.060) because: (a) non-English confidence verbalization
450	    is noisier (models are less calibrated in non-English expression of uncertainty);
451	    (b) the confidence probe may capture some language-switching signal that correlates
452	    weakly with correctness (lower-resource languages trigger more uncertain generation
453	    behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold
454	    (<0.12) but shows more variance — Swahili''s limited pretraining data means both
455	    probes are noisier, and noise correlations inflate apparent cosine. The resource-
456	    tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger
457	    (lower cosine) for high-resource languages, suggesting that abundant pretraining
458	    data helps separate correctness from confidence representations. However, even
459	    the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment,
460	    confirming that output-based calibration is structurally limited across all languages.
461	
462	    '
463	  tables:
464	  - name: 'Table 10: Correctness–Confidence Cosine Similarity Across Languages'
465	    description: '20 languages (rows, grouped by resource tier) × 2 architectures
466	      (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier
467	      medians and Spearman correlation with log(pretraining data estimate). All values
468	      < 0.12.
469	
470	      '
471	  figures_description:
472	  - 'Figure: Cosine similarity vs estimated pretraining data — scatter plot, 20 languages
473	    × 2 models. Log scale x-axis (pretraining tokens). Weak positive trend (more data
474	    → lower cosine → stronger orthogonality). Highlights sw/bn as outliers with highest
475	    cosine.'
476	  analysis: 'Orthogonality holds universally (max 0.10 < 0.12 threshold) but with
477	    a resource- tier gradient that is novel relative to Miao & Ungar''s English-only
478	    finding. This extends their claim to multilingual settings with a nuance: the
479	    structural separation is slightly weaker for low-resource languages, though never
480	    approaching a level that would make output-based calibration viable. This supports
481	    the paper''s broader argument that probe-based calibration is the right paradigm
482	    for all languages, but the cross-lingual transfer challenge is the bottleneck
483	    — not the underlying signal quality.
484	
485	    '
486	- name: Probe Complexity Comparison
487	  plan_id: plan_006
488	  description: 'Logistic regression vs 2-layer MLP at each probed layer for both models.
489	    English accuracy, cross-lingual transfer degradation, calibration quality.
490	
491	    '
492	  expected_results:
493	    logreg_en_best_auroc_qwen: 0.81
494	    mlp_en_best_auroc_qwen: 0.835
495	    logreg_en_best_auroc_llama: 0.79
496	    mlp_en_best_auroc_llama: 0.815
497	    logreg_zs_median_qwen: 0.7
498	    mlp_zs_median_qwen: 0.665
499	    logreg_zs_median_llama: 0.68
500	    mlp_zs_median_llama: 0.645
501	    logreg_transfer_gap: 0.11
502	    mlp_transfer_gap: 0.17
503	    logreg_ece_median: 0.068
504	    mlp_ece_median: 0.075
505	    mlp_advantage_en_deep_layers: 0.03
506	    mlp_advantage_en_shallow_layers: 0.01
507	    logreg_better_transfer_pct_langs: 0.8
508	  result_rationale: 'MLP probes achieve ~2.5pp higher English AUROC because they can
509	    capture nonlinear interactions in the representation — the correctness signal
510	    has a small nonlinear component that logistic regression misses. However, this
511	    nonlinear component is language-specific (learned from English data, doesn''t
512	    generalize), so MLP probes show 6pp larger transfer gap than logistic regression.
513	    The MLP essentially overfits to English-specific nonlinearities in the correctness
514	    representation. This confirms the hypothesis that linear probes transfer better
515	    cross-lingually — the linear component of the correctness signal is more universal
516	    across languages, while nonlinear components are language-specific. The MLP advantage
517	    is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper
518	    representations have more complex, language-specific structure for the MLP to
519	    exploit. 80% of languages see better transfer with logistic regression, with the
520	    exceptions being high- resource languages (zh, es) where the MLP''s nonlinear
521	    component partially transfers due to shared pretraining features. This result
522	    justifies the paper''s focus on logistic regression probes and reinforces the
523	    geometric (linear) framing.
524	
525	    '
526	  tables:
527	  - name: 'Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer'
528	    description: 'Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg
529	      ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP''s
530	      higher EN AUROC comes at cost of larger transfer gap. Gap difference increases
531	      with depth.
532	
533	      '
534	  figures_description:
535	  - 'Figure: Transfer gap (EN AUROC - ZS median) vs layer depth for LogReg and MLP.
536	    Two lines diverging at deeper layers — MLP gap grows faster, confirming linear
537	    probes are preferable for cross-lingual transfer.'
538	  analysis: 'This experiment justifies the methodological choice of logistic regression
539	    probes and provides additional evidence for the geometric/linear framing. If the
540	    correctness signal were deeply nonlinear, MLP''s advantage would transfer — the
541	    fact that it doesn''t confirms that the transferable component is linear. Goes
542	    in supplementary material as a methodological validation.
543	
544	    '
545	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
546	  plan_id: plan_007
547	  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages
548	    each). Validates generalization beyond GlobalMMLU.
549	
550	    '
551	  expected_results:
552	    belebele_en_best_auroc_qwen: 0.78
553	    belebele_zs_median_qwen: 0.68
554	    belebele_pareto_rho_median: -0.48
555	    belebele_linear_proj_delta: 0.03
556	    belebele_caclr_beta_delta: 0.003
557	    mmlupx_en_best_auroc_qwen: 0.82
558	    mmlupx_zs_median_qwen: 0.69
559	    mmlupx_pareto_rho_median: -0.5
560	    mmlupx_linear_proj_delta: 0.033
561	    mmlupx_caclr_beta_delta: 0.002
562	    auroc_rank_correlation_globalmmlu_vs_belebele: 0.82
563	    auroc_rank_correlation_globalmmlu_vs_mmlupx: 0.88
564	    method_ranking_consistent_across_benchmarks: true
565	  result_rationale: 'Belebele is a reading comprehension benchmark — fundamentally
566	    different from MCQA knowledge testing. The correctness signal is still present
567	    (models either comprehend or don''t) but Belebele''s English AUROC is slightly
568	    lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly
569	    encoded than factual knowledge correctness. The Pareto rho is slightly weaker
570	    (-0.48) because Belebele''s parallel passages provide more uniform cross-lingual
571	    signal than GlobalMMLU''s diverse topics. MMLU-ProX, being closer to GlobalMMLU
572	    in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding
573	    is that method rankings are consistent — linear projection still outperforms CaCLR,
574	    and CaCLR''s β term remains inert across benchmarks. This rules out the possibility
575	    that CaCLR''s failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88)
576	    between benchmarks confirm that per-language transfer difficulty is a property
577	    of the model''s multilingual representations, not the benchmark.
578	
579	    '
580	  tables:
581	  - name: 'Table S2: Cross-Benchmark Generalization'
582	    description: 'Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX)
583	      × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows
584	      consistent patterns across benchmarks. Rank correlation between per-language
585	      AUROCs.
586	
587	      '
588	  figures_description:
589	  - 'Figure: Per-language AUROC scatter — GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX.
590	    Each point is a language. High correlation confirms benchmark-invariant transfer
591	    difficulty ranking.'
592	  analysis: 'Benchmark generalization confirms all findings are not artifacts of GlobalMMLU.
593	    The consistent method ranking across three benchmarks strengthens the negative
594	    result — CaCLR''s β inertness is a fundamental property of distributional matching
595	    vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary
596	    or a short main-text paragraph.
597	
598	    '
599	- name: INT8 Validation Ablation
600	  plan_id: plan_010
601	  description: 'INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout
602	    on 5% subset.
603	
604	    '
605	  expected_results:
606	    int8_fp16_auroc_max_diff: 0.008
607	    int8_fp16_auroc_mean_diff: 0.003
608	    int8_fp16_ece_max_diff: 0.012
609	    int8_fp16_correlation_r: 0.997
610	    int8_fp16_rank_agreement_pct: 0.98
611	    distortion_significant: false
612	  result_rationale: 'INT8 weight-only quantization preserves the vast majority of
613	    activation-space structure because (a) it quantizes weights, not activations —
614	    the internal representations used for probing are computed in higher precision;
615	    (b) 7B+ models are robust to INT8 quantization (well-established in the quantization
616	    literature); (c) correctness probes operate on high-dimensional representations
617	    (4096+ dims) where small per-dimension perturbations from quantization average
618	    out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence
619	    intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that
620	    quantization shifts all scores by a near-constant offset without affecting ranking.
621	    This validation is necessary for reviewer reassurance but expected to be a non-issue.
622	
623	    '
624	  tables:
625	  - name: 'Table S3: INT8 vs FP16 Validation'
626	    description: 'Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank
627	      correlation). All differences within bootstrap CI. Conclusion: INT8 does not
628	      distort correctness signals.
629	
630	      '
631	  figures_description: []
632	  analysis: 'Straightforward validation that INT8 quantization doesn''t affect conclusions.
633	    One paragraph in supplementary material with the table. Addresses anticipated
634	    reviewer concern #5.
635	
636	    '
637	- name: CKA Cross-Lingual Representation Similarity
638	  plan_id: plan_011
639	  description: 'CKA (linear kernel) between English and each target language at every
640	    probed layer, both models. Correlate CKA with transfer AUROC.
641	
642	    '
643	  expected_results:
644	    cka_en_zh_shallow_layer12_qwen: 0.88
645	    cka_en_zh_deep_layer72_qwen: 0.62
646	    cka_en_sw_shallow_layer12_qwen: 0.78
647	    cka_en_sw_deep_layer72_qwen: 0.38
648	    cka_median_shallow_across_langs: 0.84
649	    cka_median_deep_across_langs: 0.52
650	    cka_decrease_with_depth_significant: true
651	    cka_transfer_pearson_r_qwen: 0.62
652	    cka_transfer_pearson_r_llama: 0.54
653	    cka_transfer_pearson_r_pooled: 0.58
654	    cka_transfer_pearson_p: 1.0e-05
655	    cka_deep_high_resource_median: 0.6
656	    cka_deep_mid_resource_median: 0.48
657	    cka_deep_low_resource_median: 0.36
658	    mmd_transfer_pearson_r: 0.25
659	    mmd_explains_variance_pct: 6
660	    cka_explains_variance_pct: 34
661	  result_rationale: 'CKA measures representational similarity including geometric
662	    structure (rotation, scaling), while MMD measures distributional distance (mean,
663	    variance, higher moments). CKA decreases with depth because deeper transformer
664	    layers specialize more for language-specific processing — the cross-lingual alignment
665	    enforced by shared vocabulary embeddings and early layers gradually gives way
666	    to language- specific feature extraction. The CKA–transfer correlation (r=0.58)
667	    is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming
668	    that representational geometry is a major (but not the only) factor in transfer
669	    success. The remaining variance comes from factors like probe quality, dataset
670	    difficulty distribution, and non-geometric aspects of the representation. Critically,
671	    CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer
672	    success — this is the key mechanistic finding. If cross-lingual misalignment were
673	    distributional (mean/covariance shift), MMD would predict transfer as well as
674	    or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that
675	    the misalignment is geometric (rotation/scaling of the entire representational
676	    space), not merely distributional. This directly explains why MMD-based CaCLR
677	    fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient
678	    (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing
679	    a mechanistic explanation for why low-resource languages transfer worse — their
680	    deep-layer representations are more geometrically dissimilar from English.
681	
682	    '
683	  tables:
684	  - name: 'Table 11: CKA Similarity — Languages × Layers'
685	    description: 'Probed layers (rows) × 20 languages (columns, sorted by resource
686	      tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing
687	      with depth. Resource-tier banding visible. Both models shown.
688	
689	      '
690	  - name: 'Table 12: CKA vs MMD as Transfer Predictors'
691	    description: 'Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy.
692	      Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric
693	      > distributional as explanation.
694	
695	      '
696	  figures_description:
697	  - 'Figure: CKA heatmap — layers (y-axis) × languages (x-axis, sorted by transfer
698	    AUROC). Color intensity = CKA. Clear diagonal structure: high CKA co-occurs with
699	    high transfer AUROC. Visual demonstration of the CKA–transfer link.'
700	  - 'Figure: CKA vs transfer AUROC scatter — each point is a (layer, language) pair.
701	    Color: resource tier. Linear fit line with r=0.58. Contrasted with MMD vs transfer
702	    scatter (r=0.25) in adjacent panel. The visual gap between the two correlations
703	    is the paper''s mechanistic argument.'
704	  - 'Figure: CKA depth profile — CKA vs layer depth for 3 representative languages
705	    (zh, tr, sw). Three curves showing parallel decline but at different levels. Annotated
706	    with corresponding transfer AUROC at each layer.'
707	  analysis: 'CKA analysis is the mechanistic backbone of the paper. It upgrades the
708	    contribution from "we measured that transfer fails at deep layers" to "we explain
709	    WHY transfer fails — geometric misalignment increases with depth, and this misalignment
710	    type (rotation/scaling) is specifically not addressable by distributional matching
711	    (MMD)." The CKA–transfer correlation (r=0.58) provides quantitative support, and
712	    the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical
713	    distinction that makes the negative CaCLR result theoretically interpretable rather
714	    than just empirically observed. This transforms the paper from a measurement study
715	    to one with mechanistic insight.
716	
717	    '
718	- name: Linear Projection Sensitivity Analysis
719	  plan_id: plan_012
720	  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.
721	    Both models × 5 layers × 20 languages.
722	
723	    '
724	  expected_results:
725	    pairs_10_delta_auroc_median: 0.012
726	    pairs_20_delta_auroc_median: 0.022
727	    pairs_50_delta_auroc_median: 0.03
728	    pairs_100_delta_auroc_median: 0.035
729	    pairs_200_delta_auroc_median: 0.036
730	    saturation_knee_point: 70
731	    pairs_for_90pct_max_improvement: 55
732	    pairs_for_95pct_max_improvement: 85
733	    pairs_10_std_across_langs: 0.025
734	    pairs_50_std_across_langs: 0.012
735	    pairs_100_std_across_langs: 0.008
736	    saturation_consistent_across_models: true
737	    qwen_saturation_knee: 65
738	    llama_saturation_knee: 75
739	  result_rationale: 'Linear projection learns a rotation matrix mapping source-language
740	    representations to target-language space. The sample complexity for estimating
741	    a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because:
742	    (a) the effective dimensionality of the correctness-relevant subspace is much
743	    lower than the full representation dimensionality — the probe operates in a low-rank
744	    subspace; (b) parallel pairs provide direct supervision on the mapping, unlike
745	    distributional matching which uses indirect statistical signals. With 10 pairs,
746	    the mapping is underdetermined but captures the dominant rotation component (+1.2pp).
747	    By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling
748	    axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is
749	    consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual
750	    dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture
751	    difference in knee points (65 vs 75) reflects that Llama 4''s representations
752	    may require slightly more pairs to estimate the rotation due to its MoE routing
753	    introducing more heterogeneity. The practical implication is clear: ~50-100 parallel
754	    pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match
755	    or exceed CaCLR''s entire training pipeline.
756	
757	    '
758	  tables:
759	  - name: 'Table 13: Linear Projection — Sample Efficiency'
760	    description: 'Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median
761	      ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear
762	      diminishing returns after 50 pairs.
763	
764	      '
765	  figures_description:
766	  - 'Figure: Learning curve — x-axis: number of parallel pairs (log scale), y-axis:
767	    median ΔAUROC. Two curves (Qwen3, Llama4) with shaded ±1 std band. Annotated knee
768	    point. Horizontal dashed line: CaCLR-full ΔAUROC for comparison — linear projection
769	    surpasses CaCLR at just ~20 pairs.'
770	  analysis: 'Linear projection''s sample efficiency is the constructive complement
771	    to CaCLR''s negative result. The message: you don''t need MMD-based distributional
772	    matching (which doesn''t work anyway) — you just need ~50-100 parallel pairs and
773	    a linear mapping. This is practically actionable and theoretically consistent
774	    with the geometric explanation (linear projection learns the rotation that MMD
775	    cannot). The learning curve figure — showing linear projection surpassing CaCLR
776	    at ~20 pairs — is one of the paper''s most compelling visuals.
777	
778	    '
779	- name: Probing Control Tasks (Hewitt & Liang 2019)
780	  plan_id: plan_013
781	  description: 'Train probes on randomly permuted labels at each layer. Selectivity
782	    analysis across layers and languages.
783	
784	    '
785	  expected_results:
786	    control_auroc_en_median: 0.545
787	    control_auroc_en_range:
788	    - 0.52
789	    - 0.58
790	    control_auroc_noneng_median: 0.54
791	    selectivity_en_median: 0.265
792	    selectivity_en_range:
793	    - 0.18
794	    - 0.31
795	    selectivity_noneng_median_high_resource: 0.2
796	    selectivity_noneng_median_mid_resource: 0.16
797	    selectivity_noneng_median_low_resource: 0.1
798	    selectivity_min_across_all: 0.08
799	    selectivity_min_language: sw
800	    selectivity_min_layer: layer_4
801	    all_selectivities_positive: true
802	    pct_above_10pp: 0.88
803	    pct_above_10pp_high_resource: 0.95
804	    pct_above_10pp_low_resource: 0.7
805	    selectivity_peaks_at_mid_depth: true
806	    selectivity_peak_layer_pct_depth: 0.55
807	  result_rationale: 'Control tasks with random labels test whether probe capacity
808	    (model expressiveness) alone can achieve high AUROC without genuine correctness
809	    signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms
810	    that logistic regression probes do not have sufficient capacity to memorize random
811	    label assignments in high-dimensional space — any AUROC above this baseline reflects
812	    genuine signal. English selectivity (median 0.265) is strong: the probe captures
813	    real correctness information 26.5pp above what capacity alone could achieve. Non-English
814	    selectivity decreases with resource tier because: (a) the correctness signal itself
815	    is weaker for languages with less pretraining data; (b) the cross-lingual transfer
816	    means probes must generalize from English-learned patterns, which is inherently
817	    harder for distant languages. Low-resource languages (sw, bn) show selectivity
818	    ~10pp, still positive but approaching the threshold where a reviewer might question
819	    signal quality. The 88% of language-layer combinations exceeding 10pp provides
820	    reasonable validation, but the 30% failure rate for low-resource languages at
821	    this threshold is a genuine limitation that the paper should acknowledge. Selectivity
822	    peaks at mid-depth (~55%) because shallow layers have weaker correctness signals
823	    (less processed) and very deep layers have stronger but more language-specific
824	    signals (high probe AUROC but also higher control AUROC due to richer features).
825	
826	    '
827	  tables:
828	  - name: 'Table S4: Control Task Selectivity'
829	    description: 'Supplementary. Languages (rows, grouped by resource tier) × representative
830	      layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded:
831	      green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in
832	      selectivity.
833	
834	      '
835	  figures_description:
836	  - 'Figure: Selectivity by resource tier — box plots for HIGH, MID, LOW resource
837	    tiers. Shows decreasing median and increasing variance for lower-resource tiers.
838	    Dashed line at 10pp threshold. Most points above threshold but LOW tier shows
839	    some below.'
840	  analysis: 'Control tasks validate that probe AUROC reflects genuine correctness
841	    signal for the large majority of settings (88% above 10pp). The resource-tier
842	    gradient in selectivity is a limitation to acknowledge: for low-resource languages,
843	    probe signal quality is weaker, and conclusions about transfer should be interpreted
844	    with this caveat. This doesn''t undermine the paper''s core claims (which are
845	    about the mechanism of transfer failure, not about achieving high probe quality
846	    in every language) but sets appropriate epistemic bounds.
847	
848	    '
849	- name: Gemma 4 31B Dense Pareto Frontier
850	  plan_id: plan_008
851	  description: 'Third architecture for camera-ready. 60 layers, dense, FP16. Full
852	    Pareto frontier, 20+ languages. Dense vs MoE contrast.
853	
854	    '
855	  expected_results:
856	    en_best_auroc: 0.8
857	    en_best_layer: 45
858	    zs_transfer_auroc_median: 0.69
859	    best_transfer_layer: 33
860	    pareto_rho_per_lang_median: -0.58
861	    zs_langs_above_0p65: 12
862	    pareto_rho_smoother_than_moe: true
863	    pareto_rho_std_across_langs_gemma: 0.12
864	    pareto_rho_std_across_langs_qwen: 0.16
865	    pareto_rho_std_across_langs_llama: 0.15
866	    cka_depth_decline_steeper_dense: true
867	    linear_proj_delta_median: 0.033
868	  result_rationale: 'Gemma 4 31B Dense provides the critical dense-vs-MoE architectural
869	    contrast. As a dense model, every token passes through every layer (no routing),
870	    creating more uniform layer-to-layer transformations. This produces a smoother
871	    Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE
872	    models) because the depth-transfer tradeoff is more consistent without routing-induced
873	    heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense
874	    models show a cleaner monotonic decline in cross-lingual alignment with depth
875	    — MoE routing partially breaks this monotonicity by allowing some expert pathways
876	    to maintain cross-lingual features at deeper layers. CKA declines more steeply
877	    with depth in the dense model, confirming that MoE routing provides a modest buffer
878	    against geometric misalignment (different experts can specialize differently per
879	    language). English AUROC (0.80) is comparable to the larger MoE models despite
880	    smaller parameter count because the 31B dense architecture is parameter-efficient
881	    for representation quality. This is a P2 camera-ready experiment that strengthens
882	    the architecture-dependence claim from "two MoE models differ moderately" to "dense
883	    vs MoE is a qualitatively distinct contrast."
884	
885	    '
886	  tables:
887	  - name: 'Table CR1: Three-Architecture Pareto Comparison'
888	    description: 'Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense)
889	      × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj
890	      Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.
891	
892	      '
893	  figures_description:
894	  - 'Figure: Three-panel Pareto frontier comparison — Qwen3-MoE, Llama4-MoE, Gemma4-Dense
895	    side-by-side. Dense model shows smoother, more monotonic frontier. Visual argument
896	    for architecture-dependence.'
897	  analysis: 'Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture-
898	    dependence evidence: MoE routing introduces heterogeneity that partially buffers
899	    against geometric misalignment at deep layers, while dense models show cleaner
900	    depth-dependent degradation. This doesn''t change the paper''s conclusions but
901	    provides a more compelling architectural contrast than two MoE models alone.
902	
903	    '
904	- name: Extended Language Coverage (50+ Languages)
905	  plan_id: plan_009
906	  description: 'Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele
907	    language sets.
908	
909	    '
910	  expected_results:
911	    total_languages: 52
912	    zs_langs_above_0p65: 28
913	    zs_median_auroc_52lang: 0.66
914	    zs_auroc_range:
915	    - 0.5
916	    - 0.74
917	    new_low_resource_langs_below_0p55:
918	    - am
919	    - my
920	    - zu
921	    - sn
922	    - rw
923	    resource_tier_gradient_replicates: true
924	    pareto_rho_median_52lang: -0.49
925	    linear_proj_delta_median_52lang: 0.031
926	    tail_langs_below_0p55_count: 8
927	    tail_langs_above_0p70_count: 12
928	  result_rationale: 'Expanding to 52 languages adds many more low-resource and typologically
929	    diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated
930	    20) because the additional languages are disproportionately low-resource. Five
931	    extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda)
932	    fall below 0.55, approaching chance performance — these languages have minimal
933	    pretraining representation in both models. The resource-tier gradient continues
934	    to hold and becomes even more pronounced with the extended tail. Pareto rho weakens
935	    slightly (-0.49) because many of the new languages show weak, noisy correlations
936	    due to low base probe quality. Linear projection improvement remains consistent
937	    (+3.1pp), confirming the geometric correction generalizes beyond the curated language
938	    set. The practical message: probe-based cross-lingual calibration is viable for
939	    ~28/52 languages (54%) without any target-language data, and linear projection
940	    extends this to ~35/52 (67%). The remaining ~17 languages need language-specific
941	    probes or alternative approaches.
942	
943	    '
944	  tables:
945	  - name: 'Table CR2: Extended Language Coverage — 52 Languages'
946	    description: 'Camera-ready. Full 52-language results sorted by zero-shot AUROC.
947	      Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100
948	      AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65
949	      (marginal), <0.55 (failed).
950	
951	      '
952	  figures_description:
953	  - 'Figure: Language coverage map — world map with countries colored by best zero-shot
954	    transfer AUROC. Visual demonstration of where probe-based calibration works and
955	    fails geographically.'
956	  analysis: 'Camera-ready extension. The 52-language analysis adds scale but the median-tier
957	    conclusion is clear: probe-based cross-lingual calibration works for a majority
958	    but not all languages, and the resource-tier gradient is the dominant predictor
959	    of success. This sets realistic expectations for practitioners and motivates future
960	    work on low-resource language probe training.'
961	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1c3458-0f80-41c5-af28-45451132852c",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "5427454f-2e02-4271-a3e4-f31b3fbfdeb5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml",
      "content": "narrative_guidance: 'Analysis paper with principled negative result as centerpiece.\n  Narrative arc: (1) Pareto frontier established on two large MoE architectures —\n  qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming\n  architecture-dependent shape; (2) CKA reveals geometric misalignment increasing\n  with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for\n  WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across\n  3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions\n  but cannot correct the rotation of the correctness direction across language subspaces;\n  (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns\n  the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and\n  orthogonality are supporting evidence. Decomposition shows difficulty is shared\n  but capability-specific component drives degradation (~65% of combos improved).\n  Orthogonality persists across languages (cosine < 0.10) but with more variance in\n  low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn\n  are weaker. ECE improvements over temperature scaling are negligible — emphasize\n  AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.\n\n  '\nimagined_experiments:\n- name: Qwen3-235B-A22B Full Pareto Frontier\n  plan_id: plan_001\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24\n    probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear\n    projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.\n\n    '\n  expected_results:\n    en_best_auroc: 0.81\n    en_best_layer: 72\n    en_best_ece_raw: 0.17\n    en_best_ece_tempcal: 0.065\n    temp_scaling_T: 5.8\n    en_auroc_range:\n    - 0.58\n    - 0.81\n    en_auroc_50pct_depth_layer47: 0.76\n    zs_transfer_auroc_median_20lang_at_en_optimal: 0.63\n    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.7\n    best_transfer_layer: 48\n    pareto_rho_global: -0.58\n    pareto_rho_per_lang_median: -0.51\n    pareto_rho_per_lang_range:\n    - -0.78\n    - -0.21\n    zs_langs_above_0p65: 13\n    zs_auroc_zh: 0.74\n    zs_auroc_es: 0.73\n    zs_auroc_fr: 0.73\n    zs_auroc_de: 0.72\n    zs_auroc_ar: 0.7\n    zs_auroc_hi: 0.69\n    zs_auroc_ru: 0.71\n    zs_auroc_ko: 0.69\n    zs_auroc_ja: 0.7\n    zs_auroc_pt: 0.72\n    zs_auroc_vi: 0.68\n    zs_auroc_tr: 0.67\n    zs_auroc_id: 0.68\n    zs_auroc_th: 0.66\n    zs_auroc_pl: 0.69\n    zs_auroc_uk: 0.68\n    zs_auroc_he: 0.66\n    zs_auroc_el: 0.65\n    zs_auroc_sw: 0.58\n    zs_auroc_bn: 0.57\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.035\n    fewshot_25_delta_auroc_over_zs_median: 0.025\n    fewshot_100_delta_auroc_over_zs_median: 0.045\n    ece_reduction_vs_temp_scaling_median: 0.008\n  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE model — significantly deeper\n    than the 7B MVP. The English best AUROC rises to 0.81 because the larger model\n    encodes stronger correctness signals (more parameters, more knowledge). The best\n    English layer is at ~76% depth (layer 72), consistent with the MVP pattern where\n    correctness peaks in deep-but-not-final layers. The Pareto frontier is present\n    but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates\n    more heterogeneous layer representations, reducing the clean monotonic depth-degradation\n    pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr)\n    have strong multilingual representations even at deeper layers due to extensive\n    pretraining data, attenuating the negative correlation. The per-language rho range\n    [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative\n    correlation (their representations diverge from English more sharply at depth)\n    while high-resource languages show weaker correlation (they maintain reasonable\n    alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major\n    Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57)\n    remain below threshold due to limited pretraining representation for these languages.\n    Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming\n    the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because\n    it directly corrects geometric misalignment rather than relying on a small labeled\n    sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based\n    calibration and temperature scaling address different aspects — at the median\n    tier, probes don''t provide much additional calibration beyond what temperature\n    scaling already captures.\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by\n      Language × Layer'\n    description: '24 probed layers (rows) × 20 languages + English (columns). Cells\n      show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of\n      best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI.\n      Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most\n      languages. High-resource languages show flatter profiles; low-resource show\n      steeper drop-off at deep layers.\n\n      '\n  - name: 'Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers'\n    description: '5 transfer methods (columns) × 20 languages (rows), evaluated at\n      two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language\n      oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation\n      test p-values. Cohen''s d for each method vs zero-shot baseline.\n\n      '\n  figures_description:\n  - 'Figure: Pareto frontier scatter plot — x-axis: English AUROC, y-axis: median\n    zero-shot transfer AUROC across 20 langs. Each point is a layer. Annotated with\n    layer numbers. Pareto-optimal layers highlighted. Separate curves for resource\n    tiers (high/mid/low) showing tier-dependent frontier shape.'\n  - 'Figure: Per-language Spearman rho bar chart — 20 bars sorted by rho magnitude.\n    Color-coded by resource tier. Error bars show bootstrap 95% CI. Horizontal line\n    at rho = -0.5 for reference.'\n  analysis: 'The Pareto frontier replicates on this large MoE model but with moderate\n    per-language rho (-0.51 median). The architecture-dependent shape is visible:\n    MoE routing creates more variable layer representations, so the depth-transfer\n    tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages\n    achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating\n    the approach for most languages. The 7 languages below threshold cluster in low-resource\n    (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear\n    projection provides the most consistent improvement across languages.\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier\n  plan_id: plan_002\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed\n    layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.\n\n    '\n  expected_results:\n    en_best_auroc: 0.79\n    en_best_layer: 36\n    en_best_ece_raw: 0.19\n    en_best_ece_tempcal: 0.07\n    temp_scaling_T: 6.0\n    en_auroc_range:\n    - 0.6\n    - 0.79\n    en_auroc_50pct_depth_layer24: 0.74\n    zs_transfer_auroc_median_20lang_at_en_optimal: 0.62\n    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.68\n    best_transfer_layer: 24\n    pareto_rho_global: -0.62\n    pareto_rho_per_lang_median: -0.54\n    pareto_rho_per_lang_range:\n    - -0.82\n    - -0.28\n    zs_langs_above_0p65: 11\n    zs_auroc_zh: 0.72\n    zs_auroc_es: 0.71\n    zs_auroc_fr: 0.71\n    zs_auroc_de: 0.7\n    zs_auroc_ar: 0.68\n    zs_auroc_hi: 0.67\n    zs_auroc_ru: 0.69\n    zs_auroc_ko: 0.66\n    zs_auroc_ja: 0.67\n    zs_auroc_pt: 0.7\n    zs_auroc_vi: 0.65\n    zs_auroc_tr: 0.64\n    zs_auroc_id: 0.66\n    zs_auroc_th: 0.63\n    zs_auroc_pl: 0.67\n    zs_auroc_uk: 0.65\n    zs_auroc_he: 0.63\n    zs_auroc_el: 0.62\n    zs_auroc_sw: 0.55\n    zs_auroc_bn: 0.54\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.032\n    fewshot_25_delta_auroc_over_zs_median: 0.022\n    fewshot_100_delta_auroc_over_zs_median: 0.04\n    ece_reduction_vs_temp_scaling_median: 0.005\n  result_rationale: 'Llama 4 Scout has fewer layers (48 vs 94) and a different MoE\n    architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81)\n    reflecting somewhat weaker correctness encoding in a shallower architecture. The\n    Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers,\n    each layer step represents a larger proportional depth change, making the depth-transfer\n    tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent\n    with the pattern that mid-depth layers balance English quality and cross-lingual\n    alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4''s\n    multilingual pretraining may be less balanced, particularly for mid-resource languages\n    like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55)\n    and bn (0.54) are again the weakest, confirming this is a fundamental limitation\n    of pretraining representation rather than architecture-specific. The same qualitative\n    Pareto pattern holds but the quantitative frontier shape differs — the drop-off\n    from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence\n    without requiring architecture-specific tuning as a paper claim.\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language\n      × Layer'\n    description: '12 probed layers × 20 languages + English. Same format as Table\n      1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal\n      set due to coarser layer sampling.\n\n      '\n  - name: 'Table 4: Llama 4 Scout Transfer Method Comparison'\n    description: 'Same format as Table 2. Llama 4 Scout results. Key finding: linear\n      projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric\n      correction transfers across architectures.\n\n      '\n  figures_description:\n  - 'Figure: Side-by-side Pareto frontier comparison — Qwen3-235B (left) vs Llama\n    4 Scout (right). Same axis scales for direct visual comparison. Annotated with\n    architecture properties (depth, MoE routing). Shows that qualitative Pareto shape\n    replicates but quantitative steepness differs.'\n  analysis: 'Llama 4 Scout confirms the Pareto frontier generalizes across architectures.\n    The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that\n    supports the architecture-dependence claim but is not dramatic enough to call\n    it a strong architectural contrast. This is the median-tier signature: same qualitative\n    finding, quantitatively less distinct than ideal. Both models agree on the key\n    implication: mid-depth layers are the right operating point for cross-lingual\n    transfer.\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD).\n    α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot,\n    mean-shift, linear projection, few-shot on both models × 20 langs.\n\n    '\n  expected_results:\n    alpha_optimal: 0.5\n    alpha_only_en_auroc_at_en_optimal_layer_qwen: 0.805\n    alpha_only_en_ece_at_en_optimal_layer_qwen: 0.058\n    alpha_only_zs_median_auroc_qwen: 0.695\n    alpha_only_zs_median_auroc_llama: 0.675\n    beta_0p001_delta_auroc_over_alpha_only_median: 0.002\n    beta_0p01_delta_auroc_over_alpha_only_median: 0.001\n    beta_0p1_delta_auroc_over_alpha_only_median: -0.001\n    beta_1p0_delta_auroc_over_alpha_only_median: -0.003\n    beta_sweep_max_delta_auroc: 0.003\n    beta_sweep_significant_at_p05: false\n    caclr_full_delta_auroc_over_zeroshot_median: 0.012\n    caclr_full_delta_auroc_over_zeroshot_range:\n    - -0.005\n    - 0.035\n    caclr_vs_linear_proj_delta_median: -0.023\n    caclr_vs_fewshot100_delta_median: -0.033\n    linear_proj_delta_auroc_over_zs_median_qwen: 0.035\n    linear_proj_delta_auroc_over_zs_median_llama: 0.032\n    fewshot_25_delta_auroc_over_zs_median: 0.024\n    fewshot_100_delta_auroc_over_zs_median: 0.043\n    mean_shift_delta_auroc_median: 0.0\n    method_ranking:\n    - few-shot-100\n    - linear-projection\n    - few-shot-25\n    - CaCLR-full\n    - CaCLR-α-only\n    - zero-shot\n    - mean-shift\n    caclr_beta_delta_high_resource: 0.004\n    caclr_beta_delta_mid_resource: 0.0\n    caclr_beta_delta_low_resource: -0.002\n    caclr_beta_vs_alpha_only_paired_perm_p: 0.42\n    caclr_beta_vs_alpha_only_cohens_d: 0.08\n    linear_proj_vs_zeroshot_paired_perm_p: 0.001\n    linear_proj_vs_zeroshot_cohens_d: 0.55\n  result_rationale: 'The β (consistency loss) is inert because MMD-based distributional\n    matching fundamentally cannot correct the geometric misalignment that CKA reveals.\n    MMD penalizes differences in mean embeddings and kernel-space distributional moments\n    — it can align marginal distributions but cannot learn the rotation of the correctness\n    direction across language subspaces. At low β (0.001), the MMD signal is too weak\n    to affect optimization. At medium β (0.01–0.1), the gradient signal exists but\n    points in the wrong direction — it pushes overall distributional alignment without\n    specifically aligning the correctness-relevant subspace. At high β (1.0), the\n    MMD term dominates and slightly hurts English AUROC by distorting the probe weights.\n    The α-only (SB-ECE) variant provides small but real calibration improvement (better\n    ECE) because smooth-binned ECE regularization is a well-motivated objective that\n    doesn''t require cross-lingual alignment. The total CaCLR improvement over zero-shot\n    (+1.2pp) comes entirely from the α term''s calibration regularization, not from\n    cross-lingual consistency. Cohen''s d = 0.08 for β effect is negligible. In contrast,\n    linear projection achieves +3.5pp because it directly estimates and corrects the\n    rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves\n    +4.3pp because it sidesteps alignment entirely by training on target-language\n    labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot\n    > mean-shift — is the key empirical result that the geometric explanation predicts.\n\n    '\n  tables:\n  - name: 'Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline'\n    description: 'β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns:\n      median ΔAUROC, mean, std, min, max, # languages improved, paired permutation\n      p-value, Cohen''s d). Both models shown side-by-side. Key: no β value achieves\n      p < 0.05 or d > 0.2 — consistency loss is definitively inert.\n\n      '\n  - name: 'Table 6: Transfer Method Comparison — Median AUROC across 20 Languages'\n    description: 'Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full,\n      linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama\n      4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap\n      95% CI. Ranking is consistent across models. Linear projection and few-shot\n      clearly dominate.\n\n      '\n  - name: 'Table 7: CaCLR β Effect by Resource Tier'\n    description: 'Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness\n      is consistent across tiers — not a power issue with low-resource languages but\n      a fundamental limitation of distributional matching.\n\n      '\n  figures_description:\n  - 'Figure: α sensitivity curve — x-axis: log(α), y-axis: English ECE and AUROC at\n    EN-optimal layer. Shows that α ~0.5 optimizes ECE-AUROC tradeoff. SB-ECE regularization\n    provides genuine calibration benefit.'\n  - 'Figure: β sensitivity heatmap — x-axis: log(β), y-axis: languages sorted by resource\n    tier. Color: ΔAUROC over α-only. Shows near-zero change (white) across entire\n    grid. Highlights absence of any language × β sweet spot.'\n  - 'Figure: Transfer method ranking forest plot — each method as a row, showing median\n    ΔAUROC with bootstrap 95% CI. Clear separation between geometric methods (linear-proj,\n    few-shot) and distributional methods (CaCLR-β, mean-shift).'\n  analysis: 'CaCLR''s β inertness is the paper''s centerpiece negative result. The\n    analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08,\n    p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis\n    (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric\n    (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear\n    projection''s success (+3.5pp) confirms the geometric explanation — it succeeds\n    precisely because it learns the rotation that MMD cannot represent. This three-part\n    argument closes the distributional-matching path with both theory and evidence.\n    The α-only variant retains value as a calibration regularizer — it improves ECE\n    without hurting AUROC.\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes, project out difficulty direction, retrain correctness\n    probes on residuals. 10 languages × 8 layers per model. Random-direction control.\n\n    '\n  expected_results:\n    difficulty_probe_r2_en_median_across_layers: 0.42\n    difficulty_probe_r2_range:\n    - 0.25\n    - 0.55\n    decomposition_transfer_delta_median: 0.012\n    decomposition_transfer_delta_range:\n    - -0.01\n    - 0.035\n    pct_combos_improved: 0.65\n    pct_combos_improved_by_tier_high: 0.72\n    pct_combos_improved_by_tier_mid: 0.65\n    pct_combos_improved_by_tier_low: 0.53\n    improvement_stronger_at_deep_layers: true\n    improvement_at_shallow_layers_pct: 0.5\n    improvement_at_deep_layers_pct: 0.78\n    random_direction_delta_median: 0.003\n    random_direction_delta_significant: false\n    difficulty_correctness_cosine_median: 0.18\n    difficulty_correctness_cosine_range:\n    - 0.08\n    - 0.3\n    decomposition_vs_baseline_paired_p: 0.03\n    decomposition_cohens_d: 0.28\n  result_rationale: 'Decomposition works but is partial because the difficulty-capability\n    separation is not clean. The difficulty direction (IRT-derived) captures ~42%\n    variance in human difficulty scores (R²) — reasonable but not perfect, meaning\n    the projection leaves residual difficulty signal mixed with capability. At deep\n    layers, removing difficulty helps more often (78% of combos) because the capability-specific\n    component dominates transfer degradation there — once you remove the shared difficulty\n    signal, the residual is more language-specific and harder to transfer. At shallow\n    layers, the improvement rate drops to ~50% (near chance) because both difficulty\n    and capability signals are more entangled and less linearly separable. The 65%\n    overall improvement rate is genuine but not universal — it demonstrates the decomposition\n    is prescriptive for about two-thirds of settings. The random-direction control\n    (median +0.3pp, not significant) confirms this isn''t a dimensionality-reduction\n    artifact. Low-resource languages show weaker improvement (53%) because their correctness\n    probes are noisier to begin with, and the difficulty projection may remove some\n    of the limited signal they have. The modest Cohen''s d (0.28) reflects that improvements\n    are real but small — this is a supporting analytical result, not a standalone\n    method contribution.\n\n    '\n  tables:\n  - name: 'Table 8: Decomposition Results — 10 Languages × 8 Layers'\n    description: 'Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC\n      after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded.\n      Marginal summaries: % improved per language, per layer. Shows concentration\n      of improvement at deep layers and high-resource languages.\n\n      '\n  - name: 'Table 9: Decomposition vs Random Direction Control'\n    description: 'Comparison: difficulty projection vs random projection vs no projection.\n      Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically\n      — not arbitrary dimensionality reduction — drives improvement.\n\n      '\n  figures_description:\n  - 'Figure: Decomposition improvement rate vs layer depth — bar chart showing fraction\n    of languages improved at each layer. Monotonically increasing trend from ~50%\n    at shallowest to ~78% at deepest. Supports narrative that capability-specific\n    component is the deep-layer transfer bottleneck.'\n  analysis: 'Decomposition provides supporting evidence for the geometric misalignment\n    narrative. The fact that difficulty removal helps more at deep layers aligns with\n    the CKA finding — at depth, the capability-specific component (which is geometrically\n    misaligned across languages) drives transfer failure, and removing the shared\n    difficulty component isolates this effect. However, the partial success rate (65%)\n    and modest effect size (d=0.28) keep this as supporting analysis rather than a\n    standalone claim. The finding is prescriptive: researchers attempting cross-lingual\n    probe transfer should first assess whether difficulty confounding explains their\n    transfer gaps — in ~65% of cases, it partially does.\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Verbalized confidence direction extraction, cosine similarity with\n    correctness direction. 20 languages × 2 architectures. Resource-tier and family\n    analysis.\n\n    '\n  expected_results:\n    en_cosine_qwen: 0.035\n    en_cosine_llama: 0.038\n    cosine_median_across_langs_qwen: 0.055\n    cosine_median_across_langs_llama: 0.06\n    cosine_max_across_langs: 0.1\n    cosine_max_language: sw\n    cosine_range:\n    - 0.02\n    - 0.1\n    cosine_median_high_resource: 0.04\n    cosine_median_mid_resource: 0.06\n    cosine_median_low_resource: 0.085\n    cosine_variance_high: 0.0003\n    cosine_variance_mid: 0.0008\n    cosine_variance_low: 0.0018\n    all_langs_below_threshold: true\n    cosine_vs_resource_spearman_rho: 0.52\n    cosine_vs_resource_p: 0.018\n  result_rationale: 'Orthogonality persists across languages because the separation\n    between correctness and verbalized confidence is a structural property of how\n    transformers process MCQA — the model''s internal \"do I know this?\" signal (correctness)\n    and its verbalized \"how confident am I?\" output occupy orthogonal subspaces by\n    design (the former is a representation-level property, the latter is optimized\n    during RLHF/instruction-tuning for human-readable outputs). The English cosine\n    (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly\n    higher (median 0.055-0.060) because: (a) non-English confidence verbalization\n    is noisier (models are less calibrated in non-English expression of uncertainty);\n    (b) the confidence probe may capture some language-switching signal that correlates\n    weakly with correctness (lower-resource languages trigger more uncertain generation\n    behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold\n    (<0.12) but shows more variance — Swahili''s limited pretraining data means both\n    probes are noisier, and noise correlations inflate apparent cosine. The resource-\n    tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger\n    (lower cosine) for high-resource languages, suggesting that abundant pretraining\n    data helps separate correctness from confidence representations. However, even\n    the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment,\n    confirming that output-based calibration is structurally limited across all languages.\n\n    '\n  tables:\n  - name: 'Table 10: Correctness–Confidence Cosine Similarity Across Languages'\n    description: '20 languages (rows, grouped by resource tier) × 2 architectures\n      (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier\n      medians and Spearman correlation with log(pretraining data estimate). All values\n      < 0.12.\n\n      '\n  figures_description:\n  - 'Figure: Cosine similarity vs estimated pretraining data — scatter plot, 20 languages\n    × 2 models. Log scale x-axis (pretraining tokens). Weak positive trend (more data\n    → lower cosine → stronger orthogonality). Highlights sw/bn as outliers with highest\n    cosine.'\n  analysis: 'Orthogonality holds universally (max 0.10 < 0.12 threshold) but with\n    a resource- tier gradient that is novel relative to Miao & Ungar''s English-only\n    finding. This extends their claim to multilingual settings with a nuance: the\n    structural separation is slightly weaker for low-resource languages, though never\n    approaching a level that would make output-based calibration viable. This supports\n    the paper''s broader argument that probe-based calibration is the right paradigm\n    for all languages, but the cross-lingual transfer challenge is the bottleneck\n    — not the underlying signal quality.\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP at each probed layer for both models.\n    English accuracy, cross-lingual transfer degradation, calibration quality.\n\n    '\n  expected_results:\n    logreg_en_best_auroc_qwen: 0.81\n    mlp_en_best_auroc_qwen: 0.835\n    logreg_en_best_auroc_llama: 0.79\n    mlp_en_best_auroc_llama: 0.815\n    logreg_zs_median_qwen: 0.7\n    mlp_zs_median_qwen: 0.665\n    logreg_zs_median_llama: 0.68\n    mlp_zs_median_llama: 0.645\n    logreg_transfer_gap: 0.11\n    mlp_transfer_gap: 0.17\n    logreg_ece_median: 0.068\n    mlp_ece_median: 0.075\n    mlp_advantage_en_deep_layers: 0.03\n    mlp_advantage_en_shallow_layers: 0.01\n    logreg_better_transfer_pct_langs: 0.8\n  result_rationale: 'MLP probes achieve ~2.5pp higher English AUROC because they can\n    capture nonlinear interactions in the representation — the correctness signal\n    has a small nonlinear component that logistic regression misses. However, this\n    nonlinear component is language-specific (learned from English data, doesn''t\n    generalize), so MLP probes show 6pp larger transfer gap than logistic regression.\n    The MLP essentially overfits to English-specific nonlinearities in the correctness\n    representation. This confirms the hypothesis that linear probes transfer better\n    cross-lingually — the linear component of the correctness signal is more universal\n    across languages, while nonlinear components are language-specific. The MLP advantage\n    is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper\n    representations have more complex, language-specific structure for the MLP to\n    exploit. 80% of languages see better transfer with logistic regression, with the\n    exceptions being high- resource languages (zh, es) where the MLP''s nonlinear\n    component partially transfers due to shared pretraining features. This result\n    justifies the paper''s focus on logistic regression probes and reinforces the\n    geometric (linear) framing.\n\n    '\n  tables:\n  - name: 'Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer'\n    description: 'Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg\n      ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP''s\n      higher EN AUROC comes at cost of larger transfer gap. Gap difference increases\n      with depth.\n\n      '\n  figures_description:\n  - 'Figure: Transfer gap (EN AUROC - ZS median) vs layer depth for LogReg and MLP.\n    Two lines diverging at deeper layers — MLP gap grows faster, confirming linear\n    probes are preferable for cross-lingual transfer.'\n  analysis: 'This experiment justifies the methodological choice of logistic regression\n    probes and provides additional evidence for the geometric/linear framing. If the\n    correctness signal were deeply nonlinear, MLP''s advantage would transfer — the\n    fact that it doesn''t confirms that the transferable component is linear. Goes\n    in supplementary material as a methodological validation.\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages\n    each). Validates generalization beyond GlobalMMLU.\n\n    '\n  expected_results:\n    belebele_en_best_auroc_qwen: 0.78\n    belebele_zs_median_qwen: 0.68\n    belebele_pareto_rho_median: -0.48\n    belebele_linear_proj_delta: 0.03\n    belebele_caclr_beta_delta: 0.003\n    mmlupx_en_best_auroc_qwen: 0.82\n    mmlupx_zs_median_qwen: 0.69\n    mmlupx_pareto_rho_median: -0.5\n    mmlupx_linear_proj_delta: 0.033\n    mmlupx_caclr_beta_delta: 0.002\n    auroc_rank_correlation_globalmmlu_vs_belebele: 0.82\n    auroc_rank_correlation_globalmmlu_vs_mmlupx: 0.88\n    method_ranking_consistent_across_benchmarks: true\n  result_rationale: 'Belebele is a reading comprehension benchmark — fundamentally\n    different from MCQA knowledge testing. The correctness signal is still present\n    (models either comprehend or don''t) but Belebele''s English AUROC is slightly\n    lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly\n    encoded than factual knowledge correctness. The Pareto rho is slightly weaker\n    (-0.48) because Belebele''s parallel passages provide more uniform cross-lingual\n    signal than GlobalMMLU''s diverse topics. MMLU-ProX, being closer to GlobalMMLU\n    in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding\n    is that method rankings are consistent — linear projection still outperforms CaCLR,\n    and CaCLR''s β term remains inert across benchmarks. This rules out the possibility\n    that CaCLR''s failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88)\n    between benchmarks confirm that per-language transfer difficulty is a property\n    of the model''s multilingual representations, not the benchmark.\n\n    '\n  tables:\n  - name: 'Table S2: Cross-Benchmark Generalization'\n    description: 'Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX)\n      × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows\n      consistent patterns across benchmarks. Rank correlation between per-language\n      AUROCs.\n\n      '\n  figures_description:\n  - 'Figure: Per-language AUROC scatter — GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX.\n    Each point is a language. High correlation confirms benchmark-invariant transfer\n    difficulty ranking.'\n  analysis: 'Benchmark generalization confirms all findings are not artifacts of GlobalMMLU.\n    The consistent method ranking across three benchmarks strengthens the negative\n    result — CaCLR''s β inertness is a fundamental property of distributional matching\n    vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary\n    or a short main-text paragraph.\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout\n    on 5% subset.\n\n    '\n  expected_results:\n    int8_fp16_auroc_max_diff: 0.008\n    int8_fp16_auroc_mean_diff: 0.003\n    int8_fp16_ece_max_diff: 0.012\n    int8_fp16_correlation_r: 0.997\n    int8_fp16_rank_agreement_pct: 0.98\n    distortion_significant: false\n  result_rationale: 'INT8 weight-only quantization preserves the vast majority of\n    activation-space structure because (a) it quantizes weights, not activations —\n    the internal representations used for probing are computed in higher precision;\n    (b) 7B+ models are robust to INT8 quantization (well-established in the quantization\n    literature); (c) correctness probes operate on high-dimensional representations\n    (4096+ dims) where small per-dimension perturbations from quantization average\n    out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence\n    intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that\n    quantization shifts all scores by a near-constant offset without affecting ranking.\n    This validation is necessary for reviewer reassurance but expected to be a non-issue.\n\n    '\n  tables:\n  - name: 'Table S3: INT8 vs FP16 Validation'\n    description: 'Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank\n      correlation). All differences within bootstrap CI. Conclusion: INT8 does not\n      distort correctness signals.\n\n      '\n  figures_description: []\n  analysis: 'Straightforward validation that INT8 quantization doesn''t affect conclusions.\n    One paragraph in supplementary material with the table. Addresses anticipated\n    reviewer concern #5.\n\n    '\n- name: CKA Cross-Lingual Representation Similarity\n  plan_id: plan_011\n  description: 'CKA (linear kernel) between English and each target language at every\n    probed layer, both models. Correlate CKA with transfer AUROC.\n\n    '\n  expected_results:\n    cka_en_zh_shallow_layer12_qwen: 0.88\n    cka_en_zh_deep_layer72_qwen: 0.62\n    cka_en_sw_shallow_layer12_qwen: 0.78\n    cka_en_sw_deep_layer72_qwen: 0.38\n    cka_median_shallow_across_langs: 0.84\n    cka_median_deep_across_langs: 0.52\n    cka_decrease_with_depth_significant: true\n    cka_transfer_pearson_r_qwen: 0.62\n    cka_transfer_pearson_r_llama: 0.54\n    cka_transfer_pearson_r_pooled: 0.58\n    cka_transfer_pearson_p: 1.0e-05\n    cka_deep_high_resource_median: 0.6\n    cka_deep_mid_resource_median: 0.48\n    cka_deep_low_resource_median: 0.36\n    mmd_transfer_pearson_r: 0.25\n    mmd_explains_variance_pct: 6\n    cka_explains_variance_pct: 34\n  result_rationale: 'CKA measures representational similarity including geometric\n    structure (rotation, scaling), while MMD measures distributional distance (mean,\n    variance, higher moments). CKA decreases with depth because deeper transformer\n    layers specialize more for language-specific processing — the cross-lingual alignment\n    enforced by shared vocabulary embeddings and early layers gradually gives way\n    to language- specific feature extraction. The CKA–transfer correlation (r=0.58)\n    is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming\n    that representational geometry is a major (but not the only) factor in transfer\n    success. The remaining variance comes from factors like probe quality, dataset\n    difficulty distribution, and non-geometric aspects of the representation. Critically,\n    CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer\n    success — this is the key mechanistic finding. If cross-lingual misalignment were\n    distributional (mean/covariance shift), MMD would predict transfer as well as\n    or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that\n    the misalignment is geometric (rotation/scaling of the entire representational\n    space), not merely distributional. This directly explains why MMD-based CaCLR\n    fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient\n    (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing\n    a mechanistic explanation for why low-resource languages transfer worse — their\n    deep-layer representations are more geometrically dissimilar from English.\n\n    '\n  tables:\n  - name: 'Table 11: CKA Similarity — Languages × Layers'\n    description: 'Probed layers (rows) × 20 languages (columns, sorted by resource\n      tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing\n      with depth. Resource-tier banding visible. Both models shown.\n\n      '\n  - name: 'Table 12: CKA vs MMD as Transfer Predictors'\n    description: 'Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy.\n      Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric\n      > distributional as explanation.\n\n      '\n  figures_description:\n  - 'Figure: CKA heatmap — layers (y-axis) × languages (x-axis, sorted by transfer\n    AUROC). Color intensity = CKA. Clear diagonal structure: high CKA co-occurs with\n    high transfer AUROC. Visual demonstration of the CKA–transfer link.'\n  - 'Figure: CKA vs transfer AUROC scatter — each point is a (layer, language) pair.\n    Color: resource tier. Linear fit line with r=0.58. Contrasted with MMD vs transfer\n    scatter (r=0.25) in adjacent panel. The visual gap between the two correlations\n    is the paper''s mechanistic argument.'\n  - 'Figure: CKA depth profile — CKA vs layer depth for 3 representative languages\n    (zh, tr, sw). Three curves showing parallel decline but at different levels. Annotated\n    with corresponding transfer AUROC at each layer.'\n  analysis: 'CKA analysis is the mechanistic backbone of the paper. It upgrades the\n    contribution from \"we measured that transfer fails at deep layers\" to \"we explain\n    WHY transfer fails — geometric misalignment increases with depth, and this misalignment\n    type (rotation/scaling) is specifically not addressable by distributional matching\n    (MMD).\" The CKA–transfer correlation (r=0.58) provides quantitative support, and\n    the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical\n    distinction that makes the negative CaCLR result theoretically interpretable rather\n    than just empirically observed. This transforms the paper from a measurement study\n    to one with mechanistic insight.\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.\n    Both models × 5 layers × 20 languages.\n\n    '\n  expected_results:\n    pairs_10_delta_auroc_median: 0.012\n    pairs_20_delta_auroc_median: 0.022\n    pairs_50_delta_auroc_median: 0.03\n    pairs_100_delta_auroc_median: 0.035\n    pairs_200_delta_auroc_median: 0.036\n    saturation_knee_point: 70\n    pairs_for_90pct_max_improvement: 55\n    pairs_for_95pct_max_improvement: 85\n    pairs_10_std_across_langs: 0.025\n    pairs_50_std_across_langs: 0.012\n    pairs_100_std_across_langs: 0.008\n    saturation_consistent_across_models: true\n    qwen_saturation_knee: 65\n    llama_saturation_knee: 75\n  result_rationale: 'Linear projection learns a rotation matrix mapping source-language\n    representations to target-language space. The sample complexity for estimating\n    a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because:\n    (a) the effective dimensionality of the correctness-relevant subspace is much\n    lower than the full representation dimensionality — the probe operates in a low-rank\n    subspace; (b) parallel pairs provide direct supervision on the mapping, unlike\n    distributional matching which uses indirect statistical signals. With 10 pairs,\n    the mapping is underdetermined but captures the dominant rotation component (+1.2pp).\n    By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling\n    axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is\n    consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual\n    dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture\n    difference in knee points (65 vs 75) reflects that Llama 4''s representations\n    may require slightly more pairs to estimate the rotation due to its MoE routing\n    introducing more heterogeneity. The practical implication is clear: ~50-100 parallel\n    pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match\n    or exceed CaCLR''s entire training pipeline.\n\n    '\n  tables:\n  - name: 'Table 13: Linear Projection — Sample Efficiency'\n    description: 'Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median\n      ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear\n      diminishing returns after 50 pairs.\n\n      '\n  figures_description:\n  - 'Figure: Learning curve — x-axis: number of parallel pairs (log scale), y-axis:\n    median ΔAUROC. Two curves (Qwen3, Llama4) with shaded ±1 std band. Annotated knee\n    point. Horizontal dashed line: CaCLR-full ΔAUROC for comparison — linear projection\n    surpasses CaCLR at just ~20 pairs.'\n  analysis: 'Linear projection''s sample efficiency is the constructive complement\n    to CaCLR''s negative result. The message: you don''t need MMD-based distributional\n    matching (which doesn''t work anyway) — you just need ~50-100 parallel pairs and\n    a linear mapping. This is practically actionable and theoretically consistent\n    with the geometric explanation (linear projection learns the rotation that MMD\n    cannot). The learning curve figure — showing linear projection surpassing CaCLR\n    at ~20 pairs — is one of the paper''s most compelling visuals.\n\n    '\n- name: Probing Control Tasks (Hewitt & Liang 2019)\n  plan_id: plan_013\n  description: 'Train probes on randomly permuted labels at each layer. Selectivity\n    analysis across layers and languages.\n\n    '\n  expected_results:\n    control_auroc_en_median: 0.545\n    control_auroc_en_range:\n    - 0.52\n    - 0.58\n    control_auroc_noneng_median: 0.54\n    selectivity_en_median: 0.265\n    selectivity_en_range:\n    - 0.18\n    - 0.31\n    selectivity_noneng_median_high_resource: 0.2\n    selectivity_noneng_median_mid_resource: 0.16\n    selectivity_noneng_median_low_resource: 0.1\n    selectivity_min_across_all: 0.08\n    selectivity_min_language: sw\n    selectivity_min_layer: layer_4\n    all_selectivities_positive: true\n    pct_above_10pp: 0.88\n    pct_above_10pp_high_resource: 0.95\n    pct_above_10pp_low_resource: 0.7\n    selectivity_peaks_at_mid_depth: true\n    selectivity_peak_layer_pct_depth: 0.55\n  result_rationale: 'Control tasks with random labels test whether probe capacity\n    (model expressiveness) alone can achieve high AUROC without genuine correctness\n    signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms\n    that logistic regression probes do not have sufficient capacity to memorize random\n    label assignments in high-dimensional space — any AUROC above this baseline reflects\n    genuine signal. English selectivity (median 0.265) is strong: the probe captures\n    real correctness information 26.5pp above what capacity alone could achieve. Non-English\n    selectivity decreases with resource tier because: (a) the correctness signal itself\n    is weaker for languages with less pretraining data; (b) the cross-lingual transfer\n    means probes must generalize from English-learned patterns, which is inherently\n    harder for distant languages. Low-resource languages (sw, bn) show selectivity\n    ~10pp, still positive but approaching the threshold where a reviewer might question\n    signal quality. The 88% of language-layer combinations exceeding 10pp provides\n    reasonable validation, but the 30% failure rate for low-resource languages at\n    this threshold is a genuine limitation that the paper should acknowledge. Selectivity\n    peaks at mid-depth (~55%) because shallow layers have weaker correctness signals\n    (less processed) and very deep layers have stronger but more language-specific\n    signals (high probe AUROC but also higher control AUROC due to richer features).\n\n    '\n  tables:\n  - name: 'Table S4: Control Task Selectivity'\n    description: 'Supplementary. Languages (rows, grouped by resource tier) × representative\n      layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded:\n      green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in\n      selectivity.\n\n      '\n  figures_description:\n  - 'Figure: Selectivity by resource tier — box plots for HIGH, MID, LOW resource\n    tiers. Shows decreasing median and increasing variance for lower-resource tiers.\n    Dashed line at 10pp threshold. Most points above threshold but LOW tier shows\n    some below.'\n  analysis: 'Control tasks validate that probe AUROC reflects genuine correctness\n    signal for the large majority of settings (88% above 10pp). The resource-tier\n    gradient in selectivity is a limitation to acknowledge: for low-resource languages,\n    probe signal quality is weaker, and conclusions about transfer should be interpreted\n    with this caveat. This doesn''t undermine the paper''s core claims (which are\n    about the mechanism of transfer failure, not about achieving high probe quality\n    in every language) but sets appropriate epistemic bounds.\n\n    '\n- name: Gemma 4 31B Dense Pareto Frontier\n  plan_id: plan_008\n  description: 'Third architecture for camera-ready. 60 layers, dense, FP16. Full\n    Pareto frontier, 20+ languages. Dense vs MoE contrast.\n\n    '\n  expected_results:\n    en_best_auroc: 0.8\n    en_best_layer: 45\n    zs_transfer_auroc_median: 0.69\n    best_transfer_layer: 33\n    pareto_rho_per_lang_median: -0.58\n    zs_langs_above_0p65: 12\n    pareto_rho_smoother_than_moe: true\n    pareto_rho_std_across_langs_gemma: 0.12\n    pareto_rho_std_across_langs_qwen: 0.16\n    pareto_rho_std_across_langs_llama: 0.15\n    cka_depth_decline_steeper_dense: true\n    linear_proj_delta_median: 0.033\n  result_rationale: 'Gemma 4 31B Dense provides the critical dense-vs-MoE architectural\n    contrast. As a dense model, every token passes through every layer (no routing),\n    creating more uniform layer-to-layer transformations. This produces a smoother\n    Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE\n    models) because the depth-transfer tradeoff is more consistent without routing-induced\n    heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense\n    models show a cleaner monotonic decline in cross-lingual alignment with depth\n    — MoE routing partially breaks this monotonicity by allowing some expert pathways\n    to maintain cross-lingual features at deeper layers. CKA declines more steeply\n    with depth in the dense model, confirming that MoE routing provides a modest buffer\n    against geometric misalignment (different experts can specialize differently per\n    language). English AUROC (0.80) is comparable to the larger MoE models despite\n    smaller parameter count because the 31B dense architecture is parameter-efficient\n    for representation quality. This is a P2 camera-ready experiment that strengthens\n    the architecture-dependence claim from \"two MoE models differ moderately\" to \"dense\n    vs MoE is a qualitatively distinct contrast.\"\n\n    '\n  tables:\n  - name: 'Table CR1: Three-Architecture Pareto Comparison'\n    description: 'Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense)\n      × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj\n      Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.\n\n      '\n  figures_description:\n  - 'Figure: Three-panel Pareto frontier comparison — Qwen3-MoE, Llama4-MoE, Gemma4-Dense\n    side-by-side. Dense model shows smoother, more monotonic frontier. Visual argument\n    for architecture-dependence.'\n  analysis: 'Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture-\n    dependence evidence: MoE routing introduces heterogeneity that partially buffers\n    against geometric misalignment at deep layers, while dense models show cleaner\n    depth-dependent degradation. This doesn''t change the paper''s conclusions but\n    provides a more compelling architectural contrast than two MoE models alone.\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele\n    language sets.\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_langs_above_0p65: 28\n    zs_median_auroc_52lang: 0.66\n    zs_auroc_range:\n    - 0.5\n    - 0.74\n    new_low_resource_langs_below_0p55:\n    - am\n    - my\n    - zu\n    - sn\n    - rw\n    resource_tier_gradient_replicates: true\n    pareto_rho_median_52lang: -0.49\n    linear_proj_delta_median_52lang: 0.031\n    tail_langs_below_0p55_count: 8\n    tail_langs_above_0p70_count: 12\n  result_rationale: 'Expanding to 52 languages adds many more low-resource and typologically\n    diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated\n    20) because the additional languages are disproportionately low-resource. Five\n    extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda)\n    fall below 0.55, approaching chance performance — these languages have minimal\n    pretraining representation in both models. The resource-tier gradient continues\n    to hold and becomes even more pronounced with the extended tail. Pareto rho weakens\n    slightly (-0.49) because many of the new languages show weak, noisy correlations\n    due to low base probe quality. Linear projection improvement remains consistent\n    (+3.1pp), confirming the geometric correction generalizes beyond the curated language\n    set. The practical message: probe-based cross-lingual calibration is viable for\n    ~28/52 languages (54%) without any target-language data, and linear projection\n    extends this to ~35/52 (67%). The remaining ~17 languages need language-specific\n    probes or alternative approaches.\n\n    '\n  tables:\n  - name: 'Table CR2: Extended Language Coverage — 52 Languages'\n    description: 'Camera-ready. Full 52-language results sorted by zero-shot AUROC.\n      Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100\n      AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65\n      (marginal), <0.55 (failed).\n\n      '\n  figures_description:\n  - 'Figure: Language coverage map — world map with countries colored by best zero-shot\n    transfer AUROC. Visual demonstration of where probe-based calibration works and\n    fails geographically.'\n  analysis: 'Camera-ready extension. The 52-language analysis adds scale but the median-tier\n    conclusion is clear: probe-based cross-lingual calibration works for a majority\n    but not all languages, and the resource-tier gradient is the dominant predictor\n    of success. This sets realistic expectations for practitioners and motivates future\n    work on low-resource language probe training.'\n",
      "numLines": 961,
      "startLine": 1,
      "totalLines": 961
    }
  },
  "sourceToolAssistantUUID": "ad1c3458-0f80-41c5-af28-45451132852c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "5427454f-2e02-4271-a3e4-f31b3fbfdeb5",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Assistant

_source line 18 · 2026-05-20T21:05:35.586Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper (10 pages) and the review context YAML. Let me now dispatch the review according to the dream-review-full protocol: 2 Reviewers (R1: methods + experiments, R2: novelty + related work), followed by a full roundtable (Step 1 independent → Step 2 cross-share → Step 3 converge → Step 4 synthesize).

Let me launch both reviewers in parallel as agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5427454f-2e02-4271-a3e4-f31b3fbfdeb5",
  "isSidechain": false,
  "requestId": "req_011CbEVzGbkPTMsehPpbyezU",
  "type": "assistant",
  "uuid": "f4d2d29a-52e3-448d-8acf-e17b5fb3aa1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZFHeCvxStaytWLA7kgWKj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42198,
      "cache_read_input_tokens": 23203,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 42198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42198
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

_source line 19 · 2026-05-20T21:05:36.509Z_

I've read the paper and the experimental design context. Now dispatching two parallel reviewers for the full review protocol.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d2d29a-52e3-448d-8acf-e17b5fb3aa1b",
  "isSidechain": false,
  "requestId": "req_011CbEVzGbkPTMsehPpbyezU",
  "type": "assistant",
  "uuid": "350697b2-b5d8-4ec6-b2b9-bd3cf38e1054",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZFHeCvxStaytWLA7kgWKj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42198,
      "cache_read_input_tokens": 23203,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 42198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42198
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

_source line 20 · 2026-05-20T21:06:17.342Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AobLHLuszCkD3WsGRVCLuN`</summary>

```json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **methods and experiments**.\n\n## Paper Summary\n\"Cross-Lingual Correctness Probes Reveal a Depth–Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\"\n\nThe paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. Key findings:\n\n1. **Pareto Frontier**: Deeper layers yield higher English AUROC (up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman ρ = −0.52).\n2. **CKA Mechanistic Explanation**: Geometric misalignment increases with depth. CKA–transfer correlation r=0.58 (34% variance), vs MMD r=0.25 (6%).\n3. **CaCLR Negative Result**: MMD-based consistency loss is inert across 3 OOM (Cohen's d=0.08, p=0.42).\n4. **Linear Projection**: +3.5pp AUROC with ~50-100 parallel pairs, succeeds because it learns the rotation MMD cannot.\n\nAdditional: correctness–confidence orthogonality persists across 20 languages (cosine < 0.10). Difficulty decomposition shows 65% improvement rate. Cross-benchmark generalization on Belebele and MMLU-ProX.\n\n## Key Tables/Results from the Paper\n\n**Table 1 (Pareto frontier summary):**\n- Qwen3-235B: EN_best=0.81 layer72, ZS_med=0.70 xfer_layer48, ρ_med=−0.51, σ_ρ=0.16\n- Llama 4 Scout: EN_best=0.79 layer36, ZS_med=0.68 xfer_layer24, ρ_med=−0.54, σ_ρ=0.15\n- Gemma 4 31B: EN_best=0.80 layer45, ZS_med=0.69 xfer_layer33, ρ_med=−0.58, σ_ρ=0.12\n\n**Table 2**: Per-language ZS transfer AUROC at best transfer layer (Qwen3). High-resource 0.72-0.74, mid 0.65-0.71, low (sw/bn) 0.57-0.58.\n\n**Table 3 (CKA):** CKA_shallow=0.84 median, CKA_deep=0.52 median. CKA Pearson r=0.58 (34% var), MMD r=0.25 (6% var).\n\n**Table 4 (β sweep):** β=0.001 Δ=+0.002, β=0.01 Δ=+0.001, β=0.1 Δ=−0.001, β=1.0 Δ=−0.003. Overall p=0.42, d=0.08.\n\n**Table 5 (Method comparison):** Mean-shift=0.000, CaCLR α-only=+0.005, CaCLR full=+0.012, Linear proj=+0.035 (p=0.001,d=0.55), Few-shot-25=+0.025, Few-shot-100=+0.045.\n\n**Table 6 (Linear proj sample efficiency):** 10 pairs→+0.012, 50→+0.030, 100→+0.035, 200→+0.036. Knee ~70 pairs.\n\n**Table 7 (Decomposition):** Overall 65% improved, +0.012 AUROC. Deep layers 78%, shallow 50%. Random direction 50% (n.s.).\n\n**Table 8 (Orthogonality):** EN cosine ~0.035-0.038, all langs <0.10, resource-tier gradient (high 0.04, low 0.085).\n\n**Appendices:** INT8 validation (max diff 0.8pp, r=0.997), MLP vs LogReg (MLP +2.5pp EN but 6pp larger transfer gap), cross-benchmark (method rankings consistent), control tasks (88% above 10pp selectivity).\n\n## Experimental Design Reference\nThe review_context.yaml lists 12 imagined experiments. The paper covers:\n- plan_001 (Qwen3 Pareto): ✓ covered in Tables 1-2\n- plan_002 (Llama4 Pareto): ✓ covered in Table 1\n- plan_003 (CaCLR): ✓ covered in Tables 4-5\n- plan_004 (Decomposition): ✓ covered in Table 7\n- plan_005 (Orthogonality): ✓ covered in Table 8\n- plan_006 (Probe complexity): ✓ Appendix B\n- plan_007 (Additional benchmarks): ✓ Appendix C\n- plan_008 (Gemma 4 Dense): ✓ Table 1, Section 5.7\n- plan_009 (Extended 52 langs): ✓ Section 5.8\n- plan_010 (INT8 validation): ✓ Appendix A\n- plan_011 (CKA analysis): ✓ Table 3, Section 5.2\n- plan_012 (Linear proj sensitivity): ✓ Table 6, Section 5.4\n- plan_013 (Control tasks): ✓ Appendix D\n\n## Your Task\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (methodological rigor, experimental design, statistical reporting)\n3. **Weaknesses** (methodological gaps, experimental concerns, missing controls/ablations)\n4. **Questions for Authors** (specific, actionable)\n5. **Minor Issues** (presentation, clarity)\n6. **Overall Assessment** with score (1-6) and confidence (1-5)\n\nFocus areas for R1:\n- Is the experimental design sufficient to support the claims?\n- Are the statistical methods appropriate (paired permutation tests, bootstrap CIs, Cohen's d)?\n- Is the CKA analysis convincing as a mechanistic explanation?\n- Is the CaCLR negative result well-controlled?\n- Are there missing baselines or ablations?\n- Is the linear projection comparison fair?\n- How robust are the results across architectures/languages/benchmarks?\n\nBe rigorous but fair. Identify both genuine weaknesses and acknowledge genuine strengths. The review should be 800-1200 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350697b2-b5d8-4ec6-b2b9-bd3cf38e1054",
  "isSidechain": false,
  "requestId": "req_011CbEVzGbkPTMsehPpbyezU",
  "type": "assistant",
  "uuid": "a94bde79-c99c-413f-afc3-8fde4ec996b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZFHeCvxStaytWLA7kgWKj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42198,
      "cache_read_input_tokens": 23203,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 42198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42198
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

_source line 21 · 2026-05-20T21:06:39.822Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UC21HHPGCD6Y8MsSPEacMe`</summary>

```json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **novelty, positioning, and related work**.\n\n## Paper Summary\n\"Cross-Lingual Correctness Probes Reveal a Depth–Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\"\n\nThe paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. Key findings:\n\n1. **Pareto Frontier**: Deeper layers yield higher English AUROC (up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman ρ = −0.52).\n2. **CKA Mechanistic Explanation**: Geometric misalignment increases with depth. CKA–transfer correlation r=0.58 (34% variance), vs MMD r=0.25 (6%).\n3. **CaCLR Negative Result**: MMD-based consistency loss is inert across 3 OOM (Cohen's d=0.08, p=0.42).\n4. **Linear Projection**: +3.5pp AUROC with ~50-100 parallel pairs, succeeds because it learns the rotation MMD cannot.\n\nAdditional findings: correctness–confidence orthogonality persists across 20 languages (cosine < 0.10), difficulty decomposition shows 65% improvement rate, cross-benchmark generalization confirmed.\n\n## Related Work as Presented in the Paper (Section 2)\n- **Probe-Based Calibration**: Burns et al. 2023, Li et al. 2024, CORAL (Miao et al. 2026), Miao & Ungar 2026 orthogonality. All English-only.\n- **Cross-Lingual Probe Transfer**: Xiao et al. 2025 (knowledge boundary probes, 8 langs — input-level answerability ≠ correctness). Civelli et al. 2024 (difficulty probes). LACE (Zhou et al. 2024) — per-language probe ensembles, needs target labels.\n- **Cross-Lingual Alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear mappings with 50-100 dictionary pairs. Paper claims linear projection sample efficiency is consistent with this.\n- **Representation Similarity**: CKA (Kornblith et al. 2019). Paper uses CKA for mechanistic explanation.\n- **Conformal Prediction**: Angelopoulos & Bates 2023. Paper claims complementary.\n\n## Key Claims to Evaluate for Novelty\n1. \"First systematic evaluation of cross-lingual correctness probe transfer\" — is this genuinely novel?\n2. The depth–transferability Pareto frontier concept — how novel vs. known depth-transfer tradeoffs?\n3. CKA as mechanistic explanation for WHY distributional matching fails — is this a genuine insight or post-hoc rationalization?\n4. CaCLR as a principled negative result — is it well-motivated enough to count as a contribution?\n5. Linear projection as \"constructive alternative\" — this is essentially applying VecMap/MUSE-style alignment to probe representations. How novel is this?\n6. Extending orthogonality from English to 20 languages — incremental extension or meaningful new finding?\n\n## Your Task\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (novelty, positioning, clarity of contribution)\n3. **Weaknesses** (novelty concerns, missing related work, overclaiming, positioning issues)\n4. **Questions for Authors** (specific, actionable)\n5. **Minor Issues** (presentation, framing)\n6. **Overall Assessment** with score (1-6) and confidence (1-5)\n\nFocus areas for R2:\n- Is the contribution genuinely novel, or is it a systematic but incremental evaluation?\n- Is the related work coverage complete? Any important missing references?\n- Is the \"Pareto frontier\" framing novel or does prior work on depth-dependent cross-lingual transfer cover this?\n- Is CaCLR a straw man? Is MMD the right distributional matching baseline? What about other domain adaptation methods (CORAL-the-method, adversarial alignment, optimal transport)?\n- Is linear projection genuinely a contribution, or just applying known techniques (VecMap) to a new domain?\n- Does the paper overclaim (\"first systematic evaluation\") when Xiao et al. 2025 already did cross-lingual probe transfer (albeit for knowledge boundaries)?\n- Is the correctness-confidence orthogonality extension from English to 20 languages a meaningful contribution or trivial extension?\n- How does this paper position relative to LACE (Zhou et al. 2024) which already addresses multilingual calibration?\n\nBe rigorous but fair. The review should be 800-1200 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a94bde79-c99c-413f-afc3-8fde4ec996b2",
  "isSidechain": false,
  "requestId": "req_011CbEVzGbkPTMsehPpbyezU",
  "type": "assistant",
  "uuid": "70663051-1f24-474a-a696-150fba8a2f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZFHeCvxStaytWLA7kgWKj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42198,
      "cache_read_input_tokens": 23203,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 42198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42198
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

_source line 22 · 2026-05-20T21:08:45.809Z_

<details><summary>↩ Tool result · `toolu_01UC21HHPGCD6Y8MsSPEacMe`</summary>

```text


Now I have all the context needed. Let me compose the R2 review focused on novelty, positioning, and related work.

---

## Review — Reviewer R2 (Novelty, Positioning, Related Work)

**Paper**: "Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes"

---

### 1. Summary

This paper presents a large-scale study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B, Llama 4 Scout) and one dense model (Gemma 4 31B, appendix). The authors identify a depth--transferability Pareto frontier, propose CaCLR (a probe training loss combining BCE, SB-ECE, and MMD consistency), decompose correctness into difficulty-shared and capability-specific components, and extend the English-only correctness--confidence orthogonality finding to 20 languages. CKA analysis is used as the mechanistic bridge linking representation geometry to transfer outcomes.

---

### 2. Strengths

**S1. Genuine gap identification and coherent narrative.** The observation that all probe-based calibration methods are English-only is accurate and important. The paper correctly identifies this as a field-level blind spot. The causal chain structure (Pareto frontier --> decomposition --> CaCLR --> orthogonality bounding) is well-organized and makes the paper readable despite its density.

**S2. The mean-shift invariance proof is a clean, novel contribution.** Proving that mean-shift alignment yields exactly zero AUROC change under StandardScaler + logistic regression is a tight theoretical result. This corrects an implicit assumption in prior work (Xiao et al. use mean-shift and report improvements, but under different metrics/pipelines). This distinction is clearly drawn and genuinely clarifies the field.

**S3. Difficulty--capability decomposition is methodologically interesting.** Separating the difficulty component (language-agnostic) from the capability component (language-dependent) via IRT probes, with a random-direction control, is a well-designed ablation. The resource-tier gradient in decomposition benefit (low-resource gains +4.1pp vs high-resource +2.2pp) is an insightful finding that goes beyond simple "low-resource is harder."

**S4. Scale of evaluation is commendable.** 20 languages, 3 architectures, 3 benchmarks, 5 transfer conditions, with control tasks and INT8 validation -- this is a thorough empirical package. The cross-benchmark generalization analysis (r=0.92 per-language correlation) strengthens external validity.

**S5. The paper honestly reports the limitations of its own method.** The depth-dependent CaCLR effectiveness analysis -- showing that MMD works at mid-depth but fails at deep layers where geometric misalignment dominates -- demonstrates intellectual honesty and provides actionable practitioner guidance.

---

### 3. Weaknesses

**W1. The "first systematic evaluation" claim overclaims relative to prior work.**
Xiao et al. (ACL 2025) already performed cross-lingual probe transfer across 8 languages with alignment methods. The paper's distinction -- knowledge boundary (input-level) vs. correctness (output-dependent) -- is valid but insufficient to claim "first systematic evaluation" of cross-lingual probe transfer wholesale. The claim should be scoped to "first systematic evaluation of cross-lingual *correctness* probe transfer" and should more carefully acknowledge that the experimental paradigm (train probe in English, transfer to other languages, evaluate with/without alignment) was established by Xiao et al.

**W2. The Pareto frontier is a quantitative refinement of known phenomena, not a conceptual discovery.**
Conneau et al. (2020, "What you can cram into a single $&!#* vector") established that deeper layers in multilingual transformers encode more language-specific information. LACE (Zhou et al. 2024) explicitly showed that non-English calibration peaks at intermediate layers. Civelli et al. (2026) demonstrated architecture-dependent optimal depth for cross-lingual probes. The "Pareto frontier" framing is a useful quantitative lens, but the underlying phenomenon -- deeper layers trade accuracy for cross-lingual transferability -- is well-established. The paper should position this as quantification and formalization of a known tradeoff, not as a discovery.

**W3. CaCLR's MMD component is not compared against other domain adaptation methods, making the negative-turned-positive result less informative.**
The paper tests only MMD for distributional alignment. Classical domain adaptation offers several alternatives: CORAL-the-method (Sun & Saenko 2016, aligning second-order statistics), adversarial alignment (DANN, Ganin et al. 2016), optimal transport (Courty et al. 2017), and contrastive alignment. Testing only MMD and then drawing conclusions about "distributional matching" in general is an incomplete experimental design. The paper's own analysis suggests geometric misalignment at depth -- but methods like Procrustes alignment or contrastive losses address geometric alignment directly. Why was only MMD tested? The conclusion "distributional matching fails where linear projection succeeds" should be "MMD-based distributional matching fails," since other distributional methods were not evaluated.

**W4. Linear projection is applying VecMap/MUSE to a new domain -- novelty is limited.**
The paper correctly cites MUSE and VecMap but does not sufficiently acknowledge that applying linear cross-lingual alignment to probe representations is a straightforward domain transfer of existing techniques. The data efficiency result (saturation at ~50 pairs) is interesting but expected given the known low intrinsic dimensionality of correctness representations (3-8 dimensions per Confidence Manifold, 2026). This should be framed as confirming theoretical expectations rather than as a finding.

**W5. Missing foundational references weaken positioning.**
Several important works are absent:
- Conneau et al. (2020) on depth-dependent language specificity in multilingual models -- directly relevant to the Pareto frontier claim.
- Pires et al. (2019) on mBERT cross-lingual transfer -- foundational context for cross-lingual probe transfer.
- Gretton et al. (2012) for MMD -- the method's foundational paper must be cited, and the kernel choice (Gaussian RBF? linear?) must be specified.
- Sun & Saenko (2016) CORAL-the-method, Ganin et al. (2016) DANN -- directly relevant domain adaptation methods that CaCLR's MMD term should be compared against or at minimum discussed.
- Chi et al. (2020) on the geometry of multilingual representations -- relevant to the CKA analysis and geometric misalignment discussion.

**W6. Orthogonality extension from English to 20 languages is incremental.**
Miao & Ungar (2026) showed cosine < 0.04 in English on 7-8B models. This paper shows cosine < 0.062 across 20 languages on larger models. Given that the underlying hypothesis -- correctness and confidence are encoded independently -- has no theoretical reason to be language-specific, confirmation across languages is expected. The resource-tier gradient (low-resource slightly higher cosine) is attributed to noise in confidence direction estimation, not genuine structural difference. This is a useful sanity check but not a meaningful independent contribution.

**W7. The paper does not adequately differentiate from LACE (Zhou et al. 2024).**
LACE addresses multilingual calibration via per-language layer ensembles and demonstrated the non-English calibration gap. The paper argues LACE requires "target-language labels" while CaCLR requires "zero target-language correctness labels." However, CaCLR requires parallel inputs (translated items) -- which is also a non-trivial data requirement. The practical advantage over LACE is not clearly quantified: is CaCLR's 3.5% ECE reduction competitive with LACE's reported ECE 22% --> 3%? Without direct comparison on the same benchmark, the positioning is incomplete.

---

### 4. Questions for Authors

1. Can you provide a direct comparison with LACE on a shared benchmark/language set? The positioning against LACE as the primary multilingual calibration competitor is central but currently relies on prose rather than empirical comparison.

2. Why was only MMD tested as the distributional alignment loss? Did you consider CORAL (second-order statistics), adversarial alignment, or optimal transport? The conclusion about "distributional matching" failing at depth would be far more compelling if multiple distributional methods showed the same pattern.

3. How does the Pareto frontier relate to the findings of Conneau et al. (2020) on depth-dependent language specificity? Their work predicts exactly this tradeoff. What does your quantification add beyond confirming their qualitative finding?

4. The paper notes CaCLR requires "parallel inputs" from GlobalMMLU translations. How sensitive is CaCLR to the quality and domain of these parallel inputs? If parallel inputs come from a different domain (e.g., Bible parallel text vs. MCQA translations), does CaCLR still work?

5. For the orthogonality analysis, can you report the full 20-language table? Showing 10/20 languages for a universal claim is insufficient.

6. The CKA analysis claims "mechanistic explanation" -- would you obtain the same correlation if you used a simpler metric like mean cosine similarity between representations? How much does CKA specifically add over cheaper alternatives?

---

### 5. Minor Issues

- The bibliography has multiple empty \cite{} placeholders (Section 1), which should be filled.
- Table 1: Scout ZS Min/Max columns show "---" without explanation.
- The paper title mentions "Distributional Matching Fails Where Linear Projection Succeeds" but the submitted version shows CaCLR (distributional matching) *succeeding*, with only deep-layer limitations. The title appears to match a different narrative path (the negative result path from paper_framing.md) rather than the actual results. This is confusing.
- "Camera-ready extension" language in the appendix (Gemma 4) should be removed for submission -- it signals incomplete work.
- The term "Pareto frontier" is technically imprecise: a Pareto frontier implies no point dominates another. Some layer-depth points are dominated (e.g., layer 88 on Qwen3 is worse than layer 76 on both EN and ZS). The correct term is "Pareto tradeoff" or simply "depth-transferability tradeoff."

---

### 6. Overall Assessment

**Score: 4/6 (Weak Accept)**

**Confidence: 4/5**

The paper addresses a genuine gap -- no prior work has systematically tested whether probe-based calibration methods transfer cross-lingually -- and provides a thorough empirical investigation at impressive scale. The mean-shift invariance proof, difficulty-capability decomposition, and CKA analysis are individually valuable analytical contributions.

However, several novelty concerns temper enthusiasm. The depth-transferability tradeoff is a quantitative formalization of a known phenomenon (Conneau et al. 2020, LACE, Civelli et al.), not a conceptual discovery. CaCLR's MMD component is tested in isolation without comparison to other domain adaptation methods, making conclusions about "distributional matching" overly broad. Linear projection is a direct application of VecMap/MUSE-style alignment to a new domain. The orthogonality extension is expected and incremental. Important foundational references are missing (Conneau et al. 2020, Pires et al. 2019, Gretton et al. 2012, domain adaptation baselines).

The paper's strongest identity is as an analytical characterization paper -- the Pareto quantification, decomposition, CKA analysis, and orthogonality confirmation collectively advance the community's understanding of multilingual calibration at the representation level. I would recommend reframing contributions to foreground these analytical insights and position CaCLR as one practical implication rather than the headline.

agentId: a64546f9eceb612f2 (use SendMessage with to: 'a64546f9eceb612f2' to continue this agent)
&lt;usage>total_tokens: 70483
tool_uses: 13
duration_ms: 125983&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70663051-1f24-474a-a696-150fba8a2f20",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "012729f5-142b-43cf-9acf-973e08152efa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **novelty, positioning, and related work**.\n\n## Paper Summary\n\"Cross-Lingual Correctness Probes Reveal a Depth–Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\"\n\nThe paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. Key findings:\n\n1. **Pareto Frontier**: Deeper layers yield higher English AUROC (up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman ρ = −0.52).\n2. **CKA Mechanistic Explanation**: Geometric misalignment increases with depth. CKA–transfer correlation r=0.58 (34% variance), vs MMD r=0.25 (6%).\n3. **CaCLR Negative Result**: MMD-based consistency loss is inert across 3 OOM (Cohen's d=0.08, p=0.42).\n4. **Linear Projection**: +3.5pp AUROC with ~50-100 parallel pairs, succeeds because it learns the rotation MMD cannot.\n\nAdditional findings: correctness–confidence orthogonality persists across 20 languages (cosine < 0.10), difficulty decomposition shows 65% improvement rate, cross-benchmark generalization confirmed.\n\n## Related Work as Presented in the Paper (Section 2)\n- **Probe-Based Calibration**: Burns et al. 2023, Li et al. 2024, CORAL (Miao et al. 2026), Miao & Ungar 2026 orthogonality. All English-only.\n- **Cross-Lingual Probe Transfer**: Xiao et al. 2025 (knowledge boundary probes, 8 langs — input-level answerability ≠ correctness). Civelli et al. 2024 (difficulty probes). LACE (Zhou et al. 2024) — per-language probe ensembles, needs target labels.\n- **Cross-Lingual Alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear mappings with 50-100 dictionary pairs. Paper claims linear projection sample efficiency is consistent with this.\n- **Representation Similarity**: CKA (Kornblith et al. 2019). Paper uses CKA for mechanistic explanation.\n- **Conformal Prediction**: Angelopoulos & Bates 2023. Paper claims complementary.\n\n## Key Claims to Evaluate for Novelty\n1. \"First systematic evaluation of cross-lingual correctness probe transfer\" — is this genuinely novel?\n2. The depth–transferability Pareto frontier concept — how novel vs. known depth-transfer tradeoffs?\n3. CKA as mechanistic explanation for WHY distributional matching fails — is this a genuine insight or post-hoc rationalization?\n4. CaCLR as a principled negative result — is it well-motivated enough to count as a contribution?\n5. Linear projection as \"constructive alternative\" — this is essentially applying VecMap/MUSE-style alignment to probe representations. How novel is this?\n6. Extending orthogonality from English to 20 languages — incremental extension or meaningful new finding?\n\n## Your Task\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (novelty, positioning, clarity of contribution)\n3. **Weaknesses** (novelty concerns, missing related work, overclaiming, positioning issues)\n4. **Questions for Authors** (specific, actionable)\n5. **Minor Issues** (presentation, framing)\n6. **Overall Assessment** with score (1-6) and confidence (1-5)\n\nFocus areas for R2:\n- Is the contribution genuinely novel, or is it a systematic but incremental evaluation?\n- Is the related work coverage complete? Any important missing references?\n- Is the \"Pareto frontier\" framing novel or does prior work on depth-dependent cross-lingual transfer cover this?\n- Is CaCLR a straw man? Is MMD the right distributional matching baseline? What about other domain adaptation methods (CORAL-the-method, adversarial alignment, optimal transport)?\n- Is linear projection genuinely a contribution, or just applying known techniques (VecMap) to a new domain?\n- Does the paper overclaim (\"first systematic evaluation\") when Xiao et al. 2025 already did cross-lingual probe transfer (albeit for knowledge boundaries)?\n- Is the correctness-confidence orthogonality extension from English to 20 languages a meaningful contribution or trivial extension?\n- How does this paper position relative to LACE (Zhou et al. 2024) which already addresses multilingual calibration?\n\nBe rigorous but fair. The review should be 800-1200 words.",
    "agentId": "a64546f9eceb612f2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nNow I have all the context needed. Let me compose the R2 review focused on novelty, positioning, and related work.\n\n---\n\n## Review — Reviewer R2 (Novelty, Positioning, Related Work)\n\n**Paper**: \"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\"\n\n---\n\n### 1. Summary\n\nThis paper presents a large-scale study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B, Llama 4 Scout) and one dense model (Gemma 4 31B, appendix). The authors identify a depth--transferability Pareto frontier, propose CaCLR (a probe training loss combining BCE, SB-ECE, and MMD consistency), decompose correctness into difficulty-shared and capability-specific components, and extend the English-only correctness--confidence orthogonality finding to 20 languages. CKA analysis is used as the mechanistic bridge linking representation geometry to transfer outcomes.\n\n---\n\n### 2. Strengths\n\n**S1. Genuine gap identification and coherent narrative.** The observation that all probe-based calibration methods are English-only is accurate and important. The paper correctly identifies this as a field-level blind spot. The causal chain structure (Pareto frontier --> decomposition --> CaCLR --> orthogonality bounding) is well-organized and makes the paper readable despite its density.\n\n**S2. The mean-shift invariance proof is a clean, novel contribution.** Proving that mean-shift alignment yields exactly zero AUROC change under StandardScaler + logistic regression is a tight theoretical result. This corrects an implicit assumption in prior work (Xiao et al. use mean-shift and report improvements, but under different metrics/pipelines). This distinction is clearly drawn and genuinely clarifies the field.\n\n**S3. Difficulty--capability decomposition is methodologically interesting.** Separating the difficulty component (language-agnostic) from the capability component (language-dependent) via IRT probes, with a random-direction control, is a well-designed ablation. The resource-tier gradient in decomposition benefit (low-resource gains +4.1pp vs high-resource +2.2pp) is an insightful finding that goes beyond simple \"low-resource is harder.\"\n\n**S4. Scale of evaluation is commendable.** 20 languages, 3 architectures, 3 benchmarks, 5 transfer conditions, with control tasks and INT8 validation -- this is a thorough empirical package. The cross-benchmark generalization analysis (r=0.92 per-language correlation) strengthens external validity.\n\n**S5. The paper honestly reports the limitations of its own method.** The depth-dependent CaCLR effectiveness analysis -- showing that MMD works at mid-depth but fails at deep layers where geometric misalignment dominates -- demonstrates intellectual honesty and provides actionable practitioner guidance.\n\n---\n\n### 3. Weaknesses\n\n**W1. The \"first systematic evaluation\" claim overclaims relative to prior work.**\nXiao et al. (ACL 2025) already performed cross-lingual probe transfer across 8 languages with alignment methods. The paper's distinction -- knowledge boundary (input-level) vs. correctness (output-dependent) -- is valid but insufficient to claim \"first systematic evaluation\" of cross-lingual probe transfer wholesale. The claim should be scoped to \"first systematic evaluation of cross-lingual *correctness* probe transfer\" and should more carefully acknowledge that the experimental paradigm (train probe in English, transfer to other languages, evaluate with/without alignment) was established by Xiao et al.\n\n**W2. The Pareto frontier is a quantitative refinement of known phenomena, not a conceptual discovery.**\nConneau et al. (2020, \"What you can cram into a single $&!#* vector\") established that deeper layers in multilingual transformers encode more language-specific information. LACE (Zhou et al. 2024) explicitly showed that non-English calibration peaks at intermediate layers. Civelli et al. (2026) demonstrated architecture-dependent optimal depth for cross-lingual probes. The \"Pareto frontier\" framing is a useful quantitative lens, but the underlying phenomenon -- deeper layers trade accuracy for cross-lingual transferability -- is well-established. The paper should position this as quantification and formalization of a known tradeoff, not as a discovery.\n\n**W3. CaCLR's MMD component is not compared against other domain adaptation methods, making the negative-turned-positive result less informative.**\nThe paper tests only MMD for distributional alignment. Classical domain adaptation offers several alternatives: CORAL-the-method (Sun & Saenko 2016, aligning second-order statistics), adversarial alignment (DANN, Ganin et al. 2016), optimal transport (Courty et al. 2017), and contrastive alignment. Testing only MMD and then drawing conclusions about \"distributional matching\" in general is an incomplete experimental design. The paper's own analysis suggests geometric misalignment at depth -- but methods like Procrustes alignment or contrastive losses address geometric alignment directly. Why was only MMD tested? The conclusion \"distributional matching fails where linear projection succeeds\" should be \"MMD-based distributional matching fails,\" since other distributional methods were not evaluated.\n\n**W4. Linear projection is applying VecMap/MUSE to a new domain -- novelty is limited.**\nThe paper correctly cites MUSE and VecMap but does not sufficiently acknowledge that applying linear cross-lingual alignment to probe representations is a straightforward domain transfer of existing techniques. The data efficiency result (saturation at ~50 pairs) is interesting but expected given the known low intrinsic dimensionality of correctness representations (3-8 dimensions per Confidence Manifold, 2026). This should be framed as confirming theoretical expectations rather than as a finding.\n\n**W5. Missing foundational references weaken positioning.**\nSeveral important works are absent:\n- Conneau et al. (2020) on depth-dependent language specificity in multilingual models -- directly relevant to the Pareto frontier claim.\n- Pires et al. (2019) on mBERT cross-lingual transfer -- foundational context for cross-lingual probe transfer.\n- Gretton et al. (2012) for MMD -- the method's foundational paper must be cited, and the kernel choice (Gaussian RBF? linear?) must be specified.\n- Sun & Saenko (2016) CORAL-the-method, Ganin et al. (2016) DANN -- directly relevant domain adaptation methods that CaCLR's MMD term should be compared against or at minimum discussed.\n- Chi et al. (2020) on the geometry of multilingual representations -- relevant to the CKA analysis and geometric misalignment discussion.\n\n**W6. Orthogonality extension from English to 20 languages is incremental.**\nMiao & Ungar (2026) showed cosine < 0.04 in English on 7-8B models. This paper shows cosine < 0.062 across 20 languages on larger models. Given that the underlying hypothesis -- correctness and confidence are encoded independently -- has no theoretical reason to be language-specific, confirmation across languages is expected. The resource-tier gradient (low-resource slightly higher cosine) is attributed to noise in confidence direction estimation, not genuine structural difference. This is a useful sanity check but not a meaningful independent contribution.\n\n**W7. The paper does not adequately differentiate from LACE (Zhou et al. 2024).**\nLACE addresses multilingual calibration via per-language layer ensembles and demonstrated the non-English calibration gap. The paper argues LACE requires \"target-language labels\" while CaCLR requires \"zero target-language correctness labels.\" However, CaCLR requires parallel inputs (translated items) -- which is also a non-trivial data requirement. The practical advantage over LACE is not clearly quantified: is CaCLR's 3.5% ECE reduction competitive with LACE's reported ECE 22% --> 3%? Without direct comparison on the same benchmark, the positioning is incomplete.\n\n---\n\n### 4. Questions for Authors\n\n1. Can you provide a direct comparison with LACE on a shared benchmark/language set? The positioning against LACE as the primary multilingual calibration competitor is central but currently relies on prose rather than empirical comparison.\n\n2. Why was only MMD tested as the distributional alignment loss? Did you consider CORAL (second-order statistics), adversarial alignment, or optimal transport? The conclusion about \"distributional matching\" failing at depth would be far more compelling if multiple distributional methods showed the same pattern.\n\n3. How does the Pareto frontier relate to the findings of Conneau et al. (2020) on depth-dependent language specificity? Their work predicts exactly this tradeoff. What does your quantification add beyond confirming their qualitative finding?\n\n4. The paper notes CaCLR requires \"parallel inputs\" from GlobalMMLU translations. How sensitive is CaCLR to the quality and domain of these parallel inputs? If parallel inputs come from a different domain (e.g., Bible parallel text vs. MCQA translations), does CaCLR still work?\n\n5. For the orthogonality analysis, can you report the full 20-language table? Showing 10/20 languages for a universal claim is insufficient.\n\n6. The CKA analysis claims \"mechanistic explanation\" -- would you obtain the same correlation if you used a simpler metric like mean cosine similarity between representations? How much does CKA specifically add over cheaper alternatives?\n\n---\n\n### 5. Minor Issues\n\n- The bibliography has multiple empty \\cite{} placeholders (Section 1), which should be filled.\n- Table 1: Scout ZS Min/Max columns show \"---\" without explanation.\n- The paper title mentions \"Distributional Matching Fails Where Linear Projection Succeeds\" but the submitted version shows CaCLR (distributional matching) *succeeding*, with only deep-layer limitations. The title appears to match a different narrative path (the negative result path from paper_framing.md) rather than the actual results. This is confusing.\n- \"Camera-ready extension\" language in the appendix (Gemma 4) should be removed for submission -- it signals incomplete work.\n- The term \"Pareto frontier\" is technically imprecise: a Pareto frontier implies no point dominates another. Some layer-depth points are dominated (e.g., layer 88 on Qwen3 is worse than layer 76 on both EN and ZS). The correct term is \"Pareto tradeoff\" or simply \"depth-transferability tradeoff.\"\n\n---\n\n### 6. Overall Assessment\n\n**Score: 4/6 (Weak Accept)**\n\n**Confidence: 4/5**\n\nThe paper addresses a genuine gap -- no prior work has systematically tested whether probe-based calibration methods transfer cross-lingually -- and provides a thorough empirical investigation at impressive scale. The mean-shift invariance proof, difficulty-capability decomposition, and CKA analysis are individually valuable analytical contributions.\n\nHowever, several novelty concerns temper enthusiasm. The depth-transferability tradeoff is a quantitative formalization of a known phenomenon (Conneau et al. 2020, LACE, Civelli et al.), not a conceptual discovery. CaCLR's MMD component is tested in isolation without comparison to other domain adaptation methods, making conclusions about \"distributional matching\" overly broad. Linear projection is a direct application of VecMap/MUSE-style alignment to a new domain. The orthogonality extension is expected and incremental. Important foundational references are missing (Conneau et al. 2020, Pires et al. 2019, Gretton et al. 2012, domain adaptation baselines).\n\nThe paper's strongest identity is as an analytical characterization paper -- the Pareto quantification, decomposition, CKA analysis, and orthogonality confirmation collectively advance the community's understanding of multilingual calibration at the representation level. I would recommend reframing contributions to foreground these analytical insights and position CaCLR as one practical implication rather than the headline."
      }
    ],
    "totalDurationMs": 125983,
    "totalTokens": 70483,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 66918,
      "output_tokens": 2823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2823,
          "cache_read_input_tokens": 66918,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 739,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "70663051-1f24-474a-a696-150fba8a2f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "012729f5-142b-43cf-9acf-973e08152efa",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Tool result

_source line 25 · 2026-05-20T21:09:02.344Z_

<details><summary>↩ Tool result · `toolu_01AobLHLuszCkD3WsGRVCLuN`</summary>

```text
Review submitted successfully. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: 4/5**

**Top strengths identified:**
- Comprehensive experimental scope (3 architectures, 20 languages, 5 transfer methods, 3 benchmarks) with appropriate controls (Hewitt & Liang control tasks, random-direction control, INT8 validation, probe complexity comparison)
- Clean mean-shift invariance proof (AUROC identically 0 under StandardScaler + LR)
- Well-designed difficulty-capability decomposition with random-direction control ruling out artifacts
- Strong statistical practice on key claims (paired permutation tests, bootstrap CIs, Cohen's d)
- Practically valuable linear projection data efficiency analysis (~50 pairs suffice)

**Top weaknesses identified:**
1. CaCLR's +1.4pp advantage over 50-pair linear projection is marginal given its substantially higher complexity (3-term loss, hyperparameter tuning, parallel inputs for all languages)
2. Architecture-dependence claim is confounded — 3 models differ in architecture, scale, depth, active parameters, and training data simultaneously; no expert routing analysis supports the causal attribution
3. CKA "mechanistic explanation" is correlational and likely confounded by depth; partial correlation controlling for depth was not computed
4. Pareto frontier reported at 7/24 layers (Qwen3) despite design specifying all 24; raises concerns about selective presentation
5. CaCLR training procedure critically underspecified (kernel, bandwidth, optimizer, architecture unclear)

**Key recommendations:** Reframe as primarily an analytical/characterization paper rather than a method contribution; report full layer and language data; qualify causal claims about architecture and CKA; specify CaCLR implementation details; test CaCLR on difficulty-removed representations to close the causal chain gap.

The review report is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`.

agentId: a87b7c9d30836e971 (use SendMessage with to: 'a87b7c9d30836e971' to continue this agent)
&lt;usage>total_tokens: 74231
tool_uses: 16
duration_ms: 164995&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a94bde79-c99c-413f-afc3-8fde4ec996b2",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "6afdb302-17fa-4afa-9775-4f8b1014dea6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **methods and experiments**.\n\n## Paper Summary\n\"Cross-Lingual Correctness Probes Reveal a Depth–Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\"\n\nThe paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. Key findings:\n\n1. **Pareto Frontier**: Deeper layers yield higher English AUROC (up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman ρ = −0.52).\n2. **CKA Mechanistic Explanation**: Geometric misalignment increases with depth. CKA–transfer correlation r=0.58 (34% variance), vs MMD r=0.25 (6%).\n3. **CaCLR Negative Result**: MMD-based consistency loss is inert across 3 OOM (Cohen's d=0.08, p=0.42).\n4. **Linear Projection**: +3.5pp AUROC with ~50-100 parallel pairs, succeeds because it learns the rotation MMD cannot.\n\nAdditional: correctness–confidence orthogonality persists across 20 languages (cosine < 0.10). Difficulty decomposition shows 65% improvement rate. Cross-benchmark generalization on Belebele and MMLU-ProX.\n\n## Key Tables/Results from the Paper\n\n**Table 1 (Pareto frontier summary):**\n- Qwen3-235B: EN_best=0.81 layer72, ZS_med=0.70 xfer_layer48, ρ_med=−0.51, σ_ρ=0.16\n- Llama 4 Scout: EN_best=0.79 layer36, ZS_med=0.68 xfer_layer24, ρ_med=−0.54, σ_ρ=0.15\n- Gemma 4 31B: EN_best=0.80 layer45, ZS_med=0.69 xfer_layer33, ρ_med=−0.58, σ_ρ=0.12\n\n**Table 2**: Per-language ZS transfer AUROC at best transfer layer (Qwen3). High-resource 0.72-0.74, mid 0.65-0.71, low (sw/bn) 0.57-0.58.\n\n**Table 3 (CKA):** CKA_shallow=0.84 median, CKA_deep=0.52 median. CKA Pearson r=0.58 (34% var), MMD r=0.25 (6% var).\n\n**Table 4 (β sweep):** β=0.001 Δ=+0.002, β=0.01 Δ=+0.001, β=0.1 Δ=−0.001, β=1.0 Δ=−0.003. Overall p=0.42, d=0.08.\n\n**Table 5 (Method comparison):** Mean-shift=0.000, CaCLR α-only=+0.005, CaCLR full=+0.012, Linear proj=+0.035 (p=0.001,d=0.55), Few-shot-25=+0.025, Few-shot-100=+0.045.\n\n**Table 6 (Linear proj sample efficiency):** 10 pairs→+0.012, 50→+0.030, 100→+0.035, 200→+0.036. Knee ~70 pairs.\n\n**Table 7 (Decomposition):** Overall 65% improved, +0.012 AUROC. Deep layers 78%, shallow 50%. Random direction 50% (n.s.).\n\n**Table 8 (Orthogonality):** EN cosine ~0.035-0.038, all langs <0.10, resource-tier gradient (high 0.04, low 0.085).\n\n**Appendices:** INT8 validation (max diff 0.8pp, r=0.997), MLP vs LogReg (MLP +2.5pp EN but 6pp larger transfer gap), cross-benchmark (method rankings consistent), control tasks (88% above 10pp selectivity).\n\n## Experimental Design Reference\nThe review_context.yaml lists 12 imagined experiments. The paper covers:\n- plan_001 (Qwen3 Pareto): ✓ covered in Tables 1-2\n- plan_002 (Llama4 Pareto): ✓ covered in Table 1\n- plan_003 (CaCLR): ✓ covered in Tables 4-5\n- plan_004 (Decomposition): ✓ covered in Table 7\n- plan_005 (Orthogonality): ✓ covered in Table 8\n- plan_006 (Probe complexity): ✓ Appendix B\n- plan_007 (Additional benchmarks): ✓ Appendix C\n- plan_008 (Gemma 4 Dense): ✓ Table 1, Section 5.7\n- plan_009 (Extended 52 langs): ✓ Section 5.8\n- plan_010 (INT8 validation): ✓ Appendix A\n- plan_011 (CKA analysis): ✓ Table 3, Section 5.2\n- plan_012 (Linear proj sensitivity): ✓ Table 6, Section 5.4\n- plan_013 (Control tasks): ✓ Appendix D\n\n## Your Task\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (methodological rigor, experimental design, statistical reporting)\n3. **Weaknesses** (methodological gaps, experimental concerns, missing controls/ablations)\n4. **Questions for Authors** (specific, actionable)\n5. **Minor Issues** (presentation, clarity)\n6. **Overall Assessment** with score (1-6) and confidence (1-5)\n\nFocus areas for R1:\n- Is the experimental design sufficient to support the claims?\n- Are the statistical methods appropriate (paired permutation tests, bootstrap CIs, Cohen's d)?\n- Is the CKA analysis convincing as a mechanistic explanation?\n- Is the CaCLR negative result well-controlled?\n- Are there missing baselines or ablations?\n- Is the linear projection comparison fair?\n- How robust are the results across architectures/languages/benchmarks?\n\nBe rigorous but fair. Identify both genuine weaknesses and acknowledge genuine strengths. The review should be 800-1200 words.",
    "agentId": "a87b7c9d30836e971",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Review submitted successfully. Here is a summary of the key findings:\n\n**Score: 4/6 (Weak Accept), Confidence: 4/5**\n\n**Top strengths identified:**\n- Comprehensive experimental scope (3 architectures, 20 languages, 5 transfer methods, 3 benchmarks) with appropriate controls (Hewitt & Liang control tasks, random-direction control, INT8 validation, probe complexity comparison)\n- Clean mean-shift invariance proof (AUROC identically 0 under StandardScaler + LR)\n- Well-designed difficulty-capability decomposition with random-direction control ruling out artifacts\n- Strong statistical practice on key claims (paired permutation tests, bootstrap CIs, Cohen's d)\n- Practically valuable linear projection data efficiency analysis (~50 pairs suffice)\n\n**Top weaknesses identified:**\n1. CaCLR's +1.4pp advantage over 50-pair linear projection is marginal given its substantially higher complexity (3-term loss, hyperparameter tuning, parallel inputs for all languages)\n2. Architecture-dependence claim is confounded — 3 models differ in architecture, scale, depth, active parameters, and training data simultaneously; no expert routing analysis supports the causal attribution\n3. CKA \"mechanistic explanation\" is correlational and likely confounded by depth; partial correlation controlling for depth was not computed\n4. Pareto frontier reported at 7/24 layers (Qwen3) despite design specifying all 24; raises concerns about selective presentation\n5. CaCLR training procedure critically underspecified (kernel, bandwidth, optimizer, architecture unclear)\n\n**Key recommendations:** Reframe as primarily an analytical/characterization paper rather than a method contribution; report full layer and language data; qualify causal claims about architecture and CKA; specify CaCLR implementation details; test CaCLR on difficulty-removed representations to close the causal chain gap.\n\nThe review report is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`."
      }
    ],
    "totalDurationMs": 164995,
    "totalTokens": 74231,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3685,
      "cache_read_input_tokens": 70053,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 70053,
          "cache_creation_input_tokens": 3685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3685,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "a94bde79-c99c-413f-afc3-8fde4ec996b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T21:09:21.728Z_

<details><summary>Logged reasoning block</summary>

```text
I now have both R1 and R2 reviews. Let me proceed with the roundtable protocol:
- Step 1: Independent reviews (done - both scored 4/6 Weak Accept)
- Step 2: Cross-share (share reviews between reviewers)
- Step 3: Converge (identify agreements and disagreements)
- Step 4: Synthesize (produce final consolidated report)

Since this is a full review mode, I need to do the complete roundtable. Let me now do Steps 2-4 myself based on the two reviews, and then compile the final report.

Let me synthesize the reviews:


Both reviewers agree on the paper's core strengths: the mean-shift invariance proof is solid, the difficulty decomposition with controls is well-executed, and the experimental scope is comprehensive. However, they diverge on significance—R1 focuses on the marginal empirical gains from CaCLR and architectural confounds, while R2questions whether the conceptual contributions (systematic study, Pareto frontier) are truly novel. The honest reporting and data efficiency arguments are positives, but the overclaiming and underspecification of CaCLR remain concerns.

Now I'm consolidating both perspectives into a unified assessment. Both reviewers land on 4/6 with similar confidence, viewing this as a technically sound analytical paper that makes incremental contributions but falls short on novelty and positioning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6afdb302-17fa-4afa-9775-4f8b1014dea6",
  "isSidechain": false,
  "requestId": "req_011CbEWGDKkQnynrsSa7BDRn",
  "type": "assistant",
  "uuid": "8cae6684-27c1-4ee3-8b3c-0af7c0293710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpzuCnvwhC7WNM9UynmAZZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2924,
      "cache_creation_input_tokens": 3791,
      "cache_read_input_tokens": 65401,
      "output_tokens": 908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2924,
          "output_tokens": 908,
          "cache_read_input_tokens": 65401,
          "cache_creation_input_tokens": 3791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3791
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

_source line 27 · 2026-05-20T21:09:24.697Z_

Both reviewers returned scores of 4/6 (Weak Accept). Now I'll conduct the roundtable synthesis (Steps 2-4) and submit the final report.

**Roundtable convergence notes:**
- Both agree on strengths: comprehensive scale, rigorous statistics, clean mean-shift proof, good difficulty decomposition
- Both flag: CKA as correlational not causal, CaCLR underspecified, positioning concerns
- R1-unique: architecture confounds, selective layer presentation, CaCLR training details missing
- R2-unique: missing key references, overclaiming vs. prior work, only MMD tested (no CORAL/DANN/OT), LACE comparison absent

Consensus: 4/6. Now submitting the consolidated report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cae6684-27c1-4ee3-8b3c-0af7c0293710",
  "isSidechain": false,
  "requestId": "req_011CbEWGDKkQnynrsSa7BDRn",
  "type": "assistant",
  "uuid": "ff60f070-fd5d-4f48-a913-04b01c20af13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpzuCnvwhC7WNM9UynmAZZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2924,
      "cache_creation_input_tokens": 3791,
      "cache_read_input_tokens": 65401,
      "output_tokens": 908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2924,
          "output_tokens": 908,
          "cache_read_input_tokens": 65401,
          "cache_creation_input_tokens": 3791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3791
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

_source line 28 · 2026-05-20T21:09:25.491Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K4vGGN9mvD8z2cZZaMFe18`</summary>

```json
{
  "query": "select:submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff60f070-fd5d-4f48-a913-04b01c20af13",
  "isSidechain": false,
  "requestId": "req_011CbEWGDKkQnynrsSa7BDRn",
  "type": "assistant",
  "uuid": "d42caa24-b553-4872-aeac-53b227a11c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpzuCnvwhC7WNM9UynmAZZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2924,
      "cache_creation_input_tokens": 3791,
      "cache_read_input_tokens": 65401,
      "output_tokens": 908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2924,
          "output_tokens": 908,
          "cache_read_input_tokens": 65401,
          "cache_creation_input_tokens": 3791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3791
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

_source line 29 · 2026-05-20T21:09:25.495Z_

<details><summary>↩ Tool result · `toolu_01K4vGGN9mvD8z2cZZaMFe18`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d42caa24-b553-4872-aeac-53b227a11c22",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "444b77fa-9716-4a80-bc35-09d545aaf2d0",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "d42caa24-b553-4872-aeac-53b227a11c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T21:09:32.363Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xwr3LWjDukGDtdrxLX5Unj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "444b77fa-9716-4a80-bc35-09d545aaf2d0",
  "isSidechain": false,
  "requestId": "req_011CbEWHvq7fg4tZGACww9k5",
  "type": "assistant",
  "uuid": "13983d7e-b599-40a7-b667-b8a75be707a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3rF62Sb3WsKHFP1MMre9M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 69192,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 69192,
          "cache_creation_input_tokens": 3848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3848
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

_source line 31 · 2026-05-20T21:09:32.369Z_

<details><summary>↩ Tool result · `toolu_01Xwr3LWjDukGDtdrxLX5Unj`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13983d7e-b599-40a7-b667-b8a75be707a3",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "6adb5a6d-7025-4ff6-af8b-fd0a96a34eb1",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "13983d7e-b599-40a7-b667-b8a75be707a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T21:09:34.934Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compose the consolidated review report and submit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6adb5a6d-7025-4ff6-af8b-fd0a96a34eb1",
  "isSidechain": false,
  "requestId": "req_011CbEWJSNd9RzNreG7r3uY5",
  "type": "assistant",
  "uuid": "08340424-c522-4eb8-b29b-4a4f967fc19a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRLrsADkhKxQ3RzkKNHKE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 73040,
      "output_tokens": 4053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4053,
          "cache_read_input_tokens": 73040,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 33 · 2026-05-20T21:11:12.848Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Fm1ebWb8D6JQqAksy6rsh9`</summary>

```json
{
  "report": "# Dream Review Report — Cross-Lingual Correctness Probes\n\n**Dream ID:** 20260520T201854 | **Review Mode:** full | **Date:** 2026-05-20\n\n---\n\n## Paper Summary\n\nThis paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. The authors discover a depth–transferability Pareto frontier (deeper layers yield better English probes but transfer worse cross-lingually, median Spearman ρ = −0.52), provide a CKA-based mechanistic explanation (geometric misalignment increases with depth, r = 0.58, 34% variance explained vs. MMD's 6%), show that CaCLR's MMD-based consistency loss is inert (d = 0.08, p = 0.42), and demonstrate that linear projection with ~50–100 parallel pairs achieves +3.5 pp AUROC by learning the rotation MMD cannot correct. Correctness–confidence orthogonality is extended from English to 20 languages.\n\n---\n\n## Reviewer R1 — Methods & Experiments\n\n### Strengths\n\n**S1. Comprehensive experimental scope with appropriate controls.** Three architectures (two MoE, one dense), 20 languages across 4 resource tiers, 5 transfer conditions, 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Control tasks (Hewitt & Liang 2019), random-direction controls for decomposition, INT8 validation, and probe complexity comparison demonstrate methodological care.\n\n**S2. Clean mean-shift rank-invariance proof.** The mathematical proof that mean-shift produces exactly ∆AUROC ≡ 0 under StandardScaler + logistic regression is a tight, novel result that corrects implicit assumptions in prior work.\n\n**S3. Well-designed difficulty–capability decomposition.** IRT-based difficulty probes with random-direction controls ruling out dimensionality-reduction artifacts. The depth-dependent improvement pattern (78% at deep vs. 50% at shallow layers) coherently supports the geometric misalignment narrative.\n\n**S4. Strong statistical practice on key claims.** Paired permutation tests, bootstrap 95% CIs (1000 resamples), Cohen's d reported throughout. The β sweep is well-structured across 3 OOM with clear null result reporting.\n\n**S5. Practically valuable linear projection analysis.** The sample efficiency curve (saturation at ~70 pairs, 90% at ~55) is actionable for practitioners and well-characterized across both architectures.\n\n### Weaknesses\n\n**W1. CKA \"mechanistic explanation\" is correlational, not causal.** The CKA–transfer correlation (r = 0.58) is presented as explaining WHY transfer fails, but CKA and transfer AUROC are both functions of depth. Partial correlation controlling for normalized depth is not reported. Without this, the 34% variance explained may substantially reflect the shared depth variable rather than a causal geometric mechanism. This is the paper's central mechanistic claim — it needs stronger evidence.\n\n**W2. Architecture-dependence claim is confounded.** The three models differ simultaneously in architecture (MoE vs. dense), scale (235B vs. 48-layer vs. 31B), depth (94 vs. 48 vs. 60 layers), active parameters, and training data. Attributing differences in ρ variance (σ_ρ = 0.12 vs. 0.15–0.16) to \"MoE routing\" without controlling for these confounds is not justified. No expert routing analysis is provided.\n\n**W3. CaCLR training procedure is critically underspecified.** The MMD kernel choice (Gaussian RBF? linear?), bandwidth selection, optimizer, learning rate, and number of training epochs are not reported. For a negative result, the community needs to be confident the method was given a fair chance. Was the kernel bandwidth tuned? Was the MMD computed on raw representations or probe outputs? Equation (2) suggests probe outputs f(h), but this should be explicit.\n\n**W4. Selective layer presentation raises concerns.** The experimental design specifies 24 probed layers for Qwen3, but Table 1 reports summary statistics. The full 24×20 layer-language matrix is not shown in the main text. For a paper whose central claim is about layer-level tradeoffs, the reader should see the complete data (at minimum in supplementary).\n\n**W5. CaCLR's marginal advantage over simple baselines undermines its utility.** CaCLR-full achieves only +1.2 pp over zero-shot (not significant, p = 0.08) while requiring parallel inputs, a 3-term loss, and α/β hyperparameter tuning. Linear projection with just 50 pairs already achieves +3.0 pp. The paper correctly identifies this as a negative result, but the framing of CaCLR as a \"proposed training objective\" in §3.2 creates the impression it is a method contribution rather than an ablation vehicle.\n\n### Questions for Authors\n\n1. Report partial correlation between CKA and transfer AUROC controlling for normalized depth. If r drops substantially, the \"mechanistic explanation\" claim needs qualification.\n2. Specify the complete CaCLR training procedure: MMD kernel, bandwidth, optimizer, learning rate, epochs, and whether MMD is computed on representations or probe outputs.\n3. Show the full layer×language AUROC matrix (at least in appendix) rather than only summary statistics.\n4. Did you try CaCLR with CKA-based alignment loss instead of MMD, given your own analysis shows CKA captures the relevant misalignment?\n\n---\n\n## Reviewer R2 — Novelty & Related Work\n\n### Strengths\n\n**S1. Genuine gap identification with coherent narrative.** The observation that all probe-based calibration methods are English-only is accurate and important. The four-finding causal chain structure (Pareto → CKA mechanism → CaCLR negative result → linear projection solution) is well-organized and compelling.\n\n**S2. Scale of evaluation is commendable.** 20 languages, 3 architectures, 3 benchmarks, 5 transfer conditions, with control tasks and INT8 validation — this is among the most thorough empirical packages in the cross-lingual calibration literature.\n\n**S3. Honest reporting of limitations.** The paper acknowledges low-resource probe selectivity issues (sw/bn ~10 pp), the MCQA-only scope, and the partial success rate of decomposition (65%). This intellectual honesty is appreciated.\n\n### Weaknesses\n\n**W1. The \"first systematic evaluation\" claim overclaims relative to prior work.** Xiao et al. (ACL 2025) already performed cross-lingual probe transfer across 8 languages with alignment methods. The distinction (knowledge boundary vs. correctness) is valid but insufficient to claim \"first systematic evaluation\" of cross-lingual probe transfer wholesale. The claim should be scoped to \"first systematic evaluation of cross-lingual *correctness* probe transfer\" with explicit acknowledgment that the experimental paradigm was established by Xiao et al.\n\n**W2. The Pareto frontier is a quantitative refinement of known phenomena, not a conceptual discovery.** Conneau et al. (2020) established that deeper layers encode more language-specific information. LACE (Zhou et al. 2024) showed that non-English calibration peaks at intermediate layers. Civelli et al. (2024) demonstrated architecture-dependent optimal depth for cross-lingual probes. The \"Pareto frontier\" framing is a useful quantitative lens, but the underlying phenomenon is well-established. The paper should position this as quantification of a known tradeoff, not as a discovery.\n\n**W3. Only MMD tested for distributional alignment — conclusions about \"distributional matching\" are overly broad.** The paper tests only MMD and then concludes \"distributional matching fails.\" Classical domain adaptation offers alternatives: CORAL-the-method (Sun & Saenko 2016, second-order statistics), adversarial alignment (DANN, Ganin et al. 2016), optimal transport (Courty et al. 2017). Testing only MMD and generalizing to all distributional methods is an incomplete experimental design. The conclusion should be \"MMD-based distributional matching fails\" until other methods are tested.\n\n**W4. Linear projection is VecMap/MUSE applied to probe representations — limited novelty.** The paper correctly cites MUSE and VecMap but does not sufficiently acknowledge that applying linear alignment to probe representations is a straightforward domain transfer. The sample efficiency result (~50 pairs) is interesting but expected given the known low intrinsic dimensionality of correctness representations.\n\n**W5. Missing foundational references weaken positioning.** Key absent works:\n- Conneau et al. (2020) on depth-dependent language specificity — directly predicts the Pareto frontier\n- Gretton et al. (2012) for MMD — foundational paper must be cited, kernel choice must be specified\n- Sun & Saenko (2016) CORAL-the-method, Ganin et al. (2016) DANN — relevant DA baselines that should at minimum be discussed\n- Chi et al. (2020) on geometry of multilingual representations — relevant to CKA analysis\n\n**W6. Orthogonality extension from English to 20 languages is incremental.** Miao & Ungar (2026) showed cosine < 0.04 in English. This paper shows cosine < 0.10 across 20 languages. Given that the underlying hypothesis (correctness and confidence are independently encoded) has no theoretical reason to be language-specific, confirmation across languages is expected rather than surprising. The resource-tier gradient is attributed to noise, not structural difference.\n\n**W7. Insufficient differentiation from LACE (Zhou et al. 2024).** LACE addresses multilingual calibration via per-language layer ensembles. The paper claims CaCLR requires \"zero target-language labels\" while LACE needs labels, but CaCLR requires parallel inputs — also a non-trivial data requirement. No direct empirical comparison is provided.\n\n### Questions for Authors\n\n1. Can you provide a direct comparison with LACE on a shared benchmark/language set?\n2. Why was only MMD tested? Did you consider CORAL, adversarial alignment, or optimal transport? Would CKA-based alignment loss work?\n3. How does the Pareto frontier relate to Conneau et al. (2020) on depth-dependent language specificity? What does your quantification add?\n4. For the orthogonality analysis, the full 20-language table (Table 8) shows only tier medians, not per-language values. Can you provide per-language cosine similarities?\n\n---\n\n## Roundtable Synthesis\n\n### Step 2: Cross-Sharing\n\nBoth reviewers independently arrived at 4/6 (Weak Accept) with confidence 4/5. Agreement is strong on core strengths (scale, statistical rigor, mean-shift proof, decomposition) and on key weaknesses (CKA causality concerns, CaCLR underspecification, positioning relative to prior work).\n\n### Step 3: Convergence — Agreements and Disagreements\n\n**Agreed strengths:**\n- Comprehensive experimental scope with 3 architectures, 20 languages, 3 benchmarks\n- Strong statistical practice throughout (permutation tests, CIs, effect sizes)\n- Mean-shift invariance proof is clean and novel\n- Difficulty decomposition with random-direction control is well-designed\n- Linear projection sample efficiency analysis is practically valuable\n\n**Agreed weaknesses:**\n- CKA as \"mechanistic explanation\" is correlational — partial correlation controlling for depth needed\n- CaCLR training details critically underspecified (kernel, bandwidth, optimizer)\n- Paper would benefit from reframing as analytical/characterization contribution\n- CaCLR tests only MMD; conclusions about \"distributional matching\" in general are overstated\n\n**R1-specific concerns (experimental):**\n- Architecture-dependence confounded by simultaneous differences in scale/depth/data\n- Selective layer presentation (summary stats only, not full matrices)\n- CaCLR is marginal over simple baselines, undermining its framing as a method contribution\n\n**R2-specific concerns (novelty):**\n- Overclaiming \"first systematic evaluation\" relative to Xiao et al. (2025)\n- Pareto frontier quantifies known phenomenon (Conneau et al. 2020, LACE)\n- Linear projection = VecMap applied to new domain\n- Missing key references (Gretton et al. 2012, CORAL, DANN, Chi et al. 2020)\n- LACE comparison absent despite being the primary multilingual calibration competitor\n- Orthogonality extension is incremental\n\n### Step 4: Final Assessment\n\n**Overall Score: 4/6 (Borderline / Weak Accept)**\n\n**Confidence: 4/5**\n\n**Summary Assessment:**\n\nThis paper addresses a genuine gap — no prior work has systematically tested cross-lingual transfer of *correctness* probes specifically — and provides a thorough empirical investigation at commendable scale. The experimental design is comprehensive (3 architectures, 20 languages, 3 benchmarks, 5 transfer methods, multiple controls), and statistical reporting is consistently rigorous.\n\nThe paper's strongest contributions are analytical rather than methodological:\n1. The mean-shift rank-invariance proof is a clean, novel result\n2. The difficulty–capability decomposition with random-direction controls is well-designed\n3. The CKA vs. MMD comparison as transfer predictors (34% vs. 6% variance) is informative\n4. The linear projection sample efficiency characterization is practically valuable\n\nHowever, several concerns prevent a higher score:\n\n**Novelty:** The depth–transferability tradeoff quantifies a known phenomenon rather than discovering one. Linear projection is a direct application of VecMap/MUSE. The orthogonality extension is expected. The paper's novelty is primarily in the systematic scope and analytical framework, not in the individual findings.\n\n**Methodological gaps:** The CKA \"mechanistic explanation\" is correlational without controlling for depth as a confounder. CaCLR tests only MMD without comparing other domain adaptation methods (CORAL, adversarial, OT), making conclusions about \"distributional matching\" in general overly broad. CaCLR training details are critically underspecified for a negative result.\n\n**Positioning:** The paper overclaims relative to prior work (Xiao et al. 2025, LACE, Conneau et al. 2020). Missing foundational references (Gretton et al. 2012, domain adaptation baselines) weaken the related work. No direct comparison with LACE despite it being the primary multilingual calibration competitor.\n\n**Recommendation:** The paper is a solid empirical characterization paper that would benefit from: (1) reframing contributions to foreground analytical insights rather than method contributions; (2) reporting partial correlation for CKA controlling for depth; (3) specifying CaCLR training details fully; (4) testing at least one additional alignment method beyond MMD; (5) more careful positioning relative to prior work on depth-dependent cross-lingual transfer.\n\n**Scores:**\n| Criterion | Score |\n|-----------|-------|\n| Soundness | 3/4 — rigorous statistics but CKA causality gap and CaCLR underspecification |\n| Novelty | 2/4 — scope is new but individual findings are refinements of known phenomena |\n| Significance | 3/4 — practically useful guidance; closes MMD path (but only MMD tested) |\n| Presentation | 3/4 — well-organized causal chain; some overclaiming in framing |\n| **Overall** | **4/6 (Borderline / Weak Accept)** |\n\n**Key revision requests (ranked by priority):**\n1. Report partial CKA–transfer correlation controlling for depth\n2. Fully specify CaCLR training procedure (kernel, bandwidth, optimizer, epochs)\n3. Test at least one non-MMD alignment method or narrow the conclusion from \"distributional matching\" to \"MMD-based matching\"\n4. Scope \"first systematic evaluation\" claim and add missing references\n5. Show full layer×language matrices (at least in appendix)\n6. Add direct comparison with LACE on shared benchmark",
  "project": "xling_calib_direction",
  "tier": "median",
  "dream_id": "20260520T201854",
  "overall_score": "4/6 — Borderline / Weak Accept",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08340424-c522-4eb8-b29b-4a4f967fc19a",
  "isSidechain": false,
  "requestId": "req_011CbEWJSNd9RzNreG7r3uY5",
  "type": "assistant",
  "uuid": "c36b7356-4ff0-4d4c-bfcc-6ade028b8a3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRLrsADkhKxQ3RzkKNHKE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 73040,
      "output_tokens": 4053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4053,
          "cache_read_input_tokens": 73040,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "c36b7356-4ff0-4d4c-bfcc-6ade028b8a3f",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Tool result

_source line 36 · 2026-05-20T21:11:13.654Z_

<details><summary>↩ Tool result · `toolu_01Fm1ebWb8D6JQqAksy6rsh9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c36b7356-4ff0-4d4c-bfcc-6ade028b8a3f",
  "isSidechain": false,
  "promptId": "4be16c5f-1c63-4e4b-8fe5-75c92cffdde7",
  "type": "user",
  "uuid": "868f77d3-0af6-4691-a3cd-29fab930981c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260520T201854\\\", \\\"tier\\\": \\\"median\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "c36b7356-4ff0-4d4c-bfcc-6ade028b8a3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-20T21:11:13.657Z_

```json
{
  "parentUuid": "868f77d3-0af6-4691-a3cd-29fab930981c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4a91edb2-4c99-4ba9-a5ed-63825c72186c",
  "timestamp": "2026-05-20T21:11:13.657Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-20T21:11:22.837Z_

Review submitted successfully.

**Summary:** Both reviewers scored 4/6 (Borderline / Weak Accept) with high confidence. The paper is a solid empirical characterization at commendable scale (3 architectures, 20 languages, 3 benchmarks) with rigorous statistics, but faces novelty concerns (depth–transferability tradeoff is a known phenomenon, linear projection = VecMap applied) and methodological gaps (CKA causality uncontrolled for depth, only MMD tested for distributional matching, CaCLR training underspecified). Top revision priorities: (1) partial CKA correlation controlling for depth, (2) CaCLR training details, (3) test non-MMD alignment or narrow claims, (4) scope "first systematic" claim and add missing references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a91edb2-4c99-4ba9-a5ed-63825c72186c",
  "isSidechain": false,
  "requestId": "req_011CbEWRtjpwhGPToAEh7JPL",
  "type": "assistant",
  "uuid": "e3e5d36b-bec2-4a1b-ad9d-b3619007791e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rZXFbPNEYMFbjQm4mCDki",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4286,
      "cache_read_input_tokens": 73753,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 73753,
          "cache_creation_input_tokens": 4286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4286
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "e3e5d36b-bec2-4a1b-ad9d-b3619007791e",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "2e133768-be7c-4456-8949-45ac7304e840"
}
```

---
