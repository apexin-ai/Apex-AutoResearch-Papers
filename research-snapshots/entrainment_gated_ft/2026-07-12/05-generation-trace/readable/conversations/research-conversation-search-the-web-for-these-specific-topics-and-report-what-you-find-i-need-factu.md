# Research conversation: Search the web for these specific topics and report what you find. I need factual verification for an ML paper review. 1

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5e7811df73ba992a.jsonl`
- **Structured JSON:** [`04e6eec9d7b15937250c.json`](../../sessions/04/04e6eec9d7b15937250c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-12T00:19:31.377Z_

Search the web for these specific topics and report what you find. I need factual verification for an ML paper review.

1. Search for "R-Sparse rank-aware activation sparsity ICLR 2025" - verify this paper exists, what it actually does (does it treat attention and MLP sparsity as additive/independent?), and its reported speedups.

2. Search for "attention MLP sparsity interaction transformer" or "joint attention MLP sparsity" - are there ANY papers that study the interaction between attention-head sparsity and MLP activation sparsity (not just applying both, but characterizing how they interact)?

3. Search for "AMP attention heads MLP pruning IJCNN 2025" - verify this paper exists and what it does.

4. Search for "cross-partial derivative sparsity" or "sparsity interaction surface" - has anyone formalized sparsity interaction this way?

5. Search for "ActTail global activation sparsity 2026" and "WiSparse mixed-granularity activation sparsity 2026" - verify these recent MLP sparsity papers exist.

Use WebSearch for each query. Report exactly what you find - titles, venues, dates, key claims. Do not speculate beyond what the search results show.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "49f0141a-ce28-4ff0-ba2e-ba2b8407a555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:19:31.381Z_

```json
{
  "parentUuid": "49f0141a-ce28-4ff0-ba2e-ba2b8407a555",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "726c3725-17dd-4103-b559-3b8edca2995a",
  "timestamp": "2026-05-12T00:19:31.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:19:33.743Z_



I'll search for all these topics in parallel. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "726c3725-17dd-4103-b559-3b8edca2995a",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWTM5K1jWmK6VM4BfU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5cdfc3b-13bc-4b53-b85d-d596c45a7f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011avA8pm2SWq4NC2KenVKJH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 841,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:19:34.106Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L8i5LGmNMRUYauvp4EB7Sb`</summary>

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
  "parentUuid": "f5cdfc3b-13bc-4b53-b85d-d596c45a7f61",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWTM5K1jWmK6VM4BfU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1007818-dbcc-4df3-ac05-3cb849689135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011avA8pm2SWq4NC2KenVKJH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 8223,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 841,
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

_source line 5 · 2026-05-12T00:19:34.110Z_

<details><summary>↩ Tool result · `toolu_01L8i5LGmNMRUYauvp4EB7Sb`</summary>

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
  "parentUuid": "d1007818-dbcc-4df3-ac05-3cb849689135",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "3758337e-5479-4991-958c-866770d587ce",
  "sourceToolAssistantUUID": "d1007818-dbcc-4df3-ac05-3cb849689135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:19:36.535Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3758337e-5479-4991-958c-866770d587ce",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04dccabe-ee8d-48fb-b15c-933603d44f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
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

_source line 7 · 2026-05-12T00:19:37.540Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E3DDi1BdkyuZiRVxKvUg2n`</summary>

```json
{
  "query": "R-Sparse rank-aware activation sparsity ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04dccabe-ee8d-48fb-b15c-933603d44f79",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66aef4eb-f241-4ee2-9f30-1dac1975cb1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
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

_source line 8 · 2026-05-12T00:19:37.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRC6YRkhSiqefKRt6kjYWr`</summary>

```json
{
  "query": "attention MLP sparsity interaction transformer joint attention MLP sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66aef4eb-f241-4ee2-9f30-1dac1975cb1f",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1792f86-d5ca-47a7-9408-6bd46a10add7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
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

_source line 9 · 2026-05-12T00:19:38.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RN1sXWRUgTKMTby4fWr3Sd`</summary>

```json
{
  "query": "AMP attention heads MLP pruning IJCNN 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1792f86-d5ca-47a7-9408-6bd46a10add7",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f5b04c-9a3d-4feb-8b2f-d61fca72a071",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
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

_source line 10 · 2026-05-12T00:19:39.379Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018AwTdU2V1142DhfZ1F4fJz`</summary>

```json
{
  "query": "cross-partial derivative sparsity \"sparsity interaction surface\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f5b04c-9a3d-4feb-8b2f-d61fca72a071",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cc10423-16a9-487d-b134-7e471b8360e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
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

_source line 11 · 2026-05-12T00:19:40.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMedLqsoEUGPwPq3g1ymvH`</summary>

```json
{
  "query": "ActTail global activation sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc10423-16a9-487d-b134-7e471b8360e8",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiWfHRPeQjc61rJQgxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89905cc0-9956-45e3-acf1-4ca5440c14d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpBn73sBBZWsHyhta7J1Cj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 9064,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1414
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 9064,
          "cache_creation_input_tokens": 1414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1414,
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

_source line 12 · 2026-05-12T00:19:42.988Z_

<details><summary>↩ Tool result · `toolu_018AwTdU2V1142DhfZ1F4fJz`</summary>

```text
Web search results for query: "cross-partial derivative sparsity "sparsity interaction surface""

No links found.

The search returned no results. This could mean that the exact phrase "sparsity interaction surface" combined with cross-partial derivative sparsity is not widely used in available web sources, or the combination of these specific terms doesn't match any indexed pages.

You might try:
- Searching for just "sparsity interaction surface" without the other terms
- Searching for "cross-partial derivative sparsity" separately
- Searching for related concepts like "additive models" or "interaction detection" combined with sparsity
- Checking academic databases or specialized research repositories that might have more technical content

Would you like me to try a modified search with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cc10423-16a9-487d-b134-7e471b8360e8",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "80316be1-040b-44bd-88cd-1fc110ecd1ff",
  "sourceToolAssistantUUID": "9cc10423-16a9-487d-b134-7e471b8360e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:19:44.543Z_

<details><summary>↩ Tool result · `toolu_01E3DDi1BdkyuZiRVxKvUg2n`</summary>

```text
Web search results for query: "R-Sparse rank-aware activation sparsity ICLR 2025"

Links: [{"title":"RANK-AWARE ACTIVATION SPARSITY FOR EFFICIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"},{"title":"[2504.19449] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/abs/2504.19449"},{"title":"GitHub - VITA-Group/R-Sparse: [ICLR'25] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://github.com/VITA-Group/R-Sparse"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/html/2508.02128v1"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250419449Z/abstract"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=1225&show=1000"},{"title":"Masked Gated Linear Unit","url":"https://arxiv.org/html/2506.23225v1"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=9175&show=25"}]

Based on the search results, I found comprehensive information about R-Sparse, which was published at ICLR 2025:

## R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference

R-Sparse is a paper published as a conference paper at ICLR 2025 by Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, and Steven Li from The University of Texas at Austin and Meta AI.

### Problem and Approach

Activation sparsity offers a promising solution to reduce computation and memory movement, enabling more efficient inference, particularly for small-batch on-device applications. However, current approaches face limitations with non-ReLU activation functions, which are foundational to most advanced LLMs, or require heavy continual training.

### Key Contributions

R-Sparse is a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs. The authors conducted two preliminary investigations into how different components contribute to the output within a single linear layer and found two key observations: (i) the non-sparse components of the input function can be regarded as a few bias terms, and (ii) The full computation can be effectively approximated by an appropriate combination of input channels and weight singular values.

### Results

Experiments on Llama-2/3 and Mistral models across ten diverse tasks demonstrate that R-Sparse achieves comparable performance at 50% model-level sparsity, resulting in a significant 43% end-to-end efficient improvements with customized kernels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66aef4eb-f241-4ee2-9f30-1dac1975cb1f",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "da4d237b-afca-4af4-9666-eac96bd1525b",
  "sourceToolAssistantUUID": "66aef4eb-f241-4ee2-9f30-1dac1975cb1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:19:45.148Z_

<details><summary>↩ Tool result · `toolu_01RN1sXWRUgTKMTby4fWr3Sd`</summary>

```text
Web search results for query: "AMP attention heads MLP pruning IJCNN 2025"

Links: [{"title":"[2504.21174] Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/abs/2504.21174"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11227985/"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421174G/abstract"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=9950&show=50"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174v1"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=1525&show=2000"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=1475&show=500"},{"title":"Attention Head Pruning Research","url":"https://www.aussieai.com/research/head-pruning"},{"title":"GitHub - arturjordao/arturjordao · GitHub","url":"https://github.com/arturjordao/arturjordao"}]

Based on the search results, here's what I found:

## AMP: Attention Heads and MLP Pruning at IJCNN 2025

AMP (Attention Heads and MLP Pruning) is a novel structured pruning method that efficiently compresses LLMs by removing less critical structures within Multi-Head Attention (MHA) and Multilayer Perceptron (MLP).

### Key Approach

AMP assesses structural importance by projecting the input data onto weights and overcomes the limitations of existing techniques, which often fall short in flexibility or efficiency.

### Performance Results

AMP surpasses the current state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points, achieving a 30% pruning ratio with minimal impact on zero-shot task performance. Moreover, AMP also improves inference speeds, making it well-suited for deployment in resource-constrained environments.

### Compatibility

The flexibility of AMP is confirmed on different families of LLMs, including LLaMA and Phi.

### Publication

The paper is to be published in the International Joint Conference on Neural Networks (IJCNN), 2025, with the conference taking place in Rome, Italy.

The paper was authored by Leandro Giusti Mugnaini, Bruno Lopes Yamamoto, Lucas Lauton de Alcantara, Victor Zacarias, Edson Bollis, Lucas Pellicer, Anna Helena Reali Costa, and Artur Jordao, and is available on arXiv as paper 2504.21174.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56f5b04c-9a3d-4feb-8b2f-d61fca72a071",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "23e1b88a-713e-464e-a52a-8a88b0ecb8a6",
  "sourceToolAssistantUUID": "56f5b04c-9a3d-4feb-8b2f-d61fca72a071",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:19:45.609Z_

<details><summary>↩ Tool result · `toolu_01KRC6YRkhSiqefKRt6kjYWr`</summary>

```text
Web search results for query: "attention MLP sparsity interaction transformer joint attention MLP sparsity"

Links: [{"title":"[2310.00535] JoMA: Demystifying Multilayer Transformers via JOint Dynamics of MLP and Attention","url":"https://arxiv.org/abs/2310.00535"},{"title":"JoMA: Demystifying Multilayer Transformers via Joint Dynamics of MLP and Attention | OpenReview","url":"https://openreview.net/forum?id=LbJqRGNYCf"},{"title":"JoMA: Demystifying Multilayer Transformers via JOint Dynamics of MLP and Attention","url":"https://arxiv.org/html/2310.00535v3"},{"title":"What Matters in Transformers? Not All Attention is Needed","url":"https://arxiv.org/html/2406.15786v6"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/html/2504.17768"},{"title":"Crisp Attention: Regularizing Transformers via Structured Sparsity","url":"https://arxiv.org/html/2508.06016v1"},{"title":"MLP Can Be A Good Transformer Learner","url":"https://arxiv.org/html/2404.05657v1"},{"title":"[2402.15055] Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/abs/2402.15055"},{"title":"Filtering with Self-Attention and Storing with MLP: One-Layer Transformers Can Provably Acquire and Extract Knowledge","url":"https://arxiv.org/html/2508.00901"}]

I've performed a web search on attention MLP sparsity interaction in transformers with joint attention MLP sparsity. Here are the key research findings:

## Key Papers and Findings:

**1. JoMA: Joint MLP/Attention Dynamics**
JoMA proposes a novel mathematical framework to understand the training procedure of multilayer Transformer architectures, achieved by integrating out the self-attention layer in Transformers, producing a modified dynamics of MLP layers only. Importantly, JoMA predicts that the attention first becomes sparse (to learn salient tokens), then dense (to learn less salient tokens) in the presence of nonlinear activations.

**2. Joint Layer Drop**
A "Joint Layer Drop" approach targets both MLP layers and Attention layers, finding that jointly dropping low-importance Attention and MLP layers yields better performance under high sparsity conditions compared to pruning only one type of layer.

**3. Attention-MLP Interactions**
While the attention mechanism and multi-layer perceptrons (MLPs) have been studied independently, their interactions remain largely unexplored, with recent studies investigating how attention heads and next-token neurons interact in LLMs to predict new words.

**4. Joint Training Dynamics**
Recent work characterizes the full joint training dynamics of self-attention and MLP components during next-token prediction-based pre-training, as well as the full and low-rank joint dynamics during subsequent fine-tuning.

These findings suggest that understanding and optimizing the interaction between attention and MLP sparsity is an emerging area of research in transformer efficiency and interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1792f86-d5ca-47a7-9408-6bd46a10add7",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "55c48dcf-7bc5-461f-a010-a38b67e368f4",
  "sourceToolAssistantUUID": "c1792f86-d5ca-47a7-9408-6bd46a10add7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:19:47.134Z_

<details><summary>↩ Tool result · `toolu_01VMedLqsoEUGPwPq3g1ymvH`</summary>

```text
Web search results for query: "ActTail global activation sparsity 2026"

Links: [{"title":"[2603.12272] ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2603.12272"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2603.12272"},{"title":"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | Request PDF","url":"https://www.researchgate.net/publication/385860215_PowerInfer_Fast_Large_Language_Model_Serving_with_a_Consumer-grade_GPU"},{"title":"LLM in a flash: Efficient Large Language Model Inference with Limited Memory | Request PDF","url":"https://www.researchgate.net/publication/384210493_LLM_in_a_flash_Efficient_Large_Language_Model_Inference_with_Limited_Memory"},{"title":"[2408.14690] Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2408.14690"},{"title":"Activation Sparsity: Concepts, Methods, and Applications | by Ali Borji | Mar, 2026 | Medium","url":"https://medium.com/@aliborji/activation-sparsity-concepts-methods-and-applications-b9b371588daa"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=osoWxY8q2E"}]

I found detailed information about ActTail. Here's what the search reveals:

## ActTail: Global Activation Sparsity in Large Language Models

ActTail was submitted on February 18, 2026, and addresses activation sparsity as a promising approach for accelerating large language model inference by reducing computation and memory movement.

### Key Innovation

ActTail is a TopK magnitude-based activation sparsity method with global activation sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. The method captures heterogeneity via the heavy-tail exponent computed from each projection's empirical spectral density (ESD), which is used as a quantitative indicator to assign projection-specific sparsity budgets.

### Why It Matters

Existing activation sparsity methods typically apply uniform sparsity across projections, ignoring the heterogeneous statistical properties of Transformer weights and thereby amplifying performance degradation. ActTail addresses this limitation.

### Performance Results

At 80% sparsity, perplexity is reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, and 9.4% on Mistral-7B. Additionally, experiments on LLaMA and Mistral models show that the method improves both perplexity and downstream task performance at high sparsity compared to uniform allocation.

### Theoretical Contribution

The paper provides a theoretical analysis that establishes an explicit relationship between the activation sparsity ratio and the heavy-tail exponent under the HT-SR regime, offering principled guidance for sparsity allocation beyond heuristic design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89905cc0-9956-45e3-acf1-4ca5440c14d5",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "330bb427-4028-4f8e-ba03-0dbf5793ea2f",
  "sourceToolAssistantUUID": "89905cc0-9956-45e3-acf1-4ca5440c14d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T00:19:50.200Z_

Now let me run the remaining searches -- the WiSparse query and some follow-up queries for better coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "330bb427-4028-4f8e-ba03-0dbf5793ea2f",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiXciRJ9oeDRX9tneWz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0fff4cf-00bd-4f6d-8d70-ab2e239e23de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld7V4Jt5KqddnjdYYxTTQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4198,
      "cache_read_input_tokens": 10478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4198,
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

_source line 18 · 2026-05-12T00:19:50.690Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0153VpSwcqPC1A1WZt6AmETr`</summary>

```json
{
  "query": "WiSparse mixed-granularity activation sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0fff4cf-00bd-4f6d-8d70-ab2e239e23de",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiXciRJ9oeDRX9tneWz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a32ce2f1-fae3-46f3-b35f-211597e4adc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld7V4Jt5KqddnjdYYxTTQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4198,
      "cache_read_input_tokens": 10478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4198,
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

_source line 19 · 2026-05-12T00:19:51.161Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C29HkFWoDcVeyskH6WpPxv`</summary>

```json
{
  "query": "\"sparsity interaction surface\" machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32ce2f1-fae3-46f3-b35f-211597e4adc1",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiXciRJ9oeDRX9tneWz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e094cb1-8f5d-4726-b3bd-fd6df725f306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld7V4Jt5KqddnjdYYxTTQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4198,
      "cache_read_input_tokens": 10478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4198,
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

_source line 20 · 2026-05-12T00:19:51.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017NnohTRNS2rXqQsLLjjQVa`</summary>

```json
{
  "query": "\"cross-partial derivative\" sparsity neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e094cb1-8f5d-4726-b3bd-fd6df725f306",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiXciRJ9oeDRX9tneWz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d84f2024-98b2-4d2d-a9f3-ee81d4078b3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld7V4Jt5KqddnjdYYxTTQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4198,
      "cache_read_input_tokens": 10478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4198,
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

_source line 21 · 2026-05-12T00:19:57.213Z_

<details><summary>↩ Tool result · `toolu_01C29HkFWoDcVeyskH6WpPxv`</summary>

```text
Web search results for query: ""sparsity interaction surface" machine learning"

Links: [{"title":"Sparsity in Machine Learning: Theory and Applications","url":"https://dspace.mit.edu/handle/1721.1/143157"},{"title":"The Concepts of Dense and Sparse in the Context of Neural Networks | Baeldung on Computer Science","url":"https://www.baeldung.com/cs/neural-networks-dense-sparse"},{"title":"Sparse Representation in Deep Learning - GeeksforGeeks","url":"https://www.geeksforgeeks.org/deep-learning/sparse-representation-in-deep-learning/"},{"title":"What Is Sparsity in AI Inference and Machine Learning? | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/sparsity-ai-inference/"},{"title":"Understanding Sparse Matrices: A Key Concept in Machine Learning","url":"https://datakulture.com/blog/understanding-sparse-matrix-a-key-concept-in-machine-learning/"},{"title":"Sparsity Meaning & Example - AI Guv","url":"https://aiguv.com/ai-dictionary/sparsity/"},{"title":"What is sparsity and why is it important for machine learning? - Quora","url":"https://www.quora.com/What-is-sparsity-and-why-is-it-important-for-machine-learning"},{"title":"Sparse Interaction Additive Networks via Feature Interaction Detection and Sparse Selection | OpenReview","url":"https://openreview.net/forum?id=Q6DJ12oQjrp"},{"title":"Sparse Learning","url":"https://sparse-learning.github.io/"},{"title":"Data Sparsity — Managing Incomplete Data in Machine Learning","url":"https://www.innovatiana.com/en/glossary/data-sparsity"}]

Based on the search results, I found relevant information about sparsity in machine learning. While the results don't contain a specific concept called "sparsity interaction surface," they do cover related topics that may be relevant to your query:

## Sparsity in Machine Learning

Sparsity refers to the condition where most of the elements in a dataset, matrix, or vector are zero or absent, and is common in high-dimensional data, where many features or attributes are not present or have zero values.

## Sparse Interactions

One particularly relevant finding is Sparse Interaction Additive Networks (SIAN), which construct a bridge from simple and interpretable models to fully connected neural networks. These networks leverage techniques in feature interaction detection to efficiently identify the necessary feature combinations.

## Benefits of Sparsity

Sparsity refers to data or models where most values are zero or inactive, with only a small number of meaningful elements, and is important in machine learning because it reduces computational cost, improves efficiency, and helps models focus on the most relevant features.

If you're looking for information about a more specific concept called "sparsity interaction surface," you may want to provide additional context or check if this is a term from a particular research paper or publication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e094cb1-8f5d-4726-b3bd-fd6df725f306",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "5aa9df9b-c642-42a3-9084-aec982564a41",
  "sourceToolAssistantUUID": "6e094cb1-8f5d-4726-b3bd-fd6df725f306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:19:57.553Z_

<details><summary>↩ Tool result · `toolu_0153VpSwcqPC1A1WZt6AmETr`</summary>

```text
Web search results for query: "WiSparse mixed-granularity activation sparsity 2026"

Links: [{"title":"[2602.14452] WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/abs/2602.14452"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-aware Mixed Activation Sparsity","url":"https://arxiv.org/html/2602.14452"},{"title":"Joint Sparsity with Mixed Granularity for Efficient GPU Implementation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9473939/"},{"title":"Published as a conference paper at ICLR 2026 LSA: LAYER-WISE SPARSITY","url":"https://openreview.net/pdf?id=xq3lza5IjN"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High ...","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.pdf"},{"title":"MixA-Q: Revisiting Activation Sparsity for Vision Transformers from a Mixed-Precision Quantization Perspective","url":"https://arxiv.org/html/2507.19131"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity | OpenReview","url":"https://openreview.net/forum?id=B9XP2R9LtG"},{"title":"Accelerating Deep Neural Networks via Semi-Structured Activation Sparsity","url":"https://openaccess.thecvf.com/content/ICCV2023W/RCV/papers/Grimaldi_Accelerating_Deep_Neural_Networks_via_Semi-Structured_Activation_Sparsity_ICCVW_2023_paper.pdf"}]

Based on the search results, I found relevant information about WiSparse and mixed-granularity activation sparsity from 2026.

## WiSparse: Mixed-Granularity Activation Sparsity

WiSparse is a Weight-aware Mixed-Granularity Training-free Activation Sparsity method that leverages both activation and weight information for adaptive sparsity allocation.

### Key Technical Approach

The method introduces a weight-aware mechanism integrating activation magnitudes with precomputed weight norms to accurately identify salient channels, combined with a mixed-granularity allocation scheme where a global budget is distributed across blocks via evolutionary search to protect sensitive regions, then refined within blocks to minimize reconstruction error.

### Performance Results

At 50% sparsity, WiSparse preserves 97% of Llama3.1's dense performance, surpassing the strongest baseline by 2.23 percentage points while achieving a 21.4% acceleration in end-to-end inference speed. The method was tested on multiple models including Llama3.1, Qwen2.5, and Mistral.

### Motivation

The research identifies two key phenomena in modern LLMs: 1) less significant activations may align with highly important weights, and 2) sparsity sensitivity varies non-monotonically across model blocks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a32ce2f1-fae3-46f3-b35f-211597e4adc1",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "aacdb52f-ae9d-40e8-bb7b-4c79aaaeecf0",
  "sourceToolAssistantUUID": "a32ce2f1-fae3-46f3-b35f-211597e4adc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:19:58.528Z_

<details><summary>↩ Tool result · `toolu_017NnohTRNS2rXqQsLLjjQVa`</summary>

```text
Web search results for query: ""cross-partial derivative" sparsity neural network"

Links: [{"title":"Layer sparsity in neural networks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0378375824000521"},{"title":"Sparsity in Deep Learning Tutorial","url":"https://htor.inf.ethz.ch/sparsity-in-dl/"},{"title":"Sparse Learning","url":"https://sparse-learning.github.io/"},{"title":"Deep-learning of parametric partial differential equations from sparse and noisy data | Physics of Fluids | AIP Publishing","url":"https://pubs.aip.org/aip/pof/article/33/3/037132/1064888/Deep-learning-of-parametric-partial-differential"},{"title":"Sparsity in Deep Learning: Pruning and growth for efficient ...","url":"https://www.jmlr.org/papers/volume22/21-0366/21-0366.pdf"},{"title":"Neural networks and deep learning","url":"http://neuralnetworksanddeeplearning.com/chap3.html"},{"title":"GN-SINDy: Greedy Sampling Neural Network in Sparse Identification of Nonlinear Partial Differential Equations","url":"https://arxiv.org/html/2405.08613v1"},{"title":"DeepMoD: Deep learning for model discovery in noisy data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0021999120307592"},{"title":"Sparsity in Deep Learning: Pruning and growth for efficient ...","url":"https://htor.inf.ethz.ch/publications/img/hoefler-sparsity-in-deep-learning.pdf"},{"title":"[2102.00554] Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks","url":"https://arxiv.org/abs/2102.00554"}]

Based on the web search results, I found information related to sparsity in neural networks and partial derivatives in neural networks, though the results don't specifically address "cross-partial derivatives" as a standalone concept in sparsity research.

Here are the relevant findings:

**Sparsity in Neural Networks:**
Sparsity has become popular in machine learning because it can save computational resources, facilitate interpretations, and prevent overfitting. Sparsity can reduce the size of neural networks by selectively pruning components, and sparse networks generalize just as well, if not better than, the original dense networks, while reducing memory footprint and shortening training time.

**Partial Derivatives and Neural Networks:**
The search results show that derivatives can be approximated by automatic differentiation during the backpropagation process, and with the benefit of the neural network, derivatives can be calculated from sparse and noisy data with high accuracy.

**Model Discovery Applications:**
Some approaches discover partial differential equations underlying spatio-temporal datasets using sparse regression on a library of possible functions and their derivatives, seamlessly integrating deep neural networks for rich representation learning, physics embedding, automatic differentiation and sparse regression.

The search results primarily focus on general sparsity techniques in neural networks and automatic differentiation for computing derivatives, but don't appear to contain specific research on "cross-partial derivatives" as a distinct concept in neural network sparsity. If you're looking for more specialized information on this topic, you may want to consult academic databases or papers that specifically address partial derivative structures in neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d84f2024-98b2-4d2d-a9f3-ee81d4078b3b",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "c78bc819-de46-4541-a784-d40a46986451",
  "sourceToolAssistantUUID": "d84f2024-98b2-4d2d-a9f3-ee81d4078b3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:20:03.798Z_

Let me do a couple more targeted follow-up searches to get more detail on a few items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c78bc819-de46-4541-a784-d40a46986451",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiYTyLaJepgtiFijaLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fba858b-e2b9-4eb5-9fc8-297ceb530888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRrZ4pc6NRqEErQVFG2k8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2898,
      "cache_read_input_tokens": 14676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2898,
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

_source line 25 · 2026-05-12T00:20:04.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RdCupdz9Azf3YZ5SorrQdX`</summary>

```json
{
  "query": "R-Sparse attention sparsity MLP sparsity additive independent treatment ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fba858b-e2b9-4eb5-9fc8-297ceb530888",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiYTyLaJepgtiFijaLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "509d2df1-1d13-42ef-a70d-bba9282c388d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRrZ4pc6NRqEErQVFG2k8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2898,
      "cache_read_input_tokens": 14676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2898,
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

_source line 26 · 2026-05-12T00:20:05.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0193hLsmjNXuh1iheZyMKqDK`</summary>

```json
{
  "query": "joint attention head pruning MLP neuron pruning interaction effect transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509d2df1-1d13-42ef-a70d-bba9282c388d",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiYTyLaJepgtiFijaLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e576551b-ec5d-43e0-b7d8-da30c9503002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRrZ4pc6NRqEErQVFG2k8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2898,
      "cache_read_input_tokens": 14676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2898,
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

_source line 27 · 2026-05-12T00:20:06.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9Zfej4rPvkTQ3FY8zh2KF`</summary>

```json
{
  "query": "WiSparse arxiv 2602.14452 mixed granularity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e576551b-ec5d-43e0-b7d8-da30c9503002",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiYTyLaJepgtiFijaLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "543b0dea-9175-43e2-94e2-1ba9afbaf27d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRrZ4pc6NRqEErQVFG2k8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2898,
      "cache_read_input_tokens": 14676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2898,
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

_source line 28 · 2026-05-12T00:20:11.375Z_

<details><summary>↩ Tool result · `toolu_01RdCupdz9Azf3YZ5SorrQdX`</summary>

```text
Web search results for query: "R-Sparse attention sparsity MLP sparsity additive independent treatment ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"Published as a conference paper at ICLR 2025","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.07164"},{"title":"Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies","url":"https://arxiv.org/html/2511.00819v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.04878"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"}]

Based on the web search results, I found relevant information about R-Sparse and related sparsity work from ICLR 2025.

## Key Findings

R-Sparse is an inference framework with an evolutionary search algorithm for determining the optimal sparsity recipe. It is a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs.

**Core Technical Approach:**

R-Sparse decomposes the computation of each linear layer with sparse and low-rank components. For the sparse portion, the approach identifies sparse channels by selecting those with large magnitude values and loads only the corresponding rows of weights into SRAM for computation. For the low-rank components, non-sparse channels are routed to low-rank modules obtained from offline low-rank decomposition of the original weights.

**Key Advantages:**

The work shifts focus to the sparse structure of input channels and singular value components, eliminating the need for active channel prediction while feasible for both attention and MLP blocks, leading to higher sparse ratios without additional training.

R-Sparse can be applied to both attention and MLP modules achieving higher sparsity levels, and the patterns of sparse and low-rank combinations vary across different layers.

The paper was published as a conference paper at ICLR 2025, and focuses on addressing limitations of previous sparsity approaches that struggled with non-ReLU activation functions and required heavy training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "509d2df1-1d13-42ef-a70d-bba9282c388d",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "b8c8f077-6bba-46f9-8200-dc1cffd651d9",
  "sourceToolAssistantUUID": "509d2df1-1d13-42ef-a70d-bba9282c388d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T00:20:13.490Z_

<details><summary>↩ Tool result · `toolu_0193hLsmjNXuh1iheZyMKqDK`</summary>

```text
Web search results for query: "joint attention head pruning MLP neuron pruning interaction effect transformer"

Links: [{"title":"Attention Heads and MLP Pruning - Efficient LLMs with AMP","url":"https://arxiv.org/pdf/2504.21174"},{"title":"Attention Head Pruning Research","url":"https://www.aussieai.com/research/head-pruning"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174"},{"title":"Adaptive MLP Pruning for Large Vision Transformers","url":"https://arxiv.org/html/2603.08100"},{"title":"Simultaneous image patch attention and pruning for patch selective transformer - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0262885624003445"},{"title":"Layer-wise Pruning of Transformer Attention Heads for Efficient Language Modeling | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9613933/"},{"title":"ADAPTIVE MLP PRUNING FOR LARGE VISION ...","url":"https://openreview.net/pdf/139955b5d36f18d37769efb8784ed1d7833a5002.pdf"},{"title":"[2110.03252] Layer-wise Pruning of Transformer Attention Heads for Efficient Language Modeling","url":"https://ar5iv.labs.arxiv.org/html/2110.03252"},{"title":"GitHub - aiha-lab/Attention-Head-Pruning: Layer-wise Pruning of Transformer Heads for Efficient Language Modeling","url":"https://github.com/aiha-lab/Attention-Head-Pruning"},{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/html/2402.15055v1"}]

I found search results related to your query about joint attention head pruning and MLP neuron pruning in transformers. Here's what the research shows:

## Joint Pruning Methods

AMP is a novel structured pruning method designed to efficiently identify and eliminate less critical components (attention heads and MLP neurons) from Large Language Models (LLMs). The approach prunes attention heads from Multi-Head Attention (MHA) and neurons from Multilayer Perceptron (MLP) within each layer of the model.

## Interaction Effects Between Attention and MLP Pruning

An important finding regarding the interaction effects is that pruning only attention heads severely impairs predictive performance, reducing the average accuracy by 23.39 percentage points compared to pruning both attention heads and MLPs. This demonstrates a significant interaction effect where the performance impact of pruning attention heads depends on whether MLPs are also being pruned.

SAViT introduces joint importance evaluation across all components for Taylor pruning to achieve a more balanced parameter reduction, which directly addresses the interaction between different transformer components during pruning.

## Understanding Attention-MLP Interactions

Beyond pruning, research has also examined the deeper interactions between these components. The exact roles, combinations, and interactions of the attention heads and MLPs have yet to be fully elucidated; researchers aim to characterize attention heads and their interaction with next-token neurons.

The search results suggest that joint consideration of both attention head and MLP pruning is important for maintaining model performance, rather than pruning these components independently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e576551b-ec5d-43e0-b7d8-da30c9503002",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "2ca80b4d-28b2-4d33-9556-f5218467fc9d",
  "sourceToolAssistantUUID": "e576551b-ec5d-43e0-b7d8-da30c9503002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T00:20:14.423Z_

<details><summary>↩ Tool result · `toolu_01L9Zfej4rPvkTQ3FY8zh2KF`</summary>

```text
Web search results for query: "WiSparse arxiv 2602.14452 mixed granularity"

Links: [{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-aware Mixed Activation Sparsity","url":"https://arxiv.org/html/2602.14452"},{"title":"[2602.14452] WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/abs/2602.14452"},{"title":"Mixed-granularity Implicit Representation for Continuous Hyperspectral Compressive Reconstruction","url":"https://arxiv.org/html/2503.12783"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"ScaleBITS: Scalable Bitwidth Search for Hardware-Aligned Mixed-Precision LLMs","url":"https://arxiv.org/html/2602.17698v1"},{"title":"[2602.22698v1] Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs","url":"https://arxiv.org/abs/2602.22698v1"},{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"[2602.20561] A Granularity Characterization of Task Scheduling Effectiveness","url":"https://arxiv.org/abs/2602.20561"},{"title":"[2602.22698] Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs","url":"https://arxiv.org/abs/2602.22698"},{"title":"A Granularity Characterization of Task Scheduling Effectiveness","url":"https://arxiv.org/html/2602.20561"}]

Based on the search results, I found detailed information about WiSparse (arxiv 2602.14452):

## WiSparse: Weight-aware Mixed Activation Sparsity

WiSparse (Weight-aware Mixed-Granularity Training-free Activation Sparsity) is a method that leverages both activation and weight information and enables adaptive sparsity allocation across different granularities.

### Key Features

WiSparse introduces a weight-aware activation sparsification mechanism that integrates activation magnitudes with precomputed weight norms to more accurately identify salient channels.

The method combines this with a mixed-granularity sparsity allocation scheme featuring a coarse-to-fine strategy: a global sparsity budget is first distributed across blocks via evolutionary search to protect sensitive regions, and subsequently refined at finer granularities within each block to minimize reconstruction error.

### Performance

At 50% sparsity, WiSparse preserves 97% of Llama3.1's dense model performance, surpassing the strongest baseline by 2.23 percentage points while achieving a 21.4% acceleration in end-to-end inference speed.

The paper addresses limitations in existing training-free activation sparsity methods by identifying that less significant activations may align with highly important weights, and that sparsity sensitivity varies across model blocks rather than following a uniform pattern.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "543b0dea-9175-43e2-94e2-1ba9afbaf27d",
  "isSidechain": true,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "agentId": "a5e7811df73ba992a",
  "type": "user",
  "uuid": "fe50b39e-96ef-4db4-9245-8f00d88e7e50",
  "sourceToolAssistantUUID": "543b0dea-9175-43e2-94e2-1ba9afbaf27d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T00:21:08.192Z_

Here are the factual findings from all five searches:

---

## 1. R-Sparse (ICLR 2025) -- VERIFIED

**Paper exists.** "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference" is a confirmed ICLR 2025 conference paper by Zhenyu Zhang et al. (UT Austin / Meta AI). It appears on the official ICLR proceedings site, arXiv (2504.19449), OpenReview, and has a GitHub repo (VITA-Group/R-Sparse).

**What it does:** R-Sparse is a training-free activation sparsity method. It decomposes each linear layer into sparse and low-rank components. Sparse channels (large-magnitude activations) are selected and only the corresponding weight rows are loaded; non-sparse channels are routed through offline low-rank decompositions of the original weights. It uses an evolutionary search algorithm to determine the optimal per-layer sparsity recipe.

**Attention vs. MLP treatment:** R-Sparse is described as "feasible for both attention and MLP blocks." The search results indicate that the patterns of sparse and low-rank combinations "vary across different layers," meaning R-Sparse applies its mechanism to both attention and MLP projections but determines sparsity ratios independently per-layer via evolutionary search. The search results do not show any explicit modeling of the *interaction* between attention sparsity and MLP sparsity -- each projection's sparsity budget is determined by the search procedure, not by a joint interaction model. This is consistent with treating them as effectively independent (additive) contributions to the overall sparsity budget.

**Reported speedups:** 50% model-level sparsity with comparable performance, yielding **43% end-to-end efficiency improvement** with customized CUDA kernels. Tested on Llama-2/3 and Mistral across ten tasks.

---

## 2. Attention-MLP Sparsity Interaction -- VERY LIMITED PRIOR WORK

The search found papers that apply sparsity to both attention and MLP, but **no paper that formally characterizes how attention-head sparsity and MLP activation sparsity interact** (i.e., whether they are additive, synergistic, or antagonistic).

What does exist:

- **JoMA** (arXiv 2310.00535) studies joint *training dynamics* of attention and MLP (not sparsity interaction per se). It integrates out attention to derive modified MLP dynamics, predicting that attention first becomes sparse then dense during training.
- **AMP** (IJCNN 2025, see item 3) prunes both attention heads and MLP neurons jointly and observes an important interaction: pruning only attention heads drops accuracy by 23.39 percentage points compared to pruning both components. This is empirical evidence of interaction, but AMP does not formalize or characterize the interaction mathematically.
- **"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions"** (arXiv 2402.15055) studies how attention heads and next-token MLP neurons interact mechanistically, but does not address sparsity.
- **"What Matters in Transformers? Not All Attention is Needed"** (arXiv 2406.15786) examines dropping attention and MLP layers jointly but again does not formalize the interaction.

**Bottom line:** No paper was found that formally models or measures the *interaction term* between attention sparsity and MLP sparsity as a joint phenomenon.

---

## 3. AMP (IJCNN 2025) -- VERIFIED

**Paper exists.** "Efficient LLMs with AMP: Attention Heads and MLP Pruning" is confirmed on arXiv (2504.21174) and IEEE Xplore. It was published at IJCNN 2025 (Rome, Italy). Authors: Leandro Giusti Mugnaini, Bruno Lopes Yamamoto, Lucas Lauton de Alcantara, Victor Zacarias, Edson Bollis, Lucas Pellicer, Anna Helena Reali Costa, and Artur Jordao.

**What it does:** AMP is a structured pruning method that removes less critical attention heads and MLP neurons. It assesses structural importance by projecting input data onto weights. At 30% pruning ratio, it surpasses state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points with minimal zero-shot performance impact. Tested on LLaMA and Phi families.

**Key empirical finding on interaction:** Pruning only attention heads (without also pruning MLP) reduces accuracy by 23.39 points, suggesting pruning these components independently is suboptimal. However, AMP does not formalize this interaction mathematically.

---

## 4. "Cross-partial derivative sparsity" / "Sparsity interaction surface" -- NOT FOUND

**No results whatsoever.** The exact phrase "sparsity interaction surface" returned zero hits. "Cross-partial derivative sparsity" combined with neural networks also returned no relevant results. Broader searches for these concepts in the machine learning literature found nothing matching this terminology.

The closest related concept found was "Sparse Interaction Additive Networks (SIAN)" from OpenReview, which is about feature interaction detection in additive models -- a completely different topic.

**These terms do not appear to exist in the published literature.**

---

## 5. ActTail and WiSparse (2026) -- BOTH VERIFIED

### ActTail -- VERIFIED
**Paper exists.** "ActTail: Global Activation Sparsity in Large Language Models," arXiv 2603.12272, submitted February 18, 2026.

**What it does:** A TopK magnitude-based activation sparsity method with *global* (non-uniform) sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Uses the heavy-tail exponent computed from each projection's empirical spectral density to assign projection-specific sparsity budgets. At 80% sparsity: perplexity reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, 9.4% on Mistral-7B vs. uniform allocation.

### WiSparse -- VERIFIED
**Paper exists.** "WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity," arXiv 2602.14452, February 2026.

**What it does:** A weight-aware, mixed-granularity, training-free activation sparsity method. Integrates activation magnitudes with precomputed weight norms for channel saliency. Uses a coarse-to-fine allocation: global budget distributed across blocks via evolutionary search, then refined within blocks to minimize reconstruction error. At 50% sparsity, preserves 97% of Llama3.1 dense performance, surpassing the strongest baseline by 2.23 points, with 21.4% end-to-end speedup.

Note: "Mixed-granularity" refers to sparsity allocation granularity (block-level vs. projection-level budgets), not to mixing attention and MLP sparsity types.

---

## Summary Table

| Claim | Verdict |
|---|---|
| R-Sparse exists at ICLR 2025 | Confirmed |
| R-Sparse treats attn/MLP sparsity independently | Consistent with evidence (per-layer search, no joint interaction model) |
| R-Sparse 43% speedup at 50% sparsity | Confirmed |
| Papers studying attn-MLP sparsity *interaction* | None found that formalize the interaction |
| AMP at IJCNN 2025 | Confirmed |
| "Cross-partial derivative sparsity" or "sparsity interaction surface" | Not found in any literature |
| ActTail (2026) | Confirmed (arXiv 2603.12272) |
| WiSparse (2026) | Confirmed (arXiv 2602.14452) |

Sources:
- [R-Sparse ICLR 2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- [R-Sparse arXiv](https://arxiv.org/abs/2504.19449)
- [R-Sparse OpenReview](https://openreview.net/forum?id=9VMW4iXfKt)
- [R-Sparse GitHub](https://github.com/VITA-Group/R-Sparse)
- [R-Sparse HTML](https://arxiv.org/html/2504.19449v1)
- [AMP arXiv](https://arxiv.org/abs/2504.21174)
- [AMP IEEE Xplore](https://ieeexplore.ieee.org/document/11227985/)
- [AMP HTML](https://arxiv.org/html/2504.21174)
- [JoMA arXiv](https://arxiv.org/abs/2310.00535)
- [Interpreting Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)
- [What Matters in Transformers](https://arxiv.org/html/2406.15786v6)
- [ActTail arXiv](https://arxiv.org/abs/2603.12272)
- [WiSparse arXiv](https://arxiv.org/abs/2602.14452)
- [WiSparse HTML](https://arxiv.org/html/2602.14452)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe50b39e-96ef-4db4-9245-8f00d88e7e50",
  "isSidechain": true,
  "agentId": "a5e7811df73ba992a",
  "requestId": "req_011CawiZdPQkwtsFHfhs23tH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54ab82d8-0b50-4a61-897d-0e183fa5726b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmhMadZ4dqueXvmktWyXEJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 17574,
      "output_tokens": 2337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2337,
          "cache_read_input_tokens": 17574,
          "cache_creation_input_tokens": 2809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2809,
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
