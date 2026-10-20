# Research conversation: I need to verify claims about CodeQL's Python analysis capabilities. The paper idea claims: 1. "CodeQL does not require 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4931b6c3d576e6e3.jsonl`
- **Structured JSON:** [`afc7d188acf699b48fc9.json`](../../sessions/af/afc7d188acf699b48fc9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T19:00:34.922Z_

I need to verify claims about CodeQL's Python analysis capabilities. The paper idea claims:
1. "CodeQL does not require compilation to build databases for Python (source extraction only)"
2. CodeQL can be configured for inter-procedural data-flow analysis with "broad source/sink definitions (all function parameters and return values as sources; all variable reads across call boundaries as sinks)"
3. This can "approximate general inter-procedural def-use chains"

Please search for:
1. "CodeQL Python data flow analysis inter-procedural"
2. "CodeQL Python database creation compilation"
3. "CodeQL Python taint tracking source sink configuration"
4. "site:codeql.github.com Python data flow"
5. "CodeQL Python def-use analysis limitations"

Try to fetch the official CodeQL documentation page for Python data flow analysis if possible.

Report back (under 400 words):
- Does CodeQL Python extraction work without compilation? 
- Can CodeQL's Python data-flow API be used for general def-use chain extraction (not just security taint tracking)?
- What are the practical limitations?
- Is the claim about configuring broad source/sink definitions realistic?
- How long does CodeQL database creation typically take for large Python repos?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "625279a0-de9b-48c2-92f7-ba7c372cac6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:00:34.927Z_

```json
{
  "parentUuid": "625279a0-de9b-48c2-92f7-ba7c372cac6b",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "813db793-1473-4449-b058-a1d93ffb83b5",
  "timestamp": "2026-05-10T19:00:34.927Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:00:37.138Z_



I'll search for information on CodeQL's Python analysis capabilities using web searches and documentation fetches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813db793-1473-4449-b058-a1d93ffb83b5",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQNudoMXRStKo4Z4r19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7210f7bb-7506-4985-b051-6f75fbfc0790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxQFiBA8KXJEtPeVUtWNoM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:00:37.543Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FhvPnaZTeuy34frUpL6BoL`</summary>

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
  "parentUuid": "7210f7bb-7506-4985-b051-6f75fbfc0790",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQNudoMXRStKo4Z4r19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e2b59e4-8296-4924-920e-6c6411e94920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxQFiBA8KXJEtPeVUtWNoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 7304,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 801,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-10T19:00:37.550Z_

<details><summary>↩ Tool result · `toolu_01FhvPnaZTeuy34frUpL6BoL`</summary>

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
  "parentUuid": "7e2b59e4-8296-4924-920e-6c6411e94920",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "403e133c-df92-4dcf-a59e-99effece0d3c",
  "sourceToolAssistantUUID": "7e2b59e4-8296-4924-920e-6c6411e94920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:00:46.219Z_



Now let me run the web searches and fetch relevant documentation pages in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403e133c-df92-4dcf-a59e-99effece0d3c",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7686d5f9-1eee-4a30-a4da-1dabb76c4212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T19:00:47.177Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZ75czzr8ZrRzzVnE5rAAJ`</summary>

```json
{
  "query": "CodeQL Python data flow analysis inter-procedural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7686d5f9-1eee-4a30-a4da-1dabb76c4212",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c194f7d2-10f8-4ac1-9934-9ea01320a3d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T19:00:47.678Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUEi7LAvDRsLoz5nM5VkFw`</summary>

```json
{
  "query": "CodeQL Python database creation compilation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c194f7d2-10f8-4ac1-9934-9ea01320a3d3",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1faff0d3-5a73-40a0-9914-4ed119c5dc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:00:48.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T9dLXj8nrFLhxhJfKnN1BQ`</summary>

```json
{
  "query": "CodeQL Python taint tracking source sink configuration custom"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1faff0d3-5a73-40a0-9914-4ed119c5dc13",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbdb9301-79fd-486f-95bc-e06e3d4e4adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T19:00:48.655Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XPfYuC6DQFQonz8UwZudXb`</summary>

```json
{
  "query": "CodeQL Python def-use analysis limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbdb9301-79fd-486f-95bc-e06e3d4e4adf",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58540326-f2ef-435d-9457-b5f44fc9088b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T19:00:48.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018K4YxcUb6eVvGPkAm722Ru`</summary>

```json
{
  "query": "CodeQL database creation time large Python repository performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58540326-f2ef-435d-9457-b5f44fc9088b",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQP77caGED7twxhsEVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "107fc7e3-ec61-4b43-b0f2-8c85463b3fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk9Lfs5JG5nrdjvjAzoN4K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8105,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 8105,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:00:53.014Z_

<details><summary>↩ Tool result · `toolu_01XZ75czzr8ZrRzzVnE5rAAJ`</summary>

```text
Web search results for query: "CodeQL Python data flow analysis inter-procedural"

Links: [{"title":"Using flow state for precise data flow analysis - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/using-flow-labels-for-precise-data-flow-analysis/"},{"title":"DataFlow - CodeQL - GitHub","url":"https://codeql.github.com/codeql-standard-libraries/python/semmle/python/dataflow/new/DataFlow.qll/module.DataFlow.html"},{"title":"Analyzing data flow in Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/"},{"title":"About data flow analysis - CodeQL - GitHub","url":"https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/"},{"title":"Analyzing control flow in Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-control-flow-in-python/"},{"title":"CodeQL for Python — CodeQL","url":"https://codeql.github.com/docs/codeql-language-guides/codeql-for-python/"},{"title":"codeql/docs/ql-libraries/dataflow/dataflow.md at main · github/codeql","url":"https://github.com/github/codeql/blob/main/docs/ql-libraries/dataflow/dataflow.md"},{"title":"An introduction to CodeQL and data flow analysis | Zeyu (Zayne) Zhang","url":"https://www.analogue.computer/blog/codeql-and-data-flow-analysis"},{"title":"Analyzing data flow in JavaScript and TypeScript — CodeQL","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-javascript-and-typescript/"},{"title":"Customizing Library Models for Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/customizing-library-models-for-python/"}]

Based on the search results, here's what I found about CodeQL Python data flow analysis inter-procedural capabilities:

## Overview

CodeQL provides a library for local (intra-procedural) and global (inter-procedural) data flow analysis: deciding whether data can flow from a source to a sink.

## Local vs. Global Data Flow

Local data flow is data flow within a single method or callable. Local data flow is easier, faster, and more precise than global data flow, and is sufficient for many queries. In contrast, global data flow tracks data flow throughout the entire program, and is therefore more powerful than local data flow. However, global data flow is less precise than local data flow, and the analysis typically requires significantly more time and memory to perform.

## Using Inter-procedural Data Flow

To use global (interprocedural) data flow, extend the class DataFlow::Configuration as documented on that class. Additionally, to use local (intraprocedural) data flow, call DataFlow::localFlow or DataFlow::localFlowStep with arguments of type DataFlow::Node.

## Key Differences

Local and global data flow differ in which edges they consider: local data flow only considers edges between data flow nodes belonging to the same function and ignores data flow between functions and through object properties. Global data flow, however, considers the latter as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c194f7d2-10f8-4ac1-9934-9ea01320a3d3",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "6123e491-a791-4395-9e73-11661a1592f1",
  "sourceToolAssistantUUID": "c194f7d2-10f8-4ac1-9934-9ea01320a3d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:00:54.450Z_

<details><summary>↩ Tool result · `toolu_01JUEi7LAvDRsLoz5nM5VkFw`</summary>

```text
Web search results for query: "CodeQL Python database creation compilation extraction"

Links: [{"title":"Preparing your code for CodeQL analysis - GitHub Docs","url":"https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis"},{"title":"database create - CodeQL CLI","url":"https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create"},{"title":"CodeQL for Python — CodeQL","url":"https://codeql.github.com/docs/codeql-language-guides/codeql-for-python/"},{"title":"database create - CodeQL","url":"https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/database-create"},{"title":"`codeql_database_create`: support custom CodeQL config file with `paths-ignore` for extraction exclusions · Issue #213 · advanced-security/codeql-development-mcp-server","url":"https://github.com/advanced-security/codeql-development-mcp-server/issues/213"},{"title":"Creating CodeQL databases - GitHub Enterprise Server 3.5 Docs","url":"https://docs.github.com/en/enterprise-server@3.5/code-security/codeql-cli/using-the-codeql-cli/creating-codeql-databases"},{"title":"Preparing your code for CodeQL analysis - GitHub Enterprise Cloud Docs","url":"https://docs.github.com/en/enterprise-cloud@latest/code-security/codeql-cli/using-the-codeql-cli/creating-codeql-databases"},{"title":"Basic query for Python code - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/basic-query-for-python-code/"},{"title":"System requirements — CodeQL","url":"https://codeql.github.com/docs/codeql-overview/system-requirements/"},{"title":"database init - CodeQL CLI","url":"https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init"}]

Here are the key findings from the web search results about CodeQL Python database creation, compilation, and extraction:

## Python Database Creation

CodeQL can generate a new Python database by executing the database create subcommand from the code's checkout root.

## No Compilation Required for Python

When running database create for JavaScript, TypeScript, Python, and Ruby, you should not specify a --command option. Otherwise this overrides the normal extractor invocation, which will create an empty database.

The database can be created without building the source root, and this mode is available for C#, Java, JavaScript/TypeScript, Python, and Ruby.

## Extraction Process

CodeQL analysis relies on extracting relational data from your code, and using it to build a CodeQL database. CodeQL databases contain all of the important information about a codebase, which can be analyzed by executing CodeQL queries against it.

## System Requirements for Python Extraction

For Python extraction on Linux and macOS, Python 3 must be installed and available on the PATH as python3 or python.

## Extractor Options

CodeQL allows setting options for CodeQL extractors, with extractor-option-name in the form of extractor_name.group1.group2.option_name or group1.group2.option_name.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1faff0d3-5a73-40a0-9914-4ed119c5dc13",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "db326fb8-5bba-445e-ab3e-4dbf2ec6833d",
  "sourceToolAssistantUUID": "1faff0d3-5a73-40a0-9914-4ed119c5dc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:00:55.239Z_

<details><summary>↩ Tool result · `toolu_01T9dLXj8nrFLhxhJfKnN1BQ`</summary>

```text
Web search results for query: "CodeQL Python taint tracking source sink configuration custom"

Links: [{"title":"TaintTracking - CodeQL - GitHub","url":"https://codeql.github.com/codeql-standard-libraries/python/semmle/python/dataflow/old/TaintTracking.qll/module.TaintTracking.html"},{"title":"Taint Tracking in CodeQL » SecurityGrind","url":"https://securitygrind.com/taint-tracking-in-codeql/"},{"title":"Practical Introduction to CodeQL :: jorgectf — blog","url":"https://jorgectf.github.io/blog/post/practical-codeql-introduction/"},{"title":"TaintSink - CodeQL - GitHub","url":"https://codeql.github.com/codeql-standard-libraries/python/semmle/python/dataflow/old/TaintTracking.qll/type.TaintTracking$TaintSink.html"},{"title":"Customizing Library Models for Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/customizing-library-models-for-python/"},{"title":"New dataflow API for writing custom CodeQL queries - GitHub Changelog","url":"https://github.blog/changelog/2023-08-14-new-dataflow-api-for-writing-custom-codeql-queries/"},{"title":"CodeQL zero to hero part 3: Security research with CodeQL - The GitHub Blog","url":"https://github.blog/security/vulnerability-research/codeql-zero-to-hero-part-3-security-research-with-codeql/"},{"title":"Analyzing data flow in Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/"},{"title":"Taint Tracking Basics | ICDT","url":"https://icandothese.com/docs/tech/development/codeql/04_taint_tracking/"},{"title":"General issue - Using this taint-tracking script can only show the source node and sink node? · Issue #5104 · github/codeql","url":"https://github.com/github/codeql/issues/5104"}]

I've found comprehensive information about CodeQL Python taint tracking with custom source and sink configuration. Here's what the search results show:

## Custom Taint Tracking Configuration

A custom taint tracking configuration is declared as a module that implements DataFlow::ConfigSig. This configuration consists of several key components:

### Sources and Sinks

Sources of taint are created by looking up function calls or other patterns and assigning them to the source parameter of type DataFlow::Node. Similarly, taint sinks represent places where if user-controlled data arrives, exploitation is possible, typically function call arguments.

### Configuration Structure

Global taint tracking is implemented by applying the module TaintTracking::Global&lt;ConfigSig> to your configuration with predicates for isSource and isSink.

### Advanced Features

Additional configuration predicates like isAdditionalTaintStep and Sanitizers are "extras" that allow you to specify additional "jumps" the flow may make to bypass known functions.

### Modern API

In the newer CodeQL API, sanitizers and barriers are unified under isBarrier instead of isSanitizer, and isAdditionalTaintStep is replaced with isAdditionalFlowStep.

### Data Flow Sources

The class RemoteFlowSource represents data flow from remote network inputs and can be used as a starting point for defining security queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbdb9301-79fd-486f-95bc-e06e3d4e4adf",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "2f6dcdce-0e0d-4d99-a72a-f01a638cb000",
  "sourceToolAssistantUUID": "cbdb9301-79fd-486f-95bc-e06e3d4e4adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:00:56.678Z_

<details><summary>↩ Tool result · `toolu_01XPfYuC6DQFQonz8UwZudXb`</summary>

```text
Web search results for query: "CodeQL Python def-use analysis limitations"

Links: [{"title":"Getting started with CodeQL, GitHub's declarative static analyzer for security - Tweag","url":"https://www.tweag.io/blog/2025-08-07-codeql-intro/"},{"title":"v2.15.3 - Python code analysis fails · Issue #2042 · github/codeql-action","url":"https://github.com/github/codeql-action/issues/2042"},{"title":"CodeQL for Python — CodeQL","url":"https://codeql.github.com/docs/codeql-language-guides/codeql-for-python/"},{"title":"Python queries for CodeQL analysis - GitHub Docs","url":"https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/python-built-in-queries"},{"title":"Understanding the time taken for analyzing queries using codeql cli · github/codeql · Discussion #6020","url":"https://github.com/github/codeql/discussions/6020"},{"title":"CodeQL library for Python — CodeQL","url":"https://codeql.github.com/docs/codeql-language-guides/codeql-library-for-python/"},{"title":"codeql/change-notes/1.20/analysis-python.md at main · github/codeql","url":"https://github.com/github/codeql/blob/main/change-notes/1.20/analysis-python.md"},{"title":"Customizing Library Models for Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/customizing-library-models-for-python/"},{"title":"codeql/change-notes/1.19/analysis-python.md at main · github/codeql","url":"https://github.com/github/codeql/blob/main/change-notes/1.19/analysis-python.md"},{"title":"Expressions and statements in Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/expressions-and-statements-in-python/"}]

Based on the search results, here are the key limitations of CodeQL's Python def-use analysis:

## Key Limitations

**Dynamic Typing and Call Resolution**

Resolving call targets in Python isn't simply a matter of finding calls with a particular name, since Python doesn't provide static types for objects, and module members can potentially be redefined on the fly. Instead, you need to track the set of possible definitions for a function or method name at each point in the program, which is a rather expensive computation.

**Modular Analysis Constraints**

CodeQL performs a modular analysis: it doesn't inspect the source code of your dependencies. As a consequence, you need to model your dependencies' behavior for them to be treated correctly by CodeQL's analysis. This means that if a library is not in CodeQL's list of supported Python libraries, you'll need to manually model the functions and data flows from that library for proper analysis.

**Performance Impact**

The def-use analysis complexity has performance implications. The need to track possible definitions is a rather expensive computation, but the result of that analysis is then cached, so it only needs to be done once for each database.

**Name Shadowing Challenges**

In Python 3, the builtin print is a function instead a keyword, so it has the same potential to be shadowed or replaced as any other function name, illustrating the broader challenge of handling dynamic name resolution in Python's def-use analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58540326-f2ef-435d-9457-b5f44fc9088b",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "be37482f-d81a-41a1-b1d2-c085ff1fb110",
  "sourceToolAssistantUUID": "58540326-f2ef-435d-9457-b5f44fc9088b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:01:00.551Z_

<details><summary>↩ Tool result · `toolu_018K4YxcUb6eVvGPkAm722Ru`</summary>

```text
Web search results for query: "CodeQL database creation time large Python repository performance"

Links: [{"title":"Understanding the time taken for analyzing queries using codeql cli · github/codeql · Discussion #6020","url":"https://github.com/github/codeql/discussions/6020"},{"title":"Horrible performance of Python PrintAst query on large databases · Issue #6964 · github/codeql","url":"https://github.com/github/codeql/issues/6964"},{"title":"CodeQL version 2.18.2 doubles the amount of time spent compiling CodeQL databases · Issue #17489 · github/codeql","url":"https://github.com/github/codeql/issues/17489"},{"title":"Preparing your code for CodeQL analysis - GitHub Docs","url":"https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis"},{"title":"Code scanning analysis takes too long - GitHub Docs","url":"https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/analysis-takes-too-long"},{"title":"CodeQL performance and coverage improvements in recent releases - GitHub Changelog","url":"https://github.blog/changelog/2025-02-12-codeql-performance-and-coverage-improvements-in-recent-releases/"},{"title":"database create - CodeQL CLI","url":"https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create"},{"title":"Streamlining CodeQL Analysis with CodeQL Wrapper - Tweag","url":"https://www.tweag.io/blog/2026-01-15-codeql-wrapper/"},{"title":"Resources requirement when building CodeQL database · github/securitylab · Discussion #311","url":"https://github.com/github/securitylab/discussions/311"},{"title":"Code scanning analysis takes too long - GitHub Enterprise Server 3.10 Docs","url":"https://docs.github.com/en/enterprise-server@3.10/code-security/code-scanning/troubleshooting-code-scanning/analysis-takes-too-long"}]

Based on the search results, here are the key findings about CodeQL database creation time and performance with large Python repositories:

## Database Creation Overhead

The overhead of database creation is tiny and has never been found to be a bottleneck for Python analysis. This suggests that while database creation does take time, it's not typically the primary performance constraint.

## Performance Bottlenecks

The main performance challenges with CodeQL on large Python repositories relate to:

1. **Memory Pressure**: Memory pressure is a problem because analysis is performed across all projects at the same time, which may result in very large sets of results being computed. If the memory needed to store these intermediate results exceeds what's available, the evaluator may end up spending a nontrivial amount of time doing garbage collection.

2. **Query Analysis Time**: Attempting to view the AST of a small Python file doesn't complete running after more than 12 hours, but by removing regex support from PrintAST.qll, the same query on the same database completes in under 1 minute.

## Recent Improvements

CodeQL databases now take 2-3x less space on disk, which makes them faster to transfer and read/manipulate thanks to a new compressed database format. Additionally, analysis of Python apps now has significantly faster extraction and analysis times.

## Memory Optimization

Database creation is very memory-intense, and you can give it more memory by passing -J-Xmx1234M to codeql database create, replacing 1234 by 80% of your available machine memory (in megabytes).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "107fc7e3-ec61-4b43-b0f2-8c85463b3fa0",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "861e47d8-a794-416f-8b31-4ef47f733e59",
  "sourceToolAssistantUUID": "107fc7e3-ec61-4b43-b0f2-8c85463b3fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T19:01:03.095Z_

Let me now fetch the key official documentation pages for more precise details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "861e47d8-a794-416f-8b31-4ef47f733e59",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQQoEdsKvMT32rtZ4th",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfed1899-c86f-45cc-9b56-19feb404b9c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4NLvet3ZqecDXjyWrgk1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4709,
      "cache_read_input_tokens": 10015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4709,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T19:01:06.246Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XTFB1xp2My3TCxBeQNgQVn`</summary>

```json
{
  "url": "https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/",
  "prompt": "Extract all details about: 1) How to configure sources and sinks (especially custom/broad definitions like all function parameters). 2) Inter-procedural (global) data flow capabilities. 3) Any limitations mentioned. 4) Whether this can be used for general def-use analysis beyond security taint tracking."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfed1899-c86f-45cc-9b56-19feb404b9c7",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQQoEdsKvMT32rtZ4th",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7713ca0a-d9ee-4ea3-a64b-5340d5f4209a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4NLvet3ZqecDXjyWrgk1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4709,
      "cache_read_input_tokens": 10015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4709,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T19:01:08.153Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ekh52S6MCGRR97i5pfyfio`</summary>

```json
{
  "url": "https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis",
  "prompt": "Extract details about: 1) Whether Python requires compilation for database creation. 2) How the extraction process works for interpreted languages. 3) Any specific notes about Python extraction. 4) Performance characteristics or time estimates for database creation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7713ca0a-d9ee-4ea3-a64b-5340d5f4209a",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQQoEdsKvMT32rtZ4th",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9345b53-5043-4da0-9ed7-2c608c0c3d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4NLvet3ZqecDXjyWrgk1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4709,
      "cache_read_input_tokens": 10015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4709,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T19:01:10.557Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011BvV6QY33EoQKufkRDJFMA`</summary>

```json
{
  "url": "https://github.com/github/codeql/blob/main/docs/ql-libraries/dataflow/dataflow.md",
  "prompt": "Extract details about: 1) How data flow configurations work internally. 2) How sources and sinks are defined. 3) Whether custom broad source/sink definitions (all parameters as sources, all reads as sinks) are feasible. 4) Any performance or scalability concerns with broad configurations. 5) Inter-procedural analysis details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9345b53-5043-4da0-9ed7-2c608c0c3d96",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQQoEdsKvMT32rtZ4th",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "176cdcef-3411-4713-9378-eda73a09cc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4NLvet3ZqecDXjyWrgk1h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4709,
      "cache_read_input_tokens": 10015,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 479,
          "cache_read_input_tokens": 10015,
          "cache_creation_input_tokens": 4709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4709,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T19:01:12.994Z_

<details><summary>↩ Tool result · `toolu_01XTFB1xp2My3TCxBeQNgQVn`</summary>

```text
# CodeQL Python Data Flow Analysis: Configuration and Capabilities

## 1. Configuring Sources and Sinks

**Custom Definitions:**
Sources and sinks are configured by implementing the `DataFlow::ConfigSig` signature with two required predicates:

- `isSource(DataFlow::Node source)` - "defines where data may flow from"
- `isSink(DataFlow::Node sink)` - "defines where data may flow to"

**Broad Definitions:**
The documentation shows how to define sources broadly. For example, using `RemoteFlowSource` captures "data flow from remote network inputs." You can also target specific node types like `ParameterNode` to capture all function parameters as sources, as demonstrated in the query examples.

Additional optional predicates include `isBarrier` (blocks flow) and `isAdditionalFlowStep` (extends flow rules).

## 2. Inter-procedural (Global) Data Flow

Global data flow "tracks data flow throughout the entire program" by implementing configurations with `DataFlow::Global&lt;ConfigSig>`. The analysis uses the predicate `flow(DataFlow::Node source, DataFlow::Node sink)` to identify complete paths.

The library also supports "global taint tracking," which extends global flow with "non-value-preserving steps." This is invoked via `TaintTracking::Global&lt;ConfigSig>`.

## 3. Stated Limitations

The documentation explicitly notes that "global data flow is less precise than local data flow, and the analysis typically requires significantly more time and memory to perform." Additionally, the modular API mentioned requires CodeQL 2.13.0 or later.

## 4. General Def-Use Analysis Capability

This framework extends beyond security taint tracking. The predefined library includes conceptual nodes like `FileSystemAccess`, `SqlExecution`, `SystemCommandExecution`, and `CodeExecution` for domain-specific analyses. The modular approach supports custom configurations for any source-to-sink investigation, making it applicable to broader program analysis tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7713ca0a-d9ee-4ea3-a64b-5340d5f4209a",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "bd7258f8-78c1-4302-8161-7a4c9f26bd5b",
  "sourceToolAssistantUUID": "7713ca0a-d9ee-4ea3-a64b-5340d5f4209a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:01:14.240Z_

<details><summary>↩ Tool result · `toolu_01Ekh52S6MCGRR97i5pfyfio`</summary>

```text
# CodeQL Python Database Creation Analysis

## 1) Python Compilation Requirements

Python does **not** require compilation for database creation. The documentation explicitly states: "The CodeQL CLI includes extractors to create databases for non-compiled languages—specifically, JavaScript (and TypeScript), Python, and Ruby."

## 2) Extraction Process for Interpreted Languages

For interpreted languages, the extraction approach differs significantly from compiled languages. The document notes: "For interpreted languages and when you specify `--build-mode none` for C/C++, C#, Java and Rust, the extraction progress is displayed in the console. For each source file, the console shows if extraction was successful or if it failed."

The extractors are "automatically invoked when you specify JavaScript, Python, or Ruby as the `--language` option when executing `database create`."

## 3) Python-Specific Extraction Notes

When creating Python databases, users must ensure:
- Python 3 is installed and available to the CodeQL extractor
- The specific Python version used by the code is installed

Importantly, users "should not specify a `--command` option" when running database creation for Python, as this "overrides the normal extractor invocation, which will create an empty database."

## 4) Performance Characteristics

The documentation provides no explicit time estimates or performance benchmarks for database creation across any language, including Python. No timing data is included in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9345b53-5043-4da0-9ed7-2c608c0c3d96",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "28557965-364c-43a1-9879-4b9eb0918e97",
  "sourceToolAssistantUUID": "b9345b53-5043-4da0-9ed7-2c608c0c3d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:01:17.983Z_

<details><summary>↩ Tool result · `toolu_011BvV6QY33EoQKufkRDJFMA`</summary>

```text
# CodeQL Data Flow Analysis: Technical Insights

## 1) Configuration Internals

The shared library separates configuration-specific and configuration-independent code. A `Configuration` class defines user behavior, while the implementation handles matching call-sites with returns and field writes. The architecture allows "multiple copies of the library to exist without duplicating configuration-independent predicates."

## 2) Sources and Sinks Definition

The document focuses on the infrastructure layer rather than source/sink specification. It addresses how data flows through the system but doesn't explicitly detail source/sink API patterns. Configurations would typically define these through the public interface exposed by `DataFlow.qll`.

## 3) Feasibility of Broad Definitions

The document doesn't directly address marking all parameters as sources or all reads as sinks. However, it warns that "certain databases have many reads and writes of the same global variable, then a direct step may have performance problems, since the straight-forward implementation is just a cartesian product." This suggests broad definitions could create scalability issues.

## 4) Performance Concerns

Key concerns include:

- **Access path limits**: "Changing this value has a direct impact on performance for large databases"
- **Cartesian products**: Global variable tracking can become inefficient without intermediate nodes
- **Call context overhead**: Virtual dispatch with context requires careful implementation to avoid joining relations that are "usually way too big to be feasible"

## 5) Inter-procedural Analysis

The system matches arguments to parameters through `ParameterPosition` and `ArgumentPosition` classes. It supports "one-level call context" for virtual dispatch precision and tracks flow through field stores, reads, and return values using dedicated node types like `PostUpdateNode` to distinguish pre- and post-mutation states.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "176cdcef-3411-4713-9378-eda73a09cc45",
  "isSidechain": true,
  "promptId": "d41d1f4e-de4e-4f06-b2bc-a9e0711227dc",
  "agentId": "a4931b6c3d576e6e3",
  "type": "user",
  "uuid": "12279fd2-c25d-456d-b66f-8c781fd540b6",
  "sourceToolAssistantUUID": "176cdcef-3411-4713-9378-eda73a09cc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:01:44.025Z_

Here is my analysis of the three claims:

---

**1. Does CodeQL Python extraction work without compilation?**

Yes, confirmed. The official docs state that CodeQL includes extractors for "non-compiled languages -- specifically, JavaScript (and TypeScript), Python, and Ruby." For Python, you must *not* specify a `--command` option; doing so overrides the extractor and produces an empty database. The extractor performs source-level extraction only, requiring Python 3 to be installed on the system. This claim is **accurate**.

**2. Can CodeQL's Python data-flow API be used for general def-use chain extraction?**

Partially. CodeQL's global (inter-procedural) data flow framework uses a `DataFlow::ConfigSig` interface where you define `isSource` and `isSink` predicates. You can target `ParameterNode` to treat all function parameters as sources and define sinks broadly across variable reads. The framework is not limited to security taint tracking -- it supports arbitrary source-to-sink data flow queries. However, calling this "general def-use chains" is an overstatement. CodeQL's data flow is value-tracking, not a classical def-use analysis. It tracks how a specific value propagates, not all definitions that may reach a use. Python's dynamic typing makes call-target resolution expensive, and CodeQL's modular analysis does not inspect dependency source code (unmodeled libraries are opaque). The claim is **directionally correct but imprecise** -- it approximates certain def-use patterns but is not equivalent to a full def-use chain analysis.

**3. Is the "broad source/sink definitions" configuration realistic?**

Technically feasible but practically problematic. The internal docs warn that broad definitions risk cartesian-product blowups -- e.g., many reads/writes of the same global variable cause performance problems. Access path limits directly impact performance on large databases. Global data flow already "requires significantly more time and memory" than local analysis. Defining all parameters as sources and all cross-boundary reads as sinks on a large codebase would likely cause severe scalability issues (memory exhaustion, very long runtimes). The claim is **technically possible but may not scale**.

**4. Database creation time for large Python repos?**

The official docs provide no benchmarks. A GitHub discussion notes that database creation overhead for Python "is tiny and has never been found to be a bottleneck." The bottleneck is query evaluation, not extraction. For large repos, memory is the main constraint (tunable via `-J-Xmx`). Extraction itself is likely minutes, not hours, for most repos; query evaluation of broad inter-procedural analyses could take much longer.

**5. Practical limitations summary:**
- Python's dynamic typing limits call resolution precision
- Dependencies without models are opaque (modular analysis)
- Global data flow is less precise than local
- Broad source/sink configurations risk combinatorial explosion
- Memory-intensive for large codebases

Sources:
- [Analyzing data flow in Python - CodeQL](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/)
- [Preparing your code for CodeQL analysis - GitHub Docs](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)
- [About data flow analysis - CodeQL](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/)
- [CodeQL dataflow internals (GitHub repo)](https://github.com/github/codeql/blob/main/docs/ql-libraries/dataflow/dataflow.md)
- [CodeQL performance discussion #6020](https://github.com/github/codeql/discussions/6020)
- [CodeQL for Python overview](https://codeql.github.com/docs/codeql-language-guides/codeql-for-python/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12279fd2-c25d-456d-b66f-8c781fd540b6",
  "isSidechain": true,
  "agentId": "a4931b6c3d576e6e3",
  "requestId": "req_011CauQS5kM7gC6BueWb3CkE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "546e1ec7-e2ca-4e1c-bb5a-422d87133a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KmUQnyPTEUjRb6f2hvyhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 14724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
