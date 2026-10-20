# Research conversation: I need to verify the paper "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad371a4f2bc829fa0.jsonl`
- **Structured JSON:** [`9ae3264983fb2ba5875d.json`](../../sessions/9a/9ae3264983fb2ba5875d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-19T23:39:08.409Z_

I need to verify the paper "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training" (arXiv 2605.06076). Specifically:
1. Does this paper exist on arXiv?
2. Does it introduce concepts of "Free Evolution" during SFT?
3. Does it introduce Circuit Distance, Circuit Stability, Circuit Conflict metrics?
4. Does it find that attention circuits shift while MLP circuits remain relatively stable?
5. What is the publication date?

Search for: "arxiv 2605.06076", "Navigating by Old Maps circuit evolution SFT", "static mechanistic localization post-training". Also try to fetch the arXiv page if possible. Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "37d607c2-4b49-43ee-865e-229c3fba97b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T23:39:08.410Z_

```json
{
  "parentUuid": "37d607c2-4b49-43ee-865e-229c3fba97b7",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
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
  "uuid": "f1038511-5ca4-4b19-a395-2a10f141eb94",
  "timestamp": "2026-05-19T23:39:08.410Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T23:39:08.411Z_

```json
{
  "parentUuid": "f1038511-5ca4-4b19-a395-2a10f141eb94",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "142ec538-4bcc-4db1-93b4-0b1ef8a4141d",
  "timestamp": "2026-05-19T23:39:08.411Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T23:39:10.637Z_



I'll search for this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142ec538-4bcc-4db1-93b4-0b1ef8a4141d",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouAzrBr3Qh3y9vfv75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7de570c5-2070-4572-be96-c8ef3bf71a8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpG63dXBDuV9rSKQkiQHHJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1511,
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

_source line 5 · 2026-05-19T23:39:11.093Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019KJ9B5CAwKm6K4XegNwYZA`</summary>

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
  "parentUuid": "7de570c5-2070-4572-be96-c8ef3bf71a8d",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouAzrBr3Qh3y9vfv75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27f5c809-ddcd-48fe-88e5-a8232d7936e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpG63dXBDuV9rSKQkiQHHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 7773,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1511
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1511,
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

_source line 6 · 2026-05-19T23:39:11.096Z_

<details><summary>↩ Tool result · `toolu_019KJ9B5CAwKm6K4XegNwYZA`</summary>

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
  "parentUuid": "27f5c809-ddcd-48fe-88e5-a8232d7936e9",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "cb52ac2c-4250-4fae-8cf8-757c5a9a7583",
  "sourceToolAssistantUUID": "27f5c809-ddcd-48fe-88e5-a8232d7936e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:39:13.577Z_



Now let me run multiple searches and fetch the arXiv page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb52ac2c-4250-4fae-8cf8-757c5a9a7583",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouNYPP78mdVLiKt7ut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "224e226f-d724-44ba-a7fd-3c6e9b11a563",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAdoMU5r2AC66pk5gzoeYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9284,
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

_source line 8 · 2026-05-19T23:39:13.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQcxpvQHrqzedJipACd2UJ`</summary>

```json
{
  "query": "arxiv 2605.06076 \"Navigating by Old Maps\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "224e226f-d724-44ba-a7fd-3c6e9b11a563",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouNYPP78mdVLiKt7ut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e20599f4-590a-4553-82fc-731508ec1929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAdoMU5r2AC66pk5gzoeYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9284,
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

_source line 9 · 2026-05-19T23:39:14.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017H9bJQcC88niS3QExHD5QL`</summary>

```json
{
  "query": "\"Navigating by Old Maps\" \"static mechanistic localization\" LLM post-training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20599f4-590a-4553-82fc-731508ec1929",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouNYPP78mdVLiKt7ut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66dc4ca1-b3ed-4005-99e2-639b4d00fc89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAdoMU5r2AC66pk5gzoeYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9284,
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

_source line 10 · 2026-05-19T23:39:15.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxqYaqDZXDKr9mPSoatFHV`</summary>

```json
{
  "query": "\"circuit evolution\" \"Free Evolution\" SFT mechanistic interpretability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66dc4ca1-b3ed-4005-99e2-639b4d00fc89",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouNYPP78mdVLiKt7ut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "569803ea-9313-4de4-9cc3-cbd840f595c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAdoMU5r2AC66pk5gzoeYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9284,
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

_source line 11 · 2026-05-19T23:39:16.858Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016neJ1chqZSU979SkeG8PRs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06076",
  "prompt": "Extract the full title, authors, abstract, publication date, and any key concepts mentioned in this paper. Look specifically for: \"Free Evolution\", \"Circuit Distance\", \"Circuit Stability\", \"Circuit Conflict\", attention circuits, MLP circuits, SFT, post-training, mechanistic localization. Report everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569803ea-9313-4de4-9cc3-cbd840f595c4",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCouNYPP78mdVLiKt7ut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1c1c5f0-1b46-4f50-9c57-c8c29e66b957",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAdoMU5r2AC66pk5gzoeYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9284,
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

### Tool result

_source line 12 · 2026-05-19T23:39:20.375Z_

<details><summary>↩ Tool result · `toolu_01BQcxpvQHrqzedJipACd2UJ`</summary>

```text
Web search results for query: "arxiv 2605.06076 "Navigating by Old Maps""

Links: [{"title":"[2605.06076] Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/abs/2605.06076"},{"title":"Navigating by Old Maps: The Pitfalls of Static","url":"https://arxiv.org/pdf/2605.06076"},{"title":"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/html/2605.06076"},{"title":"Latent learning without map-like representation of space in navigating ants","url":"https://www.biorxiv.org/content/10.1101/2024.08.29.610243.full.pdf"},{"title":"Emergence of Maps in the Memories of Blind Navigation Agents","url":"https://arxiv.org/pdf/2301.13261"},{"title":"Differential Brain Activity in Regions Linked to Visuospatial Processing During Landmark-Based Navigation in Young and Healthy Older Adults","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7668216/"},{"title":"Differential brain activity in visuo-perceptual regions during landmark-based navigation in young and healthy older adults","url":"https://www.biorxiv.org/content/10.1101/2020.03.13.990572.full.pdf"}]

Based on the search results, here's what I found about arxiv paper 2605.06076:

## "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training"

The paper addresses the "Locate-then-Update" paradigm, which has become a predominant approach in the post-training of large language models (LLMs), identifying critical components via mechanistic interpretability for targeted parameter updates.

The paper questions a fundamental assumption: can mechanisms derived from current static parameters reliably guide future dynamic parameter updates?

**Methodology:**
The authors systematically track the structural evolution of Transformer circuits throughout the supervised fine-tuning (SFT) process, and introduce three novel metrics—Circuit Distance, Circuit Stability, and Circuit Conflict—to analyze circuit evolution across three dimensions: neural migration, semantic stability, and cross-task interference.

**Key Finding:**
The empirical results reveal that circuits inherently exhibit "Free Evolution" during parameter updates.

The paper was submitted to arxiv on May 7, 2026, and is authored by Hang Chen, Jiaying Zhu, Hongyang Chen, Hongxu Liu, Xinyu Yang, and Wenya Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20599f4-590a-4553-82fc-731508ec1929",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "b69d7e42-8bed-47a0-9339-614acb51509f",
  "sourceToolAssistantUUID": "e20599f4-590a-4553-82fc-731508ec1929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T23:39:22.105Z_

<details><summary>↩ Tool result · `toolu_017H9bJQcC88niS3QExHD5QL`</summary>

```text
Web search results for query: ""Navigating by Old Maps" "static mechanistic localization" LLM post-training"

Links: [{"title":"[2605.06076] Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/abs/2605.06076"},{"title":"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/html/2605.06076"},{"title":"The Pitfalls of Static Mechanistic Localization in LLM Post- ...","url":"https://arxiv.org/pdf/2605.06076"},{"title":"How Post-Training Reshapes LLMs: A Mechanistic View on Knowledge, Truthfulness, Refusal, and Confidence","url":"https://arxiv.org/html/2504.02904v2"},{"title":"How Post-Training Reshapes LLMs: A Mechanistic View on Knowledge, Truthfulness, Refusal, and Confidence","url":"https://arxiv.org/pdf/2504.02904"},{"title":"Memorization Sinks: Isolating Memorization during LLM Training","url":"https://arxiv.org/html/2507.09937v2"}]

I found the paper you were looking for! Here are the search results:

"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training" is a recent research paper available on arXiv.

**Main Focus:**
The "Locate-then-Update" paradigm has become a predominant approach in the post-training of large language models (LLMs), identifying critical components via mechanistic interpretability for targeted parameter updates. However, this paradigm rests on a fundamental yet unverified assumption: can mechanisms derived from current static parameters reliably guide future dynamic parameter updates?

**Key Findings:**
The researchers systematically track the structural evolution of Transformer circuits throughout the supervised fine-tuning (SFT) process, introducing three novel metrics—Circuit Distance, Circuit Stability, and Circuit Conflict—to analyze circuit evolution across three dimensions: neural migration, semantic stability, and cross-task interference.

Static mechanisms extracted from current states inevitably suffer from temporal latency, making them fundamentally inadequate for guiding future states. The paper proposes that a "foresight" in mechanistic localization is necessary and proposes a predictive framework for future research.

The code is available on GitHub at https://github.com/Zodiark-ch/MechLocalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66dc4ca1-b3ed-4005-99e2-639b4d00fc89",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "339c3105-c194-44a8-b428-30daec82f14f",
  "sourceToolAssistantUUID": "66dc4ca1-b3ed-4005-99e2-639b4d00fc89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T23:39:22.180Z_

<details><summary>↩ Tool result · `toolu_016neJ1chqZSU979SkeG8PRs`</summary>

```text
# Paper Analysis: "Navigating by Old Maps"

**Full Title:** "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training"

**Authors:** Hang Chen, Jiaying Zhu, Hongyang Chen, Hongxu Liu, Xinyu Yang, Wenya Wang

**Publication Date:** Submitted May 7, 2026

**Key Concepts Found:**

The paper introduces a critical analysis of the "Locate-then-Update" paradigm in LLM post-training. Three novel metrics are central to the work:
- **Circuit Distance** - measures neural migration
- **Circuit Stability** - assesses semantic stability  
- **Circuit Conflict** - analyzes cross-task interference

**"Free Evolution" Phenomenon:** The research reveals that "circuits inherently exhibit 'Free Evolution' during parameter updates," indicating mechanisms evolve unpredictably during training.

**Core Finding:** The authors demonstrate that static mechanisms extracted from current model states suffer from "temporal latency" and cannot adequately guide future parameter modifications. They argue this represents an "illusion of effectiveness" in existing mechanistic localization methods.

**Research Scope:** The study tracks structural evolution of Transformer circuits throughout supervised fine-tuning (SFT), examining task mechanism dynamics.

**Proposed Direction:** The work advocates for incorporating "foresight" in mechanistic localization and suggests a predictive framework for future research approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1c1c5f0-1b46-4f50-9c57-c8c29e66b957",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "f362e3de-a35a-4be7-a0be-d42ed490faa9",
  "sourceToolAssistantUUID": "d1c1c5f0-1b46-4f50-9c57-c8c29e66b957",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T23:39:25.462Z_

<details><summary>↩ Tool result · `toolu_01UxqYaqDZXDKr9mPSoatFHV`</summary>

```text
Web search results for query: ""circuit evolution" "Free Evolution" SFT mechanistic interpretability 2025 2026"

Links: [{"title":"Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training","url":"https://arxiv.org/html/2605.06076"},{"title":"Mechanistic Interpretability Explained (2026)","url":"https://www.taskade.com/blog/what-is-mechanistic-interpretability"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Circuit Tracing for the Rest of Us: From Probes to Attribution Graphs and What It Means for Production Safety | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/circuit-tracing-production/"},{"title":"Adaptive Circuit Behavior and Generalization in Mechanistic   Interpretability","url":"https://arxiv.org/pdf/2411.16105"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/pdf/2510.14936"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/pdf/2304.14997"}]

Based on the search results, here's what I found regarding circuit evolution, "Free Evolution," SFT, and mechanistic interpretability:

## Key Finding: "Free Evolution" in SFT

Task mechanisms inherently undergo "free evolution" due to dynamic shifts during post-training, which causes static interpretability conclusions to suffer from severe temporal latency, fundamentally failing to guide future parameter updates. This concept comes from a recent paper titled "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training" (published 2 weeks ago on arXiv).

## Context: Mechanistic Localization and SFT

Mechanistic Localization uses mechanistic interpretability to identify the minimal parameter space responsible for a target skill. However, recent studies show that Mechanistic Localization often lacks completeness and exclusiveness. This is particularly relevant during supervised fine-tuning (SFT), where the paper demonstrates that circuit components shift dynamically during parameter updates.

## Recent Circuit Discovery Work

Anthropic open-sourced their circuit-tracing tools in May 2025, and the community has since applied them to open-weight models like Gemma-2-2b and Llama-3.2-1b. Additionally, Anthropic's 2025 work made a breakthrough by tracing not just what features are active but how they influence each other in sequence.

The search results highlight that understanding how circuits evolve during training and fine-tuning remains an active and challenging area in mechanistic interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "569803ea-9313-4de4-9cc3-cbd840f595c4",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "69b1147b-8abb-4ee7-8e14-6943784d6efc",
  "sourceToolAssistantUUID": "569803ea-9313-4de4-9cc3-cbd840f595c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T23:39:28.070Z_

Now let me fetch the HTML version for more detailed information about the specific findings regarding attention vs. MLP circuits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b1147b-8abb-4ee7-8e14-6943784d6efc",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCovRsqVCeTbqviWpjCM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a705921-ea47-4327-a743-5e12cd500aec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7u893JPm5xSjxjq5ucopT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 357,
      "cache_creation_input_tokens": 2458,
      "cache_read_input_tokens": 10399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2458,
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

_source line 17 · 2026-05-19T23:39:29.655Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kd6BU9yQetfLcNnvimuMFs`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06076",
  "prompt": "Look specifically for findings about attention circuits vs MLP circuits. Does the paper find that attention circuits shift while MLP circuits remain relatively stable? Extract any specific claims about attention heads, MLP layers, their relative stability or instability during SFT. Also extract the exact publication/submission date and any other key findings about circuit evolution patterns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a705921-ea47-4327-a743-5e12cd500aec",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCovRsqVCeTbqviWpjCM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca674c22-607d-483b-a885-64f307452880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7u893JPm5xSjxjq5ucopT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 357,
      "cache_creation_input_tokens": 2458,
      "cache_read_input_tokens": 10399,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2458
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 357,
          "output_tokens": 174,
          "cache_read_input_tokens": 10399,
          "cache_creation_input_tokens": 2458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2458,
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

_source line 18 · 2026-05-19T23:39:35.606Z_

<details><summary>↩ Tool result · `toolu_01Kd6BU9yQetfLcNnvimuMFs`</summary>

```text
# Key Findings on Circuit Evolution

## Publication Details
**Date:** arXiv:2605.06076v1, submitted May 7, 2026

## Attention vs. MLP Circuit Stability

The paper presents a clear dichotomy in circuit evolution patterns:

**Attention Circuits:** The researchers found that "Attn components consistently exhibit significantly higher C​DCD than MLP components throughout SFT," indicating substantial structural shifts. They characterize attention mechanisms as "highly volatile and prone to migration during updates."

**MLP Circuits:** In contrast, "knowledge"-centric MLP circuits "remain largely inert" and exhibit "resistance to neural migration." The paper notes that MLP stability "substantially exceeds Attn stability."

## Mechanistic Basis

The authors attribute this difference to functional roles: attention handles inter-token "skills" (like induction heads), while MLPs store semantic "knowledge" (factual concepts). The massive parameter volume in MLPs creates "deeply entrenched" information that resists reorganization, whereas attention's smaller footprint makes it "much more susceptible to interference."

## Key Implication

This differential evolution explains why static mechanistic localization appears effective for knowledge-editing tasks (MLP-dominated, slow-changing circuits) but fails for skill-centric tasks (attention-dominated, rapidly-evolving circuits)—revealing what the authors call "the illusion of effectiveness."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca674c22-607d-483b-a885-64f307452880",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "ad371a4f2bc829fa0",
  "type": "user",
  "uuid": "53cf508b-5ce8-4b15-98c1-f16d758c2827",
  "sourceToolAssistantUUID": "ca674c22-607d-483b-a885-64f307452880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T23:39:46.650Z_

Here is a comprehensive report on each of your questions:

---

**1. Does this paper exist on arXiv?**

Yes. The paper "Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training" exists at arXiv ID **2605.06076**. It is available in abstract, PDF, and HTML formats.

**2. Does it introduce "Free Evolution" during SFT?**

Yes. The paper reveals that circuits inherently exhibit "Free Evolution" during parameter updates in supervised fine-tuning (SFT). This refers to the phenomenon where task mechanisms evolve unpredictably during training, causing static interpretability conclusions to suffer from severe "temporal latency" -- making them fundamentally inadequate for guiding future parameter updates.

**3. Does it introduce Circuit Distance, Circuit Stability, and Circuit Conflict metrics?**

Yes. The paper introduces three novel metrics to analyze circuit evolution across three dimensions:
- **Circuit Distance** -- measures neural migration
- **Circuit Stability** -- assesses semantic stability
- **Circuit Conflict** -- analyzes cross-task interference

**4. Does it find that attention circuits shift while MLP circuits remain relatively stable?**

Yes. This is one of the paper's central empirical findings:
- **Attention circuits** consistently exhibit significantly higher Circuit Distance than MLP components throughout SFT. They are characterized as "highly volatile and prone to migration during updates."
- **MLP circuits** (knowledge-centric) "remain largely inert" and exhibit "resistance to neural migration." MLP stability substantially exceeds attention stability.

The authors attribute this to functional roles: attention handles inter-token "skills" (like induction heads) with a smaller parameter footprint making it susceptible to interference, while MLPs store semantic "knowledge" with massive parameter volumes that create deeply entrenched information resistant to reorganization. This differential evolution explains why static mechanistic localization appears effective for knowledge-editing (MLP-dominated) but fails for skill-centric tasks (attention-dominated) -- what they call "the illusion of effectiveness."

**5. What is the publication date?**

The paper was submitted to arXiv on **May 7, 2026** (arXiv:2605.06076v1).

**Additional details:**
- **Authors:** Hang Chen, Jiaying Zhu, Hongyang Chen, Hongxu Liu, Xinyu Yang, Wenya Wang
- **Code:** Available at https://github.com/Zodiark-ch/MechLocalization
- The paper critiques the "Locate-then-Update" paradigm and proposes that "foresight" in mechanistic localization is necessary, suggesting a predictive framework for future research.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2605.06076)
- [arXiv HTML version](https://arxiv.org/html/2605.06076)
- [arXiv PDF](https://arxiv.org/pdf/2605.06076)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cf508b-5ce8-4b15-98c1-f16d758c2827",
  "isSidechain": true,
  "agentId": "ad371a4f2bc829fa0",
  "requestId": "req_011CbCowBFXxkZRjKvrez1XF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17e8a7a3-dc9d-4fc4-9d4b-de60f4e47043",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1LfeVyBzZEc7YTUSWEQwY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 12857,
      "output_tokens": 693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 851
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 693,
          "cache_read_input_tokens": 12857,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 851,
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
