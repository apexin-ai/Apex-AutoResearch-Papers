# Research conversation: I'm reviewing a paper idea called "SinkWatch" that proposes to track attention sink features temporally during LLM gener

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3d1af933f509dd09.jsonl`
- **Structured JSON:** [`dae9c33bf07c56d886e9.json`](../../sessions/da/dae9c33bf07c56d886e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-15T14:12:57.372Z_

I'm reviewing a paper idea called "SinkWatch" that proposes to track attention sink features temporally during LLM generation to detect hallucinations. I need to find competing or concurrent work the authors may have missed. 

Search for:
1. "attention sink hallucination temporal" site:arxiv.org 2025 2026
2. "hallucination detection internal representations temporal dynamics" 2026
3. "attention pattern evolution generation hallucination" arxiv 2026
4. "online hallucination detection attention" LLM 2025 2026
5. "hallucination early detection decoding" arxiv 2026
6. "calibrated uncertainty attention sink" LLM 2026
7. "token-level hallucination detection probe" 2025 2026
8. EMNLP 2025 "hallucination detection" attention outstanding paper
9. "Calibrating Verbal Uncertainty as a Linear Feature" arxiv
10. "Measuring Chain of Thought Faithfulness by Unlearning" arxiv
11. "hallucination basins" arxiv 2026
12. "Frequency-Aware Attention hallucination" arxiv 2026

For each search, report the most relevant results found. I especially need to know about:
- Any paper that tracks attention features over generation steps for hallucination
- Any paper that compares attention-based vs hidden-state-based temporal hallucination signals
- The two EMNLP 2025 Outstanding Papers mentioned (calibrating verbal uncertainty, measuring CoT faithfulness)
- Any work on attention sink dynamics during generation specifically

Use WebSearch for each query. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "8348f829-9463-4ff3-8f92-c859dc1cbf41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:12:57.374Z_

```json
{
  "parentUuid": "8348f829-9463-4ff3-8f92-c859dc1cbf41",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
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
  "uuid": "69650a7f-b2a3-4c2e-817a-bd983e2550ed",
  "timestamp": "2026-05-15T14:12:57.374Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:13:00.372Z_



I'll load the WebSearch tool first, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69650a7f-b2a3-4c2e-817a-bd983e2550ed",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VVMnCWhxPLbwUUriCU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae392e2d-560c-4a86-931e-6663ddf22e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpDTp5dr69HQQneWvnb1x1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 927,
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

_source line 4 · 2026-05-15T14:13:00.513Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CfXskdtRqphhFbNW66bjy8`</summary>

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
  "parentUuid": "ae392e2d-560c-4a86-931e-6663ddf22e69",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VVMnCWhxPLbwUUriCU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1d26be2-de39-4a58-9c87-ccd6599ab0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpDTp5dr69HQQneWvnb1x1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 8223,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 927
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 927,
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

_source line 5 · 2026-05-15T14:13:00.516Z_

<details><summary>↩ Tool result · `toolu_01CfXskdtRqphhFbNW66bjy8`</summary>

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
  "parentUuid": "d1d26be2-de39-4a58-9c87-ccd6599ab0e1",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "31a59d8b-8ed3-4c58-b00c-e55340dfce3c",
  "sourceToolAssistantUUID": "d1d26be2-de39-4a58-9c87-ccd6599ab0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T14:13:03.295Z_



Now let me run all 12 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a59d8b-8ed3-4c58-b00c-e55340dfce3c",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VVbyUhizq17Y1KgHY7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cad571da-5c89-41d9-898a-c9b3641aee24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuSyiwbVWgzBuT3GM9K6Fe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1411,
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

_source line 7 · 2026-05-15T14:13:05.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WipfdQSDzmB6v5UAeupDAx`</summary>

```json
{
  "query": "attention sink hallucination temporal site:arxiv.org 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad571da-5c89-41d9-898a-c9b3641aee24",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VVbyUhizq17Y1KgHY7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f187b31-0806-4b36-8173-d525e7e38dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuSyiwbVWgzBuT3GM9K6Fe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9150,
      "output_tokens": 83,
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
          "input_tokens": 3,
          "output_tokens": 83,
          "cache_read_input_tokens": 9150,
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

_source line 8 · 2026-05-15T14:13:13.311Z_

<details><summary>↩ Tool result · `toolu_01WipfdQSDzmB6v5UAeupDAx`</summary>

```text
Web search results for query: "attention sink hallucination temporal site:arxiv.org 2025 2026"

Links: [{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation","url":"https://arxiv.org/html/2604.10098"},{"title":"[2604.10697] Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2604.10697"},{"title":"FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG","url":"https://arxiv.org/pdf/2601.05866"},{"title":"[2504.10063] Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/abs/2504.10063"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v3"},{"title":"TARAC: Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection","url":"https://arxiv.org/html/2504.04099"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.10027"},{"title":"[2604.10027] SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/abs/2604.10027"},{"title":"[2501.15269] Mirage in the Eyes: Hallucination Attack on Multi-modal Large Language Models with Only Attention Sink","url":"https://arxiv.org/abs/2501.15269"}]

I've successfully performed the web search for your query about attention sink hallucination temporal phenomena on arXiv from 2025-2026. Here are the key findings:

## Recent Research on Attention Sinks and Hallucination

The search returned several highly relevant papers from 2025-2026 examining the relationship between attention sinks and hallucinations:

### Key Papers:

1. **"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models"** (April 2026)
   - Proposes SinkProbe, a hallucination detection method grounded in the observation that hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation

2. **"Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation"** (April 2026)
   - Addresses the challenge of Attention Sink (AS), in which a disproportionate amount of attention is focused on a small subset of specific yet uninformative tokens, complicating interpretability and exacerbating issues such as hallucinations
   - Conducts a comprehensive review and taxonomy of over 180 studies

3. **"TARAC: Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection"** (April 2026)
   - Observes that during the generation process, LVLMs progressively allocate less attention to image tokens as more tokens are generated, and the positions where hallucinated statements occur exhibit correspondingly lower attention to visual information

4. **"SinkTrack: Attention Sink based Context Anchoring for Large Language Models"** (April 2026)
   - Identifies attention drift where LLMs' attention progressively concentrates on more recent tokens, as the generation proceeds, attention on the initial tokens dramatically decays, which is a primary cause of hallucination and context forgetting


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f187b31-0806-4b36-8173-d525e7e38dd1",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "0f17351c-ae1a-4cf7-9dd8-5b9df77b03a9",
  "sourceToolAssistantUUID": "1f187b31-0806-4b36-8173-d525e7e38dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:13:15.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014YNpVG4NNwWCT26cjEh6eC`</summary>

```json
{
  "query": "hallucination detection internal representations temporal dynamics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f17351c-ae1a-4cf7-9dd8-5b9df77b03a9",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37e004f3-3a6b-461e-815e-fc589ca5c07c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 10 · 2026-05-15T14:13:16.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011tXWTKPcvkK43SpkeEYq95`</summary>

```json
{
  "query": "attention pattern evolution generation hallucination arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37e004f3-3a6b-461e-815e-fc589ca5c07c",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df3cdce5-3de9-4434-8432-f920db5f2ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 11 · 2026-05-15T14:13:16.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LhfVVUqHWV1yCpRadPaU96`</summary>

```json
{
  "query": "online hallucination detection attention LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3cdce5-3de9-4434-8432-f920db5f2ea9",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c61bd9a-2aff-45d1-bc91-9190271603f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 12 · 2026-05-15T14:13:17.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XJiec6dpDVhoWWxm4wPzvg`</summary>

```json
{
  "query": "hallucination early detection decoding arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c61bd9a-2aff-45d1-bc91-9190271603f7",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6273447-d0b9-4eef-87e3-21e8d44113df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 13 · 2026-05-15T14:13:17.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dGdGhJUA6sa7TPBPbXTxr`</summary>

```json
{
  "query": "calibrated uncertainty attention sink LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6273447-d0b9-4eef-87e3-21e8d44113df",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae3005a0-1c1b-42bd-be67-067853777488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 14 · 2026-05-15T14:13:17.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxMhJe6EDBH5hkREqVsfYW`</summary>

```json
{
  "query": "token-level hallucination detection probe 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae3005a0-1c1b-42bd-be67-067853777488",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e20fc00-b4d1-40bb-90fa-bd8367cbdaa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 15 · 2026-05-15T14:13:18.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YW3fP7Ry3kx36WV8Uq8FgT`</summary>

```json
{
  "query": "EMNLP 2025 hallucination detection attention outstanding paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e20fc00-b4d1-40bb-90fa-bd8367cbdaa6",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dcea9b0-938b-4ab5-9573-759b5226bcfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 16 · 2026-05-15T14:13:18.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ltf2TxdmyiQigvE1YazKTP`</summary>

```json
{
  "query": "\"Calibrating Verbal Uncertainty as a Linear Feature\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dcea9b0-938b-4ab5-9573-759b5226bcfa",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32fc0d4c-78b2-4a5f-a06b-32b58f332a1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 17 · 2026-05-15T14:13:19.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UTASfM8paHtRBbryMBQ9AX`</summary>

```json
{
  "query": "\"Measuring Chain of Thought Faithfulness by Unlearning\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32fc0d4c-78b2-4a5f-a06b-32b58f332a1e",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ab44aed-ee90-4f4f-a2b4-4393bf435df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 18 · 2026-05-15T14:13:19.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WV1NXZNQ4m3sooDAgX8Cr`</summary>

```json
{
  "query": "hallucination basins arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ab44aed-ee90-4f4f-a2b4-4393bf435df5",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caa468e1-f786-4101-8292-2e0d3d1bb792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 19 · 2026-05-15T14:13:19.440Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018khL5cs8RZ7muf5xMhmkg7`</summary>

```json
{
  "query": "Frequency-Aware Attention hallucination arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa468e1-f786-4101-8292-2e0d3d1bb792",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VWXvvMNPLbQ7sUzQwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c08e19f8-d654-4b8e-85c9-f28c2533996c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er6RZxsYpLvqKPrpLUh6ih",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 10561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 20 · 2026-05-15T14:13:22.857Z_

<details><summary>↩ Tool result · `toolu_014YNpVG4NNwWCT26cjEh6eC`</summary>

```text
Web search results for query: "hallucination detection internal representations temporal dynamics 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"DynHD: Hallucination Detection for Diffusion Large Language Models via Denoising Dynamics Deviation Learning","url":"https://arxiv.org/html/2603.16459"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888v1"},{"title":"[2604.13068] Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models","url":"https://arxiv.org/abs/2604.13068"},{"title":"HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders","url":"https://arxiv.org/html/2604.16430"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection | OpenReview","url":"https://openreview.net/forum?id=QbuBZvwcDZ"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"Mitigating Hallucination in VideoLLMs via Temporal-Aware Activation Engineering","url":"https://openreview.net/pdf?id=7mTECPRtll"},{"title":"Hallucination Detection via Internal States and Structured Reasoning Consistency in Large Language Models","url":"https://arxiv.org/html/2510.11529v1"},{"title":"HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs","url":"https://arxiv.org/html/2601.18753"}]

I found relevant recent research on hallucination detection using internal representations and temporal dynamics. Here's what the web search revealed:

## Key Research Areas

**Temporal Dynamics in Hallucination Detection:**

MIND is an unsupervised detector that models temporal dynamics of hidden states without requiring labels, representing an important advance in this field. Additionally, one approach treats token log-probabilities as a time series, classifying hallucinations based on their temporal dynamics rather than absolute values.

**Phase Transition Perspectives:**

Recent work has adopted a dynamic view of hallucinations. Factual errors emerge when internal representations, propelled by specific high-energy sparse features, abruptly transition from a low-energy "truth attractor" to a persistent, unstable high-energy plateau. This represents the first work leveraging dynamic SAE geometry for general factual hallucination detection.

**Pre-Generation Signals:**

Research studies the temporal dynamics of hallucination-indicative internal representations across 7 autoregressive transformers (117M--7B parameters) using three fact-based datasets, finding that hallucination signals can emerge before generation even begins.

**Decomposed Risk Framework:**

A unified framework decomposes hallucination risk into data-driven and reasoning-driven components, with hallucinations originating from semantic approximation gaps and being amplified by unstable rollout dynamics across decoding steps.

These 2026 papers demonstrate significant progress in understanding hallucinations through the lens of internal representation dynamics and temporal evolution during language model inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e004f3-3a6b-461e-815e-fc589ca5c07c",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "44a03ff0-4135-42d2-b3ea-2d02cca1c6cb",
  "sourceToolAssistantUUID": "37e004f3-3a6b-461e-815e-fc589ca5c07c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T14:13:23.673Z_

<details><summary>↩ Tool result · `toolu_011tXWTKPcvkK43SpkeEYq95`</summary>

```text
Web search results for query: "attention pattern evolution generation hallucination arxiv 2026"

Links: [{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"Detecting Hallucinations in Graph Retrieval-Augmented Generation via Attention Patterns and Semantic Alignment","url":"https://arxiv.org/html/2512.09148"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"[2602.18145] Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention","url":"https://arxiv.org/abs/2602.18145"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2512.05546] Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models","url":"https://arxiv.org/abs/2512.05546"},{"title":"[2512.09148] Detecting Hallucinations in Graph Retrieval-Augmented Generation via Attention Patterns and Semantic Alignment","url":"https://arxiv.org/abs/2512.09148"},{"title":"1 A Survey on Hallucination in Large Language Models:","url":"https://arxiv.org/pdf/2311.05232"},{"title":"A Geometric Taxonomy of Hallucination in LLMs","url":"https://arxiv.org/html/2602.13224v3"},{"title":"Survey of Hallucination in Natural Language Generation","url":"https://arxiv.org/pdf/2202.03629"}]

I found several recent arxiv papers from 2026 related to attention patterns, hallucination, and generation. Here's a summary of the key findings:

## Recent Research on Attention Patterns and Hallucination (2026)

### Attention Dynamics and Hallucination Detection

Researchers have introduced a frequency-aware perspective on attention by analyzing its variation during generation, modeling attention distributions as discrete signals and extracting high-frequency components that reflect rapid local changes in attention, with findings that hallucinated tokens are associated with high-frequency attention energy, reflecting fragmented and unstable grounding behavior.

### Saliency-Based Framework

A gradient-aware diagnostic framework called LVLMs-Saliency quantifies the visual grounding strength of each output token by fusing attention weights with their input gradients, uncovering that hallucinations frequently arise when preceding output tokens exhibit low saliency toward the prediction of the next token, signaling a breakdown in contextual memory retention.

### Graph-Based Knowledge Processing

Researchers introduced two lightweight interpretability metrics: Path Reliance Degree (PRD), which quantifies whether the model disproportionately concentrates attention on shortest-path triples during answer generation, and Semantic Alignment Score (SAS), which measures the degree to which the model's internal token representations align with the retrieved knowledge triples.

### Trajectory Analysis of Generation

Analysis of hidden states reveals that upon the first divergent token, trajectories fork into distinct regions of activation space, with the fork widening monotonically across subsequent steps.

These papers suggest that understanding attention pattern evolution is crucial for explaining and mitigating hallucinations in language model generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df3cdce5-3de9-4434-8432-f920db5f2ea9",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "3f354089-d187-436c-bfdf-8249f0a083db",
  "sourceToolAssistantUUID": "df3cdce5-3de9-4434-8432-f920db5f2ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:13:24.157Z_

<details><summary>↩ Tool result · `toolu_01XJiec6dpDVhoWWxm4wPzvg`</summary>

```text
Web search results for query: "hallucination early detection decoding arxiv 2026"

Links: [{"title":"[2603.05465] HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/abs/2603.05465"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"TDGNet: Hallucination Detection in Diffusion Language ...","url":"https://arxiv.org/pdf/2602.08048"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"}]

I found several recent arXiv papers from 2026 on hallucination early detection and decoding. Here are the most relevant results:

## Key Papers on Early Hallucination Detection

**1. HALP: Detecting Hallucinations in Vision-Language Models (arXiv 2603.05465)**

This paper demonstrates that hallucination risk is detectable pre-generation through probes trained on internal representations, achieving up to 0.93 AUROC on several modern models without requiring decoding. The researchers investigate whether hallucination risk can be predicted before any token is generated by probing a model's internal representations in a single forward pass.

**2. Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (arXiv 2605.05953)**

This work proposes PCNet, a Probabilistic Circuit trained as a density estimator over the LLM residual stream that detects hallucinations as geometric anomalies via exact Negative Log-Likelihood computation. PCNet achieves near-perfect hallucination detection across multiple benchmarks with AUROC reaching up to 99%.

**3. Hallucination as Trajectory Commitment (arXiv 2604.15400)**

This paper presents causal evidence that hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics. The study found that on a tested model, 27 out of 61 prompts (44.3%) showed factual and hallucinated trajectories diverging at the first generated token.

These papers represent cutting-edge research on detecting hallucinations early in the generation process, before full token decoding occurs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6273447-d0b9-4eef-87e3-21e8d44113df",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "5814a57b-fd25-4897-8fa3-044247902dff",
  "sourceToolAssistantUUID": "f6273447-d0b9-4eef-87e3-21e8d44113df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T14:13:24.371Z_

<details><summary>↩ Tool result · `toolu_011dGdGhJUA6sa7TPBPbXTxr`</summary>

```text
Web search results for query: "calibrated uncertainty attention sink LLM 2026"

Links: [{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3744238"},{"title":"LLM Uncertainty Quantification Should Be More Human- ...","url":"https://arxiv.org/pdf/2506.07461"},{"title":"LLM Judge Calibration: Fast Uncertainty Estimation - ByteTrending","url":"https://bytetrending.com/2026/01/02/llm-judge-calibration-fast-uncertainty-estimation/"},{"title":"SelectLLM – Calibrating LLMs for Selective Prediction: Balancing Coverage and Risk | OpenReview","url":"https://openreview.net/forum?id=JJPAy8mvrQ"},{"title":"Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2","url":"https://dl.acm.org/doi/10.1145/3711896.3736569"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"}]

Based on the search results, here's what I found regarding calibrated uncertainty and attention-related work in LLMs for 2026:

## Key Findings

**Calibrated Uncertainty in LLMs:**
The 2025 consensus is to aim for calibrated uncertainty: systems that transparently signal doubt and can safely refuse to answer when unsure, rather than chasing an unrealistic "zero error" goal.

**Attention-Based Methods:**
Recent efforts in probe-based uncertainty estimation focus on curating more informative features, such as attention activation maps. Additionally, Trainable attention-based dependency (TAD) trains a regression model on the conditional dependence between the tokens and applies the predicted factors to improve the estimated uncertainty of the LLM.

**Calibration Research:**
Recent work includes approaches for post-hoc calibration and truth-aligned uncertainty. Truth AnChoring (TAC) is a post-hoc calibration method to remedy uncertainty estimation metrics, by mapping the raw scores to truth-aligned scores.

**Attention Sink Phenomenon:**
While the search results don't directly discuss "attention sink" in the context of calibrated uncertainty, the results do show that calibration behavior is distributed across the network's depth, especially in intermediate layers, rather than being an isolated property of the final output layer.

The field is moving toward more systematic approaches to uncertainty quantification and calibration in 2026, with emphasis on both technical improvements and human-centered evaluation of these systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae3005a0-1c1b-42bd-be67-067853777488",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "99b92181-3238-4598-8ff3-3d11f68268fd",
  "sourceToolAssistantUUID": "ae3005a0-1c1b-42bd-be67-067853777488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T14:13:24.679Z_

<details><summary>↩ Tool result · `toolu_01Ltf2TxdmyiQigvE1YazKTP`</summary>

```text
Web search results for query: ""Calibrating Verbal Uncertainty as a Linear Feature" arxiv"

Links: [{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Revisiting Uncertainty Estimation and Calibration of Large ...","url":"https://arxiv.org/pdf/2505.23854"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"CALIBRATING THE VOICE OF DOUBT: HOW LLMS DI","url":"https://openreview.net/pdf?id=uZ2A0k5liR"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to ...","url":"https://aclanthology.org/2025.emnlp-main.187.pdf"}]

I found the paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" on arXiv. Here are the key findings:

## Overview

This paper addresses how LLMs often adopt an assertive language style even when making false claims, which misleads users and erodes trust.

## Main Findings

The researchers found that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and showed that this has only moderate correlation with the actual "semantic uncertainty" of the model.

## Key Contributions

The mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and they can intervene on verbal uncertainty at inference time and reduce confident hallucinations on short-form answers, achieving an average relative reduction of ~30%.

## Technical Approach

The researchers discovered that verbal uncertainty is mediated by a single direction in representation space, i.e., a linear Verbal Uncertainty Feature (VUF). They propose a method called Mechanistic Uncertainty Calibration (MUC) that steers LLM activations using VUFs to calibrate verbal uncertainty with semantic uncertainty, thereby mitigating hallucinations.

**arXiv ID:** 2503.14477


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32fc0d4c-78b2-4a5f-a06b-32b58f332a1e",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "1d076d74-5211-49e7-8b93-09ff0725676e",
  "sourceToolAssistantUUID": "32fc0d4c-78b2-4a5f-a06b-32b58f332a1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T14:13:25.004Z_

<details><summary>↩ Tool result · `toolu_01YW3fP7Ry3kx36WV8Uq8FgT`</summary>

```text
Web search results for query: "EMNLP 2025 hallucination detection attention outstanding paper"

Links: [{"title":"A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1809/"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"Re-evaluating Hallucination Detection in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1761.pdf"},{"title":"Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.67/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"An Empirical Study on Hallucinations in Embodied Agents ...","url":"https://aclanthology.org/2025.findings-emnlp.1158.pdf"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Unsupervised Hallucination Detection by Inspecting Reasoning Processes - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1124/"},{"title":"Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.631/"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"}]

Based on the search results, I found several notable papers on hallucination detection at EMNLP 2025 that involve attention mechanisms:

## Key Papers on Hallucination Detection with Attention at EMNLP 2025

**Hallucination Detection in LLMs Using Spectral Features of Attention Maps** was published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 24354–24385, Suzhou, China. This work investigates the spectral features of attention maps by interpreting them as adjacency matrices of graph structures, and proposes the LapEigvals method, which utilises the top-k eigenvalues of the Laplacian matrix derived from the attention maps as an input to hallucination detection probes. The approach achieves state-of-the-art hallucination detection performance among attention-based methods.

**A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs** was published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 35712–35731, Suzhou, China. Their strong performance stems from the transformer architecture in their design, in the form of informative features derived from LLM attention maps and logits.

Additional papers at EMNLP 2025 address hallucination detection from other perspectives, including IRIS, an unsupervised hallucination detection framework that leverages internal representations intrinsic to factual correctness by prompting the LLM to carefully verify the truthfulness of a given statement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dcea9b0-938b-4ab5-9573-759b5226bcfa",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "3abdc8e2-8067-4358-82d6-e0129d0b0764",
  "sourceToolAssistantUUID": "6dcea9b0-938b-4ab5-9573-759b5226bcfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T14:13:25.743Z_

<details><summary>↩ Tool result · `toolu_01LhfVVUqHWV1yCpRadPaU96`</summary>

```text
Web search results for query: "online hallucination detection attention LLM 2025 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"[2510.06265] Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/abs/2510.06265"},{"title":"How to Detect Hallucinations in Your LLM Applications","url":"https://www.getmaxim.ai/articles/how-to-detect-hallucinations-in-your-llm-applications/"},{"title":"Hallucination (artificial intelligence) - Wikipedia","url":"https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection | OpenReview","url":"https://openreview.net/forum?id=QbuBZvwcDZ"}]

Based on the search results, here's what the latest research shows about online hallucination detection using attention mechanisms in LLMs for 2025-2026:

## Key Detection Techniques

Techniques such as Cross-Layer Attention Probing (CLAP) train lightweight classifiers on the model's own activations to flag likely hallucinations in real time. The MetaQA framework (ACM 2025) uses metamorphic prompt mutations to detect hallucinations even in closed-source models without relying on token probabilities or external tools.

## Attention-Based Approaches

Recent research has focused on leveraging attention mechanisms for detection. Pre-trained uncertainty quantification heads predict claim-level hallucination by leveraging attention maps and token probability features within the LLM. Additionally, LapEigvals models attention maps as a graph Laplacian using spectral features, attaining superior results with an AUCROC of 88.9% on the TriviaQA dataset.

Neural probe-based methods train lightweight classifiers on intermediate hidden states, offering real-time and lightweight advantages over uncertainty estimation and external knowledge retrieval.

## 2025-2026 Research Consensus

The 2025 consensus is to aim for calibrated uncertainty: systems that transparently signal doubt and can safely refuse to answer when unsure, rather than chasing an unrealistic "zero error" goal. An August 2025 joint safety evaluation by OpenAI and Anthropic shows major labs converging on "Safe Completions" training, evidence that incentive-aligned methods are moving from research to practice.

## Detection Performance

LLM-based self-evaluation detects hallucinations in approximately 60%–75% of outputs depending on prompt design, and ensemble detection models improve accuracy by 10%–15% over single-model approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c61bd9a-2aff-45d1-bc91-9190271603f7",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "9bf4fde0-7a0c-4302-a02d-5c81fa86528e",
  "sourceToolAssistantUUID": "6c61bd9a-2aff-45d1-bc91-9190271603f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T14:13:26.211Z_

<details><summary>↩ Tool result · `toolu_018khL5cs8RZ7muf5xMhmkg7`</summary>

```text
Web search results for query: "Frequency-Aware Attention hallucination arxiv 2026"

Links: [{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145v1"},{"title":"[2602.18145] Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention","url":"https://arxiv.org/abs/2602.18145"},{"title":"[2110.01880] Frequency Aware Face Hallucination Generative Adversarial Network with Semantic Structural Constraint","url":"https://ar5iv.labs.arxiv.org/html/2110.01880"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"[2505.16652] Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding","url":"https://arxiv.org/abs/2505.16652"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://arxiv.org/pdf/2505.16652"},{"title":"A Graph Signal Processing Framework for Hallucination Detection","url":"https://www.arxiv.org/pdf/2510.19117"},{"title":"[2603.02754] Seeing Clearly without Training: Mitigating Hallucinations in Multimodal LLMs for Remote Sensing","url":"https://arxiv.org/abs/2603.02754"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"}]

Based on the web search results, here's what I found about "Frequency-Aware Attention hallucination arxiv 2026":

## Main Research Paper

The primary paper is "Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention," which addresses hallucination detection in LLMs. While existing approaches rely on coarse attention summaries that fail to capture fine-grained instabilities, this work introduces a frequency-aware perspective inspired by signal processing.

## Key Methodology

The approach models attention distributions as discrete signals and extracts high-frequency components that reflect rapid local changes in attention. The analysis reveals that hallucinated tokens are associated with high-frequency attention energy, reflecting fragmented and unstable grounding behavior, upon which the researchers developed a lightweight hallucination detector using these high-frequency attention features.

## Core Insight

The work treats attention weights over context tokens as a discrete temporal signal, where stable grounding corresponds to smooth, slowly varying signals, while instability manifests as rapid local oscillations. Frequency-aware decomposition captures both low-frequency components (global trends) and high-frequency components (sharp spikes and abrupt local changes).

## Results

The frequency-based attention features improve hallucination detection over existing verification-based, internal representation-based, and attention-based baselines across multiple models and tasks.

The paper was published on arXiv on February 20, 2026 (arxiv ID: 2602.18145).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c08e19f8-d654-4b8e-85c9-f28c2533996c",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "0abcaa7e-a27c-4299-a64e-7878e0aed326",
  "sourceToolAssistantUUID": "c08e19f8-d654-4b8e-85c9-f28c2533996c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T14:13:27.012Z_

<details><summary>↩ Tool result · `toolu_01UTASfM8paHtRBbryMBQ9AX`</summary>

```text
Web search results for query: ""Measuring Chain of Thought Faithfulness by Unlearning" arxiv"

Links: [{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"[2502.14829] Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/abs/2502.14829"},{"title":"Measuring Faithfulness of Chains of Thought by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v1"},{"title":"Measuring Faithfulness of Chains of Thought by Unlearning Reasoning Steps - Paper Detail","url":"https://deeplearn.org/arxiv/578536/measuring-faithfulness-of-chains-of-thought-by-unlearning-reasoning-steps"},{"title":"LIE TO ME: HOW FAITHFUL IS CHAIN-OF-THOUGHT REASONING","url":"https://arxiv.org/pdf/2603.22582"},{"title":"[2307.13702] Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2307.13702"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250214829T/abstract"},{"title":"Measuring Faithfulness of Chains of Thought by Unlearning Reasoning Steps | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/measuring-faithfulness-chains-thought-by-unlearning-reasoning"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"}]

I found the paper you're looking for. Here's information about "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps":

## Paper Overview

The paper introduces PFF, a framework for measuring parametric faithfulness of LM reasoning. It proposes Faithfulness by Unlearning Reasoning steps (FUR), an instance of this framework.

## Key Contribution

FUR erases information contained in reasoning steps from model parameters, and measures faithfulness as the resulting effect of the model's prediction. The experiments with four LMs and five multi-hop multi-choice question answering (MCQA) datasets show that FUR is frequently able to precisely change the underlying models' prediction for a given instance by unlearning key steps, indicating when a CoT is parametrically faithful.

## Motivation

When prompted to think step-by-step, language models produce a chain of thought, a sequence of reasoning steps that the model supposedly used to produce its prediction. Despite much work on CoT prompting it is unclear if reasoning verbalized in a CoT is faithful to the models' parametric beliefs.

## Paper Details

- **arXiv ID:** 2502.14829
- **Authors:** Martin Tutek and colleagues
- **Status:** Published at EMNLP 2025

You can access the full paper at: https://arxiv.org/abs/2502.14829


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ab44aed-ee90-4f4f-a2b4-4393bf435df5",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "c37d7d80-b6b4-44d8-a5f9-7eae947a9789",
  "sourceToolAssistantUUID": "3ab44aed-ee90-4f4f-a2b4-4393bf435df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T14:13:27.967Z_

<details><summary>↩ Tool result · `toolu_017WV1NXZNQ4m3sooDAgX8Cr`</summary>

```text
Web search results for query: "hallucination basins arxiv 2026"

Links: [{"title":"[2604.04743] Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/abs/2604.04743"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743v1"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"[2510.06265] Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/abs/2510.06265"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"[2601.07046] Engineering of Hallucination in Generative AI: It's not a Bug, it's a Feature","url":"https://arxiv.org/abs/2601.07046"},{"title":"A Geometric Taxonomy of Hallucination in LLMs","url":"https://arxiv.org/html/2602.13224v3"}]

Based on the search results, I found several relevant arxiv papers from 2026 about hallucination basins:

## Main Paper: "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations"

This paper presents a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space. Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, the researchers find that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap.

Hallucinations arise from a task-dependent geometric collapse, determined by the cardinality of the set of valid answers—factoid tasks with single answers induce a point attractor; generation tasks with many valid outputs form high-dimensional manifolds; misconception tasks create indistinguishable basins.

The paper formalizes this behavior with task-complexity and multi-basin theorems, characterizes basin emergence in L-layer transformers, and shows that geometry-aware steering can reduce hallucination probability without retraining.

## Related Papers

Two other recent papers also explore hallucination basins and attractor dynamics:

- "Hallucination as Trajectory Commitment" presents causal evidence that hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics.

- "Attractor Geometry of Transformer Memory" shows that in hidden-state space of autoregressive generation, learned facts form attractor basins. Conflict is basin competition where working memory disrupts convergence to the correct basin without raising output entropy, while hallucination is basin absence where the hidden state drifts freely when no memorized basin exists.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa468e1-f786-4101-8292-2e0d3d1bb792",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "8d31222f-c5ee-4ad6-8ced-42759b911161",
  "sourceToolAssistantUUID": "caa468e1-f786-4101-8292-2e0d3d1bb792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T14:13:29.284Z_

<details><summary>↩ Tool result · `toolu_01UxMhJe6EDBH5hkREqVsfYW`</summary>

```text
Web search results for query: "token-level hallucination detection probe 2025 2026"

Links: [{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"},{"title":"HalLoc: Token-level Localization of Hallucinations for Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.hallucination-probes.com/"},{"title":"GitHub - mala-lab/HaMI: [NeurIPS 2025] Official implementation for ''Robust Hallucination Detection in LLMs via Adaptive Token Selection'' https://arxiv.org/abs/2504.07863 · GitHub","url":"https://github.com/mala-lab/HaMI"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"Token-Level Self-Consistency for Hallucination Detection","url":"https://aclanthology.org/2025.semeval-1.38.pdf"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/pdf/2504.07863"}]

Based on the search results, here's an overview of token-level hallucination detection probe research from 2025-2026:

## Key Approaches and Methods

Hidden-state probes are linear or neural probes attached to internal representations to predict hallucination probability per token, with nonlinear MLP probes providing superior accuracy and recall under low false positive rate regimes.

The HalluField Framework uses a field-theoretic approach that models each token's semantic stability via free energy and Shannon entropy under temperature perturbations, detecting hallucinations directly on logits without requiring fine-tuning.

HaMI is a novel approach that enables robust detection of hallucinations through adaptive selection and learning of critical tokens by formulating hallucination detection as Multiple Instance learning over token-level representations.

## Recent Advances

A streaming approach presents a cheap, scalable method for real-time identification of hallucinated tokens in long-form generations, targeting entity-level hallucinations rather than claim-level.

Hallucination signals are most detectable at the onset of hallucinated spans, while multi-token reliability estimation aggregates logits from up to the first ten tokens to estimate output reliability.

## Performance and Benchmarks

State-of-the-art methods report F1 improvements of 10–20 points and AUROC gains up to 30 on challenging domains and models.

Real-time and streaming inference is feasible with lightweight probes and attention-based models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e20fc00-b4d1-40bb-90fa-bd8367cbdaa6",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "32a5e77c-518e-45c9-9a6b-660ae82c4f75",
  "sourceToolAssistantUUID": "1e20fc00-b4d1-40bb-90fa-bd8367cbdaa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T14:13:35.495Z_

Now let me run a few more targeted searches to fill in gaps -- specifically for the EMNLP 2025 outstanding papers, and the most directly competing works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32a5e77c-518e-45c9-9a6b-660ae82c4f75",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc88d77a-3e25-473f-94bb-75e4b3927817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5937,
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

_source line 32 · 2026-05-15T14:13:35.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UFrWPDaUay5XPsYdk7NQ6`</summary>

```json
{
  "query": "EMNLP 2025 outstanding paper award winners list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc88d77a-3e25-473f-94bb-75e4b3927817",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b0ddf3c-19fe-42ad-837b-19714534f9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5937,
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

_source line 33 · 2026-05-15T14:13:35.692Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MmQdQJAqJguNusuD4Us8Dw`</summary>

```json
{
  "query": "arxiv 2604.10697 \"Attention Sinks as Internal Signals\" SinkProbe hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b0ddf3c-19fe-42ad-837b-19714534f9a4",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46ee855b-0fb3-408b-b34b-8a503a7371d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5937,
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

_source line 34 · 2026-05-15T14:13:35.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WSpqAx3fFp5FRBWyqjeVRS`</summary>

```json
{
  "query": "SinkTrack 2604.10027 attention sink context anchoring ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46ee855b-0fb3-408b-b34b-8a503a7371d3",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "297ebb3a-b60f-4be4-85bc-345ad2f58a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5937,
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

_source line 35 · 2026-05-15T14:13:36.665Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LSG4CrFk1PVBaeDaFtJn5B`</summary>

```json
{
  "query": "HALT hallucination log-probs time series 2602.02888 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297ebb3a-b60f-4be4-85bc-345ad2f58a3e",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0099ffd-1af5-4814-90dd-f5b9fefe55c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5937,
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

_source line 36 · 2026-05-15T14:13:37.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CEe1GLpUMC2KrGFjFgbQ11`</summary>

```json
{
  "query": "\"Before the First Token\" hallucination signals autoregressive 2604.13068"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0099ffd-1af5-4814-90dd-f5b9fefe55c0",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VXiEKdbhQuK9UsghS2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b1f177d-2a2d-416d-99c1-4d5104b4d1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129qoL98yn6QriMfjCNPPMh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4455,
      "cache_creation_input_tokens": 5937,
      "cache_read_input_tokens": 11602,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4455,
          "output_tokens": 327,
          "cache_read_input_tokens": 11602,
          "cache_creation_input_tokens": 5937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5937,
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

_source line 37 · 2026-05-15T14:13:40.745Z_

<details><summary>↩ Tool result · `toolu_01MmQdQJAqJguNusuD4Us8Dw`</summary>

```text
Web search results for query: "arxiv 2604.10697 "Attention Sinks as Internal Signals" SinkProbe hallucination"

Links: [{"title":"[2604.10697] Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2604.10697"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"When Attention Dynamics Matter: Revealing and Enhancing Core Visual Regions for Hallucination Mitigation in LVLMs","url":"https://arxiv.org/html/2602.15556v1"},{"title":"SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/html/2604.10027"},{"title":"verthinking Causes Hallucination: Tracing Confounder Propagation in Vision Language Models","url":"https://arxiv.org/html/2603.07619"},{"title":"Seeing Clearly by Layer Two: Enhancing Attention Heads to Alleviate Hallucination in LVLMs","url":"https://arxiv.org/html/2411.09968v1"},{"title":"The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity","url":"https://arxiv.org/html/2605.06611"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=4twbqwV4br"}]

Based on the search results, I found the arxiv paper you're looking for:

SinkProbe is a hallucination detection method grounded in the observation that hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation - indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation.

Although sink scores are computed solely from attention maps, the classifier preferentially relies on sinks whose associated value vectors have large norms. Additionally, previous methods implicitly depend on attention sinks by establishing their mathematical relationship to sink scores.

The paper was authored by Jakub Binkowski, Kamil Adamczewski, and Tomasz Kajdanowicz, and was published on April 12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46ee855b-0fb3-408b-b34b-8a503a7371d3",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "9b7129e8-7d56-4352-b950-8e19edc31827",
  "sourceToolAssistantUUID": "46ee855b-0fb3-408b-b34b-8a503a7371d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T14:13:41.539Z_

<details><summary>↩ Tool result · `toolu_015UFrWPDaUay5XPsYdk7NQ6`</summary>

```text
Web search results for query: "EMNLP 2025 outstanding paper award winners list"

Links: [{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"EMNLP 2026 on X: \"🎉 Congratulations to all #EMNLP2025 award winners 🎉 Starting with the ✨Best Paper award ✨: \"Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index\" by Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, and Hannaneh Hajishirzi https://t.co/DKYhylaopF 1/n https://t.co/lrrtlZuyWw\" / X","url":"https://x.com/emnlpmeeting/status/1986922316643651775"},{"title":"Linguistics Doctoral Student, Sasha Boguraev, wins Outstanding Paper Award at EMNLP 2025.>","url":"https://liberalarts.utexas.edu/linguistics/news/linguistics-doctoral-student-sasha-boguraev-wins-outstanding-paper-award-at-emnlp-2025"},{"title":"Freda Shi and colleagues win EMNLP 2025 Outstanding Paper Award for research on LLM meta-linguistic reasoning | Cheriton School of Computer Science | University of Waterloo","url":"https://cs.uwaterloo.ca/news/freda-shi-colleagues-win-emnlp-2025-outstanding-paper-award-research-llm-meta-linguistic-reasoning"},{"title":"EMNLP 2025 on X: \"Thanks again all for a wonderful #EMNLP2025! For future reference, you can now find all accepted papers, award winners, and outstanding reviewers, area chairs, and senior area chairs on the conference website: https://t.co/dMWGwPej05\" / X","url":"https://x.com/emnlpmeeting/status/1997739138695778793"},{"title":"Columbia Electrical Engineering Students Earn Senior Area ...","url":"https://www.ee.columbia.edu/news/columbia-electrical-engineering-students-earn-senior-area-chair-highlight-emnlp-2025"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Best Paper Award MRL 2025 WS at EMNLP | Universität des Saarlandes","url":"https://www.uni-saarland.de/en/department/lst/news/best-paper-award-mrl-2025-ws-at-emnlp-40784.html"},{"title":"EMNLP 2025 Highlights. I just got back from EMNLP 2025 in… | by Itay Nakash | Medium","url":"https://medium.com/@itaynakash/emnlp-2025-highlights-1d2bca37cc7a"},{"title":"🏆 EMNLP 2025 Outstanding Paper Award - Nick Clark","url":"https://nicholasclark.org/media/emnlp-outstanding-paper-2025"}]

Based on the search results, I found information about some EMNLP 2025 award winners:

## Outstanding Paper Awards

Professor Freda Shi and her collaborators Changbing Yang, Franklin Ma and Jian Zhu from the University of British Columbia received an Outstanding Paper Award at EMNLP 2025 for their paper "LingGym: How Far Are LLMs from Thinking Like Field Linguists?"

Sasha Boguraev, a doctoral student, won an Outstanding Paper Award at EMNLP 2025.

## Best Paper Award

"Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index" by Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, and Hannaneh Hajishirzi won the Best Paper award.

## Notable Papers

The Senior Area Chairs highlighted 35 papers as particularly noteworthy, including papers on prompt-agnostic fine-tuning, linguistic constructions, human-AI alignment, unified translation frameworks, and reducing hallucinations in language models.

For a complete list of all award winners, the conference website contains all accepted papers, award winners, and outstanding reviewers, area chairs, and senior area chairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b0ddf3c-19fe-42ad-837b-19714534f9a4",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "22fd27d7-c5a6-4ea2-93f5-0d9c223252f1",
  "sourceToolAssistantUUID": "2b0ddf3c-19fe-42ad-837b-19714534f9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T14:13:42.835Z_

<details><summary>↩ Tool result · `toolu_01WSpqAx3fFp5FRBWyqjeVRS`</summary>

```text
Web search results for query: "SinkTrack 2604.10027 attention sink context anchoring ICLR 2026"

Links: [{"title":"[2604.10027] SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/abs/2604.10027"},{"title":"ICLR Poster SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://iclr.cc/virtual/2026/poster/10010470"},{"title":"SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/html/2604.10027"},{"title":"GitHub - 67L1/SinkTrack: [ICLR'26] SinkTrack: Attention Sink based Context Anchoring for Large Language Models · GitHub","url":"https://github.com/67L1/SinkTrack"},{"title":"SinkTrack: Attention Sink based Context Anchoring for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Gg1aPETCL6"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.10027"},{"title":"SINKTRACK: ATTENTION SINK BASED CONTEXT ...","url":"https://openreview.net/pdf?id=Gg1aPETCL6"},{"title":"Guikun Chen - Homepage","url":"https://guikunchen.github.io/"},{"title":"Papers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SinkTrack%3A-Attention-Sink-based-Context-Anchoring-Liu-Chen/22be224e3f8419bec45bb8abe4d753ed6ad83712"},{"title":"When Attention Sink Emerges in Language Models: An Empirical View | OpenReview","url":"https://openreview.net/forum?id=78Nn4QJTEN"}]

Based on the search results, here's what I found about SinkTrack (arXiv:2604.10027):

## Overview

SinkTrack is a paper submitted on April 11, 2026, authored by Xu Liu, Guikun Chen, and Wenguan Wang, and it was published as a conference paper at ICLR 2026.

## Problem and Approach

Large language models suffer from hallucination and context forgetting, with attention drift being a primary cause where LLMs' focus shifts towards newly generated tokens and away from the initial input context. 

The method leverages the attention sink -- the tendency to consistently allocate high attention to the very first token (i.e., &lt;BOS>) of a sequence. SinkTrack treats &lt;BOS> as an information anchor and injects key contextual features (such as those derived from the input image or instruction) into its representation.

## Key Features

SinkTrack is training-free, plug-and-play, and introduces negligible inference overhead.

## Performance Results

Experiments demonstrate that SinkTrack mitigates hallucination and context forgetting across both textual (e.g., +21.6% on SQuAD2.0 with Llama3.1-8B-Instruct) and multi-modal (e.g., +22.8% on M3CoT with Qwen2.5-VL-7B-Instruct) tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "297ebb3a-b60f-4be4-85bc-345ad2f58a3e",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "37d2a433-91dc-4199-9b1b-7ca7d4fab40f",
  "sourceToolAssistantUUID": "297ebb3a-b60f-4be4-85bc-345ad2f58a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T14:13:43.769Z_

<details><summary>↩ Tool result · `toolu_01LSG4CrFk1PVBaeDaFtJn5B`</summary>

```text
Web search results for query: "HALT hallucination log-probs time series 2602.02888 arxiv"

Links: [{"title":"[2602.02888] HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/abs/2602.02888"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://www.arxiv.org/pdf/2602.02888"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888"},{"title":"(PDF) HALT: Hallucination Assessment via Log-probs as Time series","url":"https://www.researchgate.net/publication/400415154_HALT_Hallucination_Assessment_via_Log-probs_as_Time_series"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series | OpenReview","url":"https://openreview.net/forum?id=l4WFDcw3Yy"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"HALT-RAG: A Task-Adaptable Framework for Hallucination Detection with Calibrated NLI Ensembles and Abstention","url":"https://arxiv.org/html/2509.07475"},{"title":"HaluMem: Evaluating Hallucinations in Memory Systems of Agents","url":"https://arxiv.org/pdf/2511.03506"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"}]

Based on the search results, here's information about the paper on arxiv 2602.02888:

## HALT: Hallucination Assessment via Log-probs as Time series

HALT (Hallucination Assessment via Log-probs as Time series) is a lightweight hallucination detector that leverages only the top-20 token log-probabilities from LLM generations as a time series.

**Key Technical Features:**

HALT uses a gated recurrent unit model combined with entropy-based features to learn model calibration bias, providing an extremely efficient alternative to large encoders.

**Advantages Over Other Approaches:**

Unlike white-box approaches, HALT does not require access to hidden states or attention maps, relying only on output log-probabilities. Unlike black-box approaches, it operates on log-probs rather than surface-form text, which enables stronger domain generalization and compatibility with proprietary LLMs without requiring access to internal weights.

**Benchmark:**

The authors introduce HUB (Hallucination detection Unified Benchmark), which consolidates prior datasets into ten capabilities.

The paper was submitted on February 2, 2026 by Ahmad Shapiro, Karan Taneja, and Ashok Goel.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0099ffd-1af5-4814-90dd-f5b9fefe55c0",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "65a2c480-00cd-408d-be84-7da66ffbae9d",
  "sourceToolAssistantUUID": "b0099ffd-1af5-4814-90dd-f5b9fefe55c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T14:13:44.747Z_

<details><summary>↩ Tool result · `toolu_01CEe1GLpUMC2KrGFjFgbQ11`</summary>

```text
Web search results for query: ""Before the First Token" hallucination signals autoregressive 2604.13068"

Links: [{"title":"[2604.13068] Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models","url":"https://arxiv.org/abs/2604.13068"},{"title":"Before the First Token: Scale-dependent Emergence of Hallucination Signals in Autoregressive Language Models by Dip Roy, Sanjay Kumar Singh, Rajiv Misra, Anisha Roy :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6465859"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"Weakly Supervised Distillation of Hallucination Signals into Transformer Representations","url":"https://arxiv.org/html/2604.06277"},{"title":"First Hallucination Tokens Are Different from Conditional Ones","url":"https://arxiv.org/html/2507.20836v4"},{"title":"[2507.20836] First Hallucination Tokens Are Different from Conditional Ones","url":"https://arxiv.org/abs/2507.20836"},{"title":"Oscar: Orchestrated Self-verification and Cross-path Refinement","url":"https://arxiv.org/html/2604.01624"},{"title":"First Hallucination Tokens Are Different from Conditional Ones","url":"https://www.emergentmind.com/papers/2507.20836"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding","url":"https://arxiv.org/html/2601.21969"}]

Based on the search results, here's what I found about the paper "Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models" (arXiv:2604.13068):

## Overview

The paper addresses when large language models decide to hallucinate, despite serious consequences in healthcare, law, and finance.

## Key Research Findings

The researchers studied the temporal dynamics of hallucination-indicative internal representations across 7 autoregressive transformers (117M--7B parameters) using three fact-based datasets (TriviaQA, Simple Facts, Biography; 552 labeled examples).

The study identified a critical scale-dependent threshold for hallucination signals:

- Models below 400M parameters show chance-level probe accuracy at every generation position (AUC = 0.48--0.67), indicating no reliable factuality signal

- Above ~1B parameters, a qualitatively different regime emerges where peak detectability occurs at position zero -- before any tokens are generated -- then declines during generation

## Authors and Submission

The paper was submitted on March 20, 2026, with authors Dip Roy, Rajiv Misra, Sanjay Kumar Singh, and Anisha Roy.

The findings suggest that larger language models show a remarkable behavior where signals about whether they will hallucinate peak before any generation actually occurs, representing a significant discovery about the internal dynamics of hallucination in transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b1f177d-2a2d-416d-99c1-4d5104b4d1bc",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "441cb6f0-7826-42b3-9c15-d47466dbca95",
  "sourceToolAssistantUUID": "3b1f177d-2a2d-416d-99c1-4d5104b4d1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T14:13:47.588Z_

Let me search for a few more details on the EMNLP 2025 outstanding papers and the specific paper comparing attention-based vs hidden-state-based approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "441cb6f0-7826-42b3-9c15-d47466dbca95",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VYrKWqxhbuEvcRzaeN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44cd3120-5d66-4f3a-8484-dcb389d322af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YE6nvifewd7mKAEAHN8Wqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 17539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9246,
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

_source line 43 · 2026-05-15T14:13:48.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ttw58339ejaykgm4WDg8TE`</summary>

```json
{
  "query": "EMNLP 2025 outstanding paper \"Calibrating Verbal Uncertainty\" OR \"Measuring Chain of Thought Faithfulness\" award"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44cd3120-5d66-4f3a-8484-dcb389d322af",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VYrKWqxhbuEvcRzaeN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41dad4f5-e62e-4fe0-a6d3-9c04b2d33269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YE6nvifewd7mKAEAHN8Wqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 17539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9246,
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

_source line 44 · 2026-05-15T14:13:49.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QT6epdBFTWx3hGpfjCmX1z`</summary>

```json
{
  "query": "attention-based vs hidden-state hallucination detection comparison probe LLM arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41dad4f5-e62e-4fe0-a6d3-9c04b2d33269",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VYrKWqxhbuEvcRzaeN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97adf1da-c435-4c1a-b0bb-6ffe0b0a996c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YE6nvifewd7mKAEAHN8Wqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 17539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9246,
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

_source line 45 · 2026-05-15T14:13:50.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013j5KQ14GPQxx3TK3epytkp`</summary>

```json
{
  "query": "\"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs\" 2504.10063"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97adf1da-c435-4c1a-b0bb-6ffe0b0a996c",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VYrKWqxhbuEvcRzaeN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ce24340-179f-4688-ba1b-a5c2c29898cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YE6nvifewd7mKAEAHN8Wqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 17539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9246,
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

_source line 46 · 2026-05-15T14:13:51.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNVHufzCJc7nYFBvi5qCCe`</summary>

```json
{
  "query": "HalluSAE sparse auto-encoders hallucination detection 2604.16430"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ce24340-179f-4688-ba1b-a5c2c29898cc",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VYrKWqxhbuEvcRzaeN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c43d3f1e-1aa0-4c85-bb4a-daa0abeff33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YE6nvifewd7mKAEAHN8Wqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9246,
      "cache_read_input_tokens": 17539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9246,
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

_source line 47 · 2026-05-15T14:13:54.470Z_

<details><summary>↩ Tool result · `toolu_01Ttw58339ejaykgm4WDg8TE`</summary>

```text
Web search results for query: "EMNLP 2025 outstanding paper "Calibrating Verbal Uncertainty" OR "Measuring Chain of Thought Faithfulness" award"

Links: [{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.504/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to ...","url":"https://aclanthology.org/2025.emnlp-main.187.pdf"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"},{"title":"Faithful Natural Language Uncertainty Expression in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1505.pdf"},{"title":"EMNLP 2025 Highlights. I just got back from EMNLP 2025 in… | by Itay Nakash | Medium","url":"https://medium.com/@itaynakash/emnlp-2025-highlights-1d2bca37cc7a"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Seeing is Believing, but How Much? A Comprehensive ...","url":"https://aclanthology.org/2025.emnlp-main.74.pdf"}]

Based on the search results, I found information about both papers at EMNLP 2025:

"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps" by Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, and Yonatan Belinkov won the "Outstanding paper" award at EMNLP 2025. This paper tackles the 'faithfulness' of CoT (chain of thought) by testing whether we can actually trust the reasoning LLMs write in their CoT using methods of unlearning on the reasoning steps information.

The other paper you mentioned, "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda, was also presented at the conference, but it was not listed as winning the outstanding paper award.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41dad4f5-e62e-4fe0-a6d3-9c04b2d33269",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "409b9ca6-fc38-44c6-af03-2f08ce144daf",
  "sourceToolAssistantUUID": "41dad4f5-e62e-4fe0-a6d3-9c04b2d33269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T14:13:56.177Z_

<details><summary>↩ Tool result · `toolu_013j5KQ14GPQxx3TK3epytkp`</summary>

```text
Web search results for query: ""Hallucination Detection in LLMs with Topological Divergence on Attention Graphs" 2504.10063"

Links: [{"title":"[2504.10063] Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/abs/2504.10063"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v3"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"},{"title":"Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v1"},{"title":"[Literature Review] Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-via-topological-divergence-on-attention-graphs"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://openreview.net/pdf?id=cJ0KbB0U7Q"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"Probabilistic distances-based hallucination detection in LLMs with RAG","url":"https://arxiv.org/html/2506.09886"},{"title":"HalluZig: Hallucination Detection using Zigzag Persistence","url":"https://arxiv.org/html/2601.01552"},{"title":"Hallucination Detection in LLMs with Topological Divergence on ...","url":"https://www.semanticscholar.org/paper/1ec4be9cd511fc87e66e15233c16fa177c10aa86"}]

I found the research paper you're looking for. Here's what I found:

## Paper Overview

The paper "Hallucination Detection in LLMs with Topological Divergence on Attention Graphs" addresses the critical challenge of hallucination—generating factually incorrect content—in large language models.

## Key Contribution

The researchers introduce TOHA, a TOpology-based HAllucination detector in the RAG setting, which leverages a topological divergence metric to quantify the structural properties of graphs induced by attention matrices.

## Main Findings

Examining the topological divergence between prompt and response subgraphs reveals consistent patterns: higher divergence values in specific attention heads correlate with hallucinated outputs, independent of the dataset.

## Results

Extensive experiments—including evaluation on question answering and summarization tasks—show that the approach achieves state-of-the-art or competitive results on several benchmarks while requiring minimal annotated data and computational resources.

The paper was published on arXiv (arXiv:2504.10063) on April 14, 2025, and has authors including Alexandra Bazarova and 12 other collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ce24340-179f-4688-ba1b-a5c2c29898cc",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "43a69793-2cab-4bec-ac56-3ec815068c5b",
  "sourceToolAssistantUUID": "3ce24340-179f-4688-ba1b-a5c2c29898cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T14:13:58.467Z_

<details><summary>↩ Tool result · `toolu_01QT6epdBFTWx3hGpfjCmX1z`</summary>

```text
Web search results for query: "attention-based vs hidden-state hallucination detection comparison probe LLM arxiv 2025 2026"

Links: [{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Detection of Hallucinations Based on the Internal States of Large Language Models | Automatic Documentation and Mathematical Linguistics | Springer Nature Link","url":"https://link.springer.com/article/10.3103/S0005105525701456"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"HIVE: Hidden-Evidence Verification for Hallucination Detection in Diffusion Large Language Models","url":"https://arxiv.org/html/2604.26139"},{"title":"AggTruth: Contextual Hallucination Detection using ...","url":"https://arxiv.org/pdf/2506.18628"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063"},{"title":"arXiv:2506.09886v1 [cs.CL] 11 Jun 2025","url":"https://arxiv.org/pdf/2506.09886"}]

I found several relevant research papers comparing attention-based and hidden-state-based approaches for hallucination detection in LLMs from recent arXiv papers (2025-2026). Here are the key findings:

## Comparison of Attention-Based vs. Hidden-State Methods

Unlike hidden state-based approaches, attention-based methods are less prone to overfitting to the training dataset, resulting in a higher AUCROC on out-of-domain target datasets.

### Specific Methods

**Hidden-State Based Probes:**
Linear and MLP-based probes can predict hallucinations using hidden states before or during generation, often achieving strong AUC scores across various tasks. Notable hidden-state methods include SAPLMA, which demonstrated that one could predict the correctness of generated text straight from LLM's hidden states.

**Attention-Based Methods:**
LapEigvals is an attention-based method that leverages the spectral properties of LLM attention maps by interpreting attention maps as weighted adjacency matrices of directed graphs, computing the corresponding graph Laplacian matrix and extracting its top-k eigenvalues to quantify disruptions or bottlenecks in the model's internal information flow, which correlate with hallucinations.

A frequency-aware characterization of attention variation serves as an intrinsic signal for hallucination detection, showing that hallucinated generation is associated with high-frequency variation in attention patterns.

### Performance Trade-offs

The AggTruth Sum method is the most stable and robust approach that resulted in the lowest overall gap across all LLMs examined and tasks, outperforming baselines on the majority of datasets, and calculating the sum of the attention scores is the fastest method.

The ability of probes to generalize to more complex settings, such as open-ended long-form generation, remains unproven.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97adf1da-c435-4c1a-b0bb-6ffe0b0a996c",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "4057f9c3-bc5f-4e7d-a7f6-5ea9acfe2a28",
  "sourceToolAssistantUUID": "97adf1da-c435-4c1a-b0bb-6ffe0b0a996c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T14:13:59.958Z_

<details><summary>↩ Tool result · `toolu_01QNVHufzCJc7nYFBvi5qCCe`</summary>

```text
Web search results for query: "HalluSAE sparse auto-encoders hallucination detection 2604.16430"

Links: [{"title":"[2604.16430] HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders","url":"https://arxiv.org/abs/2604.16430"},{"title":"HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders","url":"https://arxiv.org/html/2604.16430"},{"title":"awesome-hallucination-detection/README.md at main · EdinburghNLP/awesome-hallucination-detection","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection/blob/main/README.md"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"[2505.16146] Steering LVLMs via Sparse Autoencoder for Hallucination Mitigation","url":"https://arxiv.org/abs/2505.16146"},{"title":"HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models","url":"https://arxiv.org/html/2604.19300v1"},{"title":"HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration","url":"https://arxiv.org/html/2512.03345v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Diving into Mitigating Hallucinations from a Vision ...","url":"https://aclanthology.org/2025.findings-emnlp.936.pdf"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"}]

Based on the search results, here's what I found about HalluSAE:

## Overview

HalluSAE is a framework for detecting hallucinations in Large Language Models via Sparse Auto-Encoders that models hallucination as a critical shift in the model's latent dynamics.

## Key Approach

The framework takes a phase transition-inspired approach that models hallucinations as critical shifts in the model's latent dynamics, by modeling the generation process as a trajectory through a potential energy landscape to identify critical transition zones and attributes factual errors to specific high-energy sparse features.

## Methodology

The approach consists of three stages: (1) Potential Energy Empowered Phase Zone Localization via sparse autoencoders and a geometric potential energy metric; (2) Hallucination-related Sparse Feature Attribution using contrastive logit attribution; and (3) Probing-based Causal Hallucination Detection.

## Performance

Extensive experiments on Gemma-2-9B demonstrate that HalluSAE achieves state-of-the-art hallucination detection performance. Additionally, the method achieves new state-of-the-art results on in-distribution (HaluEval) tasks, and out-of-distribution (TriviaQA) benchmarks.

## Authors

The paper was authored by Boshui Chen, Zhaoxin Fan, Ke Wang, Zhiying Leng, Faguo Wu, Hongwei Zheng, Yifan Sun, and Wenjun Wu.

The paper was submitted to arXiv on April 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c43d3f1e-1aa0-4c85-bb4a-daa0abeff33c",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "db970052-abb2-40b3-aab6-54ad15982792",
  "sourceToolAssistantUUID": "c43d3f1e-1aa0-4c85-bb4a-daa0abeff33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T14:14:03.653Z_

Now let me get the EMNLP 2025 awards page directly for clarity, and search for two more relevant items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db970052-abb2-40b3-aab6-54ad15982792",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VZyMiJX1CqyGn7aX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c8e6194-da16-4aea-8eb4-52bb802c3428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XmLu8XJj3o9knP4sVqoLR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3876,
      "cache_read_input_tokens": 26785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3876,
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

_source line 52 · 2026-05-15T14:14:04.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lg6eZYbrQMNsaCrJeXaibU`</summary>

```json
{
  "query": "site:2025.emnlp.org awards outstanding paper list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8e6194-da16-4aea-8eb4-52bb802c3428",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VZyMiJX1CqyGn7aX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b421b388-d19a-42d2-95bb-3b9c6dd4f810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XmLu8XJj3o9knP4sVqoLR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3876,
      "cache_read_input_tokens": 26785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3876,
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

_source line 53 · 2026-05-15T14:14:05.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UerzWFFJWq7guSjkNaMMnP`</summary>

```json
{
  "query": "\"Shadows in the Attention\" contextual perturbation representation drift hallucination 2505.16894"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b421b388-d19a-42d2-95bb-3b9c6dd4f810",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VZyMiJX1CqyGn7aX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cfcd62d-e3bc-4e21-b038-d322414186ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XmLu8XJj3o9knP4sVqoLR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3876,
      "cache_read_input_tokens": 26785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3876,
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

_source line 54 · 2026-05-15T14:14:05.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L39dRCAdVHT59RZ5tP2Byv`</summary>

```json
{
  "query": "MIND unsupervised hallucination detector temporal dynamics hidden states 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cfcd62d-e3bc-4e21-b038-d322414186ac",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VZyMiJX1CqyGn7aX8B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9b1f0bb-7160-4e2d-8c30-32cc532a8fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XmLu8XJj3o9knP4sVqoLR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3876,
      "cache_read_input_tokens": 26785,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3876
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 26785,
          "cache_creation_input_tokens": 3876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3876,
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

_source line 55 · 2026-05-15T14:14:09.552Z_

<details><summary>↩ Tool result · `toolu_01Lg6eZYbrQMNsaCrJeXaibU`</summary>

```text
Web search results for query: "site:2025.emnlp.org awards outstanding paper list"

Links: [{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"Keynotes - EMNLP 2025","url":"https://2025.emnlp.org/program/keynotes/"},{"title":"Panel - EMNLP 2025","url":"https://2025.emnlp.org/program/panel/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Conference Overview - EMNLP 2025","url":"https://2025.emnlp.org/program/"},{"title":"Accepted System Demonstrations Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/demo_papers/"},{"title":"Call for Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/industry_track/"},{"title":"Accepted TACL Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/tacl_papers/"}]

Based on the search results from the EMNLP 2025 awards page, I found information about the outstanding papers:

The Senior Area Chairs highlighted the following 35 papers as particularly noteworthy, including:

1. PAFT: Prompt-Agnostic Fine-Tuning
2. Constructions are Revealed in Word Distributions
3. To Mask or to Mirror: Human-AI Alignment in Collective Reasoning
4. Whisper-UT: A Unified Translation Framework for Speech and Text
5. Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations

A special committee, with assignments based on reviewer expertise, produced 92 reviews and selected four best paper nominations, from which the final awardees were chosen.

The Best Paper Committee was chaired by Owen Rambow (Stony Brook University) and Mirella Lapata (University of Edinburgh).

For the complete list of all 35 outstanding papers, you can visit the awards page directly at https://2025.emnlp.org/program/awards/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b421b388-d19a-42d2-95bb-3b9c6dd4f810",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "099f00d6-2c03-45b2-8203-19147126b4e6",
  "sourceToolAssistantUUID": "b421b388-d19a-42d2-95bb-3b9c6dd4f810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T14:14:12.423Z_

<details><summary>↩ Tool result · `toolu_01L39dRCAdVHT59RZ5tP2Byv`</summary>

```text
Web search results for query: "MIND unsupervised hallucination detector temporal dynamics hidden states 2026"

Links: [{"title":"MIND: Unsupervised Hallucination Detection Framework ...","url":"https://github.com/oneal2000/MIND"},{"title":"Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models","url":"https://arxiv.org/html/2403.06448v1"},{"title":"[2403.06448] Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models","url":"https://arxiv.org/abs/2403.06448"},{"title":"Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384209997_Unsupervised_Real-Time_Hallucination_Detection_based_on_the_Internal_States_of_Large_Language_Models"},{"title":"Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.854/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"[Literature Review] Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models","url":"https://www.themoonlight.io/en/review/unsupervised-real-time-hallucination-detection-based-on-the-internal-states-of-large-language-models"},{"title":"[PDF] Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Real-Time-Hallucination-Detection-on-Su-Wang/411b725522e2747e890ba5acfbf43d22f759c00a"},{"title":"[2403.06448v2] Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models","url":"https://arxiv.org/abs/2403.06448v2"},{"title":"Detecting Hallucinations in Large Language Model ...","url":"https://www.rivas.ai/pdfs/quevedo2024hallucinations.pdf"}]

Based on the search results, I found comprehensive information about MIND, the unsupervised hallucination detector framework:

## MIND: Unsupervised Hallucination Detection Framework

MIND is an unsupervised training framework for real-time hallucination detection based on the internal states of LLM. MIND stands for "Modeling of INternal states for hallucination Detection" and detects hallucinations in large language models in real-time, without needing manual labels.

### Key Characteristics

MIND is unsupervised, directly extracting pseudo-training data from Wikipedia without requiring any manual annotation for the training of the hallucination detector. The framework is real-time and designed to reduce computational overhead and detection latency, using a simple multi-layer perceptron model built upon the contextual embeddings of each token in LLM's inference process.

### Hidden States and Internal Dynamics

HELM (the accompanying benchmark) provides contextualized embeddings, self-attentions and hidden-layer activations recorded in the inference process of each LLM, which serve as snapshots of each LLM's internal states during their inference process. The framework uses the internal states of LLMs (the contextualized embeddings of tokens) during text generation to detect hallucinations.

### Associated Benchmark

HELM is a hallucination detection benchmark featuring text from six LLMs and contains the internal states of each LLM during the text generation process. The paper was published in the Findings of the Association for Computational Linguistics: ACL 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9b1f0bb-7160-4e2d-8c30-32cc532a8fa0",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "8967b075-1ccd-4e3b-ae04-fda0d8a0b432",
  "sourceToolAssistantUUID": "d9b1f0bb-7160-4e2d-8c30-32cc532a8fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T14:14:12.555Z_

<details><summary>↩ Tool result · `toolu_01UerzWFFJWq7guSjkNaMMnP`</summary>

```text
Web search results for query: ""Shadows in the Attention" contextual perturbation representation drift hallucination 2505.16894"

Links: [{"title":"[2505.16894] Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/abs/2505.16894"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894v1"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-4088-4_32"},{"title":"Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation","url":"https://arxiv.org/html/2604.10071"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://arxiv.org/pdf/2505.16652"},{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding","url":"https://arxiv.org/html/2505.16652v1"},{"title":"[2505.21472] Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration","url":"https://arxiv.org/abs/2505.21472"},{"title":"More Thinking, Less Seeing? Assessing Amplified Hallucination in Multimodal Reasoning Models","url":"https://arxiv.org/html/2505.21523v2"}]

Based on the search results, I found the paper you're looking for. Here's information about it:

## "Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs"

This paper presents the first systematic study linking hallucination incidence to internal-state drift induced by incremental context injection.

**Methodology:**
The researchers construct two 16-round "titration" tracks per question using TruthfulQA: one appends relevant but partially flawed snippets, the other injects deliberately misleading content. They track overt hallucination rates across six open-source LLMs with a tri-perspective detector and covert dynamics via cosine, entropy, JS and Spearman drifts of hidden states and attention maps.

**Key Findings:**
The results reveal (1) monotonic growth of hallucination frequency and representation drift that plateaus after 5-7 rounds; (2) relevant context drives deeper semantic assimilation, producing high-confidence "self-consistent" hallucinations, whereas irrelevant context induces topic-drift errors anchored by attention re-routing; and (3) convergence of JS-Drift (~0.69) and Spearman-Drift (~0) marks an "attention-locking" threshold beyond which hallucinations solidify and become resistant to correction.

These findings supply empirical foundations for intrinsic hallucination prediction and context-aware mitigation mechanisms.

The paper was submitted to arXiv on May 22, 2025, with paper ID 2505.16894.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cfcd62d-e3bc-4e21-b038-d322414186ac",
  "isSidechain": true,
  "promptId": "c7ba2d71-5479-4065-8e6b-563fda093afd",
  "agentId": "a3d1af933f509dd09",
  "type": "user",
  "uuid": "dcd08c37-8f50-4aa4-ac47-2fdc61bcc9ec",
  "sourceToolAssistantUUID": "1cfcd62d-e3bc-4e21-b038-d322414186ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-15T14:15:32.352Z_

Here is my comprehensive report on competing and concurrent work relevant to the "SinkWatch" paper idea.

---

## Competing and Concurrent Work for SinkWatch

### CRITICAL DIRECT COMPETITORS

**1. SinkProbe -- "Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models" (arXiv:2604.10697, April 2026)**
This is the most directly competing paper. SinkProbe proposes hallucination detection grounded in the observation that hallucinations are entangled with attention sinks -- tokens that accumulate disproportionate attention mass during generation. It identifies a transition from distributed, input-grounded attention to compressed, prior-dominated computation. Although sink scores are computed solely from attention maps, the classifier preferentially relies on sinks whose associated value vectors have large norms. This paper also mathematically relates previous methods to attention sink scores. Authors: Binkowski, Adamczewski, Kajdanowicz.
- [SinkProbe paper](https://arxiv.org/abs/2604.10697)

**2. SinkTrack -- "SinkTrack: Attention Sink based Context Anchoring for Large Language Models" (arXiv:2604.10027, ICLR 2026)**
Published at ICLR 2026. Identifies "attention drift" where LLMs progressively concentrate attention on recent tokens while attention to initial tokens decays -- a primary cause of hallucination and context forgetting. SinkTrack treats &lt;BOS> as an information anchor and injects key contextual features into its representation. Training-free and plug-and-play. Results: +21.6% on SQuAD2.0, +22.8% on M3CoT.
- [SinkTrack paper](https://arxiv.org/abs/2604.10027)
- [ICLR 2026 poster](https://iclr.cc/virtual/2026/poster/10010470)

**3. "Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention" (arXiv:2602.18145, February 2026)**
Models attention distributions as discrete signals and extracts high-frequency components reflecting rapid local changes. Hallucinated tokens are associated with high-frequency attention energy, reflecting fragmented and unstable grounding behavior. This is essentially a temporal/signal-processing view of attention dynamics during generation -- directly overlapping with SinkWatch's concept.
- [Frequency-Aware Attention paper](https://arxiv.org/abs/2602.18145)

**4. "Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation" (arXiv:2604.10098, April 2026)**
Comprehensive survey of 180+ studies on the attention sink phenomenon, covering its relationship to hallucination. Any reviewer will check if SinkWatch cites this.
- [Survey paper](https://arxiv.org/html/2604.10098)

---

### TEMPORAL DYNAMICS OF INTERNAL REPRESENTATIONS

**5. HALT -- "Hallucination Assessment via Log-probs as Time series" (arXiv:2602.02888, February 2026)**
Treats token log-probabilities as a time series and classifies hallucinations based on temporal dynamics rather than absolute values. Uses a GRU model with entropy-based features. Does not require access to hidden states or attention maps. Introduces the HUB benchmark.
- [HALT paper](https://arxiv.org/abs/2602.02888)

**6. "Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models" (arXiv:2604.13068, April 2026)**
Studies temporal dynamics of hallucination-indicative internal representations across 7 transformers (117M--7B). Finds a critical scale-dependent threshold: below 400M parameters, no reliable signal; above ~1B, peak detectability occurs at position zero (before any tokens are generated), then declines during generation.
- [Before the First Token paper](https://arxiv.org/abs/2604.13068)

**7. "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation" (arXiv:2604.15400, April 2026)**
Provides causal evidence that hallucination is an early trajectory commitment governed by asymmetric attractor dynamics. Factual and hallucinated trajectories diverge at the first generated token in 44.3% of prompts tested.
- [Trajectory Commitment paper](https://arxiv.org/abs/2604.15400)

**8. "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations" (arXiv:2604.04743, April 2026)**
Models hallucinations as task-dependent basin structures in latent space using dynamical systems theory. Factoid tasks with single answers induce a point attractor; generation tasks form high-dimensional manifolds; misconception tasks create indistinguishable basins. Shows geometry-aware steering can reduce hallucination without retraining.
- [Hallucination Basins paper](https://arxiv.org/abs/2604.04743)

**9. "Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs" (arXiv:2505.16894, May 2025)**
First systematic study linking hallucination to internal-state drift induced by incremental context injection. Tracks hidden states AND attention maps across generation rounds. Finds an "attention-locking" threshold (JS-Drift ~0.69, Spearman-Drift ~0) beyond which hallucinations solidify and become resistant to correction. This directly compares attention-based vs. hidden-state temporal signals.
- [Shadows in the Attention paper](https://arxiv.org/abs/2505.16894)

---

### ATTENTION-BASED HALLUCINATION DETECTION (NON-TEMPORAL)

**10. "Hallucination Detection in LLMs Using Spectral Features of Attention Maps" (EMNLP 2025)**
LapEigvals method: interprets attention maps as adjacency matrices, computes Laplacian eigenvalues as hallucination features. State-of-the-art among attention-based methods. Key finding: attention-based methods are less prone to overfitting than hidden-state probes, with higher out-of-domain AUCROC.
- [LapEigvals / Spectral Features paper](https://aclanthology.org/2025.emnlp-main.1239/)

**11. "Hallucination Detection in LLMs with Topological Divergence on Attention Graphs" (arXiv:2504.10063, April 2025)**
TOHA method: uses topological divergence between prompt and response subgraphs from attention matrices. Higher divergence in specific attention heads correlates with hallucinated outputs.
- [TOHA paper](https://arxiv.org/abs/2504.10063)

---

### SAE-BASED AND MECHANISTIC APPROACHES

**12. HalluSAE -- "Detecting Hallucinations in LLMs via Sparse Auto-Encoders" (arXiv:2604.16430, April 2026)**
Models hallucination as phase transitions in latent dynamics using sparse autoencoders. Identifies high-energy sparse features that propel representations from "truth attractors" to unstable hallucination plateaus. Three-stage pipeline: potential energy phase zone localization, sparse feature attribution, probing-based causal detection.
- [HalluSAE paper](https://arxiv.org/abs/2604.16430)

**13. "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" (arXiv:2605.05686, May 2026)**
Shows learned facts form attractor basins in hidden-state space. Conflict = basin competition; hallucination = basin absence where hidden state drifts freely.
- [Attractor Geometry paper](https://arxiv.org/html/2605.05686)

**14. PCNet -- "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv:2605.05953, May 2026)**
Probabilistic circuit trained as a density estimator over the LLM residual stream. Detects hallucinations as geometric anomalies. Claims near-perfect detection (AUROC up to 99%).
- [PCNet paper](https://arxiv.org/abs/2605.05953)

---

### TOKEN-LEVEL AND REAL-TIME DETECTION

**15. HaMI -- "Robust Hallucination Detection in LLMs via Adaptive Token Selection" (NeurIPS 2025)**
Formulates hallucination detection as Multiple Instance Learning over token-level representations.
- [HaMI paper / GitHub](https://github.com/mala-lab/HaMI)

**16. "Real-Time Detection of Hallucinated Entities in Long-Form Generation" (arXiv:2509.03531)**
Streaming approach for real-time identification of hallucinated tokens targeting entity-level hallucinations. Finds hallucination signals most detectable at the onset of hallucinated spans.
- [Real-Time Detection paper](https://arxiv.org/html/2509.03531v1)

**17. HALP -- "Detecting Hallucinations in Vision-Language Models without Generating a Single Token" (arXiv:2603.05465, March 2026)**
Probes internal representations pre-generation to predict hallucination risk, achieving up to 0.93 AUROC without any decoding.
- [HALP paper](https://arxiv.org/abs/2603.05465)

---

### THE TWO EMNLP 2025 PAPERS OF INTEREST

**18. "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" (arXiv:2503.14477, EMNLP 2025 main, highlighted as one of the 35 SAC-highlighted papers)**
Finds verbal uncertainty is governed by a single linear feature (VUF) in representation space. The mismatch between semantic and verbal uncertainty is a better hallucination predictor than semantic uncertainty alone. Proposes Mechanistic Uncertainty Calibration (MUC) to steer activations, reducing confident hallucinations by ~30%. Note: This was an SAC-highlighted paper at EMNLP 2025, but was NOT one of the official Outstanding Paper Award winners.
- [Calibrating Verbal Uncertainty paper](https://arxiv.org/abs/2503.14477)
- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.187/)

**19. "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps" (arXiv:2502.14829, EMNLP 2025 Outstanding Paper Award winner)**
Introduces FUR (Faithfulness by Unlearning Reasoning steps): erases information in reasoning steps from model parameters, then measures the effect on predictions. Won the EMNLP 2025 Outstanding Paper Award. Authors: Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov.
- [Measuring CoT Faithfulness paper](https://arxiv.org/abs/2502.14829)
- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.504/)

---

### ADDITIONAL RELEVANT CONTEXT

**20. MIND (ACL 2024 Findings)** -- Unsupervised real-time hallucination detection using internal states (contextual embeddings during inference). An older but important baseline for temporal internal-state monitoring.
- [MIND paper](https://arxiv.org/abs/2403.06448)

**21. TARAC -- "Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection" (arXiv:2504.04099, April 2025)**
Observes progressive decline of attention to image tokens during generation, with hallucinated positions exhibiting lower visual attention. Multimodal but the temporal attention tracking mechanism is relevant.
- [TARAC paper](https://arxiv.org/html/2504.04099)

**22. "The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity" (arXiv:2605.06611, May 2026)**
Explains the mechanistic origin of attention sinks -- important for any paper building on sink features.
- [Structural Origin of Attention Sink paper](https://arxiv.org/html/2605.06611)

---

### SUMMARY OF KEY THREATS AND GAPS

**Most dangerous competitor:** SinkProbe (2604.10697) is almost exactly the same idea -- attention sinks as hallucination signals. The SinkWatch authors need to clearly differentiate from this April 2026 paper.

**Strongest temporal competitors:** The Frequency-Aware Attention paper (2602.18145) treats attention as a temporal signal and extracts frequency features, and "Shadows in the Attention" (2505.16894) directly compares attention drift vs. hidden-state drift during generation -- both overlap with SinkWatch's core contribution.

**Attention vs. hidden-state comparison:** The LapEigvals EMNLP 2025 paper found attention-based methods generalize better out-of-domain than hidden-state probes. "Shadows in the Attention" is the most direct study comparing both signal types temporally.

**EMNLP 2025 clarification:** "Calibrating Verbal Uncertainty" was SAC-highlighted (top 35) but did NOT win the Outstanding Paper Award. "Measuring CoT Faithfulness by Unlearning" DID win the Outstanding Paper Award.

**The dynamical systems cluster** (Hallucination Basins, Trajectory Commitment, Attractor Geometry, HalluSAE) represents a rapidly growing body of work framing hallucination through the lens of attractor dynamics in latent space -- a closely related theoretical framework to temporal tracking of attention features.

Sources:
- [SinkProbe - Attention Sinks as Internal Signals](https://arxiv.org/abs/2604.10697)
- [SinkTrack - ICLR 2026](https://arxiv.org/abs/2604.10027)
- [Frequency-Aware Attention](https://arxiv.org/abs/2602.18145)
- [Attention Sink Survey](https://arxiv.org/html/2604.10098)
- [HALT - Log-probs as Time series](https://arxiv.org/abs/2602.02888)
- [Before the First Token](https://arxiv.org/abs/2604.13068)
- [Hallucination as Trajectory Commitment](https://arxiv.org/abs/2604.15400)
- [Hallucination Basins](https://arxiv.org/abs/2604.04743)
- [Shadows in the Attention](https://arxiv.org/abs/2505.16894)
- [LapEigvals / Spectral Features - EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1239/)
- [TOHA - Topological Divergence](https://arxiv.org/abs/2504.10063)
- [HalluSAE - Sparse Auto-Encoders](https://arxiv.org/abs/2604.16430)
- [Attractor Geometry of Transformer Memory](https://arxiv.org/html/2605.05686)
- [PCNet - Probabilistic Circuits](https://arxiv.org/abs/2605.05953)
- [HaMI - NeurIPS 2025](https://github.com/mala-lab/HaMI)
- [Real-Time Hallucinated Entities](https://arxiv.org/html/2509.03531v1)
- [HALP - Pre-generation Detection](https://arxiv.org/abs/2603.05465)
- [Calibrating Verbal Uncertainty - EMNLP 2025](https://arxiv.org/abs/2503.14477)
- [Measuring CoT Faithfulness - EMNLP 2025 Outstanding Paper](https://arxiv.org/abs/2502.14829)
- [MIND - ACL 2024](https://arxiv.org/abs/2403.06448)
- [TARAC - Temporal Attention](https://arxiv.org/html/2504.04099)
- [Structural Origin of Attention Sink](https://arxiv.org/html/2605.06611)
- [EMNLP 2025 Awards](https://2025.emnlp.org/program/awards/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd08c37-8f50-4aa4-ac47-2fdc61bcc9ec",
  "isSidechain": true,
  "agentId": "a3d1af933f509dd09",
  "requestId": "req_011Cb4VauECCBZGPJkBuFH9k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fed4060-4822-465e-8761-9d2bf0d236c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ecba7aa0-8ace-4a3e-8057-4d59d32dc732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167QhET4KxxzQq7Zk7ioqVV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 30661,
      "output_tokens": 4094,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1020,
          "output_tokens": 4094,
          "cache_read_input_tokens": 30661,
          "cache_creation_input_tokens": 1860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1860,
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
