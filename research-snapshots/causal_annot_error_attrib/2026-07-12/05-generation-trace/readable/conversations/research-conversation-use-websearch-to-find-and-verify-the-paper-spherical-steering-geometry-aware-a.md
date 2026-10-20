# Research conversation: Use WebSearch to find and verify the paper "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-add766dc6f6f2b147.jsonl`
- **Structured JSON:** [`aaea095215c9e39dad30.json`](../../sessions/aa/aaea095215c9e39dad30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-16T08:45:27.273Z_

Use WebSearch to find and verify the paper "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" (arXiv 2602.08169). I need to know:
1. Does it actually exist? What are its exact claims?
2. Does it use a "von Mises-Fisher confidence gate" that "dynamically modulates steering strength based on input uncertainty"?
3. What TruthfulQA results does it achieve (specifically MC1 percentage improvement)?
4. Does it operate per-token or per-sequence?
5. Is it actually accepted at ICML 2026?
6. Does it have released code?

Search for: "Spherical Steering geometry-aware activation rotation" and "arxiv 2602.08169". Also try fetching the arxiv page if possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "92f8201e-a8bb-47e9-8337-6032508576c8",
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

_source line 2 · 2026-05-16T08:45:27.278Z_

```json
{
  "parentUuid": "92f8201e-a8bb-47e9-8337-6032508576c8",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
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
  "uuid": "c2469f22-821d-479d-978c-52161e64fe9e",
  "timestamp": "2026-05-16T08:45:27.278Z",
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

_source line 3 · 2026-05-16T08:45:29.975Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0133gjKMyfhcHXPLme8fw3dE`</summary>

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
  "parentUuid": "c2469f22-821d-479d-978c-52161e64fe9e",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xKnPukvMtJYhP2wnp6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2951427-d7f9-45f8-8d33-5b9caf3090b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015viJpGDF3CPvSD7CmFBBVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8957,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8957,
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

_source line 4 · 2026-05-16T08:45:29.980Z_

<details><summary>↩ Tool result · `toolu_0133gjKMyfhcHXPLme8fw3dE`</summary>

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
  "parentUuid": "a2951427-d7f9-45f8-8d33-5b9caf3090b8",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "aea00ee6-3a92-4618-acc4-4ec39678c4b6",
  "sourceToolAssistantUUID": "a2951427-d7f9-45f8-8d33-5b9caf3090b8",
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

_source line 5 · 2026-05-16T08:45:32.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xe7ZZYs336wPHV3DADoSuc`</summary>

```json
{
  "query": "Spherical Steering geometry-aware activation rotation language models arxiv 2602.08169"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea00ee6-3a92-4618-acc4-4ec39678c4b6",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xKz9qv7YcfUNKjWHmn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cabf67e3-f73b-472e-987f-2125dec26ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ss3fjuFmLdTnrikHN7qJxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 6 · 2026-05-16T08:45:32.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PkrPXiDWEPV6gDJmHPUfHB`</summary>

```json
{
  "query": "\"arxiv 2602.08169\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabf67e3-f73b-472e-987f-2125dec26ef2",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xKz9qv7YcfUNKjWHmn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a523ec9e-9292-4fdd-ae49-fa15162be840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ss3fjuFmLdTnrikHN7qJxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 7 · 2026-05-16T08:45:37.515Z_

<details><summary>↩ Tool result · `toolu_01PkrPXiDWEPV6gDJmHPUfHB`</summary>

```text
Web search results for query: ""arxiv 2602.08169""

Links: [{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"The Approximate Fisher Influence Function:","url":"https://arxiv.org/pdf/2407.08169"},{"title":"arXiv:2406.08169v2 [quant-ph] 19 Jul 2024","url":"https://arxiv.org/pdf/2406.08169"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2504.08169"},{"title":"Machine Learning","url":"https://www.arxiv.org/list/cs.LG/pastweek?skip=200&show=1000"},{"title":"[2601.08169] Relational Knowledge Distillation Using Fine-tuned Function Vectors","url":"https://arxiv.org/abs/2601.08169"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=4400"},{"title":"Changxin Lao","url":"https://scholar.google.com/citations?user=LnrMFI4AAAAJ&hl=en"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"}]

The search found the paper you're looking for! Here are the details:

**Title:** Spherical Steering: Geometry-Aware Activation Rotation for Language Models

**Authors:** Zejia You and 2 other authors

**Submission Date:** February 9, 2026

**Summary:** Inference-time steering has emerged as a promising paradigm for controlling language models without the cost of retraining. However, standard approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations. The paper explores Spherical Steering, a training-free primitive that resolves this trade-off through activation rotation, where activations are rotated along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of the signal.

The paper is available on arXiv at: https://arxiv.org/abs/2602.08169


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a523ec9e-9292-4fdd-ae49-fa15162be840",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "5ccd3063-f4fd-47c5-8328-be53670eeced",
  "sourceToolAssistantUUID": "a523ec9e-9292-4fdd-ae49-fa15162be840",
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

_source line 8 · 2026-05-16T08:45:39.817Z_

<details><summary>↩ Tool result · `toolu_01Xe7ZZYs336wPHV3DADoSuc`</summary>

```text
Web search results for query: "Spherical Steering geometry-aware activation rotation language models arxiv 2602.08169"

Links: [{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"Publications","url":"https://hanjiechen.github.io/publication.html"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"Hanjie Chen's research works | Johns Hopkins University and other places","url":"https://www.researchgate.net/scientific-contributions/Hanjie-Chen-2260402100"},{"title":"ICML Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://icml.cc/virtual/2025/50230"},{"title":"Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://openreview.net/pdf/9a82b26d157916819f7a69e1e31ced6f640ca130.pdf"},{"title":"NeurIPS Poster Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://neurips.cc/virtual/2025/poster/117017"}]

I found the paper! Here are the search results for arxiv 2602.08169:

## Paper Overview

The paper "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" was submitted on February 9, 2026, by authors Zejia You, Chunyuan Deng, and Hanjie Chen.

## Key Concept

The work explores Spherical Steering, a training-free primitive that resolves the trade-off between control and generation quality through activation rotation. Standard inference-time steering approaches rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.

## Method

Rather than using fixed vector addition, the method rotates activations along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of representations. To further enhance adaptivity, the approach incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.

## Results

Extensive experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.

The paper has been accepted to the Forty-Third International Conference on Machine Learning (ICML) in Seoul, South Korea in July 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cabf67e3-f73b-472e-987f-2125dec26ef2",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "9b994107-68d8-4b3d-8043-0bcc448e9871",
  "sourceToolAssistantUUID": "cabf67e3-f73b-472e-987f-2125dec26ef2",
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

_source line 9 · 2026-05-16T08:45:42.583Z_

Now let me fetch the actual arxiv page and GitHub repo for more specific details about the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b994107-68d8-4b3d-8043-0bcc448e9871",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xLhrqXG9rgWuodJySG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3051e60e-de97-480b-95b5-facbc01d1a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018buLfjtHwzPp5v9TRjYVvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 10 · 2026-05-16T08:45:44.627Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01261jAGYB7o4LFje9k7uPUH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08169",
  "prompt": "Extract all details from this paper page: full title, all authors, abstract, submission date, any mention of von Mises-Fisher, confidence gate, TruthfulQA MC1 results, per-token vs per-sequence operation, ICML acceptance, and any code links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3051e60e-de97-480b-95b5-facbc01d1a6f",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xLhrqXG9rgWuodJySG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24580706-8766-40d4-bb9b-020f90ec459c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018buLfjtHwzPp5v9TRjYVvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 11 · 2026-05-16T08:45:45.686Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R3b5Nf8K72Aw6dDcpR9kjz`</summary>

```json
{
  "url": "https://github.com/chili-lab/Spherical-Steering",
  "prompt": "Extract all details about this repository: what code is available, README contents, any mention of von Mises-Fisher confidence gate, TruthfulQA MC1 results, per-token vs per-sequence operation, ICML 2026 acceptance status."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24580706-8766-40d4-bb9b-020f90ec459c",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xLhrqXG9rgWuodJySG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2e87e44-0e53-492d-9d20-8f2c33e9bed2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018buLfjtHwzPp5v9TRjYVvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 10845,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 643,
          "output_tokens": 288,
          "cache_read_input_tokens": 10845,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 995,
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

_source line 12 · 2026-05-16T08:45:49.659Z_

<details><summary>↩ Tool result · `toolu_01261jAGYB7o4LFje9k7uPUH`</summary>

```text
# Paper Details: Spherical Steering

**Full Title:**
"Spherical Steering: Geometry-Aware Activation Rotation for Language Models"

**Authors:**
- Zejia You
- Chunyuan Deng
- Hanjie Chen

**Abstract Summary:**
The paper introduces a training-free method for inference-time control of language models. Rather than using activation addition (which alters magnitude), it employs "activation rotation along a geodesic toward a target direction" while preserving signal integrity. A confidence gate dynamically adjusts steering strength based on input uncertainty. Results show improvements of approximately 10% on multiple-choice benchmarks including TruthfulQA, COPA, and Storycloze.

**Submission Date:**
February 9, 2026

**Key Findings - NOT Mentioned:**
- von Mises-Fisher: Not mentioned in the provided content
- TruthfulQA MC1 specific results: Not detailed (only generic "+10%" improvement noted)
- Per-token vs per-sequence operation: Not discussed in available excerpt
- ICML acceptance: Not mentioned

**Key Findings - Present:**
- Confidence gate: Confirmed as incorporated feature
- Code availability: "The code is at: [this https URL]" linking to https://github.com/chili-lab/Spherical-Steering

**License:**
CC-BY-NC-SA 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24580706-8766-40d4-bb9b-020f90ec459c",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "37297522-b837-47fd-b8e1-386689619597",
  "sourceToolAssistantUUID": "24580706-8766-40d4-bb9b-020f90ec459c",
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

_source line 13 · 2026-05-16T08:45:51.562Z_

<details><summary>↩ Tool result · `toolu_01R3b5Nf8K72Aw6dDcpR9kjz`</summary>

```text
# Spherical Steering Repository Analysis

## Repository Overview
This is a GitHub repository for "Spherical Steering: Geometry-Aware Activation Rotation for Language Models," an ICML 2026 paper by the chili-lab group.

## Available Code
The repository contains Python scripts for:
- **get_activations.py**: Extracts last-token hidden states from answer pairs
- **get_prototypes.py**: Computes steering targets with question-level splits
- **evaluate_mc.py**: Multiple-choice evaluation (MC1/MC2/MC3 metrics)
- **evaluate_llm_judge.py**: Open-ended generation with truth/information scoring
- **spherical_steering.py**: Core steering logic with geometric intervention hooks
- **utils.py**: Data loading and activation extraction utilities

Additionally, quickstart scripts are provided for Llama3.1-8B-Instruct and Qwen2.5-7B-Instruct models.

## README Summary
The methodology treats steering as "a directional update in representation space" by rotating activations along a geodesic toward target directions while preserving magnitudes.

## Information Not Present
The provided content does **not** mention:
- Von Mises-Fisher confidence gates
- Specific TruthfulQA MC1 benchmark results
- Whether operations are per-token or per-sequence
- ICML 2026 acceptance confirmation (though the header suggests acceptance)

## Environment & Dependencies
Python 3.10 with dependencies specified in environment.yml. The codebase uses TruthfulQA benchmark data and acknowledges baukit, TruthfulQA, and ITI projects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2e87e44-0e53-492d-9d20-8f2c33e9bed2",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "2f632cca-9cc9-4b06-8bd0-1661c70a2d53",
  "sourceToolAssistantUUID": "c2e87e44-0e53-492d-9d20-8f2c33e9bed2",
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

_source line 14 · 2026-05-16T08:45:54.397Z_

Let me search for more specific details about the von Mises-Fisher distribution connection and the per-token vs per-sequence question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f632cca-9cc9-4b06-8bd0-1661c70a2d53",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xMa6Hp3dTB5o97MkYg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0748aa6c-1099-4400-bbd3-6f0e3d17ccbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjwrQ41cdE2Vf2trTwjxLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 11840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1694,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 15 · 2026-05-16T08:45:54.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UnRghaqKHtoGgznjs8ESiY`</summary>

```json
{
  "query": "\"Spherical Steering\" \"von Mises-Fisher\" confidence gate language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0748aa6c-1099-4400-bbd3-6f0e3d17ccbc",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xMa6Hp3dTB5o97MkYg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a46a1221-c1a2-4f9d-8646-9711d43b591b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjwrQ41cdE2Vf2trTwjxLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 11840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1694,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-16T08:45:55.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LtZsYGotz5bjeXLcKJFrKR`</summary>

```json
{
  "query": "\"Spherical Steering\" TruthfulQA MC1 results percentage improvement 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a46a1221-c1a2-4f9d-8646-9711d43b591b",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xMa6Hp3dTB5o97MkYg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "921b0f88-2eeb-4e25-a37f-f7e68b530003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjwrQ41cdE2Vf2trTwjxLt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 11840,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 11840,
          "cache_creation_input_tokens": 1694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1694,
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

_source line 17 · 2026-05-16T08:45:59.728Z_

<details><summary>↩ Tool result · `toolu_01LtZsYGotz5bjeXLcKJFrKR`</summary>

```text
Web search results for query: ""Spherical Steering" TruthfulQA MC1 results percentage improvement 2026"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"Steering off Course: Reliability Challenges in Steering Language Models","url":"https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1744632039595936&disposition=inline"},{"title":"MSRS: Adaptive Multi-Subspace Representation Steering for Attribute Alignment in Large Language Models","url":"https://arxiv.org/html/2508.10599"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"}]

Based on the search results, I found relevant information about Spherical Steering and its TruthfulQA MC1 results:

Spherical Steering significantly outperforms addition-based baselines by +10% on TruthfulQA. This represents the percentage improvement for the method on the TruthfulQA MC1 benchmark.

The research paper on Spherical Steering was published in February 2026 and demonstrates that Spherical Steering achieves the best multiple-choice performance while simultaneously maintaining or improving generation quality—a Pareto improvement over all baselines. The method was specifically designed as a technique that rotates activations along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of the signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "921b0f88-2eeb-4e25-a37f-f7e68b530003",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "83062d9d-e81b-4f2c-992c-dc0caae036d6",
  "sourceToolAssistantUUID": "921b0f88-2eeb-4e25-a37f-f7e68b530003",
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

_source line 18 · 2026-05-16T08:46:01.499Z_

<details><summary>↩ Tool result · `toolu_01UnRghaqKHtoGgznjs8ESiY`</summary>

```text
Web search results for query: ""Spherical Steering" "von Mises-Fisher" confidence gate language model"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/pdf/2503.02863"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"von Mises–Fisher distribution - Wikipedia","url":"https://en.wikipedia.org/wiki/Von_Mises%E2%80%93Fisher_distribution"},{"title":"NeurIPS Poster SteerConf: Steering LLMs for Confidence Elicitation","url":"https://neurips.cc/virtual/2025/poster/119826"},{"title":"(PDF) Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://www.researchgate.net/publication/401057888_Understanding_Unreliability_of_Steering_Vectors_in_Language_Models_Geometric_Predictors_and_the_Limits_of_Linear_Approximations"},{"title":"Von Mises-Fisher Clustering Models Siddharth Gopal SGOPAL1@CS.CMU.EDU","url":"https://www.cs.cmu.edu/~sgopal1/papers/ICML14.pdf"},{"title":"A Collection of Functions for Directional Data Analysis - CRAN","url":"https://cran.r-project.org/web/packages/Directional/Directional.pdf"}]

I found relevant information about your search query. Here's what the results show:

## Spherical Steering Overview

Spherical Steering is a training-free primitive that resolves the trade-off between steering and open-ended generation through activation rotation, which rotates activations along a geodesic toward a target direction rather than shifting them with a fixed vector.

## Von Mises-Fisher Confidence Gate

The method uses a von Mises-Fisher (vMF)-based confidence gate that dynamically modulates steering strength based on input uncertainty. The vMF confidence gate maps the alignment-derived score to determine steering behavior.

## Key Results

Extensive experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.

## Technical Details

The approach includes controllable parameters: the overall intervention is primarily controlled by β, which sets the selection boundary, and α, which controls the rotation strength, and tuning involves choosing a permissive threshold and moderate steering strength to identify promising layers.

This work was published at ICML 2026 and includes implementations available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a46a1221-c1a2-4f9d-8646-9711d43b591b",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "a1569670-a19a-4cf8-aba0-081e69e914d8",
  "sourceToolAssistantUUID": "a46a1221-c1a2-4f9d-8646-9711d43b591b",
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

_source line 19 · 2026-05-16T08:46:04.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UX9sH75hE2aiMHZY7spULm`</summary>

```json
{
  "query": "\"Spherical Steering\" per-token per-sequence \"last token\" activation intervention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1569670-a19a-4cf8-aba0-081e69e914d8",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xNJZvPYZDBN2ho76Km",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90ea7ffe-d0a6-4b4b-8257-876eded819b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jdf7EStjuou6pCbpUdBWk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 800,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 13534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1064,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 20 · 2026-05-16T08:46:07.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y9LGt5mGUPzVHe9Lx3Lo2p`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08169v1",
  "prompt": "I need very specific details: 1) Does the paper use a \"von Mises-Fisher confidence gate\"? What exactly is the confidence gate mechanism? 2) What are the exact TruthfulQA MC1 percentage improvements reported (specific numbers, not just +10%)? 3) Does the method operate per-token or per-sequence? How are activations extracted - last token only or all tokens? 4) Is ICML 2026 acceptance mentioned? 5) Any specific MC1 accuracy numbers in tables?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ea7ffe-d0a6-4b4b-8257-876eded819b4",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xNJZvPYZDBN2ho76Km",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d203b218-6e4f-41c3-b3c9-19f467e616ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jdf7EStjuou6pCbpUdBWk2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 800,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 13534,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1064
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 800,
          "output_tokens": 254,
          "cache_read_input_tokens": 13534,
          "cache_creation_input_tokens": 1064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1064,
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

_source line 21 · 2026-05-16T08:46:11.621Z_

<details><summary>↩ Tool result · `toolu_01UX9sH75hE2aiMHZY7spULm`</summary>

```text
Web search results for query: ""Spherical Steering" per-token per-sequence "last token" activation intervention"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907"},{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/html/2512.24143v2"},{"title":"The Development of Activation Steering","url":"https://sidn.baulab.info/steering/"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Vector Steering Intervention in Neural Models","url":"https://www.emergentmind.com/topics/vector-steering-intervention"}]

Based on the search results, here's what I found about Spherical Steering and activation intervention approaches:

## Spherical Steering Overview

Spherical Steering is an inference-time activation steering method for controlling language models via geometry-consistent interventions. Rather than shifting activations with a fixed vector, the method rotates them along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of the signal.

## Key Technical Approach

Spherical Steering is a training-free primitive that resolves the activation addition trade-off through activation rotation, rotating activations along a geodesic toward a target direction while preserving signal integrity. To further enhance adaptivity, it incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.

## Performance Results

Extensive experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality. Spherical Steering achieves the best multiple-choice performance while simultaneously maintaining or improving generation quality—a Pareto improvement over all baselines.

## Relationship to Per-Token and Last-Token Interventions

Analysis includes the mean ℓ2 norm of last-token activations at each residual layer for correct vs. incorrect answers. The research also addresses how different layers may prefer different intervention rates and strengths through per-layer tuning of parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90ea7ffe-d0a6-4b4b-8257-876eded819b4",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "c500765f-4534-4176-ba2b-d1cddc21812e",
  "sourceToolAssistantUUID": "90ea7ffe-d0a6-4b4b-8257-876eded819b4",
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

_source line 22 · 2026-05-16T08:46:14.102Z_

<details><summary>↩ Tool result · `toolu_01Y9LGt5mGUPzVHe9Lx3Lo2p`</summary>

```text
# Spherical Steering: Technical Details

## 1. Von Mises-Fisher Confidence Gate

Yes, the paper employs a vMF-based confidence gate. The mechanism works as follows:

The gate computes alignment scores between the current activation direction and both truthful/hallucinated directions using cosine similarity. These scores feed into vMF-induced exponential terms: "f(u;m,κ)∝exp(κ m⊤u)" normalized via softmax to produce probabilities pT and pH. The difference δ=pH−pT∈[−1,1] maps to intervention strength t∈[0,1] through a thresholded rule controlled by three hyperparameters (α, β, κ).

## 2. TruthfulQA MC1 Improvements

Specific percentage improvements reported in Table 1:
- **LLaMA-3.1-8B-Instruct**: 34.15% (baseline) → 49.95% (Spherical Steering) = **+15.8 percentage points**
- **Qwen-2.5-7B-Instruct**: 35.87% (baseline) → 48.71% (Spherical Steering) = **+12.84 percentage points**

## 3. Per-Token vs Per-Sequence Operation

The method operates **per-token during generation**. Activations are extracted at the last token position: "we extract the layer-l activation of the last token" during offline prototype construction, but at inference, the steering applies to each decoding step j where rotations occur token-by-token based on current activations.

## 4. Conference/Venue

The document is an arXiv preprint (arXiv:2602.08169v1). **No ICML 2026 acceptance is mentioned**.

## 5. Additional MC1 Numbers

Table 2 provides zero-shot results across six benchmarks on LLaMA-3.1-8B showing Spherical Steering achieves 49.95% on TruthfulQA MC1 with average improvement of +8.06 points across all benchmarks tested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d203b218-6e4f-41c3-b3c9-19f467e616ef",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "add766dc6f6f2b147",
  "type": "user",
  "uuid": "9b78235c-2470-4a32-9f99-f867e60e043a",
  "sourceToolAssistantUUID": "d203b218-6e4f-41c3-b3c9-19f467e616ef",
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

_source line 23 · 2026-05-16T08:46:35.967Z_

Now I have comprehensive information. Let me compile the findings.

Based on my research, here is a detailed verification of each claim about "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" (arXiv 2602.08169):

---

## 1. Does the paper exist?

**Yes, it exists.** It is a real paper on arXiv (2602.08169), submitted February 9, 2026, by Zejia You, Chunyuan Deng, and Hanjie Chen. The paper proposes a training-free inference-time steering method that rotates activations along a geodesic toward a target direction (rather than using standard activation addition), preserving representation magnitude while steering model behavior.

---

## 2. Does it use a "von Mises-Fisher confidence gate" that "dynamically modulates steering strength based on input uncertainty"?

**Yes, confirmed.** The paper employs a vMF-based confidence gate. The mechanism computes alignment scores between the current activation direction and both truthful/hallucinated prototype directions using cosine similarity. These scores are fed into vMF-induced exponential terms (f(u;m,kappa) proportional to exp(kappa * m^T * u)), normalized via softmax to produce probabilities pT and pH. The difference delta = pH - pT maps to intervention strength t in [0,1] through a thresholded rule controlled by hyperparameters alpha, beta, and kappa. So the claim about "dynamically modulating steering strength based on input uncertainty" is accurate.

---

## 3. TruthfulQA MC1 results?

The paper reports specific MC1 improvements:
- **LLaMA-3.1-8B-Instruct**: 34.15% (baseline) to 49.95% (Spherical Steering) = **+15.8 percentage points**
- **Qwen-2.5-7B-Instruct**: 35.87% (baseline) to 48.71% (Spherical Steering) = **+12.84 percentage points**

The general claim of "+10% on TruthfulQA" in the abstract appears to be a rounded/conservative figure; actual improvements are larger (12-16 percentage points on MC1). The average improvement across all six benchmarks tested is +8.06 points.

---

## 4. Per-token or per-sequence?

**Per-token during generation.** Prototypes are constructed using last-token activations extracted offline, but at inference time, the steering rotation is applied at each decoding step (token-by-token) based on the current activations. So it operates per-token.

---

## 5. Is it accepted at ICML 2026?

**Evidence is mixed but leans toward yes.** The arXiv paper itself does not explicitly state ICML 2026 acceptance (it is posted as a preprint). However, the GitHub repository (github.com/chili-lab/Spherical-Steering) has "[ICML 2026]" in its title/description, and search results consistently reference it as an ICML 2026 paper. This is consistent with papers that receive acceptance after the preprint is posted and update their repo but not the arXiv abstract immediately.

---

## 6. Does it have released code?

**Yes.** Code is available at: https://github.com/chili-lab/Spherical-Steering

The repository contains:
- `spherical_steering.py` - Core steering logic with geometric intervention hooks
- `get_activations.py` - Extracts last-token hidden states from answer pairs
- `get_prototypes.py` - Computes steering targets with question-level splits
- `evaluate_mc.py` - Multiple-choice evaluation (MC1/MC2/MC3 metrics)
- `evaluate_llm_judge.py` - Open-ended generation with truth/information scoring
- `utils.py` - Data loading and activation extraction utilities
- Quickstart scripts for Llama3.1-8B-Instruct and Qwen2.5-7B-Instruct

License: CC-BY-NC-SA 4.0, Python 3.10, dependencies in environment.yml.

---

## Summary

All major claims check out as real. The paper exists, uses a vMF confidence gate, achieves substantial TruthfulQA MC1 improvements (+12-16 percentage points), operates per-token at inference, appears accepted at ICML 2026 (per GitHub repo tagging), and has publicly released code.

Sources:
- [arXiv:2602.08169 Abstract](https://arxiv.org/abs/2602.08169)
- [arXiv:2602.08169 HTML](https://arxiv.org/html/2602.08169v1)
- [GitHub: chili-lab/Spherical-Steering](https://github.com/chili-lab/Spherical-Steering)
- [ResearchGate Publication](https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b78235c-2470-4a32-9f99-f867e60e043a",
  "isSidechain": true,
  "agentId": "add766dc6f6f2b147",
  "requestId": "req_011Cb5xPETu6gM1AHUWGcdG9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1af4bbff-546a-4534-8f65-3a24cafa1f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFdmUdvKpHExLgdJSgxqmU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 14598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2429,
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
