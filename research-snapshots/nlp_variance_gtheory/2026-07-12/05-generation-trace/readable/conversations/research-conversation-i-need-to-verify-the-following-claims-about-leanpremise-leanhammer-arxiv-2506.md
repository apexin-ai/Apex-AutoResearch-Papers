# Research conversation: I need to verify the following claims about LeanPremise/LeanHammer (arXiv 2506.07477): 1. Is it accepted at ICLR 2026? 2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa85e714bc0c4243e.jsonl`
- **Structured JSON:** [`fe908b2db6d6f49f24a6.json`](../../sessions/fe/fe908b2db6d6f49f24a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-28T14:48:04.686Z_

I need to verify the following claims about LeanPremise/LeanHammer (arXiv 2506.07477):
1. Is it accepted at ICLR 2026?
2. Does it achieve 79.4% relative proof rate on OOD benchmarks (miniCTX-v2)?
3. Does it show project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%?
4. Is it described as "first end-to-end domain-general hammer for Lean"?
5. Does it use an 82M-parameter neural premise selector?

Please search for:
- "LeanPremise LeanHammer" OR "arXiv 2506.07477"
- "premise selection lean hammer ICLR 2026"
- Try to fetch the arxiv page at https://arxiv.org/abs/2506.07477

Report what you find, including any discrepancies with the claims above.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "70802069-6e83-4b22-9f01-e27386da3a84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T14:48:04.689Z_

```json
{
  "parentUuid": "70802069-6e83-4b22-9f01-e27386da3a84",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
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
  "uuid": "8ad813db-745b-4a0c-964d-7b8eed948b17",
  "timestamp": "2026-05-28T14:48:04.689Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T14:48:04.690Z_

```json
{
  "parentUuid": "8ad813db-745b-4a0c-964d-7b8eed948b17",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "237b8a18-bbb1-425a-abab-664d59254a4f",
  "timestamp": "2026-05-28T14:48:04.690Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T14:48:07.200Z_



I'll search for information about this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "237b8a18-bbb1-425a-abab-664d59254a4f",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gbqrvqaTN9my8wjmL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c1d3586-aeb5-46e8-b7d2-0048633d9fc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vz5UceBdMHi5ydijuRje88",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8983,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 5 · 2026-05-28T14:48:07.581Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Qi3URHUcz3412SpEZpfLF`</summary>

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
  "parentUuid": "0c1d3586-aeb5-46e8-b7d2-0048633d9fc2",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gbqrvqaTN9my8wjmL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a1708ba-2cd1-4532-87b0-4daf266267cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vz5UceBdMHi5ydijuRje88",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8983,
      "cache_read_input_tokens": 0,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8983,
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

_source line 6 · 2026-05-28T14:48:07.585Z_

<details><summary>↩ Tool result · `toolu_017Qi3URHUcz3412SpEZpfLF`</summary>

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
  "parentUuid": "0a1708ba-2cd1-4532-87b0-4daf266267cc",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "0eca6063-25f4-496e-ac89-101b4070148c",
  "sourceToolAssistantUUID": "0a1708ba-2cd1-4532-87b0-4daf266267cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T14:48:10.095Z_



Now let me run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eca6063-25f4-496e-ac89-101b4070148c",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gpba9fB9CVPhokRxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb7765b5-bef0-421b-be69-6919d24ff14d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmtnxXXzMAjGHD5h6mV6qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 8 · 2026-05-28T14:48:14.376Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PHJVmSdWJHxKdBssNdDUge`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.07477",
  "prompt": "Extract ALL details from this paper page: title, authors, abstract, submission date, any conference acceptance info, and all specific numerical results mentioned. Pay special attention to: proof rates, benchmark names (especially miniCTX-v2), model parameters (especially 82M), project-level results (Carleson, Foundation, ConNF, FLT), and any claim about being \"first end-to-end domain-general hammer for Lean\". Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb7765b5-bef0-421b-be69-6919d24ff14d",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gpba9fB9CVPhokRxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efeaf0e4-1f25-4daa-b769-3f6355f41025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmtnxXXzMAjGHD5h6mV6qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 9 · 2026-05-28T14:48:15.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PwwpgD7AR6KGgUNtYb1yHq`</summary>

```json
{
  "query": "LeanPremise LeanHammer arXiv 2506.07477 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efeaf0e4-1f25-4daa-b769-3f6355f41025",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gpba9fB9CVPhokRxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a90eb48-bc75-4488-876a-ccfe258a785a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmtnxXXzMAjGHD5h6mV6qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 10 · 2026-05-28T14:48:15.948Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013a6wPA3U6Db24yyz1F41KM`</summary>

```json
{
  "query": "\"premise selection\" \"lean hammer\" ICLR 2026 neural premise selector"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a90eb48-bc75-4488-876a-ccfe258a785a",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9gpba9fB9CVPhokRxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1cc234f-5fb0-48a4-bbb0-bca69b71e96b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmtnxXXzMAjGHD5h6mV6qe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8983,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 8983,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1117,
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

_source line 11 · 2026-05-28T14:48:19.138Z_

<details><summary>↩ Tool result · `toolu_01PHJVmSdWJHxKdBssNdDUge`</summary>

```text
# Paper Details: Premise Selection for a Lean Hammer

**Title:** "Premise Selection for a Lean Hammer"

**Authors:** Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Qiaochu Jiang, Sean Welleck

**arXiv Identifier:** 2506.07477

**Submission Date:** June 9, 2025 (v1); revised February 25, 2026 (v2)

**Subject Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Logic in Computer Science (cs.LO)

## Abstract Summary

The paper presents LeanPremise, a neural premise selection system combined with LeanHammer, described as "the first end-to-end domain general hammer for the Lean proof assistant." The system integrates premise selection, translation to external theorem provers, and proof reconstruction.

## Key Result

The paper reports that "LeanPremise enables LeanHammer to solve 21% more goals than existing" alternative systems and generalizes across diverse domains.

## Availability

Code repositories are provided for both LeanPremise and LeanHammer on GitHub.

**Note:** The provided webpage does not contain detailed benchmark names (miniCTX-v2), model parameters (82M), or project-level results (Carleson, Foundation, ConNF, FLT) mentioned in your query. These specifics would require access to the full PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efeaf0e4-1f25-4daa-b769-3f6355f41025",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "053773ba-b68d-4c9e-9d27-54895e63362c",
  "sourceToolAssistantUUID": "efeaf0e4-1f25-4daa-b769-3f6355f41025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T14:48:22.020Z_

<details><summary>↩ Tool result · `toolu_013a6wPA3U6Db24yyz1F41KM`</summary>

```text
Web search results for query: ""premise selection" "lean hammer" ICLR 2026 neural premise selector"

Links: [{"title":"Premise Selection for a Lean Hammer [Quick Review]","url":"https://liner.com/review/premise-selection-for-a-lean-hammer"},{"title":"PREMISE SELECTION FOR A LEAN HAMMER","url":"https://openreview.net/pdf/d5e22b3ba61c4293d448955bf429dfd690a44e6c.pdf"},{"title":"Premise Selection for a Lean Hammer","url":"https://arxiv.org/pdf/2506.07477"},{"title":"Premise Selection for a Lean Hammer","url":"https://www.catalyzex.com/paper/premise-selection-for-a-lean-hammer"},{"title":"Premise Selection for a Lean Hammer","url":"https://arxiv.org/html/2506.07477v1"},{"title":"Premise Selection for a Lean Hammer | OpenReview","url":"https://openreview.net/forum?id=m04JJNeRK6"},{"title":"Premise Selection for a Lean Hammer | Request PDF","url":"https://www.researchgate.net/publication/392531565_Premise_Selection_for_a_Lean_Hammer"}]

Based on the search results, here's what I found:

The paper presents LeanPremise, a novel neural premise selection system, and combines it with existing translation and proof reconstruction components to create LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant.

LeanPremise is specifically trained for use with a hammer in dependent type theory. The research includes new hammer-aware data extraction techniques, and an important feature of LeanPremise is that it dynamically augments the library of facts with locally defined facts from the user's project, which is essential in practice.

The results are impressive: LeanHammer, particularly with the large model in the cumulative setting, significantly outperforms existing premise selectors on Mathlib theorems, achieving a 33.3% proof rate, which is a substantial improvement over MePo's 27.5% and ReProver's 22.3%.

The paper is under review at ICLR as of April 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1cc234f-5fb0-48a4-bbb0-bca69b71e96b",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "0199ca2f-e394-493e-b65c-3d93d24e2d15",
  "sourceToolAssistantUUID": "d1cc234f-5fb0-48a4-bbb0-bca69b71e96b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T14:48:22.694Z_

<details><summary>↩ Tool result · `toolu_01PwwpgD7AR6KGgUNtYb1yHq`</summary>

```text
Web search results for query: "LeanPremise LeanHammer arXiv 2506.07477 ICLR 2026"

Links: [{"title":"[2506.07477] Premise Selection for a Lean Hammer","url":"https://arxiv.org/abs/2506.07477"},{"title":"Premise Selection for a Lean Hammer [Quick Review]","url":"https://liner.com/review/premise-selection-for-a-lean-hammer"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf"},{"title":"LeanHammer","url":"https://cmu-l3.github.io/lean-hammer/"},{"title":"Premise Selection for a Lean Hammer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250607477Z/abstract"},{"title":"arXiv:2506.07477v1 [cs.LG] 9 Jun 2025 Preprint. Under review.","url":"https://arxiv.org/pdf/2506.07477"},{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137v2"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.22554"}]

Based on the search results, here's what I found about this paper:

LeanPremise is a novel neural premise selection system that, when combined with existing translation and proof reconstruction components, creates LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant.

A hammer is a tool that integrates premise selection, translation to external automatic theorem provers, and proof reconstruction into one overarching tool to automate tedious reasoning steps.

Key features of the work include:

- LeanPremise is specifically trained for use with a hammer in dependent type theory and dynamically adapts to user-specific contexts, enabling it to recommend premises from libraries outside its training data as well as lemmas defined by the user locally.

- LeanPremise enables LeanHammer to solve 21% more goals than existing premise selectors and generalizes well to diverse domains.

- LeanHammer is callable as a tactic in Lean, and the premise selector runs on an external server with low computational cost and latency.

This is an ICLR 2026 paper, and the authors are Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Q. Jiang, and Sean Welleck.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a90eb48-bc75-4488-876a-ccfe258a785a",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "8b80e757-2a65-45be-96af-1b9a81361db9",
  "sourceToolAssistantUUID": "4a90eb48-bc75-4488-876a-ccfe258a785a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T14:48:26.974Z_

Good, I have initial results. Let me now fetch the full PDF and the OpenReview page to get the specific numerical claims (miniCTX-v2 results, 82M parameter count, project-level variation).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b80e757-2a65-45be-96af-1b9a81361db9",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9hvucXryQXc3CiGYs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dd14e41-b335-4236-972c-602ebe7b9cae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5M94Eoo9MyAvZNW6KmAeK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 589,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 10100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
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

_source line 15 · 2026-05-28T14:48:28.862Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BmTKtmADBPNZE4UXwDqurJ`</summary>

```json
{
  "url": "https://openreview.net/forum?id=m04JJNeRK6",
  "prompt": "Extract all details about this paper submission: Is it accepted at ICLR 2026 or still under review? What is the decision status? Extract any reviewer scores, acceptance decisions, or venue information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dd14e41-b335-4236-972c-602ebe7b9cae",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9hvucXryQXc3CiGYs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8a8639a-463c-4406-9a62-62a7c081d4a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5M94Eoo9MyAvZNW6KmAeK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 589,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 10100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
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

_source line 16 · 2026-05-28T14:48:33.684Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016iE1ZPjijUADp8uhkstSt1`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.07477v1",
  "prompt": "Extract ALL specific numerical results from this paper. I need: 1) Any mention of 79.4% or relative proof rate on OOD benchmarks or miniCTX-v2. 2) Any mention of 82M parameters for the neural premise selector. 3) Project-level results for Carleson, Foundation, ConNF, FLT - what are the exact percentages? 4) The exact phrasing about \"first end-to-end domain-general hammer for Lean\". 5) Any other key numerical results, benchmark names, and model sizes. Be exhaustive and quote exact numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a8639a-463c-4406-9a62-62a7c081d4a1",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9hvucXryQXc3CiGYs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70af2fad-124f-4619-b7d1-4d841d9c5e79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5M94Eoo9MyAvZNW6KmAeK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 589,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 10100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1358,
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

_source line 17 · 2026-05-28T14:48:36.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wx8zGXmqpxshsdRrKpZZoF`</summary>

```json
{
  "url": "https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf",
  "prompt": "Extract ALL specific numerical results. I need: 1) Any mention of 79.4% or relative proof rate on OOD or miniCTX-v2. 2) The exact parameter count of the neural premise selector (82M or otherwise). 3) Project-level breakdown for Carleson, Foundation, ConNF, FLT with exact percentages. 4) All benchmark results and model sizes mentioned. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70af2fad-124f-4619-b7d1-4d841d9c5e79",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9hvucXryQXc3CiGYs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae6633ec-8165-4551-b4e9-533a02494e4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5M94Eoo9MyAvZNW6KmAeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 589,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 10100,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1358
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 589,
          "output_tokens": 561,
          "cache_read_input_tokens": 10100,
          "cache_creation_input_tokens": 1358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1358,
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

_source line 18 · 2026-05-28T14:48:41.585Z_

<details><summary>↩ Tool result · `toolu_01Wx8zGXmqpxshsdRrKpZZoF`</summary>

```text
I appreciate your request, but I need to be direct: the content you've provided appears to be a PDF file encoded in binary/compressed format (indicated by the `%PDF-1.5` header and FlateDecode compression streams). This is not readable text content—it's the raw PDF structure itself.

To extract the specific numerical results you're seeking (79.4% proof rates, 82M parameter counts, project-level breakdowns for Carleson/Foundation/ConNF/FLT, and benchmark results), I would need:

1. **The decoded/rendered text** of the actual PDF document, or
2. **A plain text version** of the paper/document

**What I cannot do:**
- Decode compressed PDF streams to extract the underlying text
- Interpret binary PDF structures as readable content

**Recommendation:**
Please provide either:
- The extracted text from the PDF (copy-paste from a PDF reader)
- A plaintext or markdown version of the document
- The document name/DOI so context is clear

Once you provide readable text, I'll extract all numerical results within your specified constraints.

[Binary content (application/pdf, 362.8KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/805a9b1b-751a-472f-be96-3da9ad6bf0e5/tool-results/webfetch-1779979716932-5nqrbh.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae6633ec-8165-4551-b4e9-533a02494e4c",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "5940f4f2-69db-47a3-a41f-692364a88e5c",
  "sourceToolAssistantUUID": "ae6633ec-8165-4551-b4e9-533a02494e4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T14:48:41.591Z_

<details><summary>↩ Tool result · `toolu_016iE1ZPjijUADp8uhkstSt1`</summary>

```text
# Numerical Results from "Premise Selection for a Lean Hammer"

## Key Model Specifications
- **Largest neural model**: "82M" parameters (large model configuration)
- **Model sizes tested**: Small (23M), Medium (33M), Large (82M)

## Primary Benchmark Results (Mathlib-test)

**Recall metrics** with large model:
- "63.5%" recall@16
- "72.7%" recall@32

**Proof rates** with large model:
- Aesop: 24.1%
- Auto: 21.3%
- Aesop+auto: 28.5%
- Full: 30.1%
- Cumulative: 33.3%

## Out-of-Distribution Performance (miniCTX-v2)

**Large model proof rate using full setting**: "20.7%"

**Relative performance ratio**: The paper states "the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and 79.4% on miniCTX with the full pipeline"

## Project-Level Results (miniCTX-v2-test, full setting)
- **Carleson**: 0.0%
- **ConNF**: 16.0%
- **FLT**: 36.4%
- **Foundation**: 38.0%
- **HepLean**: 10.0%
- **Seymour**: 24.0%
- **Average**: 20.7%

## Core Contribution Language
The paper describes LeanHammer as "the first end-to-end domain-general hammer for Lean"

## Additional Key Results
- Comparison to ReProver: LeanHammer proves "150% more theorems" in full setting, "50% more" in cumulative setting
- Comparison to MePo: 73% higher recall@32, 21% higher cumulative proof rate
- **Training data**: 469,965 states from 206,005 theorem proofs; 265,348 filtered premises
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70af2fad-124f-4619-b7d1-4d841d9c5e79",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "4b877349-7a08-4b5b-8c44-9f9ad900f2f9",
  "sourceToolAssistantUUID": "70af2fad-124f-4619-b7d1-4d841d9c5e79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T14:49:02.804Z_

<details><summary>↩ Tool result · `toolu_01BmTKtmADBPNZE4UXwDqurJ`</summary>

```text
# Paper Submission Status

Based on the webpage content provided, here are the key details:

**Acceptance Status:** The paper has been **accepted** to ICLR 2026 as an oral presentation.

**Paper Details:**
- **Title:** "Premise Selection for a Lean Hammer"
- **Authors:** Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Q. Jiang, Sean Welleck
- **Publication Date:** January 26, 2026
- **Last Modified:** April 11, 2026
- **Presentation Type:** "ICLR 2026 Oral"

**Key Information:**
The document explicitly states this is an "ICLR 2026 Oral" submission, confirming acceptance. The page shows "Revisions" and "BibTeX" options, typical of accepted papers in the review system.

**Venue Information:**
This is presented at ICLR 2026 Conference, published on OpenReview.net under a Creative Commons Attribution 4.0 International license.

**Note:** The webpage does not display individual reviewer scores or detailed review comments in the content provided, though such information may exist in other sections of the full OpenReview page not included in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8a8639a-463c-4406-9a62-62a7c081d4a1",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "5bd585f0-c3e7-4cc5-a851-cce675a747db",
  "sourceToolAssistantUUID": "d8a8639a-463c-4406-9a62-62a7c081d4a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-28T14:49:06.330Z_

I now have comprehensive information from the arxiv HTML version and OpenReview. Let me also check the v2 revision for any updated numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd585f0-c3e7-4cc5-a851-cce675a747db",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9ktNPsem7zYS1hEwqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b0538b2-dfeb-4ccc-b84c-7664cee16e1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENn7x3Sc6gtg3Tf5DFDX55",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 888,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 11458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1561,
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

_source line 22 · 2026-05-28T14:49:08.972Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FdQ5XhuDE3sJ9MsjH7BGWh`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.07477v2",
  "prompt": "Extract ALL specific numerical results. Focus on: 1) Any changes from v1 - proof rates, parameter counts, project-level results. 2) The exact 79.4% claim and its context. 3) Project-level results for Carleson, Foundation, ConNF, FLT. 4) Model parameter sizes. 5) miniCTX-v2 results. Quote exact numbers and their context."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b0538b2-dfeb-4ccc-b84c-7664cee16e1b",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9ktNPsem7zYS1hEwqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfbaa857-8a38-4edf-89a0-cd3f00beaeab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENn7x3Sc6gtg3Tf5DFDX55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 888,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 11458,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 888,
          "output_tokens": 208,
          "cache_read_input_tokens": 11458,
          "cache_creation_input_tokens": 1561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1561,
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

_source line 23 · 2026-05-28T14:49:16.290Z_

<details><summary>↩ Tool result · `toolu_01FdQ5XhuDE3sJ9MsjH7BGWh`</summary>

```text
# Key Numerical Results from LeanHammer Paper

## Proof Rates & Performance

**Mathlib-test Results (Table 2):**
- LeanHammer (large model) achieves 30.1% proof rate in "full" setting
- 33.3% with "cumul" (accumulation across variants)
- 37.3% when accumulated across all model sizes
- Ground truth baseline: 43.0%

**Comparison Claims:**
The paper states that LeanHammer "solves 21% more goals" compared to existing premise selectors, and proves "150% more theorems" versus ReProver in the full setting.

## Out-of-Distribution Generalization

**miniCTX-v2 Results (Table 3):**
- LeanHammer (large model): 20.7% proof rate
- Ground truth: 26.1%
- The 79.4% figure appears in this context: "the proportion of theorems proven...out of theorems proven with the ground-truth premises...is 73.5% on Mathlib and 79.4% on miniCTX with the full pipeline"

**Project-Level Performance:**
- Carleson: 0.0%
- ConNF: 16.0%
- FLT: 36.4%
- Foundation: 38.0%
- HepLean: 10.0%
- Seymour: 24.0%

## Model Sizes

- Small: 23M parameters
- Medium: 33M parameters
- Large: 82M parameters
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfbaa857-8a38-4edf-89a0-cd3f00beaeab",
  "isSidechain": true,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "agentId": "aa85e714bc0c4243e",
  "type": "user",
  "uuid": "cd8a0cb1-f3b7-471d-92c8-d14b5842749b",
  "sourceToolAssistantUUID": "dfbaa857-8a38-4edf-89a0-cd3f00beaeab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T14:49:37.697Z_

I now have all the information needed to provide a thorough verification. Here is my report:

---

## Verification of Claims about LeanPremise/LeanHammer (arXiv 2506.07477)

### Paper Basics
- **Title:** "Premise Selection for a Lean Hammer"
- **Authors:** Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Q. Jiang, Sean Welleck
- **arXiv:** 2506.07477 (v1: June 9, 2025; v2: February 25, 2026)

---

### Claim 1: "Accepted at ICLR 2026"
**CONFIRMED.** The OpenReview page ([link](https://openreview.net/forum?id=m04JJNeRK6)) shows the paper was accepted as an **ICLR 2026 Oral** presentation. The search results also surfaced a direct link titled "Published as a conference paper at ICLR 2026."

---

### Claim 2: "79.4% relative proof rate on OOD benchmarks (miniCTX-v2)"
**CONFIRMED, but requires careful interpretation.** The paper states: "the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and **79.4% on miniCTX** with the full pipeline." This 79.4% is a **relative** proof rate -- it is the ratio of theorems proven by LeanHammer to theorems proven with oracle/ground-truth premises. The **absolute** proof rate on miniCTX-v2 is 20.7% (vs. 26.1% ground truth). So the claim is accurate as stated ("relative proof rate").

---

### Claim 3: "Project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%"
**CONFIRMED.** The miniCTX-v2 project-level breakdown (full setting, large model) is:
- **Carleson: 0.0%**
- **ConNF: 16.0%**
- **FLT: 36.4%**
- **Foundation: 38.0%**
- HepLean: 10.0%
- Seymour: 24.0%
- Average: 20.7%

All four claimed numbers match exactly.

---

### Claim 4: "First end-to-end domain-general hammer for Lean"
**CONFIRMED.** The paper explicitly describes LeanHammer as "the first end-to-end domain-general hammer for Lean" (or equivalently, "the first end-to-end domain general hammer for the Lean proof assistant").

---

### Claim 5: "82M-parameter neural premise selector"
**CONFIRMED.** The paper tests three model sizes: Small (23M), Medium (33M), and **Large (82M)** parameters. The flagship results use the 82M large model.

---

### Summary

All five claims are **verified as accurate** based on the paper content. No discrepancies were found. The only nuance worth noting is that the 79.4% figure is explicitly a *relative* proof rate (ratio to ground-truth performance), not an absolute proof rate -- and the claim as stated correctly uses the word "relative," so it is faithful to the paper.

Sources:
- [arXiv page: 2506.07477](https://arxiv.org/abs/2506.07477)
- [Full HTML paper (v1)](https://arxiv.org/html/2506.07477v1)
- [OpenReview forum](https://openreview.net/forum?id=m04JJNeRK6)
- [OpenReview PDF](https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf)
- [LeanHammer project page](https://cmu-l3.github.io/lean-hammer/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd8a0cb1-f3b7-471d-92c8-d14b5842749b",
  "isSidechain": true,
  "agentId": "aa85e714bc0c4243e",
  "requestId": "req_011CbV9mt459FQZ8Hku9cY41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72100067-76df-4caf-9d93-fee175837321",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmL2W9LjvFN23vhdAMHc4N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 13019,
      "output_tokens": 983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 983,
          "cache_read_input_tokens": 13019,
          "cache_creation_input_tokens": 1470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1470,
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
