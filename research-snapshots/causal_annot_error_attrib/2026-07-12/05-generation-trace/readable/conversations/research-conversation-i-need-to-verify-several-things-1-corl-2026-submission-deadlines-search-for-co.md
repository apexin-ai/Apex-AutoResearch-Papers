# Research conversation: I need to verify several things: 1. CoRL 2026 submission deadlines. Search for "CoRL 2026 deadline", "CoRL 2026 call for

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8598031bd959b33e.jsonl`
- **Structured JSON:** [`67f2792afaa9e6a1be00.json`](../../sessions/67/67f2792afaa9e6a1be00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-14T05:33:02.228Z_

I need to verify several things:

1. CoRL 2026 submission deadlines. Search for "CoRL 2026 deadline", "CoRL 2026 call for papers", "Conference on Robot Learning 2026". The idea claims abstract deadline May 25 and paper deadline May 28 AoE.

2. OpenVLA-OFT paper and its LIBERO performance. Search for "OpenVLA-OFT" (arXiv 2502.19645) - verify it exists and check if it really achieves 97.1% on LIBERO.

3. Also check: "Generalized Information Bottleneck" paper (arXiv 2509.26327, 2025) - does this exist? Note the arXiv ID format "2509.26327" would mean September 2025.

4. FOMA (First-Order Manifold Data Augmentation) at ICML 2024 - verify existence.

5. DRIBO (Robust Deep RL via Multi-View Information Bottleneck) at ICML 2022 - verify existence.

Report all findings with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "c08859be-5720-4c83-8f70-7cd5dcb48aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T05:33:02.233Z_

```json
{
  "parentUuid": "c08859be-5720-4c83-8f70-7cd5dcb48aeb",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
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
  "uuid": "6cd6725a-b380-4637-9b61-9f54646fc374",
  "timestamp": "2026-05-14T05:33:02.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-14T05:33:04.773Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VZntV7ShPGbAG775q2Aymr`</summary>

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
  "parentUuid": "6cd6725a-b380-4637-9b61-9f54646fc374",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v2v91zJgWAJupYYnRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33944ab5-9fad-4a52-9b0b-6682a09bcbfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnSVMKcCFSQWYYs7mg8Gej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 807,
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

_source line 4 · 2026-05-14T05:33:04.776Z_

<details><summary>↩ Tool result · `toolu_01VZntV7ShPGbAG775q2Aymr`</summary>

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
  "parentUuid": "33944ab5-9fad-4a52-9b0b-6682a09bcbfe",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "9ab63009-3069-48c7-bb07-d17719a82e03",
  "sourceToolAssistantUUID": "33944ab5-9fad-4a52-9b0b-6682a09bcbfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:33:08.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FvqJXja88s2Qn2mtRGvS3G`</summary>

```json
{
  "query": "CoRL 2026 deadline call for papers \"Conference on Robot Learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ab63009-3069-48c7-bb07-d17719a82e03",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v378ZqVTKW4QLSBvSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8354aa95-26c9-4186-9324-b9b97b44e02e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGiNUBjQx73BBBQyPkqL5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 6 · 2026-05-14T05:33:08.665Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019HXymemHUgTWuN3W9VFTJa`</summary>

```json
{
  "query": "OpenVLA-OFT arXiv 2502.19645 LIBERO performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8354aa95-26c9-4186-9324-b9b97b44e02e",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v378ZqVTKW4QLSBvSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1c978ea-09b8-494f-8db6-f0d9307adfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGiNUBjQx73BBBQyPkqL5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 7 · 2026-05-14T05:33:09.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019BrfPmvmbdf1vcG5gta1Pm`</summary>

```json
{
  "query": "\"Generalized Information Bottleneck\" arXiv 2509.26327"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1c978ea-09b8-494f-8db6-f0d9307adfd1",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v378ZqVTKW4QLSBvSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcf2ded2-c762-4b2a-9cde-197815370c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGiNUBjQx73BBBQyPkqL5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 8 · 2026-05-14T05:33:09.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jk5bZcmfERHv8nvYMTpWJN`</summary>

```json
{
  "query": "FOMA \"First-Order Manifold Data Augmentation\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcf2ded2-c762-4b2a-9cde-197815370c90",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v378ZqVTKW4QLSBvSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f362a64-73cc-4e80-822b-e716fe5e5644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGiNUBjQx73BBBQyPkqL5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 9 · 2026-05-14T05:33:09.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012w6K7Ls7DMtCtuSeEZDE73`</summary>

```json
{
  "query": "DRIBO \"Robust Deep Reinforcement Learning via Multi-View Information Bottleneck\" ICML 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f362a64-73cc-4e80-822b-e716fe5e5644",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v378ZqVTKW4QLSBvSG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20b0f961-fe42-407a-b54a-b1cb3749732e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGiNUBjQx73BBBQyPkqL5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9030,
      "output_tokens": 292,
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
          "output_tokens": 292,
          "cache_read_input_tokens": 9030,
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

_source line 10 · 2026-05-14T05:33:13.994Z_

<details><summary>↩ Tool result · `toolu_01FvqJXja88s2Qn2mtRGvS3G`</summary>

```text
Web search results for query: "CoRL 2026 deadline call for papers "Conference on Robot Learning""

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"Conference on Robot Learning (@corl_conf) · X","url":"https://twitter.com/corl_conf"},{"title":"CoRL 2023","url":"https://www.corl2023.org/"}]

Based on the search results, here's the information about the CoRL 2026 call for papers:

**Conference Details:**
CoRL 2026 will be held in Austin, Texas, US, and the conference dates are November 9-12, 2026.

**Submission Deadlines:**
The abstract submission deadline is May 26, 2026 11:59 UTC and the paper submission deadline is May 29, 2026 11:59 UTC. (Note: One source indicates the paper deadline as May 28 EOD, so you may want to verify the exact deadline on the official site.)

**About the Conference:**
The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning.

**Submission Topics:**
CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models, imitation learning, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.

**Submission Requirements:**
Papers may be submitted through OpenReview, and submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.

For more details, visit the official CoRL 2026 website at https://www.corl.org/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8354aa95-26c9-4186-9324-b9b97b44e02e",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "dcec5a9c-b56e-4344-8618-b765983b90a6",
  "sourceToolAssistantUUID": "8354aa95-26c9-4186-9324-b9b97b44e02e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T05:33:14.219Z_

<details><summary>↩ Tool result · `toolu_019HXymemHUgTWuN3W9VFTJa`</summary>

```text
Web search results for query: "OpenVLA-OFT arXiv 2502.19645 LIBERO performance"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"}]

Based on the search results, here is information about OpenVLA-OFT's performance on LIBERO:

## LIBERO Performance

OpenVLA-OFT achieves a state-of-the-art average success rate of 97.1% across four LIBERO task suites, significantly improving over the original OpenVLA's 76.5%. 

The evaluation covers four task suites—LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long—each providing 500 expert demonstrations across 10 tasks to assess policy generalization to different spatial layouts, objects, goals, and long-horizon tasks.

### Method Details

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective. Parallel decoding and action chunking not only increase throughput but also improve performance significantly, raising average success rates by 14% (absolute) over autoregressive OpenVLA policies, with this improvement particularly pronounced in LIBERO-Long.

### Efficiency Gains

OpenVLA-OFT also increases action generation throughput by 26×, and achieves 26× speedup, reaching 109.7 Hz with 8-step action chunks while maintaining low latency of 0.0729 seconds per action chunk.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1c978ea-09b8-494f-8db6-f0d9307adfd1",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "05ad1124-c4ea-41bc-a779-fc6e49d18c88",
  "sourceToolAssistantUUID": "e1c978ea-09b8-494f-8db6-f0d9307adfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T05:33:15.515Z_

<details><summary>↩ Tool result · `toolu_019BrfPmvmbdf1vcG5gta1Pm`</summary>

```text
Web search results for query: ""Generalized Information Bottleneck" arXiv 2509.26327"

Links: [{"title":"[2509.26327] A Generalized Information Bottleneck Theory of Deep Learning","url":"https://arxiv.org/abs/2509.26327"},{"title":"A GENERALIZED INFORMATION BOTTLENECK THEORY OF DEEP LEARNING","url":"https://arxiv.org/pdf/2509.26327"},{"title":"(PDF) A Generalized Information Bottleneck Theory of Deep Learning","url":"https://www.researchgate.net/publication/396049012_A_Generalized_Information_Bottleneck_Theory_of_Deep_Learning"},{"title":"A Generalized Information Bottleneck Theory of Deep Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250926327W/abstract"},{"title":"Information Theory Sep 2025","url":"https://arxiv.org/list/cs.IT/2025-09?skip=300&show=1000"},{"title":"Generalization or Memorization: Dynamic Decoding for Mode Steering","url":"https://arxiv.org/html/2510.22099v1"},{"title":"Generalized Information Bottleneck","url":"https://ecommons.cornell.edu/entities/publication/f148b88c-ae81-483b-b384-1fb5c0729c74"},{"title":"Information bottleneck method - Wikipedia","url":"https://en.wikipedia.org/wiki/Information_bottleneck_method"},{"title":"[2303.17762] Generalized Information Bottleneck for Gaussian Variables","url":"https://arxiv.org/abs/2303.17762"},{"title":"A Generalized Information Bottleneck Method: A Decision-Theoretic Perspective This work was supported by JSPS KAKENHI Grant Number JP23K16886 and JST CRONOS Grant Number JPMJCS25N5.","url":"https://arxiv.org/html/2602.18405"}]

Based on the search results, here's information about arXiv paper 2509.26327 on "Generalized Information Bottleneck":

## Overview

The Information Bottleneck (IB) principle offers a compelling theoretical framework to understand how neural networks learn, though its practical utility has been constrained by unresolved theoretical ambiguities and significant challenges in accurate estimation.

## Main Contribution

The paper presents a Generalized Information Bottleneck (GIB) framework that reformulates the original IB principle through the lens of synergy, which is the information obtainable only through joint processing of features.

## Key Findings

Theoretical and empirical evidence demonstrate that synergistic functions achieve superior generalization compared to their non-synergistic counterparts. The IB is reformulated using a computable definition of synergy based on the average interaction information (II) of each feature with those remaining.

## Authors and Details

The paper was submitted on September 30, 2025 (v1) and last revised on January 30, 2026 (v3), with authors Charles Westphal, Stephen Hailes, and Mirco Musolesi.

The paper addresses fundamental limitations of the original Information Bottleneck framework and provides both theoretical and empirical evidence for why deep networks benefit from learning synergistic representations rather than processing features independently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcf2ded2-c762-4b2a-9cde-197815370c90",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "dd748143-d63f-4e4b-9938-3dd774a9a316",
  "sourceToolAssistantUUID": "fcf2ded2-c762-4b2a-9cde-197815370c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T05:33:15.958Z_

<details><summary>↩ Tool result · `toolu_01Jk5bZcmfERHv8nvYMTpWJN`</summary>

```text
Web search results for query: "FOMA "First-Order Manifold Data Augmentation" ICML 2024"

Links: [{"title":"Curvature Enhanced Data Augmentation for Regression","url":"https://bibliography.icpsr.umich.edu/bibliography/citations/data/181268/fileDownload"},{"title":"First-Order Manifold Data Augmentation for Regression Learning","url":"https://proceedings.mlr.press/v235/kaufman24a.html"},{"title":"ICML Poster First-Order Manifold Data Augmentation for Regression Learning","url":"https://icml.cc/virtual/2024/poster/33419"},{"title":"First-Order Manifold Data Augmentation for Regression Learning","url":"https://arxiv.org/html/2406.10914"},{"title":"[2406.10914] First-Order Manifold Data Augmentation for Regression Learning","url":"https://arxiv.org/abs/2406.10914"},{"title":"Curvature Enhanced Data Augmentation for Regression","url":"https://arxiv.org/html/2506.06853"},{"title":"Data Augmentation Policy Search for Long-Term Forecasting","url":"https://arxiv.org/pdf/2405.00319"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"GitHub - azencot-group/CEMS: Curvature Emhanced Manifold Sampling","url":"https://github.com/azencot-group/CEMS"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"}]

Based on the search results, I found comprehensive information about FOMA (First-Order Manifold Data Augmentation) at ICML 2024:

## Overview

FOMA is a new data-driven domain-independent data augmentation method for regression. The approach samples new examples from the tangent planes of the train distribution.

## Key Details

**Authors and Publication:** The work is by Ilya Kaufman and Omri Azencot, published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 23324-23342.

**Motivation:** While regularizing classification tasks via data augmentation is a well-explored research topic, the effect of DA on regression problems received less attention.

**How It Works:** Augmenting data in this way aligns with the network tendency towards capturing the dominant features of its input signals.

**Results:** FOMA improves the generalization of several neural architectures on in-distribution generalization and out-of-distribution robustness benchmarks, and strong baselines based on mixup are less effective in comparison to this approach.

**Availability:** The code is publicly available at https://github.com/azencot-group/FOMA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f362a64-73cc-4e80-822b-e716fe5e5644",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "c3f12b6f-07eb-4567-b325-b67bbddfdf49",
  "sourceToolAssistantUUID": "5f362a64-73cc-4e80-822b-e716fe5e5644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:33:16.706Z_

<details><summary>↩ Tool result · `toolu_012w6K7Ls7DMtCtuSeEZDE73`</summary>

```text
Web search results for query: "DRIBO "Robust Deep Reinforcement Learning via Multi-View Information Bottleneck" ICML 2022"

Links: [{"title":"ICML Poster DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://icml.cc/virtual/2022/poster/16441"},{"title":"[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://arxiv.org/abs/2102.13268"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"},{"title":"GitHub - JmfanBU/DRIBO: DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://github.com/JmfanBU/DRIBO"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=Py8WbvKH_wv"},{"title":"dblp: Jiameng Fan","url":"https://dblp.org/pid/196/7836.html"},{"title":"Home | jiamengf","url":"https://www.jiamengf.com"},{"title":"(PDF) Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://www.researchgate.net/publication/349682874_Robust_Deep_Reinforcement_Learning_via_Multi-View_Information_Bottleneck"},{"title":"Track: MISC: Representation Learning/Causality","url":"https://icml.cc/virtual/2022/session/20088"},{"title":"Robust cooperative multi-agent reinforcement learning via multi-view message certification | Science China Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11432-023-3853-y"}]

I found comprehensive information about the DRIBO paper. Here's a summary of the search results:

## DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck

DRIBO was published at ICML 2022, authored by Jiameng Fan and Wenchao Li.

### Overview
The paper addresses the problem that deep reinforcement learning agents are often sensitive to visual changes unseen in their training environments, and proposes leveraging the sequential nature of RL to learn robust representations that encode only task-relevant information.

### Key Contribution
The work introduces a novel contrastive version of the Multi-View Information Bottleneck (MIB) objective for temporal data. The approach trains RL agents from pixels with this auxiliary objective to learn robust representations that can compress away task-irrelevant information and are predictive of task-relevant dynamics, enabling high-performance policies that are robust to visual distractions and can generalize well to unseen environments.

### Results
The approach achieves state-of-the-art performance on diverse visual control tasks on the DeepMind Control Suite when the background is replaced with natural videos.

### Resources
- **Official Implementation**: Available on GitHub as the official implementation, based on CURL by Misha Laskin and SAC+AE by Denis Yarats
- **Paper Access**: Available on arXiv and through the ICML proceedings


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20b0f961-fe42-407a-b54a-b1cb3749732e",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "51122848-3052-4410-ad66-81536371bb5e",
  "sourceToolAssistantUUID": "20b0f961-fe42-407a-b54a-b1cb3749732e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T05:33:19.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0139SdyzdDxmuZDJXZ6vT1sJ`</summary>

```json
{
  "query": "CoRL 2026 submission deadline exact date May 2026",
  "allowed_domains": [
    "corl.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51122848-3052-4410-ad66-81536371bb5e",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v3yw147cVg97xsVKpG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f427ab-e19d-4472-8e2c-8f5d97bf8717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Bmj7N4rZSgbEKaamdsrYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4327,
      "cache_read_input_tokens": 10422,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4327
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 10422,
          "cache_creation_input_tokens": 4327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4327,
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

_source line 16 · 2026-05-14T05:33:22.252Z_

<details><summary>↩ Tool result · `toolu_0139SdyzdDxmuZDJXZ6vT1sJ`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline exact date May 2026"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"CoRL 2026 - CoRL History","url":"https://www.corl.org/about-corl/corl-history"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"CoRL 2024","url":"https://2024.corl.org/home"}]

Based on the search results, the submission deadline for CoRL 2026 is May 28, 2026 (AoE - Anywhere on Earth).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08f427ab-e19d-4472-8e2c-8f5d97bf8717",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "a6a2deda-ab00-41f6-87db-7db64102349c",
  "sourceToolAssistantUUID": "08f427ab-e19d-4472-8e2c-8f5d97bf8717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T05:33:25.818Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018qVuB5PidoggxbLStMoWcg`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a2deda-ab00-41f6-87db-7db64102349c",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v4PfWUMnPYc7caYmMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e7f6072-1ea0-44dc-8caa-c5f171152f38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6Wok4wqqmPqCfqQupJDpR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 14749,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 14749,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 479,
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

_source line 18 · 2026-05-14T05:33:25.820Z_

<details><summary>↩ Tool result · `toolu_018qVuB5PidoggxbLStMoWcg`</summary>

````text
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
  "parentUuid": "9e7f6072-1ea0-44dc-8caa-c5f171152f38",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "956cb569-3576-418e-9ee9-154fc63e689b",
  "sourceToolAssistantUUID": "9e7f6072-1ea0-44dc-8caa-c5f171152f38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:33:29.711Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016BLW3KNdbi8fQaMyCevKL9`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "What are the exact submission deadlines (abstract deadline and paper deadline) for CoRL 2026? Include exact dates and timezone information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "956cb569-3576-418e-9ee9-154fc63e689b",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v4fAfqBsh1pn2Y8NgA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc4412ba-e737-4487-8f3b-fdb312b98685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013edykLg7UTQ2mB4NZkL6sm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15228,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 15228,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 595,
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

_source line 20 · 2026-05-14T05:33:33.096Z_

<details><summary>↩ Tool result · `toolu_016BLW3KNdbi8fQaMyCevKL9`</summary>

```text
Based on the webpage content provided, the exact submission deadlines for CoRL 2026 are not specified on this page. 

The Call for Papers section states: "For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)"

To find the specific abstract and paper submission deadlines with timezone information, you would need to visit the Instruction for Authors page, which is referenced but not included in the content provided here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc4412ba-e737-4487-8f3b-fdb312b98685",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "41b3cfcc-b0fb-420f-a89c-c93a83748d62",
  "sourceToolAssistantUUID": "bc4412ba-e737-4487-8f3b-fdb312b98685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:33:36.268Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YANvgBsbRfaxVCuzFZq7W9`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "What are the exact submission deadlines (abstract deadline and paper deadline) for CoRL 2026? Include exact dates and timezone information (AoE, UTC, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41b3cfcc-b0fb-420f-a89c-c93a83748d62",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v5C14Zgy1EDfB22N9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67bda314-0f91-4992-9dc9-e1583070a550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiUXChnVQ8Q5U8mYFWrdvE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 15823,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 15823,
          "cache_creation_input_tokens": 223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 223,
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

_source line 22 · 2026-05-14T05:33:38.962Z_

<details><summary>↩ Tool result · `toolu_01YANvgBsbRfaxVCuzFZq7W9`</summary>

```text
I've reviewed the provided content, but it does not contain the specific abstract and paper submission deadlines with exact dates and timezone information for CoRL 2026.

The page mentions "Key Dates" as a section heading and notes that "the paper submission deadline is Thursday (5/28) EOD rather than Friday," but the actual detailed deadline table or list with complete dates and timezone specifications is not included in the content you provided.

To obtain the exact submission deadlines, you would need to visit the full CoRL 2026 website or contact the organizing committee directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67bda314-0f91-4992-9dc9-e1583070a550",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "fba2dc14-217a-4d18-816e-031d863123cf",
  "sourceToolAssistantUUID": "67bda314-0f91-4992-9dc9-e1583070a550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T05:33:41.904Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FzcD9jr8jJr3XkJMdQcDvF`</summary>

```json
{
  "url": "https://www.corl.org/",
  "prompt": "What are the exact submission deadlines listed on the CoRL 2026 homepage? Include any mention of abstract deadline, paper deadline, with exact dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba2dc14-217a-4d18-816e-031d863123cf",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v5d4hG2CAo6qAmh1JR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e49c51ea-a546-4c8c-88ab-5ff889901643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jKZXzyeN3CDHfqQosDbD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 16046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 251,
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

### Tool result

_source line 24 · 2026-05-14T05:33:44.299Z_

<details><summary>↩ Tool result · `toolu_01FzcD9jr8jJr3XkJMdQcDvF`</summary>

```text
Based on the webpage content provided, **no specific submission deadlines are listed**. 

The page mentions that "The [Call for Papers](/contributions/call-for-papers) and [key dates](/home) are now available" as of January 25, but the actual deadline dates are not included in this excerpt. To find the exact submission deadlines for abstracts and papers, you would need to visit the full "Call for Papers" or "Key Dates" pages referenced on the site.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e49c51ea-a546-4c8c-88ab-5ff889901643",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "4f67beef-8ca7-4df2-b0e6-73e760e45464",
  "sourceToolAssistantUUID": "e49c51ea-a546-4c8c-88ab-5ff889901643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T05:33:47.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgqVboj9VAY7PZJAK9Jco7`</summary>

```json
{
  "query": "CoRL 2026 abstract deadline \"May 25\" OR \"May 26\" paper deadline \"May 28\" OR \"May 29\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f67beef-8ca7-4df2-b0e6-73e760e45464",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v61xr6n2LL2Kuks46E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "572e7923-2be9-49da-aaee-8c45f12a523e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWFRwR628W9DvBEnhiYKXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 16297,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 16297,
          "cache_creation_input_tokens": 223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 223,
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

_source line 26 · 2026-05-14T05:33:52.538Z_

<details><summary>↩ Tool result · `toolu_01RgqVboj9VAY7PZJAK9Jco7`</summary>

```text
Web search results for query: "CoRL 2026 abstract deadline "May 25" OR "May 26" paper deadline "May 28" OR "May 29""

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"AI Conference Deadlines","url":"https://mldeadlines.com/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, here's what I found regarding CoRL 2026 deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC. However, the official CoRL website notes that the paper submission deadline is Thursday (5/28) EOD rather than Friday.

There appears to be a discrepancy in the sources. Some sources list May 29 as the deadline, while the official CoRL instructions page indicates May 28. According to the CoRL social media announcement, the dates are May 25 for Abstract Submission and May 28 for Full Paper Submission.

The conference will be held November 9-12, 2026 in Austin, Texas, USA, with a paper deadline of May 28, 2026 (AoE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "572e7923-2be9-49da-aaee-8c45f12a523e",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "740d080f-26f8-47b9-9e31-677ed08b5939",
  "sourceToolAssistantUUID": "572e7923-2be9-49da-aaee-8c45f12a523e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T05:33:56.260Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ExCMPLDuMdQ86euPdQzfGg`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "What are the exact CoRL 2026 deadlines listed in this commit? Include abstract deadline and paper deadline with exact dates and timezone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "740d080f-26f8-47b9-9e31-677ed08b5939",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v6d8wK2whrv8b73Q3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3740536-4ac4-4bad-bdad-f636052fbd5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eKTQpv25qbKrjtruagp7L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 16520,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 16520,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 773,
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

_source line 28 · 2026-05-14T05:33:58.771Z_

<details><summary>↩ Tool result · `toolu_01ExCMPLDuMdQ86euPdQzfGg`</summary>

```text
# CoRL 2026 Deadlines

Based on the commit, the exact deadlines for CoRL 2026 are:

## Abstract Submission Deadline
- **Date:** May 26, 2026
- **Time:** 11:59 UTC
- **Full timestamp:** 2026-05-26 11:59:00 UTC

## Paper Submission Deadline
- **Date:** May 29, 2026
- **Time:** 11:59 UTC
- **Full timestamp:** 2026-05-29 11:59:00 UTC

Both deadlines are specified in **UTC timezone**.

The conference itself runs **November 9-12, 2026** in Austin, Texas at the JW Marriott Austin (110 E 2nd St), with workshops on Nov 9 and the main conference running Nov 10-12.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3740536-4ac4-4bad-bdad-f636052fbd5c",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "9c242fe1-909f-4e14-a646-7882b60597e9",
  "sourceToolAssistantUUID": "b3740536-4ac4-4bad-bdad-f636052fbd5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T05:34:04.512Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PnJstKomFgCwcgbeSy7qKh`</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
  "prompt": "What are the exact submission deadlines for CoRL 2026 listed on OpenReview? Include abstract deadline and paper deadline with exact dates and timezone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c242fe1-909f-4e14-a646-7882b60597e9",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v762Soj5XUajtnKjJu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8c6928d-f1b0-440d-a3fa-3646367e5aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLHn7yk44Ch6VVz2A7jnaJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 17293,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 17293,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 350,
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

_source line 30 · 2026-05-14T05:34:08.132Z_

<details><summary>↩ Tool result · `toolu_01PnJstKomFgCwcgbeSy7qKh`</summary>

```text
I cannot find the specific submission deadlines for CoRL 2026 on the web page content provided. The page shows only the OpenReview platform's navigation menu and footer information, but does not include any details about CoRL 2026's abstract deadline, paper deadline, or timezone information.

To locate these submission deadlines, you would need to visit the actual CoRL 2026 conference page on OpenReview or check the conference's official website directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8c6928d-f1b0-440d-a3fa-3646367e5aaa",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a8598031bd959b33e",
  "type": "user",
  "uuid": "2d0fc5d3-1b6a-49e7-be35-c656159d650a",
  "sourceToolAssistantUUID": "b8c6928d-f1b0-440d-a3fa-3646367e5aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T05:34:41.186Z_

Now I have sufficient information to compile my findings. Here is the complete report:

---

## Findings

### 1. CoRL 2026 Submission Deadlines

**PARTIALLY MATCHES the claim.** The idea claims abstract deadline May 25 and paper deadline May 28 AoE. According to available sources:

- The Hugging Face AI-deadlines tracker (which pulls from official sources) lists: **Abstract deadline: May 26, 2026 (11:59 UTC)** and **Paper deadline: May 29, 2026 (11:59 UTC)**.
- However, the official CoRL website's "Instruction for Authors" page explicitly states "the paper submission deadline is Thursday (5/28) EOD rather than Friday."
- Note that 11:59 UTC on May 26 is essentially May 25 AoE (since AoE = UTC-12, meaning 11:59 UTC on the 26th corresponds to 23:59 AoE on May 25). Similarly, 11:59 UTC on May 29 corresponds to 23:59 AoE on May 28.

**Verdict: The claimed deadlines of May 25 (abstract) and May 28 (paper) AoE appear to be CORRECT** when converting from the UTC times listed. The AoE interpretation matches: May 26 11:59 UTC = May 25 23:59 AoE, and May 29 11:59 UTC = May 28 23:59 AoE. This is further confirmed by the official site mentioning 5/28 as the paper deadline day.

Sources:
- [CoRL 2026 Official Site](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [HuggingFace AI-Deadlines Commit](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)

---

### 2. OpenVLA-OFT (arXiv 2502.19645) and LIBERO Performance

**CONFIRMED.** The paper exists and the 97.1% LIBERO claim is verified.

- **Title:** "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
- **arXiv ID:** 2502.19645 (confirmed)
- **LIBERO Performance:** OpenVLA-OFT achieves **97.1% average success rate** across four LIBERO task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long), up from 76.5% for the original OpenVLA.
- **Additional details:** Uses parallel decoding, action chunking, continuous action representation, and L1 regression. Achieves 26x speedup in action generation throughput (109.7 Hz).

Sources:
- [arXiv 2502.19645](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [GitHub Repository](https://github.com/moojink/openvla-oft)

---

### 3. "Generalized Information Bottleneck" (arXiv 2509.26327)

**CONFIRMED - the paper EXISTS.** The arXiv ID 2509.26327 is valid.

- **Full Title:** "A Generalized Information Bottleneck Theory of Deep Learning"
- **Authors:** Charles Westphal, Stephen Hailes, Mirco Musolesi
- **Submitted:** September 30, 2025 (v1); last revised January 30, 2026 (v3)
- **Note on arXiv ID format:** The ID "2509.26327" is valid -- it was submitted in September 2025, which is consistent with the 2509.xxxxx format. Since today is May 2026, this paper exists and has been available for several months.

Sources:
- [arXiv 2509.26327](https://arxiv.org/abs/2509.26327)
- [ResearchGate](https://www.researchgate.net/publication/396049012_A_Generalized_Information_Bottleneck_Theory_of_Deep_Learning)

---

### 4. FOMA (First-Order Manifold Data Augmentation) at ICML 2024

**CONFIRMED.**

- **Full Title:** "First-Order Manifold Data Augmentation for Regression Learning"
- **Authors:** Ilya Kaufman and Omri Azencot
- **Published in:** Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 23324-23342
- **arXiv:** 2406.10914
- **Code:** https://github.com/azencot-group/FOMA

Sources:
- [ICML 2024 Poster](https://icml.cc/virtual/2024/poster/33419)
- [PMLR Proceedings](https://proceedings.mlr.press/v235/kaufman24a.html)
- [arXiv 2406.10914](https://arxiv.org/abs/2406.10914)

---

### 5. DRIBO (Robust Deep RL via Multi-View Information Bottleneck) at ICML 2022

**CONFIRMED.**

- **Full Title:** "DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck"
- **Authors:** Jiameng Fan and Wenchao Li
- **Published at:** ICML 2022 (Proceedings of Machine Learning Research, v162)
- **arXiv:** 2102.13268
- **Code:** https://github.com/JmfanBU/DRIBO

Sources:
- [ICML 2022 Poster](https://icml.cc/virtual/2022/poster/16441)
- [arXiv 2102.13268](https://arxiv.org/abs/2102.13268)
- [PMLR PDF](https://proceedings.mlr.press/v162/fan22b/fan22b.pdf)
- [OpenReview](https://openreview.net/forum?id=Py8WbvKH_wv)

---

## Summary Table

| Claim | Status | Notes |
|-------|--------|-------|
| CoRL 2026 abstract deadline May 25 AoE | CORRECT | May 26 11:59 UTC = May 25 23:59 AoE |
| CoRL 2026 paper deadline May 28 AoE | CORRECT | May 29 11:59 UTC = May 28 23:59 AoE; official site confirms "5/28" |
| OpenVLA-OFT (2502.19645) achieves 97.1% on LIBERO | CORRECT | Verified across four LIBERO task suites |
| Generalized Information Bottleneck (2509.26327) exists | CORRECT | Published Sep 2025, revised Jan 2026 |
| FOMA at ICML 2024 | CORRECT | Confirmed in proceedings |
| DRIBO at ICML 2022 | CORRECT | Confirmed in proceedings |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0fc5d3-1b6a-49e7-be35-c656159d650a",
  "isSidechain": true,
  "agentId": "a8598031bd959b33e",
  "requestId": "req_011Cb1v7moMrVaQhXNPD2kNU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96bef64a-7ade-42eb-93f3-2820a36cc0b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3AdZzhyv42bPCFPiuoNZW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 17643,
      "output_tokens": 1824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1824,
          "cache_read_input_tokens": 17643,
          "cache_creation_input_tokens": 239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 239,
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
