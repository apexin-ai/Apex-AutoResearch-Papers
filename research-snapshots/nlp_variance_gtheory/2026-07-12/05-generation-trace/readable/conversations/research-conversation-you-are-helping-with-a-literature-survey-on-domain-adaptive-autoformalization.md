# Research conversation: You are helping with a literature survey on domain-adaptive autoformalization for mathematical theorem proving (2024-202

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 1
- **Tool calls:** 44
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0e94d6bda196d649.jsonl`
- **Structured JSON:** [`3e6df760135c14ea4567.json`](../../sessions/3e/3e6df760135c14ea4567.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

101 recorded events

### User

_source line 1 · 2026-05-28T10:16:12.209Z_

You are helping with a literature survey on domain-adaptive autoformalization for mathematical theorem proving (2024-2026). 

Search for the most important recent papers on AUTOFORMALIZATION - converting natural language mathematics to formal proofs in Lean4/Isabelle/Coq. Focus on papers from 2024-2026.

Execute these searches and for EVERY promising paper, fetch its arXiv abstract:

1. Search: "autoformalization Lean4 2025 2026"
2. Search: "autoformalization language model mathematics 2025"
3. Search: "natural language to formal proof translation 2025 2026"
4. Search: "autoformalization benchmark evaluation 2025"
5. Search: "site:arxiv.org autoformalization Lean 2025"

For each paper found, use WebFetch on its arXiv page to get the title, authors, abstract, and date.

Key seed papers to be aware of (don't re-search these, but look for papers that cite or extend them):
- Herald (ICLR 2025) - 580k NL-formal pairs
- StepFun-Formalizer (AAAI 2026) - SOTA autoformalization
- DDR (arXiv 2511.11990) - retrieval-augmented autoformalization
- Autoformalizer with Tool Feedback (arXiv 2510.06857)
- APRIL (arXiv 2602.02990) - repair tuples

Report back with a list of papers found, including: title, authors, venue, URL, and a one-line summary of what the paper does. Focus on papers NOT in the seed list above.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "0402a8d6-2691-4bbf-8fb1-2f141f8b7476",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T10:16:12.213Z_

```json
{
  "parentUuid": "0402a8d6-2691-4bbf-8fb1-2f141f8b7476",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
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
  "uuid": "0640cadb-a8a3-46a2-9051-5c5360f928ed",
  "timestamp": "2026-05-28T10:16:12.213Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T10:16:12.213Z_

```json
{
  "parentUuid": "0640cadb-a8a3-46a2-9051-5c5360f928ed",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "606932ce-02e0-4269-81c6-e4f108d1b9f2",
  "timestamp": "2026-05-28T10:16:12.213Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T10:16:14.914Z_



I'll conduct a systematic literature search on autoformalization. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "606932ce-02e0-4269-81c6-e4f108d1b9f2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnx91pfea4SPRj2JUZ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97e6a6db-bf1a-416e-b510-7b15871e9f08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5h5zfEkXEGEhMn8fnQPb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9138,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9138,
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

_source line 5 · 2026-05-28T10:16:15.398Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MPzgAH1AJrT9MLN7ZmKayN`</summary>

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
  "parentUuid": "97e6a6db-bf1a-416e-b510-7b15871e9f08",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnx91pfea4SPRj2JUZ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "020944de-b958-4768-a2d0-915b39d90b9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5h5zfEkXEGEhMn8fnQPb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9138,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9138,
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

_source line 6 · 2026-05-28T10:16:15.406Z_

<details><summary>↩ Tool result · `toolu_01MPzgAH1AJrT9MLN7ZmKayN`</summary>

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
  "parentUuid": "020944de-b958-4768-a2d0-915b39d90b9e",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "93738cfa-90ab-45ac-b211-ac199feeae7d",
  "sourceToolAssistantUUID": "020944de-b958-4768-a2d0-915b39d90b9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T10:16:17.876Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93738cfa-90ab-45ac-b211-ac199feeae7d",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e55f8330-2b10-4c99-8443-a983c4db8714",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 8 · 2026-05-28T10:16:18.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJrvrzLY65MNunr7uLakk2`</summary>

```json
{
  "query": "autoformalization Lean4 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55f8330-2b10-4c99-8443-a983c4db8714",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2af000ed-acae-4ce0-9ad9-3b9a585ddfb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 9 · 2026-05-28T10:16:18.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HxWiT3L4pmJN98XnreYaW`</summary>

```json
{
  "query": "autoformalization language model mathematics 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2af000ed-acae-4ce0-9ad9-3b9a585ddfb0",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c999db3-5a68-4635-a59c-9e865b9f1bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 10 · 2026-05-28T10:16:19.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAb6ueB8mRPKouwnB14q2M`</summary>

```json
{
  "query": "natural language to formal proof translation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c999db3-5a68-4635-a59c-9e865b9f1bcb",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc33532a-70d4-4bf1-98f3-08c67b18691b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 11 · 2026-05-28T10:16:20.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ahqom8NYFzqjmzuyp8UfdG`</summary>

```json
{
  "query": "autoformalization benchmark evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc33532a-70d4-4bf1-98f3-08c67b18691b",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1ce13c8-afa3-456c-bc9e-8a6df02a4320",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 12 · 2026-05-28T10:16:20.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5zygm8fqP7dKUJdX4qCDE`</summary>

```json
{
  "query": "site:arxiv.org autoformalization Lean 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1ce13c8-afa3-456c-bc9e-8a6df02a4320",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnxP98J5ZnFcsc8CuM3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f228d1cb-26ad-455a-bf5f-da5a80cb926d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016njmNVbvWEp7abVmsD8Gwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 9138,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 9138,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 13 · 2026-05-28T10:16:27.001Z_

<details><summary>↩ Tool result · `toolu_01MAb6ueB8mRPKouwnB14q2M`</summary>

```text
Web search results for query: "natural language to formal proof translation 2025 2026"

Links: [{"title":"[2509.09726] Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure","url":"https://arxiv.org/abs/2509.09726"},{"title":"Transforming Natural Language Requirements to Formalism Using LLMs - Meng - 2026 - Systems Engineering - Wiley Online Library","url":"https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.70023"},{"title":"Natural Language Translation of Formal Proofs through ...","url":"https://aclanthology.org/2025.inlg-main.23.pdf"},{"title":"Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure","url":"https://arxiv.org/html/2509.09726v1"},{"title":"Natural Language to Formal Logic Translation","url":"https://www.emergentmind.com/topics/natural-language-to-formal-logic-translation"},{"title":"Transforming Natural Language into Formal Specifications (AgenticSE 2025) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/agenticse-2025-papers/6/Transforming-Natural-Language-into-Formal-Specifications"},{"title":"Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure","url":"https://arxiv.org/pdf/2509.09726"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"}]

I found several recent research results on natural language to formal proof translation from 2025-2026:

## Key Recent Work

**Natural Language Translation of Formal Proofs (2025)**
A paper proposes a natural language translation method for machine-verifiable formal proofs that leverages the informalization and summarization capabilities of LLMs. Autoformalization is a technology that automatically converts human-written proofs (natural language proofs) into formal proofs, reducing the burden of manually formalizing mathematical theorems.

**Transforming Natural Language Requirements to Formalism (2026)**
Researchers present an LLM-based approach to interactively translate unstructured natural language requirements to logical formalism, employing a NL-based interface that provides high assurance for translation correctness while still being approachable for nonexperts in formal methods. The effectiveness of the tool was demonstrated through an experimental evaluation of an industry use case—landing gear.

**ProofBridge Auto-Formalization (2025)**
Formalizing an entire NL proof requires first performing theorem-only auto-formalization to translate the NL theorem into formal language, followed by formal proof synthesis, as demonstrated by AlphaProof which achieved silver-medal standard in the 2024 International Mathematical Olympiad.

## Challenges
Challenges persist due to the lack of natural language proofs paired with formal proofs for model training, with targets remaining primarily on high school level mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc33532a-70d4-4bf1-98f3-08c67b18691b",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "6c367353-c42d-485a-a4b8-78d44e885a0f",
  "sourceToolAssistantUUID": "dc33532a-70d4-4bf1-98f3-08c67b18691b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T10:16:27.071Z_

<details><summary>↩ Tool result · `toolu_01Ahqom8NYFzqjmzuyp8UfdG`</summary>

```text
Web search results for query: "autoformalization benchmark evaluation 2025"

Links: [{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.907/"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"[2406.07222] Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/abs/2406.07222"},{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"Reliable Evaluation and Benchmarks for Statement ...","url":"https://aclanthology.org/2025.emnlp-main.907.pdf"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"}]

Based on the search results, here's what I found about autoformalization benchmark evaluation in 2025:

## Key Developments

Evaluating statement autoformalization—translating natural language mathematics into formal languages like Lean 4—remains a significant challenge, with few metrics, datasets, and standards to robustly measure progress. Recent work presents a comprehensive approach combining improved metrics, robust benchmarks, and systematic evaluation.

## Important Benchmarks and Metrics

A new automated metric called BEq+ correlates strongly with human judgment, along with ProofNetVerif, a new dataset for assessing autoformalization quality. Additionally, new benchmarks include a research-level mathematics dataset RLM25, a corrected ProofNet, and ProofNetVerif with labeled correct and incorrect autoformalization pairs for evaluating metrics.

The BEq (Bidirectional Extended Definitional Equivalence) metric extends Definition Equality in dependent type theory to be more aligned with human intuition. Recent methods include Generalized Tree Edit Distance (GTED) which computes structural similarity through operator trees, while Bidirectional Extended Definitional Equivalence (BEq) provides neural-symbolic equivalence checking.

## Recent Performance Improvements

Recent approaches achieve a 68.4% pass rate on benchmarks such as MiniF2F, with datasets containing 30,000 synthetic proof instances, each containing a natural language question, an automatically formalized Lean statement, and the corresponding proof.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1ce13c8-afa3-456c-bc9e-8a6df02a4320",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "7271ab1d-535a-4055-a14b-8360de1a9ed5",
  "sourceToolAssistantUUID": "a1ce13c8-afa3-456c-bc9e-8a6df02a4320",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T10:16:27.759Z_

<details><summary>↩ Tool result · `toolu_01PJrvrzLY65MNunr7uLakk2`</summary>

```text
Web search results for query: "autoformalization Lean4 2025 2026"

Links: [{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4 | OpenReview","url":"https://openreview.net/forum?id=22ITxc8y5p"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

Here are the key findings from recent research on autoformalization in Lean4 for 2025-2026:

## Recent Papers and Research

A March 2026 paper on "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning" focuses on automatically translating natural language mathematical texts into formal proof language such as Lean4 to help accelerate AI-assisted mathematical research. The approach involves fine-tuning Qwen3.5-2B with LoRA for natural language to Lean4 formalization using reinforcement learning with cycle consistency rewards.

The FormL4 benchmark was introduced to evaluate autoformalization in Lean 4, along with a process-supervised verifier that enhances the accuracy of LLMs in converting informal statements and proofs into formal ones. Autoformalization offers significant potential for advancing mathematical reasoning.

## Major Breakthroughs in 2025

In 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs on the International Mathematical Olympiad. 5 out of 6 IMO 2025 problems were solved with formally verified proofs.

Using an autoformalization system called Gauss, the strong Prime Number Theorem in Lean was completed in just three weeks, a task that had stalled after 18+ months of human expert effort.

Nearly all major advances use reinforcement learning with formal verification as the reward.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2af000ed-acae-4ce0-9ad9-3b9a585ddfb0",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "0842f68a-a6f4-4c6e-98ef-b635b8b65369",
  "sourceToolAssistantUUID": "2af000ed-acae-4ce0-9ad9-3b9a585ddfb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T10:16:28.291Z_

<details><summary>↩ Tool result · `toolu_01K5zygm8fqP7dKUJdX4qCDE`</summary>

```text
Web search results for query: "site:arxiv.org autoformalization Lean 2025"

Links: [{"title":"arXiv:2406.03847v3 [cs.CL] 18 Jun 2025","url":"https://arxiv.org/pdf/2406.03847v3"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

Based on the search results for "site:arxiv.org autoformalization Lean 2025", here are the relevant papers found:

1. **Lean Workbook** (2406.03847): This paper presents Lean Workbook: an iterative autoformalization pipeline, together with a large-scale Lean problem set. The autoformalization model is trained based on active learning, using the model to translate natural language problems into formal statements.

2. **ProofBridge** (2510.15681): ProofBridge is a unified framework for automatically translating entire NL theorems and proofs into Lean 4. At its core is a joint embedding model that aligns NL and FL (NL-FL) theorem+proof pairs in a shared semantic space.

3. **Autoformalization Survey** (2505.23486): Recent work achieves 68.4% pass rate on benchmarks such as MiniF2F. Additionally, large-scale LLM was used to automatically translate natural language math problems into Lean 4 formal statements, and the Goedel-Pset-v1 dataset containing 1.64M formulative statements was generated.

4. **Process-Driven Autoformalization in Lean 4** (2406.01940): The paper introduces a Process-Supervised Verifier (PSV) model that leverages feedback from Lean 4 compilers to enhance autoformalization, improving accuracy using less filtered training data.

5. **130k Lines of Formal Topology in Two Weeks** (2601.03298): Recent work managed to finish a full Lean proof with an LLM-based agent, and a stable setup has been used for automated formalization resulting in about 130k lines of code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f228d1cb-26ad-455a-bf5f-da5a80cb926d",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "01301c14-8703-46f9-8eeb-63d88c7755c5",
  "sourceToolAssistantUUID": "f228d1cb-26ad-455a-bf5f-da5a80cb926d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T10:16:29.062Z_

<details><summary>↩ Tool result · `toolu_015HxWiT3L4pmJN98XnreYaW`</summary>

```text
Web search results for query: "autoformalization language model mathematics 2025"

Links: [{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"[2505.23486] Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/abs/2505.23486"},{"title":"Autoformalization in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.23486"},{"title":"[2509.09810] Towards a Common Framework for Autoformalization","url":"https://arxiv.org/abs/2509.09810"},{"title":"eprints@whiterose.ac.uk https://eprints.whiterose.ac.uk","url":"https://eprints.whiterose.ac.uk/id/eprint/234717/1/2025.emnlp-main.90.pdf"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"RLMEval: Evaluating Autoformalization on Research-Level Mathematics","url":"http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"},{"title":"[2205.12615] Autoformalization with Large Language Models","url":"https://arxiv.org/abs/2205.12615"}]

Based on the search results, here's what's happening with autoformalization, language models, and mathematics in 2025:

## Definition and Overview

Autoformalization with LLMs is the automated translation of informal mathematical, logical, or scientific statements—typically expressed in everyday language or domain text—into formal representations suitable for machine reasoning, verification, or symbolic manipulation. More specifically, autoformalization is the process of transforming informal mathematical propositions into verifiable formal representations, which is a foundational task in automated theorem proving.

## Recent Progress and Methods

The rapid development of LLMs has fundamentally changed the landscape of autoformalization across mathematics, logic programming, game theory, and applied domains. 

In 2025, several advanced methodologies have emerged:

- **Process-Driven Approaches**: Process-driven autoformalization (FormL4+PSV) uses stepwise compiler traces, labeling each tactic as correct/incorrect, while the Process-Supervised Verifier (PSV) filters and ranks candidate formalizations, improving accuracy and sample efficiency.

- **Data-Centric Methods**: On-the-fly and distilled backtranslation, as well as line-by-line proof state analysis, have demonstrated superior results for Lean4 formalization.

- **Self-Improvement Frameworks**: Recent work explores a framework in which a model validates its own output, filtering or reweighting the data and extracting filtered data to initiate a comprehensive, modular and controlled LLM self-improvement study.

## Applications and Benchmarks

The autoformalization of mathematics shows broad application prospects and theoretical value in multiple dimensions. Recent 2025 research includes studies assessing LLMs on real-world mathematical definitions presented at the 2025 Conference on Empirical Methods in Natural Language Processing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c999db3-5a68-4635-a59c-9e865b9f1bcb",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "369487b1-a47a-4471-beb7-840d1b6bf2c0",
  "sourceToolAssistantUUID": "7c999db3-5a68-4635-a59c-9e865b9f1bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-28T10:16:31.750Z_

Excellent. I found many promising papers. Now let me fetch the arXiv abstracts for all unique papers. Let me start with the first batch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "369487b1-a47a-4471-beb7-840d1b6bf2c0",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0efdddf-40d4-4033-b52f-1dbb8337278e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 19 · 2026-05-28T10:16:32.706Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VobGQQfmt7gFSYcBzyhKKr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.24372",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0efdddf-40d4-4033-b52f-1dbb8337278e",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7574e28f-aa30-4b5e-9c5d-eca2187965b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 20 · 2026-05-28T10:16:33.654Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wbe42pxHn9GyhE8rThHaHA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.01940",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7574e28f-aa30-4b5e-9c5d-eca2187965b0",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c14960af-c645-4a32-a974-97b0a39ba03b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 21 · 2026-05-28T10:16:34.129Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KvgvuzBAyMqGte61msfHKR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23486",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c14960af-c645-4a32-a974-97b0a39ba03b",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5285caad-d427-483b-a282-6c572295cae7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 22 · 2026-05-28T10:16:35.072Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SAewdXJGkdP1rrNqwhrtwj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.09810",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5285caad-d427-483b-a282-6c572295cae7",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "938775dd-2388-4eeb-b499-76be8e4685bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 23 · 2026-05-28T10:16:35.550Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012V4JyPN1orUDEvP95qF1Jy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.15681",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "938775dd-2388-4eeb-b499-76be8e4685bc",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "006cdad1-170b-4c51-af8f-690a107945e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 24 · 2026-05-28T10:16:36.022Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QwMnYdHHFoggZ2EDZp57fk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.07222",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "006cdad1-170b-4c51-af8f-690a107945e7",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69b8eb01-4eae-4d14-9191-23b18487462a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 25 · 2026-05-28T10:16:36.960Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CpW5d27Jqas65YPWmmg5wD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.09726",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b8eb01-4eae-4d14-9191-23b18487462a",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa4411fb-fea3-4a36-8a23-e4f4dbb86c5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 26 · 2026-05-28T10:16:37.399Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0182CZ9Z5nkPXKtAwqQmRSwL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03298",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa4411fb-fea3-4a36-8a23-e4f4dbb86c5c",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9233aaff-cdac-47bd-a09f-204d03bd459b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 27 · 2026-05-28T10:16:37.862Z_

<details><summary>↩ Tool result · `toolu_01VobGQQfmt7gFSYcBzyhKKr`</summary>

```text
# arXiv Paper Details

**Title:** "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning"

**Author:** Arsen Shebzukhov

**Submission Date:** March 25, 2026

**Abstract Summary:**

The paper addresses autoformalization—converting mathematical text from natural language into the Lean4 formal proof language. The researcher fine-tuned Qwen3.5-2B using LoRA on FineLeanCorpus, comparing three approaches: supervised fine-tuning with curriculum learning, supervised fine-tuning without curriculum ordering, and reinforcement learning with group relative policy optimization (GRPO) using cycle consistency rewards.

Cycle consistency evaluates meaning preservation through a "NL to Lean4 to NL' loop" using sentence embeddings. Results showed reinforcement learning substantially outperformed supervised variants, achieving "mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench," with minimal quality degradation despite increased cross-entropy loss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7574e28f-aa30-4b5e-9c5d-eca2187965b0",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "89c560d1-bf3c-4ec8-9e5f-b8c1223b04f7",
  "sourceToolAssistantUUID": "7574e28f-aa30-4b5e-9c5d-eca2187965b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T10:16:37.618Z_

<details><summary>↩ Tool result · `toolu_01Wbe42pxHn9GyhE8rThHaHA`</summary>

```text
# Process-Driven Autoformalization in Lean 4

**Title:** "Process-Driven Autoformalization in Lean 4"

**Authors:** Jianqiao Lu, Yingjia Wan, Zhengying Liu, Yinya Huang, Jing Xiong, Chengwu Liu, Jianhao Shen, Hui Jin, Jipeng Zhang, Haiming Wang, Zhicheng Yang, Jing Tang, and Zhijiang Guo

**Submission Date:** June 4, 2024 (v1); last revised October 14, 2024 (v2)

**Abstract:** The paper introduces a benchmark called FormL4 for evaluating how well large language models can convert natural language mathematics into Lean 4 formal code. The authors present a "Process-Supervised Verifier" model that uses compiler feedback to improve this conversion process. Their approach demonstrates enhanced performance with less filtered training data and particularly benefits from detailed process information in training examples.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c14960af-c645-4a32-a974-97b0a39ba03b",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "87292617-66f2-419b-b6cd-0f40a558ef83",
  "sourceToolAssistantUUID": "c14960af-c645-4a32-a974-97b0a39ba03b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T10:16:37.772Z_

<details><summary>↩ Tool result · `toolu_01KvgvuzBAyMqGte61msfHKR`</summary>

```text
# Autoformalization Survey Paper

**Title:** "Autoformalization in the Era of Large Language Models: A Survey"

**Authors:** Ke Weng, Lun Du, Sirui Li, Wangyue Lu, Haozhe Sun, Hengyu Liu, and Tiancheng Zhang

**Submission Date:** May 29, 2025 (v1); Last revised July 3, 2025 (v2)

**Abstract:** The paper examines how informal mathematical statements are converted into formal, verifiable representations using large language models. It surveys recent progress in this field, covering applications across different mathematical domains and difficulty levels. The work analyzes the complete workflow from data preparation through model development and assessment, while exploring how autoformalization can enhance the reliability and reasoning abilities of LLM-generated content. The authors also summarize available open-source tools and datasets and identify remaining challenges and opportunities for future research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5285caad-d427-483b-a282-6c572295cae7",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "0bc698ba-0600-4dfa-a0de-bdf31001d73d",
  "sourceToolAssistantUUID": "5285caad-d427-483b-a282-6c572295cae7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-28T10:16:37.904Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Btz7an2w85gpzVZ4U5oJQb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.03847",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bc698ba-0600-4dfa-a0de-bdf31001d73d",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa649c7b-ae41-4a50-8184-9b23b306c0a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 31 · 2026-05-28T10:16:38.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016y6jHndQvMmLquonhk2PAF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.12784",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa649c7b-ae41-4a50-8184-9b23b306c0a2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnyP3ChvaoPB1m28npE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04e666ff-7c0f-4ad8-bab2-04e91d4519fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sbNGYLdjuRMYGZRJBU8Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2420,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 10267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1843,
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

_source line 32 · 2026-05-28T10:16:39.338Z_

<details><summary>↩ Tool result · `toolu_01SAewdXJGkdP1rrNqwhrtwj`</summary>

```text
# arXiv Paper Summary

**Title:** "Towards a Common Framework for Autoformalization"

**Authors:** Agnieszka Mensfelt, David Tena Cucala, Santiago Franco, Angeliki Koutsoukou-Argyraki, Vince Trencsenyi, Kostas Stathis

**Submission Date:** September 11, 2025 (v1); last revised December 15, 2025 (v3)

**Abstract:** The paper addresses how autoformalization—converting informal language into formal logical representations—has developed across multiple fields without sufficient cross-pollination. The researchers observe that "despite addressing similar tasks, the largely independent development of these research areas has limited opportunities for shared methodologies, benchmarks, and theoretical frameworks." They propose establishing a unified framework to bridge work in mathematical formalization using theorem provers, LLM-based reasoning systems, and knowledge representation to accelerate progress in AI development.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "938775dd-2388-4eeb-b499-76be8e4685bc",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "f4441700-519a-476e-abfe-4451a385e01c",
  "sourceToolAssistantUUID": "938775dd-2388-4eeb-b499-76be8e4685bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T10:16:39.933Z_

<details><summary>↩ Tool result · `toolu_012V4JyPN1orUDEvP95qF1Jy`</summary>

```text
# ProofBridge Paper Details

**Title:** "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings"

**Authors:** Prithwish Jana, Kaan Kale, Ahmet Ege Tanriverdi, Cruise Song, Sriram Vishwanath, and Vijay Ganesh

**Submission Date:** October 17, 2025 (v1); most recent version (v3) on March 29, 2026

**Abstract Summary:** The paper addresses the challenge of converting human-written mathematical theorems and proofs into formal languages like Lean 4. ProofBridge uses a joint embedding model to align natural language and formal language theorem-proof pairs in a shared semantic space. This enables "retrieval-augmented fine-tuning with iterative proof repair," leveraging type checking to ensure correctness. Results demonstrate substantial improvements over existing approaches including GPT-5 and Gemini-2.5, with gains of "+31.14% SC and +1.64% TC (pass@32)" compared to baseline methods on the miniF2F-Test-PF dataset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "006cdad1-170b-4c51-af8f-690a107945e7",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "4060c57b-8ca0-4882-a397-9fbbeec16983",
  "sourceToolAssistantUUID": "006cdad1-170b-4c51-af8f-690a107945e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T10:16:40.192Z_

<details><summary>↩ Tool result · `toolu_01QwMnYdHHFoggZ2EDZp57fk`</summary>

```text
# Paper Information

**Title:** "Reliable Evaluation and Benchmarks for Statement Autoformalization"

**Authors:** Auguste Poiroux, Gail Weiss, Viktor Kunčak, and Antoine Bosselut

**Submission Date:** June 11, 2024 (v1); last revised October 29, 2025 (v3)

**Abstract Summary:** 

The researchers tackle the challenge of evaluating systems that convert natural language mathematics into formal languages like Lean 4. They introduce BEq+, an evaluation metric aligned with human judgment, plus ProofNetVerif—a dataset containing 3,752 annotated examples for assessing metric quality. The team also developed two new benchmarks: ProofNet# (a corrected version of ProofNet) and RLM25, featuring 619 research-level mathematics pairs from six formalization projects. Their findings show current methods achieve approximately 45% accuracy on undergraduate mathematics but face difficulties with research-level content lacking proper context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69b8eb01-4eae-4d14-9191-23b18487462a",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "019c587c-f9da-49a9-acd6-f0a02db3db70",
  "sourceToolAssistantUUID": "69b8eb01-4eae-4d14-9191-23b18487462a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T10:16:40.710Z_

<details><summary>↩ Tool result · `toolu_01CpW5d27Jqas65YPWmmg5wD`</summary>

```text
# arXiv Paper Summary

**Title:** "Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure"

**Authors:** Seiji Hattori, Takuya Matsuzaki, Makoto Fujiwara

**Submission Date:** September 10, 2025

**Abstract:** The paper introduces a methodology for converting machine-verifiable formal proofs into natural language. It combines "informalization (verbalization of formal language proof steps) and summarization capabilities of LLMs." The researchers tested their approach using formal proofs derived from undergraduate textbooks and evaluated the output against original natural language versions. They also demonstrated the method's effectiveness on existing Lean proof assistant libraries, showing it can generate "highly readable and accurate natural language proofs."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa4411fb-fea3-4a36-8a23-e4f4dbb86c5c",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "1bd151a1-e85c-4a42-8107-9fcafd2e8193",
  "sourceToolAssistantUUID": "aa4411fb-fea3-4a36-8a23-e4f4dbb86c5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T10:16:41.272Z_

<details><summary>↩ Tool result · `toolu_016y6jHndQvMmLquonhk2PAF`</summary>

```text
# arXiv Paper Summary

**Title:** "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing"

**Authors:** Hayden Moore and Asfahan Shah

**Submission Date:** November 16, 2025 (v1); December 4, 2025 (v2)

**Abstract Summary:** The paper investigates whether large language models remain reliable when generating formal proofs from paraphrased natural language inputs. The researchers tested two modern LLMs using established benchmarks and found that "minor shifts in NL statements can significantly impact model outputs," indicating performance variability across semantically equivalent phrasings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04e666ff-7c0f-4ad8-bab2-04e91d4519fd",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "153903e7-b0e0-4d2e-994a-8b26dabde764",
  "sourceToolAssistantUUID": "04e666ff-7c0f-4ad8-bab2-04e91d4519fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T10:16:41.804Z_

<details><summary>↩ Tool result · `toolu_01Btz7an2w85gpzVZ4U5oJQb`</summary>

```text
# Lean Workbook arXiv Paper

**Title:** "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems"

**Authors:** Huaiyuan Ying, Zijian Wu, Yihan Geng, Zheng Yuan, Dahua Lin, Kai Chen

**Submission Date:** June 6, 2024 (v1); last revised June 18, 2025 (v3)

**Abstract Summary:**
The paper addresses the scarcity of formal language training data by proposing "a novel pipeline that iteratively generates and filters synthetic data to translate natural language mathematical problems into Lean 4 statements." The researchers created a dataset containing approximately 57,000 formal-informal question pairs sourced from math contest forums and 21 new IMO questions. They demonstrate that this synthetic data improves large language models' performance in translating and understanding mathematical problems and proofs. The code and data have been made publicly available through GitHub and Hugging Face.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa649c7b-ae41-4a50-8184-9b23b306c0a2",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "7455bd88-6cfb-4cca-b3b0-8421b2be64d6",
  "sourceToolAssistantUUID": "aa649c7b-ae41-4a50-8184-9b23b306c0a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T10:16:42.021Z_

<details><summary>↩ Tool result · `toolu_0182CZ9Z5nkPXKtAwqQmRSwL`</summary>

```text
# arXiv Paper Summary

**Title:** "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?"

**Author:** Josef Urban

**Submission Date:** January 6, 2026

**Abstract Summary:**

This project demonstrates automated formalization of general topology from the Munkres textbook, producing approximately 160,000 lines of formal code since November 2025. Within a two-week period ending January 4, 2026, the effort generated roughly 130,000 lines at a cost of approximately $100 using LLM subscriptions.

Key achievements include formal proofs of significant theorems such as Urysohn's lemma (3,000 lines), Urysohn's Metrization theorem (2,000 lines), and the Tietze extension theorem (10,000+ lines), along with over 1,500 additional lemmas and theorems.

The approach uses a feedback loop between language models (ChatGPT or Claude Sonnet) and Chad Brown's Megalodon proof checker, leveraging a foundational library of set theory. The authors argue this demonstrates that formalization could become accessible and widespread in 2026 across various proof assistants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9233aaff-cdac-47bd-a09f-204d03bd459b",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "a3b63ab3-274e-4e14-b0ad-dfb3ae382d57",
  "sourceToolAssistantUUID": "9233aaff-cdac-47bd-a09f-204d03bd459b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-28T10:16:45.927Z_

Good, I have detailed information on many papers. Let me now search for additional papers I may have missed, particularly those related to the seed papers and other recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3b63ab3-274e-4e14-b0ad-dfb3ae382d57",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnzLVSH7G5FTh17etJn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1566a5b1-557e-4cb2-8131-268d1d4d67c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiqLNn174KGxAJJEDnErs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 427,
      "cache_creation_input_tokens": 10121,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10121,
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

_source line 40 · 2026-05-28T10:16:46.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VntnEKrveeHQQ5yqbAJHZ7`</summary>

```json
{
  "query": "autoformalization retrieval augmented formal proof 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1566a5b1-557e-4cb2-8131-268d1d4d67c4",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnzLVSH7G5FTh17etJn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aafd4f2b-af9d-461c-ab33-98028da09c18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiqLNn174KGxAJJEDnErs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 427,
      "cache_creation_input_tokens": 10121,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10121,
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

_source line 41 · 2026-05-28T10:16:47.262Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XpFiSu5f6yGsFPmfDhtx4c`</summary>

```json
{
  "query": "autoformalization self-improvement reinforcement learning formal verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aafd4f2b-af9d-461c-ab33-98028da09c18",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnzLVSH7G5FTh17etJn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1326552-79a8-49f9-beb5-8904736098fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiqLNn174KGxAJJEDnErs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 427,
      "cache_creation_input_tokens": 10121,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10121,
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

_source line 42 · 2026-05-28T10:16:47.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMqeWP7iv2NTKFn6fDnXoj`</summary>

```json
{
  "query": "\"domain adaptive\" autoformalization mathematical proof 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1326552-79a8-49f9-beb5-8904736098fe",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnzLVSH7G5FTh17etJn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5d0afbc-5bb8-4b20-85ec-f8eabe857b60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiqLNn174KGxAJJEDnErs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 427,
      "cache_creation_input_tokens": 10121,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10121,
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

_source line 43 · 2026-05-28T10:16:48.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KbjjJ4EJMut8MTUSTjQoBQ`</summary>

```json
{
  "query": "autoformalization data synthesis backtranslation formal proof 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5d0afbc-5bb8-4b20-85ec-f8eabe857b60",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUnzLVSH7G5FTh17etJn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0af31671-15bd-41a4-b262-51291edcf820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiqLNn174KGxAJJEDnErs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 427,
      "cache_creation_input_tokens": 10121,
      "cache_read_input_tokens": 7407,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 427,
          "output_tokens": 244,
          "cache_read_input_tokens": 7407,
          "cache_creation_input_tokens": 10121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10121,
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

_source line 44 · 2026-05-28T10:16:52.768Z_

<details><summary>↩ Tool result · `toolu_01VntnEKrveeHQQ5yqbAJHZ7`</summary>

```text
Web search results for query: "autoformalization retrieval augmented formal proof 2025 arxiv"

Links: [{"title":"[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/abs/2511.11990"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"TOWARDS AUTOFORMALIZATION OF LLM-GENERATED OUTPUTS FOR REQUIREMENT VERIFICATION","url":"https://arxiv.org/pdf/2511.11829"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/html/2511.11990v2"},{"title":"arXiv:2505.23486v2 [cs.AI] 3 Jul 2025","url":"https://arxiv.org/pdf/2505.23486"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/abs/2508.06931"}]

I found several relevant papers on arXiv about autoformalization with retrieval-augmented approaches from 2025:

1. **"Improving Autoformalization Using Direct Dependency Retrieval"** (arXiv:2511.11990, November 2025)
   - Proposes a novel retrieval-augmented framework based on DDR (Direct Dependency Retrieval) for statement autoformalization

2. **"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings"** (arXiv:2510.15681, October 2025)
   - Integrates retrieval-augmented fine-tuning with iterative proof repair, leveraging Lean's type checker and semantic equivalence feedback
   - Shows improvements in proof auto-formalization with retrieval-augmented approach yielding gains in semantic correctness and type correctness

3. **"Automated Formalization via Conceptual Retrieval-Augmented LLMs"** (arXiv:2508.06931, August 2025)
   - CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation
   - Experiments show consistent improvements in translation accuracy, achieving up to 62.1% and an average of 29.9% relative improvement

4. **"Autoformalization in the Era of Large Language Models: A Survey"** (arXiv:2505.23486, May 2025)
   - A comprehensive survey covering retrieval-augmented approaches and other recent developments in the field

These papers represent the cutting edge of research combining autoformalization with retrieval-augmented methods in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aafd4f2b-af9d-461c-ab33-98028da09c18",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "02e3e74a-771d-439b-b9ea-8c3c807e1a78",
  "sourceToolAssistantUUID": "aafd4f2b-af9d-461c-ab33-98028da09c18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T10:16:55.475Z_

<details><summary>↩ Tool result · `toolu_01SMqeWP7iv2NTKFn6fDnXoj`</summary>

```text
Web search results for query: ""domain adaptive" autoformalization mathematical proof 2025"

Links: [{"title":"Autoformalization of Mathematics","url":"https://www.emergentmind.com/topics/autoformalization-of-mathematics"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"Autoformalization in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.23486"},{"title":"Automated Theorem Proving Systems","url":"https://www.emergentmind.com/topics/automated-theorem-proving-atp-systems"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"Towards Autoformalization of Mathematics and Code Correctness:   Experiments with Elementary Proofs","url":"https://arxiv.org/pdf/2301.02195"}]

Based on the search results, here's what I found about domain adaptive autoformalization and mathematical proof in 2025:

## Recent Developments in Autoformalization

Autoformalization is the task of automatically translating informal mathematical content—typically written in human natural language or LaTeX—into formal statements or proofs in a machine-verifiable proof assistant language.

### Domain Adaptation Approaches

Practical autoformalization workflows use few-shot prompting with domain-rich exemplars and model-specific token augmentation for robustness. Carefully engineered prompts and in-context retrieval methods further improve performance, especially when tailored to the mathematical domain at hand.

### Current Challenges

Geometry and combinatorics often lack the necessary corpus for high-quality training, with PDE control marking early progress in applied mathematics autoformalization. Additionally, fully automated approaches continue to struggle with semantic consistency, complex mathematical reasoning, and the domain gap between natural language and formal specifications.

### Advanced Systems

Systems like ATF employ iterative, tool-augmented NL-to-formal translation with multi-pass generation plus tool calls including Lean 4 syntax validation and LLM-ensemble semantic checks, with training through Cold-start on synthetic tool-calling dialogues and Direct Preference Optimization.

### Future Directions

Promising future directions include hybrid symbolic–neural semantic checkers, extraction of broader multi-modal corpora, curriculum learning for difficulty-adaptive reflection, and cross-assistant transfer protocols.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5d0afbc-5bb8-4b20-85ec-f8eabe857b60",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "845b6f24-4be2-4fd1-8e4e-f9a341418317",
  "sourceToolAssistantUUID": "a5d0afbc-5bb8-4b20-85ec-f8eabe857b60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T10:16:57.293Z_

<details><summary>↩ Tool result · `toolu_01XpFiSu5f6yGsFPmfDhtx4c`</summary>

```text
Web search results for query: "autoformalization self-improvement reinforcement learning formal verification 2025"

Links: [{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Autoformalization and Formally Verifiable AI | Big AI Dream | Jie Fu","url":"https://bigaidream.github.io/project/auto/"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/html/2510.24592"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"(PDF) Towards Autoformalization of LLM-generated Outputs for Requirement Verification","url":"https://www.researchgate.net/publication/397700246_Towards_Autoformalization_of_LLM-generated_Outputs_for_Requirement_Verification"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"}]

Based on the search results, here's what I found on autoformalization, self-improvement, reinforcement learning, and formal verification in 2025:

## Key Developments in 2025

**Reinforcement Learning in Autoformalization**

Recent work has introduced reinforcement learning and subgoal decomposition techniques, where models like DeepSeek V3 decompose complex problems into subgoals, then combine proof processes with stepwise reasoning to form complete solution chains for cold start reinforcement learning training. This approach achieved an 88.9% pass rate on the MiniF2F test set and solved 49 problems on PutnamBench.

**Self-Improvement with Formal Verification**

Song et al. (2025) explores a framework where a model validates its own output, filters or reweights data, and initiates LLM self-improvement controlled by a formal generative validation gap (GV-Gap). 

The interweaving of autoformalization and self-validation creates a virtuous cycle where autoformalization capability develops semantic awareness by learning from self-validation, while self-validation becomes more adept at identifying errors, standing in contrast to traditional one-pass approaches.

**FormaRL: Data-Efficient RL Approach**

FormaRL improved autoformalization accuracy by a factor of 4–6 (from 4.04% to 26.15%) with only 859 unlabeled training examples. Its RL-trained formalizer outperforms open-source state-of-the-art autoformalizers such as DeepSeek-Math-7B in both in-distribution and out-of-distribution benchmarks.

**General Progress in Autoformalization**

Autoformalization (converting natural language content into verifiable formalization) is considered a promising way of learning general purpose reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1326552-79a8-49f9-beb5-8904736098fe",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "7648487c-8e34-4710-88a1-d2c6f83dd837",
  "sourceToolAssistantUUID": "a1326552-79a8-49f9-beb5-8904736098fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T10:16:57.546Z_

<details><summary>↩ Tool result · `toolu_01KbjjJ4EJMut8MTUSTjQoBQ`</summary>

```text
Web search results for query: "autoformalization data synthesis backtranslation formal proof 2025"

Links: [{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Translating Natural Language into Lean 4 through Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.1586v2.pdf"},{"title":"Autoformalization with Backtranslation: Training an Automated Mathematician","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/JakobNordhagen.pdf"},{"title":"Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual   Data in AutoFormalization","url":"https://arxiv.org/pdf/2502.15795"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://arxiv.org/pdf/2502.05567"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"}]

I found relevant search results about autoformalization, data synthesis, backtranslation, and formal proofs from 2025. Here's what the research shows:

## Data Synthesis Through Backtranslation

Synthetic data is generated by informalizing large-scale formal corpora (e.g., using GPT-4 to generate natural language from formal Lean/Isabelle) and backtranslating these into the formal domain—a strategy that enables scaling training. Researchers synthesize informal-formal pairs by rule-based informalization, LLM-based back-translation, training with multilingual corpus, or utilizing in-context learning capabilities.

## Data Quality Emphasis

Recent 2025 research emphasizes quality over quantity. Quality-first data generation (distilled backtranslation, line-wise proof state annotation) yields substantially better token efficiency and accuracy than training on large, diverse, but loosely aligned datasets. High-fidelity, backtranslated paired datasets significantly outperform large but less curated corpora, with on-the-fly and distilled backtranslation and line-by-line proof state analysis demonstrating superior results for Lean4 formalization.

## Performance Improvements

A 2025 approach generates new training samples through a scalable data synthesis framework with a guided tree search algorithm, achieving 68.4% pass rate on benchmarks such as MiniF2F. This research has published a dataset containing 30,000 synthetic proof instances, each with a natural language question, an automatically formalized Lean statement, and the corresponding proof.

## Multi-Agent and Process-Level Approaches

MASA demonstrates modular multi-agent designs with specialized agents: AutoformalizationAgent performs NL→formal mapping, CritiqueAgents invoke theorem provers and LLM judges, RefinementAgents apply provable or semantic corrections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0af31671-15bd-41a4-b262-51291edcf820",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "e7ccaedf-a71f-4e81-8221-f988a91adab2",
  "sourceToolAssistantUUID": "0af31671-15bd-41a4-b262-51291edcf820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-28T10:16:59.615Z_

Let me fetch the abstracts for the additional papers I discovered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7ccaedf-a71f-4e81-8221-f988a91adab2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5cd0ad3-dc0a-4dd6-a623-0e202c8e4b5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 49 · 2026-05-28T10:17:00.589Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017Hyn3PkNbKi3DqqwuG5ZLG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.06931",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cd0ad3-dc0a-4dd6-a623-0e202c8e4b5d",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c7a460-db81-4ec3-8679-76d16003d1a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 50 · 2026-05-28T10:17:01.510Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014TBrjeKxm2xRBQkBcKmBFG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.24592",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c7a460-db81-4ec3-8679-76d16003d1a6",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a2bbc4-d383-46f4-9202-90ed9c142068",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 51 · 2026-05-28T10:17:02.011Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N5ite34FNVDDvY61XWHm72`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.18914",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a2bbc4-d383-46f4-9202-90ed9c142068",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "864aacbd-139f-47a3-8607-9d01079420a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 52 · 2026-05-28T10:17:02.954Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VNomyX1U33guto6T6YXeCm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.15795",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "864aacbd-139f-47a3-8607-9d01079420a2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3092f39-df68-4c55-b521-e483bc7b86d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 53 · 2026-05-28T10:17:03.426Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017aEhraYDSJMhTqvqWY9QxS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.05567",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3092f39-df68-4c55-b521-e483bc7b86d5",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a1c14ee-4c83-4f64-b7cd-bbda60764b86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 54 · 2026-05-28T10:17:04.382Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VksAFEcoedU7fmuegBow75`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.06555",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a1c14ee-4c83-4f64-b7cd-bbda60764b86",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b343274-84a9-43f7-bc51-e89035de15b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3964,
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

_source line 55 · 2026-05-28T10:17:04.463Z_

<details><summary>↩ Tool result · `toolu_017Hyn3PkNbKi3DqqwuG5ZLG`</summary>

```text
# Paper Information

**Title:** "Automated Formalization via Conceptual Retrieval-Augmented LLMs"

**Authors:** Wangyue Lu, Lun Du, Sirui Li, Ke Weng, Haozhe Sun, Hengyu Liu, Minghe Yu, Tiancheng Zhang, and Ge Yu

**Submission Date:** August 9, 2025 (v1); revised March 21, 2026 (v2)

**Abstract Summary:**
The research addresses challenges in automated formalization for interactive theorem provers. The team proposes CRAMF, a framework that enhances LLM-based formalization by retrieving definitions of core mathematical concepts to reduce hallucination and bridge semantic gaps. The system constructs a knowledge base from Mathlib4 containing over 26,000 definitions and uses contextual query augmentation plus hybrid retrieval strategies. Testing showed improvements of up to 62.1% relative accuracy gain across multiple benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c7a460-db81-4ec3-8679-76d16003d1a6",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "3286cfe5-fce2-4c1b-a52d-9d5c58f48ce3",
  "sourceToolAssistantUUID": "46c7a460-db81-4ec3-8679-76d16003d1a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T10:17:05.403Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JWSRig1Y3uNJmXeF677xAn`</summary>

```json
{
  "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf",
  "prompt": "Extract the title, authors, abstract, and date of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3286cfe5-fce2-4c1b-a52d-9d5c58f48ce3",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo1UoXWmHZY1K1rYupx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f2a57d8-8190-4f7a-8a64-68dbd7dd93c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186E2FULDDstpNojwD5dFq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 17528,
      "output_tokens": 624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 624,
          "cache_read_input_tokens": 17528,
          "cache_creation_input_tokens": 3964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3964,
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

_source line 57 · 2026-05-28T10:17:06.004Z_

<details><summary>↩ Tool result · `toolu_01N5ite34FNVDDvY61XWHm72`</summary>

```text
# FormaRL Research Paper Details

**Title:** "FormaRL: Enhancing Autoformalization with no Labeled Data"

**Authors:** Yanxing Huang, Xinling Jin, Sijie Liang, Peng Li, and Yang Liu

**Submission Date:** August 26, 2025

**Abstract Summary:**
The paper introduces FormaRL, a reinforcement learning framework designed to improve autoformalization—converting informal mathematical proofs into formal verification language. The approach requires only minimal unlabeled data and combines syntax verification from the Lean compiler with consistency checks from large language models to generate reward signals. The authors also present a new dataset called uproof derived from undergraduate mathematics materials. Their experiments demonstrate significant improvements, increasing pass@1 accuracy from 4.04% to 26.15% on ProofNet using just 859 unlabeled examples with the Qwen2.5-Coder model, along with strong out-of-distribution performance gains on the uproof benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "864aacbd-139f-47a3-8607-9d01079420a2",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "ca14ede2-8e70-43b2-bc63-f691a6426814",
  "sourceToolAssistantUUID": "864aacbd-139f-47a3-8607-9d01079420a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T10:17:06.114Z_

<details><summary>↩ Tool result · `toolu_014TBrjeKxm2xRBQkBcKmBFG`</summary>

```text
# ReForm: Reflective Autoformalization Paper

**Title:** "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization"

**Authors:** Guoxin Chen, Jing Wu, Xinjie Chen, Wayne Xin Zhao, Ruihua Song, Chengxi Li, Kai Fan, Dayiheng Liu, and Minpeng Liao

**Submission Date:** October 28, 2025 (most recent version: February 10, 2026)

**Abstract Summary:**
The paper addresses limitations in converting natural language mathematics into formal statements. The authors note that "Large Language Models can generate syntactically correct formal statements, they often fail to preserve the original problem's semantic intent." Their method integrates semantic consistency evaluation with iterative refinement. They introduce a training technique called Prospective Bounded Sequence Optimization and present ReForm, which achieves improvements of 22.6 percentage points over existing approaches across multiple benchmarks. Additionally, they created ConsistencyCheck, a validated benchmark of 859 expert-annotated items revealing that even human experts introduce semantic errors in up to 38.5% of cases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a2bbc4-d383-46f4-9202-90ed9c142068",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "789e2c43-2017-4fc1-80be-7c9a1b75d6c3",
  "sourceToolAssistantUUID": "19a2bbc4-d383-46f4-9202-90ed9c142068",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T10:17:07.429Z_

<details><summary>↩ Tool result · `toolu_01VksAFEcoedU7fmuegBow75`</summary>

```text
# Paper Summary

**Title:** "An Evaluation Benchmark for Autoformalization in Lean4"

**Authors:** Aryan Gulati, Devanshu Ladsaria, Shubhra Mishra, Jasdeep Sidhu, and Brando Miranda

**Submission Date:** June 1, 2024

**Abstract:** The paper introduces a benchmark for evaluating how well large language models can convert informal mathematics into formal Lean4 code. The researchers tested GPT-3.5, GPT-4, and Gemini Pro, finding that "despite recent advancements, these LLMs still exhibit limitations in autoformalization, particularly in more complex areas of mathematics." The study aims to guide future improvements in this emerging capability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b343274-84a9-43f7-bc51-e89035de15b2",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "c213cb56-4c7b-4d80-b42a-1ebb9454bf26",
  "sourceToolAssistantUUID": "4b343274-84a9-43f7-bc51-e89035de15b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-28T10:17:07.916Z_

<details><summary>↩ Tool result · `toolu_017aEhraYDSJMhTqvqWY9QxS`</summary>

```text
# ATLAS Research Paper Summary

**Title:** "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data"

**Authors:** Xiaoyang Liu, Kangjie Bao, Jiashuo Zhang, Yunqi Liu, Yu Chen, Yuntian Liu, Yang Jiao, and Tao Luo

**Submission Date:** February 8, 2025 (v1); most recent revision October 1, 2025 (v3)

**Abstract Overview:**
This work addresses a key bottleneck in autoformalization—the scarcity of parallel datasets mapping natural language mathematics to formal languages. The researchers developed a data generation framework that creates large-scale, high-quality corpora of theorem statements. After 10 iterations, they produced 117,000 undergraduate-level theorem statements and fine-tuned Llama3.1-8B-Instruct to create the ATLAS Translator. The model "establishes a new state of the art, demonstrating statistically significant improvements over both the Herald Translator and the Kimina-Autoformalizer across all benchmarks" (p<0.05). The paper has been accepted to NeurIPS 2025, with datasets, model, and code made publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a1c14ee-4c83-4f64-b7cd-bbda60764b86",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "64aefa74-0e2d-4e98-a486-3dc2d5d3e028",
  "sourceToolAssistantUUID": "1a1c14ee-4c83-4f64-b7cd-bbda60764b86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-28T10:17:08.661Z_

<details><summary>↩ Tool result · `toolu_01VNomyX1U33guto6T6YXeCm`</summary>

```text
# Paper Summary

**Title:** "Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual Data in AutoFormalization"

**Authors:** Willy Chan, Michael Souliman, Jakob Nordhagen, Brando Miranda, Elyas Obbad, and Kai Fronsdal Sanmi Koyejo

**Submission Date:** February 18, 2025

**Abstract Summary:**

The paper addresses autoformalization—converting informal mathematical language into formal specifications. The researchers introduce a methodology utilizing back-translation with curated prompts to enhance language models' mathematical abilities while tackling data scarcity. They evaluate three strategic variations emphasizing data quality over quantity. Their key finding: "synthetic data, which prioritizes quality over volume, improves the Autoformalization performance of LLMs" on benchmarks like ProofNet. Notably, their approach achieves superior results compared to extensive multilingual dataset fine-tuning while requiring substantially fewer computational tokens, demonstrating a resource-efficient path toward advancing AI for mathematics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3092f39-df68-4c55-b521-e483bc7b86d5",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "03145974-aa1d-42e9-939e-a72ad59b91be",
  "sourceToolAssistantUUID": "e3092f39-df68-4c55-b521-e483bc7b86d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-28T10:17:09.281Z_

<details><summary>↩ Tool result · `toolu_01JWSRig1Y3uNJmXeF677xAn`</summary>

```text
I appreciate your request, but I'm unable to extract the requested information from this document. The content provided appears to be a PDF file encoded in binary format (raw PDF stream data), which is not human-readable text.

To help you extract the title, authors, abstract, and date, I would need:

1. **The actual text content** of the paper (not the raw PDF encoding)
2. Or a **properly rendered/decoded version** of the document

If you have access to this paper, I'd recommend:
- Converting the PDF to plain text first
- Copying and pasting the readable text portion
- Or providing the document URL if it's available online

Once you share the readable text, I'll be happy to identify and extract the bibliographic information you're looking for while respecting the character limits you've specified.

[Binary content (application/pdf, 936.5KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/6add041d-94c4-4ef6-b86d-e64a189e2047/tool-results/webfetch-1779963425983-18yzl6.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f2a57d8-8190-4f7a-8a64-68dbd7dd93c1",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "f43517e3-cbf7-4e23-b024-aaba5c64e53f",
  "sourceToolAssistantUUID": "8f2a57d8-8190-4f7a-8a64-68dbd7dd93c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-28T10:17:12.104Z_

Let me search for a few more papers I noticed in the results, and also search for IndiMathBench and the multi-pass translation paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43517e3-cbf7-4e23-b024-aaba5c64e53f",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo2LyWz3R1eH5KztXaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbe59d7b-4f36-4a3d-bf81-0ca300699a1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQkDbdgxG3VCYUEXSBRdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 21492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2556,
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

_source line 64 · 2026-05-28T10:17:13.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCRYow7sqdTHa1bQWkQcjA`</summary>

```json
{
  "query": "IndiMathBench autoformalization Indian mathematics Lean 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbe59d7b-4f36-4a3d-bf81-0ca300699a1a",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo2LyWz3R1eH5KztXaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a25df82-38c7-4ff3-8de8-e3b554a6e34d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQkDbdgxG3VCYUEXSBRdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 21492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2556,
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

_source line 65 · 2026-05-28T10:17:14.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Xgt7x7ahXh4e1VrdPvVea`</summary>

```json
{
  "query": "\"multi-pass\" OR \"multi-agent\" autoformalization Lean proof 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a25df82-38c7-4ff3-8de8-e3b554a6e34d",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo2LyWz3R1eH5KztXaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68c403f0-0ffc-43dc-8a20-14cd52f31cf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQkDbdgxG3VCYUEXSBRdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 21492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2556,
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

_source line 66 · 2026-05-28T10:17:14.560Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EJxQDosXE4JHYRyuPQsG9D`</summary>

```json
{
  "query": "Gauss autoformalization prime number theorem Lean 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68c403f0-0ffc-43dc-8a20-14cd52f31cf2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo2LyWz3R1eH5KztXaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad3a9400-ce3a-4bee-bd70-fcb6fb04b523",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQkDbdgxG3VCYUEXSBRdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 21492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2556,
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

_source line 67 · 2026-05-28T10:17:14.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QZnDyAAvniZB8sc3B6hka`</summary>

```json
{
  "query": "Kimina autoformalizer Lean 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3a9400-ce3a-4bee-bd70-fcb6fb04b523",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo2LyWz3R1eH5KztXaX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d368be1-5131-4a39-9435-2905b124ee7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQkDbdgxG3VCYUEXSBRdG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 21492,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 21492,
          "cache_creation_input_tokens": 2556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2556,
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

_source line 68 · 2026-05-28T10:17:20.116Z_

<details><summary>↩ Tool result · `toolu_01SCRYow7sqdTHa1bQWkQcjA`</summary>

```text
Web search results for query: "IndiMathBench autoformalization Indian mathematics Lean 2025 arxiv"

Links: [{"title":"IndiMathBench: Autoformalization Mathematical Reasoning Problems with a Human Touch - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/indimathbench-autoformalization-mathematical-reasoning-problems-with-a-human-touch/"},{"title":"[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/abs/2512.00997"},{"title":"(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview","url":"https://openreview.net/forum?id=tmReo37kl2"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"}]

Based on the search results, here's what I found about IndiMathBench:

## Overview

IndiMathBench is a human-verified benchmark designed to evaluate mathematical theorem proving, curated using an AI-powered human-assisted pipeline for formalizing natural language problems in Lean.

## Composition

IndiMathBench is composed of 312 formal Lean 4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads. The problems are sourced from algebra, euclidean geometry, elementary number theory, and combinatorics.

## Methodology

Through category-based retrieval, iterative compiler feedback, and multi-model ensembles, the pipeline generates candidate formalizations that experts efficiently validate via an interactive dashboard with automated quality summaries.

## Key Findings

Autoformalization remains challenging, with substantial gaps between syntactic validity and semantic correctness, while theorem proving success rates remain low even with iterative refinement. Claude Opus 4 achieved the highest BEq score (67/312) and compilation success rate (243/312), representing the current state-of-the-art in mathematical autoformalization.

## Publication

The paper was submitted on November 30, 2025 with an update on March 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a25df82-38c7-4ff3-8de8-e3b554a6e34d",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "e24ff62c-9e9d-4b68-9fa1-f53adbd58115",
  "sourceToolAssistantUUID": "6a25df82-38c7-4ff3-8de8-e3b554a6e34d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-28T10:17:20.581Z_

<details><summary>↩ Tool result · `toolu_011QZnDyAAvniZB8sc3B6hka`</summary>

```text
Web search results for query: "Kimina autoformalizer Lean 2025 arxiv"

Links: [{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v3"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"}]

Based on the search results, I found several relevant papers from 2025 mentioning Kimina Autoformalizer in arXiv:

Kimina-Autoformalizer-7B is a state-of-the-art auto-formalization tool that auto-formalizes theorem statements and proofs in Lean.

Kimina-Autoformalizer-7B was developed by Wang et al. in 2025, and appears to be used as a baseline in several recent papers on autoformalization.

The tool is referenced in multiple 2025 arxiv papers:
- ProofBridge (arXiv:2510.15681) evaluates against Kimina-Prover and builds on Kimina-Prover-RL-1.7B
- StepFun-Formalizer (arXiv:2508.04440) compares prompting approaches with the original prompt of Kimina-Autoformalizer
- Autoformalizer with Tool Feedback (arXiv:2510.06857) notes that about 40% of statements fail syntax validation when using Kimina-Autoformalizer


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d368be1-5131-4a39-9435-2905b124ee7e",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "5e23ac6d-3920-49cc-91d4-e600915cceb0",
  "sourceToolAssistantUUID": "6d368be1-5131-4a39-9435-2905b124ee7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T10:17:21.480Z_

<details><summary>↩ Tool result · `toolu_01EJxQDosXE4JHYRyuPQsG9D`</summary>

```text
Web search results for query: "Gauss autoformalization prime number theorem Lean 2025"

Links: [{"title":"Introducing Gauss, an agent for autoformalization — Math, Inc.","url":"https://www.math.inc/gauss"},{"title":"Introducing Gauss, an agent for autoformalization","url":"https://milesmathis.forumotion.com/t792-introducing-gauss-an-agent-for-autoformalization"},{"title":"The Dawn Of AI-Powered Mathematics: Gauss AI Conquers The Strong Prime Number Theorem","url":"https://www.nowadais.com/ai-mathematics-gauss-ai-strong-prime-number/"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"GitHub - math-inc/strongpnt · GitHub","url":"https://github.com/math-inc/strongpnt"},{"title":"Strong PNT | by Math Inc.","url":"https://math-inc.github.io/strongpnt/"},{"title":"Jesse Michael Han on X: \"In the first year of my PhD, I formalized the independence of the continuum hypothesis in Lean. It was considered a breakthrough at the time, taking ~12 months and 20K lines of code. With Gauss, we finished Strong PNT with 25K LOC in 3 weeks. There are two really remarkable\" / X","url":"https://x.com/jessemhan/status/1966379609932673097"},{"title":"AI formalizes \"strong\" Prime Number Theorem in Lean","url":"https://www.linkedin.com/posts/john-n-dvorak_introducing-gauss-an-agent-for-autoformalization-activity-7372118373310251008-KRDg"},{"title":"GFLean: An Autoformalisation Framework for Lean via GF","url":"https://arxiv.org/pdf/2404.01234"}]

Based on the search results, here's what I found about Gauss, autoformalization, and the Prime Number Theorem:

## Gauss Autoformalization Agent

Math Inc. introduced Gauss, a first-of-its-kind autoformalization agent for assisting human expert mathematicians at formal verification, which successfully completed a challenge to formalize the strong Prime Number Theorem (PNT) in Lean.

## The Achievement

Gauss AI successfully completed the Strong Prime Number Theorem formalization in just three weeks, in stark contrast to the 18+ months that top human mathematicians, including Fields Medallist Terence Tao and Alex Kontorovich, spent working on the same project. This was in response to a challenge set by Tao and Kontorovich in January 2024.

## Technical Details

The finished Lean development is substantial with over 25k lines and 1.1k theorems/definitions, showing how AI agents can accelerate large formalization efforts when combined with human guidance. The development was completed with targeted human scaffolding and review of key lemmas and strategies.

## How It Works

Gauss can work autonomously for hours, dramatically compressing the labor previously reserved for top formalization experts. Currently, it relies on natural language scaffolding supplied by human mathematicians, and requires high-level expert guidance and development on that scaffolding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad3a9400-ce3a-4bee-bd70-fcb6fb04b523",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "6a22a34e-3542-4d3f-bf44-c7a016881b20",
  "sourceToolAssistantUUID": "ad3a9400-ce3a-4bee-bd70-fcb6fb04b523",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-28T10:17:23.181Z_

<details><summary>↩ Tool result · `toolu_011Xgt7x7ahXh4e1VrdPvVea`</summary>

```text
Web search results for query: ""multi-pass" OR "multi-agent" autoformalization Lean proof 2025 arxiv"

Links: [{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"Ax-Prover: A Deep Reasoning Agentic Framework for Theorem Proving in Mathematics and Quantum Physics","url":"https://arxiv.org/html/2510.12787v2"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"Automatic Textbook Formalization","url":"https://arxiv.org/html/2604.03071v1"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"MASA: LLM-Driven Multi-Agent Systems for Autoformalization","url":"https://arxiv.org/pdf/2510.08988"},{"title":"Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving","url":"https://arxiv.org/pdf/2603.24465"}]

Based on the search results, I found several relevant papers on multi-agent and related autoformalization approaches for Lean proofs from 2025 and early 2026:

## Key Papers Found:

**MASA: LLM-Driven Multi-Agent Systems for Autoformalization**
MASA is a multi-agent system comprising agents, LLMs, knowledge bases, retrievers, and theorem provers that demonstrates a fully automated pipeline for formalizing mathematical statements from miniF2F into Lean 4.

**Automatic Textbook Formalization**
This work studies the efficacy of multi-agent proof engineering systems by attempting a full formalization of a graduate textbook on algebraic combinatorics of more than 500 pages.

**MerLean and Related Agentic Frameworks**
Xu and Odersky (2026) demonstrated "agentic proof automation" by mechanizing System Capless (14,000+ lines of Lean 4) with 87% task success rate across 189 annotated tasks. Liu et al. (2026) proposed Numina-Lean-Agent, combining Claude Code with MCP-based Lean tools that solved all 12 Putnam 2025 problems without model training.

**ProofBridge**
ProofBridge compares against foundation models and automated formal language proof synthesis tools, including GPT-5-mini and Gemini-2.5 variants.

These papers demonstrate significant progress in multi-agent and agentic approaches to autoformalization in Lean, with recent work achieving high success rates on various mathematical benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68c403f0-0ffc-43dc-8a20-14cd52f31cf2",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "e781e021-9d61-4db8-9d51-f8dcf79fbdca",
  "sourceToolAssistantUUID": "68c403f0-0ffc-43dc-8a20-14cd52f31cf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-28T10:17:28.582Z_

Let me fetch the remaining papers I haven't accessed yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e781e021-9d61-4db8-9d51-f8dcf79fbdca",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eaa3b18-3f19-44f6-a22c-e02477185b25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 73 · 2026-05-28T10:17:29.522Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017bsgkzFkrzmkKZrvqj92FE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.00997",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eaa3b18-3f19-44f6-a22c-e02477185b25",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cfcc400-a1e5-4ae2-8532-bc902b489cdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 74 · 2026-05-28T10:17:30.492Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011F7ab7dituiTacm6s3Veaz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.08988",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper. This should be the MASA multi-agent autoformalization paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cfcc400-a1e5-4ae2-8532-bc902b489cdd",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af8580e5-b85b-4929-9dd5-c9b18c962243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 75 · 2026-05-28T10:17:31.964Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L6qFHJ48Px2yMgqbKdU8jJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03071",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (Automatic Textbook Formalization)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af8580e5-b85b-4929-9dd5-c9b18c962243",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "febf5b8b-4c66-4e10-a861-c85f5ef95763",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 76 · 2026-05-28T10:17:32.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ey6C721ExaZ8vgjSyHC3Bv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16554",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (MerLean)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "febf5b8b-4c66-4e10-a861-c85f5ef95763",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9416efc6-cfad-4819-9cbc-3ff49c2d71bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 77 · 2026-05-28T10:17:32.992Z_

<details><summary>↩ Tool result · `toolu_011F7ab7dituiTacm6s3Veaz`</summary>

```text
# MASA Paper Details

**Title:** "MASA: LLM-Driven Multi-Agent Systems for Autoformalization"

**Authors:** Lan Zhang, Marco Valentino, and André Freitas

**Abstract:** The paper introduces MASA, a framework enabling collaborative agents to convert natural language statements into formal representations. The system emphasizes modularity and extensibility, integrating LLMs with theorem provers. Researchers demonstrated its effectiveness using mathematical definitions and formal mathematics datasets, highlighting multi-agent systems' potential for improving autoformalization efficiency and reliability.

**Submission Date:** October 10, 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af8580e5-b85b-4929-9dd5-c9b18c962243",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "bec5b34f-d2c7-4c78-a3a0-68225d488101",
  "sourceToolAssistantUUID": "af8580e5-b85b-4929-9dd5-c9b18c962243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-28T10:17:33.379Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JpS4wKnpxtxuZn6MPLFLgD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.03108",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (miniF2F-Lean Revisited)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bec5b34f-d2c7-4c78-a3a0-68225d488101",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b262fad9-7003-40a5-8ab5-0fea7b0f8681",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 79 · 2026-05-28T10:17:33.417Z_

<details><summary>↩ Tool result · `toolu_017bsgkzFkrzmkKZrvqj92FE`</summary>

```text
# IndiMathBench Paper Details

**Title:** "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch"

**Authors:** Param Biyani, Shashank Kirtania, Yasharth Bajpai, Sumit Gulwani, and Ashish Tiwari

**Submission Date:** November 30, 2025 (v1); revised March 10, 2026 (v2)

**Abstract Summary:**
The researchers created a benchmark containing 312 formal Lean 4 theorems paired with informal problem statements from Indian Mathematics Olympiads. They developed an "AI-powered human-assisted pipeline" for converting natural language math problems into formal proofs. The work demonstrates that "autoformalization remains challenging, with substantial gaps between syntactic validity and semantic correctness," even when using advanced language models. The benchmark serves as a demanding testbed for evaluating mathematical reasoning capabilities in modern AI systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cfcc400-a1e5-4ae2-8532-bc902b489cdd",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "8014e2c1-ed88-4003-807f-44817de0c6b2",
  "sourceToolAssistantUUID": "7cfcc400-a1e5-4ae2-8532-bc902b489cdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-28T10:17:33.906Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KrBvL3oEAAELL66fspj2No`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.04440",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (StepFun-Formalizer)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8014e2c1-ed88-4003-807f-44817de0c6b2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo3PuuGxJKFuVVdXYUy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c3280b6-1256-4deb-bd40-25c8332da205",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141jUZVG5q3exTLN16iaMxr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1473,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 24048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1826,
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

_source line 81 · 2026-05-28T10:17:35.930Z_

<details><summary>↩ Tool result · `toolu_01L6qFHJ48Px2yMgqbKdU8jJ`</summary>

```text
# Automatic Textbook Formalization - Paper Details

**Title:** Automatic Textbook Formalization

**Authors:** Fabian Gloeckle, Ahmad Rammal, Charles Arnal, Remi Munos, Vivien Cabannes, Gabriel Synnaeve, and Amaury Hayat

**Submission Date:** April 3, 2026

**Abstract Summary:**
This research demonstrates an AI system that automatically converted a 500+ page graduate-level algebraic combinatorics textbook into formal Lean code. The project achieved 130K lines of code and 5900 declarations, representing a significant advancement in textbook formalization. The work employed 30,000 Claude Opus agents operating collaboratively through version control over one week. The authors note that "The inference cost matches or undercuts what we estimate as the salaries required for a team of human experts," and they have released their code and resulting formalization as open-source materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "febf5b8b-4c66-4e10-a861-c85f5ef95763",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "7de2d678-51da-4ba5-b439-daeaaa89af20",
  "sourceToolAssistantUUID": "febf5b8b-4c66-4e10-a861-c85f5ef95763",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-28T10:17:36.674Z_

<details><summary>↩ Tool result · `toolu_01Ey6C721ExaZ8vgjSyHC3Bv`</summary>

```text
# MerLean Paper Details

**Title:** "MerLean: An Agentic Framework for Autoformalization in Quantum Computation"

**Authors:** Yuanjie Ren, Jinzheng Li, and Yidi Qi

**Submission Date:** February 18, 2026

**Abstract Summary:**

The paper introduces an automated system that extracts mathematical statements from LaTeX files and converts them into verified Lean 4 code built on Mathlib. The framework then translates results back to human-readable LaTeX format. Testing on three quantum computing papers produced over 2,000 Lean declarations from 114 statements. The authors claim their approach achieves end-to-end formalization while reducing verification work to only newly introduced definitions and axioms. They suggest this technology could support machine-verified peer review and generate synthetic training data for reasoning models, with potential applications extending to mathematics and theoretical physics research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9416efc6-cfad-4819-9cbc-3ff49c2d71bc",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "645e085e-9cf4-4fad-aaa6-acba8e9cf0a0",
  "sourceToolAssistantUUID": "9416efc6-cfad-4819-9cbc-3ff49c2d71bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-28T10:17:36.992Z_

<details><summary>↩ Tool result · `toolu_01JpS4wKnpxtxuZn6MPLFLgD`</summary>

```text
# miniF2F-Lean Revisited Paper Details

**Title:** "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward"

**Authors:** Azim Ospanov, Farzan Farnia, and Roozbeh Yousefzadeh

**Submission Date:** November 5, 2025

**Abstract Summary:**
The researchers conducted a comprehensive evaluation of the miniF2F benchmark through the lens of an AI system tackling math olympiad problems. They discovered that when combining autoformalization and theorem proving in a full pipeline, accuracy drops significantly to 36%—despite individual models achieving 97% and 69% respectively. The authors identified that discrepancies between formal and informal problem statements accounted for much of this performance gap. After correcting these issues, they released miniF2F-v2 with verified statements and proofs, achieving 70% accuracy on the improved benchmark. They conclude that higher-quality benchmarks are essential for better evaluating progress in formal reasoning systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b262fad9-7003-40a5-8ab5-0fea7b0f8681",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "524ff867-4d13-47c5-aab6-41a46de7c4f3",
  "sourceToolAssistantUUID": "b262fad9-7003-40a5-8ab5-0fea7b0f8681",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-28T10:17:38.337Z_

<details><summary>↩ Tool result · `toolu_01KrBvL3oEAAELL66fspj2No`</summary>

```text
# StepFun-Formalizer Paper Details

**Title:** "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion"

**Authors:** Yutong Wu, Di Huang, Ruosi Wan, Yue Peng, Shijie Shang, Chenrui Cao, Lei Qi, Rui Zhang, Zidong Du, Jie Yan, and Xing Hu

**Submission Date:** August 6, 2025 (with revisions through December 26, 2025)

**Abstract Summary:** The paper addresses autoformalization—converting natural-language math statements into formal language. The researchers identify two critical capabilities: mastery of formal-language knowledge and reasoning ability for problem understanding. They introduce a training pipeline called ThinkingF that combines curated formal-knowledge datasets with expert-guided informal-to-formal reasoning trajectories. The resulting 7B and 32B parameter models achieve state-of-the-art results, with the 32B variant reaching "40.5% on FormalMATH-Lite and 26.7% on ProverBench" benchmark scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3280b6-1256-4deb-bd40-25c8332da205",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "f43251e2-be7c-4b34-b407-600030450984",
  "sourceToolAssistantUUID": "4c3280b6-1256-4deb-bd40-25c8332da205",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-28T10:17:42.254Z_

Let me do one more round of searches for papers I may have missed, particularly on the EMNLP multi-pass translation paper and GFLean.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43251e2-be7c-4b34-b407-600030450984",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo4VGe55m9v7zBZm68N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d3f9437-b259-40d8-bc18-7ed596ecec39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsHpxLjPxrWzM75ULLzpJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 25874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
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

_source line 86 · 2026-05-28T10:17:43.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xk1dWe8iorsz7kLTC8Fu2H`</summary>

```json
{
  "query": "\"translating natural language into Lean 4\" multi-pass EMNLP 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d3f9437-b259-40d8-bc18-7ed596ecec39",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo4VGe55m9v7zBZm68N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c518d5e0-d341-4df0-b247-2cde285cce67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsHpxLjPxrWzM75ULLzpJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 25874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
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

_source line 87 · 2026-05-28T10:17:44.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EmBBGi9kgMK4MjMMewjveu`</summary>

```json
{
  "query": "GFLean autoformalisation GF Lean arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c518d5e0-d341-4df0-b247-2cde285cce67",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo4VGe55m9v7zBZm68N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c93f351b-a236-4b5e-8488-6f41b13154e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsHpxLjPxrWzM75ULLzpJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 25874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
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

_source line 88 · 2026-05-28T10:17:44.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0163z4t1N69AieYs8MLvEvMJ`</summary>

```json
{
  "query": "ConsistencyCheck semantic autoformalization 2025 benchmark arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c93f351b-a236-4b5e-8488-6f41b13154e0",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo4VGe55m9v7zBZm68N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07eae848-63ec-4c15-92a1-65553a7749e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsHpxLjPxrWzM75ULLzpJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 25874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
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

_source line 89 · 2026-05-28T10:17:49.066Z_

<details><summary>↩ Tool result · `toolu_01Xk1dWe8iorsz7kLTC8Fu2H`</summary>

```text
Web search results for query: ""translating natural language into Lean 4" multi-pass EMNLP 2025 arxiv"

Links: [{"title":"NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1586/"},{"title":"Translating Natural Language into Lean 4 through Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.1586v2.pdf"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Herald: A Natural Language Annotated Lean 4 Dataset","url":"https://arxiv.org/html/2410.10878v1"},{"title":"[2410.10878] Herald: A Natural Language Annotated Lean 4 Dataset","url":"https://arxiv.org/abs/2410.10878"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"}]

Based on the search results, I found a highly relevant paper for your query:

**NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning** was presented at the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) by Fang et al.

The paper's key approach includes:

- A multi-aspect dense reward mechanism covering four key dimensions: semantic alignment, term-level alignment, global-level alignment, and compile-checking
- Separate reward models trained via preference modeling, with their normalized outputs combined to guide optimization via PPO
- A curriculum learning strategy based on multi-dimensional difficulty that allows the model to learn progressively from simple to complex cases

Experiments on NL-to-Lean 4 tasks show that their method consistently outperforms baseline models.

The paper is available at the ACL Anthology: https://aclanthology.org/2025.emnlp-main.1586/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c518d5e0-d341-4df0-b247-2cde285cce67",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "1496a709-f2bb-4a56-b8ec-9ffddafd51cf",
  "sourceToolAssistantUUID": "c518d5e0-d341-4df0-b247-2cde285cce67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-28T10:17:50.187Z_

<details><summary>↩ Tool result · `toolu_0163z4t1N69AieYs8MLvEvMJ`</summary>

```text
Web search results for query: "ConsistencyCheck semantic autoformalization 2025 benchmark arxiv"

Links: [{"title":"[2510.24592] ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/abs/2510.24592"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/html/2510.24592"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"arXiv:2505.23486v2 [cs.AI] 3 Jul 2025","url":"https://arxiv.org/pdf/2505.23486"},{"title":"[2511.12784] Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/abs/2511.12784"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/pdf/2509.09810"}]

Based on the search results, I found relevant information about ConsistencyCheck:

ConsistencyCheck is a benchmark of 859 expert-annotated items that validates LLMs as judges and reveals that autoformalization is inherently difficult, with even human experts producing semantic errors in up to 38.5% of cases.

The benchmark was constructed to rigorously investigate the reliability of frontier LLMs as evaluation metrics and test how accurately a model determines whether a given formal statement correctly captures the problem's intent.

Analysis on ConsistencyCheck revealed insights about human expert fallibility, showing that 16.4% of miniF2F and 38.5% of ProofNet's human-written formal statements contain semantic errors, demonstrating that autoformalization challenges even human experts.

This benchmark appears in the paper "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization," which was updated on arXiv as recently as February 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07eae848-63ec-4c15-92a1-65553a7749e1",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "2d2fdc0c-644b-4650-b91f-8bf65f6feb88",
  "sourceToolAssistantUUID": "07eae848-63ec-4c15-92a1-65553a7749e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-28T10:17:51.007Z_

<details><summary>↩ Tool result · `toolu_01EmBBGi9kgMK4MjMMewjveu`</summary>

```text
Web search results for query: "GFLean autoformalisation GF Lean arxiv 2024 2025"

Links: [{"title":"[2404.01234] GFLean: An Autoformalisation Framework for Lean via GF","url":"https://arxiv.org/abs/2404.01234"},{"title":"GFLean: An Autoformalisation Framework for Lean via GF","url":"https://arxiv.org/html/2404.01234v1"},{"title":"[Literature Review] GFLean: An Autoformalisation Framework for Lean via GF","url":"https://www.themoonlight.io/en/review/gflean-an-autoformalisation-framework-for-lean-via-gf"},{"title":"GFLEAN: AN AUTOFORMALISATION FRAMEWORK FOR LEAN VIA GF Shashank Pathak","url":"https://arxiv.org/pdf/2404.01234"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via","url":"https://arxiv.org/pdf/2507.08665"},{"title":"GFLean: An Autoformalisation Framework for Lean via GF","url":"https://www.semanticscholar.org/paper/GFLean:-An-Autoformalisation-Framework-for-Lean-via-Pathak/7852aa1613a5eeaf791376c71ad306f5e17fc853"},{"title":"Free Video: GFLean - Autoformalisation for Lean via Grammatical Framework from Hausdorff Center for Mathematics | Class Central","url":"https://www.classcentral.com/course/youtube-shashank-pathak-gflean-autoformalisation-for-lean-via-gf-309813"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/html/2507.08665"}]

## Search Results

I found several sources about GFLean autoformalisation. Here are the key findings:

### Main Paper

GFLean is an autoformalisation framework for the Lean theorem prover submitted on April 1, 2024. GFLean converts simple mathematical statements to expressions for the Lean theorem prover.

### How It Works

GFLean uses a high-level grammar writing tool called Grammatical Framework (GF) for parsing and linearisation. GFLean is implemented in Haskell.

### Performance

When tested on statements from Chapter 3 of the textbook Mathematical Proofs, GFLean was able to parse and formalise 42 out of 62 statements with minor rephrasing of the input.

### Integration with Other Systems

The paper appears in recent research on autoformalization: GFLean was referenced as an autoformalisation framework for Lean via GF published in 2024, and it is cited in newer works like Atlas: Autoformalizing theorems through lifting, augmentation, and synthesis of data, published in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c93f351b-a236-4b5e-8488-6f41b13154e0",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "581dadbc-73eb-4578-a0e4-92f5de83e898",
  "sourceToolAssistantUUID": "c93f351b-a236-4b5e-8488-6f41b13154e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-28T10:17:53.120Z_

Let me fetch the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "581dadbc-73eb-4578-a0e4-92f5de83e898",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo5SunXD75w9ViwqsiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b766409-b6b5-4f44-a892-603ab9436679",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhtcLjoU5mEYi46tcuTcLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 654,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1714,
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

_source line 93 · 2026-05-28T10:17:55.092Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F591BTecCzC9k5KKvic7uC`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.1586/",
  "prompt": "Extract the title, authors, abstract, and publication date of this EMNLP paper (NL2Lean)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b766409-b6b5-4f44-a892-603ab9436679",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo5SunXD75w9ViwqsiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c47a521-7cdc-4470-ab08-6894ecf5dfa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhtcLjoU5mEYi46tcuTcLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 654,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1714,
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

_source line 94 · 2026-05-28T10:17:55.592Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WoFcRbkSJYG7AnYSNdaaC7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.08665",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (KELPS)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c47a521-7cdc-4470-ab08-6894ecf5dfa1",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo5SunXD75w9ViwqsiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "315c6fbe-5379-436a-8ba1-7e90247144d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhtcLjoU5mEYi46tcuTcLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 654,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1714,
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

_source line 95 · 2026-05-28T10:17:56.642Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M4zZMVmqgdrrL5JwogJ7Ey`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.01234",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (GFLean)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "315c6fbe-5379-436a-8ba1-7e90247144d7",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo5SunXD75w9ViwqsiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f65ba04b-9f33-4caf-bff3-b071ed417750",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhtcLjoU5mEYi46tcuTcLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 654,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1714,
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

_source line 96 · 2026-05-28T10:17:57.377Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KQhkxa3nVW94LW4YpRU3YX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.24465",
  "prompt": "Extract the title, authors, abstract, and submission date of this arXiv paper (Mechanic)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f65ba04b-9f33-4caf-bff3-b071ed417750",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo5SunXD75w9ViwqsiD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5be959a5-2bb3-4244-bc99-35be6f48da6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhtcLjoU5mEYi46tcuTcLn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 654,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1714,
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

_source line 97 · 2026-05-28T10:17:58.145Z_

<details><summary>↩ Tool result · `toolu_01F591BTecCzC9k5KKvic7uC`</summary>

```text
# NL2Lean Paper Details

**Title:** "NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning"

**Authors:** Yue Fang, Shaohan Huang, Xin Yu, Haizhen Huang, Zihan Zhang, Weiwei Deng, Furu Wei, Feng Sun, Qi Zhang, and Zhi Jin

**Publication Date:** November 2025

**Abstract:** The paper addresses the challenge of converting natural language descriptions into formal Lean 4 code. The researchers developed a framework called ReLean that fine-tunes a LLaMA3-8B model and employs "a multi-aspect dense reward mechanism covering four key dimensions: semantic alignment, term-level alignment, global-level alignment, and compile-checking." They combine separate reward models through preference modeling and use PPO for optimization, alongside a curriculum learning approach for progressive learning from simpler to more complex examples. Their experiments demonstrate consistent improvements over existing baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c47a521-7cdc-4470-ab08-6894ecf5dfa1",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "a70e0d09-96f0-439b-819d-7b0efda7e7df",
  "sourceToolAssistantUUID": "3c47a521-7cdc-4470-ab08-6894ecf5dfa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-28T10:17:59.383Z_

<details><summary>↩ Tool result · `toolu_01WoFcRbkSJYG7AnYSNdaaC7`</summary>

```text
# KELPS Paper Summary

**Title:** "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment"

**Authors:** Jiyao Zhang, Chengli Zhong, Hui Xu, Qige Li, and Yi Zhou

**Submission Date:** July 11, 2025

**Abstract Summary:**
The researchers developed a neuro-symbolic system designed to convert informal mathematics into machine-verifiable formal theorems across multiple languages (Lean, Coq, Isabelle). The approach introduces "Knowledge Equations" as an intermediate representation grounded in assertional logic. The framework produced over 60,000 parallel problems and demonstrated strong performance, achieving "88.9% syntactic accuracy (pass@1) on MiniF2F," surpassing comparable models. The team made their datasets and code publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "315c6fbe-5379-436a-8ba1-7e90247144d7",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "3a2bf002-33fa-4a7f-b07f-38c43d2d4626",
  "sourceToolAssistantUUID": "315c6fbe-5379-436a-8ba1-7e90247144d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-28T10:17:59.472Z_

<details><summary>↩ Tool result · `toolu_01M4zZMVmqgdrrL5JwogJ7Ey`</summary>

```text
# GFLean Paper Details

**Title:** "GFLean: An Autoformalisation Framework for Lean via GF"

**Author:** Shashank Pathak

**Submission Date:** April 1, 2024

**Abstract:** The paper presents an autoformalisation framework designed for the Lean theorem prover. It leverages Grammatical Framework (GF), a high-level grammar tool, to handle parsing and linearisation tasks. Built using Haskell, the framework explains its capabilities, operational mechanisms, and constraints. The work discusses integrating neural network-based translation with rule-based approaches to develop more effective autoformalisation systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f65ba04b-9f33-4caf-bff3-b071ed417750",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "e2d3ef41-3805-48b0-abb7-2c0a16854c1a",
  "sourceToolAssistantUUID": "f65ba04b-9f33-4caf-bff3-b071ed417750",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-28T10:18:02.350Z_

<details><summary>↩ Tool result · `toolu_01KQhkxa3nVW94LW4YpRU3YX`</summary>

```text
# Mechanic: arXiv Paper Summary

**Title:** "Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving"

**Authors:** Ruichen Qiu, Yichuan Cao, Junqi Liu, Dakai Guo, Xiao-Shan Gao, Lihong Zhi, and Ruyong Feng

**Submission Date:** March 25, 2026

**Abstract Summary:** The paper introduces an agent system that addresses inefficiencies in automated theorem proving. Rather than discarding failed proofs entirely or iteratively patching errors (both problematic approaches), Mechanic employs "the sorry placeholder in Lean to precisely isolate unresolved subgoals while preserving the surrounding verified proof structure." This strategy isolates each failed subproblem into a standalone context for independent resolution. The researchers demonstrate their approach's effectiveness on challenging mathematical benchmarks, including IMO 2025 and Putnam 2025 competitions, showing improved proving efficiency compared to existing methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5be959a5-2bb3-4244-bc99-35be6f48da6a",
  "isSidechain": true,
  "promptId": "949fce33-07bd-4a5e-9cb4-aa8ea38faeec",
  "agentId": "a0e94d6bda196d649",
  "type": "user",
  "uuid": "3835f2b5-020c-4ba2-85b8-2384af0bc6e2",
  "sourceToolAssistantUUID": "5be959a5-2bb3-4244-bc99-35be6f48da6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-28T10:19:39.550Z_

Now let me compile the full results. Here is the comprehensive literature survey:

---

## Literature Survey: Domain-Adaptive Autoformalization (2024-2026)

Below are the papers found beyond the five seed papers (Herald, StepFun-Formalizer, DDR, Autoformalizer with Tool Feedback, APRIL). Papers are organized thematically.

---

### SURVEYS

**1. Autoformalization in the Era of Large Language Models: A Survey**
- Authors: Ke Weng, Lun Du, Sirui Li, Wangyue Lu, Haozhe Sun, Hengyu Liu, Tiancheng Zhang
- Date: May 2025 (revised July 2025)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2505.23486
- Summary: Comprehensive survey covering data preparation, model development, evaluation, and open-source tools for LLM-based autoformalization across difficulty levels and mathematical domains.

**2. Towards a Common Framework for Autoformalization**
- Authors: Agnieszka Mensfelt, David Tena Cucala, Santiago Franco, Angeliki Koutsoukou-Argyraki, Vince Trencsenyi, Kostas Stathis
- Date: September 2025 (revised December 2025)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2509.09810
- Summary: Proposes unifying the independently-developed autoformalization research strands (theorem provers, LLM reasoning, knowledge representation) into a shared framework with common benchmarks and methodologies.

---

### DATA SYNTHESIS AND TRAINING

**3. ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data**
- Authors: Xiaoyang Liu, Kangjie Bao, Jiashuo Zhang, Yunqi Liu, Yu Chen, Yuntian Liu, Yang Jiao, Tao Luo
- Date: February 2025 (revised October 2025)
- Venue: NeurIPS 2025
- URL: https://arxiv.org/abs/2502.05567
- Summary: Iterative data-generation framework producing 117k undergraduate-level theorem statements; the fine-tuned ATLAS Translator (Llama3.1-8B) achieves SOTA surpassing both Herald Translator and Kimina-Autoformalizer across all benchmarks.

**4. Lean Workbook: A Large-Scale Lean Problem Set Formalized from Natural Language Math Problems**
- Authors: Huaiyuan Ying, Zijian Wu, Yihan Geng, Zheng Yuan, Dahua Lin, Kai Chen
- Date: June 2024 (revised June 2025)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2406.03847
- Summary: Iterative pipeline generating ~57k formal-informal question pairs from math contest forums plus 21 IMO questions; demonstrates that synthetic data improves LLM formalization and understanding.

**5. Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual Data in AutoFormalization**
- Authors: Willy Chan, Michael Souliman, Jakob Nordhagen, Brando Miranda, Elyas Obbad, Kai Fronsdal, Sanmi Koyejo
- Date: February 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2502.15795
- Summary: Shows that curated, high-quality backtranslated synthetic data outperforms larger multilingual datasets for autoformalization, achieving superior ProofNet results with fewer tokens.

---

### TRAINING METHODS (RL, REFLECTION, CYCLE CONSISTENCY)

**6. FormaRL: Enhancing Autoformalization with No Labeled Data**
- Authors: Yanxing Huang, Xinling Jin, Sijie Liang, Peng Li, Yang Liu
- Date: August 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2508.18914
- Summary: RL framework using Lean compiler syntax verification + LLM consistency checks as rewards; improves pass@1 from 4.04% to 26.15% on ProofNet with only 859 unlabeled examples (Qwen2.5-Coder).

**7. ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization**
- Authors: Guoxin Chen, Jing Wu, Xinjie Chen, Wayne Xin Zhao, Ruihua Song, Chengxi Li, Kai Fan, Dayiheng Liu, Minpeng Liao
- Date: October 2025 (revised February 2026)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2510.24592
- Summary: Integrates semantic consistency evaluation with iterative refinement; introduces Prospective Bounded Sequence Optimization and the ConsistencyCheck benchmark (859 expert-annotated items revealing 38.5% human error rate); achieves +22.6pp improvement.

**8. Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning**
- Author: Arsen Shebzukhov
- Date: March 2026
- Venue: arXiv preprint (Stanford CS224N project)
- URL: https://arxiv.org/abs/2603.24372
- Summary: Fine-tunes Qwen3.5-2B with LoRA using GRPO with cycle consistency rewards (NL -> Lean4 -> NL' round-trip); RL substantially outperforms supervised variants.

**9. NL2Lean: Translating Natural Language into Lean 4 through Multi-Aspect Reinforcement Learning**
- Authors: Yue Fang, Shaohan Huang, Xin Yu, Haizhen Huang, Zihan Zhang, Weiwei Deng, Furu Wei, Feng Sun, Qi Zhang, Zhi Jin
- Date: November 2025
- Venue: EMNLP 2025
- URL: https://aclanthology.org/2025.emnlp-main.1586/
- Summary: Multi-aspect dense reward mechanism (semantic, term-level, global-level alignment + compile-checking) with PPO and curriculum learning for NL-to-Lean4 translation; consistent improvements over baselines.

---

### RETRIEVAL-AUGMENTED APPROACHES

**10. CRAMF: Automated Formalization via Conceptual Retrieval-Augmented LLMs**
- Authors: Wangyue Lu, Lun Du, Sirui Li, Ke Weng, Haozhe Sun, Hengyu Liu, Minghe Yu, Tiancheng Zhang, Ge Yu
- Date: August 2025 (revised March 2026)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2508.06931
- Summary: Retrieves formal definitions of core mathematical concepts from a 26k-entry Mathlib4 knowledge base using contextual query augmentation + hybrid retrieval; achieves up to 62.1% relative accuracy improvement.

**11. ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings**
- Authors: Prithwish Jana, Kaan Kale, Ahmet Ege Tanriverdi, Cruise Song, Sriram Vishwanath, Vijay Ganesh
- Date: October 2025 (revised March 2026)
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2510.15681
- Summary: Joint embedding model aligning NL and formal theorem+proof pairs in shared semantic space; retrieval-augmented fine-tuning with iterative proof repair; +31.14% SC over GPT-5/Gemini-2.5 baselines on miniF2F-Test-PF.

---

### MULTI-LANGUAGE AND NEURO-SYMBOLIC

**12. KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment**
- Authors: Jiyao Zhang, Chengli Zhong, Hui Xu, Qige Li, Yi Zhou
- Date: July 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2507.08665
- Summary: Neuro-symbolic system using "Knowledge Equations" as intermediate representation; generates 60k+ parallel problems across Lean/Coq/Isabelle; achieves 88.9% syntactic accuracy (pass@1) on MiniF2F.

**13. GFLean: An Autoformalisation Framework for Lean via GF**
- Author: Shashank Pathak
- Date: April 2024
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2404.01234
- Summary: Rule-based autoformalisation using Grammatical Framework (GF) for parsing/linearisation in Haskell; parses 42/62 textbook statements; discusses neural+rule-based hybrid integration.

---

### BENCHMARKS AND EVALUATION

**14. Reliable Evaluation and Benchmarks for Statement Autoformalization**
- Authors: Auguste Poiroux, Gail Weiss, Viktor Kuncak, Antoine Bosselut
- Date: June 2024 (revised October 2025)
- Venue: EMNLP 2025
- URL: https://arxiv.org/abs/2406.07222
- Summary: Introduces BEq+ metric (correlates with human judgment), ProofNetVerif dataset (3,752 annotated examples), corrected ProofNet#, and RLM25 benchmark (619 research-level math pairs); shows ~45% accuracy on undergrad math, major drops on research-level.

**15. Process-Driven Autoformalization in Lean 4 (FormL4)**
- Authors: Jianqiao Lu, Yingjia Wan, Zhengying Liu, Yinya Huang, Jing Xiong, et al.
- Date: June 2024 (revised October 2024)
- Venue: ICLR 2025
- URL: https://arxiv.org/abs/2406.01940
- Summary: Introduces FormL4 benchmark and a Process-Supervised Verifier (PSV) using stepwise Lean4 compiler traces; improves autoformalization accuracy with less filtered training data.

**16. An Evaluation Benchmark for Autoformalization in Lean4**
- Authors: Aryan Gulati, Devanshu Ladsaria, Shubhra Mishra, Jasdeep Sidhu, Brando Miranda
- Date: June 2024
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2406.06555
- Summary: Benchmark evaluating GPT-3.5/GPT-4/Gemini Pro on autoformalization tasks; finds significant limitations especially in complex mathematical areas.

**17. Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing**
- Authors: Hayden Moore, Asfahan Shah
- Date: November 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2511.12784
- Summary: Tests whether LLMs remain reliable when autoformaizing paraphrased inputs; finds minor NL shifts significantly impact formal outputs, revealing robustness concerns.

**18. miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward**
- Authors: Azim Ospanov, Farzan Farnia, Roozbeh Yousefzadeh
- Date: November 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2511.03108
- Summary: Reveals that combining autoformalization + theorem proving in a full pipeline drops accuracy to 36% despite strong individual scores (97% and 69%); releases corrected miniF2F-v2 achieving 70%.

**19. IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch**
- Authors: Param Biyani, Shashank Kirtania, Yasharth Bajpai, Sumit Gulwani, Ashish Tiwari
- Date: November 2025 (revised March 2026)
- Venue: arXiv preprint (Microsoft Research)
- URL: https://arxiv.org/abs/2512.00997
- Summary: 312 Lean4 theorems from Indian Math Olympiads with human-in-the-loop AI pipeline; shows large gap between syntactic validity and semantic correctness; Claude Opus 4 achieves best BEq (67/312).

---

### AGENTIC AND MULTI-AGENT SYSTEMS

**20. MASA: LLM-Driven Multi-Agent Systems for Autoformalization**
- Authors: Lan Zhang, Marco Valentino, Andre Freitas
- Date: October 2025
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2510.08988
- Summary: Modular multi-agent framework (AutoformalizationAgent, CritiqueAgents, RefinementAgents) integrating LLMs with theorem provers for collaborative autoformalization.

**21. Automatic Textbook Formalization**
- Authors: Fabian Gloeckle, Ahmad Rammal, Charles Arnal, Remi Munos, Vivien Cabannes, Gabriel Synnaeve, Amaury Hayat
- Date: April 2026
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2604.03071
- Summary: 30,000 Claude Opus agents collaboratively formalized a 500+ page graduate algebraic combinatorics textbook into 130k lines of Lean code / 5,900 declarations in one week; cost competitive with human experts.

**22. MerLean: An Agentic Framework for Autoformalization in Quantum Computation**
- Authors: Yuanjie Ren, Jinzheng Li, Yidi Qi
- Date: February 2026
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2602.16554
- Summary: End-to-end pipeline extracting math from LaTeX papers, converting to verified Lean4/Mathlib code, and back to LaTeX; tested on 3 quantum computing papers producing 2,000+ Lean declarations.

**23. Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving**
- Authors: Ruichen Qiu, Yichuan Cao, Junqi Liu, Dakai Guo, Xiao-Shan Gao, Lihong Zhi, Ruyong Feng
- Date: March 2026
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2603.24465
- Summary: Uses Lean's `sorry` placeholder to isolate unresolved subgoals while preserving verified proof structure, enabling independent subproblem resolution; tested on IMO/Putnam 2025.

---

### INFORMALIZATION (REVERSE DIRECTION)

**24. Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure**
- Authors: Seiji Hattori, Takuya Matsuzaki, Makoto Fujiwara
- Date: September 2025
- Venue: INLG 2025
- URL: https://arxiv.org/abs/2509.09726
- Summary: Converts formal proofs to readable natural language via stepwise informalization + recursive summarization; produces high-quality NL proofs from Lean libraries and undergraduate textbooks.

---

### LARGE-SCALE FORMALIZATION SYSTEMS (NOT STRICTLY PAPERS BUT NOTABLE)

**25. 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?**
- Author: Josef Urban
- Date: January 2026
- Venue: arXiv preprint
- URL: https://arxiv.org/abs/2601.03298
- Summary: Formalized Munkres topology textbook into ~160k lines of formal code using ChatGPT/Claude Sonnet + Megalodon proof checker feedback loop at ~$100 cost; includes Urysohn's lemma, metrization theorem, Tietze extension.

---

### KEY OBSERVATIONS

1. **Data quality > quantity** is a recurring theme (ATLAS, Lean-ing on Quality, Herald all confirm this).
2. **RL with formal verification rewards** is now the dominant training paradigm (FormaRL, NL2Lean/ReLean, ReForm, cycle consistency).
3. **Retrieval augmentation** is emerging as critical for bridging the domain gap (CRAMF, ProofBridge, DDR).
4. **Evaluation is undergoing a reckoning**: miniF2F-v2 corrections, ConsistencyCheck revealing 38.5% human error, BEq+ metric, and robustness-via-paraphrasing studies all highlight that current metrics are insufficient.
5. **Agentic/multi-agent architectures** represent the newest wave (MASA, Automatic Textbook Formalization with 30k agents, MerLean, Mechanic).
6. **Multi-language autoformalization** is starting to appear (KELPS targeting Lean+Coq+Isabelle simultaneously).
7. **Domain-specific autoformalization** is broadening beyond pure math into quantum computing (MerLean) and topology (Urban).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3835f2b5-020c-4ba2-85b8-2384af0bc6e2",
  "isSidechain": true,
  "agentId": "a0e94d6bda196d649",
  "requestId": "req_011CbUo6Fv2FLXzJ7ZQgcSMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e49e81ee-39d1-4faa-9353-62272fca4527",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6add041d-94c4-4ef6-b86d-e64a189e2047",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148EuPEVAcksPUff9QHYfG1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 31164,
      "output_tokens": 4357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4357,
          "cache_read_input_tokens": 31164,
          "cache_creation_input_tokens": 1957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1957,
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
