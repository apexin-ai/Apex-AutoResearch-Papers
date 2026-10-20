# Research conversation: You are helping with a literature survey on learned query routing for information retrieval and adaptive retrieval strat

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a17cf06e02d2052fb.jsonl`
- **Structured JSON:** [`c6321600691ffc442345.json`](../../sessions/c6/c6321600691ffc442345.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

78 recorded events

### User

_source line 1 · 2026-05-30T06:13:01.878Z_

You are helping with a literature survey on learned query routing for information retrieval and adaptive retrieval strategies.

Execute these web searches and for each promising paper, fetch its arXiv abstract to verify relevance:

1. Search: "RouterRetriever learned query routing retrieval AAAI 2025"
2. Search: "adaptive query routing sparse dense retrieval 2024 2025 2026"
3. Search: "mixture of experts retrieval routing 2025 2026"
4. Search: "query-dependent retrieval strategy selection 2024 2025"
5. Search: "learned interpolation weight sparse dense retrieval per-query 2025"

For each paper found (2024-2026), use WebFetch on its arXiv page to read the abstract and confirm what the paper actually does.

Return a list of papers with: title, authors, venue, URL, why_important, one_line_summary. Focus on papers about learning to route or adaptively weight different retrieval strategies per query, mixture-of-experts approaches for retrieval, and query-adaptive hybrid retrieval.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "b2af061f-9a74-4609-8a68-1f487be25f8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:13:01.883Z_

```json
{
  "parentUuid": "b2af061f-9a74-4609-8a68-1f487be25f8e",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "c0a9954d-b424-4c05-9522-5318623f6ec6",
  "timestamp": "2026-05-30T06:13:01.883Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:13:01.885Z_

```json
{
  "parentUuid": "c0a9954d-b424-4c05-9522-5318623f6ec6",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0ef16b3c-7b52-4758-96a4-379f8c198c24",
  "timestamp": "2026-05-30T06:13:01.885Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:13:05.475Z_



I'll start by loading the WebSearch and WebFetch tools, then execute the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef16b3c-7b52-4758-96a4-379f8c198c24",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2TZ4L1UZFhtj95NKs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11cc085a-a82b-4289-8d28-cb0fe4fcd99f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NPRqPPS3wLqpC77n9Ft24",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1555,
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

_source line 5 · 2026-05-30T06:13:05.998Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LpYU2rARFVRhWJhxCam5A6`</summary>

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
  "parentUuid": "11cc085a-a82b-4289-8d28-cb0fe4fcd99f",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2TZ4L1UZFhtj95NKs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7112626f-e5a1-43d3-a915-8c723022ac46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NPRqPPS3wLqpC77n9Ft24",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 7413,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1555
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1555,
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

_source line 6 · 2026-05-30T06:13:06.015Z_

<details><summary>↩ Tool result · `toolu_01LpYU2rARFVRhWJhxCam5A6`</summary>

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
  "parentUuid": "7112626f-e5a1-43d3-a915-8c723022ac46",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "c4617c3d-8495-4645-9f8a-a4ba7c8f4c68",
  "sourceToolAssistantUUID": "7112626f-e5a1-43d3-a915-8c723022ac46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:13:08.099Z_



Now let me execute all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4617c3d-8495-4645-9f8a-a4ba7c8f4c68",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "973ab6fe-6db1-4b72-b9b4-c9ac7cc2680c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 8 · 2026-05-30T06:13:09.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3mcegDDgoTkAQALPQEoFz`</summary>

```json
{
  "query": "RouterRetriever learned query routing retrieval AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "973ab6fe-6db1-4b72-b9b4-c9ac7cc2680c",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0b8e8c3-d645-423c-b4e6-60dc86d8575a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 9 · 2026-05-30T06:13:09.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QMo6z77kdD8KTakkKgrj7g`</summary>

```json
{
  "query": "adaptive query routing sparse dense retrieval 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b8e8c3-d645-423c-b4e6-60dc86d8575a",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f093453-9895-43f5-8e7e-7ad51a0bd189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 10 · 2026-05-30T06:13:10.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ZCgztoZgmnaudRTPy9RsH`</summary>

```json
{
  "query": "mixture of experts retrieval routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f093453-9895-43f5-8e7e-7ad51a0bd189",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93dd69dc-0cb3-4c64-8a7d-ee7b02e56646",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 11 · 2026-05-30T06:13:10.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017HiSbPuhgRJLdi87geZNET`</summary>

```json
{
  "query": "query-dependent retrieval strategy selection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93dd69dc-0cb3-4c64-8a7d-ee7b02e56646",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fae3c58-823b-4c98-8b55-0227cc01ccd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
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

_source line 12 · 2026-05-30T06:13:11.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014rmXjYQX9ejRe4vYi5gDD4`</summary>

```json
{
  "query": "learned interpolation weight sparse dense retrieval per-query 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fae3c58-823b-4c98-8b55-0227cc01ccd4",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG2mFfwsvRzr1ZSNpYh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8453ca75-43ed-46b6-a8d5-6f1ca240488b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ew6ZWvfVnqyp5jGDeaGrpt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 8968,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 8968,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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

_source line 13 · 2026-05-30T06:13:15.896Z_

<details><summary>↩ Tool result · `toolu_01M3mcegDDgoTkAQALPQEoFz`</summary>

```text
Web search results for query: "RouterRetriever learned query routing retrieval AAAI 2025"

Links: [{"title":"GitHub - amy-hyunji/RouterRetriever","url":"https://github.com/amy-hyunji/RouterRetriever"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33306"},{"title":"amy-hyunji-lee/RouterRetriever · Hugging Face","url":"https://huggingface.co/amy-hyunji-lee/RouterRetriever"},{"title":"ROUTERRETRIEVER: Routing over a Mixture of Expert Embedding Models Hyunji Lee1*","url":"https://arxiv.org/pdf/2409.02685"},{"title":"[2409.02685] RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/abs/2409.02685"},{"title":"RouterRetriever: Exploring the Benefits of Routing over Multiple Expert Embedding Models","url":"https://arxiv.org/html/2409.02685v1"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/html/2409.02685v2"},{"title":"arXiv:2506.13743v1 [cs.CL] 16 Jun 2025","url":"https://arxiv.org/pdf/2506.13743"},{"title":"LTRR: Learning To Rank Retrievers for LLMs","url":"https://arxiv.org/html/2506.13743v1"},{"title":"Unsupervised Query Routing for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2501.07793"}]

Based on the search results, I found information about RouterRetriever:

## RouterRetriever: AAAI 2025

RouterRetriever is a retrieval model that leverages a mixture of domain-specific experts by using a routing mechanism to select the most appropriate expert for each query. This is an official paper accepted at AAAI 2025.

### Key Features

RouterRetriever is lightweight and allows easy addition or removal of experts without additional training. For each domain, the model trains gates (experts), and during inference, it determines the most relevant expert by computing the average similarity between the query and a set of pilot embeddings representing each expert, selecting the expert with the highest similarity score.

### Performance

Evaluation on the BEIR benchmark demonstrates that RouterRetriever outperforms both models trained on MSMARCO (+2.1 absolute nDCG@10) and multi-task models (+3.2). Additionally, the routing mechanism surpasses other routing techniques (+1.8 on average) commonly used in language modeling.

### Authors

The paper is authored by Hyunji Lee, Luca Soldaini, Arman Cohan, Minjoon Seo, and Kyle Lo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0b8e8c3-d645-423c-b4e6-60dc86d8575a",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "06ba886f-ea11-4641-8566-52183374fa74",
  "sourceToolAssistantUUID": "f0b8e8c3-d645-423c-b4e6-60dc86d8575a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-30T06:13:17.591Z_

<details><summary>↩ Tool result · `toolu_016ZCgztoZgmnaudRTPy9RsH`</summary>

```text
Web search results for query: "mixture of experts retrieval routing 2025 2026"

Links: [{"title":"[2505.22095] Mixture-of-Retrieval Experts for Reasoning-Guided Multimodal Knowledge Exploitation","url":"https://arxiv.org/abs/2505.22095"},{"title":"Mixture-of-Experts for Knowledge Graph Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=1KkIChhCv7"},{"title":"MixRAG : Mixture-of-Experts Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2509.21391"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/pdf/2409.02685"},{"title":"Union-of-Experts: Experts in Mixture-of-Experts are Secretly Routers | OpenReview","url":"https://openreview.net/forum?id=Ksgiup7ZNZ"},{"title":"Mixture of Experts in Large Language Models †: Corresponding author: Junhao Song (junhao.song23@imperial.ac.uk)","url":"https://arxiv.org/html/2507.11181v2"},{"title":"MoE-Inference-Bench: Performance Evaluation of Mixture of Expert Large Language and Vision Models | Proceedings of the SC '25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3731599.3767706"},{"title":"[2509.21391] MIXRAG : Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering","url":"https://arxiv.org/abs/2509.21391"},{"title":"Mixture-of-experts with expert choice routing | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3600270.3600785"}]

Based on the search results, here are some recent developments in mixture of experts retrieval routing for 2025-2026:

## Key Research Directions

**Multimodal Retrieval-Augmented Generation:**
A recent approach proposes Mixture-of-Retrieval Experts (MoRE) with Stepwise Group Relative Policy Optimization to coordinate multiple retrieval experts, achieving performance gains of over 7% compared to competitive baselines.

**Knowledge Graph Integration:**
Mixture-of-Experts approaches are being applied to Knowledge Graph Retrieval-Augmented Generation (KG-RAG) to help LLMs with factual accuracy and multi-hop reasoning. These systems achieve superior performance across multiple KG-based Question Answering benchmarks.

**Dynamic Routing with Specialized Experts:**
MIXRAG is a Mixture-of-Experts Graph-RAG framework that introduces multiple specialized graph retrievers and a dynamic routing controller, where each retriever is trained to focus on specific aspects of graph semantics, with adaptive selection based on input queries.

**Expert Selection and Routing:**
RouterRetriever is a retrieval model that leverages multiple domain-specific experts with a routing mechanism that selects the most suitable expert by computing similarity between queries and pilot embeddings.

**Broader MoE Trends:**
Expert routing is increasingly integrated with retrieval, instruction tuning, and agent-based control paradigms. From mid-2025 onward, the main technical focus has shifted to making routing reliable under long training runs and deployment constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93dd69dc-0cb3-4c64-8a7d-ee7b02e56646",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "4b59c20b-45cc-4be6-8ae9-1ef98ccbc7cc",
  "sourceToolAssistantUUID": "93dd69dc-0cb3-4c64-8a7d-ee7b02e56646",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-30T06:13:18.146Z_

<details><summary>↩ Tool result · `toolu_01QMo6z77kdD8KTakkKgrj7g`</summary>

```text
Web search results for query: "adaptive query routing sparse dense retrieval 2024 2025 2026"

Links: [{"title":"Adaptive Query Routing: A Tier-Based Framework for","url":"https://arxiv.org/pdf/2604.14222"},{"title":"Dense–Sparse Hybrid Retrieval","url":"https://www.emergentmind.com/topics/dense-sparse-hybrid-retrieval"},{"title":"Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents","url":"https://arxiv.org/html/2604.14222v1"},{"title":"Hybrid Retrieval: Combining Sparse and Dense Methods for Effective Information Retrieval - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/hybrid-retrieval-combining-sparse-dense-methods-effective-information-retrieval"},{"title":"Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench","url":"https://arxiv.org/html/2604.03455v1"},{"title":"Domain-Adaptive and Scalable Dense Retrieval for Content-Based Recommendation","url":"https://arxiv.org/pdf/2602.00899"},{"title":"When should I search more: Adaptive Complex Query Optimization with Reinforcement Learning","url":"https://arxiv.org/html/2601.21208"}]

Based on the web search results, here's what I found on adaptive query routing with sparse and dense retrieval from 2024-2026:

## Key Approaches and Recent Developments

**Adaptive Fusion Strategies:**
Adaptive weighting approaches set fusion parameters per-query, resulting in +2–7.5 pp gains in Precision@1 and MRR@20 across "hybrid-sensitive" queries compared to static hybrids, as noted in research from March 2025.

Dynamic Weighted Reciprocal Rank Fusion uses query specificity (average tf·idf) to inform per-query weighting between BM25 and semantic retrieval, fused via RRF; this approach dramatically reduces hallucination rates and increases relevance in RAG pipelines.

**Per-Query Strategy Selection:**
BERT-based cross-encoders can be trained to select between sparse-only, dense-only, or hybrid per query, enabling resource/budget-aware retrieval.

**Query Routing in RAG Systems:**
Adaptive-RAG trains a T5-Large classifier on automatically derived complexity labels to route among three retrieval strategies, demonstrating that a three-class query-complexity router can match always-expensive baselines with substantially lower cost.

Recent research shows that no single paradigm universally dominates: optimal paradigm selection is driven by query-corpus interactions, with both query type and structural or semantic corpus properties shaping which paradigm performs best (Wang et al., 2026).

**Hybrid System Development:**
The emergence of hybrid retrieval systems in 2024 represented a pivotal convergence in information retrieval, as researchers and practitioners recognized that neither sparse nor dense retrieval methods alone could adequately address the diverse requirements of modern search applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f093453-9895-43f5-8e7e-7ad51a0bd189",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "4a32d181-6c04-48ea-8370-72733df05be7",
  "sourceToolAssistantUUID": "3f093453-9895-43f5-8e7e-7ad51a0bd189",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:13:18.607Z_

<details><summary>↩ Tool result · `toolu_014rmXjYQX9ejRe4vYi5gDD4`</summary>

```text
Web search results for query: "learned interpolation weight sparse dense retrieval per-query 2025"

Links: [{"title":"LSTM-based Selective Dense Text Retrieval Guided by Sparse Lexical Retrieval","url":"https://arxiv.org/pdf/2502.10639"},{"title":"Dense–Sparse Hybrid Retrieval","url":"https://www.emergentmind.com/topics/dense-sparse-hybrid-retrieval"},{"title":"Article Not peer-reviewed version Learning to Retrieve, Generate, and","url":"https://www.preprints.org/manuscript/202508.1211/v1/download"},{"title":"Relevance & Pseudo-Relevance Feedback","url":"https://www.emergentmind.com/topics/relevance-feedback-and-pseudo-relevance-feedback"},{"title":"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval","url":"https://arxiv.org/html/2508.16707v1"},{"title":"Sparse-to-Dense Embedding Pipeline","url":"https://www.emergentmind.com/topics/sparse-to-dense-embedding-pipeline"},{"title":"Augmenting Document Representations for Dense Retrieval with   Interpolation and Perturbation","url":"https://arxiv.org/pdf/2203.07735"}]

Based on the search results, here's what I found regarding learned interpolation weights for sparse-dense retrieval with per-query adaptation in 2025:

## Key Findings

**Per-Query Learned Weighting:** Dynamic, query-aware weighting strategies set interpolation weights per query using external predictors, LLM judges, or query specificity scores, as in DAT (Hsu et al., 29 Mar 2025) and reciprocal rank fusion (Mala et al., 28 Feb 2025). These methods outperform static weights, especially for queries mixing factoid and semantic content.

**Hybrid Retrieval Framework:** Hybrid retrievers combine sparse and dense signals using the formula: score(q, d) = λ · BM25(q, d) + (1 −λ) · sim(q, d), where λ ∈[0, 1] is a tunable interpolation weight.

**Practical Implementation:** Production systems combine sparse, dense, and contextual representations using hybrid retrieval and reranking schemes with hand-tuned or learned weights to maximize both recall and CTR in large-scale systems.

**Performance Improvements:** Hybrid methods outperform individual components in retrieval accuracy and robustness, especially in open-domain QA and multi-hop reasoning tasks.

The 2025 research shows a clear shift toward making interpolation weights adaptive and query-dependent rather than using fixed static weights across all queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8453ca75-43ed-46b6-a8d5-6f1ca240488b",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "276bf1e2-b9e3-4445-8ca1-54d684664061",
  "sourceToolAssistantUUID": "8453ca75-43ed-46b6-a8d5-6f1ca240488b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:13:21.218Z_

<details><summary>↩ Tool result · `toolu_017HiSbPuhgRJLdi87geZNET`</summary>

```text
Web search results for query: "query-dependent retrieval strategy selection 2024 2025"

Links: [{"title":"heiDS at ArchEHR-QA 2025: From Fixed-k to Query- ...","url":"https://arxiv.org/pdf/2506.19512"},{"title":"Query-Aware Token Selection","url":"https://www.emergentmind.com/topics/query-aware-token-selection"},{"title":"CFDA & CLIP at TREC iKAT 2025: Enhancing Personalized Conversational Search via Query Reformulation and Rank Fusion","url":"https://arxiv.org/pdf/2509.15588"},{"title":"Retrieval strategies: Finding the right information | Anyscale Docs","url":"https://docs.anyscale.com/rag/quality-improvement/retrieval-strategies"},{"title":"I.J. Information Technology and Computer Science, 2025, 2, 73-81","url":"https://www.mecs-press.org/ijitcs/ijitcs-v17-n2/IJITCS-V17-N2-7.pdf"},{"title":"(PDF) Information retrieval with query expansion and re-ranking: a survey","url":"https://www.researchgate.net/publication/389704150_Information_retrieval_with_query_expansion_and_re-ranking_a_survey"},{"title":"[2407.01219] Searching for Best Practices in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2407.01219"}]

Based on the search results, here's what I found regarding query-dependent retrieval strategy selection in 2024-2025:

## Key Recent Approaches

**Ranked List Truncation (RLT) Method**: A query-dependent-k selection strategy based on the Ranked List Truncation method determines the number of sentences to consider by adjusting retrieval scores using generalized Pareto distributions from extreme value theory, and truncates a ranked list using a score threshold to allow for a variable number of relevant sentences to be selected per query.

**Query-Aware Token Selection**: Query-aware token selection yields substantial improvements in both efficiency (latency, memory, and FLOP reduction) and in retrieval/QA accuracy—often outperforming naive or heuristic selection. This is widely applied in long-context LLMs and video/multimodal systems where it dynamically allocates tokens based on query relevance.

**Retrieval Fusion Strategies**: For conversational search, best-of-N selection and Reciprocal Rank Fusion (RRF) strategies are used to handle different tasks, with reranking and fusion improving robustness while revealing trade-offs between effectiveness and efficiency.

**Hybrid Retrieval Approaches**: Combining vector search with traditional keyword or BM25 search, then merging results using techniques such as Reciprocal Rank Fusion (RRF), represents a common hybrid strategy.

These approaches demonstrate a shift toward more adaptive, query-dependent methods that balance performance and efficiency in retrieval-augmented systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fae3c58-823b-4c98-8b55-0227cc01ccd4",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "d93ec0cd-ff1e-47ed-b05b-71da0f0a932c",
  "sourceToolAssistantUUID": "5fae3c58-823b-4c98-8b55-0227cc01ccd4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-30T06:13:23.728Z_

Good, I have strong leads. Now let me fetch the arXiv abstracts for the most promising papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d93ec0cd-ff1e-47ed-b05b-71da0f0a932c",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17eb4d0a-19f5-477f-a70d-fede92ea4015",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 19 · 2026-05-30T06:13:24.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016LMZLHKc5AkQb4zhQFYf3j`</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.02685",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17eb4d0a-19f5-477f-a70d-fede92ea4015",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8fbe009-ded9-4458-a6e0-0792cfa6840c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 20 · 2026-05-30T06:13:25.132Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MHDDmbLNFcv461VciJPq2B`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.22095",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8fbe009-ded9-4458-a6e0-0792cfa6840c",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "292a67b6-323c-4a7d-9108-db625eb1ddd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 21 · 2026-05-30T06:13:26.088Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H4cKJvv7DCtpKGrRpNbgff`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14222",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "292a67b6-323c-4a7d-9108-db625eb1ddd1",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41e92546-9f71-49d5-be7d-d6ed9754d561",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 22 · 2026-05-30T06:13:26.550Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014rH4VaUsPPmotN6J56Z6MY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03455",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e92546-9f71-49d5-be7d-d6ed9754d561",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c02dc80-da34-4481-84b4-27d8ec5375f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 23 · 2026-05-30T06:13:27.488Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XA5o9BQKkz33pZnBagjwh1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.13743",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c02dc80-da34-4481-84b4-27d8ec5375f9",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ca0ab9-6817-46ed-97ce-e1d4e3d4afd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 24 · 2026-05-30T06:13:27.963Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W5tLKvaC8Wmcb9scuTapXR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21391",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ca0ab9-6817-46ed-97ce-e1d4e3d4afd3",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc92f763-829d-45e1-bbfd-7408b084e939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 25 · 2026-05-30T06:13:28.883Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KzsBvPShcrKaSibJnNkR2d`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.10639",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc92f763-829d-45e1-bbfd-7408b084e939",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab1beb16-f162-4aff-ba11-c08d5ca94ba0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 26 · 2026-05-30T06:13:29.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SUEaPbFqe5GeEzcqYvXJYq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.07793",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab1beb16-f162-4aff-ba11-c08d5ca94ba0",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adbe0966-4f10-4fec-bba2-7758087150dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3501,
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

_source line 27 · 2026-05-30T06:13:29.956Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NMDdGhbma1GWWZz71oxDAW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.01219",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adbe0966-4f10-4fec-bba2-7758087150dd",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG3sx2hkUHSQPXiXvMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "633be18d-85c0-49c1-a1f2-bc51937e20b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDxxLT4vVhJXqFjirATDrR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 3501,
      "cache_read_input_tokens": 10090,
      "output_tokens": 763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3501
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 703,
          "output_tokens": 763,
          "cache_read_input_tokens": 10090,
          "cache_creation_input_tokens": 3501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3501,
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

_source line 28 · 2026-05-30T06:13:31.375Z_

<details><summary>↩ Tool result · `toolu_01XA5o9BQKkz33pZnBagjwh1`</summary>

```text
# Paper Summary

**Full Title:**
"LTRR: Learning To Rank Retrievers for LLMs"

**Authors:**
- To Eun Kim
- Fernando Diaz

**Complete Abstract:**
The paper addresses the limitation that Retrieval-Augmented Generation (RAG) systems typically depend on a single fixed retriever. The researchers propose a query routing method that dynamically chooses from multiple retrievers based on the query characteristics, using both heuristic and learned approaches. They frame this as a learning-to-rank problem called LTRR, which "Learns To Rank Retrievers according to their expected contribution to downstream RAG performance." Their experiments on question-answering benchmarks show that routing-based systems outperform single-retriever baselines, with particularly strong results using the Answer Correctness objective and pairwise ranking methods like XGBoost. The approach also generalizes better to out-of-distribution queries, highlighting the importance of training strategy and optimization metrics in effective query routing for RAG systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ca0ab9-6817-46ed-97ce-e1d4e3d4afd3",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "e753c4b6-aab9-4ae8-9608-6612fb10557d",
  "sourceToolAssistantUUID": "31ca0ab9-6817-46ed-97ce-e1d4e3d4afd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T06:13:31.670Z_

<details><summary>↩ Tool result · `toolu_01H4cKJvv7DCtpKGrRpNbgff`</summary>

```text
# Paper Summary

**Full Title:** "Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents"

**Author:** Afshan Hashmi

**Complete Abstract:**

The research addresses how language models can better leverage external documents for accurate responses. The study evaluates three retrieval methods—Vector RAG, Tree Reasoning, and a newly proposed Adaptive Hybrid Retrieval system—across financial, legal, and medical domains using a four-tier complexity benchmark. 

Results indicate that tree-based approaches excel overall (0.900 score), though no single method dominates universally. Vector systems performed best on multi-document synthesis tasks (0.900), while hybrid methods achieved superior results on cross-reference queries (0.850) and multi-section searches (0.929). Notably, tree and hybrid approaches reached 100% recall on cross-references versus 91.7% for vector search. 

Testing on real SEC filings confirmed these patterns, with tree reasoning scoring 0.938, hybrid approaches at 0.901, and vector methods at 0.821. The authors conclude that adaptive systems selecting strategies based on query characteristics represent the most promising path forward. Research materials are publicly accessible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e92546-9f71-49d5-be7d-d6ed9754d561",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "87e702ef-613d-46a4-b3a6-87421565eb1c",
  "sourceToolAssistantUUID": "41e92546-9f71-49d5-be7d-d6ed9754d561",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T06:13:31.713Z_

<details><summary>↩ Tool result · `toolu_014rH4VaUsPPmotN6J56Z6MY`</summary>

```text
# Paper Details

**Full Title:** "Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench"

**Authors:** Prakhar Bansal, Shivangi Agarwal

**Complete Abstract:**

The authors investigate how to efficiently select retrieval strategies for RAG pipelines by evaluating classifier-based routing on RAGRouter-Bench, a benchmark containing 7,727 queries across four domains. Each query is categorized as factual, reasoning, or summarization type.

They test five classical classifiers across three feature approaches: TF-IDF, MiniLM sentence embeddings, and structural features—totaling 15 configurations. Their strongest model combines TF-IDF with SVM, achieving "macro-averaged F1 of 0.928 and accuracy of 93.2%" while generating "28.1% token savings." 

Key finding: "Lexical TF-IDF features outperform semantic sentence embeddings by 3.1 macro-F1 points," indicating surface-level keyword patterns effectively predict query complexity. Domain analysis shows medical queries present routing challenges while legal queries are easier to classify. The results establish a baseline for query-focused routing while revealing gaps that corpus-aware methods must address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c02dc80-da34-4481-84b4-27d8ec5375f9",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "164dc418-700a-434b-96a3-80bb9b4b58ff",
  "sourceToolAssistantUUID": "6c02dc80-da34-4481-84b4-27d8ec5375f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T06:13:32.138Z_

<details><summary>↩ Tool result · `toolu_01MHDDmbLNFcv461VciJPq2B`</summary>

```text
# Paper Information

**Full Title:** "Mixture-of-Retrieval Experts for Reasoning-Guided Multimodal Knowledge Exploitation"

**Authors:** Chunyi Peng, Zhipeng Xu, Zhenghao Liu, Yishan Li, Yukun Yan, Shuo Wang, Yu Gu, Minghe Yu, Ge Yu, and Maosong Sun

**Abstract:** 

The researchers introduce a framework addressing hallucinations in multimodal language models. Rather than following fixed retrieval patterns, their approach "enables MLLMs to collaboratively interact with diverse retrieval experts for more effective knowledge exploitation." The system learns to dynamically select which expert to engage based on evolving reasoning states.

They propose a training method called Stepwise Group Relative Policy Optimization that "goes beyond sparse outcome-based supervision" by encouraging interaction with multiple experts and synthesizing detailed rewards. Experiments across question-answering benchmarks show performance improvements exceeding 7% compared to competing methods. The framework demonstrates strong adaptability through "dynamically coordinating heterogeneous experts to precisely locate relevant information," validating its capacity for "robust, reasoning-driven expert collaboration."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "292a67b6-323c-4a7d-9108-db625eb1ddd1",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "27c5400e-6881-4de9-8f6c-4c3e6ee39dbd",
  "sourceToolAssistantUUID": "292a67b6-323c-4a7d-9108-db625eb1ddd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T06:13:32.660Z_

<details><summary>↩ Tool result · `toolu_01W5tLKvaC8Wmcb9scuTapXR`</summary>

```text
# MIXRAG Paper Details

**Full Title:** "MIXRAG : Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering"

**Authors:**
- Lihui Liu
- Jiayuan Ding
- Subhabrata Mukherjee
- Carl J. Yang

**Complete Abstract:**

Large Language Models have demonstrated strong capabilities across applications but frequently generate inaccurate information in knowledge-intensive scenarios due to dependence on fixed pretraining datasets. Retrieval-Augmented Generation addresses this by integrating external knowledge during inference. Textual graphs offer structured, semantically meaningful data enabling more accurate reasoning. However, existing graph-based RAG systems typically employ a single retriever, limiting their capacity to handle multifaceted queries. Additionally, these approaches struggle to properly assess retrieved content relevance, introducing noise.

The authors propose MIXRAG, employing multiple specialized graph retrievers with dynamic routing. Each retriever targets distinct graph aspects—entities, relations, or topology. A Mixture-of-Experts module intelligently selects and combines relevant retrievers per query. A query-aware GraphEncoder analyzes retrieved subgraph relationships, emphasizing relevant components while suppressing extraneous information. Results indicate state-of-the-art performance across multiple domains and graph-based tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc92f763-829d-45e1-bbfd-7408b084e939",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "7a8f4e87-72f8-45c7-8738-a076844c8003",
  "sourceToolAssistantUUID": "cc92f763-829d-45e1-bbfd-7408b084e939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:13:32.806Z_

<details><summary>↩ Tool result · `toolu_01KzsBvPShcrKaSibJnNkR2d`</summary>

```text
# Paper Information

**Full Title:** "LSTM-based Selective Dense Text Retrieval Guided by Sparse Lexical Retrieval"

**Authors:**
- Yingrui Yang
- Parker Carlson
- Yifan Qiao
- Wentai Xie
- Shanxiu He
- Tao Yang

**Abstract:**

The paper introduces a method that combines dense and sparse retrieval approaches. It proposes "CluSD," which uses clustering and an LSTM model to "quickly identify relevant clusters while incurring limited extra memory space overhead." The approach processes searches in two stages, selectively triggering dense retrieval operations and performing cluster-based disk input/output when necessary. The authors evaluate their method on MS MARCO and BEIR datasets for both in-memory and on-disk scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab1beb16-f162-4aff-ba11-c08d5ca94ba0",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "c86a6bf9-134c-4557-a5d1-6efcbdada533",
  "sourceToolAssistantUUID": "ab1beb16-f162-4aff-ba11-c08d5ca94ba0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:13:32.933Z_

<details><summary>↩ Tool result · `toolu_01SUEaPbFqe5GeEzcqYvXJYq`</summary>

```text
# Paper Information

**Title:** "Unsupervised Query Routing for Retrieval Augmented Generation"

**Authors:** Feiteng Mu, Liwen Zhang, Yong Jiang, Wenjie Li, Zhen Zhang, Pengjun Xie, Fei Huang

**Abstract:** 
The research addresses query routing for retrieval-augmented generation by proposing an unsupervised approach that avoids the need for extensive manual annotation. Rather than relying on labeled datasets, the method constructs an "upper-bound" response to assess retrieval quality and determine the most suitable search engine for each query. This technique enables automatic processing of large-scale real user queries to generate training data. The authors demonstrate across five datasets that their approach "significantly enhances scalability and generalization capabilities" in out-of-distribution scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adbe0966-4f10-4fec-bba2-7758087150dd",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "6add04ee-c476-4e86-85f1-abeb0c92b38e",
  "sourceToolAssistantUUID": "adbe0966-4f10-4fec-bba2-7758087150dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-30T06:13:33.463Z_

<details><summary>↩ Tool result · `toolu_016LMZLHKc5AkQb4zhQFYf3j`</summary>

```text
# RouterRetriever Paper Details

**Full Title:**
"RouterRetriever: Routing over a Mixture of Expert Embedding Models"

**Authors:**
- Hyunji Lee
- Luca Soldaini
- Arman Cohan
- Minjoon Seo
- Kyle Lo

**Abstract:**
The researchers present a retrieval system that "leverages a mixture of domain-specific experts by using a routing mechanism to select the most appropriate expert for each query." Rather than relying on single general-purpose embedding models, this approach maintains specialized retrievers for different domains. The method demonstrates performance gains exceeding both MSMARCO-trained models and multi-task alternatives on the BEIR benchmark. Notably, the routing strategy "surpasses other routing techniques commonly used in language modeling," and benefits extend to datasets without dedicated experts, representing the first successful application of this mixture-of-experts concept to specialized embedding models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8fbe009-ded9-4458-a6e0-0792cfa6840c",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "0e204a78-9025-46ae-88f9-d105349ef2a9",
  "sourceToolAssistantUUID": "a8fbe009-ded9-4458-a6e0-0792cfa6840c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:13:35.035Z_

<details><summary>↩ Tool result · `toolu_01NMDdGhbma1GWWZz71oxDAW`</summary>

```text
# Paper Details

**Title:** "Searching for Best Practices in Retrieval-Augmented Generation"

**Authors:** Xiaohua Wang, Zhenghua Wang, Xuan Gao, Feiran Zhang, Yixin Wu, Zhibo Xu, Tianyuan Shi, Zhengyuan Wang, Shizheng Li, Qi Qian, Ruicheng Yin, Changze Lv, Xiaoqing Zheng, and Xuanjing Huang

**Abstract:** 

The researchers investigate RAG methodologies and their combinations to discover optimal deployment practices. They note that "RAG techniques have proven to be effective in integrating up-to-date information, mitigating hallucinations, and enhancing response quality," particularly in specialized fields. Their extensive experiments reveal strategies balancing performance with efficiency. The work also demonstrates that multimodal retrieval methods substantially improve question-answering on visual content and accelerate multimodal generation through a retrieval-based approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "633be18d-85c0-49c1-a1f2-bc51937e20b7",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "44bed0b6-a71c-4ac6-8d2c-ce13b55e2bbe",
  "sourceToolAssistantUUID": "633be18d-85c0-49c1-a1f2-bc51937e20b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-30T06:13:38.395Z_

Good. Now let me search for a few more specific papers that were mentioned in the search results, and run additional targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44bed0b6-a71c-4ac6-8d2c-ce13b55e2bbe",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG4uFCGhs7HKD88jNQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1908c68-2db8-45a5-97b1-ffaa51446e4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi16CVatRoieQWXUMaWEdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3829,
      "cache_read_input_tokens": 13591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3829,
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

_source line 38 · 2026-05-30T06:13:39.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N1hCHNXMKharj2iuW1Bkw4`</summary>

```json
{
  "query": "Adaptive-RAG query complexity routing retrieval augmented generation arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1908c68-2db8-45a5-97b1-ffaa51446e4a",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG4uFCGhs7HKD88jNQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7efa539-b21a-499d-899f-b0cf2227697c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi16CVatRoieQWXUMaWEdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3829,
      "cache_read_input_tokens": 13591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3829,
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

_source line 39 · 2026-05-30T06:13:40.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QLY5MBatEsFr5kBtuX2vgs`</summary>

```json
{
  "query": "\"DAT\" \"dynamic adaptive\" per-query weight sparse dense retrieval 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7efa539-b21a-499d-899f-b0cf2227697c",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG4uFCGhs7HKD88jNQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d6a89e-e3e1-4b9d-a456-fbc0f177b791",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi16CVatRoieQWXUMaWEdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3829,
      "cache_read_input_tokens": 13591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3829,
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

_source line 40 · 2026-05-30T06:13:41.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016W7XP1pkHsCoxGij5dWrXb`</summary>

```json
{
  "query": "query-adaptive hybrid retrieval learned routing SIGIR ECIR 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d6a89e-e3e1-4b9d-a456-fbc0f177b791",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG4uFCGhs7HKD88jNQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b395f668-afe6-45cb-9e05-656b0c7455fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi16CVatRoieQWXUMaWEdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3829,
      "cache_read_input_tokens": 13591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3829,
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

_source line 41 · 2026-05-30T06:13:41.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkLbM9UumYZZXx7bjTJ3Lj`</summary>

```json
{
  "query": "\"learned sparse dense\" \"per-query\" interpolation retrieval arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b395f668-afe6-45cb-9e05-656b0c7455fb",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG4uFCGhs7HKD88jNQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf2e5c5-d423-4ad6-8539-1607bd5f8de7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi16CVatRoieQWXUMaWEdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3829,
      "cache_read_input_tokens": 13591,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 13591,
          "cache_creation_input_tokens": 3829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3829,
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

_source line 42 · 2026-05-30T06:13:46.877Z_

<details><summary>↩ Tool result · `toolu_01QLY5MBatEsFr5kBtuX2vgs`</summary>

```text
Web search results for query: ""DAT" "dynamic adaptive" per-query weight sparse dense retrieval 2025 arXiv"

Links: [{"title":"Entropy-Based Dynamic Hybrid Retrieval for Adaptive Query Weighting in","url":"https://openreview.net/pdf?id=bwGaZOVo0c"},{"title":"DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2503.23013v1"},{"title":"[2503.23013] DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2503.23013"},{"title":"Dense–Sparse Hybrid Retrieval","url":"https://www.emergentmind.com/topics/dense-sparse-hybrid-retrieval"},{"title":"Preprint. Under review. DAT: Dynamic Alpha Tuning for Hybrid Retrieval in","url":"https://arxiv.org/pdf/2503.23013"},{"title":"arXiv:2506.00049v1 [cs.IR] 28 May 2025","url":"https://arxiv.org/pdf/2506.00049"},{"title":"Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval","url":"https://arxiv.org/html/2602.03306v2"}]

I found relevant information about DAT. Here are the search results:

## DAT: Dynamic Alpha Tuning

DAT (Dynamic Alpha Tuning) is a novel hybrid retrieval framework that dynamically balances dense retrieval and BM25 for each query. 

**Key Characteristics:**

- DAT dynamically adjusts the weighting between sparse and dense retrieval for each query by leveraging LLMs to evaluate document effectiveness.

- DAT leverages a large language model (LLM) to evaluate the effectiveness of the top-1 results from both retrieval methods, assigning an effectiveness score to each.

- The method calibrates the optimal weighting factor through effectiveness score normalization, ensuring a more adaptive and query-aware weighting between the two approaches.

**Performance:**

Empirical results show that DAT consistently significantly outperforms fixed-weighting hybrid retrieval methods across various evaluation metrics. Additionally, DAT results in +2–7.5 pp gains in Precision@1 and MRR@20 across "hybrid-sensitive" queries compared to static hybrids.

The paper was published on arXiv in March 2025 (arXiv:2503.23013).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d6a89e-e3e1-4b9d-a456-fbc0f177b791",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "24324698-7ada-43ac-8284-53e6ab5f208f",
  "sourceToolAssistantUUID": "92d6a89e-e3e1-4b9d-a456-fbc0f177b791",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-30T06:13:48.531Z_

<details><summary>↩ Tool result · `toolu_01N1hCHNXMKharj2iuW1Bkw4`</summary>

```text
Web search results for query: "Adaptive-RAG query complexity routing retrieval augmented generation arXiv 2024"

Links: [{"title":"Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench","url":"https://arxiv.org/html/2604.03455v1"},{"title":"FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.22344v1"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v1"},{"title":"Dynamic Query Routing: Adaptive RAG Systems Leveraging Hallucination Risk and Specialization Affordance - Pattern Recognition Lab","url":"https://lme.tf.fau.de/thesis/dynamic-query-routing-adaptive-rag-systems-leveraging-hallucination-risk-and-specialization-affordance/"},{"title":"Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench","url":"https://arxiv.org/pdf/2604.03455"},{"title":"MAO-ARAG: Multi-Agent Orchestration for Adaptive Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2508.01005"},{"title":"RAGRouter-Bench: A Dataset and Benchmark for Adaptive RAG Routing","url":"https://arxiv.org/pdf/2602.00296"},{"title":"HANRAG: Heuristic Accurate Noise-resistant Retrieval-Augmented Generation for Multi-hop Question Answering","url":"https://arxiv.org/html/2509.09713v1"}]

Based on the search results, here's what I found about Adaptive-RAG and query complexity routing in retrieval augmented generation:

## Adaptive-RAG Overview

Adaptive-RAG (Jeong et al., 2024) trains a T5-Large classifier on automatically derived complexity labels to route among three retrieval strategies, and demonstrates that a three-class query-complexity router can match always-expensive baselines with substantially lower cost.

## Key Approach

The system introduces a classifier to pre-assess query complexity and route it to an appropriate strategy: no retrieval for simple questions, single-step retrieval for moderate ones, or a multi-step approach for complex queries.

## Research Context

RAG has become the dominant approach for grounding LLM outputs in external knowledge, but the design space spans multiple retrieval paradigms with very different cost profiles. A simple dense-retrieval step (NaiveRAG) is fast and cheap; an iterative pipeline (IterativeRAG) that alternates retrieval and generation can handle complex queries but costs 3.5× more in tokens. Most deployed systems apply one paradigm uniformly to every query.

## Related Research Infrastructure

Wang et al. (2026) recently released RAGRouter-Bench, the first benchmark designed specifically for RAG routing research, which provides 7,727 queries across four domains, each annotated with one of three canonical query types (factual, reasoning, summarization), alongside evaluations of five RAG paradigms.

The Adaptive-RAG approach is part of a broader trend in the LLM field toward cost-efficient routing systems that match query complexity to appropriate processing strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7efa539-b21a-499d-899f-b0cf2227697c",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "59f40c70-521b-4373-9d1a-076dcfd4dbca",
  "sourceToolAssistantUUID": "a7efa539-b21a-499d-899f-b0cf2227697c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-30T06:13:49.168Z_

<details><summary>↩ Tool result · `toolu_01FkLbM9UumYZZXx7bjTJ3Lj`</summary>

```text
Web search results for query: ""learned sparse dense" "per-query" interpolation retrieval arXiv 2024 2025"

Links: [{"title":"[2205.00235] To Interpolate or not to Interpolate: PRF, Dense and Sparse Retrievers","url":"https://arxiv.org/abs/2205.00235"},{"title":"[2203.07735v2] Augmenting Document Representations for Dense Retrieval with Interpolation and Perturbation","url":"https://arxiv.org/abs/2203.07735v2"},{"title":"[2108.13454] Improving Query Representations for Dense Retrieval with Pseudo Relevance Feedback","url":"https://ar5iv.labs.arxiv.org/html/2108.13454"},{"title":"To Interpolate or not to Interpolate: PRF, Dense and Sparse Retrievers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220500235L/abstract"},{"title":"Effective Inference-Free Retrieval for Learned Sparse Representations","url":"https://arxiv.org/html/2505.01452"},{"title":"Multimodal Learned Sparse Retrieval with Probabilistic Expansion Control","url":"https://arxiv.org/pdf/2402.17535"},{"title":"Augmenting Document Representations for Dense Retrieval with   Interpolation and Perturbation","url":"https://arxiv.org/pdf/2203.07735"},{"title":"A Unified Framework for Learned Sparse Retrieval","url":"https://arxiv.org/pdf/2303.13416"},{"title":"Effective Inference-Free Retrieval for Learned Sparse Representations","url":"https://arxiv.org/pdf/2505.01452"}]

Based on the search results, I found several relevant papers on sparse and dense retrieval with interpolation techniques. Here are the most relevant findings:

## Key Papers on Sparse-Dense Retrieval Interpolation

Previous work has investigated how relevance signals from sparse retrievers could be combined with those from dense retrievers via interpolation. 

A particularly relevant paper is "To Interpolate or not to Interpolate: PRF, Dense and Sparse Retrievers" (arXiv:2205.00235, April 2022), which addresses the specific challenge of combining sparse and dense signals in retrieval. The research evaluates whether to use a zero-shot bag-of-words model (BM25) or a learnt sparse representation, considering an effective neural PRF approach (Vector-PRF), three effective dense retrievers (ANCE, TCTv2, DistillBERT), and one state-of-the-art learnt sparse retriever (uniCOIL).

## Recent Work on Learned Sparse Representations (2024-2025)

Learned sparse representations (LSR) map queries and documents into n-dimensional vectors where dimensions are grounded on the vocabulary of the collection, and when a coordinate is nonzero in a sparse embedding, that indicates that the corresponding term is semantically relevant to the input.

A more recent paper (arXiv:2505.01452, April 2025) titled "Effective Inference-Free Retrieval for Learned Sparse Representations" discusses efficiency challenges in LSR-based retrieval systems.

The search results don't contain papers specifically matching all your exact search terms with "per-query" interpolation weighting learned automatically, but the papers above represent the closest matches to your query in the recent literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf2e5c5-d423-4ad6-8539-1607bd5f8de7",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "b13874db-c5c0-4a60-96b9-a1ff53ed549c",
  "sourceToolAssistantUUID": "ecf2e5c5-d423-4ad6-8539-1607bd5f8de7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-30T06:13:50.618Z_

<details><summary>↩ Tool result · `toolu_016W7XP1pkHsCoxGij5dWrXb`</summary>

```text
Web search results for query: "query-adaptive hybrid retrieval learned routing SIGIR ECIR 2024 2025"

Links: [{"title":"LTRR: Learning To Rank Retrievers for LLMs","url":"https://arxiv.org/pdf/2506.13743"},{"title":"Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents","url":"https://arxiv.org/html/2604.14222v1"},{"title":"Unsupervised Query Routing for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2501.07793"},{"title":"Your Dense Retriever is Secretly an Expeditious Reasoner","url":"https://arxiv.org/pdf/2510.21727"},{"title":"Adaptive Retrieval | Avishek Anand","url":"https://www.avishekanand.com/blog/2025/adaptive-retrieval/"},{"title":"dblp: ECIR 2024 - Part III","url":"https://dblp.org/db/conf/ecir/ecir2024-3.html"},{"title":"RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition","url":"https://arxiv.org/pdf/2602.20735"}]

I found several relevant results related to query-adaptive hybrid retrieval and learned routing in recent research conferences. Here's what the search revealed:

## Query Routing and Adaptive Retrieval Research

LTRR (Learning To Rank Retrievers) was presented at SIGIR 2025 LiveRAG challenge, where it demonstrated the practical viability of query routing approaches in RAG systems. The approach builds on established IR fields including Distributed Search, Federated Search, Selective Search, and Meta Search, employing resource representations and selection strategies to effectively route queries.

Additionally, a paper on Adaptive Hybrid Retrieval (AHR) evaluates three retrieval architectures (Vector RAG, Tree Reasoning, and AHR) across financial, legal, and medical domains with a four-tier query complexity benchmark.

## Adaptive Retrieval at ECIR 2024

Adaptive retrieval research has progressed through multiple papers including QUAM (WSDM), SlideGAR (ECIR), ORE (SIGIR), and SUNAR, each broadening the scope of adaptive retrieval from graph-based reranking to LLM-based re-rankers.

## Recent RAG Systems with Dynamic Routing

Routing-to-RAG (R2RAG) is a RAG architecture that dynamically adapts the retrieval strategy based on inferred query complexity and evidence sufficiency.

The search results show active research in this area at both SIGIR and ECIR conferences in 2024-2025, with multiple approaches to learned routing and query-adaptive hybrid retrieval systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b395f668-afe6-45cb-9e05-656b0c7455fb",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "a9d40ea5-2da7-45cb-bf58-217b904a2e48",
  "sourceToolAssistantUUID": "b395f668-afe6-45cb-9e05-656b0c7455fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-30T06:13:54.389Z_

Let me now fetch the abstracts for the additional papers discovered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9d40ea5-2da7-45cb-bf58-217b904a2e48",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90fe1e4c-7356-4647-a12e-44e9a1bf5d1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 47 · 2026-05-30T06:13:55.771Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PdVTX4MYY1mFfWWCmvNmvM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.23013",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90fe1e4c-7356-4647-a12e-44e9a1bf5d1a",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "678fdf2d-886f-413d-afcd-d02dc0249b8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 48 · 2026-05-30T06:13:56.271Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KCmTg8EEdE3mjcJMjT2PZv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23052",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "678fdf2d-886f-413d-afcd-d02dc0249b8c",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eac63126-1668-4bfd-890e-ee7c28ebf459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 49 · 2026-05-30T06:13:57.189Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NLMDSHANGgDxahwSxeMFML`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.00296",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac63126-1668-4bfd-890e-ee7c28ebf459",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0c3e511-3b20-4f1e-893b-2433dcacdac5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 50 · 2026-05-30T06:13:57.661Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TWgxHwCH7rNHJ4F9ZqHJfS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03306",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper. Also extract submission date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0c3e511-3b20-4f1e-893b-2433dcacdac5",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c16cce5-1300-4908-a2a2-558fb5003e3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 51 · 2026-05-30T06:13:58.707Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NTe4gbhUFVgCe62U7VkZBY`</summary>

```json
{
  "query": "Adaptive-RAG Jeong complexity classifier T5 retrieval routing arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c16cce5-1300-4908-a2a2-558fb5003e3d",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG63r9ZjgfZcu9b5yQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7a2e092-d464-4923-9c47-a9b3d5e0794f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMYQxBr7gzdtezrhr2stu7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17420,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 875,
          "output_tokens": 412,
          "cache_read_input_tokens": 17420,
          "cache_creation_input_tokens": 2485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2485,
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

_source line 52 · 2026-05-30T06:13:59.536Z_

<details><summary>↩ Tool result · `toolu_01PdVTX4MYY1mFfWWCmvNmvM`</summary>

```text
# Paper Details

**Full Title:** "DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation"

**Authors:** Hsin-Ling Hsu and Jengnan Tzeng

**Complete Abstract:**

Hybrid retrieval in RAG systems combines dense and sparse retrieval methods to enhance information retrieval. However, fixed weighting approaches fail to adapt across different queries. The authors propose DAT, which dynamically balances dense retrieval and BM25 for each query. An LLM evaluates the effectiveness of top results from both methods and assigns scores. Through effectiveness score normalization, the framework calibrates optimal weighting factors, enabling query-aware balancing. Empirical findings demonstrate that DAT significantly surpasses fixed-weighting hybrid retrieval methods across multiple evaluation metrics, with strong performance even on smaller models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "678fdf2d-886f-413d-afcd-d02dc0249b8c",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "b3fb2bb8-9ccf-4a05-8f6b-f9bf17424fab",
  "sourceToolAssistantUUID": "678fdf2d-886f-413d-afcd-d02dc0249b8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-30T06:14:00.651Z_

<details><summary>↩ Tool result · `toolu_01KCmTg8EEdE3mjcJMjT2PZv`</summary>

```text
# Paper Summary

**Title:** "RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models"

**Authors:** Jiarui Zhang, Xiangyu Liu, Yong Hu, Chaoyue Niu, Fan Wu, and Guihai Chen

**Abstract:** The paper addresses how to intelligently direct queries to the most suitable model among multiple retrieval-augmented language systems. The authors observe that external documents significantly influence LLM performance, yet existing routing approaches rely on static knowledge rather than dynamic document influence. They introduce RAGRouter, which employs document embeddings and contrastive learning to recognize knowledge shifts. Testing across diverse knowledge-intensive tasks demonstrates this method surpasses individual models and competing routing strategies, while also enabling strong performance-efficiency trade-offs under latency restrictions. The researchers have made their code and data publicly accessible through GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eac63126-1668-4bfd-890e-ee7c28ebf459",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "e7c4ece0-27c2-45c3-92d7-9371d6c5620b",
  "sourceToolAssistantUUID": "eac63126-1668-4bfd-890e-ee7c28ebf459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-30T06:14:01.264Z_

<details><summary>↩ Tool result · `toolu_01NLMDSHANGgDxahwSxeMFML`</summary>

```text
# RAGRouter-Bench Paper Details

**Full Title:**
"RAGRouter-Bench: A Dataset and Benchmark for Adaptive RAG Routing"

**Authors:**
Ziqi Wang, Xi Zhu, Shuhang Lin, Haochen Xue, Minghao Guo, and Yongfeng Zhang

**Complete Abstract:**

The paper introduces a benchmark addressing how different retrieval-augmented generation approaches perform across varying contexts. The authors created a dataset incorporating three query types and corpus characteristics measuring both structural and semantic features. They evaluated multiple RAG systems using different language model backbones, measuring both output quality and resource usage.

Key findings indicate that "no one-size-fits-all paradigm exists across query-corpus pairs," and that adaptive routing strategies outperform fixed approaches in balancing effectiveness with efficiency. The research establishes query-corpus compatibility as a foundational principle for developing smarter RAG systems that can dynamically select appropriate techniques based on specific input characteristics and resource constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0c3e511-3b20-4f1e-893b-2433dcacdac5",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "da9920dd-c820-43a4-989b-1bdcd2a2a766",
  "sourceToolAssistantUUID": "a0c3e511-3b20-4f1e-893b-2433dcacdac5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-30T06:14:01.582Z_

<details><summary>↩ Tool result · `toolu_01TWgxHwCH7rNHJ4F9ZqHJfS`</summary>

```text
# Paper Information

**Full Title:** "Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval"

**Authors:** Zhanyu Wu, Richong Zhang, Zhijie Nie

**Submission Date:** February 3, 2026 (v1); revised February 7, 2026 (v2)

**Abstract Summary:**

The paper addresses redundancy in high-dimensional embeddings used for dense retrieval. The researchers propose that "for a given information need, only a subset of dimensions is consistently helpful for ranking."

Their approach differs from prior methods by learning to predict per-dimension importance directly from query embeddings, rather than relying on pseudo-relevance feedback or global transformations. They construct oracle importance distributions using labeled relevance data, then train a predictor to map query embeddings to these importance scores.

At inference, their selector identifies query-specific dimensions for similarity computation without requiring pseudo-relevance feedback. The method demonstrates improvements across multiple dense retrievers and benchmarks compared to full-dimensional baselines and alternative masking approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c16cce5-1300-4908-a2a2-558fb5003e3d",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "31b566fd-5d6d-40c2-a577-b37b3255444c",
  "sourceToolAssistantUUID": "0c16cce5-1300-4908-a2a2-558fb5003e3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-30T06:14:04.786Z_

<details><summary>↩ Tool result · `toolu_01NTe4gbhUFVgCe62U7VkZBY`</summary>

```text
Web search results for query: "Adaptive-RAG Jeong complexity classifier T5 retrieval routing arXiv 2024"

Links: [{"title":"Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench","url":"https://arxiv.org/html/2604.03455v1"},{"title":"Adaptive Retrieval without Self-Knowledge? Bringing Uncertainty Back Home","url":"https://arxiv.org/html/2501.12835v1"},{"title":"GitHub - starsuzi/Adaptive-RAG · GitHub","url":"https://github.com/starsuzi/Adaptive-RAG"},{"title":"GitHub - AsH1605/Adaptive-RAG: Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity · GitHub","url":"https://github.com/AsH1605/Adaptive-RAG"},{"title":"[2403.14403] Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity","url":"https://arxiv.org/abs/2403.14403"},{"title":"FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.22344v1"},{"title":"[PDF] Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-RAG:-Learning-to-Adapt-Retrieval-Augmented-Jeong-Baek/e5e8c6ac537e0f5b5db14170bc232d6f9e641bbc"},{"title":"Fast or Better? Balancing Accuracy and Cost in Retrieval-Augmented Generation with Flexible User Control","url":"https://arxiv.org/html/2502.12145"},{"title":"Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.389/"},{"title":"Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity","url":"https://arxiv.org/html/2403.14403v1"}]

Based on the search results, here's what I found about Adaptive-RAG:

Adaptive-RAG (Jeong et al., 2024) trains a T5-Large classifier on automatically derived complexity labels to route among three retrieval strategies, and demonstrates that a three-class query-complexity router can match always-expensive baselines with substantially lower cost.

More specifically, the classifier predicts one of three outcomes: whether not to retrieve at all, retrieve once, and retrieve multiple times with IRCoT.

The framework can dynamically select the most suitable strategy for retrieval-augmented LLMs from the simplest to the most sophisticated ones based on the query complexity. The selection process is operationalized with a classifier, which is a smaller LM trained to predict the complexity level of incoming queries with automatically collected labels.

The paper was published at NAACL 2024, with the original arXiv preprint submitted on March 21, 2024. You can find the original paper at arXiv:2403.14403, and the official code repository is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7a2e092-d464-4923-9c47-a9b3d5e0794f",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "dde37c96-7306-417e-80e4-4ee8ecdbe1fc",
  "sourceToolAssistantUUID": "f7a2e092-d464-4923-9c47-a9b3d5e0794f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-30T06:14:07.958Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016dGbdBcWQ8XnbcdcBcipwn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.14403",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde37c96-7306-417e-80e4-4ee8ecdbe1fc",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG76J1dmydvm6j6vk5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c08fab8b-3c02-4f73-95de-0da3243165d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhWDAQTvyFxs9i1mTNkPvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3085,
      "cache_read_input_tokens": 19905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3085,
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

_source line 58 · 2026-05-30T06:14:09.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G3aJwgMzVCTQnBgEM3kUMg`</summary>

```json
{
  "query": "\"retrieval expert selection\" OR \"retrieval routing\" OR \"retrieval strategy selection\" per-query CIKM WSDM EMNLP 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08fab8b-3c02-4f73-95de-0da3243165d1",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG76J1dmydvm6j6vk5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60c88734-28b9-4928-9380-47346603df56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhWDAQTvyFxs9i1mTNkPvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3085,
      "cache_read_input_tokens": 19905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3085,
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

_source line 59 · 2026-05-30T06:14:10.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyyrmT7E5qpC3XhVECtLGu`</summary>

```json
{
  "query": "selective dense retrieval query routing when to use sparse vs dense 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60c88734-28b9-4928-9380-47346603df56",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG76J1dmydvm6j6vk5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6012a1f3-3816-4fb0-986a-cda175ab5954",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhWDAQTvyFxs9i1mTNkPvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3085,
      "cache_read_input_tokens": 19905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3085,
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

_source line 60 · 2026-05-30T06:14:11.661Z_

<details><summary>↩ Tool result · `toolu_016dGbdBcWQ8XnbcdcBcipwn`</summary>

```text
# Paper Information

**Full Title:**
"Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity"

**Authors:**
1. Soyeong Jeong
2. Jinheon Baek
3. Sukmin Cho
4. Sung Ju Hwang
5. Jong C. Park

**Complete Abstract:**

This work addresses limitations in retrieval-augmented LLMs by proposing "a novel adaptive QA framework, that can dynamically select the most suitable strategy" based on query complexity. Rather than applying uniform approaches across all questions, the system uses a smaller language model classifier trained on automatically-generated labels to assess incoming query complexity and choose between simple no-retrieval methods, single-step retrieval approaches, or iterative retrieval strategies. The authors validate their approach on open-domain question-answering datasets and demonstrate improvements in both efficiency and accuracy compared to existing baselines and other adaptive retrieval techniques. Implementation code is made publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c08fab8b-3c02-4f73-95de-0da3243165d1",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "5a9c0de4-1f21-4c30-8772-15ef634c73db",
  "sourceToolAssistantUUID": "c08fab8b-3c02-4f73-95de-0da3243165d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-30T06:14:17.263Z_

<details><summary>↩ Tool result · `toolu_01G3aJwgMzVCTQnBgEM3kUMg`</summary>

```text
Web search results for query: ""retrieval expert selection" OR "retrieval routing" OR "retrieval strategy selection" per-query CIKM WSDM EMNLP 2024 2025"

Links: [{"title":"Expert-Choice Routing","url":"https://www.emergentmind.com/topics/expert-choice-routing"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/pdf/2409.02685"},{"title":"End-to-End Optimization for Multimodal Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.24.pdf"},{"title":"Blog","url":"https://dial.skku.edu/blog"},{"title":"Unsupervised Query Routing for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2501.07793"}]

Here are the search results for your query on retrieval expert selection, routing, and strategy selection from major conferences in 2024-2025:

## Key Findings:

**1. RouterRetriever (CIKM/ArXiv 2024)**
RouterRetriever is a retrieval model that leverages multiple domain-specific experts along with a routing mechanism to select the most appropriate expert for each query. Evaluation on the BEIR benchmark demonstrates that RouterRetriever outperforms both MSMARCO-trained (+2.1 absolute nDCG@10) and multi-task trained (+3.2) models. RouterRetriever is the first work to demonstrate the advantages of using multiple domain-specific expert embedding models with effective routing over a single, general-purpose embedding model in retrieval tasks.

**2. Expert-Choice Routing Advances**
Recent work like MoETuner (Feb 2025) employs integer linear programming to optimize expert-to-GPU assignment, explicitly modeling both load balancing and minimizing inter-GPU communication, achieving up to 17.5% end-to-end speedup in multi-node settings.

**3. Query Routing for RAG (2025)**
Query routing seeks to direct queries to the most suitable search engines to optimize performance and reduce costs.

**4. Multimodal Retrieval (EMNLP 2025)**
MM-RewardRAG includes a query translator to route queries to text, image, and LLM knowledge bases, with adaptive reranking subsequently applied for answer generation.

The search results show active research in this area across CIKM, WSDM, and EMNLP conferences during 2024-2025 on expert selection and routing strategies for retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60c88734-28b9-4928-9380-47346603df56",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "fbf917ff-bcde-41dd-844a-d6d2e6c29971",
  "sourceToolAssistantUUID": "60c88734-28b9-4928-9380-47346603df56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-30T06:14:17.722Z_

<details><summary>↩ Tool result · `toolu_01NyyrmT7E5qpC3XhVECtLGu`</summary>

```text
Web search results for query: "selective dense retrieval query routing when to use sparse vs dense 2024 2025 arXiv"

Links: [{"title":"Towards Dynamic Dense Retrieval with Routing Strategy","url":"https://arxiv.org/html/2602.22547"},{"title":"LSTM-based Selective Dense Text Retrieval Guided by Sparse Lexical Retrieval","url":"https://arxiv.org/pdf/2502.10639"},{"title":"Dense–Sparse Hybrid Retrieval","url":"https://www.emergentmind.com/topics/dense-sparse-hybrid-retrieval"},{"title":"Predicting Efficiency/Effectiveness Trade-offs for Dense vs. ...","url":"https://arxiv.org/pdf/2109.10739"},{"title":"Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval","url":"https://arxiv.org/pdf/2602.03306"},{"title":"Salient Phrase Aware Dense Retrieval: Can a Dense Retriever Imitate a   Sparse One?","url":"https://arxiv.org/pdf/2110.06918"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs","url":"https://arxiv.org/html/2502.15526v1"},{"title":"Your Dense Retriever is Secretly an Expeditious Reasoner","url":"https://arxiv.org/pdf/2510.21727"}]

Based on the search results, here are several relevant recent papers on selective dense retrieval, query routing, and sparse vs. dense retrieval from 2024-2025 on arXiv:

## Key Papers Found:

1. **"Towards Dynamic Dense Retrieval with Routing Strategy"** (February 2026, arXiv:2602.22547)
   - Discusses dynamic dense retrieval with routing mechanisms, including sparse routing strategies that selectively activate modules

2. **"LSTM-based Selective Dense Text Retrieval Guided by Sparse Lexical Retrieval"** (2025, arXiv:2502.10639)
   - Focuses on selective dense retrieval guided by sparse lexical methods

3. **"Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval"** (2026, arXiv:2602.03306)
   - Addresses how high-dimensional dense representations can be redundant at the query level, with only a subset of dimensions contributing meaningfully to relevance, motivating selection of informative dimensions per query

4. **"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs"** (February 2025, arXiv:2502.15526)
   - Demonstrates that sparse retrieval models consistently outperform dense retrieval across both in-domain and out-of-domain benchmarks, with greater robustness to imperfect supervised signals

5. **"Your Dense Retriever is Secretly an Expeditious Reasoner"** (2024, arXiv:2510.21727)
   - Proposes a routing mechanism where a Reasoner Router determines whether queries can be reliably handled by dense reasoning, otherwise resorting to LLM-based approaches

6. **Query-Aware Adaptive Weighting Strategies**
   - Recent work includes dynamic query-aware weighting strategies and BERT-based cross-encoders trained to select between sparse-only, dense-only, or hybrid approaches per query


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6012a1f3-3816-4fb0-986a-cda175ab5954",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "afe3db0a-1687-4acb-982d-4902c8aa0dfb",
  "sourceToolAssistantUUID": "6012a1f3-3816-4fb0-986a-cda175ab5954",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-30T06:14:22.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BJtYMvakp2dLEVdREQhGb6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.22547",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe3db0a-1687-4acb-982d-4902c8aa0dfb",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG83vQw9XD5d9P6C92Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f592b8c-c221-4806-86c5-2c4789023457",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7Pyddq4wbRNPHzQEmtMYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 22990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 64 · 2026-05-30T06:14:23.615Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015szBpkcuJhZAFqtzCR2v77`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23052",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f592b8c-c221-4806-86c5-2c4789023457",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG83vQw9XD5d9P6C92Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8069542-c54b-4ca9-9680-e25ecf364d88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7Pyddq4wbRNPHzQEmtMYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 22990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 65 · 2026-05-30T06:14:24.897Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QQZo3Wpu7rR3WnGAr3aXiH`</summary>

```json
{
  "url": "https://openreview.net/forum?id=1KkIChhCv7",
  "prompt": "Extract the paper title, all authors, venue, and the abstract. What conference or workshop was this submitted to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8069542-c54b-4ca9-9680-e25ecf364d88",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG83vQw9XD5d9P6C92Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed4eb3f0-48c4-43f7-9799-fc5a530c1ad7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7Pyddq4wbRNPHzQEmtMYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 22990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 66 · 2026-05-30T06:14:27.077Z_

<details><summary>↩ Tool result · `toolu_01BJtYMvakp2dLEVdREQhGb6`</summary>

```text
# Paper Details

**Full Title:** "Towards Dynamic Dense Retrieval with Routing Strategy"

**Authors:** Zhan Su, Fengran Mo, Jinghan Zhang, Yuchen Hui, Jia Ao Sun, Bingbing Wen, Jian-Yun Nie

**Submission Date:** February 26, 2026

**Abstract:**

The conventional approach for adapting dense retrieval to new tasks involves fine-tuning pretrained models for specific applications. However, this method faces two key limitations: difficulty adapting to new domains with limited training data, and the expense of replacing outdated models with newly trained versions—particularly problematic when frequent updates are needed.

To address these issues, the authors propose "dynamic dense retrieval" (DDR). This approach employs prefix tuning as specialized domain modules that can be compositionally combined through a dynamic routing strategy, enabling flexible domain adaptation in retrieval tasks. Testing on six zero-shot downstream tasks demonstrates the method can match traditional dense retrieval performance while requiring only 2% of standard training parameters, suggesting a promising direction for more adaptable dense retrieval systems across diverse applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f592b8c-c221-4806-86c5-2c4789023457",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "84d468fb-f5b9-43b1-ac73-aacd99803c6d",
  "sourceToolAssistantUUID": "5f592b8c-c221-4806-86c5-2c4789023457",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-30T06:14:27.722Z_

<details><summary>↩ Tool result · `toolu_01QQZo3Wpu7rR3WnGAr3aXiH`</summary>

```text
# Paper Information

**Title:** "Mixture-of-Experts for Knowledge Graph Retrieval-Augmented Generation"

**Authors:** Haochen Liu, Guanghui Min, Song Wang, Yada Zhu, Chen Chen, Jundong Li

**Venue:** ICLR 2026 Conference

**Conference/Workshop:** This paper was submitted to the ICLR 2026 Conference (International Conference on Learning Representations). The submission status shows it was a "Withdrawn Submission."

**Abstract Summary:** The authors propose MoRA, a framework using Mixture-of-Experts to improve knowledge graph retrieval for question answering with large language models. The system employs expert-specific and contextual soft prompts to enhance multi-hop reasoning while maintaining computational efficiency with lightweight language models, demonstrating superior performance across multiple KG-based question answering benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed4eb3f0-48c4-43f7-9799-fc5a530c1ad7",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "83e303cf-0144-4f87-a1a9-840cbce80e4d",
  "sourceToolAssistantUUID": "ed4eb3f0-48c4-43f7-9799-fc5a530c1ad7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-30T06:14:28.445Z_

<details><summary>↩ Tool result · `toolu_015szBpkcuJhZAFqtzCR2v77`</summary>

```text
# Paper Details

**Full Title:**
"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models"

**Authors:**
Jiarui Zhang, Xiangyu Liu, Yong Hu, Chaoyue Niu, Fan Wu, Guihai Chen

**Submission Date:**
May 29, 2025 (v1); revised October 17, 2025 (v2)

**Abstract:**
The paper addresses how Retrieval-Augmented Generation improves LLM performance on knowledge tasks by proposing an intelligent routing mechanism. The researchers note that "external documents dynamically affect LLMs' ability to answer queries," yet existing methods rely on static knowledge representations. They introduce RAGRouter, which employs document embeddings and contrastive learning to enable context-aware model selection. Testing across multiple tasks and LLMs demonstrates the approach outperforms individual models and existing routing methods while supporting latency constraints through a score-threshold mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8069542-c54b-4ca9-9680-e25ecf364d88",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "efc721c7-5950-44c6-8442-a3f66a785132",
  "sourceToolAssistantUUID": "b8069542-c54b-4ca9-9680-e25ecf364d88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-30T06:14:30.509Z_

Let me do one more round of searches to find any remaining important papers in this space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc721c7-5950-44c6-8442-a3f66a785132",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG8qSMdD2sbwQRL2uEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17e7fbe6-c9ee-4390-8b05-a12e2088c8b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8ourRzc4tJ7CwUVLvqan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 24982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 803,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 70 · 2026-05-30T06:14:31.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LfeWeHBFaEYv4628JD6TdN`</summary>

```json
{
  "query": "QUAM query-aware retrieval model selection WSDM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17e7fbe6-c9ee-4390-8b05-a12e2088c8b2",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG8qSMdD2sbwQRL2uEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8801deaf-497d-4316-9438-1be331bcec7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8ourRzc4tJ7CwUVLvqan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 24982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 803,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 71 · 2026-05-30T06:14:32.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AHFYrubDF27VeisEqvfUub`</summary>

```json
{
  "query": "\"retrieval model selection\" OR \"retriever selection\" per-query learned 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8801deaf-497d-4316-9438-1be331bcec7d",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG8qSMdD2sbwQRL2uEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07900f54-2b96-4edf-8e9f-da55599c54e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8ourRzc4tJ7CwUVLvqan",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 24982,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 228,
          "output_tokens": 150,
          "cache_read_input_tokens": 24982,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 803,
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

_source line 72 · 2026-05-30T06:14:37.855Z_

<details><summary>↩ Tool result · `toolu_01LfeWeHBFaEYv4628JD6TdN`</summary>

```text
Web search results for query: "QUAM query-aware retrieval model selection WSDM 2024 2025"

Links: [{"title":"QUAM: Adaptive Retrieval through Query Affinity Modelling · smac.pub - smac.pub","url":"https://smac.pub/wsdm2025-quam"},{"title":"GitHub - Mandeep-Rathee/quam","url":"https://github.com/Mandeep-Rathee/quam"},{"title":"QUAM: Adaptive Retrieval through Query Affinity Modelling","url":"https://eprints.gla.ac.uk/340125/"},{"title":"Quam: Adaptive Retrieval through Query Affinity Modelling Mandeep Rathee","url":"https://eprints.gla.ac.uk/340125/2/340125.pdf"},{"title":"bibtex - smac.pub","url":"https://smac.pub/bib/wsdm2025-quam.bib"},{"title":"Quam: Adaptive Retrieval through Query Affinity Modelling | Request PDF","url":"https://www.researchgate.net/publication/389707855_Quam_Adaptive_Retrieval_through_Query_Affinity_Modelling"},{"title":"Quam: Adaptive Retrieval through &lt;u>Qu&lt;/u>ery &lt;u>A&lt;/u>ffinity &lt;u>M&lt;/u>odelling | Proceedings of the Eighteenth ACM International Conference on Web Search and Data Mining","url":"https://dl.acm.org/doi/10.1145/3701551.3703584"},{"title":"Quam: Adaptive Retrieval through Query Affinity Modelling | Scilit","url":"https://www.scilit.com/publications/71b3ca098307eac37600624add126888"},{"title":"(PDF) Quam: Adaptive Retrieval through Query Affinity Modelling","url":"https://www.researchgate.net/publication/385316901_Quam_Adaptive_Retrieval_through_Query_Affinity_Modelling"},{"title":"[2410.20286] Quam: Adaptive Retrieval through Query Affinity Modelling","url":"https://arxiv.org/abs/2410.20286"}]

Based on the search results, here's what I found about QUAM:

QUAM (Quam: Adaptive Retrieval through Query Affinity Modelling) is a paper accepted at the 18th ACM International Conference on Web Search and Data Mining (WSDM 2025), held in Hannover, Germany, from March 10-14, 2025.

**Authors and Key Details:**
The paper is authored by Mandeep Rathee, Sean MacAvaney, and Avishek Anand.

**What QUAM Does:**
QUAM proposes a query-affinity model of adaptive re-ranking that includes two complementary components: (1) a more principled algorithm for document selection, and (2) a data-driven approach to model document co-relevance during indexing.

**Performance:**
The proposed approach improves recall performance by up to 26% over standard re-ranking baselines.

**Broader Impact:**
The query affinity modelling and relevance-aware document graph components can be injected into any adaptive retrieval approach.

The GitHub repository for the paper is available at https://github.com/Mandeep-Rathee/quam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8801deaf-497d-4316-9438-1be331bcec7d",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "454005b7-74c6-4ebb-acf9-bf2f2fccb996",
  "sourceToolAssistantUUID": "8801deaf-497d-4316-9438-1be331bcec7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-30T06:14:41.072Z_

<details><summary>↩ Tool result · `toolu_01AHFYrubDF27VeisEqvfUub`</summary>

```text
Web search results for query: ""retrieval model selection" OR "retriever selection" per-query learned 2024 2025 arXiv"

Links: [{"title":"LTRR: Learning To Rank Retrievers for LLMs","url":"https://arxiv.org/pdf/2506.13743"},{"title":"Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval","url":"https://arxiv.org/pdf/2602.03306"},{"title":"From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation","url":"https://arxiv.org/html/2508.09497v1"},{"title":"MoR: Better Handling Diverse Queries with a Mixture of Sparse, Dense, and Human Retrievers","url":"https://arxiv.org/pdf/2506.15862"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"},{"title":"Generalized Reinforcement Learning for Retriever-Specific Query Rewriter with Unstructured Real-World Documents","url":"https://arxiv.org/html/2507.23242v1"},{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"State-of-the-Art Retrieval Models","url":"https://www.emergentmind.com/topics/state-of-the-art-retrieval-models"}]

I found several relevant papers on arXiv from 2024-2025 related to retrieval model/retriever selection with per-query learned approaches:

1. **LTRR: Learning To Rank Retrievers for LLMs** (arXiv 2506.13743)
   This paper addresses the problem that no single retriever consistently outperforms others across diverse queries and corpora. The paper shows that performance gains are especially pronounced in models trained with the Answer Correctness metric and with pairwise learning approaches, especially with XGBoost.

2. **Learning to Select: Query-Aware Adaptive Dimension Selection for Dense Retrieval** (arXiv 2602.03306)
   This work focuses on how high-dimensional representations can be redundant at the query level, motivating selecting informative dimensions per query to improve effectiveness.

3. **MoR: Better Handling Diverse Queries with a Mixture of Sparse, Dense, and Human Retrievers** (arXiv 2506.15862)
   MoR dynamically selects and combines retrievers for each query by leveraging signals collected both before and after retrieval, eliminating the need for manual retriever selection.

4. **From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation** (arXiv 2508.09497)
   This paper addresses selection strategies within RAG pipelines for passage selection.

These papers represent recent research on learning to select appropriate retrievers or retrieval strategies on a per-query basis for improved performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07900f54-2b96-4edf-8e9f-da55599c54e0",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "a947e4f9-c770-488b-b80c-90240e56d08f",
  "sourceToolAssistantUUID": "07900f54-2b96-4edf-8e9f-da55599c54e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-30T06:14:44.090Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WWekbbgTpS2EfbE96pcZee`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.20286",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a947e4f9-c770-488b-b80c-90240e56d08f",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG9mQJ6qmqWWsnfDGtF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "642fe415-844f-4b03-80ef-d102d93ba173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HtWN4SgTdTiSyV4YcapZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 25785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 75 · 2026-05-30T06:14:44.394Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011pwuWx3nsFaLmXF8HNzbLe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.15862",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "642fe415-844f-4b03-80ef-d102d93ba173",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYG9mQJ6qmqWWsnfDGtF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c501bdd3-9860-47a1-a287-c64d2326b341",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HtWN4SgTdTiSyV4YcapZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 25785,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 25785,
          "cache_creation_input_tokens": 2063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2063,
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

_source line 76 · 2026-05-30T06:14:48.319Z_

<details><summary>↩ Tool result · `toolu_01WWekbbgTpS2EfbE96pcZee`</summary>

```text
# Paper Information

**Full Title:** "Quam: Adaptive Retrieval through Query Affinity Modelling"

**Authors:** 
- Mandeep Rathee
- Sean MacAvaney
- Avishek Anand

**Submission Date:** October 26, 2024

**Complete Abstract:**

The paper addresses the challenge of building relevance models for document ranking in information retrieval. Many knowledge-intensive tasks rely on initial retrieval stages for context selection, but these are limited by recall constraints. The authors propose Quam, a query-affinity model designed to overcome this limitation by using a "relevance-aware document similarity graph to improve recall, especially for low re-ranking budgets." The research demonstrates that their approach achieves recall improvements up to 26% compared to standard re-ranking baselines. Additionally, the modular components can be integrated into existing adaptive retrieval methods, which independently showed up to 12% recall gains. The authors have made their code publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "642fe415-844f-4b03-80ef-d102d93ba173",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "2fd8c106-24dd-4ae3-aa48-61ee3b18e66f",
  "sourceToolAssistantUUID": "642fe415-844f-4b03-80ef-d102d93ba173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-30T06:14:51.751Z_

<details><summary>↩ Tool result · `toolu_011pwuWx3nsFaLmXF8HNzbLe`</summary>

```text
# Paper Information

**Full Title:**
"MoR: Better Handling Diverse Queries with a Mixture of Sparse, Dense, and Human Retrievers"

**Authors:**
Jushaan Singh Kalra, Xinran Zhao, To Eun Kim, Fengyu Cai, Fernando Diaz, Tongshuang Wu

**Submission Date:**
June 18, 2025

**Abstract:**
The research addresses how retrieval-augmented generation systems can dynamically leverage multiple retriever types for individual queries. The authors propose a "zero-shot, weighted combination of heterogeneous retrievers" that integrates lexical matching (BM25) with semantic similarity approaches. Their findings indicate this mixture approach, despite using only 0.8B parameters total, "outperforms every individual retriever and even larger 7B models by +10.8% and +3.9% on average, respectively." The framework also demonstrates potential for incorporating human information sources as retrievers, achieving "a 58.9% relative performance improvement over simulated humans alone."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c501bdd3-9860-47a1-a287-c64d2326b341",
  "isSidechain": true,
  "promptId": "c5e23b13-5a8b-4dcd-b09b-907f969c761c",
  "agentId": "a17cf06e02d2052fb",
  "type": "user",
  "uuid": "1ab2e10f-ffa4-42cd-b1b7-eefb43af407d",
  "sourceToolAssistantUUID": "c501bdd3-9860-47a1-a287-c64d2326b341",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-30T06:16:04.629Z_

Now I have a comprehensive set of verified papers. Here is the consolidated survey list:

---

## Literature Survey: Learned Query Routing for Information Retrieval & Adaptive Retrieval Strategies (2024--2026)

### 1. RouterRetriever: Routing over a Mixture of Expert Embedding Models

- **Authors:** Hyunji Lee, Luca Soldaini, Arman Cohan, Minjoon Seo, Kyle Lo
- **Venue:** AAAI 2025
- **URL:** https://arxiv.org/abs/2409.02685
- **Why important:** First work to demonstrate that routing queries across multiple domain-specific expert embedding models outperforms a single general-purpose embedding model for retrieval. Lightweight routing via pilot embeddings makes it easy to add/remove experts without retraining.
- **One-line summary:** Trains domain-specific retrieval experts and a gate that routes each query to the best expert by comparing query embeddings to pilot embeddings, outperforming both MSMARCO-trained and multi-task models on BEIR by +2.1 and +3.2 nDCG@10 respectively.

---

### 2. MoR: Better Handling Diverse Queries with a Mixture of Sparse, Dense, and Human Retrievers

- **Authors:** Jushaan Singh Kalra, Xinran Zhao, To Eun Kim, Fengyu Cai, Fernando Diaz, Tongshuang Wu
- **Venue:** arXiv preprint, June 2025
- **URL:** https://arxiv.org/abs/2506.15862
- **Why important:** Directly addresses per-query adaptive weighting across heterogeneous retriever types (sparse, dense, human), using zero-shot weighted combination. Shows that small-parameter mixtures beat much larger single retrievers.
- **One-line summary:** A zero-shot, query-level weighted mixture of BM25, dense, and human retrievers that outperforms every individual retriever and larger 7B models by +10.8% and +3.9% on average using only 0.8B parameters total.

---

### 3. LTRR: Learning To Rank Retrievers for LLMs

- **Authors:** To Eun Kim, Fernando Diaz
- **Venue:** arXiv preprint, June 2025
- **URL:** https://arxiv.org/abs/2506.13743
- **Why important:** Formalizes query routing as a learning-to-rank problem over retrievers, connecting it to classical federated/distributed search. Shows that pairwise ranking with XGBoost and answer-correctness objectives generalize well, including on out-of-distribution queries.
- **One-line summary:** Frames retriever selection as a learning-to-rank problem (LTRR) where a model ranks multiple retrievers per query by predicted downstream RAG performance, outperforming single-retriever baselines especially with pairwise XGBoost trained on answer correctness.

---

### 4. DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation

- **Authors:** Hsin-Ling Hsu, Jengnan Tzeng
- **Venue:** arXiv preprint, March 2025
- **URL:** https://arxiv.org/abs/2503.23013
- **Why important:** Directly tackles the per-query interpolation weight problem for sparse-dense hybrid retrieval. Uses LLM-based effectiveness scoring to dynamically calibrate the alpha weight between BM25 and dense retrieval for each query.
- **One-line summary:** Uses an LLM to evaluate top-1 results from BM25 and dense retrieval per query, normalizes effectiveness scores to dynamically set the sparse-dense interpolation weight, yielding +2--7.5 pp gains in Precision@1 and MRR@20 over fixed-weight hybrids.

---

### 5. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity

- **Authors:** Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, Jong C. Park
- **Venue:** NAACL 2024
- **URL:** https://arxiv.org/abs/2403.14403
- **Why important:** Seminal work on routing queries to different retrieval strategies (no retrieval / single-step / iterative multi-step) based on learned query complexity. Demonstrates that a lightweight T5-based classifier can match always-expensive baselines at much lower cost.
- **One-line summary:** Trains a T5-Large classifier on automatically derived complexity labels to route each query to no-retrieval, single-step, or iterative multi-step retrieval, matching expensive baselines at substantially lower cost.

---

### 6. RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models

- **Authors:** Jiarui Zhang, Xiangyu Liu, Yong Hu, Chaoyue Niu, Fan Wu, Guihai Chen
- **Venue:** arXiv preprint, May 2025
- **URL:** https://arxiv.org/abs/2505.23052
- **Why important:** Goes beyond static knowledge-based routing by incorporating document embeddings and contrastive learning to capture how retrieved documents dynamically affect LLM performance, enabling context-aware model selection.
- **One-line summary:** Uses document embeddings and contrastive learning to route queries to the most suitable retrieval-augmented LLM by modeling how external documents dynamically shift model capabilities, outperforming static routing under latency constraints.

---

### 7. Unsupervised Query Routing for Retrieval Augmented Generation

- **Authors:** Feiteng Mu, Liwen Zhang, Yong Jiang, Wenjie Li, Zhen Zhang, Pengjun Xie, Fei Huang
- **Venue:** arXiv preprint, January 2025
- **URL:** https://arxiv.org/abs/2501.07793
- **Why important:** Addresses the annotation bottleneck in query routing by proposing an unsupervised method that constructs upper-bound responses to automatically assess retrieval quality and generate training data for routing, enabling scalable real-world deployment.
- **One-line summary:** Constructs upper-bound responses to automatically evaluate retrieval quality per query and generate training data for routing without manual annotation, significantly improving scalability and out-of-distribution generalization across five datasets.

---

### 8. Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench

- **Authors:** Prakhar Bansal, Shivangi Agarwal
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.03455
- **Why important:** Establishes strong baselines for query routing using classical classifiers (TF-IDF + SVM achieves 93.2% accuracy). Surprisingly shows that lexical features outperform semantic embeddings for routing, providing a practical low-cost baseline.
- **One-line summary:** Evaluates 15 classical classifier configurations for routing queries across RAG strategies on RAGRouter-Bench, finding TF-IDF + SVM achieves 93.2% accuracy with 28.1% token savings, and that lexical features beat semantic embeddings by 3.1 F1 points.

---

### 9. RAGRouter-Bench: A Dataset and Benchmark for Adaptive RAG Routing

- **Authors:** Ziqi Wang, Xi Zhu, Shuhang Lin, Haochen Xue, Minghao Guo, Yongfeng Zhang
- **Venue:** arXiv preprint, February 2026
- **URL:** https://arxiv.org/abs/2602.00296
- **Why important:** Provides the first dedicated benchmark for RAG routing research (7,727 queries, 4 domains, 3 query types). Establishes that no single RAG paradigm dominates and that query-corpus compatibility is the key factor, motivating adaptive routing.
- **One-line summary:** Introduces a 7,727-query benchmark across four domains for evaluating RAG routing, demonstrating that no one-size-fits-all paradigm exists and that adaptive routing based on query-corpus compatibility outperforms fixed approaches.

---

### 10. QUAM: Adaptive Retrieval through Query Affinity Modelling

- **Authors:** Mandeep Rathee, Sean MacAvaney, Avishek Anand
- **Venue:** WSDM 2025
- **URL:** https://arxiv.org/abs/2410.20286
- **Why important:** Proposes a query-affinity model using relevance-aware document similarity graphs to adaptively improve recall, especially under low re-ranking budgets. Modular design allows injection into any adaptive retrieval pipeline.
- **One-line summary:** Builds a relevance-aware document similarity graph for query-adaptive re-ranking that improves recall by up to 26% over standard baselines and by 12% when integrated into existing adaptive retrieval methods.

---

### 11. MIXRAG: Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering

- **Authors:** Lihui Liu, Jiayuan Ding, Subhabrata Mukherjee, Carl J. Yang
- **Venue:** arXiv preprint, September 2025 (arXiv: 2509.21391)
- **URL:** https://arxiv.org/abs/2509.21391
- **Why important:** Applies MoE routing to graph-based retrieval, training multiple specialized graph retrievers (entity, relation, topology) with a dynamic routing controller that adaptively selects and combines retrievers per query.
- **One-line summary:** A Mixture-of-Experts Graph-RAG framework with multiple specialized graph retrievers (entity, relation, topology) and a dynamic routing controller that selects and combines the most relevant retrievers per query, achieving state-of-the-art across multiple graph QA benchmarks.

---

### 12. Towards Dynamic Dense Retrieval with Routing Strategy

- **Authors:** Zhan Su, Fengran Mo, Jinghan Zhang, Yuchen Hui, Jia Ao Sun, Bingbing Wen, Jian-Yun Nie
- **Venue:** arXiv preprint, February 2026
- **URL:** https://arxiv.org/abs/2602.22547
- **Why important:** Proposes "dynamic dense retrieval" (DDR) using prefix-tuned domain modules composed via routing, enabling flexible domain adaptation with only 2% of standard training parameters. Demonstrates that compositional routing of lightweight modules can match full fine-tuning.
- **One-line summary:** Uses prefix tuning as domain-specific modules combined through dynamic routing to achieve flexible domain adaptation for dense retrieval, matching traditional fine-tuning performance with only 2% of the parameters across six zero-shot tasks.

---

### 13. Mixture-of-Retrieval Experts for Reasoning-Guided Multimodal Knowledge Exploitation

- **Authors:** Chunyi Peng, Zhipeng Xu, Zhenghao Liu, Yishan Li, Yukun Yan, Shuo Wang, Yu Gu, Minghe Yu, Ge Yu, Maosong Sun
- **Venue:** arXiv preprint, May 2025
- **URL:** https://arxiv.org/abs/2505.22095
- **Why important:** Extends MoE retrieval routing to the multimodal setting, where diverse retrieval experts are dynamically coordinated based on evolving reasoning states, trained via stepwise group relative policy optimization.
- **One-line summary:** Proposes MoRE (Mixture-of-Retrieval Experts) for multimodal LLMs that dynamically selects among diverse retrieval experts based on evolving reasoning states, trained with stepwise group relative policy optimization, achieving 7%+ gains over baselines.

---

### 14. CluSD: LSTM-based Selective Dense Text Retrieval Guided by Sparse Lexical Retrieval

- **Authors:** Yingrui Yang, Parker Carlson, Yifan Qiao, Wentai Xie, Shanxiu He, Tao Yang
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.10639
- **Why important:** Addresses the efficiency side of query-adaptive retrieval by using sparse retrieval signals to selectively trigger dense retrieval only when needed, via LSTM-based cluster selection.
- **One-line summary:** Uses sparse lexical retrieval scores and an LSTM model to selectively trigger cluster-based dense retrieval only for queries/clusters where it is likely to help, reducing computation while maintaining effectiveness on MS MARCO and BEIR.

---

### Summary of Key Themes

The papers cluster into several complementary research directions:

1. **Expert retriever routing** (RouterRetriever, MoR, LTRR): Learning which specialized retriever to use per query.
2. **Per-query sparse-dense weighting** (DAT): Dynamically setting the interpolation weight between BM25 and dense retrieval.
3. **RAG complexity routing** (Adaptive-RAG, RAGRouter, Unsupervised Query Routing): Choosing retrieval depth/strategy based on query complexity.
4. **Benchmarks and baselines** (RAGRouter-Bench, Lightweight Query Routing): Infrastructure for evaluating routing approaches.
5. **MoE-style retrieval** (MIXRAG, MoRE, DDR): Mixture-of-experts architectures applied directly to retrieval components.
6. **Adaptive re-ranking and selective retrieval** (QUAM, CluSD): Query-adaptive decisions about when and how aggressively to retrieve/re-rank.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ab2e10f-ffa4-42cd-b1b7-eefb43af407d",
  "isSidechain": true,
  "agentId": "a17cf06e02d2052fb",
  "requestId": "req_011CbYGAZ6tzkWAcVvUKDh7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40b5d571-e1db-49e5-91f3-b831d8a8a03f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d9b8af30-59dc-4c7a-a01f-49c577bff243",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyFtbMaky8KmznYboX6Rwh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 27848,
      "output_tokens": 3339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3339,
          "cache_read_input_tokens": 27848,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 702,
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
