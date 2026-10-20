# Research conversation: I need to find: ## A) Current top open-source models for process reward modeling and math reasoning (as of May 2026) Sea

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 103
- **Recorded user turns:** 1
- **Tool calls:** 47
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7fcd55ce3613e611.jsonl`
- **Structured JSON:** [`f77179134f3de2cdd66b.json`](../../sessions/f7/f77179134f3de2cdd66b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

103 recorded events

### User

_source line 1 · 2026-05-27T08:04:18.169Z_

I need to find:

## A) Current top open-source models for process reward modeling and math reasoning (as of May 2026)

Search for:
1. "best open source process reward model 2026"
2. "top process reward model PRM leaderboard 2026"
3. "open source math reasoning model 2026 state of the art"
4. "Qwen math model 2026"
5. "DeepSeek math model 2026"  
6. "Llama math reasoning 2026"
7. "PRMBench leaderboard results 2026"
8. "process reward model benchmark scores 2026"

## B) Baseline numbers to beat

Search for:
1. "PRMBench scores process reward model"
2. "ProcessBench results 2025 2026"
3. "process reward model accuracy MATH dataset 2026"
4. "best of N process reward model math accuracy 2026"

## C) Similar implementations on GitHub

Search for:
1. "github premise dependency reward model"
2. "github contrastive process reward model"
3. "github DAG math reasoning verification"
4. "github PERL premise extraction reasoning"

## D) Hardware/data requirements for similar experiments

Search for:
1. "process reward model training GPU hours cost"
2. "contrastive learning reward model compute requirements"
3. "PRM training data size math-shepherd"

Report all findings comprehensively with specific numbers, model names, and URLs where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "85da456b-bbe8-4a78-9d2a-3d25d3b5efa4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T08:04:18.173Z_

```json
{
  "parentUuid": "85da456b-bbe8-4a78-9d2a-3d25d3b5efa4",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "ba8b01ce-19f7-4db6-8d6b-19ad96529acd",
  "timestamp": "2026-05-27T08:04:18.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T08:04:18.173Z_

```json
{
  "parentUuid": "ba8b01ce-19f7-4db6-8d6b-19ad96529acd",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5aa83985-dc6b-46f8-8622-58944c3d42c6",
  "timestamp": "2026-05-27T08:04:18.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T08:04:25.541Z_



I'll conduct a comprehensive web search across all these queries. Let me start by loading the WebSearch tool, then run the searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aa83985-dc6b-46f8-8622-58944c3d42c6",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj5r1Nj7y1T4xdtKnPw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8975f94-734f-4d75-8a5e-002e01e38d6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS6t3cA4xigvDXup3eBAr1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1686,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1686,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-27T08:04:26.297Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B6noBkBnTeGFBAoPBik1Km`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8975f94-734f-4d75-8a5e-002e01e38d6a",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj5r1Nj7y1T4xdtKnPw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7cb0435-5684-41b0-bbd6-d45b03059963",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS6t3cA4xigvDXup3eBAr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1686,
      "cache_read_input_tokens": 7411,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1686
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1686,
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

_source line 6 · 2026-05-27T08:04:26.305Z_

<details><summary>↩ Tool result · `toolu_01B6noBkBnTeGFBAoPBik1Km`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7cb0435-5684-41b0-bbd6-d45b03059963",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "ab7493d4-49ce-4f74-99ac-2115862eac7a",
  "sourceToolAssistantUUID": "e7cb0435-5684-41b0-bbd6-d45b03059963",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T08:04:32.679Z_



Now let me run all the searches in parallel batches. I'll start with Section A and B searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab7493d4-49ce-4f74-99ac-2115862eac7a",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "644ddbdd-d7fc-44c7-a270-8586045d23af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-27T08:04:33.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DT6XjwMd8PRFBffyTyRCrT`</summary>

```json
{
  "query": "best open source process reward model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644ddbdd-d7fc-44c7-a270-8586045d23af",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "635b8878-c2c7-4fce-9a5d-cea4a7e1ae16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-27T08:04:34.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNC8UYHNq7XLM6vVBpnczd`</summary>

```json
{
  "query": "top process reward model PRM leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635b8878-c2c7-4fce-9a5d-cea4a7e1ae16",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d9a8a2-15ad-4060-a578-3d400e0dc0a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-27T08:04:34.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dyaj2Xuhampm4ktdHGuqwp`</summary>

```json
{
  "query": "open source math reasoning model 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d9a8a2-15ad-4060-a578-3d400e0dc0a2",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceba5a53-86a4-4400-b1b9-a40a522476f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-27T08:04:35.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BVB8FXckk1Wo5ExoGkbJkR`</summary>

```json
{
  "query": "Qwen math model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceba5a53-86a4-4400-b1b9-a40a522476f2",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eea04bd-c61d-441f-813e-74f35a9cadf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 12 · 2026-05-27T08:04:35.560Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EvBtRRy6m6NizuyhLhcZxS`</summary>

```json
{
  "query": "DeepSeek math model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eea04bd-c61d-441f-813e-74f35a9cadf0",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e3d358e-6a20-411c-ab59-825a8e0ccd41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 13 · 2026-05-27T08:04:36.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qzd9bGrqK4u1vAfTvunuBS`</summary>

```json
{
  "query": "Llama math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e3d358e-6a20-411c-ab59-825a8e0ccd41",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaac4d47-78c6-4f93-8f8d-b4f9d1f918b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 14 · 2026-05-27T08:04:36.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AksczXQzPa3WMaoDBwMyft`</summary>

```json
{
  "query": "PRMBench leaderboard results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaac4d47-78c6-4f93-8f8d-b4f9d1f918b6",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e80dcfd-9013-488b-8da2-e4f2ba26fc17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 15 · 2026-05-27T08:04:36.665Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UwEGKuQ44J3bLh1797fYiG`</summary>

```json
{
  "query": "process reward model benchmark scores 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e80dcfd-9013-488b-8da2-e4f2ba26fc17",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj6T2HwieJ1xrKhmT2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e6e7253-891a-45cd-9faa-566366005dfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JFeveMLCgDGhyYs8yzboB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 9097,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 391,
          "cache_read_input_tokens": 9097,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1134,
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

_source line 16 · 2026-05-27T08:04:42.378Z_

<details><summary>↩ Tool result · `toolu_01EvBtRRy6m6NizuyhLhcZxS`</summary>

```text
Web search results for query: "DeepSeek math model 2026"

Links: [{"title":"DeepSeekMath-V2: How Self-Verifiable AI Models Transform Math APIs","url":"https://apidog.com/blog/deepseekmath-v2/"},{"title":"DeepSeek launches new math-oriented model to solve secrets of the universe - Neowin","url":"https://www.neowin.net/news/deepseek-launches-new-math-oriented-model-to-solve-secrets-of-the-universe/"},{"title":"DeepSeek Math V2 Is Quietly Building the Future of AI - Here's Why It Matters | Christopher S. Penn - Marketing AI Keynote Speaker","url":"https://www.christopherspenn.com/2026/01/deepseek-math-v2-is-quietly-building-the-future-of-ai-heres-why-it-matters/"},{"title":"DeepSeek","url":"https://www.deepseek.com/en/"},{"title":"DeepSeek Math V2: Open-Source AI for Math Reasoning","url":"https://tech-now.io/en/blogs/deepseek-math-v2-the-open-source-ai-model-redefining-mathematical-reasoning"},{"title":"DeepSeek’s self-correcting AI model aces tough maths proofs","url":"https://www.nature.com/articles/d41586-025-03959-9"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open   Language Models","url":"https://arxiv.org/pdf/2402.03300"},{"title":"deepseek-ai/DeepSeek-Math-V2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Math-V2"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.22570"}]

Based on the search results, here's what I found about DeepSeek's math model in 2026:

## DeepSeekMath-V2

DeepSeek unveiled DeepSeekMath-V2, a specialized AI model built to solve and self-verify complex mathematical theorems. The model combines a massive 685B-parameter architecture with robust self-verification mechanisms, enabling developers to tackle theorem proving, automated grading, and open mathematical problems through accessible APIs.

### Key Features

The model aims to achieve self-verifiable mathematical reasoning and rigorous step-by-step derivation, with a focus on theorem proving, moving beyond reliance on correct final numerical answers. The company said that its new model uses a generation-verification loop, with an accurate LLM-based verifier trained for theorem proving, and a proof generator trained using the verifier as the reward model.

### Performance

The model achieves gold-medal-level performance on the world's toughest math challenges, including the International Mathematical Olympiad (IMO) 2025. On the Putnam 2024 undergraduate competition, it scored 118/120, exceeding the highest score of 90 obtained by human participants.

DeepSeekMath-V2 is built on top of DeepSeek-V3.2-Exp-Base and is available as an open-source model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e3d358e-6a20-411c-ab59-825a8e0ccd41",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "5c3f0f26-e29b-4e78-856a-41e75bd6f213",
  "sourceToolAssistantUUID": "7e3d358e-6a20-411c-ab59-825a8e0ccd41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T08:04:42.892Z_

<details><summary>↩ Tool result · `toolu_01DNC8UYHNq7XLM6vVBpnczd`</summary>

```text
Web search results for query: "top process reward model PRM leaderboard 2026"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/html/2601.12294v1"},{"title":"GitHub - allenai/reward-bench: RewardBench: the first evaluation tool for reward models. · GitHub","url":"https://github.com/allenai/reward-bench"},{"title":"OR-PRM: A Process Reward Model for Algorithmic Problem in Operations Research | OpenReview","url":"https://openreview.net/forum?id=tFEAzYdz92"},{"title":"Process Reward Model with Q-value Rankings | OpenReview","url":"https://openreview.net/forum?id=wQEdh2cgEk"},{"title":"Reward Bench Leaderboard - a Hugging Face Space by allenai","url":"https://huggingface.co/spaces/allenai/reward-bench"},{"title":"VRPRM: Process Reward Modeling via Visual Reasoning | OpenReview","url":"https://openreview.net/forum?id=sj9jmrBjMf"},{"title":"What are the best PRM software solutions out there 2026?","url":"https://partnerplace.io/knowledge-base/what-are-the-best-prm-software-solutions-out-there-2026"}]

Based on the search results, here are the key findings about Process Reward Model (PRM) leaderboards in 2026:

## Major PRM Benchmarks and Leaderboards

**PRMBench**: PRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs, comprising 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity. The experiments evaluated 15 models, spanning both open-source PRMs and closed-source large language models prompted as critic models.

**ToolPRMBench**: This benchmark includes a series of LLMs, general PRMs, and tool-using specialized PRMs, building a comprehensive PRMs leaderboard in the tool-using scenario. ToolPRM-GRPO achieves the best average accuracy among all non-API models, outperforming even the API-based LLMs, while ToolPRM-CoT and ToolPRM-Base further show that reward models explicitly trained for tool-using substantially outperform both open-source LLMs and general-purpose PRMs.

**Notable Recent Models (2025-2026)**:
- ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs, and outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K.

The search results show active development in the PRM field with multiple specialized models emerging for different domains and use cases throughout 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d9a8a2-15ad-4060-a578-3d400e0dc0a2",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "b29e7d4a-b512-4bf9-a77d-812df7ebf8ae",
  "sourceToolAssistantUUID": "54d9a8a2-15ad-4060-a578-3d400e0dc0a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T08:04:42.995Z_

<details><summary>↩ Tool result · `toolu_01Dyaj2Xuhampm4ktdHGuqwp`</summary>

```text
Web search results for query: "open source math reasoning model 2026 state of the art"

Links: [{"title":"Best Open Source LLM For Math In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"Ultimate Guide - The Best Open Source LLMs for Reasoning in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning"},{"title":"OpenThoughts: Data Recipes for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=7xjoTuaNmN"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"2025-4-24 AIMO-2 Winning Solution: Building","url":"https://arxiv.org/pdf/2504.16891"}]

Based on the search results, here are the state-of-the-art open source math reasoning models for 2026:

## Top Open Source Math Reasoning Models

The top three recommendations for 2026 are DeepSeek-R1, Qwen/QwQ-32B, and THUDM/GLM-Z1-9B-0414.

### DeepSeek-R1
DeepSeek-R1-0528 is a reasoning model powered by reinforcement learning that achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks, with 671B total parameters in its MoE architecture and 164K context length.

A compact version also shows impressive results: DeepSeek-R1-Distill-Qwen3-8B outperforms Google's Gemini 2.5 Flash on AIME 2025 mathematical reasoning tasks and nearly matches Microsoft's Phi 4 reasoning model on HMMT benchmarks.

### Other Notable Models

OpenThinker3-7B achieves state-of-the-art results with 53% on AIME 2025, 51% on LiveCodeBench 06/24-01/25, and 54% on GPQA Diamond.

OpenAI's gpt-oss-120B is a 117B-parameter open-weight model with chain-of-thought access, and Qwen3-235B-Instruct-2507 offers 1M+ token context with state-of-the-art multilingual reasoning and instruction following.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceba5a53-86a4-4400-b1b9-a40a522476f2",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "26bcf6df-8faf-45bd-b20e-88cc828356f1",
  "sourceToolAssistantUUID": "ceba5a53-86a4-4400-b1b9-a40a522476f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T08:04:43.812Z_

<details><summary>↩ Tool result · `toolu_01Qzd9bGrqK4u1vAfTvunuBS`</summary>

```text
Web search results for query: "Llama math reasoning 2026"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"Best LLM for Math 2026 - AI Model Benchmark Comparison","url":"https://pricepertoken.com/leaderboards/math"},{"title":"Best Math LLMs (2026): Equations, Proofs, Reasoning","url":"https://alignify.co/tools/llm-for-math"},{"title":"Best Ollama Models 2026: 15 Ranked (Coding, Reasoning, Chat) | Local AI Master","url":"https://localaimaster.com/blog/best-ollama-models"},{"title":"【Proposal】MathLLaMA: A Specialized Language Model for Mathematical Reasoning and Problem-Solving | OpenReview","url":"https://openreview.net/forum?id=61OPn1Y5u2&noteId=9gIeYGCc91"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Math Education Digital Shadows for facilitating learning with LLMs: Math performance, anxiety and confidence in simulated students and AIs","url":"https://arxiv.org/html/2604.27618v1"},{"title":"Launch The Llama - Play with Math Games","url":"https://www.mathgames.com/play/launch-the-llama.html"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"MathLLaMA: A Specialized Language Model for ...","url":"https://openreview.net/pdf?id=61OPn1Y5u2"}]

Based on the search results, here's what I found about Llama math reasoning in 2026:

## Llama Models and Math Reasoning Performance

Llama is among the open frontier models being compared for reasoning capabilities, and there are several developments in this area:

### Llama 3.3 and Recent Releases
Llama 3.3 70B is noted as the best overall model if you have 48GB+ VRAM/RAM, and it ranks among the top Ollama models for chat alongside other specialized options like Qwen 2.5 Coder and DeepSeek R1.

### Llama 4 Series
More recently, Llama 4 Maverick, a 17 billion active parameter model with 128 experts, is the best multimodal model in its class, beating GPT-4o and Gemini 2.0 Flash across a broad range of widely reported benchmarks, while achieving comparable results to DeepSeek v3 on reasoning and coding.

Additionally, Llama 4 Behemoth, a 288B active parameter model, offers state-of-the-art performance for non-reasoning models on math, multilinguality, and image benchmarks.

### Training Improvements
A key learning in Llama 4's development was that SFT and DPO can over-constrain the model, restricting exploration during online RL and leading to suboptimal accuracy, particularly in reasoning, coding, and math domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaac4d47-78c6-4f93-8f8d-b4f9d1f918b6",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "e5f1ad4f-c458-4170-a5c3-b46f9686c6e8",
  "sourceToolAssistantUUID": "eaac4d47-78c6-4f93-8f8d-b4f9d1f918b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:04:46.687Z_

<details><summary>↩ Tool result · `toolu_01UwEGKuQ44J3bLh1797fYiG`</summary>

```text
Web search results for query: "process reward model benchmark scores 2026"

Links: [{"title":"RewardBench 2: Advancing Reward Model Evaluation | OpenReview","url":"https://openreview.net/forum?id=fb0G86Dewb"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent","url":"https://arxiv.org/html/2510.18596v1"},{"title":"Paper page - ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://huggingface.co/papers/2601.12294"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"}]

Based on the search results, here's what I found regarding process reward model benchmark scores in 2026:

## Key Benchmarks and Recent Scores

RewardBench 2 is a new multi-skill reward modeling benchmark where models score about 20 points on average lower compared to its predecessor.

ThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search, and surpasses discriminative verifiers trained with the full PRM800K by 8% and 4.5% respectively on out-of-domain evaluations over subsets of GPQA-Diamond and LiveCodeBench.

## Performance Evaluation Methods

PRM performance is assessed at both the step and solution levels using standard F1 metrics for correctly labeling steps, and a composite PRMScore combining positive and negative F1. Best-of-N selection evaluates how well the PRM can select or rerank correct solutions from a pool of candidates, with high BoN accuracy underpinning most of the performance gains achieved by PRMs in test-time scaling.

## Emerging Benchmarks

Other notable benchmarks include PRMBench, which focuses on fine-grained evaluation of step correctness and PRM performance systematically, as current benchmarks primarily focus on step correctness, and CUARewardBench for evaluating process reward models on computer-using agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e6e7253-891a-45cd-9faa-566366005dfc",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "549a9942-14c1-452c-b919-8986dec5f338",
  "sourceToolAssistantUUID": "7e6e7253-891a-45cd-9faa-566366005dfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T08:04:48.980Z_

<details><summary>↩ Tool result · `toolu_01BVB8FXckk1Wo5ExoGkbJkR`</summary>

```text
Web search results for query: "Qwen math model 2026"

Links: [{"title":"Qwen 3.7 Max: Alibaba's New Flagship AI Model 2026","url":"https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026"},{"title":"Qwen Studio","url":"https://qwen.ai/blog?id=qwen2-math"},{"title":"Qwen/Qwen2-Math-72B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2-Math-72B"},{"title":"GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Math"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Deploy Qwen-Math-Plus for Advanced Mathematical Reasoning via API - Model Studio - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/model-studio/math-language-model"},{"title":"Qwen2.5-Math: The world's leading open-sourced mathematical LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math/"},{"title":"Qwen 3.7 Max Developer Guide: 1M Context, $2.50/MTok, and the Anthropic-Protocol Drop-In (2026)","url":"https://ofox.ai/blog/qwen3-7-max-developer-guide-2026/"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"}]

Based on the search results, here's what I found about Qwen math models in 2026:

## Qwen 3.7 Max (May 2026)

Alibaba shipped Qwen 3.7 Max-Preview on May 19, 2026 with a 1M-token context window, native Anthropic Messages support, and pricing below Claude Opus 4.7. 

**Performance on Math:**
It scores 97.1 on HMMT 2026 February, and the Preview variant placed #7 in Math on the Arena leaderboard.

**Pricing:** $2.50/$7.50 per million tokens with a 90% cached-input discount ($0.25/M).

## Earlier Qwen Math Models

Before the 2026 release, Alibaba also developed specialized math models:

- **Qwen2.5-Math:** The Qwen2.5-Math-72B-Instruct model outperforms the Qwen2-Math-72B-Instruct model by an average margin of 4.4 and 6.1 points in English and Chinese, respectively, establishing itself as the best open-source mathematical model currently available.

- **Qwen3:** The flagship model, Qwen3-235B-A22B, achieves competitive results in benchmark evaluations of coding, math, general capabilities, etc., when compared to other top-tier models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eea04bd-c61d-441f-813e-74f35a9cadf0",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "c5a24a4e-4703-4692-bc00-f5e112954e3a",
  "sourceToolAssistantUUID": "8eea04bd-c61d-441f-813e-74f35a9cadf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T08:04:50.737Z_

<details><summary>↩ Tool result · `toolu_01AksczXQzPa3WMaoDBwMyft`</summary>

```text
Web search results for query: "PRMBench leaderboard results 2026"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"GitHub - ssmisya/PRMBench: [ACL' 25] The official code repository for PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models.","url":"https://github.com/ssmisya/PRMBench"},{"title":"SWE-bench & LiveCodeBench Leaderboard (March 2026) — AI Coding Benchmarks | BenchLM.ai","url":"https://benchlm.ai/coding"},{"title":"LiveCodeBench Leaderboard 2026 - Compare AI Model Scores","url":"https://pricepertoken.com/leaderboards/benchmark/livecodebench"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"}]

Based on the search results, I found information about PRMBench, though the 2026 leaderboard data appears to be from the official project page.

The PRMBench leaderboard displays overall results of different models on process-level reward models. The benchmark evaluates models across multiple task types including Non-Redundancy, Non-Circular Logic, Empirically Soundness, Step Consistency, Domain Consistency, Confidence Invariance, Prerequisite Sensitivity, Deception Resistance, and Multi-Solution Consistency.

Qwen2.5-Math-PRM-7B became the new state-of-the-art for open-source PRMs on PRMBench as of January 2025, and Qwen2.5-Math-PRM-72B results were added more recently.

For the most current and detailed leaderboard results, you can visit the official PRMBench project page at https://prmbench.github.io/, which maintains the live leaderboard with specific model performance metrics across all evaluation categories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e80dcfd-9013-488b-8da2-e4f2ba26fc17",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "deb97f38-76ca-452e-993b-feee779d734a",
  "sourceToolAssistantUUID": "2e80dcfd-9013-488b-8da2-e4f2ba26fc17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T08:04:52.338Z_

<details><summary>↩ Tool result · `toolu_01DT6XjwMd8PRFBffyTyRCrT`</summary>

```text
Web search results for query: "best open source process reward model 2026"

Links: [{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Skywork-Reward-V2: Leading the New Milestone for Open-Source Reward Models","url":"https://ai-techpark.com/skywork-reward-v2-leading-the-new-milestone-for-open-source-reward-models/"},{"title":"GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub","url":"https://github.com/RLHFlow/RLHF-Reward-Modeling"},{"title":"GitHub - Gen-Verse/OpenClaw-RL: OpenClaw-RL: Train any agent simply by talking · GitHub","url":"https://github.com/Gen-Verse/OpenClaw-RL"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"On the Importance of Open Sourcing Reward Models","url":"https://www.lesswrong.com/posts/nTy48zvBPPttoLhdJ/on-the-importance-of-open-sourcing-reward-models"},{"title":"Reward Modeling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/05-reward-models"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Reward Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/reward-models"},{"title":"OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees | OpenReview","url":"https://openreview.net/forum?id=fGIqGfmgkW"}]

Based on the search results, here are some of the best open-source process reward models and related systems in 2026:

## Leading Process Reward Models

VersaPRM is a multi-domain process reward model via synthetic reasoning data released in February 2025 with code, model, and data available. This represents one of the latest advancements in the field.

Other notable recent process reward models include OpenPRM (Building Open-domain Process-based Reward Models with Preference Trees), which was accepted to ICLR 2025, and FreePRM (Training Process Reward Models Without Ground Truth Process Labels), released in June 2025.

## General Reward Model Approaches

For broader reward modeling, Skywork-Reward-V2 demonstrates broad applicability and excellent performance across multiple capability dimensions and achieved leading results in multiple advanced capability evaluations, including Best-of-N (BoN) tasks, bias resistance capability testing (RM-Bench), complex instruction understanding, and truthfulness judgment (RewardBench v2).

ArmoRM is the Rank #1 8B model on RewardBench, and the top-3 open-source 8B reward models on RewardBench (ArmoRM, Pair Pref. Model, BT RM) were all trained using the RLHFlow RLHF-Reward-Modeling repository.

Decision-Tree-Reward-Gemma-2-27B achieves the new state-of-the-art score (95.4%) on RewardBench.

These models represent the cutting edge of open-source reward modeling as of 2026, with particular emphasis on process-based approaches for complex reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "635b8878-c2c7-4fce-9a5d-cea4a7e1ae16",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "13c3b271-1945-4f69-8f7b-03684ace1c53",
  "sourceToolAssistantUUID": "635b8878-c2c7-4fce-9a5d-cea4a7e1ae16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T08:04:54.805Z_

Now let me run the Section B and C searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13c3b271-1945-4f69-8f7b-03684ace1c53",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef15060f-ed6a-435d-88c5-47b7c48dd719",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 25 · 2026-05-27T08:04:55.660Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164WdqviRdFue7eUZ4A6Ji7`</summary>

```json
{
  "query": "PRMBench scores process reward model specific numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef15060f-ed6a-435d-88c5-47b7c48dd719",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09039f93-aa05-47af-b66e-9c2a63669179",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 26 · 2026-05-27T08:04:55.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015j2J8cEC2349j8oUm3yY8J`</summary>

```json
{
  "query": "ProcessBench results 2025 2026 accuracy scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09039f93-aa05-47af-b66e-9c2a63669179",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b4a2d44-099b-4937-bd6a-7f9a8965f934",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 27 · 2026-05-27T08:04:56.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NNrenfYSy2Faw5AChu8fur`</summary>

```json
{
  "query": "process reward model accuracy MATH dataset best of N 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b4a2d44-099b-4937-bd6a-7f9a8965f934",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5368100-1692-4c48-8cda-889464f530d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 28 · 2026-05-27T08:04:56.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EZQkG5avtQF1ADpg6bwjJV`</summary>

```json
{
  "query": "best of N process reward model math accuracy results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5368100-1692-4c48-8cda-889464f530d5",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be14450e-7f84-44c9-b9d7-1ccec6d4e900",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 29 · 2026-05-27T08:04:57.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPQL9mMMmeq5pXF59bvmC9`</summary>

```json
{
  "query": "github premise dependency reward model math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be14450e-7f84-44c9-b9d7-1ccec6d4e900",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb8b121d-3df1-45bc-8389-1c7de460c618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 30 · 2026-05-27T08:04:57.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATCgLmGGt5z1L8TadvEPzg`</summary>

```json
{
  "query": "github contrastive process reward model training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb8b121d-3df1-45bc-8389-1c7de460c618",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a33c339-eda0-47d0-943d-9ed6f038703e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 31 · 2026-05-27T08:04:58.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QaW4WsAGMvfWKMJwd61QiL`</summary>

```json
{
  "query": "github DAG math reasoning verification reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a33c339-eda0-47d0-943d-9ed6f038703e",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee4a8aa7-4960-4755-991a-b65c38880473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 32 · 2026-05-27T08:04:59.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWTdBpzgZkFyxfyxFtMPBW`</summary>

```json
{
  "query": "github PERL premise extraction reasoning verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4a8aa7-4960-4755-991a-b65c38880473",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj8N7vQraKP3aaBCyLG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e603e1d3-b27e-4f45-9043-5d8945d0c690",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xz5e89XAQMPTXjqeV6bQro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5602,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 10231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 33 · 2026-05-27T08:05:01.976Z_

<details><summary>↩ Tool result · `toolu_0164WdqviRdFue7eUZ4A6Ji7`</summary>

```text
Web search results for query: "PRMBench scores process reward model specific numbers"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"[Literature Review] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://www.themoonlight.io/en/review/prmbench-a-fine-grained-and-challenging-benchmark-for-process-level-reward-models"},{"title":"Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://huggingface.co/papers/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://arxiv.org/html/2505.23474v1"}]

Based on the search results, here are the specific PRMBench scores and numbers for process reward models:

## PRMBench Dataset Specifications

PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

## Model Performance Scores

PathFinder-PRM achieves a state-of-the-art PRMScore of 67.7, outperforming the prior best score of 65.5.

In related research on another PRM benchmark, Qwen2.5-Math-PRM, the highest-performing PRM, attained a score of 68.0.

R-PRM surpasses strong baselines by 11.9 and 8.5 points in F1 scores on ProcessBench and PRMBench, respectively.

## Evaluation Categories

The benchmark evaluates models across task types including Non-Redundancy, Non-Circular Logic, Empirically Soundness, Step Consistency, Domain Consistency, Confidence Invariance, Prerequisite Sensitivity, Deception Resistance, and Multi-Solution Consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09039f93-aa05-47af-b66e-9c2a63669179",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "5e5cb25c-ad4e-4793-bc40-83426b0356ed",
  "sourceToolAssistantUUID": "09039f93-aa05-47af-b66e-9c2a63669179",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T08:05:02.613Z_

<details><summary>↩ Tool result · `toolu_015j2J8cEC2349j8oUm3yY8J`</summary>

```text
Web search results for query: "ProcessBench results 2025 2026 accuracy scores"

Links: [{"title":"[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/abs/2412.06559"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.50/"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"PSBench: a large-scale benchmark for estimating the accuracy of protein complex structural models","url":"https://arxiv.org/pdf/2505.22674"},{"title":"GitHub - QwenLM/ProcessBench: Official repository for ACL 2025 paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"","url":"https://github.com/QwenLM/ProcessBench"},{"title":"[Quick Review] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://liner.com/review/processbench-identifying-process-errors-in-mathematical-reasoning"},{"title":"2025-2026 AI Computer-Use Benchmarks & Top AI Agents ...","url":"https://o-mega.ai/articles/the-2025-2026-guide-to-ai-computer-use-benchmarks-and-top-ai-agents"}]

Based on the search results, I found information about ProcessBench, which is an ACL 2025 paper titled "ProcessBench: Identifying Process Errors in Mathematical Reasoning".

Here are the key accuracy scores and results:

**Model Performance:**
- A process reward model achieved 67.5 F1 on ProcessBench compared to 66.4 for reference-guided training and 61.9 for GPT-4o
- The best open-source model, QwQ-32B-Preview, has demonstrated critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini
- Using Qwen2.5-Math-7B, an average accuracy of 47.4% was achieved across six mathematical reasoning benchmarks

**Benchmark Details:**
ProcessBench features 3,400 test cases with competition- and Olympiad-level math problems, generated by diverse language models and annotated with expert-verified error locations.

The research demonstrates that existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4a2d44-099b-4937-bd6a-7f9a8965f934",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "63f30858-283e-4791-b0a8-c67040dff151",
  "sourceToolAssistantUUID": "8b4a2d44-099b-4937-bd6a-7f9a8965f934",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T08:05:05.393Z_

<details><summary>↩ Tool result · `toolu_01ATCgLmGGt5z1L8TadvEPzg`</summary>

```text
Web search results for query: "github contrastive process reward model training"

Links: [{"title":"GitHub - mengdi-li/awesome-RLAIF: A continually updated list of literature on Reinforcement Learning from AI Feedback (RLAIF) · GitHub","url":"https://github.com/mengdi-li/awesome-RLAIF"},{"title":"Contrastive Learning and Reward Smoothing for Deep Portfolio Management","url":"https://www.ijcai.org/proceedings/2023/0441.pdf"},{"title":"GitHub - JLZhong23/awesome-reward-models","url":"https://github.com/jlzhong23/awesome-reward-models"},{"title":"Learning Goal-Conditioned Representations for Language Reward Models","url":"https://arxiv.org/pdf/2407.13887"},{"title":"GRACE: Generative Representation Learning via Contrastive Policy Optimization","url":"https://arxiv.org/pdf/2510.04506"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"GitHub - opendilab/awesome-RLHF: A curated list of reinforcement learning with human feedback resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLHF"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"}]

Here are the search results for "github contrastive process reward model training":

The search found several relevant GitHub repositories and research papers related to contrastive learning and reward model training:

1. **awesome-RLAIF Repository**: This resource covers "Reinforcement Learning from Contrastive Distillation (RLCD), a method for aligning language models to follow principles expressed in natural language without using human feedback."

2. **awesome-reward-models Repository**: This GitHub repository curates a collection of reward model papers, including several related to contrastive learning approaches like "Noise Contrastive Alignment of Language Models with Explicit Rewards" and various direct preference optimization methods.

3. **Goal-Conditioned Reward Models**: Code is available for "Learning Goal-Conditioned Representations for Language Reward Models" with an overview of contrastive goal-conditioned learning for text.

4. **GRACE (Generative Representation Learning via Contrastive Policy Optimization)**: This work "treats contrastive objectives as rewards over rationales, unifying representation learning with generation to produce stronger embeddings and transparent rationales," with model, data and code available on GitHub.

5. **Process Reward Models Research**: Recent work on "Adversarial Training for Process Reward Models" introduces "Adversarially Trained PRMs (APRM), where a Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them."

These repositories and papers focus on using contrastive learning approaches to improve reward model training for language models and reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a33c339-eda0-47d0-943d-9ed6f038703e",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "64e08526-e256-40c0-b981-23640229c57a",
  "sourceToolAssistantUUID": "3a33c339-eda0-47d0-943d-9ed6f038703e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T08:05:05.823Z_

<details><summary>↩ Tool result · `toolu_01EZQkG5avtQF1ADpg6bwjJV`</summary>

```text
Web search results for query: "best of N process reward model math accuracy results 2026"

Links: [{"title":"[2504.16828] Process Reward Models That Think - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2504.16828"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"Free Process Rewards without Process Labels","url":"https://arxiv.org/html/2412.01981v1"},{"title":"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/html/2503.13551"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"process reward model with qvalue rankings","url":"https://arxiv.org/pdf/2410.11287"}]

Based on the search results, here are the key findings on best-of-N process reward model math accuracy results from 2026:

## Recent 2026 Research Results

Recent work evaluates the accuracy of PRMs using the processBench benchmark, where PRMs predict whether responses are correct, as well as through Best-of-N evaluation on real-world math reasoning tasks.

A hierarchical multi-step reward model (HRM) evaluation using Qwen2.5-72B-Math-Instruct as the policy model showed that HRM maintains stable performance, with accuracy converging to 80% as N increases, in contrast to traditional outcome reward models and process reward models which showed significant performance fluctuations.

Recent comparisons include evaluations across multiple math benchmarks with different difficulties, including OlympiaBench, MATH, GSM8K, and CollegeMath, comparing state-of-the-art PRMs such as Qwen2.5-Math-7B-PRM and Qwen2.5-Math-PRM-72B.

## Earlier Notable Results (2025)

ThinkPRM-14B outperforms a discriminative PRM based on the same base model in terms of accuracy while using far fewer supervision signals, and ThinkPRM-14B exhibits the best accuracy scaling curve compared to LLM-as-a-judge, DiscPRM, and majority vote on AIME '24 and MATH-500.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be14450e-7f84-44c9-b9d7-1ccec6d4e900",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "54b5add2-2c7b-447c-9564-35a327ed8a03",
  "sourceToolAssistantUUID": "be14450e-7f84-44c9-b9d7-1ccec6d4e900",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T08:05:06.030Z_

<details><summary>↩ Tool result · `toolu_01QaW4WsAGMvfWKMJwd61QiL`</summary>

```text
Web search results for query: "github DAG math reasoning verification reward model"

Links: [{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs Yuanhe Zhang*","url":"https://arxiv.org/pdf/2510.19842"},{"title":"Proof-RM: A Scalable and Generalizable Reward Model for Math Proof","url":"https://arxiv.org/pdf/2602.02377"},{"title":"DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v2"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"},{"title":"GitHub - benjaminzwhite/reasoning-models: Experiments with reasoning models, training techniques, papers · GitHub","url":"https://github.com/benjaminzwhite/reasoning-models"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/html/2506.12509v3"},{"title":"Reinforcement Learning with Conditional Expectation Reward","url":"https://arxiv.org/pdf/2603.10624"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.22570"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"}]

Based on the search results, here are the key findings related to DAG, math reasoning, verification, and reward models:

## DAG-Math Framework

DAG-MATH introduces a CoT format and constructs a benchmark that guides LLMs to generate CoT trajectories in this format, enabling evaluation of their reasoning ability. The framework introduces logical closeness, a metric that quantifies how well a model's CoT trajectory adheres to the DAG structure, providing evaluation beyond classical PASS@k metrics. The benchmark and code are available at https://github.com/YuanheZ/DAG-MATH-Formatted-CoT.

## Graph of Verification Framework

Another related approach is the Graph of Verification (GoV) framework. By modeling reasoning as a DAG, the GoV framework ensures a transparent, structured, and non-circular verification process, where each statement is grounded in a traceable chain of valid inferences. Code is available at https://github.com/Frevor/Graph-of-Verification.

## Proof Verification Reward Models

Proof-RM is designed as a scalable and generalizable reward model for mathematics proof verification, addressing the need for a Reward Model capable of reliably evaluating full proof processes.

These approaches represent recent advances in combining structured reasoning representations (DAGs) with verification and reward mechanisms for improving mathematical reasoning in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee4a8aa7-4960-4755-991a-b65c38880473",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "6f5c9b06-b65a-46ad-99c0-b1522500a555",
  "sourceToolAssistantUUID": "ee4a8aa7-4960-4755-991a-b65c38880473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-27T08:05:06.354Z_

<details><summary>↩ Tool result · `toolu_01NPQL9mMMmeq5pXF59bvmC9`</summary>

```text
Web search results for query: "github premise dependency reward model math reasoning"

Links: [{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"RM-R1: Reward Modeling as Reasoning","url":"https://arxiv.org/pdf/2505.02387"},{"title":"Accurate and Diverse LLM Mathematical Reasoning via Automated PRM-Guided GFlowNets","url":"https://arxiv.org/pdf/2504.19981"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"},{"title":"PREMISE: Scalable and Strategic Prompt Optimization for Efficient Mathematical Reasoning in Large Models","url":"https://arxiv.org/pdf/2506.10716"},{"title":"DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning","url":"https://arxiv.org/pdf/2506.17533"},{"title":"reward-model · GitHub Topics · GitHub","url":"https://github.com/topics/reward-model"}]

Based on the search results, here's what I found:

The search returned several relevant results related to reward models and mathematical reasoning. The most directly relevant result appears to be PREMISE (PRompt-based Efficient Mathematical Inference with Strategic Evaluation), a prompt-only framework designed for efficient reasoning in black-box Large Reasoning Models that introduces reasoning text level metrics to diagnose overthinking and underthinking in a model's output.

Other notable findings include:

- FoVer, a project providing datasets, models, and code at https://github.com/psunlpgroup/FoVer for creating generalizable process reward models via formally verified training data

- RM-R1, a project with code, data, and models publicly available at https://github.com/RM-R1-UIUC/RM-R1 that explores reward modeling as a reasoning task

- DuaShepherd, which combines two types of PRM reward signals and achieves state-of-the-art improvements in MATH500 and ProcessBench

Additionally, there's a curated resource page listing various reward model approaches for mathematical reasoning, including VersaPRM and other process-supervised reward models from 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb8b121d-3df1-45bc-8389-1c7de460c618",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "84387d37-b1bc-4d01-87ee-68e283402d0e",
  "sourceToolAssistantUUID": "eb8b121d-3df1-45bc-8389-1c7de460c618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-27T08:05:06.378Z_

<details><summary>↩ Tool result · `toolu_01DWTdBpzgZkFyxfyxFtMPBW`</summary>

```text
Web search results for query: "github PERL premise extraction reasoning verification"

Links: [{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://abhinavchinta.com/parc/"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://arxiv.org/html/2502.02362"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs","url":"https://arxiv.org/pdf/2502.02362"},{"title":"Don’t Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning","url":"https://arxiv.org/html/2504.06438"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"}]

Based on the search results, here's what I found about PERL (Premises and ERrors identification in LLMs) related to premise extraction, reasoning verification:

## PERL Dataset and PARC Framework

The PERL dataset was developed to assess premise extraction capabilities, incorporating reasoning chains from established mathematical reasoning datasets (GSM8K, MATH, Orca-Math, and MetaMathQA), annotated with both premises and error types using OpenAI's GPT-4o.

## How It Works

The framework restructures conventional linear reasoning chains into Premise Augmented Reasoning Chains (PARC) by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links.

## Key Results

PERL demonstrates that LLMs can reliably identify premises within complex reasoning chains, with even open-source LLMs achieving 90% recall in premise identification. Additionally, PARC helps identify errors in reasoning chains more reliably, with accuracy improving by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.

## GitHub Repository

The code and data are available on https://github.com/SagnikMukherjee/PARC


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e603e1d3-b27e-4f45-9043-5d8945d0c690",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "dc43cc27-4f9c-4205-831f-849a27de4adc",
  "sourceToolAssistantUUID": "e603e1d3-b27e-4f45-9043-5d8945d0c690",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-27T08:05:07.494Z_

<details><summary>↩ Tool result · `toolu_01NNrenfYSy2Faw5AChu8fur`</summary>

```text
Web search results for query: "process reward model accuracy MATH dataset best of N 2025 2026"

Links: [{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"process reward model with qvalue rankings","url":"https://arxiv.org/pdf/2410.11287"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"},{"title":"From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling","url":"https://arxiv.org/pdf/2506.00027"},{"title":"Entropy-Regularized Process Reward Model","url":"https://arxiv.org/pdf/2412.11006"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"}]

Based on the search results, I found several recent studies on process reward models (PRMs) and their accuracy on the MATH dataset with best-of-N evaluation:

## Recent Process Reward Model Performance on MATH

ThinkPRM beats baselines on MATH-500 under best-of-N selection and reward-guided search. This is a generative PRM approach from 2025 that shows improvements over existing methods.

Parallel scaling with THINKPRM-1.5B@4 boosts accuracy by more than 5 percentage points and yields the best accuracy on MATH-500, while parallel scaling with THINKPRM-14B@4 and THINKPRM-14B@8 boosts best-of-N performance on MATH-500.

For comparison, baseline best-of-N@1 accuracy on MATH500 ranges from 18.4 to 37.4 depending on the model backbone, with the Llama-3-70B-Instruct achieving the highest baseline performance.

## Key Findings

ThinkPRM surpasses discriminative verifiers trained with the full PRM800K by 8% on GPQA-Diamond and 4.5% on LiveCodeBench, and outperforms LLM-as-a-Judge by 7.2% on ProcessBench under the same token budget.

Additionally, MCTS is the most effective strategy when ample computational resources are available, while Best-of-N Sampling offers a practical solution under resource constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5368100-1692-4c48-8cda-889464f530d5",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "36afc26f-eedc-4fbc-b291-3d35f5cb6234",
  "sourceToolAssistantUUID": "a5368100-1692-4c48-8cda-889464f530d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-27T08:05:11.422Z_

Now let me run the Section D searches plus a few follow-up searches to get more specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36afc26f-eedc-4fbc-b291-3d35f5cb6234",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bf1e35d-1835-4ea8-8707-eb8f9ae2955c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 42 · 2026-05-27T08:05:12.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JChjmuckm1aHSJ9G7dpDAP`</summary>

```json
{
  "query": "process reward model training GPU hours cost compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bf1e35d-1835-4ea8-8707-eb8f9ae2955c",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfb0a75c-fc3a-4028-85b4-28fafc76e6fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 43 · 2026-05-27T08:05:12.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUCVZC1U8PVg8qmtvNUsLt`</summary>

```json
{
  "query": "contrastive learning reward model compute requirements GPU training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfb0a75c-fc3a-4028-85b4-28fafc76e6fb",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "379bee25-7c8b-4cf3-9ebf-4ed8ed9985c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 44 · 2026-05-27T08:05:13.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JtdmWFcgRSDaQ11emucx25`</summary>

```json
{
  "query": "PRM training data size math-shepherd PRM800K dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "379bee25-7c8b-4cf3-9ebf-4ed8ed9985c3",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7987f802-b47b-487d-be51-3ef583c406cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 45 · 2026-05-27T08:05:14.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0121yhVCSy9xKXNdcKReetBE`</summary>

```json
{
  "query": "ThinkPRM scores MATH-500 best of N accuracy numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7987f802-b47b-487d-be51-3ef583c406cb",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e674d3e-ef37-4071-89c2-c55e8a6a8d94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 46 · 2026-05-27T08:05:15.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KbJumWEsV5DoR4QtxGZhqQ`</summary>

```json
{
  "query": "Qwen2.5-Math-PRM-72B PRMBench ProcessBench scores accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e674d3e-ef37-4071-89c2-c55e8a6a8d94",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSj9UtEueDEAAruQ2F36",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fa09a17-fa5f-419c-8708-efaaab038a53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5pYrYsxHYVmRhr6SXgijR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3493,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 11606,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3493,
          "output_tokens": 279,
          "cache_read_input_tokens": 11606,
          "cache_creation_input_tokens": 8224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8224,
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

_source line 47 · 2026-05-27T08:05:20.428Z_

<details><summary>↩ Tool result · `toolu_01JtdmWFcgRSDaQ11emucx25`</summary>

```text
Web search results for query: "PRM training data size math-shepherd PRM800K dataset"

Links: [{"title":"Supervised Training for PRMs — a brief dive into the training script | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/supervised-training-for-prms-a-brief-dive-into-the-training-script-64594d4bdc05"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning","url":"https://arxiv.org/html/2503.02382v1"},{"title":"Reward Models | OpenR Documents","url":"https://openreasoner.github.io/docs/usage/prm.html"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards","url":"https://arxiv.org/html/2604.17957"},{"title":"Datasets - MATH","url":"https://openreasoner.github.io/docs/datasets.html"},{"title":"Papers with Code - PRM800K Dataset","url":"https://paperswithcode.com/dataset/prm800k"},{"title":"GitHub - openai/prm800k: 800,000 step-level correctness labels on LLM solutions to MATH problems · GitHub","url":"https://github.com/openai/prm800k"}]

Based on the search results, here's information about PRM training datasets:

## PRM800K Dataset

PRM800K is a process supervision dataset containing 800,000 step-level correctness labels for model-generated solutions to problems from the MATH dataset. However, after deduplication, PRM800K consists of approximately 265k samples. PRM800K relies on costly human annotation.

## Math-Shepherd Dataset

The Math-Shepherd open-source dataset contains 445k samples. Math-Shepherd uses automatic annotation. According to one paper, the Math-Shepherd dataset is four times larger than that provided in PRM800K.

## Comparison

Recent work has shown that these datasets can be improved upon. For example, a PRM trained on Epic50k (50k annotated intermediate steps) achieves supervision performance comparable to, and in some cases surpassing, PRMs trained on the PRM800k and Math-Shepherd datasets, despite being less than 10% the size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7987f802-b47b-487d-be51-3ef583c406cb",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "32921faa-d0ec-4234-b54e-648f2cf76587",
  "sourceToolAssistantUUID": "7987f802-b47b-487d-be51-3ef583c406cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T08:05:20.920Z_

<details><summary>↩ Tool result · `toolu_01JChjmuckm1aHSJ9G7dpDAP`</summary>

```text
Web search results for query: "process reward model training GPU hours cost compute requirements"

Links: [{"title":"Model Training Cost Calculator – GPU, Token & Cloud Compute Estimator","url":"https://mytimecalculators.com/tools/model-training-cost-calculator/"},{"title":"What is the cost of training large language models?","url":"https://www.cudocompute.com/blog/what-is-the-cost-of-training-large-language-models"},{"title":"GPU Computing for AI Training: Complete Hardware and Optimization Guide","url":"https://helpforce.ai/news/gpu-computing-ai-training-hardware-guide-2025"},{"title":"How Much Does LLM Training Cost? | Galileo","url":"https://galileo.ai/blog/llm-model-training-cost"},{"title":"Exploring the cost of training an AI model on cloud infrastructure","url":"https://nebius.com/blog/posts/cost-of-training-an-ai-model-on-cloud"},{"title":"Reusing Embeddings: Reproducible Reward Model Research in Large Language   Model Alignment without GPUs","url":"https://arxiv.org/pdf/2502.04357"},{"title":"Cloud GPU Pricing: Compare 28 Providers (2026)","url":"https://gpuperhour.com/"},{"title":"Guide to Hardware Requirements for Training and Fine-Tuning Large Language Models | Towards AI","url":"https://towardsai.net/p/artificial-intelligence/guide-to-hardware-requirements-for-training-and-fine-tuning-large-language-models"}]

Based on the search results, here's what I found regarding process reward model training, GPU hours, costs, and compute requirements:

## Reward Model Training Costs

RLHF involves training additional models (reward models) and running reinforcement learning algorithms that themselves require lots of computations on GPUs and custom data generated by human annotators, which is expensive.

## General GPU Training Costs

Cloud GPU pricing ranges from $2-$10 per GPU-hour depending on model, with H100s at ~$5-8/hour and A100s at ~$2-5/hour. Additionally, an H100 SXM costs over $25,000 to buy but can be rented for $1.50-$3.50/hr depending on the provider.

## Large-Scale Training Requirements

For context on larger training operations, training 70B-parameter-class models on modern clusters (on the order of hundreds of H100/H200-class GPUs for several weeks) typically incurs compute-only cloud costs in the low- to mid-seven-figure range.

## Hardware Specifications

GPU selection depends on workload with 40-80GB for training medium models and 80GB+ for large language model training. For 70B models, minimum setup requires 16 GPUs with 40GB VRAM each, with 32 A100 GPUs (40GB each) being ideal for efficient training.

## Training Duration

Training on 1 trillion tokens takes approximately 2–3 months on 16 A100 GPUs or ~1 month on 32 A100 GPUs.

The search results provide general training cost frameworks, but specific details about reward model training costs are limited to noting that they're part of the broader RLHF pipeline and add significant expenses beyond base model training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfb0a75c-fc3a-4028-85b4-28fafc76e6fb",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "768f5a29-4e16-444f-ba4c-f994f0554de5",
  "sourceToolAssistantUUID": "cfb0a75c-fc3a-4028-85b4-28fafc76e6fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-27T08:05:21.139Z_

<details><summary>↩ Tool result · `toolu_0121yhVCSy9xKXNdcKReetBE`</summary>

```text
Web search results for query: "ThinkPRM scores MATH-500 best of N accuracy numbers"

Links: [{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Published in Transactions on Machine Learning Research (03/2026)","url":"https://openreview.net/pdf?id=FPVCb0WMuN"},{"title":"📉 May the Best Cheater Win - LLM Watch","url":"https://www.llmwatch.com/p/may-the-best-cheater-win"},{"title":"GitHub - SorenDreano/MATH-500-subset-qwen2-answers-evaluated-by-open-PRM","url":"https://github.com/SorenDreano/MATH-500-subset-qwen2-answers-evaluated-by-open-PRM"},{"title":"Structured Pruning for Diverse Best-of-N Reasoning Optimization","url":"https://arxiv.org/pdf/2506.03978"}]

Based on the search results, here's what I found about ThinkPRM's MATH-500 best-of-N accuracy scores:

ThinkPRM-14B exhibits the best accuracy scaling curve compared to LLM-as-a-judge, DiscPRM, and unweighted majority vote on best-of-N testing. On best-of-N selection with MATH-500, ThinkPRM achieves higher or comparable reasoning accuracy to DiscPRM across all sampling budgets.

The research demonstrates that ThinkPRM surpasses discriminative PRMs trained with orders of magnitude more process labels, highlighting the advantages of utilizing generative language-modeling objectives. Additionally, ThinkPRM, trained on just 1% of the data used by discriminative PRMs, outperforms both LLM-as-a-judge and discriminative baselines by up to 8 F1 points on in-domain benchmarks including MATH-500.

The search results show comparative performance information but don't include specific numerical accuracy percentages for each sampling budget on MATH-500. The paper (available at arxiv.org/pdf/2504.16828) likely contains detailed numerical results in tables or figures if you need those specific numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e674d3e-ef37-4071-89c2-c55e8a6a8d94",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "43d683d9-f766-4aef-ac4b-d8faf128e02e",
  "sourceToolAssistantUUID": "3e674d3e-ef37-4071-89c2-c55e8a6a8d94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-27T08:05:22.187Z_

<details><summary>↩ Tool result · `toolu_01AUCVZC1U8PVg8qmtvNUsLt`</summary>

```text
Web search results for query: "contrastive learning reward model compute requirements GPU training"

Links: [{"title":"DisCo-CLIP: A Distributed Contrastive Loss for Memory Efficient CLIP   Training","url":"https://arxiv.org/pdf/2304.08480"},{"title":"ROLL 2025-10-14 Part II: ROLL Flash – Accelerating RLVR and Agentic Training","url":"https://arxiv.org/pdf/2510.11345"},{"title":"Breaking the Memory Barrier: Near Infinite Batch Size Scaling for   Contrastive Loss","url":"https://arxiv.org/pdf/2410.17243"},{"title":"Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup","url":"https://arxiv.org/pdf/2101.06983"},{"title":"Contrastive Learning: A Tutorial | Built In","url":"https://builtin.com/machine-learning/contrastive-learning"},{"title":"CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning","url":"https://deepreinforce-ai.github.io/cudal1_blog/"},{"title":"Learning Goal-Conditioned Representations for Language Reward Models","url":"https://arxiv.org/pdf/2407.13887"}]

Here are the search results for your query on contrastive learning reward model compute requirements for GPU training:

## Key Findings

**Memory Complexity in Contrastive Learning:**

Contrastive loss computation typically requires GPU memory that scales quadratically with batch size (O(B²)), but distributed approaches can reduce this to O(B²/N), where B and N are batch size and number of GPUs. More recent methods have made even greater improvements: Inf-CL reduces space complexity from quadratic (e.g., O(b²) for CLIP, O(b²/n) for OpenCLIP) to linear (O(b/n²)).

**Practical GPU Requirements:**

DisCo-CLIP can enable contrastive training of a ViT-B/32 model with a batch size of 32K or 196K using 8 or 64 A100 40GB GPUs, compared with the original CLIP solution which requires 128 A100 40GB GPUs to train a ViT-B/32 model with a batch size of 32K.

For larger models, training a ViT-L/14 CLIP model with a batch size over 10M on 32 A800 GPUs (80 GB each) requires only 1.44 GB of memory per GPU—over a 30× improvement over previous methods.

**Training Time Considerations:**

Inf-CL takes approximately 59 hours to process a 64k batch size on 8 A800 GPUs, with time cost scaling nearly linearly with batch size (batch size increase from 64k to 256k results in roughly 4× growth in training time).

**Reward Models with Contrastive Learning:**

Contrastive objectives can be applied to reward model hidden representations from desirable and undesirable sequences to improve alignment of language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "379bee25-7c8b-4cf3-9ebf-4ed8ed9985c3",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "f316f985-5a96-4df3-b77a-f074f5136c45",
  "sourceToolAssistantUUID": "379bee25-7c8b-4cf3-9ebf-4ed8ed9985c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-27T08:05:22.926Z_

<details><summary>↩ Tool result · `toolu_01KbJumWEsV5DoR4QtxGZhqQ`</summary>

```text
Web search results for query: "Qwen2.5-Math-PRM-72B PRMBench ProcessBench scores accuracy"

Links: [{"title":"Qwen/Qwen2.5-Math-PRM-72B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B"},{"title":"Qwen/Qwen2.5-Math-PRM-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.06559v4"},{"title":"README.md · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"Qwen2.5-Math-PRM: Advanced Math LLM Framework","url":"https://www.emergentmind.com/topics/qwen2-5-math-prm"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/html/2503.22233"},{"title":"Qwen2.5-Math-PRM-72B","url":"https://www.promptlayer.com/models/qwen25-math-prm-72b"}]

Based on the search results, here's what I found about Qwen2.5-Math-PRM-72B's performance on PRMBench and ProcessBench:

## ProcessBench Performance

The Qwen2.5-Math-PRM-72B was evaluated on ProcessBench for measuring the ability to identify erroneous steps. When compared with LLM-as-judge, Qwen2.5-Math-PRM-7B demonstrates superior performance over all open-source models. For proprietary language models, Qwen2.5-Math-PRM-7B outperforms GPT-4o-0806, while there remains a performance gap compared to o1-mini. Both Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B exhibit substantial advantages over their counterparts.

## Overall Capabilities

The trained PRMs exhibit both impressive performance in the Best-of-N (BoN) evaluation and stronger error identification performance in ProcessBench. Additionally, Qwen2.5-Math-PRM-72B exhibits slightly better overall performance than Qwen2.5-Math-RM-72B, with particularly significant improvements observed in the Minerva Math and MMLU STEM tasks.

While the search results confirm strong performance from the Qwen2.5-Math-PRM models on ProcessBench, the exact numerical accuracy scores for the 72B variant specifically are not provided in these results. The documents focus more on comparative advantages over other models rather than absolute accuracy percentages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fa09a17-fa5f-419c-8708-efaaab038a53",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "c58bc4b3-e852-4440-842d-660b8b43ac36",
  "sourceToolAssistantUUID": "6fa09a17-fa5f-419c-8708-efaaab038a53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-27T08:05:26.547Z_

Let me fetch some more specific numbers from key pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c58bc4b3-e852-4440-842d-660b8b43ac36",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e5f4590-5dd1-4020-9f44-bd4789172056",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7578,
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

_source line 53 · 2026-05-27T08:05:27.993Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012SnPViMwpkKGdXnknEwJXY`</summary>

```json
{
  "url": "https://prmbench.github.io/",
  "prompt": "Extract all model scores from the leaderboard table. List every model name and its corresponding PRMBench score/accuracy. Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5f4590-5dd1-4020-9f44-bd4789172056",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca485ee1-3985-4a59-a874-d8b47d8b7264",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7578,
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

_source line 54 · 2026-05-27T08:05:29.373Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011P8gCvnGiYdnMicjYVW9oJ`</summary>

```json
{
  "url": "https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B",
  "prompt": "Extract all benchmark scores, accuracy numbers, and performance metrics mentioned for Qwen2.5-Math-PRM-72B. Include ProcessBench scores, Best-of-N results, and any other numerical metrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca485ee1-3985-4a59-a874-d8b47d8b7264",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d8bbefe-de3f-418c-b0ec-52859b8d6684",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7578,
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

_source line 55 · 2026-05-27T08:05:31.662Z_

<details><summary>↩ Tool result · `toolu_012SnPViMwpkKGdXnknEwJXY`</summary>

```text
# PRMBench Leaderboard Scores

I cannot provide the specific model scores from the leaderboard table because the web page content you shared does not include the actual numerical results. 

The page references a leaderboard with sections for "Proprietary LLMs" and "Open LLMs," organized by evaluation categories (Overall, Simplicity, Soundness, and Sensitivity), but the actual performance scores are not displayed in the text provided.

The content states: "Overall results of different models on the PRMBench leaderboard. The best-performing model in each category is in-red, and the second best is underlined," however, the specific model names and their corresponding scores are not included in this excerpt.

To access the complete leaderboard data, you would need to visit the interactive leaderboard directly on the website or consult the full paper at the arXiv link provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca485ee1-3985-4a59-a874-d8b47d8b7264",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "5112fd3a-b233-4ed9-87ac-0d7777260554",
  "sourceToolAssistantUUID": "ca485ee1-3985-4a59-a874-d8b47d8b7264",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-27T08:05:31.783Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D4rCixrQtfob5gE9SrLCVB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.16828",
  "prompt": "Extract all numerical results for ThinkPRM. Include MATH-500, ProcessBench, AIME, best-of-N accuracy numbers, F1 scores, and any other specific performance metrics. List all tables of results if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5112fd3a-b233-4ed9-87ac-0d7777260554",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dfdaeca-0490-4b84-ab4a-ed95af61455f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7578,
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

_source line 57 · 2026-05-27T08:05:33.762Z_

<details><summary>↩ Tool result · `toolu_011P8gCvnGiYdnMicjYVW9oJ`</summary>

```text
# Benchmark Scores and Performance Metrics for Qwen2.5-Math-PRM-72B

Based on the provided web page content, **no specific numerical benchmark scores, accuracy numbers, or performance metrics are explicitly mentioned** for Qwen2.5-Math-PRM-72B.

## What is Referenced:

The page mentions that:

1. **ProcessBench Performance**: The model exhibits "stronger error identification performance in [ProcessBench](https://huggingface.co/papers/2412.06559)" but no specific scores are provided on this page.

2. **Best-of-N (BoN) Evaluation**: The model has "impressive performance in the Best-of-N (BoN) evaluation" but quantitative results are not listed.

3. **Research Papers**: Two papers are referenced with potential benchmark details:
   - *ProcessBench: Identifying Process Errors in Mathematical Reasoning* (arXiv: 2412.06559)
   - *The Lessons of Developing Process Reward Models in Mathematical Reasoning* (arXiv: 2501.07301)

## To Find Specific Metrics:

For detailed benchmark scores and performance metrics, you would need to:
- Consult the full research papers (arXiv: 2501.07301 and 2412.06559)
- Review the complete model card documentation
- Check the [ProcessBench paper](https://huggingface.co/papers/2412.06559) directly
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d8bbefe-de3f-418c-b0ec-52859b8d6684",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "ec1ee40b-7426-4234-aeef-64536ca19d41",
  "sourceToolAssistantUUID": "0d8bbefe-de3f-418c-b0ec-52859b8d6684",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-27T08:05:34.043Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QhP4QvuEmDjRA9ViHhWaHi`</summary>

```json
{
  "url": "https://github.com/SagnikMukherjee/PARC",
  "prompt": "Extract details about the PARC/PERL project: what it does, the premise extraction approach, any training details, GPU requirements, dataset sizes, and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1ee40b-7426-4234-aeef-64536ca19d41",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c49eb071-e012-41e1-8cda-7f5b884fe19b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7578,
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

_source line 59 · 2026-05-27T08:05:35.119Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JP6s97XSSV2gLfxJkzuR99`</summary>

```json
{
  "url": "https://github.com/YuanheZ/DAG-MATH-Formatted-CoT",
  "prompt": "Extract all details about the DAG-MATH project: what it does, any training or compute requirements, dataset details, and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49eb071-e012-41e1-8cda-7f5b884fe19b",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjAcsVH78ZU36emEwPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e46f7de7-7700-4547-83b6-cec9561b6578",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3igEqpKNa2j5dWg2CX2nv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7578,
      "cache_read_input_tokens": 19830,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7578
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 565,
          "cache_read_input_tokens": 19830,
          "cache_creation_input_tokens": 7578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7578,
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

_source line 60 · 2026-05-27T08:05:36.183Z_

<details><summary>↩ Tool result · `toolu_01D4rCixrQtfob5gE9SrLCVB`</summary>

```text
# ThinkPRM Performance Results

Based on the provided abstract, the following numerical results are mentioned:

**Key Performance Metrics:**

- **Data Efficiency**: ThinkPRM uses "only 1% of the process labels in PRM800K" compared to discriminative baselines

- **Out-of-Domain Performance**:
  - GPQA-Diamond subset: outperforms discriminative verifiers by 8%
  - LiveCodeBench subset: outperforms discriminative verifiers by 4.5%

- **Verification Scaling**: Under equivalent token budgets, ThinkPRM "outperforming it by 7.2% on a subset of ProcessBench" when compared to LLM-as-a-Judge

**Benchmarks Evaluated:**
The abstract confirms ThinkPRM was tested on ProcessBench, MATH-500, and AIME '24 under both best-of-N selection and reward-guided search conditions.

Unfortunately, the provided web page content does not include detailed numerical results tables, specific accuracy percentages for each benchmark, or comprehensive F1 scores. The full paper would contain the complete results tables referenced in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dfdaeca-0490-4b84-ab4a-ed95af61455f",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "be1e55e0-a5c5-492e-b69f-0689e5f1dfd5",
  "sourceToolAssistantUUID": "6dfdaeca-0490-4b84-ab4a-ed95af61455f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-27T08:05:40.497Z_

<details><summary>↩ Tool result · `toolu_01JP6s97XSSV2gLfxJkzuR99`</summary>

```text
# DAG-MATH Project Summary

## Project Overview
DAG-MATH is a research project submitted to ICLR 2026 that focuses on "Graph-of-Thought Guided Mathematical Reasoning in LLMs." The work aims to improve how large language models approach mathematical problem-solving by structuring reasoning as directed acyclic graphs (DAGs).

## Dataset Details
The project includes a benchmark dataset called DAG-MATH-Formatted-CoT containing approximately 2,894 annotated chain-of-thought solutions. These solutions are sourced from the Omni-MATH dataset and feature problems across varying difficulty levels (scale of 1-6).

**Key dataset structure:**
- Problems include domain taxonomy classifications
- Solutions are broken into numbered steps
- Each step captures nodes in a reasoning DAG with dependencies
- Steps contain inference edges showing how previous steps support conclusions

## Dataset Schema
The structured format includes:
- Problem identifiers and text
- Final answers
- Step objects with: step IDs, inference edges, dependent steps, and node conclusions

## Notable Gaps
The provided content does not include information about:
- Training or computational requirements
- Model performance results or benchmarks
- Implementation details
- Comparison metrics with baseline approaches

The repository appears to still be under development, as indicated by the "In Progress" notation on the benchmark overview.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e46f7de7-7700-4547-83b6-cec9561b6578",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "a9320b3e-6c91-4bf5-b947-23635e800f71",
  "sourceToolAssistantUUID": "e46f7de7-7700-4547-83b6-cec9561b6578",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-27T08:05:41.150Z_

<details><summary>↩ Tool result · `toolu_01QhP4QvuEmDjRA9ViHhWaHi`</summary>

```text
# PARC Project Overview

## What It Does
PARC (Premise-Augmented Reasoning Chains) is a system designed to improve error identification in mathematical reasoning tasks performed by large language models. The approach works by mapping reasoning steps to their underlying premises and using this information to better detect errors.

## Premise Extraction Approach
The dataset includes a "premise_annotation" field that provides "Mapping of each model step to its underlying premises." This allows the system to trace which foundational assumptions or facts support each reasoning step, enabling more precise error detection.

## Dataset Details
The repository includes datasets in JSON format with entries containing:
- Mathematical word problems
- Step-by-step reasoning chains from models
- Ground truth solutions and answers
- Error annotations labeled at the step level with error types and descriptions
- Premise mappings for each step

Example datasets are available for GSM8K (a math word problem benchmark).

## Evaluation Infrastructure
The codebase supports three evaluation approaches:
1. **Premise Mapping** - Maps steps to premises via inference
2. **Baseline Error Evaluation** - Standard error classification
3. **Error Evaluation with Premises** - Incorporates premise information for improved detection

## Implementation Details
- Built in Python with PyTorch-based inference
- Supports multiple LLM backbones (tested with Llama-3.1-8B-Instruct)
- Uses tensor parallelization for inference scaling
- Requires Azure OpenAI credentials for certain model configurations

The project is MIT-licensed and maintained by Sagnik Mukherjee at the University of Illinois.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c49eb071-e012-41e1-8cda-7f5b884fe19b",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "d4dca8aa-14f9-4932-93ad-496583c7e81a",
  "sourceToolAssistantUUID": "c49eb071-e012-41e1-8cda-7f5b884fe19b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-27T08:05:47.099Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RqFVwmaD2xo4YSz5SYPfYZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.03124",
  "prompt": "Extract all specific model scores from the PRMBench paper. List every model tested and its numerical score. Include scores for models like Qwen2.5-Math-PRM, Math-Shepherd, RLHFlow, any GPT/Claude models, etc. Get all numbers from results tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4dca8aa-14f9-4932-93ad-496583c7e81a",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjBxn5r8HiC2QFMqHt3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c49e5707-ca4a-46e2-81ea-15d2bcc7b77d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zyK2xt48mcxGHGnHgnemB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 329,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 27408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 64 · 2026-05-27T08:05:48.608Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PRZq7wKMypugzKjX9RLwNp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.06559",
  "prompt": "Extract all specific numerical scores from ProcessBench tables. List every model and its accuracy/F1 score on ProcessBench. Include scores for Qwen2.5-Math-PRM, GPT-4o, o1-mini, and any other models tested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49e5707-ca4a-46e2-81ea-15d2bcc7b77d",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjBxn5r8HiC2QFMqHt3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c3cb21d-df80-4cfc-b12e-64a474b8620b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zyK2xt48mcxGHGnHgnemB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 329,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 27408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 65 · 2026-05-27T08:05:49.951Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lmu7L2xe8NDTuMNsXwXB9B`</summary>

```json
{
  "url": "https://qwenlm.github.io/blog/qwen2.5-math-prm/",
  "prompt": "Extract all benchmark scores and numerical results for Qwen2.5-Math-PRM models. Include ProcessBench scores, Best-of-N results, accuracy percentages, and any comparisons with other models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3cb21d-df80-4cfc-b12e-64a474b8620b",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjBxn5r8HiC2QFMqHt3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c508a49-a509-4cc1-b3d1-2a753f35640d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zyK2xt48mcxGHGnHgnemB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 329,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 27408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 66 · 2026-05-27T08:05:50.359Z_

<details><summary>↩ Tool result · `toolu_01RqFVwmaD2xo4YSz5SYPfYZ`</summary>

```text
# Response

I cannot provide the specific model scores you've requested. While the webpage confirms that **PRMBench includes "experiments on 15 models, spanning both open-source PRMs and closed-source large language models,"** the actual numerical results tables are not included in the provided content.

To access the detailed scores for models like Qwen2.5-Math-PRM, Math-Shepherd, RLHFlow, GPT variants, and Claude models, you would need to:

1. **View the full PDF** via the link at `/pdf/2501.03124`
2. **Visit the project page** at `prmbench.github.io`
3. **Check the paper's results section** directly in the arXiv source

The webpage excerpt only contains the abstract and metadata, not the benchmark results tables containing the numerical performance metrics you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c49e5707-ca4a-46e2-81ea-15d2bcc7b77d",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "9b4bb6f2-b970-400b-b6a2-4fde2d360afb",
  "sourceToolAssistantUUID": "c49e5707-ca4a-46e2-81ea-15d2bcc7b77d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-27T08:05:51.831Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0179SdrV9vV4pr9bKPBndk9F`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.07301",
  "prompt": "Extract all numerical results, training details, GPU requirements, compute costs, and dataset sizes mentioned in this paper about developing process reward models for mathematical reasoning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b4bb6f2-b970-400b-b6a2-4fde2d360afb",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjBxn5r8HiC2QFMqHt3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c5801de-5cb5-4a94-b420-c3cd5c192cc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zyK2xt48mcxGHGnHgnemB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 329,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 27408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 68 · 2026-05-27T08:05:52.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KKgzWdrc8UmsW8oroYBtzV`</summary>

```json
{
  "query": "process reward model training 8xA100 GPU hours fine-tuning 7B 72B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c5801de-5cb5-4a94-b420-c3cd5c192cc5",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjBxn5r8HiC2QFMqHt3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51a69713-fc43-4f8f-b25a-926993929da0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zyK2xt48mcxGHGnHgnemB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 329,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 27408,
      "output_tokens": 539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 329,
          "output_tokens": 539,
          "cache_read_input_tokens": 27408,
          "cache_creation_input_tokens": 1816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1816,
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

_source line 69 · 2026-05-27T08:05:54.557Z_

<details><summary>↩ Tool result · `toolu_01PRZq7wKMypugzKjX9RLwNp`</summary>

```text
# ProcessBench Scores - Information Limitation

I cannot provide the specific numerical scores you're requesting because **the web page content provided contains only the abstract and metadata** for the ProcessBench paper, not the actual research tables with model performance data.

The abstract mentions that the study "conduct[s] extensive evaluation on ProcessBench, involving two types of models: process reward models (PRMs) and critic models," and notes that "existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH." It also states that "QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o."

However, **no specific accuracy scores, F1 scores, or numerical performance metrics** appear in this excerpt. To access the actual benchmark results for Qwen2.5-Math-PRM, GPT-4o, o1-mini, and other tested models, you would need to view the full paper PDF available at arxiv.org/pdf/2412.06559.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3cb21d-df80-4cfc-b12e-64a474b8620b",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "61011020-7c11-4389-8c24-beb7615e5b96",
  "sourceToolAssistantUUID": "1c3cb21d-df80-4cfc-b12e-64a474b8620b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-27T08:05:56.312Z_

<details><summary>↩ Tool result · `toolu_0179SdrV9vV4pr9bKPBndk9F`</summary>

```text
# Analysis of arXiv:2501.07301

Based on the provided web page content, I cannot extract specific numerical results, training details, GPU requirements, compute costs, or dataset sizes. 

The page displays only the **abstract and metadata** for this paper about Process Reward Models (PRMs) in mathematical reasoning. The abstract describes the research findings conceptually—such as identifying flaws in Monte Carlo estimation approaches and proposing a "consensus filtering mechanism"—but does not include concrete performance metrics or computational specifications.

To access the actual numerical data you're seeking, you would need to:
- Download the full PDF via the "View PDF" link
- Review the paper's experimental results sections
- Examine any supplementary materials or appendices

The abstract notes they "significantly improve both model performance and data efficiency" and release "a state-of-the-art PRM," but specific values are not provided in this summary page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c5801de-5cb5-4a94-b420-c3cd5c192cc5",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "3c77ce9a-8c59-4a15-b74d-140c44c871b4",
  "sourceToolAssistantUUID": "8c5801de-5cb5-4a94-b420-c3cd5c192cc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-27T08:06:00.315Z_

<details><summary>↩ Tool result · `toolu_01KKgzWdrc8UmsW8oroYBtzV`</summary>

```text
Web search results for query: "process reward model training 8xA100 GPU hours fine-tuning 7B 72B"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via   Generative Reasoning","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models","url":"https://arxiv.org/pdf/2506.09532"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"AURORA:Automated Training Framework of Universal Process Reward Models   via Ensemble Prompting and Reverse Verification","url":"https://arxiv.org/pdf/2502.11520"},{"title":"Guide to Hardware Requirements for Training and Fine-Tuning Large Language Models | Towards AI","url":"https://towardsai.net/p/artificial-intelligence/guide-to-hardware-requirements-for-training-and-fine-tuning-large-language-models"},{"title":"Fine-Tuning LLMs on a Budget: Using DigitalOcean GPU Droplets | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/fine-tuning-llms-on-budget-digitalocean-gpu"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"VRPRM: Process Reward Modeling via Visual Reasoning","url":"https://arxiv.org/pdf/2508.03556"}]

The search results provide information about process reward models (PRMs) and their training, though they don't contain specific details about 8xA100 GPU hours for the exact configurations you mentioned. Here's what the results reveal:

**Process Reward Model Research:**

Several recent papers discuss PRM training approaches:

- A 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench, showing that smaller models can outperform much larger ones with the right training approach.

- A 1.5B model trained on only 700 problems achieves +4.32% improvements in Pass@1 on the AIME 2024 benchmark, while a 7B model trained on just 1070 problems achieves +6.67% gain.

- Using 3.6K CoT-PRM supervised fine-tuning data and 50K non-CoT PRM reinforcement learning training data, VRPRM can surpass non-thinking PRM with a total data volume of 400K.

**General A100 Training Benchmarks:**

Training on 1 trillion tokens takes approximately 1 month on 8 A100 GPUs (40GB each), and fine-tuning a 7B+ parameter model can require multiple A100 or H100 GPUs running for hours or even days, depending on dataset size and batch configurations.

The search results don't contain specific GPU hour metrics for the exact 7B and 72B model sizes with 8xA100 configurations you're asking about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51a69713-fc43-4f8f-b25a-926993929da0",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "2b81e3d3-cbd8-4a9b-acd6-ea96bc596d13",
  "sourceToolAssistantUUID": "51a69713-fc43-4f8f-b25a-926993929da0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-27T08:06:04.656Z_

<details><summary>↩ Tool result · `toolu_01Lmu7L2xe8NDTuMNsXwXB9B`</summary>

```text
# Qwen2.5-Math-PRM Benchmark Results

The webpage provides limited specific numerical scores. Here's what's available:

## Best-of-N (BoN) Evaluation
The article states that "Qwen2.5-Math-PRM-7B demonstrates superior performance compared to other PRMs of equivalent model scale" and achieved "an average improvement of 1.4%" over the maj@8 baseline across seven benchmarks (GSM8K, MATH, Minerva Math, GaoKao 2023 En, OlympiadBench, College Math, and MMLU STEM).

The 72B model showed "slightly better overall performance than Qwen2.5-Math-RM-72B, with particularly significant improvements observed in the Minerva Math and MMLU STEM tasks."

## ProcessBench Results
The document notes that "Qwen2.5-Math-PRM-7B in smaller model size demonstrates superior performance over all open-source models" and "outperforms GPT-4o-0806, while there remains a performance gap compared to o1-mini."

**Note:** The webpage contains two performance comparison charts/images but does not provide specific numerical values in the text. For exact percentage scores and detailed results, you would need to access the full research papers referenced (arXiv:2412.06559 and arXiv:2501.07301) or the GitHub/Hugging Face repositories linked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c508a49-a509-4cc1-b3d1-2a753f35640d",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "9cf65638-15c6-45b7-b56a-ad4c3cc439fe",
  "sourceToolAssistantUUID": "0c508a49-a509-4cc1-b3d1-2a753f35640d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-27T08:06:11.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013hj9JFXf57xstzhFcshQY6`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.03124v1",
  "prompt": "Extract all model scores from the results tables in this paper. List every model name and its PRMBench score or accuracy. Include all numerical values from all tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cf65638-15c6-45b7-b56a-ad4c3cc439fe",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjDiNiWL7LDiMNmkWMi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2286a238-4976-4c2c-adbc-626a2a0f9306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHsvRvwe5a8wgKWVdvdEit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1030,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 29224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1691,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 74 · 2026-05-27T08:06:11.524Z_

<details><summary>↩ Tool result · `toolu_013hj9JFXf57xstzhFcshQY6`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2286a238-4976-4c2c-adbc-626a2a0f9306",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "aa235158-8d04-48a9-86cf-24f40eb9169b",
  "sourceToolAssistantUUID": "2286a238-4976-4c2c-adbc-626a2a0f9306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-27T08:06:12.738Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01STTjzCD4Nme4SFASPYuMem`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559v4",
  "prompt": "Extract all numerical scores from the ProcessBench results tables. List every model name and its accuracy or F1 score. Include all difficulty levels if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa235158-8d04-48a9-86cf-24f40eb9169b",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjDiNiWL7LDiMNmkWMi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29564b46-9887-490b-b16b-eeaf929b64f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHsvRvwe5a8wgKWVdvdEit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1030,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 29224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1691,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 76 · 2026-05-27T08:06:12.747Z_

<details><summary>↩ Tool result · `toolu_01STTjzCD4Nme4SFASPYuMem`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29564b46-9887-490b-b16b-eeaf929b64f2",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "f48df269-9301-4201-8f02-acbb3f364a0e",
  "sourceToolAssistantUUID": "29564b46-9887-490b-b16b-eeaf929b64f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-27T08:06:13.664Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017nhapLiszeVQGTTDTw2Kua`</summary>

```json
{
  "query": "Math-Shepherd PRM training details GPU compute 8 A100 training time epochs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48df269-9301-4201-8f02-acbb3f364a0e",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjDiNiWL7LDiMNmkWMi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dedbd852-6280-4acd-b346-8d0e17049683",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHsvRvwe5a8wgKWVdvdEit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1030,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 29224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1691,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 78 · 2026-05-27T08:06:14.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0165yos8knDMiuYvbQEP3xou`</summary>

```json
{
  "query": "R-PRM reasoning driven process reward model scores PRMBench ProcessBench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedbd852-6280-4acd-b346-8d0e17049683",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjDiNiWL7LDiMNmkWMi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5589301-ccd5-4c10-9b25-70dab3f904e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHsvRvwe5a8wgKWVdvdEit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1030,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 29224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1691,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 79 · 2026-05-27T08:06:36.212Z_

<details><summary>↩ Tool result · `toolu_0165yos8knDMiuYvbQEP3xou`</summary>

```text
Web search results for query: "R-PRM reasoning driven process reward model scores PRMBench ProcessBench"

Links: [{"title":"R-PRM: Reasoning-Driven Process Reward Modeling | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.679@ACL"},{"title":"[Literature Review] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://www.themoonlight.io/en/review/r-prm-reasoning-driven-process-reward-modeling"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling | OpenReview","url":"https://openreview.net/forum?id=mHHRWSIsXm"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/pdf/2503.21295"},{"title":"[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/abs/2503.21295"},{"title":"[2503.21295v1] R-PRM: Reasoning-Driven Process Reward Modeling","url":"http://arxiv.org/abs/2503.21295v1"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.679/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"}]

Based on the search results, here's what I found about R-PRM and its performance on PRMBench and ProcessBench:

## R-PRM Overview

R-PRM (Reasoning-Driven Process Reward Modeling) addresses issues with existing Process Reward Models by leveraging stronger LLMs to generate seed data from limited annotations, enhancing performance through preference optimization without additional annotated data, and introducing inference-time scaling to harness the model's reasoning potential.

## Performance Scores

On ProcessBench and PRMBench, R-PRM surpasses strong baselines by 11.9 and 8.5 points in F1 scores, respectively. Note that one source reports slightly higher improvements of 13.9 and 8.5 F1 scores on these benchmarks.

## Additional Results

When applied to guide mathematical reasoning, R-PRM achieves consistent accuracy improvements of over 8.5 points across six challenging datasets.

ProcessBench tests the ability to identify the earliest incorrect step in a solution, while PRMBench is a comprehensive benchmark for evaluating PRMs across various dimensions of error diagnosis (Simplicity, Soundness, and Sensitivity).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5589301-ccd5-4c10-9b25-70dab3f904e1",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "e193ad5b-44d2-4414-9eb1-f6feb487d6cc",
  "sourceToolAssistantUUID": "d5589301-ccd5-4c10-9b25-70dab3f904e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-27T08:06:40.536Z_

<details><summary>↩ Tool result · `toolu_017nhapLiszeVQGTTDTw2Kua`</summary>

```text
Web search results for query: "Math-Shepherd PRM training details GPU compute 8 A100 training time epochs"

Links: [{"title":"Training details: Compute measured in A100 40GB GPU","url":"https://www.researchgate.net/figure/Training-details-Compute-measured-in-A100-40GB-GPU-hours-number-of-parameters-and_tbl1_368753315"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"Math-Shepherd: LLM Step-by-Step Verification","url":"https://www.emergentmind.com/papers/2312.08935"},{"title":"Improve Mathematical Reasoning in Language Models by ...","url":"https://arxiv.org/pdf/2406.06592"},{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"Paper page - Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://huggingface.co/papers/2312.08935"},{"title":"NVIDIA A100 GPU Guide: 2.0TB/s Specs, MIG & Cloud Rental","url":"https://www.runpod.io/articles/guides/nvidia-a100-gpu"}]

Let me search for more specific training details from the Math-Shepherd paper.

Links: [{"title":"What is Epoch vs Batch in Machine Learning?","url":"https://www.eimt.edu.eu/difference-between-epoch-and-batch-machine-learning"},{"title":"Relation Between Learning Rate and Batch Size | Baeldung on Computer Science","url":"https://www.baeldung.com/cs/learning-rate-batch-size"},{"title":"Published as a conference paper at ICLR 2018 DON’T DECAY THE LEARNING RATE,","url":"https://openreview.net/pdf?id=B1Yy1BxCZ"},{"title":"Understanding Parameters in ML Training — Batch Size, Iteration, Epoch, Learning Rate","url":"https://medium.com/@weidagang/understanding-parameters-in-ml-training-batch-size-iteration-epoch-learning-rate-a1217d8f80e1"},{"title":"How many epochs are enough to train your model","url":"https://nebius.com/blog/posts/factors-influencing-epoch-count"},{"title":"Don't Decay the Learning Rate, Increase the Batch Size","url":"https://arxiv.org/pdf/1711.00489"},{"title":"How Should the Learning Rate Change as the Batch Size Changes? - GeeksforGeeks","url":"https://www.geeksforgeeks.org/deep-learning/how-should-the-learning-rate-change-as-the-batch-size-changes/"},{"title":"Day 48: Training Neural Networks — Hyperparameters, Batch Size, Epochs | by Adithya Prasad Pandelu | Medium","url":"https://medium.com/@bhatadithya54764118/day-48-training-neural-networks-hyperparameters-batch-size-epochs-712c57d9e30c"}]

Let me search more specifically for the Math-Shepherd paper's training configuration details.

Links: [{"title":"Paper page - Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://huggingface.co/papers/2312.08935"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.510/"},{"title":"Math-Shepherd: LLM Step-by-Step Verification","url":"https://www.emergentmind.com/papers/2312.08935"},{"title":"[PDF] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Math-Shepherd:-Verify-and-Reinforce-LLMs-without-Wang-Li/4ba57555bef02f988f2ed3bab2f102733dc55221"},{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"[2312.08935v3] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935v3"},{"title":"Papers Explained 366: Math Shepherd | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-366-math-shepherd-234b1bdfbcae"},{"title":"Math Shepherd - Distilabel Docs","url":"https://distilabel.argilla.io/1.5.0/sections/pipeline_samples/papers/math_shepherd/"}]

I found that the reward model is trained in 1 epoch. Let me search for more specific details about compute hours and GPU configuration.

Links: [{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"[2312.08935v3] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935v3"},{"title":"Paper page - Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://huggingface.co/papers/2312.08935"},{"title":"[PDF] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Math-Shepherd:-Verify-and-Reinforce-LLMs-without-Wang-Li/4ba57555bef02f988f2ed3bab2f102733dc55221"},{"title":"Math-Shepherd: A Label-Free Step-by-Step Verifier for LLMs in Mathematical Reasoning","url":"https://arxiv.org/html/2312.08935v1"},{"title":"Math-Shepherd: LLM Step-by-Step Verification","url":"https://www.emergentmind.com/papers/2312.08935"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | alphaXiv","url":"https://www.alphaxiv.org/overview/2312.08935"},{"title":"To learn more: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations - https://arxiv.org/pdf/2312.08935 Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning - https://arxiv.org/pdf/2410.08146 Solving math word problems with processand outcome-based feedback - https://arxiv.org/pdf/2211.14275 Scaling test-time compute with Open Models - https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute","url":"https://www.threads.com/@rajistics/post/DD0c2OcS8eh"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"}]

Based on my web search results, I found limited specific information about the GPU compute hours and detailed training configuration for Math-Shepherd PRM. From the search results, I was able to identify one key detail about the training:

The reward model is trained in 1 epoch.

Unfortunately, I was unable to find detailed information in the search results about the specific training duration in A100 GPU hours, batch size, learning rate, or other hyperparameter configurations mentioned in your query. While I found references to the Math-Shepherd paper (arxiv 2312.08935) and summaries of the work, the specific technical training details you're asking about—particularly the compute requirements for 8 A100 GPUs and training time—are not present in the available search results.

To obtain this information, you may need to:
1. Access the full PDF of the paper directly from arXiv
2. Check the appendix or supplementary materials section
3. Review the paper's GitHub repository if the authors have shared training code and configurations


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dedbd852-6280-4acd-b346-8d0e17049683",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "c3716856-52d5-41c6-ac88-d3cd3485f7a6",
  "sourceToolAssistantUUID": "dedbd852-6280-4acd-b346-8d0e17049683",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-27T08:06:48.589Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PFjwXUDwfNU4j6dGYvEHbY`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.21295v1",
  "prompt": "Extract all numerical benchmark results. List every model and its specific scores on ProcessBench, PRMBench, and any math benchmarks. Include F1 scores, accuracy percentages, and best-of-N results. Focus on tables of results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3716856-52d5-41c6-ac88-d3cd3485f7a6",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjGLh547EoXEc22s7Ak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a17de9f-4317-441a-aaa0-cbd8278ec49d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3CQ7HAaUe5N9EThLxE6xH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3713,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 82 · 2026-05-27T08:06:51.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018tb293ttmnWSEvNT4ioZUV`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.16828",
  "prompt": "Extract all numerical results from tables. List specific accuracy numbers for ThinkPRM on MATH-500, ProcessBench, AIME 24, GPQA Diamond, LiveCodeBench. Include best-of-N results with specific numbers. Include training compute details if mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a17de9f-4317-441a-aaa0-cbd8278ec49d",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjGLh547EoXEc22s7Ak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a8e4ee0-7ffa-406e-aaee-3661b462c1f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3CQ7HAaUe5N9EThLxE6xH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3713,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 83 · 2026-05-27T08:06:52.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XmxJKhdW782qnuvaUuGFQv`</summary>

```json
{
  "query": "GenPRM 7B surpasses Qwen2.5-Math-PRM-72B ProcessBench specific scores numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8e4ee0-7ffa-406e-aaee-3661b462c1f8",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjGLh547EoXEc22s7Ak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d77adf3c-94fb-4eae-8785-262181a791b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3CQ7HAaUe5N9EThLxE6xH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3713,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 84 · 2026-05-27T08:06:53.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1DPGRKGxAigh9hS9ejAvN`</summary>

```json
{
  "query": "PathFinder-PRM PRMBench 67.7 score details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d77adf3c-94fb-4eae-8785-262181a791b1",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjGLh547EoXEc22s7Ak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cc25642-0d3e-41af-b6d5-38108adf22e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3CQ7HAaUe5N9EThLxE6xH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 30915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3713,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 85 · 2026-05-27T08:06:58.880Z_

<details><summary>↩ Tool result · `toolu_01XmxJKhdW782qnuvaUuGFQv`</summary>

```text
Web search results for query: "GenPRM 7B surpasses Qwen2.5-Math-PRM-72B ProcessBench specific scores numbers"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"README.md · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"},{"title":"Qwen/Qwen2.5-Math-PRM-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"},{"title":"Qwen/Qwen2.5-Math-PRM-72B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B"},{"title":"arXiv:2501.07301v2 [cs.CL] 5 Jun 2025 2025-06-12","url":"https://arxiv.org/pdf/2501.07301"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"}]

Based on the search results, I found information about GenPRM 7B surpassing Qwen2.5-Math-PRM-72B on ProcessBench, but the specific score numbers are limited in the publicly available excerpts. Here's what I found:

A 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench through test-time scaling. 

From another source, the 7B GenPRM model surpasses Qwen2.5-Math-PRM-72B (which is 10x larger) on average F1 score when using test-time scaling.

However, the specific numerical scores for each model are not clearly presented in the search result excerpts. I did find one reference indicating that Qwen2.5-Math-PRM-72B achieved an average F1 score of 78.3 on ProcessBench, but the exact corresponding GenPRM 7B score wasn't included in these excerpts.

For the complete detailed scores and comparisons, you would need to access the full GenPRM research paper (arXiv:2504.00891), which likely contains comprehensive tables with all the specific numerical results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d77adf3c-94fb-4eae-8785-262181a791b1",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "f65511e6-d93b-4e67-bca1-ce3a712e4776",
  "sourceToolAssistantUUID": "d77adf3c-94fb-4eae-8785-262181a791b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-27T08:06:59.754Z_

<details><summary>↩ Tool result · `toolu_01PFjwXUDwfNU4j6dGYvEHbY`</summary>

```text
# R-PRM Benchmark Results Summary

## ProcessBench Results (Table 1)

**R-PRM Models:**
- R-PRM-7B-SFT: 65.2 F1 score
- R-PRM-7B-DPO: 70.4 F1 score

**Key Baselines:**
- Qwen2.5-Math-PRM-7B: 73.5 F1
- Qwen2.5-Math-7B-PRM800K: 58.5 F1
- Qwen2.5-Math-PRM-7B: 82.4 F1 (GSM8K), 77.6 F1 (MATH), 67.5 F1 (OlympiadBench)

## PRMBench Results (Table 2)

**R-PRM Performance:**
- R-PRM-7B-SFT: 64.9 overall score
- R-PRM-7B-DPO: 66.8 overall score

**Comparative Results:**
- Qwen2.5-Math-PRM-7B: 65.5 overall
- ReasonEval-7B: 60.0 overall

## Best-of-N and Guided Search (Tables 3-4)

**Greedy Guide Search Performance:**
- R-PRM-7B-DPO: 49.4 average accuracy across six datasets
- Qwen2.5-Math-PRM-7B: 46.8 average

**Best-of-8 Results:**
- R-PRM-7B-DPO: 49.6 average accuracy
- Qwen2.5-Math-PRM-7B: 48.0 average

The findings demonstrate that "R-PRM achieves F1 score improvements of 11.9 and 8.5 points" over baselines on ProcessBench and PRMBench respectively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a17de9f-4317-441a-aaa0-cbd8278ec49d",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "241b4c05-cbe2-4671-9822-979dabf77e4c",
  "sourceToolAssistantUUID": "0a17de9f-4317-441a-aaa0-cbd8278ec49d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-27T08:07:00.319Z_

<details><summary>↩ Tool result · `toolu_018tb293ttmnWSEvNT4ioZUV`</summary>

```text
# Numerical Results from ThinkPRM Research

## Key Performance Metrics

**ProcessBench (F1-Score):**
- ThinkPRM-14B on OlympiadBench: 87.3
- ThinkPRM-14B on OmniMath: 85.7
- Trained on only 1K synthetic examples (8K step labels)

**MATH-500 Results:**
The paper evaluated on a 100-problem subset covering difficulty levels 1-5. ThinkPRM-1.5B with beam search showed substantial improvements over discriminative and LLM-as-judge baselines, though specific accuracy percentages for this benchmark aren't explicitly tabulated in the provided sections.

**Out-of-Domain Performance:**
- GPQA-Physics: ThinkPRM outperformed discriminative PRMs by 8%
- LiveCodeBench: ThinkPRM exceeded discriminative baselines by 4.5%

## Training Efficiency

- **Data Requirements:** Only 8,000 step-level labels versus 712,000 for discriminative PRMs
- **Training Duration:** 1.5 hours for 14B models; 4.5 hours for QwQ-32B on single A100 GPU
- **Synthetic Data:** 1,000 verification chains collected through filtered sampling

The research demonstrates that "generative step-by-step verification can greatly benefit from scaling up the verifier's inference compute" through extended reasoning chains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a8e4ee0-7ffa-406e-aaee-3661b462c1f8",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "c5c50ac4-b7b5-43f3-a5c5-a19f7cb1fc8d",
  "sourceToolAssistantUUID": "2a8e4ee0-7ffa-406e-aaee-3661b462c1f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-27T08:07:01.009Z_

<details><summary>↩ Tool result · `toolu_01R1DPGRKGxAigh9hS9ejAvN`</summary>

```text
Web search results for query: "PathFinder-PRM PRMBench 67.7 score details"

Links: [{"title":"PRMBench: Benchmark for Process-level Math Reasoning","url":"https://www.emergentmind.com/topics/prmbench"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"declare-lab/PathFinder-PRM-7B · Hugging Face","url":"https://huggingface.co/declare-lab/PathFinder-PRM-7B"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"[Literature Review] Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://www.themoonlight.io/en/review/socratic-prmbench-benchmarking-process-reward-models-with-systematic-reasoning-patterns"}]

Based on the search results, here are the details about PathFinder-PRM's 67.7 PRMBench score:

## Score Achievement

PathFinder-PRM achieved a PRMScore of 67.7 with three times less data than previous best scores. More specifically, PathFinder-PRM achieves a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5).

## Model Architecture

PathFinder-PRM-7B is a hierarchical discriminative Process Reward Model (PRM) designed to identify errors and reward correct math reasoning in multi-step outputs from large language models (LLMs). Instead of treating evaluation as a single correct-or-wrong decision, PathFinder-PRM-7B breaks down its error judgment into 2 parts: whether the reasoning is mathematically correct, and logically consistent, then combines them to decide if the current reasoning steps lead to a correct final solution.

## Training Approach

PathFinder-PRM's explicit decoupling of error-type detection from reward estimation is key to its performance. PathFinder-PRM-7B is trained on a combination of high-quality human annotated data (PRM800K) and additional automatically annotated samples, enabling robustness to common failure patterns and strong generalization across diverse benchmarks such as ProcessBench and PRMBench.

## Performance Recognition

PathFinder-PRM-7B outperforms all open-source discriminative PRMs and LLM-as-judge models, while achieving competitive performance compared to large proprietary models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cc25642-0d3e-41af-b6d5-38108adf22e6",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "d06409e5-6c1b-4af0-8cb8-d95d06b0caa3",
  "sourceToolAssistantUUID": "9cc25642-0d3e-41af-b6d5-38108adf22e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-27T08:07:05.165Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017SApYJW3gKa5iyV8MvGYyd`</summary>

```json
{
  "url": "https://github.com/declare-lab/PathFinder-PRM",
  "prompt": "Extract all benchmark scores, training details, GPU requirements, compute costs, dataset sizes, and implementation details for PathFinder-PRM."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06409e5-6c1b-4af0-8cb8-d95d06b0caa3",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjHrF6WPJW1yfe54X4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf19bb56-d089-411c-9b5a-a51d9c2e0d1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e2fTwxfhF9AxKuNFPDSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3639,
      "cache_read_input_tokens": 34628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 90 · 2026-05-27T08:07:06.624Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014feZXEZNbmSojcwFfkoQ7s`</summary>

```json
{
  "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models",
  "prompt": "List all process reward models mentioned with their release dates, sizes, and any performance numbers. Focus on models from 2025-2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf19bb56-d089-411c-9b5a-a51d9c2e0d1a",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjHrF6WPJW1yfe54X4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87026888-fd50-4a0f-b5e3-63fbea1eb077",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e2fTwxfhF9AxKuNFPDSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3639,
      "cache_read_input_tokens": 34628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 91 · 2026-05-27T08:07:07.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HL3CmhJd5v3dXo32aMNeJM`</summary>

```json
{
  "query": "FoVer formally verified process reward model training compute GPU requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87026888-fd50-4a0f-b5e3-63fbea1eb077",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjHrF6WPJW1yfe54X4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1d5e5ab-40c9-4c41-ae3e-c39e8a0d8237",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e2fTwxfhF9AxKuNFPDSBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3639,
      "cache_read_input_tokens": 34628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 92 · 2026-05-27T08:07:08.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172uRRYbfTWSqKdJeo4HAEn`</summary>

```json
{
  "query": "\"process reward model\" training cost \"8 GPU\" OR \"4 GPU\" OR \"A100 hours\" fine-tune 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1d5e5ab-40c9-4c41-ae3e-c39e8a0d8237",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjHrF6WPJW1yfe54X4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e61731e7-221c-474e-a3b3-265af53d4409",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e2fTwxfhF9AxKuNFPDSBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3639,
      "cache_read_input_tokens": 34628,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 34628,
          "cache_creation_input_tokens": 3639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3639,
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

_source line 93 · 2026-05-27T08:07:12.540Z_

<details><summary>↩ Tool result · `toolu_017SApYJW3gKa5iyV8MvGYyd`</summary>

```text
# PathFinder-PRM: Key Metrics and Implementation Details

## Benchmark Scores

**PRMBench Performance:**
- PRMScore: 67.7 (state-of-the-art)
- Prior best baseline: 65.5
- Reward-guided greedy search (prm@8): 48.3 (+1.5 point improvement)

## Dataset Specifications

**Training Data:**
- "400K‑sample dataset by enriching the human‑annotated PRM800K corpus and RLHFlow Mistral traces with three‑dimensional step‑level labels"
- Uses 3× less data than prior approaches
- Error categories: Math, Consistency, and Optimality (step-level annotations)

## Model Architecture

The system employs a hierarchical approach: "The model first classifies step-level errors into Math and Consistency categories, followed by estimating step Optimality"

## Available Resources

- **Pretrained Model:** PathFinder-PRM-7B (available on Hugging Face)
- **Dataset:** PathFinder-600K accessible via Hugging Face
- **Code Language Composition:** 86.4% Jupyter Notebook, 13.5% Python

## GPU/Compute Requirements

**Not specified** in the provided documentation. The README references setup instructions but does not detail computational requirements, memory needs, or training duration.

## Implementation Components

Three main modules:
1. Data generation pipeline with automated error labeling
2. Hierarchical PRM training scripts
3. Evaluation frameworks for ProcessBench, PRMBench, and Reward-Guided Generation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf19bb56-d089-411c-9b5a-a51d9c2e0d1a",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "f4b0cb21-6c7a-41c3-a43e-73969257a77f",
  "sourceToolAssistantUUID": "cf19bb56-d089-411c-9b5a-a51d9c2e0d1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-27T08:07:13.945Z_

<details><summary>↩ Tool result · `toolu_01HL3CmhJd5v3dXo32aMNeJM`</summary>

```text
Web search results for query: "FoVer formally verified process reward model training compute GPU requirements"

Links: [{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data | OpenReview","url":"https://openreview.net/forum?id=LAejsDitr3"},{"title":"FoVer: Efficient PRM Training Data Synthesis via Formal Verification","url":"https://fover-prm.github.io/"},{"title":"GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub","url":"https://github.com/psunlpgroup/FoVer"},{"title":"FOVER: Training Verifiers with Formal Tools","url":"https://www.emergentmind.com/papers/2505.15960"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, here's what I found about FoVer:

FoVer is a framework that synthesizes PRM (Process Reward Model) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.

By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. The framework creates PRM training data from formal logic and theorem proving tasks.

However, the search results do not contain specific information about the compute GPU requirements for training PRMs with FoVer. The papers focus on the methodology and effectiveness of the framework rather than detailed hardware specifications. You may need to consult the full paper on arXiv (2505.15960) or the GitHub repository (github.com/psunlpgroup/FoVer) for specific GPU requirement details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1d5e5ab-40c9-4c41-ae3e-c39e8a0d8237",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "ebe45ee7-3926-497a-8d1e-de98ca36e8d4",
  "sourceToolAssistantUUID": "b1d5e5ab-40c9-4c41-ae3e-c39e8a0d8237",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-27T08:07:14.854Z_

<details><summary>↩ Tool result · `toolu_014feZXEZNbmSojcwFfkoQ7s`</summary>

```text
# Process Reward Models (2025-2026)

Based on the repository, here are the PRMs mentioned with available information:

## Mathematical Task PRMs

**CoLD** (2025.07) - "Counterfactually-Guided Length Debiasing for Process Reward Models"
- No size or performance metrics provided

**SPARE** (2025.06) - "Single-Pass Annotation with Reference-Guided Evaluation"
- No specifications listed

**SP-PRM** (2025.06) - "From Outcomes to Processes: Guiding PRM Learning"
- No details available

**FreePRM** (2025.06) - Trains without ground truth process labels
- No model size or benchmarks disclosed

**Q-RM** (2025.05, ICML 2025) - Token-level discriminative optimization
- No performance data provided

**ThinkPRM** (2025.04) - "Process Reward Models That Think"
- **14B parameters** (Hugging Face model available)

**GenPRM** (2025.04) - Test-time compute scaling via generative reasoning
- No size specifications mentioned

**R-PRM** (2025.03) - "Reasoning-Driven Process Reward Modeling"
- **7B version available** (DPO variant on Hugging Face)

**Universal PRM** (2025.02) - "AURORA: Automated Training Framework"
- **7B model** released

**Qwen2.5-Math PRM** (2025.01) - Mathematical reasoning specialization
- Model collection available; no specific size stated

## Non-Mathematical Task PRMs

**VersaPRM** (2025.02) - Multi-domain via synthetic data
- Supports multiple reasoning domains beyond mathematics

**o1-Coder** (2024.12) - Coding task specialization
- Replicates o1 capabilities for programming

**Note:** The document lacks detailed performance benchmarks, training data sizes, and comparative metrics for most models listed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87026888-fd50-4a0f-b5e3-63fbea1eb077",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "964c600f-f0e2-4e73-bec7-782bed5e4cec",
  "sourceToolAssistantUUID": "87026888-fd50-4a0f-b5e3-63fbea1eb077",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-27T08:07:18.180Z_

<details><summary>↩ Tool result · `toolu_0172uRRYbfTWSqKdJeo4HAEn`</summary>

```text
Web search results for query: ""process reward model" training cost "8 GPU" OR "4 GPU" OR "A100 hours" fine-tune 2025 2026"

Links: [{"title":"AI Model Training Costs 2026: GPT Budget & GPU Pricing","url":"https://localaimaster.com/blog/ai-model-training-costs-2025-analysis"},{"title":"Machine Learning Model Training Cost Statistics 2026","url":"https://www.aboutchromebooks.com/machine-learning-model-training-cost-statistics/"},{"title":"LLM Fine-Tuning Cost Calculator 2026 - DeepSeek, Llama, GPT Training ROI","url":"https://bytecalculators.com/llm-fine-tuning-cost-calculator"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/pdf/2504.10559"},{"title":"How to Fine-Tune LLMs in 2026: Costs, GPUs, and Code | Spheron Blog","url":"https://www.spheron.network/blog/how-to-fine-tune-llm-2026/"},{"title":"LLM Fine-Tuning Pricing 2026 — Compare Training Costs | Price Per Token","url":"https://pricepertoken.com/fine-tuning"},{"title":"How Much Does Llama-3 Fine-Tuning Cost? (2026 Budget Guide) | Calcix | Calcix","url":"https://calcix.net/guides/business-startup/ai-model-training-cost-budgeting-guide"},{"title":"How Much Does LLM Training Cost? | Galileo","url":"https://galileo.ai/blog/llm-model-training-cost"}]

Based on the search results, I found relevant information about process reward model training and fine-tuning costs:

## Process Reward Model Training

Process reward models (PRMs) were proposed to identify process errors and provide finer-grained supervision of the training process. The main challenge in training Process Reward Models lies in obtaining fine-grained step-level annotations, which remain prohibitively expensive.

Lightman et al. (2023) pioneered PRM training by employing human experts to label 75K questions at the step level. Recent research has focused on reducing these costs—ACTPRM surpasses prior SOTA models with significantly lower costs, outperforming UniversalPRM by 0.7% using only 20% of its annotation budget.

## Fine-Tuning Costs (2025-2026)

For general fine-tuning on smaller scales:

- Training 1 million tokens on a 70B model with LoRA takes ~2-3 hours on an A100.
- You can fine-tune a 7B parameter model with a single GPU for under $5 and see results in hours, not weeks.
- Fine-tuning a 70B Llama-3 model typically costs between $12,000 and $45,000 depending on your dataset size and hardware efficiency, while a smaller 8B model can be optimized for under $1,500.

The search results don't contain specific information about process reward model fine-tuning costs with the exact GPU configurations you mentioned (8 GPU or 4 GPU setups). The information available focuses more on general LLM fine-tuning costs and PRM annotation expenses rather than specific compute hardware requirements for PRM fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e61731e7-221c-474e-a3b3-265af53d4409",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "615721d9-5f58-4229-986a-99985873ca2b",
  "sourceToolAssistantUUID": "e61731e7-221c-474e-a3b3-265af53d4409",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-27T08:07:21.961Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jux3aApsBCeRWFKtnqP4VC`</summary>

```json
{
  "url": "https://github.com/Frevor/Graph-of-Verification",
  "prompt": "Extract all details about the Graph of Verification project: what it does, implementation details, compute requirements, results, and dataset sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "615721d9-5f58-4229-986a-99985873ca2b",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjK7cLwDEWLv2cENitq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98d90b81-b3d3-4e58-bff7-f7e0f4700e49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WszSKY5oQ5pWWdewJi3A7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2609,
      "cache_read_input_tokens": 38267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 98 · 2026-05-27T08:07:23.428Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SoeTWRSMQSGeWUNc4hcXwt`</summary>

```json
{
  "url": "https://github.com/NJUNLP/R-PRM",
  "prompt": "Extract training details, GPU requirements, compute costs, dataset sizes, and implementation specifics for R-PRM."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98d90b81-b3d3-4e58-bff7-f7e0f4700e49",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjK7cLwDEWLv2cENitq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "279e1025-2161-483f-95f8-d9be4af70f3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WszSKY5oQ5pWWdewJi3A7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2609,
      "cache_read_input_tokens": 38267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 99 · 2026-05-27T08:07:23.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YVGy3kSzvRKSojNV8kFVzz`</summary>

```json
{
  "query": "APRM adversarial process reward model training compute GPU requirements dataset size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "279e1025-2161-483f-95f8-d9be4af70f3b",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjK7cLwDEWLv2cENitq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d8c4902-abf5-4218-9d50-a18686925d23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WszSKY5oQ5pWWdewJi3A7z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2609,
      "cache_read_input_tokens": 38267,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 38267,
          "cache_creation_input_tokens": 2609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2609,
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

_source line 100 · 2026-05-27T08:07:31.461Z_

<details><summary>↩ Tool result · `toolu_01SoeTWRSMQSGeWUNc4hcXwt`</summary>

```text
# R-PRM Training and Implementation Details

## Dataset Sizes
- **SFT Training Data**: Approximately 289K samples generated via prompting LLaMA3.3-70B-Instruct
- **DPO Preference Pairs**: Around 269K pairs constructed from sampled trajectories
- **Validation Set**: 20K held-out samples for early stopping

## Training Hyperparameters
- **Base Model**: Qwen2.5-Math-7B-Instruct
- **Batch Size**: 128
- **Training Epochs**: 1
- **Learning Rates**:
  - SFT: `5e-6`
  - DPO: `5e-7`
- **Inference Trajectories**: Default K=10 per step

## Training Approach
The framework employs two sequential stages: "(1) Supervised Fine-Tuning (SFT) We prompt stronger LLMs with PRM800K samples to construct seed data with detailed step-level analyses and correctness judgments" followed by direct preference optimization using "multiple evaluation trajectories and construct preference pairs based on agreement with ground-truth labels."

## GPU/Compute Requirements
The documentation does not specify GPU requirements, VRAM needs, or computational costs. Training duration and hardware specifications are not disclosed.

## Implementation Details
Code uses Python (65.7%), Shell scripts (32.9%), and Jinja templating (1.4%). Evaluation occurs through ProcessBench and PRMBench scripts located in `src/scripts/examples/`. The repository includes utilities in `src/utils/inference.py` for constructing training data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "279e1025-2161-483f-95f8-d9be4af70f3b",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "906efa6f-ed1e-4f70-bca5-82a73567186e",
  "sourceToolAssistantUUID": "279e1025-2161-483f-95f8-d9be4af70f3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-27T08:07:33.365Z_

<details><summary>↩ Tool result · `toolu_01Jux3aApsBCeRWFKtnqP4VC`</summary>

```text
# Graph of Verification (GoV) Project Summary

## Purpose
GoV is a training-free framework that enhances LLM reasoning verification by decomposing complex multi-step reasoning into a directed acyclic graph (DAG) structure, enabling detection of localized errors that holistic methods miss.

## Core Mechanism
The system operates through four stages:
1. **DAG Construction**: Models reasoning as a graph where nodes represent steps and edges show logical dependencies
2. **Topological Sorting**: Enforces causal consistency by verifying premises before dependent conclusions
3. **Sequential Verification**: An LLM assesses each unit in sorted order using previously validated steps as context
4. **Termination**: Stops at the first detected error for precise fault localization

## Key Design Dimensions
- **Verification Granularity**: Ranges from atomic nodes (single equations) to node blocks (entire paragraphs)
- **Contextual Scope**: From minimal context (direct premises only) to inclusive context (all verified steps)

## Implementation Details
The repository contains two main experimental modules:

**Number Triangle Summation**: Tests atomic-level granularity on formal arithmetic tasks with unambiguous dependency graphs.

**ProcessBench (GSM8K)**: Evaluates block-level granularity on natural language mathematical reasoning, using paragraph-level verification with inclusive context.

## Datasets & Results
The project mentions datasets for N = 2, 4, 6, and 8 in the summation task, plus the GSM8K split from ProcessBench. Performance improvements are measured via F1 scores, with GoV reportedly outperforming "both holistic baselines and other state-of-the-art methods."

## Technical Requirements
- Python with dependencies listed in requirements.txt
- OpenAI API key (configurable via .env file)
- Model used: Qwen2.5 series (hardcoded, modifiable in scripts)

No explicit compute requirements or detailed result metrics are provided in the documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98d90b81-b3d3-4e58-bff7-f7e0f4700e49",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "23b5b21c-a823-4a41-8ef2-f7ae8fe5be19",
  "sourceToolAssistantUUID": "98d90b81-b3d3-4e58-bff7-f7e0f4700e49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-27T08:07:51.563Z_

<details><summary>↩ Tool result · `toolu_01YVGy3kSzvRKSojNV8kFVzz`</summary>

```text
Web search results for query: "APRM adversarial process reward model training compute GPU requirements dataset size"

Links: [{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141v2"},{"title":"[2504.06141] Adversarial Training of Reward Models","url":"https://arxiv.org/abs/2504.06141"},{"title":"Preprint. Under review. Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"}]

Based on the search results, here's what I found about APRM (Adversarially Trained Process Reward Models):

## Overview
APRM involves a Generator (G) that learns to produce reasoning errors to deceive a PRM (R), while R concurrently learns to detect them, yielding progressively harder negatives that improve robustness and generalization to novel errors without requiring manual step-level labels.

## Computational Requirements
The computational cost is one of the main considerations. Training requires additional resources due to the adversarial optimization between generator and PRM, though inference-time compute is unchanged.

For related adversarial reward model training (Adv-RM), the specific hardware and timing requirements include: experiments conducted on Nvidia A100 80G GPUs, with conventional 8b reward model training taking around 4 hours on one 8 GPU node, policy training taking around 12 hours on 2 8 GPU nodes, and adversarial policy training taking around 12 hours on 2 8 GPU nodes, resulting in conventional RLHF taking 224 A100 hours while Adv-RM training (with 2 rounds) takes 672 A100 hours.

## Dataset Requirements
The search results do not contain specific information about APRM's dataset size requirements. The paper notes that as the availability of high-quality training data for large models plateaus, adversarial training offers a way to generate targeted supervision, specifically focusing on model weaknesses, where data collection is expensive or impractical.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d8c4902-abf5-4218-9d50-a18686925d23",
  "isSidechain": true,
  "promptId": "e22bfc79-0a49-4220-ab7a-aad9ac9cf7cd",
  "agentId": "a7fcd55ce3613e611",
  "type": "user",
  "uuid": "a6c90b44-adb8-4ea7-a7d5-24c3207f7309",
  "sourceToolAssistantUUID": "1d8c4902-abf5-4218-9d50-a18686925d23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-27T08:09:34.301Z_

Now I have comprehensive data. Let me compile the final report.

---

# Comprehensive Research Report: Process Reward Models, Math Reasoning, and Related Work

## A. Current Top Open-Source Models for Process Reward Modeling and Math Reasoning (as of May 2026)

### Top Process Reward Models (PRMs)

**1. PathFinder-PRM-7B** (2025)
- State-of-the-art PRMScore of **67.7** on PRMBench, surpassing the prior best of 65.5
- Uses a hierarchical approach: classifies step-level errors into Math and Consistency categories, then estimates step Optimality
- Trained on ~400K samples (3x less data than prior approaches), enriching PRM800K with automated annotations
- GitHub: https://github.com/declare-lab/PathFinder-PRM
- HuggingFace: https://huggingface.co/declare-lab/PathFinder-PRM-7B

**2. R-PRM-7B-DPO** (March 2025, EMNLP 2025)
- ProcessBench F1: **70.4** (SFT variant: 65.2)
- PRMBench overall: **66.8** (SFT variant: 64.9)
- Best-of-8 average accuracy across 6 math datasets: **49.6** vs Qwen2.5-Math-PRM-7B's 48.0
- Surpasses baselines by **11.9 F1** on ProcessBench and **8.5 F1** on PRMBench
- Base: Qwen2.5-Math-7B-Instruct; trained on ~289K SFT samples + ~269K DPO pairs
- GitHub: https://github.com/NJUNLP/R-PRM

**3. Qwen2.5-Math-PRM (7B and 72B)** (January 2025)
- Qwen2.5-Math-PRM-7B ProcessBench F1: **73.5** (overall), with per-subset scores of 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench)
- PRMBench overall: **65.5**
- The 7B model outperforms GPT-4o-0806 on ProcessBench; the 72B model achieves ~**78.3** average F1 on ProcessBench
- Blog: https://qwenlm.github.io/blog/qwen2.5-math-prm/

**4. ThinkPRM (1.5B and 14B)** (April 2025, TMLR 2026)
- A generative PRM that uses long chain-of-thought verification
- ProcessBench F1: **87.3** (OlympiadBench), **85.7** (OmniMath) for ThinkPRM-14B
- Trained on only **8,000 step-level labels** (1% of PRM800K's 712K labels)
- Outperforms discriminative verifiers by **8%** on GPQA-Diamond and **4.5%** on LiveCodeBench
- Outperforms LLM-as-a-Judge by **7.2%** on ProcessBench
- Training time: **1.5 hours** for 14B, **4.5 hours** for QwQ-32B on a single A100
- Paper: https://arxiv.org/abs/2504.16828

**5. GenPRM-7B** (April 2025)
- A 7B model that surpasses Qwen2.5-Math-PRM-72B (10x larger) on ProcessBench through test-time scaling
- Paper: https://arxiv.org/abs/2504.00891

**6. Other Notable PRMs (2025-2026):**
- **FreePRM** (June 2025): Trains without ground-truth process labels
- **FoVer** (May 2025, ACL 2026 Findings): Uses formal verification (Z3, Isabelle) for data synthesis; GitHub: https://github.com/psunlpgroup/FoVer
- **APRM** (Nov 2025): Adversarial training for PRMs
- **VersaPRM** (Feb 2025): Multi-domain PRM via synthetic reasoning data
- **Universal PRM / AURORA** (Feb 2025): Automated training framework, 7B model released

### Top Open-Source Math Reasoning Models

**1. DeepSeekMath-V2** (2026)
- 685B parameters, built on DeepSeek-V3.2-Exp-Base
- Uses a generation-verification loop with an LLM-based verifier as reward model
- Gold-medal-level on IMO 2025; scored **118/120** on Putnam 2024 (human best: 90)
- Open-source

**2. DeepSeek-R1-0528**
- 671B total parameters (MoE), 164K context
- Performance comparable to OpenAI o1 on math, code, and reasoning
- Distilled variant DeepSeek-R1-Distill-Qwen3-8B outperforms Gemini 2.5 Flash on AIME 2025

**3. Qwen 3.7 Max (May 2026)**
- **97.1** on HMMT 2026 February
- 1M-token context window
- Pricing: $2.50/$7.50 per million tokens

**4. Qwen2.5-Math-72B-Instruct**
- Outperforms Qwen2-Math-72B-Instruct by 4.4 points (English) and 6.1 points (Chinese) on average

**5. Llama 4 Maverick** (17B active params, 128 experts)
- Beats GPT-4o and Gemini 2.0 Flash on broad benchmarks
- Comparable to DeepSeek v3 on reasoning and coding

**6. Llama 4 Behemoth** (288B active params)
- SOTA for non-reasoning models on math benchmarks

**7. OpenThinker3-7B**: **53%** on AIME 2025, **51%** on LiveCodeBench, **54%** on GPQA Diamond

---

## B. Baseline Numbers to Beat

### PRMBench Scores (Step-Level Error Detection)

| Model | PRMBench Score |
|-------|---------------|
| PathFinder-PRM-7B | **67.7** (SOTA) |
| R-PRM-7B-DPO | 66.8 |
| Qwen2.5-Math-PRM-7B | 65.5 |
| R-PRM-7B-SFT | 64.9 |
| ReasonEval-7B | 60.0 |

### ProcessBench Scores (F1, Error Identification)

| Model | ProcessBench F1 |
|-------|----------------|
| ThinkPRM-14B (OlympiadBench) | **87.3** |
| ThinkPRM-14B (OmniMath) | 85.7 |
| Qwen2.5-Math-PRM-72B | ~78.3 (avg) |
| Qwen2.5-Math-PRM-7B | 73.5 (avg); 82.4 (GSM8K), 77.6 (MATH), 67.5 (OlympiadBench) |
| R-PRM-7B-DPO | 70.4 |
| R-PRM-7B-SFT | 65.2 |
| GPT-4o | ~61.9 |
| Qwen2.5-Math-7B-PRM800K | 58.5 |

### Best-of-N Math Accuracy

| Model | BoN-8 Avg (6 datasets) |
|-------|----------------------|
| R-PRM-7B-DPO | **49.6** |
| Qwen2.5-Math-PRM-7B | 48.0 |
| R-PRM-7B-SFT | ~46-47 |

- Hierarchical Reward Model (HRM) using Qwen2.5-72B-Math-Instruct: accuracy converges to **~80%** as N increases
- ThinkPRM-1.5B with parallel scaling boosts MATH-500 accuracy by **>5 percentage points** over baselines
- Baseline best-of-N@1 on MATH-500: 18.4-37.4 depending on backbone

### Key Benchmark Reference Points
- **RewardBench**: Decision-Tree-Reward-Gemma-2-27B achieves **95.4%** (SOTA for general reward models)
- **Skywork-Reward-V2**: Leading on RewardBench v2 across BoN, RM-Bench, and truthfulness
- **RewardBench 2**: Models score ~20 points lower on average than the original RewardBench

---

## C. Similar Implementations on GitHub

### Premise/Dependency-Based Approaches

**1. PARC (Premise-Augmented Reasoning Chains)**
- Restructures linear reasoning chains into DAGs with premise links
- LLMs achieve **90% recall** in premise identification
- Error identification accuracy improves by **6-16% absolute** with premise-augmented verification
- Tested with Llama-3.1-8B-Instruct
- MIT License
- GitHub: https://github.com/SagnikMukherjee/PARC

**2. DAG-MATH (Graph-of-Thought Guided Mathematical Reasoning)**
- Submitted to ICLR 2026
- Benchmark with ~2,894 annotated CoT solutions from Omni-MATH
- Introduces "logical closeness" metric for DAG structure adherence
- GitHub: https://github.com/YuanheZ/DAG-MATH-Formatted-CoT

**3. Graph of Verification (GoV)**
- Training-free framework: decomposes reasoning into a DAG, applies topological sort, then sequential verification
- Outperforms holistic baselines on ProcessBench (GSM8K) F1 scores
- Uses Qwen2.5 series; requires OpenAI API
- GitHub: https://github.com/Frevor/Graph-of-Verification

### Contrastive/Adversarial Approaches

**4. APRM (Adversarial Training for PRMs)**
- Generator learns to produce reasoning errors; PRM learns to detect them
- Related Adv-RM training: conventional 8B reward model training takes ~4 hours on 1 node (8 GPUs); full adversarial pipeline takes **672 A100 hours** (2 rounds) vs **224 A100 hours** for conventional RLHF
- Paper: https://arxiv.org/abs/2511.22888

**5. GRACE (Generative Representation via Contrastive Policy Optimization)**
- Treats contrastive objectives as rewards over rationales
- Paper: https://arxiv.org/abs/2510.04506

### Other Relevant Repositories

**6. RM-R1 (Reward Modeling as Reasoning)**
- GitHub: https://github.com/RM-R1-UIUC/RM-R1

**7. FoVer (Formally Verified PRM Training Data)**
- Uses Z3 and Isabelle for automated step-level annotation
- GitHub: https://github.com/psunlpgroup/FoVer

**8. Awesome-Process-Reward-Models** (curated list)
- GitHub: https://github.com/RyanLiu112/Awesome-Process-Reward-Models

**9. RLHFlow/RLHF-Reward-Modeling**
- Trained top-3 8B models on RewardBench (ArmoRM, Pair Pref. Model, BT RM)
- GitHub: https://github.com/RLHFlow/RLHF-Reward-Modeling

**10. OpenPRM** (ICLR 2025)
- Building open-domain PRMs with preference trees
- Paper: https://openreview.net/forum?id=fGIqGfmgkW

---

## D. Hardware/Data Requirements for Similar Experiments

### Training Compute

| Experiment | Hardware | Time | Total GPU-Hours |
|-----------|----------|------|----------------|
| ThinkPRM-14B fine-tuning | 1x A100 | 1.5 hours | **1.5 A100-hours** |
| ThinkPRM-QwQ-32B | 1x A100 | 4.5 hours | **4.5 A100-hours** |
| Conventional 8B reward model | 8x A100 (1 node) | ~4 hours | **~32 A100-hours** |
| Adversarial RM (full pipeline, 2 rounds) | 16x A100 (2 nodes) | ~12 hours | **~672 A100-hours** |
| Conventional RLHF pipeline | 8x A100 | varies | **~224 A100-hours** |
| General 7B fine-tuning (LoRA) | 1x A100 | hours | **<$5 cloud cost** |
| General 70B fine-tuning | 8-32x A100 | days | **$12K-$45K** |

### Cloud GPU Pricing (2026)
- H100 SXM: **$1.50-$3.50/hr** rental, ~$5-8/hr on premium clouds
- A100 80GB: **$2-5/hr** depending on provider

### Dataset Sizes

| Dataset | Size | Annotation Method |
|---------|------|------------------|
| PRM800K | ~800K labels (~265K after dedup) | Human expert annotation |
| Math-Shepherd | ~445K samples | Automatic (Monte Carlo) |
| PathFinder-600K | ~400K samples | PRM800K + automated enrichment |
| R-PRM SFT data | ~289K samples | LLaMA3.3-70B-Instruct generation |
| R-PRM DPO pairs | ~269K pairs | Sampled trajectory construction |
| Epic50k | ~50K annotated steps | Matches PRM800K/Math-Shepherd performance at <10% size |
| ThinkPRM | **1K examples (8K step labels)** | Filtered synthetic sampling |
| VRPRM | 3.6K CoT-PRM SFT + 50K non-CoT RL | Mixed |
| PRMBench (evaluation) | 6,216 problems, 83,456 step labels | Expert-designed |
| ProcessBench (evaluation) | 3,400 test cases | Expert-verified error locations |
| DAG-MATH benchmark | ~2,894 annotated CoT solutions | From Omni-MATH |

### Key Efficiency Findings
- **ThinkPRM** achieves SOTA with only **1% of PRM800K labels** (8K vs 712K), making it extremely data-efficient
- **Epic50k** (50K steps) matches models trained on PRM800K/Math-Shepherd at <10% dataset size
- **GenPRM-7B** surpasses Qwen2.5-Math-PRM-72B (10x larger) via test-time compute scaling
- **ACTPRM** outperforms Universal PRM by 0.7% using only **20% of annotation budget**
- A 1.5B model trained on only **700 problems** achieves +4.32% on AIME 2024; a 7B on **1,070 problems** achieves +6.67%

---

Sources:
- [PRMBench (ACL 2025)](https://prmbench.github.io/)
- [PRMBench Paper](https://arxiv.org/abs/2501.03124)
- [ProcessBench (ACL 2025)](https://arxiv.org/abs/2412.06559)
- [ProcessBench GitHub](https://github.com/QwenLM/ProcessBench)
- [ThinkPRM Paper](https://arxiv.org/abs/2504.16828)
- [R-PRM Paper](https://arxiv.org/abs/2503.21295)
- [R-PRM GitHub](https://github.com/NJUNLP/R-PRM)
- [PathFinder-PRM GitHub](https://github.com/declare-lab/PathFinder-PRM)
- [PathFinder-PRM HuggingFace](https://huggingface.co/declare-lab/PathFinder-PRM-7B)
- [GenPRM Paper](https://arxiv.org/abs/2504.00891)
- [Qwen2.5-Math-PRM Blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)
- [Qwen2.5-Math-PRM-72B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B)
- [Qwen2.5-Math-PRM-7B HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B)
- [Qwen 3.7 Max](https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026)
- [DeepSeekMath-V2 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2)
- [DeepSeekMath-V2 Nature Coverage](https://www.nature.com/articles/d41586-025-03959-9)
- [Top Open-Source Reasoning Models 2026](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [Best Open-Source LLM for Math 2026](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [Llama 4 Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [PARC GitHub](https://github.com/SagnikMukherjee/PARC)
- [DAG-MATH GitHub](https://github.com/YuanheZ/DAG-MATH-Formatted-CoT)
- [Graph of Verification GitHub](https://github.com/Frevor/Graph-of-Verification)
- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)
- [RM-R1 GitHub](https://github.com/RM-R1-UIUC/RM-R1)
- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [Awesome Reward Models](https://github.com/JLZhong23/awesome-reward-models)
- [RLHFlow RLHF Reward Modeling](https://github.com/RLHFlow/RLHF-Reward-Modeling)
- [APRM Paper](https://arxiv.org/abs/2511.22888)
- [RewardBench](https://huggingface.co/spaces/allenai/reward-bench)
- [RewardBench 2](https://openreview.net/forum?id=fb0G86Dewb)
- [PRM800K GitHub](https://github.com/openai/prm800k)
- [Math-Shepherd Paper](https://arxiv.org/abs/2312.08935)
- [OpenPRM (ICLR 2025)](https://openreview.net/forum?id=fGIqGfmgkW)
- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)
- [ToolPRMBench](https://arxiv.org/html/2601.12294v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c90b44-adb8-4ea7-a7d5-24c3207f7309",
  "isSidechain": true,
  "agentId": "a7fcd55ce3613e611",
  "requestId": "req_011CbSjMaNUkr7WwswxCVyP3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51fc9c80-e7a0-42cb-b6b5-ab48a3b28586",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "17534bdc-c682-449b-afbd-9cd4dfa99aa8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wtx6aJjxH9LaCRihgaCc5N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 40876,
      "output_tokens": 5062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5062,
          "cache_read_input_tokens": 40876,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1786,
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
