# Research conversation: I'm reviewing a research proposal that cites several key papers. I need you to verify these papers exist and check their

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a836d5ba67e75fa6c.jsonl`
- **Structured JSON:** [`6a1f766aeef7ce177e03.json`](../../sessions/6a/6a1f766aeef7ce177e03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-16T09:00:17.771Z_

I'm reviewing a research proposal that cites several key papers. I need you to verify these papers exist and check their claims using WebSearch and WebFetch. Search for each and report what you find:

1. "Endogenous Resistance to Activation Steering in Language Models" (arXiv 2602.06941, Feb 2026) - Does it exist? What does it actually show about model resistance to steering?

2. "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" (Ji et al., EMNLP 2025 Outstanding Paper) - Does it exist? Did it win Outstanding Paper? What models was it tested on? What was the VUF direction result?

3. "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (Nielsen et al., arXiv 2605.05953, May 2026) - PC-LDCD paper. Does it exist? What results does it achieve? Does it acknowledge limitations with overconfident hallucinations?

4. "Real-Time Detection of Hallucinated Entities in Long-Form Generation" (obalcells et al., EMNLP 2025 Findings) - Does it exist? Does it provide pretrained probes? What AUROC does it achieve?

5. "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control" (CSS, arXiv 2604.17487, April 2026) - Does it exist? What's the 0.913 utility claim?

For each paper, do a WebSearch, and for the most critical ones (especially #2 and #3), try to WebFetch the actual arXiv page to verify details. Report exactly what you find - don't assume the proposal's claims are correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "869144a3-67ea-4d6d-9696-57ce735aff7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:00:17.774Z_

```json
{
  "parentUuid": "869144a3-67ea-4d6d-9696-57ce735aff7d",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
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
  "uuid": "93f5490a-23fc-4398-8e32-21f24e30019b",
  "timestamp": "2026-05-16T09:00:17.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:00:21.259Z_



I'll start by loading the WebSearch and WebFetch tools, then search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93f5490a-23fc-4398-8e32-21f24e30019b",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yTRYNyhdo6QehcfDku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6af99614-2850-4fc8-9c18-ca64101ef059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018veWfoRAK5d6JJD1EHiTDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9183,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9183,
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

_source line 4 · 2026-05-16T09:00:21.402Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qju8mG3FG4p1Sw3RrxGNvF`</summary>

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
  "parentUuid": "6af99614-2850-4fc8-9c18-ca64101ef059",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yTRYNyhdo6QehcfDku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59a240ad-51b1-4d11-bdca-579ede95b35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018veWfoRAK5d6JJD1EHiTDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9183,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9183,
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

_source line 5 · 2026-05-16T09:00:21.407Z_

<details><summary>↩ Tool result · `toolu_01Qju8mG3FG4p1Sw3RrxGNvF`</summary>

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
  "parentUuid": "59a240ad-51b1-4d11-bdca-579ede95b35a",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "c95682cf-2a82-456f-9a5d-47f7e56fbbbe",
  "sourceToolAssistantUUID": "59a240ad-51b1-4d11-bdca-579ede95b35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T09:00:24.175Z_



Now let me search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c95682cf-2a82-456f-9a5d-47f7e56fbbbe",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71b2451d-31d7-44a6-b8ec-5b29c101370b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-16T09:00:24.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ES4HLQP3kR9jefs3uLKRyu`</summary>

```json
{
  "query": "arXiv 2602.06941 \"Endogenous Resistance to Activation Steering in Language Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b2451d-31d7-44a6-b8ec-5b29c101370b",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9776ada7-d0b5-4375-8afd-66075377f23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-16T09:00:25.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KNkfq6z37z2NKiUU5RkUBU`</summary>

```json
{
  "query": "\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" Ji et al. EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9776ada7-d0b5-4375-8afd-66075377f23b",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c1dead0-aa45-49b7-8d0a-148f2cdf3f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-16T09:00:26.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RGzHsqA13WRQtvXbCX8R7K`</summary>

```json
{
  "query": "arXiv 2605.05953 \"Hallucination as an Anomaly\" Nielsen \"Probabilistic Circuits\" PC-LDCD"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c1dead0-aa45-49b7-8d0a-148f2cdf3f9d",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa15393c-d466-4b21-b3e9-4257eda87dc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-16T09:00:26.595Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017q6jvxg2tiq9xDocSkYRKN`</summary>

```json
{
  "query": "\"Real-Time Detection of Hallucinated Entities in Long-Form Generation\" obalcells EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa15393c-d466-4b21-b3e9-4257eda87dc5",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d53ead85-6f5e-49dd-974c-9235b8f14f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 11 · 2026-05-16T09:00:27.040Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HTJVTfrwA3Ew7e6JcfXLU`</summary>

```json
{
  "query": "arXiv 2604.17487 \"Answer Only as Precisely as Justified\" Calibrated Claim-Level Specificity Control CSS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d53ead85-6f5e-49dd-974c-9235b8f14f8f",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yThmgvMX74fkorf9ZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dda97824-6807-4e29-a084-d3d629c13178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhzhuFFuHY2eMa1kP6M9jA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9183,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 9183,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 12 · 2026-05-16T09:00:31.607Z_

<details><summary>↩ Tool result · `toolu_01ES4HLQP3kR9jefs3uLKRyu`</summary>

```text
Web search results for query: "arXiv 2602.06941 "Endogenous Resistance to Activation Steering in Language Models""

Links: [{"title":"[2602.06941] Endogenous Resistance to Activation Steering in Language Models","url":"https://arxiv.org/abs/2602.06941"},{"title":"Endogenous Resistance to Activation Steering in Language Models","url":"https://arxiv.org/html/2602.06941v1"},{"title":"Steering Language Models With Activation Engineering","url":"https://arxiv.org/html/2308.10248v5"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner","url":"https://arxiv.org/pdf/2308.10248"},{"title":"[2602.01716] Mechanistic Indicators of Steering Effectiveness in Large Language Models","url":"https://arxiv.org/abs/2602.01716"},{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/html/2512.24143v1"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN","url":"https://openreview.net/pdf?id=2XBPdPIcFK"},{"title":"Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models","url":"https://arxiv.org/html/2602.04896"},{"title":"[2602.04896] Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models","url":"https://arxiv.org/abs/2602.04896"},{"title":"Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics","url":"https://arxiv.org/html/2602.02343"}]

I found the paper you're looking for. Here are the key details:

**Paper: "Endogenous Resistance to Activation Steering in Language Models"**

**arXiv ID:** 2602.06941

**Submission Date:** February 6, 2026

**Authors:** Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, and Michael S. A. Graziano

**Main Findings:**

Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. This is termed Endogenous Steering Resistance (ESR).

Using sparse autoencoder (SAE) latents to steer model activations, Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently.

The researchers identified 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits.

You can access the full paper at: https://arxiv.org/abs/2602.06941


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9776ada7-d0b5-4375-8afd-66075377f23b",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "2dbd7ca6-2761-4b4e-bfc0-560378f6dd88",
  "sourceToolAssistantUUID": "9776ada7-d0b5-4375-8afd-66075377f23b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T09:00:32.182Z_

<details><summary>↩ Tool result · `toolu_01KNkfq6z37z2NKiUU5RkUBU`</summary>

```text
Web search results for query: ""Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" Ji et al. EMNLP 2025"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.187@ACL"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to ...","url":"https://aclanthology.org/2025.emnlp-main.187.pdf"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"GitHub - facebookresearch/verbal_uncertainty_feature_calibration: Mechanistic uncertainty calibration of LLMs. · GitHub","url":"https://github.com/facebookresearch/verbal_uncertainty_feature_calibration"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"[Literature Review] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.themoonlight.io/en/review/calibrating-verbal-uncertainty-as-a-linear-feature-to-reduce-hallucinations"}]

I found the paper! Here's what I found about "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ji et al. published at EMNLP 2025:

## Paper Overview

The paper is authored by Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda, and was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP) in Suzhou, China, on pages 3769–3793.

## Main Findings

The paper addresses the problem that "LLMs often adopt an assertive language style also when making false claims" and notes that such "overconfident hallucinations" mislead users and erode trust.

The key finding is that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and this has only moderate correlation with the actual "semantic uncertainty" of the model.

## Results and Impact

The authors show that (1) the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone and (2) they can intervene on verbal uncertainty at inference time and reduce confident hallucinations on short-form answers, achieving an average relative reduction of ~30%.

The paper also has an associated GitHub repository for their mechanistic uncertainty calibration work, making their research reproducible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c1dead0-aa45-49b7-8d0a-148f2cdf3f9d",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "8bceff67-5d61-453f-a481-3d9f5efd957e",
  "sourceToolAssistantUUID": "9c1dead0-aa45-49b7-8d0a-148f2cdf3f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:00:34.041Z_

<details><summary>↩ Tool result · `toolu_01RGzHsqA13WRQtvXbCX8R7K`</summary>

```text
Web search results for query: "arXiv 2605.05953 "Hallucination as an Anomaly" Nielsen "Probabilistic Circuits" PC-LDCD"

Links: [{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Hallucinations Live in Variance","url":"https://arxiv.org/html/2601.07058v1"},{"title":"[2605.13146] On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods","url":"https://arxiv.org/abs/2605.13146"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Understanding Hallucinations in Diffusion Models through Mode Interpolation","url":"https://arxiv.org/html/2406.09358v2"},{"title":"[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/abs/2605.13772"},{"title":"On the Fundamental Impossibility of Hallucination Control in ...","url":"https://arxiv.org/pdf/2506.06382v3"},{"title":"Paper Digest: NeurIPS 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/neurips-2025-papers-highlights/"},{"title":"A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/html/2406.06950v1"}]

Based on the search results, I found the paper you're looking for:

**"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits"** (arXiv:2605.05953) by Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, and Giovanni Iacca, submitted on May 7, 2026.

**Key contributions:**

The paper proposes PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold via exact Negative Log-Likelihood computation, without requiring sampling, external verifiers, or weight modifications.

PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) activates only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

**Results:**

Across four LLMs ranging from 1B to 8B models and four benchmarks covering conversational reasoning, knowledge-intensive QA, reading comprehension, and truthfulness, PCNET achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%. PC-LDCD obtains the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models, while reducing the mean corruption rate to 53.7% and achieving a preservation rate of 79.3%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa15393c-d466-4b21-b3e9-4257eda87dc5",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "a8bef2b4-cf08-4bf6-a649-899fe43edfd8",
  "sourceToolAssistantUUID": "aa15393c-d466-4b21-b3e9-4257eda87dc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T09:00:34.375Z_

<details><summary>↩ Tool result · `toolu_017q6jvxg2tiq9xDocSkYRKN`</summary>

```text
Web search results for query: ""Real-Time Detection of Hallucinated Entities in Long-Form Generation" obalcells EMNLP 2025"

Links: [{"title":"GitHub - obalcells/hallucination_probes: Real-Time Detection of Hallucinated Entities in Long-Form Generation · GitHub","url":"https://github.com/obalcells/hallucination_probes"},{"title":"[2509.03531] Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/abs/2509.03531"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.hallucination-probes.com/"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation - MATS Research","url":"https://www.matsprogram.org/research/real-time-detection-of-hallucinated-entities-in-long-form-generation"},{"title":"[2509.03531v1] Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/abs/2509.03531v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation | OpenReview","url":"https://openreview.net/forum?id=YxJEMTflww"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.researchgate.net/publication/395270424_Real-Time_Detection_of_Hallucinated_Entities_in_Long-Form_Generation"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.03531"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"}]

I found the paper! Here are the search results for "Real-Time Detection of Hallucinated Entities in Long-Form Generation" by obalcells (Oscar Obeso):

## Paper Overview

The paper presents a cheap, scalable method for real-time identification of hallucinated tokens in long-form generations, and scales it effectively to 70B parameter models.

## Key Contributions

The approach targets entity-level hallucinations—e.g., fabricated names, dates, citations—rather than claim-level, thereby naturally mapping to token-level labels and enabling streaming detection.

The researchers develop an annotation methodology that leverages web search to annotate model responses with grounded labels indicating which tokens correspond to fabricated entities, enabling them to train effective hallucination classifiers with simple and efficient methods such as linear probes.

## Results

Evaluating across four model families, their classifiers consistently outperform baselines on long-form responses, including more expensive methods such as semantic entropy (e.g., AUC 0.90 vs 0.71 for Llama-3.3-70B), and are also an improvement in short-form question-answering settings.

Despite being trained only to detect hallucinated entities, their probes effectively detect incorrect answers in mathematical reasoning tasks, indicating generalization beyond entities.

## Paper Details

- **Authors**: Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda
- **ArXiv ID**: 2509.03531
- **Code & Resources**: Available at https://github.com/obalcells/hallucination_probes


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d53ead85-6f5e-49dd-974c-9235b8f14f8f",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "6b1c4a55-1022-4a45-84f2-321e2f206995",
  "sourceToolAssistantUUID": "d53ead85-6f5e-49dd-974c-9235b8f14f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:00:35.667Z_

<details><summary>↩ Tool result · `toolu_015HTJVTfrwA3Ew7e6JcfXLU`</summary>

```text
Web search results for query: "arXiv 2604.17487 "Answer Only as Precisely as Justified" Calibrated Claim-Level Specificity Control CSS"

Links: [{"title":"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems","url":"https://arxiv.org/html/2604.17487"},{"title":"[2604.17487] Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems","url":"https://arxiv.org/abs/2604.17487"},{"title":"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity","url":"https://arxiv.org/pdf/2604.17487"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/html/2502.19110v1"},{"title":"Justified or Just Convincing? Error Verifiability as a Dimension of LLM Quality","url":"https://arxiv.org/html/2604.04418"},{"title":"What Do Claim Verification Datasets Actually Test? A Reasoning Trace Analysis","url":"https://arxiv.org/html/2604.01657v1"},{"title":"Calibrated Surprise: An Information-Theoretic Account of Creative Quality","url":"https://arxiv.org/html/2604.26269"},{"title":"Escaping the Agreement Trap: Defensibility Signals for Evaluating Rule-Governed AI","url":"https://arxiv.org/html/2604.20972v1"},{"title":"[2604.04418] Justified or Just Convincing? Error Verifiability as a Dimension of LLM Quality","url":"https://arxiv.org/abs/2604.04418"}]

Based on the search results, here is information about the arXiv paper 2604.17487:

## Paper Overview

The paper is titled "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems".

## Problem and Solution

Agentic systems often fail not by being entirely wrong, but by being too precise: a response may be generally useful while particular claims exceed what the evidence supports. The paper introduces compositional selective specificity (CSS), a post-generation layer that decomposes an answer into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level that appears admissible.

## Key Features

The method is designed to express uncertainty as a local semantic backoff rather than as a whole-answer refusal.

## Results

Across a full LongFact run and HotpotQA pilots, calibrated CSS improves the risk-utility trade-off of fixed drafts. On the full LongFact run, it raises overcommitment-aware utility from 0.846 to 0.913 relative to the no-CSS output while achieving 0.938 specificity retention.

The paper was submitted by Tianyi Huang and 4 other authors on April 19, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda97824-6807-4e29-a084-d3d629c13178",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "1e8b0ab7-7b26-4eb6-8058-bd1a92124246",
  "sourceToolAssistantUUID": "dda97824-6807-4e29-a084-d3d629c13178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T09:00:39.962Z_

Good, all five papers appear to exist. Now let me fetch the actual arXiv pages for papers #2 and #3 (the most critical ones per the request), and also #4 to verify the AUROC claim and EMNLP venue details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e8b0ab7-7b26-4eb6-8058-bd1a92124246",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yUk3PiVURUn2BPdubp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70c669a0-ae3c-4076-9795-c9e53b69011a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfoRXzSLSGfQWEQV9emutN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4828,
      "cache_read_input_tokens": 11096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4828,
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

_source line 18 · 2026-05-16T09:00:42.330Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0119R4k25wupB3sLWdQdmbps`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.14477",
  "prompt": "What are the full details of this paper? Did it win any award at EMNLP 2025 (e.g. Outstanding Paper, Best Paper)? What models was it tested on? What was the \"VUF direction\" result? List the key quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70c669a0-ae3c-4076-9795-c9e53b69011a",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yUk3PiVURUn2BPdubp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b51e9f09-6980-46ac-91af-5a17ace69ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfoRXzSLSGfQWEQV9emutN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4828,
      "cache_read_input_tokens": 11096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4828,
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

_source line 19 · 2026-05-16T09:00:43.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YWYnCg4tgBc17jxPEVb37u`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05953",
  "prompt": "What are the full details of this paper? What are the key quantitative results (AUROC, corruption rate, preservation rate)? Does it acknowledge limitations with overconfident hallucinations? What models and benchmarks were tested? List the authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51e9f09-6980-46ac-91af-5a17ace69ea2",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yUk3PiVURUn2BPdubp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a49970fb-efc2-4cf6-a971-e341ae5541fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfoRXzSLSGfQWEQV9emutN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4828,
      "cache_read_input_tokens": 11096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4828,
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

_source line 20 · 2026-05-16T09:00:45.219Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XLvsBh2NecUtzLgKiQAmHi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.03531",
  "prompt": "What are the full details of this paper? What venue was it published at - was it EMNLP 2025 Findings? Does it provide pretrained probes? What AUROC or AUC does it achieve? List the authors and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a49970fb-efc2-4cf6-a971-e341ae5541fa",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yUk3PiVURUn2BPdubp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0d291cc-1cee-4e3e-b285-005f1406ecb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfoRXzSLSGfQWEQV9emutN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4828,
      "cache_read_input_tokens": 11096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4828,
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

_source line 21 · 2026-05-16T09:00:46.600Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TdoNH3Y7qxVATtHRpATG8H`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.187/",
  "prompt": "Does this page indicate that the paper won any award at EMNLP 2025 (Outstanding Paper, Best Paper, etc.)? What are the full publication details? List any awards or special recognitions mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0d291cc-1cee-4e3e-b285-005f1406ecb6",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yUk3PiVURUn2BPdubp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48a08215-f7f9-47b0-b3b8-65263fd27528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfoRXzSLSGfQWEQV9emutN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4828,
      "cache_read_input_tokens": 11096,
      "output_tokens": 555,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 555,
          "cache_read_input_tokens": 11096,
          "cache_creation_input_tokens": 4828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4828,
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

_source line 22 · 2026-05-16T09:00:46.941Z_

<details><summary>↩ Tool result · `toolu_0119R4k25wupB3sLWdQdmbps`</summary>

```text
# Paper Summary: Calibrating Verbal Uncertainty as a Linear Feature

## Available Information

Based on the arXiv page content provided, I can confirm the following details:

**Basic Metadata:**
- arXiv ID: 2503.14477
- Submitted: March 18, 2025 (revised April 22, 2025)
- Field: Computer Science - Computation and Language (cs.CL)
- Authors: Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda

**Core Contribution:**
The researchers discovered that "verbal uncertainty is governed by a single linear feature in the representation space of LLMs" and found this has only moderate correlation with actual semantic uncertainty. They achieved approximately 30% relative reduction in confident hallucinations through inference-time intervention.

## Information Not Available

The provided page content does not include:
- EMNLP 2025 award status
- Specific models tested
- Details about "VUF direction" results
- Complete quantitative benchmarks
- The full paper text

To obtain these details, you would need to access the full PDF or HTML version of the paper linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b51e9f09-6980-46ac-91af-5a17ace69ea2",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "e3ab51b2-9bc6-4dcb-a698-294cadf7e276",
  "sourceToolAssistantUUID": "b51e9f09-6980-46ac-91af-5a17ace69ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T09:00:48.821Z_

<details><summary>↩ Tool result · `toolu_01YWYnCg4tgBc17jxPEVb37u`</summary>

```text
# Paper Details: Hallucination as an Anomaly

## Authors
Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca

## Core Contribution
The researchers developed PCNET, which treats hallucinations as "geometric anomalies on the factual manifold" using probabilistic circuits as a density estimator. They created PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) to selectively intervene only when hallucinations are detected.

## Key Quantitative Results
- **AUROC**: Achieved "near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%"
- **Corruption Rate**: Reduced to 53.7%
- **Preservation Rate**: 79.3%
- The method obtained "the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models"

## Models & Benchmarks Tested
- **Models**: Four LLMs ranging from 1B to 8B parameters
- **Benchmarks**: CoQA, SQuAD v2.0, TriviaQA, and TruthfulQA (covering conversational reasoning, knowledge-intensive QA, reading comprehension, and truthfulness)

## Limitations Discussion
The abstract does not explicitly acknowledge limitations regarding overconfident hallucinations or other failure modes.

## Availability
The method is "publicly available on GitHub."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a49970fb-efc2-4cf6-a971-e341ae5541fa",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "142aec2d-a125-4cd3-9fee-c910486fb9b0",
  "sourceToolAssistantUUID": "a49970fb-efc2-4cf6-a971-e341ae5541fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T09:00:49.776Z_

<details><summary>↩ Tool result · `toolu_01XLvsBh2NecUtzLgKiQAmHi`</summary>

```text
# Real-Time Detection of Hallucinated Entities in Long-Form Generation

## Authors
Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda

## Publication Venue
The webpage does not specify a conference publication venue. The paper was submitted to arXiv on August 26, 2025, with a revision on February 5, 2026 (arXiv:2509.03531).

## Key Results
The method achieves strong performance metrics: "AUC 0.90 vs 0.71 for Llama-3.3-70B" when compared to semantic entropy baselines. The classifiers consistently outperform existing approaches across four model families on long-form responses.

## Pretrained Probes
The webpage indicates the authors plan to "publicly release our datasets to facilitate reuse," though it doesn't explicitly confirm whether pretrained probes are included.

## Main Contribution
The research presents "a cheap, scalable method for real-time identification of hallucinated tokens in long-form generations" using linear probes trained on web search-annotated data. The approach focuses on entity-level hallucinations (fabricated names, dates, citations) rather than claim-level ones, enabling streaming detection and token-level predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0d291cc-1cee-4e3e-b285-005f1406ecb6",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "04003df7-19b0-4d68-80bd-5ddfe41aa07f",
  "sourceToolAssistantUUID": "a0d291cc-1cee-4e3e-b285-005f1406ecb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T09:00:49.876Z_

<details><summary>↩ Tool result · `toolu_01TdoNH3Y7qxVATtHRpATG8H`</summary>

```text
# Paper Award and Publication Details

## Award Recognition
Yes, the page indicates a special recognition: the paper received a **"SAC Highlight Award"** at EMNLP 2025.

## Full Publication Details
- **Title:** "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations"
- **Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda
- **Conference:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing
- **Location:** Suzhou, China
- **Publication Date:** November 2025
- **Pages:** 3769–3793
- **Publisher:** Association for Computational Linguistics
- **DOI:** 10.18653/v1/2025.emnlp-main.187
- **ISBN:** 979-8-89176-332-6
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48a08215-f7f9-47b0-b3b8-65263fd27528",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "f7f7f0cf-cfba-4310-af35-6e7f781d9848",
  "sourceToolAssistantUUID": "48a08215-f7f9-47b0-b3b8-65263fd27528",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T09:00:55.571Z_

Now let me do a few more targeted lookups to verify specific claims - the EMNLP 2025 award status for paper #2, whether paper #4 was actually at EMNLP Findings, and the limitations section of paper #3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f7f0cf-cfba-4310-af35-6e7f781d9848",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yVnmNsTF38aP8EobSY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bf1bffa-27e5-4389-bd4a-6a094ecf3334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThgMuiyhoKcYo7imZ4ovXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 27 · 2026-05-16T09:00:56.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ppKvj9Y9maSb5or7VchDP`</summary>

```json
{
  "query": "EMNLP 2025 Outstanding Paper award winners list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bf1bffa-27e5-4389-bd4a-6a094ecf3334",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yVnmNsTF38aP8EobSY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aeba007-6944-42e3-83ba-693435ab5cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThgMuiyhoKcYo7imZ4ovXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 28 · 2026-05-16T09:00:57.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W4iYxmwjXJFAjr8c7LyxRT`</summary>

```json
{
  "query": "\"Real-Time Detection of Hallucinated Entities\" EMNLP 2025 Findings obalcells hallucination_probes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aeba007-6944-42e3-83ba-693435ab5cd7",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yVnmNsTF38aP8EobSY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f1f9d29-7976-4a66-b62a-34efcba31d46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThgMuiyhoKcYo7imZ4ovXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 29 · 2026-05-16T09:00:58.412Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SDYgBT4fgcQYV5HPmkj4Gg`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Look for the limitations section or discussion of limitations. Does this paper acknowledge any limitations regarding overconfident hallucinations specifically? What does it say about cases where hallucinations are produced with high confidence? Quote any relevant text about limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1f9d29-7976-4a66-b62a-34efcba31d46",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yVnmNsTF38aP8EobSY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c8b4e4c-f904-4d70-88c1-bc333c335540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThgMuiyhoKcYo7imZ4ovXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 30 · 2026-05-16T09:00:59.731Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hp7Vk1AvFUuP2VJr6CXf7o`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.14477v1",
  "prompt": "What specific models was this paper tested on? What was the VUF direction result? Look for information about a \"verbal uncertainty feature\" direction and its effects. What are the key quantitative results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8b4e4c-f904-4d70-88c1-bc333c335540",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yVnmNsTF38aP8EobSY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8352fb1-b2a7-4732-8b2b-3eb0aa126ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThgMuiyhoKcYo7imZ4ovXp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 15924,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 411,
          "cache_read_input_tokens": 15924,
          "cache_creation_input_tokens": 1961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1961,
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

_source line 31 · 2026-05-16T09:01:01.461Z_

<details><summary>↩ Tool result · `toolu_017ppKvj9Y9maSb5or7VchDP`</summary>

```text
Web search results for query: "EMNLP 2025 Outstanding Paper award winners list"

Links: [{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"EMNLP 2026 on X: \"🎉 Congratulations to all #EMNLP2025 award winners 🎉 Starting with the ✨Best Paper award ✨: \"Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index\" by Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, and Hannaneh Hajishirzi https://t.co/DKYhylaopF 1/n https://t.co/lrrtlZuyWw\" / X","url":"https://x.com/emnlpmeeting/status/1986922316643651775"},{"title":"Linguistics Doctoral Student, Sasha Boguraev, wins Outstanding Paper Award at EMNLP 2025.>","url":"https://liberalarts.utexas.edu/linguistics/news/linguistics-doctoral-student-sasha-boguraev-wins-outstanding-paper-award-at-emnlp-2025"},{"title":"EMNLP 2025 on X: \"Thanks again all for a wonderful #EMNLP2025! For future reference, you can now find all accepted papers, award winners, and outstanding reviewers, area chairs, and senior area chairs on the conference website: https://t.co/dMWGwPej05\" / X","url":"https://x.com/emnlpmeeting/status/1997739138695778793"},{"title":"Freda Shi and colleagues win EMNLP 2025 Outstanding Paper Award for research on LLM meta-linguistic reasoning | Cheriton School of Computer Science | University of Waterloo","url":"https://cs.uwaterloo.ca/news/freda-shi-colleagues-win-emnlp-2025-outstanding-paper-award-research-llm-meta-linguistic-reasoning"},{"title":"Columbia Electrical Engineering Students Earn Senior Area ...","url":"https://www.ee.columbia.edu/news/columbia-electrical-engineering-students-earn-senior-area-chair-highlight-emnlp-2025"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP 2025 Highlights. I just got back from EMNLP 2025 in… | by Itay Nakash | Medium","url":"https://medium.com/@itaynakash/emnlp-2025-highlights-1d2bca37cc7a"},{"title":"🏆 EMNLP 2025 Outstanding Paper Award - Nick Clark","url":"https://nicholasclark.org/media/emnlp-outstanding-paper-2025"},{"title":"GitHub - FeijiangHan/Top-Conference-Best-Papers: A list of post-GPT-era (2022-2026) Best Paper award winners from ICLR/NeurIPS/ICML/ACL/EMNLP/NAACL/AAAI/CVPR/ECCV. · GitHub","url":"https://github.com/FeijiangHan/Top-Conference-Best-Papers"}]

Based on the search results, here's what I found about EMNLP 2025 Outstanding Paper award winners:

Professor Freda Shi and her collaborators Changbing Yang, Franklin Ma and Jian Zhu from the University of British Columbia received an Outstanding Paper Award at EMNLP 2025 for their paper "LingGym: How Far Are LLMs from Thinking Like Field Linguists?" which introduced a new benchmark evaluating how effectively large language models can perform meta-linguistic reasoning.

Sasha Boguraev, a doctoral student, also won an Outstanding Paper Award at EMNLP 2025.

Additionally, the search results mention that the Senior Area Chairs highlighted 35 papers as particularly noteworthy, though this appears to be a separate distinction from the Outstanding Paper awards.

For a complete list of all Outstanding Paper award winners, you can find all award winners on the conference website at https://2025.emnlp.org/program/awards/. The search results provided don't contain a comprehensive list of all Outstanding Paper awardees, so I'd recommend visiting that official page for the complete information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aeba007-6944-42e3-83ba-693435ab5cd7",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "2a557c0a-91ea-4d9c-82fd-1f40724397e3",
  "sourceToolAssistantUUID": "6aeba007-6944-42e3-83ba-693435ab5cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T09:01:04.873Z_

<details><summary>↩ Tool result · `toolu_01W4iYxmwjXJFAjr8c7LyxRT`</summary>

```text
Web search results for query: ""Real-Time Detection of Hallucinated Entities" EMNLP 2025 Findings obalcells hallucination_probes"

Links: [{"title":"[2509.03531] Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/abs/2509.03531"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.hallucination-probes.com/"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"The Mirage of Hallucination Detection","url":"https://aclanthology.org/2025.findings-emnlp.1035.pdf"},{"title":"Unsupervised Hallucination Detection by Inspecting Reasoning Processes - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1124/"},{"title":"[2509.03531v1] Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/abs/2509.03531v1"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.researchgate.net/publication/395270424_Real-Time_Detection_of_Hallucinated_Entities_in_Long-Form_Generation"},{"title":"GitHub - obalcells/hallucination_probes: Real-Time Detection of Hallucinated Entities in Long-Form Generation · GitHub","url":"https://github.com/obalcells/hallucination_probes"},{"title":"Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.67/"},{"title":"Re-evaluating Hallucination Detection in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1761.pdf"}]

Based on the web search results, I found information about the paper "Real-Time Detection of Hallucinated Entities in Long-Form Generation," which matches your query.

The paper is authored by Oscar Obeso and 5 other authors, with the full author list being Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda.

The work presents a cheap, scalable method for real-time identification of hallucinated tokens in long-form generations, targeting entity-level hallucinations such as fabricated names, dates, and citations rather than claim-level, thereby enabling streaming detection.

Key findings from the research include:

- Classifiers consistently outperform baselines on long-form responses, including more expensive methods such as semantic entropy (e.g., AUC 0.90 vs 0.71 for Llama-3.3-70B)
- Despite being trained only to detect hallucinated entities, the probes effectively detect incorrect answers in mathematical reasoning tasks, indicating generalization beyond entities
- The researchers developed an annotation methodology that leverages web search to annotate model responses with grounded labels, enabling training of effective hallucination classifiers with simple and efficient methods such as linear probes
- Annotated responses from one model can be used to train effective classifiers on other models, with datasets publicly released to facilitate reuse

The arXiv preprint (2509.03531) was originally posted on August 26, 2025, with a more recent version from February 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1f9d29-7976-4a66-b62a-34efcba31d46",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "80b148bb-2a99-4c1f-97b3-0c35d8393436",
  "sourceToolAssistantUUID": "8f1f9d29-7976-4a66-b62a-34efcba31d46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T09:01:05.799Z_

<details><summary>↩ Tool result · `toolu_01Hp7Vk1AvFUuP2VJr6CXf7o`</summary>

```text
# Key Findings on Verbal Uncertainty Features

## Models Tested

The research evaluated three 7B-parameter instruction-tuned models:
- Llama3.1-8B-Instruct
- Mistral-7B-Instruct-v0.3
- Qwen2.5-7B-Instruct

## VUF Direction Results

The paper discovered that "verbal uncertainty is mediated by a single direction" in the model's representation space. Through visualization using PCA, they demonstrated that activations from "certain" and "uncertain" responses "clearly linearly separated into two distinct clusters, starting from the middle layers."

The causal validation showed that manipulating this direction via the intervention equation h^(l)(x) ← h^(l)(x) + α∗r_VU^(l) successfully controlled uncertainty expression. Positive α values increased verbal uncertainty scores, while negative values decreased them.

Importantly, the VUF proved consistent across datasets, with high cosine similarity between features extracted from TriviaQA, NQ-Open, and PopQA.

## Key Quantitative Results

**Hallucination Detection:** Combining verbal and semantic uncertainty improved AUROC scores. For Llama3.1 on TriviaQA, the combined approach achieved 79.71 AUROC versus 79.21 for semantic uncertainty alone.

**Hallucination Mitigation:** The Mechanistic Uncertainty Calibration method achieved an "average relative reduction of 31.9%" in hallucinations across datasets while improving VU/SU alignment correlation from 0.34 to 0.55.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8352fb1-b2a7-4732-8b2b-3eb0aa126ab8",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "86b82067-7142-45f1-86ab-c289514e7849",
  "sourceToolAssistantUUID": "a8352fb1-b2a7-4732-8b2b-3eb0aa126ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:01:06.523Z_

<details><summary>↩ Tool result · `toolu_01SDYgBT4fgcQYV5HPmkj4Gg`</summary>

```text
# Limitations Regarding Overconfident Hallucinations

The paper includes a dedicated Limitations section that acknowledges several constraints:

**General limitations stated:**
"PCNet requires a small calibration set of labeled factual and hallucinated hidden states, which may be costly in new domains. Moreover, our evaluation is limited to models up to 8B parameters, leaving open whether geometric separation holds in larger models."

**Regarding task-specific performance:**
The authors note that "PC-LDCD gains are stronger on generative benchmarks than on exact-match tasks, suggesting it is better suited to open-ended generation than precise answers."

**On overconfident hallucinations specifically:**
The paper does not explicitly address overconfident hallucinations in its limitations section. However, the work addresses LLM overconfidence throughout—particularly noting that baseline detection methods "suffer from LLM overconfidence and require multi-pass sampling." The approach uses latent geometric anomaly detection to circumvent reliance on output-space confidence signals, which are unreliable when models hallucinate with high confidence.

The methodology implicitly handles this through density estimation over hidden states rather than token probabilities, but the limitations section doesn't directly discuss remaining challenges with high-confidence hallucinations that PCNet may still fail to detect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c8b4e4c-f904-4d70-88c1-bc333c335540",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "ad2be74c-1df5-4cfa-ae5a-c69282e34836",
  "sourceToolAssistantUUID": "4c8b4e4c-f904-4d70-88c1-bc333c335540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T09:01:09.301Z_

Let me now check the EMNLP 2025 awards page and verify the venue for paper #4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad2be74c-1df5-4cfa-ae5a-c69282e34836",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yX1wv58N5pBd3UiUbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcd0796f-9520-42a2-82b6-397c71c9b026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae3GA5Y9RoqW1pgKjSNQ8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 399,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 17885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2806,
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

_source line 36 · 2026-05-16T09:01:10.905Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Nk2RJ9Q9rnLw5HYkT3zgi`</summary>

```json
{
  "url": "https://2025.emnlp.org/program/awards/",
  "prompt": "List ALL Outstanding Paper award winners at EMNLP 2025. Is \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" by Ji et al. listed as an Outstanding Paper? What award did it win, if any?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd0796f-9520-42a2-82b6-397c71c9b026",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yX1wv58N5pBd3UiUbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d305841-32ea-46f8-ab74-efcfa4926668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae3GA5Y9RoqW1pgKjSNQ8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 399,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 17885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2806,
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

_source line 37 · 2026-05-16T09:01:12.074Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BnzeyWPSsdSxdSi1HkJPYi`</summary>

```json
{
  "url": "https://openreview.net/forum?id=YxJEMTflww",
  "prompt": "What venue is this paper published at? Is it EMNLP 2025 Findings? What are the key details about this paper's acceptance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d305841-32ea-46f8-ab74-efcfa4926668",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yX1wv58N5pBd3UiUbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dab8664a-2d1b-4eda-9632-df333d21d600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae3GA5Y9RoqW1pgKjSNQ8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 399,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 17885,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 399,
          "output_tokens": 272,
          "cache_read_input_tokens": 17885,
          "cache_creation_input_tokens": 2806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2806,
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

_source line 38 · 2026-05-16T09:01:15.665Z_

<details><summary>↩ Tool result · `toolu_01BnzeyWPSsdSxdSi1HkJPYi`</summary>

```text
Based on the content provided, this paper is submitted to **ICLR 2026 Conference**, not EMNLP 2025 Findings.

The page shows this is a submission to "ICLR 2026 Conference" as indicated by the navigation link. The submission details reveal:

- **Submission Number:** 13897
- **Submission Date:** September 18, 2025 (modified February 11, 2026)
- **Primary Area:** Interpretability and explainable AI
- **Status:** The page indicates this is a submitted paper under review

The document does not specify acceptance status. It appears to be a live submission under the OpenReview platform awaiting peer review decisions, rather than a published or accepted paper. The "Everyone" designation and presence of "Revisions" link suggest the review process is ongoing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dab8664a-2d1b-4eda-9632-df333d21d600",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "c9d04509-1bab-4f64-b17d-3865781c7510",
  "sourceToolAssistantUUID": "dab8664a-2d1b-4eda-9632-df333d21d600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T09:01:15.691Z_

<details><summary>↩ Tool result · `toolu_013Nk2RJ9Q9rnLw5HYkT3zgi`</summary>

```text
# Outstanding Papers at EMNLP 2025

The seven Outstanding Paper award winners are:

1. "LingGym: How Far Are LLMs from Thinking Like Field Linguists?"
2. "Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?"
3. "DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement"
4. "Generative or Discriminative? Revisiting Text Classification in the Era of Transformers"
5. "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps"
6. "MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning"
7. "Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions"

## Regarding the Ji et al. Paper

The paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ji et al. was **not** designated as an Outstanding Paper. Instead, it appears in the SAC Highlights section, meaning it was recognized by Senior Area Chairs as "particularly noteworthy" among 35 highlighted papers, but did not receive the Official Outstanding Paper distinction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d305841-32ea-46f8-ab74-efcfa4926668",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "579b7cef-af0d-461c-b21b-423115b8f6db",
  "sourceToolAssistantUUID": "2d305841-32ea-46f8-ab74-efcfa4926668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-16T09:01:18.595Z_

Interesting -- paper #4 appears to be under review at ICLR 2026, not published at EMNLP 2025 Findings. Let me verify this further.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "579b7cef-af0d-461c-b21b-423115b8f6db",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yXhALgAdKmWD6HVBgF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f55a7cc-33c6-4c68-be4c-de30849cf693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ysgF37iJGcQMwLATyY5Di",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 20691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 992,
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

_source line 41 · 2026-05-16T09:01:19.530Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0177Hr43PdRZfRWDHYMS7Nwb`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-emnlp.880/",
  "prompt": "What is the title of this paper? Is it \"Real-Time Detection of Hallucinated Entities in Long-Form Generation\"? Who are the authors? What venue is it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f55a7cc-33c6-4c68-be4c-de30849cf693",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yXhALgAdKmWD6HVBgF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2119f258-9334-4e83-9f8f-412f16474f14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ysgF37iJGcQMwLATyY5Di",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 20691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 992,
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

_source line 42 · 2026-05-16T09:01:20.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JvmaayHBMZxMb8cVRunvsY`</summary>

```json
{
  "query": "aclanthology \"Real-Time Detection of Hallucinated Entities\" site:aclanthology.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2119f258-9334-4e83-9f8f-412f16474f14",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yXhALgAdKmWD6HVBgF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dba04f0-423a-4a39-811e-acbddd881c7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ysgF37iJGcQMwLATyY5Di",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 20691,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 219,
          "output_tokens": 232,
          "cache_read_input_tokens": 20691,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 992,
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

_source line 43 · 2026-05-16T09:01:21.821Z_

<details><summary>↩ Tool result · `toolu_0177Hr43PdRZfRWDHYMS7Nwb`</summary>

```text
# Paper Details

**Title:** No, the title is not "Real-Time Detection of Hallucinated Entities in Long-Form Generation." The actual title is "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation."

**Authors:** The paper was written by Jiatong Han, Neil Band, Muhammed Razzak, Jannik Kossen, Tim G. J. Rudner, and Yarin Gal.

**Venue:** The work appears in the "Findings of the Association for Computational Linguistics: EMNLP 2025," held in Suzhou, China in November 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2119f258-9334-4e83-9f8f-412f16474f14",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "4758f04b-cbc0-4978-8e6e-9f62f03611b4",
  "sourceToolAssistantUUID": "2119f258-9334-4e83-9f8f-412f16474f14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T09:01:23.915Z_

<details><summary>↩ Tool result · `toolu_01JvmaayHBMZxMb8cVRunvsY`</summary>

```text
Web search results for query: "aclanthology "Real-Time Detection of Hallucinated Entities" site:aclanthology.org"

No links found.

The search didn't return any results. This could mean:

1. The exact paper title "Real-Time Detection of Hallucinated Entities" may not exist on ACL Anthology, or
2. The exact phrasing in the search query might not match how it's indexed on the site, or
3. The paper may be listed under a slightly different title

If you're looking for a paper related to detecting hallucinated entities, I'd recommend:
- Visiting aclanthology.org directly and searching for related terms like "hallucination detection" or "hallucinated entities"
- Checking if the paper title might be phrased differently
- Searching without the site restriction to see if the paper appears in other venues

Would you like me to try a different search query to help you find this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dba04f0-423a-4a39-811e-acbddd881c7c",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "ca57b46b-c7bf-4322-935b-6a88cf8b9386",
  "sourceToolAssistantUUID": "7dba04f0-423a-4a39-811e-acbddd881c7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T09:01:27.288Z_

Now let me check the GitHub repo for paper #4 to see if pretrained probes are available, and verify the CSS paper (#5) details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca57b46b-c7bf-4322-935b-6a88cf8b9386",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yYJKw7r3HUzar1ZZwA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a3e19d7-bef1-4741-a68e-13f8632901eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UcdzBfvXEWn1RWysfv1Xd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 21683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1003,
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

_source line 46 · 2026-05-16T09:01:28.470Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FqpGjWA55Phri5rBzcPHJw`</summary>

```json
{
  "url": "https://github.com/obalcells/hallucination_probes",
  "prompt": "Does this repository provide pretrained probes for download? What does the README say about pretrained probes or pretrained models? What AUROC or AUC results are reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a3e19d7-bef1-4741-a68e-13f8632901eb",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yYJKw7r3HUzar1ZZwA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc3f990d-51f0-47d5-9574-f50b5c442462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UcdzBfvXEWn1RWysfv1Xd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 21683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1003,
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

_source line 47 · 2026-05-16T09:01:29.883Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lyfzv43FxmHZFjsgCC2u3y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.17487",
  "prompt": "What are the full details of this paper? Who are the authors? What is the 0.913 utility claim exactly? What benchmarks were used? List key quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3f990d-51f0-47d5-9574-f50b5c442462",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yYJKw7r3HUzar1ZZwA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "148ae6a9-6b4e-4d17-a531-c137054b83f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UcdzBfvXEWn1RWysfv1Xd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 21683,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1003
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 21683,
          "cache_creation_input_tokens": 1003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1003,
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

_source line 48 · 2026-05-16T09:01:33.394Z_

<details><summary>↩ Tool result · `toolu_01FqpGjWA55Phri5rBzcPHJw`</summary>

```text
# Pretrained Probes and Results

**Yes, the repository provides pretrained probes for download.** According to the README, they are available at the HuggingFace model hub location: "Pretrained hallucination detection probes for various LLMs are available at: [obalcells/hallucination-probes](https://huggingface.co/obalcells/hallucination-probes)"

The README describes three types of probes offered:
- "Linear probes (`*_linear`): Simple linear classifiers trained on model hidden states"
- "LoRA probes with KL regularization (`*_lora_lambda_kl_0_05`): LoRA adapters with KL divergence regularization"
- "LoRA probes with LM regularization (`*_lora_lambda_lm_0_01`): LoRA adapters with cross-entropy loss regularization"

These are provided for five supported models including Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B, Mistral Small 24B, and Qwen 2.5 7B.

**However, the README does not report AUROC or AUC results.** Performance metrics appear to be presented in the associated research paper rather than in this repository's documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3f990d-51f0-47d5-9574-f50b5c442462",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "c8bf6236-b431-492f-bc2f-cf8499314105",
  "sourceToolAssistantUUID": "fc3f990d-51f0-47d5-9574-f50b5c442462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T09:01:34.737Z_

<details><summary>↩ Tool result · `toolu_01Lyfzv43FxmHZFjsgCC2u3y`</summary>

```text
# Paper Details: Calibrated Claim-Level Specificity Control for Agentic Systems

## Authors
- Tianyi Huang
- Samuel Xu
- Jason Tansong Dang
- Samuel Yan
- Kimberley Yin

## Core Innovation
The paper introduces **Compositional Selective Specificity (CSS)**, described as "a post-generation layer that decomposes an answer into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level that appears admissible."

## The 0.913 Utility Metric
On the full LongFact evaluation, the method achieved an "overcommitment-aware utility" increase from 0.846 to 0.913 while maintaining 0.938 specificity retention. This addresses the problem where agentic systems "fail not by being entirely wrong, but by being too precise."

## Benchmarks Used
- **LongFact** (full run)
- **HotpotQA** (pilot studies)

## Key Quantitative Results
- Utility improvement: 0.846 → 0.913 (LongFact)
- Specificity retention: 0.938
- The approach expresses uncertainty through "local semantic backoff rather than as a whole-answer refusal"

## Submission Details
- **arXiv ID**: 2604.17487
- **Field**: Computation and Language (cs.CL)
- **Submitted**: April 19, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "148ae6a9-6b4e-4d17-a531-c137054b83f2",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a836d5ba67e75fa6c",
  "type": "user",
  "uuid": "0bf0057f-f984-4fba-a52d-1100ede7496b",
  "sourceToolAssistantUUID": "148ae6a9-6b4e-4d17-a531-c137054b83f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-16T09:02:29.266Z_

Now I have comprehensive information on all five papers. Here is my full report.

---

## Verification Report: Five Cited Papers

### Paper 1: "Endogenous Resistance to Activation Steering in Language Models" (arXiv 2602.06941, Feb 2026)

**VERDICT: EXISTS. Claims appear accurate.**

- The paper exists at [arXiv:2602.06941](https://arxiv.org/abs/2602.06941), submitted February 6, 2026.
- Authors: Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, and Michael S. A. Graziano.
- It introduces "Endogenous Steering Resistance (ESR)" -- the finding that LLMs can resist task-misaligned activation steering during inference, sometimes recovering mid-generation. Llama-3.3-70B shows substantial ESR, while smaller models (Llama-3 and Gemma-2 families) exhibit it less frequently.
- They identified 26 SAE latents causally linked to ESR. Zero-ablating these reduces the multi-attempt rate by 25%.

---

### Paper 2: "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" (Ji et al., EMNLP 2025)

**VERDICT: EXISTS, but the "Outstanding Paper" claim is INCORRECT.**

- The paper exists at [arXiv:2503.14477](https://arxiv.org/abs/2503.14477) and was published in EMNLP 2025 main conference proceedings ([ACL Anthology](https://aclanthology.org/2025.emnlp-main.187/)).
- Authors: Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda.
- **Award status: It received a "SAC Highlight" (Senior Area Chair Highlight), NOT the "Outstanding Paper" award.** The EMNLP 2025 Outstanding Paper awards went to 7 other papers (including "LingGym," "Mind the Value-Action Gap," etc.). The SAC Highlight is a tier below -- 35 papers were highlighted as "particularly noteworthy," but this is a distinct and lesser recognition than Outstanding Paper. **The proposal's claim of "Outstanding Paper" is an exaggeration.**
- Models tested: Three 7B-class instruction-tuned models -- Llama3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct.
- VUF direction result: They found verbal uncertainty is mediated by a single linear direction in the representation space. Activations from "certain" vs. "uncertain" responses are linearly separable starting from middle layers. Manipulating this direction causally controls uncertainty expression, and the direction shows high cosine similarity across datasets (TriviaQA, NQ-Open, PopQA).
- Key results: ~31.9% average relative reduction in hallucinations; VU/SU alignment correlation improved from 0.34 to 0.55; combined verbal+semantic uncertainty achieved 79.71 AUROC on TriviaQA for Llama3.1 (vs. 79.21 for semantic uncertainty alone).

---

### Paper 3: "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (Nielsen et al., arXiv 2605.05953, May 2026)

**VERDICT: EXISTS. Results are largely as described, but limitation acknowledgment is weak.**

- The paper exists at [arXiv:2605.05953](https://arxiv.org/abs/2605.05953), submitted May 7, 2026.
- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, and Giovanni Iacca.
- It proposes PCNET (a Probabilistic Circuit trained as a density estimator over the LLM residual stream) and PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding).
- Key results: AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA; mean corruption rate reduced to 53.7%; preservation rate of 79.3%; highest True+Info, MC2, MC3 scores on TruthfulQA in 3 of 4 models.
- Models tested: Four LLMs from 1B to 8B parameters. Benchmarks: CoQA, SQuAD v2.0, TriviaQA, TruthfulQA.
- **Regarding overconfident hallucinations:** The paper mentions that baseline methods "suffer from LLM overconfidence and require multi-pass sampling," and their approach uses hidden-state geometry rather than output-space confidence. However, the **Limitations section does NOT explicitly acknowledge remaining challenges with overconfident hallucinations**. It only notes: (1) calibration set requirements may be costly in new domains, (2) evaluation limited to 8B models, and (3) gains are stronger on generative benchmarks than exact-match tasks. If the proposal claims this paper "acknowledges limitations with overconfident hallucinations," that is an overstatement -- it addresses the problem but does not flag it as a remaining limitation of their own method.

---

### Paper 4: "Real-Time Detection of Hallucinated Entities in Long-Form Generation" (obalcells et al.)

**VERDICT: EXISTS, but the venue claim of "EMNLP 2025 Findings" is UNVERIFIED/LIKELY INCORRECT.**

- The paper exists at [arXiv:2509.03531](https://arxiv.org/abs/2509.03531), submitted August 26, 2025, revised February 5, 2026.
- Authors: Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda.
- **Venue problem:** The paper does NOT appear in ACL Anthology under EMNLP 2025 Findings. A search for it on aclanthology.org returned no results. The OpenReview page (forum ID YxJEMTflww) indicates it was submitted to **ICLR 2026**, not EMNLP 2025 Findings. There is a *different* paper at EMNLP 2025 Findings with a similar title -- "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation" by Han et al. (aclanthology.org/2025.findings-emnlp.880). **The proposal's venue claim appears to be wrong.**
- **Pretrained probes: YES.** The [GitHub repo](https://github.com/obalcells/hallucination_probes) confirms pretrained probes are available on HuggingFace (obalcells/hallucination-probes) for Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B, Mistral Small 24B, and Qwen 2.5 7B. Linear probes and LoRA probes are provided.
- **AUC results:** The paper reports AUC 0.90 for Llama-3.3-70B (vs. 0.71 for semantic entropy baseline). Note this is reported as "AUC," not "AUROC" -- the proposal should use the paper's own terminology.

---

### Paper 5: "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control" (CSS, arXiv 2604.17487, April 2026)

**VERDICT: EXISTS. The 0.913 claim checks out.**

- The paper exists at [arXiv:2604.17487](https://arxiv.org/abs/2604.17487), submitted April 19, 2026.
- Authors: Tianyi Huang, Samuel Xu, Jason Tansong Dang, Samuel Yan, Kimberley Yin.
- It introduces Compositional Selective Specificity (CSS), a post-generation layer that decomposes answers into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level.
- **The 0.913 claim:** On LongFact, CSS raises "overcommitment-aware utility" from 0.846 to 0.913, with 0.938 specificity retention. This is confirmed. Note this is a specific metric ("overcommitment-aware utility"), not a general accuracy or F1 score -- the proposal should describe it precisely.
- Benchmarks: LongFact (full run) and HotpotQA (pilots).

---

## Summary of Red Flags for the Proposal

1. **Paper #2 (Ji et al.):** The claim of "EMNLP 2025 Outstanding Paper" is **false**. It received a SAC Highlight, which is a lesser distinction. This is a material misrepresentation of the paper's recognition.

2. **Paper #4 (obalcells et al.):** The claim of "EMNLP 2025 Findings" venue is **likely false**. The paper does not appear in ACL Anthology for EMNLP 2025 and appears to be under review at ICLR 2026. The proposal may be confusing it with the similar Han et al. paper at EMNLP Findings.

3. **Paper #3 (Nielsen et al.):** If the proposal claims this paper "acknowledges limitations with overconfident hallucinations," that is an overstatement. The paper addresses overconfidence as a problem with *baselines* but does not flag it as a remaining limitation of their own approach.

4. **Paper #4 AUC vs AUROC:** The paper reports "AUC 0.90," and the proposal should not inflate this to "AUROC" without verification that they are using the same metric definition.

Sources:
- [arXiv:2602.06941 - Endogenous Resistance to Activation Steering](https://arxiv.org/abs/2602.06941)
- [arXiv:2503.14477 - Calibrating Verbal Uncertainty](https://arxiv.org/abs/2503.14477)
- [ACL Anthology - Ji et al. EMNLP 2025](https://aclanthology.org/2025.emnlp-main.187/)
- [EMNLP 2025 Awards Page](https://2025.emnlp.org/program/awards/)
- [arXiv:2605.05953 - Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [arXiv:2509.03531 - Real-Time Detection of Hallucinated Entities](https://arxiv.org/abs/2509.03531)
- [OpenReview - ICLR 2026 submission](https://openreview.net/forum?id=YxJEMTflww)
- [GitHub - obalcells/hallucination_probes](https://github.com/obalcells/hallucination_probes)
- [arXiv:2604.17487 - Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)
- [ACL Anthology - EMNLP 2025 Findings paper 880 (different paper)](https://aclanthology.org/2025.findings-emnlp.880/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bf0057f-f984-4fba-a52d-1100ede7496b",
  "isSidechain": true,
  "agentId": "a836d5ba67e75fa6c",
  "requestId": "req_011Cb5yZ6YneqPZ5CcCJcTiq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e49e4eba-3f0c-4291-82ca-721556c2d0ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZRhRz7oCjwPTzNhBhQDqP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 22686,
      "output_tokens": 2848,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2848,
          "cache_read_input_tokens": 22686,
          "cache_creation_input_tokens": 979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 979,
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
