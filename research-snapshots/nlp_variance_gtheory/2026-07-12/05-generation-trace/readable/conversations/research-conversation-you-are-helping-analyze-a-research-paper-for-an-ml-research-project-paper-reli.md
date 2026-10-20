# Research conversation: You are helping analyze a research paper for an ML research project. Paper: "ReliabilityRAG: Effective and Provably Robu

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a620a8dbf50fd8bc7.jsonl`
- **Structured JSON:** [`2e261ca57fbd880336ba.json`](../../sessions/2e/2e261ca57fbd880336ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-30T06:27:40.157Z_

You are helping analyze a research paper for an ML research project.

Paper: "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search" by Zeyu Shen et al., NeurIPS 2025 (listed as from Princeton/USC group), https://arxiv.org/abs/2509.23519

Tasks:
1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2509.23519
2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2509.23519
3. Search for OpenReview reviews of this paper (try searching OpenReview for "ReliabilityRAG" or the title)
4. Search the web for any discussion/reviews

Provide a detailed summary covering:
- The exact problem/gap they identified (especially vs RobustRAG)
- Their key insight about document reliability and MIS computation
- Technical method details (graph construction, MIS algorithm, weighted sampling for long-form generation)
- Certified robustness guarantees — what exactly do they prove?
- Any reviewer praise/criticism if found
- Limitations they acknowledge

Be thorough and specific about the technical details. Report back everything you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "7b7ad4e8-cd58-4413-b770-3cf2ea3e43f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:27:40.160Z_

```json
{
  "parentUuid": "7b7ad4e8-cd58-4413-b770-3cf2ea3e43f0",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
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
  "uuid": "ff0ab371-4617-4cd2-8740-7da3d16291e2",
  "timestamp": "2026-05-30T06:27:40.160Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:27:40.160Z_

```json
{
  "parentUuid": "ff0ab371-4617-4cd2-8740-7da3d16291e2",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e4e154f1-da6d-41ad-9b0d-8917536ca488",
  "timestamp": "2026-05-30T06:27:40.160Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:27:42.953Z_



I'll start by fetching the tools I need, then gather information from multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4e154f1-da6d-41ad-9b0d-8917536ca488",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9CL5bAjmfzpLttZ2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebb38027-1eb4-4e79-bc2b-940ffc6c0002",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6P8MDDeZVaRXcHzbLuS6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1637,
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

_source line 5 · 2026-05-30T06:27:43.547Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B3RdxQsTQ71cV1Vf9opeKB`</summary>

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
  "parentUuid": "ebb38027-1eb4-4e79-bc2b-940ffc6c0002",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9CL5bAjmfzpLttZ2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d9701a1-8026-47b1-851c-c91ccfd85884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6P8MDDeZVaRXcHzbLuS6K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 7413,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1637
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1637,
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

_source line 6 · 2026-05-30T06:27:43.555Z_

<details><summary>↩ Tool result · `toolu_01B3RdxQsTQ71cV1Vf9opeKB`</summary>

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
  "parentUuid": "8d9701a1-8026-47b1-851c-c91ccfd85884",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "5b88a780-cd7b-4a4b-85c0-ed104486bd8e",
  "sourceToolAssistantUUID": "8d9701a1-8026-47b1-851c-c91ccfd85884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:27:47.386Z_



Now let me fetch information from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b88a780-cd7b-4a4b-85c0-ed104486bd8e",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9TBYdKq4p35hGu2Qh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a88ef677-fde7-451c-985a-e7c078b0acfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMihyvzjUiM8PibRznV6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 8 · 2026-05-30T06:27:49.404Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xguu1npvHRorWMAbJNHce9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23519",
  "prompt": "Extract everything from this arxiv page: the full title, all authors and affiliations, the complete abstract text, submission date, any categories/subjects, and any other metadata shown on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a88ef677-fde7-451c-985a-e7c078b0acfa",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9TBYdKq4p35hGu2Qh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeefd4a4-d743-4203-874f-dcf3479ab03f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMihyvzjUiM8PibRznV6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 9 · 2026-05-30T06:27:55.557Z_

<details><summary>↩ Tool result · `toolu_01Xguu1npvHRorWMAbJNHce9`</summary>

```text
# ReliabilityRAG Paper Metadata

**Full Title:** "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search"

**Authors:**
- Zeyu Shen
- Basileal Imana
- Tong Wu
- Chong Xiang
- Prateek Mittal
- Aleksandra Korolova

(No institutional affiliations are displayed on this page)

**Abstract Summary:**
The paper addresses vulnerabilities in Retrieval-Augmented Generation systems to attacks on retrieval corpora, such as prompt injection. The researchers propose a framework leveraging document reliability signals. They introduce two main contributions: first, a graph-theoretic algorithm finding Maximum Independent Sets to filter malicious documents while prioritizing reliability; second, a scalable weighted sample-and-aggregate approach for larger document sets. Results demonstrate superior robustness against adversarial attacks while maintaining accuracy in long-form generation tasks.

**Submission Details:**
- ArXiv ID: 2509.23519
- Initial Submission: September 27, 2025
- Latest Version: February 15, 2026 (v2)

**Categories:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

**Status:** Accepted to NeurIPS 2025

**DOI:** https://doi.org/10.48550/arXiv.2509.23519

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeefd4a4-d743-4203-874f-dcf3479ab03f",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "6e3e15db-e98e-40f7-a7fc-016cd7ec03c0",
  "sourceToolAssistantUUID": "eeefd4a4-d743-4203-874f-dcf3479ab03f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-30T06:27:56.996Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016yGc8okCGzobkCo8w6zpfs`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2509.23519",
  "prompt": "Extract the complete content of this research paper in full detail. I need:\n1. The full abstract\n2. The introduction - what problem they identify, what gap exists vs prior work (especially RobustRAG)\n3. Their key insight about document reliability and Maximum Independent Set (MIS)\n4. The complete technical method: graph construction, MIS algorithm details, how weighted sampling works for long-form generation\n5. Their certified robustness guarantees - what theorems do they prove? What are the exact formal statements?\n6. Experimental results - datasets, baselines, key numbers\n7. Limitations section\n8. Any discussion of computational complexity\n9. Related work discussion\nPlease be as thorough and technical as possible, preserving mathematical details and algorithm descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e3e15db-e98e-40f7-a7fc-016cd7ec03c0",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9TBYdKq4p35hGu2Qh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bc3b5a3-89c1-4b65-aad4-ceefc481aa4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMihyvzjUiM8PibRznV6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 11 · 2026-05-30T06:27:57.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PEWkeuRSHvz6QA65QfHRWv`</summary>

```json
{
  "query": "ReliabilityRAG \"Effective and Provably Robust Defense\" RAG web-search NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bc3b5a3-89c1-4b65-aad4-ceefc481aa4e",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9TBYdKq4p35hGu2Qh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "832bf6e3-4c9e-4039-8204-264a95375017",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMihyvzjUiM8PibRznV6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 12 · 2026-05-30T06:27:57.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114T9djh9y2D1oGtoe4tDs9`</summary>

```json
{
  "query": "OpenReview ReliabilityRAG reliability RAG robust defense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "832bf6e3-4c9e-4039-8204-264a95375017",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYH9TBYdKq4p35hGu2Qh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9287b32-5077-4347-9c91-a80ba0945e38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMihyvzjUiM8PibRznV6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 13 · 2026-05-30T06:28:04.128Z_

<details><summary>↩ Tool result · `toolu_01PEWkeuRSHvz6QA65QfHRWv`</summary>

```text
Web search results for query: "ReliabilityRAG "Effective and Provably Robust Defense" RAG web-search NeurIPS 2025"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...","url":"https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/pdf/2503.06950"}]

I found excellent results for your search! Here's what I found about ReliabilityRAG:

## Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The work was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## Key Contributions

The framework introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, and the MIS variant explicitly prioritizes higher-reliability documents while providing provable robustness guarantees against bounded adversarial corruption under natural assumptions.

Recognizing the computational cost of exact MIS for large retrieval sets, the second contribution is a scalable weighted sample and aggregate framework that explicitly utilizes reliability information while preserving some robustness guarantees and efficiently handling many documents.

## Performance Results

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

## Problem Context

RAG systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection, though RAG-based search systems like Google's Search AI Overview can benefit from built-in reliability signals like document ranking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "832bf6e3-4c9e-4039-8204-264a95375017",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "b126ac32-9f14-44d1-a6c3-b0fa06a5e747",
  "sourceToolAssistantUUID": "832bf6e3-4c9e-4039-8204-264a95375017",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-30T06:28:04.485Z_

<details><summary>↩ Tool result · `toolu_0114T9djh9y2D1oGtoe4tDs9`</summary>

```text
Web search results for query: "OpenReview ReliabilityRAG reliability RAG robust defense"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://openreview.net/pdf?id=D9JeNTs5Bu"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"Certifiably Robust RAG against Retrieval Corruption | OpenReview","url":"https://openreview.net/forum?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"}]

Based on the search results, I found information about ReliabilityRAG:

ReliabilityRAG is a novel framework designed to make RAG-based systems robust. It is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.

**Key Technical Approach:**

The framework includes a document-selection algorithm that identifies a "consistent majority" among retrieved documents by finding the Maximum Independent Set (MIS) on a "contradiction graph," where vertices represent the retrieved documents and edges connect pairs determined to be contradictory by a Natural Language Inference (NLI) model. The approach incorporates reliability signals from the retriever—whether in the form of document rank or explicit reliability scores—to guide more robust generation.

**Robustness Guarantees:**

The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. The second contribution is a scalable weighted sample and aggregate framework that explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.

**Performance:**

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9287b32-5077-4347-9c91-a80ba0945e38",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "94b98a7a-e3b7-47da-a621-c432e731c2da",
  "sourceToolAssistantUUID": "b9287b32-5077-4347-9c91-a80ba0945e38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-30T06:28:07.685Z_

<details><summary>↩ Tool result · `toolu_016yGc8okCGzobkCo8w6zpfs`</summary>

```text
# ReliabilityRAG: Summary of Key Technical Content

## Abstract & Problem Statement

The paper presents ReliabilityRAG, a defense mechanism for RAG-based web-search systems against poisoned or low-quality retrieved documents. The authors identify that existing RAG systems remain vulnerable to attacks where malicious documents are injected into search results or knowledge bases.

## Core Innovation: Document Reliability & Maximum Independent Set

The key insight involves modeling document selection as a graph problem. Rather than simply ranking documents, the method constructs a conflict graph where edges represent documents that contradict each other. The system then applies Maximum Independent Set (MIS) algorithms to select a subset of mutually non-contradictory documents, ensuring robustness against poisoning.

## Technical Method

**Graph Construction:** Documents are represented as nodes. The authors build edges between documents identified as contradictory using a learned pairwise classifier (based on NLI-style models). This creates an undirected graph capturing semantic conflicts.

**MIS Selection:** The MIS algorithm identifies the largest subset of documents with no internal conflicts. This selection inherently filters out adversarial documents that contradict benign ones, since poisoned content typically stands alone or clusters separately.

**Weighted Sampling for Generation:** For long-form answers, the method uses reliability-weighted sampling where document importance scores weight the selection probability during generation. This prevents any single unreliable source from dominating the output.

## Certified Robustness Guarantees

The paper provides formal robustness certificates under specific threat models. The theorems establish that under bounded poisoning (adversary can inject up to k malicious documents), the MIS-based selection guarantees inclusion of a minimum number of benign documents with high confidence.

Key theorem statements (paraphrased): Under k-poisoning attacks, the selected document set contains at least some guaranteed proportion of benign documents, with provable bounds on the contamination ratio.

## Experimental Results

**Datasets:** Testing on QA benchmarks (likely TriviaQA, NQ variants) and web-search scenarios.

**Baselines:** Comparisons against RobustRAG (prior defense), standard RAG, and retrieval-based systems without defense mechanisms.

**Key Findings:** ReliabilityRAG achieves superior performance when documents contain contradictions, with measurable improvements in answer accuracy even under adversarial poisoning. The method shows particular strength when malicious documents are semantically distinct from legitimate ones.

## Computational Considerations

Maximum Independent Set is NP-hard in general graphs. The paper likely discusses approximation algorithms or heuristic approaches (greedy selection, sampling-based methods) for practical scalability rather than exact solutions.

## Limitations

The approach depends on accurate contradiction detection via the pairwise classifier. Sophisticated adversaries crafting subtly contradictory content might evade this mechanism. The method's effectiveness degrades when poisoned documents are semantically similar to benign ones rather than overtly contradictory.

## Comparison to Prior Work

The paper distinguishes itself from RobustRAG by explicitly modeling document conflicts as graph structure rather than using scoring heuristics, providing theoretical guarantees rather than empirical robustness alone, and offering provably certified defense bounds under formal threat models.

[Binary content (application/pdf, 1.5MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/458a2eed-0834-465b-87af-c8668736149f/tool-results/webfetch-1780122477013-jr2v27.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bc3b5a3-89c1-4b65-aad4-ceefc481aa4e",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "a145df91-571e-4dfe-ad3b-417ccef79dba",
  "sourceToolAssistantUUID": "7bc3b5a3-89c1-4b65-aad4-ceefc481aa4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-30T06:28:12.640Z_

Good, I found the OpenReview link. Let me now fetch the OpenReview page for reviews, the PDF directly for deeper technical details, and search for additional discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a145df91-571e-4dfe-ad3b-417ccef79dba",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHBEDF4KMoV7pCBFj4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5985b2c1-a59f-4e8d-9fec-9c0f62980410",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxR3ToPeyXBEWWevr52e2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1527,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 10171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
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

_source line 17 · 2026-05-30T06:28:15.562Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0116JRCL6RZnogRd9fY3vZtm`</summary>

```json
{
  "url": "https://openreview.net/forum?id=D9JeNTs5Bu",
  "prompt": "Extract ALL reviewer comments, scores, and author responses from this OpenReview page. I need:\n1. Each reviewer's rating and confidence score\n2. Their detailed comments - strengths, weaknesses, questions\n3. Any author rebuttals/responses\n4. The final decision\n5. Meta-reviewer comments if any\nBe as complete as possible, capturing the full text of reviews."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5985b2c1-a59f-4e8d-9fec-9c0f62980410",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHBEDF4KMoV7pCBFj4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35d3e009-c0cb-4433-9957-fcbc80227732",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxR3ToPeyXBEWWevr52e2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1527,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 10171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
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

_source line 18 · 2026-05-30T06:28:17.254Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016xA1eVV3LfCiCRmTW45vvH`</summary>

```json
{
  "url": "https://neurips.cc/virtual/2025/poster/119236",
  "prompt": "Extract all information about this NeurIPS 2025 poster for ReliabilityRAG. Include any session details, abstract, author list, and any linked materials or discussion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35d3e009-c0cb-4433-9957-fcbc80227732",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHBEDF4KMoV7pCBFj4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "611b34fd-81b6-4c6c-b605-2b39b299924a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxR3ToPeyXBEWWevr52e2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1527,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 10171,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1527,
          "output_tokens": 366,
          "cache_read_input_tokens": 10171,
          "cache_creation_input_tokens": 1666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1666,
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

_source line 19 · 2026-05-30T06:28:17.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016xTYVgYwa214d66EuXei4t`</summary>

```json
{
  "query": "ReliabilityRAG paper review discussion Maximum Independent Set RAG robustness 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "611b34fd-81b6-4c6c-b605-2b39b299924a",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHBEDF4KMoV7pCBFj4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43d3c90e-2f53-4eb3-9069-6db70cd5f634",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxR3ToPeyXBEWWevr52e2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1527,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 10171,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1527,
          "output_tokens": 366,
          "cache_read_input_tokens": 10171,
          "cache_creation_input_tokens": 1666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1666,
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

_source line 20 · 2026-05-30T06:28:19.142Z_

<details><summary>↩ Tool result · `toolu_0116JRCL6RZnogRd9fY3vZtm`</summary>

```text
# ReliabilityRAG Review Analysis

Based on the provided OpenReview page content, I cannot extract the reviewer comments, scores, author responses, or final decision because **this information is not included in the page excerpt provided**.

The page content shows only:
- Paper title and metadata
- Author names and affiliations
- Publication date (18 Sept 2025)
- Keywords and abstract
- Primary area classification
- Footer/navigation elements

## What's Missing:
- Individual reviewer ratings and confidence scores
- Detailed reviewer comments (strengths/weaknesses)
- Author rebuttals or responses
- Final acceptance/rejection decision
- Meta-reviewer commentary

To access this information, you would need to:
1. Visit the full paper page on OpenReview
2. Scroll to the "Reviews" section
3. Click the "Revisions" link noted on the page
4. Access the decision letter

The page structure indicates these sections exist (note the "[Revisions](/revisions?id=D9JeNTs5Bu)" link), but the actual review content wasn't included in your provided excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35d3e009-c0cb-4433-9957-fcbc80227732",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "cdda555f-0027-444c-abdb-c094149871ce",
  "sourceToolAssistantUUID": "35d3e009-c0cb-4433-9957-fcbc80227732",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:28:22.613Z_

<details><summary>↩ Tool result · `toolu_016xA1eVV3LfCiCRmTW45vvH`</summary>

```text
# ReliabilityRAG - NeurIPS 2025 Poster Information

## Session Details
- **Type:** Poster presentation
- **Date & Time:** Thursday, December 4, 2025, 11:00 AM – 2:00 PM PST
- **Location:** San Diego

## Authors
Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova

## Overview
This work addresses vulnerabilities in Retrieval-Augmented Generation systems, particularly those used for web search. The framework tackles adversarial attacks on retrieval corpora through a novel defense mechanism that leverages document reliability signals.

## Key Contribution Summary
The researchers introduced an approach using graph theory to identify trustworthy documents among retrieved results. They developed an algorithm based on Maximum Independent Set optimization that "prioritizes higher-reliability documents" while providing robustness guarantees. A scalable variation enables efficient processing of large document sets.

## Materials Available
- Project page (GitHub repository)
- Presentation slides (PDF)
- Poster (PNG image)
- OpenReview discussion forum

## Results Highlight
The framework demonstrates improved robustness against corpus attacks compared to existing methods, maintains accuracy on benign queries, and performs well on longer-form generation tasks where previous defenses showed limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "611b34fd-81b6-4c6c-b605-2b39b299924a",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "25e33910-faf2-49bf-a1ab-9112c88c79e3",
  "sourceToolAssistantUUID": "611b34fd-81b6-4c6c-b605-2b39b299924a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-30T06:28:25.755Z_

<details><summary>↩ Tool result · `toolu_016xTYVgYwa214d66EuXei4t`</summary>

```text
Web search results for query: "ReliabilityRAG paper review discussion Maximum Independent Set RAG robustness 2025"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/html/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://openreview.net/pdf?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"When Should You Wait Before Updating? Toward a Robustness Refinement","url":"https://arxiv.org/pdf/2304.05831"},{"title":"Learning-Augmented Maximum Independent Set - DROPS","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2024.24"}]

Based on the search results, I found the ReliabilityRAG paper. Here's an overview:

## ReliabilityRAG Overview

ReliabilityRAG is a novel framework designed to make RAG-based systems robust. Retrieval-Augmented Generation (RAG) enhances Large Language Models by grounding their outputs in external documents, but these systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection.

## Maximum Independent Set (MIS) Approach

The paper's key technical contribution involves using graph theory for robustness. The framework introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, with the MIS variant explicitly prioritizing higher-reliability documents and providing provable robustness guarantees against bounded adversarial corruption under natural assumptions.

The document-selection algorithm identifies a "consistent majority" among retrieved documents by finding the Maximum Independent Set (MIS) on a "contradiction graph," where vertices represent the retrieved documents, and edges connect pairs determined to be contradictory by a Natural Language Inference (NLI) model.

## Scalability and Performance

Recognizing the computational cost of exact MIS for large retrieval sets, the framework includes a scalable weighted sample and aggregate framework that explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.

Empirical results show ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43d3c90e-2f53-4eb3-9069-6db70cd5f634",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "032b4e06-01d0-4c54-ae4a-507cefb32605",
  "sourceToolAssistantUUID": "43d3c90e-2f53-4eb3-9069-6db70cd5f634",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-30T06:28:29.923Z_

Let me try to get the full paper content from the HTML version and dig into the OpenReview reviews more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "032b4e06-01d0-4c54-ae4a-507cefb32605",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHCZF19kKmHGtAus3ih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7d1cd0a-9555-45a7-b569-6861b7d8eef6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGvHr5abcjT6qCJDHGsjR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 11837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 24 · 2026-05-30T06:28:38.446Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GaaCCDj8hQuHCKYDNuSK8q`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.23519",
  "prompt": "Extract the COMPLETE technical content of this paper. I need every detail:\n\n1. INTRODUCTION: What exact problem/gap do they identify? How do they compare to RobustRAG specifically? What are RobustRAG's limitations they point out?\n\n2. METHOD - Graph Construction: How exactly is the contradiction graph built? What NLI model? What are the edge criteria? How is reliability incorporated into the graph?\n\n3. METHOD - MIS Algorithm: What is the exact MIS formulation? Is it weighted MIS? What approximation algorithm do they use? What is the greedy procedure? How do reliability scores factor in?\n\n4. METHOD - Weighted Sample and Aggregate: How does this work for long-form generation? How are sampling weights determined? How many samples? How is aggregation done?\n\n5. THEOREMS: What are the exact formal certified robustness guarantees? State each theorem precisely with its conditions and conclusions. What assumptions are required?\n\n6. THREAT MODEL: What is the exact threat model? How many adversarial documents can the attacker inject? What can/can't the attacker do?\n\n7. EXPERIMENTS: All datasets, all baselines, key numerical results (accuracy numbers, robustness percentages)\n\n8. LIMITATIONS: What do they acknowledge as limitations?\n\n9. How do they handle the NP-hardness of MIS?\n\nBe extremely thorough and technical."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7d1cd0a-9555-45a7-b569-6861b7d8eef6",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHCZF19kKmHGtAus3ih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bae3f873-72b2-4bf2-88ac-1e3ad6422d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGvHr5abcjT6qCJDHGsjR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 11837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 25 · 2026-05-30T06:28:40.872Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ea8aesE5X1sHdgh6dMtk7U`</summary>

```json
{
  "url": "https://openreview.net/forum?id=D9JeNTs5Bu",
  "prompt": "I need to find the reviews for this paper. Look for any links to reviewer comments, official reviews, or review sections. Extract any reviewer IDs, review text, ratings, or links to individual reviews. Also look for any tabs or sections labeled \"Reviews\", \"Official Review\", or similar."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bae3f873-72b2-4bf2-88ac-1e3ad6422d4d",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHCZF19kKmHGtAus3ih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c89f41f-0e4e-4311-8fc8-1c4e88c1b455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGvHr5abcjT6qCJDHGsjR7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3373,
      "cache_read_input_tokens": 11837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3373,
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

_source line 26 · 2026-05-30T06:28:43.663Z_

<details><summary>↩ Tool result · `toolu_01Ea8aesE5X1sHdgh6dMtk7U`</summary>

```text
Based on the web page content provided, **no reviews are visible or accessible** from this excerpt. 

The page shows the paper's title, author list, abstract, and publication metadata for NeurIPS 2025, but does not display actual reviewer comments or ratings. While there is a "Revisions" link mentioned (`/revisions?id=D9JeNTs5Bu`), the actual review sections are not included in the content shared.

To locate reviews, you would likely need to:
- Click on the paper's full page on OpenReview.net
- Look for tabs such as "Reviews," "Official Reviews," or "Comments"
- Check if reviewer identities and scores are publicly available (policies vary by venue)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c89f41f-0e4e-4311-8fc8-1c4e88c1b455",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "15a580e9-0e22-48b3-ad4c-8b5198a25af9",
  "sourceToolAssistantUUID": "5c89f41f-0e4e-4311-8fc8-1c4e88c1b455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-30T06:29:04.404Z_

<details><summary>↩ Tool result · `toolu_01GaaCCDj8hQuHCKYDNuSK8q`</summary>

```text
# ReliabilityRAG: Technical Paper Summary

## 1. INTRODUCTION & PROBLEM IDENTIFICATION

**Core Problem:** RAG systems are vulnerable to corpus poisoning and prompt injection attacks that manipulate retrieved documents. Existing defense like RobustRAG suffer from critical limitations.

**RobustRAG Limitations Identified:**
- "Necessarily comes with significant information loss" in benign scenarios
- "Struggles in complex generation tasks" like long-form output
- Uses majority voting via "either keywords or next-token probabilities"
- Treats documents "as an unordered set," missing reliability signals

**Key Insight:** RAG-based web search has built-in reliability metrics (document ranking, PageRank) that are "difficult for adversaries to circumvent" due to decades of SEO defense development.

---

## 2. METHOD - GRAPH CONSTRUCTION

**Three-Stage Process:**

**Stage 1 - Isolated Answering:** LLM generates individual answers for each retrieved document: y_i ← LLM(q, {x_i})

**Stage 2 - Contradiction Testing:** 
- NLI model tests all pairs (y_i, y_j)
- Model: "DeBERTa-v3-large-mnli-fever-anli-ling-wanli"
- Contradiction threshold β = 0.5
- Marks pair contradictory if NLI(y_i, y_j) ≥ β

**Stage 3 - Graph Encoding:**
- Vertices = retrieved documents (inheriting retrieval rank)
- Edges = contradiction relationships between document pairs
- Result: undirected contradiction graph G = (V, E)

**Reliability Integration:** Documents maintain original ranking indices; lexicographic ordering prioritizes higher-ranked documents in tie-breaking.

---

## 3. METHOD - MIS ALGORITHM

**Exact MIS Formulation:**

"S* = arg max_S independent (|S|, -lex(S))"

**Key Properties:**
- Maximum cardinality (prioritizes largest non-contradictory set)
- Lexicographically smallest among maximum sets (prefers higher-ranked documents)
- Not weighted MIS; instead, rank-aware selection via lexicographic ordering

**Algorithm Implementation:**
- Brute-force enumeration of all 2^|V| subsets for k ≤ 20
- Bit-masking suffices for practical RAG pipelines
- Computational complexity: exponential, feasible for small k

**Reliability Incorporation:** The lexicographic tie-breaking rule (lex(S)) ensures when multiple MIS exist with equal size, the set containing higher-indexed documents (better ranked) is selected.

---

## 4. METHOD - WEIGHTED SAMPLE AND AGGREGATE

**Framework for Scalability (Algorithm 2):**

**Sampling Mechanism:**
- T rounds of sampling (default T=20)
- Each round samples m documents with replacement (default m=2)
- Sampling probability: w(x_i) for each document
- Weight formula: w(x_i) ∝ γ^(i-1) with γ=0.9 (exponential decay by rank)

**Aggregation:** General framework instantiated with MIS:
- Treat intermediate answers a_t as "isolated answers"
- Treat contexts S_t as "documents"
- Rank contexts lexicographically based on contained documents
- Apply MIS algorithm to aggregate T intermediate answers

**Robustness Preservation:** Framework maintains theoretical guarantees with high probability while controlling runtime via parameter T.

---

## 5. THEOREMS & CERTIFIED ROBUSTNESS

**Theorem 1 (Main Robustness Result):**

**Conditions:**
- Adversary corrupts at most k' ≤ (1/5)k documents
- NLI error ≤ ε₁ between benign documents
- NLI error ≤ ε₂ between benign and malicious documents
- ε₁ < μ/m and ε₂ < ((1-μ)m-1)/((1+δ)em) for constants 0<μ<1/2, 0<δ<1
- m = k - k' = number of benign documents

**Conclusion:** "Probability that maximum independent set does not contain any malicious document is at least 1 - e^(-O(k))"

**Robustness Level:** Algorithm is (1 - e^(-O(k)))-robust, meaning malicious document selection probability vanishes as k grows.

**Perfect NLI Case (Appendix B.2):** When ε₁ = ε₂ = 0, MIS exactly identifies benign documents with perfect robustness and utility for k' < k/2.

**Weighted Sampling Guarantee (Appendix B.3):** Robustness guarantees preserved with high probability through weighted sampling framework.

---

## 6. THREAT MODEL

**Adversary Capabilities:**
- Injects k' corrupted documents into k retrieved documents
- Replaces documents at selected positions S ⊆ {1,...,k}
- Bounded corruption: k' ≪ k (fundamentally necessary condition)
- Ranking positions fixed; higher ranks require more effort to compromise

**Attack Difficulty Structure:** "Injecting documents into higher-ranked or higher-weighted positions is more difficult" than lower positions.

**Attack Types Evaluated:**
1. **Corpus Poisoning:** "Inserts false or misleading factual statements"
2. **Prompt Injection:** "Embeds jailbreak or control prompts"

**Out of Scope:** Direct infrastructure attacks on system providers.

**Defense Goal:** Sub-select unmanipulated documents to thwart adversary's specific malicious output objective.

---

## 7. EXPERIMENTS

**Datasets:** RealtimeQA (RQA), Natural-Questions (NQ), TriviaQA (TQA), Biography (Bio)

**LLMs:** Mistral-7B-Instruct-v0.2, Llama3.2-3B-Instruct, GPT-4o-mini (temperature=0)

**Configurations:**
- MIS: k=10 documents
- Sampling+MIS: k=50 documents, T=20 rounds, m=2 context size

**Baselines:** Vanilla RAG, RobustRAG (Keyword), AstuteRAG, InstructRAG

### Key Numerical Results (Table 1, k=10, Prompt Injection):

**Mistral-7B (RQA):**
- Benign: MIS 70% vs RobustRAG 56%
- Position 1: MIS 68% vs RobustRAG 53%
- Position 10: MIS 60% vs RobustRAG 55%

**Bio (Long-form, GPT-4o-mini):**
- Benign: MIS 80.1 vs RobustRAG 61.2 (judge score)
- Position 1: MIS 77.9 vs RobustRAG 60.4
- Position 10: MIS 79 vs RobustRAG 61.4

**Key Finding:** MIS maintains substantially higher performance on long-form generation tasks where RobustRAG struggles.

### Sampling+MIS Results (Table 2, k=50):

**GPT-4o-mini (NQ):**
- Benign: 68.6% vs RobustRAG 63.4%
- Position 1: 60.8% vs RobustRAG 60.6%
- Position 25: 67.4% vs RobustRAG 63.4%
- Position 50: 68.6% vs RobustRAG 63%

**Multi-Position Attacks (Figure 2, NQ, k=50):** With 40% document corruption at lower ranks, Sampling+MIS "shows decent performance, whereas RobustRAG collapses much faster."

---

## 8. ACKNOWLEDGED LIMITATIONS

1. **Ambiguous Queries:** Assumes "consistent majority" exists; fails on queries lacking consensus
2. **Scalability:** MIS requires exponential time; sampling heuristic needed for k>>20
3. **Reliability Signals:** Framework designed for web search; applicability to other domains unclear
4. **NLI Dependency:** Performance degrades with weaker contradiction detection models
5. **Long-Form Generation:** Applicability to "complex long-form generation" beyond tested tasks uncertain
6. **Consistent Malicious Behavior:** Assumes adversaries produce consistently contradictory outputs

---

## 9. NP-HARDNESS HANDLING

"Finding MIS...requires 2^Ω(|V|) time in worst case under Exponential Time Hypothesis"

**Practical Solution:** For k ≤ 20 documents (current RAG practice), "exact MIS can be found with brute-force in milliseconds"

**Scalability Solution:** Weighted sample-and-aggregate framework (Section 4):
- Reduces problem size through sampling
- Applies MIS to T intermediate answers instead of k documents
- Controls runtime via parameter T
- Trades exact optimality for computational feasibility while preserving robustness guarantees probabilistically
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bae3f873-72b2-4bf2-88ac-1e3ad6422d4d",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "b0446b1b-4b7b-4fb8-90dd-129380c372b0",
  "sourceToolAssistantUUID": "bae3f873-72b2-4bf2-88ac-1e3ad6422d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-30T06:29:07.323Z_

Let me try to access the OpenReview reviews directly and also search for any blog posts or discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0446b1b-4b7b-4fb8-90dd-129380c372b0",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHFQdRPunAzPSPBmj7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf460932-ba49-4e3e-8cc8-c06d15cffb86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdmHuz1oYtXJ6tKvtH8DNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 2777,
      "cache_read_input_tokens": 15210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2777,
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

_source line 29 · 2026-05-30T06:29:09.669Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G64QVQEktxHUWWncnSeZCn`</summary>

```json
{
  "url": "https://openreview.net/forum?id=D9JeNTs5Bu&noteId=D9JeNTs5Bu",
  "prompt": "Extract all official reviews, reviewer ratings, confidence scores, and any discussion comments. Look for any sections with reviewer text, strengths, weaknesses, questions, ratings. Extract everything visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf460932-ba49-4e3e-8cc8-c06d15cffb86",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHFQdRPunAzPSPBmj7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e3288d6-aeb5-48ac-83a9-bde644b4ef81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdmHuz1oYtXJ6tKvtH8DNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 2777,
      "cache_read_input_tokens": 15210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2777,
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

_source line 30 · 2026-05-30T06:29:10.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7txBWojsE3sC4wXz5m972`</summary>

```json
{
  "query": "site:openreview.net \"D9JeNTs5Bu\" review rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e3288d6-aeb5-48ac-83a9-bde644b4ef81",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHFQdRPunAzPSPBmj7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f7602dc-7100-4a12-9f8a-bc9fda3014cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdmHuz1oYtXJ6tKvtH8DNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 2777,
      "cache_read_input_tokens": 15210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2777,
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

_source line 31 · 2026-05-30T06:29:10.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01322WpYy4fnySyVJXDKJ8Zx`</summary>

```json
{
  "query": "\"ReliabilityRAG\" review blog discussion analysis criticism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f7602dc-7100-4a12-9f8a-bc9fda3014cc",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHFQdRPunAzPSPBmj7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ace8e5aa-1c41-4878-a1ad-663322c6ca50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdmHuz1oYtXJ6tKvtH8DNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 2777,
      "cache_read_input_tokens": 15210,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 190,
          "output_tokens": 262,
          "cache_read_input_tokens": 15210,
          "cache_creation_input_tokens": 2777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2777,
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

_source line 32 · 2026-05-30T06:29:12.694Z_

<details><summary>↩ Tool result · `toolu_01G64QVQEktxHUWWncnSeZCn`</summary>

```text
# ReliabilityRAG Review Extraction

Based on the provided web page content, **no official reviews, reviewer ratings, confidence scores, or discussion comments are visible**. 

The page displays:
- Paper metadata (title, authors, publication date)
- Abstract describing the research
- Paper keywords and submission information
- Navigation and footer elements

The page does not contain the peer review section that would typically appear on OpenReview platforms. To access reviews and ratings, you would likely need to:

1. Click on the "[Revisions](/revisions?id=D9JeNTs5Bu)" link visible on the page
2. Navigate to a dedicated reviews section (if available)
3. Check if reviews are restricted to logged-in users via the "[Login](/login)" option
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e3288d6-aeb5-48ac-83a9-bde644b4ef81",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "7aca8ce5-463b-4e93-a7e6-deeb6c3bfde4",
  "sourceToolAssistantUUID": "2e3288d6-aeb5-48ac-83a9-bde644b4ef81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:29:14.816Z_

<details><summary>↩ Tool result · `toolu_01Y7txBWojsE3sC4wXz5m972`</summary>

```text
Web search results for query: "site:openreview.net "D9JeNTs5Bu" review rating"

Links: [{"title":"How to Get Reviewer Ratings | OpenReview","url":"https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-reviewer-ratings"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"OpenReview Support | OpenReview","url":"https://openreview.net/group?id=OpenReview.net%2FSupport"},{"title":"How to submit a Review Revision | OpenReview","url":"https://docs.openreview.net/how-to-guides/submissions-comments-reviews-and-decisions/how-to-submit-a-review-revision"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"About | OpenReview","url":"https://openreview.net/about"},{"title":"Frequently Asked Questions | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions"},{"title":"Data Retrieval for API 1 Venues | OpenReview","url":"https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/data-retrieval-for-api-1-venues"},{"title":"Open Review (@openreviewnet) / Posts / X","url":"https://x.com/openreviewnet?lang=en"},{"title":"Submissions, comments, reviews, and decisions | OpenReview","url":"https://docs.openreview.net/how-to-guides/submissions-comments-reviews-and-decisions"}]

The search results did not return any specific information about the review ID "D9JeNTs5Bu" or its rating on OpenReview. The results returned general OpenReview documentation about how reviewer ratings work on the platform, but no specific data about that particular review.

The search with the `site:openreview.net` constraint and the specific review ID "D9JeNTs5Bu" did not yield direct results. This could mean:

1. The review ID may not be publicly accessible or indexed by search engines
2. The review may require direct access to OpenReview to view
3. The ID may not exist or may be formatted differently

If you're looking for information about a specific review on OpenReview, you might need to visit the OpenReview website directly and access the review through the paper's forum page (https://openreview.net/forum?id=D9JeNTs5Bu).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f7602dc-7100-4a12-9f8a-bc9fda3014cc",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "a03f66a4-e9b2-47e7-97c2-aadb91a97ec7",
  "sourceToolAssistantUUID": "7f7602dc-7100-4a12-9f8a-bc9fda3014cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-30T06:29:17.430Z_

<details><summary>↩ Tool result · `toolu_01322WpYy4fnySyVJXDKJ8Zx`</summary>

```text
Web search results for query: ""ReliabilityRAG" review blog discussion analysis criticism"

Links: [{"title":"Evaluating Answer Quality in RAG Systems: Precision, Recall, and Faithfulness - Cobbai Blog","url":"https://cobbai.com/blog/evaluate-rag-answers"},{"title":"RAG evaluation: a technical guide to measuring retrieval-augmented generation","url":"https://toloka.ai/blog/rag-evaluation-a-technical-guide-to-measuring-retrieval-augmented-generation/"},{"title":"4 Key Reasons Why Your RAG Application Struggles with Accuracy","url":"https://www.pryon.com/landing/4-key-reasons-why-your-rag-application-struggles-with-accuracy"},{"title":"RAG Evaluation: A Complete Guide for 2025","url":"https://www.getmaxim.ai/articles/rag-evaluation-a-complete-guide-for-2025/"},{"title":"A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges","url":"https://www.mdpi.com/2504-2289/9/12/320"},{"title":"RAG Evaluation: Don’t let customers tell you first | Pinecone","url":"https://www.pinecone.io/learn/series/vector-databases-in-production-for-busy-engineers/rag-evaluation/"},{"title":"A complete guide to RAG evaluation: metrics, testing and best practices","url":"https://www.evidentlyai.com/llm-guide/rag-evaluation"},{"title":"Trustworthiness in Retrieval-Augmented Generation Systems: A Survey","url":"https://arxiv.org/html/2409.10102v1"}]

Based on the search results, I found several resources discussing RAG (Retrieval-Augmented Generation) evaluation, but the search did not return any specific results for a product, tool, or framework called "ReliabilityRAG." 

The search results do cover extensive discussions about RAG evaluation more broadly, including:

- **RAG Evaluation Frameworks and Best Practices**: Multiple articles discuss evaluation methodologies for RAG systems, including metrics like precision, recall, and F1 scores.

- **Challenges with RAG Systems**: Common obstacles include document ingestion and parsing issues that prevent the system from understanding diverse content, to misalignment with user queries, ineffective answer matching, and LLM hallucinations that distort the final output.

- **Trustworthiness Concerns**: Analysis covers six different aspects: factuality, robustness, fairness, transparency, accountability, and privacy.

- **Evaluation Approaches**: Judge reliability improves with mixed methods: LLM-as-a-judge, programmatic checks, and human review.

If you're looking for information about a specific tool or product called "ReliabilityRAG," it may not have significant online discussion or reviews, or it might be known by a different name. Could you provide more context about what ReliabilityRAG is or where you encountered it?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ace8e5aa-1c41-4878-a1ad-663322c6ca50",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "ce929899-a00a-4934-b094-97d41b4b723d",
  "sourceToolAssistantUUID": "ace8e5aa-1c41-4878-a1ad-663322c6ca50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-30T06:29:20.559Z_

Let me try the OpenReview API and also look for the NeurIPS slides, plus search for RobustRAG comparison discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce929899-a00a-4934-b094-97d41b4b723d",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHGNFpV7fDTtXYA98Ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b09a4ef-3fc0-403f-9044-57a1d70bf717",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZjbGUCQ9UDAhRKYfF93L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2121,
      "cache_read_input_tokens": 17987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2121,
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

_source line 36 · 2026-05-30T06:29:22.636Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019McVG9JSs1sz2ykGmco8iq`</summary>

```json
{
  "url": "https://api.openreview.net/notes?forum=D9JeNTs5Bu",
  "prompt": "Extract all review content from this API response. Look for any notes that contain reviewer ratings, review text, strengths, weaknesses, questions, confidence scores, and any decision information. Extract everything completely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b09a4ef-3fc0-403f-9044-57a1d70bf717",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHGNFpV7fDTtXYA98Ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07c024ff-1981-44de-8727-c4be443c6163",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZjbGUCQ9UDAhRKYfF93L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2121,
      "cache_read_input_tokens": 17987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2121,
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

_source line 37 · 2026-05-30T06:29:23.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014nQTcTQcc2Wu3yhBUHKoCN`</summary>

```json
{
  "query": "RobustRAG vs ReliabilityRAG comparison \"Maximum Independent Set\" contradiction graph certified robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c024ff-1981-44de-8727-c4be443c6163",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHGNFpV7fDTtXYA98Ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4031dfd-7254-4f09-b58f-c4dc03a966dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZjbGUCQ9UDAhRKYfF93L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2121,
      "cache_read_input_tokens": 17987,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 17987,
          "cache_creation_input_tokens": 2121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2121,
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

_source line 38 · 2026-05-30T06:29:24.143Z_

<details><summary>↩ Tool result · `toolu_019McVG9JSs1sz2ykGmco8iq`</summary>

```text
# Review Content Extraction Result

Based on the API response provided, there is **no review content to extract**.

The response contains:
- An empty notes array: `"notes":[]`
- A count of zero: `"count":0`

There are no reviewer ratings, review text, strengths, weaknesses, questions, confidence scores, or decision information present in this data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07c024ff-1981-44de-8727-c4be443c6163",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "e853520e-a6df-43cd-8b90-afd70f8457e4",
  "sourceToolAssistantUUID": "07c024ff-1981-44de-8727-c4be443c6163",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-30T06:29:30.912Z_

<details><summary>↩ Tool result · `toolu_014nQTcTQcc2Wu3yhBUHKoCN`</summary>

```text
Web search results for query: "RobustRAG vs ReliabilityRAG comparison "Maximum Independent Set" contradiction graph certified robustness"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/html/2509.23519"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://openreview.net/pdf?id=D9JeNTs5Bu"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119236"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"}]

Based on the search results, here's a comparison of RobustRAG and ReliabilityRAG:

## Core Approaches

Both RobustRAG and ReliabilityRAG provide instance-level certification for RAG generation in the presence of corrupted or malicious retrieval results. However, they differ in their methodologies:

**RobustRAG:** RobustRAG employs majority voting over retrieved documents to mitigate the impact of adversarially manipulated contents, based on either keywords or next-token probabilities, but this implementation necessarily comes with significant information loss.

**ReliabilityRAG:** ReliabilityRAG adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones through a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.

## Key Advantages of ReliabilityRAG

ReliabilityRAG's MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. Additionally, RobustRAG suffers from limited performance in benign (no-attack) scenarios and struggles in complex generation tasks, whereas ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

## Scalability

Recognizing the computational cost of exact MIS for large retrieval sets, ReliabilityRAG includes a scalable weighted sample and aggregate framework that explicitly utilizes reliability information while efficiently handling many documents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4031dfd-7254-4f09-b58f-c4dc03a966dd",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "7982c3ef-4c77-436b-8e70-998fe5eca351",
  "sourceToolAssistantUUID": "d4031dfd-7254-4f09-b58f-c4dc03a966dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-30T06:29:34.375Z_

Let me try the Emergent Mind page for community discussion and try an alternative OpenReview API endpoint for reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7982c3ef-4c77-436b-8e70-998fe5eca351",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHHMsHNdDFRr9ysbG43",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44ff0b3e-8572-4568-a9bf-8e01e684d645",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYwd5wiqU3FSCu4ADKiKVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 20108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
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

_source line 41 · 2026-05-30T06:29:36.312Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DxGSaQC5BpY92eUVTXuoWa`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems",
  "prompt": "Extract all information about ReliabilityRAG from this page. Look for any discussion, analysis, comparison with other methods, community commentary, or technical summaries. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44ff0b3e-8572-4568-a9bf-8e01e684d645",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHHMsHNdDFRr9ysbG43",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b9975f2-6949-4de5-8cd0-10c9a092c4e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYwd5wiqU3FSCu4ADKiKVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 20108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
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

_source line 42 · 2026-05-30T06:29:37.747Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DiDgK6CpJKBhvYuv8qhEgA`</summary>

```json
{
  "url": "https://api.openreview.net/notes?forum=D9JeNTs5Bu&details=replies",
  "prompt": "Extract all content from this API response - look for reviews, comments, replies, ratings, any text content at all."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b9975f2-6949-4de5-8cd0-10c9a092c4e2",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHHMsHNdDFRr9ysbG43",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d07758f-c95a-410b-bce8-1c8db38e5b03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYwd5wiqU3FSCu4ADKiKVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 20108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
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

_source line 43 · 2026-05-30T06:29:38.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FcLVJBXpTmPvR7147aFx3M`</summary>

```json
{
  "query": "NeurIPS 2025 \"ReliabilityRAG\" review score accept poster"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d07758f-c95a-410b-bce8-1c8db38e5b03",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHHMsHNdDFRr9ysbG43",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80c446ae-c856-4f80-a7a0-d76534250573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYwd5wiqU3FSCu4ADKiKVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 20108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
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

### Tool result

_source line 44 · 2026-05-30T06:29:39.619Z_

<details><summary>↩ Tool result · `toolu_01DiDgK6CpJKBhvYuv8qhEgA`</summary>

```text
# API Response Analysis

The provided response contains **no extractable content**. 

The JSON object shows:
- Empty notes array: `"notes":[]`
- Zero count: `"count":0`
- Cached data: `"fromCache":true`

There are no reviews, comments, ratings, or text content present in this API response to analyze or summarize.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d07758f-c95a-410b-bce8-1c8db38e5b03",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "eec603b8-486f-46ba-95f9-f1dfbabff012",
  "sourceToolAssistantUUID": "3d07758f-c95a-410b-bce8-1c8db38e5b03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-30T06:29:41.749Z_

<details><summary>↩ Tool result · `toolu_01DxGSaQC5BpY92eUVTXuoWa`</summary>

```text
# ReliabilityRAG Information Extracted

Based on the provided content, here is all information about ReliabilityRAG:

## References and Citations
ReliabilityRAG is mentioned as one of the frameworks providing instance-level certification for RAG generation when dealing with corrupted or malicious retrieval results, alongside RobustRAG and related systems.

## Core Strategy
ReliabilityRAG employs an "isolate-then-aggregate" approach where "the LLM produces an isolated response" for each retrieved passage, with aggregation functions combining these results to constrain adversarial effects to at most t responses.

## Performance Metrics
The framework achieves robust certification rates of "greater than 40% certifiable accuracy for k=10" depending on the specific task and methodology employed.

## Defense Mechanism
ReliabilityRAG utilizes "majority keyword voting, thresholded keyword inclusion, or robust sequential token aggregation" to combine isolated responses in a manner that formally bounds the adversary's impact.

## Clean Data Preservation
The certified aggregation approach maintains data integrity, reducing attack success rates while causing only "1–11% accuracy decrease on clean data, depending on aggregation tightness."

## Source
ReliabilityRAG is documented in the paper: *ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search* (2025)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b9975f2-6949-4de5-8cd0-10c9a092c4e2",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "3ca889d3-14ea-4ce5-a832-716f5e7e0062",
  "sourceToolAssistantUUID": "5b9975f2-6949-4de5-8cd0-10c9a092c4e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-30T06:29:43.162Z_

<details><summary>↩ Tool result · `toolu_01FcLVJBXpTmPvR7147aFx3M`</summary>

```text
Web search results for query: "NeurIPS 2025 "ReliabilityRAG" review score accept poster"

Links: [{"title":"Reflections on the 2025 Review Process from the Program Committee Chairs – NeurIPS Blog","url":"https://blog.neurips.cc/2025/09/30/reflections-on-the-2025-review-process-from-the-program-committee-chairs/"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"2025 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2025/ReviewerGuidelines"},{"title":"2025 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2025-conference/"},{"title":"Will My (NeurIPS?) Paper get Accepted?","url":"https://horace.io/willmypaperbeaccepted/"},{"title":"Evaluating Quality of Answers for Retrieval-Augmented Generation: A   Strong LLM Is All You Need","url":"https://arxiv.org/pdf/2406.18064"}]

Based on the search results, I found information about the ReliabilityRAG paper. ReliabilityRAG is a framework for robust defense in RAG-based systems that provides provable robustness guarantees against adversarial attacks, maintains high benign accuracy, and excels in long-form generation tasks.

However, the search results do not contain specific information about the paper's review score at NeurIPS 2025 or its acceptance status as a poster. While I found the arxiv version of the ReliabilityRAG paper and general information about NeurIPS 2025's review process and acceptance criteria, I was unable to locate the specific review scores or acceptance details you're looking for through this search.

To find this information, you may want to check:
- The NeurIPS 2025 OpenReview platform directly
- The official NeurIPS 2025 accepted papers list
- The paper's OpenReview page if it was submitted to NeurIPS 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80c446ae-c856-4f80-a7a0-d76534250573",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "b69ce5ab-01cb-45b2-93c4-df8bccd4d14c",
  "sourceToolAssistantUUID": "80c446ae-c856-4f80-a7a0-d76534250573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-30T06:29:48.335Z_

Let me try a different API path for the OpenReview reviews and also get the NeurIPS slides for additional detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b69ce5ab-01cb-45b2-93c4-df8bccd4d14c",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHJGWbehJCpupapo6GG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a221d05-2776-4337-bbc9-bfd930fa7489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qztp5qtqFgpDiSmrzWtEGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1325,
      "cache_read_input_tokens": 21428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1325,
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

_source line 48 · 2026-05-30T06:29:50.166Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01726W9BBsHvrhvNa5hxA24r`</summary>

```json
{
  "url": "https://api2.openreview.net/notes?forum=D9JeNTs5Bu",
  "prompt": "Extract ALL content from this API response. Look for any reviews, comments, decisions, ratings, or text content. Return everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a221d05-2776-4337-bbc9-bfd930fa7489",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHJGWbehJCpupapo6GG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5f34f95-b1db-45ab-bd37-353fbc822fca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qztp5qtqFgpDiSmrzWtEGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1325,
      "cache_read_input_tokens": 21428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1325,
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

_source line 49 · 2026-05-30T06:29:52.512Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QYuDkHTWQVNEqwXf7RpPB8`</summary>

```json
{
  "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf",
  "prompt": "Extract all content from these presentation slides. I need:\n1. Key claims and contributions\n2. Any results tables or figures described\n3. Comparison with RobustRAG\n4. Any additional technical details not in the paper\n5. Any discussion of limitations or future work\nBe thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5f34f95-b1db-45ab-bd37-353fbc822fca",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHJGWbehJCpupapo6GG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "491d042a-283a-4e5f-bda5-f67e93c696d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qztp5qtqFgpDiSmrzWtEGq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1325,
      "cache_read_input_tokens": 21428,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1325
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 21428,
          "cache_creation_input_tokens": 1325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1325,
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

_source line 50 · 2026-05-30T06:29:58.277Z_

<details><summary>↩ Tool result · `toolu_01726W9BBsHvrhvNa5hxA24r`</summary>

```text
# ReliabilityRAG Paper Review Summary

## Decision
**Accept (poster)** - The paper was accepted for NeurIPS 2025.

## Core Contribution
The authors propose ReliabilityRAG, a defense framework against retrieval corpus attacks in RAG systems using a graph-theoretic approach based on Maximum Independent Set (MIS) selection combined with reliability signals like search rankings.

## Key Strengths (Per Reviews)

- **Novel methodology**: "Translating document consistency into a rank-aware MIS problem is a novel, intuitive insight" that advances RAG robustness research
- **Theory-practice balance**: Provides λ-robustness guarantees while addressing computational barriers through scalable sampling
- **Empirical performance**: Maintains high benign accuracy while outperforming baselines (RobustRAG, VanillaRAG) across attack types
- **Defense-in-depth approach**: Combines NLI-based detection with ranking signals for resilience

## Primary Concerns Raised

1. **NLI dependency**: Performance degrades in non-English/technical domains; authors showed graceful degradation with 50% NLI error probability
2. **Multi-position attacks**: Initially underexplored in main text; comprehensive analysis relegated to appendix
3. **Computational overhead**: Sub-1s latency acknowledged as unoptimized; potential for parallelization improvements
4. **Parameter tuning**: Sampling parameters (γ, T, m) set heuristically without full theoretical justification

## Author Responses

Authors addressed reviewer concerns through:
- NLI robustness experiments showing graceful performance drops
- Lexical matching experiments demonstrating insufficiency (<4.31% attack failure even at optimal threshold)
- Multiple-choice dataset validation confirming LLM-judge reliability
- Latency analysis and optimization pathways proposed

## Reviewer Dispositions
All four reviewers ultimately affirmed positive assessments after discussion, with no unresolved fatal flaws.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5f34f95-b1db-45ab-bd37-353fbc822fca",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "bdbbacdb-e8bf-4d06-a6cb-00b146377720",
  "sourceToolAssistantUUID": "c5f34f95-b1db-45ab-bd37-353fbc822fca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-30T06:29:59.617Z_

<details><summary>↩ Tool result · `toolu_01QYuDkHTWQVNEqwXf7RpPB8`</summary>

```text
I appreciate your request, but I'm unable to extract meaningful content from the provided document. The text you've shared appears to be a PDF file encoded in binary/compressed format (starting with `%PDF-1.3` and containing FlateDecode streams), which renders as unintelligible character sequences rather than readable presentation slides.

To help you effectively, I would need:

1. **A plaintext or readable format** - such as:
   - Extracted text from the PDF
   - A markdown or .txt version of the slides
   - An HTML export
   - Screenshots with OCR'd text

2. **Or direct access to** the underlying slide content in a human-readable form

**What I can tell you:** The document structure indicates it contains images (XObjects) and text, but the compression and encoding prevent me from parsing the actual claims, results, comparisons with RobustRAG, or technical details you're seeking.

Could you provide the content in a more accessible format? Once you do, I'll be happy to:
- Identify key claims and contributions
- Extract results and figures
- Highlight RobustRAG comparisons
- Note technical details and limitations
- Summarize future work discussions

All while respecting the character limits and citation standards you've outlined.

[Binary content (application/pdf, 808.6KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/458a2eed-0834-465b-87af-c8668736149f/tool-results/webfetch-1780122593639-1djdw5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "491d042a-283a-4e5f-bda5-f67e93c696d4",
  "isSidechain": true,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "agentId": "a620a8dbf50fd8bc7",
  "type": "user",
  "uuid": "0a936287-9344-4f87-91bf-69527178be32",
  "sourceToolAssistantUUID": "491d042a-283a-4e5f-bda5-f67e93c696d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-30T06:31:22.467Z_

Excellent -- I got the OpenReview reviews from the API. Now I have a comprehensive picture. Let me compile everything.

Here is a thorough summary of the ReliabilityRAG paper:

---

## ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search

**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova (Princeton/USC)
**Venue:** NeurIPS 2025 (accepted as poster), presented December 4, 2025 in San Diego
**ArXiv:** https://arxiv.org/abs/2509.23519 (v1: Sep 27, 2025; v2: Feb 15, 2026)
**OpenReview:** https://openreview.net/forum?id=D9JeNTs5Bu

---

### 1. Problem and Gap Identified (Especially vs. RobustRAG)

The paper targets the vulnerability of RAG-based web-search systems (e.g., Google's Search AI Overview) to corpus poisoning and prompt injection attacks, where adversaries inject malicious documents into the retrieval corpus.

**Specific limitations of RobustRAG (Xiang et al.) they identify:**

- **Information loss:** RobustRAG uses majority voting via keywords or next-token probabilities, which "necessarily comes with significant information loss" in benign scenarios. It decomposes responses into atomic units (keywords or tokens) and aggregates via voting, which destroys contextual coherence.
- **Struggles with complex/long-form generation:** The keyword/token-level voting mechanism fundamentally cannot handle biography generation, multi-paragraph answers, or other long-form tasks. Their experiments show RobustRAG scoring ~61 vs. ReliabilityRAG's ~80 on biography generation.
- **Ignores reliability signals:** RobustRAG treats all retrieved documents "as an unordered set," completely ignoring the retrieval ranking, PageRank scores, and other reliability signals that web search engines already provide. These signals are the product of decades of SEO defense development and are genuinely informative about document trustworthiness.
- **Limited scalability:** RobustRAG's approach does not scale well to large retrieval sets.

**Key insight:** RAG-based web-search systems have built-in reliability metrics (document ranking, domain authority) that are "difficult for adversaries to circumvent." The paper argues these should be explicitly leveraged rather than discarded.

---

### 2. Key Insight: Document Reliability and MIS Computation

The central idea is to reframe robust document selection as a **graph-theoretic problem**:

- Model retrieved documents as vertices in a graph
- Connect contradictory document pairs with edges (using NLI)
- Finding the largest set of mutually non-contradictory documents = finding the **Maximum Independent Set (MIS)**
- Incorporate reliability/ranking information through **lexicographic tie-breaking** -- when multiple MIS of equal size exist, prefer the one containing higher-ranked (more reliable) documents

The insight is that adversarial documents will typically contradict the majority of benign documents, so they will be densely connected in the contradiction graph and naturally excluded from the MIS.

---

### 3. Technical Method Details

#### Stage 1: Isolated Answering
For each retrieved document x_i, the LLM generates an individual answer in isolation:
`y_i = LLM(q, {x_i})`

This prevents cross-contamination between documents during generation.

#### Stage 2: Contradiction Graph Construction
- Use a pairwise NLI model (**DeBERTa-v3-large-mnli-fever-anli-ling-wanli**) to test all answer pairs (y_i, y_j)
- An edge is added between documents i and j if `NLI_contradiction(y_i, y_j) >= beta` where beta = 0.5
- Result: undirected contradiction graph G = (V, E)

#### Stage 3: MIS Selection (Algorithm 1)
The optimization objective:
```
S* = argmax_S independent { (|S|, -lex(S)) }
```
This is a **two-criteria optimization**: first maximize the cardinality of the independent set, then among all maximum independent sets, choose the one that is lexicographically smallest (i.e., containing the highest-ranked documents).

**NP-hardness handling:** For k <= 20 documents (standard in current RAG pipelines), they use **brute-force enumeration** over all 2^|V| subsets via bit-masking. This is feasible -- runs "in milliseconds" for k=10.

Note: This is NOT weighted MIS. Reliability is incorporated through lexicographic ordering, not edge/vertex weights.

#### Stage 4: Weighted Sample-and-Aggregate for Scalability (Algorithm 2)
For larger document sets (k >> 20), exact MIS is infeasible. The scalable alternative:

1. **T = 20 rounds of sampling**, each drawing m = 2 documents with replacement
2. **Sampling weights:** `w(x_i) proportional to gamma^(i-1)` with gamma = 0.9 (exponential decay by rank). Higher-ranked documents have higher sampling probability.
3. In each round t, the LLM generates an answer a_t from the sampled context S_t
4. **Meta-aggregation:** Treat the T intermediate answers as new "isolated answers" and the T contexts as new "documents." Rank contexts lexicographically based on their constituent documents. Apply the MIS algorithm to aggregate these T intermediate answers.

This reduces the MIS problem from k documents to T intermediate results while preserving reliability information through the sampling weights.

---

### 4. Certified Robustness Guarantees

#### Theorem 1 (Main Result):
**Setting:** k total retrieved documents, adversary corrupts at most k' of them, m = k - k' benign documents remain.

**Conditions (natural assumptions):**
- k' <= (1/5)k (adversary controls at most 20% of documents)
- NLI error rate epsilon_1 between benign-benign document pairs (false contradiction rate)
- NLI error rate epsilon_2 between benign-malicious pairs (false non-contradiction rate)
- epsilon_1 < mu/m for some 0 < mu < 1/2
- epsilon_2 < ((1-mu)m - 1) / ((1+delta)em) for some 0 < delta < 1

**Conclusion:** The probability that the MIS contains any malicious document is at most e^(-Omega(k)). That is, the algorithm is **(1 - e^(-Omega(k)))-robust** -- the contamination probability vanishes exponentially as k grows.

**Intuition:** With a good NLI model, benign documents form a large clique-free cluster (low contradiction among themselves), while malicious documents contradict most benign ones (high connectivity in the graph). The MIS naturally selects the benign cluster.

#### Perfect NLI Case (Appendix B.2):
When epsilon_1 = epsilon_2 = 0 (perfect contradiction detection), the MIS **exactly** identifies all benign documents with perfect robustness and utility, provided k' < k/2 (adversary is a strict minority).

#### Weighted Sampling Guarantee (Appendix B.3):
The robustness guarantees are preserved with high probability through the weighted sampling framework, with bounds depending on T and the sampling weight distribution.

---

### 5. Threat Model

- Adversary can inject k' corrupted documents into the k retrieved results
- Documents can be placed at specific ranking positions S subset of {1,...,k}
- **Key structural assumption:** Injecting documents at higher-ranked positions is harder (requires more adversarial effort due to search engine ranking defenses)
- Two attack types evaluated: **corpus poisoning** (false/misleading facts) and **prompt injection** (jailbreak/control prompts)
- Out of scope: direct infrastructure attacks on the search provider
- Defense goal: sub-select only unmanipulated documents

---

### 6. Experimental Results

**Datasets:** RealtimeQA (RQA), Natural Questions (NQ), TriviaQA (TQA), Biography generation (Bio)

**LLMs tested:** Mistral-7B-Instruct-v0.2, Llama3.2-3B-Instruct, GPT-4o-mini (temperature=0)

**Baselines:** Vanilla RAG, RobustRAG (Keyword variant), AstuteRAG, InstructRAG

**Configurations:**
- MIS: k=10 documents
- Sampling+MIS: k=50 documents, T=20, m=2

**Key results (Table 1, k=10, prompt injection attack):**

| Setting | Method | Benign | Pos 1 Attack | Pos 10 Attack |
|---------|--------|--------|-------------|---------------|
| Mistral/RQA | MIS | 70% | 68% | 60% |
| Mistral/RQA | RobustRAG | 56% | 53% | 55% |
| Bio/GPT-4o-mini | MIS | 80.1 | 77.9 | 79.0 |
| Bio/GPT-4o-mini | RobustRAG | 61.2 | 60.4 | 61.4 |

**Key results (Table 2, k=50, sampling+MIS):**

| Setting | Method | Benign | Pos 1 | Pos 25 | Pos 50 |
|---------|--------|--------|-------|--------|--------|
| GPT-4o-mini/NQ | S+MIS | 68.6% | 60.8% | 67.4% | 68.6% |
| GPT-4o-mini/NQ | RobustRAG | 63.4% | 60.6% | 63.4% | 63.0% |

**Multi-position attacks (Figure 2, NQ, k=50):** With 40% document corruption at lower ranks, Sampling+MIS "shows decent performance, whereas RobustRAG collapses much faster."

The long-form biography generation results are particularly striking -- nearly 20 points better than RobustRAG, confirming the information-loss critique.

---

### 7. OpenReview Reviews (NeurIPS 2025)

**Decision:** Accept (poster). All four reviewers gave positive assessments after discussion.

**Reviewer praise:**
- "Translating document consistency into a rank-aware MIS problem is a novel, intuitive insight" -- considered a genuine methodological advance
- Good theory-practice balance: provides formal lambda-robustness guarantees while addressing computational barriers through scalable sampling
- Strong empirical performance: maintains high benign accuracy while outperforming baselines across attack types
- Defense-in-depth: combining NLI-based detection with ranking signals viewed favorably

**Reviewer criticisms / concerns:**
1. **NLI dependency:** Performance degrades in non-English or technical domains. Authors responded with experiments showing "graceful degradation" even with 50% NLI error probability.
2. **Multi-position attacks:** Initially underexplored in the main text; comprehensive analysis was relegated to the appendix. Reviewers wanted this more prominent.
3. **Computational overhead:** Sub-1-second latency acknowledged as unoptimized; authors proposed parallelization improvements.
4. **Parameter tuning:** Sampling parameters (gamma, T, m) are set heuristically without full theoretical justification for specific values.

**Author responses addressed:**
- NLI robustness experiments showing graceful performance drops
- Lexical matching experiments demonstrating its insufficiency (less than 4.31% attack failure rate even at optimal threshold -- justifying the NLI-based approach over simpler lexical methods)
- Multiple-choice dataset validation confirming LLM-judge reliability
- Latency analysis and optimization pathways

No unresolved fatal flaws were identified; all reviewers affirmed positive assessments.

---

### 8. Acknowledged Limitations

1. **Ambiguous queries:** Assumes a "consistent majority" exists among benign documents. Fails on queries where legitimate documents genuinely disagree or the question is subjective.
2. **Scalability:** Exact MIS requires exponential time (2^Omega(|V|) under ETH). The sampling heuristic is needed for k >> 20, but trades exact optimality for feasibility.
3. **Domain specificity of reliability signals:** Framework is designed for web search where ranking signals exist. Applicability to other RAG domains (e.g., enterprise document stores without ranking) is unclear.
4. **NLI model quality:** Performance degrades with weaker contradiction detection models. Domain-specific or multilingual NLI may be needed.
5. **Long-form generation beyond tested tasks:** Applicability to more complex generation tasks than those evaluated remains uncertain.
6. **Assumes consistent malicious behavior:** Adversarial documents are assumed to produce outputs that consistently contradict benign ones. Sophisticated adversaries crafting subtly aligned-but-wrong content might evade detection.

---

### 9. Key Takeaways for Your Research

- The paper's core contribution is showing that **reliability signals from search engines** (which existing defenses ignore) can be leveraged through a principled graph-theoretic framework
- The MIS formulation is elegant but the practical applicability hinges on NLI quality and the assumption that adversarial documents contradict benign ones
- The certified guarantee (1 - e^(-Omega(k))) is strong but requires the 20% corruption bound (k' <= k/5) and bounded NLI error rates
- The sampling+aggregation extension for scalability is practical but the theoretical guarantees become probabilistic rather than deterministic
- The 14-19 point improvement over RobustRAG on long-form generation is the most compelling empirical result, directly validating the information-loss critique

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a936287-9344-4f87-91bf-69527178be32",
  "isSidechain": true,
  "agentId": "a620a8dbf50fd8bc7",
  "requestId": "req_011CbYHKUbQQgC6veFLavhtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "666bb8cf-2dc5-42cd-b566-43171f2bf7c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfFtPo1EGi7hUzvXUvtvwd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 22753,
      "output_tokens": 3354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3354,
          "cache_read_input_tokens": 22753,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1153,
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
