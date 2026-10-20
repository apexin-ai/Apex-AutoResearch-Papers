# Research conversation: Use WebSearch to find the MOST RECENT papers (March-May 2026) on activation steering for hallucination reduction that mi

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1993c84ad2495b66.jsonl`
- **Structured JSON:** [`5ce8d51ec5907d42734a.json`](../../sessions/5c/5ce8d51ec5907d42734a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-16T08:48:11.827Z_

Use WebSearch to find the MOST RECENT papers (March-May 2026) on activation steering for hallucination reduction that might compete with a "geometry-triggered sentence-level steering" approach. I need to check if there are concurrent submissions the generator may have missed.

Search for:
1. "activation steering hallucination 2026" site:arxiv.org
2. "geometry-aware steering hallucination" 2026
3. "selective steering hallucination detection" 2026
4. "claim-level hallucination intervention decoding" 2026
5. "Mahalanobis distance hallucination steering" 2026
6. "sentence boundary steering LLM" 2026

Also search for:
7. "PCNet hallucination probabilistic circuits" to verify this paper (arxiv 2605.05953)
8. "HELIX tethered reasoning Mahalanobis" OR "arxiv 2602.17691" to verify this paper's actual mechanism

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "5010010f-cc16-4320-be4b-c7e15c73d0de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:48:11.829Z_

```json
{
  "parentUuid": "5010010f-cc16-4320-be4b-c7e15c73d0de",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
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
  "uuid": "5167a0fe-340c-4201-b0c8-8ae3d600314b",
  "timestamp": "2026-05-16T08:48:11.829Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T08:48:18.276Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QjEKbEQYJxpDTs73hAQTbe`</summary>

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
  "parentUuid": "5167a0fe-340c-4201-b0c8-8ae3d600314b",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xXurDaSnmDJWup76ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba44bf1c-f27a-4410-bf6e-f35cf7f56a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2ba2V9XAwTa4FVBK3ZY8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 774,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 4 · 2026-05-16T08:48:18.278Z_

<details><summary>↩ Tool result · `toolu_01QjEKbEQYJxpDTs73hAQTbe`</summary>

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
  "parentUuid": "ba44bf1c-f27a-4410-bf6e-f35cf7f56a7a",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "5226637c-6b03-4fb9-a574-8bbd2a2f769c",
  "sourceToolAssistantUUID": "ba44bf1c-f27a-4410-bf6e-f35cf7f56a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T08:48:21.837Z_

I'll search for all these queries to find recent competing papers. Let me run them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5226637c-6b03-4fb9-a574-8bbd2a2f769c",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xYPpiaUq9GD8xZJobM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6a163ef-e6a6-4b2c-b380-6dd6122246ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9RRbTpsEPtcCRTKoXzMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-16T08:48:22.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4EgCEya2gKtkj5tRRDtTx`</summary>

```json
{
  "query": "activation steering hallucination 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a163ef-e6a6-4b2c-b380-6dd6122246ca",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xYPpiaUq9GD8xZJobM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63bde2c1-d68a-49b7-94ed-3a992e15d199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9RRbTpsEPtcCRTKoXzMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-16T08:48:22.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DiswvVx65buj7HPGRiAev1`</summary>

```json
{
  "query": "\"geometry-aware steering hallucination\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63bde2c1-d68a-49b7-94ed-3a992e15d199",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xYPpiaUq9GD8xZJobM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8836f2e5-aac3-436b-800d-2b5fb87d0b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9RRbTpsEPtcCRTKoXzMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-16T08:48:23.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CfCcckJwJbhoBBdH9if8bB`</summary>

```json
{
  "query": "\"selective steering hallucination detection\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8836f2e5-aac3-436b-800d-2b5fb87d0b47",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xYPpiaUq9GD8xZJobM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9963bf36-4861-46c3-a356-58b59befa91d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9RRbTpsEPtcCRTKoXzMf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8997,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 8997,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-16T08:48:23.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014eZ2G3jDVnYgSGMJK9jSi9`</summary>

```json
{
  "query": "\"claim-level hallucination intervention decoding\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9963bf36-4861-46c3-a356-58b59befa91d",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xYPpiaUq9GD8xZJobM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2f77388-97a9-4729-9791-fefbe32dac57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9RRbTpsEPtcCRTKoXzMf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8997,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 8997,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 10 · 2026-05-16T08:48:28.760Z_

<details><summary>↩ Tool result · `toolu_01E4EgCEya2gKtkj5tRRDtTx`</summary>

```text
Web search results for query: "activation steering hallucination 2026 site:arxiv.org"

Links: [{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.06495"},{"title":"Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models","url":"https://arxiv.org/html/2511.10292"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"},{"title":"Prompt–Activation Duality: Improving Activation Steering via Attention-Level Interventions","url":"https://arxiv.org/html/2605.10664"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034"},{"title":"[2511.10292] Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models","url":"https://arxiv.org/abs/2511.10292"}]

I found several relevant papers from arxiv.org on activation steering and hallucination mitigation from 2026. Here are the key results:

## Recent 2026 Papers on Activation Steering and Hallucination

**1. Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models** (February 25, 2026)

This paper proposes Dynamic Multimodal Activation Steering, a training-free approach for hallucination mitigation. The research reveals that truthfulness and visual perception capabilities predominantly engage different subsets of attention heads within the model architecture, and truthfulness steering vectors vary significantly across different semantic contexts. The method constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors, enabling context-aware interventions during inference by dynamically selecting the most relevant steering vectors based on input semantic similarity and applying them to the most influential attention heads.

**2. COLD-FD: Activation Steering for Behavior Control** (March 5, 2026)

This paper appears to be published as a conference paper at ICLR 2026 and explores using activation steering to modulate hallucinations while maintaining fluency and relevance in language models.

**3. Additional Related Work**

Other 2026 papers in this space include work on Spherical Steering (geometric-aware activation rotation) and studies on how activation steering methods compare to prompt-based approaches for controlling model behavior.

All of these papers focus on inference-time interventions that avoid the computational cost of retraining while addressing hallucination problems in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63bde2c1-d68a-49b7-94ed-3a992e15d199",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "c76955eb-5fdc-4554-b848-b97ed377a917",
  "sourceToolAssistantUUID": "63bde2c1-d68a-49b7-94ed-3a992e15d199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T08:48:29.642Z_

<details><summary>↩ Tool result · `toolu_01DiswvVx65buj7HPGRiAev1`</summary>

```text
Web search results for query: ""geometry-aware steering hallucination" 2026"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313v1"},{"title":"Steering Vector Fields for Context-Aware Inference-Time ...","url":"https://www.arxiv.org/pdf/2602.01654"},{"title":"Latent Space Steering Techniques","url":"https://www.emergentmind.com/topics/latent-space-steering"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=YtWZdwEG5K"},{"title":"Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction | Request PDF","url":"https://www.researchgate.net/publication/403683244_Mitigating_Entangled_Steering_in_Large_Vision-Language_Models_for_Hallucination_Reduction"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"}]

Based on the search results, I found several relevant papers related to "geometry-aware steering" and hallucination mitigation in 2026:

## Key Research Findings

**Spherical Steering: Geometry-Aware Activation Rotation**

Spherical Steering is a training-free primitive that resolves the trade-off between controlling language models and maintaining generation quality through activation rotation, rotating activations along a geodesic toward a target direction while preserving signal integrity. This approach significantly outperforms addition-based baselines by notably +10% on TruthfulQA, COPA, and Storycloze, while maintaining the model's general open-ended generation quality.

**Curveball Steering: Nonlinear Geometry-Aware Approach**

Research analyzing the intrinsic geometry of LLM activation spaces revealed substantial and concept-dependent geometric distortions, leading to the proposal of "Curveball steering," a nonlinear steering method based on polynomial kernel PCA. Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion.

**Dynamic Multimodal Activation Steering for Vision-Language Models**

Research on Large Vision-Language Models found that truthfulness and visual perception engage different attention head subsets, and steering vectors vary across semantic contexts, leading to Dynamic Multimodal Activation Steering, a training-free approach that constructs semantic-based truthfulness steering vector databases and enables context-aware interventions.

These papers represent the cutting edge of geometry-aware steering techniques for addressing hallucination in language and vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8836f2e5-aac3-436b-800d-2b5fb87d0b47",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "5c7e2390-4e57-4c60-a1c2-f347af043559",
  "sourceToolAssistantUUID": "8836f2e5-aac3-436b-800d-2b5fb87d0b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T08:48:30.351Z_

<details><summary>↩ Tool result · `toolu_01CfCcckJwJbhoBBdH9if8bB`</summary>

```text
Web search results for query: ""selective steering hallucination detection" 2026"

Links: [{"title":"Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction | Request PDF","url":"https://www.researchgate.net/publication/403683244_Mitigating_Entangled_Steering_in_Large_Vision-Language_Models_for_Hallucination_Reduction"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"[2604.07914] Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction","url":"https://arxiv.org/abs/2604.07914"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"REVIS: Sparse Latent Steering to Mitigate Object Hallucination in Large","url":"https://arxiv.org/pdf/2602.11824"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention | Request PDF","url":"https://www.researchgate.net/publication/394298568_Activation_Steering_Decoding_Mitigating_Hallucination_in_Large_Vision-Language_Models_through_Bidirectional_Hidden_State_Intervention"},{"title":"[2605.04641] CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering","url":"https://arxiv.org/abs/2605.04641"},{"title":"Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering | OpenReview","url":"https://openreview.net/forum?id=LBl7Hez0fF"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention | Underline","url":"https://underline.io/lecture/121289-activation-steering-decoding-mitigating-hallucination-in-large-vision-language-models-through-bidirectional-hidden-state-intervention"}]

Based on the search results, here are the recent 2026 research developments on selective steering and hallucination detection:

## Key Research Areas

**Dynamic Multimodal Activation Steering (DMAS)**

Large Vision-Language Models (LVLMs) exhibit outstanding performance on vision-language tasks but struggle with hallucination problems. Through in-depth analysis of LVLM activation patterns, research reveals that truthfulness and visual perception capabilities predominantly engage different subsets of attention heads within the model architecture, and truthfulness steering vectors vary significantly across different semantic contexts. Based on these observations, Dynamic Multimodal Activation Steering is proposed as a training-free approach for hallucination mitigation. The method constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors, enabling context-aware interventions during inference by dynamically selecting the most relevant steering vectors based on input semantic similarity and applying them to the most influential attention heads.

**MESA Framework**

Existing methods mitigate hallucinations but often alter generation behavior, resulting in shorter outputs and shifted token distributions, especially in latent space steering approaches. The issue stems from entangled steering signals, where suppressing hallucinations inadvertently disrupts the model's intrinsic generation behavior. To address this, MESA is proposed as an effective plug-and-play framework that performs controlled and selective latent intervention for hallucination mitigation.

**Caption-Guided Visual Attention Steering (CAST)**

LVLMs' attention to visual information is significantly enhanced when answering caption queries compared to non-caption queries. Inspired by this phenomenon, CAST is a training-free, plug-and-play hallucination mitigation method that leverages the attention activation pattern corresponding to caption queries to enhance LVLMs' visual perception capability.

**REVIS Method**

REVIS utilizes orthogonal projection to extract purified visual vectors, and performs sparse intervention through calibration-based layer selection and inference-time dynamic risk-aware steering.

These approaches represent the forefront of 2026 research on using selective steering mechanisms to detect and mitigate hallucinations in large vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9963bf36-4861-46c3-a356-58b59befa91d",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "5f462c24-5cd2-4ee8-a398-fe6e055d6aef",
  "sourceToolAssistantUUID": "9963bf36-4861-46c3-a356-58b59befa91d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T08:48:32.017Z_

<details><summary>↩ Tool result · `toolu_014eZ2G3jDVnYgSGMJK9jSi9`</summary>

```text
Web search results for query: ""claim-level hallucination intervention decoding" 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Hallucination Mitigation: RAG, Decoding, and Training - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/hallucination-mitigation"},{"title":"InEx: Hallucination Mitigation via Introspection and Cross- ...","url":"https://arxiv.org/pdf/2512.02981"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"hallucination-mitigation · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination-mitigation"},{"title":"Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12425127/"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.pdf"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"}]

Based on the search results, here's what I found about claim-level hallucination intervention decoding in 2026:

## Recent Research on Hallucination Mitigation

The most promising systems now add span-level verification: each generated claim is matched against retrieved evidence and flagged if unsupported, as shown in the REFIND SemEval 2025 benchmark.

### Decoding-Based Intervention Approaches

Decoding-time control regulates token-level generation through logit calibration or uncertainty-based penalties. However, these techniques often generate overconfident yet unreliable outputs due to shallow, modality-unaware reasoning and poor uncertainty modeling.

### Recent Innovations

Recent 2026 work includes several approaches:

1. **Dynamic Multimodal Steering**: During inference, researchers dynamically retrieve the most semantically relevant truthfulness steering vector for the input query and apply both truthfulness and visual perception vectors to the top-K attention heads with the largest activation differences. This dual intervention effectively reduces hallucinations.

2. **Probabilistic Circuits**: PCNet, a Probabilistic Circuit trained as a tractable density estimator over a low-dimensional projection of the LLM's final hidden state, computes the exact Negative Log-Likelihood of any latent state. A high NLL identifies a hallucination trajectory as a geometric anomaly, and this signal gates PC-LDCD, a manifold-preserving intervention that performs a density-penalized lookahead search in the discrete vocabulary space.

3. **Attention Causal Decoding**: FarSight is a versatile plug-and-play decoding strategy that reduces attention interference from outlier tokens by optimizing the causal mask, and designs a dynamic register-attention distribution mechanism that explicitly optimizes attention allocation at each decoding step.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2f77388-97a9-4729-9791-fefbe32dac57",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "9b230a46-ecc6-4c24-8c78-4121c51898fa",
  "sourceToolAssistantUUID": "d2f77388-97a9-4729-9791-fefbe32dac57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T08:48:35.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4e1csWDQDHAEmZDSgX72o`</summary>

```json
{
  "query": "\"Mahalanobis distance hallucination steering\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b230a46-ecc6-4c24-8c78-4121c51898fa",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xZQ5d8KcbdMkBrQvvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efad11a9-c161-4faf-afd3-5f2a43b5e039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRPvoeBw4cHXgpGt9t7WCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 10389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4223,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 15 · 2026-05-16T08:48:35.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YFggoLwfJgH5P67PSSAq3z`</summary>

```json
{
  "query": "\"sentence boundary steering LLM\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efad11a9-c161-4faf-afd3-5f2a43b5e039",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xZQ5d8KcbdMkBrQvvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89f57a2b-c85e-4c10-ab0d-29e3aac6e546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRPvoeBw4cHXgpGt9t7WCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 10389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4223,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 16 · 2026-05-16T08:48:36.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013wo5Wom9bWG7nuBc3sFARU`</summary>

```json
{
  "query": "\"PCNet hallucination probabilistic circuits\" arxiv 2605.05953"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f57a2b-c85e-4c10-ab0d-29e3aac6e546",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xZQ5d8KcbdMkBrQvvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65802edb-0fbe-46c0-9b2c-c5097015b508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRPvoeBw4cHXgpGt9t7WCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 10389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4223,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 17 · 2026-05-16T08:48:37.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqKYWTzCepbu5C6dx2hgsN`</summary>

```json
{
  "query": "\"HELIX tethered reasoning Mahalanobis\" OR \"arxiv 2602.17691\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65802edb-0fbe-46c0-9b2c-c5097015b508",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xZQ5d8KcbdMkBrQvvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b091386-0dc2-4e36-bf71-ace8de6a0185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRPvoeBw4cHXgpGt9t7WCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 10389,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 10389,
          "cache_creation_input_tokens": 4223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4223,
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

_source line 18 · 2026-05-16T08:48:41.794Z_

<details><summary>↩ Tool result · `toolu_01E4e1csWDQDHAEmZDSgX72o`</summary>

```text
Web search results for query: ""Mahalanobis distance hallucination steering" 2026"

Links: [{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/html/2602.17691"},{"title":"[2602.17691] Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/abs/2602.17691"},{"title":"Decoupling Entropy from Hallucination in Quantized LLMs ...","url":"https://arxiv.org/pdf/2602.17691"},{"title":"Mahalanobis distance - Wikipedia","url":"https://en.wikipedia.org/wiki/Mahalanobis_distance"},{"title":"Mahalanobis Distance Uri Shaham April 13, 2026 1 Issues with Euclidean Distance","url":"https://u.cs.biu.ac.il/~shahamu/lecture%20notes%20pdf%20files/Mahalanobis.pdf"},{"title":"Detecting anomalies in unmanned vehicles using the Mahalanobis distance | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/5509781/"},{"title":"Mahalanobis distance | Resonance | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF02834632"},{"title":"Mahalanobis Distance: Simple Definition, Examples - Statistics How To","url":"https://www.statisticshowto.com/mahalanobis-distance/"},{"title":"Mahalanobis Distance-Based Supervised and Semi-Supervised Machine Learning Methods for Anomaly Detection in IoT Sensor Data | Bentham Science Publishers","url":"https://www.benthamdirect.com/content/journals/swcc/10.2174/0122103279403481251014104800"},{"title":"Bolster Hallucination Detection via Prompt-Guided Data Augmentation | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/41096"}]

Based on the web search results, I found relevant research on Mahalanobis distance, hallucination steering, and related topics from 2026. Here are the key findings:

## Recent Research on Hallucination Steering

A geometric framework called Helix decouples output entropy from hallucination by tethering hidden-state trajectories to a pre-computed truthfulness manifold, computing a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from the manifold.

High-temperature "hallucination" in quantized language models is primarily trajectory divergence—activations escaping structurally coherent regions of the representation space—rather than semantic collapse. When UTS indicates trajectory divergence, graduated steering vectors redirect activations toward structurally coherent regions while affecting only 0.2–2.5% of tokens.

## Performance Results

On 4-bit quantized Granite 4.0 H Small, Helix exceeds the full-precision baseline (91.80% vs 87.27% GSM8K), and MMLU maintains 72.49% accuracy across 14,042 questions (1.24pp degradation).

## Additional Applications

Another recent development involves a Contrastive Mahalanobis Score (CM Score) for evaluating the truthfulness of sparse intermediate embeddings produced by LLMs, based on modeling the distributions of truthful and hallucinated data in the activation space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efad11a9-c161-4faf-afd3-5f2a43b5e039",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "ae3101d4-8661-479d-ab25-cb66676ecdc0",
  "sourceToolAssistantUUID": "efad11a9-c161-4faf-afd3-5f2a43b5e039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T08:48:42.507Z_

<details><summary>↩ Tool result · `toolu_013wo5Wom9bWG7nuBc3sFARU`</summary>

```text
Web search results for query: ""PCNet hallucination probabilistic circuits" arxiv 2605.05953"

Links: [{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Computer Science Feb 2023","url":"http://arxiv.org/list/cs/2023-02?skip=2625&show=25"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=5650&show=25"},{"title":"A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/html/2406.06950v1"},{"title":"Probabilistic Guarantees for Reducing Contextual Hallucinations in LLMs","url":"https://arxiv.org/pdf/2601.00641"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2411.12256"},{"title":"Rethinking Probabilistic Circuit Parameter Learning","url":"https://arxiv.org/html/2505.19982v1"},{"title":"[2502.08663] Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/abs/2502.08663"}]

I found the paper! Here's what the search revealed:

PCNet is a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream that detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications.

The method exploits PCNet as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step, triggering PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

Across four LLMs ranging from 1B to 8B models and four benchmarks covering conversational reasoning, knowledge-intensive QA, reading comprehension, and truthfulness, PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA with AUROC reaching up to 99%, and PC-LDCD obtains the highest scores on TruthfulQA in three out of four models while reducing the mean corruption rate.

The paper was submitted to arXiv on May 7, 2026, by Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, and Giovanni Iacca from the University of Trento.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65802edb-0fbe-46c0-9b2c-c5097015b508",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "66d0bad1-fcde-4959-bca1-9b95fc8c03e0",
  "sourceToolAssistantUUID": "65802edb-0fbe-46c0-9b2c-c5097015b508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T08:48:43.411Z_

<details><summary>↩ Tool result · `toolu_01YFggoLwfJgH5P67PSSAq3z`</summary>

```text
Web search results for query: ""sentence boundary steering LLM" 2026"

Links: [{"title":"Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"},{"title":"The Complete Guide to LLM Steering: From Concepts to Code | by Adeel mukhtar | Medium","url":"https://medium.com/@adeelmukhtar051/the-complete-guide-to-llm-steering-from-concepts-to-code-5f72bed1992c"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour","url":"https://arxiv.org/pdf/2512.16602"},{"title":"Steering LLM Behavior Without Fine-Tuning – Frank's World of Data Science & AI","url":"https://www.franksworld.com/2026/01/20/steering-llm-behavior-without-fine-tuning/"},{"title":"A New Method to Steer AI Output Uncovers Vulnerabilities and Potential Improvements","url":"https://today.ucsd.edu/story/a-new-method-to-steer-ai-output-uncovers-vulnerabilities-and-potential-improvements"},{"title":"LLM Concept Vectors: MIT Research on Steering AI Behavior / Blogs / Perficient","url":"https://blogs.perficient.com/2026/02/26/llm-concept-vectors-research/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=steering+vector"},{"title":"EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering","url":"https://arxiv.org/html/2509.25175v1"},{"title":"[2308.10248] Activation Addition: Steering Language Models Without Optimization","url":"https://ar5iv.labs.arxiv.org/html/2308.10248"}]

Based on the search results, here's what I found about "sentence boundary steering LLM" in 2026:

## Overview of LLM Steering in 2026

LLM steering, also known as activation engineering or representation engineering, has become an active area of research. Steering works at a deeper level than prompts or fine-tuning—it manipulates the model's internal thought process as it generates text.

## Recent Advances (2026)

The field has seen rapid development in early 2026. January-February 2026 saw the field explode with new research, with several notable approaches emerging:

- **Steering Vector Fields**: Li et al. proposed Steering Vector Fields where instead of a static vector applied uniformly, they learn a differentiable scoring function whose gradient defines the steering direction at each activation.

- **SAE-Guided Steering**: Fang et al. proposed SAE-Steering for controlling reasoning strategies like backtracking and cross-verification, not just surface behaviors.

- **Concept Vectors**: Researchers from MIT and UC San Diego published a paper describing LLM concept vectors and an algorithm called the Recursive Feature Machine (RFM) that extracts patterns of neural activity corresponding to specific ideas or behaviors.

## Practical Applications

Steering vectors work well for some behaviors like refusal, sentiment, and formality, but fail for others like factual recall and complex reasoning. Steering can be used to improve LLM output, with research showing it improved LLM performance on narrow, precise tasks such as translating from Python to C++ code.

However, the search results don't contain specific information about "sentence boundary steering" as a particular technique. The results discuss steering methods in general but not this specific variant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89f57a2b-c85e-4c10-ab0d-29e3aac6e546",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "76e669d7-ea36-4bb5-9068-ea3c1498821d",
  "sourceToolAssistantUUID": "89f57a2b-c85e-4c10-ab0d-29e3aac6e546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T08:48:44.025Z_

<details><summary>↩ Tool result · `toolu_01UqKYWTzCepbu5C6dx2hgsN`</summary>

```text
Web search results for query: ""HELIX tethered reasoning Mahalanobis" OR "arxiv 2602.17691""

Links: [{"title":"[2602.17691] Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/abs/2602.17691"},{"title":"Decoupling Entropy from Hallucination in Quantized LLMs ...","url":"https://arxiv.org/pdf/2602.17691"},{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/html/2602.17691"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=651&show=50"},{"title":"[2507.17691] CASCADE: LLM-Powered JavaScript Deobfuscator at Google","url":"https://arxiv.org/abs/2507.17691"},{"title":"arXiv:2409.17691v1 [cs.LG] 26 Sep 2024","url":"https://arxiv.org/pdf/2409.17691"},{"title":"Efficient Bias Mitigation Without Privileged Information","url":"https://arxiv.org/html/2409.17691"},{"title":"[2406.17691] A sharp quantitative Alexandrov inequality and applications to volume preserving geometric flows in 3D","url":"https://arxiv.org/abs/2406.17691"},{"title":"[2501.17691] Non relativistic limit of the nonlinear Klein-Gordon equation: Uniform in time approximation of KAM solutions","url":"https://arxiv.org/abs/2501.17691"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?show=2000&skip=976"}]

I found the paper! Here are the search results for arxiv 2602.17691:

## Paper Details

The paper is titled "Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering" by Craig Atkinson.

## Overview

Quantized language models face a fundamental dilemma: low sampling temperatures yield repetitive, mode-collapsed outputs, while high temperatures (T > 2.0) cause trajectory divergence and semantic incoherence.

## The HELIX Framework

The paper presents HELIX, a geometric framework that decouples output entropy from hallucination by tethering hidden-state trajectories to a pre-computed truthfulness manifold. 

HELIX computes a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from the manifold. When UTS indicates trajectory divergence, graduated steering vectors redirect activations toward structurally coherent regions while affecting only 0.2-2.5% of tokens.

## Results

On 4-bit quantized Granite 4.0 H Small (32B/9B active, hybrid Mamba-Transformer): GSM8K maintains 88.84% accuracy at T = 3.0 (2.81pp degradation from T = 0.5); MMLU maintains 72.49% across 14,042 questions (1.24pp degradation).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b091386-0dc2-4e36-bf71-ace8de6a0185",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "e5ac19a0-e691-4ccd-b295-5637a56fc10d",
  "sourceToolAssistantUUID": "7b091386-0dc2-4e36-bf71-ace8de6a0185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-16T08:48:48.295Z_

Now let me search for a few more specific papers that appeared in the results to get more details on the most relevant competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ac19a0-e691-4ccd-b295-5637a56fc10d",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xaHRJi5bT1RAvweUyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e1c24e9-6661-427f-b072-def85bcd7ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyxFcgsRUzaRDsjCXkjsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 14612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
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

_source line 23 · 2026-05-16T08:48:49.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FjEdz8fd2y8SQivUMNCFL9`</summary>

```json
{
  "query": "arxiv 2602.08169 \"Spherical Steering\" geometry-aware activation rotation hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e1c24e9-6661-427f-b072-def85bcd7ade",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xaHRJi5bT1RAvweUyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fb4142c-a4c0-43db-96fd-79f09d4f83bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyxFcgsRUzaRDsjCXkjsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 14612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
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

_source line 24 · 2026-05-16T08:48:50.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AdoHo8NrpWr7o3nqL9qF8Y`</summary>

```json
{
  "query": "arxiv 2604.07914 \"Mitigating Entangled Steering\" MESA hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fb4142c-a4c0-43db-96fd-79f09d4f83bd",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xaHRJi5bT1RAvweUyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36fb3fbe-f3e6-46ee-b276-1227adad0c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyxFcgsRUzaRDsjCXkjsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 14612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
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

_source line 25 · 2026-05-16T08:48:51.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019yXAaFPKT2X9dLdAtiNmzW`</summary>

```json
{
  "query": "arxiv 2603.09313 \"Curveball Steering\" nonlinear geometry hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36fb3fbe-f3e6-46ee-b276-1227adad0c15",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xaHRJi5bT1RAvweUyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47ddc1df-a025-4556-b685-eef63dac46a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyxFcgsRUzaRDsjCXkjsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 14612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3784,
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

_source line 26 · 2026-05-16T08:48:51.566Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WPRJFCznpDC4Hu9EVFTJHk`</summary>

```json
{
  "query": "arxiv 2602.01654 \"Steering Vector Fields\" context-aware inference hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ddc1df-a025-4556-b685-eef63dac46a3",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xaHRJi5bT1RAvweUyz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0caf65d1-eff6-4074-a0fe-399c3739d739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uyxFcgsRUzaRDsjCXkjsw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3784,
      "cache_read_input_tokens": 14612,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 14612,
          "cache_creation_input_tokens": 3784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3784,
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

_source line 27 · 2026-05-16T08:48:55.527Z_

<details><summary>↩ Tool result · `toolu_01FjEdz8fd2y8SQivUMNCFL9`</summary>

```text
Web search results for query: "arxiv 2602.08169 "Spherical Steering" geometry-aware activation rotation hallucination"

Links: [{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"Publications","url":"https://hanjiechen.github.io/publication.html"},{"title":"Hanjie Chen's research works | Johns Hopkins University and other places","url":"https://www.researchgate.net/scientific-contributions/Hanjie-Chen-2260402100"},{"title":"Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"},{"title":"[2604.08169v1] Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/abs/2604.08169v1"},{"title":"ICML Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://icml.cc/virtual/2025/50230"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313v1"}]

I found the paper! Here are the details about arxiv 2602.08169:

**Title:** Spherical Steering: Geometry-Aware Activation Rotation for Language Models

**Authors:** Zejia You, Chunyuan Deng, and Hanjie Chen

**Submission Date:** Submitted on 9 Feb 2026

**Main Contribution:** The paper introduces Spherical Steering, a training-free primitive that resolves trade-offs through activation rotation, rotating activations along a geodesic toward a target direction to guide activation toward the target concept while preserving the integrity of the representations.

**Key Problem Addressed:** Standard inference-time steering approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.

**Publication Venue:** The paper is being presented at The Forty-Third International Conference on Machine Learning (ICML), Seoul, South Korea, July 2026.

You can access the paper directly at https://arxiv.org/abs/2602.08169, and the code is available on GitHub at the chili-lab/Spherical-Steering repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fb4142c-a4c0-43db-96fd-79f09d4f83bd",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "95b9bc2f-979a-4e7f-ab38-0fc6fa8f3c73",
  "sourceToolAssistantUUID": "5fb4142c-a4c0-43db-96fd-79f09d4f83bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T08:48:56.327Z_

<details><summary>↩ Tool result · `toolu_01AdoHo8NrpWr7o3nqL9qF8Y`</summary>

```text
Web search results for query: "arxiv 2604.07914 "Mitigating Entangled Steering" MESA hallucination 2026"

Links: [{"title":"[2604.07914] Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction","url":"https://arxiv.org/abs/2604.07914"},{"title":"Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction | Request PDF","url":"https://www.researchgate.net/publication/403683244_Mitigating_Entangled_Steering_in_Large_Vision-Language_Models_for_Hallucination_Reduction"},{"title":"Observation of Non-Markovian Evolution of Tripartite Quantum Steering","url":"https://arxiv.org/html/2604.26711"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=200&show=2000"},{"title":"Cost of Simulating Entanglement in Steering Scenarios","url":"https://arxiv.org/html/2302.09060v4"},{"title":"[2308.07914] Benchmarking highly entangled states on a 60-atom analog quantum simulator","url":"https://arxiv.org/abs/2308.07914"},{"title":"Arxiv","url":"https://arxiv.org/pdf/1903.00469"},{"title":"Reliable Control-Point Selection for Steering Reasoning in ...","url":"https://arxiv.org/pdf/2604.02113"},{"title":"Towards scalable active steering protocols for genuinely entangled state manifolds","url":"https://arxiv.org/html/2412.04168"},{"title":"[2505.22411] Mitigating Overthinking in Large Reasoning Models via Manifold Steering","url":"https://arxiv.org/abs/2505.22411"}]

Based on the search results, I found information about the arxiv paper 2604.07914:

## Paper Overview

The paper addresses hallucinations in Large Vision-Language Models (LVLMs), which produce textual outputs inconsistent with visual content.

## The MESA Framework

MESA is an effective plug-and-play framework that performs controlled and selective latent intervention for hallucination mitigation. MESA targets hallucination-relevant responses while preserving the model's original token distribution, enabling effective hallucination reduction without compromising generation behavior.

## Problem Addressed

The paper identifies that hallucination issues stem from entangled steering signals, where suppressing hallucinations inadvertently disrupts the model's intrinsic generation behavior. Existing methods mitigate hallucinations but often alter generation behavior, resulting in shorter outputs and shifted token distributions, especially in latent space steering approaches.

## Results

Extensive experiments across diverse generative and discriminative benchmarks demonstrate that MESA consistently reduces hallucinations while better preserving generation behavior, outperforming prior methods across multiple LVLM families.

The paper was submitted on April 9, 2026 and is a recent preprint that has not yet been peer-reviewed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36fb3fbe-f3e6-46ee-b276-1227adad0c15",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "cb21551c-5a2d-4578-bcab-e5ad29c60dd5",
  "sourceToolAssistantUUID": "36fb3fbe-f3e6-46ee-b276-1227adad0c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T08:48:59.201Z_

<details><summary>↩ Tool result · `toolu_01WPRJFCznpDC4Hu9EVFTJHk`</summary>

```text
Web search results for query: "arxiv 2602.01654 "Steering Vector Fields" context-aware inference hallucination 2026"

Links: [{"title":"Steering Vector Fields for Context-Aware Inference-Time ...","url":"https://www.arxiv.org/pdf/2602.01654"},{"title":"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models","url":"https://arxiv.org/html/2602.01654"},{"title":"[2602.01654] Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models","url":"https://arxiv.org/abs/2602.01654"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/html/2410.15778v2"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/html/2502.03628v2"},{"title":"[2410.15778] Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/abs/2410.15778"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"}]

I found the paper! Here's information about arXiv:2602.01654:

## Steering Vector Fields for Context-Aware Inference-Time Control in LLMs

Steering vectors (SVs) offer a lightweight way to control large language models (LLMs) at inference time by shifting hidden activations, providing a practical middle ground between prompting and fine-tuning. However, SVs can be unreliable in practice, with some concepts being unsteerable, and reliability degrading in long-form generation and multi-attribute steering.

### The Problem with Static Steering Vectors

A static SV applies the same update vector everywhere in representation space, implicitly assuming that the concept-improving direction is constant across contexts. When the locally effective direction varies with the current activation, a single global vector can become misaligned, which yields weak or reversed effects.

### The SVF Solution

The authors propose Steering Vector Fields (SVF), which learns a differentiable concept scoring function whose local gradient defines the steering direction at each context. SVF is consistently stronger on long-form generation, with the design choice of refreshing steering directions from the evolving hidden states, allowing the intervention to track locally effective concept geometry throughout decoding.

### Evaluation on Hallucination Control

The paper evaluates SVF on hallucination control using a dataset containing two types of hallucination cases (unprompted hallucination and context-triggered hallucination), with 1,000 examples total, each with a prompt and two candidate continuations. SVF achieves the best overall performance, slightly outperforming the preference-training baseline BiPO and substantially exceeding the remaining baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0caf65d1-eff6-4074-a0fe-399c3739d739",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "eaf67db0-41f2-4348-b64b-0c62fc8d827d",
  "sourceToolAssistantUUID": "0caf65d1-eff6-4074-a0fe-399c3739d739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T08:48:59.469Z_

<details><summary>↩ Tool result · `toolu_019yXAaFPKT2X9dLdAtiNmzW`</summary>

```text
Web search results for query: "arxiv 2603.09313 "Curveball Steering" nonlinear geometry hallucination 2026"

Links: [{"title":"[2603.09313] Curveball Steering: The Right Direction To Steer Isn't Always Linear","url":"https://arxiv.org/abs/2603.09313"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313"},{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/html/2602.17691v1"},{"title":"Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation","url":"https://arxiv.org/html/2603.16284"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/html/2602.06801v4"},{"title":"Free Final Time Adaptive Mesh Covariance Steering via Sequential Convex Programming","url":"https://arxiv.org/html/2603.14868"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/html/2603.24543v1"},{"title":"REVIS: Sparse Latent Steering to Mitigate Object Hallucination in Large","url":"https://arxiv.org/pdf/2602.11824"},{"title":"Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior","url":"https://arxiv.org/html/2605.05115v1"}]

I found the paper you're looking for! Here's what I found about arxiv 2603.09313:

## Curveball Steering: The Right Direction To Steer Isn't Always Linear

Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations, and existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. However, such linear interventions often behave inconsistently in practice. Researchers questioned this assumption by analyzing the intrinsic geometry of LLM activation spaces, and found substantial and concept-dependent geometric distortions, indicating that activation spaces are not well-approximated by a globally linear geometry.

In response, researchers proposed "Curveball steering", a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry. Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions.

The paper was submitted on March 10, 2026 with the final version posted on March 22, 2026, and authored by Shivam Raval, Hae Jin Song, Linlin Wu, Abir Harrasse, Jeff M. Phillips, Fazl Barez, and Amirali Abdullah.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47ddc1df-a025-4556-b685-eef63dac46a3",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "8a233085-c068-42d4-a243-bcaf216e708e",
  "sourceToolAssistantUUID": "47ddc1df-a025-4556-b685-eef63dac46a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T08:49:03.138Z_

Let me also search for a few more potentially competing papers from March-May 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a233085-c068-42d4-a243-bcaf216e708e",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xbRUmEv3XVBKUwWdTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb99938-0e3f-40e6-93c0-63a49b76f799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4kWHrUf5Hk64qHgUcapUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 18396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2751,
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

_source line 32 · 2026-05-16T08:49:04.087Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9QNnmUARiZb6VN4oBmDSh`</summary>

```json
{
  "query": "arxiv 2605.03907 \"Steer Like the LLM\" activation steering prompting 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb99938-0e3f-40e6-93c0-63a49b76f799",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xbRUmEv3XVBKUwWdTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d595fe2b-b9c2-4dd1-a4e7-0e83c5a838bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4kWHrUf5Hk64qHgUcapUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 18396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2751,
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

_source line 33 · 2026-05-16T08:49:04.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jtvm7eTf9dA76sJS9rrnhW`</summary>

```json
{
  "query": "arxiv 2602.11824 REVIS sparse latent steering hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d595fe2b-b9c2-4dd1-a4e7-0e83c5a838bd",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xbRUmEv3XVBKUwWdTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "381ba66c-cd23-48f4-a8f7-1f32fd5e622d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4kWHrUf5Hk64qHgUcapUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 18396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2751,
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

_source line 34 · 2026-05-16T08:49:05.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C1fuKqLqH4WZLqJSvTHTf3`</summary>

```json
{
  "query": "\"sentence-level\" OR \"claim-level\" activation steering hallucination arxiv 2026",
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
  "parentUuid": "381ba66c-cd23-48f4-a8f7-1f32fd5e622d",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xbRUmEv3XVBKUwWdTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3351cd1-4ae5-45f5-97b5-70f23785b149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4kWHrUf5Hk64qHgUcapUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 18396,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 887,
          "output_tokens": 232,
          "cache_read_input_tokens": 18396,
          "cache_creation_input_tokens": 2751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2751,
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

_source line 35 · 2026-05-16T08:49:10.505Z_

<details><summary>↩ Tool result · `toolu_01B9QNnmUARiZb6VN4oBmDSh`</summary>

```text
Web search results for query: "arxiv 2605.03907 "Steer Like the LLM" activation steering prompting 2026"

Links: [{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"},{"title":"[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907"},{"title":"[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907v1"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"},{"title":"Steered LLM Activations are Non-Surjective","url":"https://arxiv.org/html/2604.09839v1"},{"title":"Steering Language Models With Activation Engineering","url":"https://arxiv.org/html/2308.10248v5"},{"title":"[2308.10248] Activation Addition: Steering Language Models Without Optimization","url":"https://ar5iv.labs.arxiv.org/html/2308.10248"},{"title":"[2509.09660] Steering MoE LLMs via Expert (De)Activation","url":"https://arxiv.org/abs/2509.09660"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN","url":"https://openreview.net/pdf?id=2XBPdPIcFK"}]

I found the paper! Here's information about arxiv 2605.03907:

## "Steer Like the LLM: Activation Steering that Mimics Prompting"

This paper was submitted on May 5, 2026, by authors Geert Heyman and Frederik Vandeputte, and addresses how large language models can be steered at inference time through prompting or activation interventions, with activation steering methods often underperforming compared to prompt-based approaches.

**Main Contribution:**

The paper proposes a framework that formulates prompt steering as a form of activation steering and investigates whether distilling successful prompt steering behavior into simpler, interpretable models can close the gap between the two approaches.

**Key Findings:**

The analysis reveals that popular activation steering methods are not faithful to the mechanics of prompt steering, which applies strong interventions on some tokens while barely affecting others.

**Proposed Solution:**

The authors introduce Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions.

**Results:**

Experiments on three steering benchmarks across multiple language models show that PSR models outperform existing activation steering methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d595fe2b-b9c2-4dd1-a4e7-0e83c5a838bd",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "827ab0bf-fdc9-4bee-a5d1-25d3f8dc4dbc",
  "sourceToolAssistantUUID": "d595fe2b-b9c2-4dd1-a4e7-0e83c5a838bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T08:49:11.723Z_

<details><summary>↩ Tool result · `toolu_01Jtvm7eTf9dA76sJS9rrnhW`</summary>

```text
Web search results for query: "arxiv 2602.11824 REVIS sparse latent steering hallucination 2026"

Links: [{"title":"REVIS: Sparse Latent Steering to Mitigate Object Hallucination in Large","url":"https://arxiv.org/pdf/2602.11824"},{"title":"[2602.11824] Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.11824"},{"title":"Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models","url":"https://arxiv.org/html/2602.11824"},{"title":"Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering | OpenReview","url":"https://openreview.net/forum?id=LBl7Hez0fF"},{"title":"Steering LVLMs via Sparse Autoencoder for Hallucination Mitigation","url":"https://arxiv.org/html/2505.16146v1"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"[2505.16146] Steering LVLMs via Sparse Autoencoder for Hallucination Mitigation","url":"https://arxiv.org/abs/2505.16146"},{"title":"Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://www.researchgate.net/publication/385107424_Reducing_Hallucinations_in_Vision-Language_Models_via_Latent_Space_Steering"},{"title":"GitHub - shengliu66/VTI: Code for Reducing Hallucinations in Vision-Language Models via Latent Space Steering · GitHub","url":"https://github.com/shengliu66/VTI"},{"title":"Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/html/2410.15778v1"}]

I found the paper! Here are the results for arXiv paper 2602.11824:

## REVIS: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models

**Paper Details:**
- arXiv:2602.11824, submitted on February 12, 2026
- Authors: Jialin Wu, Wei Shi, Han Shen, Peigui Qi, Kunsheng Tang, Zhicong Huang, Binghao Wang, Zhou Yang

**Overview:**
Large Vision-Language Models (LVLMs) frequently suffer from object hallucination because visual features and pretrained textual representations often become intertwined in the deeper network layers.

**Proposed Solution:**
REVIS is a training-free framework designed to explicitly re-activate this suppressed visual information. Rooted in latent space geometry, REVIS extracts the pure visual information vector via orthogonal projection and employs a calibrated strategy to perform sparse intervention only at the precise depth where suppression occurs, effectively restoring visual information with minimal computational cost.

**Results:**
Empirical evaluations on standard benchmarks demonstrate that REVIS reduces object hallucination rates by approximately 19% compared to state-of-the-art baselines, while preserving general reasoning capabilities.

The paper is available at https://arxiv.org/abs/2602.11824 and https://arxiv.org/pdf/2602.11824.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "381ba66c-cd23-48f4-a8f7-1f32fd5e622d",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "ae201193-f062-4b28-ae87-89b844f50991",
  "sourceToolAssistantUUID": "381ba66c-cd23-48f4-a8f7-1f32fd5e622d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T08:49:12.469Z_

<details><summary>↩ Tool result · `toolu_01C1fuKqLqH4WZLqJSvTHTf3`</summary>

```text
Web search results for query: ""sentence-level" OR "claim-level" activation steering hallucination arxiv 2026"

Links: [{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation","url":"https://arxiv.org/html/2603.16284"},{"title":"From Detection to Diagnosis: Advancing Hallucination Analysis with Automated Data Synthesis","url":"https://arxiv.org/html/2601.09734"},{"title":"Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://arxiv.org/pdf/2507.12455"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/html/2410.15778v1"},{"title":"MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination","url":"https://arxiv.org/html/2603.24579v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"[2308.06394] Detecting and Preventing Hallucinations ... - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2308.06394"}]

I found several highly relevant papers from 2026 and recent years. Here are the key results:

## Key Papers Found:

**1. Dynamic Multimodal Activation Steering for Hallucination Mitigation (Feb 2026)**
This method reduces hallucinations by 20.2 at the sentence level (CHAIRS) and by 3.8 at the image level (CHAIRI). The approach, called Dynamic Multimodal Activation Steering, is a training-free method that constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors for context-aware interventions during inference.

**2. Locate-then-Sparsify: Attribution Guided Sparse Strategy (March 2026)**
This work constructs a synthetic dataset comprising token-level and sentence-level hallucination cases. The method constructs hallucination samples at token and sentence granularity levels, then locates hallucination-relevant layers through an attribution method based on causal interventions.

**3. Real-Time Detection of Hallucinated Entities in Long-Form Generation**
This introduces a token-level hallucination detection approach framed as a token-labeling task, focusing on entity-level hallucinations rather than claim-level.

**4. Reducing Hallucinations via Latent Space Steering (VTI method)**
Visual shifting and textual shifting demonstrate effectiveness on different assessment dimensions: visual shifting is more effective in reducing CHAIRI that calculates on image-level, while textual shifting is more effective in reducing CHAIRs that calculates on sentence-level.

These papers represent recent advances in activation steering and fine-grained hallucination detection at both sentence and claim levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3351cd1-4ae5-45f5-97b5-70f23785b149",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "35932c14-e0ae-4d5e-b3b7-3d3d1d3d1f3f",
  "sourceToolAssistantUUID": "a3351cd1-4ae5-45f5-97b5-70f23785b149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T08:49:15.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ECT1Sv4J2imyG8jnZiJTb5`</summary>

```json
{
  "query": "arxiv 2605.13772 \"step-level hallucination\" \"hidden-state transport geometry\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35932c14-e0ae-4d5e-b3b7-3d3d1d3d1f3f",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xcP3wZ585iUwQ5DKys",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0f9f439-b42f-46ef-84f8-b5d795ddb849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wd85muMK3heXJ8BkqgCgzH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3726,
      "cache_read_input_tokens": 21147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3726,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 39 · 2026-05-16T08:49:16.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GfTAnkn8HRHsmea7fXdLh5`</summary>

```json
{
  "query": "arxiv 2507.12455 \"sentence-level early intervention\" hallucination steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f9f439-b42f-46ef-84f8-b5d795ddb849",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xcP3wZ585iUwQ5DKys",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "041b2588-5e76-473a-8121-70abf1278eab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wd85muMK3heXJ8BkqgCgzH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3726,
      "cache_read_input_tokens": 21147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3726,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 40 · 2026-05-16T08:49:22.002Z_

<details><summary>↩ Tool result · `toolu_01GfTAnkn8HRHsmea7fXdLh5`</summary>

```text
Web search results for query: "arxiv 2507.12455 "sentence-level early intervention" hallucination steering"

Links: [{"title":"[2507.12455] Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://arxiv.org/abs/2507.12455"},{"title":"Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://arxiv.org/html/2507.12455"},{"title":"(PDF) Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://www.researchgate.net/publication/393771584_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention"},{"title":"Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/html/2410.15778v2"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Peng_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention_ICCV_2025_paper.pdf"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/pdf/2404.09971"},{"title":"Disentangling Deception and Hallucination Failures in LLMs","url":"https://arxiv.org/html/2602.14529"},{"title":"Mitigating Hallucination via Evaluating the Factuality of ...","url":"https://aclanthology.org/2025.findings-acl.752.pdf"}]

Based on the search results, here's what I found about arXiv paper 2507.12455:

## Paper Overview

The paper is titled "Mitigating Object Hallucinations via Sentence-Level Early Intervention" and was submitted on July 16, 2025.

## Problem and Main Contribution

Multimodal large language models (MLLMs) struggle with hallucinations - fabricated content contradicting visual inputs, and existing hallucination mitigation methods either incur prohibitive computational costs or introduce distribution mismatches between training data and model outputs. 

The key insight of the paper is that hallucinations predominantly emerge at the early stages of text generation and propagate through subsequent outputs.

## The SENTINEL Framework

To address this problem, the authors propose SENTINEL (Sentence-level Early iNtervention Through IN-domain prEference Learning), a framework that eliminates dependency on human annotations. 

Specifically, they bootstrap high-quality in-domain preference pairs by iteratively sampling model outputs, validating object existence through cross-checking with two open-vocabulary detectors, and classifying sentences into hallucinated/non-hallucinated categories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "041b2588-5e76-473a-8121-70abf1278eab",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "ca210963-e21c-41a9-8084-73ba871b29b6",
  "sourceToolAssistantUUID": "041b2588-5e76-473a-8121-70abf1278eab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T08:49:22.934Z_

<details><summary>↩ Tool result · `toolu_01ECT1Sv4J2imyG8jnZiJTb5`</summary>

```text
Web search results for query: "arxiv 2605.13772 "step-level hallucination" "hidden-state transport geometry" 2026"

Links: [{"title":"[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/abs/2605.13772"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models","url":"https://arxiv.org/html/2605.10002v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Do We Really Need External Tools to Mitigate Hallucinations? Sira: Shared-Prefix Internal Reconstruction of Attribution","url":"https://arxiv.org/html/2605.14621"},{"title":"Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs","url":"https://arxiv.org/html/2509.13813v1"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/html/2601.17467v1"},{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"}]

I found the paper! Here are the details for arXiv paper 2605.13772:

**Title:** Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry

**Authors:** Tyler Alvarez and Ali Baheri

**Submission Date:** 13 May 2026

**Main Concept:** The paper addresses how large language models hallucinate during multi-step reasoning by framing hallucination as a property of the hidden-state trajectory produced during a single forward pass. Correct reasoning moves through a stable manifold of locally coherent transitions; a first error appears as a localized excursion in transport cost away from this manifold.

**Approach:** The authors operationalize this view with a label-conditioned teacher that builds a trace-specific contrastive PCA lens and scores each step with seven geometric transition features, and a deployable BiLSTM student distilled from the teacher that operates on raw hidden states without inference-time labels.

**Results:** On ProcessBench, PRM800K, HaluEval, and TruthfulQA, both models outperform entropy-based, probing-based, and attention-based baselines in-domain; the teacher transfers stably across language models and datasets, while the student collapses under shift.

You can access the full paper at: https://arxiv.org/abs/2605.13772


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0f9f439-b42f-46ef-84f8-b5d795ddb849",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a1993c84ad2495b66",
  "type": "user",
  "uuid": "6b6fa874-341d-4b51-9221-8add1f26304d",
  "sourceToolAssistantUUID": "e0f9f439-b42f-46ef-84f8-b5d795ddb849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T08:50:18.627Z_

Here is my comprehensive report on recent competing papers (March-May 2026) on activation steering for hallucination reduction that could compete with a "geometry-triggered sentence-level steering" approach:

---

## Highly Relevant Concurrent Competitors (Feb-May 2026)

### 1. Steering Vector Fields (SVF) -- arXiv 2602.01654 (Feb 2026)
- **Mechanism**: Learns a differentiable concept scoring function whose local gradient defines the steering direction at each context. Unlike static steering vectors, SVF refreshes steering directions from evolving hidden states throughout decoding.
- **Why it competes**: This is context-aware, geometry-sensitive steering that adapts per-token -- directly overlapping with "geometry-triggered" approaches. Evaluates on hallucination control and outperforms BiPO and other baselines on long-form generation.
- [Paper](https://arxiv.org/abs/2602.01654)

### 2. Spherical Steering -- arXiv 2602.08169 (Feb 2026, ICML 2026)
- **Mechanism**: Rotates activations along a geodesic toward a target direction (preserving norm/magnitude), rather than adding steering vectors. Training-free.
- **Why it competes**: Explicitly "geometry-aware" -- uses hypersphere geometry to avoid representation collapse. +10% on TruthfulQA over addition-based baselines. The "geometry-aware" framing directly overlaps with your paper's positioning.
- [Paper](https://arxiv.org/abs/2602.08169) | [Code](https://github.com/chili-lab/Spherical-Steering)

### 3. Curveball Steering -- arXiv 2603.09313 (March 2026)
- **Mechanism**: Nonlinear steering via polynomial kernel PCA that respects learned activation geometry. Demonstrates that LLM activation spaces have substantial concept-dependent geometric distortions, making linear interventions suboptimal.
- **Why it competes**: Another "geometry-aware" steering method that addresses the same core insight -- that activation space geometry matters for effective steering. Outperforms linear PCA-based steering in distorted regimes.
- [Paper](https://arxiv.org/abs/2603.09313)

### 4. HELIX / Tethered Reasoning -- arXiv 2602.17691 (Feb 2026)
- **Mechanism**: Computes a Unified Truth Score (UTS) combining token-level semantic entropy with **Mahalanobis distance** from a pre-computed truthfulness manifold. When UTS indicates trajectory divergence, graduated steering vectors redirect activations. Only affects 0.2-2.5% of tokens.
- **Why it competes**: Uses Mahalanobis distance as a geometric trigger for selective steering -- very close to "geometry-triggered" steering. Focused on quantized LLMs but the mechanism generalizes. GSM8K: 88.84% at T=3.0.
- [Paper](https://arxiv.org/abs/2602.17691)

### 5. PCNet / Hallucination as an Anomaly -- arXiv 2605.05953 (May 7, 2026)
- **Mechanism**: Probabilistic Circuit (PCNet) trained as a tractable density estimator over the LLM residual stream. Detects hallucinations as geometric anomalies via exact NLL computation (no sampling). Gates PC-LDCD (latent density contrastive decoding) only when latent geometry deviates from factual regions.
- **Why it competes**: Geometric anomaly detection triggering selective intervention at decoding time. AUROC up to 99% for hallucination detection. Very recent (May 2026) and directly models the "factual manifold" concept.
- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca (University of Trento)
- [Paper](https://arxiv.org/abs/2605.05953)

### 6. Where Does Reasoning Break? -- arXiv 2605.13772 (May 13, 2026)
- **Mechanism**: Frames hallucination as excursions in transport cost away from a stable manifold of coherent hidden-state transitions. Uses step-level geometric transition features (7 features) to detect the first error in multi-step reasoning.
- **Why it competes**: Step-level (granular) hallucination detection via hidden-state geometry. Directly relevant to "sentence-level" detection. Uses contrastive PCA lens and BiLSTM student. Outperforms entropy/probing/attention baselines on ProcessBench, PRM800K, HaluEval, TruthfulQA.
- [Paper](https://arxiv.org/abs/2605.13772)

### 7. MESA (Mitigating Entangled Steering) -- arXiv 2604.07914 (April 2026)
- **Mechanism**: Plug-and-play framework that performs controlled and selective latent intervention. Addresses "entangled steering signals" where suppressing hallucinations disrupts generation behavior. Targets hallucination-relevant responses while preserving token distribution.
- **Why it competes**: Selective steering (only intervening when needed) while preserving generation quality -- similar to sentence-level selective intervention.
- [Paper](https://arxiv.org/abs/2604.07914)

### 8. SENTINEL (Sentence-Level Early Intervention) -- arXiv 2507.12455 (July 2025, published ICCV 2025)
- **Mechanism**: Identifies that hallucinations predominantly emerge at early stages of generation and propagate. Uses sentence-level preference learning with bootstrapped in-domain preference pairs.
- **Why it competes**: Explicitly "sentence-level" intervention for hallucination. Though older (2025) and preference-learning-based rather than activation-steering, the sentence-level framing is identical. Published at ICCV 2025 -- you should cite this.
- [Paper](https://arxiv.org/abs/2507.12455)

---

## Moderately Relevant Papers

### 9. Dynamic Multimodal Activation Steering (DMAS) -- arXiv 2602.21704 (Feb 2026)
- Context-aware dynamic selection of steering vectors based on semantic similarity + attention head targeting. Training-free. Focused on Vision-Language Models. 20.2% reduction in sentence-level hallucination (CHAIRS).
- [Paper](https://arxiv.org/abs/2602.21704)

### 10. REVIS -- arXiv 2602.11824 (Feb 2026)
- Sparse latent steering using orthogonal projection to extract pure visual vectors + calibration-based layer selection + inference-time dynamic risk-aware steering. 19% hallucination reduction. Vision-Language focused.
- [Paper](https://arxiv.org/abs/2602.11824)

### 11. Steer Like the LLM (PSR) -- arXiv 2605.03907 (May 5, 2026)
- Shows that effective steering should apply token-specific coefficients (strong on some tokens, weak on others), mimicking how prompts actually work. Introduces Prompt Steering Replacement models.
- [Paper](https://arxiv.org/abs/2605.03907)

### 12. Prompt-Activation Duality -- arXiv 2605.10664 (May 2026)
- Attention-level interventions for activation steering.
- [Paper](https://arxiv.org/html/2605.10664)

---

## Verification of Specific Papers

**PCNet (arXiv 2605.05953)**: CONFIRMED. "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" by Nielsen, Cunegatti, Vukojevic, Iacca (U. Trento). May 7, 2026. Uses PCNet as density estimator on residual stream, gates PC-LDCD intervention when NLL indicates anomaly.

**HELIX (arXiv 2602.17691)**: CONFIRMED. "Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering" by Craig Atkinson. Feb 2026. Uses Mahalanobis distance from truthfulness manifold + semantic entropy to compute UTS, triggers graduated steering vectors. Note: The paper name is "Tethered Reasoning" and the framework is called "HELIX" -- not "HELIX tethered reasoning" as a single unit.

---

## Key Threat Assessment for "Geometry-Triggered Sentence-Level Steering"

**Highest overlap papers** (most likely to be flagged by reviewers as concurrent work):
1. **Steering Vector Fields** (2602.01654) -- context-aware geometry-driven steering
2. **Spherical Steering** (2602.08169) -- geometry-aware steering (ICML 2026 accepted)
3. **HELIX** (2602.17691) -- Mahalanobis-triggered selective steering
4. **PCNet** (2605.05953) -- geometric anomaly-triggered selective intervention
5. **Step-Level Transport Geometry** (2605.13772) -- step-level geometric hallucination detection

The combination of "geometric trigger + sentence-level granularity + text LLM hallucination" appears to be a gap -- most geometric approaches operate token-level or step-level, and most sentence-level approaches (SENTINEL) use preference learning rather than activation geometry. However, PCNet and the Transport Geometry paper are very close in spirit and extremely recent (May 2026).

Sources:
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)
- [Spherical Steering](https://arxiv.org/abs/2602.08169)
- [Curveball Steering](https://arxiv.org/abs/2603.09313)
- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)
- [PCNet / Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [Step-Level Hallucination via Transport Geometry](https://arxiv.org/abs/2605.13772)
- [MESA](https://arxiv.org/abs/2604.07914)
- [SENTINEL](https://arxiv.org/abs/2507.12455)
- [DMAS](https://arxiv.org/abs/2602.21704)
- [REVIS](https://arxiv.org/abs/2602.11824)
- [Steer Like the LLM](https://arxiv.org/abs/2605.03907)
- [Prompt-Activation Duality](https://arxiv.org/html/2605.10664)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b6fa874-341d-4b51-9221-8add1f26304d",
  "isSidechain": true,
  "agentId": "a1993c84ad2495b66",
  "requestId": "req_011Cb5xd9oFT2eAznJPedTVB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffb731cb-e412-49b2-af64-a2f41327fb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfcdjZ6De6zryBjWTYYYbW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 24873,
      "output_tokens": 2622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 837,
          "output_tokens": 2622,
          "cache_read_input_tokens": 24873,
          "cache_creation_input_tokens": 1008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1008,
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
