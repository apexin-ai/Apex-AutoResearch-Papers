# Research conversation: You are helping review an ML paper proposal. I need to verify the compute feasibility of the following plan: The proposa

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3ef468e6e9bc3aab.jsonl`
- **Structured JSON:** [`dae193b8d96dce4eca58.json`](../../sessions/da/dae193b8d96dce4eca58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-10T18:39:41.218Z_

You are helping review an ML paper proposal. I need to verify the compute feasibility of the following plan:

The proposal wants to train a ~15M parameter policy network via PPO on top of a frozen World-Action Model (WAM). The policy decides per-step whether to cache, compute, or extend denoising steps. Training involves:
1. Pre-computing "teacher cache" — running frozen WAM at full steps on training data (~20-30h H100 claimed)
2. PPO training of the 15M param policy (~60-80h H100 claimed)
3. Evaluation and ablations (~40-55h)
Total claimed: 130-180 H100-hours

Please search for:
1. "PPO training diffusion policy" or "reinforcement learning diffusion step allocation" — what compute do similar RL-for-diffusion-control methods actually require?
2. "D3P dynamic denoising diffusion policy" training details — this paper uses PPO for adaptive step allocation, what GPU hours did they use?
3. "AdaDiff training cost" — how much compute does AdaDiff's step predictor require?
4. How large is the LIBERO dataset? How many trajectories/episodes? Is it available publicly?
5. Is UWM (Unified World Models) publicly available with pretrained checkpoints? Search "UWM unified world models checkpoint huggingface" or "UWM RSS 2025 code release"
6. Is DreamZero's code publicly available? Search "DreamZero github code release"

Report specific numbers wherever possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "f609c93b-b3cb-4d99-897f-01dc7560910e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:39:41.221Z_

```json
{
  "parentUuid": "f609c93b-b3cb-4d99-897f-01dc7560910e",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
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
  "uuid": "69a6a440-3dc3-4a51-bc8c-58b697f20657",
  "timestamp": "2026-05-10T18:39:41.221Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:39:46.624Z_



I'll search for all of these topics in parallel to verify the compute feasibility claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69a6a440-3dc3-4a51-bc8c-58b697f20657",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNnVVg1SgVtFbYuvNLs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fbc6e36-06b0-41a2-aaad-7978f471e10c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137VvDXBcNiLXZBRrYErR4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:39:46.968Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XFpGeyjXNZrcZChvYh2X33`</summary>

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
  "parentUuid": "9fbc6e36-06b0-41a2-aaad-7978f471e10c",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNnVVg1SgVtFbYuvNLs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b59df256-142d-4b4b-bafb-b111b24c9a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137VvDXBcNiLXZBRrYErR4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-10T18:39:46.970Z_

<details><summary>↩ Tool result · `toolu_01XFpGeyjXNZrcZChvYh2X33`</summary>

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
  "parentUuid": "b59df256-142d-4b4b-bafb-b111b24c9a11",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "1bfda491-7173-424e-b95c-b761dbfb6f5c",
  "sourceToolAssistantUUID": "b59df256-142d-4b4b-bafb-b111b24c9a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:39:49.606Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bfda491-7173-424e-b95c-b761dbfb6f5c",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNnvnSiuDGXECwYisof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50202763-721a-402c-b39b-a497cc0556ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEiHTALGAXdk7uuvpEG3KE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 9129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1412,
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

_source line 7 · 2026-05-10T18:39:50.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01889hQ9cUhyxNZgLxDAJQVL`</summary>

```json
{
  "query": "PPO training diffusion policy reinforcement learning step allocation compute cost GPU hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50202763-721a-402c-b39b-a497cc0556ff",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNnvnSiuDGXECwYisof",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57683e7e-f457-46a9-99fe-ffb021064579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEiHTALGAXdk7uuvpEG3KE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 9129,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 78,
          "cache_read_input_tokens": 9129,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1412,
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

_source line 8 · 2026-05-10T18:39:57.190Z_

<details><summary>↩ Tool result · `toolu_01889hQ9cUhyxNZgLxDAJQVL`</summary>

```text
Web search results for query: "PPO training diffusion policy reinforcement learning step allocation compute cost GPU hours"

Links: [{"title":"Training Diffusion Models with Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/07/14/ddpo/"},{"title":"GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning","url":"https://arxiv.org/html/2505.18763"},{"title":"PPO — Stable Baselines3 2.9.0a2 documentation","url":"https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html"},{"title":"Finetune Stable Diffusion Models with DDPO via TRL","url":"https://huggingface.co/blog/trl-ddpo"},{"title":"Proximal Policy Optimization | OpenAI","url":"https://openai.com/index/openai-baselines-ppo/"},{"title":"Proximal policy optimization - Wikipedia","url":"https://en.wikipedia.org/wiki/Proximal_policy_optimization"},{"title":"Proximal Policy Gradient (PPO) - CleanRL","url":"https://docs.cleanrl.dev/rl-algorithms/ppo/"},{"title":"Proximal Policy Optimization (PPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/ppo.html"},{"title":"Training Diffusion Models with Reinforcement Learning","url":"https://rl-diffusion.github.io/"},{"title":"Efficient Online Reinforcement Learning for Diffusion Policy | OpenReview","url":"https://openreview.net/forum?id=6Anv3KB9lz"}]

I've performed the web search for your query on PPO training with diffusion policies and reinforcement learning. Here's what I found:

## Key Findings

**DDPO (Denoising Diffusion Policy Optimization):**

Diffusion models can be trained directly on downstream objectives using reinforcement learning by posing denoising diffusion as a multi-step decision-making problem, enabling a class of policy gradient algorithms called denoising diffusion policy optimization (DDPO).

DDPOIS (which uses an importance sampled estimator) is the best-performing algorithm with implementation closely following proximal policy optimization (PPO), and was used for finetuning Stable Diffusion v1-4.

**Step Allocation in the Denoising Process:**

In MDP terminology, each denoising step is an action, and the agent only gets a reward on the final step of each denoising trajectory when the final sample is produced.

**Computational Efficiency:**

One implementation using PyTorch + LoRA can finetune Stable Diffusion with less than 10GB of GPU memory.

Regarding computational cost concerns, backpropagating policy gradient through the diffusion process incurs huge computational costs and instability, thus being expensive and not scalable. More recent research has addressed this with Reweighted Score Matching (RSM) which preserves the optimal solution and low computational cost of denoising score matching.

The search results provide architectural information about DDPO and efficiency considerations, though they don't contain specific GPU hour or step allocation benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57683e7e-f457-46a9-99fe-ffb021064579",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "4852d89b-521b-4a08-95a7-230265baea7c",
  "sourceToolAssistantUUID": "57683e7e-f457-46a9-99fe-ffb021064579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:39:59.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PzVusyvVi7bMV423ZfMChG`</summary>

```json
{
  "query": "D3P dynamic denoising diffusion policy PPO adaptive step allocation training GPU hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4852d89b-521b-4a08-95a7-230265baea7c",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNofo56M6GfR7CexowA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b36091bf-e700-4b97-ab95-ec1d2e7dde61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sd9UqEjjfFdcrqeWkqJSDm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 10541,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 10541,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
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

_source line 10 · 2026-05-10T18:40:08.377Z_

<details><summary>↩ Tool result · `toolu_01PzVusyvVi7bMV423ZfMChG`</summary>

```text
Web search results for query: "D3P dynamic denoising diffusion policy PPO adaptive step allocation training GPU hours"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Diffusion Policy Policy Optimization","url":"https://diffusion-ppo.github.io/"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"GitHub - irom-princeton/dppo: Official implementation of Diffusion Policy Policy Optimization, arxiv 2024 · GitHub","url":"https://github.com/irom-princeton/dppo"}]

Based on the search results, here's what I found about D3P (Dynamic Denoising Diffusion Policy):

## Overview

D3P is a diffusion-based policy that adaptively allocates denoising steps across actions at test time. The D3P architecture consists of a standard noise predicting network serving as the base diffusion policy and a lightweight adaptor designed to predict the noise-level strides based on the current observation, which adapts the number of denoising steps for the current action.

## Training Approach

The lightweight adaptor is trained from scratch with PPO, where its reward function incentivizes minimizing denoising steps without compromising performance. A base policy is fine-tuned with DPPO to maximize task success. The adaptor and base diffusion policy are jointly optimized via reinforcement learning to balance task performance and inference efficiency.

## Performance

D3P achieves up to 2.2× inference speedups without reduced performance by adapting the number of denoising steps per action.

## Motivation

Robotic tasks often contain a mix of crucial and routine actions which differ in their impact on task success, with task executions typically consisting of pivotal crucial actions that largely determine success and more forgiving routine actions with only marginal impact.

The search results did not include specific information about GPU hours required for training D3P. If you need that specific detail, you may want to check the full paper on arXiv (2508.06804).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b36091bf-e700-4b97-ab95-ec1d2e7dde61",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "7c92685f-5827-48a4-8b3a-c23fa9fe1c3a",
  "sourceToolAssistantUUID": "b36091bf-e700-4b97-ab95-ec1d2e7dde61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:40:10.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0118MFemMVbRJLVGeuSuxEsT`</summary>

```json
{
  "query": "AdaDiff adaptive diffusion steps predictor training cost compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c92685f-5827-48a4-8b3a-c23fa9fe1c3a",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNpVkrYgjSsSPS9s7F2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5410d6d-9a84-46f1-9578-a41adc72c432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014epTojhvojnbWJYyu73Bcs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 11426,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 11426,
          "cache_creation_input_tokens": 954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 954,
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

_source line 12 · 2026-05-10T18:40:17.148Z_

<details><summary>↩ Tool result · `toolu_0118MFemMVbRJLVGeuSuxEsT`</summary>

```text
Web search results for query: "AdaDiff adaptive diffusion steps predictor training cost compute requirements"

Links: [{"title":"[2311.14768] AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/abs/2311.14768"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/html/2311.14768v2"},{"title":"GitHub - icon-lab/AdaDiff: Official PyTorch implementation of AdaDiff described in the paper (https://arxiv.org/abs/2207.05876).","url":"https://github.com/icon-lab/AdaDiff"},{"title":"[2309.17074] AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://arxiv.org/abs/2309.17074"},{"title":"AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72986-7_5"},{"title":"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10120.pdf"},{"title":"GitHub - Tangshengku/AdaDiff: Official Pytorch Implementation of Paper \"AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation\" · GitHub","url":"https://github.com/Tangshengku/AdaDiff"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models | Request PDF","url":"https://www.researchgate.net/publication/390721137_AdaDiff_Adaptive_Step_Selection_for_Fast_Diffusion_Models"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion","url":"https://www.emergentmind.com/papers/2311.14768"},{"title":"AdaDiff: Accelerating Diffusion Models Through Step-Wise Adaptive Computation | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-72986-7_5"}]

Based on the search results, I found information about AdaDiff and its training compute requirements:

## AdaDiff Overview

AdaDiff is a lightweight framework designed to learn instance-specific step usage policies, which are then used by the diffusion model for generation. AdaDiff is optimized using a policy gradient method to maximize a carefully designed reward function, balancing inference time and generation quality.

## Training Cost and Compute Requirements

The training cost ranges from 16 to 80 A100 GPU hours for the adaptive step policy applied to different base models.

## Performance Results

The method demonstrates significant efficiency gains. The dynamic strategy saves 39.2% and 33.8% of generation time on two datasets separately compared to the fixed 50-step generation while maintaining comparable generation quality. Additionally, the approach achieves similar visual quality compared to the baseline using a fixed 50 denoising steps while reducing inference time by at least 33%, going as high as 40%.

It's worth noting that there are multiple papers with the "AdaDiff" name - the primary results above focus on the adaptive step selection for fast diffusion models (arXiv:2311.14768), which learns prompt-specific policies for determining the number of denoising steps needed for each input.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5410d6d-9a84-46f1-9578-a41adc72c432",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "78bfbf84-ab2b-4862-9c22-b60c7a8c024a",
  "sourceToolAssistantUUID": "e5410d6d-9a84-46f1-9578-a41adc72c432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T18:40:19.586Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016TYqqD133fFLCafaAjLfPV`</summary>

```json
{
  "query": "LIBERO benchmark dataset robot manipulation trajectories episodes size publicly available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78bfbf84-ab2b-4862-9c22-b60c7a8c024a",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNq9AddRgSamPuNHbsU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9654d3a-3442-46bd-97fa-e12f37309c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EiT1yRRNr69kApkAXJPoF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 12380,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 12380,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 925,
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

_source line 14 · 2026-05-10T18:40:26.621Z_

<details><summary>↩ Tool result · `toolu_016TYqqD133fFLCafaAjLfPV`</summary>

```text
Web search results for query: "LIBERO benchmark dataset robot manipulation trajectories episodes size publicly available"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"A Unified 3D Multi-Modal Representation for Robot ...","url":"https://arxiv.org/pdf/2505.10105"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Benchmark Descriptions — RoboVerse 0.1.0 documentation","url":"https://roboverse.wiki/dataset_benchmark/tasks/descriptions"},{"title":"RoboCerebra: A Large-scale Benchmark for Long-horizon ...","url":"https://arxiv.org/pdf/2506.06677"},{"title":"Research – LIBERO","url":"https://libero-project.github.io/research"}]

Based on the search results, here's what I found about the LIBERO benchmark dataset regarding robot manipulation trajectories and episodes:

## Dataset Size and Trajectory Information

LIBERO generates 130 language-conditioned robot manipulation tasks grouped into four suites. For the demonstration data specifically, the dataset includes 50 trajectories of high-quality demonstrations for every single task in the generated task suites. This means the total demonstration dataset contains approximately 6,500 trajectory demonstrations (130 tasks × 50 trajectories per task).

## Evaluation Episodes

For benchmarking purposes, 10 episodes per task are used across all four standard suites (Spatial, Object, Goal, Long), which gives 400 total episodes and matches the protocol used for published results.

## Public Availability

The datasets are hosted on HuggingFace, making them publicly available. The demonstrations are collected by human experts through teleoperation with 3Dconnexion Spacemouse.

## Task Suite Organization

The 130 language-conditioned manipulation tasks are organized into 4 groups: Tasks with distribution shifts in object types (LIBERO-OBJECT), Tasks with distribution shifts in the spatial arrangement of objects (LIBERO-SPATIAL), Tasks with distribution shifts in the task goals (LIBERO-GOAL), and Tasks with a combination of the above three (LIBERO-100).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9654d3a-3442-46bd-97fa-e12f37309c24",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "4be1e5e1-609a-4462-bf20-a40897893d2c",
  "sourceToolAssistantUUID": "d9654d3a-3442-46bd-97fa-e12f37309c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:40:30.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KgyixLY4EWRY29HRN2o78t`</summary>

```json
{
  "query": "UWM unified world models pretrained checkpoint huggingface code release RSS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4be1e5e1-609a-4462-bf20-a40897893d2c",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNqqgSkyQHqLedjpPmt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac83a52b-8745-4fb4-a427-124a7307cd1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRUVh8zjVECPHANXnj42kK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 13305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 863,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:40:37.613Z_

<details><summary>↩ Tool result · `toolu_01KgyixLY4EWRY29HRN2o78t`</summary>

```text
Web search results for query: "UWM unified world models pretrained checkpoint huggingface code release RSS 2025"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"Code World Model (CWM) · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/cwm"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"Code World Model (CWM)","url":"https://huggingface.co/docs/transformers/main/model_doc/cwm"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"tencent/HY-World-2.0 · Hugging Face","url":"https://huggingface.co/tencent/HY-World-2.0"},{"title":"facebook/cwm · Hugging Face","url":"https://huggingface.co/facebook/cwm"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"GitHub - World-In-World/world-in-world: Code implementation of the paper \"World-in-World: World Models in a Closed-Loop World\" (ICLR'26 Oral) · GitHub","url":"https://github.com/World-In-World/world-in-world"}]

Based on the search results, here's what I found about UWM (Unified World Models) and its code/checkpoint release:

## UWM Overview

Unified World Model (UWM) is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos to flexibly learn policies, forward dynamics, inverse dynamics, and video prediction models from both robot and video data.

## Code and Checkpoint Release

UWM was published in the Proceedings of Robotics: Science and Systems (RSS) 2025.

**GitHub Repository:** The repository provides a PyTorch implementation of Unified World Model (UWM), which combines action diffusion and video diffusion to enable scalable pretraining on large, heterogeneous robotics datasets.

**Pretrained Checkpoints:** The authors release the pretrained and cotrained DROID UWM checkpoints, which you can download and directly finetune from.

**Resources:** Videos and code are available at https://weirdlabuw.github.io/uwm/ The code is available on GitHub at [github.com/WEIRDLabUW/unified-world-model](https://github.com/WEIRDLabUW/unified-world-model).

The checkpoints appear to be available through the official GitHub repository rather than directly through Hugging Face, though they can be used with standard PyTorch workflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac83a52b-8745-4fb4-a427-124a7307cd1b",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "d21d4bde-9b09-49b3-b405-453cc0a116b7",
  "sourceToolAssistantUUID": "ac83a52b-8745-4fb4-a427-124a7307cd1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T18:40:41.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYMtxDXaru9GzQoKbKEpeZ`</summary>

```json
{
  "query": "DreamZero github code release publicly available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21d4bde-9b09-49b3-b405-453cc0a116b7",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNredCvNJ2fS18oABRD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff4bad4-c6f3-473d-9ba6-dc93834ac365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117xCzHS6jbtuJjQ7KfvSoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 14168,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 14168,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 937,
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

_source line 18 · 2026-05-10T18:40:47.022Z_

<details><summary>↩ Tool result · `toolu_01AYMtxDXaru9GzQoKbKEpeZ`</summary>

```text
Web search results for query: "DreamZero github code release publicly available"

Links: [{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"dreamzero/README.md at main · dreamzero0/dreamzero","url":"https://github.com/dreamzero0/dreamzero/blob/main/README.md"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"zero-dream (ZeroDream) · GitHub","url":"https://github.com/zero-dream"},{"title":"Issues · dreamzero0/dreamzero","url":"https://github.com/dreamzero0/dreamzero/issues"},{"title":"ZeroDream - Overview","url":"https://github.com/ZeroDream"},{"title":"Codezero Technologies Inc. · GitHub","url":"https://github.com/c6o"},{"title":"CodeZero · GitHub","url":"https://github.com/codezero-be"},{"title":"dream · GitHub Topics","url":"https://github.com/topics/dream"},{"title":"Dreams of Code · GitHub","url":"https://github.com/dreamsofcode-io"}]

Yes, DreamZero code has been publicly released on GitHub, with the full training codebase, preprocessed dataset, and guide for new embodiments released on 02/20. The code is available at the GitHub repository: https://github.com/dreamzero0/dreamzero

On 02/27, the DreamZero-AgiBot checkpoint and post-training code for efficient few-shot adaptation were also released. Additionally, the preprocessed DROID dataset used to train DreamZero is released on HuggingFace, and a 14B pretrained DROID checkpoint is available on Huggingface for download.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff4bad4-c6f3-473d-9ba6-dc93834ac365",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "b6ef8496-dc80-4950-ac9c-48e60b6b6077",
  "sourceToolAssistantUUID": "9ff4bad4-c6f3-473d-9ba6-dc93834ac365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T18:40:51.639Z_

Now let me get more specific details on some of these.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ef8496-dc80-4950-ac9c-48e60b6b6077",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNsLqQi7rLGQNgxCscd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3824f666-366b-4e6f-bf9e-8b3f9b86c558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbYZrq4FSnaqKGRXHAJHDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 15105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 570,
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

_source line 20 · 2026-05-10T18:40:52.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CC2GGJ7LraosJHNyqxAtos`</summary>

```json
{
  "query": "D3P \"Dynamic Denoising Diffusion Policy\" training details GPU hours compute A100 H100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3824f666-366b-4e6f-bf9e-8b3f9b86c558",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNsLqQi7rLGQNgxCscd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6593208-8c4b-4b59-9eab-29f14083b199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbYZrq4FSnaqKGRXHAJHDJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 15105,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 570
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 15105,
          "cache_creation_input_tokens": 570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 570,
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

_source line 21 · 2026-05-10T18:41:04.359Z_

<details><summary>↩ Tool result · `toolu_01CC2GGJ7LraosJHNyqxAtos`</summary>

```text
Web search results for query: "D3P "Dynamic Denoising Diffusion Policy" training details GPU hours compute A100 H100"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://arxiv.org/pdf/2508.06804"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"GitHub - yk7333/d3po: [CVPR 2024] Code for the paper \"Using Human Feedback to Fine-tune Diffusion Models without Any Reward Model\" · GitHub","url":"https://github.com/yk7333/d3po"},{"title":"Discrete Denoising Diffusion Models (D3PM)","url":"https://www.emergentmind.com/topics/discrete-denoising-diffusion-probabilistic-models-d3pm"},{"title":"3D Diffusion Policy","url":"https://arxiv.org/html/2403.03954v1"},{"title":"D3PM: Discrete Denoising Diffusion Probabilistic Models","url":"https://hunterheidenreich.com/notes/machine-learning/generative-models/discrete-diffusion-models/"}]

Based on the search results, I found information about D3P (Dynamic Denoising Diffusion Policy), but the available sources don't contain specific details about GPU hours or computational requirements using A100 or H100 GPUs.

Here's what I found about D3P:

## Overview
D3P is a diffusion policy that dynamically adjusts the number of denoising steps during task execution, consisting of a standard noise predicting network as the base diffusion policy and a lightweight adaptor designed to predict the noise-level strides based on the current observation.

## Training Approach
The method uses reinforcement learning with a two-layer POMDP to jointly train both the base diffusion policy and the adaptor, where the base policy is fine-tuned with DPPO to maximize task success, and the lightweight adaptor is trained from scratch with PPO to minimize denoising steps without compromising performance.

## Performance Results
D3P achieves an average 2.2× inference speed-up over baseline methods while maintaining comparable performance. On a physical robot, it achieves a 1.9× acceleration in inference speed against a normal fixed-step diffusion policy.

## Inference Hardware
All inference was performed on a consumer-grade desktop (i7-12900K CPU, RTX 2080 GPU).

Unfortunately, the paper does not appear to specify training GPU hours or computational requirements using high-end accelerators like A100 or H100 GPUs in the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6593208-8c4b-4b59-9eab-29f14083b199",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "e3a173d2-f7c5-45d6-bc31-b4148af1d7e0",
  "sourceToolAssistantUUID": "e6593208-8c4b-4b59-9eab-29f14083b199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T18:41:07.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELUZszDppa4Lh6gLm3LGZU`</summary>

```json
{
  "query": "DPPO \"diffusion policy policy optimization\" training compute GPU hours robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3a173d2-f7c5-45d6-bc31-b4148af1d7e0",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNtczXsk1o9sxzMhGgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4047051-29ae-45eb-9c5b-a99957f56a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JP1K4nUQRKzmty7qf6cM1j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 15675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:41:14.978Z_

<details><summary>↩ Tool result · `toolu_01ELUZszDppa4Lh6gLm3LGZU`</summary>

```text
Web search results for query: "DPPO "diffusion policy policy optimization" training compute GPU hours robotics"

Links: [{"title":"Diffusion Policy Policy Optimization","url":"https://diffusion-ppo.github.io/"},{"title":"GitHub - irom-princeton/dppo: Official implementation of Diffusion Policy Policy Optimization, arxiv 2024 · GitHub","url":"https://github.com/irom-princeton/dppo"},{"title":"[2409.00588] Diffusion Policy Policy Optimization","url":"https://arxiv.org/abs/2409.00588"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"Diffusion Policy Policy Optimization","url":"https://arxiv.org/html/2409.00588v1"},{"title":"DPPO: Diffusion Policy Policy Optimization","url":"https://www.alphaxiv.org/overview/2409.00588"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Training Diffusion Models with Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/07/14/ddpo/"},{"title":"(PDF) Diffusion Policy Policy Optimization","url":"https://www.researchgate.net/publication/383700708_Diffusion_Policy_Policy_Optimization"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION - Princeton University","url":"https://collaborate.princeton.edu/en/publications/diffusion-policy-policy-optimization/"}]

I've completed the web search for "DPPO diffusion policy policy optimization training compute GPU hours robotics". Here's what I found:

## Key Findings:

DPPO is an algorithmic framework and set of best practices for fine-tuning diffusion-based policies in continuous control and robot learning tasks.

### Core Contribution:
DPPO is an algorithmic framework including best practices for fine-tuning diffusion-based policies (e.g. Diffusion Policy) in continuous control and robot learning tasks using the policy gradient (PG) method from reinforcement learning (RL).

### Performance:
DPPO achieves the strongest overall performance and efficiency for fine-tuning in common benchmarks compared to other RL methods for diffusion-based policies and also compared to PG fine-tuning of other policy parameterizations.

### Robotics Applications:
DPPO solves the more challenging Square and Transport tasks from robomimic to >90% success rates using either state or pixel input and sparse reward. Additionally, in three multi-stage assembly tasks from Furniture-Bench, One-leg, Lamp, and Round-table, DPPO improves the success rate of pre-trained policies from 57% to 97%, 12% to 87%, and 1% to 86%, respectively, learning from only sparse reward.

### Computational Setup:
In Gym, Robomimic, and D3IL tasks, they run 40, 50, and 50 parallelized MuJoCo environments on CPU, respectively. Furniture-Bench tasks run IsaacGym on a single GPU.

**Note:** The search results did not contain specific GPU hour requirements for training DPPO models, so that particular detail was not found in the available sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4047051-29ae-45eb-9c5b-a99957f56a70",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "322c7b04-fe66-422e-a008-5776ad6b098b",
  "sourceToolAssistantUUID": "b4047051-29ae-45eb-9c5b-a99957f56a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T18:41:17.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LLUrvGCRuey9LWevKXv3hG`</summary>

```json
{
  "query": "DDPO denoising diffusion policy optimization training time single GPU compute cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "322c7b04-fe66-422e-a008-5776ad6b098b",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNuQMJiru47qoLkU5dL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21810d98-2abe-448a-ab75-4d40931c0797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMnG8WtUvSnsyjRjWj5tzL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 16642,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 16642,
          "cache_creation_input_tokens": 933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 933,
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

_source line 25 · 2026-05-10T18:41:24.205Z_

<details><summary>↩ Tool result · `toolu_01LLUrvGCRuey9LWevKXv3hG`</summary>

```text
Web search results for query: "DDPO denoising diffusion policy optimization training time single GPU compute cost"

Links: [{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"Diffusion Policy Policy Optimization","url":"https://diffusion-ppo.github.io/"},{"title":"Denoising Diffusion Policy Optimization · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/ddpo_trainer"},{"title":"Denoising Diffusion Policy Optimization","url":"https://huggingface.co/docs/trl/ddpo_trainer"},{"title":"GitHub - kvablack/ddpo-pytorch: DDPO for finetuning diffusion models, implemented in PyTorch with LoRA support · GitHub","url":"https://github.com/kvablack/ddpo-pytorch"},{"title":"GitHub - irom-princeton/dppo: Official implementation of Diffusion Policy Policy Optimization, arxiv 2024 · GitHub","url":"https://github.com/irom-princeton/dppo"},{"title":"Training Diffusion Models with Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/07/14/ddpo/"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"GitHub - yk7333/d3po: [CVPR 2024] Code for the paper \"Using Human Feedback to Fine-tune Diffusion Models without Any Reward Model\" · GitHub","url":"https://github.com/yk7333/d3po"},{"title":"[2305.13301] Training Diffusion Models with Reinforcement Learning","url":"https://arxiv.org/abs/2305.13301"}]

Based on the search results, here's what I found regarding DDPO training requirements and compute costs:

## GPU Memory Requirements

DDPO with LoRA support requires less than 10GB of GPU memory to finetune Stable Diffusion, and the implementation works as long as each GPU has at least 10GB of memory.

One A100 GPU is recommended for running DDPO, as anything below an A100 will not be able to run the example script effectively, even with smaller parameters.

## Training Structure

Each DDPO epoch consists of generating a batch of images, computing their rewards, and then doing training steps on those images, with an important hyperparameter being the number of images generated per epoch.

## Computational Optimization

Recent developments have focused on reducing computational demands: Dynamic Denoising Schedules like D3P adapt the number of denoising steps per action to allocate more compute to critical samples/actions, achieving up to 2.2× inference speedups without reduced performance. Additionally, Real-Time Iteration (RTI) schemes warm-start the denoising chain from prior control steps, significantly reducing the average denoising iterations for time-critical applications (down to 25–145 ms per inference).

However, the search results don't provide specific information about total training time or detailed compute cost metrics for single GPU training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21810d98-2abe-448a-ab75-4d40931c0797",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "7ce6d4bc-86ae-47a9-95ba-c869580a1bbe",
  "sourceToolAssistantUUID": "21810d98-2abe-448a-ab75-4d40931c0797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T18:41:27.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FEGvJY94Moy6faYwMsBBoP`</summary>

```json
{
  "query": "LIBERO dataset number of demonstrations per task 50 demos total size download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce6d4bc-86ae-47a9-95ba-c869580a1bbe",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNv612R48XbtVumXzcT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6ef2b6d-1d2d-4ce9-ba6f-9155a58fbc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XztWNsNBoVGEELyJrqdtUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 17575,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 17575,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 866,
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

_source line 27 · 2026-05-10T18:41:32.677Z_

<details><summary>↩ Tool result · `toolu_01FEGvJY94Moy6faYwMsBBoP`</summary>

```text
Web search results for query: "LIBERO dataset number of demonstrations per task 50 demos total size download"

Links: [{"title":"LIBERO Datasets – LIBERO","url":"https://libero-project.github.io/datasets"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"Datasets — libero 0.1.0 documentation","url":"https://lifelong-robot-learning.github.io/LIBERO/html/algo_data/datasets.html"},{"title":"libero · PyPI","url":"https://pypi.org/project/libero/"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"Embodied-CoT/embodied_features_and_demos_libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Embodied-CoT/embodied_features_and_demos_libero"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"}]

Based on the search results, I found specific information about the LIBERO dataset demonstrations:

The LIBERO-90 dataset contains 50 trajectories for each of 90 tasks. This means there are 50 demonstrations per task, for a total of 4,500 demonstrations across LIBERO-90.

LIBERO provides 4 datasets: libero_spatial, libero_object, libero_goal and libero_100, which consist of 10, 10, 10, and 100 tasks each.

For downloading the dataset, you can download the demonstration dataset by running: python benchmark_scripts/download_libero_datasets.py, and by default the dataset will be stored under the LIBERO folder with all four datasets downloaded.

However, the search results did not contain specific information about the total download size of the datasets. The results confirm the 50 demonstrations per task structure for LIBERO-90, but don't specify the exact file sizes for each dataset suite.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6ef2b6d-1d2d-4ce9-ba6f-9155a58fbc2a",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "c0f15c51-6e07-46f5-9bb2-c81d14bcc4b2",
  "sourceToolAssistantUUID": "a6ef2b6d-1d2d-4ce9-ba6f-9155a58fbc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T18:41:36.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RcAMrZxrxVKFaxeW4DjyNs`</summary>

```json
{
  "query": "UWM unified world model github pretrained checkpoints DROID download weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f15c51-6e07-46f5-9bb2-c81d14bcc4b2",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNvi2hjktpvyX8pdz8Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d034cb69-d3fd-48dc-90b7-f6eb0eebb8d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG5eKhaD8kzVvUfrZLbq8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 18441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 804,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T18:41:45.152Z_

<details><summary>↩ Tool result · `toolu_01RcAMrZxrxVKFaxeW4DjyNs`</summary>

```text
Web search results for query: "UWM unified world model github pretrained checkpoints DROID download weights"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"GitHub - facebookresearch/jepa-wms: Code, data and weights for the paper **What drives success in physical planning with Joint-Embedding Predictive World Models?** · GitHub","url":"https://github.com/facebookresearch/jepa-wms"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"GitHub - unitreerobotics/unifolm-world-model-action · GitHub","url":"https://github.com/unitreerobotics/unifolm-world-model-action"},{"title":"GitHub - lucas-maes/le-wm: Official code base for LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels · GitHub","url":"https://github.com/lucas-maes/le-wm"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"GitHub - LMD0311/HERMES: [ICCV 2025] HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation · GitHub","url":"https://github.com/lmd0311/hermes"}]

Based on the web search results, here's what I found regarding UWM (Unified World Model) pretrained checkpoints and DROID weights:

## Pretrained Checkpoints Available

The pretrained and cotrained DROID UWM checkpoints are released and you can download and directly finetune from these checkpoints. Additionally, a pretrained LIBERO-90 checkpoint is available for download and direct finetuning.

## Repository Location

The official repository is located at: **https://github.com/WEIRDLabUW/unified-world-model**

## Project Information

UWM is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos to flexibly learn policies, forward dynamics, inverse dynamics, and video prediction models from both robot and video data.

UWM was pretrained on a subset of the DROID dataset, and then finetuned to diverse downstream tasks.

## Additional Resources

- Shell scripts for DROID pretraining/cotraining/finetuning experiments are provided in the scripts directory, with each script running a dataset conversion pipeline to create a Zarr buffer for the corresponding DROID TFDS dataset.
- Videos and code are available at https://weirdlabuw.github.io/uwm/

For the specific download links and detailed instructions for accessing the weights, you'll need to visit the GitHub repository directly, as the exact URLs for the checkpoint downloads are referenced but not explicitly listed in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d034cb69-d3fd-48dc-90b7-f6eb0eebb8d4",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "df808fb0-c660-42ec-9a7d-cdd980178696",
  "sourceToolAssistantUUID": "d034cb69-d3fd-48dc-90b7-f6eb0eebb8d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T18:41:47.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S2VPwqU8DqyQymi5BwpRQz`</summary>

```json
{
  "query": "DreamZero world action model training compute GPU hours pretrain DROID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df808fb0-c660-42ec-9a7d-cdd980178696",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNwdQRW7sENYTh31Dmy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28637e4f-ad74-4d39-89a2-9dcc5a5130a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Qy7kcuwVXD9z9MguB8q4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 19245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:41:56.562Z_

<details><summary>↩ Tool result · `toolu_01S2VPwqU8DqyQymi5BwpRQz`</summary>

```text
Web search results for query: "DreamZero world action model training compute GPU hours pretrain DROID"

Links: [{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"dreamzero/README.md at main · dreamzero0/dreamzero","url":"https://github.com/dreamzero0/dreamzero/blob/main/README.md"},{"title":"dreamzero0/dreamzero | DeepWiki","url":"https://deepwiki.com/dreamzero0/dreamzero"},{"title":"World Action Models as Zero-Shot Policies","url":"https://www.emergentmind.com/papers/2602.15922"},{"title":"GEAR-Dreams/DreamZero-DROID · Hugging Face","url":"https://huggingface.co/GEAR-Dreams/DreamZero-DROID"},{"title":"(PDF) World Action Models are Zero-shot Policies","url":"https://www.researchgate.net/publication/400930242_World_Action_Models_are_Zero-shot_Policies"},{"title":"Dreamer 4: Scalable World Model Agents","url":"https://www.emergentmind.com/papers/2509.24527"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Why Is DreamZero So Good at Robotics Benchmarks?","url":"https://itcanthink.substack.com/p/why-is-dreamzero-so-good-at-robotics"}]

Based on the search results, here's what I found about DreamZero's training compute and specifications:

## Model Architecture and Training

DreamZero-DROID is a 14B parameter World Action Model (WAM) checkpoint trained from scratch using only the DROID dataset. It's built upon a pretrained video diffusion backbone (Wan2.1-I2V-14B-480P).

## Training Details

Training was performed for 100K steps with a global batch size of 128 for both AgiBot and DROID datasets. The model updates all DiT blocks, the state encoder, action encoder, and action decoder, while freezing the text encoder, image encoder, and VAE.

## GPU Training Configuration

The training script uses 4 GPUs as a default configuration. However, the search results don't contain specific information about the total GPU hours required for pretraining DreamZero-DROID.

## Inference Specifications

While specific pretraining GPU hours aren't mentioned in the available results, DreamZero runs inference at 7Hz using 2 GB200s, demonstrating the computational requirements for deployment.

If you need more specific details about the total GPU hours used for pretraining, that information may be in the full paper or technical documentation on their GitHub repository or arXiv page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28637e4f-ad74-4d39-89a2-9dcc5a5130a4",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "6a1c2083-1a54-4d3b-8b8e-a5d998755618",
  "sourceToolAssistantUUID": "28637e4f-ad74-4d39-89a2-9dcc5a5130a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T18:41:59.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BgMVcvH2Xz7NhJBW7SKYoa`</summary>

```json
{
  "query": "PPO small policy network 15M parameters training time reinforcement learning robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a1c2083-1a54-4d3b-8b8e-a5d998755618",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNxUDZJ36MMUFjtcQx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c73d3ff-db08-448c-8694-7b68b5cab81b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReVaPBhc7dfCwGkWhQc2a3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 20280,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 20280,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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

_source line 33 · 2026-05-10T18:42:06.086Z_

<details><summary>↩ Tool result · `toolu_01BgMVcvH2Xz7NhJBW7SKYoa`</summary>

```text
Web search results for query: "PPO small policy network 15M parameters training time reinforcement learning robotics"

Links: [{"title":"Proximal policy optimization - Wikipedia","url":"https://en.wikipedia.org/wiki/Proximal_policy_optimization"},{"title":"The 37 Implementation Details of Proximal Policy Optimization · The ICLR Blog Track","url":"https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/"},{"title":"Experience-Efficient Model-Free Deep Reinforcement Learning Using Pre-Training","url":"https://arxiv.org/html/2510.10029"},{"title":"What is Proximal Policy Optimization (PPO)? | IBM","url":"https://www.ibm.com/think/topics/proximal-policy-optimization"},{"title":"Proximal Policy Optimization (PPO)","url":"https://huggingface.co/blog/deep-rl-ppo"},{"title":"Proximal Policy Optimization — Spinning Up documentation","url":"https://spinningup.openai.com/en/latest/algorithms/ppo.html"},{"title":"Proximal Policy Optimization (PPO) - GeeksforGeeks","url":"https://www.geeksforgeeks.org/machine-learning/a-brief-introduction-to-proximal-policy-optimization/"},{"title":"Proximal Policy Optimization | OpenAI","url":"https://openai.com/index/openai-baselines-ppo/"},{"title":"[1707.06347] Proximal Policy Optimization Algorithms","url":"https://arxiv.org/abs/1707.06347"},{"title":"A proximal policy optimization based deep reinforcement learning framework for tracking control of a flexible robotic manipulator - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2590123025002646"}]

Based on the search results, I found relevant information about PPO training in robotics environments. Here are the key findings:

## PPO Training Time in Robotics

Brax can train a viable agent in robotics tasks with PPO using a massive N = 2048 environments and a small M=20, yet finish the training in one minute. This demonstrates how hardware-accelerated vectorized environments can significantly reduce training time.

## PPO Applications in Robotics

PPO has been applied to many areas, such as controlling a robotic arm. Additionally, it trains robots to perform complex control tasks like walking, grasping or balancing by learning optimal movement policies.

## Network Architecture and Efficiency

While the search results don't specifically mention 15M parameter networks, they do discuss PPO's efficiency characteristics. Compared to TRPO, the PPO method is relatively easy to implement and requires less computational resource and time. Therefore, it is cheaper and more efficient to use PPO in large-scale problems.

For robotics-specific improvements, researchers have proposed to use accelerated vectorized environments, with examples including Nvidia's Isaac Gym using torch for hardware-accelerated vectorized environments, allowing users to spin up N=4096 environments easily, and Google's Brax using jax to write hardware-accelerated vectorized environments, allowing users to spin up N=2048 environments easily.

The search results suggest that with modern hardware acceleration, PPO training on robotics tasks can be quite fast, though specific timing for 15M parameter networks was not found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c73d3ff-db08-448c-8694-7b68b5cab81b",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "d90ad20f-3683-4058-8782-454f95788264",
  "sourceToolAssistantUUID": "3c73d3ff-db08-448c-8694-7b68b5cab81b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T18:42:08.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JFxV4dSJWYQRpAxDeijbb5`</summary>

```json
{
  "query": "AdaDiff step predictor training 16 80 A100 GPU hours policy gradient reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d90ad20f-3683-4058-8782-454f95788264",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNyAroa2fpUhA2JXYYZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c096e330-beb4-4f7a-b2db-0b47ea1314cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzXWfg8bcshYLfBLobjLxn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 21128,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 21128,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 893,
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

_source line 35 · 2026-05-10T18:42:13.364Z_

<details><summary>↩ Tool result · `toolu_01JFxV4dSJWYQRpAxDeijbb5`</summary>

```text
Web search results for query: "AdaDiff step predictor training 16 80 A100 GPU hours policy gradient reward"

Links: [{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/html/2311.14768"},{"title":"[2311.14768] AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://arxiv.org/abs/2311.14768"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33075/35230"},{"title":"AdaDiff: Adaptive Step Selection for Fast Diffusion Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33075"},{"title":"The Definitive Guide to Policy Gradients in Deep Reinforcement Learning:","url":"https://arxiv.org/pdf/2401.13662"},{"title":"1 Training step timing breakdown for ViT-B/16 on a single A100 GPU. We measure the forward, backward, and optimizer times per training step. We observe that the CUDA-accelerated learned optimizer steps (cyan, green) show substantial improvements over the naive implementations (yellow, red). In all cases, as the batch size is increased, the relative overhead of the optimizer shrinks.","url":"https://arxiv.org/html/2506.10315"},{"title":"Methods and tools for efficient training on a single GPU","url":"https://huggingface.co/docs/transformers/v4.33.2/perf_train_gpu_one"},{"title":"Methods and tools for efficient training on a single GPU · Hugging Face","url":"https://huggingface.co/docs/transformers/v4.42.0/perf_train_gpu_one"},{"title":"Efficient Training on a Single GPU","url":"https://huggingface.co/docs/transformers/v4.20.1/en/perf_train_gpu_one"},{"title":"What should I consider when choosing a GPU for training vs. inference in my AI project?","url":"https://www.runpod.io/articles/comparison/choosing-a-gpu-for-training-vs-inference"}]

Based on the search results, I found relevant information about AdaDiff and its training specifications:

The training cost for the AdaDiff step predictor ranges from 16 to 80 A100 GPU hours for the adaptive step policy applied to different base models.

AdaDiff is optimized using a policy gradient method to maximize a carefully designed reward function, balancing inference time and generation quality.

The step selection network is trained to produce a policy for step usage and is optimized using a policy gradient method to maximize a meticulously crafted reward function, with the primary objective being to encourage the generation of high-quality visual content while minimizing computational resources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c096e330-beb4-4f7a-b2db-0b47ea1314cb",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "08641710-89ec-4743-b48f-f40d326436bc",
  "sourceToolAssistantUUID": "c096e330-beb4-4f7a-b2db-0b47ea1314cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T18:42:16.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CGruy8UeRwmvmdh9S771k9`</summary>

```json
{
  "query": "DPPO diffusion policy optimization training time wall clock GPU single Robomimic Furniture-Bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08641710-89ec-4743-b48f-f40d326436bc",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNyiBxgvu9Ja7K8Jx51",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28ab167b-7475-41c9-97b0-b3e0e30e63a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APp6uVohQCAhV8WYV4yJcQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 22021,
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
          "cache_read_input_tokens": 22021,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 37 · 2026-05-10T18:42:23.732Z_

<details><summary>↩ Tool result · `toolu_01CGruy8UeRwmvmdh9S771k9`</summary>

```text
Web search results for query: "DPPO diffusion policy optimization training time wall clock GPU single Robomimic Furniture-Bench"

Links: [{"title":"Diffusion Policy Policy Optimization","url":"https://diffusion-ppo.github.io/"},{"title":"GitHub - irom-princeton/dppo: Official implementation of Diffusion Policy Policy Optimization, arxiv 2024 · GitHub","url":"https://github.com/irom-princeton/dppo"},{"title":"Diffusion Policy Policy Optimization","url":"https://arxiv.org/html/2409.00588v3"},{"title":"(PDF) Diffusion Policy Policy Optimization","url":"https://www.researchgate.net/publication/383700708_Diffusion_Policy_Policy_Optimization"},{"title":"DPPO: Diffusion Policy Policy Optimization","url":"https://www.alphaxiv.org/overview/2409.00588"},{"title":"dppo/README.md at main · irom-princeton/dppo","url":"https://github.com/irom-princeton/dppo/blob/main/README.md"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss","url":"https://arxiv.org/html/2508.02644v1"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"Diffusion Policy Policy Optimization (2409.00588v3)","url":"https://www.emergentmind.com/papers/2409.00588"}]

Based on the search results, I found information about DPPO (Diffusion Policy Policy Optimization) and its performance on Furniture-Bench tasks. Here's what the research shows:

## DPPO Performance on Furniture-Bench

DPPO demonstrates exceptional performance in long-horizon, multi-stage tasks using the Furniture-Bench environment. In simulated furniture assembly tasks (One-leg, Lamp, Round-table), DPPO maintains strong training stability and performance improvement even with medium randomness, while Gaussian-MLP policies frequently collapse to zero success rates.

## Training Efficiency and Wall-Clock Time

Regarding training time and GPU efficiency, the search results indicate that wall-clock times are roughly comparable (and often faster) than other diffusion-based RL baselines, though can be up to 2× slower than other policy parameterization baselines. Additionally, DPPO also runs significantly faster in wall-clock time than the baselines as it leverages sampling from highly parallelized environments.

The official implementation supports GPU training and is available on GitHub. The code requires a Linux machine with a Nvidia GPU for core dependencies.

However, the search results do not contain specific wall-clock GPU training time metrics (in hours) for individual Furniture-Bench tasks with single GPU setups. For those specific numerical details, you may want to check the paper's appendix or the official DPPO GitHub repository at https://github.com/irom-princeton/dppo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28ab167b-7475-41c9-97b0-b3e0e30e63a8",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "b80c5da0-f921-4e4c-8fe8-7749d5f59483",
  "sourceToolAssistantUUID": "28ab167b-7475-41c9-97b0-b3e0e30e63a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T18:42:26.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhCcw7414dqjZx6ifw1b6p`</summary>

```json
{
  "query": "D3P paper appendix training details \"4090\" OR \"A100\" OR \"H100\" hours adaptor PPO denoising"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b80c5da0-f921-4e4c-8fe8-7749d5f59483",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauNzURG6pay2yRhJgEVR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf53a91-25da-4392-83e9-57aca5eb16b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f1kN41i6PvuBpW9YNkX1i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 22825,
      "output_tokens": 81,
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
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 22825,
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

_source line 39 · 2026-05-10T18:42:43.423Z_

<details><summary>↩ Tool result · `toolu_01FhCcw7414dqjZx6ifw1b6p`</summary>

```text
Web search results for query: "D3P paper appendix training details "4090" OR "A100" OR "H100" hours adaptor PPO denoising"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804"},{"title":"GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub","url":"https://github.com/dao-ailab/flash-attention"},{"title":"Towards Stabilized and Efﬁcient Diffusion Transformers through","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Towards_Stabilized_and_Efficient_Diffusion_Transformers_through_Long-Skip-Connections_with_Spectral_ICCV_2025_paper.pdf"},{"title":"Why A100/H100 Beat RTX 4090 for Large-Model Training","url":"https://www.allpcb.com/allelectrohub/why-a100h100-beat-rtx-4090-for-large-model-training"},{"title":"What should I consider when choosing a GPU for training vs. inference in my AI project?","url":"https://www.runpod.io/articles/comparison/choosing-a-gpu-for-training-vs-inference"},{"title":"A100/H100 too expensive, why not use 4090? | Bojie Li","url":"https://01.me/en/2023/09/h100-vs-4090/"},{"title":"Difference between A100 vs RTX 4090 in training deep learning models - TensorRT - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/difference-between-a100-vs-rtx-4090-in-training-deep-learning-models/315232"},{"title":"RTX 4090 vs A100 vs H100: Complete GPU Comparison for AI in 2026 | SynpixCloud","url":"https://www.synpixcloud.com/blog/rtx-4090-vs-a100-vs-h100-comparison"},{"title":"The Definitive AI Workstation Build Guide: H100 vs. 4090 vs. 4x 4090 | by Danny H Lee | Medium","url":"https://medium.com/@danny_54172/the-definitive-ai-workstation-build-guide-h100-vs-4090-vs-4x-4090-e8033f9777fd"},{"title":"NVIDIA RTX 4090 for AI & Training: Cloud Pricing and Best Options (2026) - Fluence","url":"https://www.fluence.network/blog/nvidia-rtx-4090/"}]

I found the D3P paper in the search results. Let me search more specifically for the appendix training details with GPU hours information.

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://arxiv.org/pdf/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"[2107.03006] Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/abs/2107.03006"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/pdf/2107.03006"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://papers.neurips.cc/paper/2021/file/958c530554f78bcd8e97125b70e6973d-Paper.pdf"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces | OpenReview","url":"https://openreview.net/forum?id=h7-XixPCAL"},{"title":"[2006.11239] Denoising Diffusion Probabilistic Models","url":"https://arxiv.org/abs/2006.11239"}]

Let me search more specifically for the D3P appendix with training computational details.

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"}]

Let me try a more direct search for the D3P paper PDF appendix section E or training details.

No links found.

Let me search for the full D3P paper PDF with training time information.

Links: [{"title":"What is meant by GPU days or GPU hours in deep learning? - Quora","url":"https://www.quora.com/What-is-meant-by-GPU-days-or-GPU-hours-in-deep-learning"},{"title":"Computational cost. We report inference time on GPU and CPU, and the... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Computational-cost-We-report-inference-time-on-GPU-and-CPU-and-the-number-of-FLOPs-for_tbl1_341402374"},{"title":"Predicting the Computational Cost of Deep Learning Models Daniel Justus","url":"https://arxiv.org/pdf/1811.11880"},{"title":"[1811.11880] Predicting the Computational Cost of Deep Learning Models","url":"https://arxiv.org/abs/1811.11880"},{"title":"Business Analysis — AI Computational Cost | by Yuqi Li | Geek Culture | Medium","url":"https://medium.com/geekculture/business-analysis-ai-computational-cost-67a136957c95"},{"title":"Minimization of high computational cost in data preprocessing and modeling using MPI4Py - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666827023000361"},{"title":"Computational cost (CPU time) of the different methods | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Computational-cost-CPU-time-of-the-different-methods_fig5_295397885"}]

Based on my search results, I found the D3P paper (arXiv:2508.06804 - "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning"). However, the search results did not return the specific appendix section with detailed training specifications including GPU hours and hardware details for the 4090, A100, or H100 GPUs.

The search results show that additional deployment details are provided in Appendix D, and detailed training curves are provided in Appendix C. The paper mentions that all inference was performed on a consumer-grade desktop (i7-12900K CPU, RTX 2080 GPU) for the physical robot experiments.

However, I was unable to locate the specific appendix section containing the training computational details (such as GPU hours on 4090, A100, or H100) that you're searching for. To access these details, you may need to:

1. Download the full PDF version of the paper from arXiv (arxiv.org/pdf/2508.06804)
2. Check appendix sections directly, particularly Appendix E or a dedicated "Computational Details" or "Training Details" section
3. Look for supplementary materials on the authors' GitHub repository if available


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cf53a91-25da-4392-83e9-57aca5eb16b7",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "f1fff053-5e8f-4da2-ad4a-72c0bfca7250",
  "sourceToolAssistantUUID": "4cf53a91-25da-4392-83e9-57aca5eb16b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T18:42:46.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjcWKHqjxC4bXsxmA3jd2n`</summary>

```json
{
  "query": "DPPO training 4000 epochs \"wall clock\" OR \"training time\" OR \"GPU hours\" diffusion policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1fff053-5e8f-4da2-ad4a-72c0bfca7250",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP1vZQnR7NjMfgwvuX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37cad3f1-c1f7-4f48-a5f9-a48e9de86368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgjMN3AB76eH8BSfMtoYJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 23703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T18:42:57.115Z_

<details><summary>↩ Tool result · `toolu_01RjcWKHqjxC4bXsxmA3jd2n`</summary>

```text
Web search results for query: "DPPO training 4000 epochs "wall clock" OR "training time" OR "GPU hours" diffusion policy"

Links: [{"title":"Diffusion Policy Policy Optimization","url":"https://diffusion-ppo.github.io/"},{"title":"GitHub - irom-princeton/dppo: Official implementation of Diffusion Policy Policy Optimization, arxiv 2024 · GitHub","url":"https://github.com/irom-princeton/dppo"},{"title":"Diffusion Policy Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=mEpqHvbD2h"},{"title":"[2409.00588] Diffusion Policy Policy Optimization","url":"https://arxiv.org/abs/2409.00588"},{"title":"Denoising Diffusion Policy Optimization · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/ddpo_trainer"},{"title":"Diffusion Policy Policy Optimization","url":"https://arxiv.org/html/2409.00588v1"},{"title":"Denoising Diffusion Policy Optimization","url":"https://huggingface.co/docs/trl/ddpo_trainer"},{"title":"Training Diffusion Models with Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/07/14/ddpo/"},{"title":"Getting Started with DPPO: A Walkthrough Using a 2D, Single-Step Toy Environment | by Neel | Medium","url":"https://medium.com/@neelsortur/getting-started-with-dppo-a-walkthrough-using-a-2d-single-step-toy-environment-1b63b48e64b7"},{"title":"DIFFUSION POLICY POLICY OPTIMIZATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"}]

The search results contain general information about DPPO (Diffusion Policy Policy Optimization) but don't include specific training time metrics. Let me search more specifically for training time information.

Links: [{"title":"[2409.00588] Diffusion Policy Policy Optimization","url":"https://arxiv.org/abs/2409.00588"},{"title":"Paper page - Diffusion Policy Policy Optimization","url":"https://huggingface.co/papers/2409.00588"},{"title":"Diffusion Policy Policy Optimization","url":"https://arxiv.org/html/2409.00588"},{"title":"Improving training time and GPU utilization in geo-distributed language model training","url":"https://arxiv.org/html/2411.14458v1"},{"title":"[2409.00588v2] Diffusion Policy Policy Optimization","url":"https://arxiv.org/abs/2409.00588v2"},{"title":"[2411.14458] Improving training time and GPU utilization in geo-distributed language model training","url":"https://arxiv.org/abs/2411.14458"},{"title":"Forecasting GPU Performance for Deep Learning Training and Inference","url":"https://arxiv.org/html/2407.13853v3"},{"title":"[2204.06240] CowClip: Reducing CTR Prediction Model Training Time from 12 hours to 10 minutes on 1 GPU","url":"https://arxiv.org/abs/2204.06240"},{"title":"Asynchronous Distributed Proximal Policy Optimization Training Framework Based on GPU | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-16-6372-7_67"},{"title":"Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective","url":"https://arxiv.org/html/2509.10371v1"}]

The search results are not returning the specific information requested. Let me try a more targeted search for the full PDF or paper appendix.

No links found.

I was unable to find specific information about DPPO training with 4000 epochs in terms of wall clock time, GPU hours, or training time in the available search results. 

Based on the search results, I found that the DPPO (Diffusion Policy Policy Optimization) paper is available on arXiv (arxiv.org/abs/2409.00588), and the official implementation is available on GitHub at irom-princeton/dppo. The paper mentions extensive experiments on tasks from various benchmarks including Robomimic and Furniture-Bench, but the search results returned do not contain the specific computational resource requirements (wall clock time, GPU hours, or training time) for 4000 epochs of DPPO training.

To find this specific information, you would need to:

1. Check the appendix of the full PDF of the paper at: https://arxiv.org/pdf/2409.00588.pdf
2. Review the GitHub repository's documentation and code at: https://github.com/irom-princeton/dppo
3. Look for supplementary materials or experiment logs associated with the paper

The specific training time metrics you're looking for are likely documented in the paper's appendix or supplementary materials but were not captured in the web search results I obtained.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37cad3f1-c1f7-4f48-a5f9-a48e9de86368",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "b88a64e8-c813-4992-93cc-019ddaf04b10",
  "sourceToolAssistantUUID": "37cad3f1-c1f7-4f48-a5f9-a48e9de86368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-10T18:42:59.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VSDxcfHehPjdKghohjZH1i`</summary>

```json
{
  "query": "reinforcement learning adaptive denoising steps diffusion model compute budget training cost comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b88a64e8-c813-4992-93cc-019ddaf04b10",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP2w3TiKjfYGPvJwVWA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fbc9dce-764a-4b7b-890f-b5aab78e840f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YVAMGbkgGJrY3ZXvNVTfd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1371,
      "cache_read_input_tokens": 25766,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 25766,
          "cache_creation_input_tokens": 1371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1371,
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

_source line 43 · 2026-05-10T18:43:07.210Z_

<details><summary>↩ Tool result · `toolu_01VSDxcfHehPjdKghohjZH1i`</summary>

```text
Web search results for query: "reinforcement learning adaptive denoising steps diffusion model compute budget training cost comparison"

Links: [{"title":"Training Diffusion Models with Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/07/14/ddpo/"},{"title":"Training Diffusion Models with Reinforcement Learning","url":"https://rl-diffusion.github.io/"},{"title":"[2305.13301] Training Diffusion Models with Reinforcement Learning","url":"https://arxiv.org/abs/2305.13301"},{"title":"TRAINING DIFFUSION MODELS WITH REINFORCEMENT LEARNING Kevin Black∗1","url":"https://rl-diffusion.github.io/files/paper.pdf"},{"title":"Training Diffusion Models with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=YCWjhGrJFD"},{"title":"Diffusion model - Wikipedia","url":"https://en.wikipedia.org/wiki/Diffusion_model"},{"title":"D3P: Dynamic Denoising Difusion Policy via Reinforcement Learning Shu’ang Yu","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/90eaaadf-c4d8-4aa2-980f-d143a1e121cd.pdf"},{"title":"Training diffusion models with reinforcement learning - ΑΙhub","url":"https://aihub.org/2023/09/15/training-diffusion-models-with-reinforcement-learning/"},{"title":"Large-scale Reinforcement Learning for Diffusion Models","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07968.pdf"},{"title":"d1: Scaling Reasoning in Diffusion ...","url":"https://dllm-reasoning.github.io/media/preprint.pdf"}]

I've found research results on reinforcement learning with diffusion models. Here's what the search revealed:

## Key Findings

**Denoising Diffusion Policy Optimization (DDPO)**: The diffusion process is reframed as a multi-step Markov decision process (MDP), where each denoising step is an action, and the agent only gets a reward on the final step of each denoising trajectory when the final sample is produced.

**Advantage over Traditional Approaches**: This framework allows application of powerful algorithms from RL literature designed for multi-step MDPs, and instead of using the approximate likelihood of the final sample, these algorithms use the exact likelihood of each denoising step, which is extremely easy to compute.

**Policy Gradient Methods**: Policy gradient algorithms were chosen due to their ease of implementation and past success in language model finetuning, leading to two variants of DDPO: DDPOSF, which uses the simple score function estimator (REINFORCE); and DDPOIS, which uses a more powerful importance sampled estimator.

**Adaptive Denoising Steps**: Research has explored dynamic approaches to denoising. Work on D3P (Dynamic Denoising Diffusion Policy) jointly optimizes an adaptor and base diffusion policy via reinforcement learning to balance task performance and inference efficiency.

**Computational Efficiency**: DDPO implementations using PyTorch with LoRA can finetune Stable Diffusion with less than 10GB of GPU memory.

The search results focus primarily on the DDPO framework rather than detailed compute budget and training cost comparisons across different methods. If you need more specific information about computational costs or comparative analyses, I can perform additional searches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fbc9dce-764a-4b7b-890f-b5aab78e840f",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "c5877e22-413c-4ebd-ad3a-06f23c333b0e",
  "sourceToolAssistantUUID": "1fbc9dce-764a-4b7b-890f-b5aab78e840f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-10T18:43:10.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWPPhePSBx74dyCQSiAfkj`</summary>

```json
{
  "query": "LIBERO benchmark 130 tasks total demonstrations dataset size GB storage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5877e22-413c-4ebd-ad3a-06f23c333b0e",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP3gRAiGm8zKYbwNaWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0410463-581b-486f-b504-c0d1b3080d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYPjCrz26FE9vLHAJSiPDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 27137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 948,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T18:43:15.278Z_

<details><summary>↩ Tool result · `toolu_01GWPPhePSBx74dyCQSiAfkj`</summary>

```text
Web search results for query: "LIBERO benchmark 130 tasks total demonstrations dataset size GB storage"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3668061"}]

Based on the search results, I can provide you with information about the LIBERO benchmark:

## LIBERO Benchmark Overview

LIBERO comprises 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

To support efficient learning, LIBERO provides high-quality, human-teleoperated demonstration data for all 130 tasks. More specifically, each task utilizes human-teleoperated demonstrations (typically 50 per task) to provide ground truth and training signals for imitation learning.

## Dataset Storage Size

Unfortunately, the search results do not contain specific information about the total dataset size in GB or storage requirements for the LIBERO benchmark demonstrations. While the sources confirm that demonstration data is available and can be downloaded, they do not specify the exact storage size needed for the complete dataset.

If you need this specific information, you might want to check the official LIBERO project repository or HuggingFace datasets page directly, as they would have detailed storage specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0410463-581b-486f-b504-c0d1b3080d90",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "b98bdc8d-eb7d-4696-8229-f90ff2923101",
  "sourceToolAssistantUUID": "e0410463-581b-486f-b504-c0d1b3080d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T18:43:18.227Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BSHjV7vk9FXGHS6p2F4hNv`</summary>

```json
{
  "query": "DreamZero pretrained checkpoint huggingface GEAR-Dreams model size parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98bdc8d-eb7d-4696-8229-f90ff2923101",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP4Gifsv1hoHu3GRtAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff3ad76d-2a0c-4608-a24a-f45478b09e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7DH9qov8erT98RBoVBZ93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 28085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 867,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T18:43:24.927Z_

<details><summary>↩ Tool result · `toolu_01BSHjV7vk9FXGHS6p2F4hNv`</summary>

```text
Web search results for query: "DreamZero pretrained checkpoint huggingface GEAR-Dreams model size parameters"

Links: [{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"GEAR-Dreams/DreamZero-DROID · Hugging Face","url":"https://huggingface.co/GEAR-Dreams/DreamZero-DROID"},{"title":"dreamzero/README.md at main · dreamzero0/dreamzero","url":"https://github.com/dreamzero0/dreamzero/blob/main/README.md"},{"title":"dreamzero0/dreamzero | DeepWiki","url":"https://deepwiki.com/dreamzero0/dreamzero"},{"title":"Loading models · Hugging Face","url":"https://huggingface.co/docs/transformers/en/models"},{"title":"Configuration · Hugging Face","url":"https://huggingface.co/docs/transformers/main_classes/configuration"},{"title":"Models · Hugging Face","url":"https://huggingface.co/docs/transformers/main_classes/model"},{"title":"Initialize a model with 100 billions parameters in no time and without using any RAM. · Hugging Face","url":"https://huggingface.co/docs/accelerate/v0.11.0/en/big_modeling"},{"title":"PEFT checkpoint format · Hugging Face","url":"https://huggingface.co/docs/peft/developer_guides/checkpoint"},{"title":"Model Loading and Weight Management | huggingface/transformers | DeepWiki","url":"https://deepwiki.com/huggingface/transformers/2.2-model-loading-and-pretrainedmodel"}]

Based on the search results, I found information about the DreamZero pretrained checkpoint:

## DreamZero-DROID Model Information

DreamZero-DROID is a 14B parameter World Action Model (WAM) checkpoint trained from scratch using only the DROID dataset.

### Model Size and Parameters
- **Model Parameters:** 14 billion parameters trained on multi-embodiment robot demonstration data
- **Checkpoint Size:** The pretrained DreamZero-AgiBot checkpoint is approximately 45GB

### Architecture Details
The architecture is a World Action Model (WAM) built upon a pretrained video diffusion backbone (Wan2.1-I2V-14B-480P).

### Available on Hugging Face
The model is available through the GEAR-Dreams organization on Hugging Face under the repository name `GEAR-Dreams/DreamZero-DROID`. To download the checkpoint, run: hf download GEAR-Dreams/DreamZero-DROID --repo-type model --local-dir

### Performance
Through model and system optimizations (DreamZero-Flash), this 14B model is capable of real-time closed-loop control at ~7Hz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff3ad76d-2a0c-4608-a24a-f45478b09e46",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "01e0e220-8713-4514-a959-f2ab3405f18d",
  "sourceToolAssistantUUID": "ff3ad76d-2a0c-4608-a24a-f45478b09e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-10T18:43:34.838Z_

Now let me fetch the D3P paper directly to find the training compute details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01e0e220-8713-4514-a959-f2ab3405f18d",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP4z4LgNupNHw1GqzR8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7970397a-f68e-4cea-9f03-c259ce4af2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167CyrV5UJpNbczJvZk5HRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 836,
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

_source line 49 · 2026-05-10T18:43:36.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0123NEQCQqNwAMdNGKz8JjMA`</summary>

```json
{
  "query": "site:arxiv.org D3P \"Dynamic Denoising Diffusion Policy\" training \"single GPU\" OR \"GPU hours\" OR \"training takes\" OR \"wall-clock\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7970397a-f68e-4cea-9f03-c259ce4af2c3",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP4z4LgNupNHw1GqzR8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5271b92d-10b4-4dc4-9add-3b0cafb3b2db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167CyrV5UJpNbczJvZk5HRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28952,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 28952,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 836,
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

_source line 50 · 2026-05-10T18:43:42.609Z_

<details><summary>↩ Tool result · `toolu_0123NEQCQqNwAMdNGKz8JjMA`</summary>

```text
Web search results for query: "site:arxiv.org D3P "Dynamic Denoising Diffusion Policy" training "single GPU" OR "GPU hours" OR "training takes" OR "wall-clock""

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://arxiv.org/pdf/2508.06804"},{"title":"Improving Robustness to Out-of-Distribution States in Imitation Learning via Deep Koopman-Boosted Diffusion Policy","url":"https://arxiv.org/html/2511.00555"},{"title":"3D Diffusion Policy","url":"https://arxiv.org/html/2403.03954v1"},{"title":"Mini Diffuser: Train a Multi-Task Diffusion Policy on RLBench-18 in One Day with One GPU","url":"https://arxiv.org/html/2505.09430v1"},{"title":"[2311.13231] Using Human Feedback to Fine-tune Diffusion Models without Any Reward Model","url":"https://arxiv.org/abs/2311.13231"},{"title":"[2010.02502] Denoising Diffusion Implicit Models","url":"https://arxiv.org/abs/2010.02502"},{"title":"[2107.03006] Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/abs/2107.03006"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces","url":"https://arxiv.org/pdf/2107.03006"}]

Based on the search results, I found information about the D3P (Dynamic Denoising Diffusion Policy) paper from arxiv.org. However, the search results do not contain specific information about training costs such as single GPU requirements, GPU hours, training duration, or wall-clock time for the D3P model.

The search results show that the paper focuses on Dynamic Denoising Diffusion Policy (D3P), a diffusion-based policy that adaptively allocates denoising steps across actions at test time, and discusses inference efficiency rather than training costs. The available information mentions inference performance metrics like achieving an average 2.2× inference speed-up over baseline methods, but does not include the specific training computational requirements you're looking for.

The paper (arXiv:2508.06804) was published in August 2025, but the specific sections containing training time or GPU requirements do not appear in the available search results. You may need to check the full paper PDF directly or look for these details in the appendix or supplementary materials.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5271b92d-10b4-4dc4-9add-3b0cafb3b2db",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "4db53bf7-49ea-4cb8-9868-0604dd09867f",
  "sourceToolAssistantUUID": "5271b92d-10b4-4dc4-9add-3b0cafb3b2db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T18:43:46.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMSdbXebRhBt37Ufcy9mQt`</summary>

```json
{
  "query": "\"Mini Diffuser\" train diffusion policy one day one GPU RLBench compute"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db53bf7-49ea-4cb8-9868-0604dd09867f",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP6Haoy2dttCCsb4oh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a06236d-5dab-499f-9686-06039df72913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9RT9xjGF7qsHB9sahP8So",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 29788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 845,
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

### Tool result

_source line 52 · 2026-05-10T18:43:52.690Z_

<details><summary>↩ Tool result · `toolu_01AMSdbXebRhBt37Ufcy9mQt`</summary>

```text
Web search results for query: ""Mini Diffuser" train diffusion policy one day one GPU RLBench compute"

Links: [{"title":"Mini Diffuser: Train a Multi-Task Diffusion Policy on RLBench-18 in One Day with One GPU","url":"https://arxiv.org/html/2505.09430v1"},{"title":"Paper page - Train a Multi-Task Diffusion Policy on RLBench-18 in One Day with One GPU","url":"https://huggingface.co/papers/2505.09430"},{"title":"[Literature Review] Train a Multi-Task Diffusion Policy on RLBench-18 in One Day with One GPU","url":"https://www.themoonlight.io/en/review/train-a-multi-task-diffusion-policy-on-rlbench-18-in-one-day-with-one-gpu"},{"title":"Mini Diffuser: Fast Multi-task Diffusion Policy Training Using Two-level Mini-batches","url":"https://arxiv.org/html/2505.09430v2"},{"title":"GitHub - utomm/mini-diffuse-actor","url":"https://github.com/utomm/mini-diffuse-actor"},{"title":"Mini Diffuser: Fast Multi-task Diffusion Policy Training Using Two-level Mini-batches | alphaXiv","url":"https://www.alphaxiv.org/resources/2505.09430v2"},{"title":"Mini Diffuser: Fast Multi-task Diffusion Policy Training Using Two-level Mini-batches","url":"https://mini-diffuse-actor.github.io/"},{"title":"[2505.09430] Mini Diffuser: Fast Multi-task Diffusion Policy Training Using Two-level Mini-batches","url":"https://arxiv.org/abs/2505.09430"},{"title":"RVT-2: Learning Precise Manipulation from Few Demonstrations | Request PDF","url":"https://www.researchgate.net/publication/383893568_RVT-2_Learning_Precise_Manipulation_from_Few_Demonstrations"},{"title":"Mini-diffuser reduces by an order of magnitude the time and memory needed to train multi-task vision-language robotic diffusion policies! | Renaud Detry","url":"https://renaud-detry.net/news/2025-06-09--mini-diffuser/"}]

Based on the search results, here's what I found about Mini Diffuser:

## Overview

Mini Diffuser is a method for training multi-task vision-language robotic diffusion policies that reduces training time and memory usage by an order of magnitude.

## Key Innovation

The method recognizes a distinction between action diffusion and image diffusion: image generation targets are high-dimensional, while robot actions lie in a much lower-dimensional space. Meanwhile, the vision-language conditions for action generation remain high-dimensional. Mini-Diffuser exploits this asymmetry by introducing Level-2 minibatching, which pairs multiple noised action samples with each vision-language condition, instead of the conventional one-to-one sampling strategy.

## Performance and Compute Requirements

Mini-Diffuser reaches 95.6% of the average task performance of 3D Diffuse Actor using only 4.8% of its training time and 6.6% of its memory consumption. 

The model can be trained end-to-end on a consumer-level GPU, such as an RTX 4090, in just 13 hours—while existing diffusion and non-diffusion methods typically require multiple GPUs and days of training.

## Benchmark Results

Mini-Diffuser is evaluated on the multi-task RLBench benchmark consisting of 18 tasks and 249 task variations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a06236d-5dab-499f-9686-06039df72913",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a3ef468e6e9bc3aab",
  "type": "user",
  "uuid": "43d819c2-4c62-40be-b56e-1e5b38a18d3e",
  "sourceToolAssistantUUID": "1a06236d-5dab-499f-9686-06039df72913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-10T18:44:48.154Z_

Now I have enough information to compile a comprehensive report. Here is my analysis:

---

## Compute Feasibility Analysis: PPO-based Policy for Adaptive Denoising Step Allocation

### 1. Comparable RL-for-Diffusion-Control Methods and Their Compute

**DDPO (Denoising Diffusion Policy Optimization):** The original RL-for-diffusion method from Berkeley. Their PyTorch+LoRA implementation runs with <10GB GPU memory for finetuning Stable Diffusion. However, DDPO operates on image generation (Stable Diffusion), not robotics control, and doesn't provide specific GPU-hour totals.

**DPPO (Diffusion Policy Policy Optimization, ICLR 2025):** The closest comparable method for RL fine-tuning of diffusion-based robot policies. DPPO uses parallelized MuJoCo environments (40-50 envs on CPU) with a single GPU for Furniture-Bench tasks via IsaacGym. Unfortunately, the paper does not publicly report specific wall-clock GPU hours. However, it's notable that DPPO successfully fine-tunes diffusion policies to >90% success on challenging manipulation tasks using a single GPU setup.

**D3P (Dynamic Denoising Diffusion Policy, arXiv 2508.06804):** This is the most directly comparable prior work -- it uses PPO to train a lightweight adaptor that predicts noise-level strides (i.e., adaptive step allocation), jointly optimized with a DPPO-finetuned base diffusion policy. The D3P adaptor is similar in spirit to the proposed 15M policy network. Inference was validated on a consumer-grade desktop (i7-12900K, RTX 2080). The paper does **not** report explicit training GPU hours in the abstract/main body. The adaptor is described as "lightweight."

**Mini Diffuser:** For reference on diffusion policy training budgets, Mini Diffuser trains a multi-task diffusion policy on RLBench-18 (18 tasks, 249 variations) in **13 hours on a single RTX 4090**, reaching 95.6% of the full-budget baseline's performance. This demonstrates that diffusion policy training at the robotics scale can be done in tens of GPU-hours, not hundreds.

### 2. AdaDiff Training Cost

**AdaDiff (AAAI 2025)** trains a lightweight step-selection policy using policy gradient methods. Their reported training cost is **16 to 80 A100 GPU-hours** depending on the base diffusion model. This is a strong reference point for RL-based step predictor training. The proposed budget of 60-80 H100-hours for PPO training of a 15M policy network is in the same ballpark as AdaDiff's upper range on A100s, which is plausible given that H100s are roughly 2-3x faster than A100s for training workloads.

### 3. LIBERO Dataset

- **130 language-conditioned manipulation tasks** across 4 suites: LIBERO-Spatial (10 tasks), LIBERO-Object (10 tasks), LIBERO-Goal (10 tasks), LIBERO-100 (100 tasks)
- **50 human-teleoperated demonstrations per task**, totaling approximately **6,500 trajectories** across all 130 tasks
- For the commonly used LIBERO-90 subset: **4,500 trajectories** (90 tasks x 50 demos)
- Evaluation protocol: 10 episodes per task
- **Publicly available**: hosted on [HuggingFace](https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets) and downloadable via the official [GitHub repo](https://github.com/Lifelong-Robot-Learning/LIBERO) script
- Published at NeurIPS 2023 (Datasets & Benchmarks track)

### 4. UWM (Unified World Models) Availability

- **Code: publicly available** at [github.com/WEIRDLabUW/unified-world-model](https://github.com/WEIRDLabUW/unified-world-model)
- **Pretrained checkpoints: available** -- the authors release pretrained and cotrained DROID UWM checkpoints, plus a pretrained LIBERO-90 checkpoint, all downloadable for direct finetuning
- Published at RSS 2025
- UWM is a multimodal diffusion transformer with separate diffusion timesteps for actions and videos, pretrained on a subset of the DROID dataset
- Shell scripts for DROID pretraining/cotraining/finetuning are provided in the repo

### 5. DreamZero Availability

- **Code: publicly available** at [github.com/dreamzero0/dreamzero](https://github.com/dreamzero0/dreamzero) (released 02/20)
- **Pretrained checkpoint: available** on HuggingFace at [GEAR-Dreams/DreamZero-DROID](https://huggingface.co/GEAR-Dreams/DreamZero-DROID)
- **14B parameter** World Action Model built on Wan2.1-I2V-14B-480P video diffusion backbone
- Checkpoint size: ~45GB
- DreamZero-AgiBot checkpoint and post-training code released 02/27
- Preprocessed DROID dataset also available on HuggingFace
- Runs real-time closed-loop control at ~7Hz using 2x GB200s

### 6. Feasibility Assessment of the 130-180 H100-hour Budget

| Component | Claimed Budget | Assessment |
|-----------|---------------|------------|
| Teacher cache (frozen WAM full-step inference on training data) | 20-30h H100 | **Plausible.** LIBERO has ~4,500-6,500 trajectories. Running a frozen diffusion model at full denoising steps on this data is essentially batch inference, not training. 20-30h on H100 is reasonable for this scale. |
| PPO training of 15M policy | 60-80h H100 | **Plausible but on the higher end.** AdaDiff's comparable step-predictor training costs 16-80 A100-hours. Given H100 is 2-3x faster than A100, the equivalent would be roughly 5-40 H100-hours. 60-80h H100 seems generous/conservative, which could be justified if the reward computation requires running the frozen WAM for each PPO rollout (expensive forward passes through a large model). If WAM forward passes are needed during PPO training (not just pre-cached), this budget makes more sense. |
| Evaluation and ablations | 40-55h | **Plausible.** Multiple ablation runs, different step-allocation strategies, evaluations across LIBERO suites -- this is a reasonable buffer. |
| **Total** | **130-180h H100** | **Reasonable overall.** The budget appears conservative but defensible. The main cost driver is likely WAM forward passes during PPO training, not the 15M policy network itself. |

**Key risk to flag:** The feasibility hinges on whether PPO rollouts require live WAM forward passes (expensive) or can rely entirely on the pre-computed teacher cache (cheap). If the policy needs to evaluate new step-allocation strategies during training by actually running the WAM with different step counts, the 60-80h PPO budget becomes tighter. If teacher-cache suffices, the PPO budget is generous.

Sources:
- [DDPO - Training Diffusion Models with RL (BAIR Blog)](https://bair.berkeley.edu/blog/2023/07/14/ddpo/)
- [DPPO - Diffusion Policy Policy Optimization](https://diffusion-ppo.github.io/)
- [DPPO GitHub](https://github.com/irom-princeton/dppo)
- [D3P: Dynamic Denoising Diffusion Policy (arXiv)](https://arxiv.org/abs/2508.06804)
- [AdaDiff: Adaptive Step Selection (arXiv)](https://arxiv.org/abs/2311.14768)
- [LIBERO Benchmark GitHub](https://github.com/Lifelong-Robot-Learning/LIBERO)
- [LIBERO Datasets on HuggingFace](https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets)
- [UWM GitHub](https://github.com/WEIRDLabUW/unified-world-model)
- [UWM Project Page](https://weirdlabuw.github.io/uwm/)
- [DreamZero GitHub](https://github.com/dreamzero0/dreamzero)
- [DreamZero-DROID on HuggingFace](https://huggingface.co/GEAR-Dreams/DreamZero-DROID)
- [DreamZero Project Page](https://dreamzero0.github.io/)
- [Mini Diffuser (arXiv)](https://arxiv.org/abs/2505.09430)
- [HuggingFace TRL DDPO Trainer](https://huggingface.co/docs/trl/ddpo_trainer)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43d819c2-4c62-40be-b56e-1e5b38a18d3e",
  "isSidechain": true,
  "agentId": "a3ef468e6e9bc3aab",
  "requestId": "req_011CauP72fQtZdHs1yNBTAwB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c907803-40ad-4283-b238-258dae4b763b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyxxRJtYwpySMgs4LwBsDy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 30633,
      "output_tokens": 2229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 971
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2229,
          "cache_read_input_tokens": 30633,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 971,
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
