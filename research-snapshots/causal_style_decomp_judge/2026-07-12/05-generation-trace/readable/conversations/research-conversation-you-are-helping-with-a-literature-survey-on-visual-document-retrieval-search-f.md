# Research conversation: You are helping with a literature survey on visual document retrieval. Search for the most important recent papers (2024

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 33
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afed2bc46f8f98e40.jsonl`
- **Structured JSON:** [`08aa8748e88fab8c8276.json`](../../sessions/08/08aa8748e88fab8c8276.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

78 recorded events

### User

_source line 1 · 2026-05-30T06:13:40.122Z_

You are helping with a literature survey on visual document retrieval. Search for the most important recent papers (2024-2026) that build on or relate to ColPali (late-interaction visual document retrieval).

Execute these searches and for each promising paper, fetch its arxiv abstract:

1. Search: "ColPali visual document retrieval 2025 2026"
2. Search: "late interaction document retrieval visual 2025 2026"
3. Search: "ColQwen document retrieval embedding 2025 2026"
4. Search: "visual document retrieval without OCR 2025 2026"
5. Search: "site:arxiv.org ColPali document retrieval 2025 2026"

For each paper you find, use WebFetch on its arxiv page to read the abstract and understand what it does. Report back with:
- Full title
- Authors (first author et al.)
- Venue (if published) or arXiv date
- URL
- What the paper does (2-3 sentences)
- Why it's important (citations, awards, impact)

Focus on papers that are NOT in this seed list: ColPali, MMDocIR, Snappy, AGREE, ColParse, MURE, ViDoRe V3, RegionGPT.

Find as many relevant papers as possible (aim for 8-10).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "3ce16b80-04f7-4d82-8a3d-9ff286d66e36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:13:40.127Z_

```json
{
  "parentUuid": "3ce16b80-04f7-4d82-8a3d-9ff286d66e36",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
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
  "uuid": "7176f381-bb3a-4730-82b7-2958c652e831",
  "timestamp": "2026-05-30T06:13:40.127Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:13:40.128Z_

```json
{
  "parentUuid": "7176f381-bb3a-4730-82b7-2958c652e831",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b27c7e79-f8d8-48d8-a064-811ff3754d1f",
  "timestamp": "2026-05-30T06:13:40.128Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:13:43.477Z_



I'll start by loading the WebSearch and WebFetch tools, then execute the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b27c7e79-f8d8-48d8-a064-811ff3754d1f",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5GxucxBrtGfBNpkkY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64c7ce3c-4133-43ec-87e3-79e161ae7cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRm9zgj8vUJpjPUSpCT96w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9058,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9058,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 5 · 2026-05-30T06:13:43.992Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019BgzQ3CEnjn6jvcA2KbigD`</summary>

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
  "parentUuid": "64c7ce3c-4133-43ec-87e3-79e161ae7cd8",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5GxucxBrtGfBNpkkY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd09aae-ed5d-4c3c-91ef-fd017a1b5dc1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRm9zgj8vUJpjPUSpCT96w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9058,
      "cache_read_input_tokens": 0,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9058,
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

_source line 6 · 2026-05-30T06:13:44.003Z_

<details><summary>↩ Tool result · `toolu_019BgzQ3CEnjn6jvcA2KbigD`</summary>

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
  "parentUuid": "0bd09aae-ed5d-4c3c-91ef-fd017a1b5dc1",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "e70b3004-c4a4-4fba-af92-e8f953301177",
  "sourceToolAssistantUUID": "0bd09aae-ed5d-4c3c-91ef-fd017a1b5dc1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:13:46.533Z_



Now let me execute all 5 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e70b3004-c4a4-4fba-af92-e8f953301177",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d5218d6-bdb1-42d2-ab32-9bbe95bd0919",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

_source line 8 · 2026-05-30T06:13:47.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RJe1Y5ecwxS5ECucQdqELV`</summary>

```json
{
  "query": "ColPali visual document retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d5218d6-bdb1-42d2-ab32-9bbe95bd0919",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f384033-cef5-4635-b6d6-f51b7a3e5c73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

_source line 9 · 2026-05-30T06:13:47.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QRWgWik9YEb7jWeqonazmq`</summary>

```json
{
  "query": "late interaction document retrieval visual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f384033-cef5-4635-b6d6-f51b7a3e5c73",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "368d010c-baf1-40e0-8413-159dcd2bd47e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

_source line 10 · 2026-05-30T06:13:48.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JxCUvskNev1qdyLdp6vcbc`</summary>

```json
{
  "query": "ColQwen document retrieval embedding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "368d010c-baf1-40e0-8413-159dcd2bd47e",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af69fbfd-9b20-4278-b7cd-a885a6242c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

_source line 11 · 2026-05-30T06:13:48.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XG1CMhZz2D4T97H3chgQMm`</summary>

```json
{
  "query": "visual document retrieval without OCR 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af69fbfd-9b20-4278-b7cd-a885a6242c31",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "295eea69-6490-4d19-91d1-9bb577b65bcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

_source line 12 · 2026-05-30T06:13:49.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MctF7DstJbeLaKGDJjuLuz`</summary>

```json
{
  "query": "site:arxiv.org ColPali document retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "295eea69-6490-4d19-91d1-9bb577b65bcc",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG5ZmCes5Bx2sHBYnfD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c732204-5f31-4584-885d-6dba1563b43c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfMe5zBwt2ENLQfBR1kHfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 9058,
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

### Tool result

_source line 13 · 2026-05-30T06:13:55.219Z_

<details><summary>↩ Tool result · `toolu_01MctF7DstJbeLaKGDJjuLuz`</summary>

```text
Web search results for query: "site:arxiv.org ColPali document retrieval 2025 2026"

Links: [{"title":"[2407.01449v6] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449v6"},{"title":"[PDF] ColPali: Efficient Document Retrieval with Vision Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ColPali:-Efficient-Document-Retrieval-with-Vision-Faysse-Sibille/c948e2d00ac2628ed4098a009c67c81ea4cc00a2"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/html/2407.01449v5"},{"title":"[2407.01449] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models 👀","url":"https://huggingface.co/blog/manu/colpali"},{"title":"[2506.21601] Hierarchical Patch Compression for ColPali: Efficient Multi-Vector Document Retrieval with Dynamic Pruning and Quantization","url":"https://arxiv.org/abs/2506.21601"},{"title":"Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/pdf/2512.02660"}]

Based on the search results, here are the arXiv papers related to ColPali document retrieval from 2025-2026:

## Main ColPali Paper

ColPali is a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages, which largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. The original paper was first posted in June 2024, with the most recent version (v6) updated on February 28, 2025.

## Related Recent Work (2025-2026)

1. **Hierarchical Patch Compression for ColPali** - HPC-ColPali is a Hierarchical Patch Compression framework that enhances the efficiency of ColPali while preserving its retrieval accuracy. This paper was posted on July 2, 2025.

2. **Spatially-Grounded Document Retrieval** - A paper from December 2025 builds on ColPali by achieving region-level retrieval through spatial coordinate mapping to return only the document regions that are both structurally coherent and semantically relevant.

The original ColPali work also introduced ViDoRe, a comprehensive benchmark to evaluate systems on page-level document retrieval with a wide coverage of domains, visual elements, and languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c732204-5f31-4584-885d-6dba1563b43c",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "9812e77c-a163-47dc-9267-3bc87bb92f06",
  "sourceToolAssistantUUID": "2c732204-5f31-4584-885d-6dba1563b43c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-30T06:13:55.257Z_

<details><summary>↩ Tool result · `toolu_01RJe1Y5ecwxS5ECucQdqELV`</summary>

```text
Web search results for query: "ColPali visual document retrieval 2025 2026"

Links: [{"title":"ColPali Methodology: Multi-Modal Retrieval","url":"https://www.emergentmind.com/topics/colpali-methodology"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models | OpenReview","url":"https://openreview.net/forum?id=ogjBpZ8uSi"},{"title":"ColPali: Better Document Retrieval with VLMs and ColBERT Embeddings - Zilliz blog","url":"https://zilliz.com/blog/colpali-enhanced-doc-retrieval-with-vision-language-models-and-colbert-strategy"},{"title":"ColPali + Milvus: Redefining Document Retrieval with Vision-Language Models - Zilliz blog","url":"https://zilliz.com/blog/colpali-milvus-redefine-document-retrieval-with-vision-language-models"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/html/2407.01449v5"},{"title":"ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/pdf/2407.01449"},{"title":"[2407.01449] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449"},{"title":"ColPali: EFFICIENT DOCUMENT RETRIEVAL WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf"},{"title":"[2512.02660] Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/abs/2512.02660"}]

Based on the search results, here's what I found about ColPali visual document retrieval in 2025-2026:

## Overview

ColPali is a family of vision-language retrieval methodologies for visually-rich documents, characterized by direct multi-patch image embedding and late-interaction scoring—enabling document retrieval pipelines that bypass traditional OCR and granular text analysis.

## Core Technology

ColPali is a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages, and combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable.

## Recent Developments (2025-2026)

Several variants and improvements have emerged recently:

- Hierarchical Patch Compression (HPC-ColPali) uses K-means quantization to compress patch embeddings into 1-byte centroid indices, and Light-ColPali/ColQwen2 merges patch vectors using hierarchical agglomerative clustering on post-projector embeddings, drastically reducing memory footprint.

- A newer hybrid architecture unifies late-interaction multimodal retrieval with OCR-based systems by using ColPali's patch-level similarity scores as spatial relevance filters over OCR-extracted regions.

## Benchmarking

ViDoRe is a comprehensive benchmark for page-level document retrieval with wide coverage of domains, visual elements, and languages, addressing practical document retrieval scenarios where queries often necessitate both textual and visual understanding for accurate document matching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f384033-cef5-4635-b6d6-f51b7a3e5c73",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "7e341247-1484-416c-b34d-c9619e514e63",
  "sourceToolAssistantUUID": "4f384033-cef5-4635-b6d6-f51b7a3e5c73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-30T06:13:55.595Z_

<details><summary>↩ Tool result · `toolu_01QRWgWik9YEb7jWeqonazmq`</summary>

```text
Web search results for query: "late interaction document retrieval visual 2025 2026"

Links: [{"title":"[2505.07730v1] Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"http://arxiv.org/abs/2505.07730v1"},{"title":"[2505.07730] Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/abs/2505.07730"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/html/2602.03992v2"},{"title":"LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026 | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21324-2_11"},{"title":"Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/pdf/2505.07730"},{"title":"Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/html/2505.07730"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.03992"}]

Here are the search results for your query about late interaction document retrieval visual research from 2025-2026:

## Key Findings

**Visual Document Retrieval with Late Interaction:**

Visual Document Retrieval (VDR) is an emerging research area that focuses on encoding and retrieving document images directly, bypassing the dependence on Optical Character Recognition (OCR) for document search. A recent advance in VDR was introduced by ColPali, which significantly improved retrieval effectiveness through a late interaction mechanism.

**Trade-offs of Late Interaction:**

Late interaction yields considerable improvements in retrieval effectiveness; however, it also introduces computational inefficiencies during inference. Research investigates the specific contributions of late interaction by looking into query-patch matching in the context of visual document retrieval, finding that although query tokens cannot explicitly match image patches as in the text retrieval scenario, they tend to match patches containing visually similar tokens or their surrounding patches.

**Recent State-of-the-Art Models:**

The Nemotron ColEmbed V2 is a family of open-weights models that achieve state-of-the-art performance on the ViDoRe benchmarks, with three model sizes—3B, 4B, and 8B parameters—based on pre-trained vision-language models. The 8B model ranks first on the ViDoRe V3 leaderboard as of February 03, 2026, achieving an average NDCG@10 of 63.42.

**Research Community:**

The First Late Interaction Workshop (LIR) is being held at ECIR 2026 on April 02, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "368d010c-baf1-40e0-8413-159dcd2bd47e",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "00667067-dbc9-4b0c-80d3-5615039d103d",
  "sourceToolAssistantUUID": "368d010c-baf1-40e0-8413-159dcd2bd47e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:13:55.638Z_

<details><summary>↩ Tool result · `toolu_01JxCUvskNev1qdyLdp6vcbc`</summary>

```text
Web search results for query: "ColQwen document retrieval embedding 2025 2026"

Links: [{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/html/2506.04997v1"},{"title":"[2512.02660] Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation","url":"https://arxiv.org/abs/2512.02660"},{"title":"Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.03992"},{"title":"Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy","url":"https://arxiv.org/html/2510.22215v2"},{"title":"ColPali Methodology: Multi-Modal Retrieval","url":"https://www.emergentmind.com/topics/colpali-methodology"},{"title":"REAL-MM-RAG: A Real-World Multi-Modal Retrieval Benchmark","url":"https://arxiv.org/pdf/2502.12342"},{"title":"Document Understanding with Artificial Intelligence (AI)","url":"https://pyxida.aueb.gr/bitstreams/b6f9d1ed-9015-494a-88e4-90a9f5a4a420/download"},{"title":"Exploration of Augmentation Strategies in Multi-modal ...","url":"https://arxiv.org/pdf/2512.16802"}]

Based on the search results, here's what I found about ColQwen document retrieval embedding developments in 2025-2026:

## ColQwen Overview

ColQwen is a newer variant that utilizes Qwen2-VL for generating multi-vector embeddings for ColBERT-style late interaction retrieval. These methods have demonstrated significant improvements over earlier text-based and OCR-dependent retrieval approaches.

## Recent Developments

**ColQwen2 and Beyond:**
ColPali/ColQwen2 represents a significant advancement in the field. ColQwen2 divides each page into 768 tokens, each represented by a 128-dimensional vector.

**Memory Optimization:**
Recent research has focused on reducing storage requirements. Light-ColPali/ColQwen2 merges patch vectors using hierarchical agglomerative clustering on post-projector embeddings, drastically reducing memory footprint.

**Latest Variant - ColQwen3:**
ColQwen3-4B with percentile-50 thresholding achieves 59.7% hit rate at IoU@0.5 for within-page localization on BBox-DocVQA.

**Hybrid Approaches:**
More recent work has explored combining efficiency with accuracy. Various efficiency-oriented variants of ColQwen2.5-based multi-vector models include document patch pooling and document patch pruning approaches.

These developments represent ongoing efforts to improve the efficiency and effectiveness of visual document retrieval systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af69fbfd-9b20-4278-b7cd-a885a6242c31",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "4a3125fe-4991-4867-89ff-c9855b515530",
  "sourceToolAssistantUUID": "af69fbfd-9b20-4278-b7cd-a885a6242c31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:13:57.688Z_

<details><summary>↩ Tool result · `toolu_01XG1CMhZz2D4T97H3chgQMm`</summary>

```text
Web search results for query: "visual document retrieval without OCR 2025 2026"

Links: [{"title":"ModernVBERT: Towards Smaller Visual Document Retrievers","url":"https://arxiv.org/html/2510.01149v1"},{"title":"Transitioning from Traditional OCR to Intelligent Document Processing: Why Legacy Models Fail in the LLM Era | by mehrdad mohamadali | Medium","url":"https://medium.com/@mehrdadmohamadali7/transitioning-from-traditional-ocr-to-intelligent-document-processing-why-legacy-models-fail-in-2a1022a67b53"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented ...","url":"https://aclanthology.org/2025.emnlp-main.464.pdf"},{"title":"Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding","url":"https://arxiv.org/html/2510.15253v3"},{"title":"Lost in OCR Translation? Vision-Based Approaches to Robust Document Retrieval","url":"https://arxiv.org/pdf/2505.05666"},{"title":"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models","url":"https://arxiv.org/pdf/2509.15432"},{"title":"Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval","url":"https://arxiv.org/pdf/2602.19961"}]

Based on the search results, here are the key findings about visual document retrieval without OCR in 2025-2026:

## Recent Developments in OCR-Free Document Retrieval

Vision-based document retrieval models now process document pages as images without OCR and produce multi-vector embeddings via late-interaction mechanisms. Several prominent systems have emerged in this space:

**Key Models and Approaches:**
- ColPali and its extension ColQwen2.5 use late interaction retrieval paradigms over page image embeddings, capturing layout and textual context without OCR
- Jina-v4 is a multimodal embedding model combining visual and textual inputs with support for multi-vector embeddings, using adapters over a unified backbone to excel on visually rich document retrieval

**Industry Evolution:**
In 2025, the industry transitioned to Agentic IDP—autonomous AI agents acting as "reasoning engines" that combine Agentic OCR (interpreting visual structure) with orchestration for task planning and self-correction.

**Vision-Language Model Innovations:**
A newer frontier in 2025 is the rise of Vision-Language Models like Synapse OV, which utilizes Optical Context Compression to treat document pages as visual signals, converting them into compressed visual tokens with a 7x to 20x reduction in token count compared to traditional text representations.

**Multimodal RAG Progress:**
Recent methods represent multi-page documents as image sequences, enabling visual encoders to extract richer representations, moving beyond traditional OCR-based approaches that fail to adequately capture cross-modal cues and structural semantics in visually rich documents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "295eea69-6490-4d19-91d1-9bb577b65bcc",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "d8be3493-f3dc-4089-8585-a47c965e558c",
  "sourceToolAssistantUUID": "295eea69-6490-4d19-91d1-9bb577b65bcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-30T06:14:01.211Z_

I found many promising papers. Let me now fetch the abstracts from arxiv for the most relevant ones, and run additional searches to find more papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8be3493-f3dc-4089-8585-a47c965e558c",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a56045a-dc41-4083-87c1-bbfe88737022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 19 · 2026-05-30T06:14:02.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XkbZyJuUiDiZuEaAriaJ7k`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.07730",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a56045a-dc41-4083-87c1-bbfe88737022",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9af16b0c-be50-4321-8a19-66d366fb4631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 20 · 2026-05-30T06:14:03.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H1aykRc9UmnvQrbVNMvcVN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03992",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9af16b0c-be50-4321-8a19-66d366fb4631",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebee6cd6-9fd2-47de-a454-57b2de9f2c8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 21 · 2026-05-30T06:14:04.025Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KHbQfxQ8qnkb4KLAFnUWef`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.02660",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebee6cd6-9fd2-47de-a454-57b2de9f2c8f",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a96b044c-3e9f-4260-8422-e62cf5865ae9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 22 · 2026-05-30T06:14:04.497Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013HxL1pftF9uazVWnN72hji`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01149",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96b044c-3e9f-4260-8422-e62cf5865ae9",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5c75763-686e-4599-b626-6aa09f23ab95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 23 · 2026-05-30T06:14:05.439Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VsqnigtqwoaiQNF3oc3xU9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.22215",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c75763-686e-4599-b626-6aa09f23ab95",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da7aea54-4c09-439f-8c4f-06ba0f30b0f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 24 · 2026-05-30T06:14:05.939Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011nUcdEyc9X69mhkHYw39xy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.15432",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7aea54-4c09-439f-8c4f-06ba0f30b0f0",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f57c340-1347-431c-a167-9bc099b36b81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 25 · 2026-05-30T06:14:06.380Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XKVsGJfVpsfF65ZjyjcFNf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.21601",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f57c340-1347-431c-a167-9bc099b36b81",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd9512e3-e88d-4279-87ca-b6e43f45822d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 26 · 2026-05-30T06:14:07.322Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fi4WNzHc9gpzuAL8jKBDfY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.12342",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd9512e3-e88d-4279-87ca-b6e43f45822d",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "223a3425-c103-4a1f-8641-66b44564f61c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 27 · 2026-05-30T06:14:07.774Z_

<details><summary>↩ Tool result · `toolu_01XkbZyJuUiDiZuEaAriaJ7k`</summary>

```text
# Paper Summary

**Full Title:** "Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction"

**Authors:** Jingfen Qiao, Jia-Huei Ju, Xinyu Ma, Evangelos Kanoulas, Andrew Yates

**Submission Date:** May 12, 2025

**Complete Abstract:**

The paper investigates visual document retrieval (VDR), which encodes and retrieves document images directly without relying on OCR. The researchers examine reproducibility and replicability of VDR methods across multiple vision-language models, confirming that "late interaction yields considerable improvements in retrieval effectiveness," though it introduces computational inefficiencies during inference. The study evaluates model adaptability to textual inputs and robustness across text-intensive datasets. A key finding reveals that query tokens "tend to match the patch contains visually similar tokens or their surrounding patches," providing insights into how late interaction mechanisms function in visual document retrieval contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9af16b0c-be50-4321-8a19-66d366fb4631",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "f0b85bd5-72ed-4647-985b-4ac1b07da074",
  "sourceToolAssistantUUID": "9af16b0c-be50-4321-8a19-66d366fb4631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T06:14:07.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KB6JQwbDtKMj42HuggxQPQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.05666",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b85bd5-72ed-4647-985b-4ac1b07da074",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ecb38a8-86ae-4f71-aee7-7fac9a8327fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 29 · 2026-05-30T06:14:08.491Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JcGkW81xdSfuGU8n3NVBxY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.19961",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ecb38a8-86ae-4f71-aee7-7fac9a8327fd",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG6ZweDSKi1GFTXJbW7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60d32d5b-f53b-4519-952e-02e6a4767dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012P2QkYhShaeaBd4Bhb8BPM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 10180,
      "output_tokens": 879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 741,
          "output_tokens": 879,
          "cache_read_input_tokens": 10180,
          "cache_creation_input_tokens": 3509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3509,
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

_source line 30 · 2026-05-30T06:14:08.598Z_

<details><summary>↩ Tool result · `toolu_013HxL1pftF9uazVWnN72hji`</summary>

```text
# Paper Summary

**Full Title:**
"ModernVBERT: Towards Smaller Visual Document Retrievers"

**Authors:**
Paul Teiletche, Quentin Macé, Max Conti, Antonio Loison, Gautier Viaud, Pierre Colombo, Manuel Faysse

**Submission Date:**
October 1, 2025 (v1); last revised December 16, 2025 (v3)

**Abstract:**
The paper addresses visual document retrieval (VDR) by demonstrating that repurposing generative vision-language models "bottlenecks retrieval performance." Through systematic experimentation, the researchers identify key factors including attention masking, image resolution, modality alignment, and contrastive objectives. They introduce ModernVBERT, a 250-million-parameter encoder that "outperforms recent models up to 10 times larger when fine-tuned on document retrieval tasks," enabling efficient CPU-based inference while maintaining strong performance in Retrieval-Augmented Generation applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5c75763-686e-4599-b626-6aa09f23ab95",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "e962cd37-adeb-4a2d-915e-ff43aa1b7866",
  "sourceToolAssistantUUID": "b5c75763-686e-4599-b626-6aa09f23ab95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T06:14:08.831Z_

<details><summary>↩ Tool result · `toolu_01H1aykRc9UmnvQrbVNMvcVN`</summary>

```text
# Paper Information

**Full Title:** "Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval"

**Authors:** Gabriel de Souza P. Moreira, Ronay Ak, Mengyao Xu, Oliver Holworthy, Benedikt Schifferer, Zhiding Yu, Yauhen Babakhin, Radek Osmulski, Jiarui Cai, Ryan Chesler, Bo Liu, and Even Oldridge

**Submission Date:** February 3, 2026 (v1); revised April 1, 2026 (v2)

**Abstract:**

The paper introduces embedding models designed for document retrieval in RAG systems. These models leverage vision-language models to preserve visual information while simplifying indexing compared to OCR-based approaches. The authors present three variants with 3B, 4B, and 8B parameters, built on NVIDIA Eagle 2 and Qwen3-VL backbones. "The 8B model ranks first on the ViDoRe V3 leaderboard" with an NDCG@10 score of 63.42. Key techniques include cluster-based sampling, hard-negative mining, bidirectional attention, late interaction, and model merging. The work also addresses computational challenges related to late interaction mechanisms and explores embedding dimension optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebee6cd6-9fd2-47de-a454-57b2de9f2c8f",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "183c9d1e-b71d-432f-9c2c-9487b500400b",
  "sourceToolAssistantUUID": "ebee6cd6-9fd2-47de-a454-57b2de9f2c8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T06:14:09.094Z_

<details><summary>↩ Tool result · `toolu_01KHbQfxQ8qnkb4KLAFnUWef`</summary>

```text
# Paper Information

**Full Title:** "Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation"

**Author:** Athos Georgiou

**Submission Date:** December 2, 2025 (v1); last revised January 1, 2026 (v3)

**Abstract:**

This research presents a hybrid system merging two document retrieval approaches. The method leverages patch-level similarity scores from ColPali models as spatial relevance filters applied to OCR-extracted text regions. The authors formalize coordinate mapping between vision transformer patches and OCR bounding boxes, introduce intersection metrics for relevance propagation, and establish theoretical bounds on area efficiency.

Testing on BBox-DocVQA with ground-truth bounding boxes shows ColQwen3-4B achieving 59.7% hit rate at IoU@0.5 for within-page localization using percentile-50 thresholding, with mean IoU of 0.569. The approach reduces context tokens by 28.8% versus all OCR regions and 52.3% versus full-page image tokens. It requires no additional training at inference time. The authors released "Snappy," an open-source implementation available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a96b044c-3e9f-4260-8422-e62cf5865ae9",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "bf16f5e8-9867-44ee-99aa-c9421c8cc8ec",
  "sourceToolAssistantUUID": "a96b044c-3e9f-4260-8422-e62cf5865ae9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:14:10.230Z_

<details><summary>↩ Tool result · `toolu_011nUcdEyc9X69mhkHYw39xy`</summary>

```text
# SERVAL Paper Information

**Full Title:**
"SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models"

**Authors:**
- Thong Nguyen
- Yibin Lei
- Jia-Huei Ju
- Andrew Yates

**Submission Date:**
September 18, 2025

**Abstract:**
The researchers introduce a zero-shot approach where "a vision-language model first produces a detailed textual description of each document image, which is then embedded by a standard text encoder." On the ViDoRe-v2 benchmark, this method achieved 63.4% nDCG@5, outperforming specialized encoders. The approach demonstrates better scalability for large collections and broader multilingual support. The authors conclude that contemporary vision-language models can effectively serve as a semantic proxy, eliminating the need for computationally demanding text-image contrastive training and establishing a baseline for future visual document retrieval systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f57c340-1347-431c-a167-9bc099b36b81",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "bf69a266-6038-4c43-866f-f55d20da842e",
  "sourceToolAssistantUUID": "6f57c340-1347-431c-a167-9bc099b36b81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:14:10.291Z_

<details><summary>↩ Tool result · `toolu_01VsqnigtqwoaiQNF3oc3xU9`</summary>

```text
# Paper Information

**Full Title:** "Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy"

**Authors:** Juyeon Kim, Geon Lee, Dongwon Choi, Taeuk Kim, Kijung Shin

**Submission Date:** October 25, 2025 (v1); last revised April 20, 2026 (v2)

**Abstract:**

The researchers address a key challenge in document retrieval by proposing "a plug-and-play two-stage hybrid-vector framework" that balances computational efficiency against retrieval precision. Their approach, named HEAVEN, operates through two sequential stages: initial screening using single-vector methods on visually-summarized composite pages, followed by reranking employing multi-vector techniques with token filtering based on linguistic relevance.

To support rigorous evaluation, the team introduces ViMDoc, "a benchmark for visually rich, multi-document, and long-document retrieval." Testing across four benchmarks demonstrates that HEAVEN "attains 99.87% of the Recall@1 performance of multi-vector models on average while reducing per-query computation by 99.82%," effectively achieving both efficiency gains and competitive accuracy. The authors have made their implementation and evaluation datasets publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da7aea54-4c09-439f-8c4f-06ba0f30b0f0",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "e4eb29de-bbc3-4898-b4d3-22a7a9039e0b",
  "sourceToolAssistantUUID": "da7aea54-4c09-439f-8c4f-06ba0f30b0f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-30T06:14:10.767Z_

<details><summary>↩ Tool result · `toolu_01XKVsGJfVpsfF65ZjyjcFNf`</summary>

```text
# Paper Information

**Full Title:** "Hierarchical Patch Compression for ColPali: Efficient Multi-Vector Document Retrieval with Dynamic Pruning and Quantization"

**Author:** Duong Bach

**Submission Date:** June 19, 2025 (v1); revised July 2, 2025 (v2)

**Abstract:**

The paper introduces HPC-ColPali, a framework designed to improve multi-vector document retrieval systems. The approach combines three main techniques: K-Means quantization reduces patch embeddings to single-byte indices (up to 32× storage reduction); attention-guided dynamic pruning keeps only the most relevant patches, decreasing computational costs by 60% with minimal accuracy loss; and optional binary encoding enables rapid similarity searches in resource-limited settings. Testing on ViDoRe and SEC-Filings datasets shows the method achieves 30–50% lower query latency while preserving retrieval precision. When applied to legal document summarization through retrieval-augmented generation, it cuts hallucination rates by 30% and reduces end-to-end processing time by half. The authors have released code publicly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd9512e3-e88d-4279-87ca-b6e43f45822d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "4523be4e-b4d3-4aeb-93da-61aab33b3409",
  "sourceToolAssistantUUID": "bd9512e3-e88d-4279-87ca-b6e43f45822d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:14:11.807Z_

<details><summary>↩ Tool result · `toolu_01Fi4WNzHc9gpzuAL8jKBDfY`</summary>

```text
# REAL-MM-RAG Paper Details

**Full Title:** REAL-MM-RAG: A Real-World Multi-Modal Retrieval Benchmark

**Authors:** Navve Wasserman, Roi Pony, Oshri Naparstek, Adi Raz Goldfarb, Eli Schwartz, Udi Barzelay, Leonid Karlinsky

**Submission Date:** February 17, 2025

**Abstract:** The paper presents an automatically generated benchmark addressing gaps in multi-modal document retrieval for Retrieval-Augmented Generation systems. The work focuses on four essential properties: multi-modal documents, enhanced difficulty, realistic RAG queries, and accurate labeling. The authors introduce a multi-difficulty evaluation scheme based on query rephrasing to assess semantic understanding beyond keyword matching. Their testing reveals significant model weaknesses, particularly with table-heavy documents and query variation robustness. To address these limitations, they created a rephrased training dataset and a finance-focused, table-heavy collection. Models fine-tuned on these resources achieve state-of-the-art retrieval performance on the REAL-MM-RAG benchmark while also providing improved training data and models for multi-modal RAG systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "223a3425-c103-4a1f-8641-66b44564f61c",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "82586480-3ec4-468c-b322-3b91d1ad64b4",
  "sourceToolAssistantUUID": "223a3425-c103-4a1f-8641-66b44564f61c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T06:14:12.085Z_

<details><summary>↩ Tool result · `toolu_01KB6JQwbDtKMj42HuggxQPQ`</summary>

```text
# Paper Details

**Full Title:** "Lost in OCR Translation? Vision-Based Approaches to Robust Document Retrieval"

**Authors:**
- Alexander Most
- Joseph Winjum
- Ayan Biswas
- Shawn Jones
- Nishath Rajiv Ranasinghe
- Dan O'Malley
- Manish Bhattarai

**Submission Date:** May 8, 2025

**Abstract:**
The research presents a comparative analysis between vision-based document retrieval systems (ColPali) and conventional OCR-dependent pipelines. The study evaluates both approaches using Llama 3.2 (90B) and Nougat OCR across documents of varying quality. Beyond standard retrieval metrics, the authors introduce "a semantic answer evaluation benchmark to assess end-to-end question-answering performance." Key findings suggest that while vision-based systems excel on documents they were trained on, OCR-based approaches demonstrate superior generalization to previously unseen, lower-quality documents. The paper emphasizes tradeoffs between computational efficiency and semantic accuracy for practitioners selecting retrieval systems for production use.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ecb38a8-86ae-4f71-aee7-7fac9a8327fd",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "55e6c8ec-0820-4873-b14f-f891e8cc114e",
  "sourceToolAssistantUUID": "5ecb38a8-86ae-4f71-aee7-7fac9a8327fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T06:14:14.381Z_

<details><summary>↩ Tool result · `toolu_01JcGkW81xdSfuGU8n3NVBxY`</summary>

```text
# Paper Information

**Full Title:** "Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval"

**Authors:** Yibo Yan, Jiahao Huo, Guanbo Feng, Mingdong Ou, Yi Cao, Xin Zou, Shuliang Liu, Yuanhuiyi Lyu, Yu Huang, Jungang Li, Kening Zheng, Xu Zheng, Philip S. Yu, James Kwok, and Xuming Hu

**Submission Date:** February 23, 2026 (v1); revised March 23, 2026 (v2)

**Abstract:** The paper addresses Visual Document Retrieval (VDR) as a critical area that bridges "unstructured visually rich data and precise information acquisition." Unlike traditional image retrieval, visual documents feature "dense textual content, intricate layouts, and fine-grained semantic dependencies." The survey examines the VDR field through the lens of Multimodal Large Language Models, covering benchmark landscapes, methodological approaches including multimodal embedding and reranking models, and the integration of "Retrieval-Augmented Generation (RAG) and Agentic systems for complex document intelligence," while identifying challenges and future research directions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60d32d5b-f53b-4519-952e-02e6a4767dc9",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "2e58432c-bea4-416e-bbad-69603178b952",
  "sourceToolAssistantUUID": "60d32d5b-f53b-4519-952e-02e6a4767dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-30T06:14:17.469Z_

Good, I have many papers. Let me search for a few more to ensure I find 8-10 distinct papers not in the seed list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e58432c-bea4-416e-bbad-69603178b952",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG7oJazuEdSYYa8vmkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "440a279c-c1f5-4abb-bf26-8fa590ae4807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApDPtFZh59oJYVfSCUoS3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10806,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10806,
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

_source line 40 · 2026-05-30T06:14:17.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ba4t2Xn2iALcmwX9zsEuPy`</summary>

```json
{
  "query": "ViDoRAG visual document retrieval augmented generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "440a279c-c1f5-4abb-bf26-8fa590ae4807",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG7oJazuEdSYYa8vmkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f524b51e-e550-4366-8aa2-a9a6a453ffc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApDPtFZh59oJYVfSCUoS3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10806,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10806,
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

_source line 41 · 2026-05-30T06:14:19.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WidWQcAkxHumPoZ3PzCoj6`</summary>

```json
{
  "query": "Jina-v4 multimodal embedding document retrieval 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f524b51e-e550-4366-8aa2-a9a6a453ffc8",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG7oJazuEdSYYa8vmkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da63820c-3031-4844-89ee-acc9187cb460",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApDPtFZh59oJYVfSCUoS3j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10806,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10806,
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

_source line 42 · 2026-05-30T06:14:19.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YV6JT1kKxytoxHpDdnQG9G`</summary>

```json
{
  "query": "\"storage efficient\" visual document retrieval patch embedding reduction 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da63820c-3031-4844-89ee-acc9187cb460",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG7oJazuEdSYYa8vmkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e60ee4b3-1524-4c5e-81d7-af8fcd11c908",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApDPtFZh59oJYVfSCUoS3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10806,
      "cache_read_input_tokens": 7413,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 10806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10806,
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

_source line 43 · 2026-05-30T06:14:25.006Z_

<details><summary>↩ Tool result · `toolu_01WidWQcAkxHumPoZ3PzCoj6`</summary>

```text
Web search results for query: "Jina-v4 multimodal embedding document retrieval 2025 2026 arxiv"

Links: [{"title":"Jina Embeddings v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://jina.ai/news/jina-embeddings-v4-universal-embeddings-for-multimodal-multilingual-retrieval/"},{"title":"[2506.18902v3] jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/abs/2506.18902v3"},{"title":"[2506.18902] jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/abs/2506.18902"},{"title":"[2506.18902v2] jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"http://arxiv.org/abs/2506.18902v2"},{"title":"jinaai/jina-embeddings-v4 · Hugging Face","url":"https://huggingface.co/jinaai/jina-embeddings-v4"},{"title":"jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval","url":"https://arxiv.org/html/2506.18902v3"},{"title":"jina-embeddings-v4 - Search Foundation Models","url":"https://jina.ai/models/jina-embeddings-v4/"},{"title":"jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/jina-embeddings-v4-universal-embeddings-multimodal-multilingual"},{"title":"Embedding API","url":"https://jina.ai/embeddings/"},{"title":"arXiv:2506.18902v3 [cs.AI] 7 Jul 2025","url":"https://arxiv.org/pdf/2506.18902"}]

I found relevant results about Jina-embeddings-v4 and its multimodal capabilities for document retrieval. Here's what the search revealed:

## Jina-embeddings-v4 Overview

Jina-embeddings-v4 is a 3.8 billion parameter multimodal embedding model that unifies text and image representations through a novel architecture supporting both single-vector and multi-vector embeddings in the late interaction style.

## Key Features

The model incorporates task-specific Low-Rank Adaptation (LoRA) adapters to optimize performance across diverse retrieval scenarios, including query-document retrieval, semantic text similarity, and code search. The model is specially designed for complex document retrieval, including visually rich documents with charts, tables, and illustrations.

## Performance and Architecture

Jina-embeddings-v4 achieves state-of-the-art performance on both single-modal and cross-modal retrieval tasks, with particular strength in processing visually rich content such as tables, charts, diagrams, and mixed-media formats.

## ArXiv Publication

The research paper was submitted to arXiv on June 23, 2025, with the identifier 2506.18902. The authors also introduce Jina-VDR, a novel benchmark specifically designed for visually rich image retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da63820c-3031-4844-89ee-acc9187cb460",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "b3f5e8fa-4162-477e-8139-9b87c1f2714f",
  "sourceToolAssistantUUID": "da63820c-3031-4844-89ee-acc9187cb460",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-30T06:14:25.775Z_

<details><summary>↩ Tool result · `toolu_01Ba4t2Xn2iALcmwX9zsEuPy`</summary>

```text
Web search results for query: "ViDoRAG visual document retrieval augmented generation 2025"

Links: [{"title":"ViDoRAG: Visual Document Retrieval-Augmented ...","url":"https://aclanthology.org/2025.emnlp-main.464.pdf"},{"title":"GitHub - Alibaba-NLP/ViDoRAG: [EMNLP 2025] ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents · GitHub","url":"https://github.com/Alibaba-NLP/ViDoRAG"},{"title":"[2502.18017] ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://arxiv.org/abs/2502.18017"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.464/"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.18017v2"},{"title":"[2502.18017v1] ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://arxiv.org/abs/2502.18017v1"},{"title":"Paper page - ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://huggingface.co/papers/2502.18017"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://www.researchgate.net/publication/397420761_ViDoRAG_Visual_Document_Retrieval-Augmented_Generation_via_Dynamic_Iterative_Reasoning_Agents"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://arxiv.org/html/2502.18017v2"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://arxiv.org/pdf/2502.18017"}]

Based on the search results, here's information about ViDoRAG:

## Overview

ViDoRAG is a novel multi-agent RAG framework tailored for complex reasoning across visual documents. Researchers from Alibaba Group's Tongyi Lab developed ViDoRAG, a multi-agent framework for Retrieval-Augmented Generation (RAG) over large corpora of visually rich documents, alongside a new benchmark dataset called ViDoSeek.

## Key Features

ViDoRAG is a novel RAG framework that utilizes a multi-agent, actor-critic paradigm for iterative reasoning, enhancing the noise robustness of generation models. It introduces a GMM-based multi-modal hybrid retrieval strategy to effectively integrate visual and textual pipelines.

The framework incorporates an iterative agent workflow incorporating exploration, summarization, and reflection, providing a framework for investigating test-time scaling in RAG domains.

## Problem Addressed

Understanding information from visually rich documents remains a significant challenge for traditional Retrieval-Augmented Generation (RAG) methods. Existing benchmarks predominantly focus on image-based question answering (QA), overlooking the fundamental challenges of efficient retrieval, comprehension, and reasoning within dense visual documents.

## Performance & Dataset

ViDoRAG significantly outperforms strong baselines, achieving over 10% improvement, thus establishing a new state-of-the-art on ViDoSeek. The ViDoSeek benchmark is specifically designed for visually rich document retrieval-reason-answer, fully suited for evaluation of RAG within large document corpus.

The work was published at EMNLP 2025 and is available on GitHub and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f524b51e-e550-4366-8aa2-a9a6a453ffc8",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "fcb9c9d8-c14c-4726-af6f-7a66be95de07",
  "sourceToolAssistantUUID": "f524b51e-e550-4366-8aa2-a9a6a453ffc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-30T06:14:26.991Z_

<details><summary>↩ Tool result · `toolu_01YV6JT1kKxytoxHpDdnQG9G`</summary>

```text
Web search results for query: ""storage efficient" visual document retrieval patch embedding reduction 2025 2026 arxiv"

Links: [{"title":"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning","url":"https://arxiv.org/pdf/2509.23883"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1003/"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/pdf/2506.04997"},{"title":"[2506.04997] Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings","url":"https://arxiv.org/abs/2506.04997"},{"title":"[2509.23883] DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning","url":"https://arxiv.org/abs/2509.23883"},{"title":"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning","url":"https://arxiv.org/html/2509.23883"},{"title":"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings | Request PDF","url":"https://www.researchgate.net/publication/394269833_Towards_Storage-Efficient_Visual_Document_Retrieval_An_Empirical_Study_on_Reducing_Patch-Level_Embeddings"},{"title":"Structural Anchor Pruning: Training-Free Multi-Vector Compression for Visual Document Retrieval","url":"https://arxiv.org/html/2601.20107"}]

I found several highly relevant papers on this topic. Here are the key research works on storage-efficient visual document retrieval with patch embedding reduction from 2025-2026:

## Main Papers Found:

### 1. DocPruner (September 2025)
DocPruner is the first framework to employ adaptive pruning in visual document retrieval to alleviate storage overhead, using patch-level attention score distribution within documents to perform adaptive pruning of patch embeddings. The framework achieves a 50-60% reduction in patch embeddings for state-of-the-art multi-vector models with negligible performance degradation.

### 2. Towards Storage-Efficient Visual Document Retrieval (June 2025)
This work establishes Light-ColPali/ColQwen2 as a baseline for patch-level embedding reduction in VDR systems, demonstrating comparable performance while achieving orders-of-magnitude reduction in patch storage requirements across three benchmarks. The approach retains 98.2% of NDCG@5 scores with only 11.8% of original memory footprint and maintains 94.6% effectiveness at just 2.8% memory footprint.

### 3. Structural Anchor Pruning (2026)
A 2026 paper by Yan et al. titled "Sculpting the vector space: towards efficient multi-vector visual document retrieval via prune-then-merge framework" addresses efficient multi-vector visual document retrieval.

These papers address the critical challenge that storing hundreds or even thousands of embedding vectors for every single document page makes large-scale deployment costly and challenging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e60ee4b3-1524-4c5e-81d7-af8fcd11c908",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "eb4c9210-bf41-4c4d-ae4a-63ed637bc0fc",
  "sourceToolAssistantUUID": "e60ee4b3-1524-4c5e-81d7-af8fcd11c908",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-30T06:14:29.250Z_

Let me fetch the remaining paper abstracts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb4c9210-bf41-4c4d-ae4a-63ed637bc0fc",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ecc258a-7d28-449a-84d2-67a95a4799c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3014,
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

_source line 47 · 2026-05-30T06:14:30.278Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UcXKEDSTBkAXqMqLiBqgZS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.18017",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ecc258a-7d28-449a-84d2-67a95a4799c5",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1825a26e-7bb3-434e-b523-5c5b63c6842d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3014,
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

_source line 48 · 2026-05-30T06:14:31.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C5Y8ZAz9wF6B3ttUhV58HA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18902",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1825a26e-7bb3-434e-b523-5c5b63c6842d",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd104339-007d-424f-b5a7-64ffd88c25f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3014,
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

_source line 49 · 2026-05-30T06:14:31.597Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F5kCsxSR97g7YY5zk87FAU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23883",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd104339-007d-424f-b5a7-64ffd88c25f6",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "030c1f47-91e0-4e39-a3e4-75e1df79fbb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3014,
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

_source line 50 · 2026-05-30T06:14:32.092Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PxvtBbwKVuemVAobNXB1Ws`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.04997",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "030c1f47-91e0-4e39-a3e4-75e1df79fbb9",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d360dd48-74e5-4e2d-98e7-173ebd00c379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3014,
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

_source line 51 · 2026-05-30T06:14:32.671Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Q54ZCCNv3raZYe8rQqBFn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20107",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d360dd48-74e5-4e2d-98e7-173ebd00c379",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG8jGnEQ1bAQA9DcfAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "118cceaa-8009-4975-a29d-1b8183b8cf3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185nREf8DACiBb6jC91zfsr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 18219,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 18219,
          "cache_creation_input_tokens": 3014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3014,
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

_source line 52 · 2026-05-30T06:14:35.002Z_

<details><summary>↩ Tool result · `toolu_01UcXKEDSTBkAXqMqLiBqgZS`</summary>

```text
# Paper Information

**Full Title:**
"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents"

**Authors:**
Qiuchen Wang, Ruixue Ding, Zehui Chen, Weiqi Wu, Shihang Wang, Pengjun Xie, Feng Zhao

**Submission Date:**
February 25, 2025 (v1); revised June 3, 2025 (v2)

**Abstract:**
The paper addresses challenges in understanding visually rich documents through traditional retrieval-augmented generation methods. The authors introduce ViDoSeek, a benchmark dataset for evaluating performance on complex visual document reasoning tasks. They identify limitations in current approaches—particularly weak integration of textual and visual features, plus insufficient reasoning capacity. To overcome these issues, they propose ViDoRAG, employing a "Gaussian Mixture Model (GMM)-based hybrid strategy to effectively handle multi-modal retrieval" alongside an iterative agent workflow emphasizing exploration, summarization, and reflection. The framework demonstrates over 10% performance improvement on their ViDoSeek benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1825a26e-7bb3-434e-b523-5c5b63c6842d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "b3ca3c28-2233-443c-8155-3798cded930d",
  "sourceToolAssistantUUID": "1825a26e-7bb3-434e-b523-5c5b63c6842d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-30T06:14:35.523Z_

<details><summary>↩ Tool result · `toolu_01F5kCsxSR97g7YY5zk87FAU`</summary>

```text
# DocPruner Research Paper Details

**Full Title:**
"DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning"

**Authors:**
Yibo Yan, Guangwei Xu, Xin Zou, Shuliang Liu, James Kwok, and Xuming Hu

**Submission Date:**
September 28, 2025

**Complete Abstract:**
The paper addresses storage challenges in visual document retrieval by introducing DocPruner, which employs "adaptive patch-level embedding pruning for VDR to effectively reduce the storage overhead." The framework leverages "intra-document patch attention distribution to dynamically identify and discard redundant embeddings for each document." Key findings include achieving "a significant 50-60% reduction in storage for leading multi-vector VDR models with negligible degradation in document retrieval performance." The authors validate their approach "across more than ten representative datasets" to demonstrate it provides "a robust, flexible, and effective solution for building storage-efficient, large-scale VDR systems."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "030c1f47-91e0-4e39-a3e4-75e1df79fbb9",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "9318af79-e49f-4fde-93b4-ec1a901db5c2",
  "sourceToolAssistantUUID": "030c1f47-91e0-4e39-a3e4-75e1df79fbb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-30T06:14:35.824Z_

<details><summary>↩ Tool result · `toolu_01C5Y8ZAz9wF6B3ttUhV58HA`</summary>

```text
# Paper Information

**Full Title:** "jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval"

**Authors:** Michael Günther, Saba Sturua, Mohammad Kalim Akram, Isabelle Mohr, Andrei Ungureanu, Bo Wang, Sedigheh Eslami, Scott Martens, Maximilian Werk, Nan Wang, and Han Xiao

**Submission Date:** June 23, 2025 (last revised July 7, 2025)

**Abstract:** The research introduces a 3.8 billion parameter model that "unifies text and image representations through a novel architecture supporting both single-vector and multi-vector embeddings in the late interaction style." The system incorporates task-specific adapters to optimize performance across retrieval scenarios including query-document matching, semantic similarity assessment, and code search. The work achieves strong results on cross-modal tasks and demonstrates particular capability with "visually rich content such as tables, charts, diagrams, and mixed-media formats." The authors also present a new benchmark called Jina-VDR designed for evaluating image retrieval of visually rich materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd104339-007d-424f-b5a7-64ffd88c25f6",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "88ce4aab-9d61-4231-8a75-fc92006ebe65",
  "sourceToolAssistantUUID": "cd104339-007d-424f-b5a7-64ffd88c25f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-30T06:14:36.935Z_

<details><summary>↩ Tool result · `toolu_014Q54ZCCNv3raZYe8rQqBFn`</summary>

```text
# Paper Information

**Full Title:**
"Structural Anchor Pruning: Training-Free Multi-Vector Compression for Visual Document Retrieval"

**Authors:**
- Zhuchenyang Liu
- Ziyu Hu
- Yao Zhang
- Yu Xiao

**Submission Date:**
January 27, 2026 (v1); Last revised May 21, 2026 (v2)

**Abstract:**
The paper addresses storage inefficiencies in Vision-Language Models used for document retrieval. The authors introduce SAP, a framework that achieves "over 90% of NDCG@5 while pruning more than 90% of visual tokens, without any per-model parameter tuning." The method operates through three components: a diagnostic tool for compression assessment, an automated window selection procedure, and a visual centrality scorer. A key finding reveals an "Alignment-Aggregation Divergence" where intermediate layers preserve document structure effectively, but final layers reshape this into a sparse, query-aligned form unsuitable for pruning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "118cceaa-8009-4975-a29d-1b8183b8cf3b",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "1a35ccf6-51c9-4963-a55b-36a91eb19bf7",
  "sourceToolAssistantUUID": "118cceaa-8009-4975-a29d-1b8183b8cf3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-30T06:14:37.452Z_

<details><summary>↩ Tool result · `toolu_01PxvtBbwKVuemVAobNXB1Ws`</summary>

```text
# Research Paper Summary

**Full Title:**
"Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings"

**Authors:**
Yubo Ma, Jinsong Li, Yuhang Zang, Xiaobao Wu, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Haodong Duan, Jiaqi Wang, Yixin Cao, Aixin Sun

**Submission Date:**
June 5, 2025

**Complete Abstract:**
The research addresses memory constraints in visual document retrieval systems. While ColPali/ColQwen2 models demonstrate strong performance, they generate numerous patch-level embeddings per page, creating significant storage demands. This study examines techniques for reducing these embeddings with minimal performance loss.

The authors tested two reduction approaches: token pruning and token merging. Surprisingly, "a simple random strategy outperforms other sophisticated pruning methods," though results remained suboptimal. The team determined that pruning lacks suitability for this task since it "requires removing certain page embeddings without query-specific information."

Token merging proved more promising. After optimizing across multiple dimensions, they developed Light-ColPali/ColQwen2, achieving "98.2% of retrieval performance with only 11.8% of original memory usage" and maintaining "94.6% effectiveness at 2.8% memory footprint."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d360dd48-74e5-4e2d-98e7-173ebd00c379",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "935547b1-729e-4135-ac8b-f64afb8f285f",
  "sourceToolAssistantUUID": "d360dd48-74e5-4e2d-98e7-173ebd00c379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-30T06:14:39.865Z_

Now let me do one more round of searches to find any additional relevant papers I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "935547b1-729e-4135-ac8b-f64afb8f285f",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG9VteGsU1UtXFvKLey",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17eceb02-327b-483e-9d8b-2b1909d72a79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQvNQempNDAAXu41unbh9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 1644,
      "cache_read_input_tokens": 21233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1644,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 58 · 2026-05-30T06:14:40.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgJD5kSWQdmoH241GmutNG`</summary>

```json
{
  "query": "DSE document screenshot embedding retrieval 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17eceb02-327b-483e-9d8b-2b1909d72a79",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG9VteGsU1UtXFvKLey",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b6b9a8-21b6-4fec-b202-96ff2a9c82ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQvNQempNDAAXu41unbh9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 1644,
      "cache_read_input_tokens": 21233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1644,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 59 · 2026-05-30T06:14:41.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VNmJYHCCRcfEidvr9yRQ5J`</summary>

```json
{
  "query": "BiPali BM25 ColPali visual document retrieval multi-vector 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b6b9a8-21b6-4fec-b202-96ff2a9c82ba",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYG9VteGsU1UtXFvKLey",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc3b3faf-0a84-43b2-af4c-0cff783bcfe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQvNQempNDAAXu41unbh9N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 1644,
      "cache_read_input_tokens": 21233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1644,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 60 · 2026-05-30T06:14:47.554Z_

<details><summary>↩ Tool result · `toolu_01SgJD5kSWQdmoH241GmutNG`</summary>

```text
Web search results for query: "DSE document screenshot embedding retrieval 2025 arxiv"

Links: [{"title":"[2406.11251] Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/abs/2406.11251"},{"title":"Document Screenshot Embedding for Retrieval","url":"https://www.emergentmind.com/papers/2406.11251"},{"title":"Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/pdf/2406.11251"},{"title":"Unifying Multimodal Retrieval via Document Screenshot Embedding","url":"https://arxiv.org/html/2406.11251v1"},{"title":"[2501.16902] Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/abs/2501.16902"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/html/2501.16902"},{"title":"Papers Explained 313: Document Screenshot Embedding | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-313-document-screenshot-embedding-792cb286643c"},{"title":"Xueguang Ma on X: \"Introducing Document Screenshot Embedding (DSE): a new retrieval paradigm that unifies various formats and modalities into a single form for direct document encoding. paper: https://t.co/wLptH9zzOr work done with amazing co-authors: @jacklin_64 @alexlimh23 @WenhuChen @lintool https://t.co/uVtnHzx7fv\" / X","url":"https://x.com/xueguang_ma/status/1803093148589318508"},{"title":"Unifying Multimodal Retrieval via Document Screenshot Embedding | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unifying-multimodal-retrieval-via-document-screenshot-embedding"}]

Based on the search results, here's what I found about DSE document screenshot embedding retrieval on arXiv:

## Document Screenshot Embedding (DSE)

Document Screenshot Embedding (DSE) is a novel retrieval paradigm that regards document screenshots as a unified input format, which does not require any content extraction preprocess and preserves all the information in a document (e.g., text, image and layout). DSE leverages a large vision-language model to directly encode document screenshots into dense representations for retrieval.

### Key Features

The approach differs from traditional methods by avoiding the need for tailored document parsing techniques and content extraction modules, which is tedious, prone to errors, and has information loss.

### Performance and Evaluation

To evaluate the method, researchers crafted the Wiki-SS dataset, a 1.3M Wikipedia web page screenshots as the corpus to answer questions from the Natural Questions dataset. The results showed strong performance: DSE outperforms BM25 by 17 points in top-1 retrieval accuracy, and in a mixed-modality task of slide retrieval, DSE significantly outperforms OCR text retrieval methods by over 15 points in nDCG@10.

### Paper Details

The original paper (arXiv:2406.11251) was published in June 2024 by researchers at the University of Waterloo and has been updated as recently as December 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11b6b9a8-21b6-4fec-b202-96ff2a9c82ba",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "ce1be2d3-6f83-4cb6-bf4a-f542cc860b6f",
  "sourceToolAssistantUUID": "11b6b9a8-21b6-4fec-b202-96ff2a9c82ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-30T06:14:48.122Z_

<details><summary>↩ Tool result · `toolu_01VNmJYHCCRcfEidvr9yRQ5J`</summary>

```text
Web search results for query: "BiPali BM25 ColPali visual document retrieval multi-vector 2025 2026 arxiv"

Links: [{"title":"ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/html/2407.01449v5"},{"title":"[PDF] ColPali: Efficient Document Retrieval with Vision Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ColPali:-Efficient-Document-Retrieval-with-Vision-Faysse-Sibille/c948e2d00ac2628ed4098a009c67c81ea4cc00a2"},{"title":"Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations","url":"https://arxiv.org/pdf/2603.01666"},{"title":"Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/pdf/2407.01449"},{"title":"[2407.01449] ColPali: Efficient Document Retrieval with Vision Language Models","url":"https://arxiv.org/abs/2407.01449"},{"title":"ColPali: EFFICIENT DOCUMENT RETRIEVAL WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf"},{"title":"Hierarchical Patch Compression for ColPali: Efficient Multi-Vector Document Retrieval with Dynamic Pruning and Quantization","url":"https://arxiv.org/html/2506.21601v1"},{"title":"Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction","url":"https://arxiv.org/html/2505.07730v1"}]

Based on the search results, here's what I found about these topics:

## ColPali: Efficient Document Retrieval with Vision Language Models

ColPali is a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines, while modern retrieval systems mainly rely on textual information extracted from document pages to index documents, causing them to struggle with key visual cues.

## BiPali vs ColPali: Multi-Vector Approach

ColPali leverages the ColBERT strategy to construct one embedding per image patch token and at inference computes all interactions between text tokens and image patches, resulting in a step-change improvement in performance compared to BiPali. The original study shows that incorporating multi-vector settings yields a significant performance boost compared to the single-vector baseline bi-encoder, BiPali.

## Related Research

The multi-vector paradigm was successfully adapted for multimodal retrieval by ColPali, shifting focus to visual documents, but despite their superior performance, these models face efficiency bottlenecks from the prohibitive storage cost of patch-level embeddings. Recent follow-up work includes HPC-ColPali, a Hierarchical Patch Compression framework that enhances the efficiency of ColPali while preserving its retrieval accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc3b3faf-0a84-43b2-af4c-0cff783bcfe5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "3dc16766-d519-4490-8440-16dfeff7d15d",
  "sourceToolAssistantUUID": "bc3b3faf-0a84-43b2-af4c-0cff783bcfe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-30T06:14:51.169Z_

Let me fetch one more paper that appeared in the results -- the "Beyond the Grid" paper that seems relevant and new.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc16766-d519-4490-8440-16dfeff7d15d",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGAHa1FEUUoSGF9pWX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f8b4dd3-d4d0-4779-a822-3fe36653c4fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBe2vo8wmS4QKAdyt4zuRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 22877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2077,
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

_source line 63 · 2026-05-30T06:14:52.192Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QuN2WVTLWaBktf7X79F57G`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.01666",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f8b4dd3-d4d0-4779-a822-3fe36653c4fd",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGAHa1FEUUoSGF9pWX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ade0f7ed-85a1-45c7-b89f-1b0e4552bd43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBe2vo8wmS4QKAdyt4zuRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 22877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2077,
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

_source line 64 · 2026-05-30T06:14:53.117Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018oDUme8CEuZxMx6XPzjxEC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.16902",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade0f7ed-85a1-45c7-b89f-1b0e4552bd43",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGAHa1FEUUoSGF9pWX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c0c25c9-5608-40ed-b03a-9265a1d9059a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBe2vo8wmS4QKAdyt4zuRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 22877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2077,
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

_source line 65 · 2026-05-30T06:14:53.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011v4L9eSkkjRd41vz7KvKMY`</summary>

```json
{
  "query": "ColBERT visual retrieval multimodal reranking document 2025 2026 arxiv new model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c0c25c9-5608-40ed-b03a-9265a1d9059a",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGAHa1FEUUoSGF9pWX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91c0c210-4bc4-4f46-8c53-785f1c9bafe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBe2vo8wmS4QKAdyt4zuRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 22877,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 22877,
          "cache_creation_input_tokens": 2077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2077,
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

_source line 66 · 2026-05-30T06:14:55.866Z_

<details><summary>↩ Tool result · `toolu_01QuN2WVTLWaBktf7X79F57G`</summary>

```text
# Paper Information

**Full Title:**
"Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations"

**Authors:**
Yibo Yan, Mingdong Ou, Yi Cao, Xin Zou, Shuliang Liu, Jiahao Huo, Yu Huang, James Kwok, Xuming Hu

**Submission Date:**
March 2, 2026

**Abstract:**
The researchers present ColParse, a method addressing storage challenges in Visual Document Retrieval. Their approach leverages document parsing to create "layout-informed sub-image embeddings" combined with page-level vectors. According to the abstract, this achieves "storage requirements by over 95%" reduction while improving performance across benchmarks. The system aims to reconcile fine-grained multi-vector retrieval accuracy with practical deployment constraints for large-scale multimodal information systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ade0f7ed-85a1-45c7-b89f-1b0e4552bd43",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "ecd489bb-dcfc-4caf-8ab4-bddd6b2123c2",
  "sourceToolAssistantUUID": "ade0f7ed-85a1-45c7-b89f-1b0e4552bd43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-30T06:14:57.129Z_

<details><summary>↩ Tool result · `toolu_018oDUme8CEuZxMx6XPzjxEC`</summary>

```text
# Paper Details

**Title:** "Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks"

**Authors:** Shengyao Zhuang, Ekaterina Khramtsova, Xueguang Ma, Bevan Koopman, Jimmy Lin, Guido Zuccon

**Submission Date:** January 28, 2025

**Abstract:**
The research examines how vision-language model-based retrievers (such as DSE and ColPali) that use document screenshots can be compromised. The team developed three pixel poisoning attack methods and found that "injecting even a single adversarial screenshot into the retrieval corpus can significantly disrupt search results, poisoning the top-10 retrieved documents for 41.9% of queries in the case of DSE and 26.4% for ColPali." These vulnerability rates exceed those found in text-only retriever systems. When attacks target specific known queries, success rates increase substantially. The findings demonstrate concerning security gaps in deploying vision-language models for document retrieval tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c0c25c9-5608-40ed-b03a-9265a1d9059a",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "0f023403-7631-4168-95be-61f2018b4c69",
  "sourceToolAssistantUUID": "6c0c25c9-5608-40ed-b03a-9265a1d9059a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-30T06:15:00.472Z_

<details><summary>↩ Tool result · `toolu_011v4L9eSkkjRd41vz7KvKMY`</summary>

```text
Web search results for query: "ColBERT visual retrieval multimodal reranking document 2025 2026 arxiv new model"

Links: [{"title":"Jina ColBERT v2: Multilingual Late Interaction Retriever for Embedding and Reranking","url":"https://jina.ai/news/jina-colbert-v2-multilingual-late-interaction-retriever-for-embedding-and-reranking/"},{"title":"ColBERT-Style Late Interaction Mechanism","url":"https://www.emergentmind.com/topics/colbert-style-late-interaction-mechanism"},{"title":"An Overview of Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen | Weaviate","url":"https://weaviate.io/blog/late-interaction-overview"},{"title":"Working with ColBERT - FastEmbed","url":"https://qdrant.tech/documentation/fastembed/fastembed-colbert/"},{"title":"Multimodal Reranking for Knowledge-Intensive Visual Question Answering","url":"https://arxiv.org/pdf/2407.12277"}]

I found some relevant results about ColBERT and multimodal retrieval developments. Here's what I discovered:

## Recent ColBERT Developments

Jina ColBERT v2 is an advanced late interaction retrieval model that improves performance of jina-colbert-v1-en and adds multilingual support and dynamic output dimensions. Jina ColBERT v2 supports 89 languages with superior retrieval performance, user-controlled output dimensions, and 8192 token-length.

## Multimodal Extensions

The ColBERT architecture has been extended to visual document retrieval. Video-ColBERT and ColPali adapt late interaction to video and visual document retrieval, aligning text tokens with spatial/temporal or visual patch embeddings—markedly improving recall and nDCG in multimodal benchmarks.

ColPali and ColQwen extend ColBERT's concept to visual content by treating the entire PDF as an image, rather than requiring Optical Character Recognition (OCR) and advanced chunking to separate different content formats.

## Multimodal Reranking

Multimodal reranking has shown importance in knowledge-intensive tasks, using multi-modal question and knowledge items to obtain relevance scores.

These developments represent significant advances in adapting ColBERT's late interaction mechanism to multimodal retrieval scenarios in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91c0c210-4bc4-4f46-8c53-785f1c9bafe5",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "ed6a1713-ac78-4f7c-bdd1-04b26e590573",
  "sourceToolAssistantUUID": "91c0c210-4bc4-4f46-8c53-785f1c9bafe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-30T06:15:03.470Z_

The "Beyond the Grid" paper is ColParse which is in the seed list. Let me check for a few more novel papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed6a1713-ac78-4f7c-bdd1-04b26e590573",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGBCJXrT5ZKtrCCSbSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95f516d7-6590-44bc-bcdd-e40251105d1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7UxroSf4kTc2jn6Xp6nDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1401,
      "cache_read_input_tokens": 24954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1401,
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

_source line 70 · 2026-05-30T06:15:04.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L3ND8mB3nYrcnHQWozXwXL`</summary>

```json
{
  "query": "VisRAG visual retrieval augmented generation page-level 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95f516d7-6590-44bc-bcdd-e40251105d1f",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGBCJXrT5ZKtrCCSbSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3995767-5916-4ae5-a132-0572a7161d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7UxroSf4kTc2jn6Xp6nDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1401,
      "cache_read_input_tokens": 24954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1401,
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

_source line 71 · 2026-05-30T06:15:04.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9qfPCxjL9K8dnso8DR8Pj`</summary>

```json
{
  "query": "MMLongBench multi-modal long document benchmark retrieval 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3995767-5916-4ae5-a132-0572a7161d4d",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGBCJXrT5ZKtrCCSbSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d37952-4cd1-4465-933f-5fcb593d56d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7UxroSf4kTc2jn6Xp6nDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1401,
      "cache_read_input_tokens": 24954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1401,
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

_source line 72 · 2026-05-30T06:15:11.043Z_

<details><summary>↩ Tool result · `toolu_01L3ND8mB3nYrcnHQWozXwXL`</summary>

```text
Web search results for query: "VisRAG visual retrieval augmented generation page-level 2024 2025 arxiv"

Links: [{"title":"[2410.10594] VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents","url":"https://arxiv.org/abs/2410.10594"},{"title":"[PDF] VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/VisRAG:-Vision-based-Retrieval-augmented-Generation-Yu-Tang/d9052dd87959e6076baf35e8f7ee87d568a32b58"},{"title":"VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning","url":"https://arxiv.org/html/2604.09508"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents","url":"https://www.rohan-paul.com/p/visrag-vision-based-retrieval-augmented"},{"title":"VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.09733"},{"title":"VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2510.09733"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241010594Y/abstract"},{"title":"VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality   Documents","url":"https://arxiv.org/pdf/2410.10594"},{"title":"VISRAG: VISION-BASED RETRIEVAL-AUGMENTED ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf"},{"title":"ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents","url":"https://arxiv.org/html/2502.18017v2"}]

Based on the search results, I found relevant information about VisRAG and related visual retrieval-augmented generation research:

## VisRAG: Vision-based Retrieval-Augmented Generation

The original VisRAG paper was first submitted on October 14, 2024, with an updated version on March 2, 2025, with the arxiv identifier 2410.10594. VisRAG retrieves document page snapshots as units, preserving visual and spatial cues so VLMs can read evidence directly from images.

VisRAG eliminates document parsing, preserving visual and layout information, addressing the limitation that traditional RAG systems rely on text-based processing, limiting their ability to handle multi-modal documents effectively.

## VisRAG 2.0

There's also a newer version: VisRAG 2.0 is titled "evidence-guided multi-image reasoning in visual retrieval-augmented generation" and has arxiv identifier 2510.09733. EVisRAG introduces evidence-based reasoning over multiple retrieved images, explicitly extracting and structuring evidence from each retrieved page to support multi-image understanding.

These papers represent recent advances in applying vision-based approaches to retrieval-augmented generation on documents with complex layouts and multi-modal content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3995767-5916-4ae5-a132-0572a7161d4d",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "3aefa820-49e4-4496-af31-f492185ea194",
  "sourceToolAssistantUUID": "e3995767-5916-4ae5-a132-0572a7161d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-30T06:15:14.638Z_

<details><summary>↩ Tool result · `toolu_01V9qfPCxjL9K8dnso8DR8Pj`</summary>

```text
Web search results for query: "MMLongBench multi-modal long document benchmark retrieval 2025 arxiv"

Links: [{"title":"[PDF] MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MMLongBench-Doc:-Benchmarking-Long-context-Document-Ma-Zang/28f735d4f08b9cd04a46ce83fbb9ced0734f9bb3"},{"title":"Benchmarking Multi-Modal Retrieval for Long Documents","url":"https://arxiv.org/html/2501.08828v1"},{"title":"M-LongDoc: A Benchmark and Retrieval-Aware Tuning for Long Multimodal Document Understanding","url":"https://arxiv.org/html/2411.06176v1"},{"title":"MMDocIR: Benchmarking Multimodal Retrieval for Long Documents","url":"https://arxiv.org/html/2501.08828v3"},{"title":"GitHub - mayubo2333/MMLongBench-Doc: Official Repository of MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations · GitHub","url":"https://github.com/mayubo2333/MMLongBench-Doc"},{"title":"[2407.01523] MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations","url":"https://arxiv.org/abs/2407.01523"},{"title":"M-Longdoc: A Benchmark For Multimodal Super-Long Document Understanding   And A Retrieval-Aware Tuning Framework","url":"https://arxiv.org/pdf/2411.06176"}]

Based on the search results, I found relevant information about multi-modal long document benchmarks from 2025. Here's what the search revealed:

## Key Findings

**MMLongBench-Doc:**
MMLongBench-Doc is a long-context, multi-modal benchmark comprising 1,062 expert-annotated questions. 33.2% of the questions are cross-page questions requiring evidence across multiple pages.

**MMDocIR - A Related 2025 Benchmark:**
MMDocIR comprises 313 lengthy documents across 10 different domains, along with 1,685 questions. This is a newer benchmark specifically focused on multi-modal document retrieval.

**Content Analysis:**
Analysis of the MMLongBench-Doc benchmark shows that text occupies only 52.7% of content area, while images and tables account for 29.2% and 12.8% respectively.

**Purpose and Challenge:**
Experiments on 14 LVLMs demonstrate that long-context document understanding greatly challenges current models, and validate the necessity of future research toward more capable long-context LVLMs.

These benchmarks are designed to evaluate how well large vision-language models can handle complex, multi-page documents that combine text with visual elements like images, tables, and charts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d37952-4cd1-4465-933f-5fcb593d56d1",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "5a4f18d1-07b7-452a-be10-f39b8051227e",
  "sourceToolAssistantUUID": "90d37952-4cd1-4465-933f-5fcb593d56d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-30T06:15:19.324Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qn7D79n3EWoXZxF2J18oCG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.09733",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a4f18d1-07b7-452a-be10-f39b8051227e",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGCFBCHNUH8EWX3QcR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d02b85ec-60a1-4e12-91c4-3c93fa6070bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtrkH6jsvU5eMWvUYaMmkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 26355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1858,
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

_source line 75 · 2026-05-30T06:15:19.973Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gr3aUhNMARuojwDjC7dWAc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.16902",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. I want a complete list of all authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02b85ec-60a1-4e12-91c4-3c93fa6070bb",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGCFBCHNUH8EWX3QcR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18d23cf7-9aeb-4cf5-ae8e-d04f3290cd49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtrkH6jsvU5eMWvUYaMmkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 26355,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 26355,
          "cache_creation_input_tokens": 1858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1858,
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

_source line 76 · 2026-05-30T06:15:23.512Z_

<details><summary>↩ Tool result · `toolu_01Qn7D79n3EWoXZxF2J18oCG`</summary>

```text
# Paper Information

**Full Title:**
"VisRAG 2.0: Evidence-Guided Multi-Image Reasoning in Visual Retrieval-Augmented Generation"

**Authors:**
Yubo Sun, Chunyi Peng, Yukun Yan, Shi Yu, Zhenghao Liu, Chi Chen, Zhiyuan Liu, Maosong Sun

**Submission Date:**
October 10, 2025

**Abstract:**
The researchers describe a framework that addresses limitations in current visual retrieval-augmented generation systems. Their approach, called EVisRAG, enables models to "learns to reason with evidence-guided multi-image" processing. The system observes retrieved images, documents per-image evidence, then formulates answers from aggregated evidence. They introduce a training method called RS-GRPO that links specific rewards to targeted tokens, optimizing both visual perception and reasoning in vision-language models. Testing shows "27% improvements on average" over baseline models across multiple visual question-answering benchmarks, with the system accurately identifying and locating question-relevant evidence across images.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d02b85ec-60a1-4e12-91c4-3c93fa6070bb",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "af839061-9e8d-43b4-9360-d4122c6088ca",
  "sourceToolAssistantUUID": "d02b85ec-60a1-4e12-91c4-3c93fa6070bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-30T06:15:24.154Z_

<details><summary>↩ Tool result · `toolu_01Gr3aUhNMARuojwDjC7dWAc`</summary>

```text
# Paper Information

**Full Title:**
"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks"

**Authors:**
1. Shengyao Zhuang
2. Ekaterina Khramtsova
3. Xueguang Ma
4. Bevan Koopman
5. Jimmy Lin
6. Guido Zuccon

**Submission Date:**
Tuesday, 28 January 2025

**Abstract:**
The research reveals that vision-language model-based document retrievers face significant vulnerabilities. As stated in the paper, "injecting even a single adversarial screenshot into the retrieval corpus can significantly disrupt search results, poisoning the top-10 retrieved documents for 41.9% of queries in the case of DSE and 26.4% for ColPali." The study proposes three pixel poisoning attack methods targeting systems like DSE and ColPali, demonstrating that these attacks prove more effective against vision-based systems compared to traditional text-only retrieval methods. The findings underscore potential security risks in deploying vision-language models for information retrieval tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18d23cf7-9aeb-4cf5-ae8e-d04f3290cd49",
  "isSidechain": true,
  "promptId": "66266847-3f6c-4ee1-b0d1-4e1e8d8d60ae",
  "agentId": "afed2bc46f8f98e40",
  "type": "user",
  "uuid": "92d6e515-c741-415b-a407-4bdecf9fba06",
  "sourceToolAssistantUUID": "18d23cf7-9aeb-4cf5-ae8e-d04f3290cd49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-30T06:16:42.464Z_

Now I have a comprehensive set of papers. Let me compile the final report, filtering out the seed list papers (ColPali, MMDocIR, Snappy, AGREE, ColParse, MURE, ViDoRe V3, RegionGPT).

Here is the literature survey of recent papers (2024-2026) that build on or relate to ColPali's late-interaction visual document retrieval paradigm. All papers below are **not** in the seed list.

---

## 1. Nemotron ColEmbed V2

- **Title:** Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval
- **Authors:** Gabriel de Souza P. Moreira et al. (NVIDIA)
- **Venue/Date:** arXiv, February 3, 2026 (revised April 1, 2026)
- **URL:** https://arxiv.org/abs/2602.03992
- **What it does:** Presents a family of open-weights late-interaction embedding models (3B, 4B, 8B parameters) built on NVIDIA Eagle 2 and Qwen3-VL backbones for visual document retrieval. Uses cluster-based sampling, hard-negative mining, bidirectional attention, and model merging. The 8B model ranked #1 on the ViDoRe V3 leaderboard as of February 2026 with NDCG@10 of 63.42.
- **Why it's important:** Current state-of-the-art on the major VDR benchmark; demonstrates that scaling late-interaction models with better training recipes yields substantial gains. Open-weights release makes it a key community resource.

---

## 2. ModernVBERT

- **Title:** ModernVBERT: Towards Smaller Visual Document Retrievers
- **Authors:** Paul Teiletche, Quentin Mace, Max Conti, Antonio Loison, Gautier Viaud, Pierre Colombo, Manuel Faysse et al.
- **Venue/Date:** arXiv, October 1, 2025 (revised December 16, 2025)
- **URL:** https://arxiv.org/abs/2510.01149
- **What it does:** Challenges the assumption that generative VLMs are the best backbone for VDR. Through systematic analysis of attention masking, resolution, modality alignment, and contrastive objectives, they build a 250M-parameter encoder-only model that outperforms models up to 10x larger on document retrieval tasks, enabling CPU-based inference.
- **Why it's important:** Demonstrates that small, well-designed encoder models can beat large generative VLMs for retrieval, opening VDR to resource-constrained deployment. Co-authored by Manuel Faysse (ColPali first author).

---

## 3. HEAVEN (Hybrid-Vector Retrieval)

- **Title:** Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy
- **Authors:** Juyeon Kim, Geon Lee, Dongwon Choi, Taeuk Kim, Kijung Shin
- **Venue/Date:** arXiv, October 25, 2025 (revised April 20, 2026)
- **URL:** https://arxiv.org/abs/2510.22215
- **What it does:** Proposes HEAVEN, a plug-and-play two-stage framework that first screens candidates using single-vector embeddings of visually-summarized composite pages, then reranks with multi-vector late interaction using token filtering. Also introduces ViMDoc, a benchmark for visually-rich, multi-document, long-document retrieval.
- **Why it's important:** Achieves 99.87% of multi-vector Recall@1 while reducing per-query computation by 99.82%. Directly addresses the main practical bottleneck of ColPali-style models (compute cost at scale).

---

## 4. SERVAL

- **Title:** SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models
- **Authors:** Thong Nguyen, Yibin Lei, Jia-Huei Ju, Andrew Yates
- **Venue/Date:** arXiv, September 18, 2025
- **URL:** https://arxiv.org/abs/2509.15432
- **What it does:** Uses a VLM to generate detailed textual descriptions of document images, then embeds those descriptions with a standard text encoder -- achieving 63.4% nDCG@5 on ViDoRe-v2 in a zero-shot setting, outperforming specialized trained encoders. No contrastive training or fine-tuning required.
- **Why it's important:** Challenges the premise that specialized visual encoders are needed; shows that VLM-as-captioner plus text retrieval can be surprisingly competitive, establishing a strong zero-shot baseline for the field.

---

## 5. HPC-ColPali

- **Title:** Hierarchical Patch Compression for ColPali: Efficient Multi-Vector Document Retrieval with Dynamic Pruning and Quantization
- **Authors:** Duong Bach
- **Venue/Date:** arXiv, June 19, 2025 (revised July 2, 2025)
- **URL:** https://arxiv.org/abs/2506.21601
- **What it does:** Combines K-means quantization (compressing patch embeddings to 1-byte indices for up to 32x storage reduction), attention-guided dynamic pruning (60% compute reduction), and optional binary encoding. Achieves 30-50% lower query latency while preserving retrieval precision on ViDoRe and SEC-Filings datasets. In RAG applications, reduces hallucination by 30%.
- **Why it's important:** Directly attacks the storage/compute bottleneck of ColPali with a multi-pronged compression framework; practical impact for real-world deployment.

---

## 6. Light-ColPali/ColQwen2 (Storage-Efficient VDR)

- **Title:** Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings
- **Authors:** Yubo Ma, Jinsong Li, Yuhang Zang, Xiaobao Wu et al.
- **Venue/Date:** arXiv June 5, 2025; ACL 2025 Findings
- **URL:** https://arxiv.org/abs/2506.04997
- **What it does:** Systematically compares token pruning vs. token merging for reducing patch-level embeddings. Finds that random pruning surprisingly beats sophisticated methods, but token merging (via hierarchical agglomerative clustering) is far better. Light-ColPali/ColQwen2 retains 98.2% of retrieval performance at 11.8% memory, and 94.6% at only 2.8% memory.
- **Why it's important:** Published at ACL 2025 Findings; provides the first rigorous empirical study of embedding compression for ColPali-family models. The surprising finding about random pruning outperforming sophisticated methods has influenced subsequent work.

---

## 7. DocPruner

- **Title:** DocPruner: A Storage-Efficient Framework for Multi-Vector Visual Document Retrieval via Adaptive Patch-Level Embedding Pruning
- **Authors:** Yibo Yan, Guangwei Xu, Xin Zou, Shuliang Liu, James Kwok, Xuming Hu
- **Venue/Date:** arXiv, September 28, 2025
- **URL:** https://arxiv.org/abs/2509.23883
- **What it does:** Uses intra-document patch attention distributions to dynamically identify and discard redundant embeddings. Achieves 50-60% storage reduction for leading multi-vector VDR models with negligible performance degradation, validated across 10+ datasets.
- **Why it's important:** Complementary to Light-ColPali; uses attention-based signals rather than merging. Adaptive per-document pruning is more principled than fixed-ratio approaches.

---

## 8. SAP (Structural Anchor Pruning)

- **Title:** Structural Anchor Pruning: Training-Free Multi-Vector Compression for Visual Document Retrieval
- **Authors:** Zhuchenyang Liu, Ziyu Hu, Yao Zhang, Yu Xiao
- **Venue/Date:** arXiv, January 27, 2026 (revised May 21, 2026)
- **URL:** https://arxiv.org/abs/2601.20107
- **What it does:** A training-free compression framework that achieves over 90% of NDCG@5 while pruning more than 90% of visual tokens, without per-model parameter tuning. Discovers "Alignment-Aggregation Divergence" -- intermediate layers preserve document structure, but final layers reshape embeddings into a sparse query-aligned form unsuitable for pruning.
- **Why it's important:** The 90%+ pruning at 90%+ performance is striking. The theoretical insight about layer-wise behavior of VLM embeddings provides useful understanding for future model design.

---

## 9. Reproducibility Study of Visual Document Retrieval with Late Interaction

- **Title:** Reproducibility, Replicability, and Insights into Visual Document Retrieval with Late Interaction
- **Authors:** Jingfen Qiao, Jia-Huei Ju, Xinyu Ma, Evangelos Kanoulas, Andrew Yates
- **Venue/Date:** arXiv, May 12, 2025
- **URL:** https://arxiv.org/abs/2505.07730
- **What it does:** Reproduces and replicates ColPali-style VDR methods across multiple VLMs, evaluating late interaction's contribution, model adaptability to text inputs, and robustness on text-intensive datasets. Key finding: query tokens tend to match patches containing visually similar tokens or their surrounding patches, despite lacking explicit text alignment.
- **Why it's important:** Provides crucial mechanistic understanding of how late interaction actually works in visual retrieval (query-patch matching dynamics). Essential for the field's scientific foundation.

---

## 10. jina-embeddings-v4

- **Title:** jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval
- **Authors:** Michael Gunther, Saba Sturua, Mohammad Kalim Akram et al. (Jina AI)
- **Venue/Date:** arXiv, June 23, 2025 (revised July 7, 2025)
- **URL:** https://arxiv.org/abs/2506.18902
- **What it does:** A 3.8B parameter model that unifies text and image representations through a single architecture supporting both single-vector and multi-vector (late interaction) embeddings. Uses task-specific LoRA adapters for different retrieval scenarios. Introduces Jina-VDR, a new benchmark for visually rich document retrieval.
- **Why it's important:** Shows how the ColPali late-interaction paradigm can be unified into a general-purpose embedding model alongside single-vector and cross-modal capabilities. Industry-backed open model with strong adoption.

---

## Additional Papers of Interest (Bonus)

**11. Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks**
- Authors: Shengyao Zhuang et al. | arXiv January 28, 2025 | https://arxiv.org/abs/2501.16902
- Demonstrates adversarial attacks where a single poisoned screenshot disrupts 42% (DSE) / 26% (ColPali) of queries. Important for security considerations in deploying visual retrieval.

**12. ViDoRAG**
- Authors: Qiuchen Wang et al. | EMNLP 2025 | https://arxiv.org/abs/2502.18017
- Multi-agent RAG framework using GMM-based hybrid retrieval over visual documents with iterative reasoning. 10%+ improvement on their ViDoSeek benchmark. Important as a downstream application of visual retrieval.

**13. VisRAG 2.0**
- Authors: Yubo Sun et al. | arXiv October 10, 2025 | https://arxiv.org/abs/2510.09733
- Evidence-guided multi-image reasoning for visual RAG, with 27% average improvement over baselines. Advances the generation side of the visual retrieval pipeline.

**14. Unlocking Multimodal Document Intelligence (Survey)**
- Authors: Yibo Yan et al. | arXiv February 23, 2026 | https://arxiv.org/abs/2602.19961
- Comprehensive survey covering VDR benchmarks, methods (embedding + reranking), and integration with RAG/agentic systems. Useful as a reference map of the field.

**15. Lost in OCR Translation?**
- Authors: Alexander Most et al. | arXiv May 8, 2025 | https://arxiv.org/abs/2505.05666
- Comparative study of ColPali vs. OCR pipelines showing vision-based systems excel on in-distribution data but OCR generalizes better to low-quality unseen documents. Important for practitioners choosing between approaches.

**16. REAL-MM-RAG**
- Authors: Navve Wasserman et al. | arXiv February 17, 2025 | https://arxiv.org/abs/2502.12342
- Benchmark with multi-difficulty evaluation based on query rephrasing. Reveals model weaknesses on table-heavy documents. Provides improved training data for multi-modal RAG.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d6e515-c741-415b-a407-4bdecf9fba06",
  "isSidechain": true,
  "agentId": "afed2bc46f8f98e40",
  "requestId": "req_011CbYGCweXQFPQmpiXy1WPr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42123883-26e9-47b3-aa83-dbd1ad6c7994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4afdc2a4-1d8d-48cb-ae88-216f86fdb790",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wNcf6aUoga4FfZFdEqvg1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 28213,
      "output_tokens": 3291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 745
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3291,
          "cache_read_input_tokens": 28213,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 745,
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
