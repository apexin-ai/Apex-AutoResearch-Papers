# Research conversation: I need you to search for concurrent and competing work on the following research idea. Use WebSearch extensively. Resear

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aefc7761e04a79fe8.jsonl`
- **Structured JSON:** [`3c905d133aed7457ebc5.json`](../../sessions/3c/3c905d133aed7457ebc5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

70 recorded events

### User

_source line 1 · 2026-05-27T12:17:52.631Z_

I need you to search for concurrent and competing work on the following research idea. Use WebSearch extensively.

Research idea: "Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition" — the idea is to use pseudo-formal proof blocks (modular NL proof blocks with explicit premises/conclusions) as targets for selective autoformalization, routing only uncertain blocks to formal verification (e.g., Lean 4) while verifying confident blocks with LLM-based verification.

Search queries to run (use WebSearch for each):
1. "selective formal verification uncertainty 2026"
2. "pseudo-formal autoformalization 2026"
3. "adaptive verification mathematical proof 2026"
4. "uncertainty guided proof verification"
5. "selective autoformalization natural language proof 2026"
6. Search arXiv for: "autoformalization selective verification 2026"
7. Search arXiv for: "proof verification uncertainty routing 2026"
8. Search OpenReview for: "selective formal verification"
9. Search OpenReview for: "pseudo-formal verification"
10. "Barkallah pseudo-formalization 2026"
11. "Safe Liu ACL 2025 formal verification lean"
12. "Mu adaptive verification allocation 2026"
13. "Bhatt uncertainty guided selective verification 2025"

For each search, report:
- The query used
- Key results found (titles, authors, dates, venues)
- Whether any result is highly similar to the proposed idea

Be thorough — this is critical for novelty checking. Report ALL findings, even tangentially related ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "947143f6-0280-4e23-9d5c-343f1f5743e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T12:17:52.635Z_

```json
{
  "parentUuid": "947143f6-0280-4e23-9d5c-343f1f5743e0",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
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
  "uuid": "c363d0ea-091f-4a7c-b375-445e5f745182",
  "timestamp": "2026-05-27T12:17:52.635Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T12:17:52.636Z_

```json
{
  "parentUuid": "c363d0ea-091f-4a7c-b375-445e5f745182",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "19c38851-e972-4b67-bdf5-e00bfcb87733",
  "timestamp": "2026-05-27T12:17:52.636Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T12:17:55.799Z_



I'll conduct a thorough search for concurrent and competing work. Let me start by loading the WebSearch tool, then run all 13 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19c38851-e972-4b67-bdf5-e00bfcb87733",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RNQDmesTzKzV7CwNA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29139337-9c09-452b-b9e9-ae9b7f65d8c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgwgzeJxYcBDt1uAZfqJao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9088,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9088,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-27T12:17:56.036Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019aw9ZXvX22ZLwVTTF4PBua`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29139337-9c09-452b-b9e9-ae9b7f65d8c8",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RNQDmesTzKzV7CwNA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e6d9615-8adb-4860-81f8-48bf4d339ca5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgwgzeJxYcBDt1uAZfqJao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9088,
      "cache_read_input_tokens": 0,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9088,
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

_source line 6 · 2026-05-27T12:17:56.040Z_

<details><summary>↩ Tool result · `toolu_019aw9ZXvX22ZLwVTTF4PBua`</summary>

````text
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
  "parentUuid": "3e6d9615-8adb-4860-81f8-48bf4d339ca5",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "764699de-74cd-41a6-95d1-c7e7bc7fcb34",
  "sourceToolAssistantUUID": "3e6d9615-8adb-4860-81f8-48bf4d339ca5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T12:18:03.450Z_



Now let me run the first batch of searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "764699de-74cd-41a6-95d1-c7e7bc7fcb34",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33d17a38-670d-468a-a2aa-c1a62a8e9a0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 8 · 2026-05-27T12:18:03.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRSgW7XEwK99qrxsPgKdXA`</summary>

```json
{
  "query": "selective formal verification uncertainty 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33d17a38-670d-468a-a2aa-c1a62a8e9a0b",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdde0e3a-839b-4c64-8b67-c55472343c90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 9 · 2026-05-27T12:18:04.236Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XjFmUaEesfWJExSy9sCNQq`</summary>

```json
{
  "query": "pseudo-formal autoformalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdde0e3a-839b-4c64-8b67-c55472343c90",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e265745-dc5c-429b-abd5-caeae0dd48c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 10 · 2026-05-27T12:18:04.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1L1BLGE39BnGirnesCJKL`</summary>

```json
{
  "query": "adaptive verification mathematical proof 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e265745-dc5c-429b-abd5-caeae0dd48c3",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "899b58fe-d8a7-47ea-8ed4-92b266820b90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 11 · 2026-05-27T12:18:04.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9oyHpgr9JTdVa1Ajr1xbR`</summary>

```json
{
  "query": "uncertainty guided proof verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "899b58fe-d8a7-47ea-8ed4-92b266820b90",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b21d52b-967f-4860-a757-3c675f1abc4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 12 · 2026-05-27T12:18:04.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011kGPhMSjXmWGjSDkaPzJ27`</summary>

```json
{
  "query": "selective autoformalization natural language proof 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b21d52b-967f-4860-a757-3c675f1abc4c",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4RdEhBa6WgGNCBZedh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dfe4f8a-918c-472a-b4d0-240ba368f38b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RKeaR3AhGhQuwjbK5Jxix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 9088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 13 · 2026-05-27T12:18:10.028Z_

<details><summary>↩ Tool result · `toolu_01DRSgW7XEwK99qrxsPgKdXA`</summary>

```text
Web search results for query: "selective formal verification uncertainty 2026"

Links: [{"title":"Formal Verification Challenges: Adoption Issues & Practical Limits","url":"https://alpinumconsulting.com/blogs/verification/strategic-issues-adopting-formal-verification/"},{"title":"Verification, Validation, and Uncertainty Quantification Symposium 2026","url":"https://event.asme.org/VandV"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Formal Verification – Why It Matters | PQShield","url":"https://pqshield.com/formal-verification-why-it-matters/"},{"title":"Statistical Frameworks for Uncertainty in Agentic Systems | ICML 2026 Workshop","url":"https://agentic-uncertainty-icml2026.github.io/"},{"title":"FOSDEM 2026 - Formal Verification in Rocq, an Exhaustive Testing","url":"https://fosdem.org/2026/schedule/event/KLZJ8Y-formal_verification_in_rocq_an_exhaustive_testing/"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=QfKpJ00t2L"},{"title":"Formal verification under uncertainty | TransferLab — appliedAI Institute","url":"https://transferlab.ai/series/formal-verification-under-uncertainty/"}]

Based on the search results, here are the key findings related to selective formal verification and uncertainty in 2026:

## Selective Formal Verification

Effective adoption of formal verification requires deliberate system-level decisions about where, when, and how formal techniques are applied. Selective formal deployment is based on classification of formal-friendly and simulation-friendly design blocks.

## Formal Uncertainty in AI-Generated Formal Artifacts

A recent research paper addresses a critical challenge in using Large Language Models for formal verification. A fundamental tension exists because LLMs are probabilistic while formal verification demands deterministic guarantees, requiring comprehensive investigation of failure modes and uncertainty quantification in LLM-generated formal artifacts.

The research introduces a lightweight fusion of uncertainty signals that enables selective verification, drastically reducing errors (14-100%) with minimal abstention. Importantly, uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93).

## Broader Uncertainty Research in 2026

An ICML 2026 workshop provides a focused venue for discussion at the intersection of modern agentic systems and rigorous uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdde0e3a-839b-4c64-8b67-c55472343c90",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "2392b41c-7ff6-4c30-9d23-b33a4aa3ca74",
  "sourceToolAssistantUUID": "fdde0e3a-839b-4c64-8b67-c55472343c90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T12:18:11.725Z_

<details><summary>↩ Tool result · `toolu_01XjFmUaEesfWJExSy9sCNQq`</summary>

```text
Web search results for query: "pseudo-formal autoformalization 2026"

Links: [{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Autoformalization and the Future of Math Research","url":"https://www.neelsomaniblog.com/p/autoformalization-and-the-future"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260103298U/abstract"},{"title":"Towards a Common Framework for Autoformalization | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/42132"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2601.03298] 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/abs/2601.03298"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Towards a Common Framework for Autoformalization","url":"https://ojs.aaai.org/index.php/AAAI/article/download/42132/46093"}]

Based on the search results, here's what I found about pseudo-formal autoformalization in 2026:

## Pseudo-Formalization Approach

Pseudo-Formalization can be viewed as a relaxation of autoformalization, where a natural language proof is translated to a fully formal language and then checked for correctness. Autoformalization targets a formal language like Lean, paired with a compiler, while pseudo-formalization instead targets a structured natural-language representation, paired with an LLM running Block Verification.

## Recent Developments in Autoformalization

The field of autoformalization has seen significant activity in 2026. A major autoformalization project has autoformalized a large portion of general topology from the Munkres textbook, producing 160k lines of formalized topology as of January 4, 2026, with about 130k lines completed in two weeks for an LLM subscription cost of about $100. The approach involves a feedback loop between an LLM (ChatGPT 5.2 or Claude Sonnet 4.5) and a proof checker called Megalodon equipped with a core foundational library.

Additionally, there are efforts to propose a unified framework for autoformalization to encourage cross-pollination between different research fields.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e265745-dc5c-429b-abd5-caeae0dd48c3",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "eadf2ab6-9c7b-4b7f-aba7-d964088d3636",
  "sourceToolAssistantUUID": "6e265745-dc5c-429b-abd5-caeae0dd48c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T12:18:12.031Z_

<details><summary>↩ Tool result · `toolu_011kGPhMSjXmWGjSDkaPzJ27`</summary>

```text
Web search results for query: "selective autoformalization natural language proof 2026"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"Autoformalization with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=IUikebJ1Bf0"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"Autoformalization in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.23486"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Autoformalization with Large Language Models","url":"https://research.google/pubs/autoformalization-with-large-language-models/"},{"title":"Towards Autoformalization of Mathematics and Code Correctness:   Experiments with Elementary Proofs","url":"https://arxiv.org/pdf/2301.02195"}]

Here are the search results for "selective autoformalization natural language proof 2026":

The search returned several recent papers and projects related to autoformalization in 2026:

1. **FormalEvolve** - A neuro-symbolic evolutionary search approach for autoformalization that aims to translate natural-language mathematics into compilable, machine-checkable statements. This work was submitted on March 20, 2026.

2. **AI for Math Workshop at ICML 2026** - A challenge track for generating formal proofs in Lean 4 from natural language informal proofs, with a challenge period from May 1 – June 15, 2026.

3. **ProofBridge** - A unified framework for automatically translating entire natural language theorems and proofs into Lean 4, which was last updated on March 29, 2026.

4. **Autoformalization Robustness Studies** - Recent work evaluating how large language models generate formal proofs from semantically similar paraphrased natural language statements by measuring semantic and compilation validity.

5. **130k Lines of Formal Topology** - A simple approach using feedback loops between LLMs and proof checkers, suggesting that autoformalization may become quite easy and ubiquitous in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dfe4f8a-918c-472a-b4d0-240ba368f38b",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "ec76605c-f5be-49f7-89e9-2c1a3624aa32",
  "sourceToolAssistantUUID": "1dfe4f8a-918c-472a-b4d0-240ba368f38b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T12:18:12.879Z_

<details><summary>↩ Tool result · `toolu_01F1L1BLGE39BnGirnesCJKL`</summary>

```text
Web search results for query: "adaptive verification mathematical proof 2026"

Links: [{"title":"ALEXI | Advanced Mathematics Learning Platform | Adaptive Practice & Proof Verification","url":"https://alexilearning.com/"},{"title":"MiniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification (Dafny 2026) - POPL 2026","url":"https://popl26.sigplan.org/details/dafny-2026-papers/16/MiniF2F-Dafny-LLM-Guided-Mathematical-Theorem-Proving-via-Auto-Active-Verification"},{"title":"AI Verifies Mathematical Proofs Step-by-Step, Improving Formal Verification Success.","url":"https://quantumzeitgeist.com/ai-verifies-mathematical-proofs-step-by-step-improving-formal-verification-success/"},{"title":"AI and Humans Verify Fields Medal Proof for the First Time","url":"https://spectrum.ieee.org/ai-proof-verification"},{"title":"Adaptive Proof Refinement with LLM-Guided Strategy Selection","url":"https://arxiv.org/pdf/2510.25103"},{"title":"ChatGPT can provide original mathematical proofs, researchers show","url":"https://phys.org/news/2026-03-chatgpt-mathematical-proofs.html"}]

Here are the search results for "adaptive verification mathematical proof 2026":

**Key Findings:**

1. **ADAPT Framework**: A novel proof refinement framework that leverages an LLM-guided decision-maker to dynamically select a suitable refinement strategy according to the state of the proof assistant and available context of an incorrect proof. This framework significantly outperforms baseline methods on two benchmarks by proving 16.63% and 18.58% more theorems, respectively.

2. **AI-Assisted Mathematical Proof Verification**: Fields Medal–winning mathematical work about optimal sphere packing in many dimensions is now formally verified by a human-AI collaboration.

3. **Step-by-Step Verification**: StepProof, a new autoformalisation method, facilitates granular, sentence-level verification of mathematical proofs, addressing a limitation of existing systems which typically verify complete proofs only.

4. **Theorem Proving Advancements**: MiniF2F-Dafny is the first translation of the mathematical reasoning benchmark miniF2F to an automated theorem prover, with Dafny's automation verifying 40.6% of the test set and 44.7% of the validation set with empty proofs.

5. **ALEXI Platform**: ALEXI is a personalized digital learning platform for advanced mathematics launching in 2026.

These results highlight significant advances in adaptive verification techniques for mathematical proofs in 2026, particularly in leveraging AI and LLMs to assist with proof generation and verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "899b58fe-d8a7-47ea-8ed4-92b266820b90",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "05c07a00-8c3d-4f5d-a7c0-6d634da58919",
  "sourceToolAssistantUUID": "899b58fe-d8a7-47ea-8ed4-92b266820b90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T12:18:13.410Z_

<details><summary>↩ Tool result · `toolu_01V9oyHpgr9JTdVa1Ajr1xbR`</summary>

```text
Web search results for query: "uncertainty guided proof verification"

Links: [{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"ExVerus: Verus Proof Repair via Counterexample Reasoning","url":"https://arxiv.org/pdf/2603.25810"},{"title":"A Protocol for Trustless Verification Under Uncertainty","url":"https://arxiv.org/html/2507.00631"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"[1705.00519] Towards Verification of Uncertain Cyber-Physical Systems","url":"https://arxiv.org/abs/1705.00519"},{"title":"New research shows how Proof-Based Scanning cuts through uncertainty","url":"https://www.invicti.com/blog/web-security/cutting-through-uncertainty-proof-based-scanning-announcing-white-paper"}]

Based on the search results, here's what I found about uncertainty guided proof verification:

## Key Research Findings

The primary research involves leveraging uncertainty quantification to enhance the reliability of step-wise verification with generative reward models for mathematical reasoning tasks, introducing a method called CoT Entropy that outperforms existing approaches in quantifying a process reward model's uncertainty in step-wise verification.

Process supervision via process reward models provides intermediate rewards to verify step-wise correctness in solution traces, which is an improvement over outcome supervision alone. However, as proxies for human judgment, PRMs suffer from reliability issues, including susceptibility to reward hacking.

Incorporating uncertainty estimates improves the robustness of judge-LM process reward models, leading to more reliable verification.

## Related Context

The search also found work on diverse downstream applications of theorem proving and symbolic reasoning, where LLMs closely cooperate with solvers for constraint satisfaction, verification, symbolic interfaces, iteration-based reasoning, and uncertainty modeling.

The most recent work on this topic (from February 2025) focuses specifically on using uncertainty quantification methods to make mathematical proof verification more reliable and resistant to failure modes in large language model-based reasoning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b21d52b-967f-4860-a757-3c675f1abc4c",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "f8d61317-db18-4bae-87d4-26beb0fbda93",
  "sourceToolAssistantUUID": "0b21d52b-967f-4860-a757-3c675f1abc4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T12:18:16.350Z_

Good, I have the first 5 results. Now let me run searches 6-10.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d61317-db18-4bae-87d4-26beb0fbda93",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93004d07-2916-4a72-a5ab-59595be071ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
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

_source line 19 · 2026-05-27T12:18:16.831Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KahqHEXZgPi2XMKo8dBj7C`</summary>

```json
{
  "query": "autoformalization selective verification 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93004d07-2916-4a72-a5ab-59595be071ca",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "827285fc-0f4b-4b9b-a2a4-190643d3f094",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
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

_source line 20 · 2026-05-27T12:18:17.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012EebSSCDM6LgaUDTVgKw9e`</summary>

```json
{
  "query": "proof verification uncertainty routing 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827285fc-0f4b-4b9b-a2a4-190643d3f094",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "334356b9-2a26-435b-a420-33c4d86d5f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
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

_source line 21 · 2026-05-27T12:18:17.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013oSzwvbrj55Bc6uydguZoP`</summary>

```json
{
  "query": "selective formal verification site:openreview.net"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "334356b9-2a26-435b-a420-33c4d86d5f3d",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7d80bac-f483-404b-b9e9-88b20caadeca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
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

_source line 22 · 2026-05-27T12:18:18.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0124fTDwVUg5Do2apstk9ViQ`</summary>

```json
{
  "query": "pseudo-formal verification site:openreview.net"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d80bac-f483-404b-b9e9-88b20caadeca",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40c7ff7c-6c1f-4bc2-b7a4-1fdc0c6902b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
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

_source line 23 · 2026-05-27T12:18:18.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DEn3YkG635BrmUAEdGpfKa`</summary>

```json
{
  "query": "Barkallah pseudo-formalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c7ff7c-6c1f-4bc2-b7a4-1fdc0c6902b8",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4SuBfV8ZfC8CFVmCmd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b61f85-dc2e-4056-bdb5-bce7e7362ecb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iXVTgk54ULRyWeVuL43gC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 770,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 9726,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 770,
          "output_tokens": 271,
          "cache_read_input_tokens": 9726,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2959,
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

_source line 24 · 2026-05-27T12:18:23.768Z_

<details><summary>↩ Tool result · `toolu_01DEn3YkG635BrmUAEdGpfKa`</summary>

```text
Web search results for query: "Barkallah pseudo-formalization 2026"

Links: [{"title":"“I Wanted Them to Think That I Wrote That”: AI-Generated Self-Presentation on Dating Apps and Implications of Non-Disclosure on Informed Consent | Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3772318.3791593"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Aymen BARKALLAH - A2B structure | LinkedIn","url":"https://www.linkedin.com/in/aymen-barkallah-a43487177/"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"FMTea 2026","url":"https://fmtea.github.io/"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"},{"title":"A fake plane via 2-adic uniformization with torsion","url":"https://arxiv.org/pdf/1411.1140"}]

Based on the search results, I found a relevant match:

Manel Barkallah and Jean-Marie Jacquet presented a paper titled "Learning Formal Methods through Project-Based Modeling of Concurrent Systems with Anemone" at the FMTea 2026 (Formal Methods Teaching Workshop) in Tokyo, Japan on May 19, 2026.

The search results show this is related to formal methods teaching and education, specifically on using project-based learning with the Anemone tool for teaching concurrent systems modeling. However, the search results don't contain specific details about "pseudo-formalization" in the context of this work. If you're looking for more specific information about this paper or concept, I'd recommend checking the FMTea 2026 proceedings directly or searching for the paper on academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11b61f85-dc2e-4056-bdb5-bce7e7362ecb",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "b1a19c5f-86c8-43be-9549-0dba41041a76",
  "sourceToolAssistantUUID": "11b61f85-dc2e-4056-bdb5-bce7e7362ecb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T12:18:24.530Z_

<details><summary>↩ Tool result · `toolu_013oSzwvbrj55Bc6uydguZoP`</summary>

```text
Web search results for query: "selective formal verification site:openreview.net"

Links: [{"title":"Fully Automatic Neural Network Reduction for Formal Verification | OpenReview","url":"https://openreview.net/forum?id=gmflcWlVMl"},{"title":"Formal Verification for Neural Networks with General Nonlinearities via Branch-and-Bound | OpenReview","url":"https://openreview.net/forum?id=ivokwVKY4o"},{"title":"Formal Verification of Graph Convolutional Networks with Uncertain Node Features and Uncertain Graph Structure | OpenReview","url":"https://openreview.net/forum?id=B6y12Ot0cP"},{"title":"FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving | OpenReview","url":"https://openreview.net/forum?id=d0gMFgrYFB"},{"title":"AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement | OpenReview","url":"https://openreview.net/forum?id=tU8QKX4dMI"},{"title":"VeriFlow: Modeling Distributions for Neural Network Verification | OpenReview","url":"https://openreview.net/forum?id=pWrCiFpm3L"},{"title":"VeriBench: End-to-End Formal Verification Benchmark for AI Code Generation in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=rWkGFmnSNl"}]

I found several papers on OpenReview related to formal verification. The search results include papers on:

1. **Neural Network Reduction for Formal Verification** - A fully automatic and sound reduction of neural networks using reachability analysis, where soundness ensures that verification of the reduced network entails verification of the original network.

2. **Branch-and-Bound Methods** - Bound propagation with branch-and-bound is among the most effective methods for neural network verification, with frameworks extending to models with various nonlinearities beyond ReLU.

3. **Graph Convolutional Networks Verification** - Research addressing verification of generic graph convolutional network architectures with uncertainty in node features and graph structure through reachability analysis.

4. **Interactive Verification with LLMs** - FVEL, an interactive Formal Verification Environment with LLMs that transforms code into Isabelle and conducts verification via neural automated theorem proving.

5. **AlphaVerus** - A self-improving framework that bootstraps formally verified code generation by iteratively translating programs and leveraging feedback from a verifier.

6. **VeriFlow** - A flow-based density model tailored to allow verification approaches to restrict their search to a specific data distribution of interest.

7. **VeriBench** - A Lean-4 benchmark that tests whether LLM-powered agents can translate real Python code into fully proved, machine-checkable implementations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d80bac-f483-404b-b9e9-88b20caadeca",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "71653145-7596-4e96-87b3-5c7959846510",
  "sourceToolAssistantUUID": "f7d80bac-f483-404b-b9e9-88b20caadeca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T12:18:24.844Z_

<details><summary>↩ Tool result · `toolu_0124fTDwVUg5Do2apstk9ViQ`</summary>

```text
Web search results for query: "pseudo-formal verification site:openreview.net"

Links: [{"title":"Formal Verification for Neural Networks with General Nonlinearities via Branch-and-Bound | OpenReview","url":"https://openreview.net/forum?id=ivokwVKY4o"},{"title":"STL-Drive: Formal Verification Guided End-to-end Automated Driving | OpenReview","url":"https://openreview.net/forum?id=DCg9r2DKKe"},{"title":"Fully Automatic Neural Network Reduction for Formal Verification | OpenReview","url":"https://openreview.net/forum?id=gmflcWlVMl"},{"title":"Fundamental Limits in Formal Verification of Message-Passing Neural Networks | OpenReview","url":"https://openreview.net/forum?id=WlbG820mRH-"},{"title":"A Formal Verification Framework for LLM-Generated Causal Expressions | OpenReview","url":"https://openreview.net/forum?id=hCCCOtPQYJ"},{"title":"StepProof: Step-by-step verification of natural language mathematical proofs | OpenReview","url":"https://openreview.net/forum?id=EXaKfdsw04"},{"title":"Re:Form --- Reducing Human Priors in Scalable Formal Software Verification with RL in LLMs: A Preliminary Study on Dafny | OpenReview","url":"https://openreview.net/forum?id=cAQmIS4GOe"}]

I found several research papers on OpenReview related to formal verification. However, I should note that the search results don't appear to contain papers specifically about "pseudo-formal verification" as a distinct topic. Instead, the results show various papers on formal verification techniques applied to different domains:

1. **Neural Network Verification**: Papers on verifying neural networks using branch-and-bound methods, formal verification frameworks for different activation functions and architectures.

2. **Automated Driving**: A paper that incorporates Signal Temporal Logic (STL) as a formal method to impose safety constraints and combines task objectives with STL robustness scores in a loss function.

3. **Network Reduction**: A paper introducing automatic and sound reduction of neural networks using reachability analysis, where soundness ensures that verification of the reduced network entails verification of the original network.

4. **Graph Neural Networks**: A paper showing that formal verification is impossible for certain Message Passing Neural Networks, particularly for graph-classifier MPNN working over graphs of unbounded size.

5. **LLM-Based Applications**: Papers on formal verification frameworks for LLM-generated causal expressions and step-by-step verification of mathematical proofs.

If you're looking for papers specifically about "pseudo-formal verification," you may want to refine your search or check if there are papers that use different terminology for this concept.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40c7ff7c-6c1f-4bc2-b7a4-1fdc0c6902b8",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "2c2facbe-ee26-402f-9b11-29c8f9b96e57",
  "sourceToolAssistantUUID": "40c7ff7c-6c1f-4bc2-b7a4-1fdc0c6902b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T12:18:24.875Z_

<details><summary>↩ Tool result · `toolu_01KahqHEXZgPi2XMKo8dBj7C`</summary>

```text
Web search results for query: "autoformalization selective verification 2026 site:arxiv.org"

Links: [{"title":"GDPR Auto-Formalization with AI Agents and Human Verification","url":"https://arxiv.org/html/2604.14607"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"[2604.25031] Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/abs/2604.25031"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"[2602.16554] MerLean: An Agentic Framework for Autoformalization in Quantum Computation","url":"https://arxiv.org/abs/2602.16554"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"}]

Based on the search results from arxiv.org, here are the papers related to autoformalization and selective verification from 2026:

## Key Papers Found:

1. **"GDPR Auto-Formalization with AI Agents and Human Verification"** (arxiv:2604.14607)
   This paper addresses legal formalization: translating legal norms into machine-executable representations for automated reasoning and compliance assessment. The human verification stage was conducted by six annotators with prior academic and applied experience in artificial intelligence and legal reasoning, with each annotator evaluating a distinct subset of instances.

2. **"Faithful Autoformalization via Roundtrip Verification and Repair"** (arxiv:2604.25031)
   The paper proposes a roundtrip verification approach: formalize a statement, translate the result back to natural language, re-formalize, and use a formal tool to check logical equivalence; when they disagree, a diagnosis step identifies which translation stage failed, and a targeted repair operator attempts to correct that stage. Diagnosis-guided repair raises formal equivalence from 45--61% to 83--85% for both models.

3. **"MerLean: An Agentic Framework for Autoformalization in Quantum Computation"** (arxiv:2602.16554)
   MerLean achieves end-to-end formalization on all three papers, reducing the verification burden to only the newly introduced definitions and axioms.

These papers demonstrate advances in selective/targeted verification approaches for autoformalization in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "827285fc-0f4b-4b9b-a2a4-190643d3f094",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "8cf77bd0-0433-4cb0-a704-c4f0ae0881ad",
  "sourceToolAssistantUUID": "827285fc-0f4b-4b9b-a2a4-190643d3f094",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T12:18:28.196Z_

<details><summary>↩ Tool result · `toolu_012EebSSCDM6LgaUDTVgKw9e`</summary>

```text
Web search results for query: "proof verification uncertainty routing 2026 site:arxiv.org"

Links: [{"title":"[2605.18796] UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/abs/2605.18796"},{"title":"Uncertainty in Multi-Commodity Routing Networks: When does it help?","url":"https://arxiv.org/pdf/1709.08441"},{"title":"STARVERI: Efficient and Accurate Verification for Risk-Avoidance Routing   in LEO Satellite Networks","url":"https://arxiv.org/pdf/2412.16496"},{"title":"Submitted as a conference paper at ICLR 2026 TYPED CHAIN-OF-THOUGHT:","url":"https://arxiv.org/pdf/2510.01069"},{"title":"A Review of Automated Formal Verification of Ad Hoc Routing Protocols   for Wireless Sensor Networks","url":"https://arxiv.org/pdf/1305.7410"},{"title":"CP-Router: An Uncertainty-Aware Router Between LLM and LRM","url":"https://arxiv.org/pdf/2505.19970"},{"title":"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/html/2605.18796"}]

Based on the search results, I found several relevant papers on arxiv.org related to uncertainty and routing. Here are the key findings:

## Most Recent Results (May 2026)

The most directly relevant paper is UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing, submitted on May 11, 2026. This paper presents UCCI, a calibration-first router that maps token-level margin uncertainty to a per-query error probability via isotonic regression and selects the escalation threshold by constrained cost minimization.

## Related Papers

Another recent paper in this space is CP-Router, which addresses how to dynamically route prompts between an LLM and an LRM to minimize computational cost without sacrificing accuracy.

Other papers in the search results address related topics:
- STARVERI presents a network path verification framework for LEO satellite networks that addresses verification limitations through dynamic relay selection and lightweight path verification algorithms
- A paper on Proof-Carrying Chain-of-Thought discusses future work exploring richer type systems incorporating modal logic and uncertainty, and integration with formal proof assistants for complete verification

The search results show active research in 2026 on combining uncertainty quantification with routing mechanisms, particularly for large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "334356b9-2a26-435b-a420-33c4d86d5f3d",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "3cb75802-b73e-4dfa-9489-81ea4f9fcbe2",
  "sourceToolAssistantUUID": "334356b9-2a26-435b-a420-33c4d86d5f3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-27T12:18:31.684Z_

Now let me run the remaining searches 11-13, plus a few follow-up searches on the most promising leads I've found so far.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cb75802-b73e-4dfa-9489-81ea4f9fcbe2",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4TzRDPEfYqst7BdU1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "127a9aa7-e9c9-43da-8d14-3a0d73a235d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVwZreXUZ8qABPh2vme58V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2042,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 12685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 30 · 2026-05-27T12:18:32.159Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AjgQWtoUdkRVNXamxpHPJi`</summary>

```json
{
  "query": "Safe Liu ACL 2025 formal verification lean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "127a9aa7-e9c9-43da-8d14-3a0d73a235d6",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4TzRDPEfYqst7BdU1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42838b72-c087-4e6d-a4b0-c200f1a868bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVwZreXUZ8qABPh2vme58V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2042,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 12685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 31 · 2026-05-27T12:18:32.690Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X37z2uTxLxY5w6NgWAf1nd`</summary>

```json
{
  "query": "Mu adaptive verification allocation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42838b72-c087-4e6d-a4b0-c200f1a868bd",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4TzRDPEfYqst7BdU1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27188222-38df-4487-a203-e8130fa8bf0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVwZreXUZ8qABPh2vme58V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2042,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 12685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2436,
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

_source line 32 · 2026-05-27T12:18:33.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WS6Wa9Jqc5A2nxtPdh2CWY`</summary>

```json
{
  "query": "Bhatt uncertainty guided selective verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27188222-38df-4487-a203-e8130fa8bf0c",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4TzRDPEfYqst7BdU1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cbbd422-51dc-4a0b-bf7b-dc52c64c72c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVwZreXUZ8qABPh2vme58V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2042,
      "cache_creation_input_tokens": 2436,
      "cache_read_input_tokens": 12685,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2436
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2042,
          "output_tokens": 179,
          "cache_read_input_tokens": 12685,
          "cache_creation_input_tokens": 2436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2436,
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

_source line 33 · 2026-05-27T12:18:39.275Z_

<details><summary>↩ Tool result · `toolu_01AjgQWtoUdkRVNXamxpHPJi`</summary>

```text
Web search results for query: "Safe Liu ACL 2025 formal verification lean"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250604592L/abstract"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"VeriBench: End-to-End Formal Verification Benchmark for ...","url":"https://openreview.net/pdf?id=rWkGFmnSNl"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291"}]

Based on the search results, I found information about the paper "Safe" by Liu and colleagues at ACL 2025:

Safe is a retrospective, step-aware formal verification framework that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to address hallucinations in Chain-of-Thought prompting from large language models.

The work represents the first endeavor to utilize formal mathematical language Lean 4 for verifying content generated by LLMs, which aligns with the original purpose of formal mathematical languages in providing a robust foundation for verification.

The researchers also propose FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements. The framework Safe was evaluated across multiple language models and various mathematical datasets, demonstrating significant performance improvement while offering interpretable and verifiable evidence.

The authors include Chengwu Liu, Ye Yuan, Yichun Yin, Yan Xu, Xin Xu, Zaoyu Chen, Yasheng Wang, Lifeng Shang, Qun Liu, and Ming Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42838b72-c087-4e6d-a4b0-c200f1a868bd",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "4b0253c2-ef54-49d9-82cb-ba7aaa4f981e",
  "sourceToolAssistantUUID": "42838b72-c087-4e6d-a4b0-c200f1a868bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T12:18:39.501Z_

<details><summary>↩ Tool result · `toolu_01X37z2uTxLxY5w6NgWAf1nd`</summary>

```text
Web search results for query: "Mu adaptive verification allocation 2026"

Links: [{"title":"Mumbai University UG Admission First Merit List 2026 Out, Download UG Course Merit List PDF @mu.ac.in – Karmasandhan","url":"https://www.karmasandhan.com/mumbai-university-ug-admission-first-merit-list-2026/"},{"title":"A Novel Human–Machine Shared Control Strategy with Adaptive Authority Allocation Considering Scenario Complexity and Driver Workload","url":"https://doi.org/10.3390/act15010051"},{"title":"Statistical Frameworks for Uncertainty in Agentic Systems | ICML 2026 Workshop","url":"https://agentic-uncertainty-icml2026.github.io/"},{"title":"MU OET 2026 Counselling - Registration, Documents, Seat Allotment, Fees, Procedure and Online Reporting","url":"https://www.collegedekho.com/exam/mu-oet/counselling-process"},{"title":"Resilient Control with Adaptive Control Allocation for Uncertain Over-Actuated Systems in the Presence of Unknown Actuator Degradation","url":"https://www.mdpi.com/2813-4648/4/2/15"},{"title":"QoE Fairness‐Aware MADRL‐Based Bitrate Allocation in Adaptive Video Streaming - Liu - 2026 - Transactions on Emerging Telecommunications Technologies - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/ett.70398"},{"title":"🍀MU: Pocket Knights First Roadmap of year 2026 ...","url":"https://www.facebook.com/MUPocketKnightsGlobal/posts/mu-pocket-knights-first-roadmap-of-year-2026-revealedwe-proudly-present-you-our-/122159970158938622/"},{"title":"Mu Digital partners with Curated and Plums to bring institutional-grade Asian credit to Ethereum","url":"https://cointelegraph.com/press-releases/mu-digital-partners-with-curated-and-plums-to-bring-institutional-grade-asian-credit-to-ethereum"},{"title":"Collection: UAV-Based Wireless Multi-modal Measurements from AERPAW Autonomous Data Mule (AADM) Challenge in Digital Twin and Real-World Environments","url":"https://arxiv.org/html/2602.16163v2"}]

Based on the search results, the query "Mu adaptive verification allocation 2026" appears to match information about **Mumbai University's UG (Undergraduate) Admission Process for 2026**.

Here are the relevant findings:

## Mumbai University UG Admission 2026

The University of Mumbai (MU) released the First Merit List for undergraduate (UG) admissions for the academic year 2026-27 on 26th May 2026.

### Document Verification and Allocation Timeline
The online document verification and fee payment window is from 27th May to 29th May 2026, with the deadline closing at 3 PM on 29th May.

### Allocation Process
Mumbai University has released the list of provisionally selected candidates who must complete document verification and fee payment. The allotment is provisional and subject to successful verification of original documents.

### Next Steps
Selected candidates must complete online document verification and fee payment, and the Second Merit List will be released on 30th May 2026 for remaining vacant seats.

The search results also show some academic and technical papers about adaptive control allocation systems, but these don't appear to be related to your specific query about Mumbai University admissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27188222-38df-4487-a203-e8130fa8bf0c",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "98260bf3-472e-40c9-89ef-1865ae4080c4",
  "sourceToolAssistantUUID": "27188222-38df-4487-a203-e8130fa8bf0c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T12:18:44.899Z_

<details><summary>↩ Tool result · `toolu_01WS6Wa9Jqc5A2nxtPdh2CWY`</summary>

```text
Web search results for query: "Bhatt uncertainty guided selective verification 2025"

Links: [{"title":"VVUQ 2025 | Verification, Validation, and Uncertainty Quantification","url":"https://event.asme.org/VandV-2025"},{"title":"[2511.12006] Uncertainty-Guided Selective Adaptation Enables Cross-Platform Predictive Fluorescence Microscopy","url":"https://arxiv.org/abs/2511.12006"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"A Complete Framework for Verification, Validation, and Uncertainty Quantification in Scientific Computing (Invited) | Request PDF","url":"https://www.researchgate.net/publication/241077911_A_Complete_Framework_for_Verification_Validation_and_Uncertainty_Quantification_in_Scientific_Computing_Invited"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Contents - Verification, Validation, and Uncertainty Quantification in Scientific Computing","url":"https://www.cambridge.org/core/books/abs/verification-validation-and-uncertainty-quantification-in-scientific-computing/contents/CB6D2C946830DE6A9E8A424D4B124B92"}]

Based on the search results, I found a paper that matches your query:

"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" is a 2025 paper that evaluates LLMs on Satisfiability Modulo Theories (SMT) based autoformalization and introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs for uncertainty quantification.

The paper finds that uncertainty signals are task-dependent and demonstrates that a lightweight fusion of these signals enables selective verification, which can drastically reduce errors (14-100%) with minimal abstention.

However, I should note that the search results do not show "Bhatt" as an author name associated with this specific work on "uncertainty guided selective verification." The results do show other papers on related topics of uncertainty quantification and verification, but the specific attribution you're asking about doesn't clearly appear in these search results. If you're looking for a specific author or paper with different keywords, I'd be happy to perform another search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cbbd422-51dc-4a0b-bf7b-dc52c64c72c9",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "79e5348d-2bb1-4582-9279-a9e6e3d158a1",
  "sourceToolAssistantUUID": "6cbbd422-51dc-4a0b-bf7b-dc52c64c72c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-27T12:18:48.469Z_

Let me now do some critical follow-up searches on the most relevant findings, particularly the "pseudo-formalization" paper and the "Grammars of Formal Uncertainty" paper, which seem highly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e5348d-2bb1-4582-9279-a9e6e3d158a1",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4VDp9b5zQQkyFjvS16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d60b88ab-6591-4c5f-af40-96a83cad38e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBfmYfJwXpikrLffJprtof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 15121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 37 · 2026-05-27T12:18:49.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nn5ovmyGT3ct4TxpZoV6wY`</summary>

```json
{
  "query": "arxiv 2605.20531 pseudo-formalization automatic proof verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d60b88ab-6591-4c5f-af40-96a83cad38e8",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4VDp9b5zQQkyFjvS16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71296341-fcb4-4347-bbb0-b1ee02592839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBfmYfJwXpikrLffJprtof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 15121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 38 · 2026-05-27T12:18:49.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FwM2N8Z1mSv17ewkRTcHgD`</summary>

```json
{
  "query": "\"Grammars of Formal Uncertainty\" LLM automated reasoning selective verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71296341-fcb4-4347-bbb0-b1ee02592839",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4VDp9b5zQQkyFjvS16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5c4d569-e55d-48f1-b7e0-ffe757507024",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBfmYfJwXpikrLffJprtof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 15121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 39 · 2026-05-27T12:18:50.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KHYn5SARfRRkLvRmNaWxkS`</summary>

```json
{
  "query": "StepProof step-by-step verification natural language mathematical proofs autoformalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5c4d569-e55d-48f1-b7e0-ffe757507024",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4VDp9b5zQQkyFjvS16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8bb189f-abfb-4368-8471-1ef66ebd1f09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBfmYfJwXpikrLffJprtof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 15121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4554,
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

_source line 40 · 2026-05-27T12:18:50.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R51jRuuhDqSZ5peSA1x7nh`</summary>

```json
{
  "query": "\"pseudo-formal\" \"block verification\" proof decomposition LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8bb189f-abfb-4368-8471-1ef66ebd1f09",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4VDp9b5zQQkyFjvS16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77f89c18-f56a-4601-a45c-cc9dc4f415df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBfmYfJwXpikrLffJprtof",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4554,
      "cache_read_input_tokens": 15121,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4554
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 15121,
          "cache_creation_input_tokens": 4554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4554,
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

_source line 41 · 2026-05-27T12:18:57.496Z_

<details><summary>↩ Tool result · `toolu_01FwM2N8Z1mSv17ewkRTcHgD`</summary>

```text
Web search results for query: ""Grammars of Formal Uncertainty" LLM automated reasoning selective verification"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=QfKpJ00t2L"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/pdf/1bd62aad3dbda001bef71c29125c2be51f974644.pdf"},{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://neurips.cc/virtual/2025/poster/118114"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"},{"title":"Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://huggingface.co/papers/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047v1"}]

Based on the search results, here's what I found about "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks":

## Overview

Large language models (LLMs) show remarkable promise for democratizing automated reasoning by generating formal specifications. However, a fundamental tension exists: LLMs are probabilistic, while formal verification demands deterministic guarantees.

## Key Contribution

The paper introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy. This framework systematically captures and analyzes output uncertainty by modeling LLM-generated SMT-LIB program distributions with Probabilistic Context-Free Grammars (PCFGs).

## Main Findings

A systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like the entropy of token probabilities failing to identify these errors.

Uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93).

## Practical Application

A lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engine.

The paper was presented at NeurIPS 2025 and addresses how to reliably use LLMs for formal verification tasks by understanding when to trust their outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5c4d569-e55d-48f1-b7e0-ffe757507024",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "1ad69aa9-b234-4681-8973-fcf4d6172877",
  "sourceToolAssistantUUID": "c5c4d569-e55d-48f1-b7e0-ffe757507024",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T12:18:57.854Z_

<details><summary>↩ Tool result · `toolu_01KHYn5SARfRRkLvRmNaWxkS`</summary>

```text
Web search results for query: "StepProof step-by-step verification natural language mathematical proofs autoformalization"

Links: [{"title":"[2506.10558] StepProof: Step-by-step verification of natural language mathematical proofs","url":"https://arxiv.org/abs/2506.10558"},{"title":"[Literature Review] StepProof: Step-by-step verification of natural language mathematical proofs","url":"https://www.themoonlight.io/en/review/stepproof-step-by-step-verification-of-natural-language-mathematical-proofs"},{"title":"StepProof: Step-by-step verification of natural language mathematical proofs | OpenReview","url":"https://openreview.net/forum?id=EXaKfdsw04"},{"title":"AI Verifies Mathematical Proofs Step-by-Step, Improving Formal Verification Success.","url":"https://quantumzeitgeist.com/ai-verifies-mathematical-proofs-step-by-step-improving-formal-verification-success/"},{"title":"StepProof: Step-by-step verification of natural language mathematical proofs | Request PDF","url":"https://www.researchgate.net/publication/392628910_StepProof_Step-by-step_verification_of_natural_language_mathematical_proofs"},{"title":"stepproof: step-by-step verification of","url":"https://arxiv.org/pdf/2506.10558"},{"title":"StepProof: Step-by-step verification of natural language mathematical proofs","url":"https://arxiv.org/html/2506.10558v2"},{"title":"STEPPROOF","url":"https://openreview.net/pdf?id=EXaKfdsw04"}]

Based on the search results, here's what I found about StepProof:

## Overview

StepProof is a novel autoformalization method designed for granular, step-by-step verification that breaks down complete proofs into multiple verifiable subproofs, enabling sentence-level verification.

## The Problem It Addresses

Interactive theorem provers (ITPs) are powerful tools for the formal verification of mathematical proofs down to the axiom level, however, their lack of a natural language interface remains a significant limitation. Existing autoformalization approaches are limited to verifying complete proofs and lack the capability for finer, sentence-level verification.

## How It Works

StepProof operates by aligning informal proof steps with their corresponding formal logic equivalents, incrementally building the formal proof and verifying each step as it proceeds. The system leverages large language models to understand the natural language representation of the proof and translate it into a formal language, such as Isabelle/HOL or Coq, that can be verified by a theorem prover.

## Results

Experimental results demonstrate that StepProof significantly improves proof success rates and efficiency compared to traditional methods, and minor manual adjustments to the natural language proofs, tailoring them for step-level verification, further enhanced StepProof's performance in autoformalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8bb189f-abfb-4368-8471-1ef66ebd1f09",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "8f83e1ca-8ff0-4b54-acf3-9f99df7398b6",
  "sourceToolAssistantUUID": "d8bb189f-abfb-4368-8471-1ef66ebd1f09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-27T12:18:58.597Z_

<details><summary>↩ Tool result · `toolu_01R51jRuuhDqSZ5peSA1x7nh`</summary>

```text
Web search results for query: ""pseudo-formal" "block verification" proof decomposition LLM"

Links: [{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically","url":"https://arxiv.org/html/2411.01829v1"},{"title":"Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification","url":"https://arxiv.org/pdf/2603.19329"},{"title":"NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference","url":"https://arxiv.org/pdf/2603.18046"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/pdf/2506.12509"},{"title":"LLM-Based Code Translation Needs Formal Compositional Reasoning Alvin Cheung","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf"},{"title":"Solving Formal Math Problems by Decomposition and Iterative Reflection","url":"https://arxiv.org/pdf/2507.15225"}]

Based on the search results, I found relevant information about your query. Here's what the research shows:

Pseudo-Formalization (PF) is a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language, where a Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

Block Verification (BV) is an algorithm where an LLM translates a natural language proof to Pseudo-Formal and then verifies each module independently. More specifically, the same model verifies each module, and a calibration model aggregates the errors into a verdict under a configurable strictness threshold.

The motivation behind this approach is that reliable verification of proofs remains a bottleneck for training and evaluating AI systems on hard mathematical reasoning. While fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, most proofs, particularly those written by AI systems, have neither property, and translating them into formal languages remains challenging in many frontier math settings.

The PF+BV approach was evaluated on two benchmarks spanning olympiad and research-level mathematics, where it pareto-dominates LLM-as-judge baselines on error-finding precision and recall.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77f89c18-f56a-4601-a45c-cc9dc4f415df",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "c0dd116d-0bd2-4537-8260-ec14a2fcfa4b",
  "sourceToolAssistantUUID": "77f89c18-f56a-4601-a45c-cc9dc4f415df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T12:18:59.515Z_

<details><summary>↩ Tool result · `toolu_01Nn5ovmyGT3ct4TxpZoV6wY`</summary>

```text
Web search results for query: "arxiv 2605.20531 pseudo-formalization automatic proof verification"

Links: [{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"The Existence of At Least Three Genomic Signature Patterns and At Least Seven Subtypes of COVID-19 and the End of the Disease","url":"https://www.biorxiv.org/content/10.1101/2022.01.24.477579.full.pdf"},{"title":"Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access","url":"https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf"},{"title":"Using General Large Language Models to Classify Mathematical Documents","url":"https://arxiv.org/pdf/2406.10274"},{"title":"Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025","url":"https://arxiv.org/pdf/2602.05930"},{"title":"Monitoring of COVID-19 Pandemic-related Psychopathology using Machine Learning","url":"https://www.medrxiv.org/content/10.1101/2021.07.13.21259962.full.pdf"}]

The search for "arxiv 2605.20531" didn't return the specific paper you're looking for. Let me try a more direct search using the topic terms you mentioned.

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/html/2604.03789"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/pdf/2604.03789"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"}]

Perfect! I found the paper. Here's what I found about arxiv 2605.20531:

## Pseudo-Formalization for Automatic Proof Verification

The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language.

**Problem Being Addressed:**
Fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, but most proofs, particularly those written by AI systems, have neither property, and translating them into formal languages remains challenging in many frontier math settings.

**How It Works:**
A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language. The proof format is intended to be both unambiguous and modular: modularity comes from decomposing the proof into parts, while unambiguity comes from requiring each node to explicitly state its premises, conclusion, proof, and dependencies.

**Verification Method:**
The paper introduces Pseudo-Formalization + Block-Verification (PF+BV) as an automatic proof verification algorithm, which they evaluate on two benchmarks covering Olympiad and research-level mathematics, where it pareto-dominates strong LLM-as-judge baselines on error-finding precision and recall.

The authors release ArxivMathGradingBench, a new benchmark of 35 mathematics research papers with 40 known errors in total.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71296341-fcb4-4347-bbb0-b1ee02592839",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "4bce294c-1558-4d50-8a2e-414ff5000dce",
  "sourceToolAssistantUUID": "71296341-fcb4-4347-bbb0-b1ee02592839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-27T12:19:02.845Z_

This is extremely relevant. The pseudo-formalization paper (arxiv 2605.20531) is very close to the proposed idea. Let me get more details on it and search for more related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bce294c-1558-4d50-8a2e-414ff5000dce",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4WJKYNdTFoqfYn8hbY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbf657d6-b304-47d8-9c80-84a5dca42bdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bES9NTtGnpm9pDQZpo985",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2286,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 19675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 46 · 2026-05-27T12:19:03.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vig5MFPTLS9uP4ECq3GZia`</summary>

```json
{
  "query": "arxiv 2605.20531 pseudo-formalization authors Lean routing selective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbf657d6-b304-47d8-9c80-84a5dca42bdd",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4WJKYNdTFoqfYn8hbY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e03f677f-ee9e-4c89-8f4c-2d677097e1ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bES9NTtGnpm9pDQZpo985",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2286,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 19675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 47 · 2026-05-27T12:19:04.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LLYYCyFL1p5h6n2nM8nawE`</summary>

```json
{
  "query": "\"confidence routing\" \"formal verification\" \"natural language proof\" LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e03f677f-ee9e-4c89-8f4c-2d677097e1ab",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4WJKYNdTFoqfYn8hbY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "350bbf6e-6d0c-4190-aba1-ad6c1ab05551",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bES9NTtGnpm9pDQZpo985",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2286,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 19675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 48 · 2026-05-27T12:19:04.788Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XFXrGQeyiQQYjmELFihPT2`</summary>

```json
{
  "query": "ProofFlow dependency graph autoformalization selective verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350bbf6e-6d0c-4190-aba1-ad6c1ab05551",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4WJKYNdTFoqfYn8hbY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6c32801-43d2-4f1a-8521-a039ef4c69a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bES9NTtGnpm9pDQZpo985",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2286,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 19675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 49 · 2026-05-27T12:19:05.161Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013LnNBXhgUgrmYCcDVegjNg`</summary>

```json
{
  "query": "\"uncertainty routing\" autoformalization lean formal proof 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c32801-43d2-4f1a-8521-a039ef4c69a2",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4WJKYNdTFoqfYn8hbY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eac0a39e-51f1-4f02-9a9f-5bb8ec109e32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bES9NTtGnpm9pDQZpo985",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2286,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 19675,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2286,
          "output_tokens": 263,
          "cache_read_input_tokens": 19675,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 50 · 2026-05-27T12:19:10.053Z_

<details><summary>↩ Tool result · `toolu_01Vig5MFPTLS9uP4ECq3GZia`</summary>

```text
Web search results for query: "arxiv 2605.20531 pseudo-formalization authors Lean routing selective"

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.05007] Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation","url":"https://arxiv.org/abs/2605.05007"},{"title":"Combining Textual and Structural Information for Premise Selection in Lean","url":"https://arxiv.org/pdf/2510.23637"},{"title":"System and method for determining routing by learned selective optimization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11092448"},{"title":"System and method for determining routing by learned selective optimization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10809080"}]

Based on the search results, I found the paper arxiv 2605.20531. Here are the key details:

**Title:** Pseudo-Formalization for Automatic Proof Verification

**Authors:** Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, Tengyu Ma

**Main Contribution:** The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language.

**Key Details:** A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language. To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm called Block Verification (BV).

The paper addresses the challenge that most proofs, particularly those written by AI systems, have neither the unambiguity nor modularity of formal proofs, and translating them into formal languages remains challenging in many frontier math settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e03f677f-ee9e-4c89-8f4c-2d677097e1ab",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "1f0bdd35-1965-450c-ae60-9775b1c006d4",
  "sourceToolAssistantUUID": "e03f677f-ee9e-4c89-8f4c-2d677097e1ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-27T12:19:10.272Z_

<details><summary>↩ Tool result · `toolu_01XFXrGQeyiQQYjmELFihPT2`</summary>

```text
Web search results for query: "ProofFlow dependency graph autoformalization selective verification"

Links: [{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"},{"title":"(PDF) ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://www.researchgate.net/publication/396716261_ProofFlow_A_Dependency_Graph_Approach_to_Faithful_Proof_Autoformalization"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981v1"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization | OpenReview","url":"https://openreview.net/forum?id=s9t2FJVsBH"},{"title":"[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/abs/2510.15981"}]

Based on the search results, here's what I found about ProofFlow:

ProofFlow is a novel pipeline that treats structural fidelity as a primary objective. It first constructs a directed acyclic graph (DAG) to map the logical dependencies between proof steps, and then employs a novel lemma-based approach to systematically formalize each step as an intermediate lemma, preserving the logical structure of the original argument.

Proof autoformalization is the task of translating natural language theorems and proofs into machine-verifiable code, which is a critical step for integrating large language models into rigorous mathematical workflows. Current approaches focus on producing executable code, but they frequently fail to preserve the semantic meaning and logical structure of the original human-written argument.

The ProofFlow pipeline has three parts: (1) Graph builder; (2) Lemma Formalizer; and (3) Tactic Completer.

In terms of performance, ProofFlow sets a new state-of-the-art for autoformalization, achieving a ProofScore of 0.545, substantially exceeding baselines like full-proof formalization (0.123) and step-proof formalization (0.072). The researchers also introduced ProofScore, a new composite metric to evaluate syntactic correctness, semantic faithfulness, and structural fidelity.

The pipeline, benchmark, and score metric are open-sourced at https://github.com/Huawei-AI4Math/ProofFlow.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6c32801-43d2-4f1a-8521-a039ef4c69a2",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "c6ddf04f-e016-4fbc-aaef-7944b8dd5d3d",
  "sourceToolAssistantUUID": "c6c32801-43d2-4f1a-8521-a039ef4c69a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-27T12:19:13.064Z_

<details><summary>↩ Tool result · `toolu_013LnNBXhgUgrmYCcDVegjNg`</summary>

```text
Web search results for query: ""uncertainty routing" autoformalization lean formal proof 2025 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"}]

I found relevant results about autoformalization and formal proofs in Lean 4 from 2025-2026. Here are the key findings:

## Recent Breakthroughs in Autoformalization

In 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs. Systems producing Lean 4 proofs offer a crucial advantage: no human verification required.

## Notable Systems and Approaches

AlphaProof is an AlphaZero-inspired agent that learns to find formal proofs through reinforcement learning by training on millions of auto-formalized problems, and for the most difficult problems, it uses Test-Time RL, a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation.

Recent autoformalization research includes several approaches:
- ProofBridge presents a unified framework for automatically translating entire natural language theorems and proofs into Lean 4.
- FormL4 is a benchmark to evaluate autoformalization in Lean 4, along with a process-supervised verifier that enhances the accuracy of LLMs in converting informal statements and proofs into formal ones.

## Real-World Impact

Using Gauss, Math Inc. completed a challenge set by Fields Medallist Terence Tao and Alex Kontorovich in January 2024 to formalize the strong Prime Number Theorem in Lean, which had stalled after 18+ months of human expert effort, completed in just three weeks.

However, I did not find specific information about "uncertainty routing" in these results. Would you like me to search more specifically for that term?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eac0a39e-51f1-4f02-9a9f-5bb8ec109e32",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "48eb0ecd-53c6-43ec-be93-c2ef36716d55",
  "sourceToolAssistantUUID": "eac0a39e-51f1-4f02-9a9f-5bb8ec109e32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-27T12:19:16.548Z_

<details><summary>↩ Tool result · `toolu_01LLYYCyFL1p5h6n2nM8nawE`</summary>

```text
Web search results for query: ""confidence routing" "formal verification" "natural language proof" LLM 2025 2026"

Links: [{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads | OpenReview","url":"https://openreview.net/forum?id=svQuvBYaCA"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://arxiv.org/html/2511.06209v2"},{"title":"LLMs and Formal Methods - Unalarming","url":"https://unalarming.com/llms-and-formal-methods"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/pdf/2601.22642"},{"title":"Prediction: AI will make formal verification go mainstream | Lobsters","url":"https://lobste.rs/s/zsgdbg/prediction_ai_will_make_formal"},{"title":"Incorporating and Evaluating LLMs on Natural Language ...","url":"https://aclanthology.org/2025.acl-long.1310.pdf"},{"title":"From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs","url":"https://arxiv.org/pdf/2501.16207"}]

Based on the search results, here's what I found regarding these topics in recent LLM research from 2025-2026:

## Confidence and Verification in LLM Reasoning

Uncertainty quantification heads (UHeads) use the internal states of a frozen LLM to estimate the uncertainty of its reasoning steps during generation. These lightweight step-level verifiers read an LLM's own internal states to detect incorrect reasoning.

## Formal Verification Approaches

A two-stage training pipeline synergizes formal logic verification-guided supervised fine-tuning and policy optimization, with 7B and 14B models outperforming state-of-the-art baselines, validating that formal verification can serve as a scalable mechanism to significantly push the performance boundaries of advanced LLM reasoning.

Formal verification has recently been used to verify LLM reasoning steps, though these methods often require specialized autoformalization data for training and are limited to narrow domains like math proofs.

## Natural Language to Formal Proofs

Most current benchmarks cannot precisely reflect the capability to convert informal proofs or requirements in natural language into formal proofs; therefore research is breaking down the process from informal requirements to formal verifiable proof. Instruction fine-tuning of LLMs uses constructed fine-tuning datasets to improve their capability in formal verification tasks.

## Semantic Routing

VERGE targets open-domain natural language where full formalization is often impossible, introducing semantic routing rather than forcing vague or commonsense claims into rigid first-order logic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "350bbf6e-6d0c-4190-aba1-ad6c1ab05551",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "09a32f40-046b-4c1c-ba60-db8d4e82a421",
  "sourceToolAssistantUUID": "350bbf6e-6d0c-4190-aba1-ad6c1ab05551",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-27T12:19:19.650Z_

Excellent. I found the most critical paper. Let me do a few more targeted searches to ensure completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a32f40-046b-4c1c-ba60-db8d4e82a421",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4XZB2pAuzFxbmaB8ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10302dea-8c53-4eb4-8005-ef172731d6a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128H8yvTrQCbkBPdwAwmQEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 20966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 55 · 2026-05-27T12:19:20.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015G44EK4hfG5xBgQX8dWyMc`</summary>

```json
{
  "query": "Barkallah Bailey Wen Abouzaid Ma pseudo-formalization block verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10302dea-8c53-4eb4-8005-ef172731d6a6",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4XZB2pAuzFxbmaB8ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dae4467-d37c-437e-9f0e-11fc0c218713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128H8yvTrQCbkBPdwAwmQEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 20966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 56 · 2026-05-27T12:19:21.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LDBXc1ghWw3bdT9cHkRgJY`</summary>

```json
{
  "query": "VERGE semantic routing formal verification LLM reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dae4467-d37c-437e-9f0e-11fc0c218713",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4XZB2pAuzFxbmaB8ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26b4e5af-8f3d-40cd-9bd7-1edee75b3d12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128H8yvTrQCbkBPdwAwmQEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 20966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 57 · 2026-05-27T12:19:21.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ni4YpR3t9SpVTQHExw2bvq`</summary>

```json
{
  "query": "\"Reasoning with Confidence\" \"uncertainty heads\" verification LLM reasoning steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b4e5af-8f3d-40cd-9bd7-1edee75b3d12",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4XZB2pAuzFxbmaB8ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2296563-dc0f-4c74-a8f2-9d1a3fedffe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128H8yvTrQCbkBPdwAwmQEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 20966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 58 · 2026-05-27T12:19:22.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UWYReyBbRqG9tmmkVtfgde`</summary>

```json
{
  "query": "hybrid verification formal informal proof routing confidence LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2296563-dc0f-4c74-a8f2-9d1a3fedffe8",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4XZB2pAuzFxbmaB8ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fd199f4-0b93-41a2-a195-a2f9ada66d57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128H8yvTrQCbkBPdwAwmQEV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 20966,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 244,
          "cache_read_input_tokens": 20966,
          "cache_creation_input_tokens": 3887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3887,
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

_source line 59 · 2026-05-27T12:19:26.844Z_

<details><summary>↩ Tool result · `toolu_015G44EK4hfG5xBgQX8dWyMc`</summary>

```text
Web search results for query: "Barkallah Bailey Wen Abouzaid Ma pseudo-formalization block verification 2025"

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Prediction: AI will make formal verification go mainstream — Martin Kleppmann’s blog","url":"https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html"},{"title":"Formal Verification of Blockchain Nonforking in DAG-Based BFT Consensus   with Dynamic Stake","url":"https://arxiv.org/pdf/2504.16853"},{"title":"Improving Auto-Formalization to UCLID5 with LLMs and Formal Methods","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-115.pdf"},{"title":"Formal Verification of Blockchain Byzantine Fault Tolerance","url":"https://arxiv.org/pdf/1909.07453"},{"title":"Holistic Verification of Blockchain Consensus","url":"https://arxiv.org/pdf/2206.04489"},{"title":"Block verification method, apparatus and device","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11983168"}]

Based on the search results, I found the most relevant paper for your query. The "Pseudo-Formalization" paper proposes a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. 

A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language. The paper appears to be focused on automatic proof verification as a means of addressing the challenge of reliably verifying mathematical proofs for training and evaluating AI systems.

The paper is authored by Slim Barkallah and others (as indicated in the search results), and is available on arXiv with the identifier 2605.20531. This appears to be a 2025 publication addressing proof verification in the context of mathematical reasoning with AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dae4467-d37c-437e-9f0e-11fc0c218713",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "4bcefb57-8279-409a-b1f5-3f9a2256ecef",
  "sourceToolAssistantUUID": "7dae4467-d37c-437e-9f0e-11fc0c218713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-27T12:19:29.798Z_

<details><summary>↩ Tool result · `toolu_01Ni4YpR3t9SpVTQHExw2bvq`</summary>

```text
Web search results for query: ""Reasoning with Confidence" "uncertainty heads" verification LLM reasoning steps"

Links: [{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2511.06209"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads | OpenReview","url":"https://openreview.net/forum?id=svQuvBYaCA"},{"title":"Paper page - Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://huggingface.co/papers/2511.06209"},{"title":"(PDF) Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://www.researchgate.net/publication/397480546_Reasoning_with_Confidence_Efficient_Verification_of_LLM_Reasoning_Steps_via_Uncertainty_Heads"},{"title":"Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads","url":"https://arxiv.org/html/2511.06209v2"},{"title":"[Quick Review] Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps\\n via Uncertainty Heads","url":"https://liner.com/review/reasoning-with-confidence-efficient-verification-llm-reasoning-steps-via-uncertainty"}]

I found comprehensive information about "Reasoning with Confidence" and uncertainty heads for LLM reasoning verification. Here's what the research shows:

## Overview

The approach trains transformer-based uncertainty quantification heads (UHeads) that use the internal states of a frozen LLM to estimate the uncertainty of its reasoning steps during generation.

## Motivation and Problem

Solving complex tasks usually requires LLMs to generate long multi-step reasoning chains, and verifying the correctness of individual reasoning steps can improve the performance and efficiency of LLMs on such tasks and enhance solution interpretability. However, existing verification approaches, such as Process Reward Models (PRMs), are either computationally expensive, limited to specific domains, or require large-scale human or model-generated annotations.

## The Solution

The research proposes a lightweight alternative for step-level reasoning verification based on data-driven uncertainty scores, training transformer-based uncertainty quantification heads (UHeads) that use the internal states of a frozen LLM to estimate the uncertainty of its reasoning steps during generation. The approach is fully automatic: target labels are generated either by another larger LLM (e.g., DeepSeek R1) or in a self-supervised manner by the original model itself.

## Performance Results

UHeads contain less than 10M parameters and across multiple domains, including mathematics, planning, and general knowledge question answering, they match or even surpass the performance of PRMs that are up to 810x larger.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2296563-dc0f-4c74-a8f2-9d1a3fedffe8",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "e4f1c93c-3f7e-4674-969c-136e05a5431f",
  "sourceToolAssistantUUID": "f2296563-dc0f-4c74-a8f2-9d1a3fedffe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-27T12:19:30.201Z_

<details><summary>↩ Tool result · `toolu_01LDBXc1ghWw3bdT9cHkRgJY`</summary>

```text
Web search results for query: "VERGE semantic routing formal verification LLM reasoning 2026"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/pdf/2601.20055"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"llm formal method | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/search?highlight=1&query=LLM+formal+method&sort=0"},{"title":"Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification","url":"https://arxiv.org/html/2604.17010"}]

Based on the search results, here's what I found about VERGE:

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

### Key Innovations

The framework features three main innovations:

1. **Multi-model Consensus**: Formal semantic equivalence checking ensures logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics.

2. **Semantic Routing**: This key innovation dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based "soft verifier."

3. **Error Localization**: Minimal Correction Subsets (MCS) pinpoint the precise subset of conflicting claims to revise, enabling the model to iteratively refine its reasoning from "probabilistic" to "provable."

### Performance Results

With the GPT-OSS-120B model, VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches. VERGE exhibits monotonic improvement across iterations, contrasting sharply with probabilistic self-refinement methods that often degrade performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26b4e5af-8f3d-40cd-9bd7-1edee75b3d12",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "b0fc78b3-135b-4db1-94db-23001873cd9f",
  "sourceToolAssistantUUID": "26b4e5af-8f3d-40cd-9bd7-1edee75b3d12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-27T12:19:31.991Z_

<details><summary>↩ Tool result · `toolu_01UWYReyBbRqG9tmmkVtfgde`</summary>

```text
Web search results for query: "hybrid verification formal informal proof routing confidence LLM 2026"

Links: [{"title":"LLMs and Formal Methods - Unalarming","url":"https://unalarming.com/llms-and-formal-methods"},{"title":"Hybrid Cloud-Local LLM: The Complete Architecture Guide (2026)","url":"https://www.sitepoint.com/hybrid-cloudlocal-llm-the-complete-architecture-guide-2026/"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/pdf/2604.06401"},{"title":"HybridProver: Augmenting Theorem Proving with LLM-Driven Proof Synthesis and Refinement","url":"https://arxiv.org/pdf/2505.15740"},{"title":"Recursively Building Formal Proofs with Informal Reasoning","url":"https://arxiv.org/pdf/2509.22819"},{"title":"From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs","url":"https://arxiv.org/pdf/2501.16207"},{"title":"VeriPlan: Integrating Formal Verification and LLMs into End-User   Planning","url":"https://arxiv.org/pdf/2502.17898"}]

Based on the search results, I found several relevant research papers and articles on hybrid verification approaches combining formal and informal reasoning with LLMs. Here's what the search revealed:

## Key Findings

**Hybrid Verification Frameworks:**

Recent work bridges the gap between formal and informal mathematics by combining the verifiability of formal reasoning with the flexibility of LLM-based informal reasoning. HERMES is a multi-modular tool-augmented agent designed to integrate formal verification into the LLM reasoning process.

ProofSketcher is a hybrid design where the LLM writes a typed proof sketch rather than a full formal proof. The sketch is a structured plan with explicit step types (rewrite, case split, induction, contradiction) and typed holes. A lightweight kernel expands each sketch node into concrete proof obligations.

**Combining Multiple Approaches:**

HybridProver is an LLM-driven automated theorem-proving framework. Two predominant approaches had emerged: whole-proof synthesis and tactic-based generation. Whole-proof synthesis excels at high-level planning but is error-prone at details; tactic-based generation excels at details but may struggle with higher-level planning. HybridProver is the first system to combine these two approaches, achieving state-of-the-art results.

**Informal-to-Formal Bridge:**

Agentic frameworks including COPRA, Prover-Agent, and ProofCompass iteratively construct proofs using informal reasoning with feedback from the formal verifier. HILBERT is an agentic framework that bridges informal reasoning with formal verification.

**Confidence and Routing:**

In 2026, engineering teams running production AI workloads face routing every request to cloud APIs versus local models. A hybrid LLM architecture addresses both problems by placing an intelligent routing layer between the application and inference providers, implementing a three-pillar routing layer (sensitivity → complexity → availability).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fd199f4-0b93-41a2-a195-a2f9ada66d57",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "9a9097b1-91f7-4941-9a81-0259bf8b6e22",
  "sourceToolAssistantUUID": "6fd199f4-0b93-41a2-a195-a2f9ada66d57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-27T12:19:34.849Z_

Let me do a final round of searches to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a9097b1-91f7-4941-9a81-0259bf8b6e22",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4YhEjtg2xrzuM2tVWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f642d236-2bf5-4ff2-889c-d140c00d7e9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01521SVY7YkxxbXJysT25a7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4715,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4715,
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

_source line 64 · 2026-05-27T12:19:35.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WB1ErPRCLiSxh3nUgshoaz`</summary>

```json
{
  "query": "ProofSketcher hybrid LLM lightweight proof checker reliable math logic reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f642d236-2bf5-4ff2-889c-d140c00d7e9f",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4YhEjtg2xrzuM2tVWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a239a86-a095-4179-8d15-981fbe9fb17d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01521SVY7YkxxbXJysT25a7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4715,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4715,
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

_source line 65 · 2026-05-27T12:19:36.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzSvcGqZg2DLD5gpo5X7by`</summary>

```json
{
  "query": "HERMES efficient verifiable mathematical reasoning LLM formal verification integration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a239a86-a095-4179-8d15-981fbe9fb17d",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4YhEjtg2xrzuM2tVWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a3b372-fd73-4efd-bd46-ee376706b960",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01521SVY7YkxxbXJysT25a7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4715,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4715,
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

_source line 66 · 2026-05-27T12:19:37.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSh9E3upHfdoua7yXr6Hkp`</summary>

```json
{
  "query": "\"modular proof verification\" \"natural language\" \"formal verification\" selective routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3a3b372-fd73-4efd-bd46-ee376706b960",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4YhEjtg2xrzuM2tVWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c79eeece-496e-4f7a-9e51-6c56b02018f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01521SVY7YkxxbXJysT25a7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4715,
      "cache_read_input_tokens": 24853,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 24853,
          "cache_creation_input_tokens": 4715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4715,
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

_source line 67 · 2026-05-27T12:19:42.645Z_

<details><summary>↩ Tool result · `toolu_01WB1ErPRCLiSxh3nUgshoaz`</summary>

```text
Web search results for query: "ProofSketcher hybrid LLM lightweight proof checker reliable math logic reasoning 2026"

Links: [{"title":"ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/html/2604.06401v1"},{"title":"ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/pdf/2604.06401"},{"title":"[2604.06401] ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/abs/2604.06401"},{"title":"ProofSketch : Efficient Verified Reasoning for Large Language Models","url":"https://arxiv.org/html/2510.24811v1"},{"title":"Natural-Formal Hybrid Reasoning Enhances LLM's Math ...","url":"https://aclanthology.org/2025.emnlp-main.850.pdf"}]

Based on the search results, here's what I found about ProofSketcher:

ProofSketcher is a hybrid LLM + lightweight proof-checking approach for reliable math and logic reasoning. The system works by having the LLM produce a typed proof sketch with explicit step tags and typed holes, while a trusted kernel expands the sketch into proof obligations and accepts a theorem only when all obligations are discharged by kernel rules or by externally produced proof certificates that a trusted checker validates.

The system returns localized failure feedback and supports fast repair through node-level caching and targeted sketch edits. More broadly, the main outcome is a practical bridge between informal LLM reasoning and formal reliability: proofs are accepted only by checking, while the LLM remains useful for proposing structure and guiding search.

This approach addresses a key problem: LLMs often make a small invalid step, miss a side condition, or use a lemma that does not follow from the context. By combining LLM capabilities with formal proof verification, ProofSketcher aims to achieve reliable mathematical and logical reasoning.

The research paper was published recently (April 7, 2026) and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a239a86-a095-4179-8d15-981fbe9fb17d",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "b32e2b94-9000-4a5f-87b9-c6b3d52f1975",
  "sourceToolAssistantUUID": "3a239a86-a095-4179-8d15-981fbe9fb17d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-27T12:19:46.095Z_

<details><summary>↩ Tool result · `toolu_01XzSvcGqZg2DLD5gpo5X7by`</summary>

```text
Web search results for query: "HERMES efficient verifiable mathematical reasoning LLM formal verification integration"

Links: [{"title":"[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760"},{"title":"[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760v1"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"ICML Poster HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://icml.cc/virtual/2026/poster/60844"},{"title":"(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"}]

Based on the search results, here's what I found about HERMES:

## Overview

HERMES is abbreviated from "Hybrid AgEnt for Reasoning in Mathematics with NEuro-Symbolic Lean4 verification," designed to integrate formal verification into the LLM reasoning process.

## Key Innovation

HERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. This addresses a fundamental challenge: informal mathematics offers flexibility and efficient argument construction but is prone to logical gaps and subtle errors, while formal theorem proving provides rigorous, verifiable mathematical reasoning where each inference step is checked by a trusted compiler, but lacks the exploratory freedom of informal problem solving.

## How It Works

HERMES comprises four modules: an LLM that generates reasoning steps, a translator that formalizes these steps into Lean code, a prover that symbolically verifies their correctness, and a feedback module that returns verification signals for subsequent reasoning. The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains.

## Performance Results

HERMES reliably improves the reasoning accuracy of base models while substantially reducing token usage and computational cost compared to reward-based approaches. Notably, on difficult datasets such as AIME'25, HERMES achieves up to a 67% accuracy improvement while using 80% fewer total inference FLOPs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3a3b372-fd73-4efd-bd46-ee376706b960",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "ffe25bed-050a-422d-a856-ee0d4393dcb9",
  "sourceToolAssistantUUID": "f3a3b372-fd73-4efd-bd46-ee376706b960",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-27T12:19:46.110Z_

<details><summary>↩ Tool result · `toolu_01KSh9E3upHfdoua7yXr6Hkp`</summary>

```text
Web search results for query: ""modular proof verification" "natural language" "formal verification" selective routing 2025 2026"

Links: [{"title":"Leveraging LLMs for Formal Software Requirements: Challenges and Prospects","url":"https://ceur-ws.org/Vol-4142/paper11.pdf"},{"title":"Protocols to Code: Formal Verification of a Next-Generation Internet Router","url":"https://arxiv.org/html/2405.06074v1"},{"title":"stepproof: step-by-step verification of","url":"https://arxiv.org/pdf/2506.10558"},{"title":"Dissect-and-Restore: AI-based Code Verification with Transient Refactoring","url":"https://arxiv.org/pdf/2510.25406"},{"title":"Trustworthy Formal Natural Language Specifications","url":"https://arxiv.org/pdf/2310.03885"},{"title":"From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs","url":"https://arxiv.org/pdf/2501.16207"},{"title":"Natural Hoare Logic: Towards formal verification of programs from   logical forms of natural language specifications","url":"https://arxiv.org/pdf/2103.05779"}]

I found several relevant research papers on modular proof verification, natural language, and formal verification. Here are the key findings:

## Recent Work on Modular Proof Verification with Natural Language

StepProof proposes an automatic formalization strategy that can realize sentence-level verification for natural language mathematical proofs, representing an advancement in how proof verification can be broken down into more manageable components.

Prometheus is an AI-assisted system that facilitates automated code verification using modular software engineering principles, beginning by decomposing complex program logic into smaller, verifiable components, then recomposing them to construct a proof of the original program. When automated tools are insufficient, users can provide lightweight natural language guidance to steer the proof process.

## Natural Language Integration with Formal Verification

Researchers have implemented a means to provide specifications in a modularly extensible formal subset of English, automatically translated into formal claims within the Lean proof assistant, while being extensible and modular.

Other work uses natural language requirements and domain ontologies as input, with different prompt strategies shaping how inputs are presented for specification generation, storing outputs in a tool-neutral intermediate format that can be translated into verification tool syntax.

## LLM-Based Formal Verification (2025-2026)

Recent research constructed 18k high-quality instruction-response pairs across five formal specification languages (Coq, Lean4, Dafny, ACSL, and TLA+) in six formal verification-related tasks by distilling gpt-4o.

The search results don't contain specific information about "selective routing" in formal verification, so I was unable to find results directly matching that particular aspect of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c79eeece-496e-4f7a-9e51-6c56b02018f3",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "aefc7761e04a79fe8",
  "type": "user",
  "uuid": "3eaf501c-cd43-4863-92f1-fffd5400dd36",
  "sourceToolAssistantUUID": "c79eeece-496e-4f7a-9e51-6c56b02018f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-27T12:21:17.623Z_

I now have comprehensive results. Here is the full report.

---

## Novelty Search Report: "Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition"

### CRITICAL FINDING: Highly Similar Prior Work Exists

---

### Search 1: "selective formal verification uncertainty 2026"

**Key results:**
- **"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks"** -- NeurIPS 2025. Introduces a PCFG framework for uncertainty quantification in LLM-generated formal artifacts, enabling **selective verification** that reduces errors 14-100% with minimal abstention. Uses uncertainty signals (grammar entropy, AUROC > 0.93) to decide when to trust LLM outputs. **HIGHLY RELEVANT** -- addresses the "uncertainty-guided selective verification" component directly.
- ICML 2026 Workshop on "Statistical Frameworks for Uncertainty in Agentic Systems"
- TransferLab article on "Formal Verification under Uncertainty"

**Similarity:** The "Grammars of Formal Uncertainty" paper is **moderately-to-highly similar** in its use of uncertainty signals to enable selective verification of LLM-generated formal artifacts.

---

### Search 2: "pseudo-formal autoformalization 2026"

**Key results:**
- **"Pseudo-Formalization for Automatic Proof Verification" (arXiv:2605.20531, May 2026)** -- Authors: **Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, Tengyu Ma**. This paper is **EXTREMELY SIMILAR** to the proposed idea. It proposes:
  - **Pseudo-Formal (PF) proof format**: decomposes proofs into self-contained modular blocks, each with explicit premises, conclusions, and proof in natural language
  - **Block Verification (BV)**: an LLM verifies each module independently
  - Evaluated on Olympiad and research-level math benchmarks
  - Pareto-dominates LLM-as-judge baselines
  - Releases ArxivMathGradingBench (35 research papers, 40 known errors)

- **"130k Lines of Formal Topology in Two Weeks" (arXiv:2601.03298, Jan 2026)** -- Demonstrates cheap, large-scale autoformalization using LLM + proof checker feedback loops.

- **"Towards a Common Framework for Autoformalization" (AAAI 2025)** -- Proposes unified framework for autoformalization across research fields.

**Similarity:** The Barkallah et al. paper is **EXTREMELY SIMILAR** -- it implements the core "pseudo-formal decomposition" concept with modular NL proof blocks having explicit premises/conclusions. The key difference is that their paper does NOT include the uncertainty-guided routing to formal verification (Lean 4); instead, all blocks are verified by LLM-based Block Verification only.

---

### Search 3: "adaptive verification mathematical proof 2026"

**Key results:**
- **ADAPT (Adaptive Proof Refinement with LLM-Guided Strategy Selection)** -- Uses an LLM decision-maker to dynamically select refinement strategies for incorrect proofs. Proves 16-18% more theorems than baselines.
- **MiniF2F-Dafny (POPL 2026)** -- First translation of miniF2F to Dafny; auto-verifies 40-44% of test sets.
- **StepProof** -- Step-by-step autoformalisation for sentence-level verification of NL proofs.

**Similarity:** ADAPT is tangentially related (adaptive strategy selection, not uncertainty-guided routing). StepProof is moderately relevant (step-level NL proof verification via autoformalization).

---

### Search 4: "uncertainty guided proof verification"

**Key results:**
- **"Uncertainty-Aware Step-wise Verification with Generative Reward Models" (arXiv:2502.11250, Feb 2025)** -- Introduces CoT Entropy to quantify process reward model uncertainty in step-wise verification. Improves robustness of LLM-based judge models. **RELEVANT** -- uses uncertainty to improve proof step verification reliability.
- **"A Protocol for Trustless Verification Under Uncertainty" (arXiv:2507.00631)**

**Similarity:** The CoT Entropy paper is **moderately similar** -- it uses uncertainty quantification for step-level verification, but does not involve routing to formal provers.

---

### Search 5: "selective autoformalization natural language proof 2026"

**Key results:**
- **FormalEvolve (arXiv:2603.19828, March 2026)** -- Neuro-symbolic evolutionary search for autoformalization of NL math to compilable formal statements.
- **AI for Math Workshop at ICML 2026** -- Challenge track for generating Lean 4 proofs from NL informal proofs (May-June 2026).
- **ProofBridge (arXiv:2510.15681)** -- Unified framework for translating entire NL theorems and proofs into Lean 4 via joint embeddings.
- **Autoformalization robustness evaluations (arXiv:2511.12784)** -- Evaluating LLM robustness in autoformalization via paraphrasing.

**Similarity:** These are relevant as components (autoformalization pipelines) but none implement selective/uncertainty-guided routing between LLM verification and formal verification.

---

### Search 6: arXiv "autoformalization selective verification 2026"

**Key results:**
- **"Faithful Autoformalization via Roundtrip Verification and Repair" (arXiv:2604.25031, April 2026)** -- Roundtrip verification: formalize, back-translate, re-formalize, check logical equivalence. Raises formal equivalence from 45-61% to 83-85%. **RELEVANT** -- addresses verification quality in autoformalization but not selective routing.
- **MerLean (arXiv:2602.16554, Feb 2026)** -- Agentic autoformalization for quantum computation; reduces verification burden to only new definitions/axioms.

**Similarity:** MerLean's idea of "reducing the verification burden" to a subset is conceptually related to selective verification, though the mechanism is different.

---

### Search 7: arXiv "proof verification uncertainty routing 2026"

**Key results:**
- **UCCI (arXiv:2605.18796, May 2026)** -- Calibrated uncertainty for cost-optimal LLM cascade routing. Uses isotonic regression to map uncertainty to error probability, then selects escalation threshold via cost minimization. **RELEVANT** -- the general framework of uncertainty-based routing between verification tiers is conceptually very close to the proposed idea, though applied to LLM cascades rather than proof verification.
- **CP-Router (arXiv:2505.19970)** -- Routes prompts between LLM and LRM based on complexity.

**Similarity:** UCCI provides a direct methodological precedent for uncertainty-based routing between verification approaches.

---

### Search 8: OpenReview "selective formal verification"

**Key results:**
- **FVEL** -- Interactive formal verification environment with LLMs via theorem proving.
- **AlphaVerus** -- Self-improving framework for formally verified code generation.
- **VeriBench** -- Lean 4 benchmark for LLM-powered agents translating Python to proved implementations.

**Similarity:** These are infrastructure/benchmark papers, not directly competing with the proposed idea.

---

### Search 9: OpenReview "pseudo-formal verification"

**Key results:**
- **StepProof (OpenReview:EXaKfdsw04)** -- Step-by-step verification of NL mathematical proofs via autoformalization. Breaks proofs into subproofs for sentence-level verification.
- **Re:Form** -- Reducing human priors in scalable formal software verification with RL in LLMs.

**Similarity:** StepProof is **moderately similar** in its decomposition approach, but uses full formalization for each step rather than selective routing.

---

### Search 10: "Barkallah pseudo-formalization 2026"

**Key results:**
- Confirmed: **Slim Barkallah** is the first author of the "Pseudo-Formalization for Automatic Proof Verification" paper (arXiv:2605.20531). A different Barkallah (Manel) presented at FMTea 2026 on formal methods teaching -- unrelated.

**Similarity:** The Slim Barkallah paper is the **most critical competing work** found.

---

### Search 11: "Safe Liu ACL 2025 formal verification lean"

**Key results:**
- **Safe (ACL 2025 Main)** -- Authors: Chengwu Liu, Ye Yuan, Yichun Yin, et al. Retrospective step-aware formal verification: articulates mathematical claims in Lean 4 at each reasoning step and provides formal proofs. First work to use Lean 4 for verifying LLM-generated content. Proposes FormalStep benchmark (30,809 formal statements). **RELEVANT** -- demonstrates step-level formal verification of LLM reasoning, but applies it uniformly rather than selectively.

**Similarity:** Safe is **moderately similar** -- it formalizes each step into Lean 4 for verification but does not do selective routing based on uncertainty.

---

### Search 12: "Mu adaptive verification allocation 2026"

**Key results:** No relevant academic results. The search returned Mumbai University admission results.

**Similarity:** No competing work found under this query.

---

### Search 13: "Bhatt uncertainty guided selective verification 2025"

**Key results:**
- Redirected to "Grammars of Formal Uncertainty" (already covered in Search 1). No specific paper by "Bhatt" found.
- **"Uncertainty-Guided Selective Adaptation" (arXiv:2511.12006)** -- About fluorescence microscopy, not proof verification.

**Similarity:** No specific "Bhatt" paper on this topic found.

---

### Additional Highly Relevant Papers Found in Follow-up Searches

- **VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv:2601.20055, Jan 2026)** -- Decomposes LLM outputs into atomic claims, autoformalizes to FOL, verifies via SMT solvers. Features **"Semantic Routing"**: dynamically classifies atomic claims -- verifiable logic goes to SMT solvers (Z3), ambiguous claims go to a consensus-based "soft verifier." **HIGHLY RELEVANT** -- implements a form of routing between formal and informal verification, though for general reasoning rather than mathematical proofs specifically.

- **HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv:2511.18760, ICML 2026 poster)** -- First tool-assisted agent that **explicitly interleaves informal reasoning with formally verified proof steps in Lean**. Comprises LLM + translator + Lean prover + feedback module. 67% accuracy improvement on AIME'25 with 80% fewer FLOPs. **HIGHLY RELEVANT** -- bridges informal and formal verification within the same pipeline.

- **ProofSketcher: Hybrid LLM + Lightweight Proof Checker (arXiv:2604.06401, April 2026)** -- LLM produces typed proof sketch with explicit step tags and typed holes; a trusted kernel expands sketches into proof obligations. Returns localized failure feedback. **MODERATELY RELEVANT** -- hybrid verification approach but without uncertainty-guided routing.

- **Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv:2511.06209)** -- Trains lightweight UHeads (<10M params) on frozen LLM internal states to estimate uncertainty of reasoning steps. Matches/surpasses PRMs 810x larger. **RELEVANT** -- provides the uncertainty estimation component that could be used for routing.

- **ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv:2510.15981)** -- Constructs DAG of logical dependencies between proof steps, formalizes each as intermediate lemma. New SOTA for autoformalization (ProofScore 0.545 vs 0.123 baseline). **MODERATELY RELEVANT** -- modular/structured autoformalization.

---

### Summary Assessment

| Aspect of Proposed Idea | Prior Work Coverage | Key Papers |
|---|---|---|
| Pseudo-formal decomposition (modular NL blocks with premises/conclusions) | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |
| Block-level LLM verification of decomposed proof modules | **DIRECTLY COVERED** | Barkallah et al. 2605.20531 |
| Uncertainty-guided routing/selection | **COVERED in adjacent domains** | Grammars of Formal Uncertainty (NeurIPS'25), UCCI, Reasoning with Confidence |
| Routing uncertain blocks to formal verification (Lean 4) | **PARTIALLY COVERED** | VERGE (semantic routing), HERMES (interleaved formal/informal) |
| Combined system: pseudo-formal decomposition + uncertainty routing to Lean 4 | **NOT DIRECTLY COVERED as a single system** | -- |

### Verdict

The **most critical competing paper** is **Barkallah et al. "Pseudo-Formalization for Automatic Proof Verification" (arXiv:2605.20531, May 2026)**, which implements the core pseudo-formal decomposition with modular NL proof blocks having explicit premises/conclusions, verified by LLM-based Block Verification. This paper was posted very recently (May 2026) and directly overlaps with the "pseudo-formal decomposition" component of the proposed idea.

The specific **novelty gap** that the proposed idea could still claim is the **uncertainty-guided selective routing to formal verification (Lean 4)**. Barkallah et al. verify all blocks with LLMs only; the proposed idea would route uncertain blocks to Lean 4 while keeping confident blocks with LLM verification. However, the individual components (uncertainty estimation for verification, routing between formal/informal, and the pseudo-formal decomposition itself) all have strong prior art. The integration of these specific components into a single pipeline is where novelty would need to be argued.

Additionally, **VERGE** (Jan 2026) already implements a form of semantic routing between formal (SMT) and informal (consensus) verification, and **HERMES** (ICML 2026) interleaves informal reasoning with Lean 4 formal verification steps.

---

### Sources

- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al.)](https://arxiv.org/abs/2605.20531)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)
- [Reasoning with Confidence: Uncertainty Heads](https://arxiv.org/abs/2511.06209)
- [UCCI: Calibrated Uncertainty for LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [ProofSketcher: Hybrid LLM + Lightweight Proof Checker](https://arxiv.org/abs/2604.06401)
- [StepProof: Step-by-step Verification](https://arxiv.org/abs/2506.10558)
- [ProofFlow: Dependency Graph Autoformalization](https://arxiv.org/abs/2510.15981)
- [ProofBridge: Auto-Formalization in Lean via Joint Embeddings](https://arxiv.org/abs/2510.15681)
- [FormalEvolve: Neuro-Symbolic Evolutionary Autoformalization](https://arxiv.org/abs/2603.19828)
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)
- [130k Lines of Formal Topology](https://arxiv.org/abs/2601.03298)
- [Uncertainty-Aware Step-wise Verification (CoT Entropy)](https://arxiv.org/abs/2502.11250)
- [ADAPT: Adaptive Proof Refinement](https://arxiv.org/abs/2510.25103)
- [ICML 2026 Workshop: Statistical Frameworks for Uncertainty in Agentic Systems](https://agentic-uncertainty-icml2026.github.io/)
- [AI for Math Workshop at ICML 2026](https://ai4math2026.github.io/)
- [OpenReview: Grammars of Formal Uncertainty](https://openreview.net/forum?id=QfKpJ00t2L)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eaf501c-cd43-4863-92f1-fffd5400dd36",
  "isSidechain": true,
  "agentId": "aefc7761e04a79fe8",
  "requestId": "req_011CbT4ZjYBRDfnHuM7XANbj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c241201f-b212-4912-ad73-6fc14a194cda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gXKnfZuYcyDxMX6JBvHAH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2215,
      "cache_read_input_tokens": 29568,
      "output_tokens": 4191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2215
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4191,
          "cache_read_input_tokens": 29568,
          "cache_creation_input_tokens": 2215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2215,
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
