# Research conversation: Read the following 5 tex files and return their FULL contents. These are LaTeX paper files for the recursive_gen_depth_e

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9375da6d3d942d71.jsonl`
- **Structured JSON:** [`21802740cfe19fc613c0.json`](../../sessions/21/21802740cfe19fc613c0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-19T21:47:10.564Z_

Read the following 5 tex files and return their FULL contents. These are LaTeX paper files for the recursive_gen_depth_est project. I need every line — do not summarize or truncate.

1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/generalization.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/section_appendix.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/discussion.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/introduction.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/abstract.tex

Read each file completely with Read tool (no line limit). Return all contents verbatim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "98046edc-0129-42be-bb86-a354e844a8b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T21:47:10.570Z_

```json
{
  "parentUuid": "98046edc-0129-42be-bb86-a354e844a8b1",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "18c890c8-8004-4a40-83ee-2388f4d47621",
  "timestamp": "2026-05-19T21:47:10.570Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

---

### Assistant

_source line 3 · 2026-05-19T21:47:12.933Z_



I'll read all 5 files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c890c8-8004-4a40-83ee-2388f4d47621",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f94d2b98-2d70-488d-9ed6-13fba9d911a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24412,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T21:47:13.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BhMih6Zbdo4zaJJETE4WNS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94d2b98-2d70-488d-9ed6-13fba9d911a4",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc1981f9-7d85-4b88-83c1-5a66e9f82cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24412,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T21:47:13.524Z_

<details><summary>↩ Tool result · reported error · `toolu_01BhMih6Zbdo4zaJJETE4WNS`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc1981f9-7d85-4b88-83c1-5a66e9f82cba",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "fe159339-b0e7-4391-9dce-d35a5f60899f",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.",
  "sourceToolAssistantUUID": "dc1981f9-7d85-4b88-83c1-5a66e9f82cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T21:47:13.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X3EtjnMsjBKTvdxNBvfMsP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe159339-b0e7-4391-9dce-d35a5f60899f",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "025a48ae-fde1-4e79-8104-683e3756bb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24412,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T21:47:13.844Z_

<details><summary>↩ Tool result · reported error · `toolu_01X3EtjnMsjBKTvdxNBvfMsP`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "025a48ae-fde1-4e79-8104-683e3756bb5f",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "de862138-a029-49ac-802c-93e5f611a87a",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.",
  "sourceToolAssistantUUID": "025a48ae-fde1-4e79-8104-683e3756bb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T21:47:16.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_011R62AD411kUgRjXjHTvNWv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de862138-a029-49ac-802c-93e5f611a87a",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c646dbc-95d6-454a-9421-6e8c5b44c008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24412,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-19T21:47:16.157Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EdRQ1RvJeJhbTxBnxpNkp9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c646dbc-95d6-454a-9421-6e8c5b44c008",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013964a1-ff71-44a1-8bed-42b89ab87b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24412,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-19T21:47:16.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WZ6rLvqJxcAkCHzVKFSuWN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "013964a1-ff71-44a1-8bed-42b89ab87b56",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfMyMa7NEyBv6UzhxqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f759170a-bfe3-450d-9d0f-5dfb9c8e1881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AMefxe6SXok3G4F8ZAYwx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24412,
      "cache_read_input_tokens": 0,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24412,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-19T21:47:16.194Z_

<details><summary>↩ Tool result · reported error · `toolu_011R62AD411kUgRjXjHTvNWv`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c646dbc-95d6-454a-9421-6e8c5b44c008",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "0a207169-a878-4bf2-99f4-0915819daf94",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.",
  "sourceToolAssistantUUID": "5c646dbc-95d6-454a-9421-6e8c5b44c008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T21:47:16.200Z_

<details><summary>↩ Tool result · reported error · `toolu_01EdRQ1RvJeJhbTxBnxpNkp9`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "013964a1-ff71-44a1-8bed-42b89ab87b56",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "62be157a-ff30-4ffd-8f9c-50d8d0df861e",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.",
  "sourceToolAssistantUUID": "013964a1-ff71-44a1-8bed-42b89ab87b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T21:47:16.207Z_

<details><summary>↩ Tool result · reported error · `toolu_01WZ6rLvqJxcAkCHzVKFSuWN`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f759170a-bfe3-450d-9d0f-5dfb9c8e1881",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "6eaa246b-a12d-444f-a2fa-7fcd2ed0442b",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4.",
  "sourceToolAssistantUUID": "f759170a-bfe3-450d-9d0f-5dfb9c8e1881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T21:47:18.284Z_

All 5 files do not exist at the specified paths. Let me search for the actual locations of these tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eaa246b-a12d-444f-a2fa-7fcd2ed0442b",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNPX89bwhtXv2Mxrzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9a6ba4c-d622-4cbd-b342-2029beb6caf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LnMVGfFCwKPsXBqeFuZiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 24412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1643,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T21:47:19.313Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VK8jmUnidp8QmgPTKg4gbL`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a6ba4c-d622-4cbd-b342-2029beb6caf5",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNPX89bwhtXv2Mxrzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bebd715b-a229-4cbf-b154-3a0bd6118d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LnMVGfFCwKPsXBqeFuZiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 24412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1643,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T21:47:19.342Z_

<details><summary>↩ Tool result · `toolu_01VK8jmUnidp8QmgPTKg4gbL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260517T075852/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260517T075852/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260517T075852/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/theory_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/theory_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/theory_draft_3bd3d2.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/classifier_comparison_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/classifier_comparison/classifier_comparison_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/classifier_comparison/coral_percell_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bebd715b-a229-4cbf-b154-3a0bd6118d52",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "96452ed2-da36-42c9-94ba-408047117c51",
  "sourceToolAssistantUUID": "bebd715b-a229-4cbf-b154-3a0bd6118d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T21:47:19.699Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SQnQ5mCSGUn4EPSKpCvNm7`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96452ed2-da36-42c9-94ba-408047117c51",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNPX89bwhtXv2Mxrzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9ecda84-a10e-4754-8bd9-3dd97a77eb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LnMVGfFCwKPsXBqeFuZiW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 24412,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1643
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 24412,
          "cache_creation_input_tokens": 1643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1643,
            "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-19T21:47:19.722Z_

<details><summary>↩ Tool result · `toolu_01SQnQ5mCSGUn4EPSKpCvNm7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_auc_decay.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_feature_trajectory.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_feature_trajectory.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_feature_trajectory.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_atlas_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_atlas_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_atlas_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/gen_fig_auc_decay_v3.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_auc_decay.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_auc_decay.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_confusion_matrix.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_confusion_matrix.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_confusion_matrix.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/citations_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/r3_text_fixes_log.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/final_paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper/theory_section_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/theory_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/theory_draft_3bd3d2.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/classifier_comparison_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.out
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9ecda84-a10e-4754-8bd9-3dd97a77eb14",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "5022e8e3-908f-425c-b0ec-f2cb2129d044",
  "sourceToolAssistantUUID": "c9ecda84-a10e-4754-8bd9-3dd97a77eb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T21:47:22.659Z_

The files exist but without the `sections/` subdirectory. The actual paths are directly under `docs/paper/`. Let me read all 5 files now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5022e8e3-908f-425c-b0ec-f2cb2129d044",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73be9140-0632-44b8-95b1-114dc95ff170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4022,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T21:47:23.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TwLBYrKdNfwrj2EoyuT9th`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73be9140-0632-44b8-95b1-114dc95ff170",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "102c50f9-cee1-42b8-9416-0d296a59f133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4022,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T21:47:23.146Z_

<details><summary>↩ Tool result · `toolu_01TwLBYrKdNfwrj2EoyuT9th`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell (a feature-determined ceiling); on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) trained end-to-end on raw text underperforms RF by 16--32\,pp across three cells (Table~\ref{tab:baselines}); the gap is largest on GPT-2~XL temp09 (53.1\% vs.\ 85.4\%), where RF signal is strongest.
14	Depth-2 recall collapses to 8.4\% under DeBERTa, indicating that intermediate-depth distributional shifts---captured by perplexity tail statistics---are invisible to token-level neural encoders without explicit feature engineering.
15	RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
16	
17	\paragraph{Binary detectors and membership inference.}
18	Perturbation-based (DetectGPT, 28.5\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL ordinal calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
19	Cross-perplexity detection tells a different story: Binoculars \cite{binoculars2024} achieves 69.8\% with simple threshold calibration, because the observer/performer perplexity ratio implicitly encodes mean-level distributional displacement across depths.
20	A single cross-perplexity score fed to RF paradoxically drops to 63.7\% (overfitting on one feature); extracting 11 distributional statistics from per-token cross-perplexity scores and training an RF yields 78.1\%---matching our 19-feature pipeline within 0.3\,pp ($\Delta$ not significant, $p{>}0.05$).
21	Feature overlap analysis reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (both capture mean-level perplexity displacement); merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
22	The convergence of two independent feature pipelines---one designed for ordinal depth, one for binary detection---strengthens the claim that depth signal is a genuine distributional property.
23	
24	\paragraph{Surface-text ablation.}
25	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below the best RF cell; Appendix~\ref{app:zeroshot_prompt}); depth signal resides in distributional statistics inaccessible from surface text.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Ordinal depth estimation: method comparison. RF mean across 9 atlas cells (5-fold CV, 200 trees); DeBERTa-v3 range across 3 tested cells; DetectGPT: 9/9 cells; Binoculars: observer=Pythia-1.4B, performer=Pythia-410M, 9/9 cells. Chance = 25\% (4-class) / 33.3\% (d1--d3).}
31	\label{tab:baselines}
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{@{}llcc@{}}
34	\toprule
35	Method & Calibration & 4-Cl (\%) & d1--d3 (\%) \\
36	\midrule
37	RF 19-feature (ours) & RF & \textbf{78.4} & \textbf{71.6} \\
38	Binoculars \cite{binoculars2024} & threshold & 69.8 & --- \\
39	Binoculars \cite{binoculars2024} & RF (1 feat) & 63.7 & --- \\
40	RoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\
41	DeBERTa-v3 (end-to-end) & cross-entropy & 53.1--60.6 & --- \\
42	\midrule
43	Zero-shot LLM (best) & --- & 36.2 & --- \\
44	Min-K\% Prob \cite{shi2024_minkprob} & CORAL & 33.2 & 40.4 \\
45	DetectGPT \cite{mitchell2023_detectgpt} & best-of-3 & 28.5 & 24.3 \\
46	Random & --- & 25.0 & 33.3 \\
47	\bottomrule
48	\end{tabular}}
49	\end{table}
50	
51	Convergence confirms the signal resides in the features: three classifiers match within 0.8\,pp (Appendix~\ref{app:learned_estimator}), perplexity features alone recover 66.0\%, and seed replication across three families shows $\Delta{\leq}3.2$\,pp (Appendix~\ref{app:seed_replication}).
52	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified (recall ${>}$99\%); errors concentrate at d2/d3 in-distribution and spread to d1--d3 under transfer.
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
57	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.9\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
58	\label{fig:confusion_matrix}
59	\end{figure}
60	
61	\subsection{Cross-Model Transfer}
62	\label{sec:gen:crossmodel}
63	
64	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
65	
66	\begin{table}[t]
67	\centering
68	\small
69	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%). Ordinal quality: MAE\,=\,0.39, QWK\,=\,0.81 (QWK$_{\text{d1--d3}}$\,=\,0.53); 94.8\% of errors at $|\Delta| \leq 1$.}
70	\label{tab:cross_model}
71	\begin{tabular}{lccccc}
72	\toprule
73	Holdout & Acc & d0 & d1 & d2 & d3 \\
74	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
75	\midrule
76	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
77	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
78	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
79	\midrule
80	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	Mean transfer accuracy is 66.4\% four-class (d1--d3: 55.4\%; $2.7\times$ chance); d0 recall ($>$98\%) inflates the four-class headline, and d2 recall drops to 26.8\% in the worst case (Pythia holdout).
86	
87	\subsection{Cross-Strategy Transfer}
88	\label{sec:gen:crossstrategy}
89	
90	Table~\ref{tab:cross_strategy} reports leave-one-strategy-out transfer.
91	
92	\begin{table}[t]
93	\centering
94	\small
95	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
96	\label{tab:cross_strategy}
97	\begin{tabular}{lccc}
98	\toprule
99	Holdout & Pythia & OLMo & GPT-2 XL \\
100	 & Acc (\%) & Acc (\%) & Acc (\%) \\
101	\midrule
102	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
103	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
104	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
108	
109	Cross-strategy transfer yields 59.1\% four-class (d1--d3: 45.9\%, chance = 33\%), 7\,pp below cross-model transfer.
110	This gap is itself an empirical finding: different decoding strategies induce structurally distinct degradation trajectories in feature space, not merely noisier versions of the same trajectory.
111	Training on nucleus + top-$k$ inverts the d1/d2 boundary under temperature (d1v2 AUC $<$ 0.5), because temperature scaling accelerates convergence (\S\ref{sec:method:theory}).
112	A two-stage pipeline (strategy identification + depth classification) recovers 11.5\,pp, with a 31.5\,pp d1--d3 gap between correct and wrong routing confirming feature-space misalignment (Appendix~\ref{app:extended_discussion}).
113	
114	\paragraph{Prompted generation.}
115	Replicating the GPT-2~XL nucleus pipeline with topic-seeded generation yields 69.5\% (95\% CI $[68.9, 70.2]$, $-$13.8\,pp vs.\ BOS-seeded, $2.8\times$ chance), with monotonic AUC decay and identical top features (Appendix~\ref{app:prompted_gen}): prompt conditioning attenuates but does not eliminate the depth signal.
116	
117	%% ----------------------------------------------------------------
118	\subsection{Preliminary Cross-Scale Observations}
119	\label{sec:gen:crossscale}
120	
121	Depth signal persists at larger scales: 7--8B models achieve 60--70\% and 14B (Qwen2.5-14B) reaches 54.1\% (d1--d3: 57.4\%, chance = 33\%), though confounded by five factors (quantization, sample size, single strategy, vocabulary mismatch, self-reference scoring; Appendix~\ref{app:cross_scale_confounds}).
122	Cross-model chains (84.75\%) and cross-domain arXiv (74.1\%) confirm robustness at the primary 1--1.5B scale (Appendix~\ref{app:cross_scale_full}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "102c50f9-cee1-42b8-9416-0d296a59f133",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "c8864849-f46a-40ca-8ca5-dff354975eda",
  "sourceToolAssistantUUID": "102c50f9-cee1-42b8-9416-0d296a59f133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T21:47:24.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JQMa98pNJ8V5VXMxev6V2Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8864849-f46a-40ca-8ca5-dff354975eda",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a0b7102-2e15-4a70-bf10-c830b275fbfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4022,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T21:47:24.365Z_

<details><summary>↩ Tool result · `toolu_01JQMa98pNJ8V5VXMxev6V2Y`</summary>

```text
1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
44	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
45	
46	\subsection{Permutation Importance}
47	\label{app:permutation}
48	
49	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
50	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
51	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
52	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
53	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
54	
55	\subsection{Feature Trajectories}
56	\label{app:feature_trajectories}
57	
58	\begin{figure}[h]
59	\centering
60	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
61	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
62	\label{fig:feature_trajectory}
63	\end{figure}
64	
65	\subsection{Per-Class Recall}
66	\label{app:per_class}
67	
68	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
69	Depth~0 recall exceeds 97\% uniformly.
70	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
71	
72	\begin{table}[h]
73	\centering
74	\small
75	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
76	\label{tab:per_class_recall}
77	\begin{tabular}{@{}lcccc@{}}
78	\toprule
79	Cell & d0 & d1 & d2 & d3 \\
80	\midrule
81	Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
82	Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
83	Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
84	OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
85	OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
86	OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
87	GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
88	GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
89	GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
90	\bottomrule
91	\end{tabular}
92	\end{table}
93	
94	\subsection{DCOL Iteration Details}
95	\label{app:dcol_iterations}
96	
97	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
98	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
99	
100	\begin{table}[h]
101	\centering
102	\small
103	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
104	\label{tab:dcol_iterations}
105	\resizebox{\columnwidth}{!}{%
106	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
107	\toprule
108	Ver. & Backbone & Config & Outcome \\
109	\midrule
110	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
111	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
112	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
113	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
114	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
115	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	\subsection{Zero-Shot LLM Prompt Template}
121	\label{app:zeroshot_prompt}
122	
123	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
124	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
125	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
126	No in-context examples are provided.
127	
128	\begin{quote}
129	\small
130	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
131	
132	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
133	\end{quote}
134	
135	\subsection{Temperature Robustness}
136	\label{app:multi_tau}
137	
138	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
139	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
140	
141	\paragraph{Within-$\tau$ robustness.}
142	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
143	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
144	
145	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
146	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
147	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
148	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
149	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
150	
151	\paragraph{Cross-$\tau$ non-transferability.}
152	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
153	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
154	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
155	
156	\paragraph{Ecological validity.}
157	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
158	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
164	\label{tab:multi_tau_within}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{@{}lcccc@{}}
167	\toprule
168	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
169	\midrule
170	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
171	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
172	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
173	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
182	\label{tab:multi_tau_cross}
183	\begin{tabular}{@{}lcc@{}}
184	\toprule
185	Holdout & Acc (\%) & d1v2 AUC \\
186	\midrule
187	$\tau{=}0.5$ & 52.2 & 0.176 \\
188	$\tau{=}0.7$ & 41.0 & 0.299 \\
189	$\tau{=}0.9$ & 46.4 & 0.277 \\
190	$\tau{=}1.1$ & 47.1 & 0.525 \\
191	\midrule
192	Mean & 46.7 & 0.319 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\subsection{Feature Overlap Analysis}
198	\label{app:feature_overlap}
199	
200	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
201	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
202	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
203	
204	\subsection{End-to-End Learning}
205	\label{app:e2e}
206	
207	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
208	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
209	
210	\begin{table}[h]
211	\centering
212	\small
213	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
214	\label{tab:e2e_detail}
215	\resizebox{\columnwidth}{!}{%
216	\begin{tabular}{@{}lccccc@{}}
217	\toprule
218	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
219	\midrule
220	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
221	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
222	\midrule
223	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
224	\bottomrule
225	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
226	\end{tabular}}
227	\end{table}
228	
229	\paragraph{Feature space divergence.}
230	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
231	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
232	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
233	
234	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
235	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
236	
237	\subsection{Domain Bias Analysis}
238	\label{app:domain_bias}
239	
240	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
241	
242	\paragraph{Methodological note.}
243	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
244	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
245	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
246	
247	\paragraph{Sub-A: Standard CV.}
248	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
249	
250	\paragraph{Sub-B: LOGO evaluation.}
251	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
252	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
253	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
254	
255	\paragraph{Sub-C: Negative control.}
256	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
257	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
258	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
259	
260	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
261	
262	\subsection{Wild-Data Calibration}
263	\label{app:calibration}
264	
265	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
266	
267	\begin{table}[h]
268	\centering
269	\small
270	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
271	\label{tab:calibration}
272	\resizebox{\columnwidth}{!}{%
273	\begin{tabular}{@{}llrccc@{}}
274	\toprule
275	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
276	\midrule
277	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
278	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
279	\addlinespace
280	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
281	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
282	\addlinespace
283	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
284	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
290	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
291	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
292	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
293	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
294	
295	\paragraph{Threshold calibration.}
296	A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
297	The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
298	Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ reduces C4 FPR from 33.4\% to 2.8\% and FineWeb FPR from 16.9\% to 0.7\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
299	The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
300	Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.
301	
302	\subsection{Downstream Curation PoC}
303	\label{app:curation_poc}
304	
305	To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
306	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
307	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
308	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
309	
310	\begin{table}[h]
311	\centering
312	\small
313	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
314	\label{tab:curation_poc}
315	\resizebox{\columnwidth}{!}{%
316	\begin{tabular}{@{}lcccccc@{}}
317	\toprule
318	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
319	\midrule
320	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
321	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
322	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
323	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
324	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
325	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
326	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
327	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
328	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
329	\bottomrule
330	\end{tabular}}
331	\end{table}
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
337	\label{tab:curation_comparisons}
338	\resizebox{\columnwidth}{!}{%
339	\begin{tabular}{@{}lccc@{}}
340	\toprule
341	Comparison & $\Delta$ PPL & $t$ & $p$ \\
342	\midrule
343	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
344	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
345	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
346	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
347	\bottomrule
348	\end{tabular}}
349	\end{table}
350	
351	RF-based depth filtering (19-feature F1\,=\,0.997) substantially outperforms a simple perplexity-threshold baseline (F1\,=\,0.845) for identifying low-depth passages; the multi-feature representation provides discriminative value beyond raw perplexity.
352	However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.
353	
354	\subsection{Reference Model Ablation}
355	\label{app:ref_ablation}
356	
357	\begin{table}[h]
358	\centering
359	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
360	\label{tab:ref_ablation}
361	\resizebox{\columnwidth}{!}{%
362	\begin{tabular}{@{}lcc@{}}
363	\toprule
364	Reference Model & Architecture & Accuracy (\%) \\
365	\midrule
366	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
367	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
368	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
369	\bottomrule
370	\end{tabular}}
371	\end{table}
372	
373	\subsection{Cross-Scale Full Results}
374	\label{app:cross_scale_full}
375	
376	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
377	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B-Instruct), all under 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth).
378	The 7--8B models generate depths $d \in \{0, 1, \ldots, 5\}$; the 14B model generates $d \in \{0, 1, 2, 3\}$.
379	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
380	
381	\paragraph{Scale comparison.}
382	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).
383	
384	\begin{table}[h]
385	\centering
386	\small
387	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3, nucleus), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
388	\label{tab:cross_scale}
389	\resizebox{\columnwidth}{!}{%
390	\begin{tabular}{@{}lccc@{}}
391	\toprule
392	Model & 4-class acc & $\mathrm{EDD}_{T{=}0.70}$ & d0v1 AUC \\
393	\midrule
394	GPT-2~XL (1.5B) & 84.3 & 4 & 0.999 \\
395	OLMo-1B & 78.9 & 4 & 0.997 \\
396	Pythia-1.4B & 78.7 & 4 & 0.998 \\
397	\midrule
398	Llama-3.1-8B & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
399	Qwen2.5-7B & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
400	\midrule
401	Qwen2.5-14B$^\dagger$ & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
402	\bottomrule
403	\end{tabular}}
404	\end{table}
405	
406	\paragraph{(1) Depth signal persists at 7--8B scale.}
407	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
408	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
409	
410	\paragraph{(2) EDD at 7--8B scale.}
411	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
412	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
413	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
414	
415	\begin{table}[h]
416	\centering
417	\small
418	\caption{Consecutive binary AUC (nucleus $p{=}0.95$). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below $T{=}0.70$); Qwen2.5-7B shows a U-shaped pattern with all pairs above $T$; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has d0v1 below $T$, yielding $\mathrm{EDD}{=}0$.}
419	\label{tab:cross_scale_auc}
420	\begin{tabular}{@{}lccccc@{}}
421	\toprule
422	Model & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
423	\midrule
424	Llama-3.1-8B & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
425	Qwen2.5-7B & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
426	Qwen2.5-14B$^\dagger$ & 0.643 & 0.713 & 0.728 & \multicolumn{2}{c}{--} \\
427	\bottomrule
428	\end{tabular}
429	\end{table}
430	
431	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
432	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
433	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
434	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
435	
436	\begin{table}[h]
437	\centering
438	\small
439	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
440	\label{tab:llama3_base_auc}
441	\begin{tabular}{lccccc}
442	\toprule
443	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
444	\midrule
445	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
446	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
452	
453	\paragraph{(4) Signal attenuation at 14B.}
454	Qwen2.5-14B represents a boundary condition: four-class accuracy drops to 54.1\% (95\% CI $[53.4, 54.7]$, $2.2\times$ chance), with $\mathrm{EDD}_{0.70}{=}0$ because d0-vs-d1 AUC (0.643) falls below the 0.70 threshold (Table~\ref{tab:cross_scale_auc}).
455	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), nearly vanishes at 14B.
456	Inter-depth discrimination at d1--d3 remains comparable: d1v2 AUC (0.713) and d2v3 AUC (0.728) both exceed 0.70, and d1--d3 balanced accuracy reaches 57.4\% (chance = 33\%).
457	Feature importance undergoes a structural shift: higher-order moments (kurtosis, skewness of perplexity) replace first/second-order statistics (\texttt{p90\_ppl}, variance) as top features, consistent with the theoretical prediction that increased model capacity compresses perplexity tails (\S\ref{sec:method:theory}); first-order tail statistics become less informative while higher-order shape changes persist.
458	This result carries an important caveat: Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), whereas all other experiments use Pythia-1.4B.
459	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
460	
461	\paragraph{Caveats.}
462	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
463	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
464	
465	\paragraph{Confounds.}
466	\label{app:cross_scale_confounds}
467	Five confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between larger generators and the 1.4B reference model; (5)~Qwen2.5-14B uses self-reference rather than the Pythia-1.4B reference used for all other experiments, preventing direct cross-scale comparison at the 14B data point.
468	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
469	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
470	
471	\subsection{Cross-Boundary Generalization}
472	\label{app:cross_boundary}
473	
474	The preceding experiments assume a single model family generates all recursive depths.
475	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
476	We probe whether the depth signal persists under two relaxations of the single-model assumption.
477	
478	\paragraph{Cross-model recursive chains.}
479	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
480	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
481	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
482	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
483	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
484	
485	\paragraph{Confound discussion.}
486	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
487	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
488	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
489	We address this confound directly with a reverse-chain control below.
490	
491	\paragraph{Reverse-chain control.}
492	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
493	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
494	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
495	
496	\paragraph{Cross-domain transfer.}
497	All prior experiments use WikiText-103 as the seed corpus.
498	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
499	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
500	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
501	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
502	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
503	
504	\subsection{Cross-Seed Replication}
505	\label{app:seed_replication}
506	
507	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
508	
509	\begin{table}[h]
510	\centering
511	\small
512	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
513	\label{tab:seed_replication}
514	\begin{tabular}{@{}llccc@{}}
515	\toprule
516	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
517	\midrule
518	Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
519	Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
520	\midrule
521	OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
522	OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
523	\midrule
524	GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
525	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
531	For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
532	Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.
533	
534	\paragraph{Outlier handling.}
535	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
536	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
537	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
538	
539	\subsection{Depth-4 Extension}
540	\label{app:depth4_ext}
541	
542	We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
543	Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
544	For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
545	$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.
546	
547	\paragraph{Feature monotonicity at d4.}
548	For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
549	Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
550	OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
551	The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
552	This discrepancy illustrates that multi-class classifiers can leverage global distributional structure unavailable to pairwise comparisons.
553	The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
554	This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.
555	
556	\subsection{Generation Length Ablation}
557	\label{app:length_ablation}
558	
559	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
560	
561	\begin{table}[h]
562	\centering
563	\small
564	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
565	\label{tab:length_ablation}
566	\begin{tabular}{@{}lc@{}}
567	\toprule
568	Passage length (tokens) & Acc (\%) \\
569	\midrule
570	128 & 68.35 \\
571	256 & 73.80 \\
572	512 & 77.82 \\
573	\bottomrule
574	\end{tabular}
575	\end{table}
576	
577	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
578	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
579	
580	\subsection{Mixed-Depth Corpus}
581	\label{app:mixed_depth}
582	
583	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
584	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.
585	Macro-recall $\Delta$ = $-$1.62\,pp (within the 2\,pp threshold); individual class variations (max 2.43\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.
586	
587	\subsection{Learned Estimator Comparison}
588	\label{app:learned_estimator}
589	
590	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
591	The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
592	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
593	
594	\begin{table}[h]
595	\centering
596	\small
597	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
598	\label{tab:learned_estimator}
599	\begin{tabular}{@{}lcccc@{}}
600	\toprule
601	Method & Pythia & OLMo & GPT-2 XL & Mean \\
602	\midrule
603	RF (baseline) & --- & --- & --- & 66.4 \\
604	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
605	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
606	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
607	\bottomrule
608	\end{tabular}
609	\end{table}
610	
611	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
612	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
613	
614	\subsection{Instruction-Tuned Model at 1.5B Scale}
615	\label{app:instruct_1p5b}
616	
617	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
618	
619	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
620	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
621	
622	The top-5 features shift substantially: \texttt{surprisal\_range}, \texttt{surprisal\_position\_corr}, \texttt{prob\_std}, \texttt{surprisal\_first\_half\_minus\_second}, and \texttt{surprisal\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
623	This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.
624	
625	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
626	
627	\subsection{Downstream Fine-Tuning Probe}
628	\label{app:downstream}
629	
630	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
631	
632	\begin{table}[h]
633	\centering
634	\small
635	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
636	\label{tab:downstream}
637	\begin{tabular}{@{}lcc@{}}
638	\toprule
639	Training subset & PPL & $\Delta$ vs.\ baseline \\
640	\midrule
641	Baseline (no fine-tuning) & 5.67 & --- \\
642	d0 only & 5.65 & $-$0.02 \\
643	d1 only & 5.55 & $-$0.12 \\
644	d2 only & 5.56 & $-$0.11 \\
645	Mixed (d0--d3) & 5.55 & $-$0.12 \\
646	\bottomrule
647	\end{tabular}
648	\end{table}
649	
650	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
651	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
652	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
653	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
654	
655	\subsection{Feature Group Ablation}
656	\label{app:feature_ablation}
657	
658	Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
659	
660	\begin{table}[h]
661	\centering
662	\small
663	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
664	\label{tab:feature_ablation}
665	\begin{tabular}{@{}lccc@{}}
666	\toprule
667	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
668	\midrule
669	Full (all 19) & 19 & 66.6 & --- \\
670	Perplexity only & 9 & 66.0 & $-$0.5 \\
671	Entropy/Surprisal only & 5 & 63.2 & $-$3.4 \\
672	Repetition/Diversity only & 5 & 53.0 & $-$13.6 \\
673	\midrule
674	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.3 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.5$\,pp), while repetition/diversity features alone fall 13.6\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
680	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
681	
682	\subsection{RF Seed Robustness}
683	\label{app:rf_seed}
684	
685	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
686	
687	\begin{table}[h]
688	\centering
689	\small
690	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
691	\label{tab:rf_seed}
692	\begin{tabular}{@{}lc@{}}
693	\toprule
694	Seed & Acc (\%) \\
695	\midrule
696	42 & 66.4 \\
697	123 & 66.5 \\
698	456 & 66.5 \\
699	\midrule
700	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
701	\bottomrule
702	\end{tabular}
703	\end{table}
704	
705	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
706	
707	\subsection{Binary Detector Baselines for Ordinal Classification}
708	\label{app:detector_baselines}
709	
710	We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.
711	
712	\paragraph{Binary detectors (Pythia nucleus).}
713	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
714	The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
715	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
716	Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.
717	
718	\paragraph{Membership inference baselines (all 9 cells).}
719	DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%).
720	Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
721	Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
722	CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
723	Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
724	Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%---matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).
725	
726	\paragraph{Augmented feature set.}
727	To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
728	The 20-feature model (19 + Min-K\%) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
729	Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
730	The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
731	The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
732	
733	\subsection{Binoculars Feature Ablation and Signal Decomposition}
734	\label{app:feature_ablation_bino}
735	
736	To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).
737	
738	\begin{table}[h]
739	\centering
740	\small
741	\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
742	\label{tab:bino_ablation}
743	\begin{tabular}{@{}lccc@{}}
744	\toprule
745	Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
746	\midrule
747	6 overlap only & 6 & 75.9 & $-$2.5 \\
748	Our 19 features & 19 & 78.4 & --- \\
749	Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
750	Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
751	\bottomrule
752	\end{tabular}
753	\end{table}
754	
755	The 6 shared perplexity features alone achieve 75.9\% (97\% of the total above-chance signal), confirming that mean-level perplexity distributional displacement is the core depth signal.
756	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.
757	
758	\paragraph{Strategy-dependent complementarity.}
759	The merged improvement varies by decoding strategy: nucleus and temperature cells gain +5.1\,pp on average, while top-k cells gain only +2.8\,pp.
760	Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
761	
762	% TODO: Add 14B Binoculars ablation results when available
763	
764	\subsection{Prompted Generation Results}
765	\label{app:prompted_gen}
766	
767	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
768	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
769	
770	\begin{table}[h]
771	\centering
772	\small
773	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
774	\label{tab:prompted_gen}
775	\begin{tabular}{@{}lc@{}}
776	\toprule
777	Metric & Value \\
778	\midrule
779	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
780	BOS-seeded baseline (\%) & 83.3 \\
781	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
782	\midrule
783	AUC d0v1 & 0.916 \\
784	AUC d1v2 & 0.782 \\
785	AUC d2v3 & 0.744 \\
786	\midrule
787	Top-1 feature & \texttt{p90\_ppl} \\
788	Top-2 feature & \texttt{var\_surprisal} \\
789	Top-3 feature & \texttt{p75\_ppl} \\
790	\bottomrule
791	\end{tabular}
792	\end{table}
793	
794	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
795	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
796	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
797	
798	\subsection{Extended Discussion}
799	\label{app:extended_discussion}
800	
801	\paragraph{Cross-strategy conditional decomposition.}
802	The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
803	Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
804	Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
805	End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.
806	
807	\paragraph{Depth-graduated curation (inconclusive preliminary evidence).}
808	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
809	Recursive generation depth estimation could enable a finer-grained alternative: retain low-depth generations (d1) while down-weighting high-depth text (d3+) where tail erosion has degraded quality.
810	A pilot study (Appendix~\ref{app:curation_poc}) yields inconclusive evidence: the RF-vs-unfiltered comparison is not significant ($p>0.4$), though RF-filtered subsets outperform size-matched random subsampling ($p<0.001$--$0.02$ before Bonferroni correction; $p<0.003$--$0.06$ after correction at $\alpha{=}0.05/3{=}0.017$, with 1 of 3 comparisons surviving).
811	The d1/d2 boundary inversion under cross-strategy transfer further limits practical curation without strategy metadata.
812	Large-scale validation is needed before depth-graduated filtering can be considered practical.
813	
814	\paragraph{Toward a provenance toolkit.}
815	Depth estimation complements existing provenance methods along orthogonal axes.
816	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
817	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
818	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
819	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
820	
821	\subsection{Computational Resources and Reproducibility}
822	\label{app:compute}
823	
824	\paragraph{Hardware.}
825	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
826	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B QLoRA experiments, and all ablations.
827	
828	\paragraph{Software.}
829	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
830	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
831	
832	\paragraph{Hyperparameters.}
833	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
834	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
835	
836	\paragraph{Inference cost.}
837	Feature extraction requires a single forward pass of the reference model.
838	On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
839	RF classification adds negligible overhead ($<$1\,s).
840	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a0b7102-2e15-4a70-bf10-c830b275fbfd",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "abd66cdb-b96f-4942-b925-1391e658a526",
  "sourceToolAssistantUUID": "0a0b7102-2e15-4a70-bf10-c830b275fbfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T21:47:24.552Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QqhuvQgerqAMYZxit4Ks6o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abd66cdb-b96f-4942-b925-1391e658a526",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3000802d-2578-40c6-ba5c-26906ae73569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4022,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T21:47:24.564Z_

<details><summary>↩ Tool result · `toolu_01QqhuvQgerqAMYZxit4Ks6o`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}); cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while binary detectors and membership inference methods achieve only 30--35\%.
6	
7	\paragraph{Accumulation settings.}
8	Our primary benchmark uses full-replacement chains; in practice, model training involves accumulation, mixing human data with synthetic outputs at unknown proportions \cite{gerstgrasser2024_accumulate}.
9	Under accumulation (GPT-2~XL, nucleus), both 50/50 and 25/75 human-synthetic mixing conditions achieve comparable accuracy (${\sim}$69--70\%), down from 84.2\% under full replacement.
10	The attenuation is substantial (${\sim}$15\,pp) but depth estimation remains $2.8{\times}$ chance; the 1\,pp gap between mixing ratios falls within cross-seed variance (2.04\,pp) and should not be interpreted as a trend.
11	Extending the feature set to handle continuous mixing ratios is a direction for future work.
12	
13	\paragraph{Scale and deployment implications.}
14	The depth signal attenuates with model scale: at 14B, d0/d1 separability drops sharply ($\mathrm{EDD}_{0.70}{=}0$), though d1--d3 discrimination persists above chance.
15	This suggests that depth estimation complements rather than replaces binary detection for practical data auditing: binary detectors handle the human-vs-machine boundary where depth estimation is redundant ($>$97\% d0 recall), while depth estimation provides the finer ordinal resolution that binary methods cannot.
16	A practical deployment path proceeds from controlled settings, where model and strategy are known, to partially known settings via strategy-identification routing, to fully unknown settings requiring strategy-invariant features (Appendix~\ref{app:extended_discussion}).
17	
18	\paragraph{Multi-channel depth encoding.}
19	Feature ablation reveals that ordinal depth signal decomposes into channels with decreasing contribution (Appendix~\ref{app:feature_ablation_bino}).
20	The 6 core perplexity features shared between our pipeline and Binoculars (mean, variance, median, p10, p90, skewness) achieve 75.9\% alone---97\% of the total above-chance signal.
21	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) add +2.3\,pp; Binoculars' 5 unique cross-model features add +4.3\,pp when merged, yielding 82.6\%.
22	The merged improvement is strategy-dependent: nucleus and temperature cells gain +5.1\,pp on average, while top-k cells gain only +2.8\,pp, suggesting that top-k truncation limits the information available to cross-model divergence features.
23	That two independent feature pipelines---one designed for depth estimation, one for binary detection---converge to within 0.3\,pp validates ordinal depth as a genuine multi-channel distributional phenomenon.
24	
25	\paragraph{Open challenges.}
26	Cross-strategy transfer (d1--d3: 45.9\%) remains the primary bottleneck, driven by structurally distinct feature-space trajectories across decoding strategies.
27	Scale-dependent signal attenuation and depth-quality entanglement are open challenges.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3000802d-2578-40c6-ba5c-26906ae73569",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "e66c5c2a-f779-4643-a175-19acc4416204",
  "sourceToolAssistantUUID": "3000802d-2578-40c6-ba5c-26906ae73569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T21:47:25.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JDXDtbrD87vs1ZvhakyZtn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e66c5c2a-f779-4643-a175-19acc4416204",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15204fff-7d8b-4e58-8f09-0f460b9270d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4022,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T21:47:25.055Z_

<details><summary>↩ Tool result · `toolu_01JDXDtbrD87vs1ZvhakyZtn`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
13	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
14	
15	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
16	Specifically, the perplexity tail feature family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance emerge as dominant depth indicators, with group-level dominance robust across all 9 model--strategy configurations and three importance measures.
17	The sole 8B instruction-tuned model tested (Llama-3.1-8B-Instruct) exhibits monotonically decreasing AUC, in contrast to the non-monotonic trajectory of its base-model counterpart; whether this regularization effect generalizes across architectures remains open (Appendix~\ref{app:cross_scale_full}).
18	
19	Following the tradition of benchmark-driven empirical studies in NLP, our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty; the convergence of multiple classifiers (RF, XGBoost, LightGBM within 0.4\,pp; \S\ref{sec:gen:baselines}) confirms that discriminative signal resides in feature design, not classifier architecture.
20	We formalize recursive generation depth estimation as ordinal classification and introduce a lightweight pipeline: compute 19 reference-model statistical features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
21	To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K samples).
22	The atlas reveals strategy-dependent degradation trajectories and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
23	
24	Our contributions are:
25	\begin{itemize}[nosep,leftmargin=*]
26	    \item \textbf{Task formalization and benchmark.} We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark ($3$ model families $\times$ $3$ decoding strategies $\times$ $4$ depths).
27	
28	    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family dominates depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}4$ for all three families, validated by 5-class (d0--d4) extension (71--80\%); at $T{=}0.75$, Pythia achieves $p{=}0.001$ with graded confidence across families.
29	
30	    \item \textbf{Generalization and cross-strategy analysis.} Cross-model LOO 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, single-cell prompted 69.5\%, preliminary cross-scale at 7--14B (54\% Qwen2.5-14B to 70\% Llama-3.1-8B, confounded by architecture and precision; \S\ref{sec:gen:crossscale}). We identify a structural barrier in cross-strategy transfer (59.1\%, d1--d3: 45.9\%): decoding strategies induce qualitatively distinct degradation trajectories, with d1/d2 boundary inversion under strategy mismatch.
31	
32	    \item \textbf{Feature convergence analysis.} Independent cross-perplexity features (Binoculars) converge to matching ordinal accuracy (78.1\% vs.\ our 78.4\%); merging both feature sets yields 82.6\%, decomposing the depth signal into three channels: perplexity displacement (97\% of above-chance signal), distributional shape (+2.3\,pp), and cross-model divergence (+4.3\,pp).
33	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15204fff-7d8b-4e58-8f09-0f460b9270d1",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "52439066-1fe7-4cf1-bf70-615523884121",
  "sourceToolAssistantUUID": "15204fff-7d8b-4e58-8f09-0f460b9270d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T21:47:25.372Z_

<details open><summary>🔧 Tool call — Read · `toolu_018juY52GAE4YkNpWebeHJjy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52439066-1fe7-4cf1-bf70-615523884121",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfNenPqW51FRVtdxcLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51d363d7-7d27-4284-838c-b7660e31538f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P36e7xQFwNQRcdJU5tfMnq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4022,
      "cache_read_input_tokens": 26055,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 418,
          "cache_read_input_tokens": 26055,
          "cache_creation_input_tokens": 4022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4022,
            "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-19T21:47:25.377Z_

<details><summary>↩ Tool result · `toolu_018juY52GAE4YkNpWebeHJjy`</summary>

```text
1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over statistical features dominated by the perplexity tail family achieves d1--d3 balanced accuracy of 59--82\% (four-class: 69--86\%) across nine model--strategy cells; convergence of RF, XGBoost, and LightGBM confirms that discriminative signal resides in feature design, not classifier choice.
5	Cross-model transfer reaches 66.4\%, cross-domain arXiv 74.1\%, and cross-strategy transfer 59.1\%; the gap reveals that decoding strategies induce structurally distinct degradation trajectories, formalized via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families).
6	Perturbation-based and membership inference baselines (29--33\%) fall far below our pipeline; cross-perplexity features (Binoculars) converge to matching performance (78.1\% vs.\ 78.4\%), and merging both feature sets yields 82.6\%, decomposing the depth signal into perplexity displacement, distributional shape, and cross-model divergence channels.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51d363d7-7d27-4284-838c-b7660e31538f",
  "isSidechain": true,
  "promptId": "b865f4c5-84b4-4a6c-b504-d11844367fe3",
  "agentId": "a9375da6d3d942d71",
  "type": "user",
  "uuid": "7ddfa02e-4232-4d9b-bac2-55a48fd3a759",
  "sourceToolAssistantUUID": "51d363d7-7d27-4284-838c-b7660e31538f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T21:57:06.806Z_

Here are the full contents of all 5 files:

---

**File 1: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex`**

```latex
\section{Generalization and Robustness}
\label{sec:generalization}

We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).

\subsection{Classifier Comparison and Surface-Text Ablation}
\label{sec:gen:baselines}

Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell (a feature-determined ceiling); on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).

\paragraph{Neural end-to-end baselines.}
DeBERTa-v3-base (LoRA) trained end-to-end on raw text underperforms RF by 16--32\,pp across three cells (Table~\ref{tab:baselines}); the gap is largest on GPT-2~XL temp09 (53.1\% vs.\ 85.4\%), where RF signal is strongest.
Depth-2 recall collapses to 8.4\% under DeBERTa, indicating that intermediate-depth distributional shifts---captured by perplexity tail statistics---are invisible to token-level neural encoders without explicit feature engineering.
RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.

\paragraph{Binary detectors and membership inference.}
Perturbation-based (DetectGPT, 28.5\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL ordinal calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
Cross-perplexity detection tells a different story: Binoculars \cite{binoculars2024} achieves 69.8\% with simple threshold calibration, because the observer/performer perplexity ratio implicitly encodes mean-level distributional displacement across depths.
A single cross-perplexity score fed to RF paradoxically drops to 63.7\% (overfitting on one feature); extracting 11 distributional statistics from per-token cross-perplexity scores and training an RF yields 78.1\%---matching our 19-feature pipeline within 0.3\,pp ($\Delta$ not significant, $p{>}0.05$).
Feature overlap analysis reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (both capture mean-level perplexity displacement); merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
The convergence of two independent feature pipelines---one designed for ordinal depth, one for binary detection---strengthens the claim that depth signal is a genuine distributional property.

\paragraph{Surface-text ablation.}
Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below the best RF cell; Appendix~\ref{app:zeroshot_prompt}); depth signal resides in distributional statistics inaccessible from surface text.

\begin{table}[t]
\centering
\small
\caption{Ordinal depth estimation: method comparison. RF mean across 9 atlas cells (5-fold CV, 200 trees); DeBERTa-v3 range across 3 tested cells; DetectGPT: 9/9 cells; Binoculars: observer=Pythia-1.4B, performer=Pythia-410M, 9/9 cells. Chance = 25\% (4-class) / 33.3\% (d1--d3).}
\label{tab:baselines}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llcc@{}}
\toprule
Method & Calibration & 4-Cl (\%) & d1--d3 (\%) \\
\midrule
RF 19-feature (ours) & RF & \textbf{78.4} & \textbf{71.6} \\
Binoculars \cite{binoculars2024} & threshold & 69.8 & --- \\
Binoculars \cite{binoculars2024} & RF (1 feat) & 63.7 & --- \\
RoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\
DeBERTa-v3 (end-to-end) & cross-entropy & 53.1--60.6 & --- \\
\midrule
Zero-shot LLM (best) & --- & 36.2 & --- \\
Min-K\% Prob \cite{shi2024_minkprob} & CORAL & 33.2 & 40.4 \\
DetectGPT \cite{mitchell2023_detectgpt} & best-of-3 & 28.5 & 24.3 \\
Random & --- & 25.0 & 33.3 \\
\bottomrule
\end{tabular}}
\end{table}

Convergence confirms the signal resides in the features: three classifiers match within 0.8\,pp (Appendix~\ref{app:learned_estimator}), perplexity features alone recover 66.0\%, and seed replication across three families shows $\Delta{\leq}3.2$\,pp (Appendix~\ref{app:seed_replication}).
Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified (recall ${>}$99\%); errors concentrate at d2/d3 in-distribution and spread to d1--d3 under transfer.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.9\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
\label{fig:confusion_matrix}
\end{figure}

\subsection{Cross-Model Transfer}
\label{sec:gen:crossmodel}

We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).

\begin{table}[t]
\centering
\small
\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%). Ordinal quality: MAE\,=\,0.39, QWK\,=\,0.81 (QWK$_{\text{d1--d3}}$\,=\,0.53); 94.8\% of errors at $|\Delta| \leq 1$.}
\label{tab:cross_model}
\begin{tabular}{lccccc}
\toprule
Holdout & Acc & d0 & d1 & d2 & d3 \\
 & (\%) & Rec. & Rec. & Rec. & Rec. \\
\midrule
Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
\midrule
Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
\bottomrule
\end{tabular}
\end{table}

Mean transfer accuracy is 66.4\% four-class (d1--d3: 55.4\%; $2.7\times$ chance); d0 recall ($>$98\%) inflates the four-class headline, and d2 recall drops to 26.8\% in the worst case (Pythia holdout).

\subsection{Cross-Strategy Transfer}
\label{sec:gen:crossstrategy}

Table~\ref{tab:cross_strategy} reports leave-one-strategy-out transfer.

\begin{table}[t]
\centering
\small
\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
\label{tab:cross_strategy}
\begin{tabular}{lccc}
\toprule
Holdout & Pythia & OLMo & GPT-2 XL \\
 & Acc (\%) & Acc (\%) & Acc (\%) \\
\midrule
nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
\bottomrule
\end{tabular}
\end{table}

Cross-strategy transfer yields 59.1\% four-class (d1--d3: 45.9\%, chance = 33\%), 7\,pp below cross-model transfer.
This gap is itself an empirical finding: different decoding strategies induce structurally distinct degradation trajectories in feature space, not merely noisier versions of the same trajectory.
Training on nucleus + top-$k$ inverts the d1/d2 boundary under temperature (d1v2 AUC $<$ 0.5), because temperature scaling accelerates convergence (\S\ref{sec:method:theory}).
A two-stage pipeline (strategy identification + depth classification) recovers 11.5\,pp, with a 31.5\,pp d1--d3 gap between correct and wrong routing confirming feature-space misalignment (Appendix~\ref{app:extended_discussion}).

\paragraph{Prompted generation.}
Replicating the GPT-2~XL nucleus pipeline with topic-seeded generation yields 69.5\% (95\% CI $[68.9, 70.2]$, $-$13.8\,pp vs.\ BOS-seeded, $2.8\times$ chance), with monotonic AUC decay and identical top features (Appendix~\ref{app:prompted_gen}): prompt conditioning attenuates but does not eliminate the depth signal.

%% ----------------------------------------------------------------
\subsection{Preliminary Cross-Scale Observations}
\label{sec:gen:crossscale}

Depth signal persists at larger scales: 7--8B models achieve 60--70\% and 14B (Qwen2.5-14B) reaches 54.1\% (d1--d3: 57.4\%, chance = 33\%), though confounded by five factors (quantization, sample size, single strategy, vocabulary mismatch, self-reference scoring; Appendix~\ref{app:cross_scale_confounds}).
Cross-model chains (84.75\%) and cross-domain arXiv (74.1\%) confirm robustness at the primary 1--1.5B scale (Appendix~\ref{app:cross_scale_full}).
```

---

**File 2: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex`**

```latex
\section{LoRA Fine-Tuning Protocol}
\label{app:lora_protocol}

Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
The HuggingFace Trainer default linear decay schedule is used with no warmup.
Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.

\begin{table}[h]
\centering
\small
\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
\label{tab:lora_protocol}
\begin{tabular}{@{}ll@{}}
\toprule
Parameter & Value \\
\midrule
LoRA rank $r$ & 16 \\
LoRA alpha $\alpha$ & 32 \\
LoRA dropout & 0.05 \\
Bias & none \\
Epochs per depth & 3 \\
Learning rate & $2 \times 10^{-4}$ \\
LR schedule & linear decay (no warmup) \\
Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
Max sequence length & 512 tokens \\
Precision & bfloat16 \\
Adapter init & from scratch (base model) \\
Seed & 42 (primary), 43 (replication) \\
\bottomrule
\end{tabular}
\end{table}

\section{Additional Results}
\label{app:additional}

\subsection{Top-$k$ Feature Trajectories}
\label{app:topk_trajectories}

Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.

\subsection{Permutation Importance}
\label{app:permutation}

To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.

\subsection{Feature Trajectories}
\label{app:feature_trajectories}

\begin{figure}[h]
\centering
\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
\label{fig:feature_trajectory}
\end{figure}

\subsection{Per-Class Recall}
\label{app:per_class}

Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
Depth~0 recall exceeds 97\% uniformly.
Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.

\begin{table}[h]
\centering
\small
\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
\label{tab:per_class_recall}
\begin{tabular}{@{}lcccc@{}}
\toprule
Cell & d0 & d1 & d2 & d3 \\
\midrule
Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
\bottomrule
\end{tabular}
\end{table}

\subsection{DCOL Iteration Details}
\label{app:dcol_iterations}

Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.

\begin{table}[h]
\centering
\small
\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
\label{tab:dcol_iterations}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
\toprule
Ver. & Backbone & Config & Outcome \\
\midrule
v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
\bottomrule
\end{tabular}}
\end{table}

\subsection{Zero-Shot LLM Prompt Template}
\label{app:zeroshot_prompt}

Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
No in-context examples are provided.

\begin{quote}
\small
\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''

\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
\end{quote}

\subsection{Temperature Robustness}
\label{app:multi_tau}

The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.

\paragraph{Within-$\tau$ robustness.}
For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.

\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.

\paragraph{Cross-$\tau$ non-transferability.}
Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.

\paragraph{Ecological validity.}
On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.

\begin{table}[h]
\centering
\small
\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
\label{tab:multi_tau_within}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lcccc@{}}
\toprule
$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
\midrule
0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
\bottomrule
\end{tabular}}
\end{table}

\begin{table}[h]
\centering
\small
\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
\label{tab:multi_tau_cross}
\begin{tabular}{@{}lcc@{}}
\toprule
Holdout & Acc (\%) & d1v2 AUC \\
\midrule
$\tau{=}0.5$ & 52.2 & 0.176 \\
$\tau{=}0.7$ & 41.0 & 0.299 \\
$\tau{=}0.9$ & 46.4 & 0.277 \\
$\tau{=}1.1$ & 47.1 & 0.525 \\
\midrule
Mean & 46.7 & 0.319 \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Feature Overlap Analysis}
\label{app:feature_overlap}

We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.

\subsection{End-to-End Learning}
\label{app:e2e}

DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.

\begin{table}[h]
\centering
\small
\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
\label{tab:e2e_detail}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lccccc@{}}
\toprule
Method & Acc (\%) & d0 & d1 & d2 & d3 \\
\midrule
DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
\midrule
RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
\bottomrule
\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
\end{tabular}}
\end{table}

\paragraph{Feature space divergence.}
SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.

DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.

\subsection{Domain Bias Analysis}
\label{app:domain_bias}

To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.

\paragraph{Methodological note.}
An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.

\paragraph{Sub-A: Standard CV.}
Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.

\paragraph{Sub-B: LOGO evaluation.}
We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.

\paragraph{Sub-C: Negative control.}
We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.

Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.

\subsection{Wild-Data Calibration}
\label{app:calibration}

Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).

\begin{table}[h]
\centering
\small
\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
\label{tab:calibration}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llrccc@{}}
\toprule
Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
\midrule
Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
\addlinespace
GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
\addlinespace
OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
\bottomrule
\end{tabular}}
\end{table}

On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.

\paragraph{Threshold calibration.}
A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ reduces C4 FPR from 33.4\% to 2.8\% and FineWeb FPR from 16.9\% to 0.7\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.

\subsection{Downstream Curation PoC}
\label{app:curation_poc}

To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.

\begin{table}[h]
\centering
\small
\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
\label{tab:curation_poc}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lcccccc@{}}
\toprule
Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
\midrule
unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
\bottomrule
\end{tabular}}
\end{table}

\begin{table}[h]
\centering
\small
\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
\label{tab:curation_comparisons}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lccc@{}}
\toprule
Comparison & $\Delta$ PPL & $t$ & $p$ \\
\midrule
rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
\bottomrule
\end{tabular}}
\end{table}

RF-based depth filtering (19-feature F1\,=\,0.997) substantially outperforms a simple perplexity-threshold baseline (F1\,=\,0.845) for identifying low-depth passages; the multi-feature representation provides discriminative value beyond raw perplexity.
However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.

\subsection{Reference Model Ablation}
\label{app:ref_ablation}

\begin{table}[h]
\centering
\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
\label{tab:ref_ablation}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lcc@{}}
\toprule
Reference Model & Architecture & Accuracy (\%) \\
\midrule
Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
\bottomrule
\end{tabular}}
\end{table}

\subsection{Cross-Scale Full Results}
\label{app:cross_scale_full}

This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B-Instruct), all under 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth).
The 7--8B models generate depths $d \in \{0, 1, \ldots, 5\}$; the 14B model generates $d \in \{0, 1, 2, 3\}$.
Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).

\paragraph{Scale comparison.}
Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).

\begin{table}[h]
\centering
\small
\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3, nucleus), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
\label{tab:cross_scale}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lccc@{}}
\toprule
Model & 4-class acc & $\mathrm{EDD}_{T{=}0.70}$ & d0v1 AUC \\
\midrule
GPT-2~XL (1.5B) & 84.3 & 4 & 0.999 \\
OLMo-1B & 78.9 & 4 & 0.997 \\
Pythia-1.4B & 78.7 & 4 & 0.998 \\
\midrule
Llama-3.1-8B & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
Qwen2.5-7B & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
\midrule
Qwen2.5-14B$^\dagger$ & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
\bottomrule
\end{tabular}}
\end{table}

\paragraph{(1) Depth signal persists at 7--8B scale.}
Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).

\paragraph{(2) EDD at 7--8B scale.}
At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).

\begin{table}[h]
\centering
\small
\caption{Consecutive binary AUC (nucleus $p{=}0.95$). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below $T{=}0.70$); Qwen2.5-7B shows a U-shaped pattern with all pairs above $T$; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has d0v1 below $T$, yielding $\mathrm{EDD}{=}0$.}
\label{tab:cross_scale_auc}
\begin{tabular}{@{}lccccc@{}}
\toprule
Model & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
\midrule
Llama-3.1-8B & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
Qwen2.5-7B & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
Qwen2.5-14B$^\dagger$ & 0.643 & 0.713 & 0.728 & \multicolumn{2}{c}{--} \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.

\begin{table}[h]
\centering
\small
\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
\label{tab:llama3_base_auc}
\begin{tabular}{lccccc}
\toprule
Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
\midrule
Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
\bottomrule
\end{tabular}
\end{table}

The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.

\paragraph{(4) Signal attenuation at 14B.}
Qwen2.5-14B represents a boundary condition: four-class accuracy drops to 54.1\% (95\% CI $[53.4, 54.7]$, $2.2\times$ chance), with $\mathrm{EDD}_{0.70}{=}0$ because d0-vs-d1 AUC (0.643) falls below the 0.70 threshold (Table~\ref{tab:cross_scale_auc}).
The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), nearly vanishes at 14B.
Inter-depth discrimination at d1--d3 remains comparable: d1v2 AUC (0.713) and d2v3 AUC (0.728) both exceed 0.70, and d1--d3 balanced accuracy reaches 57.4\% (chance = 33\%).
Feature importance undergoes a structural shift: higher-order moments (kurtosis, skewness of perplexity) replace first/second-order statistics (\texttt{p90\_ppl}, variance) as top features, consistent with the theoretical prediction that increased model capacity compresses perplexity tails (\S\ref{sec:method:theory}); first-order tail statistics become less informative while higher-order shape changes persist.
This result carries an important caveat: Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), whereas all other experiments use Pythia-1.4B.
Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.

\paragraph{Caveats.}
For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.

\paragraph{Confounds.}
\label{app:cross_scale_confounds}
Five confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between larger generators and the 1.4B reference model; (5)~Qwen2.5-14B uses self-reference rather than the Pythia-1.4B reference used for all other experiments, preventing direct cross-scale comparison at the 14B data point.
The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.

\subsection{Cross-Boundary Generalization}
\label{app:cross_boundary}

The preceding experiments assume a single model family generates all recursive depths.
In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
We probe whether the depth signal persists under two relaxations of the single-model assumption.

\paragraph{Cross-model recursive chains.}
We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.

\paragraph{Confound discussion.}
The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
We address this confound directly with a reverse-chain control below.

\paragraph{Reverse-chain control.}
To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.

\paragraph{Cross-domain transfer.}
All prior experiments use WikiText-103 as the seed corpus.
To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.

\subsection{Cross-Seed Replication}
\label{app:seed_replication}

Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.

\begin{table}[h]
\centering
\small
\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
\label{tab:seed_replication}
\begin{tabular}{@{}llccc@{}}
\toprule
Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
\midrule
Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
\midrule
OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
\midrule
GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
\bottomrule
\end{tabular}
\end{table}

Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.

\paragraph{Outlier handling.}
Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.

\subsection{Depth-4 Extension}
\label{app:depth4_ext}

We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.

\paragraph{Feature monotonicity at d4.}
For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
This discrepancy illustrates that multi-class classifiers can leverage global distributional structure unavailable to pairwise comparisons.
The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.

\subsection{Generation Length Ablation}
\label{app:length_ablation}

Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).

\begin{table}[h]
\centering
\small
\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
\label{tab:length_ablation}
\begin{tabular}{@{}lc@{}}
\toprule
Passage length (tokens) & Acc (\%) \\
\midrule
128 & 68.35 \\
256 & 73.80 \\
512 & 77.82 \\
\bottomrule
\end{tabular}
\end{table}

Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.

\subsection{Mixed-Depth Corpus}
\label{app:mixed_depth}

Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.
Macro-recall $\Delta$ = $-$1.62\,pp (within the 2\,pp threshold); individual class variations (max 2.43\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.

\subsection{Learned Estimator Comparison}
\label{app:learned_estimator}

Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.

\begin{table}[h]
\centering
\small
\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
\label{tab:learned_estimator}
\begin{tabular}{@{}lcccc@{}}
\toprule
Method & Pythia & OLMo & GPT-2 XL & Mean \\
\midrule
RF (baseline) & --- & --- & --- & 66.4 \\
XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
\bottomrule
\end{tabular}
\end{table}

All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.

\subsection{Instruction-Tuned Model at 1.5B Scale}
\label{app:instruct_1p5b}

To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).

The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.

The top-5 features shift substantially: \texttt{surprisal\_range}, \texttt{surprisal\_position\_corr}, \texttt{prob\_std}, \texttt{surprisal\_first\_half\_minus\_second}, and \texttt{surprisal\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.

Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.

\subsection{Downstream Fine-Tuning Probe}
\label{app:downstream}

We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).

\begin{table}[h]
\centering
\small
\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
\label{tab:downstream}
\begin{tabular}{@{}lcc@{}}
\toprule
Training subset & PPL & $\Delta$ vs.\ baseline \\
\midrule
Baseline (no fine-tuning) & 5.67 & --- \\
d0 only & 5.65 & $-$0.02 \\
d1 only & 5.55 & $-$0.12 \\
d2 only & 5.56 & $-$0.11 \\
Mixed (d0--d3) & 5.55 & $-$0.12 \\
\bottomrule
\end{tabular}
\end{table}

The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.

\subsection{Feature Group Ablation}
\label{app:feature_ablation}

Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.

\begin{table}[h]
\centering
\small
\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
\label{tab:feature_ablation}
\begin{tabular}{@{}lccc@{}}
\toprule
Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
\midrule
Full (all 19) & 19 & 66.6 & --- \\
Perplexity only & 9 & 66.0 & $-$0.5 \\
Entropy/Surprisal only & 5 & 63.2 & $-$3.4 \\
Repetition/Diversity only & 5 & 53.0 & $-$13.6 \\
\midrule
\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.3 \\
\bottomrule
\end{tabular}
\end{table}

The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.5$\,pp), while repetition/diversity features alone fall 13.6\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.

\subsection{RF Seed Robustness}
\label{app:rf_seed}

Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.

\begin{table}[h]
\centering
\small
\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
\label{tab:rf_seed}
\begin{tabular}{@{}lc@{}}
\toprule
Seed & Acc (\%) \\
\midrule
42 & 66.4 \\
123 & 66.5 \\
456 & 66.5 \\
\midrule
Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
\bottomrule
\end{tabular}
\end{table}

The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.

\subsection{Binary Detector Baselines for Ordinal Classification}
\label{app:detector_baselines}

We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.

\paragraph{Binary detectors (Pythia nucleus).}
Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.

\paragraph{Membership inference baselines (all 9 cells).}
DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%).
Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%---matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).

\paragraph{Augmented feature set.}
To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
The 20-feature model (19 + Min-K\%) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.

\subsection{Binoculars Feature Ablation and Signal Decomposition}
\label{app:feature_ablation_bino}

To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).

\begin{table}[h]
\centering
\small
\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
\label{tab:bino_ablation}
\begin{tabular}{@{}lccc@{}}
\toprule
Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
\midrule
6 overlap only & 6 & 75.9 & $-$2.5 \\
Our 19 features & 19 & 78.4 & --- \\
Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
\bottomrule
\end{tabular}
\end{table}

The 6 shared perplexity features alone achieve 75.9\% (97\% of the total above-chance signal), confirming that mean-level perplexity distributional displacement is the core depth signal.
Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.

\paragraph{Strategy-dependent complementarity.}
The merged improvement varies by decoding strategy: nucleus and temperature cells gain +5.1\,pp on average, while top-k cells gain only +2.8\,pp.
Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.

% TODO: Add 14B Binoculars ablation results when available

\subsection{Prompted Generation Results}
\label{app:prompted_gen}

Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.

\begin{table}[h]
\centering
\small
\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
\label{tab:prompted_gen}
\begin{tabular}{@{}lc@{}}
\toprule
Metric & Value \\
\midrule
4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
BOS-seeded baseline (\%) & 83.3 \\
$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
\midrule
AUC d0v1 & 0.916 \\
AUC d1v2 & 0.782 \\
AUC d2v3 & 0.744 \\
\midrule
Top-1 feature & \texttt{p90\_ppl} \\
Top-2 feature & \texttt{var\_surprisal} \\
Top-3 feature & \texttt{p75\_ppl} \\
\bottomrule
\end{tabular}
\end{table}

The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.

\subsection{Extended Discussion}
\label{app:extended_discussion}

\paragraph{Cross-strategy conditional decomposition.}
The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.

\paragraph{Depth-graduated curation (inconclusive preliminary evidence).}
Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
Recursive generation depth estimation could enable a finer-grained alternative: retain low-depth generations (d1) while down-weighting high-depth text (d3+) where tail erosion has degraded quality.
A pilot study (Appendix~\ref{app:curation_poc}) yields inconclusive evidence: the RF-vs-unfiltered comparison is not significant ($p>0.4$), though RF-filtered subsets outperform size-matched random subsampling ($p<0.001$--$0.02$ before Bonferroni correction; $p<0.003$--$0.06$ after correction at $\alpha{=}0.05/3{=}0.017$, with 1 of 3 comparisons surviving).
The d1/d2 boundary inversion under cross-strategy transfer further limits practical curation without strategy metadata.
Large-scale validation is needed before depth-graduated filtering can be considered practical.

\paragraph{Toward a provenance toolkit.}
Depth estimation complements existing provenance methods along orthogonal axes.
Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.

\subsection{Computational Resources and Reproducibility}
\label{app:compute}

\paragraph{Hardware.}
All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B QLoRA experiments, and all ablations.

\paragraph{Software.}
Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).

\paragraph{Hyperparameters.}
LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.

\paragraph{Inference cost.}
Feature extraction requires a single forward pass of the reference model.
On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
RF classification adds negligible overhead ($<$1\,s).
```

---

**File 3: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex`**

```latex
\section{Discussion and Conclusion}
\label{sec:discussion}

This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}); cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while binary detectors and membership inference methods achieve only 30--35\%.

\paragraph{Accumulation settings.}
Our primary benchmark uses full-replacement chains; in practice, model training involves accumulation, mixing human data with synthetic outputs at unknown proportions \cite{gerstgrasser2024_accumulate}.
Under accumulation (GPT-2~XL, nucleus), both 50/50 and 25/75 human-synthetic mixing conditions achieve comparable accuracy (${\sim}$69--70\%), down from 84.2\% under full replacement.
The attenuation is substantial (${\sim}$15\,pp) but depth estimation remains $2.8{\times}$ chance; the 1\,pp gap between mixing ratios falls within cross-seed variance (2.04\,pp) and should not be interpreted as a trend.
Extending the feature set to handle continuous mixing ratios is a direction for future work.

\paragraph{Scale and deployment implications.}
The depth signal attenuates with model scale: at 14B, d0/d1 separability drops sharply ($\mathrm{EDD}_{0.70}{=}0$), though d1--d3 discrimination persists above chance.
This suggests that depth estimation complements rather than replaces binary detection for practical data auditing: binary detectors handle the human-vs-machine boundary where depth estimation is redundant ($>$97\% d0 recall), while depth estimation provides the finer ordinal resolution that binary methods cannot.
A practical deployment path proceeds from controlled settings, where model and strategy are known, to partially known settings via strategy-identification routing, to fully unknown settings requiring strategy-invariant features (Appendix~\ref{app:extended_discussion}).

\paragraph{Multi-channel depth encoding.}
Feature ablation reveals that ordinal depth signal decomposes into channels with decreasing contribution (Appendix~\ref{app:feature_ablation_bino}).
The 6 core perplexity features shared between our pipeline and Binoculars (mean, variance, median, p10, p90, skewness) achieve 75.9\% alone---97\% of the total above-chance signal.
Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) add +2.3\,pp; Binoculars' 5 unique cross-model features add +4.3\,pp when merged, yielding 82.6\%.
The merged improvement is strategy-dependent: nucleus and temperature cells gain +5.1\,pp on average, while top-k cells gain only +2.8\,pp, suggesting that top-k truncation limits the information available to cross-model divergence features.
That two independent feature pipelines---one designed for depth estimation, one for binary detection---converge to within 0.3\,pp validates ordinal depth as a genuine multi-channel distributional phenomenon.

\paragraph{Open challenges.}
Cross-strategy transfer (d1--d3: 45.9\%) remains the primary bottleneck, driven by structurally distinct feature-space trajectories across decoding strategies.
Scale-dependent signal attenuation and depth-quality entanglement are open challenges.
```

---

**File 4: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex`**

```latex
\section{Introduction}
\label{sec:intro}

The text on which large language models are trained increasingly contains their own outputs.
As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.

Existing tools address adjacent but distinct problems.
Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.

We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
Specifically, the perplexity tail feature family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance emerge as dominant depth indicators, with group-level dominance robust across all 9 model--strategy configurations and three importance measures.
The sole 8B instruction-tuned model tested (Llama-3.1-8B-Instruct) exhibits monotonically decreasing AUC, in contrast to the non-monotonic trajectory of its base-model counterpart; whether this regularization effect generalizes across architectures remains open (Appendix~\ref{app:cross_scale_full}).

Following the tradition of benchmark-driven empirical studies in NLP, our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty; the convergence of multiple classifiers (RF, XGBoost, LightGBM within 0.4\,pp; \S\ref{sec:gen:baselines}) confirms that discriminative signal resides in feature design, not classifier architecture.
We formalize recursive generation depth estimation as ordinal classification and introduce a lightweight pipeline: compute 19 reference-model statistical features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K samples).
The atlas reveals strategy-dependent degradation trajectories and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.

Our contributions are:
\begin{itemize}[nosep,leftmargin=*]
    \item \textbf{Task formalization and benchmark.} We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark ($3$ model families $\times$ $3$ decoding strategies $\times$ $4$ depths).

    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family dominates depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}4$ for all three families, validated by 5-class (d0--d4) extension (71--80\%); at $T{=}0.75$, Pythia achieves $p{=}0.001$ with graded confidence across families.

    \item \textbf{Generalization and cross-strategy analysis.} Cross-model LOO 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, single-cell prompted 69.5\%, preliminary cross-scale at 7--14B (54\% Qwen2.5-14B to 70\% Llama-3.1-8B, confounded by architecture and precision; \S\ref{sec:gen:crossscale}). We identify a structural barrier in cross-strategy transfer (59.1\%, d1--d3: 45.9\%): decoding strategies induce qualitatively distinct degradation trajectories, with d1/d2 boundary inversion under strategy mismatch.

    \item \textbf{Feature convergence analysis.} Independent cross-perplexity features (Binoculars) converge to matching ordinal accuracy (78.1\% vs.\ our 78.4\%); merging both feature sets yields 82.6\%, decomposing the depth signal into three channels: perplexity displacement (97\% of above-chance signal), distributional shape (+2.3\,pp), and cross-model divergence (+4.3\,pp).
\end{itemize}
```

---

**File 5: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex`**

```latex
\begin{abstract}
As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement recursive chains at the 1--1.5B scale.
A Random Forest over statistical features dominated by the perplexity tail family achieves d1--d3 balanced accuracy of 59--82\% (four-class: 69--86\%) across nine model--strategy cells; convergence of RF, XGBoost, and LightGBM confirms that discriminative signal resides in feature design, not classifier choice.
Cross-model transfer reaches 66.4\%, cross-domain arXiv 74.1\%, and cross-strategy transfer 59.1\%; the gap reveals that decoding strategies induce structurally distinct degradation trajectories, formalized via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families).
Perturbation-based and membership inference baselines (29--33\%) fall far below our pipeline; cross-perplexity features (Binoculars) converge to matching performance (78.1\% vs.\ 78.4\%), and merging both feature sets yields 82.6\%, decomposing the depth signal into perplexity displacement, distributional shape, and cross-model divergence channels.
\end{abstract}
```

---

All 5 files returned in full. Note: the correct paths are directly under `docs/paper/` (not `docs/paper/sections/`).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ddfa02e-4232-4d9b-bac2-55a48fd3a759",
  "isSidechain": true,
  "agentId": "a9375da6d3d942d71",
  "requestId": "req_011CbCfP4qVyg6v5xCPdyiwM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0141c38c-972e-4bfa-b171-71da9865ee86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/reviewer_2647e3b4",
  "sessionId": "c3d895c8-8417-4ec9-8d44-c18f604a54ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lively-singing-hellman",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvmCbBtWnpdJYDgKZ6D3y6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29282,
      "cache_read_input_tokens": 30077,
      "output_tokens": 26727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26727,
          "cache_read_input_tokens": 30077,
          "cache_creation_input_tokens": 29282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29282,
            "ephemeral_1h_input_tokens": 0
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
