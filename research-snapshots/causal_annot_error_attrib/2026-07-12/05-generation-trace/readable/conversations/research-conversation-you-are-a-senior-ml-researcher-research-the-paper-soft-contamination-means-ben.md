# Research conversation: You are a senior ML researcher. Research the paper "Soft Contamination Means Benchmarks Test Shallow Generalization" by 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2b8479d348e87f02.jsonl`
- **Structured JSON:** [`fe6e84b0d34cc04f3f45.json`](../../sessions/fe/fe6e84b0d34cc04f3f45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-29T05:43:56.762Z_

You are a senior ML researcher. Research the paper "Soft Contamination Means Benchmarks Test Shallow Generalization" by Spiesberger et al., arXiv 2026, at https://arxiv.org/abs/2602.12413

Steps:
1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2602.12413
2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2602.12413
3. Search for any reviews or discussions: Use WebSearch to find "Soft Contamination Means Benchmarks Test Shallow Generalization 2026 review" and if found, fetch additional information.

For the paper, extract and report:
- The exact gap/problem they identified and how they discovered it
- Their key insight that others missed
- How they formulated the problem differently from prior work
- What existing techniques they adapted, combined, or simplified
- Technical method details (how they define and detect soft contamination, how they measure its effects)
- Key quantitative results (especially the 78% CodeForces finding mentioned in context)
- If reviewer comments found: what was praised and what was criticized

Be thorough and specific — include numbers, method details, and precise descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "dbc1e163-18d3-46bd-92b5-aad7c6571b40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:43:56.766Z_

```json
{
  "parentUuid": "dbc1e163-18d3-46bd-92b5-aad7c6571b40",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
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
  "uuid": "dcc1a68c-2f25-475d-87cb-808fcf3dfa91",
  "timestamp": "2026-05-29T05:43:56.766Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:43:56.769Z_

```json
{
  "parentUuid": "dcc1a68c-2f25-475d-87cb-808fcf3dfa91",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "22048f7a-8fe5-4eda-bb3a-96956f0c26f0",
  "timestamp": "2026-05-29T05:43:56.769Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:43:59.603Z_



I'll start by fetching the arxiv abstract page and the full PDF, and searching for reviews simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22048f7a-8fe5-4eda-bb3a-96956f0c26f0",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWKzu6cGoGVy9tgxH3uX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2047748e-3ee0-4142-b8b1-cd7ee4e9b7e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RC6quB1CtDNKgdcoPQKQsu",
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

_source line 5 · 2026-05-29T05:43:59.784Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AsvvwBXcuh8TuJ8TKmiAgL`</summary>

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
  "parentUuid": "2047748e-3ee0-4142-b8b1-cd7ee4e9b7e3",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWKzu6cGoGVy9tgxH3uX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e54b6e7-1beb-4cbd-b3b7-831275f2eee6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RC6quB1CtDNKgdcoPQKQsu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 7413,
      "output_tokens": 103,
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
          "output_tokens": 103,
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

_source line 6 · 2026-05-29T05:43:59.790Z_

<details><summary>↩ Tool result · `toolu_01AsvvwBXcuh8TuJ8TKmiAgL`</summary>

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
  "parentUuid": "5e54b6e7-1beb-4cbd-b3b7-831275f2eee6",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "11822de1-306e-4de6-ba0b-b85404478c26",
  "sourceToolAssistantUUID": "5e54b6e7-1beb-4cbd-b3b7-831275f2eee6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:44:03.389Z_



Now let me fetch the arxiv abstract page, the PDF, and search for reviews all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11822de1-306e-4de6-ba0b-b85404478c26",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL18SHqN1cmf72Uz6Ga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb08f7b1-f8e2-4b6d-b9ed-900729a54261",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMbJBZ1g2JxBqo8JPaZyxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 8 · 2026-05-29T05:44:04.817Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K2EXK73wWcmwsge7jV47Ys`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12413",
  "prompt": "Extract ALL information from this arxiv abstract page: the full title, all authors, the complete abstract text, submission date, any subject categories, and any other metadata available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb08f7b1-f8e2-4b6d-b9ed-900729a54261",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL18SHqN1cmf72Uz6Ga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2c79abb-ee81-448e-9cc6-36bf6c74a5d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMbJBZ1g2JxBqo8JPaZyxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 9 · 2026-05-29T05:44:08.675Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HpYpW8MGdvc1UBNZRNxrKv`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2602.12413",
  "prompt": "Extract the COMPLETE content of this research paper. I need:\n1. Full abstract\n2. Complete introduction section with all details about the problem, motivation, and contributions\n3. All methodology/technical details - how they define soft contamination, how they detect it, how they measure its effects, all formulas and algorithms\n4. All experimental results with specific numbers, percentages, and findings\n5. The complete related work section\n6. Discussion and conclusion sections\n7. Any tables and figures descriptions with their data\n8. Key definitions and theorems\nBe as thorough and detailed as possible - include specific numbers, method names, dataset names, and quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2c79abb-ee81-448e-9cc6-36bf6c74a5d0",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL18SHqN1cmf72Uz6Ga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f986e248-4065-468d-abb3-0a3c8878cd92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMbJBZ1g2JxBqo8JPaZyxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 10 · 2026-05-29T05:44:08.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013mff8167r4ZvuRs7oXesvc`</summary>

```json
{
  "query": "Soft Contamination Means Benchmarks Test Shallow Generalization Spiesberger 2026 review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f986e248-4065-468d-abb3-0a3c8878cd92",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL18SHqN1cmf72Uz6Ga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4ad4b9b-e1cf-4af5-b871-0c2978a0eaf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMbJBZ1g2JxBqo8JPaZyxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 9050,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 9050,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 11 · 2026-05-29T05:44:09.741Z_

<details><summary>↩ Tool result · `toolu_01K2EXK73wWcmwsge7jV47Ys`</summary>

```text
# arXiv Paper Extraction: 2602.12413

**Full Title:**
"Soft Contamination Means Benchmarks Test Shallow Generalization"

**Authors:**
Ari Spiesberger, Juan J. Vazquez, Nicky Pochinkov, Tomáš Gavenčiak, Peli Grietzer, Gavin Leech, Nandi Schoots

**Submission Date:**
February 12, 2026

**Subject Categories:**
- Machine Learning (cs.LG)
- Artificial Intelligence (cs.AI)

**Abstract Summary:**
The research investigates how benchmark performance becomes unreliable when training data contains semantic duplicates of test material. While traditional decontamination uses n-gram matching, this approach misses semantically equivalent content. The authors analyzed the Olmo3 corpus and discovered that "contamination remains widespread, e.g. we find semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems." Their findings demonstrate that including such duplicates improves benchmark scores, suggesting "gains reflect both genuine capability improvements and the accumulation of test data" in training corpora.

**Additional Metadata:**
- arXiv Identifier: 2602.12413
- DOI: 10.48550/arXiv.2602.12413
- License: CC BY 4.0
- PDF and HTML versions available
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2c79abb-ee81-448e-9cc6-36bf6c74a5d0",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "a0ca511e-b631-4161-a1d3-d39fe2f17f6a",
  "sourceToolAssistantUUID": "b2c79abb-ee81-448e-9cc6-36bf6c74a5d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T05:44:15.434Z_

<details><summary>↩ Tool result · `toolu_013mff8167r4ZvuRs7oXesvc`</summary>

```text
Web search results for query: "Soft Contamination Means Benchmarks Test Shallow Generalization Spiesberger 2026 review"

Links: [{"title":"[2602.12413] Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/abs/2602.12413"},{"title":"GitHub - AriSpiesberger/Soft-Contamination-Prevelance: Repository for SDTD expirements · GitHub","url":"https://github.com/AriSpiesberger/Soft-Contamination-Prevelance"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"},{"title":"Soft Contamination Inflates LLM Benchmarks - YouTube","url":"https://www.youtube.com/watch?v=zN1HugYZN30"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization | Hacker News","url":"https://news.ycombinator.com/item?id=47041000"},{"title":"LLM Benchmark Contamination","url":"https://peerlist.io/scroll/post/ACTHDNDNQPJRQ7NOE2AK9JQ8BDRQP9"},{"title":"Soft Contamination Means Benchmarks Test Shallow ...","url":"https://www.youtube.com/watch?v=k68-hlYoayw"},{"title":"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination","url":"https://arxiv.org/pdf/2509.00072"},{"title":"Soft Contamination in LLM Training: Shallow Generalization","url":"https://www.linkedin.com/posts/charlesmartin14_%F0%9D%90%92%F0%9D%90%A8%F0%9D%90%9F%F0%9D%90%AD-%F0%9D%90%82%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%AD%F0%9D%90%9A%F0%9D%90%A6%F0%9D%90%A2%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%A7-%F0%9D%90%8C%F0%9D%90%9E%F0%9D%90%9A%F0%9D%90%A7%F0%9D%90%AC-activity-7429255693205045249-KwM0"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/pdf/2603.21636"}]

Based on the search results, I found relevant information about this paper:

The paper "Soft Contamination Means Benchmarks Test Shallow Generalization" is authored by Ari Spiesberger and colleagues, and addresses how benchmark performance gives biased estimates of out-of-distribution generalization when LLM training data is polluted with benchmark test data.

The research focuses on a key problem: typical decontamination filters use n-gram matching which fail to detect semantic duplicates—sentences with equivalent or near-equivalent content that are not close in string space.

Using the open-data model OLMo3 as a case study, the researchers found semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems in OLMo3's training corpus.

The paper demonstrates that contamination improves benchmark scores through finetuning on semantic duplicates of benchmark data, but performance improvements on truly held-out items from the same benchmark suggest within-benchmark-distribution generalization rather than genuine capability growth.

This is an ICML 2026 submission.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4ad4b9b-e1cf-4af5-b871-0c2978a0eaf6",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "8711ff70-1e0d-4b97-b857-f946eeb48bed",
  "sourceToolAssistantUUID": "d4ad4b9b-e1cf-4af5-b871-0c2978a0eaf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T05:44:18.122Z_

<details><summary>↩ Tool result · `toolu_01HpYpW8MGdvc1UBNZRNxrKv`</summary>

```text
# Research Paper Summary: "Soft Contamination Means Benchmarks Test Shallow Generalization"

## Overview
This paper by Spiesberger et al. investigates "soft contamination" in AI model evaluation—where test data similarity to training data compromises benchmark validity without exact duplication.

## Abstract
The authors argue that current benchmarks may not properly assess genuine generalization because models trained on large internet-scale datasets encounter similar content during evaluation, even without explicit data leakage.

## Core Contributions

**Problem Definition:**
The paper distinguishes soft contamination from traditional data leakage. Rather than exact test set inclusion in training data, soft contamination describes scenarios where test examples are semantically similar to training examples, allowing models to succeed through surface pattern matching rather than robust generalization.

**Key Methodology:**

1. **Detection Framework**: The authors develop methods to quantify semantic similarity between training and test data using embedding-based approaches, examining overlap in vector space representations.

2. **Measurement Approach**: They assess contamination across multiple dimensions—exact duplicates, near-duplicates, and semantically related content—measuring similarity thresholds and their performance impact.

3. **Quantitative Analysis**: The research measures performance gaps between clean and contaminated scenarios, showing how benchmark scores artificially inflate when soft contamination exists.

## Major Findings

The research demonstrates that significant portions of popular benchmarks exhibit soft contamination. Models show substantially different performance profiles when evaluated on genuinely novel versus contaminated test sets, with performance degradation ranging from 5-15% on several benchmarks when controlling for contamination.

The analysis covers major models including GPT-4, OLMo 3, Claude Opus 4.5, and others, examining contamination across benchmarks like MMLU, GSM8K, HumanEval, and others.

## Related Work
The paper connects to prior research on:
- Data contamination detection (Yang et al., Riddell et al.)
- Benchmark reliability concerns
- Training data documentation practices
- Distribution shift and generalization

## Implications
Results suggest current benchmark evaluations may overestimate model capabilities and generalization abilities, with important consequences for model selection and deployment decisions.

[Binary content (application/pdf, 2.9MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-adversarial/257f41c8-db0b-4478-8965-67d0a340e5ab/tool-results/webfetch-1780033449415-69yp67.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f986e248-4065-468d-abb3-0a3c8878cd92",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "e64d655f-42ca-4aaa-89a2-9ebad1dd594b",
  "sourceToolAssistantUUID": "f986e248-4065-468d-abb3-0a3c8878cd92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T05:44:21.745Z_

Good, I have initial information. Now let me fetch the Hacker News discussion, the GitHub repository, and try to read the PDF that was saved locally for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e64d655f-42ca-4aaa-89a2-9ebad1dd594b",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL2UR6tT852YvSHg7pd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "517c51dc-ef4c-4c28-b606-99e5b0fad16b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r25VENCa37Ef1K68tWueB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 10175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
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

_source line 15 · 2026-05-29T05:44:23.797Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013iQ6DsMXDXNAWu92JAdQrM`</summary>

```json
{
  "url": "https://news.ycombinator.com/item?id=47041000",
  "prompt": "Extract ALL comments and discussions about this paper. Include every comment, who said it, and any criticisms, praise, or technical observations made. Be thorough - capture the full discussion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "517c51dc-ef4c-4c28-b606-99e5b0fad16b",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL2UR6tT852YvSHg7pd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a909c7d6-a971-41a5-8a4a-631e6f54e91d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r25VENCa37Ef1K68tWueB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 10175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
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

_source line 16 · 2026-05-29T05:44:24.568Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WSaaJLzC2SdVNJniG8WEp6`</summary>

```json
{
  "url": "https://github.com/AriSpiesberger/Soft-Contamination-Prevelance",
  "prompt": "Extract all information about this repository: README content, what code/experiments are included, methodology details, any results or data shared. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a909c7d6-a971-41a5-8a4a-631e6f54e91d",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL2UR6tT852YvSHg7pd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3b3d32-206a-476c-884f-aba3f55b343e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r25VENCa37Ef1K68tWueB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 10175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
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

_source line 17 · 2026-05-29T05:44:24.588Z_

<details><summary>↩ Tool result · `toolu_013iQ6DsMXDXNAWu92JAdQrM`</summary>

```text
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a909c7d6-a971-41a5-8a4a-631e6f54e91d",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "21e6244f-9564-4a18-959b-1e134199be3b",
  "sourceToolAssistantUUID": "a909c7d6-a971-41a5-8a4a-631e6f54e91d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-29T05:44:25.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013SyhYaNQApVzhaH7Pdymdi`</summary>

```json
{
  "query": "\"Soft Contamination\" Spiesberger ICML 2026 review decision openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e6244f-9564-4a18-959b-1e134199be3b",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL2UR6tT852YvSHg7pd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7be2713c-7450-4dca-9cd3-45727c614366",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r25VENCa37Ef1K68tWueB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1048,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 10175,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1048,
          "output_tokens": 322,
          "cache_read_input_tokens": 10175,
          "cache_creation_input_tokens": 1363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1363,
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

_source line 19 · 2026-05-29T05:44:25.143Z_

<details><summary>↩ Tool result · `toolu_01WSaaJLzC2SdVNJniG8WEp6`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3b3d32-206a-476c-884f-aba3f55b343e",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "2397e981-2aac-44bb-ae33-3cf8b1af82b2",
  "sourceToolAssistantUUID": "2a3b3d32-206a-476c-884f-aba3f55b343e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T05:44:31.200Z_

<details><summary>↩ Tool result · `toolu_013SyhYaNQApVzhaH7Pdymdi`</summary>

```text
Web search results for query: ""Soft Contamination" Spiesberger ICML 2026 review decision openreview"

Links: [{"title":"GitHub - AriSpiesberger/Soft-Contamination-Prevelance: Repository for SDTD expirements · GitHub","url":"https://github.com/AriSpiesberger/Soft-Contamination-Prevelance"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/html/2602.12413"},{"title":"[2602.12413] Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/abs/2602.12413"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"},{"title":"Citation Contamination of Systematic Review Literature in the Life Sciences by Paper Mills","url":"https://www.medrxiv.org/content/10.1101/2024.12.26.24319521.full.pdf"}]

Based on the search results, I found information about the "Soft Contamination" paper by Spiesberger and colleagues. Here's what I found:

The paper "Soft Contamination Means Benchmarks Test Shallow Generalization" is an ICML 2026 submission by Ari Spiesberger and colleagues. The research studies soft contamination of LLM training data by semantic duplicates of benchmark test data.

Using the open-data model OLMo3 as a case study, the researchers found semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems in OLMo3's training corpus. The contamination improves benchmark scores, and performance also improves on truly held-out items from the same benchmark, suggesting within-benchmark-distribution generalization rather than genuine capability growth.

However, I could not find specific information about the review decision status on OpenReview for this paper in the search results. The paper appears to be available on arXiv (arxiv.org/abs/2602.12413) and has a GitHub repository for the code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be2713c-7450-4dca-9cd3-45727c614366",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "d6ddde8c-7ca4-4317-a01e-7148f5d643d7",
  "sourceToolAssistantUUID": "7be2713c-7450-4dca-9cd3-45727c614366",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T05:44:35.134Z_

Let me fetch the HTML version of the paper for more detailed content, and try the Hacker News discussion again.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ddde8c-7ca4-4317-a01e-7148f5d643d7",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL3SLcyUW9B6M7bYnDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cef5c0e5-188a-401d-9377-90424b6be0fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTNZN7HHy6L7V4238La5fB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 11538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 22 · 2026-05-29T05:44:41.995Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011cBALsAie9NqDXpMveEeeM`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.12413",
  "prompt": "Extract the COMPLETE content of this paper with full detail. I need:\n\n1. FULL ABSTRACT - every sentence\n2. COMPLETE INTRODUCTION - the exact problem they identify, how they discovered it, all stated contributions\n3. METHODOLOGY in full detail:\n   - How they define \"soft contamination\" formally\n   - How they detect semantic duplicates (what embedding model, what similarity thresholds, what algorithm)\n   - How they distinguish soft contamination from hard contamination\n   - The experimental setup for measuring contamination effects (finetuning details, model used, datasets)\n4. ALL RESULTS with specific numbers:\n   - The 78% CodeForces finding - what exactly does this mean\n   - ZebraLogic 50% finding\n   - Any other benchmark contamination rates\n   - Performance differences between contaminated and clean evaluations\n   - Any ablation studies\n5. RELATED WORK - how they position relative to prior contamination work\n6. DISCUSSION and LIMITATIONS\n7. All TABLE and FIGURE data with specific numbers\n8. Any formal definitions or mathematical formulations\n\nBe extremely thorough. Include every number, percentage, and specific finding you can extract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cef5c0e5-188a-401d-9377-90424b6be0fd",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL3SLcyUW9B6M7bYnDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c862d752-ab94-4ef4-a0af-d0b981747777",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTNZN7HHy6L7V4238La5fB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 11538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 23 · 2026-05-29T05:44:42.591Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013JVp7JUzECgvEBfWtLbSWg`</summary>

```json
{
  "url": "https://news.ycombinator.com/item?id=47041000",
  "prompt": "Extract ALL comments and discussion about this paper. Include every commenter's username, their comment text, and any replies. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c862d752-ab94-4ef4-a0af-d0b981747777",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL3SLcyUW9B6M7bYnDX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de033857-0009-46bc-98c6-cb16b5776437",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTNZN7HHy6L7V4238La5fB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 11538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 24 · 2026-05-29T05:44:42.707Z_

<details><summary>↩ Tool result · `toolu_013JVp7JUzECgvEBfWtLbSWg`</summary>

```text
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de033857-0009-46bc-98c6-cb16b5776437",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "69b5438b-7704-4d71-88b5-73efb91b3eb4",
  "sourceToolAssistantUUID": "de033857-0009-46bc-98c6-cb16b5776437",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-29T05:45:32.170Z_

<details><summary>↩ Tool result · `toolu_011cBALsAie9NqDXpMveEeeM`</summary>

```text
# Comprehensive Paper Extraction: "Soft Contamination Means Benchmarks Test Shallow Generalization"

## 1. COMPLETE ABSTRACT

The paper addresses whether LLM training data contamination with benchmark test data biases performance estimates. Standard decontamination using n-gram matching fails to detect "semantic duplicates"—semantically equivalent content with different string forms. 

The authors found:
- **78% of CodeForces problems** have semantic duplicates in Olmo3 training data
- **50% of ZebraLogic problems** have exact duplicates
- Finetuning on semantic duplicates improves benchmark performance on both seen AND unseen items (20% improvement reported)
- Even ecologically valid contamination amounts (~5% of finetuning data) produce **12% performance gains** on seen items and **5.6% on unseen items**

They conclude recent benchmark gains are confounded by accumulating test-like data in growing corpora, reflecting "shallow generalization" rather than pure capability improvements.

---

## 2. COMPLETE INTRODUCTION

### Problem Identification

Reasoning and coding benchmarks show rapid performance improvements, but the source is ambiguous: genuine OOD capability growth or training corpus contamination?

Key facts establishing urgency:
- LLM training corpora grew **10,000x since 2020**
- Despite decontamination efforts, "soft" semantic contamination remains "extremely hard to detect"
- Previous n-gram methods miss semantic duplicates

### Core Discovery Process

Using open-source Olmo3 model (enabling known training data analysis), they embedded the full training corpus and discovered:
- Widespread semantic duplicates despite decontamination efforts
- Performance improvements from finetuning on benchmark-similar data generalizes within benchmarks

### Stated Contributions

1. **Large contamination rates**: Screened 1% of pretraining + all finetuning data; found more contamination than prior studies (likely due to examining vastly more data)

2. **Shallow generalization effects**: Finetuning on benchmark semantic duplicates improved unseen benchmark items by ~20% (MuSR), with effect sizes comparable to exact duplicates. Finetuning on cosine-similar embeddings alone showed no effect.

3. **Ecologically valid contamination impact**: Using realistic contamination ratios in finetuning (~4 in 10,000 datapoints are semantic duplicates), found **15% substantial benchmark improvements**

---

## 3. METHODOLOGY - COMPLETE DETAIL

### 3.1 Formal Definitions

**Exact duplicate**: Training corpus example syntactically identical (or within n-grams) to test item

**Semantic duplicate**: Training example with same meaning as test item (without syntactic similarity)

**Soft contamination**: Contamination involving semantic duplicates

**Shallow generalization**: Limited to within-distribution generalization + generalization across semantic duplicates

### 3.2 Semantic Duplicate Detection Pipeline

**Data Processed**:
- Dolma3 (6.0TB) - sampled 1%
- Dolmino (250GB) - sampled 1%
- Dolci3 SFT (3.08GB) - 100%
- Dolci3 DPO (811MB) - 100%
- Dolci3 RL (483MB) - 100%

**Stratified reservoir sampling** preserved corpus hierarchical structure by source.

**Embedding Model**: llama-embed-nemotron-8b (rank #2 on MTEB leaderboard), FP16 precision

**Similarity Metric**: Cosine similarity between benchmark embeddings and corpus embeddings

**Detection Algorithm**:
1. Embed all corpus data and benchmarks
2. Calculate cosine similarity
3. For high-similarity matches: Use Gemini-3-flash to annotate semantic duplicate status
4. Sample from top 0.1% similarity matches (100 samples per benchmark item)

**Duplicate Classification Types**: Exact, equivalent, subset, superset

### 3.3 Benchmarks Selected

**MBPP**: 257 programming tasks with test cases; easy to generate alternative solutions

**CodeForces**: 468 competitive programming problems; expected to have lower-context variants in training data

**MuSR**: 250 logic-tree-based murder mysteries; generates duplicates by regenerating narratives from same trees

**ZebraLogic**: 1000 logic grid puzzles; Olmo3 not saturated (32.9% accuracy)

### 3.4 Synthetic Semantic Duplicate Generation

**MBPP**: 
- Inputs: 5 distinct paraphrases per task via LLM
- Outputs: Alternative Python implementations with <0.85 difflib similarity, validated against test cases

**MuSR** (3 levels):
- Level 1: Same tree, regenerated story context
- Level 2: One non-critical branch changed
- Level 3: All replaceable branches changed
- Generated 2 duplicates per level × 250 samples = 1500 duplicates per task

**ZebraLogic**:
- Substitution: "color" → "shape" via category mappings
- Shuffling: Reorder clues
- Paraphrasing: Preserve values exactly
- Applied individually and in combinations

### 3.5 Finetuning Experimental Setup

**Base Model**: Olmo3-7b Instruct

**Procedure**:
- Generate Chain-of-Thought reasoning via teacher models (Opus 4.5, GPT-4-mini)
- LoRA finetuning (Rank 16, Alpha 32, Dropout 0.05)
- Split duplicates 50-50: finetune on half, evaluate on both halves

**Hyperparameters by Benchmark**:
- MBPP: LR 1.5e-4, KL 0.02, 10 epochs
- MuSR: LR 2e-4, 6 epochs
- ZebraLogic: LR 2e-4, 10 epochs

**Generalization Testing**: Evaluated on different benchmarks in same domain:
- MuSR → TrueDetective
- ZebraLogic → Arc Challenge
- MBPP → HumanEval

---

## 4. ALL RESULTS WITH SPECIFIC NUMBERS

### 4.1 Exact Duplicates in Training

**ZebraLogic Findings**:
- **49.5% of all tasks** have corpus duplicates
- **70%+ of 4×4 puzzles and larger** have exact duplicates
- Found in Dolci-Instruct-RL dataset despite being evaluation benchmark

Model performance progression correlated with duplicate presence:
- SFT: 18%
- DPO (no duplicates detected): 28.4% (+10.4 points)
- RL (heavy duplication): 32.9% (+4.5 points)

### 4.2 Natural Semantic Duplicates in Wild

**MBPP**:
- **100% of problems** have ≥1 semantic duplicate in top 100 cosine-similar matches
- No exact duplicates found
- Across all training datasets: semantic duplicates present everywhere

**CodeForces**:
- **77.5% of problems** have ≥1 semantic duplicate in top 100 matches
- Authors note this is lower bound; more would be found checking all data
- **78% contamination rate** (as stated in abstract)

**Cosine Similarity Relationship**:
- Very high similarity (0.8+): substantial portion are semantic duplicates
- Even within top 0.1% matches, many non-duplicates exist

**Scaling Observation**: As more matches investigated, contamination % increases:
- CodeForces: 28.4% with top-1 match only
- Scales up with more matches examined

**Breakdown by Training Dataset**:
- MBPP: Present in all 5 datasets (Dolma, Dolmino, Dolci-SFT, DPO, RL)
- CodeForces: Particularly high in Dolma, Dolci-SFT, Dolci-DPO

**MuSR Finding**: Highest cosine similarity ~0.40; no semantic duplicates or MuSR-like problems detected

### 4.3 Finetuning on Semantic Duplicates

#### MuSR Results (Table 2)
| Condition | Seen | Unseen | TrueDetective |
|-----------|------|--------|---------------|
| Baseline | 66.0% | 28.3% | — |
| Exact Dupes | 87.9% | 87.3% | 27.7% |
| Level 1 | 85.8% | 86.2% | 29.3% |
| Level 2 | 85.7% | 86.0% | 28.3% |
| Level 3 | 87.5% | 87.9% | 29.8% |
| Cosine-Similarity SFT | 68.6% | 25.1% | — |

**Key Findings**:
- **~20 percentage point improvement** on both seen and unseen with exact or semantic duplicates
- Cosine-similar data alone provides no benefit
- Cross-benchmark transfer (TrueDetective) remains stable (~28%)
- **Strong within-benchmark generalization evident**

#### ZebraLogic Results (Table 3)
| Condition | Seen | Unseen | Arc Challenge |
|-----------|------|--------|----------------|
| Baseline | 36.9% | 50.1% | — |
| Exact Dupes | 48.4% | 43.4% | 49.5% |
| Paraphrase | 39.2% | 36.2% | 49.3% |
| Shuffle/Subs | 36.0% | 36.8% | 50.7% |
| Shuffle/Para | 38.0% | 36.0% | 49.4% |
| Shuffle/Subs/Para | 28.0% | 28.4% | 50.4% |
| Cosine-Similarity | 22.9% | — | — |

**Key Findings**:
- Exact duplicates show **11.5 point seen improvement**, degraded to **-6.7 unseen**
- Semantic duplicates show **minimal effect** (often degradation)
- Complex transformations actually harm performance
- Cross-benchmark (Arc) stable throughout
- Suggests semantic duplicates less effective for this task than MuSR

#### MBPP Results (Table 4)
| Condition | Seen | Unseen | HumanEval |
|-----------|------|--------|-----------|
| Baseline | 46.4% | 55.3% | — |
| Exact Dupes | 63.0% | 48.8% | 49.2% |
| Semantic (Python) | 55.1% | 53.6% | **67.0%** |
| Cosine-Similarity | 48.8% | 53.1% | — |

**Key Findings**:
- Exact duplicates: **16.6 point seen boost**, **-6.5 unseen degradation**
- Semantic duplicates: **8.7 point seen boost**, **-1.7 unseen minimal degradation**
- **Surprising 11.7 point HumanEval improvement** with semantic duplicates suggests some cross-domain transfer despite "shallow" framing
- Baseline variability noted: 6% difference between halves (atypical)

### 4.4 Ecologically Valid Contamination

**Contamination Rate Determination**:
- Found ~40 semantic duplicates per 100 samples in top 0.1% similarity range
- Concluded **~4 in 10,000 training datapoints** per benchmark item are semantic duplicates

**Experimental Setup (MuSR)**:
- Clean finetuning: 10,000 verified decontaminated datapoints
- Contaminated finetuning: Same dataset with 5% replaced by 500 semantic duplicates (2 Level 2 + 2 Level 3 per 125 examples)

#### Olmo3 Results
| Metric | Clean | Contaminated |
|--------|-------|--------------|
| Seen items | — | +12.0 points vs clean |
| Unseen items | 29.3% | +5.6 points vs clean |
| TrueDetective | 28.0% | 28.0% (stable) |

**Key Finding**: Even low contamination rates produce substantial benchmark gains without cross-domain transfer.

#### Qwen3 Results (noisy)
- Contaminated model: 13.6% seen advantage
- Clean model unexpectedly showed substantive MuSR gains (unexpected result)
- TrueDetective improvements noted (unexpected)

---

## 5. RELATED WORK POSITIONING

**First wave** (Magar & Schwartz 2022, et al.): Focused on exact syntactic duplicates

**Second wave** (Yang et al. 2023, Riddell et al. 2024): Extended to semantic contamination but:
- Smaller datasets investigated
- Focused on item-to-item memorization effects
- Limited or no finetuning validation
- No ecological validity consideration

**Key differentiation of this work**:
- **Largest data investigation**: 1% of pretraining + 100% of instruction tuning
- **Unified framework**: Treats all contamination forms (exact, semantic, embedding-neighbors) as shallow generalization
- **Novel generalization testing**: Within-benchmark generalization (finetuning on some items improves unseen items)
- **First ecologically valid study**: Realistic contamination ratios
- **Open-source model advantage**: Known training data enables exhaustive analysis

---

## 6. DISCUSSION & LIMITATIONS

### Key Arguments

**Shallow vs. genuine progress unclear**: 
- Benchmark gains partly reflect interpolation on growing corpus
- Not necessarily illusory (models are improving), but confounded

**Why benchmark-convergent data is problematic**:
- Benchmarks intended as OOD generalization tests
- Convergent training data acts as major confounder
- Rapid corpus growth × data deduplication gaps = systematic contamination

### Stated Limitations

1. **Likely underestimation**: High false-negative rate in semantic duplicate detection; rephrasings underrepresented in Dolma vs. current synthetic pipelines

2. **Scope limitation**: Only open-source models; frontier models use much larger corpora (30T tokens for Llama 4) with different natural duplicate rates

3. **Philosophical objection**: Some argue in-distribution performance on all tasks is valid goal, not OOD generalization

4. **Synthetic duplicates caveat**: Quality/realism of generated duplicates impacts findings; real contamination may differ

5. **Partial within-benchmark generalization**: Strong in high-contamination setup (Section 4.3) but weaker in ecological setup (Section 4.4); requires further investigation

---

## 7. TABLE & FIGURE DATA

### Figure 1: ZebraLogic Exact Duplicates by Puzzle Size
Grid size 4×4: ~70% have ≥1 duplicate
Grid size 5×5+: ~75%+ have duplicates
Cumulative: 49.5% minimum across all sizes

### Figure 2: Cosine Similarity vs. Semantic Duplicate Status
**MBPP**: 
- ~95% of 0.95+ similarity matches are semantic duplicates
- Even 0.70-0.75 range: 50%+ are duplicates
- Perfect overlay of exact/semantic (no exact duplicates found)

**CodeForces**:
- 0.95+: ~85% semantic duplicates
- 0.75-0.80: ~60-70% semantic duplicates
- Exact vs. semantic diverge (exact duplicates present)

### Figure 3: Semantic Duplicate Occurrence by Elo Score
- No strong correlation with problem difficulty
- Easier and harder problems equally likely to have duplicates

### Figure 4: Contamination by Training Dataset
**MBPP**: Present in all datasets
- Dolmino, Dolci-RL highest rates
- All >70% benchmark coverage

**CodeForces**: 
- Dolma: ~80%
- Dolci-SFT, DPO: ~70-80%
- Variation present but consistent presence

### Figure 5: Scaling with Number of Matches
**MBPP**: Approaches 100% as more matches checked
**CodeForces**: Scales from 28% (top-1) toward ~80%+
Shows sparse but ubiquitous distribution of duplicates

### Figure 6: Cosine Similarity Distributions
Across all benchmark-corpus pairs:
- Long right tails beyond 0.8 similarity
- Peak distributions around 0.2-0.4 range
- MuSR peaks lower (~0.35) than MBPP/CodeForces (~0.45)

---

## 8. FORMAL DEFINITIONS & MATHEMATICAL FORMULATION

The paper uses:
- **Cosine similarity** (standard vector dot product normalized)
- **SequenceMatcher similarity** threshold <0.85 for code duplicates (validates alternative implementations sufficiently different)
- **Sampling**: Stratified reservoir sampling maintaining source distribution topology
- **Annotation**: Multi-class (exact/equivalent/subset/superset) via LLM with confidence scores

No formal mathematical framework provided; relies on empirical thresholds and algorithmic procedures.

---

## CRITICAL NUMBERS SUMMARY

| Finding | Number | Context |
|---------|--------|---------|
| CodeForces contamination | 78% | Semantic duplicates in top 100 matches |
| ZebraLogic exact contamination | 50% | Minimum across all puzzle sizes |
| MBPP 100% benchmark coverage | 100% | Semantic duplicates present for all 257 tasks |
| MuSR within-benchmark improvement | ~20 points | Both seen and unseen with duplicates |
| Exact duplicate effect (MBPP) | 16.6 points (seen) | Finetuning improvement |
| Semantic duplicate effect (MBPP) | 8.7 points (seen) | Finetuning improvement |
| Ecologically valid effect (unseen) | 5.6 points | Realistic contamination ratio |
| Ecologically valid effect (seen) | 12 points | Realistic contamination ratio |
| Contamination ratio | 4/10,000 | Semantic duplicates per item |
| Training data growth | 10,000x | Since 2020 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c862d752-ab94-4ef4-a0af-d0b981747777",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "0379cacf-6696-4823-9462-67dccea03618",
  "sourceToolAssistantUUID": "c862d752-ab94-4ef4-a0af-d0b981747777",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-29T05:45:36.073Z_

Excellent, the HTML version gave very detailed content. Let me now try to fetch the Hacker News discussion and search for any OpenReview reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0379cacf-6696-4823-9462-67dccea03618",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL7w5s4UMqyJxQodDi7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6abd5881-061b-4cff-8848-6b9953f32629",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126u1e6NNqq5mZgzdyVvN2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 87,
      "cache_creation_input_tokens": 4964,
      "cache_read_input_tokens": 13747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4964,
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

_source line 27 · 2026-05-29T05:45:36.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EnZo32Bqh9vtKLrW2yPJfH`</summary>

```json
{
  "query": "site:openreview.net \"Soft Contamination\" \"Shallow Generalization\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6abd5881-061b-4cff-8848-6b9953f32629",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL7w5s4UMqyJxQodDi7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89111fb8-1e10-42fc-a9a0-7cde590f033b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126u1e6NNqq5mZgzdyVvN2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 87,
      "cache_creation_input_tokens": 4964,
      "cache_read_input_tokens": 13747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4964,
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

_source line 28 · 2026-05-29T05:45:37.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KX2deSsP6qHGJLXYmTztDg`</summary>

```json
{
  "query": "\"Soft Contamination Means Benchmarks\" Spiesberger discussion criticism opinion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89111fb8-1e10-42fc-a9a0-7cde590f033b",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL7w5s4UMqyJxQodDi7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a6d8cdf-5873-4a15-b808-ecf2032df2f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126u1e6NNqq5mZgzdyVvN2U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 87,
      "cache_creation_input_tokens": 4964,
      "cache_read_input_tokens": 13747,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 87,
          "output_tokens": 165,
          "cache_read_input_tokens": 13747,
          "cache_creation_input_tokens": 4964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4964,
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

_source line 29 · 2026-05-29T05:45:43.399Z_

<details><summary>↩ Tool result · `toolu_01EnZo32Bqh9vtKLrW2yPJfH`</summary>

```text
Web search results for query: "site:openreview.net "Soft Contamination" "Shallow Generalization" 2026"

Links: [{"title":"GitHub - AriSpiesberger/Soft-Contamination-Prevelance: Repository for SDTD expirements · GitHub","url":"https://github.com/AriSpiesberger/Soft-Contamination-Prevelance"},{"title":"[2602.12413] Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/abs/2602.12413"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization | Hacker News","url":"https://news.ycombinator.com/item?id=47041000"},{"title":"Soft Contamination in LLM Training: Shallow Generalization","url":"https://www.linkedin.com/posts/charlesmartin14_%F0%9D%90%92%F0%9D%90%A8%F0%9D%90%9F%F0%9D%90%AD-%F0%9D%90%82%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%AD%F0%9D%90%9A%F0%9D%90%A6%F0%9D%90%A2%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%A7-%F0%9D%90%8C%F0%9D%90%9E%F0%9D%90%9A%F0%9D%90%A7%F0%9D%90%AC-activity-7429255693205045249-KwM0"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"LLM Benchmark Contamination","url":"https://peerlist.io/scroll/post/ACTHDNDNQPJRQ7NOE2AK9JQ8BDRQP9"},{"title":"Contamination Detection for VLMs Using Multi‑Modal Semantic Perturbations | OpenReview","url":"https://openreview.net/forum?id=gk6OC3XIZW"}]

Based on the search results, I found relevant information about "Soft Contamination" and "Shallow Generalization" from 2026:

The paper "Soft Contamination Means Benchmarks Test Shallow Generalization" is an ICML 2026 submission. The paper studies soft contamination of training data by semantic duplicates—sentences with equivalent or near-equivalent content that are not close in string space—which typical decontamination filters using n-gram matching fail to detect.

Using the open-data model OLMo3 as a case study, the researchers found semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems in OLMo3's training corpus. They found that finetuning on semantic duplicates of benchmark data improves performance on those benchmarks, and performance also improves on truly held-out items from the same benchmark, suggesting within-benchmark-distribution generalization rather than genuine capability growth.

The paper appears on arXiv (arxiv.org/abs/2602.12413) and was submitted in February 2026, though the search results don't show it directly on OpenReview.net in this query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89111fb8-1e10-42fc-a9a0-7cde590f033b",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "6c134f02-6327-4a03-8af0-a252fcc3bf89",
  "sourceToolAssistantUUID": "89111fb8-1e10-42fc-a9a0-7cde590f033b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T05:45:44.677Z_

<details><summary>↩ Tool result · `toolu_01KX2deSsP6qHGJLXYmTztDg`</summary>

```text
Web search results for query: ""Soft Contamination Means Benchmarks" Spiesberger discussion criticism opinion 2026"

Links: [{"title":"[2602.12413] Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/abs/2602.12413"},{"title":"GitHub - AriSpiesberger/Soft-Contamination-Prevelance: Repository for SDTD expirements · GitHub","url":"https://github.com/AriSpiesberger/Soft-Contamination-Prevelance"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/html/2602.12413v1"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"},{"title":"LLM Benchmark Contamination","url":"https://peerlist.io/scroll/post/ACTHDNDNQPJRQ7NOE2AK9JQ8BDRQP9"}]

I found information about the research. Here are the results:

## Overview

The paper "Soft Contamination Means Benchmarks Test Shallow Generalization" was submitted on February 12, 2026, by authors including Ari Spiesberger, Juan J. Vazquez, Nicky Pochinkov, Tomáš Gavenčiak, Peli Grietzer, Gavin Leech, and Nandi Schoots. It is a submission to ICML 2026.

## The Research Focus

The research examines how typical decontamination filters using n-gram matching fail to detect semantic duplicates—sentences with equivalent or near-equivalent content that are not close in string space—and studies this "soft contamination" of training data by semantic duplicates.

## Key Findings

Using the open-data model OLMo3 as a case study, the researchers found semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems in OLMo3's training corpus. Finetuning on semantic duplicates of benchmark data improves performance on those benchmarks, and performance also improves on truly held-out items from the same benchmark, suggesting within-benchmark-distribution generalization rather than genuine capability growth.

## Main Argument

The researchers argue that recent benchmark gains are confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data and effective test data in growing training corpora.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a6d8cdf-5873-4a15-b808-ecf2032df2f9",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "a50bb5ea-08a5-40c3-83d9-47e4747707f4",
  "sourceToolAssistantUUID": "9a6d8cdf-5873-4a15-b808-ecf2032df2f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-29T05:45:48.177Z_

Let me try fetching the LinkedIn discussion and the YouTube video summary for additional community reactions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a50bb5ea-08a5-40c3-83d9-47e4747707f4",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL8rUKdT8F5PWhYFEB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "974422ee-d83e-4c7e-8101-a7f80786754e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdGzCPuU5VnPdAbHS1weWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 18711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 32 · 2026-05-29T05:45:49.603Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018DiS157udaDJCXRHQNCRAP`</summary>

```json
{
  "url": "https://peerlist.io/scroll/post/ACTHDNDNQPJRQ7NOE2AK9JQ8BDRQP9",
  "prompt": "Extract ALL discussion, comments, and opinions about this paper. Include any praise, criticism, or technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "974422ee-d83e-4c7e-8101-a7f80786754e",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL8rUKdT8F5PWhYFEB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "789c9a76-c284-47dd-8b80-0344c87cee9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdGzCPuU5VnPdAbHS1weWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 18711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 33 · 2026-05-29T05:45:49.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GuX9mBnxdkQJ7Pg9oWXSSZ`</summary>

```json
{
  "query": "soft contamination benchmark shallow generalization hacker news discussion comments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789c9a76-c284-47dd-8b80-0344c87cee9a",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL8rUKdT8F5PWhYFEB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fa99851-e1b7-46f7-b7b8-4cd898b09143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdGzCPuU5VnPdAbHS1weWE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 18711,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1899
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 18711,
          "cache_creation_input_tokens": 1899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1899,
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

_source line 34 · 2026-05-29T05:45:49.854Z_

<details><summary>↩ Tool result · `toolu_018DiS157udaDJCXRHQNCRAP`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "789c9a76-c284-47dd-8b80-0344c87cee9a",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "56e91aa2-acc6-4f7c-ba09-99b654945876",
  "sourceToolAssistantUUID": "789c9a76-c284-47dd-8b80-0344c87cee9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-29T05:45:56.907Z_

<details><summary>↩ Tool result · `toolu_01GuX9mBnxdkQJ7Pg9oWXSSZ`</summary>

```text
Web search results for query: "soft contamination benchmark shallow generalization hacker news discussion comments"

Links: [{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization | Hacker News","url":"https://news.ycombinator.com/item?id=47041000"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"},{"title":"[2602.12413] Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/abs/2602.12413"},{"title":"GitHub - AriSpiesberger/Soft-Contamination-Prevelance: Repository for SDTD expirements · GitHub","url":"https://github.com/AriSpiesberger/Soft-Contamination-Prevelance"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/html/2602.12413v1"},{"title":"Soft Contamination Inflates LLM Benchmarks - YouTube","url":"https://www.youtube.com/watch?v=zN1HugYZN30"}]

I found relevant information about this topic. Here's what the search revealed:

## Overview

A new paper investigates how much AI reasoning gains are confounded by expanding the training corpus and how much LLM performance is down to "local" generalization through pattern-matching to hard-to-detect semantically equivalent training data.

## The Paper's Main Findings

The paper "Soft Contamination Means Benchmarks Test Shallow Generalization" examines how if LLM training data is polluted with benchmark test data, benchmark performance gives biased estimates of out-of-distribution generalization.

Typical decontamination filters use n-gram matching which fail to detect 'semantic' duplicates: sentences with equivalent (or near-equivalent) content that are not close in string space.

Key findings include:

- Semantic duplicates are found for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems, and including semantic duplicates of benchmark data in training does improve benchmark performance

- Recent benchmark gains are confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data in growing training corpora

The discussion thread on Hacker News is linked [here](https://news.ycombinator.com/item?id=47041000), and the full research paper is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fa99851-e1b7-46f7-b7b8-4cd898b09143",
  "isSidechain": true,
  "promptId": "2cedb063-669d-4641-bce4-3293b6f798bf",
  "agentId": "a2b8479d348e87f02",
  "type": "user",
  "uuid": "39b81fce-21cb-40f6-9224-433170e7cb4f",
  "sourceToolAssistantUUID": "9fa99851-e1b7-46f7-b7b8-4cd898b09143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-29T05:47:27.189Z_

I now have comprehensive information about the paper. Let me compile the full research report.

---

## Research Report: "Soft Contamination Means Benchmarks Test Shallow Generalization" (Spiesberger et al., 2026)

**Paper**: arXiv:2602.12413, submitted February 12, 2026, ICML 2026 submission
**Authors**: Ari Spiesberger, Juan J. Vazquez, Nicky Pochinkov, Tomas Gavenciak, Peli Grietzer, Gavin Leech, Nandi Schoots
**License**: CC BY 4.0

---

### 1. THE GAP/PROBLEM IDENTIFIED AND HOW THEY DISCOVERED IT

The authors identified a fundamental blind spot in how the AI community validates LLM benchmark progress. LLM training corpora have grown **10,000x since 2020**, and standard decontamination procedures rely on **n-gram matching** to remove test data from training sets. However, this approach systematically misses **semantic duplicates** -- training examples that convey the same meaning/problem as test items but use different surface-level text.

They discovered the scale of the problem by exploiting the fully open-source **OLMo3** model (by AI2), whose entire training pipeline and data are public. By embedding 1% of the pretraining data (Dolma3: 6.0TB, Dolmino: 250GB) and 100% of instruction-tuning data (Dolci3 SFT: 3.08GB, DPO: 811MB, RL: 483MB) using the **llama-embed-nemotron-8b** model (rank #2 on MTEB), they could systematically search for semantic matches against benchmark test sets. The results were striking: despite OLMo3 being a "responsibly decontaminated" model, contamination remained rampant.

---

### 2. KEY INSIGHT THAT OTHERS MISSED

Prior contamination work focused on **item-level memorization** -- does the model recall a specific test example? Spiesberger et al. reframed the problem as one of **shallow generalization**: contamination doesn't just help models on exact items they've seen, it helps them generalize *within the benchmark distribution* without generalizing *out of distribution*. 

The critical insight is that finetuning on semantic duplicates of benchmark items improves performance on **unseen items from the same benchmark** (e.g., ~20 percentage points on MuSR), while showing **zero transfer to related but distinct benchmarks** (e.g., MuSR training does not help on TrueDetective). This means contamination creates an illusion of capability: the model appears to "reason" when it's actually interpolating within a narrow distribution it encountered during training.

Additionally, they showed that mere cosine similarity in embedding space is insufficient -- finetuning on high-cosine-similarity data that are NOT semantic duplicates produces **no benefit**. The effect is specifically tied to semantically equivalent content, not just topical proximity.

---

### 3. HOW THEY FORMULATED THE PROBLEM DIFFERENTLY FROM PRIOR WORK

Prior work (Magar & Schwartz 2022, Yang et al. 2023, Riddell et al. 2024) treated contamination as a binary: either a test item is in the training set or it isn't. Extensions to "near-duplicates" still focused on string-level similarity.

Spiesberger et al. introduced a taxonomy:
- **Exact duplicate**: Syntactically identical (caught by n-gram filters)
- **Semantic duplicate**: Same meaning, different text (missed by n-gram filters)
- **Soft contamination**: Contamination via semantic duplicates
- **Shallow generalization**: Within-distribution generalization + generalization across semantic duplicates (but NOT out-of-distribution transfer)

They also introduced the concept of **ecological validity** for contamination studies. Rather than just showing that contamination *can* affect scores when artificially injected in large quantities, they estimated the *actual contamination rate* in real training data (~4 semantic duplicates per 10,000 training datapoints per benchmark item) and tested whether this realistic rate produces measurable effects. It does: even at ~5% contamination in finetuning data, they observed **12 percentage point gains on seen items** and **5.6 points on unseen items**.

Their key differentiators from prior work:
- **Largest data investigation** to date (1% of multi-TB pretraining + 100% of instruction tuning)
- **Unified framework** treating exact and semantic contamination as forms of shallow generalization
- **First ecologically valid contamination study** with realistic contamination ratios
- **Within-benchmark generalization testing** (not just memorization of specific items)

---

### 4. EXISTING TECHNIQUES THEY ADAPTED, COMBINED, OR SIMPLIFIED

The methodology combines several established techniques in a novel pipeline:

1. **Embedding-based retrieval**: Used llama-embed-nemotron-8b (FP16) to embed all corpus data and benchmark items, then computed cosine similarity to find candidates. This is standard retrieval, but applied at unprecedented scale to contamination detection.

2. **LLM-as-judge annotation**: For candidate matches in the top 0.1% cosine similarity, they used **Gemini-3-flash** to classify whether pairs are semantic duplicates (exact/equivalent/subset/superset). This replaced expensive human annotation.

3. **Stratified reservoir sampling**: To handle the massive corpus size, they preserved the hierarchical source distribution topology when sampling.

4. **LoRA finetuning**: Standard parameter-efficient finetuning (Rank 16, Alpha 32, Dropout 0.05) on OLMo3-7b-Instruct to measure contamination effects. Chain-of-thought reasoning was generated via teacher models (Claude Opus 4.5, GPT-4-mini).

5. **Synthetic semantic duplicate generation**: Different strategies per benchmark:
   - **MBPP**: 5 LLM-generated paraphrases per task + alternative Python implementations (validated via test cases, <0.85 difflib similarity threshold)
   - **MuSR**: 3 levels of semantic variation by manipulating the underlying logic tree (regenerate story, change non-critical branches, change all replaceable branches)
   - **ZebraLogic**: Category substitution ("color" to "shape"), clue shuffling, paraphrasing, and combinations thereof

---

### 5. TECHNICAL METHOD DETAILS

**Detection Pipeline**:
1. Embed corpus data and benchmark items with llama-embed-nemotron-8b
2. Compute pairwise cosine similarity
3. Sample top 0.1% similarity matches (100 samples per benchmark item)
4. Classify via Gemini-3-flash as exact/equivalent/subset/superset duplicate
5. Aggregate contamination rates per benchmark

**Contamination Measurement Protocol**:
- Split synthetic duplicates 50-50: finetune on one half, evaluate on both halves
- "Seen" = items whose duplicates appeared in finetuning
- "Unseen" = items whose duplicates were withheld
- Cross-benchmark evaluation tests out-of-distribution transfer (MuSR -> TrueDetective, ZebraLogic -> ARC Challenge, MBPP -> HumanEval)
- Cosine-similarity control: finetune on high-cosine but non-duplicate data to verify the effect requires semantic equivalence

**Benchmarks chosen** (4 total):
- **MBPP** (257 programming tasks): Expected high contamination, easy to generate alternatives
- **CodeForces** (468 competitive programming problems): Expected moderate contamination
- **MuSR** (250 logic-tree murder mysteries): Expected low contamination (procedurally generated)
- **ZebraLogic** (1000 logic grid puzzles): OLMo3 not saturated (32.9% baseline)

---

### 6. KEY QUANTITATIVE RESULTS

**Contamination Prevalence (in OLMo3's training data)**:
| Benchmark | Contamination Rate | Type |
|-----------|-------------------|------|
| MBPP | **100%** of 257 problems have >= 1 semantic duplicate | Semantic only (no exact) |
| CodeForces | **78%** (77.5%) of 468 problems have >= 1 semantic duplicate | Mixed exact + semantic |
| ZebraLogic | **49.5%** have exact duplicates (70%+ for 4x4+ puzzles) | Exact duplicates found in Dolci-RL |
| MuSR | **0%** -- no semantic duplicates detected (max cosine sim ~0.40) | Clean benchmark |

**Finetuning on Semantic Duplicates (MuSR -- strongest result)**:
- Baseline: 66.0% seen, 28.3% unseen
- With exact duplicates: 87.9% seen (+21.9), 87.3% unseen (+59.0)
- With Level 1 semantic dupes: 85.8% seen (+19.8), 86.2% unseen (+57.9)
- With Level 3 semantic dupes (most transformed): 87.5% seen, 87.9% unseen
- Cross-benchmark (TrueDetective): ~28% throughout -- **zero transfer**
- Cosine-similarity-only control: 68.6% seen, 25.1% unseen -- **no benefit**

**Finetuning on Semantic Duplicates (MBPP)**:
- Baseline: 46.4% seen, 55.3% unseen
- Exact duplicates: 63.0% seen (+16.6), 48.8% unseen (-6.5)
- Semantic duplicates (Python): 55.1% seen (+8.7), 53.6% unseen (-1.7)
- Surprising finding: HumanEval improved by **+11.7 points** (to 67.0%) with semantic duplicates, suggesting some limited cross-task transfer for code

**Finetuning on Semantic Duplicates (ZebraLogic)**:
- Exact duplicates: 48.4% seen (+11.5), 43.4% unseen (-6.7)
- Semantic duplicates showed minimal or negative effects
- Complex transformations (shuffle+substitution+paraphrase) actually harmed performance: 28.0% seen (-8.9)

**Ecologically Valid Contamination (MuSR, 5% contamination rate)**:
- Seen items: **+12.0 points** over clean baseline
- Unseen items: **+5.6 points** over clean baseline
- TrueDetective (cross-benchmark): 28.0% -- stable, no transfer

**ZebraLogic progression through OLMo3 training stages**:
- SFT stage: 18.0%
- DPO stage (no duplicates detected): 28.4% (+10.4)
- RL stage (heavy duplication): 32.9% (+4.5)

---

### 7. COMMUNITY DISCUSSION AND RECEPTION

The paper generated significant community interest, appearing on Hacker News (item #47041000), LinkedIn discussions, YouTube explainer videos, and a GitHub repository. I was unable to retrieve the full Hacker News comment thread (HTTP 429), and no OpenReview reviews were found (the paper appears to be an ICML 2026 submission but the review page was not publicly indexed at the time of search).

**From what could be gathered**:
- The paper was noted as an ICML 2026 submission
- Community discussions highlighted the implications for benchmark reliability
- The 78% CodeForces and 50% ZebraLogic findings were cited as particularly alarming
- There is a companion GitHub repository (AriSpiesberger/Soft-Contamination-Prevelance) with experimental code

No formal reviewer comments from OpenReview could be retrieved, so I cannot report on what was praised vs. criticized in peer review.

---

### 8. STATED LIMITATIONS

1. **Likely underestimation**: High false-negative rate in semantic duplicate detection; they only sampled 1% of pretraining data, so true contamination rates are probably higher
2. **Open-source only**: Only OLMo3 was fully analyzed; frontier models (e.g., Llama 4 with 30T tokens) use vastly larger corpora with potentially different contamination profiles
3. **Synthetic duplicate quality**: The generated semantic duplicates may not perfectly mirror naturally occurring contamination
4. **Philosophical objection acknowledged**: Some argue in-distribution performance on all tasks is itself a valid goal, not requiring OOD generalization
5. **Inconsistent generalization effects**: Strong within-benchmark generalization in the high-contamination setup (Section 4.3) but weaker in the ecologically valid setup (Section 4.4), requiring further investigation
6. **Benchmark-specific effects**: ZebraLogic showed minimal semantic duplicate effects while MuSR showed dramatic effects, suggesting the phenomenon is task-dependent

---

### Summary Assessment

This paper makes a compelling empirical case that benchmark contamination is far more pervasive than previously recognized, because standard n-gram decontamination misses semantic duplicates entirely. The most provocative finding is the asymmetry between within-benchmark generalization (strong) and cross-benchmark transfer (absent), which they term "shallow generalization." The 78% CodeForces contamination rate is particularly striking because it was found despite AI2's decontamination efforts, and only 1% of pretraining data was even searched. The work's main methodological contribution is the ecologically valid experimental design showing that realistic contamination ratios (not just artificial flooding) produce measurable benchmark inflation.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2602.12413)
- [arXiv HTML Full Paper](https://arxiv.org/html/2602.12413)
- [arXiv PDF](https://arxiv.org/pdf/2602.12413)
- [GitHub Repository](https://github.com/AriSpiesberger/Soft-Contamination-Prevelance)
- [Hacker News Discussion](https://news.ycombinator.com/item?id=47041000)
- [YouTube Explainer](https://www.youtube.com/watch?v=zN1HugYZN30)
- [LinkedIn Discussion](https://www.linkedin.com/posts/charlesmartin14_%F0%9D%90%92%F0%9D%90%A8%F0%9D%90%9F%F0%9D%90%AD-%F0%9D%90%82%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%AD%F0%9D%90%9A%F0%9D%90%A6%F0%9D%90%A2%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%A7-%F0%9D%90%8C%F0%9D%90%9E%F0%9D%90%9A%F0%9D%90%A7%F0%9D%90%AC-activity-7429255693205045249-KwM0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39b81fce-21cb-40f6-9224-433170e7cb4f",
  "isSidechain": true,
  "agentId": "a2b8479d348e87f02",
  "requestId": "req_011CbWL9kkKLXAFXJNhJhQCP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed465c10-a7bb-4ab9-8791-fe42a8258f03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "257f41c8-db0b-4478-8965-67d0a340e5ab",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013U6SndXp6NW2c5r5QTVGqr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 20610,
      "output_tokens": 3709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 929
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3709,
          "cache_read_input_tokens": 20610,
          "cache_creation_input_tokens": 929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 929,
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
