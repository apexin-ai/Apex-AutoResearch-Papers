# Research conversation: I need to understand Robometer (RSS 2026, arXiv 2603.02115) in detail for a research proposal revision. Specifically: 1.

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a19c0e1dbe7cfc9b4.jsonl`
- **Structured JSON:** [`488926671cc49d291643.json`](../../sessions/48/488926671cc49d291643.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-13T19:23:10.636Z_

I need to understand Robometer (RSS 2026, arXiv 2603.02115) in detail for a research proposal revision. Specifically:

1. Search for "Robometer scaling general-purpose robotic reward models trajectory comparisons" and find the paper.
2. Use WebFetch to read the actual paper (try https://arxiv.org/abs/2603.02115).
3. I need to know:
   - Is code/model weights publicly released? Search GitHub for "robometer" or check the paper for a code link.
   - What model architecture (Qwen3-VL-4B)? What inputs does it take?
   - Can it score individual trajectories on RoboMimic? What format does it expect?
   - How long would it take to score 300 RoboMimic MH demos on a single A100?
   - Is it mode-aware or does it give a single global quality score?
   - What benchmarks was it evaluated on? Was RoboMimic one of them?

4. Also search for "Robometer github code release" to verify availability.

Report your findings concisely - focus on practical details about using Robometer as a baseline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "b573affe-f8fb-4276-a696-d19c21a45142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:23:10.639Z_

```json
{
  "parentUuid": "b573affe-f8fb-4276-a696-d19c21a45142",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
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
  "uuid": "8e35ff03-ee67-4562-9b98-450d9435acb7",
  "timestamp": "2026-05-13T19:23:10.639Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:23:13.707Z_



I'll start by fetching the paper and searching for related information in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e35ff03-ee67-4562-9b98-450d9435acb7",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XbmJoqDVBv7VL4F2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50bd450a-7d4a-49dd-9679-8e3fbfb709ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USMySUERn5or95xSiwfoMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9044,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9044,
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

_source line 4 · 2026-05-13T19:23:13.945Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Py4nP1RpAn7YL6VnynWfFA`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50bd450a-7d4a-49dd-9679-8e3fbfb709ab",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XbmJoqDVBv7VL4F2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bae6034-9237-4c0d-b640-8ed1ed4097ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USMySUERn5or95xSiwfoMC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9044,
      "cache_read_input_tokens": 0,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9044,
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

_source line 5 · 2026-05-13T19:23:13.953Z_

<details><summary>↩ Tool result · `toolu_01Py4nP1RpAn7YL6VnynWfFA`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "4bae6034-9237-4c0d-b640-8ed1ed4097ed",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "dac08e8a-47a3-48bc-a330-d0c0c37c83eb",
  "sourceToolAssistantUUID": "4bae6034-9237-4c0d-b640-8ed1ed4097ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:23:18.223Z_



Now let me fetch the paper and search for related information in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dac08e8a-47a3-48bc-a330-d0c0c37c83eb",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XqiwoVg9UABdsjmYu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdb0a255-5019-4e15-be0d-c4b2a75dc784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018E5uo7UDdef4HuZxQuDP58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 7 · 2026-05-13T19:23:25.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CT4ev1wBWBNdJyURy5A5PM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.02115",
  "prompt": "Extract ALL details from this paper about Robometer. I need:\n1. Full title, authors, and affiliation\n2. Model architecture details (backbone model, size, inputs, outputs)\n3. Training data - what datasets, how many trajectory comparisons, how collected\n4. Can it score individual trajectories or only compare pairs? What format/input does it expect?\n5. Is it mode-aware (different quality dimensions) or single global score?\n6. All benchmarks it was evaluated on - list every single one. Was RoboMimic used?\n7. Code/model release - any GitHub links, model weights links, or statements about public release\n8. Inference speed / computational cost details\n9. Any details about how to use it as a reward model for downstream RL or filtering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdb0a255-5019-4e15-be0d-c4b2a75dc784",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XqiwoVg9UABdsjmYu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "958add5e-6a20-4885-8b93-ab624ed21e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018E5uo7UDdef4HuZxQuDP58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 8 · 2026-05-13T19:23:25.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RnqhyVv6fH2Bmcqg1UVzBH`</summary>

```json
{
  "query": "Robometer scaling general-purpose robotic reward models trajectory comparisons RSS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "958add5e-6a20-4885-8b93-ab624ed21e32",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XqiwoVg9UABdsjmYu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28cb6775-7737-4c04-9f0a-edd874dc4b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018E5uo7UDdef4HuZxQuDP58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 9 · 2026-05-13T19:23:25.790Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pmzHfHRDsm1EVBp85j5JM`</summary>

```json
{
  "query": "Robometer github code release robotic reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28cb6775-7737-4c04-9f0a-edd874dc4b5b",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17XqiwoVg9UABdsjmYu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f75ddde-3bc2-4d24-a80d-5340966fe165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018E5uo7UDdef4HuZxQuDP58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9044,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 368,
          "cache_read_input_tokens": 9044,
          "cache_creation_input_tokens": 1906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1906,
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

_source line 10 · 2026-05-13T19:23:32.297Z_

<details><summary>↩ Tool result · `toolu_01CT4ev1wBWBNdJyURy5A5PM`</summary>

```text
# Robometer: Scaling General-Purpose Robotic Reward Models - Details

## 1. Title, Authors & Affiliation
**Title:** "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons"

**Authors:** Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, Jesse Zhang (17 authors total)

**Affiliation:** Not specified in the provided content

---

## 2. Model Architecture Details
Not provided in the web page excerpt. Only mentions training on trajectory data; specific architecture details are absent.

---

## 3. Training Data
- **Dataset:** RBM-1M (reward-learning dataset curated for this work)
- **Size:** "over one million trajectories"
- **Composition:** Diverse robot embodiments, tasks, substantial suboptimal and failure data included
- **Collection method:** Not detailed in excerpt

---

## 4. Scoring Capability
The abstract indicates "trajectory-comparison preference loss that imposes global ordering constraints across trajectories," suggesting comparative assessment, though individual trajectory scoring capability isn't explicitly confirmed.

---

## 5. Mode-Awareness
Not specified. The framework appears to provide a single unified score rather than multiple quality dimensions.

---

## 6. Benchmarks Evaluated
**Not listed in the provided content.** The abstract mentions "across benchmarks and real-world evaluations" but provides no specific benchmark names. RoboMimic usage is not mentioned.

---

## 7. Code/Model Release
"Code, model weights, and videos at [this https URL]" referencing robometer.github.io (exact URL not fully resolved in excerpt)

---

## 8. Inference Speed / Computational Cost
Not provided in the web page content.

---

## 9. Downstream Usage Details
"Improves robot learning performance across a diverse set of downstream applications," but specific integration protocols for RL or filtering aren't detailed in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958add5e-6a20-4885-8b93-ab624ed21e32",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "8dc66493-160e-4dc1-941e-fdd229963e35",
  "sourceToolAssistantUUID": "958add5e-6a20-4885-8b93-ab624ed21e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T19:23:33.385Z_

<details><summary>↩ Tool result · `toolu_01RnqhyVv6fH2Bmcqg1UVzBH`</summary>

```text
Web search results for query: "Robometer scaling general-purpose robotic reward models trajectory comparisons RSS 2026"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"Jiahui Zhang's research works | University of Southern California and other places","url":"https://www.researchgate.net/scientific-contributions/Jiahui-Zhang-2254368611"},{"title":"ROBOMETER: Scaling Robotic Reward Models - YouTube","url":"https://www.youtube.com/watch?v=WBBdgLdncG4"},{"title":"GitHub - philfung/reward-scope: visually compare robot reward functions · GitHub","url":"https://github.com/philfung/reward-scope"}]

I found relevant information about Robometer. Here's what the research shows:

## Overview

Robometer is a general-purpose robotic reward model presented at Robotics: Science and Systems (RSS) 2026, authored by researchers from USC, UT Dallas, MIT, University of Washington, and NVIDIA.

## Key Innovation

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision, trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task.

## Training Data

RBM-1M is a large-scale reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

## Capabilities and Performance

Robometer enables scalable training of rewards on both reward-labeled expert demonstrations and reward-unlabeled, suboptimal trajectories, and provides dense, video-language-conditioned rewards for robot learning. Across benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods and improves robot learning performance across a diverse set of downstream applications.

## Resources

The researchers have made the code, model weights, and datasets publicly available through their GitHub repository and project website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28cb6775-7737-4c04-9f0a-edd874dc4b5b",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "de1b0cac-1c5a-4687-87d6-b31915f4b691",
  "sourceToolAssistantUUID": "28cb6775-7737-4c04-9f0a-edd874dc4b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:23:33.465Z_

<details><summary>↩ Tool result · `toolu_014pmzHfHRDsm1EVBp85j5JM`</summary>

```text
Web search results for query: "Robometer github code release robotic reward model"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"GitHub - philfung/reward-scope: visually compare robot reward functions · GitHub","url":"https://github.com/philfung/reward-scope"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.02115v1"},{"title":"GitHub - FlagOpen/Robo-Dopamine: [CVPR 2026] Official implementation of \"Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation\" · GitHub","url":"https://github.com/FlagOpen/Robo-Dopamine"},{"title":"GitHub - BaiShuanghao/my_arXiv_daily · GitHub","url":"https://github.com/BaiShuanghao/my_arXiv_daily"}]

Based on the search results, here's what I found about Robometer:

## Robometer: Scaling General-Purpose Robotic Reward Models

Robometer is a project about scaling general-purpose robotic reward models via trajectory comparisons, and the code, model weights, and videos are available at https://robometer.github.io/.

### Key Overview

Robometer is a general-purpose, video-language-input, dense reward model trained with a dual reward-prediction objective: a frame-level progress loss on expert data and a preference-prediction loss over trajectory comparisons. It is trained on RBM-1M, a large-scale reward-learning dataset containing over one million trajectories collected from 21 robot platforms.

### The Training Approach

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision. It is trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task, enabling effective learning from both real and augmented failed trajectories.

### The RBM-1M Dataset

RBM-1M is a large-scale reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

### GitHub Repository

The repository contains a main package with data/datasets and preprocessing, Hydra and experiment configs, model definitions, and baseline evaluations, along with a training entrypoint and dependencies managed via uv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f75ddde-3bc2-4d24-a80d-5340966fe165",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "5cdc8bf4-fc7c-4a27-a384-585e9f60df25",
  "sourceToolAssistantUUID": "9f75ddde-3bc2-4d24-a80d-5340966fe165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T19:23:37.023Z_

Good, I have initial information. Now let me fetch the full paper PDF, the GitHub repo, and the project page for more architectural and practical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cdc8bf4-fc7c-4a27-a384-585e9f60df25",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17ZH7CVzG1WaSQ3wZSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9493f6f5-a0ef-4149-b611-9c86f162c268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKztMz1YauyBELEzM68Lse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 10950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
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

_source line 14 · 2026-05-13T19:23:45.653Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TCENHaamc5gGmd3R46kZBp`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.02115v1",
  "prompt": "Extract ALL technical details:\n1. Model architecture: what is the backbone? Is it Qwen2-VL, Qwen3-VL, or something else? What size (4B, 7B, etc.)? \n2. What are the exact inputs? Video frames + language instruction? How many frames? Resolution?\n3. What does the model output? A single scalar reward per frame? Per trajectory?\n4. Training details: loss functions, number of comparisons, batch size, training hardware, training time\n5. ALL benchmarks and datasets used for evaluation - list every single one explicitly. Was RoboMimic, MimicGen, or any MH (multi-human) demonstrations used?\n6. Inference speed: how long does scoring take? Any throughput numbers?\n7. Can it score a single trajectory independently (absolute scoring) or only compare pairs?\n8. Is the reward mode-aware (different quality dimensions like success, fluency, safety) or a single scalar?\n9. Any downstream RL or filtering experiments - what tasks, what improvement?\n10. Code/model availability: exact URLs for GitHub, model weights, datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9493f6f5-a0ef-4149-b611-9c86f162c268",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17ZH7CVzG1WaSQ3wZSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ada23db3-793c-4b55-9d60-8bf04f84d592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKztMz1YauyBELEzM68Lse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 10950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
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

_source line 15 · 2026-05-13T19:23:49.274Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PUJqvoNZVjdioppKwtPWmv`</summary>

```json
{
  "url": "https://github.com/robometer/robometer",
  "prompt": "Extract ALL details from this GitHub repository:\n1. What is the model architecture? Is it based on Qwen2-VL, Qwen3-VL, or another VLM?\n2. What model sizes are available?\n3. How to run inference / score a trajectory? What input format does it expect?\n4. Are model weights released? Where (HuggingFace link)?\n5. What dependencies are needed?\n6. Any benchmarks or evaluation scripts included?\n7. Installation instructions\n8. How to use it as a reward model for filtering or RL?\n9. Any information about inference speed or GPU requirements?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ada23db3-793c-4b55-9d60-8bf04f84d592",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17ZH7CVzG1WaSQ3wZSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c43267d6-14e1-4cb8-8549-fcb3bce5653c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKztMz1YauyBELEzM68Lse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 10950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
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

_source line 16 · 2026-05-13T19:23:51.426Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L1A8kVgzMiZ6iahvxTu9wr`</summary>

```json
{
  "url": "https://robometer.github.io/",
  "prompt": "Extract ALL details from this project page:\n1. Model architecture and size\n2. What inputs does the model take?\n3. What benchmarks was it evaluated on? List all of them.\n4. Code/model release links\n5. Any demo or usage examples\n6. RoboMimic or MimicGen mentions\n7. Any inference speed or computational cost information\n8. Training data details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c43267d6-14e1-4cb8-8549-fcb3bce5653c",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17ZH7CVzG1WaSQ3wZSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4214272-973e-4b53-bbbb-dd34c8ebc187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKztMz1YauyBELEzM68Lse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 10950,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 722,
          "cache_read_input_tokens": 10950,
          "cache_creation_input_tokens": 2655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2655,
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

_source line 17 · 2026-05-13T19:23:58.167Z_

<details><summary>↩ Tool result · `toolu_01PUJqvoNZVjdioppKwtPWmv`</summary>

````text
# Robometer Repository Analysis

## 1. Model Architecture
The documentation does not specify the base VLM architecture (Qwen2-VL, Qwen3-VL, etc.). It only mentions "general-purpose robot reward models" without disclosing the underlying architecture details.

## 2. Model Sizes Available
- **Robometer-4B** (primary general-purpose model)
- **Robometer-LIBERO** (fine-tuned variant for LIBERO-90 tasks)

## 3. Inference / Scoring Trajectories

**Input format:** Video files (mp4) + task description text

**Inference methods:**
- HTTP server approach: `robometer/evals/eval_server.py`
- Local inference: `scripts/example_inference_local.py`

**Output:** Per-frame progress scores, per-frame success predictions, and preference scores between trajectory pairs.

Example command: `--video /path/to/video.mp4 --task "your task description" --fps 3`

## 4. Model Weights Release
Yes, weights are publicly available:
- **Robometer-4B** on Hugging Face: `robometer/Robometer-4B`
- **Robometer-LIBERO** fine-tuned checkpoint also available

## 5. Dependencies
- Python 3.10+
- NVIDIA GPU drivers required
- Package manager: `uv` (recommended)
- Listed in `pyproject.toml` and `requirements-robodopamine.txt`

## 6. Benchmarks & Evaluation Scripts
Included evaluation types:
- Reward alignment testing
- Policy ranking assessment
- Confusion matrix analysis
- Baseline comparisons (ReWIND, Robo-Dopamine, VLAC, RoboReward)

Details in `robometer/evals/run_baseline_eval.py` and `eval_commands/` directory.

## 7. Installation
```
git clone https://github.com/aliang8/robometer.git
cd robometer
uv sync
```

## 8. Use as Reward Model for Filtering/RL
The framework supports:
- Training on custom datasets with trajectory comparison preferences
- LoRA fine-tuning on new data: set `model.use_peft=true`
- Loading from checkpoint: `training.load_from_checkpoint=robometer/Robometer-4B`
- Integration in downstream RL applications

## 9. Inference Speed & GPU Requirements
No specific metrics provided in the documentation. Only prerequisites mention "NVIDIA drivers (GPU)" without detailing VRAM or throughput specifications.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c43267d6-14e1-4cb8-8549-fcb3bce5653c",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "c5df8655-38bc-4478-a772-3394ea205428",
  "sourceToolAssistantUUID": "c43267d6-14e1-4cb8-8549-fcb3bce5653c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T19:24:00.043Z_

<details><summary>↩ Tool result · `toolu_01L1A8kVgzMiZ6iahvxTu9wr`</summary>

```text
# Robometer Project Details

## 1. Model Architecture and Size

The model is a **video-language reward model** available in **4B and 8B parameter versions**. The base model appears to be built on Qwen3-VL architecture.

## 2. Model Inputs

The model accepts:
- **Video trajectories** from robotic demonstrations
- **Language instructions** describing tasks
- Per-frame visual information for dense reward prediction

## 3. Benchmarks and Evaluations

**Offline evaluation benchmarks:**
- RBM-EVAL (in-distribution and out-of-distribution splits)
- RoboRewardBench
- Multiple dataset evaluations: RACER, OXE variants (BC-Z, Berkeley Cable Routing, Bridge V2, Jaco Play, Toto, Viola), Metaworld, Libero (90)
- USC Franka, USC Koch, USC Trossen, USC xArm, MIT Franka, UT Dallas SO101

**Downstream task evaluations:**
- Online RL (single-stage and multi-stage)
- Offline RL with IQL
- Model-based RL with DreamZero
- Failure detection (7 tasks across 7 robot platforms)
- Data retrieval + imitation learning

**Metrics used:** Value Order Correlation (VOC Pearson r), Kendall τ, preference accuracy, MAE

## 4. Code/Model Release Links

- **ArXiv:** https://arxiv.org/abs/2603.02115
- **Code:** https://github.com/robometer/robometer
- **Model Weights:** https://huggingface.co/robometer/Robometer-4B
- **OOD Eval Data:** https://huggingface.co/datasets/robometer/rbm-1m-ood
- **RBM-1M Dataset:** "Coming Soon"

## 5. Demo and Usage Examples

An interactive UI is available at https://robometer-rewardeval-ui.hf.space for "reward model evaluation."

## 6. RoboMimic/MimicGen Mentions

No mentions of RoboMimic or MimicGen appear in the provided content.

## 7. Inference Speed/Computational Cost

The only computational detail provided: LoRA fine-tuning can be performed on "a single GPU" with limited data and compute.

## 8. Training Data Details

**RBM-1M Dataset composition:**
- "1M+ trajectories" across "21 robot embodiments"
- "140,000+ trajectories from mixed expertise datasets"
- Substantial suboptimal and failure data included
- Training uses dual objectives: frame-level progress/success prediction and trajectory-comparison preference prediction
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4214272-973e-4b53-bbbb-dd34c8ebc187",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "2c997f1f-9352-4fe1-aa84-431c12c02c26",
  "sourceToolAssistantUUID": "a4214272-973e-4b53-bbbb-dd34c8ebc187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T19:24:01.501Z_

<details><summary>↩ Tool result · `toolu_01TCENHaamc5gGmd3R46kZBp`</summary>

```text
# Robometer: Technical Details Extraction

## 1. Model Architecture
**Backbone:** Qwen3-VL-4B-Instruct (vision-language model)
**Size:** 4B parameters (also evaluated 8B variant as baseline)
**Type:** Causally masked VLM with inserted learnable tokens

## 2. Exact Inputs
- **Video frames:** Up to 32 frames per trajectory (downsampled for efficiency)
- **Resolution:** Shortest edge resized to 240 pixels, aspect ratio maintained
- **Language instruction:** Task description as text
- **Processing:** Interleaved progress tokens within first video sequence; preference token after dual-video prompt

## 3. Model Outputs
- **Per-frame progress:** Categorical distribution over N bins (continuous estimate via expectation)
- **Per-frame success:** Binary classification (0 until final frame, 1 at completion)
- **Trajectory preference:** Binary classification indicating which of two trajectories better completes task

## 4. Training Details

**Loss Functions:**
- Progress: Cross-entropy over discretized bins (C51 formulation)
- Success: Balanced binary cross-entropy with class weighting
- Preference: Binary cross-entropy via sigmoid

**Data Augmentation Strategies:**
1. Progress-based comparisons (expert vs. failures)
2. Instruction negatives (different tasks)
3. Video rewind (reversing segments to simulate failures)

**Dataset:** RBM-1M containing 1,059,370 trajectories across 21 robot embodiments

**Hardware:** UW Hyak and Tillicum HPC clusters, USC CARC (specific batch sizes/training time not disclosed in excerpt)

## 5. Evaluation Benchmarks & Datasets

**Training Data Sources:**
- Open-X Embodiment (449,475 trajectories)
- AGIBot World (216,911)
- Galaxea Open-World (108,118)
- RoboReward OXE Mix (45,072)
- MolmoACT (15,546)
- Humanoid Everyday (9,208)
- LIBERO (1,709 expert + 1,473 failures)
- MetaWorld (100)
- MotIF (83)
- RH-20T (29,969)
- PH2D (3,596)
- H2R (2,254)
- RoboArena (12,379)
- SOAR (16,812)
- FAILSafe (71,614)
- RACER (29,115)
- AutoEval (8,677)
- Fino-Net (229)
- Epic-Kitchens (37,030)

**Evaluation Datasets:**
- RBM-EVAL-ID: 32,767 trajectories (in-distribution)
- RBM-EVAL-OOD: 976 trajectories from 3 institutions (out-of-distribution)
- RoboRewardBench (external benchmark)
- Custom robot evaluations (USC Franka, Koch Arms, Trossen, MIT Franka, UTD SO-101)

**Note:** No RoboMimic, MimicGen, or multi-human datasets explicitly mentioned.

## 6. Inference Speed
Not specified in document. No throughput or latency numbers provided.

## 7. Scoring Capability
**Dual capability:** Can score single trajectories independently (absolute progress prediction) OR compare trajectory pairs (preference prediction). Progress tokens attend causally to current/previous frames only; preference token attends to both trajectories.

## 8. Reward Dimensionality
Three separate outputs: dense per-frame progress (scalar via categorical distribution), per-frame success (binary), and relative preference (binary). Not mode-aware for different quality dimensions; single scalar progress primary signal.

## 9. Downstream Applications

**Online RL (DSRL):** Single-stage improved from 20% to 85% success; multi-stage from 20% to 70% (2.5× over RoboReward baseline)

**Offline RL (IQL):** 2.4× average success improvement on mixed noisy/expert trajectories

**Data Filtering & Retrieval:** 4.5× higher success rates vs. best baseline for imitation learning

**Failure Detection:** Highest F1 score (0.81 average) for zero-shot detection of irreversible and insufficient-progress failures across 7 tasks

## 10. Code & Model Availability
**Website:** https://robometer.github.io/
**Availability:** "Code, model weights, and videos at [https://robometer.github.io/](https://robometer.github.io/)" (direct quote limited to URL scope)

GitHub and detailed code links not explicitly provided in excerpt, though site references GitHub issue reporting functionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada23db3-793c-4b55-9d60-8bf04f84d592",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "6d872be2-1273-4cbc-9846-37da8690b751",
  "sourceToolAssistantUUID": "ada23db3-793c-4b55-9d60-8bf04f84d592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T19:24:05.273Z_

Now let me get a few more specific details - the HuggingFace model page for exact architecture info, and check if there's any RoboMimic-specific information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d872be2-1273-4cbc-9846-37da8690b751",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17bLiJX7Zv2TKHhjUmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "770a118e-81b2-47fa-9b1c-c1ef224e6055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfEaC8kAQPWEqukzTbMKPk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1309,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 13605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1881,
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

_source line 21 · 2026-05-13T19:24:07.959Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UT26dUnHCxneWyanVnUgSs`</summary>

```json
{
  "url": "https://huggingface.co/robometer/Robometer-4B",
  "prompt": "Extract all details:\n1. What is the exact base model? Qwen2-VL-4B or Qwen3-VL-4B?\n2. Model card details - architecture, training, usage\n3. Any inference speed benchmarks?\n4. Input format requirements\n5. VRAM requirements\n6. Any usage code examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "770a118e-81b2-47fa-9b1c-c1ef224e6055",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17bLiJX7Zv2TKHhjUmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbef2add-3eee-4ba4-98e0-a9e444ad1402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfEaC8kAQPWEqukzTbMKPk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1309,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 13605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1881,
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

_source line 22 · 2026-05-13T19:24:08.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019BMtG9Aw79BaXcGhKQz7Rx`</summary>

```json
{
  "query": "Robometer RoboMimic scoring demonstrations reward model compatibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbef2add-3eee-4ba4-98e0-a9e444ad1402",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17bLiJX7Zv2TKHhjUmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88446d53-e5ba-48f5-a10c-57d8aeec6253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfEaC8kAQPWEqukzTbMKPk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1309,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 13605,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1309,
          "output_tokens": 252,
          "cache_read_input_tokens": 13605,
          "cache_creation_input_tokens": 1881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1881,
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

_source line 23 · 2026-05-13T19:24:14.685Z_

<details><summary>↩ Tool result · `toolu_01UT26dUnHCxneWyanVnUgSs`</summary>

````text
# Robometer-4B Model Details

## 1. Base Model
**Qwen3-VL-4B-Instruct** (not Qwen2-VL-4B)
- Fine-tuned from [Qwen/Qwen3-VL-4B-Instruct](/Qwen/Qwen3-VL-4B-Instruct)
- 265 models have been fine-tuned from this base

## 2. Model Card Details

**Purpose:** General-purpose vision-language reward model for robotics

**Training:**
- Trained on RBM-1M dataset
- Uses frame-level progress supervision on expert data
- Uses trajectory-comparison preference supervision

**Architecture:** Vision-language model (4B parameters, BF16 precision)

**Capabilities:**
- **Per-frame progress**: Continuous progress values (0–1 or binned)
- **Per-frame success**: Success probability at each timestep
- **Preference/ranking**: Compares which of two trajectories is better

## 3. Inference Speed Benchmarks
Not provided in the documentation.

## 4. Input Format Requirements

Takes inputs:
- **Task instruction** (text description)
- **Rollout video** (or frame sequence) (video file path)

## 5. VRAM Requirements
Not specified in the documentation.

## 6. Usage Code Examples

**Option 1 — Local inference:**
```python
from transformers import AutoProcessor, RFM

processor = AutoProcessor.from_pretrained("robometer/Robometer-4B")
model = RFM.from_pretrained("robometer/Robometer-4B")
```

**Option 2 — Local script execution:**
```bash
uv run python scripts/example_inference_local.py \
  --model-path robometer/Robometer-4B \
  --video /path/to/video.mp4 \
  --task "your task description"
```

**Option 3 — Evaluation server:**
```bash
# Start server
uv run python robometer/evals/eval_server.py \
  --config-path=robometer/configs \
  --config-name=eval_config_server \
  model_path=robometer/Robometer-4B \
  server_url=0.0.0.0 \
  server_port=8000

# Client request
uv run python scripts/example_inference.py \
  --eval-server-url http://localhost:8000 \
  --video /path/to/video.mp4 \
  --task "your task description"
```

**Full setup & scripts:** [github.com/robometer/robometer](https://github.com/robometer/robometer)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbef2add-3eee-4ba4-98e0-a9e444ad1402",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "fa5feefa-a47e-4f4c-831b-11596bfbaaf9",
  "sourceToolAssistantUUID": "bbef2add-3eee-4ba4-98e0-a9e444ad1402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T19:24:15.611Z_

<details><summary>↩ Tool result · `toolu_019BMtG9Aw79BaXcGhKQz7Rx`</summary>

```text
Web search results for query: "Robometer RoboMimic scoring demonstrations reward model compatibility"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"robomimic","url":"https://robomimic.github.io/"},{"title":"GitHub - ARISE-Initiative/robomimic: robomimic: A Modular Framework for Robot Learning from Demonstration · GitHub","url":"https://github.com/ARISE-Initiative/robomimic"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.02115"},{"title":"robomimic v0.1 (CoRL 2021) — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/datasets/robomimic_v0.1.html"}]

Based on the search results, here's what I found about Robometer, RoboMimic, scoring demonstrations, and reward model compatibility:

## Robometer: Scaling General-Purpose Robotic Reward Models

Robometer is a general-purpose, video-language-input, dense reward model trained with a dual reward-prediction objective: a frame-level progress loss on expert data and a preference-prediction loss over trajectory comparisons.

### Scoring Demonstrations

For each task (unseen data), Robometer scores all video–instruction pairs, and yields the most diagonal matrix, indicating strong alignment between demos and instructions. Robometer's inference runs a pretrained model on videos to get per-frame progress, per-frame success, and (for two trajectories) preference scores.

### Reward Model Compatibility

Robometer is a general-purpose robotic reward model trained on trajectory comparisons from the RBM-1M dataset and provides dense, video-language-conditioned rewards for robot learning. Robometer significantly improves robot learning performance across a diverse set of downstream applications, including model-free online RL, model-based online RL, offline RL, failure detection, and data retrieval for IL.

### Relationship with RoboMimic

While the search results show that robomimic is a framework for robot learning from demonstration that offers a broad set of demonstration datasets collected on robot manipulation domains and learning algorithms, the specific integration or compatibility between Robometer and RoboMimic datasets is not detailed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88446d53-e5ba-48f5-a10c-57d8aeec6253",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "0f2acc2e-d196-4b8e-99ae-7376c2124f36",
  "sourceToolAssistantUUID": "88446d53-e5ba-48f5-a10c-57d8aeec6253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T19:24:25.793Z_

Let me get the final piece - checking the GitHub README more carefully for inference timing and GPU details, and also checking if there are any benchmarks on the inference side.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f2acc2e-d196-4b8e-99ae-7376c2124f36",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17cP2yd8fiFNTzseKeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6eb035ef-4b8d-4ce2-9a0f-479c195f40d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRhMux82yhHgMtaBodgb4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 15486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 26 · 2026-05-13T19:24:27.216Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FYwAKPYTYqVXgwjPyh39Bh`</summary>

```json
{
  "url": "https://github.com/robometer/robometer/blob/main/scripts/example_inference_local.py",
  "prompt": "Extract the full inference code. What does it do step by step? What format does the video need to be in? How are frames sampled? What is returned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb035ef-4b8d-4ce2-9a0f-479c195f40d8",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17cP2yd8fiFNTzseKeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7532e38-7c1e-4311-b057-9b2eece0d89a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRhMux82yhHgMtaBodgb4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 15486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3098,
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

_source line 27 · 2026-05-13T19:24:29.562Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XBcQK2ZkrXUW7Ji5uHHHju`</summary>

```json
{
  "url": "https://github.com/robometer/robometer/blob/main/README.md",
  "prompt": "Extract ALL details about:\n1. GPU/VRAM requirements\n2. Inference speed or timing\n3. Input format (video format, frame rate, resolution)\n4. How to score individual trajectories\n5. Fine-tuning instructions\n6. Any mention of RoboMimic\n7. Full installation instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7532e38-7c1e-4311-b057-9b2eece0d89a",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17cP2yd8fiFNTzseKeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79aa4dac-2417-4a31-9a10-025a07de17ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRhMux82yhHgMtaBodgb4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 15486,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3098
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 15486,
          "cache_creation_input_tokens": 3098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3098,
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

_source line 28 · 2026-05-13T19:24:32.101Z_

<details><summary>↩ Tool result · `toolu_01FYwAKPYTYqVXgwjPyh39Bh`</summary>

```text
# RBM Inference Code Analysis

## Overall Function
The script loads a Robot Behavior Model from HuggingFace and analyzes video content to generate per-frame progress and success predictions for a specified task.

## Step-by-Step Process

1. **Load frames** from video or array file
2. **Create trajectory data structure** with frames and task instruction
3. **Initialize model** from HuggingFace checkpoint
4. **Run inference** to compute progress and success predictions
5. **Save outputs** as numpy arrays and visualization plot

## Video Input Format

The script accepts multiple formats:
- **Video files**: MP4 or other video formats (via path/URL)
- **NumPy arrays**: `.npy` files with shape (T, H, W, C)
- **NumPy archives**: `.npz` files containing frames

The code expects or converts frames to **uint8 format** (unsigned 8-bit integers for 0-255 pixel values).

## Frame Sampling

Frames are extracted using `extract_frames()` with:
- **fps**: frames per second (default: 1.0)
- **max_frames**: maximum frames to extract (default: 512)

## Returned Outputs

The function returns:
- **progress_array**: per-frame progress predictions (float32)
- **success_array**: per-frame success probabilities (float32)

Additionally, the script saves:
- Rewards `.npy` file
- Success probabilities `.npy` file  
- Combined progress/success visualization as PNG
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7532e38-7c1e-4311-b057-9b2eece0d89a",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "8e89c563-4faa-4353-98ef-21b74d8adcfa",
  "sourceToolAssistantUUID": "e7532e38-7c1e-4311-b057-9b2eece0d89a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T19:24:35.762Z_

<details><summary>↩ Tool result · `toolu_01XBcQK2ZkrXUW7Ji5uHHHju`</summary>

````text
# Robometer Documentation Extract

## 1. GPU/VRAM Requirements
Not specified in the README. Only mentions "NVIDIA drivers (GPU)" as a prerequisite.

## 2. Inference Speed or Timing
No timing information provided in the documentation.

## 3. Input Format
The inference examples show video file inputs with task descriptions. Supported formats demonstrated:
- MP4 video files
- Frame rate: 3 fps mentioned in example commands
- Resolution: Not specified

## 4. Scoring Individual Trajectories
Per the documentation: "run the client" to obtain "per-frame progress, per-frame success, and (for two trajectories) preference scores."

## 5. Fine-tuning Instructions
Complete guide provided via `FINETUNE_ROBOMETER.md`. Key steps outlined:
- **Preprocessing**: "Add your dataset to the preprocess config and run the preprocessor"
- **Fine-tuning**: "Set `model.use_peft=true` and `training.load_from_checkpoint=robometer/Robometer-4B`, then train on your dataset"
- **Upload**: "Use `robometer/utils/upload_to_hub.py` to push checkpoints"

## 6. RoboMimic Mention
No reference to RoboMimic found in the provided content.

## 7. Full Installation Instructions

**Prerequisites**: "Git, Python 3.10+, NVIDIA drivers (GPU), uv (recommended)"

**Main environment**:
```
git clone https://github.com/aliang8/robometer.git
cd robometer
uv sync
```

**Dataset setup**:
```
hf auth
export ROBOMETER_PROCESSED_DATASETS_PATH=/path/to/save/processed_datasets
./scripts/download_processed_datasets.sh
./scripts/untar_processed_datasets.sh
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79aa4dac-2417-4a31-9a10-025a07de17ac",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a19c0e1dbe7cfc9b4",
  "type": "user",
  "uuid": "24b44704-e8ee-415c-917d-02d6c9fe87e6",
  "sourceToolAssistantUUID": "79aa4dac-2417-4a31-9a10-025a07de17ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-13T19:25:31.959Z_

I now have comprehensive information. Here is my consolidated report.

---

## Robometer: Practical Details for Research Proposal

### Paper Identity
- **Title:** "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons"
- **Venue:** RSS 2026, arXiv 2603.02115
- **Authors:** Anthony Liang, Yigit Korkmaz, Jiahui Zhang, + 14 others (USC, UT Dallas, MIT, UW, NVIDIA)

---

### 1. Code/Model Weights: YES, Publicly Released

| Resource | URL |
|---|---|
| GitHub | https://github.com/robometer/robometer |
| Model weights (4B) | https://huggingface.co/robometer/Robometer-4B |
| OOD eval data | https://huggingface.co/datasets/robometer/rbm-1m-ood |
| RBM-1M full dataset | Listed as "Coming Soon" on project page |
| Project page | https://robometer.github.io/ |
| Interactive demo | https://robometer-rewardeval-ui.hf.space |

Installation is straightforward: `git clone` + `uv sync`. Two model variants are available: **Robometer-4B** (general-purpose) and **Robometer-LIBERO** (fine-tuned for LIBERO-90).

---

### 2. Architecture

- **Backbone:** Qwen3-VL-4B-Instruct (confirmed on HuggingFace model card)
- **Size:** 4B parameters, BF16 precision. An 8B variant was evaluated as a baseline but the released model is 4B.
- **Type:** Causal VLM with learnable progress/success/preference tokens inserted into the sequence.

---

### 3. Inputs and Outputs

**Inputs:**
- **Video:** MP4 file, NumPy array (T,H,W,C), or .npz. Shortest edge resized to 240px, aspect ratio preserved. Up to 32 frames per trajectory (downsampled). Default extraction at 3 fps (configurable via `--fps`).
- **Language instruction:** Text string describing the task.

**Outputs (three heads):**
- **Per-frame progress:** Continuous scalar in [0,1] via categorical distribution over N bins (C51-style). This is the dense reward signal.
- **Per-frame success:** Binary probability at each timestep.
- **Trajectory preference:** Binary classification indicating which of two trajectories is better (requires two videos as input).

**Key point:** It CAN score individual trajectories independently (absolute progress + success prediction). It does NOT require paired comparisons at inference time. Paired comparison is an additional capability.

---

### 4. Scoring RoboMimic MH Demos

**Format:** RoboMimic stores demos as HDF5 with image observations as NumPy arrays. Robometer accepts `.npy` arrays with shape `(T, H, W, C)` in uint8, so you would extract the `agentview_image` observations from each demo and pass them directly. No video encoding needed.

**Example inference:**
```python
from transformers import AutoProcessor, RFM
processor = AutoProcessor.from_pretrained("robometer/Robometer-4B")
model = RFM.from_pretrained("robometer/Robometer-4B")
```
Or via CLI:
```bash
uv run python scripts/example_inference_local.py \
  --model-path robometer/Robometer-4B \
  --video /path/to/video.mp4 \
  --task "pick up the can"
```

**Estimated time for 300 MH demos on a single A100:** The paper provides no explicit throughput numbers. However, a 4B VLM processing ~32 frames per trajectory on an A100 (80GB) should run at roughly 1-3 seconds per trajectory for a forward pass (based on comparable Qwen2/3-VL-4B inference benchmarks). For 300 demos, expect approximately **5-15 minutes total** on a single A100. This is a rough estimate -- actual time depends on trajectory length and frame sampling rate.

**VRAM:** Not documented, but Qwen3-VL-4B in BF16 requires ~8-10GB for weights alone. With 32 frames of video context, expect ~16-24GB VRAM. Comfortably fits on an A100-40GB or A100-80GB.

---

### 5. Mode-Awareness vs. Single Score

Robometer provides **three separate output signals**, not a single global score:
1. Dense per-frame **progress** (main reward signal, continuous scalar)
2. Per-frame **success** probability (binary)
3. Pairwise **preference** (when comparing two trajectories)

However, it is **NOT mode-aware** in the sense of separate quality dimensions (e.g., fluency, safety, precision). The progress score is a single scalar capturing task completion progress. It does not decompose quality into multiple factors.

---

### 6. Benchmarks and Evaluation

**Training data (RBM-1M):** 1,059,370 trajectories across 21 robot embodiments, drawn from Open-X Embodiment, AGIBot World, Galaxea, LIBERO, MetaWorld, RH-20T, Epic-Kitchens, FAILSafe, RACER, SOAR, and others.

**Evaluation benchmarks:**
- **RBM-EVAL-ID:** 32,767 in-distribution trajectories
- **RBM-EVAL-OOD:** 976 out-of-distribution trajectories from 3 institutions
- **RoboRewardBench** (external benchmark)
- **Downstream tasks:** Online RL (DSRL), Offline RL (IQL), Model-based RL (DreamZero), failure detection (7 tasks, 7 robots), data retrieval + imitation learning
- **Real-robot evaluations:** USC Franka, Koch Arms, Trossen, xArm, MIT Franka, UTD SO-101
- **Per-dataset eval:** BC-Z, Berkeley Cable Routing, Bridge V2, Jaco Play, Toto, Viola, MetaWorld, LIBERO-90

**RoboMimic was NOT one of the evaluation benchmarks.** There is no mention of RoboMimic or MimicGen anywhere in the paper, project page, or GitHub repo. However, since Robometer accepts arbitrary video+language input in a zero-shot manner, it should generalize to RoboMimic tasks (tabletop manipulation is well within distribution given training on similar domains like LIBERO and MetaWorld).

---

### 7. Key Downstream Results

| Application | Improvement |
|---|---|
| Online RL (single-stage) | 20% -> 85% success |
| Online RL (multi-stage) | 20% -> 70% success (2.5x over RoboReward) |
| Offline RL (IQL) | 2.4x average success improvement |
| Data filtering for IL | 4.5x higher success vs. best baseline |
| Failure detection | 0.81 avg F1 (best among all methods) |

---

### Practical Summary for Your Proposal

Robometer is a strong baseline choice. It is fully open (code + 4B weights on HuggingFace), takes raw video + language instruction as input, and produces dense per-frame reward scores that can be used for trajectory filtering without any task-specific training. Scoring 300 RoboMimic MH demos on a single A100 should take on the order of 5-15 minutes. The main caveat is that RoboMimic was not in its training or evaluation set, so you would be using it zero-shot -- but the model was trained on similar tabletop manipulation domains (LIBERO, MetaWorld, Bridge V2) and is designed for cross-embodiment generalization. Fine-tuning on your specific domain is also supported via LoRA (`model.use_peft=true`).

Sources:
- [arXiv paper](https://arxiv.org/abs/2603.02115)
- [Full HTML paper](https://arxiv.org/html/2603.02115v1)
- [Project page](https://robometer.github.io/)
- [GitHub repository](https://github.com/robometer/robometer)
- [HuggingFace model weights](https://huggingface.co/robometer/Robometer-4B)
- [Interactive demo](https://robometer-rewardeval-ui.hf.space)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b44704-e8ee-415c-917d-02d6c9fe87e6",
  "isSidechain": true,
  "agentId": "a19c0e1dbe7cfc9b4",
  "requestId": "req_011Cb17dsBvBDZBXFi9bL6JF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a7434a4-ddea-4cf5-96de-19e2970238a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iiEXQf9ficdQyis9eQceu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 18584,
      "output_tokens": 2096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2096,
          "cache_read_input_tokens": 18584,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
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
