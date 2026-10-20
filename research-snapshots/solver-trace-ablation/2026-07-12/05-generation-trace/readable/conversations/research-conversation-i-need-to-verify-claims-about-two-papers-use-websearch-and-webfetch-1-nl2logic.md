# Research conversation: I need to verify claims about two papers. Use WebSearch and WebFetch. 1. **NL2Logic** (arXiv 2602.13237) - Claims: AST-g

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a39f5c098b85d3911.jsonl`
- **Structured JSON:** [`5610f856a0dad0884ce2.json`](../../sessions/56/5610f856a0dad0884ce2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-10T19:20:25.979Z_

I need to verify claims about two papers. Use WebSearch and WebFetch.

1. **NL2Logic** (arXiv 2602.13237) - Claims: AST-guided FOL translation achieving 99% syntactic accuracy and 0.99 executable rate across 13 models (0.5B-27B), improving Logic-LM by 31%, EACL 2026 Findings, code at github.com/peng-gao-lab/nl2logic. Also claims that with Qwen2.5-7B, it achieves 0.94 syntax correctness on FOLIO.

2. **VERGE** (arXiv 2601.20055) - Claims: Z3-based verification with semantic routing, 18.7% average improvement on FOLIO/ZebraLogic/AR-LSAT/BBEH/HLE, uses iterative refinement with 120B+ parameter models, January 2026.

For each:
- Verify arXiv existence and title
- Check the claimed metrics
- Verify venue acceptance if claimed
- Check if the paper's methods are accurately characterized

Also search for:
- "NL2Logic FOL translation" to see if claims about executable rates are accurate
- "VERGE formal verification LLM reasoning" to verify the 18.7% claim
- Any other recent FOL translation papers that might compete with NL2Logic

Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "16a2507a-38f3-4ccc-8a38-eecbe1f44d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:20:25.986Z_

```json
{
  "parentUuid": "16a2507a-38f3-4ccc-8a38-eecbe1f44d2e",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
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
  "uuid": "16afee01-017e-4ae9-9844-18080e8c0d07",
  "timestamp": "2026-05-10T19:20:25.986Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:20:28.618Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then conduct the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16afee01-017e-4ae9-9844-18080e8c0d07",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtiDAQqoAKSUXCyJSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebbadb79-e60d-4c51-88af-e76d71ba858b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016McrSvpCLjyVBVaqn4SnTs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 877,
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

_source line 4 · 2026-05-10T19:20:28.999Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014JueFkgRYsTQo2Lz2zgSNV`</summary>

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
  "parentUuid": "ebbadb79-e60d-4c51-88af-e76d71ba858b",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtiDAQqoAKSUXCyJSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cee27b76-f0cb-4300-82a6-9810ddbf4e14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016McrSvpCLjyVBVaqn4SnTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 877,
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

_source line 5 · 2026-05-10T19:20:29.003Z_

<details><summary>↩ Tool result · `toolu_014JueFkgRYsTQo2Lz2zgSNV`</summary>

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
  "parentUuid": "cee27b76-f0cb-4300-82a6-9810ddbf4e14",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "48ba1764-3198-47d3-a8d5-0679b707b4be",
  "sourceToolAssistantUUID": "cee27b76-f0cb-4300-82a6-9810ddbf4e14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:20:31.276Z_



Now let me run all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ba1764-3198-47d3-a8d5-0679b707b4be",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "556b681a-23e4-4326-a54d-59b8609ed9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-10T19:20:31.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKyRazoVVDzJfqf94NNyaa`</summary>

```json
{
  "query": "arXiv 2602.13237 NL2Logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "556b681a-23e4-4326-a54d-59b8609ed9a4",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9075c16b-40bd-425e-9978-6dfb77cf6ff2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-10T19:20:35.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RKGH16XxbtPyztDhpmnjZK`</summary>

```json
{
  "query": "arXiv 2601.20055 VERGE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9075c16b-40bd-425e-9978-6dfb77cf6ff2",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7f3dc01-fd14-4cfa-bfc2-fc22b355340a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-10T19:20:35.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018GJqEyjsituF5zTGSTUBEZ`</summary>

```json
{
  "query": "NL2Logic FOL translation executable rate syntax accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f3dc01-fd14-4cfa-bfc2-fc22b355340a",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21bfc546-4e33-4796-8ecd-decc823d4f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-10T19:20:36.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016D5ng2YcP5x3AeRrcCRniG`</summary>

```json
{
  "query": "VERGE formal verification LLM reasoning 18.7% improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21bfc546-4e33-4796-8ecd-decc823d4f06",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a1eefc3-4a0e-4ed0-8506-be7b4bcd41cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 11 · 2026-05-10T19:20:36.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MBCy8Ha9tiRViCwqPivY4U`</summary>

```json
{
  "query": "FOL first-order logic translation LLM 2025 2026 recent papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a1eefc3-4a0e-4ed0-8506-be7b4bcd41cd",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0c12ef4-3914-49a9-9388-a825b1eed2e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 12 · 2026-05-10T19:20:37.587Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NxvNmjeBQWvexYrsqTiKHB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.13237",
  "prompt": "Extract the full title, authors, abstract, any venue/conference mentions, and all key metrics/results claimed in this paper. Include any mention of executable rate, syntactic accuracy, number of models tested, model sizes, Logic-LM improvement percentage, and EACL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0c12ef4-3914-49a9-9388-a825b1eed2e5",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d8e3c6c-79e8-4d68-9020-644a513b91f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

### Tool result

_source line 13 · 2026-05-10T19:20:39.244Z_

<details><summary>↩ Tool result · `toolu_01NKyRazoVVDzJfqf94NNyaa`</summary>

```text
Web search results for query: "arXiv 2602.13237 NL2Logic"

Links: [{"title":"[2602.13237] NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/abs/2602.13237"},{"title":"NL2Logic: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/html/2602.13237"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/recent?skip=118&show=500"},{"title":"[2603.13237] A Dual-Path Generative Framework for Zero-Day Fraud Detection in Banking Systems","url":"https://arxiv.org/abs/2603.13237"},{"title":"SAKURA: On the Multi-hop Reasoning of Large Audio-Language Models Based on Speech and Audio Information","url":"https://arxiv.org/html/2505.13237"},{"title":"[2602.10177] Towards Autonomous Mathematics Research","url":"https://arxiv.org/abs/2602.10177"},{"title":"Learning to Retrieve with Weakened Labels: Robust Training under Label Noise","url":"https://arxiv.org/html/2512.13237"},{"title":"Large Language Models are Easily Confused: A Quantitative Metric, Security Implications and Typological Analysis","url":"https://arxiv.org/html/2410.13237"},{"title":"[2509.13237] Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors","url":"https://arxiv.org/abs/2509.13237"},{"title":"[2403.13237] Graph Attention Network-based Block Propagation with Optimal AoI and Reputation in Web 3.0","url":"https://arxiv.org/abs/2403.13237"}]

Based on the search results, here's information about arXiv paper 2602.13237:

The paper is titled "NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models" by Rizky Ramadhana Putra and 3 other authors, and it was accepted to Findings of EACL 2026.

NL2LOGIC is a first-order logic translation framework that introduces an abstract syntax tree as an intermediate representation, combining a recursive large language model based semantic parser with an abstract syntax tree guided generator that deterministically produces solver-ready logic code.

The paper addresses the problem that existing methods suffer from fragile syntax control due to weak enforcement of global grammar constraints and low semantic faithfulness caused by insufficient clause-level semantic understanding.

In terms of performance, experiments on the FOLIO, LogicNLI, and ProofWriter benchmarks show that NL2LOGIC achieves 99 percent syntactic accuracy and improves semantic correctness by up to 30 percent over state-of-the-art baselines. Additionally, integrating NL2LOGIC into Logic-LM yields near-perfect executability and improves downstream reasoning accuracy by 31 percent compared to Logic-LM's original few-shot unconstrained translation module.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9075c16b-40bd-425e-9978-6dfb77cf6ff2",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "dce98474-0d95-41f1-ac2e-b602e725db0d",
  "sourceToolAssistantUUID": "9075c16b-40bd-425e-9978-6dfb77cf6ff2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T19:20:40.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J1qNkEi7rxgTnZyyoBtviT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20055",
  "prompt": "Extract the full title, authors, abstract, any venue/conference mentions, and all key metrics/results claimed. Include any mention of Z3 verification, semantic routing, percentage improvements, benchmarks used (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE), iterative refinement, model sizes, and submission date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce98474-0d95-41f1-ac2e-b602e725db0d",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRtw6ZQrdhio2Vkb9QS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "138eeb31-e720-42a4-bc18-9d85110db36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgfBfFaft5wq4KyWp97hRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

### Tool result

_source line 15 · 2026-05-10T19:20:41.932Z_

<details><summary>↩ Tool result · `toolu_01NxvNmjeBQWvexYrsqTiKHB`</summary>

```text
# NL2LOGIC Paper Summary

**Full Title:**
"NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models"

**Authors:**
Rizky Ramadhana Putra, Raihan Sultan Pasha Basuki, Yutong Cheng, Peng Gao

**Venue:**
Accepted to Findings of EACL 2026

**Abstract Summary:**
The paper proposes a framework for translating natural language into first-order logic using an abstract syntax tree as an intermediate representation. It combines an LLM-based semantic parser with a tree-guided generator for producing executable logic code.

**Key Results & Metrics:**
- Syntactic accuracy: 99 percent
- Semantic correctness improvement: Up to 30 percent over state-of-the-art baselines
- Downstream reasoning accuracy improvement when integrated with Logic-LM: 31 percent increase
- Executability: Described as "near-perfect" when integrated with Logic-LM

**Benchmarks Tested:**
FOLIO, LogicNLI, and ProofWriter

**Paper Details:**
17 pages, 6 figures; submitted January 29, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d8e3c6c-79e8-4d68-9020-644a513b91f1",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "fbe8a69b-51a3-48b5-90db-3593b0d03ac2",
  "sourceToolAssistantUUID": "7d8e3c6c-79e8-4d68-9020-644a513b91f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:20:42.481Z_

<details><summary>↩ Tool result · `toolu_018GJqEyjsituF5zTGSTUBEZ`</summary>

```text
Web search results for query: "NL2Logic FOL translation executable rate syntax accuracy"

Links: [{"title":"NL2Logic: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/html/2602.13237"},{"title":"Advancing Natural Language Formalization to First Order ...","url":"https://arxiv.org/pdf/2509.22338"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic","url":"https://openreview.net/pdf?id=lBc3MXcGqZ"},{"title":"Evaluating LLMs Capabilities at Natural Language to Logic ...","url":"https://ceur-ws.org/Vol-3904/paper13.pdf"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into","url":"https://www.arxiv.org/pdf/2602.13237"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into ...","url":"https://people.cs.vt.edu/penggao/papers/nl2logic-eacl26findings.pdf"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"Speaking in Words, Thinking in Logic: A Dual-Process Framework in QA Systems","url":"https://arxiv.org/pdf/2507.20491"},{"title":"[2602.13237] NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/abs/2602.13237"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"}]

Based on the search results, here's what I found about NL2Logic FOL translation performance:

## Key Performance Metrics

NL2Logic attains 99% syntactic accuracy on the FOLIO, LogicNLI, and ProofWriter benchmarks and improves semantic correctness by 30% over state-of-the-art baselines.

NL2Logic achieves near-perfect executable rate (0.99) across all 13 models, which represents a significant improvement. For context, Logic-LM's original few-shot translation produces highly variable executable rates (0.01-0.94), with particularly poor performance on smaller models.

## Approach

NL2Logic is a FOL translation framework that uses an AST as an intermediate layer, combining a recursive LLM-based semantic parser with an AST-guided generator that deterministically produces solver-ready code. The AST-guided generator ensures syntactic correctness by deterministically compiling the FOLAST through a two-pass algorithm that registers constants, variables, and relation signatures, while also assembling scoped expressions following solver-specific grammar, producing executable logical rules compatible with solvers such as Z3 and SMT-LIB.

## Integration Results

Integrating NL2Logic into Logic-LM yields near-perfect executability and improves downstream reasoning accuracy by 31% over Logic-LM's original few-shot unconstrained FOL translation module.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21bfc546-4e33-4796-8ecd-decc823d4f06",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "7ac6781e-7fb8-4075-94ae-ab0355e600d9",
  "sourceToolAssistantUUID": "21bfc546-4e33-4796-8ecd-decc823d4f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:20:43.474Z_

<details><summary>↩ Tool result · `toolu_01RKGH16XxbtPyztDhpmnjZK`</summary>

```text
Web search results for query: "arXiv 2601.20055 VERGE"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1181&show=2000"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[2604.20055] From Fuzzy to Formal: Scaling Hospital Quality Improvement with AI","url":"https://arxiv.org/abs/2604.20055"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2603.01549"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1499&show=2000"},{"title":"Chunking, Retrieval, and Re-ranking: An Empirical Evaluation of...","url":"https://arxiv.org/abs/2601.15457"},{"title":"An Addressable and Tunable Module for Donor-based Scalable Silicon Quantum Computing","url":"https://arxiv.org/html/2412.20055"}]

Based on the search results, here's what I found about arXiv paper 2601.20055:

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

This paper is authored by Vikash Singh (Case Western Reserve University), Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless (Amazon Web Services).

### Overview
VERGE presents a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The work addresses the fundamental challenge of ensuring the logical correctness of Large Language Models despite their syntactic fluency.

### Key Approach
The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

### Three Main Innovations
The framework introduces: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies (symbolic solvers for logical claims and LLM ensembles for commonsense reasoning), and (3) precise logical error localization via Minimal Correction Subsets (MCS) to pinpoint the exact subset of claims to revise.

### Results
The system iteratively refines answers using structured feedback until acceptance criteria are met or convergence is achieved, delivering formal guarantees where possible and consensus verification elsewhere.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7f3dc01-fd14-4cfa-bfc2-fc22b355340a",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "3686f606-36ff-4923-96a3-b250b8f36adb",
  "sourceToolAssistantUUID": "e7f3dc01-fd14-4cfa-bfc2-fc22b355340a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T19:20:43.479Z_

<details><summary>↩ Tool result · `toolu_016D5ng2YcP5x3AeRrcCRniG`</summary>

```text
Web search results for query: "VERGE formal verification LLM reasoning 18.7% improvement"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"VeriPlan: Integrating Formal Verification and LLMs into End-User Planning | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3706598.3714113"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/pdf/2507.13290"},{"title":"Enhancing Mathematical Reasoning in Large Language ...","url":"https://aclanthology.org/2025.acl-long.594.pdf"}]

Based on the search results, I found relevant information about VERGE and the 18.7% improvement metric you mentioned.

## VERGE: Formal Verification and LLM Reasoning

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement by decomposing LLM outputs into atomic claims, autoformalizing them into first-order logic, and verifying their logical consistency using automated theorem proving.

### Key Improvements and Performance

VERGE, using the GPT-OSS-120B model, demonstrated an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE) compared to single-pass approaches.

### Core Innovations

The framework includes three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise.

### Notable Advantages

VERGE exhibits monotonic improvement across iterations, contrasting sharply with probabilistic self-refinement methods that often degrade performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a1eefc3-4a0e-4ed0-8506-be7b4bcd41cd",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "db62c53f-6cc6-426b-9fa5-97da96167488",
  "sourceToolAssistantUUID": "2a1eefc3-4a0e-4ed0-8506-be7b4bcd41cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:20:45.546Z_

<details><summary>↩ Tool result · `toolu_01MBCy8Ha9tiRViCwqPivY4U`</summary>

```text
Web search results for query: "FOL first-order logic translation LLM 2025 2026 recent papers"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"[2509.22338] Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/abs/2509.22338"},{"title":"Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/html/2509.22338v1"},{"title":"Do LLMs Really Struggle at NL-FOL Translation? ...","url":"https://arxiv.org/pdf/2511.11816"},{"title":"Few-Shot Natural Language to First-Order Logic Translation via Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.547/"},{"title":"Do LLMs Really Struggle at NL-FOL Translation? Revealing their Strengths via a Novel Benchmarking Strategy","url":"https://arxiv.org/html/2511.11816"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"Neuro-Symbolic Reasoning with Multiple Large Language Models Combined by First-Order Logic | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08462-0_18"},{"title":"Few-Shot Natural Language to First-Order Logic ...","url":"https://aclanthology.org/2025.naacl-long.547.pdf"},{"title":"Advancing Natural Language Formalization to First Order ...","url":"https://arxiv.org/pdf/2509.22338"}]

I found several recent papers on FOL (First-Order Logic) translation with LLMs from 2025-2026. Here are the key findings:

## Recent Papers on FOL Translation with LLMs:

### 1. **FoVer: First-Order Logic Verification for Natural Language Reasoning** (2025)
An automated pipeline that verifies the logical correctness of reasoning texts using first-order logic, operating through LLM-driven translation of natural language into executable logical expressions and automated logical verification using the Z3 theorem prover.

### 2. **Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs** (September-November 2025)
A systematic evaluation of fine-tuned LLMs for automating the translation of natural language to first-order logic, comparing architectures (encoder-decoder vs. decoder-only) and training strategies. Their fine-tuned Flan-T5-XXL achieves 70% accuracy with predicate lists, outperforming GPT-4o and even the DeepSeek-R1-0528 model with CoT reasoning ability.

### 3. **Do LLMs Really Struggle at NL-FOL Translation?** (November 2025, Accepted at AAAI-26)
This work examines existing datasets and protocols for evaluating NL-FOL translation performance and proposes a novel evaluation protocol to distinguish genuine semantic-level logical understanding from pattern recognition, showing that state-of-the-art dialogue-oriented LLMs demonstrate strong NL-FOL translation skills.

### 4. **Code4Logic: Few-Shot Natural Language to First-Order Logic Translation via Code Generation** (April 2025)
A novel NL-FOL translation method based on in-context learning that employs code snippets to bridge the gap between natural language and first-order logic.

### 5. **Neuro-Symbolic Reasoning with Multiple LLMs Combined by First-Order Logic** (2026)
A training-free neuro-symbolic model that integrates multiple LLMs by converting their latent knowledge into unified first-order logic representations, parsing object-centric features and generating structured FOL-based representations.

These papers collectively show active research in improving LLM-based FOL translation, with diverse approaches including fine-tuning, code generation, verification pipelines, and neuro-symbolic integration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0c12ef4-3914-49a9-9388-a825b1eed2e5",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "75b4cef4-984b-4214-ba3b-f194b4ab5cb7",
  "sourceToolAssistantUUID": "b0c12ef4-3914-49a9-9388-a825b1eed2e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:20:46.279Z_

<details><summary>↩ Tool result · `toolu_01J1qNkEi7rxgTnZyyoBtviT`</summary>

```text
# VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

**Full Title:** VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

**Authors:** Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless

**Submission Date:** January 27, 2026 (v1); revised May 2, 2026 (v2)

**Classification:** Computer Science > Computation and Language (cs.CL); Artificial Intelligence (cs.AI)

## Abstract Summary
The framework combines large language models with SMT solvers to generate verified answers through iterative refinement. Key innovations include:

1. **Multi-model consensus** using formal semantic equivalence checking to align candidates at the logic level
2. **Semantic routing** directing claims to appropriate verification strategies (symbolic solvers for logical claims, LLM ensembles for commonsense)
3. **Minimal Correction Subsets (MCS)** pinpointing exact claims needing revision

## Key Results & Metrics
- **Performance improvement:** "average performance uplift of 18.7% at convergence across a set of reasoning benchmarks" when compared to single-pass approaches
- **Model tested:** GPT-OSS-120B

## Notable Technical Elements
The system decomposes outputs into atomic claims, autoformalizes them into first-order logic, and verifies consistency using automated theorem proving. It classifies claims by logical status and aggregates verification signals into a unified score with variance-based penalties.

**Note:** Specific benchmark names (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE) and Z3 solver details were not mentioned in the provided abstract content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "138eeb31-e720-42a4-bc18-9d85110db36a",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "50aad08f-b41c-4efc-ba9a-87edb2d1d2ca",
  "sourceToolAssistantUUID": "138eeb31-e720-42a4-bc18-9d85110db36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T19:20:48.254Z_

Now let me fetch the actual paper pages for more detailed metric verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50aad08f-b41c-4efc-ba9a-87edb2d1d2ca",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRvChCRDdBmYYXMGx9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf02755-7e3b-4943-8f31-fac9a9cc9943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJsMBbFRhD5ftn3CJJqaC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 11012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5731,
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

_source line 22 · 2026-05-10T19:20:52.554Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KyTNw3GxC6LQsA3fMqfhex`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.13237",
  "prompt": "Find and extract: 1) The exact executable rate numbers (is it 0.99 across 13 models?), 2) The exact model size range (0.5B-27B?), 3) The exact number of models tested (13?), 4) Any mention of Qwen2.5-7B and its syntax correctness on FOLIO (0.94?), 5) The exact syntactic accuracy percentage (99%?), 6) EACL 2026 Findings acceptance, 7) GitHub repository URL. Report all specific numbers you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf02755-7e3b-4943-8f31-fac9a9cc9943",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRvChCRDdBmYYXMGx9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39f0b08f-619a-464e-99c4-c2f3d71722d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJsMBbFRhD5ftn3CJJqaC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 11012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5731,
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

_source line 23 · 2026-05-10T19:20:55.851Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XjrZzLbPQ72EP3ExjyKyio`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.20055",
  "prompt": "Find and extract: 1) The exact 18.7% average improvement claim and which benchmarks it covers (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE?), 2) Whether Z3 is specifically mentioned as the verification tool, 3) Whether 'semantic routing' is used as a term, 4) Whether 120B+ parameter models are used (GPT-OSS-120B?), 5) The iterative refinement details, 6) Any venue/conference acceptance, 7) The exact submission date. Report all specific numbers and benchmark names you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f0b08f-619a-464e-99c4-c2f3d71722d4",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRvChCRDdBmYYXMGx9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54ac8c7c-42c2-4510-952f-51133d752994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJsMBbFRhD5ftn3CJJqaC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 11012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5731,
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

_source line 24 · 2026-05-10T19:20:57.250Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JKCUnMU67GCbSAGFN9icgt`</summary>

```json
{
  "url": "https://github.com/peng-gao-lab/nl2logic",
  "prompt": "Does this GitHub repository exist? What does it contain? Is it the code for the NL2Logic paper? What is the description and content?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54ac8c7c-42c2-4510-952f-51133d752994",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRvChCRDdBmYYXMGx9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c74d4a6b-0e6a-4b12-ba93-2808d308466b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJsMBbFRhD5ftn3CJJqaC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 11012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5731,
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

_source line 25 · 2026-05-10T19:20:59.489Z_

<details><summary>↩ Tool result · `toolu_01KyTNw3GxC6LQsA3fMqfhex`</summary>

```text
# NL2Logic: Key Findings Extraction

## Executable Rate & Model Testing

The paper confirms **0.99 executable rate across all models** tested. Specifically: "NL2Logic achieves near-perfect executable rate (0.99) across all 13 models and both datasets." The model size range is **0.5B to 27B parameters**, with **13 distinct models evaluated** including Gemma, Llama, Mistral, and Qwen variants.

## Syntax Correctness Metrics

The framework achieves **99% syntactic accuracy**: "NL2Logic attains 99% syntactic accuracy and improves semantic correctness by 30% over state-of-the-art baselines."

For Qwen-2.5-7B specifically, Table 1 shows syntax correctness rates of **0.94 on FOLIO and 0.99 on LogicNLI** (not 0.94 on FOLIO alone—it reached 0.94 there but higher on other datasets).

## Semantic & Integration Improvements

The method improves semantic correctness by **31% over Logic-LM's baseline**: "improving downstream reasoning accuracy by 31% over Logic-LM's original few-shot unconstrained FOL translation module."

## Repository & Publication Details

**GitHub URL**: "we release our implementation at: https://github.com/peng-gao-lab/nl2logic"

**Publication venue**: No mention of EACL 2026 acceptance appears in the provided content. The document is identified as an arXiv preprint (2602.13237v1).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39f0b08f-619a-464e-99c4-c2f3d71722d4",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "d9c43491-74aa-4311-abcd-67ce47dc6fc5",
  "sourceToolAssistantUUID": "39f0b08f-619a-464e-99c4-c2f3d71722d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T19:21:02.056Z_

<details><summary>↩ Tool result · `toolu_01JKCUnMU67GCbSAGFN9icgt`</summary>

```text
# NL2Logic GitHub Repository

Yes, this repository exists. It contains the official implementation of the NL2Logic paper.

## Overview

NL2Logic is "a framework for translating natural language into semantically faithful and syntactically executable first-order logic (FOL) using an AST-guided approach." Rather than generating logic in one step, it iteratively builds a First-Order Logic Abstract Syntax Tree and deterministically compiles it into solver-ready code compatible with engines like Z3.

## Contents

The repository includes:

- **Core modules**: `pipeline.py` (main entry point), `ast_rl.py`, and `structured_output.py`
- **Documentation**: README with installation and usage instructions
- **Configuration files**: Requirements and environment setup
- **License**: MIT

## Key Features

The system has been tested on multiple models including Gemma, Llama, Qwen, and Mistral variants. It supports multiple LLM backends (OpenAI, vLLM, Ollama) and provides a simple public API through the `Pipeline` class.

The paper was accepted to the EACL 2026 conference and uses datasets including LogicNLI, FOLIO, and ProofWriter for evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c74d4a6b-0e6a-4b12-ba93-2808d308466b",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "348e4f3d-6630-4f29-9311-884a82bf1ccb",
  "sourceToolAssistantUUID": "c74d4a6b-0e6a-4b12-ba93-2808d308466b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:21:03.633Z_

<details><summary>↩ Tool result · `toolu_01XjrZzLbPQ72EP3ExjyKyio`</summary>

```text
# VERGE Framework Extraction Summary

## 1) 18.7% Average Performance Improvement
The paper states: **"VERGE demonstrates an average performance uplift of 18.7% at convergence"** across reasoning benchmarks with GPT-OSS-120B. However, the paper does NOT explicitly list which specific benchmarks this aggregate covers in the introduction.

Table 1 shows results across six benchmarks: FOLIO, ProofWriter, ZebraLogic, AR-LSAT, BBEH, and HLE. The 18.7% figure appears to be a computed mean across these datasets at convergence (T_max=10), though the abstract specifies "convergence" rather than the standard T=3 comparison point.

## 2) Verification Tool Specification
**Yes, Z3 is explicitly mentioned.** The text states: "we check satisfiability using the Z3 solver" in Section 3.4 (SMT-Based Verification).

## 3) Semantic Routing Terminology
**Confirmed.** The paper uses "semantic routing" extensively. Section 3.4 is titled "Verification Cascade" with subsection "Semantic Routing (Flexibility Mechanism)." The routing function is defined in Equation 4.

## 4) Model Scale (120B+ Parameters)
**Yes, GPT-OSS-120B is used.** The paper evaluates three models: GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet. GPT-OSS-120B crosses what the authors call the "Formalization Barrier" (>90% SMT syntax validity).

## 5) Iterative Refinement Details
- **Maximum iterations:** T_max = 3 (standard comparison) and T_max = 10 (convergence analysis)
- **Termination criteria:** 𝒮(𝒜) ≥ 0.75 OR Δ𝒮 < 0.01 (convergence)
- **Feedback components:** Unsat Cores, MCS (Minimal Correction Subsets), and Joint Conflicts

## 6) Venue/Conference Acceptance
**Not mentioned.** The paper is identified as arXiv preprint 2601.20055v2, dated 02 May 2026. No conference acceptance information appears in the provided content.

## 7) Submission/Publication Date
**arXiv version date:** 02 May 2026 (listed as "arXiv:2601.20055v2 [cs.CL]")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54ac8c7c-42c2-4510-952f-51133d752994",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "8289a0a1-4cc2-4d37-b55b-ca22ca90af04",
  "sourceToolAssistantUUID": "54ac8c7c-42c2-4510-952f-51133d752994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T19:21:07.263Z_

Now I have comprehensive data. Let me do one final check on the VERGE benchmarks to confirm the exact list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8289a0a1-4cc2-4d37-b55b-ca22ca90af04",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRwUvYYB9Qnm2F2AF5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1f1ebd1-266d-44fc-9e10-e4e3f4300cd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP86YxJFAVkxQETxZcjtNm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 308,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 16743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1557,
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

_source line 29 · 2026-05-10T19:21:11.263Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RjwJM9hDEz1Vg1y5NRPNxm`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning",
  "prompt": "Extract the specific benchmarks used by VERGE, the exact improvement percentages per benchmark, whether the 18.7% is averaged across FOLIO/ZebraLogic/AR-LSAT/BBEH/HLE or also includes ProofWriter. Also extract any details about which models were tested and the iterative refinement process."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1f1ebd1-266d-44fc-9e10-e4e3f4300cd8",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRwUvYYB9Qnm2F2AF5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "886f40b1-2100-4986-8903-46c73e48a6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP86YxJFAVkxQETxZcjtNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 308,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 16743,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 308,
          "output_tokens": 205,
          "cache_read_input_tokens": 16743,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1557,
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

_source line 30 · 2026-05-10T19:21:16.362Z_

<details><summary>↩ Tool result · `toolu_01RjwJM9hDEz1Vg1y5NRPNxm`</summary>

```text
# VERGE Benchmarks and Performance Analysis

## Benchmarks Used
VERGE was evaluated on five specific reasoning benchmarks: FOLIO, ZebraLogic, AR-LSAT, BBEH, and HLE. The document does not mention ProofWriter as part of the evaluation set.

## Overall Performance
The paper reports "an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks" comparing VERGE to single-pass approaches. However, the review does not provide individual improvement percentages for each benchmark—only the aggregated figure across these five datasets.

## Model Tested
VERGE utilized "the GPT-OSS-120B model" for its experiments. The paper notes an important discovery called the "Formalization Barrier," indicating that models under 20B parameters struggle with valid SMT formalization, while those at 120B+ parameters successfully achieve this capability.

## Iterative Refinement Process
The system operates through repeated cycles where the LLM generates answers, which are then decomposed into atomic claims, formalized, and verified. When verification fails, the system computes feedback using Minimal Correction Subsets to guide refinement, allowing "monotonic improvement across iterations" rather than degradation seen in probabilistic self-refinement methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "886f40b1-2100-4986-8903-46c73e48a6b0",
  "isSidechain": true,
  "promptId": "25ba4436-1dca-421d-a3aa-b10d8ba0cf89",
  "agentId": "a39f5c098b85d3911",
  "type": "user",
  "uuid": "115b0328-bf04-4cf2-886a-44c6431e7d31",
  "sourceToolAssistantUUID": "886f40b1-2100-4986-8903-46c73e48a6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T19:22:00.701Z_

I now have all the information needed. Here is the full verification report.

---

## Verification Report

### Paper 1: NL2Logic (arXiv 2602.13237)

**arXiv existence and title:** CONFIRMED. The paper exists at arXiv 2602.13237 with the title "NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models." Authors: Rizky Ramadhana Putra, Raihan Sultan Pasha Basuki, Yutong Cheng, Peng Gao.

**Claimed metrics verification:**

| Claim | Verdict |
|---|---|
| 99% syntactic accuracy | CONFIRMED. The paper states "NL2Logic attains 99% syntactic accuracy." |
| 0.99 executable rate across 13 models (0.5B-27B) | CONFIRMED. The paper states "near-perfect executable rate (0.99) across all 13 models and both datasets." Model sizes range 0.5B-27B, including Gemma, Llama, Mistral, and Qwen variants. |
| Improves Logic-LM by 31% | CONFIRMED. "Improving downstream reasoning accuracy by 31% over Logic-LM's original few-shot unconstrained FOL translation module." |
| Qwen2.5-7B achieves 0.94 syntax correctness on FOLIO | CONFIRMED. Table 1 shows Qwen2.5-7B achieves 0.94 syntax correctness specifically on FOLIO (and 0.99 on LogicNLI). |
| EACL 2026 Findings | CONFIRMED. The arXiv abstract page and the GitHub repository both confirm acceptance to Findings of EACL 2026. |
| Code at github.com/peng-gao-lab/nl2logic | CONFIRMED. The repository exists, contains the implementation (pipeline.py, ast_rl.py, structured_output.py), is MIT licensed, and matches the paper's description. |

**Method characterization:** ACCURATE. The paper does use an AST (Abstract Syntax Tree) as an intermediate representation, combining a recursive LLM-based semantic parser with an AST-guided generator that deterministically produces solver-ready logic code compatible with Z3 and SMT-LIB.

**One nuance:** The "99% syntactic accuracy" is across FOLIO, LogicNLI, and ProofWriter benchmarks collectively -- the claim as stated is accurate but aggregated. The semantic correctness improvement is "up to 30%" (not exactly 30% uniformly).

---

### Paper 2: VERGE (arXiv 2601.20055)

**arXiv existence and title:** CONFIRMED. The paper exists at arXiv 2601.20055 with the title "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning." Authors: Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless.

**Claimed metrics verification:**

| Claim | Verdict |
|---|---|
| Z3-based verification | CONFIRMED. The paper explicitly states "we check satisfiability using the Z3 solver" in Section 3.4 (SMT-Based Verification). |
| Semantic routing | CONFIRMED. Section 3.4 uses this exact term, with a subsection titled "Semantic Routing (Flexibility Mechanism)," formally defined in Equation 4. |
| 18.7% average improvement | CONFIRMED. The paper states "average performance uplift of 18.7% at convergence" using GPT-OSS-120B. |
| Benchmarks: FOLIO/ZebraLogic/AR-LSAT/BBEH/HLE | PARTIALLY CONFIRMED. These five benchmarks are confirmed. However, Table 1 in the paper actually shows results across **six** benchmarks including ProofWriter as well. The 18.7% figure appears to be computed at convergence (T_max=10), not at the standard comparison point (T_max=3). |
| Iterative refinement with 120B+ parameter models | CONFIRMED. GPT-OSS-120B is the primary model. The paper also tests GPT-OSS-20B and Claude 3.7 Sonnet. The paper identifies a "Formalization Barrier" where models under 20B struggle with valid SMT formalization. |
| January 2026 | CONFIRMED. v1 submitted January 27, 2026; v2 revised May 2, 2026. |

**Method characterization:** ACCURATE. VERGE decomposes LLM outputs into atomic claims, autoformalizes them into FOL, verifies via Z3/SMT solvers, and uses semantic routing to direct different claim types to appropriate verification strategies. It uses Minimal Correction Subsets (MCS) for error localization and iterative refinement.

**Nuances:**
- The 18.7% is specifically "at convergence" (T_max=10), which may differ from results at the standard T_max=3 comparison point.
- ProofWriter is also used as a benchmark beyond the five listed in the claim.
- No venue acceptance is claimed or found -- it remains an arXiv preprint.

---

### Competing FOL Translation Papers

Several recent papers compete in the NL-to-FOL translation space:

1. **FoVer** (2025, TACL) -- First-order logic verification for NL reasoning using Z3 theorem prover; an automated pipeline rather than a translation framework per se.
2. **"Advancing Natural Language Formalization to FOL with Fine-tuned LLMs"** (arXiv 2509.22338) -- Fine-tuned Flan-T5-XXL achieves 70% accuracy with predicate lists, outperforming GPT-4o.
3. **"Do LLMs Really Struggle at NL-FOL Translation?"** (arXiv 2511.11816, accepted AAAI-26) -- Proposes a novel evaluation protocol distinguishing genuine semantic understanding from pattern recognition.
4. **Code4Logic** (NAACL 2025) -- Few-shot NL-to-FOL translation via code generation as an intermediate step.
5. **"Efficient Translation of NL-based Logical Problems to FOL"** (arXiv 2506.18383) -- Another recent entry in this space.

NL2Logic's distinguishing contribution relative to these is the AST-guided deterministic compilation guaranteeing syntactic correctness, which none of the competing approaches provide at the same level (0.99 executable rate across 13 models).

---

### Summary

Both papers exist and their core claims are **largely accurate**. NL2Logic's claims are fully verified with no meaningful discrepancies. VERGE's claims are verified with minor nuances: the 18.7% figure is specifically at convergence (T_max=10), and ProofWriter is an additional sixth benchmark beyond the five listed in the claim.

Sources:
- [NL2Logic arXiv page](https://arxiv.org/abs/2602.13237)
- [NL2Logic HTML](https://arxiv.org/html/2602.13237)
- [NL2Logic GitHub](https://github.com/peng-gao-lab/nl2logic)
- [VERGE arXiv page](https://arxiv.org/abs/2601.20055)
- [VERGE HTML](https://arxiv.org/html/2601.20055)
- [VERGE HuggingFace Paper](https://huggingface.co/papers/2601.20055)
- [VERGE Literature Review](https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning)
- [FoVer (TACL)](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural)
- [NL-FOL Fine-tuning](https://arxiv.org/abs/2509.22338)
- [Do LLMs Really Struggle at NL-FOL Translation?](https://arxiv.org/abs/2511.11816)
- [Code4Logic (NAACL 2025)](https://aclanthology.org/2025.naacl-long.547/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "115b0328-bf04-4cf2-886a-44c6431e7d31",
  "isSidechain": true,
  "agentId": "a39f5c098b85d3911",
  "requestId": "req_011CauRxRMWXVGERS2LjyvEz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7daa6f1-e251-4919-b77b-ac3e0fcb5da2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d89a0838-14ce-4fe2-99ef-d218876a6221",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XiJZTK8TMh2i1fL7Rpvoo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 18300,
      "output_tokens": 2041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2041,
          "cache_read_input_tokens": 18300,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 809,
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
