# Research conversation: I need to research the paper "Learning to Disprove: Formal Counterexample Generation with Large Language Models" (arXiv 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac834b3e9f20d97fe.jsonl`
- **Structured JSON:** [`42b9b7dcddef7a8f2c89.json`](../../sessions/42/42b9b7dcddef7a8f2c89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-27T20:24:03.476Z_

I need to research the paper "Learning to Disprove: Formal Counterexample Generation with Large Language Models" (arXiv 2603.19514, March 2026). 

Please:
1. Search the web for "Learning to Disprove formal counterexample generation LLM arXiv 2603.19514"
2. Fetch the arXiv abstract page at https://arxiv.org/abs/2603.19514
3. Search for any related discussions

I need: the full title, authors, key methodology (symbolic mutation strategy, how they train LLMs to generate formal counterexamples in Lean 4), their results, scale of counterexample generation, and how this relates to using formal counterexamples as training signals for verification. Report in detail (300-500 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "29c76615-7d41-4d68-b702-379e38d29890",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T20:24:03.478Z_

```json
{
  "parentUuid": "29c76615-7d41-4d68-b702-379e38d29890",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
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
  "uuid": "e1887649-28df-4de1-9c41-0ca12c828476",
  "timestamp": "2026-05-27T20:24:03.478Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T20:24:03.479Z_

```json
{
  "parentUuid": "e1887649-28df-4de1-9c41-0ca12c828476",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "841b3e89-9a8a-4e3d-a44d-2cfdc3401caf",
  "timestamp": "2026-05-27T20:24:03.479Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T20:24:05.854Z_



I'll research this paper by searching the web and fetching the arXiv page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "841b3e89-9a8a-4e3d-a44d-2cfdc3401caf",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVgGgP6Dt4WMyLLnUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "214131ba-0368-4ba5-b11e-8c2344fb544f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW1jjBfgtSFqPabiYmFF9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1532,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1532,
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

_source line 5 · 2026-05-27T20:24:06.463Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HafCk813nad1oU7dxQCqmC`</summary>

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
  "parentUuid": "214131ba-0368-4ba5-b11e-8c2344fb544f",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVgGgP6Dt4WMyLLnUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0941118-7c79-4e22-b49f-f70e3d0d9c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW1jjBfgtSFqPabiYmFF9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1532,
      "cache_read_input_tokens": 7411,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1532,
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

_source line 6 · 2026-05-27T20:24:06.469Z_

<details><summary>↩ Tool result · `toolu_01HafCk813nad1oU7dxQCqmC`</summary>

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
  "parentUuid": "b0941118-7c79-4e22-b49f-f70e3d0d9c39",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "0c3d05d2-77b1-497b-9dda-08eebdc266a4",
  "sourceToolAssistantUUID": "b0941118-7c79-4e22-b49f-f70e3d0d9c39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T20:24:09.584Z_



Now let me run all three research tasks in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c3d05d2-77b1-497b-9dda-08eebdc266a4",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVuMykHbevEyi3EWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f405ba6e-1f44-4df2-9e4e-6eb505ad9f6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mc61X4CH9zwhH8nTRtSaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 8 · 2026-05-27T20:24:10.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qri46af7DNEMhKD3WDC8w9`</summary>

```json
{
  "query": "Learning to Disprove formal counterexample generation LLM arXiv 2603.19514"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f405ba6e-1f44-4df2-9e4e-6eb505ad9f6d",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVuMykHbevEyi3EWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd47d084-94d1-401e-8469-3f0ce6be361a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mc61X4CH9zwhH8nTRtSaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 9 · 2026-05-27T20:24:10.996Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dvp5jHVr1HJf7jUKjczWXx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19514",
  "prompt": "Extract the full title, all authors, the complete abstract, and any metadata (submission date, subjects, comments) from this arXiv paper page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd47d084-94d1-401e-8469-3f0ce6be361a",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVuMykHbevEyi3EWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "605f8034-3d71-4802-9191-90dae5c817e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mc61X4CH9zwhH8nTRtSaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
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

_source line 10 · 2026-05-27T20:24:11.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B21d6g6VqWXK6DCmxAFLzb`</summary>

```json
{
  "query": "\"Learning to Disprove\" formal counterexample Lean 4 LLM 2026 discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "605f8034-3d71-4802-9191-90dae5c817e7",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThVuMykHbevEyi3EWpc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b5dc188-2a12-4a00-a77b-8cd2813239d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Mc61X4CH9zwhH8nTRtSaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 8943,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 8943,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1123,
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

_source line 11 · 2026-05-27T20:24:14.851Z_

<details><summary>↩ Tool result · `toolu_01Dvp5jHVr1HJf7jUKjczWXx`</summary>

```text
# Paper Extraction Summary

**Full Title:** Learning to Disprove: Formal Counterexample Generation with Large Language Models

**Authors:**
- Zenan Li
- Zhaoyu Li
- Kaiyu Yang
- Xiaoxing Ma
- Zhendong Su

**Abstract:**
The paper addresses a gap in AI mathematics research by focusing on counterexample discovery alongside proof construction. The authors fine-tuned LLMs to "reason about and generate counterexamples" with formal verification in Lean 4. They introduced a symbolic mutation strategy to synthesize diverse training data and developed a multi-reward expert iteration framework. Experiments on three newly collected benchmarks demonstrated significant performance improvements.

**Metadata:**
- **Submission Date:** March 19, 2026
- **arXiv Identifier:** 2603.19514
- **Subject Classification:** Artificial Intelligence (cs.AI)
- **DOI:** https://doi.org/10.48550/arXiv.2603.19514
- **License:** Creative Commons Attribution 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605f8034-3d71-4802-9191-90dae5c817e7",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "f73e4a10-0367-4bfb-bb35-0b2149251fb6",
  "sourceToolAssistantUUID": "605f8034-3d71-4802-9191-90dae5c817e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T20:24:16.181Z_

<details><summary>↩ Tool result · `toolu_01Qri46af7DNEMhKD3WDC8w9`</summary>

```text
Web search results for query: "Learning to Disprove formal counterexample generation LLM arXiv 2603.19514"

Links: [{"title":"[2603.19514] Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/abs/2603.19514"},{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/html/2603.19514v1"},{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EBa52sye9K"},{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/pdf/2603.19514"},{"title":"ExVerus: Verus Proof Repair via Counterexample Reasoning","url":"https://arxiv.org/pdf/2603.25810"}]

I found the paper you're searching for. Here's what I can tell you about it:

The paper "Learning to Disprove: Formal Counterexample Generation with Large Language Models" addresses the gap in AI efforts by fine-tuning large language models (LLMs) to reason about and generate counterexamples.

The task is formalized as formal counterexample generation, which requires LLMs not only to propose candidate counterexamples but also to produce formal proofs that can be automatically verified in the Lean 4 theorem prover.

To enable effective learning, the authors introduce a symbolic mutation strategy that synthesizes diverse training data by systematically extracting theorems and discarding selected hypotheses, thereby producing diverse counterexample instances.

The paper was submitted on March 19, 2026, and was authored by Zenan Li, Zhaoyu Li, Kaiyu Yang, Xiaoxing Ma, and Zhendong Su from ETH Zurich, University of Toronto, MiroMind, and Nanjing University.

You can access the paper directly at https://arxiv.org/abs/2603.19514.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd47d084-94d1-401e-8469-3f0ce6be361a",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "6416c3b8-3a59-45cd-a50d-64c15d39597d",
  "sourceToolAssistantUUID": "bd47d084-94d1-401e-8469-3f0ce6be361a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T20:24:21.121Z_

<details><summary>↩ Tool result · `toolu_01B21d6g6VqWXK6DCmxAFLzb`</summary>

```text
Web search results for query: ""Learning to Disprove" formal counterexample Lean 4 LLM 2026 discussion"

Links: [{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=EBa52sye9K"},{"title":"[2603.19514] Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/abs/2603.19514"},{"title":"Lean Workbook: A large-scale Lean problem set formalized from natural language math problems | Request PDF","url":"https://www.researchgate.net/publication/397197806_Lean_Workbook_A_large-scale_Lean_problem_set_formalized_from_natural_language_math_problems"},{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/html/2603.19514v1"},{"title":"Learning to Disprove: Formal Counterexample Generation with Large Language Models","url":"https://arxiv.org/pdf/2603.19514"},{"title":"LEARNING TO DISPROVE: FORMAL COUNTEREXAM","url":"https://openreview.net/pdf?id=EBa52sye9K"}]

Based on the search results, here's what I found about "Learning to Disprove":

## Overview

Mathematical reasoning demands two critical, complementary skills: constructing rigorous proofs for true statements and discovering counterexamples that disprove false ones. However, current AI efforts in mathematics focus almost exclusively on proof construction, often neglecting the equally important task of finding counterexamples.

## The Research Paper

The paper addresses this gap by fine-tuning large language models (LLMs) to reason about and generate counterexamples, formalizing this task as formal counterexample generation, which requires LLMs not only to propose candidate counterexamples but also to produce formal proofs that can be automatically verified in the Lean 4 theorem prover.

## Key Innovation

To enable effective learning, the researchers introduce a symbolic mutation strategy that synthesizes diverse training data by systematically extracting theorems and discarding selected hypotheses, thereby producing diverse counterexample instances.

## Status and Discussion

The paper was submitted to ICLR 2026 Conference in September 2025 (modified November 2025). The work has generated recent discussion in the academic community, with references appearing on OpenReview and arXiv (dated March 19, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b5dc188-2a12-4a00-a77b-8cd2813239d2",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "6705d842-36ce-42e8-adb5-f34e71ffc676",
  "sourceToolAssistantUUID": "7b5dc188-2a12-4a00-a77b-8cd2813239d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T20:24:23.805Z_

Let me fetch the full HTML version and the OpenReview page for more detailed methodology and results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6705d842-36ce-42e8-adb5-f34e71ffc676",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThWygi8kdzWHvFUMHPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d03bad0e-8ada-41c8-afa5-a9df2d648850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8GFa6NZrtwA3QJ9SZa4SD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 10066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1728,
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

_source line 15 · 2026-05-27T20:24:25.628Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UYfeS29bV1Bb5ZHWwg9Qg2`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.19514v1",
  "prompt": "Extract detailed information about: (1) the symbolic mutation strategy - how it works step by step, (2) the multi-reward expert iteration framework, (3) the three benchmarks they collected, (4) quantitative results and performance numbers, (5) scale of counterexample generation (how many examples, training data size), (6) how counterexamples serve as training signals for verification. Include all numbers, percentages, and specific details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03bad0e-8ada-41c8-afa5-a9df2d648850",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThWygi8kdzWHvFUMHPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "039ebb5f-32cd-42f5-abe1-171d7cb4f886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8GFa6NZrtwA3QJ9SZa4SD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 10066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1728,
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

_source line 16 · 2026-05-27T20:24:26.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015snXNt9PkijQV7G3MXhWMy`</summary>

```json
{
  "url": "https://openreview.net/forum?id=EBa52sye9K",
  "prompt": "Extract all discussion, reviewer comments, key criticisms, strengths noted by reviewers, and any author responses about the paper 'Learning to Disprove'. Include any scores or ratings if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "039ebb5f-32cd-42f5-abe1-171d7cb4f886",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThWygi8kdzWHvFUMHPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c45214d-266b-46e0-a2db-e60afd141428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8GFa6NZrtwA3QJ9SZa4SD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 10066,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 10066,
          "cache_creation_input_tokens": 1728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1728,
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

_source line 17 · 2026-05-27T20:24:29.388Z_

<details><summary>↩ Tool result · `toolu_015snXNt9PkijQV7G3MXhWMy`</summary>

```text
# Summary

Based on the provided web page content, I cannot extract discussion, reviewer comments, key criticisms, strengths, or author responses about the paper "Learning to Disprove: Formal Counterexample Generation with Large Language Models."

The webpage only displays the paper's title, author information, submission date (19 Sept 2025, modified 21 Nov 2025), status as a "Withdrawn Submission," and the abstract. The page indicates that "Revisions" are available, but no actual review content, comments, or scores are visible in the material provided.

To access peer review information, one would need to view the actual revision history or comments section on the OpenReview platform, which are not included in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c45214d-266b-46e0-a2db-e60afd141428",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "d007d42a-e9ca-47d7-a5d7-73482846a1ad",
  "sourceToolAssistantUUID": "7c45214d-266b-46e0-a2db-e60afd141428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T20:24:41.395Z_

<details><summary>↩ Tool result · `toolu_01UYfeS29bV1Bb5ZHWwg9Qg2`</summary>

```text
# Learning to Disprove: Key Technical Details

## (1) Symbolic Mutation Strategy

The mutation process operates in three steps:

**Starting Point:** Takes a formally provable theorem with universal quantification, e.g., `theorem original_version (x : X) : H₁ x → H₂ x → C x`

**Mutation Operation:** "Discards one of the hypotheses (for example, H₁(x)), resulting in H₂(x)→C(x). If H₁(x) is indeed essential to the original theorem, the mutated version will be invalid, indicating the existence of a counterexample."

**Verification:** Uses the Lean 4 prover to analyze original proof traces and identify necessary hypotheses before elimination, ensuring mutation validity.

**Output:** Generates two derived theorems:
- Mutated version: `∃ x : X, H₂ x → C x`
- Dropped hypothesis: `∃ x : X, ¬ H₁ x`

## (2) Multi-Reward Expert Iteration Framework

The framework employs two separate language models and combines verification signals:

**Architecture:** Qwen3 8B generates counterexample candidates; DeepSeek-Prover-V2 7B produces formal proofs.

**Dual Rewards:** For each generated counterexample x*, the system computes two independent verification signals:
- Reward 1 (weight α): whether x* proves `¬H₁ x*` (dropped hypothesis)
- Reward 2 (weight 1-α): whether x* proves `H₂ x* → C x*` (mutated version)

**Rationale:** "Since the necessary condition can be satisfied directly and its proof is straightforward to construct, the first reward is considerably easier to activate."

**Combined Score:** `r_i := α·I(π_i^M) + (1-α)·I(π_i^H)` where α=0.8 in experiments, serving as sample weights for supervised fine-tuning.

## (3) Three Benchmarks Collected

**For-Counter:** 1,058 formal counterexample problems formalized from CounterMath using Kimina-Autoformalizer 7B.

**Veri-Formalize:** 3,000 unprovable problems from formalizing FormalMath dataset.

**Veri-Reason:** 3,000 problems generated from DSP+ proof attempts on FormalMath that failed or contained errors.

## (4) Quantitative Results & Performance

**Pass@k metrics on three tasks:**

For-Counter benchmark:
- Pass@1: 222 problems solved (74% improvement over strongest baseline of 127)
- Pass@4: 274 problems (37% gain)
- Pass@9: 302 problems (34% gain)

Veri-Reason:
- Pass@1: 213 (47% improvement from 144 baseline)
- Pass@4: 260 (23% gain)
- Pass@9: 295 (26% gain)

Veri-Formalize:
- Pass@1: 174 (56% improvement from 111 baseline)
- Pass@4: 255 (28% gain)
- Pass@9: 313 (25% gain)

**Validation set performance:**
- Single-reward baseline: 43%/46%/47% pass@1/4/9
- Multi-reward approach: 49%/52%/54% pass@1/4/9

## (5) Scale of Counterexample Generation

**Mutation results across four sources:**
- Mathlib: 43,990 seed theorems → 88,217 mutated problems
- Leanworkbook: 17,061 seeds → 42,480 problems
- MiniF2F: 48,415 seeds → 94,215 problems
- PutnamBench: 212,463 seeds → 350,127 problems

**Total:** 321,929 seed theorems produced 575,039 counterexample instances

**Efficiency:** Mutation ratio ranged 1.65-2.48 problems per seed; execution time averaged 0.3-0.71 seconds per theorem.

**Training data:** 575K synthesized problems with 3K reserved for validation; single epoch training used 56 iterations processing 10K examples each.

## (6) Counterexamples as Training Signals

The system creates a verification feedback loop:

**Generation Phase:** Model proposes concrete counterexample instances and constructs formal proofs validating the mutated and dropped-hypothesis theorems.

**Verification Phase:** Lean 4 theorem prover checks both proofs within 60-second timeout and 8GB memory limit.

**Signal Generation:** Verification results produce dual reward signals indicating whether each counterexample successfully satisfies either or both target properties.

**Training Application:** "The correct ones are then used to further refine the model through supervised fine-tuning" with computed rewards as sample weights, enabling learning even when models fail on harder problems through the easier dropped-hypothesis proof path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "039ebb5f-32cd-42f5-abe1-171d7cb4f886",
  "isSidechain": true,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "agentId": "ac834b3e9f20d97fe",
  "type": "user",
  "uuid": "b5aaf0be-23c6-4b76-8362-b063769488b8",
  "sourceToolAssistantUUID": "039ebb5f-32cd-42f5-abe1-171d7cb4f886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T20:25:03.084Z_

Here is the detailed report on the paper.

---

**Title:** Learning to Disprove: Formal Counterexample Generation with Large Language Models

**Authors:** Zenan Li, Zhaoyu Li, Kaiyu Yang, Xiaoxing Ma, and Zhendong Su (ETH Zurich, University of Toronto, MiroMind, Nanjing University)

**arXiv ID:** 2603.19514 (submitted March 19, 2026)

**Core Motivation and Problem.** Current AI-for-mathematics research overwhelmingly targets proof construction -- proving true statements. This paper addresses the neglected complementary skill: discovering counterexamples to disprove false statements. The authors formalize the task as *formal counterexample generation*, requiring an LLM not only to propose a concrete counterexample but also to produce a machine-checkable proof in the Lean 4 theorem prover that the counterexample indeed invalidates the claim.

**Symbolic Mutation Strategy.** The key data-synthesis innovation is a three-step symbolic mutation pipeline. Starting from a formally proved theorem of the form `forall x, H1(x) -> H2(x) -> C(x)`, the method (1) analyzes the original proof trace to identify which hypotheses are necessary, (2) discards one essential hypothesis (e.g., H1), producing a mutated -- now false -- statement `H2(x) -> C(x)`, and (3) verifies via Lean 4 that the mutation is indeed invalid. This yields two companion tasks: find an x* satisfying the remaining hypothesis path, and show that x* violates the dropped hypothesis. Applied to four theorem sources (Mathlib, Lean Workbook, MiniF2F, PutnamBench), the strategy produced **575,039 counterexample instances from 321,929 seed theorems**, at an average rate of 0.3--0.7 seconds per theorem.

**Multi-Reward Expert Iteration.** Training uses a dual-model architecture: Qwen3-8B generates counterexample candidates while DeepSeek-Prover-V2-7B constructs the formal proofs. A combined reward score `r = alpha * I(dropped-hypothesis proof) + (1-alpha) * I(mutated-statement proof)` (with alpha = 0.8) weights training examples for supervised fine-tuning. The easier dropped-hypothesis reward activates more frequently, providing a learning signal even when the model cannot yet solve the harder full disproof, creating a curriculum-like effect. Training ran for 56 iterations of 10K examples each over one epoch.

**Benchmarks and Results.** The authors introduce three new benchmarks: *For-Counter* (1,058 problems formalized from CounterMath), *Veri-Formalize* (3,000 unprovable formalization problems), and *Veri-Reason* (3,000 problems from failed proof attempts). On For-Counter at Pass@1, the system solves 222 problems -- a **74% improvement** over the strongest baseline (127). Gains on Veri-Reason and Veri-Formalize are 47% and 56% respectively at Pass@1. The multi-reward approach also outperforms single-reward ablations (49% vs. 43% Pass@1 on validation).

**Connection to Verification Training Signals.** The formal counterexamples close a feedback loop: Lean 4 verification of both the mutated-statement and dropped-hypothesis proofs generates dual reward signals that directly refine the model via weighted SFT. This means counterexamples are not just end products but serve as verifiable training signals -- correct counterexamples with machine-checked proofs become high-weight training data, enabling the model to progressively tackle harder disproof tasks. This paradigm demonstrates that formal refutation can complement formal proof as a scalable, automatically verified supervision source for mathematical reasoning.

**Note:** The paper was initially submitted to ICLR 2026 (September 2025) and later withdrawn; the arXiv version (March 2026) appears to be a revised posting.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2603.19514)
- [arXiv HTML Full Paper](https://arxiv.org/html/2603.19514v1)
- [OpenReview Submission](https://openreview.net/forum?id=EBa52sye9K)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5aaf0be-23c6-4b76-8362-b063769488b8",
  "isSidechain": true,
  "agentId": "ac834b3e9f20d97fe",
  "requestId": "req_011CbThYULfC83ed6Vuhve9P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6962775d-2ac6-4f1c-8979-05c78404120c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqrqvAWyYKqvbeePHMUz2K",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 1535,
      "cache_read_input_tokens": 11794,
      "output_tokens": 1036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1535
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 190,
          "output_tokens": 1036,
          "cache_read_input_tokens": 11794,
          "cache_creation_input_tokens": 1535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1535,
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
