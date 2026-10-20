# Research conversation: I need to research two things for a paper revision: 1. **TTPL (Test-Time Perturbation Learning with Delayed Feedback for

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaadd70e821d54dca.jsonl`
- **Structured JSON:** [`e64fb63bcff8accb5866.json`](../../sessions/e6/e64fb63bcff8accb5866.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-10T20:19:06.225Z_

I need to research two things for a paper revision:

1. **TTPL (Test-Time Perturbation Learning with Delayed Feedback for VLA Models)** - arXiv April 2026. Claims +7.4% on LIBERO via test-time perturbation learning with delayed feedback. I need to understand:
   - What is their exact mechanism? (augmentation + voting? uncertainty estimation?)
   - Do they require environment feedback during deployment?
   - How does their approach compare to simply averaging predictions from augmented views?
   - Search for "TTPL test-time perturbation learning VLA" and fetch the paper.

2. **Test-time augmentation (TTA) for robot manipulation policies** - I need to understand what simple TTA baselines exist:
   - Search "test-time augmentation robot policy manipulation"
   - Search "ensemble augmentation inference robot learning diffusion"
   - What's the state of the art for simple prediction averaging from augmented views?
   - Has anyone compared TTA to more sophisticated filtering methods for robot policies?

3. **Fast-WAM architecture details** - Search for "Fast-WAM world action model" and verify:
   - Does it use flow-matching (velocity field) or diffusion (score)?
   - How many integration steps?
   - Is the code/checkpoint actually released on HuggingFace?
   - Has it been evaluated on LIBERO-Plus anywhere?

Report findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "0b752609-df31-4f61-a0a9-e3f9819ea0fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:19:06.228Z_

```json
{
  "parentUuid": "0b752609-df31-4f61-a0a9-e3f9819ea0fa",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
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
  "uuid": "d5d6f686-3c81-4d01-99e8-0f6c1abb48b1",
  "timestamp": "2026-05-10T20:19:06.228Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T20:19:11.816Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Loj4wU5pPqmS4qoeNBWNYS`</summary>

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
  "parentUuid": "d5d6f686-3c81-4d01-99e8-0f6c1abb48b1",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNCWjEME92b9ZVQb1M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "787fba9f-c43f-4007-9164-f7b207a7141d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKUXcDkaewiHojta9KfAZZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 878,
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

_source line 4 · 2026-05-10T20:19:11.820Z_

<details><summary>↩ Tool result · `toolu_01Loj4wU5pPqmS4qoeNBWNYS`</summary>

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
  "parentUuid": "787fba9f-c43f-4007-9164-f7b207a7141d",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "69a0ec0d-c1e0-4dca-aa55-1cbfb59e058d",
  "sourceToolAssistantUUID": "787fba9f-c43f-4007-9164-f7b207a7141d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T20:19:15.412Z_

I'll research all three topics in parallel with multiple searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69a0ec0d-c1e0-4dca-aa55-1cbfb59e058d",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNcdofNphUCz23E6Cn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "566fd277-7805-42ab-8c5d-47440c2e9564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sUfXAtiLRTai4K5FS6mKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-10T20:19:15.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H5Rr3m49vRw5YhCNXsd3zW`</summary>

```json
{
  "query": "TTPL test-time perturbation learning VLA delayed feedback arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "566fd277-7805-42ab-8c5d-47440c2e9564",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNcdofNphUCz23E6Cn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfce4734-f225-45de-bf0f-678a5e4bc7bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sUfXAtiLRTai4K5FS6mKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-10T20:19:16.404Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017BGookAXkm9nHoq6iSc2EA`</summary>

```json
{
  "query": "test-time augmentation robot policy manipulation prediction averaging 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfce4734-f225-45de-bf0f-678a5e4bc7bd",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNcdofNphUCz23E6Cn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d12ec5c5-a8c1-430a-85fc-0655939456b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sUfXAtiLRTai4K5FS6mKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-10T20:19:16.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01538FfYvuaU3QKZ9giuTbZx`</summary>

```json
{
  "query": "ensemble augmentation inference robot learning diffusion policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d12ec5c5-a8c1-430a-85fc-0655939456b8",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNcdofNphUCz23E6Cn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89683037-810e-41fe-8c06-d66ced098be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sUfXAtiLRTai4K5FS6mKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9101,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 221,
          "cache_read_input_tokens": 9101,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

### Tool call

_source line 9 · 2026-05-10T20:19:16.940Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013M5TgPcWYK6U6Y1tEBgxx8`</summary>

```json
{
  "query": "Fast-WAM world action model flow matching robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89683037-810e-41fe-8c06-d66ced098be4",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWNcdofNphUCz23E6Cn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bf1dc0f-0312-467a-8840-51d3f8df7022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sUfXAtiLRTai4K5FS6mKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9101,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 221,
          "cache_read_input_tokens": 9101,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-10T20:19:22.585Z_

<details><summary>↩ Tool result · `toolu_013M5TgPcWYK6U6Y1tEBgxx8`</summary>

```text
Web search results for query: "Fast-WAM world action model flow matching robot"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"World Action Models are Zero-shot Policies (arXiv:2602.15922v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2602.15922"},{"title":"World Action Models as Zero-Shot Policies","url":"https://www.emergentmind.com/papers/2602.15922"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"}]

Here's what I found about Fast-WAM, the world action model using flow matching for robotics:

## Overview

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time. World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action.

## Training and Architecture

Fast-WAM is trained with a joint flow matching objective over action tokens and future video latents. Fast-WAM is built on a pretrained video Diffusion Transformer backbone and an action expert DiT. During training, it jointly learns action prediction and video modeling so the shared visual backbone acquires stronger world-grounded representations.

## Key Finding

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. This suggests that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

## Performance

Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining. Notably, it runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bf1dc0f-0312-467a-8840-51d3f8df7022",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "e9ea2708-57bc-4d0f-9986-b45449f0cfdb",
  "sourceToolAssistantUUID": "9bf1dc0f-0312-467a-8840-51d3f8df7022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:19:22.731Z_

<details><summary>↩ Tool result · `toolu_01H5Rr3m49vRw5YhCNXsd3zW`</summary>

```text
Web search results for query: "TTPL test-time perturbation learning VLA delayed feedback arXiv 2026"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"Test-Time Learning for Large Language Models","url":"https://arxiv.org/html/2505.20633v1"},{"title":"Test-Time Adaptation for Tactile-Vision-Language Models","url":"https://arxiv.org/html/2602.15873v1"},{"title":"Reinforcement Learning for Control Systems with Time Delays: A Comprehensive Survey","url":"https://arxiv.org/html/2602.00399v1"},{"title":"[2505.20633] Test-Time Learning for Large Language Models","url":"https://arxiv.org/abs/2505.20633"},{"title":"Paper page - TTRL: Test-Time Reinforcement Learning","url":"https://huggingface.co/papers/2504.16084"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models

The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.

**Key Features:**

PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.

**Performance:**

Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.

**arXiv Details:**

The paper was published on arXiv as **2604.18107** on April 20, 2026, and the code is available according to the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfce4734-f225-45de-bf0f-678a5e4bc7bd",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "0a812165-0379-4030-befa-691a92d9a056",
  "sourceToolAssistantUUID": "cfce4734-f225-45de-bf0f-678a5e4bc7bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:19:22.940Z_

<details><summary>↩ Tool result · `toolu_017BGookAXkm9nHoq6iSc2EA`</summary>

```text
Web search results for query: "test-time augmentation robot policy manipulation prediction averaging 2025 2026"

Links: [{"title":"[2502.00622] Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling","url":"https://arxiv.org/abs/2502.00622"},{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v1"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | OpenReview","url":"https://openreview.net/forum?id=c0dhw1du33"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"GitHub - BaiShuanghao/Awesome-Robotics-Manipulation: A comprehensive list of papers about Robot Manipulation, including papers, codes, and related websites. · GitHub","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"}]

I found several relevant research papers on robot policy and manipulation from 2025-2026. Here are the key findings:

## Recent Research on Robot Policies and World Modeling (2025-2026)

Generative Predictive Control (GPC) is an inference-time method for improving pretrained behavior-cloning policies without retraining, which augments a frozen diffusion policy at deployment with an action-conditioned world model trained on expert demonstrations and random exploration rollouts.

DreamZero, a World Action Model approach, unlocks new generalization capabilities beyond traditional VLAs across environments, tasks, and embodiments.

Video diffusion models demonstrate the ability to predict future frames and understanding of the physical world, and the Video Prediction Policy (VPP) learns implicit inverse dynamics models conditioned on predicted future representations inside VDMs.

MotuBrain, an advanced World Action Model for robot control, achieves strong results on WorldArena benchmarks and can be adapted to new humanoid embodiments with minimal trajectories, suggesting unified world action models can scale in generality, controllability, and real-world deployability.

The research shows a shift toward leveraging world models and predictive capabilities at inference time to improve robot manipulation policies, with recent work in 2025-2026 focusing on test-time adaptation and prediction-based refinement methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d12ec5c5-a8c1-430a-85fc-0655939456b8",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "eec54c05-a8bb-4a0a-90de-392dcb6e3950",
  "sourceToolAssistantUUID": "d12ec5c5-a8c1-430a-85fc-0655939456b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:19:24.750Z_

<details><summary>↩ Tool result · `toolu_01538FfYvuaU3QKZ9giuTbZx`</summary>

```text
Web search results for query: "ensemble augmentation inference robot learning diffusion policy"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation","url":"https://arxiv.org/html/2410.14868v1"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"GitHub - mbreuss/diffusion-literature-for-robotics: Summary of key papers and blogs about diffusion models to learn about the topic. Detailed list of all published diffusion robotics papers. · GitHub","url":"https://github.com/mbreuss/diffusion-literature-for-robotics"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"}]

Based on the web search results, here's what I found about ensemble augmentation inference in robot learning with diffusion policies:

## Diffusion Policy Overview

Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process. The policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps.

## Data Augmentation

Many methodologies employ diffusion-based data augmentation in vision-based manipulation tasks to scale up datasets and reconstruct scenes. Diffusion models for scene and image augmentation lie at the intersection of robotics and computer vision for vision-based tasks to enhance generalizability and data scarcity.

## Ensemble Methods for Inference

Regarding ensemble approaches, ensemble methods for robot-gated DAgger effectively distinguish in-distribution uni-modal from out-of-distribution data using action variance, though they fail at in-distribution multi-modal points due to policy disagreement. 

Diff-DAgger uses a single policy, reducing the wall clock time for both training and inference by the factor of the number of policies used for ensemble. In fact, Diff-DAgger reduced training time by a factor of 5.1, threshold setting time by a factor of 24.5, and inference time by a factor of 5.3 compared to Ensemble-DAgger.

## Key Advantages

The diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89683037-810e-41fe-8c06-d66ced098be4",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "48ec9d24-2d8f-4981-a35a-d6fb78f9a05f",
  "sourceToolAssistantUUID": "89683037-810e-41fe-8c06-d66ced098be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T20:19:30.912Z_

Now let me fetch more details from the TTPL paper and Fast-WAM paper, and search for more specific information on TTA baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ec9d24-2d8f-4981-a35a-d6fb78f9a05f",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWPbrCdU6foRHYzLeq6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "187e474d-69f7-4251-8fa9-9290498b66d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkJgUSEVTmYumcyRSaC925",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 868,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 10989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 15 · 2026-05-10T20:19:35.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012gDfwLuQPMee84v4qx4NGz`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.18107",
  "prompt": "Extract the full technical details of the method:\n1. What is the exact mechanism of the perturbation learning? Is it augmentation + voting?\n2. How does the uncertainty estimation work?\n3. Does the method require environment feedback during deployment? What kind of delayed feedback?\n4. How does it compare to simply averaging predictions from augmented views (naive TTA baseline)?\n5. What are the ablation results - what contributes most to the +7.4% gain on LIBERO?\n6. What is the \"adaptive scheduler\" and how does the augmentation budget work?\n7. What is the lightweight perturbation module?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187e474d-69f7-4251-8fa9-9290498b66d0",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWPbrCdU6foRHYzLeq6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df73a227-99f8-497c-bb1b-4142d32bf204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkJgUSEVTmYumcyRSaC925",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 868,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 10989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 16 · 2026-05-10T20:19:38.531Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WUjExbG9dN4gxna1vCGD8q`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.16666v1",
  "prompt": "Extract details about Fast-WAM:\n1. Does it use flow-matching (velocity field) or diffusion (score-based)?\n2. How many integration/denoising steps at inference?\n3. Is the code or checkpoint released? Is there a HuggingFace link?\n4. Has it been evaluated on LIBERO-Plus?\n5. What are the exact LIBERO benchmark results?\n6. What is the architecture - DiT backbone details?\n7. What is the training objective formula?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df73a227-99f8-497c-bb1b-4142d32bf204",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWPbrCdU6foRHYzLeq6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "886571cd-ff7d-45ff-a18b-f7253899347f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkJgUSEVTmYumcyRSaC925",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 868,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 10989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 17 · 2026-05-10T20:19:39.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GnnSeD2qMwQQeTA8y3JsDt`</summary>

```json
{
  "query": "\"test-time augmentation\" averaging predictions robot policy baseline comparison filtering 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "886571cd-ff7d-45ff-a18b-f7253899347f",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWPbrCdU6foRHYzLeq6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e86565b-8b28-4ee0-b620-0c0e4bc71836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkJgUSEVTmYumcyRSaC925",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 868,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 10989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 18 · 2026-05-10T20:19:39.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZ2c9q53M9UqD3Nz37N4qP`</summary>

```json
{
  "query": "TTPL PDF verifier-free test-time adaptation VLA action voting augmentation budget"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e86565b-8b28-4ee0-b620-0c0e4bc71836",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWPbrCdU6foRHYzLeq6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "211dee06-1f3b-4914-aa37-1893298c192f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkJgUSEVTmYumcyRSaC925",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 868,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 10989,
      "output_tokens": 537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2815
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 868,
          "output_tokens": 537,
          "cache_read_input_tokens": 10989,
          "cache_creation_input_tokens": 2815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2815,
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

_source line 19 · 2026-05-10T20:19:44.432Z_

<details><summary>↩ Tool result · `toolu_01WUjExbG9dN4gxna1vCGD8q`</summary>

```text
# Fast-WAM: Key Technical Details

## 1. Flow-Matching (Velocity Field)
Fast-WAM uses **flow-matching**, not diffusion. The paper states: "The model is trained to predict the corresponding velocity field with a standard flow matching objective" using interpolated samples and velocity prediction rather than score-based approaches.

## 2. Inference Steps
**10 denoising steps** with classifier-free guidance (CFG) scale of 1.0, as specified in the implementation details section.

## 3. Code/Checkpoint Release
The paper provides a project website (https://yuantianyuan01.github.io/FastWAM/) but does not explicitly mention code release, GitHub repositories, or HuggingFace model availability in this HTML version.

## 4. LIBERO-Plus Evaluation
Not evaluated on LIBERO-Plus. The benchmark only covers standard LIBERO suites: Spatial, Object, Goal, and Long.

## 5. LIBERO Results
Fast-WAM achieves **97.6% average success rate**:
- Spatial: 98.2%
- Object: 100.0%
- Goal: 97.0%
- Long: 95.2%

This was accomplished without embodied pretraining.

## 6. Architecture
Built on Wan2.2-5B backbone with a Mixture-of-Transformer (MoT) design: "5B parameter video DiT and 1B action expert," totaling 6B parameters. Action horizon is 32 steps with 9 video frames per chunk.

## 7. Training Objective
Unified flow-matching loss: **L = L_act + λL_vid**, where both action and video losses follow the same velocity field prediction framework across their respective token types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "886571cd-ff7d-45ff-a18b-f7253899347f",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "3c6640ff-6561-43e9-a928-7e953798d8b5",
  "sourceToolAssistantUUID": "886571cd-ff7d-45ff-a18b-f7253899347f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T20:19:46.360Z_

<details><summary>↩ Tool result · `toolu_012gDfwLuQPMee84v4qx4NGz`</summary>

```text
# Technical Details of PDF (Perturbation Learning with Delayed Feedback)

## 1. Perturbation Learning Mechanism

The approach combines data augmentation with voting and learned logit perturbations. The final logits are computed as:

**z̃ₜ = hϕ(fₜ) + λhθ(fₜ)**

where hϕ produces decision logits from the frozen VLA, and hθ (the trainable perturbation head) generates learnable adjustments. "The resulting final logits z̃ₜ are detokenized into a set of candidate actions, from which the final action aₜ is then selected through majority voting."

## 2. Uncertainty Estimation

Uncertainty uses normalized Shannon entropy of the predicted action distribution:

**𝒰ₜ = -1/log K ∑ p(aₖ|sₖ) log p(aₖ|sₖ)**

This quantifies model decision confidence across possible action tokens.

## 3. Environment Feedback Requirement

Yes, the method requires delayed feedback during deployment. "Upon task completion, the agent receives delayed feedback signals rᵢ ∈ ℛ, i ∈ [1,T], which encapsulate task completion status or reward information." This feedback is episodic (end-of-episode), not per-step.

## 4. Comparison to Naive Averaging

The paper doesn't explicitly compare against simple prediction averaging. However, PDF adds: (1) adaptive augmentation budgeting, and (2) learned perturbation corrections guided by feedback, which goes beyond naive averaging.

## 5. Ablation Results on LIBERO

Key findings from Table 2:
- **Full PDF**: 0.89 success rate on Spatial (+0.04 over baseline)
- **Without Delayed Feedback (DF)**: Major performance drops (0.50 on Object suite)
- **Without Data Augmentation (DA)**: Modest degradation

The paper states: "The synergy between DF and DA is evident. The full PDF model outperforms both variants and yields more stable results."

## 6. Adaptive Scheduler & Augmentation Budget

The augmentation budget adapts to uncertainty:

**Nₜ = Nₘₐₓ · 𝒰ₜ**

"Augmented observations are generated by applying transformations adaptively determined by the model's uncertainty." Higher uncertainty triggers more augmented views (up to Nₘₐₓ = 3). Figure 5 shows excessive augmentation degrades performance.

## 7. Lightweight Perturbation Module

The P head hθ is a small learnable network (9M parameters total for the entire PDF system). It optimizes via:

**ℒₚ𝒟𝓕 = -(r-b) log πϕ + λₖₗ 𝕀[r>b] KL(πϕ ∥ π̃)**

"Only the P head hθ is updated; all other VLA parameters remain frozen for efficient, stable test-time adaptation." The REINFORCE term increases likelihood when feedback exceeds baseline; KL regularization prevents excessive divergence when feedback is positive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df73a227-99f8-497c-bb1b-4142d32bf204",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "bb36d441-1540-4d01-b42d-ed0cb0a2b3ba",
  "sourceToolAssistantUUID": "df73a227-99f8-497c-bb1b-4142d32bf204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T20:19:46.372Z_

<details><summary>↩ Tool result · `toolu_01GnnSeD2qMwQQeTA8y3JsDt`</summary>

```text
Web search results for query: ""test-time augmentation" averaging predictions robot policy baseline comparison filtering 2025"

Links: [{"title":"Feature Augmentation based Test-Time Adaptation Younggeol Cho* Youngrae Kim*","url":"https://openaccess.thecvf.com/content/WACV2025/papers/Cho_Feature_Augmentation_Based_Test-Time_Adaptation_WACV_2025_paper.pdf"},{"title":"MEMO: Test Time Robustness via Adaptation and Augmentation","url":"https://openreview.net/pdf?id=vn74m_tWu8O"},{"title":"Greedy Policy Search: A Simple Baseline for Learnable Test-Time Augmentation","url":"https://proceedings.mlr.press/v124/lyzhov20a.html"},{"title":"Test-Time Augmentation for Cross-Domain Leukocyte Classification via OOD Filtering and Self-Ensembling - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12470409/"},{"title":"EDAS: Effective Data Augmentation Strategies for test-time adaptation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525001110"},{"title":"MEMO: Test Time Robustness via Adaptation and Augmentation","url":"https://arxiv.org/pdf/2110.09506"},{"title":"Greedy Policy Search: A Simple Baseline for Learnable Test-Time Augmentation | DeepAI","url":"https://deepai.org/publication/greedy-policy-search-a-simple-baseline-for-learnable-test-time-augmentation"},{"title":"How to Use Test-Time Augmentation to Make Better Predictions - MachineLearningMastery.com","url":"https://machinelearningmastery.com/how-to-use-test-time-augmentation-to-improve-model-performance-for-image-classification/"},{"title":"MEMO: Test Time Robustness via Adaptation and Augmentation | OpenReview","url":"https://openreview.net/forum?id=XrGEkCOREX2"},{"title":"In Search of Lost Online Test-Time Adaptation: A Survey | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-024-02213-5"}]

I found several relevant papers and resources on test-time augmentation. Here's what the search results reveal:

## Key Findings

**Core Concept of Test-Time Augmentation:**
Test-time data augmentation—averaging the predictions of a machine learning model across multiple augmented samples of data—is a widely used technique that improves the predictive performance.

**Recent Approaches (2025 and Later):**

Test-time adaptation (TTA) is a method of updating model parameters during inference using only unlabeled test data, though data augmentation may not function effectively in TTA settings due to discrepancies between predictions using original and augmented samples. A novel approach employs selected augmentations with distinct adaptation strategies customized for each transformation.

**Filtering and Prediction Quality:**
Test-time augmentation can solve the domain shift issue and improve robustness by aggregating predictions from multiple augmented versions of the same input, however, TTA may inadvertently generate unrealistic or Out-of-Distribution (OOD) samples that negatively affect prediction quality.

**Aggregation Methods:**
Test-time Augmentation applies data augmentations to input data during inference, creating multiple variations of the same test sample, and the final prediction typically aggregates these predictions through averaging or majority voting.

The search results include recent 2025 research on effective data augmentation strategies for test-time adaptation and methods addressing OOD filtering issues in test-time augmentation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e86565b-8b28-4ee0-b620-0c0e4bc71836",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "1adf7425-bb62-4320-92d3-726529fd95c6",
  "sourceToolAssistantUUID": "5e86565b-8b28-4ee0-b620-0c0e4bc71836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T20:19:47.262Z_

<details><summary>↩ Tool result · `toolu_01JZ2c9q53M9UqD3Nz37N4qP`</summary>

```text
Web search results for query: "TTPL PDF verifier-free test-time adaptation VLA action voting augmentation budget"

Links: [{"title":"Verifier-free Test-Time Sampling for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=UD4Rw8MOEK"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2603.02203"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/399707107_On-the-Fly_VLA_Adaptation_via_Test-Time_Reinforcement_Learning"},{"title":"[2510.10975] RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10975"},{"title":"WorldAgen: Unified State-Action Prediction with Test-Time World Model Training","url":"https://openreview.net/pdf?id=egbFo1gvYp"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=o3HYrfai5D"},{"title":"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10975v2"},{"title":"VLA-Reasoner: Empowering Vision-Language-Action Models with","url":"https://arxiv.org/pdf/2509.22643"},{"title":"(PDF) Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://www.researchgate.net/publication/398269618_Steering_Vision-Language-Action_Models_as_Anti-Exploration_A_Test-Time_Scaling_Approach"}]

Based on the search results, here's what I found related to your query about test-time adaptation and VLA (Vision-Language-Action) methods:

## Key Research Papers Found

The search returned several relevant papers on test-time scaling and adaptation for Vision-Language-Action models:

### 1. **Verifier-free Test-Time Sampling**
A novel framework called Masking Distribution Guided Selection (MG-Select) proposes a test-time scaling approach for VLAs that leverages the model's internal properties without requiring additional training or external modules, utilizing KL divergence from a reference action token distribution as a confidence metric for selecting optimal actions from multiple candidates.

### 2. **RoVer: Robot Reward Model as Test-Time Verifier**
RoVer is a test-time scaling framework that uses a Robot Process Reward Model (PRM) as a Test-Time Verifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. By caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget.

### 3. **Test-Time Reinforcement Learning (TT-VLA)**
TT-VLA is a framework that enables on-the-fly policy adaptation during inference, formulating a dense reward mechanism that leverages step-by-step task-progress signals to refine action policies during test time while preserving the SFT/RL-trained priors.

### 4. **TACO: Anti-Exploration Test-Time Scaling**
TACO is a test-time-scaling framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks, enabling VLA models to execute actions with maximum pseudo-count from sampled action chunks while preventing distribution shifts.

These papers collectively address test-time adaptation, action voting/selection, and computational budget optimization for Vision-Language-Action models in robotic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "211dee06-1f3b-4914-aa37-1893298c192f",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "8e4f35a8-0dab-496b-a7bc-9002bacbf361",
  "sourceToolAssistantUUID": "211dee06-1f3b-4914-aa37-1893298c192f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T20:19:54.150Z_

Let me get more details on the verifier-free sampling paper, the Fast-WAM project page for code release info, and the GPC paper about inference-time enhancement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e4f35a8-0dab-496b-a7bc-9002bacbf361",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWRMr8sjUtb3495Wr6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "096d6059-d67c-4147-9cdc-00bf401ba748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVK2RqXwLCrmBxmDTdq9hn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 13804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
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

_source line 24 · 2026-05-10T20:19:57.325Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018dQyNEHQ3PQLnhLRbpEHjf`</summary>

```json
{
  "url": "https://openreview.net/forum?id=UD4Rw8MOEK",
  "prompt": "What is this paper about? Extract: 1) The method name and key idea. 2) Does it use test-time augmentation or prediction averaging? 3) How does it select among candidate actions? 4) What benchmarks does it test on? 5) Does it compare to simple TTA averaging baselines?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "096d6059-d67c-4147-9cdc-00bf401ba748",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWRMr8sjUtb3495Wr6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5a3c3d1-9070-4cf9-83d9-3ddc8c6dcf5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVK2RqXwLCrmBxmDTdq9hn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 13804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
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

_source line 25 · 2026-05-10T20:19:58.552Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014d14i4tMmVDTJVEjHaSUFS`</summary>

```json
{
  "url": "https://yuantianyuan01.github.io/FastWAM/",
  "prompt": "Extract all information about: 1) Code release - is there a GitHub link? 2) Model checkpoints - are they on HuggingFace? 3) Any mention of LIBERO-Plus evaluation. 4) Architecture details and flow matching specifics. 5) Number of inference steps."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a3c3d1-9070-4cf9-83d9-3ddc8c6dcf5e",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWRMr8sjUtb3495Wr6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce03deda-14f7-4533-b4b3-0d29d355421b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVK2RqXwLCrmBxmDTdq9hn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 13804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
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

_source line 26 · 2026-05-10T20:20:00.747Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MZsidvVftiv6DynZbezSEN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.00622",
  "prompt": "What is Generative Predictive Control (GPC)? Extract: 1) Does it use test-time augmentation? 2) Does it average predictions from augmented views? 3) How does it filter/select actions at inference time? 4) What world model does it use? 5) What benchmarks and results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce03deda-14f7-4533-b4b3-0d29d355421b",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWRMr8sjUtb3495Wr6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03bd45af-590c-4eee-bf65-cd42cc864a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVK2RqXwLCrmBxmDTdq9hn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 13804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4617,
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

_source line 27 · 2026-05-10T20:20:00.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LEihj4ueWN6zeXgcG4QhuK`</summary>

```json
{
  "query": "test-time augmentation action prediction averaging VLA robot manipulation simple baseline \"majority voting\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03bd45af-590c-4eee-bf65-cd42cc864a7a",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWRMr8sjUtb3495Wr6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb71c5b3-f760-4c6c-be9a-0478e0224df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVK2RqXwLCrmBxmDTdq9hn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4617,
      "cache_read_input_tokens": 13804,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 13804,
          "cache_creation_input_tokens": 4617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4617,
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

_source line 28 · 2026-05-10T20:20:02.191Z_

<details><summary>↩ Tool result · `toolu_018dQyNEHQ3PQLnhLRbpEHjf`</summary>

```text
# Summary of "Verifier-free Test-Time Sampling for Vision-Language-Action Models"

## 1) Method Name and Key Idea
The paper introduces **MG-Select** (Masking Distribution Guided Selection), which "leverages the model's internal properties without requiring additional training or external modules." The core innovation uses KL divergence from a reference distribution to identify optimal actions.

## 2) Test-Time Augmentation vs. Averaging
The paper employs test-time scaling with multiple candidate sampling rather than simple averaging. It uses a reference distribution generated by masking inputs to guide selection, representing a more sophisticated approach than basic prediction averaging.

## 3) Action Selection Mechanism
MG-Select selects actions by comparing candidates against "a reference action token distribution as a confidence metric for selecting optimal action from multiple candidates." The reference distribution comes from the same model with randomly masked states and language conditions.

## 4) Benchmarks
The paper tests on "diverse simulation and real-world benchmarks" for robotic manipulation, though specific benchmark names aren't detailed in this excerpt.

## 5) Comparison to Simple Baselines
The provided content doesn't explicitly mention comparisons to standard TTA averaging baselines. The focus is on distinguishing their approach from "test-time scaling approaches using external verifiers," which they argue require additional training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a3c3d1-9070-4cf9-83d9-3ddc8c6dcf5e",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "d3466d56-2f59-49e6-b75c-219233d2b8fd",
  "sourceToolAssistantUUID": "e5a3c3d1-9070-4cf9-83d9-3ddc8c6dcf5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T20:20:03.964Z_

<details><summary>↩ Tool result · `toolu_014d14i4tMmVDTJVEjHaSUFS`</summary>

```text
# Fast-WAM Information Extraction

## 1) Code Release
Yes, a GitHub link is provided. The repository is available at: `https://github.com/yuantianyuan01/FastWAM`

## 2) Model Checkpoints
No mention of HuggingFace model checkpoints is made in the provided content.

## 3) LIBERO-Plus Evaluation
There is no reference to LIBERO-Plus evaluation in this material. The paper evaluates on standard LIBERO benchmarks (Spatial, Object, Goal, Long categories) but does not mention LIBERO-Plus specifically.

## 4) Architecture Details
The backbone consists of a "Wan2.2-5B video DiT with a 1B action expert." The design features a "shared-attention Mixture-of-Transformer" structure. During training, the system jointly learns action prediction and video modeling. At test time, it "processes them with the video backbone once, and directly generates actions without explicit future video denoising." However, specifics regarding flow matching are not discussed.

## 5) Number of Inference Steps
The document does not specify the number of inference steps. It emphasizes runtime efficiency, reporting "190 ms" latency on a single GPU, but does not detail step counts for the inference process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce03deda-14f7-4533-b4b3-0d29d355421b",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "766a44c1-a9c6-4078-b3d1-d7c78a0ef972",
  "sourceToolAssistantUUID": "ce03deda-14f7-4533-b4b3-0d29d355421b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T20:20:12.882Z_

<details><summary>↩ Tool result · `toolu_01MZsidvVftiv6DynZbezSEN`</summary>

```text
# Generative Predictive Control (GPC) Summary

Based on the arXiv abstract provided, here's what can be extracted:

**Core Concept:**
GPC is described as "an inference-time method for improving pretrained behavior-cloning policies without retraining." It combines a frozen diffusion policy with an action-conditioned world model.

**Addressing Your Questions:**

1. **Test-time augmentation:** Not mentioned in the available content.

2. **Prediction averaging:** Not addressed in this abstract.

3. **Action filtering/selection:** GPC enables "lightweight online planning that ranks and refines" action proposals through model-based look-ahead, though specific filtering mechanisms aren't detailed.

4. **World model:** An "action-conditioned world model trained on expert demonstrations and random exploration rollouts" predicts action consequences.

5. **Benchmarks/results:** The abstract states GPC "consistently outperforms standard behavior cloning and compares favorably with other inference-time adaptation baselines" across "diverse robotic manipulation tasks, including state- and vision-based settings in both simulation and real-world experiments," but specific numerical results aren't provided in this excerpt.

**Note:** For complete technical details, benchmarks, and methodology, the full paper (available as PDF or HTML) would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03bd45af-590c-4eee-bf65-cd42cc864a7a",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "731ff910-f912-449e-8c91-efd4a08f378b",
  "sourceToolAssistantUUID": "03bd45af-590c-4eee-bf65-cd42cc864a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T20:20:19.854Z_

<details><summary>↩ Tool result · `toolu_01LEihj4ueWN6zeXgcG4QhuK`</summary>

```text
Web search results for query: "test-time augmentation action prediction averaging VLA robot manipulation simple baseline "majority voting" 2024 2025"

Links: [{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116"},{"title":"[2507.05116] VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/abs/2507.05116"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Published as a conference paper at ICLR 2026 VERIFIER-FREE TEST-TIME SAMPLING","url":"https://openreview.net/pdf?id=UD4Rw8MOEK"},{"title":"Verifier-free Test-Time Sampling for Vision Language Action Models","url":"https://arxiv.org/html/2510.05681v1"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10975v2"},{"title":"HyperVLA: Efficient Inference in Vision-Language-Action Models via Hypernetworks","url":"https://arxiv.org/html/2510.04898v1"},{"title":"Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression","url":"https://arxiv.org/html/2412.03293v1"}]

Based on the search results, I found several highly relevant papers on test-time augmentation and ensemble strategies for Vision-Language-Action (VLA) models in robot manipulation. Here are the key findings:

## VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting

The VOTE paper introduces an inference optimization technique with a novel voting-based ensemble strategy to combine current and previous action predictions, improving the utilization of generated actions and overall performance. The Average strategy simply averages all historical predictions. Table 5 compares the proposed action ensemble strategy, Vote Ensemble, with other strategies.

VOTE achieves 39× faster inference than OpenVLA with 46 Hz throughput on edge platforms, demonstrating practical deployability.

## Test-Time Scaling and Majority Voting Approaches

The search results also identified two other relevant test-time approaches:

1. **MG-Select (Verifier-free Test-Time Sampling)**: MG-Select identifies the most confident action sequences by selecting actions with the highest KL divergence from an uncertainty-aware reference, while avoiding the limitations of likelihood-based selection.

2. **RoVer (Robot Reward Model as Test-Time Verifier)**: To enhance VLA performance without further training, researchers have begun to increase the proportion of 'thinking' at test-time.

## Limitations of Simple Averaging

The literature also discusses why simple arithmetic averaging may be insufficient: While this approach addresses some of the limitations associated with token discretization, multimodal states often correspond to multiple valid actions, and the attempt to model these states through techniques such as arithmetic averaging can result in infeasible or suboptimal action outputs.

These papers from 2024-2025 represent the current state of research on test-time augmentation and ensemble methods for VLA robot manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb71c5b3-f760-4c6c-be9a-0478e0224df3",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "d237dbbf-56d8-40b7-acfb-a6f35ae9d586",
  "sourceToolAssistantUUID": "cb71c5b3-f760-4c6c-be9a-0478e0224df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T20:20:23.280Z_

Let me get more details on the VOTE paper and the full MG-Select paper, and also check if Fast-WAM's GitHub repo is actually available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d237dbbf-56d8-40b7-acfb-a6f35ae9d586",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWTdHdpkRWSTaYXX7YV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35a9c8df-ef11-4567-b2ad-70585c3196b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjQHVF47oU5VGrhBH5KAmT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 18421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T20:20:25.761Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SQdB78SUebPLPXowEeo8wr`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.05116",
  "prompt": "Extract details about VOTE: 1) What is the trajectory ensemble voting mechanism? 2) How does the Average baseline compare to the Vote Ensemble method? 3) What augmentation strategies are used? 4) What benchmarks and results? 5) Does it compare simple averaging/TTA to more sophisticated filtering? 6) What is the exact comparison between naive averaging and their voting method?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a9c8df-ef11-4567-b2ad-70585c3196b0",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWTdHdpkRWSTaYXX7YV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d1d8575-0fea-48d4-bd60-cca9cd69164c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjQHVF47oU5VGrhBH5KAmT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 18421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T20:20:30.726Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0114BJnvTT9Msu5sJ28BPVsL`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.05681v1",
  "prompt": "Extract details about MG-Select (verifier-free test-time sampling for VLA): 1) How does it generate multiple action candidates? 2) What is the reference distribution and KL divergence mechanism? 3) Does it compare to simple averaging of augmented predictions? 4) What benchmarks and results? 5) How many candidates are sampled? 6) Does it use any data augmentation at test time?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d1d8575-0fea-48d4-bd60-cca9cd69164c",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWTdHdpkRWSTaYXX7YV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ffe7ed-1e1f-4e10-83b1-e7bcee094778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjQHVF47oU5VGrhBH5KAmT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 18421,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 18421,
          "cache_creation_input_tokens": 2432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2432,
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

### Tool call

_source line 35 · 2026-05-10T20:20:30.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XEjAeDMcdrRpMniT6t8Puq`</summary>

```json
{
  "query": "Fast-WAM github yuantianyuan01 code release checkpoint huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ffe7ed-1e1f-4e10-83b1-e7bcee094778",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWTdHdpkRWSTaYXX7YV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c21b9d8-9b0f-4ecd-8475-d37c20f19a16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjQHVF47oU5VGrhBH5KAmT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2432,
      "cache_read_input_tokens": 18421,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 18421,
          "cache_creation_input_tokens": 2432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2432,
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

_source line 36 · 2026-05-10T20:20:32.963Z_

<details><summary>↩ Tool result · `toolu_01SQdB78SUebPLPXowEeo8wr`</summary>

```text
# VOTE: Key Details Analysis

## 1) Trajectory Ensemble Voting Mechanism

The voting mechanism operates by collecting historical action predictions from previous timesteps. At the current timestep, it computes cosine similarity between each historical prediction and the newest prediction. Actions are split into two groups—those with similarity above threshold τ (0.5) and those below. The subset with more members is averaged to produce the final action. As the paper states, this approach "selects the actions with more votes, thus more likely to be correct."

## 2) Average Baseline Comparison

Table 5 directly compares strategies:
- None (no ensemble): 47.1% average success
- Temporal: 53.7%
- Adaptive: 60.4%
- Average: 61.6%
- Vote: 64.5%

Vote Ensemble outperforms naive averaging by approximately 2.9 percentage points.

## 3) Augmentation Strategies

The paper does not employ traditional data augmentation. Instead, it uses SimplerEnv's built-in variations, which introduces "changes in lighting, color, texture, and camera pose" to test robustness.

## 4) Benchmarks and Results

**LIBERO**: Achieves 98.0% average success rate (vs. OpenVLA-OFT's 95.3%)

**SimplerEnv WidowX**: 58.3% average success rate, surpassing CogACT (51.3%)

**Inference speedup**: 39× faster than OpenVLA on edge devices (46 Hz throughput on NVIDIA Jetson Orin)

## 5) Filtering Sophistication

Unlike "straightforward action chunking" or "static weighted aggregation," the voting method "effectively filters out unreasonable or inconsistent mode predictions, thereby enhancing reliability."

## 6) Naive Averaging vs. Voting

The key distinction: naive averaging considers all historical predictions equally, potentially introducing incorrect predictions. Voting instead performs "majority selection," discarding inconsistent predictions and only averaging actions that vote similarly to the current prediction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d1d8575-0fea-48d4-bd60-cca9cd69164c",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "4a3265e9-adbb-4ec2-89b9-44b6302807f3",
  "sourceToolAssistantUUID": "6d1d8575-0fea-48d4-bd60-cca9cd69164c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T20:20:38.245Z_

<details><summary>↩ Tool result · `toolu_01XEjAeDMcdrRpMniT6t8Puq`</summary>

```text
Web search results for query: "Fast-WAM github yuantianyuan01 code release checkpoint huggingface"

Links: [{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"yuanty/fastwam · Hugging Face","url":"https://huggingface.co/yuanty/fastwam"},{"title":"FastWAM/README.md at main · yuantianyuan01/FastWAM","url":"https://github.com/yuantianyuan01/FastWAM/blob/main/README.md"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"Paper page - Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://huggingface.co/papers/2603.16666"},{"title":"[Feature Request]: Use the `huggingface_hub` library for downloading checkpoints from the HF Hub · Issue #8217 · AUTOMATIC1111/stable-diffusion-webui","url":"https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/8217"},{"title":"FrancisRing/FlashPortrait · Hugging Face","url":"https://huggingface.co/FrancisRing/FlashPortrait"},{"title":"Phr00t/WAN2.2-14B-Rapid-AllInOne · Hugging Face","url":"https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne"},{"title":"Release FocalNet checkpoints on Hugging Face · Issue #56 · microsoft/FocalNet","url":"https://github.com/microsoft/FocalNet/issues/56"},{"title":"huggingface/diffusers v0.33.0 on GitHub","url":"https://newreleases.io/project/github/huggingface/diffusers/release/v0.33.0"}]

Based on the search results, here's what I found about Fast-WAM:

## Fast-WAM GitHub Repository and Checkpoints

The official codebase for Fast-WAM is located at https://github.com/yuantianyuan01/FastWAM and contains the training and evaluation code for FastWAM on LIBERO and RoboTwin.

## Official Checkpoints on Hugging Face

The Hugging Face repository releases the official FastWAM checkpoints for the open-source release of Fast-WAM: Do World Action Models Need Test-time Future Imagination? The checkpoints are available at: https://huggingface.co/yuanty/fastwam

The Hugging Face model repository contains checkpoint files in .pt format for LIBERO and RoboTwin benchmarks, including libero_uncond_2cam224.pt, libero_uncond_2cam224_dataset_stats.json, robotwin_uncond_3cam_384.pt, and robotwin_uncond_3cam_384_dataset_stats.json.

## Downloading Checkpoints

To download the checkpoints, you can use: `pip install -U huggingface_hub` and then `huggingface-cli download yuanty/fastwam` with the specific checkpoint files and `--local-dir ./checkpoints/fastwam_release`.

## Related Resources

Preprocessed datasets for Fast-WAM are available on Hugging Face at https://huggingface.co/datasets/yuanty/LIBERO-fastwam and https://huggingface.co/datasets/yuanty/robotwin2.0-fastwam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c21b9d8-9b0f-4ecd-8475-d37c20f19a16",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "ffa840e4-dbfb-4b30-bfba-20ed7cc9d8ed",
  "sourceToolAssistantUUID": "3c21b9d8-9b0f-4ecd-8475-d37c20f19a16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T20:20:38.534Z_

<details><summary>↩ Tool result · `toolu_0114BJnvTT9Msu5sJ28BPVsL`</summary>

```text
# MG-Select: Verifier-free Test-Time Sampling for VLAs

## 1. Multiple Action Candidate Generation
MG-Select generates candidates through "parallel stochastic sampling" with temperature-controlled noise. The system samples N action sequences in parallel using: "a~j(n)∼πθ(⋅∣ot,qt,I,a~<j(n);τ)" where temperature τ controls distribution sharpness, with lower values approaching greedy decoding.

## 2. Reference Distribution & KL Divergence
The key innovation uses "condition-masking distributions"—the same VLA model with randomly masked inputs (text, state, or both). The confidence metric measures "KL(Qi∥Pi)" where Qi represents the masked distribution and Pi the normal prediction. This creates "maximum uncertainty while remaining aligned with the target task distribution."

## 3. Comparison to Simple Averaging
The paper explicitly contrasts this approach to naive likelihood selection. Simple highest-probability selection fails because "VLAs fine-tuned on target tasks often memorize expert trajectories, causing the probability distribution...to become overly concentrated." The masking approach provides more meaningful confidence signals than uniform baselines.

## 4. Benchmarks & Results
Testing covered:
- **RoboCasa**: 168% improvement with 30 demonstrations on pick-and-place tasks
- **SIMPLER-WidowX**: Consistent improvements across 4 tasks
- **LIBERO**: Superior performance across multiple generalization axes
- **Real robot (Franka)**: 28% gain in-distribution, 35% out-of-distribution

## 5. Number of Candidates Sampled
Ablation studies show "performance improves as N increases from 1 to 4," with N=4 being the sweet spot. Larger values (8, 16) show diminishing returns.

## 6. Test-Time Data Augmentation
No test-time augmentation occurs. However, a "joint training strategy" applies dropout during training to both condition-masked and normal variants, enabling the model to learn both distributions simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ffe7ed-1e1f-4e10-83b1-e7bcee094778",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "4e520e80-5ed8-4098-bc1a-7c0674160b70",
  "sourceToolAssistantUUID": "b4ffe7ed-1e1f-4e10-83b1-e7bcee094778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T20:20:45.601Z_

Now let me get the final pieces of information - the GPC full paper details and check for any direct comparison of TTA vs filtering in robot policy literature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e520e80-5ed8-4098-bc1a-7c0674160b70",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWV18oxbqVF1epL5GpR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d6e5db5-0e28-4a14-9290-7f1da803d660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8zV7NiqX1oSGbTtmeRvJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1009,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 20853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 40 · 2026-05-10T20:20:47.969Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K3ggfEbv1jv3DJLabSmHgV`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.00622",
  "prompt": "Extract detailed information about Generative Predictive Control (GPC): 1) How does it use the world model to filter/rank action proposals at inference? 2) Does it average predictions or select best ones? 3) What is the exact inference-time procedure? 4) What are the benchmark results? 5) How does it compare to baselines including simple averaging or TTA?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6e5db5-0e28-4a14-9290-7f1da803d660",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWV18oxbqVF1epL5GpR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "763964d0-cc8b-437e-9643-2a934f7e87e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8zV7NiqX1oSGbTtmeRvJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1009,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 20853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 41 · 2026-05-10T20:20:48.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UUgttrmEPw85bXe8mpeV5T`</summary>

```json
{
  "query": "\"test-time augmentation\" \"action averaging\" robot policy multimodal action distribution failure mode 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763964d0-cc8b-437e-9643-2a934f7e87e9",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWV18oxbqVF1epL5GpR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a19b94be-b213-4a22-ab09-12d0b8421309",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8zV7NiqX1oSGbTtmeRvJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1009,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 20853,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1009,
          "output_tokens": 259,
          "cache_read_input_tokens": 20853,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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

_source line 42 · 2026-05-10T20:20:55.881Z_

<details><summary>↩ Tool result · `toolu_01K3ggfEbv1jv3DJLabSmHgV`</summary>

```text
# Generative Predictive Control (GPC): Key Details

## 1) World Model Action Filtering

GPC uses the world model to **rank and refine** action proposals rather than averaging them. The paper states: "The generative policy proposes multiple action sequences that are evaluated in imagination using the predictive world model; the action with the highest predicted reward is selected."

## 2) Selection vs. Averaging Strategy

GPC employs **selection-based approaches**, not averaging:
- **GPC-RANK**: Samples K action proposals, rolls each through the world model, and picks "the one with highest reward"
- **GPC-OPT**: Takes a single proposal as warm-start and refines it via gradient ascent through the learned dynamics
- **GPC-RANK+OPT**: Combines both strategies with multiple initializations

## 3) Exact Inference-Time Procedure

The process follows three steps:
1. Sample K action proposals from the frozen diffusion policy
2. Unroll each through the world model to get predicted future observations
3. Evaluate using a reward function (learned predictor or VLM) and select/optimize the best

The paper notes this requires "K×M world model evaluations" for the combined approach.

## 4) Benchmark Results

**Vision-based simulation tasks** (Table II):
- Push-T: 0.739 (GPC-RANK vs. 0.642 behavior cloning baseline)
- Block Stacking: 0.989
- Triangle Drawing: 0.767

**State-based Push-T**: Best variant achieved 0.952 IoU compared to 0.812 baseline

**Real-world success rates**: GPC-RANK improved Push-T and cloth folding tasks over pure behavior cloning baselines

## 5) Comparison to Baselines

GPC substantially outperforms:
- **Pure behavior cloning**: ~10-25% improvement across tasks
- **Planning-only methods** (MPPI, CEM, gradient ascent without policy priors): "achieve substantially lower performance...with success rates below 0.20"
- **Latent-space methods**: Outperforms LaDi-WM, V-GPS, and DreamerV3 on vision tasks

The paper emphasizes "the importance of integrating generative priors with inference-time planning" over planning alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "763964d0-cc8b-437e-9643-2a934f7e87e9",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "74ab8a96-e768-4936-8a20-dbe6107a6ddc",
  "sourceToolAssistantUUID": "763964d0-cc8b-437e-9643-2a934f7e87e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T20:20:56.560Z_

<details><summary>↩ Tool result · `toolu_01UUgttrmEPw85bXe8mpeV5T`</summary>

```text
Web search results for query: ""test-time augmentation" "action averaging" robot policy multimodal action distribution failure mode 2024 2025"

Links: [{"title":"WARPD – World-model Assisted Reactive Policy Diffusion | OpenReview","url":"https://openreview.net/forum?id=OS9eo7NQeO"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies | OpenReview","url":"https://openreview.net/forum?id=Hu3NoPMAg4"},{"title":"Case Studies of Foundation Model Integration in Embodied ...","url":"https://aclanthology.org/2025.findings-emnlp.69.pdf"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"Understanding Test-Time Augmentation","url":"https://arxiv.org/html/2402.06892v1"},{"title":"Beyond Model Adaptation at Test Time: A Survey","url":"https://arxiv.org/html/2411.03687v1"},{"title":"Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"},{"title":"SEMANTIC WORLD MODELS Jacob Berg1 Chuning Zhu1 Yanda Bao1 Ishan Durugkar2","url":"https://weirdlabuw.github.io/swm/static/documents/swm.pdf"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"}]

I found several relevant results related to robot policies, multimodal action distributions, and test-time techniques. Here's what the search revealed:

## Key Findings:

**Multimodal Action Distributions in Robot Policies:**
Diffusion models are now widely used to train large, generalized policies that predict controls or trajectories, leveraging their ability to model multimodal action distributions. Regression methods, such as using a Mean Squared Error (MSE) loss, tend to average these diverse expert behaviors, resulting in conservative or even invalid actions.

**Test-Time Techniques:**
Test-Time Augmentation (TTA) is a very powerful heuristic that takes advantage of data augmentation during testing to produce averaged output. However, the search results don't specifically address failure modes of action averaging in multimodal distributions.

**Recent VLA and Policy Architectures (2024-2025):**
The results show advances in vision-language-action (VLA) models and diffusion-based policies, with hierarchical and late fusion architectures achieving the highest manipulation success and generalization, and diffusion-based decoders demonstrating superior cross-domain transfer and robustness compared to autoregressive heads.

**Failure Modes:**
While the results mention Diffusion Policy (DP) suffers from a trade-off between performance and action horizon: fewer diffusion queries lead to larger trajectory chunks, which in turn accumulate tracking errors, specific failure modes related to averaging multimodal action distributions at test time are not extensively discussed in these results.

The search didn't return papers specifically focused on the failure modes of action averaging when dealing with multimodal action distributions. Would you like me to search for more specific information about this topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a19b94be-b213-4a22-ab09-12d0b8421309",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "b7df6146-2893-4aab-9a39-1508253c9794",
  "sourceToolAssistantUUID": "a19b94be-b213-4a22-ab09-12d0b8421309",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-10T20:21:01.685Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LtosvdR6XLocG6LQyywHB7`</summary>

```json
{
  "url": "https://openreview.net/forum?id=Hu3NoPMAg4",
  "prompt": "What is this paper about? Does it use test-time augmentation for robot policies? Does it compare augmented view averaging to other methods? Extract key details about the method and results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7df6146-2893-4aab-9a39-1508253c9794",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWWLEYQvKnCzQNCon9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b56d0928-f434-4b50-af18-960d08e11358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHvSB75kBeZrH2bJRsB2KU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2820,
      "cache_read_input_tokens": 22274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2820,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T20:21:02.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSKQqjVJVVoRLMsreHoGTZ`</summary>

```json
{
  "query": "PDF \"perturbation learning delayed feedback\" LIBERO ablation \"data augmentation\" \"without\" environment reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b56d0928-f434-4b50-af18-960d08e11358",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWWLEYQvKnCzQNCon9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7d81faf-5d07-4222-9855-b9ecd1377cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHvSB75kBeZrH2bJRsB2KU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2820,
      "cache_read_input_tokens": 22274,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2820
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 22274,
          "cache_creation_input_tokens": 2820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2820,
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

_source line 46 · 2026-05-10T20:21:05.664Z_

<details><summary>↩ Tool result · `toolu_01LtosvdR6XLocG6LQyywHB7`</summary>

```text
# Paper Summary

## Topic
This research addresses a key challenge in robotic manipulation: visuomotor policies that fail when encountering new object configurations or obstacles. The work proposes a data augmentation framework to improve policy robustness without extensive manual data collection.

## Method Overview
The approach generates synthetic training data by:
- Creating realistic fisheye image sequences from real demonstrations
- Generating physically feasible action trajectories through optimization
- Using an adapted Gaussian Splatting technique for 3D scene reconstruction and editing with wide field-of-view cameras
- Rendering novel viewpoints to augment the training dataset

As stated in the abstract, the method aims to produce "visually realistic fisheye image sequences and corresponding physically feasible action trajectories."

## Test-Time Augmentation & Comparison Details
Based on the content provided, the paper does not contain information about whether it employs test-time augmentation for robot policies or whether it compares augmented view averaging against alternative methods. The abstract focuses on the augmentation framework's training-time application and empirical results showing "improved success rate for various manipulation tasks."

## Key Results
Experiments demonstrated improvements across simulation and real-world tests, with better performance on both original tasks and scenarios requiring collision avoidance with novel obstacles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b56d0928-f434-4b50-af18-960d08e11358",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "8f4b7a33-eb2a-499c-b141-c07eaac6fc9a",
  "sourceToolAssistantUUID": "b56d0928-f434-4b50-af18-960d08e11358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T20:21:09.099Z_

<details><summary>↩ Tool result · `toolu_01CSKQqjVJVVoRLMsreHoGTZ`</summary>

```text
Web search results for query: "PDF "perturbation learning delayed feedback" LIBERO ablation "data augmentation" "without" environment reward"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"Universal Graph Contrastive Learning with a Novel Laplacian Perturbation","url":"https://proceedings.mlr.press/v216/ko23a/ko23a.pdf"},{"title":"SURF: SEMI-SUPERVISED REWARD LEARNING WITH ...","url":"https://openreview.net/pdf?id=TfhfZLQ2EJO"},{"title":"A Taxonomy for Learning with Perturbation and Algorithms | ACM Transactions on Knowledge Discovery from Data","url":"https://dl.acm.org/doi/10.1145/3644391"},{"title":"Data-Efﬁcient Augmentation for Training Neural Networks Tian Yu Liu","url":"https://baharanm.github.io/assets/pdf/liu22augmentation.pdf"},{"title":"Adapting Offline Reinforcement Learning with Online Delays","url":"https://arxiv.org/pdf/2506.00131"},{"title":"A Survey of Reinforcement Learning from Human Feedback Timo Kaufmann","url":"https://arxiv.org/pdf/2312.14925"},{"title":"Learning perturbation sets for robust machine learning","url":"https://locuslab.github.io/2020-07-20-perturbation/"}]

Based on the web search results, I found the paper you're looking for! The search returned information about:

**"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models"**

This paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model. 

PDF mitigates spurious correlations through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. It also learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback.

**Regarding the ablation study you mentioned:** The ablation compares the baseline OpenVLA with variants of the proposed PDF, where "PDF w/o DF" denotes OpenVLA that selects actions solely via multi-view voting (without delayed feedback), and "PDF w/o DA" denotes OpenVLA that learns perturbations using only the original pixel observations (without data augmentation).

Experiments on LIBERO demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation, with a +7.4% success rate improvement.

The paper is available on arXiv as document 2604.18107, and you can access both the HTML and PDF versions through the links in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7d81faf-5d07-4222-9855-b9ecd1377cb8",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "aaadd70e821d54dca",
  "type": "user",
  "uuid": "53453c0f-2655-432d-a692-08cf02c06290",
  "sourceToolAssistantUUID": "e7d81faf-5d07-4222-9855-b9ecd1377cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-10T20:22:10.730Z_

I now have comprehensive information on all three topics. Here is my detailed research report:

---

## 1. TTPL / PDF (Test-Time Perturbation Learning with Delayed Feedback)

**Paper**: [arXiv:2604.18107](https://arxiv.org/abs/2604.18107), April 2026. The method is actually called **PDF** (Perturbation learning with Delayed Feedback), though the paper title uses "Test-Time Perturbation Learning."

### Exact Mechanism

PDF has three components working together:

1. **Uncertainty-based Data Augmentation + Action Voting**: At each timestep, the model computes normalized Shannon entropy of the predicted action distribution: `U_t = -1/log(K) * sum(p(a_k|s_k) * log(p(a_k|s_k)))`. This uncertainty score drives an adaptive augmentation budget: `N_t = N_max * U_t` (with N_max = 3). Multiple augmented observations are generated, passed through the frozen VLA, and the resulting candidate actions are selected via **majority voting** (not simple averaging).

2. **Adaptive Scheduler**: Allocates more augmented views when the model is uncertain, fewer when confident. This balances performance vs. computational cost.

3. **Lightweight Perturbation Module (P-head)**: A small 9M-parameter learned head `h_theta` that adjusts action logits: `z_tilde_t = h_phi(f_t) + lambda * h_theta(f_t)`. Only `h_theta` is updated; all VLA parameters remain frozen.

### Environment Feedback Requirement

**Yes, it requires delayed episodic feedback during deployment.** Upon task completion, the agent receives a delayed reward signal `r_i` indicating task success/failure. The perturbation head is trained via REINFORCE: `L = -(r-b) * log(pi_phi) + lambda_kl * I[r>b] * KL(pi_phi || pi_tilde)`. This is a critical limitation -- it needs end-of-episode reward signals.

### Comparison to Simple Averaging

The paper does NOT explicitly include a "simple averaging of augmented views" baseline. However, based on the ablation:
- **PDF w/o DF** = multi-view voting only (no delayed feedback learning) -- this is essentially augment + vote without the learned perturbation
- **PDF w/o DA** = perturbation learning with only original observations (no augmentation)
- Both underperform the full method. Notably, without delayed feedback, performance drops substantially (0.50 on Object suite vs much higher with full method).

The key difference from naive TTA averaging: (1) they use majority voting not mean averaging; (2) the augmentation budget adapts to uncertainty; (3) the perturbation head learns from episodic feedback to correct overconfidence.

### LIBERO Results: +7.4% average success rate improvement over vanilla OpenVLA.

---

## 2. Test-Time Augmentation (TTA) for Robot Manipulation Policies

### State of the Art for Prediction Averaging / Filtering

The literature reveals several distinct approaches, none of which are simple TTA averaging:

**a) MG-Select (ICLR 2026)** -- [Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)
- Samples N=4 action candidates in parallel (temperature-controlled stochastic sampling)
- Scores them using KL divergence between normal predictions and "condition-masked" predictions (model with randomly masked text/state inputs)
- Selects the candidate with highest KL divergence (most "confident" deviation from uncertain baseline)
- Does NOT use data augmentation at test time
- Results: +168% on RoboCasa, +28%/+35% in/out-of-distribution on real Franka

**b) VOTE (2025)** -- [Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)
- Collects action predictions across timesteps and uses cosine similarity to identify consensus
- Actions split into two groups by threshold (tau=0.5); the larger group is averaged
- Explicitly compares Vote Ensemble (64.5%) vs. naive Average (61.6%) vs. no ensemble (47.1%)
- **This is the clearest direct comparison**: voting outperforms simple averaging by ~3 points

**c) GPC (Generative Predictive Control, 2025)** -- [arXiv:2502.00622](https://arxiv.org/abs/2502.00622)
- Samples K action proposals from frozen diffusion policy
- Rolls each forward through a learned world model
- Selects the one with highest predicted reward (GPC-RANK) or refines via gradient ascent (GPC-OPT)
- ~10-25% improvement over pure behavior cloning

**d) RoVer** -- Uses a learned Process Reward Model to score action chunks at test time

### Key Finding: Why Simple Averaging Fails

The literature consistently notes that **averaging multimodal action distributions produces invalid or suboptimal actions**. MSE-style averaging of diverse expert behaviors results in conservative or infeasible actions (the "averaging" problem). This is why voting/selection methods dominate over simple mean-based TTA in robotics.

### Has Anyone Compared TTA to Sophisticated Filtering?

**Yes -- the VOTE paper (Table 5) is the most direct comparison**:
- No ensemble: 47.1%
- Simple Average: 61.6%  
- Vote Ensemble (filtering): 64.5%

MG-Select compares against likelihood-based selection but not against augmentation-based averaging specifically.

---

## 3. Fast-WAM Architecture Details

**Paper**: [arXiv:2603.16666](https://arxiv.org/abs/2603.16666), March 2026.

### Flow-Matching vs. Diffusion

**Flow-matching (velocity field)**. The paper explicitly states it is "trained to predict the corresponding velocity field with a standard flow matching objective." This is NOT score-based diffusion.

### Integration Steps

**10 denoising steps** at inference with classifier-free guidance (CFG) scale of 1.0.

### Code and Checkpoint Release

Both are publicly available:
- **GitHub**: https://github.com/yuantianyuan01/FastWAM (official codebase)
- **HuggingFace checkpoints**: https://huggingface.co/yuanty/fastwam
  - `libero_uncond_2cam224.pt` + stats JSON
  - `robotwin_uncond_3cam_384.pt` + stats JSON
- **Preprocessed datasets**: `huggingface.co/datasets/yuanty/LIBERO-fastwam` and `huggingface.co/datasets/yuanty/robotwin2.0-fastwam`

### LIBERO-Plus Evaluation

**No.** Fast-WAM has NOT been evaluated on LIBERO-Plus. It only evaluates on standard LIBERO suites (Spatial, Object, Goal, Long) and RoboTwin.

### LIBERO Results

Average **97.6%** success rate:
- Spatial: 98.2%
- Object: 100.0%
- Goal: 97.0%
- Long: 95.2%

### Architecture

- Built on **Wan2.2-5B** video DiT backbone + 1B action expert DiT (6B total parameters)
- **Mixture-of-Transformer (MoT)** design with shared attention
- Action horizon: 32 steps; 9 video frames per chunk
- Training: joint flow-matching loss `L = L_act + lambda * L_vid`
- Inference latency: **190ms** on single GPU (4x faster than imagine-then-execute WAMs)
- Key insight: video co-training during training improves representations, but explicit future video generation at test time is unnecessary

---

## Summary Table for Your Paper Revision

| Method | Mechanism | Needs Env Feedback? | Simple Avg Baseline? |
|--------|-----------|--------------------|--------------------|
| PDF/TTPL | Augment + vote + learned perturbation | Yes (episodic reward) | Not directly compared |
| MG-Select | Multi-sample + KL selection | No | No (compares to likelihood) |
| VOTE | Temporal ensemble + cosine voting | No | Yes: Avg=61.6%, Vote=64.5% |
| GPC | World model ranking/optimization | No (needs world model) | Not directly |
| Fast-WAM | Flow-matching WAM (no test-time imagination) | No | N/A (not a TTA method) |

Sources:
- [TTPL/PDF - arXiv:2604.18107](https://arxiv.org/abs/2604.18107)
- [Fast-WAM - arXiv:2603.16666](https://arxiv.org/abs/2603.16666)
- [Fast-WAM GitHub](https://github.com/yuantianyuan01/FastWAM)
- [Fast-WAM HuggingFace](https://huggingface.co/yuanty/fastwam)
- [MG-Select - Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)
- [VOTE - Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)
- [GPC - Generative Predictive Control](https://arxiv.org/abs/2502.00622)
- [RoVer - Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)
- [Diff-DAgger - Uncertainty Estimation with Diffusion Policy](https://arxiv.org/html/2410.14868v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53453c0f-2655-432d-a692-08cf02c06290",
  "isSidechain": true,
  "agentId": "aaadd70e821d54dca",
  "requestId": "req_011CauWXFrtdsUHYN68SE63X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "872fd232-2476-4f57-bd15-2fd8899811c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAVhRXnBX77VQGTqYkKssb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 25094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1309,
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
