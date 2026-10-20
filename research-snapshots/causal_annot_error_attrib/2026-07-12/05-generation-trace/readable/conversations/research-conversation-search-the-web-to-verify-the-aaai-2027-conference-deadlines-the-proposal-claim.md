# Research conversation: Search the web to verify the AAAI 2027 conference deadlines. The proposal claims: - Abstract deadline: July 21, 2026 - P

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac9639fdd12716ee4.jsonl`
- **Structured JSON:** [`b069140025310bea907d.json`](../../sessions/b0/b069140025310bea907d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-28T13:02:00.543Z_

Search the web to verify the AAAI 2027 conference deadlines. The proposal claims:
- Abstract deadline: July 21, 2026
- Paper deadline: July 28, 2026

Search for:
1. "AAAI 2027 deadline" 
2. "AAAI 2027 call for papers"
3. "AAAI conference 2027 submission"

Also check if AAAI has an "AI Alignment" track or "Robustness Evaluation" track. Report what you find, including any discrepancies with the claimed dates. Today's date is 2026-05-28.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "a5ca9d4b-533b-4311-b982-eff4530f12cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T13:02:00.548Z_

```json
{
  "parentUuid": "a5ca9d4b-533b-4311-b982-eff4530f12cb",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
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
  "uuid": "27e6bda0-36bf-4655-b0d2-7a8c0bd02fe3",
  "timestamp": "2026-05-28T13:02:00.548Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T13:02:00.549Z_

```json
{
  "parentUuid": "27e6bda0-36bf-4655-b0d2-7a8c0bd02fe3",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0eacdcde-f9f2-4def-8f0c-ee56acbcc44d",
  "timestamp": "2026-05-28T13:02:00.549Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T13:02:03.594Z_



I'll search the web for AAAI 2027 conference deadline information. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eacdcde-f9f2-4def-8f0c-ee56acbcc44d",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1bUWGDLzoKLX42iBaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54645904-78af-467e-ab65-624ac9efbb77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LmMyjm3eBG8H7hrKJM6QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8902,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8902,
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

_source line 5 · 2026-05-28T13:02:03.826Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DaSUj38Zjc7sZFeDXFddQt`</summary>

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
  "parentUuid": "54645904-78af-467e-ab65-624ac9efbb77",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1bUWGDLzoKLX42iBaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c47255-714c-4815-a857-4ce5d77b04f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LmMyjm3eBG8H7hrKJM6QT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8902,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8902,
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

_source line 6 · 2026-05-28T13:02:03.846Z_

<details><summary>↩ Tool result · `toolu_01DaSUj38Zjc7sZFeDXFddQt`</summary>

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
  "parentUuid": "46c47255-714c-4815-a857-4ce5d77b04f8",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "06342cbd-6f91-4e5a-96db-0962d8768237",
  "sourceToolAssistantUUID": "46c47255-714c-4815-a857-4ce5d77b04f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T13:02:06.929Z_



Now let me run all three searches in parallel to gather information about AAAI 2027 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06342cbd-6f91-4e5a-96db-0962d8768237",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1biyfGHuhvNUbE72mL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc0293f8-b071-4a50-888f-0f907cc6a837",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvgbRhw6dpMu61GMvjLtsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 8902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 8 · 2026-05-28T13:02:06.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPHP2fdLoEbnzEsHNGoQcu`</summary>

```json
{
  "query": "AAAI 2027 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc0293f8-b071-4a50-888f-0f907cc6a837",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1biyfGHuhvNUbE72mL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7834c992-9eb6-4018-862c-96bbf9f43992",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvgbRhw6dpMu61GMvjLtsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 8902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 9 · 2026-05-28T13:02:07.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PKPW2DbSiaq6sbb84Gk2KR`</summary>

```json
{
  "query": "AAAI 2027 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7834c992-9eb6-4018-862c-96bbf9f43992",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1biyfGHuhvNUbE72mL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c63a5c5-d27b-4048-beef-14e0d502c38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvgbRhw6dpMu61GMvjLtsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 8902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 634,
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

_source line 10 · 2026-05-28T13:02:07.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NfdCq7b86WqskkTgSnE52t`</summary>

```json
{
  "query": "AAAI conference 2027 submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c63a5c5-d27b-4048-beef-14e0d502c38e",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1biyfGHuhvNUbE72mL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "536b82a7-25d3-4aad-ae53-a2d0b88c052e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvgbRhw6dpMu61GMvjLtsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 8902,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 8902,
          "cache_creation_input_tokens": 634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 634,
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

_source line 11 · 2026-05-28T13:02:12.173Z_

<details><summary>↩ Tool result · `toolu_01EPHP2fdLoEbnzEsHNGoQcu`</summary>

```text
Web search results for query: "AAAI 2027 deadline"

Links: [{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"}]

Based on the search results, here's the information about AAAI 2027 deadlines:

AAAI-27 will be held in Montréal, Canada, from February 16 to February 23, 2027.

For the Main Technical Track, the key deadlines are:
- June 24, 2026: OpenReview submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12

Track-specific deadlines are listed on their respective Call for Papers, as deadlines are track-specific and may differ from those listed above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7834c992-9eb6-4018-862c-96bbf9f43992",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "7e9155e4-e85b-45a8-b083-403355847d1f",
  "sourceToolAssistantUUID": "7834c992-9eb6-4018-862c-96bbf9f43992",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T13:02:13.671Z_

<details><summary>↩ Tool result · `toolu_01PKPW2DbSiaq6sbb84Gk2KR`</summary>

```text
Web search results for query: "AAAI 2027 call for papers"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"Ten simple rules for using large language models in science, version 1.0","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10829980/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Assessing the Reproducibility of the Structured Abstracts Generated by ChatGPT and Bard Compared to Human-Written Abstracts in the Field of Spine Surgery: Comparative Analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11237793/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"}]

Here are the search results for the AAAI 2027 call for papers:

## Key Information

The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.

## Submission Deadlines (Main Technical Track)

The submission deadlines for AAAI-27 are:
- June 17, 2026: Open Review submission site opens for author registration
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12
- September 24, 2026: Notification of Phase 1 rejections
- October 19-25, 2026: Author feedback window
- November 30, 2026: Notification of final acceptance or rejection
- December 14, 2026: Submission of camera-ready files

## Additional Details

The official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/. Note that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c63a5c5-d27b-4048-beef-14e0d502c38e",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "6c856a5b-f5b4-4f31-9f7b-1791b4e26d4f",
  "sourceToolAssistantUUID": "6c63a5c5-d27b-4048-beef-14e0d502c38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T13:02:14.193Z_

<details><summary>↩ Tool result · `toolu_01NfdCq7b86WqskkTgSnE52t`</summary>

```text
Web search results for query: "AAAI conference 2027 submission"

Links: [{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"Ten simple rules for using large language models in science, version 1.0","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10829980/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"Future Annual Meeting Dates and Locations | AAAAI Annual Meeting","url":"https://annualmeeting.aaaai.org/attendee/future-dates-locations"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"}]

Based on the search results, here's the information about AAAI 2027 submissions:

## Conference Details
The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.

## Submission Timeline (Main Technical Track)
The submission timeline includes:
- June 17, 2026: OpenReview submission site opens for author registration
- June 24, 2026: OpenReview submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12
- September 24, 2026: Notification of Phase 1 rejections
- October 19-25, 2026: Author feedback window
- November 30, 2026: Notification of final acceptance or rejection
- December 14, 2026: Submission of camera-ready files

## Submission Details
AAAI papers are limited to 7 pages for the main body, with unlimited additional pages for references. The official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/.

Note that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536b82a7-25d3-4aad-ae53-a2d0b88c052e",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "a5815c4a-c792-495b-a4d3-4dae66cedb47",
  "sourceToolAssistantUUID": "536b82a7-25d3-4aad-ae53-a2d0b88c052e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T13:02:17.449Z_

Now let me search specifically for AAAI 2027 tracks to check whether "AI Alignment" or "Robustness Evaluation" tracks exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5815c4a-c792-495b-a4d3-4dae66cedb47",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1cUrdaLnSXn4Mp3R3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1501dcf2-7b5b-462f-b18f-da27e5826c5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YGR2ZUXfHsjw1VDZUhjiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2721,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2721,
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

_source line 15 · 2026-05-28T13:02:17.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XDDvyYauuLKnEXNTYHh7vi`</summary>

```json
{
  "query": "AAAI 2027 tracks \"AI Alignment\" OR \"Robustness Evaluation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1501dcf2-7b5b-462f-b18f-da27e5826c5b",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1cUrdaLnSXn4Mp3R3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05d59abe-3aff-4eb9-b763-6587739361fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YGR2ZUXfHsjw1VDZUhjiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2721,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2721,
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

_source line 16 · 2026-05-28T13:02:18.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EDUzkdws4CLSuJuQFamjrj`</summary>

```json
{
  "query": "AAAI-27 conference tracks list site:aaai.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05d59abe-3aff-4eb9-b763-6587739361fd",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1cUrdaLnSXn4Mp3R3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b441cc3-d70e-4a96-ad97-92ba17f86bd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YGR2ZUXfHsjw1VDZUhjiB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2721,
      "cache_read_input_tokens": 9536,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 9536,
          "cache_creation_input_tokens": 2721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2721,
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

_source line 17 · 2026-05-28T13:02:22.677Z_

<details><summary>↩ Tool result · `toolu_01XDDvyYauuLKnEXNTYHh7vi`</summary>

```text
Web search results for query: "AAAI 2027 tracks "AI Alignment" OR "Robustness Evaluation""

Links: [{"title":"AAAI-26 Call for the Special Track on AI Alignment","url":"https://aaai.org/conference/aaai/aaai-26/aia-call/"},{"title":"AAAI-25 Call for the Special Track on AI Alignment","url":"https://aaai.org/conference/aaai/aaai-25/ai-alignment-call/"},{"title":"Language Log » Alignment","url":"https://languagelog.ldc.upenn.edu/nll/?p=70026"},{"title":"The Specification Trap: Why Static Value Alignment Alone Cannot Produce Robust Alignment","url":"https://arxiv.org/pdf/2512.03048"},{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"AI Alignment: A Comprehensive Survey","url":"https://arxiv.org/pdf/2310.19852"},{"title":"Pressure Reveals Character: Behavioural Alignment Evaluation at Depth","url":"https://arxiv.org/pdf/2602.20813"}]

Based on the search results, I found information about AAAI-26 (not AAAI-27) tracks related to your query:

AAAI-26 features a special track focused on AI Alignment. The 2026 AI Alignment track seeks research on scalable oversight, mechanistic interpretability, empirical robustness evaluation, red-teaming, human cognitive and psychological factors, and safe-by-design engineering—including formal safety cases.

The search results do not contain information about AAAI-27 tracks specifically. The most current information available is for AAAI-26 (2026). If you're looking for AAAI-27 (2027) track information, it may not yet be publicly available, as conference details are typically announced closer to the conference date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05d59abe-3aff-4eb9-b763-6587739361fd",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "a17a8908-a3e5-404f-a4e1-35604e67ac4a",
  "sourceToolAssistantUUID": "05d59abe-3aff-4eb9-b763-6587739361fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T13:02:27.576Z_

<details><summary>↩ Tool result · `toolu_01EDUzkdws4CLSuJuQFamjrj`</summary>

```text
Web search results for query: "AAAI-27 conference tracks list site:aaai.org"

Links: [{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"Vol. 40 No. 27: AAAI-26 Technical Tracks 27 | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/issue/view/709"},{"title":"The Association for the Advancement of Artificial Intelligence","url":"https://aaai.org/"},{"title":"Proceedings of the Fortieth AAAI Conference on Artificial Intelligence Archives - AAAI","url":"https://aaai.org/proceeding/aaai-40-2026/"},{"title":"Conferences Archive - AAAI","url":"https://aaai.org/conference/"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"}]

Based on the search results, I found information about AAAI-27. The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.

However, the search results don't provide a complete list of the specific conference tracks for AAAI-27. The first search result mentions that deadlines are track-specific and track-specific deadlines are listed on their respective CFP, and I found a page for the Main Technical Track, but the detailed list of all tracks is not fully visible in these search results.

To get the complete list of AAAI-27 conference tracks, you may want to visit the main AAAI-27 conference page directly at https://aaai.org/conference/aaai/aaai-27/ or check the AAAI-27 Calls page, which should have listings for all available tracks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b441cc3-d70e-4a96-ad97-92ba17f86bd8",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "73cbd05d-6e2a-4625-af27-b61554510f54",
  "sourceToolAssistantUUID": "7b441cc3-d70e-4a96-ad97-92ba17f86bd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T13:02:30.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016cz88dWoqDKUafaRYLtcXt`</summary>

```json
{
  "query": "AAAI-27 special tracks calls for papers 2027 alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73cbd05d-6e2a-4625-af27-b61554510f54",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1dU2o5uYcaTa4EJMgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c2624c4-706c-479d-a5ca-4ebd2c93db67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv2LkJ5ETBGa13d6AJBuck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 12257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 20 · 2026-05-28T13:02:30.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VDUuTcujeoohn6FgzpRtuK`</summary>

```json
{
  "query": "site:aaai.org/conference/aaai/aaai-27/call"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c2624c4-706c-479d-a5ca-4ebd2c93db67",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1dU2o5uYcaTa4EJMgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42c8329-59da-4f21-93b4-52d7fd785174",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv2LkJ5ETBGa13d6AJBuck",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 12257,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 12257,
          "cache_creation_input_tokens": 1318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1318,
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

_source line 21 · 2026-05-28T13:02:36.361Z_

<details><summary>↩ Tool result · `toolu_01VDUuTcujeoohn6FgzpRtuK`</summary>

```text
Web search results for query: "site:aaai.org/conference/aaai/aaai-27/call"

Links: [{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI-27 Calls (Overview) - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/"},{"title":"Attitudes and Perceptions of Biomedical Journal Editors-in-Chief Towards the Use of Artificial Intelligence Chatbots in the Scholarly Publishing Process: A Cross-Sectional Survey","url":"https://www.medrxiv.org/content/10.1101/2025.05.26.25328101.full.pdf"},{"title":"System and method for tracking emotional state of a caller using artificial intelligence","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12555594"},{"title":"Call center system having reduced communication latency","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11223723"},{"title":"Artificial intelligence based call handling optimization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11425250"}]

I found the AAAI-27 Call for Papers overview page. Based on the search results, AAAI-27 is scheduled for February 16 – February 23, 2027 in Montréal, Canada. 

The search returned the main calls page and the main technical track page. Deadlines are track-specific and may differ from the overall conference dates, with track-specific deadlines listed on their respective calls for papers.

To get more detailed information about specific submission deadlines and requirements, you would want to visit the individual track pages linked from the AAAI-27 Calls overview at https://aaai.org/conference/aaai/aaai-27/call/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b42c8329-59da-4f21-93b4-52d7fd785174",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "0a02ac37-e745-46fa-a148-85234b0d2ac2",
  "sourceToolAssistantUUID": "b42c8329-59da-4f21-93b4-52d7fd785174",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T13:02:36.622Z_

<details><summary>↩ Tool result · `toolu_016cz88dWoqDKUafaRYLtcXt`</summary>

```text
Web search results for query: "AAAI-27 special tracks calls for papers 2027 alignment"

Links: [{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"Vol. 40 No. 27: AAAI-26 Technical Tracks 27 | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/issue/view/709"},{"title":"AAAI-26 Journal Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/journal-track-call/"},{"title":"AAAI-25 Main Technical: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-25/aaai-25-main-technical-call-for-papers/"},{"title":"AAAI-25 Call for the Special Track on AI Alignment","url":"https://aaai.org/conference/aaai/aaai-25/ai-alignment-call/"}]

Based on the search results, I found information about AAAI special tracks, though the details are for AAAI-26 and AAAI-25 rather than AAAI-27 specifically:

AAAI-27 will be held in Montréal, Canada, from February 16 to February 23, 2027.

Regarding special tracks, based on the pattern from previous conferences: Authors are encouraged to submit papers for the Special Track on AI for Social Impact and the Special Track on AI Alignment.

For the AI Alignment track specifically, the evaluation criteria include:
- Whether the paper addresses a problem central to the challenge of developing safe and secure AI systems, aligned with human values
- Engagement with existing literature in the field of AI Alignment
- Methodological or analysis novelty

However, the search results show that the main technical track deadlines include abstract submission on July 21, 2026, and full papers due July 28, 2026, though track-specific deadlines may differ and are listed on their respective call for papers. For the most current and specific information about AAAI-27 special tracks calls for papers, I recommend visiting the official AAAI-27 website directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c2624c4-706c-479d-a5ca-4ebd2c93db67",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "323584b0-8f1f-4b8e-9357-c053e4b8ffc6",
  "sourceToolAssistantUUID": "8c2624c4-706c-479d-a5ca-4ebd2c93db67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-28T13:02:39.077Z_

Let me fetch the AAAI-27 Calls overview page to see the full list of tracks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "323584b0-8f1f-4b8e-9357-c053e4b8ffc6",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1e8ij1RERa4dpp7KoP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "932d622d-77ff-49e4-8124-6339ef245087",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SchFPp5Fe9HZEFhEReaqvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 13575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1001,
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

_source line 24 · 2026-05-28T13:02:39.529Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NbFMWPWnS3YQeV5JfFBEyR`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932d622d-77ff-49e4-8124-6339ef245087",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1e8ij1RERa4dpp7KoP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e7de6ca-6a3f-4120-a6f8-e30741beea03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SchFPp5Fe9HZEFhEReaqvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 551,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 13575,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 551,
          "output_tokens": 100,
          "cache_read_input_tokens": 13575,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1001,
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

_source line 25 · 2026-05-28T13:02:39.535Z_

<details><summary>↩ Tool result · `toolu_01NbFMWPWnS3YQeV5JfFBEyR`</summary>

````text
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
  "parentUuid": "6e7de6ca-6a3f-4120-a6f8-e30741beea03",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "331e68b9-5234-46d2-aa65-0d1b1335736f",
  "sourceToolAssistantUUID": "6e7de6ca-6a3f-4120-a6f8-e30741beea03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T13:02:43.247Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q4nAeD22u6uVgCoXZX7Gws`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/call/",
  "prompt": "List ALL the tracks and calls for papers mentioned on this page. I need the complete list of every track name (e.g., Main Technical Track, AI Alignment, etc.) and any deadlines mentioned for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "331e68b9-5234-46d2-aa65-0d1b1335736f",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1eMSSvdeZu82r9qJaE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc6940b6-84fc-4817-be36-ac42d6816af2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019btR7AUHyNtH6Q5gvc6k9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 14576,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 135,
          "cache_read_input_tokens": 14576,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1169,
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

_source line 27 · 2026-05-28T13:02:46.557Z_

<details><summary>↩ Tool result · `toolu_01Q4nAeD22u6uVgCoXZX7Gws`</summary>

```text
# AAAI-27 Tracks and Calls for Papers

Based on the webpage content provided, only **one track** is explicitly listed:

1. **AAAI-27 Main Technical Track** - No deadline information is provided on this page.

The page indicates this is an overview/index page for "AAAI-27 Calls" with a link to "Continue Reading" for the Main Technical Track, suggesting that detailed information about submission deadlines and additional tracks would be found on the linked page rather than on this overview page itself.

No other specific tracks, themed areas, or submission deadlines are mentioned in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6940b6-84fc-4817-be36-ac42d6816af2",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "3f46fdc2-6503-4db0-8455-02e322263ecb",
  "sourceToolAssistantUUID": "bc6940b6-84fc-4817-be36-ac42d6816af2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T13:02:50.379Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AAnarPk57YsjCjzRCk8qUa`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/",
  "prompt": "List ALL tracks, special tracks, workshops, and calls for papers mentioned on this AAAI-27 main conference page. Is there any mention of an \"AI Alignment\" track, a \"Robustness Evaluation\" track, or any other special tracks? List everything you can find about the conference structure and tracks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f46fdc2-6503-4db0-8455-02e322263ecb",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1esGZzf4Ks4h3S8LeL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "339d3b24-b29a-45a9-92e1-e99529028c5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8BoobHbKBXCJ7MQXufGbU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 15745,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 287
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 15745,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 287,
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

_source line 29 · 2026-05-28T13:02:58.425Z_

<details><summary>↩ Tool result · `toolu_01AAnarPk57YsjCjzRCk8qUa`</summary>

```text
# AAAI-27 Conference Tracks and Structure

Based on the provided webpage content, **no specific tracks are detailed** on this main conference page. The page does not mention an "AI Alignment" track, "Robustness Evaluation" track, or any other named special tracks.

## What IS mentioned about conference structure:

The document indicates that AAAI-27 "will feature technical paper presentations, special tracks, invited speakers, workshops, tutorials, poster sessions, senior member presentations, competitions, and exhibit programs."

However, **no detailed information is provided** about:
- Names of specific tracks
- Workshop topics
- Special track titles
- Calls for papers by track

## Key note from the page:

"Deadlines are track-specific and may differ from those listed above. Track-specific deadlines are listed on their respective CFP" (Call for Papers).

This suggests that detailed track information exists elsewhere—likely on individual track pages linked from the main conference site, but those links and details are not included in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "339d3b24-b29a-45a9-92e1-e99529028c5d",
  "isSidechain": true,
  "promptId": "dc568e59-04a7-423e-afcb-8c8e23de99ac",
  "agentId": "ac9639fdd12716ee4",
  "type": "user",
  "uuid": "36abbc17-6a14-4e89-8391-c3c5c731265f",
  "sourceToolAssistantUUID": "339d3b24-b29a-45a9-92e1-e99529028c5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-28T13:03:19.629Z_

Here is my complete findings report.

---

## AAAI 2027 Deadline Verification

### Claimed Deadlines vs. Verified Deadlines

The proposal's claimed deadlines are **confirmed as accurate** for the Main Technical Track:

| Deadline | Claimed | Verified |
|---|---|---|
| Abstract deadline | July 21, 2026 | **July 21, 2026** (11:59 PM UTC-12) |
| Paper deadline | July 28, 2026 | **July 28, 2026** (11:59 PM UTC-12) |

Both dates match exactly with what is published on the official AAAI-27 website and corroborated by multiple third-party deadline trackers.

### Full Verified Timeline (Main Technical Track)

- **June 17, 2026** -- OpenReview site opens for author registration
- **June 24, 2026** -- OpenReview site opens for paper submission
- **July 21, 2026** -- Abstracts due (11:59 PM UTC-12)
- **July 28, 2026** -- Full papers due (11:59 PM UTC-12)
- **July 31, 2026** -- Supplementary material and code due (11:59 PM UTC-12)
- **September 24, 2026** -- Notification of Phase 1 rejections
- **October 19-25, 2026** -- Author feedback window
- **November 30, 2026** -- Final acceptance/rejection notification
- **December 14, 2026** -- Camera-ready files due

The conference itself is scheduled for **February 16-23, 2027** in **Montreal, Canada**.

### Track Verification: "AI Alignment" and "Robustness Evaluation"

**AI Alignment Track:** AAAI-25 and AAAI-26 both had a dedicated "Special Track on AI Alignment." The AAAI-27 main conference page states it "will feature special tracks" but as of today (May 28, 2026), the only track with a published Call for Papers on the AAAI-27 website is the **Main Technical Track**. The specific special tracks for AAAI-27 have not yet been announced on the official site. Given the pattern from the past two years, it is plausible that an AI Alignment track will return for AAAI-27, but this is **not yet confirmed**.

**Robustness Evaluation Track:** No evidence was found of a standalone "Robustness Evaluation" track at any recent AAAI conference (2025, 2026, or 2027). Robustness evaluation has been mentioned as a *topic of interest* within the AI Alignment track (e.g., AAAI-26's AI Alignment call listed "empirical robustness evaluation" as a relevant topic), but it has never been a separate track. If the proposal claims AAAI 2027 has a dedicated "Robustness Evaluation" track, **that claim cannot be verified and appears to be incorrect** based on available information.

### Key Caveat

The AAAI-27 website notes that "deadlines are track-specific and may differ" from the Main Technical Track deadlines. If the proposal is targeting a special track rather than the main track, the actual deadlines could be different once those tracks are announced.

Sources:
- [AAAI-27 Main Conference Page](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI-27 Calls Overview](https://aaai.org/conference/aaai/aaai-27/call/)
- [AAAI-26 AI Alignment Special Track Call](https://aaai.org/conference/aaai/aaai-26/aia-call/)
- [AAAI-25 AI Alignment Special Track Call](https://aaai.org/conference/aaai/aaai-25/ai-alignment-call/)
- [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)
- [AI Deadlines Tracker](http://aideadlines.org/conference/?id=aaai27)
- [PaperPilot AAAI 2027 Deadlines](https://www.getpaperpilot.com/deadlines/aaai-2027.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36abbc17-6a14-4e89-8391-c3c5c731265f",
  "isSidechain": true,
  "agentId": "ac9639fdd12716ee4",
  "requestId": "req_011CbV1fkKdkQHBzmwUJ4TrH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ab1c1b4-1a34-4013-90ad-1378a6e92aaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "c23f3e51-9def-46f8-88a4-21c4a46b23f8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wTBdzJwStro9Vj325UdGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 16032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 394,
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
