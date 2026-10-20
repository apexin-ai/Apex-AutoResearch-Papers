# Research conversation: I need to verify two key papers cited in a research proposal: 1. "No Training No Problem Rethinking Classifier-Free Guid

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a63e0bcfb0ad64b5c.jsonl`
- **Structured JSON:** [`e36ef9f0f139ce46dcd7.json`](../../sessions/e3/e36ef9f0f139ce46dcd7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-10T19:46:15.086Z_

I need to verify two key papers cited in a research proposal:

1. "No Training No Problem Rethinking Classifier-Free Guidance" ICLR 2025 — also known as Independent Condition Guidance (ICG). Verify it exists, was published at ICLR 2025, and that it enables CFG on any pretrained conditional model without dropout training by using random/independent conditions.

2. "Diffusion State-Guided Projected Gradient" or "DiffStateGrad" ICLR 2025 — verify it exists, was published at ICLR 2025, and that it uses SVD-based subspace projection for filtering diffusion guidance signals in image restoration.

3. "Towards Understanding Mechanisms Classifier-Free Guidance" CPC theory NeurIPS 2025 — verify this paper about contrastive principal components decomposition of CFG exists and was published at NeurIPS 2025.

4. Search for "β-CFG adaptive scaling classifier-free guidance" 2025 — verify timestep-adaptive guidance scheduling exists.

Use WebSearch for each. Report exact findings. Under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "21b9d1d0-a067-4481-86d6-71be1ae18e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:46:15.089Z_

```json
{
  "parentUuid": "21b9d1d0-a067-4481-86d6-71be1ae18e2c",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
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
  "uuid": "92af87d5-474d-4064-b522-8e5c9862b19d",
  "timestamp": "2026-05-10T19:46:15.089Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:46:18.808Z_



I'll search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92af87d5-474d-4064-b522-8e5c9862b19d",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTru4TQCHcjfNGCK2nm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5b35744-b175-4f06-abf4-ac78c56003a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwNybHbuZipQo1uBuK2iXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 810,
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

_source line 4 · 2026-05-10T19:46:19.359Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VZuzkhMAfXMVks3Yw9EGrq`</summary>

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
  "parentUuid": "f5b35744-b175-4f06-abf4-ac78c56003a1",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTru4TQCHcjfNGCK2nm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dc9e938-7dc1-4963-b534-2d1b29fec095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwNybHbuZipQo1uBuK2iXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 8223,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 810
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 810,
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

_source line 5 · 2026-05-10T19:46:19.361Z_

<details><summary>↩ Tool result · `toolu_01VZuzkhMAfXMVks3Yw9EGrq`</summary>

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
  "parentUuid": "9dc9e938-7dc1-4963-b534-2d1b29fec095",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "df3d587a-0660-4409-8828-44666f8bce7f",
  "sourceToolAssistantUUID": "9dc9e938-7dc1-4963-b534-2d1b29fec095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:46:22.762Z_



Now I'll search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3d587a-0660-4409-8828-44666f8bce7f",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTsDjc9uDakse8Z8euJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c6e55c3-a05c-4303-99e9-4b1c3dd5fbc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWNfAjv11iHs4z4jwe4Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 7 · 2026-05-10T19:46:24.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hk1catMm5eep9MtmGGSCtD`</summary>

```json
{
  "query": "\"No Training No Problem\" \"Independent Condition Guidance\" ICLR 2025 classifier-free guidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c6e55c3-a05c-4303-99e9-4b1c3dd5fbc3",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTsDjc9uDakse8Z8euJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eb7c185-1869-4578-ba8e-5438e74d2daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWNfAjv11iHs4z4jwe4Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 8 · 2026-05-10T19:46:24.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tTy3AyNYNq97ecVKt4qD5`</summary>

```json
{
  "query": "\"DiffStateGrad\" \"Diffusion State-Guided Projected Gradient\" ICLR 2025 SVD subspace projection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb7c185-1869-4578-ba8e-5438e74d2daa",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTsDjc9uDakse8Z8euJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d434534-8c78-4da3-a884-d93aa19b7065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWNfAjv11iHs4z4jwe4Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 9 · 2026-05-10T19:46:25.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vT3vAn3da1n1wdWt2yBwT`</summary>

```json
{
  "query": "\"Towards Understanding Mechanisms\" \"classifier-free guidance\" \"contrastive principal components\" NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d434534-8c78-4da3-a884-d93aa19b7065",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTsDjc9uDakse8Z8euJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3477a661-94a6-4286-9ffe-af7f9c21e333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWNfAjv11iHs4z4jwe4Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 10 · 2026-05-10T19:46:26.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WrwdyyLEbWLd2CK3tprcZy`</summary>

```json
{
  "query": "\"β-CFG\" OR \"beta-CFG\" adaptive scaling classifier-free guidance timestep 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3477a661-94a6-4286-9ffe-af7f9c21e333",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTsDjc9uDakse8Z8euJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "980ff037-7f0f-4709-824b-74b08a857a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWNfAjv11iHs4z4jwe4Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9033,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 275,
          "cache_read_input_tokens": 9033,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
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

_source line 11 · 2026-05-10T19:46:29.345Z_

<details><summary>↩ Tool result · `toolu_015vT3vAn3da1n1wdWt2yBwT`</summary>

```text
Web search results for query: ""Towards Understanding Mechanisms" "classifier-free guidance" "contrastive principal components" NeurIPS 2025"

No links found.

The search did not return any results for that specific combination of terms and phrases. This could mean that:

1. A paper with exactly that title and those specific terms may not be publicly available or indexed yet
2. The exact phrasing might be slightly different
3. The paper might not have been published or released yet as of the available search index

Would you like me to try a modified search? For example, I could:
- Search for just the title or key concepts separately
- Search for "classifier-free guidance NeurIPS 2025"
- Search for the authors if you know them
- Try a different combination of the key terms

Let me know how you'd like me to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3477a661-94a6-4286-9ffe-af7f9c21e333",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "dfdbb07a-7cb8-42a1-b9f1-7842c0501fbf",
  "sourceToolAssistantUUID": "3477a661-94a6-4286-9ffe-af7f9c21e333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:46:30.977Z_

<details><summary>↩ Tool result · `toolu_01Hk1catMm5eep9MtmGGSCtD`</summary>

```text
Web search results for query: ""No Training No Problem" "Independent Condition Guidance" ICLR 2025 classifier-free guidance"

Links: [{"title":"ICLR Poster No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models","url":"https://iclr.cc/virtual/2025/poster/29126"},{"title":"No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models | Disney Research Studios","url":"https://studios.disneyresearch.com/2025/04/23/no-training-no-problem-rethinking-diffusion-guidance-for-diffusion-models/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8bead340bb510de5c8356f60ca039efc-Paper-Conference.pdf"},{"title":"[Quick Review] No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models","url":"https://liner.com/review/no-training-no-problem-rethinking-classifierfree-guidance-for-diffusion-models"},{"title":"RETHINKING CLASSIFIER-FREE GUIDANCE FOR ...","url":"https://studios.disneyresearch.com/app/uploads/2025/05/No-Training-No-Problem-Rethinking-Classifier-Free-Guidance-for-Diffusion-Models-Paper.pdf"},{"title":"ICLR 2025 Orals","url":"https://iclr.cc/virtual/2025/events/oral"},{"title":"Carnegie Mellon University at ICLR 2025 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2025/04/23/carnegie-mellon-university-at-iclr-2025/"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"}]

Based on the search results, here's what I found about "No Training, No Problem" and Independent Condition Guidance at ICLR 2025:

## Overview

The paper introduces Independent Condition Guidance (ICG), which provides the benefits of classifier-free guidance without the need for any special training procedures.

## Problem Being Addressed

Classifier-free guidance (CFG) has become the standard method for enhancing the quality of conditional diffusion models. However, employing CFG requires either training an unconditional model alongside the main diffusion model or modifying the training procedure by periodically inserting a null condition.

## Key Innovation

The paper revisits the core principles of CFG and introduces Independent Condition Guidance (ICG), which provides the benefits of CFG without the need for any special training procedures. The approach streamlines the training process of conditional diffusion models and can also be applied during inference on any pretrained conditional model.

Additionally, by leveraging the time-step information encoded in all diffusion networks, the authors propose an extension of CFG, called timestep guidance (TSG), which can be applied to any diffusion model, including unconditional ones.

## Performance

ICG consistently matches or slightly surpasses the quantitative performance of standard CFG across diverse conditional diffusion models, including Stable Diffusion, DiT-XL/2, Pose-to-Image, and MDM, as evidenced by FID scores. For instance, on Stable Diffusion, ICG achieved an FID of 20.05 compared to CFG's 20.13, and on DiT-XL/2, ICG yielded an FID of 5.50 versus CFG's 5.56.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eb7c185-1869-4578-ba8e-5438e74d2daa",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "ed363d3a-7f87-44aa-86b1-f904974b3fae",
  "sourceToolAssistantUUID": "2eb7c185-1869-4578-ba8e-5438e74d2daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:46:32.159Z_

<details><summary>↩ Tool result · `toolu_015tTy3AyNYNq97ecVKt4qD5`</summary>

```text
Web search results for query: ""DiffStateGrad" "Diffusion State-Guided Projected Gradient" ICLR 2025 SVD subspace projection"

Links: [{"title":"GitHub - Anima-Lab/DiffStateGrad: DiffStateGrad [ICLR 2025]","url":"https://github.com/Anima-Lab/DiffStateGrad"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://diffstategrad.github.io/"},{"title":"DIFFUSION STATE-GUIDED PROJECTED GRADIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5b7f7a0603b75e39ffebbf95e3b7ee-Paper-Conference.pdf"},{"title":"[2410.03463] Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://arxiv.org/abs/2410.03463"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d5b7f7a0603b75e39ffebbf95e3b7ee-Abstract-Conference.html"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems | OpenReview","url":"https://openreview.net/forum?id=kRBQwlkFSP"},{"title":"ICLR Poster Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://iclr.cc/virtual/2025/poster/28584"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://arxiv.org/html/2410.03463v1"},{"title":"GitHub - moatifbutt/awesome-diffusion-iclr-2025: List of diffusion related active submissions on OpenReview for ICLR 2025. · GitHub","url":"https://github.com/moatifbutt/awesome-diffusion-iclr-2025"},{"title":"[PDF] Diffusion State-Guided Projected Gradient for Inverse Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/afcb67c251fc60bbb9c8946c184990e7be46a545"}]

Based on the search results, here's what I found about DiffStateGrad:

## Overview

DiffStateGrad is a novel approach that enhances diffusion-based inverse problem solvers by projecting measurement guidance gradients onto a data-driven low-rank subspace defined by intermediate diffusion states.

## Key Technical Details

The method projects the measurement gradient onto a subspace that is a low-rank approximation of an intermediate state of the diffusion process. More specifically, the approach performs singular value decomposition (SVD) on the diffusion state of an image to which guidance is applied and uses the r highest contributing singular vectors as a choice of the projection matrix.

The SVD captures the principal directions of variation in the diffusion state, which are likely to align with the local structure of the manifold when the data is high-dimensional, and by adaptively choosing the rank based on a variance retention threshold, the projection preserves the most significant state-related structural information.

## Benefits and Applications

DiffStateGrad, as a module, can be added to a wide range of diffusion-based inverse solvers to improve the preservation of the diffusion process on the prior manifold and filter out artifact-inducing components. It improves the robustness of diffusion models in terms of the choice of measurement guidance step size and noise while improving the worst-case performance, and demonstrates improvements upon the state-of-the-art on linear and nonlinear image restoration inverse problems.

## Publication

The paper is by Rayhan Zirvi, Bahareh Tolooshams, and Anima Anandkumar, published at The Thirteenth International Conference on Learning Representations (ICLR 2025). The code is available on GitHub at the Anima-Lab repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d434534-8c78-4da3-a884-d93aa19b7065",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "c87c07a6-c4e0-426b-8abb-68e321f735c6",
  "sourceToolAssistantUUID": "9d434534-8c78-4da3-a884-d93aa19b7065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:46:33.198Z_

<details><summary>↩ Tool result · `toolu_01WrwdyyLEbWLd2CK3tprcZy`</summary>

```text
Web search results for query: ""β-CFG" OR "beta-CFG" adaptive scaling classifier-free guidance timestep 2025"

Links: [{"title":"GitHub - gmum/beta-CFG: This paper presents β-CFG, a dynamic guidance method for text-to-image diffusion models. Unlike standard CFG, which uses a fixed guidance scale, β-CFG adapts guidance strength over time using a β-distribution. This improves image quality, keeps sampling closer to the data manifold, and achieves better FID while maintaining prompt alignment. · GitHub","url":"https://github.com/gmum/beta-CFG"},{"title":"[2502.10574] Classifier-free Guidance with Adaptive Scaling","url":"https://arxiv.org/abs/2502.10574"},{"title":"Classifier-free Guidance with Adaptive Scaling","url":"https://arxiv.org/html/2502.10574v1"},{"title":"(PDF) Classifier-free Guidance with Adaptive Scaling","url":"https://www.researchgate.net/publication/389090573_Classifier-free_Guidance_with_Adaptive_Scaling"},{"title":"Classifier-Free Diffusion Guidance (CFG)","url":"https://www.emergentmind.com/topics/classifier-free-diffusion-guidance-cfg"},{"title":"Paper page - Classifier-free Guidance with Adaptive Scaling","url":"https://huggingface.co/papers/2502.10574"},{"title":"TCFG: Truncated Classifier-Free Guidance for Efficient and ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_TCFG_Truncated_Classifier-Free_Guidance_for_Efficient_and_Scalable_Text-to-Image_Acceleration_ICCV_2025_paper.pdf"},{"title":"Classifier-Free Guidance Rescaling","url":"https://www.emergentmind.com/topics/classifier-free-guidance-cfg-rescaling"},{"title":"[Literature Review] Classifier-free Guidance with Adaptive Scaling","url":"https://www.themoonlight.io/en/review/classifier-free-guidance-with-adaptive-scaling"},{"title":"An overview of classifier-free guidance for diffusion models | AI Summer","url":"https://theaisummer.com/classifier-free-guidance/"}]

Based on the search results, I found comprehensive information about β-CFG (beta-CFG):

## Overview

β-CFG is a dynamic guidance method for text-to-image diffusion models that adapts guidance strength over time using a β-distribution, unlike standard CFG which uses a fixed guidance scale.

## Key Components

β-CFG stabilizes the effects of guiding by gradient-based adaptive normalization and uses the family of single-modal (β-distribution), time-dependent curves to dynamically adapt the trade-off between prompt matching and the quality of samples during the diffusion denoising process.

## Problem It Addresses

In practice, controlling the impact of guidance involves a trade-off: strong guidance makes generated images fit the conditioned text perfectly but at the cost of their quality, while small guidance generates high-quality results but the images don't suit the prompt.

## Benefits

β-CFG improves image quality, keeps sampling closer to the data manifold, and achieves better FID while maintaining prompt alignment. The model obtained better FID scores, maintaining the text-to-image CLIP similarity scores at a level similar to that of the reference CFG.

## Publication

The work was published as an arXiv preprint (arXiv:2502.10574) on February 14, 2025, with authors including Malarz, Kasymov, Zięba, Tabor, and Spurek.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "980ff037-7f0f-4709-824b-74b08a857a28",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "ae9cb6b9-c449-4912-a32a-fff5df84c112",
  "sourceToolAssistantUUID": "980ff037-7f0f-4709-824b-74b08a857a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:46:36.600Z_

Let me do a broader search for paper 3 with relaxed terms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9cb6b9-c449-4912-a32a-fff5df84c112",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTtF2XUPCcf462uoDp4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72c21b57-c752-441a-a8cf-aac92cc830ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoDXhPsmgQN9gEj59hVWax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 10437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3450,
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

_source line 16 · 2026-05-10T19:46:37.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JTk2JDn3YPfgPt9CahQZJ7`</summary>

```json
{
  "query": "\"classifier-free guidance\" \"contrastive\" \"principal components\" mechanism theory NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72c21b57-c752-441a-a8cf-aac92cc830ba",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTtF2XUPCcf462uoDp4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d47ce811-9903-4a73-afff-b32b886576d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoDXhPsmgQN9gEj59hVWax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 10437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3450,
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

_source line 17 · 2026-05-10T19:46:38.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RaDKngwiwyMcwss2KkzpxX`</summary>

```json
{
  "query": "\"towards understanding\" classifier-free guidance mechanism decomposition NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47ce811-9903-4a73-afff-b32b886576d3",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTtF2XUPCcf462uoDp4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d881a2c3-669a-4cad-8a88-2e86bd8111da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoDXhPsmgQN9gEj59hVWax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 10437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3450,
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

_source line 18 · 2026-05-10T19:46:43.403Z_

<details><summary>↩ Tool result · `toolu_01RaDKngwiwyMcwss2KkzpxX`</summary>

```text
Web search results for query: ""towards understanding" classifier-free guidance mechanism decomposition NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117182"},{"title":"NeurIPS Poster Towards a Golden Classifier-Free Guidance Path via Foresight Fixed Point Iterations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115124"},{"title":"[2505.19210] Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://arxiv.org/abs/2505.19210"},{"title":"NeurIPS Poster Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking","url":"https://neurips.cc/virtual/2025/poster/120339"},{"title":"Towards Understanding the Mechanisms of Classifier-Free Guidance | OpenReview","url":"https://openreview.net/forum?id=bRAm7A02Qm"},{"title":"Classifier-Free Guidance (CFG)","url":"https://apxml.com/courses/intro-diffusion-models/chapter-6-conditional-generation-diffusion/classifier-free-guidance"},{"title":"Improving Classifier-Free Guidance of Flow Matching via Manifold Projection","url":"https://arxiv.org/html/2601.21892"},{"title":"[2207.12598] Classifier-Free Diffusion Guidance","url":"https://arxiv.org/abs/2207.12598"},{"title":"Eliminating Oversaturation and Artifacts of High Guidance Scales in Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=e2ONKX6qzJ"},{"title":"NeurIPS Classifier-Free Diffusion Guidance","url":"https://neurips.cc/virtual/2021/48591"}]

Based on the search results, I found the paper you're looking for:

"Towards Understanding the Mechanisms of Classifier-Free Guidance" was published at NeurIPS 2025 as a spotlight paper. 

Classifier-free guidance (CFG) is a core technique powering state-of-the-art image generation systems, yet its underlying mechanisms remain poorly understood. The paper analyzes CFG in a simplified linear diffusion model and reveals that linear CFG improves generation quality via three distinct components: (i) a mean-shift term that approximately steers samples in the direction of class means, (ii) a positive Contrastive Principal Components (CPC) term that amplifies class-specific features, and (iii) a negative CPC term that suppresses generic features prevalent in unconditional data.

The paper is available on both the NeurIPS website and arXiv (paper ID 2505.19210), and was authored by Xiang Li and collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d881a2c3-669a-4cad-8a88-2e86bd8111da",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "c92ee232-6fbd-44c9-b168-9a0214f824b8",
  "sourceToolAssistantUUID": "d881a2c3-669a-4cad-8a88-2e86bd8111da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:46:44.067Z_

<details><summary>↩ Tool result · `toolu_01JTk2JDn3YPfgPt9CahQZJ7`</summary>

```text
Web search results for query: ""classifier-free guidance" "contrastive" "principal components" mechanism theory NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://neurips.cc/virtual/2025/poster/117182"},{"title":"[2505.19210] Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://arxiv.org/abs/2505.19210"},{"title":"Fifteen papers by ECE researchers at NeurIPS 2025","url":"https://ece.engin.umich.edu/stories/fifteen-papers-by-ece-researchers-at-neurips-2025"},{"title":"Towards Understanding the Mechanisms of Classifier-Free Guidance | OpenReview","url":"https://openreview.net/forum?id=bRAm7A02Qm"},{"title":"NeurIPS Improved Sampling from Masked Diffusion Models with Position Contrastive Guidance","url":"https://neurips.cc/virtual/2025/loc/san-diego/125443"},{"title":"Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://arxiv.org/html/2505.19210"},{"title":"(PDF) Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://www.researchgate.net/publication/392104901_Towards_Understanding_the_Mechanisms_of_Classifier-Free_Guidance"},{"title":"Paper page - Towards Understanding the Mechanisms of Classifier-Free Guidance","url":"https://huggingface.co/papers/2505.19210"},{"title":"No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=b3CzCCCILJ"},{"title":"Adaptive Classifier-Free Guidance via Dynamic Low- ...","url":"https://openreview.net/pdf?id=FLjL20fPul"}]

I found relevant results for your search query. Here's what the research shows:

## Paper Overview

"Towards Understanding the Mechanisms of Classifier-Free Guidance" was published as a NeurIPS 2025 spotlight paper. Classifier-free guidance (CFG) is a core technique powering state-of-the-art image generation systems, yet its underlying mechanisms remain poorly understood.

## Key Findings on Mechanism

The research demonstrates that CFG guidance naturally decomposes into three components with distinct effects: (i) a mean-shift term that approximately pushes the samples towards the direction of the class mean, (ii) a positive contrastive principal components (CPC) term that enhances the target class's unique features and (iii) a negative contrastive principal components (CPC) term that suppresses the features prominent in the unconditional dataset.

## Theory and Validation

The authors first analyze CFG in a simplified linear diffusion model, where they show its behavior closely resembles that observed in the nonlinear case. They then verify these insights in real-world, nonlinear diffusion models: over a broad range of noise levels, linear CFG resembles the behavior of its nonlinear counterpart. Although the two eventually diverge at low noise levels, the insights from the linear analysis still shed light on the CFG's mechanism in the nonlinear regime.

The paper appears to be available on arXiv (2505.19210) and on OpenReview for the NeurIPS 2025 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d47ce811-9903-4a73-afff-b32b886576d3",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "2d03a5b5-a63b-499c-ac0f-815992767d67",
  "sourceToolAssistantUUID": "d47ce811-9903-4a73-afff-b32b886576d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T19:46:48.247Z_

Now let me check whether beta-CFG was actually published at a venue or remains a preprint.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d03a5b5-a63b-499c-ac0f-815992767d67",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTu2u3pjM8UcqKBHkFi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74584e98-4588-43ce-aa16-f052bd0f6022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEsHApBSSnQ3zhAhGh6pZ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 13887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1129,
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

_source line 21 · 2026-05-10T19:46:48.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ar9DiKiNGBgxLHxVjsi7jJ`</summary>

```json
{
  "query": "beta-CFG \"Classifier-free Guidance with Adaptive Scaling\" accepted conference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74584e98-4588-43ce-aa16-f052bd0f6022",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTu2u3pjM8UcqKBHkFi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "863c8e77-566c-4290-a66d-87e98397a987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEsHApBSSnQ3zhAhGh6pZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 13887,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 98,
          "cache_read_input_tokens": 13887,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 22 · 2026-05-10T19:46:56.027Z_

<details><summary>↩ Tool result · `toolu_01Ar9DiKiNGBgxLHxVjsi7jJ`</summary>

```text
Web search results for query: "beta-CFG "Classifier-free Guidance with Adaptive Scaling" accepted conference 2025 2026"

Links: [{"title":"[2502.10574] Classifier-free Guidance with Adaptive Scaling","url":"https://arxiv.org/abs/2502.10574"},{"title":"GitHub - gmum/beta-CFG: This paper presents β-CFG, a dynamic guidance method for text-to-image diffusion models. Unlike standard CFG, which uses a fixed guidance scale, β-CFG adapts guidance strength over time using a β-distribution. This improves image quality, keeps sampling closer to the data manifold, and achieves better FID while maintaining prompt alignment. · GitHub","url":"https://github.com/gmum/beta-CFG"},{"title":"Classifier-free Guidance with Adaptive Scaling","url":"https://arxiv.org/html/2502.10574v1"},{"title":"(PDF) Classifier-free Guidance with Adaptive Scaling","url":"https://www.researchgate.net/publication/389090573_Classifier-free_Guidance_with_Adaptive_Scaling"},{"title":"Paper page - Classifier-free Guidance with Adaptive Scaling","url":"https://huggingface.co/papers/2502.10574"},{"title":"Eliminating Oversaturation and Artifacts of High Guidance Scales in Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=e2ONKX6qzJ"},{"title":"Feedback Guidance of Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=8ySOcf7UpM"},{"title":"[Literature Review] Classifier-free Guidance with Adaptive Scaling","url":"https://www.themoonlight.io/en/review/classifier-free-guidance-with-adaptive-scaling"},{"title":"Multimodal Classifier-Free Guidance (m-cfg)","url":"https://www.emergentmind.com/topics/multimodal-classifier-free-guidance-m-cfg"},{"title":"Classifier-Free Guidance (CFG)","url":"https://www.emergentmind.com/topics/classifier-free-guidance-cfg"}]

Based on the web search results, I found information about β-CFG ("Classifier-free Guidance with Adaptive Scaling"):

## Paper Information

β-CFG (β-adaptive scaling in Classifier-Free Guidance) is a method that controls the impact of guidance during generation. β-CFG stabilizes the effects of guiding by gradient-based adaptive normalization and uses time-dependent β-distribution curves to dynamically adapt the trade-off between prompt matching and sample quality during the diffusion denoising process.

## Publication Status

The paper appears to be in **preprint stage** as of the search results. The work is currently in the preprint stage, and there may be some changes to the code. The paper was submitted to arXiv on February 14, 2025.

Based on the search results, **the paper does not appear to have been accepted to a major conference yet** as of May 2026. It is available as an arXiv preprint (2502.10574) with a GitHub repository, but I found no information indicating acceptance to specific conferences like NeurIPS, ICML, ICCV, or similar venues in 2025 or 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "863c8e77-566c-4290-a66d-87e98397a987",
  "isSidechain": true,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "agentId": "a63e0bcfb0ad64b5c",
  "type": "user",
  "uuid": "3d204e25-54ca-4144-a213-19d3da690353",
  "sourceToolAssistantUUID": "863c8e77-566c-4290-a66d-87e98397a987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T19:47:15.834Z_

Here are the findings for all four papers:

**1. "No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models" -- VERIFIED.** Published at ICLR 2025 (conference paper). Introduces Independent Condition Guidance (ICG), which enables CFG benefits on any pretrained conditional diffusion model without dropout/null-condition training. Uses random independent conditions instead of unconditional scores. Also proposes Timestep Guidance (TSG) for unconditional models. Claims are accurate.

**2. "Diffusion State-Guided Projected Gradient for Inverse Problems" (DiffStateGrad) -- VERIFIED.** Published at ICLR 2025 (conference paper). Uses SVD on intermediate diffusion states to define a low-rank subspace, then projects measurement guidance gradients onto it to filter artifact-inducing components. Applied to linear and nonlinear image restoration. By Zirvi, Tolooshams, and Anandkumar (Anima-Lab). Claims are accurate.

**3. "Towards Understanding the Mechanisms of Classifier-Free Guidance" -- VERIFIED with corrections.** Published at NeurIPS 2025 as a **spotlight** paper (arXiv: 2505.19210). Decomposes CFG into three components: (i) mean-shift toward class mean, (ii) positive Contrastive Principal Components (CPC) enhancing class-specific features, (iii) negative CPC suppressing generic features. The CPC theory claim is accurate. Note: the title is "Towards Understanding the **Mechanisms** of Classifier-Free Guidance" (not "Mechanisms of").

**4. beta-CFG ("Classifier-free Guidance with Adaptive Scaling") -- PARTIALLY VERIFIED.** The paper exists (arXiv: 2502.10574, Feb 2025) and proposes timestep-adaptive guidance scheduling using beta-distribution curves. However, it appears to remain an **arXiv preprint only** -- no evidence of acceptance at a peer-reviewed venue as of May 2026.

Sources:
- [ICLR 2025 Poster - No Training, No Problem](https://iclr.cc/virtual/2025/poster/29126)
- [ICLR 2025 Proceedings - No Training, No Problem (PDF)](https://proceedings.iclr.cc/paper_files/paper/2025/file/8bead340bb510de5c8356f60ca039efc-Paper-Conference.pdf)
- [DiffStateGrad GitHub (Anima-Lab)](https://github.com/Anima-Lab/DiffStateGrad)
- [ICLR 2025 Proceedings - DiffStateGrad](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d5b7f7a0603b75e39ffebbf95e3b7ee-Abstract-Conference.html)
- [NeurIPS 2025 Poster - Towards Understanding Mechanisms of CFG](https://neurips.cc/virtual/2025/poster/117182)
- [arXiv 2505.19210 - Towards Understanding Mechanisms of CFG](https://arxiv.org/abs/2505.19210)
- [arXiv 2502.10574 - beta-CFG](https://arxiv.org/abs/2502.10574)
- [beta-CFG GitHub](https://github.com/gmum/beta-CFG)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d204e25-54ca-4144-a213-19d3da690353",
  "isSidechain": true,
  "agentId": "a63e0bcfb0ad64b5c",
  "requestId": "req_011CauTuv3pMc5y3ZMLktG1Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "755d62fd-50c7-4f83-9393-e10aaea78db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BapT3BR55ETm8MStLZzaL4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 15016,
      "output_tokens": 832,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 832,
          "cache_read_input_tokens": 15016,
          "cache_creation_input_tokens": 1674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1674,
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
