# Research conversation: I'm assessing the feasibility of a research project that uses environment observations (DOM diffs, inventory changes, te

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8dcaa37ccc3468ff.jsonl`
- **Structured JSON:** [`cf37c5136ae1f42ebf8c.json`](../../sessions/cf/cf37c5136ae1f42ebf8c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

83 recorded events

### User

_source line 1 · 2026-05-11T22:34:09.115Z_

I'm assessing the feasibility of a research project that uses environment observations (DOM diffs, inventory changes, test outputs) as potential-based reward shaping (PBRS) signals for training LLM agents via RL. I need to check:

## 1. Existing Implementations on GitHub
Search for:
- "github.com PBRS reward shaping LLM agent"
- "github.com potential based reward shaping agent training"
- "github.com TIPS reward shaping agentic" 
- "github.com AgentPRM process reward"
- "github.com WebArena reward shaping RL training"
- "github.com agentic RL training code"
- "github.com observation reward agent reinforcement learning"

Report what open-source code exists that could serve as building blocks.

## 2. Dataset Availability
Search for:
- "huggingface.co/datasets WebArena"
- "huggingface.co/datasets ALFWorld"
- "huggingface.co/datasets SWE-bench"
- "paperswithcode.com web agent benchmarks"
- "WebArena environment setup requirements"
- "ALFWorld environment setup"
- "SWE-bench docker setup cost"

Report which datasets/environments are freely available and what compute they require.

## 3. Training Cost References
Search for:
- "agentic RL training cost GPU hours A100"
- "WebArena training compute requirements"
- "GRPO training LLM agent GPU cost"
- "reinforcement learning LLM agent training cost 2025 2026"
- "TIPS PBRS training cost compute"

Report any concrete numbers about GPU hours and costs for similar experiments.

Be thorough and report all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "46b12943-5db5-4b56-96ca-a2c8d0b8f63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T22:34:09.119Z_

```json
{
  "parentUuid": "46b12943-5db5-4b56-96ca-a2c8d0b8f63a",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
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
  "uuid": "e89423e5-dd01-426b-983b-1ca38fe2a902",
  "timestamp": "2026-05-11T22:34:09.119Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T22:34:12.386Z_



I'll conduct a thorough web search across all three areas. Let me start by loading the WebSearch tool and then run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e89423e5-dd01-426b-983b-1ca38fe2a902",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUQzhiJaL1bbs8sUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbd57a0a-c8f5-4f77-93b2-7ba08b5d87a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D74mmfDrrjxyShBG3CQsmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 935,
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

_source line 4 · 2026-05-11T22:34:12.905Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K3MWAFyHYKM8dXWxUjoZoQ`</summary>

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
  "parentUuid": "dbd57a0a-c8f5-4f77-93b2-7ba08b5d87a6",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUQzhiJaL1bbs8sUWk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c81a0f7-41d7-4035-8bf2-cf91467a5e5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D74mmfDrrjxyShBG3CQsmj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 7304,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 935,
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

_source line 5 · 2026-05-11T22:34:12.908Z_

<details><summary>↩ Tool result · `toolu_01K3MWAFyHYKM8dXWxUjoZoQ`</summary>

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
  "parentUuid": "6c81a0f7-41d7-4035-8bf2-cf91467a5e5e",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "014e470d-0aec-4e27-820b-6648e0652cb7",
  "sourceToolAssistantUUID": "6c81a0f7-41d7-4035-8bf2-cf91467a5e5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T22:34:16.006Z_



Now let me run all the searches in parallel across the three areas.

**Area 1: Existing Implementations on GitHub**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "014e470d-0aec-4e27-820b-6648e0652cb7",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e10d7be1-70ca-4de0-8a87-edd9bc895af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-11T22:34:16.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ejr1y25EBqQzTLjZyUzS7`</summary>

```json
{
  "query": "PBRS reward shaping LLM agent GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e10d7be1-70ca-4de0-8a87-edd9bc895af6",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "604c9a2f-445f-43e2-8a02-398cd64eacdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-11T22:34:17.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dAk8pC4UPMMcSXY5pGX7s`</summary>

```json
{
  "query": "potential based reward shaping agent training GitHub repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "604c9a2f-445f-43e2-8a02-398cd64eacdc",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df7478f4-d34a-4669-9253-f65eb7014a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-11T22:34:17.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E6doCXgQUhdgefPWs1BmLt`</summary>

```json
{
  "query": "TIPS reward shaping agentic GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df7478f4-d34a-4669-9253-f65eb7014a4d",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42d44dcf-bf59-4f7b-85f7-96b58cfcec7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 10 · 2026-05-11T22:34:18.390Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018kqc4VTVubizxrFQC7bS4c`</summary>

```json
{
  "query": "AgentPRM process reward model GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d44dcf-bf59-4f7b-85f7-96b58cfcec7c",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df61647b-49b6-4e44-a099-c7c3c1d9e7e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 11 · 2026-05-11T22:34:18.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CsA3riwkRJhm1kXQcejoBy`</summary>

```json
{
  "query": "WebArena reward shaping RL training GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df61647b-49b6-4e44-a099-c7c3c1d9e7e7",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "902b29db-7f0b-4842-8a5f-31218119ef7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 12 · 2026-05-11T22:34:19.325Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ewzi2DeSnYwhvgcUf4nrX6`</summary>

```json
{
  "query": "agentic RL training code GitHub 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "902b29db-7f0b-4842-8a5f-31218119ef7b",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6587715c-3920-4816-8b52-5f49857510a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 13 · 2026-05-11T22:34:19.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FmTELQQMRxbvGdkxC9UxEg`</summary>

```json
{
  "query": "observation reward agent reinforcement learning GitHub code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6587715c-3920-4816-8b52-5f49857510a5",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaUhAo8ypbpHB8jjoGX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e52b735-41d3-4633-acc6-4cbd9d5faacc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDaCBtfX1QZP24RrnVNL7k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8239,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 8239,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 14 · 2026-05-11T22:34:24.037Z_

<details><summary>↩ Tool result · `toolu_018kqc4VTVubizxrFQC7bS4c`</summary>

```text
Web search results for query: "AgentPRM process reward model GitHub"

Links: [{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/abs/2502.10325"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Agent+Process+Reward+Models"},{"title":"Awesome-Process-Reward-Models/README.md at main · RyanLiu112/Awesome-Process-Reward-Models","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models/blob/main/README.md"},{"title":"GitHub - sanjibanc/agent_prm","url":"https://github.com/sanjibanc/agent_prm"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Request PDF","url":"https://www.researchgate.net/publication/403735553_AgentPRM_Process_Reward_Models_for_LLM_Agents_via_Step-Wise_Promise_and_Progress"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"}]

Based on the search results, here's what I found about AgentPRM:

## Overview

AgentPRM (Agent Process Reward Models) is a simple and scalable framework for training LLM agents to continually improve through interactions. AgentPRM follows a lightweight actor-critic paradigm, using Monte Carlo rollouts to compute reward targets and optimize policies.

## Key Features

It requires minimal modifications to existing RLHF pipelines, making it easy to integrate at scale. Beyond AgentPRM, the framework also proposes InversePRM, which learns process rewards directly from demonstrations without explicit outcome supervision.

## GitHub Repository

The code is available at: https://github.com/sanjibanc/agent_prm.

## Performance

The framework was evaluated on the ALFWorld benchmark, showing that small 3B models trained with AgentPRM and InversePRM outperform strong GPT-4o baselines.

## Research Paper

AgentPRM is documented in a paper titled "Process Reward Models for LLM Agents: Practical Framework and Directions" published on arXiv in February 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df61647b-49b6-4e44-a099-c7c3c1d9e7e7",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "f09900fb-22b9-44bf-bb5f-12d2eedb6249",
  "sourceToolAssistantUUID": "df61647b-49b6-4e44-a099-c7c3c1d9e7e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T22:34:24.039Z_

<details><summary>↩ Tool result · `toolu_019ejr1y25EBqQzTLjZyUzS7`</summary>

```text
Web search results for query: "PBRS reward shaping LLM agent GitHub"

Links: [{"title":"Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents","url":"https://arxiv.org/pdf/2604.11088"},{"title":"A Simple Framework for Intrinsic Reward-Shaping for RL using LLM Feedback","url":"https://alexzhang13.github.io/assets/pdfs/Reward_Shaping_LLM.pdf"},{"title":"Using Incomplete and Incorrect Plans to Shape Reinforcement","url":"https://alaworkshop2023.github.io/papers/ALA2023_paper_28.pdf"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"Potential-Based Reward Shaping (PBRS)","url":"https://www.emergentmind.com/topics/potential-based-reward-shaping-pbrs"},{"title":"[1902.06239] A new Potential-Based Reward Shaping for Reinforcement Learning Agent","url":"https://arxiv.org/abs/1902.06239"},{"title":"LLM-Enhanced Reinforcement Learning for Time Series Anomaly Detection","url":"https://arxiv.org/html/2601.02511"},{"title":"Automatic Reward Shaping from Confounded Offline Data","url":"https://causalai.net/r123.pdf"},{"title":"GitHub - AADILab/leader-follower: Repository for extending \"Learning Based Leadership in Swarm Navigation\" paper to multiagent setting. · GitHub","url":"https://github.com/AADILab/leader-follower"},{"title":"LLM-Guided Reward Shaping","url":"https://www.emergentmind.com/topics/llm-guided-reward-shaping"}]

Based on the search results, I found several relevant resources on PBRS (Potential-Based Reward Shaping) applied to LLM agents:

## Key Findings

**Academic Papers:**

1. The paper "Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents" analyzes results through the lens of potential-based reward shaping (PBRS) from reinforcement learning, extending the PBRS framework analogically to LLM instruction following.

2. Agent Process Reward Models (AgentPRM) introduce a simple and scalable framework for training LLM agents to continually improve through interactions, following a lightweight actor-critic paradigm using Monte Carlo rollouts.

3. One framework combines an LSTM-based RL agent with VAE-enhanced reward mechanisms, LLM-based potential functions for semantic reward shaping, and active learning with label propagation.

**General PBRS Framework:**

Potential-based reward shaping (PBRS) is a particular category of machine learning methods which aims to improve the learning speed of a reinforcement learning agent by extracting and utilizing extra knowledge while performing a task.

**GitHub Resources:**

A GitHub repository holds code for D-Indirect and Agent Specific PBRS for influence-based reward shaping (available at AADILab/leader-follower).

The search results indicate active research in combining PBRS techniques with LLM agents for both instruction following and reinforcement learning applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "604c9a2f-445f-43e2-8a02-398cd64eacdc",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "c09210d3-14b9-4d30-9d41-eff23e81f631",
  "sourceToolAssistantUUID": "604c9a2f-445f-43e2-8a02-398cd64eacdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T22:34:24.167Z_

<details><summary>↩ Tool result · `toolu_011dAk8pC4UPMMcSXY5pGX7s`</summary>

```text
Web search results for query: "potential based reward shaping agent training GitHub repository"

Links: [{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"A Simple Framework for Intrinsic Reward-Shaping for RL using LLM Feedback","url":"https://alexzhang13.github.io/assets/pdfs/Reward_Shaping_LLM.pdf"},{"title":"GitHub - brianwade1/Gym_QLearning_and_RewardShaping: This repo demonstrates basic Q-learning for the Mountain Car Gym environment. It also shows how reward shaping can result in faster training of the agent. · GitHub","url":"https://github.com/brianwade1/Gym_QLearning_and_RewardShaping"},{"title":"reward-shaping · GitHub Topics · GitHub","url":"https://github.com/topics/reward-shaping"},{"title":"Reward Shaping for Reinforcement Learning with An ... - GitHub","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24l/ma24l.pdf"},{"title":"Potential-Based Reward Shaping in Reinforcement Learning | by Sophie Zhao | Medium","url":"https://medium.com/@sophiezhao_2990/potential-based-reward-shaping-in-reinforcement-learning-05da05cfb84a"},{"title":"Exploration-Guided Reward Shaping for Reinforcement ...","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/266c0f191b04cbbbe529016d0edc847e-Supplemental-Conference.pdf"},{"title":"Improving the Effectiveness of Potential-Based Reward Shaping in Reinforcement Learning","url":"https://arxiv.org/html/2502.01307v1"},{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"GitHub - facebookresearch/controllable_agent: The Controllable Agent project trains RL Agents able to optimize any reward function specified in real time, without any further learning or fine-tuning. Training is reward-free and based on the Forward-Backward representation. · GitHub","url":"https://github.com/facebookresearch/controllable_agent"}]

Based on the search results, I found several relevant resources related to potential-based reward shaping and agent training on GitHub:

## Key Findings:

**Educational Resources:**
- Potential-based reward shaping is a particular type of reward shaping with nice theoretical guarantees, where a potential function assigns a heuristic value of goodness to each state.

**GitHub Repositories:**

1. **Gym Q-Learning and Reward Shaping** - This repository demonstrates basic Q-learning for the Mountain Car Gym environment and shows how reward shaping can result in faster training of the agent. Repository: `brianwade1/Gym_QLearning_and_RewardShaping`

2. **Exploration-Guided Reward Shaping** - A GitHub repository at machine-teaching-group/neurips2022_exploration-guided-reward-shaping that implements exploration-guided reward shaping for RL agents.

3. **Reward Shaping Topic** - GitHub Topics page for reward-shaping contains multiple repositories including implementations of deep reinforcement learning with PyTorch using algorithms like A2C and PPO.

4. **Controllable Agent Framework** - The facebookresearch/controllable_agent project, which provides RL agents able to optimize any reward function specified in real time, with training that is reward-free and based on the Forward-Backward representation.

**Additional Research:**
Recent work on improving potential-based reward shaping effectiveness has been published on arXiv, focusing on optimizing the approach for better training convergence and policy learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df7478f4-d34a-4669-9253-f65eb7014a4d",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "9880ebeb-cbc7-47b5-ad71-e3b5c7d6f7c4",
  "sourceToolAssistantUUID": "df7478f4-d34a-4669-9253-f65eb7014a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T22:34:26.220Z_

<details><summary>↩ Tool result · `toolu_01E6doCXgQUhdgefPWs1BmLt`</summary>

```text
Web search results for query: "TIPS reward shaping agentic GitHub"

Links: [{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=eBMOr6a84z"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/html/2509.25779v1"},{"title":"GitHub - TencentYoutuResearch/SPEAR: An RL Recipe for Building Agentic LLMs via Self-Imitation on Long-Horizon Agentic Tasks · GitHub","url":"https://github.com/TencentYoutuResearch/SPEAR"},{"title":"GitHub - ucsd-wang-lab-lm/tips: TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs · GitHub","url":"https://github.com/ucsd-wang-lab-lm/tips"},{"title":"GitHub - ventr1c/Awesome-RL-based-Agentic-Search-Papers: The official repository of \"A Comprehensive Survey on Reinforcement Learning-based Agentic Search: Foundations, Roles, Optimizations, Evaluations, and Applications\". · GitHub","url":"https://github.com/ventr1c/Awesome-RL-based-Agentic-Search-Papers"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/html/2603.22293v1"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs | OpenReview","url":"https://openreview.net/forum?id=CmOaD42eAT"},{"title":"PLANNER-R1: REWARD SHAPING ENABLES EFFI- CIENT AGENTIC RL WITH SMALLER LLMS","url":"https://arxiv.org/pdf/2509.25779"}]

Based on the search results, here's what I found:

## TIPS: Turn-level Information-Potential Reward Shaping

TIPS (Turn-Level Information Potential Reward Shaping) is a framework that assigns dense, turn-level rewards to each reasoning + tool-call segment based on the increased likelihood of the correct answer under a teacher model. Evaluated on seven QA benchmarks, TIPS consistently outperforms GRPO/PPO baselines and substantially improves training stability.

### Key Technical Details

TIPS converts an outcome-only signal into dense, turn-level feedback that directly targets the core ambiguity in tool-use credit assignment: which information-acquisition steps actually moved the agent closer to a correct answer. The information credit takes the form of a potential difference over segment states, yielding a potential-based reward shaping (PBRS) construction that preserves the set of optimal policies while improving learning signals, offering a clean interpretation of TIPS as a policy-invariant way to reduce variance and stabilize long-horizon optimization.

### Performance Results

With a Qwen-2.5 7B Instruct model, TIPS improves the average Exact Match score by 11.8% and F1 by 13.6% relative to PPO.

### GitHub Repository

The TIPS repository is a verl-based project for Search-R1 style RL training with tool use (multi-turn retrieval, PPO/GRPO training, and validation workflows). The code base for TIPS is available at https://github.com/ucsd-wang-lab-lm/tips.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42d44dcf-bf59-4f7b-85f7-96b58cfcec7c",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "d8f1f2ea-c6e9-4944-bfd6-a3f947042a51",
  "sourceToolAssistantUUID": "42d44dcf-bf59-4f7b-85f7-96b58cfcec7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T22:34:26.838Z_

<details><summary>↩ Tool result · `toolu_01CsA3riwkRJhm1kXQcejoBy`</summary>

```text
Web search results for query: "WebArena reward shaping RL training GitHub"

Links: [{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"GitHub - WooooDyy/AgentGym-RL: Code and implementations for the paper \"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/AgentGym-RL"},{"title":"GitHub - THUDM/WebRL: Building Open LLM Web Agents with Self-Evolving Online Curriculum RL · GitHub","url":"https://github.com/THUDM/WebRL"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/html/2411.02337v1"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"GitHub - alexzhang13/reward-shaping-rl","url":"https://github.com/alexzhang13/reward-shaping-rl"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"GitHub - flowersteam/EAGER","url":"https://github.com/flowersteam/EAGER"},{"title":"webarena · GitHub Topics · GitHub","url":"https://github.com/topics/webarena"}]

Based on the search results, here are the key findings related to WebArena reward shaping RL training on GitHub:

## WebRL - Self-Evolving Online Curriculum RL

WebRL is a novel self-evolving online curriculum RL framework for training LLM-based web agents that implements the infrastructure for RL in the WebArena environment, together with a strong ORM (Outcome-Supervised Reward Model). WebRL is a self-evolving online curriculum learning framework designed for training web agents, targeting the WebArena environment, and the code is available at https://github.com/THUDM/WebRL.

WebRL incorporates 1) a self-evolving curriculum that generates new tasks from unsuccessful attempts, 2) a robust outcome-supervised reward model (ORM), and 3) adaptive reinforcement learning strategies to ensure consistent improvements. The framework has demonstrated significant performance gains: On WebArena-Lite, WebRL improves the success rate of Llama-3.1-8B from 4.8% to 42.4%, and from 6.1% to 43% for GLM-4-9B.

## WebAgent-R1

Another relevant project is WebAgent-R1, which learns directly from online interactions with web environments by asynchronously generating diverse trajectories, entirely guided by binary rewards depending on task success. It extends group relative policy optimization (GRPO) to multi-turn settings (M-GRPO) and employs an asynchronous trajectory rollout strategy.

## Related Resources

There's also mention of applying on-policy M-GRPO using sparse binary signals in WebArena-Lite, indicating broader adoption of these reward shaping techniques in web agent training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "902b29db-7f0b-4842-8a5f-31218119ef7b",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "102d84c8-761d-427f-a066-7730bf8c3ca3",
  "sourceToolAssistantUUID": "902b29db-7f0b-4842-8a5f-31218119ef7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T22:34:27.702Z_

<details><summary>↩ Tool result · `toolu_01FmTELQQMRxbvGdkxC9UxEg`</summary>

```text
Web search results for query: "observation reward agent reinforcement learning GitHub code"

Links: [{"title":"GitHub - KhoomeiK/LlamaGym: Fine-tune LLM agents with online reinforcement learning · GitHub","url":"https://github.com/KhoomeiK/LlamaGym"},{"title":"GitHub - FLAIROx/JaxMARL: Multi-Agent Reinforcement Learning with JAX · GitHub","url":"https://github.com/FLAIROx/JaxMARL"},{"title":"GitHub - eleurent/rl-agents: Implementations of Reinforcement Learning and Planning algorithms · GitHub","url":"https://github.com/eleurent/rl-agents"},{"title":"GitHub - tsmatz/reinforcement-learning-tutorials: Reinforcement Learning Algorithms Tutorial (Python) from scratch (Mar 2021) · GitHub","url":"https://github.com/tsmatz/reinforcement-learning-tutorials"},{"title":"GitHub - AgentR1/Agent-R1: Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning · GitHub","url":"https://github.com/0russwest0/Agent-R1"},{"title":"GitHub - RodrigoToroIcarte/reward_machines · GitHub","url":"https://github.com/RodrigoToroIcarte/reward_machines"},{"title":"GitHub - Devnetly/Hierarchical-Multi-agent-Reinforcement-Learning: This project features a hierarchical cooperative multi-agent environment where agents must work together to solve a two-part puzzle. · GitHub","url":"https://github.com/Devnetly/Hierarchical-Multi-agent-Reinforcement-Learning"},{"title":"GitHub - facebookresearch/Pearl: A Production-ready Reinforcement Learning AI Agent Library brought by the Applied Reinforcement Learning team at Meta. · GitHub","url":"https://github.com/facebookresearch/Pearl"},{"title":"GitHub - tongjingqi/Awesome-Agent-RL: A curated list of awesome resources about reward construction for AI agents. This repository covers cutting-edge research, and practical guides on defining and collecting rewards to build more intelligent and aligned AI agents. · GitHub","url":"https://github.com/tongjingqi/Awesome-Agent-RL"},{"title":"GitHub - Anshuman265/Deep-Reinforcement-Learning-Trading-Agent · GitHub","url":"https://github.com/Anshuman265/Deep-Reinforcement-Learning-Trading-Agent"}]

I found several relevant GitHub repositories related to observation, reward, agent, and reinforcement learning. Here are some key projects:

## Key Projects Found

1. **LlamaGym** - Fine-tune LLM agents with online reinforcement learning, where the agent receives observations and acts based on them while receiving rewards from the environment. The project shows a pattern where the agent receives an observation and info from environment reset, then acts based on the observation and receives observation, reward, terminated, truncated, and info from environment steps.

2. **JaxMARL** - Multi-agent reinforcement learning framework where actions, observations, rewards and done values are passed as dictionaries keyed by agent name, allowing for differing action and observation spaces.

3. **RL-Agents** - A repository for reinforcement learning algorithms with configuration-based experiments that log episode rewards, lengths, and seeds to stats files.

4. **Agent-R1** - An open-source framework for training powerful language agents with end-to-end reinforcement learning designed for multi-step agent tasks, where each interaction step is treated as a proper RL transition with an environment-defined state, an LLM action, and the next observation produced by the environment.

5. **Pearl** - A production-ready reinforcement learning library with modular design that offers features for production environments including dynamic action spaces, offline learning, and history summarization.

6. **Reward Machines** - A project proposing reward machines as finite state machines that support specification of reward functions while exposing reward function structure, with methodologies including automated reward shaping, task decomposition, and counterfactual reasoning.

These repositories provide various implementations of agent-reward-observation patterns in reinforcement learning with different approaches and specializations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e52b735-41d3-4633-acc6-4cbd9d5faacc",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "7e26c17a-f94d-439b-89c6-5f010d319da5",
  "sourceToolAssistantUUID": "9e52b735-41d3-4633-acc6-4cbd9d5faacc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T22:34:28.398Z_

<details><summary>↩ Tool result · `toolu_01Ewzi2DeSnYwhvgcUf4nrX6`</summary>

```text
Web search results for query: "agentic RL training code GitHub 2025 2026"

Links: [{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"GitHub - Gen-Verse/OpenClaw-RL: OpenClaw-RL: Train any agent simply by talking · GitHub","url":"https://github.com/Gen-Verse/OpenClaw-RL"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"GitHub - PrimeIntellect-ai/prime-rl: Agentic RL Training at Scale · GitHub","url":"https://github.com/PrimeIntellect-ai/prime-rl"},{"title":"GitHub - JiazhengZhang/AgentV-RL · GitHub","url":"https://github.com/JiazhengZhang/AgentV-RL"},{"title":"GitHub - WooooDyy/AgentGym-RL: Code and implementations for the paper \"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/AgentGym-RL"},{"title":"GitHub - RLinf/RLinf: RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI · GitHub","url":"https://github.com/RLinf/RLinf"},{"title":"hello-agents/docs/chapter11/Chapter11-Agentic-RL.md at main · datawhalechina/hello-agents","url":"https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/Chapter11-Agentic-RL.md"}]

Based on the search results, here are several key agentic RL training code repositories on GitHub from 2025-2026:

## Major Agentic RL Frameworks

**1. Agentic-RL-Training-Recipes**
A 2026 survey titled "Training Recipes for Agentic Reinforcement Learning in LLMs" that provides training recipes and implementations for various agentic RL approaches.

**2. Open-AgentRL**
An ICML 2026 project called "RLAnything & DemyAgent" for general and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings. It includes high-quality SFT and RL datasets, demonstrating that simple recipes enable even 4B models to outperform 32B models on challenging benchmarks.

**3. OpenClaw-RL**
A 2026 fully asynchronous RL framework for training personalized AI agents from natural conversation feedback with three learning paradigms (Binary RL / OPD / Combine).

**4. PRIME-RL**
Fully asynchronous RL for high-throughput agentic training at scale, built to train 1T+ MoE models on 1000+ GPUs with FSDP2 for training and vLLM for inference.

**5. RAGEN (Reasoning Agents with Reinforcement Learning)**
RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. RAGEN-2 was released in 2026.3.12.

**6. AgentGym-RL**
A framework to train LLM agents for multi-turn interactive decision-making through RL that encompasses a wide variety of real-world scenarios and supports mainstream RL algorithms.

**7. RLinf**
A flexible and scalable open-source RL infrastructure designed for Embodied and Agentic AI, where 'inf' stands for Infrastructure.

These repositories represent the state-of-the-art in agentic RL training code available in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6587715c-3920-4816-8b52-5f49857510a5",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "ddc1f09f-61bb-4c1d-9f57-a87e89c9ec40",
  "sourceToolAssistantUUID": "6587715c-3920-4816-8b52-5f49857510a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-11T22:34:49.071Z_

Now let me search for Area 2 (Datasets) and Area 3 (Training Costs) in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddc1f09f-61bb-4c1d-9f57-a87e89c9ec40",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f043787-586e-4d9c-9a58-b7831def9cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 22 · 2026-05-11T22:34:50.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016DS2PxF5Qpkzm775WhLAvh`</summary>

```json
{
  "query": "huggingface datasets WebArena web agent benchmark",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f043787-586e-4d9c-9a58-b7831def9cb2",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22115a19-30b1-4459-8c57-ff62ca6568a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 23 · 2026-05-11T22:34:51.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6N7cgtztm3GDcS4YVwfKc`</summary>

```json
{
  "query": "huggingface datasets ALFWorld embodied agent",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22115a19-30b1-4459-8c57-ff62ca6568a6",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd7fda78-060a-4070-871f-7346b4e8c508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 24 · 2026-05-11T22:34:51.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017F58Hs5DvQzAcRYWjEqRYq`</summary>

```json
{
  "query": "huggingface datasets SWE-bench software engineering",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd7fda78-060a-4070-871f-7346b4e8c508",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91855e7d-d566-4aa6-bb99-458ca8bd20ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 25 · 2026-05-11T22:34:52.563Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CGqAQim8SyAkgkA4rHZQdc`</summary>

```json
{
  "query": "web agent benchmarks WebArena ALFWorld datasets 2025 2026",
  "allowed_domains": [
    "paperswithcode.com"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91855e7d-d566-4aa6-bb99-458ca8bd20ce",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53a0e1bd-d9e2-4fa8-9222-20ebdca62fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 26 · 2026-05-11T22:34:52.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011bUQZuUB6kPxCR7zm6w5Wx`</summary>

```json
{
  "query": "WebArena environment setup requirements compute GPU docker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53a0e1bd-d9e2-4fa8-9222-20ebdca62fd5",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bab0de9-a3b1-4015-841a-b1394072f898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 27 · 2026-05-11T22:34:53.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SbSo72BhBR1SNYzyHR8rSB`</summary>

```json
{
  "query": "ALFWorld environment setup installation requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bab0de9-a3b1-4015-841a-b1394072f898",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38fe8684-aec7-44cc-9b1a-07700b418696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 28 · 2026-05-11T22:34:53.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ksw9uBengzCxrfJFPRbAuf`</summary>

```json
{
  "query": "SWE-bench docker setup cost compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38fe8684-aec7-44cc-9b1a-07700b418696",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaVqNSWz9MDd31JG2bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc0c04ca-57a4-470d-a6e2-8fcc64e2d9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUw8REn8bFgCR3Vbw8h9uG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 10158,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1020,
          "output_tokens": 463,
          "cache_read_input_tokens": 10158,
          "cache_creation_input_tokens": 6213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6213,
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

_source line 29 · 2026-05-11T22:34:56.767Z_

<details><summary>↩ Tool result · `toolu_01H6N7cgtztm3GDcS4YVwfKc`</summary>

```text
Web search results for query: "huggingface datasets ALFWorld embodied agent"

Links: [{"title":"hkust-nlp/agentboard · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hkust-nlp/agentboard"},{"title":"awawa-agi/alfworld-raw · Datasets at Hugging Face","url":"https://huggingface.co/datasets/awawa-agi/alfworld-raw"},{"title":"awawa-agi/alfworld-prompts · Datasets at Hugging Face","url":"https://huggingface.co/datasets/awawa-agi/alfworld-prompts"},{"title":"data/alfworld-00000-of-00001-302ad687bb3817a4.parquet · zai-org/AgentInstruct at main","url":"https://huggingface.co/datasets/zai-org/AgentInstruct/blob/main/data/alfworld-00000-of-00001-302ad687bb3817a4.parquet"},{"title":"README.md · hkust-nlp/agentboard at 0680548ef773505788d3cced65640a0fd511242f","url":"https://huggingface.co/datasets/hkust-nlp/agentboard/blob/0680548ef773505788d3cced65640a0fd511242f/README.md"},{"title":"neulab/agent-data-collection · Datasets at Hugging Face","url":"https://huggingface.co/datasets/neulab/agent-data-collection/viewer/agenttuning_alfworld/train"},{"title":"u-10bei/sft_alfworld_trajectory_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset"},{"title":"zjunlp/WKM-mistral-alfworld · Hugging Face","url":"https://huggingface.co/zjunlp/WKM-mistral-alfworld"},{"title":"Paper page - Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld","url":"https://huggingface.co/papers/2311.16714"},{"title":"data/alfworld-00000-of-00001-302ad687bb3817a4.parquet · THUDM/AgentInstruct at main","url":"https://huggingface.co/datasets/THUDM/AgentInstruct/blob/main/data/alfworld-00000-of-00001-302ad687bb3817a4.parquet"}]

Based on the search results, here's what I found about ALFWorld and related datasets on Hugging Face:

## Key Findings:

**ALFWorld Overview:**
ALFWorld contains abstract game files (TextWorld + PDDL) used to align high-level language planning with embodied ALFRED tasks.

**Available Hugging Face Datasets:**

1. **AgentBoard** - AgentBoard is composed of 9 diverse tasks including Embodied AI, Game, Web, and Tool, and includes an ALFWorld subset with 134 rows of test data.

2. **alfworld-raw** - This dataset includes unique game instance identifiers, high-level task types, original file paths, and full TextWorld + PDDL specifications, with splits for train, eval_in_distribution, and eval_out_of_distribution.

3. **SFT ALFWorld Trajectory Dataset** - This is a synthetic SFT dataset designed for agent training in ALFWorld-compatible environments that programmatically generates expert trajectories without requiring an actual ALFWorld environment.

4. **AgentInstruct** - Contains ALFWorld data for training agents.

These datasets are designed to support embodied AI agent research and training on sequential decision-making tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd7fda78-060a-4070-871f-7346b4e8c508",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "e36a949d-4032-44db-99a0-930f031aead4",
  "sourceToolAssistantUUID": "fd7fda78-060a-4070-871f-7346b4e8c508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-11T22:34:57.289Z_

<details><summary>↩ Tool result · `toolu_016DS2PxF5Qpkzm775WhLAvh`</summary>

```text
Web search results for query: "huggingface datasets WebArena web agent benchmark"

Links: [{"title":"Paper page - WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://huggingface.co/papers/2307.13854"},{"title":"AmineHA/WebArena-Verified · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AmineHA/WebArena-Verified"},{"title":"ST-WebAgentBench/st-webagentbench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench"},{"title":"dolev31/st-webagentbench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/dolev31/st-webagentbench"},{"title":"yamhm/WebDS · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yamhm/WebDS"},{"title":"https://huggingface.co/datasets/McGill-NLP/agent-r...","url":"https://huggingface.co/datasets/McGill-NLP/agent-reward-bench/commit/c4431826a2f999bf26b9c8cc697daa3ac0a84789.diff?file=judgments/webarena/GenericAgent-meta-llama_Llama-3.3-70B-Instruct/gpt-4o-mini/webarena.265.json"},{"title":"judgments/webarena/GenericAgent-anthropic_claude-3.7-sonnet/aer/webarena.295.json · McGill-NLP/agent-reward-bench at 1c445e26fbc537ffe3bdc81563f1494c6c21ebff","url":"https://huggingface.co/datasets/McGill-NLP/agent-reward-bench/blob/1c445e26fbc537ffe3bdc81563f1494c6c21ebff/judgments/webarena/GenericAgent-anthropic_claude-3.7-sonnet/aer/webarena.295.json"},{"title":"Paper page - WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks","url":"https://huggingface.co/papers/2506.01952"},{"title":"Paper page - SafeArena: Evaluating the Safety of Autonomous Web Agents","url":"https://huggingface.co/papers/2503.04957"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Web-Agent"}]

Based on the search results, here's what I found about WebArena and related web agent benchmarks on Hugging Face:

## WebArena Benchmark

WebArena is a realistic and reproducible environment that evaluates the performance of autonomous agents performing complex tasks on websites using benchmark tasks that require human-like reasoning. The environment includes fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management.

The tasks in the benchmark are diverse, long-horizon, and are designed to emulate tasks that humans routinely perform on the internet. Results demonstrate that solving complex tasks is challenging, with the best GPT-4-based agent only achieving an end-to-end task success rate of 10.59%.

## Related Datasets on Hugging Face

Several related web agent benchmark datasets are available on Hugging Face:

1. **WebArena-Verified**: A curated benchmark dataset of web tasks designed for reproducible evaluation of web agents across multiple realistic websites.

2. **WebChoreArena**: A new benchmark comprising 532 tasks that extends the scope of WebArena to more complex and tedious web browsing tasks, measuring advancements in LLM capabilities.

3. **SafeArena**: The first benchmark to focus on the deliberate misuse of web agents, comprising 250 safe and 250 harmful tasks across four websites.

4. **WebDS**: The first end-to-end benchmark designed for evaluating agents on real-world web-based data science workflows, containing 870 tasks across 29 containerized websites spanning 10 domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22115a19-30b1-4459-8c57-ff62ca6568a6",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "c04c76a1-ad80-4d7b-af60-4e572d04ddb8",
  "sourceToolAssistantUUID": "22115a19-30b1-4459-8c57-ff62ca6568a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T22:34:57.579Z_

<details><summary>↩ Tool result · `toolu_017F58Hs5DvQzAcRYWjEqRYq`</summary>

```text
Web search results for query: "huggingface datasets SWE-bench software engineering"

Links: [{"title":"SWE-bench/SWE-bench_Verified · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified"},{"title":"ScaleAI/SWE-bench_Pro · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"},{"title":"princeton-nlp/SWE-bench_Verified · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified"},{"title":"princeton-nlp/SWE-bench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench"},{"title":"SWE-bench-Live/SWE-bench-Live · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live"},{"title":"TuringEnterprises/SWE-Bench-plus-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/TuringEnterprises/SWE-Bench-plus-plus"},{"title":"SWE-bench/SWE-smith · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench/SWE-smith"},{"title":"SWE-bench (SWE-bench)","url":"https://huggingface.co/SWE-bench"},{"title":"princeton-nlp/SWE-bench_Lite · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite"},{"title":"princeton-nlp/SWE-bench_bm25_27K · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench_bm25_27K"}]

I found comprehensive information about SWE-bench datasets available on Hugging Face. Here's what I found:

## Overview

SWE-bench is a benchmark for evaluating Language Models and AI Systems on their ability resolve real world GitHub Issues. The benchmark proposes a specific task: issue resolution provided a full repository and GitHub issue.

## Dataset Variants

Several versions of SWE-bench are available on Hugging Face:

1. **SWE-bench (Main)**: The dataset collects 2,294 Issue-Pull Request pairs from 12 popular Python repositories.

2. **SWE-bench_Verified**: The dataset collects 500 test Issue-Pull Request pairs from popular Python repositories. Evaluation is performed by unit test verification using post-PR behavior as the reference solution.

3. **SWE-bench_Lite**: The dataset collects 300 test Issue-Pull Request pairs from 11 popular Python repositories. Evaluation is performed by unit test verification using post-PR behavior as the reference solution.

4. **SWE-smith**: The SWE-smith Dataset is a training dataset of 50137 task instances from 128 GitHub repositories, collected using the SWE-smith toolkit. It is the largest dataset to date for training software engineering agents.

5. **SWE-bench-Live**: A brand-new, continuously updated SWE-bench-like dataset powered by an automated curation pipeline.

6. **SWE-bench_Pro**: SWE-Bench Pro is a challenging, enterprise-level dataset for testing agent ability on long-horizon software engineering tasks.

All datasets are available through Hugging Face's datasets library for training and evaluating AI systems on software engineering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91855e7d-d566-4aa6-bb99-458ca8bd20ce",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "72042710-cb3e-417f-85ee-71b4a9edf45a",
  "sourceToolAssistantUUID": "91855e7d-d566-4aa6-bb99-458ca8bd20ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-11T22:34:59.070Z_

<details><summary>↩ Tool result · `toolu_01CGqAQim8SyAkgkA4rHZQdc`</summary>

```text
Web search results for query: "web agent benchmarks WebArena ALFWorld datasets 2025 2026"

Links: [{"title":"ALFWorld Dataset","url":"https://paperswithcode.com/dataset/alfworld"},{"title":"Paper page - WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://paperswithcode.com/paper/webarena-a-realistic-web-environment-for"},{"title":"Papers with Code - Machine Learning Datasets","url":"https://paperswithcode.com/datasets?mod=environment&v=lst"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/dataset/aflw"},{"title":"Papers with Code - Arena-Web -- A Web-based Development and Benchmarking Platform for Autonomous Navigation Approaches","url":"https://paperswithcode.com/paper/arena-web-a-web-based-development-and"},{"title":"Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation | Papers With Code","url":"https://paperswithcode.com/paper/web-agents-with-world-models-learning-and"},{"title":"Web-Bench Dataset","url":"https://paperswithcode.com/dataset/web-bench"},{"title":"Web-Bench: A LLM Code Benchmark Based on ...","url":"https://paperswithcode.com/paper/web-bench-a-llm-code-benchmark-based-on-web"},{"title":"Yifei Zhou | Papers With Code","url":"https://paperswithcode.com/search?q=author:Yifei+Zhou"},{"title":"Papers with Code - Paper tables with annotated results for Large Language Models Can Self-Improve At Web Agent Tasks","url":"https://paperswithcode.com/paper/large-language-models-can-self-improve-at-web/review/"}]

Based on the search results, here's what I found about web agent benchmarks and datasets:

## WebArena Benchmark

WebArena is a realistic and reproducible environment that evaluates the performance of autonomous agents performing complex tasks on websites using benchmark tasks that require human-like reasoning. The environment includes fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management. The results demonstrate that solving complex tasks is challenging, with the best GPT-4-based agent only achieving an end-to-end task success rate of 10.59%.

## ALFWorld Dataset

ALFWorld contains interactive TextWorld environments that parallel embodied worlds in the ALFRED dataset, with aligned environments allowing agents to reason and learn high-level policies in an abstract space before solving embodied tasks through low-level actuation.

## Recent Research (2025-2026)

The search results indicate ongoing research in this area. Recent experiments on WebArena and Mind2Web show that world models improve agents' policy selection and demonstrate cost- and time-efficiency compared to recent tree-search-based agents. Additionally, work has validated autonomous agent approaches on challenging vision-based web navigation using both real-world and self-hosted websites from WebVoyager and WebArena, representing effective learning systems for autonomous task proposals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a0e1bd-d9e2-4fa8-9222-20ebdca62fd5",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "690c41bb-7670-4622-961b-574bbc8ff654",
  "sourceToolAssistantUUID": "53a0e1bd-d9e2-4fa8-9222-20ebdca62fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-11T22:34:59.411Z_

<details><summary>↩ Tool result · `toolu_01SbSo72BhBR1SNYzyHR8rSB`</summary>

```text
Web search results for query: "ALFWorld environment setup installation requirements"

Links: [{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"Installation and Setup | alfworld/alfworld | DeepWiki","url":"https://deepwiki.com/alfworld/alfworld/1.1-installation-and-setup"},{"title":"alfworld - Overview","url":"https://github.com/alfworld/"},{"title":"alfworld/README.md at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/blob/master/README.md"},{"title":"alfworld/setup.py at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/blob/master/setup.py"},{"title":"alfworld/configs/base_config.yaml at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/blob/master/configs/base_config.yaml"},{"title":"alfworld/Dockerfile at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/blob/master/Dockerfile"},{"title":"AttributeError: module 'alfworld.agents.environment' has no attribute 'AlfredTWEnv' · Issue #101 · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/issues/101"},{"title":"GitHub - sanjibanc/leap_llm","url":"https://github.com/sanjibanc/leap_llm"},{"title":"alf.environments - Agent Learning Framework (ALF) documentation","url":"https://alf.readthedocs.io/en/latest/api/alf.environments.html"}]

Based on the search results, here are the key ALFWorld environment setup and installation requirements:

## Python Version
ALFWorld requires Python 3.9 or higher.

## Installation Method
Installing from source is recommended for development. The basic steps include:
1. Clone the repo: git clone https://github.com/alfworld/alfworld.git alfworld
2. Create a virtual environment using python 3.9

## Prerequisites/Requirements Files
ALFWorld provides different requirement files depending on your use case:

- requirements.txt for the prerequisites to run ALFWorld text-only version
- requirements-vis.txt for the prerequisites to run ALFWorld with both text and visual modalities
- requirements-full.txt for the full prerequisites to run experiments

## Hardware Requirements
The setup has been tested on: GPU - GTX 1080 Ti (12GB), CPU - Intel Xeon (Quad Core), RAM - 16GB, and OS - Ubuntu 16.04.

## Docker Alternative
You can alternatively pull vzhong's Docker image from https://hub.docker.com/r/vzhong/alfworld or install Docker and NVIDIA Docker.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38fe8684-aec7-44cc-9b1a-07700b418696",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "12629425-defd-4169-9ffd-379b75aac9e9",
  "sourceToolAssistantUUID": "38fe8684-aec7-44cc-9b1a-07700b418696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T22:35:00.803Z_

<details><summary>↩ Tool result · `toolu_01Ksw9uBengzCxrfJFPRbAuf`</summary>

```text
Web search results for query: "SWE-bench docker setup cost compute requirements"

Links: [{"title":"Docker Setup - SWE-bench","url":"https://www.swebench.com/SWE-bench/guides/docker_setup/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"How to run SWE-bench Verified in one hour on one machine | Epoch AI","url":"https://epoch.ai/blog/swebench-docker"},{"title":"SWE-bench Quickstart - SWE-bench","url":"https://www.swebench.com/SWE-bench/guides/quickstart/"},{"title":"GitHub - aorwall/SWE-bench-docker","url":"https://github.com/aorwall/SWE-bench-docker"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub","url":"https://github.com/scaleapi/SWE-bench_Pro-os"},{"title":"FAQ - SWE-bench","url":"https://www.swebench.com/SWE-bench/faq/"},{"title":"Installation - SWE-bench","url":"https://www.swebench.com/SWE-bench/installation/"},{"title":"Docker Deployment | peng-weihan/SWE-QA-Bench | DeepWiki","url":"https://deepwiki.com/peng-weihan/SWE-QA-Bench/2.4-docker-deployment"}]

Based on the search results, here's comprehensive information about SWE-bench Docker setup cost and compute requirements:

## Compute Requirements

SWE-bench evaluation is resource intensive and recommends running on an x86_64 machine with at least 120GB of free storage, 16GB of RAM, and 8 CPU cores. More specifically:

Docker Desktop should allocate at least 8 CPUs and 16GB RAM, with disk image size set to at least 120GB.

## Disk Storage Costs

The disk storage requirements vary depending on the caching strategy:

- With the default cache_level set to env, base and environment images require about 100GB of disk space.
- For the fastest evaluation times with cache_level set to instance, all base, environment, and instance images are stored, taking up about 2,000GB of disk space.

## Image Registry and Optimization

A public Docker image registry has been created with optimizations that reduced the total size of the registry to 67 GiB for all 2290 SWE-bench images (10x reduction), and to 30 GiB for 500 SWE-bench Verified images (6x reduction). This allows running SWE-bench Verified in 62 minutes on a single GitHub actions VM with 32 cores and 128GB of RAM.

## Worker Parallelization

It's recommended to use fewer than min(0.75 * os.cpu_count(), 24) for the --max_workers parameter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc0c04ca-57a4-470d-a6e2-8fcc64e2d9e9",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "de4cd9dd-d6f4-4cc7-a5e7-7fc74c0d08ac",
  "sourceToolAssistantUUID": "dc0c04ca-57a4-470d-a6e2-8fcc64e2d9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T22:35:01.646Z_

<details><summary>↩ Tool result · `toolu_011bUQZuUB6kPxCR7zm6w5Wx`</summary>

```text
Web search results for query: "WebArena environment setup requirements compute GPU docker"

Links: [{"title":"webarena/environment_docker/README.md at main · web-arena-x/webarena","url":"https://github.com/web-arena-x/webarena/blob/main/environment_docker/README.md"},{"title":"webarena/environment_docker at main · web-arena-x/webarena","url":"https://github.com/web-arena-x/webarena/tree/main/environment_docker"},{"title":"GitHub - web-arena-x/webarena: Code repo for \"WebArena: A Realistic Web Environment for Building Autonomous Agents\" · GitHub","url":"https://github.com/web-arena-x/webarena"},{"title":"visualwebarena/environment_docker/README.md at main · web-arena-x/visualwebarena","url":"https://github.com/web-arena-x/visualwebarena/blob/main/environment_docker/README.md"},{"title":"Specialized Configurations with Docker — NVIDIA Container Toolkit","url":"https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html"},{"title":"GPU support in Docker Desktop for Windows | Docker Docs","url":"https://docs.docker.com/desktop/features/gpu/"},{"title":"webarena/README.md at main · web-arena-x/webarena","url":"https://github.com/web-arena-x/webarena/blob/main/README.md"},{"title":"Containers For Deep Learning Frameworks User Guide - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html"},{"title":"web-arena-x/webarena | DeepWiki","url":"https://deepwiki.com/web-arena-x/webarena"},{"title":"Request for shopping_admin_final_0719 Docker image or build instructions · Issue #219 · web-arena-x/webarena","url":"https://github.com/web-arena-x/webarena/issues/219"}]

Based on the search results, here's what I found about WebArena environment setup requirements:

## Infrastructure Requirements

For AWS deployment, the recommended instance type is t3a.xlarge with a 1000GB EBS root volume, and if running your own infrastructure, you should launch an Ubuntu 24.04 LTS instance (t3a.xlarge, 1000GB storage) in us-east-2.

## Software Setup

For local development, WebArena requires Python 3.10+ and involves creating a conda environment with `conda create -n webarena python=3.10`, followed by pip installation of requirements and Playwright installation.

## Docker Configuration

WebArena consists of Docker-based web services with five containerized websites providing different interaction domains, with each website deployed as a separate Docker container with realistic data and functionality. Docker commands are used to start and run containers for various services like shopping, shopping_admin, gitlab, and forum.

## GPU Support (General Docker Information)

While the search results don't specify GPU requirements specific to WebArena, the general Docker/GPU documentation shows that Docker Desktop for Windows supports NVIDIA GPU Paravirtualization (GPU-PV) on NVIDIA GPUs, allowing containers to access GPU resources for compute-intensive workloads, and GPUs can be specified to the Docker CLI using the --gpus option starting with Docker 19.03.

For comprehensive setup details, you can check the official WebArena GitHub repository's environment_docker README file.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bab0de9-a3b1-4015-841a-b1394072f898",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "2c2d0542-33df-49e0-9164-6259bf4cecc1",
  "sourceToolAssistantUUID": "8bab0de9-a3b1-4015-841a-b1394072f898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-11T22:35:07.689Z_

Now let me search for Area 3: Training Cost References.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c2d0542-33df-49e0-9164-6259bf4cecc1",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9566952-9c32-491c-aa96-6a73f717e92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6136,
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

_source line 37 · 2026-05-11T22:35:08.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4RquJNJRoojg1bFtNhcBz`</summary>

```json
{
  "query": "agentic RL training cost GPU hours A100 LLM agent 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9566952-9c32-491c-aa96-6a73f717e92e",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09200f38-3d67-4e43-9b32-44130eaa1bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6136,
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

_source line 38 · 2026-05-11T22:35:09.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182qFcD4VtuRvBkML5BmqKD`</summary>

```json
{
  "query": "WebArena WebRL training compute requirements GPU hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09200f38-3d67-4e43-9b32-44130eaa1bcd",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b388941e-ffdf-428b-b4ff-2545ba3d91b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6136,
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

_source line 39 · 2026-05-11T22:35:10.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DY9kYZyXL2YwFxGG3WPfjj`</summary>

```json
{
  "query": "GRPO training LLM agent GPU cost compute hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b388941e-ffdf-428b-b4ff-2545ba3d91b0",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9f20133-276d-4c23-acfe-ae6f8f387ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6136,
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

_source line 40 · 2026-05-11T22:35:10.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0162c2uaqwtmbfpMUHyoNHV5`</summary>

```json
{
  "query": "reinforcement learning LLM agent training cost 2025 2026 compute budget"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9f20133-276d-4c23-acfe-ae6f8f387ad6",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4c528e6-93a5-4567-9786-d40a7e5d0f6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6136,
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

_source line 41 · 2026-05-11T22:35:11.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SE2TXiDh9nrnrbc6CaH3Lz`</summary>

```json
{
  "query": "TIPS PBRS training cost compute GPU requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4c528e6-93a5-4567-9786-d40a7e5d0f6a",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaYHZ67ZkHSajDuQ4VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f9713ef-fbae-4117-b97f-a1a43866f7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsEzaPjJRQEEpFqPi5Fvcx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1582,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 16371,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1582,
          "output_tokens": 273,
          "cache_read_input_tokens": 16371,
          "cache_creation_input_tokens": 6136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6136,
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

_source line 42 · 2026-05-11T22:35:13.793Z_

<details><summary>↩ Tool result · `toolu_0182qFcD4VtuRvBkML5BmqKD`</summary>

```text
Web search results for query: "WebArena WebRL training compute requirements GPU hours"

Links: [{"title":"GitHub - THUDM/WebRL: Building Open LLM Web Agents with Self-Evolving Online Curriculum RL · GitHub","url":"https://github.com/THUDM/WebRL"},{"title":"WebArena-x","url":"https://webarena.dev/"},{"title":"WebRL: The Framework Training LLM Web Agents - BrightCoding","url":"https://www.blog.brightcoding.dev/2026/05/01/webrl-the-revolutionary-framework-training-llm-web-agents"},{"title":"WebRL/README.md at main · THUDM/WebRL","url":"https://github.com/THUDM/WebRL/blob/main/README.md"},{"title":"webrl: training llm web agents via self","url":"https://arxiv.org/pdf/2411.02337"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"Preprint WEBRL: TRAINING LLM WEB AGENTS VIA SELF-","url":"https://arxiv.org/pdf/2411.02337v1"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/html/2411.02337v1"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning · HF Daily Paper Reviews by AI","url":"https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2411.02337/"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=oVKEAFjEqv"}]

Based on the search results, here are the key compute requirements for WebRL training on WebArena:

## GPU Hardware Requirements

Minimum configuration is 1x A100 80GB for 8B models, with 8x A100 80GB recommended for 70B models.

## Training Time

Training a full WebRL agent from SFT baseline takes 48-72 hours on 8xA100.

## Inference Requirements

For inference, a single RTX 4090 runs the 8B model at interactive speeds.

The framework supports multiple model architectures, including GLM-4-9B, LLaMA-3.1-8B, and LLaMA-3.1-70B, with the compute requirements scaling based on the model size being trained.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b388941e-ffdf-428b-b4ff-2545ba3d91b0",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "096f992e-5f72-48fe-b83a-d7c84eab06ba",
  "sourceToolAssistantUUID": "b388941e-ffdf-428b-b4ff-2545ba3d91b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-11T22:35:16.163Z_

<details><summary>↩ Tool result · `toolu_01A4RquJNJRoojg1bFtNhcBz`</summary>

```text
Web search results for query: "agentic RL training cost GPU hours A100 LLM agent 2025 2026"

Links: [{"title":"Building Efficient RL Training for the Agentic Era - Salesforce","url":"https://www.salesforce.com/blog/efficient-rl-training-agentic-era/"},{"title":"How to Train Scientific Agents with Reinforcement Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/"},{"title":"What is the cost of training large language models?","url":"https://www.cudocompute.com/blog/what-is-the-cost-of-training-large-language-models"},{"title":"Custom LLM Development Cost: What to Budget in 2026 | TechAhead","url":"https://www.techaheadcorp.com/blog/custom-llm-development-cost/"},{"title":"ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents","url":"https://arxiv.org/pdf/2603.18815"},{"title":"Best GPUs for LLM training in 2025 | WhiteFiber","url":"https://www.whitefiber.com/compare/best-gpus-for-llm-training-in-2025"},{"title":"When LLMs Grow Hands and Feet, How to Design our Agentic RL Systems? | Jiachen Liu","url":"https://amberljc.github.io/blog/2025-09-05-agentic-rl-systems.html"},{"title":"Agent2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?","url":"https://arxiv.org/html/2604.10547"},{"title":"LLM Training Cost: What $100M+ Really Buys in 2026","url":"https://aisuperior.com/llm-training-cost/"},{"title":"rLLM Project - Home","url":"https://rllm-project.com/"}]

I've performed the web search on agentic RL training costs with A100 GPUs for LLM agents in 2025-2026. Here's what I found:

## Key Findings on Agentic RL Training Costs

**GPU Pricing (A100):**
2025 cloud pricing for A100 80GB ranges from $3–$5/hr, though pricing can start from $1.50 per hour on some platforms.

**Fine-tuning Costs:**
A 7B model fine-tune costs $45–$720 on A100s or H100s and runs in hours to 2 days, while a 70B fine-tune costs $240–$4,800 and takes 1–7 days.

**Pre-training Costs:**
For pretraining, a 7B model from scratch costs $60K–$1.2M in GPU compute; a 70B model costs $750K–$12M.

**Agentic RL System Architecture:**
Recent research shows that agentic era RL involves models calling tools, browsing the web, and executing code across multi-turn trajectories with thousands of concurrent tool calls and variable-length trajectories. Rollout is I/O-intensive involving sandbox creation and tool sessions, while training is GPU-intensive centered on forward and backward passes and gradient synchronization.

**Efficiency Improvements:**
Deep research agents have achieved 5× faster training (1 day vs 5 days) by adopting fully asynchronous training architecture with decoupled inference and training groups.

The search results indicate that agentic RL training is becoming a more specialized and costly variant of standard LLM training, with infrastructure challenges distinct from traditional RL for chat-based models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09200f38-3d67-4e43-9b32-44130eaa1bcd",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "63476de3-3a17-4034-b101-758d02122d7f",
  "sourceToolAssistantUUID": "09200f38-3d67-4e43-9b32-44130eaa1bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-11T22:35:17.886Z_

<details><summary>↩ Tool result · `toolu_0162c2uaqwtmbfpMUHyoNHV5`</summary>

```text
Web search results for query: "reinforcement learning LLM agent training cost 2025 2026 compute budget"

Links: [{"title":"What is the cost of training large language models?","url":"https://www.cudocompute.com/blog/what-is-the-cost-of-training-large-language-models"},{"title":"How Much Does LLM Training Cost? | Galileo","url":"https://galileo.ai/blog/llm-model-training-cost"},{"title":"Custom LLM Development Cost: What to Budget in 2026 | TechAhead","url":"https://www.techaheadcorp.com/blog/custom-llm-development-cost/"},{"title":"LLM Training Cost: What $100M+ Really Buys in 2026","url":"https://aisuperior.com/llm-training-cost/"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Cost of Training LLM From Scratch in 2026: Real Numbers","url":"https://aisuperior.com/cost-of-training-llm-from-scratch/"},{"title":"Understanding LLM Cost Per Token: A 2026 Practical Guide - Silicon Data — GPU Performance Data for Companies","url":"https://www.silicondata.com/blog/llm-cost-per-token"},{"title":"What Is an LLM? Training Costs and How It Works 2026","url":"https://www.aitooldiscovery.com/ai-infra/what-is-an-llm"},{"title":"What Does It Cost to Build an AI System in 2026? A Practical Look at LLM Pricing","url":"https://www.businesswaretech.com/blog/what-does-it-cost-to-build-an-ai-system-in-2025-a-practical-look-at-llm-pricing"},{"title":"LLM Training Costs and ROI | Teradata","url":"https://www.teradata.com/insights/ai-and-machine-learning/llm-training-costs-roi"}]

Based on the search results, here's what I found about reinforcement learning LLM agent training costs for 2025-2026:

## Frontier Model Training Costs

Current frontier model training costs span $100 million to $1 billion according to Anthropic CEO Dario Amodei. More specifically, frontier model training costs have escalated dramatically—with GPT-4's training estimated at $78-100+ million, and Gemini Ultra 1.0 reaching $192 million, representing a 287,000x increase from the cost of a Transformer model in 2017.

## 2025-2026 Projections

Training costs are projected to reach $5-10 billion by 2025-2026 and potentially $10-100 billion within three years.

## Reinforcement Learning Costs

After initial pre-training, many models undergo fine-tuning phases, such as Reinforcement Learning from Human Feedback (RLHF), to align the model with human preferences and instructions. RLHF involves training additional models (reward models) and running reinforcement learning algorithms that themselves require lots of computations on GPUs and custom data generated by human annotators, which is expensive.

Data annotation now exceeds compute costs by up to 28x for contemporary models, with human-in-the-loop (HITL) annotation for reinforcement learning from human feedback (RLHF) costing approximately $100 per high-quality annotation and expert annotation rates reaching $40 or more per hour.

## Hardware Costs in 2025-2026

NVIDIA H100 (80GB) units cost approximately $25,000 per unit, with additional infrastructure costs of $5,000-$50,000 per GPU for power, cooling, and networking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4c528e6-93a5-4567-9786-d40a7e5d0f6a",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "2e30725b-6714-4b68-aa27-2be6eafcff85",
  "sourceToolAssistantUUID": "f4c528e6-93a5-4567-9786-d40a7e5d0f6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-11T22:35:18.226Z_

<details><summary>↩ Tool result · `toolu_01SE2TXiDh9nrnrbc6CaH3Lz`</summary>

```text
Web search results for query: "TIPS PBRS training cost compute GPU requirements"

Links: [{"title":"What should I consider when choosing a GPU for training vs. inference in my AI project?","url":"https://www.runpod.io/articles/comparison/choosing-a-gpu-for-training-vs-inference"},{"title":"GPU Cloud Pricing 2026: H100 From $2.21/hr — AWS vs Azure vs GCP Compared","url":"https://spendark.com/blog/machine-learning-cloud-cost/"},{"title":"Cloud GPU Pricing - Compare 59 Providers (2026)","url":"https://getdeploying.com/gpus"},{"title":"GPU Computing for AI Training: Complete Hardware and Optimization Guide","url":"https://helpforce.ai/news/gpu-computing-ai-training-hardware-guide-2025"},{"title":"How Much Do GPU Cloud Platforms Cost for AI Startups in 2026?","url":"https://www.gmicloud.ai/en/blog/how-much-do-gpu-cloud-platforms-cost-for-ai-startups-in-2026"},{"title":"Training AI Models and Compute Cost Optimization","url":"https://www.hyperbolic.ai/blog/training-ai-models-and-compute-cost-optimization"},{"title":"Best GPU for AI training (2026 guide)","url":"https://www.runpod.io/articles/guides/best-gpu-for-ai-training-2026"},{"title":"The Essential Guide to GPUs for AI, Training and Inference","url":"https://lambda.ai/blog/the-essential-guide-to-gpus"},{"title":"Exploring the cost of training an AI model on cloud infrastructure","url":"https://nebius.com/blog/posts/cost-of-training-an-ai-model-on-cloud"},{"title":"13 Best GPU for Machine Learning: Complete Selection Guide for Training, Inference, and Optimization - Fluence","url":"https://www.fluence.network/blog/best-gpu-for-machine-learning/"}]

Based on the search results, I found information about GPU training costs and compute requirements, but the search did not return specific results about "TIPS PBRS" training. The results provide general information about GPU training costs and compute requirements for AI models. Let me provide what I found:

## GPU Training Cost & Compute Requirements

GPU pricing ranges from $2-$10 per GPU-hour depending on model, with H100s costing approximately $5-8/hour and A100s costing $2-5/hour.

### Compute Requirements by Model Size

For different model scales:
- Training a full 7B LLM on 1–2 trillion tokens requires approximately 60,000 H100 GPU-hours.
- Use 16GB of VRAM per billion parameters for training and 2GB per billion for inference.

### Recommended GPU Options

For training, you typically need more VRAM and computational power, with high-end GPUs like H100, H200 and A100 being preferred.

For budget training: RTX 4090 (24GB) and RTX 5090 (32GB) are strong single-GPU options when your model fits. L40S (48GB) is a practical step up when you need more VRAM, and when constantly fighting out-of-memory errors, move to 80GB+ (H100/H200) or 180GB usable (B200).

**Note:** The search results did not contain specific information about "TIPS PBRS" training. If you're looking for information about a specific training method or system by that name, you may want to search with additional context or clarify what TIPS PBRS refers to.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f9713ef-fbae-4117-b97f-a1a43866f7d1",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "05109528-ecbe-4717-95e0-bfe0025bf87a",
  "sourceToolAssistantUUID": "1f9713ef-fbae-4117-b97f-a1a43866f7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-11T22:35:18.290Z_

<details><summary>↩ Tool result · `toolu_01DY9kYZyXL2YwFxGG3WPfjj`</summary>

```text
Web search results for query: "GRPO training LLM agent GPU cost compute hours"

Links: [{"title":"What is the cost of training large language models?","url":"https://www.cudocompute.com/blog/what-is-the-cost-of-training-large-language-models"},{"title":"How Much Does LLM Training Cost? | Galileo","url":"https://galileo.ai/blog/llm-model-training-cost"},{"title":"The Complete Guide to GPU Requirements for LLM Fine-Tuning | Runpod Blog","url":"https://www.runpod.io/blog/llm-fine-tuning-gpu-guide"},{"title":"LLM Inference Benchmarking: How Much Does Your LLM Inference Cost? | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/llm-inference-benchmarking-how-much-does-your-llm-inference-cost/"},{"title":"Cost Effective GPU for LLM Training: 2026 Guide","url":"https://aisuperior.com/cost-effective-gpu-for-llm-training/"},{"title":"HuggingFace ml-intern: Open-Source ML Research Agent - AgentConn Blog","url":"https://agentconn.com/blog/huggingface-ml-intern-open-source-ml-research-agent-2026/"},{"title":"How Much Do GPU Cloud Platforms Cost for AI Startups in 2026?","url":"https://www.gmicloud.ai/en/blog/how-much-do-gpu-cloud-platforms-cost-for-ai-startups-in-2026"},{"title":"Local LLM Hardware Guide 2025: GPU Specs & Pricing | Introl Blog","url":"https://introl.com/blog/local-llm-hardware-pricing-guide-2025"},{"title":"Hugging Face Releases ml-intern: An Open-Source AI Agent that Automates the LLM Post-Training Workflow - MarkTechPost","url":"https://www.marktechpost.com/2026/04/21/hugging-face-releases-ml-intern-an-open-source-ai-agent-that-automates-the-llm-post-training-workflow/"},{"title":"GitHub - OpenPipe/ART: Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen3.5, GPT-OSS, Llama, and more! · GitHub","url":"https://github.com/OpenPipe/ART"}]

I found relevant information about GRPO training for LLM agents and GPU costs. Here's what the search results reveal:

## GRPO Training Implementation

GRPO (Group Relative Policy Optimization) is used for training post-training LLM workflows, with implementations handling steps like reading papers, finding datasets, and writing training scripts. ml-intern can implement complex techniques like Group Relative Policy Optimization (GRPO) to optimize math performance.

## GPU Compute Hours and Costs

Recent examples show practical GRPO training scenarios:

- A Qwen3-1.7B base model was trained from a 10% baseline to 32% on GPQA in under 10 hours on a single H100
- The PostTrainBench benchmark tests an agent's ability to post-train a base model within a strict 10-hour window on a single H100 GPU

## General GPU Cost Structure

For broader context on GPU costs:

- Training 70B-parameter-class models on modern clusters (on the order of hundreds of H100/H200-class GPUs for several weeks) typically incurs compute-only cloud costs in the low- to mid-seven-figure range
- NVIDIA H100 (80GB) units cost approximately $25,000 per unit, with additional infrastructure costs of $5,000-$50,000 per GPU for power, cooling, and networking
- Specialized GPU cloud providers charge $0.50-$1.20 per hour on-demand

The search results focus more on general LLM training costs rather than specific GRPO benchmarks, but show that agent training with GRPO on single H100 GPUs can be accomplished in 10 hours for smaller models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9f20133-276d-4c23-acfe-ae6f8f387ad6",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "25f12eed-4b39-40b0-b661-da5baac936ee",
  "sourceToolAssistantUUID": "e9f20133-276d-4c23-acfe-ae6f8f387ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-11T22:35:20.898Z_

Let me do a few more targeted searches to fill in gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f12eed-4b39-40b0-b661-da5baac936ee",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3653dbc-55f3-41f7-a639-e2c5f92d0a3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 48 · 2026-05-11T22:35:22.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Err1skAiDLNGGmbDsN8jD`</summary>

```json
{
  "query": "TIPS turn-level information potential reward shaping training details GPU Qwen verl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3653dbc-55f3-41f7-a639-e2c5f92d0a3f",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc32cd56-2e2e-4561-8b4e-86809b219fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 49 · 2026-05-11T22:35:22.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01632QULXmRzXt7DhHQkfyqS`</summary>

```json
{
  "query": "AgentGym-RL training compute cost GPU hours multi-turn reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc32cd56-2e2e-4561-8b4e-86809b219fc0",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98b1ab66-f493-455e-a9cf-b07fdbe0ce17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 50 · 2026-05-11T22:35:23.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wm9ZRtCBkG2zrztvFnAyT7`</summary>

```json
{
  "query": "Open-AgentRL RLAnything DemyAgent training cost compute ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b1ab66-f493-455e-a9cf-b07fdbe0ce17",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "000b98d9-7639-43fd-a2d3-d409cc1c152e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 51 · 2026-05-11T22:35:24.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uxoyj5ALH2RBW9ehnzQL71`</summary>

```json
{
  "query": "SPEAR Tencent agentic RL self-imitation training compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "000b98d9-7639-43fd-a2d3-d409cc1c152e",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c95cdda5-1a6b-4c5b-bd85-758ca7362608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 52 · 2026-05-11T22:35:25.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KumvG2fbW64VfqmxL9APgK`</summary>

```json
{
  "query": "Planner-R1 reward shaping agentic RL smaller LLMs training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c95cdda5-1a6b-4c5b-bd85-758ca7362608",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6edded19-d60e-47b5-8ee3-0ea9dec83415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 53 · 2026-05-11T22:35:26.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LG2nUpbY1ZtBBcXStaua7S`</summary>

```json
{
  "query": "prime-rl PrimeIntellect agentic RL training scale GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6edded19-d60e-47b5-8ee3-0ea9dec83415",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaZWjNy1qLU8nCEuAfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2e55234-13a8-47cd-a3fa-dfa840f4e39d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YN5GvSNnjCc7ApRab9txUJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1885,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 22507,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4573
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1885,
          "output_tokens": 351,
          "cache_read_input_tokens": 22507,
          "cache_creation_input_tokens": 4573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4573,
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

_source line 54 · 2026-05-11T22:35:29.070Z_

<details><summary>↩ Tool result · `toolu_01Wm9ZRtCBkG2zrztvFnAyT7`</summary>

```text
Web search results for query: "Open-AgentRL RLAnything DemyAgent training cost compute ICML 2026"

Links: [{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"GitHub - Gen-Verse/OpenClaw-RL: OpenClaw-RL: Train any agent simply by talking · GitHub","url":"https://github.com/Gen-Verse/OpenClaw-RL"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"SCALE Workshop @ ICML 2026","url":"https://scale-icml-2026.github.io/"},{"title":"Continual Adaptation at Scale — ICML 2026 Workshop","url":"https://cats-icml.github.io/"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"ICLR 2026 Workshop - Lifelong Agents: Learning, Aligning, Evolving","url":"https://lifelongagent.github.io/"},{"title":"Workshop on Computer Use Agents","url":"https://icml.cc/virtual/2025/workshop/39960"}]

Based on the search results, I found information about RLAnything & DemyAgent as general and scalable agentic RL algorithms accepted at ICML 2026. The GitHub repository for Open-AgentRL contains information about these projects.

However, the search results do not contain specific information about the training cost or compute requirements for these models. The results show that DemyAgent-4B has only 4B parameters and matches or outperforms much larger models (14B/32B) across challenging benchmarks, and the work includes training code and model checkpoints for both policy models (RLAnything-7B/8B) and reward models (RLAnything-Reward-8B/14B), but specific training costs or compute budgets are not mentioned in the available search results.

To find detailed information about training costs and compute requirements, you may need to consult the full ICML 2026 paper or the detailed documentation in the GitHub repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "000b98d9-7639-43fd-a2d3-d409cc1c152e",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "a5e73c58-d3de-44ef-acad-cbf0e276b8b8",
  "sourceToolAssistantUUID": "000b98d9-7639-43fd-a2d3-d409cc1c152e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-11T22:35:30.091Z_

<details><summary>↩ Tool result · `toolu_01632QULXmRzXt7DhHQkfyqS`</summary>

```text
Web search results for query: "AgentGym-RL training compute cost GPU hours multi-turn reinforcement learning"

Links: [{"title":"[2509.08755] AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2509.08755"},{"title":"How to Train Scientific Agents with Reinforcement Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/"},{"title":"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning","url":"https://agentgym-rl.github.io/"},{"title":"GitHub - WooooDyy/AgentGym-RL: Code and implementations for the paper \"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/AgentGym-RL"},{"title":"Reinforcement Learning Revolution – Accelerate Your Agent’s Training with GPUs","url":"https://www.runpod.io/articles/guides/reinforcement-learning-revolution-accelerate-your-agents-training-with-gpus"},{"title":"AgentGym-RL: An Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making via Multi-Turn RL | OpenReview","url":"https://openreview.net/forum?id=ZgCCDwcGwn"},{"title":"AgentGym/AgentGym-RL-Data-ID · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AgentGym/AgentGym-RL-Data-ID"},{"title":"GitHub - NVIDIA-NeMo/Gym: Evaluate and improve models and agents using environments · GitHub","url":"https://github.com/NVIDIA-NeMo/Gym"},{"title":"Paper page - AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2509.08755"},{"title":"Training an Agent - Gymnasium Documentation","url":"https://gymnasium.farama.org/introduction/train_agent/"}]

Based on the search results, I found information about AgentGym-RL and its multi-turn reinforcement learning approach. Here's what the search revealed:

## AgentGym-RL Overview

AgentGym-RL is a framework designed to train LLM agents for multi-turn interactive decision-making through RL. The framework features a modular and decoupled architecture, ensuring high flexibility and extensibility, and encompasses a wide variety of real-world scenarios while supporting mainstream RL algorithms.

## Training Approach

The framework proposes ScalingInter-RL, a training approach designed for exploration-exploitation balance and stable RL optimization, which emphasizes exploitation by restricting the number of interactions in early stages, and gradually shifts towards exploration with larger horizons.

## Model Performance

The framework leverages Qwen2.5-3B and Qwen2.5-7B as primary backbone models. AgentGym-RL-7B outperforms other open-source models by a large margin, substantially enhancing the open-sourced 7B-scale models' capabilities to a level that rivals or even surpasses top-tier proprietary large models.

## Important Note

While the search results provide comprehensive information about AgentGym-RL's architecture, capabilities, and training methodology, **the specific compute cost metrics in GPU hours were not found in the search results**. The paper documentation available through these sources does not appear to include detailed computational resource requirements or GPU hour costs for training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b1ab66-f493-455e-a9cf-b07fdbe0ce17",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "509b59e0-b904-4657-9398-63975abf122c",
  "sourceToolAssistantUUID": "98b1ab66-f493-455e-a9cf-b07fdbe0ce17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-11T22:35:31.876Z_

<details><summary>↩ Tool result · `toolu_01Uxoyj5ALH2RBW9ehnzQL71`</summary>

```text
Web search results for query: "SPEAR Tencent agentic RL self-imitation training compute requirements"

Links: [{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v3"},{"title":"GitHub - TencentYoutuResearch/SPEAR: An RL Recipe for Building Agentic LLMs via Self-Imitation on Long-Horizon Agentic Tasks · GitHub","url":"https://github.com/TencentYoutuResearch/SPEAR"},{"title":"Paper page - Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://huggingface.co/papers/2509.22601"},{"title":"ICLR Poster Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://iclr.cc/virtual/2026/poster/10010088"},{"title":"[2509.22601] Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/abs/2509.22601"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Kssko33Ekq"},{"title":"RollArt: Scaling Agentic RL Training via Disaggregated Infrastructure","url":"https://arxiv.org/html/2512.22560v1"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning - AI Research Papers Daily","url":"https://ai-blogs.co.in/paper/2509.22601v1"},{"title":"Toward Training Superintelligent Software Agents through Self-Play SWE-RL","url":"https://arxiv.org/pdf/2512.18552"},{"title":"GitHub - PrimeIntellect-ai/prime-rl: Agentic RL Training at Scale · GitHub","url":"https://github.com/PrimeIntellect-ai/prime-rl"}]

I found information about SPEAR from Tencent's research. Here's what I found about the compute requirements and training characteristics:

## Overview

SPEAR is a curriculum-based self-imitation learning (SIL) recipe for training agentic LLMs. It's a curriculum-based RL recipe for improving the exploration-exploitation balance with self-imitation and intrinsic reward.

## Compute Requirements

Regarding compute efficiency, the gains incur only 10%–25% extra theoretical complexity and negligible runtime overhead in practice, demonstrating the plug-and-play scalability of SPEAR. This indicates that SPEAR adds minimal computational overhead compared to baseline methods.

## Performance Results

In ALFWorld and WebShop, SPEAR increases the success rates of GRPO/GiGPO/Dr.BoT by up to 16.1%/5.1%/8.6% and 20.7%/11.8%/13.9%, respectively. In AIME24 and AIME25, SPEAR boosts Dr.BoT by up to 3.8% and 6.1%, respectively.

## Model Coverage

SPEAR brings consistent gains across 1.5B and 7B models up to 20%.

The paper was published by Tencent Youtu Research and is available on arXiv (paper 2509.22601), with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c95cdda5-1a6b-4c5b-bd85-758ca7362608",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "edd4ac05-736a-454f-a2d5-d228f182e9e1",
  "sourceToolAssistantUUID": "c95cdda5-1a6b-4c5b-bd85-758ca7362608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-11T22:35:32.064Z_

<details><summary>↩ Tool result · `toolu_019Err1skAiDLNGGmbDsN8jD`</summary>

```text
Web search results for query: "TIPS turn-level information potential reward shaping training details GPU Qwen verl"

Links: [{"title":"GitHub - ucsd-wang-lab-lm/tips: TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs · GitHub","url":"https://github.com/ucsd-wang-lab-lm/tips"},{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=eBMOr6a84z"},{"title":"[2603.22293] TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/abs/2603.22293"},{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/html/2603.22293"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260322293X/abstract"},{"title":"TURN-LEVEL INFORMATION-POTENTIAL REWARD SHAPING ...","url":"https://openreview.net/pdf/13085d9acfed8b19aee5efc0de2bc905f3022ef4.pdf"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22293v1"},{"title":"verl - Qwen docs","url":"https://qwen.readthedocs.io/en/latest/training/verl.html"},{"title":"Qwen Image Models Training - 0 to Hero Level Tutorial - LoRA & Fine Tuning - Base & Edit Model - DEV Community","url":"https://dev.to/furkangozukara/qwen-image-models-training-0-to-hero-level-tutorial-lora-fine-tuning-base-edit-model-2goj"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for ...","url":"https://www.aimodels.fyi/papers/arxiv/tips-turn-level-information-potential-reward-shaping"}]

Based on the search results, here's what I found about TIPS, reward shaping training details, and its implementation with Qwen and VeRL:

## Overview of TIPS

TIPS (Turn-Level Information Potential Reward Shaping) is a framework that assigns dense, turn-level rewards to each reasoning + tool-call segment based on the increased likelihood of the correct answer under a teacher model. The optimization in search-augmented LLMs is often unstable due to sparse rewards and difficult credit assignments across reasoning and tool calls.

## Key Benefits

By leveraging potential-based reward shaping, TIPS offers fine-grained and policy-invariant guidance that overcomes the limitations of outcome-only optimization. Evaluated on seven QA benchmarks, TIPS consistently outperforms GRPO/PPO baselines and substantially improves training stability.

## Performance with Qwen Models

Experiments were conducted with Qwen-2.5-3B Instruct and Qwen-2.5-7B Instruct models, with an additional generalization test across five models from two families: Qwen2.5-3B/7B/14B, Qwen3-4B, and Llama3.1-8B. On Qwen-2.5-7B Instruct, TIPS improves average exact match (EM) and F1 by over 10% relative to PPO, with larger margins over GRPO, while exhibiting reduced training variance and fewer collapse/drift failures.

## GPU and Computational Overhead

TIPS adds only about 12% relative to vanilla PPO for both model sizes, since KV caches can be reused in the teacher forward passes on a given rollout. For comparison, GRPO requires roughly 3.5× the PPO FLOPs for both model sizes.

## VeRL Integration

The TIPS codebase is a verl-based project for Search-R1 style RL training with tool use (multi-turn retrieval, PPO/GRPO training, and validation workflows).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc32cd56-2e2e-4561-8b4e-86809b219fc0",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "a5ab35b8-94c2-4691-a51b-4bc15f7ddc43",
  "sourceToolAssistantUUID": "dc32cd56-2e2e-4561-8b4e-86809b219fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-11T22:35:34.050Z_

<details><summary>↩ Tool result · `toolu_01KumvG2fbW64VfqmxL9APgK`</summary>

```text
Web search results for query: "Planner-R1 reward shaping agentic RL smaller LLMs training details"

Links: [{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/html/2509.25779v2"},{"title":"PLANNER-R1: REWARD SHAPING ENABLES EFFI- CIENT AGENTIC RL WITH SMALLER LLMS","url":"https://arxiv.org/pdf/2509.25779"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs | OpenReview","url":"https://openreview.net/forum?id=CmOaD42eAT"},{"title":"[2509.25779] Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/abs/2509.25779"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250925779Z/abstract"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=agentic+RL"},{"title":"PLANNER-R1: REWARD SHAPING ENABLES EFFI","url":"https://openreview.net/pdf/24fff7e9068e6d8af9f07e73abfdcb0d788c3abe.pdf"},{"title":"Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization","url":"https://arxiv.org/html/2512.07478"},{"title":"Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training","url":"https://arxiv.org/html/2602.22576"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"}]

Based on the search results, here are the key training details for Planner-R1:

## Approach & Methodology

Training uses agentic RL with trajectory-level rewards gated by schema validity. The main focus is the role of reward density: feedback varies from dense, process-level signals to sparse final-pass rewards, and also tests a curriculum that transitions between them. All reward variants are properly shaped, ensuring they converge to the same optimal policy while revealing how granularity influences learning dynamics.

## Performance Results

Planner-R1 achieved a 56.9% final-pass rate with only 180 training queries, a 2.7× improvement over GPT-5's 21.2% baseline and the strongest agentic result on the public leaderboard.

## Key Finding: Smaller Models and Reward Shaping

The central finding concerns how smaller LLMs respond to reward shaping: Smaller models (8B) were highly responsive to reward shaping: with dense process-level signals, they reached competitive performance while being 1.5× more memory-efficient than 32B models. Larger models were more robust under sparse rewards but exhibited smaller relative gains from shaping and higher variance across runs. While curriculum learning offered no significant benefit, shaped rewards consistently amplified learning dynamics, making 8B models the most efficient setting for agentic RL.

## Generalization

Fine-tuned models mostly maintained or exceeded baseline performance on out-of-domain tasks, including Multi-IF, NaturalPlan, and τ-BENCH.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6edded19-d60e-47b5-8ee3-0ea9dec83415",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "2f59e187-37ea-4d02-a2f0-df651e8e5492",
  "sourceToolAssistantUUID": "6edded19-d60e-47b5-8ee3-0ea9dec83415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-11T22:35:34.187Z_

<details><summary>↩ Tool result · `toolu_01LG2nUpbY1ZtBBcXStaua7S`</summary>

```text
Web search results for query: "prime-rl PrimeIntellect agentic RL training scale GPU"

Links: [{"title":"GitHub - PrimeIntellect-ai/prime-rl: Agentic RL Training at Scale · GitHub","url":"https://github.com/PrimeIntellect-ai/prime-rl"},{"title":"Prime Intellect - The Open Stack for Self-Improving Agents","url":"https://www.primeintellect.ai/"},{"title":"INTELLECT-3: A 100B+ MoE trained with large-scale RL","url":"https://www.primeintellect.ai/blog/intellect-3"},{"title":"Introducing Lab: The Full-Stack Platform for Training your Own Models","url":"https://www.primeintellect.ai/blog/lab"},{"title":"INTELLECT-2 Release: The First 32B Parameter Model Trained Through Globally Distributed Reinforcement Learning","url":"https://www.primeintellect.ai/blog/intellect-2-release"},{"title":"INTELLECT-3: Technical Report","url":"https://arxiv.org/html/2512.16144v1"},{"title":"Environments Hub: A Community Hub To Scale RL To Open AGI","url":"https://www.primeintellect.ai/blog/environments"},{"title":"prime-rl/examples/wordle at main · PrimeIntellect-ai/prime-rl","url":"https://github.com/PrimeIntellect-ai/prime-rl/tree/main/examples/wordle"},{"title":"Workflow runs · PrimeIntellect-ai/prime-rl","url":"https://github.com/PrimeIntellect-ai/prime-rl/actions"},{"title":"Prime Intellect: Distributed training and RL with NVIDIA GB200 NVL72","url":"https://nebius.com/customer-stories/prime-intellect"}]

I found comprehensive information about prime-RL, PrimeIntellect's agentic RL framework. Here's what the search reveals:

## prime-RL Framework

prime-RL is designed to be easy to use and hackable, yet capable of scaling to 1000+ GPUs, and is built for fully asynchronous RL for high-throughput agentic training at scale.

prime-RL is an open framework for large-scale asynchronous reinforcement learning that scales seamlessly from a single node to thousands of GPUs, and is tailored for agentic RL with first-class support for multi-turn interactions and tool use.

## INTELLECT-3 Training at Scale

The framework was used to train INTELLECT-3, a 100B+ parameter Mixture-of-Experts model. Both stages of training, including multiple ablations, were carried out on a 512-GPU H200 cluster over the course of two months, with compute orchestration across 512 NVIDIA H200 GPUs in 64 interconnected nodes.

## Key Capabilities

Small experiments can be trained on a single H100 GPU in just over an hour. A key distinction between prime-RL and many other RL trainers is that it is async-only, recognizing that the future of RL is asynchronous.

## Compute Platform

Prime Intellect aggregates cloud GPUs from around the world on a unified platform, enabling small teams and startups to access more compute, with a full training and evaluation stack to support pre-training, agent learning and reinforcement learning at scale, and the company is building infrastructure for distributed pre-training and reinforcement learning for agents using hundreds to thousands of GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2e55234-13a8-47cd-a3fa-dfa840f4e39d",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "74428a63-e449-48bf-8066-46335013f76c",
  "sourceToolAssistantUUID": "b2e55234-13a8-47cd-a3fa-dfa840f4e39d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-11T22:35:36.896Z_

Let me fetch a few more specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74428a63-e449-48bf-8066-46335013f76c",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaaggwX6ZCtQnyLSgff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c33d968-0d33-4a1c-a23e-78729e3738fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxWWHHGNSs4F6vdxiqtR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7893,
      "cache_read_input_tokens": 27080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7893,
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

_source line 61 · 2026-05-11T22:35:38.518Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0113z2FvfbVgTTVh4bLAje6C`</summary>

```json
{
  "url": "https://github.com/ucsd-wang-lab-lm/tips",
  "prompt": "What are the training compute requirements, GPU setup, and training time mentioned? What model sizes were trained? How many GPUs were used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c33d968-0d33-4a1c-a23e-78729e3738fc",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaaggwX6ZCtQnyLSgff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20b0be41-4c2c-41a9-b38c-f3ba8bd41fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxWWHHGNSs4F6vdxiqtR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7893,
      "cache_read_input_tokens": 27080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7893,
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

_source line 62 · 2026-05-11T22:35:39.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ce2db6ZuiLAwBCqsrtsCna`</summary>

```json
{
  "url": "https://github.com/sanjibanc/agent_prm",
  "prompt": "What are the training compute requirements, GPU setup, and training time? What environments does it support? What models were trained?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b0be41-4c2c-41a9-b38c-f3ba8bd41fa9",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaaggwX6ZCtQnyLSgff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55a777a3-3998-45e9-abbe-66ff87ce949e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxWWHHGNSs4F6vdxiqtR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7893,
      "cache_read_input_tokens": 27080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7893,
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

_source line 63 · 2026-05-11T22:35:41.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QFmKMzXX54cSfmyqmJWLGf`</summary>

```json
{
  "url": "https://github.com/blacksnail789521/Agentic-RL-Training-Recipes",
  "prompt": "List all the methods, frameworks, and training approaches covered in this survey. What compute costs or GPU requirements are mentioned? What environments and benchmarks are covered?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a777a3-3998-45e9-abbe-66ff87ce949e",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaaggwX6ZCtQnyLSgff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1470a518-99a8-40fe-a404-5372fb36ac15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxWWHHGNSs4F6vdxiqtR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7893,
      "cache_read_input_tokens": 27080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7893,
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

_source line 64 · 2026-05-11T22:35:42.774Z_

<details><summary>↩ Tool result · `toolu_0113z2FvfbVgTTVh4bLAje6C`</summary>

```text
# Training Compute Requirements from TIPS Repository

Based on the provided web page content, **specific training compute requirements, GPU setup details, model sizes, and training time are not mentioned**.

The documentation only specifies:

- **Hardware requirements**: "GPU training: Linux + CUDA toolchain (CUDA 12.1 recommended)"
- **Optional infrastructure**: "Ray cluster (single node is supported and used by the example scripts)"

The README focuses on installation, data preprocessing, and execution workflows rather than computational specifications. For detailed information about model sizes trained and GPU requirements, you would need to consult the actual research paper referenced: the "ICLR 2026 poster" or the "Arxiv" link provided in the repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20b0be41-4c2c-41a9-b38c-f3ba8bd41fa9",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "d64052cf-3ea8-457c-acbf-e3e126424504",
  "sourceToolAssistantUUID": "20b0be41-4c2c-41a9-b38c-f3ba8bd41fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-11T22:35:42.975Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DFG6v7QWxBLuDthPwap2wf`</summary>

```json
{
  "url": "https://github.com/THUDM/WebRL",
  "prompt": "What are the specific training compute requirements? How many GPUs are needed? What are the training times? What model sizes are supported? How much storage is needed for the environment?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64052cf-3ea8-457c-acbf-e3e126424504",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawaaggwX6ZCtQnyLSgff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fdb2f1b-f478-486e-b704-3b13378590c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxWWHHGNSs4F6vdxiqtR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7893,
      "cache_read_input_tokens": 27080,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 27080,
          "cache_creation_input_tokens": 7893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7893,
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

_source line 66 · 2026-05-11T22:35:44.999Z_

<details><summary>↩ Tool result · `toolu_01Ce2db6ZuiLAwBCqsrtsCna`</summary>

```text
# Agent PRM: Training Requirements & Setup

Based on the repository documentation, here's what's specified:

## Compute & GPU Setup
The README does not explicitly state GPU requirements, memory needs, or training duration. It mentions using "SGLang for fast inference" and recommends "batched" rollouts, suggesting GPU acceleration is expected, but specific hardware specifications aren't documented.

## Supported Environments
The project currently supports **AlfWorld**. The setup instructions include: "Clone AlfWorld from AlfWorld github repository" and require setting an environment variable pointing to the AlfWorld data directory.

## Trained Models
The documentation mentions one pre-trained model: "rl-llm-agent/Llama-3.2-3B-Instruct-sft-alfworld-iter0" which is provided for convenience to skip the initial SFT training stage.

## Training Framework
The pipeline uses:
- **OpenInstruct** (with custom fixes) for PRM training
- **SGLang** (with custom modifications) for inference
- **Llama 3.2 3B** as the base model size demonstrated

The README doesn't provide training time estimates or detailed hardware specifications, focusing instead on workflow instructions rather than computational infrastructure details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55a777a3-3998-45e9-abbe-66ff87ce949e",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "42422114-b25a-4f8f-b213-bdb62423cb50",
  "sourceToolAssistantUUID": "55a777a3-3998-45e9-abbe-66ff87ce949e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-11T22:35:46.985Z_

<details><summary>↩ Tool result · `toolu_01DFG6v7QWxBLuDthPwap2wf`</summary>

```text
# Training Compute Requirements for WebRL

Based on the GitHub repository documentation provided, **specific training compute requirements are not detailed**. The page does not explicitly specify:

- GPU requirements (number or type)
- Training duration/time estimates
- Supported model sizes beyond those released
- Storage capacity needed for the WebArena environment

## What Is Available

The repository does mention released model checkpoints in various sizes:
- "WebRL-GLM-4-9B checkpoint"
- "WebRL-Llama-3.1-8B checkpoint"
- "WebRL-Llama-3.1-70B checkpoint"

However, the documentation focuses on providing code, pretrained models, and instructions for training rather than computational specifications.

## Next Steps

To obtain this information, you would need to:
1. Review the linked research paper (arXiv:2411.02337)
2. Consult the LLaMA-Factory training configuration files in the `hparams` directory
3. Contact the THUDM team directly through the GitHub repository
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fdb2f1b-f478-486e-b704-3b13378590c4",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "de9ebb01-238c-4a76-9e57-328b17cb1415",
  "sourceToolAssistantUUID": "5fdb2f1b-f478-486e-b704-3b13378590c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-11T22:35:49.679Z_

<details><summary>↩ Tool result · `toolu_01QFmKMzXX54cSfmyqmJWLGf`</summary>

```text
# Agentic RL Training Survey: Methods, Costs & Environments

## Training Schemes & Methods

**Rollout & Data Strategies:**
- Reinforced Self-Training (ReST), rejection sampling, and "Group Relative Policy Optimization (GRPO) for group-based sampling"
- Tree-based exploration, curriculum learning (reverse and self-evolving variants)
- Contrastive learning from failure trajectories

**Feedback & Credit Assignment:**
- Outcome vs. process rewards, "Process reward models (PRM)" for dense supervision
- LLM-based critique and retrospective analysis
- Step-level value networks and implicit credit estimation
- Multi-turn reward design adaptations

**Policy Optimization:**
- PPO variants (clipped gradient, entropy bonuses)
- "GRPO" scaling for reasoning tasks
- Asymmetric REINFORCE for off-policy reuse
- Safety-constrained MDPs

**Memory Training:**
- Explicit read/write API fine-tuning, reflection tokens for retrieval triggering
- Multi-conversation summarization pipelines

## Infrastructure Components

**Actor-Learner Architectures:**
- Synchronous (PPO baseline) and asynchronous setups with staleness correction
- "V-trace correction for off-policy lag in asynchronous setups"

**Precision & Acceleration:**
- FP8/FP4 training, block-wise quantization, "Hadamard rotations to spread outliers"
- Adaptive quantization noise for exploration

**Training-Inference Mismatch:**
- Token-level importance sampling, sequence masking, FP32 output head upcasting

## Environments & Benchmarks

**Single-Domain:**
Web navigation, tool use (SQL, code, visual tasks), "hierarchical T5 planner with V-MPO"

**Multi-Domain:**
WebArena, OSWorld, AndroidWorld, ALFWorld bridging reasoning and embodied control

**Certification Benchmarks:**
MMLU, math word problems, SWE-bench, CVE-Bench, ethical hazard scenarios

**No specific GPU/compute costs mentioned in survey.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1470a518-99a8-40fe-a404-5372fb36ac15",
  "isSidechain": true,
  "promptId": "5ed4f59c-7ce6-44b7-89cd-fcc2ff7ebd67",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "54d3608c-8844-4edc-a8e8-779fb5b2eee9",
  "sourceToolAssistantUUID": "1470a518-99a8-40fe-a404-5372fb36ac15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-11T22:35:58.972Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HoH21sGVkXYxwB6jqppqhh`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22293",
  "prompt": "What are the exact training compute requirements? How many GPUs were used? What was the training time? What model sizes were trained? Report any specific numbers about GPU hours, A100s, H100s, or training duration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d3608c-8844-4edc-a8e8-779fb5b2eee9",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawabpwJy2KmxMV6BLySA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5deb7886-fe12-473e-a522-6bad2243d4f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TznX4ZDGdLJK7hMQVoBNi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 34973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-11T22:35:59.923Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PMty721uXcJALocPoyJYhs`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.02337v1",
  "prompt": "What are the exact training compute requirements? How many GPUs were used? What was the training time? Report any specific numbers about GPU hours, hardware, or training duration for WebRL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5deb7886-fe12-473e-a522-6bad2243d4f7",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawabpwJy2KmxMV6BLySA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79afd849-57a8-4653-9edf-411e9d0922d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TznX4ZDGdLJK7hMQVoBNi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 34973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-11T22:36:00.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SoBwEz8sDUikFiU2FtauLW`</summary>

```json
{
  "query": "Agent-R1 training compute GPU hours A100 agentic reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79afd849-57a8-4653-9edf-411e9d0922d2",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawabpwJy2KmxMV6BLySA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dc7a2ac-e7ef-4369-9fef-8d34b36e18a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TznX4ZDGdLJK7hMQVoBNi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 34973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-11T22:36:00.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcmratgLyQ3Cq6gWdfyw4e`</summary>

```json
{
  "query": "RAGEN reasoning agent reinforcement learning training GPU compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc7a2ac-e7ef-4369-9fef-8d34b36e18a0",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011CawabpwJy2KmxMV6BLySA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8080083-d2ef-47ba-b898-8c4bc99c8ef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TznX4ZDGdLJK7hMQVoBNi9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 34973,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 266,
          "output_tokens": 330,
          "cache_read_input_tokens": 34973,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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

_source line 73 · 2026-05-11T22:36:03.111Z_

<details><summary>↩ Tool result · `toolu_01PMty721uXcJALocPoyJYhs`</summary>

```text
# Training Compute Requirements for WebRL

The document does not provide specific information about GPU count, training time, or GPU hours used for WebRL training.

The only compute-related detail mentioned is: "We would like to thank Zhipu AI for sponsoring the computation resources and annotation cost used in this work."

The paper includes hyperparameter tables and training details in Appendix A, but these focus on learning rates, batch sizes, and epoch counts rather than infrastructure specifications. No hardware specifications, duration metrics, or computational resource quantification appear anywhere in the provided content.

To obtain this information, you would need to contact the authors directly or check for supplementary materials not included in this arXiv paper excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79afd849-57a8-4653-9edf-411e9d0922d2",
  "isSidechain": true,
  "promptId": "adc6d305-499e-4676-ad21-0c8f9ec9c836",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "d5169f1f-0835-4bf6-92f6-47d7aaff13b9",
  "sourceToolAssistantUUID": "79afd849-57a8-4653-9edf-411e9d0922d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-11T22:36:04.328Z_

<details><summary>↩ Tool result · `toolu_01HoH21sGVkXYxwB6jqppqhh`</summary>

```text
# TIPS Training Compute Requirements

Based on the paper, here are the specific computational details provided:

## Hardware Configuration
Training runs used **"8×H200 GPUs with FSDP and gradient checkpointing."**

## Model Sizes Trained
The research trained multiple model scales:
- Qwen-2.5-3B Instruct
- Qwen-2.5-7B Instruct
- Qwen-2.5-14B Instruct
- Qwen3-4B-Instruct-2507
- Llama3.1-8B

## Training Duration
Training proceeded for **"500 steps, or until a performance collapse to 0"** on the hardware configuration mentioned above.

## Computational Overhead
The paper specifically quantifies TIPS' additional cost: **"teacher scoring adds only ≈11.7% per-step FLOPs"** compared to standard PPO. Wall-clock overhead was measured at approximately 16-18% for the models tested.

## Notable Limitation
The paper does not provide total GPU-hours or wall-clock training time figures. The focus is on relative computational overhead rather than absolute resource consumption metrics, making it difficult to estimate total training costs without additional calculations based on the hardware and step counts provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5deb7886-fe12-473e-a522-6bad2243d4f7",
  "isSidechain": true,
  "promptId": "adc6d305-499e-4676-ad21-0c8f9ec9c836",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "2fd5ec84-4d27-42da-a681-49a0fa13c052",
  "sourceToolAssistantUUID": "5deb7886-fe12-473e-a522-6bad2243d4f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-11T22:36:05.757Z_

<details><summary>↩ Tool result · `toolu_01SoBwEz8sDUikFiU2FtauLW`</summary>

```text
Web search results for query: "Agent-R1 training compute GPU hours A100 agentic reinforcement learning"

Links: [{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"GitHub - AgentR1/Agent-R1: Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning · GitHub","url":"https://github.com/AgentR1/Agent-R1"},{"title":"GitHub - jiangxinke/Agentic-RAG-R1: Agentic RAG R1 Framework via Reinforcement Learning · GitHub","url":"https://github.com/jiangxinke/Agentic-RAG-R1"},{"title":"[2511.14460] Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://arxiv.org/abs/2511.14460"},{"title":"Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://arxiv.org/html/2511.14460v1"},{"title":"GitHub - PrimeIntellect-ai/prime-rl: Agentic RL Training at Scale · GitHub","url":"https://github.com/PrimeIntellect-ai/prime-rl"},{"title":"Reinforcement Learning Revolution – Accelerate Your Agent’s Training with GPUs","url":"https://www.runpod.io/articles/guides/reinforcement-learning-revolution-accelerate-your-agents-training-with-gpus"},{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"},{"title":"How to Train Scientific Agents with Reinforcement Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/"},{"title":"Paper page - Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://huggingface.co/papers/2511.14460"}]

Based on the search results, I found relevant information about Agent-R1 training with A100 GPUs:

## WebAgent-R1 Training Setup

WebAgent-R1 models are trained on a single node of 8 NVIDIA A100 GPUs with 80GB memory via full-parameter fine-tuning. To optimize GPU utilization, the training adopts DeepSpeed with ZeRO-3 offload, along with gradient checkpointing, FlashAttention-2, and bf16 mixed precision training.

For the specific training configurations:
- For SFT (Supervised Fine-Tuning), a learning rate of 5e-5 and batch size of 128 are used with a cosine LR scheduler for 5% warmup steps.
- For RL training, a constant learning rate of 1e-6 is used with a batch size of 16.

The search results mention Agent-R1 as a general framework for training LLM agents with reinforcement learning, but the specific GPU hour compute metrics for the Agent-R1 project itself are not detailed in these search results. The WebAgent-R1 project provides a concrete example of how A100 GPUs are utilized for agentic reinforcement learning training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dc7a2ac-e7ef-4369-9fef-8d34b36e18a0",
  "isSidechain": true,
  "promptId": "adc6d305-499e-4676-ad21-0c8f9ec9c836",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "e64486d1-e354-4f29-8871-745140bc5a77",
  "sourceToolAssistantUUID": "3dc7a2ac-e7ef-4369-9fef-8d34b36e18a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-11T22:36:07.528Z_

<details><summary>↩ Tool result · `toolu_01EcmratgLyQ3Cq6gWdfyw4e`</summary>

```text
Web search results for query: "RAGEN reasoning agent reinforcement learning training GPU compute requirements"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"RAGEN/ragen/trainer/agent_trainer.py at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/ragen/trainer/agent_trainer.py"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://arxiv.org/html/2604.06268v1"},{"title":"Paper page - RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2504.20073"},{"title":"[2504.20073] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2504.20073"},{"title":"How to Train Scientific Agents with Reinforcement Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"}]

Based on the search results, here's what I found about RAGEN's GPU compute requirements for training:

## GPU Compute Requirements

RAGEN training uses H100 GPUs. Specifically, the framework trains Qwen-2.5 (0.5B) with StarPO variants on H100 GPUs for 200 rollout–update iterations, with each batch sampling 8 prompts, with 16 rollouts per prompt, up to 5 turns and 10 actions.

## About RAGEN

RAGEN (Reasoning AGENT) is a flexible RL framework for training reasoning agents. RAGEN is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

Policy updates use GRPO or PPO with GAE (γ=1.0, λ=1.0), Adam optimizer, entropy bonus (β=0.001), and a response-format penalty (−0.1).

The search results indicate that RAGEN supports distributed training and includes optimizations for efficient GPU usage, though specific requirements for larger models or different configurations are not detailed in the available documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8080083-d2ef-47ba-b898-8c4bc99c8ef4",
  "isSidechain": true,
  "promptId": "adc6d305-499e-4676-ad21-0c8f9ec9c836",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "04524b68-945d-43f8-aea3-19c490e10c8f",
  "sourceToolAssistantUUID": "c8080083-d2ef-47ba-b898-8c4bc99c8ef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-11T22:36:10.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011uRHzZEqGiihh4EnEQGawY`</summary>

```json
{
  "query": "WebAgent-R1 training GPU hours total compute cost WebArena"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04524b68-945d-43f8-aea3-19c490e10c8f",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011Cawad9EAtshoxBRohqfmr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23e3b7e4-9c5d-460f-8173-bf07e20b6c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MtM1GW3DbJEfKxaCJyZh9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 36399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2857,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-11T22:36:11.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFPsS3W2M6ToTKEq2mSjuX`</summary>

```json
{
  "query": "\"DOM diff\" \"reward shaping\" OR \"observation signal\" agent reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23e3b7e4-9c5d-460f-8173-bf07e20b6c78",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011Cawad9EAtshoxBRohqfmr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e82c04cd-7e51-4daf-972c-a0e64e1c92ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MtM1GW3DbJEfKxaCJyZh9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 36399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2857,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-11T22:36:12.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cw9U553gtzyHfPbf566ANt`</summary>

```json
{
  "query": "OpenPipe ART agent reinforcement trainer GRPO training cost GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e82c04cd-7e51-4daf-972c-a0e64e1c92ab",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011Cawad9EAtshoxBRohqfmr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b61125e-4315-4847-981a-2ca85bbf638a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MtM1GW3DbJEfKxaCJyZh9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 36399,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 2857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2857,
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

_source line 80 · 2026-05-11T22:36:15.819Z_

<details><summary>↩ Tool result · `toolu_011uRHzZEqGiihh4EnEQGawY`</summary>

```text
Web search results for query: "WebAgent-R1 training GPU hours total compute cost WebArena"

Links: [{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"GitHub - weizhepei/WebAgent-R1: [EMNLP 2025] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning · GitHub","url":"https://github.com/weizhepei/WebAgent-R1"},{"title":"Paper page - WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2505.16421"},{"title":"WebArena-x","url":"https://webarena.dev/"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=KqrYTALRjH"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.16421v1"},{"title":"[Literature Review] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://www.themoonlight.io/en/review/webagent-r1-training-web-agents-via-end-to-end-multi-turn-reinforcement-learning"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to- ...","url":"https://www.alphaxiv.org/abs/2505.16421"}]

Based on the search results, I found information about WebAgent-R1, but the specific details about GPU hours and total compute cost are not directly mentioned in these search results. The results focus on the paper's methodology, performance improvements, and training approach.

From the search results, I can tell you that WebAgent-R1 is an end-to-end multi-turn RL framework for training web agents that learns directly from online interactions with web environments. The paper describes their training infrastructure and efficiency measures, such as "using vLLM with a tensor parallel size of 1 and a GPU memory utilization ratio of 0.7" for efficient LLM rollouts.

However, the search results don't contain explicit information about the total GPU hours used for training or the specific compute costs. To find these specific technical details, you may need to access the full paper PDF directly from arXiv (arxiv.org/pdf/2505.16421) or the GitHub repository (github.com/weizhepei/WebAgent-R1), as this information is often included in supplementary materials or detailed sections of research papers that aren't fully captured in web summaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23e3b7e4-9c5d-460f-8173-bf07e20b6c78",
  "isSidechain": true,
  "promptId": "adc6d305-499e-4676-ad21-0c8f9ec9c836",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "492e22ff-3ae8-4f75-b532-ecec873ba746",
  "sourceToolAssistantUUID": "23e3b7e4-9c5d-460f-8173-bf07e20b6c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-11T22:36:17.943Z_

<details><summary>↩ Tool result · `toolu_01GFPsS3W2M6ToTKEq2mSjuX`</summary>

```text
Web search results for query: ""DOM diff" "reward shaping" OR "observation signal" agent reinforcement learning"

Links: [{"title":"Reward Shaping for Faster Learning in Reinforcement ...","url":"https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Define Observation and Reward Signals in Custom Environments - MATLAB & Simulink","url":"https://www.mathworks.com/help/reinforcement-learning/ug/define-reward-and-observation-signals.html"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"LOGIC-BASED REWARD SHAPING FOR MULTI-AGENT REINFORCEMENT LEARNING","url":"https://arxiv.org/pdf/2206.08881"},{"title":"Reward Models in Deep Reinforcement Learning: A Survey","url":"https://arxiv.org/html/2506.15421v1"},{"title":"The role of reward signal in deep reinforcement learning","url":"https://www.researchgate.net/publication/349731636_The_role_of_reward_signal_in_deep_reinforcement_learning"},{"title":"[2103.15941] Shaping Advice in Deep Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2103.15941"},{"title":"Reward Shaping for Reinforcement Learning with An Assistant Reward Agent | OpenReview","url":"https://openreview.net/forum?id=a3XFF0PGLU"},{"title":"(PDF) Reward shaping for knowledge-based multi-objective multi-agent reinforcement learning","url":"https://www.researchgate.net/publication/328531682_Reward_shaping_for_knowledge-based_multi-objective_multi-agent_reinforcement_learning"}]

The search results show information about reward shaping and observation signals in reinforcement learning, but they don't specifically address "DOM diff" (Document Object Model differences) in relation to these concepts. Let me provide you with what the search results contain:

## Reward Shaping in Reinforcement Learning

Reward shaping is the use of small intermediate 'fake' rewards given to the learning agent that help it converge more quickly. Reward shaping is a powerful technique for accelerating learning by providing more informative feedback to agents, and helps overcome the sparse reward problem by giving intermediate signals based on progress toward goals.

## Observation Signals

Choosing the right observations for the agent is crucial for effective training and performance in reinforcement learning, and the observations should provide sufficient information about the current environment state for the agent to make informed decisions.

## Combining Both Concepts

When designing a reinforcement learning environment, the choice of observation and reward signals is crucial because they directly influence the agent's learning efficiency and its ability to generalize and perform well in the task.

However, the search results do not contain specific information about "DOM diff" in the context of reinforcement learning agents. DOM (Document Object Model) differences might be relevant for web automation or UI-based RL tasks, but that specific connection is not covered in these results. If you're looking for research on agents that use DOM differences as observation signals with reward shaping, you may need to search for more specialized literature on web automation or UI-based reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e82c04cd-7e51-4daf-972c-a0e64e1c92ab",
  "isSidechain": true,
  "promptId": "9e372975-987f-4122-b82d-85f7203b623d",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "69286faa-dfd7-4a86-a8a3-1f660e37cd8f",
  "sourceToolAssistantUUID": "e82c04cd-7e51-4daf-972c-a0e64e1c92ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-11T22:36:19.411Z_

<details><summary>↩ Tool result · `toolu_01Cw9U553gtzyHfPbf566ANt`</summary>

```text
Web search results for query: "OpenPipe ART agent reinforcement trainer GRPO training cost GPU"

Links: [{"title":"GitHub - OpenPipe/ART: Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen3.5, GPT-OSS, Llama, and more! · GitHub","url":"https://github.com/OpenPipe/ART"},{"title":"ART Docs - OpenPipe","url":"https://art.openpipe.ai/"},{"title":"OpenPipe: Building ART·E: Reinforcement Learning for Email Search Agent Development - ZenML LLMOps Database","url":"https://www.zenml.io/llmops-database/building-art-e-reinforcement-learning-for-email-search-agent-development"},{"title":"GRPO with OpenPipe ART — NVIDIA NeMo Agent Toolkit (1.6)","url":"https://docs.nvidia.com/nemo/agent-toolkit/latest/improve-workflows/finetuning/rl_with_openpipe.html"},{"title":"GitHub - Josephrp/openpipe-ART: Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more!","url":"https://github.com/Josephrp/openpipe-ART"},{"title":"ART/README.md at main · OpenPipe/ART","url":"https://github.com/OpenPipe/ART/blob/main/README.md"},{"title":"openpipe-art - Agent Reinforcement Trainer","url":"https://pypi.org/project/openpipe-art/"},{"title":"Tutorial: The OpenPipe ART project - Wandb","url":"https://wandb.ai/onlineinference/genai-research/reports/Tutorial-The-OpenPipe-ART-project--VmlldzoxMzcxMDQyMg"},{"title":"Teaching Small LLMs to Think — Part 2: Reinforcement Learning with OpenPipe ART | Queryloop","url":"https://www.queryloop.ai/blog/teaching-small-llms-to-think-part-2-reinforcement-learning-with-openpipe-art"},{"title":"OpenPipe | RL For Agents","url":"https://openpipe.ai/"}]

Based on the search results, here's what I found about OpenPipe ART with GRPO training:

## Overview

ART (Agent Reinforcement Trainer) is an open-source training framework for teaching agentic LLMs to improve performance and reliability through experience. ART provides a convenient wrapper around reinforcement learning techniques like GRPO (Group Relative Policy Optimization) to dramatically improve model performance while minimizing training costs.

## Training Cost and GPU Infrastructure

A concrete example of training costs comes from OpenPipe's ART·E project: The resulting model achieved higher accuracy while being faster and cheaper than o3, taking fewer turns to answer questions correctly and hallucinating less frequently, all while being trained on a single H100 GPU for under $80.

## GPU Requirements and Infrastructure

Run the ART client on your laptop and let the ART server kick off an ephemeral GPU-enabled environment, or run on a local GPU. W&B Training (Serverless RL) is the first publicly available service for flexibly training models with reinforcement learning. It manages your training and inference infrastructure automatically, letting you focus on defining your data, environment and reward function—leading to faster feedback cycles, lower costs, and far less DevOps.

## Training Efficiency

GRPO runs reached competitive reward scores in far fewer steps than PPO. OpenPipe ART finished training in under 40 minutes per run. PPO with Agent-R1 required 6–8 hours for similar experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b61125e-4315-4847-981a-2ca85bbf638a",
  "isSidechain": true,
  "promptId": "9e372975-987f-4122-b82d-85f7203b623d",
  "agentId": "a8dcaa37ccc3468ff",
  "type": "user",
  "uuid": "ef35a336-38ae-4f7c-92eb-540a2c3b1944",
  "sourceToolAssistantUUID": "1b61125e-4315-4847-981a-2ca85bbf638a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-11T22:38:17.919Z_

Now I have comprehensive data across all three areas. Here is the full report.

---

# Feasibility Assessment: PBRS for LLM Agent Training via RL

## 1. Existing Implementations on GitHub

There is a rich and rapidly growing ecosystem of open-source code directly relevant to your proposed project. Here are the key building blocks:

### Directly Relevant: PBRS / Dense Reward Shaping for LLM Agents

**TIPS (Turn-level Information-Potential Reward Shaping)**
- Repository: [ucsd-wang-lab-lm/tips](https://github.com/ucsd-wang-lab-lm/tips)
- The most directly relevant project. TIPS converts sparse outcome-only signals into dense, turn-level feedback using a PBRS construction that preserves optimal policies. It assigns rewards to each reasoning + tool-call segment based on increased likelihood of the correct answer under a teacher model. Built on [verl](https://github.com/verl-project/verl). Trained on Qwen-2.5-3B/7B/14B, Qwen3-4B, Llama3.1-8B. Improves EM by 11.8% and F1 by 13.6% over PPO on Qwen-2.5-7B. Adds only ~12% FLOPs overhead vs vanilla PPO (compared to GRPO which requires ~3.5x PPO FLOPs). ICLR 2026 poster.

**Planner-R1: Reward Shaping for Agentic RL**
- Paper: [arxiv.org/abs/2509.25779](https://arxiv.org/abs/2509.25779) | [OpenReview](https://openreview.net/forum?id=CmOaD42eAT)
- Central finding: 8B models are highly responsive to dense process-level reward shaping, reaching competitive performance while being 1.5x more memory-efficient than 32B models. Achieved 56.9% final-pass rate with only 180 training queries (2.7x over GPT-5 baseline). Demonstrates that shaped rewards are more important for smaller models.

**AgentPRM (Process Reward Models for LLM Agents)**
- Repository: [sanjibanc/agent_prm](https://github.com/sanjibanc/agent_prm)
- Lightweight actor-critic paradigm using Monte Carlo rollouts for process reward. Includes InversePRM (learns process rewards from demonstrations without explicit outcome supervision). Evaluated on ALFWorld; small 3B models trained with AgentPRM outperform GPT-4o baselines. Uses Llama-3.2-3B as base model.

### Agentic RL Training Frameworks (Infrastructure)

**WebRL (Web Agent RL)**
- Repository: [THUDM/WebRL](https://github.com/THUDM/WebRL)
- Self-evolving online curriculum RL for WebArena. Includes outcome-supervised reward model (ORM). Improves Llama-3.1-8B from 4.8% to 42.4% on WebArena-Lite. Supports GLM-4-9B, Llama-3.1-8B, and Llama-3.1-70B.

**Open-AgentRL (RLAnything & DemyAgent)**
- Repository: [Gen-Verse/Open-AgentRL](https://github.com/Gen-Verse/Open-AgentRL)
- ICML 2026. General and scalable agentic RL across terminal, GUI, SWE, and tool-call settings. Includes SFT and RL datasets. DemyAgent-4B matches/outperforms 14B/32B models.

**SPEAR (Tencent)**
- Repository: [TencentYoutuResearch/SPEAR](https://github.com/TencentYoutuResearch/SPEAR)
- Curriculum-based self-imitation learning recipe. Adds only 10-25% extra theoretical complexity. Boosts GRPO/GiGPO/Dr.BoT by up to 20.7% on WebShop and 16.1% on ALFWorld. Supports 1.5B and 7B models. ICLR 2026 poster.

**prime-rl (PrimeIntellect)**
- Repository: [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl)
- Fully asynchronous RL for agentic training at scale (1000+ GPUs). First-class multi-turn and tool-use support. Used to train INTELLECT-3 (100B+ MoE) on 512 H200 GPUs over 2 months. Small experiments run on a single H100 in ~1 hour.

**RAGEN**
- Repository: [RAGEN-AI/RAGEN](https://github.com/RAGEN-AI/RAGEN)
- StarPO framework for multi-turn, trajectory-level agent training. Supports GRPO and PPO with GAE. Trains Qwen-2.5-0.5B on H100 GPUs. RAGEN-2 studies reasoning collapse in agentic RL.

**AgentGym-RL**
- Repository: [WooooDyy/AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL)
- Multi-turn RL for long-horizon decision making. ScalingInter-RL approach. AgentGym-RL-7B rivals/surpasses proprietary models. Wide variety of real-world scenarios.

**Agent-R1 / WebAgent-R1**
- Repositories: [AgentR1/Agent-R1](https://github.com/0russwest0/Agent-R1) | [weizhepei/WebAgent-R1](https://github.com/weizhepei/WebAgent-R1)
- End-to-end RL for multi-step agent tasks. WebAgent-R1 extends GRPO to multi-turn settings (M-GRPO) with asynchronous trajectory rollout. Trained on 8x A100 80GB GPUs with DeepSpeed ZeRO-3.

**OpenPipe ART (Agent Reinforcement Trainer)**
- Repository: [OpenPipe/ART](https://github.com/OpenPipe/ART)
- GRPO-based training for multi-step agents. Supports Qwen3.5, GPT-OSS, Llama. Finished training in under 40 minutes per run on a single H100 for under $80. PPO with Agent-R1 required 6-8 hours for similar experiments.

**verl (HybridFlow)**
- Repository: [verl-project/verl](https://github.com/verl-project/verl)
- The underlying RL post-training framework used by TIPS, RAGEN, and others. Flexible and efficient.

### Curated Resource Lists

- [Agentic-RL-Training-Recipes](https://github.com/blacksnail789521/Agentic-RL-Training-Recipes) -- comprehensive survey of all methods, covering rollout strategies, reward types (outcome vs. process), credit assignment, PPO/GRPO variants, memory training, and async architectures.
- [Awesome-Agent-RL](https://github.com/tongjingqi/Awesome-Agent-RL) -- curated list on reward construction for AI agents.
- [Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models) -- comprehensive collection of PRMs.

### Gap: DOM Diff as PBRS Signal

No existing implementation was found that specifically uses DOM diffs as a potential function for PBRS. The closest analog is TIPS, which uses information-theoretic potential (likelihood under a teacher model) rather than environment observation diffs. Your proposed approach of using observation changes (DOM diffs, inventory changes, test outputs) as the potential function would be novel. The TIPS PBRS framework and verl infrastructure provide the cleanest starting point for implementing this.

---

## 2. Dataset & Environment Availability

### WebArena
- **Datasets on HuggingFace**: [AmineHA/WebArena-Verified](https://huggingface.co/datasets/AmineHA/WebArena-Verified), [ST-WebAgentBench/st-webagentbench](https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench)
- **Setup**: Docker-based, 5 containerized websites (e-commerce, forum, GitLab, CMS, Reddit). Requires AWS t3a.xlarge or equivalent with 1000GB EBS storage. Python 3.10+, conda environment, Playwright. No GPU needed for the environment itself (GPU is for the agent model).
- **Cost**: Environment hosting is CPU-only; a t3a.xlarge instance costs ~$0.15/hr on AWS. The 1TB storage requirement is the main cost driver (~$80/month on EBS gp3).
- **Freely available**: Yes, fully open source at [web-arena-x/webarena](https://github.com/web-arena-x/webarena).

### ALFWorld
- **Datasets on HuggingFace**: [awawa-agi/alfworld-raw](https://huggingface.co/datasets/awawa-agi/alfworld-raw), [awawa-agi/alfworld-prompts](https://huggingface.co/datasets/awawa-agi/alfworld-prompts), [u-10bei/sft_alfworld_trajectory_dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset), and subsets within [hkust-nlp/agentboard](https://huggingface.co/datasets/hkust-nlp/agentboard) (134 test rows).
- **Setup**: Python 3.9+, lightweight TextWorld-based environment. Tested on GTX 1080 Ti (12GB), quad-core CPU, 16GB RAM, Ubuntu. Docker image available at [vzhong/alfworld](https://hub.docker.com/r/vzhong/alfworld).
- **Compute**: Very low -- runs on consumer hardware. No GPU needed for the environment.
- **Freely available**: Yes, fully open source at [alfworld/alfworld](https://github.com/alfworld/alfworld).

### SWE-bench
- **Datasets on HuggingFace**: Multiple variants available:
  - [princeton-nlp/SWE-bench](https://huggingface.co/datasets/princeton-nlp/SWE-bench) -- 2,294 instances from 12 Python repos
  - [SWE-bench/SWE-bench_Verified](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified) -- 500 curated instances
  - [princeton-nlp/SWE-bench_Lite](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite) -- 300 instances
  - [SWE-bench/SWE-smith](https://huggingface.co/datasets/SWE-bench/SWE-smith) -- 50,137 training instances from 128 repos (largest training set)
  - [SWE-bench-Live/SWE-bench-Live](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live) -- continuously updated
- **Setup**: x86_64 machine, at least 120GB storage, 16GB RAM, 8 CPU cores. Docker Desktop with 8+ CPUs and 16GB+ RAM allocated. Storage ranges from 100GB (env cache) to 2TB (instance cache). Optimized registry: 30GB for SWE-bench Verified, 67GB for full SWE-bench.
- **Evaluation speed**: SWE-bench Verified can run in 62 minutes on a single 32-core machine with 128GB RAM.
- **Freely available**: Yes, fully open source at [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench).

### Other Relevant Benchmarks
- [McGill-NLP/agent-reward-bench](https://huggingface.co/datasets/McGill-NLP/agent-reward-bench) -- reward model benchmark for agents including WebArena judgments.
- [AgentGym/AgentGym-RL-Data-ID](https://huggingface.co/datasets/AgentGym/AgentGym-RL-Data-ID) -- RL training data for AgentGym.

### Summary: All three environments (WebArena, ALFWorld, SWE-bench) are freely available with open-source code and HuggingFace datasets. ALFWorld is the cheapest to run (consumer hardware). WebArena requires ~1TB storage and a modest cloud instance. SWE-bench needs 120GB-2TB storage and a beefy CPU machine for evaluation.

---

## 3. Training Cost References

### Concrete Numbers from Specific Projects

| Project | Model Size | Hardware | Duration / Cost | Notes |
|---------|-----------|----------|----------------|-------|
| **TIPS** | Qwen-2.5-3B/7B/14B | 8x H200 GPUs | 500 training steps; ~12% overhead vs PPO | Wall-clock ~16-18% overhead; GRPO costs 3.5x PPO FLOPs |
| **WebRL** | 8B-70B | 1x A100 80GB (8B) to 8x A100 80GB (70B) | 48-72 hours on 8xA100 (full training) | Minimum 1x A100 for 8B models |
| **WebAgent-R1** | 8B | 8x A100 80GB | Not reported (single node) | DeepSpeed ZeRO-3, FlashAttention-2, bf16 |
| **OpenPipe ART** | Various | 1x H100 | <40 minutes per run; <$80 total | GRPO-based; PPO took 6-8 hours for similar |
| **RAGEN** | 0.5B | H100 GPUs | 200 iterations, 8 prompts x 16 rollouts | Small-scale research framework |
| **prime-rl / INTELLECT-3** | 100B+ MoE | 512x H200 | 2 months | Production scale; small experiments ~1 hour on 1x H100 |
| **Planner-R1** | 8B | Not specified | 180 training queries | 8B most efficient for reward shaping |
| **SPEAR** | 1.5B-7B | Not specified | 10-25% overhead vs baseline | Minimal extra compute |
| **GRPO (general)** | 1.7B | 1x H100 | <10 hours | Qwen3-1.7B from 10% to 32% on GPQA |

### General GPU Cost Reference Points (2026)

- **A100 80GB cloud rental**: $2-5/hr (spot/on-demand varies)
- **H100 80GB cloud rental**: $2.21-8/hr depending on provider
- **H200 cloud rental**: Higher, less widely available
- **7B model fine-tune**: $45-$720 on A100s/H100s, hours to 2 days
- **70B model fine-tune**: $240-$4,800, 1-7 days

### Estimated Budget for Your Project

Based on the data above, here are reasonable estimates for a PBRS-with-observation-diffs research project:

- **Small scale (3B-8B model, ALFWorld)**: 1x A100/H100, 1-3 days. Cost: ~$100-500 in cloud compute.
- **Medium scale (7B-8B model, WebArena)**: 8x A100 80GB, 2-3 days. Cost: ~$800-3,000 in cloud compute, plus ~$100/month for WebArena environment hosting.
- **Full scale (8B-70B, multi-environment)**: 8x A100/H100, 1-2 weeks. Cost: ~$3,000-15,000 in cloud compute.

The OpenPipe ART result (<$80 for a competitive GRPO run on 1x H100) suggests that if you start with a small model and efficient GRPO implementation, initial experiments are very affordable.

---

## Overall Feasibility Assessment

The project is highly feasible. The key findings are:

1. **Strong building blocks exist**: TIPS provides an actual PBRS implementation for LLM agents built on verl, and its codebase can be adapted to use observation-based potentials instead of teacher-model likelihoods. AgentPRM provides process reward infrastructure for ALFWorld specifically.

2. **Your proposed signal is novel**: No existing work uses DOM diffs / observation diffs as the potential function in a PBRS construction. TIPS uses information-theoretic potential, and Planner-R1 uses schema-validity signals. This is a genuine research contribution.

3. **All environments are free and accessible**: WebArena, ALFWorld, and SWE-bench all have open-source environments with HuggingFace datasets. ALFWorld is the easiest starting point.

4. **Costs are manageable**: Initial experiments with 3B-8B models can be run for under $500. A thorough study across environments and model sizes would cost $3,000-15,000 in GPU compute.

5. **Recommended starting stack**: verl + TIPS codebase for the PBRS framework, ALFWorld for initial experiments (cheapest, well-studied by AgentPRM), then WebArena for web-specific DOM diff experiments.

Sources:
- [TIPS GitHub](https://github.com/ucsd-wang-lab-lm/tips)
- [TIPS Paper (arXiv)](https://arxiv.org/abs/2603.22293)
- [AgentPRM GitHub](https://github.com/sanjibanc/agent_prm)
- [AgentPRM Paper](https://arxiv.org/abs/2502.10325)
- [Planner-R1 Paper](https://arxiv.org/abs/2509.25779)
- [WebRL GitHub](https://github.com/THUDM/WebRL)
- [WebRL Paper](https://arxiv.org/abs/2411.02337)
- [Open-AgentRL GitHub](https://github.com/Gen-Verse/Open-AgentRL)
- [SPEAR GitHub](https://github.com/TencentYoutuResearch/SPEAR)
- [prime-rl GitHub](https://github.com/PrimeIntellect-ai/prime-rl)
- [RAGEN GitHub](https://github.com/RAGEN-AI/RAGEN)
- [AgentGym-RL GitHub](https://github.com/WooooDyy/AgentGym-RL)
- [WebAgent-R1 GitHub](https://github.com/weizhepei/WebAgent-R1)
- [OpenPipe ART GitHub](https://github.com/OpenPipe/ART)
- [verl GitHub](https://github.com/verl-project/verl)
- [Agentic-RL-Training-Recipes Survey](https://github.com/blacksnail789521/Agentic-RL-Training-Recipes)
- [Awesome-Agent-RL](https://github.com/tongjingqi/Awesome-Agent-RL)
- [Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [WebArena GitHub](https://github.com/web-arena-x/webarena)
- [WebArena Docker Setup](https://github.com/web-arena-x/webarena/blob/main/environment_docker/README.md)
- [ALFWorld GitHub](https://github.com/alfworld/alfworld)
- [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench)
- [SWE-bench Docker Setup](https://www.swebench.com/SWE-bench/guides/docker_setup/)
- [SWE-bench Verified (HuggingFace)](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)
- [SWE-smith (HuggingFace)](https://huggingface.co/datasets/SWE-bench/SWE-smith)
- [WebArena-Verified (HuggingFace)](https://huggingface.co/datasets/AmineHA/WebArena-Verified)
- [ALFWorld-raw (HuggingFace)](https://huggingface.co/datasets/awawa-agi/alfworld-raw)
- [Epoch AI: SWE-bench in 1 hour](https://epoch.ai/blog/swebench-docker)
- [Salesforce: Efficient RL Training for the Agentic Era](https://www.salesforce.com/blog/efficient-rl-training-agentic-era/)
- [Agent-R1 GitHub](https://github.com/0russwest0/Agent-R1)
- [LLM Reward Shaping Framework (Alex Zhang)](https://alexzhang13.github.io/assets/pdfs/Reward_Shaping_LLM.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef35a336-38ae-4f7c-92eb-540a2c3b1944",
  "isSidechain": true,
  "agentId": "a8dcaa37ccc3468ff",
  "requestId": "req_011Cawae22cgnVqWLrqd68p5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bec20241-b447-4207-bbf7-74cab39e956b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d3248afb-e3ca-44de-b1af-e0845a7ab538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ubip4SXE64Tkui8ow98uMb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 39256,
      "output_tokens": 5346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5346,
          "cache_read_input_tokens": 39256,
          "cache_creation_input_tokens": 2886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2886,
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
