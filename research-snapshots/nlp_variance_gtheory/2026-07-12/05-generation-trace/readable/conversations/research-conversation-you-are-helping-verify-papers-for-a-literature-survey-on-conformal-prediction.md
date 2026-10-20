# Research conversation: You are helping verify papers for a literature survey on conformal prediction for RAG under adversarial poisoning. I nee

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6c6bffecb9fbd54d.jsonl`
- **Structured JSON:** [`1bdef44d21f269b5f9e3.json`](../../sessions/1b/1bdef44d21f269b5f9e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-30T06:20:26.086Z_

You are helping verify papers for a literature survey on conformal prediction for RAG under adversarial poisoning. I need you to fetch the arXiv pages for these specific papers and extract their exact title, authors, venue, and abstract summary. Also search for papers citing them.

Papers to verify:
1. https://arxiv.org/abs/2410.09878 - "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" (RPS, ICLR 2025 Spotlight)
2. https://arxiv.org/abs/2405.15556 - "RobustRAG: Certifiably Robust RAG against Retrieval Corruption"
3. https://arxiv.org/abs/2603.16817 - "Is Conformal Factuality for RAG-based LLMs Robust?"
4. https://arxiv.org/abs/2509.23519 - "ReliabilityRAG"

Also search for:
5. "conformal prediction exchangeability beyond 2024 2025" to find papers on CP without exchangeability
6. "partition vote aggregation conformal prediction robust" to find papers using partition-and-vote style methods
7. "Gao et al RobustRAG SaTML 2026" or "certifiably robust RAG SaTML 2026" to find the exact venue info

For each paper, provide: title, authors, venue, URL, and one-line summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "b5c83f17-81c2-462e-9d2b-d7e26dec768f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:20:26.089Z_

```json
{
  "parentUuid": "b5c83f17-81c2-462e-9d2b-d7e26dec768f",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
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
  "uuid": "50d9f2cf-0bda-4048-b55b-a25a4e3ab2df",
  "timestamp": "2026-05-30T06:20:26.089Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:20:26.090Z_

```json
{
  "parentUuid": "50d9f2cf-0bda-4048-b55b-a25a4e3ab2df",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1bf6dbc4-02f9-49c6-97f2-cc8259461223",
  "timestamp": "2026-05-30T06:20:26.090Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:20:29.325Z_



I'll fetch the arXiv pages and run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf6dbc4-02f9-49c6-97f2-cc8259461223",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbCTsnTXoLkisX5w4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adaa9958-4d20-4bfe-b783-7ad242d5fe84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpA8aL5GRiBXZKXgviDukQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1689,
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

_source line 5 · 2026-05-30T06:20:29.988Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XhngEdkYbhJUvNVPk8jfmS`</summary>

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
  "parentUuid": "adaa9958-4d20-4bfe-b783-7ad242d5fe84",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbCTsnTXoLkisX5w4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9a43cbd-0863-4381-9ca7-366bae23fa1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpA8aL5GRiBXZKXgviDukQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1689,
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

_source line 6 · 2026-05-30T06:20:29.997Z_

<details><summary>↩ Tool result · `toolu_01XhngEdkYbhJUvNVPk8jfmS`</summary>

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
  "parentUuid": "f9a43cbd-0863-4381-9ca7-366bae23fa1c",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "2a51e635-b866-446f-8457-886ff1b838b0",
  "sourceToolAssistantUUID": "f9a43cbd-0863-4381-9ca7-366bae23fa1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:20:35.511Z_



Now I'll fetch all four arXiv pages and run the three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a51e635-b866-446f-8457-886ff1b838b0",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82658c8b-6a9e-4fab-9770-ede0d72568a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 8 · 2026-05-30T06:20:37.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R7SWACCmwmr2YFz1MeHrUk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.09878",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82658c8b-6a9e-4fab-9770-ede0d72568a7",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc18ced-1130-401a-8b11-f08b4a29bad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 9 · 2026-05-30T06:20:38.078Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ReuwV43giMZbg596hVqp2k`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.15556",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cc18ced-1130-401a-8b11-f08b4a29bad6",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cafa76d6-8bf0-42e0-bfce-3215231f187a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 10 · 2026-05-30T06:20:38.916Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019zBkwB5jXDy9zFke3fMmxo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16817",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cafa76d6-8bf0-42e0-bfce-3215231f187a",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adc7ddc2-1e4a-4e57-84b9-fcfce8ca54ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 11 · 2026-05-30T06:20:39.840Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K49VGrKdBZG88pbJSzDjrg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23519",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adc7ddc2-1e4a-4e57-84b9-fcfce8ca54ad",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "579f7a2b-6fcf-4f57-bb77-a2d963d35b05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 12 · 2026-05-30T06:20:40.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LdqpoPX8iuXu97ZeqQNUoW`</summary>

```json
{
  "query": "conformal prediction exchangeability beyond 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "579f7a2b-6fcf-4f57-bb77-a2d963d35b05",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10dbf46a-6ec9-4fc0-8864-f0aa5a46f9b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 13 · 2026-05-30T06:20:40.326Z_

<details><summary>↩ Tool result · `toolu_01R7SWACCmwmr2YFz1MeHrUk`</summary>

```text
# Paper Summary

**Title:** "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning"

**Authors:** Yan Scholten, Stephan Günnemann

**Submission Date:** October 13, 2024 (v1); last revised March 16, 2025 (v4)

**Venue:** ICLR 2025 (Spotlight)

**Abstract Summary:** The authors propose reliable prediction sets (RPS), a new approach for constructing conformal prediction sets that remain effective even when training and calibration data contain poisoned samples. The method uses smoothed score functions to aggregate predictions across data partitions and constructs multiple calibrated sets that are combined through majority voting. This approach maintains coverage guarantees on clean data while demonstrating improved robustness against poisoning attacks in image classification tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc18ced-1130-401a-8b11-f08b4a29bad6",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "bf7ce463-b5b1-4486-9c9f-c4a9cbd49c8d",
  "sourceToolAssistantUUID": "6cc18ced-1130-401a-8b11-f08b4a29bad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-30T06:20:40.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EL9irdWAjtdeTo4ey6GeHy`</summary>

```json
{
  "query": "partition vote aggregation conformal prediction robust arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf7ce463-b5b1-4486-9c9f-c4a9cbd49c8d",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e65390f5-828b-4366-930a-d58619efc9a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 15 · 2026-05-30T06:20:41.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMvkNewW7zcC49UPtGixPD`</summary>

```json
{
  "query": "Gao et al RobustRAG SaTML 2026 certifiably robust RAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e65390f5-828b-4366-930a-d58619efc9a6",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGbj1A3NSFh1Tu8aZep",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8bebaa5-77f4-4ae4-a250-6912fef2f670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZCXi9xRisY8LmNDhtdV1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9102,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 552,
          "cache_read_input_tokens": 9102,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1118,
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

_source line 16 · 2026-05-30T06:20:42.369Z_

<details><summary>↩ Tool result · `toolu_01ReuwV43giMZbg596hVqp2k`</summary>

```text
# Paper Extraction

**Title:** "Certifiably Robust RAG against Retrieval Corruption"

**Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal

**Submission Date:** May 24, 2024 (v1); last revised April 1, 2026 (v2)

**Abstract:** The paper addresses vulnerabilities in retrieval-augmented generation systems where malicious passages can compromise outputs. The proposed RobustRAG framework employs an "isolate-then-aggregate strategy" that partitions passages into separate groups, generates responses from each group independently, then securely combines results. The authors developed keyword-based and decoding-based aggregation methods for text responses. The framework provides formal guarantees against adaptive attackers injecting bounded malicious content, evaluated on question-answering and text generation tasks across three datasets and language models.

**Venue/Conference Information:** No specific venue or conference is mentioned on this page. The paper is categorized under Computer Science > Machine Learning (cs.LG) with cross-listings in Computation and Language (cs.CL) and Cryptography and Security (cs.CR).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cafa76d6-8bf0-42e0-bfce-3215231f187a",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "beafcc35-105f-4b68-aaf6-6af1b8f07252",
  "sourceToolAssistantUUID": "cafa76d6-8bf0-42e0-bfce-3215231f187a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:20:44.044Z_

<details><summary>↩ Tool result · `toolu_019zBkwB5jXDy9zFke3fMmxo`</summary>

```text
# Paper Information Summary

**Exact Title:**
"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

**All Authors:**
- Yi Chen
- Daiwei Chen
- Sukrut Madhav Chikodikar
- Caitlyn Heqi Yin
- Ramya Korlakai Vinayak

**Submission Date:**
Submitted on 17 March 2026

**Abstract:**
The paper examines how well conformal factuality works for RAG-based language models. The authors note that while RAG grounds responses in retrieved evidence, it doesn't guarantee output correctness, and conformal filtering offers statistical reliability but may produce uninformative outputs. Their analysis across multiple benchmarks reveals three key findings: conformal filtering struggles with usefulness at high factuality levels, the statistical guarantee lacks robustness against distribution shifts, and lightweight verifiers match LLM-based scorers while requiring significantly fewer computations. They propose novel metrics and call for new approaches balancing reliability with robustness.

**Venue/Conference Information:**
No specific conference or venue is mentioned on this arXiv page. The submission is classified under Computer Science categories: Artificial Intelligence (cs.AI), Computation and Language (cs.CL), and Machine Learning (cs.LG).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adc7ddc2-1e4a-4e57-84b9-fcfce8ca54ad",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "9dba54ae-a391-45c0-9074-36bdb9dc6ff7",
  "sourceToolAssistantUUID": "adc7ddc2-1e4a-4e57-84b9-fcfce8ca54ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T06:20:46.550Z_

<details><summary>↩ Tool result · `toolu_01VMvkNewW7zcC49UPtGixPD`</summary>

```text
Web search results for query: "Gao et al RobustRAG SaTML 2026 certifiably robust RAG"

Links: [{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | OpenReview","url":"https://openreview.net/forum?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"ICML Certifiably Robust RAG against Retrieval Corruption","url":"https://icml.cc/virtual/2024/37487"}]

Based on the search results, I found information about RobustRAG:

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.

To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses. RobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, non-trivial lower bounds on response quality can be formally certified—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.

The work was evaluated on the tasks of open-domain question-answering and free-form long text generation across three datasets and three LLMs. The paper was accepted to the IEEE SaTML 2026 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8bebaa5-77f4-4ae4-a250-6912fef2f670",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "a4cfd3e0-e5c2-4741-a356-e9fed26cb33b",
  "sourceToolAssistantUUID": "f8bebaa5-77f4-4ae4-a250-6912fef2f670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:20:47.019Z_

<details><summary>↩ Tool result · `toolu_01EL9irdWAjtdeTo4ey6GeHy`</summary>

```text
Web search results for query: "partition vote aggregation conformal prediction robust arxiv"

Links: [{"title":"[2601.02998] Multi-Distribution Robust Conformal Prediction","url":"https://arxiv.org/abs/2601.02998"},{"title":"Multi-Distribution Robust Conformal Prediction","url":"https://arxiv.org/pdf/2601.02998"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"One Sample is Enough to Make Conformal Prediction Robust","url":"https://arxiv.org/pdf/2506.16553"},{"title":"arXiv:2506.20173v1 [stat.ML] 25 Jun 2025 Valid Selection among Conformal Sets","url":"https://arxiv.org/pdf/2506.20173"}]

Based on the web search results, here are the key findings related to partition, vote aggregation, conformal prediction, and robustness on arXiv:

## Multi-Distribution Robust Conformal Prediction

The paper studies constructing conformal prediction sets that are uniformly valid across multiple heterogeneous distributions, and proposes a max-p aggregation scheme that delivers finite-sample, multi-distribution coverage given any conformity scores associated with each distribution. The authors prove the optimality and tightness of their aggregation scheme, and propose a general algorithm to learn conformity scores that lead to efficient prediction sets after the aggregation under standard conditions.

Their method delivers valid worst-case coverage across multiple distributions while greatly reducing the set size compared with naively applying max-p aggregation to single-source conformity scores.

## Robust Conformal Prediction Methods

Recent work also addresses robustness in conformal prediction through other approaches. Robust CP extends coverage guarantees to worst-case (adversarial) inputs by bounding randomly smoothed conformity scores. Additionally, one approach combines prediction sets from multiple algorithms through a voting mechanism, where weights are dynamically adjusted over time based on past performance.

The search results highlight the development of aggregation schemes and voting-based methods for robust conformal prediction across multiple distributions and models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e65390f5-828b-4366-930a-d58619efc9a6",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "aec575ba-1db1-4a33-82ab-61afffaceaaf",
  "sourceToolAssistantUUID": "e65390f5-828b-4366-930a-d58619efc9a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:20:47.761Z_

<details><summary>↩ Tool result · `toolu_01LdqpoPX8iuXu97ZeqQNUoW`</summary>

```text
Web search results for query: "conformal prediction exchangeability beyond 2024 2025 arxiv"

Links: [{"title":"Conformal prediction beyond exchangeability","url":"https://www.researchgate.net/publication/371558117_Conformal_prediction_beyond_exchangeability"},{"title":"[2202.13415] Conformal prediction beyond exchangeability","url":"https://arxiv.org/abs/2202.13415"},{"title":"Distribution-informed Online Conformal Prediction","url":"https://arxiv.org/pdf/2512.07770"},{"title":"Conformal prediction beyond exchangeability","url":"https://arxiv.org/pdf/2202.13415"},{"title":"Conformal Prediction Beyond Exchangeability","url":"https://arxiv.org/html/2202.13415v5"},{"title":"A Gentle Introduction to Conformal Time Series Forecasting","url":"https://arxiv.org/html/2511.13608v1"},{"title":"Extreme Conformal Prediction: Reliable Intervals for High-Impact Events","url":"https://arxiv.org/html/2505.08578v3"},{"title":"Online Conformal Prediction: Enforcing monotonicity via Online Optimization","url":"https://arxiv.org/html/2605.12668"}]

Here are the search results for "conformal prediction exchangeability beyond 2024 2025 arxiv":

## Key Recent Papers

**2022-2023 Foundational Work:**
The seminal paper "Conformal prediction beyond exchangeability" by Barber, Candès, Ramdas, and Tibshirani (arxiv 2202.13415) provides valid predictive inference for arbitrary machine learning models, though its validity relies on exchangeability of the data and symmetry of the model fitting algorithm.

**2024-2025 Developments:**

Recent studies (2024-2025) further examine conformal selection, calibration, and robustness in deep models. Several extensions have adapted the method to dependent or non-exchangeable data, including time series, online learning, and other structured settings with recent publications in 2024-2025.

Despite the success of conformal prediction for exchangeable data, it remains challenging to directly perform it in scenarios involving distribution shifts and temporal dependence that violate the exchangeability assumption.

**2025 Surveys:**
A recent review (arxiv 2511.13608, November 2025) titled "A Gentle Introduction to Conformal Time Series Forecasting" synthesizes modern approaches to conformal prediction mainly in the context of time-series data, collectively called Conformal Forecasting.

These results show active research in extending conformal prediction methods beyond the exchangeability assumption, particularly for time series and online learning applications in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10dbf46a-6ec9-4fc0-8864-f0aa5a46f9b4",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "afe74075-69e6-4cc5-a767-5e186bd7f028",
  "sourceToolAssistantUUID": "10dbf46a-6ec9-4fc0-8864-f0aa5a46f9b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:20:47.962Z_

<details><summary>↩ Tool result · `toolu_01K49VGrKdBZG88pbJSzDjrg`</summary>

```text
# ReliabilityRAG Paper Details

**Title:** "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search"

**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova

**Submission Date:** September 27, 2025 (v1); February 15, 2026 (v2)

**Venue:** Accepted to NeurIPS 2025

**Abstract Summary:**
The paper addresses vulnerabilities in Retrieval-Augmented Generation (RAG) systems to attacks on retrieval corpora, such as prompt injection. ReliabilityRAG proposes a defense framework leveraging document reliability signals. The approach uses graph-theoretic methods to identify a "consistent majority" among retrieved documents, introducing a Maximum Independent Set algorithm that prioritizes higher-reliability documents while offering provable robustness guarantees. A scalable variant using weighted sampling and aggregation handles large document sets efficiently. Empirical results demonstrate improved robustness against adversarial attacks while maintaining accuracy in long-form generation tasks where previous robustness methods struggled.

**arXiv Identifier:** 2509.23519 [cs.CR]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "579f7a2b-6fcf-4f57-bb77-a2d963d35b05",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "1e2138f5-4c0d-4ba1-a607-c3acfc3fd867",
  "sourceToolAssistantUUID": "579f7a2b-6fcf-4f57-bb77-a2d963d35b05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-30T06:20:50.369Z_

Now let me fetch more details on the key papers found in the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2138f5-4c0d-4ba1-a607-c3acfc3fd867",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGcp6XUbBGhXNm9KFgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23a357f0-052b-469e-92b6-9c88a8b1b364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8PTwqxSL5xavfDdnLEpt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
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

_source line 23 · 2026-05-30T06:20:52.253Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WNpXb8L8PhbhEkdwKY6XB1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2202.13415",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a357f0-052b-469e-92b6-9c88a8b1b364",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGcp6XUbBGhXNm9KFgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb359097-0c87-4f91-bbbf-eb75c314e410",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8PTwqxSL5xavfDdnLEpt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
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

_source line 24 · 2026-05-30T06:20:52.738Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EjDm1W8U18Lez6pyBs43Ee`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.02998",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb359097-0c87-4f91-bbbf-eb75c314e410",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGcp6XUbBGhXNm9KFgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f93b5cc1-b216-45bd-b60f-3ccf95b48a73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8PTwqxSL5xavfDdnLEpt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
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

_source line 25 · 2026-05-30T06:20:55.852Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012jZ49hRXoPKTSEDJxgwAf8`</summary>

```json
{
  "url": "https://satml.org/accepted-papers/",
  "prompt": "Look for the paper \"Certifiably Robust RAG against Retrieval Corruption\" or \"RobustRAG\" in the accepted papers list. Extract the exact title, authors, and any other details listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f93b5cc1-b216-45bd-b60f-3ccf95b48a73",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGcp6XUbBGhXNm9KFgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afafe27c-027b-46f8-90f5-ae1bfa0d8cdb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8PTwqxSL5xavfDdnLEpt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
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

_source line 26 · 2026-05-30T06:20:55.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLkYPs4Y2XggPQUjzyAGJK`</summary>

```json
{
  "query": "\"conformal prediction\" \"data poisoning\" robust partition aggregation voting 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afafe27c-027b-46f8-90f5-ae1bfa0d8cdb",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGcp6XUbBGhXNm9KFgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1a8960a-2bd0-4165-94b0-a17c566514fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8PTwqxSL5xavfDdnLEpt3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 1812,
      "cache_read_input_tokens": 10220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1812,
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

_source line 27 · 2026-05-30T06:20:57.388Z_

<details><summary>↩ Tool result · `toolu_01EjDm1W8U18Lez6pyBs43Ee`</summary>

```text
# Paper Extraction Summary

**Title:** "Multi-Distribution Robust Conformal Prediction"

**Authors:** Yuqi Yang, Ying Jin

**Submission Date:** January 6, 2026

**Abstract:** The researchers address constructing prediction sets valid across multiple source distributions. They introduce a max-p aggregation method ensuring finite-sample coverage regardless of which distribution a test point originates from. Key contributions include proving optimality of their aggregation scheme and proposing an algorithm for learning efficient conformity scores. The work connects to distributionally robust optimization, fairness, and multi-source learning, with experiments demonstrating valid worst-case coverage across distributions while reducing set sizes compared to naive approaches.

**Subject Classifications:** Machine Learning (cs.LG); Methodology (stat.ME); Machine Learning (stat.ML)

**Venue/Conference Information:** None explicitly mentioned on this page. This is an arXiv preprint (arXiv:2601.02998v1).

**License:** Creative Commons Attribution 4.0 (CC BY 4.0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f93b5cc1-b216-45bd-b60f-3ccf95b48a73",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "6fe3e885-e5fb-477a-9157-97314b0ba443",
  "sourceToolAssistantUUID": "f93b5cc1-b216-45bd-b60f-3ccf95b48a73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-30T06:20:59.397Z_

<details><summary>↩ Tool result · `toolu_01WNpXb8L8PhbhEkdwKY6XB1`</summary>

```text
# Paper Summary

**Title:** "Conformal prediction beyond exchangeability"

**Authors:** Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani

**Submission Date:** February 27, 2022 (with final revision March 17, 2023)

**Abstract:** The paper addresses a key limitation of conformal prediction methods by extending them beyond the exchangeability assumption. The researchers introduce "weighted quantiles to introduce robustness against distribution drift" and develop a new randomization approach for asymmetric algorithms. Their approach maintains coverage guarantees under exchangeability while showing "substantially less loss of coverage when exchangeability is violated due to distribution drift." The methods are validated using electricity and election forecasting applications.

**Venue/Subject Area:** Statistics - Methodology (stat.ME)

**Identifier:** arXiv:2202.13415
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb359097-0c87-4f91-bbbf-eb75c314e410",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "516b26fc-165d-4257-9044-e2b3884bf83a",
  "sourceToolAssistantUUID": "cb359097-0c87-4f91-bbbf-eb75c314e410",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T06:21:00.598Z_

<details><summary>↩ Tool result · `toolu_012jZ49hRXoPKTSEDJxgwAf8`</summary>

```text
# RobustRAG Paper Details

**Exact Title:** "Certifiably Robust RAG against Retrieval Corruption"

**Authors:** Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University)

**Key Information:**
- **Category:** Research Papers
- **Program Slot:** Group 1 (/program/#slot-2026-03-23-1700-2000)
- **Abstract Available:** Yes

**Summary:** The paper addresses vulnerabilities in retrieval-augmented generation systems where malicious passages inserted into search results can compromise model outputs. The authors propose RobustRAG, introducing an "isolate-then-aggregate strategy" that partitions passages into separate groups, generates responses for each, then securely combines them. The framework provides formal robustness guarantees and is tested on question-answering and text generation tasks across multiple datasets and language models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afafe27c-027b-46f8-90f5-ae1bfa0d8cdb",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "577e12c8-4cb0-44ce-b530-3ac108ccfdfd",
  "sourceToolAssistantUUID": "afafe27c-027b-46f8-90f5-ae1bfa0d8cdb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T06:21:08.904Z_

<details><summary>↩ Tool result · `toolu_01XLkYPs4Y2XggPQUjzyAGJK`</summary>

```text
Web search results for query: ""conformal prediction" "data poisoning" robust partition aggregation voting 2024 2025 arxiv"

Links: [{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Run-Off Election: Improved Provable Defense against Data Poisoning   Attacks","url":"https://arxiv.org/pdf/2302.02300"},{"title":"Lethal Dose Conjecture on Data Poisoning","url":"https://arxiv.org/pdf/2208.03309"},{"title":"provably reliable conformal prediction sets","url":"https://yascho.github.io/assets/pdf/scholten2025provably.pdf"},{"title":"[2406.05405] Robust Conformal Prediction Using Privileged Information","url":"https://arxiv.org/abs/2406.05405"},{"title":"Improved Certified Defenses against Data Poisoning with (Deterministic)   Finite Aggregation","url":"https://arxiv.org/pdf/2202.02628"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"}]

Based on the search results, I found relevant research on conformal prediction under data poisoning. Here are the key findings:

## Main Result: Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

The most directly relevant paper proposes reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. This paper was submitted in October 2024 with the latest version from March 2025.

## Key Technical Approach

The method uses two complementary aggregation strategies:

1. **For training poisoning:** The approach introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data.

2. **For calibration poisoning:** Multiple prediction sets are constructed, each calibrated on distinct subsets of the calibration data, then aggregated into a majority prediction set, which includes a class only if it appears in a majority of the individual sets.

## Results and Validation

The approach was experimentally validated on image classification tasks, achieving strong reliability while maintaining utility and preserving coverage on clean data.

## Related Work on Partition Aggregation

Your query also touches on related work using partition aggregation and voting for robustness. Deep Partition Aggregation (DPA) and its extension, Finite Aggregation (FA) are recent approaches for provable defenses against data poisoning, where they predict through the majority vote of many base models trained from different subsets of training set.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1a8960a-2bd0-4165-94b0-a17c566514fe",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "4192d278-f349-445b-93a0-40a89ba6b4c4",
  "sourceToolAssistantUUID": "d1a8960a-2bd0-4165-94b0-a17c566514fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-30T06:21:11.953Z_

Now let me check a couple more things: search for citations of the key papers and verify the arXiv ID validity for papers 3 and 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4192d278-f349-445b-93a0-40a89ba6b4c4",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGeMXuoMyAjGmeBs6WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c57230d8-5801-4474-8cf6-b1b4aaeae4d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjesYatf6ZHLjTUBHSBFn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3797,
      "cache_read_input_tokens": 12032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3797,
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

_source line 32 · 2026-05-30T06:21:12.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Hxs2XmUGfpPMAjWQJgEP9`</summary>

```json
{
  "query": "arxiv 2603.16817 \"Is Conformal Factuality for RAG-based LLMs Robust\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57230d8-5801-4474-8cf6-b1b4aaeae4d4",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGeMXuoMyAjGmeBs6WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df0e798d-17c3-436b-86b8-5a0e7458e11f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjesYatf6ZHLjTUBHSBFn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3797,
      "cache_read_input_tokens": 12032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3797,
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

_source line 33 · 2026-05-30T06:21:13.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LqrdXJDJZYsaUwrn3sffoU`</summary>

```json
{
  "query": "arxiv 2509.23519 ReliabilityRAG \"Effective and Provably Robust Defense\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df0e798d-17c3-436b-86b8-5a0e7458e11f",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGeMXuoMyAjGmeBs6WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3df1b1ff-c833-4dac-8757-820b6300dbdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjesYatf6ZHLjTUBHSBFn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3797,
      "cache_read_input_tokens": 12032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3797,
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

_source line 34 · 2026-05-30T06:21:14.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014nEqxmiKNcNHmb4vNqG6ei`</summary>

```json
{
  "query": "citing \"Provably Reliable Conformal Prediction Sets\" Scholten Gunnemann 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3df1b1ff-c833-4dac-8757-820b6300dbdc",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGeMXuoMyAjGmeBs6WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14f910df-1057-4f37-9193-c3437bd2c0aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjesYatf6ZHLjTUBHSBFn2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3797,
      "cache_read_input_tokens": 12032,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 12032,
          "cache_creation_input_tokens": 3797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3797,
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

_source line 35 · 2026-05-30T06:21:19.361Z_

<details><summary>↩ Tool result · `toolu_014nEqxmiKNcNHmb4vNqG6ei`</summary>

```text
Web search results for query: "citing "Provably Reliable Conformal Prediction Sets" Scholten Gunnemann 2025"

Links: [{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/html/2511.18562"},{"title":"provably reliable conformal prediction sets","url":"https://yascho.github.io/assets/pdf/scholten2025provably.pdf"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS","url":"https://openreview.net/pdf?id=ofuLWn8DFZ"}]

Based on the search results, I found information about this paper:

"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" by Scholten and Günnemann was published in the 13th International Conference on Learning Representations (ICLR 2025). The paper was accepted as a Spotlight presentation.

**Overview:**
The paper addresses conformal prediction, which provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with user-specified probability, but notes that conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data.

**Main Contribution:**
The authors propose reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. To ensure reliability under training poisoning, they introduce smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data, and to ensure reliability under calibration poisoning, they construct multiple prediction sets, each calibrated on distinct subsets of the calibration data.

An implementation of the method is available on GitHub, and the paper details and additional materials can be found on the OpenReview platform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14f910df-1057-4f37-9193-c3437bd2c0aa",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "19aa5f4a-eded-47c4-8695-ba00bf97361f",
  "sourceToolAssistantUUID": "14f910df-1057-4f37-9193-c3437bd2c0aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T06:21:25.432Z_

<details><summary>↩ Tool result · `toolu_014Hxs2XmUGfpPMAjWQJgEP9`</summary>

```text
Web search results for query: "arxiv 2603.16817 "Is Conformal Factuality for RAG-based LLMs Robust""

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"IRB: Automated Generation of Robust Factuality Benchmarks","url":"https://arxiv.org/pdf/2602.08070"},{"title":"RAC: Efficient LLM Factuality Correction with Retrieval Augmentation","url":"https://arxiv.org/pdf/2410.15667"},{"title":"Prompt Perturbation in Retrieval-Augmented Generation based Large Language Models","url":"https://arxiv.org/pdf/2402.07179"}]

I found the paper you were looking for. Here's what I found:

The paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" was submitted on March 17, 2026, and authored by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak.

The paper systematically analyzes the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency, and proposes novel informativeness-aware metrics.

The key findings include: (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

The paper is available on arXiv at https://arxiv.org/abs/2603.16817.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df0e798d-17c3-436b-86b8-5a0e7458e11f",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "41ef1a9a-e324-4580-9d5d-8c517a292cdc",
  "sourceToolAssistantUUID": "df0e798d-17c3-436b-86b8-5a0e7458e11f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T06:21:26.035Z_

<details><summary>↩ Tool result · `toolu_01LqrdXJDJZYsaUwrn3sffoU`</summary>

```text
Web search results for query: "arxiv 2509.23519 ReliabilityRAG "Effective and Provably Robust Defense""

Links: [{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...","url":"https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"}]

I found the paper! Here's what the search revealed:

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. 

Retrieval-Augmented Generation (RAG) enhances Large Language Models by grounding their outputs in external documents, but these systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection.

The paper presents two main contributions:

1. A graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones.

2. A scalable weighted sample and aggregate framework that explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.

ReliabilityRAG achieves superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks. The MIS variant provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.

The paper (arxiv 2509.23519) was published as part of NeurIPS 2025 proceedings and is authored by Zeyu Shen and colleagues from Princeton and Nvidia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df1b1ff-c833-4dac-8757-820b6300dbdc",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "97ad1b63-f871-4c1f-ac47-d9a9e02c12e5",
  "sourceToolAssistantUUID": "3df1b1ff-c833-4dac-8757-820b6300dbdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-30T06:21:28.964Z_

Let me also search for papers citing RobustRAG and ReliabilityRAG, and look for further partition-and-vote CP methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97ad1b63-f871-4c1f-ac47-d9a9e02c12e5",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGfcwe6Fri3Yiosm2uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36009616-b2fe-4bfc-a1ee-d11e579440c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjRWyV31BgW1PKNnJ37H1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 15829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1487,
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

_source line 39 · 2026-05-30T06:21:29.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YBndxTpWzuJFqhZvan8cPB`</summary>

```json
{
  "query": "papers citing \"Certifiably Robust RAG\" Xiang 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36009616-b2fe-4bfc-a1ee-d11e579440c2",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGfcwe6Fri3Yiosm2uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee1ecf3c-3a17-4625-90f0-b10e78977a4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjRWyV31BgW1PKNnJ37H1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 15829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1487,
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

_source line 40 · 2026-05-30T06:21:30.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E6BbuHoseh3a85cmDSTJii`</summary>

```json
{
  "query": "\"conformal prediction\" \"without exchangeability\" OR \"non-exchangeable\" robust coverage 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee1ecf3c-3a17-4625-90f0-b10e78977a4e",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGfcwe6Fri3Yiosm2uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49318edd-de31-4b0d-8913-5539a7f548b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjRWyV31BgW1PKNnJ37H1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 15829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1487,
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

_source line 41 · 2026-05-30T06:21:31.884Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012QymHEYek4FfZQf4ptdJw5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.05405",
  "prompt": "Extract the exact title, all authors, submission date, abstract, and any venue/conference information mentioned on this arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49318edd-de31-4b0d-8913-5539a7f548b3",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGfcwe6Fri3Yiosm2uk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb306ace-bb28-4157-a2fb-ea8620d1f0bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjRWyV31BgW1PKNnJ37H1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 15829,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1487
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 809,
          "output_tokens": 262,
          "cache_read_input_tokens": 15829,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1487,
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

_source line 42 · 2026-05-30T06:21:35.284Z_

<details><summary>↩ Tool result · `toolu_012QymHEYek4FfZQf4ptdJw5`</summary>

```text
# Paper Details

**Title:** "Robust Conformal Prediction Using Privileged Information"

**Authors:** Shai Feldman and Yaniv Romano

**Submission Date:** June 8, 2024 (v1); last revised January 9, 2025 (v3)

**Abstract:** The researchers developed a method for generating prediction sets with guaranteed coverage that remains robust despite corruptions in training data. Their approach extends conformal prediction methodology to address distribution shifts caused by data corruption, utilizing privileged information (PI)—additional features available only during training. They introduce a novel weighted conformal prediction generalization with theoretical coverage guarantees. The method reportedly achieves valid coverage rates and more informative predictions than existing approaches on real and synthetic datasets.

**Venue/Conference:** No specific conference or venue is mentioned on this page. The paper is classified under Computer Science > Machine Learning (cs.LG) on arXiv.

**arXiv Identifier:** 2406.05405
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb306ace-bb28-4157-a2fb-ea8620d1f0bb",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "f6b0eddf-ac6f-46cb-94cb-a38b0fadcdca",
  "sourceToolAssistantUUID": "fb306ace-bb28-4157-a2fb-ea8620d1f0bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-30T06:21:38.063Z_

<details><summary>↩ Tool result · `toolu_01E6BbuHoseh3a85cmDSTJii`</summary>

```text
Web search results for query: ""conformal prediction" "without exchangeability" OR "non-exchangeable" robust coverage 2024 2025 arxiv"

Links: [{"title":"[2202.13415] Conformal prediction beyond exchangeability","url":"https://arxiv.org/abs/2202.13415"},{"title":"Conformal prediction beyond exchangeability","url":"https://arxiv.org/pdf/2202.13415"},{"title":"Conformal Prediction Beyond Exchangeability","url":"https://arxiv.org/html/2202.13415v5"},{"title":"Conformal Prediction for Privacy-Preserving Machine Learning","url":"https://arxiv.org/html/2507.09678"},{"title":"Non-exchangeable Conformal Prediction for Temporal Graph Neural Networks","url":"https://arxiv.org/html/2507.02151v1"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/html/2410.06494v3"},{"title":"A Gentle Introduction to Conformal Time Series Forecasting","url":"https://arxiv.org/html/2511.13608v1"},{"title":"Non-exchangeable Conformal Prediction with Optimal Transport: Tackling Distribution Shifts with Unlabeled Data","url":"https://arxiv.org/html/2507.10425v1"}]

I found several relevant papers on conformal prediction without exchangeability with robust coverage properties from 2024-2025:

## Key Papers

1. **Conformal Prediction Beyond Exchangeability** (arXiv:2202.13415)
   - This paper introduces methods that are provably robust with less coverage loss when exchangeability is violated, using weighted quantiles and new randomization techniques to handle non-symmetric algorithms.
   - The methods achieve same coverage guarantees as standard conformal prediction when data is exchangeable.

2. **Non-exchangeable Conformal Prediction for Temporal Graph Neural Networks** (arXiv:2507.02151, July 2025)
   - Addresses non-exchangeability in temporal graphs through transformations or weighted quantile adjustments.

3. **Non-exchangeable Conformal Prediction with Optimal Transport** (arXiv:2507.10425, July 2025)
   - Demonstrates greater robustness to different types of distribution shifts.

4. **Conformal Prediction: A Data Perspective** (arXiv:2410.06494, March 2025)
   - Covers extensions to general non-exchangeable settings by Barber et al. (2023).
   - Discusses distributionally robust methods that calibrate confidence levels to maintain validity for worst-case distributions.

5. **A Gentle Introduction to Conformal Time Series Forecasting** (arXiv:2511.13608, November 2025)
   - Connects conformal risk control to non-exchangeable settings by incorporating weights for optimized risk bounds.

These papers represent recent developments in making conformal prediction robust when exchangeability assumptions are violated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49318edd-de31-4b0d-8913-5539a7f548b3",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "7f405a86-c635-45dc-8317-14d5c3b1bf86",
  "sourceToolAssistantUUID": "49318edd-de31-4b0d-8913-5539a7f548b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-30T06:21:47.219Z_

<details><summary>↩ Tool result · `toolu_01YBndxTpWzuJFqhZvan8cPB`</summary>

```text
Web search results for query: "papers citing "Certifiably Robust RAG" Xiang 2024 2025 2026"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"[2405.15556v1] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556v1"},{"title":"\"Certifiably Robust RAG against Retrieval Corruption\" by Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal | MLSecOps Community","url":"https://community.mlsecops.com/public/forum/boards/research-a45/posts/certifiably-robust-rag-against-retrieval-corruption-by-chong-xiang-tong-wu-zexuan-zhong-david-wagner-danqi-chen-prateek-mittal-1m53y449ia"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"Chong Xiang's research works | Princeton University and other places","url":"https://www.researchgate.net/scientific-contributions/Chong-Xiang-2175323098"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Zexuan Zhong's research works","url":"https://www.researchgate.net/scientific-contributions/Zexuan-Zhong-2182109785"}]

Let me search more specifically for papers that cite this work:

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"}]

Let me search for papers that specifically cite the Certifiably Robust RAG paper on Google Scholar or arxiv:

Links: [{"title":"[2405.15556v1] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556v1"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"dblp: Certifiably Robust RAG against Retrieval Corruption.","url":"https://dblp.org/rec/journals/corr/abs-2405-15556.html"},{"title":"1 Trustworthiness in Retrieval-Augmented Generation Systems: A Survey","url":"https://www.zhouyujia.cn/attaches/TrustworthyRAG.pdf"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"}]

Let me search for more recent papers that cite this work:

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Through the Stealth Lens: Attention-Aware Defenses Against Poisoning in RAG | OpenReview","url":"https://openreview.net/forum?id=PS43wqCSME"},{"title":"RAGuard: A Layered Defense Framework for Retrieval- ...","url":"https://openreview.net/pdf/f7bd605a521e7fe5a23b34a2ef51659d26264d62.pdf"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"}]

Based on my search results, I found several important papers related to the "Certifiably Robust RAG" work by Xiang et al. (2024). Here are the key findings:

## Original Paper

The original work "Certifiably Robust RAG against Retrieval Corruption" proposes RobustRAG, the first defense framework with certifiable robustness against retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. The paper is authored by Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, and Prateek Mittal.

## Papers Citing This Work (2024-2026)

Several recent papers build upon or cite the Certifiably Robust RAG work:

1. **ReliabilityRAG (2025)** - A paper by Shen, Imana, Wu, Xiang, Mittal, and Korolova titled "ReliabilityRAG: effective and provably robust defense for RAG-based web-search" presented at the Thirty-ninth Annual Conference on Neural Information Processing Systems.

2. **Trustworthy RAG Survey** - A trustworthiness survey discusses how RobustRAG proposes a defense framework for protecting RAG systems from retrieval corruption attacks, utilizing an isolate-then-aggregate strategy that computes LLM responses for each passage in isolation and then securely aggregates these responses.

3. **RAG Defense Papers (2025-2026)** - Recent work includes papers on RAGuard, RAGPart & RAGMask, and other layered defense frameworks addressing corpus poisoning and retrieval corruption in RAG systems.

The web search results indicate that the Certifiably Robust RAG paper has influenced the broader research community working on RAG security and robustness, with multiple follow-up works exploring different defense mechanisms and attack strategies in 2025 and 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee1ecf3c-3a17-4625-90f0-b10e78977a4e",
  "isSidechain": true,
  "promptId": "0bbfb3fe-705b-4235-955b-db4183adf96c",
  "agentId": "a6c6bffecb9fbd54d",
  "type": "user",
  "uuid": "0ed36c1d-75ae-466e-87be-53d3c191c53d",
  "sourceToolAssistantUUID": "ee1ecf3c-3a17-4625-90f0-b10e78977a4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-30T06:22:39.155Z_

Here is the complete verification report for your literature survey.

---

## Paper 1: RPS (Scholten & Gunnemann)

- **Title:** "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning"
- **Authors:** Yan Scholten, Stephan Gunnemann
- **Venue:** ICLR 2025 (Spotlight) -- **CONFIRMED**
- **URL:** https://arxiv.org/abs/2410.09878
- **Dates:** Submitted Oct 13, 2024; revised Mar 16, 2025 (v4)
- **Summary:** Proposes Reliable Prediction Sets (RPS) that use smoothed score functions over training-data partitions and majority-vote aggregation over calibration-data subsets to maintain conformal coverage guarantees under both training and calibration poisoning.
- **Code:** https://github.com/yascho/reliable_conformal_prediction
- **Status:** VERIFIED. Title, authors, venue, and arXiv ID all match your listing.

---

## Paper 2: RobustRAG (Xiang et al.)

- **Title:** "Certifiably Robust RAG against Retrieval Corruption" (note: the actual title does NOT include "RobustRAG" -- that is the method name used inside the paper)
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** IEEE SaTML 2026 -- **CONFIRMED** (found on the SaTML 2026 accepted papers page; affiliations listed as NVIDIA, Princeton, UC Berkeley)
- **URL:** https://arxiv.org/abs/2405.15556
- **Dates:** Submitted May 24, 2024; revised Apr 1, 2026 (v2)
- **Summary:** Introduces an isolate-then-aggregate strategy that partitions retrieved passages into disjoint groups, generates LLM responses per group, and securely aggregates them (keyword-based and decoding-based), providing certified robustness against bounded adversarial passage injection.
- **Important correction:** Your listing says "RobustRAG" as a standalone title. The actual arXiv title is "Certifiably Robust RAG against Retrieval Corruption." Also, the authors are Xiang et al., not "Gao et al." The venue is **IEEE SaTML 2026**, confirmed.

---

## Paper 3: Conformal Factuality for RAG (Chen et al.)

- **Title:** "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"
- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak
- **Venue:** No venue listed (arXiv preprint as of March 2026)
- **URL:** https://arxiv.org/abs/2603.16817
- **Date:** Submitted March 17, 2026
- **Summary:** Systematically evaluates conformal factuality filtering for RAG-based LLMs, finding it suffers from low usefulness at high factuality levels, lacks robustness to distribution shifts/distractors, and that lightweight entailment verifiers match LLM-based scorers at 100x fewer FLOPs.
- **Status:** VERIFIED. The arXiv ID and title match. Note the full title includes the subtitle "Novel Metrics and Systematic Insights."

---

## Paper 4: ReliabilityRAG (Shen et al.)

- **Title:** "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search"
- **Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova
- **Venue:** NeurIPS 2025 -- **CONFIRMED** (OpenReview and NeurIPS virtual site both list it)
- **URL:** https://arxiv.org/abs/2509.23519
- **Dates:** Submitted Sep 27, 2025; revised Feb 15, 2026 (v2)
- **Summary:** Uses graph-theoretic methods (Maximum Independent Set) to identify a consistent majority among retrieved documents, leveraging document reliability signals for provable robustness against bounded adversarial corruption, with a scalable weighted-sampling variant for long-form generation.
- **Status:** VERIFIED. Title, authors, venue, and arXiv ID all match.

---

## Search 5: CP Beyond Exchangeability

Key papers found:

- **"Conformal Prediction Beyond Exchangeability"** -- Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani. arXiv:2202.13415 (Feb 2022, revised Mar 2023). The foundational work introducing weighted quantiles for CP under distribution drift. Published in Annals of Statistics.
- **"Non-exchangeable Conformal Prediction with Optimal Transport"** -- arXiv:2507.10425 (Jul 2025). Tackles distribution shifts using optimal transport with unlabeled data.
- **"Non-exchangeable Conformal Prediction for Temporal Graph Neural Networks"** -- arXiv:2507.02151 (Jul 2025). Extends CP to temporal graphs.
- **"A Gentle Introduction to Conformal Time Series Forecasting"** -- arXiv:2511.13608 (Nov 2025). Survey connecting conformal risk control to non-exchangeable settings.

---

## Search 6: Partition-and-Vote Aggregation for Robust CP

Key papers found:

- **Paper 1 (RPS) above** is the primary hit -- it is exactly a partition-and-vote method for robust CP under poisoning.
- **"Multi-Distribution Robust Conformal Prediction"** -- Yuqi Yang, Ying Jin. arXiv:2601.02998 (Jan 2026). Proposes max-p aggregation for CP valid across multiple heterogeneous distributions. Preprint, no venue listed yet.
- **"Robust Conformal Prediction Using Privileged Information"** -- Shai Feldman, Yaniv Romano. arXiv:2406.05405 (Jun 2024, revised Jan 2025). Weighted CP generalization using privileged information to handle distribution shifts from data corruption.
- **Deep Partition Aggregation / Finite Aggregation** (Levine & Feizi, 2020-2022) -- the precursor idea of training on disjoint partitions and majority-voting for certified poisoning defense (not CP-specific but the technique RPS builds on).

---

## Search 7: RobustRAG Venue Confirmation

**Confirmed: IEEE SaTML 2026.** The paper "Certifiably Robust RAG against Retrieval Corruption" by Xiang, Wu, Zhong, Wagner, Chen, Mittal appears on the SaTML 2026 accepted papers page (https://satml.org/accepted-papers/). The authors are **Xiang et al.**, not "Gao et al." as mentioned in your query -- this may be an error in your notes.

---

## Key Citing / Follow-up Papers Found

Papers that cite RobustRAG and/or are relevant to robust RAG under adversarial poisoning:

| Paper | Authors | Venue | URL |
|-------|---------|-------|-----|
| ReliabilityRAG | Shen, Imana, Wu, Xiang, Mittal, Korolova | NeurIPS 2025 | https://arxiv.org/abs/2509.23519 |
| RAGPart & RAGMask | (retrieval-stage defenses) | arXiv preprint 2024 | https://arxiv.org/abs/2512.24268 |
| Semantic Chameleon: Corpus-Dependent Poisoning | -- | arXiv Mar 2026 | https://arxiv.org/abs/2603.18034 |
| Securing RAG: Taxonomy of Attacks, Defenses | -- | arXiv Apr 2026 | https://arxiv.org/abs/2604.08304 |
| Through the Stealth Lens: Attention-Aware Defenses | -- | OpenReview | https://openreview.net/forum?id=PS43wqCSME |
| Towards More Robust RAG: Evaluating Under Adversarial Poisoning | -- | arXiv Dec 2024 | https://arxiv.org/abs/2412.16708 |

---

## Warnings / Corrections for Your Survey

1. **Paper 2 author attribution:** Your query references "Gao et al." for RobustRAG. The correct first author is **Chong Xiang**, not Gao. Please double-check your citation.
2. **Paper 2 title:** The arXiv title is "Certifiably Robust RAG against Retrieval Corruption" -- "RobustRAG" is the method name, not part of the formal title.
3. **Paper 3 has no venue yet:** As of May 2026, arXiv:2603.16817 is a preprint with no conference acceptance listed.
4. **All four arXiv IDs are valid and resolve correctly.** No fabricated/hallucinated paper IDs were found among these four.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed36c1d-75ae-466e-87be-53d3c191c53d",
  "isSidechain": true,
  "agentId": "a6c6bffecb9fbd54d",
  "requestId": "req_011CbYGhBN4JKjCzfxeZaMA9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2e4b38f-b0cc-4922-9c5e-523818089225",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "346aee95-9c0f-4dac-99e5-86fe556b6f86",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FUcXGKjXj4ujaQQT6im12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 3343,
      "cache_read_input_tokens": 17316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3343,
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
