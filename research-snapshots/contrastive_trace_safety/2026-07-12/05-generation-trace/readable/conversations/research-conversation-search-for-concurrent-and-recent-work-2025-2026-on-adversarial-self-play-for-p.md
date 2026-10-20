# Research conversation: Search for concurrent and recent work (2025-2026) on adversarial self-play for patch verification, adversarial test gene

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af8b74f330792cf27.jsonl`
- **Structured JSON:** [`ae13f2b8101517874ef5.json`](../../sessions/ae/ae13f2b8101517874ef5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-11T20:55:15.107Z_

Search for concurrent and recent work (2025-2026) on adversarial self-play for patch verification, adversarial test generation for program repair, and self-play bug repair. I need to know if anyone is already doing this specific combination.

Perform these searches using WebSearch:
1. "adversarial test generation patch verification self-play 2026"
2. "adversarial test generation program repair 2025 2026"
3. "self-play patch verification test time" on arxiv
4. "solver verifier self-play program repair"
5. Search arxiv for recent (last 3 months) papers on "adversarial test generation for automated program repair"
6. Search OpenReview for ICML 2026, NeurIPS 2026, ICLR 2026 submissions related to "self-play program repair" or "adversarial patch verification"

For each relevant paper found, report: title, authors, venue/arxiv ID, date, and a 1-sentence summary of how it relates. Flag any that are highly similar to the proposed idea of using self-play between patch generation and adversarial test generation at test time (no additional training) to improve repair quality.

Report your findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "b5f8e8dd-fdf2-499d-bf3e-5fbd15f7af30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T20:55:15.111Z_

```json
{
  "parentUuid": "b5f8e8dd-fdf2-499d-bf3e-5fbd15f7af30",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9f917600-dbbe-4776-98b2-7538e041095b",
  "timestamp": "2026-05-11T20:55:15.111Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T20:55:17.929Z_



I'll load the WebSearch tool first, then execute all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f917600-dbbe-4776-98b2-7538e041095b",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSvzYcHFCajCXtskPMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "128a9553-8975-47d0-a3b7-fae80c0906e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpaVpEQCNkKy6gBdp4wBZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 824,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T20:55:18.017Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WSJb4XEq6gEDMJ6sBHCWnb`</summary>

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
  "parentUuid": "128a9553-8975-47d0-a3b7-fae80c0906e3",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSvzYcHFCajCXtskPMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4741abc-da31-406e-b584-2acdeb3e90df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpaVpEQCNkKy6gBdp4wBZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 824,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T20:55:18.022Z_

<details><summary>↩ Tool result · `toolu_01WSJb4XEq6gEDMJ6sBHCWnb`</summary>

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
  "parentUuid": "c4741abc-da31-406e-b584-2acdeb3e90df",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "b5c63b9b-02ab-4282-9f0c-3015d5919a9a",
  "sourceToolAssistantUUID": "c4741abc-da31-406e-b584-2acdeb3e90df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T20:55:20.731Z_



Now I'll run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c63b9b-02ab-4282-9f0c-3015d5919a9a",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f89d6f01-4411-4d0e-945d-6d78113cf944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-11T20:55:21.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SpmmDx2vBoFvcwKerM7ZzV`</summary>

```json
{
  "query": "adversarial test generation patch verification self-play 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f89d6f01-4411-4d0e-945d-6d78113cf944",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c70b89a1-5b80-474a-8e10-293e8c6c9e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-11T20:55:21.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByyS75GihNR6AsWFuFvSrV`</summary>

```json
{
  "query": "adversarial test generation program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c70b89a1-5b80-474a-8e10-293e8c6c9e18",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e13c602-5c98-4381-9770-02bf905837e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-11T20:55:22.122Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jdh9irJX64AYx5LX5q7kgy`</summary>

```json
{
  "query": "self-play patch verification test time arxiv",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e13c602-5c98-4381-9770-02bf905837e5",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eec1204-1e95-47ba-9050-0b95a17b2925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-11T20:55:22.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017FHXiq1by7cZjVFjrGGXwm`</summary>

```json
{
  "query": "solver verifier self-play program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eec1204-1e95-47ba-9050-0b95a17b2925",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c5b0bc6-db29-47fe-ac85-e4e5ad0f39c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-11T20:55:23.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018eYAUfT6dv8hN6nNCAbQo4`</summary>

```json
{
  "query": "arxiv 2026 adversarial test generation automated program repair recent",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c5b0bc6-db29-47fe-ac85-e4e5ad0f39c8",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4312e263-e651-4162-95d9-90f66ed97062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-11T20:55:23.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01162V8W1BtzLaHW9Rpsp4Bd`</summary>

```json
{
  "query": "site:openreview.net ICML 2026 NeurIPS 2026 ICLR 2026 \"self-play program repair\" OR \"adversarial patch verification\"",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4312e263-e651-4162-95d9-90f66ed97062",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSwDJZjEsochyG6rCjF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c886f77b-fdb3-433e-a346-e353664784b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyEJ2GZbN3wYA925CW2rUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9047,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 409,
          "cache_read_input_tokens": 9047,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 13 · 2026-05-11T20:55:29.380Z_

<details><summary>↩ Tool result · `toolu_01SpmmDx2vBoFvcwKerM7ZzV`</summary>

```text
Web search results for query: "adversarial test generation patch verification self-play 2026"

Links: [{"title":"Toward Training Superintelligent Software Agents through Self-Play SWE-RL","url":"https://arxiv.org/pdf/2512.18552"},{"title":"[2603.15611] Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/abs/2603.15611"},{"title":"Paper page - Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://huggingface.co/papers/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/html/2603.15611v1"},{"title":"Self-Play SWE-RL for Superintelligent Agents","url":"https://www.emergentmind.com/papers/2512.18552"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://arxiv.org/html/2506.11442v1"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/html/2502.14948v4"},{"title":"Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification","url":"https://arxiv.org/html/2604.17010"},{"title":"OpenAEV | Adversarial Exposure Validation Platform by Filigran","url":"https://filigran.io/platform/openaev/"},{"title":"Self-Improving AI Agents through Self-Play","url":"https://arxiv.org/html/2512.02731v1"}]

Based on the search results, I found several recent research papers from 2026 on adversarial test generation, patch verification, and self-play approaches in machine learning:

## Key Findings:

**Code-A1: Adversarial Evolving Framework (March 2026)**

Code-A1 is an adversarial co-evolution framework that jointly optimizes a Code LLM and a Test LLM with opposing objectives, where the Code LLM is rewarded for passing more tests, while the Test LLM is rewarded for exposing more defects. Recent self-play methods face an inherent dilemma: white-box access leads to self-collusion where the model produces trivial tests for easy rewards, yet black-box restriction yields generic tests that miss implementation-specific bugs. This architectural separation eliminates self-collusion risks and safely enables white-box test generation, where the Test LLM can inspect candidate code to craft targeted adversarial tests.

**Self-Play SWE-RL for Software Engineering (December 2025)**

After applying a model-generated patch, the test suite is run to verify correctness. Inverse mutation testing verifies that each file in the bug-injection patch is necessary to trigger the bug by checking if reverting a file causes failing tests to pass, using this approach to validate that each buggy file can be detected by the tests.

**Sol-Ver: Solver-Verifier Self-Play Framework (March 2026)**

Sol-Ver proposes a self-play solver-verifier framework where the model itself verifies the correctness of its own data and jointly improves a single model's code and test generation capacity.

These approaches represent cutting-edge research in using adversarial interactions and self-play mechanisms to improve code generation and verification systems in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c70b89a1-5b80-474a-8e10-293e8c6c9e18",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "d85db375-4008-4f41-87a7-83a4cd84003d",
  "sourceToolAssistantUUID": "c70b89a1-5b80-474a-8e10-293e8c6c9e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T20:55:29.798Z_

<details><summary>↩ Tool result · `toolu_01162V8W1BtzLaHW9Rpsp4Bd`</summary>

```text
Web search results for query: "site:openreview.net ICML 2026 NeurIPS 2026 ICLR 2026 "self-play program repair" OR "adversarial patch verification""

No links found.

I wasn't able to find any results for that specific search query. This could be because:

1. **The search terms are too restrictive**: The combination of site restriction, multiple conference names, and specific phrase searches may be filtering out relevant results
2. **Papers may not be indexed yet**: If you're looking for very recent submissions to ICML 2026, NeurIPS 2026, or ICLR 2026, they may not yet be indexed by search engines
3. **The specific phrases may not appear together**: Papers on these topics might use different terminology

If you're looking for papers on these topics, I'd recommend:
- Visiting OpenReview.net directly and using their search interface
- Searching for each conference separately (e.g., "ICML 2026 site:openreview.net")
- Trying broader search terms without the specific phrases
- Checking the conference websites directly for submission timelines and accepted papers

Would you like me to try a different search query with fewer restrictions?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c886f77b-fdb3-433e-a346-e353664784b9",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "3f61100d-0c3e-4d3f-a9e1-bf1bff927128",
  "sourceToolAssistantUUID": "c886f77b-fdb3-433e-a346-e353664784b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T20:55:30.262Z_

<details><summary>↩ Tool result · `toolu_01ByyS75GihNR6AsWFuFvSrV`</summary>

```text
Web search results for query: "adversarial test generation program repair 2025 2026"

Links: [{"title":"Adversarial Reasoning for Repair Based on Inferred ...","url":"https://arxiv.org/pdf/2505.13008"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3728939"},{"title":"Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair","url":"https://arxiv.org/html/2509.05372v2"},{"title":"AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent (ISSTA 2025 - Research Papers) - ISSTA 2025","url":"https://conf.researchr.org/details/issta-2025/issta-2025-papers/61/AdverIntent-Agent-Adversarial-Reasoning-for-Repair-Based-on-Inferred-Program-Intent"},{"title":"Adversarial patch generation for automated program repair | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09709-4"},{"title":"Adversarial Reasoning for Repair Based on Inferred Program Intent","url":"https://arxiv.org/html/2505.13008v1"},{"title":"Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair | Andreas Happe","url":"https://snikt.net/blog/2025/09/04/adversarial-bug-reports-as-a-security-risk-in-language-model-based-automated-program-repair/"},{"title":"OpenAEV | Adversarial Exposure Validation Platform by Filigran","url":"https://filigran.io/platform/openaev/"},{"title":"Adversarial Exposure Validation (AEV) - The Definitive Guide to 2025 Trends, Challenges, Innovations, and 2026 Projections in Cybersecurity - Cyber Strategy Institute","url":"https://cyberstrategyinstitute.com/adversarial-exposure-validation-aev-the-definitive-guide-to-2025-trends-challenges-innovations-and-2026-projections-in-cybersecurity/"}]

Based on the search results, here are the key findings about adversarial test generation and program repair in 2025-2026:

## AdverIntent-Agent (2025)

A notable recent research paper published in June 2025 introduces AdverIntent-Agent, presented at ISSTA 2025. This multi-agent approach consists of three agents: a reasoning agent that generates adversarial program intents along with faulty statements, a test agent that produces adversarial test cases aligned with each inferred intent, and a repair agent that generates patches using LLM prompts to satisfy both the inferred program intent and the generated tests.

The approach was evaluated on Defects4J 2.0 and HumanEval-Java benchmarks, correctly repairing 77 and 105 bugs respectively. The work addresses a key limitation where most APR tools focus on code transformations specified by test suites rather than reasoning about program intent, often generating patches that overfit incomplete test suites and fail to reflect developer intentions.

## Security Concerns in APR Systems (2026)

Recent research from 2026 investigates how adversarial bug reports can exploit LLM-powered repair systems, compromise CI/CD pipelines, and waste developer and compute resources. The findings show that current defenses are insufficient: 90% of crafted bug reports triggered attacker-aligned patches, with the best pre-repair filter blocking only 47%, while post-repair analysis was effective in just 58% of cases.

## Adversarial Patch Generation

The NEVERMORE approach uses Generative Adversarial Networks architecture trained on historical bug fixes to generate repairs that closely mimic human-produced fixes, with empirical evaluation on 500 real-world bugs demonstrating 21.2% effectiveness in matching human fixes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e13c602-5c98-4381-9770-02bf905837e5",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "e299004b-c854-4773-bc1c-9af5fdd207b2",
  "sourceToolAssistantUUID": "0e13c602-5c98-4381-9770-02bf905837e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T20:55:30.944Z_

<details><summary>↩ Tool result · `toolu_017FHXiq1by7cZjVFjrGGXwm`</summary>

```text
Web search results for query: "solver verifier self-play program repair"

Links: [{"title":"(PDF) Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://www.researchgate.net/publication/398978797_Propose_Solve_Verify_Self-Play_Through_Formal_Verification"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/html/2512.18160"},{"title":"Self-Play SWE-RL for Superintelligent Agents","url":"https://www.emergentmind.com/papers/2512.18552"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/html/2502.14948"},{"title":"VERSE: Verification-based Self-Play for Code Instructions | OpenReview","url":"https://openreview.net/forum?id=woKbSkgDsq"},{"title":"VERSE: Verification-based Self-Play for Code Instructions","url":"https://www.researchgate.net/publication/390700425_VERSE_Verification-based_Self-Play_for_Code_Instructions"},{"title":"[2502.14948] Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/abs/2502.14948"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Mutually Improving Code and Test Generation | OpenReview","url":"https://openreview.net/forum?id=j6tMZaPWWF"},{"title":"VERSE: Verification-based Self-Play for Code Instructions | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34604"},{"title":"Self-Play via Formal Verification in Code Synthesis","url":"https://www.emergentmind.com/papers/2512.18160"}]

The search results reveal several important research directions on solver-verifier self-play frameworks for program repair and code generation. Here are the key findings:

## Self-Play Frameworks for Code Generation

Propose, Solve, Verify (PSV) is a self-play framework where formal verification signals are used to create a proposer capable of generating challenging synthetic problems and a solver trained via expert iteration. PSV uses formal verification to unlock a new paradigm for self-play in code generation, with a proposer generating problems in the form of formal specifications and a solver trying to generate programs that meet the specifications.

PSV-Verus improves pass@1 by up to 9.6x over inference-only and expert-iteration baselines across three benchmarks.

## Solver-Verifier Co-Development

Sol-Ver is a self-play solver-verifier framework that jointly improves a single model's code and test generation capacity by iteratively refining code (LLM-as-a-solver) and tests (LLM-as-a-verifier) together. Experiments with the Llama 3.1 8B model demonstrate substantial performance enhancements, achieving average relative improvements of 19.63% in code generation and 17.49% in test generation on MBPP and LiveCodeBench.

## Program Repair with Self-Play

Self-play SWE-RL (SSR) is a training paradigm for superintelligent software agents where a single LLM agent is trained via reinforcement learning in a self-play setting to iteratively inject and repair software bugs of increasing complexity.

## Verification-Based Approaches

VERSE (Verification-Based Self-Play) aims to enhance model proficiency in generating correct responses, where Code LLMs engage in self-play to generate instructions and corresponding verifications, evaluating execution results and self-consistency as verification outcomes.

The common theme across these approaches is using verification mechanisms (whether formal verification, unit tests, or execution results) to provide reliable feedback signals for iterative improvement in self-play settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c5b0bc6-db29-47fe-ac85-e4e5ad0f39c8",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "603fbc65-6895-4ae0-880e-52188da6c723",
  "sourceToolAssistantUUID": "3c5b0bc6-db29-47fe-ac85-e4e5ad0f39c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T20:55:31.368Z_

<details><summary>↩ Tool result · `toolu_018eYAUfT6dv8hN6nNCAbQo4`</summary>

```text
Web search results for query: "arxiv 2026 adversarial test generation automated program repair recent"

Links: [{"title":"Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair","url":"https://arxiv.org/html/2509.05372v2"},{"title":"[2509.05372] Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair","url":"https://arxiv.org/abs/2509.05372"},{"title":"Adversarial Reasoning for Repair Based on Inferred Program Intent","url":"https://arxiv.org/html/2505.13008v1"},{"title":"Adversarial Bug Reports as a Security Risk in Language ...","url":"https://arxiv.org/pdf/2509.05372"},{"title":"How Safe Are AI-Generated Patches? A Large-scale Study on Security Risks in LLM and Agentic Automated Program Repair on SWE-bench","url":"https://arxiv.org/html/2507.02976"},{"title":"[2505.13008] Adversarial Reasoning for Repair Based on Inferred Program Intent","url":"https://arxiv.org/abs/2505.13008"},{"title":"Runtime Execution Traces Guided Automated Program Repair","url":"https://arxiv.org/pdf/2604.02647"},{"title":"CodeHacker: Automated Test Case Generation for Detecting","url":"https://arxiv.org/pdf/2602.20213"},{"title":"[2303.12848] Test-time Detection and Repair of Adversarial Samples via Masked Autoencoder","url":"https://arxiv.org/abs/2303.12848"},{"title":"Adversarial Patch Generation for Automated Program Repair","url":"https://arxiv.org/pdf/2012.11060"}]

I found several relevant recent papers on arXiv combining adversarial approaches, test generation, and automated program repair. Here are the key findings:

## Major Recent Works (2026)

**1. Adversarial Bug Reports as a Security Risk in APR**

This work investigates security risks posed by adversarial bug reports -- realistic-looking issue submissions crafted to mislead APR systems into producing insecure or harmful code changes. The research provides an attack framework including prompts used for attacks as well as an open-source prototype that automates the generation and evaluation of adversarial bug reports.

Key findings include: 90% of crafted bug reports triggered attacker-aligned patches, with the best pre-repair filter blocking only 47%, while post-repair analysis was effective in just 58% of cases.

**2. Adversarial Reasoning for Repair (AdverIntent-Agent)**

AdverIntent-Agent uses LLMs to infer multiple possible developer intentions with respect to a buggy function, and uses test generation to help demonstrate and validate that the inferred intentions are likely adversarial. AdverIntent-Agent correctly repaired 77 and 105 bugs in the Defects4J 2.0 and HumanEval-Java benchmarks, respectively.

**3. Security Analysis of LLM-Generated Patches**

A large-scale security analysis of LLM-generated patches using 20,000+ GitHub issues presents the first comprehensive assessment of security risks in real-world program repair.

**4. CodeHacker - Automated Adversarial Test Case Generation**

CodeHacker is a program-centric adversarial framework for competitive programming that automates expert-level test case generation.

These papers collectively demonstrate recent advances in using adversarial techniques and automated test generation to both attack and improve automated program repair systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4312e263-e651-4162-95d9-90f66ed97062",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "a5da6d60-6bfc-4b43-aff2-6ba6299090d9",
  "sourceToolAssistantUUID": "4312e263-e651-4162-95d9-90f66ed97062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T20:55:31.824Z_

<details><summary>↩ Tool result · `toolu_01Jdh9irJX64AYx5LX5q7kgy`</summary>

```text
Web search results for query: "self-play patch verification test time arxiv"

Links: [{"title":"Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/html/2601.15808v1"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/html/2512.18160v1"},{"title":"[2512.18160] Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/abs/2512.18160"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/html/2501.19306v3"},{"title":"[2501.19306] SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/abs/2501.19306"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/html/2502.14948"},{"title":"Scalable Supervising Software Agents with Patch Reasoner","url":"https://arxiv.org/html/2510.22775"},{"title":"[2601.15808v1] Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/abs/2601.15808v1"},{"title":"Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2505.13445"}]

I found several relevant arxiv papers related to your search query on self-play, patch verification, and test-time scaling. Here are the key results:

## Main Papers Found:

1. **"Propose, Solve, Verify: Self-Play Through Formal Verification"** (December 2025)
   This paper studies self-play in the verified code generation setting, where formal verification provides reliable correctness signals, introducing Propose, Solve, Verify (PSV), a self-play framework where formal verification signals are used to create a proposer capable of generating challenging synthetic problems and a solver trained via expert iteration. PSV-Verus improves pass@1 by up to 9.6× over inference-only and expert-iteration baselines across three benchmarks.

2. **"Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification"** (January 2026)
   This work proposes an alternative paradigm where agents self-evolve by iteratively verifying the policy model's outputs guided by crafted rubrics, giving rise to inference-time scaling of verification, wherein an agent self-improves by evaluating its generated answers to produce iterative feedback and refinements.

3. **"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling"** (December 2025)
   This paper introduces Self-Enhanced Test-Time Scaling (SETS), which overcomes limitations by strategically combining parallel and sequential techniques and exploits the inherent self-verification and self-correction capabilities of LLMs, unifying sampling, verification, and correction within a single framework.

4. **"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation"** (March 2026)
   This paper trains an LLM to both generate coding solutions and unit tests in an iterative self-play framework, whereby synthetic preference pairs are constructed at each iteration depending on whether the code passes the generated tests or not, enabling the model to self-improve in both capabilities.

5. **"Scalable Supervising Software Agents with Patch Reasoner"** (October 2025)
   This work explores using reward models with absolute patch verification capability to provide scalable, deterministic supervision for software engineering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eec1204-1e95-47ba-9050-0b95a17b2925",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "9283f471-e825-4cdf-a584-79bc522617b7",
  "sourceToolAssistantUUID": "5eec1204-1e95-47ba-9050-0b95a17b2925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-11T20:55:34.532Z_

The OpenReview search was too restrictive. Let me run a few follow-up searches to fill gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9283f471-e825-4cdf-a584-79bc522617b7",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSxE1WWA3zBFN312qbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfea1400-3664-4ad9-840f-19ca52607478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192Ae2hnqCRWFbBevkiXDtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2227,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 10456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3483,
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

### Tool call

_source line 20 · 2026-05-11T20:55:35.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RCavQ6iFFp7PmyQv1wEypw`</summary>

```json
{
  "query": "openreview self-play code generation verification 2026 ICML ICLR",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfea1400-3664-4ad9-840f-19ca52607478",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSxE1WWA3zBFN312qbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe4425e-bba7-4774-ba09-6c17d4f7b5d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192Ae2hnqCRWFbBevkiXDtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2227,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 10456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3483,
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

### Tool call

_source line 21 · 2026-05-11T20:55:36.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BC8yi4DzGSTkuxiQiJfX5Z`</summary>

```json
{
  "query": "arxiv \"Sol-Ver\" solver verifier self-play code test generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fe4425e-bba7-4774-ba09-6c17d4f7b5d2",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSxE1WWA3zBFN312qbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc1f146b-729d-420a-aab6-db5bb3ff785d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192Ae2hnqCRWFbBevkiXDtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2227,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 10456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3483,
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

### Tool call

_source line 22 · 2026-05-11T20:55:37.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ArWpGQfBNQP2B4ACZ6ywcz`</summary>

```json
{
  "query": "Code-A1 adversarial evolving code LLM test LLM reinforcement learning 2603.15611"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc1f146b-729d-420a-aab6-db5bb3ff785d",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSxE1WWA3zBFN312qbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7a55173-bff7-4776-a939-d2829059d27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192Ae2hnqCRWFbBevkiXDtE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2227,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 10456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3483,
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

### Tool call

_source line 23 · 2026-05-11T20:55:38.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5eF7nFT3jTv4wKPK3UePB`</summary>

```json
{
  "query": "\"test-time\" \"patch verification\" OR \"program repair\" self-play OR adversarial no training inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a55173-bff7-4776-a939-d2829059d27e",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSxE1WWA3zBFN312qbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3644b26d-a2d0-4777-8d68-e6dcb029cc51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192Ae2hnqCRWFbBevkiXDtE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2227,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 10456,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2227,
          "output_tokens": 301,
          "cache_read_input_tokens": 10456,
          "cache_creation_input_tokens": 3483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3483,
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

_source line 24 · 2026-05-11T20:55:42.676Z_

<details><summary>↩ Tool result · `toolu_01RCavQ6iFFp7PmyQv1wEypw`</summary>

```text
Web search results for query: "openreview self-play code generation verification 2026 ICML ICLR"

Links: [{"title":"ReVeal: Self-Evolving Code Agents via Reliable Self-Verification | OpenReview","url":"https://openreview.net/forum?id=q56ZI1Co43"},{"title":"Published as a conference paper at ICLR 2026 ANCHORED SELF-PLAY FOR CODE REPAIR","url":"https://openreview.net/pdf/1d5dbf8c7eb7e1a4beef53e17e4a100bba12a40e.pdf"},{"title":"Published as a conference paper at ICLR 2026 SEARCH SELF-PLAY:","url":"https://openreview.net/pdf/cae7daa248c757f51dfe31ef9236f68e23ee6ba4.pdf"},{"title":"Verification Limits Code LLM Training | OpenReview","url":"https://openreview.net/forum?id=rkIwvPxArN"},{"title":"VERIFICATION LIMITS CODE LLM TRAINING","url":"https://openreview.net/pdf?id=rkIwvPxArN"},{"title":"ICLR 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=wpQ6rTpGY6"},{"title":"ICLR 2026 Workshop LLM Reasoning | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=142&venue=ICLR.cc/2026/Conference"},{"title":"ICML | OpenReview","url":"https://openreview.net/group?id=ICML.cc"}]

I found several relevant papers on OpenReview related to self-play, code generation, and verification for ICLR 2026. Here are the key findings:

## ICLR 2026 Papers Found:

1. **"Anchored Self-Play for Code Repair"** - This paper proposes generator-fixer self-play, which trains a single model with reinforcement learning to alternate between generating bugs and fixing them, using unit tests for verification when curated code-repair data is limited. Across bug sources in BUGSOURCEBENCH, ASP achieves the best fix rates, improving the average fix rate by +25% (relative) / +7.2 pp (absolute) over standard self-play.

2. **"ReVeal: Self-Evolving Code Agents via Reliable Self-Verification"** - This paper introduces ReVeal, a multi-turn Reinforcement learning framework that evolves code generation through self-Verification and tool-based evaluation, structuring long-horizon reasoning as iterative generation-verification turns.

3. **"Search Self-Play"** - This paper discusses self-play in a search context with verification mechanisms to prevent the proposer from generating incorrect questions.

4. **"Verification Limits Code LLM Training"** - This paper studies how verification limits code generation when both problem solutions and verification tests are generated by models, identifying a "verification ceiling" where the quality and diversity of training data are constrained by synthetic verifiers' capabilities.

These papers represent the intersection of self-play mechanisms, code generation, and verification methodologies being actively researched for ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fe4425e-bba7-4774-ba09-6c17d4f7b5d2",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "9734a9dc-c4c7-446d-afed-f658713cddd8",
  "sourceToolAssistantUUID": "5fe4425e-bba7-4774-ba09-6c17d4f7b5d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T20:55:43.230Z_

<details><summary>↩ Tool result · `toolu_01BC8yi4DzGSTkuxiQiJfX5Z`</summary>

```text
Web search results for query: "arxiv "Sol-Ver" solver verifier self-play code test generation 2025 2026"

Links: [{"title":"[2502.14948] Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/abs/2502.14948"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/html/2502.14948"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/html/2512.18160v1"},{"title":"[2502.14948v2] Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation","url":"https://arxiv.org/abs/2502.14948v2"},{"title":"[2512.18160] Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/abs/2512.18160"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2502.14948"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.18160v1"},{"title":"(PDF) Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://www.researchgate.net/publication/398978797_Propose_Solve_Verify_Self-Play_Through_Formal_Verification"},{"title":"Learning to Solve and Verify: A Self-Play Framework for Mutually Improving Code and Test Generation | OpenReview","url":"https://openreview.net/forum?id=j6tMZaPWWF"},{"title":"Self-Play via Formal Verification in Code Synthesis","url":"https://www.emergentmind.com/papers/2512.18160"}]

I found relevant research papers matching your search query. Here are the main findings:

## Sol-Ver Framework

Sol-Ver is a self-play solver-verifier framework that jointly improves a single model's code and test generation capacity. By iteratively refining code (LLM-as-a-solver) and tests (LLM-as-a-verifier) together, it boosts both capabilities without relying on human annotations or larger teacher models.

**Key Results:** Experiments with the Llama 3.1 8B model demonstrate substantial performance enhancements, achieving average relative improvements of 19.63% in code generation and 17.49% in test generation on MBPP and LiveCodeBench.

**Paper Details:** The arXiv paper (2502.14948) was posted on February 24, 2025, with updates through March 3, 2026.

## Related Work: Propose, Solve, Verify (PSV)

A related approach is the Propose, Solve, Verify framework. This framework studies self-play in the verified code generation setting, where formal verification provides reliable correctness signals, introducing a simple self-play framework where formal verification signals are used to create a proposer capable of generating challenging synthetic problems and a solver trained via expert iteration. PSV-Verus improves pass@1 by up to 9.6x over inference-only and expert-iteration baselines.

This paper (arXiv 2512.18160) was published on December 20, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc1f146b-729d-420a-aab6-db5bb3ff785d",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "d2ba9923-49ed-4a1f-958c-2090da76e7cd",
  "sourceToolAssistantUUID": "dc1f146b-729d-420a-aab6-db5bb3ff785d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T20:55:43.789Z_

<details><summary>↩ Tool result · `toolu_01ArWpGQfBNQP2B4ACZ6ywcz`</summary>

```text
Web search results for query: "Code-A1 adversarial evolving code LLM test LLM reinforcement learning 2603.15611"

Links: [{"title":"GitHub - ZJU-REAL/Code-A1: Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning · GitHub","url":"https://github.com/ZJU-REAL/Code-A1"},{"title":"[2603.15611] Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/abs/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/html/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM","url":"https://arxiv.org/pdf/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://zju-real.github.io/Code-A1/"},{"title":"Paper page - Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://huggingface.co/papers/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test ...","url":"https://swarmit.nextshiftconsulting.com/reviews/2026-03-17-code-a1-adversarial-evolving-of-code-llm-and-test-llm-via-re/"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=bHwu8XVNHcU"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning - YouTube","url":"https://www.youtube.com/watch?v=Efp8r6zEgXQ"},{"title":"EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning","url":"https://arxiv.org/html/2603.12698"}]

Based on the search results, here's what I found about Code-A1:

## Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning

Code-A1 is an adversarial co-evolution framework that jointly optimizes a Code LLM and a Test LLM with opposing objectives. The Code LLM is rewarded for passing more tests, while the Test LLM is rewarded for exposing more defects.

**Problem it Addresses:**

Reinforcement learning for code generation relies on verifiable rewards from unit test pass rates, yet high-quality test suites are scarce, existing datasets offer limited coverage, and static rewards fail to adapt as models improve. Recent self-play methods unify code and test generation in a single model, but face an inherent dilemma: white-box access leads to self-collusion where the model produces trivial tests for easy rewards, yet black-box restriction yields generic tests that miss implementation-specific bugs.

**Key Innovation:**

The architectural separation of the Code LLM and Test LLM addresses the inherent dilemma in prior self-play methods, enabling the Test LLM to craft targeted adversarial tests while avoiding self-collusion.

The paper (arXiv:2603.15611) was submitted on March 16, 2026, and the RL training stack is built on top of the verl framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7a55173-bff7-4776-a939-d2829059d27e",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "6f643a92-54c3-462e-9e94-bff3fca33677",
  "sourceToolAssistantUUID": "f7a55173-bff7-4776-a939-d2829059d27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-11T20:55:46.293Z_

<details><summary>↩ Tool result · `toolu_01N5eF7nFT3jTv4wKPK3UePB`</summary>

```text
Web search results for query: ""test-time" "patch verification" OR "program repair" self-play OR adversarial no training inference 2025 2026"

Links: [{"title":"Adversarial patch generation for automated program repair | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09709-4"},{"title":"[2303.12848] Test-time Detection and Repair of Adversarial Samples via Masked Autoencoder","url":"https://arxiv.org/abs/2303.12848"},{"title":"awesome-test-time-adaptation/TTA-OTTA.md at main · tim-learn/awesome-test-time-adaptation","url":"https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-OTTA.md"},{"title":"awesome-test-time-adaptation/TTA-TTBA.md at main · tim-learn/awesome-test-time-adaptation","url":"https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-TTBA.md"},{"title":"On the Adversarial Vulnerability of Label-Free Test-Time Adaptation | OpenReview","url":"https://openreview.net/forum?id=N0ETIi580T"},{"title":"On the Adversarial Risk of Test Time Adaptation: An Investigation into Realistic Test-Time Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=7893vsQenk"},{"title":"An empirical investigation into learning bug-fixing patches in the wild via neural machine translation | Request PDF","url":"https://www.researchgate.net/publication/327131570_An_empirical_investigation_into_learning_bug-fixing_patches_in_the_wild_via_neural_machine_translation"},{"title":"Uncovering Adversarial Risks of Test-Time Adaptation","url":"https://proceedings.mlr.press/v202/wu23h/wu23h.pdf"},{"title":"Self-Play via Formal Verification in Code Synthesis","url":"https://www.emergentmind.com/papers/2512.18160"},{"title":"(PDF) On the Adversarial Risk of Test Time Adaptation: An Investigation into Realistic Test-Time Data Poisoning","url":"https://www.researchgate.net/publication/384699521_On_the_Adversarial_Risk_of_Test_Time_Adaptation_An_Investigation_into_Realistic_Test-Time_Data_Poisoning"}]

Based on the search results, here are the key findings related to your query on test-time approaches, patch verification, program repair, self-play, and adversarial techniques in 2025-2026:

## Recent Research Highlights

### Program Repair and Adversarial Patches
NEVERMORE is a novel learning-based mechanism inspired by the adversarial nature of bugs and fixes, built upon the Generative Adversarial Networks architecture and trained on historical bug fixes to generate repairs that closely mimic human-produced fixes. Their empirical evaluation on 500 real-world bugs demonstrated effectiveness in bug-fixing, generating repairs that match human fixes for 21.2% of the examined bugs.

### Test-Time Adaptation and Adversarial Vulnerability
Test-time adaptation (TTA) updates the model weights during the inference stage using testing data to enhance generalization. However, recent work has shown that adding relatively small adversarial perturbations to a limited number of samples leads to significant performance degradation. Researchers have proposed attack algorithms that do not rely on access to labeled test samples, thus providing a concrete way to assess the security vulnerabilities of TTA algorithms.

### Test-Time Detection and Repair
DRAM is a novel defense method to detect and repair adversarial samples at test time via Masked autoencoder (MAE).

### Self-Play in Code Synthesis
Recent work on test-time training (TTT) involves running verification-based synthesis locally on repo-specific specs to adapt code models to project patterns without human labels.

These approaches represent an emerging trend of leveraging test-time inference and verification mechanisms for both robustness enhancement and program repair without requiring additional training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3644b26d-a2d0-4777-8d68-e6dcb029cc51",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "e88aca62-41c1-4d03-a0b2-eefbeca2ff04",
  "sourceToolAssistantUUID": "3644b26d-a2d0-4777-8d68-e6dcb029cc51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-11T20:55:49.355Z_

Let me get more details on a few critical papers I found, especially the ICLR 2026 "Anchored Self-Play for Code Repair" and "EvolveCoder."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e88aca62-41c1-4d03-a0b2-eefbeca2ff04",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSyHsCzqxGyQUEdBJcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33ea9061-5f98-4848-a38f-88b9b9d23bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhsy8pv7tYKhBqNA8a7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6366,
      "cache_read_input_tokens": 13939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6366,
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

### Tool call

_source line 29 · 2026-05-11T20:55:49.834Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Tprv7e4nrjHZonTJVX9QG`</summary>

```json
{
  "query": "\"Anchored Self-Play for Code Repair\" ICLR 2026 authors details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ea9061-5f98-4848-a38f-88b9b9d23bb0",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSyHsCzqxGyQUEdBJcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bca97f79-053c-4b00-9db5-2e6856081eab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhsy8pv7tYKhBqNA8a7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6366,
      "cache_read_input_tokens": 13939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6366,
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

### Tool call

_source line 30 · 2026-05-11T20:55:51.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHdKhAVCW6uKs2ge262rgo`</summary>

```json
{
  "query": "EvolveCoder adversarial verification code reinforcement learning arxiv 2603.12698"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca97f79-053c-4b00-9db5-2e6856081eab",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSyHsCzqxGyQUEdBJcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe1f3676-991a-4248-968b-9612caaa6895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhsy8pv7tYKhBqNA8a7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6366,
      "cache_read_input_tokens": 13939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6366,
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

### Tool call

_source line 31 · 2026-05-11T20:55:51.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JVmzha4ekq2J476VRFmnX3`</summary>

```json
{
  "query": "VERSE verification self-play code instructions AAAI 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe1f3676-991a-4248-968b-9612caaa6895",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSyHsCzqxGyQUEdBJcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8509610-ac27-48c9-ba9a-7ed91fe2759d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhsy8pv7tYKhBqNA8a7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6366,
      "cache_read_input_tokens": 13939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6366,
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

### Tool call

_source line 32 · 2026-05-11T20:55:51.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MVwhR49ex76atGsesCooJG`</summary>

```json
{
  "query": "ReVeal self-evolving code agents self-verification arxiv 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8509610-ac27-48c9-ba9a-7ed91fe2759d",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSyHsCzqxGyQUEdBJcf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fb47cc6-b4e6-48ff-bb9a-aba2c7c510e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhsy8pv7tYKhBqNA8a7QN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6366,
      "cache_read_input_tokens": 13939,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 13939,
          "cache_creation_input_tokens": 6366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6366,
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

_source line 33 · 2026-05-11T20:55:56.439Z_

<details><summary>↩ Tool result · `toolu_019Tprv7e4nrjHZonTJVX9QG`</summary>

```text
Web search results for query: ""Anchored Self-Play for Code Repair" ICLR 2026 authors details"

Links: [{"title":"Published as a conference paper at ICLR 2026 ANCHORED SELF-PLAY FOR CODE REPAIR","url":"https://openreview.net/pdf/1d5dbf8c7eb7e1a4beef53e17e4a100bba12a40e.pdf"},{"title":"From Self-Play to Self-Research: The ICLR 2026 RSI Workshop and the State of Self-Improving AI | Artifocial Blog","url":"https://www.artifocial.ai/blog/rsi-workshop-2026-mar-18"},{"title":"SPACeR: Self-Play Anchoring with Centralized Reference Models | OpenReview","url":"https://openreview.net/forum?id=Q5H3NCy18S"},{"title":"ICML Poster Toward Training Superintelligent Software Agents through Self-Play SWE-RL","url":"https://icml.cc/virtual/2026/poster/66747"},{"title":"SPACER: SELF-PLAY ANCHORING WITH CENTRAL- IZED REFERENCE MODELS","url":"https://www.arxiv.org/pdf/2510.18060"},{"title":"[2510.18060] SPACeR: Self-Play Anchoring with Centralized Reference Models","url":"https://arxiv.org/abs/2510.18060"},{"title":"Published as a conference paper at ICLR 2026 SEARCH SELF-PLAY:","url":"https://openreview.net/pdf/cae7daa248c757f51dfe31ef9236f68e23ee6ba4.pdf"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"Accepted Papers | ICLR 2026 Workshop RSI","url":"https://recursive-workshop.github.io/papers.html"}]

Based on the search results, I found information about "Anchored Self-Play for Code Repair" published at ICLR 2026:

## Paper Details

The paper "Anchored Self-Play for Code Repair" is by Choi et al. and was published as a conference paper at ICLR 2026.

## Key Information

The paper proposes generator–fixer self-play, which trains a single model with reinforcement learning to alternate between generating bugs and fixing them, and as the fixer improves, the generator adapts to produce more challenging bugs, yielding an automatic curriculum.

## Main Contribution

The paper addresses a critical realism gap where self-play generates increasingly hard bugs that may not resemble bugs that humans actually write. The authors show that unanchored self-play improves repair on synthetic bugs while degrading on human-authored ones. Their fix—anchoring self-play to a reference set from real bug distributions—improves average fix rates by +25 pp (relative) across all bug sources.

The authors also introduce BUGSOURCEBENCH, which holds the underlying prompt and unit tests fixed and varies only the buggy program source.

The paper was presented as a Spotlight paper (#22) at the ICLR 2026 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bca97f79-053c-4b00-9db5-2e6856081eab",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "796636bd-02a2-4822-9987-5d60a3f6cfdd",
  "sourceToolAssistantUUID": "bca97f79-053c-4b00-9db5-2e6856081eab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T20:55:57.134Z_

<details><summary>↩ Tool result · `toolu_01JVmzha4ekq2J476VRFmnX3`</summary>

```text
Web search results for query: "VERSE verification self-play code instructions AAAI 2025 2026"

Links: [{"title":"VERSE: Verification-based Self-Play for Code Instructions | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34604"},{"title":"VERSE: Verification-based Self-Play for Code Instructions","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34604/36759"},{"title":"VERSE: Verification-based Self-Play for Code Instructions | OpenReview","url":"https://openreview.net/forum?id=woKbSkgDsq"},{"title":"VERSE: Verification-based Self-Play for Code Instructions","url":"https://www.researchgate.net/publication/390700425_VERSE_Verification-based_Self-Play_for_Code_Instructions"},{"title":"(PDF) Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://www.researchgate.net/publication/398978797_Propose_Solve_Verify_Self-Play_Through_Formal_Verification"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/html/2512.18160v1"},{"title":"[2512.18160] Propose, Solve, Verify: Self-Play Through Formal Verification","url":"https://arxiv.org/abs/2512.18160"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"Self-Play via Formal Verification in Code Synthesis","url":"https://www.emergentmind.com/papers/2512.18160"},{"title":"Propose, Solve, Verify: Self-Play Through Formal Verification | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.18160v1"}]

Based on the search results, I found information about VERSE and related verification-based self-play approaches for code instructions:

## VERSE: Verification-based Self-Play for Code Instructions

VERSE establishes a robust verification framework that covers various code instructions, and Code LLMs engage in self-play to generate instructions and corresponding verifications. They evaluate execution results and self-consistency as verification outcomes, using them as scores. This work was published in the AAAI Conference on Artificial Intelligence in 2025.

## Related Work: Propose, Solve, Verify (PSV)

The search also revealed a complementary approach called Propose, Solve, Verify (PSV). PSV is a simple self-play framework where formal verification signals are used to create a proposer capable of generating challenging synthetic problems and a solver trained via expert iteration. PSV-Verus, across three benchmarks improves pass@1 by up to 9.6x over inference-only and expert-iteration baselines.

The key difference is that PSV uses formal verification (with tools like Verus in Rust) rather than just unit tests, which only cover a limited set of cases, so programs can pass them and still be incorrect.

If you need more specific details about code instructions or implementation details for either approach, I can search for additional information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8509610-ac27-48c9-ba9a-7ed91fe2759d",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "5a23334e-e849-4be5-8649-6c3cfd046bb0",
  "sourceToolAssistantUUID": "d8509610-ac27-48c9-ba9a-7ed91fe2759d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T20:55:57.592Z_

<details><summary>↩ Tool result · `toolu_01LHdKhAVCW6uKs2ge262rgo`</summary>

```text
Web search results for query: "EvolveCoder adversarial verification code reinforcement learning arxiv 2603.12698"

Links: [{"title":"[2603.12698] EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning","url":"https://arxiv.org/abs/2603.12698"},{"title":"EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning","url":"https://arxiv.org/html/2603.12698"},{"title":"EvolveCoder: Evolving Test Cases via Adversarial Verification for Code","url":"https://arxiv.org/pdf/2603.12698"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://arxiv.org/html/2506.11442v1"},{"title":"Paper page - Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://huggingface.co/papers/2603.15611"},{"title":"[2506.03136] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/html/2603.15611"},{"title":"[2603.15611] Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/abs/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM","url":"https://arxiv.org/pdf/2603.15611"},{"title":"[2603.11433] Adversarial Reinforcement Learning for Detecting False Data Injection Attacks in Vehicular Routing","url":"https://arxiv.org/abs/2603.11433"}]

Based on the search results, I found the paper you're looking for:

## EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning

Reinforcement learning with verifiable rewards (RLVR) is a promising approach for improving code generation in large language models, but its effectiveness is limited by weak and static verification signals in existing coding RL datasets.

The paper proposes a solution-conditioned and adversarial verification framework that iteratively refines test cases based on the execution behaviors of candidate solutions, with the goal of increasing difficulty, improving discriminative power, and reducing redundancy.

The researchers introduce EvolveCoder-22k, a large-scale coding reinforcement learning dataset constructed through multiple rounds of adversarial test case evolution.

Reinforcement learning on EvolveCoder-22k yields stable optimization and consistent performance gains, improving Qwen3-4B by an average of 4.2 points across four downstream benchmarks and outperforming strong 4B-scale baselines.

The paper was submitted to arXiv on March 13, 2026, with authors Chi Ruan, Dongfu Jiang, Huaye Zeng, Ping Nie, and Wenhu Chen from the University of Waterloo, Vector Institute, and Harvard University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe1f3676-991a-4248-968b-9612caaa6895",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "29dafa74-1c1e-4643-9ffb-500d18981489",
  "sourceToolAssistantUUID": "fe1f3676-991a-4248-968b-9612caaa6895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-11T20:55:58.522Z_

<details><summary>↩ Tool result · `toolu_01MVwhR49ex76atGsesCooJG`</summary>

```text
Web search results for query: "ReVeal self-evolving code agents self-verification arxiv 2506"

Links: [{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://arxiv.org/html/2506.11442v1"},{"title":"[2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification","url":"https://arxiv.org/abs/2506.11442"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://www.arxiv.org/pdf/2506.11442v1"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.11442v1"},{"title":"Paper page - ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://huggingface.co/papers/2506.11442"},{"title":"Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://www.alphaxiv.org/abs/2506.11442v1"},{"title":"ReVeal: Iterative Code Generation & Verification","url":"https://www.emergentmind.com/papers/2506.11442"},{"title":"ReVeal: Self-Evolving Code Agents via Reliable Self-Verification | OpenReview","url":"https://openreview.net/forum?id=q56ZI1Co43"},{"title":"GitHub - XMUDeepLIT/Awesome-Self-Evolving-Agents: A Survey of Self-Evolving Agents | A curated list of resources (surveys, papers, benchmarks, and opensource projects) on Self-Evolving Agents. · GitHub","url":"https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://www.researchgate.net/publication/392717329_ReVeal_Self-Evolving_Code_Agents_via_Iterative_Generation-Verification"}]

Based on the search results, I found comprehensive information about the ReVeal paper. Here's what the research presents:

## Overview

ReVeal is a multi-turn RL framework that enables code agents to engage in an iterative generation-verification loop.

## Key Mechanism

At each turn, the model generates a candidate program and self-verifies its correctness by constructing test cases and interacting with external tools (e.g., Python interpreters). This closed-loop process provides executable verification plans and fine-grained feedback, allowing the model to identify errors, revise strategies, and progressively refine its output.

## Self-Evolution Capability

ReVeal enables test-time scaling into deeper inference regimes through robust self-verification: although trained with up to three reasoning turns, the model progressively evolves its solutions across up to 19 inference turns and tackles previously intractable problems.

## Performance Results

When using DAPO-Qwen-32B as the base model, ReVeal exceeds the performance of DeepSeek-R1-Zero-Qwen-32B using only 11k TACO training data. Furthermore, ReVeal significantly improves Pass@k accuracy over both the base model and strong RL baselines, demonstrating its ability to expand the reasoning boundaries of the underlying model.

## Design Innovation

This gives rise to a self-evolving code LLM: without relying on distillation or supervised fine-tuning, the model continually improves via RL-zero training, driven by the co-evolution of its generation and verification capabilities.

The paper was published on arXiv as 2506.11442 in June 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb47cc6-b4e6-48ff-bb9a-aba2c7c510e4",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "21d6a351-a430-47e7-b880-adfb5008cdf5",
  "sourceToolAssistantUUID": "2fb47cc6-b4e6-48ff-bb9a-aba2c7c510e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-11T20:56:01.505Z_

Let me do one final search for any work specifically combining test-time (no training) self-play for program repair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21d6a351-a430-47e7-b880-adfb5008cdf5",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSzCAwEUBpcKHNw1nuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ed99059-97f3-44b4-84dc-c26d04f44782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9wxHL8FViBfUUtfuoQXLK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3790,
      "cache_read_input_tokens": 20305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3790,
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

_source line 38 · 2026-05-11T20:56:03.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Svir4YeegM5gwB4mNq5gyH`</summary>

```json
{
  "query": "\"inference time\" OR \"test time\" adversarial test generation bug fix patch without training 2025 2026 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ed99059-97f3-44b4-84dc-c26d04f44782",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSzCAwEUBpcKHNw1nuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e804c3e1-9381-4886-8400-a11084d7f708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9wxHL8FViBfUUtfuoQXLK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3790,
      "cache_read_input_tokens": 20305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3790,
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

_source line 39 · 2026-05-11T20:56:03.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WNkothQLGUkYm1YvxUGcG`</summary>

```json
{
  "query": "SWE-bench adversarial test generation patch filtering verification no finetuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e804c3e1-9381-4886-8400-a11084d7f708",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawSzCAwEUBpcKHNw1nuN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cb396f0-6015-4eb7-aefc-04bc2bb6c58c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9wxHL8FViBfUUtfuoQXLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3790,
      "cache_read_input_tokens": 20305,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 20305,
          "cache_creation_input_tokens": 3790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3790,
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

_source line 40 · 2026-05-11T20:56:11.305Z_

<details><summary>↩ Tool result · `toolu_017WNkothQLGUkYm1YvxUGcG`</summary>

```text
Web search results for query: "SWE-bench adversarial test generation patch filtering verification no finetuning 2025 2026"

Links: [{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark","url":"https://arxiv.org/html/2603.00520v1"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified Issues Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-issues"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench/SWE-bench_Verified · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified"},{"title":"SWE-BENCH+: ENHANCED CODING BENCHMARK","url":"https://openreview.net/pdf/7b25f35e8d13c2c33d84177f371a0c76252ba1f4.pdf"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"}]

Based on the search results, I found relevant information about adversarial test generation and patch filtering for SWE-bench:

## SWE-ABS: Adversarial Benchmark Strengthening

SWE-ABS is an adversarial framework that actively attacks test suites to expose latent weaknesses, and then fortifies them. The two-stage approach combines complementary signals: Stage I uses Coverage-Driven Augmentation that leverages program slicing to identify patch-affected code regions and generates tests to exercise them, with a test decoupling mechanism adopted to prevent generated tests from overfitting to the specific implementation details of the gold patch.

Stage II involves Mutation-Driven Adversarial Strengthening that targets subtle semantic blind spots by synthesizing "mutant" patches that are plausible (i.e., they pass all existing tests) yet semantically incorrect, and by identifying mutants that evade existing tests, generates targeted adversarial tests to reject them, effectively mirroring red-team/blue-team dynamics used in security testing.

## Results and Impact

On SWE-Bench Verified, SWE-ABS strengthens 50.2% of instances (25.1× improvement over UTBoost), and induces an average decline of 14.56 percentage points in resolve rates across systems, resulting in 30 rank changes within the top-30 leaderboard. Prior work, such as UTBoost (Yu et al., 2025), attempts test augmentation by generating additional unit tests via LLMs, but strengthens only 10 out of 500 (2%) instances on SWE-Bench Verified.

## SWE-Bench+ Framework

Additionally, SWE-Bench+ targets identifying issues that include solutions in the issue description or comments and enhancing the test suites for filtering out suspicious patches, introducing an LLM-based solution leak detection tool to filter out issues with solution leaks and enhance the test suite of issues to avoid the weak test problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb396f0-6015-4eb7-aefc-04bc2bb6c58c",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "5ea7e8d5-1c14-4be9-9425-78ba78f22477",
  "sourceToolAssistantUUID": "6cb396f0-6015-4eb7-aefc-04bc2bb6c58c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-11T20:56:11.489Z_

<details><summary>↩ Tool result · `toolu_01Svir4YeegM5gwB4mNq5gyH`</summary>

```text
Web search results for query: ""inference time" OR "test time" adversarial test generation bug fix patch without training 2025 2026 LLM"

Links: [{"title":"Paper page - Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://huggingface.co/papers/2603.15611"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/html/2603.15611v1"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Adversarial Attacks on LLMs | Lil'Log","url":"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/"},{"title":"A First Look at Bugs in LLM Inference Engines","url":"https://arxiv.org/html/2506.09713"},{"title":"LLMs in Software Testing: Reshaping QA with GenAI & Self-Healing","url":"https://cloudqa.io/how-llms-are-reshaping-qa-in-2025/"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"LLM Inference 2026: How It Works & How to Optimize for Speed | Future AGI Blog","url":"https://futureagi.com/blog/llm-inference-human-prompts-2025"},{"title":"LLM Testing Tools and Frameworks in 2026: The Engineering Guide","url":"https://contextqa.com/blog/llm-testing-tools-frameworks-2026/"},{"title":"AegisLLM: Scaling LLM Security Through Adaptive Multi-Agent Systems at Inference Time - MarkTechPost","url":"https://www.marktechpost.com/2025/07/18/aegisllm-scaling-llm-security-through-adaptive-multi-agent-systems-at-inference-time/"}]

Based on the search results, here are the most relevant findings for your query about inference/test-time adversarial test generation and bug fixes for LLMs in 2025-2026:

## Key Research and Developments

**Code Generation and Adversarial Testing:**

Recent work focuses on generating difficult test cases, such as "hacking inputs" designed to induce timeouts, by prompting models to write "test generator programs" and using oracle programs to validate the outputs. At inference time, automatically synthesized tests enable self-verification in agentic workflows.

Direct generation methods often produce invalid or hallucinated tests, which is a key challenge in this space. Code-A1 decouples the two tasks into models with opposing objectives, safely enabling white-box test generation and stable co-evolution via the Mistake Book.

**Inference-Time Security:**

AegisLLM is a framework to improve LLM security through a cooperative, inference-time multi-agent system. Through automated prompt optimization and Bayesian learning, the system refines its defense capabilities without model retraining, allowing real-time adaptation to evolving attack strategies while providing scalable, inference-time security.

**Automated Adversarial Test Case Generation:**

Giskard is an Apache 2.0 licensed testing framework specifically built for automated LLM vulnerability detection. Unlike other frameworks which require manual test case authoring, Giskard automatically generates adversarial test cases for hallucinations, contradictions, prompt injections, data disclosures, and inappropriate content.

**LLM Inference Engine Bugs:**

A comprehensive dataset of 929 real-world bugs was constructed from official repositories of 5 widely adopted LLM inference engines, analyzing these bugs to uncover their symptoms, root causes, commonality, fix effort, fix strategies, and temporal evolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e804c3e1-9381-4886-8400-a11084d7f708",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "16dfb057-81d5-4bc1-b893-1b35d67569eb",
  "sourceToolAssistantUUID": "e804c3e1-9381-4886-8400-a11084d7f708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-11T20:56:14.831Z_

This is a critical find -- SWE-ABS is very close to the proposed idea. Let me get more details on it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16dfb057-81d5-4bc1-b893-1b35d67569eb",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawT19awTzrbAqwCoV5qC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bceb1b6-ff3e-40a5-accf-9f4b62e5233b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FizMyg13SpTjDZ95dqGrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1179,
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

### Tool call

_source line 43 · 2026-05-11T20:56:15.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHkS8jft9rTr4rREm1VgAb`</summary>

```json
{
  "query": "SWE-ABS adversarial benchmark strengthening arxiv 2603.00520 authors date details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bceb1b6-ff3e-40a5-accf-9f4b62e5233b",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawT19awTzrbAqwCoV5qC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb88fafe-027a-4380-9b0d-e3b920c7ec19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FizMyg13SpTjDZ95dqGrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1179,
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

### Tool call

_source line 44 · 2026-05-11T20:56:16.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRQHx3Fh359GvDQVzyLYBL`</summary>

```json
{
  "query": "\"Co-Evolving LLM Coder and Unit Tester\" arxiv 2506.03136 2025 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb88fafe-027a-4380-9b0d-e3b920c7ec19",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawT19awTzrbAqwCoV5qC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d5ec3af-ef32-495e-a2fa-32c75707185f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FizMyg13SpTjDZ95dqGrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 960,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1179,
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

### Tool result

_source line 45 · 2026-05-11T20:56:23.588Z_

<details><summary>↩ Tool result · `toolu_01UHkS8jft9rTr4rREm1VgAb`</summary>

```text
Web search results for query: "SWE-ABS adversarial benchmark strengthening arxiv 2603.00520 authors date details"

Links: [{"title":"[2603.00520] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark","url":"https://arxiv.org/abs/2603.00520"},{"title":"SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark","url":"https://arxiv.org/html/2603.00520"},{"title":"[2512.10218] Does SWE-Bench-Verified Test Agent Ability or Model Memory?","url":"https://arxiv.org/abs/2512.10218"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"[2509.16941] SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://arxiv.org/abs/2509.16941"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"[2603.03233v1] AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework","url":"https://arxiv.org/abs/2603.03233v1"},{"title":"AutoAdvExBench: Benchmarking autonomous exploitation ...","url":"https://arxiv.org/pdf/2503.01811"},{"title":"AutoAdvExBench: Benchmarking autonomous exploitation of adversarial example defenses","url":"https://arxiv.org/html/2503.01811v1"},{"title":"[2603.00285] TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?","url":"https://arxiv.org/abs/2603.00285"}]

Based on the search results, here are the details for the SWE-ABS paper (arxiv 2603.00520):

## Paper Details

**Title:** SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark

**ArXiv ID:** 2603.00520

**Submission Date:** February 28, 2026

## Authors

Boxi Yu, Yang Cao, Yuzhong Zhang, Liting Lin, Junjielong Xu, Zhiqing Zhong, Qinghua Xu, Guancheng Wang, Jialun Cao, Shing-Chi Cheung, Pinjia He, Lionel Briand

## Key Findings

The performance on the SWE-Bench Verified leaderboard is inflated, with one in five "solved" patches from the top-30 agents being semantically incorrect, passing only because weak test suites fail to expose their errors.

## Methodology

SWE-ABS is an adversarial framework that strengthens test suites through a two-stage pipeline: (1) coverage-driven augmentation using program slicing to target untested code regions, and (2) mutation-driven adversarial testing that synthesizes plausible but incorrect patches to expose semantic blind spots.

## Results

On SWE-Bench Verified (500 instances), SWE-ABS strengthens 50.2% of instances, a 25.1x improvement over prior work, and rejects 19.71% of previously passing patches. As a result, the top agent's score decreases from 78.80% to 62.20%, causing significant leaderboard reshuffling, with the previous top-ranked agent dropping to fifth place.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb88fafe-027a-4380-9b0d-e3b920c7ec19",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "e4a9f420-0c2b-473a-8fd6-51fb4a7ec225",
  "sourceToolAssistantUUID": "bb88fafe-027a-4380-9b0d-e3b920c7ec19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-11T20:56:23.850Z_

<details><summary>↩ Tool result · `toolu_01YRQHx3Fh359GvDQVzyLYBL`</summary>

```text
Web search results for query: ""Co-Evolving LLM Coder and Unit Tester" arxiv 2506.03136 2025 details"

Links: [{"title":"[2506.03136] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136"},{"title":"[2506.03136v1] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136v1"},{"title":"GitHub - Gen-Verse/CURE: [NeurIPS 2025 Spotlight] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning · GitHub","url":"https://github.com/Gen-Verse/CURE"},{"title":"Paper page - Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://huggingface.co/papers/2506.03136"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/html/2506.03136"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=wPdBe9zxNr"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning |…","url":"https://www.opentrain.ai/papers/co-evolving-llm-coder-and-unit-tester-via-reinforcement-learning--arxiv-2506.03136/"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250603136W/abstract"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/392372360_Co-Evolving_LLM_Coder_and_Unit_Tester_via_Reinforcement_Learning"},{"title":"Technical Report Guided Self-Evolving LLMs with Minimal Human Supervision","url":"https://arxiv.org/pdf/2512.02472"}]

Based on the search results, here are the details about the paper "Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning" (arXiv 2506.03136):

## Overview
The paper proposes CURE, a novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes, without any ground-truth code as supervision.

## Key Features
This approach enables flexible and scalable training and allows the unit tester to learn directly from the coder's mistakes.

## Authors and Publication
The paper was submitted on June 3, 2025, with authors including Yinjie Wang, Ling Yang, Ye Tian, Ke Shen, and Mengdi Wang. A version 2 was released on September 25, 2025.

## Results
The derived ReasonFlux-Coder-7B and 14B models improve code generation accuracy by 5.3% and Best-of-N accuracy by 9.0% after optimization on Qwen2.5-Instruct models, outperforming similarly sized Qwen-Coder, DeepSeek-Coder, and Seed-Coder. They naturally extend to downstream tasks such as test-time scaling and agentic coding—achieving an 8.1% improvement over the base model.

## Recognition
The paper was selected as a NeurIPS 2025 Spotlight presentation.

The code is available on GitHub at [https://github.com/Gen-Verse/CURE](https://github.com/Gen-Verse/CURE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d5ec3af-ef32-495e-a2fa-32c75707185f",
  "isSidechain": true,
  "promptId": "7417be52-17de-4614-9345-1ff076bf6567",
  "agentId": "af8b74f330792cf27",
  "type": "user",
  "uuid": "9875ba49-015a-4e0c-8f44-98ae5df26401",
  "sourceToolAssistantUUID": "4d5ec3af-ef32-495e-a2fa-32c75707185f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-11T20:57:28.415Z_

Here is my consolidated report of findings.

---

## Landscape Report: Adversarial Self-Play for Patch Verification / Program Repair (2025-2026)

This is an active and crowded research area. I found **12 closely related papers** from the last ~18 months. I classify them by proximity to your proposed idea (test-time self-play between patch generation and adversarial test generation, no additional training).

---

### HIGHEST RELEVANCE -- FLAG THESE

**1. SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark**
- Authors: Boxi Yu, Yang Cao, Yuzhong Zhang, et al.
- Venue: arXiv [2603.00520](https://arxiv.org/abs/2603.00520), Feb 28 2026
- Summary: Two-stage adversarial framework that (1) uses coverage-driven augmentation to generate tests targeting patch-affected code, and (2) synthesizes plausible-but-incorrect "mutant" patches to generate targeted adversarial tests that reject them -- explicitly a red-team/blue-team dynamic applied to patch verification.
- **Similarity assessment: HIGH.** This is adversarial test generation for patch verification at evaluation time (no model training). The key difference from your proposal is that SWE-ABS strengthens the benchmark test suite post-hoc rather than using iterative self-play loops between a patch generator and test generator at inference time. But the core insight (adversarial tests to reject plausible-but-wrong patches) is essentially the same.

**2. Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning**
- Authors: ZJU-REAL group (Zhejiang University)
- Venue: arXiv [2603.15611](https://arxiv.org/abs/2603.15611), March 16 2026
- Summary: Adversarial co-evolution of two separate models -- a Code LLM (rewarded for passing tests) and a Test LLM (rewarded for exposing defects) -- via RL with opposing objectives. Eliminates self-collusion by architectural separation, enabling white-box adversarial test generation.
- **Similarity assessment: HIGH.** This is the closest to "adversarial self-play between code generation and test generation." The critical difference from your proposal: Code-A1 involves RL training of both models, whereas your idea is test-time only (no additional training).

**3. AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent**
- Authors: (ISSTA 2025 paper), also at arXiv [2505.13008](https://arxiv.org/abs/2505.13008)
- Venue: ISSTA 2025 / ACM TOSEM 2026
- Summary: Multi-agent framework with a reasoning agent that generates adversarial program intents + faulty statements, a test agent that produces adversarial test cases aligned with inferred intents, and a repair agent that generates patches. No training -- purely inference-time multi-agent orchestration.
- **Similarity assessment: VERY HIGH.** This is adversarial test generation for program repair at inference time with no training. The main difference is it frames adversarial intent around program understanding rather than explicit self-play iteration, and it doesn't iterate (generate patch -> adversarial test -> re-generate patch -> ...).

---

### HIGH RELEVANCE -- Training-based self-play (solver/verifier for code)

**4. Anchored Self-Play for Code Repair (ASP)**
- Authors: Choi et al.
- Venue: **ICLR 2026 (Spotlight)**
- OpenReview: [PDF](https://openreview.net/pdf/1d5dbf8c7eb7e1a4beef53e17e4a100bba12a40e.pdf)
- Summary: Generator-fixer self-play where a single model alternates between generating bugs and fixing them via RL, anchored to real bug distributions to prevent distribution drift. Improves average fix rate by +25% relative over standard self-play.
- **Similarity: MODERATE-HIGH.** Self-play for code repair, but it's a training method (RL), not test-time. Also generates bugs rather than adversarial tests.

**5. Sol-Ver (Learning to Solve and Verify): A Self-Play Framework for Code and Test Generation**
- Authors: (multiple affiliations)
- Venue: arXiv [2502.14948](https://arxiv.org/abs/2502.14948), Feb 2025; also on [OpenReview](https://openreview.net/forum?id=j6tMZaPWWF)
- Summary: Self-play solver-verifier framework that jointly improves a single model's code and test generation via iterative refinement. 19.63% improvement in code generation, 17.49% in test generation on MBPP/LiveCodeBench.
- **Similarity: MODERATE.** Self-play between code and test generation, but it's a training framework, not test-time.

**6. CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning**
- Authors: Yinjie Wang, Ling Yang, Ye Tian, et al.
- Venue: **NeurIPS 2025 (Spotlight)**, arXiv [2506.03136](https://arxiv.org/abs/2506.03136)
- Summary: RL framework co-evolving coding and unit test generation based on their interaction outcomes, without ground-truth code supervision. Unit tester learns from coder's mistakes.
- **Similarity: MODERATE.** Co-evolution of coder and tester, but training-based.

**7. EvolveCoder: Evolving Test Cases via Adversarial Verification for Code RL**
- Authors: Chi Ruan, Dongfu Jiang, et al. (Waterloo, Vector Institute, Harvard)
- Venue: arXiv [2603.12698](https://arxiv.org/abs/2603.12698), March 13 2026
- Summary: Solution-conditioned adversarial verification framework that iteratively refines test cases based on execution behaviors of candidate solutions to increase difficulty and discriminative power.
- **Similarity: MODERATE.** Adversarial test evolution conditioned on solutions, but for RL training data construction, not test-time.

---

### MODERATE RELEVANCE -- Self-play for code (different focus)

**8. Propose, Solve, Verify (PSV): Self-Play Through Formal Verification**
- Venue: arXiv [2512.18160](https://arxiv.org/abs/2512.18160), Dec 2025
- Summary: Self-play where formal verification signals train a proposer (generates hard problems) and solver (expert iteration). 9.6x pass@1 improvement. Focused on code synthesis, not repair.

**9. Self-Play SWE-RL (SSR)**
- Venue: arXiv [2512.18552](https://arxiv.org/abs/2512.18552), Dec 2025; **ICML 2026**
- Summary: Single LLM agent trained via RL in a self-play setting to inject and repair software bugs of increasing complexity. Training paradigm for SWE agents.

**10. VERSE: Verification-based Self-Play for Code Instructions**
- Venue: **AAAI 2025**, [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/34604)
- Summary: Code LLMs engage in self-play to generate instructions and corresponding verifications, evaluating execution results and self-consistency as verification outcomes.

**11. ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification**
- Venue: arXiv [2506.11442](https://arxiv.org/abs/2506.11442), June 2025; also on [OpenReview](https://openreview.net/forum?id=q56ZI1Co43)
- Summary: Multi-turn RL framework for iterative generation-verification loops. Trained with 3 turns but self-evolves to 19 inference turns. Training-based but demonstrates test-time scaling.

**12. NEVERMORE: Adversarial Patch Generation for Automated Program Repair**
- Venue: Software Quality Journal, [Springer](https://link.springer.com/article/10.1007/s11219-025-09709-4), 2025
- Summary: GAN-based approach trained on historical bug fixes to generate repairs mimicking human patches. 21.2% match rate on 500 real bugs. "Adversarial" here refers to GANs, not adversarial testing.

---

### Key Gap Analysis (your proposed idea vs. existing work)

Your specific proposal -- **self-play between patch generation and adversarial test generation at test time (no additional training) to iteratively improve repair quality** -- occupies a specific niche that is **partially but not fully covered**:

| Aspect | Existing coverage |
|---|---|
| Adversarial test generation for patch verification | **Covered** (SWE-ABS, AdverIntent-Agent) |
| Self-play between code gen and test gen | **Covered** (Code-A1, Sol-Ver, CURE, EvolveCoder) |
| Self-play for code repair specifically | **Covered** (ASP at ICLR 2026, SWE-RL at ICML 2026) |
| Test-time / inference-only (no training) | **Partially covered** (AdverIntent-Agent, SWE-ABS) |
| **Iterative self-play loop at test time** (generate patch -> adversarial test -> reject/re-generate -> repeat) | **NOT explicitly covered** |

The key differentiator that remains open: **iterative, multi-round self-play at inference time** where a patch generator and adversarial test generator repeatedly challenge each other without any parameter updates. AdverIntent-Agent is close but is a single-pass pipeline (not iterative). SWE-ABS is adversarial test generation for patch filtering but doesn't loop back to re-generate patches. The training-based methods (Code-A1, CURE, ASP) achieve the iterative dynamics but via RL training.

**Bottom line:** The ingredients are all published separately, and the space is extremely active. No paper I found combines all three elements (iterative + self-play + test-time-only + for program repair) in a single system. However, AdverIntent-Agent (ISSTA 2025) and SWE-ABS (Feb 2026) are close enough that reviewers will expect detailed comparison and clear articulation of what the iterative test-time loop adds beyond single-pass adversarial filtering.

---

Sources:
- [Code-A1 (arXiv 2603.15611)](https://arxiv.org/abs/2603.15611)
- [SWE-ABS (arXiv 2603.00520)](https://arxiv.org/abs/2603.00520)
- [AdverIntent-Agent (arXiv 2505.13008)](https://arxiv.org/abs/2505.13008)
- [Anchored Self-Play for Code Repair (ICLR 2026)](https://openreview.net/pdf/1d5dbf8c7eb7e1a4beef53e17e4a100bba12a40e.pdf)
- [Sol-Ver (arXiv 2502.14948)](https://arxiv.org/abs/2502.14948)
- [CURE (arXiv 2506.03136)](https://arxiv.org/abs/2506.03136)
- [EvolveCoder (arXiv 2603.12698)](https://arxiv.org/abs/2603.12698)
- [PSV (arXiv 2512.18160)](https://arxiv.org/abs/2512.18160)
- [Self-Play SWE-RL (arXiv 2512.18552)](https://arxiv.org/abs/2512.18552)
- [VERSE (AAAI 2025)](https://ojs.aaai.org/index.php/AAAI/article/view/34604)
- [ReVeal (arXiv 2506.11442)](https://arxiv.org/abs/2506.11442)
- [NEVERMORE (Springer)](https://link.springer.com/article/10.1007/s11219-025-09709-4)
- [Adversarial Bug Reports (arXiv 2509.05372)](https://arxiv.org/abs/2509.05372)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9875ba49-015a-4e0c-8f44-98ae5df26401",
  "isSidechain": true,
  "agentId": "af8b74f330792cf27",
  "requestId": "req_011CawT24Xc7Jt81vrCWMZy3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b3e69a4-263d-4d4c-851e-4c8d9eeff3c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "27cace6c-f66c-4d0f-9738-1b0888f23945",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNs69PSVmyEjtLz8nKodmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3118,
      "cache_read_input_tokens": 25274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3118,
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
