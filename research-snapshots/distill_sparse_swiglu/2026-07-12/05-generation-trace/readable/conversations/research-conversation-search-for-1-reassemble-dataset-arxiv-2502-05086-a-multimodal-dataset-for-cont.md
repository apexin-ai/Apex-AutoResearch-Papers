# Research conversation: Search for: 1. "REASSEMBLE dataset" (arXiv 2502.05086) — a multimodal dataset for contact-rich robotic assembly. Verify 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aabaffd40f980f5d0.jsonl`
- **Structured JSON:** [`f262a6eaf5496320ee1f.json`](../../sessions/f2/f262a6eaf5496320ee1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-13T17:27:01.252Z_

Search for:

1. "REASSEMBLE dataset" (arXiv 2502.05086) — a multimodal dataset for contact-rich robotic assembly. Verify it exists and whether it includes proprioception and force-torque data. Is it publicly available?

2. "LIBERO benchmark low VOC tasks" or "LIBERO visual observability" — are there any published analyses of which LIBERO tasks have low visual observability? Do LIBERO tasks generally have high or low VOC (Value-Order Correlation)?

3. "multimodal contrastive learning progress estimation robot" — any work that trains contrastive encoders on vision + proprioception for task progress estimation?

Use WebSearch. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "b799f4e4-7af9-4351-852d-7b0a1aeb00f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T17:27:01.254Z_

```json
{
  "parentUuid": "b799f4e4-7af9-4351-852d-7b0a1aeb00f8",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
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
  "uuid": "929f0632-cf45-41cb-abff-a7759754d04d",
  "timestamp": "2026-05-13T17:27:01.254Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T17:27:03.282Z_



I'll search for all three topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "929f0632-cf45-41cb-abff-a7759754d04d",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxfr8vUgaiNUFm4BXM1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "473f5533-7d5c-4894-9a57-9eac6ebd7d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XR93faCNmAJuUVbkmE13DM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 708,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-13T17:27:03.883Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UT87EXdt3vE993GF7BQew9`</summary>

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
  "parentUuid": "473f5533-7d5c-4894-9a57-9eac6ebd7d4d",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxfr8vUgaiNUFm4BXM1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9ca6f20-21e4-4599-99a2-22d47f2df3ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XR93faCNmAJuUVbkmE13DM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 8223,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 708,
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

_source line 5 · 2026-05-13T17:27:03.886Z_

<details><summary>↩ Tool result · `toolu_01UT87EXdt3vE993GF7BQew9`</summary>

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
  "parentUuid": "a9ca6f20-21e4-4599-99a2-22d47f2df3ab",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "d17c78cf-00f3-443c-a1c7-5ecddea1ab73",
  "sourceToolAssistantUUID": "a9ca6f20-21e4-4599-99a2-22d47f2df3ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T17:27:10.542Z_



Now let me run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d17c78cf-00f3-443c-a1c7-5ecddea1ab73",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxg3u7EVxuB6Nk6jebm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4a0930d-b8f4-456a-94eb-278221cf72e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4PbPutSY2etwGqLWgZSXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 7 · 2026-05-13T17:27:11.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AwqqYD4BV26ABFF27uxMLH`</summary>

```json
{
  "query": "REASSEMBLE dataset arXiv 2502.05086 multimodal contact-rich robotic assembly proprioception force-torque"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4a0930d-b8f4-456a-94eb-278221cf72e7",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxg3u7EVxuB6Nk6jebm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "759caa24-ab05-4a49-918d-b96c5f8bcb1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4PbPutSY2etwGqLWgZSXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 8 · 2026-05-13T17:27:12.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K1upfp92HLgCEaNQWpThiy`</summary>

```json
{
  "query": "LIBERO benchmark visual observability VOC value-order correlation tasks analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "759caa24-ab05-4a49-918d-b96c5f8bcb1a",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxg3u7EVxuB6Nk6jebm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e2e16fb-a232-4e51-bf0d-32791673887c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4PbPutSY2etwGqLWgZSXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 9 · 2026-05-13T17:27:13.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014qUH8TyxkWdXy4SNn53mK6`</summary>

```json
{
  "query": "multimodal contrastive learning progress estimation robot vision proprioception"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2e16fb-a232-4e51-bf0d-32791673887c",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011Cazxg3u7EVxuB6Nk6jebm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13a9aaef-4b8c-4b46-b06e-29a4d719ccad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4PbPutSY2etwGqLWgZSXk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8931,
      "output_tokens": 190,
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
          "output_tokens": 190,
          "cache_read_input_tokens": 8931,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
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

_source line 10 · 2026-05-13T17:27:17.978Z_

<details><summary>↩ Tool result · `toolu_01AwqqYD4BV26ABFF27uxMLH`</summary>

```text
Web search results for query: "REASSEMBLE dataset arXiv 2502.05086 multimodal contact-rich robotic assembly proprioception force-torque"

Links: [{"title":"[2502.05086] REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://arxiv.org/abs/2502.05086"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://arxiv.org/html/2502.05086v1"},{"title":"REASSEMBLE: A Multimodal Dataset for","url":"https://arxiv.org/pdf/2502.05086"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250205086S/abstract"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://researchdata.tuwien.ac.at/records/0ewrv-8cb44"},{"title":"(PDF) REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://www.researchgate.net/publication/388848226_REASSEMBLE_A_Multimodal_Dataset_for_Contact-rich_Robotic_Assembly_and_Disassembly"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.05086v2"},{"title":"Preview","url":"https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/preview/README.txt?include_deleted=0"},{"title":"GitHub - TUWIEN-ASL/REASSEMBLE · GitHub","url":"https://github.com/TUWIEN-ASL/REASSEMBLE"},{"title":"electronic library - Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://elib.dlr.de/221994/"}]

Based on the search results, here's what I found about the REASSEMBLE dataset (arXiv 2502.05086):

## Overview
REASSEMBLE is a multimodal dataset designed specifically for contact-rich manipulation tasks, built around the NIST Assembly Task Board 1 benchmark and includes four actions (pick, insert, remove, and place) involving 17 objects.

## Dataset Size and Scope
The dataset contains 4,551 demonstrations, of which 4,035 were successful, spanning a total of 781 minutes.

## Sensor Modalities
The dataset features multi-modal sensor data, including event cameras, force-torque sensors, microphones, and multi-view RGB cameras. Additionally, REASSEMBLE contains data from robot proprioception, RGB cameras, Force & Torque sensors, microphones, and event cameras.

## Key Features
The diverse dataset supports research in areas such as learning contact-rich manipulation, task condition identification, action segmentation, and more, with multimodal data including force-torque sensors, hierarchical labels, and long horizon tasks covering multiple steps.

## Motivation
Robotic manipulation remains a core challenge in robotics, particularly for contact-rich tasks such as industrial assembly and disassembly, and existing datasets have significantly advanced learning in manipulation but are primarily focused on simpler tasks like object rearrangement, falling short of capturing the complexity and physical dynamics involved in assembly and disassembly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "759caa24-ab05-4a49-918d-b96c5f8bcb1a",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "51f664e7-bfed-4498-a6e8-2ac5516bea01",
  "sourceToolAssistantUUID": "759caa24-ab05-4a49-918d-b96c5f8bcb1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T17:27:19.306Z_

<details><summary>↩ Tool result · `toolu_01K1upfp92HLgCEaNQWpThiy`</summary>

```text
Web search results for query: "LIBERO benchmark visual observability VOC value-order correlation tasks analysis"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v1"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"}]

Based on the search results, I found information related to the LIBERO benchmark and robustness analysis of vision-language-action models. However, the specific terms "visual observability," "VOC," and "value-order correlation tasks analysis" don't appear in the results I retrieved.

Here's what I found about LIBERO and related analyses:

**LIBERO Benchmark Overview:**
LIBERO is a standardized, extensible suite benchmarking VLA models in robot manipulation with lifelong, multi-task challenges in dynamic, simulated environments.

**LIBERO-Plus Analysis:**
The benchmark construction follows a systematic two-stage process: (1) expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing based on empirical findings; and (2) evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels (Level-1 to Level-5) according to observed accuracy distributions.

**Robustness Findings:**
The analysis introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

The search results focus on robustness analysis and perturbation studies of Vision-Language-Action models but don't contain information about the specific metrics or analyses you mentioned (visual observability, VOC, value-order correlation). If you're looking for information about those specific concepts, you may want to search with more targeted terms or check the full research papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e2e16fb-a232-4e51-bf0d-32791673887c",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "ccf01f06-ac9d-4928-885c-0a9b8ab47961",
  "sourceToolAssistantUUID": "1e2e16fb-a232-4e51-bf0d-32791673887c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T17:27:22.144Z_

<details><summary>↩ Tool result · `toolu_014qUH8TyxkWdXy4SNn53mK6`</summary>

```text
Web search results for query: "multimodal contrastive learning progress estimation robot vision proprioception"

Links: [{"title":"Scaling Proprioceptive-Visual Learning with ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e0f393e7980a24fd12fa6f15adfa25fb-Paper-Conference.pdf"},{"title":"Multimodal Information Bottleneck for Deep","url":"https://arxiv.org/pdf/2410.17551"},{"title":"Frontiers | Multimodal perception-driven decision-making for human-robot interaction: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1604472/full"},{"title":"Enhancing Tactile-based Reinforcement Learning for Robotic Control Elle Miller","url":"https://openreview.net/pdf/768a2743685c0eedc89d66ff9a06bd2430f49db7.pdf"},{"title":"Contrastive Learning for Enhancing Robust Scene Transfer in Vision-based Agile Flight","url":"https://arxiv.org/html/2309.09865v3"},{"title":"Temporal consistent multi-view perception for robust embodied manipulation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325008386"},{"title":"arXiv:2406.15917v1 [cs.RO] 22 Jun 2024","url":"https://cicl.stanford.edu/papers/du2024robotic.pdf"},{"title":"Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision","url":"https://arxiv.org/pdf/2504.02477"},{"title":"Multimodal Visual-Tactile Representation Learning through ...","url":"https://arxiv.org/pdf/2401.12024"},{"title":"GitHub - curieuxjy/Awesome_Quadrupedal_Robots: Awesome Quadrupedal Robots · GitHub","url":"https://github.com/curieuxjy/Awesome_Quadrupedal_Robots"}]

I found several relevant research papers and projects on the intersection of multimodal contrastive learning, vision, and proprioception in robotics. Here are the key findings:

## Multimodal Learning Approaches

Heterogeneous Pre-trained Transformers (HPT) is a family of architectures designed to scalably learn from data across heterogeneous embodiments, using embodiment-specific tokenizers to align various sensor inputs such as camera views and proprioception inputs, inspired by learning from multimodal data.

Recent work integrates the reconstruction loss and the contrastive loss for learning latent joint representations from images and proprioception. Additionally, the InfoNCE loss with a score function encourages representations of single modalities to be close to the joint representation.

## Progress Estimation in Robot Vision

A ResNet-based vision encoder can be trained via multi-pair adaptive contrastive learning on images of a drone flying around a race track in multiple environments, using task-specific track progress to disambiguate potential self-intersections. The vision encoder enforces that images perceived at similar progress from different environments have similar embeddings.

## Task-Specific Applications

Temporal Consistent Multi-View Perception (TMVP) is a novel two-stage framework that integrates contrastive learning with multi-view imitation learning, employing contrastive learning to extract meaningful, task-relevant features from visual inputs, enhancing temporal consistency.

## Multimodal Tactile and Visual Learning

Multimodal visual-tactile approaches use contrastive training with two distinct paradigms: intra-modal and inter-modal learning, where intra-modal refers to learning exclusively within the same data modality, either between tactile-to-tactile or visual-to-visual representations.

These approaches demonstrate significant progress in combining vision and proprioceptive/tactile information through contrastive learning for robotic applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13a9aaef-4b8c-4b46-b06e-29a4d719ccad",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "010a940f-4432-4e21-85cd-534d80245051",
  "sourceToolAssistantUUID": "13a9aaef-4b8c-4b46-b06e-29a4d719ccad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T17:27:25.667Z_

Let me do a couple of follow-up searches to fill in gaps, particularly on REASSEMBLE's public availability and on the specific VOC / visual observability concept for LIBERO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010a940f-4432-4e21-85cd-534d80245051",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxhPUcACidiotF4HoEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1929d3a6-d40f-4d12-9fcc-17b119ba2a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J532k3fsYPMwtkVWE8Jxcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 10335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

_source line 14 · 2026-05-13T17:27:26.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BazpgRs86f9NYbGbB4RCke`</summary>

```json
{
  "query": "REASSEMBLE dataset publicly available download TUWIEN ASL github robot assembly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1929d3a6-d40f-4d12-9fcc-17b119ba2a5b",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxhPUcACidiotF4HoEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2905a6ea-b335-42b3-8a33-89ae3c3ba0e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J532k3fsYPMwtkVWE8Jxcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 10335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

_source line 15 · 2026-05-13T17:27:27.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FknV4LLFjxpDvHEUqZmWb9`</summary>

```json
{
  "query": "LIBERO benchmark \"low visual observability\" OR \"visual observability coefficient\" OR \"VOC\" robotic manipulation tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2905a6ea-b335-42b3-8a33-89ae3c3ba0e4",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxhPUcACidiotF4HoEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5cd2061-c167-49f3-ba16-c31c4d41e492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J532k3fsYPMwtkVWE8Jxcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 10335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

_source line 16 · 2026-05-13T17:27:27.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SqjNBEj9ovX2jTs5pLFmFe`</summary>

```json
{
  "query": "contrastive learning proprioception vision task progress estimation reward robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cd2061-c167-49f3-ba16-c31c4d41e492",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxhPUcACidiotF4HoEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd24dc7f-752d-4ec6-bf78-77696aaac55a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J532k3fsYPMwtkVWE8Jxcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 10335,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 10335,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2978,
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

_source line 17 · 2026-05-13T17:27:32.821Z_

<details><summary>↩ Tool result · `toolu_01BazpgRs86f9NYbGbB4RCke`</summary>

```text
Web search results for query: "REASSEMBLE dataset publicly available download TUWIEN ASL github robot assembly"

Links: [{"title":"GitHub - TUWIEN-ASL/REASSEMBLE · GitHub","url":"https://github.com/TUWIEN-ASL/REASSEMBLE"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://tuwien-asl.github.io/REASSEMBLE_page/"},{"title":"GitHub - TUWIEN-ASL/ATLAS-tuwienasl: An Annotation Tool for Long-horizon Robotic Action Segmentation · GitHub","url":"https://github.com/TUWIEN-ASL/ATLAS-tuwienasl"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://researchdata.tuwien.ac.at/records/0ewrv-8cb44"},{"title":"[2502.05086] REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://arxiv.org/abs/2502.05086"},{"title":"Preview","url":"https://researchdata.tuwien.ac.at/records/0ewrv-8cb44/preview/README.txt?include_deleted=0"},{"title":"(PDF) REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly","url":"https://www.researchgate.net/publication/388848226_REASSEMBLE_A_Multimodal_Dataset_for_Contact-rich_Robotic_Assembly_and_Disassembly"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly | OpenReview","url":"https://openreview.net/forum?id=vZBuK0mt1A"},{"title":"REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250205086S/abstract"},{"title":"REASSEMBLE: A Multimodal Dataset for","url":"https://arxiv.org/pdf/2502.05086"}]

Based on the search results, here's what I found about the REASSEMBLE dataset:

## Overview

REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt) is a new dataset designed specifically for contact-rich manipulation tasks. Built around the NIST Assembly Task Board 1 benchmark, REASSEMBLE includes four actions (pick, insert, remove, and place) involving 17 objects. The dataset contains 4,551 demonstrations, of which 4,035 were successful, spanning a total of 781 minutes.

## Multimodal Data

The dataset features multi-modal sensor data including event cameras, force-torque sensors, microphones, and multi-view RGB cameras. REASSEMBLE contains data from robot proprioception, RGB cameras, Force&Torque sensors, microphones, and event cameras, with actions segmentation labels at two hierarchical levels.

## Public Availability and Download

The dataset is publicly available on the project website: https://tuwien-asl.github.io/REASSEMBLE_page/. The dataset can be downloaded from Google Drive: https://drive.google.com/drive/u/1/folders/1HPsG63iI2tpovJoh_o2zhmyx9muNcnVx

## Code and Installation

The repository can be cloned using: git clone https://github.com/TUWIEN-ASL/REASSEMBLE.git The GitHub repository contains installation instructions and scripts for using the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2905a6ea-b335-42b3-8a33-89ae3c3ba0e4",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "a44172b6-62c5-46da-a08f-8cf751dcbdf8",
  "sourceToolAssistantUUID": "2905a6ea-b335-42b3-8a33-89ae3c3ba0e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T17:27:34.786Z_

<details><summary>↩ Tool result · `toolu_01FknV4LLFjxpDvHEUqZmWb9`</summary>

```text
Web search results for query: "LIBERO benchmark "low visual observability" OR "visual observability coefficient" OR "VOC" robotic manipulation tasks"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"}]

Based on the search results, I found information about the LIBERO benchmark for robotic manipulation tasks. However, the search results do not contain specific information about "low visual observability," "visual observability coefficient," or "VOC" as explicit concepts or metrics within the LIBERO benchmark.

What I did find is that LIBERO is a standardized and extensible benchmarking suite that evaluates multi-modal vision-language-action models in diverse robotic manipulation tasks. The benchmark includes several variants and extensions:

- LIBERO-PRO incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and environments—and supports randomized combinations of these dimensions for more faithful evaluation.

- LIBERO-X is an evolved version of the original LIBERO benchmark, where "X" denotes eXtreme to reflect its goal of pushing evaluation limits, with a new evaluation protocol that delivers a progressively challenging, multi-level test suite for assessing the generalization of VLA models in complex environments.

The search results discuss various evaluation dimensions like spatial generalization, object recognition, and instruction understanding, but they do not mention "low visual observability" or a "visual observability coefficient" as a specific benchmark metric or task characteristic within LIBERO.

If you're looking for information specifically about visual observability metrics in the LIBERO benchmark, you may need to consult the original papers directly or search for more recent publications that introduce this concept.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5cd2061-c167-49f3-ba16-c31c4d41e492",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "3e0da061-6881-490a-9fcb-daa779f8bd1e",
  "sourceToolAssistantUUID": "a5cd2061-c167-49f3-ba16-c31c4d41e492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T17:27:35.510Z_

<details><summary>↩ Tool result · `toolu_01SqjNBEj9ovX2jTs5pLFmFe`</summary>

```text
Web search results for query: "contrastive learning proprioception vision task progress estimation reward robot manipulation"

Links: [{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/html/2508.01600"},{"title":"Frontiers | Reinforcement Learning With Vision-Proprioception Model for Robot Planar Pushing","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.829437/full"},{"title":"Learning Non-prehensile Manipulation with Force and ...","url":"https://www.merl.com/publications/docs/TR2026-011.pdf"},{"title":"Enhancing Tactile-based Reinforcement Learning for Robotic Control","url":"https://dexterous-humanoid-manipulation.github.io/src/file/paper/emiller.pdf"},{"title":"Scaling Proprioceptive-Visual Learning with ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e0f393e7980a24fd12fa6f15adfa25fb-Paper-Conference.pdf"},{"title":"[2512.13093] PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations","url":"https://arxiv.org/abs/2512.13093"},{"title":"Precise and Dexterous Robotic Manipulation via Human-in ...","url":"https://hil-serl.github.io/static/hil-serl-paper.pdf"},{"title":"BarlowWalk: Self-supervised Representation Learning for Legged","url":"https://www.arxiv.org/pdf/2508.00939"},{"title":"GitHub - hk-zh/language-conditioned-robot-manipulation-models: https://arxiv.org/abs/2312.10807 · GitHub","url":"https://github.com/hk-zh/language-conditioned-robot-manipulation-models"},{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"}]

I found several relevant research papers and resources on your search query. Here's what the search results revealed:

## Key Research Areas

**Contrastive Learning in Robot Manipulation:**

Recent work includes contrastive representation learning as pre-training that performs policy fine-tuning with proprioception and vision representation. One notable approach is CLASS (Contrastive Learning via Action Sequence Supervision), which uses a contrastive learning objective that incorporates soft positive supervision using pre-computed DTW (Dynamic Time Warping) values.

**Proprioception and Vision Integration:**

Both proprioception and vision information are crucial for complex, contact-rich, long-horizon behaviors in robotics. A vision-proprioception model for object manipulation uses a Variational Autoencoder (VAE) to extract compact representations from the task-relevant part of the image, fusing latent representations from the VAE and robot end-effector position together as the state of a Markov Decision Process.

**Task Progress and Reward Estimation:**

The PvP framework uses a Proprioceptive-Privileged contrastive learning approach that learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning.

**Multimodal Learning Approaches:**

Recent work suggests that self-supervised objectives should be modality-specific, with reconstruction for proprioception and contrastive losses for images.

The search results show active research combining these elements for improving robot manipulation through better representation learning and reward estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd24dc7f-752d-4ec6-bf78-77696aaac55a",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "a0d17b06-edee-43a1-9c73-28174baa8085",
  "sourceToolAssistantUUID": "fd24dc7f-752d-4ec6-bf78-77696aaac55a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T17:27:38.630Z_

Let me do one more targeted search on the VOC concept to see if it originates from a specific paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0d17b06-edee-43a1-9c73-28174baa8085",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxiNcJPn5j3XyDGPHF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b126e678-c4c1-4faa-b842-73ffb9cc1f9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PETLP84DmLPMWKi7DVMwDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3060,
      "cache_read_input_tokens": 13313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3060,
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

_source line 21 · 2026-05-13T17:27:39.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T7zdbvJ1xgv3qRqn8cisqX`</summary>

```json
{
  "query": "\"value-order correlation\" VOC robot manipulation task progress visual observation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b126e678-c4c1-4faa-b842-73ffb9cc1f9f",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxiNcJPn5j3XyDGPHF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98b42ec4-fdaa-4d7a-aadc-d214b458d6c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PETLP84DmLPMWKi7DVMwDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3060,
      "cache_read_input_tokens": 13313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3060,
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

_source line 22 · 2026-05-13T17:27:40.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DBYDa5ypPiiunZcwtRiVYL`</summary>

```json
{
  "query": "CLASS contrastive learning action sequence supervision robot manipulation task progress DTW 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b42ec4-fdaa-4d7a-aadc-d214b458d6c1",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxiNcJPn5j3XyDGPHF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ea8a8e-c2fd-4134-90f5-e5467f8aa648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PETLP84DmLPMWKi7DVMwDq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3060,
      "cache_read_input_tokens": 13313,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 13313,
          "cache_creation_input_tokens": 3060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3060,
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

_source line 23 · 2026-05-13T17:27:47.169Z_

<details><summary>↩ Tool result · `toolu_01T7zdbvJ1xgv3qRqn8cisqX`</summary>

```text
Web search results for query: ""value-order correlation" VOC robot manipulation task progress visual observation 2024 2025"

Links: [{"title":"OpenGVL - Benchmarking Visual Temporal Progress for Data Curation","url":"https://arxiv.org/html/2509.17321"},{"title":"Generative Value Learning: Vision Language Models are In-Context Value Learners","url":"https://generative-value-learning.github.io/"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Vision Language Models are In-Context Value Learners","url":"https://arxiv.org/html/2411.04549"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/pdf/2507.10672"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, I found relevant information about VOC (Value-Order Correlation) in robot manipulation research:

## Value-Order Correlation (VOC) Overview

VOC is a lightweight, yet predictive method for evaluating value models at scale on real-world robotic datasets. The metric computes the rank correlation between the predicted values and the chronological order of the input expert video, with VOC ranging from −1 to 1, where 1 indicates that the two orderings are perfectly aligned.

## Task Progress and Visual Observation

Predicting temporal progress from visual trajectories is important for intelligent robots that can learn, adapt, and improve. To address the challenges of learning progress estimators across different tasks and domains, researchers presented Generative Value Learning (GVL), a universal value function estimator that leverages the world knowledge embedded in vision-language models (VLMs) to predict task progress.

Expert quality demonstrations, by construction, have values that monotonically increase with time, and thus a good value model should have high VOC scores when evaluated on expert videos. On the other hand, fixing a good value model, low-quality trajectories should have low VOC scores.

## Recent Progress (2024-2025)

Ma et al. introduced the Value-Order Correlation (VOC) metric, which exhibits useful characteristics for data curation applications. Recent work in 2025 has involved benchmarking VOC through the OpenGVL framework, which evaluates various vision-language models' performance on temporal progress prediction tasks for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b42ec4-fdaa-4d7a-aadc-d214b458d6c1",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "f6e08a75-5d55-4886-9ec4-8f674039f340",
  "sourceToolAssistantUUID": "98b42ec4-fdaa-4d7a-aadc-d214b458d6c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T17:27:48.395Z_

<details><summary>↩ Tool result · `toolu_01DBYDa5ypPiiunZcwtRiVYL`</summary>

```text
Web search results for query: "CLASS contrastive learning action sequence supervision robot manipulation task progress DTW 2025"

Links: [{"title":"[2508.01600] CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/abs/2508.01600"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://proceedings.mlr.press/v305/lee25a.html"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://arxiv.org/html/2508.01600v1"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://class-robot.github.io/"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250801600L/abstract"},{"title":"CLASS: Contrastive Learning via Action Sequence Supervision for Robot Manipulation","url":"https://www.researchgate.net/publication/394293406_CLASS_Contrastive_Learning_via_Action_Sequence_Supervision_for_Robot_Manipulation"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"Time-Contrastive Networks: Self-Supervised Learning from Video | Request PDF","url":"https://www.researchgate.net/publication/327814164_Time-Contrastive_Networks_Self-Supervised_Learning_from_Video"},{"title":"Contrastive Language, Action, and State Pre-training for Robot Learning","url":"https://openreview.net/pdf?id=sxKR6zhBDH"}]

Based on the search results, here's what I found about CLASS:

## Overview

CLASS (Contrastive Learning via Action Sequence Supervision) is a method for learning behavioral representations from demonstrations using supervised contrastive learning.

## Key Technical Approach

CLASS leverages weak supervision from similar action sequences identified via Dynamic Time Warping (DTW) and optimizes a soft InfoNCE loss with similarity-weighted positive pairs. The method consists of two stages: (a) pre-computing pairwise action sequence similarities from demonstration data, and (b) representation learning via supervised contrastive learning with a Soft InfoNCE loss.

## Problem it Addresses

Recent advances in Behavior Cloning (BC) have led to strong performance in robotic manipulation, but BC faces significant challenges when applied to heterogeneous datasets, such as visual shift with different camera poses or object appearances, where performance degrades. This stems from BC's tendency to overfit individual demonstrations rather than capture shared structure, limiting generalization.

## Performance Results

CLASS was evaluated on 5 simulation benchmarks and 3 real-world tasks to achieve competitive results using retrieval-based control with representations only. For downstream policy learning under significant visual shifts, Diffusion Policy with CLASS pre-training achieves an average success rate of 75%, while all other baseline methods fail to perform competitively.

## Publication

CLASS was published in the Proceedings of The 9th Conference on Robot Learning (CoRL), PMLR 305:4743-4766, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ea8a8e-c2fd-4134-90f5-e5467f8aa648",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "ae2f13d4-e0cb-4020-8de3-29f875aa1dc5",
  "sourceToolAssistantUUID": "e7ea8a8e-c2fd-4134-90f5-e5467f8aa648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T17:27:52.983Z_

Now let me do one final search to check whether VOC has been specifically analyzed on LIBERO tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2f13d4-e0cb-4020-8de3-29f875aa1dc5",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxjKkgXYwh9yUFBAn9d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "607d262e-0ced-4a49-8fc5-024537d2ebcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqMdC4RTZ364YQPn33J7Wg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 16373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2130,
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

_source line 26 · 2026-05-13T17:27:53.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QjdxV1eQdbUUryDnyUDxFo`</summary>

```json
{
  "query": "OpenGVL \"value-order correlation\" LIBERO tasks VOC scores visual progress estimation benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "607d262e-0ced-4a49-8fc5-024537d2ebcb",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxjKkgXYwh9yUFBAn9d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f2a896b-4781-4dfc-aceb-435afb99a981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqMdC4RTZ364YQPn33J7Wg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 16373,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 16373,
          "cache_creation_input_tokens": 2130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2130,
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

_source line 27 · 2026-05-13T17:28:01.868Z_

<details><summary>↩ Tool result · `toolu_01QjdxV1eQdbUUryDnyUDxFo`</summary>

```text
Web search results for query: "OpenGVL "value-order correlation" LIBERO tasks VOC scores visual progress estimation benchmark"

Links: [{"title":"GitHub - budzianowski/opengvl: Open GVL · GitHub","url":"https://github.com/budzianowski/opengvl"},{"title":"OpenGVL - Benchmarking Visual Temporal Progress for Data Curation","url":"https://arxiv.org/html/2509.17321"},{"title":"OpenGVL - Benchmarking Visual Temporal Progress for Data Curation","url":"https://openreview.net/pdf/c90b8ea97ca405a97aa589f07ec4217be636cf57.pdf"},{"title":"Generative Value Learning: Vision Language Models are In-Context Value Learners","url":"https://generative-value-learning.github.io/"},{"title":"Vision Language Models are In-Context Value Learners","url":"https://arxiv.org/html/2411.04549v1"},{"title":"Paper page - OpenGVL - Benchmarking Visual Temporal Progress for Data Curation","url":"https://huggingface.co/papers/2509.17321"},{"title":"[2509.17321] OpenGVL -- Benchmarking Visual Temporal Progress for Data Curation","url":"https://arxiv.org/abs/2509.17321"},{"title":"OpenGVL -- Benchmarking Visual Temporal Progress for Data Curation | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.17321v4"},{"title":"Michał Tyrolski","url":"https://mtyrolski.github.io/"},{"title":"OpenGVL (OpenGVL)","url":"https://huggingface.co/OpenGVL"}]

Based on the web search results, here's what I found about OpenGVL, value-order correlation, LIBERO tasks, VOC scores, and visual progress estimation:

## OpenGVL Overview

OpenGVL is an open-source benchmark for evaluating VLMs on temporal task progress prediction for robotics applications. It was developed as a foundational tool for data management at scale.

## Value-Order Correlation (VOC)

Value-Order Correlation (VOC) is a metric that computes the rank correlation between the predicted values and the chronological order of the input expert video, ranging from −1 to 1, where 1 indicates that the two orderings are perfectly aligned.

Expert quality demonstrations, by construction, have values that monotonically increase with time, and thus a good value model should have high VOC scores when evaluated on expert videos.

## Visual Progress Estimation Benchmark

OpenGVL is a comprehensive benchmark for estimating task progress across diverse challenging manipulation tasks involving both robotic and human embodiments. The Value-Order Correlation (VOC) metric exhibits useful characteristics for data curation applications.

## Performance Findings

Open-source model families significantly underperform closed-source counterparts, achieving only approximately 70% of their performance on temporal progress prediction tasks.

The search results discuss OpenGVL's general framework and metrics but do not contain specific information about LIBERO tasks within the OpenGVL benchmark. The results indicate that OpenGVL evaluates task progress on various robotic datasets but don't detail LIBERO-specific results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f2a896b-4781-4dfc-aceb-435afb99a981",
  "isSidechain": true,
  "promptId": "e4227f8e-b015-45cc-9a19-d9d9011fba01",
  "agentId": "aabaffd40f980f5d0",
  "type": "user",
  "uuid": "b66dd626-bda6-490e-b8e3-07353783a9bd",
  "sourceToolAssistantUUID": "2f2a896b-4781-4dfc-aceb-435afb99a981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T17:28:45.596Z_

Here are the findings for all three queries:

---

## 1. REASSEMBLE Dataset (arXiv 2502.05086)

**Confirmed to exist.** REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt) is a multimodal dataset for contact-rich robotic assembly and disassembly from TU Wien's Autonomous Systems Lab.

**Modalities -- Yes, it includes both proprioception and force-torque data.** The full sensor suite is:
- Robot proprioception
- Multi-view RGB cameras
- Force & torque sensors
- Microphones
- Event cameras

The dataset is built around the NIST Assembly Task Board 1 benchmark, covers 4 actions (pick, insert, remove, place) across 17 objects, and contains 4,551 demonstrations (4,035 successful), totaling 781 minutes. It also provides hierarchical action segmentation labels.

**Publicly available -- Yes.** The dataset can be downloaded from Google Drive, with code and tooling on GitHub at [TUWIEN-ASL/REASSEMBLE](https://github.com/TUWIEN-ASL/REASSEMBLE). The project page is at [tuwien-asl.github.io/REASSEMBLE_page](https://tuwien-asl.github.io/REASSEMBLE_page/), and the data record is also archived at [researchdata.tuwien.ac.at](https://researchdata.tuwien.ac.at/records/0ewrv-8cb44).

---

## 2. LIBERO Benchmark and VOC / Visual Observability

**No published analysis of "low visual observability" specific to LIBERO tasks was found.** The term "visual observability coefficient" does not appear as an established metric in the LIBERO literature.

However, the concept you may be referring to -- **Value-Order Correlation (VOC)** -- does exist as a distinct metric introduced by Ma et al. in the **Generative Value Learning (GVL)** paper (arXiv 2411.04549). VOC measures the rank correlation between predicted value scores and chronological order in expert demonstration videos, ranging from -1 to 1. A high VOC means visual progress is easy to track from video frames alone; a low VOC suggests the task's progress is not well-captured visually (i.e., low visual observability).

The **OpenGVL benchmark** (arXiv 2509.17321) subsequently built a comprehensive evaluation framework around VOC for benchmarking VLMs on temporal progress prediction. However, searches did not surface a specific published analysis breaking down which individual LIBERO tasks have high vs. low VOC. The OpenGVL benchmark evaluates across diverse manipulation datasets, but LIBERO-specific VOC breakdowns were not found in publicly available materials.

In general, many LIBERO tasks involve visually salient pick-and-place style manipulation where progress is reasonably observable from images, but contact-rich or occluded sub-tasks could plausibly have lower VOC. No paper explicitly categorizes LIBERO tasks by this dimension.

---

## 3. Multimodal Contrastive Learning for Progress Estimation (Vision + Proprioception)

Several relevant lines of work exist, though no single paper precisely matches "contrastive encoder on vision + proprioception for task progress estimation":

- **CLASS (Contrastive Learning via Action Sequence Supervision)** -- CoRL 2025, Lee et al. Uses supervised contrastive learning with soft InfoNCE loss and DTW-based action sequence similarity to learn behavioral representations from demonstrations. It learns representations from vision that capture task structure, though it uses action sequences (not proprioception directly) as the supervision signal. [Paper](https://arxiv.org/abs/2508.01600) | [Project page](https://class-robot.github.io/)

- **PvP (Proprioceptive-Privileged Contrastive Representations)** -- arXiv 2512.13093. Uses contrastive learning to learn compact, task-relevant latent representations from proprioception specifically, enabling more data-efficient humanoid robot learning. This is proprioception-focused but uses contrastive methods for representation learning.

- **Scaling Proprioceptive-Visual Learning (HPT)** -- NeurIPS 2024. Heterogeneous Pre-trained Transformers use embodiment-specific tokenizers to align camera views and proprioception inputs, learning joint representations across modalities.

- **Multimodal Information Bottleneck** -- arXiv 2410.17551. Uses reconstruction loss for proprioception and contrastive loss for images, with InfoNCE encouraging single-modality representations to align with joint representations.

- **GVL (Generative Value Learning)** -- arXiv 2411.04549. Uses VLMs (not traditional contrastive learning) to predict task progress from visual observations, introducing the VOC metric. This is vision-only and uses in-context learning rather than contrastive encoders.

The closest match to your query is the **Multimodal Information Bottleneck** work, which explicitly trains contrastive objectives on vision while fusing with proprioception for joint representations, though its primary framing is deep reinforcement learning rather than explicit "progress estimation."

---

Sources:
- [REASSEMBLE paper (arXiv 2502.05086)](https://arxiv.org/abs/2502.05086)
- [REASSEMBLE GitHub](https://github.com/TUWIEN-ASL/REASSEMBLE)
- [REASSEMBLE project page](https://tuwien-asl.github.io/REASSEMBLE_page/)
- [REASSEMBLE data record (TU Wien)](https://researchdata.tuwien.ac.at/records/0ewrv-8cb44)
- [GVL: Vision Language Models are In-Context Value Learners](https://arxiv.org/html/2411.04549)
- [GVL project page](https://generative-value-learning.github.io/)
- [OpenGVL benchmark (arXiv 2509.17321)](https://arxiv.org/abs/2509.17321)
- [OpenGVL GitHub](https://github.com/budzianowski/opengvl)
- [LIBERO benchmark (NeurIPS 2023)](https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf)
- [LIBERO-Plus (arXiv 2510.13626)](https://arxiv.org/abs/2510.13626)
- [CLASS: Contrastive Learning via Action Sequence Supervision (CoRL 2025)](https://arxiv.org/abs/2508.01600)
- [PvP: Proprioceptive-Privileged Contrastive Representations](https://arxiv.org/abs/2512.13093)
- [Scaling Proprioceptive-Visual Learning (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0f393e7980a24fd12fa6f15adfa25fb-Paper-Conference.pdf)
- [Multimodal Information Bottleneck (arXiv 2410.17551)](https://arxiv.org/pdf/2410.17551)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66dd626-bda6-490e-b8e3-07353783a9bd",
  "isSidechain": true,
  "agentId": "aabaffd40f980f5d0",
  "requestId": "req_011CazxkKJRbYKdzPjvqvnwB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "128d8855-9f9f-43f6-8c79-ad123cebc196",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0525d9e9-fe7e-4027-a76e-c873be061569",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xr5T7TsTa2VA86aXrrfx1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 18503,
      "output_tokens": 1753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1753,
          "cache_read_input_tokens": 18503,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 907,
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
