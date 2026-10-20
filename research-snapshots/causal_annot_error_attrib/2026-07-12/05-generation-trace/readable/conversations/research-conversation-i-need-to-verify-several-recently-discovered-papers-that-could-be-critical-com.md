# Research conversation: I need to verify several recently discovered papers that could be critical competing work for an ML paper idea about det

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab9a7331924632daa.jsonl`
- **Structured JSON:** [`96ff7701586fc629379f.json`](../../sessions/96/96ff7701586fc629379f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-16T10:04:38.032Z_

I need to verify several recently discovered papers that could be critical competing work for an ML paper idea about detecting high-confidence hallucinations via output logit KL after perturbation at intermediate layers. Use WebSearch and WebFetch to verify these:

1. "Attractor Geometry of Transformer Memory" arxiv 2605.05686 - This paper allegedly argues that output logit gaps are fundamentally blind to high-confidence hallucinations because the frozen LM head cannot distinguish failure states. Fetch the arxiv page and read the abstract carefully. Does it actually make this claim? This would be a DIRECT theoretical objection to the LSP proposal.

2. "Between the Layers Lies the Truth: Uncertainty Estimation Using Intra-Layer Local Information Scores" arxiv 2603.22299 - Does this paper exist? What does it do? Does it compute pairwise KL divergence between layers?

3. "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (CCPS) arxiv 2505.21772 - Does this exist? Is it at EMNLP 2025? Does it perturb hidden states and use a classifier?

4. "Detecting Hallucinations via Internal Attention Divergence Signals" arxiv 2605.05025 - Does this exist? Does it find that middle-layer dynamics provide hallucination signals?

5. "Hallucination Basins" arxiv 2604.04743 - This paper is cited in the proposal. Does it exist? What does it propose?

6. Search "In-Context Sharpness as Alerts hallucination ICML 2024 arxiv 2403.01548" - does this paper exist and what does it do? It's cited in the proposal as an ICML 2024 paper.

For papers 1 and 6, please use WebFetch to read the actual arxiv abstract, as these are the most critical.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "4222912b-3df3-4883-9a80-5681f3d68ea5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:04:38.035Z_

```json
{
  "parentUuid": "4222912b-3df3-4883-9a80-5681f3d68ea5",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
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
  "uuid": "b24f6745-a7ab-4085-9e7e-1581325eccf9",
  "timestamp": "2026-05-16T10:04:38.035Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T10:04:41.092Z_



I'll start by searching for and fetching these papers in parallel. Let me load the WebSearch and WebFetch tools first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b24f6745-a7ab-4085-9e7e-1581325eccf9",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64Myom78ihwFXKd1EkQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7a1ba37-d13c-4c66-8234-2d586d83846e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcHrzkBJu78HQwNSLdDpTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 998,
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

_source line 4 · 2026-05-16T10:04:41.189Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018k8f8ixWUb23EahVLKKgHk`</summary>

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
  "parentUuid": "b7a1ba37-d13c-4c66-8234-2d586d83846e",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64Myom78ihwFXKd1EkQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f654f8-e3a6-4848-937f-c5149de89473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcHrzkBJu78HQwNSLdDpTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 998,
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

### Tool result

_source line 5 · 2026-05-16T10:04:41.192Z_

<details><summary>↩ Tool result · `toolu_018k8f8ixWUb23EahVLKKgHk`</summary>

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
  "parentUuid": "56f654f8-e3a6-4848-937f-c5149de89473",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "f4d23c4d-1473-4b7b-bdd2-be33f6f9d542",
  "sourceToolAssistantUUID": "56f654f8-e3a6-4848-937f-c5149de89473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T10:04:44.200Z_



Now let me launch all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d23c4d-1473-4b7b-bdd2-be33f6f9d542",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "119f0adf-9f59-4341-b9c1-c7a1c1072708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 7 · 2026-05-16T10:04:45.841Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V5LTL99WdgfjyXstMM4UtW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05686",
  "prompt": "Read the full abstract of this paper carefully. What is the paper's title? What does it argue? Does it claim that output logit gaps are fundamentally blind to high-confidence hallucinations? Does it discuss the frozen LM head being unable to distinguish failure states? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "119f0adf-9f59-4341-b9c1-c7a1c1072708",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ccb2084-c1a9-4976-baa9-a78a0c66e64a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 8 · 2026-05-16T10:04:47.099Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YBFGu3zpe6zAdkjreFUhYA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22299",
  "prompt": "What is the title of this paper? Read the abstract carefully. Does this paper compute pairwise KL divergence between layers? What method does it propose for uncertainty estimation? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ccb2084-c1a9-4976-baa9-a78a0c66e64a",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ff6793-62a5-4687-9951-cde4c1fb6e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 9 · 2026-05-16T10:04:48.495Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0185yzftaGuz9AWoMAiM1Be6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21772",
  "prompt": "What is the title of this paper? Does it exist? Read the abstract. Does it involve perturbing hidden states and using a classifier? Is there any mention of EMNLP 2025? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ff6793-62a5-4687-9951-cde4c1fb6e07",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e89137d-b6fc-4cb6-abf4-0095262624a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 10 · 2026-05-16T10:04:49.652Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HZzWYRSRPwDaaH9NSk4er3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05025",
  "prompt": "What is the title of this paper? Does it exist? Read the abstract. Does it discuss internal attention divergence signals for detecting hallucinations? Does it find that middle-layer dynamics provide hallucination signals? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e89137d-b6fc-4cb6-abf4-0095262624a5",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2b99eb0-6ffd-412a-9cc7-3c8eaea4d722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 11 · 2026-05-16T10:04:50.613Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DcaQxrpQ8KyGXQRwFGDfWp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04743",
  "prompt": "What is the title of this paper? Does it exist? Read the abstract. Does it discuss \"hallucination basins\"? What does it propose? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b99eb0-6ffd-412a-9cc7-3c8eaea4d722",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c490f81f-f4b9-4b27-a7a9-b8079ff7a1c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

### Tool result

_source line 12 · 2026-05-16T10:04:50.938Z_

<details><summary>↩ Tool result · `toolu_01V5LTL99WdgfjyXstMM4UtW`</summary>

```text
# Paper Summary

**Title:** "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination"

## What It Argues

The paper presents a geometric framework explaining how language models fail confidently. It proposes that learned facts create "attractor basins" in hidden-state space. Two distinct failure modes emerge: conflict (when parametric and working memory clash) and hallucination (when facts were never learned). Crucially, both produce confident outputs regardless.

## On Output-Based Monitoring

Yes, the paper explicitly claims output entropy cannot reliably detect these failures. As stated: "Both produce confident output regardless, making output-based monitoring blind by design."

## On the Frozen LM Head

Yes, the paper directly addresses this: "The frozen LM head, designed for next-token prediction, cannot distinguish these cases and fires confidently either way." It further argues this limitation "systematically erases" epistemic state information encoded in hidden states, with the erasure worsening at scale.

## Complete Abstract

The full abstract appears above in the source document, beginning with "Language models draw on two knowledge sources..." and concluding with "...and this erasure worsens with scale."

The authors propose geometric margin—measuring distance to the nearest memorized basin—as a superior detection method compared to entropy-based approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ccb2084-c1a9-4976-baa9-a78a0c66e64a",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "bf85de96-db3b-4723-abdb-1facaf90a877",
  "sourceToolAssistantUUID": "7ccb2084-c1a9-4976-baa9-a78a0c66e64a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T10:04:51.428Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012xiDK58Q1UUW2cpw6hASHu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.01548",
  "prompt": "What is the title of this paper? Does it exist? Read the abstract. Does it discuss \"in-context sharpness\" and hallucination? Is it related to ICML 2024? Provide the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf85de96-db3b-4723-abdb-1facaf90a877",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a52008d9-3408-4a65-acf1-fd7c19f4ac00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 14 · 2026-05-16T10:04:52.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XF9KzUBhoNRJtBxmWuTW1d`</summary>

```json
{
  "query": "arxiv 2605.05686 \"Attractor Geometry of Transformer Memory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a52008d9-3408-4a65-acf1-fd7c19f4ac00",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dccc3cd-f7e1-4eb7-9a96-605b40f07020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

### Tool result

_source line 15 · 2026-05-16T10:04:53.833Z_

<details><summary>↩ Tool result · `toolu_01YBFGu3zpe6zAdkjreFUhYA`</summary>

```text
# Paper Analysis

**Title:** "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores"

**Does it compute pairwise KL divergence between layers?**
No, the abstract does not mention KL divergence. The paper focuses on "cross-layer agreement patterns in internal representations."

**Proposed Method:**
The authors propose "a compact, per-instance UE method that scores cross-layer agreement patterns in internal representations using a single forward pass." Rather than computing divergence metrics, it examines how different layers align in their uncertainty encoding.

**Complete Abstract:**
"Large language models (LLMs) are often confidently wrong, making reliable uncertainty estimation (UE) essential. Output-based heuristics are cheap but brittle, while probing internal representations is effective yet high-dimensional and hard to transfer. We propose a compact, per-instance UE method that scores cross-layer agreement patterns in internal representations using a single forward pass. Across three models, our method matches probing in-distribution, with mean diagonal differences of at most $-1.8$ AUPRC percentage points and $+4.9$ Brier score points. Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to $+2.86$ AUPRC and $+21.02$ Brier points. Under 4-bit weight-only quantization, it remains robust, improving over probing by $+1.94$ AUPRC points and $+5.33$ Brier points on average. Beyond performance, examining specific layer--layer interactions reveals differences in how disparate models encode uncertainty. Altogether, our UE method offers a lightweight, compact means to capture transferable uncertainty in LLMs."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9ff6793-62a5-4687-9951-cde4c1fb6e07",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "c021807a-5628-4e76-8731-d00daeca43d4",
  "sourceToolAssistantUUID": "f9ff6793-62a5-4687-9951-cde4c1fb6e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:04:53.890Z_

<details><summary>↩ Tool result · `toolu_0185yzftaGuz9AWoMAiM1Be6`</summary>

```text
# Paper Summary

**Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

**Existence:** Yes, this paper exists as arXiv:2505.21772.

**Hidden State Perturbation & Classifier:** Yes, the method does involve this approach. According to the abstract, CCPS "applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness."

**EMNLP 2025 Mention:** There is no mention of EMNLP 2025 in the provided content.

**Complete Abstract:**

"Miscalibration in Large Language Models (LLMs) undermines their reliability, highlighting the need for accurate confidence estimation. We introduce CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability), a novel method analyzing internal representational stability in LLMs. CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats. Our results show that CCPS significantly outperforms current approaches. Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method. CCPS delivers an efficient, broadly applicable, and more accurate solution for estimating LLM confidence, thereby improving their trustworthiness."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e89137d-b6fc-4cb6-abf4-0095262624a5",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "592b6da1-22a9-4833-891b-df3c26ff6f4c",
  "sourceToolAssistantUUID": "3e89137d-b6fc-4cb6-abf4-0095262624a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T10:04:54.178Z_

<details><summary>↩ Tool result · `toolu_01HZzWYRSRPwDaaH9NSk4er3`</summary>

```text
# Paper Analysis

**Title:** "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals"

**Existence:** Yes, this paper exists on arXiv (identifier 2605.05025), submitted May 6, 2026.

**Internal Attention Divergence:** Yes, the paper directly addresses this topic. The authors propose measuring "Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution" to detect hallucinations.

**Middle-Layer Dynamics:** Yes, the findings confirm this. The abstract states: "This signal is concentrated in middle layers and on factual tokens such as named entities and numbers."

**Complete Abstract:**

"We propose a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models. The method uses attention matrices to estimate uncertainty without requiring repeated sampling or external models. Specifically, we measure the Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution, and use these features in a logistic regression probe. Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. We find that this signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable white-box signal of model uncertainty."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b99eb0-6ffd-412a-9cc7-3c8eaea4d722",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "3fd60f4a-7b7a-45d5-8a53-fa002228b77d",
  "sourceToolAssistantUUID": "c2b99eb0-6ffd-412a-9cc7-3c8eaea4d722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T10:04:54.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DeTuF9TKPJGaw5Bgjy6n9p`</summary>

```json
{
  "query": "arxiv 2603.22299 \"Between the Layers Lies the Truth\" uncertainty estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fd60f4a-7b7a-45d5-8a53-fa002228b77d",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b09b4ddc-b068-404f-b41c-cba66f924add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 19 · 2026-05-16T10:04:54.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTuoZhy68ceESAUN6SZgEf`</summary>

```json
{
  "query": "arxiv 2505.21772 \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b09b4ddc-b068-404f-b41c-cba66f924add",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c16da42b-ad24-4c8c-89ed-8e1ac5f6b2a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 20 · 2026-05-16T10:04:54.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3FRbouUPJNbmnkw1AaV1Z`</summary>

```json
{
  "query": "arxiv 2605.05025 \"Detecting Hallucinations via Internal Attention Divergence Signals\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c16da42b-ad24-4c8c-89ed-8e1ac5f6b2a6",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b230407a-0c35-4eb5-b032-444de583ebd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 21 · 2026-05-16T10:04:54.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GK7Vfpomp6wDvyQk7ReEZm`</summary>

```json
{
  "query": "arxiv 2604.04743 \"Hallucination Basins\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b230407a-0c35-4eb5-b032-444de583ebd3",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "910c0711-6da5-48db-8c8e-cf400178612f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "output_tokens": 1059,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1059,
          "cache_read_input_tokens": 9221,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1917,
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

### Tool call

_source line 22 · 2026-05-16T10:04:54.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DGrEEvaGjnGga9smz1CA2C`</summary>

```json
{
  "query": "\"In-Context Sharpness\" hallucination ICML 2024 arxiv 2403.01548"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "910c0711-6da5-48db-8c8e-cf400178612f",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64NETZrxN8RcXqiBwQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c87679d5-fee1-455d-b31c-78dc4ba710b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCoGsf3nTxirLoxH2rDRp8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9221,
      "output_tokens": 1059,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1059,
          "cache_read_input_tokens": 9221,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1917,
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

_source line 23 · 2026-05-16T10:04:55.893Z_

<details><summary>↩ Tool result · `toolu_01DcaQxrpQ8KyGXQRwFGDfWp`</summary>

```text
# Paper Analysis

**Title:** "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations"

**Does it exist?** Yes, this paper exists on arXiv (submitted April 6, 2026).

**Does it discuss "hallucination basins"?** Yes, extensively. The framework centers on this concept.

**What it proposes:** The authors introduce a geometric dynamical systems approach for understanding how LLMs generate factually incorrect outputs. Their key innovation involves analyzing how different task types create distinct structural patterns in the model's internal representations.

**Complete Abstract:**

"Large language models (LLMs) hallucinate: they produce fluent outputs that are factually incorrect. We present a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space. Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, we find that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap. We formalize this behavior with task-complexity and multi-basin theorems, characterize basin emergence in L-layer transformers, and show that geometry-aware steering can reduce hallucination probability without retraining."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c490f81f-f4b9-4b27-a7a9-b8079ff7a1c5",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "1f574893-8cac-4b49-9dbd-75c8d6f75bb3",
  "sourceToolAssistantUUID": "c490f81f-f4b9-4b27-a7a9-b8079ff7a1c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T10:04:57.109Z_

<details><summary>↩ Tool result · `toolu_012xiDK58Q1UUW2cpw6hASHu`</summary>

```text
# Paper Analysis

**Title:** Yes, the paper exists with the title "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation"

**In-Context Sharpness & Hallucination:** Yes, the abstract directly addresses both concepts. The researchers discovered that "correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to the incorrect ones."

**ICML 2024 Connection:** The page does not indicate this paper is related to ICML 2024. It's an arXiv submission from March 2024 in the cs.CL category.

**Complete Abstract:**

"Large language models (LLMs) frequently hallucinate and produce factual errors, yet our understanding of why they make these errors remains limited. In this study, we delve into the underlying mechanisms of LLM hallucinations from the perspective of inner representations, and discover a salient pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to the incorrect ones. Leveraging this insight, we propose an entropy-based metric to quantify the 'sharpness' among the in-context hidden states and incorporate it into the decoding process to formulate a constrained decoding approach. Experiments on various knowledge-seeking and hallucination benchmarks demonstrate our approach's consistent effectiveness, for example, achieving up to an 8.6 point improvement on TruthfulQA. We believe this study can improve our understanding of hallucinations and serve as a practical solution for hallucination mitigation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a52008d9-3408-4a65-acf1-fd7c19f4ac00",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "05efbf32-1af4-4bbf-beca-e2f9d9c94108",
  "sourceToolAssistantUUID": "a52008d9-3408-4a65-acf1-fd7c19f4ac00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T10:04:59.230Z_

<details><summary>↩ Tool result · `toolu_01PTuoZhy68ceESAUN6SZgEf`</summary>

```text
Web search results for query: "arxiv 2505.21772 "Calibrating LLM Confidence by Probing Perturbed Representation Stability""

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://bytez.com/docs/arxiv/2505.21772/paper"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://www.alphaxiv.org/resources/2505.21772v2"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"}]

I found the paper for you! Here's what the search revealed about arxiv paper 2505.21772:

## Paper Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

## Problem Addressed

Miscalibration in Large Language Models (LLMs) undermines their reliability, highlighting the need for accurate confidence estimation.

## Methodology

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

## Experimental Evaluation

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

## Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points.

The paper was published on arXiv on May 27, 2025, and has since been accepted to the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c16da42b-ad24-4c8c-89ed-8e1ac5f6b2a6",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "27af830f-44f6-4750-81ac-39f1998a6cf4",
  "sourceToolAssistantUUID": "c16da42b-ad24-4c8c-89ed-8e1ac5f6b2a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T10:05:00.273Z_

<details><summary>↩ Tool result · `toolu_01XF9KzUBhoNRJtBxmWuTW1d`</summary>

```text
Web search results for query: "arxiv 2605.05686 "Attractor Geometry of Transformer Memory""

Links: [{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"[2605.12466] Solve the Loop: Attractor Models for Language and Reasoning","url":"https://arxiv.org/abs/2605.12466"},{"title":"The Bayesian Geometry of Transformer Attention","url":"https://arxiv.org/html/2512.22471v1"},{"title":"Understanding and controlling the geometry of memory organization in RNNs","url":"https://arxiv.org/html/2502.07256v1"},{"title":"Transformers learn factored representations","url":"https://arxiv.org/html/2602.02385v1"},{"title":"Revisiting Transformer Layer Parameterization Through Causal Energy Minimization","url":"https://arxiv.org/html/2605.07588"},{"title":"Self-attention as an attractor network: transient memories without backpropagation M. N. acknowledges the support of PNRR MUR Project No. PE0000013-FAIR.","url":"https://arxiv.org/html/2409.16112v1"},{"title":"Back to the Continuous Attractor","url":"https://arxiv.org/html/2408.00109v2"},{"title":"Predicting Atomistic Transitions with Transformers","url":"https://arxiv.org/html/2603.06526v1"}]

I found the paper! Here's what I found about arxiv 2605.05686:

## "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination"

The paper is authored by Qiyao Liang (MIT), Risto Miikkulainen (University of Texas Austin), and Ila Fiete (MIT), and was submitted on May 7, 2026.

### Main Contribution

Language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM). The paper studies two mechanistically distinct failure modes—conflict, when PM and WM disagree and interfere; and hallucination, when the queried fact was never learned.

### Key Findings

The authors show both failures share a unified geometric account, where in the hidden-state space of autoregressive generation, learned facts form attractor basins. Conflict is basin competition: WM disrupts convergence to the correct basin without raising output entropy, while hallucination is basin absence: the hidden state drifts freely when no memorized basin exists.

### Experimental Approach

The researchers verify this account in a controlled synthetic task—entity identifiers mapped to unique codes with PM installed via LoRA adapters—where ground truth is exact. Geometric margin—the hidden state's distance to the nearest memorized basin—reads this geometry directly and separates correct recall from hallucination far more cleanly than output entropy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dccc3cd-f7e1-4eb7-9a96-605b40f07020",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "f8afe848-1a67-4720-9cf3-6fcb5467a342",
  "sourceToolAssistantUUID": "8dccc3cd-f7e1-4eb7-9a96-605b40f07020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T10:05:01.093Z_

<details><summary>↩ Tool result · `toolu_01M3FRbouUPJNbmnkw1AaV1Z`</summary>

```text
Web search results for query: "arxiv 2605.05025 "Detecting Hallucinations via Internal Attention Divergence Signals""

Links: [{"title":"[2605.05025] Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/abs/2605.05025"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"Representation-based Broad Hallucination Detectors Fail to Generalize Out of Distribution","url":"https://arxiv.org/html/2509.19372v1"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v2"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence","url":"https://arxiv.org/html/2412.13949"},{"title":"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck","url":"https://arxiv.org/html/2601.05547"}]

I found the paper! Here are the details about arxiv 2605.05025:

**Title:** Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals

**Author:** Gijs van Dijk from Utrecht University

**Submission Date:** May 6, 2026

**Summary:**

The paper proposes a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models using attention matrices to estimate uncertainty without requiring repeated sampling or external models.

**Key Methodology:**

The method measures the Kullback–Leibler divergence between each attention head's distribution and a uniform reference distribution, and uses these features in a logistic regression probe.

**Results and Findings:**

Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. Additionally, the signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable white-box signal of model uncertainty.

You can access the paper directly at https://arxiv.org/abs/2605.05025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b230407a-0c35-4eb5-b032-444de583ebd3",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "8a300847-7855-4a1b-b4a7-d04ee827b8f6",
  "sourceToolAssistantUUID": "b230407a-0c35-4eb5-b032-444de583ebd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T10:05:01.266Z_

<details><summary>↩ Tool result · `toolu_01GK7Vfpomp6wDvyQk7ReEZm`</summary>

```text
Web search results for query: "arxiv 2604.04743 "Hallucination Basins""

Links: [{"title":"[2604.04743] Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/abs/2604.04743"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Hallucination, Abstention, and Recursive Inseparability","url":"https://arxiv.org/html/2604.28067"},{"title":"HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models","url":"https://arxiv.org/html/2310.14566v5"},{"title":"[2604.00983] ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration","url":"https://arxiv.org/abs/2604.00983"},{"title":"[2604.17982] Mitigating Multimodal Hallucination via Phase-wise Self-reward","url":"https://arxiv.org/abs/2604.17982"},{"title":"[2401.01313] A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models","url":"https://arxiv.org/abs/2401.01313"},{"title":"[2604.19765] Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs","url":"https://arxiv.org/abs/2604.19765"}]

I found the paper arxiv 2604.04743 "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations" by Kalyan Cherukuri and Lav R. Varshney, published on April 6, 2026.

## Summary

The paper presents a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space.

### Key Findings

Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, the researchers find that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap.

### Main Contributions

The authors formalize this behavior with task-complexity and multi-basin theorems, characterize basin emergence in L-layer transformers, and show that geometry-aware steering can reduce hallucination probability without retraining.

The paper reframes LLM hallucinations as a dynamical systems phenomenon involving attractor-like basins in latent space, offering both theoretical characterization and practical steering methods to mitigate hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "910c0711-6da5-48db-8c8e-cf400178612f",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "31fbc61c-2f7c-49c6-98f1-02b1d67103a0",
  "sourceToolAssistantUUID": "910c0711-6da5-48db-8c8e-cf400178612f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T10:05:01.651Z_

<details><summary>↩ Tool result · `toolu_01DGrEEvaGjnGga9smz1CA2C`</summary>

```text
Web search results for query: ""In-Context Sharpness" hallucination ICML 2024 arxiv 2403.01548"

Links: [{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"GitHub - hkust-nlp/Activation_Decoding: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024)","url":"https://github.com/hkust-nlp/Activation_decoding"},{"title":"In-Context Sharpness as Alerts: An Inner Representation...","url":"https://www.emergentmind.com/papers/2403.01548"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://paperreading.club/page?id=212632"},{"title":"[PDF] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/In-Context-Sharpness-as-Alerts:-An-Inner-for-Chen-Xiong/ed8f46f493abce9498851e647d900a4628f6ff7f"},{"title":"arXiv:2403.01548v3 [cs.CL] 12 Mar 2024","url":"https://arxiv.org/pdf/2403.01548"},{"title":"Enhancing Visual Reliance in Text Generation: A Bayesian Perspective on Mitigating Hallucination in Large Vision-Language Models","url":"https://arxiv.org/html/2505.19498v2"},{"title":"Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding","url":"https://arxiv.org/html/2502.01056v1"},{"title":"Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps","url":"https://arxiv.org/html/2407.07071v2"},{"title":"What are Models Thinking about? Understanding Large Language Model Hallucinations through Model Internal State Analysis","url":"https://arxiv.org/html/2502.13490v1"}]

I found the paper! Here's what I can tell you about "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation":

## Overview
The paper was submitted to arXiv on March 3, 2024, and was last revised on March 12, 2024. It appears in the proceedings as a 2024 work presented at a conference (referenced as ArXiv/ICML 2024).

## Key Findings
The research discovers a salient pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to the incorrect ones.

## Methodology
The paper introduces an entropy-based metric to quantify the sharpness of these activations, finding that lower entropy (sharper activations) is associated with more factual outputs. 

A new constrained decoding approach, named Activation Decoding, is proposed, utilizing the sharpness metric to improve the factuality of LLM outputs across multiple benchmarks.

## Authors and Implementation
The paper is authored by Shiqi Chen, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, and Junxian He. The code is available on GitHub at the hkust-nlp/Activation_Decoding repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c87679d5-fee1-455d-b31c-78dc4ba710b7",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "497322f3-6d69-40be-922b-2213b7415a32",
  "sourceToolAssistantUUID": "c87679d5-fee1-455d-b31c-78dc4ba710b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:05:02.105Z_

<details><summary>↩ Tool result · `toolu_01DeTuF9TKPJGaw5Bgjy6n9p`</summary>

```text
Web search results for query: "arxiv 2603.22299 "Between the Layers Lies the Truth" uncertainty estimation"

Links: [{"title":"[2603.22299] Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/abs/2603.22299"},{"title":"Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/html/2603.22299"},{"title":"Between the Layers Lies the Truth:","url":"https://arxiv.org/pdf/2603.22299"},{"title":"Enhancing Accuracy of Uncertainty Estimation in Appearance-based Gaze Tracking with Probabilistic Evaluation and Calibration","url":"https://arxiv.org/html/2501.14894v4"},{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/html/2601.14210v2"},{"title":"Confidence Matters: Uncertainty Quantification and Precision Assessment of Deep Learning-based CMR Biomarker Estimates Using Scan-rescan Data","url":"https://arxiv.org/html/2603.26789"},{"title":"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups","url":"https://arxiv.org/html/2512.10294"},{"title":"[2603.10731] Beyond Accuracy: Reliability and Uncertainty Estimation in Convolutional Neural Networks","url":"https://arxiv.org/abs/2603.10731"},{"title":"[2603.20000] Monte Carlo conformal prediction for quantifying uncertainty in radio galaxy classification under ambiguous ground truth","url":"https://arxiv.org/abs/2603.20000"},{"title":"Contents","url":"https://arxiv.org/html/2603.06634"}]

I found the paper! Here's what the search revealed:

"Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores" (arxiv 2603.22299) is a recent paper submitted on March 17, 2026 by Zvi N. Badash, Yonatan Belinkov, and Moti Freiman.

**Main Contribution:**
The paper addresses the problem that large language models are often confidently wrong, and proposes a compact, per-instance uncertainty estimation method that scores cross-layer agreement patterns in internal representations using a single forward pass.

**Key Results:**
- Across three models, their method matches probing in-distribution, with mean diagonal differences of at most -1.8 AUPRC percentage points and +4.9 Brier score points
- Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to +2.86 AUPRC and +21.02 Brier points
- Under 4-bit weight-only quantization, it remains robust, improving over probing by +1.94 AUPRC points and +5.33 Brier points on average

You can access the full paper at https://arxiv.org/abs/2603.22299


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b09b4ddc-b068-404f-b41c-cba66f924add",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "ab9a7331924632daa",
  "type": "user",
  "uuid": "14ab3b39-a17e-4cbd-a545-c53df8beb47b",
  "sourceToolAssistantUUID": "b09b4ddc-b068-404f-b41c-cba66f924add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T10:05:47.990Z_

Here are the detailed verification results for all six papers:

---

## Paper 1: "Attractor Geometry of Transformer Memory" (arxiv 2605.05686)

**Status: EXISTS. The claimed theoretical objection is REAL.**

The paper is titled "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" by Qiyao Liang (MIT), Risto Miikkulainen (UT Austin), and Ila Fiete (MIT), submitted May 7, 2026.

The abstract confirms it **does** make the claimed argument. Specifically:
- It explicitly states that **"Both produce confident output regardless, making output-based monitoring blind by design."**
- It directly addresses the frozen LM head: **"The frozen LM head, designed for next-token prediction, cannot distinguish these cases and fires confidently either way."** It further argues this limitation "systematically erases" epistemic state information encoded in hidden states, with the erasure worsening at scale.
- The paper proposes **geometric margin** (distance to nearest memorized basin in hidden-state space) as a superior detection method compared to entropy-based approaches.

**This is indeed a direct theoretical objection to any LSP-style approach that relies on output logit divergence.** The paper argues that the LM head is fundamentally the wrong place to look because it collapses the rich epistemic geometry of hidden states into confident predictions regardless of whether the model is hallucinating or correct. However, note that their experiments use a **controlled synthetic task** (entity identifiers mapped to codes with LoRA adapters), not naturalistic benchmarks. This is a limitation you could potentially address in a rebuttal.

---

## Paper 2: "Between the Layers Lies the Truth" (arxiv 2603.22299)

**Status: EXISTS. It does NOT compute pairwise KL divergence between layers.**

The paper is titled "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores" by Zvi N. Badash, Yonatan Belinkov, and Moti Freiman, submitted March 17, 2026.

The method scores **cross-layer agreement patterns** in internal representations using a single forward pass. There is no mention of KL divergence in the abstract. It focuses on how different layers align in their uncertainty encoding, measuring this with a compact per-instance metric. It outperforms probing under cross-dataset transfer and quantization. This is **related work** (internal representations for uncertainty) but uses a different mechanism than pairwise KL between layers.

---

## Paper 3: "Calibrating LLM Confidence by Probing Perturbed Representation Stability" / CCPS (arxiv 2505.21772)

**Status: EXISTS. It IS at EMNLP 2025. It DOES perturb hidden states and use a classifier.**

The paper applies **targeted adversarial perturbations to final hidden states**, extracts features reflecting the model's response to these perturbations, and uses a **lightweight classifier** to predict answer correctness. Evaluated on LLMs from 8B to 32B parameters. The search results confirm it was published in the [ACL Anthology as EMNLP 2025 Main proceedings (paper 530)](https://aclanthology.org/2025.emnlp-main.530/).

**This is highly relevant competing work.** The key difference from LSP would be: CCPS perturbs **final** hidden states with adversarial perturbations and trains a classifier, whereas LSP (presumably) perturbs **intermediate** layers and measures output logit KL divergence directly. But the general idea of "perturb representations, measure stability" is shared.

---

## Paper 4: "Detecting Hallucinations via Internal Attention Divergence Signals" (arxiv 2605.05025)

**Status: EXISTS. It DOES find middle-layer signals.**

Full title: "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" by Gijs van Dijk (Utrecht University), submitted May 6, 2026.

The method measures **KL divergence between each attention head's distribution and a uniform reference distribution**, then feeds these features into a logistic regression probe. The abstract explicitly states: **"This signal is concentrated in middle layers and on factual tokens such as named entities and numbers."** This is relevant related work but uses attention distributions (not hidden-state perturbation or output logit KL).

---

## Paper 5: "Hallucination Basins" (arxiv 2604.04743)

**Status: EXISTS.**

Full title: "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations" by Kalyan Cherukuri and Lav R. Varshney, submitted April 6, 2026.

It proposes a geometric dynamical systems framework where hallucinations arise from **task-dependent basin structure in latent space**. Key finding: separability is strongly task-dependent -- factoid settings show clearer basin separation, while summarization and misconception-heavy settings overlap. They formalize this with task-complexity and multi-basin theorems and show that **geometry-aware steering** can reduce hallucination probability without retraining. This paper is thematically related to Paper 1 (both use geometric/basin frameworks in hidden-state space).

---

## Paper 6: "In-Context Sharpness as Alerts" (arxiv 2403.01548)

**Status: EXISTS. It IS an ICML 2024 paper.**

Full title: "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation" by Shiqi Chen, Miao Xiong, Junteng Liu, Zhengxuan Wu, Teng Xiao, Siyang Gao, and Junxian He (HKUST). The GitHub repository for their code ([hkust-nlp/Activation_Decoding](https://github.com/hkust-nlp/Activation_decoding)) confirms it is an **ICML 2024** paper.

The key finding: **correct generations tend to have sharper context activations in the hidden states of in-context tokens** compared to incorrect ones. They propose an entropy-based metric to quantify this "sharpness" and incorporate it into a constrained decoding approach ("Activation Decoding"), achieving up to 8.6 point improvement on TruthfulQA.

---

## Summary of Critical Findings for Your LSP Proposal

1. **Most threatening**: Paper 1 (arxiv 2605.05686) is a genuine theoretical challenge. It directly argues that output logit monitoring is "blind by design" to high-confidence hallucinations because the frozen LM head erases epistemic information. However, it uses synthetic tasks only, and your approach (perturbing intermediate layers) may surface information that static output entropy misses -- you should argue that perturbation-based KL divergence is fundamentally different from static output entropy.

2. **Closest competing method**: Paper 3 (CCPS, arxiv 2505.21772) shares the core idea of "perturb representations and measure stability." It is published at EMNLP 2025. You must differentiate LSP clearly -- the distinction would be perturbation location (intermediate vs. final layers), perturbation type (noise vs. adversarial), and measurement (output logit KL vs. trained classifier).

3. **All six papers are real** -- none are fabricated citations. Papers 2, 4, and 5 are related but use different approaches. Paper 6 is correctly attributed to ICML 2024.

Sources:
- [Attractor Geometry of Transformer Memory (2605.05686)](https://arxiv.org/abs/2605.05686)
- [Between the Layers Lies the Truth (2603.22299)](https://arxiv.org/abs/2603.22299)
- [CCPS (2505.21772)](https://arxiv.org/abs/2505.21772)
- [CCPS at EMNLP 2025 - ACL Anthology](https://aclanthology.org/2025.emnlp-main.530/)
- [Detecting Hallucinations via Internal Attention Divergence (2605.05025)](https://arxiv.org/abs/2605.05025)
- [Hallucination Basins (2604.04743)](https://arxiv.org/abs/2604.04743)
- [In-Context Sharpness as Alerts (2403.01548)](https://arxiv.org/abs/2403.01548)
- [Activation Decoding GitHub (ICML 2024)](https://github.com/hkust-nlp/Activation_decoding)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ab3b39-a17e-4cbd-a545-c53df8beb47b",
  "isSidechain": true,
  "agentId": "ab9a7331924632daa",
  "requestId": "req_011Cb64Pkh2WcbqSfpXNw4kC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4633d485-643f-4f5f-bfbc-119981f85a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RER5oNhj8FoiYqYd5JfkS3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3517,
      "cache_creation_input_tokens": 5080,
      "cache_read_input_tokens": 11138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5080,
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
