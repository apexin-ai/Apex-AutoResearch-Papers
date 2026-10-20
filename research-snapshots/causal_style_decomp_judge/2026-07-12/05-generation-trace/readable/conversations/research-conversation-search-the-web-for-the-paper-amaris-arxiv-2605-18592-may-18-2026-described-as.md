# Research conversation: Search the web for the paper "AMARIS" (arXiv:2605.18592, May 18, 2026) — described as a "Memory-Augmented Rubric Improve

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8291f41460c22049.jsonl`
- **Structured JSON:** [`5288392011f842d65dbc.json`](../../sessions/52/5288392011f842d65dbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-28T13:35:58.151Z_

Search the web for the paper "AMARIS" (arXiv:2605.18592, May 18, 2026) — described as a "Memory-Augmented Rubric Improvement System" that grounds rubric modifications in long-term training history. I need to understand:
1. What exactly does AMARIS do?
2. How does it modify rubrics during training?
3. Does it have any difficulty-awareness component?
4. What domains does it operate in?
5. How does it relate to reward hacking / gaming detection?

Search using multiple queries:
- "AMARIS Memory-Augmented Rubric Improvement System arXiv 2605.18592"
- "AMARIS rubric RL training history 2026"
- "memory augmented rubric improvement reinforcement learning"

Try to fetch the actual paper from arxiv.org/abs/2605.18592 if possible. Give me a detailed summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "cd80a2c3-8ab2-498c-85b7-7777239dcaa0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T13:35:58.155Z_

```json
{
  "parentUuid": "cd80a2c3-8ab2-498c-85b7-7777239dcaa0",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
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
  "uuid": "595a033e-9128-49a6-a094-d774af4f8f33",
  "timestamp": "2026-05-28T13:35:58.155Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T13:35:58.156Z_

```json
{
  "parentUuid": "595a033e-9128-49a6-a094-d774af4f8f33",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0dbe424a-249e-474e-b03d-5ffc20e88cd6",
  "timestamp": "2026-05-28T13:35:58.156Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T13:36:00.246Z_



I'll search for this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbe424a-249e-474e-b03d-5ffc20e88cd6",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4Bg4E6ZgAZgsJMkAer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0007973-fa5a-4e0b-83f8-da54b45d611f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUYpqAkT8N9wZBAe6tFvzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8965,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8965,
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

_source line 5 · 2026-05-28T13:36:00.806Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DgrZ7WqT74LkjEPcV1SyJr`</summary>

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
  "parentUuid": "f0007973-fa5a-4e0b-83f8-da54b45d611f",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4Bg4E6ZgAZgsJMkAer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc50090-f727-4469-8f2b-cfe31a4cb4f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUYpqAkT8N9wZBAe6tFvzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8965,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8965,
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

_source line 6 · 2026-05-28T13:36:00.811Z_

<details><summary>↩ Tool result · `toolu_01DgrZ7WqT74LkjEPcV1SyJr`</summary>

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
  "parentUuid": "ebc50090-f727-4469-8f2b-cfe31a4cb4f8",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "6f545f5e-23fe-465c-be9e-c5ffef050ed9",
  "sourceToolAssistantUUID": "ebc50090-f727-4469-8f2b-cfe31a4cb4f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T13:36:03.141Z_



Now let me run all the searches and the direct arXiv fetch in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f545f5e-23fe-465c-be9e-c5ffef050ed9",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4BsiTCaTcZ3pngWPZP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ceb513-36d9-494f-84ed-f6a4619be771",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeKyzcfNC6A16NxrPuK7qx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 8 · 2026-05-28T13:36:04.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKG4LngkirqJKzu1RvXShK`</summary>

```json
{
  "query": "AMARIS Memory-Augmented Rubric Improvement System arXiv 2605.18592"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ceb513-36d9-494f-84ed-f6a4619be771",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4BsiTCaTcZ3pngWPZP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "477d8615-c4f3-4648-adab-5d6e09fd013c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeKyzcfNC6A16NxrPuK7qx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 9 · 2026-05-28T13:36:04.560Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mTVu1yci1bfCPgXxYEnpw`</summary>

```json
{
  "query": "AMARIS rubric RL training history 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "477d8615-c4f3-4648-adab-5d6e09fd013c",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4BsiTCaTcZ3pngWPZP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28a22fc3-67a2-4449-80d3-a7d57fbbdac1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeKyzcfNC6A16NxrPuK7qx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 10 · 2026-05-28T13:36:05.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016tdxsWfa2Stdrj5rzr1e6m`</summary>

```json
{
  "query": "memory augmented rubric improvement reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a22fc3-67a2-4449-80d3-a7d57fbbdac1",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4BsiTCaTcZ3pngWPZP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "390db794-b7b2-4be5-bdda-8466633f44bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeKyzcfNC6A16NxrPuK7qx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 11 · 2026-05-28T13:36:07.417Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RC7DJXop8XaAFN9uWuKL2J`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.18592",
  "prompt": "Extract the full abstract, author list, title, and all details about what AMARIS does, how it modifies rubrics, its difficulty-awareness component, the domains it operates in, and how it relates to reward hacking or gaming detection. Include any methodological details, experimental results, and key contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "390db794-b7b2-4be5-bdda-8466633f44bb",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4BsiTCaTcZ3pngWPZP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aff67c7-07fe-4310-9c81-f617443d08b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeKyzcfNC6A16NxrPuK7qx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8965,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 8965,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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

_source line 12 · 2026-05-28T13:36:11.689Z_

<details><summary>↩ Tool result · `toolu_01AKG4LngkirqJKzu1RvXShK`</summary>

```text
Web search results for query: "AMARIS Memory-Augmented Rubric Improvement System arXiv 2605.18592"

Links: [{"title":"[2605.18592] AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/abs/2605.18592"},{"title":"AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.18592v1"},{"title":"Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks","url":"https://arxiv.org/pdf/2602.05125"},{"title":"SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing","url":"https://arxiv.org/pdf/2602.20751"},{"title":"RubricRAG: Towards Interpretable and Reliable LLM Evaluation via Domain Knowledge Retrieval for Rubric Generation","url":"https://arxiv.org/pdf/2603.20882"},{"title":"[2601.05960] Distilling Feedback into Memory-as-a-Tool","url":"https://arxiv.org/abs/2601.05960"},{"title":"[2605.10899] RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards","url":"https://arxiv.org/abs/2605.10899"}]

I found the paper you're looking for. Here's what I discovered:

AMARIS: A Memory-Augmented Rubric Improvement System is a paper submitted on May 18, 2026, by Peilin Wu and 6 other authors that addresses rubric-based reward shaping as an effective method for fine-tuning LLMs via reinforcement learning.

The key problem AMARIS addresses is that existing methods discard the diagnostics produced during evaluation after immediate use and prevent the long-term accumulation and strategic reuse of evaluation knowledge.

Experiments across both closed and open-ended domains show that AMARIS consistently outperforms the baselines. Ablation studies demonstrate that both static and dynamic memory retrieval contribute to performance gains, with their combination providing the strongest results at moderate retrieval budgets.

The paper is available on arXiv at https://arxiv.org/abs/2605.18592.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "477d8615-c4f3-4648-adab-5d6e09fd013c",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "b9bdfd94-890a-48d5-8451-5dbf64b047ca",
  "sourceToolAssistantUUID": "477d8615-c4f3-4648-adab-5d6e09fd013c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T13:36:12.373Z_

<details><summary>↩ Tool result · `toolu_018mTVu1yci1bfCPgXxYEnpw`</summary>

```text
Web search results for query: "AMARIS rubric RL training history 2026"

Links: [{"title":"[2605.18592] AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/abs/2605.18592"},{"title":"AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.18592"},{"title":"Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains | OpenReview","url":"https://openreview.net/forum?id=c1bTcrDmt4"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"How Top AI Labs Are Building RL Agents in 2026","url":"https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"},{"title":"Alternating Reinforcement Learning for Rubric-Based ...","url":"https://arxiv.org/pdf/2602.01511"},{"title":"RL Training Environments: Methods & Scalability","url":"https://www.emergentmind.com/topics/rl-training-environment"},{"title":"Paper page - Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://huggingface.co/papers/2602.01511"},{"title":"[2602.01511] Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://arxiv.org/abs/2602.01511"},{"title":"ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning","url":"https://arxiv.org/html/2605.23454"}]

Based on the search results, I found information about AMARIS and its application to rubric-based RL training with training history tracking.

## AMARIS: A Memory-Augmented Rubric Improvement System

AMARIS grounds rubric modifications in long-term training history. The system addresses a key limitation in existing rubric-based reinforcement learning approaches.

### How AMARIS Works

At each training step, AMARIS analyzes individual rollouts, aggregates findings into step-level summaries, retrieves relevant historical context from a persistent evaluation memory through both static (recent steps) and dynamic (semantically matched) retrieval, and updates rubrics based on these accumulated analyses. This procedure runs asynchronously alongside the normal RL loop with minimal overhead.

### Key Problem It Solves

Previous methods discard the diagnostics produced during evaluation after immediate use and prevent the long-term accumulation and strategic reuse of evaluation knowledge. This forces the system to re-derive evaluation principles from scratch, limits its ability to detect recurring suboptimal behaviors, and forfeits the curriculum-like progression that a persistent training history would naturally support.

### Performance Results

Experiments across both closed and open-ended domains show that AMARIS consistently outperforms the baselines. Ablation studies show that static and dynamic memory retrieval contributes to the performance gain and their combination provides the strongest results with moderate retrieval budgets sufficient to provide most of the gain, and that the entire pipeline adds only ~5% time overhead through asynchronous execution.

The paper appears to have been published recently (approximately 2 weeks ago as of May 2026) on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a22fc3-67a2-4449-80d3-a7d57fbbdac1",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "6f2e35f2-33c7-462f-b088-b3efbb222f90",
  "sourceToolAssistantUUID": "28a22fc3-67a2-4449-80d3-a7d57fbbdac1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T13:36:13.142Z_

<details><summary>↩ Tool result · `toolu_016tdxsWfa2Stdrj5rzr1e6m`</summary>

```text
Web search results for query: "memory augmented rubric improvement reinforcement learning 2026"

Links: [{"title":"[2605.18592] AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/abs/2605.18592"},{"title":"AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.18592"},{"title":"MEM-$\\alpha$: LEARNING MEMORY CONSTRUCTION VIA REINFORCEMENT LEARNING | OpenReview","url":"https://openreview.net/forum?id=dm42omwep1"},{"title":"Augmented Replay Memory in Reinforcement Learning With Continuous   Control","url":"https://arxiv.org/pdf/1912.12719"},{"title":"GitHub - aiming-lab/SkillRL: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning · GitHub","url":"https://github.com/aiming-lab/SkillRL"},{"title":"Reinforcement Learning with Rubric Anchors","url":"https://arxiv.org/pdf/2508.12790"}]

Based on the search results, I found highly relevant research on this topic:

## Key Finding: AMARIS Paper

A recent paper submitted on May 18, 2026, titled "AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning" by Peilin Wu and colleagues addresses the intersection of memory augmentation, rubric improvement, and reinforcement learning.

The paper focuses on rubric-based reward shaping as an effective method for fine-tuning large language models via RL, where structured rubrics decompose standard outcome rewards into multiple dimensions to provide richer reward signals.

## The Problem Being Addressed

The research identifies that existing methods discard the diagnostics produced during evaluation after immediate use and prevent the long-term accumulation and strategic reuse of evaluation knowledge.

## The AMARIS Solution

AMARIS combines memory augmentation with rubric improvement by using persistent evaluation memory to ground rubric updates in accumulated rollout diagnostics, summaries, and prior updates. This addresses limitations of methods that adapt rubrics based only on recent or local signals, without grounding the updates using rich information from long-term training dynamics.

The search also revealed other related 2026 research in memory-augmented reinforcement learning, including work on memory construction and skill-augmented RL approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "390db794-b7b2-4be5-bdda-8466633f44bb",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "eff4dd15-d964-40ef-9980-7c2b8936d362",
  "sourceToolAssistantUUID": "390db794-b7b2-4be5-bdda-8466633f44bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T13:36:14.519Z_

<details><summary>↩ Tool result · `toolu_01RC7DJXop8XaAFN9uWuKL2J`</summary>

```text
# AMARIS: Memory-Augmented Rubric Improvement System

## Title and Authors
**Title:** AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning

**Authors:** Peilin Wu, Xinlu Zhang, Kun Wan, Wentian Zhao, Gang Wu, Xinya Du, Zhiyu Chen

## Core Abstract
The system addresses a key limitation in adaptive rubric methods: they typically rely on "local evidence such as the current batch or instance-level comparisons," discarding diagnostic information from training history. AMARIS counters this by grounding rubric updates in "longitudinal training evidence."

## How AMARIS Modifies Rubrics

The system employs a memory-augmented approach:
- **Storage:** Maintains a persistent evaluation memory containing rollout analyses, step-level summaries, and prior rubric update records
- **Retrieval:** Accesses recent and semantically relevant historical information to inform revisions
- **Execution:** Operates asynchronously alongside the RL loop, reducing latency from synchronous updates

## Difficulty Progression Component
The research indicates that memory "supports a progression from early failure correction to later curriculum advancement," suggesting the system adapts rubric difficulty standards as models improve and earlier criteria become saturated.

## Experimental Domains
AMARIS was evaluated across four distinct areas:
- Science (GPQA-Diamond: +2.8 point improvement)
- Medicine
- Instruction following (IFBench: +2.2 point improvement)
- Creative writing

Both global and instance-specific rubric settings were tested.

## Key Benefits
- Reduces oscillatory rubric edits through memory-informed decision-making
- Outperforms static baselines and local-adaptive competitors
- Tracks recurring failures systematically across training
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aff67c7-07fe-4310-9c81-f617443d08b4",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "175a9cfe-a69e-4f33-9e96-87fcba52e7d9",
  "sourceToolAssistantUUID": "9aff67c7-07fe-4310-9c81-f617443d08b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-28T13:36:16.610Z_

Good, I have substantial information. Let me now fetch the full HTML version of the paper for more detailed content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "175a9cfe-a69e-4f33-9e96-87fcba52e7d9",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4Ct25uSa14NEmYLmdE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4baffd1a-083a-473d-8909-fd7c34bd65e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ce67bbGzwkAdVJno4xjn3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 10080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
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

_source line 17 · 2026-05-28T13:36:20.766Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KMX2BbZ9NKvah6Rx2myHaQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.18592v1",
  "prompt": "Extract ALL details from this paper including: (1) the full abstract, (2) the complete methodology of how AMARIS works step by step, (3) the memory architecture (static vs dynamic retrieval), (4) how rubrics are modified at each step, (5) any difficulty-awareness or curriculum-like progression component, (6) how it relates to reward hacking or gaming detection, (7) all experimental domains and results with numbers, (8) ablation study results, (9) key contributions listed by the authors, (10) the RL algorithms used (GRPO etc.), (11) overhead analysis, and (12) any baselines compared against. Be as detailed and comprehensive as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4baffd1a-083a-473d-8909-fd7c34bd65e0",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4Ct25uSa14NEmYLmdE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "733d4ee2-5b1f-4bd1-b5e0-0cd1edcdbada",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ce67bbGzwkAdVJno4xjn3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 10080,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 10080,
          "cache_creation_input_tokens": 2932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2932,
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

_source line 18 · 2026-05-28T13:37:09.305Z_

<details><summary>↩ Tool result · `toolu_01KMX2BbZ9NKvah6Rx2myHaQ`</summary>

```text
# AMARIS: Memory-Augmented Rubric Improvement System - Comprehensive Overview

## 1. ABSTRACT

AMARIS proposes a system that uses persistent evaluation memory to improve rubric-based reinforcement learning for LLMs. Rather than adapting rubrics based solely on current step signals, the system grounds modifications in long-term training history through stored rollout analyses, step summaries, and update records. Testing across science, medicine, instruction following, and creative writing shows consistent improvements: "+1.6 points on GPQA-Diamond and +1.0 points on HealthBench over strongest baselines" with only "~5% time overhead through asynchronous execution."

## 2. COMPLETE METHODOLOGY - STEP-BY-STEP WORKFLOW

### Stage 1: Individual Rollout Analysis
For each rollout, AMARIS generates a structured diagnostic report analyzing:
- **Reward hacking detection**: Whether outputs show gaming behaviors (over-refusal, sycophancy) with confidence levels
- **Training-stage assessment**: Performance appropriateness for current model size and training step
- **Rubric analysis**: How current rubrics shaped observed behavior and specific weighting flaws
- **Curriculum advancement**: Which capabilities should advance next toward high-level goals
- **Additional observations**: Other noteworthy signals for later analysis

The analysis function: "a=A_ψ(x,y,G_t,z)" where A_ψ is the LLM analyzer processing input x, output y, active rubric set G_t, and supplemental context z.

### Stage 2: Step-Level Batch Summarization
Individual analyses from a training step aggregate into summaries capturing:
- General training health and current learning phase
- Recurring behavioral patterns across the batch
- Dominant reward hacking risks with evidence
- Weakest performing rubrics
- Signs of task saturation and provisional improvement plans

For large batches, hierarchical "meta-summarization" partitions analyses into chunks, summarizes each independently, then consolidates results: "b_t=C_ψ({B_ψ(c_j)})" where C_ψ handles consolidation.

### Stage 3: Memory-Grounded Rubric Improvement
Before updating, the system retrieves relevant historical context through:

**Static Retrieval**: Most recent N preceding step-level summaries, providing "I_{t,s}={b_j∈M_{t-1}: t-N≤j≤t-1}" to capture short-term temporal patterns.

**Dynamic Retrieval**: Current summary generates targeted search queries "Q_ψ(b_t)" (typically 5-10 queries) that may retrieve individual analyses, prior summaries, or update records from any training point, returning "up to D documents per query" for semantic matching.

The retrieved context "I_t={I_{t,s}, I_{t,d}}" informs rubric updates following three strategies:
- **Defensive**: Reduces suboptimal behaviors using memory to check if issues recurred previously, applying stronger corrections
- **Curriculum advancement**: Raises evaluation standards when current rubrics saturate, verifying model mastery through memory
- **Maintenance**: Makes minor or no changes when unnecessary

Rubric operations include: Create (new rubrics), Update (improve text precision), Delete (remove counterproductive ones), Reweight (shift emphasis), Merge (combine overlapping), Split (decompose into atomics).

### Stage 4: Asynchronous RL Integration
The entire pipeline runs in parallel with standard RL training. "Rollouts are scored immediately using currently active rubric set, while rubric improvement proceeds in background." Once updates complete, new rubrics activate for subsequent steps. This avoids blocking the policy training loop.

## 3. MEMORY ARCHITECTURE

### Persistent Evaluation Memory Structure
Memory accumulates: "M_t=M_{t-1}∪{a_j}∪{B_ψ(c_j)}∪b_t∪u_t"

Components stored:
- Individual rollout analyses (a_j)
- Chunk-level summaries (B_ψ(c))
- Step-level summaries (b_t)
- Rubric update records (u_t) containing: update strategy, consulted history, edit operations, resulting rubrics, and summary for future reference

Each document indexed with metadata: type, training step, timestamp, semantic embedding for retrieval.

### Hybrid Retrieval Strategy

**Static Retrieval**:
- Window size N (default N=4) retrieves preceding step summaries
- Provides temporal continuity for recent learning trajectory
- Prevents oscillatory rubric changes
- Most effective for domains where errors cluster within short periods (science)

**Dynamic Retrieval**:
- Generates complementary queries targeting: dominant failure modes, suspected rubric flaws, possible curriculum objectives, failures from similar past updates
- Uses semantic matching against memory
- Returns documents from any training point
- Effective when suboptimal behaviors recur across distant steps (medicine)

**Retrieval Budget**: "If static window retrieves N summaries, dynamic uses at most q_n queries each returning at most D documents, then |I_t|≤N+n_{q,t}D"

Ablation findings show:
- Static memory alone: +0.9 points on GPQA-D (38.9 vs. 38.0 baseline)
- Dynamic memory alone: +0.6 points on GPQA-D
- Combined: +1.9 points on GPQA-D (39.9 vs. 38.0)
- Retrieval budget N=4, K=10 provides "most gain with moderate retrieval budgets"

## 4. RUBRIC MODIFICATION MECHANISM

The updater "G_{t+1}, u_t = U_ψ(G_t, b_t, I_t)" uses memory-grounded reasoning to select appropriate strategies:

**Modification Logic**:
1. Analyzes current step summary identifying problems
2. Retrieves historical context revealing whether similar issues occurred
3. Checks if previous attempts addressed the problem (and their outcomes)
4. If recurring issue: applies stronger correction than previous attempts
5. If new issue: creates targeted new rubrics or weights
6. Verifies through memory that curriculum progression is appropriate before raising standards
7. Documents reasoning and operations for future reference

**Example Operations** (from case studies):
- Merging overlapping structure rubrics to reduce redundancy
- Precise scalar reweighting for generic-but-correct reasoning
- Detecting reward hacking and adding constraints
- Curriculum advancement via saturation detection when model masters current criteria

## 5. DIFFICULTY-AWARENESS AND CURRICULUM PROGRESSION

The system enables curriculum-like advancement through:

1. **Saturation Detection**: Step summaries flag when "current rubrics appear saturated" and models show task mastery
2. **Memory-Verified Progression**: Before raising standards, retrieves historical analyses confirming the model has mastered prerequisites
3. **Three-Stage Rubric Evolution** (per analysis):
   - Initial phase: Foundation criteria establishment
   - Middle phase: Progressive difficulty increases as model improves
   - Final phase: Standards stabilize at appropriate difficulty

The prompt instructs updaters to check "whether the model has been steadily improving" and whether "performance is expected given the model size at the current training step," enabling informed curriculum decisions rather than reactive adjustments.

## 6. REWARD HACKING AND GAMING DETECTION

**Integrated Monitoring**:
Individual rollout analysis explicitly detects: "Whether the rollout shows signs of reward hacking, such as over-refusal for safety or sycophancy, reported with evidence and confidence level"

**Systematic Approach**:
- Each analysis categorizes reward hacking signals with confidence scores
- Step summaries identify "dominant reward hacking risk and its evidence"
- Memory tracks which hacking behaviors have recurred
- Defensive update strategy strengthens corrections when past attempts proved insufficient
- Dynamic retrieval includes queries targeting "suspected rubric flaws" that enable gaming

**Protective Mechanisms**:
Case studies document "Reward hacking correction" where AMARIS detected and removed problematic rubrics. The ethics statement acknowledges "AMARIS explicitly monitors for reward hacking and suboptimal behaviors as core component of individual rollout analysis."

## 7. EXPERIMENTAL DOMAINS AND DETAILED RESULTS

### Domains and Benchmarks

**Science**:
- Training: RaR-Science (rubric-annotated corpus)
- Evaluation: GPQA-Diamond (graduate-level questions)
- Metric: Average accuracy (%) over 10 measurements

**Medicine**:
- Training: RaR-Medicine
- Evaluation: HealthBench
- Metric: HealthBench composite score

**Instruction Following**:
- Training: OpenRubrics dataset
- Evaluation: IFEval, InfoBench, IFBench
- Metric: Overall accuracy per benchmark

**Creative Writing**:
- Training: RubricHub writing subset
- Evaluation: WritingBench, Creative Writing v3 (EQ-Bench)
- Metric: Overall scores

### Main Results (Table 1)

| Domain | Benchmark | AMARIS Global | AMARIS Per-Instance | Best Baseline | Improvement |
|--------|-----------|----------------|-------------------|---------------|------------|
| Science | GPQA-Diamond | 39.9 | **40.4** | 38.8 | +1.6 |
| Medicine | HealthBench | 33.6 | **34.0** | 33.0 | +1.0 |
| Instruction Following | IFEval | 80.6 | **81.0** | 80.4 | +0.6 |
| Instruction Following | InfoBench | 84.8 | **85.2** | 84.1 | +1.1 |
| Instruction Following | IFBench | 35.2 | **36.0** | 35.0 | +1.0 |
| Creative Writing | WritingBench | 57.9 | 57.3 | 56.9 | +1.0 |
| Creative Writing | CW-v3 | 39.5 | **40.1** | 39.0 | +1.1 |

**Consistent Superiority**: "AMARIS consistently achieves the best performance on all benchmarks under both rubric strategies"

Per-instance rubrics yielded strongest results on six of seven benchmarks, suggesting that instance-specific memory enables more targeted improvements.

## 8. ABLATION STUDY RESULTS

### Memory Configuration (Global Rubrics - Table 2)

**No Memory Baseline**: 38.0 (GPQA-D)

**Static-Only Results**:
- N=2: 38.2 GPQA-D
- N=4: 38.9 GPQA-D (optimal static)
- N=6: 38.8 GPQA-D
- N=8: 38.9 GPQA-D

**Dynamic-Only Results**:
- K=5: 38.4 GPQA-D
- K=10: 38.6 GPQA-D (optimal dynamic)
- K=15: 38.6 GPQA-D (diminishing returns)

**Combined (N=4, K=10)**: 39.9 GPQA-D (+1.9 absolute)

**Domain-Specific Patterns**:
- Science: Static stronger (recent patterns dominant) - 38.9 vs. 38.6
- Medicine: Dynamic stronger (semantic matching across distant steps) - 33.3 vs. 33.1
- Conclusion: "Combined configuration captures both temporal and semantic signals"

### Per-Instance Results (Appendix B.1 - Table 6)

Similar patterns confirmed:
- No memory: 38.4 (GPQA-D)
- Static+Dynamic (N=4, K=10): 40.4 GPQA-D
- Relative trends match global setting

### LLM Choice Influence (Appendix C)

Different LLM allocations tested:
- Scoring/analysis: GPT-OSS-120B (cost-effective for high token volume)
- Remaining stages: GPT-5.1 (higher reasoning capability)
- Analysis shows performance stability across configurations

### Update Scheduling Influence (Appendix D)

Tested different rubric update frequencies and maximum staleness configurations with performance maintained.

## 9. KEY CONTRIBUTIONS (Author-Stated)

1. "Identify persistent evaluation memory as overlooked component in adaptive rubric-based reward modeling, and show that grounding rubric updates in long-term training history is more effective than relying solely on local signals"

2. "Propose AMARIS, system that couples structured rollout analysis, step-level summarization, and hybrid static + dynamic memory retrieval to produce memory-grounded rubric updates with minimal overhead"

3. "Demonstrate through experiments on various domains that AMARIS consistently outperforms baselines, and provide detailed analysis of influence from different memory configurations, underlying LLMs, and rubric evolution"

## 10. RL ALGORITHM AND TRAINING SETUP

**Policy Training**:
- Base model: Qwen2.5-7B-Instruct
- RL algorithm: GRPO (Group-wise Reward Policy Optimization)
- Configuration: "group-wise and batch-wise reward normalization enabled"
- Hardware: "4 NVIDIA A100 80GB GPUs"
- Training duration: "up to 400 steps"
- Checkpointing: "every 50 steps"
- Final checkpoint used for testing "to ensure fair evaluation"

**Reward Computation**:
- Following prior work (RaR, RubricHub): "single LLM call per rollout"
- LLM judges compute scalar rewards based on active rubric set
- Prompts specified in Appendix G (Figures 2-3)

**Batch Configuration**:
- Global rubrics: standard batch sizes
- Per-instance rubrics: "batch size 256, samples per query 4" for increased epoch count and revisit frequency

## 11. OVERHEAD AND EFFICIENCY ANALYSIS

### Component-Level Profiling (Table 3)

| Component | Time | % of Pipeline | Tokens/Step |
|-----------|------|---------------|------------|
| Individual analysis | 426.4s | 63.1% | 2.32M |
| Batch summarization | 192.3s | 28.5% | 246k |
| Query generation | 2.7s | 0.4% | 14.1k |
| Memory retrieval | 23.7s | 3.5% | 0 |
| Rubric update | 30.6s | 4.5% | 110.9k |
| **Total Pipeline** | **675.7s** | **100%** | **2.691M** |

Individual analysis dominates due to processing every rollout.

### Execution Mode Comparison (Table 4)

**Synchronous Mode**:
- Total training time: ~146 hours
- Quality: 40.1 GPQA-D
- Overhead: ~92%
- Marginal advantage: +0.2 points

**Asynchronous Mode** (adopted as default):
- Total training time: ~80 hours
- Quality: 39.9 GPQA-D (virtually identical)
- Overhead: ~5%
- Substantial efficiency gain

"Asynchronous execution therefore provides substantially more favorable trade-off" with "marginal quality differences (≤0.2 across most benchmarks)" but "nearly doubling total training time" for synchronous approach.

**Bottleneck Analysis**: "The entire pipeline adds only ~5% time overhead through asynchronous execution"

Per-instance settings show similar minimal latency since "per-instance setting naturally limits update opportunity but provides abundant time for analysis and rubric update."

## 12. BASELINES COMPARED

### Cross-Domain Baselines (all domains)

1. **Naive (no RL)**: Base model without training
   - GPQA-D: 35.0
   - HealthBench: 22.7

2. **RubricHub (RuRL)**: Large-scale rubric-annotated dataset baseline
   - GPQA-D: 38.8
   - HealthBench: 33.0

3. **RuscaRL**: Rubric-scaffolded RL method
   - GPQA-D: 38.5
   - HealthBench: 32.9

### Science & Medicine Baselines

4. **RaR**: Fixed rubric set throughout training on RaR-Science/RaR-Medicine
   - GPQA-D: 37.6
   - HealthBench: 31.2

### Instruction Following Baselines

5. **OpenRubrics**: DPO via Rubric-RM
   - IFEval: 79.5
   - InfoBench: 83.0
   - IFBench: 33.7

6. **Rubric-ARM**: Alternating RL for rubric-based reward modeling
   - IFEval: 80.4
   - InfoBench: 83.7
   - IFBench: 35.0

7. **RLCF**: Checklist-based alignment
   - IFEval: 78.6
   - InfoBench: 84.1
   - IFBench: 28.2

**Reporting**: Where possible, authors "re-train and re-evaluate using same base model"; otherwise "reference their reported values."

---

## SUMMARY OF NOVELTY

AMARIS's core innovation shifts from reactive, step-local rubric adaptation to evidence-driven evolution grounded in accumulated training history. By coupling structured individual analysis, step-level summarization, and hybrid static+dynamic memory retrieval, the system enables more informed modifications while maintaining practical efficiency through asynchronous execution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "733d4ee2-5b1f-4bd1-b5e0-0cd1edcdbada",
  "isSidechain": true,
  "promptId": "4b5c2c80-bbfb-476a-afa3-a31e21f120aa",
  "agentId": "a8291f41460c22049",
  "type": "user",
  "uuid": "65010f9b-cfd4-4812-afb8-a19f34344463",
  "sourceToolAssistantUUID": "733d4ee2-5b1f-4bd1-b5e0-0cd1edcdbada",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-28T13:37:56.785Z_

Here is a detailed summary of the AMARIS paper.

---

## AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning

**Paper:** arXiv:2605.18592 (May 18, 2026)
**Authors:** Peilin Wu, Xinlu Zhang, Kun Wan, Wentian Zhao, Gang Wu, Xinya Du, Zhiyu Chen

---

### 1. What AMARIS Does

AMARIS addresses a gap in rubric-based reinforcement learning for LLMs. In rubric-based RL, structured rubrics decompose outcome rewards into multiple evaluative dimensions to provide richer reward signals during fine-tuning. The problem is that existing adaptive rubric methods rely only on **local** signals (the current batch or instance-level comparisons) and **discard all diagnostic information** after each step. This prevents long-term accumulation of evaluation knowledge, forces the system to re-derive evaluation principles from scratch, limits detection of recurring suboptimal behaviors, and forfeits curriculum-like progression that a persistent training history would naturally support.

AMARIS solves this by maintaining a **persistent evaluation memory** that stores rollout analyses, step-level summaries, and prior rubric update records. It grounds all rubric modifications in this longitudinal training evidence rather than only local signals.

The system runs **asynchronously** alongside the standard RL loop (GRPO on Qwen2.5-7B-Instruct), adding only approximately 5% time overhead.

---

### 2. How It Modifies Rubrics During Training

The pipeline has four stages:

**Stage 1 -- Individual Rollout Analysis:** For each rollout, an LLM analyzer produces a structured diagnostic report covering: reward hacking detection (with confidence levels), training-stage assessment, rubric analysis (how current rubrics shaped behavior and specific weighting flaws), curriculum advancement recommendations, and additional observations.

**Stage 2 -- Step-Level Batch Summarization:** Individual analyses are aggregated into a step summary capturing general training health, recurring behavioral patterns, dominant reward hacking risks with evidence, weakest-performing rubrics, and signs of task saturation. For large batches, hierarchical meta-summarization is used (partition into chunks, summarize each, then consolidate).

**Stage 3 -- Memory-Grounded Rubric Update:** Before modifying rubrics, the system retrieves historical context through two mechanisms:
- **Static retrieval:** The most recent N step-level summaries (default N=4), providing temporal continuity and preventing oscillatory edits.
- **Dynamic retrieval:** The current summary generates 5-10 targeted search queries that semantically match against the full memory, retrieving documents from any point in training history (up to D documents per query, default K=10 total).

The updater then selects one of three strategies:
- **Defensive:** Corrects suboptimal behaviors, checking memory to see if the issue has recurred and applying stronger corrections than previous attempts if so.
- **Curriculum advancement:** Raises evaluation standards when memory confirms the model has mastered current criteria (saturation detection).
- **Maintenance:** Minor or no changes when the current rubrics are working well.

Available rubric operations include: Create, Update, Delete, Reweight, Merge (combine overlapping rubrics), and Split (decompose into atomic criteria).

**Stage 4 -- Asynchronous Integration:** Rollouts are scored immediately using currently active rubrics while the improvement pipeline runs in the background. New rubrics activate for subsequent steps once ready.

---

### 3. Difficulty-Awareness Component

Yes, AMARIS has an explicit curriculum-like difficulty progression mechanism:

- **Saturation detection:** Step summaries flag when current rubrics appear saturated and the model shows mastery.
- **Memory-verified progression:** Before raising difficulty, the system retrieves historical analyses to confirm the model has been steadily improving and has mastered prerequisites -- preventing premature difficulty increases.
- **Three-phase rubric evolution:** (1) Initial phase establishing foundation criteria, (2) middle phase with progressive difficulty increases as the model improves, (3) final phase where standards stabilize at appropriate difficulty.

The analysis prompt explicitly instructs the system to check "whether the model has been steadily improving" and "whether performance is expected given the model size at the current training step."

---

### 4. Domains of Operation

AMARIS was evaluated across four domains:

| Domain | Training Data | Evaluation Benchmark | Key Result |
|---|---|---|---|
| **Science** | RaR-Science | GPQA-Diamond | +1.6 pts over best baseline (40.4 vs 38.8) |
| **Medicine** | RaR-Medicine | HealthBench | +1.0 pts (34.0 vs 33.0) |
| **Instruction Following** | OpenRubrics | IFEval, InfoBench, IFBench | +0.6 to +1.1 pts across benchmarks |
| **Creative Writing** | RubricHub writing subset | WritingBench, Creative Writing v3 (EQ-Bench) | +1.0 to +1.1 pts |

Both closed-ended (science, medicine) and open-ended (instruction following, creative writing) tasks were covered. Per-instance rubrics outperformed global rubrics on six of seven benchmarks.

---

### 5. Relation to Reward Hacking / Gaming Detection

Reward hacking detection is a **core, integrated component** of AMARIS, not an afterthought:

- **Rollout-level detection:** Each individual analysis explicitly categorizes reward hacking signals (over-refusal, sycophancy, etc.) with evidence and confidence levels.
- **Batch-level aggregation:** Step summaries identify dominant reward hacking risks across the batch with supporting evidence.
- **Memory-tracked recurrence:** The persistent memory tracks which gaming behaviors have recurred across training, enabling the system to recognize patterns that would be invisible to local-only methods.
- **Defensive correction:** When reward hacking is detected and memory shows past correction attempts were insufficient, the system applies stronger corrective measures (e.g., deleting problematic rubrics, adding constraints).
- **Dynamic retrieval targeting:** Queries specifically target "suspected rubric flaws" that enable gaming behavior.

The authors' ethics statement notes: "AMARIS explicitly monitors for reward hacking and suboptimal behaviors as core component of individual rollout analysis."

---

### Key Ablation Findings

- Static memory alone: +0.9 pts on GPQA-D; dynamic memory alone: +0.6 pts. Combined: +1.9 pts -- confirming complementarity.
- Static retrieval is stronger for science (recent patterns dominant); dynamic retrieval is stronger for medicine (semantic matching across distant steps).
- Moderate retrieval budgets (N=4, K=10) capture most of the gain; increasing beyond this shows diminishing returns.
- Synchronous execution yields only +0.2 pts over async but nearly doubles training time (~146 hrs vs ~80 hrs).

### Baselines Compared Against

RaR (fixed rubrics), RubricHub/RuRL, RuscaRL, OpenRubrics, Rubric-ARM, RLCF -- AMARIS outperformed all of them consistently across every benchmark.

---

Sources:
- [AMARIS paper on arXiv](https://arxiv.org/abs/2605.18592)
- [AMARIS full HTML version](https://arxiv.org/html/2605.18592v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65010f9b-cfd4-4812-afb8-a19f34344463",
  "isSidechain": true,
  "agentId": "a8291f41460c22049",
  "requestId": "req_011CbV4GvFtfdqLTrNVEMXoj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8ffebdc-8ea1-4833-903a-5ab2e7e21758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "685603de-b7aa-40cf-a081-c3652dd9c757",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8Y3a6oSMVqxnWbRmZJUh6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4490,
      "cache_read_input_tokens": 13012,
      "output_tokens": 1753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4490
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1753,
          "cache_read_input_tokens": 13012,
          "cache_creation_input_tokens": 4490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4490,
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
