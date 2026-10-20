# Research conversation: I need to research MathAtlas (arXiv:2605.14061, May 2026), described as the first large-scale autoformalization benchmar

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8e91c0fc33459163.jsonl`
- **Structured JSON:** [`598846c352c1a007095e.json`](../../sessions/59/598846c352c1a007095e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-27T23:04:48.520Z_

I need to research MathAtlas (arXiv:2605.14061, May 2026), described as the first large-scale autoformalization benchmark of graduate-level math (~52k theorems from 103 textbooks, achieving at most 9.8% correctness).

Please:
1. Search the web for "MathAtlas arXiv 2605.14061 autoformalization benchmark"
2. Fetch the arXiv abstract page at https://arxiv.org/abs/2605.14061
3. Search for "MathAtlas large-scale autoformalization graduate math"
4. Try to get details from the paper

Key questions:
- What exactly does MathAtlas contain? (size, scope, domains)
- What correctness metrics were used?
- Which models were evaluated and what were the results?
- How does it compare to existing benchmarks like ProofNet and FormalMATH-Lite?
- Any insights about reward design or evaluation for autoformalization?

Be thorough - read actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "d5d597d3-0b5a-41d3-9b8d-c05c67ade6fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T23:04:48.523Z_

```json
{
  "parentUuid": "d5d597d3-0b5a-41d3-9b8d-c05c67ade6fe",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
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
  "uuid": "b985e75e-978f-4df5-bdc7-0c4594d2fd0f",
  "timestamp": "2026-05-27T23:04:48.523Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T23:04:48.523Z_

```json
{
  "parentUuid": "b985e75e-978f-4df5-bdc7-0c4594d2fd0f",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "98db9d35-92f6-4f0f-8623-12d80f14f451",
  "timestamp": "2026-05-27T23:04:48.523Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T23:04:51.188Z_



I'll research MathAtlas thoroughly by searching the web and fetching the arXiv page in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98db9d35-92f6-4f0f-8623-12d80f14f451",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTukevNuX1DNcP9M7sgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e59a214-e5ad-44ac-895a-9443e680d1ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lmy8DgA7gkppvY7dsDWjTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1568,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-27T23:04:51.329Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U1QtZJv9HCwDBsuy2Kndwt`</summary>

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
  "parentUuid": "7e59a214-e5ad-44ac-895a-9443e680d1ab",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTukevNuX1DNcP9M7sgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "519eb1db-b042-4fbc-beea-517cfd1f57ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lmy8DgA7gkppvY7dsDWjTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1568,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 6 · 2026-05-27T23:04:51.332Z_

<details><summary>↩ Tool result · `toolu_01U1QtZJv9HCwDBsuy2Kndwt`</summary>

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
  "parentUuid": "519eb1db-b042-4fbc-beea-517cfd1f57ee",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "77f7b0a8-f6f1-4de7-84a9-450d3fb9de62",
  "sourceToolAssistantUUID": "519eb1db-b042-4fbc-beea-517cfd1f57ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T23:04:54.807Z_



Now let me run all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77f7b0a8-f6f1-4de7-84a9-450d3fb9de62",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTuktMXG8PX3xXPjteKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "764cbdac-cdfb-419b-842f-0564cef793f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4airJxnKd68iS7kLxG8Ty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-27T23:04:54.808Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011HuNB9sQeT8FqrRdm2o8fd`</summary>

```json
{
  "query": "MathAtlas arXiv 2605.14061 autoformalization benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "764cbdac-cdfb-419b-842f-0564cef793f1",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTuktMXG8PX3xXPjteKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2357877a-3b56-4d2e-b711-38e07c048204",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4airJxnKd68iS7kLxG8Ty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-27T23:04:55.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DQk66178muQXrZroGVYrBE`</summary>

```json
{
  "query": "MathAtlas large-scale autoformalization graduate math 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2357877a-3b56-4d2e-b711-38e07c048204",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTuktMXG8PX3xXPjteKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3347048d-f985-41fa-a5d6-9f2deb56952a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4airJxnKd68iS7kLxG8Ty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 10 · 2026-05-27T23:04:57.090Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C5UxSzx8XRbpSwxeoPhGrE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.14061",
  "prompt": "Extract ALL details from this arXiv abstract page about the MathAtlas paper. I need: full title, all authors, complete abstract text, submission date, subject categories, and any other metadata. Be thorough and include every detail on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3347048d-f985-41fa-a5d6-9f2deb56952a",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTuktMXG8PX3xXPjteKZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5651a92c-ccc0-4a90-89a6-3650fe0bd7b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4airJxnKd68iS7kLxG8Ty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 8979,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 8979,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-27T23:05:00.754Z_

<details><summary>↩ Tool result · `toolu_011HuNB9sQeT8FqrRdm2o8fd`</summary>

```text
Web search results for query: "MathAtlas arXiv 2605.14061 autoformalization benchmark"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"Autoformalization with Large Language Models","url":"https://arxiv.org/pdf/2205.12615"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"Autoformalizing Euclidean Geometry","url":"https://arxiv.org/pdf/2405.17216"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

Based on the search results, here's what I found about MathAtlas (arXiv 2605.14061):

## Overview

MathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

## Key Features

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

## Motivation

Current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored.

## Performance Results

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. The paper also shows that performance degrades substantially with dependency depth.

The paper was submitted to arXiv on May 13, 2026, and comes from researchers at the University of California, Santa Cruz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2357877a-3b56-4d2e-b711-38e07c048204",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "a29d1999-2332-48dd-a0ef-fd81659d54d6",
  "sourceToolAssistantUUID": "2357877a-3b56-4d2e-b711-38e07c048204",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T23:05:01.778Z_

<details><summary>↩ Tool result · `toolu_01C5UxSzx8XRbpSwxeoPhGrE`</summary>

```text
# MathAtlas Paper Details

**Full Title:** "MathAtlas: A Benchmark for Autoformalization in the Wild"

**Authors:** Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, Jeffrey Flanigan

**Submission Date:** May 13, 2026

**arXiv Identifier:** 2605.14061

**Subject Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

**Abstract Summary:** The paper presents the inaugural large-scale benchmark for converting informal graduate-level mathematics into formal notation. It comprises approximately 52,000 mathematical entities sourced from 103 graduate textbooks, plus a dependency graph containing roughly 178,000 relationships. Testing shows even leading models achieve modest performance: "at most 9.8% correctness on theorem statements and 16.7% on definitions." The MA-Hard subset, containing 700 deeply nested entities, proves exceptionally difficult.

**Status:** Submitted to NeurIPS 2026

**DOI:** https://doi.org/10.48550/arXiv.2605.14061

**License:** Creative Commons Attribution 4.0

**Available Formats:** PDF, HTML (experimental), TeX source
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5651a92c-ccc0-4a90-89a6-3650fe0bd7b5",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "401d7786-2f69-4c07-a4bc-2303bb34b0d2",
  "sourceToolAssistantUUID": "5651a92c-ccc0-4a90-89a6-3650fe0bd7b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T23:05:02.101Z_

<details><summary>↩ Tool result · `toolu_01DQk66178muQXrZroGVYrBE`</summary>

```text
Web search results for query: "MathAtlas large-scale autoformalization graduate math 2026"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"(PDF) ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://www.researchgate.net/publication/388883482_ATLAS_Autoformalizing_Theorems_through_Lifting_Augmentation_and_Synthesis_of_Data"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://arxiv.org/pdf/2502.05567"},{"title":"Patrick Shafto: Autoformalization and the future of math and science - YouTube","url":"https://www.youtube.com/watch?v=ZMO3xy1bayE"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"}]

Based on the search results, here's what I found about MathAtlas:

## MathAtlas Overview

MathAtlas is a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild. It is the first large-scale autoformalization benchmark of graduate-level mathematics, containing approximately 52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

## Key Features

MathAtlas is enriched with a mathematical dependency graph containing approximately 178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.

## Benchmark Difficulty

MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. The strongest baseline has only 2.6% overall correctness on MA-Hard, a subset of 700 entities with the deepest dependency trees.

The benchmark was published in May 2026 and represents an important advancement in autoformalization research by focusing on graduate-level mathematics, which had previously been underexplored in this field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3347048d-f985-41fa-a5d6-9f2deb56952a",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "d57b83a0-7633-4ea8-b37f-e09db782b8e9",
  "sourceToolAssistantUUID": "3347048d-f985-41fa-a5d6-9f2deb56952a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T23:05:08.799Z_

Good, I have the basic overview. Now let me fetch the full HTML paper to get detailed content about methodology, metrics, model evaluations, and comparisons.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d57b83a0-7633-4ea8-b37f-e09db782b8e9",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTumf1cZdBioYYNL3GPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "430ea7c3-4663-43d3-95f9-2852e358a291",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PY6imAyQaVsZ84dd9AU5gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 347,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 10105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1476,
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

_source line 15 · 2026-05-27T23:05:13.535Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MAKRSY7rwywUdCK4sYAakM`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.14061",
  "prompt": "Extract ALL detailed information from this paper. I need:\n\n1. DATASET DETAILS: Exact size, what types of entities are included (theorems, definitions, exercises, etc.), how many of each type, how textbooks were selected, which 87 math domains are covered, how extraction was done.\n\n2. DEPENDENCY GRAPH: How was the dependency graph constructed? What are the ~178k relations? What is dependency depth and how is it measured?\n\n3. EVALUATION METRICS: What correctness metrics are used? How is correctness defined for autoformalization? Any details on type-checking, semantic equivalence, or other evaluation methods.\n\n4. MODEL EVALUATIONS: Which specific models were tested (names and versions)? What were the exact numerical results for each model on each task? Include all numbers from tables.\n\n5. MA-HARD SUBSET: How was it defined? What are the results on it?\n\n6. COMPARISON TO EXISTING BENCHMARKS: How does MathAtlas compare to ProofNet, FormalMATH-Lite, miniF2F, and other benchmarks? Include any comparison tables.\n\n7. REWARD DESIGN / EVALUATION INSIGHTS: Any discussion of reward signals, RLHF, evaluation challenges for autoformalization.\n\n8. KEY FINDINGS AND CONCLUSIONS: Main takeaways, limitations, future work.\n\nBe extremely thorough - include all numbers, table data, and specific details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "430ea7c3-4663-43d3-95f9-2852e358a291",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTumf1cZdBioYYNL3GPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "069c9fab-ff54-451d-9ed7-338419767079",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PY6imAyQaVsZ84dd9AU5gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 347,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 10105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1476,
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

_source line 16 · 2026-05-27T23:05:13.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VvA6j4ZwuWTXE9TaSUyLYi`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization models evaluated results correctness Lean4 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "069c9fab-ff54-451d-9ed7-338419767079",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTumf1cZdBioYYNL3GPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f36ca7d8-8232-49d1-95b2-546a29427618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PY6imAyQaVsZ84dd9AU5gr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 347,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 10105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1476,
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

_source line 17 · 2026-05-27T23:05:14.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFSKkS2CX5hFPUScJSZuTn`</summary>

```json
{
  "query": "MathAtlas autoformalization dependency graph MA-Hard ProofNet comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36ca7d8-8232-49d1-95b2-546a29427618",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTumf1cZdBioYYNL3GPu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f29d094b-d9f8-401c-b9b0-98b4e9cd074a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PY6imAyQaVsZ84dd9AU5gr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 347,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 10105,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 347,
          "output_tokens": 534,
          "cache_read_input_tokens": 10105,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1476,
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

_source line 18 · 2026-05-27T23:05:20.942Z_

<details><summary>↩ Tool result · `toolu_01TFSKkS2CX5hFPUScJSZuTn`</summary>

```text
Web search results for query: "MathAtlas autoformalization dependency graph MA-Hard ProofNet comparison"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"towards a faithful metric and a dependency retrieval","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/abs/2510.15981"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"}]

Based on the search results, here's what I found about these autoformalization systems:

## MathAtlas

MathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

## MA-Hard Subset

MA-Hard is a subset of 700 entities from MathAtlas where performance of state-of-the-art models degrades substantially with dependency depth. Overall, MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions.

## Comparison with ProofNet

Current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored. ProofNet is referenced in the research as an existing undergraduate-level benchmark, indicating that MathAtlas addresses a gap by focusing on graduate-level mathematics that ProofNet does not cover.

The key distinction is that MathAtlas uniquely incorporates dependency graph information to support development of dependency-aware formalization systems, which sets it apart from previous benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f29d094b-d9f8-401c-b9b0-98b4e9cd074a",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "33db8e0f-47d2-4584-a5d6-7f1b3de59bc2",
  "sourceToolAssistantUUID": "f29d094b-d9f8-401c-b9b0-98b4e9cd074a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T23:05:21.078Z_

<details><summary>↩ Tool result · `toolu_01VvA6j4ZwuWTXE9TaSUyLYi`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization models evaluated results correctness Lean4 2026"

Links: [{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/html/2406.06555v1"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4 | OpenReview","url":"https://openreview.net/forum?id=22ITxc8y5p"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"[2406.06555] An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/abs/2406.06555"}]

Based on the search results, here are the key findings about the MathAtlas benchmark and autoformalization models:

## MathAtlas Benchmark Overview

MathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations.

## Evaluation Results and Correctness

The benchmark demonstrates that autoformalization is extremely challenging for current models. Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. 

Performance degrades significantly with increased complexity: On MA-Hard, a subset of 700 entities with the deepest dependency trees, the best model achieves only 2.6% correctness for autoformalization.

## Related Lean4 Evaluation Work

Separate from MathAtlas, another recent study evaluated autoformalization capabilities in Lean4. That benchmark included 101 pairs of mathematical formal-informal statements across 17 different topics in math, with evaluation of GPT-3.5, GPT-4, and Gemini Pro. Autoformalizations were evaluated on a 0-4 scale based on correction effort, referring to the amount of necessary adjustments required to transform the generated formalization output into an accurate and fully correct Lean4 formalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f36ca7d8-8232-49d1-95b2-546a29427618",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "eeb8185f-40c2-4f34-89a7-ddf9e501f47b",
  "sourceToolAssistantUUID": "f36ca7d8-8232-49d1-95b2-546a29427618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T23:05:36.517Z_

<details><summary>↩ Tool result · `toolu_01MAKRSY7rwywUdCK4sYAakM`</summary>

```text
# MathAtlas: Comprehensive Paper Analysis

## 1. DATASET DETAILS

**Overall Size & Composition:**
- Total: ~52,052 entities from 103 graduate mathematics textbooks
- Distribution: ~18k theorems, ~10k exercises, ~10k definitions, ~10k proofs, ~55k examples
- Coverage: 87 distinct mathematical fields/subfields

**Entity Types & Characteristics:**
The dataset includes definitions, theorems, examples, exercises, and proofs. Approximately 90% of entities contain at least one object reference (mathematical concept dependency). Each entity can contain multiple formalizable items—e.g., a single definition might introduce two distinct mathematical objects requiring separate formal definitions.

**Textbook Selection & Extraction:**
PDFs were converted to Mathematical Markdown (MMD) using Nougat, then filtered to remove metadata. A few-shot prompted gpt-oss-120b identified entity spans and types. The pipeline extracted 193k object references (~3.69 per entity) and 17k entity references, with 83.7% of object references successfully matched to defining entities.

**Quality Assurance:**
"90.4% of the annotated entities are correctly extracted" across 250 sampled entities (50 per type). Reference extraction achieved 96% accuracy on 100 sampled references.

## 2. DEPENDENCY GRAPH

**Construction & Relations:**
The graph contains ~178k relations of three types: entity references (one entity referencing another), object references (linking concepts to their definitions), and "proves" relations (connecting proofs to theorems).

**Dependency Metrics:**
- Dependency depth: maximum height of an entity's dependency tree (range: 0–80, mean: 30, median: 17)
- Dependency mass: total unique nodes in a dependency tree
- Field variation: Lie algebra/quantum groups averaged ~50 depth; set theory/logic averaged ~6

**Grounding in Mathlib:**
Using LeanSearch, "27.9% of definitions which our linker grounded in Mathlib are correctly formalized, whereas only 16.8% of missing definitions are correct" (p<0.001 statistically significant).

## 3. EVALUATION METRICS

**Correctness Definition:**
"A formal statement must both compile and be faithful to the informal statement for it to be considered correct." This combines:
- **Compile rate:** syntactic correctness verified with the blv tool against Lean v4.24.0
- **Semantic faithfulness:** whether formal and informal statements have equivalent mathematical meaning

**Semantic Faithfulness:**
The authors introduce MA-Align, a 200-entity benchmark with binary "aligned"/"misaligned" labels. They evaluate CriticLean (14B and 32B variants) and LLM-as-judge systems using prompts from prior work (ReForm) and novel engineered prompts.

## 4. MODEL EVALUATIONS

**Fine-tuned Models (Statements Only):**
- Herald 7B: 1.5% correctness
- Kimina 7B: 2.3% correctness
- ATLAS-L 8B: 3.5% correctness
- Goedel 8B: 7.1% correctness
- Goedel 32B: 7.1% correctness
- ReForm 8B: 9.8% correctness (best fine-tuned)

**Prompted Models (Definitions):**
- gpt-oss-20b zero-shot: 2.2% correctness
- gpt-oss-120b with tuned examples: 16.7% correctness (best)

**Prompted Models (Statements):**
- gpt-oss-20b zero-shot: 4.2% correctness
- gpt-oss-120b with tuned examples: 7.8% correctness

**Semantic Faithfulness (Table 2):**
On MA-Align definitions: CriticLean 32B achieved 80.0%; on MA-Align statements: 75.0%. The proprietary gpt-5.2 with engineered prompts reached 86.0% (definitions) and 80.0% (statements).

## 5. MA-HARD SUBSET

**Definition:**
MA-Hard comprises ~700 entities with the deepest dependency trees, primarily from advanced fields (algebraic geometry, Lie theory) spanning 14 subjects. It includes ~600 statements and ~100 definitions.

**Results:**
"On MA-Hard, the best model achieves only 2.6% correctness for autoformalization on this challenging dataset." The strongest prompted model (gpt-oss-120b) achieved 14.6% compilation but only 2.6% correctness overall.

## 6. COMPARISON TO EXISTING BENCHMARKS

**Scope Expansion:**
Unlike ProofNet (undergraduate), MiniF2F (olympiad), and FATE-H/X (100 algebra problems), MathAtlas provides 52k graduate-level entities spanning 87 fields. Prior benchmarks focused primarily on theorem statements; MathAtlas includes definitions, a significant gap.

**Dependency Graph Innovation:**
"MathAtlas is the first large-scale, in the wild autoformalization benchmark" with rich contextual and dependency data. Previous benchmarks lacked dependency annotations, making it impossible to study prerequisite-aware autoformalization systematically.

**Semantic Faithfulness Benchmarking:**
MA-Align is "the first [benchmark] to include both labeled examples of theorem statements and definitions, and covers a wide variety of mathematics at the graduate level," whereas ConsistencyCheck and CriticLeanBench focus on simpler domains.

## 7. REWARD DESIGN & EVALUATION INSIGHTS

**Local Context Challenge:**
Including 300 tokens of local context "decreases system performance from 20.3% to 17.4% on definitions, and 10.5% to 8.6% on statements for the best model," indicating that naive context incorporation confuses LLMs. The authors note this highlights the need for better dependency-aware retrieval.

**Compilation vs. Faithfulness Gap:**
Fine-tuned models exhibited dramatic gaps: "Kimina 7B... achieves 27.3% compilation rate, but just 2.3% of formalizations compile and are faithful," suggesting that syntactic correctness alone is insufficient and models struggle with semantic alignment.

**Dependency Depth Correlation:**
A Kolmogorov–Smirnov test confirmed "significant difference between the max depth distributions for correct and incorrect examples (p<0.001)," establishing that deeper dependencies substantially degrade performance.

## 8. KEY FINDINGS & CONCLUSIONS

**Main Takeaways:**
1. Graduate-level autoformalization remains extremely challenging, with best models achieving only 9.8–16.7% correctness
2. Dependency depth is a critical difficulty factor; performance degrades significantly on MA-Hard (2.6% correctness)
3. Existing Mathlib coverage is a major advantage; grounded definitions are 1.66× more likely to formalize correctly
4. Definition autoformalization is underexplored; no prior fine-tuned methods generalize from theorem to definition tasks

**Limitations:**
The benchmark focuses on graduate (not research-level) mathematics. Approximately 30% of entities come from Springer textbooks (released only as generation code for copyright compliance). The authors leave proof formalization and full-theorem proving to future work.

**Future Directions:**
The paper emphasizes the need for "dependency-aware autoformalization systems" and better semantic faithfulness metrics that generalize beyond olympiad/undergraduate domains to graduate mathematics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "069c9fab-ff54-451d-9ed7-338419767079",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "a20f266e-8653-4e84-ad4b-a56dea68ce68",
  "sourceToolAssistantUUID": "069c9fab-ff54-451d-9ed7-338419767079",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T23:05:39.173Z_

Let me get more details from the paper, particularly about the specific comparison tables and the extraction pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a20f266e-8653-4e84-ad4b-a56dea68ce68",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTupCAujJmiCpeV6hZGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c796c47a-9985-4a7b-a242-e30e41e318f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152iLDo5rS3QbAKg6dQ7vg4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1312,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 11581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 22 · 2026-05-27T23:05:47.647Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RpqFUjRk1J49TETv55KvNv`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.14061",
  "prompt": "I need very specific details from this paper that I haven't yet captured. Please extract:\n\n1. TABLE 1: The full comparison table between MathAtlas and other benchmarks (ProofNet, miniF2F, FormalMATH-Lite, FATE, etc.). Include all columns and rows with exact numbers.\n\n2. TABLE 3 or any table showing per-model results: The full results table with compilation rates AND correctness rates for ALL models tested. Include Herald 7B, Kimina 7B, ATLAS-L 8B, Goedel 8B, Goedel 32B, ReForm 8B, and any prompted models (gpt-oss-20b, gpt-oss-120b). Show both zero-shot and few-shot results if available.\n\n3. SPECIFIC MATH DOMAINS: List as many of the 87 mathematical areas as mentioned in the paper.\n\n4. MA-ALIGN details: How exactly was the semantic faithfulness evaluation done? What prompts were used? What were the inter-annotator agreement numbers?\n\n5. LOCAL CONTEXT EXPERIMENTS: Full details on the context ablation experiments - what contexts were tried, what were the exact numbers?\n\n6. Any discussion of REWARD SIGNALS for training autoformalization models, or insights about how compilation-based rewards fail.\n\n7. The EXTRACTION PIPELINE details: How Nougat was used, how gpt-oss-120b was prompted, entity boundary detection accuracy, reference linking accuracy.\n\n8. Any ABLATION STUDIES or additional experiments not in the main results.\n\nBe as specific and numerical as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c796c47a-9985-4a7b-a242-e30e41e318f8",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTupCAujJmiCpeV6hZGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2d4323c-47cb-4372-89e0-0f3f43820cf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152iLDo5rS3QbAKg6dQ7vg4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1312,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 11581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 23 · 2026-05-27T23:05:48.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0137iDbDqdwsYyzCUTYXuxvC`</summary>

```json
{
  "query": "\"MathAtlas\" autoformalization \"gpt-oss\" \"ReForm\" \"Goedel\" correctness compilation results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d4323c-47cb-4372-89e0-0f3f43820cf7",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTupCAujJmiCpeV6hZGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7854a26-4fb5-437e-8107-eeb95044d842",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152iLDo5rS3QbAKg6dQ7vg4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1312,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 11581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2672,
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

_source line 24 · 2026-05-27T23:05:56.417Z_

<details><summary>↩ Tool result · `toolu_0137iDbDqdwsYyzCUTYXuxvC`</summary>

```text
Web search results for query: ""MathAtlas" autoformalization "gpt-oss" "ReForm" "Goedel" correctness compilation results"

Links: [{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/html/2510.24592"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"[2510.24592] ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/abs/2510.24592"},{"title":"Autoformalizing Mathematical Statements by Symbolic ...","url":"https://openreview.net/pdf?id=8ihVBYpMV4"},{"title":"Towards Autoformalization of Mathematics and Code Correctness:   Experiments with Elementary Proofs","url":"https://arxiv.org/pdf/2301.02195"}]

Based on the search results, I found relevant information about the MathAtlas benchmark and autoformalization results. Here's what the research shows:

## MathAtlas Benchmark Overview

MathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations.

## Compilation and Correctness Results

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. More specifically:

- On the statement split, the strongest baseline is ReForm 8B, which achieved an overall correctness of 9.8%.
- On the definition split, gpt-oss-120b achieved 16.7% correctness, with a significant 11.8% gap between compilation rate and overall correctness.

## Performance on Harder Subsets

On MA-Hard, a significant challenge subset, the strongest model achieved only 2.6% correctness.

## ReForm and Semantic Consistency

ReForm-8B surpasses the strongest baseline Goedel-FormalizerV2-8B by an average of +14.8pp in semantic consistency while improving syntactic correctness (+8.2pp). The evaluation metrics consider syntactic correctness (whether the formal statement passes Lean compiler verification) and semantic consistency (whether the statement is both syntactically correct and semantically faithful).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7854a26-4fb5-437e-8107-eeb95044d842",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "fee55785-c717-4165-9a5f-616ce2811729",
  "sourceToolAssistantUUID": "d7854a26-4fb5-437e-8107-eeb95044d842",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T23:06:01.308Z_

<details><summary>↩ Tool result · `toolu_01RpqFUjRk1J49TETv55KvNv`</summary>

```text
# MathAtlas: Detailed Extraction

## 1. TABLE 1: Benchmark Comparison

The paper does not include a direct comparison table between MathAtlas and other benchmarks (ProofNet, miniF2F, etc.). However, it provides these characterizations:

- **MathAtlas**: ~52k entities from 103 graduate textbooks, 87 mathematical areas, ~178k dependency relations
- **ProofNet**: Undergraduate-level mathematics
- **miniF2F**: Olympiad-level mathematics
- **FATE benchmarks**: 100 problems from commutative/abstract algebra

## 2. TABLE 3: Full Model Results

**Definitions (Table 3a):**
- gpt-oss-20b zero-shot: 10.5% compiles, 20.9% faithful, 2.2% correct
- gpt-oss-120b with tuned examples: 28.5% compiles, 58.5% faithful, 16.7% correct

**Statements (Table 3b):**
- Herald 7B: 11.8% compiles, 12.7% faithful, 1.5% correct
- Kimina 7B: 27.3% compiles, 8.4% faithful, 2.3% correct
- ATLAS-L 8B: 21.4% compiles, 16.4% faithful, 3.5% correct
- Goedel 8B: 20.3% compiles, 34.9% faithful, 7.1% correct
- ReForm 8B: 19.0% compiles, 48.4% faithful, 9.8% correct (strongest)
- gpt-oss-120b with tuned examples: 21.7% compiles, 35.9% faithful, 7.8% correct

## 3. Mathematical Domains (87 Areas)

Explicitly mentioned: "real analysis, differential geometry, category theory, topology, quantum groups, Lie algebra, set theory, logic, algebraic geometry, commutative algebra, abstract algebra, probability, quantum theory, number theory"

The paper states coverage spans "87 fields and subfields" but does not enumerate all 87.

## 4. MA-Align Evaluation Details

- **Composition**: 200 syntactically correct statements formalized by gpt-oss-120b
- **Annotation**: Binary labels ("aligned" or "misaligned")
- **Evaluation**: "We selectively sample 200 such entities to better balance the label distribution"
- **Results (Table 2)**: 
  - CriticLean (32B): 80.0% definitions, 75.0% statements
  - gpt-5.2 with few-shot: 86.0% definitions, 80.0% statements
- **Inter-annotator agreement**: Not explicitly reported

## 5. Local Context Experiments

From Section 4.3, "Added Local Context":

- **Method**: "500 tokens in the context window" (later stated as "300 tokens")
- **Definitions result**: Performance decreased from 20.3% to 17.4% correctness
- **Statements result**: Performance decreased from 10.5% to 8.6% correctness
- **Interpretation**: "Including 300 tokens of local context seems to confuse prompted systems"

## 6. Reward Signals Discussion

The paper does not discuss reward signals for training autoformalization models explicitly. However, it observes a notable gap between compilation and correctness: "We note the disparity between compilation rate and correctness...Kimina 7B, for example, achieves 27.3% compilation rate, but just 2.3% of formalizations compile and are faithful."

## 7. Extraction Pipeline Details

- **PDF-to-Markdown**: Nougat conversion with filtering of metadata pages
- **Entity Extraction**: "Few-shot, prompt-engineered gpt-oss-120b" with JSON schema and structured decoding, temperature 0.3
- **Reference Extraction**: Prompted gpt-oss-120b identifying object, entity, and local variable references
- **Quality Metrics (Table 1b)**: Overall 90.4% valid entities; definitions 98.0%, proofs 80.0%
- **Reference Extraction Quality (Table 1a)**: 94.8% F1 score overall (entity refs 94.7%, object refs 94.9%)

## 8. Ablation Studies

**Prompt Engineering Ablations (Statement formalization):**
- Zero-shot baseline: 14.3% (gpt-oss-120b)
- +Few-shot examples: 16.8%
- +Tuned prompt: 17.1%
- +Tuned examples: 21.7%

**Definition-Specific Observation**: "We are unable to evaluate some prior definition autoformalization methods such as ARIA or LoC-Decomp due to unreleased code." Fine-tuned theorem methods failed to generalize to definitions.

**Dependency Depth Analysis**: "We compute a two-sample Kolmogorov–Smirnov, and find significant difference between the max depth distributions for correct and incorrect examples (p<0.001)."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d4323c-47cb-4372-89e0-0f3f43820cf7",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "f58bfb88-8503-4bdc-b2c4-e75e280e3d02",
  "sourceToolAssistantUUID": "d2d4323c-47cb-4372-89e0-0f3f43820cf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-27T23:06:03.936Z_

Let me get one more round of details, specifically about the Mathlib grounding analysis and the Lean verification setup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f58bfb88-8503-4bdc-b2c4-e75e280e3d02",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTur29DTo8xMX5YebL9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ebac91-f33e-47d8-8703-a4e1d95c1db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehe1xnZW7vA1VZS1GXxnRo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 14253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3097,
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

_source line 27 · 2026-05-27T23:06:13.256Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QHocRoHTBte3Nqnj65NnUf`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.14061",
  "prompt": "I need the following SPECIFIC details from this paper that I am still missing:\n\n1. LEAN VERSION AND SETUP: What exact version of Lean 4 was used? What tool was used for compilation checking (blv)? How was compilation checking done at scale?\n\n2. MATHLIB GROUNDING: The paper mentions using LeanSearch to ground definitions in Mathlib. What percentage of definitions were grounded? What was the exact comparison (27.9% vs 16.8%)? Any more details on this analysis?\n\n3. GOEDEL 32B results: Were Goedel 32B results reported? What were they exactly?\n\n4. TABLE comparing all benchmarks: Is there a table (Table 4 or similar) that compares MathAtlas size, level, language, dependency info against ProofNet, miniF2F, FormalMATH-Lite, FATE-H, FATE-X, ConsistencyCheck, etc.?\n\n5. PROMPT ENGINEERING: What specific prompts were used for the few-shot and tuned prompts? How were examples selected?\n\n6. TEXTBOOK SOURCES: Are specific textbooks named? What publishers? What is the copyright approach (mentioned code release for Springer)?\n\n7. The DEPENDENCY DEPTH ANALYSIS: Is there a figure or table showing how correctness degrades with depth? What are the specific numbers at different depth levels?\n\n8. FUTURE WORK: What specific directions do the authors propose? Dependency-aware systems, proof formalization, etc.?\n\n9. Any mention of FormalMATH-Lite specifically?\n\n10. Details about the 'blv' compilation tool - what is it and how does it work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ebac91-f33e-47d8-8703-a4e1d95c1db6",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTur29DTo8xMX5YebL9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "493c3c53-011c-4b08-8527-2f3b55f34cb3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehe1xnZW7vA1VZS1GXxnRo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 14253,
      "output_tokens": 489,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 489,
          "cache_read_input_tokens": 14253,
          "cache_creation_input_tokens": 3097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3097,
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

_source line 28 · 2026-05-27T23:06:22.480Z_

<details><summary>↩ Tool result · `toolu_01QHocRoHTBte3Nqnj65NnUf`</summary>

```text
# MathAtlas Paper: Missing Details Analysis

I'll address each requested detail based on the provided content:

## 1. LEAN VERSION AND SETUP
The paper specifies: **Lean v4.24.0** was used. The compilation tool **blv** (referenced as `github.com/offendo/blv`) was employed. No details on scale or distribution methods are provided in the visible sections.

## 2. MATHLIB GROUNDING
- **27.9%** of definitions grounded in Mathlib were correctly formalized
- **16.8%** of missing definitions achieved correctness
- This difference was statistically significant (chi-square p<0.001)
- LeanSearch retrieved 10 candidates; gpt-oss-120b selected matches

## 3. GOEDEL 32B RESULTS
Yes, reported in Table 3(b): **23.2% compile rate, 30.6% faithful, 7.1% correct** on statements.

## 4. BENCHMARK COMPARISON TABLE
No comprehensive cross-benchmark table comparing MathAtlas to ProofNet, miniF2F, FATE-H, etc. is visible in provided sections. The related work discusses these separately but lacks consolidated metrics.

## 5. PROMPT ENGINEERING
The Appendix B shows: zero-shot prompts from prior work; few-shot used LeanWorkbook examples; "engineered prompt" provided detailed instructions; "tuned examples" selected graduate-level instances. Specific prompts are downloadable but full text isn't in the excerpt.

## 6. TEXTBOOK SOURCES
~30% extracted from **Springer textbooks** (code-release only for copyright compliance). Remaining 70% publicly released. Covers **87 mathematical fields** across **103 PDFs**. Specific titles unnamed in visible content.

## 7. DEPENDENCY DEPTH ANALYSIS
Figure 4 shows correctness versus depth for both definitions and statements. Key findings: average depth = 30 (median 17, range 0–80). Lie algebra/quantum groups average ~50; logic/set theory ~6. MA-Hard (700 deepest) achieved only 2.6% correctness.

## 8. FUTURE WORK
The conclusion mentions: graduate-level focus (research math deferred); dependency-aware systems; proof formalization beyond statements. No explicit bulleted roadmap provided.

## 9. FormalMATH-Lite
No mention found in provided excerpts.

## 10. BLV TOOL DETAILS
Minimal information: it's a Lean 4 compilation checker (v4.24.0). No implementation details visible; referenced as external software package for measuring "compile rate."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "493c3c53-011c-4b08-8527-2f3b55f34cb3",
  "isSidechain": true,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "agentId": "a8e91c0fc33459163",
  "type": "user",
  "uuid": "3036741a-b20c-4c9f-b9a1-f89ed7f54add",
  "sourceToolAssistantUUID": "493c3c53-011c-4b08-8527-2f3b55f34cb3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-27T23:07:07.733Z_

Now I have a comprehensive picture. Here is the full research synthesis.

---

## MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061)

**Authors:** Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, Jeffrey Flanigan (UC Santa Cruz)
**Submitted:** May 13, 2026 | **Venue:** Submitted to NeurIPS 2026
**Categories:** cs.AI, cs.LG

---

### 1. What MathAtlas Contains

**Scale:** ~52,052 mathematical entities extracted from 103 graduate-level mathematics textbooks.

**Entity types and approximate counts:**
- ~18k theorems
- ~10k exercises
- ~10k definitions
- ~10k proofs
- ~5k examples (the paper states ~55k examples in one passage, but the total is ~52k entities, so this may reflect sub-entities)

**Domain coverage:** 87 distinct mathematical fields/subfields, including real analysis, differential geometry, category theory, topology, quantum groups, Lie algebra, set theory, logic, algebraic geometry, commutative algebra, abstract algebra, probability, quantum theory, and number theory.

**Dependency graph:** ~178k relations of three types:
- **Entity references** (one entity referencing another)
- **Object references** (linking concepts to their definitions, ~193k total, ~3.69 per entity)
- **"Proves" relations** (connecting proofs to theorems)

Dependency depth ranges from 0 to 80 (mean ~30, median ~17). Fields like Lie algebra/quantum groups average ~50 depth; set theory/logic average ~6.

**Extraction pipeline:**
1. PDFs converted to Mathematical Markdown using Nougat
2. Metadata pages filtered out
3. Few-shot prompted gpt-oss-120b with JSON schema and structured decoding (temperature 0.3) identified entity spans and types
4. Quality: 90.4% of annotated entities correctly extracted (98% for definitions, 80% for proofs); reference extraction achieved 94.8% F1 overall

**Copyright handling:** ~30% from Springer textbooks (released only as generation code); remaining 70% publicly released.

---

### 2. Correctness Metrics

MathAtlas uses a two-pronged correctness definition: **A formalization is correct only if it both compiles AND is semantically faithful to the informal statement.**

- **Compilation rate:** Checked using the `blv` tool against Lean v4.24.0
- **Semantic faithfulness:** Evaluated via MA-Align, a new 200-entity benchmark with binary "aligned"/"misaligned" labels for syntactically correct formalizations

For MA-Align evaluation, they tested CriticLean (14B and 32B) and LLM-as-judge systems (gpt-5.2 with engineered prompts). Results on MA-Align:
- CriticLean 32B: 80.0% accuracy on definitions, 75.0% on statements
- gpt-5.2 with few-shot engineered prompts: 86.0% on definitions, 80.0% on statements

The critical insight is the massive gap between compilation and correctness -- models can produce code that compiles but is mathematically meaningless.

---

### 3. Model Evaluation Results

**Statements (fine-tuned models):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| Herald 7B | 11.8% | 12.7% | 1.5% |
| Kimina 7B | 27.3% | 8.4% | 2.3% |
| ATLAS-L 8B | 21.4% | 16.4% | 3.5% |
| Goedel 8B | 20.3% | 34.9% | 7.1% |
| Goedel 32B | 23.2% | 30.6% | 7.1% |
| **ReForm 8B** | **19.0%** | **48.4%** | **9.8%** |

**Statements (prompted models):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| gpt-oss-20b zero-shot | -- | -- | 4.2% |
| gpt-oss-120b tuned examples | 21.7% | 35.9% | 7.8% |

**Definitions (prompted models only -- no fine-tuned methods generalize):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| gpt-oss-20b zero-shot | 10.5% | 20.9% | 2.2% |
| gpt-oss-120b tuned examples | 28.5% | 58.5% | 16.7% |

**MA-Hard subset** (~700 entities with deepest dependency trees, 14 subjects, primarily algebraic geometry and Lie theory):
- Best model: only **2.6% correctness**
- gpt-oss-120b: 14.6% compilation but only 2.6% correctness

**Prompt engineering ablation (statements, gpt-oss-120b):**
- Zero-shot: 14.3% compile
- +Few-shot examples: 16.8%
- +Tuned prompt: 17.1%
- +Tuned examples: 21.7%

---

### 4. Comparison to Existing Benchmarks

MathAtlas fills a clear gap. Prior benchmarks focus on simpler math:
- **ProofNet:** Undergraduate-level mathematics
- **miniF2F:** Olympiad-level mathematics
- **FATE-H/FATE-X:** 100 problems from commutative/abstract algebra
- **ConsistencyCheck / CriticLeanBench:** Focus on simpler domains

MathAtlas is distinguished by:
1. **Scale:** ~52k entities vs. hundreds in prior benchmarks
2. **Level:** Graduate-level vs. undergraduate/olympiad
3. **Dependency graph:** First benchmark to include ~178k dependency relations
4. **Entity diversity:** Includes definitions (previously underexplored), not just theorem statements
5. **MA-Align:** First semantic faithfulness benchmark covering both theorems and definitions at the graduate level

No mention of FormalMATH-Lite was found in the paper.

---

### 5. Key Insights on Reward Design and Evaluation

**Compilation is a poor proxy for correctness.** The paper's most striking finding is the dramatic gap between compilation rate and actual correctness. Kimina 7B is the extreme case: 27.3% compilation rate but only 2.3% correctness. This means **only ~8% of Kimina's compiling formalizations are semantically faithful.** This directly challenges RL approaches that use compilation as a reward signal.

**ReForm 8B is the exception:** Despite having a lower compile rate (19.0%) than Kimina (27.3%) or Goedel 32B (23.2%), ReForm achieves the highest faithfulness (48.4%) and correctness (9.8%), suggesting its "reflective" training approach produces more meaningful formalizations even if fewer compile.

**Local context hurts, counterintuitively.** Adding 300 tokens of surrounding context *decreased* performance from 20.3% to 17.4% on definitions and from 10.5% to 8.6% on statements. This suggests that naive context inclusion confuses models, highlighting the need for smarter dependency-aware retrieval.

**Mathlib grounding matters.** Definitions grounded in Mathlib (via LeanSearch) had a 27.9% correctness rate vs. 16.8% for ungrounded definitions (chi-square p<0.001). This 1.66x advantage shows that existing library coverage is a critical factor.

**Dependency depth is the key difficulty driver.** A Kolmogorov-Smirnov test confirmed a statistically significant difference (p<0.001) between depth distributions for correct vs. incorrect formalizations. The MA-Hard subset (deepest dependency trees) drops to just 2.6% correctness.

**Definition autoformalization is an open problem.** No fine-tuned methods successfully generalize from theorem to definition autoformalization. The authors could not evaluate some prior definition methods (ARIA, LoC-Decomp) due to unreleased code.

---

### 6. Limitations and Future Directions

- Focus is graduate-level, not research-level mathematics
- Proof formalization and full theorem proving are left to future work
- The authors call for **dependency-aware autoformalization systems** that can leverage the graph structure
- Better semantic faithfulness metrics are needed that generalize beyond simple domains

---

Sources:
- [MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv abstract)](https://arxiv.org/abs/2605.14061)
- [MathAtlas: A Benchmark for Autoformalization in the Wild (HTML full paper)](https://arxiv.org/html/2605.14061)
- [ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization](https://arxiv.org/abs/2510.24592)
- [An Evaluation Benchmark for Autoformalization in Lean4](https://arxiv.org/abs/2406.06555)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3036741a-b20c-4c9f-b9a1-f89ed7f54add",
  "isSidechain": true,
  "agentId": "a8e91c0fc33459163",
  "requestId": "req_011CbTusaf6L7vFuBYDZB32k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a355bff4-1dd5-4926-8a7f-bdc6597ed0c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eYQBgiXPrc3XW6hjALMxo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1859,
      "cache_read_input_tokens": 17350,
      "output_tokens": 2300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1859
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2300,
          "cache_read_input_tokens": 17350,
          "cache_creation_input_tokens": 1859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1859,
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
