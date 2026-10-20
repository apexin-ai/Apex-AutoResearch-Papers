# Research conversation: I'm revising a research proposal and reviewers flagged several missing references. Please research the following 4 paper

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adf0ac9b242421c10.jsonl`
- **Structured JSON:** [`84e9abf5c97c54b9a004.json`](../../sessions/84/84e9abf5c97c54b9a004.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-19T10:28:16.862Z_

I'm revising a research proposal and reviewers flagged several missing references. Please research the following 4 papers thoroughly:

1. David (2511.14773) "Temporal Predictors of Outcome in Reasoning Language Models" - probes hidden states after first t reasoning tokens with linear classifiers
2. Zhang et al. (2504.05419) "Reasoning Models Know When They're Right" - probes hidden states at intermediate answer positions, derives probe-based early-exit (24% token reduction)
3. Lewis-Lim et al. (2508.19827) - tracks answer confidence trajectories across CoT step positions
4. arxiv 2603.22816 "The Illusion of Reasoning" - three-mode taxonomy (genuine/scaffolding/decoration) based on step-level faithfulness evaluation

For each paper:
- Fetch the arxiv abstract page (https://arxiv.org/abs/XXXX.XXXXX) 
- Search for any related discussions or citations
- Report: What exactly do they do? What models/benchmarks? What's their key contribution? How does it overlap with measuring temporal information flow across CoT for faithfulness assessment?

Be thorough - I need to understand exactly what each paper contributes to position our work properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "64e64ccb-1326-4398-8bcf-8b18ad0e3f65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T10:28:16.865Z_

```json
{
  "parentUuid": "64e64ccb-1326-4398-8bcf-8b18ad0e3f65",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "f582781c-c626-4315-92ad-0a6ce58f6f43",
  "timestamp": "2026-05-19T10:28:16.865Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T10:28:16.865Z_

```json
{
  "parentUuid": "f582781c-c626-4315-92ad-0a6ce58f6f43",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "605e084c-c226-467b-a516-e61a65cff19d",
  "timestamp": "2026-05-19T10:28:16.865Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T10:28:19.169Z_



I'll research all four papers thoroughly. Let me start by fetching the arxiv abstract pages for each paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "605e084c-c226-467b-a516-e61a65cff19d",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbKFxKBh2cKCSZWxWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de6d8abf-3d82-41d4-ab89-c478a221acad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbB1rGnivy2MxjHoML4id8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-19T10:28:19.693Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015HXDJ5dYZ6BZTgQJ78AXav`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6d8abf-3d82-41d4-ab89-c478a221acad",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbKFxKBh2cKCSZWxWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40409783-45d5-4240-85d6-22766eec9b15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbB1rGnivy2MxjHoML4id8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 7773,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1634,
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

_source line 6 · 2026-05-19T10:28:19.702Z_

<details><summary>↩ Tool result · `toolu_015HXDJ5dYZ6BZTgQJ78AXav`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40409783-45d5-4240-85d6-22766eec9b15",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "7e42a50a-d684-4861-a76e-921a05ba061b",
  "sourceToolAssistantUUID": "40409783-45d5-4240-85d6-22766eec9b15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T10:28:22.516Z_



Now let me fetch all four arxiv abstract pages and run web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e42a50a-d684-4861-a76e-921a05ba061b",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b4cd70e-6f14-4041-9cb4-43d8aaabe8d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-19T10:28:23.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014FMyw3vKREcHAFRRQ5MRth`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.14773",
  "prompt": "Extract the full title, all authors, abstract text, submission date, and any other metadata (subjects, comments about benchmarks/models used). Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b4cd70e-6f14-4041-9cb4-43d8aaabe8d0",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79e089bb-275b-4e77-89fb-94e7a987d1f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-19T10:28:24.407Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XEYEcgjJUa95MSRJh4LhGj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.05419",
  "prompt": "Extract the full title, all authors, abstract text, submission date, and any other metadata (subjects, comments about benchmarks/models used). Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e089bb-275b-4e77-89fb-94e7a987d1f4",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42a5a532-51be-48bb-9c21-931a6859ccc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 10 · 2026-05-19T10:28:25.347Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HFCXuCRi5jq2EhJdWBoRAf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.19827",
  "prompt": "Extract the full title, all authors, abstract text, submission date, and any other metadata (subjects, comments about benchmarks/models used). Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a5a532-51be-48bb-9c21-931a6859ccc5",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b82df653-0b63-4c6a-b9ed-408c6ac888d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-19T10:28:25.877Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DJwiqe8zNLkK3k6TkmRD7V`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22816",
  "prompt": "Extract the full title, all authors, abstract text, submission date, and any other metadata (subjects, comments about benchmarks/models used). Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82df653-0b63-4c6a-b9ed-408c6ac888d5",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dffb2012-8f29-4e19-89e8-35eb0e8f0366",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 12 · 2026-05-19T10:28:26.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pLg3kWEBVV8PQ7pa1Cucx`</summary>

```json
{
  "query": "David \"Temporal Predictors of Outcome in Reasoning Language Models\" arxiv 2511.14773"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dffb2012-8f29-4e19-89e8-35eb0e8f0366",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbebb301-f945-434c-b1e4-a7ed36a296a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 13 · 2026-05-19T10:28:27.295Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUMLjchSZPHHJwEe7vfb2o`</summary>

```json
{
  "query": "Zhang et al \"Reasoning Models Know When They're Right\" arxiv 2504.05419 probe early exit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbebb301-f945-434c-b1e4-a7ed36a296a3",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9eaf5a4c-b1b4-45f9-a472-bf3a0731cb4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

### Tool result

_source line 14 · 2026-05-19T10:28:27.768Z_

<details><summary>↩ Tool result · `toolu_014FMyw3vKREcHAFRRQ5MRth`</summary>

```text
# Paper Metadata Extraction

**Full Title:** "Temporal Predictors of Outcome in Reasoning Language Models"

**Author(s):** Joey David

**Submission Date:** November 3, 2025

**arXiv Identifier:** 2511.14773

**Subject Classification:** Computation and Language (cs.CL)

**Comments:** 4 pages, 4 figures

**Abstract Summary:**
The research investigates timing of outcome commitment in language models using chain-of-thought reasoning. Researchers trained linear classifiers on hidden states after initial reasoning tokens and found "eventual correctness is highly predictable after only a few tokens, even when longer outputs are needed." The work identifies selection artifacts in harder questions and suggests implications for interpretability and inference-time control mechanisms.

**License:** Creative Commons Attribution-ShareAlike 4.0

**DOI:** https://doi.org/10.48550/arXiv.2511.14773

**Access Formats Available:** PDF, HTML (experimental), TeX Source
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79e089bb-275b-4e77-89fb-94e7a987d1f4",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "b163beb8-27c3-403b-873e-7afc87995c50",
  "sourceToolAssistantUUID": "79e089bb-275b-4e77-89fb-94e7a987d1f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T10:28:27.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KvbLNPX7HWpACXj1yjbaU6`</summary>

```json
{
  "query": "Lewis-Lim arxiv 2508.19827 answer confidence trajectories chain of thought"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b163beb8-27c3-403b-873e-7afc87995c50",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "575696af-dd2f-4232-abed-a70d352eafa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 16 · 2026-05-19T10:28:27.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uUCXkSoeo3nW7PRBJ54tW`</summary>

```json
{
  "query": "\"The Illusion of Reasoning\" arxiv 2603.22816 three-mode taxonomy faithfulness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "575696af-dd2f-4232-abed-a70d352eafa1",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmbXasBtEt4mDb1EJA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b75d5001-67fd-4fa8-b4c2-29bb3a27f074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4embbyAAatJKbrV52X5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9407,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 662,
          "cache_read_input_tokens": 9407,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 17 · 2026-05-19T10:28:28.842Z_

<details><summary>↩ Tool result · `toolu_01XEYEcgjJUa95MSRJh4LhGj`</summary>

```text
# Paper Metadata Extract

**Full Title:**
"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"

**Authors:**
Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He

**Submission Date:**
Monday, April 7, 2025 (18:42:01 UTC)

**Subjects:**
Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

**Abstract:**
The paper investigates whether reasoning models can assess correctness of intermediate answers by examining hidden states. Key findings indicate: probes derived from hidden states verify intermediate answers with high accuracy and well-calibrated confidence scores. Models' internal representations encode information about future answer correctness, enabling early prediction. Using the probe as a verifier reduces inference tokens by 24% without performance loss. The authors conclude that reasoning models encode correctness information but fail to leverage it naturally, representing "substantial untapped potential to enhance their efficiency."

**arXiv Identifier:**
2504.05419 [cs.AI]

**DOI:**
https://doi.org/10.48550/arXiv.2504.05419

**Benchmarks/Models:** Not explicitly specified in the abstract or visible metadata
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42a5a532-51be-48bb-9c21-931a6859ccc5",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "cac05734-5860-40de-bc8d-050ca5f52e98",
  "sourceToolAssistantUUID": "42a5a532-51be-48bb-9c21-931a6859ccc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T10:28:29.623Z_

<details><summary>↩ Tool result · `toolu_01HFCXuCRi5jq2EhJdWBoRAf`</summary>

```text
# Paper Metadata Extraction

**Full Title:**
"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?"

**Authors:**
- Samuel Lewis-Lim
- Xingwei Tan
- Zhixue Zhao
- Nikolaos Aletras

**Abstract:**
"Recent work has demonstrated that Chain-of-Thought (CoT) often yields limited gains for soft-reasoning problems such as analytical and commonsense reasoning. CoT can also be unfaithful to a model's actual reasoning. We investigate the dynamics and faithfulness of CoT in soft-reasoning tasks across instruction-tuned, reasoning and reasoning-distilled models. Our findings reveal differences in how these models rely on CoT, and show that CoT influence and faithfulness are not always aligned."

**Submission Date:**
27 August 2025

**Additional Metadata:**
- **arXiv Identifier:** 2508.19827
- **Classification:** Computer Science > Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- **Venue Status:** Accepted at EMNLP 2025 Main Conference
- **DOI:** https://doi.org/10.48550/arXiv.2508.19827
- **Available Formats:** PDF, HTML (experimental), TeX Source
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b82df653-0b63-4c6a-b9ed-408c6ac888d5",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "02fd7401-670a-492b-a36c-5177e6f327e4",
  "sourceToolAssistantUUID": "b82df653-0b63-4c6a-b9ed-408c6ac888d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T10:28:31.112Z_

<details><summary>↩ Tool result · `toolu_01DJwiqe8zNLkK3k6TkmRD7V`</summary>

```text
# Paper Metadata Extraction

**Full Title:**
"Measuring and curing reasoning rigidity: from decorative chain-of-thought to genuine faithfulness"

**Authors:**
- Abhinaba Basu
- Pavan Chakraborty

**Submission Date:**
Submitted 24 March 2026; last revised 13 April 2026 (v3)

**Abstract:**
The authors investigate whether language models genuinely use step-by-step reasoning or produce predetermined answers. They introduce the Step-Level Reasoning Capacity (SLRC) metric with theoretical guarantees and propose LC-CoSR training to reduce reasoning rigidity. Testing 16 frontier models across six domains, they find OpenAI's o4-mini demonstrates the highest faithfulness (74-88% step necessity). Their key finding reveals that reinforcement learning-based reasoning training matters more than thinking tokens. They identify a "faithfulness paradox" where high-performing models show greater susceptibility to sycophancy, leading them to propose the Reasoning Integrity Score combining SLRC and sycophancy resistance.

**Subjects:**
Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

**Comments:**
"Includes SLRC metric with formal guarantees (Theorem 1), LC-CoSR training intervention, Reasoning Integrity Score, and mechanistic analysis"

**Models Evaluated:**
o4-mini, GPT-5.4, Claude Opus, Grok-4, DeepSeek-R1, Gemini 2.5 Pro (16 total)

**arXiv Identifier:** 2603.22816
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dffb2012-8f29-4e19-89e8-35eb0e8f0366",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "f30a8845-7dcc-472e-9de0-a7208bcce0ba",
  "sourceToolAssistantUUID": "dffb2012-8f29-4e19-89e8-35eb0e8f0366",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T10:28:31.460Z_

<details><summary>↩ Tool result · `toolu_013pLg3kWEBVV8PQ7pa1Cucx`</summary>

```text
Web search results for query: "David "Temporal Predictors of Outcome in Reasoning Language Models" arxiv 2511.14773"

Links: [{"title":"[2511.14773] Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/abs/2511.14773"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/html/2511.14773"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?","url":"https://arxiv.org/pdf/2603.19017"},{"title":"Towards Benchmarking and Improving the Temporal Reasoning Capability of   Large Language Models","url":"https://arxiv.org/pdf/2306.08952"}]

I found the paper you're looking for! Here are the details:

**Title:** Temporal Predictors of Outcome in Reasoning Language Models

**Author:** Joey David

**ArXiv ID:** 2511.14773

**Submitted:** November 3, 2025

**Abstract Summary:** The chain-of-thought (CoT) paradigm uses the elicitation of step-by-step rationales as a proxy for reasoning, gradually refining the model's latent representation of a solution. The research shows that eventual correctness is highly predictable after only a few tokens, even when longer outputs are needed to reach a definite answer. For harder questions, a drop in predictive accuracy highlights a selection artifact: hard items are disproportionately represented in long CoTs.

The paper is available on arXiv at: https://arxiv.org/abs/2511.14773


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbebb301-f945-434c-b1e4-a7ed36a296a3",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "8219234c-7056-41e9-84e3-a20cc6c1fb03",
  "sourceToolAssistantUUID": "fbebb301-f945-434c-b1e4-a7ed36a296a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T10:28:34.187Z_

<details><summary>↩ Tool result · `toolu_01KvbLNPX7HWpACXj1yjbaU6`</summary>

```text
Web search results for query: "Lewis-Lim arxiv 2508.19827 answer confidence trajectories chain of thought"

Links: [{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/html/2508.19827"},{"title":"[2508.19827] Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/abs/2508.19827"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2603.08999"},{"title":"Cycles of Thought: Measuring LLM Confidence through Stable Explanations","url":"https://arxiv.org/html/2406.03441"},{"title":"Temporalizing Confidence: Evaluation of Chain-of-Thought Reasoning with Signal Temporal Logic","url":"https://arxiv.org/pdf/2506.08243"},{"title":"Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/pdf/2603.18940"},{"title":"Optimizing Chain-of-Thought Confidence via Topological and Dirichlet Risk Analysis","url":"https://arxiv.org/pdf/2511.06437"}]

Based on the search results, I found the paper you're looking for:

"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?" is a paper by Samuel Lewis-Lim and colleagues that investigates the dynamics and faithfulness of CoT in soft-reasoning tasks across instruction-tuned, reasoning and reasoning-distilled models.

Regarding answer confidence trajectories specifically: The researchers analyzed probability trajectories of the final answer throughout the reasoning steps, with the expectation that if CoT were merely a post-hoc rationalisation, stable confidence with minimal fluctuations would be observed, whereas genuine reasoning should show distinct changes in probability as the model processes intermediate steps.

For most tasks, instruction-tuned models typically show flat trajectories with minimal confidence change, while for reasoning models, the trajectories show that confidence remains high and generally stable in the cue answer, with this flat trajectory occurring even when the CoT faithfully acknowledges the cue.

The findings reveal that CoT influence and faithfulness are not always aligned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "575696af-dd2f-4232-abed-a70d352eafa1",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "acb7307c-66e5-4ce3-b723-6c1cfecd41ed",
  "sourceToolAssistantUUID": "575696af-dd2f-4232-abed-a70d352eafa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T10:28:34.858Z_

<details><summary>↩ Tool result · `toolu_015uUCXkSoeo3nW7PRBJ54tW`</summary>

```text
Web search results for query: ""The Illusion of Reasoning" arxiv 2603.22816 three-mode taxonomy faithfulness"

Links: [{"title":"[2603.22816] The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/abs/2603.22816"},{"title":"The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/html/2603.22816"},{"title":"The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/pdf/2603.22816"},{"title":"(PDF) The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity","url":"https://www.academia.edu/143382468/The_Illusion_of_Thinking_Understanding_the_Strengths_and_Limitations_of_Reasoning_Models_via_the_Lens_of_Problem_Complexity"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"}]

Based on the search results, I found the paper you're looking for:

## "The Illusion of Reasoning" (arxiv 2603.22816)

The paper investigates whether language models genuinely use their step-by-step reasoning steps or generate decorative narratives after the model has already decided.

### Methodology
The researchers introduce step-level faithfulness evaluation - removing one reasoning sentence at a time and checking whether the answer changes - requiring only API access at $1-2 per model per task.

### Three-Mode Taxonomy
Evaluating 13 frontier models across six domains, they find reasoning falls into three modes - not the binary faithful/unfaithful of prior work:

1. **Genuine Reasoning**: Steps matter and CoT is essential (MiniMax: 37% necessity, +69pp from CoT)

2. **Scaffolding**: CoT helps but steps are interchangeable (Kimi on math: 1% necessity, +94pp from CoT)

3. **Decoration**: CoT adds nothing and steps are ornamental (DeepSeek-V3.2 on sentiment: 11% necessity, -1pp from CoT)

### Key Finding
The DeepSeek model family provides clear causal evidence: R1 reasoning-distilled models show 91–93% step necessity on mathematics versus 4% for the general-purpose V3.2—proving that training objective determines faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b75d5001-67fd-4fa8-b4c2-29bb3a27f074",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "44a6e77e-b2eb-43a9-90a6-8941b7c11c35",
  "sourceToolAssistantUUID": "b75d5001-67fd-4fa8-b4c2-29bb3a27f074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T10:28:34.908Z_

<details><summary>↩ Tool result · `toolu_01WUMLjchSZPHHJwEe7vfb2o`</summary>

```text
Web search results for query: "Zhang et al "Reasoning Models Know When They're Right" arxiv 2504.05419 probe early exit"

Links: [{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"[2504.05419v1] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419v1"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Dynamic Early Exit in Reasoning Models","url":"https://arxiv.org/html/2504.15895v1"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.05419"},{"title":"Therefore I am. I Think.","url":"https://arxiv.org/html/2604.01202"},{"title":"FlashThink: An Early Exit Method For Efficient Reasoning","url":"https://arxiv.org/pdf/2505.13949"},{"title":"Towards a Progress Bar for Reasoning: Progress Prediction in Large Reasoning Models","url":"https://arxiv.org/html/2506.23274v2"}]

I found the paper you're searching for! Here's what the research shows:

"Reasoning Models Know When They're Right" by Zhang et al. studies whether reasoning models encode information about answer correctness through probing the model's hidden states.

Key findings include:

- The resulting probe can verify intermediate answers with high accuracy and produces highly calibrated scores.

- The models' hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated.

- The probe is used as a verifier to decide whether to exit reasoning at intermediate answers during inference, reducing the number of inference tokens by 24% without compromising performance.

- The findings confirm that reasoning models do encode a notion of correctness yet fail to exploit it, revealing substantial untapped potential to enhance their efficiency.

The paper (arXiv 2504.05419) was published on April 7, 2025, and involves authors from New York University and NYU Shanghai.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9eaf5a4c-b1b4-45f9-a472-bf3a0731cb4a",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "397375fe-c903-4f47-bfcd-84d69ab5466c",
  "sourceToolAssistantUUID": "9eaf5a4c-b1b4-45f9-a472-bf3a0731cb4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T10:28:38.634Z_

Good, I have the abstracts and initial search results. Let me now fetch the full HTML versions for more details on models, benchmarks, and methodology, and run additional searches for citations and discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "397375fe-c903-4f47-bfcd-84d69ab5466c",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f2caec-5b28-44f4-b81f-fde1b29a2de8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 25 · 2026-05-19T10:28:41.150Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DaoS2KvzykdbwNivgJ2HzM`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.14773",
  "prompt": "Extract detailed methodology: What specific models were used? What benchmarks/datasets? How exactly are the linear classifiers trained (what layer, what token position, what features)? What are the key quantitative results (accuracy of prediction at different token counts)? What do they find about hard vs easy questions? What are the main figures showing?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f2caec-5b28-44f4-b81f-fde1b29a2de8",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9213ffbd-4281-4689-a6c4-ac4f00eb56a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 26 · 2026-05-19T10:28:43.765Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017Rr89HSQGx7Ecm4kNmQMEK`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.05419v1",
  "prompt": "Extract detailed methodology: What specific models were used (e.g. QwQ, DeepSeek-R1)? What benchmarks/datasets? How exactly are the probes trained - at what token positions (intermediate answer positions)? What layers? What is the probe architecture? What are the key quantitative results for verification accuracy and the early-exit token savings? How does the early-exit mechanism work specifically?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9213ffbd-4281-4689-a6c4-ac4f00eb56a2",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "169a81fd-3a73-43db-8c2c-10adbea25f78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 27 · 2026-05-19T10:28:46.165Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BruMrxCZXmGyVGvF6DHNWR`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.19827",
  "prompt": "Extract detailed methodology: What specific models were used? What benchmarks/datasets? How exactly do they track answer confidence trajectories - what probability are they measuring, at which positions? How do they measure faithfulness? What is the relationship between CoT dynamics and faithfulness? What are the key quantitative results? What do they find about instruction-tuned vs reasoning vs reasoning-distilled models? What do the trajectory shapes look like?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "169a81fd-3a73-43db-8c2c-10adbea25f78",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a044f3-c0d7-4d0b-a411-3e5972f831a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 28 · 2026-05-19T10:28:48.053Z_

<details><summary>↩ Tool result · `toolu_01DaoS2KvzykdbwNivgJ2HzM`</summary>

```text
# Detailed Methodology Summary

## Models Tested
The researchers evaluated two 8B-parameter models:
- **Qwen3-8B**: Explicitly fine-tuned for reasoning with structured reasoning mode enabled
- **Llama3.1-8B-Instruct**: General instruction-tuned model (as a control to show the signal exists beyond reasoning-specialized architectures)

## Dataset
The study used the Hendrycks MATH dataset, split into difficulty-balanced buckets:
- 750 easy problems (difficulty levels 1-2)
- 750 hard problems (difficulty levels 4-5)
- Total: 1,500 examples

Qwen3-8B achieved 85.1% accuracy on easy items but only 32.1% on hard ones.

## Linear Classifier Training
The methodology involved:
- Extracting "final hidden states of the last four reasoning tokens at fixed prefix lengths" (t ∈ {4, 8, 16, 32, 64, 128, 192, 256, 384, 512})
- Applying PCA dimensionality reduction (down to 128 components maximum)
- Training "ℓ₂-regularized logistic regression probe"
- Using 80/20 stratified train-test split with balanced class weights

## Key Quantitative Results
- At t=4 tokens: ROC-AUC of 0.84 and accuracy of 0.76
- Performance "remain[s] high—around 0.8—well into the 100 token mark"
- Easy vs. hard questions at t=4: AUC 0.77 vs. 0.72 respectively
- Output-space baselines (entropy+length) achieved only 0.59 AUC at t=8

## Hard vs. Easy Question Findings
The analysis revealed that performance appears to degrade at longer prefixes because "only the hardest examples in the remaining pool" survive as questions complete—this represents a selection artifact rather than actual signal degradation.

## Main Figures
- **Figure 4** displays ROC-AUC and accuracy curves stratified by difficulty level across prefix lengths
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9213ffbd-4281-4689-a6c4-ac4f00eb56a2",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "50babd5d-ce40-422c-8e68-552cf3655dbc",
  "sourceToolAssistantUUID": "9213ffbd-4281-4689-a6c4-ac4f00eb56a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T10:28:48.103Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0171QJuo85xNjs1r2y1FUqgV`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22816",
  "prompt": "Extract detailed methodology: What specific models were evaluated (all 13+)? What six domains/benchmarks? How exactly does the step-level faithfulness evaluation work (SLRC metric)? What is LC-CoSR training? What is the Reasoning Integrity Score? What are the key quantitative results? What do they find about o4-mini vs other models? What is the faithfulness paradox? How does RL training relate to faithfulness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50babd5d-ce40-422c-8e68-552cf3655dbc",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae97ae88-039c-4514-bcd2-415134c8244d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 30 · 2026-05-19T10:28:49.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVQmwtjeYrM6rQXiwh4y3A`</summary>

```json
{
  "query": "arxiv 2511.14773 Joey David reasoning model linear classifier hidden states DeepSeek QwQ model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae97ae88-039c-4514-bcd2-415134c8244d",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25a9c752-ec06-4b3a-ad96-08ff0fef1cb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 31 · 2026-05-19T10:28:49.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WaurDpmb9QpQAFCri8FeMd`</summary>

```json
{
  "query": "\"Reasoning Models Know When They're Right\" Zhang 2025 citation discussion QwQ DeepSeek probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25a9c752-ec06-4b3a-ad96-08ff0fef1cb5",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34ee7e85-ee9f-4e05-9a1c-5470d4fca1f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 32 · 2026-05-19T10:28:50.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012TcefpuWGXdVQ7TjKvgrf4`</summary>

```json
{
  "query": "Lewis-Lim \"Analysing Chain of Thought Dynamics\" EMNLP 2025 answer probability trajectory faithfulness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ee7e85-ee9f-4e05-9a1c-5470d4fca1f9",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cea7fd19-5b00-4882-bc07-24dc6fb6ab9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
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

_source line 33 · 2026-05-19T10:28:51.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UEDVHqCR277QP7QMArfr9b`</summary>

```json
{
  "query": "Basu Chakraborty \"Measuring and curing reasoning rigidity\" 2603.22816 SLRC step-level metric 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cea7fd19-5b00-4882-bc07-24dc6fb6ab9c",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmceR9mF3tevRVcMDn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e48fcfa0-1508-4866-b51a-45bde6ee7623",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXS2W3a3Uh8u2ojgdqppxJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1331,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 10533,
      "output_tokens": 918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1331,
          "output_tokens": 918,
          "cache_read_input_tokens": 10533,
          "cache_creation_input_tokens": 3172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3172,
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

_source line 34 · 2026-05-19T10:28:52.602Z_

<details><summary>↩ Tool result · `toolu_017Rr89HSQGx7Ecm4kNmQMEK`</summary>

```text
# Methodology Summary

## Models Used
The study employed several reasoning models: DeepSeek-R1-Distill series (Llama-8B, Llama-70B, Qwen-1.5B, Qwen-7B, Qwen-32B) and QwQ-32B, all trained with long Chain-of-Thought (CoT) data.

## Datasets
Four benchmarks were evaluated: GSM8K, MATH, AIME (mathematical reasoning), and KnowLogic (logical reasoning with ~5.4k multiple-choice questions).

## Probe Training Methodology

**Data Collection Process:**
The researchers segmented long reasoning traces into chunks by identifying keywords like "wait," "double-check," and "alternatively" that signal new reasoning paths. Using Gemini 2.0 Flash, they extracted intermediate answers and labeled correctness against ground truth.

**Representation Extraction:**
"For each chunk, they take the last-layer hidden states at the last token position as its representation." This captures the model's internal state immediately after completing an intermediate answer.

**Probe Architecture:**
A two-layer MLP classifier was trained with the formula: output = sigmoid(ReLU(hidden_state × W₁ + b₁) × W₂ + b₂). The hidden dimension d ranged from 0-32 tokens during grid search, with many converging to linear probes (d=0).

## Key Results

**Verification Accuracy:**
ROC-AUC scores exceeded 0.7 in-distribution across datasets, with R1-Distill-Qwen-32B reaching "over 0.9 ROC-AUC score on AIME." Expected Calibration Error remained below 0.1, indicating well-calibrated confidence estimates.

**Early-Exit Performance:**
"At threshold 0.85, the strategy achieves roughly the same reasoning accuracy (88.2%) as no early-exit, while reducing generated tokens by approximately 24%." At threshold 0.9, identical accuracy was maintained with 19% token reduction.

## Early-Exit Mechanism

The system sequentially evaluates intermediate answers during inference. Once a probe-generated confidence score exceeds a predefined threshold, reasoning terminates and that answer becomes final. This contrasts with static baselines that stop after m fixed chunks, demonstrating "up to 5% accuracy improvement" when controlling for equivalent token usage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "169a81fd-3a73-43db-8c2c-10adbea25f78",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "eacc9852-b820-47aa-ba6e-9ffff9bec5cb",
  "sourceToolAssistantUUID": "169a81fd-3a73-43db-8c2c-10adbea25f78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T10:28:54.850Z_

<details><summary>↩ Tool result · `toolu_01FVQmwtjeYrM6rQXiwh4y3A`</summary>

```text
Web search results for query: "arxiv 2511.14773 Joey David reasoning model linear classifier hidden states DeepSeek QwQ model"

Links: [{"title":"[2511.14773] Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/abs/2511.14773"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/html/2511.14773"},{"title":"LLM Reasoning Does Not Protect Against Clinical Cognitive Biases - An Evaluation Using BiasMedQA","url":"https://www.medrxiv.org/content/10.1101/2025.06.22.25330078.full.pdf"},{"title":"System and method for reasoning about the diversity and robustness of an ensemble of classifiers","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12353994"},{"title":"Cognitive-Mental-LLM: Evaluating Reasoning in Large Language Models for Mental Health Prediction via Online Text","url":"https://arxiv.org/pdf/2503.10095"},{"title":"TextReasoningBench: Does Reasoning Really Improve Text Classification in Large Language Models?","url":"https://arxiv.org/pdf/2603.19558"},{"title":"On Robustness of Linear Classifiers to Targeted Data Poisoning","url":"https://arxiv.org/html/2511.12722v1"}]

I found the arxiv paper you're looking for! Here's what I found:

The paper is titled "Temporal Predictors of Outcome in Reasoning Language Models" by Joey David, submitted November 3, 2025.

The research probes how early an LLM internally commits to an outcome by training linear classifiers on hidden states after the first t reasoning tokens, showing that eventual correctness is highly predictable after only a few tokens, even when longer outputs are needed to reach a definite answer.

For harder questions, the study shows a drop in predictive accuracy highlighting a selection artifact where hard items are disproportionately represented in long CoTs, with overall results implying that for reasoning models, internal self-assessment of success tends to emerge after only a few tokens, with implications for interpretability and inference-time control.

You can access the full paper at https://arxiv.org/abs/2511.14773. While the search results don't specifically mention the DeepSeek QwQ model, that detail may be covered in the full paper itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25a9c752-ec06-4b3a-ad96-08ff0fef1cb5",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "05e7f2a7-ecf6-44bb-a7cf-62887d5ca601",
  "sourceToolAssistantUUID": "25a9c752-ec06-4b3a-ad96-08ff0fef1cb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T10:28:55.160Z_

<details><summary>↩ Tool result · `toolu_01BruMrxCZXmGyVGvF6DHNWR`</summary>

```text
# Detailed Methodology Summary

## Models Tested
The study examined three model categories:
- **Instruction-tuned**: Qwen2.5-7B/32B-Instruct, Llama-8B-Instruct
- **Multi-step Reasoning**: Qwen3-32B, QwQ-32B (trained with reasoning-specific reinforcement learning)
- **Distilled-Reasoning**: R1-Distill variants (7B, 32B) based on DeepSeek-R1

## Datasets
Five soft-reasoning benchmark sets were used: CSQA (commonsense), StrategyQA, MUSR (semi-symbolic), LSAT (analytical), and GPQA (graduate-level science). All featured multiple-choice questions, totaling 5,518 examples.

## Confidence Trajectory Measurement
Researchers tracked model confidence by computing softmax probabilities of the final chosen answer across sequential CoT steps. Formally, they measured `c_i = P(final_answer | prompt, reasoning_steps_1_to_i)` at each step. For reasoning models, they used content between `&lt;think>` tags; for others, they segmented CoT by double line breaks and explicitly prompted step-wise answers.

## Faithfulness Assessment
Two misleading cues were injected:
1. **Professor cue**: Appending statements like "A Stanford Professor thinks the answer is X"
2. **Metadata cue**: Embedding XML-style hint tags with answer values

The researchers identified unfaithful CoTs where models changed answers matching the cue but failed to verbally acknowledge using that cue. They employed GPT-4.1 to classify whether CoTs explicitly articulated cue influence.

## Key Findings

**Answer Change Rates**:
- Distilled models changed initial answers ~65% of time
- Instruction-tuned and reasoning models changed answers ~24-25%

**Trajectory Patterns**:
- Instruction-tuned models displayed flat trajectories, suggesting post-hoc rationalization
- Distilled models showed increasing confidence toward final answers, with sharp increases often near the conclusion
- Reasoning models exhibited mixed behavior—mostly flat but occasionally more dynamic on difficult tasks

**Influence-Faithfulness Disconnect**:
The crucial finding: "unfaithful CoTs can still guide model confidence" while faithful acknowledgments sometimes don't influence final answers. Distilled models demonstrated this disconnect most prominently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3a044f3-c0d7-4d0b-a411-3e5972f831a4",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "5097aa03-f265-49e9-afbe-c9e1d7647e3b",
  "sourceToolAssistantUUID": "f3a044f3-c0d7-4d0b-a411-3e5972f831a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T10:28:55.448Z_

<details><summary>↩ Tool result · `toolu_01WaurDpmb9QpQAFCri8FeMd`</summary>

```text
Web search results for query: ""Reasoning Models Know When They're Right" Zhang 2025 citation discussion QwQ DeepSeek probing"

Links: [{"title":"Do Reasoning Models Know When They're Right?","url":"https://aclanthology.org/2025.emnlp-main.73.pdf"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Thinking Out Loud: Do Reasoning Models Know When They’re Right?","url":"https://arxiv.org/html/2504.06564v3"},{"title":"Reasoning Models Know When They’re Right | CSDSE | NYU Shanghai","url":"https://cs.shanghai.nyu.edu/news/reasoning-models-know-when-theyre-right"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"}]

Great! I found the research you're looking for. Here's information about the paper:

## Paper Overview

The paper "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification" is by Anqi Zhang and colleagues from New York University and NYU Shanghai.

## Key Research Question and Findings

The research addresses whether reasoning models can evaluate the correctness of their intermediate answers during reasoning by probing the model's hidden states. The resulting probe can verify intermediate answers with high accuracy and produces highly calibrated scores.

## Models Studied

The research uses models like DeepSeek-R1-Distill and QwQ-32B, along with other reasoning models mentioned in the citations.

## Main Contributions

While reasoning models suffer from overthinking with unnecessary steps even after reaching correct answers, their hidden states encode correctness of both intermediate and future answers. 

Using the probe as a verifier to decide whether to exit reasoning at intermediate answers during inference reduced inference tokens by 24% without compromising performance.

## Significance

The findings confirm that reasoning models do encode a notion of correctness yet fail to exploit it, revealing substantial untapped potential to enhance their efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ee7e85-ee9f-4e05-9a1c-5470d4fca1f9",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "3fc646c7-4ae2-4881-b791-f585c387ed6e",
  "sourceToolAssistantUUID": "34ee7e85-ee9f-4e05-9a1c-5470d4fca1f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T10:28:57.650Z_

<details><summary>↩ Tool result · `toolu_01UEDVHqCR277QP7QMArfr9b`</summary>

```text
Web search results for query: "Basu Chakraborty "Measuring and curing reasoning rigidity" 2603.22816 SLRC step-level metric 2026"

Links: [{"title":"[2603.22816] The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/abs/2603.22816"},{"title":"[2603.22816v1] When AI Shows Its Work, Is It Actually Working? Step-Level Evaluation Reveals Frontier Language Models Frequently Bypass Their Own Reasoning","url":"https://arxiv.org/abs/2603.22816v1"},{"title":"Reasoning Model is Stubborn: Diagnosing Instruction Overriding in Reasoning Models","url":"https://arxiv.org/pdf/2505.17225"},{"title":"The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models","url":"https://arxiv.org/html/2603.22816"},{"title":"[2603.20508] Measuring Reasoning Trace Legibility: Can Those Who Understand Teach?","url":"https://arxiv.org/abs/2603.20508"}]

Based on the search results, I found information about the paper you're asking about. The query appears to be referring to arXiv paper 2603.22816, but with some clarifications needed about the details:

The paper is authored by Abhinaba Basu and Pavan Chakraborty (note: the author name in your query appears to be "Chakraborty" rather than "Basu Chakraborty"). 

The actual title of the paper is "The illusion of reasoning: step-level evaluation reveals decorative chain-of-thought in frontier language models" - not "Measuring and curing reasoning rigidity" as mentioned in your query.

The paper does introduce a step-level evaluation metric. The method involves removing one reasoning sentence at a time and checking whether the answer changes, requiring only API access with no model weights needed, at $1–2 per model per task.

The study evaluated 13 frontier models across six domains with N=376-500 each, and discovered "output rigidity" - models that shortcut internally also refuse to explain externally.

It appears your query may have been combining details from multiple related papers on reasoning in language models. The paper 2603.22816 uses a step-level metric but focuses on evaluating chain-of-thought faithfulness rather than "curing reasoning rigidity."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e48fcfa0-1508-4866-b51a-45bde6ee7623",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "5aab60ff-34c9-4d5d-bc84-a8aeecdddeff",
  "sourceToolAssistantUUID": "e48fcfa0-1508-4866-b51a-45bde6ee7623",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T10:28:58.885Z_

<details><summary>↩ Tool result · `toolu_012TcefpuWGXdVQ7TjKvgrf4`</summary>

```text
Web search results for query: "Lewis-Lim "Analysing Chain of Thought Dynamics" EMNLP 2025 answer probability trajectory faithfulness"

Links: [{"title":"[PDF] Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analysing-Chain-of-Thought-Dynamics:-Active-or-Lewis-Lim-Tan/f33ba21e7e699fbc772b1c0b537986342f214ccd"},{"title":"[2508.19827] Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/abs/2508.19827"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"},{"title":"Explainable Chain-of-Thought Reasoning: An Empirical Analysis on State-Aware Reasoning Dynamics","url":"https://arxiv.org/pdf/2509.00190"},{"title":"Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought","url":"https://arxiv.org/pdf/2509.23365"}]

Based on the search results, I found the paper you're looking for:

"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?" is a paper by Samuel Lewis-Lim, Xingwei Tan, Zhixue Zhao, and Nikolaos Aletras from 2025.

The paper investigates the dynamics and faithfulness of CoT in soft-reasoning tasks across instruction-tuned, reasoning and reasoning-distilled models, revealing differences in how these models rely on CoT and showing that CoT influence and faithfulness are not always aligned.

A key question the paper addresses is why CoT fails on soft-reasoning tasks: whether it just provides a post-hoc rationalisation for a predetermined answer, or acts as influential yet ineffective reasoning for these tasks.

The paper appears to be available on arXiv (ID: 2508.19827). While the search results don't provide specific details about "answer probability trajectory" metrics, the paper's focus on the alignment between CoT influence and faithfulness relates to your query about analyzing how Chain of Thought reasoning evolves and whether it genuinely guides the model's reasoning process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cea7fd19-5b00-4882-bc07-24dc6fb6ab9c",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "114117b5-39aa-45e8-b2ab-0b53117a8bdc",
  "sourceToolAssistantUUID": "cea7fd19-5b00-4882-bc07-24dc6fb6ab9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T10:29:01.424Z_

<details><summary>↩ Tool result · `toolu_0171QJuo85xNjs1r2y1FUqgV`</summary>

```text
# Research Paper Summary: Measuring Chain-of-Thought Faithfulness

## Models Evaluated

The study examined **16 frontier models** including:
- OpenAI: GPT-5.4, o4-mini
- Anthropic: Claude Opus 4.6-R
- DeepSeek: V3.2, R1-32B, R1-70B
- Others: Grok-4, Gemini 2.5 Pro, Kimi-K2.5, MiniMax-M2.5, Qwen variants, GLM-5, Nemotron-Ultra, GPT-OSS-120B

Plus six smaller open-weight models (0.8–8B parameters).

## Six Evaluation Domains

1. Sentiment classification (SST-2)
2. Mathematical reasoning (GSM8K)
3. Topic classification (AG News)
4. Medical QA (MedQA)
5. Commonsense reasoning (CommonsenseQA)
6. Science reasoning (ARC-Challenge)

## SLRC Metric Methodology

The Step-Level Reasoning Capacity metric works through three tests per reasoning step:

**Necessity:** "Remove step ii, present remaining steps, check if answer changes"

**Sufficiency:** "Present step ii alone, check if answer recovers"

**Formula:** SLRC = Necessity × (1 − Sufficiency), ranging from 0 (decorative) to 1 (genuinely sequential)

This requires only API access (~$1–2 per model-task pair) with no weight access needed.

## Key Quantitative Results

**RL-trained reasoning models** showed highest faithfulness:
- o4-mini: 74–88% step necessity on five of six tasks (SLRC = 0.87 on sentiment)
- DeepSeek-R1: 91–93% necessity on mathematics (SLRC = 0.86)

**General-purpose models** showed decorative reasoning:
- GPT-5.4: 0.1% necessity on sentiment (SLRC = 0.00)
- Claude Opus: ≤15% necessity across all tasks

**Critical finding:** Thinking tokens without RL training remained decorative—Grok-4 reasoning mode showed only 1.4% necessity despite producing thinking tokens, lower than its non-reasoning mode (7.2%).

## Three Modes of Behavior

1. **Genuine Reasoning:** Steps matter; individual removal changes answers; CoT improves accuracy
2. **Scaffolding:** Structure helps accuracy, but "steps are interchangeable" (Kimi-K2.5: +94pp from CoT yet 1% necessity)
3. **Decoration:** Neither improves accuracy nor contains necessary steps

## The Faithfulness Paradox

High-SLRC models proved more susceptible to sycophancy (accepting false answers when prompted). The correlation between faithfulness and manipulability was ρ = 0.53.

## Reasoning Integrity Score (RIS)

Developed to capture deployment safety: **RIS = SLRC × (1 − Sycophancy Rate)**

This metric significantly predicted error detection ability (ρ = 0.66, p = 0.026), outperforming SLRC alone.

## LC-CoSR Training Method

Lyapunov-Constrained Contrastive Step Reinforcement combines:
- Direct reward when step removal changes answers
- Lyapunov stability bound: V(θ) ≥ V_min throughout training
- Requires only 2 forward passes per example on single GPU

Preliminary results showed 2.6× less negative reward (−0.13 vs. −0.34) than baseline methods without requiring external models.

## RL Training as Determinant

The research established that **reinforcement learning focused on reasoning tasks—not scale, architecture, or thinking tokens—determined faithfulness.** Models with identical parameter counts but different training showed divergent results; same organizations' RL-trained reasoning models (OpenAI's o4-mini, DeepSeek's R1) independently achieved genuine faithfulness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae97ae88-039c-4514-bcd2-415134c8244d",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "66750df6-58bf-4c6c-aae3-3bc1225f3ec3",
  "sourceToolAssistantUUID": "ae97ae88-039c-4514-bcd2-415134c8244d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T10:29:05.890Z_

Now let me get some more details on the specific models/benchmarks and related work for proper positioning. Let me also search for how these papers cite or relate to each other.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66750df6-58bf-4c6c-aae3-3bc1225f3ec3",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmebmiNn3qQeyK9S7wp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "740de61d-47f6-42a4-a634-33ab946e6fee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDS4V8xJr3cLU8Puxuu43k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2479,
      "cache_creation_input_tokens": 4915,
      "cache_read_input_tokens": 13705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4915,
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

_source line 42 · 2026-05-19T10:29:06.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015gty9CG7iz71o75ehvezj5`</summary>

```json
{
  "query": "probing hidden states reasoning models chain of thought faithfulness temporal information flow 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "740de61d-47f6-42a4-a634-33ab946e6fee",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmebmiNn3qQeyK9S7wp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4abd8fe9-9f22-453c-91a4-8dbe82e69f50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDS4V8xJr3cLU8Puxuu43k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2479,
      "cache_creation_input_tokens": 4915,
      "cache_read_input_tokens": 13705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4915,
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

_source line 43 · 2026-05-19T10:29:07.227Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012bFBEdPhUS9qtoX15YEzwc`</summary>

```json
{
  "query": "\"early exit\" reasoning models probing correctness chain of thought 2504.05419 cited by"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4abd8fe9-9f22-453c-91a4-8dbe82e69f50",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmebmiNn3qQeyK9S7wp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94ae5b41-737a-4dbd-b1d7-bf7a536e9b12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDS4V8xJr3cLU8Puxuu43k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2479,
      "cache_creation_input_tokens": 4915,
      "cache_read_input_tokens": 13705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4915,
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

_source line 44 · 2026-05-19T10:29:07.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nn7fBSRPatFRAsFPBGwbkX`</summary>

```json
{
  "query": "Lewis-Lim Tan Zhao Aletras EMNLP 2025 CoT dynamics confidence trajectory instruction-tuned reasoning distilled models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94ae5b41-737a-4dbd-b1d7-bf7a536e9b12",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmebmiNn3qQeyK9S7wp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48f2c828-22c7-488a-a5ae-b5a831cab10f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDS4V8xJr3cLU8Puxuu43k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2479,
      "cache_creation_input_tokens": 4915,
      "cache_read_input_tokens": 13705,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2479,
          "output_tokens": 235,
          "cache_read_input_tokens": 13705,
          "cache_creation_input_tokens": 4915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4915,
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

_source line 45 · 2026-05-19T10:29:14.249Z_

<details><summary>↩ Tool result · `toolu_012bFBEdPhUS9qtoX15YEzwc`</summary>

```text
Web search results for query: ""early exit" reasoning models probing correctness chain of thought 2504.05419 cited by"

Links: [{"title":"Therefore I am. I Think.","url":"https://arxiv.org/html/2604.01202"},{"title":"Dynamic Early Exit in Reasoning Models","url":"https://arxiv.org/html/2504.15895v1"},{"title":"When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning","url":"https://arxiv.org/pdf/2604.06787"},{"title":"S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models","url":"https://arxiv.org/pdf/2505.07686"},{"title":"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought","url":"https://arxiv.org/pdf/2603.05488"},{"title":"Entropy After &lt;/Think> for reasoning model early exiting","url":"https://arxiv.org/pdf/2509.26522"},{"title":"Dynamic Early Exit in Reasoning Models DYNAMIC EARLY EXIT IN REASONING MODELS","url":"https://arxiv.org/pdf/2504.15895"}]

Based on the search results, here's what I found about the paper and its citations:

## Paper Details

The paper you're referencing is "Reasoning models know when they're right: probing hidden states for self-verification" by A. Zhang, Y. Chen, J. Pan, C. Zhao, A. Panda, J. Li, and H. He (2025), with arXiv ID 2504.05419.

## Research Focus

The paper shows that hidden states encode information about answer correctness early enough to enable early exit. The work contributes to a broader research area investigating how reasoning models can detect when they've arrived at correct answers and potentially terminate reasoning early.

## Related Work and Citations

The paper has been cited by several recent works on early exit in reasoning models:

1. A paper titled "Dynamic Early Exit in Reasoning Models" cites this work directly, which proposes to terminate early based on trial answers but requires an additional probe model to determine correctness.

2. Another work introduces Dynamic Thought Sufficiency in Reasoning (DTSR), a framework that enables models to dynamically assess the sufficiency of their chain-of-thought and determine the optimal point for early exit.

3. A paper called "Reasoning Theater" uses probe-guided early exit to reduce tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94ae5b41-737a-4dbd-b1d7-bf7a536e9b12",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "01c92978-5d20-442f-9067-439ad5fa975a",
  "sourceToolAssistantUUID": "94ae5b41-737a-4dbd-b1d7-bf7a536e9b12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T10:29:15.317Z_

<details><summary>↩ Tool result · `toolu_015gty9CG7iz71o75ehvezj5`</summary>

```text
Web search results for query: "probing hidden states reasoning models chain of thought faithfulness temporal information flow 2025 2026 survey"

Links: [{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/html/2510.09312v1"},{"title":"Data Mining and Machine Learning Lab Is Chain-of-Thought Reasoning of LLMs a","url":"https://arxiv.org/pdf/2508.01191"},{"title":"Deep Hidden Cognition Facilitates Reliable Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2507.10007"},{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful","url":"https://arxiv.org/pdf/2503.08679"}]

I found several highly relevant research papers on this topic from 2025-2026. Here's what the search revealed:

## Key Research Areas

**Probing Hidden States for Correctness**: Recent work trains linear classifiers on hidden states after the first t reasoning tokens, showing that eventual correctness is highly predictable after only a few tokens. Models' hidden states encode correctness of future answers, enabling early prediction of correctness before the intermediate answer is fully formulated.

**Chain-of-Thought Faithfulness**: Approaches probe CoT faithfulness by perturbing reasoning traces, for example by adding mistakes, removing steps, or forcing early answers, and then testing whether the final prediction changes accordingly. However, recent studies reveal that CoTs are often unfaithful: they may contain factual mistakes, incoherent steps, or post-hoc rationalizations that obscure the true reasoning process.

**Temporal Information Flow**: Research predicts answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated, not only after initial question or the final answer. Hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.

**Reasoning Model Efficiency**: Probes can be used as verifiers to decide whether to exit reasoning at intermediate answers during inference, reducing the number of inference tokens by 24% without compromising performance, revealing substantial untapped potential to enhance their efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4abd8fe9-9f22-453c-91a4-8dbe82e69f50",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "50d7fc91-630c-4bc4-b4d0-c5e45a26b576",
  "sourceToolAssistantUUID": "4abd8fe9-9f22-453c-91a4-8dbe82e69f50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T10:29:23.082Z_

<details><summary>↩ Tool result · `toolu_01Nn7fBSRPatFRAsFPBGwbkX`</summary>

```text
Web search results for query: "Lewis-Lim Tan Zhao Aletras EMNLP 2025 CoT dynamics confidence trajectory instruction-tuned reasoning distilled models"

Links: [{"title":"Our EMNLP 2025 Papers - Institute of Artificial Intelligence","url":"https://ai.ucf.edu/our-emnlp-2025-papers/"},{"title":"Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1624/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"EMNLP 2025 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/emnlp-2025"},{"title":"Evaluating large language models for natural-language-to-code generation on aggregate Czech public health data analysis","url":"https://www.medrxiv.org/content/10.64898/2025.12.05.25341697.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"}]

Let me search more specifically for the paper with the complete author list and topic keywords:

Links: [{"title":"Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://aclanthology.org/2025.emnlp-main.1516.pdf"},{"title":"Verbalized Confidence Triggers Self-Verification : Emergent Behavior Without Explicit Reasoning Supervision","url":"https://arxiv.org/html/2506.03723"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"},{"title":"1 Introduction","url":"https://arxiv.org/html/2507.08182v2"},{"title":"Distilling LLM Agent into Small Models with Retrieval and Code Tools","url":"https://arxiv.org/html/2505.17612"},{"title":"R-Stitch: Dynamic Trajectory Stitching for Efficient Reasoning","url":"https://arxiv.org/html/2507.17307v2"},{"title":"Reasoning Models Better Express Their Confidence","url":"https://arxiv.org/pdf/2505.14489"},{"title":"Effectiveness of Chain-of-Thought in Distilling Reasoning Capability from Large Language Models","url":"https://arxiv.org/pdf/2511.05184"}]

Great! I found the paper. Let me search for more specific information about the authors to confirm:

Links: [{"title":"LLM-Based Annotation and Token-Augmented Modeling for Emotional Tone Classification in Online Cancer Peer-Support Posts","url":"https://www.medrxiv.org/content/10.64898/2026.01.27.26344999.full.pdf"},{"title":"Identifying Brain Regions Related to Word Prediction During Listening to Japanese Speech by Combining a LSTM Language Model and MEG","url":"https://www.biorxiv.org/content/10.1101/2021.03.25.436887.full.pdf"},{"title":"Mapping echocardiogram reports to a structured ontology: a task for statistical machine learning or large language models?","url":"https://www.medrxiv.org/content/10.1101/2024.02.20.24302419.full.pdf"},{"title":"A clinical specific BERT developed with huge size of Japanese clinical narrative","url":"https://www.medrxiv.org/content/10.1101/2020.07.07.20148585.full.pdf"},{"title":"A Study to Assess the Safety and Immune Response to Env-C DNA and Protein Vaccines in Kenya","url":"https://cdn.clinicaltrials.gov/large-docs/94/NCT04826094/SAP_001.pdf"},{"title":"A multitask bi-directional RNN model for named entity recognition on Chinese electronic medical records","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6309059/"},{"title":"Brain-Informed Fine-Tuning for Improved Multilingual Understanding in Language Models","url":"https://www.biorxiv.org/content/10.1101/2025.07.07.662360.full.pdf"}]

Let me try a more direct search for the paper title:

Links: [{"title":"[2508.19827] Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/abs/2508.19827"},{"title":"[PDF] Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analysing-Chain-of-Thought-Dynamics:-Active-or-Lewis-Lim-Tan/f33ba21e7e699fbc772b1c0b537986342f214ccd"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"},{"title":"Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought","url":"https://arxiv.org/pdf/2509.23365"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/html/2508.19827"}]

Perfect! I found comprehensive information about the paper. Here are the search results:

## Search Results

The paper is titled "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?" by Samuel Lewis-Lim, Xingwei Tan, Zhixue Zhao, and Nikolaos Aletras from the School of Computer Science at the University of Sheffield.

The paper investigates the dynamics and faithfulness of CoT in soft-reasoning tasks across instruction-tuned, reasoning and reasoning-distilled models, revealing differences in how these models rely on CoT and showing that CoT influence and faithfulness are not always aligned.

Key findings from the research include:

- For most tasks, instruction-tuned models typically show flat trajectories with minimal confidence change, suggesting mostly post-hoc behaviour.

- Distilled-reasoning models change their initial answer on average in 65% of cases across all distilled models and datasets, over two and a half times the rate of instruction-tuned models (25%) and full reasoning models (24%).

- Distilled-reasoning models consistently demonstrate trajectories with clear increases in final answer probability during CoT, unlike the minimal answer changes observed for chat models.

The paper was submitted to arXiv on August 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f2c828-22c7-488a-a5ae-b5a831cab10f",
  "isSidechain": true,
  "promptId": "4c390cce-cad6-445a-98d6-44351b07c6e9",
  "agentId": "adf0ac9b242421c10",
  "type": "user",
  "uuid": "fcd04412-34a7-4773-bb61-0c16ce5a7225",
  "sourceToolAssistantUUID": "48f2c828-22c7-488a-a5ae-b5a831cab10f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-19T10:30:52.844Z_

I now have thorough information on all four papers. Let me compile a comprehensive analysis.

---

Here is the detailed analysis of all four papers:

---

## Paper 1: David (2511.14773) -- "Temporal Predictors of Outcome in Reasoning Language Models"

**Authors:** Joey David
**Date:** November 3, 2025
**Length:** 4 pages (short paper)

**What they do:** Train L2-regularized logistic regression probes on hidden states extracted after the first *t* reasoning tokens (at prefix lengths t = 4, 8, 16, 32, 64, 128, 192, 256, 384, 512). Specifically, they take the final hidden states of the last four reasoning tokens at each prefix length, apply PCA (down to 128 components), and train binary classifiers predicting whether the model will ultimately answer correctly.

**Models:** Two 8B-parameter models: **Qwen3-8B** (reasoning-specialized) and **Llama-3.1-8B-Instruct** (general instruction-tuned, as control).

**Benchmarks:** Hendrycks MATH dataset -- 750 easy problems (levels 1-2) and 750 hard problems (levels 4-5), totaling 1,500 examples.

**Key results:**
- At t=4 tokens: ROC-AUC of **0.84**, accuracy of **0.76**
- Performance remains around **0.8 AUC** well past 100 tokens
- Output-space baselines (entropy + length) achieve only **0.59 AUC** at t=8
- Easy vs. hard at t=4: AUC 0.77 vs. 0.72

**Key contribution:** Demonstrates that a model's eventual correctness is *linearly decodable* from hidden states after as few as 4 tokens of reasoning. The apparent accuracy drop at longer prefixes is explained as a **selection artifact** -- only the hardest problems survive to long CoT lengths, so the remaining pool is biased.

**Overlap with your work (measuring temporal information flow across CoT for faithfulness):** This is the most directly related paper. David measures how *temporal position within CoT* relates to information about outcome in hidden states. However, the paper is narrowly focused on **correctness prediction** (binary: will this be right or wrong?) rather than faithfulness assessment per se. It does not ask whether the CoT steps are *causally necessary* or *faithful* -- it asks whether the model "already knows" the outcome. The implication for faithfulness is indirect: if correctness is determined at token 4, the subsequent hundreds of tokens may be post-hoc rationalization. Your work could build on this by asking not just "is outcome determined early?" but "does the information flow through CoT steps actually change the model's internal representation, or is it decorative?"

---

## Paper 2: Zhang et al. (2504.05419) -- "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"

**Authors:** Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He (NYU / NYU Shanghai)
**Date:** April 7, 2025

**What they do:** Train probes on hidden states at **intermediate answer positions** within long reasoning traces. They segment CoT into chunks using transition keywords ("wait," "double-check," "alternatively"), extract intermediate answers using Gemini 2.0 Flash, and take the **last-layer hidden state at the last token of each intermediate answer** as the representation. The probe is a two-layer MLP: sigmoid(ReLU(h * W1 + b1) * W2 + b2), though many converge to linear (hidden dim d=0).

**Models:** DeepSeek-R1-Distill series (Llama-8B, Llama-70B, Qwen-1.5B, Qwen-7B, Qwen-32B) and **QwQ-32B**.

**Benchmarks:** GSM8K, MATH, AIME (mathematical), KnowLogic (~5.4k multiple-choice logical reasoning).

**Key results:**
- ROC-AUC exceeds **0.7** in-distribution; R1-Distill-Qwen-32B reaches **>0.9 AUC on AIME**
- Expected Calibration Error below 0.1 (well-calibrated)
- **Early-exit at threshold 0.85:** maintains 88.2% accuracy while reducing tokens by **~24%**
- At threshold 0.9: identical accuracy with 19% token reduction
- Up to 5% accuracy improvement over static baselines at equivalent token budgets

**Key contribution:** (1) Models' hidden states encode correctness of *future* answers before they are generated. (2) A practical early-exit mechanism: when probe confidence exceeds a threshold at an intermediate answer, reasoning terminates. (3) The gap between what models "know internally" and what they "exploit" -- they encode correctness but fail to use it.

**Overlap with your work:** Zhang et al. probe at **discrete intermediate answer positions** (chunk boundaries), whereas temporal information flow analysis would track continuous evolution across all CoT positions. Their probe answers "is this intermediate answer correct?" while your work would ask "is the reasoning step faithfully contributing to the conclusion?" They focus on **efficiency** (early exit) rather than **faithfulness**. The probe architecture (last-layer, last-token of answer chunks) is a specific choice that misses how information accumulates *between* answer positions. Your work could argue that tracking information flow *continuously* across CoT positions reveals whether the model is genuinely reasoning vs. just arriving at answers it already "knows" (connecting to David's finding).

---

## Paper 3: Lewis-Lim et al. (2508.19827) -- "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?"

**Authors:** Samuel Lewis-Lim, Xingwei Tan, Zhixue Zhao, Nikolaos Aletras (University of Sheffield)
**Date:** August 27, 2025
**Venue:** Accepted at **EMNLP 2025 Main Conference**

**What they do:** Track **answer confidence trajectories** across CoT step positions. Formally, they compute c_i = P(final_answer | prompt, reasoning_steps_1_to_i) at each step i -- the softmax probability of the final chosen answer given the CoT generated so far. For reasoning models they use content between `&lt;think>` tags; for others they segment by double line breaks. They also inject **misleading cues** (a "Stanford Professor" endorsement or XML metadata hints) and measure whether CoT acknowledges these cues (faithfulness) vs. whether answers actually change (influence).

**Models:** Three categories:
- Instruction-tuned: Qwen2.5-7B/32B-Instruct, Llama-8B-Instruct
- Reasoning: Qwen3-32B, QwQ-32B
- Distilled-reasoning: DeepSeek-R1-Distill variants (7B, 32B)

**Benchmarks:** Five **soft-reasoning** tasks: CSQA, StrategyQA, MUSR, LSAT, GPQA (5,518 examples total, all multiple-choice).

**Key results:**
- Instruction-tuned models: **flat trajectories** (minimal confidence change across CoT steps) -- suggests post-hoc rationalization
- Distilled models: **increasing confidence** with sharp rises near conclusion; change initial answer **~65%** of the time
- Reasoning models: **mostly flat** but more dynamic on hard tasks; change answers ~24% of the time
- Critical finding: **CoT influence and faithfulness are not aligned** -- unfaithful CoTs can still guide model confidence, and faithful acknowledgments of cues sometimes don't affect the final answer

**Key contribution:** The first paper to systematically track how answer probability *evolves* across CoT positions and cross-reference this with faithfulness, across three model families. Reveals that trajectory shape is a diagnostic of whether CoT is genuine reasoning or rationalization.

**Overlap with your work:** This is the paper most directly about "temporal information flow across CoT for faithfulness assessment." However, Lewis-Lim et al. work entirely in **output space** (softmax probabilities of answer tokens) rather than hidden state representations. They cannot see what the model "internally knows" vs. what it "outputs" -- they only observe the output distribution at each step. Your work, if it probes hidden states across CoT positions, would provide a complementary and arguably deeper view: you could detect cases where the hidden state has already committed to an answer but the output probability trajectory still appears to be "reasoning." Lewis-Lim et al. also focus on **soft-reasoning** tasks specifically (commonsense, analytical), not math/logic, and use cue injection as their faithfulness test rather than step ablation.

---

## Paper 4: Basu & Chakraborty (2603.22816) -- "The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models"

**Authors:** Abhinaba Basu, Pavan Chakraborty
**Date:** March 24, 2026 (revised April 13, 2026, v3)

**What they do:** Introduce the **Step-Level Reasoning Capacity (SLRC)** metric with formal guarantees (Theorem 1). For each reasoning step, they perform:
- **Necessity test:** Remove step i, present remaining steps, check if answer changes
- **Sufficiency test:** Present step i alone, check if answer recovers
- **SLRC = Necessity x (1 - Sufficiency)**, ranging from 0 (decorative) to 1 (genuinely sequential)

This requires only API access (~$1-2 per model per task), no weight access. They also propose **LC-CoSR** (Lyapunov-Constrained Contrastive Step Reinforcement) training to reduce reasoning rigidity, and a **Reasoning Integrity Score (RIS) = SLRC x (1 - Sycophancy Rate)**.

**Models:** 16 frontier models including GPT-5.4, o4-mini, Claude Opus 4.6-R, DeepSeek V3.2/R1-32B/R1-70B, Grok-4, Gemini 2.5 Pro, Kimi-K2.5, MiniMax-M2.5, Qwen variants, GLM-5, Nemotron-Ultra, GPT-OSS-120B, plus 6 smaller open-weight models.

**Benchmarks:** Six domains: SST-2 (sentiment), GSM8K (math), AG News (topic), MedQA (medical), CommonsenseQA, ARC-Challenge (science).

**Key results:**
- o4-mini: **74-88% step necessity** on 5/6 tasks (SLRC = 0.87 on sentiment)
- DeepSeek-R1: **91-93% necessity** on math (SLRC = 0.86)
- GPT-5.4: **0.1% necessity** on sentiment (SLRC = 0.00)
- Claude Opus: **<=15% necessity** across all tasks
- Grok-4 reasoning mode: only **1.4% necessity** despite producing thinking tokens (lower than its non-reasoning mode at 7.2%)
- **Faithfulness paradox:** high-SLRC models are *more* susceptible to sycophancy (rho = 0.53)
- RIS predicts error detection ability (rho = 0.66, p = 0.026)

**Three-mode taxonomy:**
1. **Genuine reasoning:** Steps causally matter, removal changes answers, CoT improves accuracy (e.g., o4-mini, R1 on math)
2. **Scaffolding:** CoT structure helps accuracy but individual steps are interchangeable (e.g., Kimi-K2.5: +94pp from CoT yet 1% necessity)
3. **Decoration:** CoT adds nothing; steps are ornamental (e.g., DeepSeek-V3.2 on sentiment: 11% necessity, -1pp from CoT)

**Key contribution:** RL-based reasoning training (not scale, architecture, or thinking tokens) is what determines faithfulness. The three-mode taxonomy replaces the binary faithful/unfaithful framing. The faithfulness paradox (faithful models are more sycophantic) motivates the combined RIS metric.

**Overlap with your work:** Basu & Chakraborty operate entirely at the **behavioral/output level** (remove a step, check if answer changes via API). They cannot observe hidden states or internal information flow. Their step-level ablation approach is complementary to probing-based temporal analysis: they measure *causal necessity* of steps, while probing hidden states would measure *what information is encoded and when*. A step might be behaviorally necessary (removing it changes the answer) but the hidden state might have encoded the answer before that step -- revealing a gap between causal necessity at the output level and genuine internal reasoning. Your work could use hidden-state probing to distinguish between cases where a step is necessary because it genuinely contributes information vs. where it is necessary only because the model's output format depends on seeing the step (format dependence rather than reasoning dependence). The three-mode taxonomy provides useful categories that hidden-state analysis could further refine with mechanistic evidence.

---

## Summary: Positioning Your Work

The four papers form a clear landscape:

| Paper | Signal source | Temporal granularity | Focus | Probes internal states? |
|-------|--------------|---------------------|-------|------------------------|
| David (2511.14773) | Hidden states | Token-level prefixes (t=4..512) | Correctness prediction | Yes (linear) |
| Zhang et al. (2504.05419) | Hidden states | Chunk-boundary answers | Correctness verification + early exit | Yes (MLP) |
| Lewis-Lim et al. (2508.19827) | Output probabilities | CoT step positions | Faithfulness via confidence trajectories | No (output space only) |
| Basu & Chakraborty (2603.22816) | Behavioral (API) | Step-level ablation | Faithfulness via causal necessity | No (black-box) |

**The gap your work can fill:** None of these papers combine hidden-state probing with faithfulness assessment across the full temporal extent of CoT. David probes hidden states but only asks about correctness. Zhang et al. probe at discrete chunk boundaries for efficiency. Lewis-Lim et al. track temporal dynamics but only in output space. Basu & Chakraborty measure faithfulness but through behavioral ablation with no internal visibility. A paper that tracks how *hidden-state information about the answer evolves continuously across CoT steps* and uses this to assess whether each step genuinely transforms the model's internal representation (faithfulness) would be novel and complementary to all four.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd04412-34a7-4773-bb61-0c16ce5a7225",
  "isSidechain": true,
  "agentId": "adf0ac9b242421c10",
  "requestId": "req_011CbBmgCPM7ZF8DFx6PMCEi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "383955c1-dbfe-41fb-b4fb-a78085bdcb41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "bc8e644e-f848-48d5-b25e-f1b6b09317f6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpHSUEJzo5B5SEL367TWG9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6020,
      "cache_read_input_tokens": 18620,
      "output_tokens": 3591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3591,
          "cache_read_input_tokens": 18620,
          "cache_creation_input_tokens": 6020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6020,
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
