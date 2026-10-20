# Research conversation: Use WebSearch to check feasibility for a research project on "latent trajectory steering for hallucination suppression".

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-add726fd536cd70e2.jsonl`
- **Structured JSON:** [`30d8fd52f23f56b661aa.json`](../../sessions/30/30d8fd52f23f56b661aa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-16T05:57:01.972Z_

Use WebSearch to check feasibility for a research project on "latent trajectory steering for hallucination suppression". I need:

1. Search "github.com activation steering hallucination" or "github.com ITI truthful" - are there reference implementations of activation steering (like ITI or ACT)?

2. Search "github.com TransformerLens steering vectors" - what infrastructure exists for extracting and applying steering vectors layer-by-layer?

3. Search for TruthfulQA baseline numbers - what are the current SOTA scores on TruthfulQA for activation steering methods? Search "TruthfulQA state of the art 2025 2026"

4. Search for "FELM benchmark" or "FactScore" or claim-level hallucination benchmarks - what datasets exist for claim-level hallucination evaluation?

5. Search "GPU hours activation steering experiments" or check papers for computational cost of running steering vector experiments on 7B-70B models.

6. Search "hallucination basins github" or any implementation of the April 2026 paper.

Report what you find about existing implementations, baseline numbers to beat, available datasets, and computational requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "c04a2b66-7fe7-4a8a-a8be-c72fd269d627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T05:57:01.976Z_

```json
{
  "parentUuid": "c04a2b66-7fe7-4a8a-a8be-c72fd269d627",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
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
  "uuid": "a7132399-8f93-447d-9b66-1c9e9391ab2f",
  "timestamp": "2026-05-16T05:57:01.976Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T05:57:05.125Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AjQ2scTzqu7q6AE6Dt6ceA`</summary>

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
  "parentUuid": "a7132399-8f93-447d-9b66-1c9e9391ab2f",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jUsxGXNrSVNQLBgdNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0c9ed12-3a59-4be6-9ac8-e8f7a68f8681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdS67Qgx2SbpkN9JNwgcKQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 813,
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

_source line 4 · 2026-05-16T05:57:05.128Z_

<details><summary>↩ Tool result · `toolu_01AjQ2scTzqu7q6AE6Dt6ceA`</summary>

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
  "parentUuid": "e0c9ed12-3a59-4be6-9ac8-e8f7a68f8681",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "974ed877-7517-46b9-bc84-77cd6f189592",
  "sourceToolAssistantUUID": "e0c9ed12-3a59-4be6-9ac8-e8f7a68f8681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T05:57:08.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GaH5DQ5ZPK6sUtu2yG1gNx`</summary>

```json
{
  "query": "github.com activation steering hallucination ITI truthful",
  "allowed_domains": [
    "github.com"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "974ed877-7517-46b9-bc84-77cd6f189592",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f5eacc1-a08d-4eb7-9089-c49ea2633d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 6 · 2026-05-16T05:57:08.859Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RC6aAFPHd51AbxExJ2f9uC`</summary>

```json
{
  "query": "github.com TransformerLens steering vectors",
  "allowed_domains": [
    "github.com"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f5eacc1-a08d-4eb7-9089-c49ea2633d33",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feaef708-fc5a-43e6-85da-a27b3145404d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 7 · 2026-05-16T05:57:09.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WKZnYV9zrRbcPdx642JwCY`</summary>

```json
{
  "query": "TruthfulQA state of the art 2025 2026 activation steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feaef708-fc5a-43e6-85da-a27b3145404d",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f87be95-3c6a-4bff-ab98-7e84d88df59f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 8 · 2026-05-16T05:57:09.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnyhxgEZckrgqWoDrB4MfD`</summary>

```json
{
  "query": "FELM benchmark FactScore claim-level hallucination evaluation dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f87be95-3c6a-4bff-ab98-7e84d88df59f",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17e9d70a-adf9-4af8-84ba-d6c8dd45eb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 9 · 2026-05-16T05:57:10.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfnoD82ZTS2cjJy5o16iie`</summary>

```json
{
  "query": "GPU hours activation steering experiments 7B 70B models computational cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17e9d70a-adf9-4af8-84ba-d6c8dd45eb60",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ed28415-9c18-4b2e-aedc-97f47f894c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 10 · 2026-05-16T05:57:10.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KCZHiHhw7csL2pTQgKMxz1`</summary>

```json
{
  "query": "hallucination basins github April 2026 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ed28415-9c18-4b2e-aedc-97f47f894c34",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jV7a4XbyQ8cNUrZAx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71dc5978-5e6f-45df-861e-26a2a0344bc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLALZVECbgANg4Vsqtvoum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9036,
      "output_tokens": 350,
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
          "output_tokens": 350,
          "cache_read_input_tokens": 9036,
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

_source line 11 · 2026-05-16T05:57:15.024Z_

<details><summary>↩ Tool result · `toolu_01GaH5DQ5ZPK6sUtu2yG1gNx`</summary>

```text
Web search results for query: "github.com activation steering hallucination ITI truthful"

Links: [{"title":"GitHub - shengliu66/VTI: Code for Reducing Hallucinations in Vision-Language Models via Latent Space Steering · GitHub","url":"https://github.com/shengliu66/VTI"},{"title":"GitHub - tianlwang/ACT","url":"https://github.com/tianlwang/ACT"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"GitHub - shyanasri/DetectLLMHallucination: Detecting hallucinations in LLMs with automated annotated datasets and a LSTM based classifier.","url":"https://github.com/shyanasri/DetectLLMHallucination"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-representation-engineering"},{"title":"GitHub - nrimsky/CAA: Steering Llama 2 with Contrastive Activation Addition · GitHub","url":"https://github.com/nrimsky/CAA"},{"title":"GitHub - ZFancy/awesome-activation-engineering: A curated list of resources for activation engineering · GitHub","url":"https://github.com/ZFancy/awesome-activation-engineering"},{"title":"GitHub - GaurangSriramanan/LLM_Check_Hallucination_Detection: LLM-Check: Investigating Detection of Hallucinations in Large Language Models (NeurIPS 2024) · GitHub","url":"https://github.com/GaurangSriramanan/LLM_Check_Hallucination_Detection"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"}]

Based on the web search results, here are the key findings related to your query about activation steering, hallucination, ITI, and truthfulness:

## Key GitHub Repositories and Research

1. **Adaptive Activation Steering (ACT)** - This repository provides code for the paper "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories".

2. **Inference-Time Intervention (ITI)** - ITI is a technique designed to enhance the truthfulness of large language models by shifting model activations during inference, following a set of directions across a limited number of attention heads. This intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark.

3. **Vision and Textual Intervention (VTI)** - VTI is a novel technique designed to reduce hallucinations by steering latent space representations during inference to enhance the stability of vision features.

4. **Hallucination Detection and Mitigation** - The search results reveal multiple approaches including:
   - Using dual-task feature modeling, spectral clustering, and attention head saliency scoring to identify and edit shared activation subspaces
   - Analyzing hallucination detection within a single LLM response using internal attention kernel maps, hidden activations and output prediction probabilities

These repositories and methods collectively focus on using activation steering techniques to improve model truthfulness and reduce hallucinations in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f5eacc1-a08d-4eb7-9089-c49ea2633d33",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "4dace169-9e61-4c8c-865b-ccac280b61c5",
  "sourceToolAssistantUUID": "0f5eacc1-a08d-4eb7-9089-c49ea2633d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:57:15.120Z_

<details><summary>↩ Tool result · `toolu_01KCZHiHhw7csL2pTQgKMxz1`</summary>

```text
Web search results for query: "hallucination basins github April 2026 paper"

Links: [{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2604.04743] Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/abs/2604.04743"},{"title":"GitHub - hukcc/Awesome-Video-Hallucination: [ACL 2026] Paper list of Video LLM hallucination. Welcome to Star and Contribute! · GitHub","url":"https://github.com/hukcc/Awesome-Video-Hallucination"},{"title":"GitHub - facebookresearch/HalluLens: Codebase for LLM Textual Hallucination Benchmark · GitHub","url":"https://github.com/facebookresearch/HalluLens"},{"title":"hallucination · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination?o=asc&s=forks"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"GitHub - showlab/Awesome-MLLM-Hallucination: 📖 A curated list of resources dedicated to hallucination of multimodal large language models (MLLM).","url":"https://github.com/showlab/awesome-mllm-hallucination"},{"title":"GitHub - aisoc-lab/low-resource-hallucination-detection · GitHub","url":"https://github.com/aisoc-lab/low-resource-hallucination-detection"},{"title":"What does it mean LLM's hallucination?","url":"https://github.com/SalvatoreRa/artificial-intelligence-articles/blob/main/articles/LLM_hallucinations.md"},{"title":"Are you hallucinated? Insights into large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525002115"}]

Based on the search results, I found information about the paper you're looking for:

The "Hallucination Basins" paper by K. Cherukuri and L. R. Varshney was published on arXiv:2604.04743 in 2026. More specifically, it was submitted on Monday, April 6, 2026.

The paper is titled "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations".

All code, data, and figures are publicly available at https://github.com/akarlaraytu/trajectory-commitment.

The paper appears to be cited in another related work on arXiv that discusses hallucinations in transformer generation and focuses on understanding hallucination as trajectory commitment in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71dc5978-5e6f-45df-861e-26a2a0344bc1",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "68f9649c-185b-4a20-926f-536c0ad373b6",
  "sourceToolAssistantUUID": "71dc5978-5e6f-45df-861e-26a2a0344bc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T05:57:16.223Z_

<details><summary>↩ Tool result · `toolu_01RC6aAFPHd51AbxExJ2f9uC`</summary>

```text
Web search results for query: "github.com TransformerLens steering vectors"

Links: [{"title":"GitHub - steering-vectors/steering-vectors: Steering vectors for transformer language models in Pytorch / Huggingface · GitHub","url":"https://github.com/steering-vectors/steering-vectors"},{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"steering-vectors · GitHub","url":"https://github.com/steering-vectors"},{"title":"GitHub - callummcdougall/TransformerLens-intro · GitHub","url":"https://github.com/callummcdougall/TransformerLens-intro"},{"title":"GitHub - DylanCope/llm-steering","url":"https://github.com/DylanCope/llm-steering"},{"title":"SAELens/tutorials/tutorial_2_0.ipynb at main · decoderesearch/SAELens","url":"https://github.com/jbloomAus/SAELens/blob/main/tutorials/tutorial_2_0.ipynb"},{"title":"TransformerLensOrg · GitHub","url":"https://github.com/transformerlensorg"},{"title":"[Proposal] Add MVP Support For 1-2 Models Per-Modality · Issue #710 · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/issues/710"},{"title":"style-vectors-for-steering-llms/scripts/evaluation/csv_to_excel_shakes.py at main · DLR-SC/style-vectors-for-steering-llms","url":"https://github.com/DLR-SC/style-vectors-for-steering-llms/blob/main/scripts/evaluation/csv_to_excel_shakes.py"},{"title":"GitHub - UKGovernmentBEIS/vllm-lens: Extract residual-stream activations and apply steering vectors (including activation oracles) to any vLLM model during inference. · GitHub","url":"https://github.com/UKGovernmentBEIS/vllm-lens"}]

Based on the search results, here's what I found regarding TransformerLens and steering vectors:

## Main Resources

**TransformerLens Library**: TransformerLens is a library for mechanistic interpretability of GPT-style language models that lets you load in 50+ different open source language models and exposes the internal activations of the model to you. You can cache any internal activation in the model, and add in functions to edit, remove or replace these activations as the model runs.

**Steering Vectors with TransformerLens**: Several projects use TransformerLens for steering vector applications:

1. **Algebraic Value Editing**: One approach involves the injection of activation vectors into the forward passes of language models like GPT-2 using the hooking functionality of transformer_lens.

2. **Dedicated Steering Vectors Library**: There's a separate library that provides utilities for training and applying steering vectors to language models (LMs) from Huggingface, like GPT, LLaMa, Gemma, Mistral, Pythia, and many more.

3. **SAE-based Steering**: Once you've found a feature in a Sparse Autoencoder, you can use it to steer a model by finding the maximum activation of a feature in a set of text, using this as the default scale, multiplying it by the vector representing the feature (as extracted from the decoder weights), and finally multiplying this by a parameter that you control.

The main GitHub repositories are:
- **TransformerLens**: https://github.com/TransformerLensOrg/TransformerLens
- **Steering Vectors**: https://github.com/steering-vectors/steering-vectors


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feaef708-fc5a-43e6-85da-a27b3145404d",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "41f18beb-34f9-4f83-968d-037eac797acd",
  "sourceToolAssistantUUID": "feaef708-fc5a-43e6-85da-a27b3145404d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:57:16.507Z_

<details><summary>↩ Tool result · `toolu_01WKZnYV9zrRbcPdx642JwCY`</summary>

```text
Web search results for query: "TruthfulQA state of the art 2025 2026 activation steering"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169"},{"title":"Steering Awareness: Models Can Be Trained to Detect Activation Steering","url":"https://arxiv.org/html/2511.21399v2"},{"title":"STEERING LLMS' REASONING WITH ACTIVATION STATE ...","url":"https://openreview.net/pdf/2baa53590dfc18e67a7b74ef37709ce5aa2ec840.pdf"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714640"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment | OpenReview","url":"https://openreview.net/forum?id=CFewUmgIIL"},{"title":"Activation steering for LLM alignment","url":"https://openreview.net/pdf/f933859674dd8327470d752a7fe861e73fd6b6b2.pdf"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"}]

Based on the search results, here are the key state-of-the-art findings on TruthfulQA with activation steering in 2025-2026:

## Recent Methods and Performance

ODESteer achieves a notable 5.7% improvement over TruthfulQA compared to state-of-the-art activation steering methods. This method proposes a unified ODE-based theoretical framework for activation steering where identifying steering directions becomes equivalent to designing a barrier function from control theory.

Spherical Steering, a geometry-aware activation rotation approach, consistently improves accuracy on the TruthfulQA dataset while simultaneously enhancing open-ended generation quality.

SADI's dynamic intervention achieves improvements up to +10.08 on the True×Info metric for TruthfulQA, underscoring generalizability through effective tailoring of activations to task-specific semantics.

## Recent Key Developments (2025-2026)

The single most important development in steering over the past year is Conditional Activation Steering (CAST), presented at ICLR 2025 as a spotlight paper. CAST solves the problem of vanilla steering always being "on" by analyzing activation patterns during inference to decide whether to steer, projecting the hidden state onto a "condition vector".

Steering Vector Fields (proposed Feb 2026) learn a differentiable scoring function whose gradient defines the steering direction at each activation, instead of applying a static vector uniformly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f87be95-3c6a-4bff-ab98-7e84d88df59f",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "ac726524-6b16-430e-ad9a-dbb23affddaa",
  "sourceToolAssistantUUID": "4f87be95-3c6a-4bff-ab98-7e84d88df59f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T05:57:17.695Z_

<details><summary>↩ Tool result · `toolu_01SnyhxgEZckrgqWoDrB4MfD`</summary>

```text
Web search results for query: "FELM benchmark FactScore claim-level hallucination evaluation dataset"

Links: [{"title":"FELM: Benchmarking Factuality Evaluation of Large Language Models Shiqi Chen1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8b8a7960d343e023a6a0afe37eee6022-Paper-Datasets_and_Benchmarks.pdf"},{"title":"FELM: Benchmarking Factuality Evaluation of Large Language Models","url":"https://arxiv.org/html/2310.00741"},{"title":"HalluLens: LLM Hallucination Benchmark","url":"https://arxiv.org/html/2504.17550v1"},{"title":"RealFactBench: A Benchmark for Evaluating Large ...","url":"https://arxiv.org/pdf/2506.12538"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Knowledge Graphs, Large Language Models, and Hallucinations: An NLP Perspective","url":"https://arxiv.org/pdf/2411.14258"},{"title":"HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs","url":"https://arxiv.org/html/2605.02443"},{"title":"Hallucination to truth: a review of fact-checking and factuality evaluation in large language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11454-w"},{"title":"(PDF) DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation","url":"https://www.researchgate.net/publication/381405056_DefAn_Definitive_Answer_Dataset_for_LLMs_Hallucination_Evaluation"},{"title":"Towards Unification of Hallucination Detection and Fact ...","url":"https://arxiv.org/pdf/2512.02772"}]

Based on the search results, here's what I found about the FELM benchmark, FactScore, and claim-level hallucination evaluation:

## FELM Benchmark

FELM (Factuality Evaluation of Large Language Models) addresses the known issue of LLMs' tendency to generate falsehoods or hallucinate contents. FELM defines factuality as whether synthetic text contains any factual errors or not, and these errors can take various forms, such as an incorrect entity, a fabricated paper reference, a misleading scientific claim, unlogical reasoning, and incorrect mathematical calculations.

## Dataset Design and Error Types

FELM emphasizes a comprehensive concept of factuality, encompassing five diverse and realistic domains. The dataset predefines four types of factual errors: (1) "Knowledge error" occurring when the model produces hallucinated or inaccurate information, (2) "Reasoning error" arising when a claim employs flawed reasoning or faulty logic (including math and reasoning domain errors), and (3) "Irrelevant" denoting content unrelated to the prompt.

## Annotation and Fine-grained Evaluation

The factuality annotations are supplemented by predefined error types and reference links that either support or contradict the statement.

## Performance Findings

Experiments investigated the performance of several LLM-based factuality evaluators on FELM, including both vanilla LLMs and those augmented with retrieval mechanisms and chain-of-thought processes, revealing that while retrieval aids factuality evaluation, current LLMs are far from satisfactory to faithfully detect factual errors.

The FELM dataset is available at https://github.com/hkust-nlp/felm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17e9d70a-adf9-4af8-84ba-d6c8dd45eb60",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "587e6bdf-93ae-48b7-9e23-3e66f81049b0",
  "sourceToolAssistantUUID": "17e9d70a-adf9-4af8-84ba-d6c8dd45eb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:57:23.166Z_

<details><summary>↩ Tool result · `toolu_01BfnoD82ZTS2cjJy5o16iie`</summary>

```text
Web search results for query: "GPU hours activation steering experiments 7B 70B models computational cost"

Links: [{"title":"Seaweed-7B: Cost-Effective Training of Video Generation Foundation Model","url":"https://arxiv.org/html/2504.08685v1"},{"title":"The Complete Guide to GPU Requirements for LLM Fine-Tuning | Runpod Blog","url":"https://www.runpod.io/blog/llm-fine-tuning-gpu-guide"},{"title":"7 Best GPU for LLM in 2026 (Including Local LLM Setups) - Fluence","url":"https://www.fluence.network/blog/best-gpu-for-llm/"},{"title":"GPU Options for Finetuning Large Models: Choose the Right Setup | DigitalOcean","url":"https://www.digitalocean.com/resources/articles/gpu-options-finetuning"},{"title":"Local LLM Hardware Guide 2025: GPU Specs & Pricing | Introl Blog","url":"https://introl.com/blog/local-llm-hardware-pricing-guide-2025"},{"title":"GPU Requirements 2026: Llama 4 = 1× H100 ($2.50/hr), DeepSeek V3.2 = 8× H200 ($36/hr), Qwen 3.5 27B = 1× H100 | Spheron Blog","url":"https://www.spheron.network/blog/gpu-requirements-cheat-sheet-2026/"},{"title":"Best GPU for Fine-Tuning 70B Models: H100 vs A100... | Lyceum Technology","url":"https://lyceum.technology/magazine/which-gpu-for-fine-tuning-70b-model/"},{"title":"GPU requirements and cost for training 7B LLaMA 2 model","url":"https://www.facebook.com/groups/artificialintelligence.lt/posts/8519734168087012/"},{"title":"Efficiently Training 7B LLM with 1 Million Sequence Length on 8 GPUs","url":"https://arxiv.org/html/2407.12117v1"},{"title":"The Real Cost of Fine-Tuning LLMs: What You Need to Know | Scopic","url":"https://scopicsoftware.com/blog/cost-of-fine-tuning-llms/"}]

I found search results related to GPU computational costs for 7B and 70B models, though the results don't specifically focus on "activation steering experiments" as a particular research area. Here's what the search revealed:

## GPU Hours and Computational Costs

**7B Models:**
A 7 billion parameter model (Seaweed-7B) was trained from scratch using 665,000 H100 GPU hours for a video generation foundation model. For fine-tuning, fine-tuning 7B–13B models typically fits on a single A100 40GB ($1.90–$3.50/hr) or an RTX 4090 ($0.34–$1.99/hr).

**70B Models:**
For 70B fine-tuning, dual A100 80GBs or a Fluence H100 ($1.99–$2.56/hr) is recommended. More specifically, QLoRA (4-bit) reduces the weight footprint to ~35GB, allowing 70B fine-tuning on a single 80GB GPU or dual 48GB GPUs.

## Memory Requirements

Full fine-tuning of a 7B model in FP16 typically requires 100–120 GB of VRAM (around 16 GB per billion parameters, including weights, gradients, and optimizer states), while a 70B model needs ~70 GB in FP8.

The search results don't contain specific information about "activation steering experiments" as a research methodology or their particular computational costs. If you're looking for research papers on activation steering specifically, you may want to search academic databases or arXiv directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ed28415-9c18-4b2e-aedc-97f47f894c34",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "5c1f7fcb-1de2-4c22-a032-761a28bea44f",
  "sourceToolAssistantUUID": "5ed28415-9c18-4b2e-aedc-97f47f894c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T05:57:26.108Z_

Now let me search for a few more specific details to round out the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1f7fcb-1de2-4c22-a032-761a28bea44f",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jWSNw7tHWHfDsvnive",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c0dd3ac-909f-46d3-b36a-813c982a17f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JtsdWHh78CtRqxxp7W6Rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 5169,
      "cache_read_input_tokens": 10428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5169,
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

_source line 18 · 2026-05-16T05:57:27.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KP6xYSQAd7jwD3mTDYXjPE`</summary>

```json
{
  "query": "github likenneth honest_llama ITI TruthfulQA results performance numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c0dd3ac-909f-46d3-b36a-813c982a17f1",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jWSNw7tHWHfDsvnive",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d745035-dc64-4949-868b-3d42c2f761c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JtsdWHh78CtRqxxp7W6Rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 5169,
      "cache_read_input_tokens": 10428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5169,
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

_source line 19 · 2026-05-16T05:57:27.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BxuejvBCQ1D5Phud5RRK5x`</summary>

```json
{
  "query": "github steering-vectors library PyPI extract apply layer by layer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d745035-dc64-4949-868b-3d42c2f761c5",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jWSNw7tHWHfDsvnive",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cc033ca-d1dd-4827-adb2-c4b63cee6fae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JtsdWHh78CtRqxxp7W6Rdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 5169,
      "cache_read_input_tokens": 10428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5169,
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

_source line 20 · 2026-05-16T05:57:28.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JU65WE3DhjoKF27R2f59yw`</summary>

```json
{
  "query": "ACT adaptive activation steering TruthfulQA MC1 MC2 scores results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc033ca-d1dd-4827-adb2-c4b63cee6fae",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jWSNw7tHWHfDsvnive",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ee2ef85-b453-4cfc-83a9-2df42222315f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JtsdWHh78CtRqxxp7W6Rdw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 5169,
      "cache_read_input_tokens": 10428,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 781,
          "output_tokens": 189,
          "cache_read_input_tokens": 10428,
          "cache_creation_input_tokens": 5169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5169,
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

_source line 21 · 2026-05-16T05:57:33.762Z_

<details><summary>↩ Tool result · `toolu_01KP6xYSQAd7jwD3mTDYXjPE`</summary>

```text
Web search results for query: "github likenneth honest_llama ITI TruthfulQA results performance numbers"

Links: [{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"honest_llama/validation/iti_replication_results.md at master · likenneth/honest_llama","url":"https://github.com/likenneth/honest_llama/blob/master/validation/iti_replication_results.md"},{"title":"honest_llama/README.md at master · likenneth/honest_llama","url":"https://github.com/likenneth/honest_llama/blob/master/README.md"},{"title":"likenneth/honest_llama2_chat_7B · Hugging Face","url":"https://huggingface.co/likenneth/honest_llama2_chat_7B"},{"title":"jujipotle/honest_llama_7B · Hugging Face","url":"https://huggingface.co/jujipotle/honest_llama_7B"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/html/2306.03341"},{"title":"README.md · likenneth/honest_llama2_chat_7B at main","url":"https://huggingface.co/likenneth/honest_llama2_chat_7B/blob/main/README.md"},{"title":"jujipotle/honest_llama3_70B_instruct · Hugging Face","url":"https://huggingface.co/jujipotle/honest_llama3_70B_instruct"},{"title":"honest_llama/utils.py at master · likenneth/honest_llama","url":"https://github.com/likenneth/honest_llama/blob/master/utils.py"},{"title":"GitHub - klae01/honest_llama_jailbreak: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://github.com/klae01/honest_llama_jailbreak"}]

Based on the search results, here's what I found about the likenneth/honest_llama ITI (Inference-Time Intervention) results on TruthfulQA:

## Overview
The ITI intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark.

## Performance Numbers
On an instruction-finetuned LLaMA called Alpaca, ITI improves its truthfulness from ... 65.1%. (Note: The exact baseline percentage appears to be truncated in the available text.)

## Replication Results
As part of a summer research project, replication of ITI on Llama 2 and 3 models used the same intervention (alpha=15, heads=48) and averaged scores across seeds 1-3, with results showing an increase in the MC1 and MC2 scores for each model. For the smaller models (llama2_chat_7B, llama3_8B_instruct), the truth score also shows substantial improvement.

## Key Characteristics
ITI is minimally invasive and computationally inexpensive, and the technique is data efficient, locating truthful directions using only few hundred examples. A tradeoff between truthfulness and helpfulness is identified and can be balanced by tuning the intervention strength.

For more detailed performance numbers, you can check the replication results directly in the [GitHub repository's iti_replication_results.md file](https://github.com/likenneth/honest_llama/blob/master/validation/iti_replication_results.md).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d745035-dc64-4949-868b-3d42c2f761c5",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "544cac17-82f1-45de-9afe-5946533d8663",
  "sourceToolAssistantUUID": "3d745035-dc64-4949-868b-3d42c2f761c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:57:34.045Z_

<details><summary>↩ Tool result · `toolu_01JU65WE3DhjoKF27R2f59yw`</summary>

```text
Web search results for query: "ACT adaptive activation steering TruthfulQA MC1 MC2 scores results 2025"

Links: [{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v2"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169"},{"title":"MSRS: Adaptive Multi-Subspace Representation Steering for Attribute Alignment in Large Language Models","url":"https://arxiv.org/html/2508.10599"},{"title":"open-llm-leaderboard/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/95"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"HuggingFaceH4/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/95"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | OpenReview","url":"https://openreview.net/forum?id=NBHOdQJ1VE"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"[Literature Review] Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://www.themoonlight.io/en/review/adaptive-activation-steering-a-tuning-free-llm-truthfulness-improvement-method-for-diverse-hallucinations-categories"}]

Based on the search results, I found detailed information about ACT (Adaptive Activation Steering) and its TruthfulQA MC1 and MC2 scores:

## ACT Performance on TruthfulQA

ACT demonstrates significant improvements on TruthfulQA across different LLaMA model sizes. For LLaMA-7B, MC1 improved from 35.1% to 35.5% and MC2 from 50.7% to 52.3%. For LLaMA-13B, MC1 improved from 39.1% to 41.4% and MC2 from 55.1% to 59.1%. For LLaMA-33B, MC1 improved from 41.9% to 44.2% and MC2 from 58.6% to 62.3%. For LLaMA-65B, MC1 improved from 45.5% to 46.3% and MC2 from 62.9% to 64.7%.

## Method Overview

ACT is a tuning-free method designed to improve the truthfulness of large language models (LLMs). Experimental results demonstrate that ACT consistently improves truthfulness across 38 categories of hallucinations on the TruthfulQA benchmark.

## Real-world Applications

While ACT has achieved significant performance improvements on the TruthfulQA benchmark, its applicability in real-world chat settings involving multi-turn conversations has not been fully explored.

The research was published in February 2025, making these among the most recent results available for this method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee2ef85-b453-4cfc-83a9-2df42222315f",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "5f540bf7-8e69-44da-aac8-c2c26cdb1715",
  "sourceToolAssistantUUID": "2ee2ef85-b453-4cfc-83a9-2df42222315f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T05:57:34.282Z_

<details><summary>↩ Tool result · `toolu_01BxuejvBCQ1D5Phud5RRK5x`</summary>

```text
Web search results for query: "github steering-vectors library PyPI extract apply layer by layer"

Links: [{"title":"steering-vectors 0.12.1 documentation","url":"https://steering-vectors.github.io/steering-vectors/"},{"title":"steering-vectors · PyPI","url":"https://pypi.org/project/steering-vectors/"},{"title":"Basic usage - steering-vectors 0.12.1 documentation","url":"https://steering-vectors.github.io/steering-vectors/basic_usage.html"},{"title":"GitHub - steering-vectors/steering-vectors: Steering vectors for transformer language models in Pytorch / Huggingface · GitHub","url":"https://github.com/steering-vectors/steering-vectors"},{"title":"steering-vectors · GitHub","url":"https://github.com/steering-vectors"},{"title":"llm-steer 1.1.1 on PyPI - Libraries.io - security & maintenance data for open source software","url":"https://libraries.io/pypi/llm-steer"},{"title":"GitHub - bassrehab/steering-vectors-agents: Runtime control of LLM agent behaviors through activation steering vectors. More calibrated than prompting. · GitHub","url":"https://github.com/bassrehab/steering-vectors-agents"},{"title":"GitHub - Venn1998/steering-vectors-from-finetuning: Exploration of an alternative approach to extracting steering vectors. Instead of using the classical contrastive method we investigate whether comparing activations between a base model and its fine-tuned deceptive version reveals a more meaningful latent direction.","url":"https://github.com/Venn1998/steering-vectors-from-finetuning"},{"title":"GitHub - IBM/activation-steering: [ICLR 2025] General-purpose activation steering library · GitHub","url":"https://github.com/IBM/activation-steering"},{"title":"Dialz: A Python Toolkit for Steering Vectors Warning: This paper contains examples of language that may be considered offensive or distressing.","url":"https://arxiv.org/html/2505.06262v1"}]

Based on the search results, here's what I found about the steering-vectors library:

## Overview

The steering-vectors library provides utilities for training and applying steering vectors to language models (LMs) from Huggingface, like GPT, LLaMa, Gemma, Mistral, Pythia, and many more.

## Key Resources

- **GitHub Repository:** https://github.com/steering-vectors/steering-vectors
- **PyPI Package:** https://pypi.org/project/steering-vectors/
- **Documentation:** https://steering-vectors.github.io/steering-vectors/

## Extract and Apply by Layer

The library supports extracting and applying steering vectors layer-by-layer:

**Extracting by Layer:**
You can customize the layers to train by passing a list of layer numbers to the layers argument, and this also works with negative indices to count from the end of the model.

**Applying by Layer:**
You can apply steering vectors with different multipliers using a context manager, such as `steering_vec.apply(model, multiplier=0.5)` to apply the vector at half magnitude or with different magnitudes.

## How It Works

The library finds a steering vector by observing the hidden activations in a language model as it processes positive and negative statements and subtracts the "negative" activations from the "positive" activations, which can then be used to "steer" the model to be more or less sycophantic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cc033ca-d1dd-4827-adb2-c4b63cee6fae",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "f34de4df-2b36-4801-8b63-6c864b9beb44",
  "sourceToolAssistantUUID": "4cc033ca-d1dd-4827-adb2-c4b63cee6fae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T05:57:37.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EiSfdXHmTBcpuQZ3r1Mn43`</summary>

```json
{
  "query": "FactScore dataset github atomic claims biography generation hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34de4df-2b36-4801-8b63-6c864b9beb44",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jXFtg8VythVERVh7FS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "959ef6ee-e618-40e2-9fdc-aaf0194b19e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjyT1JgDf3ctiCrPqTUbM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 15597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2790,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 25 · 2026-05-16T05:57:38.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jpa6ttVfDUryGMTZFFgiVe`</summary>

```json
{
  "query": "activation steering computational cost inference overhead single GPU latent space"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "959ef6ee-e618-40e2-9fdc-aaf0194b19e6",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jXFtg8VythVERVh7FS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89a07e48-9b77-4026-b07a-93ac3b714860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjyT1JgDf3ctiCrPqTUbM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 15597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2790,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 26 · 2026-05-16T05:57:38.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xn3ZjGphQ2xUTLgH2gwrhT`</summary>

```json
{
  "query": "arxiv 2604.04743 \"hallucination basins\" code implementation results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a07e48-9b77-4026-b07a-93ac3b714860",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jXFtg8VythVERVh7FS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14ddfb00-6f4f-4734-a32b-8739b27c9679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjyT1JgDf3ctiCrPqTUbM8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2790,
      "cache_read_input_tokens": 15597,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 161,
          "cache_read_input_tokens": 15597,
          "cache_creation_input_tokens": 2790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2790,
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

_source line 27 · 2026-05-16T05:57:44.764Z_

<details><summary>↩ Tool result · `toolu_01EiSfdXHmTBcpuQZ3r1Mn43`</summary>

```text
Web search results for query: "FactScore dataset github atomic claims biography generation hallucination"

Links: [{"title":"FactScore: Factual Evaluation Framework","url":"https://www.emergentmind.com/topics/factscore-113e12f4-d246-433f-8289-063e105dc511"},{"title":"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Request PDF","url":"https://www.researchgate.net/publication/376394762_FActScore_Fine-grained_Atomic_Evaluation_of_Factual_Precision_in_Long_Form_Text_Generation?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"},{"title":"FACTSCORE: Fine-grained Atomic Evaluation of Factual ...","url":"https://martiansideofthemoon.github.io/assets/factscore.pdf"},{"title":"GitHub - shmsw25/FActScore: A package to evaluate factuality of long-form generation. Original implementation of our EMNLP 2023 paper \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation\" · GitHub","url":"https://github.com/shmsw25/FActScore"},{"title":"factuality · GitHub Topics","url":"https://github.com/topics/factuality"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Extrinsic Hallucinations in LLMs | Lil'Log","url":"https://lilianweng.github.io/posts/2024-07-07-hallucination/"},{"title":"Core: Robust Factual Precision Scoring with Informative Sub-Claim Identification","url":"https://arxiv.org/html/2407.03572v1"},{"title":"OpenFActScore: Open-Source Atomic Evaluation of Factuality in Text Generation","url":"https://arxiv.org/html/2507.05965v1"},{"title":"FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Research - AI at Meta","url":"https://ai.meta.com/research/publications/factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation/"}]

Based on the search results, here's what I found about the FactScore dataset:

## Overview

FactScore is a fine-grained factuality evaluation framework that decomposes texts into atomic claims and verifies each against trusted references, employing a decompose-then-verify pipeline using retrievers and validators to assess claim-level factual accuracy in long-form and structured data.

## Dataset and GitHub

The official GitHub repository contains a package to evaluate factuality of long-form generation, as the original implementation of the EMNLP 2023 paper "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation" at https://github.com/shmsw25/FActScore.

## Atomic Claims and Biography Generation

FactScore breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable knowledge source. The initial evaluation conducted human assessment of people biographies generated by several state-of-the-art commercial LMs—InstructGPT, ChatGPT, and the retrieval-augmented PerplexityAI—and reported that ChatGPT only achieved 58%.

## Hallucination Detection

Automated FactScore pipelines have been optimized for cost and scalability by coupling dense retrievers with LLM prompts for true/false entailment, reducing human labeling error to under 2% for biography generation. FactScore is used both as a metric and as a reward for hallucination detection frameworks and alignment/fine-tuning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "959ef6ee-e618-40e2-9fdc-aaf0194b19e6",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "d38f80c5-e4b1-4bcf-948a-7eb523b2638d",
  "sourceToolAssistantUUID": "959ef6ee-e618-40e2-9fdc-aaf0194b19e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T05:57:45.085Z_

<details><summary>↩ Tool result · `toolu_01Xn3ZjGphQ2xUTLgH2gwrhT`</summary>

```text
Web search results for query: "arxiv 2604.04743 "hallucination basins" code implementation results"

Links: [{"title":"[2604.04743] Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/abs/2604.04743"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Hallucination, Abstention, and Recursive Inseparability","url":"https://arxiv.org/html/2604.28067v1"},{"title":"Hallucination Inspector: A Fact-Checking Judge for API Migration","url":"https://arxiv.org/html/2604.20202"},{"title":"Hallucinations in Code Change to Natural Language Generation: Prevalence and Evaluation of Detection Metrics","url":"https://arxiv.org/html/2508.08661v1"},{"title":"[2604.17982] Mitigating Multimodal Hallucination via Phase-wise Self-reward","url":"https://arxiv.org/abs/2604.17982"},{"title":"Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code","url":"https://arxiv.org/html/2404.00971v3"},{"title":"A Systematic Literature Review of Code Hallucinations in","url":"https://arxiv.org/pdf/2511.00776"},{"title":"Mitigating Prompt-Induced Hallucinations in Large Language Models via Structured Reasoning","url":"https://arxiv.org/html/2601.02739v1"}]

Based on the search results, I found information about the paper arxiv 2604.04743 titled "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations."

## Paper Overview

The paper presents a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space.

## Key Findings and Results

Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, the researchers found that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap.

## Theoretical Contributions and Methods

The researchers formalize this behavior with task-complexity and multi-basin theorems, characterize basin emergence in L-layer transformers, and show that geometry-aware steering can reduce hallucination probability without retraining.

The search results point to the arxiv page and HTML version of the paper but don't contain detailed information about specific code implementations or their detailed results. To access the full code implementation details and comprehensive experimental results, you would need to view the complete paper directly on arxiv.org or check if the authors have published their code in a repository like GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14ddfb00-6f4f-4734-a32b-8739b27c9679",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "e6e44057-5aca-4fe0-afe1-6102fa10b99f",
  "sourceToolAssistantUUID": "14ddfb00-6f4f-4734-a32b-8739b27c9679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T05:57:45.891Z_

<details><summary>↩ Tool result · `toolu_01Jpa6ttVfDUryGMTZFFgiVe`</summary>

```text
Web search results for query: "activation steering computational cost inference overhead single GPU latent space"

Links: [{"title":"SpecOffload: Unlocking Latent GPU Capacity for LLM Inference on Resource-Constrained Devices","url":"https://arxiv.org/html/2505.10259v3"},{"title":"FairSteer: Inference Time Debiasing for LLMs with ...","url":"https://aclanthology.org/2025.findings-acl.589.pdf"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/10.1145/3764589"},{"title":"LIA: A Single-GPU LLM Inference Acceleration with Cooperative AMX-Enabled CPU-GPU Computation and CXL Offloading | Proceedings of the 52nd Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/10.1145/3695053.3731092"},{"title":"Mind the Memory Gap: Unveiling GPU Bottlenecks in Large-Batch LLM Inference","url":"https://arxiv.org/html/2503.08311v2"},{"title":"A Systematic Characterization of LLM Inference on GPUs","url":"https://arxiv.org/pdf/2512.01644"},{"title":"Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/"},{"title":"KVPR: Efficient LLM Inference with I/O-Aware KV Cache ...","url":"https://aclanthology.org/2025.findings-acl.997.pdf"},{"title":"Efficient CPU-GPU Collaborative Inference for MoE-based LLMs on Memory-Limited Systems","url":"https://arxiv.org/html/2512.16473v1"},{"title":"Faster inference from state space models via GPU computing - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1574954124000281"}]

I've performed a web search on activation steering computational cost inference overhead for single GPU latent space. Here are the key findings from the search results:

## Key Results:

The search returned several relevant papers on GPU inference optimization, though not all specifically focused on "activation steering." Here are the most relevant insights:

**GPU Inference Overhead and Latency:**

During the decoding phase, the average GPU core utilization of existing methods is only 13% at most, with GPU cores frequently remaining idle while awaiting parameter loading.

**Computational Cost and Memory Efficiency:**

Many studies have shown that LLMs exhibit a high degree of sparsity in both attention and MLP blocks, with proposals to exploit this sparsity to decrease computational complexity and memory usage by efficiently ignoring zero elements (non-activated neurons) during computation.

**Single GPU Performance Characteristics:**

In the decode phase, the LLM generates output tokens autoregressively one at a time, which is like a matrix-vector operation that underutilizes the GPU compute ability compared to the prefill phase, with the speed at which data is transferred to the GPU from memory dominating the latency.

**Inference Overhead on Resource-Constrained Systems:**

Previous research on MoE-based LLM inference has predominantly focused on GPU-based computations, which remains limited by model transfer time between CPU and GPU, with the advantage of CPU computation stemming from the interplay between computation and communication costs.

The results suggest that computational overhead in single GPU inference is primarily driven by memory bandwidth limitations and data transfer latency rather than raw computation speed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89a07e48-9b77-4026-b07a-93ac3b714860",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "7f202ac9-4664-4ae3-a1d3-beae2638b337",
  "sourceToolAssistantUUID": "89a07e48-9b77-4026-b07a-93ac3b714860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T05:57:51.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KtrymFspg7FfzvKwk44qu1`</summary>

```json
{
  "query": "github IBM activation-steering ICLR 2025 library features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f202ac9-4664-4ae3-a1d3-beae2638b337",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jY7bde9YPj4Rj9jRvs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "672f8ce9-a385-4e06-9f50-e52efa361c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RZJmqC65QqCBaktEHQUnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 794,
      "cache_creation_input_tokens": 3195,
      "cache_read_input_tokens": 18387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3195,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 31 · 2026-05-16T05:57:51.440Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2UW5dhspqRcDwUYg43n8U`</summary>

```json
{
  "query": "vllm-lens UKGovernmentBEIS steering vectors inference production"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672f8ce9-a385-4e06-9f50-e52efa361c34",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jY7bde9YPj4Rj9jRvs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d790fa35-126e-46c8-ab08-57e4b30d5836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RZJmqC65QqCBaktEHQUnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 794,
      "cache_creation_input_tokens": 3195,
      "cache_read_input_tokens": 18387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3195,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 32 · 2026-05-16T05:57:59.034Z_

<details><summary>↩ Tool result · `toolu_01R2UW5dhspqRcDwUYg43n8U`</summary>

```text
Web search results for query: "vllm-lens UKGovernmentBEIS steering vectors inference production"

Links: [{"title":"GitHub - UKGovernmentBEIS/vllm-lens: Extract residual-stream activations and apply steering vectors (including activation oracles) to any vLLM model during inference. · GitHub","url":"https://github.com/UKGovernmentBEIS/vllm-lens"},{"title":"vLLM-Lens: Fast Interpretability Tooling That Scales to ...","url":"https://www.lesswrong.com/posts/3bs27nZQuEcKhXf7q/vllm-lens-fast-interpretability-tooling-that-scales-to"},{"title":"Department of Business, Energy and Industrial Strategy · GitHub","url":"https://github.com/UKGovernmentBEIS"},{"title":"EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering","url":"https://arxiv.org/html/2509.25175v1"},{"title":"GitHub - UKGovernmentBEIS/vllm-control-arena · GitHub","url":"https://github.com/UKGovernmentBEIS/vllm-control-arena"},{"title":"Steering Vectors: Beamforming to LLM Control","url":"https://www.emergentmind.com/topics/steering-vectors"},{"title":"Using Vector Steering to Improve Model Guidance | Towards Data Science","url":"https://towardsdatascience.com/using-vector-steering-to-improve-model-guidance-9cca64635510/"},{"title":"GitHub - ZJU-REAL/EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering · GitHub","url":"https://github.com/ZJU-REAL/EasySteer"},{"title":"vLLM Production Deployment: Complete 2026 Guide | SitePoint","url":"https://www.sitepoint.com/vllm-production-deployment-guide-2026/"},{"title":"GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub","url":"https://github.com/vllm-project/vllm"}]

Based on the search results, here's what I found about vllm-lens, UKGovernmentBEIS steering vectors, and inference production:

## vLLM-Lens Overview

vLLM-Lens enables top-down interpretability (e.g., probes, steering, activation oracles) and offers high performance, supporting tensor parallelism & pipeline parallelism (across GPUs and nodes) out of the box. The tool is released under an MIT license by UKGovernmentBEIS on GitHub.

## Steering Vectors for Production

vLLM-Lens can extract residual-stream activations and apply steering vectors (including activation oracles) to any vLLM model during inference. To utilize the plugin, you can pass extra arguments such as output_residual_stream or apply_steering_vectors in the sampling parameters.

## Technical Architecture for Inference

vLLM-Lens registers as a vLLM plugin and injects itself into vLLM's processing pipeline in 3 locations, and you can pass extra args such as output_residual_stream or apply_steering_vectors in the sampling parameters.

vLLM dynamically batches tokens from multiple concurrent requests into a single forward pass, and vLLM-Lens applies steering to just the slices that correspond to the sample that requested it.

## Performance for Production Use

Other tools didn't support larger models, didn't support multi-node inference and/or were prohibitively slow to run, which motivated the creation of vLLM-Lens. You can apply all these techniques concurrently (in the same dynamic batch) - removing the need to switch between model instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d790fa35-126e-46c8-ab08-57e4b30d5836",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "55d1caa9-aba0-4b44-90c9-e04422804732",
  "sourceToolAssistantUUID": "d790fa35-126e-46c8-ab08-57e4b30d5836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T05:57:59.081Z_

<details><summary>↩ Tool result · `toolu_01KtrymFspg7FfzvKwk44qu1`</summary>

```text
Web search results for query: "github IBM activation-steering ICLR 2025 library features"

Links: [{"title":"GitHub - IBM/activation-steering: [ICLR 2025] General-purpose activation steering library · GitHub","url":"https://github.com/IBM/activation-steering"},{"title":"activation-steering/docs/quickstart.md at main · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/blob/main/docs/quickstart.md"},{"title":"Activity · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/activity"},{"title":"Releases · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/releases"},{"title":"activation-steering/docs/faq.md at main · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/blob/main/docs/faq.md"},{"title":"PROGRAMMING REFUSAL WITH CONDITIONAL ACTIVATION STEERING for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/programming-refusal-with-conditional-activation-steering--1"},{"title":"Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"},{"title":"Steering LLMs' Behavior with Concept Activation Vectors | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/steering-llms-behavior/"},{"title":"Paper Code 50+ ! Conditional Activation Steering Programming Refusal with","url":"https://iclr.cc/media/iclr-2025/Slides/29806.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf"}]

Based on the search results, here's what I found about the IBM activation-steering library for ICLR 2025:

## Overview

IBM's activation-steering is a general-purpose activation steering library presented at ICLR 2025.

## Key Features

The library provides tools for extracting steering vectors from contrastive examples and applying steering vectors to modify model behavior.

The library supports two main approaches:

1. **Basic Activation Steering**: Conceptually similar to Steering Language Models With Activation Engineering

2. **Conditional Activation Steering (CAST)**: This method analyzes LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context. It is based on the observation that different categories of prompts activate distinct patterns in the model's hidden states.

## Capabilities

Using CAST, one can systematically control LLM behavior with rules like "if input is about hate speech or adult content, then refuse" or "if input is not about legal advice, then refuse." This allows for selective modification of responses to specific content while maintaining normal responses to other content, all without requiring weight optimization.

## Model Compatibility

The activation steering code is designed to work with transformer-based models from the Hugging Face transformers library. It should work with most causal language models (e.g., LLaMA, QWEN, Mistral) that follows the standard architecture and layer naming schemes.

## Documentation and Resources

The library includes a Quick Start Tutorial (10 minutes to 60 minutes depending on hardware) for getting started with activation steering and conditional activation steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "672f8ce9-a385-4e06-9f50-e52efa361c34",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "add726fd536cd70e2",
  "type": "user",
  "uuid": "c7f76f41-cbe4-4f66-98c2-11b05565b037",
  "sourceToolAssistantUUID": "672f8ce9-a385-4e06-9f50-e52efa361c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T05:59:07.078Z_

Here is my comprehensive feasibility report for your research project on "latent trajectory steering for hallucination suppression":

---

## 1. Reference Implementations of Activation Steering (ITI, ACT, etc.)

**Several mature implementations exist:**

- **ITI (Inference-Time Intervention)** - [likenneth/honest_llama](https://github.com/likenneth/honest_llama): The original implementation from the Harvard group. Shifts model activations during inference across a limited number of attention heads. Has been replicated on Llama 2 and Llama 3 models. Uses alpha=15, heads=48 as default intervention params. Computationally cheap and data-efficient (only a few hundred examples needed to locate truthful directions).

- **ACT (Adaptive Activation Steering)** - [tianlwang/ACT](https://github.com/tianlwang/ACT): Published at ACM Web Conference 2025. A tuning-free method that adaptively selects steering directions across 38 categories of hallucinations. Key advantage over ITI: handles diverse hallucination types.

- **CAA (Contrastive Activation Addition)** - [nrimsky/CAA](https://github.com/nrimsky/CAA): Steering Llama 2 with contrastive activation addition. A clean, well-documented implementation.

- **IBM Activation Steering** - [IBM/activation-steering](https://github.com/IBM/activation-steering): ICLR 2025 spotlight paper implementing CAST (Conditional Activation Steering). General-purpose library supporting LLaMA, Qwen, Mistral. Key innovation: analyzes activation patterns to decide *whether* to steer, avoiding the "always-on" problem of vanilla steering.

---

## 2. Infrastructure for Layer-by-Layer Steering Vector Extraction

**Three main options, in order of maturity:**

- **steering-vectors** (PyPI: `steering-vectors`, v0.12.1) - [GitHub](https://github.com/steering-vectors/steering-vectors): A dedicated library for training and applying steering vectors to HuggingFace models (GPT, LLaMA, Gemma, Mistral, Pythia). Supports layer-specific extraction via a `layers` argument and per-layer application with configurable multipliers via context managers. This is probably your best starting point for rapid prototyping.

- **TransformerLens** - [GitHub](https://github.com/TransformerLensOrg/TransformerLens): 50+ open-source model support. Exposes all internal activations via hooking. You can cache, edit, remove, or replace activations at any layer. More general-purpose (mechanistic interpretability) but well-suited for custom steering experiments.

- **vLLM-Lens** - [GitHub](https://github.com/UKGovernmentBEIS/vllm-lens): Production-grade tool from UK BEIS. Extracts residual-stream activations and applies steering vectors to any vLLM model during inference. Supports tensor parallelism and pipeline parallelism across GPUs/nodes. MIT licensed. Key advantage: if you need to scale experiments to 70B models or want production-ready inference with steering, this handles dynamic batching with per-request steering.

---

## 3. TruthfulQA Baseline Numbers to Beat

**Current SOTA activation steering results on TruthfulQA:**

| Method | Model | MC1 | MC2 |
|--------|-------|-----|-----|
| ACT | LLaMA-7B | 35.5% | 52.3% |
| ACT | LLaMA-13B | 41.4% | 59.1% |
| ACT | LLaMA-33B | 44.2% | 62.3% |
| ACT | LLaMA-65B | 46.3% | 64.7% |

**More recent (2025-2026) methods claiming improvements over these baselines:**

- **ODESteer**: Claims +5.7% improvement over prior SOTA activation steering on TruthfulQA. Uses a unified ODE-based theoretical framework where identifying steering directions becomes a barrier function design problem from control theory.
- **Spherical Steering** (Feb 2026): Geometry-aware activation rotation that consistently improves TruthfulQA accuracy while also enhancing open-ended generation quality.
- **SADI (dynamic intervention)**: Up to +10.08 on True x Info metric.
- **CAST (IBM, ICLR 2025)**: Conditional steering -- no published MC1/MC2 absolute numbers in search results, but it was a spotlight paper.

Your baselines to beat: MC1 ~46% and MC2 ~65% on 65B-class models; MC1 ~44% and MC2 ~62% on 33B-class models.

---

## 4. Claim-Level Hallucination Evaluation Datasets

**Available benchmarks:**

- **FELM** (NeurIPS 2023 D&B track) - [GitHub](https://github.com/hkust-nlp/felm): Five domains, fine-grained claim-level annotations with predefined error types (knowledge error, reasoning error, irrelevant). Includes reference links supporting/contradicting each statement. Good for diverse hallucination categories.

- **FActScore** (EMNLP 2023) - [GitHub](https://github.com/shmsw25/FActScore): Decomposes text into atomic claims and verifies each against a knowledge source. Originally evaluated on biography generation. Pipeline: decompose-then-verify using retrievers + LLM validators. Automated pipelines achieve <2% labeling error vs. humans.

- **HalluLens** (Facebook Research, 2025) - [GitHub](https://github.com/facebookresearch/HalluLens): LLM textual hallucination benchmark from Meta.

- **TruthfulQA** - [GitHub](https://github.com/sylinrl/TruthfulQA): 817 questions across 38 categories. MC1 (single-answer) and MC2 (multi-answer) metrics. Standard benchmark for truthfulness interventions.

- **HalluScan** (2025): Systematic benchmark for detecting and mitigating hallucinations in instruction-following LLMs.

- **OpenFActScore** (2025): Open-source version of atomic factuality evaluation.

---

## 5. Computational Requirements

**Activation steering is cheap compared to fine-tuning.** Key findings:

- **Steering vector extraction**: Requires one forward pass per contrastive example pair through the model. For ITI, only a few hundred examples are needed. On a single A100 80GB, extracting vectors for a 7B model takes minutes; for 70B, you need 2x A100 80GB or use quantization (QLoRA reduces 70B to ~35GB footprint).

- **Inference with steering**: Near-zero overhead -- you're adding a vector to activations at selected layers. vLLM-Lens demonstrates this can be done in production batched inference without meaningful latency increase.

- **Hardware requirements by model size**:
  - 7B models: Single A100 40GB or RTX 4090 ($1.90-$3.50/hr cloud)
  - 13B-33B models: Single A100 80GB
  - 70B models: 2x A100 80GB or 1x H100 ($2.50/hr cloud); with 4-bit quantization, fits on single 80GB GPU
  - Full experiment sweep (multiple layers, multiple strengths, multiple seeds): Expect 10-50 GPU-hours for 7B, 50-200 GPU-hours for 70B depending on search space

- **IBM's CAST quickstart** estimates 10-60 minutes depending on hardware for a basic steering experiment.

---

## 6. Hallucination Basins Paper (April 2026)

**The paper exists and has code available:**

- **Paper**: "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations" ([arXiv:2604.04743](https://arxiv.org/abs/2604.04743)), submitted April 6, 2026 by K. Cherukuri and L. R. Varshney.

- **Code repository**: [github.com/akarlaraytu/trajectory-commitment](https://github.com/akarlaraytu/trajectory-commitment) -- all code, data, and figures are publicly available.

- **Key findings**: Formalizes hallucinations as arising from task-dependent basin structure in latent space. Finds that separability is strongly task-dependent (factoid settings show clearer basin separation; summarization and misconception-heavy settings show overlap). Provides task-complexity and multi-basin theorems, characterizes basin emergence in L-layer transformers, and demonstrates that geometry-aware steering can reduce hallucination probability without retraining.

- **Related paper**: "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation" ([arXiv:2604.15400](https://arxiv.org/html/2604.15400v1)) cites the basins paper, suggesting a growing subfield.

---

## Feasibility Assessment Summary

**This project is highly feasible.** The ecosystem is mature:

1. **Code infrastructure**: Multiple production-ready libraries (IBM activation-steering, steering-vectors PyPI package, vLLM-Lens) mean you don't need to build from scratch.
2. **Baselines are well-established**: ACT/ITI/CAST provide clear numbers on TruthfulQA to compare against, and the hallucination basins paper provides a direct theoretical predecessor.
3. **Datasets are available**: FELM, FActScore, TruthfulQA, and HalluLens cover both claim-level and QA evaluation.
4. **Compute is modest**: Steering experiments are inference-time only (no training), so a single A100 for 7B-13B or a small cluster for 70B is sufficient. Budget estimate: $200-$2000 in cloud compute for a thorough experimental sweep.
5. **The theoretical gap you'd be filling** -- connecting the basins/trajectory framework to practical latent trajectory steering -- has direct precursors in the April 2026 papers and available code.

---

Sources:
- [ITI / honest_llama](https://github.com/likenneth/honest_llama)
- [ACT - Adaptive Activation Steering](https://github.com/tianlwang/ACT)
- [CAA - Contrastive Activation Addition](https://github.com/nrimsky/CAA)
- [IBM activation-steering (ICLR 2025)](https://github.com/IBM/activation-steering)
- [steering-vectors PyPI library](https://github.com/steering-vectors/steering-vectors)
- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)
- [vLLM-Lens](https://github.com/UKGovernmentBEIS/vllm-lens)
- [FELM Benchmark](https://github.com/hkust-nlp/felm)
- [FActScore](https://github.com/shmsw25/FActScore)
- [HalluLens (Meta)](https://github.com/facebookresearch/HalluLens)
- [TruthfulQA](https://github.com/sylinrl/TruthfulQA)
- [Hallucination Basins paper (arXiv:2604.04743)](https://arxiv.org/abs/2604.04743)
- [Hallucination Basins code](https://github.com/akarlaraytu/trajectory-commitment)
- [ODESteer](https://openreview.net/forum?id=CFewUmgIIL)
- [Spherical Steering (Feb 2026)](https://arxiv.org/html/2602.08169)
- [ACT paper (ACM Web 2025)](https://dl.acm.org/doi/10.1145/3696410.3714640)
- [Activation Steering Field Guide 2026](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)
- [Awesome Activation Engineering](https://github.com/ZFancy/awesome-activation-engineering)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7f76f41-cbe4-4f66-98c2-11b05565b037",
  "isSidechain": true,
  "agentId": "add726fd536cd70e2",
  "requestId": "req_011Cb5jZ6Rxqf4EFDDJCCzh9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9bac83f-9835-4509-a5d0-ac23121e7558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4GhVPtYiw4ntxQ4sUofr4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 978,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 21582,
      "output_tokens": 3009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 978,
          "output_tokens": 3009,
          "cache_read_input_tokens": 21582,
          "cache_creation_input_tokens": 1838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1838,
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
