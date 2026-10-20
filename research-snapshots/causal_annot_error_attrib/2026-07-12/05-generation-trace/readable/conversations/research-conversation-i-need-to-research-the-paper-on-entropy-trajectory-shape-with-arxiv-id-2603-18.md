# Research conversation: I need to research the paper on "Entropy Trajectory Shape" with arXiv ID 2603.18940 (March 2026). It reportedly uses per

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab39e23077dea11a9.jsonl`
- **Structured JSON:** [`a7880c1155701aa18cef.json`](../../sessions/a7/a7880c1155701aa18cef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T09:57:08.565Z_

I need to research the paper on "Entropy Trajectory Shape" with arXiv ID 2603.18940 (March 2026). It reportedly uses per-step entropy dynamics for reliability prediction in LLM reasoning.

Please do the following:
1. Search for "Entropy Trajectory Shape arXiv 2603.18940", "per-step entropy dynamics reliability prediction LLM reasoning 2026", "entropy trajectory reasoning chain confidence"
2. Fetch and read the paper from https://arxiv.org/abs/2603.18940
3. Extract:
   - Exact title, authors, venue
   - Core method: How does it use entropy trajectories? What features are extracted per step?
   - Key results on calibration / reliability prediction
   - How does it relate to confidence composition?
   - Limitations

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "7f655e32-e922-4797-93ab-95ecd1584a71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:57:08.568Z_

```json
{
  "parentUuid": "7f655e32-e922-4797-93ab-95ecd1584a71",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
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
  "uuid": "170c1f44-298a-419f-b12c-10d695813e9d",
  "timestamp": "2026-05-19T09:57:08.568Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T09:57:08.568Z_

```json
{
  "parentUuid": "170c1f44-298a-419f-b12c-10d695813e9d",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e267e90f-a9ce-43ba-823c-8beec1ecf472",
  "timestamp": "2026-05-19T09:57:08.568Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T09:57:11.392Z_



I'll research this paper by searching the web and fetching the arXiv page. Let me start with multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e267e90f-a9ce-43ba-823c-8beec1ecf472",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDbVAmbN5EvWtnE9SW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91156ec9-cb64-4a2c-b467-abc8206eb149",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuSx8JbiE5PNNyR5ibjGmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1526,
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

_source line 5 · 2026-05-19T09:57:11.749Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Tq7HmzgPwNiF46thVKWcKR`</summary>

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
  "parentUuid": "91156ec9-cb64-4a2c-b467-abc8206eb149",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDbVAmbN5EvWtnE9SW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc06210e-6366-42d5-93ea-d29dc2694289",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuSx8JbiE5PNNyR5ibjGmE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 7773,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1526,
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

_source line 6 · 2026-05-19T09:57:11.753Z_

<details><summary>↩ Tool result · `toolu_01Tq7HmzgPwNiF46thVKWcKR`</summary>

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
  "parentUuid": "dc06210e-6366-42d5-93ea-d29dc2694289",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "91dcab31-1d33-4a18-80d8-85054c5ad7f7",
  "sourceToolAssistantUUID": "dc06210e-6366-42d5-93ea-d29dc2694289",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T09:57:14.707Z_



Now let me run the searches and fetch the arXiv page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91dcab31-1d33-4a18-80d8-85054c5ad7f7",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDqLrhznv2uLNo3sX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0386b1b-b499-4b9c-bbdd-46bba7583203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gwX6FQ2xomy6L9AP9H6N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 8 · 2026-05-19T09:57:14.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xrg692PCdNpK9wZrmQnSzv`</summary>

```json
{
  "query": "Entropy Trajectory Shape arXiv 2603.18940"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0386b1b-b499-4b9c-bbdd-46bba7583203",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDqLrhznv2uLNo3sX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cff46490-4c64-48da-8d86-05fda13f91ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gwX6FQ2xomy6L9AP9H6N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 9 · 2026-05-19T09:57:15.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FT2RKj6GaU6N8u7AKXsM4B`</summary>

```json
{
  "query": "per-step entropy dynamics reliability prediction LLM reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cff46490-4c64-48da-8d86-05fda13f91ab",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDqLrhznv2uLNo3sX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb007851-36ed-4e52-9653-40672a4b09ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gwX6FQ2xomy6L9AP9H6N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 10 · 2026-05-19T09:57:15.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018W994kkQNCgaKR5ia8rUwa`</summary>

```json
{
  "query": "entropy trajectory reasoning chain confidence LLM calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb007851-36ed-4e52-9653-40672a4b09ae",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDqLrhznv2uLNo3sX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bcb1ef8-561f-437d-b729-2532bedde9ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gwX6FQ2xomy6L9AP9H6N5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 11 · 2026-05-19T09:57:16.651Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016bM44HCstaeNTn5KWBPDE4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.18940",
  "prompt": "Extract the full details of this paper: exact title, all authors, abstract, submission date, venue/conference if mentioned, and any other metadata available on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bcb1ef8-561f-437d-b729-2532bedde9ec",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjDqLrhznv2uLNo3sX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba159c16-5dd3-48de-a77f-4ee636aeeeae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gwX6FQ2xomy6L9AP9H6N5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 9299,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 276,
          "cache_read_input_tokens": 9299,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1130,
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

_source line 12 · 2026-05-19T09:57:20.848Z_

<details><summary>↩ Tool result · `toolu_016bM44HCstaeNTn5KWBPDE4`</summary>

```text
# Paper Details

**Title:** "Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought"

**Author:** Xinghao Zhao

**ArXiv ID:** 2603.18940

**Submission Date:** March 19, 2026 (v1); March 27, 2026 (v2)

**Subject Areas:** Computation and Language (cs.CL); Machine Learning (cs.LG)

**Abstract Summary:** The paper proposes a diagnostic method based on entropy trajectory patterns rather than scalar values. The approach aims to evaluate uncertainty in reasoning tasks within LLMs. Key characteristics include: it is practical, interpretable, and accessible in black-box settings; it demonstrates robustness across different models and datasets; it has applications for selective prediction and task prioritization; and it focuses particularly on numeric and discrete-answer problems.

**Available Formats:** PDF, HTML (experimental), TeX source

**DOI:** https://doi.org/10.48550/arXiv.2603.18940

**Note:** No specific conference or venue publication is mentioned on this arXiv abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba159c16-5dd3-48de-a77f-4ee636aeeeae",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "af613739-2f7e-434e-b5d7-79e05aefe061",
  "sourceToolAssistantUUID": "ba159c16-5dd3-48de-a77f-4ee636aeeeae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T09:57:21.812Z_

<details><summary>↩ Tool result · `toolu_01Xrg692PCdNpK9wZrmQnSzv`</summary>

```text
Web search results for query: "Entropy Trajectory Shape arXiv 2603.18940"

Links: [{"title":"ENTROPY TRAJECTORY SHAPE PREDICTS LLM REASONING RELIABILITY:","url":"https://arxiv.org/pdf/2603.18940"},{"title":"[2603.18940] Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/abs/2603.18940"},{"title":"Entropy Trajectory Shape Predicts LLM Reasoning Reliability: A Diagnostic Study of Uncertainty Dynamics in Chain-of-Thought","url":"https://arxiv.org/html/2603.18940"},{"title":"Trajectory analysis through entropy characterization over coded representation","url":"https://arxiv.org/html/2405.03693v1"},{"title":"Trajectory analysis through entropy characterization over coded   representation","url":"https://arxiv.org/pdf/2405.03693"},{"title":"Rate of Entropy Production in Evolving Interfaces and Membranes under Astigmatic Kinematics: Shape Evolution in Geometric-Dissipation Landscapes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7597146/"}]

Based on the search results, here's information about arXiv paper 2603.18940:

## Overview

The paper "Entropy Trajectory Shape Predicts LLM Reasoning Reliability" is a diagnostic study of uncertainty dynamics in chain-of-thought reasoning, authored by Xinghao Zhao from Huazhong University of Science and Technology.

## Key Findings

The paper introduces entropy-trajectory monotonicity: a chain is monotone if its per-step answer-distribution entropy decreases at every step, reflecting consistent uncertainty reduction. 

On GSM8K with Qwen2.5-7B-Instruct, monotone chains achieve 68.8% accuracy versus 46.8% for non-monotone chains.

## Main Contribution

The paper proposes a simple yet effective diagnostic approach based on trajectory shape rather than scalar magnitude. This signal is practical, interpretable, and inexpensive to obtain in black-box settings, while remaining robust across models and datasets.

The work demonstrates that the shape of uncertainty dynamics—specifically whether entropy decreases monotonically across reasoning steps—is a better predictor of LLM reasoning correctness than the magnitude of entropy changes themselves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cff46490-4c64-48da-8d86-05fda13f91ab",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "6dcb0e97-4478-4bf1-8f5b-a07f3511b821",
  "sourceToolAssistantUUID": "cff46490-4c64-48da-8d86-05fda13f91ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:57:22.551Z_

<details><summary>↩ Tool result · `toolu_018W994kkQNCgaKR5ia8rUwa`</summary>

```text
Web search results for query: "entropy trajectory reasoning chain confidence LLM calibration 2026"

Links: [{"title":"ENTROPY TRAJECTORY SHAPE PREDICTS LLM REASONING RELIABILITY:","url":"https://arxiv.org/pdf/2603.18940"},{"title":"Entropy Trajectory Shape Predicts LLM Reasoning Reliability: A Diagnostic Study of Uncertainty Dynamics in Chain-of-Thought","url":"https://arxiv.org/html/2603.18940"},{"title":"[2603.18940] Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/abs/2603.18940"},{"title":"[2602.01288] EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/abs/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/html/2602.01288"},{"title":"Think Just Enough: Sequence-Level Entropy as a Confidence Signal for LLM Reasoning","url":"https://arxiv.org/pdf/2510.08146"},{"title":"A Survey on Entropy Mechanism in Large Reasoning Models","url":"https://www.techrxiv.org/users/1008371/articles/1370755/master/file/data/Entropy_RL_LLM_Survey%20(5)/Entropy_RL_LLM_Survey%20(5).pdf?inline=true"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/pdf/2602.01288"}]

I found recent research on this topic. Here are the key findings:

## Main Research Areas

Understanding uncertainty in chain-of-thought reasoning is critical for reliable deployment of large language models, with researchers proposing diagnostic approaches based on trajectory shape rather than scalar magnitude.

### Entropy Trajectory Shape and LLM Reliability

Recent work studies entropy dynamics within a single chain rather than across chains, analyzing the shape of the trajectory. The central insight is that reasoning quality can be diagnosed from how confidence evolves during generation, not just its average value.

### EDIS Framework

The Entropy Dynamics Instability Score (EDIS) is a trajectory-level metric that captures instability patterns in entropy evolution during LLM reasoning. EDIS quantifies instability in entropy evolution as a trajectory-level metric, and serves as an effective diagnostic signal for inference-time selection, substantially improving reasoning accuracy.

### Key Insight on Calibration

Recent evidence suggests entropy calibration degrades during autoregressive generation; reasoning unfolds sequentially and confidence evolves throughout the process, and how confidence evolves during generation is more informative than its aggregate value.

These 2026 papers represent recent advances in using entropy trajectory analysis as a diagnostic tool for understanding and improving LLM reasoning reliability and calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bcb1ef8-561f-437d-b729-2532bedde9ec",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "b63ec113-8147-4886-8aed-d1491f834e13",
  "sourceToolAssistantUUID": "1bcb1ef8-561f-437d-b729-2532bedde9ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T09:57:24.182Z_

<details><summary>↩ Tool result · `toolu_01FT2RKj6GaU6N8u7AKXsM4B`</summary>

```text
Web search results for query: "per-step entropy dynamics reliability prediction LLM reasoning 2026"

Links: [{"title":"[2603.18940] Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/abs/2603.18940"},{"title":"Entropy Trajectory Shape Predicts LLM Reasoning Reliability: A Diagnostic Study of Uncertainty Dynamics in Chain-of-Thought","url":"https://arxiv.org/html/2603.18940"},{"title":"ENTROPY TRAJECTORY SHAPE PREDICTS LLM REASONING RELIABILITY:","url":"https://arxiv.org/pdf/2603.18940"},{"title":"[2602.01288] EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/abs/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/pdf/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/html/2602.01288"},{"title":"The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?","url":"https://arxiv.org/pdf/2604.06192"},{"title":"The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?","url":"https://arxiv.org/html/2604.06192"},{"title":"Entropy Dynamics in LLMs: Metrics & Implications","url":"https://www.emergentmind.com/topics/entropy-dynamics-in-llms"}]

I found several highly relevant research papers from 2026 on this topic. Here are the key findings:

## Main Research Directions

Entropy-trajectory monotonicity captures information by tracking uncertainty evolution across steps in reasoning chains. This represents a significant advancement over simpler approaches.

### Key Papers from 2026

**1. Entropy Trajectory Shape Predicts LLM Reasoning Reliability**

Xinghao Zhao published a study on entropy trajectory shape predicting LLM reasoning reliability as a diagnostic study of uncertainty dynamics in chain-of-thought reasoning. This approach captures richer information by tracking uncertainty evolution across steps, at the cost of approximately 5 short completions per step.

**2. EDIS: Entropy Dynamics Instability Score**

The Entropy Dynamics Instability Score (EDIS) is a trajectory-level metric quantifying instability in entropy evolution. EDIS serves as an effective diagnostic signal for inference-time selection, substantially improving reasoning accuracy, and offers a promising direction for training-time sample curation.

### Why Entropy Dynamics Matter

How confidence evolves during generation is more informative than its aggregate value. Entropy dynamics have been established as an underexplored yet informative lens for understanding and improving LLM reasoning.

### Theoretical Understanding

The entropy-correctness correlation arises if autoregressive models learn, through training, to accumulate information about the true answer via answer-informative prefixes, a pattern inherited from human reasoning traces and reinforced by fine-tuning and reinforcement-learning pipelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb007851-36ed-4e52-9653-40672a4b09ae",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "80bea8f7-1696-47c0-ab50-ad0f2fc84a88",
  "sourceToolAssistantUUID": "fb007851-36ed-4e52-9653-40672a4b09ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T09:57:32.057Z_

Good, I have the basic metadata. Now let me fetch the full HTML version of the paper for detailed method, results, and limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80bea8f7-1696-47c0-ab50-ad0f2fc84a88",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjEkDK7CdZNKxiHqTPZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c6a3105-3918-4ab7-833b-50cddd12e21a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWGUKV5n4S38qyBrrjARt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 10429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1717,
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

_source line 17 · 2026-05-19T09:57:36.920Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NSo1XRFCvAVJAEovYSmCxN`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.18940",
  "prompt": "Extract ALL of the following in detail:\n\n1. Full abstract text\n2. The core method: How exactly are entropy trajectories computed? What is measured at each reasoning step? What features are extracted from the trajectory (monotonicity, slope, variance, etc.)?\n3. Key definitions: What is \"entropy-trajectory monotonicity\"? How is per-step entropy defined?\n4. Experimental setup: Which models and datasets are used? What baselines are compared?\n5. Key quantitative results: accuracy numbers, calibration metrics (ECE, AUROC, etc.), reliability prediction performance\n6. How does this relate to confidence composition across reasoning steps?\n7. Limitations section: what are the stated limitations?\n8. Related work: how does it position itself relative to prior work on LLM uncertainty/calibration?\n9. Any discussion of practical applications or deployment implications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c6a3105-3918-4ab7-833b-50cddd12e21a",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjEkDK7CdZNKxiHqTPZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "050feb43-db9d-48f7-af97-d1d3f7e54c64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWGUKV5n4S38qyBrrjARt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 10429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1717,
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

_source line 18 · 2026-05-19T09:57:38.880Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PzqqJSUehmf5jmemsRHark`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.18940",
  "prompt": "Extract the full details of:\n1. The complete abstract\n2. Section on methodology - how entropy trajectories are computed per step, what features are extracted\n3. All key quantitative results (tables, accuracy numbers, AUROC, ECE)\n4. The limitations section\n5. How the paper discusses confidence composition\n6. Any theoretical analysis or proofs provided"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "050feb43-db9d-48f7-af97-d1d3f7e54c64",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjEkDK7CdZNKxiHqTPZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb946e3d-7ec3-47fc-b200-62c788057fc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWGUKV5n4S38qyBrrjARt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1029,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 10429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1717,
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

_source line 19 · 2026-05-19T09:57:46.678Z_

<details><summary>↩ Tool result · `toolu_01PzqqJSUehmf5jmemsRHark`</summary>

```text
# Analysis of "Entropy Trajectory Shape Predicts LLM Reasoning Reliability"

## Abstract

The paper investigates how entropy trajectories—the sequence of probability distributions across reasoning steps—can serve as diagnostic indicators for predicting whether large language models will produce correct outputs during chain-of-thought reasoning. The authors propose that the shape and dynamics of these trajectories provide meaningful signals about model reliability.

## Methodology

The methodology involves computing entropy at each step during chain-of-thought generation:

- **Entropy Computation**: At each reasoning step, the model's output distribution is analyzed to extract entropy values, creating a temporal sequence across the entire reasoning process
- **Feature Extraction**: The trajectory itself serves as the primary feature set, capturing how confidence evolves through reasoning stages
- **Core Insight**: Rather than relying on single-point confidence metrics, the approach examines patterns in how uncertainty changes throughout the reasoning sequence

## Key Quantitative Results

While the document structure indicates extensive experimental sections with tables (tables.caption references range from 12 to 63), the specific numerical results are embedded in the compressed PDF streams. The paper demonstrates:

- Performance across multiple datasets including GSM8K
- AUROC (Area Under Receiver Operating Characteristic) metrics for reliability prediction
- ECE (Expected Calibration Error) measurements
- Comparisons with baseline confidence estimation approaches

## Limitations Section

The paper includes structured appendix material addressing ablation studies, fairness considerations, and token accounting details (subsections A.1 through A.22), suggesting comprehensive treatment of limitations and methodological details.

## Confidence Composition Discussion

The work examines how confidence emerges compositionally across reasoning steps, moving beyond treating "confidence as a monolithic construct" to understanding its dynamic formation through sequential hypothesis building and refinement.

## Theoretical Analysis

The paper provides mathematical formulations (equations 1-3 referenced) establishing the relationship between entropy trajectories and prediction reliability, though full proofs are embedded in the PDF's binary content streams.

[Binary content (application/pdf, 539.1KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-gen-pipeline/2d2eeec8-b593-4064-a21e-9999f7b6018b/tool-results/webfetch-1779184658901-m7bfgd.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb946e3d-7ec3-47fc-b200-62c788057fc3",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "f0d07f1c-b78e-4049-bc66-fe6c166e2c34",
  "sourceToolAssistantUUID": "bb946e3d-7ec3-47fc-b200-62c788057fc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T09:57:56.859Z_

<details><summary>↩ Tool result · `toolu_01NSo1XRFCvAVJAEovYSmCxN`</summary>

```text
# Research Summary: Entropy Trajectory Shape Predicts LLM Reasoning Reliability

## 1. Abstract

The paper investigates whether the shape of uncertainty dynamics across chain-of-thought reasoning steps predicts final answer correctness. By sampling answer completions at each step prefix, the authors compute per-step answer-distribution entropy trajectories and test whether monotonically decreasing patterns indicate reliable reasoning.

**Key finding:** On GSM8K (n=300) with Qwen2.5-7B, monotone chains achieve 68.8% accuracy versus 46.8% for non-monotone chains (+21.9pp, p=0.0005). Critically, total entropy reduction (scalar) shows no predictive power (ρ=−0.06), revealing a shape-over-magnitude dissociation.

## 2. Core Method

**Entropy trajectory computation:**
- At each reasoning step prefix, m=5 answer completions are sampled (temperature τ=0.7, max 150 tokens)
- Final numerical answers are extracted from completions
- Per-step answer-distribution entropy is calculated using: H_k = −∑ₐ p̂_k(a) log p̂_k(a)

**Trajectory analysis:**
- Binary monotonicity: chain is monotone if H_{k+1} ≤ H_k + ε for all steps (ε=0.01)
- Scalar coherence: C = H_0 − H_N (total entropy drop)
- Violation count: graded signal counting non-monotone transitions

## 3. Key Definitions

**"Entropy-trajectory monotonicity":** A reasoning chain exhibits this property when answer-distribution entropy decreases at every step (within tolerance ε), reflecting consistent uncertainty reduction about the final answer throughout generation.

**Per-step entropy:** Shannon entropy of the empirical answer distribution from m sampled completions at step prefix k.

## 4. Experimental Setup

**Models:** Qwen2.5-7B-Instruct (primary); Mistral-7B-Instruct-v0.3 (replication)

**Datasets:** 
- GSM8K pilot (n=300)
- Full GSM8K (n=1,319)
- MATH-500 (n=500)

**Baselines compared:**
- Self-consistency (SC@3, SC@5, SC@40)
- Scalar coherence
- Final-step entropy
- Token log-probability confidence
- Chain length
- Self-judgment signals

## 5. Key Quantitative Results

**Accuracy by monotonicity (GSM8K, n=300):**
- Monotone: 68.8% | Non-monotone: 46.8% | Gap: +21.9pp (95% CI: [+9.5, +34.3], OR=2.50)

**Full-scale results:**
- Full GSM8K (n=1,319): monotone 93.2% vs. 81.7% (+11.5pp)
- MATH-500 (n=500): monotone 63.7% vs. 30.4% (+33.3pp)
- Mistral-7B (n=300): monotone 72.3% vs. 37.6% (+34.7pp, OR=4.33)

**Calibration metrics:**
- Token log-probability ECE: 0.186 (step 0) → 0.312 (step 7)
- Answer-distribution AUROC: 0.547 (weak single-step signal)
- Violation count correlation: ρ=−0.198 (GSM8K), ρ=−0.381 (MATH-500)

**Selective prediction (73.7% coverage):**
- Monotonicity: +5.8pp gain
- Final-step entropy: +2.2pp
- Scalar coherence: −0.6pp (worse than random)

## 6. Confidence Composition Across Steps

The paper observes that token log-probability confidence becomes progressively miscalibrated at later reasoning steps—counterintuitively worsening rather than improving as models approach final answers. All standard proxy transformations (sigmoid, exponential) compress confidence ranges to near-degenerate intervals [0.802, 0.818], masking discrimination failure through normalization collapse rather than true calibration issues.

The answer-distribution scalar (majority-vote rate) at individual steps provides limited predictive power, motivating the trajectory-shape analysis.

## 7. Limitations

- Limited dataset breadth (concentrated on math word problems; HotpotQA insufficient for headline claims)
- Model coverage incomplete (Qwen, Mistral tested; broader families needed)
- Binary monotonicity exhibits 31.2% false-positive rate (precision 68.8%)
- Step-level correctness labels unavailable; ECE analysis uses final-answer correctness as proxy
- Early ECE curves underpowered at later steps (n=42 at step 7)
- Requires step-segmentation heuristics; sensitivity to segmentation method partially tested
- Shape signal not compared directly against anchor-token confidence or newer self-judgment baselines

## 8. Positioning Relative to Prior Work

**Versus self-consistency:** Generates 5 short completions per step (~1,500 tokens/question) rather than 10–40 full chains, providing step-level interpretability without discarding trajectory structure.

**Versus token log-probability methods:** Captures within-chain uncertainty evolution rather than relying on poorly-calibrated token-level confidences that collapse to narrow ranges.

**Versus process reward models:** Fully unsupervised, requiring only inference; no labeled process data or model internals needed.

**Versus single-trajectory reliability signals:** Richer temporal structure than anchor-token confidence; cheaper than white-box computational graph verification.

**Novel contribution:** First to demonstrate shape-over-magnitude dissociation—that _consistency_ of uncertainty decrease matters more than _magnitude_ of total drop.

## 9. Practical Applications

**Selective prediction triage:** Use monotonicity as a coverage filter—answer only monotone chains, abstain otherwise. Achieves superior accuracy-cost trade-off relative to scalar baselines at ~1,500 tokens/question.

**Compute-aware deployment:** Early-step monotonicity (k=2 transitions) recovers 76% of the full accuracy gap at 60% of trajectory cost, enabling two-stage triage: rapid early screening, full trajectory expansion only for ambiguous cases.

**Failure detection:** Violation count provides graded reliability signal (chains with ≥2 violations show accuracy drops to 24–72%); pattern interpretable for debugging.

**Complementary to majority voting:** Not positioned as SC replacement but as cheap, interpretable signal for scenarios prioritizing efficiency over maximum accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "050feb43-db9d-48f7-af97-d1d3f7e54c64",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "67cc73ec-ff97-413e-a2b5-f6456e2d2b23",
  "sourceToolAssistantUUID": "050feb43-db9d-48f7-af97-d1d3f7e54c64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T09:58:00.258Z_

Let me now search for any additional details about the related EDIS paper and the theoretical grounding paper mentioned in the search results, to provide fuller context on how this work fits into the broader landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67cc73ec-ff97-413e-a2b5-f6456e2d2b23",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjH9zcCHnNn8oJaaQbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c4c89ba-bae3-409c-8db8-14f1510a71c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M324TMCN5HPSwqEjEzZFgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 3093,
      "cache_read_input_tokens": 12146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3093,
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

_source line 22 · 2026-05-19T09:58:01.679Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017RMf8hstCzbfcsLATrq2LP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.01288",
  "prompt": "Extract the title, authors, abstract, and key method of the EDIS paper. How does it relate to entropy trajectory shape analysis? What is the Entropy Dynamics Instability Score?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c4c89ba-bae3-409c-8db8-14f1510a71c5",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjH9zcCHnNn8oJaaQbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4437c69-fa8a-4e8b-80da-ba44923c3181",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M324TMCN5HPSwqEjEzZFgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 3093,
      "cache_read_input_tokens": 12146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3093,
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

_source line 23 · 2026-05-19T09:58:02.551Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B61ZD3mgMjMgUr8E2oKLnt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06192",
  "prompt": "Extract the title, authors, and abstract. How does this paper explain WHY entropy dynamics correlate with reasoning correctness? What is the Stepwise Informativeness Assumption?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4437c69-fa8a-4e8b-80da-ba44923c3181",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjH9zcCHnNn8oJaaQbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5dfcd57-7888-4b3c-9a3f-d5b98bfa796d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M324TMCN5HPSwqEjEzZFgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 3093,
      "cache_read_input_tokens": 12146,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 266,
          "cache_read_input_tokens": 12146,
          "cache_creation_input_tokens": 3093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3093,
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

_source line 24 · 2026-05-19T09:58:07.027Z_

<details><summary>↩ Tool result · `toolu_017RMf8hstCzbfcsLATrq2LP`</summary>

```text
# EDIS Paper Summary

**Title:** "EDIS: Diagnosing LLM Reasoning via Entropy Dynamics"

**Authors:** Chenghua Zhu, Siyan Wu, Xiangkang Zeng, Zishan Xu, Zhaolu Kang, Yifu Guo, Yuquan Lu, Junduan Huang, and Guojing Zhou

**Abstract Overview:**
The researchers demonstrate that observing how confidence changes over time during text generation reveals more insights than static measurements. They discovered specific patterns in these temporal patterns that indicate reasoning errors.

**Key Method & Entropy Trajectory Analysis:**
The paper emphasizes that "the temporal evolution of confidence during generation carries richer information than aggregate statistics alone." The team identified characteristic entropy trajectory shapes distinguishing correct from incorrect reasoning. Erroneous outputs display unstable dynamics with two notable patterns:
- Burst spikes (sustained uncertainty growth)
- Peak-valley spikes (sharp rebounds after momentary confidence)

These patterns appear consistently across different models and training phases, suggesting they reflect fundamental aspects of reasoning failure.

**Entropy Dynamics Instability Score (EDIS):**
EDIS is a trajectory-level metric designed to quantify instability in how entropy evolves during generation. It functions as a diagnostic signal at inference time, improving reasoning accuracy while potentially supporting training-phase data selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4437c69-fa8a-4e8b-80da-ba44923c3181",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "ba97e640-e8e5-4e91-be62-e81b38e2fd36",
  "sourceToolAssistantUUID": "d4437c69-fa8a-4e8b-80da-ba44923c3181",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T09:58:07.332Z_

<details><summary>↩ Tool result · `toolu_01B61ZD3mgMjMgUr8E2oKLnt`</summary>

```text
# Paper Summary

**Title:** The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?

**Authors:** Mar Gonzàlez I Català, Haitz Sáez de Ocáriz Borde, George D. Montañez, Pietro Liò

**Abstract:** The researchers address why "internal entropy dynamics, defined under the predictive distribution of a model, correlate so robustly with external correctness given by the ground-truth answer."

## How the Paper Explains This Correlation

The authors propose that the correlation emerges because language models reason successfully when "they accumulate information about the true answer via answer-informative prefixes." In other words, correct reasoning traces progressively build up clues pointing toward the right answer.

## The Stepwise Informativeness Assumption (SIA)

SIA formalizes this intuition: "reasoning prefixes accumulate answer-relevant information in expectation as generation progresses." The authors demonstrate that this assumption naturally arises from standard training on human reasoning data and is reinforced by fine-tuning and reinforcement learning. They then derive testable predictions linking conditional answer entropy patterns to correctness, validating their theory across multiple reasoning benchmarks and diverse language model architectures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5dfcd57-7888-4b3c-9a3f-d5b98bfa796d",
  "isSidechain": true,
  "promptId": "c803892c-5106-4584-8104-83ba36b7b3b2",
  "agentId": "ab39e23077dea11a9",
  "type": "user",
  "uuid": "c4ed979f-cf38-4788-b084-69c25f5bd2e0",
  "sourceToolAssistantUUID": "a5dfcd57-7888-4b3c-9a3f-d5b98bfa796d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T09:58:44.273Z_

I now have comprehensive information. Here is the full research report.

---

## Research Report: "Entropy Trajectory Shape Predicts LLM Reasoning Reliability"

### Paper Metadata

- **Title:** Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought
- **Authors:** Xinghao Zhao (Huazhong University of Science and Technology)
- **ArXiv ID:** 2603.18940
- **Submitted:** March 19, 2026 (v1); March 27, 2026 (v2)
- **Subject Areas:** cs.CL, cs.LG
- **Venue:** No specific conference/journal publication mentioned (arXiv preprint)
- **DOI:** https://doi.org/10.48550/arXiv.2603.18940

---

### Core Method: Entropy Trajectory Analysis

The paper's central insight is that the **shape** of how uncertainty evolves across chain-of-thought reasoning steps predicts answer correctness far better than any scalar summary of uncertainty.

**Per-step entropy computation:**
1. At each reasoning step prefix k, sample m=5 answer completions (temperature=0.7, max 150 tokens).
2. Extract final numerical answers from each completion.
3. Compute per-step answer-distribution entropy: **H_k = -sum_a p_hat_k(a) log p_hat_k(a)**, where p_hat_k(a) is the empirical frequency of answer a among the m completions at step k.

**Features extracted from the trajectory:**
- **Binary monotonicity:** A chain is classified as "monotone" if H_{k+1} <= H_k + epsilon for all consecutive steps (epsilon=0.01 tolerance). This captures whether the model's uncertainty about the final answer decreases consistently at every step.
- **Scalar coherence (C):** C = H_0 - H_N, the total entropy drop from first to last step. This is the "magnitude" baseline.
- **Violation count:** A graded signal counting the number of non-monotone transitions (steps where entropy increases).

**Key dissociation discovered:** Total entropy reduction (scalar coherence) has essentially zero predictive power (rho = -0.06), while the binary shape property of monotonicity is highly predictive. This reveals a fundamental **shape-over-magnitude dissociation** -- the consistency of uncertainty reduction matters far more than how much total reduction occurs.

**Cost:** Approximately 1,500 tokens per question (5 short completions per step), which is substantially cheaper than self-consistency methods requiring 10-40 full chain regenerations.

---

### Key Quantitative Results

**Accuracy split by monotonicity:**

| Setting | Monotone Accuracy | Non-monotone Accuracy | Gap |
|---|---|---|---|
| GSM8K pilot (n=300, Qwen2.5-7B) | 68.8% | 46.8% | +21.9pp (OR=2.50, p=0.0005) |
| Full GSM8K (n=1,319) | 93.2% | 81.7% | +11.5pp |
| MATH-500 (n=500) | 63.7% | 30.4% | +33.3pp |
| Mistral-7B (n=300) | 72.3% | 37.6% | +34.7pp (OR=4.33) |

**Calibration and discrimination metrics:**
- Token log-probability ECE degrades across steps: 0.186 at step 0, worsening to 0.312 at step 7 -- confidence becomes *more* miscalibrated as reasoning progresses.
- Answer-distribution AUROC at individual steps: 0.547 (weak single-step signal, motivating trajectory-level analysis).
- Violation count correlation with correctness: rho = -0.198 (GSM8K), rho = -0.381 (MATH-500).

**Selective prediction (at 73.7% coverage):**
- Monotonicity filter: +5.8pp accuracy gain over unfiltered baseline
- Final-step entropy: +2.2pp
- Scalar coherence: -0.6pp (actually worse than random)

**Early stopping efficiency:** Using only k=2 transitions (early-step monotonicity) recovers 76% of the full accuracy gap at 60% of the trajectory computation cost.

---

### Relation to Confidence Composition

This paper makes a strong case that **confidence should not be treated as a monolithic, single-point quantity** but rather as something that evolves compositionally across reasoning steps. Key observations on this theme:

1. **Token log-probabilities are misleadingly stable:** All standard proxy transformations (sigmoid, exponential) compress confidence into near-degenerate intervals like [0.802, 0.818], creating an illusion of calibration through "normalization collapse" rather than genuine discrimination.

2. **Step-level calibration degrades:** Counterintuitively, token-level confidence becomes *more* miscalibrated at later reasoning steps, not less. This undermines approaches that simply aggregate per-step confidence scores.

3. **Shape captures compositional dynamics:** The monotonicity property captures whether each successive reasoning step genuinely narrows the answer distribution -- i.e., whether each step is doing useful compositional work toward the answer. Non-monotone trajectories indicate steps that "undo" previous progress, a hallmark of confused or erroneous reasoning.

4. **Theoretical grounding (from related work 2604.06192):** The "Stepwise Informativeness Assumption" by Gonzalez I Catala et al. formalizes why this works: correct reasoning prefixes accumulate answer-relevant information in expectation as generation progresses. When this accumulation is consistent (monotone entropy decrease), it signals the model is on a correct reasoning path.

---

### Limitations (as stated by the authors)

1. **Limited dataset breadth:** Concentrated on math word problems (GSM8K, MATH-500). HotpotQA was tested but found insufficient for headline claims. Generalization to other reasoning domains (code, logic, commonsense) is unproven.
2. **Incomplete model coverage:** Only Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 tested. Broader model families (GPT, Llama, Gemma, larger scales) are needed.
3. **High false-positive rate:** Binary monotonicity has a 31.2% false-positive rate (precision = 68.8%). Many monotone chains still produce wrong answers.
4. **No step-level correctness labels:** ECE analysis uses final-answer correctness as proxy for step-level correctness, which is an imperfect substitute.
5. **Underpowered late-step analysis:** Only n=42 chains reach step 7, making later ECE curves unreliable.
6. **Step segmentation sensitivity:** Requires heuristics for segmenting chains into discrete steps; sensitivity to segmentation method only partially tested.
7. **Missing comparisons:** Shape signal is not compared directly against anchor-token confidence methods or newer self-judgment baselines.

---

### Broader Context: Related Work in 2026

This paper is part of a rapidly emerging 2026 research thread:

- **EDIS (arXiv 2602.01288)** by Zhu et al. independently developed the Entropy Dynamics Instability Score, a trajectory-level metric quantifying instability in entropy evolution. EDIS identifies two characteristic failure patterns: "burst spikes" (sustained uncertainty growth) and "peak-valley spikes" (sharp rebounds after momentary confidence). EDIS serves both inference-time selection and training-time data curation.

- **Stepwise Informativeness Assumption (arXiv 2604.06192)** by Gonzalez I Catala et al. provides theoretical grounding for *why* entropy dynamics correlate with correctness, formalizing that autoregressive models trained on human reasoning traces learn to accumulate answer-relevant information step by step.

Together these three papers establish entropy trajectory analysis as a coherent new paradigm for LLM reasoning diagnostics, distinct from prior work on self-consistency, token log-probabilities, and process reward models.

---

Sources:
- [Entropy trajectory shape predicts LLM reasoning reliability (arXiv abstract)](https://arxiv.org/abs/2603.18940)
- [Entropy trajectory shape predicts LLM reasoning reliability (HTML)](https://arxiv.org/html/2603.18940)
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](https://arxiv.org/abs/2602.01288)
- [The Stepwise Informativeness Assumption](https://arxiv.org/html/2604.06192)
- [Entropy Dynamics in LLMs: Metrics & Implications (Emergent Mind)](https://www.emergentmind.com/topics/entropy-dynamics-in-llms)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4ed979f-cf38-4788-b084-69c25f5bd2e0",
  "isSidechain": true,
  "agentId": "ab39e23077dea11a9",
  "requestId": "req_011CbBjHvhRy5tPEmyvJScUB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77784335-6188-4432-888f-3d4e97deec12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2d2eeec8-b593-4064-a21e-9999f7b6018b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwNGeydXdbSGgivY4d5vHt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 15239,
      "output_tokens": 2140,
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
          "output_tokens": 2140,
          "cache_read_input_tokens": 15239,
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
