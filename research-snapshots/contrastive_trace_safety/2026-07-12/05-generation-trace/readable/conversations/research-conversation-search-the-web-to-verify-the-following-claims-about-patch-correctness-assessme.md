# Research conversation: Search the web to verify the following claims about patch correctness assessment (APCA) research: 1. ComPass (arXiv 2602

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2cd6c34985cbd664.jsonl`
- **Structured JSON:** [`a412a0966c241e1f517f.json`](../../sessions/a4/a412a0966c241e1f517f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-11T22:59:43.577Z_

Search the web to verify the following claims about patch correctness assessment (APCA) research:

1. ComPass (arXiv 2602.07561, Feb 2026) - claims 88.35% accuracy on Defects4J via contrastive learning on code representations. Search for this paper and verify its existence, results, and methodology.

2. APSG/Graph-LoRA (arXiv 2505.02629, May 2025) - claims 85.8-96.8% accuracy via attributed patch semantic graphs. Verify existence and results.

3. RePaCA (arXiv 2507.22580, 2025) - claims 83.1% accuracy using reasoning LLMs for APCA. Verify existence.

4. APPT - Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models (TSE 2024) - claims 79.7%. Verify.

5. Shibboleth (ISSTA 2022) - claims 88.7% dynamic APCA accuracy. Verify.

Use WebSearch for each. Report what you find - whether each paper exists, what accuracy they actually claim, and whether the SOTA landscape described is accurate. Also search for any OTHER recent APCA methods that might be missing from this list (search "automated patch correctness assessment 2025 2026").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "c146d585-bc5c-481b-81ff-d25850dd97d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T22:59:43.581Z_

```json
{
  "parentUuid": "c146d585-bc5c-481b-81ff-d25850dd97d2",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
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
  "uuid": "d1c3ffc2-6942-4668-98b4-e2cf07af90b0",
  "timestamp": "2026-05-11T22:59:43.581Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T22:59:49.143Z_



I'll search for each of these papers and verify the claims. Let me start by loading the WebSearch tool, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1c3ffc2-6942-4668-98b4-e2cf07af90b0",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRXTYTaYY9JauT7vtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "693b0764-232d-416c-acf9-4b067a729ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnMfQXhDBdf7pqEi6uaGS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9081,
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

_source line 4 · 2026-05-11T22:59:49.285Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JiMtrdwnmacFn5sAcuq4Ng`</summary>

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
  "parentUuid": "693b0764-232d-416c-acf9-4b067a729ede",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRXTYTaYY9JauT7vtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db299a62-00f3-4df0-940f-c3fbc76ba290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnMfQXhDBdf7pqEi6uaGS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9081,
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

### Tool result

_source line 5 · 2026-05-11T22:59:49.289Z_

<details><summary>↩ Tool result · `toolu_01JiMtrdwnmacFn5sAcuq4Ng`</summary>

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
  "parentUuid": "db299a62-00f3-4df0-940f-c3fbc76ba290",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "d7827d25-cc1d-4645-86ca-6e3793edb100",
  "sourceToolAssistantUUID": "db299a62-00f3-4df0-940f-c3fbc76ba290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T22:59:52.006Z_



Now let me search for each paper in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7827d25-cc1d-4645-86ca-6e3793edb100",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "880c4b8c-9a87-44a2-991b-9452f9794dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 7 · 2026-05-11T22:59:52.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U9WFVXVXY1rSXJyK7jysTi`</summary>

```json
{
  "query": "ComPass arXiv 2602.07561 contrastive learning patch correctness assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880c4b8c-9a87-44a2-991b-9452f9794dfa",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d19dbf2d-b2c2-4f0e-b2fb-f18bf141df38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 8 · 2026-05-11T22:59:52.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLhuw5ojtwgfNJYRqjXuMR`</summary>

```json
{
  "query": "arXiv 2505.02629 APSG Graph-LoRA attributed patch semantic graphs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d19dbf2d-b2c2-4f0e-b2fb-f18bf141df38",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d18aad5a-8b75-41c5-ac95-5f116656f191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 9 · 2026-05-11T22:59:53.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018rK7c677DcSLJJD6HvcMmx`</summary>

```json
{
  "query": "arXiv 2507.22580 RePaCA reasoning LLMs patch correctness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d18aad5a-8b75-41c5-ac95-5f116656f191",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6aaaa64-1534-42c6-96e7-b618a45801f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 10 · 2026-05-11T22:59:53.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M15hbWpArHyeUasireQMC3`</summary>

```json
{
  "query": "APPT boosting automated patch correctness prediction fine-tuning pre-trained models TSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6aaaa64-1534-42c6-96e7-b618a45801f5",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94312301-67ce-4e60-9b59-e42beb1f893b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 11 · 2026-05-11T22:59:54.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016weHAWAs1KJkWw1CvbaPvG`</summary>

```json
{
  "query": "Shibboleth ISSTA 2022 dynamic patch correctness assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94312301-67ce-4e60-9b59-e42beb1f893b",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcRxNzLhMYjnsDCpU1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63616a0d-4ead-493b-ae6c-f947ab5f0332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGz1MfGkgpFRPGZSruQ3DH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 12 · 2026-05-11T22:59:58.756Z_

<details><summary>↩ Tool result · `toolu_01U9WFVXVXY1rSXJyK7jysTi`</summary>

```text
Web search results for query: "ComPass arXiv 2602.07561 contrastive learning patch correctness assessment"

Links: [{"title":"[2602.07561] ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/abs/2602.07561"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"Contrastive Learning for Automated Patch Correctness ...","url":"https://arxiv.org/pdf/2602.07561"},{"title":"ReConPatch : Contrastive Patch Representation Learning for Industrial Anomaly Detection","url":"https://arxiv.org/html/2305.16713v3"},{"title":"Patch-Based Contrastive Learning and Memory Consolidation for Online Unsupervised Continual Learning","url":"https://arxiv.org/html/2409.16391v1"},{"title":"Patch-level Contrastive Learning via Positional Query for Visual Pre-training | OpenReview","url":"https://openreview.net/forum?id=Si9pBgOGeD"},{"title":"Weakly Supervised Contrastive Learning for Histopathology Patch Embeddings","url":"https://arxiv.org/html/2602.09477"},{"title":"[2409.16391] Patch-Based Contrastive Learning and Memory Consolidation for Online Unsupervised Continual Learning","url":"https://arxiv.org/abs/2409.16391"},{"title":"1 Deeply Unsupervised Patch Re-Identiﬁcation for Pre-training Object Detectors","url":"https://arxiv.org/pdf/2103.04814"},{"title":"Conducting patch contrastive learning with mixture of experts on mixed datasets for medical image segmentation | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-025-11234-1"}]

Based on the search results, I found the paper you're looking for:

## ComPass: Contrastive Learning for Automated Patch Correctness Assessment

ComPass is a PLM-based automated patch correctness assessment (APCA) approach that leverages contrastive learning and data augmentation to address challenges in automated program repair.

**Key Problem:**
APR is limited in generating overfitting patches, i.e., patches passing available test suites but incorrect. Patch overfitting has become a key concern in the APR community.

**Approach:**
ComPass utilizes code transformation rules to generate semantic-preserving code snippets for both unlabeled pre-training corpus and labeled fine-tuning patches, pre-trains PLMs with contrastive learning which captures code features with the same semantics but different structures, and finally integrates representation embeddings of patch code snippets and fine-tunes PLMs with a binary classifier jointly to assess patch code correctness.

**Results:**
Experimental results on 2274 real-world patches from Defects4J demonstrate that ComPass achieves an accuracy of 88.35%, significantly outperforming state-of-the-art baseline.

The paper was published on arXiv on February 7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d19dbf2d-b2c2-4f0e-b2fb-f18bf141df38",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "74654eb9-1972-49f2-99f8-54e6b11817ae",
  "sourceToolAssistantUUID": "d19dbf2d-b2c2-4f0e-b2fb-f18bf141df38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T22:59:59.314Z_

<details><summary>↩ Tool result · `toolu_01XLhuw5ojtwgfNJYRqjXuMR`</summary>

```text
Web search results for query: "arXiv 2505.02629 APSG Graph-LoRA attributed patch semantic graphs"

Links: [{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2505.02629"},{"title":"[2505.02629] Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2505.02629"},{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch ...","url":"https://arxiv.org/pdf/2505.02629"},{"title":"Semantic-guided LoRA Parameters Generation","url":"https://arxiv.org/html/2509.10535v1"},{"title":"Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks","url":"https://arxiv.org/html/2505.16901v1"},{"title":"Quantizing Text-attributed Graphs for Semantic-Structural Integration","url":"https://arxiv.org/html/2507.19526v1"},{"title":"Semantic Graph Consistency: Going Beyond Patches for Regularizing Self-Supervised Vision Transformers","url":"https://arxiv.org/html/2406.12944v1"},{"title":"[2504.12474] Integrating Structural and Semantic Signals in Text-Attributed Graphs with BiGTex","url":"https://arxiv.org/abs/2504.12474"},{"title":"Graph Machine Learning in the Era of Large Language Models (LLMs)","url":"https://arxiv.org/html/2404.14928v1"},{"title":"Semantic Scholar - Academic Graph API","url":"https://api.semanticscholar.org/api-docs/"}]

Based on the search results, I found detailed information about arXiv paper 2505.02629:

## Paper Overview

The paper is titled "Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment".

## Key Contributions

The paper introduces two main innovations:

1. **Attributed Patch Semantic Graph (APSG)**: APSG is a novel patch graph representation that adequately captures the patch semantic and explicitly reflects important patch attributes. More specifically, APSG is a directed graph which captures the patch semantic through data and control flow between program elements, and captures important attributes associated with the changed and related unchanged code by labeling different types of APSG nodes with different types of explicit attributes.

2. **Graph-LoRA**: Graph-LoRA is a new parameter-efficient fine-tuning (PEFT) method proposed on top of LoRA to retain graph information and fully train LLMs.

## Performance Results

Compared with the best static method LLM4PatchCorrect, the method improves the accuracy and F1 score by 3.1% to 7.5% and 3.0% to 7.1% respectively.

## Context

The paper addresses the problem of patch overfitting in automated program repair, where generated patches are not genuinely correct despite passing employed tests, and proposes using graph-based representations with LLMs for automated patch correctness assessment (APCA).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d18aad5a-8b75-41c5-ac95-5f116656f191",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "58b73a3c-803a-4a35-aaaf-7d80ddb67a49",
  "sourceToolAssistantUUID": "d18aad5a-8b75-41c5-ac95-5f116656f191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:00:00.651Z_

<details><summary>↩ Tool result · `toolu_01M15hbWpArHyeUasireQMC3`</summary>

```text
Web search results for query: "APPT boosting automated patch correctness prediction fine-tuning pre-trained models TSE 2024"

Links: [{"title":"[2301.12453] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://arxiv.org/abs/2301.12453"},{"title":"GitHub - iSEngLab/APPT: [TSE 2024] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models · GitHub","url":"https://github.com/iSEngLab/APPT"},{"title":"Actions · iSEngLab/APPT","url":"https://github.com/iSEngLab/APPT/actions"},{"title":"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10402095/;jsessionid=5922708BFC9F37FBEE6DF1C5986009E3"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"APPT: Boosting Automated Patch Correctness Prediction ...","url":"https://arxiv.org/pdf/2301.12453"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"Boosting Automated Patch Correctness Prediction via Pre- ...","url":"https://openreview.net/attachment?id=FzXGX0s8q7&name=pdf"},{"title":"(PDF) Boosting Automated Patch Correctness Prediction via Pre-trained Language Model","url":"https://www.researchgate.net/publication/367558621_Boosting_Automated_Patch_Correctness_Prediction_via_Pre-trained_Language_Model"},{"title":"APPT Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://www.scribd.com/document/874799956/APPT-Boosting-Automated-Patch-Correctness-Prediction-via-Fine-tuning-Pre-trained-Models"}]

I found the research paper you were searching for! Here's what the search revealed:

## APPT: Boosting Automated Patch Correctness Prediction

APPT is a TSE 2024 paper by Zhang, Quanjun and colleagues that focuses on boosting automated patch correctness prediction via fine-tuning pre-trained models.

### Overview

APPT is the first automated pre-trained model-based patch correctness assessment technique, which employs pre-training and fine-tuning to address limitations of prior work. The technique treats the source code as token sequences without extra overhead to design hand-crafted features.

### Technical Approach

APPT adopts a pre-trained model as the encoder stack, followed by an LSTM stack and a deep learning classifier. The pre-trained model is fine-tuned in conjunction with other components as a whole pipeline to fully adapt it specifically for reasoning about patch correctness.

### Performance Results

APPT achieves prediction accuracy of 79.7% and recall of 83.2%, outperforming CACHE by 4.3% and 6.7%. The fine-tuning process and the LSTM stack increase F1-score by 10.22% and 4.11%, respectively.

The research includes both open-source code available on GitHub (iSEngLab/APPT) and publication through IEEE Xplore for the TSE 2024 venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94312301-67ce-4e60-9b59-e42beb1f893b",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "99d32e66-e374-4f71-a2c1-952c10e5e5bd",
  "sourceToolAssistantUUID": "94312301-67ce-4e60-9b59-e42beb1f893b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:00:00.661Z_

<details><summary>↩ Tool result · `toolu_018rK7c677DcSLJJD6HvcMmx`</summary>

```text
Web search results for query: "arXiv 2507.22580 RePaCA reasoning LLMs patch correctness"

Links: [{"title":"[2507.22580] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580"},{"title":"[2507.22580v1] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580v1"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"Enhancing Mathematical Reasoning in LLMs by Stepwise Correction","url":"https://arxiv.org/html/2410.12934v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"Probabilistic Soundness Guarantees in LLM Reasoning Chains","url":"https://arxiv.org/html/2507.12948v1"},{"title":"GitHub - Xuchen-Li/llm-arxiv-daily: Automatically update arXiv papers about LLM Reasoning, LLM Evaluation, LLM & MLLM and Video Understanding using Github Actions. · GitHub","url":"https://github.com/Xuchen-Li/llm-arxiv-daily"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://arxiv.org/html/2502.12289v3"},{"title":"Trustworthy Reasoning: Evaluating and Enhancing Factual Accuracy in LLM Intermediate Thought Processes","url":"https://arxiv.org/html/2507.22940v1"},{"title":"The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination | OpenReview","url":"https://openreview.net/forum?id=vHKUXkrpVs"}]

Based on the search results, here's information about arXiv paper 2507.22580:

## RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment

RePaCA is a novel static Automated Patch Correctness Assessment (APCA) technique that leverages Large Language Models (LLMs) specialized in thinking tasks. The model is prompted with buggy and fixed code snippets and guided to generate a Chain of Thought that analyzes code differences, reasons about how the patch addresses the root cause, and ultimately provides a binary classification: correct or overfitting.

### Problem Being Addressed

Automated Program Repair (APR) seeks to automatically correct software bugs without requiring human intervention. However, existing tools tend to generate patches that satisfy test cases without fixing the underlying bug, known as overfitting patches. To address this issue, Automated Patch Correctness Assessment (APCA) attempts to identify overfitting patches generated by APR tools.

### Key Technical Approach

To enhance reasoning capabilities for the APCA task specifically, the LLM is finetuned using Reinforcement Learning with the Group Relative Policy Optimization algorithm.

### Performance Results

When evaluated on a standard Defects4J-derived test, the approach achieves state-of-the-art performance, with 83.1% accuracy and an 84.8% F1-score. Furthermore, the model demonstrates superior generalization capabilities when trained on different datasets, outperforming the leading technique.

The reasoning capability provides enhanced explainability for the patch assessment, underscoring the considerable promise of finetuned, reasoning LLMs to advance static APCA by enhancing accuracy, generalization, and explainability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6aaaa64-1534-42c6-96e7-b618a45801f5",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "14a66640-2416-454d-b758-59966573ac5c",
  "sourceToolAssistantUUID": "f6aaaa64-1534-42c6-96e7-b618a45801f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:00:01.745Z_

<details><summary>↩ Tool result · `toolu_016weHAWAs1KJkWw1CvbaPvG`</summary>

```text
Web search results for query: "Shibboleth ISSTA 2022 dynamic patch correctness assessment"

Links: [{"title":"Patch Correctness Assessment in Automated Program Repair Based on the Impact of Patches on Production and Test Code (ISSTA 2022 - Technical Papers) - ISSTA 2022","url":"https://conf.researchr.org/details/issta-2022/issta-2022-technical-papers/5/Patch-Correctness-Assessment-in-Automated-Program-Repair-Based-on-the-Impact-of-Patch"},{"title":"Patch Correctness Assessment in Automated Program Repair","url":"https://ali-ghanbari.github.io/publications/issta22-shibboleth.pdf"},{"title":"GitHub - ali-ghanbari/shibboleth: Patch Correctness Assessment in Automated Program Repair Based on the Impact of Patches on Production and Test Codes · GitHub","url":"https://github.com/ali-ghanbari/shibboleth"},{"title":"Patch Correctness Assessment in Automated Program Repair ...","url":"https://dl.acm.org/doi/pdf/10.1145/3533767.3534368"},{"title":"Shibboleth: Hybrid Patch Correctness Assessment in ...","url":"https://ali-ghanbari.github.io/publications/ase-22-demo.pdf"},{"title":"Patch correctness assessment in automated program repair based on the impact of patches on production and test code | Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis","url":"https://dl.acm.org/doi/10.1145/3533767.3534368"},{"title":"Patch Correctness Assessment: A Survey | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/abs/10.1145/3702972"},{"title":"Assessing Patch Correctness in Test-based Automated Program Repair Jared Wang","url":"https://www.conferenceharvester.com/uploads/harvester/presentations/BEOMCBDO/BEOMCBDO-PDF-0-2320823-1-PDF(6).pdf"},{"title":"[PDF] Automated Patch Correctness Assessment: How Far are We? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automated-Patch-Correctness-Assessment:-How-Far-are-Wang-Wen/45d3ca14f3445075eed6e32b1207bb914514a39a"},{"title":"Improving Patch Correctness Analysis via Random Testing ...","url":"https://facumolina.github.io/files/MOLINA_ETAL_ICST2024.pdf"}]

I found relevant results for your search. Here's what I found:

## Shibboleth ISSTA 2022 Paper

Shibboleth is a novel technique for automatic correctness assessment of patches generated by test-based generate-and-validate APR systems, presented at ISSTA 2022 by Ali Ghanbari and Andrian Marcus.

### Overview

Test-based generate-and-validate automated program repair (APR) systems often generate many patches that pass the test suite without fixing the bug, and these generated patches must be manually inspected by the developers.

### Technical Approach

The impact of patches is captured along three complementary facets - the technique measures the impact of patches on both production code (via syntactic and semantic similarity) and test code (via code coverage of passing tests) to separate patches that result in similar programs and that do not delete desired program elements.

### Evaluation Results

In 43% (66%) of cases, Shibboleth ranks the correct patch in top-1 (top-2) positions, and in classification mode it achieves an accuracy and F1-score of 0.887 and 0.852, respectively.

The technique was evaluated on 1,871 patches generated by 29 Java-based APR systems for Defects4J programs and outperforms state-of-the-art ranking and classification techniques.

### Availability

Shibboleth is implemented as a one-click Maven-plugin, as well as a command-line tool, and is publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63616a0d-4ead-493b-ae6c-f947ab5f0332",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "327860e1-07ab-4a6c-aa5c-c044dcf9fb57",
  "sourceToolAssistantUUID": "63616a0d-4ead-493b-ae6c-f947ab5f0332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-11T23:00:04.440Z_

Good, all five papers found. Now let me search for the broader APCA landscape and any missing recent methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "327860e1-07ab-4a6c-aa5c-c044dcf9fb57",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcSs9Vdt4stjzT51tSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c868e51d-9c31-43dc-a0cd-890870a160ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dN3C9GsMmaBuMwjWiEX9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 10503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4983,
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

_source line 18 · 2026-05-11T23:00:04.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JpcURsAH6aQp1Eqc9Lns2u`</summary>

```json
{
  "query": "automated patch correctness assessment 2025 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c868e51d-9c31-43dc-a0cd-890870a160ca",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcSs9Vdt4stjzT51tSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cad7fd6f-50b9-426a-a433-7c2ac6296c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dN3C9GsMmaBuMwjWiEX9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 10503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4983,
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

_source line 19 · 2026-05-11T23:00:05.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YUTbXjbno8UsiwzJqu51Vt`</summary>

```json
{
  "query": "LLM4PatchCorrect automated patch correctness LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad7fd6f-50b9-426a-a433-7c2ac6296c59",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcSs9Vdt4stjzT51tSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fadb1339-4cee-45db-a772-19474786ba3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dN3C9GsMmaBuMwjWiEX9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 10503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4983,
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

_source line 20 · 2026-05-11T23:00:06.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgiScq3E5MLMhDVwgMDs6T`</summary>

```json
{
  "query": "APSG Graph-LoRA 2505.02629 accuracy percentage Defects4J results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fadb1339-4cee-45db-a772-19474786ba3e",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcSs9Vdt4stjzT51tSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50b8850d-475c-4d85-86a1-ea383ea7237d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dN3C9GsMmaBuMwjWiEX9A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 10503,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 10503,
          "cache_creation_input_tokens": 4983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4983,
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

_source line 21 · 2026-05-11T23:00:12.402Z_

<details><summary>↩ Tool result · `toolu_01FgiScq3E5MLMhDVwgMDs6T`</summary>

```text
Web search results for query: "APSG Graph-LoRA 2505.02629 accuracy percentage Defects4J results"

Links: [{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2505.02629v1"},{"title":"[2505.02629] Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2505.02629"},{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch ...","url":"https://arxiv.org/pdf/2505.02629"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models","url":"https://arxiv.org/html/2505.02931"},{"title":"An Anatomy of 488 Faults from Defects4J Based on the Control- and Data-Flow Graph Representations of Programs","url":"https://arxiv.org/html/2502.02299v2"},{"title":"[2502.02629] Graph Structure Learning for Tumor Microenvironment with Cell Type Annotation from non-spatial scRNA-seq data","url":"https://arxiv.org/abs/2502.02629"},{"title":"[2502.02299] An Anatomy of 488 Faults from Defects4J Based on the Control- and Data-Flow Graph Representations of Programs","url":"https://arxiv.org/abs/2502.02299"},{"title":"Automatic Repair of Real Bugs in Java: A Large-Scale Experiment on the Defects4J Dataset - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181102429M/abstract"},{"title":"Mark Needham, Developer Relations at Neo4j Graph Based AI","url":"https://apsg.bcs.org/materials/presentations/20190214.pdf"}]

Based on the search results, I found information about the APSG Graph-LoRA paper (arxiv 2505.02629). Here's what the paper reports:

The method improves accuracy and F1 score by 2.3% to 6.6% and 1.8% to 6.1% respectively compared to state-of-the-art methods. However, the search results don't provide the specific absolute accuracy percentage on Defects4J for the APSG Graph-LoRA method itself.

The paper uses multiple datasets including the Wang dataset, Lin dataset, and Merge dataset for evaluating automated patch correctness assessment (APCA), but the specific accuracy percentages for the Defects4J results are not shown in the available search result content.

To get the exact accuracy percentages on Defects4J, you would need to access the full paper directly at https://arxiv.org/html/2505.02629v1 or https://arxiv.org/pdf/2505.02629, where the detailed results tables should be included.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b8850d-475c-4d85-86a1-ea383ea7237d",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "db958253-7522-41d1-aebb-76f16d269dd6",
  "sourceToolAssistantUUID": "50b8850d-475c-4d85-86a1-ea383ea7237d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:00:12.654Z_

<details><summary>↩ Tool result · `toolu_01JpcURsAH6aQp1Eqc9Lns2u`</summary>

```text
Web search results for query: "automated patch correctness assessment 2025 2026 state of the art"

Links: [{"title":"Automated patch correctness assessment | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416590"},{"title":"Automated Patch Correctness Assessment: How Far are We? | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9286063"},{"title":"Patch correctness assessment in automated program repair based on the impact of patches on production and test code | Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis","url":"https://dl.acm.org/doi/10.1145/3533767.3534368"},{"title":"[2507.22580v1] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580v1"},{"title":"Automated patch assessment for program repair at scale | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-020-09920-w"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10066209/"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"[2507.22580] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580"},{"title":"[PDF] Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Invalidator:-Automated-Patch-Correctness-Assessment-Le-Cong-Luong/f6beeaf7ca72e4ef32a8a8110d4c7e30b18b0231"},{"title":"[2303.00202] PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://arxiv.org/abs/2303.00202"}]

Based on the search results, here's an overview of the current state of the art in automated patch correctness assessment for 2025-2026:

## Core Challenge

The overfitting problem remains a major challenge in automated program repair, where generated patches pass test cases but don't actually fix the underlying bug.

## Recent State-of-the-Art Approaches

### LLM-Based Static Assessment (2025)

RePaCA introduces a novel static APCA technique leveraging Large Language Models specialized in thinking tasks, using Chain of Thought reasoning to analyze code differences and reason about how patches address root causes, with the LLM finetuned using Reinforcement Learning and Group Relative Policy Optimization. This approach achieves state-of-the-art performance with 83.1% accuracy and 84.8% F1-score on standard Defects4J-derived tests.

### Multi-Faceted Assessment

Recent techniques measure the impact of patches on both production code via syntactic and semantic similarity, and test code via code coverage of passing tests.

### Semantic and Syntactic Reasoning

Invalidator assesses patch correctness via semantic and syntactic reasoning, leveraging program invariants to reason about program semantics while capturing program syntax through language semantics learned from large code corpuses using pre-trained language models.

## Zero-Shot and Cross-Tool Generalization

Recent approaches achieve approximately 84.4% accuracy and 86.5% F1-score without requiring labeled patches from new or unseen APR tools, reducing the manual labeling burden when evaluating newly developed repair tools.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad7fd6f-50b9-426a-a433-7c2ac6296c59",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "75e7f607-bad9-4cc0-b35a-15a14f64dae8",
  "sourceToolAssistantUUID": "cad7fd6f-50b9-426a-a433-7c2ac6296c59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T23:00:14.888Z_

<details><summary>↩ Tool result · `toolu_01YUTbXjbno8UsiwzJqu51Vt`</summary>

```text
Web search results for query: "LLM4PatchCorrect automated patch correctness LLM 2024 2025"

Links: [{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2024.3452252"},{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2505.02629"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Leveraging Large Language Model for Automatic Patch Correctness Assessment | Request PDF","url":"https://www.researchgate.net/publication/383591189_Leveraging_Large_Language_Model_for_Automatic_Patch_Correctness_Assessment"},{"title":"[PDF] Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f6beeaf7ca72e4ef32a8a8110d4c7e30b18b0231"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"SoK: Towards Effective Automated Vulnerability Repair","url":"https://www.usenix.org/system/files/usenixsecurity25-li-ying.pdf"},{"title":"A Large-Scale Empirical Review of Patch Correctness Checking Approaches | Request PDF","url":"https://www.researchgate.net/publication/376087277_A_Large-Scale_Empirical_Review_of_Patch_Correctness_Checking_Approaches"},{"title":"[PDF] Is this Change the Answer to that Problem?: Correlating Descriptions of Bug and Code Changes for Evaluating Patch Correctness | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-this-Change-the-Answer-to-that-Problem:-of-Bug-Tian-Tang/bd7d7f7d79df4c628494ee4d6ce19cd7dbebb367"}]

Based on the web search results, here's what I found about **LLM4PatchCorrect**:

## Overview

LLM4PatchCorrect is proposed to utilize labeled patches of existing APR tools to predict the correctness of the patches generated by a new/unseen APR tool.

## Key Features

LLM4PatchCorrect employs an open-source large language model (LLM) for code, called Starcoder-7B, to evaluate patch correctness, without requiring fine-tuning. 

To provide knowledge regarding the automatic patch correctness assessment (APCA) task to the large language model for code, LLM4PatchCorrect leverages bug descriptions, execution traces, failing test cases, test coverage, and labeled patches generated by existing APR tools, before deciding the correctness of the unlabeled patches of a new or unseen APR tool.

## Performance Results

LLM4PatchCorrect can achieve an accuracy of 84.4% and an F1-score of 86.5% on average although no labeled patch of the new or unseen APR tool is available. The experimental results demonstrate that LLM4PatchCorrect significantly improves Accuracy, F1, and AUC scores, increasing them from 10.2% to 32.4%, 6.1% to 24.1%, and 10.1% to 33.2%, on average, respectively, compared to state-of-the-art APCA approaches.

## Recent Developments

The approach has been published and continues to be referenced in recent work. Compared with the LLM4PatchCorrect method (the most advanced LLM-based method), a newer method achieves 3.4%, 3.5%, 2.5%, and 3.0% higher in accuracy, precision, recall, and F1 score respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fadb1339-4cee-45db-a772-19474786ba3e",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "6e578fef-ac5a-4ad4-a24c-b169b04ccf0c",
  "sourceToolAssistantUUID": "fadb1339-4cee-45db-a772-19474786ba3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-11T23:00:17.452Z_

Let me get more specific accuracy numbers for the APSG/Graph-LoRA paper and search for any other recent APCA methods I might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e578fef-ac5a-4ad4-a24c-b169b04ccf0c",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcTqPbwPk1Ko9rce7MQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6325243-e921-494b-801e-30047630a07d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZrbb9fHqQGZQx1TxCmiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 15486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2326,
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

_source line 25 · 2026-05-11T23:00:18.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRi5YKbRBtgMoCfGvnSYL1`</summary>

```json
{
  "query": "\"Graph-LoRA\" \"APSG\" patch correctness accuracy 85 96 results dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6325243-e921-494b-801e-30047630a07d",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcTqPbwPk1Ko9rce7MQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "531f718d-b2bc-4036-8699-37794628acb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZrbb9fHqQGZQx1TxCmiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 15486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2326,
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

_source line 26 · 2026-05-11T23:00:18.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nrh72gb7fHmkLGqVyp7yvC`</summary>

```json
{
  "query": "PatchZero CACHE Invalidator patch correctness assessment accuracy 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "531f718d-b2bc-4036-8699-37794628acb6",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcTqPbwPk1Ko9rce7MQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4df5f21f-04b3-435c-9210-f2e8900304dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZrbb9fHqQGZQx1TxCmiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 15486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2326,
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

_source line 27 · 2026-05-11T23:00:19.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATyqBqdEmy87WmaJ1e6yZF`</summary>

```json
{
  "query": "automated patch correctness assessment survey 2025 new methods techniques"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df5f21f-04b3-435c-9210-f2e8900304dd",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcTqPbwPk1Ko9rce7MQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dc7bc56-2782-45af-ba28-c97b5e9d3573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABZrbb9fHqQGZQx1TxCmiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 15486,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 822,
          "output_tokens": 210,
          "cache_read_input_tokens": 15486,
          "cache_creation_input_tokens": 2326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2326,
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

_source line 28 · 2026-05-11T23:00:25.226Z_

<details><summary>↩ Tool result · `toolu_01YRi5YKbRBtgMoCfGvnSYL1`</summary>

```text
Web search results for query: ""Graph-LoRA" "APSG" patch correctness accuracy 85 96 results dataset"

Links: [{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2505.02629"},{"title":"[2505.02629] Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2505.02629"},{"title":"LoFT: LoRA-Fused Training Dataset Generation with Few-shot Guidance","url":"https://arxiv.org/html/2505.11703v1"},{"title":"MoSalama98/LoRA-WiSE · Datasets at Hugging Face","url":"https://huggingface.co/datasets/MoSalama98/LoRA-WiSE"},{"title":"Evaluating LoRA Fine-Tuning Results | Niklas Heidloff","url":"https://heidloff.net/article/evaluating-lora-fine-tuning-results/"},{"title":"A Large-Scale Empirical Review of Patch Correctness Checking Approaches | Request PDF","url":"https://www.researchgate.net/publication/376087277_A_Large-Scale_Empirical_Review_of_Patch_Correctness_Checking_Approaches"},{"title":"Patch Correctness Assessment: A Survey | Request PDF","url":"https://www.researchgate.net/publication/385670765_Patch_Correctness_Assessment_A_Survey"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"LoRA Without Regret - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/lora/"},{"title":"LoRA: A Logical Reasoning Augmented Dataset for Visual Question Answering | OpenReview","url":"https://openreview.net/forum?id=bW1uwPV3im"}]

The search results found relevant research on Graph-LoRA and APSG. Graph-LoRA is a parameter-efficient fine-tuning method proposed on top of LoRA to retain graph information and fully train language models. 

APSG (Attributed Patch Semantic Graph) is a directed graph which captures patch semantics through data and control flow between program elements, while labeling different types of nodes with explicit attributes.

Regarding the accuracy metrics mentioned in your query: Compared with the best static method LLM4PatchCorrect, the Graph-LoRA method improves accuracy and F1 score by 3.1% to 7.5% and 3.0% to 7.1% respectively.

The results of ablation studies show that both APSG and Graph-LoRA play a significant role in fine-tuning LLM on the patch correctness assessment (APCA) task.

The research appears to focus on automated patch correctness assessment, where these methods are applied to evaluate whether automatically generated software patches are correct.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "531f718d-b2bc-4036-8699-37794628acb6",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "6eebb1ea-51a8-4a8e-84b6-ce97a50a5965",
  "sourceToolAssistantUUID": "531f718d-b2bc-4036-8699-37794628acb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-11T23:00:27.587Z_

<details><summary>↩ Tool result · `toolu_01ATyqBqdEmy87WmaJ1e6yZF`</summary>

```text
Web search results for query: "automated patch correctness assessment survey 2025 new methods techniques"

Links: [{"title":"Automated patch correctness assessment | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416590"},{"title":"Automated Patch Correctness Assessment: How Far are We? | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9286063"},{"title":"Patch Correctness Assessment: A Survey | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3702972"},{"title":"Automated patch assessment for program repair at scale | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-020-09920-w"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10066209/"},{"title":"[2505.02629] Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2505.02629"},{"title":"Automated patch correctness predicting to fix software defect - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417424017445"},{"title":"Patch Correctness Assessment: A Survey - R Discovery","url":"https://discovery.researcher.life/article/patch-correctness-assessment-a-survey/9b4c4224522333148629cc7ec062e349"},{"title":"Patch Correctness Assessment: A Survey | Request PDF","url":"https://www.researchgate.net/publication/385670765_Patch_Correctness_Assessment_A_Survey"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"}]

Based on the search results, here's what I found about automated patch correctness assessment and the latest methods and techniques in 2025:

## Overview

Overfitting is a longstanding problem in automated program repair, where patches that pass tests require further validation to determine their correctness. Researchers have proposed many methods to automatically assess the correctness of patches, but no systematic review provides a detailed introduction to this problem, the existing solutions, and the challenges.

## Recent Survey and Approaches

A systematic review of existing approaches to patch correctness assessment proposes a comprehensive categorization of publicly available techniques and datasets, examines the commonly used evaluation metrics, and performs an in-depth analysis of the effectiveness of the existing models in addressing the challenge of overfitting.

## 2025 New Techniques and Methods

Several emerging approaches in 2025 include:

1. **Large Language Model-based Assessment**: With the emergence of large language model (LLM) technology, researchers have employed LLM to assess the patch correctness and have obtained the state-of-the-art performance.

2. **Semantic Graph Approaches**: The literature on APCA has demonstrated the importance of capturing patch semantic and explicitly considering certain code attributes in predicting patch correctness.

3. **Semantic and Syntactic Reasoning**: The Invalidator technique automatically assesses the correctness of APR-generated patches via semantic and syntactic reasoning, leveraging program invariants to reason about program semantics while also capturing program syntax through language semantics learned from a large code corpus using a pre-trained language model.

## Traditional Classification of Methods

Static-based APCA relies on static code features, while dynamic-based APCA necessitates runtime information obtained by executing test cases on fixed or patched programs, with a growing trend of employing learning-based APCA techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dc7bc56-2782-45af-ba28-c97b5e9d3573",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "745abc99-3c62-4c07-b531-e8a778ee7235",
  "sourceToolAssistantUUID": "7dc7bc56-2782-45af-ba28-c97b5e9d3573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-11T23:00:27.619Z_

<details><summary>↩ Tool result · `toolu_01Nrh72gb7fHmkLGqVyp7yvC`</summary>

```text
Web search results for query: "PatchZero CACHE Invalidator patch correctness assessment accuracy 2023 2024"

Links: [{"title":"[2303.00202] PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://arxiv.org/abs/2303.00202"},{"title":"(PDF) PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://www.researchgate.net/publication/368923526_PatchZero_Zero-Shot_Automatic_Patch_Correctness_Assessment"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2023.3255177"},{"title":"PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://www.emergentmind.com/papers/2303.00202"},{"title":"GitHub - thanhlecongg/Invalidator: Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning (IEEE TSE) · GitHub","url":"https://github.com/thanhlecongg/Invalidator"},{"title":"[2303.00202v2] PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://arxiv.org/abs/2303.00202v2"},{"title":"[PDF] Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Invalidator:-Automated-Patch-Correctness-Assessment-Le-Cong-Luong/f6beeaf7ca72e4ef32a8a8110d4c7e30b18b0231"},{"title":"JOURNAL OF LATEX CLASS FILES, VOL. XX, NO. X, XX XXXX 1","url":"https://arxiv.org/pdf/2303.00202v2"},{"title":"[2301.01113] Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning","url":"https://arxiv.org/abs/2301.01113"},{"title":"Invalidator: Automated Patch Correctness Assessment Via Semantic and Syntactic Reasoning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10066209/"}]

I found relevant information about PatchZero and related patch correctness assessment techniques. Here are the key findings:

## PatchZero Overview

PatchZero proposes patch correctness assessment by adopting large pre-trained models. APR techniques face an overfitting problem where a generated patch can be incorrect although it passes all tests.

## Accuracy and Performance

PatchZero can achieve an accuracy of 82.7% and an F1-score of 86.0% on average although no labeled patch of the new or unseen APR tool is available. The proposed technique outperformed the prior state-of-the-art by a large margin.

## Comparison with CACHE and Invalidator

The search results mention that PatchZero is compared against other approaches. Invalidator took five hours to infer dynamic features and seven minutes (on average) to assess the correctness for a single patch. 

Invalidator is a novel technique to automatically assess the correctness of APR-generated patches via semantic and syntactic reasoning, which outperforms existing methods in terms of Accuracy and F-measure.

## Timeline

The PatchZero paper was submitted on March 1, 2023, with the latest version released on March 22, 2024. Invalidator was published in IEEE Transactions on Software Engineering in 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4df5f21f-04b3-435c-9210-f2e8900304dd",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "1ff0ca28-8dd5-4359-86d0-38f9039583a9",
  "sourceToolAssistantUUID": "4df5f21f-04b3-435c-9210-f2e8900304dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-11T23:00:31.901Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EnYD9WoD4ex3bF42fXPK7v`</summary>

```json
{
  "query": "patch correctness assessment APCA 2026 new approach deep learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff0ca28-8dd5-4359-86d0-38f9039583a9",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcUmmr5QEhTWpnP4L8Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a74b53b-11f3-4a1d-b8d4-c9732d5ef900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhSto5b5aVHmfpd2FeF8r3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 985,
      "cache_creation_input_tokens": 2789,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2789,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T23:00:32.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5nvvnP6JeXWyAGJ8DLV3o`</summary>

```json
{
  "query": "site:arxiv.org \"patch correctness\" 2025 2026 assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a74b53b-11f3-4a1d-b8d4-c9732d5ef900",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcUmmr5QEhTWpnP4L8Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae5d5d3c-fd6f-4ee6-9d41-dc0559f5b912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhSto5b5aVHmfpd2FeF8r3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 985,
      "cache_creation_input_tokens": 2789,
      "cache_read_input_tokens": 17812,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 985,
          "output_tokens": 119,
          "cache_read_input_tokens": 17812,
          "cache_creation_input_tokens": 2789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2789,
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

_source line 33 · 2026-05-11T23:00:39.425Z_

<details><summary>↩ Tool result · `toolu_01EnYD9WoD4ex3bF42fXPK7v`</summary>

```text
Web search results for query: "patch correctness assessment APCA 2026 new approach deep learning"

Links: [{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"On the Effectiveness of Code Representation in Deep Learning-Based Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2603.07520v1"},{"title":"[2602.07561] ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/abs/2602.07561"},{"title":"Enhancing Automated Patch Correctness | PDF | Deep Learning | Machine Learning","url":"https://www.scribd.com/document/874799956/APPT-Boosting-Automated-Patch-Correctness-Prediction-via-Fine-tuning-Pre-trained-Models"},{"title":"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2505.02629"},{"title":"Automated patch correctness predicting to fix software defect - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417424017445"},{"title":"Context-Aware Code Change Embedding for Better Patch Correctness Assessment | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3505247"},{"title":"Patch Correctness Assessment: A Survey | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3702972"},{"title":"Automated Patch Correctness Assessment: How Far are We? | Request PDF","url":"https://www.researchgate.net/publication/343988938_Automated_Patch_Correctness_Assessment_How_Far_are_We"}]

Based on the search results, I found several recent research papers on patch correctness assessment using deep learning approaches. Here are the key findings:

## Recent Approaches (2026)

ComPass is a novel BERT-based patch correctness assessment approach that uses pre-trained language models with contrastive learning and data augmentation, making it the first to exploit pre-training and fine-tuning PLMs via contrastive learning and data augmentation for assessing patch correctness. On 2274 patches from Defects4J, ComPass achieves 88.35% accuracy, 87.50% precision, 88.69% recall and 88.09% F1-score, improving the state-of-the-art technique APPT by 6.33% accuracy, 5.29% precision, 8.87% recall, and 7.05% F1-score.

Another recent approach involves a novel patch graph representation named Attributed Patch Semantic Graph (APSG) and a new parameter-efficient fine-tuning method of LLMs named Graph-LoRA, which can effectively incorporate additional graph information while fine-tuning LLMs.

## Code Representation Study

An extensive study evaluates the performance of different code representations on predicting patch correctness, involving more than 500 trained APCA models, showing that graph-based representation consistently outperforms other representations, with an average accuracy of 82.69% for CPG across three GNN models.

These approaches represent significant advances in using deep learning for automated patch correctness assessment, moving beyond traditional static and dynamic methods to leverage modern neural network architectures and pre-trained language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a74b53b-11f3-4a1d-b8d4-c9732d5ef900",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "5f48b995-c460-457d-95f9-397409b9f071",
  "sourceToolAssistantUUID": "0a74b53b-11f3-4a1d-b8d4-c9732d5ef900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T23:00:40.894Z_

<details><summary>↩ Tool result · `toolu_01W5nvvnP6JeXWyAGJ8DLV3o`</summary>

```text
Web search results for query: "site:arxiv.org "patch correctness" 2025 2026 assessment"

Links: [{"title":"[2507.22580v1] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580v1"},{"title":"[2505.02629] Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2505.02629"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"[1805.05983] On Reliability of Patch Correctness Assessment","url":"https://ar5iv.labs.arxiv.org/html/1805.05983"},{"title":"[2602.07561] ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/abs/2602.07561"},{"title":"[2507.22580] RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment","url":"https://arxiv.org/abs/2507.22580"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"[2301.01113] Invalidator: Automated Patch Correctness Assessment via Semantic and Syntactic Reasoning","url":"https://ar5iv.labs.arxiv.org/html/2301.01113"},{"title":"[2603.00649] Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment","url":"https://arxiv.org/abs/2603.00649"},{"title":"[2303.00202] PatchZero: Zero-Shot Automatic Patch Correctness Assessment","url":"https://arxiv.org/abs/2303.00202"}]

The search returned several relevant papers from arxiv.org about patch correctness assessment from 2025-2026. Here are the key findings:

## Recent Papers on Patch Correctness Assessment (2025-2026)

**RePaCA (July 2025)**
RePaCA is a novel static APCA technique that leverages Large Language Models specialized in thinking tasks, where the model is prompted with buggy and fixed code snippets and guided to generate a Chain of Thought that ultimately provides a binary classification: correct or overfitting. When evaluated on a standard Defects4J-derived test, the approach achieves state-of-the-art performance, with 83.1% accuracy and an 84.8% F1-score.

**Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph (May 2025, updated December 2025)**
Many research efforts have been devoted for automated patch correctness assessment (APCA), and with the emergence of large language model (LLM) technology, researchers have employed LLM to assess the patch correctness and have obtained state-of-the-art performance.

**ComPass (February 2026)**
ComPass is a PLM-based APCA approach that leverages contrastive learning and data augmentation to address technical limitations of prior work. Experimental results on 2274 real-world patches from Defects4J demonstrate that ComPass achieves an accuracy of 88.35%, significantly outperforming state-of-the-art baseline APPT.

**Historian (February 2026)**
Historian is a framework that leverages Large Language Models to perform multi-reference comparisons against a knowledge base of historically validated patches, producing traceable, evidence-based verdicts. In leave-one-tool-out evaluation, Historian achieves 95.0% coverage with 88.4% accuracy, reducing manual validation to 5% of patches, and as an evidence-based pre-filter, enhancing the accuracy of standalone APCA tools by up to 21.8%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae5d5d3c-fd6f-4ee6-9d41-dc0559f5b912",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "4a62e4d4-a460-442c-bab1-aaffefa28c85",
  "sourceToolAssistantUUID": "ae5d5d3c-fd6f-4ee6-9d41-dc0559f5b912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-11T23:00:43.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FK1Q4eq3629oLvLVjVu2J3`</summary>

```json
{
  "query": "arXiv 2603.07520 code representation deep learning patch correctness assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a62e4d4-a460-442c-bab1-aaffefa28c85",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcVkWiskZ6a1j5tU6rQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6db419ac-14b5-4c13-a09f-72b83df68f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiayxqFHdndCmpjZH5T9ga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3062,
      "cache_read_input_tokens": 20601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3062,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-11T23:00:43.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGPwDZwJfRjif3dRmYUHGB`</summary>

```json
{
  "query": "arXiv 2603.00649 Historian APR benchmarking evidence-based assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db419ac-14b5-4c13-a09f-72b83df68f17",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcVkWiskZ6a1j5tU6rQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d579366-3d91-44c2-a0ca-c7df6432c411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiayxqFHdndCmpjZH5T9ga",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3062,
      "cache_read_input_tokens": 20601,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3062
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 20601,
          "cache_creation_input_tokens": 3062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3062,
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

_source line 37 · 2026-05-11T23:00:48.289Z_

<details><summary>↩ Tool result · `toolu_01FK1Q4eq3629oLvLVjVu2J3`</summary>

```text
Web search results for query: "arXiv 2603.07520 code representation deep learning patch correctness assessment"

Links: [{"title":"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200802944T/abstract"},{"title":"On the Effectiveness of Code Representation in Deep Learning-Based Automated Patch Correctness Assessment","url":"https://arxiv.org/html/2603.07520v1"},{"title":"[2008.02944] Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair","url":"https://arxiv.org/abs/2008.02944"},{"title":"Learning to Represent Patches","url":"https://arxiv.org/html/2308.16586"},{"title":"Evaluating Representation Learning of Code Changes for ...","url":"https://arxiv.org/pdf/2008.02944"},{"title":"ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair","url":"https://arxiv.org/html/2602.07561"},{"title":"Automatic Patch Correctness Assessment with Large Language Model","url":"https://arxiv.org/html/2303.00202v3"},{"title":"Technical Report: Toward Patch Robustness Certification and Detection for Deep Learning Systems Beyond Consistent Samples","url":"https://arxiv.org/html/2512.06123"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Evaluating representation learning of code changes for predicting patch correctness in program repair | Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3324884.3416532"}]

Based on the search results, I found the paper you're looking for:

The arXiv paper 2603.07520, titled "On the Effectiveness of Code Representation in Deep Learning-Based Automated Patch Correctness Assessment," addresses how patched code snippets are encoded into well-designed representations for correctness prediction, with a focus on systematically examining code representation's role.

The paper appears to be a recent contribution (published March 8, 2026) to the field of automated program repair, specifically focusing on evaluating different approaches to representing code changes for assessing whether software patches are correct. This builds on a growing body of research that explores how deep learning models can better understand and reason about code modifications and their correctness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6db419ac-14b5-4c13-a09f-72b83df68f17",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "03267c70-eaec-4014-95f3-c69aff1e6fed",
  "sourceToolAssistantUUID": "6db419ac-14b5-4c13-a09f-72b83df68f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-11T23:00:51.906Z_

<details><summary>↩ Tool result · `toolu_01PGPwDZwJfRjif3dRmYUHGB`</summary>

```text
Web search results for query: "arXiv 2603.00649 Historian APR benchmarking evidence-based assessment"

Links: [{"title":"[2603.00649] Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment","url":"https://arxiv.org/abs/2603.00649"},{"title":"Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment","url":"https://arxiv.org/html/2603.00649"},{"title":"[2603.18019] BenchBrowser: Retrieving Evidence for Evaluating Benchmark Validity","url":"https://arxiv.org/abs/2603.18019"},{"title":"[2603.10765] RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems","url":"https://arxiv.org/abs/2603.10765"},{"title":"[2604.25256] AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery","url":"https://arxiv.org/abs/2604.25256"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1107&show=2000"},{"title":"[2603.20807] BenchBench: Benchmarking Automated Benchmark Generation","url":"https://arxiv.org/abs/2603.20807"},{"title":"Efficient Benchmarking of AI Agents","url":"https://arxiv.org/html/2603.23749v1"},{"title":"[2603.08680v1] Metriq: A Collaborative Platform for Benchmarking Quantum Computers","url":"https://arxiv.org/abs/2603.08680v1"},{"title":"[2603.06580] RISCBench: Benchmarking RISC-V Orchestration Efficiency in FPGA and FPGA-Like Computing Engines","url":"https://arxiv.org/abs/2603.06580"}]

Based on the search results, I found the paper you're looking for. Here's what the arXiv paper 2603.00649 is about:

**Paper Title:** Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment

**Authors:** Sahand Moslemi, Mayasah Lami, and Anil Koyuncu from Bilkent University

**Problem Addressed:** Assessing the correctness of patches generated by Automated Program Repair (APR) is a major bottleneck, as manual validation is labor-intensive and limited: exact matching overlooks valid variants, while semantic inspection is subjective and hard to reproduce.

**Key Findings:** Analysis of a large corpus of tool-generated patches reveals that about 39% of unique correct patches are syntactic clones, suggesting opportunities for automation, yet about 65% of bugs have multiple distinct correct fixes, making single-reference assessment insufficient.

**The Historian Framework:** Historian leverages Large Language Models to perform multi-reference comparisons against a knowledge base of historically validated patches, producing traceable, evidence-based verdicts while conservatively isolating novel cases as Unknown.

**Results:** In leave-one-tool-out evaluation, Historian achieves 95.0% coverage with 88.4% accuracy, reducing manual validation to 5% of patches, and as an evidence-based pre-filter, enhances the accuracy of standalone APCA tools by up to 21.8%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d579366-3d91-44c2-a0ca-c7df6432c411",
  "isSidechain": true,
  "promptId": "a06ed623-5f20-4607-9521-c8b92a171372",
  "agentId": "a2cd6c34985cbd664",
  "type": "user",
  "uuid": "843b807d-0b5a-40e5-9a0f-c72bff6d9349",
  "sourceToolAssistantUUID": "9d579366-3d91-44c2-a0ca-c7df6432c411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-11T23:01:35.201Z_

Now I have comprehensive information to provide a thorough verification report. Here are my findings:

---

## Verification Results for APCA Research Claims

### 1. ComPass (arXiv 2602.07561, Feb 2026)
**VERIFIED.** The paper exists at the claimed arXiv ID. The title is "ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair." The claimed results are confirmed: **88.35% accuracy** on 2,274 real-world patches from Defects4J, along with 87.50% precision, 88.69% recall, and 88.09% F1-score. The methodology description is accurate -- it uses contrastive learning with code transformation rules on PLMs (pre-trained language models), pre-training with semantic-preserving code snippets and fine-tuning with a binary classifier. ComPass is reported to improve over APPT by 6.33% accuracy. Published February 7, 2026.

### 2. APSG/Graph-LoRA (arXiv 2505.02629, May 2025)
**VERIFIED, but accuracy claim needs nuance.** The paper exists: "Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment." The two core contributions (Attributed Patch Semantic Graph and Graph-LoRA PEFT method) are confirmed. However, the specific accuracy range "85.8-96.8%" could not be directly confirmed from the search results. What the search results do confirm is that it improves accuracy by **3.1% to 7.5%** and F1 by **3.0% to 7.1%** compared to the best prior static method (LLM4PatchCorrect). Since LLM4PatchCorrect reports ~84.4% accuracy, an improvement of 3.1-7.5% would yield roughly **87.5-91.9%**, which does not match the claimed "85.8-96.8%" range. The range you cited may correspond to results across different datasets (Wang, Lin, Merge datasets) rather than just Defects4J. The paper was updated in December 2025.

### 3. RePaCA (arXiv 2507.22580, 2025)
**VERIFIED.** The paper exists: "RePaCA: Leveraging Reasoning Large Language Models for Static Automated Patch Correctness Assessment." The claimed **83.1% accuracy** is confirmed, along with 84.8% F1-score on a standard Defects4J-derived test set. The methodology is confirmed: it uses reasoning LLMs prompted with buggy/fixed code snippets to generate Chain-of-Thought analysis, fine-tuned with Reinforcement Learning using Group Relative Policy Optimization (GRPO). The paper also claims superior generalization on cross-dataset evaluation.

### 4. APPT (TSE 2024)
**VERIFIED.** The paper exists: "APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models," published in IEEE TSE 2024 (arXiv 2301.12453). The claimed **79.7% accuracy** is confirmed, along with 83.2% recall. APPT outperformed CACHE by 4.3% accuracy and 6.7% recall. It uses a pre-trained model as encoder, followed by LSTM and a classifier. Code is available at github.com/iSEngLab/APPT.

### 5. Shibboleth (ISSTA 2022)
**VERIFIED.** The paper exists: "Patch Correctness Assessment in Automated Program Repair Based on the Impact of Patches on Production and Test Code," published at ISSTA 2022 by Ali Ghanbari and Andrian Marcus. The claimed **88.7% accuracy** is confirmed (reported as 0.887 accuracy, 0.852 F1-score in classification mode). It is a **dynamic** APCA technique that measures patch impact across three facets: syntactic similarity, semantic similarity on production code, and test code coverage. Evaluated on 1,871 patches from 29 APR systems. Note: Shibboleth is dynamic (requires test execution), so it is not directly comparable to static methods.

---

## SOTA Landscape Assessment

The list captures the main APCA methods reasonably well, but several notable approaches are missing:

### Missing from the list:

- **LLM4PatchCorrect** (TSE 2024) -- Uses StarCoder-7B LLM with bug descriptions, execution traces, and failing test cases. Achieves **84.4% accuracy** and 86.5% F1-score in a zero-shot cross-tool setting. This is a key baseline that APSG/Graph-LoRA compares against.

- **PatchZero** (arXiv 2303.00202, updated 2024) -- Zero-shot approach achieving **82.7% accuracy** and 86.0% F1-score without labeled patches from unseen APR tools.

- **Invalidator** (IEEE TSE 2023) -- Uses semantic (program invariants) and syntactic reasoning via pre-trained language models. Important prior work in the static APCA space.

- **Historian** (arXiv 2603.00649, March 2026) -- A very recent framework using LLMs for multi-reference comparison against historically validated patches. Achieves **88.4% accuracy** with 95.0% coverage, and can enhance other APCA tools' accuracy by up to 21.8% as a pre-filter. This is a complementary approach rather than a direct competitor.

- **Code Representation Study** (arXiv 2603.07520, March 2026) -- An extensive empirical study evaluating 500+ APCA models across different code representations, finding graph-based representations (CPG) consistently outperform others with ~82.69% average accuracy.

### Overall accuracy ranking (approximate, on Defects4J-derived benchmarks):

| Method | Type | Accuracy | Year |
|--------|------|----------|------|
| ComPass | Static | 88.35% | 2026 |
| Shibboleth | Dynamic | 88.7% | 2022 |
| Historian | Hybrid/LLM | 88.4% | 2026 |
| APSG/Graph-LoRA | Static | ~87-92% | 2025 |
| LLM4PatchCorrect | Static/LLM | 84.4% | 2024 |
| RePaCA | Static/LLM | 83.1% | 2025 |
| PatchZero | Static/LLM | 82.7% | 2023 |
| APPT | Static | 79.7% | 2024 |

**Key caveat**: Direct comparison across these numbers is problematic because they use different evaluation datasets, dataset splits, and experimental setups. Static vs. dynamic methods have fundamentally different requirements (dynamic methods like Shibboleth need test execution, which is far more expensive). Cross-tool generalization settings also differ significantly.

The overall landscape described is **largely accurate** -- APCA is an active and rapidly evolving field where static LLM-based methods are closing the gap with dynamic methods, and ComPass appears to be among the current SOTA for static approaches.

Sources:
- [ComPass (arXiv 2602.07561)](https://arxiv.org/abs/2602.07561)
- [APSG/Graph-LoRA (arXiv 2505.02629)](https://arxiv.org/abs/2505.02629)
- [RePaCA (arXiv 2507.22580)](https://arxiv.org/abs/2507.22580)
- [APPT (arXiv 2301.12453)](https://arxiv.org/abs/2301.12453)
- [APPT GitHub](https://github.com/iSEngLab/APPT)
- [APPT IEEE Xplore](https://ieeexplore.ieee.org/document/10402095/)
- [Shibboleth (ISSTA 2022)](https://dl.acm.org/doi/10.1145/3533767.3534368)
- [Shibboleth PDF](https://ali-ghanbari.github.io/publications/issta22-shibboleth.pdf)
- [Shibboleth GitHub](https://github.com/ali-ghanbari/shibboleth)
- [LLM4PatchCorrect (TSE 2024)](https://dl.acm.org/doi/abs/10.1109/TSE.2024.3452252)
- [PatchZero (arXiv 2303.00202)](https://arxiv.org/abs/2303.00202)
- [Invalidator (IEEE TSE 2023)](https://ieeexplore.ieee.org/document/10066209/)
- [Historian (arXiv 2603.00649)](https://arxiv.org/abs/2603.00649)
- [Code Representation Study (arXiv 2603.07520)](https://arxiv.org/html/2603.07520v1)
- [Patch Correctness Assessment Survey (ACM TOSEM)](https://dl.acm.org/doi/10.1145/3702972)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "843b807d-0b5a-40e5-9a0f-c72bff6d9349",
  "isSidechain": true,
  "agentId": "a2cd6c34985cbd664",
  "requestId": "req_011CawcWZnLFgyNdmCM8SJFv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7453c28-f037-449d-9273-2a37a70546d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c8c7043e-0aea-4c45-bafa-2f2b45f858d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkqsgAVxqtQubFWtt8Zutn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 23663,
      "output_tokens": 2247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2247,
          "cache_read_input_tokens": 23663,
          "cache_creation_input_tokens": 1702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1702,
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
