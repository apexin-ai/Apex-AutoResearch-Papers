# Research conversation: This is a critical question for an ML paper review. I need to understand how VLA models with action chunking predict the

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-afb599c2ddc537543.jsonl`
- **Structured JSON:** [`3beb1f7e188689002b05.json`](../../sessions/3b/3beb1f7e188689002b05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-13T17:44:59.157Z_

This is a critical question for an ML paper review. I need to understand how VLA models with action chunking predict their action chunks, because it determines whether per-position training loss varies across chunk positions.

Search for:

1. "OpenVLA-OFT action chunking implementation" — How does OpenVLA-OFT predict action chunks? Is it autoregressive within the chunk (each action conditions on previous), or does it predict all K actions in parallel from the observation?

2. "action chunking teacher forcing VLA training" — Is there teacher forcing within action chunks during VLA training?

3. "pi0 action prediction mechanism" — How does pi0 predict action chunks (flow matching, parallel)?

4. "ACT action chunking transformer prediction mechanism" — The original ACT paper — does it predict chunks in parallel via CVAE or autoregressively?

5. "action chunk loss per position training" — Any evidence of per-position loss variation during training

6. "prioritized experience replay supervised learning failure" OR "PER doesn't work supervised learning" — Evidence that PER-style methods fail in supervised settings

The key question: In standard VLA action-chunked training (e.g., OpenVLA-OFT), does the model predict all K actions from a single observation (making later positions harder because they're temporally distant from the observation), or does it use teacher forcing within the chunk (making all positions approximately equally difficult)?

This distinction is critical because the paper under review assumes per-position loss varies significantly within chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "bdf8c723-b948-45a7-a98e-aebb1ad6d5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T17:44:59.162Z_

```json
{
  "parentUuid": "bdf8c723-b948-45a7-a98e-aebb1ad6d5b8",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
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
  "uuid": "18733da9-025f-4fb3-b816-f6d9eed3b6c4",
  "timestamp": "2026-05-13T17:44:59.162Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T17:45:02.606Z_



I'll research each of these topics systematically to answer your question about VLA action chunking mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18733da9-025f-4fb3-b816-f6d9eed3b6c4",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz3JhYr7W55U8fzTJqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab3ce1e3-d367-4b4a-842b-24e2ae71d967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej4HqAfmsP6uDpn9YgPdpg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 880,
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

_source line 4 · 2026-05-13T17:45:02.925Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JAb3ESuvcNnP6C6rz5Lonr`</summary>

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
  "parentUuid": "ab3ce1e3-d367-4b4a-842b-24e2ae71d967",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz3JhYr7W55U8fzTJqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44e2b949-7dd5-4f1e-88d0-f331a7a2f917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej4HqAfmsP6uDpn9YgPdpg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 8223,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 880,
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

_source line 5 · 2026-05-13T17:45:02.930Z_

<details><summary>↩ Tool result · `toolu_01JAb3ESuvcNnP6C6rz5Lonr`</summary>

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
  "parentUuid": "44e2b949-7dd5-4f1e-88d0-f331a7a2f917",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "7db118d3-e88a-4cd0-bf43-ace3c517666a",
  "sourceToolAssistantUUID": "44e2b949-7dd5-4f1e-88d0-f331a7a2f917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T17:45:05.875Z_



Now let me search for all the topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db118d3-e88a-4cd0-bf43-ace3c517666a",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz3b72JJEnx9jnjaikt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61a8a4f3-1505-4447-b29e-0bbce51e5b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXwdrARtW3DnwD4niAHnLr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-13T17:45:06.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uu7gzkpbTSU3h1VeqqPcjs`</summary>

```json
{
  "query": "OpenVLA-OFT action chunking implementation how predict action chunks autoregressive parallel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61a8a4f3-1505-4447-b29e-0bbce51e5b5e",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz3b72JJEnx9jnjaikt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ae914ba-40a8-4528-9984-80d6148f4e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXwdrARtW3DnwD4niAHnLr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-13T17:45:13.785Z_

<details><summary>↩ Tool result · `toolu_01Uu7gzkpbTSU3h1VeqqPcjs`</summary>

```text
Web search results for query: "OpenVLA-OFT action chunking implementation how predict action chunks autoregressive parallel"

Links: [{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310"},{"title":"EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation","url":"https://arxiv.org/html/2511.05397"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, I can provide you with comprehensive information about OpenVLA-OFT's action chunking implementation and how it predicts action chunks using both autoregressive and parallel approaches:

## Action Chunking Overview

Parallel decoding and action chunking enable the model to map input embeddings to the predicted output sequence in a single forward pass, unlike autoregressive generation which requires sequential token prediction.

## Parallel Decoding Implementation

The model receives empty action embeddings as input and replaces the causal attention mask with bidirectional attention, allowing the decoder to predict all actions simultaneously. Parallel decoding naturally extends to action chunking: to predict actions for multiple future timesteps, additional empty action embeddings are inserted in the decoder's inputs.

More specifically, the modified architecture receives "empty" action embeddings as input and uses bidirectional attention to predict all actions simultaneously in a single forward pass.

## Comparison with Autoregressive Approach

In the original OpenVLA autoregressive training scheme, the model receives ground-truth action tokens shifted right by one position as input (teacher forcing), with a causal attention mask ensuring the model only attends to current and previous tokens, and at test time, each predicted token is fed back as input for the next prediction.

## Performance Benefits

Parallel decoding and action chunking not only increase throughput but also improve performance significantly, raising average success rates by 14% (absolute) over autoregressive OpenVLA policies, with improvement particularly pronounced in LIBERO-Long, suggesting that action chunking helps capture temporal dependencies and reduce compounding errors.

Additionally, through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ae914ba-40a8-4528-9984-80d6148f4e88",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "b7c51ed2-6152-4395-9b0d-1db787dc80cb",
  "sourceToolAssistantUUID": "1ae914ba-40a8-4528-9984-80d6148f4e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T17:45:16.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGyb9UoW59Ke3LGXvBX8z6`</summary>

```json
{
  "query": "action chunking teacher forcing within chunk VLA training loss per position"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7c51ed2-6152-4395-9b0d-1db787dc80cb",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz4PBhPLCXL34rBifxa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90cbb5b1-3e3d-4ffc-a605-913c9f4a4d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJnwWDXVH1ThkhtrtieqhZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 10518,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 10518,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
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

_source line 10 · 2026-05-13T17:45:25.222Z_

<details><summary>↩ Tool result · `toolu_01KGyb9UoW59Ke3LGXvBX8z6`</summary>

```text
Web search results for query: "action chunking teacher forcing within chunk VLA training loss per position"

Links: [{"title":"Action Chunking for Robotics and AV | Igl's Blog","url":"https://www.maximilianigl.com/blog/action-chunking"},{"title":"Learning Native Continuation for Action Chunking Flow Policies","url":"https://arxiv.org/html/2602.12978"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models","url":"https://arxiv.org/html/2601.14323"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"},{"title":"Dissecting Action Chunking with Transformers (ACT): Precision Imitation Learning for Robotic Manipulation","url":"https://blog.phospho.ai/dissecting-action-chunking-with-transformers-act-precision-imitation-learning-for-robotic-manipulation/"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Mixture of Horizons in Action Chunking","url":"https://timsty1.github.io/moh/"}]

I found several relevant research papers and resources related to action chunking in VLA training. Here's what the search results reveal:

## Key Findings

**Action Chunking Fundamentals:**
Action chunking breaks the shortcut of simply repeating the last action by requiring the policy to predict 2-6 seconds of future actions, forcing it to actually reason about the scene including lanes, other vehicles, traffic signals, to produce a coherent plan.

**Training-Time Continuation (Legato):**
Stable chunked execution requires chunk continuation to be a native, learned property of the policy, which entails per-step guidance and training-inference consistency. Legato is a training-time continuation mechanism for action-chunked flow-based VLA policies.

**Loss Per Position in Action Correction:**
The A2C2 module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

**Teacher Forcing with Loss:**
The CVAE is trained to maximize the log-likelihood of demonstration action chunks, using an L1 reconstruction loss for precise action modeling and a KL-divergence term weighted by a hyperparameter (β) to regularize the encoder.

**Post-Training Approaches:**
An action chunk based on proximal policy optimization (PPO) with behavior cloning using self-collected demonstrations aggregates consecutive actions into chunks to improve temporal consistency of the policy and the density of informative feedback.

The research indicates that action chunking involves computing loss per position within chunks during training, with various approaches to handle transitions and maintain consistency across chunk boundaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90cbb5b1-3e3d-4ffc-a605-913c9f4a4d5f",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "afee832f-8e54-42e9-9520-adc70b5976e6",
  "sourceToolAssistantUUID": "90cbb5b1-3e3d-4ffc-a605-913c9f4a4d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T17:45:27.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019W5R1NAM3dzdYoAJYhgZFV`</summary>

```json
{
  "query": "pi0 action prediction mechanism flow matching parallel chunk prediction architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afee832f-8e54-42e9-9520-adc70b5976e6",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz5E6HX7QibB6ohesdB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be06c606-6c86-4ea6-a5b6-f1d2df9dc3cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KHQW6zqPL4hLBSiJmAGqX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 11524,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 11524,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 945,
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

_source line 12 · 2026-05-13T17:45:35.089Z_

<details><summary>↩ Tool result · `toolu_019W5R1NAM3dzdYoAJYhgZFV`</summary>

```text
Web search results for query: "pi0 action prediction mechanism flow matching parallel chunk prediction architecture"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"},{"title":"Understanding pi0 by Physical Intelligence: A Vision-Language-Action Flow Model for General Robot Control","url":"https://blog.phospho.ai/understanding-p0-by-physical-intelligence-a-vision-language-action-flow-model-for-general-robot-control/"},{"title":"GitHub - AlmondGod/action-diffusion-handbook: From the fundamentals of diffusion to flow matching in pi0 · GitHub","url":"https://github.com/AlmondGod/action-diffusion-handbook"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Demystifying Robotic Foundational Models: Pi0 - TUUL.AI Research","url":"https://tuul.ai/research/pi0-robotic-foundation-model"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.pi.website/download/pi05.pdf"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"}]

Based on the search results, here's information about π0's action prediction mechanism using flow matching and parallel chunk prediction:

## Flow Matching for Action Prediction

π₀ implements action prediction by running flow matching on multiple action tokens in parallel, gaining efficiency from this parallelization since flow matching is an iterative process at inference time. Flow matching is a method inspired by diffusion models to model continuous action distributions.

## Action Chunking and Parallel Prediction

Rather than predicting a single action, π₀ generates a sequence of future actions (A_t = [a_t, a_t+1, ..., a_t+H-1], where H=50), with this chunking approach ensuring smooth, continuous control critical for tasks like folding laundry. 

Flow matching can result in faster inference than autoregressive prediction since it can predict a whole chunk at once—to generate a chunk of 50 actions, the model may need to run only 10 inferences for flow matching, which is faster than decoding 50 steps autoregressively.

## Training Mechanism

During training, given an observation o_t, the model learns to denoise an action chunk A_t from a noisy version A_t^tau, where tau (ranging from 0 to 1) controls the noise level, with the training objective minimizing the difference between the model's predicted vector field and the true denoising vector.

## Architecture Details

The action expert is a transformer model with the same number of layers but smaller embedding dimensions and MLP widths, with suffix tokens going through the action expert transformer while incorporating the KV embeddings from the prefix (computed once then cached).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be06c606-6c86-4ea6-a5b6-f1d2df9dc3cb",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "7e37afe1-f2c5-4700-bb1d-c6b74f02de80",
  "sourceToolAssistantUUID": "be06c606-6c86-4ea6-a5b6-f1d2df9dc3cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T17:45:37.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HRbQroARxbLDcixoJk6Weh`</summary>

```json
{
  "query": "ACT action chunking transformer CVAE parallel prediction mechanism architecture paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e37afe1-f2c5-4700-bb1d-c6b74f02de80",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz5xQVfjze21wesfk4e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51f37867-2e33-42de-9166-c46b5850bb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTpL8uswfTqeoAxQiAVVB4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 12469,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 12469,
          "cache_creation_input_tokens": 998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 998,
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

_source line 14 · 2026-05-13T17:45:46.222Z_

<details><summary>↩ Tool result · `toolu_01HRbQroARxbLDcixoJk6Weh`</summary>

```text
Web search results for query: "ACT action chunking transformer CVAE parallel prediction mechanism architecture paper"

Links: [{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Action Chunking with Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-with-transformer-act"},{"title":"ACT (Action Chunking with Transformers) · Hugging Face","url":"https://huggingface.co/docs/lerobot/act"},{"title":"Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware","url":"https://tonyzhaozh.github.io/aloha/"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"InterACT: Inter-dependency Aware Action Chunking with Hierarchical Attention Transformers for Bimanual Manipulation","url":"https://arxiv.org/html/2409.07914v3"},{"title":"Action-Chunking Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-transformer-act"},{"title":"Dissecting Action Chunking with Transformers (ACT): Precision Imitation Learning for Robotic Manipulation","url":"https://blog.phospho.ai/dissecting-action-chunking-with-transformers-act-precision-imitation-learning-for-robotic-manipulation/"},{"title":"How does ACT (Action Chunking with Transformers) actually work?","url":"https://vizuara.substack.com/p/how-does-act-action-chunking-with"},{"title":"Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer | Masato Kobayashi | 小林 聖人","url":"https://mertcookimg.github.io/bi-act/"}]

Based on the search results, I found comprehensive information about ACT (Action Chunking with Transformers) and its architecture, including details about the CVAE and parallel prediction mechanisms. Here's what I found:

## ACT Architecture Overview

ACT predicts a sequence of actions ("an action chunk") instead of a single action like standard Behavior Cloning. The ACT policy is trained as the decoder of a Conditional VAE (CVAE) and synthesizes images from multiple viewpoints, joint positions, and style variable z with a transformer encoder, then predicts a sequence of actions with a transformer decoder.

## Core Components

The architecture includes 4 encoder layers and 7 decoder layers (deliberately asymmetric — the decoder is deeper because it does more work). ACT uses a transformer-based architecture with three main components: Vision Backbone (ResNet-18 processes images from multiple camera viewpoints), Transformer Encoder (synthesizes information from camera features, joint positions, and a learned latent variable), and Transformer Decoder (generates coherent action sequences using cross-attention).

## CVAE Mechanism

The encoder of CVAE compresses action sequence and joint observation into z, the "style" of the action sequence, and is implemented with a transformer. To handle stochasticity in demonstrations, ACT trains the policy as a Conditional Variational Autoencoder (CVAE), which models the distribution of action sequences conditioned on observations.

## Parallel Prediction & Temporal Ensembling

Parallel Decoding (PD-VLA) eliminates sequential inference bottlenecks by reframing AR chunked decode as a fixed-point system, enabling significant acceleration without retraining or model surgery. Temporal ensembling mechanism averages or exponentially weights overlapping predictions from multiple most-recent chunks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51f37867-2e33-42de-9166-c46b5850bb6a",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "ab8338d3-ef2a-4b38-bbf7-4d9219c663e6",
  "sourceToolAssistantUUID": "51f37867-2e33-42de-9166-c46b5850bb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T17:45:50.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XbEbqLsELtGJjHMEFx57Hu`</summary>

```json
{
  "query": "OpenVLA-OFT parallel decoding bidirectional attention predict all actions simultaneously single forward pass training loss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab8338d3-ef2a-4b38-bbf7-4d9219c663e6",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz6s9G12P8idYqRkPo6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d75044ed-56a2-4ff5-9794-2d5051c3cc34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2G93R1bosU2Hk2UXWkssz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 13467,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1032
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 13467,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1032,
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

_source line 16 · 2026-05-13T17:45:58.242Z_

<details><summary>↩ Tool result · `toolu_01XbEbqLsELtGJjHMEFx57Hu`</summary>

```text
Web search results for query: "OpenVLA-OFT parallel decoding bidirectional attention predict all actions simultaneously single forward pass training loss"

Links: [{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15669v1"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics ...","url":"https://arxiv.org/pdf/2506.07530"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

Based on the search results, here's comprehensive information about OpenVLA-OFT's parallel decoding approach:

## Parallel Decoding with Bidirectional Attention

OpenVLA-OFT enables the model to map input embeddings to the predicted output sequence in a single forward pass by receiving empty action embeddings as input and replacing the causal attention mask with bidirectional attention, allowing the decoder to predict all actions simultaneously.

## Key Technical Details

**Attention Mechanism:** The model replaces teacher-forced action inputs with empty action embeddings that differ only in their positional encoding values, and uses a bidirectional attention mask (instead of causal), enabling the model to leverage all intermediate features non-causally when predicting each element in the action chunk.

**Single Forward Pass:** Instead of sequentially predicting each action token, the modified architecture receives "empty" action embeddings as input and uses bidirectional attention to predict all actions simultaneously in a single forward pass.

## Action Chunking and Training Loss

Parallel decoding naturally extends to action chunking: to predict actions for multiple future timesteps, the model simply inserts additional empty action embeddings in the decoder's inputs.

**Training Objective:** The model implements L1 regression by replacing the decoder's output embedding layer with an MLP action head that directly maps final decoder layer hidden states to continuous action values, and is trained to minimize the mean L1 difference between predicted and ground-truth actions.

## Performance Impact

Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d75044ed-56a2-4ff5-9794-2d5051c3cc34",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "4bbf0d4d-1ba8-42f1-bbf9-a11fc91c42d6",
  "sourceToolAssistantUUID": "d75044ed-56a2-4ff5-9794-2d5051c3cc34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T17:46:01.118Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KNMeNX9wPsQ6uRQRaeDWmG`</summary>

```json
{
  "query": "\"action chunking\" loss variation position within chunk later actions harder predict temporally distant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bbf0d4d-1ba8-42f1-bbf9-a11fc91c42d6",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz7fFfxiHak1SMcxbmy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8c0e11f-f003-4d33-bedf-7904e4ff8792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmUUzGpDq9RxFFuwa17Lfx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 14499,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 14499,
          "cache_creation_input_tokens": 950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 950,
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

_source line 18 · 2026-05-13T17:46:12.739Z_

<details><summary>↩ Tool result · `toolu_01KNMeNX9wPsQ6uRQRaeDWmG`</summary>

```text
Web search results for query: ""action chunking" loss variation position within chunk later actions harder predict temporally distant"

Links: [{"title":"Reinforcement Learning with Action Chunking","url":"https://arxiv.org/html/2507.07969v1"},{"title":"The importance of action chunking in imitation learning | Haonan's blog","url":"https://www.haonanyu.blog/post/action_chunking/"},{"title":"[2507.07969] Reinforcement Learning with Action Chunking","url":"https://arxiv.org/abs/2507.07969"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Action chunking as conditional policy compression - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0010027725001416"},{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"An Introduction to the Action Chunking Transformer","url":"https://radekosmulski.com/how-to-train-your-robot-with-a-transformer/"},{"title":"Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://arxiv.org/html/2408.17355v1"},{"title":"Action Chunking for Robotics and AV | Igl's Blog","url":"https://www.maximilianigl.com/blog/action-chunking"},{"title":"Dissecting Action Chunking with Transformers (ACT): Precision Imitation Learning for Robotic Manipulation","url":"https://blog.phospho.ai/dissecting-action-chunking-with-transformers-act-precision-imitation-learning-for-robotic-manipulation/"}]

I found relevant search results about action chunking. Let me search for more specific information about the loss variation and temporal prediction difficulty across positions within chunks.

Links: [{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"[2507.07969] Reinforcement Learning with Action Chunking","url":"https://arxiv.org/abs/2507.07969"},{"title":"SEAR: Sample Efficient Action Chunking Reinforcement Learning","url":"https://arxiv.org/html/2603.01891v1"},{"title":"Action Chunking for Robotics and AV | Igl's Blog","url":"https://www.maximilianigl.com/blog/action-chunking"},{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Reinforcement Learning with Action Chunking | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/reinforcement-learning-action-chunking"},{"title":"Reinforcement Learning with Action Chunking","url":"https://openreview.net/pdf?id=XUks1Y96NR"},{"title":"Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://arxiv.org/html/2408.17355v1"},{"title":"Reinforcement Learning with Action Chunking | OpenReview","url":"https://openreview.net/forum?id=XUks1Y96NR"},{"title":"Action Chunking Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-transformer-act-84121459-f59e-4f6f-9a4e-0441ed519749"}]

Let me search more specifically for research on loss variation across chunk positions and temporal prediction difficulty.

Links: [{"title":"Real time action chunking for robot policies | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/real-time-action-chunking-for-robot-policies-4636cc085a6a"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"ERP prediction error responses under temporal constraints - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0006899325004287"},{"title":"Action Chunking with Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-with-transformer-act"},{"title":"SEAR: Sample Efficient Action Chunking Reinforcement Learning","url":"https://arxiv.org/html/2603.01891v1"},{"title":"VLA Knows Its Limits","url":"https://arxiv.org/html/2602.21445"},{"title":"Prediction and final temporal errors are used for trial-to-trial motor corrections | Scientific Reports","url":"https://www.nature.com/articles/s41598-019-55560-6"},{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Adaptive Action Chunking for Robotic Imitation Learning","url":"https://www.mdpi.com/2313-7673/11/5/316"}]

Based on my web searches, I found highly relevant information about your query. Let me provide you with what I found:

The search results reveal important insights about action chunking and how prediction difficulty varies across positions within action chunks:

## Key Finding: Later Actions Are Harder to Predict

Research analyzing vision-language-action (VLA) models shows that actions within the same chunk consistently attend to the same vision-language tokens with nearly identical importance, and although the model predicts a temporally extended sequence of future actions, later actions fail to adaptively adjust to environmental changes. Instead, they repeatedly rely on static visual-linguistic features that are informative for early actions but increasingly outdated or misleading for later ones.

## Loss Variation Across Chunk Positions

A documented issue is that "chunk size is too large relative to task dynamics—the policy commits to a plan that's outdated by execution end," indicating that prediction quality degrades as temporal distance increases within a chunk.

## Underlying Challenge

When executing N actions in an open-loop manner, it requires the predicted action sequence to be highly accurate since errors cannot be corrected during execution. This suggests that temporally distant actions within a chunk face compounding prediction difficulties.

Early actions benefit from perceptual contexts, but these contexts become increasingly outdated for later ones as the environment changes, revealing the limited adaptability of the predicted chunks.

This phenomenon represents a fundamental challenge in action chunking: the model struggles to maintain prediction accuracy for temporally distant actions within a chunk because it must rely on fixed initial observations that become less relevant as the temporal horizon extends.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8c0e11f-f003-4d33-bedf-7904e4ff8792",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "4ca1f0b0-0589-4109-bec2-02efd38a9af7",
  "sourceToolAssistantUUID": "d8c0e11f-f003-4d33-bedf-7904e4ff8792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T17:46:15.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MM7tkAZco8Qr5fyh9ofv62`</summary>

```json
{
  "query": "prioritized experience replay supervised learning failure doesn't work imitation learning behavior cloning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca1f0b0-0589-4109-bec2-02efd38a9af7",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz8jHnZ7ej9YKobmb4a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35786def-b66b-49e0-86ca-fa60d6cb2416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA2sURaME49ZSQDcAdNiJ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 15449,
      "output_tokens": 67,
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
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 15449,
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

_source line 20 · 2026-05-13T17:46:22.563Z_

<details><summary>↩ Tool result · `toolu_01MM7tkAZco8Qr5fyh9ofv62`</summary>

```text
Web search results for query: "prioritized experience replay supervised learning failure doesn't work imitation learning behavior cloning"

Links: [{"title":"Optimal Combination of Imitation and Reinforcement ...","url":"https://www.iieta.org/download/file/fid/20991"},{"title":"GitHub - hoangminhle/hierarchical_IL_RL: Code for hierarchical imitation learning and reinforcement learning","url":"https://github.com/hoangminhle/hierarchical_IL_RL"},{"title":"[RL] Imitation Learning with Behavior Cloning (BC)","url":"https://leeyngdo.github.io/blog/reinforcement-learning/2024-02-20-imitation-learning/"},{"title":"Ch. 21 - Imitation Learning - Underactuated Robotics","url":"https://underactuated.mit.edu/imitation.html"},{"title":"Integrating Behavior Cloning and Reinforcement Learning for","url":"https://arxiv.org/pdf/1910.04281"},{"title":"Behavioral Cloning (BC) - imitation","url":"https://imitation.readthedocs.io/en/latest/algorithms/bc.html"},{"title":"[1805.01954] Behavioral Cloning from Observation","url":"https://arxiv.org/abs/1805.01954"},{"title":"Behavioral Cloning: Supervised Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning"},{"title":"Imitation learning - Wikipedia","url":"https://en.wikipedia.org/wiki/Imitation_learning"},{"title":"Combining Imitation Learning and Reinforcement Learning Using DQfD","url":"https://danieltakeshi.github.io/2019/04/30/il-and-rl/"}]

Based on the search results, here's what I found about these topics:

## Prioritized Experience Replay (PER)

Prioritized experience replay stores agent experience in a memory queue ranked using the TD-error criterion, giving the highest probability to transitions with the highest |TD-errors|, since they have the highest potential of learning progress.

## Behavior Cloning and Supervised Learning Issues

Behavioral cloning directly learns a policy by using supervised learning on observation-action pairs from expert demonstrations. It is a simple approach to learning a policy, but the policy often generalizes poorly and does not recover well from errors.

Supervised learning yields successful performance when training and test data distributions match. However, in reinforcement learning, the states derived from the expert policy are not uniformly sampled throughout the entire state space. The learned policy produces its own distribution of states, making it prone to underperform when operating in states distant from the expert distributions, and minor mistakes of the learned agent may lead to severe degradations due to temporal structure in RL.

## Combining PER with Imitation Learning

In the DQfD algorithm, the demonstration data is sampled with prioritization using prioritized experience replay. Additionally, one study showed that a fixed buffer ratio outperforms PER in the sparse reward scenario when used with behavior cloning and reinforcement learning.

The search results suggest that while PER can be used in combination with behavior cloning and reinforcement learning approaches, behavioral cloning itself has fundamental limitations related to distribution shift that aren't directly solved by PER alone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35786def-b66b-49e0-86ca-fa60d6cb2416",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "a544e21a-634d-4969-8603-df65f5b83814",
  "sourceToolAssistantUUID": "35786def-b66b-49e0-86ca-fa60d6cb2416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T17:46:26.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rzu6ie1nzWdqJk5YBcxdTM`</summary>

```json
{
  "query": "OpenVLA-OFT arxiv paper parallel decoding training details empty action tokens bidirectional attention mask L1 loss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a544e21a-634d-4969-8603-df65f5b83814",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011Cazz9TH9fyshwRTenAj6M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6991d66-66c3-4acd-856e-5fe7ba44d85c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tdSgx2qetFHXyJMxZSMCs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 17366,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 17366,
          "cache_creation_input_tokens": 871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 871,
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

_source line 22 · 2026-05-13T17:46:33.629Z_

<details><summary>↩ Tool result · `toolu_01Rzu6ie1nzWdqJk5YBcxdTM`</summary>

```text
Web search results for query: "OpenVLA-OFT arxiv paper parallel decoding training details empty action tokens bidirectional attention mask L1 loss"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models","url":"https://arxiv.org/html/2509.23655v1"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"}]

I found the OpenVLA-OFT arxiv paper and relevant information about the training details. Here's what the search results reveal about the key technical aspects you asked about:

## Parallel Decoding Training Details

Unlike autoregressive generation which requires sequential token prediction, parallel decoding enables the model to map input embeddings to the predicted output sequence in a single forward pass.

## Empty Action Tokens

For parallel decoding, they replace this input with empty action embeddings that differ only in their positional encoding values. This is a key implementation detail that enables efficient parallel prediction.

## Bidirectional Attention Mask

They use a bidirectional attention mask (instead of causal), enabling the model to leverage all intermediate features non-causally when predicting each element in the action chunk. This contrasts with the standard causal masking used in the original OpenVLA's autoregressive training.

## L1 Loss

They implement L1 regression by replacing the decoder's output embedding layer with an MLP action head that directly maps final decoder layer hidden states to continuous action values. The model is trained to minimize the mean L1 difference between predicted and ground-truth actions.

The arxiv paper is "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" (arXiv:2502.19645), and the optimized fine-tuning recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6991d66-66c3-4acd-856e-5fe7ba44d85c",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "a7ac60b9-697c-46b6-ba49-0133b4363798",
  "sourceToolAssistantUUID": "b6991d66-66c3-4acd-856e-5fe7ba44d85c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T17:46:37.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tgepe5fwSS3NMcKzfmRB6u`</summary>

```json
{
  "query": "pi0 flow matching training action chunk denoising all positions simultaneously conditional flow matching loss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ac60b9-697c-46b6-ba49-0133b4363798",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzAGcjKAqd4ZkuWjSBy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4eae288-7388-4b56-9b36-cc3d0f865915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FknKEDctT1YSWnbX7Me3rX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 18237,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 18237,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 932,
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

_source line 24 · 2026-05-13T17:46:44.346Z_

<details><summary>↩ Tool result · `toolu_01Tgepe5fwSS3NMcKzfmRB6u`</summary>

```text
Web search results for query: "pi0 flow matching training action chunk denoising all positions simultaneously conditional flow matching loss"

Links: [{"title":"GitHub - AlmondGod/action-diffusion-handbook: From the fundamentals of diffusion to flow matching in pi0 · GitHub","url":"https://github.com/AlmondGod/action-diffusion-handbook"},{"title":"Flow Matching Explained: From Noise to Robot Actions | Federico Sarrocco","url":"https://federicosarrocco.com/blog/flow-matching"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"Understanding pi0 by Physical Intelligence: A Vision-Language-Action Flow Model for General Robot Control","url":"https://blog.phospho.ai/understanding-p0-by-physical-intelligence-a-vision-language-action-flow-model-for-general-robot-control/"},{"title":"Demystifying Robotic Foundational Models: Pi0 - TUUL.AI Research","url":"https://tuul.ai/research/pi0-robotic-foundation-model"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models","url":"https://arxiv.org/html/2510.25889v1"},{"title":"$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control - samrat's thought space","url":"https://samratsahoo.com/2025/08/28/pi-zero"},{"title":"Training-Time Action Conditioning for Efficient Real-Time Chunking","url":"https://arxiv.org/html/2512.05964"}]

Based on the search results, I found comprehensive information about pi0's flow matching training approach. Here's what the research reveals:

## π0 Flow Matching Training Overview

π0 is a generalist robot foundation model consisting of an "action expert" which uses conditional flow matching to augment a pretrained Vision-Language Model (VLM).

## Action Chunk and Denoising Process

The model learns p(A_t|o_t) where A_T = [a_t, a_{t + 1}, …, a_{t + H - 1}] is an action chunk of future actions with horizon H = 50. 

During training, given an observation o_t, the model learns to denoise an action chunk A_t from a noisy version A_t^tau, where tau (ranging from 0 to 1) controls the noise level.

## Denoising All Positions Simultaneously

The action expert uses full bidirectional attention across action tokens, ensuring coherent sequence generation. This means all positions in the action chunk are processed together rather than sequentially.

## Conditional Flow Matching Loss

The Action Expert is trained specifically with a Flow Matching loss (essentially a Mean Squared Error between predicted and target vector fields) to learn how to generate realistic, continuous action sequences.

More specifically, the target vector field u is defined as: u (A_t^τ|A_t) = ϵ − A_t, where the noisy action A_t^τ = τA_t + (1−τ)ϵ. The training process for flow matching involves perturbing action sequences with noise, here drawn from a shifted beta distribution which emphasizes lower timesteps (i.e., noisier actions).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4eae288-7388-4b56-9b36-cc3d0f865915",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "37f68761-ecf1-4ca7-a670-ca02e73c2b02",
  "sourceToolAssistantUUID": "f4eae288-7388-4b56-9b36-cc3d0f865915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T17:46:47.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVxdxZwy7h55aq16szCo7V`</summary>

```json
{
  "query": "ACT action chunking transformer decoder queries predict all timesteps parallel single forward pass CVAE not autoregressive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f68761-ecf1-4ca7-a670-ca02e73c2b02",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzB4P3noigw7YKVZ8TJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ffcc976-e8cc-450c-b931-6a53e48ee5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XU8hJnPFWr5AiqEKXgkxeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 19169,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 19169,
          "cache_creation_input_tokens": 1048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1048,
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

_source line 26 · 2026-05-13T17:46:54.362Z_

<details><summary>↩ Tool result · `toolu_01WVxdxZwy7h55aq16szCo7V`</summary>

```text
Web search results for query: "ACT action chunking transformer decoder queries predict all timesteps parallel single forward pass CVAE not autoregressive"

Links: [{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"ACT (Action Chunking with Transformers) · Hugging Face","url":"https://huggingface.co/docs/lerobot/act"},{"title":"Action-Chunking Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-transformer-act"},{"title":"Dissecting Action Chunking with Transformers (ACT): Precision Imitation Learning for Robotic Manipulation","url":"https://blog.phospho.ai/dissecting-action-chunking-with-transformers-act-precision-imitation-learning-for-robotic-manipulation/"},{"title":"Action Chunking with Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-with-transformer-act"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware","url":"https://tonyzhaozh.github.io/aloha/"},{"title":"GitHub - KhaledSharif/robot-transformers: Train and evaluate an Action Chunking Transformer (ACT) to perform cooperative robot manipulation tasks","url":"https://github.com/KhaledSharif/robot-transformers"},{"title":"Understanding Action Chunking with Transformers (ACT): A Simple Guide","url":"https://hankyukim.com/act/"},{"title":"An Introduction to the Action Chunking Transformer","url":"https://radekosmulski.com/how-to-train-your-robot-with-a-transformer/"}]

Based on the search results, here's what I found about ACT (Action Chunking with Transformers) and the architectural components you mentioned:

## Key Architectural Points

**Parallel Prediction of All Timesteps:**
The decoder uses standard transformer cross-attention: the positional queries attend to the observation tokens and z, producing k action predictions in parallel. During inference, the chunk is typically produced in one forward pass, but only the first action is executed per step.

**Decoder Queries:**
The decoder takes three inputs: the latent z (or zero at inference), the current observation tokens (from the vision backbone + proprioception), and a set of k learnable positional queries (one per action in the chunk). No ground truth information is passed into the decoder (just the learnable query embeddings) and thus no need for causal masking! For the generation of each action, the decoder can consider both the earlier and subsequent actions it is predicting.

**CVAE Framework:**
ACT uses a CVAE (Conditional Variational Autoencoder) architecture with a transformer backbone. The CVAE structure is purely a training aid that prevents mode collapse — without it, the model tends to average across demonstration styles, producing motions that are the mean of all approaches.

**Non-Autoregressive Design:**
Instead of using causal attention (which would only allow the model to consider the sequence up to t-1 when predicting the action at t), the authors opted to leverage the DETR approach which allows the decoder to reason about the entire output sequence without the limitations of causal masking.

This design enables ACT to predict entire action chunks in a single forward pass, making it fundamentally non-autoregressive at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ffcc976-e8cc-450c-b931-6a53e48ee5af",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "a5d8e8fa-9465-4685-9b0d-5287f736b802",
  "sourceToolAssistantUUID": "8ffcc976-e8cc-450c-b931-6a53e48ee5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T17:46:57.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TCxR6hDGhF9L2XLXXnukZr`</summary>

```json
{
  "query": "\"mixture of horizons\" action chunking per-position loss weighting later actions prediction error"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5d8e8fa-9465-4685-9b0d-5287f736b802",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzBoCX1twWfLhj3RdWK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18ffc1c6-d507-454b-b7d8-9f9923d68043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qw4mP9Uy7AHQj9FdTs61bK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 20217,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 20217,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1004,
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

_source line 28 · 2026-05-13T17:47:04.902Z_

<details><summary>↩ Tool result · `toolu_01TCxR6hDGhF9L2XLXXnukZr`</summary>

```text
Web search results for query: ""mixture of horizons" action chunking per-position loss weighting later actions prediction error"

Links: [{"title":"Mixture of Horizons in Action Chunking","url":"https://arxiv.org/html/2511.19433v1"},{"title":"Mixture of Horizons in Action Chunking","url":"https://timsty1.github.io/moh/"},{"title":"Paper page - Mixture of Horizons in Action Chunking","url":"https://huggingface.co/papers/2511.19433"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Mixture of Horizons in Action Chunking | Request PDF","url":"https://www.researchgate.net/publication/397935119_Mixture_of_Horizons_in_Action_Chunking"},{"title":"Timsty/mixture_of_horizons · Hugging Face","url":"https://huggingface.co/Timsty/mixture_of_horizons"},{"title":"Learning Fine-Grained Bimanual Manipulation with Low- ...","url":"https://www.roboticsproceedings.org/rss19/p016.pdf"},{"title":"Action-Chunking Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-transformer-act"},{"title":"(Preprint) AAS 25-897 ACTION CHUNKING WITH TRANSFORMERS FOR IMAGE-BASED","url":"https://www.arxiv.org/pdf/2509.04628"},{"title":"Bi-ACT: Bilateral Control-Based Imitation Learning Via Action ...","url":"https://ras.papercept.net/images/temp/AIM/files/0129.pdf"}]

I found comprehensive information about "Mixture of Horizons" in action chunking. Here's what the search reveals:

## Overview

Mixture of Horizons (MoH) is a plug-and-play strategy that fuses multiple horizons within a single policy to inherit the strengths of both with minimal training or inference overhead.

## The Core Problem

VLA models' performance is sensitive to the action chunk length (horizon), and a single horizon induces an inherent trade-off between long-term foresight and short-term precision. Longer horizons facilitate structural foresight (beneficial for Goal/Long tasks), whereas shorter horizons ensure precise control (crucial for Spatial/Object tasks).

## The MoH Approach

MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a lightweight linear gate.

## Key Components

**Loss Weighting:** Without the balance loss, the gate head tends to assign higher weights to action chunks with longer horizons, because longer horizons participate in more steps during action mixture, introducing statistical and gradient bias during training. A balance loss is introduced to encourage all horizons are effectively utilized.

**Per-Position Fusion:** A linear gate head with only 2k parameters produces per-step, per-horizon weights to fuse horizon-wise predictions.

## Benefits

MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18ffc1c6-d507-454b-b7d8-9f9923d68043",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "f1f06365-bc6a-4233-83e9-c92ae34e5bdd",
  "sourceToolAssistantUUID": "18ffc1c6-d507-454b-b7d8-9f9923d68043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T17:47:07.731Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018xEEFDkZS8Nkbf6GUzG7B2`</summary>

```json
{
  "query": "bidirectional decoding action chunking prediction error later positions degradation empirical evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1f06365-bc6a-4233-83e9-c92ae34e5bdd",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzCaHfW7SiEzcwRHJCx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f213ee7-d775-4ffe-bc8c-4c93668ff271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RtD1PL9jgYJMcovp22hi2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 21221,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 21221,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 913,
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

_source line 30 · 2026-05-13T17:47:13.581Z_

<details><summary>↩ Tool result · `toolu_018xEEFDkZS8Nkbf6GUzG7B2`</summary>

```text
Web search results for query: "bidirectional decoding action chunking prediction error later positions degradation empirical evidence"

Links: [{"title":"Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://arxiv.org/html/2408.17355v1"},{"title":"Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling","url":"https://arxiv.org/html/2408.17355"},{"title":"Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling | OpenReview","url":"https://openreview.net/forum?id=qZmn2hkuzw"},{"title":"[2408.17355] Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling","url":"https://arxiv.org/abs/2408.17355"},{"title":"Bidirectional Decoding: Action Chunking","url":"https://www.emergentmind.com/papers/2408.17355"},{"title":"Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240817355L/abstract"},{"title":"[2408.17355v1] Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://arxiv.org/abs/2408.17355v1"},{"title":"BIDIRECTIONAL DECODING: IMPROVING ACTION CHUNKING VIA GUIDED TEST-TIME SAMPLING","url":"https://bid-robot.github.io/static/BID_paper.pdf"},{"title":"Bidirectional Decoding","url":"https://bid-robot.github.io/"},{"title":"Bidirectional Decoding: Improving Action Chunking via Closed-Loop Resampling","url":"https://www.farayare.ikit.technology/Bidirectional+Decoding:+Improving+Action+Chunking+via+Closed-Loop+Resampling/HTML-2408.17355"}]

Based on the search results, I found a highly relevant research paper that directly addresses your query. Here's what the research reveals:

## Key Findings on Action Chunking and Prediction Error

Longer action chunks enable a policy to better capture temporal dependencies by taking into account more past states and actions, however, this advantage comes at the cost of exacerbating errors in stochastic environments due to fewer observations of recent states.

## Empirical Evidence

While existing inference methods offer some benefits for closed-loop operations, they lack robustness, with Warmstart yielding mild performance gains but degrading performance on 3 out of 7 tasks, and EMA leading to competitive results yet exhibiting performance drops in 2 tasks.

The performance of EMA degrades significantly as the environment gets more noisy, likely due to the divergence in strategies between consecutive action chunks.

## The Problem with Later Positions

Recent states are often more important to decision making, and therefore the disadvantages of action chunking become pronounced when inferring these recent states becomes difficult, which can happen if the test environment is stochastic.

The research paper "Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling" by Liu and colleagues (published August 2024) provides both theoretical analysis and extensive empirical validation of these phenomena in robot learning from human demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f213ee7-d775-4ffe-bc8c-4c93668ff271",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "13de9598-20b4-4770-b5d7-0b7ac67918a4",
  "sourceToolAssistantUUID": "7f213ee7-d775-4ffe-bc8c-4c93668ff271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T17:47:16.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016t6gDiJ3vNmUHdeSpi4ghB`</summary>

```json
{
  "query": "\"prioritized experience replay\" \"doesn't work\" OR \"fails\" OR \"harmful\" supervised learning OR offline OR \"behavior cloning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13de9598-20b4-4770-b5d7-0b7ac67918a4",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzDDT4jARHoPZycMSZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbcb832d-1e20-45c7-a789-e4f9b4dbc331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZcYxdKLcZSjCKJrDkzrRc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 22134,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22134,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 924,
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

_source line 32 · 2026-05-13T17:47:22.625Z_

<details><summary>↩ Tool result · `toolu_016t6gDiJ3vNmUHdeSpi4ghB`</summary>

```text
Web search results for query: ""prioritized experience replay" "doesn't work" OR "fails" OR "harmful" supervised learning OR offline OR "behavior cloning""

Links: [{"title":"[2007.09569] Understanding and Mitigating the Limitations of Prioritized Experience Replay","url":"https://arxiv.org/abs/2007.09569"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=HBlNGvIicg9"},{"title":"[2302.07741] Prioritized Offline Goal-Swapping Experience Replay","url":"https://ar5iv.labs.arxiv.org/html/2302.07741"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay","url":"https://proceedings.mlr.press/v180/pan22a/pan22a.pdf"},{"title":"Prioritized Experience Replay","url":"https://arxiv.org/pdf/1511.05952"},{"title":"(PDF) OER: Offline Experience Replay for Continual Offline Reinforcement Learning","url":"https://www.researchgate.net/publication/374324757_OER_Offline_Experience_Replay_for_Continual_Offline_Reinforcement_Learning"},{"title":"Prioritized Sequence Experience Replay","url":"https://arxiv.org/pdf/1905.12726"},{"title":"A divided and prioritized experience replay approach for streaming regression - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2215016121003617"},{"title":"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets","url":"https://arxiv.org/html/2110.04698"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"}]

I found several relevant results on your search topic. Here are the key findings:

## Main Finding: Limitations of Prioritized Experience Replay

Prioritized Experience Replay (PER) has been empirically shown to improve sample efficiency across many domains; however, there is little theoretical understanding of why such prioritized sampling helps and its limitations.

## Identified Problems

Two limitations of the prioritized ER method are: 1) outdated priorities and 2) insufficient coverage of the sample space.

A particularly notable finding is that in supervised learning settings, PER is worse than uniform sampling (L2), and the PrioritizedER may not even outperform regular ER.

## Related Research on Offline RL and Behavior Cloning

In the context of offline reinforcement learning and behavior cloning, the prioritized sampling method does not fully address the noisy label and static distribution problems in high-noise datasets.

The search results show that researchers have been actively investigating these issues, with papers like "Understanding and Mitigating the Limitations of Prioritized Experience Replay" (2022) providing theoretical analysis of when and why PER fails.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbcb832d-1e20-45c7-a789-e4f9b4dbc331",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "eaa232a9-cf1f-45a6-a5a9-d65fc6d9b511",
  "sourceToolAssistantUUID": "fbcb832d-1e20-45c7-a789-e4f9b4dbc331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T17:47:25.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nz7UxLPnYHqxxdn1SKtTcN`</summary>

```json
{
  "query": "OpenVLA-OFT training no teacher forcing within action chunk all actions predicted from observation tokens only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa232a9-cf1f-45a6-a5a9-d65fc6d9b511",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzDt2Y2AKVhopxxpRS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8c3a012-2912-4399-8dd7-7c1d19415be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1FzjRooLEULJiym7JkUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 23058,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 842
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 23058,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 842,
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

_source line 34 · 2026-05-13T17:47:32.461Z_

<details><summary>↩ Tool result · `toolu_01Nz7UxLPnYHqxxdn1SKtTcN`</summary>

```text
Web search results for query: "OpenVLA-OFT training no teacher forcing within action chunk all actions predicted from observation tokens only"

Links: [{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://arxiv.org/html/2507.01016v1"},{"title":"OpenVLA: Training Robot Policies by Treating Actions as Language Tokens | Starlog","url":"https://starlog.is/articles/llm-engineering/openvla-openvla/"}]

Based on the search results, I found relevant information about OpenVLA-OFT's training approach regarding teacher forcing and action prediction. Here's what the research shows:

## Training Approach Without Teacher Forcing

OpenVLA-OFT uses parallel decoding and action chunking, where parallel decoding enables the model to map input embeddings to the predicted output sequence in a single forward pass by receiving empty action embeddings as input and replacing the causal attention mask with bidirectional attention, allowing the decoder to predict all actions simultaneously.

This architecture represents a departure from the base OpenVLA's approach. The base OpenVLA model originally employs autoregressive generation of discrete action tokens optimized via next-token prediction, which inherently uses teacher forcing. In contrast, the parallel decoding approach in OpenVLA-OFT eliminates this dependency.

## Action Prediction from Observation Tokens

All input embeddings—visual features, robot state, and language tokens—are concatenated along the sequence dimension before being passed to the decoder, and this unified latent representation enables the model to attend to all available information when generating actions.

To predict actions for multiple future timesteps with action chunking, the model inserts additional empty action embeddings in the decoder's inputs, which are then filled in through the parallel decoding mechanism based on the concatenated observation embeddings.

This design allows OpenVLA-OFT to generate entire action chunks directly from observation tokens without sequential prediction, fundamentally changing how the model learns and generates robot actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8c3a012-2912-4399-8dd7-7c1d19415be3",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "18c5a2af-9887-40b1-904e-47b3b5a7ab9b",
  "sourceToolAssistantUUID": "d8c3a012-2912-4399-8dd7-7c1d19415be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T17:47:35.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JLvBEZjm5eg3nCgzmWjzbg`</summary>

```json
{
  "query": "diffusion policy action chunk predict all actions parallel single observation denoising training loss per timestep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c5a2af-9887-40b1-904e-47b3b5a7ab9b",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzEc67dfAjEnMMVpDpH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a105237-dbf5-43db-8ae5-7e78105a8c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrhTwoiPbamcmM2x4T3oBy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 23900,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 23900,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 892,
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

_source line 36 · 2026-05-13T17:47:42.945Z_

<details><summary>↩ Tool result · `toolu_01JLvBEZjm5eg3nCgzmWjzbg`</summary>

```text
Web search results for query: "diffusion policy action chunk predict all actions parallel single observation denoising training loss per timestep"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"Diffusion Policy Explained. This is a detailed breakdown of the… | by Fotios (Fotis) Lygerakis | Medium","url":"https://medium.com/@ligerfotis/diffusion-policy-explained-14a3075ba26c"},{"title":"Training-Time Action Conditioning for Efficient Real-Time Chunking","url":"https://arxiv.org/html/2512.05964"},{"title":"Imitation Learning Policies | huggingface/lerobot | DeepWiki","url":"https://deepwiki.com/huggingface/lerobot/4.2-act-policy"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC","url":"https://www.roboticscenter.ai/blog/diffusion-policy-robots"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Fast Policy Synthesis with Variable Noise Diffusion Models","url":"https://arxiv.org/html/2406.04806v3"},{"title":"Diffusion Transformer Policy","url":"https://arxiv.org/html/2410.15959v6"},{"title":"Diving into Diffusion Policy with LeRobot","url":"https://radekosmulski.com/diving-into-diffusion-policy-with-lerobot/"}]

Based on the search results, I found comprehensive information about diffusion policy and related concepts:

## Action Chunks and Parallel Prediction

Diffusion Policy predicts a chunk of 16-32 future actions in a single denoising pass. Diffusion policies are trained to predict an action chunk — a sequence of actions a few time steps into the future — to promote temporal consistency.

The Diffusion Transformer structure denoises action token chunks, instead of each single action token, conditioned directly on image observation and instruction tokens by an in-context conditioning style.

## Single Observation Conditioning

The way to condition diffusion policies on observations is by conditioning the denoising (reverse diffusion) processes on the observations. Starting from pure Gaussian noise in action space, the model iteratively denoises it conditioned on the current visual observation and robot state, producing a coherent, high-quality action sequence after 10–100 denoising steps.

## Denoising and Training Loss

During training, for each example in the batch, a random denoising step number is sampled, and a variable amount of noise is added to each example as per the noise scheduler, obtaining the noisy trajectory as input to the U-Net, with the noise that was added or the original trajectories constituting the targets.

The U-Net runs to predict either epsilon prediction or the clean trajectory, using MSE loss, optionally masked where action_is_pad is True.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a105237-dbf5-43db-8ae5-7e78105a8c3c",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "c3b63f1a-9be9-4dfa-b96e-86d5a0d17c0e",
  "sourceToolAssistantUUID": "9a105237-dbf5-43db-8ae5-7e78105a8c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T17:47:45.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VQPxCHW9VJhSRU2woUpSpZ`</summary>

```json
{
  "query": "VLA action chunking training loss increases later positions empirical measurement per-step loss curve"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3b63f1a-9be9-4dfa-b96e-86d5a0d17c0e",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzFNxckK1wNmf9Bwda2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dad18f5-baee-421f-88e6-5c47c0a43cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJ8EGUidTwLCSXWvyjAwaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 24792,
      "output_tokens": 69,
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
          "output_tokens": 69,
          "cache_read_input_tokens": 24792,
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

### Tool result

_source line 38 · 2026-05-13T17:47:51.604Z_

<details><summary>↩ Tool result · `toolu_01VQPxCHW9VJhSRU2woUpSpZ`</summary>

```text
Web search results for query: "VLA action chunking training loss increases later positions empirical measurement per-step loss curve"

Links: [{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"Learning Native Continuation for Action Chunking Flow Policies","url":"https://arxiv.org/html/2602.12978"},{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Mixture of Horizons in Action Chunking","url":"https://timsty1.github.io/moh/"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Efficient VLA Executor","url":"https://www.emergentmind.com/topics/vision-language-action-vla-executor"},{"title":"PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"}]

The search results contain several papers related to VLA (Vision-Language-Action) models and action chunking, but I don't see specific empirical measurements of per-step loss curves showing that training loss increases for later positions within action chunks. 

The results do mention relevant topics:

1. Vision-Language-Action (VLA) models often predict action chunks to improve efficiency and temporal coherence, and researchers have observed that longer horizons degrade fine-grained accuracy, while shorter ones struggle on long-term tasks.

2. Several papers address challenges with action chunking, including Asynchronous Action Chunk Correction (A2C2), which adds a time-aware correction that encodes the index of the base action within the chunk.

However, the search results don't contain specific empirical measurements or loss curves showing that per-step training loss increases systematically at later positions within action chunks. The papers focus more on architectural solutions and inference-time corrections rather than detailed empirical analysis of loss patterns across chunk positions during training. You may need to look directly at the full papers on arXiv or search for more specific technical reports on this phenomenon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dad18f5-baee-421f-88e6-5c47c0a43cc1",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "6d17f354-0e1b-44a8-af5a-b4a9a84b441f",
  "sourceToolAssistantUUID": "3dad18f5-baee-421f-88e6-5c47c0a43cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T17:47:55.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lr4hdB84ZBe8BZdUUqnCU9`</summary>

```json
{
  "query": "\"leave no observation behind\" A2C2 per-position correction action chunk VLA later actions worse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d17f354-0e1b-44a8-af5a-b4a9a84b441f",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzG1yajfES5pqi9o14e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e5eed58-5811-44a8-9ae2-99b9d5aa9cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrHcqRo292751bnyaXyMLA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 25699,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 25699,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 40 · 2026-05-13T17:48:02.790Z_

<details><summary>↩ Tool result · `toolu_01Lr4hdB84ZBe8BZdUUqnCU9`</summary>

```text
Web search results for query: ""leave no observation behind" A2C2 per-position correction action chunk VLA later actions worse"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS","url":"https://www.arxiv.org/pdf/2509.23224"},{"title":"A2C2: Real-Time Action Chunk Correction","url":"https://www.emergentmind.com/topics/asynchronous-action-chunk-correction-a2c2"},{"title":"Training-Time Action Conditioning for Efficient Real-Time Chunking","url":"https://arxiv.org/html/2512.05964"},{"title":"VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots","url":"https://arxiv.org/html/2512.24673"},{"title":"Learning Native Continuation for Action Chunking Flow Policies","url":"https://arxiv.org/html/2602.12978"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"}]

Based on the search results, I found comprehensive information about your query. Here's what the research reveals:

## Leave No Observation Behind: A2C2 Overview

Asynchronous Action Chunk Correction (A2C2) is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk.

## Core Mechanism

The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

## Why It Addresses the Problem

Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. A2C2 preserves the base model's competence while restoring closed-loop responsiveness.

## Key Advantages

- The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).
- On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, the method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay.

This work addresses the critical challenge of maintaining real-time responsiveness in VLA models that use action chunking, by incorporating the latest observations to dynamically correct actions as they execute.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e5eed58-5811-44a8-9ae2-99b9d5aa9cd1",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "bc67e079-7a94-4ee5-9fc6-86eab963d2e9",
  "sourceToolAssistantUUID": "9e5eed58-5811-44a8-9ae2-99b9d5aa9cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-13T17:48:06.273Z_

Now let me get a few more details on the exact OpenVLA-OFT paper and the original OpenVLA autoregressive approach to make a clear contrast.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc67e079-7a94-4ee5-9fc6-86eab963d2e9",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzGqretogBM9kQBkWY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3936c65-bf24-49e9-a3c2-40babd770187",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhXRBvcQrGJXwpTtrbQF9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 26503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 928,
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

_source line 42 · 2026-05-13T17:48:06.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017EKYNtzdrgB1UwA6Z8oPNv`</summary>

```json
{
  "query": "OpenVLA original autoregressive action tokens teacher forcing training causal attention each token conditioned on previous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3936c65-bf24-49e9-a3c2-40babd770187",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzGqretogBM9kQBkWY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4ffb40a-1e23-49df-8da7-20d4937ccfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhXRBvcQrGJXwpTtrbQF9u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 26503,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 26503,
          "cache_creation_input_tokens": 928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 928,
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

_source line 43 · 2026-05-13T17:48:12.145Z_

<details><summary>↩ Tool result · `toolu_017EKYNtzdrgB1UwA6Z8oPNv`</summary>

```text
Web search results for query: "OpenVLA original autoregressive action tokens teacher forcing training causal attention each token conditioned on previous"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"AR-VLA: True Autoregressive Action Expert for Vision–Language–Action Models","url":"https://arxiv.org/html/2603.10126"},{"title":"DEEPTHINKVLA: ENHANCING REASONING CAPA- BILITY OF VISION-LANGUAGE-ACTION MODELS","url":"https://arxiv.org/pdf/2511.15669"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15669"},{"title":"Multi-Token Prediction Needs Registers Anastasios Gerontopoulos1,3","url":"https://openreview.net/pdf?id=WDdBhcwzGe"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"Autoregressive Action Sequence Learning for Robotic Manipulation","url":"https://arxiv.org/html/2410.03132v5"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"Taming Teacher Forcing for Masked Autoregressive Video Generation Deyu Zhou1","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_Taming_Teacher_Forcing_for_Masked_Autoregressive_Video_Generation_CVPR_2025_paper.pdf"}]

I found relevant information about OpenVLA's original training approach. Here's what the search revealed:

## OpenVLA's Original Autoregressive Training Scheme

In the original OpenVLA autoregressive training scheme, the model receives ground-truth action tokens shifted right by one position as input (a setup known as teacher forcing). A causal attention mask ensures the model only attends to current and previous tokens.

More specifically, OpenVLA's original training formulation uses autoregressive prediction of 7 discrete robot action tokens per timestep: 3 for position control, 3 for orientation control, and 1 for gripper control. It employs next-token prediction with cross-entropy loss as its learning objective, similar to language models.

This training approach means that each token is conditioned on all previous tokens in the sequence through the causal attention mechanism, which only allows the model to attend to current and previous positions in the sequence during both training and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4ffb40a-1e23-49df-8da7-20d4937ccfc6",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "88507eb1-62d1-46d8-9454-9a0423f6a7d0",
  "sourceToolAssistantUUID": "d4ffb40a-1e23-49df-8da7-20d4937ccfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-13T17:48:14.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D1LPLgx4zwArkqMMsAqfx2`</summary>

```json
{
  "query": "\"prioritized experience replay\" supervised learning regression worse uniform sampling empirical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88507eb1-62d1-46d8-9454-9a0423f6a7d0",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzHXmVooyxP4JY3CFox",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30ca3d1c-e353-4c2b-97e8-9a259af63b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jn64ULANwmUiPiWfe1aWh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 27431,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 27431,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 918,
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

_source line 45 · 2026-05-13T17:48:20.728Z_

<details><summary>↩ Tool result · `toolu_01D1LPLgx4zwArkqMMsAqfx2`</summary>

```text
Web search results for query: ""prioritized experience replay" supervised learning regression worse uniform sampling empirical"

Links: [{"title":"[2007.09569] Understanding and Mitigating the Limitations of Prioritized Experience Replay","url":"https://arxiv.org/abs/2007.09569"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=HBlNGvIicg9"},{"title":"Beyond Prioritized Replay: Sampling States in Model-Based Reinforcement Learning via Simulated Priorities | OpenReview","url":"https://openreview.net/forum?id=FNSR8Okx8a"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay","url":"https://proceedings.mlr.press/v180/pan22a/pan22a.pdf"},{"title":"Understanding Prioritized Experience Replay","url":"https://danieltakeshi.github.io/2019/07/14/per/"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Prioritized Experience Replay (PER)","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/prioritized-experience-replay"},{"title":"Experience Replay with Random Reshuffling","url":"https://arxiv.org/html/2503.02269v1"},{"title":"(PDF) Prioritized Experience Replay","url":"https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"},{"title":"Prioritized experience replay based on dynamics priority - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10933423/"}]

The search results found relevant research on prioritized experience replay, particularly in relation to supervised learning and regression tasks. Here are the key findings:

## Main Result

In a supervised learning setting, researchers showed the equivalence between the error-based prioritized sampling method for minimizing mean squared error and uniform sampling for cubic power loss. This is an important theoretical finding because it reveals a surprising limitation of prioritized experience replay in supervised learning contexts.

## Empirical Finding

Empirically, uniform experience replay outperformed prioritized experience replay in supervised learning tasks (prioritized L2 regression performed worse than standard L2 with uniform sampling).

## Theoretical Explanation

Researchers provided theoretical insight into why error-based prioritized sampling improves convergence rate upon uniform sampling when minimizing mean squared error during early learning. However, the work also pointed out two limitations of the prioritized ER method: 1) outdated priorities and 2) insufficient coverage of the sample space.

These findings come from a peer-reviewed research paper titled "Understanding and Mitigating the Limitations of Prioritized Experience Replay," which offers both theoretical analysis and empirical validation of when and why prioritized experience replay can be less effective than uniform sampling, particularly in regression tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30ca3d1c-e353-4c2b-97e8-9a259af63b4d",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "afb599c2ddc537543",
  "type": "user",
  "uuid": "074eb5ef-0719-40c8-b3bd-e4e5b7db7c73",
  "sourceToolAssistantUUID": "30ca3d1c-e353-4c2b-97e8-9a259af63b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-13T17:49:31.419Z_

Now I have comprehensive information to provide a thorough answer. Let me compile the findings.

---

Here is a detailed synthesis of my findings across all six topics:

## 1. OpenVLA-OFT: Parallel Prediction, NOT Autoregressive Within Chunks

OpenVLA-OFT predicts **all K actions in parallel from the observation in a single forward pass**. It does NOT use autoregressive decoding within the action chunk. The key architectural changes from the original OpenVLA:

- **Empty action embeddings** replace teacher-forced ground-truth inputs. These embeddings differ only in positional encoding values -- they carry no information about the ground-truth actions.
- **Bidirectional attention mask** replaces the causal attention mask, so each action position can attend to all other positions and all observation tokens simultaneously.
- An **MLP action head** maps decoder hidden states to continuous action values, trained with **mean L1 loss** between predicted and ground-truth actions.

This is a critical distinction: **there is no teacher forcing within the action chunk during training**. Each action position must predict its value solely from the observation tokens (image, language, robot state) and the positional encoding indicating which timestep it corresponds to. The model cannot "cheat" by looking at ground-truth actions at earlier positions within the chunk.

The original base OpenVLA (without OFT) **did** use autoregressive teacher forcing -- ground-truth action tokens shifted right by one position with causal masking, standard next-token prediction with cross-entropy loss. But OpenVLA-OFT fundamentally changed this to parallel decoding.

Paper: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" (arXiv:2502.19645)

## 2. Teacher Forcing Within Chunks: Generally NO for Modern VLA Models

For models using **parallel decoding** (OpenVLA-OFT), **flow matching** (pi0), **diffusion** (Diffusion Policy), or **CVAE** (ACT), there is **no teacher forcing within the action chunk**. All positions are predicted simultaneously from the observation:

- **OpenVLA-OFT**: Empty action embeddings + bidirectional attention; no ground-truth actions provided during training's forward pass through the action head.
- **pi0**: Flow matching denoises the entire chunk simultaneously; the model predicts a vector field for all H=50 action positions at once.
- **Diffusion Policy**: Denoises all 16-32 action positions in parallel, conditioned on the observation.
- **ACT**: Decoder uses learnable positional queries (not ground-truth actions) + cross-attention to observation tokens; explicitly noted that "no ground truth information is passed into the decoder" so there is "no need for causal masking."

The only VLA paradigm that uses teacher forcing within a chunk is the **original autoregressive token-prediction** approach (e.g., base OpenVLA, RT-2), where each action token is predicted conditioned on previous ground-truth tokens during training. But these models typically predict a single timestep's action (e.g., 7 tokens for one action), not a multi-step chunk.

## 3. pi0: Flow Matching, All Positions Simultaneously

pi0 uses **conditional flow matching** to predict action chunks of H=50 timesteps in parallel:

- During training, given observation o_t, the model learns to denoise a noisy action chunk A_t^tau back to the clean chunk A_t, where tau controls noise level. The training loss is MSE between the predicted vector field and the true denoising direction.
- The **action expert** uses **full bidirectional attention** across action tokens, meaning all 50 positions are processed together, not sequentially.
- At inference, the model performs ~10 iterative denoising steps (each processing all 50 positions simultaneously), which is faster than 50 autoregressive steps.
- The noise schedule uses a shifted beta distribution emphasizing lower timesteps (noisier actions), but this is about the *denoising* timestep tau, not about position within the chunk.

Paper: "pi0: A Vision-Language-Action Flow Model for General Robot Control" (arXiv:2410.24164)

## 4. ACT: CVAE, Parallel Prediction via Learnable Queries

ACT predicts entire action chunks in a **single forward pass** using a **non-autoregressive** design:

- The decoder takes **k learnable positional queries** (one per action in the chunk), the latent z from the CVAE, and observation tokens.
- Critically: "No ground truth information is passed into the decoder (just the learnable query embeddings) and thus no need for causal masking! For the generation of each action, the decoder can consider both the earlier and subsequent actions it is predicting."
- This is inspired by DETR (object detection), which similarly uses a set of queries to predict outputs in parallel.
- Training loss: L1 reconstruction loss + KL-divergence regularization (CVAE objective).

The CVAE is a training aid to handle multimodality in demonstrations -- without it, the model averages across demonstration styles. But the prediction mechanism is fundamentally parallel.

Paper: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" (Tony Zhao et al.)

## 5. Per-Position Loss Variation: Indirect Evidence That Later Positions ARE Harder

While I did not find papers that explicitly plot per-position training loss curves across chunk positions, there is strong indirect evidence that **later positions within a chunk are harder to predict**, and multiple papers build on this assumption:

**"Leave No Observation Behind" (A2C2)**: Introduces a correction module that explicitly encodes "the index of the base action within the chunk" as a positional feature, implying that different positions need different corrections. The paper shows +23% improvement on dynamic tasks.

**"Bidirectional Decoding"**: Documents that "recent states are often more important to decision making" and that prediction quality degrades for later positions because the initial observation becomes "outdated" -- errors compound in open-loop execution.

**"Mixture of Horizons"**: Explicitly addresses the trade-off where "longer horizons facilitate structural foresight but shorter horizons ensure precise control," and uses per-position gating to weight predictions from different horizon lengths.

**"VLA Knows Its Limits"**: Research showing VLA models' attention patterns reveal that "later actions fail to adaptively adjust to environmental changes" -- they "repeatedly rely on static visual-linguistic features that are informative for early actions but increasingly outdated or misleading for later ones."

**The key theoretical reason**: In parallel prediction models (OpenVLA-OFT, ACT, Diffusion Policy, pi0), all actions are predicted from the **same single observation**. Later actions in the chunk correspond to timesteps that are temporally further from the observation. Since the environment evolves, predicting actions further into the future from a single snapshot is inherently harder -- the mapping from observation to action becomes more uncertain as temporal distance increases. This should manifest as higher per-position loss for later chunk positions during training.

## 6. PER in Supervised Learning: Evidence It Can Be Harmful

The paper "Understanding and Mitigating the Limitations of Prioritized Experience Replay" (Pan et al., 2022, published at UAI) provides both theoretical and empirical evidence:

- **Theoretical finding**: Error-based prioritized sampling for MSE minimization is mathematically equivalent to uniform sampling with a cubic power loss. This means PER implicitly changes the loss function rather than truly improving optimization.
- **Empirical finding**: In supervised learning (regression) settings, PER performed **worse** than uniform sampling.
- **Two core limitations**: (1) outdated priorities -- the loss landscape changes during training but priorities lag, and (2) insufficient coverage of the sample space -- high-loss samples are oversampled at the expense of others.

In an offline/supervised setting (which is what VLA training is -- behavior cloning from demonstrations), there is no evolving replay buffer or non-stationarity that PER was designed to address. The fixed dataset means priorities become a static reweighting that biases the loss function without the exploration benefit PER provides in online RL.

---

## Answer to Your Critical Question

**In standard VLA action-chunked training (OpenVLA-OFT, ACT, Diffusion Policy, pi0), the model predicts all K actions from a single observation WITHOUT teacher forcing within the chunk.** This is true for all the major paradigms:

- OpenVLA-OFT: empty embeddings + bidirectional attention
- ACT: learnable queries + CVAE, no ground-truth in decoder
- pi0: flow matching denoises all positions simultaneously
- Diffusion Policy: denoises all positions simultaneously

**This means the paper's assumption that per-position loss varies significantly within chunks is architecturally well-founded.** Later positions ARE harder because they must predict actions for timesteps that are temporally more distant from the conditioning observation. Multiple papers implicitly or explicitly build on this observation (A2C2's positional correction, Mixture of Horizons' per-position gating, Bidirectional Decoding's analysis).

The one exception would be if someone were using a purely autoregressive VLA with teacher forcing and multi-step action chunks -- in that case, during *training*, all positions would be approximately equally easy (since each token sees the ground truth for all previous tokens). But at *inference* time, the autoregressive model would still suffer from compounding errors at later positions. This autoregressive-with-teacher-forcing setup is uncommon for action-chunked VLAs; the dominant approaches are all parallel.

Sources:
- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/html/2502.19645v1)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [pi0 Paper (arXiv:2410.24164)](https://arxiv.org/html/2410.24164v1)
- [pi0 PDF](https://www.pi.website/download/pi0.pdf)
- [ACT / ALOHA Paper](https://tonyzhaozh.github.io/aloha/)
- [ACT Policy Explained](https://www.roboticscenter.ai/blog/act-policy-explained)
- [ACT Hugging Face Documentation](https://huggingface.co/docs/lerobot/act)
- [Leave No Observation Behind (A2C2) (arXiv:2509.23224)](https://arxiv.org/html/2509.23224v1)
- [Bidirectional Decoding (arXiv:2408.17355)](https://arxiv.org/html/2408.17355v1)
- [Mixture of Horizons](https://timsty1.github.io/moh/)
- [VLA Knows Its Limits (arXiv:2602.21445)](https://arxiv.org/html/2602.21445)
- [Understanding and Mitigating PER Limitations](https://arxiv.org/abs/2007.09569)
- [PER Limitations (UAI 2022 proceedings)](https://proceedings.mlr.press/v180/pan22a/pan22a.pdf)
- [PD-VLA Parallel Decoding (arXiv:2503.02310)](https://arxiv.org/html/2503.02310v1)
- [Action Chunking Blog Post](https://www.maximilianigl.com/blog/action-chunking)
- [Legato: Learning Native Continuation (arXiv:2602.12978)](https://arxiv.org/html/2602.12978)
- [Training-Time Action Conditioning (arXiv:2512.05964)](https://arxiv.org/html/2512.05964)
- [AR-VLA: True Autoregressive Action Expert](https://arxiv.org/html/2603.10126)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "074eb5ef-0719-40c8-b3bd-e4e5b7db7c73",
  "isSidechain": true,
  "agentId": "afb599c2ddc537543",
  "requestId": "req_011CazzJAYpoTD3Zx3A9XaQi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9926cb0e-7ab2-4eca-aa47-7ee34032444d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nGckY5ha3ENdzHaPnhN3k",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 28349,
      "output_tokens": 2815,
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
          "input_tokens": 1,
          "output_tokens": 2815,
          "cache_read_input_tokens": 28349,
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
