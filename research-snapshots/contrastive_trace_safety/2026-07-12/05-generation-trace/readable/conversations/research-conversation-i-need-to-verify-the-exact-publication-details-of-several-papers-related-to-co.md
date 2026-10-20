# Research conversation: I need to verify the exact publication details of several papers related to code structure analysis for a bibliography. 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6f54155fec009ea1.jsonl`
- **Structured JSON:** [`af7f22a4f572c7e90a85.json`](../../sessions/af/af7f22a4f572c7e90a85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-15T03:14:14.629Z_

I need to verify the exact publication details of several papers related to code structure analysis for a bibliography. Use WebSearch to find the correct details.

1. CodeQL — find the canonical academic paper or reference for CodeQL (GitHub's static analysis engine). It may be published under the name "QL" or "Semmle QL" by Pavel Avgustinov et al., or there may be a more recent reference.
2. Tree-sitter — find if there is an academic paper about tree-sitter for code parsing, or identify the best academic work that uses tree-sitter for code structure in ML/NLP context
3. Program dependence graph — find the classic paper by Ferrante, Ottenstein, Warren (1987) on "The program dependence graph and its use in optimization"
4. Joern — the open source code analysis tool, find its academic paper (Yamaguchi et al.)
5. InferCode (Bui et al., 2021) — learning code representations from AST subtrees

For each, I need: full author list, exact title, venue, year, and any identifier (arXiv, DOI).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "e17a79ab-35d5-4acf-819a-97b2aff6a2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T03:14:14.639Z_

```json
{
  "parentUuid": "e17a79ab-35d5-4acf-819a-97b2aff6a2dd",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f6d5b8c5-83b0-4eae-a02e-799ff181f6b4",
  "timestamp": "2026-05-15T03:14:14.639Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T03:14:16.945Z_



I'll search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d5b8c5-83b0-4eae-a02e-799ff181f6b4",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dFy7VzhquJpefYTsoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe3b1dc-696b-4ced-88bd-81d93bec8c81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WubnyQwL4LxqUDez8Qbzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 7330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6009,
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

_source line 4 · 2026-05-15T03:14:17.380Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MWNTMc8xT5FTjRrd1JR8LG`</summary>

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
  "parentUuid": "5fe3b1dc-696b-4ced-88bd-81d93bec8c81",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dFy7VzhquJpefYTsoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81a688a-a05e-499a-a2fa-7ade06cb65c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WubnyQwL4LxqUDez8Qbzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 7330,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6009
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 7330,
          "cache_creation_input_tokens": 6009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6009,
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

_source line 5 · 2026-05-15T03:14:17.383Z_

<details><summary>↩ Tool result · `toolu_01MWNTMc8xT5FTjRrd1JR8LG`</summary>

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
  "parentUuid": "d81a688a-a05e-499a-a2fa-7ade06cb65c2",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "fd551be5-ff6a-4da4-9bf7-222d1c295e9a",
  "sourceToolAssistantUUID": "d81a688a-a05e-499a-a2fa-7ade06cb65c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T03:14:19.877Z_



Now let me search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd551be5-ff6a-4da4-9bf7-222d1c295e9a",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "923d5881-ea9f-4396-9580-e4ed2d51c322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-15T03:14:20.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A7BfrLmKxhSSnBjgPJaRif`</summary>

```json
{
  "query": "CodeQL QL Semmle academic paper Pavel Avgustinov \"QL: Object-oriented Queries on Relational Data\" OOPSLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "923d5881-ea9f-4396-9580-e4ed2d51c322",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55c855f5-1a3a-4dc1-93de-f14e3a08be7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 8 · 2026-05-15T03:14:21.948Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgB9L88UBYoZNjC7c7T3jd`</summary>

```json
{
  "query": "tree-sitter academic paper code parsing ML NLP \"tree-sitter\" scholarly reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55c855f5-1a3a-4dc1-93de-f14e3a08be7c",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eedc6d31-6d06-4008-9319-71e63fa50564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-15T03:14:22.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkLtMojt3kAd3ypFSG5sqG`</summary>

```json
{
  "query": "Ferrante Ottenstein Warren 1987 \"program dependence graph and its use in optimization\" TOPLAS DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eedc6d31-6d06-4008-9319-71e63fa50564",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6185aca3-6dd4-43f1-ad5f-cd1539f43a01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 10 · 2026-05-15T03:14:23.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0131DM1SDS6MNeX5Dhb3yebL`</summary>

```json
{
  "query": "Joern code analysis academic paper Yamaguchi \"Modeling and Discovering Vulnerabilities with Code Property Graphs\" IEEE S&P"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6185aca3-6dd4-43f1-ad5f-cd1539f43a01",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b0e19f9-1c76-4ce9-a408-f2468ba545dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 11 · 2026-05-15T03:14:24.011Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXsZcNbfYy9fqqVCCeSgon`</summary>

```json
{
  "query": "InferCode Bui 2021 \"self-supervised learning of code representation\" AST subtrees ICSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b0e19f9-1c76-4ce9-a408-f2468ba545dc",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dGB5q2fgEuHaVknwyK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "628ea1f7-8f77-41ed-9484-b26eebd2fec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXX3FfauKMqdmhSNfn9XMj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13339,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 337,
          "cache_read_input_tokens": 13339,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 12 · 2026-05-15T03:14:25.256Z_

<details><summary>↩ Tool result · `toolu_01A7BfrLmKxhSSnBjgPJaRif`</summary>

```text
Web search results for query: "CodeQL QL Semmle academic paper Pavel Avgustinov "QL: Object-oriented Queries on Relational Data" OOPSLA"

Links: [{"title":"QL: Object-oriented Queries on Relational Data - DROPS","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2016.2"},{"title":"[PDF] QL: Object-oriented Queries on Relational Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-oriented-Queries-on-Relational-Data-Avgustinov-Moor/8d941602bca76656dacfa1062fc9ef481deb6680"},{"title":"Academic publications - CodeQL - GitHub","url":"https://codeql.github.com/publications/"},{"title":"QL: Object-oriented Queries on Relational Data (ECOOP 2016 - Research Track) - ECOOP 2016","url":"https://2016.ecoop.org/details/ecoop-2016-papers/17/QL-Object-oriented-Queries-on-Relational-Data"}]

I found the academic paper you're looking for! 

"QL: Object-oriented Queries on Relational Data" was authored by Pavel Avgustinov, Oege de Moor, Michael Peyton Jones, and Max Schäfer, and was published at the 30th European Conference on Object-Oriented Programming (ECOOP 2016).

Note: The paper was actually published at ECOOP 2016, not OOPSLA. The paper describes QL, a language for querying complex, potentially recursive data structures that compiles to Datalog and runs on a standard relational database, while providing object-oriented features such as classes and methods.

The paper is available through the official DROPS repository and other academic sources. The canonical version is available on the Semmle website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55c855f5-1a3a-4dc1-93de-f14e3a08be7c",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "c88668c9-4fe4-4f65-bfb7-195ebbc28db3",
  "sourceToolAssistantUUID": "55c855f5-1a3a-4dc1-93de-f14e3a08be7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T03:14:26.779Z_

<details><summary>↩ Tool result · `toolu_01FkLtMojt3kAd3ypFSG5sqG`</summary>

```text
Web search results for query: "Ferrante Ottenstein Warren 1987 "program dependence graph and its use in optimization" TOPLAS DOI"

Links: [{"title":"The program dependence graph and its use in optimization | ACM Transactions on Programming Languages and Systems","url":"https://dl.acm.org/doi/10.1145/24039.24041"},{"title":"\"The Program Dependence Graph and Its Use in Optimization\" by Jeanne Ferrante, Karl J. Ottenstein et al.","url":"https://digitalcommons.mtu.edu/michigantech-p/12533/"},{"title":"The Program Dependence Graph and Its Use in Optimization JEANNE FERRANTE","url":"https://web.eecs.umich.edu/~mahlke/courses/583f23/reading/ferrante_toplas_87.pdf"},{"title":"The program dependence graph and its use in optimization, ACM Transactions on Programming Languages and Systems (TOPLAS) | 10.1145/24039.24041 | DeepDyve","url":"https://www.deepdyve.com/lp/association-for-computing-machinery/the-program-dependence-graph-and-its-use-in-optimization-5Q6b2CkUWI"},{"title":"The Program Dependence Graph and Its Use in Optimization for ACM Transactions on Programming Languages and Systems (TOPLAS) - IBM Research","url":"https://research.ibm.com/publications/the-program-dependence-graph-and-its-use-in-optimization"},{"title":"Program Dependence Graphs 1 The Program Dependence Graph and Its Use In Op-","url":"https://users.cs.northwestern.edu/~chrdimo/teaching/eecs396-w19/18.pdf"},{"title":"[PDF] The program dependence graph and its use in optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-program-dependence-graph-and-its-use-in-Ferrante-Ottenstein/38641821f40fe883c5ce51a5133d538099093f9a"},{"title":"Ferrante, J., Ottenstein, K.J. and Warren, J.D. (1987) The Program Dependence Graph and Its Use in Optimization. ACM Transactions on Programming Languages and Systems, 9, 319-349. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(lz5mqp453edsnp55rrgjct55.))/reference/referencespapers.aspx?referenceid=1183324"},{"title":"Hal","url":"https://theses.hal.science/tel-01626398v1/html_references"},{"title":"The program dependence graph and its use in optimization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-12925-1_33"}]

Based on the search results, here is the information about the Ferrante, Ottenstein, and Warren paper from 1987:

## Publication Details

The paper "The Program Dependence Graph and Its Use in Optimization" was published in ACM Transactions on Programming Languages and Systems (TOPLAS), Volume 9(3), pages 319-349.

## DOI

The DOI is 10.1145/24039.24041

## Summary

The paper presents an intermediate program representation, called the program dependence graph (PDG), that makes explicit both the data and control dependences for each operation in a program. The paper was published in ACM Transactions on Programming Languages and Systems, Vol. 9, No. 3, July 1987, Pages 319-349.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6185aca3-6dd4-43f1-ad5f-cd1539f43a01",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "a3eb68dc-e58d-4da2-9c89-1d42834180a4",
  "sourceToolAssistantUUID": "6185aca3-6dd4-43f1-ad5f-cd1539f43a01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:14:29.740Z_

<details><summary>↩ Tool result · `toolu_01FgB9L88UBYoZNjC7c7T3jd`</summary>

```text
Web search results for query: "tree-sitter academic paper code parsing ML NLP "tree-sitter" scholarly reference"

Links: [{"title":"Evaluating the Impact of Source Code Parsers on ML4SE Models Ilya Utkin","url":"https://arxiv.org/pdf/2206.08713"},{"title":"GitHub - tree-sitter/tree-sitter: An incremental parsing system for programming tools · GitHub","url":"https://github.com/tree-sitter/tree-sitter"},{"title":"Tree-sitter: Revolutionizing Parsing with an Incremental Parsing Library","url":"https://www.deusinmachina.net/p/tree-sitter-revolutionizing-parsing"},{"title":"Advanced Parsing - Tree-sitter","url":"https://tree-sitter.github.io/tree-sitter/using-parsers/3-advanced-parsing.html"},{"title":"GitHub - AmirHesam46/Tree-sitter-Code-Parsing-and-Analysis","url":"https://github.com/AmirHesam46/Tree-sitter-Code-Parsing-and-Analysis"},{"title":"5 Powerful Ways to Use Tree-sitter in Your Next Project | by Istiaq Ahmed Fahad | Medium","url":"https://medium.com/@ahmedfahad04/5-powerful-ways-to-use-tree-sitter-in-your-next-project-50e17c1f7055"},{"title":"tree-sitter · GitHub","url":"https://github.com/tree-sitter"},{"title":"Tree Sitter and the Complications of Parsing Languages - Mastering Emacs","url":"https://www.masteringemacs.org/article/tree-sitter-complications-of-parsing-languages"},{"title":"Using Parsers - Tree-sitter","url":"https://tree-sitter.github.io/tree-sitter/using-parsers/"},{"title":"Speech and Language Processing. Daniel Jurafsky & James H. Martin.","url":"https://web.stanford.edu/~jurafsky/slp3/21.pdf"}]

Based on the web search results, I found several relevant resources about Tree-sitter in academic and practical contexts:

## Key Findings

**Academic Research:**
A 2022 arxiv paper titled "Evaluating the Impact of Source Code Parsers on ML4SE Models" examines whether ASTs extracted with different parsers are similar and how they affect ML model quality, noting that Tree-sitter is commonly used in ML4SE data mining pipelines.

**Core Definition:**
Tree-sitter is a parser generator tool and an incremental parsing library that can build a concrete syntax tree for a source file and efficiently update the syntax tree as the source file is edited.

**Historical Context:**
Tree-sitter was announced publicly in a GitHub blog post in 2018 by its creator Max Brunsfeld, who developed it out of the need for an incremental parsing solution that was faster than the state of the art at the time.

**ML/NLP Applications:**
The search results show that TreeLSTM, originally created for natural language processing, has been reused and adapted for working with source code, and works directly with tree representation of code. This demonstrates Tree-sitter's relevance to machine learning applications in code analysis.

**Broader Impact:**
Tree-sitter's impact has been undeniable, with adoption in Vscode, Emacs, Neovim, and many other editors.

The most relevant academic reference appears to be the arXiv paper on evaluating source code parsers for ML4SE models, which specifically investigates Tree-sitter's role in machine learning applications for software engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eedc6d31-6d06-4008-9319-71e63fa50564",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "020d38bb-81c2-4392-a5a5-7e7c6de9882f",
  "sourceToolAssistantUUID": "eedc6d31-6d06-4008-9319-71e63fa50564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T03:14:29.909Z_

<details><summary>↩ Tool result · `toolu_0131DM1SDS6MNeX5Dhb3yebL`</summary>

```text
Web search results for query: "Joern code analysis academic paper Yamaguchi "Modeling and Discovering Vulnerabilities with Code Property Graphs" IEEE S&P"

Links: [{"title":"Joern - The Bug Hunter's Workbench | Impact","url":"https://joern.io/impact/"},{"title":"Modeling and Discovering Vulnerabilities with Code Property Graphs | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6956589/"},{"title":"[PDF] Modeling and Discovering Vulnerabilities with Code Property Graphs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-and-Discovering-Vulnerabilities-with-Code-Yamaguchi-Golde/07c4549be429a52274bc0ec083bf5598a3e5c365"},{"title":"Modeling and Discovering Vulnerabilities with Code ...","url":"https://pdfs.semanticscholar.org/d595/fefae63d190b6e9d64f8ea2c0ee5a102c37b.pdf"},{"title":"(PDF) Modeling and Discovering Vulnerabilities with Code Property Graphs","url":"https://www.researchgate.net/publication/263658395_Modeling_and_Discovering_Vulnerabilities_with_Code_Property_Graphs"},{"title":"GraphEye: A Novel Solution for Detecting Vulnerable ...","url":"https://arxiv.org/pdf/2202.02501"},{"title":"Elegant and Scalable Code Querying with Code Property Graphs Fabian Yamaguchi","url":"https://fabianyamaguchi.com/files/2019-cdl.pdf"},{"title":"GitHub - gbrigandi/cpg-rs: A Rust library for working with Code Property Graphs (CPG)","url":"https://github.com/gbrigandi/cpg-rs"},{"title":"Enhancing Software Vulnerability Detection Using Code Property Graphs and Convolutional Neural Networks","url":"https://arxiv.org/html/2503.18175v1"},{"title":"Modeling and Discovering Vulnerabilities with Code Property Graphs","url":"https://comsecuris.com/papers/06956589.pdf"}]

Based on the search results, I found comprehensive information about the academic paper you're looking for:

## Paper Information

The Joern project provides the original implementation of the Code Property Graph, based on the 2014 IEEE Security & Privacy paper "Modeling and Discovering Vulnerabilities with Code Property Graphs". The paper was authored by Fabian Yamaguchi, Nico Golde, Daniel Arp, and Konrad Rieck and published in the 2014 IEEE Symposium on Security and Privacy, with pages 590-604.

## Paper Significance

The paper introduces a novel representation of source code called a code property graph that merges concepts of classic program analysis, namely abstract syntax trees, control flow graphs and program dependence graphs, into a joint data structure. This comprehensive representation enables the authors to elegantly model templates for common vulnerabilities with graph traversals that can identify buffer overflows, integer overflows, and form string vulnerabilities, among others.

## Recent Recognition

In recognition of its long lasting impact, the paper received the IEEE Test-of-Time Award in 2024. Additionally, Joern is by far the most popular tool for code analysis/compilation in the context of automated software vulnerability detection using machine learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b0e19f9-1c76-4ce9-a408-f2468ba545dc",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "078f5a86-7956-4772-b461-d01cbce560f8",
  "sourceToolAssistantUUID": "8b0e19f9-1c76-4ce9-a408-f2468ba545dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:14:30.888Z_

<details><summary>↩ Tool result · `toolu_01EXsZcNbfYy9fqqVCCeSgon`</summary>

```text
Web search results for query: "InferCode Bui 2021 "self-supervised learning of code representation" AST subtrees ICSE"

Links: [{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees (ICSE 2021 - Technical Track) - ICSE 2021","url":"https://2021.icse-conferences.org/details/icse-2021-papers/97/InferCode-Self-Supervised-Learning-of-Code-Representations-by-Predicting-Subtrees"},{"title":"InferCode: Self-Supervised Learning of Code Representations ...","url":"https://oro.open.ac.uk/75238/"},{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9402028/"},{"title":"GitHub - bdqnghi/infercode: [ICSE 2021] - InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees","url":"https://github.com/bdqnghi/infercode"},{"title":"[PDF] InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InferCode:-Self-Supervised-Learning-of-Code-by-Bui-Yu/acd8e24eda17808e3528d2dfd52de1619d13241a"},{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | Request PDF","url":"https://www.researchgate.net/publication/351420922_InferCode_Self-Supervised_Learning_of_Code_Representations_by_Predicting_Subtrees"},{"title":"[2012.07023] InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees","url":"https://arxiv.org/abs/2012.07023"},{"title":"InferCode: Self-Supervised Learning of Code Representations ...","url":"http://www.mysmu.edu/faculty/lxjiang/papers/icse21infercode.pdf"},{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/bui2021infercode/"},{"title":"infercode/README.md at master · bdqnghi/infercode","url":"https://github.com/bdqnghi/infercode/blob/master/README.md?plain=1"}]

I found comprehensive information about the InferCode paper. Here's a summary of the search results:

## InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees

The paper was authored by Nghi D.Q. Bui, Yijun Yu, and Lingxiao Jiang and published at the 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE) in May 2021.

### Core Approach

InferCode adapts the self-supervised learning idea from natural language processing to abstract syntax trees (ASTs) of code, with the key novelty lying in the training of code representations by predicting subtrees automatically identified from the context of ASTs.

### Key Innovation

Subtrees in ASTs are treated as the labels for training the code representations without any human labeling effort or the overhead of expensive graph construction, and the trained representations are no longer tied to any specific downstream tasks or code units.

### Technical Implementation

InferCode was trained using tree-based convolutional neural network (TBCNN) as the encoder on a large set of Java code.

### Applications and Results

The pre-trained model can be applied to downstream unsupervised tasks such as code clustering, code clone detection, cross-language code search, or be reused under a transfer learning scheme for supervised tasks. Compared with prior techniques such as code2vec, code2seq, and ASTNN, the pre-trained InferCode model achieves higher results in most tasks with a significant margin, including tasks involving different programming languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "628ea1f7-8f77-41ed-9484-b26eebd2fec7",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "2c4d039f-8d96-4b35-b61e-e6f0695f6374",
  "sourceToolAssistantUUID": "628ea1f7-8f77-41ed-9484-b26eebd2fec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T03:14:34.324Z_

Let me get a few more details for completeness — the full author list for the CodeQL paper and the exact DOI/pages for InferCode and Joern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4d039f-8d96-4b35-b61e-e6f0695f6374",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dHAabX4jW4KV6umzGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc27f691-358d-4e45-9b0c-c6ade302faf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122PDphbZxVUbEj8KieB14d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4580,
      "cache_read_input_tokens": 14790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4580,
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

_source line 18 · 2026-05-15T03:14:35.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XFMo7zDVfKCm5PQmsFzYE5`</summary>

```json
{
  "query": "Pavel Avgustinov Oege de Moor Michael Peyton Jones Max Schäfer \"QL: Object-oriented Queries on Relational Data\" ECOOP 2016 DOI LIPIcs full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc27f691-358d-4e45-9b0c-c6ade302faf0",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dHAabX4jW4KV6umzGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f977861c-ade2-423f-932f-7ff53f1a34a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122PDphbZxVUbEj8KieB14d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4580,
      "cache_read_input_tokens": 14790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4580,
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

_source line 19 · 2026-05-15T03:14:36.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144tbCYdDkGy4z7jMkaC9bh`</summary>

```json
{
  "query": "InferCode Bui Yu Jiang ICSE 2021 DOI pages IEEE 9402028"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f977861c-ade2-423f-932f-7ff53f1a34a6",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dHAabX4jW4KV6umzGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f68fb2fd-c4f0-44c7-bb0f-2f5bbe3f4b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122PDphbZxVUbEj8KieB14d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4580,
      "cache_read_input_tokens": 14790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4580,
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

_source line 20 · 2026-05-15T03:14:36.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HTLdFtk8Ld8j8sRVfAzSdB`</summary>

```json
{
  "query": "tree-sitter Max Brunsfeld academic citation \"incremental parsing\" paper reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68fb2fd-c4f0-44c7-bb0f-2f5bbe3f4b59",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dHAabX4jW4KV6umzGa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ef46bc2-f6f9-4fa4-ac46-f3e326dbbad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122PDphbZxVUbEj8KieB14d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4580,
      "cache_read_input_tokens": 14790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4580,
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

_source line 21 · 2026-05-15T03:14:40.829Z_

<details><summary>↩ Tool result · `toolu_0144tbCYdDkGy4z7jMkaC9bh`</summary>

```text
Web search results for query: "InferCode Bui Yu Jiang ICSE 2021 DOI pages IEEE 9402028"

Links: [{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees (ICSE 2021 - Technical Track) - ICSE 2021","url":"https://2021.icse-conferences.org/details/icse-2021-papers/97/InferCode-Self-Supervised-Learning-of-Code-Representations-by-Predicting-Subtrees"},{"title":"InferCode: Self-Supervised Learning of Code Representations ...","url":"https://oro.open.ac.uk/75238/"},{"title":"[PDF] InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InferCode:-Self-Supervised-Learning-of-Code-by-Bui-Yu/acd8e24eda17808e3528d2dfd52de1619d13241a"},{"title":"infercode/README.md at master · bdqnghi/infercode","url":"https://github.com/bdqnghi/infercode/blob/master/README.md?plain=1"},{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | Request PDF","url":"https://www.researchgate.net/publication/351420922_InferCode_Self-Supervised_Learning_of_Code_Representations_by_Predicting_Subtrees"},{"title":"GitHub - bdqnghi/infercode: [ICSE 2021] - InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees","url":"https://github.com/bdqnghi/infercode"},{"title":"infercode 0.0.28 on PyPI - Libraries.io","url":"https://libraries.io/pypi/infercode"},{"title":"InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9402028/"},{"title":"Yu, Yijun - Open Research Online","url":"https://oro.open.ac.uk/view/person/yy66.html"},{"title":"Yu Jiang - ICSE 2021","url":"https://2021.icse-conferences.org/profile/yujiang"}]

Based on the search results, I found the information about the InferCode paper:

**Authors:** Nghi D. Q. Bui, Yijun Yu, Lingxiao Jiang

**Title:** InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees

**Conference:** 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)

**Pages:** 1186–1197

**Year:** 2021

**Organization:** IEEE

**DOI:** 10.1109/ICSE43902.2021.00109

The paper was presented in ICSE 2021 and proposes InferCode, which adapts self-supervised learning to abstract syntax trees (ASTs) of code by predicting subtrees automatically identified from the context of ASTs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f68fb2fd-c4f0-44c7-bb0f-2f5bbe3f4b59",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "804aa0f3-2c70-4446-aaf8-dd0763218d4d",
  "sourceToolAssistantUUID": "f68fb2fd-c4f0-44c7-bb0f-2f5bbe3f4b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T03:14:42.288Z_

<details><summary>↩ Tool result · `toolu_01HTLdFtk8Ld8j8sRVfAzSdB`</summary>

```text
Web search results for query: "tree-sitter Max Brunsfeld academic citation "incremental parsing" paper reference"

Links: [{"title":"Tree-sitter: Revolutionizing Parsing with an Incremental Parsing Library","url":"https://www.deusinmachina.net/p/tree-sitter-revolutionizing-parsing"},{"title":"GitHub - tree-sitter/tree-sitter: An incremental parsing system for programming tools · GitHub","url":"https://github.com/tree-sitter/tree-sitter"},{"title":"Tree-sitter | notes","url":"https://thaliaarchi.github.io/notes/topics/tree-sitter.html"},{"title":"Tree-sitter - a new parsing system for programming tools - Strange Loop","url":"https://www.thestrangeloop.com/2018/tree-sitter---a-new-parsing-system-for-programming-tools.html"},{"title":"(PDF) SMIE: Weakness is Power!: Auto-indentation with incomplete information","url":"https://www.researchgate.net/publication/341924321_SMIE_Weakness_is_Power_Auto-indentation_with_incomplete_information"},{"title":"tree-sitter/tree-sitter: An incremental parsing system for programming tools - tree-sitter - Gitea: Git with a cup of tea","url":"https://gitea.com/tree-sitter/tree-sitter"},{"title":"fast Scala 3 parsing with tree-sitter · eed3si9n","url":"https://eed3si9n.com/fast-scala3-parsing-with-tree-sitter/"},{"title":"maxbrunsfeld (Max Brunsfeld) · GitHub","url":"https://github.com/maxbrunsfeld"},{"title":"Hacker News Comments on \"\"Tree-sitter - a new parsing system for programming tools\" by Max Brunsfeld\" Strange Loop Conference Youtube Video | HN Theater","url":"https://yahnd.com/theater/r/youtube/Jes3bD6P0To/"},{"title":"tree-sitter · GitHub","url":"https://github.com/tree-sitter"}]

Based on the search results, here's what I found regarding Tree-sitter, Max Brunsfeld, and relevant academic citations:

## Main Reference

The primary citation is: Max Brunsfeld. Tree-sitter - a new parsing system for programming tools. Strange Loop Conference, 2018.

## Additional Context

Max Brunsfeld was the creator of Tree-sitter, and he developed it out of the need for an incremental parsing solution that was faster than the state of the art at the time. Tree-sitter was announced to the public in a GitHub blog post in 2018.

## Academic Influences

The search results also indicate there are academic papers that influenced Tree-sitter's design. One research paper that greatly influenced the design of Tree-sitter is "Practical Algorithms for Incremental Software Development Environments" by Tim A. Wagner, 1998.

The main academic citation you're looking for appears to be the Strange Loop Conference 2018 presentation by Max Brunsfeld, which introduced Tree-sitter as a new parsing system with incremental parsing capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ef46bc2-f6f9-4fa4-ac46-f3e326dbbad7",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "b8f89cd0-0b42-45bf-b6ab-9fd01f2f466b",
  "sourceToolAssistantUUID": "8ef46bc2-f6f9-4fa4-ac46-f3e326dbbad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T03:14:43.089Z_

<details><summary>↩ Tool result · `toolu_01XFMo7zDVfKCm5PQmsFzYE5`</summary>

```text
Web search results for query: "Pavel Avgustinov Oege de Moor Michael Peyton Jones Max Schäfer "QL: Object-oriented Queries on Relational Data" ECOOP 2016 DOI LIPIcs full author list"

Links: [{"title":"QL: Object-oriented Queries on Relational Data (ECOOP 2016 - Research Track) - ECOOP 2016","url":"https://2016.ecoop.org/details/ecoop-2016-papers/17/QL-Object-oriented-Queries-on-Relational-Data"},{"title":"QL: Object-oriented Queries on Relational Data - DROPS","url":"https://drops.dagstuhl.de/storage/00lipics/lipics-vol056-ecoop2016/LIPIcs.ECOOP.2016.2/LIPIcs.ECOOP.2016.2.pdf"},{"title":"[PDF] QL: Object-oriented Queries on Relational Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-oriented-Queries-on-Relational-Data-Avgustinov-Moor/8d941602bca76656dacfa1062fc9ef481deb6680"},{"title":"QL: Object-oriented Queries on Relational Data","url":"https://drops.dagstuhl.de/opus/volltexte/2016/6096/"},{"title":"dblp: 30. ECOOP 2016","url":"https://dblp.org/db/conf/ecoop/ecoop2016.html"},{"title":"Academic publications - CodeQL - GitHub","url":"https://codeql.github.com/publications/"},{"title":"30th European Conference on Object-Oriented Programming, ECOOP 2016, July 18-22, 2016, Rome, Italy - researchr publication","url":"https://researchr.org/publication/ecoop-2016"},{"title":".QL: Object-Oriented Queries Made Easy | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-540-88643-3_3"},{"title":"(PDF) .QL: Object-Oriented Queries Made Easy","url":"https://www.researchgate.net/publication/221202308_QL_Object-Oriented_Queries_Made_Easy"},{"title":"[PDF] .QL: Object-Oriented Queries Made Easy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-Oriented-Queries-Made-Easy-Moor-Sereni/d7be52e78154dbde1884f07510fa7901b9915277"}]

Based on the search results, here is the information about the paper:

**Full Citation:**

Pavel Avgustinov, Oege de Moor, Michael Peyton Jones, and Max Schäfer. QL: Object-oriented Queries on Relational Data. In 30th European Conference on Object-Oriented Programming (ECOOP 2016). Leibniz International Proceedings in Informatics (LIPIcs), Volume 56, pp. 2:1-2:25, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2016) https://doi.org/10.4230/LIPIcs.ECOOP.2016.2

**Complete Author List:**
Pavel Avgustinov, Oege de Moor, Michael Peyton Jones, and Max Schäfer

**DOI:** 10.4230/LIPIcs.ECOOP.2016.2

**Publication Details:**
- Conference: 30th European Conference on Object-Oriented Programming (ECOOP 2016)
- Location: Rome, Italy
- Date: July 18-22, 2016
- Series: Leibniz International Proceedings in Informatics (LIPIcs)
- Volume: 56
- Pages: 2:1-2:25
- Publisher: Schloss Dagstuhl – Leibniz-Zentrum für Informatik


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f977861c-ade2-423f-932f-7ff53f1a34a6",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "d4ca30b7-edd7-4515-9eff-0f58f16afe36",
  "sourceToolAssistantUUID": "f977861c-ade2-423f-932f-7ff53f1a34a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T03:14:46.523Z_

Let me get one more search to find the Joern paper's exact DOI and confirm pages, plus check for an earlier QL paper that may also be relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4ca30b7-edd7-4515-9eff-0f58f16afe36",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dJ4nNSqiACHBo6c1f8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6a48c04-f76b-4996-86c9-016f3d8ba880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyTgcJibchGK6E7G4g6M5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1636,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 19370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 25 · 2026-05-15T03:14:48.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156fth2Df7wapsKBfJecfFQ`</summary>

```json
{
  "query": "Yamaguchi Golde Arp Rieck \"Modeling and Discovering Vulnerabilities with Code Property Graphs\" 2014 IEEE S&P DOI pages 590"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6a48c04-f76b-4996-86c9-016f3d8ba880",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dJ4nNSqiACHBo6c1f8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "366c533f-0996-426a-b8d9-2c82654927af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyTgcJibchGK6E7G4g6M5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1636,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 19370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 26 · 2026-05-15T03:14:49.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015F6wPqynwYQ9tnX2AW7i4y`</summary>

```json
{
  "query": "Avgustinov de Moor Jones Sherfer ECOOP 2016 QL earlier version \".QL Object-Oriented Queries Made Easy\" GTTSE 2007"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "366c533f-0996-426a-b8d9-2c82654927af",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dJ4nNSqiACHBo6c1f8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f78559-eca1-41dd-a5b1-4582b3967c94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyTgcJibchGK6E7G4g6M5n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1636,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 19370,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1636,
          "output_tokens": 205,
          "cache_read_input_tokens": 19370,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1411,
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

_source line 27 · 2026-05-15T03:14:51.566Z_

<details><summary>↩ Tool result · `toolu_0156fth2Df7wapsKBfJecfFQ`</summary>

```text
Web search results for query: "Yamaguchi Golde Arp Rieck "Modeling and Discovering Vulnerabilities with Code Property Graphs" 2014 IEEE S&P DOI pages 590"

Links: [{"title":"[PDF] Modeling and Discovering Vulnerabilities with Code Property Graphs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-and-Discovering-Vulnerabilities-with-Code-Yamaguchi-Golde/07c4549be429a52274bc0ec083bf5598a3e5c365"},{"title":"dblp: Modeling and Discovering Vulnerabilities with Code Property Graphs.","url":"https://dblp.org/rec/conf/sp/YamaguchiGAR14.html"},{"title":"Figure 4 from Modeling and Discovering Vulnerabilities with Code Property Graphs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-and-Discovering-Vulnerabilities-with-Code-Yamaguchi-Golde/07c4549be429a52274bc0ec083bf5598a3e5c365/figure/3"},{"title":"Modeling and Discovering Vulnerabilities with Code ...","url":"https://pdfs.semanticscholar.org/d595/fefae63d190b6e9d64f8ea2c0ee5a102c37b.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Yamaguchi%2C+F.%2C+Golde%2C+N.%2C+Arp%2C+D.%2C+Rieck%2C+K.%3A+Modeling+and+discovering+vulnerabilities+with+code+property+graphs.+In%3A+Security+and+Privacy%2C+pp.+590%E2%80%93604+%282014%29"},{"title":"Modeling and Discovering Vulnerabilities with Code Property Graphs | Proceedings of the 2014 IEEE Symposium on Security and Privacy","url":"https://dl.acm.org/doi/10.1109/sp.2014.44"},{"title":"Modeling and Discovering Vulnerabilities with Code Property Graphs","url":"https://www.ieee-security.org/TC/SP2014/papers/ModelingandDiscoveringVulnerabilitieswithCodePropertyGraphs.pdf"},{"title":"Enhancing Software Vulnerability Detection Using Code Property Graphs and Convolutional Neural Networks","url":"https://arxiv.org/html/2503.18175v1"},{"title":"(PDF) Modeling and Discovering Vulnerabilities with Code Property Graphs","url":"https://www.researchgate.net/publication/263658395_Modeling_and_Discovering_Vulnerabilities_with_Code_Property_Graphs"},{"title":"Modeling and Discovering Vulnerabilities with Code Property Graphs | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6956589/"}]

I found information about the paper you're searching for. Here are the details:

The paper "Modeling and Discovering Vulnerabilities with Code Property Graphs" by Fabian Yamaguchi, Nico Golde, Dan Arp, and Konrad Rieck was published in the 2014 IEEE Symposium on Security and Privacy on May 18, 2014, with pages 590-604 and DOI 10.1109/SP.2014.44.

The paper introduces a novel representation of source code called a code property graph that merges concepts of abstract syntax trees, control flow graphs and program dependence graphs into a joint data structure, which enables modeling of templates for common vulnerabilities such as buffer overflows and integer overflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "366c533f-0996-426a-b8d9-2c82654927af",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "cd2201bb-b33c-4b3b-a59c-8e9cbbbfc6e2",
  "sourceToolAssistantUUID": "366c533f-0996-426a-b8d9-2c82654927af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T03:14:58.473Z_

<details><summary>↩ Tool result · `toolu_015F6wPqynwYQ9tnX2AW7i4y`</summary>

```text
Web search results for query: "Avgustinov de Moor Jones Sherfer ECOOP 2016 QL earlier version ".QL Object-Oriented Queries Made Easy" GTTSE 2007"

Links: [{"title":"30th European Conference on Object-Oriented Programming (ECOOP 2016)","url":"https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-56"},{"title":"QL: Object-oriented Queries on Relational Data - DROPS","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2016.2"},{"title":"QL: Object-oriented Queries on Relational Data (ECOOP 2016 - Research Track) - ECOOP 2016","url":"https://2016.ecoop.org/details/ecoop-2016-papers/17/QL-Object-oriented-Queries-on-Relational-Data"},{"title":"The Pyttern Program Query Language - DROPS","url":"https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.Programming.2025.23"},{"title":"Variant Analysis with QL | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-319-95582-7_42"},{"title":"Queries with External Predicates - DROPS - Schloss Dagstuhl","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2025.22"},{"title":"30th European Conference on Object-Oriented Programming, ECOOP 2016, July 18-22, 2016, Rome, Italy - researchr publication","url":"https://researchr.org/publication/ecoop-2016"},{"title":"Breaking the Negative Cycle: Exploring the Design Space of Stratification for First-Class Datalog Constraints","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2023.31"},{"title":"[PDF] QL: Object-oriented Queries on Relational Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-oriented-Queries-on-Relational-Data-Avgustinov-Moor/8d941602bca76656dacfa1062fc9ef481deb6680"},{"title":"dblp: 30. ECOOP 2016","url":"https://dblp.org/db/conf/ecoop/ecoop2016.html"}]

Now let me search for information about the GTTSE 2007 earlier version:

Links: [{"title":"QL: Object-oriented Queries on Relational Data - DROPS","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2016.2"},{"title":"(PDF) .QL: Object-Oriented Queries Made Easy","url":"https://www.researchgate.net/publication/221202308_QL_Object-Oriented_Queries_Made_Easy"},{"title":".QL: Object-Oriented Queries Made Easy | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-540-88643-3_3"},{"title":"Academic publications - CodeQL - GitHub","url":"https://codeql.github.com/publications/"},{"title":"dblp: Generative and Transformational Techniques in Software Engineering 2007","url":"https://dblp.org/db/conf/gttse/gttse2007.html"},{"title":"[PDF] QL: Object-oriented Queries on Relational Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-oriented-Queries-on-Relational-Data-Avgustinov-Moor/8d941602bca76656dacfa1062fc9ef481deb6680"},{"title":"[PDF] .QL: Object-Oriented Queries Made Easy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QL:-Object-Oriented-Queries-Made-Easy-Moor-Sereni/d7be52e78154dbde1884f07510fa7901b9915277"},{"title":"Lecture Notes in Computer Science Ser.: Generative and Transformational Techniques in Software Engineering II : International Summer School, GTTSE 2007, Braga, Portugal, July 2007, Revised Papers by Joost Visser (2008, Trade Paperback) for sale online | eBay","url":"https://www.ebay.com/p/71188588"},{"title":".QL: Object-Oriented Queries Made Easy","url":"https://link.springer.com/content/pdf/10.1007/978-3-540-88643-3_3.pdf"},{"title":".QL: Object-Oriented Queries Made Easy","url":"http://www.researchgate.net/profile/Torbjorn_Ekman/publication/221202308_.QL_Object-Oriented_Queries_Made_Easy/links/54d3e2d40cf246475803a900.pdf"}]

Based on my web search results, I found the information you're looking for:

The authors Oege de Moor, Damien Sereni, Mathieu Verbaere, Elnar Hajiyev, Pavel Avgustinov, Torbjörn Ekman, Neil Ongkingco, and Julian Tibble published ".QL: Object-oriented queries made easy" in GTTSE 2007. 

Later, Pavel Avgustinov, Oege de Moor, Michael Peyton Jones, and Max Schäfer published "QL: Object-oriented Queries on Relational Data" in the 30th European Conference on Object-Oriented Programming (ECOOP 2016).

So the GTTSE 2007 paper titled ".QL: Object-Oriented Queries Made Easy" was indeed an earlier version of the work that was later presented as "QL: Object-oriented Queries on Relational Data" at ECOOP 2016. The GTTSE 2007 version was authored by a broader team including more co-authors than appeared in the ECOOP 2016 publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56f78559-eca1-41dd-a5b1-4582b3967c94",
  "isSidechain": true,
  "promptId": "1e09569d-8f0d-4ac9-a93e-affea5b986a2",
  "agentId": "a6f54155fec009ea1",
  "type": "user",
  "uuid": "ab1ac39f-13fd-4ebf-a2da-b1fe6af3cb5f",
  "sourceToolAssistantUUID": "56f78559-eca1-41dd-a5b1-4582b3967c94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T03:15:19.439Z_

Here are the verified publication details for all five references:

---

**1. CodeQL / QL**

There are two key papers. The canonical academic reference for the QL language underlying CodeQL is:

- **Authors:** Pavel Avgustinov, Oege de Moor, Michael Peyton Jones, Max Schäfer
- **Title:** "QL: Object-oriented Queries on Relational Data"
- **Venue:** 30th European Conference on Object-Oriented Programming (ECOOP 2016), LIPIcs, Volume 56, pp. 2:1--2:25
- **Year:** 2016
- **DOI:** `10.4230/LIPIcs.ECOOP.2016.2`

An earlier version of the language was published as:

- **Authors:** Oege de Moor, Damien Sereni, Mathieu Verbaere, Elnar Hajiyev, Pavel Avgustinov, Torbjörn Ekman, Neil Ongkingco, Julian Tibble
- **Title:** ".QL: Object-Oriented Queries Made Easy"
- **Venue:** GTTSE 2007, Lecture Notes in Computer Science, Springer
- **Year:** 2007 (revised papers published 2008)

The ECOOP 2016 paper is the more commonly cited academic reference for CodeQL/Semmle QL.

---

**2. Tree-sitter**

Tree-sitter has **no formal academic paper**. It is an open-source project by Max Brunsfeld. The best citable reference is:

- **Author:** Max Brunsfeld
- **Title:** "Tree-sitter -- a new parsing system for programming tools"
- **Venue:** Strange Loop Conference 2018 (talk/presentation, not a peer-reviewed paper)
- **URL:** https://github.com/tree-sitter/tree-sitter

For a bibliography, cite the GitHub repository or the Strange Loop talk. If you need an academic paper that uses tree-sitter for code structure in the ML/SE context, a relevant one is:

- **Authors:** Ilya Utkin et al.
- **Title:** "Evaluating the Impact of Source Code Parsers on ML4SE Models"
- **Year:** 2022
- **arXiv:** `2206.08713`

---

**3. Program Dependence Graph**

- **Authors:** Jeanne Ferrante, Karl J. Ottenstein, Joe D. Warren
- **Title:** "The Program Dependence Graph and Its Use in Optimization"
- **Venue:** ACM Transactions on Programming Languages and Systems (TOPLAS), Vol. 9, No. 3, pp. 319--349
- **Year:** July 1987
- **DOI:** `10.1145/24039.24041`

---

**4. Joern / Code Property Graphs**

- **Authors:** Fabian Yamaguchi, Nico Golde, Daniel Arp, Konrad Rieck
- **Title:** "Modeling and Discovering Vulnerabilities with Code Property Graphs"
- **Venue:** 2014 IEEE Symposium on Security and Privacy (IEEE S&P), pp. 590--604
- **Year:** 2014
- **DOI:** `10.1109/SP.2014.44`

Note: This paper received the IEEE Test-of-Time Award in 2024.

---

**5. InferCode**

- **Authors:** Nghi D. Q. Bui, Yijun Yu, Lingxiao Jiang
- **Title:** "InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees"
- **Venue:** 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE), pp. 1186--1197
- **Year:** 2021
- **DOI:** `10.1109/ICSE43902.2021.00109`
- **arXiv:** `2012.07023`

---

Sources:
- [QL: Object-oriented Queries on Relational Data (DROPS)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2016.2)
- [CodeQL Academic Publications](https://codeql.github.com/publications/)
- [.QL: Object-Oriented Queries Made Easy (Springer)](https://link.springer.com/chapter/10.1007/978-3-540-88643-3_3)
- [Tree-sitter GitHub repository](https://github.com/tree-sitter/tree-sitter)
- [Evaluating the Impact of Source Code Parsers on ML4SE Models (arXiv)](https://arxiv.org/pdf/2206.08713)
- [The Program Dependence Graph (ACM DL)](https://dl.acm.org/doi/10.1145/24039.24041)
- [Modeling and Discovering Vulnerabilities with Code Property Graphs (IEEE Xplore)](https://ieeexplore.ieee.org/document/6956589/)
- [Joern Impact Page](https://joern.io/impact/)
- [InferCode (IEEE Xplore)](https://ieeexplore.ieee.org/document/9402028/)
- [InferCode (arXiv)](https://arxiv.org/abs/2012.07023)
- [InferCode ICSE 2021 page](https://2021.icse-conferences.org/details/icse-2021-papers/97/InferCode-Self-Supervised-Learning-of-Code-Representations-by-Predicting-Subtrees)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab1ac39f-13fd-4ebf-a2da-b1fe6af3cb5f",
  "isSidechain": true,
  "agentId": "a6f54155fec009ea1",
  "requestId": "req_011Cb3dKCVVzW9dwbmzbBTuD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f3c0717-cb4f-4861-aa22-1fc0257409d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "8c3dfb9b-6330-40ad-a7df-88d6f823d16e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyTb1JyAMNnEN2bQN1d77H",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20781,
      "output_tokens": 1374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1374,
          "cache_read_input_tokens": 20781,
          "cache_creation_input_tokens": 4402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4402,
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
